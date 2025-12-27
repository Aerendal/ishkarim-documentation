# 📄 Vendor Management Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter defines external dependencies and vendor needs"
    conditions:
      - when: "project.has_external_vendors === true"
        applies: true
      - when: "project.fully_internal === true"
        applies: false
    sections:
      - from: "Project Charter §7 Dependencies"
        to: "§2 Vendor List"
        influence: "Project dependencies identify required vendors"

  - id: RESOURCE-REQUIREMENTS-*
    type: requires
    reason: "Resource Requirements identifies vendor resource needs"
    conditions:
      - when: "project.has_external_vendors === true"
        applies: true
    sections:
      - from: "Resource Requirements §4 External Resources"
        to: "§2 Vendor Selection Criteria"
        influence: "Resource requirements define vendor capabilities needed"

  - id: SECURITY-PLAN-*
    type: requires
    reason: "Security Plan defines vendor security requirements"
    conditions:
      - when: "vendors.handle_sensitive_data === true"
        applies: true
    sections:
      - from: "Security Plan §6 Third-Party Security"
        to: "§5 Vendor Security Requirements"
        influence: "Security policies define vendor compliance requirements"

  - id: DATA-GOVERNANCE-POLICY-*
    type: requires
    reason: "Data Governance Policy defines vendor data handling requirements"
    conditions:
      - when: "vendors.handle_data === true"
        applies: true
    sections:
      - from: "Data Governance Policy §4 Data Sharing"
        to: "§4 Contractual Terms"
        influence: "Data governance requirements included in vendor contracts"
```

### Impacts
```yaml
impacts:
  - id: RISK-OVERVIEW-TECH-*
    type: influences
    reason: "Vendor dependencies create technical risks"
    conditions:
      - when: "project.has_external_vendors === true"
        applies: true
    sections:
      - from: "§3 Vendor Risk Assessment"
        to: "Risk Overview §2 Technical Risks"
        influence: "Vendor risks included in overall technical risk assessment"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: influences
    reason: "Vendor performance affects operational risks"
    conditions:
      - when: "project.has_external_vendors === true"
        applies: true
    sections:
      - from: "§4 Quality Monitoring"
        to: "Operational Risk Assessment §3 Vendor Risks"
        influence: "Vendor monitoring identifies operational risk exposures"

  - id: SLA-*
    type: influences
    reason: "Vendor SLAs must align with overall service SLAs"
    conditions:
      - when: "vendors.provide_critical_services === true"
        applies: true
    sections:
      - from: "§4 Contractual Terms (SLA)"
        to: "SLA §3 Service Level Targets"
        influence: "Vendor SLAs must support overall SLA commitments"

  - id: COMPLIANCE-REPORT-*
    type: informs
    reason: "Vendor compliance audits reported in compliance report"
    conditions:
      - when: "project.compliance.vendor_audits === true"
        applies: true
    sections:
      - from: "§5 Audit Schedule"
        to: "Compliance Report §3 Third-Party Compliance"
        influence: "Vendor audit results demonstrate third-party compliance"

  - id: DRP-*
    type: informs
    reason: "Vendor disaster recovery capabilities affect DRP"
    conditions:
      - when: "vendors.provide_critical_services === true"
        applies: true
    sections:
      - from: "§4 Contractual Terms (DR)"
        to: "DRP §3 Recovery Dependencies"
        influence: "Vendor recovery capabilities impact overall DR strategy"
```

### Related
```yaml
related:
  - id: BCP-*
    type: informs
    reason: "Vendor continuity plans affect business continuity"

  - id: CHANGE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Vendor changes require change management coordination"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-VENDOR-MANAGEMENT-*.md"
    required: true
    purpose: "Track vendor selections, contract negotiations, performance reviews, audits"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-VENDOR-MANAGEMENT-*.md"
    required: true
    purpose: "Store vendor contracts, SLAs, audit reports, performance metrics, compliance certifications"

  - type: DoD
    path: "satellites/dod/DOD-VENDOR-MANAGEMENT-*.md"
    required: true
    purpose: "Define completion criteria: vendors selected, contracts signed, monitoring established, audits scheduled"
```

## Cel biznesowy / techniczny
Vendor Management Plan określa zasady współpracy i kontroli dostawców oraz partnerów biznesowych. Dokument pomaga w ocenie ryzyka i zapewnieniu jakości usług zewnętrznych.

## Zawartość
- Lista kluczowych dostawców
- Kryteria wyboru i oceny dostawców
- Procedury monitorowania jakości usług
- Warunki kontraktowe i SLA
- Plan audytów i przeglądów

## Czego nie zawiera
- Kodów źródłowych
- Analiz marketingowych
- Szczegółowych opisów technicznych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Dział zakupów
