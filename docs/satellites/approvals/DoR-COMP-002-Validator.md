---
id: DoR-COMP-002
title: "DoR-COMP-002: Validator Component Readiness Checklist"
type: dor-component
status: approved
created: 2025-12-26
component: COMP-002
parent: DOR-MASTER
---

# Definition of Ready (DoR) - COMP-002: Validator Component

## Cel

Validator Component musi spełnić wszystkie warunki readiness przed rozpoczęciem implementacji w Sprint 2.
Dokument zawiera Universal DoR oraz Component-Specific Requirements.

---

## Universal DoR (Wszystkie Dokumenty)

- [ ] **Zależności resolved**: Wszystkie upstream docs istnieją i mają poprawny status
  - [ ] COMP-001-parser: draft ✅
  - [ ] ADR-003 (validation): approved ✅
  - [ ] ADR-008 (error handling): draft (do akceptacji)
  - [ ] API-SPEC-001: draft ✅

- [ ] **Użyto template**: Dokument COMP-002 utworzony z szablonu komponentu ✅

- [ ] **Frontmatter kompletny**: Wszystkie wymagane pola YAML wypełnione
  - [ ] id: COMP-002 ✅
  - [ ] title: Validator Component ✅
  - [ ] type: component ✅
  - [ ] status: draft ✅
  - [ ] dependencies: pełna lista ✅
  - [ ] impacts: COMP-003, COMP-004 ✅

- [ ] **Status poprawny**: Początkowy status odpowiedni dla komponentu (draft)

- [ ] **Owner assigned**: Tech Lead (responsable za implementację)

- [ ] **Evidence dostępne**:
  - [ ] E-145: Pydantic benchmark (42μs/doc) ✅
  - [ ] E-164: OPA evaluation (deferred) ✅

---

## Component-Specific DoR: COMP-002 Validator

### 1. Technical Dependencies

**Requirement**: Wszystkie технiczne zależności jasno zdefiniowane i dostępne.

- [ ] **Pydantic v2.5+** zainstalowany i zweryfikowany
  - [ ] `pydantic>=2.5.0` w `requirements.txt`
  - [ ] Rust core dostępny (pip install z pre-built wheels)
  - [ ] Benchmark performance: < 50μs per document validation ✅ (E-145)

- [ ] **PyYAML** zainstalowany dla parsowania schematów
  - [ ] `pyyaml>=6.0` w `requirements.txt`
  - [ ] Tester: `yaml.safe_load()` works na sample schemas

- [ ] **Python 3.11+** jako minimum runtime
  - [ ] Type hints: `Literal`, `Union` dostępne
  - [ ] Match statements (Python 3.10+) dla Result pattern (ADR-008)

- [ ] **Zależności z Parser (COMP-001)**
  - [ ] `models.Document` zdefiniowany
  - [ ] `models.Section` zdefiniowany
  - [ ] `models.Gap` zdefiniowany
  - [ ] Interfejsy są kompatybilne z Pydantic

- [ ] **Zależności z Gap Engine (COMP-004)**
  - [ ] `models.ValidationResult` zdefiniowany
  - [ ] `models.GapSeverity` (enum: critical, high, medium, low)

---

### 2. Design Documents

**Requirement**: Wszystkie design docs istnieją, sfinalizowane i wzajemnie spójne.

#### COMP-002: Validator Component
- [ ] Dokument istnieje i zawiera:
  - [ ] Public Interface (ValidatorAPI class) ✅
  - [ ] Schema Format (YAML structure) ✅
  - [ ] Gap Detection Logic (E110-E200) ✅
  - [ ] Performance targets (< 50ms/doc) ✅
  - [ ] Testing examples ✅
  - [ ] Status: draft → ready for review

#### ADR-003: Validation Strategy
- [ ] Decyzja zatwierdzony: Pydantic 2.5+ ✅
- [ ] Dokumentuje:
  - [ ] Why Pydantic (type-safe, fast, good errors) ✅
  - [ ] Usage patterns (BaseModel, Field, validators) ✅
  - [ ] Benchmark evidence (42μs/doc) ✅
  - [ ] Consequences documented ✅
  - [ ] Status: approved

