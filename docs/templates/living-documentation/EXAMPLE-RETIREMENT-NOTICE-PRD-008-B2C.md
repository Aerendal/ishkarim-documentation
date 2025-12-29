---
id: RETIREMENT-PRD-008-B2C
type: retirement_notice
retired_document: "DOC-PRD-008-B2C"
retired_version: "2.5.3"
retirement_date: "2026-03-15"
retirement_type: "superseded"
created: "2025-12-15"
author: "Jan Kowalski"
status: "active"
---

# Retirement Notice: PRD-008-B2C (Ishkarim Mobile App - B2C Model)

**Retired Document:** DOC-PRD-008-B2C - Ishkarim Mobile App (B2C Model)
**Final Version:** 2.5.3
**Retirement Date:** 2026-03-15
**Retirement Type:** Superseded (zastąpiony nowym dokumentem)

---

## Deprecation Banner

> **🚨 DOKUMENT WYCOFANY (RETIRED)**
>
> Ten dokument został oficjalnie wycofany w dniu 2026-03-15.
>
> **Powód:** Pivot firmy z modelu B2C na B2B
>
> **Zastąpiony przez:** [DOC-PRD-012-B2B: Ishkarim Enterprise Mobile App](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md)
>
> **Archive Location:** `archive/2026-Q1-B2C-pivot/PRD-008-B2C/`
>
> **Tylko dla referencji historycznej** — Nie używaj dla nowych projektów

---

## 1. Dlaczego ten dokument został wycofany?

### Kontekst Biznesowy

W listopadzie 2025 roku firma Ishkarim podjęła strategiczną decyzję o **pivocie z modelu B2C (konsumenci indywidualni) na model B2B (przedsiębiorstwa)**.

**Powody pivot:**

1. **Większy rynek:**
   - B2C TAM: $5M (freelancers, individual users)
   - B2B TAM: $50M (enterprise documentation market)
   - **Decyzja:** B2B ma 10x większy potential

2. **Wyższe przychody:**
   - B2C ARPU: $0.25/user/month (freemium, 5% conversion)
   - B2B ARPU: $50/user/month (enterprise SaaS)
   - **Decyzja:** B2B ma 200x wyższy ARPU

3. **Lepsza konkurencja:**
   - B2C: Zacięta konkurencja (Notion, Evernote, Bear)
   - B2B: Mniej konkurentów dla niche (enterprise documentation management)

4. **Efektywniejsza akwizycja:**
   - B2C: Kosztowne social media ads
   - B2B: Enterprise sales (wyższy LTV:CAC ratio)

**Dokumenty decyzyjne:**
- **ADR-050:** "Decision to Pivot from B2C to B2B Model" (2025-11-01)
- **BUSINESS-CASE-005-B2B:** Nowy business case dla modelu B2B (ROI analysis)

---

### Wydarzenie Wyzwalające

**ADR-050: Pivot Decision** (2025-11-01)

**Kluczowe ustalenia:**
- Wszystkie dokumenty B2C zostaną deprecated
- Nowe dokumenty B2B zostaną utworzone
- Migration period: 90 dni (2025-12-15 → 2026-03-15)

---

## 2. Co zastępuje ten dokument?

### Dokument Zastępujący

**Nowy Dokument:** [DOC-PRD-012-B2B: Ishkarim Enterprise Mobile App](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md)
**Wersja:** 1.0.0
**Status:** approved
**Owner:** Anna Kowalska

### Dlaczego nowy dokument jest lepszy?

**PRD-012-B2B (B2B) vs PRD-008-B2C (B2C):**

| Aspekt | PRD-008-B2C (Ten dokument) | PRD-012-B2B (Nowy) |
|--------|---------------------------|-------------------|
| **Target Users** | Freelancers, studenci | Enterprise teams (500+ employees) |
| **Revenue Model** | Freemium ($5/month) | Enterprise SaaS ($50/user/month) |
| **Key Features** | Social login, offline reading | SSO/SAML, approval workflows, audit logging |
| **Compliance** | None | SOC2, GDPR, HIPAA |
| **Mobile Focus** | Casual reading | Business-critical approvals on-the-go |

