# EXPERIMENT-LOG: EXP-001 - MongoDB Performance Benchmark vs PostgreSQL

---

## Document Metadata

```yaml
id: EXPERIMENT-001
doctype: EXPERIMENT-LOG
status: completed
version: 2.0
created: 2026-01-06
updated: 2026-02-14
owner: Jan Kowalski
project: Ishkarim Document Management System
experiment_id: EXP-001
hypothesis_id: HYPOTHESIS-001
```

---

## Cross-References

```yaml
dependencies:
  - id: HYPOTHESIS-001
    type: requires
    reason: "Eksperyment waliduje hipotezę o wydajności MongoDB vs PostgreSQL"

impacts:
  - id: RESEARCH-FINDINGS-001
    type: blocks
    reason: "Research Findings będą agregować wyniki z tego eksperymentu"
  - id: ADR-042
    type: informs
    reason: "Dane z eksperymentu wspierają decyzję o migracji bazy danych"
  - id: POC-DOC-001
    type: informs
    reason: "PoC wykorzystuje wyniki tego eksperymentu"
```

---

## SEC-EXP-HYPOTHESIS: Link do hipotezy

### Hipoteza testowana

**ID:** HYPOTHESIS-001
**Stwierdzenie:** Migracja z PostgreSQL na MongoDB poprawi wydajność full-text search o minimum 60%, graph queries o 50%, oraz document indexing o 40%.

### Success criteria (z hipotezy)

- [x] Full-text search średnio <1.0s (baseline: 2.5s) - **ACHIEVED: 0.6s** ✅
- [x] Graph queries średnio <0.9s (baseline: 1.8s) - **ACHIEVED: 0.7s** ✅
- [x] Document indexing <300ms (baseline: 500ms) - **ACHIEVED: 280ms** ✅
- [x] 100% feature parity - **CONFIRMED** ✅
- [x] Infrastructure cost ≤$1,040/mth - **ACTUAL: $920/mth** ✅

---

## SEC-EXP-SETUP: Setup eksperymentu

### Środowisko

**PostgreSQL (Baseline):**
- Platform: AWS RDS
- Instance type: db.t3.large (2 vCPU, 8GB RAM)
- OS: Amazon Linux 2
- Network: VPC eu-central-1, private subnet
- PostgreSQL version: 14.5
- Storage: 100GB gp3 SSD

**MongoDB (Experiment):**
- Platform: MongoDB Atlas
- Instance type: M30 (8GB RAM, 2 vCPU, NVMe SSD)
- Region: AWS eu-central-1
- Network: VPC Peering do naszego AWS VPC
- MongoDB version: 7.0.4
- Storage: 100GB (auto-scaling enabled)

### Konfiguracja

**PostgreSQL config:**
```yaml
shared_buffers: 2GB
effective_cache_size: 6GB
work_mem: 16MB
maintenance_work_mem: 512MB
max_connections: 100
```

**MongoDB config:**
```yaml
# Atlas M30 defaults
wiredTiger:
  engineConfig:
    cacheSizeGB: 6
  collectionConfig:
    blockCompressor: snappy
indexes:
  - collection: documents
    fields: {content: "text", metadata: 1}
  - collection: dependencies
    fields: {from_doc: 1, to_doc: 1}
```

### Dataset

- **Source:** Anonymized production data z 3 customer projects
- **Size:** 10,000 dokumentów Markdown + 5,000 Canvas files
- **Total volume:** 180MB raw content
- **Dependencies:** 12,500 cross-references (średnio 1.25 dep/doc)
- **Characteristics:**
  - Średni rozmiar dokumentu: 12KB
  - Największy dokument: 450KB (technical spec)
  - Najmniejszy: 0.5KB (TODO note)
  - Średnia długość dependency chain: 4.2 nodes

### Narzędzia