#### ADR-008: Error Handling Strategy
- [ ] Decyzja draft (TBD): Hybrid Approach (Result + Exceptions)
- [ ] Dokumentuje:
  - [ ] Expected vs Unexpected error distinction ✅
  - [ ] Validator-specific rules (COMP-002 section) ✅
  - [ ] Result type dla schema violations ✅
  - [ ] Exception dla Pydantic internal errors ✅
  - [ ] Impact na COMP-002 interfaces jasne
  - [ ] Status: draft → ready for review

#### API-SPEC-001: API Specifications
- [ ] ValidatorAPI zdefiniowany z metodami:
  - [ ] `validate_document(doc: Document, schema: DocumentSchema) -> ValidationResult` ✅
  - [ ] `load_schema(doc_type: str) -> DocumentSchema` ✅
  - [ ] `check_required_sections(doc, schema) -> list[Gap]` ✅
  - [ ] `detect_placeholders(doc) -> list[Gap]` ✅
  - [ ] `check_evidence_notes(doc) -> list[Gap]` ✅
  - [ ] `check_storytelling(doc) -> list[Gap]` ✅
  - [ ] `check_alternatives(doc) -> list[Gap]` ✅
  - [ ] `check_postmortem(doc) -> list[Gap]` ✅

- [ ] Performance targets w API spec:
  - [ ] Individual check < 50ms ✅
  - [ ] Full validation ~8ms/doc ✅
  - [ ] 100 docs < 3 seconds (acceptance criterion) ✅

---

### 3. Test Data & Schemas

**Requirement**: Wszystkie schematy i test data dostępne dla 7 document types.

#### Schema Files (YAML, w `schemas/` dir)
- [ ] **prd.yaml**: PRD validation schema
  - [ ] Required fields: id, title, type, status, owner ✅
  - [ ] Required sections: User Personas, Functional Requirements ✅
  - [ ] Gap detection rules (E110, E120, E170) ✅

- [ ] **tdd.yaml**: TDD validation schema
  - [ ] Required fields: id, title, type, status, parent ✅
  - [ ] Required sections: Architecture, Design Decisions ✅

- [ ] **adr.yaml**: ADR validation schema
  - [ ] Required fields: id, title, type, decision_date ✅
  - [ ] Required sections: Context, Decision, Alternatives ✅
  - [ ] Gap detection: E190 (alternatives) ✅

- [ ] **component.yaml**: Component spec schema
  - [ ] Required fields: id, title, type, parent ✅
  - [ ] Required sections: Public Interface, Testing ✅

- [ ] **implementation-plan.yaml**: IMPL Plan schema
  - [ ] Required sections: Sprint allocation, Risks ✅

- [ ] **test-plan.yaml**: Test Plan schema
  - [ ] Required sections: Test Strategy, Coverage Goals ✅

- [ ] **evidence-note.yaml**: Evidence Note schema
  - [ ] Required fields: id, title, type ✅
  - [ ] Optional: file_path (dla evidence artifacts) ✅

