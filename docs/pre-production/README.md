# Pre-Production — Business Justification & Strategic Vision

## 📋 Przeznaczenie

Folder **pre-production/** zawiera **dokumenty strategiczne fazy discovery** — uzasadnienie biznesowe, wizję produktu, i roadmap definiujące DLACZEGO budujemy system Ishkarim i JAK wygląda sukces.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Strategic alignment** — Wyrównanie projektu z celami biznesowymi
- **Business justification** — ROI (674%), uzasadnienie build vs buy
- **Vision setting** — Wizja długoterminowa (12-24 miesiące)
- **Stakeholder buy-in** — Funding approval, executive support
- **Roadmap planning** — High-level milestones i phased delivery

## 👥 Kto używa?

- **C-Level / Leadership** — Executive Summary, Business Case (funding decisions)
- **Product Owners** — Vision, Roadmap (strategic direction)
- **Stakeholders** — All docs (understand project context)
- **Finance** — Business Case (budget approval, ROI tracking)
- **Project Managers** — Roadmap (timeline, milestones)

## ⏱️ Kiedy używać?

**Timing:** Faza **discovery** (pre-engineering)

**Lifecycle Position:**
```
Pre-Production (YOU ARE HERE) → Engineering → Implementation → Operations
     ↓
  Vision, Business Case, Roadmap → PRD, TDD → Sprint Execution → Deployment
```

**Kiedy czytać:**
- **Onboarding** — Pierwszy krok dla nowych członków zespołu
- **Strategic review** — Quarterly business case updates, vision refresh
- **Funding decisions** — Before budget allocation
- **Scope negotiations** — When stakeholders question priorities

---

## 📂 Zawartość folderu (8 plików)

### Current Versions (V2) ✅

**1. vision-v2.md**
- **ID:** VISION-001-V2
- **Status:** ✅ Approved (2025-12-26)
- **Rozmiar:** ~500 lines
- **Cel:** Długoterminowa wizja produktu (12-24 miesiące)
- **Zawiera:**
  - Strategic goal & OKRs
  - Alternatives considered (cloud vs local-first, CLI vs GUI)
  - Roadmap decision graph (MVP-first vs feature-complete)
  - Context snapshot (market Q4 2025, team skills, constraints)
  - Evidence trail (E-080 to E-086)
- **Approved by:** Product Owner, Tech Lead
- **Dependencies:** Requires EXEC-SUM-001 (approved)
- **Impacts:** INFORMS Business Case, PRD, Roadmap

**2. business-case-v2.md**
- **ID:** BIZ-CASE-001-V2
- **Status:** ✅ Approved (2025-12-26)
- **Rozmiar:** ~600 lines
- **Cel:** Uzasadnienie biznesowe — dlaczego budować, ROI, build vs buy
- **Kluczowe metryki:**
  - **ROI:** 674% over 24 months
  - **Payback period:** 7 months
  - **NPV:** +$340k (assuming cost basis)
  - **TCO:** Build < Buy (3x cheaper over 24mo)
- **Zawiera:**
  - Pain points survey (E-081, E-082, E-083 user interviews)
  - Time-tracking study (avg 4.2h/week on doc management)
  - Build vs Buy analysis (vs Confluence, Notion, custom)
  - Risk assessment (E-092)
  - Budget breakdown (E-091)
- **Evidence:** E-120 through E-133 (13 evidence docs)
- **Gates:** FUNDING-APPROVAL-001 depends on this
- **Dependencies:** Requires EXEC-SUM-001, VISION-001-V2
- **Impacts:** INFORMS PRD (requirements justified by ROI)

**3. executive-summary.md**
- **ID:** EXEC-SUM-001
- **Status:** ✅ Approved (2025-12-26)
- **Rozmiar:** ~200 lines (concise for C-level)
- **Cel:** One-page strategic overview dla executive stakeholders
- **Zawiera:**
  - Problem statement (documentation chaos, lack of proof system)
  - Solution overview (local-first proof system with graph viz)
  - Business value (ROI 674%, 7mo payback)
  - Strategic fit (aligns with digital transformation goals)
  - High-level roadmap (MVP by Q2 2025, V1.0 by Q3)
- **Approved by:** CPO, CTO (implicit via funding approval)
- **Impacts:** REQUIRES for Vision, Business Case (strategic foundation)

**4. roadmap.md**
- **ID:** ROADMAP-001
- **Status:** 📝 Draft (baseline established)
- **Rozmiar:** ~400 lines
- **Cel:** Phased delivery plan (6-12 months)
- **Fazy:**
  - **Phase 1 (MVP):** Parser, Validator, Graph (Q1-Q2 2025)
  - **Phase 2 (GUI):** PySide6 app, Graph viz (Q2 2025)
  - **Phase 3 (V1.0):** Gap engine, Reports, Export (Q3 2025)
  - **Phase 4 (Extensions):** Obsidian plugin, CI/CD integration (Q4 2025)
- **Dependencies:** INFORMS Implementation Plan (6-sprint breakdown)
- **Evidence:** E-086 (roadmap options analysis)

### Deprecated Versions (V1) 🗂️

**5. vision-v1-deprecated.md**
- **Status:** Deprecated (superseded by VISION-001-V2)
- **Kept for:** Historical reference, migration context
- **Superseded:** 2025-12-26
- **Migration guide:** See CONCEPTS-001-MIGRATION-GUIDE.md (applies to vision too)

**6. business-case-v1-deprecated.md**
- **Status:** Deprecated (superseded by BIZ-CASE-001-V2)
- **Kept for:** Audit trail, understanding evolution
- **Superseded:** 2025-12-26
- **Key changes v1→v2:** Updated ROI (624% → 674%), added evidence trail, NPV calculation

### Symlinks / Duplicates (for convenience)

**7. vision.md**
- **Type:** Symlink or duplicate of vision-v2.md
- **Purpose:** Convenience (users expect `vision.md`, not `vision-v2.md`)

**8. business-case.md**
- **Type:** Symlink or duplicate of business-case-v2.md
- **Purpose:** Convenience (canonical name points to current version)

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Wejście:**
- (brak) — Pre-production to **pierwsza faza**, nie ma upstream dependencies

**Assumptions:**
- Market conditions Q4 2025 (Confluence/Notion dominance, no proof-system tools)
- Team skills (Python, TypeScript, NetworkX, PySide6)
- Budget availability (funding approved)

### Impacts (Co te dokumenty popychają do przodu)

**Vision-v2 INFORMS:**
- `engineering/prd-v2.md` — Wymagania muszą align z wizją
- `engineering/tdd-v2.md` — Architektura wspiera vision
- `roadmap.md` — Roadmap execution opiera się na vision

**Business-Case-v2 INFORMS:**
- `engineering/prd-v2.md` — Requirements justified by ROI
- `satellites/approvals/FUNDING-APPROVAL-001.md` — Funding decision based on business case

**Executive-Summary REQUIRES for:**
- `vision-v2.md` — Strategic alignment check
- `business-case-v2.md` — ROI claims must align with exec summary

**Roadmap INFORMS:**
- `implementation/implementation-plan.md` — 6-sprint breakdown maps to roadmap phases

### Related Documents

- `satellites/evidence/E-080-market-research.md` — Competitive analysis (supports vision)
- `satellites/evidence/E-081-083-user-interviews.md` — User pain points (supports business case)
- `satellites/evidence/E-090-roi-calculation.md` — ROI details (supports business case 674%)
- `satellites/evidence/E-091-budget-breakdown.md` — Cost structure
- `satellites/evidence/E-092-risk-assessment.md` — Risks identified
- `satellites/approvals/FUNDING-APPROVAL-001.md` — Funding decision record

---

## 📊 Statystyki

- **Liczba plików:** 8 (4 current + 2 deprecated + 2 symlinks/duplicates)
- **Status:**
  - ✅ Approved: 3 (Vision-v2, Business-Case-v2, Executive Summary)
  - 📝 Draft: 1 (Roadmap)
  - 🗂️ Deprecated: 2 (Vision-v1, Business-Case-v1)
  - 🔗 Symlinks: 2 (vision.md, business-case.md)
- **Evidence coverage:** 13 docs (E-080 to E-086, E-090 to E-092, E-120 to E-133)
- **Approvals:** FUNDING-APPROVAL-001 ✅
- **ROI:** 674% over 24 months, 7-month payback
- **Timeline:** MVP by Q2 2025, V1.0 by Q3 2025

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Onboarding nowego członka zespołu

**Czas:** 30-60 minut

1. **Start:** `executive-summary.md` (10 min) — Zrozum problem, solution, business value
2. **Deep dive:** `vision-v2.md` (20 min) — Wizja długoterminowa, alternatives considered
3. **Justification:** `business-case-v2.md` (30 min) — ROI, build vs buy, evidence
4. **Roadmap:** `roadmap.md` (10 min) — Phased delivery plan

**Output:** Pełne zrozumienie DLACZEGO budujemy system i JAK wygląda sukces

### Scenario 2: Quarterly business review

**Czas:** 1h (meeting prep)

1. Review `business-case-v2.md` — Czy assumptions nadal valid? (market, team, budget)
2. Update ROI calculations — Recalculate z actual data (if available)
3. Review `roadmap.md` — Adjust milestones based on progress
4. Update `vision-v2.md` — Refine based on learnings (if major pivot)
5. Re-approve if needed — Get stakeholder sign-off on updates

**Output:** Updated business case, adjusted roadmap, continued stakeholder buy-in

### Scenario 3: Funding decision (CFO review)

**Czas:** 30 min (prep) + meeting

1. **Czytaj:** `executive-summary.md` (CFO wants 1-pager)
2. **Evidence:** `satellites/evidence/E-090-roi-calculation.md` (ROI breakdown)
3. **Risks:** `satellites/evidence/E-092-risk-assessment.md` (what could go wrong)
4. **Budget:** `satellites/evidence/E-091-budget-breakdown.md` (cost structure)
5. **Decision:** `satellites/approvals/FUNDING-APPROVAL-001.md` (formal approval)

**Output:** Funding approved/rejected with documented rationale

---

## ⚠️ Uwagi

### Wersjowanie

**Pattern:**
- V2 = **CURRENT** (approved 2025-12-26)
- V1 = **DEPRECATED** (kept for audit trail)
- Migration guides available (CONCEPTS-001-MIGRATION-GUIDE.md applies to vision structure)

**Dlaczego V2?**
- V1 lacked evidence trail (no E-XXX references)
- V1 ROI outdated (624% → 674% after refined calculations)
- V1 alternatives incomplete (missing roadmap decision graph)

### Evidence-Driven Claims

**Każde twierdzenie MUSI mieć evidence:**

- **"Market gap dla proof-system tools"** → E-080 (market research)
- **"Users spend 4.2h/week on doc management"** → E-081, E-082, E-083 (user interviews)
- **"ROI 674% over 24 months"** → E-090 (ROI calculation)
- **"Build 3x cheaper than Buy"** → E-090, E-091 (TCO analysis)

**Bez evidence = claim odrzucony w review!**

### Status Constraints

**Approved docs nie mogą być edytowane bez:**
1. **Change Request** — Formalna CR (satellite document)
2. **Re-review** — Stakeholder review of changes
3. **Re-approval** — Updated approval date w frontmatter

**Dlaczego?** Approved docs są foundation dla downstream docs (PRD, TDD). Nieautoryzowane zmiany niszczą dependency integrity.

### Lifecycle Gates

**FUNDING-APPROVAL-001** gate requires:
- ✅ Business Case approved
- ✅ Executive Summary approved
- ✅ Vision approved (strategic alignment)
- ✅ No critical risks unmitigated (E-092)

**Current status:** ✅ All conditions met (funding approved 2025-12-26)

---

## 📈 Success Criteria

**Pre-Production phase complete when:**
- [x] Executive Summary approved
- [x] Vision V2 approved
- [x] Business Case V2 approved
- [x] Roadmap baseline established
- [x] Funding approval obtained (FUNDING-APPROVAL-001)
- [x] Evidence trail complete (min 10 docs for MVP) → 13 docs ✅
- [x] Stakeholder buy-in secured (CPO, CTO, Finance)

**Status:** ✅ **COMPLETE** (2025-12-26)

---

## 📖 Zobacz też

### Upstream (Dependencies)

- (brak — pre-production to pierwsza faza)

### Downstream (Impacts)

- **[../engineering/](../engineering/)** — PRD, TDD oparte na vision & business case
- **[../implementation/](../implementation/)** — Implementation plan maps to roadmap phases
- **[../satellites/evidence/](../satellites/evidence/)** — Evidence docs (E-080 to E-092)
- **[../satellites/approvals/](../satellites/approvals/)** — FUNDING-APPROVAL-001

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Graf A: Pre-Production Workflow
- **[../templates/przedprodukcyjna/](../templates/przedprodukcyjna/)** — Szablony użyte do utworzenia tych docs
- **[../FINAL-GAP-ANALYSIS-REPORT.md](../FINAL-GAP-ANALYSIS-REPORT.md)** — How these docs were created (gap remediation)

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Pre-Production (Discovery Phase)
**Status:** ✅ Phase Complete (all docs approved, funding secured)
**Next Phase:** Engineering (PRD, TDD) → Status: req-freeze achieved ✅
