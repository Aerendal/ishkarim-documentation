# 📄 Incident Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: MONITORING-PLAN-*
    type: influences
    reason: "Monitoring system detects incidents that require reporting"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
      - when: "incident.detected_by === 'monitoring'"
        applies: true
    sections:
      - from: "Monitoring Plan §3 Alert Thresholds"
        to: "§2 Incident Description"
        influence: "Monitoring alerts provide initial incident detection data"

  - id: RUNBOOK-*
    type: influences
    reason: "Runbook procedures guide incident response"
    conditions:
      - when: "project.has_runbook === true"
        applies: true
    sections:
      - from: "Runbook §4 Incident Response Procedures"
        to: "§3 Resolution Steps"
        influence: "Runbook procedures document how incident was resolved"

  - id: BCP-*
    type: influences
    reason: "Major incidents may trigger BCP activation"
    conditions:
      - when: "incident.severity === 'critical'"
        applies: true
    sections:
      - from: "BCP §6 Crisis Communication"
        to: "§5 Escalation Path"
        influence: "BCP defines escalation procedures for critical incidents"
```

### Impacts
```yaml
impacts:
  - id: POSTMORTEM-REPORT-*
    type: influences
    reason: "Serious incidents require detailed postmortem analysis"
    conditions:
      - when: "incident.severity in ['critical', 'major']"
        applies: true
      - when: "incident.duration > threshold"
        applies: true
    sections:
      - from: "§4 Root Cause Analysis"
        to: "Postmortem Report §3 Root Cause"
        influence: "Incident RCA becomes basis for postmortem analysis"
      - from: "§6 Lessons Learned"
        to: "Postmortem Report §5 Action Items"
        influence: "Incident lessons inform postmortem improvement actions"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: informs
    reason: "Incidents reveal operational risks that need assessment"
    conditions:
      - when: "incident.reveals_new_risk === true"
        applies: true
    sections:
      - from: "§4 Root Cause Analysis"
        to: "Operational Risk Assessment §3 Risk Inventory"
        influence: "Incident causes identify previously unknown operational risks"

  - id: RUNBOOK-*
    type: influences
    reason: "Incident resolution procedures update runbook"
    conditions:
      - when: "incident.procedure_gap_found === true"
        applies: true
    sections:
      - from: "§3 Resolution Steps"
        to: "Runbook §4 Incident Response Procedures"
        influence: "New resolution procedures added to runbook"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Incidents reveal training needs"
    conditions:
      - when: "incident.caused_by === 'human_error'"
        applies: true
    sections:
      - from: "§6 Lessons Learned"
        to: "Training Materials §3 Incident Response Training"
        influence: "Incident lessons define training content to prevent recurrence"
```

### Related
```yaml
related:
  - id: SECURITY-PLAN-*
    type: informs
    reason: "Security incidents may require security plan updates"

  - id: CHANGE-LOG-*
    type: informs
    reason: "Changes related to incident documented in changelog"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-INCIDENT-*.md"
    required: true
    purpose: "Track incident remediation and follow-up action items"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-INCIDENT-*.md"
    required: true
    purpose: "Store logs, screenshots, monitoring data, communication records"

  - type: DoD
    path: "satellites/dod/DOD-INCIDENT-*.md"
    required: true
    purpose: "Define completion criteria: RCA complete, actions implemented, documentation updated"
```

## Cel biznesowy / techniczny
Incident Report dokumentuje szczegóły zdarzeń krytycznych, awarii lub incydentów bezpieczeństwa. Jego celem jest analiza przyczyn i zapobieganie podobnym sytuacjom w przyszłości.

## Zawartość
- Data i opis incydentu
- Zakres i wpływ zdarzenia
- Kroki podjęte w celu rozwiązania
- Analiza przyczyn źródłowych (root cause analysis)
- Wnioski i rekomendacje
- Plan działań zapobiegawczych

## Czego nie zawiera
- Strategii biznesowych
- Kodów źródłowych
- Raportów finansowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zespół wsparcia
- Administratorzy
- Zarząd
