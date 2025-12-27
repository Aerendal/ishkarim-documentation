# 📄 Cost-Benefit Analysis (CBA)

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
    reason: "Business Case dostarcza initial assessment korzyści i kosztów wymaganych do szczegółowej CBA"
    conditions:
      - when: "project.investment_required === true"
        applies: true
      - when: "project.budget < 10000"
        applies: false
    sections:
      - from: "Business Case §16 Prognozy finansowe"
        to: "§12 Oczekiwane przychody"
        influence: "Prognozy finansowe z Business Case stanowią bazę dla revenue projections w CBA"
      - from: "Business Case §14 Korzyści organizacyjne i rynkowe"
        to: "§13 Wartości niematerialne"
        influence: "Korzyści organizacyjne mapują się na intangible benefits"

  - id: FINANCIAL-PLAN-*
    type: requires
    reason: "Financial Plan dostarcza szczegółowych breakdown kosztów dla CBA"
    conditions:
      - when: "project.phase === 'detailed_planning'"
        applies: true
    sections:
      - from: "Financial Plan §3 Budget Breakdown"
        to: "§11 Koszty bezpośrednie i pośrednie"
        influence: "Budget breakdown definiuje structure kosztów dla analizy"

  - id: MARKET-ANALYSIS-*
    type: influences
    reason: "Market Analysis informuje revenue assumptions i market opportunity w CBA"
    conditions:
      - when: "project.has_revenue_model === true"
        applies: true
    sections:
      - from: "Market Analysis §5 Analiza rynku docelowego"
        to: "§14 Analiza scenariuszowa"
        influence: "Market size i growth definiują realistic/optimistic scenarios"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary prezentuje kluczowe wnioski z CBA dla decision makers"
    conditions:
      - when: "cba.recommendation === 'proceed'"
        applies: true
    sections:
      - from: "§16 Wskaźniki ROI i NPV"
        to: "Executive Summary §16 Strategia finansowa"
        influence: "ROI/NPV metrics stanowią financial justification w Executive Summary"
      - from: "§17 Rekomendacja"
        to: "Executive Summary §18 Następne kroki"
        influence: "Rekomendacja CBA determinuje action items w Executive Summary"

  - id: FINANCIAL-PLAN-*
    type: influences
    reason: "CBA validation wpływa na refinement Financial Plan"
    conditions:
      - when: "cba.shows_positive_roi === true"
        applies: true
    sections:
      - from: "§14 Analiza scenariuszowa"
        to: "Financial Plan §5 Contingency Planning"
        influence: "Scenariusze CBA informują contingency buffers w Financial Plan"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "CBA identyfikuje financial risks wymagające mitigation strategies"
    sections:
      - from: "§14 Analiza scenariuszowa"
        to: "Risk Overview §3 Financial Risks"
        influence: "Pesymistyczne scenariusze definiują downside risks"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility Study dostarcza technical viability assessment wspierającego cost assumptions w CBA"

  - id: PROCUREMENT-PLAN-*
    type: informs
    reason: "Procurement Plan szczegółowo rozbija procurement costs ujęte w CBA"

  - id: PROJECT-CHARTER-*
    type: informs
    reason: "Project Charter definiuje high-level budget constraints dla CBA"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CBA-*.md"
    required: false
    purpose: "Tracking data collection and analysis tasks for CBA"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CBA-*.md"
    required: true
    purpose: "Supporting financial data, market research, and cost justifications"

  - type: DoR
    path: "satellites/dor/DOR-CBA-*.md"
    required: true
    purpose: "Definition of Ready: required financial data, cost estimates, revenue projections before CBA creation"
```

---

## Cel biznesowy / techniczny
Cost-Benefit Analysis (CBA) porównuje koszty projektu z potencjalnymi korzyściami. Dokument wspiera podejmowanie decyzji inwestycyjnych.

## Zawartość
- Koszty bezpośrednie i pośrednie
- Oczekiwane przychody
- Wartości niematerialne (np. reputacja, satysfakcja klienta)
- Analiza scenariuszowa (pesymistyczny, realistyczny, optymistyczny)
- Wskaźniki ROI i NPV
- Rekomendacja

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów sprintowych
- Opisów technicznych

## Objętość
- 2–3 strony
- 6–8 punktów kluczowych

## Kategoria
- **Wymagane/Przydatne** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd
- Project managerowie
