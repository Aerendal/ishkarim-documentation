# 📈 Diagram zależności dokumentacji — przepływ i porządek tworzenia

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Dokument przedstawia chronologiczny przepływ powstawania dokumentacji projektowej, zależności między nimi oraz które dokumenty są wejściem/wyjściem dla innych. Przygotowałem: 1) skrócony **diagram ASCII** dla szybkiego przeglądu, 2) **swimlane/timeline** (przedprodukcyjne → produkcyjne → operacje), 3) tabelę zależności (Nazwa | Faza | Zależności wejściowe | Generuje / wykorzystują dalej).

---

## Legendy
- →  oznacza "prowadzi do / jest wejściem dla" (dependency)
- ||  oznacza równoległe współistnienie
- (Ciągłe) oznacza dokument aktualizowany przez cały projekt

---

## 1) Skrócony diagram (ASCII)

```
IDEA/CONCEPT
  |
  |--> Executive Summary, Pitch Deck
  |--> Feasibility Study <-- Research Plan
  |--> Market Analysis
  |
  +--> Business Case, Financial Plan
           |
           +--> Project Charter --> Project Management Plan
                       |
                       +--> Procurement Plan, Training Plan, Communication Plan
                       |
    (go/no-go) --> START PROD

PRODUCTION PLANNING
  PRD <--- Business Case + Feasibility + Vision Document
  BRD <--- PRD (minimal scope)
  High-Level Architecture <--- PRD + Feasibility
  TDD <--- High-Level Architecture + PRD
  Security Plan, Data Management Plan <--- PRD + TDD
  Test Plan <--- PRD + TDD
  RTM <--- PRD + Test Plan
  ADRs (ciągłe) <-- decyzje architektoniczne z TDD

IMPLEMENTATION → RELEASE
  Implementation (kod) uses TDD, ADRs
  Runbook, Deployment Guide, Operational Manual <--- TDD + DevOps
  Release Management Plan <--- Test Plan + Runbook
  UAT Plan <--- PRD + Test Plan
  Performance Test Report, Test Summary Report <--- Test Plan
  API Documentation (ciągłe) <--- TDD

OPERATIONS & SUPPORT
  Monitoring & Observability Plan <--- Runbook + TDD
  SIRP, DRP, BCP <--- Security Plan + Operational Risk Assessment
  SLA, Service Catalog <--- Business Case + Resource Requirements
  Knowledge Base / Wiki (ciągłe) <--- wszystkie dokumenty + implementacja
  Postmortem / Retrospective Report --> lessons into Innovation Log, ADRs
```

---

## 2) Timeline / Swimlanes (Krótkie fazy i kluczowe dokumenty)

**Faza A — Przedprodukcyjna (Idea → decyzja inwestycyjna)**
- Najpierw: Research Plan, Market Analysis, Executive Summary, Pitch Deck
- Równolegle: Feasibility Study, Business Case, Financial Plan
- Na końcu fazy: Project Charter, Project Management Plan, Procurement & Training Plan

**Faza B — Planowanie produkcyjne (Start prac deweloperskich)**
- Wejścia: PRD (z Business Case, Feasibility, Vision), BRD
- Architektura: High-Level Architecture → TDD (szczegóły)
- Bezpieczeństwo/dane: Security Plan, Data Management Plan, DPIA
- Testy: Test Plan, RTM (mapowanie wymagań)

**Faza C — Implementacja & Wydanie**
- Implementacja zgodnie z TDD i ADRs
- Dokumenty operacyjne: Runbook, Deployment Guide, Operational Manual
- Release Management + UAT → Release
- Testy wydajnościowe i Test Summary

**Faza D — Operacje & Zamknięcie**
- Monitoring, Observability, SIRP/DRP/BCP aktywne
- SLA/Service Catalog/Support Guides utrzymywane
- Postmortem → Closure Report, Lessons -> Innovation Log, update ADRs/PRD

---

## 3) Tabela zależności (wybrane kluczowe dokumenty)

