# CONCEPT-BRANCH: [Branch ID] - [Alternative Approach Title]

---

## Document Metadata

```yaml
id: CONCEPT-BRANCH-[XXX]
doctype: CONCEPT-BRANCH
status: draft  # draft | active | paused | merged | killed | completed
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
parent_concept: [Parent concept ID]
branch_id: [Unique branch identifier]
```

---

## Cross-References

```yaml
dependencies:
  - id: PARENT-CONCEPT
    type: requires
    reason: "Branch powstaje z istniejącego konceptu głównego"

impacts:
  - id: RESEARCH-FINDINGS
    type: influences
    reason: "Wyniki z branchy są agregowane w Research Findings"
  - id: ADR
    type: blocks
    reason: "Decyzja merge/kill wymaga ADR"
```

---

## SEC-CB-DIVERGENCE: Punkt rozwidlenia (fork point)

### Parent Concept
**ID:** [PARENT-CONCEPT-ID]
**Title:** [Tytuł parent concept]
**Link:** [Link do dokumentu parent]

### Fork Point
**Date:** YYYY-MM-DD
**Version of parent:** [Version number]
**State at fork:** [Status parent concept w momencie forka]

### Triggering Event
[Co spowodowało utworzenie nowej gałęzi badawczej?]
- [Reason 1]
- [Reason 2]

### Alternative Question
[Jakie alternatywne pytanie ta gałąź eksploruje?]

---

## SEC-CB-RATIONALE: Dlaczego nowa gałąź

### Problem with Parent Approach
[Co jest problematyczne lub ograniczające w podejściu parent?]
- [Issue 1]
- [Issue 2]
- [Issue 3]

### Opportunity Identified
[Jaka okazja została zidentyfikowana, która uzasadnia eksplorację alternatywnej ścieżki?]

### Hypothesis for Branch
**H0 (Parent approach):** [Hipoteza dla parent]
**H1 (This branch):** [Hipoteza dla tej gałęzi]

### Success Criteria for Branch
- [ ] [Kryterium 1 - musi być lepsze niż parent]
- [ ] [Kryterium 2 - musi być lepsze niż parent]
- [ ] [Kryterium 3 - musi być lepsze niż parent]

### Resources Allocated
- **Team:** [Liczba osób/% czasu]
- **Budget:** $[Amount]
- **Timeline:** [Duration]

---

## SEC-CB-APPROACH: Alternatywne podejście

### Key Differences from Parent

| Aspect | Parent Approach | This Branch |
|--------|----------------|-------------|
| [Aspect 1] | [Parent method] | [Branch method] |
| [Aspect 2] | [Parent method] | [Branch method] |
| [Aspect 3] | [Parent method] | [Branch method] |

### Technical Approach
[Szczegółowy opis alternatywnego podejścia technicznego]

### Architecture (if applicable)
```
[Diagram lub opis architektury dla tej gałęzi]
```

### Methodology
[Jak będzie prowadzona eksploracja w tej gałęzi]

### Scope of Exploration
**In scope:**
- [Obszar 1]
- [Obszar 2]

**Out of scope:**
- [Obszar 1]
- [Obszar 2]

---

## SEC-CB-PROGRESS: Progress tracking

### Timeline

| Phase | Start | End | Status | Notes |
|-------|-------|-----|--------|-------|
| [Phase 1] | YYYY-MM-DD | YYYY-MM-DD | ✅/⏳/❌ | [Notes] |
| [Phase 2] | YYYY-MM-DD | YYYY-MM-DD | ✅/⏳/❌ | [Notes] |
| [Phase 3] | YYYY-MM-DD | YYYY-MM-DD | ✅/⏳/❌ | [Notes] |

### Milestones

- [x] [Milestone 1] - YYYY-MM-DD - ✅ Achieved
- [ ] [Milestone 2] - YYYY-MM-DD - ⏳ In progress
- [ ] [Milestone 3] - YYYY-MM-DD - 🔜 Upcoming

### Key Deliverables

- [x] [Deliverable 1]: [Link] - Completed YYYY-MM-DD
- [ ] [Deliverable 2]: [Link] - Expected YYYY-MM-DD
- [ ] [Deliverable 3]: [Link] - Expected YYYY-MM-DD

### Current Status Summary
[Krótki opis obecnego statusu gałęzi - max 3-4 zdania]

### Blockers
- [Blocker 1]: [Status/Resolution]
- [Blocker 2]: [Status/Resolution]

---

## SEC-CB-LEARNINGS: Learnings vs parent branch

### What Works Better
✅ **[Aspect 1]:**
- **Parent:** [Jak było w parent]
- **This branch:** [Jak jest w tej gałęzi]
- **Improvement:** [Quantify if possible]

✅ **[Aspect 2]:**
- **Parent:** [Jak było w parent]
- **This branch:** [Jak jest w tej gałęzi]
- **Improvement:** [Quantify if possible]

### What Works Worse
❌ **[Aspect 1]:**
- **Parent:** [Jak było w parent]
- **This branch:** [Jak jest w tej gałęzi]
- **Degradation:** [Quantify if possible]

### Trade-offs Identified
⚖️ **Trade-off 1:**
- **Gain:** [Co zyskujemy]
- **Loss:** [Co tracimy]
- **Worth it?:** [Yes/No/Unclear - uzasadnienie]

⚖️ **Trade-off 2:**
- **Gain:** [Co zyskujemy]
- **Loss:** [Co tracimy]
- **Worth it?:** [Yes/No/Unclear - uzasadnienie]

