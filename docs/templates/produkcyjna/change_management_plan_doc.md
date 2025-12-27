# 📄 Change Management Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter defines governance structure and stakeholders for change control"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
      - when: "project.type === 'informal'"
        applies: false
    sections:
      - from: "Project Charter §11 Key Stakeholders"
        to: "§4 Roles and Responsibilities"
        influence: "Stakeholders define change control board membership"
      - from: "Project Charter §13 Project Scope"
        to: "§2 Change Evaluation Criteria"
        influence: "Project scope defines baseline for evaluating change requests"

  - id: BRD-*
    type: requires
    reason: "BRD defines baseline requirements against which changes are evaluated"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "BRD §4 Scope & Boundaries"
        to: "§2 Change Evaluation Criteria"
        influence: "Scope boundaries determine what constitutes a change vs baseline"

  - id: TIMELINE-*
    type: influences
    reason: "Timeline provides schedule baseline for impact assessment"
    conditions:
      - when: "project.has_timeline === true"
        applies: true
    sections:
      - from: "Timeline §2 Project Milestones"
        to: "§2 Change Evaluation Criteria"
        influence: "Timeline baseline helps assess schedule impact of changes"
```

### Impacts
```yaml
impacts:
  - id: CONFIGURATION-MANAGEMENT-PLAN-*
    type: influences
    reason: "Configuration Management tracks approved changes from Change Management"
    conditions:
      - when: "project.has_configuration_management === true"
        applies: true
    sections:
      - from: "§5 Change Documentation and Tracking"
        to: "Configuration Management Plan §3 Change Tracking"
        influence: "Change approval process feeds configuration management"

  - id: CHANGE-LOG-*
    type: influences
    reason: "Approved changes documented in changelog"
    conditions:
      - when: "project.has_releases === true"
        applies: true
    sections:
      - from: "§5 Change Documentation and Tracking"
        to: "Change Log §3 New Features"
        influence: "Approved changes become changelog entries"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Change requests may introduce new risks"
    conditions:
      - when: "change.has_risk_impact === true"
        applies: true
    sections:
      - from: "§2 Change Evaluation Criteria"
        to: "Risk Overview §3 Risk Inventory"
        influence: "Change evaluation identifies new risks requiring assessment"
```

### Related
```yaml
related:
  - id: RELEASE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Release planning incorporates approved changes"

  - id: INTEGRATION-PLAN-*
    type: informs
    reason: "Integration changes require change management approval"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CHANGE-MGMT-*.md"
    required: false
    purpose: "Track pending change requests and approval workflows"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CHANGE-MGMT-*.md"
    required: true
    purpose: "Store change request forms, approval records, impact assessments"

  - type: DoD
    path: "satellites/dod/DOD-CHANGE-MGMT-*.md"
    required: true
    purpose: "Define completion criteria: process documented, stakeholders trained, tools established"
```

## Cel biznesowy / techniczny
Change Management Plan opisuje proces wprowadzania zmian w projekcie. Zapewnia kontrolę nad zakresem i minimalizuje ryzyko chaosu projektowego.

## Zawartość
- Procedury zgłaszania zmian
- Kryteria oceny zmian
- Proces zatwierdzania zmian
- Role i odpowiedzialności (komitet zmian, project manager)
- Dokumentowanie i śledzenie zmian
- Komunikacja zmian w zespole

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych backlogów sprintów
- Treści marketingowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Project managerowie
- Zarząd
- Zespół developerski
