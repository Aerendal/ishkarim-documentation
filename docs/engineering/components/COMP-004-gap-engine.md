---
id: COMP-004
title: "COMP-004: Gap Detection Engine"
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
    summary: "Initial component specification for Gap Detection Engine"
    breaking: false
    changes:
      - "Zdefiniowano public API (GapEngineAPI class)"
      - "Określono all 10 gap types (E110-E200)"
      - "Zdefiniowano gap detection logic (validator-based + graph-based)"
      - "Określono remediation generation templates"
      - "Określono prioritization algorithm (severity × impact)"
      - "Benchmark: 1.26s dla 100 docs (E-168)"
    impacts:
      - id: "COMP-005-gui"
        impact_type: "informs"
        description: "GUI wyświetla gaps w GapsPanel"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending:
    - id: "COMP-002-validator"
      change_type: "requires"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Gap Engine requires Validator for E110, E120, E170, E180, E190, E200"
    - id: "COMP-003-graph"
      change_type: "requires"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "Gap Engine requires Graph Builder for E130, E140, E150, E160"
  downstream_impacts_pending:
    - id: "COMP-005-gui"
      notified_date: "2025-12-26"
      acknowledged: true
      acknowledged_by: "Component Developers"
      acknowledged_date: "2025-12-26"
      note: "GUI czeka na Gap list format dla GapsPanel"

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
      pending_changes: 2
      note: "Blocked by COMP-002-validator and COMP-003-graph"

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      note: "Evidence E-168 supports gap detection performance"

# Deprecation
deprecation: null

dependencies:
  - id: "COMP-002-validator"
    type: requires
    reason: "Validator detects E110, E120, E170, E180, E190, E200"

  - id: "COMP-003-graph"
    type: requires
    reason: "Graph analysis detects E130, E140, E150, E160"

  - id: "API-SPEC-001"
    type: implements
    reason: "Gap Engine implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

evidence_ids:
  - "E-168"  # Gap detection performance benchmark
---

# COMP-004: Gap Detection Engine

**Responsibility**: Detect all 10 gap types (E110-E200), generate remediation, prioritize

---

## Gap Type Overview

| Gap Type | Name | Source | Severity |
|----------|------|--------|----------|
| **E110** | Missing required section | Validator | Critical |
| **E120** | Placeholder detected (TODO/TBD) | Validator | High |
| **E130** | Missing evidence document | Graph | High |
| **E140** | Broken dependency | Graph | Critical |
| **E150** | Gate blocker | Graph | Critical |
| **E160** | Missing approval | Graph | High |
| **E170** | Missing evidence notes ([E-XXX]) | Validator | Medium |
| **E180** | Missing storytelling | Validator | Medium |
| **E190** | Missing alternatives (decision docs) | Validator | High |
| **E200** | Missing post-mortem | Validator | Low |

---

## Public Interface

```python
# src/core/gap_engine.py

from models.document import Document
from models.gap import Gap
from models.graph import nx.DiGraph

class GapEngineAPI:
    """Comprehensive gap detection and remediation."""

    def detect_all_gaps(
        self,
        docs: list[Document],
        graph: nx.DiGraph
    ) -> list[Gap]:
        """
        Detect all gap types (E110-E200).

        Returns:
            Sorted list of gaps (by severity: critical > high > medium > low)
        """

    def detect_graph_gaps(self, graph: nx.DiGraph) -> list[Gap]:
        """E130, E140, E150, E160 (graph-based gaps)."""

    def detect_validator_gaps(self, docs: list[Document]) -> list[Gap]:
        """E110, E120, E170, E180, E190, E200 (validator gaps)."""

    def generate_remediation(self, gap: Gap) -> list[str]:
        """
        Generate actionable remediation steps for gap.

        Returns:
            List of steps (e.g., ["Create document ADR-005", "Update PRD frontmatter"])
        """

    def prioritize_gaps(self, gaps: list[Gap]) -> list[Gap]:
        """
        Sort gaps by priority (severity + impact).

        Priority = severity_weight × impact_factor
        """

    def generate_todo_list(self, gaps: list[Gap]) -> str:
        """
        Generate TODO.md document from gaps.

        Format: Markdown checklist grouped by document.
        """
```

