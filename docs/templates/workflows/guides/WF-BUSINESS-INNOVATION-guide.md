# Business Innovation Workflow - User Guide

**Workflow ID:** `WF-BUSINESS-INNOVATION`
**Version:** 1.0
**Last Updated:** 2025-12-29

---

## 📋 Overview

### Kiedy używać?

✅ Startupy walidujące nowy pomysł biznesowy
✅ Product teams eksplorujące nowe features / produkty
✅ Innovation teams testujące business models
✅ Ventures / intrapreneurship initiatives

### Główny cel

**Data-driven validation** business idea od concept → MVP launch.

### Czas trwania

**Target:** <12 tygodni (Idea → MVP launch decision)

### Workflow Path

```
Idea → Hypothesis → Market Research + Customer Validation → Feasibility → Go/No-Go → Business Case → PRD → MVP
```

---

## 🚀 Quick Start

### Minimum Viable Path

1. **HYPOTHESIS-DOC** - Business hypothesis (customer problem + solution)
2. **EXPERIMENT-LOG** - Customer interviews (min 10-20 interviews)
3. **RESEARCH-FINDINGS** - Aggregate validation data
4. **GO-NO-GO-DECISION** - Data-driven go/no-go
5. **PRD** - MVP scope (jeśli GO)

**Time:** 6-8 tygodni (fast validation)

### Full Workflow (Recommended)

Add:
- **MARKET-ANALYSIS** - TAM/SAM/SOM research
- **FEASIBILITY-STUDY** - Technical + Economic + Legal feasibility
- **BUSINESS-CASE** - ROI justification, financial projections
- **TDD** - Technical design dla MVP

**Time:** 10-12 tygodni (complete validation)

---

## 📖 Phases

### Phase 1: Ideation & Hypothesis (Week 1-2)

**Artifacts:** `HYPOTHESIS-DOC`, `MARKET-ANALYSIS`, `EXPERIMENT-LOG`

**Key Steps:**

1. **Formulate Business Hypothesis**
```yaml
H1: "SMB accountants spend >5h/week on manual invoice processing"
H2: "AI-powered tool can reduce to <30 min/week (90% reduction)"
H3: "SMBs willing to pay $100-200/month dla this solution"

success_criteria:
  - criterion: ">70% interviewed confirm >5h/week pain point"
  - criterion: "Willingness to pay >$100/month"
  - criterion: "TAM >$100M dla SMB segment"
```

2. **Plan Customer Validation**
- Min 10-20 customer interviews
- Target: Early adopter segment (most pain)
- Questions: Pain point severity, current solutions, willingness to pay

3. **Initial Market Research**
- TAM/SAM/SOM estimation
- Competitor analysis
- Market trends

**Checkpoint:** GATE-HYPOTHESIS_VALIDATION
- ✅ Customer problem validated (>10 interviews confirm pain)
- ✅ Approvers: Product Owner + Business Lead

**Decision:** Proceed vs Pivot

---

### Phase 2: Validation (Week 3-6)

**Artifacts:** `RESEARCH-FINDINGS`, `MARKET-ANALYSIS`, `FEASIBILITY-STUDY`

**Key Steps:**

1. **Customer Validation**
```markdown
**Interviews Conducted:** 20 SMB accountants

**Results:**
- 17/20 confirm >5h/week pain point (85%) ✅
- 15/20 willing to pay $100-200/month (75%) ✅
- Top pain points: Manual data entry (90%), Reconciliation errors (80%)

**Conclusion:** Customer problem VALIDATED ✅
```

2. **Market Validation**
```yaml
TAM: $5B (invoice processing software market globally)
SAM: $500M (SMB segment, US+EU)
SOM: $50M (realistic 3-year capture, 10% SAM)

Competitor Analysis:
  - 3 incumbents: Poor SMB UX, expensive ($500+/month)
  - Opportunity: Simplified UX + affordable pricing ($100-200/month)
```

