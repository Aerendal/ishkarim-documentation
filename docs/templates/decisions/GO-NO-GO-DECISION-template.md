# GO-NO-GO-DECISION: Go/No-Go Decision Template

---
**Meta (WYMAGANE):**
```yaml
id: GO-NO-GO-[NNN]
doctype: GO-NO-GO-DECISION
status: [pending/approved/rejected/conditional]
version: "1.0"
owner: "[Decision Owner/Release Manager]"
project: "[Project/Sprint/Release Name]"
decision_deadline: "YYYY-MM-DD HH:MM"
decision_type: "[sprint_release/mvp_launch/feature_rollout/market_entry/procurement/other]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [RELEASE-CHECKLIST]
    type: requires
    reason: "Release checklist informs go/no-go criteria"
  - id: [TESTING-RESULTS]
    type: requires
    reason: "Test results determine readiness"

impacts:
  - id: [DEPLOYMENT-GUIDE]
    type: blocks
    reason: "GO decision triggers deployment"
  - id: [POSTMORTEM]
    type: influences
    reason: "NO-GO decision may trigger postmortem (why not ready)"
```

**Wymagane dokumenty satelitarne:**
- APPROVAL-[NNN]: Formal approval from decision makers (especially for high-risk GO decisions)

---

## SEC-GNG-DECISION: Decision statement

> **Cel:** Crystal clear statement czego dotyczy ta go/no-go decision.

**Decision question:**
[Jednoznaczne pytanie, np. "Should we release Sprint 15 to production on 2025-12-30?"]

**Scope of decision:**
- **What:** [Co dokładnie jest przedmiotem decyzji]
- **When:** [Planowana data/time dla GO]
- **Who affected:** [Kto jest impacted - users, customers, team]
- **Reversibility:** [Czy decision jest reversible? Jak szybko?]

**Context:**
[1-2 akapity kontekstu - dlaczego teraz, co się dzieje, dlaczego ta decision jest critical]

---

## SEC-GNG-CRITERIA: Go/No-Go criteria (checklist)

> **Cel:** Objective criteria które muszą być spełnione dla GO decision.

### MUST-HAVE criteria (blockers if not met)

**Purpose:** These are non-negotiable - jeśli którykolwiek nie jest spełniony → NO-GO

- [ ] **[Criterion 1]** - [Opis kryterium, jak zmierzyć]
  - Current status: [✅ Met / ❌ Not met / ⚠️ Partially met]
  - Evidence: [Link do evidence/results]

- [ ] **[Criterion 2]** - [Opis]
  - Current status: [...]
  - Evidence: [...]

- [ ] **[Criterion 3]** - [Opis]
  - Current status: [...]
  - Evidence: [...]

**Total MUST-HAVE:** [X/Y met] ([Z%])

---

### SHOULD-HAVE criteria (warnings if not met)

**Purpose:** Important but not blockers - może GO with mitigation

- [ ] **[Criterion 1]** - [Opis kryterium]
  - Current status: [✅ Met / ⚠️ Not met]
  - Impact if not met: [Consequence]
  - Mitigation: [If not met, jak zmitigować risk]

- [ ] **[Criterion 2]** - [Opis]
  - Current status: [...]
  - Impact if not met: [...]
  - Mitigation: [...]

**Total SHOULD-HAVE:** [X/Y met] ([Z%])

---

### NICE-TO-HAVE criteria (desired but optional)

**Purpose:** Desired features/qualities - nie wpływają na GO/NO-GO decision

- [ ] **[Criterion 1]** - [Opis kryterium]
  - Current status: [✅ Met / ❌ Not met]

- [ ] **[Criterion 2]** - [Opis]
  - Current status: [...]

**Total NICE-TO-HAVE:** [X/Y met] ([Z%])

---

## SEC-GNG-STATUS: Current status (vs criteria)

> **Cel:** Snapshot aktualnego stanu relative to criteria.

**Overall readiness:** [X% of MUST-HAVE + Y% of SHOULD-HAVE]

**Summary:**
- ✅ **MUST-HAVE:** [X/Y criteria met] ([Z%])
- ⚠️ **SHOULD-HAVE:** [X/Y criteria met] ([Z%])
- 📊 **NICE-TO-HAVE:** [X/Y criteria met] ([Z%])

### Blockers (MUST-HAVE not met)

#### Blocker 1: [Nazwa blockera]
- **Criterion:** [Które MUST-HAVE kryterium]
- **Current state:** [Aktualny stan]
- **Gap:** [Co brakuje do spełnienia]
- **Mitigation plan:** [Jak resolve przed deadline]
- **Owner:** [Kto responsible]
- **ETA:** [Kiedy będzie resolved]

