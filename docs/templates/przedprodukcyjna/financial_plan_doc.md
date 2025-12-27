# 📄 Financial Plan / Projections

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case dostarcza initial financial assumptions wymagane do szczegółowego Financial Plan"
    conditions:
      - when: "project.requires_investment === true"
        applies: true
    sections:
      - from: "Business Case §16 Prognozy finansowe"
        to: "§11 Prognozy przychodów"
        influence: "High-level revenue projections z Business Case są refined w Financial Plan"
      - from: "Business Case §17 Plan osiągnięcia ROI"
        to: "§14 Punkt rentowności"
        influence: "ROI targets definiują break-even expectations"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis dostarcza market size i pricing assumptions dla revenue projections"
    conditions:
      - when: "project.has_revenue_model === true"
        applies: true
    sections:
      - from: "Market Analysis §5 Analiza rynku docelowego"
        to: "§11 Prognozy przychodów"
        influence: "Market size definiuje addressable market dla revenue forecasts"
      - from: "Market Analysis §6 Competitive Pricing"
        to: "§15 Scenariusze pesymistyczny, realistyczny, optymistyczny"
        influence: "Competitive pricing informuje pricing assumptions w scenarios"

  - id: PROJECT-CHARTER-*
    type: influences
    reason: "Project Charter definiuje high-level budget constraints dla Financial Plan"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "Project Charter §17 Budżet wysokopoziomowy"
        to: "§12 Struktura kosztów (CAPEX, OPEX)"
        influence: "High-level budget z Charter jest decomposed w detailed cost structure"

  - id: ROADMAP-*
    type: influences
    reason: "Innovation Roadmap timeline wpływa na phased investment i revenue timeline"
    sections:
      - from: "Innovation Roadmap §3 Timeline i Milestones"
        to: "§16 Cash flow"
        influence: "Roadmap milestones definiują timing of costs i revenues"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: CBA-*
    type: blocks
    reason: "CBA wymaga detailed Financial Plan jako input dla cost-benefit calculations"
    conditions:
      - when: "project.requires_cba === true"
        applies: true
    sections:
      - from: "§12 Struktura kosztów (CAPEX, OPEX)"
        to: "CBA §11 Koszty bezpośrednie i pośrednie"
        influence: "Detailed cost structure feeds into CBA cost analysis"
      - from: "§11 Prognozy przychodów"
        to: "CBA §12 Oczekiwane przychody"
        influence: "Revenue projections inform CBA benefit calculations"
      - from: "§15 Scenariusze pesymistyczny, realistyczny, optymistyczny"
        to: "CBA §14 Analiza scenariuszowa"
        influence: "Financial scenarios są adopted w CBA scenario analysis"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary prezentuje key financial highlights z Financial Plan"
    sections:
      - from: "§13 Marże brutto i netto"
        to: "Executive Summary §16 Strategia finansowa"
        influence: "Margin projections są summarized dla executive audience"
      - from: "§14 Punkt rentowności"
        to: "Executive Summary §16 Strategia finansowa"
        influence: "Break-even analysis komunikuje financial viability"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck visualization wymaga financial data z Financial Plan"
    conditions:
      - when: "project.seeks_funding === true"
        applies: true
    sections:
      - from: "§11 Prognozy przychodów"
        to: "Pitch Deck §8 Financial Projections"
        influence: "Revenue projections są visualized dla investors"
      - from: "§16 Cash flow"
        to: "Pitch Deck §8 Financial Projections"
        influence: "Cash flow projections demonstrate financial sustainability"

  - id: PROCUREMENT-PLAN-*
    type: influences
    reason: "Financial Plan budget constraints wpływają na procurement decisions"
    sections:
      - from: "§12 Struktura kosztów (CAPEX, OPEX)"
        to: "Procurement Plan §4 Budget Allocation"
        influence: "Cost structure definiuje procurement budgets per category"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Risk Overview identyfikuje financial risks wpływające na projections"

  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility Study technical cost estimates informują Financial Plan CAPEX"

  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainability investments mogą wpływać na cost structure"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-FIN-PLAN-*.md"
    required: false
    purpose: "Tracking financial data collection and model validation tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-FIN-PLAN-*.md"
    required: true
    purpose: "Supporting financial assumptions, market data, cost quotations, revenue model validation"

  - type: DoR
    path: "satellites/dor/DOR-FIN-PLAN-*.md"
    required: true
    purpose: "Definition of Ready: market analysis completed, cost estimates gathered, revenue model defined before Financial Plan creation"

  - type: DoD
    path: "satellites/dod/DOD-FIN-PLAN-*.md"
    required: true
    purpose: "Definition of Done: financial model validated, scenarios stress-tested, CFO reviewed"
```

---

## Cel biznesowy / techniczny
Financial Plan przedstawia perspektywę finansową projektu – szacowane koszty, przychody i marże. Służy do oceny opłacalności przedsięwzięcia przez inwestorów i zarząd.

## Zawartość
- Prognozy przychodów
- Struktura kosztów (CAPEX, OPEX)
- Marże brutto i netto
- Punkt rentowności (break-even)
- Scenariusze pesymistyczny, realistyczny, optymistyczny
- Cash flow (wysokopoziomowy)

## Czego nie zawiera
- Detali technicznych
- Planów sprintów i backlogów
- Kodów źródłowych

## Objętość
- 3–6 stron
- 6–8 tabel / punktów kluczowych

## Kategoria
- **Wymagane** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd i dział finansowy
- Grantodawcy
