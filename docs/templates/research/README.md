# Research Templates - Dokumentacja

**Wersja:** 1.0
**Data:** 2025-12-29
**Podstawa:** PROPOZYCJA-1-Research-Branch-Templates.md

---

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Kiedy używać Research Templates](#kiedy-używać-research-templates)
3. [Katalog szablonów](#katalog-szablonów)
4. [Workflows i przepływy](#workflows-i-przepływy)
5. [Przykłady użycia](#przykłady-użycia)
6. [Best Practices](#best-practices)
7. [FAQ](#faq)

---

## Wprowadzenie

### Czym są Research Templates?

Research Templates to zestaw **7 szablonów dokumentacyjnych** zaprojektowanych do systematycznego prowadzenia badań, eksperymentów i eksploracji konceptów w projektach.

**Problem, który rozwiązują:**
- ❌ Badania są ad-hoc, wyniki giną w Slack/email
- ❌ Eksperymenty nie są powtarzalne (brak dokumentacji metodologii)
- ❌ Decyzje oparte na "gut feeling" zamiast danych
- ❌ Wiedza z PoC/spike'ów przepada po zakończeniu

**Rozwiązanie:**
- ✅ Formalizacja procesu badawczego (Hypothesis → Experiment → Findings)
- ✅ Audytowalny trail eksperymentów (compliance, knowledge retention)
- ✅ Data-driven decisions (ADR wspierane empirycznymi danymi)
- ✅ Systematyczna eksploracja alternatyw (scoring matrix, trade-offs)

### Dla kogo?

**Zespoły software:**
- Spike solutions (Scrum/Agile)
- PoC (Proof of Concept) dla nowych technologii
- Performance optimization research
- Architecture exploration (A/B testing approaches)

**Zespoły R&D:**
- Formalizacja hipotez naukowych
- Tracking eksperymentów (lab notebooks)
- Publikacja wyników (papers, reports)

**Zespoły produktowe:**
- UX research spikes
- Business model validation (pricing, features)
- Market research documentation

**Branże regulowane:**
- Clinical trials (pharma, medical devices)
- Financial compliance (audit trails)
- Quality assurance (manufacturing)

---

## Kiedy używać Research Templates

### Decision Tree

```
┌─────────────────────────────────────────┐
│ Czy masz pytanie wymagające badań?      │
└──────────────┬──────────────────────────┘
               │
               ▼
      ┌────────┴────────┐
      │   TAK           │
      └────────┬────────┘
               │
               ▼
┌──────────────────────────────────────────────┐
│ Czy potrzebujesz porównać wiele opcji?       │
└──────────┬───────────────────────────────────┘
           │
    ┌──────┴──────┐
    │ TAK         │ NIE
    ▼             ▼
ALTERNATIVE-  ┌─────────────────────────┐
EXPLORATION   │ Czy to krótkie badanie? │
              └─────┬───────────────────┘
                    │
             ┌──────┴──────┐
             │ TAK (<5 dni)│ NIE (>1 tydzień)
             ▼             ▼
        SPIKE-SOLUTION  HYPOTHESIS-DOC
                           ↓
                     EXPERIMENT-LOG
                           ↓
                        POC-DOC
```

### Quick Reference

| Szablon | Kiedy używać | Czas trwania | Output |
|---------|--------------|--------------|--------|
| **HYPOTHESIS-DOC** | Masz hipotezę do zwalidowania | 4-8 tygodni | Validated/Invalidated hypothesis |
| **EXPERIMENT-LOG** | Prowadzisz eksperyment | 2-6 tygodni | Data, metrics, conclusions |
| **POC-DOC** | Potrzebujesz PoC techniczny | 2-4 tygodnie | Proceed/Pivot/Stop recommendation |
| **SPIKE-SOLUTION** | Szybkie pytanie techniczne/UX/biznesowe | 2-5 dni | YES/NO/CONDITIONAL answer |
| **RESEARCH-FINDINGS** | Agregacja wyników z wielu badań | N/A (raport) | Executive summary, recommendations |
| **ALTERNATIVE-EXPLORATION** | Wybór między 3+ opcjami | 2-4 tygodnie | Ranking, recommendation |
| **CONCEPT-BRANCH** | Parallel exploration dwóch podejść | 4-8 tygodni | Merge/Kill decision |

---

## Katalog szablonów

### 1. HYPOTHESIS-DOC (Hypothesis Document)

**Grupa:** research
**Domena:** innovation
**Plik:** [HYPOTHESIS-DOC.md](./HYPOTHESIS-DOC.md)

**Opis:**
Formalizacja hipotezy badawczej z kryteriami walidacji. Używany przed rozpoczęciem eksperymentu lub PoC.

**Struktura kluczowa:**
- Stwierdzenie hipotezy (H0/H1)
- Założenia
- Kryteria sukcesu/porażki (measurable!)
- Metodologia walidacji
- Timeboxing

**Kiedy używać:**
- Przed rozpoczęciem kosztownego eksperymentu/PoC
- Gdy potrzebujesz alignment zespołu na tym, CO badamy i JAK zmierzymy sukces
- Gdy wymagana jest formalna aprobata (przed alokacją budżetu)

**Przykład:** [HYPOTHESIS-DOC-001-migracja-postgres-mongodb.md](../../examples/research/HYPOTHESIS-DOC-001-migracja-postgres-mongodb.md)

---

### 2. EXPERIMENT-LOG (Experiment Log)

**Grupa:** research
**Domena:** innovation
**Plik:** [EXPERIMENT-LOG.md](./EXPERIMENT-LOG.md)

**Opis:**
Tracking eksperymentu - setup, execution, observations (timestamped), results, analysis.

**Struktura kluczowa:**
- Link do hipotezy (HYPOTHESIS-DOC)
- Setup eksperymentu (environment, dataset, tools)
- Procedura wykonania (kroki, variables)
- **Obserwacje (timestamped!)** - chronologiczny log
- Dane i metryki
- Analiza wyników (statistical significance)
- Wnioski (hipoteza potwierdzona/odrzucona)

**Kiedy używać:**
- Podczas wykonywania eksperymentu (live documentation)
- Gdy potrzebujesz audytowalnego trail (compliance)
- Gdy wyniki będą podstawą decyzji (ADR)

**Best practice:**
- Zapisuj obserwacje w czasie rzeczywistym (timestamped entries)
- Dokumentuj także nieoczekiwane wyniki (surprises, anomalies)
- Statystyczna analiza wyników (p-values, confidence intervals)

**Przykład:** [EXPERIMENT-LOG-001-mongodb-benchmark.md](../../examples/research/EXPERIMENT-LOG-001-mongodb-benchmark.md)

---

### 3. POC-DOC (Proof of Concept)

**Grupa:** research
**Domena:** engineering
**Plik:** [POC-DOC.md](./POC-DOC.md)

**Opis:**
Dokumentacja Proof of Concept z validation criteria i decision framework (Proceed/Pivot/Stop).

**Struktura kluczowa:**
- Cel PoC (problem/opportunity)
- Zakres (In/Out)
- Podejście techniczne (high-level architecture)
- **Success criteria** (functional, non-functional, business)
- Wyniki i metryki (vs criteria)
- Zidentyfikowane luki/ryzyka
- **Rekomendacja:** PROCEED / PIVOT / STOP (z uzasadnieniem)

**Kiedy używać:**
- Przed adopcją nowej technologii (evaluate feasibility)
- Przed dużą inwestycją (de-risk decision)
- Gdy potrzebujesz empirycznych danych dla ADR

**Output:**
- Go/No-Go decision (data-driven)
- Lista warunków kontynuacji (jeśli PROCEED)
- Zidentyfikowane ryzyka i gaps

**Przykład:** [POC-DOC-001-mongodb-pilot-deployment.md](../../examples/research/POC-DOC-001-mongodb-pilot-deployment.md)

---

### 4. SPIKE-SOLUTION (Spike Solution Template)

**Grupa:** research
**Domena:** multi (tech/ux/business)
**Plik:** [SPIKE-SOLUTION.md](./SPIKE-SOLUTION.md)

**Opis:**
Lightweight template dla timeboxed spike solutions (max 2-5 dni). Szybka odpowiedź na konkretne pytanie.

**Typy spike'ów:**
- **Technical Spike:** API evaluation, library comparison, performance testing
- **UX Spike:** Usability testing, wireframing, accessibility audit
- **Business Spike:** Pricing model, market research, competitor analysis

**Struktura kluczowa:**
- Pytanie badawcze (konkretne, answerable)
- Dlaczego teraz (business value, blocker status)
- **Timebox:** Max 5 dni (HARD STOP!)
- Podejście (methodology)
- Odkrycia (daily log)
- **Odpowiedź:** YES / NO / YES with conditions / NEEDS MORE RESEARCH

**Kiedy używać:**
- Scrum Sprint Planning (blocker przed User Story)
- Szybka walidacja założenia (2-3 dni wystarczą)
- Risk reduction (przed heavy investment)

**Zasada spike:**
- **Timeboxed:** 2-5 dni, NO EXTENSIONS!
- **Focused:** Jedno pytanie, konkretna odpowiedź
- **Lightweight:** Prototype, nie production code
- **Actionable:** Output to decision (create ADR, update User Story, etc.)

**Przykład:** [SPIKE-SOLUTION-001-rust-wasm-rendering.md](../../examples/research/SPIKE-SOLUTION-001-rust-wasm-rendering.md)

---

### 5. RESEARCH-FINDINGS (Research Findings Document)

**Grupa:** research
**Domena:** knowledge
**Plik:** [RESEARCH-FINDINGS.md](./RESEARCH-FINDINGS.md)

**Opis:**
Agregacja wyników z wielu eksperymentów/PoC/spike'ów. Executive summary dla stakeholderów.

**Struktura kluczowa:**
- Executive summary (TL;DR)
- Lista przeprowadzonych eksperymentów
- **Kluczowe odkrycia** (findings z evidence)
- Wzorce i trendy (cross-experiment insights)
- Niespodzianki i anomalie
- **Implikacje** (product, technical, business)
- Rekomendacje (priorytetyzowane)
- Przyszłe badania (unanswered questions)

**Kiedy używać:**
- Po zakończeniu research cycle (quarterly, project-based)
- Przed ważną decyzją strategiczną (data dla Board/Execs)
- Jako podstawa dla roadmap planning

**Value:**
- **Knowledge aggregation:** Wyniki nie giną po zakończeniu research
- **Pattern recognition:** Insights across experiments
- **Strategic alignment:** Research → roadmap decisions

**Przykład:** [RESEARCH-FINDINGS-001-performance-optimization-q1-2026.md](../../examples/research/RESEARCH-FINDINGS-001-performance-optimization-q1-2026.md)

---

### 6. ALTERNATIVE-EXPLORATION (Alternative Approach Analysis)

**Grupa:** research
**Domena:** decision-support
**Plik:** [ALTERNATIVE-EXPLORATION.md](./ALTERNATIVE-EXPLORATION.md)

**Opis:**
Systematyczna eksploracja i porównanie alternatywnych podejść do tego samego problemu (min 3 opcje).

**Struktura kluczowa:**
- Problem statement
- Constraints i evaluation criteria (weighted!)
- Zidentyfikowane alternatywy (min 3)
- **Detailed analysis** każdej opcji (pros/cons, cost, risks)
- **Scoring matrix** (quantitative comparison)
- Porównanie (trade-offs visualization)
- **Rekomendacja** z uzasadnieniem
- Odrzucone opcje (why rejected, when reconsider)

**Kiedy używać:**
- Wybór technologii (database, framework, cloud provider)
- Architectural decision (monolith vs microservices)
- Build vs Buy vs Partner decisions
- Vendor selection

**Best practice:**
- **Min 3 opcje** (forced exploration, nie binary choice)
- **Weighted criteria** (align stakeholders on priorities)
- **Quantitative scoring** (reduce bias, increase objectivity)
- **Document rejected options** (why + when to reconsider)

**Przykład:** [ALTERNATIVE-EXPLORATION-001-baza-dokumentow.md](../../examples/research/ALTERNATIVE-EXPLORATION-001-baza-dokumentow.md)

---

### 7. CONCEPT-BRANCH (Concept Branch Document)

**Grupa:** research
**Domena:** innovation-management
**Plik:** [CONCEPT-BRANCH.md](./CONCEPT-BRANCH.md)

**Opis:**
Fork-merge framework dla równoległych gałęzi badawczych. Parallel exploration dwóch (lub więcej) radykalnie różnych podejść.

**Struktura kluczowa:**
- Punkt rozwidlenia (fork point z parent concept)
- Dlaczego nowa gałąź (rationale)
- Alternatywne podejście (key differences vs parent)
- **Progress tracking** (milestones, deliverables)
- **Learnings vs parent branch** (what works better/worse)
- **Merge/Kill/Continue decision** (final verdict)

**Kiedy używać:**
- Radykalnie różne podejścia do tego samego problemu (np. REST vs GraphQL)
- High uncertainty - nie wiesz, które podejście lepsze
- Parallel teams available (2+ teams, 4-8 weeks)
- Cost of wrong choice > cost of parallel exploration

**Pattern:**
```
Parent Concept (Problem defined)
    ├─ Branch A: Approach 1 (Team A, 4 weeks)
    └─ Branch B: Approach 2 (Team B, 4 weeks)
         ↓
    Compare results → Merge winner / Kill loser
```

**Value:**
- **Risk mitigation:** Validate assumptions before full commitment
- **Faster iteration:** Parallel vs sequential (4 weeks vs 8 weeks)
- **Team learning:** Both teams gain knowledge (retained even if branch killed)

**Przykład:** [CONCEPT-BRANCH-001-realtime-collab-websocket.md](../../examples/research/CONCEPT-BRANCH-001-realtime-collab-websocket.md)

---

## Workflows i przepływy

### Workflow 1: Technology Selection (Wybór technologii)

**Use case:** Zespół wybiera nową bazę danych dla modułu analytics.

```
1. ALTERNATIVE-EXPLORATION
   ├─ Zidentyfikuj opcje (Elasticsearch, ClickHouse, TimescaleDB)
   ├─ Scoring matrix (performance, cost, team expertise)
   └─ Shortlist: Top 2 opcje

2. HYPOTHESIS-DOC (dla Top 1)
   ├─ "ClickHouse oferuje lepsze performance/cost ratio"
   └─ Success criteria defined

3. POC-DOC
   ├─ Implement prototype (2 weeks)
   ├─ Benchmark vs criteria
   └─ Recommendation: PROCEED with conditions

4. ADR-XXX
   └─ Final decision: Adopt ClickHouse (based on POC evidence)
```

**Czas:** 6-8 tygodni total
**Output:** Data-driven decision, audytowalny trail

---

### Workflow 2: Sprint Spike (Agile/Scrum)

**Use case:** Sprint Planning - User Story blocked przez technical unknown.

```
Sprint Planning
    ↓
User Story US-123 blocked
    ↓
SPIKE-SOLUTION (timeboxed 3 dni)
    ├─ Pytanie: "Can we use React Server Components?"
    ├─ Prototyping (Day 1-2)
    ├─ Testing (Day 3)
    └─ Answer: YES, with conditions
         ↓
Update US-123
    ├─ Split into US-123a (RSC) + US-123b (refactor)
    └─ Re-estimate (now we know!)
         ↓
Sprint continues (no longer blocked)
```

**Czas:** 3 dni (w ramach sprintu)
**Output:** Unblock User Story, clear implementation path

---

### Workflow 3: Research Cycle (Quarterly R&D)

**Use case:** Quarterly performance optimization research.

```
Q1 2026 Research Initiative
    ├─ HYPOTHESIS-001: MongoDB performance
    │   └─ EXPERIMENT-001: Benchmark (2 weeks)
    │       └─ POC-001: Pilot deployment (4 weeks)
    │
    ├─ SPIKE-001: WASM Canvas rendering (3 days)
    │
    └─ RESEARCH-FINDINGS-001
        ├─ Aggregate all results
        ├─ Key findings: 70% performance improvement
        ├─ Recommendations: PROCEED with both initiatives
        └─ Informs Q2 roadmap
             ↓
ADR-042: Migrate to MongoDB
ADR-045: Adopt Rust/WASM for Canvas
```

**Czas:** 14 tygodni research → informuje Q2-Q3 roadmap
**Output:** Strategic decisions backed by empirical data

---

### Workflow 4: Parallel Exploration (Concept Branching)

**Use case:** Real-time collaboration - unknown best approach.

```
HYPOTHESIS-005: Real-time collab increases engagement
    ↓
Unknown: Which approach? (OT vs CRDT vs Locking)
    ↓
Parallel Branches (4 weeks)
    ├─ CONCEPT-BRANCH-001: WebSocket + Locking (Team A)
    │   ├─ Prototype (2 weeks)
    │   ├─ User testing (1 week)
    │   └─ Results: 90% comprehension, fast implementation
    │
    └─ CONCEPT-BRANCH-002: CRDT (Yjs) (Team B)
        ├─ Prototype (3 weeks)
        ├─ User testing (1 week)
        └─ Results: 65% comprehension, complex implementation
             ↓
Compare branches
    ├─ WebSocket wins (simplicity, user clarity)
    └─ Decision: MERGE Branch A, KILL Branch B
         ↓
ADR-048: Adopt WebSocket approach
Production implementation (8 weeks)
```

**Czas:** 4 weeks parallel + 8 weeks implementation = 12 weeks total
**Alternatywa sequential:** Try CRDT (5w) → fail → Try WebSocket (5w) = 10w + risk
**Value:** Higher confidence, mitigated risk, faster overall

---

## Przykłady użycia

### Przykład 1: Database Migration (End-to-end)

**Scenariusz:** Ishkarim ma performance problems z PostgreSQL.

**Research workflow:**

1. **Problem identification** (Week 0)
   - User complaints: "Search is slow" (2.5s latency)
   - Business impact: 2 enterprise deals blocked

2. **ALTERNATIVE-EXPLORATION-001** (Week 1-2)
   - Options: MongoDB, Elasticsearch, PostgreSQL Optimized, Dgraph
   - Scoring matrix → MongoDB wins (8.35/10)
   - Decision: Proceed with MongoDB validation

3. **HYPOTHESIS-001** (Week 3)
   - "MongoDB improves search 60%, graph queries 50%"
   - Success criteria defined, timeline 8 weeks

4. **EXPERIMENT-001** (Week 4-6)
   - Benchmark: 10K docs, synthetic workload
   - Results: Search -76% (2.5s → 0.6s), Graph -61% (1.8s → 0.7s)
   - Hypothesis: VALIDATED ✅

5. **POC-001** (Week 7-10)
   - Pilot: 5K real docs, 20 users, 4 weeks production-like
   - Results: Real-world -68% search, -50% graph (slightly slower than benchmark, but excellent)
   - User satisfaction: NPS +85
   - Recommendation: **PROCEED** ✅

6. **RESEARCH-FINDINGS-001** (Week 11)
   - Aggregate all results (EXP-001, POC-001, SPIKE-001 WASM)
   - Executive summary dla CTO/Board
   - Strategic implications: Unlock enterprise tier, Q2 roadmap

7. **ADR-042** (Week 12)
   - Decision: Migrate to MongoDB (based on research evidence)
   - Approved budget: $65K production migration

**Total:** 12 tygodni research → High-confidence $65K investment decision

---

### Przykład 2: Quick Spike (Agile Sprint)

**Scenariusz:** Sprint Planning - "Can we use WASM for Canvas rendering?"

**Spike workflow (3 dni):**

**Day 1:**
- Setup Rust + wasm-pack
- Minimal PoC (render rectangle)
- Verify compilation works ✅

**Day 2:**
- Implement rendering loop (1000 nodes)
- Benchmark WASM vs JS
- Results: **71% faster!** 😮

**Day 3:**
- Browser compatibility testing (97% coverage ✅)
- Bundle size analysis (580KB gzipped - acceptable ✅)
- Write SPIKE-SOLUTION-001 with answer: **YES, with conditions**

**Output:**
- User Story US-156 unblocked
- Clear implementation path (WASM + JS fallback)
- Confidence: HIGH (empirical data, not speculation)

**Time:** 3 dni (vs potentially 4 weeks wasted implementation bez spike)

---

## Best Practices

### 1. Timeboxing is Sacred

**Zasada:** Każdy research initiative musi mieć hard deadline.

- **Hypothesis:** 4-8 tygodni max
- **Experiment:** 2-6 tygodni max
- **PoC:** 2-4 tygodnie max
- **Spike:** 2-5 DNI max (no extensions!)

**Dlaczego:**
- Prevents analysis paralysis
- Forces prioritization (MVP scope)
- Ensures timely decision (opportunity cost)

**Enforcement:**
- Timebox w metadata (YAML frontmatter)
- Weekly check-ins (on track? extend/kill/pivot decision)
- Hard stop at deadline (output: decision or "inconclusive" + next steps)

---

### 2. Success Criteria Must Be Measurable

**Bad:** "System should be fast"
**Good:** "Search latency <1s (p95), 60% improvement vs baseline"

**Formula:**
```
Success Criteria = Metric + Target Value + Measurement Method
```

**Examples:**
- Performance: "API latency <100ms (p95), JMeter load test 100 concurrent users"
- User Satisfaction: "NPS >80, survey n=20 users"
- Cost: "Infrastructure <$1,000/month, AWS billing"
- Quality: "0 critical bugs, verified w test suite"

**Best practice:**
- Quantitative > Qualitative (when possible)
- Baseline + Target (pokazuje improvement %)
- Measurement method documented (reproducible)

---

### 3. Link Everything (Cross-References)

**Zasada:** Every research document linkuje do predecessors/successors.

```yaml
dependencies:
  - id: HYPOTHESIS-001
    type: requires
    reason: "Eksperyment waliduje tę hipotezę"

impacts:
  - id: ADR-042
    type: informs
    reason: "Wyniki eksperymentu wspierają decyzję w ADR"
```

**Value:**
- **Traceability:** Decision → Research → Evidence (audit trail)
- **Knowledge graph:** Visualize research dependencies
- **Context preservation:** Future readers understand "dlaczego"

**Tools:**
- Manual links (YAML cross-references w każdym dokumencie)
- Automated graph (parse YAML → visualize w Cytoscape/Obsidian)

---

### 4. Document Failures (Not Just Successes)

**Zasada:** Rejected hypotheses są VALUABLE knowledge!

**Bad practice:**
- PoC fails → document deleted → repeat mistake later ❌

**Good practice:**
- PoC fails → POC-DOC with "STOP" recommendation + why ✅
- Hypothesis rejected → EXPERIMENT-LOG with invalidation reasons ✅
- Spike answer "NO" → SPIKE-SOLUTION documenting why NO ✅

**Value:**
- **Prevent repetition:** Team 6 months later: "Let's try X!" → "We tried, see EXP-042, failed because Y"
- **Organizational learning:** Failures teach more than successes
- **Justify decisions:** "We chose A over B because PoC-B failed on criteria C"

---

### 5. Involve Stakeholders Early

**Zasada:** Get buy-in BEFORE heavy research investment.

**Workflow:**
1. **Draft HYPOTHESIS-DOC** → present to stakeholders
2. **Get approval** (budget, timeline, success criteria alignment)
3. **Run experiment/PoC**
4. **Present RESEARCH-FINDINGS** → decision (ADR)

**Avoid:**
- Surprise stakeholders z results (they feel "decided without them")
- Ask for budget AFTER research complete (sunk cost fallacy)

**Best practice:**
- Weekly/bi-weekly research sync (short updates)
- "Preview" presentations (interim results, ask for feedback)
- Involve decision-makers w defining success criteria (ownership)

---

### 6. Keep It Lightweight (MVP Research)

**Zasada:** Research documents ≠ academic papers. Focus on decision-making, not perfection.

**Good:**
- Executive summary (1 paragraph TL;DR)
- Bullet points, tables, visuals
- Sufficient detail dla reproducibility
- Clear recommendation (Proceed/Pivot/Stop)

**Avoid:**
- 50-page reports (nobody reads)
- Perfection paralysis (80% good enough > 100% never done)
- Academic rigor dla sake of rigor (balance pragmatism vs thoroughness)

**Rule of thumb:**
- Hypothesis: 2-4 strony
- Experiment Log: 5-10 stron
- PoC: 8-12 stron
- Spike: 3-5 stron
- Research Findings: 10-15 stron
- Alternative Exploration: 10-15 stron

**If longer:** Consider splitting (too much scope).

---

### 7. Automate Where Possible

**Tooling recommendations:**

**Benchmarking:**
- JMeter, k6 (load testing, automated metrics collection)
- pytest-benchmark (Python performance tests)
- Datadog/Grafana (real-time monitoring, export data)

**Data collection:**
- Python scripts (automated data export, checksums verification)
- Git hooks (track experiment versions)
- CI/CD integration (regression testing dla performance)

**Visualization:**
- Jupyter Notebooks (interactive analysis, charts)
- Matplotlib/Plotly (Python visualization)
- Excel/Google Sheets (quick charts dla stakeholders)

**Templates:**
- Cookiecutter (generate research docs from templates)
- Scripts to pre-fill metadata (project, owner, dates)

---

## FAQ

### Q: Kiedy użyć SPIKE vs HYPOTHESIS+EXPERIMENT?

**A: Spike dla szybkich pytań (2-5 dni), Hypothesis+Experiment dla długich badań (4-8 tygodni).**

**Spike:**
- Timeboxed (max 5 dni)
- Jedno konkretne pytanie
- Lightweight prototype
- Quick answer (YES/NO/CONDITIONAL)

**Hypothesis + Experiment:**
- Dłuższy cykl (4-8 tygodni)
- Comprehensive testing
- Statistical validation
- Detailed analysis

**Example:**
- "Can we use library X?" → **SPIKE** (3 dni prototype)
- "Library X improves performance 50%?" → **HYPOTHESIS+EXPERIMENT** (4 tygodnie benchmark, validation)

---

### Q: Czy muszę użyć wszystkich 7 szablonów dla jednego research initiative?

**A: NIE. Używaj tylko tych, które dodają wartość.**

**Minimal research:**
- SPIKE-SOLUTION (3 dni) → ADR (decision)

**Standard research:**
- HYPOTHESIS-DOC → EXPERIMENT-LOG → ADR

**Comprehensive research:**
- ALTERNATIVE-EXPLORATION → HYPOTHESIS-DOC → EXPERIMENT-LOG → POC-DOC → RESEARCH-FINDINGS → ADR

**Zasada:** Start minimal, expand jeśli potrzeba (don't overengineer).

---

### Q: Co jeśli moja hipoteza została odrzucona?

**A: To SUCCESS, nie failure! Documented rejection jest valuable knowledge.**

**Workflow:**
1. Update HYPOTHESIS-DOC status → `invalidated`
2. Complete EXPERIMENT-LOG z wnioskami (why rejected, lessons learned)
3. Optional: RESEARCH-FINDINGS (what we learned, alternative approaches)
4. Create ADR: "Decision NOT to pursue X (based on EXP-042)"

**Value:**
- Prevent future teams from repeating mistake
- Justify decision ("We considered X, tested, rejected because Y")
- Organizational learning (failures > successes dla knowledge)

---

### Q: Jak długo trzymać research documents?

**A: Indefinitely (archive, don't delete).**

**Retention policy:**
- **Active research:** `/docs/research/` (current work)
- **Completed research:** `/docs/research/archive/YYYY/` (by year)
- **References:** ADR linkuje do archived research (traceability)

**Why retain:**
- Audit trail (compliance, especially regulated industries)
- Knowledge retention (new team members learn from past research)
- Prevent repetition ("We tried this in 2023, see archived EXP-015")

**Storage:**
- Git repository (version control, searchable)
- Minimal storage cost (Markdown files są small)

---

### Q: Czy Research Templates są TYLKO dla technical research?

**A: NIE! Działają dla UX, business, product research też.**

**Examples:**

**UX Research:**
- SPIKE-SOLUTION: Usability testing (5 users, 3 dni)
- EXPERIMENT-LOG: A/B test tracking (2 tygodnie)
- RESEARCH-FINDINGS: Quarterly UX insights

**Business Research:**
- HYPOTHESIS-DOC: "Pricing model X increases conversion 20%"
- EXPERIMENT-LOG: A/B test (pricing variants, 4 weeks)
- ALTERNATIVE-EXPLORATION: Pricing models comparison

**Product Research:**
- SPIKE-SOLUTION: Feature exploration (customer interviews, 5 dni)
- POC-DOC: MVP prototype (validate product-market fit)

**Zasada:** Jeśli formułujesz pytanie + potrzebujesz empirycznej odpowiedzi → Research Templates apply!

---

### Q: Jak zmierzyć ROI Research Templates adoption?

**A: Track metrics przed i po adoption.**

**Metrics:**

**M1: Knowledge Retention**
- Before: "Can you find results z past experiment X?" → 30% success rate
- After: → 90% success rate (documented, searchable)

**M2: Decision Quality**
- Before: X% decisions backed by data
- After: Y% decisions backed by documented research (target: >70%)

**M3: Time to Decision**
- Before: Average 8 tygodni (hypothesis → decision)
- After: Average 4-6 tygodni (structured process, timeboxing)

**M4: Avoided Bad Decisions**
- Count: PoC with "STOP" recommendation → prevented waste
- Estimate: $X saved by NOT pursuing failed PoC

**M5: Team Confidence**
- Survey: "How confident are you w research-backed decisions?" (1-10 scale)
- Target: Average >8/10

---

## Zasoby

### Templates

- [HYPOTHESIS-DOC.md](./HYPOTHESIS-DOC.md)
- [EXPERIMENT-LOG.md](./EXPERIMENT-LOG.md)
- [POC-DOC.md](./POC-DOC.md)
- [SPIKE-SOLUTION.md](./SPIKE-SOLUTION.md)
- [RESEARCH-FINDINGS.md](./RESEARCH-FINDINGS.md)
- [ALTERNATIVE-EXPLORATION.md](./ALTERNATIVE-EXPLORATION.md)
- [CONCEPT-BRANCH.md](./CONCEPT-BRANCH.md)

### Przykłady

Wszystkie przykłady w katalogu: [`/examples/research/`](../../examples/research/)

**End-to-end workflow:**
1. [HYPOTHESIS-DOC-001-migracja-postgres-mongodb.md](../../examples/research/HYPOTHESIS-DOC-001-migracja-postgres-mongodb.md)
2. [EXPERIMENT-LOG-001-mongodb-benchmark.md](../../examples/research/EXPERIMENT-LOG-001-mongodb-benchmark.md)
3. [POC-DOC-001-mongodb-pilot-deployment.md](../../examples/research/POC-DOC-001-mongodb-pilot-deployment.md)
4. [RESEARCH-FINDINGS-001-performance-optimization-q1-2026.md](../../examples/research/RESEARCH-FINDINGS-001-performance-optimization-q1-2026.md)

**Standalone:**
- [SPIKE-SOLUTION-001-rust-wasm-rendering.md](../../examples/research/SPIKE-SOLUTION-001-rust-wasm-rendering.md)
- [ALTERNATIVE-EXPLORATION-001-baza-dokumentow.md](../../examples/research/ALTERNATIVE-EXPLORATION-001-baza-dokumentow.md)
- [CONCEPT-BRANCH-001-realtime-collab-websocket.md](../../examples/research/CONCEPT-BRANCH-001-realtime-collab-websocket.md)

### Dokumentacja źródłowa

- [PROPOZYCJA-1-Research-Branch-Templates.md](../../proposals/PROPOZYCJA-1-Research-Branch-Templates.md) - Pełna specyfikacja research templates

---

## Kontakt i Wsparcie

**Pytania?** Utwórz issue w projekcie lub skontaktuj się z zespołem dokumentacji.

**Feedback?** Sugestie dotyczące templates są mile widziane - Research Templates to living framework!

**Contributions?** Pull requests z improvements/examples przyjmowane z wdzięcznością.

---

**Ostatnia aktualizacja:** 2025-12-29
**Wersja README:** 1.0
**Maintainer:** Zespół Dokumentacji Ishkarim
