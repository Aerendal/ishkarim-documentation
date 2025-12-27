# 📄 Postmortem / Retrospective Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: CLOSURE-REPORT-*
    type: requires
    reason: "Closure Report provides project outcomes for postmortem analysis"
    conditions:
      - when: "project.phase === 'closed'"
        applies: true
    sections:
      - from: "Closure Report §2 Objectives Achieved"
        to: "§2 Project Summary"
        influence: "Closure results inform postmortem project summary"
      - from: "Closure Report §5 Lessons Learned"
        to: "§5 Lessons Learned"
        influence: "Closure lessons feed into postmortem analysis"

  - id: INCIDENT-REPORT-*
    type: influences
    reason: "Major incidents require postmortem analysis"
    conditions:
      - when: "incident.severity in ['critical', 'major']"
        applies: true
      - when: "incident.duration > threshold"
        applies: true
    sections:
      - from: "Incident Report §4 Root Cause"
        to: "§3 Root Cause Analysis"
        influence: "Incident RCA becomes postmortem root cause analysis"
      - from: "Incident Report §6 Lessons Learned"
        to: "§5 Lessons Learned"
        influence: "Incident lessons inform postmortem"

  - id: TIMELINE-*
    type: influences
    reason: "Timeline provides schedule baseline for retrospective analysis"
    conditions:
      - when: "project.has_timeline === true"
        applies: true
    sections:
      - from: "Timeline §2 Milestones"
        to: "§4 Schedule Analysis"
        influence: "Planned vs actual timeline analyzed in postmortem"
```

### Impacts
```yaml
impacts:
  - id: RISK-OVERVIEW-*
    type: informs
    reason: "Postmortem learnings identify new risks for future projects"
    conditions:
      - when: "postmortem.identifies_risks === true"
        applies: true
    sections:
      - from: "§4 What Went Wrong"
        to: "Risk Overview §3 Risk Inventory"
        influence: "Postmortem problems become identified risks for future projects"

  - id: KNOWLEDGE-TRANSFER-PLAN-*
    type: informs
    reason: "Postmortem lessons are knowledge to transfer"
    conditions:
      - when: "project.has_knowledge_transfer === true"
        applies: true
    sections:
      - from: "§5 Lessons Learned"
        to: "Knowledge Transfer Plan §2 Knowledge Areas"
        influence: "Postmortem learnings become knowledge transfer content"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Postmortem reveals training needs and best practices"
    conditions:
      - when: "postmortem.identifies_training_gaps === true"
        applies: true
    sections:
      - from: "§6 Recommendations"
        to: "Training Materials §3 Best Practices Training"
        influence: "Postmortem recommendations inform training content"
```

### Related
```yaml
related:
  - id: PROJECT-CHARTER-*
    type: informs
    reason: "Postmortem compares results against original charter objectives"

  - id: BIZ-CASE-*
    type: informs
    reason: "Postmortem validates business case predictions"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-POSTMORTEM-*.md"
    required: false
    purpose: "Track postmortem action items and improvement initiatives"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-POSTMORTEM-*.md"
    required: true
    purpose: "Store retrospective meeting notes, team feedback, metrics data, timeline analysis"

  - type: DoD
    path: "satellites/dod/DOD-POSTMORTEM-*.md"
    required: true
    purpose: "Define completion criteria: all stakeholders participated, action items documented, learnings shared"
```

## Cel biznesowy / techniczny
Postmortem Report (lub Retrospective Report) dokumentuje doświadczenia po zakończeniu projektu lub jego etapu. Ma na celu wyciągnięcie wniosków i usprawnienie przyszłych działań.

## Zawartość
- Streszczenie projektu / etapu
- Co poszło dobrze
- Co poszło źle
- Główne problemy i przyczyny
- Wnioski i rekomendacje na przyszłość
- Lista działań naprawczych

## Czego nie zawiera
- Strategii sprzedażowych
- Szczegółowych kodów źródłowych
- Prognoz finansowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Zespół projektowy
