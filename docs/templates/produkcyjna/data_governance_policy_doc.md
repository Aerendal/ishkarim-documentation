# 📄 Data Governance Policy

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines organizational structure for data governance roles"
    conditions:
      - when: "project.has_data_governance === true"
        applies: true
      - when: "project.handles_minimal_data === true"
        applies: false
    sections:
      - from: "Project Charter §11 Key Stakeholders"
        to: "§3 Roles and Responsibilities"
        influence: "Stakeholders define data governance roles (data owners, stewards, custodians)"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines data protection policies that data governance enforces"
    conditions:
      - when: "project.has_sensitive_data === true"
        applies: true
    sections:
      - from: "Security Plan §5 Data Protection"
        to: "§5 Data Access Policies"
        influence: "Data protection requirements inform access control policies"
      - from: "Security Plan §3 Access Control Policies"
        to: "§5 Data Access Policies"
        influence: "Security access controls become data governance policies"

  - id: DATA-MANAGEMENT-PLAN-*
    type: requires
    reason: "Data Management Plan provides operational implementation of governance policies"
    conditions:
      - when: "project.has_data_management_plan === true"
        applies: true
    sections:
      - from: "Data Management Plan §2 Data Lifecycle"
        to: "§2 Data Classification"
        influence: "Data lifecycle stages inform data classification strategy"
```

### Impacts
```yaml
impacts:
  - id: TDD-*
    type: influences
    reason: "Data governance policies affect database and data architecture design"
    conditions:
      - when: "project.has_database === true"
        applies: true
    sections:
      - from: "§4 Data Quality Standards"
        to: "TDD §6 Database Architecture"
        influence: "Data quality standards drive database schema and validation design"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Data governance demonstrates compliance with data regulations"
    conditions:
      - when: "compliance.covers_data_privacy === true"
        applies: true
    sections:
      - from: "§5 Data Access Policies"
        to: "Compliance Report §2 Compliance Status"
        influence: "Data access policies demonstrate GDPR/HIPAA compliance"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "Data governance policies require staff training"
    conditions:
      - when: "project.has_staff === true"
        applies: true
    sections:
      - from: "§3 Roles and Responsibilities"
        to: "Training Materials §3 Data Governance Training"
        influence: "Data governance roles and policies define training curriculum"

  - id: API-DOCUMENTATION-*
    type: informs
    reason: "API data handling must comply with data governance policies"
    conditions:
      - when: "project.has_api === true"
        applies: true
    sections:
      - from: "§2 Data Classification"
        to: "API Documentation §5 Data Handling"
        influence: "Data classification determines API data exposure and protection"
```

### Related
```yaml
related:
  - id: ACCESSIBILITY-REPORT-*
    type: informs
    reason: "Data governance may include accessibility requirements for data presentation"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: informs
    reason: "Data governance failures are operational risks"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-DATA-GOVERNANCE-*.md"
    required: false
    purpose: "Track data governance policy updates and compliance actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DATA-GOVERNANCE-*.md"
    required: true
    purpose: "Store data quality audits, access logs, governance committee minutes"

  - type: DoD
    path: "satellites/dod/DOD-DATA-GOVERNANCE-*.md"
    required: true
    purpose: "Define completion criteria: policies documented, roles assigned, audits established"
```

## Cel biznesowy / techniczny
Data Governance Policy określa zasady zarządzania danymi w organizacji. Dokument zapewnia spójność, jakość i bezpieczeństwo danych.

## Zawartość
- Definicje i klasyfikacja danych
- Role i odpowiedzialności w zarządzaniu danymi
- Standardy jakości danych
- Polityki dostępu do danych
- Procedury audytowe
- Plan poprawy jakości danych

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych opisów technicznych
- Strategii marketingowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zarząd
- Administratorzy danych
- Project managerowie
