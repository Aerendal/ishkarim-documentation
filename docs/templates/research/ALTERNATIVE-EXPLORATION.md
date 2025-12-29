# ALTERNATIVE-EXPLORATION: [Problem] - [Title]

---

## Document Metadata

```yaml
id: ALT-EXPLORATION-[XXX]
doctype: ALTERNATIVE-EXPLORATION
status: draft  # draft | in-analysis | in-review | approved | decided
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
problem_id: [Problem reference ID]
```

---

## Cross-References

```yaml
dependencies:
  - id: FEASIBILITY-STUDY
    type: influences
    reason: "Feasibility identyfikuje potrzebę eksploracji alternatyw"

impacts:
  - id: ADR
    type: blocks
    reason: "Wybór alternatywy wymaga formalnej decyzji (ADR)"
  - id: POC-DOC
    type: influences
    reason: "Top 2-3 alternatywy mogą wymagać PoC"
```

---

## SEC-ALT-PROBLEM: Problem do rozwiązania

### Problem Statement
[Jasne sformułowanie problemu, który wymaga rozwiązania]

### Context
[Kontekst biznesowy i techniczny problemu]

### Current State
[Jak obecnie adresujemy ten problem, jeśli w ogóle]

### Desired Outcome
[Jaki jest pożądany wynik/rozwiązanie]

### Stakeholders
- [Stakeholder 1]: [Interes w rozwiązaniu]
- [Stakeholder 2]: [Interes w rozwiązaniu]

---

## SEC-ALT-CONSTRAINTS: Ograniczenia i kryteria

### Hard Constraints (must-have)
- [ ] [Constraint 1] - [Uzasadnienie]
- [ ] [Constraint 2] - [Uzasadnienie]
- [ ] [Constraint 3] - [Uzasadnienie]

### Soft Constraints (nice-to-have)
- [ ] [Constraint 1] - [Uzasadnienie]
- [ ] [Constraint 2] - [Uzasadnienie]

### Evaluation Criteria
| Criterion | Weight | Description | Measurement |
|-----------|--------|-------------|-------------|
| [Criterion 1] | [X%] | [Opis] | [Jak mierzymy 1-10] |
| [Criterion 2] | [X%] | [Opis] | [Jak mierzymy 1-10] |
| [Criterion 3] | [X%] | [Opis] | [Jak mierzymy 1-10] |

**Total weight:** 100%

### Success Threshold
[Minimalna punktacja lub kryteria, które rozwiązanie musi spełnić]

---

## SEC-ALT-OPTIONS: Zidentyfikowane alternatywy (min 3)

### Option A: [Name]
**Type:** [Build | Buy | Partner | Hybrid]

**Description:**
[Krótki opis alternatywy]

**Key Characteristics:**
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

---

### Option B: [Name]
**Type:** [Build | Buy | Partner | Hybrid]

**Description:**
[Krótki opis alternatywy]

**Key Characteristics:**
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

---

### Option C: [Name]
**Type:** [Build | Buy | Partner | Hybrid]

**Description:**
[Krótki opis alternatywy]

**Key Characteristics:**
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

---

### Option D: [Name] (optional)
**Type:** [Build | Buy | Partner | Hybrid]

**Description:**
[Krótki opis alternatywy]

**Key Characteristics:**
- [Characteristic 1]
- [Characteristic 2]
- [Characteristic 3]

---

## SEC-ALT-ANALYSIS: Analiza każdej opcji

### Option A: [Name] - Detailed Analysis

#### Pros
- ✅ [Pro 1]
- ✅ [Pro 2]
- ✅ [Pro 3]

#### Cons
- ❌ [Con 1]
- ❌ [Con 2]
- ❌ [Con 3]

#### Technical Feasibility
**Rating:** [High | Medium | Low]
**Details:** [Szczegóły wykonalności technicznej]

