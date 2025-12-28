# Engineering — Technical Design & Architecture

## 📋 Przeznaczenie

Folder **engineering/** zawiera **dokumenty techniczne fazy design** — wymagania produktu (PRD), architekturę techniczną (TDD), decyzje architektoniczne (ADR), komponenty systemu, i koncepcje. To warstwa "CO budujemy i JAK".

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Requirements definition** — Functional & non-functional requirements (PRD)
- **Technical architecture** — System design, technology stack (TDD)
- **Architectural decisions** — ADR pattern (9 kluczowych decyzji)
- **Component specification** — 6 głównych komponentów (Parser, Validator, Graph, GUI, Viz, Storage)
- **Concept modeling** — 18 koncepcji systemu (modular Concepts-v2)
- **Traceability** — Requirements Traceability Matrix (RTM)

## 👥 Kto używa?

- **Tech Leads** — PRD, TDD, ADR (technical direction)
- **Software Architects** — Architecture docs, component specs
- **Developers** — Component specs, Concepts, RTM (implementation guide)
- **QA Engineers** — PRD (acceptance criteria), Test Plan inputs
- **Product Owners** — PRD review, NFR validation

## ⏱️ Kiedy używać?

**Timing:** Faza **design** (post-business case, pre-implementation)

**Lifecycle Position:**
```
Pre-Production → Engineering (YOU ARE HERE) → Implementation → Operations
                      ↓
               PRD, TDD, ADR → Sprint Execution → Deployment
```

**Kiedy czytać:**
- **Before implementation** — Developers must read PRD, Components, ADR przed kodowaniem
- **Architecture review** — Quarterly ADR review for tech debt
- **Requirement changes** — Check RTM impact before modifying PRD
- **Technical decisions** — Reference ADR-001 to ADR-009 for precedents

---

## 📂 Zawartość folderu (34 pliki)

### Root Level (14 plików)

**Product Requirements Document (PRD)**

1. **prd-v2.md** ✅
   - **ID:** PRD-001-V2
   - **Status:** ✅ Req-freeze (achieved 2025-12-26)
   - **Rozmiar:** ~800 lines
   - **Cel:** Complete product requirements (functional + non-functional)
   - **Kluczowe sekcje:**
     - FR-001 to FR-015 (functional requirements)
     - NFR-001 to NFR-010 (non-functional requirements)
     - User stories (3 personas: Technical Writer, Project Manager, Developer)
     - Acceptance criteria (GIVEN/WHEN/THEN)
     - Technology stack (Python 3.11+, PySide6, NetworkX, SQLite)
   - **Gates:** REQ-FREEZE passed → TDD-001-V2 unblocked
   - **Dependencies:** REQUIRES Business-Case-V2, Vision-V2, Concepts-V2
   - **Impacts:** BLOCKS TDD-001-V2 until req-freeze

2. **prd-v1-deprecated.md** 🗂️
   - **Status:** Deprecated (superseded by PRD-001-V2)
   - **Kept for:** Audit trail, migration context

**Technical Design Document (TDD)**

3. **tdd-v2.md** 📝
   - **ID:** TDD-001-V2
   - **Status:** 📝 Draft (awaiting design-complete gate)
   - **Rozmiar:** ~700 lines
   - **Cel:** System architecture, component design
   - **Kluczowe sekcje:**
     - System architecture (hexagonal architecture, SOLID principles)
     - Component breakdown (6 main components)
     - Data models (Pydantic schemas)
     - API design (internal module APIs)
     - Deployment architecture (local app, future cloud)
   - **Dependencies:** BLOCKED BY PRD-001-V2 req-freeze (now unblocked ✅)
   - **Impacts:** INFORMS Implementation Plan (when design-complete)

**Concepts System**

4. **koncepcje-v2-modular-index.md** ✅
   - **ID:** CONCEPTS-001-V2
   - **Status:** ✅ Completed (modular structure)
   - **Cel:** Index of 18 core concepts (modularized)
   - **Pattern:** Concepts-v2 split into 5 files for scalability

5. **koncepcje-v2-core.md** (Concepts 1-6: Core System)
6. **koncepcje-v2-validation.md** (Concepts 7-10: Validation Engine)
7. **koncepcje-v2-graph.md** (Concepts 11-14: Graph & Dependencies)
8. **koncepcje-v2-quality.md** (Concepts 15-16: Quality Gates)
9. **koncepcje-v2-evidence.md** (Concepts 17-18: Evidence & Living Docs)

**Migration & Analysis**

10. **CONCEPTS-001-DIFF-REPORT.md**
    - **Cel:** What changed v1→v2
    - **Summary:** +6 concepts, +35 functions, modularized from 1 file → 6 files

11. **CONCEPTS-001-MIGRATION-GUIDE.md**
    - **Cel:** How to migrate from v1 to v2
    - **Audience:** Developers using old concept structure

**Requirements Traceability Matrix**

12. **rtm.md** ✅
    - **ID:** RTM-001
    - **Status:** ✅ Active (living document)
    - **Cel:** Trace requirements → design → implementation → tests
    - **Format:** Table mapping FR/NFR → Components → Test Cases

**Deprecated**

13. **prd.md**, **koncepcje.md** 🗂️
    - **Status:** Deprecated or symlinks to v2 versions

### Subfolder: apis/ (1 plik)

**API Specifications**

1. **api-spec.md**
   - **Cel:** Internal module API contracts
   - **Zawiera:** Parser API, Validator API, Graph API, Storage API
   - **Use:** Developer reference for module interfaces

### Subfolder: architecture/ (2 pliki)

**System Architecture**

1. **architecture-overview.md**
   - **Cel:** High-level system design
   - **Pattern:** Hexagonal architecture (ports & adapters)
   - **Diagrams:** Component diagram, deployment diagram

2. **technology-stack.md**
   - **Cel:** Technology choices & rationale
   - **Stack:**
     - **Language:** Python 3.11+
     - **GUI:** PySide6 (Qt for Python)
     - **Graph:** NetworkX
     - **Storage:** SQLite (hybrid with filesystem)
     - **Validation:** Pydantic
     - **Logging:** Structlog

### Subfolder: components/ (6 plików)

**Component Specifications** (COMP-001 to COMP-006)

1. **COMP-001-parser.md** ✅
   - **Component:** Parser (Markdown + frontmatter)
   - **Responsibility:** Read .md files, extract metadata, parse structure
   - **Tech:** Python-markdown, PyYAML
   - **DoR:** `satellites/approvals/DoR-COMP-001-Parser.md`

2. **COMP-002-validator.md** ✅
   - **Component:** Validator (rules engine)
   - **Responsibility:** Check required sections, enforce gates, verify dependencies
   - **Tech:** Pydantic for schema validation
   - **DoR:** `satellites/approvals/DoR-COMP-002-Validator.md`

3. **COMP-003-graph-builder.md** 📝
   - **Component:** Graph Builder
   - **Responsibility:** Build dependency graph from parsed docs
   - **Tech:** NetworkX (directed graph)

4. **COMP-004-gui.md** 📝
   - **Component:** GUI Application
   - **Responsibility:** PySide6 app (document browser, graph viewer)
   - **ADR:** ADR-002 (PySide6 choice)

5. **COMP-005-visualization.md** 📝
   - **Component:** Graph Visualization
   - **Responsibility:** Render dependency graphs (Cytoscape.js or native)
   - **ADR:** ADR-006 (Cytoscape performance)

6. **COMP-006-storage.md** ✅
   - **Component:** Hybrid Storage
   - **Responsibility:** SQLite metadata + filesystem .md files
   - **Evidence:** E-144 (hybrid storage prototype)
   - **DoR:** `satellites/approvals/DoR-COMP-006-Storage.md`

### Subfolder: decisions/ (9 plików)

**Architecture Decision Records (ADR-001 to ADR-009)**

1. **ADR-001-python-over-typescript.md** ✅
   - **Decision:** Use Python (not TypeScript) for MVP
   - **Rationale:** Team expertise, ecosystem (NetworkX, Pydantic), fast prototyping
   - **Status:** Accepted (2025-12-18)
   - **Evidence:** E-140 (tech evaluation)

2. **ADR-002-pyside6-gui-framework.md** ✅
   - **Decision:** PySide6 for GUI (not Electron, not web)
   - **Rationale:** Native performance, no web overhead, Qt maturity
   - **Alternatives:** Electron (rejected: memory bloat), Tkinter (rejected: limited)
   - **Evidence:** E-140 (PySide6 evaluation)

3. **ADR-003-local-first-no-cloud.md** ✅
   - **Decision:** Local-first architecture (no cloud dependency MVP)
   - **Rationale:** Data privacy, auditability, offline work, no vendor lock-in
   - **Future:** Cloud sync optional (Phase 4)

4. **ADR-004-sqlite-hybrid-storage.md** ✅
   - **Decision:** Hybrid storage (SQLite metadata + filesystem .md)
   - **Rationale:** Fast queries (SQLite) + human-readable files (.md)
   - **Evidence:** E-144 (hybrid storage prototype), E-146 (SQLite FTS5 benchmark)

5. **ADR-005-networkx-graph-library.md** ✅
   - **Decision:** NetworkX for dependency graph
   - **Rationale:** Python native, mature, algorithms (cycle detection, topological sort)

6. **ADR-006-cytoscape-visualization.md** 📝
   - **Decision:** Cytoscape.js for graph rendering (or native Qt)
   - **Evidence:** E-143 (Cytoscape performance benchmark)
   - **Status:** Draft (awaiting final decision)

7. **ADR-007-pydantic-validation.md** ✅
   - **Decision:** Pydantic for schema validation (over OPA)
   - **Rationale:** Python native, type safety, JSON Schema compatibility
   - **Evidence:** E-142 (OPA vs Pydantic comparison)

8. **ADR-008-markdown-not-custom-format.md** ✅
   - **Decision:** Use Markdown + YAML frontmatter (not custom DSL)
   - **Rationale:** Human-readable, Obsidian compatible, ecosystem support

9. **ADR-009-structlog-logging.md** ✅
   - **Decision:** Structlog for structured logging
   - **Rationale:** Queryable logs, production debugging, JSON output
   - **Evidence:** E-260 (structlog best practices)

**ADR Dependency Graph:** See `satellites/decisions/DECISION-INDEX.md`

### Subfolder: data-models/ (2 pliki)

**Data Models & Schemas**

1. **document-schema.md**
   - **Cel:** Pydantic schema for document metadata
   - **Fields:** id, title, type, status, dependencies, impacts, evidence_ids

2. **graph-schema.md**
   - **Cel:** NetworkX graph structure
   - **Nodes:** Documents (id, metadata)
   - **Edges:** Dependencies (type: requires/blocks/informs)

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**PRD-V2 REQUIRES:**
- `pre-production/business-case-v2.md` — Requirements justified by ROI
- `pre-production/vision-v2.md` — Requirements align with vision
- `engineering/koncepcje-v2-*.md` — All FR map to 18 concepts

**TDD-V2 BLOCKED BY:**
- `PRD-001-V2.status == req-freeze` ✅ (now unblocked)

### Impacts (Co te dokumenty popychają do przodu)

**PRD-V2 BLOCKS:**
- `TDD-001-V2` — Can't design architecture without stable requirements
- `implementation/test-plan.md` — Test plan needs stable AC

**TDD-V2 INFORMS (when design-complete):**
- `implementation/implementation-plan.md` — Sprint tasks based on components
- `components/COMP-001 to COMP-006` — Component specs derive from TDD

**ADR-001 to ADR-009 INFORM:**
- All technical decisions in TDD, Components

### Related Documents

- `satellites/evidence/E-140-pyside6-evaluation.md` — Supports ADR-002
- `satellites/evidence/E-142-opa-vs-pydantic.md` — Supports ADR-007
- `satellites/evidence/E-143-cytoscape-performance.md` — Supports ADR-006
- `satellites/evidence/E-144-hybrid-storage-prototype.md` — Supports ADR-004
- `satellites/approvals/DoR-COMP-001-Parser.md` — Component readiness
- `satellites/decisions/DECISION-INDEX.md` — ADR dependency graph

---

## 📊 Statystyki

- **Liczba plików:** 34 (14 root + 20 subfolders)
- **Subfoldery:** 4 (apis, architecture, components, decisions)
- **Status:**
  - ✅ Req-freeze: PRD-V2 (2025-12-26)
  - ✅ Completed: Concepts-V2, RTM, ADR-001,002,003,004,005,007,008,009 (8/9)
  - 📝 Draft: TDD-V2 (awaiting design-complete), ADR-006
  - 🗂️ Deprecated: PRD-V1, Concepts-V1
- **Components:** 6 (Parser, Validator, Graph, GUI, Viz, Storage)
- **ADRs:** 9 architectural decisions documented
- **Concepts:** 18 core concepts (modular structure)
- **Gates passed:** REQ-FREEZE ✅

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Developer starting implementation

**Czas:** 2-3h (deep reading)

1. **PRD-V2** (1h) — Read all FR-001 to FR-015, NFR-001 to NFR-010
   - Note: Which FRs map to your sprint (e.g., FR-001 Parser → Sprint 1)
2. **Concepts-V2** (30m) — Understand 18 core concepts (read modular index first)
3. **Component spec** (30m) — Read COMP-001 to COMP-006 for your component
4. **ADRs** (30m) — Read relevant ADR (e.g., ADR-001 Python, ADR-004 Storage)
5. **TDD-V2** (30m) — Understand system architecture (hexagonal, module APIs)

**Output:** Ready to code with full context (requirements, architecture, decisions)

### Scenario 2: Architecture review (quarterly)

**Czas:** 2h (meeting)

1. Review **ADR-001 to ADR-009** — Still valid? Any tech debt from decisions?
2. Check **TDD-V2** — Architecture evolved? Need ADR-010 for new decisions?
3. Review **Components** — Any new components needed? COMP-007+?
4. Update **RTM** — Requirements → design → implementation still traced?

**Output:** Updated ADRs, new components identified, RTM validated

### Scenario 3: Requirement change request

**Czas:** 1h (impact analysis)

1. **RTM** — Check FR/NFR impact (which components affected?)
2. **Dependency graph** — Check PRD-V2 impacts (TDD, Test Plan, Implementation)
3. **Status check** — Is PRD still req-freeze? If yes, need CR (change request)
4. **ADR review** — Does change violate existing ADR? Need new ADR?

**Output:** Impact assessment, CR created (if req-freeze), stakeholder approval needed

---

## ⚠️ Uwagi

### Wersjowanie

**Pattern:**
- V2 = **CURRENT** (req-freeze 2025-12-26)
- V1 = **DEPRECATED** (kept for migration)
- DIFF reports: CONCEPTS-001-DIFF-REPORT (v1→v2 changes)

**Dlaczego V2?**
- PRD-V1: lacked NFR detail, no RTM integration
- Concepts-V1: monolithic (1 file, 600 lines) → V2 modular (6 files)

### Req-Freeze Discipline

**PRD-V2 status = req-freeze** means:
- ❌ NO edits without formal Change Request (CR)
- ❌ NO new FR/NFR without stakeholder approval
- ✅ Clarifications OK (comments, examples)
- ✅ Bug fixes OK (AC typos, broken links)

**Dlaczego?** TDD-V2 zależy od stabilnych requirements. Zmiany PRD = cascade do TDD, Test Plan, Implementation.

### ADR Pattern

**Every architectural decision MUST have ADR:**
- Title: Decision made
- Context: Problem being solved
- Decision: What we chose
- Rationale: Why (with evidence E-XXX)
- Alternatives: What we rejected & why
- Consequences: Trade-offs accepted

**Example:** ADR-004 (SQLite hybrid storage)
- Decision: SQLite + filesystem
- Rationale: Fast queries + human-readable
- Evidence: E-144 (prototype), E-146 (benchmark)
- Alternatives: Pure filesystem (rejected: slow queries), Pure DB (rejected: not human-readable)

### Modular Concepts

**Concepts-V2 modularized** for scalability:
- koncepcje-v2-modular-index.md (index)
- koncepcje-v2-core.md (Concepts 1-6)
- koncepcje-v2-validation.md (Concepts 7-10)
- koncepcje-v2-graph.md (Concepts 11-14)
- koncepcje-v2-quality.md (Concepts 15-16)
- koncepcje-v2-evidence.md (Concepts 17-18)

**Why?** V1 was 600 lines, hard to navigate. V2: each file < 200 lines, focused.

---

## 📈 Success Criteria

**Engineering phase complete when:**
- [x] PRD-V2 req-freeze achieved ✅
- [ ] TDD-V2 design-complete (in progress)
- [x] All 6 components specified (COMP-001 to COMP-006) ✅
- [x] 9 ADRs documented ✅ (8 accepted, 1 draft)
- [x] Concepts-V2 modular structure ✅
- [x] RTM initialized ✅
- [ ] DoR passed for all components (3/6 done: Parser, Validator, Storage)

**Status:** 📝 **85% complete** (awaiting TDD design-complete, remaining DORs)

---

## 📖 Zobacz też

### Upstream (Dependencies)

- **[../pre-production/](../pre-production/)** — Vision, Business Case (strategic foundation)
- **[../satellites/evidence/](../satellites/evidence/)** — E-140 to E-146 (tech evaluations)

### Downstream (Impacts)

- **[../implementation/](../implementation/)** — Implementation Plan (maps to components)
- **[../satellites/approvals/](../satellites/approvals/)** — DoR for components

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Graf B: Engineering Dependencies
- **[../templates/przedprodukcyjna/](../templates/przedprodukcyjna/)** — PRD, TDD templates
- **[../satellites/decisions/DECISION-INDEX.md](../satellites/decisions/DECISION-INDEX.md)** — ADR dependency graph

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Engineering (Design Phase)
**Status:** 📝 85% Complete (req-freeze ✅, design-complete pending)
**Next Phase:** Implementation (Sprint 1: Parser + Models)
