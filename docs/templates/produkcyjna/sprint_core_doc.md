# Szablon Sprintu — CORE (Delivery)

> Minimalny, ale kompletny szablon sprintu „delivery". Uzupełnij wszystkie pola oznaczone `<>`.

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: PROJECT-CHARTER
    type: foundation
    from_sections:
      - project_goals
      - success_criteria
    to_sections:
      - sprint_goal
      - success_criteria
    influence: "Cele projektu definiują priorytety i cel sprintu"
    when:
      condition: sprint.type == "core"
      applies: always

  - id: ROADMAP
    type: planning
    from_sections:
      - quarterly_milestones
      - feature_priorities
    to_sections:
      - sprint_backlog
      - scope_definition
    influence: "Roadmapa determinuje zakres i priorytety prac w sprincie"
    when:
      condition: sprint.alignment_required == true
      applies: always

  - id: BACKLOG
    type: input
    from_sections:
      - prioritized_items
      - user_stories
      - technical_debt
    to_sections:
      - sprint_backlog
      - capacity_planning
    influence: "Backlog dostarcza konkretne zadania gotowe do realizacji"
    when:
      condition: sprint.planning_complete == false
      applies: always

  - id: TEAM-CAPACITY-DOC
    type: constraint
    from_sections:
      - available_hours
      - team_velocity
    to_sections:
      - capacity_osobodni
      - buffer_calculation
    influence: "Dostępność zespołu określa realny zakres sprintu"
    when:
      condition: sprint.planning_phase == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: RETROSPECTIVE-DOC
    type: feedback_loop
    from_sections:
      - sprint_execution
      - blockers_issues
      - velocity_achieved
    to_sections:
      - what_went_well
      - what_to_improve
      - action_items
    influence: "Przebieg sprintu dostarcza danych do analizy i ulepszeń"
    when:
      condition: sprint.completed == true
      applies: always

  - id: BACKLOG
    type: update
    from_sections:
      - incomplete_tasks
      - discovered_issues
      - technical_debt_created
    to_sections:
      - backlog_refinement
      - priority_changes
    influence: "Niedokończone zadania i nowe odkrycia wracają do backlogu"
    when:
      condition: sprint.has_carryover == true
      applies: conditionally

  - id: SPRINT-REVIEW
    type: presentation
    from_sections:
      - deliverables
      - demo_scenarios
      - acceptance_status
    to_sections:
      - stakeholder_feedback
      - acceptance_decisions
    influence: "Rezultaty sprintu są prezentowane i akceptowane przez stakeholderów"
    when:
      condition: sprint.review_scheduled == true
      applies: always

  - id: VELOCITY-METRICS
    type: measurement
    from_sections:
      - completed_story_points
      - team_capacity_actual
      - cycle_time
    to_sections:
      - team_velocity_trend
      - capacity_forecasting
      - predictability_index
    influence: "Dane sprintu aktualizują metryki i prognozy zespołu"
    when:
      condition: sprint.completed == true
      applies: always

  - id: RELEASE-NOTES
    type: documentation
    from_sections:
      - completed_features
      - bug_fixes
      - breaking_changes
    to_sections:
      - changelog_entries
      - user_documentation
    influence: "Ukończone prace są dokumentowane dla użytkowników"
    when:
      condition: sprint.has_deployable_changes == true
      applies: always
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: SPRINT-PLANNING-DOC
    relationship: prerequisite
    sections_mapping:
      - from: planning_output
        to: sprint_backlog
    usage: "Planowanie definiuje dokładny scope sprintu core"

  - id: DEFINITION-OF-DONE
    relationship: quality_gate
    sections_mapping:
      - from: acceptance_criteria
        to: task_completion_checks
    usage: "DoD weryfikuje czy zadania spełniają standardy jakości"

  - id: RISK-REGISTER
    relationship: monitoring
    sections_mapping:
      - from: sprint_risks
        to: risk_tracking
      - from: mitigation_plans
        to: contingency_actions
    usage: "Ryzyka sprintu są monitorowane i mitigowane"

  - id: CI-CD-PIPELINE-DOC
    relationship: execution
    sections_mapping:
      - from: deployment_strategy
        to: pipeline_configuration
    usage: "Pipeline automatyzuje deployment i weryfikację"
