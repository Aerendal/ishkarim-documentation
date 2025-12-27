---
id: POST-MORTEM-{{PARENT_DOC_ID}}
title: "Post-mortem - {{PROJECT_TITLE}}"
type: post-mortem
parent: {{PARENT_DOC_ID}}  # np. ADR-005
implementation_log: IMPL-LOG-{{PARENT_DOC_ID}}
review_date: "{{REVIEW_DATE}}"  # 90 dni po deploy
deployment_date: "{{DEPLOY_DATE}}"
outcome: {{success|partial_success|failure}}
participants: ["{{PARTICIPANT_1}}", "{{PARTICIPANT_2}}"]
---

# Post-mortem: {{PROJECT_TITLE}}

**⚠️ UWAGA**: To jest szablon. Post-mortem przeprowadza się **ZAWSZE** (nawet przy sukcesie) 90 dni po deployment. Wypełnij wszystkie sekcje.

---

## Executive Summary

**Project**: {{PROJECT_NAME}}
**Timeline**: {{START_DATE}} → {{END_DATE}}
**Outcome**: {{SUCCESS|PARTIAL|FAILURE}}
**Key Metric**: {{PRIMARY_METRIC}} = {{VALUE}} (target: {{TARGET}})

**Overall Assessment**:
{{1-2 PARAGRAPH_SUMMARY}}

---

## Timeline

| Milestone | Planned | Actual | Delay | Reason |
|-----------|---------|--------|-------|--------|
| Start | {{DATE}} | {{DATE}} | {{N days}} | {{REASON}} |
| Design Complete | {{DATE}} | {{DATE}} | {{N days}} | {{REASON}} |
| Implementation Complete | {{DATE}} | {{DATE}} | {{N days}} | {{REASON}} |
| Deployed | {{DATE}} | {{DATE}} | {{N days}} | {{REASON}} |
| **TOTAL** | **{{X days}}** | **{{Y days}}** | **{{Y-X days}}** | - |

---

## Metrics Review

### Success Criteria (defined w DoD)

| Metric | Target | Actual (90d avg) | Status | Notes |
|--------|--------|------------------|--------|-------|
| {{METRIC_1}} | {{TARGET}} | {{ACTUAL}} | ✅/⚠️/❌ | {{COMMENT}} |
| {{METRIC_2}} | {{TARGET}} | {{ACTUAL}} | ✅/⚠️/❌ | {{COMMENT}} |
| {{METRIC_3}} | {{TARGET}} | {{ACTUAL}} | ✅/⚠️/❌ | {{COMMENT}} |
| {{METRIC_4}} | {{TARGET}} | {{ACTUAL}} | ✅/⚠️/❌ | {{COMMENT}} |

**Legend**: ✅ Met or exceeded | ⚠️ Partially met | ❌ Not met

**Overall**: {{X}}/{{Y}} metrics met ({{PERCENTAGE}}%)

---

## What Worked Better Than Expected

### 1. {{ITEM_TITLE}}

**Expected**: {{WHAT_WAS_EXPECTED}}
**Actual**: {{WHAT_ACTUALLY_HAPPENED}}
**Improvement**: {{QUANTIFIED_IMPROVEMENT}} (np. "4× faster", "+50% throughput")

**Reason**: {{WHY_THIS_WORKED_BETTER}}

**Learning**: {{WHAT_TO_REPLICATE_NEXT_TIME}}

**Evidence**: [{{EVIDENCE_ID}}] {{DESCRIPTION}}

---

### 2. {{ITEM_TITLE}}

**Expected**: {{EXPECTED}}
**Actual**: {{ACTUAL}}

**Reason**: {{WHY}}

**Learning**: {{LEARNING}}

---

## What Worked Worse Than Expected

### 1. {{ITEM_TITLE}}

**Expected**: {{WHAT_WAS_EXPECTED}}
**Actual**: {{WHAT_ACTUALLY_HAPPENED}}
**Degradation**: {{QUANTIFIED_DEGRADATION}} (np. "+32% cost", "+2 days delay")

**Reason**: {{ROOT_CAUSE}}

**Impact**:
- **Business**: {{BUSINESS_IMPACT}}
- **Technical**: {{TECHNICAL_IMPACT}}
- **Team**: {{TEAM_IMPACT}}

