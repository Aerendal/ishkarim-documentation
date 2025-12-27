# 📄 Closure Report

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter defines objectives and success criteria to evaluate at closure"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "Project Charter §12 Project Objectives"
        to: "§2 Objectives Achieved"
        influence: "Original objectives compared against actual results"
      - from: "Project Charter §14 Budget Allocation"
        to: "§4 Budget Analysis"
        influence: "Planned budget compared against actual spend"

  - id: BRD-*
    type: requires
    reason: "BRD defines success criteria and KPIs to measure at closure"
    conditions:
      - when: "project.has_brd === true"
        applies: true
    sections:
      - from: "BRD §8 Success Criteria & KPIs"
        to: "§2 Objectives Achieved"
        influence: "Success criteria determine what achievements to report"

  - id: TIMELINE-*
    type: requires
    reason: "Timeline provides schedule baseline for comparing planned vs actual"
    conditions:
      - when: "project.has_timeline === true"
        applies: true
    sections:
      - from: "Timeline §2 Project Milestones"
        to: "§4 Schedule Analysis"
        influence: "Planned milestones compared against actual delivery dates"

  - id: TEST-SUMMARY-REPORT-*
    type: requires
    reason: "Test results demonstrate quality achievements at closure"
    conditions:
      - when: "project.has_testing === true"
        applies: true
    sections:
      - from: "Test Summary Report §3 Test Results"
        to: "§2 Objectives Achieved"
        influence: "Test results validate quality objectives were met"

  - id: UAT-PLAN-*
    type: influences
    reason: "UAT results confirm user acceptance at closure"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "UAT Plan §6 UAT Results"
        to: "§2 Objectives Achieved"
        influence: "UAT results demonstrate user acceptance achievement"
```

### Impacts
```yaml
impacts:
  - id: POSTMORTEM-REPORT-*
    type: influences
    reason: "Closure Report provides foundation for postmortem analysis"
    conditions:
      - when: "project.conducts_postmortem === true"
        applies: true
    sections:
      - from: "§5 Lessons Learned"
        to: "Postmortem Report §3 What Went Well"
        influence: "Lessons learned inform postmortem retrospective"
      - from: "§6 Open Items"
        to: "Postmortem Report §4 What Could Improve"
        influence: "Open items highlight areas for improvement"

  - id: KNOWLEDGE-TRANSFER-PLAN-*
    type: informs
    reason: "Closure identifies knowledge that needs transfer to operations"
    conditions:
      - when: "project.has_operations_handoff === true"
        applies: true
    sections:
      - from: "§5 Lessons Learned"
        to: "Knowledge Transfer Plan §2 Knowledge Areas"
        influence: "Lessons learned identify knowledge to transfer"
```

### Related
```yaml
related:
  - id: EXEC-SUMMARY-*
    type: informs
    reason: "Executive Summary may reference closure report results"

  - id: BIZ-CASE-*
    type: informs
    reason: "Closure validates business case ROI predictions"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-CLOSURE-*.md"
    required: false
    purpose: "Track closure activities and final documentation tasks"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-CLOSURE-*.md"
    required: true
    purpose: "Store final deliverables, sign-off documents, completion certificates"

  - type: DoD
    path: "satellites/dod/DOD-CLOSURE-*.md"
    required: true
    purpose: "Define completion criteria: all objectives validated, stakeholders signed off, lessons documented"
```

## Cel biznesowy / techniczny
Closure Report formalnie zamyka projekt i potwierdza, że cele zostały osiągnięte. Dokument zawiera podsumowanie wyników, ocenę zgodności z planem i wnioski na przyszłość.

## Zawartość
- Streszczenie projektu
- Osiągnięte cele i rezultaty
- Porównanie planów i faktycznych wyników
- Analiza budżetu i harmonogramu
- Wnioski i rekomendacje
- Lista otwartych spraw

## Czego nie zawiera
- Szczegółowych kodów źródłowych
- Strategii marketingowych
- Prognoz finansowych

## Objętość
- 2–3 strony
- 5–7 punktów kluczowych

## Kategoria
- **Nice-to-Have** (produkcyjne)

## Odbiorcy
- Zarząd
- Project managerowie
- Inwestorzy
