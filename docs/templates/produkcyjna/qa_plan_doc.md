# 📄 Quality Assurance Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines quality objectives and acceptance criteria"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §11 Success Metrics"
        to: "§2 Quality Objectives"
        influence: "PRD success metrics define quality goals"

  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines quality standards and compliance requirements"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §12 Objectives"
        to: "§2 Quality Objectives"
        influence: "Project objectives inform quality objectives"
```

### Impacts
```yaml
impacts:
  - id: TEST-PLAN-*
    type: blocks
    reason: "QA Plan defines testing strategy that Test Plan implements"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Test Strategy"
        to: "Test Plan §2 Testing Approach"
        influence: "QA strategy defines test plan approach"

  - id: UAT-PLAN-*
    type: influences
    reason: "QA Plan includes UAT as part of quality assurance"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "§15 Acceptance Criteria"
        to: "UAT Plan §6 Acceptance Criteria"
        influence: "QA acceptance criteria define UAT pass/fail criteria"

  - id: TEST-SUMMARY-REPORT-*
    type: informs
    reason: "Test summary validates QA plan effectiveness"
    conditions:
      - when: "testing.phase === 'completed'"
        applies: true
    sections:
      - from: "§12 Test Metrics"
        to: "Test Summary Report §5 Quality Metrics"
        influence: "QA metrics define what test summary reports"
```

### Related
```yaml
related:
  - id: RTM-*
    type: informs
    reason: "RTM tracks requirements coverage per QA plan"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "QA Plan ensures compliance with quality standards"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-QA-PLAN-*.md"
    required: false
    purpose: "Track QA plan implementation and process improvements"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-QA-PLAN-*.md"
    required: true
    purpose: "Store quality audits, test metrics, process compliance evidence"

  - type: DoD
    path: "satellites/dod/DOD-QA-PLAN-*.md"
    required: true
    purpose: "Define completion criteria: all QA processes documented, tools established, team trained"
```

## Cel biznesowy / techniczny
Quality Assurance Plan (QA Plan) definiuje procesy, standardy i procedury zapewnienia jakości w projekcie. Pomaga utrzymać wysoką jakość produktu na każdym etapie cyklu życia.

## Zawartość

### Quality Objectives
Cele jakościowe projektu i definicja "quality" w kontekście produktu.

### Quality Standards & Compliance
Standardy jakości (ISO 9001, ISTQB, IEEE), regulacje branżowe, compliance requirements.

### Roles & Responsibilities
Role w QA (QA Lead, Test Engineers, Developers, Product Owner) i ich odpowiedzialności.

### Test Strategy
Strategia testowania:
- Typy testów (unit, integration, system, UAT, regression, performance, security)
- Poziomy testowania (component, integration, system, acceptance)
- Podejście (manual vs automated testing ratio)

### Test Planning & Execution
Proces planowania testów, przygotowania test cases, execution, defect tracking.

### Test Environments
Środowiska testowe (dev, staging, pre-prod, prod) i ich konfiguracja.

### Entry & Exit Criteria
Kryteria wejścia i wyjścia dla każdej fazy testowej.

### Test Deliverables
Artefakty testowe: test plans, test cases, test scripts, test data, defect reports, test summary reports.

### Defect Management
Proces zgłaszania, kategoryzacji, priorytetyzacji i tracking'u defektów.

### Validation & Verification Procedures
Procedury V&V (Verification: czy budujemy produkt poprawnie? Validation: czy budujemy poprawny produkt?).

### Test Tools & Infrastructure
Narzędzia QA (test management, automation, CI/CD, performance testing, security scanning).

### Test Metrics & Reporting
Metryki jakości (test coverage, defect density, pass/fail rates) i procedury raportowania.

### Risk-Based Testing
Podejście do testowania opartego na ryzyku - priorytetyzacja testów według ryzyka biznesowego.

### Regression Testing Strategy
Strategia testów regresji i automated regression suites.

### Acceptance Criteria
Kryteria akceptacji produktu przez klienta/stakeholderów.

### QA Schedule & Milestones
Harmonogram działań QA zintegrowany z timeline'em projektu.

## Czego nie zawiera
- Strategii sprzedażowych
- Szczegółowych kodów źródłowych
- Analiz finansowych

## Objętość
- 8–12 stron
- 20–25 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project managerowie
