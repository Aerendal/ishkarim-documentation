# 📄 Data Management Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: DATA-GOVERNANCE-POLICY-*
    type: requires
    reason: "Data Governance Policy defines strategic data management policies"
    conditions:
      - when: "project.has_data_governance === true"
        applies: true
      - when: "project.data_complexity === 'minimal'"
        applies: false
    sections:
      - from: "Data Governance Policy §2 Data Classification"
        to: "§2 Data Types"
        influence: "Data classification defines types and categories in management plan"
      - from: "Data Governance Policy §5 Data Access Policies"
        to: "§4 Data Access Policy"
        influence: "Governance access policies become operational data access procedures"

  - id: TDD-*
    type: influences
    reason: "TDD defines database architecture and data structures"
    conditions:
      - when: "project.has_database === true"
        applies: true
    sections:
      - from: "TDD §6 Database Architecture"
        to: "§2 Data Types"
        influence: "Database schema defines data structures to manage"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines data protection requirements"
    conditions:
      - when: "project.has_sensitive_data === true"
        applies: true
    sections:
      - from: "Security Plan §5 Data Protection"
        to: "§4 Data Access Policy"
        influence: "Data protection requirements inform access controls"
```

### Impacts
```yaml
impacts:
  - id: ADMINISTRATOR-GUIDE-*
    type: influences
    reason: "Administrators implement data management procedures"
    conditions:
      - when: "project.has_admin_team === true"
        applies: true
    sections:
      - from: "§5 Backup and Retention Procedures"
        to: "Administrator Guide §4 Backup Procedures"
        influence: "Data backup procedures become administrative tasks"

  - id: DRP-*
    type: influences
    reason: "Data management backup procedures support disaster recovery"
    conditions:
      - when: "project.requires_drp === true"
        applies: true
    sections:
      - from: "§5 Backup and Retention Procedures"
        to: "DRP §4 Data Recovery Procedures"
        influence: "Backup procedures define data recovery capabilities"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Data management demonstrates regulatory compliance"
    conditions:
      - when: "compliance.covers_data_regulations === true"
        applies: true
    sections:
      - from: "§6 Data Archival and Deletion"
        to: "Compliance Report §2 Compliance Status"
        influence: "Data retention and deletion procedures demonstrate GDPR/HIPAA compliance"
```

### Related
```yaml
related:
  - id: API-DOCUMENTATION-*
    type: informs
    reason: "API data handling aligns with data management plan"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "Data storage and access monitoring requirements"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-DATA-MGMT-*.md"
    required: false
    purpose: "Track data management tasks and policy updates"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DATA-MGMT-*.md"
    required: true
    purpose: "Store backup logs, retention schedules, access audit trails"

  - type: DoD
    path: "satellites/dod/DOD-DATA-MGMT-*.md"
    required: true
    purpose: "Define completion criteria: procedures documented, backups tested, access controls verified"
```

## Cel biznesowy / techniczny
Data Management Plan (DMP) definiuje sposób gromadzenia, przechowywania, udostępniania i archiwizacji danych w projekcie. Zapewnia zgodność z regulacjami oraz efektywne wykorzystanie danych.

## Zawartość
- Typy danych w projekcie
- Źródła danych i sposób pozyskania
- Standardy i formaty przechowywania
- Polityka dostępu do danych
- Procedury backupu i retencji
- Plan archiwizacji i usuwania danych

## Czego nie zawiera
- Kodów źródłowych
- Strategii marketingowych
- Analiz finansowych

## Objętość
- 3–5 stron
- 8–10 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zespół developerski
- Administratorzy danych
- Project managerowie
