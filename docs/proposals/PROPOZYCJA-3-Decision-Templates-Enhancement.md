# PROPOZYCJA 3: Decision Templates Enhancement

**Data:** 2025-12-27
**Autor:** Analiza systemu szablonów Ishkarim
**Wersja:** 1.0
**Status:** Draft

---

## 1. Uzasadnienie

### Kontekst problemu

Podejmowanie decyzji jest **kręgosłupem każdego projektu** – od strategicznych wyborów (pivot vs persist) po taktyczne (which database, which cloud provider). Złe decyzje kosztują czas, pieniądze i morale zespołu. Dobre decyzje wymagają:

1. **Structured thinking** – systematyczna eksploracja opcji, nie "gut feeling"
2. **Data-driven analysis** – empiryczne dane, benchmarki, trade-offs
3. **Stakeholder alignment** – transparentny proces, clear rationale
4. **Auditability** – ślad decyzyjny dla przyszłych zespołów i dla compliance

Aktualny system szablonów Ishkarim zawiera **ADR (Architecture Decision Records)**, który jest doskonałym narzędziem dla decyzji architektonicznych. Jednakże ADR jest:
- ✅ Świetny dla **technicznych** decyzji (architecture, tools, frameworks)
- ❌ Za ciężki dla **lightweight** decyzji (daily tactical calls)
- ❌ Niewystarczający dla **business** decyzji (pricing, go-to-market)
- ❌ Brak **structured trade-off analysis** (pros/cons są free-form, nie systematyczne)
- ❌ Brak **option comparison matrix** (porównanie 3+ opcji side-by-side)
- ❌ Brak **go/no-go decision template** (binary choices z clear criteria)

### Gap w obecnym systemie

**Co mamy:**
- ✅ **ADR** – Architecture Decision Records (świetne dla tech decisions)
- ✅ **FEASIBILITY-STUDY** – High-level feasibility assessment (go/pilot/no-go)
- ✅ **BUSINESS-CASE** – Business justification (ROI-focused)
- ✅ **ALTERNATIVE-EXPLORATION** (Propozycja 1) – Eksploracja alternatyw

**Czego brakuje:**

| Potrzeba | Obecny template | Luka |
|----------|----------------|------|
| **Lightweight decisions** | ADR (za ciężki) | Brak Decision Log dla daily decisions |
| **Trade-off analysis** | ADR §Pros/Cons (free-form) | Brak structured trade-off framework |
| **Option comparison** | Manual w ADR | Brak comparison matrix template |
| **Go/No-Go decisions** | FEASIBILITY (za szeroki) | Brak lightweight go/no-go dla feature/sprint |
| **Decision reversal** | None | Brak template gdy decyzja się nie sprawdza |
| **Impact assessment** | Buried w ADR §Consequences | Brak dedicated impact analysis |

### Dlaczego to jest problem?

**Dla projektów software:**
- 🔴 **Decision fatigue** – Zespół nie dokumentuje małych decyzji (zbyt ciężkie ADR)
- 🔴 **Poor trade-off analysis** – Pros/cons są subjective, brak systematic scoring
- 🔴 **Comparison paralysis** – Porównywanie 3+ opcji jest chaotic bez matrix
- 🔴 **Pivot risk** – Brak structured process gdy decyzja wymaga reversal

**Dla business:**
- 🔴 **Pricing decisions** – Brak template dla pricing strategy decisions
- 🔴 **Market entry** – Go/no-go dla nowych rynków jest ad-hoc
- 🔴 **Partner selection** – Vendor/partner decisions brak structured comparison

**Dla compliance:**
- 🔴 **Audit trail gaps** – Małe decyzje nie są dokumentowane → lost rationale
- 🔴 **Risk decisions** – Risk mitigation decisions brak impact assessment

### Przykłady decision gaps w real projects

**Przykład 1: Feature prioritization (Software Team)**
- **Decision:** Zbudować feature A czy B w następnym sprincie?
- **Obecny proces:** PM decides ad-hoc, team learns via Slack
- **Problem:** No rationale documented, team doesn't understand "why"
- **Potrzeba:** Lightweight Decision Log z clear criteria (impact, effort, urgency)

**Przykład 2: Vendor selection (Procurement)**
- **Decision:** AWS vs Azure vs GCP dla cloud infrastructure
- **Obecny proces:** Excel spreadsheet, email threads, scattered docs
- **Problem:** Comparison criteria inconsistent, final decision rationale unclear
- **Potrzeba:** Option Comparison Matrix z weighted criteria, scoring, final recommendation

**Przykład 3: Go/No-Go for MVP launch (Product)**
- **Decision:** Launch MVP teraz czy czekać 2 tygodnie na bugfixes?
- **Obecny proces:** Stakeholder meeting, verbal decision, no documentation
- **Problem:** When bugs surface post-launch, no record of "why we launched despite bugs"
- **Potrzeba:** Go/No-Go Decision template z clear launch criteria, risk assessment

**Przykład 4: Pricing model change (Business)**
- **Decision:** Zmienić pricing z per-user na per-feature?
- **Obecny proces:** Business Case (zbyt ciężki), albo Slack thread (za lekki)
- **Problem:** No structured trade-off analysis (revenue vs churn vs implementation cost)
- **Potrzeba:** Trade-off Analysis template z multi-dimensional scoring

**Przykład 5: Architecture decision reversal (Tech)**
- **Decision:** MongoDB nie sprawdził się (performance issues) → migrate back to PostgreSQL
- **Obecny proces:** New ADR, ale no clear process dla "decision reversal"
- **Problem:** No structured retrospective "dlaczego original decision was wrong"
- **Potrzeba:** Decision Reversal template z root cause analysis, lessons learned

---

## 2. Szczegóły implementacji

