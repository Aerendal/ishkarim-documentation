---
id: ADR-001
title: "ADR-001: GUI Framework (PySide6 vs Tkinter vs PyQt6)"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-18
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-18"
  status_reason: "Decision approved after evaluation - PySide6 selected"
  next_review_date: "2026-12-18"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-18"
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
  note: "ADR approved - establishes GUI framework choice"

version_history:
  - version: "1.0.0"
    date: "2025-12-18"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: PySide6 selected as GUI framework"
    breaking: false
    changes:
      - "Evaluated 3 options: Tkinter, PyQt6, PySide6"
      - "Selected PySide6 (LGPL, QtWebEngine, professional look)"
      - "Rejected Tkinter (90s look, no web view)"
      - "Rejected PyQt6 (GPL license issues)"
    impacts:
      - id: "COMP-005-gui"
        impact_type: "unblocked"
        description: "GUI component design can proceed with PySide6"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes PySide6 as GUI framework"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-005-gui"
      notified_date: "2025-12-18"
      acknowledged: true
      acknowledged_by: "GUI Developer"
      acknowledged_date: "2025-12-18"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 11
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
      note: "Evidence E-144, E-160, E-161 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "PRD-001-V2"
    type: requires
    reason: "NFR-008 (intuitive UI), NFR-009 (4.5/5 rating) require professional GUI framework"

impacts:
  - id: "COMP-005-gui"
    type: blocks
    until: "ADR-001.status == approved"

context_snapshot:
  date: "2025-12-18"
  team_skills:
    pyside6: "Novice (need learning)"
    tkinter: "Mid (basic experience)"
    pyqt6: "Novice"
  requirements:
    - "Cross-platform (Linux, macOS, Windows)"
    - "QtWebEngine needed (dla Cytoscape.js embed)"
    - "Professional look (not 90s UI)"
    - "Commercial-friendly license"

evidence_ids:
  - "E-144"  # PySide6 evaluation matrix (7 criteria)
  - "E-160"  # Tkinter prototype (ugly, no web view)
  - "E-161"  # PyQt6 license analysis (GPL problematic)

alternatives:
  - id: "OPT-TKINTER"
    title: "Tkinter (built-in Python)"
    status: rejected
    reason: "90s look (unacceptable UX), no QtWebEngine (can't embed Cytoscape.js)"

  - id: "OPT-PYQT6"
    title: "PyQt6 (Qt6 binding)"
    status: rejected
    reason: "GPL license (problematic for commercial use - requires Qt commercial license or GPL release)"

  - id: "OPT-PYSIDE6"
    title: "PySide6 (Official Qt6)"
    status: selected
    reason: "LGPL (commercial-friendly), QtWebEngine included, professional look, official Qt binding"

triggers:
  - id: "TRIGGER-PERF-GUI"
    condition: "GUI responsiveness > 200ms (2× NFR-003 target)"
    action: "Optimize Qt event loop or consider lighter framework"
---

# ADR-001: GUI Framework Selection

**Decision**: Use **PySide6 (Qt 6.5+)** for GUI framework

**Status**: ✅ APPROVED (2025-12-18)

---

## Context

**Problem**: Wybór GUI framework dla cross-platform desktop app.

**Requirements**:
1. **QtWebEngine support**: CRITICAL - need embed Cytoscape.js (JavaScript graph viz)
2. **Cross-platform**: Linux, macOS, Windows
3. **Professional look**: Native widgets, modern UI (not 90s Tkinter)
4. **Commercial license**: LGPL/MIT acceptable (GPL problematic)
5. **Team learning curve**: Reasonable (2 weeks max to productivity)

---

## Decision

### PySide6 (Qt 6.5+) ✅

**Why**:
- ✅ **QtWebEngine**: Can embed Cytoscape.js (CRITICAL requirement met)
- ✅ **LGPL license**: Commercial-friendly (dynamic linking allowed)
- ✅ **Official Qt binding**: Better long-term support than PyQt6
- ✅ **Professional look**: Native widgets, material design support
- ✅ **Mature ecosystem**: 25+ years Qt development

**Key modules**:
- `QtWidgets`: Main window, dialogs, layouts
- `QtWebEngineWidgets`: Cytoscape.js embed (QtWebEngineView)
- `QtWebChannel`: Python ↔ JavaScript bridge
- `QtCore`: Signals/slots, event loop

**Evidence**: [E-144] Evaluation scored PySide6 8.5/10 vs Tkinter 4/10, PyQt6 7/10

---

## Alternatives

### Tkinter ❌

**Pros**: Built-in (no install), simple
**Cons**:
- ❌ Ugly (90s look - violates NFR-009)
- ❌ No web view (can't embed Cytoscape.js - **SHOWSTOPPER**)
- ❌ Limited widgets

**Evidence**: [E-160] Prototype showed unacceptable UX

---

### PyQt6 ❌

**Pros**: Same Qt features as PySide6
**Cons**:
- ❌ **GPL license**: Requires commercial Qt license (~$5k/year) OR release app as GPL (contradicts commercial use)
- ❌ Third-party binding (Riverbank) - less official support

**Evidence**: [E-161] License analysis

---

### PySide6 ✅ SELECTED

**Cons**:
- ⚠️ Learning curve (team novice - but 2 weeks training acceptable)
- ⚠️ Binary size (~100MB with Qt libs - acceptable for desktop)

**Mitigation**: 2-week training phase (weeks 1-2), Qt documentation excellent

---

## Consequences

**Positive**:
- ✅ Professional UI achievable (NFR-009 target: 4.5/5 rating)
- ✅ Cytoscape.js embed working (prototype validated [E-144])
- ✅ Cross-platform (tested on Linux/macOS/Windows)

**Negative**:
- ⚠️ 100MB bundle size (but acceptable dla desktop app)
- ⚠️ Learning curve (but mitigated by training)

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Created**: 2025-12-26
