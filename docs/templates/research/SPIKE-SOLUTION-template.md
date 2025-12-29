# SPIKE-SOLUTION: Spike Solution Template

---
**Meta (WYMAGANE):**
```yaml
id: SPIKE-XXX
doctype: SPIKE-SOLUTION
status: draft  # draft | in-progress | completed | answered
version: "1.0"
owner: "[Imię Nazwisko (Rola)]"
project: "[Nazwa projektu]"
spike_type: technical  # technical | ux | business | market | architectural
timebox: "[Max duration - np. 2-5 dni]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [SPRINT-BACKLOG-XXX]
    type: research_input
    reason: "Spike redukuje uncertainty przed implementacją user story"

impacts:
  - id: [USER-STORY-XXX]
    type: blocks
    reason: "Spike answer determinuje czy story może być implemented"
  - id: [ADR-XXX]
    type: influences
    reason: "Technical spike może prowadzić do ADR"
```

---

## SEC-SPIKE-QUESTION: Pytanie badawcze

### Główne pytanie
[JEDNO konkretne pytanie, na które spike ma odpowiedzieć - nie więcej!]

**Format:** "Czy możemy [ACTION] używając [TECHNOLOGY] aby osiągnąć [GOAL]?"

**Przykłady:**
```
- "Czy możemy użyć Rust WASM do przyspieszenia image processing <500ms?"
- "Czy React Server Components są kompatybilne z naszym current Next.js 13 setup?"
- "Czy możemy zintegrować Stripe Checkout w <2 tygodnie z current tech stack?"
```

### Context
[W 2-3 zdaniach: dlaczego to pytanie jest ważne teraz?]

---

## SEC-SPIKE-WHY: Dlaczego teraz (business value)

### Blocker/Trigger
**Co blokuje projekt:**
- User Story: [US-XXX] - [Tytuł]
- Blocker: [Czego nie wiemy? Co jest uncertain?]
- Risk jeśli nie robimy spike: [Co się stanie jeśli blind implementation?]

### Business value
**Jeśli spike answer = YES:**
- Value: [Np. "Możemy deliver US-123 w tym sprincie"]
- Impact: [Np. "30% faster user experience"]

**Jeśli spike answer = NO:**
- Alternative: [Co robimy zamiast?]
- Saved cost: [Ile oszczędzamy nie implementując wrong approach?]

### Urgency
**Deadline:** [Kiedy musimy znać odpowiedź?]
- Sprint deadline: [YYYY-MM-DD]
- Decision point: [Kiedy musimy podjąć decyzję - np. "Sprint Planning Meeting 2026-01-05"]

---

## SEC-SPIKE-APPROACH: Podejście

### Timebox
**Duration:** [Np. "3 dni robocze"]
- Start: [YYYY-MM-DD]
- End: [YYYY-MM-DD]
- **HARD STOP:** [Czy zatrzymujemy spike po deadline, czy extend?]

### Minimal scope
**Co jest MINIMUM do odpowiedzi na pytanie:**
- ✅ [Minimal feature 1 - must implement]
- ✅ [Minimal feature 2 - must implement]
- ❌ [Feature 3 - nice-to-have, ale OUT OF SCOPE dla spike]
- ❌ [Feature 4 - defer to implementation]

**Spike != Production code** - to jest disposable code, quick & dirty OK!

### Approach (krok po kroku)
**Plan spike (high-level):**

**Day 1:** [Co robimy - np. "Setup environment, initial prototype"]
- [ ] Setup [Tech/Tool]
- [ ] Minimal Hello World implementation
- [ ] Test basic integration

**Day 2:** [Co robimy - np. "Core feature implementation"]
- [ ] Implement [Key feature 1]
- [ ] Implement [Key feature 2]
- [ ] Benchmark performance

**Day 3:** [Co robimy - np. "Testing, evaluation"]
- [ ] Test edge cases
- [ ] Measure key metrics
- [ ] Document findings

### Success criteria
**Spike jest SUCCESS jeśli możemy ODPOWIEDZIEĆ na pytanie:**
- ✅ Clear YES/NO answer
- ✅ Confidence level >80% (nie guessing)
- ✅ Enough data dla decision (metrics, observations)

---

## SEC-SPIKE-FINDINGS: Odkrycia

### Obserwacje (chronological log)

---

#### [YYYY-MM-DD] Day 1 - Setup
**Co zrobiłem:**
[Opis aktywności - setup, initial code, first tests]

**Observations:**
- [Observation 1]: [Co zaobserwowałem]
- [Observation 2]: [Positive surprise / Issue / Blocker?]

