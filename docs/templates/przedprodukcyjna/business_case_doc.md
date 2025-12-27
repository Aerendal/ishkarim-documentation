# 📄 Business Case

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
    reason: "Długoterminowa wizja definiuje strategiczny kontekst dla Business Case"
    sections:
      - from: "Vision §13 Strategiczne cele biznesowe"
        to: "§14 Korzyści organizacyjne i rynkowe"
        influence: "Cele strategiczne mapują się na korzyści biznesowe"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Analiza rynku dostarcza danych o wielkości rynku i konkurencji dla uzasadnienia inwestycji"
    sections:
      - from: "Market Analysis §12 Wielkość rynku (TAM, SAM, SOM)"
        to: "§15 Uzasadnienie wyboru projektu"
        influence: "Wielkość rynku uzasadnia potencjał zwrotu z inwestycji"

  - id: FINANCIAL-PLAN-*
    type: requires
    reason: "Financial Plan dostarcza szczegółowych prognoz finansowych wspierających ROI"
    sections:
      - from: "Financial Plan §12 Prognozy przychodów"
        to: "§16 Prognozy finansowe (wysokopoziomowe)"
        influence: "Prognozy definiują oczekiwany zwrot finansowy"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: EXEC-SUMMARY-*
    type: blocks
    reason: "Executive Summary nie może być stworzony bez uzasadnienia biznesowego z Business Case"
    sections:
      - from: "§17 Plan osiągnięcia ROI"
        to: "Executive Summary §17 Model biznesowy i szacowane przychody"
        influence: "Plan ROI definiuje model generowania przychodów"

  - id: PROJECT-CHARTER-*
    type: blocks
    reason: "Project Charter formalizuje budżet i zakres zdefiniowany w Business Case"
    sections:
      - from: "§14 Korzyści organizacyjne i rynkowe"
        to: "Project Charter §16 Kryteria sukcesu"
        influence: "Korzyści definiują measurable success criteria"

  - id: FEASIBILITY-STUDY-*
    type: blocks
    reason: "Feasibility Study ocenia wykonalność projektu uzasadnionego w Business Case"
    sections:
      - from: "§13 Analiza alternatywnych rozwiązań"
        to: "Feasibility Study §17 Rekomendacja (go / no-go)"
        influence: "Alternatywy wymagają oceny wykonalności"

  - id: PRD-*
    type: informs
    reason: "PRD rozwija wymagania produktowe uzasadnione biznesowo w Business Case"
    sections:
      - from: "§12 Opis problemu biznesowego"
        to: "PRD §12 Opis produktu i jego celu"
        influence: "Problem biznesowy definiuje cel produktu"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: RISK-OVERVIEW-INVEST-*
    type: informs
    reason: "Risk Overview identyfikuje zagrożenia dla korzyści biznesowych opisanych w Business Case"

  - id: CBA-*
    type: informs
    reason: "Cost-Benefit Analysis dostarcza szczegółowej analizy kosztów vs. korzyści"

  - id: PITCH-DECK-*
    type: informs
    reason: "Pitch Deck prezentuje kluczowe argumenty biznesowe z Business Case w formie wizualnej"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-BIZ-CASE-*.md"
    required: true
    purpose: "Tracking research and analysis tasks per section"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-BIZ-CASE-*.md"
    required: true
    purpose: "Financial models, competitive analysis, ROI calculations"

  - type: Approval
    path: "satellites/approvals/APPROVAL-BIZ-CASE-*.md"
    required: true
    purpose: "Stakeholder sign-off on investment decision"
```

---

## Cel biznesowy / techniczny
Business Case służy do uzasadnienia inwestycji w projekt. Odpowiada na pytanie „dlaczego warto to robić” z punktu widzenia zwrotu z inwestycji (ROI), strategicznego dopasowania i korzyści.

## Zawartość

### Executive Summary
Zwięzłe podsumowanie Business Case w 1-2 akapitach (problem, rozwiązanie, ROI, rekomendacja).

### Problem Statement
Szczegółowy opis problemu biznesowego, który rozwiązujemy. Jaki jest jego wpływ na organizację?

### Strategic Alignment
Jak projekt wspiera strategię organizacji i długoterminowe cele biznesowe?

### Solution Overview
Opis proponowanego rozwiązania na wysokim poziomie.

### Alternatives Analysis
Analiza rozważanych alternatyw:
- Status quo (nic nie robimy)
- Alternatywa A, B, C
- Porównanie kosztów, korzyści, ryzyk
- Uzasadnienie wyboru rekomendowanego rozwiązania

### Financial Projections
Prognozy finansowe:
- Szacowane koszty (CAPEX, OPEX)
- Oczekiwane przychody/oszczędności
- ROI i payback period
- NPV i IRR (jeśli applicable)
- Cash flow timeline

### Benefits Analysis
Korzyści:
- Tangible (wymierne finansowo)
- Intangible (jakościowe: brand, morale, customer satisfaction)
- Krótko- i długoterminowe

### Cost-Benefit Analysis
Zestawienie kosztów vs korzyści w perspektywie czasu.

### Risks & Mitigation
Kluczowe ryzyka biznesowe i plany mitygacji.

### Implementation Approach
Wysokopoziomowe podejście do implementacji (fazy, timeline, zasoby).

### Success Metrics
Jak zmierzymy sukces inwestycji? KPIs i metryki biznesowe.

### Stakeholder Impact
Wpływ projektu na kluczowych interesariuszy (pozytywny/negatywny).

### Resource Requirements
Wymagane zasoby (ludzie, technologia, budżet, czas).

### Dependencies & Assumptions
Kluczowe zależności i założenia leżące u podstaw Business Case.

### Recommendation & Next Steps
Jasna rekomendacja (GO/NO-GO) i proponowane następne kroki.

## Czego nie zawiera
- Szczegółowych planów kodowania
- Backlogów sprintów
- Technicznych diagramów

## Objętość
- 8–15 stron
- 20–30 punktów kluczowych

## Kategoria
- **Wymagane** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd i komitety inwestycyjne
- Menedżerowie ds. strategii
