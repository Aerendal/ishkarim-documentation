---
id: MIGRATION-PRD-008-B2C-to-PRD-012-B2B
type: migration_guide
from_document: "DOC-PRD-008-B2C"
from_version: "2.5.3"
to_document: "DOC-PRD-012-B2B"
to_version: "1.0.0"
migration_type: "full_rewrite"
created: "2025-12-15"
author: "Jan Kowalski"
status: "completed"
completion_date: "2026-01-10"
---

# Migration Guide: PRD-008-B2C v2.5.3 → PRD-012-B2B v1.0.0

## Executive Summary

**Migration Type:** Full Rewrite (Complete Document Replacement)

**Powód Migracji:**
Firma Ishkarim wykonała strategiczny pivot z modelu B2C (konsumenci indywidualni) na model B2B (przedsiębiorstwa). Stary PRD dla aplikacji mobilnej B2C (freemium, social login, casual users) nie jest już aktualny. Nowy PRD dla aplikacji B2B (enterprise SaaS, SSO, compliance) został utworzony jako replacement.

**Timeline:**
- **Deprecation Announced:** 2025-12-15
- **Migration Deadline:** 2026-03-15 (90 dni)
- **Sunset Date:** 2026-03-15
- **Completion Status:** ✅ Completed 2026-01-10 (ahead of deadline)

**Impact Severity:** 🔴 **CRITICAL**

Wszystkie dokumenty zależne od PRD-008-B2C muszą być zmigrowane przed sunset date. To jest breaking change wymagający complete rewrite większości downstream documents.

---

## Co Się Zmieniło?

### High-Level Changes

| Aspekt | PRD-008-B2C (Old) | PRD-012-B2B (New) | Impact |
|--------|-------------------|-------------------|--------|
| **Scope** | Mobile app dla individual users (freelancers, students) | Mobile app dla enterprise teams (500+ employees) | 🔴 HIGH |
| **Target Users** | Freelance tech writers, students (consumer personas) | Enterprise IT managers, compliance officers, team admins | 🔴 HIGH |
| **Key Requirements** | Social login, freemium tier, offline reading, public sharing | SSO/SAML, enterprise pricing, approval workflows, audit logging | 🔴 HIGH |
| **Architecture** | Simple auth (OAuth), freemium tier management, client-side caching | Multi-tenant, SSO integration, server-side audit trail, role-based access | 🔴 HIGH |
| **Compliance** | None (consumer app) | SOC2 Type II, GDPR, HIPAA-ready | 🔴 HIGH |
| **Pricing Model** | Freemium: $0 (free tier, 10 docs) / $5/month (premium, unlimited) | Enterprise SaaS: $50/user/month (minimum 10 users) | 🔴 HIGH |
| **Success Metrics** | DAU, freemium conversion rate, churn rate | Enterprise adoption rate, mobile approval completion, audit log completeness | 🟡 MEDIUM |

---

### Breaking Changes

#### 1. **Authentication Method Changed (Social Login → SSO/SAML)**

**Co się zmieniło:**
- **Old (B2C):** Social login via Facebook, Google (OAuth 2.0)
- **New (B2B):** SSO/SAML integration (Okta, Azure AD, Google Workspace)

**Dlaczego:**
Enterprise requires centralized identity management (nie pozwalają employees tworzyć accounts via social login). SSO eliminuje password sprawl i zapewnia audit trail.

**Impact:**
- **TDD:** Auth architecture complete rewrite (OAuth → SAML)
- **TEST-PLAN:** New test cases (SSO integration tests, SAML assertion validation)
- **USER-GUIDE:** Tutorial changed (social login onboarding → SSO setup guide)

**Action Required:**
- Remove all social login code (Facebook SDK, Google Sign-In)
- Implement SAML 2.0 authentication flow
- Add SSO configuration UI (dla enterprise admins)

---

#### 2. **Pricing Model Changed (Freemium → Enterprise SaaS)**

**Co się zmieniło:**
- **Old (B2C):** Freemium model
  - Free tier: 10 documents max, basic features
  - Premium tier: $5/month, unlimited docs, advanced features
- **New (B2B):** Enterprise SaaS pricing
  - No free tier (enterprise sales only)
  - $50/user/month (minimum 10 users = $500/month minimum)
  - Annual contracts (not monthly subscriptions)

**Dlaczego:**
B2B sales cycle wymaga enterprise pricing (nie self-serve freemium). Higher ARPU ($50 vs $5) justifies higher CAC (enterprise sales team).

