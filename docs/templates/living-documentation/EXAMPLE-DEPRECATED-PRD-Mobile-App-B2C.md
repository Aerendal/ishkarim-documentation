---
# === Standardowe pola (istniejące) ===
id: DOC-PRD-008-B2C-DEPRECATED
doctype: PRD
status: deprecated
version: "2.5.3"
owner: "Jan Kowalski"
project: "Ishkarim Mobile (B2C) - DEPRECATED"
created: "2025-01-15"

# === NOWE: Status Metadata (Living Documentation) ===
status_metadata:
  previous_status: approved
  status_changed_date: "2025-12-15"
  status_reason: "Firma wykonała pivot z modelu B2C na B2B - wymagania dla konsumentów indywidualnych nie są już aktualne"
  next_review_date: null  # No further reviews - deprecated

# === NOWE: Lifecycle Tracking ===
lifecycle:
  created: "2025-01-15"
  first_approved: "2025-02-01"
  last_modified: "2025-11-20"
  last_reviewed: "2025-11-20"
  sunset_date: "2026-03-15"  # 90 days from deprecation
  migration_target: "DOC-PRD-012-B2B"

# === NOWE: Version Metadata (Semantic Versioning) ===
version_metadata:
  major: 2       # Last major version (B2C model)
  minor: 5       # Last minor version
  patch: 3       # Last patch (final update before deprecation)
  breaking_changes: false
  backward_compatible_with: ["2.4.x", "2.3.x", "2.2.x"]
  forward_compatible_with: []

version_history:
  - version: "2.5.3"
    date: "2025-11-20"
    author: "Jan Kowalski"
    type: "patch"
    summary: "Ostatnia aktualizacja przed deprecation - doprecyzowanie acceptance criteria"
    breaking: false
    impacts: []

  - version: "2.5.0"
    date: "2025-10-15"
    author: "Jan Kowalski"
    type: "minor"
    summary: "Dodano wymagania dla systemu referral program (viralność)"
    breaking: false
    impacts:
      - id: DOC-TDD-008
        action: "Dodano architekturę referral tracking"

  - version: "2.0.0"
    date: "2025-05-10"
    author: "Jan Kowalski"
    type: "major"
    summary: "Przeprojektowanie na freemium model (wcześniej: płatna subskrypcja)"
    breaking: true
    impacts:
      - id: DOC-BUSINESS-CASE-003
        action: "Wymaga przeliczenia ROI dla freemium"
      - id: DOC-TDD-008
        action: "Dodano tier management (free vs premium)"

  - version: "1.0.0"
    date: "2025-02-01"
    author: "Jan Kowalski"
    type: "major"
    summary: "Pierwsza zatwierdzona wersja - mobilna aplikacja B2C dla Ishkarim"
    breaking: false
    impacts:
      - id: DOC-TDD-008
        action: "Rozpoczęcie detailed design"

# === NOWE: Cross-Reference Status (Impact Propagation) ===
cross_reference_status:
  upstream_changes_pending: []  # No pending changes (deprecated)

  downstream_impacts_pending:
    - id: DOC-TDD-008-B2C
      notified_date: "2025-12-15"
      acknowledged: true
      acknowledged_by: "Piotr Wiśniewski (Tech Lead)"
      acknowledged_date: "2025-12-16"
      action: "TDD-008 także deprecated, migracja do TDD-012-B2B"
    - id: DOC-TEST-PLAN-008-B2C
      notified_date: "2025-12-15"
      acknowledged: true
      acknowledged_by: "Maria Nowak (QA Lead)"
      acknowledged_date: "2025-12-16"
      action: "Test plan deprecated, test cases migrują do TEST-PLAN-012-B2B"
    - id: DOC-USER-GUIDE-008-B2C
      notified_date: "2025-12-15"
      acknowledged: true
      acknowledged_by: "Anna Kowalska (Tech Writer)"
      acknowledged_date: "2025-12-17"
      action: "User guide deprecated, nowa wersja dla B2B w trakcie tworzenia"

