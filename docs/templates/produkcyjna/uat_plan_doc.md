# 📄 User Acceptance Test (UAT) Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines user stories and requirements that UAT must validate"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §4 User Stories & Personas"
        to: "§5 UAT Scenarios"
        influence: "User stories become UAT acceptance scenarios"
      - from: "PRD §11 Success Metrics"
        to: "§6 Acceptance Criteria"
        influence: "Success metrics define UAT pass/fail criteria"

  - id: TEST-PLAN-*
    type: requires
    reason: "Test Plan provides foundation for UAT planning"
    conditions:
      - when: "project.has_test_plan === true"
        applies: true
    sections:
      - from: "Test Plan §3 Test Scenarios"
        to: "§5 UAT Scenarios"
        influence: "Test scenarios inform UAT scenario design"

  - id: USER-GUIDE-*
    type: influences
    reason: "User Guide helps UAT participants understand system functionality"
    conditions:
      - when: "project.has_user_guide === true"
        applies: true
    sections:
      - from: "User Guide §3 Feature Documentation"
        to: "§5 UAT Scenarios"
        influence: "User guide features inform UAT testing scope"
```

### Impacts
```yaml
impacts:
  - id: TEST-SUMMARY-REPORT-*
    type: influences
    reason: "UAT results are part of overall test summary"
    conditions:
      - when: "uat.phase === 'completed'"
        applies: true
    sections:
      - from: "§6 UAT Results"
        to: "Test Summary Report §3 UAT Results"
        influence: "UAT outcomes reported in test summary"

  - id: CLOSURE-REPORT-*
    type: informs
    reason: "UAT acceptance is milestone for project closure"
    conditions:
      - when: "uat.status === 'passed'"
        applies: true
    sections:
      - from: "§6 UAT Results"
        to: "Closure Report §2 Objectives Achieved"
        influence: "Successful UAT validates project objectives achieved"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "UAT feedback identifies training needs"
    conditions:
      - when: "uat.reveals_training_gaps === true"
        applies: true
    sections:
      - from: "§6 UAT Results"
        to: "Training Materials §2 Training Topics"
        influence: "UAT challenges identify areas needing better training"

  - id: CHANGE-LOG-*
    type: informs
    reason: "UAT defects may trigger changes documented in changelog"
    conditions:
      - when: "uat.has_defects === true"
        applies: true
    sections:
      - from: "§6 UAT Results"
        to: "Change Log §4 Bug Fixes"
        influence: "UAT-identified bugs become changelog entries"
```

### Related
```yaml
related:
  - id: QA-PLAN-*
    type: informs
    reason: "UAT is part of overall quality assurance strategy"

  - id: ACCESSIBILITY-REPORT-*
    type: informs
    reason: "UAT should include accessibility testing with diverse users"

  - id: ONBOARDING-GUIDE-*
    type: informs
    reason: "UAT participants may need onboarding to system"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-UAT-*.md"
    required: false
    purpose: "Track UAT coordination, participant recruitment, scenario execution"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-UAT-*.md"
    required: true
    purpose: "Store UAT test results, user feedback, sign-off documents, defect reports"

  - type: DoR
    path: "satellites/dor/DOR-UAT-*.md"
    required: true
    purpose: "Define prerequisites: system ready, test data prepared, participants trained, scenarios documented"

  - type: DoD
    path: "satellites/dod/DOD-UAT-*.md"
    required: true
    purpose: "Define completion criteria: all scenarios tested, acceptance criteria met, stakeholders signed off"
```

## Cel biznesowy / techniczny
UAT Plan definiuje sposób przeprowadzania testów akceptacyjnych przez użytkowników końcowych. Dokument potwierdza, że system spełnia wymagania biznesowe i jest gotowy do wdrożenia.

## Zawartość
- Cele testów UAT
- Zakres testowania
- Kryteria wejścia i wyjścia
- Role i odpowiedzialności uczestników
- Scenariusze testowe
- Kryteria akceptacji
- Harmonogram testów

## Czego nie zawiera
- Kodów źródłowych
- Detali implementacyjnych
- Analiz finansowych

## Objętość
- 3–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Użytkownicy końcowi
- QA / testerzy
- Project managerowie