**Impact:**
- **TDD:** Remove freemium tier logic (document limits, upgrade prompts)
- **TEST-PLAN:** Remove freemium tests (tier limits, conversion flows)
- **USER-GUIDE:** Remove upgrade tutorial, add enterprise procurement guide

**Action Required:**
- Remove all freemium tier code (document limits, paywall UI)
- Implement enterprise billing integration (Stripe Billing, annual invoices)
- Add admin panel (manage users, billing, usage analytics)

---

#### 3. **Key Features Changed (Casual Use → Enterprise Workflows)**

**Co się zmieniło:**

| Feature | B2C (Old) | B2B (New) | Rationale |
|---------|-----------|-----------|-----------|
| **Primary Use Case** | Offline reading (commute, travel) | Mobile approval workflows (approve docs on-the-go) | Enterprise admins need approve specs podczas podróży służbowych |
| **Sharing** | Public sharing links (anyone with link) | Enterprise-only sharing (audit logged, permissions-based) | Compliance requirement: no public data leakage |
| **Offline Mode** | Client-side cache (ostatnie 20 docs) | Secure offline sync (encrypted, enterprise data isolation) | Multi-tenant security: offline data musi być encrypted per tenant |
| **Collaboration** | Simple comments (like social media) | Structured approval workflows (request → review → approve/reject) | Enterprise process: formal approval required |

**Impact:**
- **TDD:**
  - Remove public sharing (add permission-based sharing)
  - Replace client-side cache → encrypted offline storage
  - Add approval workflow engine
- **TEST-PLAN:**
  - Remove public sharing tests
  - Add offline encryption tests
  - Add approval workflow tests (request, approve, reject, audit)

**Action Required:**
- Implement role-based permissions (viewer, editor, approver, admin)
- Add approval workflow (multi-step approval chains)
- Implement audit logging (all actions logged, immutable)

---

#### 4. **Compliance Requirements Added (None → SOC2, GDPR)**

**Co się zmieniło:**
- **Old (B2C):** No compliance requirements (consumer app)
- **New (B2B):** Enterprise compliance
  - SOC2 Type II certification required
  - GDPR compliance (EU customers)
  - HIPAA-ready (healthcare customers)

**Dlaczego:**
Enterprise customers require compliance certifications dla vendor selection. SOC2 = table stakes dla enterprise SaaS.

**Impact:**
- **TDD:**
  - Add audit logging system (all user actions logged)
  - Implement data retention policies (GDPR right to deletion)
  - Add encryption (data at rest, data in transit)
- **SECURITY-PLAN:** Complete rewrite (compliance requirements)
- **TEST-PLAN:** Add compliance tests (audit log validation, encryption verification)

**Action Required:**
- Implement immutable audit log (append-only, cannot be deleted)
- Add data export (GDPR right to data portability)
- Add data deletion workflow (GDPR right to be forgotten)
- Encrypt sensitive data (PII, documents)

---

### Non-Breaking Changes (Significant Updates)

#### 1. **Mobile UI Optimization dla Enterprise**

**B2C:** Casual reading UI (large fonts, social-media-like)
**B2B:** Business-focused UI (dense info, approval actions prominent)

**Impact:** 🟡 MEDIUM (UI redesign, ale core functionality similar)

---

#### 2. **Performance Requirements Updated**

**B2C:** Render <2s (500 docs limit)
**B2B:** Render <1s (enterprise może mieć 5000+ docs)

**Impact:** 🟡 MEDIUM (performance optimization required)

---

#### 3. **Success Metrics Changed**

**B2C:** DAU, freemium conversion, NPS
**B2B:** Enterprise adoption rate, mobile approval completion, audit compliance

**Impact:** 🟢 LOW (analytics tracking, nie functional change)

---

## Migration Steps

### Step 1: Preparation (Estimated Time: 2-4 hours)

**Actions:**

- [ ] **1.1. Read This Migration Guide Completely**
  - Understand all breaking changes
  - Identify impact on your document (TDD, TEST-PLAN, etc.)

- [ ] **1.2. Read PRD-012-B2B**
  - Path: `EXAMPLE-PRD-Ishkarim-B2B-Enterprise.md`
  - Focus on: §4 (Functional Requirements), §5 (NFRs)

