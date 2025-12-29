---
id: DOR-COMP-002
title: "Definition of Ready: Validator Component"
type: dor
component: COMP-002-validator
sprint: Sprint 2
date: "2025-12-28"
status: draft
created: 2025-12-28
owner: Tech Lead
gate: READY-FOR-IMPLEMENTATION
components: [COMP-002-validator]
---

# DoR: Validator Component

## Cel
Validator Component musi spełnić kryteria gotowości przed rozpoczęciem implementacji w Sprint 2.

---

## Universal DoR (ze wzoru DOR-MASTER)

- [ ] **Zależności resolved**: Wszystkie upstream docs istnieją i mają poprawny status
- [ ] **Użyto template**: Dokument COMP-002-validator.md utworzony z odpowiedniego szablonu
- [ ] **Frontmatter kompletny**: Wszystkie wymagane pola YAML w dokumentach źródłowych wypełnione
- [ ] **Status poprawny**: COMP-002-validator w statusie "design-complete"
- [ ] **Owner assigned**: Właściciel komponentu wyznaczony i zatwierdzony
- [ ] **Evidence dostępne**: Referencjonowane dokumenty architektoniczne (ADR) istnieją

---

## Component-Specific DoR - Validator Component

### 1. Zależności Techniczne
- [ ] **Pydantic** >= 2.0.0 zainstalowany (główna biblioteka walidacji)
- [ ] **pyyaml** >= 6.0 zainstalowany (schema loading z YAML)
- [ ] **pytest** >= 7.0.0 dostępny dla testów
- [ ] **COMP-001-parser** zakończony i działający
  - [ ] Parser dostarcza Document objects
  - [ ] Document model ma pola: sections, body, frontmatter
- [ ] Virtual environment skonfigurowany i aktywny
- [ ] Python 3.11+ zweryfikowany (obsługa Pydantic v2)

### 2. Dokumenty Projektowe
- [ ] COMP-002-validator.md przejrzany i zrozumiany
- [ ] ADR-003 (Validation Architecture) przejrzany
  - [ ] Pydantic v2 jako validation library zatwierdzone
  - [ ] Schema format (YAML) zrozumiany
- [ ] ADR-008 (Error Handling) - strategia Result type zatwierdzona
- [ ] API-SPEC-001 ValidatorAPI kontrakt zatwierdzony
- [ ] PRD-V2 Requirements przejrzane:
  - [ ] FR-005 (Validate Schema) - zrozumiany
  - [ ] FR-006 (Validate Frontmatter) - zrozumiany
  - [ ] FR-007 (Validate Required Sections) - zrozumiany
  - [ ] FR-008 (Detect Placeholders) - zrozumiany
- [ ] Gap types E110, E120, E170, E180, E190, E200 udokumentowane

### 3. Schema Design
- [ ] Document type schemas zaprojektowane dla minimum 3 typów:
  - [ ] PRD schema (required sections, frontmatter fields)
  - [ ] ADR schema (Alternatives Considered, Decision, etc.)
  - [ ] RFC schema (Open Questions, Stakeholders, etc.)
- [ ] Schema format YAML uzgodniony:
  - [ ] frontmatter.required_fields
  - [ ] frontmatter.constraints (pattern, enum)
  - [ ] required_sections (name, pattern, mandatory, min_items)
  - [ ] gap_detection (E110, E120, E170 configs)
- [ ] Schema location: schemas/{doc_type}.yaml
- [ ] Schema validation rules enumerated (regex patterns, enums, required fields)

### 4. Validation Rules Documentation
- [ ] **E110 detection rules** (Missing Sections):
  - [ ] Regex patterns dla każdego required section
  - [ ] Mandatory vs optional sections logic
  - [ ] Min_items criteria dla list sections (np. 10+ FRs)
- [ ] **E120 detection rules** (Placeholders):
  - [ ] Keyword list: TODO, TBD, PLACEHOLDER, XXX, FIXME, TBA
  - [ ] Ignore logic dla code blocks i quotes (markdown AST)
  - [ ] Section severity classification (critical vs informational)
- [ ] **E170 detection rules** (Missing Evidence):
  - [ ] Min evidence notes per document type
  - [ ] [E-XXX] reference format validation
- [ ] **E180 detection rules** (Storytelling):
  - [ ] Bullet list vs narrative detection logic
  - [ ] Storytelling template per document type
