---
id: ADR-003
title: "ADR-003: Validation Strategy"
type: adr
status: approved
decision_date: 2025-12-20
parent: TDD-001-V2

evidence_ids:
  - "E-145"  # Pydantic benchmark (42ms dla 1000 docs)
  - "E-164"  # OPA evaluation (overkill dla MVP)

alternatives:
  - id: "OPT-CERBERUS"
    title: "Cerberus (Python validator)"
    status: rejected
    reason: "Slower, less type-safe, weaker error messages"

  - id: "OPT-OPA-REGO"
    title: "OPA + Rego (policy-as-code)"
    status: deferred
    reason: "Overkill dla MVP (complex policy language). Defer to V1.5 if complex policies needed."

  - id: "OPT-PYDANTIC"
    title: "Pydantic 2.x"
    status: selected
    reason: "Type-safe (Python hints), fast (Rust core), excellent errors, JSON Schema export"
---

# ADR-003: Validation Strategy

**Decision**: Use **Pydantic 2.5+** for schema validation

**Status**: ✅ APPROVED

---

## Context

**Problem**: Validate documents against schemas (frontmatter fields, constraints).

**Requirements**:
1. Type-safe (Python type hints)
2. Fast (< 50ms per document - NFR-001)
3. Good error messages (user-friendly)
4. Extensible (custom validation logic)

---

## Decision

### Pydantic 2.5+ ✅

**Why**:
- ✅ **Type-safe**: Python type hints → runtime validation
- ✅ **Fast**: Rust core w v2 (17× faster than v1) - 42μs/doc [E-145]
- ✅ **Error messages**: Precise, actionable ("field 'id' is required")
- ✅ **JSON Schema export**: Future OPA integration if needed
- ✅ **Mature**: v2 stable, production-ready

**Usage**:
```python
from pydantic import BaseModel, Field

class DocumentFrontmatter(BaseModel):
    id: str = Field(..., pattern=r"^[A-Z]+-\d+")
    title: str = Field(..., min_length=1)
    type: Literal["prd", "tdd", "adr"]
    status: Literal["draft", "review", "approved"]

# Validate
try:
    fm = DocumentFrontmatter(**yaml_data)
except ValidationError as e:
    print(e.errors())  # Detailed errors
```

**Evidence**: [E-145] Benchmark: 1000 docs validated → 42ms (42μs/doc avg)

---

## Alternatives

### Cerberus ❌
**Cons**: Slower, less type-safe, weaker error messages
**Rejected**: Pydantic superior in all criteria

### OPA/Rego ❌ (Deferred)
**Pros**: Policy-as-code (complex rules engine)
**Cons**: **Overkill dla MVP** (learning curve, YAML → Rego translation complex)
**Decision**: Defer to V1.5 if complex policies emerge
**Evidence**: [E-164] Evaluation showed 80% rules achievable w Pydantic validators

---

## Consequences

**Positive**:
- ✅ Type safety (catch errors at runtime + IDE autocomplete)
- ✅ Performance excellent (< 50ms target met)
- ✅ Maintainable (Python-native, standard library integration)

**Negative**:
- ⚠️ Complex policies need custom validators (but acceptable dla MVP scope)

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
