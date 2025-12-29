---
id: E-092
title: "Macierz Oceny Ryzyka"
type: evidence
evidence_type: analysis
date: 2025-12-26

related_documents:
  - BIZ-CASE-001-V2
  - ROADMAP-001

source:
  type: internal_analysis
  date_collected: 2025-12-26
---

# Macierz Oceny Ryzyka

## Kontekst
Systematyczna ocena ryzyk projektu Ishkarim w celu proaktywnej identyfikacji zagrożeń i opracowania strategii mitigation. Analiza obejmuje ryzyka techniczne, biznesowe, operacyjne i rynkowe.

## Metodologia

### Framework Oceny Ryzyka
**Scoring**:
- **Likelihood** (prawdopodobieństwo): 1-5 (1=bardzo rzadkie, 5=prawie pewne)
- **Impact** (wpływ): 1-5 (1=minimalny, 5=katastrofalny)
- **Risk Score** = Likelihood × Impact (max 25)

**Priorytety**:
- **Critical** (score 15-25): Immediate action required
- **High** (score 10-14): Active monitoring + mitigation plan
- **Medium** (score 5-9): Periodic review
- **Low** (score 1-4): Accept risk

### Kategorie Ryzyka
1. **Technical**: Technology, architecture, performance
2. **Business**: Market, competition, revenue
3. **Operational**: Team, timeline, resources
4. **Legal/Compliance**: Licensing, IP, regulations

## Wyniki

### Risk Register - 8 Top Risks

---

#### **RISK-001: Performance Degradation (Large Graphs)**
**Kategoria**: Technical

**Opis**:
Graf visualization z NetworkX może być wolny dla >1,000 nodes. Qt rendering może freeze UI przy complex layouts. User experience degraduje dla large documentation sets.

**Likelihood**: 4/5 (High - inevitable dla enterprise users z 500+ docs)

**Impact**: 4/5 (High - core feature unusable)

**Risk Score**: **16 (Critical)**

**Mitigation Strategies**:
1. **Pagination/Filtering** (Short-term):
   - Show only subgraph (1-hop neighbors) by default
   - Filter by document type, date range
   - Lazy loading (render only visible nodes)

2. **Performance Optimization** (Mid-term):
   - Use ForceAtlas2 layout (faster than Fruchterman-Reingold)
   - Offload layout calculation to background thread (QThread)
   - Cache layout positions (SQLite)

3. **Alternative Visualization** (Long-term):
   - WebGL-based graph (three.js, sigma.js) instead Qt native
   - Level-of-detail rendering (simplified nodes when zoomed out)
   - Clustering (collapse related nodes into meta-nodes)

4. **Benchmarking** (Immediate):
   - Test dengan 100, 500, 1000, 5000 nodes
   - Define performance SLA: <2s render dla 500 nodes
   - Fail early jeśli SLA nie met

**Residual Risk**: Medium (with mitigation)

**Owner**: Tech Lead

---

#### **RISK-002: Qt/PySide6 Licensing Confusion**
**Kategoria**: Legal/Compliance

**Opis**:
PySide6 jest LGPL. Jeśli statically link lub modify source, muszę release source code. Confusion o commercial licensing requirements może prowadzić do legal issues.

**Likelihood**: 3/5 (Medium - LGPL is well-understood, but complex)

**Impact**: 5/5 (Critical - legal liability, reputational damage)

**Risk Score**: **15 (Critical)**

**Mitigation Strategies**:
1. **Legal Review** (Immediate):
   - Hire IP lawyer ($500 consultation) to review LGPL compliance
   - Document compliance plan (dynamic linking, no modifications to PySide6 source)

2. **LGPL Compliance** (Mandatory):
   - Dynamic linking only (distribute PySide6 as separate .whl, not bundled)
   - No modifications to PySide6 source code
   - Include LGPL license text w/ distribution
   - Offer source code for LGPL components (via GitHub)

3. **Commercial License Option** (Fallback):
   - If LGPL compliance too restrictive, buy Qt Commercial License
   - Cost: ~$500/month/developer = $6k/year for 1 dev (expensive)
   - Only if absolutely necessary (e.g., proprietary plugin system)

4. **Alternative Framework** (Nuclear option):
   - Switch to Electron (web-based, MIT license) jeśli Qt licensing blocked
   - Cost: 2-3 months rework
   - Only if Qt licensing is showstopper