**Status:** [On track / Behind / Blocker encountered]

---

#### [YYYY-MM-DD] Day 2 - Core implementation
**Co zrobiłem:**
[Opis implementation]

**Observations:**
- **Performance:** [Metryki - np. "180ms latency vs target 500ms ✅"]
- **Integration:** [Jak integracja działa? Issues?]
- **Developer experience:** [Czy to jest easy/hard do użycia?]

**Status:** [On track / Behind / Blocker]

---

#### [YYYY-MM-DD] Day 3 - Testing & evaluation
**Co zrobiłem:**
[Testy, edge cases, final evaluation]

**Key findings:**
1. **[Finding 1]:** ✅ [Positive result - np. "Performance 11x faster than JS"]
2. **[Finding 2]:** ❌ [Negative result - np. "Bundle size +2.5MB"]
3. **[Finding 3]:** ⚠️ [Trade-off - np. "Works ale requires lazy loading"]

**Metrics collected:**
| Metric | Result | Target | Status |
|--------|--------|--------|--------|
| [Metric 1] | [Value] | [Target] | ✅/❌ |
| [Metric 2] | [Value] | [Target] | ✅/❌ |

---

### Niespodzianki
**Positive surprises:**
- [Co było lepsze niż expected?]

**Negative surprises:**
- [Co było gorsze niż expected?]

**Unknowns (still):**
- [Co nadal nie wiemy? Follow-up spike potrzebny?]

---

## SEC-SPIKE-ANSWER: Odpowiedź na pytanie

### Answer: [YES / NO / YES with conditions / INCONCLUSIVE]

**Uzasadnienie (1-3 zdania):**
[Dlaczego YES lub NO? Na podstawie jakich danych?]

**Przykład - YES with conditions:**
```
Answer: YES z warunkami

Uzasadnienie:
WASM delivers 11x performance improvement (180ms vs 2000ms JS baseline),
ALE wymaga lazy loading (bundle size +2.5MB) i fallback dla IE users (6% traffic).
Akceptowalne dla 94% users - PROCEED z conditional implementation.
```

### Confidence level
- [ ] 95-100% confidence (very certain)
- [x] 80-95% confidence (confident, ale minor unknowns)
- [ ] 60-80% confidence (some uncertainty - może follow-up spike)
- [ ] <60% confidence (INCONCLUSIVE - więcej research needed)

### Trade-offs identified
**Jeśli YES with conditions - jakie trade-offs:**
| Trade-off | Impact | Mitigation |
|-----------|--------|------------|
| [Trade-off 1] | [HIGH/MEDIUM/LOW] | [Jak handleujemy] |
| [Trade-off 2] | [Impact] | [Mitigation] |

**Przykład:**
```
| Trade-off | Impact | Mitigation |
| Bundle size +2.5MB | MEDIUM | Lazy load WASM module |
| IE not supported | LOW | Fallback to JS (6% users) |
```

---

## SEC-SPIKE-ACTIONS: Akcje wynikowe

### Immediate actions
- [ ] **[Action 1]** - [Co robimy teraz - np. "Update US-123 z wynikami spike"] - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] **[Action 2]** - [Np. "Create ADR-045 dla formalnej decyzji"] - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] **[Action 3]** - [Np. "Split user story - WASM + fallback"] - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]

### Implementation plan (jeśli answer = YES)
**Jeśli proceed z implementation:**
1. [Step 1 - np. "Create production-ready WASM module"]
2. [Step 2 - np. "Implement lazy loading"]
3. [Step 3 - np. "Add fallback logic for unsupported browsers"]
4. [Step 4 - np. "Add browser compatibility tests"]

**Estimated effort:** [Np. "2 sprinty"]

### Alternative plan (jeśli answer = NO)
**Jeśli nie implementujemy:**
- Alternative approach: [Co robimy zamiast?]
- Impact: [Jak to wpływa na user story / roadmap?]

### Follow-up spikes (jeśli potrzebne)
- [ ] **Spike 2:** [Pytanie - jeśli spike odkrył nowe unknowns]
- [ ] **Spike 3:** [Inny aspekt wymagający research]

---

## CHANGELOG (WYMAGANE)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [Imię Nazwisko] | Spike started |
| 2.0 | YYYY-MM-DD | [Imię Nazwisko] | Spike completed - answer: YES with conditions |

---

**Czas wypełnienia:** 1-2 godziny (+ czas spike execution)
**Timebox enforcement:** MAX 2-5 dni robocze
**Template version:** SPIKE-SOLUTION v1.0
**Ostatnia aktualizacja:** 2025-12-29
