# 📄 High-Level Architecture

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines requirements that drive architecture decisions"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements"
        to: "§2 Architecture Overview"
        influence: "NFRs (performance, scalability, availability) drive architectural patterns"
      - from: "PRD §8 Technical Constraints"
        to: "§2 Architecture Overview"
        influence: "Technical constraints limit architectural choices"

  - id: BRD-*
    type: influences
    reason: "BRD requirements inform high-level architecture when PRD doesn't exist"
    conditions:
      - when: "!project.has_prd && project.has_brd"
        applies: true
    sections:
      - from: "BRD §6 Core Non-Functional Requirements"
        to: "§2 Architecture Overview"
        influence: "Core NFRs inform architecture decisions"

  - id: ADR-*
    type: influences
    reason: "Architecture Decision Records document architectural choices"
    conditions:
      - when: "project.documents_architecture_decisions === true"
        applies: true
    sections:
      - from: "ADR §4 Decision"
        to: "§2 Architecture Overview"
        influence: "Accepted ADRs define architectural components and patterns"
```

### Impacts
```yaml
impacts:
  - id: TDD-*
    type: blocks
    reason: "TDD cannot be created without high-level architecture"
    conditions:
      - when: "project.requires_detailed_design === true"
        applies: true
    sections:
      - from: "§2 Architecture Overview"
        to: "TDD §3 System Architecture"
        influence: "High-level architecture provides foundation for detailed technical design"
      - from: "§3 Key Components"
        to: "TDD §2 Component Design"
        influence: "Component structure defines what needs detailed design"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Architecture defines deployment requirements"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Key Components"
        to: "Deployment Guide §2 Environment Requirements"
        influence: "Component architecture determines deployment infrastructure needs"

  - id: INTEGRATION-PLAN-*
    type: influences
    reason: "Architecture integration points define integration requirements"
    conditions:
      - when: "project.has_integrations === true"
        applies: true
    sections:
      - from: "§4 Integration Points"
        to: "Integration Plan §2 Systems to Integrate"
        influence: "Architectural integration points define what systems need integration"

  - id: SECURITY-PLAN-*
    type: influences
    reason: "Architecture defines security boundaries and requirements"
    conditions:
      - when: "project.has_security_requirements === true"
        applies: true
    sections:
      - from: "§2 Architecture Overview"
        to: "Security Plan §2 Security Architecture"
        influence: "System architecture defines security zones and boundaries"

  - id: ADR-*
    type: informs
    reason: "Architecture may require new architectural decisions"
    conditions:
      - when: "architecture.requires_decisions === true"
        applies: true
    sections:
      - from: "§2 Architecture Overview"
        to: "ADR §3 Context"
        influence: "Architecture gaps or changes trigger new ADRs"
```

### Related
```yaml
related:
  - id: SYSTEM-CONTEXT-DIAGRAM-*
    type: informs
    reason: "System Context Diagram shows system boundaries that inform architecture"

  - id: DRP-*
    type: informs
    reason: "Architecture affects disaster recovery planning"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "Architecture components require monitoring"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ARCHITECTURE-*.md"
    required: false
    purpose: "Track architecture definition and review tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ARCHITECTURE-*.md"
    required: true
    purpose: "Store architecture diagrams, POCs, technology evaluations"

  - type: DoR
    path: "satellites/dor/DOR-ARCHITECTURE-*.md"
    required: true
    purpose: "Define prerequisites: requirements finalized, constraints identified, stakeholders aligned"

  - type: DoD
    path: "satellites/dod/DOD-ARCHITECTURE-*.md"
    required: true
    purpose: "Define completion criteria: all components defined, integration points documented, reviewed by architects"
```

## Cel biznesowy / techniczny
High-Level Architecture przedstawia ogólny obraz systemu – jego moduły, komponenty i integracje. Jest dokumentem technicznym na poziomie koncepcyjnym, służącym jako przewodnik dla projektowania szczegółowego.

## Zawartość
- Ogólny schemat architektury systemu
- Główne moduły i ich odpowiedzialności
- Kluczowe przepływy danych
- Integracje z systemami zewnętrznymi
- Diagramy wysokopoziomowe

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych diagramów klas
- Backlogów sprintowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- Architekci systemów
- Zespół developerski
- Project manager