**Residual Risk**: Low (with legal review + LGPL compliance)

**Owner**: Founder (legal compliance)

---

#### **RISK-003: Scope Creep (Feature Bloat)**
**Kategoria**: Operational

**Opis**:
User requests dla "just one more feature" narastają. MVP scope rozszerza się z 10 features do 20+. Timeline delay z 6 miesięcy do 12+. Budget overrun.

**Likelihood**: 5/5 (Very High - inevitable w każdym projekcie)

**Impact**: 3/5 (Medium - delays, but not fatal)

**Risk Score**: **15 (Critical)**

**Mitigation Strategies**:
1. **Strict Scope Definition** (Immediate):
   - MVP scope frozen (E-085: Top 10 features only)
   - All new requests → Post-MVP backlog (ROADMAP-001 Phase 2)
   - "No" is default answer to feature requests

2. **Stakeholder Communication** (Ongoing):
   - Weekly updates: "We're focused on X, Y is deferred to post-MVP"
   - Transparent roadmap (public Notion page)
   - Manage expectations: "MVP = minimal, not perfect"

3. **Change Control Process** (Formal):
   - New feature request → document in backlog
   - Evaluate via RICE (E-085) → only add if score >50
   - Require executive approval (founder) dla scope changes

4. **Time Boxes** (Enforcement):
   - M1-M2: Alpha features only
   - M3-M4: Beta features only
   - M5-M6: RC features only
   - Hard cutoff dates - no exceptions

**Residual Risk**: Medium (scope creep partially unavoidable, but contained)

**Owner**: Product Manager (founder)

---

#### **RISK-004: Contractor Attrition/Availability**
**Kategoria**: Operational

**Opis**:
Contractor (1 dev @ $6k/month) może quit mid-project, take another gig, lub become unavailable. Replacement search takes 2-4 tygodnie. Project delayed.

**Likelihood**: 3/5 (Medium - freelancers less committed than FTE)

**Impact**: 4/5 (High - 50% team capacity gone)

**Risk Score**: **12 (High)**

**Mitigation Strategies**:
1. **Backup Contractors** (Proactive):
   - Identify 2-3 backup devs (pre-vetted, ready to start)
   - Maintain relationships (occasional small gigs)
   - Contract clause: 2-week notice required

2. **Knowledge Transfer** (Ongoing):
   - Detailed documentation (architecture, code comments)
   - Pair programming sessions (founder + contractor)
   - Weekly code reviews (founder stays up-to-date)

