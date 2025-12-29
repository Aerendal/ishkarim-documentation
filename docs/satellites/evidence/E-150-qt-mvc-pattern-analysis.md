---
id: E-150
title: "Evidence: Qt MVC vs MVVM Pattern Analysis"
type: evidence
evidence_type: analysis
date: 2025-12-21
author: Tech Lead
related_documents:
  - ADR-007 (GUI architecture pattern decision)
tags: [qt, mvc, mvvm, model-view, architecture, gui]
status: completed
---

# Evidence: Qt MVC vs MVVM Pattern Analysis

## Kontekst

ADR-007 evaluates GUI architecture patterns dla PySide6. **Question**: MVC, MVVM, or Model-View - który pattern najlepszy dla Qt?

---

## Pattern Comparison

### 1. **Traditional MVC** (Model-View-Controller)

**Structure**:
- Model: Data layer
- View: UI widgets
- Controller: Explicit mediator class

**Qt Implementation**:
```python
class DocumentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect signals
        self.view.save_button.clicked.connect(self.on_save)

    def on_save(self):
        data = self.view.get_data()
        self.model.save(data)
```

**Pros**: Clear separation
**Cons**: **Redundant** - Qt Signal/Slot already acts as implicit controller

---

### 2. **MVVM** (Model-View-ViewModel)

**Structure**:
- Model: Data
- View: QML/Widgets
- ViewModel: Data binding layer

**Qt Implementation**: Designed dla QML (declarative UI), **overkill dla widgets**.

**Pros**: Great dla QML
**Cons**: **Unnecessary** dla QWidget-based apps (not using QML)

---

### 3. **Model-View** (Qt's Native Pattern)

**Structure**:
- Model: Data + business logic
- View: UI widgets
- Controller: **Implicit** (Qt Signal/Slot mechanism)

**Qt Implementation**:
```python
class DocumentModel(QObject):
    document_changed = Signal(dict)

    def save(self, data):
        # Business logic
        self.document_changed.emit(data)

class DocumentView(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.document_changed.connect(self.on_update)
        self.save_button.clicked.connect(lambda: self.model.save(self.get_data()))

    def on_update(self, data):
        self.display(data)
```

**Pros**: **Natural dla Qt** - Signal/Slot = implicit controller
**Cons**: None dla QWidget apps

---

## Qt Documentation Recommendation

**From Qt Official Docs**:
> "Qt uses a Model/View architecture where the Controller is implicit through Signal/Slot connections."

**Verdict**: Qt's design **favors Model-View**, explicit Controller redundant.

---

## Implications dla ADR-007

### ✅ Model-View Pattern (Qt's Native)

**Evidence**:
1. **Qt's official recommendation** - documented w Qt architecture guides
2. **Signal/Slot = implicit controller** - no need for explicit Controller class
3. **Simpler code** - fewer classes, less boilerplate
4. **Natural dla QWidget apps** - MVVM overkill (designed for QML)

**Rekomendacja**: **Model-View pattern** - align with Qt's design philosophy.

---

**Related Documents**:
- [ADR-007: GUI Architecture Pattern](../../engineering/decisions/ADR-007-gui.md)
- [E-166: Qt Signal/Slot Performance](E-166-qt-signals.md)
