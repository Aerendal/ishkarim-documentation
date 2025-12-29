# Decision Templates - Ishkarim System

**Wersja:** 1.0
**Utworzone:** 2025-12-29
**Bazuje na:** PROPOZYCJA-3-Decision-Templates-Enhancement.md

---

## Przegląd

System Decision Templates wypełnia lukę między strategicznymi decyzjami architektonicznymi (ADR) a codziennymi decyzjami taktycznymi. Zawiera **5 specjalizowanych szablonów** które umożliwiają strukturalną dokumentację decyzji na różnych poziomach złożoności i formalności.

---

## Szablony Decision Templates

### 1. DECISION-LOG: Lightweight Decision Log

**Plik:** `DECISION-LOG-template.md`

**Czas wypełnienia:** 5-10 minut

**Kiedy używać:**
- Codzienne decyzje taktyczne (feature prioritization, bug triage)
- Decyzje wymagające dokumentacji, ale ADR jest overkill
- Sprint planning decisions
- Decisions gdzie kontekst może być zapomniany po tygodniu

**Przykłady:**
- Który feature zbudować w następnym sprincie?
- Która biblioteka do obsługi PDF?
- Czy naprawiać bug X czy Y jako pierwszy?

**Scope:** Tactical/operational
**Stakeholders:** Single decision owner
**Lifecycle:** Short-term (sprint/quarter)

---

### 2. TRADE-OFF-ANALYSIS: Structured Trade-off Analysis

**Plik:** `TRADE-OFF-ANALYSIS-template.md`

**Czas wypełnienia:** 2-4 godziny

**Kiedy używać:**
- Decisions z multiple competing criteria (performance vs cost vs maintainability)
- Decisions gdzie stakeholders mają różne priorities
- Decisions wymagające quantitative scoring
- Complex technical/business decisions where data is available

**Przykłady:**
- Wybór message queue: RabbitMQ vs Kafka vs AWS SQS
- Pricing model change: per-user vs per-feature
- Cloud provider selection z weighted criteria

**Wartość dodana:**
- ✅ Quantitative scoring (weighted criteria)
- ✅ Sensitivity analysis (robustness testing)
- ✅ Transparent trade-offs
- ✅ Stakeholders mogą debate weights, nie opinions

---

### 3. OPTION-COMPARISON-MATRIX: Option Comparison Matrix

**Plik:** `OPTION-COMPARISON-MATRIX-template.md`

**Czas wypełnienia:** 3-6 godzin

**Kiedy używać:**
- Vendor selection (3-5 vendors)
- Tool selection (comprehensive comparison)
- Partner selection
- Platform selection
- Qualitative side-by-side comparison

**Przykłady:**
- CRM selection: Salesforce vs HubSpot vs Zoho
- CI/CD tool: Jenkins vs GitLab CI vs CircleCI
- Payment gateway: Stripe vs PayPal vs Square

**Różnica vs Trade-off Analysis:**
- **Trade-off Analysis** = quantitative, weighted scoring, mathematical
- **Option Comparison Matrix** = qualitative, comprehensive narrative, side-by-side

---

### 4. GO-NO-GO-DECISION: Go/No-Go Decision Template

**Plik:** `GO-NO-GO-DECISION-template.md`

**Czas wypełnienia:** 1-2 godziny

**Kiedy używać:**
- Sprint/release go/no-go (ship now vs delay)
- Feature flag enablement (100% rollout vs rollback)
- Market launch decisions
- MVP launch decisions
- Major deployment decisions

**Przykłady:**
- Czy wypuścić Sprint 15 do produkcji?
- Czy włączyć nowy feature dla 100% users?
- Czy podpisać vendor contract?

**Różnica vs Feasibility Study:**
- **Feasibility Study** = high-level, project initiation (months ahead)
- **Go/No-Go** = tactical, immediate decision (days/weeks ahead)

**Wartość dodana:**
- ✅ Clear criteria (checklist format)
- ✅ Risk/impact balanced
- ✅ Conditional GO option (flexible)
- ✅ Documented accountability

---

### 5. DECISION-REVERSAL: Decision Reversal Document

**Plik:** `DECISION-REVERSAL-template.md`