```

### Satellite Documents

```yaml
satellites:
  - name: DAILY-STANDUP-NOTES
    purpose: "Codzienne aktualizacje postępu i blokad"
    trigger: daily
    lifecycle: ephemeral
    retention: 2_weeks

  - name: SPRINT-BURNDOWN-CHART
    purpose: "Wizualizacja pozostałej pracy w czasie"
    trigger: daily_update
    lifecycle: sprint_duration
    retention: 3_months

  - name: IMPEDIMENTS-LOG
    purpose: "Śledzenie blokad i ich rozwiązań"
    trigger: as_needed
    lifecycle: sprint_duration
    retention: 6_months

  - name: TECHNICAL-DEBT-LOG
    purpose: "Rejestracja długu technicznego powstałego w sprincie"
    trigger: code_review
    lifecycle: continuous
    retention: permanent

  - name: SPRINT-BOARD
    purpose: "Wizualna tablica zadań (kanban/scrum board)"
    trigger: realtime
    lifecycle: sprint_duration
    retention: 1_month
```

---
## 0. Metryki nagłówka
- **Sprint ID**: `<YYYY‑MM‑DD / Sprint‑N>`
- **Zespół / Obszar**: `<nazwa zespołu>`
- **Czas trwania**: `<data start> → <data koniec>`
- **Capacity (osobodni)**: `planowane: <x> / dostępne: <y> / bufor: <z>`
- **Wersja produktu / strumień wartości**: `<np. WebApp 2.x>`
- **Tryb sprintu**: `delivery`

## 1. Cel sprintu (Sprint Goal)
- `<jedno zdanie biznesowo‑techniczne, mierzalne>`
- **Kryterium sukcesu (KPI/OKR)**: `<np. wzrost CR o 2 p.p.>`

## 2. Zakres i kontekst
- **Zakres (MUST/SHOULD/NICE)**:
  - MUST: `<...>`
  - SHOULD: `<...>`
  - NICE: `<...>`
- **Poza zakresem (Non‑Goals)**: `<...>`
- **Założenia / ograniczenia**: `<...>`

## 3. Backlog sprintu (Sprint Backlog)
Dla każdego elementu zapewnij kompletność DoR/DoD.

| ID | Typ | Tytuł | Story Points | Wartość | Ryzyko | Priorytet | Właściciel |
|---|---|---|---:|---|---|---|---|
|   |   |   |    |    |    |    |    |

### 3.1 Definition of Ready (DoR) – checklista
- [ ] Cel i wartość biznesowa opisane
- [ ] Kryteria akceptacji (GIVEN‑WHEN‑THEN)
- [ ] Zależności rozpoznane i zaplanowane
- [ ] Szacunek (SP/ideal hours) i koszt
- [ ] Ryzyka i plan mitigacji
- [ ] Wymogi jakości/bezpieczeństwa określone

### 3.2 Definition of Done (DoD) – checklista
- [ ] Kod + testy jednostkowe
- [ ] Testy integracyjne / e2e (jeśli dotyczy)
- [ ] Static analysis / SAST / lint / coverage ≥ `<X%>`
- [ ] Dokumentacja zaktualizowana (USER_GUIDE/CHANGELOG/ADR)
- [ ] SBOM/licencje (jeśli dotyczy)
- [ ] Deploy na środowisko docelowe + monitoring
- [ ] Akceptacja PO/Stakeholdera

## 4. Plan wykonania (Sprint Plan)
- **Mapa pracy**: `<kamienie milowe, punkty kontroli>`
- **Bufor techniczny**: `<%> czasu na dług/utrzymanie`
- **Strategia równoległości / WIP**: `<kto/co/kiedy>`

## 5. Zależności i integracje
- **Komponenty / zespoły zależne**: `<...>`
- **Interfejsy / kontrakty (API, wersje)**: `<...>`
- **Okna integracji / terminy**: `<...>`

## 6. Ryzyka i „What‑If” (kontyngencje)
| Ryzyko | Prawdop. | Wpływ | Właściciel | Mitigacja | Trigger | Plan B |
|---|---:|---:|---|---|---|---|
|   |     |     |         |          |         |       |

**Reguły automatyczne**
- If `<warunek>` → Then `<akcja>` → Because `<ograniczenie>`

## 7. Jakość, bezpieczeństwo, zgodność
- **Standardy kodu**: `<wersje narzędzi, konwencje>`
- **Testy**: `<zakres, progi, matryca przypadków>`
- **Bezpieczeństwo**: `SAST/DAST/secret scan, polityka zależności`
- **Dane (RODO/PII)**: `klasyfikacja, maskowanie, retencja`

## 8. CI/CD i środowiska
- **Strategia gałęzi / release**: `<trunk/GitFlow/...>`
- **Pipeline**: `build → test → scan → package → deploy → verify`
- **Środowiska**: `DEV / SIT / UAT / PROD` (adresy, dostęp, okna)
- **Rollback / feature flags**: `<procedura, SLA>`

## 9. Obserwowalność i SLO
- **Logi / metryki / ślady**: `<zakres i retencja>`
- **Alerting**: `<progi, kanały, dyżury>`
- **SLO/SLI**: `<np. 99.9% dostępności, P95 latency>`

## 10. Komunikacja i interesariusze
- **Rytuały**: `daily HH:MM`, `refinement`, `review`, `retro`
- **Kanały**: `<issue tracker, chat, email, tablica>`
- **RACI**: R `<...>` / A `<...>` / C `<...>` / I `<...>`

## 11. Dokumentacja i śledzenie zmian
- **Artefakty**: `ADR‑INDEX, RFC‑INDEX, CHANGELOG, RELEASE_NOTES`
- **Traceability**: `PBI ↔ commit ↔ build ↔ deploy ↔ ticket`
- **Wymogi audytu**: `<podpisy, zgody, licencje>`

## 12. Kryteria Review i Demo
- **Scenariusze demo (user‑journeys)**: `<...>`
- **Dane testowe**: `<...>`
- **Lista oczekiwań stakeholderów**: `<...>`

## 13. Retrospektywa (szablon)
- **Dane wejściowe**: `velocity, przepływ, defekty, SLA, wąskie gardła`
- **Co poszło dobrze / źle / zaskoczyło**: `<...>`
- **Akcje usprawniające (SMART, właściciel, data)**: `<...>`
- **Aktualizacja procesu / checklist**: `<...>`

## 14. Załączniki operacyjne (opcjonalne)
- **Mapa C4 (Context/Container/Component)**: `<skrót>`
- **Matryca zgodności**: `<RODO, ISO 27001, OWASP ASVS>`
- **Tablica decyzji eskalacyjnych**: `<progi, ścieżki>`

---
## Bramka „START” (gotowość)
- [ ] Cel sprintu zaakceptowany przez PO/Tech Lead
- [ ] Backlog z DoR ≥ 90% pozycji
- [ ] Capacity i bufor potwierdzone
- [ ] Zależności i okna integracji zarezerwowane
- [ ] Pipeline/środowiska sprawdzone (test deploy)
- [ ] Ryzyka z planem B i triggerami

## Bramka „CLOSE” (zamknięcie)
- [ ] Wszystkie PBI „Done” spełniają DoD
- [ ] Demo wykonane, wnioski zebrane
- [ ] CHANGELOG / RELEASE_NOTES zaktualizowane
- [ ] Metryki i raport retro opublikowane
- [ ] Akcje usprawniające dodane do backlogu
