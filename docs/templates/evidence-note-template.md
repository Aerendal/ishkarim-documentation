---
id: E-{{NUMBER}}  # Auto-generated (np. E-042)
type: {{TYPE}}  # benchmark | incident | analysis | requirement | cost | approval | review | test | research
title: "{{TITLE}}"
date: "{{DATE}}"  # Kiedy evidence został utworzony
author: "{{AUTHOR}}"  # Team lub osoba
parent_documents: ["{{DOC_1}}", "{{DOC_2}}"]  # Które dokumenty używają tego evidence
validity:
  valid_from: "{{DATE}}"
  valid_until: "{{DATE}}"  # Null = indefinite, Date = expires
  re_validation_trigger: "{{CONDITION}}"  # Kiedy re-validate (np. "Technology version upgrade")
---

# [E-{{NUMBER}}] {{TITLE}}

**Type**: {{TYPE}}
**Date**: {{DATE}}
**Author**: {{AUTHOR}}

**⚠️ UWAGA**: To jest szablon. Wybierz odpowiedni typ evidence (benchmark/incident/etc.) i wypełnij odpowiednią sekcję poniżej.

---

## Summary

**1-2 sentence overview**: {{BRIEF_DESCRIPTION}}

---

## Evidence Type: {{TYPE}}

**⚠️ WYBIERZ JEDNĄ SEKCJĘ** odpowiednią dla typu evidence. Usuń pozostałe sekcje.

---

### TYPE: Benchmark

**Technology/Tool**: {{WHAT_WAS_BENCHMARKED}} (np. "MongoDB 7.0")

#### Methodology

**Tool**: {{TOOL_USED}} (np. "k6", "JMeter", "sysbench", "pgbench")
**Configuration**:
- Virtual Users: {{VU_COUNT}}
- Duration: {{DURATION}}
- Ramp-up: {{RAMP_UP}}
- Test scenario: {{SCENARIO_DESCRIPTION}}

**Environment**:
- Instance type: {{INSTANCE}} (np. "Atlas M40", "RDS db.m5.large")
- Region: {{REGION}}
- Replicas: {{COUNT}}
- Network: {{NETWORK_CONFIG}}

**Dataset**:
- Size: {{DATA_SIZE}} (np. "2M rows", "10GB")
- Distribution: {{DATA_DISTRIBUTION}}

#### Results

| Metric | Value | Unit | Percentile |
|--------|-------|------|------------|
| Throughput (reads) | {{VALUE}} | ops/s | mean |
| Throughput (writes) | {{VALUE}} | ops/s | mean |
| Latency (reads) | {{VALUE}} | ms | p50 / p99 / p999 |
| Latency (writes) | {{VALUE}} | ms | p50 / p99 / p999 |
| CPU Usage | {{VALUE}} | % | avg / max |
| Memory Usage | {{VALUE}} | GB | avg / max |
| Cost | {{VALUE}} | $/month | - |

#### Key Findings

1. **{{FINDING_1}}**: {{DESCRIPTION}} (np. "Write throughput 12k ops/s exceeds target 10k")
2. **{{FINDING_2}}**: {{DESCRIPTION}}
3. **{{FINDING_3}}**: {{DESCRIPTION}}

#### Comparison (jeśli applicable)

| Metric | {{OPTION_A}} | {{OPTION_B}} | {{OPTION_C}} | Winner |
|--------|--------------|--------------|--------------|--------|
| Throughput | {{VALUE}} | {{VALUE}} | {{VALUE}} | {{OPTION}} |
| Latency p99 | {{VALUE}} | {{VALUE}} | {{VALUE}} | {{OPTION}} |
| Cost | {{VALUE}} | {{VALUE}} | {{VALUE}} | {{OPTION}} |

---

### TYPE: Incident

**Incident ID**: {{INC-XXX}}
**Date**: {{DATE}}
**Severity**: {{P0|P1|P2|P3|P4}}
**Duration**: {{DOWNTIME}} (np. "45 min", "0 min (no downtime)")

