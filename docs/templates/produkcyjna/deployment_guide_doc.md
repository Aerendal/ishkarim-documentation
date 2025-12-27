# 📄 Deployment Guide

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: TDD-*
    type: requires
    reason: "TDD defines technical architecture and infrastructure requirements for deployment"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "TDD §3 System Architecture"
        to: "§2 Environment Requirements"
        influence: "System architecture defines infrastructure and deployment requirements"
      - from: "TDD §6 Database Architecture"
        to: "§2 Installation Steps"
        influence: "Database design determines database deployment procedures"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "High-Level Architecture provides deployment context and component structure"
    conditions:
      - when: "project.has_architecture_doc === true"
        applies: true
    sections:
      - from: "High-Level Architecture §3 Key Components"
        to: "§2 Installation Steps"
        influence: "Component structure defines deployment sequence"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines security configurations needed during deployment"
    conditions:
      - when: "project.has_security_requirements === true"
        applies: true
    sections:
      - from: "Security Plan §3 Access Control Policies"
        to: "§3 Configuration Procedures"
        influence: "Security policies define deployment security configuration"
      - from: "Security Plan §4 Network Security"
        to: "§2 Environment Requirements"
        influence: "Network security requirements define deployment network configuration"
```

### Impacts
```yaml
impacts:
  - id: ADMINISTRATOR-GUIDE-*
    type: influences
    reason: "Deployment procedures provide foundation for ongoing administration"
    conditions:
      - when: "project.has_admin_team === true"
        applies: true
    sections:
      - from: "§2 Installation Steps"
        to: "Administrator Guide §2 Configuration"
        influence: "Deployment configuration becomes administrative baseline"

  - id: RUNBOOK-*
    type: influences
    reason: "Deployment procedures inform operational runbook"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§4 Startup Procedures"
        to: "Runbook §2 System Startup"
        influence: "Deployment startup procedures become operational runbook steps"
      - from: "§6 Rollback Procedures"
        to: "Runbook §6 Emergency Rollback"
        influence: "Deployment rollback procedures inform emergency recovery"

  - id: CHANGE-LOG-*
    type: informs
    reason: "Deployment changes documented in changelog"
    conditions:
      - when: "deployment.introduces_changes === true"
        applies: true
    sections:
      - from: "§3 Configuration Procedures"
        to: "Change Log §4 Deployment Changes"
        influence: "Configuration changes become changelog entries"

  - id: CONFIGURATION-MANAGEMENT-PLAN-*
    type: influences
    reason: "Deployment procedures inform configuration management"
    conditions:
      - when: "project.has_config_mgmt === true"
        applies: true
    sections:
      - from: "§3 Configuration Procedures"
        to: "Configuration Management Plan §2 Configuration Items"
        influence: "Deployment configurations define what gets managed"
```

### Related
```yaml
related:
  - id: MIGRATION-PLAN-*
    type: informs
    reason: "Migration plan may reference deployment procedures"

  - id: RELEASE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Release management incorporates deployment procedures"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-DEPLOYMENT-*.md"
    required: false
    purpose: "Track deployment tasks and environment setup activities"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DEPLOYMENT-*.md"
    required: true
    purpose: "Store deployment logs, configuration files, environment verification results"

  - type: DoR
    path: "satellites/dor/DOR-DEPLOYMENT-*.md"
    required: true
    purpose: "Define prerequisites: environment prepared, approvals obtained, rollback tested"

  - type: DoD
    path: "satellites/dod/DOD-DEPLOYMENT-*.md"
    required: true
    purpose: "Define completion criteria: deployment successful, smoke tests passed, rollback verified"
```

## Cel biznesowy / techniczny
Deployment Guide zawiera instrukcje dotyczące wdrożenia systemu w środowisku produkcyjnym. Ułatwia zespołom technicznym szybkie i poprawne uruchomienie systemu.

## Zawartość
- Wymagania środowiskowe (OS, serwery, bazy danych)
- Kroki instalacji
- Procedury konfiguracji
- Instrukcje uruchomienia
- Checklisty wdrożeniowe
- Procedury rollbacku w razie awarii

## Czego nie zawiera
- Strategii biznesowych
- Treści marketingowych
- Ogólnych wizji

## Objętość
- 3–5 stron
- 8–10 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- DevOps
- Administratorzy systemów
- Zespół developerski
