---
id: "SPRINT-BACKLOG-SXX"
title: "Sprint Backlog — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master / Delivery Lead"
status: "draft"          # draft|in-review|approved|closed
version: "0.1"
period: "YYYY-MM-DD..YYYY-MM-DD"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Backlog realizuje zadania wybrane w planie sprintu"
    sections:
      - from: "Sprint Plan §4 Backlog wybrany do sprintu"
        to: "§Items Table"
        influence: "Określa listę zadań do wykonania"

  - id: SPRINT-DOR-SXX
    type: requires
    reason: "Wszystkie zadania muszą spełniać Definition of Ready"
    sections:
      - from: "Sprint DoR §Kryteria"
        to: "§Notes"
        influence: "Filtruje zadania gotowe do wejścia do sprintu"

  - id: TODO-PRD-*
    type: influences
    reason: "Zadania z PRD TODO trafiają do backlogu sprintu"
    sections:
      - from: "PRD TODO §Tasks"
        to: "§Items Table (Related doc / TODO)"
        influence: "Łączy zadania backlogu z wymaganiami PRD"

  - id: TODO-TDD-*
    type: influences
    reason: "Zadania techniczne z TDD zasilają backlog"
    sections:
      - from: "TDD TODO §Technical Tasks"
        to: "§Items Table (Related doc / TODO)"
        influence: "Dodaje zadania implementacyjne i techniczne"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-REVIEW-SXX
    type: blocks
    reason: "Review nie może się odbyć bez znanego backlogu"
    sections:
      - from: "§Items Table (Status)"
        to: "Sprint Review §2 Delivered"
        influence: "Status zadań określa co zostało dostarczone"

  - id: SPRINT-METRICS-SXX
    type: informs
    reason: "Backlog jest podstawą do kalkulacji velocity i burndown"
    sections:
      - from: "§Items Table (Estimate, Status)"
        to: "Sprint Metrics §Delivery"
        influence: "Estymacje i statusy zasilają metryki sprintu"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Zablokowane zadania generują impedimenty"
    sections:
      - from: "§Items Table (Status=blocked)"
        to: "Impediments Log §Impediment"
        influence: "Zadania zablokowane trafiają do rejestru impedimentów"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: informs
    reason: "Change Requesty modyfikują zakres backlogu"

  - id: SPRINT-ACTION-ITEMS-SXX
    type: complements
    reason: "Action Items z retro mogą generować nowe zadania"

### Satellite Documents
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PRD-*.md"
    required: true
    purpose: "Szczegółowe zadania z wymagań produktowych"

  - type: TODO
    path: "satellites/todos/TODO-TDD-*.md"
    required: true
    purpose: "Zadania techniczne z dokumentacji technicznej"

  - type: Evidence
    path: "satellites/evidence/SPRINT-BACKLOG-SXX-*.md"
    required: false
    purpose: "Dowody wykonania zadań (screeny, logi, testy)"

# Sprint Backlog — SXX

| ID | Item | Owner | Estimate | Status | Related doc / TODO | Acceptance |
|---|---|---|---:|---|---|---|
| SXX-001 | ... | ... | 3 | todo | TODO-PRD-001 | AC link |

## Notes
- Do sprintu trafiają tylko itemy spełniające Sprint DoR.
