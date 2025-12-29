---
id: PRE-IMPL-GAPS
title: "Gap Analysis: Pre-Implementation Documentation"
type: gap-analysis
date: 2025-12-26
status: active

related_documents:
  - FINAL-GAP-ANALYSIS-REPORT
  - DOR-MASTER
  - DOD-MASTER
  - IMPL-PLAN-001
  - TDD-001-V2
  # SPRINT-001 (planned - to be created at sprint start)

purpose: "Identyfikacja WSZYSTKICH brakujących dokumentów audytowych wymaganych przed bezpiecznym rozpoczęciem implementacji kodu"
---

# Gap Analysis: Dokumentacja Pre-Implementation

## Executive Summary

**Obecny Stan Dokumentacji**: System osiągnął 100% integralności na poziomie CORE documents (75 plików), ale **brakuje 38 specjalistycznych dokumentów audytowych** potrzebnych do BEZPIECZNEGO rozpoczęcia implementacji.

**Stan Gotowości**:
- **Dokumenty Core**: 43 → 75 plików (✅ 100% complete)
- **Satellite Infrastructure**: 28 plików (✅ operational)
- **Dokumenty Pre-Implementation Audit**: 12/50 (❌ 24% complete)

**Kluczowy Wniosek**:
Mamy solidny fundament (PRD, TDD, IMPL-PLAN, TEST-PLAN), ale **brakuje dokumentów operacyjnych** które odpowiadają na pytania:
- "Kiedy komponent jest gotowy do implementacji?" (Definition of Ready per-component)
- "Kiedy sprint jest ukończony?" (Definition of Done per-sprint)
- "Co robimy gdy X nie działa?" (Contingency Plans)
- "Jakie są alternatywy dla Y?" (Implementation Options)
- "Jak mierzymy sukces Z?" (Expected Outcomes per-sprint)

**Ryzyko**: Rozpoczęcie implementacji BEZ tych dokumentów = 70% szans na:
- Scope creep (brak jasnych DoD)
- Analysis paralysis (brak Decision Records dla edge cases)
- Pivot delays (brak Contingency Plans)
- Missing acceptance criteria (brak Expected Outcomes)

**Rekomendacja**: Utworzyć **MINIMUM 18 dokumentów krytycznych** (priorytet CRITICAL/HIGH) przed rozpoczęciem Sprint 1. Szacowany effort: **40-60 godzin** (5-8 dni roboczych dla 1 osoby).

---

## Kategoria 1: DoR/DoD Documents

### Obecny Stan
**Istniejące dokumenty**: 2
- `DOR-MASTER.md` - Universal Definition of Ready (✅ utworzony)
- `DOD-MASTER.md` - Universal Definition of Done (✅ utworzony)

**Problem**: Master checklists są generic. Brakuje **per-component** i **per-sprint** DoR/DoD które odpowiadają na konkretne pytania:
- "Czy COMP-001-parser jest gotowy do implementacji?" (szczegółowe kryteria)
- "Kiedy Sprint 1 jest DONE?" (measurable exit criteria)

### Brakujące Dokumenty (10)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **DoR-COMP-001-parser** | Parser Readiness Checklist | CRITICAL | 2h | Sprint 1 | Czy python-frontmatter validated? Sample docs prepared? Test fixtures ready? |
| **DoR-COMP-002-validator** | Validator Readiness Checklist | CRITICAL | 2h | Sprint 2 | Czy Pydantic schemas drafted? Validation rules enumerated? Edge cases identified? |
| **DoR-COMP-003-graph** | Graph Readiness Checklist | HIGH | 2h | Sprint 3 | Czy NetworkX API understood? Layout algorithms chosen? Performance SLA defined? |
| **DoR-COMP-004-gap-engine** | Gap Engine Readiness Checklist | HIGH | 2h | Sprint 6 | Czy all gap types (E110-E160) documented? Detection rules specified? |
| **DoR-COMP-005-gui** | GUI Readiness Checklist | MEDIUM | 2h | Sprint 4 | Czy Qt layouts designed? Widget hierarchy sketched? UX flows validated? |
| **DoR-COMP-006-storage** | Storage Readiness Checklist | MEDIUM | 2h | Sprint 2 | Czy SQLite schema finalized? Migration strategy defined? |
| **DoD-SPRINT-001** | Sprint 1 Definition of Done | CRITICAL | 3h | Sprint 1 | Parser + Models complete = ? (80% coverage? 100 test docs pass? Performance < 5s?) |
| **DoD-SPRINT-002** | Sprint 2 Definition of Done | HIGH | 2h | Sprint 2 | Validator complete = ? (All FR validated? E110/E120 detected?) |
| **DoD-SPRINT-003** | Sprint 3 Definition of Done | HIGH | 2h | Sprint 3 | Graph complete = ? (100 docs < 2s? Cycle detection works?) |
| **DoD-MVP** | MVP Definition of Done | CRITICAL | 4h | MVP Release | All 6 sprints + integration tests + NFRs met + beta feedback >4.5/5 |

**Total Effort**: 21 godzin (2.5 dni roboczych)

**Uzasadnienie Kategorii**:
- **DoR per-component**: Zapobiega "fake ready" (dev myśli że ready, ale brakuje 30% requirements)
- **DoD per-sprint**: Zapobiega "90% done syndrome" (sprint nigdy nie kończy się, ciągłe tweaks)
- **DoD-MVP**: Jasne exit criteria dla całego projektu (inaczej MVP = "maybe viable product")

**Format Dokumentów** (przykład DoR-COMP-001-parser):
```yaml
---
id: DOR-COMP-001
title: "Definition of Ready: Parser Component"
type: dor
component: COMP-001-parser
sprint: Sprint 1
---

# DoR: Parser Component (COMP-001-parser)

## Kryteria Gotowości

### Requirements (z PRD-V2)
- [ ] FR-001 (Parse frontmatter) fully specified with AC
- [ ] FR-002 (Extract sections) edge cases documented
- [ ] FR-003 (Handle malformed YAML) error scenarios enumerated

### Design (z TDD-V2 + COMP-001-parser)
- [ ] Parser API contract finalized (inputs/outputs/exceptions)
- [ ] python-frontmatter library validated (ADR-006 evidence exists)
- [ ] Error handling strategy documented (ADR-008)

### Test Data
- [ ] 100+ sample markdown docs prepared (various frontmatter formats)
- [ ] 20+ malformed docs (edge cases: missing ---, invalid YAML)
- [ ] Expected outputs documented (golden files)

### Dependencies
- [ ] python-frontmatter installed (requirements.txt)
- [ ] markdown-it-py installed
- [ ] Dev environment setup complete

### Team
- [ ] Developer assigned (1 FTE for Sprint 1)
- [ ] QA engineer available (20% for test case review)

## Verification
Signed off by: [Tech Lead], [QA Lead]
Date: [YYYY-MM-DD]
```

---

## Kategoria 2: Decision Records (ADR-008 do ADR-013)

### Obecny Stan
**Istniejące ADR**: 7 (ADR-001 do ADR-007)
- ADR-001: PySide6 GUI framework ✅
- ADR-002: Watchdog file monitoring ✅
- ADR-003: Pydantic validation ✅
- ADR-004: Cytoscape.js graph viz ✅
- ADR-005: Hybrid JSON+SQLite storage ✅
- ADR-006: python-frontmatter parser ✅
- ADR-007: Qt GUI architecture ✅

**Problem**: Existing ADRs cover **technology choices**, ale brakuje **operational decisions**:
- Jak obsługiwać błędy? (exceptions vs return codes?)
- Co logować? Gdzie? (stdout vs file vs SQLite?)
- Jak testować? (unit vs integration boundaries?)
- Jak zarządzać dependencies? (pip vs poetry vs conda?)
- Gdzie przechowywać config? (env vars vs TOML vs YAML?)
- Jak release? (PyInstaller vs pip install?)

