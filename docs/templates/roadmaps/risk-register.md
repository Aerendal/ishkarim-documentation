---
id: "RISK-REGISTER-001"
title: "Roadmap Risk Register"
project: "NAZWA_PROJEKTU"
owner: "Head of Product"
version: "0.1"
status: "live"
related: ["ROADMAP-PROD-001"]
---

# Risk Register (roadmap‑level)

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: ROADMAP-PROD-*
    type: requires
    reason: "Product Roadmap identifies strategic risks, dependencies, and blockers"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Roadmap §6 Risks (top items)"
        to: "§1 Risk table"
        influence: "Roadmap high-level risks are detailed in risk register"
      - from: "Roadmap §5 Dependencies & Blockers"
        to: "§1 Risk table"
        influence: "Dependencies and blockers become risk items with mitigation plans"

  - id: CAPACITY-PLAN-*
    type: influences
    reason: "Capacity gaps and constraints are project risks"
    conditions:
      - when: "capacity_plan.has_gaps === true"
        applies: true
    sections:
      - from: "Capacity Plan §4 Gaps & mitigation"
        to: "§1 Risk table"
        influence: "Capacity shortfalls become resource risk items"

  - id: TDD-*
    type: influences
    reason: "Technical design identifies technical risks and dependencies"
    conditions:
      - when: "project.has_tdd === true"
        applies: true
    sections:
      - from: "TDD §7 Risks & Assumptions"
        to: "§1 Risk table"
        influence: "Technical risks (scalability, integration, security) feed into risk register"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: influences
    reason: "Vendor dependencies and SLAs are project risks"
    conditions:
      - when: "project.has_vendor_dependencies === true"
        applies: true
    sections:
      - from: "Vendor Management Plan §5 Vendor Risks"
        to: "§1 Risk table"
        influence: "Vendor delivery failures, SLA breaches become risk items"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Regulatory compliance risks affect roadmap delivery"
    conditions:
      - when: "project.has_compliance_requirements === true"
        applies: true
    sections:
      - from: "Compliance Report §4 Compliance Gaps"
        to: "§1 Risk table"
        influence: "Regulatory approval delays become high-impact risks"

  - id: SECURITY-PLAN-*
    type: influences
    reason: "Security vulnerabilities and threats are project risks"
    conditions:
      - when: "project.has_security_plan === true"
        applies: true
    sections:
      - from: "Security Plan §6 Threat Assessment"
        to: "§1 Risk table"
        influence: "Security threats and vulnerabilities become risk items"
```

### Impacts
```yaml
impacts:
  - id: ROADMAP-PROD-*
    type: influences
    reason: "High-severity risks may force roadmap adjustments or delays"
    conditions:
      - when: "risk.severity === 'High' || risk.severity === 'Critical'"
        applies: true
    sections:
      - from: "§1 Risk table (high severity items)"
        to: "Roadmap §3 Milestones & Releases"
        influence: "Critical risks may delay milestones or reduce scope"
      - from: "§1 Risk table (mitigation plans)"
        to: "Roadmap §5 Dependencies & Blockers"
        influence: "Risk mitigation actions become roadmap dependencies"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Sprint-level risks require sprint-level mitigation"
    conditions:
      - when: "project.uses_agile === true"
        applies: true
    sections:
      - from: "§1 Risk table (active risks)"
        to: "Sprint Core §6 Risks & Blockers"
        influence: "Active risks are monitored and mitigated in sprints"

  - id: INCIDENT-REPORT-*
    type: influences
    reason: "Materialized risks become incidents requiring response"
    conditions:
      - when: "risk.status === 'Materialized'"
        applies: true
    sections:
      - from: "§1 Risk table (materialized risks)"
        to: "Incident Report §2 Incident Description"
        influence: "When risks materialize, they trigger incident reports"

  - id: POSTMORTEM-REPORT-*
    type: influences
    reason: "Materialized risks require postmortem analysis"
    conditions:
      - when: "risk.status === 'Materialized' && risk.impact === 'High'"
        applies: true
    sections:
      - from: "§1 Risk table (high-impact materialized risks)"
        to: "Postmortem §3 Root cause"
        influence: "High-impact risk events trigger postmortem investigations"

  - id: CHANGE-MANAGEMENT-PLAN-*
    type: influences
    reason: "Risk mitigation may require organizational change"
    conditions:
      - when: "risk.mitigation.requires_org_change === true"
        applies: true
    sections:
      - from: "§1 Risk table (mitigation actions)"
        to: "Change Management Plan §3 Change Initiatives"
        influence: "Risk mitigation requiring process changes drive change management"

  - id: BUSINESS-CONTINUITY-PLAN-*
    type: influences
    reason: "High-impact risks require business continuity planning"
    conditions:
      - when: "risk.severity === 'Critical'"
        applies: true
    sections:
      - from: "§1 Risk table (critical risks)"
        to: "BCP §4 Critical Risk Scenarios"
        influence: "Critical risks define BCP scenarios and response plans"
```

### Related
```yaml
related:
  - id: TIMELINE-*
    type: informs
    reason: "Risks may affect project timeline and critical path"

  - id: BUDGET-PLAN-*
    type: informs
    reason: "Risk mitigation may require budget allocation"

  - id: STAKEHOLDER-COMMUNICATION-*
    type: informs
    reason: "High-severity risks require stakeholder communication"

  - id: QUALITY-ASSURANCE-PLAN-*
    type: informs
    reason: "Quality risks inform QA focus areas"

  - id: INTEGRATION-PLAN-*
    type: informs
    reason: "Integration risks affect integration approach and testing"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RISK-REGISTER-*.md"
    required: false
    purpose: "Track risk mitigation actions, risk review meetings, risk owner assignments"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RISK-REGISTER-*.md"
    required: true
    purpose: "Store risk assessments, mitigation plans, risk review notes, incident reports for materialized risks"

  - type: Review
    path: "satellites/reviews/REVIEW-RISK-REGISTER-*.md"
    required: true
    purpose: "Monthly risk register reviews to update status, severity, and mitigation effectiveness"

  - type: DoR
    path: "satellites/dor/DOR-RISK-REGISTER-*.md"
    required: true
    purpose: "Prerequisites: roadmap defined, dependencies identified, risk owners assigned, severity scoring criteria established"
```

| ID | Risk description | Likelihood | Impact | Severity | Owner | Mitigation | Status |
|---|---|---:|---:|---:|---|---|---|
| R‑001 | Regulatory approval delay | Medium | High | High | Legal Lead | Early engagement; contingency plan | Open |
| R‑002 | Vendor integration fails | Low | Medium | Medium | Integration Lead | PoC first; fallback option | Open |

---

Aktualizuj ten plik na bieżąco — każdy wiersz to pojedynczy RAID item.
