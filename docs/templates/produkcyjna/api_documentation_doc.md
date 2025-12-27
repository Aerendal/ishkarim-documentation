# 📄 API Documentation

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: TDD-*
    type: requires
    reason: "TDD defines API specifications, data models, and endpoint architecture"
    conditions:
      - when: "project.has_api === true"
        applies: true
      - when: "project.type === 'frontend-only'"
        applies: false
    sections:
      - from: "TDD §4 API Specifications"
        to: "§2 Available Endpoints"
        influence: "TDD API specs define endpoints, methods, and data contracts"
      - from: "TDD §7 Data Flow Diagrams"
        to: "§6 Data Flow Diagrams"
        influence: "Data flow diagrams show API interaction patterns"

  - id: PRD-*
    type: influences
    reason: "PRD defines functional requirements that determine API capabilities"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§2 Available Endpoints"
        influence: "Functional requirements determine what API endpoints are needed"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines authentication, authorization, and API security policies"
    conditions:
      - when: "project.has_sensitive_data === true || project.is_public_api === true"
        applies: true
      - when: "project.security_level === 'none'"
        applies: false
    sections:
      - from: "Security Plan §3 Access Control Policies"
        to: "§5 Authorization Policies"
        influence: "Access control policies define API authentication and authorization mechanisms"
      - from: "Security Plan §5 Data Protection"
        to: "§5 Authorization Policies"
        influence: "Data protection requirements define API encryption and data handling"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "Architecture defines system boundaries and integration points for APIs"
    conditions:
      - when: "project.has_external_integrations === true"
        applies: true
    sections:
      - from: "High-Level Architecture §4 Integration Points"
        to: "§2 Available Endpoints"
        influence: "Integration points define external-facing API endpoints"
```

### Impacts
```yaml
impacts:
  - id: INTEGRATION-PLAN-*
    type: blocks
    reason: "Integration Plan requires API documentation to plan integrations"
    conditions:
      - when: "project.has_external_integrations === true"
        applies: true
    sections:
      - from: "§2 Available Endpoints"
        to: "Integration Plan §3 Integration Specifications"
        influence: "API endpoints define how external systems integrate"
      - from: "§5 Authorization Policies"
        to: "Integration Plan §4 Security Requirements"
        influence: "API authorization policies determine integration security setup"

  - id: USER-GUIDE-*
    type: informs
    reason: "Developer-facing user guides reference API documentation"
    conditions:
      - when: "project.has_developer_users === true"
        applies: true
    sections:
      - from: "§3 Request/Response Examples"
        to: "User Guide §4 Code Examples"
        influence: "API examples provide code snippets for user guide"

  - id: TEST-PLAN-*
    type: influences
    reason: "API testing requires documented endpoints and expected behaviors"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§2 Available Endpoints"
        to: "Test Plan §3 Test Scenarios"
        influence: "API endpoints define integration and API test scenarios"
      - from: "§4 Error Codes"
        to: "Test Plan §4 Expected Results"
        influence: "Error codes define expected test outcomes for failure scenarios"

  - id: ONBOARDING-GUIDE-*
    type: informs
    reason: "Developer onboarding includes API usage training"
    conditions:
      - when: "project.has_developer_users === true"
        applies: true
    sections:
      - from: "§2 Available Endpoints"
        to: "Onboarding Guide §3 System Overview"
        influence: "API structure informs developer onboarding curriculum"
```

### Related
```yaml
related:
  - id: RUNBOOK-*
    type: informs
    reason: "Runbook may include API troubleshooting procedures"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "API endpoints require monitoring for availability and performance"

  - id: SLA-*
    type: informs
    reason: "SLAs define API performance and availability commitments"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-API-DOC-*.md"
    required: false
    purpose: "Track API documentation updates as endpoints evolve"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-API-DOC-*.md"
    required: true
    purpose: "Store OpenAPI/Swagger specs, Postman collections, API test results"

  - type: DoD
    path: "satellites/dod/DOD-API-DOC-*.md"
    required: true
    purpose: "Define completion criteria: all endpoints documented, examples tested, security reviewed"
```

## Cel biznesowy / techniczny
API Documentation zawiera szczegółowy opis interfejsów API wykorzystywanych w systemie. Umożliwia developerom integrację i korzystanie z funkcji systemu.

## Zawartość
- Opis dostępnych endpointów
- Parametry wejściowe i wyjściowe
- Przykłady zapytań i odpowiedzi
- Kody błędów
- Polityki autoryzacji i limitów
- Diagramy przepływu danych (opcjonalnie)

## Czego nie zawiera
- Strategii biznesowych
- Analiz rynkowych
- Ogólnych opisów marketingowych

## Objętość
- Dokument ciągły (w formie online lub PDF)

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Developerzy
- Architekci systemów
- Partnerzy integracyjni
