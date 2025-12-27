# 📄 Business Continuity Plan (BCP)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case identifies critical business processes that must maintain continuity"
    conditions:
      - when: "project.business_critical === true"
        applies: true
      - when: "project.type === 'experimental' || 'poc'"
        applies: false
    sections:
      - from: "Business Case §3 Business Objectives"
        to: "§2 Critical Business Processes"
        influence: "Business objectives define which processes are critical for continuity"

  - id: DRP-*
    type: requires
    reason: "DRP provides technical recovery procedures that BCP coordinates"
    conditions:
      - when: "project.has_technical_infrastructure === true"
        applies: true
    sections:
      - from: "DRP §3 Recovery Procedures"
        to: "§4 Continuity Procedures"
        influence: "Technical recovery procedures support business continuity"
      - from: "DRP §4 RTO/RPO Targets"
        to: "§2 Critical Business Processes"
        influence: "Recovery time objectives inform business continuity planning"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: requires
    reason: "Risk assessment identifies threats that BCP must address"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Operational Risk Assessment §3 Risk Inventory"
        to: "§3 Threat and Risk Identification"
        influence: "Identified risks become the basis for continuity planning"
      - from: "Operational Risk Assessment §4 Risk Mitigation"
        to: "§4 Continuity Procedures"
        influence: "Risk mitigation strategies inform continuity procedures"

  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines stakeholders and organizational structure"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §11 Key stakeholders"
        to: "§5 Roles and Responsibilities"
        influence: "Stakeholder map defines crisis response team structure"
```

### Impacts
```yaml
impacts:
  - id: RUNBOOK-*
    type: influences
    reason: "BCP continuity procedures inform operational runbook procedures"
    conditions:
      - when: "project.has_operations === true"
        applies: true
    sections:
      - from: "§4 Continuity Procedures"
        to: "Runbook §4 Emergency Procedures"
        influence: "Business continuity procedures define emergency operational responses"

  - id: INCIDENT-REPORT-*
    type: informs
    reason: "BCP defines incident response procedures and escalation paths"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§6 Crisis Communication Procedures"
        to: "Incident Report §5 Escalation Path"
        influence: "BCP communication procedures define incident escalation"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "BCP procedures require training for crisis response teams"
    conditions:
      - when: "bcp.requires_training === true"
        applies: true
    sections:
      - from: "§7 BCP Testing and Exercises"
        to: "Training Materials §3 Crisis Response Training"
        influence: "BCP exercises define crisis response training scenarios"

  - id: OPERATIONAL-MANUAL-*
    type: informs
    reason: "Operational manual incorporates business continuity procedures"
    conditions:
      - when: "project.has_operations_team === true"
        applies: true
    sections:
      - from: "§4 Continuity Procedures"
        to: "Operational Manual §7 Emergency Procedures"
        influence: "BCP procedures inform operational emergency protocols"
```

### Related
```yaml
related:
  - id: SLA-*
    type: informs
    reason: "SLAs define service availability commitments that BCP must maintain"

  - id: SECURITY-PLAN-*
    type: informs
    reason: "Security incidents may trigger BCP activation"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Regulatory compliance may require BCP documentation"

  - id: VENDOR-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor dependencies affect business continuity planning"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-BCP-*.md"
    required: false
    purpose: "Track BCP testing, updates, and improvement actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-BCP-*.md"
    required: true
    purpose: "Store BCP test results, crisis exercise reports, continuity validation"

  - type: DoD
    path: "satellites/dod/DOD-BCP-*.md"
    required: true
    purpose: "Define completion criteria: BCP tested, team trained, procedures validated"
```

## Cel biznesowy / techniczny
Business Continuity Plan (BCP) określa procedury zapewniające ciągłość działania organizacji w przypadku kryzysów. Dokument jest szerszy niż DRP i obejmuje także procesy biznesowe.

## Zawartość
- Analiza krytycznych procesów biznesowych
- Identyfikacja zagrożeń i ryzyk
- Procedury utrzymania kluczowych usług
- Role i odpowiedzialności w sytuacjach kryzysowych
- Procedury komunikacji w kryzysie
- Testy i ćwiczenia BCP

## Czego nie zawiera
- Strategii marketingowych
- Kodów źródłowych
- Szczegółowych analiz finansowych

## Objętość
- 5–8 stron
- 8–10 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Zespół kryzysowy
