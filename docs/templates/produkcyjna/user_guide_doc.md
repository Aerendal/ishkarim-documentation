# 📄 User Guide

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines features and user stories that user guide documents"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§4 Feature Documentation"
        influence: "Functional requirements define features to document in user guide"
      - from: "PRD §4 User Stories & Personas"
        to: "§2 User Personas"
        influence: "User personas inform user guide audience and tone"

  - id: API-DOCUMENTATION-*
    type: influences
    reason: "For developer-facing products, API docs inform user guide"
    conditions:
      - when: "project.users === 'developers'"
        applies: true
    sections:
      - from: "API Documentation §3 Request/Response Examples"
        to: "§3 Code Examples"
        influence: "API examples become user guide code snippets"

  - id: ACCESSIBILITY-REPORT-*
    type: influences
    reason: "Accessibility features require documentation in user guide"
    conditions:
      - when: "project.has_accessibility_features === true"
        applies: true
    sections:
      - from: "Accessibility Report §5 Compliance Level"
        to: "§4 Feature Documentation"
        influence: "Accessibility features documented for user guidance"
```

### Impacts
```yaml
impacts:
  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "User Guide provides foundation for training materials"
    conditions:
      - when: "project.requires_training === true"
        applies: true
    sections:
      - from: "§3 Step-by-Step Instructions"
        to: "Training Materials §3 Tutorials"
        influence: "User guide instructions become training tutorials"
      - from: "§6 FAQ"
        to: "Training Materials §4 Common Questions"
        influence: "FAQ becomes training reference material"

  - id: UAT-PLAN-*
    type: informs
    reason: "User Guide helps UAT participants understand functionality"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "§4 Feature Documentation"
        to: "UAT Plan §5 UAT Scenarios"
        influence: "Feature documentation informs UAT scenario design"

  - id: ONBOARDING-GUIDE-*
    type: influences
    reason: "User Guide is reference material for new user onboarding"
    conditions:
      - when: "project.has_end_users === true"
        applies: true
    sections:
      - from: "§2 Getting Started"
        to: "Onboarding Guide §3 Initial Setup"
        influence: "Getting started guide becomes onboarding first steps"

  - id: CHANGE-LOG-*
    type: informs
    reason: "New features in changelog require user guide updates"
    conditions:
      - when: "release.has_new_features === true"
        applies: true
    sections:
      - from: "§4 Feature Documentation"
        to: "Change Log §3 New Features"
        influence: "User guide updates track with changelog new features"
```

### Related
```yaml
related:
  - id: ADMINISTRATOR-GUIDE-*
    type: informs
    reason: "Admin guide complements user guide for technical users"

  - id: SERVICE-CATALOG-*
    type: informs
    reason: "Service catalog may reference user guide for service usage"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-USER-GUIDE-*.md"
    required: false
    purpose: "Track user guide content creation and updates for new features"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-USER-GUIDE-*.md"
    required: false
    purpose: "Store screenshots, user feedback, usability testing results"

  - type: DoD
    path: "satellites/dod/DOD-USER-GUIDE-*.md"
    required: true
    purpose: "Define completion criteria: all features documented, screenshots current, FAQ updated, reviewed by users"
```

## Cel biznesowy / techniczny
User Guide to przewodnik dla użytkowników końcowych systemu. Dokument zapewnia instrukcje dotyczące korzystania z funkcji i rozwiązywania podstawowych problemów.

## Zawartość
- Wprowadzenie do systemu
- Instrukcje krok po kroku
- Zrzuty ekranu
- Opisy funkcji
- Najczęstsze problemy i ich rozwiązania
- FAQ

## Czego nie zawiera
- Szczegółowych kodów źródłowych
- Analiz technicznych
- Strategii biznesowych

## Objętość
- 5–15 stron
- 10–20 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Użytkownicy końcowi
- Zespół wsparcia IT
