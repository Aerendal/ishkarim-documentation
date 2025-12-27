# 📄 Integration Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "High-Level Architecture defines system boundaries and integration points"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "High-Level Architecture §4 Integration Points"
        to: "§2 Systems to Integrate"
        influence: "Architecture integration points define what systems need integration"

  - id: TDD-*
    type: requires
    reason: "TDD defines API specifications and integration interfaces"
    conditions:
      - when: "project.has_technical_design === true"
        applies: true
    sections:
      - from: "TDD §4 API Specifications"
        to: "§3 Integration Interfaces"
        influence: "API specs define integration communication protocols"

  - id: API-DOCUMENTATION-*
    type: requires
    reason: "API Documentation provides integration endpoint specifications"
    conditions:
      - when: "integration.uses_apis === true"
        applies: true
    sections:
      - from: "API Documentation §2 Available Endpoints"
        to: "§3 Integration Interfaces"
        influence: "API endpoints define integration communication details"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines security requirements for external integrations"
    conditions:
      - when: "integration.involves_external_systems === true"
        applies: true
    sections:
      - from: "Security Plan §3 Access Control Policies"
        to: "§4 Security Requirements"
        influence: "Access control policies define integration authentication/authorization"
```

### Impacts
```yaml
impacts:
  - id: TEST-PLAN-*
    type: influences
    reason: "Integration Plan defines integration test scenarios"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§5 Integration Testing Procedures"
        to: "Test Plan §3 Integration Test Scenarios"
        influence: "Integration testing procedures become test plan scenarios"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Integration configurations affect deployment procedures"
    conditions:
      - when: "integration.affects_deployment === true"
        applies: true
    sections:
      - from: "§3 Integration Interfaces"
        to: "Deployment Guide §3 Configuration"
        influence: "Integration configurations become deployment configuration steps"

  - id: RUNBOOK-*
    type: informs
    reason: "Integration troubleshooting procedures inform runbook"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§6 Contingency Plan"
        to: "Runbook §5 Integration Troubleshooting"
        influence: "Integration contingency procedures become operational troubleshooting steps"
```

### Related
```yaml
related:
  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor systems may be integration targets"

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "Data integration requires data management planning"

  - id: CHANGE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Integration changes require change management approval"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-INTEGRATION-*.md"
    required: false
    purpose: "Track integration tasks and coordination activities"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-INTEGRATION-*.md"
    required: true
    purpose: "Store integration test results, API contracts, integration verification logs"

  - type: DoR
    path: "satellites/dor/DOR-INTEGRATION-*.md"
    required: true
    purpose: "Define prerequisites: APIs documented, access granted, test environments ready"

  - type: DoD
    path: "satellites/dod/DOD-INTEGRATION-*.md"
    required: true
    purpose: "Define completion criteria: integration tested, data validated, error handling verified"
```

## Cel biznesowy / techniczny
Integration Plan opisuje proces integracji nowego systemu z istniejącymi rozwiązaniami. Dokument zapewnia spójność danych i płynność operacyjną.

## Zawartość
- Lista systemów do integracji
- Zakres i cele integracji
- Interfejsy i protokoły komunikacji
- Harmonogram integracji
- Procedury testów integracyjnych
- Plan awaryjny w przypadku błędów

## Czego nie zawiera
- Kodów źródłowych
- Strategii marketingowych
- Analiz rynkowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Developerzy
- Architekci systemów
- Project managerowie
