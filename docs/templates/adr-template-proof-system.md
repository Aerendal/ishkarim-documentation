---
id: ADR-XXX  # Auto-generated (np. ADR-006)
title: "{{DECISION_TITLE}}"  # Wypełnij: Krótki tytuł decyzji
type: adr
status: draft  # draft → review → approved → deployed → closed
created: "{{CREATED_DATE}}"  # Auto-populated
updated: "{{UPDATED_DATE}}"  # Auto-populated
decision_date: "{{DECISION_DATE}}"  # Kiedy podjęto decyzję
decision_maker: ["{{ROLE_1}}", "{{ROLE_2}}"]  # Kto podejmował decyzję

# Bramki wejścia (co wpływa na ten dokument)
dependencies:
  - id: "{{DEPENDENCY_ID}}"  # np. RFC-2024-08
    title: "{{DEPENDENCY_TITLE}}"
    type: requires  # requires | informs
    status_constraint: [approved, completed]
    reason: "{{WHY_THIS_DEPENDENCY}}"
    evidence: ["{{EVIDENCE_ID}}"]  # np. E-040

  # Dodaj więcej dependencies jeśli potrzeba

# Bramki wyjścia (na co wpływa ten dokument)
impacts:
  - id: "{{IMPACT_TARGET_ID}}"  # np. IMPL-CART-DB
    title: "{{IMPACT_TARGET_TITLE}}"
    type: blocks  # blocks | informs | impacts
    until: "{{THIS_DOC_ID}}.status == approved"
    reason: "{{WHY_THIS_BLOCKS}}"
    cascade: true  # true = zmiana generuje TODO, false = tylko notyfikacja

  # Dodaj więcej impacts jeśli potrzeba

# Context snapshot (T₀ - stan w momencie decyzji)
context_snapshot:
  budget: "{{BUDGET}}"  # np. "$5k/month"
  team_size: {{TEAM_SIZE}}  # np. 2
  team_skills: ["{{SKILL_1}}", "{{SKILL_2}}"]  # np. ["SQL", "Python"]
  timeline: "{{TIMELINE}}"  # np. "Launch by 2024-10-01"
  constraints:
    - "{{CONSTRAINT_1}}"  # np. "GDPR compliance"
    - "{{CONSTRAINT_2}}"  # np. "ACID required (ADR-003)"
    # Dodaj więcej constraints

# Evidence trail
evidence_ids:
  - "{{EVIDENCE_ID_1}}"  # np. E-042 (MongoDB benchmark)
  - "{{EVIDENCE_ID_2}}"  # np. E-043 (MySQL benchmark)
  # Dodaj wszystkie evidence notes (≥1 per alternative)

# Alternatives considered
alternatives:
  - id: "OPTION-A"
    title: "{{OPTION_A_TITLE}}"
    status: rejected  # selected | rejected | deferred
    reason: "{{WHY_REJECTED}}"
    evidence: ["{{EVIDENCE_ID}}"]

  - id: "OPTION-B"
    title: "{{OPTION_B_TITLE}}"
    status: selected  # Tylko jedna może być selected
    reason: "{{WHY_SELECTED}}"
    evidence: ["{{EVIDENCE_ID}}"]

  # Dodaj minimum 2 opcje (zalecane: 3-4)

# Satellites (auto-generated lub manual)
satellites:
  - "TODO-{{THIS_DOC_ID}}"
  - "IMPL-LOG-{{THIS_DOC_ID}}"
  - "POST-MORTEM-{{THIS_DOC_ID}}"
  - "DOR-{{THIS_DOC_ID}}"
  - "DOD-{{THIS_DOC_ID}}"

# Changelog (obowiązkowy)
changelog:
  - version: "1.0"
    date: "{{CREATED_DATE}}"
    author: "{{AUTHOR}}"
    changes: "Initial version"
    reason: "N/A"

  # Przy każdej edycji dodaj nowy wpis:
  # - version: "1.1"
  #   date: "YYYY-MM-DD"
  #   changes: "Budget updated $2.5k → $3.3k (Multi-AZ)"
  #   reason: "Incident [E-051] showed single-AZ = SPOF"
  #   approved_by: "CFO"
  #   evidence: ["E-056"]