**Korzyści B2B:**
- ✅ 10x większy TAM ($50M vs $5M)
- ✅ 200x wyższy ARPU ($50 vs $0.25)
- ✅ Lepszy product-market fit (enterprise needs > consumer casual use)
- ✅ Clearer competitive positioning

---

## 3. Migration Guide

**Pełny Migration Guide:** [B2C → B2B Migration Guide](EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md)

### Podsumowanie Kluczowych Zmian

| Komponent | PRD-008-B2C | PRD-012-B2B | Akcja Wymagana |
|-----------|-------------|-------------|----------------|
| **§3: Target Users** | Freelancers, studenci | Enterprise IT managers, compliance officers | Przepisz user personas |
| **§4: FR-01 Authentication** | Social login (FB, Google) | SSO/SAML (Okta, Azure AD) | Zmień auth flow w TDD |
| **§4: FR-02 Pricing** | Freemium (10 docs free) | Enterprise SaaS ($50/user) | Usuń freemium tier logic |
| **§4: FR-05 Sharing** | Public sharing links | Enterprise-only (audit logged) | Dodaj audit logging |
| **§5: NFR-Security** | Basic (HTTPS) | SOC2 Type II, GDPR | Dodaj compliance requirements |

### Quick Migration Checklist

Dla każdego dokumentu zależnego od PRD-008-B2C:

- [ ] **Krok 1:** Przeczytaj [Migration Guide](EXAMPLE-MIGRATION-GUIDE-B2C-to-B2B.md)
- [ ] **Krok 2:** Przeczytaj [PRD-012-B2B](EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md)
- [ ] **Krok 3:** Zaktualizuj front-matter dependencies:
  ```yaml
  # Stare:
  dependencies:
    - id: DOC-PRD-008-B2C

  # Nowe:
  dependencies:
    - id: DOC-PRD-012-B2B
  ```
- [ ] **Krok 4:** Zaktualizuj treść (user flows, requirements, test cases)
- [ ] **Krok 5:** Bump version (MAJOR jeśli breaking changes)
- [ ] **Krok 6:** Notify stakeholders

---

## 4. Timeline

### Deprecation & Retirement Timeline

| Faza | Data | Status | Akcja |
|------|------|--------|-------|
| **Pivot Decision** | 2025-11-01 | ✅ Complete | ADR-050 approved |
| **PRD-012-B2B Created** | 2025-11-15 | ✅ Complete | New PRD dla B2B |
| **PRD-012-B2B Approved** | 2025-12-01 | ✅ Complete | Ready for implementation |
| **Deprecation Announced** | 2025-12-15 | ✅ Complete | PRD-008-B2C deprecated |
| **Migration Period** | 2025-12-15 → 2026-03-15 | ✅ Complete | 90 dni migration window |
| **30-Day Warning** | 2026-02-13 | ✅ Complete | Reminder email sent |
| **14-Day Final Warning** | 2026-03-01 | ✅ Complete | Final reminder + calendar |
| **Retirement Date** | 2026-03-15 | ✅ Complete | PRD-008-B2C archived |

### Kluczowe Daty

- **Utworzony:** 2025-01-15
- **Pierwszy raz zatwierdzony:** 2025-02-01 (v1.0.0)
- **Ostatnia modyfikacja:** 2025-11-20 (v2.5.3 - final update)
- **Deprecated:** 2025-12-15
- **Sunset:** 2026-03-15 (90 dni później)
- **Archived:** 2026-03-15

---

## 5. Wpływ na Downstream Documents

### Dokumenty Które Referencowały PRD-008-B2C

#### DOC-TDD-008-B2C: Technical Design Document
- **Impact:** High
- **Akcja:** Zastąpiony przez TDD-012-B2B
- **Status:** ✅ Migrated (2025-12-20)
- **Zmienione przez:** Piotr Wiśniewski (Tech Lead)
- **Kluczowe zmiany:**
  - Usunięto social login architecture → dodano SSO/SAML
  - Usunięto freemium tier management → dodano multi-tenant architecture
  - Dodano audit logging system

---

