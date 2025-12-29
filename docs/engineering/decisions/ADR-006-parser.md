---
id: ADR-006
title: "ADR-006: Parser Architecture"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-20
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-20"
  status_reason: "Decision approved after benchmarking - python-frontmatter + markdown-it-py selected"
  next_review_date: "2026-12-20"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-20"
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
  note: "ADR approved - establishes parser libraries"

version_history:
  - version: "1.0.0"
    date: "2025-12-20"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: python-frontmatter + markdown-it-py for parsing"
    breaking: false
    changes:
      - "Evaluated 3 options: Custom parser, mistune, python-frontmatter + markdown-it-py"
      - "Selected python-frontmatter 1.0+ (YAML) + markdown-it-py 3.0+ (markdown)"
      - "Rejected Custom parser (reinventing wheel, maintenance burden)"
      - "Rejected mistune (not fully CommonMark compliant)"
    impacts:
      - id: "COMP-001-parser"
        impact_type: "unblocked"
        description: "Parser component can proceed with selected libraries"
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes parser libraries"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending:
    - id: "COMP-001-parser"
      notified_date: "2025-12-20"
      acknowledged: true
      acknowledged_by: "Parser Developer"
      acknowledged_date: "2025-12-20"

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 9
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
      note: "Evidence E-149, E-162 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "TDD-001-V2"
    type: requires
    reason: "Parser requirements defined in TDD"

impacts:
  - id: "COMP-001-parser"
    type: blocks
    until: "ADR-006.status == approved"
    reason: "Parser implementation needs library choice"
  - id: "TDD-001-V2"
    type: informs
    reason: "Architecture updated with parser libraries"

context_snapshot:
  date: "2025-12-20"
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
