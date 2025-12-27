# 📊 Pełny diagram zależności dokumentacji (ASCII) — z checkpointami

> Powiązana rozmowa: [zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji](../../zbiór-rozmów-do-przetworzenia-kiedyś-szablony-dokumentacji--szablony-dokumentacji.md)
>
> Katalog szablonów: [dokumentacja_typy.md](dokumentacja_typy.md)


Poniżej znajdziesz szczegółowy, **pełny diagram ASCII** opisujący kolejność powstawania dokumentów, ich zależności wejściowe/wyjściowe i przepływ danych między fazami projektu — rozszerzony o **checkpointy (gate review)** z kryteriami i odpowiedzialnymi za decyzję.

---

## Legendy

- `=>` oznacza przepływ / "prowadzi do" (dependency)
- `||` oznacza równoległe tworzenie
- `(ciągłe)` dokument aktualizowany przez cały cykl
- Fazy: [PRZEDPROD] → [PRODUKCJA] → [WDROŻENIE] → [OPERACJE] → [ZAMKNIĘCIE]
- `[CHECKPOINT: NAZWA]` — punkt decyzyjny, wymagane kryteria i akceptacja

---

## ASCII Diagram (szeroki przepływ poziomy) z checkpointami

```
[PRZEDPROD]

  (Idea / Hipoteza)
       |
       +--> [Research Plan] ------------------+
       |                                       |
       +--> [Market Analysis] -----------------+--> [Feasibility Study] --> [Business Case] --> [Project Charter]
       |                                       |                                              |
       +--> [Executive Summary / Pitch Deck] --+                                              +--> [Project Management Plan]
                                                                                                     |
                                                                                                     +--> [Procurement Plan]
                                                                                                     +--> [Training Plan]
                                                                                                     +--> [Communication Plan]
                                                                                                     
  [CHECKPOINT: GO / NO-GO]
    - Kryteria: kompletna Feasibility Study, Business Case z podstawowymi projekcjami finansowymi, minimalne ryzyka opisane, rekomendacja (go/no-go).
    - Akceptuje: Sponsor projektu + CFO + Head of Product.
    - Jeśli "go": podpisanie Project Charter i start fazy PRODUKCJA.

-----------------------------------------------------------------------------------------------
[PRODUKCJA]

  [Business Case] --> [PRD] --------------------+--> [BRD]
                                                 |
                                                 +--> [Vision Document]
                                                 |
                                                 +--> [High-Level Architecture (HLA)] --> [TDD]
                                                                                |                |
                                                                                |                +--> [API Documentation] (ciągłe)
                                                                                |                +--> [Runbook / Deployment Guide]
                                                                                |                +--> [Operational Manual]
                                                                                |
                                                 +--> [Security Plan] <-- [DPIA]
                                                 |                |        |
                                                 |                |        +--> [SIRP / DRP / BCP]
                                                 |                |
                                                 +--> [Data Management Plan] --> [Data Governance Policy]

  [PRD] + [TDD] --> [Test Plan] --> [RTM] --> [UAT Plan]
                     |             |
                     |             +--> [Test Summary Report]
                     |
                     +--> [Performance Test Report]

  [HLA/TDD] --> [ADRs] (ciągłe decyzje architektoniczne)

  [CHECKPOINT: REQUIREMENTS FREEZE]
    - Kryteria: PRD zatwierdzony, RTM pokrywa wszystkie wymagania krytyczne, BRD potwierdzone, bezpieczeństwo (DPIA) ma plan mitigacji.
    - Akceptuje: Product Owner + Architect + Security Lead.
    - Skutek: zablokowanie zmian zakresu bez formalnego Change Request.

-----------------------------------------------------------------------------------------------
[WDROŻENIE]

  [TDD] + [Runbook] + [Test Plan]  --> [Release Management Plan] --> [Release]
                                          |
                                          +--> [Change Management Plan]
                                          +--> [Configuration Management Plan]

  [Release] --> [Deployment Guide] --> [Operational Manual]
               [API Documentation] (aktualizacja)

  [CHECKPOINT: RELEASE READINESS / PRE-DEPLOY]
    - Kryteria: wszystkie testy krytyczne (funkcjonalne, integracyjne, performance) zakończone i zaakceptowane; Test Summary Report i Performance Report w zielonej strefie; Runbook i Deployment Guide dostępne; plan rollbacku przetestowany.
    - Akceptuje: Release Manager + QA Lead + DevOps Lead + Product Owner.
    - Skutek: autoryzacja wdrożenia do środowiska produkcyjnego.

-----------------------------------------------------------------------------------------------
[OPERACJE]

  [Runbook] + [Operational Manual] --> [Monitoring & Observability Plan] --> [Alerts / Incidents]
                                                        |                                   |
                                                        +--> [Incident Report] --------------+
                                                        |                                   +--> [Postmortem / Retrospective]
                                                        +--> [SLA / Service Catalog]

  [Security Plan] + [Operational Risk Assessment] --> [SIRP / DRP / BCP]

  (ciągłe) [Knowledge Base / Wiki]  <--- aktualizuje: PRD, TDD, ADR, Runbook, Release Notes

  [CHECKPOINT: OPERATIONS HANDOVER]
    - Kryteria: Operational Manual i Runbook zatwierdzone; Monitoring & Alerts wdrożone; SLA ustalone; zespoły wsparcia przeszkolone (Training Materials).
    - Akceptuje: Head of Operations + DevOps Lead + Product Owner.
    - Skutek: formalne przekazanie systemu do trybu produkcyjnego i wsparcia.

-----------------------------------------------------------------------------------------------
[ZAMKNIĘCIE]

  [Postmortem / Retrospective] --> [Closure Report] --> archiwizacja do Knowledge Base
  [Postmortem] --> feed to [Innovation Log] and update [ADRs], [PRD] lessons

  [CHECKPOINT: PROJECT CLOSURE]
    - Kryteria: wszystkie kluczowe deliverables zaakceptowane; otwarte ryzyka pod kontrolą lub udokumentowane; Closure Report przygotowany; lessons learned z Postmortem wdrożone lub zaplanowane.
    - Akceptuje: Sponsor projektu + Project Manager + Business Owner.
    - Skutek: formalne zamknięcie projektu i archiwizacja dokumentów.

-----------------------------------------------------------------------------------------------
```

