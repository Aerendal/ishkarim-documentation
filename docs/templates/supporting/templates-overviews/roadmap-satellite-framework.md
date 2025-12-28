# Szablony — Roadmapy i satelitarne artefakty

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: SATELITARNE-ARTEFAKTY-*
    type: requires
    reason: "Roadmap templates implement satellite artifacts framework opisany w Satelitarne Artefakty kanwie"
    sections:
      - from: "Satelitarne Artefakty atomic templates (TODO, DoR, DoD, Approval, Evidence, etc.)"
        to: "Roadmap satellite templates implementation"
        influence: "Atomic templates definiują structure of roadmap-specific satellites"

  - id: SPECS-DOC-TYPES-*
    type: influences
    reason: "Roadmap templates follow Doc Types specifications dla ROADMAP_PRODUCT doctype"
    sections:
      - from: "Specs Doc Types ROADMAP_PRODUCT specification"
        to: "roadmap.product.md template"
        influence: "Doc Types specification definiuje required sections i satellites dla roadmaps"

  - id: INNOVATION-ROADMAP-*
    type: influences
    reason: "Innovation Roadmap template influences roadmap template design"
    sections:
      - from: "Innovation Roadmap template structure"
        to: "roadmap.product.md atomic template"
        influence: "Innovation-specific roadmap informs general roadmap template"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-ROADMAP-INSTANCES-*
    type: blocks
    reason: "Roadmap templates są used to create actual project roadmaps"
    sections:
      - from: "roadmap.product.md, capacity-plan.md, risk-register.md templates"
        to: "Project-specific roadmap instances"
        influence: "Templates provide structure dla roadmap creation"

  - id: PROJECT-MGMT-PLAN-*
    type: influences
    reason: "Roadmap templates integrate z Project Management Plan processes"
    sections:
      - from: "Roadmap templates (milestones, capacity, risks)"
        to: "Project Mgmt Plan §12 Harmonogram, §15 Plan ryzyka"
        influence: "Roadmap artifacts feed into project planning"

  - id: INNOVATION-ROADMAP-*
    type: influences
    reason: "Roadmap atomic templates mogą be adapted dla Innovation Roadmap instances"
    sections:
      - from: "Atomic templates (TODO, DoR, DoD, etc.)"
        to: "Innovation Roadmap satellite artifacts"
        influence: "Atomic templates are reusable across different roadmap types"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: SPECS-GATES-*
    type: informs
    reason: "Roadmap templates reference gates (checkpoints) definitions"

  - id: FINANCIAL-PLAN-*
    type: informs
    reason: "Roadmap capacity-plan.md coordinates z Financial Plan budgeting"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Roadmap risk-register.md coordinates z Risk Overview"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ROADMAP-TEMPLATES-*.md"
    required: false
    purpose: "Tracking roadmap template improvements, new satellite types addition"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ROADMAP-TEMPLATES-*.md"
    required: false
    purpose: "Roadmap template usage examples, effectiveness analysis, user feedback"

  - type: DoD
    path: "satellites/dod/DOD-ROADMAP-TEMPLATES-*.md"
    required: false
    purpose: "Definition of Done: template completeness validation, example roadmaps created, documentation updated"
