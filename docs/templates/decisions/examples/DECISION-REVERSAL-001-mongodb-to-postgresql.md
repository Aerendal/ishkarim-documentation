# DECISION-REVERSAL-001: MongoDB → PostgreSQL Migration (Analytics Module)

---
**Meta (WYMAGANE):**
```yaml
id: DECISION-REVERSAL-ADR-042-MONGODB
doctype: DECISION-REVERSAL
status: approved
version: "1.0"
owner: "Piotr Nowak (Tech Lead)"
project: "Ishkarim - Analytics Module"
original_decision_id: ADR-042-MONGODB-MIGRATION
original_decision_date: "2025-10-01"
reversal_date: "2025-12-27"
reversal_reason: "Performance degraded at production scale (300ms vs 45ms PoC), operational complexity underestimated, 3 outages in 1 month"
created: "2025-12-27"
updated: "2025-12-29"
```

**Cross-References:**
```yaml
dependencies:
  - id: ADR-042-MONGODB-MIGRATION
    type: requires
    reason: "Original decision being reversed - context essential"
  - id: EVIDENCE-MONGODB-PRODUCTION-METRICS
    type: requires
    reason: "Production data showing performance degradation"
  - id: EVIDENCE-INCIDENT-REPORTS-DEC2025
    type: requires
    reason: "3 outages documented (Nov 15, Nov 28, Dec 10)"
  - id: POC-042-MONGODB-BENCHMARK
    type: influences
    reason: "Original PoC data (misleading - dataset too small)"

impacts:
  - id: ADR-055-POSTGRESQL-OPTIMIZATION
    type: blocks
    reason: "Reversal creates new ADR with updated decision"
  - id: MIGRATION-PLAN-MONGODB-TO-PG
    type: blocks
    reason: "4-week migration plan required for reversal"
  - id: POSTMORTEM-MONGODB-FAILURE
    type: blocks
    reason: "Incident postmortem documenting what went wrong"
  - id: POC-TEMPLATE-UPDATE
    type: influences
    reason: "Lessons learned → update PoC template (add scale testing requirements)"
```

**Wymagane dokumenty satelitarne:**
- ✅ APPROVAL-REVERSAL-001: CTO + Engineering Manager approval dla reversal (significant cost)
- ✅ EVIDENCE-MONGODB-PROD-METRICS: Production latency data (P95, P99), outage reports
- ✅ EVIDENCE-POSTGRESQL-BENCHMARK: New PostgreSQL benchmark (validates reversal choice)
- ✅ EVIDENCE-COST-ANALYSIS: Total cost of MongoDB experiment ($82K calculated)

---

## SEC-DR-ORIGINAL: Oryginalna decyzja (link)

**Original decision ID:** ADR-042-MONGODB-MIGRATION

**Original decision document:** `/docs/engineering/decisions/ADR-042-mongodb-analytics-migration.md`

**Decision date:** October 1, 2025 (approved after 2-week PoC)

**Decision owner (original):** Piotr Nowak (Tech Lead) + Backend Team

**Implementation timeline:**
- **Decision approved:** 2025-10-01
- **Development started:** 2025-10-08 (Sprint 19)
- **Implementation completed:** 2025-11-15 (Sprint 21, 5 weeks)
- **Production rollout:** 2025-11-15 (100% cutover - big bang migration)
- **Time in production:** 6 weeks (Nov 15 - Dec 27) before reversal decision
- **Total experiment duration:** 12 weeks (PoC → Production → Reversal)

---

### What was decided

**Original decision statement:**
Migrate analytics module from PostgreSQL to MongoDB dla improved query performance on document-heavy analytics workloads. Target: 3× performance improvement (150ms → 45ms average query latency).

**Selected option:** MongoDB 6.0 (self-hosted cluster na AWS EC2)

**Architecture:**
- **Deployment:** 3-node MongoDB replica set (m5.large × 3, us-east-1)
- **Data model:** Document-oriented (analytics events jako nested documents)
- **Query pattern:** Aggregation pipelines dla complex analytics queries
- **Migration:** Big bang cutover (PostgreSQL → MongoDB, 1-day downtime)

**Alternatives rejected (originally):**

1. **PostgreSQL with optimized indexes** - rejected because:
   - "Benchmarks showed 150ms latency (vs MongoDB 45ms)"
   - "Document queries require complex JOINs (6-8 tables) - slow"
   - "JSON columns in PostgreSQL slower than native MongoDB documents"

2. **Elasticsearch** - rejected because:
   - "Overkill - need database, not search engine"
   - "Operational complexity similar to MongoDB, no clear advantage"
   - "Team has zero Elasticsearch experience"

3. **Stay with PostgreSQL (no migration)** - rejected because:
   - "Performance unacceptable (150ms, target: <100ms)"
   - "Scaling PostgreSQL vertically expensive (larger instances = $$$)"
   - "Customer complaints about slow analytics dashboard"

---

### Original rationale

**Why MongoDB seemed like a good decision (October 2025):**

**1. PoC showed dramatic performance improvement** ✅
- **PoC benchmark (Sept 20-30):** MongoDB 45ms avg latency vs PostgreSQL 150ms
- **PoC dataset:** 1 million analytics events (Sept data only)
- **PoC queries:** 5 common analytics queries (user growth, feature usage, conversion funnels)
- **Conclusion:** "MongoDB is **3.3× faster** - clear winner" 🎉

**2. Document model seemed natural fit** ✅
- Analytics events = hierarchical structure (user → session → events → properties)
- PostgreSQL = 6-8 table JOINs required (complex queries, slow)
- MongoDB = single collection, nested documents (simple queries, fast)
- **Conclusion:** "Document model matches our data structure perfectly" 👍

**3. Scalability story compelling** ✅
- MongoDB horizontal sharding (add nodes = linear scale)
- PostgreSQL vertical scaling (bigger instance = expensive, ceiling at 64 cores)
- Growth projection: 1M events/month → 10M events/month by Q2 2026
- **Conclusion:** "MongoDB scales better dla future growth" 📈

**4. Industry adoption validated choice** ✅
- Company X (similar SaaS) using MongoDB dla analytics - "works great"
- MongoDB marketing: "Built for scale, flexible schema, developer-friendly"
- Community: Large ecosystem, active forums, good documentation
- **Conclusion:** "Industry-proven solution, low risk" ✅

---

### Key assumptions (that turned out wrong)

**Assumption 1: PoC dataset representative of production** ❌
- **Assumed:** 1M records sufficient test (Sept data)
- **Reality:** Production = 12M+ records (Jan-Dec 2025 data)
- **Impact:** Performance degraded dramatically at scale (45ms → 300ms)

**Assumption 2: Query patterns stable** ❌
- **Assumed:** 5 common queries cover 90% of usage
- **Reality:** 20+ unique query patterns (ad-hoc analytics, custom dashboards)
- **Impact:** Indexing strategy from PoC insufficient dla diverse queries

**Assumption 3: Operational complexity manageable** ❌
- **Assumed:** "Team can manage MongoDB" (2 years AWS RDS experience)
- **Reality:** MongoDB cluster management significantly harder (replica sets, sharding, backups, monitoring)
- **Impact:** 3 outages in 1 month (99.5% uptime vs SLA 99.9%)

**Assumption 4: Document model advantages persist at scale** ❌
- **Assumed:** Nested documents always faster (avoid JOINs)
- **Reality:** Large nested documents = slower reads (10KB+ docs), index bloat
- **Impact:** Query performance worse than PostgreSQL at production scale

**Assumption 5: Migration downtime acceptable (1 day)** ❌
- **Assumed:** 24-hour downtime acceptable (weekend maintenance)
- **Reality:** Migration took 36 hours (data corruption issues), customer complaints
- **Impact:** SLA breach (99.9% monthly uptime violated), customer escalations

---

### Expected outcomes (vs reality)

| Outcome | Expected (October 2025) | Reality (December 2025) | Delta |
|---------|------------------------|------------------------|-------|
| **Avg query latency** | 45ms (PoC result) | 280ms (P50 production) | **6.2× WORSE** ❌ |
| **P95 latency** | 80ms (PoC result) | 650ms (production) | **8.1× WORSE** ❌ |
| **P99 latency** | 150ms (PoC result) | 1,200ms (production) | **8× WORSE** ❌ |
| **Uptime SLA** | 99.9% (standard) | 99.5% (actual) | **-0.4%** (3 outages) ❌ |
| **Operational overhead** | 5h/month (assumed) | 25h/month (actual) | **5× WORSE** ❌ |
| **Cost** | $450/month (EC2 instances) | $850/month (instances + engineer time) | **1.9× WORSE** ❌ |
| **Team satisfaction** | High (new tech!) | Low (constant firefighting) | **Morale hit** ❌ |

**Summary:** **0/7 outcomes met expectations** - complete failure 💥

---

## SEC-DR-WHY-WRONG: Dlaczego decyzja była błędna

**Summary:**
MongoDB migration was **catastrophic failure**. Performance **degraded 6-8× at production scale** (280ms vs 45ms PoC), **3 outages in 1 month** (operational complexity underestimated), **25h/month firefighting** vs 5h expected. PoC was **fundamentally flawed** - dataset too small (1M vs 12M), query patterns simplified, operational testing skipped. Cost of experiment: **$82K** (wasted development + incidents + opportunity cost).

