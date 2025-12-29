---
id: ADR-004
title: "ADR-004: Graph Visualization"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-19
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-19"
  status_reason: "Decision approved after prototyping - NetworkX + Cytoscape.js selected"
  next_review_date: "2026-12-19"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-19"
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
  note: "ADR approved - establishes graph analysis and visualization libraries"

version_history:
  - version: "1.0.0"
    date: "2025-12-19"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: NetworkX + Cytoscape.js for graph processing and viz"
    breaking: false
    changes:
      - "Evaluated 4 options: D3.js, vis.js, Cytoscape.js, igraph"
      - "Selected NetworkX 3.2+ (Python algorithms) + Cytoscape.js 3.26+ (JS viz)"
      - "Rejected D3.js (too low-level, need custom layouts)"
      - "Rejected vis.js (less maintained, last release 2021)"
    impacts:
      - id: "COMP-003-graph"
        impact_type: "unblocked"
        description: "Graph component can proceed with NetworkX + Cytoscape.js"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes dual graph libraries (Python + JS)"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-003-graph"
      notified_date: "2025-12-19"
      acknowledged: true
      acknowledged_by: "Graph Developer"
      acknowledged_date: "2025-12-19"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 10
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
      note: "Evidence E-143, E-148, E-165 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "TDD-001-V2"
    type: requires
    reason: "Graph visualization requirements defined in TDD"
  - id: "ADR-001"
    type: related
    reason: "QtWebEngine (from PySide6) needed to embed Cytoscape.js"

impacts:
  - id: "COMP-003-graph"
    type: blocks
    until: "ADR-004.status == approved"
    reason: "Graph implementation needs library choices"
  - id: "TDD-001-V2"
    type: informs
    reason: "Architecture updated with graph libraries"

context_snapshot:
  date: "2025-12-19"
  requirements:
    - "Python library: Rich algorithms (cycle detection, DAG)"
    - "Visualization: Interactive (zoom, pan, drag), handles 1000+ nodes"
    - "Performance: < 2s build dla 100 nodes (NFR-002)"

evidence_ids:
  - "E-143"  # NetworkX benchmark (800ms dla 100 nodes)
  - "E-148"  # Cytoscape.js prototype (1000 nodes interactive)
  - "E-165"  # D3.js evaluation (powerful but complex)

alternatives:
  - id: "OPT-D3JS"
    title: "D3.js (data visualization)"
    status: rejected
    reason: "Powerful but low-level (need write layout algorithms). Cytoscape.js has built-in graph layouts."

  - id: "OPT-VISJS"
    title: "vis.js (network viz)"
    status: rejected
    reason: "Less maintained (last release 2021), smaller community, fewer layouts"

  - id: "OPT-CYTOSCAPE"
    title: "Cytoscape.js + NetworkX"
    status: selected
    reason: "Cytoscape.js = best graph viz (1000+ nodes, rich layouts). NetworkX = Python graph algorithms."
---

# ADR-004: Graph Visualization & Analysis

**Decision**: Use **NetworkX 3.2+** (Python) + **Cytoscape.js 3.26+** (JavaScript viz)

**Status**: ✅ APPROVED

---

## Context

**Problem**:
1. **Graph analysis** (Python): Cycle detection, hierarchy, shortest path
2. **Graph visualization** (GUI): Interactive, 1000+ nodes, layouts

**Requirements**:
1. Python library: Rich algorithms (cycle detection, DAG)
2. Visualization: Interactive (zoom, pan, drag), handles 1000+ nodes
3. Performance: < 2s build dla 100 nodes (NFR-002)

---

## Decision

### NetworkX 3.2+ (Python) ✅

**Why**:
- ✅ **Rich algorithms**: `simple_cycles()`, `topological_sort()`, `shortest_path()`, `subgraph()`
- ✅ **Fast enough**: 800ms dla 100 nodes [E-143] - well under 2s target
- ✅ **Pure Python**: Easy debug, no C extensions
- ✅ **Mature**: 15+ years, battle-tested

**Usage**:
```python
import networkx as nx

G = nx.DiGraph()
G.add_node("PRD-001", type="prd")
G.add_edge("PRD-001", "TDD-001", edge_type="requires")

# Algorithms
cycles = list(nx.simple_cycles(G))  # Detect circular deps
hierarchy = nx.topological_sort(G)  # DAG ordering
```

**Evidence**: [E-143] Benchmark: 100 nodes + 200 edges → 800ms (build + cycle detection)

### Cytoscape.js 3.26+ (JavaScript) ✅

**Why**:
- ✅ **Handles scale**: 1000+ nodes interactive [E-148]
- ✅ **Rich layouts**: Hierarchical, force-directed (CoSE), circular, breadthfirst
- ✅ **Interactive**: Zoom, pan, drag nodes, edge filtering
- ✅ **Mature**: 10+ years, widely used (Cytoscape desktop = bioinformatics standard)

**Embed via QtWebEngine**:
```python
from PySide6.QtWebEngineWidgets import QWebEngineView

class GraphWidget(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setHtml("""
        <script src="cytoscape.min.js"></script>
        <script>
        var cy = cytoscape({
            container: document.getElementById('cy'),
            elements: [...],  // From Python via QtWebChannel
            layout: { name: 'cose' }
        });
        </script>
        """)
```

**Evidence**: [E-148] Prototype: 1000 nodes → smooth rendering, interactive

---

## Alternatives

### D3.js ❌
**Pros**: Most powerful (any viz possible)
**Cons**: Low-level (need write layout algorithms), steep learning curve
**Rejected**: Cytoscape.js has built-in graph layouts (don't reinvent)

### vis.js ❌
**Cons**: Less maintained (2021 last release), smaller community
**Rejected**: Cytoscape.js more active

### igraph (Python alt) ❌
**Pros**: Faster than NetworkX (C core)
**Cons**: Harder to extend (C extension), less Pythonic
**Rejected**: NetworkX fast enough (800ms < 2s target), ease of use > speed

---

## Consequences

**Positive**:
- ✅ Performance targets met (NetworkX < 2s, Cytoscape.js handles 1000+ nodes)
- ✅ Rich features (algorithms + interactive viz)
- ✅ Proven tech (both libraries battle-tested)

**Negative**:
- ⚠️ Two libraries (Python + JavaScript) - but necessary (no Python viz library matches Cytoscape.js)
- ⚠️ QtWebEngine bridge (Python ↔ JS) - but QtWebChannel makes this straightforward

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
