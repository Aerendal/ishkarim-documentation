---
id: "SPRINT-RETRO-SXX"
title: "Sprint Retrospective — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "draft"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-REVIEW-SXX
    type: requires
    reason: "Retro analizuje wyniki i feedback z review"
    sections:
      - from: "Sprint Review §1 Sprint Goal — status"
        to: "§Went well / To improve"
        influence: "Realizacja celu jest kluczowym tematem retro"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Impedimenty są głównym źródłem improvement areas"
    sections:
      - from: "Impediments Log §Impediment"
        to: "§To improve"
        influence: "Blokery wymagają analizy i działań naprawczych"

  - id: SPRINT-METRICS-SXX
    type: influences
    reason: "Metryki dostarczają danych do retrospektywy"
    sections:
      - from: "Sprint Metrics §Delivery, §Quality"
        to: "§Went well / To improve"
        influence: "Dane ilościowe wspierają dyskusję o procesie"

  - id: SPRINT-ACTION-ITEMS-SXX-1
    type: influences
    reason: "Review action items z poprzedniego sprintu"
    sections:
      - from: "Previous Sprint Action Items §Status"
        to: "§Went well / To improve"
        influence: "Weryfikacja realizacji poprzednich commitments"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-ACTION-ITEMS-SXX
    type: blocks
    reason: "Retro generuje action items do wykonania"
    sections:
      - from: "§Action items"
        to: "Action Items §Action"
        influence: "Improvement areas przekładają się na konkretne zadania"

  - id: SPRINT-APPROVAL-SXX
    type: informs
    reason: "Retro jest częścią ceremonii zamknięcia sprintu"
    sections:
      - from: "§Action items"
        to: "Sprint Approval §Notes"
        influence: "Commitments zespołu są zapisane w approval"

  - id: SPRINT-PLAN-SXX+1
    type: informs
    reason: "Retro wpływa na planowanie następnego sprintu"
    sections:
      - from: "§To improve"
        to: "Next Sprint Plan §5 Zależności i ryzyka"
        influence: "Zidentyfikowane problemy są uwzględniane w planning"

  - id: PROCESS-IMPROVEMENT-*
    type: influences
    reason: "Systematyczne problemy wymagają zmian procesowych"
    sections:
      - from: "§To improve (recurring)"
        to: "Process Improvement §Initiatives"
        influence: "Powtarzające się problemy trigger improvement initiatives"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: informs
    reason: "Zmiany scope'u mogą być tematem retro"

  - id: TEAM-HEALTH-*
    type: complements
    reason: "Retro może wpływać na health metrics zespołu"

### Satellite Documents
satellites:
  - type: Notes
    path: "satellites/notes/SPRINT-RETRO-SXX-NOTES.md"
    required: false
    purpose: "Szczegółowe notatki z retrospektywy, anonimowy feedback"

  - type: TODO
    path: "satellites/todos/SPRINT-RETRO-SXX-TODO-*.md"
    required: false
    purpose: "Zadania związane z przygotowaniem i facilitacją retro"

# Sprint Retrospective — SXX

## Went well
- ...

## To improve
- ...

## Action items
- AI-001 — owner — due
- AI-002 — owner — due
