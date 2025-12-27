# 📄 Onboarding Guide

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines project context for new team members"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §11 Key Stakeholders"
        to: "§2 Team Structure"
        influence: "Stakeholder map defines team organizational structure"

  - id: USER-GUIDE-*
    type: requires
    reason: "User Guide provides system usage reference for new users"
    conditions:
      - when: "onboarding.audience === 'end_users'"
        applies: true
    sections:
      - from: "User Guide §2 Getting Started"
        to: "§3 Initial Setup"
        influence: "User guide getting started becomes onboarding first steps"

  - id: ADMINISTRATOR-GUIDE-*
    type: requires
    reason: "Admin Guide provides technical setup for new administrators"
    conditions:
      - when: "onboarding.audience === 'administrators'"
        applies: true
    sections:
      - from: "Administrator Guide §2 Configuration"
        to: "§4 Access Procedures"
        influence: "Admin configuration procedures guide new admin onboarding"

  - id: OPERATIONAL-MANUAL-*
    type: requires
    reason: "Operational Manual provides operations procedures for new team members"
    conditions:
      - when: "onboarding.audience === 'operations_team'"
        applies: true
    sections:
      - from: "Operational Manual §3 Daily Operations"
        to: "§5 Operational Processes"
        influence: "Daily operations become onboarding workflow training"

  - id: TRAINING-MATERIALS-*
    type: requires
    reason: "Training materials provide learning content for onboarding"
    conditions:
      - when: "project.has_training === true"
        applies: true
    sections:
      - from: "Training Materials §2 Tutorials"
        to: "§4 Training Schedule"
        influence: "Training modules become onboarding curriculum"
```

### Impacts
```yaml
impacts:
  - id: KNOWLEDGE-TRANSFER-PLAN-*
    type: informs
    reason: "Onboarding is form of knowledge transfer to new team members"
    conditions:
      - when: "project.has_knowledge_transfer === true"
        applies: true
    sections:
      - from: "§3 Initial Setup"
        to: "Knowledge Transfer Plan §4 Transfer Methods"
        influence: "Onboarding process informs knowledge transfer approach"
```

### Related
```yaml
related:
  - id: UAT-PLAN-*
    type: informs
    reason: "UAT participants may need onboarding"

  - id: SERVICE-CATALOG-*
    type: informs
    reason: "Service catalog helps new team members understand available services"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ONBOARDING-*.md"
    required: false
    purpose: "Track onboarding tasks for new team members"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ONBOARDING-*.md"
    required: false
    purpose: "Store onboarding checklists, completion records, new hire feedback"

  - type: DoD
    path: "satellites/dod/DOD-ONBOARDING-*.md"
    required: true
    purpose: "Define completion criteria: all access granted, training complete, team member productive"
```

## Cel biznesowy / techniczny
Onboarding Guide wspiera nowych członków zespołu w szybkim wdrożeniu się do projektu. Dokument minimalizuje czas potrzebny na adaptację i zapewnia spójność wiedzy.

## Zawartość
- Wprowadzenie do projektu
- Struktura organizacyjna zespołu
- Główne narzędzia i systemy
- Procedury dostępu do środowisk
- Podstawowe procesy projektowe
- Lista kontaktów i źródeł wiedzy

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych analiz technicznych
- Strategii biznesowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Nowi członkowie zespołu
- Project managerowie
- HR / dział rekrutacji