### Proponowane szablony (5 nowych)

#### 2.1. DECISION-LOG: Lightweight Decision Log

**Grupa:** decisions
**Domena:** multi (tech/product/business)
**Opis:** Lightweight template dla daily tactical decisions

**Kiedy używać:**
- Small-to-medium decisions (nie strategic)
- Decisions które wymagają dokumentacji, ale ADR jest overkill
- Daily team decisions (sprint planning, feature prioritization, bug triage)

**Struktura:**
```yaml
required_meta: [id, doctype, status, version, owner, project, decision_type, decision_date]
required_sections:
  - {id: SEC-DL-QUESTION, title: "Pytanie decyzyjne"}
  - {id: SEC-DL-CONTEXT, title: "Kontekst (1-2 zdania)"}
  - {id: SEC-DL-OPTIONS, title: "Opcje rozważane"}
  - {id: SEC-DL-DECISION, title: "Decyzja"}
  - {id: SEC-DL-RATIONALE, title: "Uzasadnienie (1-3 zdania)"}
  - {id: SEC-DL-OWNER, title: "Decision owner"}
satellites_required: []
dependencies: []
outputs: {creates_artifacts: []}
```

**Czas wypełnienia:** 5-10 minut (vs ADR: 1-2 godziny)

**Cross-References:**
```yaml
dependencies:
  - id: SPRINT-PLANNING
    type: influences
    reason: "Decision Log może być outcome ze Sprint Planning"

impacts:
  - id: BACKLOG
    type: informs
    reason: "Decisions wpływają na prioritization w backlogu"
```

**Przykład użycia:**
```markdown
---
id: DECISION-LOG-042
decision_type: feature_prioritization
decision_date: "2025-12-27"
owner: "Product Manager"
---

## Pytanie decyzyjne
Czy zbudować Feature A (social sharing) czy Feature B (export to PDF) w Sprint 15?

## Kontekst
Sprint 15 capacity: 40 story points. Both features są requested by customers.

## Opcje rozważane
1. **Feature A (social sharing)** – 25 SP, high customer demand (15 requests)
2. **Feature B (export PDF)** – 20 SP, medium demand (8 requests)
3. **Both (partial)** – Split A into smaller scope (15 SP) + B (20 SP) = 35 SP

## Decyzja
**Option 1:** Build Feature A (social sharing) – full scope

## Uzasadnienie
- Customer demand jest 2x wyższy dla A vs B
- Social sharing ma higher viral potential (growth driver)
- PDF export może poczekać do Sprint 16

## Decision owner
Product Manager (approved by Tech Lead)
```

**Różnica vs ADR:**

| Aspekt | ADR | DECISION-LOG |
|--------|-----|--------------|
| **Czas wypełnienia** | 1-2h | 5-10 min |
| **Scope** | Strategic/architectural | Tactical/operational |
| **Detail level** | High (options, consequences) | Medium (quick rationale) |
| **Stakeholders** | Multiple (formal approval) | Single (decision owner) |
| **Lifecycle** | Long-term (years) | Short-term (sprint/quarter) |

---

#### 2.2. TRADE-OFF-ANALYSIS: Structured Trade-off Analysis

**Grupa:** decisions
**Domena:** multi
**Opis:** Systematyczna analiza trade-offs dla complex decisions

**Kiedy używać:**
- Decisions z multiple competing criteria (performance vs cost vs maintainability)
- Decisions gdzie stakeholders mają różne priorities
- Decisions wymagające quantitative scoring

**Struktura:**
```yaml
required_meta: [id, doctype, status, version, owner, project, decision_context]
required_sections:
  - {id: SEC-TA-DECISION, title: "Decyzja do podjęcia"}
  - {id: SEC-TA-CRITERIA, title: "Kryteria oceny (weighted)"}
  - {id: SEC-TA-OPTIONS, title: "Opcje (min 2)"}
  - {id: SEC-TA-SCORING, title: "Scoring matrix"}
  - {id: SEC-TA-SENSITIVITY, title: "Sensitivity analysis"}
  - {id: SEC-TA-RECOMMENDATION, title: "Rekomendacja"}
  - {id: SEC-TA-TRADEOFFS, title: "Key trade-offs"}
satellites_required: [EVIDENCE, APPROVAL]
dependencies: []
outputs: {creates_artifacts: [ADR, DECISION-LOG]}
```

**Cross-References:**
```yaml
dependencies:
  - id: POC-DOC
    type: influences
    reason: "PoC data feeds into trade-off scoring"

impacts:
  - id: ADR
    type: blocks
    reason: "Trade-off analysis feeds into formal ADR"
```

