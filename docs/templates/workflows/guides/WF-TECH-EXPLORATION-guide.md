# Tech Exploration Workflow - User Guide

**Workflow ID:** `WF-TECH-EXPLORATION`
**Version:** 1.0
**Last Updated:** 2025-12-29

---

## 📋 Overview

### Kiedy używać tego workflow?

Użyj Tech Exploration Workflow gdy:
- ✅ Eksplorujesz nową technologię (framework, bibliotekę, narzędzie)
- ✅ Badasz nową architekturę (microservices, serverless, event-driven)
- ✅ Porównujesz różne techniczne podejścia (SQL vs NoSQL, REST vs GraphQL)
- ✅ Musisz podjąć decyzję architektoniczną opartą na danych (nie gut-feeling)

### Główny cel

Przeprowadzić **systematyczną eksplorację techniczną** od unknown/risk → validated decision → implementation plan.

### Czas trwania

**Target:** <8 tygodni (Discovery → Decision)

### Główne fazy

```
Unknown → Hypothesis → Spike/PoC → Research Findings → Trade-off Analysis → ADR → TDD → Implementation
```

---

## 🚀 Quick Start

### Minimum Viable Workflow

Jeśli masz ograniczony czas, minimum to:
1. **HYPOTHESIS-DOC** (required) - Sformułuj hypothesis i success criteria
2. **SPIKE-SOLUTION lub POC-DOC** (required) - Szybki spike (2-5 dni) lub szczegółowy PoC (2-4 tygodnie)
3. **RESEARCH-FINDINGS** (required) - Agreguj wyniki
4. **ADR** (required) - Udokumentuj decyzję

**Total time:** 2-4 tygodnie (minimalna ścieżka)

### Full Workflow

Dla złożonych exploration:
- Dodaj **EXPERIMENT-LOG** - Track detailed experiments podczas PoC
- Dodaj **TRADE-OFF-ANALYSIS** - Jeśli porównujesz 2+ opcje
- Dodaj **ALTERNATIVE-EXPLORATION** - Systematyczne porównanie 3-5 alternatyw

**Total time:** 6-8 tygodni (pełna ścieżka)

---

## 📖 Phases - Step by Step

### Phase 1: Discovery & Hypothesis

**Duration:** 1-2 tygodnie
**Main Artifact:** `HYPOTHESIS-DOC`

#### 1.1. Start: Identify Unknown/Risk

**Gdzie to zidentyfikować:**
- 📝 Product Backlog (user story z technicznym unknownem)
- ⚠️ Risk Register (zidentyfikowane tech risk)
- 💬 Tech Discussion (team conversation o nowym approach)

**Example:**
```markdown
**Unknown:** "Which microservices communication pattern?"
**Risk:** Current monolith REST APIs won't scale dla planned 10x traffic
**Trigger:** Product roadmap requires 10x scalability w Q3
```

#### 1.2. Create Hypothesis Document

**Template:** `templates/research/HYPOTHESIS-DOC-template.md`

**Key Sections:**
```yaml
# Minimum Required Fields
id: HYPOTHESIS-DOC-MICROSERVICES-MSG-001
hypothesis_type: technical_architecture
project: PROJ-MICROSERVICES-MIGRATION

# Hypothesis Statement
H0: "Current REST synchronous communication is adequate"
H1: "Event-driven async messaging improves scalability >50%"

# Success Criteria (MUST be quantifiable!)
success_criteria:
  - criterion: "Throughput >10,000 req/s (current: 2,000 req/s)"
    threshold: ">5x improvement"
  - criterion: "Latency p99 <100ms (current: 250ms)"
    threshold: "<100ms"
  - criterion: "Zero message loss"
    threshold: "100% delivery guarantee"

# Timebox (Important!)
timebox:
  duration: "3 tygodnie"
  hard_deadline: "2025-02-15"
  justification: "Product roadmap Q3 dependent on decision"
```

**Checkpoint:** GATE-HYPOTHESIS_REVIEW
- ✅ Hypothesis is testable (clear success criteria)
- ✅ Success criteria are quantifiable (>70% recommended threshold)
- ✅ Approvers: Research Lead + Product Owner

