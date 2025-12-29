# Research Templates — Research & Exploration Framework

---

## 📋 Przeznaczenie

Folder **research/** zawiera **7 szablonów badawczych** do formalizacji eksploracji konceptów, eksperymentów, PoC i research spikes. Te szablony wypełniają krytyczną lukę w systemie Ishkarim między fazą przedprodukcyjną (Feasibility, Business Case) a fazą produkcyjną (ADR, TDD) — dostarczają strukturalne narzędzia dla **fazy discovery i research**.

## 🎯 Funkcja

Research templates służą do:
- **Formalizacji hipotez** — Strukturalne definiowanie testable assumptions
- **Tracking eksperymentów** — Timestamped logs z observations i results
- **Proof of Concept** — Validation criteria i decision framework (Proceed/Pivot/Stop)
- **Spike solutions** — Timeboxed research (max 2-5 dni) dla quick questions
- **Agregacji wyników** — Research Findings łączą wiele eksperymentów
- **Eksploracji alternatyw** — Systematyczne porównanie 3-5 opcji z weighted scoring
- **Parallel research** — Concept Branching dla fork-merge workflows

## 👥 Kto używa?

- **R&D Teams** — Hipotezy, eksperymenty, parallel exploration
- **Software Engineers** — Spikes, PoC, tech evaluation
- **Product Managers** — Business experiments (pricing, market tests)
- **Data Scientists** — ML model exploration, A/B tests
- **UX Designers** — User research, prototyping spikes
- **Architects** — Alternative architecture exploration, trade-off analysis

## 📂 Zawartość folderu (7 szablonów)

| Szablon | Czas wypełnienia | Use case |
|---------|------------------|----------|
| **HYPOTHESIS-DOC-template.md** | 30-60 min | Formalizacja testable hypothesis |
| **EXPERIMENT-LOG-template.md** | Continuous | Tracking eksperymentów (timestamped) |
| **POC-DOC-template.md** | 2-4h | Proof of Concept z validation criteria |
| **SPIKE-SOLUTION-template.md** | 1-2h | Timeboxed spike (MAX 5 dni) |
| **RESEARCH-FINDINGS-template.md** | 2-3h | Agregacja wyników z eksperymentów |
| **ALTERNATIVE-EXPLORATION-template.md** | 2-3h | Systematyczne porównanie 3-5 alternatives |
| **CONCEPT-BRANCH-template.md** | 1-2h | Fork-merge pattern dla parallel research |

## 🔗 Research Workflows

### Workflow 1: Tech Exploration (4-12 tygodni)
```
HYPOTHESIS → ALTERNATIVE-EXPLORATION → POC (top 2) → RESEARCH-FINDINGS → ADR → TDD
```

### Workflow 2: Agile Spike (2-5 dni)
```
USER-STORY (blocked) → SPIKE-SOLUTION → Answer → ADR (if needed) → USER-STORY (unblocked)
```

### Workflow 3: Parallel R&D (4-8 tygodni)
```
PARENT-HYPOTHESIS → CONCEPT-BRANCH-001 + BRANCH-002 → RESEARCH-FINDINGS → ADR
```

### Workflow 4: Business Experimentation (4-8 tygodni)
```
HYPOTHESIS → EXPERIMENT-LOG (A/B test) → RESEARCH-FINDINGS → ADR (pricing decision)
```

## 🚀 Quick Start

### Scenariusz 1: "Nie wiem czy technologia X będzie działać"
1. Utworzyć **HYPOTHESIS-DOC** z success criteria
2. Utworzyć **POC-DOC** (2-week PoC)
3. Track results w **EXPERIMENT-LOG**
4. Agreguj w **RESEARCH-FINDINGS**
5. Utworzyć **ADR** based on data

### Scenariusz 2: "Muszę szybko sprawdzić czy to możliwe" (Sprint)
1. Utworzyć **SPIKE-SOLUTION** (timebox 3 dni)
2. Answer: YES/NO/YES with conditions
3. Actions: Split user story, create ADR

### Scenariusz 3: "Mamy 3 opcje, która jest najlepsza?"
1. Utworzyć **ALTERNATIVE-EXPLORATION** z weighted criteria
2. Scoring każdej opcji (X/10 per criterion)
3. Sensitivity analysis (robust vs fragile)
4. Utworzyć **ADR** with recommendation

### Scenariusz 4: "Chcemy zbadać 2 podejścia równolegle"
1. **PARENT-HYPOTHESIS** defines goal
2. Fork: **CONCEPT-BRANCH-001** || **BRANCH-002**
3. Parallel execution (4 weeks)
4. Decision: MERGE winner, KILL loser
5. **RESEARCH-FINDINGS** aggregates

## ⚠️ Best Practices

### DO ✅
- Timeboxing: Hypothesis max 4 tyg, Spike MAX 5 dni
- Define success criteria BEFORE experiment
- Document failures (learnings valuable!)
- Link research → decisions (RESEARCH-FINDINGS → ADR)

### DON'T ❌
- Don't skip hypothesis (write it first!)
- Don't let spikes drag >5 days
- Don't do PoC in production
- Don't sequential when parallel makes sense

## 📖 Zobacz też

- **[../decisions/](../decisions/)** — Decision Templates - research feeds decisions!
- **[../pre-production/](../pre-production/)** — Feasibility Study identifies PoC needs
- **[../specs/specs_doc_types.md](../specs/)** — Research doctypes specifications

---

**Status:** ✅ 7 templates production-ready
**Wygenerowano:** 2025-12-29
**Podstawa:** PROPOZYCJA-1-Research-Branch-Templates.md