**Przykład użycia:**
```markdown
## Decyzja do podjęcia
Wybór message queue dla nowego event-driven architecture: RabbitMQ vs Kafka vs AWS SQS

## Kryteria oceny (weighted)

| Kryterium | Waga | Uzasadnienie |
|-----------|------|--------------|
| **Throughput** | 30% | Critical dla high-volume events (1M+/day) |
| **Latency** | 25% | Real-time processing required (target <100ms) |
| **Operational overhead** | 20% | Team ma limited DevOps capacity |
| **Cost** | 15% | Budget constraint: <$2K/month |
| **Team expertise** | 10% | Learning curve impacts time-to-market |

## Scoring matrix

| Kryterium (waga) | RabbitMQ | Kafka | AWS SQS |
|------------------|----------|-------|---------|
| **Throughput** (30%) | 7/10 (50K msg/s) | 10/10 (1M+ msg/s) | 6/10 (10K msg/s with batching) |
| **Latency** (25%) | 9/10 (<10ms) | 7/10 (~20ms) | 6/10 (~50ms) |
| **Operational overhead** (20%) | 5/10 (self-hosted) | 4/10 (complex ops) | 10/10 (fully managed) |
| **Cost** (15%) | 8/10 (~$500/mo) | 6/10 (~$1.5K/mo) | 9/10 (~$800/mo) |
| **Team expertise** (10%) | 8/10 (team knows it) | 3/10 (steep learning curve) | 7/10 (AWS-familiar) |
| **TOTAL (weighted)** | **7.25** | **6.85** | **7.45** |

## Sensitivity analysis

**Scenario 1:** If throughput weight → 40% (current: 30%)
- Kafka wins: **7.85** (RabbitMQ: 7.05, SQS: 7.05)

**Scenario 2:** If operational overhead weight → 30% (current: 20%)
- SQS wins: **8.15** (RabbitMQ: 7.05, Kafka: 6.45)

**Scenario 3:** If team expertise weight → 20% (current: 10%)
- RabbitMQ wins: **7.65** (Kafka: 6.55, SQS: 7.45)

## Rekomendacja
**AWS SQS** (score: 7.45) – narrow win over RabbitMQ (7.25)

### Uzasadnienie
- SQS wygrywa przez **operational simplicity** (managed service)
- RabbitMQ ma lepszą latency, ale SQS latency (50ms) jest acceptable
- Kafka odrzucone przez steep learning curve + high ops overhead

### Warunki
- If throughput grows >100K msg/s → revisit Kafka
- If latency requirement drops <10ms → revisit RabbitMQ

## Key trade-offs

| Trade-off | Wybierając SQS, zyskujemy... | ...ale tracimy... |
|-----------|------------------------------|-------------------|
| **Ops simplicity** | Zero DevOps overhead (managed) | Control over infrastructure |
| **Cost predictability** | Pay-per-use, no upfront | Potentially higher at scale |
| **Latency** | Good enough (50ms) | Ultra-low latency (RabbitMQ: 10ms) |
```

**Wartość dodana:**
- ✅ Quantitative scoring (nie subjective "RabbitMQ jest lepsze")
- ✅ Weighted criteria (stakeholders mogą debate weights, nie opinions)
- ✅ Sensitivity analysis (pokazuje jak zmiana priorities wpływa na outcome)
- ✅ Transparent trade-offs (wszyscy wiedzą "co tracą")

---

#### 2.3. OPTION-COMPARISON-MATRIX: Option Comparison Matrix

**Grupa:** decisions
**Domena:** multi
**Opis:** Side-by-side comparison dla 3+ opcji

**Różnica vs Trade-off Analysis:**
- **Trade-off Analysis** = weighted scoring, quantitative
- **Option Comparison** = qualitative, comprehensive side-by-side

**Kiedy używać:**
- Vendor selection (np. CRM: Salesforce vs HubSpot vs Zoho)
- Tool selection (np. CI/CD: Jenkins vs GitLab CI vs CircleCI)
- Partner selection (np. Payment gateway: Stripe vs PayPal vs Square)

**Struktura:**
```yaml
required_meta: [id, doctype, status, version, owner, project, comparison_type]
required_sections:
  - {id: SEC-OCM-PURPOSE, title: "Cel porównania"}
  - {id: SEC-OCM-OPTIONS, title: "Opcje (3-5)"}
  - {id: SEC-OCM-CRITERIA, title: "Kryteria porównania"}
  - {id: SEC-OCM-MATRIX, title: "Comparison matrix"}
  - {id: SEC-OCM-PROS-CONS, title: "Pros/Cons per option"}
  - {id: SEC-OCM-RECOMMENDATION, title: "Rekomendacja (top 1-2)"}
satellites_required: [EVIDENCE]
dependencies: []
outputs: {creates_artifacts: [TRADE-OFF-ANALYSIS, ADR]}
```

**Cross-References:**
```yaml
dependencies:
  - id: VENDOR-REQUIREMENTS
    type: requires
    reason: "Requirements drive comparison criteria"

impacts:
  - id: TRADE-OFF-ANALYSIS
    type: influences
    reason: "Comparison matrix feeds into quantitative trade-off analysis"
  - id: ADR
    type: informs
    reason: "Final selection documented in ADR"
```

