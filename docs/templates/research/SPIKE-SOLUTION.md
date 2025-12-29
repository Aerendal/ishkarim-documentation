# SPIKE-SOLUTION: [Spike ID] - [Research Question Title]

---

## Document Metadata

```yaml
id: SPIKE-[XXX]
doctype: SPIKE-SOLUTION
status: draft  # draft | in-progress | completed | cancelled
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
spike_type: [technical | ux | business | architectural]
timebox: [X days]  # Max 2-5 days
```

---

## Cross-References

```yaml
dependencies:
  - id: SPRINT-BACKLOG
    type: research_input
    reason: "Spike jest timeboxed research w ramach sprintu"

impacts:
  - id: USER-STORY
    type: blocks
    reason: "Spike redukuje uncertainty przed implementacją user story"
  - id: ADR
    type: influences
    reason: "Technical spike może prowadzić do ADR"
```

---

## SEC-SPIKE-QUESTION: Pytanie badawcze

### Główne pytanie
[Sformułuj konkretne pytanie, na które spike ma odpowiedzieć]

### Kontekst
[Dlaczego to pytanie jest istotne w kontekście projektu]

### Related Work Items
- [User Story ID]: [Tytuł] - [Jak spike odnosi się do story]
- [Task ID]: [Tytuł] - [Jak spike odnosi się do zadania]

### Unknown/Risk
[Co nie wiemy? Jakie ryzyko chcemy zredukować?]

---

## SEC-SPIKE-WHY: Dlaczego teraz (business value)

### Business Impact
[Jak odpowiedź na to pytanie wpłynie na biznes/produkt]

### Blocker Status
- [ ] This spike blocks: [Work item ID]
- [ ] This spike is nice-to-have exploration

### Cost of Delay
[Co się stanie, jeśli nie odpowiemy na to pytanie teraz?]

### Value Proposition
[Jaka wartość wynika z przeprowadzenia tego spike]

---

## SEC-SPIKE-APPROACH: Podejście

### Timebox
- **Start:** YYYY-MM-DD
- **End:** YYYY-MM-DD
- **Duration:** [X days] (max 5 days)

### Scope
**Will investigate:**
- [Obszar 1]
- [Obszar 2]
- [Obszar 3]

**Will NOT investigate:**
- [Obszar poza zakresem 1]
- [Obszar poza zakresem 2]

### Methodology

**For Technical Spike:**
- [ ] Code exploration (existing codebase)
- [ ] Prototype implementation
- [ ] Library/Framework evaluation
- [ ] Performance testing
- [ ] Integration testing
- [ ] Other: [Specify]

**For UX Spike:**
- [ ] User research
- [ ] Wireframing/Prototyping
- [ ] Usability testing
- [ ] Accessibility audit
- [ ] Design system exploration
- [ ] Other: [Specify]

**For Business Spike:**
- [ ] Market research
- [ ] Competitor analysis
- [ ] Pricing model exploration
- [ ] Customer interviews
- [ ] Financial modeling
- [ ] Other: [Specify]

### Tools & Resources
- [Tool/Resource 1]
- [Tool/Resource 2]

### Success Criteria
[Jak będziemy wiedzieć, że spike zakończył się sukcesem?]
- [ ] [Kryterium 1]
- [ ] [Kryterium 2]

---

## SEC-SPIKE-FINDINGS: Odkrycia

### Day 1: [YYYY-MM-DD]
**Activities:**
- [Aktywność 1]
- [Aktywność 2]

**Discoveries:**
- [Odkrycie 1]
- [Odkrycie 2]

**Notes:**
[Notatki z pierwszego dnia]

---

### Day 2: [YYYY-MM-DD]
**Activities:**
- [Aktywność 1]
- [Aktywność 2]

**Discoveries:**
- [Odkrycie 1]
- [Odkrycie 2]

**Notes:**
[Notatki z drugiego dnia]

---

### Day 3: [YYYY-MM-DD]
**Activities:**
- [Aktywność 1]
- [Aktywność 2]

**Discoveries:**
- [Odkrycie 1]
- [Odkrycie 2]

**Notes:**
[Notatki z trzeciego dnia]

---

### Key Learnings Summary