```

---

To jest komplet szablonów i artefaktów pomocniczych ("satelitów"), gotowych do skopiowania do struktury Twojego repozytorium. Pliki są przygotowane tak, aby ułatwić zarządzanie roadmapami, planowaniem wydań oraz powiązaną dokumentacją operacyjną i compliance.

**Zestaw zawiera:**

- `templates/roadmaps/` — główny szablon roadmapy oraz powiązane artefakty: capacity plan, risk register, release checklist, postmortem, KPI spec.
- `templates/atomic/` — lekkie, atomowe pliki (TODO, DoR, DoD, Approval, Evidence, Risk Item, Release checklist — atom, Postmortem — atom itd.).
- `manifests/` — przykładowe manifesty CSV i JSON z metadanymi plików (importowalne do narzędzi PM).

Skopiuj wybrane pliki do odpowiednich katalogów (np. `docs/<project>/roadmaps/` lub `templates/roadmaps/`) i edytuj front‑matter zgodnie z projektem.

---

## Główne zasady użycia

1. **Proporcjonalność**: stosuj satelity tylko tam, gdzie ich wartość uzasadnia koszt utrzymania.  
2. **Jedno zadanie = jeden atom**: każdy plik atomowy powinien dotyczyć jednej sprawy (TODO, ADR, CR, Evidence itp.).  
3. **Traceability**: używaj front‑matter `related` do wiązania artefaktów z dokumentem głównym.  
4. **Automatyzacja**: front‑matter pozwala na generowanie issue/PR skeletonów i walidację CI.  
5. **Wersjonowanie**: trzymaj dokumenty w repo, każda akceptacja i decyzja powinna mieć commit/PR.

---

# Szablony: Roadmaps (katalog `templates/roadmaps/`)

Poniżej znajdują się kompletne, gotowe do użycia pliki markdown. Zachowaj front‑matter i dostosuj pola `project`, `owner`, `date_created` itp.

### `roadmap.product.md`
```markdown
---
id: "ROADMAP-PROD-001"
title: "Product Roadmap — H1 2026"
project: "NAZWA_PROJEKTU"
owner: "Head of Product"
status: "draft"          # draft|in-review|approved|archived
version: "0.1"
date_created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
horizon: "12 months"
related_docs: ["DOC-BUSCASE-001","DOC-PRD-001"]
tags: ["roadmap","product","release"]
approvers: ["CEO","CPO"]
---

# Product Roadmap — H1 2026

## 0. Meta
- **Project:** NAZWA_PROJEKTU
- **Owner:** Head of Product
- **Status:** draft
- **Version:** 0.1

## 1. Context & Strategic goal
- Krótkie podsumowanie kontekstu i celów strategicznych (powiązanie z OKR/KPIs):
  - OKR-1: ...
  - KPI: ...

## 2. Roadmap swimlanes (high‑level)
| Horizon | Focus | Key outcomes |
|---|---|---|
| Strategic (2–5y) | Platform growth | ... |
| Product (12m) | Core features | ... |
| Release (3–6m) | Release X | ... |
| Tactical (sprint) | Iteration delivery | ... |

## 3. Milestones & Releases
- **Release 1 (M1)** — YYYY‑MM‑DD — scope: Epics A, B
- **Release 2 (M2)** — YYYY‑MM‑DD — scope: Epics C

## 4. Epics / Feature sets (skrót)
- **EPIC‑001:** Tytuł — Owner — Priorytet — Hipoteza wartości
  - DoR: link/todo
  - Dependencies: EPIC‑003

## 5. Dependencies & Blockers
- External vendor X: opis zależności
- Regulatory approval Y: spodziewana data

## 6. Risks (top items) — link do `risk-register.md`
- R1: opis ryzyka — owner — mitigacje

## 7. Capacity & Budget summary — link do `capacity-plan.md`
- FTE needed: 5 devs for 3 months
- Budget: EUR 100k

## 8. KPIs & success metrics
- Metric A: target
- Metric B: target

## 9. Checkpoints & Gates
- Quarterly strategic review (data)
- Pre‑freeze DoR check (data)
- Pre‑release DoD verification (data)

## 10. Communication / Stakeholders
- Weekly: Product Sync (owners)
- Monthly: Exec update (CPO/CEO)

## 11. Links & evidence
- Business Case: DOC‑BUSCASE‑001
- RTM: docs/rtm.csv

---
*Suggested length: 2–6 pages. Keep the roadmap high‑level and link do szczegółowych artefaktów.*
```

---

### `capacity-plan.md`
```markdown
---
id: "CAP-PLAN-001"
title: "Capacity Plan — H1 2026"
project: "NAZWA_PROJEKTU"
owner: "Delivery Manager"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# Capacity Plan — H1 2026

## Summary
- Dostępne zasoby: 12 FTE (engineering)
- Dostępne godziny kontraktorskie: 800h

## Assumptions
- Okna urlopowe: ...
- Rezerwa (bench): 10%

## Demand by milestone
| Milestone | Effort (FTE months) | Owner |
|---|---:|---|
| Release 1 | 5.0 | Delivery Lead |
| Release 2 | 3.0 | Delivery Lead |

