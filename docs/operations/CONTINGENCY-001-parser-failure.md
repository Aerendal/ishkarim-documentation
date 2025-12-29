---
id: CONTINGENCY-001
title: "Contingency Plan - Parser Implementation Failure"
type: contingency-plan
parent_document: COMP-001-parser
status: draft
created: 2025-12-26

triggers:
  - parser_accuracy_below_95_percent
  - performance_violation_nfr001
  - critical_bug_sprint1

rollback_criteria:
  - decision_points: [day_3, day_7, day_14]
  - escalation_path: [Developer, Tech Lead, Product Owner]
---

# Contingency Plan: Parser Failure

## Overview

Plan B dla przypadku gdy implementacja Parser (COMP-001) nie spełnia wymagań.

Ten dokument definiuje strategię awaryjną dla kluczowego komponentu systemu - parsera dokumentów Markdown z frontmatter YAML. Parser jest fundamentalnym elementem całego systemu, od którego zależy poprawność indeksowania, wyszukiwania i analizy dokumentacji.

**Cel**: Zapewnić alternatywne ścieżki implementacji w przypadku niepowodzenia pierwotnego rozwiązania opartego na python-frontmatter + markdown-it-py.

**Zakres**: Pokrywa trzy główne kategorie ryzyka:
- Dokładność parsowania YAML
- Wydajność przetwarzania
- Kompatybilność międzyplatformowa

---

## Failure Scenarios

### Scenario A: python-frontmatter Nie Parsuje YAML Poprawnie

**Trigger**: > 5% dokumentów fail parsing

**Symptomy**:
- `yaml.YAMLError` dla poprawnych plików
- Nested structures nie są parsowane (np. listy obiektów)
- Unicode issues (emoji, znaki specjalne)
- Niepoprawna interpretacja typów (string vs int, null vs "null")
- Problemy z multi-line strings

**Root Cause Analysis**:
- python-frontmatter używa PyYAML pod spodem, ale dodaje własną logikę
- Możliwe konflikty w wykrywaniu granic frontmatter (---...---)
- Edge cases w handling białych znaków
- Brak wsparcia dla custom YAML tags używanych w dokumentacji

**Plan B**: Przełączenie na PyYAML + Custom Regex

**Uzasadnienie**:
- PyYAML jest de-facto standardem w Python ecosystem
- Pełna kontrola nad logiką parsowania
- Lepsza diagnostyka błędów
- Możliwość custom error handling

**Effort Estimation**:
- **Czas**: 3 dni (1 dev)
- **Risk**: Medium (PyYAML jest bardziej verbose, wymaga więcej boilerplate)
- **Evidence**: E-270 (benchmark PyYAML accuracy: 99.5% na 1000 test cases)

**Implementation**:

```python
import yaml
import re
from pathlib import Path
from typing import Tuple
from result import Result, Ok, Err

class ParseError:
    class NoFrontmatter:
        def __str__(self):
            return "No frontmatter delimiter found"

    class InvalidYAML:
        def __init__(self, msg: str):
            self.msg = msg

        def __str__(self):
            return f"Invalid YAML: {self.msg}"

    class FileReadError:
        def __init__(self, msg: str):
            self.msg = msg

        def __str__(self):
            return f"File read error: {self.msg}"

def parse_frontmatter_custom(content: str) -> Result[Tuple[dict, str], ParseError]:
    """
    Parsuje frontmatter YAML i zwraca (metadata, markdown_content).

    Args:
        content: Pełna treść pliku Markdown

    Returns:
        Ok((metadata_dict, markdown_body)) lub Err(ParseError)
    """
    # Regex: match --- na początku, potem cokolwiek (non-greedy), potem ---
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)

    if not match:
        # Fallback: sprawdź czy to nie Windows line endings
        match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n(.*)$', content, re.DOTALL)

        if not match:
            return Err(ParseError.NoFrontmatter())

    yaml_str = match.group(1)
    markdown_body = match.group(2)

    try:
        metadata = yaml.safe_load(yaml_str)

        # Validation: frontmatter musi być dict
        if not isinstance(metadata, dict):
            return Err(ParseError.InvalidYAML(
                f"Frontmatter must be a YAML object, got {type(metadata).__name__}"
            ))

        return Ok((metadata, markdown_body))

    except yaml.YAMLError as e:
        return Err(ParseError.InvalidYAML(str(e)))

def parse_markdown_file(path: Path) -> Result[Tuple[dict, str], ParseError]:
    """
    Wczytuje i parsuje plik Markdown z frontmatter.
    """
    try:
        content = path.read_text(encoding='utf-8')
        return parse_frontmatter_custom(content)
    except Exception as e:
        return Err(ParseError.FileReadError(str(e)))

# Przykład użycia:
# result = parse_markdown_file(Path("docs/COMP-001.md"))
# match result:
#     case Ok((metadata, body)):
#         print(f"Title: {metadata.get('title')}")
#         print(f"Body length: {len(body)}")
#     case Err(error):
#         print(f"Parse failed: {error}")
```

