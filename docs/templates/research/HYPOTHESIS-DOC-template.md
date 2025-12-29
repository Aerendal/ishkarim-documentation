# HYPOTHESIS-DOC: Hypothesis Document Template

---
**Meta (WYMAGANE):**
```yaml
id: HYPOTHESIS-XXX
doctype: HYPOTHESIS-DOC
status: draft  # draft | in-review | approved | rejected | validated | invalidated
version: "1.0"
owner: "[Imię Nazwisko (Rola)]"
project: "[Nazwa projektu]"
hypothesis_type: technical  # technical | business | ux | market | clinical
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [DOC-ID]
    type: [research_input | strategic_alignment | requires]
    reason: "[Dlaczego ta zależność istnieje]"

impacts:
  - id: [DOC-ID]
    type: [blocks | influences | informs]
    reason: "[Jaki wpływ ma ta hipoteza]"
```

---

## SEC-HYP-CONTEXT: Kontekst i motywacja

**Opis problemu/możliwości:**
[W 2-4 zdaniach opisz kontekst biznesowy lub techniczny, który prowadzi do tej hipotezy. Dlaczego to jest ważne teraz?]

**Dlaczego hipoteza a nie decyzja:**
[Wyjaśnij, dlaczego nie możemy od razu podjąć decyzji - co jest unknown/uncertain?]

**Business value:**
[Jaka wartość biznesowa jest oczekiwana, jeśli hipoteza zostanie potwierdzona?]
- Estimated impact: [np. "30% performance improvement", "$50K/year cost reduction", "20% conversion rate increase"]
- Strategic alignment: [Jak to wpływa na roadmap/strategy]

---

## SEC-HYP-STATEMENT: Stwierdzenie hipotezy (H0/H1)

### Hipoteza zerowa (H0)
[Stwierdzenie status quo - to, co zakładamy obecnie jako prawdę lub baseline]

**Przykład:**
```
H0: Migracja z PostgreSQL na MongoDB nie poprawi wydajności zapytań o więcej niż 10%.
```

### Hipoteza alternatywna (H1)
[Stwierdzenie tego, co chcemy udowodnić - oczekiwana zmiana/poprawa]

**Przykład:**
```
H1: Migracja z PostgreSQL na MongoDB poprawi wydajność zapytań o minimum 30% dla query pattern X.
```

### Falsifiability (Czy hipoteza jest falsyfikowalna?)
- [ ] Hipoteza jest konkretna i mierzalna
- [ ] Możemy jasno określić, kiedy H1 jest TRUE i kiedy FALSE
- [ ] Istnieje eksperyment, który może odrzucić H1

---

## SEC-HYP-ASSUMPTIONS: Założenia

**Założenia kluczowe:**
Lista założeń, które muszą być prawdziwe, aby hipoteza była ważna:

1. **[Założenie 1]**
   - Opis: [Co zakładamy]
   - Risk if false: [Co się stanie, jeśli to założenie jest błędne]
   - Validation method: [Jak możemy to zweryfikować]

2. **[Założenie 2]**
   - Opis: ...
   - Risk if false: ...
   - Validation method: ...

**Przykład:**
```
1. Dataset size
   - Opis: Zakładamy, że production dataset będzie podobny do PoC dataset (1-2M records)
   - Risk if false: Performance może być znacznie gorsza przy 10M+ records
   - Validation method: Test z realistic production-size dataset
```

---

## SEC-HYP-SUCCESS-CRITERIA: Kryteria sukcesu/porażki

### Kryteria akceptacji (H1 = TRUE)
Hipoteza jest **POTWIERDZONA**, jeśli:

- [ ] **[Kryterium 1]** - [Konkretna miara, np. "Query latency < 100ms"]
- [ ] **[Kryterium 2]** - [Konkretna miara, np. "P95 latency < 150ms"]
- [ ] **[Kryterium 3]** - [Konkretna miara, np. "Cost increase < 20%"]
- [ ] **[Kryterium 4]** - [Opcjonalne dodatkowe kryterium]

**Threshold sukcesu:** [Ile kryteriów musi być spełnionych? np. "Min. 3/4 kryteria"]

### Kryteria odrzucenia (H1 = FALSE)
Hipoteza jest **ODRZUCONA**, jeśli:

- [ ] **[Kryterium 1]** - [Co dyskwalifikuje hipotezę]
- [ ] **[Kryterium 2]** - [Np. "Cost increase > 50%"]

**Blocker criteria:** [Czy jakiekolwiek kryterium odrzucenia jest automatycznym blocker?]

### Edge cases i anomalie
[Jak obsługujemy przypadki graniczne? Np. "Jeśli wyniki są na granicy 28-32% improvement, co wtedy?"]

