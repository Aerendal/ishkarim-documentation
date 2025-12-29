# Retirement Notice Template

**Living Documentation Framework (PROPOZYCJA-2)**

Ten szablon służy do dokumentowania wycofania (retirement) dokumentu z systemu.

---

## Front-Matter

```yaml
---
id: RETIREMENT-<DOC-ID>
type: retirement_notice
retired_document: "DOC-<ID>"
retired_version: "X.Y.Z"
retirement_date: "YYYY-MM-DD"
retirement_type: "deprecated | obsolete | superseded | consolidated"
created: "YYYY-MM-DD"
author: "<Name>"
---
```

---

# Retirement Notice: <DOC-ID> v<X.Y.Z>

**Retired Document:** DOC-<ID> - <Document Title>
**Final Version:** X.Y.Z
**Retirement Date:** YYYY-MM-DD
**Retirement Type:** [Deprecated / Obsolete / Superseded / Consolidated]

---

## Deprecation Banner

> **RETIRED DOCUMENT**
>
> This document has been retired as of YYYY-MM-DD.
>
> **Reason:** [Brief reason]
>
> **Replacement:** [Link to new document or migration path]
>
> **For historical reference only** - Do not use for new work

---

## Why is this document being retired?

### Business Context

[Detailed explanation of why this document is being retired]

**Examples:**
- Company pivoted from B2C to B2B model
- Technology stack changed (e.g., migrated from monolith to microservices)
- Scope consolidated into another document
- Project cancelled or deprioritized
- Requirements became obsolete due to market changes

### Triggering Event

[What specific event triggered the retirement?]

**Examples:**
- ADR-040: Decision to pivot to B2B model
- Executive decision to cancel Project Alpha
- Merger with Project Beta - documentation consolidated

---

## What replaces it?

### Replacement Document

**New Document:** DOC-<NEW-ID> - <New Document Title>
**Version:** A.B.C
**Link:** [Link to new document]

**Why is the new document better?**
- [Reason 1: e.g., reflects current business model]
- [Reason 2: e.g., aligned with new architecture]
- [Reason 3: e.g., consolidated duplicate requirements]

### Alternative: No Direct Replacement

**If no replacement exists:**

This document is retired without a direct replacement because:
- [Reason: e.g., project cancelled]
- [Reason: e.g., requirements no longer applicable]

**For similar needs, refer to:**
- [Alternative document or resource]

---

## Migration Guide

**Migration Guide Available:** [Yes / No]

**Link to Migration Guide:** [Link to migration guide document]

### Key Changes Summary

| Aspect | Retired Document | New Document | Impact |
|--------|-----------------|--------------|--------|
| **Scope** | Old scope | New scope | High/Medium/Low |
| **Target Users** | Old users | New users | High/Medium/Low |
| **Key Requirements** | Old reqs | New reqs | High/Medium/Low |

### Quick Migration Checklist

- [ ] Read migration guide: [link]
- [ ] Update all references to point to new document
- [ ] Review affected downstream documents
- [ ] Update project documentation
- [ ] Notify affected stakeholders

---

## Timeline

### Deprecation Timeline

| Phase | Date | Status | Action |
|-------|------|--------|--------|
| **Deprecation Announced** | YYYY-MM-DD | ✅ Complete | Stakeholders notified |
| **Migration Period** | YYYY-MM-DD to YYYY-MM-DD | 🔄 In Progress | Teams migrating |
| **Sunset Warning** | YYYY-MM-DD | ⏳ Pending | Final reminder (30 days before) |
| **Retirement Date** | YYYY-MM-DD | ⏳ Pending | Document archived |

### Important Dates

- **First Deprecated:** YYYY-MM-DD (status changed to "deprecated")
- **Final Warning:** YYYY-MM-DD (30 days before retirement)
- **Retirement Date:** YYYY-MM-DD (status changed to "archived")
- **Archive Location:** `archive/YYYY-MM/<doc-id>/`

---

## Affected Documents

### Documents That Referenced This Document

List all documents that referenced the retired document:

#### DOC-TDD-001: Technical Design Document
- **Impact:** High
- **Action Taken:** Updated to reference DOC-PRD-003-B2B
- **Status:** ✅ Migrated
- **Updated By:** Tech Lead
- **Updated Date:** YYYY-MM-DD

#### DOC-TEST-PLAN-001: Test Plan
- **Impact:** Medium
- **Action Taken:** Migrated test cases to new requirements
- **Status:** ✅ Migrated
- **Updated By:** QA Lead
- **Updated Date:** YYYY-MM-DD

#### DOC-BUSINESS-CASE-001: Business Case
- **Impact:** Critical
- **Action Taken:** Complete rewrite required (new document created: DOC-BUSINESS-CASE-002)
- **Status:** ✅ Migrated
- **Updated By:** Product Owner
- **Updated Date:** YYYY-MM-DD

### Documents Blocked by This Retirement

List any documents that were blocked or need changes:

