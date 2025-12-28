---
id: "DEF-READY-<DOC>-001"
type: "definition"
title: "Definition of Ready — <DOC>"
owner: "Product Owner"
status: "draft"
created: "YYYY-MM-DD"
related: ["DOC-<id>"]
---

# Definition of Ready (DoR)

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, SPRINT-*) defines scope for DoR
- Architectural Design Records may define technical readiness criteria
- Team agreements and process documentation

**Impacts:**
- Gates creation of TODO items from backlog
- Blocks Sprint planning if stories don't meet DoR
- Informs PRD/TDD refinement process
- Prevents premature work on incomplete requirements

**Related:**
- DoD-template (complementary exit criteria)
- TODO-template (tasks must pass DoR before starting)
- Approval-template (DoR compliance may require approval)

**Satellites:**
- None (DoR is atomic definition document)

## Purpose
- Kryteria wejścia przed rozpoczęciem prac

## Criteria (example)
- [ ] Description and business goal
- [ ] Acceptance Criteria (GIVEN/WHEN/THEN)
- [ ] Estimation (story points)
- [ ] Owner available
- [ ] Dependencies listed
- [ ] Test data / mocks available
- [ ] Tech Lead checked feasibility
