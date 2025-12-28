---
id: "SPRINT-REVIEW-SXX"
title: "Sprint Review — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "draft"
related: ["SPRINT-PLAN-SXX","SPRINT-BACKLOG-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Review weryfikuje realizację celu i planu sprintu"
    sections:
      - from: "Sprint Plan §1 Sprint Goal"
        to: "§1 Sprint Goal — status"
        influence: "Cel sprintu jest głównym kryterium oceny"

  - id: SPRINT-BACKLOG-SXX
    type: requires
    reason: "Review podsumowuje wykonanie zadań z backlogu"
    sections:
      - from: "Sprint Backlog §Items (Status)"
        to: "§2 Delivered i §3 Not delivered"
        influence: "Status zadań określa deliverables i carry-over"

  - id: SPRINT-DOD-SXX
    type: requires
    reason: "Review weryfikuje spełnienie Definition of Done"
    sections:
      - from: "Sprint DoD §Kryteria wyjścia"
        to: "§1 Sprint Goal — status"
        influence: "DoD określa czy sprint można uznać za zakończony"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Impedimenty wyjaśniają context niedostarczonych zadań"
    sections:
      - from: "Impediments Log §Impediment"
        to: "§3 Not delivered / carry-over"
        influence: "Blokery są kluczowym kontekstem dla opóźnień"

  - id: SPRINT-METRICS-SXX
    type: influences
    reason: "Metryki dostarczają danych do oceny sprintu"
    sections:
      - from: "Sprint Metrics §Delivery"
        to: "§2 Delivered"
        influence: "Velocity i burndown wspierają ocenę realizacji"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-RETRO-SXX
    type: informs
    reason: "Review dostarcza kontekstu dla retrospektywy"
    sections:
      - from: "§4 Feedback / decyzje"
        to: "Sprint Retro §Went well / To improve"
        influence: "Wyniki review są punktem wyjścia dla retro"

  - id: SPRINT-ACTION-ITEMS-SXX
    type: influences
    reason: "Review może generować action items"
    sections:
      - from: "§5 Następne kroki"
        to: "Action Items §Action"
        influence: "Decyzje stakeholderów wymagają followup"

  - id: SPRINT-APPROVAL-SXX
    type: blocks
    reason: "Approval nie może być wydany bez pozytywnego review"
    sections:
      - from: "§1 Sprint Goal — status (tak)"
        to: "Sprint Approval §Approved by"
        influence: "Pozytywny review jest warunkiem approval"

  - id: SPRINT-PLAN-SXX+1
    type: informs
    reason: "Review wpływa na planowanie następnego sprintu"
    sections:
      - from: "§3 Not delivered / carry-over"
        to: "Next Sprint Plan §4 Backlog"
        influence: "Carry-over items trafiają do następnego sprintu"

  - id: ROADMAP-PROD-001
    type: informs
    reason: "Review może wpływać na aktualizację roadmapy"
    sections:
      - from: "§4 Feedback / decyzje"
        to: "Roadmap §Adjustments"
        influence: "Feedback stakeholderów może zmienić priorytety roadmapy"

### Related Documents (Powiązane dokumenty)
related:
  - id: PRD-*
    type: complements
    reason: "Review weryfikuje realizację wymagań z PRD"

  - id: REL-CHECK-001
    type: informs
    reason: "Review może trigger release process"

### Satellite Documents
satellites:
  - type: Evidence
    path: "satellites/evidence/SPRINT-REVIEW-SXX-*.md"
    required: true
    purpose: "Dowody dostarczonych funkcji (demo, screeny, release notes)"

  - type: Notes
    path: "satellites/notes/SPRINT-REVIEW-SXX-NOTES.md"
    required: false
    purpose: "Notatki ze spotkania review, feedback stakeholderów"

# Sprint Review — SXX

## 1. Sprint Goal — status
- Czy cel został osiągnięty? (tak/nie + komentarz)

## 2. Delivered
- Lista dowiezionych elementów (linki do PR, dokumentów, release notes)

## 3. Not delivered / carry-over
- Co nie weszło i dlaczego

## 4. Feedback / decyzje
- Ustalenia i decyzje stakeholderów

## 5. Następne kroki
- Link do action items
