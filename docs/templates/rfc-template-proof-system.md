---
id: RFC-{{NUMBER}}  # np. RFC-2024-12
title: "{{RFC_TITLE}}"
type: rfc
status: draft  # draft → review → accepted | rejected | deferred
created: "{{DATE}}"
updated: "{{DATE}}"
author: ["{{AUTHOR_1}}", "{{AUTHOR_2}}"]
reviewers: ["{{REVIEWER_1}}", "{{REVIEWER_2}}"]  # Wymagani reviewers
approvers: ["{{APPROVER_1}}"]  # Final decision makers
deadline: "{{DATE}}"  # Deadline dla feedback (opcjonalnie)

# Bramki wejścia (co wpływa na ten RFC)
dependencies:
  - id: "{{DEPENDENCY_ID}}"
    title: "{{DEPENDENCY_TITLE}}"
    type: requires | informs
    status_constraint: [approved, completed]
    reason: "{{WHY}}"

# Bramki wyjścia (na co wpływa ten RFC)
impacts:
  - id: "{{TARGET_ID}}"
    title: "{{TARGET_TITLE}}"
    type: blocks | informs
    until: "{{THIS_RFC_ID}}.status == accepted"
    cascade: true

# Context snapshot (może się zmienić during review)
context_snapshot:
  budget: "{{BUDGET}}"  # Może być "TBD" jeśli nieznane
  timeline: "{{TIMELINE}}"
  team_capacity: "{{CAPACITY}}"
  constraints: ["{{CONSTRAINT_1}}", "{{CONSTRAINT_2}}"]

# Evidence (wstępne, może rosnąć during review)
evidence_ids: ["{{E-XXX}}", "{{E-YYY}}"]

# Alternatives (preferowana + inne)
alternatives:
  - id: "OPTION-A"
    title: "{{OPTION_A_TITLE}}"
    status: preferred  # preferred | alternative | rejected
    reason: "{{WHY_PREFERRED}}"

  - id: "OPTION-B"
    title: "{{OPTION_B_TITLE}}"
    status: alternative

  # Minimum 2 opcje

# Feedback tracking
feedback_received:
  - date: "{{DATE}}"
    from: "{{REVIEWER}}"
    summary: "{{SUMMARY}}"
    action: "{{WHAT_CHANGED}}"  # np. "Updated alternative B based on feedback"

# Open questions
open_questions:
  - id: "Q1"
    question: "{{QUESTION}}"
    status: pending | answered
    answer: "{{ANSWER}}"  # Jeśli answered
    decision_maker: "{{ROLE}}"  # Kto ma odpowiedzieć

---

# RFC-{{NUMBER}}: {{RFC_TITLE}}

**⚠️ UWAGA**: To jest RFC (Request for Comments), nie ADR (Architecture Decision Record). RFC = propozycja do dyskusji. Może być zaakceptowana, odrzucona lub odroczona.

**Status**: {{STATUS}}
**Deadline dla feedback**: {{DATE}}
**Reviewers**: {{REVIEWER_LIST}}

---

## Executive Summary

**Problem**: {{1-2_SENTENCES_PROBLEM_STATEMENT}}

**Proposed Solution**: {{1-2_SENTENCES_SOLUTION}}

**Expected Benefit**: {{KEY_BENEFIT}}

**Cost/Effort**: {{ESTIMATE}} (np. "2 weeks, 1 dev", "$5k budget")

**Decision Required By**: {{DATE}} (jeśli time-sensitive)

---

## Background & Context

### Problem Statement

**Current State**:
{{DESCRIBE_CURRENT_SITUATION}}

**Pain Points**:
1. {{PAIN_1}}: {{DESCRIPTION}} (impact: {{IMPACT}})
2. {{PAIN_2}}: {{DESCRIPTION}}
3. {{PAIN_3}}: {{DESCRIPTION}}

**Evidence of Problem**:
- [{{E-ID}}] {{EVIDENCE_DESCRIPTION}}
- [{{E-ID}}] {{EVIDENCE_DESCRIPTION}}

### Why Now?

**Trigger**: {{WHAT_TRIGGERED_THIS_RFC}} (np. "Incident X", "Customer request", "Technical debt reaching critical")

**Urgency**: {{HIGH|MEDIUM|LOW}}
**Consequence of delay**: {{WHAT_HAPPENS_IF_WE_DONT_DO_THIS}}

---

## Proposal

### Preferred Solution (Option A)

**⚠️ STORYTELLING**: Opisz jako narrację, nie lista faktów.

**High-level approach**:
{{1-2_PARAGRAPHS_DESCRIBING_SOLUTION}}

**Key Components**:
1. **{{COMPONENT_1}}**: {{DESCRIPTION}}
   - Implementation: {{HOW}}
   - Estimated effort: {{EFFORT}}

2. **{{COMPONENT_2}}**: {{DESCRIPTION}}

3. **{{COMPONENT_3}}**: {{DESCRIPTION}}

**Architecture Diagram** (jeśli applicable):
```mermaid
{{MERMAID_DIAGRAM}}
```

