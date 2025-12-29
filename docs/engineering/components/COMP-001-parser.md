---
id: COMP-001
title: "COMP-001: Parser Component"
type: component
domain: architecture
status: draft
created: 2025-12-26
owner: Tech Lead
parent: TDD-001-V2

dependencies:
  - id: "ADR-006"
    type: requires
    status_constraint: [approved]
    reason: "Parser implementation follows ADR-006 decisions (python-frontmatter + markdown-it-py)"

  - id: "API-SPEC-001"
    type: implements
    reason: "Parser implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

  - id: "COMP-002-validator"
    type: blocks
    reason: "Validator depends on Parser output (Document object)"

  - id: "COMP-006-storage"
    type: informs
    reason: "Storage schema derived from Document model"

context_snapshot:
  libraries:
    - "python-frontmatter 1.0+"
    - "markdown-it-py 3.0+"
  performance_target: "< 50ms per document (NFR-001)"
  input_format: "Markdown with YAML frontmatter"

evidence_ids:
  - "E-149"  # Benchmark: 8.4ms/doc avg
  - "E-167"  # Parser implementation prototype
---

# COMP-001: Parser Component

**Responsibility**: Parse markdown files → structured `Document` objects

**Status**: Draft specification

---

## Spis Treści

1. [Overview](#overview) (Linie 55-80)
2. [Public Interface](#public-interface) (Linie 81-130)
3. [Internal Architecture](#internal-architecture) (Linie 131-200)
4. [Data Structures](#data-structures) (Linie 201-260)
5. [Algorithms](#algorithms) (Linie 261-300)
6. [Error Handling](#error-handling) (Linie 301-340)
7. [Performance](#performance) (Linie 341-360)
8. [Testing Strategy](#testing-strategy) (Linie 361-400)

---

## Overview

### Responsibility

**Input**: Markdown file path (`.md` with YAML frontmatter)
**Output**: `Document` object (Pydantic model)

**Core functions**:
1. Extract YAML frontmatter → dict
2. Parse markdown body → AST (sections, paragraphs, lists)
3. Identify section hierarchy (H1-H6)
4. Detect inline references ([E-XXX], ADR-XXX, etc.)
5. Construct `Document` object

### Dependencies

**External libraries**:
- `python-frontmatter 1.0+`: YAML extraction
- `markdown-it-py 3.0+`: Markdown parsing
- `pydantic 2.5+`: Data validation (Document model)

**Internal dependencies**:
- `models.document.Document`: Output data model
- `models.document.Section`: Section data model

---

## Public Interface

### ParserAPI Class

```python
# src/core/parser.py

from pathlib import Path
from typing import Optional
from models.document import Document, Section

class ParserAPI:
    """Public API for parsing markdown documents."""

    def parse_document(self, file_path: Path) -> Document:
        """
        Parse markdown file to Document object.

        Args:
            file_path: Path to .md file

        Returns:
            Document: Parsed document with frontmatter + sections

        Raises:
            FileNotFoundError: If file doesn't exist
            YAMLError: If frontmatter YAML invalid
            ParseError: If markdown parsing fails
        """

    def parse_string(self, content: str, file_path: Optional[Path] = None) -> Document:
        """
        Parse markdown string (for testing/in-memory use).

        Args:
            content: Markdown string with frontmatter
            file_path: Optional path (for metadata)

        Returns:
            Document: Parsed document
        """

    def extract_frontmatter(self, content: str) -> dict:
        """
        Extract YAML frontmatter only (no markdown parsing).

        Args:
            content: Markdown string

        Returns:
            dict: Parsed YAML frontmatter

        Raises:
            YAMLError: If frontmatter invalid
        """

    def parse_sections(self, markdown: str) -> list[Section]:
        """
        Parse markdown to section hierarchy.

        Args:
            markdown: Markdown body (no frontmatter)

        Returns:
            list[Section]: Hierarchical section tree
        """

    def detect_references(self, content: str) -> list[str]:
        """
        Detect inline references ([E-XXX], ADR-XXX, etc.).

        Args:
            content: Markdown content

        Returns:
            list[str]: Found references (e.g., ["E-001", "ADR-005"])
        """
```

---

## Internal Architecture

### Component Structure

```
ParserAPI (public interface)
    ↓
FrontmatterExtractor (uses python-frontmatter)
    ↓
MarkdownParser (uses markdown-it-py)
    ↓
SectionBuilder (constructs hierarchy)
    ↓
ReferenceDetector (regex patterns)
    ↓
DocumentBuilder (assembles final Document)
```

### Internal Classes

#### 1. FrontmatterExtractor

```python
class FrontmatterExtractor:
    """Extract YAML frontmatter from markdown."""

    def extract(self, content: str) -> tuple[dict, str]:
        """
        Returns: (frontmatter_dict, body_without_frontmatter)
        """
        import frontmatter
        post = frontmatter.loads(content)
        return post.metadata, post.content
```

#### 2. MarkdownParser

```python
from markdown_it import MarkdownIt

class MarkdownParser:
    """Parse markdown to AST using markdown-it-py."""

    def __init__(self):
        self.md = MarkdownIt()

    def parse(self, markdown: str) -> list:
        """
        Returns: Token list (markdown-it-py AST)
        """
        return self.md.parse(markdown)
```

#### 3. SectionBuilder

```python
class SectionBuilder:
    """Build hierarchical section structure from tokens."""

    def build_hierarchy(self, tokens: list) -> list[Section]:
        """
        Args:
            tokens: markdown-it-py tokens

        Returns:
            list[Section]: Top-level sections with nested children
        """
        # Algorithm: Stack-based hierarchy construction
```

#### 4. ReferenceDetector

```python
import re

class ReferenceDetector:
    """Detect inline references using regex patterns."""

    PATTERNS = {
        'evidence': r'\[E-\d+\]',
        'adr': r'\[?ADR-\d+\]?',
        'document': r'\[?[A-Z]+-[A-Z]+-\d+\]?',
    }

    def detect(self, content: str) -> dict[str, list[str]]:
        """
        Returns: {'evidence': ['E-001', ...], 'adr': ['ADR-005', ...], ...}
        """
```

---

## Data Structures

### Section Model

```python
from pydantic import BaseModel
from typing import Optional

class Section(BaseModel):
    """Represents a markdown section (H1-H6)."""

    level: int  # 1-6 (H1=1, H2=2, etc.)
    title: str
    content: str  # Section body (markdown)
    line_start: int  # Line number in file
    line_end: int
    children: list['Section'] = []  # Nested sections
    parent: Optional['Section'] = None

    class Config:
        arbitrary_types_allowed = True  # For parent reference
```

### Document Model

```python
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime

class Document(BaseModel):
    """Parsed markdown document."""

    # From frontmatter
    id: str = Field(..., pattern=r'^[A-Z]+-[A-Z0-9]+-\d+')
    title: str
    type: str  # prd, tdd, adr, etc.
    status: str  # draft, review, approved
    frontmatter: dict  # Full YAML

    # From parsing
    sections: list[Section]
    body: str  # Raw markdown body
    references: dict[str, list[str]]  # Detected references

    # Metadata
    file_path: Path
    content_hash: str  # SHA256 of content
    last_modified: datetime
    line_count: int
```

---

## Algorithms

### Section Hierarchy Construction (Stack-Based)

**Problem**: Convert flat token list → hierarchical section tree

**Algorithm**:
```python
def build_hierarchy(tokens: list) -> list[Section]:
    """
    Stack-based hierarchy construction.

    Example:
    Tokens: [H1, H2, H2, H3, H1]
    Result:
        H1
          H2
          H2
            H3
        H1
    """
    stack = []  # Stack of (level, Section)
    root_sections = []

    for token in tokens:
        if token.type == 'heading_open':
            level = int(token.tag[1])  # h1 → 1, h2 → 2
            section = Section(level=level, ...)

            # Pop stack until parent found
            while stack and stack[-1][0] >= level:
                stack.pop()

            if stack:
                # Nested section
                parent = stack[-1][1]
                parent.children.append(section)
                section.parent = parent
            else:
                # Top-level section
                root_sections.append(section)

            stack.append((level, section))

    return root_sections
```

**Complexity**: O(n) where n = number of tokens

---

## Error Handling

### Error Types

#### 1. FileNotFoundError

**When**: `file_path` doesn't exist
**Handling**: Raise immediately (caller handles)

```python
if not file_path.exists():
    raise FileNotFoundError(f"Document not found: {file_path}")
```

#### 2. YAMLError (Invalid Frontmatter)

**When**: YAML syntax error in frontmatter
**Handling**: Graceful degradation - parse what's possible, report as gap

```python
try:
    metadata = frontmatter.load(file)
except yaml.YAMLError as e:
    # Create minimal Document with error
    return Document(
        id="UNKNOWN",
        title=f"Parse Error: {file_path.name}",
        frontmatter={'_error': str(e)},
        ...
    )
```

#### 3. ParseError (Markdown Parsing Fails)

**When**: markdown-it-py crashes (rare - robust library)
**Handling**: Log error, return partial Document

```python
try:
    tokens = md.parse(body)
except Exception as e:
    logger.error(f"Markdown parse failed: {file_path}", exc_info=True)
    # Return Document with empty sections
    return Document(..., sections=[], body=body)
```

### Error Recovery Principle

**Never crash the application**. Parser errors → Document with `_error` flag → Validator detects as gap (E110/E120).

---

## Performance

### Target: < 50ms per document (NFR-001)

**Measured** (prototype [E-167]):
- python-frontmatter: ~5ms/doc
- markdown-it-py: ~10ms/doc
- Section hierarchy: ~2ms/doc
- Reference detection: ~1ms/doc
- **Total**: ~18ms/doc (well under 50ms target ✅)

### Optimization Strategies

**If performance degrades**:
1. **Lazy parsing**: Parse sections only when accessed (property getter)
2. **Caching**: Cache parsed Documents (TTL = file modification time)
3. **Parallel parsing**: `concurrent.futures` for batch parsing (10+ docs)

**Current status**: Optimization NOT needed (18ms << 50ms target)

---

## Testing Strategy

### Unit Tests

**Test coverage target**: 90%+ (critical component)

#### Test Cases

1. **Happy path**: Valid frontmatter + markdown → correct Document
2. **Missing frontmatter**: No `---` delimiters → empty frontmatter dict
3. **Invalid YAML**: Syntax error → graceful degradation
4. **Empty file**: 0 bytes → minimal Document
5. **No sections**: Plain text (no headers) → single section
6. **Nested sections**: H1 > H2 > H3 → correct hierarchy
7. **References**: Detect [E-001], ADR-005, PRD-001 → correct lists
8. **Unicode**: Non-ASCII chars (Polish, emoji) → correct parsing
9. **Large files**: 10MB markdown → performance acceptable

#### Test Structure

```python
# tests/unit/test_parser.py

import pytest
from pathlib import Path
from core.parser import ParserAPI

@pytest.fixture
def parser():
    return ParserAPI()

def test_parse_valid_document(parser):
    content = """---
id: TEST-001
title: Test Document
type: test
---

# Section 1

Content here.
"""
    doc = parser.parse_string(content)
    assert doc.id == "TEST-001"
    assert len(doc.sections) == 1
    assert doc.sections[0].level == 1

def test_invalid_yaml_graceful(parser):
    content = """---
id: TEST-001
invalid yaml here: [unclosed
---
"""
    doc = parser.parse_string(content)
    assert '_error' in doc.frontmatter  # Error captured
```

### Integration Tests

**Test with real documents**:
- Parse all documents from `/docs` directory
- Verify no crashes
- Verify all documents have valid structure

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related ADR**: [ADR-006-parser](../decisions/ADR-006-parser.md)
**Created**: 2025-12-26
