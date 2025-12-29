# DECISION-REVERSAL: Decision Reversal Document

---
**Meta (WYMAGANE):**
```yaml
id: DECISION-REVERSAL-[Original-Decision-ID]
doctype: DECISION-REVERSAL
status: [draft/in-review/approved/implemented]
version: "1.0"
owner: "[Reversal Owner Name]"
project: "[Project Name]"
original_decision_id: "[ID of original decision being reversed]"
original_decision_date: "YYYY-MM-DD"
reversal_date: "YYYY-MM-DD"
reversal_reason: "[Brief summary, np. 'Performance issues at scale']"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [ORIGINAL-ADR/DECISION-LOG]
    type: requires
    reason: "Decision Reversal wymaga reference do original decision"
  - id: [EVIDENCE-OF-FAILURE]
    type: requires
    reason: "Evidence showing why original decision failed"

impacts:
  - id: [NEW-ADR]
    type: blocks
    reason: "Reversal tworzy nowy ADR z updated decision"
  - id: [MIGRATION-PLAN]
    type: blocks
    reason: "Reversal wymaga migration plan do new state"
```

**Wymagane dokumenty satelitarne:**
- APPROVAL-[NNN]: Formal approval dla reversal (especially if significant cost/impact)
- EVIDENCE-[NNN]: Data showing original decision failure (metrics, incidents, feedback)

---

## SEC-DR-ORIGINAL: Oryginalna decyzja (link)

> **Cel:** Clear reference do original decision która jest teraz reversed.

**Original decision ID:** [ORIGINAL-DECISION-ID]

**Original decision document:** [Link do original ADR/DECISION-LOG]

**Decision date:** [YYYY-MM-DD]

**Decision owner (original):** [Kto podjął original decision]

---

### What was decided

**Original decision statement:**
[1-2 zdania: co było decided originally]

**Selected option:** [Która opcja została wybrana]

**Alternatives rejected (originally):**
1. [Opcja A] - rejected because [reason]
2. [Opcja B] - rejected because [reason]

---

### Original rationale

**Why this decision was made:**
[Podsumowanie original rationale - dlaczego wydawało się to dobrą decyzją]

**Key assumptions:**
1. [Założenie 1 które uzasadniało original decision]
2. [Założenie 2]
3. [Założenie 3]

**Expected outcomes:**
- [Expected outcome 1]
- [Expected outcome 2]
- [Expected outcome 3]

---

### Implementation timeline

**Decision approved:** [YYYY-MM-DD]
**Implementation started:** [YYYY-MM-DD]
**Implementation completed:** [YYYY-MM-DD]
**Time in production:** [X months/weeks przed reversal]

---

## SEC-DR-WHY-WRONG: Dlaczego decyzja była błędna

> **Cel:** Honest assessment dlaczego original decision nie sprawdziła się.

**Summary:**
[2-3 zdania high-level summary dlaczego decision failed]

---

### Problem 1: [Nazwa problemu]

**What went wrong:**
[Szczegółowy opis problemu]

**Expected vs Reality:**
- **Expected:** [Co zakładaliśmy że się stanie]
- **Reality:** [Co faktycznie się stało]

**Evidence:**
[Link do evidence: metrics, incidents, customer feedback, etc.]

**Impact:**
- **Severity:** [Critical/High/Medium]
- **Stakeholders affected:** [Kto ucierpiał]
- **Quantification:** [Liczby jeśli możliwe: downtime, cost, customer churn, etc.]

---

### Problem 2: [Nazwa problemu]

[Analogicznie jak Problem 1]

---

### Problem 3: [Nazwa problemu, jeśli dotyczy]

[Analogicznie]

---

### Which assumptions were wrong?

**Original assumptions vs Reality:**

| Original assumption | Reality | Impact |
|---------------------|---------|--------|
| [Założenie 1] | [Co faktycznie było prawdą] | [Jak to wpłynęło na outcome] |
| [Założenie 2] | [...] | [...] |
| [Założenie 3] | [...] | [...] |

