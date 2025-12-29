---
id: COMP-002
title: "COMP-002: Validator Component"
type: component
status: draft
parent: TDD-001-V2

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
