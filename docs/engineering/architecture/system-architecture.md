---
id: ARCH-SYS-001
title: "System Architecture - Documentation Management System"
type: architecture
parent: TDD-001-V2
status: draft
created: 2025-12-26
updated: 2025-12-26
owner: Tech Lead
---

# System Architecture

**Parent Document**: [TDD-001-V2](../tdd-v2.md)

## Spis Treści

1. [Architecture Overview](#architecture-overview) (Linie 30-80)
2. [Layered Architecture](#layered-architecture) (Linie 81-160)
3. [Component Interactions](#component-interactions) (Linie 161-240)
4. [Data Flow](#data-flow) (Linie 241-300)
5. [Concurrency Model](#concurrency-model) (Linie 301-340)
6. [Error Handling Strategy](#error-handling) (Linie 341-380)
7. [State Management](#state-management) (Linie 381-420)

---

## Architecture Overview

### Pattern: Layered Monolith

**Decision**: **ARCH-A - Monolithic Architecture** (selected w TDD-V2)

**Rationale**:
- ✅ **Local-first requirement**: Single process optimal (no IPC overhead)
- ✅ **Performance targets**: < 2s/100docs requires low latency (no network calls)
- ✅ **Simplicity**: 12-week timeline favors simple architecture
- ✅ **MVP scope**: Feature set doesn't require distribution

**Evidence**: [E-150] Architecture prototype validated monolith feasibility, [E-153] performance model

### High-Level Structure

```
┌──────────────────────────────────────────────────────┐
│                PRESENTATION LAYER                     │
│              (PySide6 GUI - Qt6)                      │
│                                                       │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │
│  │ Main Window  │  │ Graph Widget │  │  Panels   │  │
│  │              │  │ (Cytoscape)  │  │  (Gaps,   │  │
│  │              │  │              │  │   Stats)  │  │
│  └──────────────┘  └──────────────┘  └───────────┘  │
└────────────────────────┬─────────────────────────────┘
                         │ Qt Signals/Slots
         ┌───────────────▼──────────────────┐
         │     BUSINESS LOGIC LAYER         │
         │        (Core Engine)             │
         │                                  │
         │  ┌────────────────────────────┐  │
         │  │  Parser                    │  │ (Markdown → Structured)
         │  ├────────────────────────────┤  │
         │  │  Validator                 │  │ (Schema checking)
         │  ├────────────────────────────┤  │
         │  │  Graph Builder             │  │ (NetworkX)
         │  ├────────────────────────────┤  │
         │  │  Gap Engine                │  │ (E110-E200 detection)
         │  ├────────────────────────────┤  │
         │  │  Gate Manager              │  │ (DoR/DoD/Impl Log)
         │  ├────────────────────────────┤  │
         │  │  Evidence Manager          │  │ ([E-XXX] tracking)
         │  ├────────────────────────────┤  │
         │  │  Storytelling Validator    │  │ (Narrative checking)
         │  └────────────────────────────┘  │
         └───────────────┬──────────────────┘
                         │
         ┌───────────────▼──────────────────┐
         │      DATA ACCESS LAYER           │
         │                                  │
         │  ┌────────────┐  ┌────────────┐  │
         │  │  SQLite    │  │ File System│  │
         │  │  (Index,   │  │ (Markdown  │  │
         │  │   FTS5,    │  │  files -   │  │
         │  │   Prov.)   │  │  source    │  │
         │  │            │  │  of truth) │  │
         │  └────────────┘  └────────────┘  │
         └──────────────────────────────────┘
                         │
         ┌───────────────▼──────────────────┐
         │    INFRASTRUCTURE LAYER          │
         │                                  │
         │  ┌────────────────────────────┐  │
         │  │  File Watcher (Watchdog)   │  │
         │  │  Auto-rebuild on changes   │  │
         │  └────────────────────────────┘  │
         └──────────────────────────────────┘
```

---

## Layered Architecture

### Layer 1: Presentation Layer (PySide6 GUI)

**Responsibility**: User interaction + visualization

**Components**:
1. **Main Window** (`src/gui/main_window.py`)
   - Menu bar (File, Edit, View, Help)
   - Toolbar (Open, Analyze, Refresh)
   - Status bar (current analysis status)
   - Layout management (splitters, docks)

2. **Graph Widget** (`src/gui/graph_widget.py`)
   - Embeds Cytoscape.js via QtWebEngine
   - Interactive graph (zoom, pan, node selection)
   - Layout algorithms (hierarchical, force-directed)
   - Edge filtering (show/hide edge types)

3. **Preview Widget** (`src/gui/preview_widget.py`)
   - Markdown rendering (safe HTML)
   - Syntax highlighting (frontmatter YAML)
   - Jump to section (from gap click)

4. **Panels** (`src/gui/panels/`)
   - Gaps Panel: List detected gaps, filter by severity
   - Stats Panel: Document counts, gap counts, coverage %
   - Remediation Panel: Suggested next steps

**Technology**: PySide6 (Qt 6.5+), QtWebEngine, QtWebChannel (dla Cytoscape.js bridge)

**Interactions**:
- **Inbound**: Signals from Core Engine (document analyzed, gaps detected)
- **Outbound**: User actions (open file, trigger analysis, apply remediation)

**State**: UI state only (selected node, filter settings, view mode)

---

### Layer 2: Business Logic Layer (Core Engine)

**Responsibility**: All domain logic (parsing, validation, gap detection)

**Sub-components**:

#### 2.1 Parser (`src/core/parser.py`)
- Extract YAML frontmatter (python-frontmatter)
- Parse markdown to AST (markdown-it-py)
- Identify sections (H1-H6 hierarchy)
- Detect inline references ([E-XXX], ADR-XXX, etc.)

**Output**: `Document` object (Pydantic model)

#### 2.2 Validator (`src/core/validator.py`)
- Schema validation (Pydantic)
- Required sections check (E110 gap type)
- Placeholder detection (E120 - TODO/TBD)
- Frontmatter constraints (enums, patterns)

**Output**: `ValidationResult` (gaps: list[Gap], status: pass/fail)

#### 2.3 Graph Builder (`src/core/graph_builder.py`)
- Build NetworkX DiGraph from documents
- Create nodes (metadata: doc type, status, gaps)
- Create edges (typed: requires, informs, implements)
- Cycle detection (NetworkX algorithms)
- Hierarchy calculation (emergent levels)

**Output**: `nx.DiGraph` + metadata

#### 2.4 Gap Engine (`src/core/gap_engine.py`)
- Detect all gap types (E110-E200)
- Generate remediation steps
- Prioritize by severity
- Track gap resolution (provenance)

**Output**: `list[Gap]` with remediation

#### 2.5 Gate Manager (`src/core/gate_manager.py`)
- Evaluate quality gates (DoR, DoD)
- Check bramki wejścia/wyjścia
- Cascade propagation (impacts)
- Generate blockers report

**Output**: `GateStatus` (blocked/passed)

#### 2.6 Evidence Manager (`src/core/evidence_manager.py`)
- Track [E-XXX] references
- Validate evidence existence
- Generate evidence index
- Detect missing evidence (E170 gap)

**Output**: `EvidenceIndex` + E170 gaps

#### 2.7 Storytelling Validator (`src/core/storytelling.py`)
- Detect fact lists (bullets without narrative)
- Check for storytelling markers ("We considered X, rejected because Y")
- Identify missing alternatives (E190 gap)

**Output**: E180/E190 gaps

**Technology**: Pure Python (no external service calls), NetworkX, Pydantic

---

### Layer 3: Data Access Layer

**Responsibility**: Persistence + indexing

**Components**:

#### 3.1 SQLite Storage (`src/storage/document_store.py`)

**Tables**:
- `documents` (id, file_path, type, status, last_modified, content_hash)
- `nodes` (doc_id, metadata_json)
- `edges` (from_id, to_id, edge_type, metadata_json)
- `gaps` (gap_id, doc_id, gap_type, severity, description, created_at)
- `provenance` (entity_id, event_type, timestamp, metadata_json)

**Indexes**:
- FTS5 virtual table dla full-text search (title, body)
- Index on (doc_id, gap_type) dla gap queries
- Index on (from_id, to_id) dla graph traversal

**Operations**:
- `index_document(doc: Document)` → store w SQLite
- `search(query: str)` → FTS5 search
- `get_gaps(doc_id: str)` → retrieve gaps
- `record_provenance(event)` → audit trail

**Evidence**: [E-146] FTS5 benchmark (< 100ms search dla 10k docs)

#### 3.2 File System (`src/storage/file_system.py`)

**Responsibility**: Read markdown files (source of truth)

**Operations**:
- `read_file(path: Path)` → raw content
- `list_documents(dir: Path)` → all .md files
- Validation: Path traversal check (security)

**Note**: **READ-ONLY** - system nie modyfikuje markdown files (user edits externally)

---

### Layer 4: Infrastructure Layer

#### File Watcher (`src/core/file_watcher.py`)

**Technology**: Watchdog library

**Responsibility**: Monitor file system changes → trigger rebuild

**Events**:
- `on_created(path)` → new document added
- `on_modified(path)` → document updated
- `on_deleted(path)` → document removed
- `on_moved(src, dest)` → document renamed

**Actions**:
- Parse changed file
- Update graph (incremental)
- Re-detect gaps
- Update SQLite index
- Emit signal to GUI (refresh)

**Evidence**: [E-147] Watchdog reliability (99.9% event detection)

---

## Component Interactions

### Sequence Diagram: User Opens Project

```
User                GUI             Parser      Validator    GraphBuilder    GapEngine    Storage       GUI
 │                   │                │             │              │             │          │           │
 │ Open Project      │                │             │              │             │          │           │
 ├──────────────────>│                │             │              │             │          │           │
 │                   │ list_documents()│             │              │             │          │           │
 │                   ├───────────────────────────────┼──────────────┼─────────────┼─────────>│           │
 │                   │                │             │              │             │  files[] │           │
 │                   │<───────────────────────────────────────────────────────────┼──────────┤           │
 │                   │                │             │              │             │          │           │
 │                   │ for each file: │             │              │             │          │           │
 │                   │ parse()        │             │              │             │          │           │
 │                   ├───────────────>│             │              │             │          │           │
 │                   │       Document │             │              │             │          │           │
 │                   │<───────────────┤             │              │             │          │           │
 │                   │                │             │              │             │          │           │
 │                   │ validate()     │             │              │             │          │           │
 │                   ├────────────────┼────────────>│              │             │          │           │
 │                   │                │   ValidationResult          │             │          │           │
 │                   │<───────────────┼─────────────┤              │             │          │           │
 │                   │                │             │              │             │          │           │
 │                   │ build_graph()  │             │              │             │          │           │
 │                   ├────────────────┼─────────────┼─────────────>│             │          │           │
 │                   │                │             │     nx.DiGraph              │          │           │
 │                   │<───────────────┼─────────────┼──────────────┤             │          │           │
 │                   │                │             │              │             │          │           │
 │                   │ detect_gaps()  │             │              │             │          │           │
 │                   ├────────────────┼─────────────┼──────────────┼────────────>│          │           │
 │                   │                │             │              │       Gaps[]│          │           │
 │                   │<───────────────┼─────────────┼──────────────┼─────────────┤          │           │
 │                   │                │             │              │             │          │           │
 │                   │ index_all()    │             │              │             │          │           │
 │                   ├────────────────┼─────────────┼──────────────┼─────────────┼─────────>│           │
 │                   │                │             │              │             │    OK    │           │
 │                   │<───────────────┼─────────────┼──────────────┼─────────────┼──────────┤           │
 │                   │                │             │              │             │          │           │
 │                   │ render_graph() │             │              │             │          │           │
 │                   ├────────────────┼─────────────┼──────────────┼─────────────┼──────────┼──────────>│
 │                   │                │             │              │             │          │  Display  │
 │<──────────────────┼────────────────┼─────────────┼──────────────┼─────────────┼──────────┼───────────┤
```

**Duration**: ~2-3s dla 100 documents (within NFR target < 5s)

---

### Sequence Diagram: File Changed (Auto-Rebuild)

```
FileSystem      Watchdog         Parser      GraphBuilder    GapEngine    Storage       GUI
    │              │                │             │             │          │           │
    │ .md modified │                │             │             │          │           │
    ├─────────────>│                │             │             │          │           │
    │              │ on_modified()  │             │             │          │           │
    │              ├───────────────>│             │             │          │           │
    │              │       Document │             │             │          │           │
    │              │<───────────────┤             │             │          │           │
    │              │                │             │             │          │           │
    │              │ update_graph() │             │             │          │           │
    │              ├────────────────┼────────────>│             │          │           │
    │              │                │   (incremental update)    │          │           │
    │              │<───────────────┼─────────────┤             │          │           │
    │              │                │             │             │          │           │
    │              │ re_detect_gaps()             │             │          │           │
    │              ├────────────────┼─────────────┼────────────>│          │           │
    │              │<───────────────┼─────────────┼─────────────┤          │           │
    │              │                │             │             │          │           │
    │              │ emit(document_changed)       │             │          │           │
    │              ├────────────────┼─────────────┼─────────────┼──────────┼──────────>│
    │              │                │             │             │          │  Refresh  │
```

**Duration**: ~200ms dla single document (fast feedback)

---

## Data Flow

### Primary Data Flow (Markdown → GUI)

```
Markdown File (.md)
    ↓
[Parser] Extract frontmatter (YAML) + sections (markdown AST)
    ↓
Document Object (Pydantic)
    ↓
[Validator] Check schema + required sections + placeholders
    ↓
ValidationResult (gaps: E110, E120, E170, E180, E190, E200)
    ↓
[Graph Builder] Create nodes + edges (NetworkX)
    ↓
nx.DiGraph (dependency graph)
    ↓
[Gap Engine] Detect E130, E140, E150, E160 (graph-based gaps)
    ↓
Gaps[] (all E110-E200)
    ↓
[Storage] Index document + gaps (SQLite)
    ↓
[GUI] Render graph (Cytoscape.js) + display gaps (panels)
    ↓
User sees: Interactive graph + gap list + remediation suggestions
```

### Secondary Data Flow (Search)

```
User enters search query
    ↓
[Storage] SQLite FTS5 search (title + body)
    ↓
Matching Document IDs
    ↓
[Graph Builder] Highlight nodes in graph
    ↓
[GUI] Zoom to highlighted nodes
```

**Performance**: < 100ms dla 10k documents [E-146]

### Tertiary Data Flow (Provenance Tracking)

```
Event occurs (document created, gap detected, gate passed)
    ↓
[Evidence Manager] Record provenance entry
    ↓
[Storage] Insert into provenance table (timestamp, event_type, metadata)
    ↓
Audit trail (queryable: "Who approved this document?", "When was gap X resolved?")
```

---

## Concurrency Model

### Threading Model: **Single-Threaded (Qt Event Loop)**

**Decision**: No multi-threading w MVP

**Rationale**:
- ✅ **Simplicity**: No race conditions, no locks
- ✅ **Performance sufficient**: All operations < 2s (within NFR [E-153])
- ✅ **Qt natural fit**: Signal/slot = async without threads

**Implications**:
- File I/O: **Synchronous** (< 10ms/doc [E-149] - negligible block)
- Graph build: **Synchronous** (< 2s/100docs [E-143] - acceptable)
- GUI updates: **Async via Qt signals** (event-driven)

**Future optimization** (if TRIGGER-PERF):
- V1.5: `QThreadPool` dla heavy operations (graph build > 10s)
- V2.0: Async I/O (`asyncio` + `aiofiles`) if needed

### Event Loop

```
Qt Event Loop (main thread)
    ↓
Process user input (mouse, keyboard)
    ↓
Execute slot functions (parse, validate, analyze)
    ↓
Emit signals (document_analyzed, gaps_detected)
    ↓
Update GUI (re-render graph, refresh panels)
    ↓
Return to event loop
```

**Blocking operations**: None expected (all < 2s per NFR)

**Watchdog integration**: Watchdog runs observer thread (library internal), emits events to Qt main thread (thread-safe queue)

---

## Error Handling Strategy

### Error Categories

#### 1. User Errors (Expected)

**Examples**:
- Invalid YAML frontmatter (syntax error)
- Missing required field (e.g., no `id:` in frontmatter)
- Broken reference (PRD links to non-existent ADR)

**Handling**:
- ✅ **Graceful degradation**: Parse what's possible, report error as gap (E140)
- ✅ **User-friendly message**: "Document PRD-001 references ADR-005 which doesn't exist"
- ✅ **No crash**: System continues, marks document as invalid

**UI**: Error icon on node, tooltip shows error, Gaps panel lists issue

#### 2. System Errors (Unexpected)

**Examples**:
- SQLite database locked (rare but possible)
- Out of memory (huge file)
- Disk full (can't write SQLite)

**Handling**:
- ✅ **Try-except blocks**: All I/O operations wrapped
- ✅ **Logging**: Error logged with stack trace (Python `logging` module)
- ✅ **User notification**: Dialog box "Error occurred, see log file"
- ✅ **Fallback**: Read-only mode if SQLite fails (parse + display only, no index)

**UI**: Status bar shows "Analysis failed - check logs", disable features gracefully

#### 3. Performance Errors (Triggers)

**Examples**:
- Graph build takes > 5s (exceeds NFR 2.5× margin)
- Memory usage > 2GB (unexpected)

**Handling**:
- ✅ **Monitoring**: Log performance metrics (parse time, graph build time)
- ✅ **Alert**: Warning if > 2× NFR target
- ✅ **Trigger re-evaluation**: TRIGGER-PERF activated

**Evidence**: [E-153] Performance model with thresholds

### Error Recovery

**Principle**: **Fail gracefully, preserve user data**

**Strategies**:
1. **Transactional SQLite**: WAL mode (crash-safe)
2. **Markdown = source of truth**: SQLite rebuildable if corrupted
3. **Incremental updates**: Single file error doesn't break entire project
4. **User notification**: Always inform user, never silent failure

---

## State Management

### Application State (GUI)

**State location**: `src/gui/app_state.py` (singleton pattern)

**State variables**:
- `current_project_path: Path` (opened project directory)
- `loaded_documents: dict[str, Document]` (in-memory cache)
- `dependency_graph: nx.DiGraph` (current graph)
- `detected_gaps: list[Gap]` (all gaps)
- `selected_node: Optional[str]` (user selection)
- `filter_settings: FilterSettings` (gap severity, edge types)

**Persistence**: None (transient - rebuilt on open project)

### Document State (Data)

**State location**: SQLite database + markdown files

**Immutable**: Markdown files (user edits externally via editor)

**Mutable**: SQLite index (rebuilt on file changes)

**Consistency**: Eventual consistency model
- File change detected (Watchdog)
- Parse + validate + re-index (~200ms)
- GUI refreshes (signal emitted)

**No distributed state**: Single process = no synchronization needed

---

## Summary

**Architecture**: Layered monolith (4 layers: Presentation, Business Logic, Data Access, Infrastructure)

**Pattern strengths**:
- ✅ Simple (12-week timeline achievable)
- ✅ Fast (no IPC, local-first optimal)
- ✅ Testable (clear layer boundaries)
- ✅ Maintainable (standard Python patterns)

**Pattern weaknesses**:
- ❌ Scalability limit (~10k docs) - acceptable per requirements
- ❌ No distribution (can't split workload) - not needed for local-first

**Re-evaluation triggers**:
- TRIGGER-SCALE: If > 10k docs needed (re-consider microservices)
- TRIGGER-CLOUD: If cloud sync required (re-architect storage)

**Status**: Architecture validated via prototype [E-150], performance modeled [E-153], ready dla implementation.

---

**Parent Document**: [TDD-001-V2](../tdd-v2.md)
**Created**: 2025-12-26
**Last Updated**: 2025-12-26
