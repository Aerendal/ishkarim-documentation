#!/usr/bin/env python3
"""
Living Documentation Framework - Watchdog Bidirectional Sync

Real-time synchronizacja między plikami markdown a bazą danych SQLite.

Funkcjonalności:
- Monitoruje zmiany w plikach .md (watchdog)
- Automatycznie aktualizuje bazę gdy plik się zmieni
- Re-parsuje dokument i wykonuje UPSERT
- Obsługuje utworzenie, modyfikację i usunięcie plików
- Graceful shutdown (Ctrl+C)
- Logging wszystkich operacji

Użycie:
    python watchdog_sync.py                    # Start daemon
    python watchdog_sync.py --test             # Test mode (single update)
    python watchdog_sync.py --path /custom     # Custom watch path
"""

import argparse
import hashlib
import json
import logging
import signal
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

# Watchdog imports
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler, FileSystemEvent
except ImportError:
    print("ERROR: watchdog nie jest zainstalowany", file=sys.stderr)
    print("Uruchom: pip install watchdog", file=sys.stderr)
    sys.exit(1)

# Dodaj parent directory do path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from document_parser import DocumentParser, Document


# Konfiguracja loggingu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class DocumentSyncHandler(FileSystemEventHandler):
    """Handler dla zmian w plikach markdown"""

    def __init__(self, db_path: Path, base_path: Path):
        """
        Inicjalizacja handlera

        Args:
            db_path: Ścieżka do bazy SQLite
            base_path: Katalog bazowy dla dokumentów
        """
        super().__init__()
        self.db_path = db_path
        self.base_path = base_path
        self.parser = DocumentParser(base_path)

        # Statystyki
        self.stats = {
            'created': 0,
            'modified': 0,
            'deleted': 0,
            'errors': 0
        }

    def get_connection(self) -> sqlite3.Connection:
        """Utwórz nowe połączenie z bazą"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def calculate_hash(self, file_path: Path) -> str:
        """Oblicz SHA256 hash zawartości pliku"""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                sha256.update(chunk)
        return sha256.hexdigest()

    def sync_document_to_db(self, file_path: Path, event_type: str) -> bool:
        """
        Synchronizuj dokument do bazy danych

        Args:
            file_path: Ścieżka do pliku
            event_type: Typ wydarzenia (created, modified, deleted)

        Returns:
            True jeśli sukces, False jeśli błąd
        """
        try:
            conn = self.get_connection()

            if event_type == 'deleted':
                # Usuń dokument z bazy
                file_rel = str(file_path.relative_to(self.base_path))

                cursor = conn.execute(
                    "SELECT id FROM documents WHERE file_path = ?",
                    (file_rel,)
                )
                row = cursor.fetchone()

                if row:
                    doc_id = row[0]
                    conn.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
                    conn.commit()
                    logger.info(f"🗑️  Usunięto: {doc_id} ({file_rel})")
                    self.stats['deleted'] += 1
                else:
                    logger.warning(f"⚠️  Nie znaleziono w bazie: {file_rel}")

                conn.close()
                return True

            # Parse dokumentu (created/modified)
            try:
                doc = self.parser.parse(file_path)
            except Exception as e:
                logger.error(f"❌ Błąd parsowania {file_path.name}: {e}")
                self.stats['errors'] += 1
                conn.close()
                return False

            # Oblicz hash
            content_hash = self.calculate_hash(file_path)
            file_rel = str(doc.file_path.relative_to(self.base_path))

            # Sprawdź czy hash się zmienił (optymalizacja)
            cursor = conn.execute(
                "SELECT content_hash FROM documents WHERE id = ?",
                (doc.id,)
            )
            row = cursor.fetchone()

            if row and row[0] == content_hash:
                logger.debug(f"⏭️  Pominięto (bez zmian): {doc.id}")
                conn.close()
                return True

            # UPSERT do documents table
            conn.execute("""
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

            # UPSERT do living_doc_metadata (jeśli applicable)
            if doc.has_living_doc_metadata:
                self._sync_living_metadata(conn, doc)

            # Record provenance
            conn.execute("""
                INSERT INTO provenance (doc_id, action, actor, details)
                VALUES (?, ?, ?, ?)
            """, (
                doc.id,
                event_type,
                'watchdog-sync',
                json.dumps({'file_path': file_rel, 'timestamp': datetime.now().isoformat()}, ensure_ascii=False)
            ))

            conn.commit()
            conn.close()

            # Log sukcesu
            icon = "📝" if event_type == "modified" else "➕"
            logger.info(f"{icon} {event_type.capitalize()}: {doc.id} ({doc.type})")

            if event_type == "created":
                self.stats['created'] += 1
            else:
                self.stats['modified'] += 1

            return True

        except Exception as e:
            logger.error(f"❌ Błąd sync {file_path.name}: {e}")
            self.stats['errors'] += 1
            if 'conn' in locals():
                conn.close()
            return False

    def _sync_living_metadata(self, conn: sqlite3.Connection, doc: Document):
        """Synchronizuj Living Documentation metadata"""
        lifecycle = doc.lifecycle or {}
        deprecation = doc.deprecation or {}

        conn.execute("""
            INSERT OR REPLACE INTO living_doc_metadata (
                doc_id, version, version_major, version_minor, version_patch,
                lifecycle_created, lifecycle_first_approved, lifecycle_last_modified,
                health_status, health_checks_json,
                is_deprecated, superseded_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            doc.id,
            doc.version,
            doc.major_version,
            doc.minor_version,
            doc.patch_version,
            lifecycle.get('created'),
            lifecycle.get('first_approved'),
            lifecycle.get('last_modified'),
            doc.health_status if doc.document_health else None,
            json.dumps(doc.document_health, ensure_ascii=False, cls=DateTimeEncoder) if doc.document_health else None,
            1 if doc.is_deprecated else 0,
            deprecation.get('superseded_by') if deprecation else None
        ))

    # Event handlers
    def on_created(self, event: FileSystemEvent):
        """Plik został utworzony"""
        if event.is_directory or not event.src_path.endswith('.md'):
            return

        file_path = Path(event.src_path)

        # Ignoruj template files
        if 'templates' in file_path.parts:
            return

        logger.debug(f"🔔 Wykryto utworzenie: {file_path.name}")
        self.sync_document_to_db(file_path, 'created')

    def on_modified(self, event: FileSystemEvent):
        """Plik został zmodyfikowany"""
        if event.is_directory or not event.src_path.endswith('.md'):
            return

        file_path = Path(event.src_path)

        # Ignoruj template files
        if 'templates' in file_path.parts:
            return

        logger.debug(f"🔔 Wykryto modyfikację: {file_path.name}")
        self.sync_document_to_db(file_path, 'modified')

    def on_deleted(self, event: FileSystemEvent):
        """Plik został usunięty"""
        if event.is_directory or not event.src_path.endswith('.md'):
            return

        file_path = Path(event.src_path)

        # Ignoruj template files
        if 'templates' in file_path.parts:
            return

        logger.debug(f"🔔 Wykryto usunięcie: {file_path.name}")
        self.sync_document_to_db(file_path, 'deleted')

    def get_stats(self) -> dict:
        """Zwróć statystyki synchronizacji"""
        return self.stats.copy()


class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder obsługujący date/datetime"""
    def default(self, obj):
        from datetime import date, datetime
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return super().default(obj)


class WatchdogSyncDaemon:
    """Daemon Watchdog sync"""

    def __init__(self, db_path: Path, watch_path: Path):
        """
        Inicjalizacja daemona

        Args:
            db_path: Ścieżka do bazy SQLite
            watch_path: Katalog do monitorowania
        """
        self.db_path = db_path
        self.watch_path = watch_path
        self.observer: Optional[Observer] = None
        self.handler: Optional[DocumentSyncHandler] = None
        self.running = False

    def start(self):
        """Uruchom daemon"""
        logger.info(f"{'='*80}")
        logger.info("WATCHDOG BIDIRECTIONAL SYNC - Living Documentation Framework")
        logger.info(f"{'='*80}")
        logger.info(f"📁 Monitorowany katalog: {self.watch_path}")
        logger.info(f"💾 Baza danych: {self.db_path}")
        logger.info(f"⏱️  Rozpoczęto: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"{'─'*80}")
        logger.info("🔍 Oczekiwanie na zmiany w plikach .md...")
        logger.info("   (Ctrl+C aby zatrzymać)")
        logger.info("")

        # Utwórz handler i observer
        self.handler = DocumentSyncHandler(self.db_path, self.watch_path)
        self.observer = Observer()
        self.observer.schedule(self.handler, str(self.watch_path), recursive=True)

        # Start observer
        self.observer.start()
        self.running = True

        # Setup signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        """Zatrzymaj daemon"""
        if not self.running:
            return

        logger.info("")
        logger.info(f"{'─'*80}")
        logger.info("⏹️  Zatrzymywanie Watchdog sync...")

        if self.observer:
            self.observer.stop()
            self.observer.join()

        # Wyświetl statystyki
        if self.handler:
            stats = self.handler.get_stats()
            logger.info(f"{'─'*80}")
            logger.info("📊 STATYSTYKI SYNCHRONIZACJI:")
            logger.info(f"   ➕ Utworzone:     {stats['created']}")
            logger.info(f"   📝 Zmodyfikowane: {stats['modified']}")
            logger.info(f"   🗑️  Usunięte:      {stats['deleted']}")
            logger.info(f"   ❌ Błędy:         {stats['errors']}")
            logger.info(f"{'─'*80}")
            logger.info(f"⏱️  Zakończono: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        self.running = False
        logger.info(f"{'='*80}")
        logger.info("✓ Watchdog sync zatrzymany")
        logger.info(f"{'='*80}\n")

    def _signal_handler(self, signum, frame):
        """Handler dla sygnałów (Ctrl+C)"""
        self.stop()
        sys.exit(0)


def test_single_update(db_path: Path, base_path: Path, file_path: Path) -> bool:
    """
    Test mode - synchronizuj pojedynczy plik

    Args:
        db_path: Ścieżka do bazy
        base_path: Katalog bazowy
        file_path: Plik do synchronizacji

    Returns:
        True jeśli sukces
    """
    logger.info(f"{'='*80}")
    logger.info("TEST MODE - Pojedyncza synchronizacja")
    logger.info(f"{'='*80}")
    logger.info(f"Plik: {file_path}")
    logger.info("")

    handler = DocumentSyncHandler(db_path, base_path)
    success = handler.sync_document_to_db(file_path, 'modified')

    logger.info("")
    logger.info(f"{'='*80}")
    if success:
        logger.info("✓ Test zakończony sukcesem")
    else:
        logger.error("✗ Test zakończony błędem")
    logger.info(f"{'='*80}\n")

    return success


def main():
    parser = argparse.ArgumentParser(
        description="Living Documentation Framework - Watchdog Bidirectional Sync"
    )
    parser.add_argument(
        "--path",
        type=Path,
        help="Katalog do monitorowania (default: docs/)"
    )
    parser.add_argument(
        "--test",
        type=Path,
        help="Test mode - synchronizuj pojedynczy plik i zakończ"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Włącz debug logging"
    )

    args = parser.parse_args()

    # Ustaw poziom loggingu
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    # Ścieżki
    base_path = args.path or Path(__file__).parent.parent.parent  # docs/
    db_path = base_path / ".semantic-docs" / "index.db"

    if not db_path.exists():
        logger.error(f"BŁĄD: Baza danych nie znaleziona: {db_path}")
        logger.error("Uruchom najpierw migrację dokumentów.")
        sys.exit(1)

    # Test mode
    if args.test:
        test_file = args.test if args.test.is_absolute() else base_path / args.test

        if not test_file.exists():
            logger.error(f"BŁĄD: Plik nie znaleziony: {test_file}")
            sys.exit(1)

        success = test_single_update(db_path, base_path, test_file)
        sys.exit(0 if success else 1)

    # Daemon mode
    daemon = WatchdogSyncDaemon(db_path, base_path)
    daemon.start()


if __name__ == "__main__":
    main()
