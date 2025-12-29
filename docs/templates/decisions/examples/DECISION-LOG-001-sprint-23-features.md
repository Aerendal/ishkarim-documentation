# DECISION-LOG-001: Wybór features dla Sprint 23

---
**Meta (WYMAGANE):**
```yaml
id: DECISION-LOG-001
doctype: DECISION-LOG
status: approved
version: "1.0"
owner: "Anna Kowalska (Product Manager)"
project: "Ishkarim - Core Platform"
decision_type: feature_prioritization
decision_date: "2025-12-29"
created: "2025-12-29"
updated: "2025-12-29"
```

**Cross-References:**
```yaml
dependencies:
  - id: SPRINT-22-RETROSPECTIVE
    type: influences
    reason: "Retrospektywa Sprint 22 pokazała potrzebę skupienia na performance"
  - id: CUSTOMER-FEEDBACK-Q4-2025
    type: requires
    reason: "Decyzja bazuje na customer feedback z Q4"

impacts:
  - id: SPRINT-23-BACKLOG
    type: blocks
    reason: "Ta decyzja determinuje zawartość Sprint 23 backlog"
  - id: ROADMAP-Q1-2026
    type: informs
    reason: "Odrzucone features przesuwają się na Q1 2026"
```

---

## SEC-DL-QUESTION: Pytanie decyzyjne

Które 2 features z backlogu priorytetyzować do implementacji w Sprint 23 (capacity: 45 story points)?

---

## SEC-DL-CONTEXT: Kontekst (1-2 zdania)

Sprint 23 startuje 6 stycznia 2026, mamy capacity 45 SP (5 deweloperów × 9 SP). W backlogu jest 5 features requested przez klientów, ale możemy zrealizować maksymalnie 2-3. Customer feedback z Q4 wskazuje na biggest pain points: wolny export danych oraz brak collaboration features.

**Kluczowe ograniczenia:**
- **Capacity:** 45 story points (nie więcej)
- **Deadline:** Sprint trwa 2 tygodnie (6-17 stycznia 2026)
- **Team composition:** 3 senior devs, 2 mid-level devs
- **Tech debt:** Musimy zarezerwować 10 SP na performance improvements (commitment ze Sprint 22 retro)

---

## SEC-DL-OPTIONS: Opcje rozważane

### Opcja 1: Feature A (Real-time Collaboration) + Feature B (Advanced Filtering)
**Opis:** Zbudowanie real-time collaboration (25 SP) + advanced filtering (15 SP)
**Kluczowe właściwości:**
- Total: 40 SP (fits capacity z 5 SP buforem)
- Collaboration ma 18 customer requests (highest demand)
- Filtering ma 12 customer requests (medium-high demand)
- Obie features mają high customer impact

### Opcja 2: Feature C (Data Export Optimization) + Feature D (Mobile Responsiveness)
**Opis:** Optymalizacja exportu (20 SP) + mobile responsiveness (20 SP)
**Kluczowe właściwości:**
- Total: 40 SP (fits capacity)
- Export optimization ma 15 customer requests + 8 support tickets (pain point!)
- Mobile responsiveness ma 10 requests
- Export ma proven ROI (zmniejszy support load)

### Opcja 3: Feature A (Real-time Collaboration) ONLY - full scope
**Opis:** Zbudowanie tylko Collaboration w pełnym scope (35 SP zamiast 25 SP MVP)
**Kluczowe właściwości:**
- Single feature (35 SP + 10 SP tech debt = 45 SP total)
- Najwyższy customer demand (18 requests)
- Full scope includes: live cursors, conflict resolution, presence indicators
- Risk: Żadne inne features w tym sprincie

### Opcja 4: Feature C (Data Export) + Feature E (Notification System)
**Opis:** Export optimization (20 SP) + notification system (18 SP)
**Kluczowe właściwości:**
- Total: 38 SP (safe margin)
- Export addresses biggest support pain point
- Notifications mają 9 requests (lower demand)
- Notifications są nice-to-have, nie must-have

### Opcja 5: Tech Debt Sprint (Performance + Refactoring ONLY)
**Opis:** Dedykowany sprint na performance improvements i refactoring (45 SP)
**Kluczowe właściwości:**
- Zero new features
- 100% focus na quality i performance
- Team velocity może wzrosnąć w przyszłych sprintach
- Risk: Stakeholders mogą być niezadowoleni (zero visible progress)

---

## SEC-DL-DECISION: Decyzja

**Wybrana opcja:** Opcja 2 - Feature C (Data Export Optimization) + Feature D (Mobile Responsiveness)

**Scope:**
- **Feature C - Data Export Optimization** (20 SP)
  - Optymalizacja exportu CSV/Excel (current: 2-3 min dla 10K rows → target: <30 sec)
  - Background processing z progress indicator
  - Email notification po zakończeniu exportu

- **Feature D - Mobile Responsiveness** (20 SP)
  - Responsive layout dla tablets (iPad, Android)
  - Touch-friendly controls dla kluczowych funkcji
  - Mobile navigation menu

**Pozostałe 5 SP:** Buffer dla unforeseen issues + Code review time

---

