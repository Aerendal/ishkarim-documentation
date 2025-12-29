---
id: WORKFLOW-GUIDE-001
title: "Concept Exploration Workflows - User Guide"
type: guide
domain: process
status: draft
created: 2025-12-29
updated: 2025-12-29
owner: System Architecture Team
parent: PROPOZYCJA-4-Concept-Exploration-Workflows

dependencies:
  - id: specs_workflows.md
    type: implements
    reason: "Implements workflows defined in specs"
  - id: specs_gates.md
    type: uses
    reason: "Uses gates as workflow checkpoints"
  - id: dependency_graph.md
    type: visualizes
    reason: "Visualizes workflow paths in Grafy I, J, K, L"
---

# Concept Exploration Workflows - User Guide

**Version:** 1.0
**Last Updated:** 2025-12-29
**Source:** [PROPOZYCJA-4-Concept-Exploration-Workflows](../../proposals/PROPOZYCJA-4-Concept-Exploration-Workflows.md)

---

## Table of Contents

1. [Overview](#overview)
2. [When to Use Concept Exploration Workflows](#when-to-use-concept-exploration-workflows)
3. [Workflow 1: Tech Exploration](#workflow-1-tech-exploration)
4. [Workflow 2: Business Innovation](#workflow-2-business-innovation)
5. [Workflow 3: Risk Mitigation](#workflow-3-risk-mitigation)
6. [Workflow 4: Parallel Branching](#workflow-4-parallel-branching)
7. [Case Studies](#case-studies)
8. [Success Metrics](#success-metrics)
9. [Integration Guide](#integration-guide)
10. [Quick Reference](#quick-reference)
11. [FAQ](#faq)
12. [Templates Matrix](#templates-matrix)

---

## Overview

### What Are Concept Exploration Workflows?

Concept Exploration Workflows to **end-to-end procesy** definiujące JAK używać szablonów dokumentacji (z Propozycji 1, 2, 3) w różnych kontekstach badawczych i decyzyjnych.

**Problem bez workflows:**
- 🔴 Zespoły mają szablony (Hypothesis, Experiment, PoC, Decision Log), ale nie wiedzą "co dalej?"
- 🔴 Research jest ad-hoc, każdy projekt wymyśla własny proces
- 🔴 Brak checkpoints → endless exploration bez clear decision points

**Rozwiązanie z workflows:**
- ✅ **Clear path**: Od unknowns → validated decisions → implementation
- ✅ **Repeatable**: Zdefiniowane procesy dla różnych kontekstów
- ✅ **Checkpoints**: Decision gates w każdym workflow
- ✅ **Integration**: Workflows łączą szablony z gatami i dependency grafem

### 4 Workflows

| Workflow | Use Case | Duration | Flow |
|----------|----------|----------|------|
| **Tech Exploration** | Software R&D (nowe technologie, architektury) | <8 weeks | Unknown → Hypothesis → Experiment → Decision → Implementation |
| **Business Innovation** | Product/Startup validation (pomysły biznesowe) | <12 weeks | Idea → Research → Validation → Business Case → MVP |
| **Risk Mitigation** | Enterprise risk management (mitigation alternatives) | <6 weeks | Risk → Alternatives → Trade-off → Decision → Mitigation |
| **Parallel Branching** | R&D concurrent exploration (testowanie wielu opcji) | <6 weeks | Parent → Branch 1/2/3 → Compare → Merge/Kill |

### Key Principles

1. **End-to-End**: Każdy workflow ma clear start i end
2. **Checkpoints**: Decision gates w kluczowych momentach
3. **Composability**: Workflows można zagnieżdżać (np. Tech Exploration w Business Innovation)
4. **Flexibility**: Artefakty required vs optional (dopasowanie do kontekstu)
5. **Auditability**: Każdy krok dokumentowany dla późniejszej analizy

---

## When to Use Concept Exploration Workflows

### Decision Tree

```
┌─ Masz nieznaną technologię / architekturę?
│  └─ YES → **Tech Exploration Workflow**
│
├─ Masz nowy pomysł biznesowy / produkt?
│  └─ YES → **Business Innovation Workflow**
│
├─ Masz zidentyfikowane ryzyko do zmitygowania?
│  └─ YES → **Risk Mitigation Workflow**
│
└─ Chcesz przetestować 2-3 podejścia równolegle?
   └─ YES → **Parallel Branching Workflow**
```

### Use Case Examples

**Tech Exploration:**
- Exploring React Server Components dla performance
- Evaluating microservices architecture (monolith → microservices)
- Testing Kafka vs RabbitMQ dla event-driven system

**Business Innovation:**
- Startup validating "AI invoice processing dla SMB"
- Product team exploring new feature (subscription model)
- Market validation dla nowego targetu klientów

**Risk Mitigation:**
- Mitigating vendor lock-in (AWS-only → multi-cloud)
- Addressing compliance risk (GDPR implementation)
- Reducing technical debt (legacy system modernization)

**Parallel Branching:**
- AI team testing 3 model architectures (Transformer vs GNN vs RF)
- Frontend team comparing frameworks (React vs Vue vs Svelte)
- Database choice (PostgreSQL vs MongoDB vs Cassandra)

---

## Workflow 1: Tech Exploration

### Overview

**Use Case:** Software development R&D - exploring new technologies, architectures, tools
**Flow:** Unknown/Risk → Hypothesis → Experiment/PoC → Decision → Implementation
**Duration:** <8 weeks

### When to Use

Use Tech Exploration Workflow when:
- ✅ You need to evaluate a new technology / architecture / tool
- ✅ There's technical uncertainty that needs validation
- ✅ Decision has significant technical impact (>4 weeks implementation)
- ✅ You want data-driven decision (not "let's use X because it's trendy")

**Don't use if:**
- ❌ Technology is already proven in your context (just implement)
- ❌ Decision is trivial (use Decision Log instead)
- ❌ Timeframe is urgent (<1 week) - use Spike Solution directly

### Process Flow

```
Phase 1: Discovery → Phase 2: Analysis → Phase 3: Decision → Phase 4: Implementation
```

#### Phase 1: Discovery

**Goal:** Formulate and validate hypothesis

**Artifacts:**
- **HYPOTHESIS-DOC** (required) - Formulate testable hypothesis
- **SPIKE-SOLUTION** (optional) - Quick exploration (2-5 days) if you need fast answer
- **POC-DOC** (optional) - Detailed validation (2-4 weeks) if you need thorough testing
- **EXPERIMENT-LOG** (required if PoC) - Track execution, results, learnings

**Checkpoint:** GATE-HYPOTHESIS_REVIEW

**Decision Point:** "Hypothesis validated? Proceed to analysis vs Reject hypothesis"

#### Phase 2: Analysis

**Goal:** Aggregate research results and analyze options

**Artifacts:**
- **RESEARCH-FINDINGS** (required) - Aggregate all experiment results
- **TRADE-OFF-ANALYSIS** (required if 2+ options) - Quantitative scoring of alternatives
- **OPTION-COMPARISON-MATRIX** (optional) - Qualitative comparison

**Checkpoint:** GATE-VALIDATION_GATE

**Decision Point:** "Which option to choose? Results validate hypothesis (>70%)?"

#### Phase 3: Decision

**Goal:** Make formal decision

**Artifacts:**
- **ADR** (required) - Architecture Decision Record (for significant decisions)
- **DECISION-LOG** (alternative) - Lightweight decision log (for simpler decisions)

**Checkpoint:** GATE-DECISION_APPROVAL

**Decision Point:** "Proceed vs Pivot vs Stop?"

#### Phase 4: Implementation

**Goal:** Design and implement solution

**Artifacts:**
- **TDD** (required) - Technical Design Document
- **SPRINT-CORE** (required) - Sprint planning and execution

**Checkpoint:** GATE-REQ_FREEZE

**Decision Point:** "Ready for production?"

### Checkpoints Summary

| Checkpoint | Criteria | Decision |
|------------|----------|----------|
| **GATE-HYPOTHESIS_REVIEW** (after Discovery) | Hypothesis is testable, clear success criteria | Proceed to Spike/PoC vs Reject |
| **GATE-VALIDATION_GATE** (after Analysis) | Results validate hypothesis (>70% success criteria) | Proceed to ADR vs More Research vs Pivot |
| **GATE-DECISION_APPROVAL** (after Decision) | Stakeholders approve decision | Proceed to TDD vs Re-evaluate |
| **GATE-REQ_FREEZE** (after TDD) | TDD approved, ready for implementation | Proceed to Implementation vs Refine |

### Real Example: React Server Components

**Scenario:** Explore React Server Components dla performance optimization

**Phase 1: Discovery (Week 1-3)**
1. **HYPOTHESIS-DOC-RSC**
   - H1: RSC reduce initial page load by 30%+
   - Success criteria: <500ms initial load (current: 800ms)
   - Timebox: 3 weeks

2. **SPIKE-SOLUTION-RSC-QUICK** (3 days)
   - Quick spike: Check compatibility z current setup
   - Result: Compatible ✅, but Redux needs refactoring

3. **POC-DOC-RSC** (2 weeks)
   - Build prototype z realistic data
   - **EXPERIMENT-LOG-RSC:** Track performance benchmarks
   - Result: 420ms initial load ✅ (48% improvement)

**Checkpoint:** GATE-HYPOTHESIS_REVIEW ✅ (hypothesis validated)

**Phase 2: Analysis (Week 4)**
4. **RESEARCH-FINDINGS-RSC**
   - Key findings: Performance goal achieved, Redux migration needed
   - Recommendation: Proceed with RSC + Zustand migration

5. **TRADE-OFF-ANALYSIS-RSC**
   - Option A: RSC + Zustand (performance + refactor cost)
   - Option B: Stick with current (no performance gain)
   - Scoring: Option A wins (8.5 vs 6.2)

**Checkpoint:** GATE-VALIDATION_GATE ✅ (results validate hypothesis)

**Phase 3: Decision (Week 5)**
6. **ADR-RSC-ADOPTION**
   - Decision: Migrate to RSC + Zustand
   - Context: Trade-off analysis, PoC results
   - Consequences: 2 sprints refactoring, 48% performance improvement

**Checkpoint:** GATE-DECISION_APPROVAL ✅ (decision approved)

**Phase 4: Implementation (Week 6-8)**
7. **TDD-RSC-ARCHITECTURE**
   - Technical design dla RSC implementation
   - Migration plan: Redux → Zustand
   - Performance targets documented

**Checkpoint:** GATE-REQ_FREEZE ✅ (ready for implementation)

8. **Implementation (Sprint 16-17)**
   - Execute migration
   - Validate performance targets

**Outcome:**
- ✅ 48% performance improvement achieved
- ✅ Data-driven decision (not "let's use RSC because it's new")
- ✅ Clear migration path documented
- ✅ Risk identified and mitigated (Redux refactor)

---

## Workflow 2: Business Innovation

### Overview

**Use Case:** Product/Startup validation - exploring new business ideas, validating market fit
**Flow:** Idea → Research → Validation → Business Case → PRD → Implementation
**Duration:** <12 weeks

### When to Use

Use Business Innovation Workflow when:
- ✅ You have a new business idea / product concept
- ✅ You need to validate customer problem and market size
- ✅ Decision requires business case justification (investment, resources)
- ✅ You want to avoid "build and hope" - validate before building

**Don't use if:**
- ❌ Feature is small iteration (use standard PRD process)
- ❌ Market is already validated (go directly to Business Case)
- ❌ It's internal tool with no market validation needed

### Process Flow

```
Phase 1: Ideation → Phase 2: Validation → Phase 3: Go/No-Go → Phase 4: Planning → Phase 5: Execution
```

#### Phase 1: Ideation

**Goal:** Formulate and validate business hypothesis

**Artifacts:**
- **HYPOTHESIS-DOC** (required) - Business hypothesis
- **MARKET-ANALYSIS** (required) - TAM/SAM/SOM research
- **EXPERIMENT-LOG** (required) - Customer interviews, A/B tests

**Checkpoint:** GATE-HYPOTHESIS_VALIDATION

**Decision Point:** "Customer problem validated (>10 interviews confirm pain)?"

#### Phase 2: Validation

**Goal:** Validate market size and feasibility

**Artifacts:**
- **RESEARCH-FINDINGS** (required) - Aggregate validation data
- **FEASIBILITY-STUDY** (required) - Technical/Economic/Legal feasibility

**Checkpoint:** GATE-MARKET_VALIDATION

**Decision Point:** "Market viable (TAM >$100M) and feasible?"

#### Phase 3: Go/No-Go

**Goal:** Make go/no-go decision

**Artifacts:**
- **GO-NO-GO-DECISION** (required)

**Checkpoint:** GATE-GO_NO_GO

**Decision Point:** "GO vs PIVOT vs NO-GO"
- **GO:** Proceed to business case
- **PIVOT:** Return to ideation with learnings
- **NO-GO:** Archive idea, document learnings

#### Phase 4: Planning

**Goal:** Build business case and requirements

**Artifacts:**
- **BUSINESS-CASE** (required) - ROI justification
- **PRD** (required) - Detailed product requirements

**Checkpoint:** GATE-REQ_FREEZE

**Decision Point:** "Business case approved? Requirements frozen?"

#### Phase 5: Execution

**Goal:** Build and launch MVP

**Artifacts:**
- **SPRINT-CORE** (required) - Sprint execution
- **TDD** (required) - Technical design

**Checkpoint:** GATE-RELEASE_READY

**Decision Point:** "Ready to launch?"

### Checkpoints Summary

| Checkpoint | Criteria | Decision |
|------------|----------|----------|
| **GATE-HYPOTHESIS_VALIDATION** (after Ideation) | >10 interviews confirm pain point | Proceed to Market Research vs Pivot |
| **GATE-MARKET_VALIDATION** (after Validation) | TAM >$100M, SAM >$10M, realistic SOM | Proceed to Feasibility vs Pivot |
| **GATE-GO_NO_GO** (after Feasibility) | Technically feasible, economically viable, legally compliant | GO vs PIVOT vs NO-GO |
| **GATE-REQ_FREEZE** (after Business Case) | ROI >3x, Payback <2 years, PRD frozen | Proceed to MVP vs Re-evaluate |
| **GATE-RELEASE_READY** (after MVP) | Testing complete, production ready | Launch vs Refine |

### Real Example: AI Invoice Processing for SMB

**Scenario:** Startup eksploruje "AI-powered invoice processing dla SMB"

**Phase 1: Ideation (Week 1-2)**
1. **HYPOTHESIS-DOC-INVOICE-AI**
   - H1: SMB spend >5 hours/week na manual invoice processing
   - H2: AI can reduce to <30 min/week (90% reduction)
   - Validation: Interview 20 SMB accountants

2. **EXPERIMENT-LOG-CUSTOMER-INTERVIEWS**
   - Week 1-2: 20 interviews conducted
   - Result: 17/20 confirm >5h/week pain point ✅
   - Willingness to pay: $100-200/month

**Checkpoint:** GATE-HYPOTHESIS_VALIDATION ✅ (17/20 = 85% confirmation)

**Phase 2: Validation (Week 3-4)**
3. **MARKET-ANALYSIS-INVOICE-AI**
   - TAM: $5B (invoice processing software market)
   - SAM: $500M (SMB segment)
   - SOM: $50M (realistic 3-year capture)

4. **RESEARCH-FINDINGS-INVOICE-AI**
   - Customer validation: 85% confirm pain point ✅
   - Market validation: TAM/SAM/SOM attractive ✅
   - Competitor analysis: 3 incumbents, but poor SMB UX
   - Recommendation: PROCEED to Feasibility

**Checkpoint:** GATE-MARKET_VALIDATION ✅ (market size attractive)

5. **FEASIBILITY-STUDY-INVOICE-AI**
   - Technical: OCR + NLP achievable (PoC shows 92% accuracy)
   - Economic: CAC $150, LTV $1,800 (12:1 ratio) ✅
   - Legal: GDPR compliant (invoice data = personal data)
   - Recommendation: GO

**Phase 3: Go/No-Go (Week 5)**
6. **GO-NO-GO-DECISION-INVOICE-AI**
   - Criteria met: Customer validation ✅, Market size ✅, Feasibility ✅
   - Decision: **GO**

**Checkpoint:** GATE-GO_NO_GO ✅ (GO decision)

**Phase 4: Planning (Week 6-8)**
7. **BUSINESS-CASE-INVOICE-AI**
   - Investment: $500K (development + marketing)
   - ROI: 5x in Year 3
   - Break-even: Month 18
   - Approval: Investors approved

8. **PRD-INVOICE-AI**
   - Features: OCR upload, AI categorization, Export to accounting software
   - Success metrics: 90% accuracy, <30 min/week processing time
   - MVP scope: Support 5 invoice formats

**Checkpoint:** GATE-REQ_FREEZE ✅ (PRD approved, requirements frozen)

**Phase 5: Execution (Week 9-32 = 6 months)**
9. **MVP Implementation**
   - SPRINT-CORE x 6 sprints
   - TDD dla architecture

**Checkpoint:** GATE-RELEASE_READY ✅ (ready to launch)

**Outcome:**
- ✅ Systematyczna walidacja (85% customer validation before building)
- ✅ Data-driven go/no-go (TAM/SAM/SOM analysis)
- ✅ Clear business case (5x ROI, Month 18 break-even)
- ✅ MVP launched with validated features

---

## Workflow 3: Risk Mitigation

### Overview

**Use Case:** Enterprise risk management - exploring mitigation alternatives for identified risks
**Flow:** Risk Identified → Alternative Exploration → Trade-off Analysis → Decision → Mitigation Plan
**Duration:** <6 weeks

### When to Use

Use Risk Mitigation Workflow when:
- ✅ You have identified risk (from Risk Register, RAID log)
- ✅ Risk requires exploration of mitigation alternatives
- ✅ Decision has significant impact (cost, timeline, architecture)
- ✅ You want quantitative trade-off analysis (not gut feeling)

**Don't use if:**
- ❌ Mitigation is obvious (just implement)
- ❌ Risk is low impact (accept risk)
- ❌ Only 1 mitigation option (use ADR directly)

### Process Flow

```
Phase 1: Exploration → Phase 2: Analysis → Phase 3: Decision → Phase 4: Implementation
```

#### Phase 1: Exploration

**Goal:** Identify and validate mitigation options

**Artifacts:**
- **ALTERNATIVE-EXPLORATION** (required) - Identify min 3 mitigation options
- **POC-DOC** (optional) - Validate options if needed

**Checkpoint:** GATE-OPTIONS_IDENTIFIED

**Decision Point:** "Min 3 options identified?"

#### Phase 2: Analysis

**Goal:** Quantitative scoring of alternatives

**Artifacts:**
- **TRADE-OFF-ANALYSIS** (required) - Quantitative scoring

**Checkpoint:** GATE-DECISION_REVIEW

**Decision Point:** "Clear winner (score >7/10)?"

#### Phase 3: Decision

**Goal:** Select mitigation approach

**Artifacts:**
- **ADR** (required) - Decision record
- **DECISION-LOG** (alternative) - Lightweight decision

**Checkpoint:** GATE-APPROVAL

**Decision Point:** "Mitigation approved?"

#### Phase 4: Implementation

**Goal:** Implement and monitor mitigation

**Artifacts:**
- **MITIGATION-PLAN** (required) - Implementation plan
- **MONITORING-PLAN** (required) - Risk tracking

**Checkpoint:** None (continuous monitoring)

**Decision Point:** "Mitigation effective?"

### Checkpoints Summary

| Checkpoint | Criteria | Decision |
|------------|----------|----------|
| **GATE-OPTIONS_IDENTIFIED** (after Exploration) | Min 3 mitigation options identified | Proceed to Analysis vs More Research |
| **GATE-DECISION_REVIEW** (after Analysis) | Clear winner (score >7/10) OR justified tie | Proceed to Decision vs Re-evaluate weights |
| **GATE-APPROVAL** (after Decision) | Stakeholders approve mitigation approach | Proceed to Implementation vs Reconsider |

### Real Example: Vendor Lock-in Risk (AWS)

**Scenario:** Enterprise projekt – Risk: Single cloud provider (AWS) = vendor lock-in

**Phase 1: Exploration (Week 1-2)**
1. **RISK-OVERVIEW-TECH-005**
   - Description: 100% AWS dependency → vendor lock-in, pricing risk
   - Impact: High (potential 50% cost increase if AWS raises prices)
   - Probability: Medium

2. **ALTERNATIVE-EXPLORATION-MULTI-CLOUD**
   - Option A: Multi-cloud (AWS + Azure)
   - Option B: Cloud-agnostic architecture (Kubernetes + Terraform)
   - Option C: Accept risk (AWS-only, negotiate long-term contract)
   - Option D: Hybrid cloud (on-prem + AWS)

**Checkpoint:** GATE-OPTIONS_IDENTIFIED ✅ (4 options identified, min 3 required)

3. **POC-DOC-KUBERNETES-ABSTRACTION**
   - PoC: Test Kubernetes abstraction layer
   - Result: Achievable, but 20% performance overhead
   - Cost: +$50K development

**Phase 2: Analysis (Week 3-4)**
4. **TRADE-OFF-ANALYSIS-MULTI-CLOUD**
   - Criteria: Cost (30%), Complexity (25%), Vendor independence (30%), Performance (15%)
   - Scoring:
     - Option A (Multi-cloud): 6.8/10 (high complexity, high cost)
     - **Option B (K8s abstraction): 7.5/10** (best balance) ✅
     - Option C (AWS-only): 5.2/10 (highest risk)
     - Option D (Hybrid): 6.1/10 (high ops overhead)
   - Recommendation: Option B

**Checkpoint:** GATE-DECISION_REVIEW ✅ (clear winner: 7.5/10)

**Phase 3: Decision (Week 5)**
5. **ADR-KUBERNETES-ABSTRACTION**
   - Decision: Adopt Kubernetes dla cloud abstraction
   - Context: Trade-off analysis, PoC validation
   - Consequences: +$50K dev cost, 20% performance overhead, vendor independence achieved

**Checkpoint:** GATE-APPROVAL ✅ (stakeholders approve)

**Phase 4: Implementation (Week 6+, 6 months)**
6. **MITIGATION-PLAN-VENDOR-LOCK-IN**
   - Implementation: Migrate to Kubernetes over 6 months
   - Milestones: Q1 dev, Q2 staging, Q3 production
   - Success criteria: 100% services Kubernetes-based, <25% performance overhead

7. **MONITORING-PLAN-CLOUD-COST**
   - Track cloud costs monthly
   - Alert if cost increase >15% MoM
   - Review vendor options quarterly

**Outcome:**
- ✅ Systematyczna eksploracja (4 alternatives compared)
- ✅ Quantitative trade-off (not "let's go multi-cloud because trendy")
- ✅ Clear mitigation plan (6-month roadmap)
- ✅ Risk reduced (vendor independence achieved)

---

## Workflow 4: Parallel Branching

### Overview

**Use Case:** R&D concurrent exploration - testing 2-3 approaches in parallel
**Flow:** Parent Concept → Branch 1 & 2 & 3 → Compare → Merge/Kill Decision
**Duration:** <6 weeks

### When to Use

Use Parallel Branching Workflow when:
- ✅ You have 2-3 viable approaches to explore
- ✅ Approaches are significantly different (architectural differences)
- ✅ You have resources dla parallel teams (2-3 engineers per branch)
- ✅ Sequential exploration would take too long (3x timeframe)

**Don't use if:**
- ❌ Only 1 approach viable (use Tech Exploration instead)
- ❌ Approaches are too similar (minor variations)
- ❌ Resources constrained (can't split team)
- ❌ Timeline is urgent (<2 weeks)

### Process Flow

```
Phase 1: Fork → Phase 2: Exploration → Phase 3: Comparison → Phase 4: Merge/Kill
```

#### Phase 1: Fork

**Goal:** Create parallel exploration branches

**Artifacts:**
- **CONCEPT-BRANCH** (multiple, one per branch) - Define each approach

**Checkpoint:** GATE-BRANCH_CREATION

**Decision Point:** "Branches properly isolated? Separate teams/resources?"

#### Phase 2: Exploration

**Goal:** Parallel execution with mid-point review

**Artifacts:**
- **EXPERIMENT-LOG** (per branch) - Track each branch's progress

**Checkpoint:** GATE-MID_POINT_REVIEW (Week 2)

**Decision Point:** "Continue all branches or kill underperforming?"

#### Phase 3: Comparison

**Goal:** Compare all branch results

**Artifacts:**
- **RESEARCH-FINDINGS** (aggregate) - Compare results from all branches

**Checkpoint:** GATE-RESULTS_REVIEW

**Decision Point:** "All branches complete?"

#### Phase 4: Merge/Kill

**Goal:** Decide which branches to merge/kill

**Artifacts:**
- **ADR** (required) - Decision record
- **DECISION-LOG** (alternative) - Lightweight decision

**Checkpoint:** GATE-MERGE_KILL_DECISION

**Decision Point:** "Merge best / Kill rest / Hybrid"
- **MERGE:** Merge winning branch to parent
- **KILL:** Archive failed branches (preserve learnings)
- **HYBRID:** Combine insights from multiple branches

### Checkpoints Summary

| Checkpoint | Criteria | Decision |
|------------|----------|----------|
| **GATE-BRANCH_CREATION** (after Fork) | Clear divergence point, separate teams/resources | Proceed with parallel exploration |
| **GATE-MID_POINT_REVIEW** (Week 2) | Each branch shows progress, no blockers | Continue vs Kill underperforming branch |
| **GATE-RESULTS_REVIEW** (after Experiments) | All branches have complete results | Proceed to Comparison |
| **GATE-MERGE_KILL_DECISION** (after Comparison) | Clear winner OR justified hybrid | Merge best / Kill rest / Hybrid |

### Real Example: Churn Prediction Model

**Scenario:** AI team eksploruje 3 architektury dla churn prediction model

**Phase 1: Fork (Week 0)**
1. **HYPOTHESIS-DOC-CHURN-PREDICTION (Parent)**
   - H1: AI model can predict churn z accuracy >80%
   - 3 approaches to explore: Transformer, GNN, Random Forest

2. **CONCEPT-BRANCH-001-TRANSFORMER**
   - Team A (2 data scientists)
   - Approach: BERT-based transformer dla user behavior sequences
   - Timeline: 4 tygodnie

3. **CONCEPT-BRANCH-002-GNN**
   - Team B (2 data scientists)
   - Approach: Graph Neural Network (user relationships graph)
   - Timeline: 4 tygodnie

4. **CONCEPT-BRANCH-003-RANDOM-FOREST**
   - Team C (1 data scientist – baseline)
   - Approach: Classical ML (feature engineering + RF)
   - Timeline: 2 tygodnie

**Checkpoint:** GATE-BRANCH_CREATION ✅ (3 branches, separate teams)

**Phase 2: Exploration (Week 1-4)**
5. **Parallel Execution**
   - EXPERIMENT-LOG-TRANSFORMER: Track training, hyperparameter tuning
   - EXPERIMENT-LOG-GNN: Track graph construction, model training
   - EXPERIMENT-LOG-RF: Baseline model (fast iteration)

**Checkpoint:** GATE-MID_POINT_REVIEW (Week 2)
- Transformer: 75% accuracy (promising) ✅
- GNN: 70% accuracy (slow progress) ⚠️
- RF: 72% accuracy (baseline achieved) ✅
- **Decision:** Continue all branches (no clear loser yet)

**Phase 3: Comparison (Week 4)**
6. **RESEARCH-FINDINGS-CHURN-COMPARISON**
   - Transformer: 83% accuracy ✅, 50ms inference ✅
   - GNN: 85% accuracy ✅, 300ms inference ❌ (too slow)
   - RF: 78% accuracy ❌, 10ms inference ✅

**Checkpoint:** GATE-RESULTS_REVIEW ✅ (all branches complete)

7. **TRADE-OFF-ANALYSIS-CHURN-MODEL**
   - Criteria: Accuracy (40%), Inference speed (30%), Maintainability (20%), Explainability (10%)
   - Scoring:
     - **Transformer: 8.2/10** (best balance) ✅
     - GNN: 7.5/10 (high accuracy but slow)
     - RF: 6.8/10 (fast but low accuracy)
   - Recommendation: Transformer for production, RF as fallback

**Phase 4: Merge/Kill (Week 5-6)**
8. **DECISION-MERGE-TRANSFORMER**
   - Decision: **Merge** Transformer branch to Parent (production)
   - Decision: **Kill** GNN branch (slow inference, not production-ready)
   - Decision: **Keep** RF as fallback (explainability dla compliance audits)

9. **ADR-CHURN-MODEL-ARCHITECTURE**
   - Decision: Transformer for production, RF for auditing
   - Context: Parallel exploration results
   - Consequences: 83% accuracy, 50ms inference, explainable fallback

**Checkpoint:** GATE-MERGE_KILL_DECISION ✅ (merge + hybrid approach)

**Outcome:**
- ✅ Parallel exploration saved time (4 weeks vs 12 weeks sequential)
- ✅ Fair comparison (same dataset, same timeframe)
- ✅ Hybrid outcome (Transformer production + RF compliance fallback)
- ✅ Documented learnings (GNN approach preserved dla future reference)

---

## Case Studies

### Case Study 1: Startup MVP - Business Innovation Workflow

**Context:** Startup building "AI invoice processing dla SMB" – using full Business Innovation workflow.

**Timeline:** Week 1-32 (8 months total, 12 weeks planning + 6 months execution)

**Workflow execution:**

**Week 1-2: Ideation Phase**
- HYPOTHESIS-DOC-INVOICE-AI created
- MARKET-ANALYSIS-INVOICE-AI (TAM/SAM/SOM research)
- EXPERIMENT-LOG-CUSTOMER-INTERVIEWS (20 interviews)
- Checkpoint: HYPOTHESIS_VALIDATION ✅ (17/20 confirm pain point)

**Week 3-4: Validation Phase**
- RESEARCH-FINDINGS-INVOICE-AI (aggregate data)
- FEASIBILITY-STUDY-INVOICE-AI (technical/economic/legal)
- Checkpoint: MARKET_VALIDATION ✅ (TAM >$100M, feasible)

**Week 5: Go/No-Go**
- GO-NO-GO-DECISION-INVOICE-AI
- Criteria met: Customer ✅, Market ✅, Feasibility ✅
- Checkpoint: GATE-GO_NO_GO ✅ (decision: GO)

**Week 6-8: Planning Phase**
- BUSINESS-CASE-INVOICE-AI (ROI 5x, break-even Month 18)
- PRD-INVOICE-AI (MVP features defined)
- Checkpoint: GATE-REQ_FREEZE ✅ (PRD approved)

**Week 9-32: Execution Phase**
- SPRINT-CORE x 6 sprints
- TDD-INVOICE-AI
- Checkpoint: GATE-RELEASE_READY ✅

**Outcome:**
- ✅ Systematyczny process (not ad-hoc)
- ✅ Clear checkpoints (go/no-go decisions data-driven)
- ✅ Complete audit trail (dla investors, dla post-launch review)
- ✅ MVP launched successfully with 85% customer validation

---

### Case Study 2: Enterprise Migration - Tech Exploration Workflow

**Context:** Enterprise migruje z monolith do microservices – using Tech Exploration workflow.

**Timeline:** Month 1-12 (1 year total, 3 months exploration + 9 months implementation)

**Workflow execution:**

**Month 1: Discovery Phase**
- UNKNOWN: "Which microservices architecture?"
- HYPOTHESIS-DOC-MICROSERVICES: "Event-driven architecture improves scalability >50%"
- POC-DOC-EVENT-DRIVEN: 2-week PoC (Kafka-based)
- EXPERIMENT-LOG-EVENT-DRIVEN: Track performance benchmarks
- Checkpoint: HYPOTHESIS_REVIEW ✅

**Month 2: Analysis Phase**
- RESEARCH-FINDINGS-MICROSERVICES: PoC results (65% scalability improvement ✅)
- ALTERNATIVE-EXPLORATION-MICROSERVICES: Compare Kafka vs RabbitMQ vs AWS SQS
- TRADE-OFF-ANALYSIS-MESSAGE-QUEUE: Quantitative scoring
- Checkpoint: VALIDATION_GATE ✅ (Kafka wins)

**Month 3: Decision Phase**
- ADR-EVENT-DRIVEN-ARCHITECTURE: Decision: Kafka-based event-driven
- ADR-MIGRATION-STRATEGY: Strangler Fig pattern
- Checkpoint: DECISION_APPROVAL ✅

**Month 4-12: Implementation Phase**
- TDD-MICROSERVICES-ARCHITECTURE
- MIGRATION-PLAN-MONOLITH-TO-MICROSERVICES
- SPRINT-CORE x 8 sprints (incremental migration)
- Checkpoint: GATE-REQ_FREEZE ✅

**Outcome:**
- ✅ Reduced migration risk (PoC validated before full commitment)
- ✅ Data-driven architecture decision (not "let's use Kafka because trendy")
- ✅ Clear migration path (strangler fig pattern dokumentowany)
- ✅ 65% scalability improvement achieved

---

### Case Study 3: R&D Team - Parallel Branching Workflow

**Context:** AI research team exploring 3 model architectures równolegle.

**Timeline:** Week 0-6 (6 weeks total, 4 weeks exploration + 2 weeks decision/merge)

**Workflow execution:**

**Week 0: Fork Phase**
- HYPOTHESIS-DOC-CHURN-PREDICTION (Parent)
- CONCEPT-BRANCH-001-TRANSFORMER (Team A)
- CONCEPT-BRANCH-002-GNN (Team B)
- CONCEPT-BRANCH-003-RF (Team C – baseline)
- Checkpoint: BRANCH_CREATION ✅

**Week 1-2: Exploration Phase (Part 1)**
- EXPERIMENT-LOG-TRANSFORMER (Team A progress)
- EXPERIMENT-LOG-GNN (Team B progress)
- EXPERIMENT-LOG-RF (Team C baseline achieved)
- Checkpoint: MID_POINT_REVIEW ✅ (all branches show progress)

**Week 3-4: Exploration Phase (Part 2)**
- Continue experiments
- Results: Transformer 83%, GNN 85%, RF 78%

**Week 5: Comparison Phase**
- RESEARCH-FINDINGS-CHURN-COMPARISON (aggregate results)
- TRADE-OFF-ANALYSIS-CHURN-MODEL (quantitative scoring)
- Checkpoint: RESULTS_REVIEW ✅

**Week 6: Merge/Kill Phase**
- ADR-CHURN-MODEL-ARCHITECTURE
- Decision: Merge Transformer (production), Keep RF (compliance fallback), Kill GNN (slow inference)
- Checkpoint: MERGE_KILL_DECISION ✅

**Outcome:**
- ✅ Parallel exploration saved time (6 weeks vs 18 weeks sequential)
- ✅ Fair comparison (same data, same timeline)
- ✅ Hybrid outcome (production + compliance fallback)
- ✅ 83% accuracy achieved (target >80%)

---

## Success Metrics

### M1: Workflow Adoption Rate

**Definicja:** % projektów using defined workflows (vs ad-hoc)
**Target:** >60% w 6 miesięcy
**Measurement:** Projects tagged with workflow_type w metadata

**How to measure:**
```yaml
# Add to document metadata:
workflow_type: TECH_EXPLORATION  # or BUSINESS_INNOVATION, RISK_MITIGATION, PARALLEL_BRANCHING
workflow_start_date: 2025-01-15
workflow_status: in_progress  # or completed, abandoned
```

---

### M2: Checkpoint Compliance

**Definicja:** % projektów które przechodzą wszystkie checkpoints w workflow
**Target:** >80%
**Measurement:** Gate validation logs

**How to measure:**
- Track gate pass/fail in validation reports
- Calculate: (projects_passing_all_gates / projects_started) * 100

---

### M3: Time-to-Decision

**Definicja:** Średni czas od start workflow → final decision
**Target:**
- Tech Exploration: <8 tygodni
- Business Innovation: <12 tygodni
- Risk Mitigation: <6 tygodni
- Parallel Branching: <6 tygodni

**Measurement:** Timestamp tracking (workflow start → ADR approved)

**How to measure:**
```yaml
# Add timestamps to documents:
workflow_start: 2025-01-15
decision_made: 2025-03-01
time_to_decision: 45 days  # auto-calculated
```

---

### M4: Workflow Completion Rate

**Definicja:** % workflows które are completed (vs abandoned mid-way)
**Target:** >70%
**Measurement:** Workflows started vs completed

**How to measure:**
- Track workflow_status: completed vs abandoned
- Calculate: (workflows_completed / workflows_started) * 100

---

### M5: Decision Quality

**Definicja:** % decisions które nie wymagają reversal w <6 miesięcy
**Target:** >85%
**Measurement:** DECISION-REVERSAL count vs total decisions

**How to measure:**
- Track decision reversals using DECISION-REVERSAL template
- Calculate: ((total_decisions - reversals_within_6mo) / total_decisions) * 100

---

## Integration Guide

### Integration z Existing Systems

#### 1. Gates System

**Workflows używają istniejących i nowych gates:**

**Existing gates (re-used):**
- GATE-GO_NO_GO (Business Innovation)
- GATE-REQ_FREEZE (Tech Exploration, Business Innovation)
- GATE-RELEASE_READY (Business Innovation)
- GATE-DECISION_APPROVAL (Tech Exploration)

**New gates (from workflows):**
- GATE-HYPOTHESIS_REVIEW (Tech Exploration, Business Innovation)
- GATE-VALIDATION_GATE (Tech Exploration)
- GATE-OPTIONS_IDENTIFIED (Risk Mitigation)
- GATE-MERGE_KILL_DECISION (Parallel Branching)

**Integration:**
- Workflows reference gates as checkpoints
- Gates validate required documents and approvals
- Gate status determines workflow progression

---

#### 2. Document Types

**Workflows używają istniejących doctypes:**

**Existing:**
- HYPOTHESIS-DOC (from Research templates)
- EXPERIMENT-LOG (from Research templates)
- POC-DOC (from Research templates)
- ADR (from Decision templates)
- DECISION-LOG (from Decision templates)
- TRADE-OFF-ANALYSIS (from Decision templates)
- TDD (from Engineering templates)
- PRD (from Product templates)
- BUSINESS-CASE (from Pre-production templates)

**May need creation (check templates/):**
- RESEARCH-FINDINGS
- ALTERNATIVE-EXPLORATION
- CONCEPT-BRANCH
- GO-NO-GO-DECISION
- MITIGATION-PLAN
- SPIKE-SOLUTION

---

#### 3. Dependency Graph

**Workflows są wizualizowane w dependency graph:**

- Graf I: Tech Exploration Workflow
- Graf J: Business Innovation Workflow
- Graf K: Risk Mitigation Workflow
- Graf L: Parallel Branching Workflow

**See:** `dependency_graph.md` lines 940-1228

---

#### 4. Sprint Integration

**Workflows mogą być wykonywane w ramach Sprint types:**

- **Discovery Sprint:** Idealne dla Phase 1-2 (Discovery, Analysis)
- **Core Sprint:** Używane dla Phase 4 (Implementation)
- **Hardening Sprint:** Post-implementation validation

**Integration:**
- Workflows definiują CO robić
- Sprints definiują JAK to zaplanować w czasie
- Workflows → Sprints: artifacts z workflow feeding into sprint planning

---

### Workflow Composability

**Workflows można zagnieżdżać:**

1. **Business Innovation ⊃ Tech Exploration**
   - Use case: Startup validating business idea needs tech feasibility
   - Example: AI Invoice Processing (Business Innovation) → OCR+NLP feasibility (Tech Exploration)

2. **Tech Exploration ⊃ Parallel Branching**
   - Use case: Tech exploration involves testing multiple architectures
   - Example: Microservices architecture (Tech Exploration) → Kafka vs RabbitMQ (Parallel Branching)

3. **Risk Mitigation ⊃ Tech Exploration**
   - Use case: Mitigating technical risk requires tech validation
   - Example: Vendor lock-in (Risk Mitigation) → Kubernetes abstraction (Tech Exploration)

---

## Quick Reference

### Which Workflow to Use?

```
START HERE
   ↓
[1] Masz nieznaną technologię/architekturę? → YES → Tech Exploration
   ↓ NO
[2] Masz nowy pomysł biznesowy/produkt? → YES → Business Innovation
   ↓ NO
[3] Masz zidentyfikowane ryzyko? → YES → Risk Mitigation
   ↓ NO
[4] Chcesz przetestować 2-3 opcje równolegle? → YES → Parallel Branching
   ↓ NO
[5] Use standard process (ADR, Decision Log, etc.)
```

---

### Workflow Duration Targets

| Workflow | Target Duration | Typical Range |
|----------|----------------|---------------|
| Tech Exploration | <8 weeks | 4-8 weeks |
| Business Innovation | <12 weeks | 8-12 weeks |
| Risk Mitigation | <6 weeks | 3-6 weeks |
| Parallel Branching | <6 weeks | 4-6 weeks |

---

### Phase Summary

| Workflow | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|----------|---------|---------|---------|---------|---------|
| Tech Exploration | Discovery | Analysis | Decision | Implementation | - |
| Business Innovation | Ideation | Validation | Go/No-Go | Planning | Execution |
| Risk Mitigation | Exploration | Analysis | Decision | Implementation | - |
| Parallel Branching | Fork | Exploration | Comparison | Merge/Kill | - |

---

## FAQ

### Q1: Czy mogę pominąć niektóre fazy workflow?

**A:** Depends on context:
- **Optional artifacts:** Tak (np. SPIKE-SOLUTION, POC-DOC)
- **Required artifacts:** Nie (np. HYPOTHESIS-DOC, ADR)
- **Checkpoints:** Nie zalecane (gates zapewniają quality)

**Best practice:** Follow full workflow first time, optimize later based on learnings.

---

### Q2: Co jeśli workflow trwa dłużej niż target duration?

**A:**
1. **Review checkpoints:** Czy wszystkie gates są passed? Może są blockers.
2. **Re-scope:** Może hipoteza jest za duża → split into smaller hypotheses
3. **Pivot:** Może czas zmienić podejście (PIVOT decision w Business Innovation)
4. **Document:** Update workflow_status i document reasons dla exceeding duration

**Target durations są guidelines, nie hard limits.**

---

### Q3: Czy mogę używać wielu workflows równocześnie?

**A:** Tak! Examples:
- **Nested:** Business Innovation ⊃ Tech Exploration (feasibility validation)
- **Parallel:** Risk Mitigation (vendor lock-in) + Tech Exploration (new architecture) running independently
- **Sequential:** Tech Exploration (architecture) → Business Innovation (product based on architecture)

**Track każdy workflow separately z własnym workflow_id.**

---

### Q4: Co jeśli nie mam niektórych szablonów (np. RESEARCH-FINDINGS)?

**A:**
1. **Check templates/ directory:** Może szablon istnieje pod inną nazwą
2. **Use existing templates:** Adapt closest template (np. use EXPERIMENT-LOG zamiast RESEARCH-FINDINGS)
3. **Create missing template:** Follow pattern from existing templates
4. **Document gap:** Add to backlog dla template creation

**Workflows działają z istniejącymi templates, missing templates nie blokują.**

---

### Q5: Kto approves gates w workflow?

**A:** Depends on gate (see specs_gates.md):
- GATE-HYPOTHESIS_REVIEW: Research Lead + Product Owner
- GATE-VALIDATION_GATE: Tech Lead + Product Owner
- GATE-GO_NO_GO: Sponsor + CFO (for business decisions)
- GATE-REQ_FREEZE: Product Owner + Tech Lead
- GATE-MERGE_KILL_DECISION: Research Lead + CTO

**Approvers mogą być dostosowani do organizacji.**

---

### Q6: Co jeśli decision jest "PIVOT" w Business Innovation?

**A:** PIVOT = return to ideation with learnings:
1. **Document learnings:** Co się nie sprawdziło? Dlaczego?
2. **Update HYPOTHESIS-DOC:** Revise hypothesis based on learnings
3. **Restart workflow:** From Phase 1 (Ideation)
4. **Track iterations:** workflow_iteration: 2 (second attempt)

**PIVOT nie jest failure - to validated learning.**

---

### Q7: Czy workflow może być abandoned?

**A:** Tak, ale tylko z clear reason:
1. **Set workflow_status: abandoned**
2. **Document reason:** Market changed, priority shifted, resource constraints
3. **Preserve artifacts:** Dla future reference (learnings are valuable)
4. **Post-mortem:** Short retrospective: co się wydarzyło? Co nauczyliśmy się?

**Abandoned workflows ≠ wasted effort. Learnings są valuable.**

---

## Templates Matrix

### Tech Exploration Workflow

| Template | Phase | Required? | Purpose |
|----------|-------|-----------|---------|
| HYPOTHESIS-DOC | Discovery | ✅ Required | Formulate testable hypothesis |
| SPIKE-SOLUTION | Discovery | Optional | Quick exploration (2-5 days) |
| POC-DOC | Discovery | Optional | Detailed validation (2-4 weeks) |
| EXPERIMENT-LOG | Discovery | Required if PoC | Track execution |
| RESEARCH-FINDINGS | Analysis | ✅ Required | Aggregate results |
| TRADE-OFF-ANALYSIS | Analysis | Required if 2+ options | Quantitative scoring |
| OPTION-COMPARISON-MATRIX | Analysis | Optional | Qualitative comparison |
| ADR | Decision | ✅ Required | Architecture decision |
| DECISION-LOG | Decision | Alternative | Lightweight decision |
| TDD | Implementation | ✅ Required | Technical design |
| SPRINT-CORE | Implementation | ✅ Required | Sprint execution |

---

### Business Innovation Workflow

| Template | Phase | Required? | Purpose |
|----------|-------|-----------|---------|
| HYPOTHESIS-DOC | Ideation | ✅ Required | Business hypothesis |
| MARKET-ANALYSIS | Ideation | ✅ Required | TAM/SAM/SOM research |
| EXPERIMENT-LOG | Ideation | ✅ Required | Customer interviews |
| RESEARCH-FINDINGS | Validation | ✅ Required | Aggregate validation data |
| FEASIBILITY-STUDY | Validation | ✅ Required | Technical/Economic/Legal |
| GO-NO-GO-DECISION | Go/No-Go | ✅ Required | GO vs PIVOT vs NO-GO |
| BUSINESS-CASE | Planning | ✅ Required | ROI justification |
| PRD | Planning | ✅ Required | Product requirements |
| SPRINT-CORE | Execution | ✅ Required | Sprint execution |
| TDD | Execution | ✅ Required | Technical design |

---

### Risk Mitigation Workflow

| Template | Phase | Required? | Purpose |
|----------|-------|-----------|---------|
| ALTERNATIVE-EXPLORATION | Exploration | ✅ Required | Identify min 3 options |
| POC-DOC | Exploration | Optional | Validate options |
| TRADE-OFF-ANALYSIS | Analysis | ✅ Required | Quantitative scoring |
| ADR | Decision | ✅ Required | Decision record |
| DECISION-LOG | Decision | Alternative | Lightweight decision |
| MITIGATION-PLAN | Implementation | ✅ Required | Implementation plan |
| MONITORING-PLAN | Implementation | ✅ Required | Risk tracking |

---

### Parallel Branching Workflow

| Template | Phase | Required? | Purpose |
|----------|-------|-----------|---------|
| HYPOTHESIS-DOC | Fork | ✅ Required | Parent hypothesis |
| CONCEPT-BRANCH | Fork | ✅ Required (multiple) | Define each branch |
| EXPERIMENT-LOG | Exploration | ✅ Required (per branch) | Track branch progress |
| RESEARCH-FINDINGS | Comparison | ✅ Required | Aggregate branch results |
| TRADE-OFF-ANALYSIS | Comparison | Recommended | Quantitative comparison |
| ADR | Merge/Kill | ✅ Required | Merge/Kill decision |
| DECISION-LOG | Merge/Kill | Alternative | Lightweight decision |

---

## Summary

### Key Takeaways

1. **4 Workflows dla różnych kontekstów:**
   - Tech Exploration: Software R&D
   - Business Innovation: Product/Startup validation
   - Risk Mitigation: Enterprise risk management
   - Parallel Branching: Concurrent R&D exploration

2. **End-to-End clarity:**
   - Każdy workflow ma clear start i end
   - Decision gates w kluczowych momentach
   - Duration targets dla każdego workflow

3. **Integration:**
   - Workflows używają existing templates
   - Gates zapewniają quality checkpoints
   - Dependency graph wizualizuje paths

4. **Composability:**
   - Workflows można zagnieżdżać
   - Business Innovation ⊃ Tech Exploration
   - Tech Exploration ⊃ Parallel Branching

5. **Success Metrics:**
   - M1: >60% adoption rate
   - M2: >80% checkpoint compliance
   - M3: Time-to-decision targets met
   - M4: >70% completion rate
   - M5: >85% decision quality

---

**Następne kroki:**
1. Choose appropriate workflow dla your use case
2. Follow process flow step-by-step
3. Document artifacts at each phase
4. Pass checkpoints before proceeding
5. Measure success metrics

**Powodzenia! 🚀**

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-29 | System Architecture Team | Initial version based on PROPOZYCJA-4 |

---

## Cross-References

### Dependencies
```yaml
dependencies:
  - id: PROPOZYCJA-4-Concept-Exploration-Workflows.md
    type: implements
    reason: "User guide implements workflows from Propozycja 4"

  - id: specs_workflows.md
    type: uses
    reason: "References formal workflow specifications"

  - id: specs_gates.md
    type: uses
    reason: "References gate checkpoints"

  - id: dependency_graph.md
    type: visualizes
    reason: "Grafy I, J, K, L visualize workflows"
```

### Related Documents
```yaml
related:
  - id: templates/research/HYPOTHESIS-DOC.md
    type: uses

  - id: templates/research/EXPERIMENT-LOG.md
    type: uses

  - id: templates/research/POC-DOC.md
    type: uses

  - id: templates/decisions/ADR-template.md
    type: uses

  - id: templates/decisions/TRADE-OFF-ANALYSIS-template.md
    type: uses
```
