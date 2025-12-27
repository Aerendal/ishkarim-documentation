# 📄 Sustainability Report

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
    reason: "Vision Document product scope definiuje environmental impact assessment needs"
    conditions:
      - when: "project.has_environmental_impact === true"
        applies: true
    sections:
      - from: "Vision §11 Opis docelowego kształtu produktu"
        to: "§11 Analiza zużycia energii i zasobów"
        influence: "Product features definiują resource consumption patterns"

  - id: FEASIBILITY-STUDY-*
    type: influences
    reason: "Feasibility Study technical architecture wpływa na environmental footprint"
    sections:
      - from: "Feasibility Study §4 Technical Architecture"
        to: "§12 Ocena śladu węglowego"
        influence: "Infrastructure choices determine carbon footprint"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "Sustainability Report environmental data feeds into Impact Assessment"
    sections:
      - from: "§12 Ocena śladu węglowego"
        to: "Impact Assessment §12 Potencjalny wpływ ekologiczny"
        influence: "Carbon footprint analysis jest integrated w environmental impact assessment"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck może highlight sustainability credentials dla ESG investors"
    conditions:
      - when: "pitch.targets_esg_investors === true"
        applies: true
    sections:
      - from: "§16 Cele długoterminowej zrównoważoności"
        to: "Pitch Deck §20 ESG Commitment"
        influence: "Sustainability goals demonstrate ESG alignment"

  - id: PROCUREMENT-PLAN-*
    type: influences
    reason: "Sustainability goals mogą wpłynąć na vendor selection criteria"
    sections:
      - from: "§13 Polityki oszczędzania zasobów"
        to: "Procurement Plan §14 Kryteria wyboru dostawców"
        influence: "Sustainability policies add vendor sustainability requirements"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: LEGAL-REGISTER-*
    type: informs
    reason: "Environmental regulations mogą be tracked w Legal Register"

  - id: FINANCIAL-PLAN-*
    type: informs
    reason: "Sustainability investments wpływają na cost structure"

  - id: GTM-*
    type: informs
    reason: "Sustainability credentials mogą be part of value proposition"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SUSTAINABILITY-*.md"
    required: false
    purpose: "Tracking sustainability initiatives, carbon reduction tasks, ESG reporting"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SUSTAINABILITY-*.md"
    required: true
    purpose: "Carbon footprint calculations, energy audits, sustainability certificates, ESG compliance reports"

  - type: DoR
    path: "satellites/dor/DOR-SUSTAINABILITY-*.md"
    required: true
    purpose: "Definition of Ready: product scope defined, technical architecture known, environmental impact areas identified before Sustainability Report"

  - type: DoD
    path: "satellites/dod/DOD-SUSTAINABILITY-*.md"
    required: true
    purpose: "Definition of Done: all impact areas assessed, carbon footprint calculated, sustainability goals set, ESG reporting compliant"
```

---

## Cel biznesowy / techniczny
Sustainability Report ocenia wpływ projektu na środowisko i przedstawia strategie zrównoważonego rozwoju. Dokument zwiększa wiarygodność projektu w oczach inwestorów i regulatorów.

## Zawartość
- Analiza zużycia energii i zasobów
- Ocena śladu węglowego
- Polityki oszczędzania zasobów
- Plany redukcji odpadów
- Cele długoterminowej zrównoważoności
- Raportowanie zgodne ze standardami ESG

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów technicznych
- Strategii sprzedażowych

## Objętość
- 3–5 stron
- 6–8 punktów kluczowych

## Kategoria
- **Nice-to-Have** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy (ESG)
- Zarząd
- Regulatorzy
