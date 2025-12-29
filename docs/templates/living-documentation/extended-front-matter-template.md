# Extended Front-Matter Template

**Living Documentation Framework (PROPOZYCJA-2)**

Ten szablon pokazuje rozszerzone front-matter dla dokumentów w systemie Living Documentation Framework.

---

## Podstawowy przykład (Extended Front-Matter)

```yaml
---
# === Standardowe pola (istniejące) ===
id: DOC-PRD-001
doctype: PRD
status: evolving
version: "2.3.1"
owner: "Jan Kowalski"
project: "Project Alpha"
created: "2025-10-01"

# === NOWE: Status Metadata (Living Documentation) ===
status_metadata:
  previous_status: approved
  status_changed_date: "2025-12-27"
  status_reason: "Iterative refinement based on Sprint 3 user feedback"
  next_review_date: "2026-01-15"

# === NOWE: Lifecycle Tracking ===
lifecycle:
  created: "2025-10-01"
  first_approved: "2025-11-01"
  last_modified: "2025-12-27"
  last_reviewed: "2025-12-27"  # Can differ from last_modified
  sunset_date: null
  migration_target: null

# === NOWE: Version Metadata (Semantic Versioning) ===
version_metadata:
  major: 2       # Breaking change
  minor: 3       # Non-breaking addition
  patch: 1       # Fix/clarification
  breaking_changes: false
  backward_compatible_with: ["2.2.x", "2.1.x"]
  forward_compatible_with: []

version_history:
  - version: "2.3.1"
    date: "2025-12-27"
    author: "Jan Kowalski"
    type: "patch"
    summary: "Clarified acceptance criteria in §7"
    breaking: false

  - version: "2.3.0"
    date: "2025-12-20"
    author: "Anna Nowak"
    type: "minor"
    summary: "Added Payment Gateway integration requirements"
    breaking: false
    impacts:
      - id: DOC-TDD-001
        action: "requires architecture update"
      - id: DOC-TEST-PLAN-001
        action: "requires new test cases"

  - version: "2.0.0"
    date: "2025-11-15"
    author: "Piotr Wiśniewski"
    type: "major"
    summary: "Pivot: Changed from B2C to B2B model"
    breaking: true
    impacts:
      - id: DOC-BUSINESS-CASE-001
        action: "requires rewrite"
      - id: DOC-TDD-001
        action: "architecture change"

# === NOWE: Cross-Reference Status (Impact Propagation) ===
cross_reference_status:
  upstream_changes_pending:
    - id: DOC-BUSINESS-CASE-001
      changed_version: "3.1.0"
      changed_date: "2025-12-25"
      change_type: "minor"
      impact_severity: "medium"
      action_required: "Review budget assumptions in §5"
      acknowledged: false

  downstream_impacts_pending:
    - id: DOC-TDD-001
      notified_date: "2025-12-27"
      acknowledged: true
      acknowledged_by: "Tech Lead"
      acknowledged_date: "2025-12-28"
    - id: DOC-TEST-PLAN-001
      notified_date: "2025-12-27"
      acknowledged: false

# === NOWE: Document Health ===
document_health:
  status: "healthy"  # healthy / warning / critical
  last_health_check: "2025-12-27"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified_days_ago: 7
      threshold_days: 90
    - name: "Dependency Validity"
      status: "healthy"
      all_dependencies_valid: true
    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true
    - name: "Owner Assignment"
      status: "healthy"
      owner_active: true
    - name: "Required Sections Completeness"
      status: "healthy"
      all_sections_present: true

# === NOWE: Deprecation (jeśli dotyczy) ===
deprecation: null
# Przykład gdy dokument jest deprecated:
# deprecation:
#   status: deprecated
#   deprecated_date: "2025-12-27"
#   deprecation_reason: "Replaced by PRD v3.0 after B2B pivot"
#   sunset_date: "2026-03-27"
#   migration_target: "DOC-PRD-003"
#   migration_guide: "docs/migrations/PRD-001-to-PRD-003.md"

---
```

---

## Przykład: Dokument w stanie "evolving"

