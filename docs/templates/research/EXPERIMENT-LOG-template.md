# EXPERIMENT-LOG: Experiment Log Template

---
**Meta (WYMAGANE):**
```yaml
id: EXPERIMENT-XXX
doctype: EXPERIMENT-LOG
status: draft  # draft | running | completed | failed | abandoned
version: "1.0"
owner: "[Imię Nazwisko (Rola)]"
project: "[Nazwa projektu]"
experiment_id: "[Unique ID eksperymentu]"
hypothesis_id: "[HYPOTHESIS-XXX - link do hipotezy]"
experiment_type: technical  # technical | business | ux | clinical | market
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [HYPOTHESIS-XXX]
    type: requires
    reason: "Eksperyment waliduje konkretną hipotezę"

impacts:
  - id: [DOC-ID]
    type: [blocks | informs | influences]
    reason: "[Wyniki wpływają na następne decyzje/dokumenty]"
```

---

## SEC-EXP-HYPOTHESIS: Link do hipotezy

**Hipoteza:** [HYPOTHESIS-XXX]

**Pytanie badawcze:**
[Przepisz pytanie badawcze z hipotezy - co chcemy udowodnić?]

**Success criteria (z hipotezy):**
[Lista kryteriów sukcesu - przepisz z HYPOTHESIS-DOC]
- [ ] [Kryterium 1]
- [ ] [Kryterium 2]
- [ ] [Kryterium 3]

---

## SEC-EXP-SETUP: Setup eksperymentu

### Environment
**Test environment:**
- **Platform:** [Np. "AWS t3.medium", "Local dev machine", "Staging environment"]
- **Database:** [Np. "MongoDB 7.0", "PostgreSQL 15", "MySQL 8.0"]
- **Dataset:** [Np. "1M records, realistic production data"]
- **Tools:** [Np. "Apache JMeter", "Postman", "Custom benchmark script"]

### Configuration
**Parametry eksperymentu:**
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| [Param 1] | [Value] | [Dlaczego ta wartość] |
| [Param 2] | [Value] | [Dlaczego ta wartość] |

**Przykład:**
```
| Parameter | Value | Rationale |
| Query timeout | 5 seconds | Realistic production timeout |
| Concurrent users | 100 | Peak production load |
| Dataset size | 1M records | Representative sample |
```

### Baseline (Control Group)
**Baseline measurement:**
- **Technology:** [Current/control technology - np. "PostgreSQL"]
- **Performance baseline:** [Metryki baseline - np. "150ms query latency, 2GB RAM"]
- **Cost baseline:** [Koszt baseline - np. "$300/month"]

---

## SEC-EXP-PROCEDURE: Procedura wykonania

### Protokół eksperymentu
**Kroki wykonania (checklist):**
- [ ] **Step 1:** [Przygotowanie environment]
- [ ] **Step 2:** [Load dataset]
- [ ] **Step 3:** [Uruchomienie benchmark]
- [ ] **Step 4:** [Collect metrics]
- [ ] **Step 5:** [Repeat N times dla statistical significance]

### Powtórzenia
- **Liczba iteracji:** [Np. "3 runs", "10 samples"]
- **Interval:** [Jak często? Np. "Co 5 minut", "Daily"]
- **Aggregation:** [Jak agregujemy wyniki? Np. "Average", "Median", "P95"]

### Data collection plan
**Metryki do zebrania:**
| Metric | Unit | Collection method | Expected range |
|--------|------|-------------------|----------------|
| [Metric 1] | [ms/MB/etc] | [Tool/script] | [Min-Max] |
| [Metric 2] | [Unit] | [Tool] | [Min-Max] |

**Przykład:**
```
| Metric | Unit | Collection method | Expected range |
| Query latency | ms | JMeter reports | 50-200ms |
| Memory usage | MB | CloudWatch | 1-4 GB |
| Error rate | % | Application logs | 0-5% |
```

---

## SEC-EXP-OBSERVATIONS: Obserwacje (timestamped)

**Format:** Timestamped log entries (chronological order)

---

### [YYYY-MM-DD HH:MM] - [Tytuł wydarzenia]
**Context:** [Co się dzieje w tym momencie eksperymentu]

**Observation:**
[Szczegółowy opis obserwacji - co zobaczyłeś, co zmierzyłeś]

**Data points:**
- [Metric 1]: [Value] (baseline: [Value]) → [% change]
- [Metric 2]: [Value] (baseline: [Value]) → [% change]

**Status:**
- ✅ Expected / ⚠️ Anomaly / ❌ Failure

**Actions taken:**
- [Co zrobiłeś w odpowiedzi na tę obserwację]

---

