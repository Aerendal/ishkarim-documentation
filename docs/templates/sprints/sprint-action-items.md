---
id: "SPRINT-AI-SXX"
title: "Action Items — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "live"
related: ["SPRINT-RETRO-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-RETRO-SXX
    type: requires
    reason: "Retro generuje action items z improvement areas"
    sections:
      - from: "Sprint Retro §Action items"
        to: "§Action"
        influence: "To improve przekłada się na konkretne zadania"

  - id: SPRINT-REVIEW-SXX
    type: influences
    reason: "Review może generować followup action items"
    sections:
      - from: "Sprint Review §5 Następne kroki"
        to: "§Action"
        influence: "Decyzje stakeholderów wymagają działań followup"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: influences
    reason: "Nierozwiązane impedimenty generują action items"
    sections:
      - from: "Impediments Log §Impediment (Status=Open)"
        to: "§Action"
        influence: "Blokery wymagają konkretnych kroków rozwiązania"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-PLAN-SXX+1
    type: informs
    reason: "Otwarte action items wpływają na planowanie następnego sprintu"
    sections:
      - from: "§Action (Status=Open)"
        to: "Next Sprint Plan §5 Zależności i ryzyka"
        influence: "Niezrealizowane commitments są ryzykiem dla kolejnego sprintu"

  - id: SPRINT-BACKLOG-SXX+1
    type: influences
    reason: "Action items mogą generować zadania w backlogu"
    sections:
      - from: "§Action (type=technical debt, process)"
        to: "Next Sprint Backlog §Items"
        influence: "Niektóre action items przekładają się na sprint tasks"

  - id: SPRINT-RETRO-SXX+1
    type: informs
    reason: "Status action items jest weryfikowany na następnym retro"
    sections:
      - from: "§Action (Status)"
        to: "Next Sprint Retro §Went well / To improve"
        influence: "Realizacja commitments jest częścią oceny procesu"

  - id: PROCESS-IMPROVEMENT-*
    type: influences
    reason: "Systematyczne action items mogą trigger process changes"
    sections:
      - from: "§Action (recurring)"
        to: "Process Improvement §Initiatives"
        influence: "Powtarzające się problemy wymagają systemowych zmian"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-METRICS-SXX
    type: complements
    reason: "Action items completion rate jest metryką procesu"

  - id: TODO-*
    type: complements
    reason: "Action items mogą być trackowane jako TODO documents"

### Satellite Documents
satellites:
  - type: TODO
    path: "satellites/todos/SPRINT-AI-SXX-TODO-*.md"
    required: false
    purpose: "Szczegółowe rozwinięcie action items na subtasks"

  - type: Evidence
    path: "satellites/evidence/SPRINT-AI-SXX-*.md"
    required: false
    purpose: "Dowody realizacji action items"

# Action Items — SXX

| ID | Action | Owner | Due | Status |
|---|---|---|---|---|
| AI-001 | ... | ... | YYYY-MM-DD | Open |