**Testing Strategy**:
```python
# Test suite dla Plan B
test_cases = [
    # Edge case 1: Nested YAML
    """---
tags:
  - category: technical
    priority: high
  - category: documentation
    priority: medium
---
# Content""",

    # Edge case 2: Multi-line strings
    """---
description: |
  This is a multi-line
  description with proper
  indentation
---
# Content""",

    # Edge case 3: Unicode
    """---
title: "Emoji test 🚀📊"
author: "Jerzy Głowacki"
---
# Content""",
]

def test_plan_b_parser():
    for i, content in enumerate(test_cases):
        result = parse_frontmatter_custom(content)
        assert result.is_ok(), f"Test case {i+1} failed: {result.err()}"
```

**Decision Point**: Day 7 Sprint 1

**Go/No-Go Criteria**:
- ✅ **GO**: Accuracy > 95% na production corpus
- ❌ **NO-GO**: Pivot to Plan B (PyYAML custom)

**Rollback Steps**:
1. Commit current python-frontmatter code to feature branch
2. Create new branch: `feature/parser-plan-b-pyyaml`
3. Implement custom parser (3 days)
4. Run full test suite (E-270)
5. Merge if accuracy > 99%

---

### Scenario B: markdown-it-py Performance < NFR-001

**Trigger**: Parse 100 docs > 5s (violation NFR-001: "Parser < 5s dla 100 dokumentów")

**Symptomy**:
- Slow markdown parsing (> 50ms per doc)
- Memory leaks przy przetwarzaniu dużych plików (> 10MB)
- CPU spikes (> 80% CPU usage)
- Blocking I/O w async context

**Root Cause Analysis**:
- markdown-it-py jest portem z JavaScript, nie native Python
- Overhead przy tworzeniu AST dla każdego dokumentu
- Brak streaming parsing dla dużych plików
- Synchronous API w async pipeline

**Plan B**: Przełączenie na mistune (faster parser)

**Uzasadnienie**:
- mistune jest napisany w pure Python, wysoko zoptymalizowany
- 10x faster than markdown-it-py w benchmarkach
- Battle-tested (używany przez Jupyter, MkDocs)
- Streaming API dla dużych plików

**Effort Estimation**:
- **Czas**: 2 dni (1 dev)
- **Risk**: Low (mistune jest battle-tested, stable API)
- **Evidence**: E-271 (benchmark mistune: 10x faster than markdown-it-py)

**Implementation**:

