# TRADE-OFF-ANALYSIS: Structured Trade-off Analysis

---
**Meta (WYMAGANE):**
```yaml
id: TRADE-OFF-ANALYSIS-[NNN]
doctype: TRADE-OFF-ANALYSIS
status: [draft/in-review/approved/implemented]
version: "1.0"
owner: "[Analysis Owner Name]"
project: "[Project Name]"
decision_context: "[Kontekst decyzji, np. 'Database selection for analytics module']"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: POC-DOC-[NNN]
    type: influences
    reason: "PoC data feeds into trade-off scoring"
  - id: [REQUIREMENTS-DOC]
    type: requires
    reason: "Requirements define evaluation criteria"

impacts:
  - id: ADR-[NNN]
    type: blocks
    reason: "Trade-off analysis feeds into formal ADR"
  - id: [IMPLEMENTATION-DOC]
    type: informs
    reason: "Selected option determines implementation approach"
```

**Wymagane dokumenty satelitarne:**
- EVIDENCE-[NNN]: Dane wspierające scoring (benchmarki, PoC results, vendor data)
- APPROVAL-[NNN]: Formalne zatwierdzenie weighted criteria i final recommendation

---

## SEC-TA-DECISION: Decyzja do podjęcia

> **Cel:** Jasne sformułowanie decyzji, która wymaga trade-off analysis.

**Decision statement:**
[Opisz decyzję która wymaga podjęcia. Np. "Wybór message queue dla nowego event-driven architecture: RabbitMQ vs Kafka vs AWS SQS"]

**Kontekst biznesowy:**
[Dlaczego ta decyzja jest ważna? Jaki problem rozwiązuje?]

**Zakres:**
- **Obszar wpływu:** [np. "Analytics module", "Entire platform", "Team X"]
- **Timeline:** [Kiedy decyzja musi być podjęta i zaimplementowana]
- **Budget constraints:** [Jeśli dotyczy]

---

## SEC-TA-CRITERIA: Kryteria oceny (weighted)

> **Cel:** Zdefiniowanie kryteriów oceny z wagami odzwierciedlającymi ich względną ważność.

| Kryterium | Waga | Uzasadnienie | Measurement method |
|-----------|------|--------------|-------------------|
| **[Kryterium 1]** | X% | [Dlaczego to kryterium jest ważne i dlaczego taka waga] | [Jak będzie mierzone, np. "Benchmark results", "Vendor SLA"] |
| **[Kryterium 2]** | Y% | [Uzasadnienie] | [Metoda pomiaru] |
| **[Kryterium 3]** | Z% | [Uzasadnienie] | [Metoda pomiaru] |
| **[...]** | ... | [...] | [...] |
| **TOTAL** | 100% | | |

**Stakeholder input na wagi:**
- **[Stakeholder 1 - Role]:** [Zaproponowane wagi / komentarze]
- **[Stakeholder 2 - Role]:** [Zaproponowane wagi / komentarze]

**Validation:**
- [ ] Sum of weights = 100%
- [ ] All key stakeholders reviewed and approved criteria
- [ ] Measurement methods are objective and feasible

---

## SEC-TA-OPTIONS: Opcje (min 2)

> **Cel:** Opis wszystkich rozważanych opcji.

### Opcja 1: [Nazwa opcji]

**Opis:**
[Szczegółowy opis opcji]

**Key characteristics:**
- [Charakterystyka 1]
- [Charakterystyka 2]
- [Charakterystyka 3]

**Data sources:**
- [Źródło 1: benchmark, PoC, vendor data, etc.]
- [Źródło 2]

### Opcja 2: [Nazwa opcji]

**Opis:**
[Szczegółowy opis opcji]

**Key characteristics:**
- [Charakterystyka 1]
- [Charakterystyka 2]
- [Charakterystyka 3]

**Data sources:**
- [Źródło 1]
- [Źródło 2]

### Opcja 3: [Nazwa opcji, jeśli dotyczy]

**Opis:**
[Szczegółowy opis opcji]

**Key characteristics:**
- [Charakterystyka 1]
- [Charakterystyka 2]
- [Charakterystyka 3]

**Data sources:**
- [Źródło 1]
- [Źródło 2]

---

## SEC-TA-SCORING: Scoring matrix

> **Cel:** Quantitative scoring każdej opcji względem kryteriów.

**Skala oceny:** 1-10 (1 = najgorzej, 10 = najlepiej)

| Kryterium (waga) | [Opcja 1] | [Opcja 2] | [Opcja 3] |
|------------------|-----------|-----------|-----------|
| **[Kryterium 1]** (X%) | [Score]/10 ([Uzasadnienie/dane]) | [Score]/10 ([Uzasadnienie]) | [Score]/10 ([Uzasadnienie]) |
| **[Kryterium 2]** (Y%) | [Score]/10 ([Uzasadnienie/dane]) | [Score]/10 ([Uzasadnienie]) | [Score]/10 ([Uzasadnienie]) |
| **[Kryterium 3]** (Z%) | [Score]/10 ([Uzasadnienie/dane]) | [Score]/10 ([Uzasadnienie]) | [Score]/10 ([Uzasadnienie]) |
| **[...]** (...%) | .../10 | .../10 | .../10 |
| **TOTAL (weighted)** | **[X.XX]** | **[Y.YY]** | **[Z.ZZ]** |