**Przykład użycia:**
```markdown
## Cel porównania
Wybór CRM platform dla sales team (target: 50 users, B2B SaaS sales)

## Opcje (5 → shortlisted to 3)

**Evaluated:**
1. Salesforce
2. HubSpot
3. Zoho CRM
4. ~~Pipedrive~~ (eliminated: brak enterprise features)
5. ~~Freshsales~~ (eliminated: weak integration ecosystem)

**Shortlist:** Salesforce, HubSpot, Zoho

## Comparison matrix

| Kryterium | Salesforce | HubSpot | Zoho CRM |
|-----------|-----------|---------|----------|
| **Pricing** | $150/user/mo | $90/user/mo | $50/user/mo |
| **Setup time** | 6-8 weeks | 2-3 weeks | 1-2 weeks |
| **Customization** | ⭐⭐⭐⭐⭐ Unlimited | ⭐⭐⭐⭐ High | ⭐⭐⭐ Medium |
| **Integrations** | ⭐⭐⭐⭐⭐ 5000+ apps | ⭐⭐⭐⭐ 1000+ apps | ⭐⭐⭐ 500+ apps |
| **Reporting** | ⭐⭐⭐⭐⭐ Advanced | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Basic |
| **Mobile app** | ⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Best-in-class | ⭐⭐⭐ Good |
| **Support** | 24/7 phone+chat | Email (24h SLA) | Email (48h SLA) |
| **Learning curve** | Steep (2-3 months) | Moderate (1 month) | Easy (1-2 weeks) |
| **Scalability** | Unlimited | Up to 10K users | Up to 5K users |

## Pros/Cons

### Salesforce
**Pros:**
- ✅ Industry standard (best-in-class features)
- ✅ Unlimited customization (Apex, Lightning)
- ✅ Best integrations ecosystem
- ✅ Best reporting/analytics

**Cons:**
- ❌ Most expensive ($150/user/mo = $7.5K/mo for 50 users)
- ❌ Steep learning curve (3 months training)
- ❌ Overkill dla startups (50 users)

### HubSpot
**Pros:**
- ✅ Best mobile app
- ✅ Great balance (features vs ease-of-use)
- ✅ Good integrations (1000+ apps)
- ✅ Moderate pricing ($90/user/mo = $4.5K/mo)

**Cons:**
- ❌ Less customization vs Salesforce
- ❌ Email-only support (no phone)

### Zoho CRM
**Pros:**
- ✅ Most affordable ($50/user/mo = $2.5K/mo)
- ✅ Fastest setup (1-2 weeks)
- ✅ Easiest to learn

**Cons:**
- ❌ Limited reporting (basic analytics)
- ❌ Slower support (48h SLA)
- ❌ Limited scalability (max 5K users)

## Rekomendacja

**Top 1: HubSpot** (best balance)

### Uzasadnienie
- Good enough features (reporting, integrations)
- Best mobile app (sales team is remote)
- Moderate pricing ($4.5K/mo affordable)
- Fast setup (2-3 weeks vs Salesforce 6-8)

**Top 2: Zoho CRM** (budget-conscious alternative)
- If budget is tight (<$3K/mo), Zoho is viable
- But lacks advanced reporting (may need upgrade later)

**Eliminated: Salesforce**
- Overkill dla 50-user startup
- Too expensive ($7.5K/mo)
- Too complex (3-month learning curve)
```

**Wartość dodana:**
- ✅ Comprehensive side-by-side view (stakeholders see all options at once)
- ✅ Clear elimination criteria (shortlist rationalized)
- ✅ Pros/Cons structured (not ad-hoc)
- ✅ Top 1-2 recommendation (clear next steps)

---

#### 2.4. GO-NO-GO-DECISION: Go/No-Go Decision Template

**Grupa:** decisions
**Domena:** multi
**Opis:** Binary decision dla launch/release/milestone

**Różnica vs Feasibility Study:**
- **Feasibility Study** = high-level, project initiation (months ahead)
- **Go/No-Go** = tactical, immediate decision (days/weeks ahead)

**Kiedy używać:**
- Sprint/release go/no-go (ship now vs delay)
- Feature flag enablement (enable for 100% users vs rollback)
- Market launch (launch in country X vs delay)
- Procurement approval (sign vendor contract vs renegotiate)

**Struktura:**
```yaml
required_meta: [id, doctype, status, version, owner, project, decision_deadline]
required_sections:
  - {id: SEC-GNG-DECISION, title: "Decision statement"}
  - {id: SEC-GNG-CRITERIA, title: "Go/No-Go criteria (checklist)"}
  - {id: SEC-GNG-STATUS, title: "Current status (vs criteria)"}
  - {id: SEC-GNG-RISKS, title: "Known risks if GO"}
  - {id: SEC-GNG-IMPACT, title: "Impact if NO-GO"}
  - {id: SEC-GNG-RECOMMENDATION, title: "Recommendation (GO/NO-GO/CONDITIONAL-GO)"}
  - {id: SEC-GNG-DECISION-FINAL, title: "Final decision + approver"}
satellites_required: [APPROVAL]
dependencies: []
outputs: {creates_artifacts: [DECISION-LOG]}
```

**Cross-References:**
```yaml
dependencies:
  - id: RELEASE-CHECKLIST
    type: requires
    reason: "Release checklist informs go/no-go criteria"

impacts:
  - id: DEPLOYMENT-GUIDE
    type: blocks
    reason: "GO decision triggers deployment"
  - id: POSTMORTEM
    type: influences
    reason: "NO-GO decision may trigger postmortem (why not ready)"
```

**Przykład użycia:**
```markdown
---
id: GO-NO-GO-SPRINT-15-RELEASE
decision_deadline: "2025-12-29 17:00"
owner: "Release Manager"
---

## Decision statement
**Should we release Sprint 15 to production on 2025-12-30?**

## Go/No-Go criteria

### MUST-HAVE (blockers if not met)
- [x] All P0 bugs fixed (3/3 done) ✅
- [x] Security scan passed (0 critical vulnerabilities) ✅
- [x] Performance tests passed (P95 latency <200ms) ✅
- [ ] UAT sign-off from Product Owner ❌ **BLOCKER**
- [x] Rollback plan documented ✅

### SHOULD-HAVE (warnings if not met)
- [x] All P1 bugs fixed (5/5 done) ✅
- [ ] Load testing completed (80% done) ⚠️ **WARNING**
- [x] Documentation updated ✅

### NICE-TO-HAVE
- [ ] All P2 bugs fixed (2/5 done – acceptable)
- [x] Monitoring dashboards ready ✅

## Current status (vs criteria)

**Status: 8/9 MUST-HAVE met** (88%)

**Blockers:**
1. ❌ **UAT sign-off missing** – PO is unavailable until 2025-12-29
   - **Mitigation:** Schedule emergency UAT session 2025-12-29 14:00

**Warnings:**
1. ⚠️ **Load testing 80% complete** – Full test suite needs 4 hours
   - **Impact:** Risk of performance issues under high load
   - **Mitigation:** Run overnight 2025-12-28 → results 2025-12-29 morning

## Known risks if GO

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| UAT finds blocker bug | Medium | High | Emergency hotfix within 24h |
| Performance degradation | Low | Medium | Rollback within 1h if P95 >300ms |
| User confusion (UI change) | Low | Low | Help docs + in-app tooltip |

## Impact if NO-GO

| Impact | Severity | Stakeholders affected |
|--------|----------|---------------------|
| Revenue loss (delayed feature) | Medium | $50K/week delayed | Sales, Finance |
| Customer disappointment | High | 5 enterprise customers waiting | Sales, Support |
| Team morale | Medium | Sprint goal not met | Engineering |
| Opportunity cost | Low | Delay next sprint planning | Product |

## Recommendation

**CONDITIONAL-GO** (proceed if UAT passes on 2025-12-29)

### Rationale
- 8/9 MUST-HAVE criteria met (88%)
- Single blocker (UAT) is resolvable przed deadline
- Load testing warning is low-risk (can monitor post-launch)
- Impact of NO-GO is high (revenue + customer disappointment)

### Conditions for GO
1. ✅ UAT completed + sign-off by 2025-12-29 16:00
2. ✅ Load testing results acceptable by 2025-12-29 10:00
3. ✅ Rollback plan tested (dry-run)

### Fallback plan (if conditions not met)
- **Partial GO:** Release to 20% users (canary deployment)
- **NO-GO:** Delay to 2026-01-06 (post-holiday window)

## Final decision

**Decision:** CONDITIONAL-GO ✅
**Approver:** Release Manager + Product Owner
**Approved:** 2025-12-29 16:30
**Conditions met:** UAT passed ✅, Load testing passed ✅
**Deployment:** Scheduled 2025-12-30 08:00 UTC
```