# === NOWE: Document Health ===
document_health:
  status: "warning"
  last_health_check: "2025-12-29T08:30:00Z"
  checks:
    - name: "Deprecation Status"
      status: "warning"
      message: "Dokument deprecated - 86 dni do sunset (2026-03-15)"
      days_until_sunset: 86

    - name: "Freshness Check"
      status: "warning"
      last_modified_days_ago: 39
      threshold_days: 90
      message: "Dokument nie będzie dalej aktualizowany (deprecated)"

    - name: "Dependency Validity"
      status: "warning"
      all_dependencies_valid: false
      deprecated_dependencies:
        - id: DOC-BUSINESS-CASE-003-B2C
          status: "deprecated"
          message: "Business Case dla B2C także deprecated"
      message: "1 deprecated dependency (BUSINESS_CASE-003-B2C)"

    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true
      message: "Cross-references spójne (wszystkie downstream docs notified)"

    - name: "Owner Assignment"
      status: "healthy"
      owner_active: true
      message: "Owner aktywny (Jan Kowalski) - monitoruje migration process"

    - name: "Migration Status"
      status: "warning"
      migration_target_exists: true
      migration_guide_exists: true
      downstream_migrated_count: 2
      downstream_total_count: 3
      message: "2/3 downstream documents zmigrowanych (USER-GUIDE pending)"

    - name: "References to Deprecated Doc"
      status: "warning"
      new_references_blocked: true
      existing_references_count: 5
      message: "5 istniejących referencji - wszystkie notified o deprecation"

  overall_score: 45
  risk_level: "medium"

# === NOWE: Deprecation ===
deprecation:
  status: deprecated
  deprecated_date: "2025-12-15"
  deprecation_reason: "Pivot firmy z modelu B2C (konsumenci indywidualni) na model B2B (przedsiębiorstwa). Wymagania dla aplikacji mobilnej B2C nie są już aktualne - nowy PRD dla B2B został utworzony."
  sunset_date: "2026-03-15"  # 90 days from deprecation
  migration_target: "DOC-PRD-012-B2B"
  migration_guide: "templates/living-documentation/EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md"

  impact_on_references:
    - id: DOC-TDD-008-B2C
      action: "Deprecated - zastąpiony przez TDD-012-B2B"
      status: "migrated"
      migrated_date: "2025-12-20"
    - id: DOC-TEST-PLAN-008-B2C
      action: "Deprecated - test cases migrują do TEST-PLAN-012-B2B"
      status: "migrated"
      migrated_date: "2025-12-22"
    - id: DOC-USER-GUIDE-008-B2C
      action: "Deprecated - nowa user guide dla B2B w trakcie tworzenia"
      status: "in_progress"
      target_completion: "2026-01-15"
    - id: DOC-MARKET-ANALYSIS-002-B2C
      action: "Archived - B2C market analysis nie jest już relevant"
      status: "archived"
      archived_date: "2025-12-18"
    - id: DOC-ROADMAP-001
      action: "Update referencji - usunięto B2C milestones, dodano B2B"
      status: "completed"
      updated_date: "2025-12-16"

  retirement_notice: "templates/living-documentation/EXAMPLE-RETIREMENT-NOTICE-PRD-008-B2C.md"

  communication_log:
    - date: "2025-12-15"
      action: "Deprecation announcement email sent to all stakeholders"
      recipients: ["Product Team", "Engineering Team", "QA Team", "Tech Writers"]
      channel: "email"
    - date: "2025-12-16"
      action: "Deprecation discussed in All-Hands meeting"
      channel: "meeting"
    - date: "2025-12-20"
      action: "Migration progress update #1 (TDD migrated)"
      channel: "slack"
    - date: "2025-12-22"
      action: "Migration progress update #2 (TEST-PLAN migrated)"
      channel: "slack"
    - date: "2026-01-15"
      action: "30-day sunset warning (planned)"
      channel: "email + slack"
    - date: "2026-03-01"
      action: "14-day final warning (planned)"
      channel: "email + slack + calendar invite"

---

# ⚠️ DEPRECATION NOTICE

