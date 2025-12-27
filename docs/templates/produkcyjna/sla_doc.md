# 📄 Service Level Agreement (SLA)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: influences
    reason: "PRD performance requirements inform SLA targets"
    conditions:
      - when: "project.has_performance_requirements === true"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements (Performance)"
        to: "§3 Service Level Targets"
        influence: "Performance NFRs define SLA performance commitments"

  - id: DRP-*
    type: influences
    reason: "DRP RTO/RPO affect SLA availability commitments"
    conditions:
      - when: "project.has_drp === true"
        applies: true
    sections:
      - from: "DRP §5 RTO/RPO Targets"
        to: "§3 Service Level Targets"
        influence: "DRP recovery targets inform SLA uptime guarantees"
```

### Impacts
```yaml
impacts:
  - id: MONITORING-PLAN-*
    type: blocks
    reason: "SLA targets require monitoring to validate compliance"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Service Level Targets"
        to: "Monitoring Plan §3 Alert Thresholds"
        influence: "SLA targets define monitoring thresholds for SLA compliance"

  - id: MAINTENANCE-GUIDE-*
    type: influences
    reason: "SLA defines maintenance response times"
    conditions:
      - when: "project.has_maintenance === true"
        applies: true
    sections:
      - from: "§4 Response Times"
        to: "Maintenance Guide §2 Support Procedures"
        influence: "SLA response commitments define maintenance SLAs"

  - id: RUNBOOK-*
    type: informs
    reason: "SLA commitments require operational procedures to maintain"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§3 Service Level Targets"
        to: "Runbook §2 Operational Procedures"
        influence: "SLA targets inform operational procedures to meet commitments"
```

### Related
```yaml
related:
  - id: SERVICE-CATALOG-*
    type: informs
    reason: "SLA defines service levels in service catalog"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance tests validate SLA targets are achievable"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SLA-*.md"
    required: false
    purpose: "Track SLA compliance monitoring and reporting"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SLA-*.md"
    required: true
    purpose: "Store SLA performance reports, uptime metrics, compliance records"

  - type: DoD
    path: "satellites/dod/DOD-SLA-*.md"
    required: true
    purpose: "Define completion criteria: SLA targets defined, monitoring established, reported to stakeholders"
```

## Cel biznesowy / techniczny
Service Level Agreement (SLA) to formalny dokument określający poziom usług świadczonych przez dostawcę systemu lub usług IT. Określa oczekiwania i zobowiązania stron.

## Zawartość
- Zakres usług
- Gwarantowane poziomy dostępności (uptime)
- Czas reakcji i czas naprawy
- Procedury monitorowania i raportowania
- Kary i konsekwencje za niedotrzymanie SLA

## Czego nie zawiera
- Kodów źródłowych
- Strategii biznesowych
- Backlogów sprintów

## Objętość
- 2–4 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Klienci końcowi
- Project managerowie
- Zespół wsparcia
