---
id: SCHEMA-001
title: "SCHEMA-001: Document Type Schemas"
type: schema
status: draft
parent: TDD-001-V2

dependencies:
  - id: "DATA-MODEL-001"
    type: requires
    reason: "Schemas validate against DocumentSchema model"

  - id: "COMP-002-validator"
    type: requires
    reason: "Validator loads and enforces these schemas"

evidence_ids:
  - "E-156"  # Schema design evaluation
---

# SCHEMA-001: Document Type Schemas

**Responsibility**: YAML schema definitions dla wszystkich typów dokumentów, validation rules, gap detection config

---

## Spis Treści

1. [Schema Format](#schema-format)
2. [PRD Schema](#prd-schema)
3. [TDD Schema](#tdd-schema)
4. [ADR Schema](#adr-schema)
5. [Component Schema](#component-schema)
6. [RFC Schema](#rfc-schema)
7. [Vision Schema](#vision-schema)

---

## Schema Format

### Schema Structure

**Location**: `schemas/{doc_type}.yaml`

```yaml
# schemas/template.yaml

document_type: "doc-type-name"  # Unique identifier
version: "1.0"                  # Schema version

# Frontmatter validation
frontmatter:
  required_fields: [id, title, type, status]
  optional_fields: [owner, priority, domain]

  constraints:
    id:
      pattern: "^[A-Z]+-[A-Z0-9]+-V?\\d+$"
      description: "Document ID format"

    status:
      enum: [draft, review, approved]
      description: "Allowed status values"

    priority:
      enum: [critical, high, medium, low]
      description: "Priority levels"

# Content validation
required_sections:
  - name: "Section Name"
    pattern: "^## Section Name"  # Regex for H2 heading
    mandatory: true
    min_items: null  # Optional: minimum items in section
    description: "Human-readable description"

# Gap detection configuration
gap_detection:
  E110:  # Missing required section
    enabled: true
    severity: critical

  E120:  # Placeholder detection
    enabled: true
    patterns: [TODO, TBD, PLACEHOLDER, XXX, FIXME]
    severity: high

  E170:  # Missing evidence notes
    enabled: true
    min_evidence_notes: 5  # Minimum [E-XXX] references
    severity: medium

# Quality gates
quality_gates:
  - name: "GATE-NAME"
    status_trigger: "approved"  # Status that triggers gate check
    conditions:
      - no_critical_gaps
      - no_high_gaps
      - all_sections_present
      - min_evidence_count: 5
```

---

## PRD Schema

**File**: `schemas/prd.yaml`

```yaml
document_type: "prd"
version: "1.0"
description: "Product Requirements Document"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - owner
    - phase
    - priority

  optional_fields:
    - domain
    - dependencies
    - impacts
    - evidence_ids
    - alternatives
    - created
    - updated

  constraints:
    id:
      pattern: "^PRD-[A-Z0-9]+(-V\\d+)?$"
      examples: ["PRD-001-V2", "PRD-MVP-V1"]

    status:
      enum:
        - draft
        - in-progress
        - review
        - req-freeze        # Quality gate
        - approved
        - deprecated
      description: "PRD lifecycle statuses"

    priority:
      enum: [critical, high, medium, low]

    phase:
      enum:
        - requirements
        - design
        - implementation
        - testing
        - operations

    owner:
      description: "Product Owner or Lead"
      examples: ["Product Manager", "Tech Lead"]

required_sections:
  # Part 1: Overview
  - name: "Executive Summary"
    pattern: "^## Executive Summary"
    mandatory: true
    description: "High-level product summary"

  - name: "Problem Statement"
    pattern: "^## Problem Statement"
    mandatory: true
    description: "What problem are we solving?"

  # Part 2: Users
  - name: "User Personas"
    pattern: "^## User Personas"
    mandatory: true
    description: "Target user profiles"

  - name: "User Stories"
    pattern: "^## User Stories"
    mandatory: true
    min_items: 5
    description: "As a [persona], I want [goal], so that [benefit]"

  # Part 3: Requirements
  - name: "Functional Requirements"
    pattern: "^## Functional Requirements"
    mandatory: true
    min_items: 10
    description: "FR-001, FR-002, etc. with acceptance criteria"

  - name: "Non-Functional Requirements"
    pattern: "^## Non-Functional Requirements"
    mandatory: true
    min_items: 5
    description: "NFR-001: Performance, scalability, security, etc."

  # Part 4: Constraints
  - name: "Constraints"
    pattern: "^## (Constraints|Technical Constraints)"
    mandatory: true
    description: "Technical, business, regulatory constraints"

  - name: "Out of Scope"
    pattern: "^## Out of Scope"
    mandatory: false
    description: "What we're explicitly NOT doing"

  # Part 5: Quality
  - name: "Acceptance Criteria"
    pattern: "^## (Acceptance Criteria|Quality Gates)"
    mandatory: true
    description: "DoR/DoD criteria"

gap_detection:
  E110:
    enabled: true
    severity: critical
    description: "Missing required section"

  E120:
    enabled: true
    severity: high
    patterns: [TODO, TBD, PLACEHOLDER, XXX, FIXME, "\\[\\]", "\\.\\.\\.", "???"]
    description: "Placeholder/incomplete content detected"

  E130:
    enabled: true
    severity: high
    description: "Missing evidence document (satellite)"

  E140:
    enabled: true
    severity: critical
    description: "Broken dependency (non-existent or wrong status)"

  E150:
    enabled: true
    severity: critical
    description: "Quality gate blocked"

  E170:
    enabled: true
    severity: medium
    min_evidence_notes: 10
    description: "Insufficient evidence notes [E-XXX]"

  E180:
    enabled: true
    severity: medium
    check_storytelling: true
    description: "Missing storytelling (bullet lists without narrative)"

  E190:
    enabled: true
    severity: high
    description: "Missing alternatives (for major decisions)"

  E200:
    enabled: false  # Not applicable to PRD
    description: "Missing post-mortem"

quality_gates:
  - name: "REQ-FREEZE"
    status_trigger: "req-freeze"
    description: "Requirements frozen for design"
    conditions:
      - no_critical_gaps
      - no_high_gaps
      - all_sections_present: true
      - min_evidence_count: 10
      - stakeholder_approvals: ["Product Owner", "Tech Lead"]

    blockers_detect:
      - E110  # Missing sections block freeze
      - E120  # Placeholders block freeze
      - E140  # Broken deps block freeze
```

---

## TDD Schema

**File**: `schemas/tdd.yaml`

```yaml
document_type: "tdd"
version: "1.0"
description: "Technical Design Document"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - owner
    - phase

  optional_fields:
    - domain
    - dependencies
    - impacts
    - evidence_ids
    - alternatives
    - context_snapshot

  constraints:
    id:
      pattern: "^TDD-[A-Z0-9]+(-V\\d+)?$"
      examples: ["TDD-001-V2"]

    status:
      enum:
        - draft
        - in-progress
        - review
        - design-complete  # Quality gate
        - approved
        - implemented
        - deprecated

    dependencies:
      description: "Must include PRD dependency"
      required_dependency_types: ["prd"]

required_sections:
  - name: "Executive Summary"
    pattern: "^## Executive Summary"
    mandatory: true

  - name: "System Architecture"
    pattern: "^## (System Architecture|Architecture Overview)"
    mandatory: true
    description: "High-level architecture diagram + explanation"

  - name: "Technology Stack"
    pattern: "^## (Technology Stack|Tech Stack)"
    mandatory: true
    description: "Libraries, frameworks, versions with rationale"

  - name: "Component Specifications"
    pattern: "^## Component(s| Specifications)"
    mandatory: true
    description: "Component breakdown with responsibilities"

  - name: "Data Models"
    pattern: "^## Data Model(s)?"
    mandatory: true
    description: "Database schemas, data structures"

  - name: "API Specifications"
    pattern: "^## API Spec(ifications)?"
    mandatory: true
    description: "Public interfaces, contracts"

  - name: "Performance Analysis"
    pattern: "^## Performance( Analysis)?"
    mandatory: true
    description: "Performance targets vs projections"

  - name: "Security Considerations"
    pattern: "^## Security( Considerations)?"
    mandatory: true
    description: "Threat model, mitigations"

gap_detection:
  E110:
    enabled: true
    severity: critical

  E120:
    enabled: true
    severity: high
    patterns: [TODO, TBD, PLACEHOLDER, FIXME]

  E130:
    enabled: true
    severity: high

  E140:
    enabled: true
    severity: critical

  E150:
    enabled: true
    severity: critical

  E170:
    enabled: true
    severity: medium
    min_evidence_notes: 15  # TDD needs more evidence

  E190:
    enabled: true
    severity: high
    description: "Architecture alternatives must be documented"

quality_gates:
  - name: "DESIGN-COMPLETE"
    status_trigger: "design-complete"
    conditions:
      - no_critical_gaps
      - no_high_gaps
      - all_sections_present: true
      - min_evidence_count: 15
      - architecture_reviewed: true
```

---

## ADR Schema

**File**: `schemas/adr.yaml`

```yaml
document_type: "adr"
version: "1.0"
description: "Architecture Decision Record"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - decision_date

  optional_fields:
    - parent
    - evidence_ids
    - alternatives
    - superseded_by

  constraints:
    id:
      pattern: "^ADR-\\d{3}$"
      examples: ["ADR-001", "ADR-042"]

    status:
      enum:
        - draft
        - review
        - approved      # Final decision made
        - deployed
        - rejected
        - deprecated
        - superseded
      description: "ADR statuses (immutable once approved)"

    decision_date:
      format: "date"
      description: "ISO date when decision was made"

required_sections:
  - name: "Context"
    pattern: "^## Context"
    mandatory: true
    description: "What is the issue we're facing?"

  - name: "Decision"
    pattern: "^## Decision"
    mandatory: true
    description: "What have we decided to do?"

  - name: "Consequences"
    pattern: "^## Consequences"
    mandatory: true
    description: "What are the positive and negative outcomes?"

  - name: "Alternatives"
    pattern: "^## Alternatives( Considered)?"
    mandatory: true
    description: "What other options did we evaluate? Why rejected?"

gap_detection:
  E110:
    enabled: true
    severity: critical
    description: "ADRs must have all 4 sections (Context, Decision, Consequences, Alternatives)"

  E120:
    enabled: true
    severity: high

  E170:
    enabled: true
    severity: high
    min_evidence_notes: 3  # ADR should back decisions with evidence

  E190:
    enabled: true
    severity: critical
    description: "Alternatives section MUST list rejected options with reasons"
    check_alternatives_present: true

quality_gates:
  - name: "ADR-APPROVED"
    status_trigger: "approved"
    conditions:
      - no_critical_gaps
      - alternatives_documented: true
      - evidence_count: 3  # Min 3 evidence notes
      - architect_approval: true
```

---

## Component Schema

**File**: `schemas/component.yaml`

```yaml
document_type: "component"
version: "1.0"
description: "Component Design Specification"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - parent

  optional_fields:
    - dependencies
    - impacts
    - evidence_ids

  constraints:
    id:
      pattern: "^COMP-\\d{3}-[a-z-]+$"
      examples: ["COMP-001-parser", "COMP-042-example-component"]

    status:
      enum: [draft, review, approved, implemented]

    parent:
      description: "Must reference TDD parent"
      pattern: "^TDD-"

required_sections:
  - name: "Public Interface"
    pattern: "^## Public Interface"
    mandatory: true
    description: "Public API with method signatures"

  - name: "Internal Architecture"
    pattern: "^## (Internal Architecture|Architecture)"
    mandatory: false
    description: "Internal component structure"

  - name: "Data Structures"
    pattern: "^## Data (Structures|Models)"
    mandatory: false

  - name: "Algorithms"
    pattern: "^## Algorithms"
    mandatory: false
    description: "Key algorithms with complexity analysis"

  - name: "Error Handling"
    pattern: "^## Error Handling"
    mandatory: true
    description: "Error scenarios and recovery"

  - name: "Performance"
    pattern: "^## Performance"
    mandatory: true
    description: "Performance targets and measurements"

  - name: "Testing"
    pattern: "^## Testing( Strategy)?"
    mandatory: true
    description: "Unit test approach"

gap_detection:
  E110:
    enabled: true
    severity: high

  E120:
    enabled: true
    severity: high

  E170:
    enabled: true
    severity: medium
    min_evidence_notes: 2
```

---

## RFC Schema

**File**: `schemas/rfc.yaml`

```yaml
document_type: "rfc"
version: "1.0"
description: "Request for Comments (Proposal)"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - author

  optional_fields:
    - reviewers
    - decision_deadline
    - alternatives

  constraints:
    id:
      pattern: "^RFC-\\d{3}$"

    status:
      enum:
        - draft
        - under-review
        - accepted
        - rejected
        - withdrawn

required_sections:
  - name: "Summary"
    pattern: "^## Summary"
    mandatory: true

  - name: "Motivation"
    pattern: "^## Motivation"
    mandatory: true

  - name: "Proposal"
    pattern: "^## (Proposal|Detailed Design)"
    mandatory: true

  - name: "Drawbacks"
    pattern: "^## Drawbacks"
    mandatory: true

  - name: "Alternatives"
    pattern: "^## Alternatives"
    mandatory: true

  - name: "Unresolved Questions"
    pattern: "^## Unresolved Questions"
    mandatory: false

gap_detection:
  E110:
    enabled: true
    severity: high

  E120:
    enabled: true
    severity: medium

  E190:
    enabled: true
    severity: high
    description: "RFCs must document alternatives"
```

---

## Vision Schema

**File**: `schemas/vision.yaml`

```yaml
document_type: "vision"
version: "1.0"
description: "Product Vision Document"

frontmatter:
  required_fields:
    - id
    - title
    - type
    - status
    - owner

  optional_fields:
    - timeline
    - dependencies
    - evidence_ids

  constraints:
    id:
      pattern: "^VISION-\\d{3}(-V\\d+)?$"

    status:
      enum: [draft, review, approved, archived]

required_sections:
  - name: "Vision Statement"
    pattern: "^## Vision( Statement)?"
    mandatory: true

  - name: "Target Users"
    pattern: "^## Target Users"
    mandatory: true

  - name: "Value Proposition"
    pattern: "^## Value Proposition"
    mandatory: true

  - name: "Roadmap"
    pattern: "^## Roadmap"
    mandatory: true

  - name: "Success Criteria"
    pattern: "^## Success Criteria"
    mandatory: true

gap_detection:
  E110:
    enabled: true
    severity: critical

  E120:
    enabled: true
    severity: high

  E170:
    enabled: true
    severity: medium
    min_evidence_notes: 5

  E180:
    enabled: true
    severity: medium
    description: "Vision needs storytelling, not just bullet points"
```

---

## Schema Loading

### Python Implementation

```python
# src/core/schema_loader.py

import yaml
from pathlib import Path
from models.schema import DocumentSchema
from typing import Optional

class SchemaLoader:
    """Load and cache document type schemas."""

    def __init__(self, schema_dir: Path):
        self.schema_dir = schema_dir
        self._cache: dict[str, DocumentSchema] = {}

    def load_schema(self, doc_type: str) -> Optional[DocumentSchema]:
        """
        Load schema for document type.

        Args:
            doc_type: Document type (prd, tdd, adr, etc.)

        Returns:
            DocumentSchema or None if schema not found
        """
        # Check cache
        if doc_type in self._cache:
            return self._cache[doc_type]

        # Load from YAML
        schema_path = self.schema_dir / f"{doc_type}.yaml"
        if not schema_path.exists():
            return None

        with open(schema_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # Parse to Pydantic model
        schema = DocumentSchema(**data)

        # Cache
        self._cache[doc_type] = schema
        return schema

    def list_available_types(self) -> list[str]:
        """List all available document types (schemas in directory)."""
        return [
            f.stem for f in self.schema_dir.glob("*.yaml")
            if f.stem != "template"
        ]
```

---

## Validation Example

```python
from core.schema_loader import SchemaLoader
from core.validator import ValidatorAPI
from core.parser import ParserAPI

# Load schema
loader = SchemaLoader(Path("schemas/"))
prd_schema = loader.load_schema("prd")

# Parse document
parser = ParserAPI()
doc = parser.parse_document(Path("docs/engineering/prd.md"))

# Validate against schema
validator = ValidatorAPI()
result = validator.validate_document(doc, prd_schema)

if not result.valid:
    for gap in result.gaps:
        print(f"{gap.gap_type} [{gap.severity}]: {gap.description}")
        for step in gap.remediation_steps:
            print(f"  → {step}")
```

---

## Schema Versioning

**Strategy**: Schema version in filename dla breaking changes.

```
schemas/
├── prd.yaml           # Latest (version 1.0)
├── prd-v2.yaml        # Future breaking change
├── tdd.yaml           # Latest
└── template.yaml      # Base template
```

**Migration path**:
1. Create `{type}-v2.yaml` with new schema
2. Update document frontmatter: `schema_version: "2.0"`
3. Validator loads versioned schema based on frontmatter
4. Deprecate old schema after 6 months

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [DATA-MODEL-001](DATA-MODEL-001.md), [COMP-002-validator](../components/COMP-002-validator.md)
