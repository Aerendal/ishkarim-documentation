# Impact Propagation Rules

**Living Documentation Framework (PROPOZYCJA-2)**

Ten dokument definiuje reguły automatycznej propagacji zmian (impact propagation) między dokumentami w dependency graph.

---

## Przegląd

Impact Propagation to system automatycznych notyfikacji i trackingu zmian, który:
- Wykrywa zmiany w dokumentach upstream (dependencies)
- Propaguje notyfikacje do dokumentów downstream (impacts)
- Trackuje acknowledgment zmian przez ownerów
- Automatycznie tworzy TODO items dla wymaganych aktualizacji
- Blokuje gates gdy critical changes nie są acknowledged

---

## Propagation Trigger Types

### 1. Version Bump (Major)

**Trigger:** Dokument upstream zmienia wersję MAJOR (X.0.0)

**Severity:** HIGH / CRITICAL

**Impact Propagation:**
```yaml
trigger: "version_bump_major"
severity: "high"
actions:
  - notify:
      targets: "all_downstream_documents"
      stakeholders: ["owner", "tech_lead", "project_manager"]
      channels: ["email_immediate", "slack", "github_issue"]
  - create_todo:
      title: "Review breaking change in <upstream-doc>"
      priority: "P1"
      due_days: 7
  - block_gates:
      gates: ["GATE-REQ_FREEZE", "GATE-RELEASE_READY"]
      until: "all_downstream_acknowledged"
  - require_acknowledgment:
      mandatory: true
      deadline_days: 14
```

**Example:**
```
BUSINESS_CASE v2.0.0 → v3.0.0 (major)
  ↓ (propagates to)
PRD, TDD, TEST_PLAN, FINANCIAL_PLAN
  ↓ (actions)
- Email sent to all owners: "CRITICAL: BUSINESS_CASE v3.0.0 breaking change"
- TODO created in each doc: "Review budget change in BC v3.0.0"
- Gate GATE-REQ_FREEZE blocked until all acknowledge
```

---

### 2. Version Bump (Minor)

**Trigger:** Dokument upstream zmienia wersję MINOR (x.Y.0)

**Severity:** MEDIUM

**Impact Propagation:**
```yaml
trigger: "version_bump_minor"
severity: "medium"
actions:
  - notify:
      targets: "direct_downstream_documents"
      stakeholders: ["owner"]
      channels: ["email_daily_digest", "slack"]
  - create_todo:
      title: "Review update in <upstream-doc>"
      priority: "P2"
      due_days: 14
  - require_acknowledgment:
      mandatory: false
      deadline_days: 30
```

**Example:**
```
PRD v2.3.0 → v2.4.0 (minor - added new section §8)
  ↓ (propagates to)
TDD, TEST_PLAN
  ↓ (actions)
- Email digest sent: "PRD v2.4.0 update: new integration requirements"
- TODO created: "Review PRD §8 - Payment Gateway integration"
- Acknowledgment requested within 30 days
```

---

### 3. Version Bump (Patch)

**Trigger:** Dokument upstream zmienia wersję PATCH (x.y.Z)

**Severity:** LOW

**Impact Propagation:**
```yaml
trigger: "version_bump_patch"
severity: "low"
actions:
  - notify:
      targets: "direct_downstream_documents"
      stakeholders: ["owner"]
      channels: ["email_weekly_digest"]
  - require_acknowledgment:
      mandatory: false
      deadline_days: null  # No deadline for patch changes
```

**Example:**
```
PRD v2.3.0 → v2.3.1 (patch - clarification)
  ↓ (propagates to)
TDD, TEST_PLAN
  ↓ (actions)
- Weekly digest: "PRD v2.3.1: clarified acceptance criteria"
- No TODO created (informational only)
```

---

### 4. Status Change (Approved → Evolving)

**Trigger:** Dokument zmienia status z `approved` na `evolving`

**Severity:** MEDIUM

**Impact Propagation:**
```yaml
trigger: "status_change_approved_to_evolving"
severity: "medium"
actions:
  - notify:
      targets: "direct_downstream_documents"
      stakeholders: ["owner"]
      channels: ["slack", "email"]
      message: "<upstream-doc> is now evolving - expect changes"
  - flag_document:
      flag: "upstream_evolving"
      impact: "Monitor for changes in upstream doc"
```

**Example:**
```
PRD status: approved → evolving
  ↓ (propagates to)
TDD, TEST_PLAN
  ↓ (actions)
- Slack notification: "PRD is now evolving - expect iterative changes"
- Document flagged: upstream_evolving = true
```

---

### 5. Status Change (Approved → Deprecated)

**Trigger:** Dokument zmienia status z `approved` na `deprecated`

**Severity:** CRITICAL

