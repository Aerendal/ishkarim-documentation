# 📄 System Context Diagram

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: BRD-*
    type: requires
    reason: "BRD defines business context and stakeholders that system serves"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "BRD §3 Stakeholders"
        to: "§2 System Actors"
        influence: "Business stakeholders become system context actors"

  - id: PRD-*
    type: influences
    reason: "PRD defines user interactions and external integrations"
    conditions:
      - when: "project.has_prd === true"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§3 System Interactions"
        influence: "Functional requirements define system interactions"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "High-level architecture defines system boundaries and external systems"
    conditions:
      - when: "project.has_architecture === true"
        applies: true
    sections:
      - from: "High-Level Architecture §4 Integration Points"
        to: "§4 External Systems"
        influence: "Architecture integration points shown in context diagram"
```

### Impacts
```yaml
impacts:
  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: blocks
    reason: "System context diagram defines scope that architecture elaborates"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§2 System Actors"
        to: "High-Level Architecture §2 System Overview"
        influence: "Context diagram scope defines architecture boundaries"

  - id: TDD-*
    type: informs
    reason: "System context informs technical design scope"
    conditions:
      - when: "project.has_tdd === true"
        applies: true
    sections:
      - from: "§4 External Systems"
        to: "TDD §5 Integration Specifications"
        influence: "External system interactions define integration requirements"

  - id: INTEGRATION-PLAN-*
    type: informs
    reason: "System context identifies external integrations to plan"
    conditions:
      - when: "project.has_integrations === true"
        applies: true
    sections:
      - from: "§4 External Systems"
        to: "Integration Plan §2 Integration Points"
        influence: "Context diagram external systems become integration points"

  - id: USER-GUIDE-*
    type: informs
    reason: "System context helps users understand system scope"
    conditions:
      - when: "project.has_user_guide === true"
        applies: true
    sections:
      - from: "§2 System Actors"
        to: "User Guide §1 Introduction"
        influence: "System context shows user's role in system"

  - id: API-DOCUMENTATION-*
    type: informs
    reason: "System context identifies external API consumers"
    conditions:
      - when: "project.has_apis === true"
        applies: true
    sections:
      - from: "§2 System Actors"
        to: "API Documentation §2 API Consumers"
        influence: "Context diagram actors become API consumer documentation"
```

### Related
```yaml
related:
  - id: SECURITY-PLAN-*
    type: informs
    reason: "System context identifies external trust boundaries"

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "System context shows external data flows"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SYSTEM-CONTEXT-*.md"
    required: false
    purpose: "Track system context diagram updates as scope evolves"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SYSTEM-CONTEXT-*.md"
    required: true
    purpose: "Store system context diagram versions, stakeholder approvals"

  - type: DoD
    path: "satellites/dod/DOD-SYSTEM-CONTEXT-*.md"
    required: true
    purpose: "Define completion criteria: all actors identified, interactions documented, stakeholders approved"
```

## Cel biznesowy / techniczny
System Context Diagram przedstawia relacje systemu z otoczeniem: użytkownikami, systemami zewnętrznymi i interfejsami. Pomaga zrozumieć kontekst działania systemu na wysokim poziomie.

## Zawartość
- System centralny (projektowany)
- Główne interakcje z użytkownikami
- Integracje z systemami zewnętrznymi
- Przepływy danych pomiędzy komponentami
- Graficzny diagram kontekstowy

## Czego nie zawiera
- Szczegółowych opisów implementacji
- Kodów źródłowych
- Strategii sprzedażowych

## Objętość
- 1–2 strony
- 1 diagram + opis

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Architekci systemów
- Developerzy
- Project managerowie
