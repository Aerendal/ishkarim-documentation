# 📄 Go-To-Market Strategy

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis identyfikuje target segments i competitive landscape wymagane dla GTM strategy"
    conditions:
      - when: "product.has_market_strategy === true"
        applies: true
    sections:
      - from: "Market Analysis §5 Analiza rynku docelowego"
        to: "§11 Definicja grupy docelowej"
        influence: "Market segmentation definiuje target customer groups dla GTM"
      - from: "Market Analysis §7 Competitive Analysis"
        to: "§13 Strategia cenowa (pricing)"
        influence: "Competitive pricing landscape informuje pricing strategy"

  - id: VISION-*
    type: requires
    reason: "Vision Document definiuje product value proposition potrzebny dla GTM messaging"
    sections:
      - from: "Vision §16 Wizja pozycji rynkowej"
        to: "§15 Plan marketingowy"
        influence: "Market positioning vision definiuje marketing messaging i channels"

  - id: BIZ-CASE-*
    type: influences
    reason: "Business Case revenue model wpływa na GTM strategy i pricing"
    conditions:
      - when: "project.seeks_profitability === true"
        applies: true
    sections:
      - from: "Business Case §16 Prognozy finansowe"
        to: "§13 Strategia cenowa (pricing)"
        influence: "Revenue targets informują pricing decisions"

  - id: FINANCIAL-PLAN-*
    type: influences
    reason: "Financial Plan marketing budget constraints wpływają na GTM execution"
    sections:
      - from: "Financial Plan §12 Struktura kosztów (CAPEX, OPEX)"
        to: "§15 Plan marketingowy"
        influence: "Marketing budget allocation definiuje scope of marketing activities"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck visualization wymaga GTM strategy jako key component dla investors"
    conditions:
      - when: "project.seeks_funding === true"
        applies: true
    sections:
      - from: "§11 Definicja grupy docelowej"
        to: "Pitch Deck §5 Target Market"
        influence: "Target customer definition jest prezentowana investors"
      - from: "§12 Kanały sprzedaży i dystrybucji"
        to: "Pitch Deck §9 Go-to-Market Strategy"
        influence: "Distribution channels demonstrują market access plan"
      - from: "§16 Harmonogram wejścia na rynek"
        to: "Pitch Deck §10 Timeline"
        influence: "Launch timeline pokazuje execution roadmap"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary includes GTM highlights dla decision makers"
    sections:
      - from: "§13 Strategia cenowa (pricing)"
        to: "Executive Summary §16 Strategia finansowa"
        influence: "Pricing strategy is key component of financial strategy"

  - id: COMMUNICATION-PLAN-*
    type: influences
    reason: "GTM external communication strategy wpływa na overall Communication Plan"
    sections:
      - from: "§15 Plan marketingowy"
        to: "Communication Plan §13 Kanały komunikacji"
        influence: "Marketing channels mogą overlapping z project communication channels"

  - id: ROADMAP-*
    type: influences
    reason: "GTM timeline wpływa na product development roadmap priorities"
    sections:
      - from: "§16 Harmonogram wejścia na rynek"
        to: "Innovation Roadmap §3 Timeline i Milestones"
        influence: "Market launch dates definiują product readiness deadlines"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: INNOVATION-LOG-*
    type: informs
    reason: "Innovation Log może capture GTM experiments i learnings"

  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability credentials mogą be part of GTM value proposition"

  - id: STAKEHOLDER-MAP-*
    type: informs
    reason: "Stakeholder Map identyfikuje distribution partners i strategic allies"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-GTM-*.md"
    required: false
    purpose: "Tracking GTM execution tasks, partner outreach, campaign launches"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-GTM-*.md"
    required: true
    purpose: "Market research validation, pricing analysis, partnership agreements, campaign performance data"

  - type: DoR
    path: "satellites/dor/DOR-GTM-*.md"
    required: true
    purpose: "Definition of Ready: market analysis completed, product positioning defined, target segments identified before GTM strategy creation"

  - type: DoD
    path: "satellites/dod/DOD-GTM-*.md"
    required: true
    purpose: "Definition of Done: pricing validated, distribution channels established, marketing plan approved, launch timeline confirmed"
```

---

## Cel biznesowy / techniczny
Go-To-Market Strategy (GTM) określa, w jaki sposób produkt zostanie wprowadzony na rynek, jakie kanały dystrybucji i modele sprzedaży zostaną wykorzystane. Jest kluczowym dokumentem dla inwestorów i zespołu sprzedażowego.

## Zawartość
- Definicja grupy docelowej
- Kanały sprzedaży i dystrybucji
- Strategia cenowa (pricing)
- Partnerstwa i alianse strategiczne
- Plan marketingowy (wysokopoziomowy)
- Harmonogram wejścia na rynek

## Czego nie zawiera
- Specyfikacji kodu
- Detali technicznych wdrożenia
- Backlogów sprintowych

## Objętość
- 4–6 stron
- 8–10 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd i dział sprzedaży
- Zespół marketingowy