---

## Dodatkowe kryteria i wskazówki dla checkpointów

- **Konsystencja dokumentów:** przed akceptacją checkpointu sprawdź spójność numeracji wersji (wersjonowanie semantyczne) między PRD, TDD, RTM i Test Plan.
- **Dowody testów:** do Pre-Deploy wymagane są artefakty testowe: zrzuty z CI, raporty z testów automatycznych, dane z monitoringu testowego.
- **Bezpieczeństwo i zgodność:** DPIA, Security Plan i Compliance Report muszą być przeglądnięte przez DPO / Security Officer przed RELEASE READINESS.
- **Formalność akceptacji:** każda akceptacja powinna być odnotowana podpisem (elektronicznym) i wersjonowana w Change Log.

---

## Co mogę jeszcze dodać?

- Wykonać wyciąg checkpointów w oddzielnej tabeli CSV z kolumnami: Nazwa checkpointu | Kryteria | Akceptuje | Dokumenty wejściowe | Dokumenty wyjściowe.
- Przygotować skrócony widok ASCII tylko z checkpointami i kryteriami (do druku na warsztat).
- Zamienić ASCII na graficzny diagram z widocznymi gate’ami (PNG/SVG).

Napisz, którą z tych opcji wybierasz lub jeśli chcesz dopasować kryteria do wewnętrznych procedur — wprowadzę zmiany.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: DIAGRAM-ZALEZNOSCI-*
    type: requires
    reason: "ASCII diagram is text representation of dependency diagram"
    conditions:
      - when: "visualization.format === 'text'"
        applies: true
    sections:
      - from: "Diagram Zależności §1 Skrócony diagram"
        to: "§1 ASCII Diagram"
        influence: "Visual diagram defines structure for ASCII representation"
      - from: "Diagram Zależności §2 Timeline"
        to: "§1 ASCII Diagram (swimlanes)"
        influence: "Timeline swimlanes map to ASCII phase sections"

  - id: GATES-SPEC-*
    type: requires
    reason: "ASCII diagram includes checkpoint gates with criteria"
    sections:
      - from: "Gates Spec §All gates"
        to: "§1 CHECKPOINT sections"
        influence: "Gate specifications define checkpoint criteria in diagram"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: PROJECT-DOCUMENTATION-*
    type: informs
    reason: "ASCII diagram provides accessible flow reference for documentation"
    conditions:
      - when: "team.prefers_text === true"
        applies: true
    sections:
      - from: "§1 ASCII Diagram with checkpoints"
        to: "Project Documentation §1 Flow guide"
        influence: "ASCII format enables easy copy-paste to planning docs"

  - id: GATE-CHECKLIST-*
    type: informs
    reason: "Checkpoint definitions inform gate checklist creation"
    sections:
      - from: "§1 CHECKPOINT sections"
        to: "Gate Checklist §All checkpoints"
        influence: "Checkpoint criteria define gate acceptance requirements"

  - id: WORKFLOW-SEQUENCE-*
    type: informs
    reason: "ASCII diagram flow guides workflow task sequencing"
    sections:
      - from: "§1 ASCII Diagram phases"
        to: "Workflow Sequence §1 Task order"
        influence: "Phase transitions define workflow stage gates"
```

### Related Documents

```yaml
related:
  - id: DIAGRAM-ZALEZNOSCI-*
    type: informs
    reason: "Visual diagram provides graphical alternative to ASCII"

  - id: DOKUMENTACJA-TABELA-*
    type: informs
    reason: "Comparison table provides detailed document attributes"

  - id: GATES-SPEC-*
    type: informs
    reason: "Gates specification provides full checkpoint definitions"
```

### Satellite Documents

```yaml
satellites:
  - type: Evidence
    path: "satellites/evidence/EVIDENCE-ASCII-DIAGRAM-*.md"
    required: false
    purpose: "Examples of checkpoint execution and gate decisions"

  - type: TODO
    path: "satellites/todos/TODO-ASCII-DIAGRAM-*.md"
    required: false
    purpose: "Track diagram updates for new phases or checkpoints"
```