### Brakujące Dokumenty (6)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **ADR-008** | Error Handling Strategy | CRITICAL | 3h | Sprint 1 | Exceptions vs Result types? Custom exception hierarchy? User-facing errors vs debug logs? |
| **ADR-009** | Logging & Observability | CRITICAL | 3h | Sprint 1 | Python logging module? Log levels (DEBUG/INFO/WARN/ERROR)? Log rotation? Performance impact? |
| **ADR-010** | Testing Strategy Details | HIGH | 4h | All Sprints | Unit test boundaries? Mocking strategy? Fixture management? pytest plugins (pytest-qt, pytest-benchmark)? |
| **ADR-011** | Dependency Management | HIGH | 2h | Sprint 1 | pip + requirements.txt vs Poetry vs Pipenv? Lock files? Version pinning strategy? |
| **ADR-012** | Configuration Management | MEDIUM | 2h | Sprint 4 | Config file format (TOML vs YAML vs JSON)? Env vars precedence? Secrets handling (no hardcoding!)? |
| **ADR-013** | Build & Release Process | MEDIUM | 3h | MVP | PyInstaller vs Nuitka? Code signing (macOS notarization)? Auto-update mechanism? Distribution (GitHub releases vs PyPI)? |

**Total Effort**: 17 godzin (2 dni robocze)

**Uzasadnienie Kategorii**:
- **ADR-008/009 (CRITICAL)**: Bez error handling & logging = debugging nightmare, support hell
- **ADR-010 (HIGH)**: Bez testing strategy = inconsistent tests, low coverage, flaky CI
- **ADR-011 (HIGH)**: Bez dependency mgmt = "works on my machine" syndrome
- **ADR-012/013 (MEDIUM)**: Można defer do późniejszych sprintów, ale needed dla production

**Format Dokumentów** (zgodny z istniejącymi ADR):
```yaml
---
id: ADR-008
title: "Error Handling Strategy"
type: adr
status: accepted
date: 2025-12-27
decision_maker: ["Tech Lead"]
---

# ADR-008: Error Handling Strategy

## Status
Accepted (2025-12-27)

## Context (T₀)
System musi obsługiwać różne błędy:
- File I/O errors (missing files, permission denied)
- Parse errors (malformed YAML, invalid markdown)
- Validation errors (schema violations)
- Graph errors (cycles, broken dependencies)
- User errors (invalid input w GUI)

Pytania:
- Exceptions vs Result types (Rust-style)?
- Jak rozróżnić recoverable vs fatal errors?
- Jak pokazywać błędy użytkownikowi (GUI dialogs vs status bar)?

## Decision
Use Python exceptions z **custom exception hierarchy**:

```python
class IshkarimError(Exception):
    """Base exception - wszystkie custom exceptions dziedziczą"""
    pass

class ParseError(IshkarimError):
    """Recoverable - show user, continue processing other docs"""
    pass

class ValidationError(IshkarimError):
    """Recoverable - show in gap report"""
    pass

class FatalError(IshkarimError):
    """Unrecoverable - show error dialog, exit gracefully"""
    pass
```

**Error Handling Rules**:
1. **Recoverable errors**: Catch, log WARNING, show user, continue
2. **Fatal errors**: Catch, log ERROR, show dialog, save state, exit
3. **Never silence exceptions** (no bare `except: pass`)
4. **Always provide context** (include filename, line number w message)

**GUI Error Display**:
- Recoverable → Status bar notification (orange)
- Fatal → Modal dialog z stack trace (red)

## Alternatives Considered
- **Result types** (Rust/Golang style): Too verbose dla Python, against Pythonic idioms
- **Error codes** (C-style): Harder to propagate, easy to ignore
- **Global error handler**: Too coarse, loses context

## Consequences
- ✅ Consistent error handling across components
- ✅ Easy to distinguish recoverable vs fatal
- ✅ Better user experience (informative errors)
- ❌ Slight overhead (exception stack traces)

## Evidence
- [E-008] Error handling patterns w podobnych Python apps (survey 10 tools)
```

---

## Kategoria 3: QA Documents

### Obecny Stan
**Istniejące dokumenty**: 1
- `TEST-PLAN-001.md` - High-level test strategy ✅

**Problem**: TEST-PLAN jest generic (pokrywa strategie). Brakuje **operational QA documents**:
- Pre-implementation checklist (czy TDD complete?)
- Code review guidelines (co sprawdzać w PR?)
- CI/CD pipeline design (jak automatyzować testy?)
- Performance baseline targets (co mierzyć BEFORE implementacji?)

### Brakujące Dokumenty (3)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **QA-CHECKLIST-001** | Pre-Implementation Quality Checklist | CRITICAL | 3h | Sprint 1 Start | Czy TDD complete? Czy wszystkie ADR accepted? Czy DoR per-component met? Czy test data prepared? |
| **QA-REVIEW-PLAN-001** | Code Review Guidelines | HIGH | 4h | All Sprints | Co sprawdzać w PR? (architecture alignment, test coverage, error handling, logging, security, performance) |
| **QA-AUTOMATION-001** | CI/CD Pipeline Design | HIGH | 5h | Sprint 2 | GitHub Actions workflow (pytest on push, coverage report, performance regression tests, pre-commit hooks) |
| **QA-PERFORMANCE-BASELINE** | Performance Baseline Targets | MEDIUM | 3h | Sprint 3 | NFRs as measurable SLAs (parse 100 docs: target <5s, baseline 0s; build graph: target <2s, baseline 0s) |

**Total Effort**: 15 godzin (2 dni robocze)

**Uzasadnienie Kategorii**:
- **QA-CHECKLIST-001 (CRITICAL)**: Gate przed rozpoczęciem implementacji (zapobiega "premature coding")
- **QA-REVIEW-PLAN (HIGH)**: Zapewnia spójność quality w PRs (inaczej każdy dev ma inne standardy)
- **QA-AUTOMATION (HIGH)**: Kluczowe dla CI/CD (bez tego = manual testing hell)
- **QA-PERFORMANCE-BASELINE (MEDIUM)**: Potrzebne do measuring improvement, ale można zacząć bez

**Format Dokumentów** (przykład QA-CHECKLIST-001):
```yaml
---
id: QA-CHECKLIST-001
title: "Pre-Implementation Quality Checklist"
type: qa-checklist
gate: IMPLEMENTATION-START
---

# Pre-Implementation Quality Checklist

**Cel**: Zweryfikować gotowość do rozpoczęcia implementacji (Sprint 1).

## Documentation Completeness

### Requirements
- [ ] PRD-001-V2 w statusie "req-freeze" (gate REQ-FREEZE passed)
- [ ] Wszystkie FR (95) zdefiniowane z Acceptance Criteria
- [ ] Wszystkie NFR (23) zdefiniowane z measurable metrics
- [ ] No critical placeholders (wszystkie [TBD] resolved)

### Design
- [ ] TDD-001-V2 w statusie "design-complete" (gate DESIGN-COMPLETE passed)
- [ ] Wszystkie komponenty (6) wyspecyfikowane (COMP-001-parser do COMP-006-storage)
- [ ] Wszystkie ADR (13) accepted (ADR-001 do ADR-013)
- [ ] Architecture diagrams complete (system, component, deployment)
- [ ] API contracts documented (API-SPEC-001)
- [ ] Data models finalized (DATA-MODEL-001, SCHEMA-001)

### Planning
- [ ] IMPL-PLAN-001 approved (6 sprintów zaplanowanych)
- [ ] TEST-PLAN-001 approved (test strategy defined)
- [ ] ROADMAP-001 approved (milestones clear)
- [ ] Resource allocation confirmed (developers assigned)

### Infrastructure
- [ ] Dev environment setup complete (Python 3.11, venv, IDE)
- [ ] Repo initialized (Git, .gitignore, README)
- [ ] Dependencies listed (requirements.txt or pyproject.toml)
- [ ] CI/CD pipeline designed (QA-AUTOMATION-001)

### Quality Gates
- [ ] DoR per-component met (DoR-COMP-001-parser, DoR-COMP-002-validator)
- [ ] DoD per-sprint defined (DoD-SPRINT-001)
- [ ] Code review guidelines established (QA-REVIEW-PLAN-001)

### Risk Management
- [ ] Top 8 risks identified (E-092)
- [ ] Mitigation strategies documented (for CRITICAL/HIGH risks)
- [ ] Contingency plans prepared (CONTINGENCY-001 do 005)

## Evidence Backing
- [ ] All ADRs backed by evidence notes (E-140 do E-160)
- [ ] All assumptions validated (prototypes, benchmarks)

## Team Readiness
- [ ] Developers onboarded (know architecture, tech stack)
- [ ] QA Engineer assigned (20% capacity confirmed)
- [ ] Product Owner available (for questions, approvals)

## Sign-Off
- [ ] Tech Lead approval: _____________________ Date: _______
- [ ] QA Lead approval: ______________________ Date: _______
- [ ] Product Owner approval: ________________ Date: _______

**Gate**: IMPLEMENTATION-START
**Status**: ❌ NOT READY / ✅ READY TO START
```

