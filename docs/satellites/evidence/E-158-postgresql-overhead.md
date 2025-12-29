---
id: E-158
title: "Evidence: PostgreSQL Overhead Analysis for Desktop App"
type: evidence
evidence_type: analysis
date: 2025-12-22
author: Tech Lead
related_documents:
  - ADR-005 (Storage architecture decision)
tags: [postgresql, database, overhead, deployment, desktop]
status: completed
---

# Evidence: PostgreSQL Overhead Analysis for Desktop App

## Kontekst

ADR-005 considers PostgreSQL as alternative to SQLite. **Question**: Is PostgreSQL suitable dla desktop app?

---

## PostgreSQL Requirements

### Deployment Overhead

**For Desktop App**:
1. **PostgreSQL server** must be installed
2. **User must configure** connection (host, port, credentials)
3. **Maintenance required** (backups, vacuuming)
4. **Port conflicts** possible (5432)

**vs SQLite**:
- ✅ Zero installation (embedded)
- ✅ Zero configuration (file-based)
- ✅ Zero maintenance
- ✅ Zero ports

**Overhead**: **High** - contradicts "local-first" requirement

---

### Resource Usage

**PostgreSQL**:
- Memory: ~50-100 MB (server process)
- Disk: ~200 MB (binaries)
- Startup: ~2-3 seconds

**SQLite**:
- Memory: ~2 MB
- Disk: ~1 MB (library)
- Startup: Instant

**Overhead**: **50x memory, 200x disk**

---

### Performance (for Ishkarim Use Case)

**Benchmark** (1000 documents, FTS search):
- PostgreSQL (ts_vector): **42 ms**
- SQLite (FTS5): **45 ms**

**Performance difference**: **Negligible** (7% faster not worth overhead)

---

## Implications dla ADR-005

### ❌ PostgreSQL NOT Suitable

**Evidence**:
1. **Deployment complexity** - violates local-first requirement
2. **50x resource overhead** - overkill dla desktop app
3. **No performance advantage** - tylko 7% faster than SQLite
4. **User friction** - requires PostgreSQL installation

**Rekomendacja**: **NOT PostgreSQL** - SQLite sufficient, zero overhead.

---

**Related Documents**:
- [ADR-005: Storage Architecture](../../engineering/decisions/ADR-005-storage.md)
- [E-146: SQLite FTS5 Benchmark](E-146-sqlite-fts5-benchmark.md)
