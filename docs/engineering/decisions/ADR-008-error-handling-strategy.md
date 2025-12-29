---
id: ADR-008
title: "ADR-008: Error Handling Strategy"
type: adr
domain: architecture
status: accepted
created: 2025-12-28
decision_date: 2025-12-28
author: ["Tech Lead"]
parent: TDD-001-V2

dependencies:
  - id: "ADR-003"
    type: related
    reason: "Validator error handling must be consistent with overall strategy"

  - id: "ADR-007"
    type: related
    reason: "GUI pattern influences error propagation to UI"

impacts:
  - id: "COMP-001-parser"
    type: informs
    reason: "Parser must use unified error handling"
    cascade: true

  - id: "COMP-002-validator"
    type: informs
    reason: "Validator must use unified error handling"
    cascade: true

  - id: "COMP-003-graph"
    type: informs
    reason: "Graph builder must use unified error handling"
    cascade: true

  - id: "COMP-004-gap-engine"
    type: informs
    reason: "Gap engine must use unified error handling"
    cascade: true

  - id: "COMP-005-gui"
    type: informs
    reason: "GUI must display errors according to strategy"
    cascade: true

  - id: "COMP-006-storage"
    type: informs
    reason: "Storage must use unified error handling"
    cascade: true

evidence_ids:
  - "E-008"  # Error handling patterns survey (10 similar Python tools)

context_snapshot:
  date: "2025-12-28"
  error_types:
    - "File I/O errors (missing files, permission denied)"
    - "Parse errors (malformed YAML, invalid markdown)"
    - "Validation errors (schema violations)"
    - "Graph errors (cycles, broken dependencies)"
    - "User errors (invalid input in GUI)"
  questions:
    - "Exceptions vs Result types (Rust-style)?"
    - "How to distinguish recoverable vs fatal errors?"
    - "How to display errors to user (GUI dialogs vs status bar)?"

alternatives:
  - id: "OPT-RESULT-TYPES"
    title: "Result Types (Rust/Golang style)"
    status: rejected
    reason: "Too verbose for Python, against Pythonic idioms"

  - id: "OPT-ERROR-CODES"
    title: "Error Codes (C-style)"
    status: rejected
    reason: "Harder to propagate, easy to ignore"

  - id: "OPT-GLOBAL-HANDLER"
    title: "Global Error Handler"
    status: rejected
    reason: "Too coarse, loses context"

  - id: "OPT-PYTHON-EXCEPTIONS"
    title: "Python Exceptions with Custom Hierarchy"
    status: selected
    reason: "Pythonic, provides context, easy to distinguish error types, supports stack traces"
---

# ADR-008: Error Handling Strategy

**Decision**: Use **Python exceptions with custom exception hierarchy**

**Status**: ACCEPTED (2025-12-28)

---

## Context (T₀)

**Problem**: System musi obsługiwać różne błędy w 6 głównych komponentach.

**Error Types**:
1. **File I/O errors**: Missing files, permission denied
2. **Parse errors**: Malformed YAML, invalid markdown
3. **Validation errors**: Schema violations, missing required fields
4. **Graph errors**: Circular dependencies, broken links
5. **User errors**: Invalid input w GUI
6. **System errors**: Database corruption, network failures

**Questions**:
- Exceptions vs Result types (Rust-style)?
- Jak rozróżnić recoverable vs fatal errors?
- Jak pokazywać błędy użytkownikowi (GUI dialogs vs status bar)?

**Requirements**:
- Consistent error handling across all components
- Clear distinction between recoverable and fatal errors
- User-friendly error messages in GUI
- Full stack traces for debugging
- Minimal performance overhead

---

## Decision

### Python Exceptions with Custom Hierarchy

Use Python exceptions z **custom exception hierarchy**:

```python
class IshkarimError(Exception):
    """Base exception - wszystkie custom exceptions dziedziczą"""
    pass

class ParseError(IshkarimError):
    """Recoverable - show user, continue processing other docs"""
    pass

class ValidationError(IshkarimError):
    """Recoverable - show in gap report"""
    pass

class FatalError(IshkarimError):
    """Unrecoverable - show error dialog, exit gracefully"""
    pass
```

**Error Handling Rules**:
1. **Recoverable errors**: Catch, log WARNING, show user, continue
2. **Fatal errors**: Catch, log ERROR, show dialog, save state, exit
3. **Never silence exceptions** (no bare `except: pass`)
4. **Always provide context** (include filename, line number w message)

**GUI Error Display**:
- Recoverable → Status bar notification (orange)
- Fatal → Modal dialog z stack trace (red)

