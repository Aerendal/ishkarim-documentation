# 📄 HIPAA Compliance Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność z amerykańskimi regulacjami HIPAA dotyczącymi ochrony danych zdrowotnych.

## Zawartość
- Procedury ochrony PHI (Protected Health Information)
- Polityki bezpieczeństwa danych zdrowotnych
- Wyniki audytów i kontroli
- Procesy raportowania naruszeń

## Czego nie zawiera
- Kodów źródłowych
- Analiz biznesowych niezwiązanych z ochroną danych

## Objętość
- 3–6 stron
- 5–7 punktów kluczowych

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Zespół prawny
- Regulatorzy
- Zarząd

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: SECURITY-ARCHITECTURE-*
    type: requires
    reason: "Architektura bezpieczeństwa definiuje techniczne zabezpieczenia PHI wymagane przez HIPAA"
    conditions:
      - when: "project.handles_phi === true"
        applies: true
      - when: "project.jurisdiction === 'US'"
        applies: true
      - when: "project.industry === 'healthcare'"
        applies: true
    sections:
      - from: "Security Architecture §8 Encryption & Data Protection"
        to: "§2 Polityki bezpieczeństwa danych zdrowotnych"
        influence: "Szyfrowanie PHI implementuje HIPAA Security Rule technical safeguards"
      - from: "Security Architecture §9 Access Control"
        to: "§2 Polityki bezpieczeństwa danych zdrowotnych"
        influence: "Kontrola dostępu realizuje HIPAA minimum necessary standard"

  - id: PRIVACY-POLICY-*
    type: requires
    reason: "Polityka prywatności definiuje procedury ochrony PHI zgodnie z HIPAA Privacy Rule"
    conditions:
      - when: "project.handles_phi === true"
        applies: true
    sections:
      - from: "Privacy Policy §4 Data Use and Disclosure"
        to: "§1 Procedury ochrony PHI"
        influence: "Zasady użycia i ujawniania danych definiują procedury HIPAA"

  - id: RISK-ASSESSMENT-*
    type: requires
    reason: "Ocena ryzyka jest wymagana przez HIPAA Security Rule dla identyfikacji zagrożeń PHI"
    conditions:
      - when: "project.handles_phi === true"
        applies: true
    sections:
      - from: "Risk Assessment §5 PHI Risk Analysis"
        to: "§3 Wyniki audytów i kontroli"
        influence: "Analiza ryzyk PHI definiuje zakres audytów HIPAA"

  - id: INCIDENT-RESPONSE-PLAN-*
    type: requires
    reason: "Plan reagowania na incydenty definiuje procedury notyfikacji naruszeń HIPAA"
    conditions:
      - when: "project.handles_phi === true"
        applies: true
    sections:
      - from: "Incident Response Plan §7 Breach Notification"
        to: "§4 Procesy raportowania naruszeń"
        influence: "Procedury notyfikacji naruszeń implementują HIPAA Breach Notification Rule"
```

### Impacts
```yaml
impacts:
  - id: BUSINESS-ASSOCIATE-AGREEMENT-*
    type: blocks
    reason: "Umowy BAA wymagają udokumentowanej zgodności z HIPAA"
    conditions:
      - when: "project.uses_business_associates === true"
        applies: true
    sections:
      - from: "§1 Procedury ochrony PHI"
        to: "Business Associate Agreement §5 PHI Safeguards"
        influence: "Procedury ochrony PHI definiują obowiązki business associates"
      - from: "§4 Procesy raportowania naruszeń"
        to: "Business Associate Agreement §8 Breach Notification"
        influence: "Procedury raportowania definiują obowiązki notyfikacyjne BA"

  - id: PATIENT-CONSENT-FORM-*
    type: influences
    reason: "Zgoda pacjenta musi być zgodna z wymogami HIPAA Privacy Rule"
    conditions:
      - when: "project.collects_patient_data === true"
        applies: true
    sections:
      - from: "§1 Procedury ochrony PHI"
        to: "Patient Consent Form §3 Authorization for Use"
        influence: "Procedury HIPAA definiują wymagania dla autoryzacji pacjentów"

  - id: HEALTHCARE-SYSTEM-IMPLEMENTATION-*
    type: blocks
    reason: "Implementacja systemów healthcare wymaga zgodności HIPAA"
    conditions:
      - when: "project.industry === 'healthcare'"
        applies: true
      - when: "project.handles_phi === true"
        applies: true
    sections:
      - from: "§2 Polityki bezpieczeństwa danych zdrowotnych"
        to: "Healthcare System Implementation §9 Security Controls"
        influence: "Kontrole bezpieczeństwa HIPAA są wymagane przed uruchomieniem systemu"

  - id: COMPLIANCE-AUDIT-REPORT-*
    type: informs
    reason: "Status HIPAA wpływa na ogólne compliance w sektorze healthcare"
    sections:
      - from: "§3 Wyniki audytów i kontroli"
        to: "Compliance Audit Report §11 Healthcare Compliance Status"
        influence: "Audyty HIPAA są częścią ogólnej oceny compliance medycznego"
```

### Related Documents
```yaml
related:
  - id: EMPLOYEE-TRAINING-PLAN-*
    type: informs
    reason: "HIPAA wymaga szkoleń pracowników w zakresie ochrony PHI"
    conditions:
      - when: "project.has_phi_handlers === true"
        applies: true

  - id: DISASTER-RECOVERY-PLAN-*
    type: informs
    reason: "HIPAA wymaga planów odzyskiwania dla systemów przetwarzających PHI"
    conditions:
      - when: "project.handles_phi === true"
        applies: true

  - id: AUDIT-LOG-POLICY-*
    type: informs
    reason: "HIPAA wymaga logowania dostępu do PHI"
    conditions:
      - when: "project.handles_phi === true"
        applies: true

  - id: MINIMUM-NECESSARY-POLICY-*
    type: informs
    reason: "Polityka minimum necessary realizuje wymagania HIPAA Privacy Rule"
    conditions:
      - when: "project.handles_phi === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-HIPAA-*.md"
    required: false
    purpose: "Tracking HIPAA compliance tasks and remediation items"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-HIPAA-*.md"
    required: true
    purpose: "Audit logs, risk assessments, breach notifications required by HIPAA"
    conditions:
      - when: "project.handles_phi === true"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-HIPAA-*.md"
    required: true
    purpose: "Definition of Ready for HIPAA compliance - security controls and policies in place"

  - type: DoD
    path: "satellites/dod/DOD-HIPAA-*.md"
    required: true
    purpose: "Definition of Done for HIPAA compliance - all safeguards validated and audited"
```
