# 📄 Communication Plan

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
    reason: "Project Charter identyfikuje kluczowe role i stakeholders wymagane do zdefiniowania communication strategy"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "Project Charter §14 Sponsor projektu i główne role"
        to: "§12 Interesariusze i ich potrzeby informacyjne"
        influence: "Role z Charter definiują communication stakeholders i ich information needs"
      - from: "Project Charter §18 Ograniczenia i założenia"
        to: "§15 Procedury eskalacyjne"
        influence: "Constraints określają escalation triggers i procedures"

  - id: STAKEHOLDER-MAP-*
    type: requires
    reason: "Stakeholder Map szczegółowo mapuje stakeholders i ich communication requirements"
    conditions:
      - when: "project.stakeholder_count > 10"
        applies: true
    sections:
      - from: "Stakeholder Map §2 Key Stakeholders"
        to: "§12 Interesariusze i ich potrzeby informacyjne"
        influence: "Stakeholder analysis definiuje tailored communication needs per stakeholder group"
      - from: "Stakeholder Map §3 Influence/Interest Matrix"
        to: "§14 Częstotliwość komunikacji"
        influence: "Stakeholder influence levels determinują communication frequency"

  - id: PROJECT-MGMT-PLAN-*
    type: influences
    reason: "Project Management Plan definiuje governance structure wpływającą na communication flows"
    conditions:
      - when: "project.governance === 'formal'"
        applies: true
    sections:
      - from: "Project Mgmt Plan §2 Governance Structure"
        to: "§16 Odpowiedzialności za komunikację"
        influence: "Governance structure mapuje się na communication responsibilities"
```

### Impacts (Co ten dokument popycha do przodu)
```yaml
impacts:
  - id: PROJECT-MGMT-PLAN-*
    type: informs
    reason: "Communication Plan informuje communication i reporting sections w Project Management Plan"
    conditions:
      - when: "project.is_formal === true"
        applies: true
    sections:
      - from: "§13 Kanały komunikacji"
        to: "Project Mgmt Plan §6 Communication Channels"
        influence: "Zdefiniowane kanały są adoptowane w project management processes"
      - from: "§15 Procedury eskalacyjne"
        to: "Project Mgmt Plan §7 Issue Escalation"
        influence: "Escalation procedures definiują project-level escalation paths"

  - id: STAKEHOLDER-MAP-*
    type: influences
    reason: "Communication Plan validation może wpłynąć na refinement stakeholder engagement strategies"
    sections:
      - from: "§14 Częstotliwość komunikacji"
        to: "Stakeholder Map §4 Engagement Strategy"
        influence: "Communication frequency informuje stakeholder engagement planning"

  - id: TRAINING-PLAN-*
    type: informs
    reason: "Communication Plan może identyfikować training needs dla communication tools"
    conditions:
      - when: "communication.requires_new_tools === true"
        applies: true
    sections:
      - from: "§13 Kanały komunikacji"
        to: "Training Plan §3 Tool Training"
        influence: "Nowe communication tools wymagają user training"
```

### Related Documents (Powiązane dokumenty)
```yaml
related:
  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Risk Overview identyfikuje communication-related risks wymagające mitigation w Communication Plan"

  - id: GO-TO-MARKET-*
    type: informs
    reason: "Go-to-Market Plan definiuje external communication strategy uzupełniającą internal Communication Plan"

  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary określa high-level information needs dla executive stakeholders"
```

### Satellite Documents
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-COMM-PLAN-*.md"
    required: false
    purpose: "Tracking setup of communication channels and stakeholder onboarding"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-COMM-PLAN-*.md"
    required: false
    purpose: "Communication templates, meeting agendas, stakeholder feedback"

  - type: DoR
    path: "satellites/dor/DOR-COMM-PLAN-*.md"
    required: true
    purpose: "Definition of Ready: stakeholder list, communication requirements identified before plan creation"

  - type: DoD
    path: "satellites/dod/DOD-COMM-PLAN-*.md"
    required: true
    purpose: "Definition of Done: communication channels tested, stakeholders briefed, procedures documented"
```

---

## Cel biznesowy / techniczny
Communication Plan definiuje strategię komunikacji w projekcie – kto, kiedy i w jaki sposób otrzymuje informacje. Ułatwia zarządzanie przepływem informacji i minimalizuje ryzyko nieporozumień.

## Zawartość
- Interesariusze i ich potrzeby informacyjne
- Kanały komunikacji (spotkania, e-mail, narzędzia online)
- Częstotliwość komunikacji
- Format raportów i aktualizacji
- Procedury eskalacyjne
- Odpowiedzialności za komunikację

## Czego nie zawiera
- Kodów źródłowych
- Backlogów sprintów
- Strategii marketingowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Przydatne** (przedprodukcyjne)

## Odbiorcy
- Project managerowie
- Zespół projektowy
- Interesariusze
