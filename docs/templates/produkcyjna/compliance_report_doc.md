# 📄 Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines requirements that must comply with regulations"
    conditions:
      - when: "project.has_regulatory_requirements === true"
        applies: true
      - when: "project.industry in ['healthcare', 'finance', 'government']"
        applies: true
      - when: "project.type === 'internal-tool' && !regulatory_scope"
        applies: false
    sections:
      - from: "PRD §6 Non-Functional Requirements"
        to: "§2 Compliance Status"
        influence: "NFR compliance requirements define what needs verification"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines security controls required for regulatory compliance"
    conditions:
      - when: "compliance.includes_security_standards === true"
        applies: true
    sections:
      - from: "Security Plan §3 Access Control Policies"
        to: "§3 Audit Procedures"
        influence: "Security policies must comply with regulatory access control requirements"
      - from: "Security Plan §5 Data Protection"
        to: "§2 Compliance Status"
        influence: "Data protection measures demonstrate compliance with privacy regulations (GDPR, HIPAA)"

  - id: DATA-GOVERNANCE-POLICY-*
    type: requires
    reason: "Data governance policies ensure compliance with data handling regulations"
    conditions:
      - when: "compliance.covers_data_privacy === true"
        applies: true
    sections:
      - from: "Data Governance Policy §3 Data Quality Standards"
        to: "§2 Compliance Status"
        influence: "Data quality standards demonstrate compliance with data accuracy requirements"
```

### Impacts
```yaml
impacts:
  - id: ACCESSIBILITY-REPORT-*
    type: influences
    reason: "Accessibility compliance may be part of overall compliance requirements"
    conditions:
      - when: "compliance.includes_accessibility === true"
        applies: true
    sections:
      - from: "§1 Applicable Regulations"
        to: "Accessibility Report §2 Accessibility Standards"
        influence: "Regulatory requirements determine accessibility standards (WCAG, ADA, Section 508)"

  - id: SECURITY-PLAN-*
    type: influences
    reason: "Compliance gaps require security plan updates"
    conditions:
      - when: "compliance_status.has_gaps === true"
        applies: true
    sections:
      - from: "§5 Remediation Plan"
        to: "Security Plan §6 Security Improvements"
        influence: "Compliance gaps drive security control enhancements"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Compliance requirements need staff training"
    conditions:
      - when: "compliance.requires_training === true"
        applies: true
    sections:
      - from: "§1 Applicable Regulations"
        to: "Training Materials §3 Compliance Training"
        influence: "Regulatory requirements define compliance training needs"
```

### Related
```yaml
related:
  - id: BCP-*
    type: informs
    reason: "Some regulations require business continuity planning"

  - id: DRP-*
    type: informs
    reason: "Disaster recovery may be regulatory requirement"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor compliance is part of organizational compliance"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-COMPLIANCE-*.md"
    required: false
    purpose: "Track remediation actions for compliance gaps"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-COMPLIANCE-*.md"
    required: true
    purpose: "Store audit reports, certifications, regulatory correspondence, compliance evidence"

  - type: DoD
    path: "satellites/dod/DOD-COMPLIANCE-*.md"
    required: true
    purpose: "Define completion criteria: all regulations verified, gaps remediated, audit passed"
```

## Cel biznesowy / techniczny
Compliance Report potwierdza zgodność projektu z obowiązującymi regulacjami, standardami branżowymi i normami prawnymi. Dokument wzmacnia zaufanie inwestorów i regulatorów.

## Zawartość
- Lista obowiązujących regulacji i norm
- Status zgodności (zgodne / w trakcie / ryzyko)
- Procedury audytowe
- Identyfikacja obszarów niezgodności
- Plan działań naprawczych

## Czego nie zawiera
- Kodów źródłowych
- Strategii marketingowych
- Prognoz finansowych

## Objętość
- 2–4 strony
- 5–7 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zarząd
- Działy prawne i compliance
- Inwestorzy
