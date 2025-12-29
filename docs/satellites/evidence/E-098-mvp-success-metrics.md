---
id: E-098
title: "Definicja Metryk Sukcesu MVP"
type: evidence
evidence_type: requirement
date: 2025-12-26

related_documents:
  - ROADMAP-001
  - TEST-PLAN-001
  - PRD-001-V2

source:
  type: internal_analysis
  date_collected: 2025-12-26
---

# Definicja Metryk Sukcesu MVP

## Kontekst
Określenie mierzalnych kryteriów sukcesu dla MVP Ishkarim (Q1-Q2 2026). Metryki obejmują performance, functionality, user adoption, i quality. Służą jako objective go/no-go criteria dla public release.

## Metodologia

### Framework: SMART Goals
- **Specific**: Konkretne, jednoznaczne metryki
- **Measurable**: Quantifiable (liczby, %)
- **Achievable**: Realistic given resources
- **Relevant**: Aligned z business goals
- **Time-bound**: Deadline: Koniec Q2 2026

### Kategorie Metryk
1. **Technical Performance**: Speed, scalability, reliability
2. **Functional Completeness**: Feature delivery
3. **User Adoption**: Active users, engagement
4. **Quality**: Bugs, stability, UX
5. **Business Viability**: Willingness to pay, retention

## Wyniki

### Technical Performance Metrics

---

#### **TP-001: Parse Speed (<5s dla 100 docs)**
**Definition**: Czas parsowania 100 YAML documents (average size 2KB each) must be <5 sekund

**Measurement**:
```python
# Benchmark test
import time
start = time.time()
parser.parse_directory("./test_docs_100/")
elapsed = time.time() - start
assert elapsed < 5.0, f"Parse too slow: {elapsed}s"
```

**Target**: <5s (mean), <10s (p99)

**Rationale**: User interviews (E-081) - technical writer manages ~150 docs. Parse on load must be fast (not blocking UI).

**Status Tracking**: Automated test w CI/CD (GitHub Actions)

**Baseline**: Current estimate 2-3s dla 100 docs (based on prototype)

**Success Criteria**: ✅ Pass if <5s average across 10 runs

---

#### **TP-002: Graph Rendering (<2s dla 500 nodes)**
**Definition**: Czas renderowania grafu z 500 nodes + 1000 edges must be <2 sekundy (from click "Show Graph" to visible on screen)

**Measurement**:
```python
# Qt performance test
start = time.perf_counter()
graph_widget.render(nodes=500, edges=1000)
QApplication.processEvents()  # Force UI update
elapsed = time.perf_counter() - start
assert elapsed < 2.0
```

**Target**: <2s (mean), <5s (p95)

**Rationale**: User experience - graph visualization jest core feature. Slow rendering = frustrated users.

**Status Tracking**: Manual testing + automated benchmark (M5)

**Success Criteria**: ✅ Pass if <2s dla 500 nodes, <5s dla 1000 nodes

---

#### **TP-003: Memory Usage (<500MB dla 1000 docs)**
**Definition**: Peak RAM usage when loading 1000 documents + graph must be <500MB

**Measurement**:
```python
import psutil
process = psutil.Process()
parser.parse_directory("./test_docs_1000/")
graph_widget.render(nodes=1000, edges=2000)
mem_mb = process.memory_info().rss / 1024 / 1024
assert mem_mb < 500, f"Memory too high: {mem_mb}MB"
```

**Target**: <500MB (1000 docs), <100MB (100 docs)

**Rationale**: Desktop app must be lightweight (nie Chrome-like bloat). Users z laptops (8GB RAM) should run smoothly.

**Status Tracking**: Automated memory profiling (M5)

**Success Criteria**: ✅ Pass if <500MB dla 1000 docs

---

#### **TP-004: Search Latency (<200ms dla FTS query)**
**Definition**: Full-text search response time (query → results displayed) must be <200ms dla 500 docs indexed

**Measurement**:
```python
# SQLite FTS5 benchmark
start = time.perf_counter()
results = search_engine.query("gap detection")
elapsed = time.perf_counter() - start
assert elapsed < 0.2, f"Search slow: {elapsed*1000}ms"
```

**Target**: <200ms (mean), <500ms (p95)

