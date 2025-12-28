---
id: "RISK-<DOC>-001"
type: "risk"
title: "Risk item"
owners: ["Name"]
likelihood: "Low|Medium|High"
impact: "Low|Medium|High"
status: "open|mitigating|closed"
related: ["DOC-<id>"]
---

# Risk item

## Document Cross-References

**Dependencies:**
- Parent document (PRD-*, TDD-*, SPRINT-*) identifies risks
- Risk assessment frameworks and organizational policies
- Architectural Design Records may identify technical risks

**Impacts:**
- High-priority risks may block PRD/TDD approval
- May trigger creation of TODO items for mitigation
- Informs Sprint planning and capacity allocation
- Affects release-checklist decisions (go/no-go)

**Related:**
- Other risk-item instances in same parent document
- TODO-template (mitigation tasks)
- postmortem-atom (realized risks become incidents)

**Satellites:**
- TODO-template (mitigation action items)
- Evidence-template (risk assessment artifacts)

- Description: ...
- Mitigation: ...
- Owner: ...