**Czas wypełnienia:** 3-5 godzin

**Kiedy używać:**
- Architecture decision nie sprawdziła się
- Vendor selection was wrong (migration needed)
- Feature removal (deprecate after launch)
- Pivot (change direction after trying approach)
- Any significant decision requiring reversal

**Przykłady:**
- MongoDB → PostgreSQL migration (performance issues)
- Remove feature X (poor adoption)
- Change from vendor Y to vendor Z

**Wartość dodana:**
- ✅ Honest retrospective (root cause analysis)
- ✅ Quantified cost of wrong decision
- ✅ Actionable lessons learned
- ✅ Knowledge sharing (prevent repetition)
- ✅ Psychological safety (OK to reverse when wrong)

---

## Decision Flow - Który szablon wybrać?

```
┌─────────────────────────────────────────┐
│   Potrzebuję podjąć decyzję             │
└──────────────┬──────────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Jaki typ?    │
        └──┬───────────┘
           │
     ┌─────┴─────────────────────────────────┐
     │                                        │
     ▼                                        ▼
┌─────────────────┐                  ┌──────────────────┐
│ Daily tactical  │                  │ Strategic/       │
│ decision?       │                  │ Complex?         │
│ (5-10 min)      │                  │                  │
└────┬────────────┘                  └────┬─────────────┘
     │                                     │
     ▼                                     │
  DECISION-LOG                             │
                                          │
                              ┌───────────┴─────────────┐
                              │                         │
                              ▼                         ▼
                    ┌──────────────────┐      ┌──────────────────┐
                    │ Launch/Binary    │      │ Need comparison  │
                    │ decision?        │      │ or trade-offs?   │
                    └────┬─────────────┘      └────┬─────────────┘
                         │                          │
                         ▼                          │
                    GO-NO-GO-DECISION               │
                                        ┌───────────┴────────────┐
                                        │                        │
                                        ▼                        ▼
                              ┌──────────────────┐    ┌──────────────────┐
                              │ 3-5 options      │    │ Weighted         │
                              │ Qualitative?     │    │ criteria?        │
                              │                  │    │ Quantitative?    │
                              └────┬─────────────┘    └────┬─────────────┘
                                   │                       │
                                   ▼                       ▼
                         OPTION-COMPARISON-MATRIX  TRADE-OFF-ANALYSIS


┌─────────────────────────────────────────┐
│   Decyzja nie sprawdziła się?           │
└──────────────┬──────────────────────────┘
               │
               ▼
        DECISION-REVERSAL
```

---

## Integracja z istniejącym systemem

### Relacja do ADR (Architecture Decision Records)

| Aspekt | ADR | DECISION-LOG | TRADE-OFF-ANALYSIS | OPTION-COMPARISON |
|--------|-----|--------------|-------------------|------------------|
| **Czas** | 1-2h | 5-10 min | 2-4h | 3-6h |
| **Scope** | Strategic | Tactical | Complex | Comparison |
| **Detail** | High | Medium | High (quantitative) | High (qualitative) |
| **Lifecycle** | Years | Sprint/quarter | Months | Months |

**Integration pattern:**
```
OPTION-COMPARISON → TRADE-OFF-ANALYSIS → ADR → TDD
       ↓                    ↓
    Qualitative        Quantitative
    shortlist          scoring
```

### Relacja do innych szablonów

**FEASIBILITY-STUDY** ← `GO-NO-GO-DECISION`
Feasibility Study feeds into GO-NO-GO dla project start

**BUSINESS-CASE** ← `TRADE-OFF-ANALYSIS`
Business Case may reference Trade-off Analysis dla detailed comparison

**SPRINT-CORE** ← `DECISION-LOG`
Sprint planning artifacts include Decision Logs

**POC-DOC** → `TRADE-OFF-ANALYSIS`
PoC data feeds into trade-off scoring

---

## Wymagane dokumenty satelitarne

### DECISION-LOG
- **Required:** Brak
- **Optional:** EVIDENCE (jeśli decision based on data)

### TRADE-OFF-ANALYSIS
- **Required:** EVIDENCE (scoring data), APPROVAL (formal sign-off)
- **Optional:** POC-DOC (benchmark results)

