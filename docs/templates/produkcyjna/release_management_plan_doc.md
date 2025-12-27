# 📄 Release Management Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: TIMELINE-*
    type: requires
    reason: "Timeline provides schedule baseline for release planning"
    conditions:
      - when: "project.has_timeline === true"
        applies: true
    sections:
      - from: "Timeline §2 Milestones"
        to: "§2 Release Schedule"
        influence: "Project milestones define release dates"

  - id: TEST-SUMMARY-REPORT-*
    type: requires
    reason: "Test results determine release readiness"
    conditions:
      - when: "release.requires_testing === true"
        applies: true
    sections:
      - from: "Test Summary Report §6 Release Recommendation"
        to: "§4 Go/No-Go Decision"
        influence: "Test summary recommendation drives release decision"

  - id: DEPLOYMENT-GUIDE-*
    type: requires
    reason: "Deployment procedures are part of release process"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Deployment Guide §6 Rollback Procedures"
        to: "§6 Rollback Procedures"
        influence: "Deployment rollback procedures inform release rollback"
```

### Impacts
```yaml
impacts:
  - id: CHANGE-LOG-*
    type: blocks
    reason: "Release Management Plan drives changelog releases"
    conditions:
      - when: "project.has_releases === true"
        applies: true
    sections:
      - from: "§2 Release Schedule"
        to: "Change Log §2 Release Date"
        influence: "Release schedule determines changelog entry dates"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "New releases may require training updates"
    conditions:
      - when: "release.has_new_features === true"
        applies: true
    sections:
      - from: "§5 Release Communication"
        to: "Training Materials §2 Feature Training"
        influence: "Release communications inform training material updates"
```

### Related
```yaml
related:
  - id: CONFIGURATION-MANAGEMENT-PLAN-*
    type: informs
    reason: "Release management coordinates with configuration management"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RELEASE-*.md"
    required: true
    purpose: "Track release tasks, approvals, communications"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RELEASE-*.md"
    required: true
    purpose: "Store release notes, approval records, deployment logs, rollback validations"

  - type: DoR
    path: "satellites/dor/DOR-RELEASE-*.md"
    required: true
    purpose: "Define prerequisites: testing complete, approvals obtained, rollback tested"

  - type: DoD
    path: "satellites/dod/DOD-RELEASE-*.md"
    required: true
    purpose: "Define completion criteria: release deployed, verified, documented, communicated"
```

## Cel biznesowy / techniczny
Release Management Plan definiuje proces planowania, harmonogramowania i wdrażania nowych wersji systemu. Dokument ten zapewnia spójność i przewidywalność w cyklu wydawniczym.

## Zawartość
- Harmonogram wydań
- Role i odpowiedzialności
- Kryteria wejścia i wyjścia dla wydań
- Procedury przygotowania wersji
- Plan komunikacji dotyczący wydań
- Procedury rollbacku

## Czego nie zawiera
- Strategii marketingowych
- Szczegółowych implementacji kodu
- Analiz finansowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- DevOps
- QA / testerzy
- Project managerowie