**Wartość dodana:**
- ✅ Crisp binary decision (GO/NO-GO/CONDITIONAL)
- ✅ Clear criteria (checklist format – easy to evaluate)
- ✅ Risk/impact balanced (not just "do we pass criteria")
- ✅ Conditional GO (flexible vs rigid binary)

---

#### 2.5. DECISION-REVERSAL: Decision Reversal Document

**Grupa:** decisions
**Domena:** multi
**Opis:** Template gdy poprzednia decyzja wymaga reversal

**Kiedy używać:**
- Architecture decision nie sprawdziła się (np. MongoDB → PostgreSQL)
- Vendor selection was wrong (np. migrate off Vendor X)
- Feature removal (deprecate feature after launch)
- Pivot (change direction after trying approach)

**Struktura:**
```yaml
required_meta: [id, doctype, status, version, owner, project, original_decision_id]
required_sections:
  - {id: SEC-DR-ORIGINAL, title: "Oryginalna decyzja (link)"}
  - {id: SEC-DR-WHY-WRONG, title: "Dlaczego decyzja była błędna"}
  - {id: SEC-DR-ROOT-CAUSE, title: "Root cause analysis"}
  - {id: SEC-DR-IMPACT, title: "Impact of original decision"}
  - {id: SEC-DR-NEW-DECISION, title: "Nowa decyzja (reversal)"}
  - {id: SEC-DR-MIGRATION, title: "Migration plan"}
  - {id: SEC-DR-LESSONS, title: "Lessons learned"}
satellites_required: [APPROVAL, EVIDENCE]
dependencies:
  - {doctype: ADR, original: true}
outputs: {creates_artifacts: [ADR, MIGRATION-PLAN]}
```

**Cross-References:**
```yaml
dependencies:
  - id: ORIGINAL-ADR
    type: requires
    reason: "Decision Reversal wymaga reference do original decision"

impacts:
  - id: NEW-ADR
    type: blocks
    reason: "Reversal tworzy nowy ADR z updated decision"
  - id: MIGRATION-PLAN
    type: blocks
    reason: "Reversal wymaga migration plan do new state"
```