### Przykład obserwacji:

---

### 2025-12-27 10:00 - Rozpoczęcie eksperymentu
**Context:** Pierwszy benchmark run z MongoDB 7.0, dataset 1M records

**Observation:**
Setup completed successfully. Environment ready dla baseline measurement.

**Data points:**
- MongoDB version: 7.0.5
- Dataset loaded: 1,000,000 records
- Index created: compound index on (userId, timestamp)

**Status:** ✅ Expected

**Actions taken:**
- Verified data integrity (random sample check)
- Started baseline measurements

---

### 2025-12-27 10:15 - Pierwszy benchmark (Query A)
**Context:** Testing główny query pattern (user timeline query)

**Observation:**
Query A wykonał się znacznie szybciej niż expected!

**Data points:**
- Query A latency: **45ms** (baseline PostgreSQL: 150ms) → ✅ **-70% (HUGE WIN!)**
- P95 latency: 62ms (baseline: 180ms) → ✅ -65%
- Memory usage: 1.2GB (baseline: 1.5GB) → ✅ -20%

**Status:** ✅ Expected (actually better than expected!)

**Actions taken:**
- Repeated measurement 3× dla confidence
- All 3 runs: 43ms, 45ms, 47ms (consistent!)

---

### 2025-12-27 10:30 - Drugi benchmark (Query B)
**Context:** Testing aggregation query

**Observation:**
Query B pokazuje mixed results - wolniejsze niż expected.

**Data points:**
- Query B latency: **120ms** (baseline: 140ms) → ⚠️ **-14% (below 30% target)**
- P95 latency: 185ms (baseline: 200ms) → ⚠️ -7.5%

**Status:** ⚠️ Anomaly (nie spełnia success criteria 30%+ improvement)

**Actions taken:**
- Analyzed query execution plan
- Discovered: Index nie jest used efficiently
- **Decision:** Test alternative indexing strategy

---

### 2025-12-27 11:00 - Anomalia wykryta
**Context:** Concurrent load testing (100 simultaneous queries)

**Observation:**
Query B znacznie wolniejsze przy concurrent load - MAJOR ISSUE!

**Data points:**
- Query B latency (concurrent): **350ms** (baseline: 140ms) → ❌ **+150% WORSE!**
- Connection pool exhaustion: 95/100 connections used
- Error rate: 3.2% (timeout errors)

**Status:** ❌ Failure (hipoteza może być invalid)

**Actions taken:**
- Increased connection pool size: 100 → 200
- Re-run test z new config
- **BLOCKER:** Requires architecture review

---

### 2025-12-27 14:00 - Po optymalizacji
**Context:** Testing po zwiększeniu connection pool + index tuning

**Observation:**
Query B improved significantly po zmianach.

**Data points:**
- Query B latency (concurrent): **95ms** (baseline: 140ms) → ✅ -32%
- Error rate: 0.1% (acceptable)

**Status:** ✅ Expected (po mitigation)

**Actions taken:**
- Documented tuning steps
- Updated configuration recommendations

---

**[DODAJ WIĘCEJ OBSERWACJI W MIARĘ POSTĘPU EKSPERYMENTU]**

---

## SEC-EXP-DATA: Dane i metryki

### Zebrane dane (summary table)

| Run | Date | Query A (ms) | Query B (ms) | Memory (GB) | Error Rate (%) | Notes |
|-----|------|--------------|--------------|-------------|----------------|-------|
| 1 | 2025-12-27 | 45 | 120 | 1.2 | 0.0 | Baseline |
| 2 | 2025-12-27 | 43 | 350 | 1.5 | 3.2 | Concurrent load issue |
| 3 | 2025-12-27 | 47 | 95 | 1.3 | 0.1 | Po tuning |
| **AVG** | - | **45** | **188** | **1.3** | **1.1** | - |

### Statistical analysis
**Query A:**
- Mean: 45ms
- Median: 45ms
- Std deviation: 2ms
- **Conclusion:** ✅ Consistent, reliable, 70% improvement vs baseline

**Query B:**
- Mean: 188ms (after averaging all runs including anomaly)
- Median: 95ms (po tuning)
- **Conclusion:** ⚠️ Mixed - good after tuning, ale wymaga careful configuration

### Raw data location
**Artifacts:**
- Benchmark logs: `/experiments/EXPERIMENT-XXX/logs/`
- Performance charts: `/experiments/EXPERIMENT-XXX/charts/`
- Configuration files: `/experiments/EXPERIMENT-XXX/config/`

---

## SEC-EXP-ANALYSIS: Analiza wyników

### Kryteria sukcesu - weryfikacja

**Sprawdzenie success criteria z hipotezy:**