- [ ] **1.3. Review ADR-050 (Pivot Decision)**
  - Path: `ADR-050-Pivot-B2C-to-B2B.md`
  - Understand business rationale za pivot

- [ ] **1.4. Identify All References to PRD-008-B2C**
  - Search your document dla `DOC-PRD-008-B2C` references
  - List all sections that reference old PRD

- [ ] **1.5. Schedule Migration Work**
  - Estimate effort (usually 1-2 sprints dla complete rewrite)
  - Allocate resources (developer, QA, tech writer)

**Affected Documents:**
- DOC-TDD-008-B2C → DOC-TDD-012-B2B
- DOC-TEST-PLAN-008-B2C → DOC-TEST-PLAN-012-B2B
- DOC-USER-GUIDE-008-B2C → DOC-USER-GUIDE-012-B2B
- DOC-SECURITY-PLAN-003-B2C → DOC-SECURITY-PLAN-005-B2B

**Checklist:**
- [ ] Migration guide read
- [ ] PRD-012-B2B read
- [ ] References identified
- [ ] Work scheduled

---

### Step 2: Update References (Estimated Time: 30 min)

**Old References (Find & Replace):**
```yaml
# Front-matter (OLD)
dependencies:
  - id: DOC-PRD-008-B2C
    type: requires
    reason: "TDD bazuje na PRD"
```

**New References:**
```yaml
# Front-matter (NEW)
dependencies:
  - id: DOC-PRD-012-B2B
    type: requires
    reason: "TDD bazuje na PRD dla enterprise B2B model"
```

**Documents to Update:**

- [ ] **Front-matter dependencies section** (YAML)
- [ ] **Cross-references section** (Markdown)
- [ ] **Text body references** (links, citations)

**Find & Replace Commands:**
```bash
# Git grep to find all references
git grep -l "DOC-PRD-008-B2C"

# Sed to replace (careful - review before committing!)
sed -i 's/DOC-PRD-008-B2C/DOC-PRD-012-B2B/g' *.md
```

**Checklist:**
- [ ] Front-matter dependencies updated
- [ ] Cross-references section updated
- [ ] Text body references updated
- [ ] Links tested (all links valid)

---

### Step 3: Content Migration (Estimated Time: 2-5 days)

**Section-by-Section Mapping:**

| Old Document Section (B2C) | New Document Section (B2B) | Action Required |
|---------------------------|---------------------------|-----------------|
| **§3: Personas / Użytkownicy** | **§3: Personas / Użytkownicy** | 🔴 **REWRITE** (completely different users) |
| §3.1: Freelance Tech Writer | §3.1: Enterprise IT Manager | Replace persona (consumer → enterprise admin) |
| §3.2: Student | ❌ Removed | Delete (B2B nie targetuje students) |
| N/A | §3.2: Compliance Officer | Add new persona (enterprise requirement) |
| **§4: Functional Requirements** | **§4: Functional Requirements** | 🔴 **MAJOR UPDATE** (many breaking changes) |
| §4 FR-01: Social Login | §4 FR-01: SSO/SAML Authentication | Rewrite (OAuth → SAML) |
| §4 FR-02: Freemium Tier Management | ❌ Removed | Delete (no freemium w B2B) |
| N/A | §4 FR-02: Multi-tenant User Management | Add new (enterprise requirement) |
| §4 FR-03: Offline Reading | §4 FR-03: Secure Offline Sync | Update (add encryption, multi-tenant isolation) |
| §4 FR-04: Public Sharing | §4 FR-04: Enterprise Sharing (Permissions) | Rewrite (public → permission-based) |
| N/A | §4 FR-05: Approval Workflows | Add new (enterprise key feature) |
| N/A | §4 FR-06: Audit Logging | Add new (compliance requirement) |
| **§5: NFRs** | **§5: NFRs** | 🟡 **UPDATE** (add compliance NFRs) |
| §5 NFR-01: Performance | §5 NFR-01: Performance | Update thresholds (500 docs → 5000 docs) |
| §5 NFR-02: Offline-first | §5 NFR-02: Offline Security | Update (add encryption requirement) |
| N/A | §5 NFR-03: SOC2 Compliance | Add new (certification requirement) |
| N/A | §5 NFR-04: Audit Trail Completeness | Add new (100% actions logged) |
| N/A | §5 NFR-05: Multi-tenancy Isolation | Add new (zero data leakage between tenants) |

---

#### Detailed Migration Instructions per Section

##### §3: Personas (CRITICAL - Complete Rewrite)