**Przykład użycia:**
```markdown
---
id: DECISION-REVERSAL-ADR-042
original_decision_id: ADR-042-MONGODB-MIGRATION
reversal_date: "2025-12-27"
owner: "Tech Lead"
---

## Oryginalna decyzja

**ADR-042 (2025-10-01):** Migrate from PostgreSQL to MongoDB dla analytics module

**Original rationale:**
- Predicted 30% performance improvement dla query pattern X
- Better scalability dla document-heavy data
- PoC showed 45ms query latency (vs PostgreSQL 150ms)

**Decision status:** APPROVED
**Implemented:** 2025-11-15

## Dlaczego decyzja była błędna

### Problem 1: Performance degraded at scale
- **PoC testing:** 1M records → 45ms latency ✅
- **Production reality:** 10M+ records → 300ms latency ❌
- **Root cause:** Index strategy from PoC didn't scale

### Problem 2: Operational complexity underestimated
- **Assumed:** DevOps can manage MongoDB (team has 2 years AWS RDS experience)
- **Reality:** MongoDB cluster management is significantly harder
- **Impact:** 3 outages in 1 month (availability: 99.5% vs SLA 99.9%)

### Problem 3: Transaction support insufficient
- **Assumed:** Eventual consistency acceptable for analytics
- **Reality:** Customer reports require ACID transactions (cross-collection updates)
- **Impact:** Data inconsistencies reported by 5 customers

## Root cause analysis

### Why did PoC succeed but production fail?

**PoC limitations (missed):**
1. Dataset too small (1M vs real 10M+)
2. Query patterns simplified (single collection, real needs cross-collection joins)
3. No operational testing (cluster failover, backups)

### Why did team underestimate complexity?

1. Overconfidence from AWS RDS experience (managed PostgreSQL)
2. MongoDB's "easy to start" marketing masked operational complexity
3. Insufficient PoC duration (2 weeks vs recommended 4-6 weeks)

### Decision-making failures

1. ❌ PoC validation criteria were insufficient (scale testing omitted)
2. ❌ Operational readiness assessment was skipped
3. ❌ No pilot phase (went straight from PoC → 100% migration)

## Impact of original decision

### Quantified costs

| Impact | Cost |
|--------|------|
| Development time (migration) | 320 hours ($48K) |
| Outages (3x, 2h each) | $12K revenue loss |
| Customer escalations | 40 hours support ($6K) |
| **Total cost of wrong decision** | **$66K** |

### Non-quantified impacts
- Team morale (frustration from constant firefighting)
- Customer trust (3 outages in 1 month)
- Tech debt (rushed MongoDB implementation)

## Nowa decyzja (reversal)

**NEW DECISION:** Migrate back to PostgreSQL + optimize query patterns

### Rationale
- PostgreSQL with proper indexing achieves 80ms latency (acceptable vs 45ms target)
- Team expertise (zero learning curve)
- ACID transactions (no data consistency issues)
- Operational simplicity (AWS RDS managed)

### Trade-offs accepted
- ❌ Not hitting original 45ms latency target (now 80ms) – **acceptable** (still <100ms SLA)
- ❌ Sunk cost $66K from MongoDB experiment – **acceptable** (lesson learned)

## Migration plan

### Timeline: 4 weeks

**Week 1 (2026-01-06):**
- [ ] Create PostgreSQL schema (optimized indexes)
- [ ] Setup dual-write (MongoDB + PostgreSQL)
- [ ] Data validation scripts

**Week 2 (2026-01-13):**
- [ ] Backfill PostgreSQL from MongoDB (10M records)
- [ ] Validate data consistency
- [ ] Performance testing (verify 80ms latency)

**Week 3 (2026-01-20):**
- [ ] Switch read traffic to PostgreSQL (20% → 50% → 100%)
- [ ] Monitor performance/errors
- [ ] Keep MongoDB as backup

**Week 4 (2026-01-27):**
- [ ] Full cutover to PostgreSQL
- [ ] Decommission MongoDB cluster
- [ ] Update documentation (TDD, Runbook)

### Rollback plan
- MongoDB cluster kept live dla 2 tygodnie post-cutover
- Switch back possible within 1 hour if critical issues

## Lessons learned

### What went wrong

1. **PoC scope was insufficient**
   - Learning: Scale testing must match production (10x dataset, production query patterns)

2. **Operational readiness was skipped**
   - Learning: Always assess team's operational capability (not just tech capability)

3. **No pilot phase**
   - Learning: Never go 0→100% – always pilot critical migrations (20% → 50% → 100%)

4. **Sunk cost fallacy**
   - Learning: We delayed reversal by 1 month (cost: +$20K) because "we invested so much"
   - Better: Fail fast, reverse quickly

### What we'll do differently next time

1. ✅ Extended PoC (4-6 weeks vs 2 weeks)
2. ✅ Scale testing mandatory (10x production dataset)
3. ✅ Operational readiness assessment (team capability + runbooks)
4. ✅ Pilot phase (20% → 50% → 100% rollout)
5. ✅ Regular decision review (1 month post-implementation)

### Knowledge sharing

- [ ] Share at Engineering All-Hands (2026-01-10)
- [ ] Write blog post (external: "When MongoDB isn't the answer")
- [ ] Update PoC template (add scale testing requirements)
- [ ] Add to Anti-Patterns catalog
```

**Wartość dodana:**
- ✅ Honest retrospective (dlaczego decyzja was wrong)
- ✅ Root cause analysis (nie surface-level)
- ✅ Quantified impact (pokazuje cost of bad decisions)
- ✅ Actionable lessons (not generic "test more")
- ✅ Knowledge sharing (prevents repeating mistakes)

---

## 3. Scenariusze użycia (5 case studies)

### Scenariusz 1: Daily feature prioritization (Agile Team)

**Kontekst:** Sprint Planning – zespół ma 5 features w backlogu, capacity na 2.

**Obecny proces:**
- PM decides ad-hoc
- Rationale shared verbally w standup
- No documentation → team forgets "why" after 1 week

**Z Decision Templates:**

1. **DECISION-LOG-SPRINT15-FEATURES** (5 minut wypełnienia)
   - Pytanie: Which 2 features dla Sprint 15?
   - Opcje: Feature A, B, C, D, E
   - Decyzja: A + B
   - Rationale: Customer demand (A: 15 requests, B: 12 requests vs C: 5 requests)

2. **Benefit:**
   - ✅ Documented rationale (team understands "why")
   - ✅ Fast (5 min vs 0 min ad-hoc, ale adds clarity)
   - ✅ Searchable (future: "why did we prioritize A over C?")

---

### Scenariusz 2: Vendor selection dla CRM (Sales Team)

**Kontekst:** Sales team needs CRM – 5 vendors evaluated.

**Obecny proces:**
- Excel spreadsheet (scattered criteria)
- Email threads (lost context)
- Final decision verbal (no rationale documented)

**Z Decision Templates:**

1. **OPTION-COMPARISON-MATRIX-CRM** (2 hours)
   - Opcje: Salesforce, HubSpot, Zoho, Pipedrive, Freshsales
   - Criteria: Pricing, Features, Integrations, Support, Ease-of-use
   - Matrix: Side-by-side comparison
   - Shortlist: Salesforce, HubSpot, Zoho (eliminated Pipedrive, Freshsales)

2. **TRADE-OFF-ANALYSIS-CRM** (1 hour)
   - Weighted criteria (Pricing 30%, Features 25%, etc.)
   - Scoring: HubSpot 8.2, Salesforce 7.9, Zoho 7.1
   - Recommendation: HubSpot (best balance)

3. **ADR-CRM-SELECTION** (30 min)
   - Decision: HubSpot
   - Context: Trade-off analysis (link)
   - Consequences: $4.5K/month cost, 2-week setup