---

### Problem 1: Performance degraded dramatically at production scale

#### What went wrong

**PoC (1M records):** MongoDB avg latency = 45ms ✅ Excellent!
**Production (12M records):** MongoDB avg latency = 280ms ❌ **6.2× WORSE**

**Expected:** Linear scaling (1M → 12M = 12× data, but latency stays ~45-60ms due to indexing)
**Reality:** Superlinear degradation (latency increased 6× faster than data growth)

#### Expected vs Reality

| Metric | PoC (1M records) | Expected (12M) | Actual (12M) | Delta |
|--------|-----------------|---------------|--------------|-------|
| **P50 latency** | 45ms | 50-60ms | **280ms** | **6.2× worse** |
| **P95 latency** | 80ms | 100-120ms | **650ms** | **8.1× worse** |
| **P99 latency** | 150ms | 180-200ms | **1,200ms** | **8× worse** |
| **Index size** | 250 MB | 3 GB (linear) | **8 GB** | **2.7× larger** |
| **Working set** | 800 MB (fits RAM) | 9.6 GB | **15 GB** | **Does NOT fit RAM (12GB)** |

#### Evidence

**EVIDENCE-MONGODB-PROD-METRICS (CloudWatch data):**
- **Week 1 (Nov 15-22):** P50 = 120ms (acceptable, fresh indexes)
- **Week 2 (Nov 23-30):** P50 = 180ms (degrading, index bloat)
- **Week 3 (Dec 1-8):** P50 = 250ms (poor, working set > RAM)
- **Week 4 (Dec 9-16):** P50 = 280ms (unacceptable, breach SLA <200ms)
- **Week 5-6 (Dec 17-27):** P50 = 280-320ms (stable but terrible)

**Customer impact:**
- Analytics dashboard load time: 8-12 seconds (vs 3 seconds PostgreSQL)
- Customer complaints: 15 tickets (Nov-Dec) - "dashboard too slow"
- Executive dashboard: CEO complained "can't get real-time insights"

#### Root cause

**1. Working set exceeded RAM (15GB working set > 12GB RAM)**
- MongoDB m5.large instances: 16GB RAM total, ~12GB available dla working set
- Working set = active indexes + frequently accessed documents
- When working set > RAM → disk I/O → latency spike
- **Fix attempted:** Upgrade to m5.xlarge (32GB RAM) = $900/month (2× cost) ❌ Rejected (too expensive)

**2. Index bloat (compound indexes inefficient)**
- PoC: 3 simple indexes (user_id, event_type, timestamp)
- Production: 12 compound indexes (cover diverse query patterns)
- Total index size: 8GB (vs 3GB expected) - some indexes 500MB+ each
- Index maintenance overhead: Writes 3× slower (update all indexes)

**3. Large nested documents (10KB+ average)**
- PoC: Simple documents (1-2 KB, minimal nesting)
- Production: Complex nested structures (user properties, session metadata, event payloads) = 10KB+ avg
- MongoDB reads entire document (not just queried fields) = wasted I/O
- **PostgreSQL advantage:** Column-based reads (SELECT specific columns only)

**4. Aggregation pipeline inefficiency at scale**
- MongoDB aggregation pipelines = multi-stage processing (match → group → sort → project)
- Each stage = full collection scan or index scan (no query planner optimization)
- PostgreSQL query planner = smarter (push-down filters, optimize JOIN order)
- At 12M records, aggregation pipelines 5-10× slower than PostgreSQL JOINs

---

### Problem 2: Operational complexity severely underestimated

#### What went wrong

**Assumption:** "Team can manage MongoDB" (AWS RDS PostgreSQL experience = managed service)
**Reality:** MongoDB self-hosted = **25h/month firefighting** vs 5h expected (5× worse)

**3 outages in 1 month** (Nov-Dec 2025):
- **Outage 1 (Nov 15, 2h):** Replica set primary election failed (network partition)
- **Outage 2 (Nov 28, 3h):** Disk full on secondary node (backup logs filled disk)
- **Outage 3 (Dec 10, 1.5h):** Index rebuild blocked writes (foreground index build)

**Availability:** 99.5% (SLA: 99.9%) = **-0.4% breach** = customer SLA violation

#### Expected vs Reality

| Operational aspect | Expected (PoC assumption) | Reality (Production) | Delta |
|-------------------|-------------------------|---------------------|-------|
| **Setup time** | 2 days (spin up EC2, install MongoDB) | **5 days** (replica set config, monitoring, backups) | **2.5× worse** |
| **Monthly maintenance** | 5 hours (patching, monitoring) | **25 hours** (troubleshooting, on-call, incidents) | **5× worse** |
| **On-call burden** | Low (stable database) | **High** (PagerDuty alerts 3×/week) | **Unacceptable** |
| **Expertise required** | Moderate (docs sufficient) | **High** (MongoDB DBA knowledge, tuning, sharding) | **Skills gap** |
| **Backup complexity** | Simple (mongodump) | **Complex** (point-in-time recovery, replica lag, consistency) | **Error-prone** |

#### Evidence

**EVIDENCE-INCIDENT-REPORTS-DEC2025:**

**Outage 1: Nov 15, 2025 (2 hours)**
- **Trigger:** Network partition (AWS AZ connectivity issue)
- **Impact:** Replica set primary election failed → no writes dla 2 hours
- **Root cause:** Insufficient oplog size (election timeout too short)
- **Resolution:** Manual intervention (force primary election), config tuning
- **Customer impact:** 50 users unable to view analytics dashboard
- **SLA impact:** 99.72% monthly uptime (breach 99.9% target)

**Outage 2: Nov 28, 2025 (3 hours)**
- **Trigger:** Disk full on secondary node (backup logs accumulated)
- **Impact:** Secondary node offline → replica set degraded → performance degraded
- **Root cause:** Log rotation misconfigured (7-day retention → disk full in 10 days)
- **Resolution:** Emergency disk expansion (60GB → 120GB), log cleanup
- **Customer impact:** 100+ users experienced slow dashboard (3× latency)
- **SLA impact:** 99.58% monthly uptime (cumulative breach)

**Outage 3: Dec 10, 2025 (1.5 hours)**
- **Trigger:** Foreground index build (admin ran `createIndex()` without `background: true`)
- **Impact:** All writes blocked during index build (1.5 hours dla 8GB index)
- **Root cause:** Operational error (lack of MongoDB expertise)
- **Resolution:** Kill index build, rebuild in background (overnight)
- **Customer impact:** Analytics events not written (30K events lost, needed backfill)
- **SLA impact:** 99.48% monthly uptime (severe breach)

**Team impact:**
- DevOps engineer (Katarzyna): 40 hours unplanned work in November (MongoDB firefighting)
- Backend engineer (Piotr): 30 hours incident response + troubleshooting
- On-call rotation: 3 engineers burned out (constant PagerDuty alerts)
- **Morale:** Team survey (Dec 15): "MongoDB was a mistake" - 6/8 engineers agree

---

### Problem 3: Transaction/consistency requirements underestimated

#### What went wrong

**Assumption:** "Eventual consistency acceptable dla analytics" (not transactional workload)
**Reality:** Customer reports require **ACID transactions** (cross-collection updates, referential integrity)

#### Examples of consistency issues

**Issue 1: User deletion cascades** (Nov 22, 2025)
- **Requirement:** When user deletes account → delete all analytics events (GDPR)
- **PostgreSQL:** `ON DELETE CASCADE` (foreign key) = atomic, guaranteed
- **MongoDB:** Manual cascade (find all events, delete batch) = **not atomic**
- **Bug:** User deleted, but 150 events remained (batch delete failed midway)
- **Impact:** GDPR violation (user data retained after deletion request)
- **Resolution:** Manual cleanup script (find orphaned events, delete) - 4 hours work

**Issue 2: Report generation race condition** (Dec 5, 2025)
- **Requirement:** Generate monthly report (aggregate events, write to reports collection)
- **PostgreSQL:** Transaction (BEGIN → aggregate → INSERT → COMMIT) = consistent
- **MongoDB:** No multi-document transactions (MongoDB 4.0+ has, but performance penalty)
- **Bug:** Report generated with incomplete data (concurrent writes during aggregation)
- **Impact:** 5 customers received incorrect monthly reports (data off by 10-15%)
- **Resolution:** Re-generate reports (manual fix), implement pessimistic locking (slow)

