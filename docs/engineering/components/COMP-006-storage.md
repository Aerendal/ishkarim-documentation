---
id: COMP-006
title: "COMP-006: Hybrid Storage Component"
type: component
status: draft
parent: TDD-001-V2

dependencies:
  - id: "ADR-005"
    type: requires
    reason: "Implements hybrid storage (ADR-005 decision)"

  - id: "ADR-002"
    type: requires
    reason: "Uses Watchdog for file monitoring (ADR-002 decision)"

  - id: "COMP-001-parser"
    type: requires
    reason: "Stores parsed Document objects"

  - id: "API-SPEC-001"
    type: implements
    reason: "Storage implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

evidence_ids:
  - "E-146"  # SQLite FTS5 benchmark (60ms search dla 10k docs)
  - "E-158"  # Hybrid storage prototype
  - "E-162"  # Watchdog reliability benchmark (99.9%)
---

# COMP-006: Hybrid Storage Component

**Responsibility**: Hybrid storage (Markdown files + SQLite index), file monitoring, cache invalidation, provenance tracking

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Application Layer                    │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ↓
┌─────────────────────────────────────────────────────────┐
│              Storage API (Facade)                       │
│  - get_document(doc_id)                                 │
│  - search_documents(query)                              │
│  - save_document(doc)                                   │
└─────┬───────────────────────────────────────────┬───────┘
      │                                           │
      ↓                                           ↓
┌──────────────────┐                    ┌─────────────────┐
│  File Storage    │                    │  SQLite Index   │
│  (Source of      │◄───sync────────────│  (Rebuildable   │
│   Truth)         │                    │   Cache)        │
│                  │                    │                 │
│  /docs/**/*.md   │                    │  - Documents    │
│                  │                    │  - FTS5 search  │
│                  │                    │  - Provenance   │
└────────┬─────────┘                    └────────┬────────┘
         │                                       │
         │                                       │
         ↓                                       ↓
┌──────────────────┐                    ┌─────────────────┐
│  File Watcher    │                    │  Cache Manager  │
│  (Watchdog)      │────invalidate──────│  (Invalidation) │
│                  │                    │                 │
│  - CREATE        │                    │  - TTL cache    │
│  - MODIFY        │                    │  - Hash check   │
│  - DELETE        │                    │  - Rebuild      │
└──────────────────┘                    └─────────────────┘
```

**Principle**: Files = Source of Truth, Database = Rebuildable Cache

---

## Public Interface

```python
# src/storage/storage_api.py

from pathlib import Path
from typing import Optional
from models.document import Document
from models.provenance import ProvenanceRecord

class StorageAPI:
    """Hybrid storage facade (files + SQLite)."""

    def __init__(self, workspace_path: Path, db_path: Path):
        """
        Initialize hybrid storage.

        Args:
            workspace_path: Root directory of markdown files
            db_path: SQLite database file path
        """
        self.workspace_path = workspace_path
        self.db_path = db_path
        self.file_store = FileStore(workspace_path)
        self.index = SQLiteIndex(db_path)
        self.watcher = FileWatcher(workspace_path, self._on_file_changed)

    def get_document(self, doc_id: str) -> Optional[Document]:
        """
        Get document by ID (checks cache first, then file).

        Returns:
            Document or None if not found
        """

    def get_all_documents(self) -> list[Document]:
        """
        Get all documents in workspace.

        Returns:
            List of all parsed documents
        """

    def search_documents(self, query: str, limit: int = 100) -> list[Document]:
        """
        Full-text search using SQLite FTS5.

        Args:
            query: Search query (FTS5 syntax)
            limit: Max results

        Returns:
            Ranked list of documents matching query

        Performance:
            < 100ms dla 10k documents (NFR)
        """

    def save_document(self, doc: Document) -> None:
        """
        Save document to file and update index.

        Args:
            doc: Document to save

        Side effects:
            - Writes .md file
            - Updates SQLite index
            - Records provenance
        """

    def delete_document(self, doc_id: str) -> None:
        """
        Delete document from file and index.

        Args:
            doc_id: Document ID to delete
        """

    def rebuild_index(self) -> None:
        """
        Rebuild SQLite index from all files (cache invalidation).

        Use cases:
            - Database corrupted
            - Schema upgrade
            - Manual cache clear
        """

    def get_provenance(self, doc_id: str) -> list[ProvenanceRecord]:
        """
        Get provenance trail for document.

        Returns:
            List of changes (timestamp, user, operation, hash)
        """

    def start_watching(self) -> None:
        """Start file system monitoring (Watchdog)."""

    def stop_watching(self) -> None:
        """Stop file system monitoring."""

    def _on_file_changed(self, event_type: str, file_path: Path) -> None:
        """
        Handle file system events.

        Args:
            event_type: CREATE | MODIFY | DELETE
            file_path: Changed file
        """
```

---

## FileStore (Markdown Files)

```python
# src/storage/file_store.py

from pathlib import Path
from typing import Optional
from models.document import Document
from core.parser import ParserAPI