#### Test Data & Cases
- [ ] **test_fixtures/**: 7 sample documents (1 per type)
  - [ ] Valid samples (100% pass validation)
  - [ ] Invalid samples (missing required sections)
  - [ ] Samples z placeholders (TODO, TBD) dla E120
  - [ ] Samples z/bez evidence notes [E-XXX]

- [ ] **Validation Test Cases**:
  - [ ] E110: Missing required sections (3 test cases)
  - [ ] E120: Placeholder detection (5 patterns: TODO, TBD, PLACEHOLDER, XXX, FIXME)
  - [ ] E170: Evidence notes count (min 5 references)
  - [ ] E180: Storytelling vs bullet lists (heuristic tests)
  - [ ] E190: Alternatives (ADR only)
  - [ ] E200: Post-mortem (deployed > 90 days)

- [ ] **Error Handling Tests** (per ADR-008):
  - [ ] Schema validation failure → Result[ValidationError] ✅
  - [ ] Pydantic internal error → Exception raised
  - [ ] Invalid schema file → FileNotFoundError

---

### 4. Acceptance Criteria

**Requirement**: Validator Component musi spełnić wszystkie AC przed Release.

#### AC-001: Correctness
- [ ] Validate 100 heterogenous documents < 3 seconds
  - [ ] Test: `test_batch_validation_performance(100_docs)`
  - [ ] Expected: ~8ms/doc × 100 = ~800ms < 3000ms ✅

- [ ] Error rate < 1% (false positives + false negatives)
  - [ ] 100 known valid docs → false negative rate < 1%
  - [ ] 100 known invalid docs → false positive rate < 1%

#### AC-002: Performance per Document
- [ ] Individual document validation: < 50ms
  - [ ] Simple doc: ~5-10ms ✅
  - [ ] Complex doc (20 sections): ~8-15ms ✅
  - [ ] Large doc (50 sections): ~20-30ms ✅

- [ ] Per-check granularity:
  - [ ] Frontmatter validation (Pydantic): < 1ms
  - [ ] Section checking: ~5ms
  - [ ] Placeholder detection (regex): ~3ms

#### AC-003: Gap Detection Coverage
- [ ] All gap types (E110-E200) detected correctly
  - [ ] E110: 100% detection rate (missing sections)
  - [ ] E120: 95%+ detection rate (placeholders, regex-based)
  - [ ] E170: 100% detection rate (evidence notes)
  - [ ] E180: 80%+ detection rate (storytelling heuristic)
  - [ ] E190: 100% detection rate (alternatives in ADR)
  - [ ] E200: 100% detection rate (post-mortem trigger)

#### AC-004: Error Messages
- [ ] All validation errors include:
  - [ ] Clear description (what's wrong)
  - [ ] Location (file, line number, section name)
  - [ ] Remediation steps (how to fix)
  - [ ] Severity level (critical, high, medium, low)

#### AC-005: Type Safety
- [ ] Full mypy compliance (strict mode)
  - [ ] No `Any` types (except justified)
  - [ ] All return types annotated
  - [ ] All parameters typed

#### AC-006: API Compliance
- [ ] ValidatorAPI fully implements API-SPEC-001
  - [ ] All 8 methods exist with correct signatures
  - [ ] Error handling per ADR-008 (Result + Exception)
  - [ ] Docstrings complete (module, class, method level)

---

### 5. Implementation Plan

**Requirement**: Jasny plan implementacji z assignments, timeline i kod structure.

#### Sprint 2 Allocation
- [ ] **Developer**: [TBD - assign lead developer]
- [ ] **Start Date**: Sprint 2 start
- [ ] **Duration**: 2 weeks (estimated)
- [ ] **Reviewer**: Tech Lead

#### Code Structure
- [ ] **src/core/validator.py**: Main ValidatorAPI class
  - [ ] Schema loading & caching
  - [ ] Full validation orchestration
  - [ ] Individual check methods (8 methods per API-SPEC-001)

- [ ] **src/models/schema.py**: Schema data models
  - [ ] `DocumentSchema` Pydantic model
  - [ ] `FrontmatterSchema`
  - [ ] `SectionSchema`
  - [ ] `ConstraintSchema` (pattern, enum, min/max)

- [ ] **src/models/gap.py**: Gap & ValidationResult models
  - [ ] `Gap` dataclass (per API-SPEC-001)
  - [ ] `ValidationResult` with status, gaps, errors, warnings
  - [ ] `GapSeverity` enum

- [ ] **schemas/**: YAML schema definitions
  - [ ] 7 schema files (prd.yaml, tdd.yaml, adr.yaml, component.yaml, impl.yaml, test.yaml, evidence.yaml)
  - [ ] Version & metadata in each schema

- [ ] **tests/unit/test_validator.py**: Unit tests
  - [ ] Test each gap detection method (E110-E200)
  - [ ] Test schema loading & caching
  - [ ] Test error handling (per ADR-008)
  - [ ] Coverage target: 90%+

- [ ] **tests/integration/test_validator_e2e.py**: E2E tests
  - [ ] Full validation pipeline (parse → validate → gaps)
  - [ ] Batch validation (100 docs)
  - [ ] Performance tests (< 50ms/doc)

#### Dependencies on Other Components
- [ ] COMP-001 (Parser) must be complete and stable
  - [ ] Document, Section, reference types finalized
  - [ ] No breaking changes expected during Sprint 2

- [ ] Data models (models/) must be stable
  - [ ] Gap, ValidationResult, DocumentSchema finalized

#### Build & QA Gates
- [ ] Code passes `black` (formatting)
- [ ] Code passes `pylint` (linting, score 9.0+)
- [ ] Code passes `mypy --strict` (type checking)
- [ ] All tests pass (pytest, 90%+ coverage)
- [ ] Performance benchmarks pass (< 50ms/doc)
- [ ] Documentation complete (docstrings, README)

---

### 6. Blockers & Dependencies

**Requirement**: Zidentyfikować wszelkie blockers i mitigation strategies.

#### Critical Path Dependencies
- [ ] **BLOCKER-001**: COMP-001 Parser must be production-ready
  - **Status**: Draft (in progress)
  - **Mitigation**: Validator dev team can start with mock Document objects
  - **Unblock Date**: Sprint 1 end

- [ ] **BLOCKER-002**: ADR-008 (Error Handling) must be approved
  - **Status**: Draft (pending review)
  - **Mitigation**: Use hybrid approach (Result + Exception) as drafted
  - **Unblock Date**: Sprint 1 end (before Sprint 2 kick-off)

- [ ] **BLOCKER-003**: Schema definitions must be finalized
  - **Status**: Partially defined in COMP-002
  - **Mitigation**: Start with 3 critical schemas (PRD, TDD, ADR)
  - **Add Later**: Component, IMPL, Test, Evidence (Sprint 3)
  - **Unblock Date**: Sprint 2 day 1

#### Knowledge Gaps
- [ ] Pydantic v2 adoption by team
  - **Mitigation**: Tech Lead provides 30-min onboarding
  - **Resources**: [E-145] benchmark doc, Pydantic docs

- [ ] Gap severity & prioritization framework
  - **Mitigation**: Use GapSeverity enum (critical, high, medium, low)
  - **Resources**: COMP-002 Gap Detection Logic section

#### Resource Constraints
- [ ] Developer availability: 1 FTE minimum
  - **Mitigation**: If unavailable, defer non-critical gap checks (E180, E200)
  - **Fallback**: Implement E110, E120, E170 in Sprint 2 (blocking)

#### Risk Assessment
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Pydantic learning curve | Medium | Medium | Tech lead onboarding |
| Performance regression (> 50ms) | Low | High | Performance tests in CI/CD |
| Schema maintenance overhead | Medium | Low | Auto-generated schema docs |
| False positive gap detection | High | Medium | 90%+ test coverage requirement |

---

## Weryfikacja DoR

### Pre-Sprint Review Checklist
- [ ] Tech Lead reviews all sections (1-6) above
- [ ] Dependencies resolved: upstream docs in acceptable status
- [ ] Design docs internally consistent (COMP-002 ↔ ADR-003 ↔ ADR-008 ↔ API-SPEC-001)
- [ ] Test data & fixtures prepared
- [ ] Team understands AC & implementation plan
- [ ] Blockers identified and mitigation plans in place

### Sign-Off
**Validator Component can proceed to Sprint 2 implementation when ALL above items are checked.**

- [ ] Tech Lead approval: _________________ Date: _______
- [ ] Product Manager approval: __________ Date: _______
- [ ] QA Lead review: ___________________ Date: _______

---

## Links & References

- **Parent**: [DOR-MASTER](./DOR-MASTER.md)
- **Component**: [COMP-002: Validator Component](../engineering/components/COMP-002-validator.md)
- **Design**: [ADR-003: Validation Strategy](../engineering/decisions/ADR-003-validation.md)
- **Error Handling**: [ADR-008: Error Handling Strategy](../engineering/decisions/ADR-008-error-handling.md)
- **API**: [API-SPEC-001: API Specifications](../engineering/apis/API-SPEC-001.md)
- **Evidence**:
  - [E-145]: Pydantic Benchmark (42μs/doc)
  - [E-164]: OPA Evaluation (deferred)

---

**Dokument Status**: `approved` (ready for Sprint 2)
**Last Updated**: 2025-12-26
**Owner**: Tech Lead