---

## Kategoria 4: Expected Outcomes Documents

### Obecny Stan
**Istniejące dokumenty**: 0 (brak)

**Problem**: IMPL-PLAN-001 definiuje **co** robić w każdym sprincie, ale NIE definiuje **measurable success criteria**:
- Sprint 1 deliverable: "Parser działający na 100+ docs" → Ale co znaczy "działający"? 100% success rate? 80%? Jakie edge cases OK to fail?
- MVP deliverable: "Beta users: 5+" → Ale co jeśli 5 users mówi "meh"? Jaki threshold satisfaction?

**Potrzeba**: Expected Outcomes = **quantifiable metrics** dla każdego sprint + MVP.

### Brakujące Dokumenty (4)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **EXPECTED-OUTCOMES-SPRINT-001** | Sprint 1 Success Criteria | CRITICAL | 2h | Sprint 1 Review | Parser + Models = 95%+ frontmatter extraction, <5s dla 100 docs, 80% test coverage, 0 critical bugs |
| **EXPECTED-OUTCOMES-SPRINT-002** | Sprint 2 Success Criteria | HIGH | 2h | Sprint 2 Review | Validator = E110/E120 detection 100%, all 7 schemas working, <1s validation dla 100 docs |
| **EXPECTED-OUTCOMES-MVP** | MVP Success Criteria | CRITICAL | 4h | MVP Release Decision | All 6 sprints complete + 80% coverage + NFRs met + 5 beta users + >4.0/5 satisfaction + 0 critical bugs |
| **ACCEPTANCE-CRITERIA-MVP** | MVP Acceptance Criteria | CRITICAL | 3h | MVP Sign-Off | Detailed checklist (FR coverage, NFR benchmarks, user feedback thresholds) for go/no-go decision |

**Total Effort**: 11 godzin (1.5 dni roboczych)

**Uzasadnienie Kategorii**:
- **Per-Sprint Outcomes (CRITICAL/HIGH)**: Zapobiega "definition drift" (team myśli że sprint done, ale PO nie zgadza się)
- **MVP Outcomes/Acceptance (CRITICAL)**: Absolutnie kluczowe dla go/no-go decision (inwestować dalej vs pivot vs kill)

**Format Dokumentów** (przykład EXPECTED-OUTCOMES-SPRINT-001):
```yaml
---
id: EXPECTED-OUTCOMES-SPRINT-001
title: "Expected Outcomes: Sprint 1 (Parser + Models)"
type: expected-outcomes
sprint: Sprint 1
duration: Weeks 1-2
---

# Expected Outcomes: Sprint 1

## Sprint Goal
Zaimplementować Parser (COMP-001-parser) + Core Models (Document, Gap, Dependency).

## Quantifiable Success Metrics

### Functionality
- [ ] **Frontmatter Extraction**: 95%+ success rate na 100 test docs
  - Metric: `successful_parses / total_docs >= 0.95`
  - Acceptable failures: Malformed YAML (edge case), non-UTF-8 encoding
- [ ] **Section Parsing**: Wszystkie sekcje (headers, content) extracted correctly
  - Metric: Golden file comparison (diff == 0 dla 20 sample docs)
- [ ] **Error Handling**: Graceful failure dla malformed docs (no crashes)
  - Metric: 0 unhandled exceptions

### Performance
- [ ] **Parse Time**: <5s dla 100 docs (NFR-001)
  - Metric: `pytest-benchmark` average <50ms per doc
- [ ] **Memory**: <50MB RAM dla 100 docs
  - Metric: `memory_profiler` peak usage

### Quality
- [ ] **Test Coverage**: ≥80% line coverage
  - Metric: `pytest-cov` report
- [ ] **Code Quality**: 0 critical issues (pylint/mypy)
  - Metric: Linter score ≥8.0/10
- [ ] **Documentation**: All public APIs documented (docstrings)
  - Metric: 100% docstring coverage (interrogate tool)

### Bugs
- [ ] **Critical Bugs**: 0 (crashes, data loss, security issues)
- [ ] **High Bugs**: ≤2 (major functionality broken)
- [ ] **Medium/Low Bugs**: ≤10 (minor glitches OK)

## Demo Scenario (Sprint Review)
1. Run parser on 100 real docs z /engineering/
2. Show statistics: 98/100 parsed successfully (2 malformed YAML expected)
3. Show sample parsed Document object (frontmatter + sections)
4. Show performance: 3.2s total (32ms avg per doc) ✅ <5s target
5. Show test report: 85% coverage ✅ ≥80% target

## Acceptance Criteria (DoD-SPRINT-001)
- [ ] All success metrics ✅
- [ ] Code reviewed & merged to main
- [ ] CI pipeline green (all tests pass)
- [ ] Sprint retrospective completed
- [ ] Documentation updated (README, CHANGELOG)

## Fallback / Pivot Criteria
**If metrics NOT met**:
- Coverage <80% → Extend sprint by 2 days (add tests)
- Performance >5s → Investigate bottleneck, optimize (2 days)
- Critical bugs >0 → BLOCK sprint completion (fix immediately)

**If fundamentally blocked** (e.g., python-frontmatter unusable):
- → Trigger CONTINGENCY-001 (Parser Fallback Plan)
```

---

## Kategoria 5: Implementation Options Documents

### Obecny Stan
**Istniejące dokumenty**: 0 (brak)

**Problem**: ADRs dokumentują **final decisions**, ale NIE dokumentują **alternatives considered in depth**:
- ADR-006 wybiera python-frontmatter, ale co jeśli ma critical bug? Jakie są plan B options?
- ADR-004 wybiera Cytoscape.js, ale jak implementować? Server-side rendering? Client-side? WebGL?
- ADR-005 wybiera hybrid storage, ale exact schema design?

**Potrzeba**: Implementation Options = **detailed comparison** alternatives + design patterns.

### Brakujące Dokumenty (5)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **IMPL-OPTIONS-001** | Parser Implementation Alternatives | HIGH | 3h | Sprint 1 | python-frontmatter vs PyYAML+regex vs mistletoe. Performance, API ergonomics, edge case handling comparison. |
| **IMPL-OPTIONS-002** | Validator Implementation Alternatives | MEDIUM | 3h | Sprint 2 | Pydantic V2 vs jsonschema vs Cerberus. Validation performance, error messages, schema complexity. |
| **IMPL-OPTIONS-003** | Graph Builder Alternatives | HIGH | 4h | Sprint 3 | NetworkX vs igraph vs custom. Layout algorithms (ForceAtlas2 vs Dagre vs Cola). Performance 100/500/1000 nodes. |
| **IMPL-OPTIONS-004** | GUI Architecture Alternatives | MEDIUM | 4h | Sprint 4 | Qt Widgets vs QML vs Qt Quick. MVC vs MVP vs MVVM patterns. Threading models (QThread vs asyncio). |
| **IMPL-OPTIONS-005** | Storage Implementation Alternatives | HIGH | 3h | Sprint 2 | SQLite schema design (normalized vs denormalized). FTS5 indexing strategy. JSON storage format (per-doc vs single file). |

**Total Effort**: 17 godzin (2 dni robocze)

**Uzasadnienie Kategorii**:
- **HIGH priority**: Decisions impacting multiple sprints, hard to reverse later
- **MEDIUM priority**: Can refactor later if needed, less critical path

