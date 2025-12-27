# 📄 Change Log / Release Notes

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: RELEASE-MANAGEMENT-PLAN-*
    type: requires
    reason: "Release Management Plan defines versioning strategy and release process"
    conditions:
      - when: "project.has_releases === true"
        applies: true
      - when: "project.type === 'one-time-delivery'"
        applies: false
    sections:
      - from: "Release Management Plan §2 Versioning Strategy"
        to: "§1 Version Number"
        influence: "Versioning strategy defines how versions are numbered in changelog"
      - from: "Release Management Plan §3 Release Schedule"
        to: "§2 Release Date"
        influence: "Release schedule determines changelog entry dates"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Deployment changes documented in changelog"
    conditions:
      - when: "release.has_deployment_changes === true"
        applies: true
    sections:
      - from: "Deployment Guide §2 Installation Steps"
        to: "§4 Improvements"
        influence: "Deployment changes become changelog entries"

  - id: TEST-SUMMARY-REPORT-*
    type: influences
    reason: "Test results inform what bugs were fixed in release"
    conditions:
      - when: "release.includes_bug_fixes === true"
        applies: true
    sections:
      - from: "Test Summary Report §4 Defects Found"
        to: "§4 Bug Fixes"
        influence: "Fixed defects documented in changelog"
```

### Impacts
```yaml
impacts:
  - id: USER-GUIDE-*
    type: informs
    reason: "User Guide updated with new features from changelog"
    conditions:
      - when: "release.has_new_features === true"
        applies: true
    sections:
      - from: "§3 New Features"
        to: "User Guide §3 Feature Documentation"
        influence: "New features require user guide updates"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "Training materials updated based on changes"
    conditions:
      - when: "release.requires_training === true"
        applies: true
    sections:
      - from: "§3 New Features"
        to: "Training Materials §3 New Features Training"
        influence: "New features require training content updates"

  - id: API-DOCUMENTATION-*
    type: informs
    reason: "API changes documented in changelog require API doc updates"
    conditions:
      - when: "release.has_api_changes === true"
        applies: true
    sections:
      - from: "§3 New Features"
        to: "API Documentation §2 Endpoints"
        influence: "API changes trigger documentation updates"
```

### Related
```yaml
related:
  - id: CONFIGURATION-MANAGEMENT-PLAN-*
    type: informs
    reason: "Configuration changes tracked in changelog"

  - id: MIGRATION-PLAN-*
    type: informs
    reason: "Breaking changes in changelog may require migration plan"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CHANGELOG-*.md"
    required: false
    purpose: "Track changelog entries to be written for upcoming releases"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CHANGELOG-*.md"
    required: false
    purpose: "Store git commit logs, issue tracker exports, feature completion records"

  - type: DoD
    path: "satellites/dod/DOD-CHANGELOG-*.md"
    required: false
    purpose: "Define completion criteria: all changes documented, user impact described, reviewed"
```

## Cel biznesowy / techniczny
Change Log dokumentuje historię zmian w projekcie. Release Notes służą do komunikowania nowości, poprawek i ulepszeń użytkownikom końcowym oraz zespołowi.

## Zawartość
- Wersja systemu / produktu
- Data wydania
- Lista nowych funkcji
- Lista poprawek i usprawnień
- Znane błędy
- Krótki opis wpływu zmian na użytkowników

## Czego nie zawiera
- Planów inwestorskich
- Strategii sprzedażowych
- Zbyt ogólnych opisów bez szczegółów zmian

## Objętość
- 1–2 strony na wersję
- 5–8 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Zespół developerski
- Użytkownicy końcowi
- QA / testerzy