**Old Persona 1 (B2C):**
```markdown
## Persona 1: Freelance Tech Writer

**Imię:** Maria, 28 lat
**Goals:** Czytać docs w pociągu, dodać quick notes
**Pain Points:** Desktop-only, brak offline access
**Willingness to Pay:** Low ($5/month max)
```

**New Persona 1 (B2B):**
```markdown
## Persona 1: Enterprise IT Manager

**Imię:** Piotr, 42 lata
**Rola:** IT Manager w firmie 500+ employees
**Goals:** Approve technical specs via mobile (podczas podróży służbowych)
**Pain Points:** Nie mogę approve poza biurem → delays w projektach
**Requirements:** SSO (no separate password), audit logging (compliance)
**Budget:** High (enterprise budget: $50/user/month OK)
```

**Action:**
1. Delete old B2C personas (Freelancer, Student)
2. Add new B2B personas:
   - Enterprise IT Manager (primary)
   - Compliance Officer (secondary)
   - Team Lead (tertiary)
3. Update persona template fields:
   - Remove: "Willingness to Pay" (B2B = enterprise procurement, not individual decision)
   - Add: "Compliance Requirements", "Procurement Process"

**Checklist:**
- [ ] Old personas deleted
- [ ] New personas added (3 minimum)
- [ ] Persona fields updated (add compliance, remove willingness to pay)

---

##### §4: Functional Requirements (CRITICAL - Many Breaking Changes)

**FR-01: Authentication**

**Old (B2C):**
```markdown
## FR-01: Social Login

User może zalogować się via Facebook lub Google (OAuth 2.0).

**AC-01:** Click "Login with Facebook" → redirects to FB login
**AC-02:** User approves → app receives OAuth token
**AC-03:** User profile created (name, email from FB)
```

**New (B2B):**
```markdown
## FR-01: SSO/SAML Authentication

User może zalogować się via enterprise SSO provider (Okta, Azure AD, Google Workspace).

**AC-01:** Click "Login with SSO" → redirects to corporate IdP
**AC-02:** User authenticates via corporate credentials → SAML assertion returned
**AC-03:** App validates SAML assertion → creates/updates user profile
**AC-04:** User role mapped from SAML attributes (e.g., admin, viewer)
**AC-05:** SSO login time <500ms (performance requirement)
```

**Migration Actions:**
1. Delete all social login requirements (FR-01, FR-02 old)
2. Add SSO requirements (SAML 2.0 spec compliance)
3. Update acceptance criteria:
   - Add: SAML assertion validation
   - Add: Role mapping from IdP attributes
   - Add: Performance requirement (<500ms login)

**Checklist:**
- [ ] Social login requirements deleted
- [ ] SSO requirements added
- [ ] Acceptance criteria updated (SAML validation, role mapping)
- [ ] Performance criteria added (<500ms)

---

**FR-02: User Management**

**Old (B2C):**
```markdown
## FR-02: Freemium Tier Management

System enforces tier limits:
- Free tier: 10 documents max
- Premium tier: unlimited documents

**AC-10:** Free user creates 11th document → paywall shown
**AC-11:** User upgrades to premium → limits removed
```

**New (B2B):**
```markdown
## FR-02: Multi-tenant User Management

Admin może zarządzać users w ramach swojej organizacji (tenant).

**AC-10:** Admin invites user → invitation email sent
**AC-11:** User accepts invite → added to tenant (zero access to other tenants)
**AC-12:** Admin assigns role (viewer, editor, approver, admin)
**AC-13:** Admin deactivates user → user access revoked immediately
**AC-14:** Tenant isolation: User A (Tenant 1) cannot see data from Tenant 2
```

**Migration Actions:**
1. Delete freemium tier requirements completely
2. Add multi-tenant user management:
   - User invitation flow
   - Role-based access control (RBAC)
   - Tenant isolation (security requirement)

**Checklist:**
- [ ] Freemium requirements deleted
- [ ] Multi-tenant management added
- [ ] RBAC requirements added
- [ ] Tenant isolation requirements added

---

**FR-05: Approval Workflows (NEW - Critical Enterprise Feature)**

**Old (B2C):** ❌ None (casual comments only)

