# 📄 Disaster Recovery Plan (DRP)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: TDD-*
    type: requires
    reason: "TDD defines system architecture and infrastructure to recover"
    conditions:
      - when: "project.has_technical_infrastructure === true"
        applies: true
      - when: "project.type === 'documentation-only'"
        applies: false
    sections:
      - from: "TDD §3 System Architecture"
        to: "§2 System Recovery Priorities"
        influence: "System architecture defines what components need disaster recovery"
      - from: "TDD §6 Database Architecture"
        to: "§4 Data Recovery Procedures"
        influence: "Database design determines recovery procedures and RPO/RTO targets"

  - id: DATA-MANAGEMENT-PLAN-*
    type: requires
    reason: "Data Management Plan defines backup procedures that enable disaster recovery"
    conditions:
      - when: "project.has_data === true"
        applies: true
    sections:
      - from: "Data Management Plan §5 Backup and Retention"
        to: "§4 Data Recovery Procedures"
        influence: "Backup procedures provide the foundation for disaster recovery"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: requires
    reason: "Risk assessment identifies disaster scenarios that DRP must address"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Operational Risk Assessment §3 Risk Inventory"
        to: "§2 Disaster Scenarios"
        influence: "Identified risks become disaster scenarios for recovery planning"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "Architecture defines system dependencies and recovery order"
    conditions:
      - when: "project.has_complex_architecture === true"
        applies: true
    sections:
      - from: "High-Level Architecture §4 Integration Points"
        to: "§2 System Recovery Priorities"
        influence: "Integration dependencies inform recovery sequencing"
```

### Impacts
```yaml
impacts:
  - id: BCP-*
    type: influences
    reason: "DRP provides technical recovery foundation for business continuity"
    conditions:
      - when: "project.has_bcp === true"
        applies: true
    sections:
      - from: "§4 Data Recovery Procedures"
        to: "BCP §4 Continuity Procedures"
        influence: "Technical recovery procedures support business continuity plans"
      - from: "§5 RTO/RPO Targets"
        to: "BCP §2 Critical Business Processes"
        influence: "Recovery time objectives inform business continuity planning"

  - id: RUNBOOK-*
    type: influences
    reason: "DRP procedures incorporated into operational runbook"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§4 Data Recovery Procedures"
        to: "Runbook §5 Disaster Recovery Procedures"
        influence: "DRP procedures become runbook disaster recovery steps"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "DRP procedures require training for IT and operations teams"
    conditions:
      - when: "drp.requires_training === true"
        applies: true
    sections:
      - from: "§6 DRP Testing Procedures"
        to: "Training Materials §3 Disaster Recovery Training"
        influence: "DRP testing becomes training exercises"
```

### Related
```yaml
related:
  - id: ADMINISTRATOR-GUIDE-*
    type: informs
    reason: "Administrators execute DRP procedures"

  - id: SLA-*
    type: informs
    reason: "SLA commitments must align with DRP RTO/RPO capabilities"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "Monitoring detects conditions that trigger DRP activation"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-DRP-*.md"
    required: false
    purpose: "Track DRP testing, updates, and improvement actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DRP-*.md"
    required: true
    purpose: "Store DRP test results, recovery time measurements, backup validation reports"

  - type: DoD
    path: "satellites/dod/DOD-DRP-*.md"
    required: true
    purpose: "Define completion criteria: DRP tested, RTO/RPO validated, team trained"
```

## Cel biznesowy / techniczny
Disaster Recovery Plan określa procedury odtwarzania systemu po awarii, katastrofie naturalnej lub cyberataku. Dokument gwarantuje ciągłość działania i minimalizację przestojów.

## Zawartość
- Scenariusze awarii i katastrof
- Priorytety odtwarzania systemów
- Role i odpowiedzialności w DRP
- Procedury backupu i przywracania danych
- Czas odtwarzania (RTO) i punkt odtworzenia danych (RPO)
- Procedury testowania DRP

## Czego nie zawiera
- Strategii marketingowych
- Szczegółowych implementacji kodu
- Ogólnych analiz biznesowych

## Objętość
- 3–6 stron
- 8–10 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Zespół IT
- Administratorzy systemów
- Zarząd
