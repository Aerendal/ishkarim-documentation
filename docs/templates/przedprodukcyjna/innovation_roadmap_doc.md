# 📄 Innovation Roadmap

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
    reason: "Vision Document definiuje strategic direction i long-term roadmap wymagane dla Innovation Roadmap"
    conditions:
      - when: "project.has_innovation_focus === true"
        applies: true
    sections:
      - from: "Vision §14 Długofalowa roadmapa rozwoju"
        to: "§15 Orientacyjny harmonogram eksploracji"
        influence: "Vision roadmap definiuje high-level timeline dla innovation exploration"
      - from: "Vision §15 Potencjalne innowacje i nowe funkcje"
        to: "§11 Obszary potencjalnych innowacji"
        influence: "Vision innovation areas są expanded w Innovation Roadmap"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis identyfikuje market trends i technology trends dla innovation planning"
    conditions:
      - when: "project.is_market_driven === true"
        applies: true
    sections:
      - from: "Market Analysis §8 Technology Trends"
        to: "§12 Technologie do zbadania"
        influence: "Market technology trends definiują technology exploration priorities"
      - from: "Market Analysis §9 Future Market Opportunities"
        to: "§13 Trendy rynkowe i technologiczne"
        influence: "Market opportunities informują innovation focus areas"

  - id: INNOVATION-LOG-*
    type: influences
    reason: "Innovation Log validated ideas mogą inform Innovation Roadmap"
    sections:
      - from: "Innovation Log §15 Wnioski i rekomendacje"
        to: "§14 Propozycje eksperymentów"
        influence: "Innovation learnings definiują future experiment proposals"

  - id: RESEARCH-PLAN-*
    type: influences
    reason: "Research Plan findings mogą identify innovation opportunities"
    conditions:
      - when: "research.explores_new_tech === true"
        applies: true
    sections:
      - from: "Research Plan §7 Expected Outcomes"
        to: "§11 Obszary potencjalnych innowacji"
        influence: "Research outcomes reveal new innovation areas"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: RESEARCH-PLAN-*
    type: blocks
    reason: "Research Plan dla innovation exploration wymaga Innovation Roadmap jako framework"
    conditions:
      - when: "roadmap.includes_research === true"
        applies: true
    sections:
      - from: "§14 Propozycje eksperymentów"
        to: "Research Plan §3 Methodology"
        influence: "Experiment proposals są formalized w research methodology"
      - from: "§12 Technologie do zbadania"
        to: "Research Plan §2 Research Questions"
        influence: "Technology exploration areas definiują research questions"

  - id: FINANCIAL-PLAN-*
    type: influences
    reason: "Innovation Roadmap wpływa na R&D budget allocation w Financial Plan"
    sections:
      - from: "§15 Orientacyjny harmonogram eksploracji"
        to: "Financial Plan §16 Cash flow"
        influence: "Innovation timeline wpływa na phased R&D investments"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck może highlight innovation roadmap jako competitive advantage"
    conditions:
      - when: "project.seeks_innovation_funding === true"
        applies: true
    sections:
      - from: "§13 Trendy rynkowe i technologiczne"
        to: "Pitch Deck §12 Innovation Strategy"
        influence: "Technology trends demonstrate innovation potential"

  - id: VISION-*
    type: influences
    reason: "Innovation Roadmap learnings mogą evolve Vision Document"
    sections:
      - from: "§11 Obszary potencjalnych innowacji"
        to: "Vision §15 Potencjalne innowacje i nowe funkcje"
        influence: "Validated innovation areas update vision planning"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: ETHICS-AI-GUIDELINES-*
    type: informs
    reason: "AI innovations on roadmap wymagają ethical guidelines"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "New technologies on roadmap mogą wymagać team training"

  - id: GO-TO-MARKET-*
    type: informs
    reason: "Innovation timeline wpływa na product launch planning"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-ROADMAP-*.md"
    required: false
    purpose: "Tracking innovation exploration tasks and experiment execution"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ROADMAP-*.md"
    required: false
    purpose: "Technology research, proof of concepts, competitive innovation analysis"

  - type: DoR
    path: "satellites/dor/DOR-ROADMAP-*.md"
    required: true
    purpose: "Definition of Ready: vision defined, market trends analyzed, innovation areas identified before roadmap creation"
```

---

## Cel biznesowy / techniczny
Innovation Roadmap pokazuje potencjalne kierunki innowacyjnych działań badawczo-rozwojowych związanych z projektem. Dokument ma charakter inspiracyjny i strategiczny, wskazuje obszary rozwoju wykraczające poza podstawowy zakres projektu.

## Zawartość
- Obszary potencjalnych innowacji
- Technologie do zbadania
- Trendy rynkowe i technologiczne
- Propozycje eksperymentów
- Orientacyjny harmonogram eksploracji

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów implementacyjnych
- Backlogów sprintowych

## Objętość
- 2–3 strony
- 5–6 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Zarząd
- Zespół R&D
- Inwestorzy innowacyjni
