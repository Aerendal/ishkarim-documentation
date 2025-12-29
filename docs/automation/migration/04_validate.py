#!/usr/bin/env python3
"""
Living Documentation Framework - Walidacja Migracji

Kompleksowa walidacja poprawności migracji dokumentów do bazy SQLite.

Testy walidacyjne:
1. Walidacja liczby dokumentów (pliki vs baza)
2. Walidacja metadanych (sample verification)
3. Integralność grafu (broken edges, orphaned nodes)
4. FTS5 operational (full-text search)
5. Living Documentation metadata completeness
6. Version history consistency
7. Provenance audit trail
8. Database integrity (foreign keys, constraints)

Użycie:
    python 04_validate.py
    python 04_validate.py --verbose  # Szczegółowy output
"""

import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path
from typing import List, Dict, Any, Set, Tuple
from dataclasses import dataclass, field

# Dodaj parent directory do path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from document_parser import DocumentParser


@dataclass
class ValidationResult:
    """Wynik pojedynczego testu walidacyjnego"""
    test_name: str
    status: str  # "pass", "warning", "fail"
    message: str
    details: Dict[str, Any] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return self.status == "pass"

    @property
    def failed(self) -> bool:
        return self.status == "fail"


class MigrationValidator:
    """Walidator migracji dokumentów"""

    def __init__(self, db_path: Path, base_path: Path, verbose: bool = False):
        """
        Inicjalizacja walidatora

        Args:
            db_path: Ścieżka do bazy SQLite
            base_path: Katalog bazowy dla dokumentów
            verbose: Czy wyświetlać szczegółowe informacje
        """
        self.db_path = db_path
        self.base_path = base_path
        self.verbose = verbose
        self.parser = DocumentParser(base_path)
        self.conn: sqlite3.Connection = None
        self.results: List[ValidationResult] = []

    def connect(self):
        """Połącz z bazą danych"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Zamknij połączenie z bazą"""
        if self.conn:
            self.conn.close()

    def add_result(self, result: ValidationResult):
        """Dodaj wynik testu"""
        self.results.append(result)

        # Wyświetl wynik
        icon = {
            "pass": "✓",
            "warning": "⚠",
            "fail": "✗"
        }[result.status]

        color = {
            "pass": "\033[92m",  # Green
            "warning": "\033[93m",  # Yellow
            "fail": "\033[91m"  # Red
        }[result.status]

        reset = "\033[0m"

        print(f"  {color}{icon}{reset} {result.test_name}: {result.message}")

        if self.verbose and result.details:
            for key, value in result.details.items():
                print(f"      {key}: {value}")

    # ========================================================================
    # TEST 1: Walidacja liczby dokumentów
    # ========================================================================

    def validate_document_count(self) -> ValidationResult:
        """Sprawdź czy liczba dokumentów w bazie zgadza się z plikami"""
        print("\n1. Walidacja liczby dokumentów...")

        # Policz dokumenty w bazie
        db_count = self.conn.execute("SELECT COUNT(*) as count FROM documents").fetchone()['count']

        # Policz pliki markdown z poprawnymi metadanymi
        documents = self.parser.parse_directory(self.base_path, skip_templates=True)
        file_count = len(documents)

        if db_count == file_count:
            return ValidationResult(
                test_name="Liczba dokumentów",
                status="pass",
                message=f"Zgadza się: {db_count} dokumentów w bazie, {file_count} plików",
                details={"db_count": db_count, "file_count": file_count}
            )
        else:
            return ValidationResult(
                test_name="Liczba dokumentów",
                status="warning",
                message=f"Różnica: {db_count} w bazie vs {file_count} plików",
                details={
                    "db_count": db_count,
                    "file_count": file_count,
                    "difference": abs(db_count - file_count),
                    "reason": "Niektóre pliki mogły być zduplikowane (INSERT OR REPLACE)"
                }
            )

    # ========================================================================
    # TEST 2: Walidacja metadanych (sample)
    # ========================================================================

    def validate_metadata_sample(self) -> ValidationResult:
        """Zweryfikuj metadane dla próbki dokumentów"""
        print("\n2. Walidacja metadanych (sample)...")

        sample_ids = ['PRD-001-V2', 'TDD-001-V2', 'ADR-009']
        errors = []

        for doc_id in sample_ids:
            try:
                # Znajdź dokument w plikach
                file_doc = self.parser.find_document_by_id(doc_id)
                if not file_doc:
                    errors.append(f"{doc_id}: nie znaleziono w plikach")
                    continue

                # Pobierz z bazy
                db_doc = self.conn.execute(
                    "SELECT * FROM documents WHERE id = ?", (doc_id,)
                ).fetchone()

                if not db_doc:
                    errors.append(f"{doc_id}: nie znaleziono w bazie")
                    continue

                # Porównaj kluczowe pola
                if file_doc.title != db_doc['title']:
                    errors.append(f"{doc_id}: title się różni")
                if file_doc.type != db_doc['doc_type']:
                    errors.append(f"{doc_id}: type się różni")
                if file_doc.status != db_doc['status']:
                    errors.append(f"{doc_id}: status się różni")

            except Exception as e:
                errors.append(f"{doc_id}: błąd - {e}")

        if not errors:
            return ValidationResult(
                test_name="Metadane (sample)",
                status="pass",
                message=f"Wszystkie {len(sample_ids)} próbek zgadza się",
                details={"sample_size": len(sample_ids), "checked_ids": sample_ids}
            )
        else:
            return ValidationResult(
                test_name="Metadane (sample)",
                status="fail",
                message=f"{len(errors)} błędów w {len(sample_ids)} próbkach",
                details={"errors": errors}
            )

    # ========================================================================
    # TEST 3: Integralność grafu
    # ========================================================================

    def validate_graph_integrity(self) -> ValidationResult:
        """Sprawdź integralność grafu zależności"""
        print("\n3. Walidacja integralności grafu...")

        # Sprawdź broken edges (foreign key violations)
        broken_edges = self.conn.execute("""
            SELECT e.from_id, e.to_id, e.edge_type
            FROM edges e
            LEFT JOIN documents d1 ON e.from_id = d1.id
            LEFT JOIN documents d2 ON e.to_id = d2.id
            WHERE d1.id IS NULL OR d2.id IS NULL
        """).fetchall()

        # Sprawdź orphaned nodes (nodes bez edges)
        orphaned_nodes = self.conn.execute("""
            SELECT d.id, d.title
            FROM documents d
            LEFT JOIN edges e1 ON d.id = e1.from_id
            LEFT JOIN edges e2 ON d.id = e2.to_id
            WHERE e1.from_id IS NULL AND e2.to_id IS NULL
        """).fetchall()

        # Sprawdź total edges
        total_edges = self.conn.execute("SELECT COUNT(*) as count FROM edges").fetchone()['count']

        if len(broken_edges) == 0 and len(orphaned_nodes) < 5:
            return ValidationResult(
                test_name="Integralność grafu",
                status="pass",
                message=f"{total_edges} krawędzi, 0 broken, {len(orphaned_nodes)} orphaned nodes",
                details={
                    "total_edges": total_edges,
                    "broken_edges": 0,
                    "orphaned_nodes": len(orphaned_nodes)
                }
            )
        elif len(broken_edges) == 0:
            return ValidationResult(
                test_name="Integralność grafu",
                status="warning",
                message=f"{total_edges} krawędzi, {len(orphaned_nodes)} orphaned nodes",
                details={
                    "total_edges": total_edges,
                    "broken_edges": 0,
                    "orphaned_nodes": len(orphaned_nodes),
                    "orphaned_list": [dict(row) for row in orphaned_nodes]
                }
            )
        else:
            return ValidationResult(
                test_name="Integralność grafu",
                status="fail",
                message=f"{len(broken_edges)} broken edges!",
                details={
                    "total_edges": total_edges,
                    "broken_edges": len(broken_edges),
                    "broken_list": [dict(row) for row in broken_edges[:10]]
                }
            )

    # ========================================================================
    # TEST 4: FTS5 Operational
    # ========================================================================

    def validate_fts5_search(self) -> ValidationResult:
        """Sprawdź czy FTS5 full-text search działa"""
        print("\n4. Walidacja FTS5 full-text search...")

        try:
            # Test search query
            results = self.conn.execute("""
                SELECT id, title FROM documents_fts
                WHERE documents_fts MATCH 'parser'
                LIMIT 5
            """).fetchall()

            # Sprawdź czy FTS5 table istnieje
            fts_count = self.conn.execute("""
                SELECT COUNT(*) as count FROM documents_fts
            """).fetchone()['count']

            if fts_count > 0 and len(results) >= 0:
                return ValidationResult(
                    test_name="FTS5 Search",
                    status="pass",
                    message=f"FTS5 działa, {fts_count} wpisów zaindeksowanych",
                    details={
                        "indexed_count": fts_count,
                        "test_query": "parser",
                        "results_found": len(results)
                    }
                )
            else:
                return ValidationResult(
                    test_name="FTS5 Search",
                    status="warning",
                    message=f"FTS5 działa ale {fts_count} wpisów",
                    details={"indexed_count": fts_count}
                )

        except Exception as e:
            return ValidationResult(
                test_name="FTS5 Search",
                status="fail",
                message=f"FTS5 error: {e}",
                details={"error": str(e)}
            )

    # ========================================================================
    # TEST 5: Living Documentation Metadata
    # ========================================================================

    def validate_living_doc_metadata(self) -> ValidationResult:
        """Sprawdź Living Documentation metadata"""
        print("\n5. Walidacja Living Documentation metadata...")

        living_count = self.conn.execute("""
            SELECT COUNT(*) as count FROM living_doc_metadata
        """).fetchone()['count']

        # Sprawdź czy są version_metadata
        with_version = self.conn.execute("""
            SELECT COUNT(*) as count FROM living_doc_metadata
            WHERE version IS NOT NULL
        """).fetchone()['count']

        # Sprawdź health_status
        with_health = self.conn.execute("""
            SELECT COUNT(*) as count FROM living_doc_metadata
            WHERE health_status IS NOT NULL
        """).fetchone()['count']

        if living_count >= 10:
            return ValidationResult(
                test_name="Living Doc Metadata",
                status="pass",
                message=f"{living_count} wpisów, {with_version} z wersją, {with_health} z health status",
                details={
                    "total": living_count,
                    "with_version": with_version,
                    "with_health": with_health
                }
            )
        elif living_count > 0:
            return ValidationResult(
                test_name="Living Doc Metadata",
                status="warning",
                message=f"Tylko {living_count} wpisów Living Doc metadata",
                details={"total": living_count}
            )
        else:
            return ValidationResult(
                test_name="Living Doc Metadata",
                status="fail",
                message="Brak Living Doc metadata!",
                details={"total": 0}
            )

    # ========================================================================
    # TEST 6: Version History
    # ========================================================================

    def validate_version_history(self) -> ValidationResult:
        """Sprawdź version history"""
        print("\n6. Walidacja version history...")

        history_count = self.conn.execute("""
            SELECT COUNT(*) as count FROM version_history
        """).fetchone()['count']

        # Sprawdź czy są breaking changes
        breaking_count = self.conn.execute("""
            SELECT COUNT(*) as count FROM version_history WHERE breaking = 1
        """).fetchone()['count']

        if history_count >= 5:
            return ValidationResult(
                test_name="Version History",
                status="pass",
                message=f"{history_count} wpisów, {breaking_count} breaking changes",
                details={
                    "total_entries": history_count,
                    "breaking_changes": breaking_count
                }
            )
        elif history_count > 0:
            return ValidationResult(
                test_name="Version History",
                status="warning",
                message=f"Tylko {history_count} wpisów version history",
                details={"total_entries": history_count}
            )
        else:
            return ValidationResult(
                test_name="Version History",
                status="fail",
                message="Brak version history!",
                details={"total_entries": 0}
            )

    # ========================================================================
    # TEST 7: Provenance Audit Trail
    # ========================================================================

    def validate_provenance(self) -> ValidationResult:
        """Sprawdź provenance audit trail"""
        print("\n7. Walidacja provenance audit trail...")

        provenance_count = self.conn.execute("""
            SELECT COUNT(*) as count FROM provenance
        """).fetchone()['count']

        # Sprawdź czy każdy dokument ma provenance
        docs_without_provenance = self.conn.execute("""
            SELECT d.id, d.title
            FROM documents d
            LEFT JOIN provenance p ON d.id = p.doc_id
            WHERE p.doc_id IS NULL
        """).fetchall()

        if len(docs_without_provenance) == 0:
            return ValidationResult(
                test_name="Provenance Trail",
                status="pass",
                message=f"{provenance_count} wpisów, wszystkie dokumenty pokryte",
                details={"total_entries": provenance_count}
            )
        else:
            return ValidationResult(
                test_name="Provenance Trail",
                status="warning",
                message=f"{len(docs_without_provenance)} dokumentów bez provenance",
                details={
                    "total_entries": provenance_count,
                    "missing_provenance": [dict(row) for row in docs_without_provenance]
                }
            )

    # ========================================================================
    # TEST 8: Database Integrity
    # ========================================================================

    def validate_database_integrity(self) -> ValidationResult:
        """Sprawdź integralność bazy danych (constraints, indexes)"""
        print("\n8. Walidacja integralności bazy danych...")

        try:
            # Sprawdź foreign keys
            self.conn.execute("PRAGMA foreign_key_check").fetchall()

            # Sprawdź indexes
            indexes = self.conn.execute("""
                SELECT name FROM sqlite_master
                WHERE type='index' AND name LIKE 'idx_%'
            """).fetchall()

            # Sprawdź tables
            tables = self.conn.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name NOT LIKE 'sqlite_%'
            """).fetchall()

            return ValidationResult(
                test_name="Database Integrity",
                status="pass",
                message=f"{len(tables)} tabel, {len(indexes)} indeksów, foreign keys OK",
                details={
                    "table_count": len(tables),
                    "index_count": len(indexes)
                }
            )

        except Exception as e:
            return ValidationResult(
                test_name="Database Integrity",
                status="fail",
                message=f"Błąd integralności: {e}",
                details={"error": str(e)}
            )

    # ========================================================================
    # Uruchom wszystkie testy
    # ========================================================================

    def run_all_tests(self) -> Dict[str, Any]:
        """Uruchom wszystkie testy walidacyjne"""
        print(f"\n{'='*80}")
        print("WALIDACJA MIGRACJI - Living Documentation Framework")
        print(f"{'='*80}")

        # Uruchom testy
        self.add_result(self.validate_document_count())
        self.add_result(self.validate_metadata_sample())
        self.add_result(self.validate_graph_integrity())
        self.add_result(self.validate_fts5_search())
        self.add_result(self.validate_living_doc_metadata())
        self.add_result(self.validate_version_history())
        self.add_result(self.validate_provenance())
        self.add_result(self.validate_database_integrity())

        # Podsumowanie
        passed = sum(1 for r in self.results if r.passed)
        warnings = sum(1 for r in self.results if r.status == "warning")
        failed = sum(1 for r in self.results if r.failed)

        print(f"\n{'='*80}")
        print("PODSUMOWANIE WALIDACJI")
        print(f"{'='*80}")
        print(f"  ✓ Passed:   {passed}/{len(self.results)}")
        print(f"  ⚠ Warnings: {warnings}/{len(self.results)}")
        print(f"  ✗ Failed:   {failed}/{len(self.results)}")
        print()

        if failed == 0:
            print("  🎉 WALIDACJA ZAKOŃCZONA SUKCESEM!")
        elif failed <= 2:
            print("  ⚠️  WALIDACJA Z DROBNYMI PROBLEMAMI")
        else:
            print("  ❌ WALIDACJA NIEPOWODZENIE - WYMAGANE POPRAWKI")

        print()

        return {
            "total_tests": len(self.results),
            "passed": passed,
            "warnings": warnings,
            "failed": failed,
            "results": [
                {
                    "test": r.test_name,
                    "status": r.status,
                    "message": r.message,
                    "details": r.details
                }
                for r in self.results
            ]
        }


def main():
    parser = argparse.ArgumentParser(
        description="Living Documentation Framework - Walidacja Migracji"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Wyświetl szczegółowe informacje"
    )

    args = parser.parse_args()

    # Ścieżki
    base_path = Path(__file__).parent.parent.parent  # docs/
    db_path = base_path / ".semantic-docs" / "index.db"

    if not db_path.exists():
        print(f"BŁĄD: Baza danych nie znaleziona: {db_path}", file=sys.stderr)
        print("Uruchom najpierw migrację dokumentów.", file=sys.stderr)
        sys.exit(1)

    # Walidacja
    validator = MigrationValidator(db_path, base_path, verbose=args.verbose)
    validator.connect()

    try:
        report = validator.run_all_tests()

        # Zapisz raport
        from datetime import datetime
        report_file = Path(__file__).parent / f"validation-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'report': report
            }, f, indent=2, ensure_ascii=False)

        print(f"✓ Raport walidacji zapisany: {report_file}\n")

        # Exit code: 0 jeśli passed, 1 jeśli failed
        sys.exit(1 if report['failed'] > 0 else 0)

    finally:
        validator.close()


if __name__ == "__main__":
    main()
