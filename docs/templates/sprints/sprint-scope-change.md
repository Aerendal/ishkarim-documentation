---
id: "SPRINT-CR-SXX-001"
title: "Sprint Scope Change Request — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Owner"
status: "draft"          # draft|approved|rejected
related: ["SPRINT-PLAN-SXX","SPRINT-BACKLOG-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Impedimenty mogą wymuszać zmiany scope'u"
    sections:
      - from: "Impediments Log §Impediment (Impact=High)"
        to: "§Zmiana"
        influence: "Blokery mogą wymagać usunięcia zadań z sprintu"

  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Change Request modyfikuje zatwierdzony plan sprintu"
    sections:
      - from: "Sprint Plan §2 Zakres (Scope)"
        to: "§Zmiana"
        influence: "Bazowy scope jest punktem odniesienia dla zmian"

  - id: PRD-*
    type: influences
    reason: "Zmiany w wymaganiach produktowych mogą wpływać na sprint"
    sections:
      - from: "PRD §Requirements (priority change)"
        to: "§Zmiana"
        influence: "Shift w priorytetach może wymagać re-planowania"

  - id: RISK-*
    type: influences
    reason: "Zmaterializowane ryzyka mogą wymuszać scope changes"
    sections:
      - from: "Risk Register §Active Risks"
        to: "§Wpływ"
        influence: "Ryzyka wpływają na assessment wpływu zmiany"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-BACKLOG-SXX
    type: blocks
    reason: "Approved CR modyfikuje backlog sprintu"
    sections:
      - from: "§Zmiana (status=approved)"
        to: "Sprint Backlog §Items"
        influence: "Dodaje lub usuwa zadania z backlogu"

  - id: SPRINT-PLAN-SXX
    type: influences
    reason: "CR może wymagać aktualizacji planu sprintu"
    sections:
      - from: "§Wpływ §Na cel sprintu"
        to: "Sprint Plan §1 Sprint Goal"
        influence: "Znaczące zmiany mogą wymagać redefinicji celu"

  - id: SPRINT-REVIEW-SXX
    type: informs
    reason: "CR jest kontekstem dla oceny realizacji sprintu"
    sections:
      - from: "§Decyzja"
        to: "Sprint Review §1 Sprint Goal — status"
        influence: "Approved changes wyjaśniają deviations od planu"

  - id: SPRINT-METRICS-SXX
    type: informs
    reason: "Scope changes wpływają na metryki sprintu"
    sections:
      - from: "§Zmiana"
        to: "Sprint Metrics §Delivery"
        influence: "CR mogą wpływać na velocity i burndown"

### Related Documents (Powiązane dokumenty)
related:
  - id: ROADMAP-PROD-001
    type: informs
    reason: "Scope changes mogą wpływać na timeline roadmapy"

  - id: CHANGE-REQUEST-*
    type: complements
    reason: "Związek z projektowymi CR documents"

### Satellite Documents
satellites:
  - type: Approval
    path: "satellites/approvals/SPRINT-CR-SXX-001-APPROVAL.md"
    required: true
    purpose: "Formalne zatwierdzenie scope change przez stakeholderów"

  - type: Evidence
    path: "satellites/evidence/SPRINT-CR-SXX-001-*.md"
    required: false
    purpose: "Dowody uzasadniające scope change (impedimenty, ryzyka)"

  - type: Impact Assessment
    path: "satellites/assessments/SPRINT-CR-SXX-001-IMPACT.md"
    required: true
    purpose: "Szczegółowa analiza wpływu na sprint goal, timeline, resources"

# Sprint Scope Change Request — SXX

## Zmiana
- Co dodajemy/usuwamy i dlaczego.

## Wpływ
- Na cel sprintu:
- Na terminy:
- Na ryzyko:

## Decyzja
- Approved/Rejected
- Approver: ...
- Date: ...
