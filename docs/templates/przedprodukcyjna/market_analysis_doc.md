# 📄 Market Analysis

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
    reason: "Vision Document product positioning wpływa na market analysis scope"
    conditions:
      - when: "project.targets_market === true"
        applies: true
    sections:
      - from: "Vision §16 Wizja pozycji rynkowej"
        to: "§15 Pozycjonowanie naszego rozwiązania"
        influence: "Vision market positioning guides competitive positioning analysis"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: BIZ-CASE-*
    type: blocks
    reason: "Business Case wymaga Market Analysis data dla market opportunity validation"
    conditions:
      - when: "project.requires_business_case === true"
        applies: true
    sections:
      - from: "§11 Wielkość rynku (TAM, SAM, SOM)"
        to: "Business Case §13 Analiza rynku docelowego"
        influence: "Market size data validates business opportunity"
      - from: "§13 Kluczowi gracze i analiza konkurencji"
        to: "Business Case §14 Uzasadnienie wyboru projektu"
        influence: "Competitive analysis justifies competitive advantage claims"

  - id: FINANCIAL-PLAN-*
    type: blocks
    reason: "Financial Plan revenue projections wymaga Market Analysis market size data"
    conditions:
      - when: "project.has_revenue_model === true"
        applies: true
    sections:
      - from: "§11 Wielkość rynku (TAM, SAM, SOM)"
        to: "Financial Plan §11 Prognozy przychodów"
        influence: "Market size definiuje addressable market dla revenue forecasts"
      - from: "§12 Dynamika wzrostu i trendy"
        to: "Financial Plan §15 Scenariusze pesymistyczny, realistyczny, optymistyczny"
        influence: "Market growth trends inform revenue scenario planning"

  - id: GTM-*
    type: blocks
    reason: "Go-to-Market Strategy wymaga Market Analysis dla target segment definition"
    sections:
      - from: "§14 Segmentacja klientów"
        to: "GTM §11 Definicja grupy docelowej"
        influence: "Customer segmentation definiuje target customer groups"
      - from: "§13 Kluczowi gracze i analiza konkurencji"
        to: "GTM §13 Strategia cenowa (pricing)"
        influence: "Competitive analysis informuje pricing strategy"

  - id: ROADMAP-*
    type: informs
    reason: "Market Analysis technology trends informują Innovation Roadmap"
    sections:
      - from: "§12 Dynamika wzrostu i trendy"
        to: "Innovation Roadmap §13 Trendy rynkowe i technologiczne"
        influence: "Market trends identify innovation opportunities"

  - id: PITCH-DECK-*
    type: blocks
    reason: "Pitch Deck visualization wymaga Market Analysis market data"
    conditions:
      - when: "project.seeks_funding === true"
        applies: true
    sections:
      - from: "§11 Wielkość rynku (TAM, SAM, SOM)"
        to: "Pitch Deck §3 Market Opportunity"
        influence: "Market size data demonstrates investment opportunity"
      - from: "§13 Kluczowi gracze i analiza konkurencji"
        to: "Pitch Deck §4 Competitive Landscape"
        influence: "Competitive analysis shows market positioning"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary highlights market opportunity z Market Analysis"
    sections:
      - from: "§11 Wielkość rynku (TAM, SAM, SOM)"
        to: "Executive Summary §14 Opportunity"
        influence: "Market size komunikuje business potential"

  - id: CBA-*
    type: influences
    reason: "Market Analysis market opportunity wpływa na CBA benefit calculations"
    sections:
      - from: "§11 Wielkość rynku (TAM, SAM, SOM)"
        to: "CBA §14 Analiza scenariuszowa"
        influence: "Market size informs optimistic/realistic revenue scenarios"

  - id: LEGAL-REGISTER-*
    type: influences
    reason: "Market Analysis geographic markets wpływają na regulatory requirements"
    conditions:
      - when: "analysis.covers_multiple_jurisdictions === true"
        applies: true
    sections:
      - from: "§14 Segmentacja klientów"
        to: "Legal Register §11 Lista obowiązujących regulacji"
        influence: "Geographic segments determine applicable jurisdictional regulations"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility Study technical viability complements Market Analysis market viability"

  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "Market Analysis może identify market-driven social impacts"

  - id: INNOVATION-LOG-*
    type: informs
    reason: "Market trends mogą inspirować logged innovations"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-MARKET-*.md"
    required: false
    purpose: "Tracking market research tasks, competitor analysis, customer interviews"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-MARKET-*.md"
    required: true
    purpose: "Market research reports, industry data, competitive intelligence, customer surveys, analyst reports"

  - type: DoR
    path: "satellites/dor/DOR-MARKET-*.md"
    required: true
    purpose: "Definition of Ready: product concept defined, target market hypothesized, research methodology planned before Market Analysis"

  - type: DoD
    path: "satellites/dod/DOD-MARKET-*.md"
    required: true
    purpose: "Definition of Done: TAM/SAM/SOM calculated, competitors analyzed, segments validated, positioning defined"
```

---

## Cel biznesowy / techniczny
Market Analysis pozwala ocenić potencjał rynkowy projektu. Dokument wykorzystywany jest do zrozumienia trendów, konkurencji oraz pozycjonowania produktu.

## Zawartość
- Wielkość rynku (TAM, SAM, SOM)
- Dynamika wzrostu i trendy
- Kluczowi gracze i analiza konkurencji
- Segmentacja klientów
- Pozycjonowanie naszego rozwiązania
- Potencjalne bariery wejścia

## Czego nie zawiera
- Kodów źródłowych
- Technicznych formuł matematycznych
- Backlogów projektowych

## Objętość
- 5–7 stron
- 6–10 punktów kluczowych

## Kategoria
- **Wymagane** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd i dział strategii
- Zespół produktowy