#### DOC-TEST-PLAN-008-B2C: Test Plan
- **Impact:** High
- **Akcja:** Test cases zmigrowane do TEST-PLAN-012-B2B
- **Status:** ✅ Migrated (2025-12-22)
- **Zmienione przez:** Maria Nowak (QA Lead)
- **Kluczowe zmiany:**
  - Usunięto test cases dla social login → dodano SSO tests
  - Usunięto freemium tier tests → dodano enterprise pricing tests
  - Dodano compliance tests (SOC2, audit logging)

---

#### DOC-USER-GUIDE-008-B2C: User Guide
- **Impact:** Medium
- **Akcja:** Przepisana jako USER-GUIDE-012-B2B
- **Status:** ✅ Migrated (2026-01-10)
- **Zmienione przez:** Anna Kowalska (Tech Writer)
- **Kluczowe zmiany:**
  - Target audience: consumers → enterprise admins
  - Features: casual reading → approval workflows, admin panel
  - Authentication: social login tutorial → SSO setup guide

---

#### DOC-BUSINESS-CASE-003-B2C: Business Case (B2C Model)
- **Impact:** Critical
- **Akcja:** Archived (nie migrowane - B2C business case obsolete)
- **Status:** ✅ Archived (2025-12-18)
- **Zastąpione przez:** BUSINESS-CASE-005-B2B (całkowicie nowy dokument)

---

#### DOC-ROADMAP-001: Product Roadmap
- **Impact:** Medium
- **Akcja:** Updated (usunięto B2C milestones, dodano B2B)
- **Status:** ✅ Updated (2025-12-16)
- **Zmienione przez:** Product Owner
- **Zmiany:**
  - Removed: Q1 2026 - "B2C Mobile App Launch"
  - Added: Q2 2026 - "B2B Enterprise Mobile App Beta"

---

## 6. Wartość Historyczna

### Dlaczego Zachowujemy Ten Dokument?

Mimo że wycofany, PRD-008-B2C ma wartość jako **referencja historyczna**:

#### 1. B2C Learnings (Insights Dla Przyszłości)

**Co zadziałało w B2C:**
- Freemium model osiągnął 5% conversion rate (benchmark dla przyszłych B2C eksperymentów)
- Social login miał 80% adoption rate (users preferują easy onboarding)
- Offline mode był #1 requested feature (45% user interviews)

**Co nie zadziałało:**
- ARPU zbyt niski ($0.25/user) dla sustainable business
- CAC zbyt wysoki dla freemium model (social ads $15 CAC, LTV $3)
- Churn rate wysoki (15% monthly) dla free tier users

**Value:** Te insights mogą być valuable jeśli firma rozważy B2C w przyszłości (np. "Ishkarim Personal Edition").

---

#### 2. Audit Trail (Compliance & Decision History)

**Dokumentuje:**
- Dlaczego firma wybrała B2C initially (market research, competitive analysis)
- Dlaczego pivot na B2B (business rationale w ADR-050)
- Jak decisions ewoluowały (version history pokazuje 2.5 years of iterations)

**Value:** Audytorzy i inwestorzy mogą zapytać "Why B2B not B2C?" → ten dokument wyjaśnia.

---

#### 3. Comparison Baseline (Metryki)

**B2C Metrics (z PRD-008-B2C):**
- NPS: 6.5
- DAU: 500 users
- Conversion: 5% (free → premium)
- Churn: 15% monthly

**B2B Metrics (z PRD-012-B2B, po 6 miesiącach):**
- NPS: 8.2 (+26% vs B2C)
- Enterprise adoption: 15 companies (avg 100 users each = 1500 total users)
- Conversion: N/A (B2B = enterprise sales, nie freemium)
- Churn: 3% monthly (-80% vs B2C)

**Value:** Pokazuje że pivot był successful (lepsze metryki w B2B).

---

#### 4. Onboarding Context (Dla Nowych Team Members)

**Nowi team members pytają:**
- "Dlaczego nie mamy B2C versji?"
- "Czy rozważaliśmy freemium model?"
- "Jakie było initial vision dla produktu?"

**Odpowiedź:** Przeczytaj PRD-008-B2C (archived) + ADR-050 (pivot decision) → pełny kontekst.

---

### Archive Location

**Path:** `archive/2026-Q1-B2C-pivot/PRD-008-B2C/`

