# 📄 Medical Device File (MDR)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Zapewnia zgodność urządzeń medycznych z regulacjami UE MDR (Medical Device Regulation).

## Zawartość
- Specyfikacje techniczne urządzenia
- Raporty z testów zgodności
- Dokumenty bezpieczeństwa i jakości
- Certyfikaty regulatorów
- Instrukcje obsługi i utrzymania

## Czego nie zawiera
- Planów marketingowych
- Ogólnych analiz rynkowych

## Objętość
- 15–40 stron
- Kilka sekcji obowiązkowych wg MDR

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Regulatorzy UE
- Producenci sprzętu medycznego
- Zespoły jakości i zgodności

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: DEVICE-DESIGN-SPECIFICATION-*
    type: requires
    reason: "Specyfikacja techniczna urządzenia jest wymagana przez MDR jako część dokumentacji technicznej"
    conditions:
      - when: "project.industry === 'healthcare'"
        applies: true
      - when: "project.type === 'medical_device'"
        applies: true
      - when: "project.region === 'EU'"
        applies: true
    sections:
      - from: "Device Design Specification §5 Technical Characteristics"
        to: "§1 Specyfikacje techniczne urządzenia"
        influence: "Charakterystyki techniczne definiują specyfikację urządzenia w MDR"
      - from: "Device Design Specification §6 Performance Requirements"
        to: "§1 Specyfikacje techniczne urządzenia"
        influence: "Wymagania wydajnościowe są częścią specyfikacji technicznej MDR"

  - id: RISK-MANAGEMENT-FILE-*
    type: requires
    reason: "Dokumentacja zarządzania ryzykiem (ISO 14971) jest wymagana przez MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "Risk Management File §7 Risk Analysis"
        to: "§3 Dokumenty bezpieczeństwa i jakości"
        influence: "Analiza ryzyk ISO 14971 jest częścią dokumentacji bezpieczeństwa MDR"
      - from: "Risk Management File §8 Risk Control Measures"
        to: "§3 Dokumenty bezpieczeństwa i jakości"
        influence: "Środki kontroli ryzyka definiują bezpieczeństwo urządzenia"

  - id: CLINICAL-EVALUATION-REPORT-*
    type: requires
    reason: "Raport oceny klinicznej jest wymagany przez MDR dla wszystkich urządzeń medycznych"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "Clinical Evaluation Report §9 Clinical Data Analysis"
        to: "§2 Raporty z testów zgodności"
        influence: "Dane kliniczne stanowią podstawę oceny zgodności z MDR"

  - id: QUALITY-MANAGEMENT-SYSTEM-*
    type: requires
    reason: "System zarządzania jakością (ISO 13485) jest wymagany przez MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "Quality Management System §4 QMS Documentation"
        to: "§3 Dokumenty bezpieczeństwa i jakości"
        influence: "Dokumentacja QMS ISO 13485 jest częścią dokumentacji jakości MDR"

  - id: USABILITY-ENGINEERING-FILE-*
    type: requires
    reason: "Dokumentacja użyteczności (IEC 62366) jest wymagana przez MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "Usability Engineering File §5 Use-Related Risk Analysis"
        to: "§3 Dokumenty bezpieczeństwa i jakości"
        influence: "Analiza ryzyk związanych z użytkowaniem jest częścią oceny bezpieczeństwa"

  - id: CONFORMITY-ASSESSMENT-*
    type: requires
    reason: "Ocena zgodności przez Notified Body jest wymagana dla większości urządzeń medycznych"
    conditions:
      - when: "project.device_class >= 'IIa'"
        applies: true
    sections:
      - from: "Conformity Assessment §6 Notified Body Opinion"
        to: "§4 Certyfikaty regulatorów"
        influence: "Opinia Notified Body jest wymagana do certyfikacji MDR"