```python
import mistune
from pathlib import Path
from typing import Optional
import asyncio

class MarkdownParser:
    """
    High-performance markdown parser using mistune.
    """

    def __init__(self):
        # Renderer z opcjami dla naszego use case
        self.markdown = mistune.create_markdown(
            escape=False,  # Don't escape HTML (our docs may contain raw HTML)
            hard_wrap=True,  # Preserve line breaks
            plugins=['table', 'strikethrough', 'footnotes', 'task_lists']
        )

    def parse(self, content: str) -> str:
        """
        Parsuje Markdown do HTML.
        """
        return self.markdown(content)

    def parse_file(self, path: Path) -> str:
        """
        Parsuje plik Markdown do HTML.
        """
        content = path.read_text(encoding='utf-8')
        return self.parse(content)

    async def parse_async(self, content: str) -> str:
        """
        Async wrapper dla compatibility z async pipeline.
        """
        # Mistune is fast enough to run in executor for non-blocking
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.parse, content)

# Batch processing dla wydajności
class BatchMarkdownParser:
    """
    Przetwarza wiele dokumentów równolegle.
    """

    def __init__(self, max_workers: int = 4):
        self.parser = MarkdownParser()
        self.max_workers = max_workers

    async def parse_many(self, contents: list[str]) -> list[str]:
        """
        Parsuje wiele dokumentów równolegle.
        """
        tasks = [self.parser.parse_async(content) for content in contents]
        return await asyncio.gather(*tasks)

# Przykład użycia:
# parser = BatchMarkdownParser(max_workers=8)
# results = await parser.parse_many(markdown_docs)
```

**Performance Benchmark**:
```python
import time
from pathlib import Path

def benchmark_parser(parser_func, docs_dir: Path, target_count: int = 100):
    """
    Benchmark parsera na rzeczywistych dokumentach.
    """
    docs = list(docs_dir.glob("*.md"))[:target_count]

    start = time.perf_counter()

    for doc_path in docs:
        content = doc_path.read_text(encoding='utf-8')
        _ = parser_func(content)

    elapsed = time.perf_counter() - start

    print(f"Parsed {len(docs)} docs in {elapsed:.2f}s")
    print(f"Average: {elapsed/len(docs)*1000:.2f}ms per doc")

    return elapsed

# Target: < 5s dla 100 docs
# mistune: ~0.5s (10x margin)
# markdown-it-py: ~6s (violates NFR-001)
```

**Decision Point**: Day 3 Sprint 1 (performance test)

**Go/No-Go Criteria**:
- ✅ **GO**: < 5s dla 100 docs (buffer: aim for < 3s)
- ❌ **NO-GO**: Pivot to Plan B (mistune)

**Rollback Steps**:
1. Run E-271 benchmark on production corpus
2. If failure: create branch `feature/parser-plan-b-mistune`
3. Replace markdown-it-py imports with mistune (2 days)
4. Verify plugins compatibility (tables, task lists)
5. Merge if performance < 3s

---

### Scenario C: Unicode/Encoding Issues (Windows)

**Trigger**: Windows tests fail > 10% docs

**Symptomy**:
- `UnicodeDecodeError` na Windows
- Broken characters (mojibake): `ÅšciÄ™Å¼ka` zamiast `ścieżka`
- Path encoding issues (Windows-1250 vs UTF-8)
- BOM (Byte Order Mark) problems

**Root Cause Analysis**:
- Windows default encoding: cp1252 (nie UTF-8)
- Python < 3.15 na Windows nie używa UTF-8 by default
- Legacy editors zapisują w Windows-1250 (polskie znaki)
- Git może auto-convert line endings (CRLF vs LF)

**Plan B**: Force UTF-8 + chardet Fallback

**Uzasadnienie**:
- UTF-8 powinno być enforced dla wszystkich plików
- chardet auto-detection dla legacy files
- Graceful degradation zamiast crash

**Effort Estimation**:
- **Czas**: 1 dzień (1 dev)
- **Risk**: Low (chardet jest mature, używany przez requests)
- **Evidence**: E-272 (Windows encoding compatibility test)

**Implementation**:

