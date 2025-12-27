# 📄 Test Summary Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: TEST-PLAN-*
    type: requires
    reason: "Test Plan defines what was tested and how"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Test Plan §3 Test Scenarios"
        to: "§2 Tests Executed"
        influence: "Test scenarios from plan executed and results reported"
      - from: "Test Plan §5 Acceptance Criteria"
        to: "§4 Pass/Fail Analysis"
        influence: "Acceptance criteria determine pass/fail status"

  - id: UAT-PLAN-*
    type: influences
    reason: "UAT results are part of test summary"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "UAT Plan §6 UAT Results"
        to: "§3 UAT Results"
        influence: "UAT outcomes included in test summary report"

  - id: PERFORMANCE-TEST-REPORT-*
    type: influences
    reason: "Performance test results are part of test summary"
    conditions:
      - when: "project.has_performance_testing === true"
        applies: true
    sections:
      - from: "Performance Test Report §3 Test Results"
        to: "§3 Performance Test Results"
        influence: "Performance test outcomes included in summary"
```

### Impacts
```yaml
impacts:
  - id: CLOSURE-REPORT-*
    type: influences
    reason: "Test summary validates quality objectives for project closure"
    conditions:
      - when: "project.phase === 'closing'"
        applies: true
    sections:
      - from: "§4 Pass/Fail Analysis"
        to: "Closure Report §2 Objectives Achieved"
        influence: "Test results demonstrate quality objectives met"

  - id: CHANGE-LOG-*
    type: informs
    reason: "Test defects become bug fixes in changelog"
    conditions:
      - when: "test_results.has_defects === true"
        applies: true
    sections:
      - from: "§4 Defects Found"
        to: "Change Log §4 Bug Fixes"
        influence: "Test defects tracked and fixed become changelog entries"

  - id: RELEASE-MANAGEMENT-PLAN-*
    type: blocks
    reason: "Test summary determines release readiness"
    conditions:
      - when: "test_results.determines_release === true"
        applies: true
    sections:
      - from: "§6 Release Recommendation"
        to: "Release Management Plan §3 Go/No-Go Decision"
        influence: "Test summary recommendation drives release decision"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Test findings may reveal training needs"
    conditions:
      - when: "test_results.reveals_usability_issues === true"
        applies: true
    sections:
      - from: "§4 Defects Found"
        to: "Training Materials §3 User Training Topics"
        influence: "Usability defects identify areas needing better training"
```

### Related
```yaml
related:
  - id: QA-PLAN-*
    type: informs
    reason: "Test summary validates QA plan effectiveness"

  - id: RTM-*
    type: informs
    reason: "Test summary shows requirements coverage via traceability matrix"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TEST-SUMMARY-*.md"
    required: false
    purpose: "Track defect resolution and retest tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TEST-SUMMARY-*.md"
    required: true
    purpose: "Store test execution logs, defect reports, test coverage reports, test artifacts"

  - type: DoD
    path: "satellites/dod/DOD-TEST-SUMMARY-*.md"
    required: true
    purpose: "Define completion criteria: all tests executed, results analyzed, recommendation documented"
```

## Cel biznesowy / techniczny
Test Summary Report podsumowuje wyniki testów przeprowadzonych w projekcie. Umożliwia ocenę, czy produkt spełnia kryteria jakościowe i biznesowe.

## Zawartość
- Zakres przeprowadzonych testów
- Wyniki testów (zdane/niezdane)
- Liczba i typy wykrytych defektów
- Ocena pokrycia testowego
- Wnioski dotyczące jakości
- Rekomendacja (gotowe do wydania / wymaga poprawek)

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych implementacji testów
- Raportów finansowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project managerowie