#### Timeline

| Time | Event |
|------|-------|
| {{HH:MM}} | {{EVENT_1}} (np. "Alert triggered: DB connection timeout") |
| {{HH:MM}} | {{EVENT_2}} |
| {{HH:MM}} | {{EVENT_3}} |
| {{HH:MM}} | {{EVENT_4}} (np. "Mitigation applied") |
| {{HH:MM}} | {{EVENT_5}} (np. "Incident resolved") |

#### Root Cause

**Problem**: {{1-2_SENTENCES_DESCRIBING_ISSUE}}

**Root Cause**: {{TECHNICAL_ROOT_CAUSE}}

**Contributing Factors**:
1. {{FACTOR_1}}
2. {{FACTOR_2}}

#### Impact

- **Users affected**: {{COUNT}} ({{PERCENTAGE}}% of total)
- **Requests failed**: {{COUNT}}
- **Downtime**: {{DURATION}}
- **SLA breach**: {{YES|NO}} (target: {{SLA}}, actual: {{ACTUAL}})
- **Revenue impact**: {{AMOUNT}} (estimated)

#### Resolution

**Immediate fix**: {{WHAT_WAS_DONE}}

**Long-term fix**: {{PERMANENT_SOLUTION}}

**Prevention**: {{HOW_TO_PREVENT_RECURRENCE}}

---

### TYPE: Analysis

**Analysis Focus**: {{WHAT_WAS_ANALYZED}} (np. "Product update frequency", "User behavior patterns")

#### Data Source

- **Source**: {{WHERE_DATA_CAME_FROM}} (np. "PostgreSQL audit log", "Google Analytics")
- **Time range**: {{START_DATE}} to {{END_DATE}}
- **Sample size**: {{COUNT}} (np. "2M products", "450k events")
- **Methodology**: {{STATISTICAL_METHOD}}

#### Findings

**Key Metrics**:
| Metric | Value | Distribution |
|--------|-------|--------------|
| {{METRIC_1}} | {{VALUE}} | {{DISTRIBUTION}} (np. "Median: 4 min, p90: 2.5 min") |
| {{METRIC_2}} | {{VALUE}} | {{DISTRIBUTION}} |

**Insights**:
1. **{{INSIGHT_1}}**: {{DESCRIPTION}} (np. "80% of updates happen between 9-11am")
2. **{{INSIGHT_2}}**: {{DESCRIPTION}}

**Implications**:
- {{IMPLICATION_1}}
- {{IMPLICATION_2}}

---

### TYPE: Requirement

**Source**: {{WHO_DEFINED_REQUIREMENT}} (np. "CFO", "Compliance Team", "Product Manager")
**Date**: {{DATE}}
**Priority**: {{MUST|SHOULD|NICE_TO_HAVE}}

#### Requirement Statement

{{CLEAR_STATEMENT_OF_REQUIREMENT}}

#### Rationale

**Business reason**: {{WHY_THIS_IS_NEEDED}}

**Consequences if not met**: {{WHAT_HAPPENS_IF_IGNORED}}

#### Acceptance Criteria

- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}
- [ ] {{CRITERION_3}}

#### Source Documentation

- **Document**: {{LINK_TO_SOURCE}} (np. "Email from CFO", "Regulatory document XYZ")
- **Quote**: "{{EXACT_QUOTE}}"

---

### TYPE: Cost

**Cost Analysis For**: {{WHAT_WAS_CALCULATED}} (np. "DynamoDB provisioned capacity")

#### Assumptions

- **Usage**: {{USAGE_PATTERN}} (np. "10k req/s peak, 5k sustained")
- **Data size**: {{SIZE}}
- **Region**: {{REGION}}
- **Replication**: {{REPLICATION_SETUP}}

#### Cost Breakdown