**Benefit:**
- ✅ Systematic comparison (not scattered Excel)
- ✅ Transparent scoring (stakeholders see weights)
- ✅ Auditable trail (dla future reference)

---

### Scenariusz 3: Go/No-Go dla MVP launch (Product Team)

**Kontekst:** MVP scheduled dla 2025-12-30, ale bugs still open.

**Obecny proces:**
- Stakeholder meeting (1 hour)
- Verbal decision ("let's ship despite bugs")
- No documentation → when bugs escalate post-launch, no record of "why we launched"

**Z Decision Templates:**

1. **GO-NO-GO-MVP-LAUNCH** (30 min)
   - Criteria: All P0 fixed ✅, UAT sign-off ✅, Performance tests ⚠️
   - Risks if GO: 3 P1 bugs open (medium impact)
   - Impact if NO-GO: $50K revenue loss, customer disappointment
   - Recommendation: CONDITIONAL-GO (launch with 3 P1 bugs, hotfix within 1 week)

2. **Decision:** GO ✅
   - Approver: Product Owner + CTO
   - Conditions: Hotfix plan ready, rollback tested

3. **Post-launch:**
   - 1 P1 bug escalates → customer complaint
   - PM references GO-NO-GO doc: "We knew this risk, accepted for revenue"
   - Stakeholders aligned (no blame game)

**Benefit:**
- ✅ Clear go/no-go criteria (checklist format)
- ✅ Documented risk acceptance (CYA dla PM)
- ✅ Post-launch context (dlaczego shipped despite bugs)

---

### Scenariusz 4: Pricing model change (Business Team)

**Kontekst:** Startup rozważa zmianę pricing: per-user → per-feature.

**Obecny proces:**
- Business Case (za ciężki dla pricing change)
- Albo Slack discussion (za lekki, no structure)

**Z Decision Templates:**

1. **TRADE-OFF-ANALYSIS-PRICING** (2 hours)
   - Criteria: Revenue impact, Customer churn, Implementation cost, Competitive position
   - Opcje: Per-user, Per-feature, Hybrid
   - Scoring: Hybrid 8.5, Per-feature 7.2, Per-user (current) 6.8
   - Recommendation: Hybrid pricing

2. **Key trade-offs:**
   - Choosing Hybrid → Higher revenue (+$200K/year) but Higher churn risk (+5%)
   - Mitigation: Grandfather existing customers (keep per-user)

3. **ADR-PRICING-MODEL** (30 min)
   - Decision: Hybrid pricing dla new customers
   - Context: Trade-off analysis
   - Consequences: Billing logic complexity, A/B testing required

**Benefit:**
- ✅ Structured trade-off analysis (revenue vs churn vs implementation)
- ✅ Clear recommendation (not "let's try and see")
- ✅ Risk mitigation (grandfather existing customers)

---

### Scenariusz 5: Decision reversal – MongoDB migration (Tech Team)

**Kontekst:** Team migrated to MongoDB (ADR-042), but performance degraded.

**Obecny proces:**
- Create new ADR ("migrate back to PostgreSQL")
- But no structured retrospective "dlaczego original decision was wrong"

**Z Decision Templates:**

1. **DECISION-REVERSAL-ADR-042** (3 hours)
   - Original decision: MongoDB dla analytics
   - Why wrong: Performance degraded at scale (300ms vs 45ms PoC)
   - Root cause: PoC dataset too small, operational complexity underestimated
   - Impact: $66K cost (dev time + outages + support)
   - Lessons: Extended PoC, scale testing, pilot phase

2. **NEW-ADR-055:** Migrate back to PostgreSQL
   - Context: Decision Reversal doc
   - Decision: PostgreSQL with optimized indexes
   - Consequences: 80ms latency (acceptable vs 45ms target)

3. **Knowledge sharing:**
   - Engineering All-Hands presentation
   - Blog post: "When MongoDB isn't the answer"
   - Updated PoC template (add scale testing requirements)

**Benefit:**
- ✅ Honest retrospective (not blaming, learning)
- ✅ Quantified cost ($66K) – shows value of better decisions
- ✅ Actionable lessons (extended PoC, scale testing, pilot)
- ✅ Knowledge retention (prevents repeating mistake)

---

## 4. Integracja z istniejącymi 148 szablonami

### 4.1. ADR (Architecture Decision Records) – Complementary

**ADR** pozostaje dla strategic/architectural decisions.

**Nowe templates** complement ADR:

| Template | Scope | Relation to ADR |
|----------|-------|-----------------|
| **DECISION-LOG** | Tactical daily decisions | Lighter alternative (nie wszystko needs ADR) |
| **TRADE-OFF-ANALYSIS** | Quantitative trade-offs | Feeds into ADR context |
| **OPTION-COMPARISON** | Qualitative comparison | Feeds into ADR options |
| **GO-NO-GO** | Binary launch decisions | May reference ADR (if technical decision) |
| **DECISION-REVERSAL** | Reversing ADR | Updates original ADR with reversal |

**Integration example:**

```yaml
# ADR-042 (original)
id: ADR-042-MONGODB-MIGRATION
status: superseded  # Marked after reversal
superseded_by: ADR-055-POSTGRESQL-OPTIMIZATION
reversal_doc: DECISION-REVERSAL-ADR-042

# ADR-055 (new)
id: ADR-055-POSTGRESQL-OPTIMIZATION
status: approved
supersedes: ADR-042
reversal_context: DECISION-REVERSAL-ADR-042
```

### 4.2. FEASIBILITY-STUDY – Complementary

**FEASIBILITY-STUDY** = high-level, project initiation
**GO-NO-GO-DECISION** = tactical, immediate decision

**Relationship:**
- Feasibility Study feeds into GO-NO-GO dla project start
- GO-NO-GO używany dla sprint/release/feature decisions