3. **Feasibility Study**
```yaml
technical_feasibility:
  result: FEASIBLE ✅
  evidence: "PoC shows 92% OCR accuracy, NLP achievable"

economic_feasibility:
  result: VIABLE ✅
  data:
    CAC: $150 (SEO + content marketing)
    LTV: $1,800 (12-month avg retention)
    LTV/CAC: 12:1 ✅

legal_feasibility:
  result: COMPLIANT ✅
  note: "GDPR applicable (invoice data = personal data), achievable"
```

**Checkpoint:** GATE-MARKET_VALIDATION + GATE-FEASIBILITY_CHECK
- ✅ Market size attractive (TAM >$100M)
- ✅ Customer validation >70%
- ✅ Technical + Economic + Legal feasibility confirmed
- ✅ Approvers: Product Owner, Business Lead, CTO, CFO, Legal

**Decision:** Proceed to Go/No-Go vs Pivot vs Terminate

---

### Phase 3: Go/No-Go Decision (Week 7)

**Artifact:** `GO-NO-GO-DECISION`

**Key Evaluation Criteria:**

```yaml
go_no_go_criteria:
  customer_validation:
    required: ">70% interviewed confirm pain"
    actual: "85%"
    status: PASS ✅

  market_size:
    required: "TAM >$100M"
    actual: "$5B TAM, $500M SAM"
    status: PASS ✅

  economic_viability:
    required: "LTV/CAC >3x"
    actual: "12:1"
    status: PASS ✅

  feasibility:
    required: "All feasibility checks pass"
    actual: "Technical ✅, Economic ✅, Legal ✅"
    status: PASS ✅

overall_decision: GO
```

**Checkpoint:** GATE-GO_NO_GO
- ✅ All criteria met
- ✅ Approvers: CEO + Product Owner + Investors (if applicable)

**Decision Options:**
- **GO** → Proceed to Business Case + PRD
- **PIVOT** → Adjust hypothesis (e.g., different customer segment)
- **NO-GO** → Archive idea, document learnings

---

### Phase 4: Planning (Week 8-10)

**Artifacts:** `BUSINESS-CASE`, `PRD`

**Key Steps:**

1. **Business Case**
```yaml
investment:
  development: $300K (6-month MVP development)
  marketing: $150K (initial customer acquisition)
  operations: $50K (infrastructure, support)
  total: $500K

financial_projections:
  year_1_revenue: $300K (150 customers @ $200/month avg)
  year_2_revenue: $1.2M (500 customers)
  year_3_revenue: $2.5M (1,000 customers)

roi:
  break_even: "Month 18"
  roi_3_year: "5x"

  approval_status: APPROVED ✅
```

2. **PRD - MVP Scope**
```markdown
## MVP Features

### P0 (Must Have dla MVP):
- OCR invoice upload (PDF, JPG, PNG)
- AI categorization (5 invoice formats supported)
- Export to accounting software (QuickBooks, Xero)
- Processing time <30 min/week (vs 5h manual)

### P1 (Nice to Have):
- Multi-currency support
- Custom categorization rules

### P2 (Future):
- Mobile app
- API dla custom integrations

## Success Metrics

**North Star:** 90% accuracy OCR + <30 min processing time
**Adoption:** 100 paying customers in first 6 months
**Retention:** 70% MoM retention (month-over-month)
```

**Checkpoint:** GATE-REQ_FREEZE
- ✅ Business case approved (ROI >3x)
- ✅ PRD approved (MVP scope defined)
- ✅ Approvers: Product Owner + Tech Lead + Business Lead

**Decision:** Proceed to MVP Execution

---

### Phase 5: Execution (Week 11-32 ~ 6 months)

**Artifacts:** `TDD`, `SPRINT-CORE` (multiple), `TEST-PLAN`, `DEPLOYMENT-GUIDE`

**Implementation Phases:**

```
Sprint 1-2:  Setup (infra, architecture)
Sprint 3-6:  Core features (OCR, AI categorization)
Sprint 7-10: Export integrations (QuickBooks, Xero)
Sprint 11-12: Testing + Beta launch
```

**Checkpoint:** GATE-RELEASE_READY
- ✅ MVP implemented
- ✅ Tests passing
- ✅ Launch ready
- ✅ Approvers: Product Owner + Tech Lead + QA Lead