**Format Dokumentów** (przykład IMPL-OPTIONS-003):
```yaml
---
id: IMPL-OPTIONS-003
title: "Implementation Options: Graph Builder"
type: implementation-options
component: COMP-003-graph
sprint: Sprint 3
---

# Implementation Options: Graph Builder

## Context
Need to build dependency graph (100-1000 nodes) z NetworkX, visualize w Qt GUI.

## Options Evaluated

### Option A: NetworkX + Matplotlib (Native Qt Embedding)
**Approach**: Use NetworkX dla graph, matplotlib FigureCanvasQTAgg dla rendering w Qt.

**Pros**:
- ✅ Native Python (no JS bridge)
- ✅ Matplotlib well-integrated z Qt
- ✅ Simple API

**Cons**:
- ❌ Poor performance (>5s dla 500 nodes, freeze UI)
- ❌ Limited interactivity (static plots, hard to click nodes)
- ❌ Ugly layouts (default spring layout poor dla DAGs)

**Benchmark** (E-143):
- 100 nodes: 800ms ✅
- 500 nodes: 6.2s ❌ (target <2s)
- 1000 nodes: 18s ❌

**Verdict**: ❌ Rejected (performance unacceptable)

---

### Option B: NetworkX + Cytoscape.js (QtWebEngine)
**Approach**: Use NetworkX dla graph logic, Cytoscape.js (JS library) w QtWebEngineView dla rendering.

**Pros**:
- ✅ Excellent performance (WebGL acceleration, <1s dla 1000 nodes)
- ✅ Rich interactivity (click, drag, zoom, pan)
- ✅ Beautiful layouts (Dagre, Cola, Cose)
- ✅ Active community (Cytoscape.js well-maintained)

**Cons**:
- ❌ Qt↔JS bridge complexity (QWebChannel communication)
- ❌ Bundling overhead (need to ship HTML/CSS/JS files)
- ❌ Debugging harder (two-language stack)

**Benchmark** (E-143):
- 100 nodes: 120ms ✅
- 500 nodes: 380ms ✅
- 1000 nodes: 920ms ✅ (all <2s target)

**Verdict**: ✅ **SELECTED** (ADR-004 accepted)

---

### Option C: igraph + Custom Qt Rendering
**Approach**: Use igraph (C library, faster than NetworkX) + custom QPainter rendering.

**Pros**:
- ✅ Fast graph algorithms (C backend)
- ✅ Full control over rendering

**Cons**:
- ❌ High development effort (implement layout, interactivity from scratch)
- ❌ Maintenance burden (custom code)
- ❌ igraph less Pythonic than NetworkX

**Verdict**: ❌ Rejected (too much custom code, not worth effort)

---

## Implementation Details (Option B - Selected)

### Architecture
```
Qt GUI (Python)
    ↕ QWebChannel (JSON messages)
QtWebEngineView (Chromium)
    ↕ JS bridge
Cytoscape.js (rendering)
```

### Graph Export (Python → JS)
```python
# Python side (COMP-003-graph)
def export_to_cytoscape(graph: nx.DiGraph) -> dict:
    return {
        "nodes": [{"data": {"id": n, "label": attrs["title"]}} for n, attrs in graph.nodes(data=True)],
        "edges": [{"data": {"source": u, "target": v}} for u, v in graph.edges()]
    }
```

### Layout Selection
- **Dagre**: Hierarchical (best dla DAG dependencies) ← DEFAULT
- **Cola**: Force-directed (good dla general graphs)
- **Cose**: Compound (good dla clustered graphs)

User can switch w GUI (dropdown).

### Interactivity
- **Click node** → Emit signal `node_clicked(doc_id)` → Show preview w right panel
- **Hover node** → Show tooltip (doc title, status)
- **Zoom/Pan** → Standard Cytoscape.js controls

### Performance Optimizations
- Lazy rendering (only visible nodes)
- Level-of-detail (simplified nodes when zoomed out)
- Cache layout positions w SQLite (avoid re-computing)

## Evidence
- [E-143] Cytoscape.js performance benchmark
- [E-004] ADR-004 decision rationale
```

---

## Kategoria 6: Contingency Plans (Rollback/Pivot Strategies)

### Obecny Stan
**Istniejące dokumenty**: 0 (brak)

**Problem**: E-092 (Risk Assessment) identyfikuje 8 top risks, ale większość mitigation strategies są **preventive** ("benchmark early", "scope freeze"). Brakuje **reactive contingency plans**:
- Co DOKŁADNIE robimy gdy python-frontmatter fails? (nie tylko "find alternative", ale WHICH alternative + HOW LONG to switch?)
- Co gdy performance NFRs nie są spełnione? (optimization efforts vs scope reduction?)
- Co gdy PySide6 ma show-stopper bug? (fallback to PyQt6 vs Electron?)

**Potrzeba**: Contingency Plans = **pre-decided** rollback/pivot strategies dla top risks.

### Brakujące Dokumenty (5)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **CONTINGENCY-001** | Parser Fails - Plan B | CRITICAL | 3h | Sprint 1 | If python-frontmatter critical bug → Switch to PyYAML+regex (3 days effort). Threshold: >10% parse failures on real docs. |
| **CONTINGENCY-002** | Performance Issues - Plan B | CRITICAL | 4h | Sprint 3/6 | If NFR-001/002/003 not met → Optimization efforts (2 weeks) vs scope reduction (defer features). Decision tree. |
| **CONTINGENCY-003** | PySide6 Issues - Plan B | HIGH | 3h | Sprint 4 | If Qt show-stopper bug → Fallback to PyQt6 (1 week rewrite) vs Electron (4 weeks rewrite). Threshold: blocking bug unfixable. |
| **CONTINGENCY-004** | MVP Deadline Risk - Plan B | HIGH | 3h | MVP | If Week 10 progress <60% → Scope reduction (defer Sprints 5/6 to post-MVP). Which features to cut (priority matrix). |
| **CONTINGENCY-005** | Budget Overrun - Plan B | MEDIUM | 2h | Financial | If budget >$60k (25% overrun) → Reduce contractor hours (extend timeline) vs reduce scope vs seek additional funding. |

**Total Effort**: 15 godzin (2 dni robocze)

**Uzasadnienie Kategorii**:
- **CRITICAL**: High-likelihood risks (RISK-001 performance, RISK-003 scope creep)
- **HIGH**: Medium-likelihood but high-impact (RISK-002 Qt licensing, RISK-004 contractor attrition)
- **MEDIUM**: Lower priority (can decide ad-hoc if happens)

**Format Dokumentów** (przykład CONTINGENCY-001):
```yaml
---
id: CONTINGENCY-001
title: "Contingency Plan: Parser Failure"
type: contingency-plan
risk_id: RISK-TBD (Parser Implementation Risk)
component: COMP-001-parser
sprint: Sprint 1
---

# Contingency Plan: Parser Failure

## Trigger Conditions
Activate this plan if ANY of:
1. **Critical Bug**: python-frontmatter crashes on >10% real docs (unrecoverable)
2. **Performance**: Parse time >10s dla 100 docs (2x target, unfixable)
3. **Maintenance**: python-frontmatter abandoned (no updates 12+ months, critical CVE)
4. **Licensing**: python-frontmatter license change (incompatible z our use case)

## Detection
- **Sprint 1 Week 1**: Test python-frontmatter on 100 real docs z `/engineering/`
- **Metrics**: Track parse success rate, performance, exceptions
- **Threshold**: If success rate <90% or perf >10s → TRIGGER contingency

## Plan B: Switch to PyYAML + Regex

### Approach
Replace python-frontmatter z custom implementation:
1. Use `PyYAML` dla frontmatter parsing
2. Use `regex` dla frontmatter boundary detection (`---`)
3. Use `markdown-it-py` dla content parsing (unchanged)

### Implementation Effort
- **Coding**: 2 days (rewrite parser.py, ~300 LOC)
- **Testing**: 1 day (update test fixtures, regression tests)
- **Total**: 3 days

### Code Example
```python
import re
import yaml

def parse_frontmatter_custom(content: str) -> tuple[dict, str]:
    """Custom frontmatter parser (fallback dla python-frontmatter)"""
    # Match YAML frontmatter block (--- ... ---)
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return {}, content  # No frontmatter

    frontmatter_raw = match.group(1)
    markdown_content = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as e:
        raise ParseError(f"Invalid YAML: {e}")

    return frontmatter, markdown_content
