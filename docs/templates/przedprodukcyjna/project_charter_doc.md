# 📄 Project Charter

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
    reason: "Vision Document definiuje strategiczne cele mapowane na cele projektowe"
    sections:
      - from: "Vision §13 Strategiczne cele biznesowe"
        to: "§12 Cele projektu"
        influence: "Cele strategiczne przekładają się na concrete project goals"

  - id: BIZ-CASE-*
    type: requires
    reason: "Business Case uzasadnia projekt i definiuje korzyści"
    sections:
      - from: "Business Case §14 Korzyści organizacyjne i rynkowe"
        to: "§16 Kryteria sukcesu"
        influence: "Korzyści biznesowe definiują measurable success criteria"
      - from: "Business Case §16 Prognozy finansowe"
        to: "§17 Budżet wysokopoziomowy"
        influence: "Prognozy finansowe określają ramy budżetowe projektu"

  - id: EXEC-SUMMARY-*
    type: requires
    reason: "Executive Summary dostarcza high-level overview przekształcany w project scope"
    sections:
      - from: "Executive Summary §15 Nasze rozwiązanie"
        to: "§13 Zakres wysokopoziomowy"
        influence: "Rozwiązanie definiuje granice projektu"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-MGMT-PLAN-*
    type: blocks
    reason: "Project Management Plan nie może być stworzony bez formalnego Charter definiującego projekt"
    sections:
      - from: "§17 Budżet wysokopoziomowy"
        to: "Project Mgmt Plan §4 Budget Baseline"
        influence: "Budżet z Charter definiuje financial baseline dla planu"
      - from: "§14 Sponsor projektu i główne role"
        to: "Project Mgmt Plan §2 Governance Structure"
        influence: "Role z Charter definiują project governance"

  - id: RESOURCE-REQUIREMENTS-*
    type: blocks
    reason: "Resource Requirements dokumentują zasoby autoryzowane przez Charter"
    sections:
      - from: "§18 Ograniczenia i założenia"
        to: "Resource Requirements §3 Constraints"
        influence: "Ograniczenia z Charter definiują resource constraints"

  - id: STAKEHOLDER-MAP-*
    type: blocks
    reason: "Stakeholder Map rozwija role i responsibilities z Charter"
    sections:
      - from: "§14 Sponsor projektu i główne role"
        to: "Stakeholder Map §2 Key Stakeholders"
        influence: "Główne role mapują się na stakeholder matrix"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: FEASIBILITY-STUDY-*
    type: informs
    reason: "Feasibility Study weryfikuje wykonalność projektu definiowanego w Charter"

  - id: COMMUNICATION-PLAN-*
    type: informs
    reason: "Communication Plan ustala kanały komunikacji dla projektu autoryzowanego przez Charter"

  - id: PROCUREMENT-PLAN-*
    type: informs
    reason: "Procurement Plan określa procurement strategy w ramach budżetu z Charter"
```

### Satellite Documents
```yaml
satellites:
  - type: Approval
    path: "satellites/approvals/APPROVAL-CHARTER-*.md"
    required: true
    purpose: "Sponsor and executive approval to formally authorize project"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CHARTER-*.md"
    required: false
    purpose: "Supporting justification for scope, budget, constraints"
```

---

## Cel biznesowy / techniczny
Project Charter formalnie rozpoczyna projekt. Określa jego zakres, cele, role oraz uprawnienia zespołu. Jest dokumentem ramowym zatwierdzanym przez sponsora projektu.

## Zawartość
- Cele projektu
- Zakres wysokopoziomowy
- Sponsor projektu i główne role
- Kluczowe deliverables
- Kryteria sukcesu
- Budżet wysokopoziomowy
- Ograniczenia i założenia

## Czego nie zawiera
- Szczegółowych wymagań technicznych
- Backlogów sprintów
- Kodów źródłowych

## Objętość
- 2–4 strony
- 6–8 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Sponsor projektu
- Zarząd
- Project managerowie