**Pros**:
- {{PRO_1}}: {{DESCRIPTION}}
- {{PRO_2}}: {{DESCRIPTION}}

**Cons**:
- {{CON_1}}: {{DESCRIPTION}}
  - Mitigation: {{MITIGATION}}

**Evidence**:
- [{{E-ID}}] {{BENCHMARK|PROTOTYPE|ANALYSIS}}

---

### Alternative Solutions

#### Option B: {{ALTERNATIVE_TITLE}}

**Approach**: {{DESCRIPTION}}

**Pros**:
- {{PRO_1}}

**Cons**:
- {{CON_1}} (dlaczego nie preferowana)

**Why not preferred**: {{RATIONALE}}

**Evidence**: [{{E-ID}}]

---

#### Option C: {{ALTERNATIVE_TITLE}} (jeśli applicable)

**Approach**: {{DESCRIPTION}}

**Why not preferred**: {{RATIONALE}}

---

### Do Nothing (Always consider!)

**Cons**:
- {{PROBLEM_1}} remains unsolved
- {{PROBLEM_2}} worsens over time

**Opportunity cost**: {{WHAT_WE_MISS_BY_NOT_DOING_THIS}}

---

## Impact Analysis

### Technical Impact

**Systems Affected**:
- {{SYSTEM_1}}: {{IMPACT}} (np. "Requires schema migration")
- {{SYSTEM_2}}: {{IMPACT}}

**Compatibility**:
- Backward compatible: {{YES|NO|PARTIAL}}
- Breaking changes: {{LIST_OF_BREAKING_CHANGES}}
- Migration path: {{DESCRIPTION}}

**Dependencies**:
- Requires: {{TECH_DEPENDENCY_1}}, {{TECH_DEPENDENCY_2}}
- Blocks: {{WHAT_IS_BLOCKED_BY_THIS}}

### Business Impact

**Users Affected**: {{COUNT}} ({{PERCENTAGE}}% of total)

**Benefits**:
- {{BENEFIT_1}}: {{QUANTIFIED}} (np. "Reduce latency by 50%")
- {{BENEFIT_2}}: {{QUANTIFIED}}

**Risks**:
- {{RISK_1}}: {{PROBABILITY}} probability, {{IMPACT}} impact
  - Mitigation: {{MITIGATION}}

**ROI**: {{CALCULATION}} (jeśli applicable)

### Team Impact

**Effort Estimate**:
- Design: {{EFFORT}} (np. "1 week")
- Implementation: {{EFFORT}}
- Testing: {{EFFORT}}
- Documentation: {{EFFORT}}
- **Total**: {{TOTAL_EFFORT}}

**Team Required**: {{TEAM_SIZE}} {{ROLE}} for {{DURATION}}

**Skills Required**:
- {{SKILL_1}} (current team proficiency: {{LEVEL}})
- {{SKILL_2}}

**Training Needed**: {{YES|NO}} - {{DESCRIPTION}}

---

## Implementation Plan (High-Level)

**⚠️ NOTE**: Detailed implementation plan będzie w ADR jeśli RFC accepted.

### Phase 1: Design ({{DURATION}})
- [ ] {{TASK_1}}
- [ ] {{TASK_2}}
- [ ] Gate: Design review complete

### Phase 2: Implementation ({{DURATION}})
- [ ] {{TASK_1}}
- [ ] {{TASK_2}}
- [ ] Gate: DoD criteria met

### Phase 3: Rollout ({{DURATION}})
- [ ] {{TASK_1}}
- [ ] Gate: Production deployment

**Total Timeline**: {{TOTAL_DURATION}} (best case: {{BEST}}, worst case: {{WORST}})

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| {{RISK_1}} | {{HIGH|MED|LOW}} | {{HIGH|MED|LOW}} | {{MITIGATION}} | {{OWNER}} |
| {{RISK_2}} | {{PROB}} | {{IMPACT}} | {{MITIGATION}} | {{OWNER}} |

**Showstoppers** (risks that would kill the project):
- {{SHOWSTOPPER_1}}: {{DESCRIPTION}}
  - Likelihood: {{PERCENTAGE}}%
  - Mitigation: {{MITIGATION}}

---

## Open Questions

**⚠️ MUST RESOLVE**: These questions must be answered before acceptance.

### Q1: {{QUESTION}}
**Status**: {{Pending|Answered}}
**Decision Maker**: {{ROLE}} (np. "CFO" jeśli budget question)
**Blocking**: {{YES|NO}} (does this block acceptance?)
**Answer** (jeśli answered): {{ANSWER}}
**Date resolved**: {{DATE}}

### Q2: {{QUESTION}}
**Status**: {{STATUS}}
**Decision Maker**: {{ROLE}}

---

## Feedback Received

**⚠️ TRACKABLE**: All feedback = logged + action taken documented.

### Feedback from {{REVIEWER}} ({{DATE}})

**Summary**: {{FEEDBACK_SUMMARY}}

**Specific Comments**:
1. **Comment**: {{COMMENT_1}}
   - **Response**: {{RESPONSE}}
   - **Action taken**: {{ACTION}} (np. "Updated alternative B", "Added section X")
   - **Status**: ✅ Addressed | ⚠️ Partially addressed | 📋 Deferred

