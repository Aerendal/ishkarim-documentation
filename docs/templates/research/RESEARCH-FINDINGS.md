# RESEARCH-FINDINGS: [Research Area] - [Title]

---

## Document Metadata

```yaml
id: RESEARCH-FINDINGS-[XXX]
doctype: RESEARCH-FINDINGS
status: draft  # draft | in-review | approved | published
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
research_area: [Area of research]
```

---

## Cross-References

```yaml
dependencies:
  - id: EXPERIMENT-LOG-*
    type: requires
    reason: "Research Findings agregują wyniki z eksperymentów"

impacts:
  - id: PRD
    type: influences
    reason: "Wyniki badań kształtują wymagania produktowe"
  - id: ADR
    type: informs
    reason: "Findings wspierają decyzje architektoniczne danymi"
  - id: INNOVATION-ROADMAP
    type: influences
    reason: "Wyniki badań wpływają na priorytety innowacji"
```

---

## SEC-RF-SUMMARY: Executive summary wyników

### Okres badawczy
**From:** YYYY-MM-DD
**To:** YYYY-MM-DD
**Duration:** [X weeks/months]

### Cel badań
[Jaki był główny cel tego research effort]

### Kluczowe wnioski (TL;DR)
1. [Wniosek 1]
2. [Wniosek 2]
3. [Wniosek 3]

### Overall Verdict
**[SUCCESS | PARTIAL SUCCESS | FAILURE | INCONCLUSIVE]**

[Krótkie uzasadnienie verdyktu]

### Strategic Implications
[Jak te wyniki wpływają na strategię produktu/projektu]

---

## SEC-RF-EXPERIMENTS: Przeprowadzone eksperymenty (lista)

### Completed Experiments

| ID | Title | Status | Hypothesis Result | Key Metric | Date |
|----|-------|--------|------------------|------------|------|
| [EXP-001] | [Tytuł] | ✅ Complete | ✅ Confirmed | [Metryka: wartość] | YYYY-MM-DD |
| [EXP-002] | [Tytuł] | ✅ Complete | ❌ Rejected | [Metryka: wartość] | YYYY-MM-DD |
| [EXP-003] | [Tytuł] | ⚠️ Inconclusive | ⚠️ Mixed | [Metryka: wartość] | YYYY-MM-DD |

### Related Research Artifacts
- [HYPOTHESIS-001]: [Tytuł]
- [POC-002]: [Tytuł]
- [SPIKE-003]: [Tytuł]

### Research Timeline
```
[Timeline visualization or description]
Week 1-2: [Activities]
Week 3-4: [Activities]
Week 5-6: [Activities]
```

---

## SEC-RF-KEY-FINDINGS: Kluczowe odkrycia

### Finding 1: [Title]
**Category:** [Technical | Business | UX | Performance | Security | etc.]
**Impact:** [High | Medium | Low]
**Confidence:** [High | Medium | Low]

**Description:**
[Szczegółowy opis odkrycia]

**Supporting Evidence:**
- [Evidence 1]: [Link do EXPERIMENT-LOG lub data]
- [Evidence 2]: [Link do EXPERIMENT-LOG lub data]

**Implications:**
[Co to odkrycie oznacza dla projektu]

---

### Finding 2: [Title]
**Category:** [Category]
**Impact:** [High | Medium | Low]
**Confidence:** [High | Medium | Low]

**Description:**
[Szczegółowy opis odkrycia]

**Supporting Evidence:**
- [Evidence 1]
- [Evidence 2]

**Implications:**
[Co to odkrycie oznacza dla projektu]

---

### Finding 3: [Title]
**Category:** [Category]
**Impact:** [High | Medium | Low]
**Confidence:** [High | Medium | Low]

**Description:**
[Szczegółowy opis odkrycia]

**Supporting Evidence:**
- [Evidence 1]
- [Evidence 2]

**Implications:**
[Co to odkrycie oznacza dla projektu]

---

## SEC-RF-PATTERNS: Wzorce i trendy

### Observed Patterns
1. **[Pattern 1]:**
   - Observed in: [Experiments/Contexts]
   - Frequency: [How often observed]
   - Significance: [Why this matters]

2. **[Pattern 2]:**
   - Observed in: [Experiments/Contexts]
   - Frequency: [How often observed]
   - Significance: [Why this matters]

### Trends Identified
**Trend 1: [Title]**
- Direction: [Increasing/Decreasing/Stable]
- Rate: [Quantify if possible]
- Projected impact: [Future implications]

**Trend 2: [Title]**
- Direction: [Increasing/Decreasing/Stable]
- Rate: [Quantify if possible]
- Projected impact: [Future implications]

### Cross-Experiment Correlations
[Czy różne eksperymenty pokazują związki przyczynowo-skutkowe?]
- [Correlation 1]
- [Correlation 2]

---

## SEC-RF-SURPRISES: Niespodzianki i anomalie

### Unexpected Findings
1. **[Surprise 1]:**
   - What we expected: [Oczekiwanie]
   - What we found: [Rzeczywistość]
   - Why surprising: [Uzasadnienie]
   - Possible explanations: [Hipotezy wyjaśniające]

2. **[Surprise 2]:**
   - What we expected: [Oczekiwanie]
   - What we found: [Rzeczywistość]
   - Why surprising: [Uzasadnienie]
   - Possible explanations: [Hipotezy wyjaśniające]