---

# {{DECISION_TITLE}}

**⚠️ UWAGA**: To jest szablon. Usuń wszystkie `{{PLACEHOLDERS}}` i zastąp rzeczywistą treścią. Usuń tę notatkę po wypełnieniu.

---

## Bramki wejścia (co wpłynęło na ten dokument)

### Globalne (między dokumentami)

- **[{{DEPENDENCY_ID}}]** "{{DEPENDENCY_TITLE}}" → {{REASON}}
  - Typ: {{TYPE}} (requires = blokuje start, informs = kontekst)
  - Status constraint: {{STATUS_CONSTRAINT}}
  - Evidence: [{{EVIDENCE_ID}}]

### Wewnętrzne (między sekcjami tego dokumentu)

- Sekcja "Context" → wpływa na "Decision" (constraints determinują opcje)
- Sekcja "Alternatives" → wpływa na "Consequences" (rejected options = accepted risks)

---

## Bramki wyjścia (na co ten dokument wpływa)

### Globalne (między dokumentami)

- **[{{IMPACT_TARGET_ID}}]** "{{IMPACT_TARGET_TITLE}}" ({{TYPE}})
  - Typ bramki: `{{blocks|informs|impacts}}`
  - Warunek: {{UNTIL_CONDITION}}
  - Cascade: `{{true|false}}` (true = zmiana w tym ADR → auto TODO dla target)
  - Uzasadnienie: {{WHY_THIS_IMPACTS}}

### Wewnętrzne (między sekcjami)

- Sekcja "Decision" ({{SELECTED_OPTION}}) → wpływa na "Deployment" (specific config)
- Sekcja "Benchmarks" → wpływa na "Monitoring" (metryki do śledzenia)

---

## Context (T₀: {{DECISION_DATE}})

### Global Context

**Budget**: {{BUDGET}}
**Team**: {{TEAM_SIZE}} {{ROLE}}
- Skills: {{SKILLS_LIST}}
- Experience: {{EXPERIENCE_WITH_TECHNOLOGIES}}

**Timeline**: {{TIMELINE}}

**Business Constraints**:
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}

**Tech Landscape** (dostępne opcje w momencie decyzji):
- {{TECHNOLOGY_1}} (version X)
- {{TECHNOLOGY_2}} (version Y)
- {{TECHNOLOGY_3}} (version Z)

### Internal Context

**Previous Decisions** (które już podjęliśmy i wpływają na tę decyzję):
- **[{{PREV_DECISION_ID}}]**: "{{PREV_DECISION_TITLE}}" → {{CONSTRAINT_FROM_PREV}}

**Baseline Assumptions** (z {{SOURCE_DOC}}):
- {{ASSUMPTION_1}}
- {{ASSUMPTION_2}}
- {{ASSUMPTION_3}}

---

## Alternatives Considered

**⚠️ STORYTELLING REQUIRED**: Opisz WSZYSTKIE opcje jako narrację (dlaczego rozważaliśmy, co testowaliśmy, dlaczego odrzuciliśmy/wybraliśmy). NIE pisz fact lists.

### Opcja A: {{OPTION_A_TITLE}}

**Benchmark** [{{EVIDENCE_ID}}]:
- {{METRIC_1}}: {{VALUE_1}}
- {{METRIC_2}}: {{VALUE_2}}
- Cost: {{COST}}

**Pros**:
- {{PRO_1}}
- {{PRO_2}}

**Cons** (ODRZUCONA):
- **{{CRITICAL_CON}}**
  - {{EXPLANATION}}
  - {{IMPACT}}
- {{CON_2}}

**Evidence**:
- [{{EVIDENCE_ID}}] {{EVIDENCE_TITLE}}

---

### Opcja B: {{OPTION_B_TITLE}}

**Benchmark** [{{EVIDENCE_ID}}]:
- {{METRICS}}

**Pros**:
- {{PROS}}