**Why This Approach**:
- Pythonic - zgodne z Python conventions
- Stack traces out-of-the-box dla debugging
- Większość bibliotek używa exceptions
- try/except dobrze znany pattern dla team
- Integracja z logging (exception chaining)
- Easy to extend hierarchy dla nowych error types

**Evidence**: [E-008] Error handling patterns survey w 10 podobnych Python tools pokazuje że 80% używa custom exception hierarchies

---

## Alternatives Considered

### Result Types (Rust/Golang style)

**Pros**: Type-safe, forces explicit error handling, no exception overhead

**Cons**:
- Too verbose dla Python
- Against Pythonic idioms
- Trudniejsza integracja z bibliotekami używającymi exceptions
- Learning curve dla team (functional programming concepts)

**Rejected**: Not Pythonic, zbyt wiele boilerplate code

---

### Error Codes (C-style)

**Pros**: Lightweight, simple to understand

**Cons**:
- Harder to propagate through call stack
- Easy to ignore (no forced handling)
- No stack traces
- No context information

**Rejected**: Loses valuable debugging information

---

### Global Error Handler

**Pros**: Centralized error handling logic

**Cons**:
- Too coarse - loses context about where error occurred
- Difficult to distinguish error types
- Hard to implement different handling dla różnych komponentów

**Rejected**: Insufficient granularity dla complex system

---

## Consequences

### Positive

- Consistent error handling across components
- Easy to distinguish recoverable vs fatal errors
- Better user experience (informative errors)
- Full stack traces dla debugging
- Natural integration z Python ecosystem
- Clear error hierarchy - easy to extend

### Negative

- Slight overhead (exception stack traces)
- Możliwość nadużycia exceptions dla flow control (wymaga code review guidelines)
- Wymaga dyscypliny w tworzeniu meaningful error messages

### Neutral

- Team już zna try/except pattern (no learning curve)
- Compatible z większością Python libraries

---

## Implementation Guidelines

### 1. Exception Hierarchy

```python
# Base exception
class IshkarimError(Exception):
    """Base for all Ishkarim custom exceptions"""
    def __init__(self, message: str, context: dict = None):
        super().__init__(message)
        self.context = context or {}

# Component-specific exceptions
class ParserError(IshkarimError):
    """Errors during document parsing"""
    pass

class ValidatorError(IshkarimError):
    """Errors during validation"""
    pass

class GraphError(IshkarimError):
    """Errors during graph operations"""
    pass

class StorageError(IshkarimError):
    """Errors during storage operations"""
    pass

# Severity-based exceptions
class RecoverableError(IshkarimError):
    """Errors that allow continued processing"""
    pass

class FatalError(IshkarimError):
    """Errors that require graceful shutdown"""
    pass
```

### 2. Error Handling Pattern

```python
# In components
def parse_document(path: Path) -> Document:
    try:
        content = path.read_text()
    except FileNotFoundError:
        raise ParserError(
            f"Document not found: {path}",
            context={"path": str(path), "operation": "read"}
        )
    except PermissionError:
        raise FatalError(
            f"Permission denied: {path}",
            context={"path": str(path), "operation": "read"}
        )

# In GUI
try:
    doc = parser.parse_document(path)
    self.display(doc)
except RecoverableError as e:
    self.show_status_bar(str(e), level="warning")
    logger.warning(f"Recoverable error: {e}", extra=e.context)
except FatalError as e:
    self.show_error_dialog(str(e), details=traceback.format_exc())
    logger.error(f"Fatal error: {e}", extra=e.context)
    self.save_state()
    sys.exit(1)
```

### 3. Error Message Guidelines

- Include what went wrong
- Include where it happened (filename, line number)
- Include what was expected
- Suggest how to fix (if applicable)

Example: "Failed to parse document '/path/to/doc.md': Invalid YAML at line 5 (expected key-value pair, got list). Please check YAML syntax."

---

## Evidence

**[E-008]**: Error handling patterns survey
- Surveyed 10 similar Python documentation tools
- 8/10 używa custom exception hierarchies
- 2/10 używa Result types (both Rust developers)
- 0/10 używa error codes
- Best practices: meaningful messages, context dict, exception chaining

---

## Related Decisions

- **ADR-003** (Validation): Pydantic ValidationError wrapped w IshkarimError.ValidatorError
- **ADR-007** (GUI Pattern): Qt signals propagują exceptions do UI layer
- **ADR-009** (Logging): Exception context logged z structured logging

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Created**: 2025-12-28
