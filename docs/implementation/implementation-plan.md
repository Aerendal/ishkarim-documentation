---
id: IMPL-PLAN-001
title: "Plan Implementacji - System Dokumentacji Semantycznej"
type: implementation-plan
status: draft
created: 2025-12-26

dependencies:
  - id: TDD-001-V2
    type: requires
    status_constraint: [design-complete, approved]
    reason: "Nie można implementować bez sfinalizowanego designu"
  - id: ROADMAP-001
    type: requires
    reason: "Sekwencjonuje milestone'y z roadmapy"

impacts:
  # SPRINT-001 (planned - to be created at sprint start)
  - id: DEPLOYMENT-001
    type: informs

evidence_ids:
  - E-155
---

# Plan Implementacji

## Podział na Sprinty (6 Sprintów dla MVP)

### Sprint 1: Fundament (Tygodnie 1-2)
**Cel**: Parser + Modele
**Zadania**:
1. Setup projektu (pyproject.toml, requirements.txt)
2. Implementacja models/ (Document, DocumentType, Gap)
3. Implementacja core/parser.py
4. Testy jednostkowe (cel: 80% coverage)

**Deliverable**: Parser działający na 100+ przykładowych docs

### Sprint 2: Validator (Tygodnie 3-4)
**Cel**: Walidacja Pydantic + schematy
**Zadania**:
1. Implementacja core/validator.py
2. Utworzenie schemas/document_types.yaml (7 schematów)
3. Implementacja detekcji luk E110, E120
4. Testy integracyjne

**Deliverable**: Validator wyłapuje wszystkie naruszenia schematu

### Sprint 3: Graph (Tygodnie 5-6)
**Cel**: Graf zależności NetworkX
**Zadania**:
1. Implementacja core/graph_builder.py
2. Implementacja E140 (broken dependencies)
3. Detekcja cykli
4. Testy wydajności (< 2s dla 100 docs)

**Deliverable**: Wizualizacja grafu w CLI

### Sprint 4: Fundament GUI (Tygodnie 7-8)
**Cel**: Główne okno PySide6 + panele
**Zadania**:
1. Implementacja gui/main_window.py
2. Implementacja gui/panels/ (gaps, stats)
3. Implementacja gui/preview_widget.py (rendering markdown)

**Deliverable**: GUI ładuje się, wyświetla listę dokumentów

### Sprint 5: Wizualizacja Grafu (Tygodnie 9-10)
**Cel**: Cytoscape.js w QtWebEngine
**Zadania**:
1. Implementacja gui/graph_widget.py
2. Layout Cytoscape.js (Cola, Dagre)
3. Interaktywność: klik node → preview doc

**Deliverable**: Interaktywny graf w GUI

### Sprint 6: Gap Engine (Tygodnie 11-12)
**Cel**: Pełna detekcja luk + remediacja
**Zadania**:
1. Implementacja pozostałych luk (E130, E150, E160)
2. Implementacja RemediationGenerator
3. Implementacja ProactiveAssistant (następne kroki)

**Deliverable**: MVP kompletne, gotowe do beta

## Alokacja Zasobów

| Rola | Alokacja | Odpowiedzialności |
|------|----------|-------------------|
| Developer 1 | 100% (full-time) | Backend (parser, validator, graph) |
| Developer 2 | 50% | GUI (PySide6, Cytoscape.js) |
| QA | 20% | Plan testów, test cases, automatyzacja |
| Tech Writer | 10% | Podręcznik użytkownika, dokumentacja API |

## Mitygacja Ryzyka

| Ryzyko | Mitygacja |
|--------|-----------|
| Krzywa uczenia Qt | ADR-001 uzasadnione, prototyp zbudowany [E-144] |
| Problemy wydajności | Benchmark wcześnie (Sprint 3), SQLite FTS5 |
| Scope creep | Bramka REQ-FREEZE wymuszana (PRD-V2) |

## Zależności External

| Zależność | Wersja | Licencja | Ryzyko |
|-----------|---------|----------|--------|
| PySide6 | 6.5+ | LGPL | Low (zaaprobowane ADR-001) |
| NetworkX | 3.2+ | BSD | Low |
| Pydantic | 2.5+ | MIT | Low |

## Kryteria Sukcesu

- Wszystkie 6 sprintów dostarczone na czas
- 80% code coverage osiągnięte
- NFRy wydajności spełnione (NFR-001, NFR-002, NFR-003)
- 0 critical bugs w beta
- 5+ beta users dostarczających feedback

## Powiązane Dokumenty
- [TDD-001-V2](../engineering/tdd-v2.md)
- [ROADMAP-001](../pre-production/roadmap.md)
- [TEST-PLAN-001](test-plan.md)