**Cons** (ODRZUCONA):
- **{{CRITICAL_CON}}**

**Evidence**:
- [{{EVIDENCE_ID}}]

---

### Opcja C: {{OPTION_C_TITLE}} ✓ WYBRANA

**Benchmark** [{{EVIDENCE_ID}}]:
- {{METRICS}}

**Pros**:
- {{PROS}}

**Cons** (AKCEPTUJEMY):
- {{CON_1}}
  - Mitigation: {{MITIGATION}}
  - Re-evaluation trigger: {{TRIGGER}}

**Evidence**:
- [{{EVIDENCE_ID}}]

---

### Opcja D: {{OPTION_D_TITLE}} (jeśli applicable)

**Benchmark** [{{EVIDENCE_ID}}]:
- {{METRICS}}

**Cons** (ODRZUCONA):
- {{REJECTION_REASON}}

**Evidence**:
- [{{EVIDENCE_ID}}]

---

## Decision: {{SELECTED_OPTION_TITLE}}

**⚠️ STORYTELLING REQUIRED**: Opisz DLACZEGO wybraliśmy tę opcję w formie narracji porównawczej.

Wybraliśmy **{{SELECTED_OPTION}}** z następującym uzasadnieniem:

### Dlaczego {{SELECTED}}, a nie {{OPTION_A}}?
- {{COMPARISON_RATIONALE_A}}
- {{SPECIFIC_REASON_vs_A}}

### Dlaczego {{SELECTED}}, a nie {{OPTION_B}}?
- {{COMPARISON_RATIONALE_B}}
- {{SPECIFIC_REASON_vs_B}}

### Dlaczego {{SELECTED}}, a nie {{OPTION_D}}? (jeśli applicable)
- {{COMPARISON_RATIONALE_D}}

---

## Consequences

### Risks Accepted

1. **{{RISK_1_TITLE}}**
   - Opis: {{RISK_DESCRIPTION}}
   - Mitigation: {{MITIGATION_STRATEGY}}
   - Re-evaluation trigger: {{TRIGGER_CONDITION}}
   - Estimated timeline: {{TIME_TO_MITIGATE}}

2. **{{RISK_2_TITLE}}**
   - Opis: {{RISK_DESCRIPTION}}
   - Mitigation: {{MITIGATION_STRATEGY}}

### Benefits Gained

1. **{{BENEFIT_1}}**: {{DESCRIPTION}}
2. **{{BENEFIT_2}}**: {{DESCRIPTION}}
3. **{{BENEFIT_3}}**: {{DESCRIPTION}}

---

## Re-evaluation Triggers

**⚠️ AUTOMATION**: System automatycznie monitoruje następujące warunki. Ustaw alerts w Grafana/CloudWatch.

1. **{{TRIGGER_CONDITION_1}}**
   - Warunek: {{SPECIFIC_METRIC}} {{OPERATOR}} {{THRESHOLD}} sustained for {{DURATION}}
   - Action: {{WHAT_TO_DO}}
   - Owner: {{ROLE}}
   - Monitoring: {{ALERT_NAME}} w {{MONITORING_TOOL}}

2. **{{TRIGGER_CONDITION_2}}**
   - Warunek: {{CONDITION}}
   - Action: {{ACTION}}
   - Owner: {{OWNER}}

3. **{{TRIGGER_CONDITION_3}}**
   - Warunek: {{CONDITION}}
   - Action: {{ACTION}}

---

## Implementation Notes

**Link do Implementation Log**: [IMPL-LOG-{{THIS_DOC_ID}}](../satellites/impl-logs/IMPL-LOG-{{THIS_DOC_ID}}.md)

**⚠️ UWAGA**: Implementation log jest tworzony automatycznie gdy status → `in-progress`. Dodawaj wpisy podczas implementacji:
- Unexpected discoveries
- Plan deviations
- Edge cases
- Performance surprises

**Major discoveries podczas implementacji** (wypełnij po deployment):
- {{DISCOVERY_1}}: {{DESCRIPTION}} → Solution: {{SOLUTION}}
- {{DISCOVERY_2}}: {{DESCRIPTION}} → Solution: {{SOLUTION}}