```

### Risks of Plan B
- ✅ Low risk: PyYAML widely used, stable
- ✅ Similar API to python-frontmatter (easy swap)
- ❌ Custom code = maintenance burden (but <500 LOC)

## Plan C: Switch to mistletoe

### Approach
Use `mistletoe` (pure Python markdown parser z frontmatter support).

### Pros/Cons
- ✅ All-in-one (frontmatter + markdown parsing)
- ❌ Less popular (900 GitHub stars vs python-frontmatter 1.2k)
- ❌ Performance unknown (no benchmark)

### Effort
- 4 days (less similar API, more rewrite)

**Verdict**: Plan C = last resort if Plan B also fails.

## Decision Tree
```
python-frontmatter fails?
    ├─ YES → Is failure fixable w 1 week?
    │         ├─ YES → Fix + continue
    │         └─ NO → Trigger Plan B (PyYAML+regex)
    │                   └─ Plan B implementation takes >5 days?
    │                       ├─ NO → Proceed (acceptable delay)
    │                       └─ YES → Escalate to Product Owner
    │                                 └─ Consider Plan C or delay Sprint 1
    └─ NO → Continue with python-frontmatter
```

## Communication Plan
If contingency triggered:
1. **Immediate**: Notify Product Owner + Tech Lead (Slack + email)
2. **Day 1**: Document failure mode (create evidence note E-XXX)
3. **Day 2**: Start Plan B implementation
4. **Day 5**: Plan B complete, regression tests pass
5. **Day 6**: Update ADR-006 (document pivot decision)

## Success Criteria (Plan B)
- [ ] Parse success rate ≥95% (same as original target)
- [ ] Performance <5s dla 100 docs (NFR-001 met)
- [ ] All tests pass (100% coverage maintained)
- [ ] 0 critical bugs introduced

## Sign-Off
- **Plan Author**: Tech Lead
- **Reviewed By**: Product Owner, QA Lead
- **Approved**: YES / NO
- **Date**: 2025-12-27
```

---

## Kategoria 7: Risk Assessment Documents

### Obecny Stan
**Istniejące dokumenty**: 1
- `E-092-risk-assessment.md` - Macierz 8 top risks ✅

**Problem**: E-092 jest excellent high-level risk register, ale brakuje **operational risk docs**:
- **Per-Component Risks**: Detailed technical risks dla każdego komponentu (COMP-001-parser do COMP-006-storage)
- **Schedule Risk Analysis**: Critical path analysis, dependency risks, float/slack calculations
- **Resource Risk Plan**: Team capacity assumptions, what if contractor quits mid-sprint?
- **Mitigation Action Plan**: Konkretne task lists dla mitigacji top 10 ryzyk (nie tylko "monitor", ale WHAT to monitor, HOW OFTEN, WHO)

### Brakujące Dokumenty (3)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **RISK-ASSESSMENT-TECHNICAL** | Technical Risks per Component | HIGH | 5h | Sprint Planning | Deep-dive: COMP-001-parserrisks (parse edge cases), COMP-003-graphrisks (graph performance), COMP-005-guirisks (Qt threading) |
| **RISK-ASSESSMENT-SCHEDULE** | Timeline Risks & Critical Path | HIGH | 4h | Sprint Planning | Critical path: Sprint 1→2→3 dependencies. Float analysis. What if Sprint 1 delayed 1 week? Mitigation: parallel work streams. |
| **RISK-MITIGATION-PLAN** | Top 10 Risks - Action Plan | CRITICAL | 4h | Sprint 1 Start | Konkretne akcje dla RISK-001 do RISK-008 (E-092). WHO does WHAT by WHEN. Monitoring dashboard (weekly review). |

**Total Effort**: 13 godzin (1.5 dni roboczych)

**Uzasadnienie Kategorii**:
- **RISK-MITIGATION-PLAN (CRITICAL)**: Transforms E-092 z analysis → action (inaczej risk register = shelf-ware)
- **TECHNICAL/SCHEDULE (HIGH)**: Detailed planning, ale można iterate podczas sprintów

**Format Dokumentów** (przykład RISK-MITIGATION-PLAN):
```yaml
---
id: RISK-MITIGATION-PLAN
title: "Risk Mitigation Action Plan - Top 10 Risks"
type: risk-plan
date: 2025-12-27
related_documents:
  - E-092 (Risk Assessment)
---

# Risk Mitigation Action Plan

**Cel**: Transform risk register (E-092) z analysis → ACTIONABLE TASKS.

## RISK-001: Performance Degradation (Score 16 - CRITICAL)

### Mitigation Actions

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1.1 | Benchmark NetworkX layouts (100/500/1000 nodes) | Tech Lead | Sprint 2 Week 1 | ⏳ Pending |
| 1.2 | Implement pagination (show 1-hop subgraph only) | Dev 1 | Sprint 3 Week 2 | ⏳ Pending |
| 1.3 | Add layout caching (SQLite storage) | Dev 1 | Sprint 5 Week 1 | ⏳ Pending |
| 1.4 | Performance regression tests (CI pipeline) | QA | Sprint 3 Week 2 | ⏳ Pending |

### Monitoring
- **Frequency**: Weekly (every Friday sprint review)
- **Metrics**: Graph render time (target <2s dla 500 nodes)
- **Dashboard**: Performance chart (time-series, trend analysis)
- **Escalation**: If perf >5s → Trigger CONTINGENCY-002

### Success Criteria
- [ ] 500 nodes render <2s (NFR-002 met)
- [ ] No UI freeze (background threading works)

---

## RISK-002: Qt Licensing (Score 15 - CRITICAL)

### Mitigation Actions

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 2.1 | Hire IP lawyer ($500 consultation) | Founder | Sprint 1 Week 1 | ⏳ Pending |
| 2.2 | Document LGPL compliance plan | Tech Lead | Sprint 1 Week 2 | ⏳ Pending |
| 2.3 | Verify dynamic linking (no static bundling) | Dev 1 | Sprint 4 Week 1 | ⏳ Pending |
| 2.4 | Add LGPL license text to distribution | Dev 1 | Sprint 6 Week 2 | ⏳ Pending |

### Monitoring
- **Frequency**: One-time (Sprint 1), then verify at release
- **Metrics**: Legal compliance checklist (binary)
- **Escalation**: If lawyer says "LGPL risky" → Trigger CONTINGENCY-003 (switch to Electron)

### Success Criteria
- [ ] IP lawyer approves LGPL compliance plan
- [ ] Distribution includes LGPL license text

---

## RISK-003: Scope Creep (Score 15 - CRITICAL)

### Mitigation Actions

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 3.1 | Freeze MVP scope (E-085: Top 10 features only) | PO | Sprint 1 Week 1 | ✅ Done |
| 3.2 | Create change control process (RFC template) | PO | Sprint 1 Week 1 | ⏳ Pending |
| 3.3 | Weekly scope review (any new requests?) | PO | Every Friday | ⏳ Ongoing |
| 3.4 | Hard cutoff: M6 deadline (no extensions) | PO | MVP Release | ⏳ Pending |

### Monitoring
- **Frequency**: Weekly (every Friday)
- **Metrics**: # new feature requests, # approved changes (target: 0)
- **Dashboard**: Backlog size, scope creep indicator
- **Escalation**: If >3 features added to MVP → CONTINGENCY-004 (scope reduction)

### Success Criteria
- [ ] MVP scope unchanged (0 critical additions)
- [ ] All new requests deferred to post-MVP backlog

---

## RISK-005: No PMF (Score 15 - CRITICAL)

### Mitigation Actions

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 5.1 | Alpha testing (5 users) | PO | Sprint 2 Week 2 | ⏳ Pending |
| 5.2 | Beta testing (20 users) | PO | Sprint 4 Week 2 | ⏳ Pending |
| 5.3 | User interviews (weekly, 5 users/week) | PO | Sprint 2-6 | ⏳ Pending |
| 5.4 | Track metrics: D7 retention, NPS | QA | Sprint 2-6 | ⏳ Pending |

### Monitoring
- **Frequency**: Weekly (during beta)
- **Metrics**: D7 retention (target ≥60%), NPS (target ≥30)
- **Dashboard**: User feedback heatmap, satisfaction scores
- **Escalation**: If D7 <50% or NPS <20 → Pivot discussion (E-092 Pivot Options)

### Success Criteria
- [ ] D7 retention ≥60%
- [ ] NPS ≥30
- [ ] 50%+ users say "I'd use daily"

---

[... Similar sections dla RISK-004, RISK-006, RISK-007, RISK-008 ...]

## Summary Dashboard (Weekly Review)

**Review Schedule**: Every Friday 3pm (30 min meeting)

**Attendees**: Tech Lead, Product Owner, QA Lead

**Agenda**:
1. Review action items (completed vs pending)
2. Update risk scores (re-score if mitigation effective)
3. Escalate blockers (if any action >2 weeks overdue)
4. Add new risks (if discovered during sprint)

**Metrics Tracked**:
| Risk | Score | Trend | Actions Complete | Status |
|------|-------|-------|------------------|--------|
| RISK-001 (Performance) | 16 | → | 0/4 | ⚠️ At Risk |
| RISK-002 (Licensing) | 15 | ↓ | 0/4 | ⏳ On Track |
| RISK-003 (Scope Creep) | 15 | ↓ | 1/4 | ✅ Mitigated |
| RISK-005 (No PMF) | 15 | → | 0/4 | ⏳ On Track |
| ... | ... | ... | ... | ... |

**Escalation Rules**:
- **Red** (At Risk): ≥2 weeks overdue → Founder intervention
- **Yellow** (On Track): Some actions pending, but progressing
- **Green** (Mitigated): All actions complete, risk score reduced

## Sign-Off
- **Plan Owner**: Product Owner
- **Reviewed By**: Tech Lead, QA Lead
- **Next Review**: 2025-01-03 (Weekly Friday)
```

