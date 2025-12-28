---
id: "REL-ATOM-001"
type: "checklist"
title: "Release Checklist — atom"
related: ["REL-CHECK-001"]
---

# Release checklist (atom)

## Document Cross-References

**Dependencies:**
- Parent release document (REL-CHECK-*) defines release scope
- DoD-template criteria rolled up to release level
- PRD/TDD completion status (all features delivered)
- Infrastructure and deployment requirements

**Impacts:**
- Blocks release deployment if checklist incomplete
- Gates production rollout (go/no-go decision)
- Triggers creation of postmortem-atom if issues found
- Informs stakeholders of release readiness

**Related:**
- DoD-template (release checklist aggregates DoD criteria)
- Approval-template (release sign-offs)
- risk-item-template (open risks evaluated before release)

**Satellites:**
- Evidence-template (test results, deployment artifacts)
- Approval-template (release approvals)
- postmortem-atom (if release issues occur)

- [ ] Smoke tests passed
- [ ] Monitoring configured
- [ ] Rollback verified
