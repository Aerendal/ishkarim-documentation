---
id: ADR-007
title: "ADR-007: GUI Architecture Pattern"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-21
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-21"
  status_reason: "Decision approved after prototype - Model-View pattern selected"
  next_review_date: "2026-12-21"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-21"
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
  note: "ADR approved - establishes GUI architecture pattern"

version_history:
  - version: "1.0.0"
    date: "2025-12-21"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: Model-View pattern (Qt's natural pattern)"
    breaking: false
    changes:
      - "Evaluated 3 options: MVC, MVVM, Model-View"
      - "Selected Model-View (Qt Signal/Slot = implicit controller)"
      - "Rejected MVC (explicit controller redundant with Qt Signal/Slot)"
      - "Rejected MVVM (overkill for desktop app, designed for WPF/XAML)"
    impacts:
      - id: "COMP-005-gui"
        impact_type: "unblocked"
        description: "GUI component can proceed with Model-View pattern"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture uses Model-View pattern"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-005-gui"
      notified_date: "2025-12-21"
      acknowledged: true
      acknowledged_by: "GUI Developer"
      acknowledged_date: "2025-12-21"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 8
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
      note: "Evidence E-150, E-166 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "TDD-001-V2"
    type: requires
    reason: "GUI architecture requirements defined in TDD"
  - id: "ADR-001"
    type: related
    reason: "PySide6 framework (from ADR-001) enables Model-View pattern"

impacts:
  - id: "COMP-005-gui"
    type: blocks
    until: "ADR-007.status == approved"
    reason: "GUI implementation needs architecture pattern choice"
  - id: "TDD-001-V2"
    type: informs
    reason: "Architecture updated with Model-View pattern"

context_snapshot:
  date: "2025-12-21"
  requirements:
    - "Separation of concerns (business logic ≠ UI code)"
    - "Testable (unit test business logic without GUI)"
    - "Maintainable (standard pattern, not custom)"
    - "Qt-idiomatic (leverage framework, don't fight it)"

evidence_ids:
  - "E-150"  # Architecture prototype (Model-View working)
  - "E-166"  # MVC vs MVVM comparison (Qt Signal/Slot = implicit controller)

alternatives:
  - id: "OPT-MVC"
    title: "Model-View-Controller (explicit controller)"
    status: rejected
    reason: "Qt Signal/Slot replaces explicit controller. Unnecessary layer dla Qt apps."

  - id: "OPT-MVVM"
    title: "Model-View-ViewModel"
    status: rejected
    reason: "Overkill dla desktop app (MVVM = WPF/XAML data binding). Qt doesn't need ViewModel layer."

  - id: "OPT-MODEL-VIEW"
    title: "Model-View (Qt's natural pattern)"
    status: selected
    reason: "Qt Signal/Slot = implicit controller. Simple, idiomatic, proven. Model = business logic, View = PySide6 widgets."
---

# ADR-007: GUI Architecture Pattern

**Decision**: Use **Model-View pattern** (Qt's natural pattern)

**Status**: ✅ APPROVED

---

## Context

**Problem**: Organize GUI code (avoid "God Object" MainWindow with all logic).

**Requirements**:
1. Separation of concerns (business logic ≠ UI code)
2. Testable (unit test business logic without GUI)
3. Maintainable (standard pattern, not custom)
4. Qt-idiomatic (leverage framework, don't fight it)

---

## Decision

### Model-View Pattern ✅

**Architecture**:

```
┌────────────────┐
│  Model Layer   │  (Business Logic - Core Engine)
│                │
│  - Parser      │  Pure Python, no Qt dependencies
│  - Validator   │  Testable independently
│  - Graph       │
│  - Gap Engine  │
└────────┬───────┘
         │
         │ Signals/Slots (implicit controller)
         ↓
┌────────────────┐
│  View Layer    │  (PySide6 Widgets)
│                │
│  - MainWindow  │  Handles user input
│  - GraphWidget │  Emits signals (user_clicked)
│  - Panels      │  Receives signals (data_updated)
└────────────────┘
```

**Why**:
- ✅ **Qt natural**: Signal/Slot = implicit controller (no need explicit Controller class)
- ✅ **Simple**: 2 layers (Model, View) vs 3 (MVC) or 3 (MVVM)
- ✅ **Testable**: Model layer = pure Python (no GUI deps)
- ✅ **Proven**: Standard Qt pattern (Qt docs recommend this)

**Example**:
```python
# Model (business logic)
class DocumentAnalyzer:
    def analyze(self, file_path: Path) -> AnalysisResult:
        # Pure Python logic
        pass

# View (GUI)
class MainWindow(QMainWindow):
    def __init__(self):
        self.analyzer = DocumentAnalyzer()
        self.analyzer.analysis_complete.connect(self.on_analysis_done)

    def open_file(self):
        path = QFileDialog.getOpenFileName(...)
        self.analyzer.analyze(path)  # Async via signal

    def on_analysis_done(self, result):
        self.graph_widget.render(result.graph)
```

**Signal/Slot = Controller**:
- User action (button click) → View emits signal
- Signal → Model slot (business logic)
- Model completes → Model emits signal
- Signal → View slot (update UI)

**Evidence**: [E-150] Prototype validated pattern works, [E-166] Comparison confirmed Qt Signal/Slot replaces Controller

---

## Alternatives

### MVC (explicit Controller) ❌
**Cons**: Qt Signal/Slot already IS controller (implicit). Explicit Controller = redundant layer.
**Rejected**: Unnecessary complexity

### MVVM ❌
**Cons**: ViewModel layer designed dla WPF/XAML data binding (not needed w Qt). Overkill dla desktop app.
**Rejected**: Over-engineering

---

## Consequences

**Positive**:
- ✅ Simple (2 layers, clear separation)
- ✅ Testable (Model independent of Qt)
- ✅ Idiomatic (Qt-native pattern)
- ✅ Async-friendly (Signal/Slot = natural async)

**Negative**:
- ⚠️ "Model-View" terminology overloaded (Qt Model/View != MVC Model/View) - but Qt docs clear

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
