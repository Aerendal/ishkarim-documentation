---
id: E-156
title: "Evidence: File-Only Storage Performance Measurement"
type: evidence
evidence_type: benchmark
date: 2025-12-22
author: Tech Lead
related_documents:
  - ADR-005 (Storage architecture decision)
tags: [storage, filesystem, performance, search, benchmark]
status: completed
---

# Evidence: File-Only Storage Performance Measurement

## Kontekst

ADR-005 evaluates pure filesystem approach (no database). **Question**: Jak szybko można przeszukać 1000 markdown files bez indexu?

---

## Benchmark

**Setup**:
- 1000 markdown files w `/docs`
- Search query: "error handling" (grep-like search)
- Platform: Linux, SSD storage

**Implementation**:
```python
from pathlib import Path
import re

def search_files(query: str, directory: Path):
    results = []
    for path in directory.rglob("*.md"):
        content = path.read_text()
        if re.search(query, content, re.IGNORECASE):
            results.append(path)
    return results

# Benchmark
start = time.perf_counter()
results = search_files("error handling", Path("/docs"))
elapsed = time.perf_counter() - start
```

**Result**: **8.2 seconds** dla 1000 files

---

## Analysis

**Performance**:
- 8.2 seconds >> **60 ms NFR target** ❌
- **137x slower** than requirement

**Reason**: Sequential file I/O (read all files, no index)

**Verdict**: ❌ **File-only DOES NOT meet performance requirements**

---

## Implications dla ADR-005

**Evidence AGAINST file-only approach**:
- 8.2 seconds unacceptable dla interactive search
- Needs indexing solution (SQLite FTS or similar)

**Rekomendacja**: **NOT file-only** - must use database index.

---

**Related Documents**:
- [ADR-005: Storage Architecture](../../engineering/decisions/ADR-005-storage.md)
- [E-146: SQLite FTS5 Benchmark](E-146-sqlite-fts5-benchmark.md)
- [E-157: Hybrid Storage Prototype](E-157-hybrid-storage.md)
