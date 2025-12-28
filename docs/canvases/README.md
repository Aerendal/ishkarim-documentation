# Canvases — Visual Documentation

## 📋 Przeznaczenie

Folder **canvases/** zawiera **wizualną dokumentację systemu** — Obsidian canvas files (node-edge graphs) pokazujące zależności między dokumentami, flow procesu, i architekturę systemu w formie graficznej.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Visual system overview** — High-level architecture w formie diagramu
- **Document flow visualization** — Jak dokumenty przepływają przez fazy (discovery → design → implementation → production)
- **Dependency mapping** — Wizualizacja zależności (requires, blocks, informs)
- **Onboarding** — Nowi członkowie zespołu szybko rozumieją strukturę
- **Stakeholder communication** — Visual presentations (executive reviews)

## 👥 Kto używa?

- **System Architects** — Projektują system, wizualizują zależności
- **New Team Members** — Onboarding (visual learning faster than reading)
- **Stakeholders** — Executive presentations (show project structure)
- **Product Owners** — Understand document relationships
- **Developers** — Navigate complex dependency chains visually

## ⏱️ Kiedy używać?

**Timing:** **Cross-cutting** — visual companion to text docs

**Use Cases:**
- **First day onboarding** — Show Project-Overview.canvas (15 min overview)
- **Architecture review** — Discuss system structure visually
- **Dependency planning** — Map impacts before making changes
- **Stakeholder updates** — Visual progress reports

---

## 📂 Zawartość folderu (1 plik)

### Project-Overview.canvas ✅

**Format:** Obsidian Canvas (JSON node-edge graph)
**Created:** 2025-12-26
**Status:** ✅ Active (updated as system evolves)
**Rozmiar:** ~500 KB (JSON with embedded node text)

**Zawartość:**

**Nodes (Dokumenty):**
- **Pre-Production Phase:**
  - Executive Summary
  - Vision-v2
  - Business-Case-v2
  - Roadmap
- **Engineering Phase:**
  - PRD-v2
  - TDD-v2
  - Concepts-v2
  - ADR-001 to ADR-009
  - Components (COMP-001 to COMP-006)
- **Implementation Phase:**
  - Implementation Plan
  - Test Plan
- **Operations Phase:**
  - Deployment Guide
  - Contingency Plans
- **Satellites:**
  - Evidence nodes (E-080, E-090, E-140, etc. — representative sample)
  - Approvals (FUNDING-APPROVAL-001, DoR nodes)
  - TODOs, Decision Index

**Edges (Dependencies):**
- **requires** (solid arrow): A requires B (blocking dependency)
- **blocks** (red arrow): A blocks B until condition met
- **informs** (dashed arrow): A influences B (informative dependency)
- **creates** (dotted arrow): Parent → Satellite (e.g., PRD → TODO-PRD-001)

**Layout:**
- **Swimlanes** (horizontal): Pre-Production | Engineering | Implementation | Operations
- **Evidence trail** (sidebar): E-XXX nodes linked to parent docs
- **Critical path** (highlighted): Vision → PRD → TDD → Implementation → Deployment

**Visual Features:**
- **Color coding:**
  - Green nodes: Approved (Vision-v2, Business-Case-v2, PRD-v2)
  - Yellow nodes: Draft (TDD-v2, Implementation Plan)
  - Blue nodes: Evidence (E-XXX)
  - Purple nodes: Satellites (TODOs, Approvals)
- **Node size:** Proportional to document size (larger nodes = bigger docs)
- **Grouping:** Related docs grouped (e.g., all ADRs clustered)

**Example Flow Visualization:**
```
Executive Summary
    ↓ requires
Vision-v2
    ↓ informs
Business-Case-v2
    ↓ requires + creates E-090 (ROI)
PRD-v2 (req-freeze ✅)
    ↓ blocks
TDD-v2 (design-complete pending)
    ↓ blocks
Implementation Plan
    ↓ informs
Deployment Guide
```

**How to View:**

1. **Obsidian (Recommended):**
   - Open `docs/` folder as Obsidian vault
   - Navigate to `canvases/Project-Overview.canvas`
   - Obsidian renders interactive graph (zoom, pan, click nodes)

2. **JSON Viewer (Fallback):**
   - Open in text editor (JSON format)
   - Nodes: `{"type": "text", "text": "...", "x": ..., "y": ...}`
   - Edges: `{"fromNode": "...", "toNode": "...", "label": "requires"}`

3. **Export to PNG (for presentations):**
   - Obsidian: Right-click canvas → "Export to image"
   - Share PNG with stakeholders (no Obsidian needed)

**Maintenance:**

- **Update frequency:** Monthly (or when major docs added)
- **Who updates:** System Architect, Product Owner
- **How:** Obsidian canvas editor (drag-drop nodes, draw edges)

**Related:**

- Complements: `dependency_graph.md` (text-based graph, Mermaid syntax)
- Superset: Canvas shows visual layout + spatial relationships (dependency_graph.md = pure connections)

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Canvas CREATED FROM:**
- All docs in `pre-production/`, `engineering/`, `implementation/`, `operations/`, `satellites/`
- Frontmatter dependencies (requires, blocks, informs)

### Impacts (Co te dokumenty popychają do przodu)

**Canvas SUPPORTS:**
- Onboarding (visual learning)
- Architecture reviews (stakeholder discussions)
- Dependency planning (impact analysis)

### Related Documents

- **[../dependency_graph.md](../dependency_graph.md)** — Text-based dependency graph (Mermaid)
- **[../pre-production/](../pre-production/)** through **[../operations/](../operations/)** — All docs visualized in canvas
- **[../satellites/](../satellites/)** — Evidence, approvals shown as satellite nodes

---

## 📊 Statystyki

- **Liczba plików:** 1 (Project-Overview.canvas)
- **Nodes:** ~80 (documents + evidence + satellites)
- **Edges:** ~150 (dependencies: requires, blocks, informs)
- **Format:** Obsidian Canvas (JSON)
- **Size:** ~500 KB
- **Last updated:** 2025-12-26

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Onboarding (Day 1)

**Czas:** 15 min (visual overview)

1. Open Obsidian vault (`docs/`)
2. Navigate to `canvases/Project-Overview.canvas`
3. **Guided tour** (follow swimlanes):
   - Pre-Production (Vision, Business Case)
   - Engineering (PRD, TDD, ADRs)
   - Implementation (6-sprint plan)
   - Operations (Deployment)
4. Click nodes → Read linked docs (Obsidian auto-navigates)

**Output:** High-level understanding of system structure (15 min vs 2h reading)

### Scenario 2: Dependency impact analysis

**Czas:** 10 min (visual inspection)

**Question:** "If I change PRD-v2, what's impacted?"

1. Open canvas, locate PRD-v2 node
2. Follow outgoing edges (PRD → TDD, PRD → Test Plan, PRD → Implementation)
3. Identify all downstream docs (visual cascade)
4. Check edge labels: "blocks" (critical), "informs" (informative)

**Output:** Impact scope identified (need to review TDD, Test Plan, Implementation)

### Scenario 3: Executive presentation

**Czas:** 30 min (prep + presentation)

1. Export canvas to PNG (Obsidian: right-click → Export)
2. Annotate PNG (highlight critical path, add status colors)
3. Present to executives:
   - "Green nodes = approved (Vision, PRD)"
   - "Yellow nodes = in progress (TDD, Implementation)"
   - "Critical path: Vision → PRD → TDD → Deployment"
4. Answer questions (zoom into specific nodes if needed)

**Output:** Exec stakeholders understand project structure (visual > spreadsheet)

---

## ⚠️ Uwagi

### Obsidian-specific format

**Canvas files are Obsidian-specific:**
- JSON format, but proprietary schema (Obsidian canvas plugin)
- **Best viewed in Obsidian** (interactive, renders layout)
- Fallback: JSON viewers, but lose visual layout

**Why Obsidian?**
- Native canvas support (drag-drop node editor)
- Integrates with markdown docs (click node → navigate to .md file)
- Graph view complements canvas (auto-generated from backlinks)

### Maintenance burden

**Canvases require manual updates:**
- When new docs added → Add nodes to canvas
- When dependencies change → Update edges
- **Frequency:** Monthly (or after major milestones)

**Mitigation (future):**
- Auto-generate canvas from frontmatter dependencies (Python script)
- CI/CD: Validate canvas matches dependency_graph.md

### Complementary to dependency_graph.md

**Canvas vs dependency_graph.md:**

| Feature | Canvas | dependency_graph.md |
|---------|--------|---------------------|
| **Format** | Visual (Obsidian JSON) | Text (Mermaid graphs) |
| **Layout** | Manual (spatial positioning) | Auto-generated (Mermaid rendering) |
| **Interactivity** | Obsidian (click, zoom, pan) | GitHub (static Mermaid render) |
| **Completeness** | ~80 nodes (high-level) | 158 docs (exhaustive) |
| **Maintenance** | Manual updates | Script-generated |

**Best practice:** Use both!
- Canvas: Visual overview, onboarding, presentations
- dependency_graph.md: Exhaustive reference, CI/CD validation

---

## 📈 Success Criteria

**Canvases folder healthy when:**
- [x] Project-Overview.canvas exists ✅
- [ ] Canvas updated monthly (or after milestones)
- [ ] All major docs represented (currently ~80/158 docs = 50%)
- [ ] Critical path highlighted (visual guidance)
- [ ] Export to PNG available (for presentations)

**Status:** ✅ **Active** (canvas exists, needs regular updates)

---

## 📖 Zobacz też

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Text-based dependency graph (exhaustive)
- **[../README.md](../README.md)** — Master README (text overview of system)
- **All doc folders** — Canvas visualizes docs from all folders

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Canvases (Visual Documentation)
**Format:** Obsidian Canvas (JSON node-edge graph)
**Nodes:** ~80 (documents + satellites), **Edges:** ~150 (dependencies)
**Best viewed in:** Obsidian (interactive visualization)
