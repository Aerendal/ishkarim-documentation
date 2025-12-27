# 📄 Clinical Trial Documentation

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Cel biznesowy / techniczny
Dokumentacja badań klinicznych dla projektów medycznych. Zapewnia zgodność z regulacjami prawnymi i etycznymi.

## Zawartość
- Protokoły badań klinicznych
- Wyniki testów i obserwacji
- Formularze zgód pacjentów
- Raporty etyczne
- Procedury audytowe

## Czego nie zawiera
- Szczegółowych implementacji kodu
- Strategii marketingowych

## Objętość
- 10–30 stron
- Kilkanaście sekcji tematycznych

## Kategoria
- **Wymagane** (branżowe)

## Odbiorcy
- Zespoły R&D
- Regulatorzy
- Instytucje medyczne

## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: RESEARCH-PROTOCOL-*
    type: requires
    reason: "Protokół badawczy definiuje metodologię i procedury badania klinicznego"
    conditions:
      - when: "project.industry === 'healthcare'"
        applies: true
      - when: "project.type === 'clinical_research'"
        applies: true
    sections:
      - from: "Research Protocol §4 Study Design"
        to: "§1 Protokoły badań klinicznych"
        influence: "Design badania definiuje protokół kliniczny zgodny z GCP"
      - from: "Research Protocol §5 Patient Selection Criteria"
        to: "§1 Protokoły badań klinicznych"
        influence: "Kryteria włączenia/wyłączenia pacjentów są częścią protokołu klinicznego"

  - id: ETHICS-COMMITTEE-APPROVAL-*
    type: requires
    reason: "Zgoda komisji etyki jest wymagana przed rozpoczęciem badania klinicznego"
    conditions:
      - when: "project.type === 'clinical_research'"
        applies: true
    sections:
      - from: "Ethics Committee Approval §3 Ethical Considerations"
        to: "§4 Raporty etyczne"
        influence: "Decyzja komisji etyki definiuje ramy etyczne badania"

  - id: INFORMED-CONSENT-FORM-*
    type: requires
    reason: "Formularze zgody pacjenta są wymagane przez GCP i regulacje medyczne"
    conditions:
      - when: "project.involves_human_subjects === true"
        applies: true
    sections:
      - from: "Informed Consent Form §2 Patient Information"
        to: "§3 Formularze zgód pacjentów"
        influence: "Formularz zgody informuje pacjentów o procedurach badania"

  - id: REGULATORY-APPROVAL-*
    type: requires
    reason: "Zgoda regulatora (FDA/EMA) jest wymagana dla badań klinicznych leków/urządzeń"
    conditions:
      - when: "project.requires_regulatory_approval === true"
        applies: true
    sections:
      - from: "Regulatory Approval §5 IND/CTA Authorization"
        to: "§5 Procedury audytowe"
        influence: "Zgoda regulatora definiuje wymagania audytowe"

  - id: SAFETY-MONITORING-PLAN-*
    type: requires
    reason: "Plan monitoringu bezpieczeństwa definiuje procedury śledzenia zdarzeń niepożądanych"
    conditions:
      - when: "project.type === 'clinical_research'"
        applies: true
    sections:
      - from: "Safety Monitoring Plan §6 Adverse Event Reporting"
        to: "§2 Wyniki testów i obserwacji"
        influence: "Procedury raportowania AE są częścią dokumentacji wyników"
```

### Impacts
```yaml
impacts:
  - id: CLINICAL-STUDY-REPORT-*
    type: blocks
    reason: "Raport badania klinicznego wymaga kompletnej dokumentacji trial documentation"
    conditions:
      - when: "project.type === 'clinical_research'"
        applies: true
    sections:
      - from: "§1 Protokoły badań klinicznych"
        to: "Clinical Study Report §4 Study Methodology"
        influence: "Protokół definiuje metodologię raportowaną w CSR"
      - from: "§2 Wyniki testów i obserwacji"
        to: "Clinical Study Report §7 Study Results"
        influence: "Dane z obserwacji stanowią podstawę wyników w CSR"
      - from: "§4 Raporty etyczne"
        to: "Clinical Study Report §3 Ethics and Compliance"
        influence: "Status etyczny jest raportowany w CSR"

  - id: REGULATORY-SUBMISSION-*
    type: blocks
    reason: "Zgłoszenie regulacyjne (NDA/MAA) wymaga dokumentacji badań klinicznych"
    conditions:
      - when: "project.requires_regulatory_approval === true"
        applies: true
    sections:
      - from: "§1 Protokoły badań klinicznych"
        to: "Regulatory Submission §8 Clinical Data Package"
        influence: "Protokoły badań są częścią pakietu danych klinicznych"
      - from: "§2 Wyniki testów i obserwacji"
        to: "Regulatory Submission §9 Efficacy Data"
        influence: "Wyniki badań wspierają wniosek o rejestrację"

  - id: MEDICAL-DEVICE-FILE-*
    type: informs
    reason: "Dokumentacja badań klinicznych wspiera certyfikację urządzeń medycznych"
    conditions:
      - when: "project.involves_medical_device === true"
        applies: true
    sections:
      - from: "§2 Wyniki testów i obserwacji"
        to: "Medical Device File §12 Clinical Evaluation"
        influence: "Dane kliniczne są częścią oceny klinicznej urządzenia"

  - id: PUBLICATION-MANUSCRIPT-*
    type: informs
    reason: "Wyniki badań klinicznych są publikowane w literaturze medycznej"
    sections:
      - from: "§2 Wyniki testów i obserwacji"
        to: "Publication Manuscript §5 Results Section"
        influence: "Dane kliniczne stanowią podstawę publikacji naukowej"
```

### Related Documents
```yaml
related:
  - id: INVESTIGATOR-BROCHURE-*
    type: informs
    reason: "Broszura badacza dostarcza informacji o produkcie badanym"
    conditions:
      - when: "project.involves_investigational_product === true"
        applies: true

  - id: DATA-MANAGEMENT-PLAN-*
    type: informs
    reason: "Plan zarządzania danymi definiuje procedury zbierania i analizy danych klinicznych"
    conditions:
      - when: "project.type === 'clinical_research'"
        applies: true

  - id: STATISTICAL-ANALYSIS-PLAN-*
    type: informs
    reason: "Plan analizy statystycznej definiuje metodologię analizy wyników"
    conditions:
      - when: "project.type === 'clinical_research'"
        applies: true

  - id: PHARMACOVIGILANCE-PLAN-*
    type: informs
    reason: "Plan farmakovigilance definiuje monitoring bezpieczeństwa po zakończeniu badania"
    conditions:
      - when: "project.involves_drugs === true"
        applies: true
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CLINICAL-TRIAL-*.md"
    required: false
    purpose: "Tracking clinical trial milestones and regulatory deadlines"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CLINICAL-TRIAL-*.md"
    required: true
    purpose: "Source documents, CRFs, lab reports, consent forms required by GCP"
    conditions:
      - when: "project.type === 'clinical_research'"
        required: true

  - type: DoR
    path: "satellites/dor/DOR-CLINICAL-TRIAL-*.md"
    required: true
    purpose: "Definition of Ready for clinical trial - regulatory approvals and site preparation"

  - type: DoD
    path: "satellites/dod/DOD-CLINICAL-TRIAL-*.md"
    required: true
    purpose: "Definition of Done for clinical trial - data lock and CSR completion criteria"
```