> **🚨 UWAGA: TEN DOKUMENT JEST WYCOFYWANY (DEPRECATED)**
>
> **Data deprecation:** 2025-12-15
>
> **Powód:** Firma wykonała pivot z modelu B2C (konsumenci indywidualni) na model B2B (przedsiębiorstwa). Wymagania dla mobilnej aplikacji B2C nie są już aktualne.
>
> **Data sunset:** 2026-03-15 (⏰ **86 dni pozostało**)
>
> **Dokument zastępujący:** [DOC-PRD-012-B2B: Ishkarim Enterprise Mobile App](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md)
>
> **Migration Guide:** [B2C → B2B Migration Guide](EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md)
>
> **Status migracji:** 🟡 **W TRAKCIE** (2/3 downstream documents migrated)
>
> ---
>
> ### ⚡ Akcje wymagane przed sunset (2026-03-15):
>
> - [x] ~~TDD-008-B2C → TDD-012-B2B~~ (✅ Completed 2025-12-20)
> - [x] ~~TEST-PLAN-008-B2C → TEST-PLAN-012-B2B~~ (✅ Completed 2025-12-22)
> - [ ] USER-GUIDE-008-B2C → USER-GUIDE-012-B2B (⏳ In Progress, target: 2026-01-15)
> - [x] ~~ROADMAP-001: Remove B2C references~~ (✅ Completed 2025-12-16)
> - [x] ~~MARKET-ANALYSIS-002-B2C: Archive~~ (✅ Archived 2025-12-18)
>
> ### 📞 Kontakt:
>
> - **Migration Owner:** Jan Kowalski (jan.kowalski@example.com)
> - **Questions/Issues:** Slack #ishkarim-b2b-migration
> - **Office Hours:** Środy 14:00-15:00 (Zoom link w Slack)
>
> ---
>
> **⚠️ DO NOT USE FOR NEW WORK** — Ten dokument jest zachowany tylko dla referencji historycznej. Dla nowych projektów używaj [DOC-PRD-012-B2B](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md).

---

# PRD: Ishkarim Mobile App (B2C Model) - DEPRECATED

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: DOC-BUSINESS-CASE-003-B2C
    type: requires
    reason: "PRD bazuje na business case dla modelu B2C (freemium)"
    min_status: approved
    current_version: "1.8.0"
    current_status: "deprecated"  # ⚠️ Also deprecated
    note: "BUSINESS_CASE dla B2C także deprecated - zobacz BC-005-B2B"

  - id: DOC-ROADMAP-001
    type: requires
    reason: "Mobile app był częścią roadmap Q2 2025"
    min_status: approved
    current_version: "2.1.0"
    current_status: "approved"
    note: "ROADMAP updated - B2C milestones usunięte, dodano B2B (v2.1.0, 2025-12-16)"

  - id: DOC-MARKET-ANALYSIS-002-B2C
    type: informs
    reason: "Market analysis dla rynku B2C (konsumenci indywidualni)"
    current_version: "1.3.0"
    current_status: "archived"  # ⚠️ Archived
    note: "Market analysis dla B2C archived - nie jest już relevant"
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: DOC-TDD-008-B2C
    type: blocks
    reason: "TDD bazuje na tym PRD"
    current_status: "deprecated"
    migration_status: "migrated"
    migration_target: "DOC-TDD-012-B2B"
    migrated_date: "2025-12-20"

  - id: DOC-TEST-PLAN-008-B2C
    type: blocks
    reason: "Test plan bazuje na acceptance criteria z PRD"
    current_status: "deprecated"
    migration_status: "migrated"
    migration_target: "DOC-TEST-PLAN-012-B2B"
    migrated_date: "2025-12-22"

  - id: DOC-USER-GUIDE-008-B2C
    type: influences
    reason: "User guide dokumentuje features z PRD"
    current_status: "deprecated"
    migration_status: "in_progress"
    migration_target: "DOC-USER-GUIDE-012-B2B"
    target_completion: "2026-01-15"
```

### Related Documents

```yaml
related:
  - id: DOC-PRD-012-B2B
    type: replaces
    reason: "Nowy PRD dla modelu B2B (przedsiębiorstwa) - zastępuje ten dokument"
    relationship: "successor"

  - id: DOC-ADR-050
    type: informs
    reason: "ADR-050: Decision to pivot from B2C to B2B"
    note: "Pivot decision triggering this deprecation"

  - id: EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B
    type: informs
    reason: "Migration guide explaining how to migrate from B2C to B2B"

  - id: EXAMPLE-RETIREMENT-NOTICE-PRD-008-B2C
    type: informs
    reason: "Retirement notice documenting this deprecation"
