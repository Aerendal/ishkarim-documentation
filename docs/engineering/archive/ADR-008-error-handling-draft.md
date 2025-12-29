---
id: ADR-008
title: "ADR-008: Error Handling Strategy"
type: adr
domain: architecture
status: draft
created: 2025-12-26
updated: 2025-12-26
owner: Tech Lead
decision_date: null
review_date: null

dependencies:
  - id: "ADR-003"
    type: related
    reason: "Validator error handling musi być spójny z ogólną strategią"

  - id: "ADR-007"
    type: related
    reason: "GUI pattern wpływa na propagację błędów do UI"

impacts:
  - id: "COMP-001-parser"
    type: informs
    reason: "Parser musi używać unified error handling"
    cascade: true

  - id: "COMP-002-validator"
    type: informs
    reason: "Validator musi używać unified error handling"
    cascade: true

  - id: "COMP-003-graph"
    type: informs
    reason: "Graph builder musi używać unified error handling"
    cascade: true

  - id: "COMP-004-gap-engine"
    type: informs
    reason: "Gap engine musi używać unified error handling"
    cascade: true

  - id: "COMP-005-gui"
    type: informs
    reason: "GUI musi wyświetlać błędy zgodnie ze strategią"
    cascade: true

  - id: "COMP-006-storage"
    type: informs
    reason: "Storage musi używać unified error handling"
    cascade: true

evidence_ids:
  - "E-250"  # Python exceptions best practices research
  - "E-251"  # Result/Either pattern benchmark
  - "E-252"  # Error handling survey (10 podobnych projektów)

related:
  - "ADR-003"
  - "ADR-007"
---

# ADR-008: Error Handling Strategy

**Status**: Draft
**Decyzja**: [TBD - do wyboru po review]
**Data Decyzji**: [TBD]
**Owner**: Tech Lead
**Reviewers**: [Lista do uzupełnienia]

---

## Context (T₀ - Stan w Momencie Decyzji)

### Problem Statement

System Ishkarim ma 6 głównych komponentów (Parser, Validator, Graph, Gap Engine, GUI, Storage), każdy z różnymi typami błędów:

**Parser (COMP-001)**:
- Expected errors: malformed YAML, invalid markdown structure
- Unexpected errors: file not found, encoding issues, memory overflow

**Validator (COMP-002)**:
- Expected errors: schema validation failures, missing required fields
- Unexpected errors: Pydantic internal errors, recursion limits

**Graph Builder (COMP-003)**:
- Expected errors: circular dependencies detected, broken links
- Unexpected errors: NetworkX exceptions, graph too large

**Gap Engine (COMP-004)**:
- Expected errors: gap detected (E110-E160)
- Unexpected errors: gap detector logic errors

**GUI (COMP-005)**:
- Expected errors: user input validation failures
- Unexpected errors: Qt crashes, rendering issues

**Storage (COMP-006)**:
- Expected errors: SQLite constraint violations, file write permissions
- Unexpected errors: database corruption, disk full

### Current State (T₀)

**Brak unified error handling strategy**:
- Każdy komponent może używać własnego podejścia
- Brak spójności w propagacji błędów między warstwami
- Trudności w debugging i observability
- Niejasne kiedy używać exceptions vs return codes vs Result types

### Requirements

**FR-ERROR-001**: System musi mieć spójną strategię error handling we wszystkich komponentach
**FR-ERROR-002**: Błędy muszą być propagowane między warstwami w przewidywalny sposób
**FR-ERROR-003**: GUI musi móc wyświetlać user-friendly error messages
**NFR-ERROR-001**: Error handling nie może degradować performance (< 5% overhead)
**NFR-ERROR-002**: Stack traces muszą być dostępne dla debugging

### Constraints

- Python 3.11+ (native exception handling)
- PySide6 GUI (Qt error handling patterns)
- Pydantic validator (ValidationError)
- NetworkX (własne exception types)
- SQLite (database exceptions)

---

## Decision Graph

### Option A: Exceptions Everywhere (Python Standard)

**Approach**: Używaj Python exceptions dla wszystkich błędów (expected i unexpected).

**Pros**:
✅ Pythonic - zgodne z Python conventions
✅ Stack traces out-of-the-box
✅ Większość bibliotek używa exceptions
✅ try/except dobrze znany pattern
✅ Integracja z logging (exception chaining)

**Cons**:
❌ Exceptions są "expensive" (performance overhead ~10-50μs per raise)
❌ Trudne do type-checkowania (mypy nie wie które funkcje raise co)
❌ Expected errors (validation failures) traktowane jak unexpected
❌ Scattered error handling (try/except wszędzie)
❌ Trudne do testowania (trzeba mockować exceptions)

**Example Implementation**:
```python
# Parser
def parse_document(path: Path) -> Document:
    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    try:
        content = path.read_text()
        frontmatter = yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise ParseError(f"Invalid YAML: {e}") from e

    if 'id' not in frontmatter:
        raise ValidationError("Missing required field: id")

    return Document(...)

# GUI
try:
    doc = parser.parse_document(path)
    self.display(doc)
except FileNotFoundError as e:
    QMessageBox.critical(self, "Error", f"File not found: {e}")
except ParseError as e:
    QMessageBox.warning(self, "Parse Error", str(e))
except ValidationError as e:
    QMessageBox.warning(self, "Validation Error", str(e))
```