**New (B2B):**
```markdown
## FR-05: Approval Workflows

User może request approval dla dokumentu → approval chain → final decision.

**AC-30:** User submits document dla approval → status zmienia się na "pending-approval"
**AC-31:** Approvers receive notification (email + push notification)
**AC-32:** Approver reviews document via mobile → approve/reject/comment
**AC-33:** Approval decision logged (audit trail: who approved, when, comment)
**AC-34:** All approvers approve → status zmienia się na "approved"
**AC-35:** Any approver rejects → status zmienia się na "rejected" (with reason)
```

**Migration Actions:**
1. Add approval workflow requirements (NEW section)
2. Define approval states (pending, approved, rejected)
3. Define notification channels (email, push, in-app)
4. Define audit requirements (who, when, why logged)

**Checklist:**
- [ ] Approval workflow section added
- [ ] Approval states defined
- [ ] Notification requirements added
- [ ] Audit logging requirements added

---

##### §5: Non-Functional Requirements (MAJOR UPDATE - Add Compliance)

**NFR-03: SOC2 Compliance (NEW - Critical)**

**Old (B2C):** ❌ None

**New (B2B):**
```markdown
## NFR-03: SOC2 Type II Compliance

System must achieve SOC2 Type II certification.

**Requirements:**
- REQ-01: All user actions logged (immutable audit trail)
- REQ-02: Data encrypted at rest (AES-256)
- REQ-03: Data encrypted in transit (TLS 1.3)
- REQ-04: Access controls enforced (RBAC, principle of least privilege)
- REQ-05: Regular security audits (quarterly penetration tests)
- REQ-06: Incident response plan (documented, tested annually)

**Measurement:**
- SOC2 Type II audit passing (annual certification)
- Zero critical vulnerabilities (penetration test results)
```

**Migration Actions:**
1. Add SOC2 compliance section (NEW)
2. Add GDPR compliance section (NEW)
3. Add encryption requirements (data at rest, in transit)
4. Add audit logging requirements (100% coverage)

**Checklist:**
- [ ] SOC2 requirements added
- [ ] GDPR requirements added
- [ ] Encryption requirements defined
- [ ] Audit logging coverage defined (100%)

---

### Step 4: Validation (Estimated Time: 1-2 days)

**Validation Checklist:**

**4.1. Completeness Check**
- [ ] All required sections present (per specs_doc_types.md dla PRD)
- [ ] All dependencies updated (front-matter references PRD-012-B2B)
- [ ] All cross-references valid (no broken links)
- [ ] Changelog updated (version bump, breaking changes documented)

**4.2. Consistency Check**
- [ ] Requirements consistent z PRD-012-B2B
  - Authentication: SSO (not social login) ✓
  - Pricing: Enterprise SaaS (not freemium) ✓
  - Compliance: SOC2, GDPR (not none) ✓
- [ ] Acceptance criteria testable
- [ ] No deprecated terms (e.g., "freemium", "social login")

**4.3. Stakeholder Review**
- [ ] Tech Lead reviewed (architecture feasible)
- [ ] QA Lead reviewed (testable requirements)
- [ ] Product Owner approved (business alignment)

**4.4. Migration Evidence**
- [ ] Diff generated (`git diff PRD-008-B2C PRD-012-B2B`)
- [ ] Migration notes documented (what changed, why)
- [ ] Stakeholders notified (migration completed)

---

### Step 5: Notification & Communication (Estimated Time: 2-4 hours)

**5.1. Update Document Status**

```yaml
# Your document front-matter (e.g., TDD-012-B2B)
cross_reference_status:
  upstream_changes_pending:
    - id: DOC-PRD-008-B2C
      acknowledged: true
      acknowledged_by: "Your Name"
      acknowledged_date: "YYYY-MM-DD"
      acknowledgment_notes: "Migrated to PRD-012-B2B - all requirements updated"
```

**5.2. Notify Stakeholders**

**Email Template:**
```
Subject: [MIGRATION COMPLETE] TDD-008-B2C → TDD-012-B2B

Team,

Migration z PRD-008-B2C (deprecated) do PRD-012-B2B (B2B model) została zakończona.

Document: DOC-TDD-012-B2B
New Version: 2.0.0 (MAJOR bump - breaking changes)
Completion Date: YYYY-MM-DD

Key Changes:
- Authentication: Social login → SSO/SAML
- Pricing: Freemium logic removed → enterprise user management
- Features: Casual reading → approval workflows, audit logging
- Compliance: None → SOC2, GDPR requirements

Migration Guide: [link]
Changelog: [link]

Next Steps:
- TEST-PLAN-012-B2B: Update test cases (target: +2 weeks)
- Implementation: Start Sprint X (target: Q2 2026)

Questions? Contact: [Your Name]

---
Ishkarim Engineering Team
```

