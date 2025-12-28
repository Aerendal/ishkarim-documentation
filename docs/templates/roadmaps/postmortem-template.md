---
id: "POST-001"
title: "Postmortem — Release 1"
project: "NAZWA_PROJEKTU"
owner: "Incident Lead"
version: "0.1"
status: "draft"
related: ["REL-CHECK-001","ROADMAP-PROD-001"]
---

# Postmortem — Release 1

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: RELEASE-CHECKLIST-*
    type: requires
    reason: "Release checklist provides context on what was supposed to happen vs what actually happened"
    conditions:
      - when: "postmortem.trigger === 'release_incident'"
        applies: true
    sections:
      - from: "Release Checklist §3 Release window"
        to: "§2 Timeline"
        influence: "Release checklist items map to postmortem timeline events"
      - from: "Release Checklist §4 Post-release"
        to: "§1 Summary"
        influence: "Checklist completion status informs postmortem scope"

  - id: INCIDENT-REPORT-*
    type: requires
    reason: "Incident report provides initial incident details and impact assessment"
    conditions:
      - when: "postmortem.trigger === 'production_incident'"
        applies: true
    sections:
      - from: "Incident Report §2 Incident Description"
        to: "§1 Summary"
        influence: "Incident description becomes postmortem summary"
      - from: "Incident Report §3 Impact Assessment"
        to: "§2 Impact"
        influence: "Incident impact metrics feed into postmortem impact section"
      - from: "Incident Report §4 Timeline"
        to: "§3 Timeline"
        influence: "Incident timeline becomes postmortem timeline baseline"

  - id: MONITORING-PLAN-*
    type: influences
    reason: "Monitoring alerts and metrics provide incident detection timeline"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "Monitoring Plan §4 Alert History"
        to: "§3 Timeline"
        influence: "Alert timestamps establish incident detection timeline"

  - id: RUNBOOK-*
    type: influences
    reason: "Runbook procedures inform incident response effectiveness"
    conditions:
      - when: "project.has_runbook === true"
        applies: true
    sections:
      - from: "Runbook §4 Troubleshooting Procedures"
        to: "§5 Remediation & Actions"
        influence: "Runbook gaps identified during incident become action items"

  - id: RISK-REGISTER-*
    type: influences
    reason: "Materialized risks from risk register become postmortem subjects"
    conditions:
      - when: "incident.was_known_risk === true"
        applies: true
    sections:
      - from: "Risk Register §1 Risk table (materialized risks)"
        to: "§4 Root cause"
        influence: "Known risks that materialized inform root cause analysis"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Deployment issues require deployment guide review"
    conditions:
      - when: "incident.type === 'deployment_failure'"
        applies: true
    sections:
      - from: "Deployment Guide §6 Rollback Procedures"
        to: "§3 Timeline"
        influence: "Rollback execution timeline feeds into postmortem"
```

### Impacts
```yaml
impacts:
  - id: RISK-REGISTER-*
    type: blocks
    reason: "Postmortem identifies new risks requiring risk register updates"
    conditions:
      - when: "postmortem.identifies_new_risks === true"
        applies: true
    sections:
      - from: "§7 Lessons learned"
        to: "Risk Register §1 Risk table"
        influence: "Lessons learned become new risk items with mitigation plans"

  - id: RUNBOOK-*
    type: blocks
    reason: "Postmortem action items require runbook updates"
    conditions:
      - when: "postmortem.has_runbook_gaps === true"
        applies: true
    sections:
      - from: "§5 Remediation & Actions"
        to: "Runbook §4 Troubleshooting Procedures"
        influence: "Incident response gaps drive runbook procedure additions"

  - id: MONITORING-PLAN-*
    type: blocks
    reason: "Postmortem may identify monitoring gaps requiring new alerts"
    conditions:
      - when: "postmortem.has_monitoring_gaps === true"
        applies: true
    sections:
      - from: "§5 Remediation & Actions (monitoring improvements)"
        to: "Monitoring Plan §3 Alert Thresholds"
        influence: "Incident detection gaps drive new monitoring alerts"

  - id: TEST-PLAN-*
    type: influences
    reason: "Postmortem identifies test coverage gaps"
    conditions:
      - when: "incident.escaped_testing === true"
        applies: true
    sections:
      - from: "§4 Root cause (testing gaps)"
        to: "Test Plan §3 Test Scenarios"
        influence: "Incidents that escaped testing drive new test scenarios"

  - id: RELEASE-PLAN-*
    type: influences
    reason: "Postmortem findings improve release process"
    conditions:
      - when: "incident.type === 'release_related'"
        applies: true
    sections:
      - from: "§7 Lessons learned"
        to: "Release Plan §7 Process Improvements"
        influence: "Release postmortems drive release process improvements"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Deployment failures require deployment guide updates"
    conditions:
      - when: "incident.type === 'deployment_failure'"
        applies: true
    sections:
      - from: "§5 Remediation & Actions (deployment improvements)"
        to: "Deployment Guide §7 Best Practices"
        influence: "Deployment issues drive deployment guide improvements"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "Postmortem may identify training gaps"
    conditions:
      - when: "postmortem.identifies_skills_gaps === true"
        applies: true
    sections:
      - from: "§7 Lessons learned (skills gaps)"
        to: "Training Materials §3 Training Modules"
        influence: "Identified skills gaps drive new training materials"

  - id: CHANGE-MANAGEMENT-PLAN-*
    type: influences
    reason: "Postmortem action items may require process changes"
    conditions:
      - when: "postmortem.requires_process_change === true"
        applies: true
    sections:
      - from: "§5 Remediation & Actions (process changes)"
        to: "Change Management Plan §3 Change Initiatives"
        influence: "Process improvement actions drive change management initiatives"

  - id: KNOWLEDGE-BASE-*
    type: blocks
    reason: "Postmortem lessons are documented in knowledge base"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§7 Lessons learned"
        to: "Knowledge Base §4 Incident Archive"
        influence: "Postmortem lessons become searchable knowledge base articles"
```

### Related
```yaml
related:
  - id: ROADMAP-PROD-*
    type: informs
    reason: "Major incidents may affect roadmap timeline and priorities"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Compliance-related incidents require compliance reporting"

  - id: STAKEHOLDER-COMMUNICATION-*
    type: informs
    reason: "Major incidents require stakeholder communication"

  - id: SLA-*
    type: informs
    reason: "Incidents affecting SLA require SLA review"

  - id: CAPACITY-PLAN-*
    type: informs
    reason: "Remediation actions may require additional capacity"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-POST-*.md"
    required: true
    purpose: "Track remediation action items, follow-up tasks, process improvement implementations"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-POST-*.md"
    required: true
    purpose: "Store logs, screenshots, monitoring graphs, incident timeline documentation, chat transcripts"

  - type: Review
    path: "satellites/reviews/REVIEW-POST-*.md"
    required: true
    purpose: "Postmortem review meeting notes, stakeholder feedback, action item status reviews"

  - type: DoR
    path: "satellites/dor/DOR-POST-*.md"
    required: true
    purpose: "Prerequisites: incident resolved, timeline reconstructed, stakeholders identified, evidence collected"
```

## Summary
- What happened (brief):

## Impact
- Users affected, metrics, outage duration

## Timeline
- YYYY‑MM‑DD HH:MM — Event
- YYYY‑MM‑DD HH:MM — Event

## Root cause
- Summary of root cause

## Remediation & Actions
- Action 1 — owner — due date
- Action 2 — owner — due date

## Lessons learned
- Bullet points

## Follow‑ups
- Tracking in TODOs / issue tracker