**Issue 3: Referential integrity violations** (ongoing)
- **Example:** Event references user_id, but user deleted → orphaned event
- **PostgreSQL:** Foreign key constraint = prevented at write time (error if user doesn't exist)
- **MongoDB:** No foreign keys = orphaned documents (discovered later)
- **Impact:** Data integrity issues (analytics queries include deleted users)
- **Resolution:** Weekly cleanup job (find orphans, delete) - ongoing maintenance burden

---

### Which assumptions were wrong?

**Original assumptions vs Reality:**

| Original assumption | What we believed | Reality | Impact |
|---------------------|-----------------|---------|--------|
| **PoC dataset representative** | 1M records = sufficient test | Production = 12M+ records, performance 6× worse | Performance disaster |
| **Query patterns stable** | 5 queries cover 90% usage | 20+ diverse queries, ad-hoc dashboards | Index strategy failed |
| **Operational simplicity** | "We can manage MongoDB" | 3 outages, 25h/month firefighting | Availability breach |
| **Document model advantage** | Nested docs always faster | Large docs (10KB+) slower than JOIN | Performance regression |
| **Eventual consistency OK** | Analytics = non-transactional | Customer reports need ACID | GDPR violation |
| **Scaling headroom** | MongoDB scales better | Never reached scale (failed at 12M, not 100M) | Premature optimization |
| **Team expertise** | "MongoDB is easy" | Requires DBA skills, tuning expertise | Skills gap |
| **Migration risk low** | 1-day downtime acceptable | 36-hour migration, data corruption | Customer complaints |

**Summary:** **8/8 assumptions wrong** - fundamental misunderstanding of requirements and MongoDB characteristics 💥

---

## SEC-DR-ROOT-CAUSE: Root cause analysis

**Primary root cause:**
**PoC was fundamentally flawed** - dataset too small (1M vs 12M), query patterns simplified, operational testing skipped, production environment not simulated. Team fell victim to **confirmation bias** (wanted MongoDB to work, ignored warning signs).

---

### Why did PoC succeed but production fail?

**PoC limitations (critical gaps missed):**

**1. Dataset too small (1M vs 12M records)** ❌
- **PoC:** September data only (1M events, 30 days)
- **Production:** Jan-Dec 2025 data (12M events, 365 days)
- **Impact:** Working set fit in RAM for PoC (800MB), but NOT for production (15GB > 12GB RAM)
- **Lesson:** PoC should test **10× target data volume** (not 1:1 with current data)

**2. Query patterns oversimplified** ❌
- **PoC:** 5 hardcoded queries (user growth, feature usage, conversion funnels)
- **Production:** 20+ unique queries (ad-hoc analytics, custom dashboards, CEO reports)
- **Impact:** PoC indexes optimized dla 5 queries, production needs 12 indexes (bloat)
- **Lesson:** PoC should include **worst-case queries** + ad-hoc query simulation

**3. No operational testing (cluster management, failover, backups)** ❌
- **PoC:** Single-node MongoDB (no replica set, no production config)
- **Production:** 3-node replica set (complex: primary election, oplog, lag)
- **Impact:** Operational issues never tested (3 outages in production)
- **Lesson:** PoC must test **production-like environment** (HA, backups, monitoring)

**4. No load testing (concurrent users, write-heavy workloads)** ❌
- **PoC:** Single-threaded queries (no concurrency)
- **Production:** 50+ concurrent users (analytics dashboard, reports)
- **Impact:** Lock contention, index contention, write amplification (3× slower writes)
- **Lesson:** PoC must include **load testing** (concurrent reads/writes, realistic traffic)

**5. No long-term testing (index bloat, performance degradation over time)** ❌
- **PoC:** 2 weeks duration (fresh database, fresh indexes)
- **Production:** 6 weeks → performance degraded weekly (index bloat, fragmentation)
- **Impact:** Week 1 OK (120ms), Week 6 terrible (280ms)
- **Lesson:** PoC must run **4-6 weeks minimum** (observe degradation over time)

---

### Why did team underestimate complexity?

**Contributing factors:**

**1. Overconfidence from AWS RDS experience** ❌
- **Assumption:** "We manage PostgreSQL on RDS (managed service) = we can manage MongoDB"
- **Reality:** RDS = AWS manages ops (backups, HA, monitoring), MongoDB self-hosted = we manage everything
- **Cognitive bias:** **Dunning-Kruger effect** (overestimated competence with new technology)

**2. MongoDB marketing obscured operational complexity** ❌
- **Marketing message:** "Developer-friendly, flexible schema, easy to scale"
- **Reality:** Easy to start (install, insert docs), hard to operate (replica sets, sharding, performance tuning)
- **Bias:** **Availability heuristic** (remembered marketing, ignored operational war stories)

**3. Insufficient PoC duration (2 weeks vs recommended 4-6 weeks)** ❌
- **Pressure:** CEO wanted quick decision (Q4 performance issues escalating)
- **Impact:** Rushed PoC = skipped operational testing, scale testing, long-term testing
- **Bias:** **Time pressure** → shortcuts → flawed data → bad decision

**4. Confirmation bias (wanted MongoDB to work)** ❌
- **Context:** Team excited about new technology (MongoDB = "modern", PostgreSQL = "boring")
- **Bias:** Ignored warning signs (working set > RAM concern, operational complexity)
- **Impact:** Rose-colored glasses = rationalized red flags away

---

### Decision-making failures

**What went wrong in decision process:**

**1. ❌ PoC validation criteria were insufficient**
- **What we did:** Tested 5 queries, 1M records, 2 weeks
- **Should have done:**
  - Test 10× production data (12M records minimum)
  - Test worst-case queries (ad-hoc, complex aggregations)
  - Test operational scenarios (failover, backup/restore, disk full)
  - Run 4-6 weeks (observe performance over time)
  - Load testing (50+ concurrent users)

**2. ❌ Operational readiness assessment was skipped**
- **What we did:** Assumed "team can manage MongoDB" (no validation)
- **Should have done:**
  - Skills assessment (does team have MongoDB DBA expertise? NO)
  - Operational runbook review (do we have playbooks dla common issues? NO)
  - On-call burden estimation (how many incidents expected? UNKNOWN)
  - Hire MongoDB consultant dla production setup ($5K = would've saved $82K)

**3. ❌ No pilot phase (went straight from PoC → 100% migration)**
- **What we did:** Big bang cutover (PostgreSQL → MongoDB, 100% traffic Day 1)
- **Should have done:**
  - Pilot phase: 10% traffic → 50% → 100% (gradual rollout)
  - Dual-write period: Write to both PostgreSQL + MongoDB (2 weeks safety net)
  - Easy rollback: Keep PostgreSQL live dla 2 weeks (instant rollback if issues)

**4. ❌ Ignored early warning signs (confirmation bias)**
- **Warning sign 1 (PoC):** Working set = 800MB (close to instance RAM) → "it's fine" ❌
- **Warning sign 2 (Week 1):** Latency 120ms (vs PoC 45ms, 2.7× worse) → "it will improve" ❌
- **Warning sign 3 (Week 2):** First outage (replica election) → "one-time issue" ❌
- **Should have:** Triggered reversal evaluation after Week 1 (early pivot = lower cost)

---

### Could this have been prevented?

**YES - multiple decision gates were missed:**

**Gate 1: Extended PoC (4-6 weeks, 10× data)** ✅ Would have caught
- Performance degradation at scale (working set > RAM)
- Index bloat issues (12 indexes vs 3)
- Query pattern diversity (20+ queries vs 5)
- **Outcome:** Would have rejected MongoDB in October (saved $82K + 3 months)

**Gate 2: Operational readiness review** ✅ Would have caught
- Team skills gap (MongoDB DBA expertise missing)
- On-call burden (underestimated 5× → would hire consultant)
- HA complexity (replica sets, failover, backups)
- **Outcome:** Would have hired MongoDB consultant ($5K) or rejected migration

**Gate 3: Pilot phase (10% → 50% → 100%)** ✅ Would have limited blast radius
- Week 1 production: Latency 120ms (10% traffic) → HOLD rollout
- Investigate root cause (working set > RAM) → upgrade instances or revert
- **Outcome:** Would have reverted in Week 1 (cost: $15K vs $82K actual)

---

### Red flags that were missed

**Early warning signs (in hindsight):**

**🚩 Red flag 1: PoC working set = 800MB (close to 12GB RAM limit)**
- **Date:** September 25, 2025 (PoC Week 2)
- **Signal:** Working set = 800MB dla 1M records → 9.6GB dla 12M (projected)
- **Action taken:** Dismissed ("it's fine, we have 12GB")
- **Should have:** Flagged concern, tested with 10M records (validate projection)

**🚩 Red flag 2: Company X reference call revealed "operational challenges"**
- **Date:** October 5, 2025 (pre-decision)
- **Signal:** Company X mentioned "MongoDB requires dedicated DBA, on-call burden"
- **Action taken:** Ignored ("we're different, smaller scale")
- **Should have:** Probed deeper (what incidents? how often? mitigation?)

**🚩 Red flag 3: Week 1 production latency = 120ms (2.7× worse than PoC)**
- **Date:** November 22, 2025 (Week 1 post-launch)
- **Signal:** P50 latency degraded from 45ms (PoC) to 120ms (production)
- **Action taken:** "Wait and see, maybe it improves as caches warm up"
- **Should have:** STOP - investigate root cause, consider rollback

**🚩 Red flag 4: First outage (Nov 15, 2h downtime)**
- **Date:** November 15, 2025 (Launch day!)
- **Signal:** Replica election failed → 2h downtime → SLA breach
- **Action taken:** "One-time network issue, won't repeat"
- **Should have:** Pause rollout, evaluate operational readiness, consider reversal

---

### When should we have reversed?

**Optimal reversal window:** **Week 2 (Nov 22-29)** = cost $15K (vs $82K actual)

**Decision timeline:**
- **Nov 15 (Day 1):** Outage 1 → 🚩 Red flag, but "give it time"
- **Nov 22 (Week 1):** Latency 120ms → 🚩 Red flag, should have triggered review
- **Nov 28 (Week 2):** Outage 2 → 🚩🚩 Critical - should have REVERSED
- **Dec 10 (Week 4):** Outage 3 → 🚩🚩🚩 Three strikes - definitely reverse
- **Dec 27 (Week 6):** Reversal decision finally made

**Sunk cost fallacy delayed reversal:**
- Nov 22: "We invested 5 weeks development, let's give it more time" ❌
- Nov 28: "We already migrated, reverting = admitting failure" ❌
- Dec 10: "Maybe next outage won't happen" ❌
- **Cost of delay:** $20K additional (Week 3-6 incidents + opportunity cost)
- **Learning:** **Fail fast, reverse quickly** - sunk cost is sunk, don't throw good money after bad

---

## SEC-DR-IMPACT: Impact of original decision

**Purpose:** Quantify cost of wrong decision - shows value of better decisions in future.

### Quantified costs (Total: $82K)

| Impact category | Cost | Details | Evidence |
|-----------------|------|---------|----------|
| **Development time (initial migration)** | $32,000 | 4 engineers × 5 weeks × $40/h × 40h/week = $32K | Sprint 19-21 time tracking |
| **Development time (firefighting/fixes)** | $18,000 | 3 engineers × 6 weeks × $40/h × 25h/week = $18K (Nov-Dec) | On-call logs, incident response |
| **Outages/downtime** | $8,000 | 3 outages × 2-3h each = 6.5h downtime, $1,200/h revenue loss = $7.8K | Revenue analytics (customers unable to use product) |
| **Support/escalations** | $4,000 | 15 customer complaints × 3h investigation each × $90/h = $4K | Support ticket time tracking |
| **Opportunity cost** | $20,000 | Sprint 22-24 could've built features (version history, AI analytics) = $20K value | Roadmap analysis (deferred features) |
| **TOTAL DIRECT COST** | **$82,000** | | |

**Cost breakdown by phase:**
- **Phase 1 (PoC):** $5K (2 weeks × 2 engineers)
- **Phase 2 (Development):** $32K (5 weeks × 4 engineers)
- **Phase 3 (Production firefighting):** $30K (incidents + support + downtime)
- **Phase 4 (Reversal):** $15K (4 weeks × 3 engineers) - **[Future cost]**

**Total MongoDB experiment cost:** $82K (already spent) + $15K (reversal) = **$97K total**

---

### Non-quantified impacts

**Team:**
- **Morale:** Team survey (Dec 15): 6/8 engineers "frustrated", 2/8 "considering leaving"
- **Burnout risk:** DevOps engineer (Katarzyna) 40h unplanned work in November (60h weeks)
- **On-call burden:** 3 engineers on rotation, PagerDuty alerts 3×/week (sleep deprivation)
- **Confidence:** "Do we make good technical decisions?" - self-doubt after MongoDB failure
- **Learning time diverted:** Engineers spent time learning MongoDB (now wasted knowledge)

**Business:**
- **Customer trust:** 15 complaints about slow dashboard, 3 customers threatened to churn
- **SLA violations:** 99.5% uptime (vs 99.9% SLA) = breach dla 5 enterprise customers (contracts at risk)
- **Reputation:** Internal reputation of engineering team ("they made bad decision, caused outages")
- **Executive confidence:** CEO questioned "why did we do this?" at All-Hands (Dec 20)

**Technical debt:**
- **Code complexity:** MongoDB-specific code (aggregation pipelines) needs rewriting dla PostgreSQL
- **Dual schema maintenance:** Need to maintain both PostgreSQL + MongoDB schemas during reversal
- **Data migration debt:** Need to migrate 12M records back (4-week effort)
- **Documentation debt:** MongoDB docs now obsolete, PostgreSQL docs outdated

---

### Timeline of degradation

| Date | Event | Impact | Severity |
|------|-------|--------|----------|
| **Sept 20-30** | PoC conducted (1M records) | 45ms latency ✅ "Success!" | ✅ Good |
| **Oct 1** | Decision approved (ADR-042) | Team excited 🎉 | ✅ Good |
| **Oct 8 - Nov 14** | Development (5 weeks) | Sprint 19-21 focused on migration | ⚠️ Opportunity cost |
| **Nov 15** | Production launch | **Outage 1 (2h)** - Replica election failed | 🚩 Red flag |
| **Nov 22 (Week 1)** | First checkpoint | Latency 120ms (2.7× worse than PoC) | 🚩 Red flag |
| **Nov 28 (Week 2)** | **Outage 2 (3h)** - Disk full | SLA breach, customer complaints | 🚩🚩 Critical |
| **Dec 5 (Week 3)** | Data consistency bug | GDPR violation (user data not deleted) | 🚩🚩 Critical |
| **Dec 10 (Week 4)** | **Outage 3 (1.5h)** - Index build | 30K events lost, needed backfill | 🚩🚩🚩 Severe |
| **Dec 15 (Week 5)** | Team survey | 6/8 engineers: "MongoDB was a mistake" | 😞 Morale hit |
| **Dec 20 (Week 5)** | CEO All-Hands | "Why did we do this?" - executive pressure | 😠 Confidence lost |
| **Dec 27 (Week 6)** | **Reversal decision** | Migrate back to PostgreSQL (4 weeks) | 🔄 Pivot |

**Pattern:** Gradual degradation (Week 1 → 6), warning signs ignored due to sunk cost fallacy, finally reversed after 3 outages + executive pressure.

---

## SEC-DR-NEW-DECISION: Nowa decyzja (reversal)

**NEW DECISION:** Migrate back to PostgreSQL + optimize query patterns

**Implementation:** 4-week migration (Jan 6 - Feb 2, 2026)

---

### New option selected

**What we're doing now:**
Reverting analytics module to **PostgreSQL 15** with **optimized schema design** and **advanced indexing strategy**. Target performance: P95 latency <100ms (vs MongoDB 650ms production, better than original 150ms).

**Architecture:**
- **Deployment:** AWS RDS PostgreSQL (m6i.2xlarge, Multi-AZ dla HA)
- **Data model:** Normalized schema (6 tables with foreign keys, JOINs optimized)
- **Query optimization:** Materialized views dla common analytics queries (precomputed aggregations)
- **Indexing strategy:** B-tree indexes dla filters, BRIN indexes dla time-series, covering indexes dla common queries
- **Performance:** Estimated P95 latency = 80ms (benchmarked on 12M records test dataset)

**Why PostgreSQL (again):**

**1. Proven performance at production scale** ✅
- Benchmark (Dec 20-23): PostgreSQL P95 latency = 80ms dla 12M records
- Optimizations applied:
  - Materialized views dla top 5 analytics queries (refresh hourly)
  - Covering indexes (avoid table lookups)
  - Partitioning dla analytics_events table (monthly partitions)
- **Conclusion:** PostgreSQL 80ms < MongoDB 650ms = **8× faster than MongoDB production**

**2. Operational simplicity (AWS RDS = managed service)** ✅
- Zero cluster management (RDS handles HA, backups, monitoring, patching)
- Team expertise (5 years PostgreSQL experience vs 2 months MongoDB)
- On-call burden: Minimal (RDS incidents rare, 99.95% uptime historical)
- **Conclusion:** 5h/month operational overhead (vs MongoDB 25h/month)

**3. ACID transactions (data consistency guaranteed)** ✅
- Foreign key constraints (referential integrity enforced at database level)
- Multi-table transactions (report generation, user deletion cascades)
- No data consistency bugs (vs MongoDB 3 incidents in 6 weeks)
- **Conclusion:** GDPR compliance guaranteed, no manual cleanup scripts

**4. Team expertise and confidence** ✅
- Team knows PostgreSQL deeply (5 years experience, no learning curve)
- Confidence restored (no "will it work?" uncertainty)
- Zero training needed (vs MongoDB 2-week training, now wasted)
- **Conclusion:** Fast implementation (4 weeks), low risk

---

### Is this one of the original alternatives?

✅ **Yes** - reverting to **Option 1: PostgreSQL with optimized indexes** (originally rejected in October 2025)

**Original rejection rationale (October 2025):**
- "PostgreSQL 150ms latency unacceptable (vs MongoDB PoC 45ms)"
- "Complex JOINs slow (6-8 tables)"
- "Doesn't scale horizontally (vertical scaling expensive)"

**Why we were wrong:**
- **150ms latency was WITHOUT optimizations** (no materialized views, no covering indexes, no partitioning)
- **With optimizations:** PostgreSQL achieves 80ms (better than MongoDB 650ms production!)
- **JOINs:** Modern PostgreSQL query planner optimizes JOINs efficiently (vs MongoDB aggregation pipelines)
- **Scaling:** We're at 12M records (not 100M) - PostgreSQL handles this easily, vertical scaling not needed yet

**Lesson:** **Should have optimized PostgreSQL BEFORE considering MongoDB** - premature optimization mistake.

---

### Rationale for reversal

**Key factors:**

**1. Performance: PostgreSQL 8× faster than MongoDB (production reality)** ✅
- MongoDB production: P95 = 650ms ❌
- PostgreSQL optimized: P95 = 80ms ✅
- **Conclusion:** MongoDB promised 3× improvement, delivered 4× degradation → PostgreSQL actually better

**2. Operational simplicity: 5× less work (5h vs 25h/month)** ✅
- MongoDB: 3 outages, 25h/month firefighting, constant PagerDuty alerts
- PostgreSQL RDS: Managed service, 99.95% uptime, minimal operational burden
- **Conclusion:** Team capacity restored, morale improved

**3. Data consistency: Zero bugs vs 3 incidents** ✅
- MongoDB: GDPR violation, report inconsistencies, orphaned documents
- PostgreSQL: ACID transactions, foreign keys, guaranteed consistency
- **Conclusion:** Compliance risk eliminated

**4. Cost: PostgreSQL cheaper ($450/month vs MongoDB $850/month)** ✅
- MongoDB: $450/month instances + $400/month engineer time = $850 total
- PostgreSQL RDS: $450/month (includes automated backups, HA, monitoring)
- **Conclusion:** 47% cost savings ($400/month = $4.8K/year)

**Supporting evidence:**
- **EVIDENCE-POSTGRESQL-BENCHMARK (Dec 20-23):** P95 latency 80ms validated
- **Team consensus:** 8/8 engineers support reversal ("we should never have left PostgreSQL")
- **Customer feedback:** 15/15 customers prefer fast dashboard (don't care about database technology)

---

### Trade-offs accepted

**What we're giving up by reversing:**

**❌ Trade-off 1: Not hitting original 45ms latency target (now 80ms)**
- **Original goal:** MongoDB PoC showed 45ms (3× improvement)
- **PostgreSQL reality:** 80ms (not as good as PoC, but better than production MongoDB 650ms)
- **Acceptable because:**
  - 80ms < 100ms SLA target (meets customer requirements)
  - 80ms = 8× better than MongoDB production (650ms)
  - Original 45ms PoC was **misleading** (1M records, not representative)
- **Verdict:** ✅ **80ms is good enough** - perfect is enemy of good

**❌ Trade-off 2: Sunk cost $82K from MongoDB experiment**
- **Already spent:** $82K (PoC + development + incidents)
- **Cannot recover:** Money and time already lost
- **Acceptable because:**
  - Sunk cost fallacy = don't throw good money after bad
  - Continuing MongoDB = additional $30K/quarter (incidents + operational burden)
  - Reversal cost $15K < continuing MongoDB cost $30K/quarter
- **Verdict:** ✅ **Cut losses now** - reversal saves money long-term

**❌ Trade-off 3: Horizontal scaling story (PostgreSQL vertical scaling only)**
- **MongoDB promise:** Horizontal sharding (add nodes = linear scale)
- **PostgreSQL reality:** Vertical scaling (bigger instance) until ~100M records
- **Acceptable because:**
  - Current scale: 12M records (PostgreSQL comfortable)
  - Projected 2026: 30M records (still within PostgreSQL range)
  - Horizontal scaling only needed at 100M+ records (not our scale)
- **Verdict:** ✅ **Premature optimization** - we don't need horizontal scaling yet

**❌ Trade-off 4: Modern tech stack (MongoDB = "cool", PostgreSQL = "boring")**
- **Lost:** "We use MongoDB" bragging rights, modern tech on resume
- **Gained:** Boring technology that works, team confidence, reliability
- **Acceptable because:**
  - **Choose boring technology** - reliability > novelty
  - Customers don't care (they care about fast dashboard, not database choice)
  - Engineering blog: "Why we chose boring PostgreSQL" = honest story (good for recruiting)
- **Verdict:** ✅ **Boring > exciting** - pragmatism wins

---

### What we're gaining

**✅ Gain 1: 8× better performance (650ms → 80ms)** 💨
- Analytics dashboard: 8-12 sec load time → **2-3 sec** (customer satisfaction)
- Customer complaints: 15 tickets/month → **0 tickets** (projected)
- CEO dashboard: Real-time insights (happy executive)

**✅ Gain 2: 5× less operational work (25h → 5h/month)** ⏰
- DevOps capacity freed: 20h/month dla other projects
- On-call burden eliminated: No more 3AM PagerDuty alerts
- Team morale restored: No more firefighting, focus on features

**✅ Gain 3: Zero data consistency bugs** ✅
- GDPR compliance: Guaranteed (foreign key cascades)
- Report accuracy: 100% (ACID transactions)
- Customer trust: Restored (no more data integrity incidents)

**✅ Gain 4: Cost savings $400/month = $4.8K/year** 💰
- MongoDB: $850/month (instances + engineer time)
- PostgreSQL: $450/month (RDS managed service)
- ROI: Reversal cost $15K paid back in 37.5 months (acceptable)

**✅ Gain 5: Team confidence and expertise** 💪
- PostgreSQL: Deep expertise (5 years), no uncertainty
- MongoDB: Shallow knowledge (2 months), wasted learning
- Future decisions: "Optimize what we have before switching" (lesson internalized)

---

### Why not continue with original decision (MongoDB)?

**Considered alternatives to reversal:**

**❌ Alternative 1: Optimize MongoDB (upgrade instances, tune queries)**
- **Approach:** Upgrade to m5.2xlarge (64GB RAM), hire MongoDB consultant ($10K)
- **Estimated improvement:** P95 latency 650ms → 300ms (still 3.75× worse than PostgreSQL 80ms)
- **Cost:** $1,800/month instances + $10K consultant = $31.6K Year 1
- **Rejected because:** Still slower than PostgreSQL (300ms vs 80ms), still high operational burden, throwing good money after bad

**❌ Alternative 2: Hybrid approach (PostgreSQL dla queries, MongoDB dla writes)**
- **Approach:** Write to MongoDB (flexible schema), read from PostgreSQL (fast queries)
- **Complexity:** Dual-write synchronization, data consistency issues, 2× operational burden
- **Cost:** $850/month MongoDB + $450/month PostgreSQL = $1,300/month
- **Rejected because:** Complexity explodes (worst of both worlds), data sync bugs inevitable, operational nightmare

**❌ Alternative 3: Migrate to managed MongoDB (Atlas)**
- **Approach:** Switch from self-hosted to MongoDB Atlas (managed service)
- **Estimated improvement:** Operational burden reduced (Atlas handles HA, backups), but performance same
- **Cost:** $2,400/month Atlas (M50 tier) = 2.8× more expensive than current
- **Rejected because:** Doesn't solve performance problem (still 650ms latency), too expensive ($28.8K/year)

**Verdict:** All alternatives worse than reversal to PostgreSQL (slower, more expensive, more complex).

---

## SEC-DR-MIGRATION: Migration plan

**Migration owner:** Backend Team (Piotr Nowak - Tech Lead)
**Timeline:** 4 weeks (January 6 - February 2, 2026)
**Risk level:** MEDIUM (well-understood technology, thorough testing planned)

---

### Migration phases

#### Phase 1: Preparation (Week 1: Jan 6-12, 2026)
**Duration:** 5 days (Mon-Fri)
**Goal:** Set up PostgreSQL, optimize schema, prepare dual-write

**Tasks:**
- [x] Provision PostgreSQL RDS instance (m6i.2xlarge, Multi-AZ, 500GB storage)
- [x] Create optimized schema (6 tables, foreign keys, indexes, partitions)
- [x] Implement materialized views (top 5 analytics queries, hourly refresh)
- [x] Configure monitoring (CloudWatch alarms, slow query log, error tracking)
- [ ] Setup dual-write code (write to both MongoDB + PostgreSQL for validation)
- [ ] Data validation scripts (compare record counts, checksums, query results)

**Success criteria:**
- PostgreSQL instance provisioned, schema created, indexes built
- Dual-write code deployed to staging (validated with test data)
- Data validation scripts pass 100% dla staging test dataset (1M records)

**Owner:** Backend Team (Piotr + 2 engineers)

---

#### Phase 2: Dual-write + Data backfill (Week 2: Jan 13-19, 2026)
**Duration:** 7 days (continuous backfill)
**Goal:** Backfill historical data to PostgreSQL, enable dual-write for new data

**Tasks:**
- [ ] Deploy dual-write to production (write to both MongoDB + PostgreSQL)
  - New events: Written to both databases simultaneously
  - Reads: Still from MongoDB (no user-facing change yet)
- [ ] Start data backfill (MongoDB → PostgreSQL, 12M records)
  - Batch size: 10K records per batch
  - Rate limit: 100 batches/hour = 1M records/day
  - Estimated duration: 12 days dla 12M records
- [ ] Monitor backfill progress (CloudWatch dashboard, Slack alerts)
- [ ] Validate data consistency (spot-check 1% of records, compare MongoDB vs PostgreSQL)

**Success criteria:**
- Dual-write deployed, 0 errors in 24 hours (write to both DBs successfully)
- Backfill progress: 50% complete by end of Week 2 (6M records migrated)
- Data validation: 99.9%+ consistency between MongoDB and PostgreSQL
- Performance: PostgreSQL queries maintain <100ms latency during backfill

**Owner:** Backend Team (continuous monitoring), DevOps (infrastructure)

**Risk mitigation:**
- Backfill runs low-priority (doesn't impact production traffic)
- Rollback plan: Disable dual-write if errors >0.1%
- Data corruption check: Daily validation (compare record counts, checksums)

---

#### Phase 3: Gradual read cutover (Week 3: Jan 20-26, 2026)
**Duration:** 7 days (phased rollout)
**Goal:** Migrate reads from MongoDB to PostgreSQL gradually (10% → 50% → 100%)

**Timeline:**
- **Monday (Jan 20):** 10% reads from PostgreSQL (feature flag: `analytics_postgres_reads` = 10%)
  - Monitor latency (P50, P95, P99), error rate, user complaints
  - Checkpoint: If P95 >100ms sustained 4h → ROLLBACK to MongoDB
- **Wednesday (Jan 22):** 50% reads from PostgreSQL (if Monday successful)
  - Monitor 24 hours, validate performance stable
  - Customer feedback: Survey 50% cohort (dashboard experience improved?)
- **Friday (Jan 24):** 100% reads from PostgreSQL (if Wednesday successful)
  - Full cutover, MongoDB read traffic drops to 0%
  - Keep MongoDB live (backup for 2 weeks, rollback option)

**Tasks:**
- [ ] Deploy feature flag (analytics_postgres_reads: 0% → 10% → 50% → 100%)
- [ ] Monitor latency/errors dla each phase (CloudWatch dashboards)
- [ ] Conduct performance spot-checks (test 20 common queries, validate <100ms)
- [ ] Customer feedback survey (send to 50% cohort on Wednesday)

**Success criteria:**
- **10% phase:** P95 latency <100ms, error rate <0.1%, 0 customer complaints
- **50% phase:** Maintained P95 <100ms dla 24 hours, customer feedback neutral/positive
- **100% phase:** Full cutover successful, MongoDB reads = 0%, PostgreSQL P95 <80ms

**Rollback trigger:**
- P95 latency >150ms sustained 4 hours → ROLLBACK to previous phase
- Error rate >1% → IMMEDIATE ROLLBACK to MongoDB
- Customer complaints >5 in 24h → HOLD rollout, investigate

**Owner:** Backend Team (monitoring), Product Manager (customer feedback)

---

#### Phase 4: Cleanup + Decommission (Week 4: Jan 27 - Feb 2, 2026)
**Duration:** 5 days (Mon-Fri)
**Goal:** Remove MongoDB, update docs, finalize migration

**Tasks:**
- [ ] Validate PostgreSQL stable (1 week at 100% reads, 0 incidents)
- [ ] Remove dual-write code (write only to PostgreSQL, MongoDB deprecated)
- [ ] Decommission MongoDB cluster (terminate EC2 instances, delete snapshots)
  - Export MongoDB data to S3 (cold storage backup, 90-day retention dla safety)
  - Terminate instances, release Elastic IPs, delete CloudWatch alarms
- [ ] Update documentation
  - [x] Technical Design Doc (TDD) - update analytics architecture diagram
  - [x] API documentation - remove MongoDB references
  - [x] Runbook - PostgreSQL operational procedures
  - [ ] ADR-055 - formalize PostgreSQL decision (replaces ADR-042)
- [ ] Team retrospective (what went wrong, lessons learned, process improvements)

**Success criteria:**
- PostgreSQL running at 100% dla 1 week, P95 latency <80ms stable
- MongoDB cluster decommissioned, $450/month cost savings realized
- Documentation updated (TDD, API docs, runbook current)
- Retrospective completed, lessons documented (DECISION-REVERSAL-001)

**Owner:** Backend Team (cleanup), Tech Lead (retrospective)

---

### Rollback plan

**Purpose:** If migration fails, how do we rollback to MongoDB?

**Rollback strategy:**
- **Phase 2 (dual-write):** Disable dual-write flag → writes only to MongoDB
- **Phase 3 (read cutover):** Revert feature flag → reads from MongoDB (instant rollback)
- **Phase 4 (decommission):** Keep MongoDB live dla 2 weeks after Phase 3 completion

**Rollback window:**
- **Weeks 2-3 (dual-write + cutover):** Instant rollback (<5 minutes, feature flag flip)
- **Week 4 (cleanup):** Keep MongoDB dla 2 weeks (can restart if critical issue)
- **After Week 6:** MongoDB data archived to S3 (cold storage, 90-day retention)

**Rollback triggers:**
- PostgreSQL P95 latency >150ms sustained 4 hours
- Error rate >1% (data consistency issues)
- Critical bug discovered (data loss, GDPR violation)
- Customer escalations >10 in 24 hours

**Rollback procedure:**
1. Flip feature flag: `analytics_postgres_reads` = 0% (revert to MongoDB reads)
2. Disable dual-write: Write only to MongoDB (PostgreSQL deprecated)
3. Announce to team: "Rolled back to MongoDB, investigating issue"
4. Root cause analysis: Why did PostgreSQL fail? (1-2 days investigation)
5. Decision: Fix PostgreSQL and retry, or abandon reversal (escalate to CTO)

**Owner:** Tech Lead (rollback authority), DevOps (execute rollback)

---

### Migration risks

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Data corruption during backfill** | LOW (5%) | HIGH | Validation scripts (daily), checksums, spot-checks 1% |
| **PostgreSQL performance worse than benchmark** | MEDIUM (20%) | HIGH | Extensive pre-testing (12M records test dataset), rollback ready |
| **Dual-write bugs (writes dropped)** | LOW (10%) | MEDIUM | Monitoring (alert if write count diverges), validation scripts |
| **Downtime during cutover** | VERY LOW (<1%) | MEDIUM | Zero-downtime migration (feature flags, gradual rollout) |
| **Customer complaints (dashboard changes)** | LOW (5%) | LOW | No UI changes (backend only), customer comms (transparency) |

**Overall risk:** MEDIUM - well-understood technology (PostgreSQL), thorough testing planned, gradual rollout, instant rollback option.

---

### Communication plan

#### Internal stakeholders

| Stakeholder | What to communicate | When | Channel |
|-------------|-------------------|------|---------|
| **Engineering Team** | Migration plan, timeline, responsibilities | Jan 5 (kickoff meeting) | Team meeting + Slack |
| **Product Team** | Timeline, user-facing impact (none), rollback plan | Jan 5 | Slack DM |
| **Customer Success** | Migration happening (backend only), customer impact (dashboard faster), talking points if asked | Jan 12 (Week 2 start) | Email + FAQ doc |
| **Executive Team** | Migration rationale (MongoDB failure), cost ($15K reversal vs $82K wasted), timeline | Jan 5 (CTO approval) | Email summary |
| **DevOps/On-call** | Monitoring dashboards, rollback procedure, escalation path | Jan 6 (Phase 1 start) | Runbook update |

**Key messages:**
- **Why:** MongoDB experiment failed (performance, operational burden), PostgreSQL better
- **What:** 4-week migration (dual-write → gradual cutover → decommission)
- **Risk:** Low (gradual rollout, instant rollback, PostgreSQL proven technology)
- **Impact:** Customer-facing: None (dashboard faster), Internal: Team capacity freed (20h/month)

#### External stakeholders (customers)

**Do we tell customers?**
- **NO** - migration is backend-only, zero user-facing changes
- **Exception:** If customers ask "why is dashboard faster?" → "We optimized our database" (don't mention MongoDB failure)

**If migration fails (rollback):**
- **Customer communication:** None (rollback instant, no downtime)
- **Internal communication:** Post-mortem (why rollback, what next)

---

## SEC-DR-LESSONS: Lessons learned

**Purpose:** Capture actionable lessons - prevent repeating same mistakes.

### What went wrong (summary)

**Top 5 mistakes:**

**1. PoC was insufficient (dataset too small, operational testing skipped)** ❌
- Tested 1M records, production = 12M records (12× gap)
- Tested 2 weeks, production degraded over 6 weeks (long-term testing skipped)
- Tested single-node, production = 3-node replica set (operational complexity missed)

**2. Confirmation bias (wanted MongoDB to work, ignored red flags)** ❌
- Working set close to RAM limit (800MB → 9.6GB projected) - dismissed
- Company X mentioned "operational challenges" - ignored
- Week 1 latency 120ms (2.7× worse than PoC) - rationalized

**3. No pilot phase (big bang migration, 100% cutover Day 1)** ❌
- Went straight from PoC → 100% migration (no gradual rollout)
- No dual-write period (safety net for rollback)
- Big bang = maximum blast radius if failure

**4. Sunk cost fallacy (delayed reversal by 4 weeks)** ❌
- Week 2: "We invested 5 weeks, let's give it time" → cost +$20K
- Week 4: "We already migrated, can't admit failure" → cost +$20K
- Week 6: Finally reversed → total cost $82K (could've been $15K if reversed Week 2)

**5. Operational readiness not assessed (skills gap, on-call burden)** ❌
- Assumed "PostgreSQL experience = MongoDB experience" (wrong)
- Didn't evaluate team capacity (DevOps already stretched thin)
- No operational runbook prepared before launch (ad-hoc incident response)

---

### Lessons learned (actionable)

#### Lesson 1: PoC must test 10× production scale + worst-case scenarios

**What we learned:**
PoC with 1M records is **not representative** of 12M production. Performance characteristics change dramatically at scale (working set > RAM, index bloat, query planner behavior). Testing only "happy path" queries misses worst-case scenarios (ad-hoc queries, concurrent load, long-running aggregations).

**Why it matters:**
If PoC had tested 10M+ records, we would have discovered:
- Working set > RAM (performance cliff)
- Index bloat issues (12 indexes vs 3)
- Query pattern diversity (20+ queries vs 5)
→ Would have **rejected MongoDB in October**, saved $82K

**Action item: Update PoC template**
- [x] **Requirement:** Test 10× target production data volume (not 1:1 with current data)
- [x] **Requirement:** Test worst-case queries (ad-hoc, complex aggregations, concurrent load)
- [x] **Requirement:** Run PoC dla 4-6 weeks minimum (observe performance degradation over time)
- [x] **Requirement:** Test production-like environment (HA setup, backups, monitoring, not single-node)
- [x] **Requirement:** Load testing (50+ concurrent users, realistic traffic patterns)
- **Owner:** Tech Lead (Piotr) - update `/docs/templates/poc-template.md`
- **Due:** February 15, 2026 (before next PoC conducted)

---

#### Lesson 2: Operational readiness assessment mandatory before production

**What we learned:**
"Team can manage X" is **assumption, not fact**. PostgreSQL RDS experience (managed service) ≠ MongoDB self-hosted experience (cluster management). Operational complexity must be **validated**, not assumed. Skills gap assessment, on-call burden estimation, runbook preparation = non-negotiable **before** production launch.

**Why it matters:**
3 outages in 1 month = operational readiness failure. If we had:
- Conducted skills assessment → would've hired MongoDB consultant ($5K)
- Estimated on-call burden → would've allocated 2 engineers (not 0)
- Prepared operational runbook → faster incident response (2h → 30min)
→ Could've **prevented 2/3 outages**, saved $6K downtime cost

**Action item: Create operational readiness checklist**
- [x] **Checklist item:** Skills assessment (does team have expertise? If NO → hire consultant or train)
- [x] **Checklist item:** Operational runbook (incident response procedures, escalation paths)
- [x] **Checklist item:** On-call burden estimation (historical data from similar technologies)
- [x] **Checklist item:** Monitoring + alerting (before launch, not after)
- [x] **Checklist item:** Practice incident response (chaos engineering, failover drill)
- **Owner:** Engineering Manager (Michał) - create checklist template
- **Due:** February 15, 2026
- **Enforcement:** ADR approval blocked if checklist not completed

---

#### Lesson 3: Gradual rollout (pilot phase) mandatory dla infrastructure changes

**What we learned:**
Big bang migration (0% → 100% Day 1) = **maximum risk**. Gradual rollout (10% → 50% → 100%) = learn quickly, fail safely. Pilot phase with small cohort (50 users) reveals issues before full rollout (5,000 users). Dual-write period = safety net (instant rollback if issues).

**Why it matters:**
If we had gradual rollout:
- **Week 1:** 10% traffic to MongoDB → latency 120ms detected → HOLD rollout
- **Week 2:** Investigate root cause (working set > RAM) → decide: fix or revert
- **Outcome:** Either fix early (cost $5K) or revert early (cost $15K vs $82K actual)

**Action item: Mandatory gradual rollout dla infrastructure changes**
- [x] **Policy:** All infrastructure migrations require gradual rollout (no big bang)
- [x] **Phases:** 10% → 50% → 100% (minimum 3 phases, checkpoints between)
- [x] **Dual-write:** Required dla database migrations (2-week overlap minimum)
- [x] **Rollback plan:** Feature flags for instant rollback (<15 min)
- [x] **Checkpoints:** Go/No-Go decision at each phase (not automatic progression)
- **Owner:** Tech Lead (Piotr) - update `/docs/engineering/deployment-standards.md`
- **Due:** February 15, 2026
- **Enforcement:** Code review blocks deployment if gradual rollout not implemented

---

#### Lesson 4: Fail fast, reverse quickly (avoid sunk cost fallacy)

**What we learned:**
Sunk cost fallacy **expensive** - delayed reversal by 4 weeks = +$20K cost. Week 2 red flags (latency degrading, Outage 2) should've triggered reversal evaluation. "We invested so much" = **bad reason** to continue. Better: Cut losses early, revert quickly, learn from failure.

**Why it matters:**
- **Week 2 reversal cost:** $15K (backfill incomplete, dual-write active)
- **Week 6 reversal cost:** $82K (full migration + incidents + opportunity cost)
- **Delta:** $67K wasted by delaying reversal 4 weeks

**Action item: Establish reversal decision framework**
- [x] **Trigger:** 2 incidents in 2 weeks → automatic reversal review (not optional)
- [x] **Trigger:** Key metric degrades >2× baseline → reversal review
- [x] **Trigger:** Team consensus "this isn't working" → reversal review (listen to engineers)
- [x] **Decision gate:** Reversal decision within 48h of trigger (not weeks of debate)
- [x] **Bias training:** Sunk cost fallacy awareness training dla leadership (quarterly)
- **Owner:** CTO (Marek) - establish reversal decision process
- **Due:** February 1, 2026
- **Enforcement:** Incident review process updated (include "should we reverse?" question)

---

#### Lesson 5: Optimize existing solution before switching technologies

**What we learned:**
**Premature optimization mistake** - switched to MongoDB before optimizing PostgreSQL. Original PostgreSQL latency = 150ms (without materialized views, covering indexes, partitioning). Optimized PostgreSQL = 80ms (better than MongoDB PoC 45ms!). Lesson: **Exhaust optimization opportunities** before technology switch.

**Why it matters:**
If we had optimized PostgreSQL first:
- Cost: $5K (1-week optimization work) vs $97K (MongoDB experiment + reversal)
- Timeline: 1 week vs 12 weeks (3 months wasted)
- Risk: Low (known technology) vs High (new technology)
- Outcome: 80ms latency achieved without migration pain
→ **$92K saved**, 11 weeks saved, zero incidents

**Action item: "Optimize before switch" policy**
- [x] **Policy:** Before switching databases/frameworks, must demonstrate:
  - [x] Current technology optimized (indexes, queries, caching, profiling)
  - [x] Performance ceiling reached (can't optimize further without technology change)
  - [x] New technology benchmarked at 10× scale (not current scale)
- [x] **Approval gate:** CTO approval required dla technology switch (not just Tech Lead)
- [x] **Documentation:** ADR must include "optimization attempts" section (what we tried first)
- **Owner:** CTO (Marek) - establish technology switch approval process
- **Due:** February 1, 2026
- **Enforcement:** ADR template updated (add "optimization attempts" required section)

---

### What we'll do differently next time

**Process improvements (implemented by Feb 15, 2026):**

**1. ✅ Extended PoC (4-6 weeks vs 2 weeks)**
- Minimum PoC duration: 4 weeks (observe long-term behavior)
- PoC dataset: 10× production scale (not 1:1 with current data)
- PoC environment: Production-like (HA, monitoring, not single-node)

**2. ✅ Scale testing mandatory (10× production dataset)**
- Test 10× target data volume (if 12M production, test 120M)
- Test worst-case queries (ad-hoc, complex aggregations)
- Load testing: 50+ concurrent users, realistic traffic patterns

**3. ✅ Operational readiness assessment (team capability + runbooks)**
- Skills assessment: Does team have expertise? (validated, not assumed)
- On-call burden: Estimated from historical data, allocated resources
- Runbook: Prepared before launch (incident response procedures)

**4. ✅ Pilot phase (20% → 50% → 100% rollout)**
- Gradual rollout mandatory (no big bang)
- Dual-write period: 2 weeks minimum (safety net for rollback)
- Checkpoints: Go/No-Go decision at each phase

**5. ✅ Regular decision review (1 month post-implementation)**
- **30-day checkpoint:** Review metrics vs PoC predictions (are assumptions holding?)
- **Reversal trigger:** 2 incidents in 2 weeks → automatic reversal review
- **Learning:** Document lessons learned (what worked, what didn't)

**6. ✅ "Optimize before switch" policy**
- Exhaust optimization opportunities before technology change
- CTO approval required dla infrastructure switches (not just Tech Lead)
- ADR must document "what we tried first" (optimization attempts)

---

### Cognitive biases / decision traps identified

**Cognitive biases that affected decision-making:**

**1. Confirmation bias** ❌
- **Trap:** Wanted MongoDB to work (exciting new technology) → ignored red flags
- **Evidence:** Dismissed working set concern (800MB → 9.6GB), ignored Company X warning ("operational challenges")
- **Countermeasure:** Devil's advocate role (one person argues against decision), pre-mortem exercise ("assume this fails, why?")

**2. Sunk cost fallacy** ❌
- **Trap:** "We invested 5 weeks development, can't give up now" → delayed reversal, wasted +$20K
- **Evidence:** Week 2 Outage 2 should've triggered reversal, but "let's give it time"
- **Countermeasure:** Reversal decision framework (2 incidents → automatic review), awareness training

**3. Availability heuristic** ❌
- **Trap:** Remembered MongoDB marketing ("fast, scalable, flexible") → forgot PostgreSQL capabilities
- **Evidence:** Assumed PostgreSQL can't be optimized (forgot materialized views, partitioning)
- **Countermeasure:** Systematic comparison (benchmark both options), consult experts (not just marketing)

**4. Dunning-Kruger effect** ❌
- **Trap:** Overestimated team's MongoDB competence ("we can manage it") → 3 outages
- **Evidence:** Assumed RDS experience = self-hosted experience (wrong)
- **Countermeasure:** Skills assessment (validate expertise), hire consultants (admit knowledge gaps)

**5. IKEA effect** ❌
- **Trap:** "We built this MongoDB migration" → overvalued our work, reluctant to abandon
- **Evidence:** Emotional attachment to MongoDB implementation → delayed reversal
- **Countermeasure:** External review (unbiased perspective), focus on outcomes (not effort invested)

**How to avoid in future:**
- [x] **Pre-mortem exercise:** Before ADR approval, team imagines "this failed, why?" (surface concerns early)
- [x] **Devil's advocate:** One person argues against decision (challenge assumptions)
- [x] **External review:** Consultant or peer team reviews ADR (unbiased perspective)
- [x] **Bias awareness training:** Quarterly training on cognitive biases (leadership + engineers)
- [x] **Reversal decision framework:** Structured process dla "should we reverse?" (not ad-hoc)

---

### Knowledge sharing

**How we'll share lessons learned (prevent organizational amnesia):**

#### Documentation updates

- [x] **ADR-042 updated:** Mark as "superseded" by ADR-055, link to DECISION-REVERSAL-001
- [x] **ADR-055 created:** PostgreSQL optimization decision (formalize reversal)
- [x] **PoC template updated:** Add scale testing requirements (10× data, 4-6 weeks, production-like env)
- [x] **ADR template updated:** Add "optimization attempts" section (what we tried first)
- [x] **Anti-Patterns catalog:** Add "MongoDB experiment" as case study (what went wrong)
- **Owner:** Tech Lead (Piotr)
- **Due:** February 15, 2026

#### Internal communication

- [ ] **Engineering All-Hands (Feb 10, 2026):** 30-min presentation
  - Title: "Lessons from MongoDB experiment: How we wasted $82K (and how to avoid it)"
  - Audience: All engineers (30 people)
  - Goal: Share lessons, update processes, build psychological safety ("it's OK to fail, learn, reverse")
- [ ] **Leadership sync (Feb 5, 2026):** 15-min summary dla CTO + Engineering Manager
  - Focus: Process improvements implemented, cost of failure, ROI of better decisions
- [ ] **Weekly engineering newsletter (Feb 12, 2026):** Article summary + link to full doc
- **Owner:** Tech Lead (Piotr) - prepare presentations

#### External communication (optional)

- [ ] **Blog post (March 2026):** "When MongoDB isn't the answer: A cautionary tale"
  - **Audience:** External (engineering community, Hacker News, Reddit /r/programming)
  - **Goal:** Honest story (builds credibility), share lessons (help others avoid same mistake)
  - **Tone:** Humble, educational, not defensive ("we made mistakes, here's what we learned")
  - **Approval:** CTO approval required (reputation risk assessment)
- [ ] **Conference talk (Q2 2026):** Submit to local tech meetup or conference
  - **Title:** "The $82K database migration: PoC pitfalls and cognitive biases"
  - **Goal:** Community knowledge sharing, recruiting (honest engineering culture)

---

### Success metrics for reversal

**How will we know the reversal was right decision?**

| Metric | Target | Actual (fill post-reversal) | Review date |
|--------|--------|----------------------------|-------------|
| **Performance: P50 latency** | <80ms | [TBD] | Feb 9, 2026 (1 week post-cutover) |
| **Performance: P95 latency** | <100ms | [TBD] | Feb 9, 2026 |
| **Performance: P99 latency** | <200ms | [TBD] | Feb 9, 2026 |
| **Reliability: Uptime** | >99.9% | [TBD] | Feb 29, 2026 (1 month post-cutover) |
| **Reliability: Incidents** | 0 P0/P1 incidents | [TBD] | Feb 29, 2026 |
| **Operational: Firefighting time** | <5h/month | [TBD] | Feb 29, 2026 |
| **Cost: Monthly spend** | <$500/month | [TBD] | Feb 29, 2026 |
| **Customer satisfaction: Complaints** | 0 complaints | [TBD] | Feb 29, 2026 |
| **Team morale: Survey score** | >4.0/5 | [TBD] | Feb 29, 2026 |

**Review date:** **March 7, 2026** (1 month post-reversal, final retrospective)

**Success criteria:**
- ✅ **Performance:** All latency targets met (P95 <100ms)
- ✅ **Reliability:** Zero incidents, 99.9%+ uptime
- ✅ **Operational:** Firefighting time <5h/month (vs MongoDB 25h/month)
- ✅ **Cost:** Monthly spend <$500 (vs MongoDB $850)
- ✅ **Team:** Morale restored (survey >4.0/5, vs MongoDB 2.8/5)

---

## Appendix: Supporting documentation

### Original decision artifacts
- **ADR-042-MONGODB-MIGRATION:** `/docs/engineering/decisions/ADR-042-mongodb-analytics-migration.md`
- **POC-042-MONGODB-BENCHMARK:** `/docs/engineering/pocs/POC-042-mongodb-benchmark-sept2025.md`
- **REQUIREMENTS-ANALYTICS-2025:** `/docs/engineering/requirements/analytics-module-requirements-2025.md`

### Evidence of failure
- **EVIDENCE-MONGODB-PROD-METRICS:** `/docs/satellites/evidence/E-180-mongodb-production-metrics-nov-dec-2025.md`
- **EVIDENCE-INCIDENT-REPORTS:**
  - Outage 1 (Nov 15): `/docs/incidents/INC-2025-11-15-mongodb-primary-election-failure.md`
  - Outage 2 (Nov 28): `/docs/incidents/INC-2025-11-28-mongodb-disk-full-secondary.md`
  - Outage 3 (Dec 10): `/docs/incidents/INC-2025-12-10-mongodb-index-build-blocking-writes.md`
- **EVIDENCE-COST-ANALYSIS:** `/docs/satellites/evidence/E-181-mongodb-experiment-cost-analysis-82K.md`
- **EVIDENCE-CUSTOMER-COMPLAINTS:** `/docs/support/customer-feedback-analytics-slow-nov-dec-2025.md`

### New decision artifacts
- **ADR-055-POSTGRESQL-OPTIMIZATION:** `/docs/engineering/decisions/ADR-055-postgresql-analytics-optimization.md` (to be created)
- **EVIDENCE-POSTGRESQL-BENCHMARK:** `/docs/satellites/evidence/E-182-postgresql-optimized-benchmark-dec2025.md`
- **MIGRATION-PLAN-MONGODB-TO-PG:** `/docs/engineering/migrations/MIGRATION-PLAN-001-mongodb-to-postgresql-jan2026.md`

---

**Document completed by:** Piotr Nowak (Tech Lead) + Backend Team + CTO (Marek Nowicki)
**Czas wypełnienia:** 8 godzin (comprehensive retrospective, root cause analysis, lessons learned)
**Template version:** DECISION-REVERSAL v1.0
**Final outcome:** Reversal approved, migration starts Jan 6, 2026. Lessons learned documented dla organizational knowledge. 🔄

---

**Post-reversal update (March 7, 2026):**

**SUCCESS METRICS (1 month post-reversal):**
- ✅ Performance: P95 = 78ms (target <100ms) - **EXCEEDED** 🎉
- ✅ Reliability: 99.97% uptime, 0 incidents - **EXCEEDED**
- ✅ Operational: 3h/month firefighting (target <5h) - **EXCEEDED**
- ✅ Cost: $450/month (target <$500) - **MET**
- ✅ Team morale: 4.3/5 survey (target >4.0) - **EXCEEDED**
- ✅ Customer satisfaction: 0 complaints, 3 positive feedback - **EXCEEDED**

**VERDICT:** Reversal was **100% correct decision** ✅

**Lessons internalized:**
- Team now asks "Did we optimize current solution first?" before technology switches
- PoC template updated (10× scale, 4-6 weeks) - used successfully dla Redis cache evaluation (Feb 2026)
- Reversal decision framework prevented another bad decision (Elasticsearch experiment cancelled after red flags)

**ROI of better decisions:**
- MongoDB experiment cost: $97K (wasted)
- Process improvements value: **$200K+ saved over 2026** (prevented 2 similar mistakes)
- Team confidence restored, engineering culture stronger

**The end.** 🚀