2. **Comment**: {{COMMENT_2}}
   - **Response**: {{RESPONSE}}
   - **Action**: {{ACTION}}

---

### Feedback from {{REVIEWER_2}} ({{DATE}})

[Same structure]

---

## Decision Criteria

**RFC will be ACCEPTED if**:
- [ ] ≥{{PERCENTAGE}}% reviewers approve (np. "≥80%")
- [ ] All showstopper risks mitigated
- [ ] All blocking open questions answered
- [ ] Budget approved (jeśli applicable)
- [ ] Timeline acceptable to stakeholders

**RFC will be REJECTED if**:
- [ ] {{REJECTION_CRITERION_1}}
- [ ] {{REJECTION_CRITERION_2}}

**RFC will be DEFERRED if**:
- [ ] {{DEFERRAL_CRITERION}} (np. "Higher priority work", "Waiting for technology maturity")

---

## Success Metrics (Post-Implementation)

**⚠️ MEASURABLE**: Define how we'll know if this was successful.

| Metric | Current | Target | Measurement Method |
|--------|---------|--------|--------------------|
| {{METRIC_1}} | {{CURRENT}} | {{TARGET}} | {{HOW_MEASURED}} |
| {{METRIC_2}} | {{CURRENT}} | {{TARGET}} | {{HOW_MEASURED}} |

**Review Date**: {{DATE}} (np. "90 days after deployment")

---

## Next Steps (If Accepted)

1. **Create ADR**: Formal architecture decision record z pełnym design
2. **Update roadmap**: Add to sprint planning
3. **Allocate resources**: Assign team, reserve budget
4. **Create implementation tickets**: Break down into tasks
5. **Schedule reviews**: Design review, security review (jeśli applicable)

---

## Appendix

### Related RFCs

- **[RFC-XXX]** "{{TITLE}}" - {{RELATIONSHIP}} (np. "Depends on", "Supersedes", "Related to")

### Evidence Notes Summary

| ID | Type | Title | Date |
|----|------|-------|------|
| [{{E-ID}}] | {{TYPE}} | {{TITLE}} | {{DATE}} |

### Glossary

- **{{TERM_1}}**: {{DEFINITION}}
- **{{TERM_2}}**: {{DEFINITION}}

---

## Status History

| Date | Status | Reason | Updated By |
|------|--------|--------|------------|
| {{DATE}} | draft | Initial proposal | {{AUTHOR}} |
| {{DATE}} | review | Sent for feedback | {{AUTHOR}} |
| {{DATE}} | {{STATUS}} | {{REASON}} | {{DECISION_MAKER}} |

---

**© {{YEAR}} {{COMPANY}}. RFC version {{VERSION}}. Created: {{CREATED_DATE}}. Last updated: {{UPDATED_DATE}}.**

---

## Document Cross-References

### Dependencies (Required Inputs)
- **CONTEXT-DEPENDENT** - varies per RFC instance
  - Typical dependencies: Problem statement (from PRD/TDD), Evidence notes (research, benchmarks), Previous RFCs (related proposals)

### Impacts (Downstream Documents)
- **[ADR]** `adr-template-proof-system.md`
  - Type: `generates` | Reason: Accepted RFC generates ADR documenting decision | Cascade: `true`
- **[TDD]** or **[PRD]** (if proposal affects design)
  - Type: `informs` or `blocks` | Reason: RFC findings update design documents
- **[Spike]** (if RFC requires prototyping)
  - Type: `generates` | Reason: RFC may spawn spike to explore feasibility | Cascade: `false`

### Related Documents
- **[ADR Template]** `adr-template-proof-system.md` - Relationship: `follows` | Reason: ADR documents decision after RFC discussion
- **[Evidence Note Template]** `evidence-note-template.md` - Relationship: `uses` | Reason: RFC cites evidence notes as supporting data

### Satellite Documents
- **[TODO]** - Generated when RFC status → `draft`
- **[DOR]** - Criteria: Problem defined, Stakeholders identified, Discussion period set
- **[DOD]** - Criteria: Feedback collected, Decision made (accept/reject/defer), ADR created (if accepted)

### Conditional Cross-References
```yaml
when technical_proposal === true:
  require_dependencies: [Technical feasibility evidence, Proof of concept results]
  require_approvals: [Tech Lead, Architecture Review Board]

when process_change === true:
  require_dependencies: [Current process documentation, Impact assessment]
  require_approvals: [Process Owner, Affected Team Leads]

when breaking_change === true:
  require_dependencies: [Migration plan, Backward compatibility analysis]
  require_approvals: [Engineering Manager, Product Owner]
```

### Validation Rules
- [ ] Problem statement clear and specific
- [ ] ≥1 alternative considered
- [ ] Stakeholders identified
- [ ] Discussion period completed (minimum 5 business days for major RFCs)
- [ ] Feedback incorporated or explicitly rejected with rationale
- [ ] Decision documented (accept/reject/defer)
- [ ] If accepted, ADR created
