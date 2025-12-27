# 📄 Procurement Plan

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter definiuje project scope i budget constraints dla procurement"
    conditions:
      - when: "project.requires_procurement === true"
        applies: true
    sections:
      - from: "Project Charter §17 Budżet wysokopoziomowy"
        to: "§15 Budżet i koszty"
        influence: "Charter budget definiuje procurement spending limits"

  - id: FINANCIAL-PLAN-*
    type: requires
    reason: "Financial Plan dostarcza detailed budget allocation dla procurement categories"
    sections:
      - from: "Financial Plan §12 Struktura kosztów (CAPEX, OPEX)"
        to: "§15 Budżet i koszty"
        influence: "Cost structure definiuje procurement budget per category"

  - id: LEGAL-REGISTER-*
    type: influences
    reason: "Legal Register regulatory requirements wpływają na vendor selection criteria"
    conditions:
      - when: "procurement.requires_compliance === true"
        applies: true
    sections:
      - from: "Legal Register §11 Lista obowiązujących regulacji"
        to: "§14 Kryteria wyboru dostawców"
        influence: "Regulatory requirements definiują vendor compliance requirements"

  - id: FEASIBILITY-STUDY-*
    type: influences
    reason: "Feasibility Study technical requirements informują procurement specifications"
    sections:
      - from: "Feasibility Study §5 Technical Requirements"
        to: "§11 Lista potrzebnych zasobów"
        influence: "Technical requirements definiują hardware/software specifications"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-MGMT-PLAN-*
    type: informs
    reason: "Procurement Plan timeline wpływa na Project Management Plan schedule"
    sections:
      - from: "§13 Harmonogram zakupów"
        to: "Project Mgmt Plan §3 Schedule"
        influence: "Procurement milestones są incorporated w project timeline"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Procurement Plan może identify vendor-related risks"
    conditions:
      - when: "procurement.has_critical_vendors === true"
        applies: true
    sections:
      - from: "§14 Kryteria wyboru dostawców"
        to: "Risk Overview §9 Vendor & Supply Chain Risks"
        influence: "Vendor dependencies are assessed jako project risks"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: DPIA-*
    type: informs
    reason: "Procurement of data processors requires DPIA compliance verification"

  - id: CBA-*
    type: informs
    reason: "CBA procurement costs inform vendor selection decisions"

  - id: SUSTAINABILITY-REPORT-*
    type: informs
    reason: "Sustainable procurement criteria może be part of vendor selection"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PROCUREMENT-*.md"
    required: false
    purpose: "Tracking procurement tasks, vendor evaluations, contract negotiations"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PROCUREMENT-*.md"
    required: true
    purpose: "Vendor quotations, contracts, compliance certificates, procurement approvals"

  - type: DoR
    path: "satellites/dor/DOR-PROCUREMENT-*.md"
    required: true
    purpose: "Definition of Ready: requirements defined, budget approved, vendor criteria established before Procurement Plan"

  - type: DoD
    path: "satellites/dod/DOD-PROCUREMENT-*.md"
    required: true
    purpose: "Definition of Done: vendors selected, contracts signed, delivery scheduled, budget approved"
```

---

## Cel biznesowy / techniczny
Procurement Plan określa proces zakupu sprzętu, oprogramowania i usług potrzebnych do realizacji projektu. Pomaga zaplanować koszty i harmonogram dostaw.

## Zawartość
- Lista potrzebnych zasobów
- Dostawcy i partnerzy
- Harmonogram zakupów
- Kryteria wyboru dostawców
- Budżet i koszty
- Procedury zatwierdzania wydatków

## Czego nie zawiera
- Kodów źródłowych
- Szczegółowych planów sprintowych
- Analiz rynkowych (poza zakupami)

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Dział zakupów