## Gaps & mitigation
- Luka: potrzebne +2 backend devs → plan: zatrudnienie / contractor

## Notes
- Aktualizować co miesiąc i synchronizować z finansami.
```

---

### `risk-register.md`
```markdown
---
id: "RISK-REGISTER-001"
title: "Roadmap Risk Register"
project: "NAZWA_PROJEKTU"
owner: "Head of Product"
version: "0.1"
status: "live"
related: ["ROADMAP-PROD-001"]
---

# Risk Register (roadmap‑level)

| ID | Risk description | Likelihood | Impact | Severity | Owner | Mitigation | Status |
|---|---|---:|---:|---:|---|---|---|
| R‑001 | Regulatory approval delay | Medium | High | High | Legal Lead | Early engagement; contingency plan | Open |
| R‑002 | Vendor integration fails | Low | Medium | Medium | Integration Lead | PoC first; fallback option | Open |

---

Aktualizuj ten plik na bieżąco — każdy wiersz to pojedynczy RAID item.
```

---

### `release-checklist.md`
```markdown
---
id: "REL-CHECK-001"
title: "Release Checklist — Release 1"
project: "NAZWA_PROJEKTU"
owner: "Release Manager"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# Release Checklist — Release 1

## Pre‑freeze
- [ ] All critical PRs merged into release branch
- [ ] DoR check for all epics: passed
- [ ] Release notes: draft

## Pre‑release
- [ ] QA smoke tests green on staging
- [ ] Security scans (SAST/DAST) passed
- [ ] DB migration scripts reviewed and rollback tested
- [ ] Ops runbook updated

## Release window
- [ ] Cutover: run idempotent deploy script
- [ ] Smoke tests on production passed
- [ ] Monitoring thresholds verified

## Post‑release
- [ ] Postmortem scheduled
- [ ] Stakeholder communication sent
- [ ] Changelog published
```

---

### `postmortem_template.md`
```markdown
---
id: "POST-001"
title: "Postmortem — Release 1"
project: "NAZWA_PROJEKTU"
owner: "Incident Lead"
version: "0.1"
status: "draft"
related: ["REL-CHECK-001","ROADMAP-PROD-001"]
---

# Postmortem — Release 1

## Summary
- What happened (brief):

## Impact
- Users affected, metrics, outage duration

## Timeline
- YYYY‑MM‑DD HH:MM — Event
- YYYY‑MM‑DD HH:MM — Event

## Root cause
- Summary of root cause

## Remediation & Actions
- Action 1 — owner — due date
- Action 2 — owner — due date

## Lessons learned
- Bullet points

## Follow‑ups
- Tracking in TODOs / issue tracker
```

---

### `kpi-dashboard-spec.md`
```markdown
---
id: "KPI-001"
title: "KPI & Dashboard Spec"
project: "NAZWA_PROJEKTU"
owner: "Product Ops"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# KPI & Dashboard Spec

## Metrics
- % complete (by epic) — metoda pomiaru
- Delivered value vs forecast — metoda pomiaru
- Lead time for features — definicja

## Dashboards
- Exec dashboard: metrics & SLA
- Delivery dashboard: progress per release

## Data sources
- Data warehouse tables, ETL jobs
```

---

# Szablony atomowe: `templates/atomic/`

Atomowe, lekkie pliki są przeznaczone do szybkiego tworzenia i powiązania z głównymi dokumentami. Wykorzystaj je jako pojedyncze, wersjonowane artefakty.

### `TODO_template.md`
```markdown
---
id: "TODO-<DOC>-001"
type: "todo"
title: "<Short title>"
owner: "<Name / Team>"
status: "todo"
priority: "P1"
created: "YYYY-MM-DD"
due: "YYYY-MM-DD"
related: ["DOC-<id>"]
acceptance_criteria: []
---

# TODO: <Short title>

## Description
- Krótki opis zadania

## Checklist
- [ ] Krok 1
- [ ] Krok 2

## Notes / Links
- Link do źródeł
```

---

### `DoR_template.md` (Definition of Ready)
```markdown
---
id: "DEF-READY-<DOC>-001"
type: "definition"
title: "Definition of Ready — <DOC>"
owner: "Product Owner"
status: "draft"
created: "YYYY-MM-DD"
related: ["DOC-<id>"]
---

