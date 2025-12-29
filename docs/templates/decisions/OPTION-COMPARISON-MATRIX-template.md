# OPTION-COMPARISON-MATRIX: Option Comparison Matrix

---
**Meta (WYMAGANE):**
```yaml
id: OPTION-COMPARISON-MATRIX-[NNN]
doctype: OPTION-COMPARISON-MATRIX
status: [draft/in-review/approved/finalized]
version: "1.0"
owner: "[Comparison Owner Name]"
project: "[Project Name]"
comparison_type: "[vendor_selection/tool_selection/partner_selection/platform_selection/other]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
```

**Cross-References:**
```yaml
dependencies:
  - id: [VENDOR-REQUIREMENTS-DOC]
    type: requires
    reason: "Requirements drive comparison criteria"
  - id: POC-DOC-[NNN]
    type: influences
    reason: "PoC data informs comparison"

impacts:
  - id: TRADE-OFF-ANALYSIS-[NNN]
    type: influences
    reason: "Comparison matrix feeds into quantitative trade-off analysis"
  - id: ADR-[NNN]
    type: informs
    reason: "Final selection documented in ADR"
```

**Wymagane dokumenty satelitarne:**
- EVIDENCE-[NNN]: Supporting data (vendor docs, demos, pricing, feature lists)

---

## SEC-OCM-PURPOSE: Cel porównania

> **Cel:** Jasne określenie po co robimy to porównanie i czego szukamy.

**What we're comparing:**
[Np. "CRM platform dla sales team (target: 50 users, B2B SaaS sales)"]

**Business context:**
[Dlaczego to porównanie jest potrzebne? Jaki problem rozwiązuje?]

**Key requirements:**
1. [Requirement 1, np. "Must support 50+ users"]
2. [Requirement 2, np. "Budget: max $5K/month"]
3. [Requirement 3]
4. [...]

**Success criteria:**
[Jak będziemy wiedzieć że wybraliśmy dobrą opcję?]

---

## SEC-OCM-OPTIONS: Opcje (3-5)

> **Cel:** Lista wszystkich opcji, które są porównywane, plus eliminated options.

### Options evaluated

**Initial list (before screening):**
1. [Opcja 1]
2. [Opcja 2]
3. [Opcja 3]
4. [Opcja 4]
5. [Opcja 5]
[... więcej jeśli były]

### Shortlist (finalists)

**Final comparison includes:**
1. ✅ **[Opcja 1]** - [1 zdanie dlaczego w shortlist]
2. ✅ **[Opcja 2]** - [1 zdanie dlaczego w shortlist]
3. ✅ **[Opcja 3]** - [1 zdanie dlaczego w shortlist]

### Eliminated options

**Excluded from detailed comparison:**

#### [Opcja X] ❌
**Reason:** [Dlaczego eliminated, np. "Brak enterprise features wymaganych dla naszego use case"]
**Evaluation depth:** [Czy to było quick screen czy deeper evaluation]

#### [Opcja Y] ❌
**Reason:** [Dlaczego eliminated]
**Evaluation depth:** [...]

---

## SEC-OCM-CRITERIA: Kryteria porównania

> **Cel:** Zdefiniowanie kryteriów używanych do porównania opcji.

**Criteria selection rationale:**
[Dlaczego te kryteria są ważne dla naszego use case?]

### Functional criteria
1. **[Kryterium 1]** - [Definicja, czego dotyczy]
2. **[Kryterium 2]** - [Definicja]
3. **[...]**

### Non-functional criteria
1. **[Kryterium 1, np. "Performance"]** - [Definicja]
2. **[Kryterium 2, np. "Scalability"]** - [Definicja]
3. **[...]**

### Business criteria
1. **[Kryterium 1, np. "Pricing"]** - [Definicja]
2. **[Kryterium 2, np. "Vendor support"]** - [Definicja]
3. **[...]**

