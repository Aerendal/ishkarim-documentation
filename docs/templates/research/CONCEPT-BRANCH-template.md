# CONCEPT-BRANCH: Concept Branch Document Template

---
**Meta (WYMAGANE):**
```yaml
id: CONCEPT-BRANCH-XXX
doctype: CONCEPT-BRANCH
status: draft  # draft | active | merged | killed | on-hold
version: "1.0"
owner: "[Imię Nazwisko (Rola)]"
project: "[Nazwa projektu]"
parent_concept: "[ID parent concept/hypothesis]"
branch_id: "[Unique branch identifier - np. 'transformer-approach']"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [PARENT-CONCEPT-XXX]
    type: requires
    reason: "Branch powstaje z istniejącego konceptu głównego"
  - id: [HYPOTHESIS-XXX]
    type: requires
    reason: "Branch testuje alternatywną hipotezę"

impacts:
  - id: [RESEARCH-FINDINGS-XXX]
    type: influences
    reason: "Wyniki z branchy są agregowane w Research Findings"
  - id: [ADR-XXX]
    type: blocks
    reason: "Decyzja merge/kill wymaga ADR"
```

---

## SEC-CB-DIVERGENCE: Punkt rozwidlenia (fork point)

### Parent concept
**ID parent:** [PARENT-CONCEPT-XXX lub HYPOTHESIS-XXX]

**Parent context:**
[W 2-3 zdaniach: jaki jest parent concept? Co już wiemy?]

**Przykład:**
```
Parent: HYPOTHESIS-003 - "AI model może przewidzieć customer churn z accuracy >80%"

Parent context:
Zespół bada różne architektury AI do predykcji churn. Parent hypothesis określa target
accuracy 80%, ale nie specyfikuje architektury. Mamy 2 główne podejścia do exploration:
Transformer-based vs Graph Neural Network (GNN).
```

### Fork point
**Kiedy fork:** [YYYY-MM-DD]

**Gdzie fork (decision point):**
[W którym momencie research powstały różne ścieżki?]

**Przykład:**
```
Fork point: Model architecture selection

W trakcie initial research (Week 1) zespół zidentyfikował 2 równorzędne podejścia:
- Transformer-based models (BERT/GPT-style)
- Graph Neural Networks (customer relationship graph)

Oba approaches są valid, ale fundamentalnie różne. Zamiast sequential exploration
(test A, then test B), decydujemy fork → parallel exploration.
```

### Parallel branches (jeśli więcej niż 2)
**Wszystkie branches w tym fork:**
| Branch ID | Owner | Approach | Status |
|-----------|-------|----------|--------|
| BRANCH-001 | [Name] | [Transformer] | ✅ Active |
| BRANCH-002 | [Name] | [GNN] | ✅ Active |
| BRANCH-003 | [Name] | [Hybrid] | 🚧 On-hold |

---

## SEC-CB-RATIONALE: Dlaczego nowa gałąź

### Dlaczego fork (nie sequential)?
**Uzasadnienie parallel exploration:**
- [Reason 1 - np. "Both approaches equally promising - nie można wybrać without data"]
- [Reason 2 - np. "Parallel exploration saves time (2 weeks vs 4 weeks sequential)"]
- [Reason 3 - np. "Different team members have expertise w różnych approaches"]

### Hypothesis tego brancha
**Branch-specific hypothesis:**
[Co konkretnie testuje TEN branch?]

**H0:** [Baseline assumption]
**H1:** [What this branch tries to prove]

**Przykład:**
```
Branch hypothesis (Transformer branch):

H0: Transformer model nie osiągnie accuracy >80% dla churn prediction
H1: Transformer model (fine-tuned BERT) osiągnie accuracy >80% z fast inference (<100ms)

Unique aspect tego brancha: Emphasis on fast inference (real-time API use case)
```

### Success criteria (branch-specific)
**Ten branch jest SUCCESS jeśli:**
- [ ] [Criterion 1 - np. "Accuracy >80%"]
- [ ] [Criterion 2 - np. "Inference time <100ms"]
- [ ] [Criterion 3 - np. "Training time <24h"]

---

## SEC-CB-APPROACH: Alternatywne podejście

### Technical approach (specific to this branch)
**Architektura:**
[Opisz arhitekturę/podejście tego brancha - czym różni się od innych branches?]

**Przykład - Transformer branch:**
```
Architecture: Fine-tuned BERT model

Approach:
1. Start z pre-trained BERT (bert-base-uncased)
2. Add classification head (binary: churn / no-churn)
3. Fine-tune on customer behavior data (180 features)
4. Optimize dla inference speed (TensorRT, quantization)

Key differentiator vs GNN branch:
- Transformer uses sequence data (customer actions over time)
- GNN uses graph structure (customer relationships)
```

### Dataset
**Data used:**
- Size: [Np. "100K customers, 2 years history"]
- Features: [Np. "180 features - demographics, behavior, transactions"]
- Split: [Np. "Train 70% / Val 15% / Test 15%"]

### Tools & stack
**Technology:**
| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Model | [BERT / GNN / etc] | [Dlaczego] |
| Framework | [PyTorch / TensorFlow] | [Dlaczego] |
| Training | [Cloud / Local] | [Dlaczego] |

---

## SEC-CB-PROGRESS: Progress tracking

### Timeline
**Duration:** [Start date] → [End date (estimated)]
- **Planned:** [Np. "4 tygodnie"]
- **Actual:** [Np. "4 tygodnie (on track)"]

### Milestones

