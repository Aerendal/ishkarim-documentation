---
id: COMP-003
title: "COMP-003: Graph Builder Component"
type: component
status: draft
parent: TDD-001-V2

dependencies:
  - id: "COMP-001-parser"
    type: requires
    reason: "Graph built from parsed Documents"

  - id: "ADR-004"
    type: requires
    reason: "Uses NetworkX (ADR-004 decision)"

  - id: "API-SPEC-001"
    type: implements
    reason: "Graph Builder implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

evidence_ids:
  - "E-143"  # NetworkX benchmark (800ms dla 100 nodes)
---

# COMP-003: Graph Builder Component

**Responsibility**: Build dependency graph (NetworkX DiGraph) from documents, detect cycles, calculate hierarchy

---

## Public Interface

```python
# src/core/graph_builder.py

import networkx as nx
from models.document import Document
from typing import Optional

class GraphBuilderAPI:
    """Dependency graph construction and analysis."""

    def build_graph(self, docs: list[Document]) -> nx.DiGraph:
        """
        Build directed graph from documents.

        Nodes = documents (metadata: type, status, gaps)
        Edges = dependencies (typed: requires, informs, implements)

        Returns:
            nx.DiGraph with full metadata
        """

    def add_document(self, graph: nx.DiGraph, doc: Document) -> None:
        """Add single document to existing graph (incremental update)."""

    def remove_document(self, graph: nx.DiGraph, doc_id: str) -> None:
        """Remove document from graph."""

    def detect_cycles(self, graph: nx.DiGraph) -> list[list[str]]:
        """
        Detect circular dependencies.

        Returns:
            List of cycles, e.g., [["PRD-001", "TDD-001", "PRD-001"], ...]
        """

    def calculate_hierarchy(self, graph: nx.DiGraph) -> dict[str, int]:
        """
        Calculate emergent hierarchy levels.

        Returns:
            {doc_id: level}, where level = max(parent_levels) + 1
        """

    def find_path(self, graph: nx.DiGraph, source: str, target: str) -> Optional[list[str]]:
        """Find shortest dependency path between documents."""

    def get_subgraph(self, graph: nx.DiGraph, doc_ids: list[str]) -> nx.DiGraph:
        """Extract subgraph containing only specified documents."""
```

---

## Graph Structure

### Node Attributes

```python
graph.nodes['PRD-001'] = {
    'doc_type': 'prd',
    'status': 'req-freeze',
    'title': 'Product Requirements Document',
    'file_path': '/docs/engineering/prd-v2.md',
    'gap_count': 3,
    'severity_max': 'high',
    'last_modified': '2025-12-26T10:00:00',
}
```

### Edge Attributes

```python
graph['PRD-001']['TDD-001'] = {
    'edge_type': 'requires',  # requires, informs, implements, tests, evidenced-by
    'reason': 'Design cannot start without frozen requirements',
    'cascade': True,  # Impact propagation
}
```

---

## Algorithms

### Cycle Detection (NetworkX)

```python
def detect_cycles(self, graph: nx.DiGraph) -> list[list[str]]:
    """
    Uses NetworkX simple_cycles (Johnson's algorithm).
    Complexity: O(V + E + C) where C = number of cycles
    """
    try:
        cycles = list(nx.simple_cycles(graph))
        return cycles
    except nx.NetworkXError:
        return []  # No cycles (DAG)
```

**Evidence**: [E-143] Benchmark: 100 nodes + 200 edges → 800ms (includes cycle detection)

### Hierarchy Calculation (Topological Sort)

```python
def calculate_hierarchy(self, graph: nx.DiGraph) -> dict[str, int]:
    """
    Level = max(parent_levels) + 1 (emergent hierarchy).

    Example:
        EXEC-SUM → BIZ-CASE → PRD → TDD
        Levels:  0         1       2     3
    """
    hierarchy = {}

    # Handle orphan nodes (no dependencies)
    for node in graph.nodes():
        if graph.in_degree(node) == 0:
            hierarchy[node] = 0

    # Topological sort (BFS-based)
    for node in nx.topological_sort(graph):
        if node not in hierarchy:
            parent_levels = [hierarchy[p] for p in graph.predecessors(node)]
            hierarchy[node] = max(parent_levels, default=0) + 1

    return hierarchy
```

---

## Incremental Updates

**Problem**: Re-building entire graph on every file change = slow (for 1000+ docs)

**Solution**: Incremental updates

```python
def add_document(self, graph: nx.DiGraph, doc: Document) -> None:
    """
    Add/update single document without full rebuild.

    Steps:
    1. Remove old node (if exists)
    2. Add new node with metadata
    3. Parse dependencies from frontmatter
    4. Add edges
    5. Re-calculate hierarchy (only affected nodes)
    """
    # Remove old
    if doc.id in graph:
        graph.remove_node(doc.id)

    # Add node
    graph.add_node(doc.id, **self._extract_metadata(doc))

    # Add edges
    for dep in doc.frontmatter.get('dependencies', []):
        graph.add_edge(dep['id'], doc.id, edge_type='requires', ...)

    # Re-calculate hierarchy (incremental)
    self._update_hierarchy_incremental(graph, doc.id)
```

**Performance**: Single doc update ~10ms (vs full rebuild 800ms dla 100 docs)

---

## Error Handling

### Broken References

**Problem**: Document references non-existent dependency (e.g., PRD → ADR-999 but ADR-999 doesn't exist)

**Handling**: Create "ghost node" (placeholder)

```python
if target_id not in graph.nodes():
    # Add ghost node
    graph.add_node(target_id, ghost=True, status='missing')
    # Edge still created (shows broken dependency in viz)
```

**Gap Engine** detects ghost nodes → E140 gap (broken dependency)

---

## Testing

```python
def test_build_graph():
    docs = [
        Document(id="PRD-001", frontmatter={'dependencies': []}),
        Document(id="TDD-001", frontmatter={'dependencies': [{'id': 'PRD-001'}]}),
    ]

    graph = GraphBuilderAPI().build_graph(docs)

    assert len(graph.nodes()) == 2
    assert len(graph.edges()) == 1
    assert graph.has_edge('PRD-001', 'TDD-001')

def test_cycle_detection():
    graph = nx.DiGraph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')  # Cycle: A → B → C → A

    builder = GraphBuilderAPI()
    cycles = builder.detect_cycles(graph)

    assert len(cycles) == 1
    assert 'A' in cycles[0] and 'B' in cycles[0] and 'C' in cycles[0]
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-004](../decisions/ADR-004-graph-viz.md)
