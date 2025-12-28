---
id: "SPRINT-DOD-SXX"
title: "Sprint Definition of Done — SXX"
project: "NAZWA_PROJEKTU"
owner: "Team Lead / QA"
status: "draft"
version: "0.1"
related: ["SPRINT-PLAN-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: DOD-PRD-*
    type: influences
    reason: "DoD produktowy określa kryteria akceptacji funkcjonalności"
    sections:
      - from: "PRD DoD §Acceptance Criteria"
        to: "§Kryteria wyjścia"
        influence: "Definiuje standardy jakości dostarczanych funkcji"

  - id: DOD-TDD-*
    type: influences
    reason: "DoD techniczny określa wymagania implementacyjne"
    sections:
      - from: "TDD DoD §Implementation Standards"
        to: "§Kryteria wyjścia"
        influence: "Dodaje wymagania techniczne dla zamknięcia"

  - id: SPRINT-PLAN-SXX
    type: requires
    reason: "Plan sprintu wymaga zdefiniowania kryteriów zakończenia"
    sections:
      - from: "Sprint Plan §6 Definicje"
        to: "§Kryteria wyjścia"
        influence: "Określa warunki sukcesu sprintu"

  - id: REL-CHECK-001
    type: influences
    reason: "Release checklist może wpływać na kryteria DoD"
    sections:
      - from: "Release Checklist §Quality Gates"
        to: "§Kryteria wyjścia"
        influence: "Dodaje wymagania dla release-ready features"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-REVIEW-SXX
    type: blocks
    reason: "Review nie może zatwierdzić sprintu bez spełnienia DoD"
    sections:
      - from: "§Kryteria wyjścia"
        to: "Sprint Review §1 Sprint Goal — status"
        influence: "Określa czy sprint goal został osiągnięty"

  - id: SPRINT-APPROVAL-SXX
    type: blocks
    reason: "Sign-off wymaga potwierdzenia spełnienia DoD"
    sections:
      - from: "§Kryteria wyjścia"
        to: "Sprint Approval §Notes"
        influence: "DoD musi być spełniony przed approval"

  - id: SPRINT-METRICS-SXX
    type: informs
    reason: "Metryki uwzględniają stopień spełnienia DoD"
    sections:
      - from: "§Kryteria wyjścia"
        to: "Sprint Metrics §Quality"
        influence: "DoD wpływa na metryki jakości"

### Related Documents (Powiązane dokumenty)
related:
  - id: SPRINT-DOR-SXX
    type: complements
    reason: "DoD (wyjście) i DoR (wejście) wspólnie definiują workflow sprintu"

  - id: SPRINT-RETRO-SXX
    type: informs
    reason: "Retro może identyfikować problemy z realizacją DoD"

### Satellite Documents
satellites:
  - type: Checklist
    path: "satellites/checklists/SPRINT-DOD-SXX-CHECKLIST.md"
    required: true
    purpose: "Checklist weryfikacji kryteriów zakończenia sprintu"

  - type: Evidence
    path: "satellites/evidence/SPRINT-DOD-SXX-*.md"
    required: true
    purpose: "Dowody spełnienia DoD (testy, dokumentacja, review)"

  - type: Approval
    path: "satellites/approvals/SPRINT-APPROVAL-SXX.md"
    required: true
    purpose: "Formalne potwierdzenie spełnienia DoD i zamknięcia sprintu"

# Sprint DoD — SXX

## Kryteria wyjścia (zamknięcia sprintu)
- [ ] Wszystkie P0/P1 itemy domknięte lub świadomie odłożone (z CR)
- [ ] Review przeprowadzone, wyniki zapisane
- [ ] Retro przeprowadzone, action items zapisane
- [ ] Dokumentacja (jeśli dotyczy) zaktualizowana i zmergowana
- [ ] Approval / sign-off (jeśli wymagane)