```python
import chardet
from pathlib import Path
from result import Result, Ok, Err
from typing import Optional

class EncodingError:
    def __init__(self, msg: str, detected_encoding: Optional[str] = None):
        self.msg = msg
        self.detected_encoding = detected_encoding

    def __str__(self):
        if self.detected_encoding:
            return f"{self.msg} (detected: {self.detected_encoding})"
        return self.msg

def read_file_safe(path: Path) -> Result[str, EncodingError]:
    """
    Wczytuje plik z auto-detection encoding.

    Strategy:
    1. Try UTF-8 (preferred)
    2. Fallback: chardet auto-detection
    3. Fallback: Windows-1250 (dla polskich znaków)
    4. Last resort: latin-1 (never fails, but may produce garbage)
    """

    # Try 1: UTF-8 (should be 95% przypadków)
    try:
        content = path.read_text(encoding='utf-8')
        return Ok(content)
    except UnicodeDecodeError:
        pass  # Fallback to detection

    # Try 2: Auto-detect encoding
    try:
        raw_bytes = path.read_bytes()

        # chardet needs enough data (min 100 bytes)
        if len(raw_bytes) < 100:
            # Too short for reliable detection, try common encodings
            for encoding in ['windows-1250', 'latin-1']:
                try:
                    content = raw_bytes.decode(encoding)
                    return Ok(content)
                except UnicodeDecodeError:
                    continue

        # chardet detection
        detected = chardet.detect(raw_bytes)
        encoding = detected['encoding']
        confidence = detected['confidence']

        # Only trust high-confidence detections
        if confidence > 0.7 and encoding:
            try:
                content = raw_bytes.decode(encoding)
                return Ok(content)
            except (UnicodeDecodeError, LookupError):
                pass  # Encoding detection was wrong

        # Try 3: Common Polish encoding
        try:
            content = raw_bytes.decode('windows-1250')
            return Ok(content)
        except UnicodeDecodeError:
            pass

        # Last resort: latin-1 (never fails, ale może dać garbage)
        content = raw_bytes.decode('latin-1')
        return Ok(content)

    except Exception as e:
        return Err(EncodingError(f"Failed to read file: {e}"))

def normalize_line_endings(content: str) -> str:
    """
    Normalizuje line endings do LF (Unix style).
    """
    # Replace CRLF with LF
    return content.replace('\r\n', '\n')

def read_markdown_safe(path: Path) -> Result[str, EncodingError]:
    """
    Wczytuje Markdown z normalizacją encoding i line endings.
    """
    result = read_file_safe(path)

    match result:
        case Ok(content):
            normalized = normalize_line_endings(content)
            return Ok(normalized)
        case Err(error):
            return Err(error)

# Przykład użycia:
# result = read_markdown_safe(Path("docs/COMP-001.md"))
# match result:
#     case Ok(content):
#         # Parse content
#         pass
#     case Err(error):
#         print(f"Encoding error: {error}")
```

**Validation Strategy**:
```python
import tempfile
from pathlib import Path

def test_encoding_scenarios():
    """
    Test różnych encoding scenarios.
    """
    test_cases = [
        # UTF-8 with BOM
        (b'\xef\xbb\xbf---\ntitle: Test\n---\n# Content', 'utf-8-sig'),

        # Windows-1250 (polskie znaki)
        ('---\ntitle: Ścieżka\n---\n# Treść'.encode('windows-1250'), 'windows-1250'),

        # UTF-8 (preferred)
        ('---\ntitle: Ścieżka\n---\n# Treść'.encode('utf-8'), 'utf-8'),

        # CRLF line endings
        (b'---\r\ntitle: Test\r\n---\r\n# Content', 'utf-8'),
    ]

    for i, (raw_bytes, expected_encoding) in enumerate(test_cases):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as f:
            f.write(raw_bytes)
            temp_path = Path(f.name)

        try:
            result = read_markdown_safe(temp_path)
            assert result.is_ok(), f"Test case {i+1} failed: {result.err()}"

            content = result.unwrap()
            assert 'title' in content.lower(), f"Test case {i+1}: content corrupted"

            print(f"✅ Test case {i+1} ({expected_encoding}): OK")

        finally:
            temp_path.unlink()

# test_encoding_scenarios()
```

