# Migration Guide Template

**Living Documentation Framework (PROPOZYCJA-2)**

Ten szablon służy do tworzenia migration guides gdy dokument przechodzi breaking change lub jest zastępowany nowym dokumentem.

---

## Front-Matter

```yaml
---
id: MIGRATION-<OLD-DOC-ID>-to-<NEW-DOC-ID>
type: migration_guide
from_document: "DOC-<OLD-ID>"
from_version: "X.Y.Z"
to_document: "DOC-<NEW-ID>"
to_version: "A.B.C"
migration_type: "full_rewrite | partial_merge | split | consolidation"
created: "YYYY-MM-DD"
author: "<Name>"
status: "draft | active | archived"
---
```

---

# Migration Guide: <OLD-DOC> v<X.Y.Z> → <NEW-DOC> v<A.B.C>

## Executive Summary

**Migration Type:** [Full Rewrite / Partial Merge / Document Split / Consolidation]

**Reason for Migration:**
- Brief explanation of why this migration is necessary (e.g., pivot, restructuring, scope change)

**Timeline:**
- Deprecation announced: YYYY-MM-DD
- Migration deadline: YYYY-MM-DD
- Sunset date: YYYY-MM-DD

**Impact Severity:** [Low / Medium / High / Critical]

---

## What Changed?

### High-Level Changes

| Aspect | Old Document | New Document | Impact |
|--------|-------------|--------------|--------|
| **Scope** | Description | Description | High/Medium/Low |
| **Target Users** | Description | Description | High/Medium/Low |
| **Key Requirements** | Description | Description | High/Medium/Low |
| **Architecture** | Description | Description | High/Medium/Low |

### Breaking Changes

List all breaking changes with details:

1. **[Breaking Change 1 Title]**
   - **What changed:** Description
   - **Why:** Reason
   - **Impact:** Who/what is affected
   - **Action required:** What needs to be done

2. **[Breaking Change 2 Title]**
   - **What changed:** Description
   - **Why:** Reason
   - **Impact:** Who/what is affected
   - **Action required:** What needs to be done

### Non-Breaking Changes

List significant non-breaking changes:

1. **[Change 1]**: Description
2. **[Change 2]**: Description

---

## Migration Steps

### Step 1: Preparation

**Actions:**
- [ ] Read this migration guide completely
- [ ] Identify all references to old document in your documentation
- [ ] Review affected downstream documents (TDD, TEST-PLAN, etc.)
- [ ] Schedule migration work in sprint/timeline

**Affected Documents:**
- DOC-<ID-1>: Action required
- DOC-<ID-2>: Action required

---

### Step 2: Update References

**Old references:**
```
DOC-<OLD-ID> v<X.Y.Z>
```

**New references:**
```
DOC-<NEW-ID> v<A.B.C>
```

**Documents to update:**
- [ ] DOC-<ID-1>: Update dependency references
- [ ] DOC-<ID-2>: Update Cross-References section
- [ ] DOC-<ID-3>: Update front-matter dependencies

---

### Step 3: Content Migration

**Section-by-section mapping:**

| Old Document Section | New Document Section | Action Required |
|---------------------|---------------------|-----------------|
| §1: Old Section | §1: New Section | Direct copy / Rewrite / Remove |
| §2: Old Section | §2: New Section | Direct copy / Rewrite / Remove |
| §3: Old Section | No equivalent | Remove (document why removed) |
| N/A | §4: New Section | Create new content |

**Detailed migration instructions:**

#### Old §1 → New §1
- **Action:** Direct copy with minor updates
- **Changes:** Update terminology from "B2C" to "B2B"
- **Checklist:**
  - [ ] Copy content from old §1
  - [ ] Update terminology
  - [ ] Review and validate

#### Old §2 → New §2
- **Action:** Rewrite required
- **Reason:** Scope changed significantly
- **Checklist:**
  - [ ] Review old §2 for context
  - [ ] Write new content based on new scope
  - [ ] Cross-reference with stakeholders

#### Old §3 → [Removed]
- **Reason:** No longer applicable after pivot
- **Historical value:** Keep in archived document for reference

#### New §4 [Added]
- **Reason:** New requirements for B2B model
- **Checklist:**
  - [ ] Write new section based on new requirements
  - [ ] Reference ADR-<ID> for decision context

---

### Step 4: Validation

**Validation checklist:**
- [ ] All required sections in new document are complete
- [ ] All dependencies updated in front-matter
- [ ] Cross-references updated in all affected documents
- [ ] Changelog updated in new document
- [ ] Stakeholders notified about migration
- [ ] Old document marked as deprecated with sunset date

---

### Step 5: Notification & Communication

**Stakeholders to notify:**
- [ ] Product Team
- [ ] Engineering Team
- [ ] QA Team
- [ ] Documentation Team
- [ ] Other: ___________