**Impact Propagation:**
```yaml
trigger: "status_change_approved_to_deprecated"
severity: "critical"
actions:
  - notify:
      targets: "all_referencing_documents"
      stakeholders: ["owner", "tech_lead", "project_manager"]
      channels: ["email_immediate", "slack", "github_issue"]
      message: "CRITICAL: <upstream-doc> deprecated - migration required"
  - create_todo:
      title: "Migrate from deprecated <upstream-doc>"
      priority: "P0"
      due_days: 30  # Based on deprecation_notice_days
  - block_new_references:
      action: "Prevent new documents from referencing deprecated doc"
  - require_acknowledgment:
      mandatory: true
      deadline_days: 7
```

**Example:**
```
BUSINESS_CASE-001 status: approved → deprecated (sunset: 90 days)
  ↓ (propagates to)
PRD, TDD, FINANCIAL_PLAN (all references)
  ↓ (actions)
- CRITICAL email: "BUSINESS_CASE-001 deprecated - migrate to BC-002"
- TODO created (P0): "Migrate to BUSINESS_CASE-002 before sunset"
- New documents blocked from referencing BC-001
```

---

### 6. Dependency Added

**Trigger:** Dokument dodaje nową dependency

**Severity:** MEDIUM

**Impact Propagation:**
```yaml
trigger: "dependency_added"
severity: "medium"
actions:
  - notify:
      targets: "new_dependency_document"
      stakeholders: ["owner"]
      channels: ["email"]
      message: "<downstream-doc> now depends on you - please review"
  - update_backlinks:
      action: "Add backlink in new dependency document (impact section)"
```

**Example:**
```
PRD adds dependency on: SECURITY_PLAN
  ↓ (propagates to)
SECURITY_PLAN
  ↓ (actions)
- Email to SECURITY_PLAN owner: "PRD now depends on your document"
- SECURITY_PLAN.impacts updated: Add PRD to impact list
```

---

### 7. Required Section Missing (Blocking)

**Trigger:** Health check detects missing required section

**Severity:** CRITICAL

**Impact Propagation:**
```yaml
trigger: "required_section_missing"
severity: "critical"
actions:
  - notify:
      targets: "document_owner"
      stakeholders: ["owner", "project_manager"]
      channels: ["email_immediate", "slack"]
  - block_status_change:
      blocked_statuses: ["approved"]
      reason: "Required section missing"
  - create_todo:
      title: "Add required section: <section-name>"
      priority: "P0"
      due_days: 3
```

---

## Propagation Rules by Document Type

### BUSINESS_CASE → [PRD, TDD, FINANCIAL_PLAN]

```yaml
propagation_rules:
  - trigger: "version_bump_minor"
    conditions:
      - section_changed: "SEC-BC-FIN"  # Budget section changed
    actions:
      - notify:
          targets: [PRD, TDD, FINANCIAL_PLAN]
          message: "Budget updated in BUSINESS_CASE - review scope/timeline"
          severity: "high"

  - trigger: "version_bump_major"
    conditions:
      - field_changed: "recommendation"  # Recommendation flipped
    actions:
      - notify:
          targets: [PRD, TDD, FINANCIAL_PLAN, ROADMAP]
          message: "CRITICAL: Business Case recommendation changed"
          severity: "critical"
      - block_gates: [GATE-REQ_FREEZE]
```

---

### PRD → [TDD, TEST_PLAN, USER_GUIDE]

```yaml
propagation_rules:
  - trigger: "version_bump_minor"
    conditions:
      - section_added: true  # New section added
    actions:
      - notify:
          targets: [TDD, TEST_PLAN]
          message: "New requirements added in PRD"
          severity: "medium"
      - create_todo:
          title: "Review new PRD section: <section-name>"
          targets: [TDD, TEST_PLAN]

  - trigger: "version_bump_major"
    conditions:
      - scope_changed: true
    actions:
      - notify:
          targets: [TDD, TEST_PLAN, USER_GUIDE]
          message: "CRITICAL: PRD scope changed - breaking change"
          severity: "critical"
      - block_gates: [GATE-REQ_FREEZE, GATE-RELEASE_READY]
```

---

### TDD → [TEST_PLAN, RUNBOOK, SECURITY_PLAN]

```yaml
propagation_rules:
  - trigger: "version_bump_minor"
    conditions:
      - section_changed: "SEC-TDD-API"  # API changed
    actions:
      - notify:
          targets: [TEST_PLAN]
          message: "API updated in TDD - review test cases"
          severity: "medium"

  - trigger: "version_bump_major"
    conditions:
      - architecture_changed: true
    actions:
      - notify:
          targets: [TEST_PLAN, RUNBOOK, SECURITY_PLAN]
          message: "CRITICAL: TDD architecture changed"
          severity: "critical"
```

---

## Notification Templates

### Email: Major Version Bump

