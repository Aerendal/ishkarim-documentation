# Semantic Changelog Template

**Living Documentation Framework (PROPOZYCJA-2)**

Ten szablon pokazuje jak prowadzić changelog z wykorzystaniem semantic versioning dla dokumentów.

---

## Front-Matter

```yaml
---
id: CHANGELOG-<DOC-ID>
type: changelog
parent_document: "DOC-<id>"
last_updated: "YYYY-MM-DD"
---
```

---

## Changelog - DOC-<ID>

### Format wersji: MAJOR.MINOR.PATCH

**Semantic Versioning dla dokumentów:**
- **MAJOR**: Breaking change (np. zmiana scope, pivot, breaking dependency change)
- **MINOR**: Non-breaking addition (np. nowa sekcja, rozszerzone wymagania)
- **PATCH**: Fix/clarification (np. typo, formatowanie, drobna clarification)

---

## [X.Y.Z] - YYYY-MM-DD (TYPE)

### Added
- Lista nowych elementów dodanych do dokumentu
- Nowe sekcje, wymagania, funkcjonalności

### Changed
- Lista zmienionych elementów
- Modyfikacje istniejących sekcji

### Fixed
- Lista poprawek
- Błędy, typo, inconsistencies

### Removed
- Lista usuniętych elementów (zazwyczaj MAJOR change)

### Deprecated
- Lista elementów oznaczonych jako deprecated (do usunięcia w przyszłości)

**Metadata:**
- **Breaking:** Yes/No
- **Impact:** Lista dokumentów, które wymagają aktualizacji
- **Migration Guide:** Link do migration guide (jeśli breaking change)

---

## Przykład: PRD Changelog

