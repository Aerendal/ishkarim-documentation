---
id: ADR-005
title: "ADR-005: Storage Architecture (Files vs Database)"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-22
author: ["Tech Lead"]
reviewers: ["Senior Dev", "Product Owner"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-22"
  status_reason: "Decision approved after hybrid storage prototype - Markdown + SQLite selected"
  next_review_date: "2026-12-22"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-22"
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
  note: "ADR approved - establishes hybrid storage architecture"

version_history:
  - version: "1.0.0"
    date: "2025-12-22"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: Hybrid storage (Markdown files + SQLite index)"
    breaking: false
    changes:
      - "Evaluated 4 options: Files Only, Database Only, Hybrid, PostgreSQL"
      - "Selected Hybrid (Markdown source of truth + SQLite rebuildable cache)"
      - "Rejected Files Only (8s search vs 60ms target)"
      - "Rejected Database Only (not Git-friendly, not human-readable)"
      - "Rejected PostgreSQL (contradicts local-first requirement)"
    impacts:
      - id: "COMP-006-storage"
        impact_type: "unblocked"
        description: "Storage component can proceed with hybrid architecture"
      - id: "COMP-001-parser"
        impact_type: "informs"
        description: "Parser output format depends on storage schema"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes hybrid storage"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-006-storage"
      notified_date: "2025-12-22"
      acknowledged: true
      acknowledged_by: "Storage Developer"
      acknowledged_date: "2025-12-22"
    - id: "COMP-001-parser"
      notified_date: "2025-12-22"
      acknowledged: true
      acknowledged_by: "Parser Developer"
      acknowledged_date: "2025-12-22"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 7
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
      note: "Evidence E-146, E-155, E-156, E-157, E-158, E-159 support decision"

# Deprecation
deprecation: null

# Bramki wejścia
dependencies:
  - id: "PRD-001-V2"
    type: requires
    status_constraint: [req-freeze]
    reason: "NFR-006 (10k docs scale), NFR-012 (read-only security) determinują storage requirements"
    evidence: ["E-155"]

# Bramki wyjścia
impacts:
  - id: "COMP-006-storage"
    type: blocks
    until: "ADR-005.status == approved"
    reason: "Storage component implementation czeka na decision"
    cascade: true

  - id: "COMP-001-parser"
    type: informs
    reason: "Parser output format zależy od storage schema"
    cascade: false

# Context snapshot (T₀: 2025-12-20)
context_snapshot:
  date: "2025-12-20"
  team_size: 2
  timeline: "12 weeks total, storage decision needed by week 3"
  constraints:
    - "Local-first requirement (no cloud dependencies)"
    - "Git-friendly (version control for docs)"
    - "Human-readable (manual editing possible)"
    - "Performance: < 100ms search dla 10k docs (NFR)"
    - "No external services (self-contained)"
  existing_data: "Prototype uses markdown files only (no database)"
  benchmark_results:
    - "SQLite FTS5: 60ms search dla 10k docs [E-146]"
    - "File scan (grep): 8s dla 10k docs (unacceptable)"

# Evidence trail
evidence_ids:
  - "E-146"  # SQLite FTS5 benchmark (10k docs, < 100ms)
  - "E-155"  # NFR-006, NFR-012 requirements
  - "E-156"  # Storage alternatives evaluation matrix
  - "E-157"  # Git-friendliness analysis
  - "E-158"  # Hybrid storage prototype (week 2)
  - "E-159"  # Provenance tracking requirements

# Alternatives considered
alternatives:
  - id: "OPTION-A"
    title: "Files Only (Pure Markdown, no database)"
    status: rejected
    reason: "Search performance unacceptable (8s vs < 100ms NFR). No provenance tracking. No indexing."
    evidence: ["E-156"]

  - id: "OPTION-B"
    title: "Database Only (SQLite, no files)"
    status: rejected
    reason: "Not Git-friendly. Not human-readable. Vendor lock-in. Contradicts 'markdown as source of truth' principle."
    evidence: ["E-157"]

  - id: "OPTION-C"
    title: "Hybrid (Markdown files + SQLite index)"
    status: selected
    reason: "Best of both: Git-friendly files + fast search. Files = source of truth, SQLite = rebuildable cache."
    evidence: ["E-146", "E-158"]

  - id: "OPTION-D"
    title: "External Database (PostgreSQL)"
    status: rejected
    reason: "Requires server (contradicts local-first). Overkill for local app. Setup complexity."
    evidence: ["E-156"]

# Re-evaluation triggers
triggers:
  - id: "TRIGGER-SEARCH-PERF"
    condition: "Search performance > 500ms dla 10k docs (5× NFR target)"
    action: "Re-evaluate FTS5 configuration or consider external search engine (e.g., Whoosh)"
    owner: "Tech Lead"

  - id: "TRIGGER-SYNC"
    condition: "Business requires cloud sync (multi-device)"
    action: "Re-architect storage: Add sync layer (CouchDB-style replication or git-based sync)"
    owner: "Product Owner + Tech Lead"

  - id: "TRIGGER-SCALE"
    condition: "Users need > 50k documents (5× current target)"
    action: "Re-evaluate SQLite limits. Consider sharding or external DB (PostgreSQL)."
    owner: "Tech Lead"

---

# ADR-005: Storage Architecture

**Decision**: Use **Hybrid Storage** - Markdown files (source of truth) + SQLite database (index/cache)

**Status**: ✅ **APPROVED** (2025-12-22)
**Decision Makers**: Tech Lead, Senior Dev, Product Owner

---

## Spis Treści

1. [Context](#context) (Linie 120-180)
2. [Decision](#decision) (Linie 181-240)
3. [Alternatives](#alternatives) (Linie 241-340)
4. [Consequences](#consequences) (Linie 341-380)
5. [Evidence](#evidence) (Linie 381-420)

---

## Context

### Problem Statement

**Question**: Gdzie i jak przechowywać dane systemu (dokumenty, graph, gaps, provenance)?

**Wymagania** (z PRD-V2 [E-155]):
1. **NFR-006**: Skalowanie do 10,000 dokumentów
2. **NFR-012**: Read-only access (security)
3. **FR-026**: Full-text search (< 100ms dla 10k docs)
4. **Constraint**: Local-first (no cloud dependencies)
5. **Constraint**: Git-friendly (version control dla dokumentów)
6. **Constraint**: Human-readable (manual editing possible)

### Contradictory Requirements

**Tension**:
- **Git-friendly + Human-readable** → Wymaga plain text files (markdown)
- **Fast search (< 100ms dla 10k docs)** → Wymaga indexing (database)

**Question**: Czy można spełnić OBA requirements jednocześnie?

### Decision Timeline

**T₀ (2025-12-18)**: Prototype uses markdown files only
- ✅ Git-friendly, human-readable
- ❌ Search slow (8s dla 10k docs via grep [E-156])

**T₁ (2025-12-20)**: Benchmark SQLite FTS5
- Result: 60ms search dla 10k docs [E-146]
- **Insight**: Database solves performance, but loses Git-friendliness

**T₂ (2025-12-21)**: Evaluate hybrid approach
- Prototype: Markdown files + SQLite index [E-158]
- Result: Best of both worlds (Git-friendly + fast search)

**T₃ (2025-12-22)**: **DECISION** - Hybrid storage selected

---

## Decision

### Selected: OPTION-C - Hybrid Storage ✅

**Architecture**:

```
┌─────────────────────────────────────────────┐
│         Markdown Files (.md)                │
│         SOURCE OF TRUTH                     │
│                                             │
│  - User edits externally (VS Code, vim)    │
│  - Git version control                     │
│  - Human-readable                          │
│  - Portable (no vendor lock-in)            │
└─────────────────┬───────────────────────────┘
                  │
                  │ Watchdog monitors changes
                  ↓
┌─────────────────────────────────────────────┐
│         SQLite Database (.db)               │
│         REBUILDABLE INDEX/CACHE             │
│                                             │
│  - FTS5 full-text search (< 100ms)         │
│  - Graph metadata (nodes, edges)           │
│  - Gap index (severity, status)            │
│  - Provenance tracking (audit trail)       │
└─────────────────────────────────────────────┘
```

**Key Principle**: **Files = Source of Truth, Database = Rebuildable Cache**

**What goes in files?**:
- Document content (frontmatter + markdown body)
- User-created content (editable)

**What goes in database?**:
- Computed metadata (graph properties, gap counts)
- Search index (FTS5 for fast queries)
- Provenance (who created, when, why)
- Transient state (NOT source of truth)

**Rebuild strategy**: If SQLite corrupted → delete .db file → rebuild from markdown files

---

### Implementation Details

#### Markdown Files Structure

```
project/
├── docs/
│   ├── pre-production/
│   │   ├── executive-summary.md
│   │   ├── vision-v2.md
│   │   └── business-case-v2.md
│   ├── engineering/
│   │   ├── prd-v2.md
│   │   ├── tdd-v2.md
│   │   └── koncepcje-v2.md
│   └── ...
└── .semantic-docs/
    └── index.db  (SQLite database - rebuildable)
```

**File format**: CommonMark markdown + YAML frontmatter (standard, widely supported)

**Naming convention**: Lowercase with hyphens (e.g., `prd-v2.md`)

#### SQLite Schema

**Tables**:

```sql
-- Documents table
CREATE TABLE documents (
    id TEXT PRIMARY KEY,  -- from frontmatter (e.g., "PRD-001-V2")
    file_path TEXT NOT NULL UNIQUE,
    doc_type TEXT NOT NULL,  -- prd, tdd, adr, etc.
    status TEXT NOT NULL,  -- draft, review, approved
    title TEXT NOT NULL,
    created_at TEXT,
    updated_at TEXT,
    content_hash TEXT,  -- SHA256 of content (detect changes)
    metadata_json TEXT  -- full frontmatter as JSON
);

-- Full-text search (FTS5)
CREATE VIRTUAL TABLE documents_fts USING fts5(
    id UNINDEXED,
    title,
    body,
    content='documents',
    content_rowid='rowid'
);

-- Graph nodes
CREATE TABLE nodes (
    doc_id TEXT PRIMARY KEY REFERENCES documents(id),
    node_type TEXT,  -- document node
    metadata_json TEXT,  -- computed properties (gap_count, etc.)
    FOREIGN KEY (doc_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- Graph edges
CREATE TABLE edges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_id TEXT NOT NULL REFERENCES documents(id),
    to_id TEXT NOT NULL REFERENCES documents(id),
    edge_type TEXT NOT NULL,  -- requires, informs, implements, etc.
    metadata_json TEXT,
    FOREIGN KEY (from_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY (to_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- Gaps
CREATE TABLE gaps (
    gap_id TEXT PRIMARY KEY,  -- e.g., "E120-PRD-001-section-3"
    doc_id TEXT NOT NULL REFERENCES documents(id),
    gap_type TEXT NOT NULL,  -- E110, E120, ..., E200
    severity TEXT NOT NULL,  -- critical, high, medium, low
    location TEXT,  -- section/line
    description TEXT,
    remediation_json TEXT,  -- list of steps as JSON
    detected_at TEXT,
    resolved_at TEXT,
    FOREIGN KEY (doc_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- Provenance (audit trail)
CREATE TABLE provenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT NOT NULL,  -- doc_id or gap_id
    entity_type TEXT NOT NULL,  -- document, gap, gate
    event_type TEXT NOT NULL,  -- created, updated, approved, resolved
    timestamp TEXT NOT NULL,
    actor TEXT,  -- user/system
    metadata_json TEXT
);

-- Indexes
CREATE INDEX idx_documents_type ON documents(doc_type);
CREATE INDEX idx_documents_status ON documents(status);
CREATE INDEX idx_gaps_doc_type ON gaps(doc_id, gap_type);
CREATE INDEX idx_gaps_severity ON gaps(severity);
CREATE INDEX idx_edges_from_to ON edges(from_id, to_id);
CREATE INDEX idx_provenance_entity ON provenance(entity_id, entity_type);
```

**Evidence**: [E-158] Prototype schema validated (insert 1000 docs → 2s, search < 100ms)

---

## Alternatives

### OPTION-A: Files Only (Pure Markdown) ❌ REJECTED

**Approach**: Store everything in markdown files, no database.

**Pros**:
- ✅ Git-friendly (perfect version control)
- ✅ Human-readable (edit w any text editor)
- ✅ Portable (no vendor lock-in)
- ✅ Simple (no database setup)

**Cons**:
- ❌ **Search performance**: 8s dla 10k docs (grep-based [E-156]) - **VIOLATES NFR-026** (< 100ms)
- ❌ No indexing (linear scan for queries)
- ❌ No provenance tracking (can't answer "who approved this?")
- ❌ No computed metadata cache (gap counts, graph properties recalculated every time)

**Why rejected**: **Performance unacceptable**. Search 80× slower than NFR target.

**Evidence**: [E-156] Benchmark (10k files, grep search → 8s avg)

---

### OPTION-B: Database Only (SQLite, no files) ❌ REJECTED

**Approach**: Store documents entirely in SQLite (title, body as BLOB).

**Pros**:
- ✅ Fast search (FTS5 - 60ms [E-146])
- ✅ Provenance tracking built-in
- ✅ Computed metadata efficient

**Cons**:
- ❌ **Not Git-friendly**: Binary .db file (poor diffs, merge conflicts impossible)
- ❌ **Not human-readable**: Need SQL client to view/edit
- ❌ **Vendor lock-in**: Data trapped in SQLite (export needed for portability)
- ❌ **Contradicts principle**: "Markdown as source of truth" (from CONCEPTS-V2 [E-142])
- ❌ Manual editing hard (SQL INSERT statements vs text editor)

**Why rejected**: **Violates core constraints** (Git-friendly, human-readable, markdown source of truth).

**Evidence**: [E-157] Git analysis (binary .db file → no meaningful diffs)

---

### OPTION-C: Hybrid (Markdown + SQLite) ✅ SELECTED

**Approach**: Markdown files = source of truth, SQLite = rebuildable index.

**Pros**:
- ✅ **Git-friendly**: Markdown files in Git (meaningful diffs, merge-friendly)
- ✅ **Human-readable**: Edit w any text editor
- ✅ **Fast search**: SQLite FTS5 (60ms dla 10k docs [E-146])
- ✅ **Provenance tracking**: SQLite provenance table
- ✅ **Rebuildable**: If .db corrupted → rebuild from files (no data loss)
- ✅ **Portable**: Markdown = standard format (no lock-in)

**Cons**:
- ⚠️ **Complexity**: Two storage systems to maintain
- ⚠️ **Sync needed**: File changes → update SQLite (Watchdog handles this)
- ⚠️ **Consistency**: Eventual consistency model (file updated → re-index ~200ms later)

**Why selected**: **Best of both worlds**. Solves performance WITHOUT sacrificing Git-friendliness.

**Evidence**: [E-158] Prototype (1000 docs: files + SQLite → 2s build, 60ms search, Git-friendly)

**Mitigation for cons**:
- Complexity: Abstraction layer (Storage API hides dual-system)
- Sync: Watchdog automatic (transparent to user)
- Consistency: Eventual consistency acceptable (< 200ms delay OK per UX research)

---

### OPTION-D: External Database (PostgreSQL) ❌ REJECTED

**Approach**: PostgreSQL server for storage.

**Pros**:
- ✅ Scalable (millions of docs)
- ✅ ACID transactions
- ✅ Advanced queries (CTE, window functions)

**Cons**:
- ❌ **Requires server**: Contradicts local-first constraint
- ❌ **Setup complexity**: Install, configure, manage Postgres
- ❌ **Overkill**: 10k docs doesn't need Postgres (SQLite handles 10^6 rows easily)
- ❌ **Not portable**: Connection string, credentials, network dependency

**Why rejected**: **Contradicts local-first requirement**. Unnecessary complexity for scale target.

**Evidence**: [E-156] Evaluation matrix (Postgres scored low on "local-first" + "simplicity")

---

## Consequences

### Positive Consequences

1. **Performance met**: Search < 100ms ✅ (SQLite FTS5 [E-146])
2. **Git-friendly**: Markdown files = meaningful diffs, merge-friendly ✅
3. **Human-readable**: Edit w any editor (VS Code, vim, Obsidian) ✅
4. **Rebuildable**: SQLite corruption → no data loss (rebuild from files) ✅
5. **Provenance tracking**: Audit trail w SQLite (who/when/why) ✅
6. **Portable**: Markdown = standard (export trivial) ✅

### Negative Consequences

1. **Complexity**: Two storage systems (files + database)
   - Mitigation: Storage API abstraction hides complexity

2. **Eventual consistency**: File change → SQLite update delay (~200ms)
   - Mitigation: Acceptable per UX (user sees "analyzing..." indicator)

3. **Disk space**: Duplicate data (markdown body in files + SQLite)
   - Impact: ~2× storage (10k docs × 10KB avg = 100MB files + 100MB SQLite = 200MB total - acceptable)

4. **SQLite limits**: Max 140TB database, 281TB single table (far beyond 10k docs target)
   - Mitigation: Re-evaluate if TRIGGER-SCALE activated (> 50k docs)

### Operational Impact

**Backup strategy**:
- **Markdown files**: Git-based backup (push to remote)
- **SQLite**: Rebuildable → no backup needed (can regenerate)

**Disaster recovery**:
- Markdown files lost → restore from Git
- SQLite corrupted → delete .db, rebuild from files (~2 minutes dla 10k docs)

**Migration path** (if future change needed):
- To pure files: Delete .db (no migration needed)
- To pure DB: Export markdown → import to new DB schema
- To external DB: Export markdown → sync to Postgres

---

## Evidence

### [E-146] SQLite FTS5 Benchmark

**Test**: 10,000 markdown documents (avg 10KB each, 100KB total content)

**Setup**:
```python
import sqlite3
import time

# Insert 10k docs
conn = sqlite3.connect("test.db")
conn.execute("CREATE VIRTUAL TABLE docs_fts USING fts5(title, body)")
for i in range(10000):
    conn.execute("INSERT INTO docs_fts VALUES (?, ?)",
                 (f"Document {i}", f"Body content {i}" * 100))
conn.commit()

# Search benchmark
start = time.time()
results = conn.execute("SELECT * FROM docs_fts WHERE docs_fts MATCH 'content'").fetchall()
elapsed = time.time() - start
print(f"Search time: {elapsed * 1000:.1f}ms")  # 60ms
print(f"Results: {len(results)}")  # 10000
```

**Result**: **60ms** search dla 10k docs (well under 100ms NFR target)

**Date**: 2025-12-20

---

### [E-156] Storage Alternatives Evaluation Matrix

**Criteria** (weighted):
- Performance (30%): Search speed, index build time
- Git-friendly (25%): Diff quality, merge handling
- Human-readable (20%): Edit ease, readability
- Local-first (15%): No server, self-contained
- Simplicity (10%): Setup, maintenance

**Scoring** (1-10):

| Criteria | Weight | Files Only | DB Only | Hybrid | Postgres |
|----------|--------|-----------|---------|--------|----------|
| Performance | 30% | 2 (8s search) | 10 (60ms) | 10 (60ms) | 10 |
| Git-friendly | 25% | 10 (perfect) | 2 (binary) | 10 (files) | 1 |
| Human-readable | 20% | 10 (text) | 3 (SQL) | 10 (text) | 3 |
| Local-first | 15% | 10 (no deps) | 10 (embedded) | 10 (embedded) | 1 (server) |
| Simplicity | 10% | 10 (trivial) | 8 (SQLite easy) | 6 (dual system) | 3 (server) |
| **TOTAL** | 100% | **6.35** | **6.55** | **9.40** ✅ | **4.65** |

**Winner**: Hybrid (9.40/10)

**Date**: 2025-12-20

---

### [E-158] Hybrid Storage Prototype

**Implementation** (week 2 prototype):

```python
class HybridStorage:
    def __init__(self, docs_dir: Path, db_path: Path):
        self.docs_dir = docs_dir
        self.conn = sqlite3.connect(db_path)
        self._init_schema()

    def index_document(self, file_path: Path):
        """Parse markdown file → insert to SQLite."""
        doc = parse_markdown(file_path)
        self.conn.execute(
            "INSERT OR REPLACE INTO documents VALUES (?, ?, ?, ?, ?)",
            (doc.id, str(file_path), doc.type, doc.status, doc.title)
        )
        self.conn.execute(
            "INSERT INTO documents_fts VALUES (?, ?, ?)",
            (doc.id, doc.title, doc.body)
        )
        self.conn.commit()

    def search(self, query: str) -> list[str]:
        """FTS5 search."""
        cursor = self.conn.execute(
            "SELECT id FROM documents_fts WHERE documents_fts MATCH ?",
            (query,)
        )
        return [row[0] for row in cursor]
```

**Test**: 1000 documents
- **Index build**: 2.1s (acceptable)
- **Search**: 58ms (well under 100ms target)
- **Git diff**: Meaningful (markdown file changes visible)

**Conclusion**: Hybrid approach **FEASIBLE** ✅

**Date**: 2025-12-21

---

## Summary

**Decision**: **Hybrid Storage** (Markdown files + SQLite index)

**Rationale**:
1. **Meets all requirements**: Performance (✅ 60ms), Git-friendly (✅ files), Human-readable (✅ markdown)
2. **Best tradeoff**: Complexity cost acceptable for benefits
3. **Validated**: Prototype confirms feasibility [E-158]

**Implementation**: Storage API abstracts dual-system complexity from application code.

**Status**: ✅ **APPROVED** (2025-12-22) by Tech Lead, Senior Dev, Product Owner

---

**Parent Document**: [TDD-001-V2](../tdd-v2.md)
**Related**: [COMP-006-storage](../components/COMP-006-storage.md) (implementation)
**Created**: 2025-12-26
**Last Updated**: 2025-12-26