**Rationale**: Search must feel instant (Google-like). >500ms = noticeable lag.

**Status Tracking**: Automated test w CI/CD

**Success Criteria**: ✅ Pass if <200ms average, <500ms p95

---

### Functional Completeness Metrics

---

#### **FC-001: MVP Feature Delivery (10/10 features)**
**Definition**: All 10 MVP features (E-085) delivered and functional by end Q2 2026

**Features (Top 10 from E-085)**:
1. ✅ FR-010: Parser YAML + relacje
2. ✅ FR-020: Gap detection engine
3. ✅ FR-011: Graf wizualizacja (NetworkX)
4. ✅ FR-040: Quality gates
5. ✅ FR-080: Completeness tracking (%)
6. ✅ FR-050: File watcher (auto-reload)
7. ✅ FR-060: Search FTS5 (SQLite)
8. ✅ FR-030: Proof system (validate evidence)
9. ✅ FR-070: Export HTML/PDF reports
10. ✅ FR-012: GUI Qt (PySide6)

**Measurement**: Binary checklist (feature exists + passes functional tests)

**Success Criteria**: ✅ 10/10 features delivered (100%)

**Fallback**: Minimum 8/10 (80%) dla RC release (defer 2 features to post-MVP)

---

#### **FC-002: Gap Detection Accuracy (>80%)**
**Definition**: Gap detection engine correctly identifies missing documents/sections

**Test Set**: 50 synthetic doc sets (25 complete, 25 with intentional gaps)
- True Positives (TP): Correctly identified gaps
- False Positives (FP): Incorrectly flagged as gap
- False Negatives (FN): Missed actual gaps

**Metrics**:
- **Precision**: TP / (TP + FP) > 80% (low false alarms)
- **Recall**: TP / (TP + FN) > 80% (catch most gaps)
- **F1 Score**: 2 × (Precision × Recall) / (Precision + Recall) > 80%

**Measurement**:
```python
# Evaluation script
gaps_expected = load_test_cases()
gaps_detected = gap_detector.find_gaps(docs)
precision = calculate_precision(gaps_detected, gaps_expected)
recall = calculate_recall(gaps_detected, gaps_expected)
assert precision > 0.8 and recall > 0.8
```

**Success Criteria**: ✅ F1 score >80% (good balance precision/recall)

**Rationale**: Core value prop - gap detection must be accurate (nie too noisy, nie missing real gaps)

---

#### **FC-003: Dependency Tracking (Bidirectional Links)**
**Definition**: All document relationships (supports/requires/contradicts) correctly parsed and visualized

**Test**:
- Create 20 docs with explicit `supports: [DOC-A]` relations
- Verify: Forward links (DOC-B supports DOC-A) + backlinks (DOC-A supported_by DOC-B)
- Measure: 100% relations correctly parsed

**Success Criteria**: ✅ 100% bidirectional links correct (zero errors)

---

### User Adoption Metrics

---

#### **UA-001: Beta User Acquisition (50+ RC users)**
**Definition**: Recruit 50+ users dla Release Candidate testing (M6)

**Milestones**:
- M2 (Alpha): 5 users
- M4 (Beta): 20 users
- M6 (RC): 50 users

**Channels**:
- Reddit (r/productivity, r/technicalwriting): 20 users
- LinkedIn outreach: 15 users
- Product Hunt "Coming Soon": 10 users
- Personal network: 5 users

**Measurement**: User sign-ups w Google Sheet / database

**Success Criteria**: ✅ 50+ users signed up by end M6

**Fallback**: Minimum 30 users (still valid for feedback)

---

#### **UA-002: Active User Rate (60%+ D7 retention)**
**Definition**: % users active 7 days after first use (Day 7 retention)

**Measurement**:
```python
# Analytics tracking
cohort_week1 = users_signed_up(week=1)
active_day7 = users_active_on_day(cohort=cohort_week1, day=7)
retention_d7 = active_day7 / cohort_week1
assert retention_d7 > 0.6
```

**Target**: >60% D7 retention (good dla B2B tool)

**Rationale**: High retention = product stickiness. <40% = warning sign (no PMF).

**Success Criteria**: ✅ D7 retention >60% (averaged across M4-M6 cohorts)

---

#### **UA-003: User Engagement (3+ sessions/week)**
**Definition**: Active users open Ishkarim 3+ times per week (average)

