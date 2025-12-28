---
id: "DEF-DONE-<DOC>-001"
type: "definition"
title: "Definition of Done — <DOC>"
owner: "Team Lead / QA"
status: "draft"
created: "YYYY-MM-DD"
related: ["DOC-<id>"]
---

# Definition of Done (DoD)

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, SPRINT-*) defines scope for DoD
- Quality standards and compliance requirements
- Team engineering practices and conventions

**Impacts:**
- Gates closure of TODO items and user stories
- Blocks Sprint completion if DoD not met
- Prevents PRD/TDD status change to "delivered"
- Informs release-checklist criteria

**Related:**
- DoR-template (complementary entry criteria)
- TODO-template (tasks completed according to DoD)
- release-checklist-atom (DoD items feed into release checks)

**Satellites:**
- Evidence-template (proof that DoD criteria are met)
- Approval-template (DoD compliance sign-off)

## Purpose
- Kryteria uznania pracy za zakończoną

## Criteria (example)
- [ ] Code merged to main/release branch
- [ ] Unit and integration tests green
- [ ] E2E / UAT (if required) passed
- [ ] Documentation updated (API, runbook)
- [ ] Build artifact published / staging smoke tests passed
- [ ] Security checks / linters passed
- [ ] Owner approval / sign-off