---

## Post-mortem

**Link do Post-mortem**: [POST-MORTEM-{{THIS_DOC_ID}}](../satellites/post-mortems/POST-MORTEM-{{THIS_DOC_ID}}.md)

**Scheduled**: 90 days after deploy (auto-trigger: {{DEPLOY_DATE + 90}})

**Success Metrics** (to be reviewed):
- [ ] {{METRIC_1}} {{OPERATOR}} {{TARGET}}
- [ ] {{METRIC_2}} {{OPERATOR}} {{TARGET}}
- [ ] {{METRIC_3}} {{OPERATOR}} {{TARGET}}
- [ ] {{METRIC_4}} {{OPERATOR}} {{TARGET}}

---

## Appendix

### Evidence Notes Summary

| ID | Type | Title | Date |
|----|------|-------|------|
| [{{EVIDENCE_ID_1}}] | {{TYPE}} | {{TITLE}} | {{DATE}} |
| [{{EVIDENCE_ID_2}}] | {{TYPE}} | {{TITLE}} | {{DATE}} |

### Related Documents

- **Predecessor**: [{{PREV_DOC}}] - {{DESCRIPTION}}
- **Successor**: [{{NEXT_DOC}}] - {{DESCRIPTION}}
- **Parallel**: [{{RELATED_DOC}}] - {{DESCRIPTION}}

---

**© {{YEAR}} {{COMPANY}}. Document version {{VERSION}}. Last updated: {{UPDATED_DATE}}.**

---

## Document Cross-References

### Dependencies (Required Inputs)
- **CONTEXT-DEPENDENT** - varies per ADR instance
  - Typical dependencies: RFC that triggered this ADR, Previous ADRs that constrain, Evidence notes (benchmarks, analyses), Requirements documents (PRD, TDD sections)

### Impacts (Downstream Documents)
- **[Implementation Log]** `implementation-log-template.md`
  - Type: `generates` | Reason: When ADR status → `in-progress`, auto-create implementation log | Cascade: `true`
- **[Post-Mortem]** (90 days post-deployment)
  - Type: `schedules` | Reason: ADR includes success metrics to be reviewed in post-mortem
- **Downstream Documents** (specified in ADR front-matter `impacts` section)
  - Type: `blocks` or `informs` | Example: ADR-005 (database choice) blocks TDD Section 4 (database schema)

### Related Documents
- **[RFC Template]** `rfc-template-proof-system.md` - Relationship: `precedes` | Reason: RFC typically precedes ADR (proposal → decision)
- **[Implementation Log Template]** `implementation-log-template.md` - Relationship: `spawns` | Reason: ADR spawns implementation log when work begins
- **[Post-Mortem Template]** `post-mortem-template.md` - Relationship: `spawns` | Reason: ADR spawns post-mortem 90 days post-deploy

### Satellite Documents
- **[TODO]** - Generated when ADR status → `draft`
- **[Implementation Log]** `IMPL-LOG-{{ADR_ID}}.md` - Auto-created when status → `in-progress`
- **[Post-Mortem]** `POST-MORTEM-{{ADR_ID}}.md` - Scheduled for deploy_date + 90 days
- **[DOR]** - Criteria: RFC approved (if applicable), Evidence gathered (≥1 per alternative)
- **[DOD]** - Criteria: ≥2 alternatives considered, Decision maker approved, Consequences documented

### Conditional Cross-References
```yaml
when budget_impact > 10000:
  require_approvals: [CFO, VP Engineering]

when affects_customer_facing_systems:
  require_dependencies: [Customer Impact Assessment]

when security_relevant:
  require_dependencies: [Security Review]
  require_approvals: [Security Officer]
```

### Validation Rules
- [ ] ≥2 alternatives considered (RULE-ADR-MIN-ALTS)
- [ ] Evidence for each alternative (≥1 benchmark/analysis per option)
- [ ] Decision maker identified and approved
- [ ] Consequences section has ≥1 accepted risk
- [ ] Re-evaluation triggers are measurable (not vague)
