# 📄 Operational Risk Assessment

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: influences
    reason: "PRD identifies risks in requirements and constraints"
    conditions:
      - when: "project.has_prd === true"
        applies: true
    sections:
      - from: "PRD §12 Risks & Mitigations"
        to: "§2 Risk Identification"
        influence: "PRD risks become operational risks to assess"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: influences
    reason: "Architecture introduces operational risks"
    conditions:
      - when: "project.has_architecture === true"
        applies: true
    sections:
      - from: "High-Level Architecture §2 Architecture Overview"
        to: "§2 Risk Identification"
        influence: "Architecture complexity and dependencies introduce operational risks"

  - id: INCIDENT-REPORT-*
    type: influences
    reason: "Past incidents reveal operational risks"
    conditions:
      - when: "project.has_incident_history === true"
        applies: true
    sections:
      - from: "Incident Report §4 Root Cause"
        to: "§2 Risk Identification"
        influence: "Incident root causes identify operational risks"
```

### Impacts
```yaml
impacts:
  - id: DRP-*
    type: influences
    reason: "High-impact risks require disaster recovery planning"
    conditions:
      - when: "risk.impact === 'critical'"
        applies: true
    sections:
      - from: "§2 Risk Identification"
        to: "DRP §2 Disaster Scenarios"
        influence: "Critical operational risks become DRP disaster scenarios"

  - id: BCP-*
    type: influences
    reason: "Business-critical risks require continuity planning"
    conditions:
      - when: "risk.affects_business_continuity === true"
        applies: true
    sections:
      - from: "§2 Risk Identification"
        to: "BCP §3 Threat Identification"
        influence: "Operational risks inform BCP threat identification"

  - id: MONITORING-PLAN-*
    type: influences
    reason: "Operational risks require monitoring"
    conditions:
      - when: "risk.requires_monitoring === true"
        applies: true
    sections:
      - from: "§4 Risk Mitigation Strategies"
        to: "Monitoring Plan §2 Monitoring Metrics"
        influence: "Risk mitigation requires monitoring risk indicators"

  - id: SECURITY-PLAN-*
    type: informs
    reason: "Security risks require security controls"
    conditions:
      - when: "risk.type === 'security'"
        applies: true
    sections:
      - from: "§2 Risk Identification"
        to: "Security Plan §6 Security Improvements"
        influence: "Security operational risks drive security plan enhancements"
```

### Related
```yaml
related:
  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Operational Risk Assessment is part of overall risk management"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Compliance risks are operational risks"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor dependencies introduce operational risks"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RISK-ASSESS-*.md"
    required: false
    purpose: "Track risk mitigation actions and risk monitoring tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RISK-ASSESS-*.md"
    required: true
    purpose: "Store risk assessment matrices, mitigation plans, risk monitoring reports"

  - type: DoD
    path: "satellites/dod/DOD-RISK-ASSESS-*.md"
    required: true
    purpose: "Define completion criteria: all risks identified, assessed, mitigation strategies defined"
```

## Cel biznesowy / techniczny
Operational Risk Assessment ocenia ryzyka operacyjne związane z procesami biznesowymi i technicznymi. Dokument wspiera zarządzanie ryzykiem i planowanie działań prewencyjnych.

## Zawartość
- Identyfikacja ryzyk operacyjnych
- Ocena prawdopodobieństwa i wpływu
- Klasyfikacja ryzyk (wysokie, średnie, niskie)
- Strategie mitigacji
- Plany awaryjne
- Monitoring i raportowanie ryzyk

## Czego nie zawiera
- Kodów źródłowych
- Analiz marketingowych
- Prognoz finansowych

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Działy operacyjne
