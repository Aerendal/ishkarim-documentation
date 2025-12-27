# 📄 Basel III Risk Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Raport zgodny z międzynarodowymi standardami Basel III, oceniający ryzyka finansowe i stabilność banków.

## Zawartość
- Wskaźniki płynności (LCR, NSFR)
- Wskaźniki kapitałowe (Tier 1, Tier 2)
- Analiza ekspozycji ryzyk kredytowych i rynkowych
- Scenariusze stres-testów

## Czego nie zawiera
- Planów marketingowych
- Szczegółowych danych klientów

## Objętość
- 10–15 stron
- Raport + wskaźniki tabelaryczne

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Banki
- Regulatorzy finansowi
- Zarządy instytucji finansowych

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: FINANCIAL-RISK-ASSESSMENT-*
    type: requires
    reason: "Ocena ryzyka finansowego dostarcza danych dla analiz ryzyk kredytowych i rynkowych Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true
      - when: "project.entity_type === 'financial_institution'"
        applies: true
    sections:
      - from: "Financial Risk Assessment §5 Credit Risk Analysis"
        to: "§3 Analiza ekspozycji ryzyk kredytowych i rynkowych"
        influence: "Ocena ryzyka kredytowego przekłada się na kalkulację wymogów kapitałowych"
      - from: "Financial Risk Assessment §6 Market Risk Analysis"
        to: "§3 Analiza ekspozycji ryzyk kredytowych i rynkowych"
        influence: "Analiza ryzyka rynkowego wpływa na bufory kapitałowe Basel III"

  - id: LIQUIDITY-MANAGEMENT-PLAN-*
    type: requires
    reason: "Plan zarządzania płynnością definiuje wskaźniki LCR i NSFR wymagane przez Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true
    sections:
      - from: "Liquidity Management Plan §4 Liquidity Coverage Ratio"
        to: "§1 Wskaźniki płynności (LCR, NSFR)"
        influence: "Plan płynności dostarcza danych do wskaźników LCR i NSFR"
      - from: "Liquidity Management Plan §5 Net Stable Funding Ratio"
        to: "§1 Wskaźniki płynności (LCR, NSFR)"
        influence: "Struktura finansowania wpływa na NSFR wymagany przez Basel III"

  - id: CAPITAL-ADEQUACY-REPORT-*
    type: requires
    reason: "Raport adekwatności kapitałowej definiuje strukturę kapitału Tier 1 i Tier 2"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true
    sections:
      - from: "Capital Adequacy Report §3 Tier 1 Capital"
        to: "§2 Wskaźniki kapitałowe (Tier 1, Tier 2)"
        influence: "Struktura kapitału Tier 1 definiuje bufory kapitałowe Basel III"
      - from: "Capital Adequacy Report §4 Tier 2 Capital"
        to: "§2 Wskaźniki kapitałowe (Tier 1, Tier 2)"
        influence: "Kapitał Tier 2 wspiera wymogi kapitałowe Basel III"

  - id: STRESS-TEST-METHODOLOGY-*
    type: requires
    reason: "Metodologia stress-testów definiuje scenariusze wymagane przez Basel III"
    conditions:
      - when: "project.requires_stress_testing === true"
        applies: true
    sections:
      - from: "Stress Test Methodology §6 Stress Scenarios"
        to: "§4 Scenariusze stres-testów"
        influence: "Scenariusze stresowe definiują testy odporności kapitałowej"
```

### Impacts
```yaml
impacts:
  - id: REGULATORY-REPORTING-*
    type: blocks
    reason: "Raportowanie regulacyjne wymaga wskaźników Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true
    sections:
      - from: "§1 Wskaźniki płynności (LCR, NSFR)"
        to: "Regulatory Reporting §5 Liquidity Reporting"
        influence: "Wskaźniki płynności Basel III są raportowane regulatorom"
      - from: "§2 Wskaźniki kapitałowe (Tier 1, Tier 2)"
        to: "Regulatory Reporting §6 Capital Reporting"
        influence: "Wskaźniki kapitałowe Basel III są wymagane w raportach regulacyjnych"

  - id: CAPITAL-PLANNING-*
    type: influences
    reason: "Wyniki Basel III wpływają na plany kapitałowe instytucji"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true
    sections:
      - from: "§2 Wskaźniki kapitałowe (Tier 1, Tier 2)"
        to: "Capital Planning §7 Capital Targets"
        influence: "Wymogi kapitałowe Basel III definiują cele kapitałowe banku"
      - from: "§4 Scenariusze stres-testów"
        to: "Capital Planning §8 Capital Buffers"
        influence: "Wyniki stress-testów wpływają na wysokość buforów kapitałowych"

  - id: RISK-APPETITE-STATEMENT-*
    type: influences
    reason: "Limity ryzyka Basel III wpływają na deklarację apetytu na ryzyko"
    sections:
      - from: "§3 Analiza ekspozycji ryzyk kredytowych i rynkowych"
        to: "Risk Appetite Statement §5 Risk Limits"
        influence: "Ekspozycje ryzyk Basel III definiują limity w risk appetite"

  - id: BOARD-REPORTING-*
    type: informs
    reason: "Status Basel III jest raportowany zarządowi jako kluczowy wskaźnik stabilności"
    sections:
      - from: "§1 Wskaźniki płynności (LCR, NSFR)"
        to: "Board Reporting §9 Financial Stability Metrics"
        influence: "Wskaźniki Basel III informują zarząd o stabilności finansowej banku"
```

### Related Documents
```yaml
related:
  - id: INTERNAL-CAPITAL-ADEQUACY-ASSESSMENT-*
    type: informs
    reason: "ICAAP wspiera ocenę adekwatności kapitałowej zgodną z Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true

  - id: RISK-WEIGHTED-ASSETS-CALCULATION-*
    type: informs
    reason: "Kalkulacja RWA jest podstawą wskaźników kapitałowych Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        applies: true

  - id: BASEL-III-IMPLEMENTATION-PLAN-*
    type: informs
    reason: "Plan implementacji Basel III definiuje roadmap zgodności"
    conditions:
      - when: "project.basel_iii_transition === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-BASEL3-*.md"
    required: false
    purpose: "Tracking Basel III compliance tasks and regulatory milestones"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-BASEL3-*.md"
    required: true
    purpose: "Capital calculations, stress test results, regulatory submissions for Basel III"
    conditions:
      - when: "project.industry === 'banking'"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-BASEL3-*.md"
    required: true
    purpose: "Definition of Ready for Basel III reporting - data quality and calculation methodology"

  - type: DoD
    path: "satellites/dod/DOD-BASEL3-*.md"
    required: true
    purpose: "Definition of Done for Basel III compliance - regulatory approval criteria"
```