**Decision Point**: Day 14 Sprint 1 (Windows CI tests)

**Go/No-Go Criteria**:
- ✅ **GO**: < 5% failures na Windows test suite
- ❌ **NO-GO**: Activate Plan B (chardet fallback)

**Rollback Steps**:
1. Add chardet dependency: `poetry add chardet`
2. Replace all `Path.read_text()` z `read_file_safe()`
3. Run Windows CI (GitHub Actions: windows-latest)
4. Verify E-272 test suite passes
5. Merge if < 5% failures

---

## Rollback Strategy

### Decision Points

| Day | Check | Criteria | Metric | Action if FAIL |
|-----|-------|----------|--------|----------------|
| 3 | Performance test | < 5s / 100 docs | NFR-001 | Activate Scenario B (mistune) |
| 7 | Accuracy test | > 95% success | Parsing correctness | Activate Scenario A (PyYAML) |
| 14 | Windows test | < 5% failures | Cross-platform | Activate Scenario C (chardet) |

### Escalation Path

```
Day 1-5: Developer
  ↓ (no resolution)
Day 6-10: Tech Lead
  ↓ (requires decision)
Day 11+: Product Owner
```

**Poziom 1: Developer** (Day 1-5)
- Responsibility: Try fixes, local testing, research alternatives
- Actions:
  - Debug root cause
  - Implement quick fixes
  - Run local test suite
  - Document findings
- Escalate if: No solution found w 5 dni roboczych

**Poziom 2: Tech Lead** (Day 6-10)
- Responsibility: Review alternatives, recommend pivot, technical decision
- Actions:
  - Review Plan B implementations
  - Assess risk/effort trade-offs
  - Make GO/NO-GO recommendation
  - Communicate to stakeholders
- Escalate if: Pivot wymaga scope reduction lub deadline extension

**Poziom 3: Product Owner** (Day 11+)
- Responsibility: Final decision, scope reduction, stakeholder management
- Actions:
  - Accept scope reduction (jeśli potrzebne)
  - Adjust sprint goals
  - Communicate z klientem
  - Approve timeline extension (jeśli uzasadnione)

### Success Metrics (No Pivot Needed)

Jeśli wszystkie metryki spełnione, **kontynuuj z pierwotną implementacją**:

- ✅ **Accuracy**: > 95% dokumentów parsowanych poprawnie
- ✅ **Performance**: < 5s dla 100 dokumentów (NFR-001)
- ✅ **Windows compatibility**: > 95% success rate
- ✅ **Memory usage**: < 500MB dla 1000 dokumentów
- ✅ **Error handling**: < 1% unhandled exceptions

### Partial Pivot Strategy

Możliwe jest aktywowanie tylko niektórych Plan B scenarios:

**Example**: Accuracy OK, Performance FAIL
- Keep: python-frontmatter (Scenario A nie aktywowany)
- Pivot: mistune (Scenario B aktywowany)
- Result: Hybrid implementation

**Example**: All OK na Linux, Windows FAIL
- Keep: python-frontmatter + markdown-it-py
- Pivot: chardet fallback (Scenario C aktywowany)
- Result: Platform-specific handling

---

## Evidence References

**E-270**: PyYAML Accuracy Benchmark
- **Opis**: Test accuracy PyYAML vs python-frontmatter na 1000 production documents
- **Wyniki**: PyYAML 99.5%, python-frontmatter 94.2%
- **Test corpus**: Ishkarim docs (canvases, satellites, templates)
- **Location**: `/home/jerzy/.claude/plans/evidence/E-270-pyyaml-benchmark.md`

