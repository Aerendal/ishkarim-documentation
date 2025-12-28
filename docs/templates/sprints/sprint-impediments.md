---
id: "SPRINT-IMP-SXX"
title: "Impediments Log — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "live"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-BACKLOG-SXX
    type: influences
    reason: "Zablokowane zadania w backlogu generują impedimenty"
    sections:
      - from: "Sprint Backlog §Items (Status=blocked)"
        to: "§Impediment"
        influence: "Zadania zablokowane trafiają do logu impedimentów"

  - id: SPRINT-PLAN-SXX
    type: influences
    reason: "Zidentyfikowane ryzyka w planie mogą się zmaterializować jako impedimenty"
    sections:
      - from: "Sprint Plan §5 Zależności i ryzyka"
        to: "§Impediment"
        influence: "Ryzyka mogą przekształcić się w blokery"

  - id: RISK-*
    type: influences
    reason: "Zewnętrzne ryzyka projektowe mogą wpływać na sprint"
    sections:
      - from: "Risk Register §Active Risks"
        to: "§Impediment"
        influence: "Ryzyka projektowe mogą blokować zadania sprintu"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-REVIEW-SXX
    type: informs
    reason: "Impedimenty wyjaśniają niewykonane zadania w review"
    sections:
      - from: "§Impediment (Impact=High)"
        to: "Sprint Review §3 Not delivered / carry-over"
        influence: "Impedimenty są kluczowym kontekstem dla niedostarczonych itemów"

  - id: SPRINT-RETRO-SXX
    type: informs
    reason: "Impedimenty są omawiane na retro jako obszar do poprawy"
    sections:
      - from: "§Impediment"
        to: "Sprint Retro §To improve"
        influence: "Powtarzające się blokery wymagają action items"

  - id: SPRINT-ACTION-ITEMS-SXX
    type: influences
    reason: "Impedimenty generują action items do rozwiązania"
    sections:
      - from: "§Impediment (Status=Open)"
        to: "Action Items §Action"
        influence: "Nierozwiązane impedimenty wymagają konkretnych działań"

  - id: SPRINT-METRICS-SXX
    type: informs
    reason: "Liczba i wpływ impedimentów są ważnymi metrykami"
    sections:
      - from: "§Impediment (Impact, Status)"
        to: "Sprint Metrics §Delivery"
        influence: "Impedimenty wpływają na velocity i realizację"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: complements
    reason: "Impedimenty mogą wymuszać zmiany scope'u sprintu"

  - id: ADR-*
    type: informs
    reason: "Niektóre impedimenty mogą wymagać decyzji architektonicznych"

### Satellite Documents
satellites:
  - type: TODO
    path: "satellites/todos/SPRINT-IMP-SXX-TODO-*.md"
    required: false
    purpose: "Zadania związane z rozwiązywaniem impedimentów"

  - type: Evidence
    path: "satellites/evidence/SPRINT-IMP-SXX-*.md"
    required: false
    purpose: "Dowody impedimentów (logi, screeny, komunikacja)"

# Impediments Log — SXX

| ID | Impediment | Since | Owner | Impact | Status | Next step |
|---|---|---|---|---|---|---|
| IMP-001 | ... | YYYY-MM-DD | ... | High | Open | ... |
