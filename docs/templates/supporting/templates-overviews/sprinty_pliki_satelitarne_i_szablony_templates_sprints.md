# Sprinty — pliki satelitarne i szablony (Markdown)

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Ten dokument zawiera:
1) **listę rekomendowanych plików satelitarnych sprintu** (minimum / standard / rozszerzony),
2) **gotowe szablony `.md`** do skopiowania do `templates/sprints/`,
3) sugerowaną strukturę `docs/<project>/sprints/SXX/`.

---

## 1) Pliki satelitarne sprintu — rekomendowany zestaw

### Minimum (zawsze, dla podejścia dojrzałego)
- `sprint-plan.md` — cel sprintu, zakres, capacity, checkpointy.
- `sprint-backlog.md` — lista itemów z ownerami, estymacją i linkami do TODO/dokumentów.
- `sprint-review.md` — co dowieziono, co nie, feedback, decyzje.
- `sprint-retro.md` — wnioski procesowe.
- `sprint-action-items.md` — akcje z retro (owner, due, status).

### Standard (zalecane w większości projektów)
- `sprint-dor.md` — Sprint DoR (kryteria wejścia dla itemów).
- `sprint-dod.md` — Sprint DoD (kryteria domknięcia).
- `sprint-impediments.md` — rejestr blokerów (live).

### Rozszerzony (dla większych / regulowanych / release‑heavy)
- `sprint-scope-change.md` — Change Request dla zmian scope w trakcie sprintu.
- `sprint-metrics.md` — velocity, jakość, lead time, dokumentacja dowieziona.
- `sprint-approval.md` — formalny sign‑off (np. PO/Sponsor) jeśli sprint domyka etap.
- `daily/` — dzienniki dzienne (opcjonalne, gdy potrzebujesz audytu).
- `metrics/` — burndown/burnup w CSV.

---

## 2) Rekomendowana struktura w repo (instancje sprintów)

```
docs/<project>/sprints/SXX/
  sprint-plan.md
  sprint-backlog.md
  sprint-dor.md
  sprint-dod.md
  sprint-impediments.md
  sprint-review.md
  sprint-retro.md
  sprint-action-items.md
  sprint-metrics.md
  sprint-scope-change.md
  approvals/sprint-approval.md
  daily/ (opcjonalnie)
  metrics/ (burndown.csv, burnup.csv)
```

---

# 3) Szablony do `templates/sprints/`

## `templates/sprints/sprint-plan.md`
```markdown
---
id: "SPRINT-PLAN-SXX"
title: "Sprint Plan — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master / Delivery Lead"
status: "draft"          # draft|in-review|approved|closed
version: "0.1"
date_created: "YYYY-MM-DD"
period: "YYYY-MM-DD..YYYY-MM-DD"
sprint_goal: ""
related: ["ROADMAP-PROD-001","REL-CHECK-001"]
---

# Sprint Plan — SXX

## 1. Sprint Goal
- Jedno zdanie: co ma zostać osiągnięte i dlaczego.

## 2. Zakres (Scope)
- In scope:
  - ...
- Out of scope:
  - ...

## 3. Capacity / dostępność
- Zespół i dostępność (FTE, urlopy, ograniczenia).

## 4. Backlog wybrany do sprintu
- Patrz: `sprint-backlog.md`

## 5. Zależności i ryzyka (top 3)
- D1: ...
- R1: ...

## 6. Definicje
- DoR sprint: `sprint-dor.md`
- DoD sprint: `sprint-dod.md`

## 7. Checkpointy
- Mid-sprint check (YYYY-MM-DD)
- Review (YYYY-MM-DD)
- Retro (YYYY-MM-DD)

## 8. Komunikacja
- Kto dostaje update i kiedy (np. weekly stakeholder update).
```

---

## `templates/sprints/sprint-backlog.md`
```markdown
---
id: "SPRINT-BACKLOG-SXX"
title: "Sprint Backlog — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master / Delivery Lead"
status: "draft"          # draft|in-review|approved|closed
version: "0.1"
period: "YYYY-MM-DD..YYYY-MM-DD"
related: ["SPRINT-PLAN-SXX"]
---

# Sprint Backlog — SXX

| ID | Item | Owner | Estimate | Status | Related doc / TODO | Acceptance |
|---|---|---|---:|---|---|---|
| SXX-001 | ... | ... | 3 | todo | TODO-PRD-001 | AC link |

## Notes
- Do sprintu trafiają tylko itemy spełniające Sprint DoR.
```

