# CONCEPT-BRANCH: CB-001 - WebSocket-based Real-time Collaboration

---

## Document Metadata

```yaml
id: CONCEPT-BRANCH-001
doctype: CONCEPT-BRANCH
status: merged
version: 2.0
created: 2026-05-01
updated: 2026-06-15
owner: Tomasz Nowicki
project: Ishkarim Document Management System
parent_concept: HYPOTHESIS-005-realtime-collaboration
branch_id: websocket-approach
```

---

## Cross-References

```yaml
dependencies:
  - id: HYPOTHESIS-005
    type: requires
    reason: "Branch powstaje z parent hipotezy o real-time collaboration"

impacts:
  - id: RESEARCH-FINDINGS-002
    type: influences
    reason: "Wyniki z tej branchy będą porównane z CRDT branch i zagregowane"
  - id: ADR-048
    type: blocks
    reason: "Decyzja merge/kill wymaga ADR po porównaniu z parallel branch"
```

---

## SEC-CB-DIVERGENCE: Punkt rozwidlenia (fork point)

### Parent Concept

**ID:** HYPOTHESIS-005
**Title:** Real-time Collaborative Document Editing dla Ishkarim
**Link:** [HYPOTHESIS-005-realtime-collaboration.md](../hypotheses/HYPOTHESIS-005-realtime-collaboration.md)

**Parent hypothesis:**
"Implementacja real-time collaborative editing zwiększy user engagement o 40% i unlock enterprise team workflows (5+ concurrent editors)."

### Fork Point

**Date:** 2026-05-01
**Version of parent:** 1.0 (approved)
**State at fork:** Hypothesis approved, approach undefined

**Divergence reason:**
Parent hypothesis definiowała **CO** (real-time collab) ale nie **JAK** (implementation approach). Team zidentyfikował 2 fundamentally different architectural approaches wymagające parallel exploration.

### Triggering Event

