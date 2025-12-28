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

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: ROADMAP-PROD-*
    type: requires
    reason: "Product Roadmap defines milestones and epic scope for capacity planning"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Roadmap §3 Milestones & Releases"
        to: "§3 Demand by milestone"
        influence: "Roadmap milestones define capacity planning periods and deadlines"
      - from: "Roadmap §4 Epics / Feature sets"
        to: "§3 Demand by milestone"
        influence: "Epic complexity estimates drive FTE demand calculations"

  - id: RESOURCE-REQUIREMENTS-*
    type: requires
    reason: "Resource Requirements define team composition and skill needs"
    conditions:
      - when: "project.has_resource_plan === true"
        applies: true
    sections:
      - from: "Resource Requirements §2 Team Composition"
        to: "§1 Summary"
        influence: "Team composition defines available FTE capacity"
      - from: "Resource Requirements §3 Skills Matrix"
        to: "§4 Gaps & mitigation"
        influence: "Skills gaps inform hiring and contractor needs"

  - id: TIMELINE-*
    type: influences
    reason: "Project timeline affects capacity planning periods"
    conditions:
      - when: "project.has_detailed_timeline === true"
        applies: true
    sections:
      - from: "Timeline §2 Project Phases"
        to: "§3 Demand by milestone"
        influence: "Phase timelines define when capacity is needed"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Sprint velocity data informs capacity estimates"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "Sprint Core §7 Velocity & Metrics"
        to: "§2 Assumptions"
        influence: "Historical velocity affects effort estimation assumptions"
```

### Impacts
```yaml
impacts:
  - id: RESOURCE-REQUIREMENTS-*
    type: blocks
    reason: "Capacity gaps trigger resource requirements updates and hiring"
    conditions:
      - when: "capacity_plan.has_gaps === true"
        applies: true
    sections:
      - from: "§4 Gaps & mitigation"
        to: "Resource Requirements §4 Hiring Plan"
        influence: "Identified capacity gaps drive hiring and contractor acquisition"

  - id: ROADMAP-PROD-*
    type: influences
    reason: "Capacity constraints may force roadmap adjustments"
    conditions:
      - when: "capacity < demand"
        applies: true
    sections:
      - from: "§4 Gaps & mitigation"
        to: "Roadmap §3 Milestones & Releases"
        influence: "Capacity shortfalls may delay milestones or reduce scope"

  - id: TIMELINE-*
    type: influences
    reason: "Capacity availability affects project timeline feasibility"
    conditions:
      - when: "project.has_timeline === true"
        applies: true
    sections:
      - from: "§3 Demand by milestone"
        to: "Timeline §3 Critical Path"
        influence: "Capacity allocation affects timeline critical path"

  - id: BUDGET-PLAN-*
    type: blocks
    reason: "Capacity plan drives budget for salaries and contractors"
    conditions:
      - when: "project.has_budget === true"
        applies: true
    sections:
      - from: "§1 Summary (contractor hours)"
        to: "Budget Plan §3 Personnel Costs"
        influence: "Contractor hours and FTE needs determine personnel budget"

  - id: RISK-REGISTER-*
    type: influences
    reason: "Capacity gaps and constraints are project risks"
    conditions:
      - when: "capacity_plan.has_gaps === true"
        applies: true
    sections:
      - from: "§4 Gaps & mitigation"
        to: "Risk Register §1 Risk table"
        influence: "Capacity shortfalls become risk items requiring mitigation"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Capacity plan affects sprint team allocation"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "§1 Summary (available FTE)"
        to: "Sprint Core §2 Team Composition"
        influence: "Available FTE defines sprint team size and composition"
```

### Related
```yaml
related:
  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Contractor needs inform vendor management"

  - id: ONBOARDING-GUIDE-*
    type: informs
    reason: "New hires require onboarding based on capacity gaps"

  - id: KNOWLEDGE-TRANSFER-PLAN-*
    type: informs
    reason: "Capacity transitions require knowledge transfer"

  - id: HR-HIRING-PLAN-*
    type: informs
    reason: "Capacity gaps drive hiring pipeline"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CAP-PLAN-*.md"
    required: false
    purpose: "Track capacity updates, hiring approvals, contractor procurement"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CAP-PLAN-*.md"
    required: true
    purpose: "Store velocity data, team availability calendars, contractor quotes, hiring approvals"

  - type: Approval
    path: "satellites/approvals/APPROVAL-CAP-PLAN-*.md"
    required: true
    purpose: "Delivery Manager and Finance approval for contractor budget and hiring"

  - type: DoR
    path: "satellites/dor/DOR-CAP-PLAN-*.md"
    required: true
    purpose: "Prerequisites: roadmap milestones defined, team composition known, historical velocity available"
```

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
