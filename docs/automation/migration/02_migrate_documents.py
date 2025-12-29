#!/usr/bin/env python3
"""
Living Documentation Framework - Document Migration

Migrates markdown documents with YAML frontmatter to SQLite database.

Features:
- Batch processing (A: Living Docs, B: Core, C: Satellites)
- SHA256 content hashing for change detection
- Living Documentation metadata extraction
- Version history migration
- FTS5 full-text indexing
- Provenance tracking

Usage:
    python 02_migrate_documents.py --batch A  # Migrate Living Docs
    python 02_migrate_documents.py --batch B  # Migrate Core Docs
    python 02_migrate_documents.py --batch C  # Migrate Satellites
    python 02_migrate_documents.py --all      # Migrate all batches
"""

import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path
from datetime import datetime, date
from typing import List, Dict, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from document_parser import DocumentParser, Document


class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder that handles date and datetime objects"""
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)


class DocumentMigrator:
    """Migrates documents from markdown to SQLite database"""

    def __init__(self, db_path: Path, base_path: Path):
        """
        Initialize document migrator

        Args:
            db_path: Path to SQLite database
            base_path: Base directory for documents
        """
        self.db_path = db_path
        self.base_path = base_path
        self.parser = DocumentParser(base_path)
        self.conn: Optional[sqlite3.Connection] = None

        # Load categorization
        categorization_file = Path(__file__).parent / "categorization-report.json"
        with open(categorization_file) as f:
            self.categorization = json.load(f)

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of file contents"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def migrate_document(self, doc: Document) -> bool:
        """
        Migrate a single document to database

        Args:
            doc: Document to migrate

        Returns:
            True if successful, False otherwise
        """
        try:
            file_rel = str(doc.file_path.relative_to(self.base_path))

            # Calculate content hash
            content_hash = self.calculate_hash(doc.file_path)

            # 1. INSERT into documents table
            self.conn.execute("""
                INSERT OR REPLACE INTO documents (
                    id, file_path, doc_type, status, title, domain,
                    created_at, updated_at, owner, content_hash, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                doc.id,
                file_rel,
                doc.type,
                doc.status,
                doc.title,
                doc.domain,
                doc.created,
                doc.updated,
                doc.owner,
                content_hash,
                json.dumps(doc.front_matter, ensure_ascii=False, cls=DateTimeEncoder)
            ))

            # 2. INSERT into living_doc_metadata (if applicable)
            if doc.has_living_doc_metadata:
                self._migrate_living_metadata(doc)

            # 3. INSERT into version_history
            if doc.version_history:
                self._migrate_version_history(doc)

            # 4. INSERT into documents_fts (full-text search)
            # FTS5 is populated via trigger, but we can manually update body
            # For now, body will be empty (can be populated by separate script)

            # 5. Record provenance
            self._record_provenance(doc.id, 'migrated', 'migration-script')

            self.conn.commit()
            return True

        except Exception as e:
            print(f"  ✗ ERROR migrating {doc.id}: {e}", file=sys.stderr)
            self.conn.rollback()
            return False

    def _migrate_living_metadata(self, doc: Document):
        """Migrate Living Documentation metadata"""
        lifecycle = doc.lifecycle or {}
        deprecation = doc.deprecation or {}

        # Extract version components
        version_major = doc.major_version
        version_minor = doc.minor_version
        version_patch = doc.patch_version

        # Health status
        health_status = doc.health_status if doc.document_health else None
        health_checks_json = json.dumps(doc.document_health, ensure_ascii=False, cls=DateTimeEncoder) if doc.document_health else None

        self.conn.execute("""
            INSERT OR REPLACE INTO living_doc_metadata (
                doc_id, version, version_major, version_minor, version_patch,
                lifecycle_created, lifecycle_first_approved, lifecycle_last_modified,
                lifecycle_deprecated, lifecycle_sunset,
                health_status, health_checks_json,
                is_deprecated, superseded_by, deprecation_reason, sunset_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            doc.id,
            doc.version,
            version_major,
            version_minor,
            version_patch,
            lifecycle.get('created'),
            lifecycle.get('first_approved'),
            lifecycle.get('last_modified'),
            lifecycle.get('deprecated'),
            lifecycle.get('sunset'),
            health_status,
            health_checks_json,
            1 if doc.is_deprecated else 0,
            deprecation.get('superseded_by') if deprecation else None,
            deprecation.get('reason') if deprecation else None,
            deprecation.get('sunset_date') if deprecation else None
        ))

    def _migrate_version_history(self, doc: Document):
        """Migrate version history entries"""
        for version_entry in doc.version_history:
            self.conn.execute("""
                INSERT INTO version_history (
                    doc_id, version, version_date, author, change_type,
                    summary, breaking, changes_json, impacts_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                doc.id,
                version_entry.get('version'),
                version_entry.get('date'),
                version_entry.get('author'),
                version_entry.get('type'),
                version_entry.get('summary'),
                1 if version_entry.get('breaking') else 0,
                json.dumps(version_entry.get('changes', []), ensure_ascii=False, cls=DateTimeEncoder),
                json.dumps(version_entry.get('impacts', []), ensure_ascii=False, cls=DateTimeEncoder)
            ))

    def _record_provenance(self, doc_id: str, action: str, actor: str, details: Optional[Dict] = None):
        """Record provenance entry"""
        self.conn.execute("""
            INSERT INTO provenance (doc_id, action, actor, details)
            VALUES (?, ?, ?, ?)
        """, (
            doc_id,
            action,
            actor,
            json.dumps(details, ensure_ascii=False, cls=DateTimeEncoder) if details else None
        ))

    def migrate_batch(self, batch: str) -> Dict[str, Any]:
        """
        Migrate a batch of documents

        Args:
            batch: Batch identifier ('A', 'B', or 'C')

        Returns:
            Migration report
        """
        batch_map = {
            'A': 'batch_a_living_docs',
            'B': 'batch_b_core',
            'C': 'batch_c_satellites'
        }

        if batch not in batch_map:
            raise ValueError(f"Invalid batch: {batch}. Must be A, B, or C")

        batch_key = batch_map[batch]
        batch_data = self.categorization[batch_key]
        document_list = batch_data['documents']

        print(f"\n{'='*80}")
        print(f"MIGRATING BATCH {batch}: {batch_data['count']} documents")
        print(f"{'='*80}\n")

        success_count = 0
        failed_count = 0
        failed_docs = []

        for doc_info in document_list:
            file_path = self.base_path / doc_info['file']

            try:
                # Parse document
                doc = self.parser.parse(file_path)

                # Migrate
                print(f"  Migrating {doc.id:20s} ({doc.type:15s}) ... ", end='', flush=True)

                if self.migrate_document(doc):
                    print("✓")
                    success_count += 1
                else:
                    print("✗")
                    failed_count += 1
                    failed_docs.append(doc.id)

            except Exception as e:
                print(f"✗ ERROR: {e}")
                failed_count += 1
                failed_docs.append(doc_info['id'])

        # Report
        report = {
            'batch': batch,
            'total': batch_data['count'],
            'success': success_count,
            'failed': failed_count,
            'failed_docs': failed_docs
        }

        print(f"\n{'─'*80}")
        print(f"Batch {batch} migration complete:")
        print(f"  ✓ Success: {success_count}/{batch_data['count']}")
        print(f"  ✗ Failed:  {failed_count}/{batch_data['count']}")
        if failed_docs:
            print(f"  Failed documents: {', '.join(failed_docs)}")
        print()

        return report

    def migrate_all(self) -> List[Dict[str, Any]]:
        """Migrate all batches"""
        reports = []
        for batch in ['A', 'B', 'C']:
            report = self.migrate_batch(batch)
            reports.append(report)

        # Summary
        total_success = sum(r['success'] for r in reports)
        total_failed = sum(r['failed'] for r in reports)
        total_docs = sum(r['total'] for r in reports)

        print(f"\n{'='*80}")
        print("MIGRATION COMPLETE - ALL BATCHES")
        print(f"{'='*80}")
        print(f"  Total documents:  {total_docs}")
        print(f"  ✓ Success:        {total_success}")
        print(f"  ✗ Failed:         {total_failed}")
        print()

        return reports


