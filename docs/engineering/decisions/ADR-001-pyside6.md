---
id: ADR-001
title: "ADR-001: GUI Framework (PySide6 vs Tkinter vs PyQt6)"
type: adr
domain: architecture
status: approved
created: 2025-12-26
decision_date: 2025-12-18
author: ["Tech Lead"]
parent: TDD-001-V2

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
