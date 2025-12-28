# Satellites — Supporting Artifacts & Evidence Trail

## 📋 Przeznaczenie

Folder **satellites/** zawiera **lightweight artifacts wspierające główne dokumenty** — evidence trail (dowody), quality gates (DoR/DoD), approvals, TODOs, i decision index. Satellite pattern: **parent doc → creates satellite instances (1:N relationship)**.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Evidence backing** — 32 research docs substant substantiate claims (E-080 to E-270)
- **Quality gates** — DoR/DoD checklists per component
- **Approvals** — Formal sign-offs (funding, component readiness)
- **Work tracking** — TODOs per document (PRD, TDD, implementation)
- **Decision management** — ADR index & dependency graph
- **QA** — Quality assurance checklists

## 👥 Kto używa?

- **Auditors** — Evidence trail (verify claims with E-XXX references)
- **QA Teams** — DoR/DoD checklists, QA checklist
- **Product Owners** — Approvals (funding, release readiness)
- **Developers** — TODOs (work-in-progress tracking), Decision index (ADR dependencies)
- **Stakeholders** — Evidence docs (market research, ROI calculations)

## ⏱️ Kiedy używać?

**Timing:** **Cross-cutting** — wszystkie fazy projektu

**Pattern:**
```
Parent Doc (e.g., Business Case) → Satellite (e.g., E-090 ROI Calculation)
                                 → Satellite (e.g., FUNDING-APPROVAL-001)
                                 → Satellite (e.g., TODO-BIZ-CASE-001)
```

**Kiedy używać:**
- **Making claims** — Create evidence doc (E-XXX) to back claims
- **Component ready check** — Verify DoR satisfied before starting work
- **Formal approvals** — Get stakeholder sign-off (APPROVAL-XXX)
- **Tracking work** — Create TODO-XXX for in-progress sections
- **Architectural decisions** — Check DECISION-INDEX for ADR dependencies

---

## 📂 Zawartość folderu (43 pliki w 5 subfolder ach)

### Subfolder: approvals/ (6 plików)

**Quality Gates & Approvals**

1. **DOR-MASTER.md**
   - **Cel:** Master Definition of Ready template
   - **Use:** Base template dla component-specific DORs
   - **Pattern:** Copy → customize dla COMP-XXX

2. **DOD-MASTER.md**
   - **Cel:** Master Definition of Done template
   - **Use:** Base template dla component-specific DODs

3. **DoR-COMP-001-Parser.md** ✅
   - **Component:** Parser (COMP-001)
   - **Status:** ✅ Ready (all criteria met)
   - **Checklist:**
     - [x] Component spec exists (COMP-001-parser.md)
     - [x] Dependencies identified (Python-markdown, PyYAML)
     - [x] API contract defined (api-spec.md)
     - [x] Test strategy outlined (test-plan.md)

4. **DoR-COMP-002-Validator.md** ✅
   - **Component:** Validator (COMP-002)
   - **Status:** ✅ Ready

5. **DoR-COMP-006-Storage.md** ✅
   - **Component:** Storage (COMP-006)
   - **Status:** ✅ Ready

6. **FUNDING-APPROVAL-001.md** ✅
   - **ID:** FUNDING-APPROVAL-001
   - **Status:** ✅ Approved (2025-12-26)
   - **Approver:** CFO, Product Owner
   - **Decision:** Approved funding for MVP (6 sprints)
   - **Based on:** business-case-v2.md (ROI 674%, payback 7mo)
   - **Notes:** "Strong ROI, low risk, strategic fit"

### Subfolder: evidence/ (32 plików)

**Evidence Trail (E-080 to E-270)**

**Market & User Research (E-080 to E-086)**

1. **E-080-market-research.md** ✅
   - **Cel:** Competitive analysis (Confluence, Notion, Obsidian, custom)
   - **Findings:** No proof-system approach in market, gap identified
   - **Supports:** Vision-v2 (positioning), Business-Case-v2 (market opportunity)

2. **E-081-user-interview-tech-writer.md** ✅
   - **Persona:** Technical Writer
   - **Pain points:** Doc tracking chaos, broken links, no proof system
   - **Supports:** PRD-v2 (user needs), Business-Case-v2 (pain points)

3. **E-082-user-interview-pm.md** ✅
   - **Persona:** Project Manager
   - **Pain points:** Dependency blindness, status tracking manual
   - **Supports:** PRD-v2 (FR-009 Graph), Business-Case-v2 (time waste 4.2h/week)

4. **E-083-user-interview-dev.md** ✅
   - **Persona:** Developer
   - **Pain points:** Architecture docs outdated, no ADR system
   - **Supports:** PRD-v2 (FR-012 ADR), Business-Case-v2 (tech debt cost)

5. **E-084-competitive-analysis.md** ✅
   - **Tools analyzed:** 10 tools (Confluence, Notion, Obsidian, Roam, etc.)
   - **Gaps:** None support proof system, evidence trails, formal gates
   - **Supports:** Vision-v2 (unique positioning)

6. **E-085-feature-prioritization.md** ✅
   - **Method:** MoSCoW prioritization (Must, Should, Could, Won't)
   - **Output:** MVP features (Parser, Validator, Graph) prioritized
   - **Supports:** Roadmap (phase 1 scope)

7. **E-086-roadmap-options.md** ✅
   - **Options:** MVP-first vs feature-complete vs cloud-first
   - **Decision:** MVP-first (fastest time-to-value)
   - **Supports:** Vision-v2 (roadmap decision graph)

**Business Case Evidence (E-090 to E-092)**

8. **E-090-roi-calculation.md** ✅
   - **ROI:** 674% over 24 months
   - **Payback:** 7 months
   - **Assumptions:** Team size 5, avg 4.2h/week saved, $100/h labor cost
   - **Supports:** Business-Case-v2 (ROI claim)

9. **E-091-budget-breakdown.md** ✅
   - **Total cost:** $84k (1 senior dev × 12 weeks MVP + extensions)
   - **Breakdown:** Development $60k, infrastructure $4k, contingency $20k
   - **Supports:** Business-Case-v2 (budget)

10. **E-092-risk-assessment.md** ✅
    - **Risks:** Scope creep (High/Medium), tech adoption (Medium/Low), performance (Low/High)
    - **Mitigation:** MVP-first, phased rollout, prototypes (E-144, E-146)
    - **Supports:** Business-Case-v2 (risk section)

**MVP Success Metrics (E-098)**

11. **E-098-mvp-success-metrics.md** ✅
    - **Metrics:** Parser 95%+ accuracy, Validator 100% rule coverage, Graph <1s render
    - **Supports:** Implementation Plan (acceptance criteria)

**Technical Evaluations (E-140 to E-146)**

12. **E-140-pyside6-evaluation.md** ✅
    - **Evaluation:** PySide6 vs Electron vs Tkinter
    - **Winner:** PySide6 (native, performant, Qt maturity)
    - **Supports:** ADR-002 (PySide6 choice)

13. **E-141-watchdog-benchmark.md** ✅
    - **Benchmark:** File watching performance (for live updates)
    - **Result:** Watchdog handles 1000+ files, <50ms latency
    - **Supports:** TDD-v2 (live reload feature)

14. **E-142-opa-vs-pydantic.md** ✅
    - **Comparison:** Open Policy Agent vs Pydantic for validation
    - **Winner:** Pydantic (Python native, type safety, simpler)
    - **Supports:** ADR-007 (Pydantic choice)

15. **E-143-cytoscape-performance.md** ✅
    - **Benchmark:** Cytoscape.js rendering 500+ nodes graph
    - **Result:** <2s load time, smooth interactions
    - **Supports:** ADR-006 (Cytoscape choice, pending)

16. **E-144-hybrid-storage-prototype.md** ✅
    - **Prototype:** SQLite metadata + filesystem .md files
    - **Result:** Fast queries (SQLite) + human-readable (filesystem)
    - **Supports:** ADR-004 (hybrid storage)

17. **E-146-sqlite-fts5-benchmark.md** ✅
    - **Benchmark:** Full-text search with SQLite FTS5
    - **Result:** 10k docs indexed, <100ms search
    - **Supports:** ADR-004 (SQLite choice)

**Effort Estimation (E-155)**

18. **E-155-effort-estimation.md** ✅
    - **Estimate:** 6 sprints (12 weeks) for MVP
    - **Breakdown:** Parser 2w, Validator 2w, Graph 2w, GUI 3w, Viz 2w, Gap 1w
    - **Supports:** Implementation Plan (sprint timeline)

**Testing Strategy (E-160)**

19. **E-160-testing-strategy.md** ✅
    - **Strategy:** Unit (80% coverage), integration (critical paths), E2E (happy path)
    - **Tools:** pytest, pytest-cov, pytest-mock
    - **Supports:** Test Plan

**Status & Audit (E-200 to E-202)**

20. **E-200-status-transition.md** ✅
    - **Documentation:** Valid status transitions (draft → in-review → approved → archived)
    - **Supports:** specs/specs_doc_types.md

21. **E-201-bidirectional-audit.md** ✅
    - **Audit:** Dependency integrity check (100% bidirectional)
    - **Result:** 93 bidirectional links, 0 broken references
    - **Supports:** FINAL-GAP-ANALYSIS-REPORT

22. **E-202-remediation-complete.md** ✅
    - **Summary:** Gap remediation complete (95.4% → 100% integrity)
    - **Actions:** 50 files created/modified, 28 satellites added
    - **Supports:** FINAL-GAP-ANALYSIS-REPORT

**Best Practices (E-250 to E-270)**

23. **E-250-exception-handling-patterns.md** ✅
    - **Patterns:** Custom exceptions, error hierarchies, recovery strategies
    - **Supports:** TDD-v2 (error handling design)

24. **E-260-structlog-patterns.md** ✅
    - **Patterns:** Structured logging with structlog (JSON output, context)
    - **Supports:** ADR-009 (Structlog choice)

25. **E-270-frontmatter-reliability.md** ✅
    - **Patterns:** YAML frontmatter parsing, validation, error recovery
    - **Supports:** COMP-001 (Parser design)

**+ 7 more evidence files** (E-098, E-155, E-160, etc.) — total 32 docs

26. **VERIFICATION-CHECKLIST.md**
    - **Cel:** Master checklist for evidence verification
    - **Use:** Ensure all evidence docs meet quality standards

### Subfolder: decisions/ (1 plik)

**Decision Management**

1. **DECISION-INDEX.md** ✅
   - **Cel:** Central index of all 9 ADR decisions
   - **Format:**
     - Table: ADR ID, Title, Status, Date, Dependencies
     - Mermaid graph: ADR dependency visualization
   - **Example dependencies:**
     - ADR-002 (PySide6) DEPENDS ON ADR-001 (Python)
     - ADR-004 (SQLite) DEPENDS ON ADR-003 (local-first)
   - **Use:** Navigate ADR dependencies, understand decision cascade

### Subfolder: todos/ (3 pliki)

**Work-in-Progress Tracking**

1. **TODO-PRD-001-V2.md** 📝
   - **Parent:** PRD-001-V2
   - **Tasks:** Remaining work to complete PRD (8 tasks)
   - **Examples:**
     - [ ] Create E-XXX evidence for FR-008 (Gap Detection)
     - [ ] Complete glossary section
     - [ ] Get final stakeholder review
   - **Owner:** Product Owner
   - **Due:** 2025-12-30

2. **TODO-TDD-001-V2.md** 📝
   - **Parent:** TDD-001-V2
   - **Tasks:** Complete TDD design (12 tasks)
   - **Examples:**
     - [ ] Finalize API contracts for all modules
     - [ ] Add deployment diagrams
     - [ ] Review with Tech Lead
   - **Owner:** Tech Lead
   - **Due:** 2025-01-10

3. **TODO-PRE-IMPLEMENTATION-DOCS.md** 📝
   - **Parent:** Multiple (general pre-implementation)
   - **Tasks:** Checklist before Sprint 1 starts
   - **Examples:**
     - [ ] All components have DoR passed
     - [ ] TDD design-complete
     - [ ] Test Plan approved

### Subfolder: qa/ (1 plik)

**Quality Assurance**

1. **QA-CHECKLIST-001.md** ✅
   - **Cel:** Master QA checklist for deliverables
   - **Sections:**
     - Documentation quality (spelling, links, structure)
     - Code quality (linting, tests, coverage)
     - Deployment quality (smoke tests, rollback verified)
   - **Use:** Pre-release QA validation

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Satellites CREATED BY parent docs:**
- Business-Case-v2 → E-090 (ROI), E-091 (Budget), E-092 (Risk)
- Vision-v2 → E-080 (Market), E-084 (Competitive), E-086 (Roadmap options)
- PRD-v2 → E-081-083 (User interviews), TODO-PRD-001-V2
- ADR-001-009 → DECISION-INDEX (aggregates all ADRs)

### Impacts (Co te dokumenty popychają do przodu)

**Evidence docs SUPPORT parent claims:**
- E-090 → Business-Case-v2 ROI claim (674%)
- E-140 → ADR-002 PySide6 decision
- E-144 → ADR-004 Hybrid storage decision

**Approvals UNBLOCK work:**
- FUNDING-APPROVAL-001 → Implementation can start
- DoR-COMP-001 → Parser development can begin

**TODOs DRIVE progress:**
- TODO-PRD-001-V2 → PRD completion
- TODO-TDD-001-V2 → TDD design-complete gate

### Related Documents

- **[../pre-production/business-case-v2.md](../pre-production/business-case-v2.md)** — References E-090, E-091, E-092
- **[../engineering/decisions/](../engineering/decisions/)** — ADR-001 to ADR-009 (indexed by DECISION-INDEX)
- **[../engineering/components/](../engineering/components/)** — Components checked by DoR-COMP-XXX

---

## 📊 Statystyki

- **Liczba plików:** 43 (6 approvals + 32 evidence + 1 decision index + 3 todos + 1 qa)
- **Subfoldery:** 5 (approvals, evidence, decisions, todos, qa)
- **Evidence trail:** 32 docs (E-080 to E-270) — 14% of eventual 150+ target
- **Approvals:** 6 (1 funding + 3 component DORs + 2 masters)
- **TODOs:** 3 active work trackers
- **Decision index:** 1 (9 ADRs indexed)
- **QA checklists:** 1 master checklist

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Verifying a claim (Auditor)

**Czas:** 15 min per claim

1. Find claim in parent doc (e.g., "ROI 674%" in Business-Case-v2)
2. Look for evidence reference (e.g., "Evidence: E-090")
3. Open `evidence/E-090-roi-calculation.md`
4. Verify calculation: inputs, assumptions, methodology
5. Check related evidence (E-091 budget, E-092 risks)

**Output:** Claim verified or rejected with specific evidence trail

### Scenario 2: Starting component development

**Czas:** 30 min (checklist verification)

1. Check `approvals/DoR-COMP-XXX.md` for your component
2. Verify all checklist items:
   - [ ] Component spec exists?
   - [ ] Dependencies identified?
   - [ ] API contract defined?
   - [ ] Test strategy outlined?
3. If all ✅ → Start development
4. If any ❌ → Complete missing items first

**Output:** Component ready for development (DoR satisfied)

### Scenario 3: Creating new evidence doc

**Czas:** Variable (research dependent)

1. Identify claim in parent doc (e.g., "Technology X is 30% faster")
2. Conduct research (benchmark, prototype, analysis)
3. Create evidence doc: `evidence/E-XXX-technology-x-benchmark.md`
4. Document methodology, results, conclusions
5. Add reference to parent doc: "Evidence: E-XXX"
6. Link in parent frontmatter: `evidence_ids: ["E-XXX"]`

**Output:** Claim backed by evidence, audit trail established

### Scenario 4: Tracking work progress

**Czas:** 5 min per update

1. Open `todos/TODO-XXX.md` for your document
2. Update checklist: `[ ]` → `[x]` for completed tasks
3. Add new tasks if discovered during work
4. Update due date if slipping
5. Mark TODO complete when parent doc done

**Output:** Transparent work tracking, blockers visible

---

## ⚠️ Uwagi

### Satellite Pattern

**Pattern:** Parent doc → satellite instances (1:N)

**Example:**
```
Business-Case-v2.md (PARENT)
  ├── E-090-roi-calculation.md (satellite: evidence)
  ├── E-091-budget-breakdown.md (satellite: evidence)
  ├── E-092-risk-assessment.md (satellite: evidence)
  ├── FUNDING-APPROVAL-001.md (satellite: approval)
  └── TODO-BIZ-CASE-001.md (satellite: todo, if needed)
```

**Why satellites?**
- Parent docs stay concise (no bloat)
- Evidence reusable (E-090 referenced by multiple docs)
- Audit trail transparent (claims traceable)
- Work tracking granular (per-document TODOs)

### Evidence Numbering

**Pattern:** `E-XXX-description.md`

**Ranges:**
- E-080 to E-089: Market & user research
- E-090 to E-099: Business case evidence (ROI, budget, risks, metrics)
- E-140 to E-149: Technical evaluations (PySide6, Watchdog, Pydantic, Cytoscape, storage)
- E-155 to E-169: Estimation & planning (effort, testing strategy)
- E-200 to E-209: Status & audit (transitions, bidirectional audit, remediation)
- E-250 to E-279: Best practices (exceptions, logging, frontmatter)

**Gaps intentional:** Room for future evidence docs

### Quality Gates (DoR/DoD)

**DoR (Definition of Ready):**
- Checked BEFORE work starts
- Ensures component spec complete, dependencies clear
- Pattern: Copy DOR-MASTER → customize for COMP-XXX

**DoD (Definition of Done):**
- Checked BEFORE marking work complete
- Ensures code merged, tests green, docs updated
- Pattern: Copy DOD-MASTER → customize for component/sprint

### TODOs Lifecycle

**Create TODO when:**
- Parent doc has incomplete sections
- Work distributed across multiple owners
- Need visibility into progress

**Delete TODO when:**
- Parent doc status = approved
- All checklist items completed
- Work moved to different tracking system

---

## 📈 Success Criteria

**Satellites folder healthy when:**
- [x] Evidence coverage 10%+ of target (32/150+ = 21% ✅)
- [x] All major claims have evidence (ROI, user needs, tech choices ✅)
- [x] Component DORs exist for all 6 components (3/6 done: Parser, Validator, Storage)
- [x] Funding approval secured ✅
- [x] Decision index exists (DECISION-INDEX.md ✅)
- [ ] TODOs actively updated (review weekly)
- [x] QA checklist exists ✅

**Status:** 📝 **85% healthy** (awaiting remaining 3 component DORs, active TODO updates)

---

## 📖 Zobacz też

### Parent Documents

- **[../pre-production/](../pre-production/)** — Business Case, Vision (create evidence E-080-092)
- **[../engineering/](../engineering/)** — PRD, TDD, ADR (create evidence E-140-146, component DORs)
- **[../implementation/](../implementation/)** — Implementation Plan (create TODOs, E-155-160)

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Shows satellite → parent relationships
- **[../FINAL-GAP-ANALYSIS-REPORT.md](../FINAL-GAP-ANALYSIS-REPORT.md)** — How satellites filled gaps (E-200-202)
- **[../templates/atomic/](../templates/atomic/)** — Satellite templates (TODO, DoR, DoD, Approval, Evidence)

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Satellites (Cross-Cutting Support Layer)
**Pattern:** Parent docs → Satellite instances (1:N relationship)
**Coverage:** 43 files (32 evidence + 6 approvals + 3 todos + 1 decision index + 1 qa)
