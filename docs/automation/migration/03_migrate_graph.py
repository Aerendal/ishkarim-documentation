#!/usr/bin/env python3
"""
Living Documentation Framework - Graph Migration

Migrates dependency relationships to create the document graph.

Features:
- Extracts dependencies and impacts from documents
- Creates bidirectional edges (requires/informs relationship)
- Handles supersedes edges for deprecated documents
- Validates edge integrity (both nodes must exist)
- Detects and reports broken references

Usage:
    python 03_migrate_graph.py
"""

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import List, Dict, Any, Set, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from document_parser import DocumentParser


class GraphMigrator:
    """Migrates dependency graph to database"""

    def __init__(self, db_path: Path, base_path: Path):
        """
        Initialize graph migrator

        Args:
            db_path: Path to SQLite database
            base_path: Base directory for documents
        """
        self.db_path = db_path
        self.base_path = base_path
        self.parser = DocumentParser(base_path)
        self.conn: sqlite3.Connection = None

        # Track statistics
        self.edges_created = 0
        self.broken_refs = []
        self.supersedes_edges = []

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def get_all_document_ids(self) -> Set[str]:
        """Get set of all document IDs in database"""
        cursor = self.conn.execute("SELECT id FROM documents")
        return {row['id'] for row in cursor}

    def parse_metadata(self, metadata_json: str) -> Dict[str, Any]:
        """Parse metadata JSON from database"""
        return json.loads(metadata_json) if metadata_json else {}

    def create_edge(self, from_id: str, to_id: str, edge_type: str, reason: str = None, cascade: bool = False) -> bool:
        """
        Create an edge in the graph

        Args:
            from_id: Source document ID
            to_id: Target document ID
            edge_type: Type of edge (requires, informs, blocks, supersedes)
            reason: Optional reason for this edge
            cascade: Whether changes should cascade

        Returns:
            True if edge was created, False if it already exists
        """
        try:
            self.conn.execute("""
                INSERT INTO edges (from_id, to_id, edge_type, reason, cascade)
                VALUES (?, ?, ?, ?, ?)
            """, (from_id, to_id, edge_type, reason, 1 if cascade else 0))

            self.edges_created += 1
            return True

        except sqlite3.IntegrityError as e:
            # Edge already exists (UNIQUE constraint)
            if "UNIQUE constraint failed" in str(e):
                return False
            # Foreign key constraint (document doesn't exist)
            elif "FOREIGN KEY constraint failed" in str(e):
                self.broken_refs.append((from_id, to_id, edge_type))
                return False
            else:
                raise

    def migrate_document_edges(self, doc_id: str, metadata: Dict[str, Any]) -> int:
        """
        Migrate edges for a single document

        Args:
            doc_id: Document ID
            metadata: Parsed metadata dictionary

        Returns:
            Number of edges created
        """
        edges_count = 0

        # 1. Dependencies → "requires" edges (upstream)
        # Format: doc_id REQUIRES dependency
        dependencies = metadata.get('dependencies') or []
        for dep in dependencies:
            # Handle both string IDs and dict format
            dep_id = dep.get('id') if isinstance(dep, dict) else dep

            if dep_id and self.create_edge(
                from_id=doc_id,
                to_id=dep_id,
                edge_type='requires',
                reason='dependency',
                cascade=True  # Upstream changes should cascade
            ):
                edges_count += 1

        # 2. Impacts → "informs" edges (downstream)
        # Format: doc_id INFORMS impact
        impacts = metadata.get('impacts') or []
        for impact in impacts:
            # Handle both string IDs and dict format
            impact_id = impact.get('id') if isinstance(impact, dict) else impact

            if impact_id and self.create_edge(
                from_id=doc_id,
                to_id=impact_id,
                edge_type='informs',
                reason='downstream impact',
                cascade=False  # Informational only
            ):
                edges_count += 1

        # 3. Supersedes → "supersedes" edges (deprecation)
        # Get from living_doc_metadata table
        cursor = self.conn.execute("""
            SELECT superseded_by FROM living_doc_metadata
            WHERE doc_id = ? AND superseded_by IS NOT NULL
        """, (doc_id,))

        row = cursor.fetchone()
        if row and row['superseded_by']:
            if self.create_edge(
                from_id=row['superseded_by'],  # New doc supersedes old doc
                to_id=doc_id,
                edge_type='supersedes',
                reason='deprecated document replaced',
                cascade=False
            ):
                edges_count += 1
                self.supersedes_edges.append((row['superseded_by'], doc_id))

        return edges_count

    def migrate_all_edges(self) -> Dict[str, Any]:
        """
        Migrate all edges from all documents

        Returns:
            Migration report
        """
        print(f"\n{'='*80}")
        print("MIGRATING DEPENDENCY GRAPH")
        print(f"{'='*80}\n")

        # Get all documents
        cursor = self.conn.execute("""
            SELECT id, metadata_json FROM documents ORDER BY id
        """)

        documents = cursor.fetchall()

        print(f"Found {len(documents)} documents\n")
        print(f"{'-'*80}")

        # Migrate edges for each document
        for doc in documents:
            doc_id = doc['id']
            metadata = self.parse_metadata(doc['metadata_json'])

            edges_count = self.migrate_document_edges(doc_id, metadata)

            if edges_count > 0:
                print(f"  {doc_id:25s} → {edges_count:3d} edges")

        self.conn.commit()

        # Report
        report = {
            'total_documents': len(documents),
            'total_edges': self.edges_created,
            'broken_references': len(self.broken_refs),
            'supersedes_edges': len(self.supersedes_edges),
            'broken_refs_list': self.broken_refs,
            'supersedes_list': self.supersedes_edges
        }

        print(f"\n{'-'*80}")
        print("MIGRATION COMPLETE")
        print(f"{'-'*80}")
        print(f"  Documents processed: {len(documents)}")
        print(f"  ✓ Edges created:     {self.edges_created}")
        print(f"  ⚠ Broken references: {len(self.broken_refs)}")
        print(f"  ↻ Supersedes edges:  {len(self.supersedes_edges)}")

        if self.broken_refs:
            print(f"\n  Broken references:")
            for from_id, to_id, edge_type in self.broken_refs:
                print(f"    {from_id:25s} → {to_id:25s} ({edge_type})")

        if self.supersedes_edges:
            print(f"\n  Supersedes relationships:")
            for new_id, old_id in self.supersedes_edges:
                print(f"    {new_id:25s} supersedes {old_id}")

        print()

        return report

    def calculate_node_metrics(self):
        """Calculate and store node metrics (degree, centrality, etc.)"""
        print(f"\n{'='*80}")
        print("CALCULATING GRAPH METRICS")
        print(f"{'='*80}\n")

        # Calculate in-degree and out-degree for each node
        cursor = self.conn.execute("""
            SELECT id FROM documents ORDER BY id
        """)

        nodes = cursor.fetchall()

        for node in nodes:
            node_id = node['id']

            # In-degree (how many edges point TO this node)
            in_degree = self.conn.execute("""
                SELECT COUNT(*) as count FROM edges WHERE to_id = ?
            """, (node_id,)).fetchone()['count']

            # Out-degree (how many edges point FROM this node)
            out_degree = self.conn.execute("""
                SELECT COUNT(*) as count FROM edges WHERE from_id = ?
            """, (node_id,)).fetchone()['count']

            # Insert or update node metrics
            self.conn.execute("""
                INSERT OR REPLACE INTO nodes (id, in_degree, out_degree)
                VALUES (?, ?, ?)
            """, (node_id, in_degree, out_degree))

        self.conn.commit()

        print(f"✓ Calculated metrics for {len(nodes)} nodes\n")


def main():
    parser = argparse.ArgumentParser(
        description="Living Documentation Framework - Graph Migration"
    )

    args = parser.parse_args()

    # Paths
    base_path = Path(__file__).parent.parent.parent  # docs/
    db_path = base_path / ".semantic-docs" / "index.db"

    if not db_path.exists():
        print(f"ERROR: Database not found at {db_path}", file=sys.stderr)
        print("Run document migration first.", file=sys.stderr)
        sys.exit(1)

    # Migrate
    migrator = GraphMigrator(db_path, base_path)
    migrator.connect()

    try:
        # Migrate edges
        report = migrator.migrate_all_edges()

        # Calculate node metrics
        migrator.calculate_node_metrics()

        # Save report
        from datetime import datetime
        report_file = Path(__file__).parent / f"graph-migration-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'report': report
            }, f, indent=2, ensure_ascii=False)

        print(f"✓ Graph migration report saved to: {report_file}\n")

    finally:
        migrator.close()


if __name__ == "__main__":
    main()