def main():
    parser = argparse.ArgumentParser(
        description="Living Documentation Framework - Document Migration"
    )
    parser.add_argument(
        "--batch",
        choices=['A', 'B', 'C'],
        help="Batch to migrate (A: Living Docs, B: Core, C: Satellites)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Migrate all batches (A, B, C)"
    )

    args = parser.parse_args()

    if not args.batch and not args.all:
        parser.error("Must specify --batch or --all")

    # Paths
    base_path = Path(__file__).parent.parent.parent  # docs/
    db_path = base_path / ".semantic-docs" / "index.db"

    if not db_path.exists():
        print(f"ERROR: Database not found at {db_path}", file=sys.stderr)
        print("Run 01_create_schema.sql first to create the database.", file=sys.stderr)
        sys.exit(1)

    # Migrate
    migrator = DocumentMigrator(db_path, base_path)
    migrator.connect()

    try:
        if args.all:
            reports = migrator.migrate_all()
        else:
            report = migrator.migrate_batch(args.batch)
            reports = [report]

        # Save reports
        report_file = Path(__file__).parent / f"migration-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'reports': reports
            }, f, indent=2, ensure_ascii=False)

        print(f"✓ Migration report saved to: {report_file}")

    finally:
        migrator.close()


if __name__ == "__main__":
    main()