**Zawartość Archiwum:**
```
archive/2026-Q1-B2C-pivot/PRD-008-B2C/
├── PRD-008-B2C-v2.5.3.md              # Final version dokumentu
├── RETIREMENT-NOTICE-PRD-008-B2C.md   # Ten dokument
├── MIGRATION-GUIDE-B2C-to-B2B.md      # Migration guide
├── CHANGELOG-PRD-008-B2C.md           # Pełna version history (1.0.0 → 2.5.3)
├── ADR-050-Pivot-B2C-to-B2B.md        # Decision record (pivot rationale)
└── evidence/
    ├── E-080-market-research-B2C.md   # B2C market analysis
    ├── E-081-user-interviews-freelancers.md  # User interviews
    └── E-090-freemium-conversion-data.md     # Conversion metrics
```

**Archive Metadata:**
```yaml
archived_date: "2026-03-15"
archived_by: "Jan Kowalski"
archive_reason: "Deprecated after B2C → B2B pivot (ADR-050)"
archive_location: "archive/2026-Q1-B2C-pivot/PRD-008-B2C/"
historical_tag: "pivot-2025-Q4-B2C-to-B2B"
access_level: "read-only"
retention_period: "indefinite"  # Keep for historical reference
```

---

## 7. Lessons Learned

### Co Nauczyliśmy Się z PRD-008-B2C?

#### Positive Outcomes (Co Zadziałało)

1. **User Research:**
   - Freelancer personas były well-researched (5 user interviews, detailed profiles)
   - Pain points correctly identified (lack of mobile access, offline mode needs)
   - **Lesson:** Strong user research transferable do B2B (enterprise users mają podobne mobile needs)

2. **Feature Prioritization:**
   - MVP scope był realistic (core reading + quick edit)
   - Freemium tier limits były clear (10 docs free tier)
   - **Lesson:** Clear scope boundaries = easier implementation

3. **Documentation Quality:**
   - PRD miał 43 acceptance criteria (bardzo detailed)
   - Evidence-based requirements (E-080, E-081)
   - **Lesson:** High documentation quality standard established (carry do B2B docs)

---

#### Areas for Improvement (Co Moglibyśmy Zrobić Lepiej)

1. **Market Validation:**
   - **Problem:** B2C TAM był overestimated ($5M → actual market smaller)
   - **Lesson:** Validate market size early (before full PRD)
   - **Action for B2B:** B2B TAM validated with 10 enterprise customer interviews

2. **Business Model Validation:**
   - **Problem:** Freemium conversion rate (5%) był insufficient dla sustainable business
   - **Lesson:** Test pricing model early (MVP pricing experiments)
   - **Action for B2B:** B2B pricing validated with pilot customers (3 companies tested $50/user)

3. **Competitive Analysis:**
   - **Problem:** Underestimated Notion/Evernote competition (fierce B2C market)
   - **Lesson:** Deep competitive analysis required (not just feature comparison)
   - **Action for B2B:** B2B competitive landscape thoroughly analyzed (less competition in niche)

---

### Recommendations for Future

**Jeśli firma rozważa pivot w przyszłości:**

1. **Early Market Validation:**
   - Validate TAM/SAM with actual customer interviews (not just desk research)
   - Test pricing models early (landing page experiments, pilot programs)

2. **Clear Pivot Criteria:**
   - Define success metrics upfront (e.g., "If B2C ARPU <$1 after 6 months → consider B2B")
   - Regular reviews (quarterly "continue/pivot/kill" decisions)

3. **Smooth Deprecation Process:**
   - 90-day migration period worked well (enough time dla teams)
   - Clear communication (email + Slack + meetings = wszystkie stakeholders informed)
   - Migration guide essential (teams appreciated detailed mapping)

4. **Preserve Historical Context:**
   - Archive deprecated docs (valuable dla audit trail, lessons learned)
   - Document rationale (ADR-050 critical dla understanding pivot decision)

---

## 8. Stakeholder Communication

### Communication Log

