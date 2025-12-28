---
id: "REL-CHECK-001"
title: "Release Checklist — Release 1"
project: "NAZWA_PROJEKTU"
owner: "Release Manager"
version: "0.1"
status: "draft"
related: ["ROADMAP-PROD-001"]
---

# Release Checklist — Release 1

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: ROADMAP-PROD-*
    type: requires
    reason: "Product Roadmap defines release milestones, scope, and quality gates"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Roadmap §3 Milestones & Releases"
        to: "§1 Pre-freeze"
        influence: "Roadmap release scope defines what must be frozen"
      - from: "Roadmap §9 Checkpoints & Gates"
        to: "§2 Pre-release"
        influence: "Roadmap quality gates become release checklist items"

  - id: RELEASE-PLAN-*
    type: requires
    reason: "Release Plan defines detailed release process and timeline"
    conditions:
      - when: "project.has_release_plan === true"
        applies: true
    sections:
      - from: "Release Plan §3 Release Process"
        to: "§3 Release window"
        influence: "Release process steps become checklist items"
      - from: "Release Plan §4 Rollback Plan"
        to: "§2 Pre-release"
        influence: "Rollback readiness checks are included in pre-release checklist"

  - id: TEST-PLAN-*
    type: requires
    reason: "Test Plan defines testing criteria for release readiness"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Test Plan §5 Test Exit Criteria"
        to: "§2 Pre-release"
        influence: "Test exit criteria become release checklist validation items"

  - id: DEPLOYMENT-GUIDE-*
    type: requires
    reason: "Deployment Guide defines deployment steps and verification"
    conditions:
      - when: "project.has_deployment_guide === true"
        applies: true
    sections:
      - from: "Deployment Guide §3 Deployment Steps"
        to: "§3 Release window"
        influence: "Deployment steps become release window checklist items"
      - from: "Deployment Guide §5 Smoke Tests"
        to: "§3 Release window"
        influence: "Smoke tests verify successful deployment"

  - id: RUNBOOK-*
    type: requires
    reason: "Runbook must be updated before release for operations support"
    conditions:
      - when: "project.has_runbook === true"
        applies: true
    sections:
      - from: "Runbook §4 Troubleshooting Procedures"
        to: "§2 Pre-release"
        influence: "Runbook updates are verified in pre-release checklist"

  - id: SECURITY-PLAN-*
    type: influences
    reason: "Security scans are required before release"
    conditions:
      - when: "project.has_security_requirements === true"
        applies: true
    sections:
      - from: "Security Plan §5 Security Testing"
        to: "§2 Pre-release"
        influence: "Security scans (SAST/DAST) are included in pre-release checks"

  - id: CHANGE-LOG-*
    type: requires
    reason: "Change log must be ready before release"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Change Log §2 Release Notes"
        to: "§1 Pre-freeze"
        influence: "Release notes draft is required before code freeze"
```

### Impacts
```yaml
impacts:
  - id: POSTMORTEM-TEMPLATE-*
    type: influences
    reason: "Release checklist completion status informs post-release review"
    conditions:
      - when: "release.has_issues === true"
        applies: true
    sections:
      - from: "§4 Post-release"
        to: "Postmortem §5 Remediation & Actions"
        influence: "Incomplete checklist items become postmortem action items"

  - id: RELEASE-PLAN-*
    type: influences
    reason: "Checklist findings may update release plan for next release"
    conditions:
      - when: "release.completed === true"
        applies: true
    sections:
      - from: "§4 Post-release (lessons learned)"
        to: "Release Plan §7 Process Improvements"
        influence: "Release checklist gaps inform release process improvements"

  - id: INCIDENT-REPORT-*
    type: influences
    reason: "Release issues trigger incident reports"
    conditions:
      - when: "release.has_critical_issues === true"
        applies: true
    sections:
      - from: "§3 Release window (deployment issues)"
        to: "Incident Report §2 Incident Description"
        influence: "Critical release issues become incident reports"

  - id: MONITORING-PLAN-*
    type: blocks
    reason: "Release verification requires monitoring thresholds to be configured"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Release window (monitoring verification)"
        to: "Monitoring Plan §3 Alert Thresholds"
        influence: "Release checklist verifies monitoring is operational"

  - id: USER-GUIDE-*
    type: influences
    reason: "User documentation must be updated post-release"
    conditions:
      - when: "project.has_user_documentation === true"
        applies: true
    sections:
      - from: "§4 Post-release (changelog published)"
        to: "User Guide §6 Release Notes"
        influence: "Published changelog updates user documentation"

  - id: STAKEHOLDER-COMMUNICATION-*
    type: blocks
    reason: "Stakeholder communication is required post-release"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Post-release (stakeholder communication)"
        to: "Stakeholder Communication §2 Release Announcements"
        influence: "Release completion triggers stakeholder announcements"
```

### Related
```yaml
related:
  - id: RTM-*
    type: informs
    reason: "Release checklist verifies RTM requirements are delivered"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Release may require compliance verification"

  - id: BACKUP-PLAN-*
    type: informs
    reason: "Pre-release checks include backup verification"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance test results inform release readiness"

  - id: UAT-PLAN-*
    type: informs
    reason: "UAT completion is a release prerequisite"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-REL-CHECK-*.md"
    required: true
    purpose: "Track checklist item completion, blocker resolution, sign-offs"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-REL-CHECK-*.md"
    required: true
    purpose: "Store test results, deployment logs, smoke test screenshots, approval emails"

  - type: Approval
    path: "satellites/approvals/APPROVAL-REL-CHECK-*.md"
    required: true
    purpose: "Release Manager and stakeholder sign-off required before production deployment"

  - type: DoR
    path: "satellites/dor/DOR-REL-CHECK-*.md"
    required: true
    purpose: "Prerequisites: all PRs merged, tests passing, security scans clean, runbook updated, stakeholders notified"
```

## Pre‑freeze
- [ ] All critical PRs merged into release branch
- [ ] DoR check for all epics: passed
- [ ] Release notes: draft

## Pre‑release
- [ ] QA smoke tests green on staging
- [ ] Security scans (SAST/DAST) passed
- [ ] DB migration scripts reviewed and rollback tested
- [ ] Ops runbook updated

## Release window
- [ ] Cutover: run idempotent deploy script
- [ ] Smoke tests on production passed
- [ ] Monitoring thresholds verified

## Post‑release
- [ ] Postmortem scheduled
- [ ] Stakeholder communication sent
- [ ] Changelog published