| Nazwa dokumentu | Faza | Zależności wejściowe (skąd czerpie dane) | Generuje / jest wejściem dla |
|---|---:|---|---|
| Research Plan | Przedprod. | Wymagania biznesowe, hipotezy | Feasibility, Market Analysis |
| Feasibility Study | Przedprod. | Research, Tech Assessment | Business Case, Project Charter |
| Business Case | Przedprod. | Feasibility, Market Analysis, Financials | PRD, CBA, Investor materials |
| PRD | Produkcyjna | Business Case, Vision, Market Analysis | BRD, HLA, Test Plan, RTM |
| High-Level Architecture (HLA) | Produkcyjna | PRD, Feasibility | TDD, ADRs, Security Plan |
| TDD | Produkcyjna | HLA, PRD | Dev implementation, API Docs, Runbook |
| Security Plan / DPIA | Produkcyjna | PRD, Data Mgmt | SIRP, DRP, BCP, Compliance Report |
| Test Plan | Produkcyjna | PRD, TDD | RTM, Test Summary, Release criteria |
| RTM | Produkcyjna | PRD, Test Plan | UAT, Acceptance |
| Runbook / Deployment Guide | Produkcyjna | TDD, DevOps configs | Release Management, Operational Manual |
| Release Management Plan | Produkcyjna | Test Plan, Runbook | Release, Change Management |
| Monitoring & Observability | Operacje | Runbook, TDD | Alerts, Incident Reports |
| SIRP / DRP / BCP | Operacje | Security Plan, Operational Risk Assessment | Incident Response, Communication |
| Postmortem / Retrospective | Zamknięcie | Release data, Incident Reports | Changes to ADR, Process improvements |

---

## 4) Zasady dobrego modelu przepływu dokumentów (krótkie wskazówki)
1. **Źródło prawdy:** PRD + TDD + RTM stanowią podstawową „trójcę” wymagań → implementacji → testów. Aktualizować wyłącznie w kontrolowany sposób.
2. **Deklaratywność:** dokumenty przedprodukcyjne muszą zawierać decyzje biznesowe (nie techniczne) — techniczne zapisy przenieść do TDD / ADR.
3. **Ciągłość:** ADR, API Docs, Knowledge Base oraz Change Log są dokumentami ciągłymi — powstają i ewoluują w trakcie implementacji.
4. **Automatyzacja:** tam gdzie możliwe, generować RTM, Change Log i Release Notes z narzędzi (Jira, Git, CI/CD).
5. **Weryfikacja:** przed przejściem między fazami (np. z przedprod. do prod.) wymusić checkpoint (CBA/Business Case + Feasibility + Project Charter zatwierdzone).

---

## 5) Jak mogę to zwizualizować dalej?
- Mogę wygenerować diagram SVG/PNG (graf DAG) z tymi zależnościami.
- Mogę przygotować wersję do wstawienia w Confluence / PowerPoint (slajd z flowchartem).

Jeśli chcesz, przygotuję wizualny diagram (graf) i wyeksportuję go jako plik obrazkowy — napisz proszę preferowany format (PNG/SVG) oraz czy chcesz podział na kolory/fazy.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: ALL-DOC-TYPES-*
    type: requires
    reason: "Dependency diagram requires knowledge of all document types to map relationships"
    conditions:
      - when: "project.has_documentation === true"
        applies: true
    sections:
      - from: "Document Type Catalog §All types"
        to: "§1 Skrócony diagram"
        influence: "Document types define nodes in dependency graph"

  - id: GATES-SPEC-*
    type: requires
    reason: "Diagram includes checkpoint gates that control flow between phases"
    sections:
      - from: "Gates Spec §All gates"
        to: "§2 Timeline / Swimlanes"
        influence: "Gates define phase transitions and approval points"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: PROJECT-PLANNING-*
    type: informs
    reason: "Dependency diagram guides project planning and document creation order"
    conditions:
      - when: "project.phase === 'planning'"
        applies: true
    sections:
      - from: "§2 Timeline / Swimlanes"
        to: "Project Plan §1 Document sequence"
        influence: "Swimlanes define which documents must precede others"
      - from: "§3 Tabela zależności"
        to: "Project Plan §2 Dependencies"
        influence: "Dependency table identifies blocking relationships"

  - id: ROADMAP-*
    type: informs
    reason: "Diagram informs roadmap milestones aligned with document phases"
    sections:
      - from: "§2 Timeline / Swimlanes"
        to: "Roadmap §3 Milestones & Releases"
        influence: "Phase structure guides milestone definition"

  - id: WORKFLOW-AUTOMATION-*
    type: informs
    reason: "Dependency graph enables automated workflow orchestration"
    conditions:
      - when: "project.has_automation === true"
        applies: true
    sections:
      - from: "§3 Tabela zależności"
        to: "Workflow Script §1 Dependency resolution"
        influence: "Dependency table defines execution order for automation"
```

### Related Documents

```yaml
related:
  - id: ASCII-DIAGRAM-*
    type: informs
    reason: "ASCII diagram provides text-based visualization of same dependencies"

  - id: DOKUMENTACJA-TABELA-*
    type: informs
    reason: "Comparison table complements dependency view with document details"

  - id: TOC-DOKUMENTACJA-*
    type: informs
    reason: "TOC provides navigational view of documents shown in diagram"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-DIAGRAM-*.md"
    required: false
    purpose: "Supporting analysis and examples validating dependency relationships"

  - type: TODO
    path: "satellites/todos/TODO-DIAGRAM-*.md"
    required: false
    purpose: "Track diagram updates as new document types are added"
```