**Decision Point:** Proceed to Spike/PoC vs Reject hypothesis

#### 1.3. Choose Exploration Approach

| Approach | Duration | When to Use |
|----------|----------|-------------|
| **SPIKE-SOLUTION** | 2-5 dni | Quick answer needed, low complexity, proof-of-feasibility |
| **POC-DOC** | 2-4 tygodnie | Detailed validation needed, high complexity, realistic data required |

**Example Decision:**
```markdown
**Chosen Approach:** PoC (Proof of Concept)

**Rationale:**
- Event-driven architecture is complex (requires message broker, event schema, etc.)
- Need realistic load testing (>10k req/s)
- Need to validate multiple aspects (throughput, latency, reliability)

**PoC Scope:**
- 2-week time frame
- Build prototype z Kafka message broker
- Test z realistic traffic (10k req/s simulation)
- Measure throughput, latency, message loss
```

---

### Phase 2: Analysis & Comparison

**Duration:** 2-3 tygodnie
**Main Artifacts:** `RESEARCH-FINDINGS`, `TRADE-OFF-ANALYSIS` (optional)

#### 2.1. Execute Spike/PoC

**During execution:**
- 📊 Track experiments w `EXPERIMENT-LOG` (timestamped observations)
- 📈 Collect metrics (performance, cost, complexity)
- ⚠️ Document anomalies i failures (NOT just successes!)

**Example Experiment Log Entry:**
```markdown
## Observation 42 - Performance Test (2025-01-15 14:30)

**Setup:** Kafka cluster (3 brokers), 10k msg/s load test

**Expected:** Throughput >10k req/s, latency p99 <100ms

**Observed:**
- ✅ Throughput: 12,500 req/s (125% of target) ✅
- ⚠️ Latency p99: 150ms (50ms ABOVE target) ⚠️
- ✅ Message loss: 0 (100% delivery)

**Analysis:**
- Throughput SUCCESS ✅
- Latency PARTIAL (need tuning - current 150ms, target <100ms)
- Hypothesis 60% validated (2/3 criteria met)

**Next Steps:**
- Tune Kafka batch.size parameter (reduce latency)
- Re-test with optimized config
```

#### 2.2. Aggregate Results → Research Findings

**Template:** `templates/research/RESEARCH-FINDINGS-template.md`

**Key Sections:**
```markdown
## Kluczowe odkrycia (Key Findings)

### Finding 1: Throughput Exceeds Target ✅
**Evidence:** Experiment Log entries 40-45
**Data:** 12,500 req/s achieved (target: 10,000 req/s)
**Confidence:** High (95%) - verified z 5 independent tests

### Finding 2: Latency Requires Tuning ⚠️
**Evidence:** Experiment Log entry 42
**Data:** p99 latency 150ms (target: <100ms)
**Confidence:** Medium (70%) - tuning może reduce to 120ms
**Mitigation:** Kafka batch.size optimization

### Finding 3: Zero Message Loss ✅
**Evidence:** Experiment Log entries 40-50
**Data:** 100% message delivery (1M messages tested)
**Confidence:** High (99%) - robust error handling

## Hypothesis Validation

**H1:** "Event-driven async messaging improves scalability >50%"

**Validation Result:** 67% validated (2/3 success criteria met)

**Recommendation:** PROCEED z async messaging + latency tuning
```

#### 2.3. (Optional) Trade-off Analysis

**Gdy używać:** Gdy porównujesz 2+ opcje (e.g., Kafka vs RabbitMQ vs AWS SQS)

**Template:** `templates/decisions/TRADE-OFF-ANALYSIS-template.md`

**Example:**
```yaml
alternatives:
  - name: "Kafka"
    scores:
      performance: 9  # 12,500 req/s
      cost: 6         # $500/month (self-hosted)
      complexity: 4   # High setup complexity
      maintainability: 7
    total_score: 8.2/10

  - name: "AWS SQS"
    scores:
      performance: 7  # 8,000 req/s (sufficient)
      cost: 8         # $200/month (managed)
      complexity: 9   # Low setup complexity
      maintainability: 9
    total_score: 7.8/10

  - name: "RabbitMQ"
    scores:
      performance: 8  # 10,000 req/s
      cost: 7         # $300/month
      complexity: 6   # Medium complexity
      maintainability: 8
    total_score: 7.5/10

recommendation: "Kafka (best performance-cost balance dla 10k req/s requirement)"
```