```yaml
---
id: DOC-PRD-005
doctype: PRD
status: evolving
version: "1.2.0"
owner: "Anna Nowak"
project: "Project Beta"

status_metadata:
  previous_status: approved
  status_changed_date: "2025-12-20"
  status_reason: "Agile iteration - adding features based on Sprint 2 retrospective"
  next_review_date: "2026-01-10"

lifecycle:
  created: "2025-11-01"
  first_approved: "2025-11-15"
  last_modified: "2025-12-20"
  last_reviewed: "2025-12-20"
  sunset_date: null
  migration_target: null

version_metadata:
  major: 1
  minor: 2
  patch: 0
  breaking_changes: false
  backward_compatible_with: ["1.1.x", "1.0.x"]

cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: DOC-TDD-005
      notified_date: "2025-12-20"
      acknowledged: false

document_health:
  status: "healthy"
  last_health_check: "2025-12-27"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified_days_ago: 7
      threshold_days: 90

deprecation: null
---
```

---

## Przykład: Dokument deprecated (do wycofania)

```yaml
---
id: DOC-PRD-001-OLD
doctype: PRD
status: deprecated
version: "2.5.0"
owner: "Jan Kowalski"
project: "Project Alpha (Archived - B2C version)"

status_metadata:
  previous_status: approved
  status_changed_date: "2025-12-27"
  status_reason: "Company pivoted from B2C to B2B - this PRD is no longer applicable"
  next_review_date: null

lifecycle:
  created: "2025-01-15"
  first_approved: "2025-02-01"
  last_modified: "2025-11-20"
  last_reviewed: "2025-11-20"
  sunset_date: "2026-03-27"
  migration_target: "DOC-PRD-003-B2B"

version_metadata:
  major: 2
  minor: 5
  patch: 0
  breaking_changes: false
  backward_compatible_with: ["2.4.x", "2.3.x"]

cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: DOC-TDD-001
      notified_date: "2025-12-27"
      acknowledged: true
      acknowledged_by: "Tech Lead"
      acknowledged_date: "2025-12-28"
      action: "Migrate to TDD-003-B2B"

document_health:
  status: "warning"
  last_health_check: "2025-12-27"
  checks:
    - name: "Deprecation Status"
      status: "warning"
      message: "Document deprecated - 90 days until sunset"

deprecation:
  status: deprecated
  deprecated_date: "2025-12-27"
  deprecation_reason: "Pivot to B2B model - B2C requirements no longer applicable"
  sunset_date: "2026-03-27"
  migration_target: "DOC-PRD-003-B2B"
  migration_guide: "docs/migrations/PRD-001-B2C-to-PRD-003-B2B.md"
  impact_on_references:
    - id: DOC-TDD-001
      action: "Update reference to PRD-003-B2B"
    - id: DOC-TEST-PLAN-001
      action: "Migrate test cases to B2B scenarios"
---
```

---

## Przykład: Dokument w stanie "validating"

```yaml
---
id: DOC-BUSINESS-CASE-007
doctype: BUSINESS_CASE
status: validating
version: "2.0.0"
owner: "Piotr Wiśniewski"
project: "Project Gamma"

status_metadata:
  previous_status: evolving
  status_changed_date: "2025-12-15"
  status_reason: "Testing new pricing model with pilot customers - awaiting validation results"
  next_review_date: "2026-01-30"

lifecycle:
  created: "2025-10-01"
  first_approved: "2025-11-01"
  last_modified: "2025-12-15"
  last_reviewed: "2025-12-15"
  sunset_date: null
  migration_target: null

version_metadata:
  major: 2
  minor: 0
  patch: 0
  breaking_changes: true
  backward_compatible_with: []
  forward_compatible_with: []
  breaking_reason: "Pricing model changed from subscription to usage-based"

version_history:
  - version: "2.0.0"
    date: "2025-12-15"
    author: "Piotr Wiśniewski"
    type: "major"
    summary: "Changed pricing model from subscription to usage-based"
    breaking: true
    impacts:
      - id: DOC-PRD-007
        action: "Update pricing section and user flows"
      - id: DOC-FINANCIAL-PLAN-007
        action: "Recalculate revenue projections"

cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: DOC-PRD-007
      notified_date: "2025-12-15"
      acknowledged: true
    - id: DOC-FINANCIAL-PLAN-007
      notified_date: "2025-12-15"
      acknowledged: false

document_health:
  status: "healthy"
  last_health_check: "2025-12-27"
  checks:
    - name: "Validation Status"
      status: "healthy"
      message: "Under active validation - pilot running"

deprecation: null
---
```

