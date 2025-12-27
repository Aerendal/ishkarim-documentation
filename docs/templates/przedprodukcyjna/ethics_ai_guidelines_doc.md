# 📄 Ethics & AI Guidelines

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
    reason: "Vision Document określa AI capabilities wymagające ethical guidelines"
    conditions:
      - when: "product.uses_ai === true"
        applies: true
      - when: "product.ai_scope === 'none'"
        applies: false
    sections:
      - from: "Vision §15 Potencjalne innowacje i nowe funkcje"
        to: "§12 Zasady etycznego rozwoju i wdrożenia AI"
        influence: "Planned AI features definiują scope of ethical considerations"

  - id: DPIA-*
    type: requires
    reason: "DPIA identyfikuje privacy risks które muszą być addressed w AI ethics guidelines"
    conditions:
      - when: "ai.processes_personal_data === true"
        applies: true
    sections:
      - from: "DPIA §14 Identyfikacja ryzyk dla prywatności"
        to: "§14 Wymagania dotyczące prywatności i ochrony danych"
        influence: "Privacy risks z DPIA definiują AI data handling guardrails"
      - from: "DPIA §13 Kategorie danych osobowych"
        to: "§14 Wymagania dotyczące prywatności i ochrony danych"
        influence: "Data categories określają sensitivity levels dla AI processing"

  - id: LEGAL-REGISTER-*
    type: influences
    reason: "Legal Register identyfikuje AI-specific regulations (EU AI Act, etc.)"
    conditions:
      - when: "project.jurisdiction === 'EU'"
        applies: true
    sections:
      - from: "Legal Register §4 AI-Specific Regulations"
        to: "§12 Zasady etycznego rozwoju i wdrożenia AI"
        influence: "Legal requirements definiują minimum ethical standards dla AI"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: RESEARCH-PLAN-*
    type: blocks
    reason: "Research Plan dla AI development wymaga ethical guidelines jako framework"
    conditions:
      - when: "research.involves_ai === true"
        applies: true
    sections:
      - from: "§13 Polityki dotyczące unikania biasu"
        to: "Research Plan §5 Bias Testing Methodology"
        influence: "Bias policies definiują research testing requirements"
      - from: "§15 Procedury audytów etycznych"
        to: "Research Plan §6 Ethics Review Process"
        influence: "Audit procedures są embedded w research workflow"

  - id: TRAINING-PLAN-*
    type: blocks
    reason: "Training Plan musi include AI ethics training dla team members"
    conditions:
      - when: "team.works_with_ai === true"
        applies: true
    sections:
      - from: "§12 Zasady etycznego rozwoju i wdrożenia AI"
        to: "Training Plan §4 AI Ethics Training"
        influence: "Ethical principles wymagają team education i onboarding"
      - from: "§16 Odpowiedzialności zespołu"
        to: "Training Plan §2 Role-Based Training"
        influence: "Team responsibilities definiują training needs per role"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Ethics Guidelines identyfikują ethical risks dla AI usage"
    sections:
      - from: "§13 Polityki dotyczące unikania biasu"
        to: "Risk Overview §6 Ethical & Reputational Risks"
        influence: "Bias risks są escalated jako project-level risks"
      - from: "§14 Zasady przejrzystości i wyjaśnialności"
        to: "Risk Overview §6 Ethical & Reputational Risks"
        influence: "Transparency gaps are identified jako reputation risks"

  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "Ethics Guidelines informują broader social impact assessment"
    sections:
      - from: "§12 Zasady etycznego rozwoju i wdrożenia AI"
        to: "Impact Assessment §4 Ethical & Social Impact"
        influence: "Ethical principles frame social impact evaluation"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability Report może adresować AI environmental impact (energy usage)"

  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility Study technical architecture musi align z ethical constraints"

  - id: INNOVATION-LOG-*
    type: informs
    reason: "Innovation Log dokumentuje AI innovations wymagające ethical review"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ETHICS-AI-*.md"
    required: false
    purpose: "Tracking ethics review tasks and policy implementation"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ETHICS-AI-*.md"
    required: true
    purpose: "Bias testing results, audit reports, explainability documentation"

  - type: DoR
    path: "satellites/dor/DOR-ETHICS-AI-*.md"
    required: true
    purpose: "Definition of Ready: AI use cases identified, DPIA completed before ethics guidelines creation"

  - type: DoD
    path: "satellites/dod/DOD-ETHICS-AI-*.md"
    required: true
    purpose: "Definition of Done: ethics committee reviewed, audit procedures tested, team trained"
```

---

## Cel biznesowy / techniczny
Ethics & AI Guidelines definiują zasady etyczne i odpowiedzialnego użycia sztucznej inteligencji w projekcie. Dokument zwiększa transparentność i ogranicza ryzyka związane z AI.

## Zawartość
- Zasady etycznego rozwoju i wdrożenia AI
- Polityki dotyczące unikania biasu
- Zasady przejrzystości i wyjaśnialności
- Wymagania dotyczące prywatności i ochrony danych
- Procedury audytów etycznych
- Odpowiedzialności zespołu

## Czego nie zawiera
- Kodów źródłowych
- Technicznych diagramów
- Strategii sprzedażowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Zarząd
- Zespół AI / Data Science
- Zespół prawny i etyczny
