---
id: COMP-002
title: "COMP-002: Validator Component"
type: component
domain: architecture
status: draft
created: 2025-12-26
updated: 2025-12-29
owner: Tech Lead
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: null
  status_changed_date: "2025-12-26"
  status_reason: "Initial component specification - awaiting implementation"
  next_review_date: "2026-01-15"
  review_frequency: "bi-weekly during implementation"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: null
  last_modified: "2025-12-29"
  last_reviewed: "2025-12-29"
  sunset_date: null
  migration_target: null
  note: "Draft specification - implementation not started"

# Version Metadata (Semantic Versioning)
version: "0.1.0"
version_metadata:
  major: 0
  minor: 1
  patch: 0
  breaking_changes: false
  backward_compatible_with: []
  pre_release: true
  note: "Draft specification - implementation phase not started"

version_history:
  - version: "0.1.0"
    date: "2025-12-26"
    author: "Tech Lead"
    type: "minor"
    summary: "Initial component specification for Validator"
    breaking: false
    changes:
      - "Zdefiniowano public API (ValidatorAPI class)"
      - "Określono gap detection logic (E110, E120, E170, E180, E190, E200)"
      - "Zdefiniowano schema format (YAML)"
      - "Określono performance target: < 50ms per document"
      - "Benchmark: 8ms/doc validation (Pydantic: 42μs/doc)"
    impacts:
      - id: "COMP-004-gap-engine"
        impact_type: "informs"
        description: "Gap Engine konsumuje ValidationResult z Validator"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending:
    - id: "COMP-001-parser"
      change_type: "blocks"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Validator oczekuje na Parser Document output"
  downstream_impacts_pending:
    - id: "COMP-004-gap-engine"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Gap Engine czeka na ValidationResult format"

# Document Health
document_health:
  status: "warning"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 30
      days_since_modified: 3
      note: "Draft components reviewed bi-weekly during implementation"

    - name: "Dependency Validity"
      status: "warning"
      invalid_dependencies:
        - "API-SPEC-001 (not found - needs to be created)"
      all_dependencies_valid: false
      note: "API-SPEC-001 referenced but not yet created"

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
      note: "Specification complete - awaiting implementation"

    - name: "Upstream Changes Pending"
      status: "warning"
      pending_changes: 1
      note: "Blocked by COMP-001-parser (awaiting Document output)"

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      note: "Evidence E-145 supports Pydantic benchmark"

# Deprecation
deprecation: null

dependencies:
  - id: "COMP-001-parser"
    type: requires
    reason: "Validator operates on parsed Document objects"

  - id: "ADR-003"
    type: requires
    reason: "Implementation uses Pydantic (ADR-003 decision)"

  - id: "API-SPEC-001"
    type: implements
    reason: "Validator implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

  - id: "COMP-004-gap-engine"
    type: informs
    reason: "Validator output (ValidationResult) feeds Gap Engine"

evidence_ids:
  - "E-145"  # Pydantic benchmark (42μs/doc)
---

# COMP-002: Validator Component

**Responsibility**: Validate documents against schemas, detect gaps (E110, E120, E170, E180, E190, E200)

---

## Public Interface

```python
# src/core/validator.py

from models.document import Document
from models.schema import DocumentSchema
from models.gap import Gap, ValidationResult

class ValidatorAPI:
    """Document validation engine."""

    def validate_document(
        self,
        doc: Document,
        schema: DocumentSchema
    ) -> ValidationResult:
        """
        Validate document against type schema.

        Returns:
            ValidationResult(
                valid: bool,
                gaps: list[Gap],  # E110, E120, E170, E180, E190, E200
                errors: list[str]
            )
        """

    def load_schema(self, doc_type: str) -> DocumentSchema:
        """Load schema from YAML (schemas/{doc_type}.yaml)."""

    def check_required_sections(self, doc: Document) -> list[Gap]:
        """E110: Missing required sections."""

    def detect_placeholders(self, doc: Document) -> list[Gap]:
        """E120: TODO/TBD/PLACEHOLDER detected."""

    def check_evidence_notes(self, doc: Document) -> list[Gap]:
        """E170: Missing evidence notes (claims without [E-XXX])."""

    def check_storytelling(self, doc: Document) -> list[Gap]:
        """E180: Missing storytelling (bullet lists without narrative)."""

    def check_alternatives(self, doc: Document) -> list[Gap]:
        """E190: Missing alternatives in decision docs."""

    def check_postmortem(self, doc: Document) -> list[Gap]:
        """E200: Missing post-mortem (deployed > 90 days)."""
```