**Final Decision:** Launch MVP ✅

---

## ✅ Checkpoints Summary

| Phase | Gate | Approvers | Decision |
|-------|------|-----------|----------|
| Ideation | GATE-HYPOTHESIS_VALIDATION | Product Owner, Business Lead | Proceed vs Pivot |
| Validation | GATE-MARKET_VALIDATION | Product Owner, Business Lead, Investor | Proceed vs Pivot |
| Validation | GATE-FEASIBILITY_CHECK | CTO, CFO, Legal | Proceed vs Re-scope vs Terminate |
| Go/No-Go | GATE-GO_NO_GO | CEO, Product Owner, Investors | GO vs PIVOT vs NO-GO |
| Planning | GATE-REQ_FREEZE | Product Owner, Tech Lead, Business Lead | Proceed vs Refine |
| Execution | GATE-RELEASE_READY | Product Owner, Tech Lead, QA Lead | Launch vs Delay |

---

## 🎯 Success Metrics

```yaml
time_to_mvp:
  target: "<12 tygodni (Idea → MVP launch decision)"

validation_accuracy:
  target: ">80% validated hypotheses lead to successful MVPs"
  measurement: "MVPs meeting success criteria / total MVPs"

pivot_rate:
  target: "20-40% (healthy pivot rate)"
  note: "Too high (>50%) = weak initial hypothesis. Too low (<10%) = not honest enough"
```

---

## 💡 Tips & Best Practices

### DO ✅

1. **Interview Early Adopters** - Target customers z MOST pain (easiest to validate)
2. **Quantify Pain** - "5 hours/week" (not "a lot of time")
3. **Ask Willingness to Pay** - Real commitment test (not "would you use this?")
4. **Start Small** - MVP = Minimum (not "all features we can think of")
5. **Honest Pivot** - If validation fails, pivot quickly (don't force GO)

### DON'T ❌

1. **Build First, Validate Later** - Classic mistake ("build it and they will come")
2. **Interview Friends/Family** - Biased feedback (not real customers)
3. **Vague TAM** - "Huge market" (quantify: $XB TAM, $YM SAM, $ZM SOM)
4. **Feature Creep** - MVP ≠ "all nice-to-have features"
5. **Ignore Economics** - Even if customers love it, check LTV/CAC ratio

---

## 📞 Common Questions

**Q: How many customer interviews are enough?**
A: **Min 10-20 dla early validation**. If 70%+ confirm pain → validated. If <50% → pivot.

**Q: What if we can't find 10 customers to interview?**
A: **RED FLAG** - If you can't find 10 people to talk to, how will you find 1,000 to sell to? Reconsider market.

**Q: Can we skip Market Analysis?**
A: **For quick validation: YES** (use Experiment Log only). **For investor funding: NO** (investors expect TAM/SAM/SOM).

**Q: What if Feasibility fails (e.g., technical not feasible)?**
A: **Options:**
1. **Re-scope** - Simplify solution (maybe AI too complex → start with rule-based)
2. **Terminate** - If fundamentally not feasible, NO-GO decision

---

## 🔗 Related Documents

- **Workflow Spec:** [`specs_workflows.md`](../../specs/specs_workflows.md)
- **Templates:**
  - [`HYPOTHESIS-DOC-template.md`](../../research/HYPOTHESIS-DOC-template.md)
  - [`EXPERIMENT-LOG-template.md`](../../research/EXPERIMENT-LOG-template.md)
  - [`RESEARCH-FINDINGS-template.md`](../../research/RESEARCH-FINDINGS-template.md)
  - [`FEASIBILITY-template.md`](../../pre-production/FEASIBILITY-template.md)
  - [`GO-NO-GO-DECISION-template.md`](../../decisions/GO-NO-GO-DECISION-template.md)
  - [`BUSINESS-CASE-template.md`](../../pre-production/BUSINESS-CASE-template.md)
  - [`PRD-template.md`](../../engineering/requirements/PRD-template.md)

---

**End of Business Innovation Workflow Guide**
