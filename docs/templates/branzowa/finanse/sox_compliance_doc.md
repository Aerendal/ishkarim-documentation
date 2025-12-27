# 📄 SOX Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność z amerykańską ustawą Sarbanes-Oxley (SOX) dotyczącą przejrzystości finansowej i kontroli wewnętrznych.

## Zawartość
- Raporty finansowe
- Procedury kontroli wewnętrznej
- Wyniki audytów
- Mechanizmy zapobiegania oszustwom

## Czego nie zawiera
- Kodów źródłowych
- Analiz technicznych systemów IT

## Objętość
- 5–10 stron
- Raporty + checklisty kontrolne

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Zarząd
- Audytorzy
- Regulatorzy giełdowi

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: FINANCIAL-REPORTING-CONTROLS-*
    type: requires
    reason: "Kontrole raportowania finansowego są fundamentem zgodności SOX Section 404"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
      - when: "project.jurisdiction === 'US'"
        applies: true
    sections:
      - from: "Financial Reporting Controls §5 Internal Control Framework"
        to: "§2 Procedury kontroli wewnętrznej"
        influence: "Framework kontroli wewnętrznej definiuje procedury wymagane przez SOX"
      - from: "Financial Reporting Controls §6 Control Testing"
        to: "§3 Wyniki audytów"
        influence: "Testy kontroli są wymagane do certyfikacji SOX 404"

  - id: FINANCIAL-STATEMENTS-*
    type: requires
    reason: "Sprawozdania finansowe są przedmiotem certyfikacji SOX Section 302"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
    sections:
      - from: "Financial Statements §8 CEO/CFO Certification"
        to: "§1 Raporty finansowe"
        influence: "Certyfikacja kadry zarządzającej jest wymagana przez SOX 302"

  - id: IT-GENERAL-CONTROLS-*
    type: requires
    reason: "Kontrole IT wspierają integralność systemów finansowych wymaganych przez SOX"
    conditions:
      - when: "project.uses_financial_systems === true"
        applies: true
    sections:
      - from: "IT General Controls §7 Access Controls"
        to: "§2 Procedury kontroli wewnętrznej"
        influence: "Kontrole dostępu IT zapewniają integralność danych finansowych"
      - from: "IT General Controls §8 Change Management"
        to: "§4 Mechanizmy zapobiegania oszustwom"
        influence: "Kontrola zmian w systemach finansowych zapobiega manipulacjom"

  - id: FRAUD-RISK-ASSESSMENT-*
    type: requires
    reason: "Ocena ryzyka oszustw jest wymagana przez SOX dla mechanizmów prewencyjnych"
    sections:
      - from: "Fraud Risk Assessment §4 Fraud Scenarios"
        to: "§4 Mechanizmy zapobiegania oszustwom"
        influence: "Scenariusze oszustw definiują mechanizmy prewencyjne SOX"
```

### Impacts
```yaml
impacts:
  - id: EXTERNAL-AUDIT-REPORT-*
    type: blocks
    reason: "Audyt zewnętrzny wymaga certyfikacji SOX jako warunku opinii audytora"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
    sections:
      - from: "§3 Wyniki audytów"
        to: "External Audit Report §5 SOX 404 Opinion"
        influence: "Audyt SOX 404 jest wymagany do wydania opinii o sprawozdaniu finansowym"
      - from: "§2 Procedury kontroli wewnętrznej"
        to: "External Audit Report §6 Internal Control Opinion"
        influence: "Ocena kontroli wewnętrznych wpływa na opinię audytora"

  - id: MANAGEMENT-REPRESENTATION-LETTER-*
    type: blocks
    reason: "Oświadczenia zarządu wymagają certyfikacji SOX"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
    sections:
      - from: "§1 Raporty finansowe"
        to: "Management Representation Letter §7 Financial Statement Accuracy"
        influence: "Certyfikacja SOX wspiera oświadczenia zarządu o rzetelności sprawozdań"

  - id: SEC-FILING-*
    type: blocks
    reason: "Dokumenty składane do SEC wymagają certyfikacji SOX"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
      - when: "project.jurisdiction === 'US'"
        applies: true
    sections:
      - from: "§1 Raporty finansowe"
        to: "SEC Filing §3 10-K Annual Report"
        influence: "Raporty finansowe z certyfikacją SOX są składane w raporcie 10-K"

  - id: COMPLIANCE-MONITORING-*
    type: informs
    reason: "Status SOX jest monitorowany jako część ogólnego compliance"
    sections:
      - from: "§3 Wyniki audytów"
        to: "Compliance Monitoring §8 SOX Compliance Status"
        influence: "Wyniki audytów SOX są śledzone w systemie monitoringu compliance"
```

### Related Documents
```yaml
related:
  - id: WHISTLEBLOWER-POLICY-*
    type: informs
    reason: "SOX Section 301 wymaga polityki whistleblower dla zgłaszania nieprawidłowości"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true

  - id: CODE-OF-ETHICS-*
    type: informs
    reason: "SOX Section 406 wymaga kodeksu etyki dla kadry zarządzającej"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true

  - id: AUDIT-COMMITTEE-CHARTER-*
    type: informs
    reason: "SOX Section 301 definiuje wymagania dla komitetu audytu"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true

  - id: DOCUMENT-RETENTION-POLICY-*
    type: informs
    reason: "SOX Section 802 wymaga polityki retencji dokumentów"
    conditions:
      - when: "project.publicly_traded === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SOX-*.md"
    required: false
    purpose: "Tracking SOX compliance tasks and quarterly/annual certification deadlines"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SOX-*.md"
    required: true
    purpose: "Control test results, audit evidence, management certifications required by SOX"
    conditions:
      - when: "project.publicly_traded === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-SOX-*.md"
    required: true
    purpose: "Definition of Ready for SOX compliance - control design and documentation requirements"

  - type: DoD
    path: "satellites/dod/DOD-SOX-*.md"
    required: true
    purpose: "Definition of Done for SOX compliance - testing completion and certification criteria"
```
