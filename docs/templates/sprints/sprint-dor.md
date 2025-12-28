---
id: "SPRINT-DOR-SXX"
title: "Sprint Definition of Ready — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Owner"
status: "draft"
version: "0.1"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: DOR-PRD-*
    type: influences
    reason: "DoR produktowy określa bazowe kryteria gotowości wymagań"
    sections:
      - from: "PRD DoR §Requirements Criteria"
        to: "§Kryteria wejścia"
        influence: "Definiuje standardy jakości wymagań"

  - id: DOR-TDD-*
    type: influences
    reason: "DoR techniczny określa gotowość zadań implementacyjnych"
    sections:
      - from: "TDD DoR §Technical Readiness"
        to: "§Kryteria wejścia"
        influence: "Dodaje wymagania techniczne dla zadań"

  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Plan sprintu wymaga zdefiniowania DoR dla zadań"
    sections:
      - from: "Sprint Plan §6 Definicje"
        to: "§Kryteria wejścia"
        influence: "Określa wymagany poziom gotowości zadań"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-BACKLOG-SXX
    type: blocks
    reason: "Zadania nie spełniające DoR nie mogą wejść do backlogu"
    sections:
      - from: "§Kryteria wejścia"
        to: "Sprint Backlog §Items"
        influence: "Filtruje zadania gotowe do wykonania"

  - id: TODO-PRD-*
    type: blocks
    reason: "TODO z PRD musi spełniać DoR przed wejściem do sprintu"
    sections:
      - from: "§Kryteria wejścia"
        to: "PRD TODO §Task Readiness"
        influence: "Określa czy zadanie może być zaplanowane"

  - id: TODO-TDD-*
    type: blocks
    reason: "TODO techniczne musi być ready zgodnie z DoR"
    sections:
      - from: "§Kryteria wejścia"
        to: "TDD TODO §Task Readiness"
        influence: "Weryfikuje gotowość zadań technicznych"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-DOD-SXX
    type: complements
    reason: "DoR (wejście) i DoD (wyjście) wspólnie definiują workflow sprintu"

  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: informs
    reason: "Zmiany scope'u mogą wymagać re-weryfikacji DoR"

### Satellite Documents
satellites:
  - type: Checklist
    path: "satellites/checklists/SPRINT-DOR-SXX-CHECKLIST.md"
    required: true
    purpose: "Checklist do weryfikacji gotowości zadań przed sprintem"

  - type: Evidence
    path: "satellites/evidence/SPRINT-DOR-SXX-*.md"
    required: false
    purpose: "Dowody spełnienia kryteriów DoR dla zadań"

# Sprint DoR — SXX

## Kryteria wejścia dla itemów sprintu
- [ ] Cel i opis zadania jasno zapisane
- [ ] Acceptance Criteria dostępne
- [ ] Estymacja wykonana
- [ ] Owner przypisany
- [ ] Zależności znane i zarejestrowane
- [ ] Dostęp do danych/test env (lub plan)