---

## `templates/sprints/sprint-dor.md`
```markdown
---
id: "SPRINT-DOR-SXX"
title: "Sprint Definition of Ready — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Owner"
status: "draft"
version: "0.1"
related: ["SPRINT-PLAN-SXX"]
---

# Sprint DoR — SXX

## Kryteria wejścia dla itemów sprintu
- [ ] Cel i opis zadania jasno zapisane
- [ ] Acceptance Criteria dostępne
- [ ] Estymacja wykonana
- [ ] Owner przypisany
- [ ] Zależności znane i zarejestrowane
- [ ] Dostęp do danych/test env (lub plan)
```

---

## `templates/sprints/sprint-dod.md`
```markdown
---
id: "SPRINT-DOD-SXX"
title: "Sprint Definition of Done — SXX"
project: "NAZWA_PROJEKTU"
owner: "Team Lead / QA"
status: "draft"
version: "0.1"
related: ["SPRINT-PLAN-SXX"]
---

# Sprint DoD — SXX

## Kryteria wyjścia (zamknięcia sprintu)
- [ ] Wszystkie P0/P1 itemy domknięte lub świadomie odłożone (z CR)
- [ ] Review przeprowadzone, wyniki zapisane
- [ ] Retro przeprowadzone, action items zapisane
- [ ] Dokumentacja (jeśli dotyczy) zaktualizowana i zmergowana
- [ ] Approval / sign-off (jeśli wymagane)
```

---

## `templates/sprints/sprint-impediments.md`
```markdown
---
id: "SPRINT-IMP-SXX"
title: "Impediments Log — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "live"
related: ["SPRINT-PLAN-SXX"]
---

# Impediments Log — SXX

| ID | Impediment | Since | Owner | Impact | Status | Next step |
|---|---|---|---|---|---|---|
| IMP-001 | ... | YYYY-MM-DD | ... | High | Open | ... |
```

---

## `templates/sprints/sprint-review.md`
```markdown
---
id: "SPRINT-REVIEW-SXX"
title: "Sprint Review — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "draft"
related: ["SPRINT-PLAN-SXX","SPRINT-BACKLOG-SXX"]
---

# Sprint Review — SXX

## 1. Sprint Goal — status
- Czy cel został osiągnięty? (tak/nie + komentarz)

## 2. Delivered
- Lista dowiezionych elementów (linki do PR, dokumentów, release notes)

## 3. Not delivered / carry-over
- Co nie weszło i dlaczego

## 4. Feedback / decyzje
- Ustalenia i decyzje stakeholderów

## 5. Następne kroki
- Link do action items
```

---

## `templates/sprints/sprint-retro.md`
```markdown
---
id: "SPRINT-RETRO-SXX"
title: "Sprint Retrospective — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "draft"
related: ["SPRINT-PLAN-SXX"]
---

# Sprint Retrospective — SXX

## Went well
- ...

## To improve
- ...

## Action items
- AI-001 — owner — due
- AI-002 — owner — due
```

---

## `templates/sprints/sprint-action-items.md`
```markdown
---
id: "SPRINT-AI-SXX"
title: "Action Items — SXX"
project: "NAZWA_PROJEKTU"
owner: "Scrum Master"
status: "live"
related: ["SPRINT-RETRO-SXX"]
---

# Action Items — SXX

| ID | Action | Owner | Due | Status |
|---|---|---|---|---|
| AI-001 | ... | ... | YYYY-MM-DD | Open |
```

---

## `templates/sprints/sprint-scope-change.md`
```markdown
---
id: "SPRINT-CR-SXX-001"
title: "Sprint Scope Change Request — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Owner"
status: "draft"          # draft|approved|rejected
related: ["SPRINT-PLAN-SXX","SPRINT-BACKLOG-SXX"]
---

# Sprint Scope Change Request — SXX

## Zmiana
- Co dodajemy/usuwamy i dlaczego.

## Wpływ
- Na cel sprintu:
- Na terminy:
- Na ryzyko:

## Decyzja
- Approved/Rejected
- Approver: ...
- Date: ...
```

---

## `templates/sprints/sprint-metrics.md`
```markdown
---
id: "SPRINT-METRICS-SXX"
title: "Sprint Metrics — SXX"
project: "NAZWA_PROJEKTU"
owner: "Product Ops"
status: "draft"
related: ["SPRINT-PLAN-SXX"]
---

# Sprint Metrics — SXX

## Delivery
- Velocity: ...
- Burnup/Burndown: link do plików w `metrics/`

## Quality
- Defects found: ...
- Rework ratio: ...

## Docs / Governance
- Dokumenty zaktualizowane (lista linków)
```