| Data | Akcja | Recipients | Kanał | Status |
|------|-------|-----------|-------|--------|
| 2025-11-01 | ADR-050 (Pivot decision) approved | Executive team | Meeting | ✅ Complete |
| 2025-12-15 | Deprecation announcement email | All teams (30 people) | Email | ✅ Complete |
| 2025-12-16 | All-Hands meeting (pivot discussion) | Company-wide (50 people) | Meeting | ✅ Complete |
| 2025-12-20 | Migration progress update #1 | Engineering, QA | Slack | ✅ Complete |
| 2025-12-22 | Migration progress update #2 | Engineering, QA | Slack | ✅ Complete |
| 2026-01-10 | Migration completed announcement | All teams | Email + Slack | ✅ Complete |
| 2026-02-13 | 30-day sunset warning | Document owners | Email | ✅ Complete |
| 2026-03-01 | 14-day final warning | All teams | Email + Slack + Calendar | ✅ Complete |
| 2026-03-15 | Retirement completed | All teams | Email | ✅ Complete |

### Final Notification (Sent 2026-03-15)

```
Subject: [RETIRED] PRD-008-B2C Archived - B2C → B2B Migration Complete

Team,

PRD-008-B2C (Ishkarim Mobile App - B2C Model) został oficjalnie wycofany (retired) w dniu 2026-03-15.

Status: deprecated → archived

Archive Location: archive/2026-Q1-B2C-pivot/PRD-008-B2C/

Replacement: DOC-PRD-012-B2B (Ishkarim Enterprise Mobile App)

Migration Status: ✅ COMPLETE
- TDD-008-B2C → TDD-012-B2B ✅
- TEST-PLAN-008-B2C → TEST-PLAN-012-B2B ✅
- USER-GUIDE-008-B2C → USER-GUIDE-012-B2B ✅

Historical Value: Dokument zachowany dla referencji (B2C learnings, pivot context)

Dziękujemy za smooth migration! 🎉

Questions? Contact: Jan Kowalski (jan.kowalski@example.com)

---
Ishkarim Product Team
```

---

## 9. Approval & Sign-Off

### Retirement Approval

- **Proposed By:** Jan Kowalski (Document Owner) on 2025-12-15
- **Reviewed By:** Anna Kowalska (Product Owner), Piotr Wiśniewski (Tech Lead), Maria Nowak (QA Lead)
- **Approved By:** Anna Kowalska (Product Owner)
- **Approval Date:** 2025-12-15

### Stakeholder Acknowledgment

- [x] Product Team - Acknowledged by Anna Kowalska on 2025-12-15
- [x] Engineering Team - Acknowledged by Piotr Wiśniewski on 2025-12-16
- [x] QA Team - Acknowledged by Maria Nowak on 2025-12-16
- [x] Tech Writing Team - Acknowledged by Anna Kowalska on 2025-12-17
- [x] Executive Team - Acknowledged by CTO on 2025-12-16 (ADR-050 approval)

---

## 10. FAQ

### Q: Czy mogę nadal czytać PRD-008-B2C?

**A:** ✅ Tak, jako referencję historyczną. Dokument archived w `archive/2026-Q1-B2C-pivot/PRD-008-B2C/` (read-only access).

---

### Q: Gdzie mogę znaleźć archived version?

**A:** `archive/2026-Q1-B2C-pivot/PRD-008-B2C/PRD-008-B2C-v2.5.3.md`

---

### Q: Czy B2C może wrócić w przyszłości?

**A:** 💡 Może. Jeśli firma rozważy B2C w przyszłości, ten dokument będzie valuable reference (B2C learnings, freemium experiments, user research).

Decision criteria dla B2C comeback:
- B2B market saturated
- B2C TAM growth (np. wzrost freelancer economy)
- New technology enabling lower CAC (np. viral growth, community-led growth)

---

### Q: Kto decyduje o retirement dates?

**A:** Product Owner (Anna Kowalska) w konsultacji z stakeholders i document owner (Jan Kowalski).

Standard retirement timeline: **90 dni od deprecation** (wystarczająco dla migration).

---

## Metadata

**Retirement Notice Created:** 2025-12-15
**Created By:** Jan Kowalski
**Last Updated:** 2026-03-15
**Status:** Completed (dokument oficjalnie retired)

**Tags:** `retirement`, `deprecated`, `B2C-pivot`, `B2B-migration`, `ishkarim-mobile`

---

**Koniec Retirement Notice**
