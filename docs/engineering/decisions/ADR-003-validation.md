---
id: ADR-003
title: "ADR-003: Validation Strategy"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-20
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-20"
  status_reason: "Decision approved after benchmarking - Pydantic 2.5+ selected"
  next_review_date: "2026-12-20"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-20"
  last_modified: "2025-12-29"
  last_reviewed: "2025-12-29"
  sunset_date: null
  migration_target: null
  note: "ADRs are typically long-lived - reviewed annually or when triggered"

# Version Metadata (Semantic Versioning)
version: "1.0.0"
version_metadata:
  major: 1
  minor: 0
  patch: 0
  breaking_changes: false
  backward_compatible_with: []
  note: "ADR approved - establishes validation library choice"

version_history:
  - version: "1.0.0"
    date: "2025-12-20"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: Pydantic 2.5+ selected for validation"
    breaking: false
    changes:
      - "Evaluated 3 options: Cerberus, OPA/Rego, Pydantic"
      - "Selected Pydantic 2.5+ (type-safe, fast Rust core, excellent errors)"
      - "Rejected Cerberus (slower, less type-safe)"
      - "Deferred OPA/Rego to V1.5 (overkill for MVP)"
    impacts:
      - id: "COMP-002-validator"
        impact_type: "unblocked"
        description: "Validator component can proceed with Pydantic"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes Pydantic for validation"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-002-validator"
      notified_date: "2025-12-20"
      acknowledged: true
      acknowledged_by: "Validator Developer"
      acknowledged_date: "2025-12-20"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 9
      note: "ADRs have longer freshness threshold (365 days)"

    - name: "Dependency Validity"
      status: "healthy"
      invalid_dependencies: []
      all_dependencies_valid: true

    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true
      broken_references: []

    - name: "Owner Assignment"
      status: "healthy"
      owner: "Tech Lead"
      owner_active: true

    - name: "Required Sections Completeness"
      status: "healthy"
      missing_sections: []
      completeness: "100%"

    - name: "Upstream Changes Pending"
      status: "healthy"
      pending_changes: 0

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      note: "Evidence E-145, E-164 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "TDD-001-V2"
    type: requires
    reason: "Validation requirements defined in TDD"

impacts:
  - id: "COMP-002-validator"
    type: blocks
    until: "ADR-003.status == approved"
    reason: "Validator implementation needs library choice"
  - id: "TDD-001-V2"
    type: informs
    reason: "Architecture updated with Pydantic validation"

context_snapshot:
  date: "2025-12-20"
  requirements:
    - "Type-safe (Python type hints)"
    - "Fast (< 50ms per document - NFR-001)"
    - "Good error messages (user-friendly)"
    - "Extensible (custom validation logic)"

evidence_ids:
  - "E-145"  # Pydantic benchmark (42ms dla 1000 docs)
  - "E-164"  # OPA evaluation (overkill dla MVP)

alternatives:
  - id: "OPT-CERBERUS"
    title: "Cerberus (Python validator)"
    status: rejected
    reason: "Slower, less type-safe, weaker error messages"

  - id: "OPT-OPA-REGO"
    title: "OPA + Rego (policy-as-code)"
    status: deferred
    reason: "Overkill dla MVP (complex policy language). Defer to V1.5 if complex policies needed."

  - id: "OPT-PYDANTIC"
    title: "Pydantic 2.x"
    status: selected
    reason: "Type-safe (Python hints), fast (Rust core), excellent errors, JSON Schema export"
---

# ADR-003: Validation Strategy

**Decision**: Use **Pydantic 2.5+** for schema validation

**Status**: ✅ APPROVED

---

## Context

**Problem**: Validate documents against schemas (frontmatter fields, constraints).

**Requirements**:
1. Type-safe (Python type hints)
2. Fast (< 50ms per document - NFR-001)
3. Good error messages (user-friendly)
4. Extensible (custom validation logic)

---

## Decision

### Pydantic 2.5+ ✅

**Why**:
- ✅ **Type-safe**: Python type hints → runtime validation
- ✅ **Fast**: Rust core w v2 (17× faster than v1) - 42μs/doc [E-145]
- ✅ **Error messages**: Precise, actionable ("field 'id' is required")
- ✅ **JSON Schema export**: Future OPA integration if needed
- ✅ **Mature**: v2 stable, production-ready

**Usage**:
```python
from pydantic import BaseModel, Field

class DocumentFrontmatter(BaseModel):
    id: str = Field(..., pattern=r"^[A-Z]+-\d+")
    title: str = Field(..., min_length=1)
    type: Literal["prd", "tdd", "adr"]
    status: Literal["draft", "review", "approved"]

# Validate
try:
    fm = DocumentFrontmatter(**yaml_data)
except ValidationError as e:
    print(e.errors())  # Detailed errors
```

**Evidence**: [E-145] Benchmark: 1000 docs validated → 42ms (42μs/doc avg)

---

## Alternatives

### Cerberus ❌
**Cons**: Slower, less type-safe, weaker error messages
**Rejected**: Pydantic superior in all criteria

### OPA/Rego ❌ (Deferred)
**Pros**: Policy-as-code (complex rules engine)
**Cons**: **Overkill dla MVP** (learning curve, YAML → Rego translation complex)
**Decision**: Defer to V1.5 if complex policies emerge
**Evidence**: [E-164] Evaluation showed 80% rules achievable w Pydantic validators

---

## Consequences

**Positive**:
- ✅ Type safety (catch errors at runtime + IDE autocomplete)
- ✅ Performance excellent (< 50ms target met)
- ✅ Maintainable (Python-native, standard library integration)

**Negative**:
- ⚠️ Complex policies need custom validators (but acceptable dla MVP scope)

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