class FileStore:
    """File-based storage (source of truth)."""

    def __init__(self, workspace_path: Path):
        self.workspace_path = workspace_path
        self.parser = ParserAPI()

    def read_document(self, doc_id: str) -> Optional[Document]:
        """
        Read and parse document from file.

        Lookup strategy:
        1. Try: docs/{doc_type}/{doc_id}.md
        2. Try: docs/**/{doc_id}.md (recursive search)

        Returns:
            Parsed Document or None
        """
        # Strategy 1: Type-based path
        for doc_type in ['engineering', 'pre-production', 'implementation', 'operations']:
            path = self.workspace_path / doc_type / f"{doc_id}.md"
            if path.exists():
                return self.parser.parse_document(path)

        # Strategy 2: Recursive search
        for md_file in self.workspace_path.rglob(f"{doc_id}.md"):
            return self.parser.parse_document(md_file)

        return None

    def write_document(self, doc: Document) -> Path:
        """
        Write document to file.

        Path: docs/{doc.type}/{doc.id}.md

        Returns:
            Path where document was saved
        """
        output_dir = self.workspace_path / doc.type
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / f"{doc.id}.md"

        # Serialize document to markdown
        content = self._serialize_document(doc)

        output_path.write_text(content, encoding='utf-8')
        return output_path

    def delete_document(self, doc_id: str) -> bool:
        """
        Delete document file.

        Returns:
            True if deleted, False if not found
        """
        doc = self.read_document(doc_id)
        if doc and doc.file_path:
            doc.file_path.unlink()
            return True
        return False

    def list_all_files(self) -> list[Path]:
        """
        List all .md files in workspace.

        Returns:
            List of file paths
        """
        return list(self.workspace_path.rglob("*.md"))

    def _serialize_document(self, doc: Document) -> str:
        """
        Serialize Document to markdown with frontmatter.

        Format:
            ---
            id: DOC-001
            title: ...
            ---

            # Section 1

            Content here.
        """
        import yaml

        # YAML frontmatter
        frontmatter = yaml.dump(doc.frontmatter, allow_unicode=True, sort_keys=False)

        # Full markdown
        return f"---\n{frontmatter}---\n\n{doc.body}"
```

---

## SQLiteIndex (Rebuildable Cache)

```python
# src/storage/sqlite_index.py

import sqlite3
from pathlib import Path
from typing import Optional
from models.document import Document
import hashlib

