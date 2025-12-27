# 📄 Feasibility Study (Studium wykonalności)

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
    reason: "Business Case definiuje projekt wymagający oceny wykonalności"
    sections:
      - from: "Business Case §13 Analiza alternatywnych rozwiązań"
        to: "§17 Rekomendacja (go / no-go)"
        influence: "Alternatywy wymagają oceny feasibility przed decyzją go/no-go"

  - id: MARKET-ANALYSIS-*
    type: requires
    reason: "Market Analysis dostarcza danych rynkowych dla oceny wykonalności biznesowej"
    sections:
      - from: "Market Analysis §17 Potencjalne bariery wejścia"
        to: "§15 Analiza organizacyjna (zasoby, kompetencje)"
        influence: "Bariery rynkowe wpływają na feasibility organizacyjną"

  - id: FINANCIAL-PLAN-*
    type: requires
    reason: "Financial Plan dostarcza danych finansowych dla oceny wykonalności ekonomicznej"
    sections:
      - from: "Financial Plan §13 Struktura kosztów (CAPEX, OPEX)"
        to: "§13 Analiza finansowa (koszty, potencjalne przychody)"
        influence: "Struktura kosztów określa financial feasibility"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-CHARTER-*
    type: blocks
    reason: "Project Charter nie powinien być tworzony jeśli Feasibility Study pokazuje no-go"
    sections:
      - from: "§17 Rekomendacja (go / no-go)"
        to: "Project Charter §12 Cele projektu"
        influence: "Rekomendacja go/no-go autoryzuje lub blokuje Charter"

  - id: PRD-*
    type: blocks
    reason: "PRD nie może być rozpoczęty bez potwierdzenia technical feasibility"
    sections:
      - from: "§12 Analiza technicznej wykonalności"
        to: "PRD §15 Wymagania niefunkcjonalne"
        influence: "Technical feasibility definiuje realistic NFRs"

  - id: RISK-OVERVIEW-INVEST-*
    type: informs
    reason: "Risk Overview rozwija ryzyka zidentyfikowane w Feasibility Study"
    sections:
      - from: "§16 Ocena ryzyka i scenariusze"
        to: "Risk Overview §12 Lista kluczowych ryzyk biznesowych"
        influence: "Scenariusze ryzyka z Feasibility są input dla Risk Overview"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: LEGAL-REGISTER-*
    type: informs
    reason: "Legal Register dokumentuje zgodność prawną ocenianą w Feasibility Study"

  - id: PROCUREMENT-PLAN-*
    type: informs
    reason: "Procurement Plan jest tworzony jeśli Feasibility Study identyfikuje external dependencies"

  - id: RESOURCE-REQUIREMENTS-*
    type: informs
    reason: "Resource Requirements opierają się na ocenie zasobów z Feasibility Study"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-FEASIBILITY-*.md"
    required: true
    purpose: "Tracking research and analysis tasks per feasibility dimension"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-FEASIBILITY-*.md"
    required: true
    purpose: "Technical POCs, financial models, legal opinions supporting feasibility claims"

  - type: Approval
    path: "satellites/approvals/APPROVAL-FEASIBILITY-*.md"
    required: true
    purpose: "Stakeholder approval on go/no-go recommendation"
```

---

## Cel biznesowy / techniczny
Feasibility Study ocenia, czy projekt jest możliwy do zrealizowania z perspektywy technicznej, finansowej, prawnej i organizacyjnej. Dokument ten zmniejsza ryzyko rozpoczęcia niewykonalnego przedsięwzięcia.

## Zawartość
- Analiza technicznej wykonalności
- Analiza finansowa (koszty, potencjalne przychody)
- Analiza prawna (zgodność regulacyjna)
- Analiza organizacyjna (zasoby, kompetencje)
- Ocena ryzyka i scenariusze
- Rekomendacja (go / no-go)

## Czego nie zawiera
- Szczegółowych planów implementacyjnych
- Kodów źródłowych
- Backlogów sprintowych

## Objętość
- 5–10 stron
- 10–15 punktów kluczowych

## Kategoria
- **Wymagane** (przedprodukcyjne)

## Odbiorcy
- Inwestorzy
- Zarząd
- Project managerowie