### Surprising Discoveries
💡 **[Discovery 1]:**
[Opis niespodziewanego odkrycia]

💡 **[Discovery 2]:**
[Opis niespodziewanego odkrycia]

### Comparative Metrics

| Metric | Parent Branch | This Branch | Delta | Target |
|--------|--------------|-------------|-------|--------|
| [Metric 1] | [Value] | [Value] | [±X%] | [Target] |
| [Metric 2] | [Value] | [Value] | [±X%] | [Target] |
| [Metric 3] | [Value] | [Value] | [±X%] | [Target] |

**Overall performance vs parent:** [Better/Worse/Mixed]

---

## SEC-CB-DECISION: Merge/Kill/Continue decision

### Current Recommendation: [MERGE | KILL | CONTINUE | PAUSED]

---

### Decision Rationale

#### If MERGE:
**Why merge:**
- [Reason 1 - based on metrics]
- [Reason 2 - based on learnings]
- [Reason 3 - based on strategic fit]

**What to merge:**
- [Element 1 to merge into main]
- [Element 2 to merge into main]
- [Element 3 to merge into main]

**What to discard from parent:**
- [Element 1 from parent to replace]
- [Element 2 from parent to replace]

**Merge strategy:**
[Jak będzie przeprowadzony merge - technical approach]

**Timeline for merge:**
- [Step 1]: [Deadline]
- [Step 2]: [Deadline]

**Risks of merge:**
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

---

#### If KILL:
**Why kill:**
- [Reason 1 - failed criteria]
- [Reason 2 - worse than parent]
- [Reason 3 - not worth continued investment]

**What we learned (valuable even if killing):**
- [Learning 1]
- [Learning 2]

**What to salvage:**
- [Insight/Artifact 1 to preserve]
- [Insight/Artifact 2 to preserve]

**Impact on parent branch:**
[Jak doświadczenia z tej gałęzi wpłyną na parent?]

---

#### If CONTINUE:
**Why continue:**
- [Reason 1 - promising but needs more time]
- [Reason 2 - critical questions unanswered]

**What needs to happen before decision:**
- [ ] [Milestone/Criteria 1]
- [ ] [Milestone/Criteria 2]

**Timeline to next decision point:**
[Date] - [What will be evaluated]

**Resource commitment:**
- Team: [X people]
- Budget: $[Y]
- Duration: [Z weeks]

---

#### If PAUSED:
**Why paused:**
- [Reason 1 - waiting for dependency]
- [Reason 2 - resource constraints]

**Conditions to resume:**
- [Condition 1]
- [Condition 2]

**Estimated resume date:**
[Date or "TBD pending [condition]"]

---

### Stakeholder Input

| Stakeholder | Role | Position | Rationale |
|------------|------|----------|-----------|
| [Name 1] | [Role] | Merge/Kill/Continue | [Their reasoning] |
| [Name 2] | [Role] | Merge/Kill/Continue | [Their reasoning] |
| [Name 3] | [Role] | Merge/Kill/Continue | [Their reasoning] |

### Final Decision
**Made by:** [Decision maker name]
**Date:** YYYY-MM-DD
**Decision:** [MERGE | KILL | CONTINUE | PAUSED]

---

## Next Actions

### Immediate Actions
- [ ] [Action 1] - [Owner] - [Deadline]
- [ ] [Action 2] - [Owner] - [Deadline]

### If Merging
- [ ] Create [ADR-XXX]: Decision to merge [branch] into main
- [ ] Create merge plan document
- [ ] Schedule stakeholder alignment meeting
- [ ] Update parent concept documentation

### If Killing
- [ ] Create [RESEARCH-FINDINGS] documenting learnings
- [ ] Archive branch artifacts
- [ ] Reallocate resources
- [ ] Communicate to stakeholders

### If Continuing
- [ ] Define next milestone
- [ ] Allocate resources for next phase
- [ ] Schedule next decision checkpoint

---

## Artifacts from Branch

### Code/Prototypes
```
Repository: [Link]
Branch: concept-branch/[branch-id]
Key commits: [List]
```

### Documents Produced
- [Document 1]: [Link]
- [Document 2]: [Link]

### Data/Metrics
- [Dataset 1]: [Link]
- [Benchmark results]: [Link]

### Presentations
- [Presentation to stakeholders]: [Link]
- [Demo recording]: [Link]

---

## TODO_SECTION: Zadania dla tej gałęzi

### Do zrobienia
- [ ] [Zadanie 1]
- [ ] [Zadanie 2]

### W trakcie
- [Zadanie obecnie realizowane]

### Zrealizowane
- [x] [Zadanie zakończone 1]
- [x] [Zadanie zakończone 2]

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Branch created from parent |
| YYYY-MM-DD | 1.5 | [Imię Nazwisko] | Phase 1 completed |
| YYYY-MM-DD | 2.0 | [Imię Nazwisko] | Decision made: [MERGE/KILL/CONTINUE] |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, kontekst, refleksje zespołu]

---

## Example: Parallel Architecture Exploration

**Parent Concept:** AI model for churn prediction

**Branch A:** Transformer-based approach
- Team: 2 data scientists
- Duration: 4 weeks
- Results: 78% accuracy, 50ms inference
- **Decision:** MERGE (for real-time predictions)

**Branch B:** Graph Neural Network approach
- Team: 2 data scientists
- Duration: 4 weeks
- Results: 83% accuracy, 300ms inference
- **Decision:** MERGE (for batch predictions)

**Outcome:** Hybrid approach - both branches merged for different use cases

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation-management
