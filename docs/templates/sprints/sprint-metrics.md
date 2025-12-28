---
id: "SPRINT-METRICS-SXX"
title: "Sprint Metrics — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Ops"
status: "draft"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-BACKLOG-SXX
    type: requires
    reason: "Backlog jest źródłem danych dla velocity i burndown"
    sections:
      - from: "Sprint Backlog §Items (Estimate, Status)"
        to: "§Delivery"
        influence: "Estymacje i completion generują velocity metrics"

  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Plan określa baseline dla porównania metrics"
    sections:
      - from: "Sprint Plan §3 Capacity"
        to: "§Delivery"
        influence: "Planned capacity vs actual delivery"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Impedimenty wpływają na delivery metrics"
    sections:
      - from: "Impediments Log §Impediment (Impact)"
        to: "§Delivery"
        influence: "Blokery wyjaśniają deviations w velocity"

  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: influences
    reason: "Scope changes wpływają na interpretację metrics"
    sections:
      - from: "Scope Change §Zmiana"
        to: "§Delivery"
        influence: "CR wyjaśniają zmiany w planned vs actual"

  - id: TEST-RESULTS-*
    type: influences
    reason: "Wyniki testów zasilają quality metrics"
    sections:
      - from: "Test Results §Defects"
        to: "§Quality"
        influence: "Bug counts i test coverage są quality indicators"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-REVIEW-SXX
    type: informs
    reason: "Metrics dostarczają danych do sprint review"
    sections:
      - from: "§Delivery, §Quality"
        to: "Sprint Review §2 Delivered"
        influence: "Dane ilościowe wspierają ocenę realizacji"

  - id: SPRINT-RETRO-SXX
    type: informs
    reason: "Metrics są podstawą do retrospective discussions"
    sections:
      - from: "§Delivery, §Quality"
        to: "Sprint Retro §To improve"
        influence: "Niskie metryki wskazują improvement areas"

  - id: SPRINT-PLAN-SXX+1
    type: informs
    reason: "Historical metrics wpływają na planowanie capacity"
    sections:
      - from: "§Delivery §Velocity"
        to: "Next Sprint Plan §3 Capacity"
        influence: "Actual velocity informuje planning następnego sprintu"

  - id: ROADMAP-PROD-001
    type: informs
    reason: "Sprint velocity wpływa na timeline roadmapy"
    sections:
      - from: "§Delivery §Velocity"
        to: "Roadmap §Timeline"
        influence: "Systematic velocity patterns mogą wymagać roadmap adjustment"

  - id: TEAM-PERFORMANCE-*
    type: influences
    reason: "Sprint metrics są częścią team performance analytics"
    sections:
      - from: "§Delivery, §Quality"
        to: "Team Performance §Trends"
        influence: "Agregowane metryki pokazują trends i patterns"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-DOD-SXX
    type: informs
    reason: "DoD compliance jest częścią quality metrics"

  - id: SPRINT-APPROVAL-SXX
    type: complements
    reason: "Metrics wspierają approval decision"

### Satellite Documents
satellites:
  - type: Charts
    path: "satellites/metrics/SPRINT-METRICS-SXX-CHARTS-*.png"
    required: true
    purpose: "Wizualizacje burndown, velocity, quality trends"

  - type: Raw Data
    path: "satellites/metrics/SPRINT-METRICS-SXX-DATA.csv"
    required: false
    purpose: "Surowe dane do analizy i reporting"

  - type: Analysis
    path: "satellites/analysis/SPRINT-METRICS-SXX-ANALYSIS.md"
    required: false
    purpose: "Szczegółowa analiza metryk, anomalies, insights"

# Sprint Metrics — SXX

## Delivery
- Velocity: ...
- Burnup/Burndown: link do plików w `metrics/`

## Quality
- Defects found: ...
- Rework ratio: ...

## Docs / Governance
- Dokumenty zaktualizowane (lista linków)