```

---

# 1. Cel Produktu (DEPRECATED)

> **⚠️ DEPRECATED CONTENT BELOW**
>
> Poniższa treść opisuje wymagania dla modelu B2C, który nie jest już aktualny.
>
> **Dla aktualnych wymagań (model B2B):** Zobacz [DOC-PRD-012-B2B](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md)

---

## 1.1. Problem / Opportunity (B2C Model)

**Problem:**

Indywidualni użytkownicy (tech writers, freelancers, studenci) potrzebują **mobilnej wersji Ishkarim** aby zarządzać dokumentacją w podróży:

- **Pain Point 1:** Brak dostępu do dokumentacji poza biurem
  - Przykład: Tech writer pracuje zdalnie, chce przeczytać PRD w pociągu
  - Efekt: Konieczność czekania do powrotu do biura → opóźnienia w pracy

- **Pain Point 2:** Brak możliwości szybkich aktualizacji
  - Przykład: PM chce dodać quick note do dokumentu podczas spotkania
  - Efekt: Musi pamiętać → często zapomina → lost insights

- **Pain Point 3:** Desktop-only experience = ograniczona mobilność
  - Efekt: Użytkownicy nie mogą wykorzystać "dead time" (commute, kolejki) na produktywną pracę

**Dane (z Evidence E-080: Market Research - B2C):**
- 65% użytkowników Ishkarim zgłosiło: "Chciałbym mobilną wersję"
- 42% użytkowników pracuje zdalnie min. 2 dni/tydzień
- Średni czas "dead time" (commute, travel): **45 minut/dzień** = potencjalny czas pracy z dokumentacją

> **🚨 DEPRECATED RATIONALE:**
>
> **Dlaczego to nie jest już aktualne:**
> - Pivot na B2B zmienił target users: z freelancers/individuals → enterprise teams
> - Enterprise users mają inne needs: nie commute (remote work standard), ale potrzebują collaboration tools, admin panels, SSO
> - Mobile app dla B2B ma inne wymagania: focus na approval workflows, mobile notifications, offline sync dla enterprise data (nie casual reading)
>
> **Zobacz B2B rationale:** [DOC-PRD-012-B2B §1](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md#1-cel-produktu)

---

## 1.2. Vision Statement (B2C Model)

**Dla:** Indywidualnych użytkowników Ishkarim (tech writers, freelancers, studenci)

**Którzy:** Potrzebują dostępu do dokumentacji w podróży i możliwości szybkich aktualizacji

**Ishkarim Mobile App jest:** Natywną aplikacją mobilną (iOS + Android) umożliwiającą czytanie, edycję i tworzenie dokumentów

**Która:** Oferuje 80% funkcjonalności desktop (fokus na core flows: read, quick edit, search)

**W przeciwieństwie do:** Desktop app (pełna funkcjonalność, ale wymaga laptopa)

**Nasz produkt:** Jest zoptymalizowany pod mobilność, offline-first, i freemium model (free tier + premium subscription)

> **🚨 DEPRECATED VISION:**
>
> **B2B Vision (aktualny):**
> "Dla enterprise teams które potrzebują mobilnego dostępu do dokumentacji korporacyjnej, Ishkarim Enterprise Mobile App oferuje secure, SSO-integrated, audit-ready mobile experience z focus na approval workflows i team collaboration."
>
> **Kluczowe różnice:**
> - B2C: Freemium, individual users, casual use
> - B2B: Enterprise SaaS, team collaboration, compliance-ready

---

## 1.3. Success Metrics (KPIs) - B2C Model

| Metryka | Baseline (Desktop) | Target (Mobile) | Measurement |
|---------|-------------------|-----------------|-------------|
| **Daily Active Users (DAU)** | 500 users (desktop) | +200 users (mobile) | Analytics |
| **Freemium Conversion Rate** | N/A | >5% (free → premium) | Subscription data |
| **Mobile Usage Time** | 0 min (no mobile) | 15 min/user/day | Time tracking |
| **NPS (Mobile App)** | N/A | >7.0 | Quarterly survey |
| **Churn Rate (Premium)** | N/A | <10% monthly | Subscription data |

> **🚨 DEPRECATED METRICS:**
>
> **B2B Metrics (aktualny):**
> - Enterprise Adoption Rate (% of pilot companies adopting mobile)
> - Mobile Approval Completion Rate (% of approvals done via mobile)
> - SSO Login Success Rate (>99%)
> - Audit Log Completeness (100% actions logged)
>
> **Rationale:** B2B fokusuje się na enterprise adoption, nie consumer acquisition

---

# 2. Zakres (In/Out of Scope) - B2C Model

## 2.1. In Scope (MVP - B2C)

**Must Have (P0):**

✅ **Core Reading:**
- Przeglądanie dokumentów (list view, detail view)
- Search (keyword search w dokumentach)
- Offline access (cache ostatnio otwartych dokumentów)

✅ **Quick Edit:**
- Edycja prostego tekstu (markdown)
- Dodawanie komentarzy (inline comments)
- Tworzenie nowych dokumentów (templates)

✅ **Freemium Model:**
- Free tier: 10 dokumentów, basic features
- Premium tier: unlimited docs, advanced features (offline, collaboration)

**Should Have (P1):**

✅ **Social Login:**
- Login via Facebook, Google (easy onboarding dla consumers)

✅ **Sharing:**
- Share dokument via link (public/private)

---

## 2.2. Out of Scope (MVP - B2C)

**Defer to V2:**

❌ **Advanced Editing:**
- Rich text editor (WYSIWYG)
- **Rationale:** V1 = markdown only (simpler)

❌ **Real-time Collaboration:**
- Multi-user editing (jak Google Docs)
- **Rationale:** Nice-to-have, not critical for solo users

---

> **🚨 SCOPE CHANGE (B2C → B2B):**
>
> **B2B Scope (aktualny):**
>
> **In Scope:**
> - ✅ SSO/SAML authentication (not social login)
> - ✅ Approval workflows (mobile approval dla enterprise docs)
> - ✅ Audit logging (compliance requirement)
> - ✅ Team collaboration (comments, mentions, notifications)
> - ✅ Multi-tenant architecture (enterprise isolation)
>
> **Out of Scope:**
> - ❌ Freemium model (B2B = enterprise SaaS pricing)
> - ❌ Social login (enterprise wymaga SSO)
> - ❌ Public sharing (enterprise = private by default)
>
> **Rationale:** B2B wymaga enterprise-grade security, compliance, i team workflows (nie individual casual use)

---

# 3. Personas / Użytkownicy - B2C Model

## Persona 1: Freelance Tech Writer (Primary User - B2C)

**Imię:** Maria, 28 lat
**Rola:** Freelance Technical Writer
**Lokalizacja:** Warszawa, Polska
**Urządzenia:** iPhone 13, MacBook Air

**Goals:**
- Czytać dokumenty klientów w pociągu (daily commute: 40 min)
- Dodać quick notes podczas spotkań z klientami
- Zarządzać 5-10 projektami jednocześnie (różni klienci)

**Pain Points (Current - Desktop Only):**
- "Nie mogę pracować w pociągu (no laptop space)"
- "Zapominam insights ze spotkań (no quick note taking)"
- "Desktop app za heavy dla quick tasks"

**How they'll use Mobile App:**
- **Morning commute:** Czyta PRD dla projektu A (20 min)
- **Client meeting:** Dodaje notes do dokumentu (5 min)
- **Lunch break:** Review dokumentu od klienta, dodaje komentarze (15 min)

**Frequency:** Daily (3-5 sessions/day, avg 10 min/session)

**Willingness to Pay:** Medium (freelancer budget-conscious, ale może zapłacić $5/month za premium)

> **🚨 DEPRECATED PERSONA:**
>
> **B2B Persona (aktualny): Enterprise IT Manager**
>
> **Imię:** Piotr, 42 lata
> **Rola:** IT Manager w firmie 500+ employees
>
> **Goals:**
> - Approve technical specs via mobile (podczas podróży służbowych)
> - Monitor compliance status (audit readiness)
> - Zarządzać dostępami team members
>
> **Pain Points:**
> - "Nie mogę approve specs poza biurem → opóźnienia w projektach"
> - "Potrzebuję SSO (nie chcę dodatkowego hasła)"
> - "Mobile musi być compliant (audit log required)"
>
> **Willingness to Pay:** High (enterprise budget: $50/user/month OK jeśli ROI clear)

---

## Persona 2: Student (Secondary User - B2C)

**Imię:** Kasia, 21 lat
**Rola:** Student Computer Science (thesis project)
**Lokalizacja:** Kraków, Polska
**Urządzenia:** Android phone (Samsung), laptop

**Goals:**
- Zarządzać thesis documentation (PRD, TDD dla projektu dyplomowego)
- Collaborate z promotorem (share docs, comments)
- Free tier wystarczy (student budget = $0)

**Pain Points (Current):**
- "Desktop app za skomplikowana dla mojego prostego use case"
- "Chcę czytać docs w bibliotece (laptop = overkill)"

**How they'll use Mobile App:**
- **Library study:** Czyta TDD na telefonie, robi notatki (30 min)
- **Bus ride:** Quick review dokumentu przed meeting z promotorem (10 min)

**Frequency:** 3-4x per week (casual user)

**Willingness to Pay:** Low (student = free tier user, unlikely to upgrade)

> **🚨 DEPRECATED PERSONA:**
>
> **B2B nie targetuje studentów** — focus na enterprise users z budżetem korporacyjnym.

---

# 4. Wymagania Funkcjonalne - B2C Model (SKRÓCONE)

> **⚠️ CONTENT TRUNCATED**
>
> Pełna lista wymagań funkcjonalnych dla modelu B2C nie jest już aktualna.
>
> **Kluczowe wymagania (B2C):**
> - FR-01: Social Login (Facebook, Google)
> - FR-02: Freemium Tier Management (free 10 docs, premium unlimited)
> - FR-03: Offline Mode (cache ostatnich 20 dokumentów)
> - FR-04: Quick Edit (markdown editing w mobile)
> - FR-05: Share via Link (public/private sharing)
>
> **Dla aktualnych wymagań (B2B):** Zobacz [DOC-PRD-012-B2B §5](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md#5-wymagania-funkcjonalne)
>
> **Kluczowe różnice B2C → B2B:**
> - ❌ Social Login → ✅ SSO/SAML
> - ❌ Freemium → ✅ Enterprise SaaS pricing
> - ❌ Public sharing → ✅ Enterprise-only sharing (audit logged)
> - ❌ Casual offline mode → ✅ Secure offline sync (encrypted)

---

# 5. Wymagania Niefunkcjonalne (NFRs) - B2C Model (SKRÓCONE)

> **⚠️ CONTENT TRUNCATED**
>
> **Kluczowe NFR (B2C):**
> - NFR-01: Performance — App launch <2s
> - NFR-02: Offline-first — Works bez internetu (cached content)
> - NFR-03: Battery efficiency — <5% battery drain/hour
> - NFR-04: Freemium limits — Free tier: 10 docs max
>
> **B2B NFR (aktualny):**
> - NFR-01: Security — SOC2 Type II compliant
> - NFR-02: SSO — SAML 2.0 integration (<500ms login)
> - NFR-03: Audit logging — 100% actions logged (immutable)
> - NFR-04: Multi-tenancy — Complete data isolation
> - NFR-05: Uptime — 99.9% SLA

---

# 6. Migracja do B2B

## 6.1. Dlaczego Pivot z B2C na B2B?

**Business Rationale (z ADR-050):**

1. **Market Opportunity:**
   - B2C TAM: $5M (freelancers, individual users)
   - B2B TAM: $50M (enterprise documentation market)
   - **Decision:** B2B ma 10x większy potential

2. **Revenue Model:**
   - B2C freemium: 5% conversion rate × $5/month = $0.25 ARPU (low)
   - B2B enterprise: $50/user/month × 100 users/company = $5,000 MRR/company
   - **Decision:** B2B ma 20x wyższy ARPU

3. **Competitive Landscape:**
   - B2C: Fierce competition (Notion, Evernote, Bear)
   - B2B: Less competition dla niche (documentation management dla enterprise)
   - **Decision:** B2B ma clearer positioning

4. **Customer Acquisition:**
   - B2C: Kosztowny (social media ads, influencer marketing)
   - B2B: Enterprise sales (higher CAC, ale wyższy LTV)
   - **Decision:** B2B ma lepszy LTV:CAC ratio

**Timeline:**
- 2025-11-01: Pivot decision (ADR-050 approved)
- 2025-11-15: New PRD-012-B2B created
- 2025-12-01: PRD-012-B2B approved
- 2025-12-15: PRD-008-B2C deprecated
- 2026-03-15: PRD-008-B2C sunset (archived)

---

## 6.2. Co Się Zmienia?

**High-Level Comparison:**

| Aspekt | B2C (Ten dokument) | B2B (PRD-012) |
|--------|-------------------|---------------|
| **Target Users** | Freelancers, students, individuals | Enterprise teams (IT managers, compliance officers) |
| **Pricing** | Freemium ($0-5/month) | Enterprise SaaS ($50/user/month) |
| **Authentication** | Social login (FB, Google) | SSO/SAML (Okta, Azure AD) |
| **Key Features** | Offline reading, quick edit, sharing | Approval workflows, audit logging, team collaboration |
| **Compliance** | None | SOC2, GDPR, HIPAA |
| **Mobile Focus** | Casual reading, quick notes | Approval on-the-go, compliance mobile access |

---

## 6.3. Migration Guide

**Pełny migration guide:** [EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md](EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md)

**Quick Summary:**

### Dla Document Owners (TDD, TEST-PLAN, etc.):

1. **Read Migration Guide** (szczegółowe mapowanie requirements)
2. **Review PRD-012-B2B** (understand nowe wymagania)
3. **Update Dependencies:**
   - Replace `DOC-PRD-008-B2C` → `DOC-PRD-012-B2B` w front-matter
4. **Update Content:**
   - Zmień user flows (social login → SSO)
   - Dodaj enterprise requirements (audit logging, compliance)
5. **Update Tests:**
   - Zmień test scenarios (freemium → enterprise)

### Dla Stakeholders:

1. **Acknowledge Deprecation** (email/Slack notification)
2. **Plan Migration Work** (schedule w sprint planning)
3. **Attend Migration Q&A** (office hours: Środy 14:00-15:00)

---

# 7. Timeline i Next Steps

## 7.1. Deprecation Timeline

| Faza | Data | Status | Akcja |
|------|------|--------|-------|
| **Deprecation Announced** | 2025-12-15 | ✅ Complete | Email sent, banner added |
| **Migration Period Start** | 2025-12-15 | 🔄 In Progress | Teams migrating downstream docs |
| **30-Day Warning** | 2026-02-13 | ⏳ Planned | Email reminder + Slack |
| **14-Day Final Warning** | 2026-03-01 | ⏳ Planned | Email + Slack + calendar invite |
| **Sunset Date** | 2026-03-15 | ⏳ Planned | Archive document |
| **Archive Location** | 2026-03-15 | ⏳ Planned | `archive/2026-Q1-B2C-pivot/PRD-008-B2C/` |

---

## 7.2. Migration Checklist

**Overall Progress: 60% (3/5 tasks completed)**

- [x] ~~Create PRD-012-B2B (replacement document)~~ ✅ Done 2025-12-01
- [x] ~~Deprecate PRD-008-B2C~~ ✅ Done 2025-12-15
- [x] ~~Migrate TDD-008-B2C → TDD-012-B2B~~ ✅ Done 2025-12-20
- [x] ~~Migrate TEST-PLAN-008-B2C → TEST-PLAN-012-B2B~~ ✅ Done 2025-12-22
- [ ] Migrate USER-GUIDE-008-B2C → USER-GUIDE-012-B2B ⏳ In Progress (target: 2026-01-15)

---

## 7.3. Historical Value

**Why Keep This Document Archived?**

Mimo że deprecated, ten dokument ma wartość historyczną:

1. **B2C Learnings:**
   - User research dla freelancers/students (może być valuable dla future B2C pivot)
   - Freemium pricing experiments (conversion rates, churn data)

2. **Audit Trail:**
   - Pokazuje evolution firmy (B2C → B2B pivot decision)
   - Dokumentuje rationale za pivot (ADR-050)

3. **Comparison Baseline:**
   - B2B metrics można porównać z B2C (np. NPS: B2C 6.5 vs B2B 8.2)

4. **Onboarding Context:**
   - Nowi team members rozumieją historię produktu
   - "Dlaczego nie B2C?" → ten dokument wyjaśnia

**Archive Location (Post-Sunset):**
```
archive/2026-Q1-B2C-pivot/PRD-008-B2C/
├── PRD-008-B2C-v2.5.3.md (final version)
├── RETIREMENT-NOTICE-PRD-008-B2C.md
├── MIGRATION-GUIDE-B2C-to-B2B.md
├── CHANGELOG-PRD-008-B2C.md (full history)
└── evidence/
    ├── E-080-market-research-B2C.md
    └── E-081-user-interviews-freelancers.md
