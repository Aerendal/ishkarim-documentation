# Document Health Check Specification

**Living Documentation Framework (PROPOZYCJA-2)**

Ten dokument definiuje system automatycznych sprawdzeń zdrowia dokumentów (health checks) w ramach Living Documentation Framework.

---

## Przegląd

Document Health Check to automatyczny system monitorowania stanu dokumentów, który:
- Wykrywa stale dokumenty (nie aktualizowane od długiego czasu)
- Sprawdza spójność zależności (czy dependencies są valid)
- Monitoruje kompletność wymaganych sekcji
- Trackuje aktywność ownerów
- Generuje alerty dla dokumentów wymagających uwagi

---

## Health Status Levels

### Status: HEALTHY (🟢)

**Kryteria:**
- Wszystkie health checks passed
- Dokument aktualny (modified/reviewed w threshold)
- Wszystkie dependencies valid
- Owner aktywny i przypisany
- Wymagane sekcje kompletne
- Cross-references consistent

**Action:** Brak akcji wymaganej

---

### Status: WARNING (🟡)

**Kryteria:**
- 1-2 health checks failed (non-critical)
- Dokument zbliża się do threshold freshness (>70% threshold)
- 1-2 deprecated dependencies
- Minor inconsistencies w cross-references

**Action:** Review zalecana w ciągu 14 dni

**Examples:**
- Dokument nie był modyfikowany od 65 dni (threshold: 90 dni)
- Jedna dependency jest deprecated (ale nie sunset)
- Owner on vacation (temporary)

---

### Status: CRITICAL (🔴)

**Kryteria:**
- 3+ health checks failed
- Dokument stale (exceeded freshness threshold)
- Multiple deprecated/invalid dependencies
- Brak ownera (owner left company)
- Wymagane sekcje missing
- Breaking inconsistencies

**Action:** Immediate action required

**Examples:**
- Dokument nie był modyfikowany od >120 dni (threshold: 90 dni)
- 3+ dependencies są archived/sunset
- Owner left company 2 months ago, no replacement
- Required section missing (blocker for approval)

---

## Health Check Types

### 1. Freshness Check

**Purpose:** Ensure documents są regularnie reviewed i aktualizowane

**Check Logic:**
```yaml
freshness_check:
  name: "Freshness Check"
  threshold_days: 90  # Depends on doctype
  check:
    - IF (current_date - last_modified) > threshold_days
      THEN status = WARNING
    - IF (current_date - last_modified) > (threshold_days * 1.5)
      THEN status = CRITICAL
    - IF (current_date - last_reviewed) > threshold_days
      AND (current_date - last_modified) < threshold_days
      THEN status = HEALTHY (reviewed recently, even if not modified)
```

**Thresholds by Doctype:**
| Doctype | Threshold | Rationale |
|---------|-----------|-----------|
| PRD | 90 days | Product requirements evolve frequently |
| TDD | 120 days | Technical design more stable |
| BUSINESS_CASE | 180 days | Business context changes slower |
| ADR | N/A | ADR are immutable once approved |
| SECURITY_PLAN | 90 days | Security landscape changes frequently |
| DPIA | 180 days | GDPR compliance requirements stable |

**Output:**
```yaml
freshness_check:
  status: "healthy | warning | critical"
  last_modified: "YYYY-MM-DD"
  last_reviewed: "YYYY-MM-DD"
  days_since_modified: 45
  days_since_reviewed: 45
  threshold_days: 90
  message: "Document fresh - last reviewed 45 days ago"
```

---

### 2. Dependency Validity Check

**Purpose:** Ensure all dependencies są valid (not deprecated/archived)

**Check Logic:**
```yaml
dependency_validity_check:
  name: "Dependency Validity Check"
  check:
    - FOR EACH dependency IN dependencies:
        - IF dependency.status == "archived"
          THEN flag as INVALID (critical)
        - IF dependency.status == "deprecated"
          THEN flag as DEPRECATED (warning)
        - IF dependency.status == "sunset"
          THEN flag as SUNSET (critical)
        - IF dependency.version < required_min_version
          THEN flag as OUTDATED (warning)
```

**Output:**
```yaml
dependency_validity_check:
  status: "healthy | warning | critical"
  total_dependencies: 5
  valid_dependencies: 3
  deprecated_dependencies:
    - id: DOC-BUSINESS-CASE-001
      status: "deprecated"
      sunset_date: "2026-03-27"
      action: "Update to DOC-BUSINESS-CASE-002"
  invalid_dependencies:
    - id: DOC-MARKET-ANALYSIS-001
      status: "archived"
      action: "Replace with current market analysis"
  message: "2 dependencies need attention"
```

---

### 3. Cross-Reference Consistency Check

**Purpose:** Ensure cross-references są consistent (bidirectional)