3. **Contract Terms** (Legal):
   - Milestone-based payments (not hourly) - incentive to finish
   - IP assignment clause (code ownership to company)
   - Non-compete (can't work dla competitor during contract)

4. **Founder Redundancy** (Backstop):
   - Founder can step in as backup dev (sweat equity)
   - Reduce reliance na contractor dla critical path items

**Residual Risk**: Medium (cannot fully eliminate contractor risk)

**Owner**: Founder (hiring & contracts)

---

#### **RISK-005: Market Validation Failure (No PMF)**
**Kategoria**: Business

**Opis**:
Beta users try Ishkarim, say "meh, not useful" lub "too complex". No product-market fit (PMF). Pivot required lub project abandoned.

**Likelihood**: 3/5 (Medium - user interviews positive, but small sample)

**Impact**: 5/5 (Critical - project failure)

**Risk Score**: **15 (Critical)**

**Mitigation Strategies**:
1. **Early User Feedback** (Iterative approach):
   - Alpha (M2): 5 users test basic concept
   - Beta (M4): 20 users test core features
   - RC (M6): 50 users test full MVP
   - Pivot points: If <50% users say "I'd use daily" → re-evaluate

2. **Metrics-Driven Validation** (Quantitative):
   - Track: Daily active users (DAU), retention (D7/D30), NPS
   - Success threshold: 60%+ D7 retention, NPS >30
   - If metrics miss → root cause analysis + pivot

3. **User Research** (Qualitative):
   - Weekly interviews (5 users/week during beta)
   - Ask: "What would make you pay for this?"
   - Iterate based on feedback (adjust features, UX)

4. **Pivot Options** (Contingency):
   - **Pivot A**: Focus on compliance market only (niche down)
   - **Pivot B**: B2B SaaS instead desktop app (easier distribution)
   - **Pivot C**: Open source + consulting revenue model

**Residual Risk**: Medium (early feedback loops reduce risk, but PMF nie guaranteed)

**Owner**: Founder (product strategy)

---

#### **RISK-006: Competitive Response (Fast Followers)**
**Kategoria**: Business

**Opis**:
Confluence/Notion see Ishkarim traction, add gap detection + graph viz features. Leverage 30M user base, crush Ishkarim przed traction.

**Likelihood**: 2/5 (Low - big players slow to respond to niche products)

**Impact**: 4/5 (High - kills competitive advantage)

**Risk Score**: **8 (Medium)**

**Mitigation Strategies**:
1. **Speed to Market** (Offensive):
   - Ship MVP fast (6 months) before competitors notice
   - Build moat via network effects (community, integrations)
   - First-mover advantage w/ compliance market (niche)

2. **Differentiation** (Defensive):
   - Focus on proof-based system (hard to copy fast)
   - Deep compliance features (FDA/HIPAA templates) - not general-purpose
   - Superior UX dla technical users (desktop app, not web bloat)

3. **Niche Focus** (Strategic):
   - Don't compete head-to-head z Notion/Confluence
   - Target: Regulated industries, technical teams (they won't use Notion)
   - "Best tool dla compliance docs" vs "best general wiki"

4. **Community Lock-In** (Long-term):
   - Open core model (free tier generous)
   - Plugin ecosystem (community contributions)
   - User-generated templates (switching cost)

**Residual Risk**: Medium (large players mogą respond eventually, ale niche focus protects)

**Owner**: Founder (strategy & marketing)

---

#### **RISK-007: Technology Obsolescence (Python/Qt)**
**Kategoria**: Technical

**Opis**:
Python/Qt stają się unpopular (shift to Rust/Tauri, web-based Electron). Difficulty hiring devs, maintaining codebase long-term.

**Likelihood**: 2/5 (Low - Python/Qt still popular w 2025, trend stable)

**Impact**: 3/5 (Medium - long-term maintenance harder)

**Risk Score**: **6 (Medium)**

**Mitigation Strategies**:
1. **Modular Architecture** (Proactive):
   - Separate business logic (Python) from UI (Qt)
   - Core engine jako library (can re-use if switch UI framework)
   - API-first design (GUI just one client)

2. **Monitor Trends** (Ongoing):
   - Track: Python usage (TIOBE index), Qt adoption
   - Re-evaluate stack every 12 months
   - Be ready to pivot jeśli ecosystem declines

3. **Web Version** (Hedge):
   - Phase 2: Build web interface (React/Vue) alongside desktop
   - Share backend (Python API server)
   - Diversify UI platforms (desktop + web)

4. **Open Source** (Community resilience):
   - If company folds, community can maintain (Python/Qt easy to fork)
   - Lower risk vs proprietary stack

**Residual Risk**: Low (Python/Qt stable, long runway before obsolete)

**Owner**: Tech Lead

---

#### **RISK-008: Data Loss/Corruption (No Git Integration MVP)**
**Kategoria**: Technical

**Opis**:
MVP nie ma Git integration (deferred to post-MVP). Users edit docs locally (Markdown files). Accidental deletion, corruption, no version control. User frustration + data loss.

**Likelihood**: 3/5 (Medium - manual file management error-prone)

**Impact**: 4/5 (High - lose user trust, churn)

**Risk Score**: **12 (High)**

**Mitigation Strategies**:
1. **Auto-Backup** (MVP feature - add to scope):
   - Ishkarim auto-saves copy of all docs to backup folder
   - Frequency: Every 5 minutes (like Google Docs)
   - Retention: 30 days (rolling window)

2. **User Education** (Documentation):
   - Onboarding tutorial: "Put docs w Git repo"
   - Best practices guide: Use version control
   - Warning message jeśli no Git detected

3. **Manual Export** (Workaround):
   - Export full doc set jako ZIP (FR-070 already scoped)
   - User manually backs up before major changes

4. **Git Integration Priority** (Post-MVP):
   - Move FR-120 (Git integration) do Q3 2026 (not Q4)
   - Add simple Git commit/push shortcuts w GUI

**Residual Risk**: Medium (auto-backup reduces risk, but Git integration needed long-term)

**Owner**: Tech Lead

---

## Implikacje

### Risk Summary - Priority Actions

| Risk ID | Risk Name | Score | Priority | **Action Required** |
|---------|-----------|-------|----------|---------------------|
| RISK-001 | Performance degradation | 16 | Critical | Benchmark 1000 nodes, implement pagination |
| RISK-002 | Qt licensing | 15 | Critical | Legal review LGPL compliance ($500) |
| RISK-003 | Scope creep | 15 | Critical | Freeze MVP scope, change control process |
| RISK-005 | No PMF | 15 | Critical | Alpha feedback (M2), pivot if <50% positive |
| RISK-004 | Contractor attrition | 12 | High | Identify 2 backup devs, knowledge transfer |
| RISK-008 | Data loss | 12 | High | Add auto-backup to MVP scope |
| RISK-006 | Competitive response | 8 | Medium | Speed to market, niche focus |
| RISK-007 | Tech obsolescence | 6 | Medium | Modular architecture, monitor trends |

### Budget Impact (Risk Mitigation Costs)

| Mitigation | Cost | Timeline |
|------------|------|----------|
| Legal review (LGPL) | $500 | M1 (immediate) |
| Backup contractor bench | $0 (relationships) | M1-M2 |
| Auto-backup feature | +0.5 person-months = $3k | M3 (add to scope) |
| Performance benchmarking | Included (QA budget) | M5 |
| User research (PMF validation) | Included (beta program) | M2, M4, M6 |
| **TOTAL ADDITIONAL** | **$3,500** | - |

**Revised budget**: $48,000 + $3,500 = **$51,500** (3.5% increase, within contingency)

### Risk Dashboard (Monthly Review)

Track podczas projektu:
- **M1**: RISK-002 (legal review), RISK-004 (hire contractor)
- **M2**: RISK-005 (Alpha feedback), RISK-003 (scope freeze)
- **M3**: RISK-008 (implement auto-backup)
- **M4**: RISK-005 (Beta feedback), RISK-001 (performance test)
- **M5**: RISK-001 (optimize graph), RISK-006 (competitive scan)
- **M6**: RISK-005 (RC feedback - go/no-go decision)

**Quarterly review**: Re-score all risks, add new risks, archive mitigated risks

## Dane Raw

### Risk Scoring Matrix

```
IMPACT →
     1    2    3    4    5
L  ┌────┬────┬────┬────┬────┐
I 5│  5 │ 10 │ 15 │ 20 │ 25 │
K  ├────┼────┼────┼────┼────┤
E 4│  4 │  8 │ 12 │ 16 │ 20 │
L  ├────┼────┼────┼────┼────┤
I 3│  3 │  6 │  9 │ 12 │ 15 │ ← RISK-005, 008
H  ├────┼────┼────┼────┼────┤
O 2│  2 │  4 │  6 │  8 │ 10 │
O  ├────┼────┼────┼────┼────┤
D 1│  1 │  2 │  3 │  4 │  5 │
   └────┴────┴────┴────┴────┘
              ↑
         RISK-001 (4×4=16)
         RISK-002 (3×5=15)
         RISK-003 (5×3=15)
```

**Critical zone** (red): Score ≥15
**High zone** (orange): Score 10-14
**Medium zone** (yellow): Score 5-9
**Low zone** (green): Score 1-4

### Industry Benchmarks - Project Failure Rates

**Software project risks** (Standish Group 2024):
- **Scope creep**: #1 cause of delay (70% projects affected)
- **Resource attrition**: #3 cause (45% projects)
- **Poor PMF**: #1 cause of failure (42% startups fail due to no market need)

**Ishkarim risk profile**:
- ✅ Lower than average: Strong user research (E-081/082/083 validate need)
- ⚠️ Average: Technical risks (performance, licensing) - standard for new products
- ❌ Higher than average: Small team (2 devs) = concentration risk

### Mitigation ROI

| Risk | Mitigation Cost | Avoided Cost (if risk occurs) | **ROI** |
|------|-----------------|------------------------------|---------|
| RISK-002 (licensing) | $500 legal review | $50k lawsuit + reputation damage | **100× ROI** |
| RISK-003 (scope creep) | $0 (discipline) | 3-6 months delay = $18-36k | **∞ ROI** |
| RISK-005 (no PMF) | $0 (iterative approach) | $48k wasted development | **∞ ROI** |
| RISK-008 (data loss) | $3k (auto-backup) | 50% user churn = $30k lost revenue (Y2) | **10× ROI** |

**Conclusion**: Risk mitigation highly cost-effective (spend $3.5k, avoid $100k+ losses)
