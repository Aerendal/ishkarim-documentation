---
id: ROADMAP-001
title: "Product Roadmap - System Dokumentacji Ishkarim"
type: roadmap
status: draft
created: 2025-12-26

dependencies:
  - id: VISION-001-V2
    type: requires
    status_constraint: [approved]
    reason: "Roadmap implementuje fazy wizji"

impacts:
  - id: IMPL-PLAN-001
    type: informs
    reason: "Plan implementacji sekwencjonuje milestone'y roadmapy"
    cascade: true

context_snapshot:
  timeline: "12 miesięcy (MVP: 3mies, V1.0: 6mies, V1.5: 12mies)"
  budget: "$48,000 development"
  team_size: 2

evidence_ids:
  - E-086
  - E-098
---

# Product Roadmap

## Przegląd Timeline

### Faza 1: MVP (Miesiące 1-3)
**Cel**: Proof of concept z funkcjonalnością rdzeniową
**Deliverables**:
- Parser (python-frontmatter + markdown-it-py)
- Validator (schematy Pydantic)
- Graph Builder (NetworkX)
- Podstawowe GUI (PySide6)
- Detekcja luk: E110, E120, E140

**Kryteria Sukcesu**:
- Parsowanie 100+ docs w < 5s
- Wykrywanie broken dependencies
- Interaktywna wizualizacja grafu

### Faza 2: V1.0 (Miesiące 4-6)
**Cel**: System production-ready
**Deliverables**:
- Pełna detekcja luk (E110-E160)
- File watcher (Watchdog)
- Hybrid storage (Markdown + SQLite FTS5)
- Proactive assistant (sugestie następnych kroków)

**Kryteria Sukcesu**:
- 80% code coverage
- < 100ms search dla 10k docs
- 99.9% uptime

### Faza 3: V1.5 (Miesiące 7-12)
**Cel**: Zaawansowane funkcje
**Deliverables**:
- Integracja Ollama (opcjonalny AI assist)
- Generowanie raportów (HTML, CSV, Markdown)
- Operacje bulk
- Architektura pluginów

**Kryteria Sukcesu**:
- 5+ dostępnych pluginów
- Export do 3+ formatów
- Zadowolenie użytkowników > 4.5/5

## Milestone'y

| Milestone | Data | Zależności | Metryki Sukcesu |
|-----------|------|------------|-----------------|
| M1: Parser + Validator | Miesiąc 1 | TDD-001-V2 (design-complete) | 100 docs sparsowanych |
| M2: Graph + GUI | Miesiąc 2 | M1 complete | Wizualizacja działa |
| M3: MVP Release | Miesiąc 3 | M2 complete, TEST-PLAN passed | Beta users: 5+ |
| M4: Gap Engine Full | Miesiąc 5 | MVP feedback | Wszystkie E110-E160 działają |
| M5: V1.0 Release | Miesiąc 6 | 80% coverage, NFRs performance | Public release |
| M6: V1.5 Features | Miesiąc 12 | V1.0 adoption > 50 users | Ekosystem pluginów |

## Mitygacja Ryzyka

| Ryzyko | Prawdopodobieństwo | Wpływ | Mitygacja |
|--------|-------------------|-------|-----------|
| Degradacja wydajności przy skali | Medium | High | Benchmark wcześnie (E-146), SQLite FTS5 |
| Problemy licencyjne Qt | Low | High | PySide6 LGPL potwierdzone (ADR-001) |
| Scope creep | High | Medium | Rygorystyczna bramka REQ-FREEZE (PRD) |

## Graf Decyzyjny

**Kontekst T₀**: Potrzeba fazowania roadmapy
**Rozważane opcje**:
- A: Big bang release (wszystkie features miesiąc 6)
- B: Iteracyjne (MVP → V1.0 → V1.5)
- C: Continuous delivery (weekly releases)

**Odrzucone**:
- A: Zbyt ryzykowne, brak wczesnego feedbacku
- C: Zbyt duży overhead dla 2-osobowego zespołu

**Wybrane**: B (Iteracyjne)
**Uzasadnienie**: Balans ryzyko/feedback/zasoby, sprawdzony pattern MVP→V1.0
**Dowód**: [E-086] Analiza 10 podobnych projektów, 8/10 używało iteracyjnego

## Powiązane Dokumenty
- [VISION-001-V2](vision-v2.md)
- [BIZ-CASE-001-V2](business-case-v2.md)
- [IMPL-PLAN-001](../implementation/implementation-plan.md)
