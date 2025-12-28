# Changelog

Wszystkie istotne zmiany w projekcie Ishkarim Documentation będą dokumentowane w tym pliku.

Format bazuje na [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
a projekt stosuje [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planowane (Proposals)
- **Research Branch Templates** (+7 szablonów: Hypothesis, Experiment Log, PoC, Spike, Research Findings, Alternative Exploration, Concept Branch)
- **Living Documentation Framework** (+6 mechanizmów: Extended Lifecycle, Semantic Versioning, Dynamic Cross-References, Auto-Validation, Deprecation Workflow, Migration)
- **Decision Templates Enhancement** (+5 szablonów: Decision Log, Trade-off Analysis, Option Comparison Matrix, Go/No-Go Decision, Decision Reversal)
- **Concept Exploration Workflows** (+4 workflows: Tech Exploration, Business Innovation, Risk Mitigation, Parallel Branching)

**Impact:** +19 szablonów, +6 mechanizmów, +~300-350 połączeń w grafie zależności

---

## [1.4.0] - 2025-12-28

### Added - Cross-References i Graf Zależności

**Cross-References dla 26 wyekstrahowanych szablonów:**
- Dodano pełne sekcje "Document Cross-References" do wszystkich 26 szablonów
- **Sprints (11):** Dependencies, Impacts, Related, Satellites dla każdego dokumentu sprintowego
- **Roadmaps (6):** Pełne powiązania strategiczne (Vision → Roadmap → PRD → Execution)
- **Atomic (8):** Satelitarne powiązania (parent docs → atomic instances → feedback)
- **Migration (1):** Dependencies na AS-IS/TO-BE Architecture, impacts na Implementation/Test Plans

**Graf Zależności - 3 nowe grafy Mermaid:**
- **Graf F: Sprint Workflow (Szczegółowy)** - kompletny cykl 11 dokumentów sprintowych
  * Plan → Backlog → DoR/DoD → Execution → Impediments → Review → Retro → Actions → Approval
  * Cross-sprint feedback loops (action items → next planning)
- **Graf G: Roadmap & Planning Workflow** - strategiczna warstwa planowania
  * Roadmap Product → Capacity Plan → Risk Register → Release Checklist → KPI Dashboard → Postmortem
  * Strategic decision-making layer nad execution documents
- **Graf H: Atomic Satellites Network** - ekosystem satelitarnych szablonów
  * Parent docs (PRD/TDD/Sprint/Roadmap) → Create instances → TODO/DoR/DoD/Evidence/Approval
  * Reusable, lightweight documentation pattern

### Changed

**README.md:**
- Badge Połączenia: 1,096 → **1,367** (+271, +25%)
- Statystyki: zaktualizowane wszystkie wzmianki o połączeniach
- Cross-References breakdown: informs 565 (41%), influences 419 (31%), requires 262 (19%), blocks 121 (9%)
- Top Documents ranking: **ROADMAP-PROD nowym liderem** (28 zależności)
  * Top 5: ROADMAP-PROD (28), PROJECT-CHARTER (20), PRD (20), SPRINT-PLAN (18), CAPACITY-PLAN (15)
- Impact Summary: rozdzielone current (1,367) vs planned (+300-350) connections

**dependency_graph.md:**
- Dokumenty: 132 → **158** (+26, +20%)
- Dependencies: 376 → **471** (+95)
- Impacts: 405 → **509** (+104)
- Related: 315 → **387** (+72)
- Total połączeń: 1,096 → **1,367** (+271, +25%)
- Linie kodu: 743 → 936 (+193 linii, +26%)

**Cross-References w 26 szablonach:**
- Każdy szablon: 4 sekcje (Dependencies, Impacts, Related, Satellites)
- Średnio ~100 linii Cross-References na szablon
- Total dodane: **2,615 linii** szczegółowych powiązań
- Unikalne zależności (nie copy-paste) dla każdego szablonu

### Statistics

**Pokrycie Cross-References:**
- Przed: 148/148 (100%)
- Po: **174/174 (100%)**
- Wzrost: +26 szablonów z pełnymi CR

**Połączenia w grafie:**
- Base (148 szablonów): 1,096 połączeń
- Nowe (26 szablonów): +271 połączeń
- **Total: 1,367 połączeń**
- Średnio połączeń/dokument: ~8.7

**Rozkład typów relacji:**
- informs: 565 (+122, 41% total)
- influences: 419 (+193, 31% total)
- requires: 262 (+48, 19% total)
- blocks: 121 (+47, 9% total)

**Nowe dokumenty w Top 15:**
- ROADMAP-PROD: #1 (28 deps) - nowy lider!
- SPRINT-PLAN: #4 (18 deps)
- CAPACITY-PLAN: #5 (15 deps)
- RISK-REGISTER: #8 (12 deps)
- POSTMORTEM: #12 (10 deps)

### Key Insights

**Nowa warstwa strategiczna:**
- Roadmaps tworzą strategic layer nad execution (Sprints, PRD, TDD)
- ROADMAP-PROD wyprzedził PRD jako najbardziej referencowany dokument
- Strategic planning → Capacity → Risk → Execution flow

**Workflow chains:**
- Sprint cycle: Plan → Execute → Review → Improve → Next Sprint
- Roadmap cycle: Vision → Roadmap → PRD → Sprints → Release → Postmortem
- Atomic satellites: Parent → Instance → Feedback → Parent update

**25% wzrost połączeń:**
- 271 nowych connections z 26 szablonów
- Bogate powiązania z istniejącymi dokumentami
- Cross-category dependencies (Roadmaps ↔ Sprints ↔ PRD ↔ Atomic)

---

## [1.3.0] - 2025-12-28

### Added - Ekstrakcja Szablonów z Meta-Dokumentów
- **26 nowych szablonów** wyekstrahowanych do dedykowanych katalogów:
  - **Sprints (11):** sprint-plan, sprint-backlog, sprint-dor, sprint-dod, sprint-impediments, sprint-review, sprint-retro, sprint-action-items, sprint-scope-change, sprint-metrics, sprint-approval
  - **Roadmaps (6):** roadmap-product, capacity-plan, risk-register, release-checklist, postmortem-template, kpi-dashboard-spec
  - **Atomic (8):** TODO-template, DoR-template, DoD-template, Approval-template, Evidence-template, risk-item-template, release-checklist-atom, postmortem-atom
  - **Migration (1):** migration_plan_doc

### Changed
- **README.md:** Zaktualizowane statystyki 148 → 174 szablony
- **README.md:** Dodane 4 nowe sekcje kategorii (Sprints, Roadmaps, Atomic, Migration)
- **README.md:** Zaktualizowana struktura katalogów z nowymi kategoriami
- **README.md:** Zaktualizowana tabela rozkładu według kategorii (10 kategorii)
- **dokumentacja_typy.md:** Dodane 4 nowe sekcje z linkami do wyekstrahowanych szablonów
- **Propozycje:** Impact Summary zaktualizowany (Current: 174, Planned: +19, Future: 193)

### Fixed
- Wypełnione 4 puste katalogi: sprints/, roadmaps/, atomic/, migration/
- Szablony wyekstrahowane z meta-dokumentów do właściwych lokalizacji

### Statistics
- **Before:** 148 szablonów (4 puste katalogi)
- **After:** 174 szablony (wszystkie katalogi wypełnione)
- **Increase:** +26 szablonów (+17.6%)
- **Categories:** 6 → 10 (+4 nowe)
- **Total lines added:** 733 (templates) + ~300 (documentation updates)

### Source Files
- Sprints: Wyekstrahowane z `supporting/templates-overviews/sprinty_pliki_satelitarne_i_szablony_templates_sprints.md`
- Roadmaps/Atomic: Wyekstrahowane z `supporting/templates-overviews/roadmaps_satellite_templates_templates_roadmaps_templates_atomic.md`
- Migration: Skopiowane z `produkcyjna/migration_plan_doc.md`

---

## [1.2.0] - 2025-12-28

### Added
- **Propozycje Ulepszeń** - 5 szczegółowych raportów w `docs/proposals/`:
  - `PROPOZYCJA-1-Research-Branch-Templates.md` (32KB)
  - `PROPOZYCJA-2-Living-Documentation-Framework.md` (34KB)
  - `PROPOZYCJA-3-Decision-Templates-Enhancement.md` (38KB)
  - `PROPOZYCJA-4-Concept-Exploration-Workflows.md` (32KB)
  - `PODSUMOWANIE-INTEGRUJACE-Wszystkie-Propozycje.md` (28KB)
- Sekcja **🔮 Propozycje Ulepszeń** w README z opisem wszystkich propozycji
- ROI analysis dla każdej propozycji (7.5x Year 1)
- Implementation roadmap z priorytetami (P1/P2/P3)

### Changed
- README badges: zaktualizowane metryki (+19 planned templates, +~300 planned connections)
- README: dodana historia projektu dla 2025-12-28
- README: data ostatniej aktualizacji → 2025-12-28

### Documentation
- Total: 164KB nowej dokumentacji (~65,000 słów)
- Business value: $52K → $500K benefits (projected)
- Knowledge retention improvement: 30% → 90% (projected)

---

## [1.1.0] - 2025-12-27

### Added
- **Polskie badges** w README (10 badges w 3 liniach):
  - Licencja CC-BY-4.0
  - Język Polski
  - Główny język, Rozmiar repo
  - Ostatni commit, GitHub topics, Made in Poland
  - Szablony: 148, Cross-References: 100%, Połączenia: 1,096
- **LICENSE file** - Creative Commons Attribution 4.0 International (CC BY 4.0)
- **GitHub Topics** (15): documentation, templates, project-management, architecture, arc42, c4-model, cross-references, dependency-graph, agile, sprint-management, software-development, engineering, requirements, technical-documentation, polish

### Changed
- Repository visibility: public
- Repository description: "Comprehensive documentation templates system with Cross-References - 148 templates for project documentation"

---

## [1.0.0] - 2025-12-27

### Added - Konsolidacja i Cross-References
- **148 szablonów** z 100% pokryciem Cross-References
- **Konsolidacja** 16 nowych szablonów z Desktop do Ishkarim:
  - **Sprint Management (5):** Core, Discovery, Hardening, Release, Infra
  - **Architecture Analysis (7):** AS-IS, TO-BE, Problems, Refactoring, Anti-Patterns, Integration Points, Module Analysis
  - **Operations (2):** Playbook - Incident Response, Rules Specification
  - **Meta (2):** Documentation Meta, System Tests Framework
- **Document Cross-References** dla wszystkich 148 szablonów:
  - Dependencies (Co napędza ten dokument)
  - Impacts (Co ten dokument popycha do przodu)
  - Related Documents (Powiązane dokumenty)
  - Satellite Documents (Dokumenty satelitarne: TODO, Evidence, DoR, DoD, Approval)
- Total dodane: **8,230 linii** wartościowej treści Cross-References

### Added - Graf Zależności
- **dependency_graph.md** - kompletny graf zależności:
  - **1,096 połączeń** między 132 dokumentami
  - **5 diagramów Mermaid**:
    - Graf A: Przedprodukcyjna (15 dokumentów)
    - Graf B: Produkcyjna (19 dokumentów)
    - Graf C: Pełny graf (30 top dokumentów)
    - Graf D: Architecture Transformation Workflow (nowy)
    - Graf E: Sprint Types Workflow (nowy)
- Top Documents ranking (najczęściej referenced)
- Workflow chains: Architecture Transformation, Przedprodukcyjna, Produkcyjna, Sprint Management

### Added - Katalog
- **dokumentacja_typy.md** - zaktualizowany katalog:
  - 3 nowe sekcje: Sprint Management, Architecture Analysis, Supporting Documentation
  - Indeksowanie wszystkich 16 nowych szablonów
  - Total: 148 szablonów w 6 kategoriach

### Added - README
- **README.md** - kompletny polski README (505 linii):
  - Statystyki systemu
  - Kategorie szablonów (Przedprodukcyjna, Produkcyjna, Branżowa, Supporting, Examples)
  - Cross-References system documentation
  - Graf zależności overview
  - Nowe szablony (16) z opisami
  - Jak używać (5-step guide)
  - Przykłady użycia (3 scenariusze)
  - Konwencje i standardy
  - Statystyki szczegółowe (rozkład, top documents)
  - Linki szybkiego dostępu

### Added - Git Infrastructure
- **.gitignore** - Obsidian, temp files, images
- **Git repository** initialized with proper structure
- **GitHub repository:** https://github.com/Aerendal/ishkarim-documentation

### Changed
- Struktura katalogów zorganizowana według kategorii:
  - `docs/templates/przedprodukcyjna/` (30 szablonów)
  - `docs/templates/produkcyjna/` (63 szablony)
  - `docs/templates/branzowa/` (16 szablonów)
  - `docs/templates/supporting/` (16 szablonów)
  - `docs/templates/examples/` (13 przykładów)
  - `docs/templates/specs/` (4 specyfikacje)

---

## [0.1.0] - Pre-2025-12-27

### Initial State
- Szablony rozproszone w różnych lokalizacjach (Desktop, Pobrane, Ishkarim)
- Brak Cross-References między dokumentami
- Brak grafu zależności
- Brak centralnego katalogu
- Brak dokumentacji README

---

## Statystyki Version History

| Version | Data | Szablony | Połączenia | Cross-Ref Coverage | Główne Zmiany |
|---------|------|----------|------------|-------------------|---------------|
| **1.4.0** | 2025-12-28 | 174 (+19 planned) | **1,367** (+~300 planned) | **100%** | Cross-Ref + Graf update |
| **1.3.0** | 2025-12-28 | 174 (+19 planned) | 1,096 (+~300 planned) | 100% | Ekstrakcja 26 szablonów |
| **1.2.0** | 2025-12-28 | 148 (+19 planned) | 1,096 (+~300 planned) | 100% | 5 Proposals, Roadmap |
| **1.1.0** | 2025-12-27 | 148 | 1,096 | 100% | Badges, LICENSE, Topics |
| **1.0.0** | 2025-12-27 | 148 | 1,096 | 100% | Konsolidacja, CR, Graf, README |
| **0.1.0** | Pre-2025 | ~132 | 0 | 0% | Initial templates |

---

## Legenda Typów Zmian

- **Added** - nowe funkcje, szablony, dokumenty
- **Changed** - zmiany w istniejących funkcjach
- **Deprecated** - funkcje/szablony przestarzałe, ale nadal dostępne
- **Removed** - usunięte funkcje/szablony
- **Fixed** - poprawki błędów
- **Security** - poprawki bezpieczeństwa
- **Documentation** - zmiany w dokumentacji
- **Planowane** - planned features (Unreleased)

---

## Links

- **Repository:** https://github.com/Aerendal/ishkarim-documentation
- **Katalog:** [docs/templates/dokumentacja_typy.md](docs/templates/dokumentacja_typy.md)
- **Graf Zależności:** [docs/dependency_graph.md](docs/dependency_graph.md)
- **Propozycje:** [docs/proposals/](docs/proposals/)
- **Licencja:** [LICENSE](LICENSE) (CC-BY-4.0)

---

**Wygenerowano z:** [Claude Code](https://claude.com/claude-code)