```

**Archive Metadata:**
```yaml
archived_date: "2026-03-15"
archived_by: "Jan Kowalski"
archive_reason: "Deprecated after B2C → B2B pivot (ADR-050)"
historical_tag: "pivot-2025-Q4-B2C-to-B2B"
access: "read-only"
```

---

# 8. Kontakt i Support

## 8.1. Migration Owner

**Jan Kowalski**
- Email: jan.kowalski@example.com
- Slack: @jan.kowalski
- Office Hours: **Środy 14:00-15:00** (Zoom link w Slack channel)

## 8.2. Migration Support Channels

- **Slack:** #ishkarim-b2b-migration (primary channel)
- **Email:** migration-support@example.com
- **Documentation:** [Migration Wiki](https://wiki.example.com/b2b-migration)

## 8.3. Escalation

Jeśli masz problem z migracją:
1. Post in Slack #ishkarim-b2b-migration
2. If urgent → email Jan Kowalski
3. If blocked → escalate to Product Owner (Anna Kowalska)

---

# 9. FAQ

## Q: Czy mogę nadal używać tego PRD?

**A:** ❌ Nie dla nowych projektów. Ten PRD jest deprecated i nie będzie dalej aktualizowany. Używaj [DOC-PRD-012-B2B](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md) dla nowych projektów.

Jeśli masz istniejący projekt bazujący na PRD-008-B2C → zaplanuj migrację przed sunset date (2026-03-15).

---

## Q: Co się stanie w sunset date (2026-03-15)?

**A:** Dokument zostanie archived:
- Status zmieni się: `deprecated` → `archived`
- Przeniesiony do: `archive/2026-Q1-B2C-pivot/PRD-008-B2C/`
- Dostępny tylko read-only (dla referencji historycznej)
- Nowe referencje zablokowane (link checker wyrzuci warning)

---

## Q: Czy mój projekt zostanie cancelled jeśli bazuje na PRD-008-B2C?

**A:** ❌ Nie automatycznie, ale **musisz zmigrować do B2B model** przed sunset.

- If projekt ma sens w B2B model → migruj do PRD-012-B2B
- If projekt jest B2C-only (np. student thesis) → możesz kontynuować, ale bez official support po sunset

---

## Q: Gdzie mogę znaleźć archived version po sunset?

**A:** `archive/2026-Q1-B2C-pivot/PRD-008-B2C/PRD-008-B2C-v2.5.3.md`

---

## Q: Kto decyduje o deprecation timeline?

**A:** Product Owner (Anna Kowalska) w konsultacji z stakeholders.

Standard deprecation period: **90 days** (wystarczająco dużo czasu dla większości teams na migrację).

---

**Koniec Deprecated Document**

**Status:** 🟡 DEPRECATED (86 dni do sunset)
**Last Updated:** 2025-12-29 (deprecation status review)
**Version:** 2.5.3 (final version before deprecation)
**Migration Status:** 🟡 60% complete (3/5 downstream docs migrated)
**Document Health:** ⚠️ WARNING (score: 45/100, risk: medium)