**✅ What Worked:**
- [Learning 1]
- [Learning 2]

**❌ What Didn't Work:**
- [Learning 1]
- [Learning 2]

**⚠️ Concerns/Risks:**
- [Concern 1]
- [Concern 2]

**💡 Unexpected Findings:**
- [Niespodziewane odkrycie 1]
- [Niespodziewane odkrycie 2]

---

## SEC-SPIKE-ANSWER: Odpowiedź na pytanie

### Answer
**[YES | NO | YES, with conditions | NEEDS MORE RESEARCH]**

### Explanation
[Szczegółowe wyjaśnienie odpowiedzi na pytanie badawcze]

### Supporting Evidence
- [Evidence 1]
- [Evidence 2]
- [Evidence 3]

### Confidence Level
**[High | Medium | Low]** - [Uzasadnienie poziomu pewności]

### Conditions/Caveats (if applicable)
1. [Warunek 1]
2. [Warunek 2]

### Alternatives Considered
| Alternative | Pros | Cons | Verdict |
|------------|------|------|---------|
| [Option A] | [Pros] | [Cons] | ✅/❌ |
| [Option B] | [Pros] | [Cons] | ✅/❌ |

---

## SEC-SPIKE-ACTIONS: Akcje wynikowe

### Immediate Actions
- [ ] [Akcja 1] - [Owner] - [Deadline]
- [ ] [Akcja 2] - [Owner] - [Deadline]

### Documentation Updates
- [ ] Update [USER-STORY-XXX]: [Co zmienić]
- [ ] Create [ADR-XXX]: [Decision title] (if architectural decision needed)
- [ ] Update [TDD]: [Technical changes needed]

### Follow-up Work Items
- [ ] [New task 1]: [Description] - [Estimate]
- [ ] [New task 2]: [Description] - [Estimate]

### Recommendations

**For implementation:**
[Rekomendacje dotyczące implementacji]

**For further research:**
[Co warto jeszcze zbadać w przyszłości]

**For team:**
[Rekomendacje dla zespołu - training, dokumentacja, itp.]

---

## Code/Prototype (if applicable)

### Repository Info
```
Repository: [GitHub/GitLab URL]
Branch: spike/[spike-name]
Commit: [Commit hash]
```

### Key Files
- [File 1]: [Opis]
- [File 2]: [Opis]

### Running the Prototype
```bash
# Setup
git clone [repo]
cd [directory]
git checkout spike/[spike-name]

# Run
npm install
npm run spike:demo
```

### Screenshots/Demos
[Screenshots lub linki do demo]

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Spike initiated |
| YYYY-MM-DD | 1.5 | [Imię Nazwisko] | Day 1-2 findings |
| YYYY-MM-DD | 2.0 | [Imię Nazwisko] | Spike completed, answer provided |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, lessons learned, refleksje]

---

## Template Examples

### Example 1: Technical Spike

**Question:** Czy możemy użyć Rust WASM do przyspieszenia przetwarzania obrazów w przeglądarce?

**Timebox:** 3 dni

**Answer:** TAK, ale z warunkami:
- Lazy load WASM module (not main bundle)
- Fallback to JS for unsupported browsers
- Acceptable for 94% users

**Actions:**
- [ ] Create ADR-045: WASM for image processing
- [ ] Update US-123: Split implementation (WASM + fallback)
- [ ] Add browser compatibility testing to QA plan

---

### Example 2: UX Spike

**Question:** Which navigation pattern (sidebar vs top nav) provides better UX for our dashboard?

**Timebox:** 2 dni

**Answer:** Sidebar, with condition - needs to be collapsible for smaller screens

**Evidence:**
- 8/10 users preferred sidebar in usability test
- Task completion time: 20% faster with sidebar
- WCAG 2.1 AA compliance achieved

---

### Example 3: Business Spike

**Question:** Should we offer a free tier to increase user acquisition?

**Timebox:** 5 dni

**Answer:** YES, with conditions - limited features, 14-day trial for premium

**Evidence:**
- Competitor analysis: 80% of SaaS products offer free tier
- Customer interviews: 70% said they'd try free tier before buying
- Financial modeling: Break-even at 15% conversion rate (industry avg: 20%)

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** multi (tech/ux/business)
