# 📄 Pitch Deck (Inwestorski)

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
    reason: "Vision Document dostarcza strategic narrative i product vision wymagane dla Pitch Deck"
    conditions:
      - when: "project.seeks_funding === true"
        applies: true
    sections:
      - from: "Vision §11 Opis docelowego kształtu produktu"
        to: "§12 Nasze rozwiązanie i przewaga konkurencyjna"
        influence: "Product vision definiuje value proposition dla investors"
      - from: "Vision §14 Długofalowa roadmapa rozwoju"
        to: "§16 Roadmap rozwoju"
        influence: "Vision roadmap jest visualized jako product timeline"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis dostarcza market data kluczowego dla investor pitch"
    sections:
      - from: "Market Analysis §11 Wielkość rynku (TAM, SAM, SOM)"
        to: "§13 Potencjał rynku (TAM, SAM, SOM)"
        influence: "Market size data demonstrates investment opportunity size"
      - from: "Market Analysis §13 Kluczowi gracze i analiza konkurencji"
        to: "§12 Nasze rozwiązanie i przewaga konkurencyjna"
        influence: "Competitive landscape validates competitive advantage claims"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case dostarcza business model i financial justification"
    sections:
      - from: "Business Case §15 Model biznesowy"
        to: "§14 Model biznesowy"
        influence: "Business model definiuje revenue generation strategy"

  - id: FINANCIAL-PLAN-*
    type: requires
    reason: "Financial Plan dostarcza financial projections dla investor presentation"
    conditions:
      - when: "pitch.includes_financials === true"
        applies: true
    sections:
      - from: "Financial Plan §11 Prognozy przychodów"
        to: "§17 Wstępne dane finansowe"
        influence: "Revenue projections są visualized dla investors"
      - from: "Financial Plan §16 Cash flow"
        to: "§17 Wstępne dane finansowe"
        influence: "Cash flow projections demonstrate financial sustainability"

  - id: GTM-*
    type: influences
    reason: "Go-to-Market Strategy informuje market entry approach w pitch"
    sections:
      - from: "GTM §11 Definicja grupy docelowej"
        to: "§13 Potencjał rynku (TAM, SAM, SOM)"
        influence: "Target customer definition sharpens market opportunity story"
      - from: "GTM §16 Harmonogram wejścia na rynek"
        to: "§16 Roadmap rozwoju"
        influence: "GTM timeline integrates z product roadmap"

  - id: IMPACT-ASSESSMENT-*
    type: influences
    reason: "Impact Assessment social impact może strengthen pitch dla impact investors"
    conditions:
      - when: "pitch.targets_impact_investors === true"
        applies: true
    sections:
      - from: "Impact Assessment §11 Analiza wpływu społecznego"
        to: "§18 Social Impact"
        influence: "Social impact metrics appeal do impact investors"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: EXEC-SUMMARY-*
    type: influences
    reason: "Pitch Deck narrative może inform Executive Summary storytelling"
    sections:
      - from: "§12 Nasze rozwiązanie i przewaga konkurencyjna"
        to: "Executive Summary §15 Nasze rozwiązanie"
        influence: "Pitch value proposition refines executive messaging"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: INNOVATION-ROADMAP-*
    type: informs
    reason: "Innovation Roadmap może enhance pitch future vision narrative"

  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability credentials mogą be pitched jako competitive differentiator"

  - id: PROJECT-CHARTER-*
    type: informs
    reason: "Project Charter team structure może inform pitch team slide"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PITCH-*.md"
    required: false
    purpose: "Tracking pitch deck iterations, investor feedback incorporation, presentation preparation"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PITCH-*.md"
    required: true
    purpose: "Visual assets, data sources, customer testimonials, demo videos, investor questions/answers"

  - type: DoR
    path: "satellites/dor/DOR-PITCH-*.md"
    required: true
    purpose: "Definition of Ready: vision defined, market analyzed, financials prepared, team assembled before Pitch Deck creation"

  - type: DoD
    path: "satellites/dod/DOD-PITCH-*.md"
    required: true
    purpose: "Definition of Done: deck designed, data validated, story tested, team rehearsed, investor feedback incorporated"
```

---

## Cel biznesowy / techniczny
Pitch Deck ma za zadanie przekonać inwestorów do projektu w krótkiej, wizualnej formie. To narzędzie sprzedażowe, a nie techniczne – ma budzić zainteresowanie i ułatwiać rozmowę.

## Zawartość
- Problem, który rozwiązujemy
- Nasze rozwiązanie i przewaga konkurencyjna
- Potencjał rynku (TAM, SAM, SOM)
- Model biznesowy
- Zespół i doświadczenie
- Roadmap rozwoju
- Wstępne dane finansowe

## Czego nie zawiera
- Szczegółowej architektury systemu
- Kodów źródłowych
- Technicznych opisów API

## Objętość
- 10–15 slajdów
- 1 punkt / slajd (hasłowo)

## Kategoria
- **Wymagane** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy VC i aniołowie biznesu
- Partnerzy strategiczni
- Grantodawcy
