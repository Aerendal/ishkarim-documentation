# 📄 Risk Overview (Techniczny)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "Architecture design reveals technical risks (scalability, single points of failure)"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "High-Level Architecture §3 System Components"
        to: "§2 Technical Risks"
        influence: "Architectural complexity and dependencies create technical risks"

  - id: TDD-*
    type: influences
    reason: "Technical design decisions introduce implementation risks"
    conditions:
      - when: "project.has_tdd === true"
        applies: true
    sections:
      - from: "TDD §3 Technology Stack"
        to: "§2 Technical Risks"
        influence: "Technology choices create adoption and integration risks"

  - id: PRD-*
    type: influences
    reason: "Non-functional requirements (performance, security) create technical risks"
    conditions:
      - when: "project.has_prd === true"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements"
        to: "§2 Technical Risks"
        influence: "NFRs define technical challenges that may fail"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: influences
    reason: "Operational risks complement technical risks"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "Operational Risk Assessment §2 Risk Categories"
        to: "§2 Technical Risks"
        influence: "Operational failures create technical risk scenarios"

  - id: INCIDENT-REPORT-*
    type: influences
    reason: "Past incidents reveal recurring technical risks"
    conditions:
      - when: "project.has_incident_history === true"
        applies: true
    sections:
      - from: "Incident Report §4 Root Cause"
        to: "§2 Technical Risks"
        influence: "Incident root causes identify systemic technical risks"

  - id: POSTMORTEM-REPORT-*
    type: influences
    reason: "Postmortem lessons learned reveal technical risks for future projects"
    conditions:
      - when: "organization.has_postmortems === true"
        applies: true
    sections:
      - from: "Postmortem Report §4 What Went Wrong"
        to: "§2 Technical Risks"
        influence: "Past project failures inform technical risk identification"
```

### Impacts
```yaml
impacts:
  - id: SECURITY-PLAN-*
    type: influences
    reason: "Technical risks inform security risk mitigation strategies"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§4 Risk Mitigation Strategies"
        to: "Security Plan §5 Risk Mitigation"
        influence: "Technical risk mitigations include security controls"

  - id: DRP-*
    type: influences
    reason: "Technical failure risks drive disaster recovery planning"
    conditions:
      - when: "project.has_drp === true"
        applies: true
    sections:
      - from: "§2 Technical Risks (System Failure)"
        to: "DRP §2 Disaster Scenarios"
        influence: "Technical failure scenarios define DR requirements"

  - id: BCP-*
    type: influences
    reason: "Technical risks affect business continuity planning"
    conditions:
      - when: "project.has_bcp === true"
        applies: true
    sections:
      - from: "§2 Technical Risks (Availability)"
        to: "BCP §3 Impact Analysis"
        influence: "Technical availability risks inform business impact"

  - id: MONITORING-PLAN-*
    type: influences
    reason: "Technical risks define what needs monitoring and alerting"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "§2 Technical Risks"
        to: "Monitoring Plan §3 Alert Thresholds"
        influence: "Risk scenarios define monitoring thresholds and alerts"

  - id: TEST-PLAN-*
    type: influences
    reason: "Technical risks drive risk-based testing priorities"
    conditions:
      - when: "project.has_testing === true"
        applies: true
    sections:
      - from: "§3 Risk Impact Assessment"
        to: "Test Plan §2 Testing Approach"
        influence: "High-impact technical risks prioritized for testing"

  - id: TIMELINE-*
    type: informs
    reason: "Technical risks may affect project schedule"
    conditions:
      - when: "risks.schedule_impact === 'high'"
        applies: true
    sections:
      - from: "§2 Technical Risks (Implementation Complexity)"
        to: "Timeline §4 Phase Duration"
        influence: "Technical complexity risks add schedule buffer"
```

### Related
```yaml
related:
  - id: CHANGE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Change management reduces technical change risks"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor risks are subset of technical risks"

  - id: PERFORMANCE-TEST-REPORT-*
    type: informs
    reason: "Performance test results validate or refute performance risks"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-RISK-OVERVIEW-*.md"
    required: true
    purpose: "Track risk assessments, mitigation implementations, risk reviews"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-RISK-OVERVIEW-*.md"
    required: true
    purpose: "Store risk assessment reports, mitigation validation, risk register updates"

  - type: DoD
    path: "satellites/dod/DOD-RISK-OVERVIEW-*.md"
    required: true
    purpose: "Define completion criteria: all technical risks identified, assessed, mitigated, monitored"
```

## Cel biznesowy / techniczny
Risk Overview (techniczny) identyfikuje zagrożenia związane z technologią, wdrożeniem i utrzymaniem systemu. Pomaga w planowaniu działań prewencyjnych i minimalizacji ryzyka awarii.

## Zawartość
- Lista kluczowych ryzyk technologicznych
- Prawdopodobieństwo wystąpienia
- Wpływ na system i użytkowników
- Plan mitigacji (techniczny)
- Strategie redundancji i odtwarzania awaryjnego

## Czego nie zawiera
- Ryzyk rynkowych i biznesowych
- Analizy finansowej
- Detali marketingowych

## Objętość
- 2–3 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Architekci systemów
- Zespół developerski
- Dział operacyjny
