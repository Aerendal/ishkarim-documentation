# Proposals — System Enhancement Proposals

## 📋 Przeznaczenie

Folder **proposals/** zawiera **propozycje rozszerzeń systemu szablonów Ishkarim** — nowe typy dokumentów, enhanced workflows, living documentation framework. To meta-dokumentacja o przyszłych ulepszeniach samego systemu.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **System evolution** — Propozycje nowych typów szablonów (research, hypothesis, experiment)
- **Workflow enhancement** — Usprawnienia procesów (concept exploration, decision templates)
- **Living documentation** — Framework dla self-updating docs
- **Stakeholder alignment** — Gather feedback on proposed enhancements
- **Prioritization** — Decide which proposals to implement (ROI, impact, effort)

## 👥 Kto używa?

- **System Architects** — Propose & evaluate enhancements
- **Template Contributors** — Understand extension patterns
- **Product Owners** — Prioritize proposals (approve/reject)
- **Developers** — Implement approved proposals
- **Documentation Teams** — Provide feedback on proposed templates

## ⏱️ Kiedy używać?

**Timing:** **Continuous** — proposals created when gaps identified

**Lifecycle Position:**
```
Proposals (Meta-layer, ongoing)
     ↓
Gap Identified → Proposal Created → Review → Approve/Reject → Implement → templates/
```

**Kiedy czytać:**
- **System planning** — Quarterly review of proposals (prioritize)
- **Gap analysis** — When existing templates don't cover use case
- **Contributing** — Before adding new template types (follow proposal pattern)

---

## 📂 Zawartość folderu (5 plików)

### 1. PROPOZYCJA-1-Research-Branch-Templates.md 💡

**ID:** PROP-001
**Status:** 💡 Proposal (awaiting approval)
**Created:** 2025-12-27
**Author:** System Architect

**Problem:**
- Template system lacks **research/spike** templates
- No formalized way to document:
  - Hypotheses (testable assumptions)
  - Experiments (PoCs, prototypes, A/B tests)
  - Research findings (competitive analysis, benchmarks)

**Gap Identified:**
- Current templates cover: pre-production (PRD, TDD), production (runbook, postmortem)
- **Missing:** Discovery/research phase templates

**Proposed Templates (7 new):**

1. **hypothesis-template.md**
   - Purpose: Document testable assumptions
   - Structure: Hypothesis, success criteria, test plan, results

2. **experiment-template.md**
   - Purpose: Plan & document experiments (A/B tests, PoCs)
   - Structure: Goal, methodology, variables, results, conclusion

3. **spike-template.md**
   - Purpose: Time-boxed research spikes (tech evaluation, feasibility)
   - Structure: Question, timebox, findings, recommendation

4. **competitive-analysis-template.md**
   - Purpose: Structured competitor analysis
   - Structure: Competitors, feature matrix, gaps, positioning

5. **benchmark-template.md**
   - Purpose: Performance benchmarking
   - Structure: Scenario, methodology, results, comparison

6. **research-findings-template.md**
   - Purpose: General research documentation
   - Structure: Question, method, findings, implications

7. **poc-template.md**
   - Purpose: Proof-of-Concept documentation
   - Structure: Goal, approach, implementation, results, go/no-go decision

**Impact:**
- **templates/** expanded by 7 files (+4% growth)
- **Coverage:** Research phase now formalized
- **Use cases:** E-080 (market research), E-143 (Cytoscape benchmark) → would use these templates

**Effort:** 2-3 days (create templates, add to specs/specs_doc_types.md)

**Recommendation:** ✅ **Approve** (fills critical gap)

### 2. PROPOZYCJA-2-Living-Documentation-Framework.md ✅ 🚧

**ID:** PROP-002
**Status:** ✅ Approved & 🚧 Partially Implemented (Phase 1)
**Created:** 2025-12-27
**Implemented:** 2025-12-29 (Phase 1 completed)

**Problem:**
- Documents become outdated (stale status, broken links, old metrics)
- No automated freshness tracking
- Manual validation tedious
- Documents treated as static artifacts with simple lifecycle (draft → approved → archived)
- No cross-reference propagation when upstream documents change
- Deprecation workflow missing (chaos when documents become obsolete)

**Proposed Solution:**
- **Living Documentation Framework** — Treat documents as living organisms that evolve with the project

**Core Features:**

1. **Extended Lifecycle States** (11 states vs 4)
   - Initial: draft, in-review
   - Active: approved, evolving, validating, refining
   - Transition: superseded, deprecated, sunset
   - Terminal: archived, migrated

2. **Semantic Versioning for Documents**
   - MAJOR.MINOR.PATCH versioning
   - Breaking change tracking
   - Version history with impacts
   - Compatibility matrix

3. **Dynamic Cross-Reference Updates**
   - Impact propagation system
   - Automatic notifications when upstream docs change
   - Acknowledgment tracking
   - Gate blocking for critical changes

4. **Deprecation Workflow**
   - Structured process: deprecated → sunset → archived/migrated
   - Migration guides
   - Retirement notices
   - 90-day sunset periods

5. **Document Health Checks**
   - Freshness checks (7 check types)
   - Dependency validity
   - Owner assignment tracking
   - Automated alerts and escalation

**Implementation Status:**

**Phase 1: Foundation** ✅ **COMPLETED** (2025-12-29)
- ✅ Extended status_order in specs_doc_types.md (11 states)
- ✅ Added lifecycle_config, version_config, deprecation_config to PRD, TDD, BUSINESS_CASE
- ✅ Created extended-front-matter-template.md
- ✅ Extended TODO-template.md with lifecycle tracking
- ✅ Created semantic-changelog-template.md
- ✅ Created migration-guide-template.md
- ✅ Created retirement-notice-template.md
- ✅ Created document-health-check-spec.md
- ✅ Created impact-propagation-rules.md

**Phase 2: Automation** ⏳ **PENDING**
- [ ] Impact propagation system (automation scripts)
- [ ] Auto-notification (email/Slack integration)
- [ ] Health dashboard (web UI)
- [ ] Deprecation workflow automation

**Phase 3: Pilot** ⏳ **PENDING**
- [ ] Pilot on 3 projects
- [ ] Feedback collection
- [ ] Refinement based on usage

**Phase 4: Rollout** ⏳ **PENDING**
- [ ] Organization-wide adoption
- [ ] Training materials
- [ ] Metrics dashboard

**Implementation Artifacts:**

Created templates in `templates/living-documentation/`:
- `extended-front-matter-template.md` — Extended YAML front-matter with lifecycle, versioning, health
- `semantic-changelog-template.md` — Semantic versioning changelog format
- `migration-guide-template.md` — Migration guide for breaking changes
- `retirement-notice-template.md` — Document retirement documentation
- `document-health-check-spec.md` — Health check specifications (7 check types)
- `impact-propagation-rules.md` — Impact propagation rules and automation

Updated core specs:
- `specs/specs_doc_types.md` — Extended with lifecycle_config, version_config, deprecation_config for key doctypes

**Impact:**
- **Phase 1:** Foundation templates ready for use
- **Reduced manual work:** (projected) Auto-updates save 2h/week when Phase 2 complete
- **Higher accuracy:** Version tracking and impact propagation reduces inconsistencies
- **Document freshness:** >80% target (vs current ~40%)
- **Consistency:** >98% valid dependencies (automated propagation)

**Effort:**
- **Phase 1:** 4 hours (COMPLETED)
- **Phase 2:** 1-2 weeks (automation)
- **Phase 3:** 2 weeks (pilot)
- **Phase 4:** 4-6 weeks (rollout)

**Recommendation:** ✅ **Approved** - Phase 1 implemented. Proceed with Phase 2 automation when ready.

**Next Steps:**
1. Review Phase 1 templates with stakeholders
2. Gather feedback on front-matter extensions
3. Plan Phase 2 automation (Python scripts, GitHub Actions)
4. Select 3 pilot projects for Phase 3

### 3. PROPOZYCJA-3-Decision-Templates-Enhancement.md 💡

**ID:** PROP-003
**Status:** 💡 Proposal
**Created:** 2025-12-27

**Problem:**
- ADR template exists, but no:
  - Decision log rollup (all decisions in one view)
  - Decision dependency graph (auto-generated)
  - Decision status tracking (accepted → deprecated when superseded)

**Proposed Enhancements:**

1. **decision-log-template.md**
   - Aggregates all ADRs into single document
   - Auto-generated from ADR-001 to ADR-N frontmatter
   - Sortable by: Date, status, impact

2. **ADR template extensions:**
   - Add: `supersedes: [ADR-XXX]` (when decision replaces old one)
   - Add: `status: accepted | deprecated | superseded_by ADR-XXX`

3. **Decision dependency graph** (auto-generated)
   - Example: ADR-002 (PySide6) DEPENDS ON ADR-001 (Python)
   - Output: Mermaid graph (already exists in DECISION-INDEX.md)

**Impact:**
- **Clarity:** All decisions visible at a glance
- **Traceability:** Understand why decisions were made (dependency chain)

**Effort:** 1 week (template + parser extension)

**Recommendation:** ✅ **Approve** (low effort, high clarity)

### 4. PROPOZYCJA-4-Concept-Exploration-Workflows.md 💡

**ID:** PROP-004
**Status:** 💡 Proposal
**Created:** 2025-12-27

**Problem:**
- Concepts (Concepts-v2) are static (18 concepts defined upfront)
- No workflow for:
  - Discovering new concepts (when system evolves)
  - Validating concepts (are they still relevant?)
  - Deprecating concepts (when superseded)

**Proposed Workflow:**

1. **Concept discovery phase:**
   - Template: `concept-exploration-template.md`
   - Use: Brainstorm new concepts (e.g., Concept 19: "Rollback Safety")
   - Structure: Concept name, definition, use cases, examples

2. **Concept validation:**
   - Criteria: Does concept appear in ≥3 documents? (frequency check)
   - Criteria: Does concept reduce complexity? (test: remove concept → harder to explain?)

3. **Concept deprecation:**
   - When concept no longer used → Mark `status: deprecated`
   - Add: `superseded_by: CONCEPT-XXX`

**Impact:**
- **Evolvability:** Concept system grows with project
- **Maintenance:** Old concepts cleaned up (no bloat)

**Effort:** 1 week (template + validation scripts)

**Recommendation:** 💡 **Consider** (nice-to-have, not critical for MVP)

### 5. PODSUMOWANIE-INTEGRUJACE-Wszystkie-Propozycje.md 📋

**ID:** PROP-SUMMARY
**Status:** 📋 Summary (integrates all proposals)
**Created:** 2025-12-27

**Cel:** Integrate all 4 proposals into unified roadmap

**Summary Table:**

| Proposal | Impact | Effort | Priority | Recommendation |
|----------|--------|--------|----------|----------------|
| PROP-001 (Research Templates) | HIGH (fills gap) | LOW (2-3 days) | P0 | ✅ Approve |
| PROP-002 (Living Docs) | HIGH (automation) | MEDIUM (1-2 weeks) | P1 | 💡 Consider |
| PROP-003 (Decision Enhancement) | MEDIUM (clarity) | LOW (1 week) | P1 | ✅ Approve |
| PROP-004 (Concept Workflows) | LOW (nice-to-have) | LOW (1 week) | P2 | 💡 Defer |

**Integrated Roadmap:**

**Phase 1 (Immediate):**
- PROP-001 (Research Templates) — 2-3 days
- PROP-003 (Decision Enhancement) — 1 week
- **Total:** ~2 weeks

**Phase 2 (Post-MVP):**
- PROP-002 (Living Docs) — 1-2 weeks
- **Total:** ~2 weeks

**Phase 3 (Future):**
- PROP-004 (Concept Workflows) — Defer until V2.0

**ROI Analysis:**
- Phase 1: High impact, low effort → **ROI: 5x**
- Phase 2: High impact, medium effort → **ROI: 3x**
- Phase 3: Low impact, low effort → **ROI: 1.5x** (nice-to-have)

**Recommendation:** Approve Phase 1, consider Phase 2 post-MVP, defer Phase 3.

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Proposals CREATED FROM:**
- Template gap analysis and consolidation (completed 2025-12-28)
- User feedback (E-081, E-082, E-083 interviews)
- System evolution needs (as project grows)

### Impacts (Co te dokumenty popychają do przodu)

**Approved Proposals EXTEND:**
- `templates/` — New template types added
- `specs/specs_doc_types.md` — New doc types registered
- `dependency_graph.md` — New connections added

### Related Documents

- **[../templates/](../templates/)** — Target for approved proposals (where new templates go)
- **[../templates/README.md](../templates/README.md)** — Template system documentation (174 templates, complete & production-ready)

---

## 📊 Statystyki

- **Liczba plików:** 5 (4 proposals + 1 integrating summary)
- **Status:** 💡 All proposals (awaiting approval)
- **New templates proposed:** 7 (PROP-001) + enhancements (PROP-002, PROP-003, PROP-004)
- **Total effort:** ~4-6 weeks (if all approved)
- **Priority:** P0 (1), P1 (2), P2 (1)

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: Reviewing proposals (quarterly)

**Czas:** 2h (stakeholder meeting)

1. Read `PODSUMOWANIE-INTEGRUJACE-Wszystkie-Propozycje.md` (10 min)
2. For each proposal:
   - Read proposal doc (PROP-00X)
   - Discuss: Impact, effort, priority
   - Vote: Approve / Consider / Reject
3. Update proposal status: 💡 Proposal → ✅ Approved / ❌ Rejected
4. Create implementation plan for approved proposals

**Output:** Roadmap for template system enhancements

### Scenario 2: Creating new proposal

**Czas:** 2-4h (research + writing)

1. Identify gap (e.g., "No template for API specs")
2. Research: Existing templates, similar patterns
3. Write proposal:
   - Problem statement
   - Proposed solution (templates, workflows)
   - Impact, effort, ROI
4. Add to `proposals/` folder: `PROPOZYCJA-N-<name>.md`
5. Update integrating summary

**Output:** New proposal ready for review

### Scenario 3: Implementing approved proposal

**Czas:** Variable (per proposal)

1. Read approved proposal (e.g., PROP-001)
2. Create new templates in `templates/`
3. Update `specs/specs_doc_types.md` (register new doc types)
4. Update `dependency_graph.md` (if new connections)
5. Test templates (create example instances)
6. Mark proposal: ✅ Approved → ✅ Implemented

**Output:** Template system extended, proposal closed

---

## ⚠️ Uwagi

### Proposals ≠ Commitments

**All proposals are SUGGESTIONS** — not guaranteed to be implemented.

**Approval process:**
1. Proposal created (anyone can propose)
2. Stakeholder review (quarterly or as-needed)
3. Vote: Approve / Consider / Reject
4. Approved → Implementation plan
5. Implemented → Close proposal

**Current status:** All 4 proposals awaiting approval (created 2025-12-27)

### Language

**All proposals in Polish** (team language).

If contributing: Write proposals in Polish for consistency.

### Template System Impact

**Be cautious:** New templates = maintenance burden.

**Before approving, ask:**
- Is this gap real? (evidence from user feedback?)
- Can existing templates be extended? (avoid duplication)
- What's maintenance cost? (updates, examples, docs)

---

## 📈 Success Criteria

**Proposals folder healthy when:**
- [ ] Proposals reviewed quarterly (stakeholder meetings)
- [ ] Approved proposals implemented within 2 sprints
- [ ] Rejected proposals archived (with rationale)
- [ ] New proposals created when gaps identified
- [ ] Integrating summary updated (roadmap current)

**Status:** 💡 **Active** (4 proposals pending review)

---

## 📖 Zobacz też

### Related

- **[../templates/](../templates/)** — Target for approved proposals
- **[../templates/README.md](../templates/README.md)** — Template system (174 templates, complete)

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Proposals (Meta-layer, System Enhancements)
**Status:** 💡 4 active proposals awaiting review
**Recommended:** Approve PROP-001 + PROP-003 (Phase 1, 2-week effort)