**Communication template:**
```
Subject: [MIGRATION REQUIRED] <OLD-DOC> → <NEW-DOC>

Team,

We are migrating from <OLD-DOC> v<X.Y.Z> to <NEW-DOC> v<A.B.C> due to [reason].

Key Changes:
- [Breaking Change 1]
- [Breaking Change 2]

Action Required:
- Review migration guide: [link]
- Update references in your documents by [deadline]
- Attend migration Q&A session: [date/time]

Timeline:
- Migration deadline: YYYY-MM-DD
- Sunset date for old doc: YYYY-MM-DD

Questions? Contact: [owner]
```

---

## Examples

### Example 1: Section Migration

**Old Document (PRD-001-B2C v1.5.0) - §3: Target Users**
```markdown
## Target Users

### Persona 1: Individual Consumer
- Age: 25-40
- Tech-savvy
- Uses social login (Facebook, Google)
- Expects freemium pricing
```

**New Document (PRD-003-B2B v2.0.0) - §3: Target Users**
```markdown
## Target Users

### Persona 1: Enterprise Buyer
- Role: IT Manager, CTO
- Company size: 100+ employees
- Requires SSO/SAML integration
- Expects enterprise SaaS pricing with SLA
```

**Migration Action:**
- Complete rewrite of user personas
- Update all downstream documents (TDD, TEST-PLAN) to reflect new personas

---

### Example 2: Requirement Migration

**Old Requirement:**
```
FR-03: User can login using Facebook account
```

**New Requirement:**
```
FR-30: User can login using SSO (SAML 2.0)
```

**Migration Action:**
- Remove FR-03 from old document
- Add FR-30 to new document
- Update TDD to remove Facebook integration, add SSO integration
- Update TEST-PLAN to remove Facebook login tests, add SSO tests

---

## Frequently Asked Questions

### Q: Can I still reference the old document?
**A:** Until the sunset date (YYYY-MM-DD), yes, but with a deprecation warning. After sunset, the document will be archived and should not be referenced.

### Q: What happens to work in progress based on old document?
**A:** [Specific guidance for your project]

### Q: Who is responsible for updating downstream documents?
**A:** Document owners are responsible. See "Affected Documents" section for assignments.

### Q: What if I find issues during migration?
**A:** Contact the migration owner: [name/email]

---

## Impact on Downstream Documents

### DOC-TDD-001: Technical Design Document

**Impact Severity:** High

**Changes Required:**
- [ ] Update architecture section (§2) - remove social login, add SSO
- [ ] Update integration section (§7) - remove Facebook/Google API, add SAML provider
- [ ] Update security section (§5) - add enterprise security requirements
- [ ] Update version: Bump to v2.0.0 (breaking change)

**Owner:** Tech Lead
**Deadline:** YYYY-MM-DD

---

### DOC-TEST-PLAN-001: Test Plan

**Impact Severity:** Medium

**Changes Required:**
- [ ] Remove test cases: TC-10 to TC-15 (social login)
- [ ] Add test cases: SSO integration tests
- [ ] Update test data: Enterprise user personas
- [ ] Update version: Bump to v1.5.0 (minor change - test case updates)

**Owner:** QA Lead
**Deadline:** YYYY-MM-DD

---

### DOC-BUSINESS-CASE-001: Business Case

**Impact Severity:** Critical

**Changes Required:**
- [ ] Complete rewrite required (different market, revenue model)
- [ ] Create new document: DOC-BUSINESS-CASE-002-B2B
- [ ] Archive old document with migration notice

**Owner:** Product Owner
**Deadline:** YYYY-MM-DD

---

## Historical Context

### Why This Migration?

[Detailed explanation of the context that led to this migration]

**Related Decisions:**
- ADR-040: Pivot Decision (B2C to B2B)
- ADR-041: Multi-tenant Architecture
- ADR-042: SSO/SAML Integration Strategy

**Business Context:**
- Market analysis showed B2B opportunity > B2C
- Enterprise customers have different requirements
- Freemium model not sustainable for our use case

---

## Migration Completion Checklist

**Before considering migration complete:**

- [ ] All affected documents updated and reviewed
- [ ] All stakeholders notified and acknowledged
- [ ] Old document status changed to "deprecated"
- [ ] Sunset date set in old document front-matter
- [ ] Migration guide published and accessible
- [ ] Q&A session conducted with teams
- [ ] Lessons learned documented
- [ ] Post-migration review scheduled (2 weeks after)

**Post-Migration Review:**
- Date: YYYY-MM-DD
- Attendees: [list]
- Agenda: Review migration success, identify improvements for future migrations

---

## Support & Contact

**Migration Owner:** [Name]
**Email:** [email]
**Slack:** [channel]
**Office Hours:** [schedule for questions]

---

**Last Updated:** YYYY-MM-DD
**Status:** [Draft / Active / Archived]

---

**Koniec szablonu**
