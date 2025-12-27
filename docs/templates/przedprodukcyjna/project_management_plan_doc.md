# 📄 Project Management Plan

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
    reason: "Project Charter authorizes project i dostarcza foundational scope/budget/goals dla PMP"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "Project Charter §12 Cele projektu"
        to: "§11 Zakres projektu"
        influence: "Charter objectives definiują project scope boundaries"
      - from: "Project Charter §17 Budżet wysokopoziomowy"
        to: "§13 Budżet i alokacja zasobów"
        influence: "High-level budget jest decomposed w detailed resource plan"
      - from: "Project Charter §14 Sponsor projektu i główne role"
        to: "§17 Plan komunikacji"
        influence: "Charter roles definiują project governance i communication structure"

  - id: STAKEHOLDER-MAP-*
    type: requires
    reason: "Stakeholder Map identyfikuje stakeholders dla communication plan"
    sections:
      - from: "Stakeholder Map §11 Lista kluczowych interesariuszy"
        to: "§17 Plan komunikacji"
        influence: "Stakeholder list definiuje communication recipients"

  - id: RISK-OVERVIEW-*
    type: requires
    reason: "Risk Overview dostarcza risk assessment wymagany dla risk management plan"
    sections:
      - from: "Risk Overview §11 Lista kluczowych ryzyk biznesowych"
        to: "§15 Plan ryzyka"
        influence: "Identified risks are managed w project risk plan"

  - id: FINANCIAL-PLAN-*
    type: influences
    reason: "Financial Plan detailed budget informuje resource allocation"
    sections:
      - from: "Financial Plan §12 Struktura kosztów (CAPEX, OPEX)"
        to: "§13 Budżet i alokacja zasobów"
        influence: "Cost structure guides resource budget allocation"

  - id: COMMUNICATION-PLAN-*
    type: influences
    reason: "Communication Plan definiuje communication channels i procedures"
    sections:
      - from: "Communication Plan §13 Kanały komunikacji"
        to: "§17 Plan komunikacji"
        influence: "Communication channels są adopted w project management"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROCUREMENT-PLAN-*
    type: influences
    reason: "PMP schedule i budget wpływają na procurement timing"
    sections:
      - from: "§12 Harmonogram (wysokopoziomowy)"
        to: "Procurement Plan §13 Harmonogram zakupów"
        influence: "Project milestones definiują procurement deadlines"

  - id: TRAINING-PLAN-*
    type: influences
    reason: "PMP może identify training needs dla team capabilities"
    sections:
      - from: "§13 Budżet i alokacja zasobów"
        to: "Training Plan §15 Budżet na szkolenia"
        influence: "Resource plan może include training budget allocation"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: ROADMAP-*
    type: informs
    reason: "Innovation Roadmap timeline może align z PMP schedule"

  - id: GTM-*
    type: informs
    reason: "Go-to-Market timeline wpływa na project delivery deadlines"

  - id: LEGAL-REGISTER-*
    type: informs
    reason: "Legal compliance requirements wpływają na project governance"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-PMP-*.md"
    required: false
    purpose: "Tracking project management tasks, plan updates, change requests"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-PMP-*.md"
    required: false
    purpose: "Project status reports, change logs, stakeholder approvals"

  - type: DoR
    path: "satellites/dor/DOR-PMP-*.md"
    required: true
    purpose: "Definition of Ready: Project Charter approved, stakeholders identified, risks assessed before PMP creation"

  - type: DoD
    path: "satellites/dod/DOD-PMP-*.md"
    required: true
    purpose: "Definition of Done: all plans integrated, baselines set, sponsor approved, team briefed"
```

---

## Cel biznesowy / techniczny
Project Management Plan (PMP) to nadrzędny dokument opisujący, jak projekt będzie planowany, monitorowany i kontrolowany. Służy jako przewodnik dla kierownika projektu i całego zespołu.

## Zawartość
- Zakres projektu
- Harmonogram (wysokopoziomowy)
- Budżet i alokacja zasobów
- Plan jakości
- Plan ryzyka
- Plan komunikacji
- Plan zarządzania zmianą

## Czego nie zawiera
- Szczegółowych backlogów sprintów
- Kodów źródłowych
- Dokumentacji technicznej niskiego poziomu

## Objętość
- 5–10 stron
- 10–15 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Project manager
- Sponsor projektu
- Zespół zarządzający
