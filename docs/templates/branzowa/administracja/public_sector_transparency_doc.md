# 📄 Public Sector Transparency Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Raport przejrzystości działań sektora publicznego, zapewniający otwartość i odpowiedzialność instytucji.

## Zawartość
- Informacje o wydatkach publicznych
- Raporty projektów
- Dane o kontraktach i zamówieniach publicznych
- Wskaźniki efektywności

## Czego nie zawiera
- Danych wrażliwych
- Strategii politycznych

## Objętość
- 5–10 stron
- Raport tabelaryczny + opisowy

## Kategoria
- **Przydatne** (branżowe)

## Odbiorcy
- Społeczeństwo
- Instytucje kontrolne
- Organizacje watchdog

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter definiuje cele i zakres projektu publicznego wymagającego raportowania"
    conditions:
      - when: "project.sector === 'public'"
        applies: true
      - when: "project.funding_source === 'public_funds'"
        applies: true
    sections:
      - from: "Project Charter §12 Cele projektu"
        to: "§2 Raporty projektów"
        influence: "Cele projektu przekładają się na KPI i wskaźniki raportowane publicznie"
      - from: "Project Charter §14 Budget i zasoby"
        to: "§1 Informacje o wydatkach publicznych"
        influence: "Budżet projektu stanowi podstawę raportowania wydatków"

  - id: PROCUREMENT-PLAN-*
    type: requires
    reason: "Plan zakupów definiuje zamówienia publiczne wymagające transparency reporting"
    conditions:
      - when: "project.has_procurement === true"
        applies: true
    sections:
      - from: "Procurement Plan §5 Contract Awards"
        to: "§3 Dane o kontraktach i zamówieniach publicznych"
        influence: "Decyzje zakupowe muszą być raportowane zgodnie z wymogami transparentności"

  - id: PERFORMANCE-METRICS-*
    type: requires
    reason: "Metryki wydajności dostarczają danych do wskaźników efektywności"
    conditions:
      - when: "project.requires_performance_reporting === true"
        applies: true
    sections:
      - from: "Performance Metrics §8 KPI Dashboard"
        to: "§4 Wskaźniki efektywności"
        influence: "KPI projektu stanowią podstawę publicznych wskaźników efektywności"
```

### Impacts
```yaml
impacts:
  - id: PUBLIC-AUDIT-REPORT-*
    type: informs
    reason: "Raporty transparentności stanowią dane wejściowe dla audytów publicznych"
    conditions:
      - when: "project.subject_to_public_audit === true"
        applies: true
    sections:
      - from: "§1 Informacje o wydatkach publicznych"
        to: "Public Audit Report §5 Expenditure Analysis"
        influence: "Dane o wydatkach są weryfikowane podczas audytów publicznych"
      - from: "§4 Wskaźniki efektywności"
        to: "Public Audit Report §9 Performance Evaluation"
        influence: "Wskaźniki efektywności są oceniane pod kątem value for money"

  - id: STAKEHOLDER-COMMUNICATION-*
    type: influences
    reason: "Raporty transparentności wpływają na komunikację z społeczeństwem"
    sections:
      - from: "§2 Raporty projektów"
        to: "Stakeholder Communication §6 Public Disclosure"
        influence: "Status projektów publicznych jest komunikowany stakeholderom"

  - id: ACCOUNTABILITY-FRAMEWORK-*
    type: informs
    reason: "Dane transparentności wspierają framework odpowiedzialności instytucji"
    conditions:
      - when: "project.sector === 'public'"
        applies: true
    sections:
      - from: "§3 Dane o kontraktach i zamówieniach publicznych"
        to: "Accountability Framework §7 Procurement Accountability"
        influence: "Transparentność zamówień publicznych zwiększa odpowiedzialność"
```

### Related Documents
```yaml
related:
  - id: OPEN-DATA-POLICY-*
    type: informs
    reason: "Polityka otwartych danych definiuje zakres i format publikowanych informacji"
    conditions:
      - when: "project.has_open_data_policy === true"
        applies: true

  - id: CITIZEN-ENGAGEMENT-PLAN-*
    type: informs
    reason: "Plan zaangażowania obywateli wykorzystuje dane transparentności"

  - id: ANTI-CORRUPTION-POLICY-*
    type: informs
    reason: "Transparentność wspiera politykę antykorupcyjną"
    conditions:
      - when: "project.risk_corruption >= 'medium'"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TRANSPARENCY-*.md"
    required: false
    purpose: "Tracking transparency reporting tasks and publication deadlines"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TRANSPARENCY-*.md"
    required: true
    purpose: "Supporting documents for transparency claims - invoices, contracts, meeting minutes"
    conditions:
      - when: "project.sector === 'public'"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-TRANSPARENCY-*.md"
    required: false
    purpose: "Definition of Ready for transparency reporting - data quality criteria"

  - type: DoD
    path: "satellites/dod/DOD-TRANSPARENCY-*.md"
    required: true
    purpose: "Definition of Done for transparency reporting - publication and accessibility criteria"
```