### Evaluation method
- **Rating scale:** [np. "⭐ 1-5 stars", "High/Medium/Low", "Numeric score 1-10"]
- **Data sources:** [Skąd data, np. "Vendor docs, demos, trials, reference customers"]

---

## SEC-OCM-MATRIX: Comparison matrix

> **Cel:** Side-by-side comparison wszystkich opcji według kryteriów.

### Matrix

| Kryterium | [Opcja 1] | [Opcja 2] | [Opcja 3] |
|-----------|-----------|-----------|-----------|
| **FUNCTIONAL** | | | |
| [Feature 1] | [Value/Rating + uzasadnienie] | [Value/Rating] | [Value/Rating] |
| [Feature 2] | [Value/Rating + uzasadnienie] | [Value/Rating] | [Value/Rating] |
| [Feature 3] | [Value/Rating + uzasadnienie] | [Value/Rating] | [Value/Rating] |
| **NON-FUNCTIONAL** | | | |
| Performance | [Rating + dane] | [Rating + dane] | [Rating + dane] |
| Scalability | [Rating + dane] | [Rating + dane] | [Rating + dane] |
| Reliability | [Rating + dane] | [Rating + dane] | [Rating + dane] |
| **BUSINESS** | | | |
| Pricing | [Price + breakdown] | [Price + breakdown] | [Price + breakdown] |
| Setup time | [Estimate + source] | [Estimate] | [Estimate] |
| Learning curve | [Assessment + rationale] | [Assessment] | [Assessment] |
| Support quality | [Rating + source] | [Rating] | [Rating] |
| Vendor stability | [Assessment] | [Assessment] | [Assessment] |
| **INTEGRATIONS** | | | |
| [Integration 1] | [Support level] | [Support level] | [Support level] |
| [Integration 2] | [Support level] | [Support level] | [Support level] |
| Ecosystem | [Rating + count] | [Rating + count] | [Rating + count] |

### Notes on ratings

**[Opcja 1]:**
- [Kluczowa uwaga 1]
- [Kluczowa uwaga 2]

**[Opcja 2]:**
- [Kluczowa uwaga 1]
- [Kluczowa uwaga 2]

**[Opcja 3]:**
- [Kluczowa uwaga 1]
- [Kluczowa uwaga 2]

---

## SEC-OCM-PROS-CONS: Pros/Cons per option

> **Cel:** Structured lista pros/cons dla każdej opcji.

### [Opcja 1]

#### Pros ✅
1. [Pro 1 - konkretny, measurable]
2. [Pro 2]
3. [Pro 3]
4. [...]

#### Cons ❌
1. [Con 1 - konkretny, measurable]
2. [Con 2]
3. [Con 3]
4. [...]

#### Overall assessment
[1-2 zdania podsumowania: dla kogo ta opcja jest najlepsza]

---

### [Opcja 2]

#### Pros ✅
1. [Pro 1]
2. [Pro 2]
3. [Pro 3]
4. [...]

#### Cons ❌
1. [Con 1]
2. [Con 2]
3. [Con 3]
4. [...]

#### Overall assessment
[1-2 zdania podsumowania]

---

### [Opcja 3]

#### Pros ✅
1. [Pro 1]
2. [Pro 2]
3. [Pro 3]
4. [...]

#### Cons ❌
1. [Con 1]
2. [Con 2]
3. [Con 3]
4. [...]

#### Overall assessment
[1-2 zdania podsumowania]

---

## SEC-OCM-RECOMMENDATION: Rekomendacja (top 1-2)

> **Cel:** Clear recommendation z uzasadnieniem.

### Top 1: [Opcja X] ⭐ RECOMMENDED

**Overall rating:** [Rating, np. "8.5/10" lub "Excellent"]

#### Dlaczego ta opcja wygrywa

1. **[Strength 1]** - [Szczegół i dlaczego to ważne]
2. **[Strength 2]** - [Szczegół i dlaczego to ważne]
3. **[Strength 3]** - [Szczegół i dlaczego to ważne]

#### Best for

- [Use case 1, np. "Teams prioritizing ease-of-use over customization"]
- [Use case 2]

