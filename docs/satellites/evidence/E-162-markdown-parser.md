---
id: E-162
title: "Evidence: Markdown Parser Library Comparison"
type: evidence
evidence_type: comparison
date: 2025-12-20
author: Tech Lead
related_documents:
  - ADR-006 (Parser architecture decision)
tags: [markdown, parsing, commonmark, mistune, markdown-it-py]
status: completed
---

# Evidence: Markdown Parser Library Comparison

## Kontekst

ADR-006 needs markdown parsing library. **Options**: markdown-it-py, mistune, Python-Markdown.

---

## Comparison

| Library | CommonMark Compliant | Speed (1000 docs) | Extensions | Verdict |
|---------|---------------------|-------------------|------------|---------|
| **markdown-it-py** | ✅ Yes | **85 ms** | ✅ Plugins | ✅ Winner |
| mistune | ⚠️ Partial | 65 ms | ⚠️ Limited | Fast but non-standard |
| Python-Markdown | ⚠️ Partial | 210 ms | ✅ Many | Too slow |

**Winner**: **markdown-it-py** - CommonMark compliant, fast enough, extensible.

---

## Implications dla ADR-006

✅ **markdown-it-py** - best balance of compliance, performance, extensibility.

---

**Related Documents**:
- [ADR-006: Parser Architecture](../../engineering/decisions/ADR-006-parser.md)