**Checkpoint:** GATE-VALIDATION_GATE
- ✅ Research findings validate hypothesis (>70% success criteria met)
- ✅ Evidence artifacts linked (Experiment Logs)
- ✅ Approvers: Tech Lead + Product Owner

**Decision Point:** Proceed to ADR vs More Research vs Pivot

---

### Phase 3: Decision & Approval

**Duration:** 1 tydzień
**Main Artifact:** `ADR` (Architecture Decision Record)

#### 3.1. Create ADR

**Template:** `templates/decisions/ADR-template.md`

**Key Sections:**
```markdown
## Decision

**We will adopt event-driven architecture z Kafka message broker dla microservices communication.**

## Context

**Research Summary:**
- Research Findings: RESEARCH-FINDINGS-MICROSERVICES-MSG-001
- PoC validated: 67% success criteria met (2/3)
- Trade-off Analysis: Kafka scored 8.2/10 (highest)

**Business Need:**
- Product roadmap requires 10x scalability (2k → 20k req/s) w Q3 2025
- Current REST synchronous architecture won't scale

**Options Considered:**
1. Kafka (CHOSEN)
2. AWS SQS (runner-up: easier setup, but lower performance)
3. RabbitMQ (middle ground)

## Consequences

**Positive:**
- ✅ Throughput: 12,500 req/s achieved (exceeds 10k requirement)
- ✅ Reliability: Zero message loss (100% delivery)
- ✅ Scalability: Horizontal scaling tested successfully

**Negative:**
- ⚠️ Latency: 150ms p99 (target <100ms) - needs tuning
- ⚠️ Complexity: High setup complexity (DevOps effort)
- ⚠️ Cost: $500/month (vs $200 dla AWS SQS)

**Risks:**
- Latency tuning may require additional 2-week sprint
- Team needs Kafka training (1 week)

**Mitigation:**
- Sprint 16: Kafka batch.size optimization (target <120ms latency)
- Sprint 17: Team Kafka workshop
```

**Checkpoint:** GATE-DECISION_APPROVAL
- ✅ ADR approved z decision rationale
- ✅ Evidence artifacts linked (Research Findings, Trade-off Analysis)
- ✅ Approvers: Tech Lead + Architect + Product Owner

**Decision Point:** Proceed to TDD vs Re-evaluate

---

### Phase 4: Implementation Planning & Execution

**Duration:** 4-12 tygodni (zależnie od scope)
**Main Artifacts:** `TDD`, `SPRINT-CORE`

#### 4.1. Create Technical Design Document

**Template:** `templates/engineering/architecture/TDD-template.md`

**Key Sections:**
```markdown
## Architecture Overview

**Event-Driven Microservices Architecture**

[Include architecture diagram]

**Components:**
1. Kafka Cluster (3 brokers, 5 partitions per topic)
2. Event Producer services (Order Service, Payment Service)
3. Event Consumer services (Notification Service, Analytics Service)
4. Schema Registry (Avro schema management)

## Implementation Phases

**Phase 1 (Sprint 16):** Kafka cluster setup + latency optimization
**Phase 2 (Sprint 17):** Migrate Order Service → event producer
**Phase 3 (Sprint 18):** Migrate Notification Service → event consumer
**Phase 4 (Sprint 19):** Full migration + testing

## Performance Targets (from ADR)

- Throughput: >10,000 req/s ✅ (achieved 12,500 req/s)
- Latency p99: <100ms (target after tuning)
- Message loss: 0% ✅

## Migration Strategy

**Strangler Fig Pattern:**
- Keep existing REST APIs running
- Incrementally migrate services to event-driven
- Decommission REST APIs after full migration
```

#### 4.2. Execute Implementation

**Sprints:**
- Use `SPRINT-CORE-template.md` dla each sprint
- Track progress w sprint artifacts
- Link back to ADR i TDD

**Checkpoint:** GATE-REQ_FREEZE
- ✅ TDD approved (technical design complete)
- ✅ Approvers: Tech Lead + QA Lead