#### Cost Analysis
| Item | One-time | Recurring (annual) | Notes |
|------|----------|-------------------|-------|
| Development | $[X] | - | [Notes] |
| Infrastructure | $[X] | $[Y]/year | [Notes] |
| Licenses | $[X] | $[Y]/year | [Notes] |
| Maintenance | - | $[Y]/year | [Notes] |
| **Total** | **$[X]** | **$[Y]/year** | |

**3-year TCO:** $[Total Cost of Ownership]

#### Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

#### Dependencies
- [Dependency 1]
- [Dependency 2]

#### Time to Implementation
**Estimated:** [X weeks/months]
**Timeline breakdown:**
- [Phase 1]: [Duration]
- [Phase 2]: [Duration]

---

### Option B: [Name] - Detailed Analysis

#### Pros
- ✅ [Pro 1]
- ✅ [Pro 2]
- ✅ [Pro 3]

#### Cons
- ❌ [Con 1]
- ❌ [Con 2]
- ❌ [Con 3]

#### Technical Feasibility
**Rating:** [High | Medium | Low]
**Details:** [Szczegóły wykonalności technicznej]

#### Cost Analysis
| Item | One-time | Recurring (annual) | Notes |
|------|----------|-------------------|-------|
| Development | $[X] | - | [Notes] |
| Infrastructure | $[X] | $[Y]/year | [Notes] |
| Licenses | $[X] | $[Y]/year | [Notes] |
| Maintenance | - | $[Y]/year | [Notes] |
| **Total** | **$[X]** | **$[Y]/year** | |

**3-year TCO:** $[Total Cost of Ownership]

#### Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

#### Dependencies
- [Dependency 1]
- [Dependency 2]

#### Time to Implementation
**Estimated:** [X weeks/months]

---

### Option C: [Name] - Detailed Analysis

#### Pros
- ✅ [Pro 1]
- ✅ [Pro 2]
- ✅ [Pro 3]

#### Cons
- ❌ [Con 1]
- ❌ [Con 2]
- ❌ [Con 3]

#### Technical Feasibility
**Rating:** [High | Medium | Low]
**Details:** [Szczegóły wykonalności technicznej]

#### Cost Analysis
| Item | One-time | Recurring (annual) | Notes |
|------|----------|-------------------|-------|
| Development | $[X] | - | [Notes] |
| Infrastructure | $[X] | $[Y]/year | [Notes] |
| Licenses | $[X] | $[Y]/year | [Notes] |
| Maintenance | - | $[Y]/year | [Notes] |
| **Total** | **$[X]** | **$[Y]/year** | |

**3-year TCO:** $[Total Cost of Ownership]

#### Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

#### Dependencies
- [Dependency 1]
- [Dependency 2]

#### Time to Implementation
**Estimated:** [X weeks/months]

---

## SEC-ALT-COMPARISON: Porównanie (matrix)

### Scoring Matrix

| Criterion (weight) | Option A | Option B | Option C | Option D |
|-------------------|----------|----------|----------|----------|
| **[Criterion 1]** ([X%]) | [Score]/10 | [Score]/10 | [Score]/10 | [Score]/10 |
| **[Criterion 2]** ([X%]) | [Score]/10 | [Score]/10 | [Score]/10 | [Score]/10 |
| **[Criterion 3]** ([X%]) | [Score]/10 | [Score]/10 | [Score]/10 | [Score]/10 |
| **[Criterion 4]** ([X%]) | [Score]/10 | [Score]/10 | [Score]/10 | [Score]/10 |
| **[Criterion 5]** ([X%]) | [Score]/10 | [Score]/10 | [Score]/10 | [Score]/10 |
| **TOTAL (weighted)** | **[X.XX]** | **[X.XX]** | **[X.XX]** | **[X.XX]** |

**Winner:** [Option X] with score [X.XX]/10

### Visual Comparison

**Cost vs Value:**
```
High Value │     B
           │
           │ A
           │
Low Value  │         C
           └──────────────
           Low Cost  High Cost
```

**Risk vs Reward:**
```
High Reward │   A
            │      B
            │
            │
Low Reward  │         C
            └──────────────
            Low Risk  High Risk
```

