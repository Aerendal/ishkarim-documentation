---
id: DATA-MODEL-001
title: "DATA-MODEL-001: Data Models Specification"
type: data-model
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
owner: Tech Lead
parent: TDD-001-V2
decision_date: 2025-12-26

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-26"
  status_reason: "Data models approved - API-SPEC-001 and all components can use stable types"
  next_review_date: "2026-06-26"
  review_frequency: "semi-annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-26"
  last_modified: "2025-12-29"
  last_reviewed: "2025-12-29"
  sunset_date: null
  migration_target: null
  note: "Foundation data models - long-lived with semi-annual reviews"

# Version Metadata (Semantic Versioning)
version: "1.0.0"
version_metadata:
  major: 1
  minor: 0
  patch: 0
  breaking_changes: false
  backward_compatible_with: []
  note: "Data models approved and frozen - all components can use stable types"

version_history:
  - version: "1.0.0"
    date: "2025-12-26"
    author: "Tech Lead"
    type: "major"
    summary: "Data models approved - 9 core models + enums defined"
    breaking: false
    changes:
      - "Zdefiniowano Document model (Pydantic BaseModel z validation)"
      - "Zdefiniowano Section model (hierarchical sections H1-H6)"
      - "Zdefiniowano Gap model (E110-E200 gap types)"
      - "Zdefiniowano ValidationResult model (validator output)"
      - "Zdefiniowano GraphNode model (NetworkX node metadata)"
      - "Zdefiniowano GraphEdge model (typed edges: requires, informs, etc.)"
      - "Zdefiniowano DocumentSchema model (YAML schema loader)"
      - "Zdefiniowano ProvenanceRecord model (audit trail)"
      - "Zdefiniowano Enums (GapType, Severity, EdgeType, OperationType, DocumentStatus, Priority, Domain)"
      - "Performance: Pydantic validation 42μs/doc, <1ms serialization"
    impacts:
      - id: "API-SPEC-001"
        impact_type: "unblocked"
        description: "API-SPEC-001 może używać zdefiniowanych typów (Document, Gap, ValidationResult, etc.)"
      - id: "COMP-001-parser"
        impact_type: "unblocked"
        description: "Parser może zwracać Document i Section types"
      - id: "COMP-002-validator"
        impact_type: "unblocked"
        description: "Validator może zwracać ValidationResult i Gap types"
      - id: "COMP-003-graph"
        impact_type: "unblocked"
        description: "Graph Builder może używać GraphNode i GraphEdge metadata"
      - id: "COMP-004-gap-engine"
        impact_type: "unblocked"
        description: "Gap Engine może używać Gap i ValidationResult types"
      - id: "COMP-006-storage"
        impact_type: "unblocked"
        description: "Storage może używać ProvenanceRecord type"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending:
    - id: "ADR-003"
      change_type: "requires"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Tech Lead"
      acknowledged_date: "2025-12-26"
      note: "Data models use Pydantic 2.5+ (ADR-003 decision)"
    - id: "CONCEPTS-001-V2"
      change_type: "requires"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Tech Lead"
      acknowledged_date: "2025-12-26"
      note: "Models implement 18 system concepts - jeśli CONCEPTS-001-V2 nie istnieje, można usunąć dependency"
  downstream_impacts_pending:
    - id: "API-SPEC-001"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Tech Lead"
      acknowledged_date: "2025-12-26"
      note: "API-SPEC-001 może używać stabilnych typów - może rozpocząć implementację"
    - id: "COMP-001-parser"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Parser implementuje Document i Section models"
    - id: "COMP-002-validator"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Validator implementuje Gap, ValidationResult, DocumentSchema models"
    - id: "COMP-003-graph"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Graph Builder używa GraphNode, GraphEdge models"
    - id: "COMP-004-gap-engine"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Gap Engine używa Gap, ValidationResult models"
    - id: "COMP-006-storage"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Storage używa ProvenanceRecord model"