**Evidence**: [E-250] Survey of 50 Python projects: 80% używa pure exceptions

**Performance Impact**: ~10-50μs per exception raise (NFR-ERROR-001: < 5% overhead może być violated dla high-frequency operations)

---

### Option B: Result/Either Monad Pattern

**Approach**: Używaj Result[T, E] type dla expected errors, exceptions tylko dla unexpected.

**Pros**:
✅ Type-safe - mypy wie co może fail
✅ Forces explicit error handling (no silent failures)
✅ Performance - no exception overhead dla expected errors
✅ Composable - można chain operations z flatmap/bind
✅ Clear separation: expected vs unexpected errors

**Cons**:
❌ Not Pythonic - rzadko używane w Python ecosystem
❌ Wymaga custom Result type lub library (e.g., returns, result)
❌ Verbose - każda funkcja returns Result, więcej boilerplate
❌ Trudniejsza integracja z bibliotekami używającymi exceptions
❌ Learning curve dla team (functional programming concepts)

**Example Implementation**:
```python
from typing import Union
from dataclasses import dataclass

@dataclass
class Ok[T]:
    value: T

@dataclass
class Err[E]:
    error: E

Result = Union[Ok[T], Err[E]]

# Parser
def parse_document(path: Path) -> Result[Document, ParseError]:
    if not path.exists():
        return Err(ParseError.FileNotFound(path))

    try:
        content = path.read_text()
    except IOError as e:
        raise UnexpectedError("IO Error") from e  # Unexpected - exception

    frontmatter_result = parse_yaml(content)
    if isinstance(frontmatter_result, Err):
        return frontmatter_result  # Propagate error

    frontmatter = frontmatter_result.value

    if 'id' not in frontmatter:
        return Err(ParseError.MissingField('id'))

    return Ok(Document(...))

# GUI
result = parser.parse_document(path)
match result:
    case Ok(doc):
        self.display(doc)
    case Err(ParseError.FileNotFound(path)):
        QMessageBox.critical(self, "Error", f"File not found: {path}")
    case Err(ParseError.MissingField(field)):
        QMessageBox.warning(self, "Validation Error", f"Missing: {field}")
```

**Evidence**: [E-251] Benchmark: Result pattern 10x faster than exceptions dla expected errors (5μs vs 50μs)

**Performance Impact**: < 1% overhead (NFR-ERROR-001: PASS ✅)

---

### Option C: Hybrid Approach (RECOMMENDED)

**Approach**: Result type dla **expected errors**, exceptions dla **unexpected errors**.

**Decision Rules**:
1. **Expected errors** (user input, validation, business logic) → Result type
2. **Unexpected errors** (bugs, I/O failures, system errors) → Exceptions
3. **Library errors** → Wrap w Result jeśli expected, re-raise jeśli unexpected

**Pros**:
✅ Best of both worlds - type safety dla expected, stack traces dla unexpected
✅ Performance - Result dla hot paths, exceptions dla rare cases
✅ Clear semantics - Result = recoverable, Exception = irrecoverable
✅ Pragmatic - nie wymaga całkowitego przepisania Python patterns
✅ Gradual adoption - można zacząć od critical paths

**Cons**:
⚠️ Wymaga jasnych guidelines (co jest expected vs unexpected)
⚠️ Mixing patterns - może być confusing początkowo
⚠️ Partial learning curve - team musi znać oba patterns

**Example Implementation**:
```python
# Parser
def parse_document(path: Path) -> Result[Document, ParseError]:
    # Expected error: file not found (user może podać zły path)
    if not path.exists():
        return Err(ParseError.FileNotFound(path))

    # Unexpected error: IO failure (system issue, nie user error)
    try:
        content = path.read_text()
    except IOError as e:
        raise UnexpectedIOError(f"Failed to read {path}") from e

    # Expected error: malformed YAML (user może mieć typo)
    yaml_result = parse_yaml(content)
    if isinstance(yaml_result, Err):
        return yaml_result

    frontmatter = yaml_result.value

    # Expected error: validation failure (user może zapomnieć pola)
    if 'id' not in frontmatter:
        return Err(ParseError.MissingField('id'))

    return Ok(Document(...))

# GUI
try:
    result = parser.parse_document(path)
    match result:
        case Ok(doc):
            self.display(doc)
        case Err(ParseError.FileNotFound(path)):
            QMessageBox.critical(self, "Error", f"File not found: {path}")
        case Err(ParseError.MissingField(field)):
            QMessageBox.warning(self, "Validation", f"Missing: {field}")
except UnexpectedIOError as e:
    logger.exception("Unexpected IO error")
    QMessageBox.critical(self, "System Error", "Please contact support")
```

**Evidence**: [E-252] Survey: 3/10 podobnych projektów używa hybrid (Django, FastAPI patterns)

**Performance Impact**: ~2% overhead (NFR-ERROR-001: PASS ✅)

