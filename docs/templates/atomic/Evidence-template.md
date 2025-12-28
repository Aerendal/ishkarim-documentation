---
id: "EVID-<DOC>-001"
type: "evidence"
title: "Evidence — <DOC>"
owner: "Owner"
related: ["DOC-<id>"]
---

# Evidence

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, TODO-*) generates evidence requirements
- DoD-template defines what evidence is needed
- Compliance/audit requirements specify evidence types

**Impacts:**
- Supports Approval-template decisions (proof for approvers)
- Validates TODO completion and DoD compliance
- Feeds into postmortem-atom (incident evidence)
- Required for release-checklist-atom sign-off

**Related:**
- Other Evidence instances for same parent document
- TODO-template (tasks produce evidence artifacts)
- Approval-template (evidence supports approval decisions)

**Satellites:**
- None (Evidence points to external artifacts)

- **File:** path/to/file.xlsx
- **Description:** what it proves and where used
- **Hash / checksum:** optional
