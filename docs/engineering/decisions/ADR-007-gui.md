---
id: ADR-007
title: "ADR-007: GUI Architecture Pattern"
type: adr
status: approved
decision_date: 2025-12-21
parent: TDD-001-V2

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
