# Templates — System Szablonów Dokumentacji Ishkarim

## 📋 Czym jest templates/?

Folder **templates/** zawiera **174 reusable templates** — puste szablony dokumentów do tworzenia instancji projektowych. To fundament całego systemu dokumentacji Ishkarim opartego na "proof system approach".

**System templates/ ≠ project docs (docs/)**
- `templates/` = **Puste szablony** (reusable, generic, 174 files)
- `docs/` (root folders) = **Wypełnione instancje** (specific to Ishkarim project)

---

## 🗂️ Struktura folderów

System szablonów zorganizowany według **typów dokumentów i faz projektu**:

```
templates/
├── przedprodukcyjna/     (30 templates) - Pre-production phase
├── produkcyjna/          (63 templates) - Production phase
├── branzowa/             (16 templates) - Industry/compliance specific
├── supporting/           (16 files)     - Meta-documentation & reference
├── examples/             (13 files)     - Filled template examples
├── specs/                (4 specs)      - System specifications
├── sprints/              (11 templates) - Agile sprint management
├── roadmaps/             (6 templates)  - Strategic planning
├── atomic/               (8 templates)  - Lightweight satellites
└── migration/            (1 template)   - System migration planning
```

### Mapowanie folderów do zastosowania

| Folder | Liczba | Zastosowanie | Kluczowe szablony |
|--------|--------|--------------|-------------------|
| **[przedprodukcyjna/](przedprodukcyjna/)** | 30 | Pre-production planning | PRD, TDD, Business Case, Vision, ADR |
| **[produkcyjna/](produkcyjna/)** | 63 | Production operations | Runbook, SLA, Postmortem, Deployment, Monitoring |
| **[branzowa/](branzowa/)** | 16 | Industry compliance | GDPR, HIPAA, SOX, ISO, Audit docs |
| **[sprints/](sprints/)** | 11 | Agile sprint mgmt | Sprint plan, backlog, DoR, DoD, retrospective |
| **[roadmaps/](roadmaps/)** | 6 | Strategic planning | Product roadmap, capacity plan, risk register |
| **[atomic/](atomic/)** | 8 | Satellite artifacts | TODO, DoR, DoD, Approval, Evidence |
| **[supporting/](supporting/)** | 16 | Meta & reference | Overviews, guides, summaries |
| **[examples/](examples/)** | 13 | Best practices | Filled examples (target quality) |
| **[specs/](specs/)** | 4 | System foundation | Doc types, error codes, gates, satellites |
| **[migration/](migration/)** | 1 | System migration | Migration planning (AS-IS → TO-BE) |

**Total:** 174 template files (168 templates + 4 specs + 2 meta)

---

## 🎯 Główne cechy systemu

### 1. Proof System Approach

**Evidence-driven documentation:**
- Każde twierdzenie wsparte dowodami (Evidence: E-XXX)
- Dependency tracking (requires, blocks, informs)
- Quality gates (go/no-go checkpoints)

**Example pattern:**
```yaml
---
id: DOC-001
dependencies:
  - id: PARENT-DOC
    type: requires
    status_constraint: [approved]
evidence_ids: ["E-080", "E-090"]
---

## Claim
"ROI is 674% over 24 months"

**Evidence:** E-090 (ROI calculation with methodology)
```

### 2. Frontmatter Metadata (YAML)

**Wszystkie szablony mają frontmatter:**
```yaml
---
id: [DOCUMENT-ID]
title: "Document Title"
type: [doc-type]
status: draft | in-review | approved | archived
created: YYYY-MM-DD
owner: "Team/Person"
dependencies:
  - id: [DOC-ID]
    type: requires | blocks | informs
impacts:
  - id: [DOC-ID]
    type: blocks | informs
evidence_ids: ["E-XXX", "E-YYY"]
---
```

**Why frontmatter?**
- Machine-readable (parser can extract metadata)
- Dependency graph auto-generation
- Status tracking automated
- Obsidian compatibility

### 3. Document Cross-References

**Modern format (na górze dokumentu):**
```yaml
## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: DOC-ID-*
    type: requires | influences
    reason: "Dlaczego potrzebujemy tego dokumentu"
    sections: [§1, §3] (które sekcje używane)

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: DOC-ID-*
    type: blocks | influences | informs
    reason: "Na co wpływa"

### Related Documents
related:
  - id: DOC-ID-*
    type: informs

### Satellite Documents
satellites:
  - type: TODO | DoR | DoD | Approval | Evidence
    path: "satellites/..."
    required: true | false
```

### 4. Satellite Pattern

**Lightweight artifacts supporting main docs:**

```
Parent Doc (e.g., PRD)
  ├── TODO-PRD-001.md (work tracking)
  ├── DOR-PRD-001.md (definition of ready)
  ├── DOD-PRD-001.md (definition of done)
  ├── APPROVAL-PRD-001.md (sign-off record)
  └── EVIDENCE-PRD-001.md (supporting research)
```

**Pattern:** 1 parent → N satellites (1:N relationship)

### 5. Versioning Support

**Template evolution:**
- V1 → V2 transitions documented
- DIFF reports (what changed v1→v2)
- Migration guides (how to upgrade)
- Deprecated templates kept (audit trail)

---

## 📊 Statystyki systemu

### Coverage

- **Liczba szablonów:** 174 (complete template system)
- **Pokrycie lifecycle:** 100% (discovery → design → execution → production)
- **Dependency connections:** 1,367 (w dependency_graph.md)
- **Template categories:** 10 głównych folderów

### Top Templates (Most Referenced)

1. **ROADMAP-PROD** — #1 most-referenced (28 dependencies)
2. **PRD** — Core requirements template
3. **TDD** — Technical design template
4. **Business Case** — ROI justification
5. **ADR** — Architecture decision records

### Template Sizes

- **Smallest:** Atomic templates (20-50 lines)
- **Medium:** Sprint, Roadmap templates (200-400 lines)
- **Largest:** PRD, TDD, Compliance templates (600-800 lines)

---

## 🚀 Quick Start — Jak używać szablonów

### Scenario 1: Rozpoczynasz nowy projekt

**Czas:** 30 min (setup)

1. **Read:** `supporting/meta/documentation-system-overview.md` (10 min)
2. **Choose phase:** Jaką fazę projektu zaczynasz?
   - Discovery → `przedprodukcyjna/` (Business Case, Vision, PRD)
   - Execution → `sprints/` (Sprint plan, backlog)
   - Production → `produkcyjna/` (Deployment, runbook)
3. **Copy template:**
   ```bash
   cp templates/przedprodukcyjna/prd-template.md docs/project/prd.md
   ```
4. **Fill frontmatter:** ID, title, owner, status
5. **Fill sections:** Replace `[TODO: ...]` placeholders
6. **Add evidence:** Create satellites/evidence/E-XXX.md for claims

**Output:** Dokument ready z pełną strukturą

### Scenario 2: Sprawdzasz jakość dokumentu

**Czas:** 15 min (validation)

1. **Read:** `specs/specs_doc_types.md` (find your doc type)
2. **Check required sections:**
   ```yaml
   PRD:
     required_sections:
       - {id: SEC-PRD-GOAL, title: "Cel produktu"}
       - {id: SEC-PRD-FUNC, title: "Wymagania funkcjonalne"}
   ```
3. **Check dependencies:** Are all `requires` docs approved?
4. **Check satellites:** DoR/DoD/TODO/Approval created?
5. **Run validation** (future): `ishkarim validate prd.md`

**Output:** Document passes quality checks

### Scenario 3: Dodajesz nowy typ dokumentu

**Czas:** 2-4h (design + implementation)

1. **Read:** `supporting/extending-guide.md` (template creation guide)
2. **Check specs:** `specs/specs_doc_types.md` (existing types)
3. **Identify gap:** Is there really no template? (avoid duplication)
4. **Design template:**
   - Frontmatter schema
   - Required sections
   - Satellite requirements
   - Dependencies
5. **Create template file:** `templates/[category]/[name]-template.md`
6. **Register in specs:** Add to `specs/specs_doc_types.md`
7. **Add example:** `examples/[name]-example.md`
8. **Update README:** This file + folder README

**Output:** New template type available

---

## 🔗 Powiązania

### Dependencies (Co napędza system szablonów)

**System specs (foundation):**
- `specs/specs_doc_types.md` — Defines all doc types, required sections
- `specs/specs_error_codes.md` — Validation error codes (E-100 to S-900)
- `specs/specs_gates.md` — Quality gates (go/no-go checkpoints)
- `specs/satelitarne_artefakty_*.md` — Satellite framework

**Templates CREATED FROM:**
- User needs (E-081, E-082, E-083 interviews)
- Gap analysis (TEMPLATE-GAP-ANALYSIS.md)
- Best practices (industry standards, PMBOK, TOGAF)

### Impacts (Co system szablonów umożliwia)

**Templates ENABLE:**
- `docs/` project instances (filled templates)
- Automated validation (parser + validator)
- Dependency graph generation (1,367 connections)
- Quality gates enforcement (req-freeze, design-complete)

**Templates SUPPORT:**
- Onboarding (new team members use templates)
- Consistency (all docs follow same structure)
- Traceability (dependencies tracked)
- Evidence backing (proof system approach)

---

## ⚙️ Specyfikacje (specs/)

**Foundation layer** — 4 core specifications:

### 1. specs_doc_types.md
**Rejestr typów dokumentów**

Definiuje wszystkie typy:
```yaml
PRD:
  required_meta: [id, doctype, status, version, owner]
  required_sections:
    - {id: SEC-PRD-GOAL, title: "Cel produktu"}
    - {id: SEC-PRD-FUNC, title: "Wymagania funkcjonalne"}
  satellites_required: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL]
  dependencies:
    - {doctype: BUSINESS_CASE, min_status: approved}
```

**Use:** Validator checks compliance

### 2. specs_error_codes.md
**Kody błędów walidacji**

- E-100: Missing file
- E-110: Missing required section
- E-120: Placeholder present
- E-130: Missing evidence
- E-140: Missing dependency link
- E-150: Gate blocked
- W-310: Recommended section missing
- S-900: Secret/PII detected

**Use:** Error reporting, remediation

### 3. specs_gates.md
**Quality gates**

- GATE-GO_NO_GO: Initial project approval
- GATE-REQ_FREEZE: Requirements freeze
- GATE-RELEASE_READY: Release readiness
- GATE-OPS_HANDOVER: Operations handover
- GATE-CLOSURE: Project closure

**Use:** Block progress until criteria met

### 4. satelitarne_artefakty_*.md
**Satellite framework**

Definiuje 8 typów satelitów:
- TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, EVIDENCE, CHANGELOG, CR, ADR

**Use:** Lightweight artifact management

---

## 📖 Folder READMEs (Nawigacja)

Każdy folder ma dedykowany README:

- **[przedprodukcyjna/README.md](przedprodukcyjna/README.md)** — 30 templates (PRD, TDD, Business Case, Vision, ADR)
- **[produkcyjna/README.md](produkcyjna/README.md)** — 63 templates (Runbook, SLA, Postmortem, Deployment)
- **[branzowa/README.md](branzowa/README.md)** — 16 templates (GDPR, HIPAA, SOX, ISO compliance)
- **[sprints/README.md](sprints/README.md)** — 11 templates (Sprint management, DoR/DoD, retro)
- **[roadmaps/README.md](roadmaps/README.md)** — 6 templates (Product roadmap, capacity, risk, release)
- **[atomic/README.md](atomic/README.md)** — 8 templates (Lightweight satellites: TODO, DoR, DoD, Approval)
- **[supporting/README.md](supporting/README.md)** — 16 files (Meta-docs, guides, overviews)
- **[examples/README.md](examples/README.md)** — 13 files (Filled examples showing target quality)
- **[specs/README.md](specs/README.md)** — 4 specs (Foundation: doc types, errors, gates, satellites)
- **[migration/README.md](migration/README.md)** — 1 template (System migration planning)

---

## ⚠️ Uwagi

### Templates vs Instances

**CRITICAL:** Rozróżnienie templates/ vs docs/:

| Aspect | templates/ | docs/ (root folders) |
|--------|-----------|----------------------|
| **Purpose** | Reusable, generic | Specific to Ishkarim project |
| **Content** | Placeholders `[TODO: ...]` | Filled, real data |
| **Status** | N/A (templates don't have status) | draft / approved / archived |
| **Evidence** | Example E-XXX references | Real evidence (E-080 to E-270) |
| **Editing** | Update template → affects all future instances | Update instance → affects only that doc |

**Example:**
- `templates/przedprodukcyjna/prd-template.md` → Template (reusable)
- `docs/engineering/prd-v2.md` → Instance (filled, status: req-freeze)

### Version Evolution

**Templates evolve:**
- Template updated → Future instances use new version
- Existing instances NOT auto-updated (manual migration if needed)
- Breaking changes → Version bump (template-v2.md)
- DIFF reports document changes

### Contribution Guidelines

**Before adding new template:**
1. Check existing templates (avoid duplication)
2. Read `supporting/extending-guide.md`
3. Follow frontmatter schema (specs/specs_doc_types.md)
4. Add example instance (examples/)
5. Update folder README
6. Update this master README (templates/README.md)

### Automated Validation

**Future: Parser + Validator**

System "Archivista Żywego Zapisu" (in development):
- Parser: Read .md, extract frontmatter, build graph
- Validator: Check required sections, verify dependencies, enforce gates
- Gap Engine: Identify missing docs, broken refs, status conflicts

**Current:** Manual validation (checklist-based)

---

## 📈 Success Criteria

**Template system healthy when:**
- [x] 174 templates covering full lifecycle ✅
- [x] All 10 folder READMEs exist ✅
- [x] Specs define all doc types ✅
- [x] Examples demonstrate best practices ✅
- [ ] Automated validation (parser + validator) — In development
- [ ] CI/CD integration (validate on commit) — Planned
- [ ] Template usage analytics (which templates most used) — Future

**Status:** ✅ **Complete foundation** (174 templates, 100% coverage)

---

## 🛠️ Tooling

### Current (Manual)

**Obsidian:**
- Open `templates/` as vault
- Browse templates, copy-paste
- Graph view (see template relationships)

**Git:**
- Version control for templates
- Track changes, revert if needed
- Collaborate (PR reviews for new templates)

### Planned (Automated)

**Ishkarim CLI** (in development):
```bash
# Create instance from template
ishkarim new prd --from templates/przedprodukcyjna/prd-template.md

# Validate instance
ishkarim validate docs/project/prd.md

# Show template dependencies
ishkarim deps prd-template.md

# Generate dependency graph
ishkarim graph --output dependency_graph.md
```

---

## 📖 Zobacz też

### Project Documentation

- **[../README.md](../README.md)** — Master docs/ README (project instances)
- **[../dependency_graph.md](../dependency_graph.md)** — 1,367 connections between 158 docs
- **[../TEMPLATE-CONSOLIDATION-STRATEGY.md](../TEMPLATE-CONSOLIDATION-STRATEGY.md)** — Consolidation strategy

### Proposals

- **[../proposals/](../proposals/)** — System enhancement proposals (4 active)
- **[../TEMPLATE-GAP-ANALYSIS.md](../TEMPLATE-GAP-ANALYSIS.md)** — Gap analysis

### Examples

- **[examples/](examples/)** — Filled template examples (best practices)
- **[../pre-production/](../pre-production/)** through **[../operations/](../operations/)** — Real project instances

---

**Wygenerowano:** 2025-12-28
**System:** Ishkarim Documentation Templates (Proof System Approach)
**Coverage:** 174 templates, 10 categories, 100% lifecycle
**Foundation:** 4 core specs (doc types, error codes, gates, satellites)
**Status:** ✅ Complete & production-ready
