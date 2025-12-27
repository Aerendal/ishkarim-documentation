# 📄 Security Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PRD-*
    type: requires
    reason: "PRD defines security and compliance requirements"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "PRD §6 Non-Functional Requirements (Security)"
        to: "§2 Security Policies"
        influence: "Security NFRs define security controls that must be implemented"
      - from: "PRD §6 Non-Functional Requirements (Compliance)"
        to: "§6 Regulatory Compliance"
        influence: "Compliance requirements (GDPR, HIPAA, ISO) drive security policies"

  - id: HIGH-LEVEL-ARCHITECTURE-*
    type: requires
    reason: "Architecture defines security zones and boundaries"
    conditions:
      - when: "project.has_architecture === true"
        applies: true
    sections:
      - from: "High-Level Architecture §2 Architecture Overview"
        to: "§2 Security Architecture"
        influence: "System architecture defines where security controls are applied"

  - id: DATA-GOVERNANCE-POLICY-*
    type: influences
    reason: "Data governance policies inform data security requirements"
    conditions:
      - when: "project.has_data === true"
        applies: true
    sections:
      - from: "Data Governance Policy §5 Data Access Policies"
        to: "§3 Access Control"
        influence: "Data access policies define security access controls"
```

### Impacts
```yaml
impacts:
  - id: TDD-*
    type: influences
    reason: "Security requirements affect technical design"
    conditions:
      - when: "project.has_technical_design === true"
        applies: true
    sections:
      - from: "§3 Access Control Policies"
        to: "TDD §5 Security Design"
        influence: "Access control policies define authentication/authorization implementation"
      - from: "§4 Data Encryption"
        to: "TDD §5 Security Design"
        influence: "Encryption requirements determine encryption implementation approach"

  - id: DEPLOYMENT-GUIDE-*
    type: influences
    reason: "Security configurations required during deployment"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§3 Access Control Policies"
        to: "Deployment Guide §3 Security Configuration"
        influence: "Security policies define deployment security setup"

  - id: ADMINISTRATOR-GUIDE-*
    type: influences
    reason: "Administrators implement and maintain security controls"
    conditions:
      - when: "project.has_admin_team === true"
        applies: true
    sections:
      - from: "§3 Access Control Policies"
        to: "Administrator Guide §3 User Management"
        influence: "Access control policies guide admin user management procedures"

  - id: COMPLIANCE-REPORT-*
    type: influences
    reason: "Security Plan demonstrates compliance with security regulations"
    conditions:
      - when: "project.has_compliance_requirements === true"
        applies: true
    sections:
      - from: "§6 Regulatory Compliance"
        to: "Compliance Report §2 Compliance Status"
        influence: "Security compliance measures demonstrate regulatory compliance"

  - id: INCIDENT-REPORT-*
    type: informs
    reason: "Security incidents require incident response procedures"
    conditions:
      - when: "incident.type === 'security'"
        applies: true
    sections:
      - from: "§5 Incident Response Plan"
        to: "Incident Report §3 Response Procedures"
        influence: "IRP defines how security incidents are handled"

  - id: TRAINING-MATERIALS-*
    type: influences
    reason: "Security policies require staff training"
    conditions:
      - when: "project.has_staff === true"
        applies: true
    sections:
      - from: "§2 Security Policies"
        to: "Training Materials §3 Security Training"
        influence: "Security policies define security awareness training content"
```

### Related
```yaml
related:
  - id: API-DOCUMENTATION-*
    type: informs
    reason: "API security controls documented in API documentation"

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "Data security affects data management procedures"

  - id: MONITORING-PLAN-*
    type: informs
    reason: "Security monitoring requirements"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SECURITY-*.md"
    required: false
    purpose: "Track security control implementation and audit tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SECURITY-*.md"
    required: true
    purpose: "Store security audit reports, penetration test results, vulnerability scans, compliance certificates"

  - type: DoD
    path: "satellites/dod/DOD-SECURITY-*.md"
    required: true
    purpose: "Define completion criteria: all controls implemented, penetration tested, compliance verified"
```

## Cel biznesowy / techniczny
Security Plan określa podejście do bezpieczeństwa systemu, ochrony danych i kontroli dostępu. Dokument gwarantuje zgodność z regulacjami i minimalizuje ryzyko incydentów.

## Zawartość
- Polityki bezpieczeństwa
- Model kontroli dostępu (RBAC, IAM)
- Procedury uwierzytelniania i autoryzacji
- Szyfrowanie danych (w spoczynku i transmisji)
- Plan reagowania na incydenty (IRP)
- Zgodność z regulacjami (RODO, ISO, NIST)

## Czego nie zawiera
- Szczegółowych implementacji kodu
- Strategii sprzedażowych
- Ogólnych opisów biznesowych

## Objętość
- 3–6 stron
- 10–12 punktów kluczowych

## Kategoria
- **Przydatne** (produkcyjne)

## Odbiorcy
- Architekci systemów
- Administratorzy
- Zespół ds. bezpieczeństwa
