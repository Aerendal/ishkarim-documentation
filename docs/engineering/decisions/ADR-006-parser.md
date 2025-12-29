---
id: ADR-006
title: "ADR-006: Parser Architecture"
type: adr
status: approved
decision_date: 2025-12-20
parent: TDD-001-V2

context_snapshot:
  requirements:
    - "Parse YAML frontmatter (all documents have frontmatter)"
    - "Parse markdown to AST (need section hierarchy H1-H6)"
    - "CommonMark compliant (standard markdown spec)"
    - "Performance: < 50ms per document (NFR-001)"

evidence_ids:
  - "E-149"  # Benchmark: python-frontmatter + markdown-it-py (< 10ms/doc)
  - "E-162"  # mistune comparison (faster but less compliant)

alternatives:
  - id: "OPT-CUSTOM"
    title: "Custom parser (regex-based)"
    status: rejected
    reason: "Reinventing wheel, edge cases nightmare, maintenance burden"

  - id: "OPT-MISTUNE"
    title: "mistune (fast parser)"
    status: rejected
    reason: "Not fully CommonMark compliant, less structured AST"

  - id: "OPT-FRONTMATTER-MARKDOWNIT"
    title: "python-frontmatter + markdown-it-py"
    status: selected
    reason: "Standard tools, CommonMark compliant, fast (< 10ms/doc), AST output"
---

# ADR-006: Parser Architecture

**Decision**: Use **python-frontmatter** (YAML) + **markdown-it-py** (markdown)

**Status**: ✅ APPROVED

---

## Context

**Problem**: Parse markdown files with YAML frontmatter → structured Document object.

**Needs**:
1. **YAML frontmatter extraction**: `---\nid: X\n---` → dict
2. **Markdown parsing**: Body → AST (headers, paragraphs, lists)
3. **Section hierarchy**: Identify H1-H6 structure
4. **Performance**: < 50ms per document (NFR-001)

---

## Decision

### python-frontmatter 1.0+ ✅

**Why**:
- ✅ Standard tool (widely used)
- ✅ Fast (< 5ms/doc [E-149])
- ✅ Simple API: `frontmatter.load(file)` → metadata + content
- ✅ Robust (handles no frontmatter, invalid YAML gracefully)

**Usage**:
```python
import frontmatter
post = frontmatter.load("doc.md")
metadata = post.metadata  # dict
body = post.content       # str
```

### markdown-it-py 3.0+ ✅

**Why**:
- ✅ CommonMark compliant (standard spec)
- ✅ AST output (structured tokens, not just HTML)
- ✅ Fast (< 10ms/doc combined [E-149])
- ✅ Plugin system (extensible if needed)

**Usage**:
```python
from markdown_it import MarkdownIt
md = MarkdownIt()
tokens = md.parse(body)  # AST
headers = [t for t in tokens if t.type == 'heading_open']
```

**Evidence**: [E-149] Benchmark: 100 docs → 840ms (8.4ms/doc avg)

---

## Alternatives

### Custom Parser ❌
**Cons**: Edge cases (nested lists, code blocks), maintenance burden
**Rejected**: Don't reinvent wheel

### mistune ❌
**Pros**: Faster (5ms/doc vs 10ms)
**Cons**: Not fully CommonMark compliant, less structured output
**Evidence**: [E-162] Comparison
**Rejected**: Compliance > speed (10ms acceptable)

---

## Consequences

**Positive**:
- ✅ Performance target met (< 50ms, actual ~10ms)
- ✅ CommonMark standard (no custom markdown dialect)
- ✅ Maintainable (standard libraries, good docs)

**Negative**:
- ⚠️ Two libraries instead of one (but both lightweight)

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