**Check Logic:**
```yaml
cross_reference_consistency_check:
  name: "Cross-Reference Consistency Check"
  check:
    - FOR EACH reference IN cross_references:
        - IF this_doc references target_doc
          THEN verify target_doc has backlink to this_doc
        - IF backlink missing
          THEN flag as INCONSISTENT
```

**Output:**
```yaml
cross_reference_consistency_check:
  status: "healthy | warning | critical"
  total_references: 8
  consistent_references: 7
  inconsistent_references:
    - id: DOC-TDD-001
      issue: "Missing backlink (TDD-001 does not reference this PRD)"
      action: "Add reference in TDD-001 dependencies section"
  message: "1 inconsistent reference found"
```

---

### 4. Owner Assignment Check

**Purpose:** Ensure dokument ma aktywnego ownera

**Check Logic:**
```yaml
owner_assignment_check:
  name: "Owner Assignment Check"
  check:
    - IF owner IS NULL
      THEN status = CRITICAL ("No owner assigned")
    - IF owner.status == "inactive" (left company)
      THEN status = CRITICAL ("Owner inactive")
    - IF owner.on_vacation AND vacation > 30 days
      THEN status = WARNING ("Owner on extended leave")
```

**Output:**
```yaml
owner_assignment_check:
  status: "healthy | warning | critical"
  owner: "Jan Kowalski"
  owner_active: true
  owner_status: "active"
  message: "Owner active and assigned"
```

**Critical Output:**
```yaml
owner_assignment_check:
  status: "critical"
  owner: "Anna Nowak"
  owner_active: false
  owner_status: "left company on 2025-11-15"
  days_without_owner: 42
  action: "Reassign owner immediately"
  message: "Owner left company 42 days ago - reassignment required"
```

---

### 5. Required Sections Completeness Check

**Purpose:** Ensure wszystkie wymagane sekcje są obecne i complete

**Check Logic:**
```yaml
required_sections_check:
  name: "Required Sections Completeness Check"
  check:
    - FOR EACH section IN doctype.required_sections:
        - IF section NOT FOUND in document
          THEN flag as MISSING
        - IF section contains only placeholders (TBD, TODO, etc.)
          THEN flag as INCOMPLETE
```

**Output:**
```yaml
required_sections_check:
  status: "healthy | warning | critical"
  required_sections: 9
  present_sections: 8
  missing_sections:
    - id: SEC-PRD-RISK
      title: "Ryzyka i mitigacje"
      severity: "critical"
      action: "Add required section before approval"
  incomplete_sections:
    - id: SEC-PRD-AC
      title: "Kryteria akceptacji"
      issue: "Contains placeholder 'TBD'"
      severity: "warning"
  message: "1 critical section missing"
```

---

### 6. Upstream Changes Pending Check

**Purpose:** Detect upstream changes that may impact this document

**Check Logic:**
```yaml
upstream_changes_check:
  name: "Upstream Changes Pending Check"
  check:
    - FOR EACH dependency IN dependencies:
        - IF dependency.version > referenced_version
          THEN flag as UPDATE_AVAILABLE
        - IF dependency.version is MAJOR bump
          THEN flag as BREAKING_CHANGE (critical)
        - IF dependency.version is MINOR bump
          THEN flag as NON_BREAKING_CHANGE (warning)
```

**Output:**
```yaml
upstream_changes_check:
  status: "healthy | warning | critical"
  upstream_changes_pending:
    - id: DOC-BUSINESS-CASE-001
      referenced_version: "2.0.0"
      current_version: "2.1.0"
      change_type: "minor"
      severity: "medium"
      action: "Review budget assumptions updated in v2.1.0"
      acknowledged: false
  message: "1 upstream change pending review"
```

---

### 7. Satellite Completeness Check

**Purpose:** Ensure wymagane satellite documents są present

**Check Logic:**
```yaml
satellite_completeness_check:
  name: "Satellite Completeness Check"
  check:
    - FOR EACH satellite IN doctype.satellites_required:
        - IF satellite NOT FOUND
          THEN flag as MISSING (based on severity)
        - IF satellite.status == "todo"
          THEN flag as INCOMPLETE
```

**Output:**
```yaml
satellite_completeness_check:
  status: "healthy | warning | critical"
  required_satellites: [TODO_SECTION, DOR_DOC, DOD_DOC, APPROVAL, EVIDENCE, CHANGELOG]
  present_satellites: [TODO_SECTION, DOR_DOC, APPROVAL, CHANGELOG]
  missing_satellites:
    - type: DOD_DOC
      severity: "warning"
      action: "Create DoD document"
    - type: EVIDENCE
      severity: "warning"
      action: "Add evidence documents"
  message: "2 recommended satellites missing"
```

---

## Health Check Execution

### Execution Frequency

