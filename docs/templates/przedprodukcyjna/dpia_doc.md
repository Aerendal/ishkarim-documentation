# 📄 Data Privacy Impact Assessment (DPIA)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: VISION-*
    type: influences
    reason: "Vision Document określa product features które mogą wymagać data processing assessment"
    conditions:
      - when: "product.handles_personal_data === true"
        applies: true
      - when: "product.data_processing === 'minimal'"
        applies: false
    sections:
      - from: "Vision §11 Opis docelowego kształtu produktu"
        to: "§12 Opis procesów przetwarzania danych"
        influence: "Product description identyfikuje data processing workflows wymagające DPIA"

  - id: FEASIBILITY-STUDY-*
    type: influences
    reason: "Feasibility Study może identyfikować technical approaches wpływające na data processing"
    conditions:
      - when: "solution.involves_ai_ml === true"
        applies: true
    sections:
      - from: "Feasibility Study §4 Technical Architecture"
        to: "§13 Kategorie danych osobowych"
        influence: "Architecture definiuje types i volumes of personal data processing"

  - id: LEGAL-REGISTER-*
    type: requires
    reason: "Legal Register identyfikuje applicable privacy regulations (GDPR, CCPA, etc.)"
    conditions:
      - when: "project.jurisdiction === 'EU' || project.jurisdiction === 'US-CA'"
        applies: true
    sections:
      - from: "Legal Register §2 Applicable Privacy Laws"
        to: "§17 Plan monitorowania zgodności"
        influence: "Legal requirements definiują compliance monitoring requirements"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: RISK-OVERVIEW-*
    type: blocks
    reason: "DPIA identyfikuje privacy risks które muszą być included w overall Risk Overview"
    conditions:
      - when: "dpia.identifies_high_risks === true"
        applies: true
    sections:
      - from: "§14 Identyfikacja ryzyk dla prywatności"
        to: "Risk Overview §4 Privacy & Compliance Risks"
        influence: "Privacy risks z DPIA są escalated jako project-level risks"
      - from: "§16 Proponowane środki ograniczające ryzyko"
        to: "Risk Overview §5 Mitigation Strategies"
        influence: "Risk mitigation measures są incorporated w risk management plan"

  - id: LEGAL-REGISTER-*
    type: informs
    reason: "DPIA validation może identyfikować additional compliance requirements"
    sections:
      - from: "§17 Plan monitorowania zgodności"
        to: "Legal Register §3 Compliance Tracking"
        influence: "DPIA compliance plan feeds into legal compliance monitoring"

  - id: ETHICS-AI-GUIDELINES-*
    type: informs
    reason: "DPIA privacy findings informują ethical AI guidelines szczególnie dla data usage"
    conditions:
      - when: "product.uses_ai === true"
        applies: true
    sections:
      - from: "§14 Identyfikacja ryzyk dla prywatności"
        to: "Ethics AI Guidelines §4 Data Privacy & Consent"
        influence: "Privacy risks definiują ethical guardrails dla AI data usage"

  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "DPIA dostarcza privacy-specific impact analysis dla broader Impact Assessment"
    sections:
      - from: "§15 Ocena wpływu i prawdopodobieństwa"
        to: "Impact Assessment §3 Privacy Impact"
        influence: "DPIA privacy impact analysis jest integrated w overall impact assessment"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability Report może adresować data governance jako sustainability aspect"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "DPIA może identyfikować staff training needs dla privacy compliance"

  - id: PROCUREMENT-PLAN-*
    type: informs
    reason: "DPIA wpływa na vendor selection criteria (data processors compliance)"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-DPIA-*.md"
    required: false
    purpose: "Tracking DPIA assessment tasks and compliance remediation actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DPIA-*.md"
    required: true
    purpose: "Data flow diagrams, processing records, consent mechanisms documentation"

  - type: DoR
    path: "satellites/dor/DOR-DPIA-*.md"
    required: true
    purpose: "Definition of Ready: data processing inventory, legal requirements identified before DPIA"

  - type: DoD
    path: "satellites/dod/DOD-DPIA-*.md"
    required: true
    purpose: "Definition of Done: DPO reviewed, high risks mitigated, compliance plan approved"
```

---

## Cel biznesowy / techniczny
DPIA ocenia ryzyka związane z przetwarzaniem danych osobowych. Dokument pomaga zapewnić zgodność z regulacjami (np. RODO) i minimalizować zagrożenia dla prywatności użytkowników.

## Zawartość
- Opis procesów przetwarzania danych
- Kategorie danych osobowych
- Identyfikacja ryzyk dla prywatności
- Ocena wpływu i prawdopodobieństwa
- Proponowane środki ograniczające ryzyko
- Plan monitorowania zgodności

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów implementacyjnych
- Treści marketingowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Inspektor ochrony danych (DPO)
- Zarząd
- Zespół prawny