---

## Gap Detection Logic

### E130: Missing Evidence Document

```python
def detect_e130(self, graph: nx.DiGraph) -> list[Gap]:
    """
    Detect references to non-existent evidence documents.

    Example:
        PRD frontmatter: evidence_ids: ["E-001", "E-002"]
        But E-002.md doesn't exist → E130 gap
    """
    gaps = []

    for node_id in graph.nodes():
        node_data = graph.nodes[node_id]
        evidence_refs = node_data.get('evidence_ids', [])

        for evidence_id in evidence_refs:
            # Check if evidence document exists
            if not self._evidence_exists(evidence_id):
                gaps.append(Gap(
                    gap_id=f"E130-{node_id}-{evidence_id}",
                    gap_type="E130",
                    severity="high",
                    document_id=node_id,
                    description=f"Missing evidence document: {evidence_id}",
                    remediation_steps=[
                        f"Create evidence note: docs/evidence/{evidence_id}.md",
                        f"Or remove reference from {node_id} frontmatter"
                    ]
                ))

    return gaps
```

### E140: Broken Dependency

```python
def detect_e140(self, graph: nx.DiGraph) -> list[Gap]:
    """
    Detect references to non-existent or wrong-status dependencies.

    Examples:
        1. PRD → ADR-999 (ADR-999 doesn't exist)
        2. TDD depends on PRD (status: req-freeze) but PRD status = draft
    """
    gaps = []

    for source, target in graph.edges():
        edge_data = graph[source][target]

        # Check 1: Target exists?
        if graph.nodes[target].get('ghost', False):
            gaps.append(Gap(
                gap_id=f"E140-{source}-{target}",
                gap_type="E140",
                severity="critical",
                description=f"{source} references non-existent {target}",
                remediation_steps=[f"Create document {target}", f"Or remove dependency from {source}"]
            ))

        # Check 2: Status constraint met?
        if 'status_constraint' in edge_data:
            target_status = graph.nodes[target].get('status')
            required_statuses = edge_data['status_constraint']

            if target_status not in required_statuses:
                gaps.append(Gap(
                    gap_id=f"E140-{source}-{target}-status",
                    gap_type="E140",
                    severity="critical",
                    description=f"{source} requires {target} status in {required_statuses}, but current status is {target_status}",
                    remediation_steps=[f"Update {target} to status: {required_statuses[0]}"]
                ))

    return gaps
```

### E150: Gate Blocker

```python
def detect_e150(self, graph: nx.DiGraph) -> list[Gap]:
    """
    Detect blocked quality gates.

    Example:
        PRD has gate: REQ-FREEZE
        Blockers:
            - E110 gaps present (missing sections)
            - E120 gaps present (placeholders)
            - Missing stakeholder approvals
    """
    gaps = []

    for node_id in graph.nodes():
        node_data = graph.nodes[node_id]
        gates = node_data.get('gates', [])

        for gate in gates:
            blockers = self._check_gate_blockers(node_id, gate, graph)

            if blockers:
                gaps.append(Gap(
                    gap_id=f"E150-{node_id}-{gate['name']}",
                    gap_type="E150",
                    severity="critical",
                    description=f"Gate '{gate['name']}' blocked for {node_id}",
                    location=f"Blockers: {', '.join(blockers)}",
                    remediation_steps=[f"Resolve blocker: {b}" for b in blockers]
                ))

    return gaps
```

---

## Remediation Generation

### Remediation Templates

