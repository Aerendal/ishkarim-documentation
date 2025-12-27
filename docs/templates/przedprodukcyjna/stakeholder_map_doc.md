# 📄 Stakeholder Map

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
    reason: "Project Charter identyfikuje key project roles i sponsor jako foundational stakeholders"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "Project Charter §14 Sponsor projektu i główne role"
        to: "§11 Lista kluczowych interesariuszy"
        influence: "Charter roles są core stakeholders w Stakeholder Map"

  - id: VISION-*
    type: influences
    reason: "Vision Document może identify strategic partners jako stakeholders"
    sections:
      - from: "Vision §16 Wizja pozycji rynkowej"
        to: "§11 Lista kluczowych interesariuszy"
        influence: "Market positioning strategy może reveal partnership stakeholders"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: COMMUNICATION-PLAN-*
    type: blocks
    reason: "Communication Plan wymaga Stakeholder Map dla stakeholder communication requirements"
    sections:
      - from: "§11 Lista kluczowych interesariuszy"
        to: "Communication Plan §12 Interesariusze i ich potrzeby informacyjne"
        influence: "Stakeholder list definiuje communication recipients"
      - from: "§13 Macierz interesariuszy (wysokie/niskie zaangażowanie vs wpływ)"
        to: "Communication Plan §14 Częstotliwość komunikacji"
        influence: "Stakeholder influence levels determinują communication frequency"

  - id: PROJECT-MGMT-PLAN-*
    type: blocks
    reason: "Project Management Plan wymaga Stakeholder Map dla stakeholder management"
    sections:
      - from: "§11 Lista kluczowych interesariuszy"
        to: "Project Mgmt Plan §17 Plan komunikacji"
        influence: "Stakeholder identification feeds into PMP communication plan"

  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Stakeholder Map może identify stakeholder-related risks"
    sections:
      - from: "§14 Oczekiwania i potencjalne obawy"
        to: "Risk Overview §11 Lista kluczowych ryzyk biznesowych"
        influence: "Stakeholder concerns są assessed jako stakeholder risks"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: GTM-*
    type: informs
    reason: "Go-to-Market stakeholders (distribution partners) są included w Stakeholder Map"

  - id: IMPACT-ASSESSMENT-*
    type: informs
    reason: "Impact Assessment może identify impacted stakeholder groups"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive stakeholders są key audience dla Executive Summary"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-STAKEHOLDER-*.md"
    required: false
    purpose: "Tracking stakeholder engagement tasks, relationship management actions"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-STAKEHOLDER-*.md"
    required: false
    purpose: "Stakeholder meeting notes, feedback, engagement records"

  - type: DoR
    path: "satellites/dor/DOR-STAKEHOLDER-*.md"
    required: true
    purpose: "Definition of Ready: project scope defined, key roles identified before Stakeholder Map creation"
```

---

## Cel biznesowy / techniczny
Stakeholder Map pomaga zidentyfikować i sklasyfikować osoby oraz organizacje mające wpływ lub interes w projekcie. Ułatwia zarządzanie komunikacją i zaangażowaniem interesariuszy.

## Zawartość
- Lista kluczowych interesariuszy
- Poziom wpływu i zainteresowania
- Macierz interesariuszy (wysokie/niskie zaangażowanie vs wpływ)
- Oczekiwania i potencjalne obawy
- Plan komunikacji

## Czego nie zawiera
- Personalnych ocen
- Danych wrażliwych (np. prywatnych adresów)
- Technicznych detali projektu

## Objętość
- 1–2 strony
- 5–8 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Zespół zarządzający projektem
- Inwestorzy
- Project managerowie