- **JMeter 5.6**: Load testing, benchmark orchestration
- **pymongo 4.6.1**: MongoDB Python driver
- **psycopg2 2.9.9**: PostgreSQL Python adapter
- **Python 3.11**: Custom scripts do migracji i validacji
- **Datadog**: Real-time monitoring, metrics collection
- **pgbench**: PostgreSQL native benchmarking tool

### Baseline

**PostgreSQL baseline metrics** (measured 2025-12-01 to 2025-12-31):
- Full-text search (p95): 2.5s
- Graph query (p95): 1.8s
- Document insert + index: 500ms
- Concurrent read throughput: 45 queries/sec
- Memory usage: 6.2GB average

---

## SEC-EXP-PROCEDURE: Procedura wykonania

### Kroki eksperymentu

1. **Environment Preparation** (Week 1)
   - Provision MongoDB Atlas M30 cluster
   - Setup VPC peering
   - Configure Datadog monitoring dla obu systemów
   - Validate network connectivity i latency

2. **Data Migration** (Week 1-2)
   - Export wszystkich dokumentów z PostgreSQL (pg_dump)
   - Transform schema: relational → document model
   - Import do MongoDB z checksums
   - Verify data integrity (0 missing records)

3. **Benchmark Preparation** (Week 2)
   - Prepare 100 realistic query patterns
   - Setup JMeter test plans (search, graph, write operations)
   - Warmup cache dla obu systemów (1000 dummy queries)

4. **Execution - Search Benchmark** (Week 3)
   - Run 10,000 full-text search queries
   - Measure p50, p95, p99 latencies
   - Test load: 1, 10, 50, 100 concurrent users

5. **Execution - Graph Benchmark** (Week 3)
   - Run 5,000 dependency graph traversal queries
   - Test depth: 1-hop, 2-hop, 5-hop, full graph
   - Measure query planning + execution time

6. **Execution - Write Benchmark** (Week 4)
   - Insert 1,000 new documents
   - Measure indexing time per document
   - Test concurrent writes (10 writers)

7. **Analysis** (Week 4)
   - Aggregate all metrics
   - Statistical significance testing (t-test)
   - Cost analysis (actual AWS bills)

### Variables

**Independent variables (controlled):**
- Database system: PostgreSQL vs MongoDB
- Query type: search / graph / write
- Concurrent load: 1, 10, 50, 100 users
- Document size: small (<5KB), medium (5-50KB), large (>50KB)

**Dependent variables (measured):**
- Query latency (ms): p50, p95, p99
- Throughput (queries/second)
- CPU utilization (%)
- Memory usage (GB)
- Network I/O (MB/s)
- Cost ($/month)

**Control variables (constant):**
- Hardware specs (equivalent: t3.large vs M30)
- Network location (same AWS region)
- Dataset (identical 10K docs)
- Time of day (all tests 02:00-06:00 UTC, low traffic)

---

## SEC-EXP-OBSERVATIONS: Obserwacje (timestamped)

### 2026-01-06 10:00 - Rozpoczęcie eksperymentu

**Status:** Setup

**Observations:**
- MongoDB Atlas M30 cluster provisioned successfully
- VPC peering established, ping latency: 0.8ms (excellent)
- Datadog agents deployed na obu systemach

**Actions taken:**
- Configured Atlas firewall rules (whitelist application IPs)
- Enabled Atlas Search index creation

---

### 2026-01-10 14:30 - Data Migration Complete

**Status:** Running

**Observations:**
- Migracja 15,000 dokumentów zajęła 45 minut
- **0 data loss** - wszystkie checksums matched ✅
- MongoDB storage: 210MB (PostgreSQL: 180MB) - overhead 16% (BSON format)
- Atlas Search index built automatically - 12 minut

**Actions taken:**
- Ran validation script: confirmed wszystkie documents accessible
- Tested sample queries - both DBs return identical results

---

### 2026-01-15 03:00 - First Benchmark Run (Search)

**Status:** Running

