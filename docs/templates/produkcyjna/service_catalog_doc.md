# 📄 Service Catalog

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: influences
    reason: "PRD defines product features that become services in catalog"
    conditions:
      - when: "project.offers_services === true"
        applies: true
      - when: "project.type === 'internal-tool'"
        applies: false
    sections:
      - from: "PRD §5 Functional Requirements"
        to: "§2 Service Descriptions"
        influence: "Product features define available services"

  - id: SLA-*
    type: requires
    reason: "SLA defines service level commitments for catalog services"
    conditions:
      - when: "project.has_sla === true"
        applies: true
    sections:
      - from: "SLA §3 Service Level Targets"
        to: "§3 Service Levels"
        influence: "SLA commitments define service availability and performance"

  - id: OPERATIONAL-MANUAL-*
    type: influences
    reason: "Operational Manual defines operational services available"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "Operational Manual §5 Service Management"
        to: "§2 Service Descriptions"
        influence: "Operational services included in service catalog"
```

### Impacts
```yaml
impacts:
  - id: USER-GUIDE-*
    type: informs
    reason: "Service catalog helps users understand available services"
    conditions:
      - when: "project.has_user_guide === true"
        applies: true
    sections:
      - from: "§2 Service Descriptions"
        to: "User Guide §2 Getting Started"
        influence: "Service catalog describes available features for users"

  - id: ONBOARDING-GUIDE-*
    type: informs
    reason: "Service catalog helps new users understand available services"
    conditions:
      - when: "project.has_onboarding === true"
        applies: true
    sections:
      - from: "§2 Service Descriptions"
        to: "Onboarding Guide §4 Available Services"
        influence: "Service catalog informs new user onboarding"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Training materials cover services in catalog"
    conditions:
      - when: "project.has_training === true"
        applies: true
    sections:
      - from: "§2 Service Descriptions"
        to: "Training Materials §2 Service Training"
        influence: "Service catalog defines training scope"

  - id: MAINTENANCE-GUIDE-*
    type: informs
    reason: "Maintenance guide includes support for catalog services"
    conditions:
      - when: "project.has_maintenance === true"
        applies: true
    sections:
      - from: "§4 Support Teams"
        to: "Maintenance Guide §2 Support Procedures"
        influence: "Service ownership defines support responsibilities"
```

### Related
```yaml
related:
  - id: ADMINISTRATOR-GUIDE-*
    type: informs
    reason: "Administrator guide covers service configuration"

  - id: API-DOCUMENTATION-*
    type: informs
    reason: "API documentation describes programmatic service access"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SERVICE-CATALOG-*.md"
    required: false
    purpose: "Track service catalog updates, new service additions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SERVICE-CATALOG-*.md"
    required: false
    purpose: "Store service catalog versions, service usage metrics"

  - type: DoD
    path: "satellites/dod/DOD-SERVICE-CATALOG-*.md"
    required: true
    purpose: "Define completion criteria: all services documented, owners assigned, catalog published"
```

## Cel biznesowy / techniczny
Service Catalog to uporządkowany spis wszystkich usług IT dostępnych dla użytkowników. Dokument ułatwia zarządzanie usługami oraz komunikację pomiędzy dostawcą a klientami.

## Zawartość
- Lista usług IT (np. hosting, wsparcie, backup)
- Opis każdej usługi
- Zakres dostępności i poziomy usług
- Odpowiedzialne zespoły
- Warunki korzystania

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych opisów implementacji
- Treści marketingowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Klienci końcowi
- Zespół wsparcia IT
- Project managerowie