# Definition of Ready (DoR)

## Purpose
- Kryteria wejścia przed rozpoczęciem prac

## Criteria (example)
- [ ] Description and business goal
- [ ] Acceptance Criteria (GIVEN/WHEN/THEN)
- [ ] Estimation (story points)
- [ ] Owner available
- [ ] Dependencies listed
- [ ] Test data / mocks available
- [ ] Tech Lead checked feasibility
```

---

### `DoD_template.md` (Definition of Done)
```markdown
---
id: "DEF-DONE-<DOC>-001"
type: "definition"
title: "Definition of Done — <DOC>"
owner: "Team Lead / QA"
status: "draft"
created: "YYYY-MM-DD"
related: ["DOC-<id>"]
---

# Definition of Done (DoD)

## Purpose
- Kryteria uznania pracy za zakończoną

## Criteria (example)
- [ ] Code merged to main/release branch
- [ ] Unit and integration tests green
- [ ] E2E / UAT (if required) passed
- [ ] Documentation updated (API, runbook)
- [ ] Build artifact published / staging smoke tests passed
- [ ] Security checks / linters passed
- [ ] Owner approval / sign-off
```

---

### `Approval_template.md`
```markdown
---
id: "APPROVAL-<DOC>-001"
type: "approval"
title: "Approval — <DOC> v0.1"
approver: "Name"
date: "YYYY-MM-DD"
related: ["DOC-<id>"]
notes: ""
---

# Approval

- **Approver:** Name
- **Date:** YYYY-MM-DD
- **Notes:** Short notes
```

---

### `evidence_template.md`
```markdown
---
id: "EVID-<DOC>-001"
type: "evidence"
title: "Evidence — <DOC>"
owner: "Owner"
related: ["DOC-<id>"]
---

# Evidence

- **File:** path/to/file.xlsx
- **Description:** what it proves and where used
- **Hash / checksum:** optional
```

---

### `risk_item_template.md`
```markdown
---
id: "RISK-<DOC>-001"
type: "risk"
title: "Risk item"
owners: ["Name"]
likelihood: "Low|Medium|High"
impact: "Low|Medium|High"
status: "open|mitigating|closed"
related: ["DOC-<id>"]
---

# Risk item

- Description: ...
- Mitigation: ...
- Owner: ...
```

---

### `release_checklist_atom.md`
```markdown
---
id: "REL-ATOM-001"
type: "checklist"
title: "Release Checklist — atom"
related: ["REL-CHECK-001"]
---

# Release checklist (atom)
- [ ] Smoke tests passed
- [ ] Monitoring configured
- [ ] Rollback verified
```

---

### `postmortem_atom.md`
```markdown
---
id: "PM-ATOM-001"
type: "postmortem"
title: "Postmortem — atom"
related: ["POST-001"]
---

# Postmortem (atom)
- Summary:
- Timeline:
- Root cause:
- Actions:
```

---

# Manifests

### `manifests/manifest.csv` (przykład)
```csv
id,filename,category,owner,estimated_days,related
ROADMAP-PROD-001,templates/roadmaps/roadmap.product.md,roadmap,Head of Product,3,DOC-BUSCASE-001
REL-CHECK-001,templates/roadmaps/release-checklist.md,release,Release Manager,1,ROADMAP-PROD-001
TODO-<DOC>-001,templates/atomic/TODO_template.md,todo,Team,0.1,DOC-<id>
```


### `manifests/manifest.json` (przykład)
```json
[
  {"id":"ROADMAP-PROD-001","filename":"templates/roadmaps/roadmap.product.md","category":"roadmap","owner":"Head of Product","estimated_days":3},
  {"id":"REL-CHECK-001","filename":"templates/roadmaps/release-checklist.md","category":"release","owner":"Release Manager","estimated_days":1}
]
```

---

## Opcjonalny skrypt — `scripts/render_templates.py` (stub)

```python
# render_templates.py — minimalny stub do renderowania Jinja2 templates
from jinja2 import Environment, FileSystemLoader
import yaml

env = Environment(loader=FileSystemLoader('templates'))