**Kick-off meeting 2026-04-28:**
- Team debated: Operational Transformation (OT) vs CRDT vs WebSocket + locking
- No consensus - każde podejście ma pros/cons
- **Decision:** Split into 2 parallel branches (2 teams, 4 weeks, compare results)
  - **Branch A (this document):** WebSocket + operational locking (Tomasz's team)
  - **Branch B:** CRDT-based (Yjs library) (Kasia's team)

### Alternative Question

**Parent question:** "Czy real-time collab zwiększy engagement?"
**Branch A question:** "Czy WebSocket + locking approach jest implementable, performant, i user-friendly dla Ishkarim use case?"

---

## SEC-CB-RATIONALE: Dlaczego nowa gałąź

### Problem with Parent Approach

Parent hypothesis nie określała implementation approach - intentionally open-ended. Jednak przed implementation musimy choose approach.

**Trade-off space:**
- **Simplicity vs Robustness:** Simple locking vs complex CRDT
- **Latency vs Consistency:** Eventual consistency (CRDT) vs immediate locks (WebSocket)
- **Implementation effort:** Locking (2-3 weeks) vs CRDT integration (4-5 weeks)

**Problem:** Nie możemy decide bez prototyping obu approaches - unknown unknowns.

### Opportunity Identified

**WebSocket + Locking approach (this branch) offers:**
- **Simplicity:** Straightforward to implement (WebSocket bidirectional communication + document locks)
- **Immediate feedback:** User sees lock immediately when someone else edits
- **Familiar UX pattern:** Google Docs-like (section locking) - proven user acceptance
- **Lower risk:** Team has WebSocket experience (used w notification system)

**Potential advantages vs CRDT:**
- Faster time-to-market (simpler implementation)
- Lower cognitive complexity (easier dla team to maintain)
- Predictable behavior (explicit locks vs eventual consistency)

### Hypothesis for Branch

**H0 (CRDT approach - Branch B):**
CRDT-based approach (Yjs library) delivers superior user experience through conflict-free merging, despite implementation complexity.

**H1 (WebSocket + locking - this branch):**
WebSocket + locking approach delivers acceptable user experience z 50% less implementation complexity, making it better choice for MVP.

### Success Criteria for Branch

- [x] **Performance:** <100ms lock acquisition latency ✅ Achieved 45ms
- [x] **User Experience:** Users understand lock UX (tested w prototype) ✅ 90% comprehension
- [x] **Reliability:** Handle edge cases (network disconnect, crash) ✅ Tested 15 scenarios
- [x] **Implementation:** Prototype w 3 weeks (vs 5 weeks CRDT) ✅ Completed 2.5 weeks
- [x] **Scalability:** Support 10 concurrent editors ✅ Tested @ 15 editors

### Resources Allocated

- **Team:** 2 developers (Tomasz, Michał) - 100% for 4 weeks
- **Budget:** $16,000 (team time) + $500 (infrastructure dla testing)
- **Timeline:** 2026-05-01 to 2026-06-01 (4 weeks prototyping + 2 weeks comparison)

---

## SEC-CB-APPROACH: Alternatywne podejście

### Key Differences from Parent

| Aspect | Parent Concept | This Branch (WebSocket) | Branch B (CRDT) |
|--------|----------------|------------------------|----------------|
| **Conflict Resolution** | Undefined | Explicit locks (pessimistic) | Automatic merge (optimistic) |
| **Architecture** | Undefined | WebSocket server + lock manager | CRDT library (Yjs) + WebRTC |
| **User Experience** | Undefined | Lock indicators, "User X editing" | Seamless multi-cursor, auto-merge |
| **Complexity** | Undefined | Low (straightforward) | High (CRDT algorithms) |
| **Implementation Time** | 6-8 weeks (est) | 3 weeks (prototype) | 5 weeks (prototype) |

### Technical Approach

**Architecture:**
```
┌─────────────────────────────────────────────┐
│         Client (Browser)                     │
│  ┌────────────────────────────────────┐     │
│  │  React Editor Component             │     │
│  │  - WebSocket client                 │     │
│  │  - Lock UI indicators               │     │
│  └────────────────┬───────────────────┘     │
└───────────────────┼─────────────────────────┘
                    │ WebSocket connection
                    ▼
┌─────────────────────────────────────────────┐
│     WebSocket Server (Node.js)              │
│  ┌────────────────────────────────────┐     │
│  │  Lock Manager (in-memory)           │     │
│  │  - Document locks (per section)     │     │
│  │  - User sessions                     │     │
│  └────────────────┬───────────────────┘     │
└───────────────────┼─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│       MongoDB (Document Storage)            │
│  - Persist lock state (recovery)            │
│  - Store document versions                  │
└─────────────────────────────────────────────┘
```

**Locking Strategy:**
- **Granularity:** Section-level (H1, H2 headers = lock boundaries)
- **Acquisition:** First-come-first-served (FIFO queue)
- **Timeout:** Auto-release after 5 min inactivity
- **Visual:** Highlighted borders + "Locked by User X" tooltip

### Methodology

**Week 1: Core Infrastructure**
- Setup WebSocket server (Socket.io)
- Implement basic lock manager (acquire, release, query)
- Client-server lock protocol

**Week 2: Editor Integration**
- Integrate locks z Markdown editor (CodeMirror)
- UI indicators (locked sections highlighted)
- User presence (avatars, "User X editing Section Y")

**Week 3: Edge Cases & Testing**
- Network disconnect recovery (release locks on disconnect)
- Crash recovery (persistent lock state w MongoDB)
- Conflict scenarios testing (15 edge cases)

**Week 4: User Testing & Comparison**
- Internal dogfooding (10 users, real documents)
- Comparison z Branch B (CRDT approach)
- Performance benchmarking

### Scope of Exploration

**In scope:**
- Document locking (section-level granularity)
- Real-time presence (who's editing where)
- Lock conflict UX (queue, timeout, manual release)
- Network resilience (reconnection, lock recovery)

**Out of scope:**
- Offline editing (requires CRDT - out of MVP)
- Mobile app support (web-only dla prototype)
- Advanced features (commenting, suggestions) - future

---

## SEC-CB-PROGRESS: Progress tracking

### Timeline

| Phase | Start | End | Status | Notes |
|-------|-------|-----|--------|-------|
| Infrastructure | 2026-05-01 | 2026-05-07 | ✅ Complete | Socket.io setup, lock manager v1 |
| Editor Integration | 2026-05-08 | 2026-05-14 | ✅ Complete | CodeMirror locks, UI indicators |
| Edge Cases | 2026-05-15 | 2026-05-21 | ✅ Complete | 15/15 scenarios handled |
| User Testing | 2026-05-22 | 2026-05-28 | ✅ Complete | 10 users tested, positive feedback |
| Comparison | 2026-05-29 | 2026-06-15 | ✅ Complete | vs CRDT branch, decision: MERGE |

### Milestones

- [x] **2026-05-07**: WebSocket server operational - ✅ Locks working
- [x] **2026-05-14**: Prototype demo-able - ✅ Internal demo successful
- [x] **2026-05-21**: Edge cases handled - ✅ Crash recovery tested
- [x] **2026-05-28**: User testing complete - ✅ 90% satisfaction
- [x] **2026-06-15**: Final decision - ✅ **MERGED into main**

### Key Deliverables

- [x] **WebSocket Lock Server**: [GitHub repo](https://github.com/ishkarim/collab-websocket) - 1,200 LOC ✅
- [x] **Client Lock UI**: React components - 800 LOC ✅
- [x] **Test Suite**: 45 integration tests ✅
- [x] **User Testing Report**: [Document](../testing/collab-websocket-user-testing.md) ✅

### Current Status Summary

**As of 2026-06-15:** Branch **MERGED** into main concept.

WebSocket approach won comparison z CRDT branch:
- **Implementation time:** 2.5 weeks vs 5 weeks (CRDT)
- **User comprehension:** 90% vs 65% (CRDT confusion about auto-merge)
- **Performance:** 45ms lock latency (excellent)
- **Maintenance:** Simpler codebase (team confidence high)

### Blockers

**Historical blockers (resolved):**
- **Week 2:** CodeMirror integration tricky (lock boundaries ≠ line numbers)
  - **Resolution:** Custom parser dla Markdown sections (H1/H2 headers)
- **Week 3:** Network disconnect → ghost locks (users couldn't edit)
  - **Resolution:** Heartbeat protocol (30s ping, auto-release if missed 2x)

---

## SEC-CB-LEARNINGS: Learnings vs parent branch

### What Works Better

✅ **User Comprehension:**
- **Parent (undefined):** No UX guidance
- **This branch (WebSocket locks):** 90% users understood lock indicators immediately
- **Improvement:** Clear UX paradigm (locks familiar from Google Docs)

✅ **Implementation Speed:**
- **Parent estimate:** 6-8 weeks
- **This branch:** 2.5 weeks actual (63% faster)
- **Improvement:** Simplicity paid off - no complex CRDT algorithms

✅ **Debugging & Maintenance:**
- **Parent (undefined):** Assumed complex
- **This branch:** WebSocket logs straightforward, lock state inspectable
- **Improvement:** Operational simplicity - DevOps team comfortable

### What Works Worse

❌ **Offline Editing:**
- **Parent expectation:** Support offline (nice-to-have)
- **This branch:** Impossible z locking approach (requires server connection)
- **Degradation:** Limitation accepted (MVP scope - web-only, online required)

**Note:** CRDT branch supports offline, but adds significant complexity.

### Trade-offs Identified

⚖️ **Trade-off 1: Simplicity vs Offline Support**
- **Gain:** Simple implementation, fast delivery (2.5 weeks)
- **Loss:** No offline editing capability
- **Worth it?:** **YES** - offline editing not critical dla MVP (95% users online during editing)

⚖️ **Trade-off 2: Explicit Locks vs Seamless Multi-cursor**
- **Gain:** Clear conflict prevention (users see locks)
- **Loss:** Less "magic" UX (CRDT auto-merge feels seamless)
- **Worth it?:** **YES** - clarity > magic (users prefer predictability)

### Surprising Discoveries

💡 **Discovery 1: Users PREFER explicit locks**
- **Expectation:** Users would want seamless auto-merge (CRDT)
- **Reality:** 80% users preferred seeing locks ("I know someone's editing, won't conflict")
- **Insight:** Transparency > convenience dla collaborative editing

💡 **Discovery 2: Section-level locking perfect granularity**
- **Concern:** Too coarse (whole section locked)?
- **Reality:** Perfect - users edit different sections 90% of time, conflicts rare
- **Insight:** H1/H2 sections natural edit boundaries

### Comparative Metrics

| Metric | CRDT Branch (B) | WebSocket Branch (A - this) | Delta |
|--------|------------|-------------|-------|
| Implementation time | 5 weeks | 2.5 weeks | **-50%** ✅ |
| User comprehension | 65% (confused by auto-merge) | 90% (locks clear) | **+38%** ✅ |
| Lock latency | N/A (no locks) | 45ms | N/A |
| Merge conflicts | 0% (auto-resolved) | 2% (rare overlaps) | +2% ⚠️ |
| Offline support | ✅ Yes | ❌ No | Limitation |
| Code complexity (LOC) | 3,200 LOC | 2,000 LOC | **-37%** ✅ |

**Overall performance vs CRDT:** **WebSocket wins on simplicity, speed, user clarity**

---

## SEC-CB-DECISION: Merge/Kill/Continue decision

### Current Recommendation: **MERGE** ✅

---

### Decision Rationale

#### Why MERGE:

**Wyniki przekonujące:**
1. **User testing success:** 90% comprehension, 85% satisfaction (vs CRDT 65%/70%)
2. **Implementation speed:** 2.5 weeks vs 5 weeks CRDT (50% faster time-to-market)
3. **Maintenance simplicity:** 2,000 LOC vs 3,200 LOC CRDT (37% less code)
4. **Performance met:** 45ms lock latency (target <100ms)

**Trade-offs acceptable:**
- Offline editing limitation OK (MVP scope, 95% users online)
- 2% conflict rate acceptable (rare edge case, manual resolution works)

**Strategic fit:**
- Aligns z "ship fast, iterate" philosophy
- Team confidence high (WebSocket familiar tech)
- Lower risk dla production deployment

### What to merge

**Components merging into main:**
1. **WebSocket Lock Server:** Production-ready, deploy as new service
2. **Client Lock UI:** React components integrate w existing editor
3. **Lock Manager:** MongoDB persistence for crash recovery
4. **Monitoring:** Datadog dashboards dla lock metrics (acquisition time, queue length)

**From CRDT branch (Branch B) - preserve learnings:**
- **Documentation:** CRDT research notes (future reference - offline editing)
- **Benchmarks:** Performance data (compare if revisit later)

### What to discard from parent

**Parent concept assumptions discarded:**
- Assumption: "Need complex CRDT dla good UX" → FALSE (simple locks work)
- Assumption: "Offline editing critical" → FALSE (nice-to-have, not MVP)

### Merge strategy

**Technical approach:**

**Phase 1: Infrastructure (Week 1-2):**
1. Deploy WebSocket server (Socket.io) production cluster (3 nodes, load balanced)
2. MongoDB lock collection setup (indices, TTL for timeouts)
3. Monitoring & alerting (Datadog integration)

**Phase 2: Client Integration (Week 3-4):**
1. Merge lock UI components do main React app
2. Feature flag: `realtime_collab_enabled` (gradual rollout)
3. A/B test: 10% users enabled first week

**Phase 3: Rollout (Week 5-8):**
1. Week 5: 25% users
2. Week 6: 50% users
3. Week 7: 75% users
4. Week 8: 100% users (full rollout)

**Rollback plan:**
- Feature flag disable → instant rollback
- WebSocket server independent (can shutdown без affecting non-collab users)

### Timeline for merge

**Milestones:**
- [x] **2026-06-15**: Merge decision approved ✅
- [ ] **2026-06-20**: Production infrastructure deployed (Week 1)
- [ ] **2026-06-27**: Client integration complete (Week 2)
- [ ] **2026-07-04**: A/B test started (10% users) (Week 3)
- [ ] **2026-08-01**: Full rollout complete (Week 8)

**Target:** Production real-time collab by **August 1, 2026** 🎯

### Risks of merge

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| WebSocket server scalability issues | Medium | High | Load testing 100+ concurrent sessions przed rollout |
| Lock deadlocks (bug scenario) | Low | Medium | Admin "force release all locks" tool |
| User confusion (lock UX) | Low | Low | In-app tooltips, help documentation |
| Network instability → UX degradation | Medium | Medium | Graceful degradation (read-only mode if WS offline) |

---

### Stakeholder Input

| Stakeholder | Role | Position | Rationale |
|------------|------|----------|-----------|
| Anna Nowak | Product Owner | **MERGE** | User testing clear - locks UX wins, ship faster |
| Piotr Zieliński | Engineering Lead | **MERGE** | Simplicity advantage, team can maintain confidently |
| Kasia Wiśniewska | CRDT Branch Lead | **MERGE (WebSocket)** | Honest assessment - CRDT overengineered dla MVP |
| Marek Wiśniewski | CTO | **MERGE** | ROI clear - 50% faster delivery, lower risk |

**Consensus:** **UNANIMOUS MERGE** 🎉

### Final Decision

**Made by:** Marek Wiśniewski (CTO)
**Date:** 2026-06-15
**Decision:** **MERGE WebSocket approach into production**

**Quote:**
> "Both branches delivered valuable insights. CRDT proved too complex dla MVP. WebSocket wins on simplicity, speed, user clarity. Ship it. We can revisit CRDT later if offline editing becomes critical."

---

## Next Actions

### Immediate Actions

- [x] **2026-06-15**: Merge decision communicated do teams ✅
- [ ] **2026-06-17**: Kick off production deployment (TDD-COLLAB-WEBSOCKET)
- [ ] **2026-06-18**: Create ADR-048: "Real-time Collaboration via WebSocket Locks"
- [ ] **2026-06-20**: Infrastructure deployed (WebSocket cluster)

### Documentation Updates

- [ ] **Create ADR-048**: Document decision WebSocket vs CRDT
  - Context: Parallel branches comparison
  - Decision: WebSocket locks dla MVP
  - Consequences: No offline editing (acceptable trade-off)

- [ ] **Update PRD-V3**: Add real-time collaboration feature spec
  - Lock UX guidelines
  - Conflict resolution flows
  - Performance SLAs (<100ms lock latency)

- [ ] **Archive CRDT Branch research**: Preserve learnings dla future
  - Document: "CRDT Research - Offline Editing Future"
  - Status: Shelved (revisit if offline becomes priority)

### Follow-up Work Items

- [ ] **TASK-301**: Production WebSocket server deployment (2 weeks, $8K)
- [ ] **TASK-302**: Client lock UI integration (2 weeks, $8K)
- [ ] **TASK-303**: Load testing (100 concurrent users) (1 week, $3K)
- [ ] **TASK-304**: Monitoring & alerting setup (3 days, $2K)
- [ ] **TASK-305**: Documentation (user help, API docs) (1 week, $4K)

**Total effort estimate:** 8 tygodni, $25K (production-ready)

---

## Artifacts from Branch

### Code/Prototypes

**Repository:** https://github.com/ishkarim/collab-websocket
**Branch:** `main` (merged from `prototype`)
**Key commits:**
- `a7f2c45`: WebSocket lock server initial implementation
- `b8e3d56`: Client lock UI components
- `c9f4e67`: Crash recovery (persistent locks)
- `d1a5f78`: User testing feedback incorporated

**Lines of Code:**
- Server: 1,200 LOC (Node.js + Socket.io)
- Client: 800 LOC (React + CodeMirror integration)
- Tests: 45 integration tests (Jest + Puppeteer)

### Documents Produced

- **User Testing Report:** [collab-websocket-user-testing.md](../testing/collab-websocket-user-testing.md)
- **Performance Benchmarks:** [collab-websocket-benchmarks.md](../benchmarks/collab-websocket-benchmarks.md)
- **Comparison Analysis:** [websocket-vs-crdt.md](../analysis/websocket-vs-crdt.md)

### Data/Metrics

- **User testing data:** 10 users, 50 editing sessions, satisfaction scores
- **Performance metrics:** Lock latency distribution (p50, p95, p99)
- **Edge case testing:** 15 scenarios (network disconnect, crashes, race conditions)

### Presentations

- **Team demo (2026-05-14):** [Recording](https://recordings.ishkarim.com/collab-websocket-demo)
- **Stakeholder comparison (2026-06-10):** [Slides](../presentations/websocket-vs-crdt-comparison.pdf)

---

## TODO_SECTION: Zadania dla tej gałęzi

### Zrealizowane

- [x] Setup WebSocket server (Socket.io) (2026-05-02)
- [x] Implement lock manager (acquire, release, query) (2026-05-05)
- [x] Client-server lock protocol (2026-05-07)
- [x] CodeMirror lock integration (2026-05-10)
- [x] UI indicators (locked sections, user presence) (2026-05-14)
- [x] Network disconnect recovery (2026-05-17)
- [x] Crash recovery (persistent locks MongoDB) (2026-05-20)
- [x] Edge cases testing (15 scenarios) (2026-05-21)
- [x] User testing (10 users) (2026-05-28)
- [x] Comparison z CRDT branch (2026-06-10)
- [x] Merge decision (2026-06-15)

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| 2026-05-01 | 1.0 | Tomasz Nowicki | Branch forked from parent, WebSocket approach defined |
| 2026-05-14 | 1.2 | Tomasz Nowicki | Prototype complete, internal demo |
| 2026-05-28 | 1.5 | Tomasz Nowicki | User testing complete, positive results |
| 2026-06-10 | 1.8 | Tomasz Nowicki | Comparison z CRDT complete, WebSocket wins |
| 2026-06-15 | 2.0 | Tomasz Nowicki | Final decision: MERGE, approved by CTO |

---

## Notatki i uwagi

### Refleksje - Dlaczego WebSocket wygrało z CRDT

**Technical reasons:**
1. **Simplicity:** 2,000 LOC vs 3,200 LOC - 37% less code to maintain
2. **Team expertise:** WebSocket familiar (notifications system), CRDT new territory
3. **Debuggability:** Lock state inspectable (MongoDB), CRDT state opaque (complex merges)

**User experience reasons:**
1. **Clarity:** Users understand locks ("User X editing") > confusion auto-merge behavior
2. **Predictability:** Explicit conflicts > mysterious merge results
3. **Trust:** Visible locks build confidence > invisible CRDT magic

**Business reasons:**
1. **Time-to-market:** 2.5 weeks vs 5 weeks - 10 weeks faster to production
2. **Risk:** Lower (simpler tech) vs higher (complex CRDT algorithms)
3. **ROI:** Deliver value sooner (Q3 2026 vs Q4 2026)

### Lessons Learned - Parallel Branches Value

**What parallel exploration delivered:**
- **Data-driven decision:** Not speculation - actual prototypes compared
- **Risk mitigation:** Validated assumptions (CRDT complexity not worth it)
- **Team learning:** Both teams learned new tech (WebSocket + CRDT knowledge retained)
- **Faster iteration:** 4 weeks parallel vs 9 weeks sequential (CRDT then WebSocket if fail)

**Cost:** 2 teams × 4 weeks = 8 team-weeks = $32K
**Value:** Saved 5 weeks sequential trial-and-error + high-confidence decision
**ROI:** **Positive** - faster time to production + lower risk

### Future Considerations - When to Revisit CRDT

**CRDT approach (Branch B) might win if:**
- Offline editing becomes critical (mobile app, poor connectivity users)
- Concurrent editing frequency 10x increases (>50 concurrent editors)
- User feedback shifts ("we want seamless auto-merge like Google Docs")

**Trigger for reconsideration:**
- User complaints about locks >10% monthly active users
- Customer churn due to lack of offline editing
- Competitive pressure (competitors ship superior CRDT-based collab)

**Preserved assets:**
- CRDT research documentation archived
- Yjs library evaluation documented
- Can pivot in Q4 2026 or 2027 if needed

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation-management
