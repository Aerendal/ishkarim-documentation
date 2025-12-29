---
id: "TODO-<DOC>-001"
type: "todo"
title: "<Short title>"
owner: "<Name / Team>"
status: "todo"
priority: "P1"
created: "YYYY-MM-DD"
due: "YYYY-MM-DD"
related: ["DOC-<id>"]
acceptance_criteria: []

# === Living Documentation Framework (PROPOZYCJA-2) ===
# Lifecycle tracking for TODO items
todo_lifecycle:
  created_from_doc: "DOC-<id>"
  created_from_version: "X.Y.Z"
  triggered_by_change: "Description of what triggered this TODO (e.g., PRD version bump, new section added)"
  completed_for_doc_version: null  # Will be filled when TODO is done
  status_history:
    - status: "todo"
      date: "YYYY-MM-DD"
      reason: "Created from parent document change"

# Impact propagation tracking
impact_tracking:
  blocks_documents: []  # List of doc IDs that are blocked until this TODO is completed
  notified_stakeholders:
    - stakeholder: "<Name/Team>"
      notified_date: "YYYY-MM-DD"
      acknowledged: false
---

# TODO: <Short title>

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, SPRINT-*, etc.) creates TODO instances
- DoR-template (task must meet DoR criteria before starting)
- Sprint-plan may generate TODO items from backlog

**Impacts:**
- Informs parent document about task progress and completion
- Task completion may trigger updates in PRD/TDD status sections
- Blocked TODOs may delay Sprint goals or Release timeline

**Related:**
- DoD-template (task closure follows DoD criteria)
- Other TODO items in same parent document
- risk-item-template (if task has identified risks)

**Satellites:**
- Evidence-template (artifacts/proofs of completion)
- Approval-template (if task requires sign-off)

## Description
- Krótki opis zadania

## Checklist
- [ ] Krok 1
- [ ] Krok 2

## Notes / Links
- Link do źródeł