---

## `templates/sprints/sprint-approval.md`
```markdown
---
id: "SPRINT-APPROVAL-SXX"
title: "Sprint Sign-off — SXX"
project: "NAZWA_PROJEKTU"
approver: "Product Owner / Sponsor"
date: "YYYY-MM-DD"
related: ["SPRINT-REVIEW-SXX","SPRINT-RETRO-SXX"]
---

# Sprint Sign-off — SXX

- **Approved by:** ...
- **Date:** ...
- **Notes:** ...
```

---

> Jeśli chcesz, można dopisać do sprintów także `daily/` (dzienniki dzienne) i `metrics/` (CSV), ale to jest opcjonalne i zależy od potrzeb audytowych.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: ROADMAP-*
    type: requires
    reason: "Sprint planning requires roadmap milestones and epic priorities"
    conditions:
      - when: "project.methodology === 'agile'"
        applies: true
      - when: "project.size < 'medium'"
        applies: false
    sections:
      - from: "Roadmap §4 Epics / Feature sets"
        to: "Sprint Plan §4 Backlog wybrany do sprintu"
        influence: "Roadmap epics define sprint backlog priorities"
      - from: "Roadmap §7 Capacity & Budget summary"
        to: "Sprint Plan §3 Capacity"
        influence: "Roadmap capacity constraints guide sprint capacity allocation"

  - id: SPRINT-DOR-*
    type: requires
    reason: "Sprint items must satisfy DoR before entering backlog"
    sections:
      - from: "Sprint DoR §1 Kryteria wejścia"
        to: "Sprint Backlog §1 Item selection"
        influence: "DoR validates items are ready for sprint commitment"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: SPRINT-REVIEW-*
    type: blocks
    reason: "Sprint review cannot occur without sprint execution and deliverables"
    conditions:
      - when: "sprint.phase === 'completed'"
        applies: true
    sections:
      - from: "Sprint Plan §1 Sprint Goal"
        to: "Sprint Review §1 Sprint Goal — status"
        influence: "Sprint goal defines success criteria for review"
      - from: "Sprint Backlog §1 Lista itemów"
        to: "Sprint Review §2 Delivered"
        influence: "Backlog items define what was delivered or not delivered"

  - id: SPRINT-RETRO-*
    type: blocks
    reason: "Retrospective requires completed sprint to analyze"
    sections:
      - from: "Sprint Review §4 Feedback"
        to: "Sprint Retro §2 To improve"
        influence: "Review feedback informs retrospective improvement areas"

  - id: SPRINT-ACTION-ITEMS-*
    type: informs
    reason: "Action items emerge from retrospective insights"
    sections:
      - from: "Sprint Retro §3 Action items"
        to: "Sprint Action Items §1 Lista akcji"
        influence: "Retrospective generates action items for process improvement"

  - id: TODO-*
    type: informs
    reason: "Sprint backlog items generate TODO artifacts for tracking"
    sections:
      - from: "Sprint Backlog §1 Lista itemów"
        to: "TODO §1 Description"
        influence: "Each backlog item may generate detailed TODO tracking"
```

### Related Documents

```yaml
related:
  - id: SPRINT-IMPEDIMENTS-*
    type: informs
    reason: "Impediments log tracks blockers affecting sprint progress"

  - id: SPRINT-METRICS-*
    type: informs
    reason: "Metrics track sprint velocity, quality, and lead time"

  - id: SPRINT-SCOPE-CHANGE-*
    type: informs
    reason: "Scope changes require formal change request process"

  - id: SPRINT-APPROVAL-*
    type: informs
    reason: "Sprint approval validates completion at gate checkpoints"
```

### Satellite Documents

```yaml
satellites:
  - type: TODO
    path: "satellites/todos/TODO-SPRINT-*.md"
    required: false
    purpose: "Track individual sprint backlog items and action items"

  - type: DoR
    path: "satellites/dor/DOR-SPRINT-*.md"
    required: true
    purpose: "Definition of Ready for sprint items"

  - type: DoD
    path: "satellites/dod/DOD-SPRINT-*.md"
    required: true
    purpose: "Definition of Done for sprint completion"

  - type: Evidence
    path: "satellites/evidence/EVIDENCE-SPRINT-*.md"
    required: false
    purpose: "Supporting data and metrics for sprint execution"
```
