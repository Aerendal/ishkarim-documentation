---
id: E-159
title: "Evidence: Git-Friendliness Analysis - Markdown vs Database"
type: evidence
evidence_type: analysis
date: 2025-12-22
author: Tech Lead
related_documents:
  - ADR-005 (Storage architecture decision)
tags: [git, version-control, markdown, database, diff]
status: completed
---

# Evidence: Git-Friendliness Analysis - Markdown vs Database

## Kontekst

ADR-005 emphasizes Git-friendliness. **Question**: Markdown files vs database blobs - który lepszy dla Git?

---

## Git Operations Analysis

### 1. **Diffs (git diff)**

**Markdown**:
```diff
--- ADR-001.md
+++ ADR-001.md
@@ -5,7 +5,7 @@
 title: "ADR-001: GUI Framework"
-status: draft
+status: accepted
```
- ✅ **Human-readable** diffs
- ✅ **Line-by-line** granularity

**SQLite Binary**:
```
Binary files index.db and index.db differ
```
- ❌ **No readable diffs**
- ❌ **Entire file changed** (even for 1-byte change)

**Winner**: **Markdown** - readable, meaningful diffs

---

### 2. **Merge Conflicts**

**Markdown**:
```markdown
<<<<<<< HEAD
status: accepted
=======
status: rejected
>>>>>>> branch
```
- ✅ **Resolvable** by humans
- ✅ **Standard Git workflow**

**SQLite**:
```
CONFLICT (content): Merge conflict in index.db
```
- ❌ **Binary conflict** - cannot resolve manually
- ❌ **Must rebuild** entire database

**Winner**: **Markdown** - standard merge workflow

---

### 3. **History & Blame (git log, git blame)**

**Markdown**:
```bash
$ git log ADR-001.md
commit abc123
Author: Tech Lead
Date: 2025-12-22

    Update ADR-001 status to accepted
```
- ✅ **Meaningful history** - see what changed
- ✅ **Git blame** shows who changed each line

**SQLite**:
```bash
$ git log index.db
commit xyz789
Author: System
Date: 2025-12-22

    Rebuild index
```
- ❌ **Opaque history** - no details on what changed
- ❌ **Git blame useless** (binary file)

**Winner**: **Markdown** - full Git history benefits

---

### 4. **Review (Pull Requests)**

**Markdown**:
- ✅ **GitHub/GitLab shows inline diffs**
- ✅ **Reviewers see exact changes**
- ✅ **Can comment on specific lines**

**SQLite**:
- ❌ **"Binary file changed"** message only
- ❌ **No visibility** into what changed
- ❌ **Cannot review** database changes

**Winner**: **Markdown** - full review workflow

---

## Implications dla ADR-005

### ✅ Markdown (Source of Truth) is Essential

**Evidence**:
1. **Readable diffs** - meaningful `git diff` output
2. **Mergeable** - standard conflict resolution
3. **Full history** - `git log` and `git blame` useful
4. **Reviewable** - PR workflows work

### ⚠️ SQLite Index Must Be:
- **Rebuildable** (can be deleted/regenerated)
- **Git-ignored** (not committed to repo)
- **Derived from Markdown** (cache, not source)

**Rekomendacja**: **Hybrid approach** - Markdown source (Git-friendly) + SQLite cache (performance).

---

**Related Documents**:
- [ADR-005: Storage Architecture](../../engineering/decisions/ADR-005-storage.md)
- [E-157: Hybrid Storage Prototype](E-157-hybrid-storage.md)