**Measurement**: Session tracking (desktop app telemetry)

**Target**: Mean 3 sessions/week, median 2 sessions/week

**Rationale**: Docs tool should be daily/weekly habit (not one-time use)

**Success Criteria**: ✅ >50% users have 3+ sessions/week

---

### Quality Metrics

---

#### **QA-001: Critical Bugs (Zero P0 bugs in production)**
**Definition**: No showstopper bugs (crashes, data loss, security vulnerabilities) w RC release

**Bug Severity**:
- **P0** (Critical): App crashes, data loss, security hole → Block release
- **P1** (High): Core feature broken → Fix before release
- **P2** (Medium): Minor feature broken → OK to release, fix in patch
- **P3** (Low): UI glitch → Defer to post-MVP

**Measurement**: Bug tracker (GitHub Issues)

**Success Criteria**: ✅ Zero P0 bugs, <5 P1 bugs at RC launch

---

#### **QA-002: Test Coverage (>70% code coverage)**
**Definition**: Unit + integration tests cover >70% of codebase (Python)

**Measurement**:
```bash
pytest --cov=ishkarim --cov-report=term
# Coverage report: 72%
```

**Target**: >70% (good dla MVP), >80% (ideal dla post-MVP)

**Rationale**: High coverage = fewer regressions, easier refactoring

**Success Criteria**: ✅ Coverage >70% (measured via pytest-cov)

---

#### **QA-003: User Satisfaction (NPS >30)**
**Definition**: Net Promoter Score >30 (good dla new product)

**NPS Calculation**:
- Survey RC users (M6): "How likely are you to recommend Ishkarim? (0-10)"
- **Promoters** (9-10): Count as +1
- **Passives** (7-8): Count as 0
- **Detractors** (0-6): Count as -1
- **NPS** = (% Promoters - % Detractors)

**Target**: NPS >30 (good), >50 (excellent)

**Measurement**: Email survey (SurveyMonkey) sent to 50 RC users

**Success Criteria**: ✅ NPS >30 (at least 30% more promoters than detractors)

---

### Business Viability Metrics

---

#### **BV-001: Willingness to Pay (>40% conversion intent)**
**Definition**: % RC users who say "I would pay $10/month for this" (intent, not actual payment)

**Measurement**: Survey question during RC testing
- "If Ishkarim cost $10/month, would you pay?" (Yes/No/Maybe)
- **Conversion intent** = (Yes + 50% Maybe) / Total

**Target**: >40% intent (strong signal dla paid product viability)

**Rationale**: MVP is free, but need validation users willing to pay post-launch

**Success Criteria**: ✅ >40% users say yes/maybe to paying

**Benchmark**: SaaS tools typically see 20-30% free→paid conversion (40% intent = promising)

---

#### **BV-002: Feature Value Ranking (Gap detection in Top 3)**
**Definition**: Users rank "most valuable feature" - gap detection must be Top 3

**Measurement**: Survey (M6)
- "Rank these features by value (1=most valuable):
  - Gap detection
  - Graf visualization
  - Quality gates
  - Proof system
  - Completeness tracking
  - Search
  - Export

**Success Criteria**: ✅ Gap detection ranked Top 3 by >60% users

**Rationale**: Validates core value prop (gap detection = differentiator)

---

## Implikacje

### Go/No-Go Decision (End Q2 2026)

**GO criteria** (launch public 1.0):
- ✅ All technical performance metrics met (TP-001 to TP-004)
- ✅ 8/10 MVP features delivered (FC-001)
- ✅ Gap detection accuracy >80% (FC-002)
- ✅ 50+ RC users (UA-001)
- ✅ D7 retention >60% (UA-002)
- ✅ Zero P0 bugs (QA-001)
- ✅ NPS >30 (QA-003)
- ✅ Willingness to pay >40% (BV-001)

**NO-GO criteria** (delay or pivot):
- ❌ <6/10 features delivered (scope too ambitious)
- ❌ Gap detection accuracy <60% (core feature broken)
- ❌ D7 retention <40% (no engagement)
- ❌ NPS <10 (users hate it)
- ❌ Willingness to pay <20% (no business model)