def render(template_path, context_path, out_path):
    template = env.get_template(template_path)
    with open(context_path) as f:
        ctx = yaml.safe_load(f)
    rendered = template.render(**ctx)
    with open(out_path, 'w') as o:
        o.write(rendered)

if __name__ == '__main__':
    # example usage: render('roadmaps/roadmap.product.md', 'data/meta.yaml', 'docs/project/roadmap.md')
    pass
```

---

## Co zrobiłem
- Przygotowałem komplet szablonów do skopiowania — roadmapy + satelity atomowe + manifesty + prosty stub skryptu do renderowania.

## Co chcesz teraz?
- Mogę:
  1) Wykonać i umieścić te pliki bezpośrednio w kanwie `templates/` (utworzyć osobne pliki),
  2) Wygenerować przykładowe wypełnienia (demo) dla Executive Summary, PRD, Roadmap (czy chcesz konkretny projekt jako przykład?),
  3) Przygotować GitHub Action / CI snippet do walidacji front‑matter i tworzenia issue skeletons z TODOs.

Wskaż 1 / 2 / 3 lub kombinację (np. 1+2).

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: ROADMAP-*
    type: requires
    reason: "Roadmaps require project vision and strategic goals from planning documents"
    conditions:
      - when: "project.phase === 'production'"
        applies: true
      - when: "project.size < 'medium'"
        applies: false
    sections:
      - from: "Vision Document §13 Strategiczne cele biznesowe"
        to: "§1 Context & Strategic goal"
        influence: "Strategic goals define roadmap OKRs and KPIs"
      - from: "Business Case §17 Plan osiągnięcia ROI"
        to: "§3 Milestones & Releases"
        influence: "ROI timeline shapes release planning"

  - id: PRD-*
    type: requires
    reason: "Product roadmaps require defined product requirements to plan features"
    conditions:
      - when: "roadmap.type === 'product'"
        applies: true
      - when: "roadmap.type === 'strategic'"
        applies: false
    sections:
      - from: "PRD §4 Wymagania funkcjonalne"
        to: "§4 Epics / Feature sets"
        influence: "Functional requirements define epics and feature priorities"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: SPRINT-PLAN-*
    type: blocks
    reason: "Sprint planning cannot begin without defined roadmap milestones and priorities"
    conditions:
      - when: "project.methodology === 'agile'"
        applies: true
      - when: "project.methodology === 'waterfall'"
        applies: false
    sections:
      - from: "§4 Epics / Feature sets"
        to: "Sprint Plan §2 Zakres"
        influence: "Roadmap epics define sprint scope and priorities"
      - from: "§7 Capacity & Budget summary"
        to: "Sprint Plan §3 Capacity"
        influence: "Roadmap capacity constraints inform sprint capacity planning"

  - id: RELEASE-CHECK-*
    type: blocks
    reason: "Release checklist requires roadmap milestones and criteria"
    sections:
      - from: "§3 Milestones & Releases"
        to: "Release Checklist §1 Pre-freeze"
        influence: "Roadmap milestones define release gates"

  - id: TODO-*
    type: informs
    reason: "Roadmap epics generate TODO items for implementation tracking"
    sections:
      - from: "§4 Epics / Feature sets"
        to: "TODO §1 Description"
        influence: "Each epic generates actionable TODO items with owners"
```

### Related Documents

```yaml
related:
  - id: CAPACITY-PLAN-*
    type: informs
    reason: "Capacity planning supports roadmap resource allocation"

  - id: RISK-REGISTER-*
    type: informs
    reason: "Risk register tracks roadmap-level risks and mitigation"

  - id: KPI-*
    type: informs
    reason: "KPI dashboards measure roadmap progress and success metrics"
```

### Satellite Documents

```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ROADMAP-*.md"
    required: false
    purpose: "Track action items per epic and milestone"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ROADMAP-*.md"
    required: false
    purpose: "Market research and capacity data supporting roadmap decisions"

  - type: DoR
    path: "satellites/dor/DOR-ROADMAP-*.md"
    required: true
    purpose: "Definition of Ready for roadmap items and epics"

  - type: DoD
    path: "satellites/dod/DOD-ROADMAP-*.md"
    required: true
    purpose: "Definition of Done for roadmap milestones and releases"
```