## SEC-DL-RATIONALE: Uzasadnienie (1-3 zdania)

Export optimization ma najwyższy impact na customer satisfaction (15 requests + 8 support tickets = biggest pain point). Mobile responsiveness ma rosnący demand (10 requests, +40% mobile traffic w Q4). Razem te 2 features addressują both performance complaints i accessibility needs, przy zachowaniu safe capacity margin.

**Kluczowe czynniki:**
- **Support load reduction:** Export optimization zmniejszy support tickets o ~30% (based on current ticket analysis)
- **Market demand:** 35% użytkowników korzysta z mobile devices (iPad w terenie)
- **Technical feasibility:** Obie features mają clear technical approach (no unknowns)
- **Team expertise:** Team ma experience z background processing i responsive design

**Opcje odrzucone i dlaczego:**

- **Opcja 1 (Collaboration + Filtering):**
  Collaboration ma highest demand (18 requests), ale jest complex i risky (real-time sync). Lepiej to zaplanować jako dedicated sprint z większym czasem na testing.

- **Opcja 3 (Collaboration ONLY - full scope):**
  Za ryzykowne - jeśli się opóźnimy, cały sprint będzie failure. Wolę 2 medium features niż 1 large high-risk feature.

- **Opcja 4 (Export + Notifications):**
  Notifications są nice-to-have, ale Mobile responsiveness ma wyższy business impact (35% mobile traffic vs 9 notification requests).

- **Opcja 5 (Tech Debt ONLY):**
  Odrzucone - stakeholders expectations wymagają visible progress. Tech debt addressujemy jako część każdego sprintu (10 SP reserved), ale nie cały sprint.

---

## SEC-DL-OWNER: Decision owner

**Decision owner:** Anna Kowalska (Product Manager)

**Współdecydenci/Konsultanci:**
- Piotr Nowak (Tech Lead) - consulted - ✅ approved technical feasibility
- Katarzyna Wiśniewska (Customer Success Manager) - consulted - ✅ confirmed customer priorities
- Michał Zieliński (Engineering Manager) - informed - ✅ acknowledged capacity planning

**Data zatwierdzenia:** 2025-12-29

**Approval notes:**
- Tech Lead confirmed: Export optimization can reuse existing background job infrastructure (zmniejsza risk)
- Customer Success potwierdziła: Export complaints są #1 issue w support tickets
- Eng Manager zasugerował:留 5 SP buffer (agreed)

---

## Notatki dodatkowe (opcjonalne)

### Następne kroki
- [x] Dodać Feature C i D do Sprint 23 backlog - **Done** (2025-12-29)
- [x] Poinformować stakeholders o decyzji - **Done** (2025-12-29, email sent)
- [ ] Przygotować detailed user stories dla Feature C - **Due:** 2026-01-02
- [ ] Przygotować detailed user stories dla Feature D - **Due:** 2026-01-02
- [ ] Design review dla Mobile Responsiveness - **Due:** 2026-01-03
- [ ] Setup performance monitoring dla Export optimization - **Due:** 2026-01-05

### Terminy review
- **Pierwszy review:** 2026-01-17 (Sprint 23 retrospective)
- **Kryteria sukcesu:**
  - Export time <30 sec dla 10K rows (current: 2-3 min)
  - Mobile responsiveness works na iPad i Android tablets (tested z 5 users)
  - Zero P0/P1 bugs w production
  - Customer feedback score >4.0/5 dla obu features

### Features przesunięte na przyszłe sprinty
- **Feature A (Real-time Collaboration):** Przesunięte na Sprint 24 lub 25 (wymaga dedicated sprint + design time)
- **Feature B (Advanced Filtering):** Przesunięte na Sprint 24 (medium priority)
- **Feature E (Notification System):** Przesunięte na Q1 2026 backlog (lower priority)

### Powiązane decyzje
- Sprint 22 Retrospective: Commitment do 10 SP tech debt każdy sprint
- Q4 2025 Roadmap Review: Prioritization of performance improvements
- Customer Feedback Analysis Q4 2025: Export i Mobile jako top requests

### Assumptions and risks
**Assumptions:**
- Team velocity pozostanie stabilna (45 SP)
- Żadne unforeseen absences (vacation plan checked)
- Background job infrastructure jest ready (Tech Lead confirmed)

**Risks:**
- **Medium risk:** Mobile testing może odkryć edge cases (mitigation: early design review)
- **Low risk:** Export optimization może wymagać database indexing (mitigation: 5 SP buffer)

### Stakeholder communication
**Communicated to:**
- ✅ Engineering team - Sprint Planning meeting (2025-12-29)
- ✅ Customer Success - Email (2025-12-29)
- ✅ Sales team - Slack announcement (2025-12-29)
- ✅ Executive team - Weekly status update (2025-12-29)

**Key message:**
"Sprint 23 fokus: Export optimization (biggest pain point) + Mobile responsiveness (growing demand). Collaboration feature postponed to Sprint 24/25 dla proper design time."

---

**Decision Log utworzony przez:** Anna Kowalska (PM)
**Czas wypełnienia:** 8 minut
**Template version:** DECISION-LOG v1.0
