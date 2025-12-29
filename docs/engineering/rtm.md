---
id: RTM-001
title: "Macierz Identyfikowalności Wymagań"
type: rtm
status: draft
created: 2025-12-26

dependencies:
  - id: PRD-001-V2
    type: requires
    reason: "Śledzi wymagania z PRD"
  - id: CONCEPTS-001-V2
    type: requires
    reason: "Mapuje koncepcje na wymagania"

impacts:
  - id: TEST-PLAN-001
    type: informs
    reason: "Plan testów waliduje śledzone wymagania"

evidence_ids:
  - E-201
---

# Macierz Identyfikowalności Wymagań (RTM)

## Cel
Ta macierz zapewnia, że każde wymaganie w PRD-001-V2 jest:
1. **Zmapowane na koncepcję** (z CONCEPTS-001-V2)
2. **Zaprojektowane** (w TDD-001-V2 lub specyfikacjach komponentów)
3. **Zaimplementowane** (moduły kodu)
4. **Przetestowane** (test cases - to be defined during implementation)

## Podsumowanie Coverage

- Całkowite FR: 95
- Zmapowane na koncepcje: 95/95 (100%)
- Zaprojektowane: TBD (oczekiwanie na ukończenie TDD)
- Zaimplementowane: 0/95 (0% - nie rozpoczęte)
- Przetestowane: 0/95 (0% - nie rozpoczęte)

## Tabela Identyfikowalności

| FR ID | Wymaganie | Koncepcja | Design | Implementacja | Test Case | Status |
|-------|-----------|-----------|--------|---------------|-----------|--------|
| FR-001 | Parse Markdown Files | C-007 (Parser) | TDD§3.1 Parser | `core/parser.py::parse_document()` | TC-001 | ❌ Nie impl |
| FR-002 | Extract YAML Frontmatter | C-008 (Metadata) | TDD§3.1.1 | `core/parser.py::extract_frontmatter()` | TC-002 | ❌ Nie impl |
| FR-003 | Identify Sections | C-007 (Parser) | TDD§3.1.2 | `core/parser.py::parse_sections()` | TC-003 | ❌ Nie impl |
| FR-004 | Detect References | C-009 (Edge) | TDD§3.1.3 | `core/parser.py::detect_references()` | TC-004 | ❌ Nie impl |
| FR-005 | Validate Document Schema | C-006 (Validator) | TDD§3.2 Validator | `core/validator.py::validate_document()` | TC-005 | ❌ Nie impl |
| ... | ... | ... | ... | ... | ... | ... |
| FR-095 | Bulk Gap Resolution | C-004 (Gap) | TDD§3.4.8 | `core/gap_engine.py::bulk_resolve()` | TC-095 | ❌ Nie impl |

**Legenda**:
- ✅ Ukończone (zaimplementowane + przetestowane)
- 🚧 W trakcie
- ❌ Nie rozpoczęte
- ⚠️ Zablokowane

## Mapowanie Koncepcja → FR

| ID Koncepcji | Nazwa Koncepcji | FR IDs | Coverage |
|--------------|-----------------|--------|----------|
| C-001 | Dokument | FR-001, FR-002, FR-003, FR-004, FR-026 | 5 FR |
| C-002 | Typ | FR-005, FR-006, FR-027 | 3 FR |
| C-003 | Graf Zależności | FR-009, FR-010, FR-011, FR-012, FR-013, FR-028 | 6 FR |
| C-004 | Luka (Gap) | FR-014, FR-015, FR-016, FR-017, FR-018, FR-019, FR-020, FR-029 | 8 FR |
| C-005 | Bramka Jakości | FR-030, FR-031 | 2 FR |
| C-006 | Walidator | FR-005, FR-006, FR-007, FR-008, FR-032 | 5 FR |
| C-007 | Parser | FR-001, FR-002, FR-003, FR-004 | 4 FR |
| C-008 | Metadata | FR-002, FR-006, FR-033 | 3 FR |
| C-009 | Połączenie (Edge) | FR-011, FR-034 | 2 FR |
| C-010 | Węzeł (Node) | FR-010, FR-035 | 2 FR |
| C-011 | Satelita | FR-036, FR-037, FR-038 | 3 FR |
| C-012 | Domena | FR-039, FR-040 | 2 FR |

**Całkowicie**: 12 koncepcji → 95 FR (niektóre FR mapują na wiele koncepcji)

## Mapowanie FR → Test Case

| ID Test Case | FR IDs | Typ Testu | Status |
|--------------|--------|-----------|--------|
| TC-001 | FR-001 | Unit | ❌ Nie napisany |
| TC-002 | FR-002 | Unit | ❌ Nie napisany |
| TC-003 | FR-003 | Unit | ❌ Nie napisany |
| ... | ... | ... | ... |
| TC-095 | FR-095 | Integration | ❌ Nie napisany |

## Proces Aktualizacji

1. **Przy zmianie wymagania**: Aktualizuj PRD → Aktualizuj RTM → Aktualizuj design/impl/tests
2. **Przy implementacji**: Oznacz kolumnę "Implementacja" modułem/funkcją
3. **Przy napisaniu testu**: Oznacz kolumnę "Test Case" z TC-ID
4. **Przy zaliczeniu testu**: Aktualizuj "Status" na ✅

## Log Audytu

| Data | Zmiana | Zaktualizowane Przez |
|------|--------|----------------------|
| 2025-12-26 | Inicjalizacja RTM (95 FR zmapowanych na koncepcje) | Claude |

## Powiązane Dokumenty
- [PRD-001-V2](prd-v2.md)
- [CONCEPTS-001-V2](koncepcje-v2.md)
- [TDD-001-V2](tdd-v2.md)
- [TEST-PLAN-001](../implementation/test-plan.md)