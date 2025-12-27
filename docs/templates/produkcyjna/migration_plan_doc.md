# 📄 Migration Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: DATA-MANAGEMENT-PLAN-*
    type: requires
    reason: "Data Management Plan defines data structures and backup procedures for migration"
    conditions:
      - when: "migration.includes_data === true"
        applies: true
    sections:
      - from: "Data Management Plan §2 Data Types"
        to: "§2 Migration Scope"
        influence: "Data types and structures define what needs migration"
      - from: "Data Management Plan §5 Backup Procedures"
        to: "§4 Backup Procedures"
        influence: "Existing backup procedures inform migration backup strategy"

  - id: TDD-*
    type: requires
    reason: "TDD defines system architecture affecting migration approach"
    conditions:
      - when: "migration.includes_applications === true"
        applies: true
    sections:
      - from: "TDD §6 Database Architecture"
        to: "§2 Migration Scope"
        influence: "Database design determines data migration complexity"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Deployment procedures inform application migration"
    conditions:
      - when: "migration.includes_system_deployment === true"
        applies: true
    sections:
      - from: "Deployment Guide §2 Installation Steps"
        to: "§4 Migration Phases"
        influence: "Deployment procedures guide system migration steps"
```

### Impacts
```yaml
impacts:
  - id: TEST-PLAN-*
    type: influences
    reason: "Migration requires testing to validate data integrity"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Migration Testing"
        to: "Test Plan §3 Migration Test Scenarios"
        influence: "Migration testing procedures define test scenarios"

  - id: RUNBOOK-*
    type: informs
    reason: "Migration procedures may become operational procedures"
    conditions:
      - when: "migration.ongoing === true"
        applies: true
    sections:
      - from: "§6 Rollback Plan"
        to: "Runbook §6 Emergency Procedures"
        influence: "Migration rollback procedures inform operational emergency steps"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Migration to new system may require user training"
    conditions:
      - when: "migration.affects_users === true"
        applies: true
    sections:
      - from: "§2 Migration Scope"
        to: "Training Materials §2 System Changes"
        influence: "Migration changes define training needs"
```

### Related
```yaml
related:
  - id: CHANGE-LOG-*
    type: informs
    reason: "Migration milestones documented in changelog"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Migration risks identified and assessed"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-MIGRATION-*.md"
    required: true
    purpose: "Track migration tasks, data validation, cutover activities"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-MIGRATION-*.md"
    required: true
    purpose: "Store migration test results, data validation reports, rollback verification"

  - type: DoR
    path: "satellites/dor/DOR-MIGRATION-*.md"
    required: true
    purpose: "Define prerequisites: backups complete, testing done, rollback tested, stakeholders notified"

  - type: DoD
    path: "satellites/dod/DOD-MIGRATION-*.md"
    required: true
    purpose: "Define completion criteria: all data migrated, validated, old system decommissioned"
```

## Cel biznesowy / techniczny
Migration Plan opisuje proces przenoszenia danych, aplikacji lub systemów do nowego środowiska. Dokument minimalizuje ryzyka związane z utratą danych i przestojami.

## Zawartość
- Zakres migracji (systemy, dane)
- Analiza ryzyk migracji
- Harmonogram i etapy
- Procedury backupu
- Testy migracyjne
- Plan rollbacku

## Czego nie zawiera
- Strategii biznesowych
- Kodów źródłowych
- Analiz rynkowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Administratorzy
- DevOps
- Project managerowie