**Mitigation Applied**: {{WHAT_WAS_DONE}}

**Learning**: {{WHAT_TO_DO_DIFFERENTLY}}

**Evidence**: [{{EVIDENCE_ID}}]

---

### 2. {{ITEM_TITLE}}

**Expected**: {{EXPECTED}}
**Actual**: {{ACTUAL}}

**Reason**: {{WHY}}

**Impact**: {{IMPACT}}

**Mitigation**: {{MITIGATION}}

**Learning**: {{LEARNING}}

---

## What We Would Do Differently

1. **{{ACTION_1}}**
   - **Why**: {{RATIONALE}}
   - **Expected benefit**: {{BENEFIT}}
   - **Est. effort**: {{EFFORT}}

2. **{{ACTION_2}}**
   - **Why**: {{RATIONALE}}

3. **{{ACTION_3}}**
   - **Why**: {{RATIONALE}}

---

## Unexpected Discoveries (from Implementation Log)

**⚠️ REFERENCE**: Pull key discoveries from [IMPL-LOG-{{PARENT_DOC_ID}}](../impl-logs/IMPL-LOG-{{PARENT_DOC_ID}}.md)

| Date | Discovery | Impact | Resolution |
|------|-----------|--------|------------|
| {{DATE}} | {{DISCOVERY_1}} | {{IMPACT}} | {{HOW_RESOLVED}} |
| {{DATE}} | {{DISCOVERY_2}} | {{IMPACT}} | {{HOW_RESOLVED}} |

**Biggest surprise**: {{DESCRIPTION}}

---

## Re-evaluation Triggers (Status Check)

**⚠️ AUTOMATION**: Check status wszystkich triggers z parent document (ADR/RFC).

### 1. {{TRIGGER_CONDITION_1}}

**Defined in**: [{{PARENT_DOC}}]({{LINK}})
**Condition**: {{METRIC}} {{OPERATOR}} {{THRESHOLD}} sustained for {{DURATION}}
**Status**: ❌ Not triggered | ⚠️ Warning (close to threshold) | ✅ Triggered
**Current value**: {{CURRENT_VALUE}}
**Action required**: {{YES|NO}} - {{WHAT_TO_DO}}
**Next review**: {{DATE}}

---

### 2. {{TRIGGER_CONDITION_2}}

**Condition**: {{CONDITION}}
**Status**: {{STATUS}}
**Current value**: {{VALUE}}
**Action required**: {{YES|NO}}

---

## Incidents & Issues (90 days)

| Date | Severity | Issue | Root Cause | Resolution | Time to Resolve |
|------|----------|-------|------------|------------|-----------------|
| {{DATE}} | {{P0-P4}} | {{ISSUE}} | {{CAUSE}} | {{FIX}} | {{DURATION}} |

**Total incidents**: {{COUNT}}
- P0 (critical): {{COUNT}}
- P1 (high): {{COUNT}}
- P2 (medium): {{COUNT}}
- P3-P4 (low): {{COUNT}}

**MTTR** (Mean Time To Resolve): {{DURATION}}

---

## Action Items

**⚠️ TRACKABLE**: Every action item = assignee + due date + status tracking.

| ID | Title | Owner | Due Date | Priority | Status |
|----|-------|-------|----------|----------|--------|
| ACTION-001 | {{TITLE}} | {{OWNER}} | {{DATE}} | {{P}} | ✅ Done / 🔄 In progress / 📋 Planned |
| ACTION-002 | {{TITLE}} | {{OWNER}} | {{DATE}} | {{P}} | {{STATUS}} |

**Completion rate**: {{X}}/{{Y}} actions completed ({{PERCENTAGE}}%)

---

## Recommendations

### For Future Projects (Similar Scope)

1. **{{RECOMMENDATION_1}}**
   - **Category**: {{Process|Technical|Team}}
   - **Priority**: {{High|Medium|Low}}
   - **Est. effort**: {{EFFORT}}
   - **Expected benefit**: {{BENEFIT}}

2. **{{RECOMMENDATION_2}}**
   - **Category**: {{CATEGORY}}
   - **Priority**: {{PRIORITY}}

### For This Project (Ongoing)

1. **{{RECOMMENDATION_1}}**
   - **Why**: {{RATIONALE}}
   - **When**: {{TIMEFRAME}}