---

## Opis pól

### status_metadata
- `previous_status`: Poprzedni status dokumentu
- `status_changed_date`: Data zmiany statusu
- `status_reason`: Powód zmiany statusu (kontekst biznesowy)
- `next_review_date`: Planowana data następnej review (opcjonalne)

### lifecycle
- `created`: Data utworzenia dokumentu
- `first_approved`: Data pierwszego zatwierdzenia
- `last_modified`: Data ostatniej modyfikacji treści
- `last_reviewed`: Data ostatniej review (może różnić się od last_modified)
- `sunset_date`: Data wycofania (jeśli dokument jest deprecated/sunset)
- `migration_target`: ID dokumentu docelowego (jeśli migracja)

### version_metadata
- `major`, `minor`, `patch`: Komponenty wersji semantycznej
- `breaking_changes`: Czy wersja zawiera breaking changes
- `backward_compatible_with`: Lista kompatybilnych wersji wstecznych
- `forward_compatible_with`: Lista kompatybilnych wersji forward

### version_history
Lista zmian wersji z:
- `version`: Numer wersji
- `date`: Data zmiany
- `author`: Autor zmiany
- `type`: major/minor/patch
- `summary`: Opis zmian
- `breaking`: Czy breaking change
- `impacts`: Lista wpływów na inne dokumenty

### cross_reference_status
**upstream_changes_pending**: Zmiany w dokumentach upstream (dependencies)
- `id`: ID dokumentu upstream
- `changed_version`: Nowa wersja
- `change_type`: major/minor/patch
- `impact_severity`: low/medium/high
- `action_required`: Co trzeba zrobić
- `acknowledged`: Czy potwierdzono

**downstream_impacts_pending**: Notyfikacje wysłane do dokumentów downstream
- `id`: ID dokumentu downstream
- `notified_date`: Data notyfikacji
- `acknowledged`: Czy potwierdzono
- `acknowledged_by`: Kto potwierdził
- `acknowledged_date`: Data potwierdzenia

### document_health
- `status`: healthy/warning/critical
- `last_health_check`: Data ostatniego sprawdzenia
- `checks`: Lista sprawdzeń:
  - `name`: Nazwa sprawdzenia
  - `status`: healthy/warning/critical
  - `message`: Dodatkowy komunikat (opcjonalnie)

### deprecation
- `status`: deprecated/sunset
- `deprecated_date`: Data ogłoszenia deprecation
- `deprecation_reason`: Powód wycofania
- `sunset_date`: Data końcowego wycofania
- `migration_target`: ID dokumentu zastępującego
- `migration_guide`: Link do migration guide
- `impact_on_references`: Lista wpływów na referencje

---

## Status Semantyka

| Status | Znaczenie | Can be referenced? | Can be modified? |
|--------|-----------|-------------------|------------------|
| **draft** | Praca w toku | ⚠️ With warning | ✅ Yes |
| **in-review** | W review | ⚠️ With warning | ✅ Limited |
| **approved** | Zatwierdzony | ✅ Yes | ⚠️ Requires CR |
| **evolving** | Ewoluujący | ✅ Yes | ✅ Yes (tracked) |
| **validating** | Walidacja | ✅ Yes | ⚠️ Limited |
| **refining** | Dopracowywanie | ✅ Yes | ✅ Minor only |
| **superseded** | Zastąpiony | ⚠️ Redirect to new | ❌ No |
| **deprecated** | Do wycofania | ⚠️ With warning | ❌ No |
| **sunset** | Wycofywany | ⚠️ With sunset date | ❌ No |
| **archived** | Archiwalny | ℹ️ Historical only | ❌ No |
| **migrated** | Migrowany | ➡️ Auto-redirect | ❌ No |

---

**Koniec szablonu**