| Component | Unit Cost | Usage | Total/Month |
|-----------|-----------|-------|-------------|
| {{COMPONENT_1}} | ${{X}}/{{UNIT}} | {{QUANTITY}} | ${{TOTAL}} |
| {{COMPONENT_2}} | ${{X}}/{{UNIT}} | {{QUANTITY}} | ${{TOTAL}} |
| **TOTAL** | - | - | **${{TOTAL}}** |

#### Comparison

| Option | Cost/Month | Notes |
|--------|------------|-------|
| {{OPTION_A}} | ${{AMOUNT}} | {{NOTES}} |
| {{OPTION_B}} | ${{AMOUNT}} | {{NOTES}} |
| {{OPTION_C}} | ${{AMOUNT}} | {{NOTES}} |

#### Cost Sensitivities

**Jeśli traffic +50%**: ${{NEW_COST}} ({{PERCENTAGE}}% increase)
**Jeśli traffic -50%**: ${{NEW_COST}} ({{PERCENTAGE}}% decrease)

---

### TYPE: Approval

**Approval For**: {{WHAT_WAS_APPROVED}} (np. "Budget increase for Multi-AZ")
**Approver**: {{NAME}} ({{ROLE}})
**Date**: {{DATE}}

#### Request

**Original request**: {{WHAT_WAS_REQUESTED}}

**Justification**: {{WHY_APPROVAL_NEEDED}}

#### Approval Details

**Method**: {{EMAIL|MEETING|FORMAL_DOCUMENT}}

**Approval statement** (exact quote):
> "{{APPROVER_QUOTE}}"

**Conditions** (jeśli applicable):
- {{CONDITION_1}}
- {{CONDITION_2}}

#### Source

- **Email**: [Link to email]({{LINK}})
- **Meeting notes**: [Link]({{LINK}})
- **Signed document**: `/artifacts/approvals/{{FILENAME}}.pdf`

---

### TYPE: Review

**Review Of**: {{WHAT_WAS_REVIEWED}} (np. "ADR-005 Security Review")
**Reviewer**: {{NAME}} ({{ROLE}}, {{TEAM}})
**Date**: {{DATE}}

#### Review Findings

**Overall Assessment**: {{APPROVE|APPROVE_WITH_CONDITIONS|REJECT}}

**Strengths**:
1. {{STRENGTH_1}}
2. {{STRENGTH_2}}

**Issues Found**:
| Severity | Issue | Recommendation |
|----------|-------|----------------|
| {{HIGH|MEDIUM|LOW}} | {{ISSUE_1}} | {{RECOMMENDATION}} |
| {{SEVERITY}} | {{ISSUE_2}} | {{RECOMMENDATION}} |

**Action Items**:
- [ ] {{ACTION_1}} (Owner: {{OWNER}})
- [ ] {{ACTION_2}} (Owner: {{OWNER}})

---

### TYPE: Test

**Test Target**: {{WHAT_WAS_TESTED}} (np. "Integration tests for Cart Service")
**Date**: {{DATE}}
**Test Framework**: {{FRAMEWORK}} (np. "pytest", "JUnit", "Cypress")

#### Test Results

**Summary**:
- **Total tests**: {{COUNT}}
- **Passed**: {{COUNT}} ({{PERCENTAGE}}%)
- **Failed**: {{COUNT}}
- **Skipped**: {{COUNT}}
- **Coverage**: {{PERCENTAGE}}%

**Failures** (jeśli applicable):
| Test Case | Error | Status |
|-----------|-------|--------|
| {{TEST_1}} | {{ERROR}} | Fixed / Known issue / Won't fix |
| {{TEST_2}} | {{ERROR}} | {{STATUS}} |

**Performance** (jeśli applicable):
- Execution time: {{DURATION}}
- Slowest test: {{TEST_NAME}} ({{DURATION}})

---

## Artifacts

**⚠️ IMPORTANT**: Link to raw data, reports, screenshots, logs.