### Anomalies
| Anomaly | Experiment | Frequency | Resolved? | Notes |
|---------|-----------|-----------|-----------|-------|
| [Anomalia 1] | [EXP-ID] | [One-time/Recurring] | ✅/❌ | [Notes] |
| [Anomalia 2] | [EXP-ID] | [One-time/Recurring] | ✅/❌ | [Notes] |

### Contradictory Results
[Czy różne eksperymenty dały sprzeczne wyniki?]
- [Contradiction 1]: [Wyjaśnienie]
- [Contradiction 2]: [Wyjaśnienie]

---

## SEC-RF-IMPLICATIONS: Implikacje dla projektu

### Product Implications
**For Product Roadmap:**
- [Implication 1]
- [Implication 2]

**For Features:**
- [Implication 1]
- [Implication 2]

**For User Experience:**
- [Implication 1]
- [Implication 2]

### Technical Implications
**For Architecture:**
- [Implication 1]
- [Implication 2]

**For Technology Stack:**
- [Implication 1]
- [Implication 2]

**For Performance:**
- [Implication 1]
- [Implication 2]

### Business Implications
**For Strategy:**
- [Implication 1]
- [Implication 2]

**For Budget/Resources:**
- [Implication 1]
- [Implication 2]

**For Timeline:**
- [Implication 1]
- [Implication 2]

### Risk Implications
**New Risks Identified:**
- [Risk 1]: [Severity] - [Mitigation]
- [Risk 2]: [Severity] - [Mitigation]

**Risks Mitigated:**
- [Risk 1]: [How mitigated]
- [Risk 2]: [How mitigated]

---

## SEC-RF-RECOMMENDATIONS: Rekomendacje

### High Priority Recommendations
1. **[Recommendation 1]:**
   - **Action:** [Co zrobić]
   - **Owner:** [Kto odpowiedzialny]
   - **Timeline:** [Kiedy]
   - **Impact:** [Oczekiwany wpływ]
   - **Based on:** [Finding X, Y, Z]

2. **[Recommendation 2]:**
   - **Action:** [Co zrobić]
   - **Owner:** [Kto odpowiedzialny]
   - **Timeline:** [Kiedy]
   - **Impact:** [Oczekiwany wpływ]
   - **Based on:** [Finding X, Y, Z]

### Medium Priority Recommendations
1. **[Recommendation 3]:**
   - **Action:** [Co zrobić]
   - **Owner:** [Kto odpowiedzialny]
   - **Timeline:** [Kiedy]
   - **Impact:** [Oczekiwany wpływ]

### Low Priority / Nice-to-Have
- [Recommendation 4]
- [Recommendation 5]

### Decisions Needed
- [ ] [Decision 1]: [Description] - [Decision maker]
- [ ] [Decision 2]: [Description] - [Decision maker]

---

## SEC-RF-FUTURE-RESEARCH: Przyszłe badania

### Unanswered Questions
1. [Question 1]
2. [Question 2]
3. [Question 3]

### Proposed Follow-up Research
**Research 1: [Title]**
- **Objective:** [Cel]
- **Approach:** [Metodologia]
- **Effort:** [Estimated timeline/resources]
- **Priority:** [High/Medium/Low]

**Research 2: [Title]**
- **Objective:** [Cel]
- **Approach:** [Metodologia]
- **Effort:** [Estimated timeline/resources]
- **Priority:** [High/Medium/Low]

### Knowledge Gaps
[Co nadal nie wiemy i dlaczego to ważne]
- [Gap 1]
- [Gap 2]

### Emerging Opportunities
[Nowe możliwości zidentyfikowane podczas badań]
- [Opportunity 1]
- [Opportunity 2]

---

## Data Summary

### Aggregated Metrics
| Metric | Min | Max | Avg | Median | Std Dev |
|--------|-----|-----|-----|--------|---------|
| [Metric 1] | [Value] | [Value] | [Value] | [Value] | [Value] |
| [Metric 2] | [Value] | [Value] | [Value] | [Value] | [Value] |

### Success Rate
**Hypotheses tested:** [X]
**Hypotheses confirmed:** [Y] ([Z%])
**Hypotheses rejected:** [A] ([B%])
**Inconclusive:** [C] ([D%])

### ROI Analysis
**Research investment:**
- Time: [X person-hours]
- Cost: $[Y]

**Value delivered:**
- Bad decisions avoided: [X]
- Good decisions validated: [Y]
- Estimated saved cost: $[Z]

**ROI:** [Ratio]

---

## EVIDENCE: Dowody i materiały

### Raw Data
- [Dataset 1]: [Location/Link]
- [Dataset 2]: [Location/Link]

### Visualizations
- [Chart/Graph 1]: [Link]
- [Chart/Graph 2]: [Link]

### Reports
- [Detailed report 1]: [Link]
- [Detailed report 2]: [Link]

### Presentations
- [Stakeholder presentation]: [Link]
- [Team demo]: [Link]

---

## APPROVAL: Zatwierdzenia

| Role | Name | Decision | Date | Comments |
|------|------|----------|------|----------|
| [Research Lead] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |
| [Product Owner] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |
| [Tech Lead] | [Name] | Approve/Reject | YYYY-MM-DD | [Comments] |

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Initial draft |
| YYYY-MM-DD | 1.5 | [Imię Nazwisko] | Added experiments 1-3 |
| YYYY-MM-DD | 2.0 | [Imię Nazwisko] | Final findings and recommendations |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, lessons learned, kontekst dla przyszłych czytelników]

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** knowledge