# Document Health
document_health:
  status: "warning"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 180
      days_since_modified: 3
      note: "Data models have longer freshness threshold (180 days) - reviewed semi-annually"

    - name: "Dependency Validity"
      status: "warning"
      invalid_dependencies:
        - "CONCEPTS-001-V2 (not found - may need to be created or removed)"
      all_dependencies_valid: false
      note: "CONCEPTS-001-V2 referenced ale nie znaleziony - opcjonalnie można usunąć dependency"

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
      note: "All 9 data models + enums defined (Document, Section, Gap, ValidationResult, GraphNode, GraphEdge, DocumentSchema, ProvenanceRecord, Enums)"

    - name: "Upstream Changes Pending"
      status: "warning"
      pending_changes: 1
      note: "Optional: Awaiting CONCEPTS-001-V2 (or can remove dependency)"

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      note: "Evidence E-145 (Pydantic benchmark), E-155 (type safety evaluation) support data model design"

# Deprecation
deprecation: null

dependencies:
  - id: "ADR-003"
    type: requires
    reason: "Uses Pydantic 2.5+ (ADR-003 decision)"

  - id: "CONCEPTS-001-V2"
    type: requires
    reason: "Models implement 18 system concepts"

evidence_ids:
  - "E-145"  # Pydantic benchmark (42μs/doc validation)
  - "E-155"  # Type safety evaluation
---

# DATA-MODEL-001: Data Models Specification

**Responsibility**: Pydantic models dla wszystkich danych systemowych, type-safe validation, serialization

---

## Spis Treści