**Observations:**
- **PostgreSQL search (p95): 2.4s** (consistent z baseline)
- **MongoDB search (p95): 0.6s** ✅ **75% faster!**
- MongoDB Atlas Search używa Lucene - bardzo efektywne full-text
- Przy 50 concurrent users: MongoDB nadal <1s, PostgreSQL degraduje do 4.2s

**Surprising finding:**
- MongoDB memory usage stabilny (5.8GB), PostgreSQL spiked do 7.1GB pod load

**Actions taken:**
- Re-ran benchmark 3x dla confidence - wyniki consistent ±5%

---

### 2026-01-17 03:00 - Graph Benchmark Results

**Status:** Running

**Observations:**
- **PostgreSQL graph query (p95): 1.9s** (slightly worse than baseline - larger dataset)
- **MongoDB graph query (p95): 0.7s** ✅ **63% faster!**
- MongoDB aggregation pipeline very efficient dla graph traversal
- Deep traversal (5-hop): PostgreSQL 8.2s, MongoDB 2.1s (74% improvement)

**Technical insight:**
- MongoDB `$graphLookup` optimized dla recursive queries
- PostgreSQL recursive CTE jest wolniejsze dla deep graphs

---

### 2026-01-22 03:00 - Write Benchmark

**Status:** Running

**Observations:**
- **PostgreSQL insert+index: 485ms** (consistent z baseline)
- **MongoDB insert+index: 280ms** ✅ **42% faster!**
- MongoDB batch insert (100 docs): 18s total = 180ms/doc (even better!)
- Atlas Search index update async (nie blokuje write)

---

### 2026-01-28 - Anomalia wykryta

**Status:** Issue detected

**Observations:**
- Spike w MongoDB latency: 3.2s dla search query o 14:23 UTC
- Root cause: Atlas auto-scaling event (M30 → M40 transition test)
- Query wykonało się ponownie po 2s: 0.5s (normal)

**Actions taken:**
- Disabled auto-scaling dla czasu eksperymentu
- Re-ran affected benchmark suite
- **Decision:** Exclude outlier z analizy (infrastructure event, not DB performance)

---

### 2026-02-05 - Cost Analysis

**Status:** Running

**Observations:**
- **PostgreSQL actual cost (Jan 2026)**: $847/month (RDS + backups + I/O)
- **MongoDB Atlas cost (Jan 2026)**: $920/month (M30 + Search + backups)
- Delta: +$73/month (+8.6%) - **WITHIN BUDGET** ✅

**Breakdown:**
```
PostgreSQL:
- RDS t3.large: $620
- Storage (100GB): $120
- Backups: $75
- Data transfer: $32
Total: $847

MongoDB:
- Atlas M30: $760
- Atlas Search: $95
- Backups: $50
- Data transfer: $15
Total: $920
```

---

### 2026-02-12 - Stress Test

**Status:** Running

**Observations:**
- Tested 200 concurrent users (2x production peak)
- PostgreSQL: degraded severely, p95 > 10s, some timeouts
- MongoDB: p95 = 1.8s (degraded ale acceptable)
- MongoDB scaled better pod heavy load

**Implication:**
- MongoDB daje headroom dla wzrostu (important dla Q1 enterprise customers)

---

## SEC-EXP-DATA: Dane i metryki

### Raw Data