---

## SEC-DR-ROOT-CAUSE: Root cause analysis

> **Cel:** Deep dive do root causes - nie surface symptoms, ale underlying reasons.

**Primary root cause:**
[Główna root cause dlaczego decision failed]

---

### Why did PoC/Evaluation succeed but production fail?

**PoC limitations (missed):**
1. [Limitation 1, np. "Dataset too small (1M vs real 10M+)"]
2. [Limitation 2, np. "Query patterns simplified"]
3. [Limitation 3, np. "No operational testing"]

**What should have been tested differently:**
- [Test/validation 1 that was missing]
- [Test/validation 2 that was missing]

---

### Why did team underestimate complexity/risk?

**Contributing factors:**
1. [Factor 1, np. "Overconfidence from previous experience"]
2. [Factor 2, np. "Vendor marketing obscured operational complexity"]
3. [Factor 3, np. "Time pressure led to shortcuts"]

**Organizational/process issues:**
- [Issue 1]
- [Issue 2]

---

### Decision-making failures

**What went wrong in decision process:**

1. ❌ [Failure 1, np. "PoC validation criteria were insufficient"]
   - **Should have:** [Co powinniśmy byli zrobić]

2. ❌ [Failure 2, np. "Operational readiness assessment was skipped"]
   - **Should have:** [...]

3. ❌ [Failure 3, np. "No pilot phase"]
   - **Should have:** [...]

---

### Could this have been prevented?

**Red flags that were missed:**
- [Red flag 1 który ignored/dismissed]
- [Red flag 2]

**Early warning signs (in hindsight):**
- [Sign 1 that hinted at problems]
- [Sign 2]

**When should we have reversed:**
[Czy reversing earlier (before full implementation) would have reduced cost?]

---

## SEC-DR-IMPACT: Impact of original decision

> **Cel:** Quantify cost of wrong decision - pokazuje value lepszych decisions.

### Quantified costs