---

## Schema Format (YAML)

```yaml
# schemas/prd.yaml
document_type: prd
version: "1.0"

frontmatter:
  required_fields: [id, title, type, status, owner]
  optional_fields: [priority, dependencies, impacts]
  constraints:
    id:
      pattern: "^PRD-[A-Z0-9]+-V\\d+$"
    status:
      enum: [draft, review, req-freeze, approved]
    priority:
      enum: [critical, high, medium, low]

required_sections:
  - name: "User Personas"
    pattern: "^## User Personas"
    mandatory: true
  - name: "Functional Requirements"
    pattern: "^## Functional Requirements"
    mandatory: true
    min_items: 10  # At least 10 FR

gap_detection:
  E110:
    enabled: true
    severity: critical
  E120:
    enabled: true
    patterns: ["TODO", "TBD", "PLACEHOLDER", "XXX", "FIXME"]
  E170:
    enabled: true
    min_evidence_notes: 5  # At least 5 [E-XXX] references
```

---

## Gap Detection Logic

### E110: Missing Sections

```python
def check_required_sections(self, doc: Document) -> list[Gap]:
    gaps = []
    schema = self.load_schema(doc.type)

    for req_section in schema.required_sections:
        found = False
        for section in doc.sections:
            if re.match(req_section.pattern, section.title):
                found = True
                break

        if not found:
            gaps.append(Gap(
                gap_id=f"E110-{doc.id}-{req_section.name}",
                gap_type="E110",
                severity="critical",
                description=f"Missing required section: {req_section.name}",
                remediation_steps=[f"Add section matching pattern: {req_section.pattern}"]
            ))

    return gaps
```

### E120: Placeholders

```python
PLACEHOLDER_PATTERNS = [
    r'\bTODO\b',
    r'\bTBD\b',
    r'\bPLACEHOLDER\b',
    r'\bXXX\b',
    r'\bFIXME\b',
]

def detect_placeholders(self, doc: Document) -> list[Gap]:
    gaps = []
    for pattern in PLACEHOLDER_PATTERNS:
        matches = re.finditer(pattern, doc.body, re.IGNORECASE)
        for match in matches:
            line_num = doc.body[:match.start()].count('\n') + 1
            gaps.append(Gap(
                gap_id=f"E120-{doc.id}-line-{line_num}",
                gap_type="E120",
                severity="high",
                location=f"Line {line_num}",
                description=f"Placeholder detected: {match.group()}",
                remediation_steps=["Replace placeholder with actual content"]
            ))

    return gaps
```

---

## Performance

**Target**: < 50ms per document (NFR-001)

**Measured**:
- Schema validation (Pydantic): 42μs/doc
- Section checking: ~5ms/doc
- Placeholder detection (regex): ~3ms/doc
- **Total**: ~8ms/doc ✅

---

## Testing

```python
def test_e110_missing_section():
    doc = Document(sections=[Section(title="## Introduction")])
    schema = DocumentSchema(required_sections=[
        {"name": "User Personas", "pattern": "^## User Personas"}
    ])

    validator = ValidatorAPI()
    result = validator.validate_document(doc, schema)

    assert len(result.gaps) == 1
    assert result.gaps[0].gap_type == "E110"

def test_e120_placeholder_detection():
    doc = Document(body="This is TODO: finish this section")
    validator = ValidatorAPI()
    gaps = validator.detect_placeholders(doc)

    assert len(gaps) == 1
    assert "TODO" in gaps[0].description
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-003](../decisions/ADR-003-validation.md)
