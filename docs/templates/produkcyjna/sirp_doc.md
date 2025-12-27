# 📄 Security Incident Response Plan (SIRP)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines security policies and controls that SIRP protects"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Security Plan §7 Incident Response"
        to: "§4 Response Procedures"
        influence: "Security policies define incident response approach"

  - id: MONITORING-PLAN-*
    type: requires
    reason: "Monitoring Plan provides incident detection mechanisms"
    conditions:
      - when: "project.has_monitoring === true"
        applies: true
    sections:
      - from: "Monitoring Plan §3 Alert Thresholds"
        to: "§3 Detection Procedures"
        influence: "Monitoring alerts trigger security incident response"

  - id: DATA-GOVERNANCE-POLICY-*
    type: influences
    reason: "Data Governance Policy defines data breach response requirements"
    conditions:
      - when: "project.handles_sensitive_data === true"
        applies: true
    sections:
      - from: "Data Governance Policy §6 Data Breach Response"
        to: "§4 Response Procedures (Data Breach)"
        influence: "Data governance defines data breach handling procedures"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Compliance requirements define incident reporting obligations"
    conditions:
      - when: "project.compliance.incident_reporting === true"
        applies: true
    sections:
      - from: "Compliance Report §4 Incident Reporting"
        to: "§5 Communication Procedures"
        influence: "Compliance mandates define external incident reporting"
```

### Impacts
```yaml
impacts:
  - id: INCIDENT-REPORT-*
    type: blocks
    reason: "SIRP defines incident documentation procedures for incident reports"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§6 Documentation Procedures"
        to: "Incident Report §2 Incident Details"
        influence: "SIRP templates define incident report structure"

  - id: RUNBOOK-*
    type: influences
    reason: "SIRP procedures integrated into operational runbooks"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§4 Response Procedures"
        to: "Runbook §6 Emergency Procedures"
        influence: "Security incident response becomes runbook procedure"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Security incident response training required for team"
    conditions:
      - when: "project.has_training === true"
        applies: true
    sections:
      - from: "§2 Roles & Responsibilities"
        to: "Training Materials §5 Security Training"
        influence: "SIRP roles define security incident training needs"

  - id: BCP-*
    type: informs
    reason: "Security incidents may trigger business continuity procedures"
    conditions:
      - when: "security_incidents.impact_business_continuity === true"
        applies: true
    sections:
      - from: "§4 Response Procedures (Containment)"
        to: "BCP §4 Continuity Procedures"
        influence: "Major security incidents trigger BCP activation"

  - id: DRP-*
    type: informs
    reason: "Security incidents may require disaster recovery"
    conditions:
      - when: "security_incidents.cause_data_loss === true"
        applies: true
    sections:
      - from: "§4 Response Procedures (Recovery)"
        to: "DRP §4 Data Recovery Procedures"
        influence: "Security incident recovery uses DR procedures"

  - id: POSTMORTEM-REPORT-*
    type: informs
    reason: "Security incidents analyzed in postmortems for lessons learned"
    conditions:
      - when: "incident.severity === 'critical'"
        applies: true
    sections:
      - from: "§7 Post-Incident Analysis"
        to: "Postmortem Report §5 Lessons Learned"
        influence: "Major security incidents require postmortem analysis"
```

### Related
```yaml
related:
  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: informs
    reason: "Security incidents inform operational risk assessment"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor-related security incidents require vendor management coordination"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SIRP-*.md"
    required: true
    purpose: "Track SIRP updates, incident response drills, team training"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SIRP-*.md"
    required: true
    purpose: "Store incident response drill results, team training records, SIRP revisions"

  - type: DoR
    path: "satellites/dor/DOR-SIRP-*.md"
    required: true
    purpose: "Define prerequisites: security policies documented, monitoring in place, team trained"

  - type: DoD
    path: "satellites/dod/DOD-SIRP-*.md"
    required: true
    purpose: "Define completion criteria: all procedures documented, team trained, plan tested"
```

## Cel biznesowy / techniczny
SIRP definiuje procedury reagowania na incydenty bezpieczeństwa w systemie. Dokument umożliwia szybkie wykrywanie, analizę i neutralizację zagrożeń.

## Zawartość
- Definicja incydentu bezpieczeństwa
- Role i odpowiedzialności zespołu bezpieczeństwa
- Procedury wykrywania i eskalacji
- Kroki reagowania (containment, eradication, recovery)
- Komunikacja wewnętrzna i zewnętrzna
- Dokumentowanie i analiza po incydencie

## Czego nie zawiera
- Kodów źródłowych
- Strategii marketingowych
- Analiz biznesowych niezwiązanych z bezpieczeństwem

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zespół bezpieczeństwa
- Administratorzy
- Zarząd