1. [Core Models](#core-models) (Document, Section, Metadata)
2. [Validation Models](#validation-models) (Gap, ValidationResult)
3. [Graph Models](#graph-models) (Node, Edge, Hierarchy)
4. [Schema Models](#schema-models) (DocumentSchema, FieldConstraint)
5. [Storage Models](#storage-models) (ProvenanceRecord, IndexEntry)
6. [Enums](#enums) (Status, Severity, GapType)

---

## Core Models

### 1. Document

**Odpowiedzialność**: Główny model reprezentujący sparsowany dokument markdown.

```python
# src/models/document.py

from pydantic import BaseModel, Field, field_validator
from pathlib import Path
from datetime import datetime
from typing import Optional

class Document(BaseModel):
    """
    Parsed markdown document.

    Validation:
        - id must match pattern: [A-Z]+-[A-Z0-9]+-V?\d+
        - type must be valid document type
        - body cannot be empty
    """

    # Identifiers
    id: str = Field(
        ...,
        pattern=r'^[A-Z]+-[A-Z0-9]+(-V\d+)?$',
        description="Unique document ID (e.g., PRD-001-V2)",
        examples=["PRD-001-V2", "TDD-001", "ADR-005"]
    )

    title: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Human-readable title"
    )

    type: str = Field(
        ...,
        description="Document type (prd, tdd, adr, etc.)",
        examples=["prd", "tdd", "adr", "rfc", "component"]
    )

    # Metadata from frontmatter
    frontmatter: dict = Field(
        default_factory=dict,
        description="Full YAML frontmatter as dict"
    )

    status: Optional[str] = Field(
        default=None,
        description="Document status (draft, review, approved, etc.)"
    )

    domain: Optional[str] = Field(
        default=None,
        description="Logical domain (requirements, architecture, testing, etc.)"
    )

    owner: Optional[str] = Field(
        default=None,
        description="Owner/responsible person"
    )

    priority: Optional[str] = Field(
        default=None,
        description="Priority (critical, high, medium, low)"
    )

    # Content
    body: str = Field(
        ...,
        min_length=1,
        description="Markdown body (without frontmatter)"
    )

    sections: list['Section'] = Field(
        default_factory=list,
        description="Hierarchical section tree"
    )

    # References
    dependencies: list[dict] = Field(
        default_factory=list,
        description="Dependencies from frontmatter"
    )

    impacts: list[dict] = Field(
        default_factory=list,
        description="Impacts (what this doc affects)"
    )

    evidence_ids: list[str] = Field(
        default_factory=list,
        description="Evidence notes referenced ([E-XXX])",
        examples=[["E-001", "E-145", "E-168"]]
    )

    # File metadata
    file_path: Optional[Path] = Field(
        default=None,
        description="Absolute path to source .md file"
    )

    content_hash: Optional[str] = Field(
        default=None,
        description="SHA256 hash of body (for cache invalidation)",
        pattern=r'^[a-f0-9]{64}$'
    )

    last_modified: Optional[datetime] = Field(
        default=None,
        description="File modification timestamp"
    )

    line_count: int = Field(
        default=0,
        ge=0,
        description="Total lines in document"
    )

    # Computed properties (set by Gap Engine)
    gap_count: int = Field(
        default=0,
        ge=0,
        description="Total gaps detected in document"
    )

    severity_max: Optional[str] = Field(
        default=None,
        description="Highest gap severity (critical, high, medium, low)"
    )

    @field_validator('type')
    @classmethod
    def validate_type(cls, v: str) -> str:
        """Validate document type."""
        allowed_types = [
            'prd', 'tdd', 'adr', 'rfc', 'component',
            'vision', 'business-case', 'concepts',
            'implementation', 'test-plan', 'runbook'
        ]
        if v not in allowed_types:
            raise ValueError(f"Invalid document type: {v}. Must be one of {allowed_types}")
        return v

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        """Validate status if present."""
        if v is None:
            return v
        allowed_statuses = [
            'draft', 'in-progress', 'review',
            'req-freeze', 'design-complete', 'approved',
            'completed', 'archived', 'deprecated'
        ]
        if v not in allowed_statuses:
            raise ValueError(f"Invalid status: {v}")
        return v

    class Config:
        arbitrary_types_allowed = True  # For Path
        json_schema_extra = {
            "example": {
                "id": "PRD-001-V2",
                "title": "Product Requirements Document",
                "type": "prd",
                "status": "req-freeze",
                "body": "# Overview\n\nContent here.",
                "sections": [],
                "evidence_ids": ["E-140", "E-141"],
                "gap_count": 3,
                "severity_max": "high"
            }
        }
```

---

### 2. Section

**Odpowiedzialność**: Reprezentacja hierarchicznej sekcji markdown (H1-H6).

```python
# src/models/document.py

from pydantic import BaseModel, Field
from typing import Optional

class Section(BaseModel):
    """
    Markdown section (H1-H6) with hierarchical children.

    Hierarchy:
        - level 1 = H1, level 2 = H2, etc.
        - children = nested sections (e.g., H2 under H1)
        - parent = reference to parent section
    """

    level: int = Field(
        ...,
        ge=1,
        le=6,
        description="Heading level (1-6, where 1=H1)"
    )

    title: str = Field(
        ...,
        min_length=1,
        description="Section heading text (without # markers)"
    )

    content: str = Field(
        default="",
        description="Section body (markdown between this heading and next)"
    )

    line_start: int = Field(
        ...,
        ge=1,
        description="Starting line number in source file"
    )

    line_end: int = Field(
        ...,
        ge=1,
        description="Ending line number in source file"
    )

    children: list['Section'] = Field(
        default_factory=list,
        description="Nested child sections"
    )

    parent: Optional['Section'] = Field(
        default=None,
        description="Parent section (None for top-level)",
        exclude=True  # Avoid circular serialization
    )

    @property
    def depth(self) -> int:
        """Calculate nesting depth (0 for top-level)."""
        if self.parent is None:
            return 0
        return self.parent.depth + 1

    @property
    def word_count(self) -> int:
        """Count words in section content."""
        return len(self.content.split())

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "level": 2,
                "title": "System Architecture",
                "content": "The system uses layered architecture...",
                "line_start": 45,
                "line_end": 120,
                "children": []
            }
        }

# Update forward references
Document.model_rebuild()
Section.model_rebuild()
```

---

## Validation Models

### 3. Gap

**Odpowiedzialność**: Reprezentacja wykrytej luki (E110-E200).

```python
# src/models/gap.py

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class GapType(str, Enum):
    """Gap type enumeration (E110-E200)."""
    E110 = "E110"  # Missing required section
    E120 = "E120"  # Placeholder detected
    E130 = "E130"  # Missing evidence document
    E140 = "E140"  # Broken dependency
    E150 = "E150"  # Gate blocker
    E160 = "E160"  # Missing approval
    E170 = "E170"  # Missing evidence notes
    E180 = "E180"  # Missing storytelling
    E190 = "E190"  # Missing alternatives
    E200 = "E200"  # Missing post-mortem

class Severity(str, Enum):
    """Gap severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Gap(BaseModel):
    """
    Detected gap with remediation steps.

    Priority calculation:
        priority = severity_weight × impact_factor
        - severity_weight: critical=100, high=50, medium=20, low=5
        - impact_factor: blocks_cascade=3, critical_path=2, standard=1
    """

    gap_id: str = Field(
        ...,
        description="Unique gap identifier (format: {type}-{doc_id}-{detail})",
        examples=["E110-PRD-001-personas", "E140-TDD-001-ADR-005-status"]
    )

    gap_type: GapType = Field(
        ...,
        description="Gap type (E110-E200)"
    )

    severity: Severity = Field(
        ...,
        description="Severity level"
    )

    document_id: str = Field(
        ...,
        description="Document where gap was detected"
    )

    description: str = Field(
        ...,
        min_length=1,
        description="Human-readable description of gap"
    )

    location: Optional[str] = Field(
        default=None,
        description="Location in document (e.g., 'Line 45', 'Section 3.2')"
    )

    remediation_steps: list[str] = Field(
        default_factory=list,
        description="Actionable steps to fix gap"
    )

    evidence: list[str] = Field(
        default_factory=list,
        description="Evidence backing the gap detection"
    )

    # Priority metadata
    blocks_cascade: bool = Field(
        default=False,
        description="True if gap blocks other documents (cascade effect)"
    )

    on_critical_path: bool = Field(
        default=False,
        description="True if gap is on project critical path"
    )

    priority_score: int = Field(
        default=0,
        ge=0,
        description="Computed priority (severity × impact)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "gap_id": "E110-PRD-001-personas",
                "gap_type": "E110",
                "severity": "critical",
                "document_id": "PRD-001-V2",
                "description": "Missing required section: User Personas",
                "location": "Expected at line 100-200",
                "remediation_steps": [
                    "Add section matching pattern: ^## User Personas",
                    "Use template: templates/prd-template.md"
                ],
                "blocks_cascade": True,
                "priority_score": 300
            }
        }
```

---

### 4. ValidationResult

**Odpowiedzialność**: Wynik walidacji dokumentu.

```python
# src/models/gap.py

from pydantic import BaseModel, Field

class ValidationResult(BaseModel):
    """
    Result of document validation.

    Usage:
        result = validator.validate_document(doc, schema)
        if result.valid:
            print("Document valid!")
        else:
            for gap in result.gaps:
                print(f"Gap: {gap.description}")
    """

    valid: bool = Field(
        ...,
        description="True if document passes all validations"
    )

    document_id: str = Field(
        ...,
        description="Document that was validated"
    )

    gaps: list[Gap] = Field(
        default_factory=list,
        description="Detected gaps (empty if valid=True)"
    )

    errors: list[str] = Field(
        default_factory=list,
        description="Validation errors (technical failures, not gaps)"
    )

    warnings: list[str] = Field(
        default_factory=list,
        description="Non-blocking warnings"
    )

    @property
    def critical_gaps(self) -> list[Gap]:
        """Filter critical severity gaps."""
        return [g for g in self.gaps if g.severity == Severity.CRITICAL]

    @property
    def high_gaps(self) -> list[Gap]:
        """Filter high severity gaps."""
        return [g for g in self.gaps if g.severity == Severity.HIGH]

    class Config:
        json_schema_extra = {
            "example": {
                "valid": False,
                "document_id": "PRD-001-V2",
                "gaps": [],  # Gap examples above
                "errors": [],
                "warnings": ["Section 'Use Cases' is very short (50 words)"]
            }
        }
```

---

## Graph Models

### 5. GraphNode

**Odpowiedzialność**: Węzeł w grafie zależności (metadata dokumentu).

```python
# src/models/graph.py

from pydantic import BaseModel, Field
from typing import Optional

class GraphNode(BaseModel):
    """
    Node in dependency graph.

    Note: Actual graph uses NetworkX DiGraph.
    This model defines node metadata stored as node attributes.
    """

    node_id: str = Field(
        ...,
        description="Document ID (unique node identifier)"
    )

    doc_type: str = Field(
        ...,
        description="Document type (prd, tdd, etc.)"
    )

    title: str = Field(
        ...,
        description="Document title"
    )

    status: Optional[str] = Field(
        default=None,
        description="Document status"
    )

    file_path: Optional[str] = Field(
        default=None,
        description="Path to source file"
    )

    # Computed properties
    gap_count: int = Field(
        default=0,
        ge=0,
        description="Total gaps in document"
    )

    severity_max: Optional[str] = Field(
        default=None,
        description="Highest gap severity"
    )

    hierarchy_level: int = Field(
        default=0,
        ge=0,
        description="Emergent hierarchy level (0=root)"
    )

    last_modified: Optional[str] = Field(
        default=None,
        description="ISO timestamp of last modification"
    )

    # Ghost node (broken dependency)
    ghost: bool = Field(
        default=False,
        description="True if node represents non-existent document"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "node_id": "PRD-001-V2",
                "doc_type": "prd",
                "title": "Product Requirements",
                "status": "req-freeze",
                "gap_count": 3,
                "severity_max": "high",
                "hierarchy_level": 2,
                "ghost": False
            }
        }
```

---

### 6. GraphEdge

**Odpowiedzialność**: Krawędź w grafie (typowane połączenie).

```python
# src/models/graph.py

from pydantic import BaseModel, Field
from enum import Enum

class EdgeType(str, Enum):
    """Typed edge relationships."""
    REQUIRES = "requires"        # Hard dependency
    INFORMS = "informs"          # Context dependency
    IMPLEMENTS = "implements"    # Implementation relationship
    TESTS = "tests"              # Test coverage
    EVIDENCED_BY = "evidenced-by"  # Evidence backing
    ALTERNATIVE_TO = "alternative-to"  # Decision alternative

class GraphEdge(BaseModel):
    """
    Edge in dependency graph.

    Note: Actual graph uses NetworkX DiGraph.
    This model defines edge metadata stored as edge attributes.
    """

    source: str = Field(
        ...,
        description="Source document ID"
    )

    target: str = Field(
        ...,
        description="Target document ID"
    )

    edge_type: EdgeType = Field(
        ...,
        description="Relationship type"
    )

    reason: Optional[str] = Field(
        default=None,
        description="Human-readable reason for dependency"
    )

    cascade: bool = Field(
        default=False,
        description="True if changes propagate through this edge"
    )

    status_constraint: list[str] = Field(
        default_factory=list,
        description="Required target statuses (e.g., ['req-freeze', 'approved'])"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "source": "PRD-001-V2",
                "target": "TDD-001-V2",
                "edge_type": "requires",
                "reason": "Design cannot start without frozen requirements",
                "cascade": True,
                "status_constraint": ["req-freeze", "approved"]
            }
        }
```

---

## Schema Models

### 7. DocumentSchema

**Odpowiedzialność**: Schema definition dla document type.

```python
# src/models/schema.py

from pydantic import BaseModel, Field
from typing import Optional

class RequiredSection(BaseModel):
    """Required section definition."""

    name: str = Field(..., description="Section name")
    pattern: str = Field(..., description="Regex pattern for matching heading")
    mandatory: bool = Field(default=True, description="True if section required")
    min_items: Optional[int] = Field(default=None, description="Min items in section (e.g., min FR count)")

class FieldConstraint(BaseModel):
    """Frontmatter field constraint."""

    field_name: str = Field(..., description="Field name")
    required: bool = Field(default=False, description="True if field required")
    enum_values: Optional[list[str]] = Field(default=None, description="Allowed values (enum)")
    pattern: Optional[str] = Field(default=None, description="Regex pattern")
    min_length: Optional[int] = Field(default=None)
    max_length: Optional[int] = Field(default=None)

class DocumentSchema(BaseModel):
    """
    Schema for validating document type.

    Loaded from: schemas/{doc_type}.yaml
    """

    document_type: str = Field(
        ...,
        description="Document type (prd, tdd, etc.)"
    )

    version: str = Field(
        default="1.0",
        description="Schema version"
    )

    # Frontmatter rules
    required_fields: list[str] = Field(
        default_factory=list,
        description="Required frontmatter fields"
    )

    optional_fields: list[str] = Field(
        default_factory=list,
        description="Optional frontmatter fields"
    )

    field_constraints: list[FieldConstraint] = Field(
        default_factory=list,
        description="Field validation constraints"
    )

    # Content rules
    required_sections: list[RequiredSection] = Field(
        default_factory=list,
        description="Required markdown sections"
    )

    # Gap detection config
    gap_detection: dict = Field(
        default_factory=dict,
        description="Gap detection configuration per type"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "document_type": "prd",
                "version": "1.0",
                "required_fields": ["id", "title", "type", "status"],
                "required_sections": [
                    {"name": "User Personas", "pattern": "^## User Personas", "mandatory": True}
                ],
                "gap_detection": {
                    "E110": {"enabled": True, "severity": "critical"},
                    "E120": {"enabled": True, "patterns": ["TODO", "TBD"]}
                }
            }
        }
```

---

## Storage Models

### 8. ProvenanceRecord

**Odpowiedzialność**: Provenance tracking (audit trail).

```python
# src/models/provenance.py

from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class OperationType(str, Enum):
    """Provenance operation types."""
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

class ProvenanceRecord(BaseModel):
    """
    Provenance record for document change tracking.

    Stored in SQLite provenance table.
    """

    id: Optional[int] = Field(
        default=None,
        description="Auto-increment ID (SQLite rowid)"
    )

    doc_id: str = Field(
        ...,
        description="Document ID"
    )

    operation: OperationType = Field(
        ...,
        description="Operation type"
    )

    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="Operation timestamp"
    )

    user: Optional[str] = Field(
        default=None,
        description="User who performed operation"
    )

    content_hash: Optional[str] = Field(
        default=None,
        description="SHA256 hash of content after operation"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "doc_id": "PRD-001-V2",
                "operation": "UPDATE",
                "timestamp": "2025-12-26T10:30:00",
                "user": "tech-lead",
                "content_hash": "a3f5..."
            }
        }
```

---

## Enums

### 9. Status Enum

```python
# src/models/enums.py

from enum import Enum

class DocumentStatus(str, Enum):
    """Document lifecycle statuses."""
    DRAFT = "draft"
    IN_PROGRESS = "in-progress"
    REVIEW = "review"
    REQ_FREEZE = "req-freeze"
    DESIGN_COMPLETE = "design-complete"
    APPROVED = "approved"
    COMPLETED = "completed"
    ARCHIVED = "archived"
    DEPRECATED = "deprecated"

class Priority(str, Enum):
    """Priority levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Domain(str, Enum):
    """Logical domains."""
    REQUIREMENTS = "requirements"
    ARCHITECTURE = "architecture"
    IMPLEMENTATION = "implementation"
    TESTING = "testing"
    OPERATIONS = "operations"
    DOCUMENTATION = "documentation"
```

---

## Relationships Diagram

```
┌──────────────┐
│   Document   │◄────┐
│              │     │
│ - id         │     │ contains
│ - title      │     │
│ - sections   │─────┘
│ - gaps       │────┐
└──────────────┘    │
                    │ references
                    ↓
              ┌──────────┐
              │   Gap    │
              │          │
              │ - type   │
              │ - severity│
              └──────────┘

┌──────────────┐         ┌──────────────┐
│  GraphNode   │◄────────│  GraphEdge   │
│              │  source │              │
│ - node_id    │         │ - edge_type  │
│ - doc_type   │  target │ - reason     │
└──────────────┘────────►└──────────────┘

┌──────────────────┐
│ DocumentSchema   │
│                  │
│ - required_fields│
│ - sections       │
└──────────────────┘

┌──────────────────┐
│ProvenanceRecord  │
│                  │
│ - operation      │
│ - timestamp      │
└──────────────────┘
```

---

## Performance

**Validation performance** [E-145]:
- Pydantic validation: 42μs per document
- Type checking: 0 runtime overhead (mypy static analysis)
- Serialization: < 1ms per document

**Memory efficiency**:
- Document model: ~2KB per instance (excluding body content)
- Gap model: ~500 bytes per instance
- Total dla 1000 docs + 5000 gaps: ~5MB (negligible)

---

## Testing

```python
def test_document_validation():
    from models.document import Document

    # Valid document
    doc = Document(
        id="TEST-001",
        title="Test Document",
        type="test",
        body="# Content\n\nTest content."
    )
    assert doc.id == "TEST-001"

    # Invalid ID pattern
    with pytest.raises(ValidationError):
        Document(id="invalid-id", title="Test", type="test", body="Content")

    # Invalid type
    with pytest.raises(ValidationError):
        Document(id="TEST-001", title="Test", type="invalid-type", body="Content")

def test_gap_priority():
    from models.gap import Gap, GapType, Severity

    gap = Gap(
        gap_id="E110-TEST",
        gap_type=GapType.E110,
        severity=Severity.CRITICAL,
        document_id="TEST-001",
        description="Test gap",
        blocks_cascade=True
    )

    # Priority = severity (100) × impact (3) = 300
    assert gap.blocks_cascade is True
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-003](../decisions/ADR-003-validation.md)