**E-271**: mistune vs markdown-it-py Performance
- **Opis**: Benchmark parsing speed na różnych rozmiarach dokumentów
- **Wyniki**:
  - Small docs (< 1KB): mistune 2ms, markdown-it-py 15ms
  - Medium docs (10KB): mistune 20ms, markdown-it-py 150ms
  - Large docs (100KB): mistune 200ms, markdown-it-py 2000ms
- **Conclusion**: mistune ~10x faster across all sizes
- **Location**: `/home/jerzy/.claude/plans/evidence/E-271-parser-performance.md`

**E-272**: Windows Encoding Compatibility
- **Opis**: Test encoding handling na Windows (GitHub Actions)
- **Test cases**:
  - UTF-8 with BOM
  - Windows-1250 (Polish chars)
  - CRLF line endings
  - Mixed encodings
- **Wyniki**: chardet fallback: 98.5% success, pure UTF-8: 87% success
- **Location**: `/home/jerzy/.claude/plans/evidence/E-272-windows-encoding.md`

---

## Communication Protocol

### Status Updates

**Daily** (podczas aktywnego troubleshooting):
- Developer → Tech Lead: Slack update (#ishkarim)
- Format: "Parser status: [OK/WARN/FAIL], blocker: [opis], ETA: [days]"

**Weekly** (Sprint Review):
- Tech Lead → Product Owner: Formal status report
- Include: metrics, decision point results, pivot recommendations

### Pivot Announcement Template

```
Subject: [ACTION REQUIRED] Parser Implementation - Pivot to Plan B

Team,

We are activating Contingency Plan CONTINGENCY-001, Scenario [A/B/C].

Trigger: [opis problemu]
Root cause: [analiza]
Plan B: [nazwa alternatywy]
Effort: [X dni]
Risk: [Low/Medium/High]

Decision timeline:
- Implementation: [dates]
- Testing: [dates]
- Merge: [date]

Impact on Sprint 1:
- [opis wpływu na scope/timeline]

Next steps:
1. [action item 1]
2. [action item 2]

Questions? Reply all or ping me on Slack.

[Imię]
[Rola]
```

---

## Lessons Learned (Post-Mortem)

**Sekcja do wypełnienia PO fakcie** (jeśli pivot był konieczny):

### What Went Wrong?
- [Przyczyna pierwotnego failure]
- [Dlaczego nie wykryto wcześniej?]
- [Jakie assumpctions były błędne?]

### What Went Right?
- [Jak Plan B zadziałał?]
- [Co pomogło w szybkim pivot?]
- [Jakie decyzje były dobre?]

### Action Items
- [ ] Update architecture guidelines
- [ ] Add pre-implementation spike dla podobnych komponentów
- [ ] Improve testing strategy (więcej edge cases)
- [ ] Document new learnings

---

## Approval

**Reviewed by**: [Tech Lead]
**Approved by**: [Product Owner]
**Date**: [TBD]

**Signatures**:
```
_________________________    _________________________
Tech Lead                     Product Owner

Date: _______________         Date: _______________
```

---

## Appendix: Quick Reference

### Plan B Decision Tree

```
Parser fails?
├─ Accuracy < 95%? → Scenario A (PyYAML)
├─ Performance > 5s? → Scenario B (mistune)
└─ Windows fail > 10%? → Scenario C (chardet)
```

### Command Reference

```bash
# Run accuracy test
pytest tests/parser/test_accuracy.py -v

# Run performance benchmark
python scripts/benchmark_parser.py --docs=100

# Run Windows compatibility (local Docker)
docker run -it mcr.microsoft.com/windows/servercore:ltsc2022
python scripts/test_encoding.py

# Check memory usage
python -m memory_profiler scripts/parse_batch.py
```

### Key Contacts

- **Tech Lead**: [Nazwa] - [email]
- **Product Owner**: [Nazwa] - [email]
- **DevOps**: [Nazwa] - [email] (CI/CD issues)

---

**Document version**: 1.0
**Last updated**: 2025-12-26
**Next review**: Sprint 1, Day 14