| Milestone | Planned Date | Actual Date | Status | Notes |
|-----------|--------------|-------------|--------|-------|
| Setup & data prep | Week 1 | [YYYY-MM-DD] | ✅ Done | [Notes] |
| Model training | Week 2 | [YYYY-MM-DD] | ✅ Done | [Notes] |
| Optimization | Week 3 | [YYYY-MM-DD] | 🚧 In progress | [Notes] |
| Evaluation | Week 4 | [YYYY-MM-DD] | ⏳ Pending | [Notes] |

### Current status (as of [YYYY-MM-DD])
**Progress:** [Np. "75% complete - Week 3/4"]

**Latest results:**
- [Metric 1]: [Current value] - [vs target]
- [Metric 2]: [Current value] - [vs target]

**Przykład:**
```
Week 3 results (as of 2025-12-27):

- Accuracy: 78% (target: 80%) - ⚠️ Below target, ale improving
- Inference time: 50ms (target: <100ms) - ✅ Excellent!
- Training time: 18h (target: <24h) - ✅ Good

Status: Promising, accuracy 78% → tuning hyperparameters może dać 80%+
```

---

## SEC-CB-LEARNINGS: Learnings vs parent branch

### Co działa lepiej (vs parent/other branches)
**Advantages tego brancha:**
1. **[Advantage 1]:** [Co jest lepsze - z danymi]
   - This branch: [Value]
   - Other branch: [Value]
   - Improvement: [%]

**Przykład:**
```
1. Inference speed
   - Transformer branch: 50ms ✅
   - GNN branch: 300ms
   - Improvement: 6x faster

2. Training simplicity
   - Transformer: 18h single GPU ✅
   - GNN: 48h multi-GPU (more complex)
   - Improvement: Simpler infrastructure
```

### Co działa gorzej
**Disadvantages tego brancha:**
1. **[Disadvantage 1]:** [Co jest gorsze]
   - This branch: [Value]
   - Other branch: [Value]
   - Gap: [%]

**Przykład:**
```
1. Accuracy
   - Transformer: 78% (below 80% target)
   - GNN: 83% ✅ (above target)
   - Gap: -5% (GNN wins)
```

### Niespodzianki (unique to this branch)
**Odkrycia:**
- **Positive surprise:** [Co było lepsze niż expected]
- **Negative surprise:** [Co było gorsze niż expected]
- **Unexpected insight:** [Coś czego się nie spodziewaliśmy]

---

## SEC-CB-DECISION: Merge/Kill/Continue decision

### Current recommendation: [MERGE / KILL / CONTINUE / ON-HOLD]

**Uzasadnienie:**

#### If MERGE:
**Dlaczego merge:**
- ✅ [Reason 1 - np. "Best accuracy (83%) among all branches"]
- ✅ [Reason 2 - np. "Meets all success criteria"]

**Merge plan:**
- [Step 1 - np. "Integrate GNN model into production pipeline"]
- [Step 2 - np. "Deprecate Transformer branch"]
- [Step 3 - np. "Create ADR documenting decision"]

#### If KILL:
**Dlaczego kill:**
- ❌ [Reason 1 - np. "Accuracy 78% below target 80%"]
- ❌ [Reason 2 - np. "Other branch (GNN) clearly superior"]

**Lessons learned before killing:**
- [Learning 1 - co możemy zastosować w innych projektach]
- [Learning 2 - co unikać w przyszłości]

#### If CONTINUE:
**Dlaczego continue:**
- ⏳ [Reason - np. "Promising results (78%) - hyperparameter tuning może dać 80%+"]

**Next steps:**
- [ ] [Action 1 - np. "Week 4: Hyperparameter tuning"]
- [ ] [Action 2 - np. "Re-evaluate after tuning"]

#### If ON-HOLD:
**Dlaczego on-hold:**
- 🚧 [Reason - np. "Waiting for more data"]

**Resume condition:**
- [Condition - np. "Resume when dataset reaches 200K customers"]

---

### Comparison with other branches (final)

| Metric | This Branch (Transformer) | Other Branch (GNN) | Winner |
|--------|---------------------------|-------------------|--------|
| Accuracy | 78% | 83% (✅) | GNN |
| Inference speed | 50ms (✅) | 300ms | Transformer |
| Training complexity | Low (✅) | High | Transformer |
| Production readiness | High (✅) | Medium | Transformer |
| **VERDICT** | KILL (accuracy miss) | **MERGE** (meets all criteria) | **GNN** |

**Final decision:** [MERGE GNN branch, KILL Transformer branch]

**ADR required:** ✅ YES - Create ADR-045 documenting architecture decision

---

## TODO_SECTION (WYMAGANE)

**Następne kroki:**
- [ ] Finalize branch evaluation - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] Create RESEARCH-FINDINGS aggregating all branches - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] Create ADR-XXX documenting merge/kill decision - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] (If MERGE) Integration plan - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] (If KILL) Archive branch code & learnings - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]

---

## CHANGELOG (WYMAGANE)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | YYYY-MM-DD | [Imię Nazwisko] | Branch forked from parent |
| 1.5 | YYYY-MM-DD | [Imię Nazwisko] | Week 2 results - 78% accuracy |
| 2.0 | YYYY-MM-DD | [Imię Nazwisko] | Final evaluation - recommend KILL |

---

**Czas wypełnienia:** 1-2 godziny (initial) + continuous updates
**Template version:** CONCEPT-BRANCH v1.0
**Ostatnia aktualizacja:** 2025-12-29