**PIVOT criteria** (re-evaluate direction):
- ⚠️ Features delivered but low adoption (<30 RC users)
- ⚠️ High engagement but wrong features valued (gap detection not Top 3)
- ⚠️ Good product but wrong pricing (willing to pay, but not $10/month)

### Tracking Dashboard (Weekly Updates)

**M1-M2 (Alpha)**:
- TP-001 (parse speed): Track weekly
- FC-001 (feature delivery): 4/10 features done (40% progress expected)

**M3-M4 (Beta)**:
- TP-002 (graph rendering): Benchmark at M4
- UA-001 (user acquisition): 20 users recruited
- UA-002 (retention): Track D7 cohorts

**M5-M6 (RC)**:
- All TP metrics: Final benchmarks
- All UA metrics: Final cohort analysis
- QA-001/002/003: Pre-launch quality checks
- BV-001/002: User surveys (M6)

**Final Review** (End M6):
- Aggregate all metrics → Go/No-Go decision
- Present to stakeholders (founder + advisors)
- Public launch or defer to Q3

## Dane Raw

### Benchmark - Competitor Performance

| Metric | Confluence | Notion | Obsidian | **Ishkarim Target** |
|--------|------------|--------|----------|---------------------|
| Parse 100 docs | ~10s (slow) | N/A (cloud) | <1s (local files) | **<5s** |
| Graph render (500 nodes) | N/A | N/A | ~3s | **<2s** |
| Search latency | ~1s (slow) | <100ms (cloud) | <50ms (local) | **<200ms** |
| Memory (1000 docs) | ~800MB | N/A (cloud) | ~200MB | **<500MB** |

**Ishkarim positioning**: Faster than Confluence, slower than Obsidian (acceptable trade-off dla semantic features)

### User Research - Feature Value (from E-081/082/083)

**Most valued features** (ranked by users):
1. **Gap detection** (3/3 users mentioned as #1 pain point)
2. **Dependency graph** (3/3 users mentioned)
3. **Quality gates** (2/3 users - compliance-focused)
4. Completeness tracking (2/3 users)
5. Proof system (1/3 users - niche)

**Validation**: Gap detection + Graph must be Top 2 in BV-002 ranking

### NPS Benchmarks (SaaS Tools 2024)

| Tool | NPS | Category |
|------|-----|----------|
| Notion | 68 | Excellent (viral growth) |
| Confluence | 12 | Poor (enterprise lock-in) |
| Obsidian | 52 | Good (community love) |
| Roam Research | 38 | Good (cult following) |
| **Ishkarim Target** | **>30** | Good (realistic dla MVP) |

**Rationale**: NPS >30 puts Ishkarim above Confluence, below Obsidian (reasonable dla niche tool)

### Success Metrics Summary Table

| ID | Metric | Target | Measurement Method | **Status** |
|----|--------|--------|--------------------|-----------:|
| TP-001 | Parse speed | <5s (100 docs) | Automated benchmark | TBD (M5) |
| TP-002 | Graph render | <2s (500 nodes) | Manual + automated test | TBD (M5) |
| TP-003 | Memory usage | <500MB (1000 docs) | psutil profiling | TBD (M5) |
| TP-004 | Search latency | <200ms | Automated benchmark | TBD (M5) |
| FC-001 | Feature delivery | 10/10 features | Checklist | TBD (M6) |
| FC-002 | Gap accuracy | >80% F1 | Test set evaluation | TBD (M6) |
| FC-003 | Dependency tracking | 100% correct | Unit tests | TBD (M4) |
| UA-001 | User acquisition | 50+ RC users | Sign-up tracker | TBD (M6) |
| UA-002 | D7 retention | >60% | Analytics | TBD (M6) |
| UA-003 | Engagement | 3+ sessions/week | Telemetry | TBD (M6) |
| QA-001 | Critical bugs | 0 P0 bugs | Bug tracker | TBD (M6) |
| QA-002 | Test coverage | >70% | pytest-cov | TBD (M6) |
| QA-003 | NPS | >30 | User survey | TBD (M6) |
| BV-001 | Willingness to pay | >40% | User survey | TBD (M6) |
| BV-002 | Feature value | Gap in Top 3 | User ranking survey | TBD (M6) |

**Total metrics**: 15 (comprehensive coverage technical/user/business)