**Final Decision:** Proceed to Implementation

---

## ✅ Checkpoints & Gates Summary

| Phase | Checkpoint | Gate | Approvers | Decision Options |
|-------|------------|------|-----------|-----------------|
| **Discovery** | After Hypothesis | GATE-HYPOTHESIS_REVIEW | Research Lead, Product Owner | Proceed vs Reject |
| **Analysis** | After Research | GATE-VALIDATION_GATE | Tech Lead, Product Owner | Proceed vs More Research vs Pivot |
| **Decision** | After ADR | GATE-DECISION_APPROVAL | Tech Lead, Architect, Product Owner | Proceed vs Re-evaluate |
| **Implementation** | Before Sprints | GATE-REQ_FREEZE | Tech Lead, QA Lead | Proceed vs Refine |

---

## 🎯 Success Metrics

### Workflow-Level Metrics

```yaml
time_to_decision:
  target: "<8 tygodni (Discovery → Decision)"
  your_project: "_____ tygodni"
  status: "On track / Delayed"

hypothesis_validation_rate:
  target: ">70% hypotheses validated"
  your_project: "_____% (e.g., 67%)"
  status: "Pass / Fail"

decision_quality:
  target: ">85% decisions not reversed w <6 miesięcy"
  measurement: "Track DECISION-REVERSAL count"
```

---

## 💡 Tips & Best Practices

### DO ✅

1. **Quantifiable Success Criteria** - Always define measurable thresholds (>70% improvement, <100ms latency)
2. **Timebox Exploration** - Hard deadline prevents endless research (max 8 weeks)
3. **Document Failures** - Failed experiments są valuable (show what NOT to do)
4. **Realistic PoC** - Use realistic data + realistic load (not toy examples)
5. **Evidence Tracking** - Link Experiment Logs jako Evidence satellites

### DON'T ❌

1. **Vague Hypotheses** - "We think X is better" (not testable!)
2. **No Success Criteria** - How do you know when you're done?
3. **Endless Research** - No timebox → research paralysis
4. **Cherry-pick Data** - Don't hide failed experiments
5. **Skip Approvals** - Gates exist dla a reason (prevent bad decisions)

---

## 🔗 Related Documents

- **Workflow Spec:** [`specs_workflows.md`](../../specs/specs_workflows.md)
- **Gates Spec:** [`specs_gates.md`](../../specs/specs_gates.md)
- **Templates:**
  - [`HYPOTHESIS-DOC-template.md`](../../research/HYPOTHESIS-DOC-template.md)
  - [`SPIKE-SOLUTION-template.md`](../../research/SPIKE-SOLUTION-template.md)
  - [`POC-DOC-template.md`](../../research/POC-DOC-template.md)
  - [`EXPERIMENT-LOG-template.md`](../../research/EXPERIMENT-LOG-template.md)
  - [`RESEARCH-FINDINGS-template.md`](../../research/RESEARCH-FINDINGS-template.md)
  - [`TRADE-OFF-ANALYSIS-template.md`](../../decisions/TRADE-OFF-ANALYSIS-template.md)
  - [`ADR-template.md`](../../decisions/ADR-template.md)
  - [`TDD-template.md`](../../engineering/architecture/TDD-template.md)

---

## 📞 Need Help?

**Common Questions:**

**Q: What if my hypothesis is NOT validated (<70%)?**
A: You have 3 options:
1. **PIVOT** - Adjust hypothesis + retry (e.g., lower threshold, different approach)
2. **MORE RESEARCH** - Extend PoC z additional experiments
3. **STOP** - Accept that hypothesis failed (document learnings!)

**Q: Can I skip Trade-off Analysis?**
A: YES - if you have only 1 option. Trade-off Analysis is required only when comparing 2+ alternatives.

**Q: Can I run Tech Exploration inside Business Innovation workflow?**
A: YES - Workflows are composable. See `specs_workflows.md` → workflow_composition.

**Q: What if I need to explore 3 architectures in parallel?**
A: Use **WF-PARALLEL-BRANCHING** workflow instead (or nest it inside Tech Exploration).

---

**End of Tech Exploration Workflow Guide**
