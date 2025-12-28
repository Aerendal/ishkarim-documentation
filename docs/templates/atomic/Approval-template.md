---
id: "APPROVAL-<DOC>-001"
type: "approval"
title: "Approval — <DOC> v0.1"
approver: "Name"
date: "YYYY-MM-DD"
related: ["DOC-<id>"]
notes: ""
---

# Approval

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, DESIGN-*) requires approval
- DoD-template or DoR-template compliance (approval criteria)
- Organizational approval workflows and authorities

**Impacts:**
- Unblocks parent document status change (draft → approved)
- Enables progression to next phase (design → implementation)
- May trigger creation of TODO items for approved work
- Gates release process if approvals incomplete

**Related:**
- Other Approval instances for same parent document
- Evidence-template (approvals may reference supporting evidence)
- release-checklist-atom (approvals required before release)

**Satellites:**
- None (Approval is terminal atomic record)

- **Approver:** Name
- **Date:** YYYY-MM-DD
- **Notes:** Short notes
