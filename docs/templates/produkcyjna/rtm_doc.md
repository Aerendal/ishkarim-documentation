# 📄 Requirements Traceability Matrix (RTM)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines requirements that RTM tracks"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§2 Requirements List"
        influence: "PRD requirements become RTM entries for tracking"

  - id: BRD-*
    type: influences
    reason: "BRD requirements tracked when PRD doesn't exist"
    conditions:
      - when: "!project.has_prd && project.has_brd"
        applies: true
    sections:
      - from: "BRD §5 Core Requirements"
        to: "§2 Requirements List"
        influence: "BRD requirements tracked in RTM"

  - id: TEST-PLAN-*
    type: requires
    reason: "Test Plan defines test cases that verify requirements"
    conditions:
      - when: "project.has_testing === true"
        applies: true
    sections:
      - from: "Test Plan §3 Test Scenarios"
        to: "§3 Test Case Mapping"
        influence: "Test scenarios mapped to requirements for traceability"
```

### Impacts
```yaml
impacts:
  - id: TEST-SUMMARY-REPORT-*
    type: informs
    reason: "RTM shows requirements test coverage in test summary"
    conditions:
      - when: "testing.phase === 'completed'"
        applies: true
    sections:
      - from: "§4 Implementation Status"
        to: "Test Summary Report §5 Requirements Coverage"
        influence: "RTM demonstrates requirements coverage in test summary"

  - id: CLOSURE-REPORT-*
    type: informs
    reason: "RTM validates all requirements delivered for project closure"
    conditions:
      - when: "project.phase === 'closing'"
        applies: true
    sections:
      - from: "§4 Implementation Status"
        to: "Closure Report §2 Objectives Achieved"
        influence: "RTM completion status demonstrates requirements fulfillment"
```

### Related
```yaml
related:
  - id: QA-PLAN-*
    type: informs
    reason: "QA Plan defines quality standards for requirements tracking"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RTM-*.md"
    required: false
    purpose: "Track RTM updates as requirements evolve"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RTM-*.md"
    required: true
    purpose: "Store requirements traceability matrix, test coverage reports, verification records"

  - type: DoD
    path: "satellites/dod/DOD-RTM-*.md"
    required: true
    purpose: "Define completion criteria: all requirements tracked, tested, verified"
```

## Cel biznesowy / techniczny
Requirements Traceability Matrix (RTM) mapuje wymagania biznesowe i techniczne do odpowiednich przypadków testowych oraz implementacji. Pomaga zapewnić, że wszystkie wymagania zostały zrealizowane i przetestowane.

## Zawartość
- Lista wymagań biznesowych i technicznych
- Powiązane przypadki użycia
- Powiązane przypadki testowe
- Status realizacji (zaimplementowane / w trakcie / niezaimplementowane)
- Status testów (zdane / niezdane)

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych raportów finansowych
- Treści marketingowych

## Objętość
- 2–4 strony (lub tabela w arkuszu kalkulacyjnym)

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project managerowie