#### Blocker 2: [Nazwa blockera, jeśli dotyczy]
[Analogicznie]

---

### Warnings (SHOULD-HAVE not met)

#### Warning 1: [Nazwa warning]
- **Criterion:** [Które SHOULD-HAVE kryterium]
- **Current state:** [Aktualny stan]
- **Impact if proceed:** [Consequence of GO without this]
- **Mitigation plan:** [Jak reduce risk]
- **Accept risk?** [Yes/No + uzasadnienie]

#### Warning 2: [Nazwa warning, jeśli dotyczy]
[Analogicznie]

---

## SEC-GNG-RISKS: Known risks if GO

> **Cel:** Explicit list of risks jeśli decyzja będzie GO.

| Risk | Probability | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [Mitigation strategy] | [Who owns] |
| [Risk 2] | [...] | [...] | [...] | [...] |
| [Risk 3] | [...] | [...] | [...] | [...] |

### High-priority risks (High probability OR High impact)

#### Risk: [Nazwa high-priority risk]
- **Scenario:** [Co może pójść źle]
- **Probability:** [High/Medium + uzasadnienie]
- **Impact:** [High/Medium + quantify if possible]
- **Detection:** [Jak wykryjemy jeśli się zmaterializuje]
- **Mitigation:** [Co robimy PRZED GO żeby reduce risk]
- **Response plan:** [Co robimy JEŚLI risk się zmaterializuje after GO]

[Repeat dla innych high-priority risks]

---

## SEC-GNG-IMPACT: Impact if NO-GO

> **Cel:** Explicit list of consequences jeśli decyzja będzie NO-GO.

**Purpose:** Balance risks of GO vs costs of NO-GO

| Impact category | Severity | Stakeholders affected | Quantification (if possible) |
|----------------|----------|----------------------|----------------------------|
| [Revenue loss] | [High/Med/Low] | [Finance, Sales] | [$X/week delayed] |
| [Customer disappointment] | [...] | [...] | [Y customers waiting] |
| [Team morale] | [...] | [...] | [Sprint goal not met] |
| [Opportunity cost] | [...] | [...] | [Delayed next sprint] |
| [Competitive disadvantage] | [...] | [...] | [Competitor launches first] |
| [Other] | [...] | [...] | [...] |

### Critical impacts (High severity)

#### Impact: [Nazwa critical impact]
- **Scenario:** [Co się stanie jeśli NO-GO]
- **Severity:** [High + dlaczego]
- **Who affected:** [Stakeholders]
- **Quantification:** [Liczby jeśli możliwe]
- **Alternative:** [Czy jest sposób żeby zmniejszyć ten impact nawet przy NO-GO?]

[Repeat dla innych critical impacts]

---

## SEC-GNG-RECOMMENDATION: Recommendation (GO/NO-GO/CONDITIONAL-GO)

> **Cel:** Clear recommendation z uzasadnieniem.

**Recommendation:** [**GO** / **NO-GO** / **CONDITIONAL-GO**]

**Recommended by:** [Imię/Rola osoby rekomendującej]
**Date:** [YYYY-MM-DD]

---

### Rationale

**Why this recommendation:**

1. [Powód 1 - odniesienie do criteria/risks/impacts]
2. [Powód 2]
3. [Powód 3]

**Key factors:**
- [Czynnik decydujący 1]
- [Czynnik decydujący 2]

**Trade-offs accepted:**
[Jeśli GO: jakie risks akceptujemy; Jeśli NO-GO: jakie impacts akceptujemy]

---

### If GO: Conditions and monitoring

**Pre-conditions (must be met before GO):**
1. [ ] [Condition 1]
2. [ ] [Condition 2]
3. [ ] [...]

**Post-GO monitoring:**
- **Metrics to watch:** [Które metryki monitorujemy after GO]
- **Alert thresholds:** [Kiedy trigger alarms]
- **Rollback triggers:** [W jakich warunkach rollback decision]

**Rollback plan:**
- **Time to rollback:** [Jak szybko możemy rollback]
- **Rollback owner:** [Kto ma authority do trigger rollback]
- **Communication plan:** [Jak komunikujemy rollback jeśli potrzebny]

---

### If CONDITIONAL-GO: Conditions

**GO only if:**
1. ✅ [Condition 1 - deadline: YYYY-MM-DD HH:MM]
   - Status: [Pending/Met]
   - Owner: [Who responsible]

2. ✅ [Condition 2 - deadline: ...]
   - Status: [...]
   - Owner: [...]