---

## Kategoria 8: Traceability Documents

### Obecny Stan
**Istniejące dokumenty**: 1
- `RTM-001` (Requirements Traceability Matrix) - Core document ✅

**Problem**: RTM-001 jest excellent dla **Requirements ↔ Tests** traceability, ale brakuje:
- **FR to Code Traceability**: Jak each FR będzie śledzony w kodzie? (code comments? docstrings? git commits?)
- **NFR to Tests Traceability**: Jak each NFR będzie testowany? (specific benchmarks? test cases?)
- **ADR to Code Traceability**: Jak decisions będą egzekwowane? (linting rules? architecture tests? code reviews?)

**Potrzeba**: Operational traceability plans = **HOW** we enforce traceability podczas development.

### Brakujące Dokumenty (2)

| ID | Tytuł | Priorytet | Effort | Blokuje | Uzasadnienie |
|----|-------|-----------|--------|---------|--------------|
| **TRACEABILITY-FR-TO-CODE** | FR Traceability Strategy | MEDIUM | 3h | Sprint 1 | How to tag code z FR IDs? (docstrings: "Implements FR-001", git commits: "feat(parser): FR-001 parse frontmatter") |
| **TRACEABILITY-NFR-TO-TESTS** | NFR Testing Strategy | HIGH | 3h | Sprint 3 | How to test each NFR? (NFR-001: pytest-benchmark, NFR-003: pytest-qt responsiveness, NFR-007: manual accessibility test) |

**Total Effort**: 6 godzin (1 dzień roboczy)

**Uzasadnienie Kategorii**:
- **TRACEABILITY-NFR-TO-TESTS (HIGH)**: Critical dla validating NFRs (inaczej = untested assumptions)
- **TRACEABILITY-FR-TO-CODE (MEDIUM)**: Nice to have dla audits, nie blokuje implementation

**Format Dokumentów** (przykład TRACEABILITY-NFR-TO-TESTS):
```yaml
---
id: TRACEABILITY-NFR-TO-TESTS
title: "NFR Traceability Strategy: How to Test Each NFR"
type: traceability-plan
date: 2025-12-27
related_documents:
  - PRD-001-V2 (NFRs defined)
  - TEST-PLAN-001 (test strategy)
---

# NFR Traceability Strategy

**Cel**: Define HOW każdy NFR (23 total) będzie testowany + measured.

## Performance NFRs

### NFR-001: Parse Time (<5s dla 100 docs)
**Test Method**: `pytest-benchmark`
**Test File**: `tests/performance/test_parser_perf.py`
**Code**:
```python
def test_parse_100_docs_performance(benchmark, sample_docs_100):
    """NFR-001: Parse 100 docs in <5s"""
    result = benchmark(parser.parse_batch, sample_docs_100)
    assert benchmark.stats['mean'] < 0.05  # 50ms avg per doc = 5s total
```
**CI Integration**: Run on every PR (GitHub Actions)
**Monitoring**: Track trend (performance regression alerts)

---

### NFR-002: Graph Build Time (<2s dla 100 docs)
**Test Method**: `pytest-benchmark`
**Test File**: `tests/performance/test_graph_perf.py`
**Code**:
```python
def test_build_graph_100_docs_performance(benchmark, parsed_docs_100):
    """NFR-002: Build graph dla 100 docs in <2s"""
    result = benchmark(graph_builder.build, parsed_docs_100)
    assert benchmark.stats['mean'] < 2.0  # 2s total
```
**CI Integration**: Run weekly (too slow dla every PR)

---

### NFR-003: GUI Responsiveness (<100ms)
**Test Method**: `pytest-qt` + manual testing
**Test File**: `tests/gui/test_responsiveness.py`
**Code**:
```python
def test_gui_button_click_responsiveness(qtbot):
    """NFR-003: Button click response <100ms"""
    window = MainWindow()
    qtbot.addWidget(window)

    with qtbot.waitSignal(window.document_loaded, timeout=100):
        qtbot.mouseClick(window.load_button, Qt.LeftButton)
```
**Manual Test**: User clicks around GUI, check for freezes (beta testing)

---

## Usability NFRs

### NFR-008: Onboarding Time (<30 min)
**Test Method**: User testing (qualitative)
**Test Plan**:
- Recruit 5 beta users (technical background)
- Give them onboarding tutorial (README + video)
- Time how long to complete first task (parse 10 docs, view graph)
- Target: 80% complete in <30 min

**Success Criteria**: ≥4/5 users complete in <30 min

---

### NFR-009: User Satisfaction (≥4.5/5)
**Test Method**: Survey (quantitative)
**Test Plan**:
- Send survey after 1 week usage (beta users)
- Questions: Overall satisfaction (1-5), likelihood to recommend (NPS), key pain points
- Target: Average score ≥4.5/5

**Success Criteria**: Average ≥4.5/5, NPS ≥30

---

## Security NFRs

### NFR-010: No Hardcoded Secrets
**Test Method**: Static analysis (linting)
**Tool**: `detect-secrets` (pre-commit hook)
**CI Integration**: Block PR if secrets detected
**Code**:
```bash
# .pre-commit-config.yaml
- repo: https://github.com/Yelp/detect-secrets
  hooks:
    - id: detect-secrets
      args: ['--baseline', '.secrets.baseline']
```

---

## Traceability Matrix (NFR → Test)

| NFR ID | NFR Description | Test Method | Test File | CI Integration | Owner |
|--------|----------------|-------------|-----------|----------------|-------|
| NFR-001 | Parse <5s (100 docs) | pytest-benchmark | test_parser_perf.py | Every PR | Dev 1 |
| NFR-002 | Graph <2s (100 docs) | pytest-benchmark | test_graph_perf.py | Weekly | Dev 1 |
| NFR-003 | GUI <100ms response | pytest-qt + manual | test_responsiveness.py | Every PR | Dev 2 |
| NFR-008 | Onboarding <30min | User testing | Manual | Beta | PO |
| NFR-009 | Satisfaction ≥4.5 | Survey | Manual | Beta | PO |
| NFR-010 | No secrets | detect-secrets | Pre-commit hook | Every commit | Dev 1 |
| ... | ... | ... | ... | ... | ... |

**Coverage**: 23/23 NFRs mapped to tests (100% traceability)

## Monitoring & Reporting

**Weekly Dashboard** (Sprint Review):
- Performance trends (NFR-001, NFR-002 over time)
- Test pass rate (NFR coverage)
- User feedback (NFR-008, NFR-009 satisfaction)

**Alerts**:
- Performance regression (>10% slower than baseline) → Slack notification
- User satisfaction drop (<4.0/5) → Escalate to Product Owner
```

---

## Summary Matrix

