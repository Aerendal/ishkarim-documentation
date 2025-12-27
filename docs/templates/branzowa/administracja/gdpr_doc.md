# 📄 GDPR Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność z europejskim RODO (General Data Protection Regulation).

## Zawartość
- Polityki prywatności
- Procedury przetwarzania danych
- Audyty zgodności
- Dokumentacja praw użytkowników (prawo do usunięcia, przenoszenia danych)

## Czego nie zawiera
- Planów sprzedażowych
- Strategii marketingowych

## Objętość
- 5–10 stron
- Raporty + checklisty

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Regulatorzy
- Zarząd
- Inspektorzy ochrony danych

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: SECURITY-ARCHITECTURE-*
    type: requires
    reason: "Architektura bezpieczeństwa definiuje mechanizmy ochrony danych wymagane przez RODO"
    conditions:
      - when: "project.handles_personal_data === true"
        applies: true
      - when: "project.region === 'EU'"
        applies: true
    sections:
      - from: "Security Architecture §8 Encryption & Data Protection"
        to: "§2 Procedury przetwarzania danych"
        influence: "Mechanizmy szyfrowania i ochrony danych implementują wymagania RODO"
      - from: "Security Architecture §9 Access Control"
        to: "§4 Dokumentacja praw użytkowników"
        influence: "Kontrola dostępu zapewnia realizację praw podmiotów danych"

  - id: DATA-MANAGEMENT-PLAN-*
    type: requires
    reason: "Plan zarządzania danymi definiuje cykl życia danych osobowych"
    conditions:
      - when: "project.handles_personal_data === true"
        applies: true
    sections:
      - from: "Data Management Plan §5 Data Retention Policies"
        to: "§2 Procedury przetwarzania danych"
        influence: "Polityki retencji danych realizują zasadę ograniczenia przechowywania RODO"

  - id: PRIVACY-IMPACT-ASSESSMENT-*
    type: requires
    reason: "PIA identyfikuje ryzyka dla prywatności wymagające audytów zgodności"
    conditions:
      - when: "project.risk_level >= 'high'"
        applies: true
      - when: "project.handles_sensitive_data === true"
        applies: true
    sections:
      - from: "Privacy Impact Assessment §6 Risk Mitigation Strategies"
        to: "§3 Audyty zgodności"
        influence: "Strategie mitigacji ryzyk przekładają się na zakres audytów RODO"
```

### Impacts
```yaml
impacts:
  - id: DATA-PROCESSING-AGREEMENT-*
    type: blocks
    reason: "Umowy powierzenia przetwarzania danych wymagają udokumentowanej zgodności z RODO"
    conditions:
      - when: "project.uses_data_processors === true"
        applies: true
    sections:
      - from: "§1 Polityki prywatności"
        to: "Data Processing Agreement §4 Processor Obligations"
        influence: "Polityki prywatności definiują obowiązki procesora danych"
      - from: "§3 Audyty zgodności"
        to: "Data Processing Agreement §7 Audit Rights"
        influence: "Wyniki audytów RODO stanowią podstawę praw audytowych w umowach"

  - id: SECURITY-INCIDENT-RESPONSE-*
    type: influences
    reason: "Procedury RODO wpływają na procedury reagowania na incydenty bezpieczeństwa"
    conditions:
      - when: "project.handles_personal_data === true"
        applies: true
    sections:
      - from: "§2 Procedury przetwarzania danych"
        to: "Security Incident Response §5 Data Breach Notification"
        influence: "Procedury RODO definiują 72-godzinny wymóg notyfikacji naruszeń"

  - id: COMPLIANCE-AUDIT-REPORT-*
    type: informs
    reason: "Raporty zgodności RODO stanowią podstawę ogólnych audytów compliance"
    sections:
      - from: "§3 Audyty zgodności"
        to: "Compliance Audit Report §8 Regulatory Compliance Status"
        influence: "Status zgodności RODO wpływa na ogólną ocenę compliance organizacji"
```

### Related Documents
```yaml
related:
  - id: INFORMATION-SECURITY-POLICY-*
    type: informs
    reason: "Polityka bezpieczeństwa informacji wspiera implementację wymogów RODO"
    conditions:
      - when: "project.has_security_policy === true"
        applies: true

  - id: EMPLOYEE-TRAINING-PLAN-*
    type: informs
    reason: "Szkolenia pracowników w zakresie RODO wspierają świadomość compliance"
    conditions:
      - when: "project.has_data_handlers === true"
        applies: true

  - id: RISK-REGISTER-*
    type: informs
    reason: "Rejestr ryzyk zawiera ryzyka compliance związane z RODO"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-GDPR-*.md"
    required: false
    purpose: "Tracking GDPR compliance action items and remediation tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-GDPR-*.md"
    required: true
    purpose: "Audit trails, consent records, data processing logs required by GDPR"
    conditions:
      - when: "project.subject_to_audit === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-GDPR-*.md"
    required: true
    purpose: "Definition of Ready for GDPR compliance - prerequisites before data processing"

  - type: DoD
    path: "satellites/dod/DOD-GDPR-*.md"
    required: true
    purpose: "Definition of Done for GDPR compliance - verification criteria for each privacy requirement"
```
