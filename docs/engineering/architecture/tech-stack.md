---
id: ARCH-TECH-001
title: "Technology Stack - Documentation Management System"
type: architecture
parent: TDD-001-V2
status: draft
created: 2025-12-26
updated: 2025-12-26
owner: Tech Lead
---

# Technology Stack

**Parent Document**: [TDD-001-V2](../tdd-v2.md)

## Spis Treści

1. [Stack Overview](#stack-overview) (Linie 25-60)
2. [Core Technologies](#core-technologies) (Linie 61-180)
3. [Dependencies](#dependencies) (Linie 181-240)
4. [Development Tools](#development-tools) (Linie 241-280)
5. [Version Constraints](#version-constraints) (Linie 281-320)

---

## Stack Overview

### Technology Layers

| Layer          | Technology         | Version | License       | Rationale                                   |
| -------------- | ------------------ | ------- | ------------- | ------------------------------------------- |
| **Language**   | Python             | 3.11+   | PSF           | Team expertise, rich ecosystem              |
| **GUI**        | PySide6 (Qt6)      | 6.5+    | LGPL          | Cross-platform, professional look [ADR-001] |
| **Graph**      | NetworkX           | 3.2+    | BSD           | Rich algorithms, Python-native [ADR-004]    |
| **Validation** | Pydantic           | 2.5+    | MIT           | Type-safe, fast (Rust core) [ADR-003]       |
| **Parser**     | python-frontmatter | 1.0+    | MIT           | YAML extraction standard                    |
| **Parser**     | markdown-it-py     | 3.0+    | MIT           | CommonMark compliant                        |
| **Storage**    | SQLite             | 3.40+   | Public Domain | Embedded, FTS5 support [ADR-005]            |
| **File Watch** | Watchdog           | 3.0+    | Apache 2.0    | Cross-platform fs events [ADR-002]          |
| **Graph Viz**  | Cytoscape.js       | 3.26+   | MIT           | Interactive, 1000+ nodes [ADR-004]          |

### Dependency Graph (High-Level)

```
Application
    ├── PySide6 (GUI framework)
    │   └── Qt6 (C++ libraries)
    ├── NetworkX (graph algorithms)
    ├── Pydantic (validation)
    ├── python-frontmatter (YAML parser)
    ├── markdown-it-py (markdown parser)
    ├── Watchdog (file monitoring)
    └── SQLite3 (built-in Python - no external dep)

GUI (QtWebEngine)
    └── Cytoscape.js (JavaScript - bundled)
```

**Total dependency count**: 8 direct, ~25 transitive (lightweight stack)

---

## Core Technologies

### 1. Python 3.11+

**Why Python 3.11?**
- ✅ Team expertise (8+ years [context_snapshot])
- ✅ Rich ecosystem (parser, graph, GUI libraries)
- ✅ 3.11 performance improvements (10-60% faster than 3.10)
- ✅ Pattern matching (nice-to-have dla gap detection logic)

**Minimum version**: 3.11 (for `tomllib` if needed, performance)

**Target version**: 3.11.7 (latest stable as of Dec 2025)

**Constraints**:
- ❌ No 3.9/3.10 support (team standard = 3.11+)
- ❌ No 3.12/3.13 yet (PySide6 compatibility uncertain)

---

### 2. PySide6 (Qt 6.5+)

**Full analysis**: [ADR-001-pyside6.md](../decisions/ADR-001-pyside6.md)

**Why PySide6?**
- ✅ Cross-platform (Linux, macOS, Windows)
- ✅ Professional look (native widgets)
- ✅ QtWebEngine (dla Cytoscape.js embed - CRITICAL)
- ✅ LGPL license (commercial-friendly vs GPL dla PyQt6)
- ✅ Official Qt binding (better long-term support)

**Key modules used**:
- `QtWidgets`: Main window, layouts, dialogs
- `QtCore`: Signals/slots, event loop, QSettings
- `QtWebEngineWidgets`: Cytoscape.js embed (QtWebEngineView)
- `QtWebChannel`: Python ↔ JavaScript bridge

**Version**: 6.5+ (QtWebEngine 6.5 has stability fixes)

**Evidence**: [E-144] Evaluation (PySide6 scored 8.5/10 vs Tkinter 4/10, PyQt6 7/10)

**Installation**:
```bash
pip install PySide6>=6.5.0
```

**Bundle size impact**: ~100MB (Qt6 shared libraries)

---

### 3. NetworkX 3.2+

**Full analysis**: [ADR-004-graph-viz.md](../decisions/ADR-004-graph-viz.md)

**Why NetworkX?**
- ✅ Rich algorithms (cycle detection, DAG analysis, shortest path)
- ✅ Fast enough (< 2s/100 nodes [E-143])
- ✅ Pure Python (easy debugging, no C extensions)
- ✅ Well-documented (mature library, 15+ years)
- ✅ DiGraph support (directed graphs dla dependencies)

**Key algorithms used**:
- `simple_cycles()`: Cycle detection (circular dependencies)
- `topological_sort()`: Hierarchy calculation (emergent levels)
- `shortest_path()`: Dependency chain analysis
- `subgraph()`: Filter graph views

**Version**: 3.2+ (Python 3.11 compatibility)

**Evidence**: [E-143] Benchmark (100 nodes, 200 edges → 800ms build + cycle detection)

**Installation**:
```bash
pip install networkx>=3.2.0
```

**Why not alternatives?**
- ❌ igraph: Faster but C extension (harder to debug/extend)
- ❌ graph-tool: Overkill (scientific computing focus)

---

### 4. Pydantic 2.5+

**Full analysis**: [ADR-003-validation.md](../decisions/ADR-003-validation.md)

**Why Pydantic 2.x?**
- ✅ Type-safe (Python type hints → runtime validation)
- ✅ Fast (Rust core w v2 - 17× faster than v1 [E-145])
- ✅ Excellent error messages (precise, actionable)
- ✅ JSON Schema export (dla future OPA integration if needed)
- ✅ Mature (v2 = stable, production-ready)

**Key features used**:
- `BaseModel`: Data models (Document, Node, Edge, Gap)
- `Field()`: Constraints (min_length, regex patterns, enums)
- `validator()`: Custom validation logic
- `model_validate()`: Runtime validation

**Version**: 2.5+ (stable v2 branch)

**Evidence**: [E-145] Benchmark (1000 docs validated → 42ms total = 42μs/doc)

**Installation**:
```bash
pip install pydantic>=2.5.0
```

**Why not alternatives?**
- ❌ Cerberus: Slower, less type-safe
- ❌ OPA/Rego: Overkill dla MVP (complex policy language - defer to V1.5 if needed)

---

### 5. python-frontmatter 1.0+

**Full analysis**: [ADR-006-parser.md](../decisions/ADR-006-parser.md)

**Why python-frontmatter?**
- ✅ Standard tool (widely used, 1k+ GitHub stars)
- ✅ Fast (< 5ms/doc [E-149])
- ✅ Simple API (`frontmatter.load(file)` → dict)
- ✅ Robust (handles edge cases: no frontmatter, invalid YAML)

**Usage**:
```python
import frontmatter
post = frontmatter.load("doc.md")
metadata = post.metadata  # dict (YAML parsed)
content = post.content    # str (markdown body)
```

**Version**: 1.0+ (stable)

**Installation**:
```bash
pip install python-frontmatter>=1.0.0
```

---

### 6. markdown-it-py 3.0+

**Full analysis**: [ADR-006-parser.md](../decisions/ADR-006-parser.md)

**Why markdown-it-py?**
- ✅ CommonMark compliant (standard markdown spec)
- ✅ AST output (structured tree, not just HTML)
- ✅ Plugin system (extensible if needed)
- ✅ Fast (< 10ms/doc combined with frontmatter [E-149])

**Usage**:
```python
from markdown_it import MarkdownIt
md = MarkdownIt()
tokens = md.parse(content)  # AST (headers, paragraphs, etc.)
```

**Version**: 3.0+ (Python 3.11 compatible)

**Evidence**: [E-149] Benchmark (100 docs parsed → 840ms = 8.4ms/doc)

**Installation**:
```bash
pip install markdown-it-py>=3.0.0
```

**Why not alternatives?**
- ❌ mistune: Faster but less CommonMark compliant
- ❌ python-markdown: Slower, less structured output

---

### 7. SQLite 3.40+ (Built-in)

**Full analysis**: [ADR-005-storage.md](../decisions/ADR-005-storage.md)

**Why SQLite?**
- ✅ Built-in (no external dependency)
- ✅ FTS5 (full-text search - < 100ms dla 10k docs [E-146])
- ✅ Zero-config (no server, file-based)
- ✅ Reliable (most-deployed DB in world)
- ✅ WAL mode (crash-safe writes)

**Version**: 3.40+ (dla FTS5 improvements)

**Check version**:
```python
import sqlite3
print(sqlite3.sqlite_version)  # Should be ≥ 3.40
```

**Features used**:
- FTS5 virtual tables (full-text search)
- JSON functions (dla metadata storage)
- WAL mode (Write-Ahead Logging)
- Foreign keys (referential integrity)

**Evidence**: [E-146] FTS5 benchmark (10k docs indexed, search < 100ms)

---

### 8. Watchdog 3.0+

**Full analysis**: [ADR-002-watchdog.md](../decisions/ADR-002-watchdog.md)

**Why Watchdog?**
- ✅ Cross-platform (inotify/FSEvents/ReadDirectoryChangesW abstraction)
- ✅ Reliable (99.9% event detection [E-147])
- ✅ Mature (10+ years production use)
- ✅ Simple API (event handler pattern)

**Usage**:
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DocHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Re-parse changed file

observer = Observer()
observer.schedule(DocHandler(), path="docs/", recursive=True)
observer.start()
```

**Version**: 3.0+ (Python 3.11 compatible)

**Evidence**: [E-147] Reliability test (10k file changes, 1 miss = 99.99%)

**Installation**:
```bash
pip install watchdog>=3.0.0
```

---

### 9. Cytoscape.js 3.26+ (JavaScript - Bundled)

**Full analysis**: [ADR-004-graph-viz.md](../decisions/ADR-004-graph-viz.md)

**Why Cytoscape.js?**
- ✅ Interactive (zoom, pan, drag nodes)
- ✅ Handles 1000+ nodes ([E-148] prototype)
- ✅ Rich layouts (hierarchical, force-directed, circular)
- ✅ Mature (10+ years, widely used)

**Deployment**: Bundled JavaScript file (loaded via QtWebEngine)

**Bridge**: Python ↔ JavaScript via QtWebChannel

**Version**: 3.26+ (stable)

**Evidence**: [E-148] Prototype (1000 nodes interactive, smooth rendering)

---

## Dependencies

### Production Dependencies (requirements.txt)

```txt
# GUI Framework
PySide6>=6.5.0,<7.0.0

# Graph Analysis
networkx>=3.2.0,<4.0.0

# Validation
pydantic>=2.5.0,<3.0.0

# Parsing
python-frontmatter>=1.0.0,<2.0.0
markdown-it-py>=3.0.0,<4.0.0

# File Monitoring
watchdog>=3.0.0,<4.0.0

# Utilities
python-dateutil>=2.8.0  # Date parsing dla frontmatter
pyyaml>=6.0.0  # YAML parsing (dependency of frontmatter)
```

**Total size**: ~150MB installed (PySide6 dominates)

### Development Dependencies (requirements-dev.txt)

```txt
# Testing
pytest>=7.4.0
pytest-cov>=4.1.0  # Coverage
pytest-qt>=4.2.0   # PySide6 testing

# Linting & Formatting
ruff>=0.1.0  # Fast linter (Rust-based)
black>=23.0.0  # Code formatter
mypy>=1.7.0  # Type checker

# Documentation
mkdocs>=1.5.0  # Docs generator
mkdocs-material>=9.4.0  # Theme

# Build
pyinstaller>=6.0.0  # Standalone executable
```

---

## Development Tools

### Code Quality

**Linter**: Ruff (Rust-based, 10-100× faster than Flake8)
```bash
ruff check src/
```

**Formatter**: Black (PEP 8 compliant, deterministic)
```bash
black src/
```

**Type Checker**: mypy (static type analysis)
```bash
mypy src/ --strict
```

### Testing

**Framework**: pytest

**Coverage target**: 80%+ (NFR-010)

**Test structure**:
```
tests/
├── unit/  (fast, isolated)
│   ├── test_parser.py
│   ├── test_validator.py
│   └── test_graph.py
├── integration/  (cross-component)
│   ├── test_full_analysis.py
│   └── test_gui_integration.py
└── fixtures/  (sample documents)
```

### Build & Distribution

**Tool**: PyInstaller 6.0+

**Build command**:
```bash
pyinstaller --onefile --windowed \
  --add-data "schemas:schemas" \
  --add-data "templates:templates" \
  --name semantic-docs \
  src/main.py
```

**Output**: `dist/semantic-docs` (standalone executable, ~120MB)

---

## Version Constraints

### Why Version Pins?

**Strategy**: **Caret ranges** (`>=X.Y.0,<X+1.0.0`)

**Rationale**:
- ✅ Allow patch updates (bug fixes)
- ✅ Allow minor updates (backwards-compatible features)
- ❌ Block major updates (breaking changes - require testing)

### Critical Constraints

| Package | Constraint | Reason |
|---------|-----------|--------|
| **Python** | `>=3.11,<3.13` | 3.11 features needed, 3.13 untested |
| **PySide6** | `>=6.5.0,<7.0.0` | Qt6 API stability, 7.0 = breaking changes |
| **Pydantic** | `>=2.5.0,<3.0.0` | v2 Rust core performance, v3 = breaking |
| **NetworkX** | `>=3.2.0,<4.0.0` | Stable API, 4.0 unknown breaking changes |

### License Compatibility

| Package | License | Commercial Use? | Attribution Required? |
|---------|---------|-----------------|----------------------|
| PySide6 | LGPL 3.0 | ✅ Yes (dynamic linking) | ✅ Yes (include license) |
| NetworkX | BSD-3-Clause | ✅ Yes | ✅ Yes |
| Pydantic | MIT | ✅ Yes | ✅ Yes |
| python-frontmatter | MIT | ✅ Yes | ✅ Yes |
| markdown-it-py | MIT | ✅ Yes | ✅ Yes |
| Watchdog | Apache 2.0 | ✅ Yes | ✅ Yes |
| SQLite | Public Domain | ✅ Yes | ❌ No |

**Conclusion**: All licenses compatible z commercial use (open-source friendly)

---

## Summary

**Stack characteristics**:
- ✅ **Lightweight**: 8 direct dependencies, 25 transitive
- ✅ **Mature**: All libraries 5+ years production use
- ✅ **Fast**: Performance validated via benchmarks [E-143 to E-149]
- ✅ **Cross-platform**: Linux, macOS, Windows supported
- ✅ **Type-safe**: Pydantic + mypy = robust
- ✅ **License-clean**: All commercial-friendly

**Installation**:
```bash
pip install -r requirements.txt  # Production
pip install -r requirements-dev.txt  # Development
```

**Validation**:
```bash
python --version  # ≥ 3.11
pip list | grep PySide6  # ≥ 6.5.0
sqlite3 --version  # ≥ 3.40
```

**Status**: Technology stack finalized, all dependencies validated via prototypes/benchmarks.

---

**Parent Document**: [TDD-001-V2](../tdd-v2.md)
**Related ADRs**: [ADR-001](../decisions/ADR-001-pyside6.md), [ADR-002](../decisions/ADR-002-watchdog.md), [ADR-003](../decisions/ADR-003-validation.md), [ADR-004](../decisions/ADR-004-graph-viz.md), [ADR-005](../decisions/ADR-005-storage.md), [ADR-006](../decisions/ADR-006-parser.md)
**Created**: 2025-12-26
**Last Updated**: 2025-12-26
