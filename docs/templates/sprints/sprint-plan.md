---
id: "SPRINT-PLAN-SXX"
title: "Sprint Plan — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master / Delivery Lead"
status: "draft"          # draft|in-review|approved|closed
version: "0.1"
date_created: "YYYY-MM-DD"
period: "YYYY-MM-DD..YYYY-MM-DD"
sprint_goal: ""
related: ["ROADMAP-PROD-001","REL-CHECK-001"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: ROADMAP-PROD-001
    type: requires
    reason: "Sprint realizuje elementy z roadmapy produktowej"
    sections:
      - from: "Roadmap §Milestones"
        to: "§2 Zakres (Scope)"
        influence: "Określa priorytety i cel sprintu"

  - id: SPRINT-PLAN-SXX-1
    type: influences
    reason: "Poprzedni sprint dostarcza kontekstu i carry-over items"
    sections:
      - from: "Previous Sprint §Not delivered"
        to: "§4 Backlog wybrany do sprintu"
        influence: "Niedokończone zadania trafiają do planowania"

  - id: PRD-*
    type: requires
    reason: "Wymagania produktowe definiują zakres funkcjonalności"
    sections:
      - from: "PRD §Features"
        to: "§2 Zakres (Scope)"
        influence: "Określa co ma być zaimplementowane"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-BACKLOG-SXX
    type: blocks
    reason: "Sprint Backlog nie może powstać bez zatwierdzonego planu"
    sections:
      - from: "§4 Backlog wybrany do sprintu"
        to: "Sprint Backlog §Items"
        influence: "Definiuje zadania do wykonania"

  - id: SPRINT-DOR-SXX
    type: requires
    reason: "Plan wymaga zdefiniowania kryteriów gotowości zadań"
    sections:
      - from: "§6 Definicje"
        to: "Sprint DoR §Kryteria"
        influence: "Określa wymagania dla zadań wchodzących do sprintu"

  - id: SPRINT-DOD-SXX
    type: requires
    reason: "Plan wymaga zdefiniowania kryteriów zakończenia sprintu"
    sections:
      - from: "§6 Definicje"
        to: "Sprint DoD §Kryteria"
        influence: "Określa warunki zamknięcia sprintu"

  - id: SPRINT-REVIEW-SXX
    type: informs
    reason: "Review weryfikuje realizację planu sprintu"
    sections:
      - from: "§1 Sprint Goal"
        to: "Sprint Review §1 Sprint Goal — status"
        influence: "Cel sprintu jest weryfikowany w review"

### Related Documents (Powiązane dokumenty)
related:
  - id: REL-CHECK-001
    type: informs
    reason: "Checklist wydania określa wymagania dla dostarczanych funkcji"

  - id: SPRINT-METRICS-SXX
    type: complements
    reason: "Metryki śledzą postęp realizacji planu"

  - id: SPRINT-IMPEDIMENTS-SXX
    type: informs
    reason: "Impedimenty mogą wpływać na realizację planu"

### Satellite Documents
satellites:
  - type: TODO
    path: "satellites/todos/SPRINT-PLAN-SXX-TODO-*.md"
    required: false
    purpose: "Zadania związane z przygotowaniem planu sprintu"

  - type: DoR
    path: "satellites/dor/SPRINT-DOR-SXX.md"
    required: true
    purpose: "Kryteria gotowości dla zadań sprintu"

  - type: DoD
    path: "satellites/dod/SPRINT-DOD-SXX.md"
    required: true
    purpose: "Kryteria zakończenia sprintu"

  - type: Approval
    path: "satellites/approvals/SPRINT-APPROVAL-SXX.md"
    required: true
    purpose: "Formalne zatwierdzenie i sign-off sprintu"

# Sprint Plan — SXX

## 1. Sprint Goal
- Jedno zdanie: co ma zostać osiągnięte i dlaczego.

## 2. Zakres (Scope)
- In scope:
  - ...
- Out of scope:
  - ...

## 3. Capacity / dostępność
- Zespół i dostępność (FTE, urlopy, ograniczenia).

## 4. Backlog wybrany do sprintu
- Patrz: `sprint-backlog.md`

## 5. Zależności i ryzyka (top 3)
- D1: ...
- R1: ...

## 6. Definicje
- DoR sprint: `sprint-dor.md`
- DoD sprint: `sprint-dod.md`

## 7. Checkpointy
- Mid-sprint check (YYYY-MM-DD)
- Review (YYYY-MM-DD)
- Retro (YYYY-MM-DD)

## 8. Komunikacja
- Kto dostaje update i kiedy (np. weekly stakeholder update).