**5.3. Update Roadmap**

- [ ] Mark PRD-008-B2C migration as "completed" w project tracker
- [ ] Update dependencies (TDD-012-B2B now blocks implementation)

---

## Examples

### Example 1: TDD Migration (Complete Rewrite)

**Scenario:** TDD-008-B2C (Technical Design dla B2C app) → TDD-012-B2B (Technical Design dla B2B app)

**Old TDD-008-B2C - §3: Authentication Module**
```markdown
## §3: Authentication Module

### 3.1. OAuth Social Login

**Architecture:**
- Client-side OAuth flow (Facebook SDK, Google Sign-In)
- Token storage: localStorage (OAuth tokens)
- Session management: JWT (7-day expiry)

**Components:**
- `AuthService` (handles OAuth redirects)
- `TokenManager` (stores/retrieves tokens)
- `SocialLoginButtons` (UI component - FB, Google buttons)

**API Endpoints:**
- POST /auth/facebook (exchange FB token for app token)
- POST /auth/google (exchange Google token for app token)
```

**New TDD-012-B2B - §3: Authentication Module**
```markdown
## §3: Authentication Module

### 3.1. SAML SSO Authentication

**Architecture:**
- Server-side SAML flow (SAML 2.0 compliant)
- Token storage: Secure session cookies (HttpOnly, SameSite=Strict)
- Session management: Server-side sessions (Redis), 8-hour expiry
- Multi-tenant: Tenant identified by subdomain (tenant1.ishkarim.com)

**Components:**
- `SAMLService` (handles SAML assertions, validates signatures)
- `TenantResolver` (identifies tenant from subdomain)
- `SessionManager` (server-side session storage)
- `SSOLoginButton` (UI component - "Login with SSO" button)

**API Endpoints:**
- GET /auth/sso (initiates SAML auth request)
- POST /auth/sso/callback (receives SAML assertion, validates, creates session)
- GET /auth/metadata (SAML metadata endpoint dla IdP configuration)

**Security:**
- SAML assertion signature verification (X.509 certificate)
- Encryption: SAML assertions encrypted (AES-256)
- Audit: All logins logged (timestamp, user, tenant, IP address)
```

**Migration Actions:**
1. Delete OAuth components (`AuthService`, `SocialLoginButtons`)
2. Implement SAML components (`SAMLService`, `TenantResolver`)
3. Replace client-side token storage → server-side sessions
4. Add tenant isolation logic
5. Add audit logging dla all authentication events

---

### Example 2: TEST-PLAN Migration (Update Test Cases)

**Old TEST-PLAN-008-B2C - Test Case TC-10: Social Login**
```markdown
## TC-10: Facebook Login Success

**Preconditions:** User has Facebook account

**Steps:**
1. Click "Login with Facebook" button
2. Redirected to Facebook login page
3. Enter Facebook credentials
4. Approve app permissions
5. Redirected back to app

**Expected Result:**
- User logged in
- Profile created (name, email from Facebook)
- localStorage contains OAuth token

**Priority:** P0
```

**New TEST-PLAN-012-B2B - Test Case TC-10: SSO Login Success**
```markdown
## TC-10: SSO Login Success (Okta)

**Preconditions:**
- Tenant configured with Okta SSO
- User exists in Okta (corporate directory)

**Steps:**
1. Navigate to tenant subdomain (tenant1.ishkarim.com)
2. Click "Login with SSO" button
3. Redirected to Okta login page
4. Enter corporate credentials (email, password)
5. 2FA challenge (if enabled)
6. Redirected back to app

**Expected Result:**
- User logged in
- Session created (server-side, 8-hour expiry)
- User role mapped from Okta attributes (e.g., "admin")
- Audit log entry created (login timestamp, user, tenant, IP)

**Priority:** P0

**Security Validation:**
- SAML assertion signature verified ✓
- Session cookie HttpOnly, SameSite=Strict ✓
- Audit log entry immutable ✓
```

**Migration Actions:**
1. Delete all social login test cases (TC-10 to TC-15)
2. Add SSO test cases:
   - TC-10: SSO Login Success (Okta)
   - TC-11: SSO Login Success (Azure AD)
   - TC-12: SSO Login Failure (invalid SAML assertion)
   - TC-13: SSO Login - Role Mapping
   - TC-14: SSO Login - Audit Trail Verification