**Scoring methodology:**
- [Opis jak scores były przypisywane, np. "Based on benchmark data from POC-042"]
- [Validation approach, np. "Scores reviewed by 3 team members independently"]

**Confidence levels:**
- **[Opcja 1]:** [High/Medium/Low] - [Dlaczego, np. "High - extensive PoC data"]
- **[Opcja 2]:** [High/Medium/Low] - [Dlaczego]
- **[Opcja 3]:** [High/Medium/Low] - [Dlaczego]

---

## SEC-TA-SENSITIVITY: Sensitivity analysis

> **Cel:** Analiza jak zmiana wag wpływa na ranking opcji.

**Purpose:** Understand robustness of recommendation - czy result zmienia się drastycznie przy small changes do wag?

### Scenario 1: [Nazwa scenariusza, np. "If throughput becomes critical (weight → 40%)"]

**Adjusted weights:**
| Kryterium | Original weight | New weight |
|-----------|----------------|------------|
| [Kryterium X] | X% | X'% |
| [Kryterium Y] | Y% | Y'% |

**New scores:**
- **[Opcja 1]:** [New score]
- **[Opcja 2]:** [New score]
- **[Opcja 3]:** [New score]

**Winner:** [Która opcja wygrywa w tym scenariuszu]

### Scenario 2: [Nazwa scenariusza]

**Adjusted weights:**
[Analogicznie jak Scenario 1]

**New scores:**
[...]

**Winner:** [...]

### Scenario 3: [Nazwa scenariusza, jeśli dotyczy]

[...]

**Sensitivity conclusion:**
[Czy recommendation jest robust (wygrywa w większości scenariuszy) czy fragile (zmienia się przy small changes)?]

---

## SEC-TA-RECOMMENDATION: Rekomendacja

> **Cel:** Clear recommendation z uzasadnieniem.

**Recommended option:** **[Opcja X]** (score: [X.XX])

### Uzasadnienie

**Why this option wins:**
1. [Powód 1, odniesienie do scoring]
2. [Powód 2]
3. [Powód 3]

**Margin of victory:**
- vs [Opcja Y]: +[Delta] points ([X%] better)
- vs [Opcja Z]: +[Delta] points ([X%] better)

**Robustness:**
[Czy recommendation holds w sensitivity analysis? Np. "Wins in 2/3 scenarios, loses only when operational overhead weight drops below 10%"]

### Warunki / Założenia

**Critical assumptions:**
1. [Założenie 1, np. "Throughput remains below 100K msg/s"]
2. [Założenie 2]

**Trigger points for re-evaluation:**
- **If [condition]** → revisit decision, consider [alternative option]
- **If [condition]** → [action]

### Alternative recommendation (if applicable)

**Second best:** [Opcja Y] (score: [Y.YY])

**When to consider alternative:**
[W jakich warunkach druga opcja może być lepsza]

---

## SEC-TA-TRADEOFFS: Key trade-offs

> **Cel:** Explicit articulation co zyskujemy i co tracimy wybierając recommended option.

| Trade-off dimension | Wybierając [Recommended option], zyskujemy... | ...ale tracimy... |
|---------------------|---------------------------------------------|------------------|
| **[Dimension 1]** | [Korzyść] | [Koszt/strata] |
| **[Dimension 2]** | [Korzyść] | [Koszt/strata] |
| **[Dimension 3]** | [Korzyść] | [Koszt/strata] |

**Overall trade-off assessment:**
[Czy trade-offs są acceptable? Czy są areas gdzie losses są concerning?]

**Mitigation strategies:**
- **[Trade-off X]:** [Jak zmitigować loss, jeśli możliwe]
- **[Trade-off Y]:** [Strategia mitigacji]

---

## Appendix: Supporting data (opcjonalne)

### Detailed benchmark results
[Linki do EVIDENCE documents, raw data, etc.]

### Stakeholder feedback
[Summary of feedback from key stakeholders na scores/weights]

### Eliminated options
[Opcje które were considered ale eliminated przed formal analysis - dlaczego]

---

**Szacowany czas wypełnienia:** 2-4 godziny (w zależności od złożoności)

**Wartość dodana:**
- ✅ Quantitative scoring (nie subjective opinions)
- ✅ Weighted criteria (stakeholders mogą debate weights, nie opinions)
- ✅ Sensitivity analysis (pokazuje robustness of recommendation)
- ✅ Transparent trade-offs (wszyscy wiedzą "co tracą")

**Kiedy używać:**
- Decisions z multiple competing criteria (performance vs cost vs maintainability)
- Decisions gdzie stakeholders mają różne priorities
- Decisions wymagające quantitative justification
- Complex technical/business decisions where data is available

**Kiedy NIE używać:**
- Simple binary decisions → użyj DECISION-LOG
- Qualitative comparisons (3+ vendors) → użyj OPTION-COMPARISON-MATRIX
- Immediate tactical decisions → użyj DECISION-LOG
- Launch/go-no-go decisions → użyj GO-NO-GO-DECISION