```
Subject: [CRITICAL] <DOC-ID> v<X.0.0> Breaking Change - Action Required

Hi <Owner Name>,

A critical update has been detected in a document that <YOUR-DOC> depends on:

Document: <DOC-ID> - <Title>
Change: v<old> → v<new> (MAJOR - Breaking Change)
Date: YYYY-MM-DD
Author: <Name>

Summary of Changes:
- <Breaking Change 1>
- <Breaking Change 2>

Impact on <YOUR-DOC>:
- Section <X> requires update
- Section <Y> requires review

Action Required:
1. Review changelog: [link]
2. Review migration guide: [link]
3. Update <YOUR-DOC> accordingly
4. Acknowledge this change: [link]

Deadline: <Date> (14 days)

Questions? Contact: <upstream-doc-owner>

---
This notification was automatically generated by Living Documentation Framework
```

---

### Slack: Minor Version Bump

```
📝 Document Update

<DOC-ID> v<x.Y.0> (minor update)

Changes:
• New section added: <section>
• Requirements expanded

Affected documents:
• <YOUR-DOC> - Review recommended

Details: [link to changelog]
Acknowledge: [button]
```

---

## Acknowledgment Tracking

### Acknowledgment Workflow

```yaml
acknowledgment_workflow:
  1. Change detected:
      - System creates notification entry in downstream doc
      - cross_reference_status.upstream_changes_pending += change

  2. Owner notified:
      - Email/Slack sent with acknowledgment link
      - TODO created (if severity >= medium)

  3. Owner reviews:
      - Owner reads changelog
      - Owner reviews migration guide (if breaking)
      - Owner updates document (if needed)

  4. Owner acknowledges:
      - Owner clicks "Acknowledge" button/link
      - System records:
          - acknowledged: true
          - acknowledged_by: <name>
          - acknowledged_date: <date>
      - TODO marked as done (if created)

  5. System validates:
      - If all downstreams acknowledged → unblock gates
      - If deadline passed without ack → escalate
```

### Acknowledgment Metadata

```yaml
cross_reference_status:
  upstream_changes_pending:
    - id: DOC-BUSINESS-CASE-001
      changed_version: "3.0.0"
      changed_date: "2025-12-27"
      change_type: "major"
      impact_severity: "critical"
      action_required: "Review budget change - scope may need adjustment"
      acknowledged: true
      acknowledged_by: "Jan Kowalski"
      acknowledged_date: "2025-12-28"
      acknowledgment_notes: "Reviewed - no changes needed in PRD"
```

---

## Gate Blocking Rules

### When to Block Gates

```yaml
gate_blocking_rules:
  GATE-REQ_FREEZE:
    block_if:
      - upstream_changes_pending:
          severity: ["critical", "high"]
          acknowledged: false
      - required_sections_missing: true
      - document_health_status: "critical"

  GATE-RELEASE_READY:
    block_if:
      - upstream_changes_pending:
          severity: "critical"
          acknowledged: false
      - dependency_status: ["deprecated", "sunset", "archived"]
      - document_health_status: "critical"

  GATE-OPS_HANDOVER:
    block_if:
      - satellite_documents_missing: ["RUNBOOK", "MONITORING_PLAN"]
      - required_sections_missing: true
```

---

## Escalation Rules

### Escalation Workflow

```yaml
escalation_rules:
  - condition: "change_not_acknowledged AND deadline_passed"
    escalation_path:
      - day_0: "Notify owner"
      - day_7: "Notify owner + reminder"
      - day_14: "Notify owner + manager"
      - day_21: "Notify owner + manager + project_manager"
      - day_30: "Escalate to executive team"

  - condition: "critical_change AND no_response_3_days"
    escalation_path:
      - day_0: "Notify owner + manager (immediate)"
      - day_3: "Escalate to project_manager"
      - day_5: "Reassign document if no response"
```

---

## Implementation Notes

### Automation Requirements

**For impact propagation:**
- GitHub Action / CI pipeline integration
- Access to dependency graph
- Email/Slack API integration
- TODO creation automation
- Front-matter update automation

**Sample Python pseudocode:**
```python
def propagate_change(document, change_type, change_metadata):
    # Get downstream documents
    downstream_docs = get_downstream_documents(document)

    # Determine severity
    severity = determine_severity(change_type, change_metadata)

    # For each downstream doc
    for downstream in downstream_docs:
        # Create notification entry
        notification = create_notification(
            upstream_doc=document,
            change_type=change_type,
            severity=severity,
            metadata=change_metadata
        )

        # Update downstream doc front-matter
        update_cross_reference_status(downstream, notification)

        # Send notifications
        send_notifications(
            downstream.owner,
            notification,
            channels=get_channels_for_severity(severity)
        )

        # Create TODO if needed
        if severity in ["high", "critical"]:
            create_todo(
                document=downstream,
                title=f"Review change in {document.id}",
                priority=get_priority_for_severity(severity)
            )

        # Block gates if needed
        if severity == "critical":
            block_gates(downstream, notification)

    return downstream_docs
```

---

**Koniec specyfikacji**