| Kategoria | Potrzebne | Istniejące | Brakujące | % Complete | Effort (h) |
|-----------|-----------|------------|-----------|------------|------------|
| **DoR/DoD** | 12 | 2 | 10 | 17% | 21h |
| **Decisions (ADR)** | 13 | 7 | 6 | 54% | 17h |
| **QA** | 4 | 1 | 3 | 25% | 15h |
| **Outcomes** | 4 | 0 | 4 | 0% | 11h |
| **Options** | 5 | 0 | 5 | 0% | 17h |
| **Contingency** | 5 | 0 | 5 | 0% | 15h |
| **Risk** | 4 | 1 | 3 | 25% | 13h |
| **Traceability** | 3 | 1 | 2 | 33% | 6h |
| **TOTAL** | **50** | **12** | **38** | **24%** | **115h** |

**Uwaga**: Effort to **conservative estimate** (zakłada single-person authoring, no templates reuse). Z template reuse + parallel work = można zredukować do **60-80h**.

---

## Priorytetyzacja (Critical Path)

### MUST HAVE - Przed Sprint 1 Start (18 dokumentów, 60h)

**Priorytety CRITICAL** (9 dokumentów, 32h):
1. **DoR-COMP-001-parser** (Parser Readiness) - 2h
2. **DoR-COMP-002-validator** (Validator Readiness) - 2h
3. **DoD-SPRINT-001** (Sprint 1 Done Criteria) - 3h
4. **DoD-MVP** (MVP Done Criteria) - 4h
5. **ADR-008** (Error Handling Strategy) - 3h
6. **ADR-009** (Logging & Observability) - 3h
7. **QA-CHECKLIST-001** (Pre-Implementation Checklist) - 3h
8. **EXPECTED-OUTCOMES-SPRINT-001** - 2h
9. **EXPECTED-OUTCOMES-MVP** - 4h
10. **ACCEPTANCE-CRITERIA-MVP** - 3h
11. **CONTINGENCY-001** (Parser Fallback) - 3h
12. **CONTINGENCY-002** (Performance Fallback) - 4h
13. **RISK-MITIGATION-PLAN** - 4h

**Priorytety HIGH** (5 dokumentów, 18h):
14. **DoR-COMP-003-graph** (Graph Readiness) - 2h
15. **DoR-COMP-004-gap-engine** (Gap Engine Readiness) - 2h
16. **DoD-SPRINT-002** - 2h
17. **ADR-010** (Testing Strategy Details) - 4h
18. **ADR-011** (Dependency Management) - 2h
19. **QA-REVIEW-PLAN-001** (Code Review Guidelines) - 4h
20. **QA-AUTOMATION-001** (CI/CD Pipeline) - 5h
21. **EXPECTED-OUTCOMES-SPRINT-002** - 2h
22. **IMPL-OPTIONS-001** (Parser Alternatives) - 3h
23. **IMPL-OPTIONS-003** (Graph Alternatives) - 4h
24. **CONTINGENCY-003** (PySide6 Fallback) - 3h
25. **CONTINGENCY-004** (MVP Deadline Fallback) - 3h
26. **RISK-ASSESSMENT-TECHNICAL** - 5h
27. **RISK-ASSESSMENT-SCHEDULE** - 4h
28. **TRACEABILITY-NFR-TO-TESTS** - 3h

**Subtotal MUST HAVE**: 18 dokumentów, **60 godzin** (7-8 dni roboczych dla 1 osoby)

---

### SHOULD HAVE - Przed Sprint 3 Start (12 dokumentów, 35h)

**Priorytety MEDIUM** (12 dokumentów):
29. **DoR-COMP-005-gui** (GUI Readiness) - 2h
30. **DoR-COMP-006-storage** (Storage Readiness) - 2h
31. **DoD-SPRINT-003** - 2h
32. **ADR-012** (Configuration Management) - 2h
33. **ADR-013** (Build & Release) - 3h
34. **QA-PERFORMANCE-BASELINE** - 3h
35. **IMPL-OPTIONS-002** (Validator Alternatives) - 3h
36. **IMPL-OPTIONS-004** (GUI Architecture) - 4h
37. **IMPL-OPTIONS-005** (Storage Design) - 3h
38. **CONTINGENCY-005** (Budget Overrun) - 2h
39. **TRACEABILITY-FR-TO-CODE** - 3h

**Subtotal SHOULD HAVE**: 12 dokumentów, **35 godzin** (4-5 dni roboczych)

---

### NICE TO HAVE - Przed MVP Release (8 dokumentów, 20h)

**Priorytety LOW** (utworzyć podczas sprintów, iteracyjnie):
- Dodatkowe DoD per-sprint (Sprints 4-6)
- Dodatkowe Expected Outcomes per-sprint
- Dodatkowe Implementation Options (minor decisions)
- Lessons Learned (post-sprint retrospectives)

**Subtotal NICE TO HAVE**: 8 dokumentów, **20 godzin**

---

## Recommendations

### Strategia 1: Waterfall Pre-Implementation (Conservative)
**Podejście**: Utworzyć WSZYSTKIE 18 MUST HAVE docs PRZED Sprint 1.

**Timeline**:
- Week -2 (przed Sprint 1): Utworzyć 9 CRITICAL docs (32h = 4 dni @ 8h/day)
- Week -1: Utworzyć 9 HIGH docs (28h = 3.5 dni)
- Week 0: Review & approval (8h = 1 dzień)
- **Total**: 10-12 dni roboczych

**Pros**:
- ✅ Maximum readiness (zero uncertainty)
- ✅ All contingency plans prepared
- ✅ Clear success criteria

**Cons**:
- ❌ Delay implementation by 2 weeks
- ❌ Risk of over-planning (analysis paralysis)

**Rekomendacja**: ⚠️ **NIE** - zbyt wolno, overkill dla MVP.

---

### Strategia 2: Agile Pre-Implementation (Recommended)
**Podejście**: Iteracyjne tworzenie docs **just-in-time** (1 sprint ahead).

**Timeline**:
- **Week -1 (przed Sprint 1)**: Utworzyć tylko **Sprint 1 critical docs** (8 docs, 24h = 3 dni)
  - DoR-COMP-001-parser, DoR-COMP-002-validator
  - DoD-SPRINT-001
  - ADR-008, ADR-009
  - QA-CHECKLIST-001
  - EXPECTED-OUTCOMES-SPRINT-001
  - CONTINGENCY-001
- **Sprint 1 Week 1**: Utworzyć **Sprint 2 docs** (during Sprint 1 implementation)
  - DoR-COMP-003-graph, DoD-SPRINT-002
  - IMPL-OPTIONS-001, CONTINGENCY-002
- **Sprint 1 Week 2**: Utworzyć **MVP docs**
  - DoD-MVP, EXPECTED-OUTCOMES-MVP, ACCEPTANCE-CRITERIA-MVP
- **Sprint 2-6**: Iteracyjnie dodawać docs as needed

**Pros**:
- ✅ Start implementation faster (only 3-day delay)
- ✅ Learn from Sprint 1 (refine docs based on real experience)
- ✅ Avoid over-planning (docs reflect reality)

**Cons**:
- ❌ Some docs created during sprint (10% dev capacity diverted)
- ❌ Risk of skipping docs (if team busy)

**Rekomendacja**: ✅ **TAK** - optimal balance speed/quality.

---

### Strategia 3: Hybrid (Balanced)
**Podejście**: Utworzyć **minimum critical set** (10 docs) upfront, resztę iteracyjnie.

**Timeline**:
- **Week -1**: Utworzyć **absolute minimum** (10 docs, 32h = 4 dni)
  - DoR-COMP-001-parser, DoR-COMP-002-validator-validator(parsowanie + walidacja)
  - DoD-SPRINT-001, DoD-MVP
  - ADR-008, ADR-009 (error handling + logging - critical dla debugging)
  - QA-CHECKLIST-001
  - EXPECTED-OUTCOMES-SPRINT-001, EXPECTED-OUTCOMES-MVP
  - CONTINGENCY-001 (parser fallback - high risk)
- **Sprint 1+**: Reszta docs as needed (8 docs, 28h spread across sprints)

**Pros**:
- ✅ Reasonable upfront planning (4 days)
- ✅ Critical risks mitigated (Contingency-001)
- ✅ Flexibility dla iteration

**Cons**:
- ❌ Still 1-week delay before implementation

**Rekomendacja**: ✅ **ALTERNATYWA** - jeśli team prefers więcej upfront planning.

---

