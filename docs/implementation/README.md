# Implementation — Sprint Execution Planning

## 📋 Przeznaczenie

Folder **implementation/** zawiera **plany wykonawcze fazy implementation** — 6-sprint MVP breakdown, test plan, i task-level execution details. To warstwa "JAK wykonujemy" (sprint po sprincie).

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Sprint planning** — 6-sprint MVP breakdown (Parser → Validator → Graph → GUI → Viz → Gap Engine)
- **Task breakdown** — User stories → tasks → effort estimates
- **Testing strategy** — Unit, integration, E2E test planning
- **Resource allocation** — Team capacity, sprint velocity
- **Timeline tracking** — Sprint start/end dates, milestones

## 👥 Kto używa?

- **Scrum Master** — Sprint planning, velocity tracking
- **Developers** — Sprint backlog, task assignment
- **QA Engineers** — Test plan, acceptance criteria
- **Tech Lead** — Sprint goals, technical guidance
- **Product Owner** — Sprint priorities, acceptance

## ⏱️ Kiedy używać?

**Timing:** Faza **execution** (post-design, pre-production)

**Lifecycle Position:**
```
Pre-Production → Engineering → Implementation (YOU ARE HERE) → Operations
                               ↓
                       Sprint 1-6 Execution → Deployment
```

**Kiedy czytać:**
- **Sprint planning** — Before each sprint starts (review sprint N plan)
- **Daily standup** — Check task progress, blockers
- **Sprint review** — Verify completed vs planned
- **Pre-QA** — Reference test plan for acceptance criteria

---

## 📂 Zawartość folderu (2 pliki)

### 1. implementation-plan.md 📝

**ID:** IMPL-PLAN-001
**Status:** 📝 Draft (planning in progress)
**Rozmiar:** ~600 lines

**Cel:** 6-sprint MVP breakdown z task-level details

**Struktura:**

**Sprint 1: Parser + Models (Week 1-2)**
- Goals:
  - Markdown parsing (Python-markdown)
  - Frontmatter extraction (PyYAML)
  - Document model (Pydantic schema)
- Tasks:
  - TASK-001: Parser module skeleton
  - TASK-002: Frontmatter parser
  - TASK-003: Document Pydantic model
  - TASK-004: Unit tests (95%+ coverage)
- Deliverables: Parser module, 95% test coverage
- Evidence: E-270 (frontmatter reliability patterns)

**Sprint 2: Validator (Week 3-4)**
- Goals:
  - Rule engine (Pydantic validation)
  - Required sections checker
  - Dependency verifier
- Tasks:
  - TASK-011: Validator module skeleton
  - TASK-012: Pydantic validation schemas
  - TASK-013: Section checker
  - TASK-014: Dependency verifier
  - TASK-015: Unit + integration tests
- Deliverables: Validator module, 100% rule coverage
- Evidence: E-142 (Pydantic patterns)

**Sprint 3: Graph Builder (Week 5-6)**
- Goals:
  - NetworkX graph construction
  - Cycle detection
  - Topological sort
- Tasks:
  - TASK-021: Graph builder module
  - TASK-022: Dependency graph construction
  - TASK-023: Cycle detection algorithm
  - TASK-024: Tests (graph operations)
- Deliverables: Graph module, cycle detection working
- ADR: ADR-005 (NetworkX choice)

**Sprint 4: GUI Application (Week 7-9)**
- Goals:
  - PySide6 app skeleton
  - Document browser
  - Settings panel
- Tasks:
  - TASK-031: PySide6 project setup
  - TASK-032: Main window + menu
  - TASK-033: Document list view
  - TASK-034: Document detail view
  - TASK-035: Settings dialog
- Deliverables: Functional GUI (browse docs)
- ADR: ADR-002 (PySide6 choice)
- Evidence: E-140 (PySide6 evaluation)

**Sprint 5: Graph Visualization (Week 10-11)**
- Goals:
  - Graph rendering (Cytoscape.js or Qt native)
  - Interactive exploration (zoom, pan, click)
  - Layout algorithms (hierarchical, force-directed)
- Tasks:
  - TASK-041: Cytoscape.js integration
  - TASK-042: Graph rendering
  - TASK-043: Interaction handlers
  - TASK-044: Layout configuration
- Deliverables: Interactive graph viz (<2s load for 500 nodes)
- ADR: ADR-006 (Cytoscape choice, pending)
- Evidence: E-143 (Cytoscape performance)

**Sprint 6: Gap Detection Engine (Week 12)**
- Goals:
  - Gap detection (missing docs, broken refs, status conflicts)
  - Report generation (markdown output)
  - CLI interface (`ishkarim validate`, `ishkarim gaps`)
- Tasks:
  - TASK-051: Gap detection algorithms
  - TASK-052: Report generator
  - TASK-053: CLI interface
  - TASK-054: Integration tests (end-to-end)
- Deliverables: Gap engine, CLI commands

**Timeline:**
- Total: 12 weeks (6 sprints × 2 weeks)
- Start: TBD (awaiting TDD design-complete gate)
- MVP delivery: Week 12

**Dependencies:**
- BLOCKED BY: TDD-001-V2 design-complete gate
- REQUIRES: All component DORs passed (3/6 done)
- INFORMS: Operations/deployment-guide.md (when MVP ready)

**Evidence:**
- E-155 (effort estimation - how we got 6 sprints)
- E-160 (testing strategy - coverage targets)
- E-098 (MVP success metrics - acceptance criteria)

### 2. test-plan.md 📝

**ID:** TEST-PLAN-001
**Status:** 📝 Draft
**Rozmiar:** ~400 lines

**Cel:** Comprehensive testing strategy (unit, integration, E2E)

**Struktura:**

**Testing Pyramid:**
- **Unit Tests (80% coverage target)**
  - Tools: pytest, pytest-cov
  - Scope: All modules (Parser, Validator, Graph, GUI components)
  - Pattern: Arrange-Act-Assert (AAA)

- **Integration Tests (Critical paths)**
  - Scope: Module interactions (Parser → Validator → Graph)
  - Pattern: Real data fixtures, no mocks

- **E2E Tests (Happy path)**
  - Scope: Full workflow (load workspace → validate → visualize)
  - Tools: pytest + PySide6 test harness

**Test Strategy per Component:**

1. **Parser Tests**
   - Frontmatter parsing (valid YAML, invalid YAML, edge cases)
   - Section extraction (H1/H2 headers, nested lists)
   - Edge cases: Empty files, malformed markdown, UTF-8

2. **Validator Tests**
   - Rule execution (required sections, dependencies, status constraints)
   - Error reporting (E-110 missing section, E-140 broken dependency)
   - Gate checking (req-freeze, design-complete)

3. **Graph Tests**
   - Cycle detection (circular dependencies)
   - Topological sort (valid ordering)
   - Bidirectional link integrity

4. **GUI Tests**
   - Widget creation (main window, dialogs)
   - User interactions (click, scroll, select)
   - Layout rendering

**Acceptance Criteria (per E-098):**
- Parser: 95%+ accuracy on real docs
- Validator: 100% rule coverage (all error codes testable)
- Graph: <1s render for 500 nodes

**Tools:**
- pytest (test runner)
- pytest-cov (coverage reporting)
- pytest-mock (mocking framework)
- hypothesis (property-based testing)

**CI/CD Integration (future):**
- GitHub Actions workflow (run tests on PR)
- Coverage gates (fail if <80% unit coverage)
- Automated E2E smoke tests

**Evidence:**
- E-160 (testing strategy rationale)
- E-098 (MVP success metrics)

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Implementation Plan BLOCKED BY:**
- `engineering/tdd-v2.md` (status != design-complete) — Awaiting TDD completion
- `engineering/prd-v2.md` (status = req-freeze) ✅ — Requirements stable

**Test Plan REQUIRES:**
- `engineering/prd-v2.md` — Acceptance criteria from PRD
- `engineering/components/COMP-*` — Component specs define test scope

### Impacts (Co te dokumenty popychają do przodu)

**Implementation Plan INFORMS:**
- `operations/deployment-guide.md` — Deployment ready when MVP complete
- `satellites/todos/TODO-PRD-001-V2.md` — Sprint execution updates TODOs

**Test Plan INFORMS:**
- QA testing (when sprints execute)
- CI/CD pipeline setup (future)

### Related Documents

- **[../engineering/tdd-v2.md](../engineering/tdd-v2.md)** — Architecture driving sprint tasks
- **[../engineering/components/](../engineering/components/)** — Component specs → sprint deliverables
- **[../satellites/evidence/E-155-effort-estimation.md](../satellites/evidence/E-155-effort-estimation.md)** — Sprint estimates
- **[../satellites/evidence/E-160-testing-strategy.md](../satellites/evidence/E-160-testing-strategy.md)** — Test plan evidence
- **[../satellites/evidence/E-098-mvp-success-metrics.md](../satellites/evidence/E-098-mvp-success-metrics.md)** — Acceptance criteria

---

## 📊 Statystyki

- **Liczba plików:** 2 (implementation plan + test plan)
- **Status:** 📝 Draft (both files)
- **Timeline:** 12 weeks (6 sprints × 2 weeks)
- **Sprints:** 6 (Parser, Validator, Graph, GUI, Viz, Gap Engine)
- **Test coverage target:** 80% unit, 100% critical paths, E2E happy path
- **Blockers:** TDD design-complete gate (in progress)

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Sprint planning (pre-sprint N)

**Czas:** 2h (planning meeting)

1. Read `implementation-plan.md` Sprint N section
2. Review deliverables & goals
3. Break down tasks → user stories → story points
4. Assign tasks to developers
5. Update sprint backlog (Jira, GitHub Projects, etc.)

**Output:** Sprint backlog ready, team aligned on goals

### Scenario 2: Daily standup reference

**Czas:** 5 min (daily)

1. Check sprint N task list (TASK-0XX)
2. Update task status (in-progress, blocked, done)
3. Identify blockers (reference dependencies)
4. Update test-plan.md if test strategy changes

**Output:** Transparent progress, blockers surfaced

### Scenario 3: Pre-QA review

**Czas:** 1h (before QA handoff)

1. Read `test-plan.md` for sprint N component
2. Verify unit tests written (95%+ coverage per E-098)
3. Run integration tests (critical paths)
4. Check acceptance criteria (from PRD FR-XXX)

**Output:** Component ready for QA, tests green

---

## ⚠️ Uwagi

### Dependency on TDD design-complete

**CRITICAL:** Implementation Plan is **BLOCKED** until:
- [x] TDD-V2 status = design-complete
- [ ] All 6 components have DoR passed (currently 3/6)

**Why?** Can't start Sprint 1 without finalized architecture & component specs.

**Current status:** Awaiting TDD completion (expected: early January 2026)

### Sprint estimates

**6 sprints (12 weeks)** based on:
- E-155 (effort estimation): 1 senior dev full-time
- Assumptions: No major blockers, team velocity 20 story points/sprint
- Contingency: +20% buffer (not in 12 weeks, but available)

**If estimates slip:** Re-evaluate after Sprint 2 (Parser + Validator complete), adjust remaining sprints.

### Test-first development

**Test Plan exists BEFORE implementation** for:
- **Clarity:** Developers know acceptance criteria up-front
- **Coverage:** 80% unit coverage enforced from day 1
- **Quality:** Tests written alongside code (not after)

**Pattern:** Read test-plan.md → write tests → implement → verify green

---

## 📈 Success Criteria

**Implementation phase complete when:**
- [ ] All 6 sprints executed (12 weeks)
- [ ] MVP deliverables complete (Parser, Validator, Graph, GUI, Viz, Gap Engine)
- [ ] Test coverage 80%+ (unit), 100% critical paths
- [ ] E-098 success metrics met (Parser 95%+ accuracy, Validator 100% rules, Graph <1s)
- [ ] Deployment guide updated (operations/deployment-guide.md)
- [ ] Ready for production handover

**Status:** ⏳ **Awaiting start** (TDD design-complete pending)

---

## 📖 Zobacz też

### Upstream (Dependencies)

- **[../engineering/tdd-v2.md](../engineering/tdd-v2.md)** — Architecture driving implementation
- **[../engineering/components/](../engineering/components/)** — Component specs
- **[../engineering/prd-v2.md](../engineering/prd-v2.md)** — Requirements & acceptance criteria

### Downstream (Impacts)

- **[../operations/](../operations/)** — Deployment guide (when MVP ready)
- **[../satellites/todos/](../satellites/todos/)** — TODOs updated during sprints

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Graf C: Implementation Dependencies
- **[../satellites/evidence/E-155-effort-estimation.md](../satellites/evidence/E-155-effort-estimation.md)** — Sprint timeline
- **[../templates/sprints/](../templates/sprints/)** — Sprint template patterns

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Implementation (Execution Phase)
**Status:** ⏳ Awaiting start (blocked by TDD design-complete)
**Timeline:** 12 weeks (6 sprints), MVP delivery Week 12