#### Acceptable trade-offs

- [Trade-off 1, np. "Less customization than Opcja Y, ale sufficient for our needs"]
- [Trade-off 2]

---

### Top 2: [Opcja Y] 🥈 ALTERNATIVE

**Overall rating:** [Rating]

#### Dlaczego to dobra alternatywa

1. [Reason 1]
2. [Reason 2]

#### Best for / When to consider

- [Scenario 1, np. "If budget is tight (<$3K/mo)"]
- [Scenario 2]

#### Why not #1

- [Reason dlaczego nie primary recommendation]

---

### Eliminated from final recommendation

#### [Opcja Z] ❌

**Reason:**
[Dlaczego nie recommended, konkretne powody]

**Would be viable if:**
[W jakich warunkach ta opcja mogłaby być viable]

---

## Additional sections (opcjonalne)

### Total Cost of Ownership (TCO) comparison

| Cost component | [Opcja 1] | [Opcja 2] | [Opcja 3] |
|----------------|-----------|-----------|-----------|
| **Setup/Implementation** | [$X] | [$Y] | [$Z] |
| **License/Subscription (Year 1)** | [$X] | [$Y] | [$Z] |
| **Training** | [$X] | [$Y] | [$Z] |
| **Ongoing support** | [$X/year] | [$Y/year] | [$Z/year] |
| **Integration costs** | [$X] | [$Y] | [$Z] |
| **TOTAL (Year 1)** | **[$XX]** | **[$YY]** | **[$ZZ]** |
| **TOTAL (3-year)** | **[$XXX]** | **[$YYY]** | **[$ZZZ]** |

### Risk assessment

| Risk category | [Opcja 1] | [Opcja 2] | [Opcja 3] |
|---------------|-----------|-----------|-----------|
| Vendor lock-in | [High/Med/Low + rationale] | [...] | [...] |
| Implementation risk | [...] | [...] | [...] |
| Adoption risk | [...] | [...] | [...] |
| Technical risk | [...] | [...] | [...] |

### Reference customers / Case studies

**[Opcja 1]:**
- [Company 1 - similar size/industry - outcome]
- [Company 2 - outcome]

**[Opcja 2]:**
- [Company 1 - outcome]
- [Company 2 - outcome]

**[Opcja 3]:**
- [Company 1 - outcome]
- [Company 2 - outcome]

### Next steps

- [ ] [Action 1, np. "Schedule demo with vendor X"]
- [ ] [Action 2, np. "Request trial access dla top 2 options"]
- [ ] [Action 3, np. "Prepare detailed implementation plan dla selected option"]

---

**Szacowany czas wypełnienia:** 3-6 godzin (w zależności od liczby opcji i depth of evaluation)

**Wartość dodana:**
- ✅ Comprehensive side-by-side view (stakeholders see all options at once)
- ✅ Clear elimination criteria (shortlist rationalized)
- ✅ Structured pros/cons (not ad-hoc)
- ✅ Top 1-2 recommendation (clear next steps)

**Różnica vs Trade-off Analysis:**
- **Trade-off Analysis** = weighted scoring, quantitative, mathematical
- **Option Comparison Matrix** = qualitative, comprehensive side-by-side, narrative

**Kiedy używać:**
- Vendor selection (np. CRM: Salesforce vs HubSpot vs Zoho)
- Tool selection (np. CI/CD: Jenkins vs GitLab CI vs CircleCI)
- Partner selection (np. Payment gateway: Stripe vs PayPal vs Square)
- Platform selection (np. Cloud: AWS vs Azure vs GCP)
- 3-5 opcji które wymagają comprehensive comparison

**Kiedy NIE używać:**
- 2 opcje only → użyj DECISION-LOG lub TRADE-OFF-ANALYSIS
- Potrzeba quantitative scoring → użyj TRADE-OFF-ANALYSIS
- Simple tactical decision → użyj DECISION-LOG
- Launch decision → użyj GO-NO-GO-DECISION