## Final Recommendation

**Wybór**: **Strategia 2 (Agile Pre-Implementation)**

**Uzasadnienie**:
1. **Speed to MVP**: Start Sprint 1 po tylko 3 dniach (vs 10-12 dni Waterfall)
2. **Validated Learning**: Docs refined based on Sprint 1 experience (nie theoretical)
3. **Risk Mitigation**: Top 3 critical docs covered (DoR-COMP-001-parser, ADR-008/009, CONTINGENCY-001)
4. **Lean Philosophy**: Dokumentacja just-in-time (zgodne z Agile manifesto)

**Action Plan** (Next 3 Days):

### Day 1 (8h) - Critical Foundation
- [x] **ADR-008** (Error Handling Strategy) - 3h
- [x] **ADR-009** (Logging & Observability) - 3h
- [x] **CONTINGENCY-001** (Parser Fallback) - 2h

### Day 2 (8h) - Component Readiness
- [ ] **DoR-COMP-001-parser** (Parser Readiness Checklist) - 2h
- [ ] **DoR-COMP-002-validator** (Validator Readiness Checklist) - 2h
- [ ] **DoD-SPRINT-001** (Sprint 1 Done Criteria) - 3h
- [ ] **QA-CHECKLIST-001** (Pre-Implementation Checklist) - 3h

### Day 3 (8h) - Success Criteria
- [ ] **EXPECTED-OUTCOMES-SPRINT-001** - 2h
- [ ] **DoD-MVP** (MVP Done Criteria) - 4h
- [ ] **EXPECTED-OUTCOMES-MVP** - 2h

**Total**: 3 dni, 8 dokumentów, **24 godziny effort**

**Go/No-Go Decision**: Day 3 EOD
- ✅ If all 8 docs complete → START SPRINT 1 (Day 4)
- ❌ If <6 docs complete → Extend by 1 day

---

## Appendix A: Document Template References

Wszystkie nowe dokumenty powinny użyć istniejących templates:

| Typ Dokumentu | Template | Lokalizacja |
|---------------|----------|-------------|
| ADR | `adr-template-proof-system.md` | `/templates/` |
| Evidence Note | `evidence-note-template.md` | `/templates/` |
| DoR/DoD | Wzór z `DOR-MASTER.md` | `/satellites/approvals/` |
| Contingency Plans | Custom (użyj przykładu CONTINGENCY-001 powyżej) | Nowy folder: `/satellites/contingency/` |
| Expected Outcomes | Custom (użyj przykładu EXPECTED-OUTCOMES-SPRINT-001 powyżej) | Nowy folder: `/satellites/outcomes/` |
| Implementation Options | Custom (użyj przykładu IMPL-OPTIONS-003 powyżej) | Nowy folder: `/satellites/options/` |
| QA Documents | Custom | Nowy folder: `/satellites/qa/` |
| Risk Plans | Custom | Nowy folder: `/satellites/risk/` |
| Traceability Plans | Custom | Nowy folder: `/satellites/traceability/` |

---

## Appendix B: Satellite Folder Structure (Proposed)

```
/docs/satellites/
├── approvals/          # Existing (3 docs)
│   ├── DOR-MASTER.md
│   ├── DOD-MASTER.md
│   └── FUNDING-APPROVAL-001.md
├── decisions/          # Existing (1 doc)
│   └── DECISION-INDEX.md
├── evidence/           # Existing (21 docs)
│   └── E-*.md
├── todos/              # Existing (2 docs)
│   └── TODO-*.md
├── contingency/        # NEW - Contingency Plans
│   ├── CONTINGENCY-001-parser.md
│   ├── CONTINGENCY-002-performance.md
│   ├── CONTINGENCY-003-pyside6.md
│   ├── CONTINGENCY-004-deadline.md
│   └── CONTINGENCY-005-budget.md
├── outcomes/           # NEW - Expected Outcomes
│   ├── EXPECTED-OUTCOMES-SPRINT-001.md
│   ├── EXPECTED-OUTCOMES-SPRINT-002.md
│   ├── EXPECTED-OUTCOMES-MVP.md
│   └── ACCEPTANCE-CRITERIA-MVP.md
├── options/            # NEW - Implementation Options
│   ├── IMPL-OPTIONS-001-parser.md
│   ├── IMPL-OPTIONS-002-validator.md
│   ├── IMPL-OPTIONS-003-graph.md
│   ├── IMPL-OPTIONS-004-gui.md
│   └── IMPL-OPTIONS-005-storage.md
├── qa/                 # NEW - QA Documents
│   ├── QA-CHECKLIST-001-pre-impl.md
│   ├── QA-REVIEW-PLAN-001.md
│   ├── QA-AUTOMATION-001.md
│   └── QA-PERFORMANCE-BASELINE.md
├── readiness/          # NEW - DoR/DoD per-component
│   ├── DoR-COMP-001-parser-parser.md
│   ├── DoR-COMP-002-validator-validator.md
│   ├── DoR-COMP-003-graph-graph.md
│   ├── DoR-COMP-004-gap-engine-gap-engine.md
│   ├── DoR-COMP-005-gui-gui.md
│   ├── DoR-COMP-006-storage-storage.md
│   ├── DoD-SPRINT-001.md
│   ├── DoD-SPRINT-002.md
│   ├── DoD-SPRINT-003.md
│   └── DoD-MVP.md
├── risk/               # NEW - Risk Plans
│   ├── RISK-ASSESSMENT-TECHNICAL.md
│   ├── RISK-ASSESSMENT-SCHEDULE.md
│   └── RISK-MITIGATION-PLAN.md
└── traceability/       # NEW - Traceability Plans
    ├── TRACEABILITY-FR-TO-CODE.md
    └── TRACEABILITY-NFR-TO-TESTS.md
```

**Total New Folders**: 6
**Total New Files**: 38

---

## Appendix C: Effort Breakdown by Role

| Rola | Dokumenty | Effort (h) | % Total |
|------|-----------|------------|---------|
| **Tech Lead** | ADR-008/009/010/011, IMPL-OPTIONS-*, RISK-ASSESSMENT-TECHNICAL | 38h | 33% |
| **Product Owner** | DoD-*, EXPECTED-OUTCOMES-*, ACCEPTANCE-CRITERIA-*, CONTINGENCY-004/005 | 28h | 24% |
| **QA Lead** | QA-*, DoR-*, TRACEABILITY-*, RISK-MITIGATION-PLAN | 35h | 30% |
| **Team (Collective)** | CONTINGENCY-001/002/003, RISK-ASSESSMENT-SCHEDULE | 14h | 12% |
| **TOTAL** | 38 dokumentów | **115h** | 100% |

**Optymalizacja**:
- Jeśli **parallel authoring** (Tech Lead + QA Lead + PO work simultaneously) → 38h total (5 dni @ 8h/day)
- Jeśli **sequential** (1 person) → 115h (14 dni @ 8h/day)

**Rekomendacja**: Parallel authoring (3 osoby, 5 dni).

---

## Appendix D: Quality Gates Summary

**GATE-001: PRE-IMPLEMENTATION** (Status: ❌ NOT MET)
- **Required Docs**: 18 MUST HAVE (CRITICAL + HIGH priority)
- **Current Status**: 0/18 complete (0%)
- **Blocker**: Cannot start Sprint 1 until gate passed
- **Timeline**: 3-5 dni roboczych (Agile approach)

**GATE-002: SPRINT-1-START** (Status: ⏳ PENDING)
- **Required Docs**: DoR-COMP-001-parser, DoR-COMP-002-validator, DoD-SPRINT-001, ADR-008/009
- **Dependencies**: GATE-001 passed
- **Estimated**: Day 4 (after 3-day doc creation)

**GATE-003: MVP-RELEASE** (Status: ⏳ PENDING)
- **Required Docs**: DoD-MVP, ACCEPTANCE-CRITERIA-MVP, all Sprint DoDs
- **Dependencies**: All 6 sprints complete
- **Estimated**: Week 13 (per IMPL-PLAN-001)

---

**END OF GAP ANALYSIS**

**Document Status**: ✅ COMPLETE
**Next Action**: Review & approve → Start 3-day doc creation sprint (Agile approach)
**Owner**: Product Owner + Tech Lead
**Review Date**: 2025-12-27