### OPTION-COMPARISON-MATRIX
- **Required:** EVIDENCE (vendor docs, demos, pricing)
- **Optional:** APPROVAL

### GO-NO-GO-DECISION
- **Required:** APPROVAL (especially for high-risk GO)
- **Optional:** RELEASE-CHECKLIST, TESTING-RESULTS

### DECISION-REVERSAL
- **Required:** APPROVAL (reversal sign-off), EVIDENCE (failure data)
- **Optional:** MIGRATION-PLAN

---

## Metryki sukcesu

**M1: Decision Documentation Rate**
Target: >70% decyzji documented (vs current ~20% ADR-only)

**M2: Lightweight Decision Adoption**
Target: >60% tactical decisions use DECISION-LOG

**M3: Reversal Rate**
Target: <10% (vs current ~20% gut-feeling decisions)

**M4: Stakeholder Alignment Score**
Target: >4.0/5 (vs current ~2.8/5) - "Do you understand decision rationale?"

**M5: Time to Decision**
Target: <7 dni dla tactical, <30 dni dla strategic

---

## Przykłady użycia

### Scenariusz 1: Feature prioritization (Daily)
**Template:** DECISION-LOG
**Czas:** 5 minut
**Outcome:** Documented rationale dlaczego Feature A > Feature B

### Scenariusz 2: Vendor selection (CRM)
**Templates:**
1. OPTION-COMPARISON-MATRIX (shortlist 5 → 3)
2. TRADE-OFF-ANALYSIS (score top 3)
3. ADR (final decision)

**Czas:** ~8 godzin total
**Outcome:** Systematic, auditable vendor selection

### Scenariusz 3: MVP Launch decision
**Template:** GO-NO-GO-DECISION
**Czas:** 1-2 godziny
**Outcome:** Clear go/no-go z documented risks/conditions

### Scenariusz 4: Architecture reversal (MongoDB → PostgreSQL)
**Templates:**
1. DECISION-REVERSAL (honest retrospective)
2. ADR-NEW (new architecture decision)
3. MIGRATION-PLAN (execution)

**Czas:** ~5 godzin reversal doc + implementation
**Outcome:** Lessons learned, prevented repetition

---

## Najlepsze praktyki

### 1. Use the lightest template that fits
- Nie używaj TRADE-OFF-ANALYSIS dla simple 2-option decision
- Zacznij od DECISION-LOG jeśli unsure

### 2. Build up complexity
```
DECISION-LOG → TRADE-OFF-ANALYSIS → ADR
    (5 min)        (2-4h)          (1-2h)
```

### 3. Link decisions together
- DECISION-REVERSAL zawsze linkuje do original ADR
- TRADE-OFF-ANALYSIS feeds into ADR context

### 4. Be honest in reversals
- DECISION-REVERSAL to miejsce na honest root cause analysis
- Quantify costs (pokazuje value lepszych decisions)

### 5. Update templates based on learnings
- Lessons z DECISION-REVERSAL → update PoC/ADR templates

---

## Cross-References

**Proposal źródłowy:**
`/proposals/PROPOZYCJA-3-Decision-Templates-Enhancement.md`

**Related templates:**
- `/templates/adr-template-proof-system.md` - ADR template
- `/templates/supporting/` - Supporting document templates
- `/satellites/approvals/` - Approval templates
- `/satellites/evidence/` - Evidence templates

**Powiązane dokumenty:**
- `engineering/decisions/` - Example decision documents
- `dependency_graph.md` - Document relationship mapping

---

## Wsparcie i pytania

**Pytania implementacyjne:**
Zobacz przykłady w `engineering/decisions/` (jeśli istnieją)

**Aktualizacje szablonów:**
Lessons learned z DECISION-REVERSAL documents powinny prowadzić do continuous improvement tych templates.

**Feedback:**
Jeśli templates są za ciężkie/lekkie, dostosuj je do swojego use case. Better imperfect documentation niż zero documentation.

---

**Ostatnia aktualizacja:** 2025-12-29
**Status:** Implemented
**Następny review:** Po 3 miesiącach użytkowania (Q2 2026)