- [ ] **E190/E200 rules** (Alternatives, Post-mortem) - basic logic drafted

### 5. Dane Testowe
- [ ] Minimum 10 przykładowych dokumentów przygotowanych:
  - [ ] 5 poprawnych (wszystkie required sections, no placeholders)
  - [ ] 5 z gaps (missing sections, placeholders, brakujące evidence)
- [ ] Przypadki graniczne zidentyfikowane i udokumentowane:
  - [ ] Missing required section (E110)
  - [ ] Multiple placeholders in one doc (E120)
  - [ ] Placeholder w code block (ignore case)
  - [ ] Invalid frontmatter (missing required field)
  - [ ] Invalid enum value (status="darft")
  - [ ] Invalid date format (created="2025/12/28")
  - [ ] Empty document (no sections)
  - [ ] Document bez frontmatter
  - [ ] Unicode w placeholders (obsługa CJK, emoji)
- [ ] Expected ValidationResults dla każdego przypadku udokumentowane:
  - [ ] Gap type (E110, E120, etc.)
  - [ ] Severity (critical, high, medium, low)
  - [ ] Location (line number, section)
  - [ ] Remediation steps

### 6. Kryteria Akceptacji
- [ ] **Performance**: Walidacja 100 dokumentów < 1 sekunda (NFR-001)
  - [ ] Individual doc validation: < 10ms per document
  - [ ] Schema loading: lazy loading, cache
- [ ] **Accuracy**: > 95% precision/recall dla gap detection
  - [ ] False positive rate < 5% (E110, E120)
  - [ ] No missing critical gaps (E110 w production docs)
- [ ] **Error Handling**: Proper ValidationResult per ADR-008
  - [ ] Result type: ValidationResult(valid, gaps, errors)
  - [ ] Rich error messages z line numbers
  - [ ] No uncaught exceptions
- [ ] **Coverage**: Minimum 85% pokrycia testami (unit + integration)
  - [ ] Unit tests dla każdego gap detection method
  - [ ] Integration tests z Parser output
  - [ ] Edge case tests (malformed schemas, invalid docs)
- [ ] **Documentation**: Docstrings dla wszystkich public methods
  - [ ] ValidatorAPI class documented
  - [ ] Gap detection logic explained
  - [ ] Schema format documented

### 7. Plan Implementacji
- [ ] **Sprint 2 allocation**: Tygodnie 3-4 rezerwacji potwierdzona
- [ ] **Developer assigned**: Główny developer wyznaczony
- [ ] **Code structure uzgodniona**:
  - [ ] src/core/validator.py - główna logika walidacji
  - [ ] src/models/schema.py - DocumentSchema model
  - [ ] src/models/gap.py - Gap, ValidationResult models
  - [ ] schemas/ - YAML schemas per document type
  - [ ] tests/test_validator.py - testy jednostkowe
  - [ ] tests/test_validator_integration.py - testy integracyjne z Parser
  - [ ] tests/fixtures/ - sample documents, schemas
- [ ] **Build configuration**: pyproject.toml z Pydantic v2 dependency
- [ ] **CI/CD pipeline**: Pre-commit hooks, pytest w GitHub Actions

### 8. Edge Cases Identified
- [ ] **Malformed schemas**:
  - [ ] Invalid YAML syntax → graceful error
  - [ ] Missing required schema fields → validation error
  - [ ] Circular schema references → detection + error
- [ ] **Parser edge cases**:
  - [ ] Document z missing sections list → handle gracefully
  - [ ] Empty body → no E120 gaps (no false positives)
  - [ ] Null frontmatter → E110 gap generated
