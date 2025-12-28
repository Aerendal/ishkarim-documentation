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

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: VISION-*
    type: requires
    reason: "Vision Document provides strategic context and long-term product direction"
    conditions:
      - when: "project.has_vision_doc === true"
        applies: true
    sections:
      - from: "Vision §13 Strategic Business Goals"
        to: "§1 Context & Strategic goal"
        influence: "Strategic goals drive roadmap priorities and focus areas"
      - from: "Vision §10 Product Strategy"
        to: "§2 Roadmap swimlanes"
        influence: "Product strategy defines roadmap horizons and themes"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case provides ROI justification and prioritization basis"
    conditions:
      - when: "project.has_business_case === true"
        applies: true
    sections:
      - from: "Business Case §15 Success Metrics"
        to: "§8 KPIs & success metrics"
        influence: "Business metrics become roadmap success metrics"
      - from: "Business Case §8 Financial Analysis"
        to: "§7 Capacity & Budget summary"
        influence: "Financial projections inform roadmap budget allocation"

  - id: PRD-*
    type: influences
    reason: "PRD requirements inform roadmap epic definitions and scope"
    conditions:
      - when: "project.starts_with_prd === true"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§4 Epics / Feature sets"
        influence: "PRD requirements are grouped into roadmap epics"
      - from: "PRD §11 Success Metrics"
        to: "§8 KPIs & success metrics"
        influence: "PRD success metrics align with roadmap KPIs"

  - id: MODULE-ANALYSIS-ROADMAP-*
    type: influences
    reason: "Module Analysis Roadmap provides technical decomposition and dependencies"
    conditions:
      - when: "project.is_complex_platform === true"
        applies: true
    sections:
      - from: "Module Analysis Roadmap §4 Module Dependencies"
        to: "§5 Dependencies & Blockers"
        influence: "Technical module dependencies affect roadmap sequencing"

  - id: INNOVATION-ROADMAP-*
    type: influences
    reason: "Innovation Roadmap identifies emerging tech and R&D opportunities"
    conditions:
      - when: "project.has_innovation_track === true"
        applies: true
    sections:
      - from: "Innovation Roadmap §3 Tech Experiments"
        to: "§4 Epics / Feature sets"
        influence: "Innovation experiments may become product features"
```

### Impacts
```yaml
impacts:
  - id: PRD-*
    type: blocks
    reason: "PRD cannot be detailed without roadmap prioritization and scope definition"
    conditions:
      - when: "roadmap_first_approach === true"
        applies: true
    sections:
      - from: "§4 Epics / Feature sets"
        to: "PRD §5 Functional Requirements"
        influence: "Roadmap epics define which requirements are in scope for PRD"
      - from: "§3 Milestones & Releases"
        to: "PRD §10 Milestones & Timeline"
        influence: "Roadmap milestones become PRD delivery milestones"

  - id: CAPACITY-PLAN-*
    type: blocks
    reason: "Capacity planning requires roadmap milestones and effort estimates"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Milestones & Releases"
        to: "Capacity Plan §3 Demand by milestone"
        influence: "Roadmap milestones define capacity planning periods"
      - from: "§4 Epics / Feature sets"
        to: "Capacity Plan §3 Demand by milestone"
        influence: "Epic effort estimates drive capacity demand"

  - id: RISK-REGISTER-*
    type: blocks
    reason: "Risk register tracks roadmap-level risks and blockers"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§6 Risks"
        to: "Risk Register §1 Risk table"
        influence: "Roadmap risks are detailed in risk register"
      - from: "§5 Dependencies & Blockers"
        to: "Risk Register §1 Risk table"
        influence: "Dependencies and blockers become risk items"

  - id: RELEASE-PLAN-*
    type: blocks
    reason: "Release planning requires roadmap milestones and release scope"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Milestones & Releases"
        to: "Release Plan §2 Release Schedule"
        influence: "Roadmap milestones define release dates and scope"
      - from: "§4 Epics / Feature sets"
        to: "Release Plan §3 Release Scope"
        influence: "Epics are decomposed into release deliverables"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Sprint planning derives work from roadmap epics"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "§4 Epics / Feature sets"
        to: "Sprint Core §3 Sprint Backlog"
        influence: "Roadmap epics are broken into sprint stories"

  - id: KPI-DASHBOARD-SPEC-*
    type: blocks
    reason: "KPI dashboard tracks roadmap progress and success metrics"
    conditions:
      - when: "project.requires_kpi_tracking === true"
        applies: true
    sections:
      - from: "§8 KPIs & success metrics"
        to: "KPI Dashboard §2 Metrics"
        influence: "Roadmap KPIs define dashboard metrics"
      - from: "§3 Milestones & Releases"
        to: "KPI Dashboard §2 Metrics"
        influence: "Milestone progress tracking becomes dashboard metric"

  - id: RELEASE-CHECKLIST-*
    type: influences
    reason: "Release checklist ensures roadmap milestones meet quality gates"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§9 Checkpoints & Gates"
        to: "Release Checklist §1 Pre-freeze"
        influence: "Roadmap quality gates become release checklist items"
```

### Related
```yaml
related:
  - id: TDD-*
    type: informs
    reason: "TDD design must support roadmap technical requirements"

  - id: TEST-PLAN-*
    type: informs
    reason: "Test planning aligns with roadmap release schedule"

  - id: RESOURCE-REQUIREMENTS-*
    type: informs
    reason: "Roadmap epics inform team composition and skill requirements"

  - id: TIMELINE-*
    type: informs
    reason: "Roadmap milestones become detailed project timeline"

  - id: STAKEHOLDER-MAP-*
    type: informs
    reason: "Roadmap communication plan requires stakeholder identification"

  - id: RTM-*
    type: informs
    reason: "Requirements traceability tracks roadmap epic delivery"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ROADMAP-PROD-*.md"
    required: false
    purpose: "Track roadmap review meetings, stakeholder approvals, dependency resolution"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ROADMAP-PROD-*.md"
    required: true
    purpose: "Store strategic planning sessions, exec approvals, roadmap reviews, prioritization workshops"

  - type: Approval
    path: "satellites/approvals/APPROVAL-ROADMAP-PROD-*.md"
    required: true
    purpose: "CEO/CPO approval required before roadmap publication"

  - type: DoR
    path: "satellites/dor/DOR-ROADMAP-PROD-*.md"
    required: true
    purpose: "Prerequisites: vision validated, business case approved, capacity estimated, key risks identified"
```

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
