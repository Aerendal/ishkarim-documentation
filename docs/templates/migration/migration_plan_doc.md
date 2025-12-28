# 📄 Migration Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: AS-IS-ARCHITECTURE-*
    type: requires
    reason: "AS-IS Architecture defines current system state that needs migration"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "AS-IS Architecture §2 Current System Components"
        to: "§2 Migration Scope"
        influence: "Current system components determine what needs to be migrated"
      - from: "AS-IS Architecture §3 Data Architecture"
        to: "§3 Data Migration Strategy"
        influence: "Current data structures inform migration complexity"

  - id: TO-BE-ARCHITECTURE-*
    type: requires
    reason: "TO-BE Architecture defines target system state for migration"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "TO-BE Architecture §2 Target System Components"
        to: "§2 Migration Scope"
        influence: "Target system defines migration destination and requirements"
      - from: "TO-BE Architecture §4 Technology Stack"
        to: "§4 Migration Phases"
        influence: "New technology stack determines migration approach"

  - id: PROBLEMS-ERRORS-ANALYSIS-*
    type: requires
    reason: "Problems & Errors Analysis identifies reasons and justification for migration"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Problems & Errors Analysis §2 Critical Issues"
        to: "§1 Migration Goals"
        influence: "Current problems define migration objectives"

  - id: REFACTORING-PROCESS-*
    type: requires
    reason: "Refactoring Process defines how to transform code/system during migration"
    conditions:
      - when: "migration.includes_code === true"
        applies: true
    sections:
      - from: "Refactoring Process §3 Transformation Steps"
        to: "§4 Migration Phases"
        influence: "Refactoring steps guide migration implementation"

  - id: TDD-*
    type: requires
    reason: "TDD defines technical architecture of target system"
    conditions:
      - when: "migration.includes_technical_components === true"
        applies: true
    sections:
      - from: "TDD §6 Database Architecture"
        to: "§3 Data Migration Strategy"
        influence: "Target database design determines data migration approach"
      - from: "TDD §4 Infrastructure Requirements"
        to: "§5 Infrastructure Migration"
        influence: "Infrastructure requirements define migration infrastructure needs"

  - id: RISK-OVERVIEW-*
    type: requires
    reason: "Risk Overview identifies migration-specific risks requiring mitigation"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Risk Overview §2 Migration Risks"
        to: "§6 Risk Mitigation"
        influence: "Identified risks inform rollback and contingency planning"
```

### Impacts
```yaml
impacts:
  - id: IMPLEMENTATION-PLAN-*
    type: influences
    reason: "Migration Plan drives concrete implementation steps"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Migration Phases"
        to: "Implementation Plan §2 Implementation Steps"
        influence: "Migration phases define specific implementation tasks"
      - from: "§7 Timeline"
        to: "Implementation Plan §3 Schedule"
        influence: "Migration timeline informs implementation schedule"

  - id: INTEGRATION-PLAN-*
    type: influences
    reason: "Migration Plan defines how to integrate new system components"
    conditions:
      - when: "migration.affects_integrations === true"
        applies: true
    sections:
      - from: "§4 Migration Phases"
        to: "Integration Plan §2 Integration Strategy"
        influence: "Migration phases determine integration approach"

  - id: TEST-PLAN-*
    type: influences
    reason: "Migration requires comprehensive testing to validate success"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Migration Testing"
        to: "Test Plan §3 Migration Test Scenarios"
        influence: "Migration testing procedures define test scenarios"
      - from: "§3 Data Migration Strategy"
        to: "Test Plan §4 Data Validation Tests"
        influence: "Data migration strategy requires validation testing"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Migration Plan informs deployment procedures for new system"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Migration Phases"
        to: "Deployment Guide §2 Deployment Steps"
        influence: "Migration phases define deployment sequence"

  - id: ROLLBACK-PLAN-*
    type: influences
    reason: "Migration Plan requires comprehensive rollback procedures"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§6 Rollback Strategy"
        to: "Rollback Plan §2 Rollback Procedures"
        influence: "Migration rollback strategy defines detailed rollback steps"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "Migration to new system requires team training"
    conditions:
      - when: "migration.affects_users === true"
        applies: true
    sections:
      - from: "§2 Migration Scope"
        to: "Training Materials §2 System Changes"
        influence: "Migration changes define training needs"
      - from: "§8 New System Features"
        to: "Training Materials §3 Feature Training"
        influence: "New features require user training"

  - id: SPRINT-CORE-*
    type: influences
    reason: "Migration Plan defines work for migration sprints"
    conditions:
      - when: "migration.uses_sprints === true"
        applies: true
    sections:
      - from: "§4 Migration Phases"
        to: "Sprint Core §2 Sprint Goals"
        influence: "Migration phases break down into sprint objectives"

  - id: SPRINT-HARDENING-*
    type: influences
    reason: "Migration requires hardening sprints for stabilization"
    conditions:
      - when: "migration.uses_sprints === true"
        applies: true
    sections:
      - from: "§5 Migration Testing"
        to: "Sprint Hardening §2 Stabilization Activities"
        influence: "Migration testing defines hardening requirements"
```

### Related
```yaml
related:
  - id: MODULE-ANALYSIS-ROADMAP-*
    type: informs
    reason: "Module Analysis & Roadmap shows module dependencies affecting migration order"

  - id: INTEGRATION-POINTS-ANALYSIS-*
    type: informs
    reason: "Integration Points Analysis identifies external integrations requiring migration"

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "Data Management Plan defines data handling during and after migration"

  - id: SECURITY-PLAN-*
    type: informs
    reason: "Security Plan ensures secure migration of sensitive data and credentials"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-MIGRATION-*.md"
    required: true
    purpose: "Track migration tasks, data validation, cutover activities, rollback verification"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-MIGRATION-*.md"
    required: true
    purpose: "Store migration test results, data validation reports, before/after comparisons"

  - type: Approval
    path: "satellites/approval/APPROVAL-MIGRATION-*.md"
    required: true
    purpose: "Document stakeholder approvals for migration go/no-go decisions"

  - type: DoR
    path: "satellites/dor/DOR-MIGRATION-*.md"
    required: true
    purpose: "Define prerequisites: backups complete, testing done, rollback tested, stakeholders notified"

  - type: DoD
    path: "satellites/dod/DOD-MIGRATION-*.md"
    required: true
    purpose: "Define completion criteria: all data migrated, validated, old system decommissioned, monitoring active"
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