- **Benchmark results**: `/experiments/exp-001/results/` (CSV files)
- **JMeter logs**: S3 bucket `ishkarim-experiments/exp001/jmeter/`
- **Datadog dashboards**: [Link do Datadog](https://app.datadoghq.com/dashboard/exp-001)
- **Migration scripts**: GitHub `ishkarim/experiments` branch `exp-001-mongodb`

### Metryki zebrane

| Metryka | Baseline (PostgreSQL) | Experiment (MongoDB) | Delta | Target | Status |
|---------|----------|------------|-------|--------|--------|
| Search latency (p95) | 2.5s | 0.6s | **-76%** | <1.0s | ✅ |
| Graph query (p95) | 1.8s | 0.7s | **-61%** | <0.9s | ✅ |
| Document indexing | 500ms | 280ms | **-44%** | <300ms | ✅ |
| Concurrent throughput | 45 q/s | 78 q/s | **+73%** | >50 q/s | ✅ |
| Memory usage (avg) | 6.2GB | 5.8GB | **-6%** | <8GB | ✅ |
| Monthly cost | $847 | $920 | **+8.6%** | <$1,040 | ✅ |

**ALL SUCCESS CRITERIA MET!** 🎉

### Visualizations

**Search Latency Distribution:**
```
PostgreSQL p95: ████████████████████████ 2.5s
MongoDB p95:    ██████ 0.6s
                └─────────────────────────┘
                0s                      3s
```

**Graph Query Performance (by depth):**
```
Depth  PostgreSQL  MongoDB   Improvement
1-hop    0.8s       0.3s        63%
2-hop    1.2s       0.5s        58%
5-hop    8.2s       2.1s        74%
Full    12.5s       3.8s        70%
```

**Cost Comparison:**
```
Component         PostgreSQL  MongoDB   Delta
Compute              $620       $760     +23%
Storage              $120        $50     -58%
Search/Index           $0        $95      N/A
Backups               $75        $50     -33%
Data transfer         $32        $15     -53%
──────────────────────────────────────────────
TOTAL                $847       $920    +8.6%
```

---

## SEC-EXP-ANALYSIS: Analiza wyników

### Statistical Analysis

**Metoda:** Two-sample t-test (PostgreSQL vs MongoDB latencies)
**Confidence level:** 95%
**Sample size:** n=10,000 queries per benchmark
**p-value:** <0.0001 (highly significant)
**Significance:** **YES** - różnice są statystycznie istotne

**Effect size (Cohen's d):**
- Search: d=2.8 (very large effect)
- Graph: d=2.1 (very large effect)
- Indexing: d=1.6 (large effect)

### Interpretacja wyników

MongoDB demonstratively outperforms PostgreSQL dla wszystkich kluczowych metryk:

1. **Search performance:** 76% redukcja latency dzięki Lucene-based Atlas Search (vs PostgreSQL tsvector)
2. **Graph queries:** 61% poprawa dzięki optimized aggregation pipeline i `$graphLookup`
3. **Write performance:** 44% szybsze indexing - async index updates vs synchronous w PostgreSQL

**Root causes wydajności:**
- Document model naturalnie pasuje do Markdown content (no ORM overhead)
- Atlas Search professionally maintained (vs custom PostgreSQL FTS setup)
- MongoDB cache efficiency lepsze dla hot documents
- WiredTiger storage engine optimized dla document workloads

**Cost tradeoff:**
- MongoDB droższe o $73/mth (+8.6%) ale:
  - Performance gains justify cost (better UX = reduced churn)
  - Eliminuje potrzebę separate Elasticsearch ($300/mth rozważany wcześniej)
  - Managed service = reduced DevOps burden (value!)

### Correlation vs Causation

**Causation confirmed:**
- Kontrolowaliśmy wszystkie variables (hardware, network, dataset)
- Repeated experiments (3x runs) pokazują consistent results
- Różnice wynikają z DB engine design, nie external factors

**Not just correlation** - architectural properties MongoDB (document store, aggregation pipeline) są przyczyną performance gains.

### Threats to Validity

**Internal validity:**
- ✅ Dataset representative (production anonymized data)
- ✅ Load patterns realistic (based on prod traffic analysis)
- ⚠️ Staging environment nie ma prod traffic noise - może być optimistic

**External validity:**
- ✅ Results generalize do podobnych document management systems
- ⚠️ Specific do naszego use case (Markdown docs + graph) - może nie apply do innych workloads
- ✅ Dataset size (10K docs) jest typowy ale enterprise (50K+) needs validation

**Mitigation:**
- Plan pilot deployment na internal project (5K real docs) - see POC-DOC-001
- Monitoring przez 4 tygodnie w production-like environment

---

## SEC-EXP-CONCLUSION: Wnioski

### Wynik względem hipotezy

**Hipoteza H1:** Migracja z PostgreSQL na MongoDB poprawi wydajność search o 60%, graph queries o 50%, indexing o 40%.

**Verdict:** ✅ **POTWIERDZONA** - Dane silnie wspierają H1

### Success Criteria Assessment

- [x] Search <1.0s: ✅ **Achieved 0.6s** (-76% improvement, exceeded target)
- [x] Graph <0.9s: ✅ **Achieved 0.7s** (-61% improvement, exceeded target)
- [x] Indexing <300ms: ✅ **Achieved 280ms** (-44% improvement, met target)
- [x] Feature parity: ✅ **100% confirmed** (all queries produce identical results)
- [x] Uptime ≥99.5%: ✅ **99.9%** (only planned maintenance)
- [x] Cost <$1,040: ✅ **$920/mth** (within budget)
- [x] Zero data loss: ✅ **Confirmed** (checksums validated)

**7/7 criteria met!**

### Kluczowe odkrycia

1. **MongoDB Atlas Search >> PostgreSQL FTS** - professionally maintained Lucene index vs custom setup
2. **Graph performance surprise** - MongoDB aggregation pipeline lepsze niż expected (63% vs target 50%)
3. **Cost competitive** - MongoDB tylko +8.6% despite premium managed service
4. **Scalability headroom** - MongoDB handles 2x load better (important dla growth)
5. **Operational simplicity** - Atlas managed service reduces DevOps burden

### Niespodzianki

**Positive:**
- MongoDB memory usage NIŻSZE niż PostgreSQL (5.8GB vs 6.2GB) - unexpected!
- Batch writes w MongoDB exceptional (180ms/doc vs 280ms single) - optimize ingestion pipeline
- Atlas automatic index optimization - zero tuning needed

**Negative:**
- Storage overhead +16% (BSON format) - acceptable ale worth noting
- Migration complexity higher than estimated (schema transformation logic)

### Limitations

1. **Dataset size:** 10K documents - production może być 5x większe (needs pilot validation)
2. **Staging environment:** Nie uwzględnia production traffic patterns (real users behavior)
3. **Timeframe:** 6 tygodni testing - long-term performance unknowns (cache behavior, index bloat)
4. **MongoDB version:** 7.0 - future upgrades may change performance characteristics

---

## SEC-EXP-NEXT-STEPS: Kolejne kroki

### Immediate actions

- [x] **2026-02-14**: Present results do stakeholders - **COMPLETED** ✅
- [ ] **2026-02-17**: Create RESEARCH-FINDINGS-001 aggregating insights
- [ ] **2026-02-18**: Create ADR-042: Decision to migrate to MongoDB
- [ ] **2026-02-20**: Kick off POC-001: Pilot deployment na internal project

### Follow-up experiments

- [ ] **EXP-002**: Real-time collaboration performance with MongoDB Change Streams
- [ ] **EXP-003**: Sharding strategy dla 100K+ documents (enterprise scale)
- [ ] **EXP-004**: Backup/restore performance testing (disaster recovery)

### Documentation updates

- [x] Update HYPOTHESIS-001 status → validated ✅
- [ ] Create RESEARCH-FINDINGS-001 → comprehensive analysis
- [ ] Create ADR-042 → formal decision record
- [ ] Update TDD → MongoDB schema i data access layer design

### Recommendations

**Hipoteza potwierdzona → PROCEED z migracją:**

1. **Phase 1 - Pilot (4 weeks):**
   - Deploy MongoDB dla internal Ishkarim documentation (5K docs)
   - Monitor real-world performance, gather user feedback
   - Refine migration scripts i procedures

2. **Phase 2 - Migration Plan (2 weeks):**
   - Design zero-downtime migration strategy (dual-write mode)
   - Create rollback procedures
   - Prepare customer communication

3. **Phase 3 - Production Rollout (8 weeks):**
   - Gradual customer migration (1 project at a time)
   - 24/7 monitoring i support
   - Performance validation per customer

4. **Phase 4 - Optimization (ongoing):**
   - Fine-tune indexes based on production query patterns
   - Implement batch write optimizations
   - Scale infrastructure as usage grows

**Budget request:** $65,000 dla full migration (12 weeks, 2 developers + DevOps)

---

## EVIDENCE: Dowody i artefakty

### Artifacts generated

- **Benchmark raw data**: `/experiments/exp-001/results/*.csv` (150MB)
- **JMeter test plans**: `/experiments/exp-001/jmeter/*.jmx`
- **Migration scripts**: GitHub `ishkarim/experiments` branch `exp-001-mongodb`
- **Analysis notebook**: Jupyter notebook z statistical analysis
- **Datadog dashboards**: Saved snapshots (PDF) w `/experiments/exp-001/monitoring/`

### Screenshots/Recordings

- **Datadog dashboard snapshot** (2026-01-15): Search performance comparison
  ![Search Performance](../artifacts/exp-001-search-perf.png)

- **JMeter results graph**: Load test 50 concurrent users
  ![Load Test](../artifacts/exp-001-load-test.png)

- **MongoDB Compass**: Document model visualization
  ![Schema](../artifacts/exp-001-schema.png)

### Code/Scripts

**Repository:** https://github.com/ishkarim/experiments
**Branch:** `exp-001-mongodb`
**Key commits:**
- `a3f7c21`: Initial MongoDB schema design
- `b8e4d55`: Data migration script (PostgreSQL → MongoDB)
- `c9a1e88`: JMeter benchmark suite
- `d2f3b99`: Results analysis scripts

**Key files:**
- `migrate_pg_to_mongo.py`: Migration script (500 LOC)
- `benchmark_search.jmx`: JMeter search test plan
- `benchmark_graph.jmx`: JMeter graph query test plan
- `analyze_results.ipynb`: Jupyter notebook z analysis

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| 2026-01-06 | 1.0 | Jan Kowalski | Eksperyment rozpoczęty, setup complete |
| 2026-01-10 | 1.1 | Jan Kowalski | Data migration complete, initial observations |
| 2026-01-20 | 1.5 | Jan Kowalski | All benchmarks executed, preliminary results |
| 2026-02-05 | 1.8 | Jan Kowalski | Cost analysis added, stress testing complete |
| 2026-02-14 | 2.0 | Jan Kowalski | Final analysis, conclusions, hipoteza POTWIERDZONA |

---

## Notatki i uwagi

### Lessons Learned

1. **Schema design matters:** Document model design took 3 iterations - invest time upfront
2. **Atlas Search is magic:** Zero-config full-text search - huge productivity boost vs DIY PostgreSQL FTS
3. **Aggregation pipeline learning curve:** Steep ale worth it - bardzo powerful
4. **Migration scripts testing:** Spent 40% of time on data validation - essential dla zero data loss

### Team Feedback

**Piotr (Backend Dev):**
> "MongoDB aggregation pipeline jest jak SQL + programming combined. Initial learning curve ale bardzo ekspresywne dla complex queries. Graph traversal kod jest czytelniejszy niż recursive PostgreSQL CTEs."

**Kasia (DevOps):**
> "Atlas managed service = life changer. No więcej PostgreSQL tuning, index bloat monitoring, vacuum jobs. Backups automated, monitoring built-in. DevOps burden drastically reduced."

**Anna (Product Owner):**
> "Performance numbers speak for themselves. Search <1s to user delight. Worth the migration effort 100%. Let's proceed!"

### Risks dla production migration

1. **Migration downtime:** Dual-write strategy adds complexity - needs careful planning
2. **Team MongoDB expertise:** 2/5 developers new to MongoDB - training investment needed
3. **Unknown production patterns:** Staging może nie capture all edge cases - pilot critical
4. **Vendor lock-in:** Atlas-specific features (Search) - mitigation: abstrakcja warstwa

**Overall confidence:** HIGH - data overwhelmingly supports migration. Proceed with pilot!

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation
