# Living Documentation — Żywa Dokumentacja

## 📋 Przeznaczenie

Folder **living-documentation/** zawiera **szablony i specyfikacje dla Living Documentation Framework** — systemu dynamicznego zarządzania cyklem życia dokumentacji, który traktuje dokumenty jako **żywe organizmy ewoluujące z projektem**.

## 🎯 Funkcja

Living Documentation Framework rozwiązuje kluczowe problemy statycznej dokumentacji:

- **Problem:** Dokumenty stają się nieaktualne (stale links, outdated metrics, broken dependencies)
- **Rozwiązanie:** Automatyczne trackowanie zmian, propagacja impacts, health monitoring

**Core Features:**

1. **Extended Lifecycle** — 11 stanów (vs 4 podstawowe): draft, in-review, approved, evolving, validating, refining, superseded, deprecated, sunset, archived, migrated
2. **Semantic Versioning** — MAJOR.MINOR.PATCH dla dokumentów z tracking breaking changes
3. **Impact Propagation** — Automatyczne notyfikacje gdy upstream documents się zmieniają
4. **Deprecation Workflow** — Structured process: deprecated → sunset → archived/migrated
5. **Document Health Checks** — 7 typów sprawdzeń (freshness, dependencies, owner, completeness)

## 👥 Kto używa?

- **Document Owners** — Używają extended front-matter i lifecycle states
- **Project Managers** — Monitorują document health i acknowledge impacts
- **Tech Leads** — Reviewują migration guides przy breaking changes
- **QA Teams** — Trackują upstream changes w PRD/TDD
- **System Administrators** — Implementują automation (Phase 2)

## ⏱️ Kiedy używać?

**Timing:** **Continuous** — Living Documentation działa przez cały lifecycle projektu

**Lifecycle Position:**
```
Draft → In-Review → Approved → Evolving → Validating → Refining
                                    ↓
                          (gdy projekt się zmienia)
                                    ↓
                    Superseded / Deprecated → Sunset → Archived/Migrated
```

**Kiedy czytać/używać:**
- **Podczas tworzenia dokumentu** — Użyj extended-front-matter-template.md
- **Przy aktualizacji dokumentu** — Update version używając semantic-changelog-template.md
- **Gdy dokument się deprecates** — Użyj retirement-notice-template.md
- **Przy breaking changes** — Stwórz migration-guide-template.md
- **Monitoring zdrowia** — Sprawdź document-health-check-spec.md
- **Upstream changes** — Review impact-propagation-rules.md

---

## 📂 Zawartość folderu (6 plików)

### 1. extended-front-matter-template.md 📄

**Cel:** Szablon rozszerzonego YAML front-matter dla dokumentów w Living Documentation Framework

**Kiedy używać:**
- Tworzysz nowy dokument (PRD, TDD, BUSINESS_CASE)
- Aktualizujesz istniejący dokument do Living Documentation

**Co zawiera:**
- `status_metadata` — Historia zmian statusu z uzasadnieniami
- `lifecycle` — Tracking created, first_approved, last_modified, last_reviewed, sunset_date
- `version_metadata` — Semantic versioning (major, minor, patch) + breaking changes
- `version_history` — Pełna historia wersji z impacts
- `cross_reference_status` — Upstream changes pending, downstream impacts
- `document_health` — Status (healthy/warning/critical) + 7 checks
- `deprecation` — Metadata dla deprecated documents

**Przykłady:**
- Dokument w stanie "evolving" (Agile iteration)
- Dokument deprecated (pivot B2C → B2B)
- Dokument w stanie "validating" (testing pricing model)

**Rozmiar:** 11K
**Format:** Markdown z YAML examples

---

### 2. semantic-changelog-template.md 📝

**Cel:** Szablon changelog z semantic versioning dla dokumentów

**Kiedy używać:**
- Po każdej zmianie dokumentu (MAJOR, MINOR, PATCH)
- Tworzysz CHANGELOG satellite document

**Format versioning:**
- **MAJOR (X.0.0):** Breaking change (np. pivot, scope change, breaking dependency)
- **MINOR (x.Y.0):** Non-breaking addition (np. nowa sekcja, rozszerzone requirements)
- **PATCH (x.y.Z):** Fix/clarification (np. typo, formatowanie, clarification)

**Sekcje:**
- **Added** — Nowe elementy
- **Changed** — Zmienione elementy
- **Fixed** — Poprawki
- **Removed** — Usunięte elementy
- **Deprecated** — Oznaczone do usunięcia

**Metadata obowiązkowa:**
- Breaking: Yes/No
- Impact: Lista dokumentów do aktualizacji
- Migration Guide: Link (jeśli breaking change)

**Przykład:**
```markdown
## [2.3.0] - 2025-12-20 (MINOR)
### Added
- New §8: Payment Gateway Integration Requirements

**Impact:**
- DOC-TDD-001: Requires update (new integration architecture)
- DOC-TEST-PLAN-001: Requires new test cases
```

**Rozmiar:** 6.6K
**Zgodność:** [Keep a Changelog](https://keepachangelog.com/) + [Semantic Versioning](https://semver.org/)

---

### 3. migration-guide-template.md 🔄

**Cel:** Przewodnik migracji gdy dokument przechodzi breaking change lub jest zastępowany

**Kiedy używać:**
- MAJOR version bump (breaking change)
- Dokument deprecated i zastępowany nowym
- Pivot wymagający rewrite dokumentacji (np. B2C → B2B)

**Struktura:**

1. **Executive Summary** — Migration type, reason, timeline, impact severity
2. **What Changed?** — High-level changes table, breaking changes list
3. **Migration Steps** — Step-by-step (Preparation, Update References, Content Migration, Validation, Notification)
4. **Examples** — Section migration examples, requirement migration
5. **FAQ** — Answers to common questions
6. **Impact on Downstream Documents** — Per-document impact analysis
7. **Historical Context** — Why this migration, related ADRs

**Migration Types:**
- Full Rewrite (complete doc replacement)
- Partial Merge (consolidating docs)
- Document Split (splitting into multiple docs)
- Consolidation (merging multiple docs)

**Przykład użycia:**
```
PRD-001 v1.5.0 (B2C) → PRD-003 v2.0.0 (B2B)
- Breaking: Target users changed (consumers → enterprise)
- Migration: 90-day period
- Affected: TDD, TEST-PLAN, BUSINESS-CASE (all require updates)
```

**Rozmiar:** 8.9K

---

### 4. retirement-notice-template.md 🗄️

**Cel:** Dokumentacja wycofania (retirement) dokumentu z systemu

**Kiedy używać:**
- Dokument deprecated osiąga sunset date
- Dokument archived (no longer active)
- Dokument migrated (replaced by new doc)

**Retirement Types:**
- **Deprecated** — Marked for sunset (discouraged but usable)
- **Obsolete** — No longer applicable (project cancelled)
- **Superseded** — Replaced by newer version
- **Consolidated** — Merged into another document

**Struktura:**

1. **Deprecation Banner** — Visible alert (do not use for new work)
2. **Why is this document being retired?** — Business context, triggering event
3. **What replaces it?** — Replacement document, migration guide link
4. **Timeline** — Deprecation → Migration → Sunset → Retirement
5. **Affected Documents** — Impact analysis per downstream doc
6. **Historical Value** — Why keep archived, where stored
7. **Lessons Learned** — Reflections, recommendations for future

**Archive Metadata:**
```yaml
archived_date: "YYYY-MM-DD"
archived_by: "<Name>"
archive_location: "archive/YYYY-MM/<doc-id>/"
historical_tag: "pivot-YYYY-MM-<context>"
```

**Przykład:**
```
DOC-PRD-001 (B2C version)
- Deprecated: 2025-12-27 (pivot decision)
- Sunset: 2026-03-27 (90 days)
- Replaced by: DOC-PRD-003 (B2B version)
- Historical value: B2C learnings preserved for reference
```

**Rozmiar:** 8.8K

---

### 5. document-health-check-spec.md 🏥

**Cel:** Specyfikacja systemu automatycznych sprawdzeń zdrowia dokumentów

**Kiedy używać:**
- Implementacja health check automation (Phase 2)
- Monitoring document freshness
- Detecting stale documents
- Validating dependencies

**Health Status Levels:**
- 🟢 **HEALTHY** — All checks passed
- 🟡 **WARNING** — 1-2 checks failed (non-critical)
- 🔴 **CRITICAL** — 3+ checks failed, immediate action required

**7 Health Check Types:**

1. **Freshness Check**
   - Threshold: 90-180 days (depends on doctype)
   - Checks: last_modified, last_reviewed vs threshold

2. **Dependency Validity Check**
   - Validates: All dependencies not deprecated/archived
   - Flags: Invalid, deprecated, sunset dependencies

3. **Cross-Reference Consistency Check**
   - Validates: Bidirectional references (backlinks)
   - Flags: Missing backlinks, broken references

4. **Owner Assignment Check**
   - Validates: Document has active owner
   - Flags: No owner, owner left company, owner on extended leave

5. **Required Sections Completeness Check**
   - Validates: All required sections present
   - Flags: Missing sections, sections with placeholders (TBD, TODO)

6. **Upstream Changes Pending Check**
   - Detects: Upstream dependencies changed (version bump)
   - Flags: MAJOR (critical), MINOR (warning), PATCH (info)

7. **Satellite Completeness Check**
   - Validates: Required satellites present (TODO, CHANGELOG, EVIDENCE)
   - Flags: Missing satellites

**Execution Frequency:**
```yaml
daily: freshness_check, dependency_validity_check
weekly: cross_reference_consistency, owner_assignment, satellite_completeness
on_demand: required_sections_check (on status change)
real_time: upstream_changes_check (on dependency version bump)
```

**Output Format:**
```yaml
document_health:
  status: "healthy | warning | critical"
  last_health_check: "2025-12-27T02:00:00Z"
  checks: [...]
  overall_score: 71  # 0-100
  risk_level: "medium"
```

**Automated Actions:**
- Alert owner (email/Slack)
- Escalate to manager (if critical >7 days)
- Block gates (if critical changes not acknowledged)

**Rozmiar:** 15K

---

### 6. impact-propagation-rules.md 🔗

**Cel:** Reguły automatycznej propagacji zmian między dokumentami w dependency graph

**Kiedy używać:**
- Implementacja impact propagation automation (Phase 2)
- Upstream document changes (version bump)
- Status changes (approved → deprecated)
- Dependency added/removed

**Propagation Trigger Types:**

1. **Version Bump (Major)** — Severity: HIGH/CRITICAL
   - Actions: Notify all downstream, create P1 TODO, block gates, require ack within 14 days

2. **Version Bump (Minor)** — Severity: MEDIUM
   - Actions: Notify direct downstream, create P2 TODO, require ack within 30 days

3. **Version Bump (Patch)** — Severity: LOW
   - Actions: Weekly digest notification, no TODO created

4. **Status Change (Approved → Evolving)** — Severity: MEDIUM
   - Actions: Flag downstream docs, notify stakeholders

5. **Status Change (Approved → Deprecated)** — Severity: CRITICAL
   - Actions: Create P0 TODO, block new references, require ack within 7 days

6. **Dependency Added** — Severity: MEDIUM
   - Actions: Notify new dependency owner, update backlinks

7. **Required Section Missing** — Severity: CRITICAL
   - Actions: Block status change to approved, create P0 TODO

**Propagation Rules by Document Type:**

**BUSINESS_CASE → [PRD, TDD, FINANCIAL_PLAN]**
- Budget change (SEC-BC-FIN) → Notify all (severity: high)
- Recommendation flipped → Critical alert, block GATE-REQ_FREEZE

**PRD → [TDD, TEST_PLAN, USER_GUIDE]**
- New section added → Notify TDD/TEST_PLAN, create TODO
- Scope changed (major) → Critical alert, block gates

**TDD → [TEST_PLAN, RUNBOOK, SECURITY_PLAN]**
- API changed → Notify TEST_PLAN
- Architecture changed (major) → Critical alert to all downstream

**Acknowledgment Workflow:**
1. Change detected → Notification created
2. Owner notified → Email/Slack + TODO created
3. Owner reviews → Reads changelog, migration guide
4. Owner acknowledges → System records ack, marks TODO done
5. System validates → Unblock gates if all ack'd, escalate if deadline passed

**Notification Templates:**
- Email: Major Version Bump (detailed, with migration guide link)
- Slack: Minor Version Bump (brief, with changelog link)

**Gate Blocking Rules:**
- GATE-REQ_FREEZE: Block if critical upstream changes not ack'd
- GATE-RELEASE_READY: Block if dependencies deprecated/archived
- GATE-OPS_HANDOVER: Block if required satellites missing

**Escalation Path:**
```
Day 0: Notify owner
Day 7: Notify owner + reminder
Day 14: Notify owner + manager
Day 21: Notify owner + manager + PM
Day 30: Escalate to executive team
```

**Rozmiar:** 14K

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza ten folder)

**Living Documentation BASED ON:**
- `PROPOZYCJA-2-Living-Documentation-Framework.md` — Original proposal (2025-12-27)
- `specs/specs_doc_types.md` — Extended with lifecycle_config, version_config, deprecation_config
- `atomic/TODO-template.md` — Extended with lifecycle tracking
- User feedback (E-081, E-082, E-083 interviews) — Manual documentation work reduction needed

### Impacts (Co ten folder popycha do przodu)

**Living Documentation EXTENDS:**
- **All 148+ document templates** — Can use extended front-matter
- **specs/specs_doc_types.md** — Defines lifecycle_config for each doctype
- **Dependency graph** — Impact propagation system uses graph structure
- **Gates** — Health checks block gates when critical issues detected

### Related Documents

- **[../specs/specs_doc_types.md](../specs/specs_doc_types.md)** — Core specs with lifecycle_config
- **[../atomic/TODO-template.md](../atomic/TODO-template.md)** — Extended with lifecycle tracking
- **[../../proposals/PROPOZYCJA-2-Living-Documentation-Framework.md](../../proposals/PROPOZYCJA-2-Living-Documentation-Framework.md)** — Original proposal
- **[../../proposals/README.md](../../proposals/README.md)** — Implementation status

---

## 📊 Statystyki

- **Liczba plików:** 6 szablonów + specyfikacji
- **Total size:** ~75 KB
- **Status:** ✅ Phase 1 COMPLETED (Foundation templates ready)
- **Implementation date:** 2025-12-29
- **Extended doctypes:** PRD, TDD, BUSINESS_CASE (+ more planned)
- **New lifecycle states:** 11 (vs 4 previous)
- **Health check types:** 7
- **Propagation trigger types:** 7

---

## 🚀 Quick Start — Typowe Workflow

### Scenario 1: Tworzenie nowego dokumentu z Living Documentation

**Czas:** 15 min (dodatkowe vs standard front-matter)

1. Skopiuj szablon dokumentu (np. `PRD-template.md`)
2. Otwórz `extended-front-matter-template.md` → skopiuj extended fields
3. Uzupełnij front-matter:
   ```yaml
   status: draft
   version: "1.0.0"
   lifecycle:
     created: "2025-12-29"
   document_health:
     status: "healthy"
   ```
4. Rozpocznij pisanie dokumentu
5. Przy każdej zmianie → update version + changelog

**Output:** Dokument z pełnym lifecycle tracking od początku

---

### Scenario 2: Aktualizacja dokumentu (version bump)

**Czas:** 10-20 min (zależnie od typu zmiany)

**Minor change (np. dodanie sekcji):**

1. Edytuj dokument → dodaj nową sekcję
2. Update front-matter:
   ```yaml
   version: "1.2.0"  # Minor bump (1.1.0 → 1.2.0)
   lifecycle:
     last_modified: "2025-12-29"
   ```
3. Update CHANGELOG (użyj `semantic-changelog-template.md`):
   ```markdown
   ## [1.2.0] - 2025-12-29 (MINOR)
   ### Added
   - New §8: Payment Gateway Integration Requirements

   **Impact:**
   - DOC-TDD-001: Requires update
   ```
4. Notify downstream documents (manual w Phase 1, auto w Phase 2)

**Output:** Version bumped, changelog updated, impacts tracked

**Major change (breaking):**

1. Edytuj dokument → breaking change (np. pivot B2C → B2B)
2. Update front-matter:
   ```yaml
   version: "2.0.0"  # Major bump
   version_metadata:
     breaking_changes: true
   ```
3. Create migration guide (użyj `migration-guide-template.md`)
4. Update CHANGELOG z linkiem do migration guide
5. Notify all downstream documents (critical alert)

**Output:** Breaking change documented, migration path clear

---

### Scenario 3: Deprecating dokumentu

**Czas:** 1-2 godziny (communication + documentation)

1. Update status:
   ```yaml
   status: deprecated
   deprecation:
     deprecated_date: "2025-12-29"
     deprecation_reason: "Replaced by PRD v3.0 after B2B pivot"
     sunset_date: "2026-03-29"  # 90 days
     migration_target: "DOC-PRD-003"
   ```
2. Create migration guide (`migration-guide-template.md`)
3. Create retirement notice (`retirement-notice-template.md`)
4. Notify all referencing documents
5. Add deprecation banner to document top:
   ```markdown
   > ⚠️ **DEPRECATION NOTICE**
   > This document is deprecated as of 2025-12-29.
   > Sunset date: 2026-03-29 (90 days remaining)
   > Migration target: [DOC-PRD-003](link)
   ```

**Output:** Structured deprecation, clear migration path, 90-day sunset period

---

### Scenario 4: Monitoring document health

**Czas:** 5-10 min (manual check w Phase 1, auto w Phase 2)

1. Read `document-health-check-spec.md` → understand 7 check types
2. Manually check document:
   - ✅ Freshness: Last modified 15 days ago (threshold: 90 days) → HEALTHY
   - ✅ Dependencies: All approved/evolving → HEALTHY
   - ⚠️ Owner: Owner on vacation 10 days → WARNING
   - ✅ Sections: All required sections present → HEALTHY
   - ⚠️ Upstream changes: PRD bumped to v2.4.0, not reviewed → WARNING
   - ✅ Cross-references: All valid → HEALTHY
   - ✅ Satellites: All present → HEALTHY
3. Update front-matter:
   ```yaml
   document_health:
     status: "warning"  # 2 warnings
     last_health_check: "2025-12-29"
   ```
4. Address warnings (review upstream changes, reassign if owner extended leave)

**Output:** Document health tracked, issues identified

---

### Scenario 5: Handling upstream change notification

**Czas:** 30-60 min (review + update if needed)

**When:** Dependency document bumped version (e.g., BUSINESS_CASE v2.0.0 → v2.1.0)

1. Receive notification (email/Slack in Phase 2, manual in Phase 1):
   ```
   BUSINESS_CASE v2.1.0 (minor) - Budget increased $3M → $5M
   Action: Review scope in PRD (may expand features)
   ```
2. Review changelog:
   - Read BUSINESS_CASE changelog entry
   - Identify impact on your document (PRD)
3. Decide action:
   - **No change needed:** Acknowledge (update cross_reference_status)
   - **Update needed:** Update document, bump version
4. Update front-matter:
   ```yaml
   cross_reference_status:
     upstream_changes_pending:
       - id: DOC-BUSINESS-CASE-001
         acknowledged: true
         acknowledged_by: "Jan Kowalski"
         acknowledged_date: "2025-12-29"
         acknowledgment_notes: "Reviewed - expanding scope to include 3 new features"
   ```
5. If updated: Bump version, update changelog

**Output:** Upstream change acknowledged, downstream document updated if needed

---

## ⚠️ Uwagi

### Phase 1 vs Phase 2

**Current (Phase 1 - COMPLETED):**
- ✅ Templates ready to use
- ✅ Manual workflow (copy/paste extended front-matter)
- ✅ Manual notifications (owner notifies downstream)
- ✅ Manual health checks (owner reviews periodically)

**Future (Phase 2 - Automation):**
- ⏳ Automated impact propagation (scripts detect changes)
- ⏳ Automated notifications (email/Slack when upstream changes)
- ⏳ Automated health checks (daily/weekly cron jobs)
- ⏳ Health dashboard (web UI to monitor all docs)

**Recommendation:** Start using Phase 1 templates now (manual workflow). Automation will enhance existing metadata when Phase 2 implemented.

---

### Extended Front-Matter Size

**Warning:** Living Documentation front-matter może być długie (100-200 linii YAML).

**Mitigation:**
- Tylko kluczowe doctypes używają full extended front-matter (PRD, TDD, BUSINESS_CASE)
- Mniejsze docs (ADR, TODO, Evidence) używają subset
- Większość pól jest optional (użyj tylko gdy needed)

**Minimal Extended Front-Matter:**
```yaml
status: approved
version: "1.0.0"
lifecycle:
  created: "2025-12-29"
  last_modified: "2025-12-29"
document_health:
  status: "healthy"
```

---

### Semantic Versioning dla Dokumentów

**Note:** Semantic versioning dla dokumentów != semantic versioning dla software.

**Differences:**
- **Software:** MAJOR = breaking API change
- **Documents:** MAJOR = breaking change in scope, direction, or dependencies

**Examples:**
- **MAJOR (doc):** Pivot B2C → B2B, target users changed, scope redefined
- **MINOR (doc):** New section added, requirements expanded
- **PATCH (doc):** Typo fix, clarification, formatting

**When unsure:** Refer to `version_config.major_change_triggers` in `specs/specs_doc_types.md` for your doctype.

---

### Deprecation Timelines

**Standard deprecation period:** 90 days (from deprecated to sunset)

**Rationale:**
- 90 days = ~2 quarters = reasonable time for teams to migrate
- Critical projects may need shorter (30 days) or longer (180 days)

**Adjust based on:**
- Number of affected documents (many refs → longer period)
- Severity of migration (simple update → shorter, rewrite → longer)
- Stakeholder availability (holiday season → extend period)

**Configure in:**
```yaml
deprecation_config:
  deprecation_notice_days: 90  # Customizable per doctype
```

---

## 📈 Success Criteria

**Living Documentation folder healthy when:**
- [ ] Templates używane w min. 3 kluczowych dokumentach (PRD, TDD, BUSINESS_CASE)
- [ ] Semantic versioning adopted (changelog z MAJOR/MINOR/PATCH)
- [ ] Min. 1 migration guide created (dla breaking change)
- [ ] Min. 1 retirement notice created (dla deprecated doc)
- [ ] Health checks manually performed co 2 tygodnie (Phase 1)
- [ ] Phase 2 automation planned (roadmap created)

**Current Status:**
- ✅ Templates created (6 plików, 75 KB)
- ✅ Phase 1 completed (2025-12-29)
- ⏳ Adoption pending (czeka na pierwsze użycie w projektach)
- ⏳ Phase 2 automation planned (Q1 2026)

---

## 📖 Zobacz też

### Related Templates

- **[../specs/specs_doc_types.md](../specs/specs_doc_types.md)** — Core specs extended with lifecycle_config
- **[../atomic/TODO-template.md](../atomic/TODO-template.md)** — Extended TODO template with lifecycle tracking
- **[../atomic/CHANGELOG-template.md](../atomic/CHANGELOG-template.md)** — Standard changelog (enhance with semantic versioning)

### Proposals

- **[../../proposals/PROPOZYCJA-2-Living-Documentation-Framework.md](../../proposals/PROPOZYCJA-2-Living-Documentation-Framework.md)** — Original proposal (33 KB, full specification)
- **[../../proposals/README.md](../../proposals/README.md)** — Implementation status, phases, roadmap

### External Resources

- [Keep a Changelog](https://keepachangelog.com/) — Changelog best practices
- [Semantic Versioning](https://semver.org/) — Versioning specification
- [Living Documentation (book)](https://www.amazon.com/Living-Documentation-Cyrille-Martraire/dp/0134689321) — Cyrille Martraire

---

**Wygenerowano:** 2025-12-29
**Kategoria:** Living Documentation (Framework)
**Status:** ✅ Phase 1 Complete, Ready for Use
**Next Phase:** Automation (Phase 2, planned Q1 2026)