- [ ] **Regex edge cases**:
  - [ ] Section pattern match: case-insensitive option
  - [ ] Multi-line placeholders (TODO spanning 2 lines)
  - [ ] Placeholder w URL (https://example.com/TODO) → ignore
- [ ] **Performance edge cases**:
  - [ ] Large documents (>10MB) → streaming/chunking
  - [ ] Deep nested sections (>10 levels) → recursion limit

### 9. Zidentyfikowane Blokery
- [ ] Brak blokerów LUB blokery udokumentowane z mitigation plan:
  - [ ] Bloker 1: COMP-001-parser nie gotowy
    - Mitigation: Mock Document objects dla development, integration tests po Sprint 1
  - [ ] Bloker 2: Schemas nie finalized dla wszystkich doc types
    - Mitigation: Start z 3 core types (PRD, ADR, RFC), iterate w Sprint 3+
  - [ ] Bloker 3: E170/E180 detection logic complex
    - Mitigation: MVP w Sprint 2 = E110 + E120 tylko, E170/E180 w Sprint 6

### 10. Zatwierdzenia i Review
- [ ] **Tech Lead review**: Architektura i design approved
- [ ] **QA review**: Test plan zatwierdzony
- [ ] **Peer review**: Co-worker (developer) przejrzał i zatwierdził
- [ ] **No open comments**: Wszystkie review comments resolved

---

## Metryki Sukcesu

| Kryterium | Status | Notes |
|-----------|--------|-------|
| Wszystkie checkboxy powyżej zaznaczone | [ ] | Go/No-Go signal |
| Tech Lead peer review passed | [ ] | Architecture & Design approved |
| QA plan review passed | [ ] | Test coverage & cases approved |
| Sprint 2 slot confirmed | [ ] | Resource allocation |
| Pydantic v2 installed and validated | [ ] | Library dependency |
| 3+ document type schemas drafted | [ ] | Schema coverage |
| Gap detection rules enumerated | [ ] | E110, E120 logic documented |
| Go/No-Go decision | **GO** / NO-GO | Final gate |

---

## Zatwierdzenia

| Rola | Imię | Data | Status |
|------|------|------|--------|
| **Tech Lead** | [TBD] | [TBD] | Pending |
| **QA Lead** | [TBD] | [TBD] | Pending |
| **Product Owner** | [TBD] | [TBD] | Pending |

---

## Notatki i Context

### Timeline
- **DoR Creation Date**: 2025-12-28
- **Target Sprint Start**: Sprint 2 Day 1 (Week 3)
- **Planned Completion**: Sprint 2 End (Week 4)
- **DoR Review Deadline**: [TBD - przed Sprint 2]
- **Dependency**: COMP-001-parser (Sprint 1) musi być complete

### Validator Scope (Sprint 2)
**In Scope**:
- E110 detection (Missing Sections) - critical dla DoR/DoD gates
- E120 detection (Placeholders: TODO/TBD/FIXME) - blocker dla REQ-FREEZE
- Pydantic v2 frontmatter validation (FR-006)
- Schema loading z YAML (3 document types minimum)

**Out of Scope** (defer do later sprints):
- E170 (Evidence notes) - defer Sprint 6
- E180 (Storytelling) - defer Sprint 6
- E190 (Alternatives) - defer Sprint 6
- E200 (Post-mortem) - defer Sprint 6
- GUI integration - defer Sprint 4
- CI/CD pre-commit hook - defer post-MVP

### Performance Baseline
- **Target**: < 10ms per document (NFR-001)
- **Evidence**: [E-145] Pydantic benchmark: 42μs/doc
- **Budget breakdown**:
  - Pydantic validation: ~0.05ms
  - Section checking (E110): ~5ms
  - Placeholder regex (E120): ~3ms
  - Total: ~8ms ✅ (under budget)

### Dodatkowe Zasoby
- Implementation Guide: [TBD]
- Pydantic v2 Migration Guide: https://docs.pydantic.dev/latest/migration/
- Regex Testing Tool: https://regex101.com/
- Schema Examples: schemas/prd.yaml, schemas/adr.yaml

---

## Linki do Dokumentów Powiązanych

- **Parent Component**: [COMP-002-validator](../../engineering/components/COMP-002-validator.md)
- **Architecture Decision Record**: [ADR-003](../../engineering/decisions/ADR-003-validation.md)
- **Error Handling Strategy**: [ADR-008](../../engineering/decisions/ADR-008-error-handling.md)
- **API Specification**: [API-SPEC-001](../../engineering/apis/API-SPEC-001.md)
- **PRD Requirements**: [PRD-V2](../../engineering/prd-v2.md) (FR-005 do FR-008)
- **Test Plan**: [TEST-COMP-002](../test-plans/TEST-COMP-002-validator.md) *(TBD - to be created)*
- **Dependency**: [COMP-001-parser](../../engineering/components/COMP-001-parser.md) (must complete Sprint 1)

---

**Status**: DRAFT → IN-REVIEW → APPROVED → READY-FOR-IMPLEMENTATION

**Ostatnia aktualizacja**: 2025-12-28
