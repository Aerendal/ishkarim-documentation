# Operations — Deployment & Runtime Operations

## 📋 Przeznaczenie

Folder **operations/** zawiera **dokumenty fazy production** — deployment guide, contingency plans, monitoring, incident response. To warstwa "JAK wdrażamy i operujemy system w produkcji".

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Deployment** — Installation procedures, prerequisites, configuration
- **Contingency planning** — Risk mitigation, failure scenarios
- **Monitoring** — Performance metrics, health checks (future)
- **Incident response** — Runbooks, escalation paths (future)
- **Operations handover** — Dev → Ops transition (OPS-HANDOVER gate)

## 👥 Kto używa?

- **DevOps Engineers** — Deployment guide, infrastructure setup
- **SRE (Site Reliability Engineers)** — Monitoring, incident response
- **System Administrators** — Installation, configuration
- **Support Teams** — Troubleshooting, incident handling
- **Developers** — Contingency plans (when failures occur)

## ⏱️ Kiedy używać?

**Timing:** Faza **production** (post-implementation)

**Lifecycle Position:**
```
Pre-Production → Engineering → Implementation → Operations (YOU ARE HERE)
                                                  ↓
                                          Deployment → Monitoring → Incident Response
```

**Kiedy czytać:**
- **Pre-deployment** — Before first production rollout
- **Incident response** — When failures occur (CONTINGENCY-001)
- **Capacity planning** — Before scaling (future)
- **Maintenance windows** — Before upgrades, migrations

---

## 📂 Zawartość folderu (2 pliki)

### 1. deployment-guide.md 📝

**ID:** DEPLOY-GUIDE-001
**Status:** 📝 Draft (planned for post-implementation)
**Rozmiar:** ~300 lines

**Cel:** Step-by-step deployment procedures for MVP

**Struktura:**

**Prerequisites:**
- **OS:** Linux (Ubuntu 20.04+), macOS (11+), Windows 10+
- **Python:** 3.11+ (with pip, virtualenv)
- **RAM:** 4GB minimum, 8GB recommended
- **Disk:** 500MB for app + 10GB for workspace (depends on doc volume)
- **Dependencies:** Git (for version control), SQLite 3.35+ (bundled with Python)

**Installation Steps:**

1. **Install from PyPI** (when MVP released)
   ```bash
   pip install ishkarim-proof-system
   ```

2. **Initialize Workspace**
   ```bash
   ishkarim init /path/to/workspace
   # Creates:
   # - .ishkarim/ (config, SQLite DB)
   # - templates/ (document templates)
   # - README.md (workspace overview)
   ```

3. **Configuration**
   ```bash
   ishkarim config set workspace.path /path/to/docs
   ishkarim config set validator.strictMode true
   ishkarim config set graph.maxNodes 1000
   ```

4. **First Validation**
   ```bash
   ishkarim validate --workspace /path/to/docs
   # Output: Validation report (missing docs, broken refs, gate status)
   ```

5. **GUI Launch**
   ```bash
   ishkarim gui
   # Opens PySide6 application (document browser, graph viz)
   ```

**Deployment Scenarios:**

- **Local Development:** Single-user, local filesystem
- **Team Shared:** Network drive, multi-user (concurrency via file locks)
- **CI/CD Integration (future):** GitHub Actions workflow, automated validation on PR

**Troubleshooting:**
- **Issue:** `ishkarim: command not found`
  - **Fix:** Add `~/.local/bin` to PATH (Linux/macOS) or reinstall with `--user` flag
- **Issue:** GUI doesn't start (Qt platform error)
  - **Fix:** Install Qt dependencies (`sudo apt-get install libxcb-xinerama0`)

**Evidence:**
- E-155 (deployment sizing estimates)

### 2. CONTINGENCY-001-parser-failure.md 📝

**ID:** CONTINGENCY-001
**Status:** 📝 Draft (risk mitigation planned)
**Rozmiar:** ~200 lines

**Cel:** Contingency plan for Parser component failure

**Risk Scenario:**
- **Trigger:** Parser fails to read .md files (corrupted YAML, malformed markdown)
- **Impact:** HIGH (system can't load documents)
- **Likelihood:** MEDIUM (user-generated markdown may have errors)
- **Severity:** HIGH (impact × likelihood)

**Mitigation Strategy:**

**Pre-Deployment (Prevention):**
1. **Robust frontmatter parsing** (E-270 patterns)
   - Graceful degradation: Invalid YAML → warn, continue with defaults
   - Error recovery: Malformed markdown → partial parse, flag section

2. **Validation on file write** (future)
   - Pre-commit hook: Validate .md before git commit
   - IDE integration: Real-time frontmatter validation (Obsidian plugin)

**Runtime (Detection):**
1. **Error logging** (Structlog, ADR-009)
   - Log parser errors: `parser.error file=foo.md error="invalid YAML"`
   - Alert threshold: >5% parse failures → notify admin

2. **Health check endpoint** (future)
   - `/health`: Reports parser status, recent failures

**Post-Incident (Recovery):**
1. **Fallback mode:**
   - Parser failure → Document marked "unreadable"
   - GUI shows warning: "File foo.md unreadable (YAML error line 5)"
   - User can edit file, retry parse

2. **Manual intervention:**
   - Admin reviews error logs
   - Fixes malformed files (YAML linter, markdown validator)
   - Re-runs validation: `ishkarim validate --force-reparse`

3. **Escalation (if widespread):**
   - Contact development team (GitHub issue)
   - Provide: Error logs, sample malformed files
   - Workaround: Revert to last known-good workspace state (git revert)

**Success Criteria:**
- Parser handles 95%+ real-world .md files (E-098 metric)
- Errors logged with actionable context (file path, line number, error type)
- Users can recover without developer intervention (graceful degradation)

**Related Risks:**
- CONTINGENCY-002 (Validator failure) — planned
- CONTINGENCY-003 (Graph cycle deadlock) — planned

---

## 🔗 Powiązania (Cross-References)

### Dependencies (Co napędza te dokumenty)

**Deployment Guide REQUIRES:**
- `implementation/implementation-plan.md` — MVP complete (Week 12)
- `engineering/components/COMP-001-parser.md` — Parser deployment details
- `satellites/evidence/E-155-effort-estimation.md` — Deployment sizing

**Contingency Plans REQUIRE:**
- `satellites/evidence/E-092-risk-assessment.md` — Risks identified
- `engineering/components/COMP-001-parser.md` — Failure modes documented

### Impacts (Co te dokumenty popychają do przodu)

**Deployment Guide ENABLES:**
- Production rollout (users can install & use MVP)
- Operations handover (OPS-HANDOVER gate)

**Contingency Plans ENABLE:**
- Incident response (when failures occur)
- Risk mitigation (proactive prevention)

### Related Documents

- **[../implementation/implementation-plan.md](../implementation/implementation-plan.md)** — MVP delivery → deployment ready
- **[../engineering/components/](../engineering/components/)** — Component failure modes
- **[../satellites/evidence/E-092-risk-assessment.md](../satellites/evidence/E-092-risk-assessment.md)** — Risk register

---

## 📊 Statystyki

- **Liczba plików:** 2 (deployment guide + 1 contingency plan)
- **Status:** 📝 Draft (planned for post-MVP)
- **Contingency plans:** 1 (CONTINGENCY-001 Parser failure)
- **Planned:** CONTINGENCY-002 (Validator), CONTINGENCY-003 (Graph cycles)
- **Blockers:** Awaiting MVP delivery (implementation phase)

---

## 🚀 Quick Start — Typowy Workflow

### Scenario 1: First production deployment

**Czas:** 1h (installation + validation)

1. Read `deployment-guide.md` prerequisites
2. Install Ishkarim: `pip install ishkarim-proof-system`
3. Initialize workspace: `ishkarim init /path/to/docs`
4. Configure settings: `ishkarim config set ...`
5. Run validation: `ishkarim validate`
6. Launch GUI: `ishkarim gui`

**Output:** System deployed, workspace validated, users can start working

### Scenario 2: Parser failure incident

**Czas:** 30 min (incident response)

1. **Detection:** User reports "Document XYZ unreadable"
2. **Triage:** Check logs (`ishkarim logs --component parser`)
3. **Reference:** Open `CONTINGENCY-001-parser-failure.md`
4. **Mitigation:** Follow recovery steps (fix YAML, retry parse)
5. **Escalation:** If widespread, contact dev team (GitHub issue)

**Output:** Incident resolved, user unblocked, root cause identified

### Scenario 3: Capacity planning

**Czas:** 2h (sizing analysis)

1. Review `deployment-guide.md` prerequisites (RAM, disk)
2. Estimate doc volume (e.g., 1000 docs × 50KB avg = 50MB)
3. SQLite sizing (metadata ~10% of filesystem = 5MB)
4. Graph rendering (1000 nodes → ~2s load per E-143)
5. Scale up if needed (8GB RAM recommended for >500 docs)

**Output:** Capacity plan, infrastructure provisioned

---

## ⚠️ Uwagi

### Deployment readiness

**Operations folder is INCOMPLETE** until:
- [ ] MVP delivered (implementation phase complete)
- [ ] Deployment guide tested (QA validation)
- [ ] Contingency plans for all critical components (currently 1/6)
- [ ] Monitoring setup (future: Prometheus, Grafana)

**Current status:** 📝 **Planned** (awaiting MVP delivery)

### Contingency coverage

**Currently:** 1 contingency plan (CONTINGENCY-001 Parser)
**Needed:** 5 more (Validator, Graph, GUI, Viz, Storage)

**Priority order:**
1. CONTINGENCY-001 (Parser) ✅ — Drafted
2. CONTINGENCY-002 (Validator) — Next (highest impact)
3. CONTINGENCY-003 (Graph cycles) — Next (deadlock risk)
4. CONTINGENCY-004 (GUI crash) — Lower priority
5. CONTINGENCY-005 (Viz performance) — Lower priority
6. CONTINGENCY-006 (Storage corruption) — Critical (future)

### Local-first constraints

**Deployment simplified** by local-first architecture (ADR-003):
- ❌ No cloud infrastructure (no AWS, Azure, GCP setup)
- ❌ No authentication/authorization (single-user or network file share)
- ❌ No database server (SQLite embedded)
- ✅ Simple installation (PyPI package, single command)

**Future (cloud sync):**
- Phase 4: Optional cloud sync (not MVP)
- Would require: Cloud deployment guide, auth setup, sync conflict resolution

---

## 📈 Success Criteria

**Operations phase complete when:**
- [ ] Deployment guide tested (QA verified installation)
- [ ] MVP deployed to first production environment
- [ ] All 6 contingency plans documented
- [ ] Monitoring setup (health checks, error alerting)
- [ ] Operations handover complete (OPS-HANDOVER gate passed)
- [ ] Runbooks for common incidents

**Status:** ⏳ **Planned** (0% complete, awaiting MVP)

---

## 📖 Zobacz też

### Upstream (Dependencies)

- **[../implementation/](../implementation/)** — MVP delivery enables deployment
- **[../engineering/components/](../engineering/components/)** — Component specs → failure modes

### Downstream (Impacts)

- Production users (when deployed)
- Support teams (runbooks, contingency plans)

### Related

- **[../dependency_graph.md](../dependency_graph.md)** — Graf D: Operations Dependencies
- **[../satellites/evidence/E-092-risk-assessment.md](../satellites/evidence/E-092-risk-assessment.md)** — Risk register
- **[../templates/produkcyjna/](../templates/produkcyjna/)** — Deployment, runbook templates

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Operations (Production Phase)
**Status:** ⏳ Planned (awaiting MVP delivery)
**Critical:** Deployment guide + 6 contingency plans needed before production rollout
