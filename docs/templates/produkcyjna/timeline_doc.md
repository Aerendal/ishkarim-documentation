# 📄 Timeline & Milestones

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


## Document Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROJECT-CHARTER-*
    type: requires
    reason: "Project Charter defines project scope, objectives, and constraints that timeline must follow"
    conditions:
      - when: "project.has_formal_governance === true"
        applies: true
    sections:
      - from: "Project Charter §12 Objectives"
        to: "§2 Milestones"
        influence: "Project objectives define timeline milestones and success criteria"

  - id: BRD-*
    type: influences
    reason: "BRD defines scope of work that timeline schedules"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "BRD §5 Core Requirements"
        to: "§3 Project Phases"
        influence: "Business requirements scope determines timeline phases"

  - id: RESOURCE-REQUIREMENTS-*
    type: requires
    reason: "Resource availability affects timeline feasibility"
    conditions:
      - when: "project.has_resource_constraints === true"
        applies: true
    sections:
      - from: "Resource Requirements §2 Team Structure"
        to: "§4 Phase Duration"
        influence: "Team capacity determines realistic phase durations"
```

### Impacts
```yaml
impacts:
  - id: RELEASE-MANAGEMENT-PLAN-*
    type: blocks
    reason: "Timeline defines release schedule that release management follows"
    conditions:
      - when: "project.has_releases === true"
        applies: true
    sections:
      - from: "§2 Milestones"
        to: "Release Management Plan §2 Release Schedule"
        influence: "Project milestones define when releases occur"

  - id: TEST-PLAN-*
    type: influences
    reason: "Timeline defines testing phase schedule"
    conditions:
      - when: "project.has_testing === true"
        applies: true
    sections:
      - from: "§3 Project Phases"
        to: "Test Plan §8 Schedule"
        influence: "Timeline testing phases define when testing begins and ends"

  - id: UAT-PLAN-*
    type: influences
    reason: "Timeline defines UAT phase schedule"
    conditions:
      - when: "project.has_uat === true"
        applies: true
    sections:
      - from: "§2 Milestones"
        to: "UAT Plan §4 UAT Schedule"
        influence: "Timeline UAT milestone defines UAT phase timing"

  - id: DEPLOYMENT-GUIDE-*
    type: informs
    reason: "Timeline defines deployment phase timing"
    conditions:
      - when: "always"
        applies: true
    sections:
      - from: "§2 Milestones"
        to: "Deployment Guide §1 Introduction"
        influence: "Timeline deployment milestone defines go-live date"

  - id: TRAINING-MATERIALS-*
    type: informs
    reason: "Timeline defines when training must be delivered"
    conditions:
      - when: "project.has_training === true"
        applies: true
    sections:
      - from: "§3 Project Phases"
        to: "Training Materials §2 Training Schedule"
        influence: "Timeline phases determine training delivery schedule"

  - id: CHANGE-MANAGEMENT-PLAN-*
    type: informs
    reason: "Timeline defines change control windows"
    conditions:
      - when: "project.has_change_management === true"
        applies: true
    sections:
      - from: "§2 Milestones"
        to: "Change Management Plan §4 Change Schedule"
        influence: "Timeline milestones define change freeze periods"

  - id: CLOSURE-REPORT-*
    type: informs
    reason: "Timeline defines project completion date"
    conditions:
      - when: "project.phase === 'closing'"
        applies: true
    sections:
      - from: "§2 Milestones"
        to: "Closure Report §3 Objectives Achieved"
        influence: "Timeline final milestone validates project completion"

  - id: POSTMORTEM-REPORT-*
    type: informs
    reason: "Timeline shows planned vs actual schedule for lessons learned"
    conditions:
      - when: "project.phase === 'closing'"
        applies: true
    sections:
      - from: "§4 Phase Duration"
        to: "Postmortem Report §4 What Went Wrong"
        influence: "Timeline variances inform schedule estimation lessons learned"
```

### Related
```yaml
related:
  - id: RISK-OVERVIEW-TECH-*
    type: informs
    reason: "Timeline risks (schedule delays) tracked in risk overview"

  - id: OPERATIONAL-RISK-ASSESSMENT-*
    type: informs
    reason: "Schedule risks assessed in operational risk assessment"
```

### Satellites
```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-TIMELINE-*.md"
    required: true
    purpose: "Track timeline updates, milestone completions, schedule adjustments"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-TIMELINE-*.md"
    required: true
    purpose: "Store milestone completion records, schedule variance reports, phase completion evidence"

  - type: DoD
    path: "satellites/dod/DOD-TIMELINE-*.md"
    required: true
    purpose: "Define completion criteria: all milestones achieved, timeline documented, stakeholders informed"
```

## Cel biznesowy / techniczny
Timeline & Milestones przedstawia harmonogram realizacji projektu, podział na etapy i kamienie milowe. Dokument służy do monitorowania postępów i zarządzania terminami.

## Zawartość
- Kluczowe etapy realizacji
- Kamienie milowe
- Terminy rozpoczęcia i zakończenia etapów
- Wskaźniki sukcesu dla każdego etapu
- Wysokopoziomowy plan sprintów

## Czego nie zawiera
- Zbyt ogólnych wizji strategicznych
- Szczegółowych backlogów sprintów
- Kodów źródłowych

## Objętość
- 2–3 strony
- 6–8 punktów kluczowych

## Kategoria
- **Wymagane** (produkcyjne)

## Odbiorcy
- Project managerowie
- Zespół developerski
- Inwestorzy (wysokopoziomowy wgląd)
