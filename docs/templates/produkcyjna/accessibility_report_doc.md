# 📄 Accessibility Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines functional requirements that must meet accessibility standards"
    conditions:
      - when: "project.compliance.accessibility === true"
        applies: true
      - when: "project.type === 'internal-tool' && !regulatory_requirements"
        applies: false
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§3 Audit Results"
        influence: "Functional requirements determine what accessibility features need testing"
      - from: "PRD §6 Non-Functional Requirements"
        to: "§3 Audit Results"
        influence: "NFRs define accessibility performance and usability standards"

  - id: USER-GUIDE-*
    type: requires
    reason: "User Guide shows actual user interface that needs accessibility verification"
    conditions:
      - when: "project.has_ui === true"
        applies: true
      - when: "project.type === 'api-only'"
        applies: false
    sections:
      - from: "User Guide §3 User Interface Screenshots"
        to: "§3 Audit Results"
        influence: "UI screenshots provide visual basis for accessibility audit"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Compliance Report may specify accessibility regulatory requirements"
    conditions:
      - when: "project.industry in ['healthcare', 'government', 'education']"
        applies: true
      - when: "project.geography === 'EU' || project.geography === 'US'"
        applies: true
    sections:
      - from: "Compliance Report §2 Regulatory Requirements"
        to: "§2 Accessibility Standards"
        influence: "Regulatory requirements determine which accessibility standards apply (WCAG, ADA, Section 508)"
```

### Impacts
```yaml
impacts:
  - id: UAT-PLAN-*
    type: influences
    reason: "Accessibility issues must be tested during UAT with diverse user groups"
    conditions:
      - when: "accessibility_issues.severity === 'critical'"
        applies: true
      - when: "accessibility_report.compliance_level < 'AA'"
        applies: true
    sections:
      - from: "§4 Proposed Fixes"
        to: "UAT Plan §4 Test Scenarios"
        influence: "Proposed accessibility fixes define UAT test scenarios for verification"
      - from: "§3 Barriers and Issues"
        to: "UAT Plan §5 Acceptance Criteria"
        influence: "Known barriers inform accessibility acceptance criteria"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Training must address accessibility features and assistive technology usage"
    conditions:
      - when: "project.has_accessibility_features === true"
        applies: true
    sections:
      - from: "§5 Compliance Level"
        to: "Training Materials §3 Feature Documentation"
        influence: "Compliance level determines what accessibility features need training"

  - id: MAINTENANCE-GUIDE-*
    type: informs
    reason: "Maintenance procedures must preserve accessibility compliance"
    conditions:
      - when: "project.lifecycle === 'long-term'"
        applies: true
    sections:
      - from: "§2 Accessibility Standards"
        to: "Maintenance Guide §4 Compliance Checks"
        influence: "Standards define ongoing accessibility verification requirements"
```

### Related
```yaml
related:
  - id: QA-PLAN-*
    type: informs
    reason: "QA Plan should incorporate accessibility testing methodologies"

  - id: TEST-SUMMARY-REPORT-*
    type: informs
    reason: "Test Summary should report on accessibility testing outcomes"

  - id: DATA-GOVERNANCE-POLICY-*
    type: informs
    reason: "Data governance may include accessibility requirements for data presentation"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ACCESSIBILITY-REPORT-*.md"
    required: false
    purpose: "Track remediation action items for accessibility issues"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ACCESSIBILITY-REPORT-*.md"
    required: true
    purpose: "Store audit tool reports, screen reader testing results, WCAG compliance matrices"

  - type: DoD
    path: "satellites/dod/DOD-ACCESSIBILITY-REPORT-*.md"
    required: true
    purpose: "Define completion criteria: all critical issues resolved, AA compliance achieved"
```

## Cel biznesowy / techniczny
Accessibility Compliance Report ocenia zgodność systemu z wymaganiami dostępności (np. WCAG, ADA). Dokument gwarantuje, że produkt jest dostępny dla wszystkich użytkowników, w tym osób z niepełnosprawnościami.

## Zawartość
- Standardy dostępności, do których odnosi się projekt
- Wyniki audytu dostępności
- Lista barier i problemów
- Propozycje poprawek
- Poziom zgodności (A, AA, AAA)

## Czego nie zawiera
- Kodów źródłowych
- Analiz finansowych
- Strategii marketingowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- QA / testerzy
- Developerzy
- Project managerowie
- Organizacje dbające o dostępność
