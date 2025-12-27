# 📄 Impact Assessment

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: VISION-*
    type: requires
    reason: "Vision Document definiuje product scope i strategic goals wymagane dla impact assessment"
    conditions:
      - when: "project.requires_impact_assessment === true"
        applies: true
    sections:
      - from: "Vision §11 Opis docelowego kształtu produktu"
        to: "§11 Analiza wpływu społecznego"
        influence: "Product features definiują potential social impact areas"
      - from: "Vision §16 Wizja pozycji rynkowej"
        to: "§11 Analiza wpływu społecznego"
        influence: "Market positioning strategy wpływa na societal influence"

  - id: DPIA-*
    type: requires
    reason: "DPIA dostarcza privacy impact analysis jako input dla broader Impact Assessment"
    conditions:
      - when: "product.handles_personal_data === true"
        applies: true
    sections:
      - from: "DPIA §14 Identyfikacja ryzyk dla prywatności"
        to: "§14 Ryzyka etyczne"
        influence: "Privacy risks są component of ethical risk assessment"

  - id: ETHICS-AI-GUIDELINES-*
    type: influences
    reason: "Ethics & AI Guidelines informują ethical impact evaluation"
    conditions:
      - when: "product.uses_ai === true"
        applies: true
    sections:
      - from: "Ethics AI Guidelines §12 Zasady etycznego rozwoju i wdrożenia AI"
        to: "§14 Ryzyka etyczne"
        influence: "Ethical principles definiują ethical risk evaluation framework"

  - id: SUSTAINABILITY-REPORT-*
    type: influences
    reason: "Sustainability Report dostarcza environmental impact data"
    conditions:
      - when: "project.has_environmental_impact === true"
        applies: true
    sections:
      - from: "Sustainability Report §3 Environmental Impact"
        to: "§12 Potencjalny wpływ ekologiczny"
        influence: "Environmental analysis feeds into impact assessment"

  - id: LEGAL-REGISTER-*
    type: requires
    reason: "Legal Register identyfikuje regulatory compliance requirements"
    sections:
      - from: "Legal Register §2 Applicable Regulations"
        to: "§13 Zgodność z regulacjami prawnymi"
        influence: "Legal requirements definiują compliance assessment scope"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Impact Assessment identyfikuje impact-related risks dla Risk Overview"
    sections:
      - from: "§14 Ryzyka etyczne"
        to: "Risk Overview §6 Ethical & Reputational Risks"
        influence: "Ethical risks są escalated jako project-level risks"
      - from: "§12 Potencjalny wpływ ekologiczny"
        to: "Risk Overview §7 Environmental Risks"
        influence: "Environmental impact risks informują risk management"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary może highlight positive impacts dla stakeholders"
    conditions:
      - when: "impact.is_positive === true"
        applies: true
    sections:
      - from: "§11 Analiza wpływu społecznego"
        to: "Executive Summary §19 Social Impact"
        influence: "Positive social impact jest komunikowany jako value proposition"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck dla impact investors wymaga impact metrics"
    conditions:
      - when: "project.seeks_impact_funding === true"
        applies: true
    sections:
      - from: "§11 Analiza wpływu społecznego"
        to: "Pitch Deck §11 Impact Metrics"
        influence: "Social impact metrics są prezentowane impact investors"

  - id: SUSTAINABILITY-REPORT-*
    type: influences
    reason: "Impact Assessment findings mogą wpłynąć na sustainability initiatives"
    sections:
      - from: "§15 Proponowane środki minimalizacji negatywnego wpływu"
        to: "Sustainability Report §5 Mitigation Strategies"
        influence: "Impact mitigation measures są incorporated w sustainability plan"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: MARKET-ANALYSIS-*
    type: informs
    reason: "Market Analysis może identify market-driven social impacts"

  - id: STAKEHOLDER-MAP-*
    type: informs
    reason: "Stakeholder Map identyfikuje impacted stakeholder groups"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "Impact Assessment może identify training needs dla impact mitigation"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-IMPACT-*.md"
    required: false
    purpose: "Tracking impact assessment tasks and mitigation action items"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-IMPACT-*.md"
    required: true
    purpose: "Impact studies, stakeholder consultations, environmental assessments, ethical review reports"

  - type: DoR
    path: "satellites/dor/DOR-IMPACT-*.md"
    required: true
    purpose: "Definition of Ready: product scope defined, stakeholders identified, regulatory requirements understood before Impact Assessment"

  - type: DoD
    path: "satellites/dod/DOD-IMPACT-*.md"
    required: true
    purpose: "Definition of Done: all impact areas assessed, mitigation strategies defined, stakeholders consulted, regulatory compliance verified"
```

---

## Cel biznesowy / techniczny
Impact Assessment ocenia wpływ projektu na otoczenie – społeczny, środowiskowy, regulacyjny i etyczny. Dokument zwiększa wiarygodność projektu w oczach inwestorów i regulatorów.

## Zawartość
- Analiza wpływu społecznego
- Potencjalny wpływ ekologiczny
- Zgodność z regulacjami prawnymi
- Ryzyka etyczne
- Proponowane środki minimalizacji negatywnego wpływu

## Czego nie zawiera
- Szczegółowych prognoz finansowych
- Kodów źródłowych
- Technicznych detali architektury

## Objętość
- 2–4 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy (ESG, impact investing)
- Regulatorzy
- Partnerzy strategiczni
