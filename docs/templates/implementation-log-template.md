---
id: IMPL-LOG-{{PARENT_DOC_ID}}
title: "Implementation Log - {{PARENT_DOC_TITLE}}"
type: implementation-log
parent: {{PARENT_DOC_ID}}  # np. ADR-005
status: in-progress  # in-progress → completed
created: "{{START_DATE}}"
implementation_period:
  start: "{{START_DATE}}"
  end: "{{END_DATE}}"  # null jeśli in-progress
team: ["{{TEAM_MEMBER_1}}", "{{TEAM_MEMBER_2}}"]
---

# Implementation Log: {{PARENT_DOC_TITLE}}

**⚠️ UWAGA**: To jest szablon. Dodawaj wpisy chronologicznie podczas implementacji. Każde unexpected discovery, plan deviation, edge case = nowy wpis.

---

## Entry 1: {{DATE}} - Rozpoczęcie Implementacji

**Type**: `start`
**Action**: {{WHAT_WAS_STARTED}}
**Status**: {{success|partial|blocked}}
**Duration**: {{DURATION}} (np. "15 min", "2 hours")
**Notes**: {{ADDITIONAL_CONTEXT}}

---

## Entry 2: {{DATE}} - {{EVENT_TITLE}}

**Type**: `{{TYPE}}`  # unexpected_discovery | plan_deviation | edge_case | performance_surprise | blocker | completion
**Severity**: `{{SEVERITY}}`  # low | medium | high | critical
**Title**: "{{SHORT_DESCRIPTION}}"

### Problem/Discovery
{{WHAT_HAPPENED}}

### Impact
{{HOW_THIS_AFFECTS_PROJECT}}

### Root Cause (jeśli applicable)
{{WHY_THIS_HAPPENED}}

### Solution
{{WHAT_WAS_DONE}}

### Trade-off Accepted (jeśli applicable)
{{WHAT_WE_ACCEPT_AS_CONSEQUENCE}}
**Mitigation**: {{HOW_WE_MITIGATE_RISK}}

### Decision Maker
{{WHO_APPROVED}} (jeśli zmiana wymaga approval)

### Evidence
- [{{EVIDENCE_ID}}] {{DESCRIPTION}}

### Documents Updated (jeśli applicable)
- {{DOCUMENT_ID}}: {{WHAT_WAS_CHANGED}}

---

## Entry 3: {{DATE}} - {{EVENT_TITLE}}

**Type**: `plan_deviation`
**Severity**: `high`
**Title**: "{{TITLE}}"

### Original Plan
{{WHAT_WAS_PLANNED}}

### Change
{{WHAT_CHANGED}}

### Reason
{{WHY_CHANGED}}

### Impact
- **Cost**: {{COST_IMPACT}} (np. "+$800/month")
- **Timeline**: {{TIMELINE_IMPACT}} (np. "+1 day delay")
- **Scope**: {{SCOPE_IMPACT}}

### Approval
- **Required from**: {{ROLE}} (np. "CFO" jeśli budget impact)
- **Approval received**: {{YES_NO}}
- **Evidence**: [{{EVIDENCE_ID}}] (np. CFO email)

### Documents Updated
- {{DOC_1}}: {{CHANGE_1}}
- {{DOC_2}}: {{CHANGE_2}}

---

## Entry 4: {{DATE}} - {{EVENT_TITLE}}

**Type**: `edge_case`
**Severity**: `low`
**Title**: "{{TITLE}}"

### Case Discovered
{{DESCRIBE_EDGE_CASE}}

### Cause
{{WHY_THIS_WASNT_CAUGHT_EARLIER}}

### Solution
{{HOW_FIXED}}

### Performance Impact (jeśli applicable)
- **Before**: {{METRIC_BEFORE}}
- **After**: {{METRIC_AFTER}}
- **Improvement**: {{PERCENTAGE}}

### Learning
{{WHAT_TO_DO_DIFFERENTLY_NEXT_TIME}}

### Evidence
- [{{EVIDENCE_ID}}] {{DESCRIPTION}}

---

## Entry N: {{DATE}} - Ukończenie Implementacji

**Type**: `completion`
**Status**: ✅ Deployed to production | ⚠️ Deployed with known issues | ❌ Blocked

### Summary
{{BRIEF_SUMMARY_OF_IMPLEMENTATION}}

### Deployment Method
{{HOW_DEPLOYED}} (np. "Blue-green deployment", "Rolling update", "Canary release")

### Downtime
{{DOWNTIME_DURATION}} (np. "0 min", "5 min planned")

### DoD Status
- [{{x| }}] All acceptance criteria met
- [{{x| }}] Implementation log complete
- [{{x| }}] Metrics before/after measured
- [{{x| }}] Tests passed
- [{{x| }}] Documentation updated
- [{{x| }}] Stakeholder sign-off

### Next Steps
- [ ] Monitor metrics for {{DURATION}} (np. "7 days")
- [ ] Schedule post-mortem ({{DATE}})
- [ ] Update runbooks

---

## Template: Dodaj Nowy Wpis (kopiuj i dostosuj)

```markdown
## Entry X: {{DATE}} - {{TITLE}}

**Type**: `{{TYPE}}`
**Severity**: `{{SEVERITY}}`

### Problem
{{DESCRIPTION}}

### Solution
{{RESOLUTION}}

### Evidence
- [{{EVIDENCE_ID}}]
```

---

## Typy Wpisów (Reference)

| Type | Kiedy używać | Severity |
|------|--------------|----------|
| `start` | Rozpoczęcie pracy | info |
| `unexpected_discovery` | Coś nieoczekiwanego (connection pool limit) | low-critical |
| `plan_deviation` | Odchylenie od planu (Multi-AZ added) | medium-critical |
| `edge_case` | Edge case discovered | low-medium |
| `performance_surprise` | Nieoczekiwana wydajność (szybsza/wolniejsza) | info-medium |
| `blocker` | Bloker wymagający decyzji | high-critical |
| `completion` | Ukończenie zadania | info |

---

**© {{YEAR}} {{COMPANY}}. Document version {{VERSION}}. Last updated: {{DATE}}.**

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Parent ADR]** `adr-template-proof-system.md`
  - Type: `requires` | Reason: Implementation log documents execution of ADR decision | Parent ID in front-matter: `parent: {{PARENT_ADR_ID}}`

### Impacts (Downstream Documents)
- **[Parent ADR]** - Implementation discoveries may trigger ADR amendment
  - Type: `informs` | Example: Unexpected performance issue → re-evaluate ADR decision
- **[Post-Mortem]** `post-mortem-template.md`
  - Type: `feeds` | Reason: Implementation log entries inform post-mortem analysis
- **[TDD]** or **[PRD]** (if implementation deviates from plan)
  - Type: `updates` | Reason: Plan deviations require parent doc updates

### Related Documents
- **[ADR Template]** `adr-template-proof-system.md` - Parent template
- **[Post-Mortem Template]** `post-mortem-template.md` - Downstream analysis

### Satellite Documents
- **[Changelog]** - Track edits to implementation log itself

### Entry Types
```yaml
entry_types:
  - start: Begin implementation
  - unexpected_discovery: Something not anticipated in ADR
  - plan_deviation: Change from original ADR plan
  - edge_case: Unexpected input/scenario
  - performance_surprise: Better/worse than expected
  - blocker: Issue requiring escalation/decision
  - completion: Implementation finished
```

### Validation Rules
- [ ] Parent ADR ID valid and exists
- [ ] All plan_deviation entries have approval if budget/timeline impact
- [ ] All blocker entries resolved before completion
- [ ] Completion entry has DoD checklist