**Fallback plan if conditions not met:**
- **Option A:** [Partial GO, np. "Release to 20% users (canary)"]
- **Option B:** [NO-GO + new date, np. "Delay to YYYY-MM-DD"]

**Decision checkpoint:** [YYYY-MM-DD HH:MM] - final GO/NO-GO based on conditions

---

### If NO-GO: Next steps

**Reason for NO-GO:**
[Główny powód dlaczego NO-GO]

**What needs to happen for GO:**
1. [Action 1 - owner - ETA]
2. [Action 2 - owner - ETA]
3. [...]

**Next decision checkpoint:**
- **Date:** [YYYY-MM-DD]
- **Criteria for next review:** [Co musi być ready]

**Stakeholder communication:**
- [ ] [Who needs to be informed]
- [ ] [Communication channel/method]
- [ ] [Key message]

---

## SEC-GNG-DECISION-FINAL: Final decision + approver

> **Cel:** Record of actual decision made and who approved.

**FINAL DECISION:** [**GO ✅** / **NO-GO ❌** / **CONDITIONAL-GO ⚠️**]

**Decision made by:** [Imię/Rola - decision authority]
**Decision date:** [YYYY-MM-DD HH:MM]

**Approvers:**
| Name | Role | Approval | Comments |
|------|------|----------|----------|
| [Name 1] | [Role] | ✅ Approved / ❌ Rejected / ⚠️ Conditional | [Komentarze jeśli były] |
| [Name 2] | [Role] | [...] | [...] |

---

### If GO was approved

**Deployment scheduled:** [YYYY-MM-DD HH:MM]

**Conditions met (if CONDITIONAL-GO):**
- [x] [Condition 1] - Met on [date]
- [x] [Condition 2] - Met on [date]

**Go-live checklist:**
- [ ] [Action 1]
- [ ] [Action 2]
- [ ] [Communication sent to stakeholders]

**Monitoring plan:**
- **Who monitors:** [Team/person]
- **Duration:** [Jak długo intensive monitoring, np. "First 48h"]
- **Escalation path:** [Kto eskalować jeśli issues]

---

### If NO-GO was decided

**Primary reason:** [Main blocker/concern]

**Revised timeline:** [Nowa data for next GO/NO-GO decision]

**Remediation plan:**
| Action | Owner | Due date | Status |
|--------|-------|----------|--------|
| [Action 1] | [Owner] | [Date] | [Pending/In progress/Done] |
| [Action 2] | [...] | [...] | [...] |

**Stakeholder communication:**
- [x] [Stakeholder group 1] - Informed on [date]
- [x] [Stakeholder group 2] - Informed on [date]

---

## Post-decision review (fill after GO)

**Review date:** [YYYY-MM-DD, np. 1 week after GO]

### Did decision work out?

**Outcome:** [Success / Partial success / Issues encountered]

**Metrics:**
- [Metric 1]: [Target] → [Actual]
- [Metric 2]: [Target] → [Actual]

### Risks that materialized
- [Risk X]: [Did it happen? Impact? How handled?]

### Surprises (risks not anticipated)
- [Surprise 1]
- [Surprise 2]

### Lessons learned
1. [Lesson 1]
2. [Lesson 2]

### Improvements for next GO/NO-GO
- [Improvement 1, np. "Add criterion X to checklist"]
- [Improvement 2]

---

**Szacowany czas wypełnienia:** 1-2 godziny

**Wartość dodana:**
- ✅ Crisp binary decision (GO/NO-GO/CONDITIONAL)
- ✅ Clear criteria (checklist format – easy to evaluate)
- ✅ Risk/impact balanced (not just "do we pass criteria")
- ✅ Conditional GO (flexible vs rigid binary)
- ✅ Documented accountability (who approved, when)

**Różnica vs Feasibility Study:**
- **Feasibility Study** = high-level, project initiation (months ahead), exploratory
- **Go/No-Go Decision** = tactical, immediate decision (days/weeks ahead), execute-focused

**Kiedy używać:**
- Sprint/release go/no-go (ship now vs delay)
- Feature flag enablement (enable for 100% users vs rollback)
- Market launch (launch in country X vs delay)
- Procurement approval (sign vendor contract vs renegotiate)
- MVP launch decision
- Major deployment decision

**Kiedy NIE używać:**
- Project initiation decision → użyj FEASIBILITY-STUDY
- Feature prioritization → użyj DECISION-LOG
- Architecture decision → użyj ADR
- Vendor selection → użyj OPTION-COMPARISON-MATRIX lub TRADE-OFF-ANALYSIS