```markdown
# Changelog - DOC-PRD-001

## [2.3.1] - 2025-12-27 (PATCH)

### Fixed
- Clarified acceptance criteria in §7 (ambiguous language regarding payment flow)
- Fixed typo in §5.2 (user role description)

### Changed
- None

### Added
- None

### Removed
- None

**Metadata:**
- **Breaking:** No
- **Impact:** None (clarification only)
- **Author:** Jan Kowalski
- **Reviewers:** Anna Nowak, Piotr Wiśniewski

---

## [2.3.0] - 2025-12-20 (MINOR)

### Added
- New §8: Payment Gateway Integration Requirements
  - Added FR-23: Support for credit card payments via Stripe
  - Added FR-24: Support for PayPal integration
- Added 2 new user personas: "Enterprise Buyer", "Finance Manager"

### Changed
- Updated §5: Functional Requirements
  - Expanded FR-15 to include payment notifications
  - Added acceptance criteria to FR-10

### Fixed
- None

### Removed
- None

**Metadata:**
- **Breaking:** No
- **Impact:**
  - DOC-TDD-001: Requires update (new integration architecture for payment gateway)
  - DOC-TEST-PLAN-001: Requires new test cases (payment flows, Stripe/PayPal integration testing)
  - DOC-SECURITY-PLAN-001: Should review PCI-DSS requirements
- **Author:** Anna Nowak
- **Reviewers:** Tech Lead, Security Lead
- **Related ADRs:** ADR-045 (Payment Gateway Selection)

---

## [2.0.0] - 2025-11-15 (MAJOR)

### Changed
- **BREAKING:** Pivoted from B2C to B2B model
  - Complete rewrite of §3: Target Users (from individual consumers to enterprise buyers)
  - Complete rewrite of §6: Pricing Model (from freemium to enterprise SaaS)
  - Updated §5: Functional Requirements
    - Removed: Social login (FR-03, FR-04)
    - Added: SSO/SAML integration (FR-30, FR-31)
    - Added: Multi-tenant architecture requirements (FR-32-FR-35)

### Added
- New §9: Enterprise Features
  - Admin portal requirements
  - User management and provisioning
  - Audit logging
- New NFR: Compliance requirements (GDPR, SOC2)

### Removed
- §7: Viral Growth Features (no longer applicable for B2B)
- FR-03: Facebook login
- FR-04: Google login
- FR-20-22: Referral program features

**Metadata:**
- **Breaking:** Yes
- **Impact:**
  - DOC-BUSINESS-CASE-001: **Requires complete rewrite** (different TAM/SAM, revenue model)
  - DOC-MARKET-ANALYSIS-001: **Requires complete rewrite** (different target market)
  - DOC-TDD-001: **Requires major update** (architecture changes for multi-tenancy, SSO)
  - DOC-TEST-PLAN-001: **Requires update** (different test scenarios for enterprise)
  - DOC-SECURITY-PLAN-001: **Requires update** (enterprise security requirements)
- **Migration Guide:** [PRD v1.x → v2.0 Migration](../migrations/PRD-001-v1-to-v2.md)
- **Author:** Piotr Wiśniewski
- **Reviewers:** Executive Team, Product Team, Engineering Team
- **Related ADRs:**
  - ADR-040 (Pivot Decision: B2C to B2B)
  - ADR-041 (Multi-tenant Architecture)
  - ADR-042 (SSO/SAML Integration Strategy)

---

## [1.5.2] - 2025-11-01 (PATCH)

### Fixed
- Corrected acceptance criteria in §5.8 (API response time requirements)
- Fixed broken links to evidence documents

### Changed
- None

### Added
- None

**Metadata:**
- **Breaking:** No
- **Impact:** None
- **Author:** Jan Kowalski

---

## [1.5.1] - 2025-10-25 (PATCH)

### Fixed
- Typo in §4: User personas (corrected "manger" to "manager")
- Formatting improvements in §6: NFRs

**Metadata:**
- **Breaking:** No
- **Impact:** None
- **Author:** Anna Nowak

---

## [1.5.0] - 2025-10-20 (MINOR)

### Added
- New §7: Analytics Requirements
  - FR-25: User activity tracking
  - FR-26: Custom event logging
  - FR-27: Dashboard for analytics

### Changed
- Updated §5.5: Added detailed acceptance criteria for search functionality

**Metadata:**
- **Breaking:** No
- **Impact:**
  - DOC-TDD-001: Requires update (analytics integration architecture)
  - DOC-TEST-PLAN-001: Requires new test cases (analytics flows)
- **Author:** Jan Kowalski
- **Reviewers:** Product Team

---

## [1.0.0] - 2025-10-01 (MAJOR)

### Added
- Initial release of PRD
- All core sections:
  - §1: Product Goal
  - §2: Scope
  - §3: Target Users (B2C personas)
  - §4: Functional Requirements (FR-01 to FR-19)
  - §5: Non-Functional Requirements
  - §6: Acceptance Criteria
  - §7: Dependencies
  - §8: Risks

**Metadata:**
- **Breaking:** N/A (initial release)
- **Impact:** None (initial version)
- **Author:** Piotr Wiśniewski
- **Reviewers:** Product Team, Stakeholders
- **Approved by:** Product Owner, CTO
- **Approval date:** 2025-10-15
```

---

## Wytyczne prowadzenia Changelog

1. **Zawsze używaj semantic versioning**: MAJOR.MINOR.PATCH
2. **Każdy entry powinien mieć sekcje**: Added, Changed, Fixed, Removed (nawet jeśli puste = None)
3. **Breaking changes = MAJOR bump**: Dokumentuj szczegółowo impact i migration guide
4. **Impact section jest obowiązkowy**: Lista dokumentów downstream, które wymagają aktualizacji
5. **Link do ADRs**: Jeśli zmiana wynika z architecture decision
6. **Author i Reviewers**: Zawsze dokumentuj kto wprowadził zmianę i kto zreviewował
7. **Daty w formacie ISO**: YYYY-MM-DD
8. **Migration Guide dla breaking changes**: Zawsze linkuj do przewodnika migracji

---

## Keep a Changelog Format

Ten template jest zgodny z [Keep a Changelog](https://keepachangelog.com/) oraz [Semantic Versioning](https://semver.org/), zaadaptowanymi dla dokumentacji (nie tylko kodu).

---

**Koniec szablonu**
