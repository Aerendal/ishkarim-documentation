# 📄 Technical Design Document (TDD)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "High-Level Architecture provides architectural foundation for detailed design"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "High-Level Architecture §2 Architecture Overview"
        to: "§3 System Architecture"
        influence: "High-level architecture defines overall system structure for detailed design"
      - from: "High-Level Architecture §3 Key Components"
        to: "§2 Component Design"
        influence: "Component structure from architecture expanded into detailed design"

  - id: PRD-*
    type: requires
    reason: "PRD defines requirements that technical design must implement"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§2 Functional Design"
        influence: "Functional requirements define what technical design must implement"
      - from: "PRD §6 Non-Functional Requirements"
        to: "§3 System Architecture"
        influence: "NFRs (performance, scalability, security) drive technical architecture decisions"

  - id: ADR-*
    type: requires
    reason: "Architectural decisions must be incorporated into technical design"
    conditions:
      - when: "adr.status === 'accepted'"
        applies: true
    sections:
      - from: "ADR §4 Decision"
        to: "§3 System Architecture"
        influence: "Accepted architectural decisions define technical design constraints"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security requirements affect technical design implementation"
    conditions:
      - when: "project.has_security_requirements === true"
        applies: true
    sections:
      - from: "Security Plan §3 Access Control"
        to: "§5 Security Design"
        influence: "Access control requirements define authentication/authorization design"
      - from: "Security Plan §4 Data Encryption"
        to: "§5 Security Design"
        influence: "Encryption requirements determine data protection implementation"
```

### Impacts
```yaml
impacts:
  - id: API-DOCUMENTATION-*
    type: blocks
    reason: "API Documentation requires TDD API specifications"
    conditions:
      - when: "project.has_api === true"
        applies: true
    sections:
      - from: "§4 API Specifications"
        to: "API Documentation §2 Endpoints"
        influence: "TDD API specs define endpoints to document"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Technical design determines deployment requirements"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 System Architecture"
        to: "Deployment Guide §2 Environment Requirements"
        influence: "System architecture defines infrastructure and deployment needs"
      - from: "§6 Database Architecture"
        to: "Deployment Guide §3 Database Setup"
        influence: "Database design determines database deployment procedures"

  - id: TEST-PLAN-*
    type: influences
    reason: "Technical design defines what needs testing"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 API Specifications"
        to: "Test Plan §4 Integration Tests"
        influence: "API specs define integration test scenarios"

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "Database design informs data management procedures"
    conditions:
      - when: "project.has_database === true"
        applies: true
    sections:
      - from: "§6 Database Architecture"
        to: "Data Management Plan §2 Data Types"
        influence: "Database schema defines data structures to manage"

  - id: ADMINISTRATOR-GUIDE-*
    type: informs
    reason: "Technical design informs administrative procedures"
    conditions:
      - when: "project.has_admin_team === true"
        applies: true
    sections:
      - from: "§3 System Architecture"
        to: "Administrator Guide §2 System Configuration"
        influence: "System architecture defines what administrators need to configure"
```

### Related
```yaml
related:
  - id: INTEGRATION-PLAN-*
    type: informs
    reason: "TDD API specs inform integration planning"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance requirements from TDD need performance testing"

  - id: CONFIGURATION-MANAGEMENT-PLAN-*
    type: informs
    reason: "System components from TDD need configuration management"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TDD-*.md"
    required: false
    purpose: "Track technical design tasks and review actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TDD-*.md"
    required: true
    purpose: "Store technical diagrams, database schemas, API prototypes, POCs"

  - type: DoR
    path: "satellites/dor/DOR-TDD-*.md"
    required: true
    purpose: "Define prerequisites: architecture approved, requirements finalized, ADRs documented"

  - type: DoD
    path: "satellites/dod/DOD-TDD-*.md"
    required: true
    purpose: "Define completion criteria: all components designed, APIs specified, reviewed by architects"
```

## Cel biznesowy / techniczny
Technical Design Document rozwija High-Level Architecture, opisując szczegółowo moduły, komponenty, API oraz przepływy danych. Dokument służy jako instrukcja dla developerów podczas implementacji.

## Zawartość
- Szczegółowy opis modułów i komponentów
- Diagramy klas i sekwencji
- Specyfikacje API
- Architektura bazy danych
- Wymagania dotyczące bezpieczeństwa i skalowalności
- Opis przepływów danych

## Czego nie zawiera
- Strategii sprzedażowych
- Treści marketingowych
- Ogólnych wizji biznesowych

## Objętość
- 10–20 stron
- 25–40 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- Developerzy
- Architekci oprogramowania
- QA / testerzy