**Example:**
```yaml
# FEASIBILITY-STUDY-PROJECT-X
go_no_go_checkpoints:
  - GATE-GO_NO_GO (project initiation)
  - GO-NO-GO-SPRINT-PILOT (after pilot sprint)
  - GO-NO-GO-MVP-LAUNCH (before production launch)
```

### 4.3. BUSINESS-CASE – Complementary

**BUSINESS-CASE** = high-level ROI justification
**TRADE-OFF-ANALYSIS** = detailed multi-criteria decision

**Relationship:**
- Business Case may reference Trade-off Analysis dla detailed comparison
- Trade-off Analysis używany dla specific decisions (vendor, pricing, architecture)

**Example:**
```yaml
# BUSINESS-CASE-CRM-IMPLEMENTATION
supporting_analyses:
  - TRADE-OFF-ANALYSIS-CRM-VENDOR (vendor selection)
  - OPTION-COMPARISON-MATRIX-CRM (detailed comparison)
```

### 4.4. Sprint Templates – Integration

**SPRINT-CORE, SPRINT-DISCOVERY** ← `DECISION-LOG`

**Integration:**
```yaml
# SPRINT-CORE artifacts
decision_logs:
  - DECISION-LOG-SPRINT15-FEATURES (feature prioritization)
  - DECISION-LOG-SPRINT15-TECH-DEBT (tech debt vs features)

# SPRINT-DISCOVERY artifacts
research_decisions:
  - TRADE-OFF-ANALYSIS-ARCHITECTURE (architecture options)
  - GO-NO-GO-POC-RESULTS (proceed vs pivot)
```

### 4.5. Dependency Graph – Nowe połączenia

**Nowe węzły:** +5 document types (DECISION-LOG, TRADE-OFF-ANALYSIS, OPTION-COMPARISON-MATRIX, GO-NO-GO-DECISION, DECISION-REVERSAL)

**Szacowane nowe połączenia:** ~80-100

**Przykładowe ścieżki:**
```
OPTION-COMPARISON → TRADE-OFF-ANALYSIS → ADR → TDD
GO-NO-GO → DEPLOYMENT-GUIDE → RELEASE-NOTES
DECISION-REVERSAL → NEW-ADR → MIGRATION-PLAN
POC-DOC → TRADE-OFF-ANALYSIS → ADR
```

---

## 5. Metryki sukcesu

### 5.1. Decision documentation coverage

**M1: Decision Documentation Rate**
- **Definicja:** % decyzji które są documented (any decision template)
- **Target:** >70% (vs current ~20% ADR-only)
- **Measurement:** Count decision docs vs estimated decision events

**M2: Lightweight Decision Adoption**
- **Definicja:** % daily decisions using DECISION-LOG (vs heavy ADR)
- **Target:** >60% tactical decisions use DECISION-LOG
- **Measurement:** DECISION-LOG count vs ADR count

**M3: Decision Template Mix**
- **Definicja:** Distribution of decision template usage
- **Target:** Balanced mix (not 95% ADR, 5% others)
- **Measurement:** Template usage breakdown

**Target distribution:**
- DECISION-LOG: 50% (daily tactical)
- TRADE-OFF-ANALYSIS: 20% (complex decisions)
- OPTION-COMPARISON: 15% (vendor/tool selection)
- GO-NO-GO: 10% (launch decisions)
- DECISION-REVERSAL: 5% (reversals)

### 5.2. Decision quality

**M4: Reversal Rate**
- **Definicja:** % decyzji które require reversal w <6 miesięcy
- **Target:** <10% (vs current ~20% gut-feeling decisions)
- **Measurement:** DECISION-REVERSAL count vs total decisions

**M5: Stakeholder Alignment Score**
- **Definicja:** Survey score "Do you understand decision rationale?" (1-5)
- **Target:** >4.0 (vs current ~2.8)
- **Measurement:** Quarterly survey

**M6: Time to Decision**
- **Definicja:** Średni czas od decision trigger do documented decision
- **Target:** <7 dni dla tactical, <30 dni dla strategic
- **Measurement:** Timestamp tracking

### 5.3. Knowledge retention

**M7: Decision Searchability**
- **Definicja:** % team members who can find past decision rationale
- **Target:** >80% (vs current ~30%)
- **Measurement:** Quarterly search test

**M8: Lessons Learned Reuse**
- **Definicja:** % DECISION-REVERSAL lessons incorporated into future decisions
- **Target:** >50%
- **Measurement:** DECISION-REVERSAL → updated templates/processes

---

## 6. Podsumowanie

### Kluczowe korzyści

1. **Decision coverage:** 70% decyzji documented (vs 20% ADR-only)
2. **Lightweight options:** DECISION-LOG dla daily decisions (5 min vs 2h ADR)
3. **Structured trade-offs:** Quantitative scoring (not subjective opinions)
4. **Clear comparisons:** Side-by-side matrices (not scattered Excel)
5. **Honest retrospectives:** DECISION-REVERSAL captures lessons learned
6. **Knowledge retention:** Searchable decision trail (not lost in Slack)

### Wartość dodana

| Obszar | Obecny stan | Z Decision Templates |
|--------|-------------|---------------------|
| **Decision documentation** | ~20% (ADR only) | >70% (all types) |
| **Time to document** | 1-2h (ADR) | 5 min (DECISION-LOG) dla tactical |
| **Trade-off clarity** | Subjective | Quantitative (weighted scoring) |
| **Comparison quality** | Scattered Excel | Structured matrix |
| **Reversal rate** | ~20% (poor decisions) | <10% (better analysis) |
| **Stakeholder alignment** | ~2.8/5 | >4.0/5 (clear rationale) |

---

**Koniec Propozycji 3**