---

## Decision

**Selected**: **Option C - Hybrid Approach** ✅

**Rationale**:
1. **Performance**: Result type dla hot paths (parser, validator) minimalizuje overhead
2. **Type Safety**: Expected errors są explicite w function signatures
3. **Developer Experience**: Exceptions dla unexpected są znane team
4. **Pragmatism**: Nie wymaga totalnego przepisania patterns
5. **Evidence**: [E-252] pokazuje że podobne projekty (Django, FastAPI) używają hybrid patterns z sukcesem

**Decision Date**: [TBD - po review]
**Approved By**: [TBD]

---

## Consequences

### Positive

✅ **Type Safety**: Expected errors są widoczne w function signatures (mypy sprawdza)
✅ **Performance**: < 2% overhead (vs 10-50% dla pure exceptions)
✅ **Clarity**: Jasny podział expected vs unexpected errors
✅ **Debugging**: Stack traces dla unexpected errors (logging + observability)
✅ **Testing**: Łatwiejsze testowanie expected errors (Result.is_err())

### Negative

⚠️ **Learning Curve**: Team musi znać oba patterns (Result + Exceptions)
⚠️ **Guidelines Required**: Potrzebne jasne dokumenty "co jest expected vs unexpected"
⚠️ **Migration**: Istniejący kod trzeba będzie refactorować (gradual adoption)

### Neutral

➡️ **Library Integration**: Większość bibliotek używa exceptions - trzeba wrappować

---

## Implementation Guidelines

### 1. Expected vs Unexpected - Decision Tree

```
Is this error caused by:
├─ User input? → EXPECTED (Result)
├─ Business logic validation? → EXPECTED (Result)
├─ External data (files, API)? → EXPECTED (Result)
├─ System resource (I/O, memory, network)? → UNEXPECTED (Exception)
├─ Library internal error? → UNEXPECTED (Exception)
└─ Logic bug (assertion failure)? → UNEXPECTED (Exception)
```

### 2. Error Type Hierarchy

```python
# Expected Errors (use Result)
class ParseError(Enum):
    FileNotFound = "file_not_found"
    InvalidYAML = "invalid_yaml"
    MissingField = "missing_field"
    InvalidFormat = "invalid_format"

class ValidationError(Enum):
    SchemaViolation = "schema_violation"
    ConstraintViolation = "constraint_violation"
    TypeMismatch = "type_mismatch"

# Unexpected Errors (use Exception)
class UnexpectedIOError(Exception): pass
class UnexpectedDatabaseError(Exception): pass
class UnexpectedSystemError(Exception): pass
```

### 3. Result Type Implementation

```python
# Use: returns library (pip install returns)
from returns.result import Result, Success, Failure

# Or: custom lightweight Result
# (see COMP-001 implementation for details)
```

### 4. Component-Specific Rules

**Parser (COMP-001)**:
- File not found, YAML errors, validation → Result
- I/O errors, encoding errors → Exception

**Validator (COMP-002)**:
- Schema violations → Result
- Pydantic internal errors → Exception

**Graph (COMP-003)**:
- Circular dependencies, broken links → Result
- NetworkX crashes → Exception

**Gap Engine (COMP-004)**:
- Gap detected (E110-E160) → Result (not an error, expected finding)
- Gap detector logic errors → Exception

**GUI (COMP-005)**:
- User input validation → Result
- Qt crashes, rendering errors → Exception

**Storage (COMP-006)**:
- Constraint violations, duplicate keys → Result
- Database corruption, disk full → Exception

---

## Alternatives Considered (Rejected)

### Option A: Pure Exceptions
**Rejected**: Performance overhead dla hot paths (parser, validator)
**Evidence**: [E-251] Benchmark pokazuje 10x overhead

### Option B: Pure Result
**Rejected**: Not Pythonic, trudna integracja z ecosystem
**Evidence**: [E-250] Survey: tylko 5% Python projektów używa pure Result

---

## Related Decisions

- **ADR-003** (Validator): Pydantic ValidationError musi być wrapped w Result[T, ValidationError]
- **ADR-007** (GUI Pattern): Qt signals propagują Result types do UI layer

---

## Evidence References

- **[E-250]**: Python Exceptions Best Practices - survey 50 projektów
- **[E-251]**: Result vs Exception Benchmark - 10x performance difference
- **[E-252]**: Hybrid Pattern Survey - 3/10 podobnych projektów używa hybrid

---

## Review & Approval

**Definition of Done (DoD) dla tego ADR**:
- [ ] Min. 3 alternatives considered (✅ A, B, C)
- [ ] Evidence notes created (E-250, E-251, E-252)
- [ ] Impact na wszystkie 6 komponentów documented
- [ ] Implementation guidelines clear
- [ ] Reviewed przez 2+ osoby
- [ ] Approved przez Tech Lead
- [ ] Status changed: draft → approved
- [ ] Dodany do DECISION-INDEX

**Reviewers**: [Lista do uzupełnienia]
**Approval Date**: [TBD]

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-003](ADR-003-validation.md), [ADR-007](ADR-007-gui.md)