2. **{{RECOMMENDATION_2}}**

---

## Success Declaration

**Outcome**: {{SUCCESS|PARTIAL SUCCESS|FAILURE}}

### Success Criteria

✅ **Success** jeśli spełnia ALL:
- ≥80% metrics met or exceeded
- Zero P0 incidents w 90 dni
- Budget within +10% of planned
- Timeline within +20% of planned

⚠️ **Partial Success** jeśli spełnia SOME:
- 50-79% metrics met
- <5 P0 incidents
- Budget within +30%
- Timeline within +50%

❌ **Failure** jeśli:
- <50% metrics met
- ≥5 P0 incidents
- Budget >+30% overrun
- Timeline >+50% delay

### Declaration

**Status**: {{✅ SUCCESS | ⚠️ PARTIAL | ❌ FAILURE}}

**Justification**: {{1-2 PARAGRAPHS_EXPLAINING_DECLARATION}}

**Recommendation**: {{Continue|Pivot|Deprecate|Refactor}}

---

## Next Review

**Scheduled**: {{DATE}} ({{TIMEFRAME}} after this review)
**Trigger**: {{WHY_NEXT_REVIEW}} (np. "6 months post-deploy", "After Q1 traffic spike")
**Owner**: {{ROLE}}

---

## Appendix

### Participants

| Name | Role | Participation |
|------|------|---------------|
| {{NAME}} | {{ROLE}} | {{CONTRIBUTION}} |

### Evidence References

| ID | Type | Title | Relevance |
|----|------|-------|-----------|
| [{{E-ID}}] | {{TYPE}} | {{TITLE}} | {{WHY_REFERENCED}} |

### Related Documents

- **Parent Decision**: [{{PARENT_DOC}}]({{LINK}})
- **Implementation Log**: [IMPL-LOG-{{ID}}]({{LINK}})
- **Follow-up ADR** (jeśli applicable): [ADR-XXX]({{LINK}})

---

**© {{YEAR}} {{COMPANY}}. Document version {{VERSION}}. Post-mortem completed: {{REVIEW_DATE}}.**

---

## Document Cross-References

### Dependencies (Required Inputs)
- **[Parent ADR]** `adr-template-proof-system.md`
  - Type: `requires` | Reason: Post-mortem reviews outcomes of ADR decision | Parent ID: `parent: {{PARENT_ADR_ID}}`
- **[Implementation Log]** `implementation-log-template.md`
  - Type: `requires` | Reason: Implementation discoveries inform post-mortem analysis
- **Operational Metrics** (from monitoring/observability)
  - Type: `requires` | Evidence ID: Performance metrics, Error rates, User satisfaction

### Impacts (Downstream Documents)
- **[New ADRs]** (if changes recommended)
  - Type: `generates` | Reason: Post-mortem findings may trigger new architectural decisions | Cascade: `true`
- **[Knowledge Base]** `docs/lessons-learned/`
  - Type: `informs` | Reason: Lessons learned captured for future reference
- **[Process Improvements]** `docs/process/improvements.md`
  - Type: `informs` | Reason: Process anti-patterns identified

### Related Documents
- **[ADR Template]** `adr-template-proof-system.md` - Parent decision
- **[Implementation Log Template]** `implementation-log-template.md` - Implementation journey
- **[Evidence Note Template]** `evidence-note-template.md` - Supporting metrics/data

### Satellite Documents
- **[Action Items]** `satellites/TODO-POSTMORTEM-{{ID}}.md` - Track improvements generated by post-mortem

### Conditional Cross-References
```yaml
when incident_related === true:
  require_dependencies: [Incident Report, Root Cause Analysis]
  require_approvals: [Incident Commander, Engineering Manager]

when security_incident === true:
  require_dependencies: [Security Incident Report, Vulnerability Assessment]
  require_approvals: [Security Officer, CISO]

when customer_impact === true:
  require_dependencies: [Customer Communication Log, Support Ticket Summary]
```

### Validation Rules
- [ ] Parent ADR ID valid and exists
- [ ] Implementation log reviewed
- [ ] Success metrics measured (from ADR)
- [ ] ≥1 lesson learned documented
- [ ] ≥1 actionable improvement identified (or explicitly state none)
- [ ] Review conducted within 90 days of deployment
