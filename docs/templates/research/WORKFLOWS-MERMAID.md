# Research Templates - Diagramy Workflow (Mermaid)

**Wersja:** 1.0
**Data:** 2025-12-29
**Opis:** Wizualne reprezentacje przepływów pracy dla Research Templates

---

## Spis treści

1. [Decision Tree - Wybór szablonu](#decision-tree---wybór-szablonu)
2. [Workflow 1: Technology Selection](#workflow-1-technology-selection)
3. [Workflow 2: Sprint Spike (Agile)](#workflow-2-sprint-spike-agile)
4. [Workflow 3: Research Cycle (Quarterly)](#workflow-3-research-cycle-quarterly)
5. [Workflow 4: Parallel Exploration](#workflow-4-parallel-exploration)
6. [Template Dependencies Graph](#template-dependencies-graph)
7. [Research Lifecycle](#research-lifecycle)

---

## Decision Tree - Wybór szablonu

```mermaid
graph TD
    Start([Masz pytanie badawcze?]) --> Question{Czy potrzebujesz<br/>porównać wiele opcji?}

    Question -->|TAK<br/>3+ alternatywy| AltExp[ALTERNATIVE-EXPLORATION<br/>Scoring matrix<br/>2-4 tygodnie]
    Question -->|NIE| Duration{Jak długie badanie?}

    Duration -->|Krótkie<br/>2-5 dni| Spike[SPIKE-SOLUTION<br/>Timeboxed spike<br/>Quick answer]
    Duration -->|Średnie<br/>2-4 tygodnie| PoC[POC-DOC<br/>Proof of Concept<br/>Proceed/Pivot/Stop]
    Duration -->|Długie<br/>4-8 tygodni| Hypothesis[HYPOTHESIS-DOC<br/>+ EXPERIMENT-LOG<br/>Comprehensive validation]

    AltExp --> PoC
    Spike --> Decision1{Czy odpowiedź<br/>wystarczająca?}
    Decision1 -->|TAK| ADR1[ADR - Decision]
    Decision1 -->|NIE| PoC

    PoC --> Decision2{Rekomendacja?}
    Decision2 -->|PROCEED| ADR2[ADR - Adoption]
    Decision2 -->|PIVOT| AltExp
    Decision2 -->|STOP| ADR3[ADR - Rejection]

    Hypothesis --> Experiment[EXPERIMENT-LOG<br/>Tracking + Analysis]
    Experiment --> Validated{Hipoteza<br/>zwalidowana?}
    Validated -->|TAK| PoC
    Validated -->|NIE| Findings1[RESEARCH-FINDINGS<br/>Document learnings]

    style Spike fill:#90EE90
    style PoC fill:#87CEEB
    style Hypothesis fill:#FFB6C1
    style AltExp fill:#FFD700
    style ADR1 fill:#DDA0DD
    style ADR2 fill:#DDA0DD
    style ADR3 fill:#DDA0DD
```

---

## Workflow 1: Technology Selection

**Scenariusz:** Wybór bazy danych dla modułu analytics

```mermaid
graph TB
    Problem([Problem: Wolne wyszukiwanie<br/>PostgreSQL nie skaluje]) --> Alt[ALTERNATIVE-EXPLORATION-001<br/>Week 1-2]

    Alt --> Options[Zidentyfikowane opcje:<br/>• MongoDB<br/>• Elasticsearch<br/>• PostgreSQL Optimized<br/>• Dgraph]

    Options --> Matrix[Scoring Matrix<br/>MongoDB: 8.35/10 ✅<br/>Elasticsearch: 6.40<br/>PostgreSQL: 7.50<br/>Dgraph: 5.80]

    Matrix --> Shortlist[Shortlist: MongoDB<br/>Top option dla validation]

    Shortlist --> Hyp[HYPOTHESIS-001<br/>Week 3<br/>MongoDB improves performance 60%+]

    Hyp --> Exp[EXPERIMENT-001<br/>Week 4-6<br/>Benchmark 10K docs]

    Exp --> Results1[Results:<br/>Search -76% ✅<br/>Graph -61% ✅<br/>Hypothesis VALIDATED]

    Results1 --> PoC[POC-001<br/>Week 7-10<br/>Pilot: 5K docs, 20 users]

    PoC --> Results2[Results:<br/>Real-world -68% search ✅<br/>NPS +85 ✅<br/>0 data loss ✅]

    Results2 --> Recommend[Recommendation:<br/>PROCEED with MongoDB]

    Recommend --> Findings[RESEARCH-FINDINGS-001<br/>Week 11<br/>Aggregate all results]

    Findings --> ADR[ADR-042<br/>Week 12<br/>Decision: Migrate to MongoDB<br/>Budget: $65K approved]

    ADR --> Impl[Production Migration<br/>Q2 2026 - 12 weeks]

    style Problem fill:#FFB6C1
    style Alt fill:#FFD700
    style Hyp fill:#FFB6C1
    style Exp fill:#87CEEB
    style PoC fill:#87CEEB
    style Findings fill:#90EE90
    style ADR fill:#DDA0DD
    style Impl fill:#98FB98
```

**Timeline:** 12 tygodni research → High-confidence decision $65K investment

---

## Workflow 2: Sprint Spike (Agile)

**Scenariusz:** User Story zablokowany przez technical unknown

```mermaid
graph LR
    Sprint[Sprint Planning] --> Blocked{User Story US-156<br/>blocked}

    Blocked --> Unknown[Unknown:<br/>Can we use WASM<br/>for Canvas rendering?]

    Unknown --> Spike[SPIKE-001<br/>3 dni timeboxed]

    Spike --> Day1[Day 1: Setup<br/>• Rust + wasm-pack<br/>• Minimal PoC<br/>• Verify compilation ✅]

    Day1 --> Day2[Day 2: Benchmark<br/>• Implement render loop<br/>• WASM vs JS test<br/>• Result: 71% faster! 😮]

    Day2 --> Day3[Day 3: Validation<br/>• Browser compatibility: 97% ✅<br/>• Bundle size: 580KB ✅<br/>• Answer: YES with conditions]

    Day3 --> Answer{Answer?}

    Answer -->|YES| Unblock[Update US-156:<br/>• Split into 2 stories<br/>• WASM + JS fallback<br/>• Re-estimate effort]

    Unblock --> Continue[Sprint continues<br/>Story unblocked ✅]

    Answer -->|NO| Alternative[Find alternative<br/>approach]

    style Sprint fill:#FFE4B5
    style Spike fill:#90EE90
    style Day1 fill:#E0FFFF
    style Day2 fill:#E0FFFF
    style Day3 fill:#E0FFFF
    style Continue fill:#98FB98
```

**Timeline:** 3 dni spike → Story unblocked → Sprint delivery on track

---

## Workflow 3: Research Cycle (Quarterly)

**Scenariusz:** Q1 2026 Performance Optimization Initiative

```mermaid
graph TD
    Initiative([Q1 2026 Research Initiative<br/>Goal: Performance Optimization]) --> Branch1[Research Branch A:<br/>Database Performance]
    Initiative --> Branch2[Research Branch B:<br/>Frontend Performance]

    Branch1 --> Hyp1[HYPOTHESIS-001<br/>MongoDB performance<br/>Week 1]

    Hyp1 --> Exp1[EXPERIMENT-001<br/>Benchmark<br/>Week 2-4]

    Exp1 --> PoC1[POC-001<br/>Pilot deployment<br/>Week 5-8]

    Branch2 --> Spike1[SPIKE-001<br/>WASM Canvas rendering<br/>Week 9 - 3 days]

    PoC1 --> Result1[Results:<br/>-68% search latency ✅<br/>-50% graph queries ✅]

    Spike1 --> Result2[Results:<br/>-71% render time ✅<br/>+222% FPS ✅]

    Result1 --> Aggregate[RESEARCH-FINDINGS-001<br/>Week 11-12<br/>Aggregate all results]
    Result2 --> Aggregate

    Aggregate --> Summary[Executive Summary:<br/>• MongoDB: PROCEED ✅<br/>• WASM: PROCEED ✅<br/>• Combined impact: 60-70% improvement<br/>• Investment: $105K]

    Summary --> Decisions[Strategic Decisions:]

    Decisions --> ADR1[ADR-042<br/>Migrate to MongoDB]
    Decisions --> ADR2[ADR-045<br/>Adopt Rust/WASM]

    ADR1 --> Roadmap[Q2-Q3 2026 Roadmap:<br/>• Enterprise tier enabled<br/>• Real-time collab unlocked<br/>• Performance competitive advantage]
    ADR2 --> Roadmap

    style Initiative fill:#FFD700
    style Hyp1 fill:#FFB6C1
    style Exp1 fill:#87CEEB
    style PoC1 fill:#87CEEB
    style Spike1 fill:#90EE90
    style Aggregate fill:#98FB98
    style ADR1 fill:#DDA0DD
    style ADR2 fill:#DDA0DD
    style Roadmap fill:#FFE4B5
```

**Timeline:** 14 tygodni research → Strategic roadmap Q2-Q3 2026

---

## Workflow 4: Parallel Exploration

**Scenariusz:** Real-time Collaboration - Unknown best approach

```mermaid
graph TB
    Parent[HYPOTHESIS-005<br/>Real-time collab increases engagement 40%] --> Unknown{Unknown:<br/>Which implementation<br/>approach?}

    Unknown --> Options[Options identified:<br/>• WebSocket + Locking<br/>• CRDT Yjs<br/>• Operational Transformation]

    Options --> Decision{Decision:<br/>Parallel exploration}

    Decision --> Fork[Fork into 2 branches<br/>4 weeks parallel]

    Fork --> BranchA[CONCEPT-BRANCH-001<br/>WebSocket + Locking<br/>Team A 2 devs]
    Fork --> BranchB[CONCEPT-BRANCH-002<br/>CRDT Yjs<br/>Team B 2 devs]

    BranchA --> ProtoA[Week 1-2: Prototype<br/>• Lock manager<br/>• WebSocket server<br/>• Client UI]
    BranchB --> ProtoB[Week 1-3: Prototype<br/>• Yjs integration<br/>• WebRTC setup<br/>• Conflict resolution]

    ProtoA --> TestA[Week 3-4: Testing<br/>• 10 users tested<br/>• 90% comprehension ✅<br/>• 2.5 weeks impl ✅]
    ProtoB --> TestB[Week 4: Testing<br/>• 10 users tested<br/>• 65% comprehension ⚠️<br/>• 5 weeks impl ⚠️]

    TestA --> Compare[Week 5-6:<br/>Compare branches]
    TestB --> Compare

    Compare --> Matrix[Comparison Matrix:<br/>WebSocket: 8.5/10 ✅<br/>CRDT: 6.8/10]

    Matrix --> Winner{Winner?}

    Winner -->|WebSocket| MergeA[MERGE Branch A<br/>into production]
    Winner -->|CRDT| KillB[KILL Branch B<br/>Document learnings]

    MergeA --> ADR[ADR-048<br/>Adopt WebSocket approach<br/>Rationale: Simplicity + User clarity]
    KillB --> Archive[Archive CRDT research<br/>Revisit if offline editing critical]

    ADR --> Production[Production Implementation<br/>8 weeks rollout<br/>August 2026 launch 🚀]

    style Parent fill:#FFB6C1
    style BranchA fill:#90EE90
    style BranchB fill:#FFB6C1
    style Compare fill:#FFD700
    style MergeA fill:#98FB98
    style KillB fill:#FFA07A
    style ADR fill:#DDA0DD
    style Production fill:#98FB98
```

**Timeline:** 4 weeks parallel + 8 weeks implementation = 12 weeks total
**Value:** Higher confidence, mitigated risk vs sequential approach (10 weeks + risk)

---

## Template Dependencies Graph

**Jak research templates odnoszą się do siebie:**

```mermaid
graph TD
    Alt[ALTERNATIVE-EXPLORATION<br/>Scoring matrix<br/>Compare 3+ options] --> Hyp[HYPOTHESIS-DOC<br/>Formalize hypothesis<br/>Success criteria]

    Hyp --> Exp[EXPERIMENT-LOG<br/>Execute & track<br/>Timestamped observations]

    Exp --> Validated{Validated?}

    Validated -->|YES| PoC[POC-DOC<br/>Real-world validation<br/>Proceed/Pivot/Stop]
    Validated -->|NO| Findings1[RESEARCH-FINDINGS<br/>Document rejection]

    PoC --> Recommend{Recommendation?}

    Recommend -->|PROCEED| ADR1[ADR<br/>Adoption decision]
    Recommend -->|PIVOT| Alt
    Recommend -->|STOP| ADR2[ADR<br/>Rejection decision]

    Spike[SPIKE-SOLUTION<br/>Quick spike<br/>2-5 days] --> Answer{Answer clear?}

    Answer -->|YES| ADR3[ADR<br/>Quick decision]
    Answer -->|NO| Hyp

    ParentConcept[Parent Concept] --> Fork{Parallel<br/>exploration?}

    Fork -->|YES| Branch1[CONCEPT-BRANCH-001<br/>Approach A]
    Fork -->|YES| Branch2[CONCEPT-BRANCH-002<br/>Approach B]
    Fork -->|NO| Hyp

    Branch1 --> Compare[Compare branches]
    Branch2 --> Compare

    Compare --> MergeKill{Decision?}
    MergeKill -->|MERGE| ADR4[ADR<br/>Chosen approach]
    MergeKill -->|KILL| Archive[Archive learnings]

    Exp --> Aggregate[RESEARCH-FINDINGS<br/>Aggregate results]
    PoC --> Aggregate
    Spike --> Aggregate
    Branch1 --> Aggregate
    Branch2 --> Aggregate

    Aggregate --> Strategy[Strategic Decisions<br/>Roadmap alignment]

    style Alt fill:#FFD700
    style Hyp fill:#FFB6C1
    style Exp fill:#87CEEB
    style PoC fill:#87CEEB
    style Spike fill:#90EE90
    style Aggregate fill:#98FB98
    style ADR1 fill:#DDA0DD
    style ADR2 fill:#DDA0DD
    style ADR3 fill:#DDA0DD
    style ADR4 fill:#DDA0DD
    style Strategy fill:#FFE4B5
```

---

## Research Lifecycle

**Od problemu do produkcji:**

```mermaid
graph LR
    Problem([Problem Identified<br/>Performance/Feature/Risk]) --> Question{Type?}

    Question -->|Quick answer<br/>needed| Spike[SPIKE<br/>2-5 days]
    Question -->|Multiple<br/>options| Alt[ALTERNATIVE<br/>EXPLORATION<br/>2-4 weeks]
    Question -->|Long research<br/>needed| Hyp[HYPOTHESIS<br/>+ EXPERIMENT<br/>4-8 weeks]

    Spike --> SpikeOut{Output}
    SpikeOut -->|YES| Implement1[Implementation]
    SpikeOut -->|NO| Alternative1[Find alternative]
    SpikeOut -->|CONDITIONAL| PoC1[PoC validation]

    Alt --> AltOut[Recommended<br/>option]
    AltOut --> Hyp

    Hyp --> Exp[EXPERIMENT]
    Exp --> ExpOut{Validated?}

    ExpOut -->|YES| PoC2[POC]
    ExpOut -->|NO| Document1[Document<br/>rejection]

    PoC1 --> PocOut{Recommendation}
    PoC2 --> PocOut

    PocOut -->|PROCEED| ADR[ADR<br/>Decision Record]
    PocOut -->|PIVOT| Alt
    PocOut -->|STOP| Document2[Document<br/>rejection + why]

    ADR --> Findings[RESEARCH-FINDINGS<br/>Aggregate knowledge]
    Document1 --> Findings
    Document2 --> Findings

    Findings --> Knowledge[Knowledge Base<br/>Organizational learning]

    ADR --> Production[Production<br/>Implementation]

    Production --> Monitor[Monitor & Iterate<br/>Continuous improvement]

    style Problem fill:#FFB6C1
    style Spike fill:#90EE90
    style Alt fill:#FFD700
    style Hyp fill:#FFB6C1
    style Exp fill:#87CEEB
    style PoC1 fill:#87CEEB
    style PoC2 fill:#87CEEB
    style ADR fill:#DDA0DD
    style Findings fill:#98FB98
    style Knowledge fill:#E0FFFF
    style Production fill:#98FB98
```

---

## Szczegółowy Timeline Example

**Technology Selection - Week by week:**

```mermaid
gantt
    title Technology Selection Workflow - MongoDB Migration
    dateFormat YYYY-MM-DD
    section Alternative Exploration
    Identify options           :a1, 2025-12-01, 7d
    Analysis & scoring         :a2, after a1, 7d
    Recommendation             :a3, after a2, 3d

    section Hypothesis
    Draft hypothesis           :h1, after a3, 3d
    Stakeholder approval       :h2, after h1, 2d

    section Experiment
    Setup environment          :e1, 2026-01-06, 7d
    Data migration             :e2, after e1, 7d
    Benchmark execution        :e3, after e2, 14d
    Analysis & conclusions     :e4, after e3, 7d

    section PoC
    Pilot deployment           :p1, after e4, 7d
    4-week monitoring          :p2, after p1, 28d
    User feedback collection   :p3, after p1, 28d
    Final analysis             :p4, after p2, 7d

    section Research Findings
    Aggregate results          :r1, after p4, 7d
    Executive summary          :r2, after r1, 3d
    Presentation               :r3, after r2, 2d

    section Decision
    ADR creation               :d1, after r3, 3d
    Budget approval            :d2, after d1, 5d
```

---

## Stakeholder Decision Points

**Kluczowe momenty decision-making w research workflow:**

```mermaid
graph TD
    Start([Research Initiative]) --> Gate1{Gate 1:<br/>Hypothesis Approval}

    Gate1 -->|APPROVED<br/>Budget allocated| Experiment[EXPERIMENT<br/>Execution]
    Gate1 -->|REJECTED<br/>Not priority| Stop1[Stop/<br/>Defer]

    Experiment --> Results[Results<br/>Analysis]

    Results --> Gate2{Gate 2:<br/>Hypothesis Validated?}

    Gate2 -->|YES<br/>Proceed to PoC| PoC[POC<br/>Real-world validation]
    Gate2 -->|NO<br/>Invalidated| Document1[Document<br/>learnings]

    PoC --> PoCResults[PoC Results<br/>& Recommendation]

    PoCResults --> Gate3{Gate 3:<br/>PoC Recommendation?}

    Gate3 -->|PROCEED<br/>Success criteria met| ADR1[ADR<br/>Adoption]
    Gate3 -->|PIVOT<br/>Try alternative| Alternative[Explore<br/>different approach]
    Gate3 -->|STOP<br/>Not feasible| ADR2[ADR<br/>Rejection]

    ADR1 --> Gate4{Gate 4:<br/>Budget Approval?}

    Gate4 -->|APPROVED<br/>$$ allocated| Production[Production<br/>Implementation]
    Gate4 -->|REJECTED<br/>No budget| Defer[Defer/<br/>Deprioritize]

    Production --> Success[Launch &<br/>Monitor]

    Document1 --> Knowledge[Knowledge<br/>Base]
    ADR2 --> Knowledge

    style Gate1 fill:#FFD700
    style Gate2 fill:#FFD700
    style Gate3 fill:#FFD700
    style Gate4 fill:#FFD700
    style ADR1 fill:#DDA0DD
    style ADR2 fill:#DDA0DD
    style Production fill:#98FB98
    style Success fill:#98FB98
    style Knowledge fill:#E0FFFF
```

**Decision Gates (kluczowe checkpoints):**

1. **Gate 1: Hypothesis Approval** - Czy badanie warte investment?
2. **Gate 2: Validation** - Czy hipoteza potwierdzona danymi?
3. **Gate 3: PoC Recommendation** - Proceed/Pivot/Stop?
4. **Gate 4: Budget Approval** - Czy inwestujemy w produkcję?

---

## Research vs Implementation Ratio

**Optymalna alokacja czasu:**

```mermaid
pie title Research vs Implementation Effort Distribution
    "Research (20-30%)" : 25
    "Implementation (60-70%)" : 65
    "Monitoring & Iteration (10%)" : 10
```

**Best practice:**
- **Zbyt mało research (<10%):** High risk bad decisions, wasted implementation
- **Zbyt dużo research (>40%):** Analysis paralysis, opportunity cost
- **Sweet spot (20-30%):** Data-driven decisions, confident implementation

---

## Complexity vs Research Depth

**Kiedy inwestować więcej w research:**

```mermaid
graph TD
    Decision([Decision to make]) --> Complexity{Complexity &<br/>Impact assessment}

    Complexity -->|Low complexity<br/>Low impact<br/>$$ < $10K| Quick[Quick Decision<br/>SPIKE 2-3 days<br/>or skip research]

    Complexity -->|Medium complexity<br/>Medium impact<br/>$$ $10K-$50K| Standard[Standard Research<br/>HYPOTHESIS + POC<br/>4-6 weeks]

    Complexity -->|High complexity<br/>High impact<br/>$$ > $50K| Deep[Deep Research<br/>ALTERNATIVE + HYPOTHESIS<br/>+ EXPERIMENT + POC<br/>8-12 weeks]

    Complexity -->|Critical decision<br/>Very high impact<br/>$$ > $100K| Parallel[Parallel Exploration<br/>CONCEPT BRANCHES<br/>Multiple teams<br/>12-16 weeks]

    style Quick fill:#90EE90
    style Standard fill:#87CEEB
    style Deep fill:#FFB6C1
    style Parallel fill:#FFD700
```

**Zasada:** Research investment proporcjonalny do:
- Complexity (technical/business)
- Impact (revenue, users, strategic)
- Cost of wrong decision ($$, time, opportunity cost)

---

## Template Selection Matrix

**Quick reference - który szablon wybrać:**

```mermaid
graph TD
    Q1{Czy masz<br/>wiele opcji<br/>do porównania?} -->|TAK<br/>3+ opcje| ALT[ALTERNATIVE-EXPLORATION]
    Q1 -->|NIE| Q2{Ile masz<br/>czasu?}

    Q2 -->|2-5 dni| SPIKE[SPIKE-SOLUTION]
    Q2 -->|1-2 tygodnie| Q3{Potrzebujesz<br/>real-world<br/>validation?}
    Q2 -->|4+ tygodnie| HYP[HYPOTHESIS-DOC<br/>+ EXPERIMENT-LOG]

    Q3 -->|TAK| POC[POC-DOC]
    Q3 -->|NIE| SPIKE

    Q4{Agregacja<br/>wyników z wielu<br/>badań?} -->|TAK| FINDINGS[RESEARCH-FINDINGS]

    Q5{Parallel<br/>exploration<br/>2 approaches?} -->|TAK| BRANCH[CONCEPT-BRANCH]

    style ALT fill:#FFD700
    style SPIKE fill:#90EE90
    style POC fill:#87CEEB
    style HYP fill:#FFB6C1
    style FINDINGS fill:#98FB98
    style BRANCH fill:#DDA0DD
```

---

## Legenda kolorów

W diagramach używane są następujące kolory dla czytelności:

| Kolor | Znaczenie | Przykład |
|-------|-----------|----------|
| 🟢 **Zielony (#90EE90)** | Spike / Quick decisions | SPIKE-SOLUTION |
| 🔵 **Niebieski (#87CEEB)** | Experiments / PoC | EXPERIMENT-LOG, POC-DOC |
| 🌸 **Różowy (#FFB6C1)** | Hypotheses / Problems | HYPOTHESIS-DOC |
| 🟡 **Żółty (#FFD700)** | Analysis / Comparison | ALTERNATIVE-EXPLORATION |
| 🟣 **Fioletowy (#DDA0DD)** | Decisions / ADR | Architecture Decision Records |
| 🟢 **Jasny zielony (#98FB98)** | Success / Production | Research Findings, Production |
| 🔶 **Pomarańczowy (#FFE4B5)** | Strategic / Roadmap | Roadmap, Strategy |
| 💧 **Cyan (#E0FFFF)** | Knowledge / Archive | Knowledge Base |

---

## Jak używać tych diagramów

### Osadzanie w dokumentach

```markdown
# Twój dokument

## Workflow

```mermaid
[skopiuj diagram stąd]
\```
```

### Renderowanie

**Narzędzia wspierające Mermaid:**
- **GitHub/GitLab:** Automatyczne renderowanie w README.md
- **Obsidian:** Plugin Mermaid
- **VS Code:** Mermaid Preview extension
- **Online:** https://mermaid.live/

### Eksport do obrazów

**Mermaid Live Editor:**
1. Otwórz https://mermaid.live/
2. Wklej kod diagramu
3. Export → PNG/SVG/PDF

---

## Modyfikacja diagramów

### Zmiana kolorów

```mermaid
graph TD
    Node1[Twój node]

    style Node1 fill:#TWÓJ_KOLOR,stroke:#333,stroke-width:2px
```

### Dodanie ikon

```mermaid
graph TD
    Success[✅ Success]
    Warning[⚠️ Warning]
    Error[❌ Error]
    Info[ℹ️ Info]
```

### Zmiana kierunku

```mermaid
graph LR  # Left to Right
graph TD  # Top to Down
graph BT  # Bottom to Top
graph RL  # Right to Left
```

---

## Więcej zasobów

**Mermaid dokumentacja:**
- https://mermaid.js.org/
- https://mermaid.js.org/syntax/flowchart.html
- https://mermaid.js.org/syntax/gantt.html

**Research Templates:**
- [README.md](./README.md) - Główna dokumentacja
- [/templates/research/](.) - Szablony
- [/examples/research/](../../examples/research/) - Przykłady

---

**Ostatnia aktualizacja:** 2025-12-29
**Wersja:** 1.0
**Maintainer:** Zespół Dokumentacji Ishkarim