```

### Impacts
```yaml
impacts:
  - id: CE-MARKING-DECLARATION-*
    type: blocks
    reason: "Deklaracja CE wymaga kompletnej dokumentacji technicznej MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
      - when: "project.region === 'EU'"
        applies: true
    sections:
      - from: "§1 Specyfikacje techniczne urządzenia"
        to: "CE Marking Declaration §3 Technical Documentation Reference"
        influence: "Specyfikacja techniczna jest podstawą deklaracji zgodności CE"
      - from: "§4 Certyfikaty regulatorów"
        to: "CE Marking Declaration §5 Notified Body Certification"
        influence: "Certyfikaty NB są wymagane w deklaracji CE"

  - id: MARKET-AUTHORIZATION-*
    type: blocks
    reason: "Autoryzacja rynkowa wymaga kompletnego MDR File"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "§1 Specyfikacje techniczne urządzenia"
        to: "Market Authorization §6 Device Description"
        influence: "Specyfikacja urządzenia stanowi podstawę autoryzacji rynkowej"
      - from: "§3 Dokumenty bezpieczeństwa i jakości"
        to: "Market Authorization §7 Safety Evidence"
        influence: "Dokumentacja bezpieczeństwa wspiera wniosek o autoryzację"

  - id: POST-MARKET-SURVEILLANCE-PLAN-*
    type: influences
    reason: "Plan nadzoru po wprowadzeniu do obrotu bazuje na danych z MDR File"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
    sections:
      - from: "§2 Raporty z testów zgodności"
        to: "Post-Market Surveillance Plan §8 Known Risks"
        influence: "Znane ryzyka z testów definiują zakres monitoringu PMS"

  - id: INSTRUCTIONS-FOR-USE-*
    type: influences
    reason: "Instrukcje obsługi bazują na specyfikacji technicznej i dokumentacji bezpieczeństwa"
    sections:
      - from: "§1 Specyfikacje techniczne urządzenia"
        to: "Instructions for Use §4 Device Specifications"
        influence: "Specyfikacje techniczne definiują parametry w instrukcji"
      - from: "§5 Instrukcje obsługi i utrzymania"
        to: "Instructions for Use §9 Maintenance Procedures"
        influence: "Procedury utrzymania są przekazywane użytkownikom końcowym"
```

### Related Documents
```yaml
related:
  - id: BIOCOMPATIBILITY-TEST-REPORT-*
    type: informs
    reason: "Testy biokompatybilności (ISO 10993) wspierają ocenę biologicznego bezpieczeństwa"
    conditions:
      - when: "project.device_contacts_patient === true"
        applies: true

  - id: STERILIZATION-VALIDATION-*
    type: informs
    reason: "Walidacja sterylizacji jest wymagana dla urządzeń sterylnych"
    conditions:
      - when: "project.device_sterile === true"
        applies: true

  - id: SOFTWARE-DOCUMENTATION-*
    type: informs
    reason: "Dokumentacja oprogramowania (IEC 62304) jest wymagana dla urządzeń z software"
    conditions:
      - when: "project.device_has_software === true"
        applies: true

  - id: VIGILANCE-REPORTING-*
    type: informs
    reason: "System vigilance raportuje incydenty związane z urządzeniem"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true

  - id: LABEL-ARTWORK-*
    type: informs
    reason: "Projekt etykiety musi być zgodny z wymaganiami MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-MDR-*.md"
    required: false
    purpose: "Tracking MDR compliance tasks and regulatory submission milestones"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-MDR-*.md"
    required: true
    purpose: "Test reports, clinical data, certificates, audit reports required by MDR"
    conditions:
      - when: "project.type === 'medical_device'"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-MDR-*.md"
    required: true
    purpose: "Definition of Ready for MDR submission - all technical documentation complete"

  - type: DoD
    path: "satellites/dod/DOD-MDR-*.md"
    required: true
    purpose: "Definition of Done for MDR compliance - CE marking and market authorization obtained"
```
