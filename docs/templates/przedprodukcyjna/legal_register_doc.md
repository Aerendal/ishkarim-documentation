# 📄 Legal & Regulatory Register

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
    reason: "Vision Document product scope określa applicable legal regulations"
    conditions:
      - when: "project.requires_compliance === true"
        applies: true
    sections:
      - from: "Vision §11 Opis docelowego kształtu produktu"
        to: "§13 Zakres zastosowania regulacji w projekcie"
        influence: "Product features definiują which regulations apply"

  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter scope i jurisdiction wpływają na regulatory requirements"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "Project Charter §13 Zakres wysokopoziomowy"
        to: "§11 Lista obowiązujących regulacji"
        influence: "Project scope identifies applicable regulations"

  - id: MARKET-ANALYSIS-*
    type: influences
    reason: "Market Analysis geographic markets definiują jurisdictional regulations"
    conditions:
      - when: "project.targets_multiple_jurisdictions === true"
        applies: true
    sections:
      - from: "Market Analysis §4 Geographic Markets"
        to: "§11 Lista obowiązujących regulacji"
        influence: "Target markets determine applicable legal frameworks"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: DPIA-*
    type: blocks
    reason: "DPIA wymaga Legal Register dla identification of privacy regulations"
    conditions:
      - when: "product.handles_personal_data === true"
        applies: true
    sections:
      - from: "§11 Lista obowiązujących regulacji"
        to: "DPIA §17 Plan monitorowania zgodności"
        influence: "Applicable privacy laws (GDPR, CCPA) definiują DPIA requirements"

  - id: ETHICS-AI-GUIDELINES-*
    type: informs
    reason: "Legal Register AI regulations informują Ethics & AI Guidelines"
    conditions:
      - when: "product.uses_ai === true && project.jurisdiction === 'EU'"
        applies: true
    sections:
      - from: "§11 Lista obowiązujących regulacji"
        to: "Ethics AI Guidelines §12 Zasady etycznego rozwoju i wdrożenia AI"
        influence: "EU AI Act requirements definiują minimum ethical standards"

  - id: IMPACT-ASSESSMENT-*
    type: blocks
    reason: "Impact Assessment regulatory compliance section wymaga Legal Register"
    sections:
      - from: "§11 Lista obowiązujących regulacji"
        to: "Impact Assessment §13 Zgodność z regulacjami prawnymi"
        influence: "Regulatory requirements są assessed dla compliance"
      - from: "§15 Status zgodności"
        to: "Impact Assessment §13 Zgodność z regulacjami prawnymi"
        influence: "Compliance status informs impact assessment"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Legal Register non-compliance risks są escalated do Risk Overview"
    conditions:
      - when: "legal.has_compliance_gaps === true"
        applies: true
    sections:
      - from: "§15 Status zgodności"
        to: "Risk Overview §8 Legal & Compliance Risks"
        influence: "Compliance gaps are identified jako legal risks"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "Legal Register może identify compliance training needs"
    sections:
      - from: "§14 Odpowiedzialne osoby/zespoły"
        to: "Training Plan §5 Compliance Training"
        influence: "Team compliance responsibilities definiują training requirements"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: PROCUREMENT-PLAN-*
    type: informs
    reason: "Procurement Plan vendor selection musi comply with regulatory requirements"

  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability regulations (ESG reporting) mogą be tracked w Legal Register"

  - id: PROJECT-MGMT-PLAN-*
    type: informs
    reason: "Project Management Plan governance musi align z legal requirements"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-LEGAL-*.md"
    required: false
    purpose: "Tracking compliance tasks, legal reviews, regulation updates monitoring"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-LEGAL-*.md"
    required: true
    purpose: "Legal opinions, compliance certificates, audit reports, regulation texts"

  - type: DoR
    path: "satellites/dor/DOR-LEGAL-*.md"
    required: true
    purpose: "Definition of Ready: project scope defined, jurisdictions identified, legal counsel consulted before Legal Register creation"

  - type: DoD
    path: "satellites/dod/DOD-LEGAL-*.md"
    required: true
    purpose: "Definition of Done: all applicable regulations identified, compliance status assessed, responsibilities assigned, legal counsel approved"
```

---

## Cel biznesowy / techniczny
Legal & Regulatory Register to rejestr przepisów prawnych i regulacji, które mają wpływ na projekt. Dokument wspiera zgodność z wymaganiami prawnymi.

## Zawartość
- Lista obowiązujących regulacji
- Daty wejścia w życie przepisów
- Zakres zastosowania regulacji w projekcie
- Odpowiedzialne osoby/zespoły
- Status zgodności

## Czego nie zawiera
- Kodów źródłowych
- Strategii biznesowych
- Ogólnych analiz marketingowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Zespół prawny
- Zarząd
- Project managerowie
