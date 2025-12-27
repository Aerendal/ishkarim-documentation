# 📄 Cyber Defense Readiness Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Ocena gotowości organizacji do odpierania cyberataków i reagowania na zagrożenia.

## Zawartość
- Procedury cyberobrony
- Wyniki symulacji ataków (red team / blue team)
- Analiza odporności na zagrożenia
- Plany awaryjne i procedury odzyskiwania

## Czego nie zawiera
- Szczegółowych implementacji kodu
- Strategii marketingowych

## Objętość
- 5–10 stron
- Raport + rekomendacje

## Kategoria
- **Przydatne** (branżowe)

## Odbiorcy
- Zespoły cyberbezpieczeństwa
- Zarząd
- Instytucje obronne

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: THREAT-INTELLIGENCE-REPORT-*
    type: requires
    reason: "Raport wywiadowczy definiuje zagrożenia cybernetyczne do których organizacja musi się przygotować"
    conditions:
      - when: "project.industry === 'defense'"
        applies: true
      - when: "project.requires_cyber_defense === true"
        applies: true
    sections:
      - from: "Threat Intelligence Report §5 Threat Landscape"
        to: "§3 Analiza odporności na zagrożenia"
        influence: "Landscape zagrożeń definiuje scenariusze testów cyberobrony"
      - from: "Threat Intelligence Report §6 APT Groups"
        to: "§2 Wyniki symulacji ataków (red team / blue team)"
        influence: "Profile grup APT definiują taktyki red team"

  - id: SECURITY-ARCHITECTURE-*
    type: requires
    reason: "Architektura bezpieczeństwa definiuje mechanizmy obronne do testowania"
    conditions:
      - when: "project.requires_cyber_defense === true"
        applies: true
    sections:
      - from: "Security Architecture §13 Defense in Depth"
        to: "§1 Procedury cyberobrony"
        influence: "Strategia defense in depth definiuje wielowarstwowe procedury obronne"
      - from: "Security Architecture §14 Incident Detection"
        to: "§3 Analiza odporności na zagrożenia"
        influence: "Mechanizmy detekcji są testowane pod kątem skuteczności"

  - id: INCIDENT-RESPONSE-PLAN-*
    type: requires
    reason: "Plan reagowania na incydenty definiuje procedury odpowiedzi na cyberataki"
    conditions:
      - when: "project.requires_cyber_defense === true"
        applies: true
    sections:
      - from: "Incident Response Plan §8 Cyber Attack Response"
        to: "§4 Plany awaryjne i procedury odzyskiwania"
        influence: "Procedury IRP stanowią podstawę planów awaryjnych cyberobrony"

  - id: PENETRATION-TEST-REPORT-*
    type: requires
    reason: "Testy penetracyjne dostarczają danych o podatnościach do analizy gotowości"
    sections:
      - from: "Penetration Test Report §7 Attack Scenarios"
        to: "§2 Wyniki symulacji ataków (red team / blue team)"
        influence: "Scenariusze ataków pentestów są wykorzystywane w symulacjach red team"
```

### Impacts
```yaml
impacts:
  - id: SECURITY-OPERATIONS-CENTER-PROCEDURES-*
    type: influences
    reason: "Wyniki testów cyberobrony wpływają na procedury SOC"
    conditions:
      - when: "project.has_soc === true"
        applies: true
    sections:
      - from: "§2 Wyniki symulacji ataków (red team / blue team)"
        to: "SOC Procedures §6 Threat Detection Playbooks"
        influence: "Wyniki red/blue team definiują playbooki detekcji zagrożeń"
      - from: "§1 Procedury cyberobrony"
        to: "SOC Procedures §7 Response Protocols"
        influence: "Procedury cyberobrony są implementowane w protokołach SOC"

  - id: SECURITY-TRAINING-PLAN-*
    type: influences
    reason: "Wyniki gotowości cyberobrony wpływają na program szkoleń"
    sections:
      - from: "§3 Analiza odporności na zagrożenia"
        to: "Security Training Plan §8 Threat-Based Training"
        influence: "Zidentyfikowane słabości definiują obszary szkoleń"

  - id: RISK-REGISTER-*
    type: informs
    reason: "Ocena gotowości cyberobrony informuje o ryzykach cybernetycznych"
    sections:
      - from: "§3 Analiza odporności na zagrożenia"
        to: "Risk Register §9 Cyber Risks"
        influence: "Podatności zidentyfikowane w testach są rejestrowane jako ryzyka"

  - id: SECURITY-INVESTMENT-PLAN-*
    type: informs
    reason: "Luki w cyberobronie wpływają na decyzje inwestycyjne w bezpieczeństwo"
    sections:
      - from: "§3 Analiza odporności na zagrożenia"
        to: "Security Investment Plan §5 Capability Gaps"
        influence: "Zidentyfikowane luki definiują priorytety inwestycyjne"
```

### Related Documents
```yaml
related:
  - id: CYBER-SECURITY-POLICY-*
    type: informs
    reason: "Polityka cyberbezpieczeństwa definiuje ramy dla cyberobrony"
    conditions:
      - when: "project.has_security_policy === true"
        applies: true

  - id: BUSINESS-CONTINUITY-PLAN-*
    type: informs
    reason: "Plan ciągłości biznesowej uwzględnia scenariusze cyberataków"
    conditions:
      - when: "project.requires_business_continuity === true"
        applies: true

  - id: THREAT-MODELING-*
    type: informs
    reason: "Modelowanie zagrożeń wspiera analizę scenariuszy ataków"
    conditions:
      - when: "project.requires_threat_modeling === true"
        applies: true

  - id: SECURITY-METRICS-DASHBOARD-*
    type: informs
    reason: "Metryki bezpieczeństwa monitorują gotowość cyberobrony"
    conditions:
      - when: "project.has_security_metrics === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CYBER-DEFENSE-*.md"
    required: false
    purpose: "Tracking cyber defense exercises and remediation tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CYBER-DEFENSE-*.md"
    required: true
    purpose: "Red team reports, blue team logs, attack simulation results"
    conditions:
      - when: "project.requires_cyber_defense === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-CYBER-DEFENSE-*.md"
    required: true
    purpose: "Definition of Ready for cyber defense assessment - infrastructure and tools prepared"

  - type: DoD
    path: "satellites/dod/DOD-CYBER-DEFENSE-*.md"
    required: true
    purpose: "Definition of Done for cyber defense readiness - all attack scenarios tested and mitigated"
```
