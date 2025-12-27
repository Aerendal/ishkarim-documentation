# 📄 Test Plan / QA Strategy

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines requirements that must be tested"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§3 Test Scenarios"
        influence: "Functional requirements define what functionality to test"
      - from: "PRD §7 Use Cases & User Flows"
        to: "§3 Test Scenarios"
        influence: "Use cases become test scenarios"
      - from: "PRD §11 Success Metrics"
        to: "§5 Acceptance Criteria"
        influence: "Success metrics define pass/fail criteria"

  - id: BRD-*
    type: influences
    reason: "BRD requirements inform testing when PRD doesn't exist"
    conditions:
      - when: "!project.has_prd && project.has_brd"
        applies: true
    sections:
      - from: "BRD §5 Core Functional Requirements"
        to: "§3 Test Scenarios"
        influence: "Core requirements define minimum testing scope"

  - id: TDD-*
    type: influences
    reason: "TDD defines technical components that need testing"
    conditions:
      - when: "project.has_technical_design === true"
        applies: true
    sections:
      - from: "TDD §4 API Specifications"
        to: "§4 Integration Tests"
        influence: "API specs define integration test scenarios"

  - id: INTEGRATION-PLAN-*
    type: influences
    reason: "Integration Plan defines integration test requirements"
    conditions:
      - when: "project.has_integrations === true"
        applies: true
    sections:
      - from: "Integration Plan §5 Integration Testing"
        to: "§4 Integration Tests"
        influence: "Integration testing procedures become test plan scenarios"
```

### Impacts
```yaml
impacts:
  - id: TEST-SUMMARY-REPORT-*
    type: blocks
    reason: "Test Summary Report requires Test Plan execution results"
    conditions:
      - when: "testing.phase === 'completed'"
        applies: true
    sections:
      - from: "§3 Test Scenarios"
        to: "Test Summary Report §3 Test Results"
        influence: "Test scenarios executed and results reported in summary"
      - from: "§5 Acceptance Criteria"
        to: "Test Summary Report §4 Pass/Fail Analysis"
        influence: "Acceptance criteria determine pass/fail status"

  - id: UAT-PLAN-*
    type: influences
    reason: "UAT Plan builds on Test Plan foundation"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "§3 Test Scenarios"
        to: "UAT Plan §3 UAT Scenarios"
        influence: "Test scenarios inform UAT scenario design"

  - id: QA-PLAN-*
    type: influences
    reason: "Test Plan is part of overall QA strategy"
    conditions:
      - when: "project.has_qa_plan === true"
        applies: true
    sections:
      - from: "§2 Testing Scope"
        to: "QA Plan §2 Quality Objectives"
        influence: "Testing scope defines quality assurance coverage"

  - id: CHANGE-LOG-*
    type: informs
    reason: "Test results may trigger bug fixes documented in changelog"
    conditions:
      - when: "test_results.has_defects === true"
        applies: true
    sections:
      - from: "§3 Test Scenarios"
        to: "Change Log §4 Bug Fixes"
        influence: "Failed tests identify bugs for changelog"
```

### Related
```yaml
related:
  - id: RTM-*
    type: informs
    reason: "Requirements Traceability Matrix links tests to requirements"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance testing is specialized testing type"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TEST-PLAN-*.md"
    required: false
    purpose: "Track test case creation and execution tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TEST-PLAN-*.md"
    required: true
    purpose: "Store test cases, test data, test execution logs, defect reports"

  - type: DoR
    path: "satellites/dor/DOR-TEST-PLAN-*.md"
    required: true
    purpose: "Define prerequisites: requirements documented, test environment ready, test data prepared"

  - type: DoD
    path: "satellites/dod/DOD-TEST-PLAN-*.md"
    required: true
    purpose: "Define completion criteria: all tests executed, results documented, acceptance criteria met"
```

## Cel biznesowy / techniczny
Test Plan określa strategię testowania produktu, w tym typy testów, scenariusze i kryteria akceptacji. Dokument ten zapewnia, że produkt spełnia wymagania jakościowe i biznesowe.

## Zawartość
- Cele testowania
- Zakres testów
- Typy testów (unit, integracyjne, systemowe, akceptacyjne)
- Scenariusze testowe
- Kryteria przejścia i akceptacji
- Harmonogram testów

## Czego nie zawiera
- Raportów finansowych
- Treści marketingowych
- Kodów źródłowych

## Objętość
- 5–8 stron
- 10–15 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project manager