| Kryterium | Target | Actual | Status | Notes |
|-----------|--------|--------|--------|-------|
| Query A latency | <100ms | 45ms | ✅ PASS | 70% improvement |
| Query B latency | <100ms | 95ms | ✅ PASS | But requires tuning |
| Memory usage | <2GB | 1.3GB | ✅ PASS | 20% reduction |
| Error rate | <1% | 0.1% | ✅ PASS | After connection pool tuning |
| Cost increase | <20% | +15% | ✅ PASS | MongoDB $350/mo vs PostgreSQL $300/mo |

**Overall:** ✅ **4/5 criteria PASSED** (80% success rate)

### Findings kluczowe
1. **Query A performance:** ✅ Massive win (70% improvement)
2. **Query B performance:** ⚠️ Requires careful configuration (connection pooling, indexing)
3. **Scalability:** ❌ Discovered issue przy concurrent load - MITIGATED po tuning
4. **Cost:** ✅ Within acceptable range (+15%)

### Niespodzianki
**Positive surprises:**
- Query A był **LEPSZY niż expected** (45ms vs target 100ms)
- Memory usage reduced (1.3GB vs baseline 1.5GB)

**Negative surprises:**
- Query B przy concurrent load był **GORSZY niż baseline** przed tuning
- Connection pool exhaustion - nie było przewidywane w hipotezie

### Edge cases
**Zidentyfikowane edge cases:**
1. Concurrent load >100 users → requires connection pool tuning
2. Index strategy ma huge impact na Query B performance
3. Aggregation queries wolniejsze - nie było testowane w hipotezie

---

## SEC-EXP-CONCLUSION: Wnioski

### Hipoteza - verdict
**Status hipotezy:** ✅ **POTWIERDZONA z warunkami**

**Uzasadnienie:**
- H1: "MongoDB poprawi wydajność o min. 30% dla query pattern X"
- **Result:** Query A: ✅ 70% improvement, Query B: ✅ 32% improvement (po tuning)
- **Verdict:** Hipoteza potwierdzona, ALE wymaga proper configuration

### Learnings
**Kluczowe wnioski:**
1. MongoDB delivers na performance dla read-heavy queries (Query A)
2. **CRITICAL:** Concurrent load wymaga larger connection pool niż default
3. **CRITICAL:** Index strategy must be carefully designed dla aggregation queries
4. Cost increase (+15%) jest acceptable dla tego gain

### Implications dla projektu
**Wpływ na projekt:**
- ✅ **Proceed z MongoDB** - ale nie blindly
- ⚠️ **Configuration kluczowa** - nie używaj default settings w production
- ⚠️ **Team training** - MongoDB expertise gap (zespół zna PostgreSQL, nie MongoDB)

---

## SEC-EXP-NEXT-STEPS: Kolejne kroki

### Immediate actions
- [ ] **Utworzyć RESEARCH-FINDINGS document** - agregacja tego eksperymentu + inne - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] **Utworzyć POC-DOC** - pełny PoC w production-like environment - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]
- [ ] **Utworzyć ADR** - formalna decyzja czy adoptować MongoDB - **Owner:** [Imię] - **Due:** [YYYY-MM-DD]

### Follow-up experiments (jeśli potrzebne)
- [ ] **Experiment 2:** Test MongoDB z 10M records (realistic production size) - **Due:** [YYYY-MM-DD]
- [ ] **Experiment 3:** Test failover/replication scenarios - **Due:** [YYYY-MM-DD]

### Documentation
- [ ] Update configuration guide z tuning recommendations
- [ ] Create migration plan (PostgreSQL → MongoDB)

---

## EVIDENCE Satellite (WYMAGANE)

**Artifacts z eksperymentu:**
- E-XXX: Benchmark raw data (CSV/JSON)
- E-XXX: Performance charts (query latency graphs)
- E-XXX: Configuration files (MongoDB config, benchmark scripts)
- E-XXX: Error logs (connection pool exhaustion incidents)

---

## CHANGELOG (WYMAGANE)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-12-27 10:00 | [Imię Nazwisko] | Experiment started |
| 1.1 | 2025-12-27 11:00 | [Imię Nazwisko] | Anomalia wykryta - concurrent load issue |
| 1.2 | 2025-12-27 14:00 | [Imię Nazwisko] | Po tuning - wyniki improved |
| 2.0 | 2025-12-27 16:00 | [Imię Nazwisko] | Experiment completed - hipoteza potwierdzona |

---

**Czas wypełnienia:** Continuous (tracking throughout experiment)
**Template version:** EXPERIMENT-LOG v1.0
**Ostatnia aktualizacja:** 2025-12-29