- [ ] DOC-<ID>: Action required
- [x] DOC-<ID>: Completed

---

## Historical Value

### Why Keep This Document?

Even though retired, this document is preserved for:

**Historical Context:**
- [Value 1: e.g., B2C learnings may be valuable for future reference]
- [Value 2: e.g., comparison baseline for B2B metrics]
- [Value 3: e.g., audit trail for regulatory compliance]

**Specific Use Cases:**
- Researchers studying company evolution
- New team members understanding historical decisions
- Compliance audits requiring historical documentation
- Post-mortem analysis of pivot decisions

### Archived Location

**Archive Path:** `archive/YYYY-MM/<doc-id>/`

**Archive Contents:**
- Original document (final version)
- This retirement notice
- Related evidence documents
- Changelog (full history)
- Migration guide (if applicable)

**Archive Metadata:**
```yaml
archived_date: "YYYY-MM-DD"
archived_by: "<Name>"
archive_reason: "Document retired - see retirement notice"
archive_location: "archive/YYYY-MM/<doc-id>/"
historical_tag: "pivot-YYYY-MM-<context>"
```

---

## Lessons Learned

### What We Learned From This Document

[Reflections on what worked well and what didn't]

**Positive Outcomes:**
- [Learning 1: e.g., B2C user research provided valuable insights]
- [Learning 2: e.g., Initial PRD structure proved effective]

**Areas for Improvement:**
- [Learning 1: e.g., Should have validated market assumptions earlier]
- [Learning 2: e.g., Dependency management needed better tooling]

### Recommendations for Future

Based on this retirement, we recommend:

- [Recommendation 1: e.g., Earlier market validation for pivots]
- [Recommendation 2: e.g., Better impact propagation system for document changes]
- [Recommendation 3: e.g., Quarterly document review cycles]

---

## Related Documents

### Decision Records

**Architecture Decision Records:**
- ADR-040: Pivot Decision (B2C to B2B)
- ADR-041: Multi-tenant Architecture
- ADR-042: SSO/SAML Integration Strategy

**Other Decisions:**
- EXEC-DECISION-005: Strategic Pivot Announcement

### Evidence Documents

**Supporting Evidence:**
- E-090: Market Analysis (B2B opportunity assessment)
- E-091: Competitive Analysis (B2B landscape)
- E-092: Customer Interviews (Enterprise buyer personas)

### Related Retirements

**Other documents retired in this wave:**
- RETIREMENT-MARKET-ANALYSIS-001 (B2C market analysis)
- RETIREMENT-USER-RESEARCH-001 (B2C user personas)

---

## Stakeholder Communication

### Communication Log

| Date | Stakeholder | Method | Status |
|------|------------|--------|--------|
| YYYY-MM-DD | Product Team | Email + Meeting | ✅ Acknowledged |
| YYYY-MM-DD | Engineering Team | Slack + Email | ✅ Acknowledged |
| YYYY-MM-DD | QA Team | Email | ✅ Acknowledged |
| YYYY-MM-DD | Executive Team | Presentation | ✅ Acknowledged |

### Final Notification Template

```
Subject: [RETIREMENT NOTICE] DOC-<ID> Archived as of YYYY-MM-DD

Team,

DOC-<ID> (<Document Title>) has been officially retired and archived as of YYYY-MM-DD.

Reason: [Brief reason]

Replacement: DOC-<NEW-ID> (<New Document Title>)
Link: [link]

Archive Location: archive/YYYY-MM/<doc-id>/

Historical Value: This document is preserved for [reasons]

Questions? Contact: [owner]
```

---

## Approval & Sign-Off

### Retirement Approval

- **Proposed By:** [Name] on [Date]
- **Reviewed By:** [List of reviewers]
- **Approved By:** [Product Owner / Tech Lead / etc.]
- **Approval Date:** YYYY-MM-DD

### Stakeholder Acknowledgment

- [ ] Product Team - Acknowledged by [Name] on [Date]
- [ ] Engineering Team - Acknowledged by [Name] on [Date]
- [ ] QA Team - Acknowledged by [Name] on [Date]
- [ ] Documentation Team - Acknowledged by [Name] on [Date]

---

## FAQ

### Q: Can I still reference this retired document?
**A:** For historical context only. Do not use for active work. Always reference the new document: DOC-<NEW-ID>.

### Q: Where can I find the archived document?
**A:** Archive location: `archive/YYYY-MM/<doc-id>/`

### Q: What if I need information from the old document?
**A:** Check the migration guide for section mappings. Most content has been migrated to DOC-<NEW-ID>.

### Q: Who do I contact with questions?
**A:** Contact the document owner: [Name/Email]

---

## Metadata

**Retirement Notice Created:** YYYY-MM-DD
**Created By:** [Name]
**Last Updated:** YYYY-MM-DD
**Status:** [Active / Archived]

**Tags:** `retirement`, `deprecated`, `<project-name>`, `<context-tag>`

---

**End of Retirement Notice**