```python
REMEDIATION_TEMPLATES = {
    'E110': [
        "Add section matching pattern: {pattern}",
        "Use template: templates/{doc_type}-template.md",
        "See example: {example_doc}"
    ],
    'E120': [
        "Replace placeholder '{placeholder}' at line {line}",
        "Fill in actual content or remove TODO marker"
    ],
    'E130': [
        "Create evidence note: docs/evidence/{evidence_id}.md",
        "Use template: templates/evidence-note-template.md"
    ],
    'E140': [
        "Create missing document: {target_doc}",
        "Or remove dependency from {source_doc} frontmatter",
        "Or update {target_doc} status to: {required_status}"
    ],
    'E150': [
        "Resolve blockers: {blocker_list}",
        "Run validation: semantic-docs validate {doc_id}",
        "Obtain approvals: {approval_list}"
    ],
}

def generate_remediation(self, gap: Gap) -> list[str]:
    """Fill remediation templates with gap-specific data."""
    template = REMEDIATION_TEMPLATES.get(gap.gap_type, [])
    return [step.format(**gap.dict()) for step in template]
```

---

## Prioritization Algorithm

```python
SEVERITY_WEIGHTS = {
    'critical': 100,
    'high': 50,
    'medium': 20,
    'low': 5,
}

def prioritize_gaps(self, gaps: list[Gap]) -> list[Gap]:
    """
    Priority = severity_weight × impact_factor

    Impact factor:
        - Blocks other documents (cascade) → ×3
        - Affects critical path → ×2
        - Standard → ×1
    """
    def priority_score(gap: Gap) -> int:
        severity = SEVERITY_WEIGHTS.get(gap.severity, 1)

        # Check if gap blocks other docs (cascade)
        impact = 1
        if self._blocks_cascade(gap):
            impact = 3
        elif self._on_critical_path(gap):
            impact = 2

        return severity * impact

    return sorted(gaps, key=priority_score, reverse=True)
```

---

## TODO Generation

```python
def generate_todo_list(self, gaps: list[Gap]) -> str:
    """
    Generate TODO.md from gaps.

    Format:
        # TODO List (Generated from Gaps)

        ## PRD-001-V2 (3 gaps)
        - [ ] **[E110-CRITICAL]** Add section: User Personas
        - [ ] **[E120-HIGH]** Replace TODO at line 45
        - [ ] **[E170-MEDIUM]** Add 3 more evidence notes

        ## TDD-001-V2 (1 gap)
        - [ ] **[E140-CRITICAL]** Create ADR-005 or remove dependency
    """
    # Group gaps by document
    by_doc = defaultdict(list)
    for gap in gaps:
        by_doc[gap.document_id].append(gap)

    # Generate markdown
    lines = ["# TODO List (Generated from Gaps)\n"]

    for doc_id in sorted(by_doc.keys()):
        doc_gaps = by_doc[doc_id]
        lines.append(f"\n## {doc_id} ({len(doc_gaps)} gaps)\n")

        for gap in sorted(doc_gaps, key=lambda g: SEVERITY_WEIGHTS[g.severity], reverse=True):
            lines.append(f"- [ ] **[{gap.gap_type}-{gap.severity.upper()}]** {gap.description}")
            for step in gap.remediation_steps:
                lines.append(f"  - {step}")

    return "\n".join(lines)
```

---

## Performance

**Target**: < 2s dla 100 documents (NFR)

**Measured** [E-168]:
- E110-E200 detection: ~1.2s dla 100 docs
- Remediation generation: ~50ms dla 100 gaps
- Prioritization: ~10ms
- **Total**: ~1.26s ✅

---

## Testing

```python
def test_e140_broken_dependency():
    graph = nx.DiGraph()
    graph.add_node('PRD-001', status='draft')
    graph.add_node('TDD-001')
    graph.add_edge('PRD-001', 'TDD-001', status_constraint=['req-freeze'])

    engine = GapEngineAPI()
    gaps = engine.detect_e140(graph)

    assert len(gaps) == 1
    assert gaps[0].gap_type == "E140"
    assert "status" in gaps[0].description

def test_prioritization():
    gaps = [
        Gap(gap_type="E120", severity="high", document_id="PRD-001"),
        Gap(gap_type="E110", severity="critical", document_id="PRD-001"),
        Gap(gap_type="E170", severity="medium", document_id="TDD-001"),
    ]

    engine = GapEngineAPI()
    sorted_gaps = engine.prioritize_gaps(gaps)

    assert sorted_gaps[0].gap_type == "E110"  # Critical first
    assert sorted_gaps[1].gap_type == "E120"  # High second
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