### Trade-offs Summary
[Najważniejsze trade-offy między opcjami]

---

## SEC-ALT-RECOMMENDATION: Rekomendacja z uzasadnieniem

### Recommended Option: [Option X]

### Uzasadnienie
[Szczegółowe uzasadnienie wyboru]

**Kluczowe czynniki decyzyjne:**
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

**Why this option wins:**
- ✅ [Reason 1]
- ✅ [Reason 2]
- ✅ [Reason 3]

**Acknowledged weaknesses:**
- ⚠️ [Weakness 1] - [How we'll address]
- ⚠️ [Weakness 2] - [How we'll address]

### Confidence Level
**[High | Medium | Low]**

[Uzasadnienie poziomu pewności]

### Conditions for Success
1. [Condition 1]
2. [Condition 2]
3. [Condition 3]

### Alternative Recommendation (Plan B)
**If [condition], then consider:** [Option Y]

---

## SEC-ALT-REJECTED: Odrzucone opcje i dlaczego

### Option B: [Name] - REJECTED
**Primary reason:** [Main reason for rejection]

**Additional reasons:**
- [Reason 1]
- [Reason 2]

**Could be reconsidered if:**
- [Condition 1]
- [Condition 2]

---

### Option C: [Name] - REJECTED
**Primary reason:** [Main reason for rejection]

**Additional reasons:**
- [Reason 1]
- [Reason 2]

**Could be reconsidered if:**
- [Condition 1]
- [Condition 2]

---

## Next Steps

### Immediate Actions
- [ ] [Action 1] - [Owner] - [Deadline]
- [ ] [Action 2] - [Owner] - [Deadline]

### Documentation Required
- [ ] Create [ADR-XXX]: [Decision title]
- [ ] Create [POC-DOC-XXX] for recommended option (if needed)
- [ ] Update [TDD] with chosen approach

### Validation Required
- [ ] [Validation 1]: [Description]
- [ ] [Validation 2]: [Description]

### Stakeholder Alignment
- [ ] Present to [Stakeholder 1]
- [ ] Get approval from [Stakeholder 2]

---

## TODO_SECTION: Zadania

### Do zrobienia
- [ ] [Zadanie 1]
- [ ] [Zadanie 2]

### W trakcie
- [Zadanie obecnie realizowane]

### Zrealizowane
- [x] [Zadanie zakończone 1]
- [x] [Zadanie zakończone 2]

---

## EVIDENCE: Dowody i materiały

### Research Materials
- [Research doc 1]: [Link]
- [Research doc 2]: [Link]

### Vendor/Product Information
- [Vendor 1 documentation]: [Link]
- [Vendor 2 pricing]: [Link]

### Benchmark Data
- [Benchmark 1]: [Link]
- [Benchmark 2]: [Link]

### Expert Opinions
- [Expert 1]: [Quote/Summary]
- [Expert 2]: [Quote/Summary]

---

## APPROVAL: Zatwierdzenia

| Role | Name | Decision | Date | Comments |
|------|------|----------|------|----------|
| [Tech Lead] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |
| [Product Owner] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |
| [CTO/Architect] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Initial options identified |
| YYYY-MM-DD | 1.5 | [Imię Nazwisko] | Analysis completed |
| YYYY-MM-DD | 2.0 | [Imię Nazwisko] | Recommendation added |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, kontekst, założenia]

---

## Example: Technology Selection

**Problem:** Choose database for analytics module

**Options:**
- Option A: Elasticsearch (score: 8.65)
- Option B: ClickHouse (score: 7.55)
- Option C: TimescaleDB (score: 6.85)

**Recommendation:** Elasticsearch

**Rationale:**
- Team has 5+ years experience with Elasticsearch
- Ecosystem tooling (Kibana) is excellent
- Migration from existing setup is minimal
- Performance gap acceptable for our use case

**Rejected:**
- ClickHouse: Requires 3+ months team training
- TimescaleDB: Overkill for our use case

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** decision-support