3. Add multi-tenant test cases:
   - TC-20: Tenant Isolation (user cannot access other tenant data)

---

### Example 3: USER-GUIDE Migration (Tutorial Rewrite)

**Old USER-GUIDE-008-B2C - Chapter 2: Getting Started**
```markdown
## Chapter 2: Getting Started

### 2.1. Creating an Account

1. Download Ishkarim Mobile App (App Store / Google Play)
2. Open app → tap "Get Started"
3. Choose sign-up method:
   - **Login with Facebook** (recommended - fastest)
   - Login with Google
   - Email + password (manual)
4. Approve app permissions (read basic info, email)
5. Account created! Start with **free tier** (10 documents)

### 2.2. Upgrading to Premium

Need more than 10 documents? Upgrade to Premium!

1. Tap "Upgrade" button (appears when you hit 10-doc limit)
2. Choose plan: $5/month or $50/year (save 17%)
3. Enter payment method (credit card, PayPal)
4. Confirm → Premium unlocked! Unlimited documents ✨
```

**New USER-GUIDE-012-B2B - Chapter 2: Getting Started**
```markdown
## Chapter 2: Getting Started (Enterprise Admins)

### 2.1. Setting Up SSO

**Prerequisites:**
- Enterprise subscription active ($50/user/month)
- Access to corporate Identity Provider (Okta, Azure AD, etc.)

**Steps:**

1. **Admin Panel → Settings → SSO Configuration**
2. **Choose your Identity Provider:**
   - Okta
   - Azure AD
   - Google Workspace
   - Custom SAML 2.0 provider
3. **Copy SAML Metadata URL** from Ishkarim
   - Example: `https://tenant1.ishkarim.com/auth/metadata`
4. **Configure in your IdP:**
   - Create new SAML app (Ishkarim)
   - Paste metadata URL
   - Map attributes:
     - Email → `email`
     - Full Name → `displayName`
     - Role → `role` (admin, viewer, editor)
5. **Test SSO login:**
   - Open incognito window
   - Navigate to `https://tenant1.ishkarim.com`
   - Click "Login with SSO"
   - Verify redirect to corporate IdP
   - Login with corporate credentials
   - Verify successful login + correct role mapping

### 2.2. Inviting Users

**Admin Panel → Users → Invite User**

1. Enter user email (must be corporate email domain)
2. Assign role:
   - **Viewer:** Can read documents only
   - **Editor:** Can read + edit documents
   - **Approver:** Can read + edit + approve documents
   - **Admin:** Full access (manage users, billing, settings)
3. Click "Send Invitation"
4. User receives email → clicks link → SSO login → added to tenant

