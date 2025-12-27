# 📄 Resource Requirements

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter defines project scope and constraints that drive resource needs"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §12 Objectives"
        to: "§2 Team Requirements"
        influence: "Project objectives define team size and skill requirements"

  - id: BRD-*
    type: requires
    reason: "BRD scope defines resource effort required"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "BRD §5 Core Requirements"
        to: "§2 Team Requirements"
        influence: "Business requirements scope determines resource capacity needed"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "Architecture complexity affects required team skills"
    conditions:
      - when: "project.has_architecture === true"
        applies: true
    sections:
      - from: "High-Level Architecture §3 System Components"
        to: "§2 Team Requirements (Skills)"
        influence: "Architecture technologies define required technical skills"

  - id: TDD-*
    type: influences
    reason: "Technical design defines technology stack and infrastructure needs"
    conditions:
      - when: "project.has_tdd === true"
        applies: true
    sections:
      - from: "TDD §3 Technology Stack"
        to: "§3 Technology & Tools"
        influence: "Technology choices define tool and license requirements"
      - from: "TDD §8 Infrastructure Requirements"
        to: "§4 Infrastructure"
        influence: "Infrastructure design defines hardware and hosting needs"
```

### Impacts
```yaml
impacts:
  - id: TIMELINE-*
    type: blocks
    reason: "Resource availability constrains timeline feasibility"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§2 Team Requirements"
        to: "Timeline §4 Phase Duration"
        influence: "Team capacity determines realistic phase durations"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: influences
    reason: "External resource needs drive vendor selection"
    conditions:
      - when: "resources.requires_external_vendors === true"
        applies: true
    sections:
      - from: "§4 Infrastructure (External)"
        to: "Vendor Management Plan §2 Vendor List"
        influence: "External infrastructure needs identify required vendors"

  - id: ONBOARDING-GUIDE-*
    type: informs
    reason: "Resource plan defines roles that need onboarding"
    conditions:
      - when: "project.has_onboarding === true"
        applies: true
    sections:
      - from: "§2 Team Requirements"
        to: "Onboarding Guide §2 Team Structure"
        influence: "Defined roles become onboarding audience"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Resource skill gaps drive training needs"
    conditions:
      - when: "resources.has_skill_gaps === true"
        applies: true
    sections:
      - from: "§2 Team Requirements (Skills)"
        to: "Training Materials §2 Training Curriculum"
        influence: "Required skills define training curriculum"

  - id: DEPLOYMENT-GUIDE-*
    type: informs
    reason: "Infrastructure requirements inform deployment environment"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Infrastructure"
        to: "Deployment Guide §2 Infrastructure Setup"
        influence: "Infrastructure requirements define deployment environment specs"
```

### Related
```yaml
related:
  - id: OPERATIONAL-MANUAL-*
    type: informs
    reason: "Operations team resources defined in resource requirements"

  - id: QA-PLAN-*
    type: informs
    reason: "QA resource needs defined in resource requirements"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RESOURCE-REQUIREMENTS-*.md"
    required: true
    purpose: "Track resource procurement, hiring, tool purchases, infrastructure provisioning"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RESOURCE-REQUIREMENTS-*.md"
    required: true
    purpose: "Store budget approvals, hiring records, license purchases, infrastructure receipts"

  - type: DoD
    path: "satellites/dod/DOD-RESOURCE-REQUIREMENTS-*.md"
    required: true
    purpose: "Define completion criteria: all resources identified, budget approved, procurement complete"
```

## Cel biznesowy / techniczny
Resource Requirements określa zasoby potrzebne do realizacji projektu – ludzi, technologie, narzędzia i budżet wykonawczy. Dokument pozwala na realistyczne zaplanowanie kosztów i zespołu.

## Zawartość
- Zespół projektowy i wymagane role
- Technologie i narzędzia
- Sprzęt i infrastruktura
- Szacowany budżet operacyjny
- Wymagania licencyjne

## Czego nie zawiera
- Strategii marketingowych
- Planów sprzedaży
- Backlogów sprintowych

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Project managerowie
- Zarząd
- Zespół developerski
