---
id: "SPRINT-APPROVAL-SXX"
title: "Sprint Sign-off — SXX"
project: "NAZWA_PROJEKTU"
approver: "Product Owner / Sponsor"
date: "YYYY-MM-DD"
related: ["SPRINT-REVIEW-SXX","SPRINT-RETRO-SXX"]
---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
dependencies:
  - id: SPRINT-REVIEW-SXX
    type: requires
    reason: "Review musi potwierdzić realizację przed approval"
    sections:
      - from: "Sprint Review §1 Sprint Goal — status"
        to: "§Notes"
        influence: "Pozytywny review jest warunkiem approval"

  - id: SPRINT-RETRO-SXX
    type: requires
    reason: "Retro musi być przeprowadzone przed zamknięciem sprintu"
    sections:
      - from: "Sprint Retro §Action items"
        to: "§Notes"
        influence: "Commitments zespołu są częścią approval"

  - id: SPRINT-DOD-SXX
    type: requires
    reason: "DoD musi być spełniony przed approval"
    sections:
      - from: "Sprint DoD §Kryteria wyjścia"
        to: "§Notes"
        influence: "Weryfikacja spełnienia wszystkich kryteriów zakończenia"

  - id: SPRINT-METRICS-SXX
    type: influences
    reason: "Metrics wspierają decision making dla approval"
    sections:
      - from: "Sprint Metrics §Delivery, §Quality"
        to: "§Notes"
        influence: "Dane ilościowe potwierdzają realizację"

  - id: SPRINT-ACTION-ITEMS-SXX
    type: influences
    reason: "Status action items wpływa na approval decision"
    sections:
      - from: "Action Items §Action (Status)"
        to: "§Notes"
        influence: "Open critical action items mogą blokować approval"

### Impacts (Co ten dokument popycha do przodu)
impacts:
  - id: SPRINT-PLAN-SXX+1
    type: informs
    reason: "Approval zamyka sprint i otwiera planowanie następnego"
    sections:
      - from: "§Approved by"
        to: "Next Sprint Plan §Reference"
        influence: "Formalnie kończy poprzedni sprint cycle"

  - id: ROADMAP-PROD-001
    type: informs
    reason: "Sprint approval potwierdza progress względem roadmapy"
    sections:
      - from: "§Date"
        to: "Roadmap §Milestones"
        influence: "Aktualizuje status milestones"

  - id: PROJECT-STATUS-*
    type: influences
    reason: "Sprint approval wpływa na overall project status"
    sections:
      - from: "§Approved by, §Notes"
        to: "Project Status §Sprint Summary"
        influence: "Sprint closure jest częścią project reporting"

  - id: RELEASE-*
    type: influences
    reason: "Approved sprint może trigger release process"
    sections:
      - from: "§Approved by"
        to: "Release §Go/No-Go"
        influence: "Sprint approval może być warunkiem release"

### Related Documents (Powiązane dokumenty)
related:
  - id: REL-CHECK-001
    type: complements
    reason: "Release checklist może być częścią sprint approval"

  - id: SPRINT-SCOPE-CHANGE-SXX-*
    type: informs
    reason: "Approved scope changes są częścią kontekstu approval"

### Satellite Documents
satellites:
  - type: Evidence
    path: "satellites/evidence/SPRINT-APPROVAL-SXX-*.md"
    required: true
    purpose: "Dowody spełnienia DoD (test results, documentation, review notes)"

  - type: Sign-off Sheet
    path: "satellites/approvals/SPRINT-APPROVAL-SXX-SIGNOFF.pdf"
    required: false
    purpose: "Formalne dokumenty podpisane przez stakeholderów"

  - type: Closure Report
    path: "satellites/reports/SPRINT-APPROVAL-SXX-CLOSURE.md"
    required: false
    purpose: "Podsumowanie sprintu dla stakeholderów i project archive"

# Sprint Sign-off — SXX

- **Approved by:** ...
- **Date:** ...
- **Notes:** ...