**Note:** No manual password setup - users authenticate via corporate SSO only.
```

**Migration Actions:**
1. Delete consumer onboarding tutorial (social login, freemium upgrade)
2. Add enterprise setup guide (SSO configuration, user management)
3. Target audience change: individual users → enterprise admins
4. Add screenshots (admin panel, SSO config screens)

---

## Frequently Asked Questions

### Q: Czy muszę migrować wszędzie naraz?

**A:** ❌ Nie - możesz migrować incrementally:

**Option 1: Big Bang Migration** (1-2 sprints, all at once)
- ✅ Pros: Clean cut, wszystko migrated razem
- ❌ Cons: High risk, długi development freeze

**Option 2: Incremental Migration** (3-4 sprints, per module)
- ✅ Pros: Lower risk, continuous delivery
- ❌ Cons: Temporary inconsistency (some modules B2C, some B2B)

**Recommendation:** Incremental migration dla large codebases (>100k LOC), Big Bang dla small (<20k LOC).

---

### Q: Co jeśli nie zdążę przed sunset date?

**A:** ⚠️ **Escalate immediately:**

1. **Contact Migration Owner** (Jan Kowalski) → discuss extension
2. **If critical blocker:** Sunset date może być extended (case-by-case)
3. **If non-critical:** Document może zostać archived bez migration (jeśli no longer needed)

**Deadline Extensions:**
- Granted dla: Critical production blockers, unforeseen technical debt
- NOT granted dla: Poor planning, low priority

---

### Q: Gdzie znaleźć help jeśli stuck?

**A:** 📞 **Support Channels:**

1. **Slack:** #ishkarim-b2b-migration (primary channel - fastest response)
2. **Office Hours:** Środy 14:00-15:00 (Zoom link w Slack)
3. **Email:** jan.kowalski@example.com (migration owner)
4. **Wiki:** https://wiki.example.com/b2b-migration (FAQ, troubleshooting)

**Escalation Path:**
- Stuck >4 hours → Post in Slack
- Stuck >1 day → Attend office hours
- Blocked (critical) → Email + tag @migration-owner w Slack

---

### Q: Czy mogę reuse code z B2C?

**A:** ⚠️ **Partially:**

**Reusable (Minor Changes):**
- ✅ UI components (buttons, forms - minor styling updates)
- ✅ Offline storage logic (add encryption)
- ✅ Document rendering (core markdown parser)

**NOT Reusable (Complete Rewrite):**
- ❌ Authentication (OAuth → SAML = completely different)
- ❌ Freemium logic (delete completely)
- ❌ Public sharing (permission-based = different architecture)

**Recommendation:**
- Review existing code → identify reusable parts
- Don't force reuse (sometimes clean rewrite faster than refactor)

---

## Impact on Downstream Documents

### Summary Table

| Document | Impact | Status | Completion Date | Owner |
|----------|--------|--------|-----------------|-------|
| **DOC-TDD-008-B2C** | 🔴 HIGH (rewrite) | ✅ Migrated | 2025-12-20 | Piotr Wiśniewski |
| **DOC-TEST-PLAN-008-B2C** | 🔴 HIGH (new tests) | ✅ Migrated | 2025-12-22 | Maria Nowak |
| **DOC-USER-GUIDE-008-B2C** | 🟡 MEDIUM (rewrite tutorials) | ✅ Migrated | 2026-01-10 | Anna Kowalska |
| **DOC-SECURITY-PLAN-003-B2C** | 🔴 HIGH (add compliance) | ✅ Migrated | 2025-12-28 | Security Team |
| **DOC-BUSINESS-CASE-003-B2C** | 🔴 CRITICAL (new doc) | ✅ Replaced | 2025-12-18 | Product Owner |

---

## Migration Completion Criteria

**Migration Complete When:**

- [x] All downstream documents migrated (5/5 completed ✅)
- [x] All stakeholders notified (emails sent, acknowledged)
- [x] PRD-008-B2C deprecated (status changed 2025-12-15)
- [x] Cross-references updated (all docs reference PRD-012-B2B)
- [x] Changelog updated (breaking changes documented)
- [x] Migration guide published (this document)
- [x] Lessons learned documented (see below)

**Status:** ✅ **MIGRATION COMPLETE** (2026-01-10, ahead of 2026-03-15 deadline)

---

## Lessons Learned

### Co Zadziałało

1. **Clear Migration Guide:**
   - Detailed section mapping = teams wiedziały exactly what to do
   - Examples (TDD, TEST-PLAN, USER-GUIDE) = practical reference

2. **90-Day Migration Period:**
   - Enough time dla teams (even completed early)
   - Multiple checkpoints (30-day, 14-day warnings) = no surprises

3. **Office Hours:**
   - Weekly Q&A sessions = szybkie rozwiązywanie blockers
   - Slack channel = async communication dla quick questions

### Co Poprawić

1. **Earlier Communication:**
   - **Problem:** Some teams nie wiedzieli o pivocie until deprecation notice
   - **Fix:** Next time: announce strategic decisions 30+ days before deprecation

2. **Automated Validation:**
   - **Problem:** Manual checking references (prone to errors)
   - **Fix:** Create script to validate cross-references (TODO dla Phase 2)

3. **Code Examples:**
   - **Problem:** Teams asked dla code examples (not just requirements)
   - **Fix:** Include code snippets w migration guide (added dla TDD example)

---

## Metadata

**Migration Guide Created:** 2025-12-15
**Created By:** Jan Kowalski (Migration Owner)
**Last Updated:** 2026-01-10 (completion date)
**Status:** Completed
**Migration Duration:** 26 days (2025-12-15 → 2026-01-10, ahead of 90-day deadline)

**Tags:** `migration`, `B2C-to-B2B`, `breaking-change`, `PRD-008`, `PRD-012`

---

**Koniec Migration Guide**

**Migration Status:** ✅ **COMPLETED** (all downstream docs migrated)
**Completion Rate:** 100% (5/5 documents)
**Timeline:** Ahead of schedule (26 days vs 90-day deadline)
**Lessons:** Documented dla future migrations