| Impact category | Cost | Details |
|-----------------|------|---------|
| Development time (original implementation) | [Hours/$] | [Breakdown] |
| Development time (firefighting/fixes) | [Hours/$] | [Breakdown] |
| Outages/downtime | [$] | [Revenue loss + details] |
| Support/escalations | [Hours/$] | [Team time handling issues] |
| Customer churn | [$] | [If applicable] |
| **Total direct cost** | **[$XXX]** | |
| **Opportunity cost** | **[$XXX]** | [What we couldn't do because busy with this] |

---

### Non-quantified impacts

**Team:**
- [Impact 1, np. "Morale (frustration from constant firefighting)"]
- [Impact 2, np. "Burnout risk"]
- [Impact 3, np. "Learning time diverted"]

**Business:**
- [Impact 1, np. "Customer trust (3 outages in 1 month)"]
- [Impact 2, np. "Competitive disadvantage"]
- [Impact 3, np. "Delayed other features"]

**Technical debt:**
- [Impact 1, np. "Rushed implementation created tech debt"]
- [Impact 2, np. "Workarounds accumulated"]

---

### Timeline of degradation

[Opcjonalne: timeline showing how sytuacja degraded over time]

| Date | Event | Impact |
|------|-------|--------|
| [YYYY-MM-DD] | [Original implementation] | [Initial state] |
| [YYYY-MM-DD] | [First issue] | [Impact] |
| [YYYY-MM-DD] | [Escalation] | [Impact] |
| [YYYY-MM-DD] | [Breaking point] | [Decision to reverse] |

---

## SEC-DR-NEW-DECISION: Nowa decyzja (reversal)

> **Cel:** Clear articulation nowej decyzji which reverses original.

**NEW DECISION:** [Stwierdzenie nowej decyzji]

[Np. "Migrate back to PostgreSQL + optimize query patterns" lub "Remove Feature X and refund customers"]

---

### New option selected

**What we're doing now:**
[Szczegółowy opis nowej opcji]

**Why this is better:**
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

**Is this one of the original alternatives?**
- [x] Yes - we're going back to [Original Option Y] which was rejected
- [ ] No - this is a new option not considered originally

---

### Rationale for reversal

**Key factors:**
- [Factor 1 making reversal right choice]
- [Factor 2]
- [Factor 3]

**Supporting evidence:**
- [Evidence 1, np. "PostgreSQL benchmark shows 80ms latency (acceptable vs 45ms original target)"]
- [Evidence 2]

---

### Trade-offs accepted

**What we're giving up by reversing:**
- ❌ [Trade-off 1, np. "Not hitting original 45ms latency target (now 80ms)"]
  - **Acceptable because:** [Why this is OK]
- ❌ [Trade-off 2, np. "Sunk cost $66K from original implementation"]
  - **Acceptable because:** [Why this is OK]

**What we're gaining:**
- ✅ [Gain 1]
- ✅ [Gain 2]
- ✅ [Gain 3]

---

### Why not continue with original decision?

[Wyjaśnienie dlaczego fixing original approach isn't viable]

**Considered but rejected:**
- [Fix attempt 1] - rejected because [reason]
- [Fix attempt 2] - rejected because [reason]

---

## SEC-DR-MIGRATION: Migration plan

> **Cel:** Detailed plan jak przejść from current (failed) state to new state.

**Migration owner:** [Who leads migration]
**Timeline:** [Duration, np. "4 weeks"]
**Risk level:** [High/Medium/Low]

---

### Migration phases

#### Phase 1: [Nazwa fazy, np. "Preparation"]
**Duration:** [Timeline]
**Goal:** [Co chcemy achieve w tej fazie]

**Tasks:**
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

#### Phase 2: [Nazwa fazy, np. "Dual-write / Data migration"]
**Duration:** [Timeline]
**Goal:** [...]

**Tasks:**
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

#### Phase 3: [Nazwa fazy, np. "Cutover"]
**Duration:** [Timeline]
**Goal:** [...]

**Tasks:**
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

#### Phase 4: [Nazwa fazy, np. "Cleanup / Decommission"]
**Duration:** [Timeline]
**Goal:** [...]

**Tasks:**
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

**Success criteria:**
- [Criterion 1]
- [Criterion 2]

---

### Rollback plan

**Purpose:** If migration itself fails, how do we rollback?

**Rollback strategy:**
[Opis jak rollback migration]

**Rollback window:**
[Jak długo możemy safely rollback, np. "2 weeks after cutover"]

**Rollback trigger conditions:**
- [Condition 1 triggering rollback]
- [Condition 2]

---

### Migration risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [Strategy] |
| [Risk 2] | [...] | [...] | [...] |

---

### Communication plan

**Internal stakeholders:**
| Stakeholder | What to communicate | When | Channel |
|-------------|-------------------|------|---------|
| [Team 1] | [Message] | [Timeline] | [Method] |
| [Team 2] | [...] | [...] | [...] |

**External stakeholders (if applicable):**
| Stakeholder | What to communicate | When | Channel |
|-------------|-------------------|------|---------|
| [Customers] | [Message] | [Timeline] | [Method] |
| [Partners] | [...] | [...] | [...] |

---

## SEC-DR-LESSONS: Lessons learned

> **Cel:** Capture actionable lessons - prevent repeating same mistakes.

### What went wrong (summary)

**Top 3 mistakes:**
1. [Mistake 1]
2. [Mistake 2]
3. [Mistake 3]

---

### Lessons learned

#### Lesson 1: [Lesson title]

**What we learned:**
[Specific lesson, not generic]

**Why it matters:**
[Impact of not following this lesson]

**Action item:**
[Specific change to process/template/practice]
- Responsibility: [Who owns]
- Due: [Date]

---

#### Lesson 2: [Lesson title]

[Analogicznie]

---

#### Lesson 3: [Lesson title]

[Analogicznie]

---

### What we'll do differently next time

**Process improvements:**
1. ✅ [Improvement 1, np. "Extended PoC (4-6 weeks vs 2 weeks)"]
2. ✅ [Improvement 2, np. "Scale testing mandatory (10x production dataset)"]
3. ✅ [Improvement 3, np. "Operational readiness assessment"]
4. ✅ [Improvement 4, np. "Pilot phase (20% → 50% → 100% rollout)"]
5. ✅ [Improvement 5, np. "Regular decision review (1 month post-implementation)"]

**Template/checklist updates:**
- [ ] [Update 1, np. "Add scale testing requirements to PoC template"]
- [ ] [Update 2, np. "Add operational readiness section to ADR template"]

**Training/knowledge gaps:**
- [ ] [Gap 1 to address]
- [ ] [Gap 2 to address]

---

### Cognitive biases / decision traps identified

[Które cognitive biases affected decision-making?]

- [Bias 1, np. "Sunk cost fallacy (delayed reversal by 1 month because 'we invested so much')"]
- [Bias 2, np. "Confirmation bias (ignored red flags)"]
- [Bias 3, np. "Overconfidence (underestimated complexity)"]

**How to avoid:**
[Strategies to counteract these biases in future]

---

### Knowledge sharing

**Documentation updates:**
- [ ] [Update 1, np. "Update ADR template (add reversal reference)"]
- [ ] [Update 2, np. "Add to Anti-Patterns catalog"]

**Communication:**
- [ ] Share at Engineering All-Hands (Date: [YYYY-MM-DD])
- [ ] Write internal postmortem (Owner: [Name])
- [ ] Write external blog post (if applicable) (Owner: [Name], Topic: [Title])

**Training:**
- [ ] [Training 1, np. "Workshop on PoC validation"]
- [ ] [Training 2]

---

### Success metrics for reversal

**How will we know the reversal was right decision?**

| Metric | Target | Actual (fill post-reversal) |
|--------|--------|---------------------------|
| [Metric 1] | [Target] | [TBD] |
| [Metric 2] | [Target] | [TBD] |
| [Metric 3] | [Target] | [TBD] |

**Review date:** [YYYY-MM-DD, np. 3 months after reversal]

---

## Appendix: Supporting documentation

### Original decision artifacts
- [Link to original ADR/DECISION-LOG]
- [Link to original PoC]
- [Link to original requirements]

### Evidence of failure
- [Link to incident reports]
- [Link to metrics/dashboards showing degradation]
- [Link to customer feedback/complaints]

### New decision artifacts
- [Link to new ADR]
- [Link to migration plan]
- [Link to new benchmarks/PoC]

---

**Szacowany czas wypełnienia:** 3-5 godzin (comprehensive retrospective)

**Wartość dodana:**
- ✅ Honest retrospective (dlaczego decyzja was wrong)
- ✅ Root cause analysis (nie surface-level)
- ✅ Quantified impact (pokazuje cost of bad decisions)
- ✅ Actionable lessons (not generic "test more")
- ✅ Knowledge sharing (prevents repeating mistakes)
- ✅ Psychological safety (it's OK to reverse decisions when data shows they're wrong)

**Kiedy używać:**
- Architecture decision nie sprawdziła się (np. MongoDB → PostgreSQL)
- Vendor selection was wrong (np. migrate off Vendor X)
- Feature removal (deprecate feature after launch)
- Pivot (change direction after trying approach)
- Any significant decision that needs to be reversed

**Kiedy NIE używać:**
- Minor tactical decisions → just make new DECISION-LOG
- Normal evolution of decision → update original ADR
- Decision succeeded but circumstances changed → new ADR (not reversal)