```yaml
health_check_schedule:
  - check: "freshness_check"
    frequency: "daily"
    time: "02:00 UTC"

  - check: "dependency_validity_check"
    frequency: "daily"
    time: "02:30 UTC"

  - check: "cross_reference_consistency_check"
    frequency: "weekly"
    day: "Monday"
    time: "03:00 UTC"

  - check: "owner_assignment_check"
    frequency: "weekly"
    day: "Monday"
    time: "03:30 UTC"

  - check: "required_sections_check"
    frequency: "on_demand"  # Triggered on status change to "in-review"

  - check: "upstream_changes_check"
    frequency: "real_time"  # Triggered when dependency version changes

  - check: "satellite_completeness_check"
    frequency: "weekly"
    day: "Monday"
    time: "04:00 UTC"
```

---

## Health Check Output Format

### Document Front-Matter

```yaml
document_health:
  status: "healthy | warning | critical"
  last_health_check: "2025-12-27T02:00:00Z"

  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified_days_ago: 7
      threshold_days: 90
      message: "Document fresh"

    - name: "Dependency Validity"
      status: "warning"
      invalid_dependencies: 1
      message: "1 deprecated dependency (DOC-BC-001)"

    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true

    - name: "Owner Assignment"
      status: "healthy"
      owner_active: true

    - name: "Required Sections"
      status: "healthy"
      all_sections_present: true

    - name: "Upstream Changes"
      status: "warning"
      pending_changes: 1
      message: "1 upstream change pending review"

    - name: "Satellite Completeness"
      status: "warning"
      missing_satellites: 2
      message: "2 recommended satellites missing"

  overall_score: 71  # 0-100 (weighted average)
  risk_level: "medium"
```

---

## Automated Actions

### Alert Triggers

```yaml
alert_rules:
  - condition: "health_status == CRITICAL"
    action: "send_email_to_owner"
    frequency: "daily"
    escalation:
      - after_days: 7
        action: "send_email_to_owner + manager"
      - after_days: 14
        action: "send_email_to_owner + manager + project_manager"

  - condition: "health_status == WARNING"
    action: "send_weekly_digest_to_owner"
    frequency: "weekly"

  - condition: "owner_inactive == true AND days_without_owner > 30"
    action: "escalate_to_project_manager"
    frequency: "immediate"
```

---

## Health Dashboard (Conceptual)

```
Document Health Dashboard
=========================

🔴 CRITICAL (3 documents)
  - DOC-PRD-001: Missing required section (Risk Management) - 14 days
  - DOC-TDD-002: Dependency on archived doc (BRD-005) - 7 days
  - DOC-TEST-PLAN-003: No owner assigned (owner left company) - 42 days

🟡 WARNING (12 documents)
  - DOC-BUSINESS-CASE-001: Not modified >60 days
  - DOC-SECURITY-PLAN-001: Deprecated dependency (DPIA-001)
  - DOC-PRD-005: Upstream change pending review (BC-001 v2.1.0)
  - ...

🟢 HEALTHY (133 documents)

Health Score Distribution:
  90-100: ████████████████████ 45 docs
  70-89:  ████████████ 38 docs
  50-69:  ██████ 25 docs
  <50:    ███ 15 docs
```

---

## Metrics

### Key Performance Indicators

```yaml
health_metrics:
  - metric: "Document Freshness Rate"
    definition: "% of docs modified/reviewed within threshold"
    target: ">80%"
    current: "72%"

  - metric: "Dependency Validity Rate"
    definition: "% of docs with all valid dependencies"
    target: ">95%"
    current: "88%"

  - metric: "Owner Assignment Rate"
    definition: "% of docs with active owner"
    target: ">98%"
    current: "94%"

  - metric: "Health Score (Average)"
    definition: "Average health score across all documents"
    target: ">75"
    current: "68"

  - metric: "Critical Documents Count"
    definition: "Number of documents in CRITICAL status"
    target: "<5"
    current: "3"
```

---

## Implementation Notes

### Technical Requirements

**For automated health checks:**
- Python script or GitHub Action
- Access to document front-matter (YAML parsing)
- Access to dependency graph
- Integration with notification system (email/Slack)

**Sample Python pseudocode:**
```python
def run_health_check(document):
    health = {
        "status": "healthy",
        "checks": []
    }

    # Run all checks
    health["checks"].append(freshness_check(document))
    health["checks"].append(dependency_validity_check(document))
    health["checks"].append(cross_reference_check(document))
    health["checks"].append(owner_assignment_check(document))
    health["checks"].append(required_sections_check(document))
    health["checks"].append(upstream_changes_check(document))
    health["checks"].append(satellite_completeness_check(document))

    # Calculate overall status
    critical_count = len([c for c in health["checks"] if c["status"] == "critical"])
    warning_count = len([c for c in health["checks"] if c["status"] == "warning"])

    if critical_count >= 3:
        health["status"] = "critical"
    elif critical_count >= 1:
        health["status"] = "critical"
    elif warning_count >= 2:
        health["status"] = "warning"

    # Update document front-matter
    update_document_health(document, health)

    # Trigger alerts if needed
    if health["status"] == "critical":
        send_alert(document.owner, health)

    return health
```

---

**Koniec specyfikacji**