---

## SEC-HYP-METHODOLOGY: Metodologia walidacji

### Typ eksperymentu
- [x] A/B Test
- [ ] PoC (Proof of Concept)
- [ ] Spike Solution
- [ ] Benchmark
- [ ] User Research (interviews, surveys)
- [ ] Clinical Trial
- [ ] Market Test
- [ ] Inny: [Opisz]

### Procedura walidacji
**Krok po kroku:**

1. **Setup**
   - [Co trzeba przygotować? Environment, dataset, tools]

2. **Execution**
   - [Jak przeprowadzić eksperyment? Jakie testy uruchomić?]

3. **Data Collection**
   - [Jakie dane zbierać? Jakie metryki trackować?]

4. **Analysis**
   - [Jak analizować wyniki? Statistical significance? Threshold?]

### Dataset/Sample size
- **Size:** [Ile próbek? Np. "1,000 users", "1M records", "100 API calls"]
- **Representativeness:** [Czy próbka reprezentuje production?]
- **Statistical significance:** [Jaki poziom confidence? Np. "95% confidence, p < 0.05"]

### Environment
- **Test environment:** [Gdzie będzie przeprowadzony eksperyment? Staging? Production subset?]
- **Control group:** [Czy jest grupa kontrolna? Baseline?]

---

## SEC-HYP-RESOURCES: Wymagane zasoby

### Zespół
- **Owner:** [Kto prowadzi eksperyment]
- **Contributors:** [Kto wspiera - devs, data scientists, designers]
- **Approvers:** [Kto musi zaaprobować wyniki]

### Zasoby techniczne
- **Infrastructure:** [Jakie serwery, bazy danych, tools są potrzebne]
- **Tools:** [Jakie narzędzia - benchmarking tools, analytics platforms]
- **Access:** [Jakie uprawnienia są potrzebne - production data, cloud resources]

### Budget
- **Estimated cost:** [Koszt infrastructure, licenses, external services]
- **Budget approval:** [Czy budget jest approved? Przez kogo?]

---

## SEC-HYP-TIMELINE: Timeboxing

### Czas trwania
- **Start date:** [YYYY-MM-DD]
- **End date (deadline):** [YYYY-MM-DD]
- **Total duration:** [Np. "2 tygodnie", "1 miesiąc"]

### Milestones
| Milestone | Date | Status |
|-----------|------|--------|
| Setup complete | [YYYY-MM-DD] | ⏳ pending |
| Experiment running | [YYYY-MM-DD] | ⏳ pending |
| Data collected | [YYYY-MM-DD] | ⏳ pending |
| Analysis complete | [YYYY-MM-DD] | ⏳ pending |
| Results reviewed | [YYYY-MM-DD] | ⏳ pending |

### Timebox enforcement
**Jeśli eksperyment przekroczy deadline:**
- [ ] Automatyczne odrzucenie (zbyt długo = too risky)
- [ ] Extension możliwe (z approval)
- [ ] Pivot to different approach

**Contingency plan:**
[Co robimy, jeśli nie zdążymy? Skracamy scope? Cancelujemy?]

---

## Notatki dodatkowe (opcjonalne)

### Risks i mitigation
**Risk 1:** [Opis ryzyka]
- **Likelihood:** [Low/Medium/High]
- **Impact:** [Low/Medium/High]
- **Mitigation:** [Jak redukujemy ryzyko]

**Risk 2:** ...

### Dependencies
**Blokery:**
- [ ] [Co musi być gotowe przed rozpoczęciem eksperymentu]
- [ ] [Np. "Production-like dataset", "Staging environment access"]

### Stakeholder buy-in
**Kto musi zaaprobować:**
- [ ] [Rola/Osoba 1] - [Status: pending/approved]
- [ ] [Rola/Osoba 2] - [Status: pending/approved]

---

## TODO_SECTION (WYMAGANE)

**Następne kroki:**
- [ ] Przygotować setup eksperymentu - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] Uzyskać approval od [Stakeholder] - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] Utworzyć EXPERIMENT-LOG document - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] [Dodatkowe action items]

---

## EVIDENCE Satellite (WYMAGANE)

**Dokumenty wspierające:**
- E-XXX: [Tytuł dokumentu evidence - research, data, benchmarks]
- E-XXX: [Market analysis, user research]

---

## CHANGELOG (WYMAGANE)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [Imię Nazwisko] | Initial hypothesis created |
| 1.1 | YYYY-MM-DD | [Imię Nazwisko] | Updated success criteria based on feedback |

---

**Czas wypełnienia:** 30-60 minut
**Template version:** HYPOTHESIS-DOC v1.0
**Ostatnia aktualizacja:** 2025-12-29