class SQLiteIndex:
    """SQLite index for fast search and metadata queries."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._create_schema()

    def _create_schema(self):
        """Create database schema with FTS5."""
        self.conn.executescript("""
            -- Document metadata
            CREATE TABLE IF NOT EXISTS documents (
                doc_id TEXT PRIMARY KEY,
                doc_type TEXT NOT NULL,
                title TEXT NOT NULL,
                status TEXT,
                file_path TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                last_indexed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                frontmatter JSON
            );

            -- Full-text search (FTS5)
            CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
                doc_id UNINDEXED,
                title,
                body,
                content='documents',
                content_rowid='rowid'
            );

            -- Provenance tracking
            CREATE TABLE IF NOT EXISTS provenance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                doc_id TEXT NOT NULL,
                operation TEXT NOT NULL,  -- CREATE | UPDATE | DELETE
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                user TEXT,
                content_hash TEXT,
                FOREIGN KEY (doc_id) REFERENCES documents(doc_id)
            );

            -- Indexes
            CREATE INDEX IF NOT EXISTS idx_doc_type ON documents(doc_type);
            CREATE INDEX IF NOT EXISTS idx_status ON documents(status);
            CREATE INDEX IF NOT EXISTS idx_hash ON documents(content_hash);
        """)
        self.conn.commit()

    def index_document(self, doc: Document) -> None:
        """
        Index document in SQLite.

        Args:
            doc: Parsed document
        """
        import json

        # Calculate content hash
        content_hash = hashlib.sha256(doc.body.encode()).hexdigest()

        # Insert/update metadata
        self.conn.execute("""
            INSERT OR REPLACE INTO documents (doc_id, doc_type, title, status, file_path, content_hash, frontmatter)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            doc.id,
            doc.type,
            doc.title,
            doc.frontmatter.get('status'),
            str(doc.file_path),
            content_hash,
            json.dumps(doc.frontmatter)
        ))

        # Update FTS5 index
        self.conn.execute("""
            INSERT OR REPLACE INTO documents_fts (doc_id, title, body)
            VALUES (?, ?, ?)
        """, (doc.id, doc.title, doc.body))

        # Record provenance
        self.conn.execute("""
            INSERT INTO provenance (doc_id, operation, content_hash)
            VALUES (?, 'UPDATE', ?)
        """, (doc.id, content_hash))

        self.conn.commit()

    def search(self, query: str, limit: int = 100) -> list[dict]:
        """
        Full-text search using FTS5.

        Args:
            query: FTS5 query (e.g., "parser AND validation")

        Returns:
            List of matching documents with rank
        """
        cursor = self.conn.execute("""
            SELECT d.doc_id, d.title, d.doc_type, d.status, d.file_path, fts.rank
            FROM documents_fts fts
            JOIN documents d ON fts.doc_id = d.doc_id
            WHERE documents_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (query, limit))

        return [
            {
                'doc_id': row[0],
                'title': row[1],
                'doc_type': row[2],
                'status': row[3],
                'file_path': row[4],
                'rank': row[5]
            }
            for row in cursor.fetchall()
        ]

    def get_metadata(self, doc_id: str) -> Optional[dict]:
        """Get document metadata without parsing file."""
        cursor = self.conn.execute("""
            SELECT doc_type, title, status, file_path, content_hash, last_indexed
            FROM documents WHERE doc_id = ?
        """, (doc_id,))

        row = cursor.fetchone()
        if not row:
            return None

        return {
            'doc_type': row[0],
            'title': row[1],
            'status': row[2],
            'file_path': row[3],
            'content_hash': row[4],
            'last_indexed': row[5]
        }

    def is_stale(self, doc_id: str, current_hash: str) -> bool:
        """
        Check if cached index is stale.

        Args:
            doc_id: Document ID
            current_hash: Hash of current file content

        Returns:
            True if cached hash != current hash
        """
        metadata = self.get_metadata(doc_id)
        if not metadata:
            return True  # Not indexed yet
        return metadata['content_hash'] != current_hash

    def delete_document(self, doc_id: str) -> None:
        """Remove document from index."""
        self.conn.execute("DELETE FROM documents WHERE doc_id = ?", (doc_id,))
        self.conn.execute("DELETE FROM documents_fts WHERE doc_id = ?", (doc_id,))
        self.conn.execute("""
            INSERT INTO provenance (doc_id, operation)
            VALUES (?, 'DELETE')
        """, (doc_id,))
        self.conn.commit()

    def rebuild_from_files(self, file_store: 'FileStore') -> None:
        """
        Rebuild entire index from files (cache invalidation).

        Args:
            file_store: FileStore instance
        """
        # Clear existing index
        self.conn.execute("DELETE FROM documents")
        self.conn.execute("DELETE FROM documents_fts")
        self.conn.commit()

        # Re-index all files
        for file_path in file_store.list_all_files():
            try:
                doc = file_store.parser.parse_document(file_path)
                self.index_document(doc)
            except Exception as e:
                print(f"Warning: Failed to index {file_path}: {e}")
```

---

## FileWatcher (Watchdog Integration)

```python
# src/storage/file_watcher.py

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
from typing import Callable

class MarkdownFileHandler(FileSystemEventHandler):
    """Handle .md file changes."""

    def __init__(self, callback: Callable[[str, Path], None]):
        self.callback = callback

    def on_created(self, event: FileSystemEvent):
        if not event.is_directory and event.src_path.endswith('.md'):
            self.callback('CREATE', Path(event.src_path))

    def on_modified(self, event: FileSystemEvent):
        if not event.is_directory and event.src_path.endswith('.md'):
            self.callback('MODIFY', Path(event.src_path))

    def on_deleted(self, event: FileSystemEvent):
        if not event.is_directory and event.src_path.endswith('.md'):
            self.callback('DELETE', Path(event.src_path))

class FileWatcher:
    """File system monitoring using Watchdog."""

    def __init__(self, workspace_path: Path, callback: Callable[[str, Path], None]):
        self.workspace_path = workspace_path
        self.observer = Observer()
        self.handler = MarkdownFileHandler(callback)

    def start(self) -> None:
        """Start watching workspace for changes."""
        self.observer.schedule(self.handler, str(self.workspace_path), recursive=True)
        self.observer.start()

    def stop(self) -> None:
        """Stop watching."""
        self.observer.stop()
        self.observer.join()
```

---

## Performance

**Targets (NFR)**:
- Search: < 100ms dla 10k documents
- Index update: < 50ms per document
- Rebuild: < 30s dla 1000 documents

**Measured** [E-146, E-158]:
- FTS5 search (10k docs): 60ms ✅
- Index single doc: 15ms ✅
- Rebuild (1000 docs): 18s ✅
- Watchdog event detection: 99.9% reliability ✅

---

## Testing

```python
def test_hybrid_storage():
    from storage.storage_api import StorageAPI
    from pathlib import Path

    workspace = Path("/tmp/test-docs")
    db_path = Path("/tmp/test.db")

    storage = StorageAPI(workspace, db_path)

    # Create document
    doc = Document(id="TEST-001", title="Test", type="test", body="Content")
    storage.save_document(doc)

    # Retrieve from cache
    retrieved = storage.get_document("TEST-001")
    assert retrieved.id == "TEST-001"

    # Search
    results = storage.search_documents("Content")
    assert len(results) >= 1

def test_cache_invalidation():
    storage = StorageAPI(workspace, db_path)

    # Modify file directly (bypass cache)
    file_path = workspace / "test" / "TEST-001.md"
    file_path.write_text("---\nid: TEST-001\n---\n\nModified content")

    # Trigger file watcher event
    storage._on_file_changed('MODIFY', file_path)

    # Verify cache updated
    doc = storage.get_document("TEST-001")
    assert "Modified content" in doc.body
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-005](../decisions/ADR-005-storage.md), [ADR-002](../decisions/ADR-002-watchdog.md)
