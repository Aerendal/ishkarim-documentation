# Szablon Sprintu — DISCOVERY / Research Spike

> Celem jest weryfikacja hipotezy; outputem jest decyzja/ADR, nie kod produkcyjny.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: PROJECT-CHARTER
    type: strategic_alignment
    from_sections:
      - innovation_goals
      - risk_appetite
    to_sections:
      - hypothesis_definition
      - experiment_scope
    influence: "Cel strategiczny projektu określa kierunki eksploracji"
    when:
      condition: sprint.type == "discovery"
      applies: always

  - id: BACKLOG
    type: research_input
    from_sections:
      - unknowns_list
      - technical_risks
      - market_hypotheses
    to_sections:
      - research_questions
      - experiment_design
    influence: "Niewiadome z backlogu determinują pytania badawcze"
    when:
      condition: sprint.has_unknowns == true
      applies: always

  - id: ROADMAP
    type: timing_constraint
    from_sections:
      - decision_deadlines
      - milestone_dependencies
    to_sections:
      - time_to_decision
      - experiment_timeline
    influence: "Roadmapa określa deadline na podjęcie decyzji"
    when:
      condition: roadmap.has_decision_dependency == true
      applies: conditionally
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: ADR
    type: decision_record
    from_sections:
      - experiment_results
      - recommendation
    to_sections:
      - context
      - decision
      - consequences
    influence: "Wyniki eksperymentu są udokumentowane w ADR"
    when:
      condition: sprint.completed == true
      applies: always

  - id: BACKLOG
    type: work_injection
    from_sections:
      - recommendation
      - next_steps
    to_sections:
      - new_user_stories
      - technical_tasks
    influence: "Decyzja Proceed/Pivot generuje nowe zadania w backlogu"
    when:
      condition: recommendation == "proceed" OR recommendation == "pivot"
      applies: conditionally

  - id: TECH-DEBT-REGISTER
    type: learnings
    from_sections:
      - prototype_code
      - technical_findings
    to_sections:
      - areas_to_improve
      - refactoring_needs
    influence: "Prototyp ujawnia obszary wymagające refaktoringu"
    when:
      condition: prototype.has_technical_findings == true
      applies: conditionally

  - id: SPRINT-CORE
    type: follow_up
    from_sections:
      - proceed_recommendation
      - implementation_plan
    to_sections:
      - sprint_backlog
      - acceptance_criteria
    influence: "Pozytywna rekomendacja prowadzi do sprintu delivery"
    when:
      condition: recommendation == "proceed"
      applies: conditionally
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: EXPERIMENT-DESIGN-DOC
    relationship: methodology
    sections_mapping:
      - from: scientific_method
        to: experiment_plan
    usage: "Metodyka eksperymentu zapewnia rzetelność wyników"

  - id: HYPOTHESIS-CANVAS
    relationship: input
    sections_mapping:
      - from: hypothesis_statement
        to: research_questions
    usage: "Canvas strukturyzuje hipotezy do przetestowania"

  - id: RESEARCH-ETHICS-CHECKLIST
    relationship: compliance
    sections_mapping:
      - from: ethics_guidelines
        to: experiment_constraints
    usage: "Etyka badań określa granice eksperymentów"
```

### Satellite Documents

```yaml
satellites:
  - name: EXPERIMENT-LOG
    purpose: "Dziennik obserwacji i wyników eksperymentu"
    trigger: during_experiment
    lifecycle: sprint_duration
    retention: permanent

  - name: PROTOTYPE-CODE
    purpose: "Kod prototypu/PoC (nie produkcyjny)"
    trigger: during_development
    lifecycle: spike_duration
    retention: 3_months

  - name: DATA-ANALYSIS-NOTEBOOK
    purpose: "Jupyter/R notebook z analizą danych"
    trigger: after_experiment
    lifecycle: analysis_phase
    retention: permanent

  - name: DECISION-LOG
    purpose: "Szczegółowe uzasadnienie decyzji Proceed/Pivot/Stop"
    trigger: at_closure
    lifecycle: single_event
    retention: permanent
```

---
## 0. Metryki nagłówka
- **Sprint ID**: `<YYYY‑MM‑DD / Spike‑N>`
- **Zespół / Obszar**: `<...>`
- **Czas trwania**: `<start → koniec>`
- **Capacity (osobodni)**: `<...>`
- **Tryb sprintu**: `discovery`

## 1. Cel sprintu (Hipoteza wartości)
- **Hipoteza**: `<Jeśli zrobimy X, to Y wzrośnie/spadnie, bo Z>`
- **Metryka sukcesu**: `<czas do wiedzy, np. odpowiedź TAK/NIE + dowód>`

## 2. Pytania badawcze i założenia
- **P1**: `<...>`
- **P2**: `<...>`
- **Założenia / ograniczenia**: `<...>`

## 3. Zakres eksperymentu
- **MUST**: `<najmniejszy eksperyment, który falsyfikuje hipotezę>`
- **SHOULD**: `<...>`
- **NICE**: `<...>`
- **Poza zakresem**: `<delivery/produkcja>`

## 4. Artefakty wyjściowe
- **Prototyp / PoC**: `<link/opis>`
- **Notatki z eksperymentu**: `<metodyka, wyniki>`
- **Rekomendacja**: `Proceed / Pivot / Stop`
- **ADR / Decision Log**: `<ID>`

## 5. DoR / DoD (Discovery)
### DoR
- [ ] Hipoteza i metryki zdefiniowane
- [ ] Kryteria falsyfikacji określone
- [ ] Zakres eksperymentu uzgodniony
- [ ] Ryzyka i etyka/zgodność ocenione
### DoD
- [ ] Prototyp/PoC ukończony i opisany
- [ ] Dane i wyniki zebrane i odtwarzalne
- [ ] Wniosek i ADR opublikowane
- [ ] Decyzja o dalszych krokach podjęta

## 6. Plan eksperymentu
- **Etapy**: `<projekt → eksperyment → analiza → wniosek>`
- **Zasoby / dane**: `<...>`
- **Ryzyka i kontyngencje**: `<...>`

## 7. Komunikacja
- **Przegląd wyników**: `<termin i forma>`
- **Stakeholderzy**: `<RACI>`

---
## Bramka „START”
- [ ] Hipoteza + metryki + kryteria falsyfikacji
- [ ] Zakres i dane dostępne
- [ ] Ryzyka zaakceptowane
## Bramka „CLOSE”
- [ ] ADR/wniosek opublikowany
- [ ] Decyzja „Proceed/Pivot/Stop”
- [ ] Wnioski przeniesione do backlogu