- [ ] Raw data: `/artifacts/evidence/E-{{NUMBER}}/{{FILENAME}}`
- [ ] Report/Dashboard: [Link]({{URL}})
- [ ] Screenshots: `/artifacts/evidence/E-{{NUMBER}}/screenshots/`
- [ ] Logs: `/artifacts/evidence/E-{{NUMBER}}/logs/`
- [ ] Script used: `/artifacts/evidence/E-{{NUMBER}}/{{SCRIPT}}.{{EXT}}`

---

## Related Decisions

**⚠️ BACKLINKS**: Które dokumenty używają tego evidence?

- **[{{DOC_ID_1}}]** "{{DOC_TITLE}}" - {{HOW_USED}} (np. "Opcja A benchmark")
- **[{{DOC_ID_2}}]** "{{DOC_TITLE}}" - {{HOW_USED}}

---

## Validity & Re-validation

**Valid from**: {{START_DATE}}
**Valid until**: {{END_DATE}} (jeśli known expiration) | `null` (indefinite)

**Re-validation trigger**: {{CONDITION}} (np. "MongoDB version upgrade", "Annual review", "Traffic > 20k req/s")

**Re-validation owner**: {{ROLE}}

---

## Changelog

| Date | Version | Change | Author |
|------|---------|--------|--------|
| {{DATE}} | 1.0 | Initial evidence | {{AUTHOR}} |
| {{DATE}} | 1.1 | {{CHANGE}} | {{AUTHOR}} |

---

**© {{YEAR}} {{COMPANY}}. Evidence version {{VERSION}}. Created: {{CREATED_DATE}}. Last updated: {{UPDATED_DATE}}.**

---

## Document Cross-References

### Dependencies (Required Inputs)
- **CONTEXT-DEPENDENT** - varies per evidence instance
  - Typical dependencies: Raw data sources, Experimental setup documentation, Measurement tools/scripts

### Impacts (Downstream Documents)
- **Documents citing this evidence** (specified in front-matter `cited_by` field)
  - Type: `informs` | Reason: Evidence supports claims in other documents | Examples: ADRs, RFCs, Research Plans, TDDs
- **[Evidence Index]** `satellites/EVIDENCE-INDEX-{{PROJECT}}.md`
  - Type: `registers` | Reason: All evidence notes registered in central index

### Related Documents
- **[ADR Template]** `adr-template-proof-system.md` - Relationship: `supports` | Reason: Evidence cited in ADR alternatives
- **[RFC Template]** `rfc-template-proof-system.md` - Relationship: `supports` | Reason: Evidence cited in RFC proposals
- **[Research Plan Templates]** `examples/*-research-plan-example.md` - Relationship: `supports` | Reason: Evidence supports experimental design

### Satellite Documents
- **[Raw Data]** - Original measurements, logs, screenshots stored separately
- **[Analysis Scripts]** - Code used to process/analyze data (in repo or linked)

### Conditional Cross-References
```yaml
when evidence_type === 'benchmark':
  require_dependencies: [Benchmark methodology, Environment spec (hardware, software versions)]
  validation_rules: [Reproducible (script provided), Statistical significance tested]

when evidence_type === 'user_research':
  require_dependencies: [IRB approval (if human subjects), Consent forms, Interview protocol]
  validation_rules: [Sample size justified, Participant privacy protected]

when evidence_type === 'cost_analysis':
  require_dependencies: [Pricing data sources, Assumptions documented, Time period specified]
  validation_rules: [Currency specified, Discount/growth rates justified]

when evidence_type === 'security_audit':
  require_dependencies: [Audit scope, Tools used, Severity classification]
  require_approvals: [Security Officer]
  validation_rules: [Findings actionable, Risk levels assigned]
```

### Validation Rules
- [ ] Evidence ID unique (E-{{PROJECT}}-{{NUMBER}})
- [ ] Evidence type specified (benchmark, user_research, cost_analysis, etc.)
- [ ] Source documented (where data came from)
- [ ] Methodology documented (how data was collected)
- [ ] Date/version documented (when evidence captured)
- [ ] Limitations acknowledged (what evidence does NOT prove)
- [ ] Raw data preserved (or link provided)
