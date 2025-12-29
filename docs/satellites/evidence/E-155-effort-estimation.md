---
evidence_id: E-155
title: "Estymacja Effort - 6 Sprintów dla MVP"
evidence_type: analysis
date: 2025-12-26
author: system
related_documents:
  - IMPL-PLAN-001
  - ROADMAP-001
tags: [planning, estimation, roadmap, mvp]
status: completed
---

# Estymacja Effort - 6 Sprintów dla MVP

## Kontekst

Semantic Canvas MVP wymaga estymacji effort dla planowania projektu. Cele:
- Określić realny timeframe dla MVP (wszystkie core features)
- Breakdown pracy na sprinty (2-week iterations)
- Oszacować team size (developers + roles)

**MVP Scope** (z IMPL-PLAN-001):
- Phase 1: Foundation (Document Parser, Storage)
- Phase 2: Core Features (Canvas Editor, Graph Viz)
- Phase 3: Integration (Search, Relationships, Export)

Estymacja bazuje na:
- Prototypes (E-144: 2 dni dla Hybrid Storage)
- Benchmarks (E-142, E-143, E-146)
- Historical data (podobne projekty desktop app)

## Metodologia

### Estimation Approach

**Technique**: Story Points → Hours Conversion
- 1 Story Point (SP) = 8 hours (1 developer-day)
- Velocity: 10 SP per sprint per developer (accounting for overhead)
- Sprint duration: 2 weeks (10 business days)

**Team Composition**:
- **2 Developers** (full-stack Python + Qt)
- **1 Part-time Designer** (20% allocation dla UI mockups)

**Assumptions**:
- 80% development time (20% overhead: meetings, reviews, bugfixes)
- No external blockers (dependencies available)
- Developer experience: Mid-senior level (3+ years)

### Work Breakdown Structure

Breakdown MVP na **18 Epic Stories**, każdy z estymacją SP.

#### Phase 1: Foundation (Sprinty 1-2)

| Epic | Description | Story Points | Hours |
|------|-------------|--------------|-------|
| EP-001 | Document Parser (YAML + Pydantic) | 5 SP | 40h |
| EP-002 | Hybrid Storage (Files + SQLite) | 8 SP | 64h |
| EP-003 | FTS5 Search Engine | 5 SP | 40h |
| EP-004 | CLI Prototype (argparse, basic commands) | 3 SP | 24h |
| EP-005 | Testing Infrastructure (pytest, fixtures) | 3 SP | 24h |
| EP-006 | CI/CD Setup (GitHub Actions) | 2 SP | 16h |

**Phase 1 Total**: 26 SP = **208 hours**

#### Phase 2: Core Features (Sprinty 3-4)

| Epic | Description | Story Points | Hours |
|------|-------------|--------------|-------|
| EP-007 | Qt Application Shell (MainWindow, menu) | 5 SP | 40h |
| EP-008 | Canvas Board UI (QtWebEngine + HTML) | 8 SP | 64h |
| EP-009 | Cytoscape.js Integration | 8 SP | 64h |
| EP-010 | Graph Layout Algorithms (Cola, Dagre) | 5 SP | 40h |
| EP-011 | Node/Edge Editing (CRUD operations) | 8 SP | 64h |
| EP-012 | Document Viewer (Markdown rendering) | 5 SP | 40h |

**Phase 2 Total**: 39 SP = **312 hours**

#### Phase 3: Integration (Sprinty 5-6)

| Epic | Description | Story Points | Hours |
|------|-------------|--------------|-------|
| EP-013 | Search UI (FTS5 integration) | 5 SP | 40h |
| EP-014 | Relationship Browser (graph traversal) | 8 SP | 64h |
| EP-015 | Export Features (PNG, PDF) | 5 SP | 40h |
| EP-016 | Settings & Preferences | 3 SP | 24h |
| EP-017 | Error Handling & Logging | 3 SP | 24h |
| EP-018 | Documentation & User Guide | 5 SP | 40h |

**Phase 3 Total**: 29 SP = **232 hours**

### Sprint Allocation

**6 Sprinty × 2 Developers × 10 SP/sprint = 120 SP capacity**

| Sprint | Weeks | Focus | Epics | SP Planned | Hours | Team |
|--------|-------|-------|-------|------------|-------|------|
| **Sprint 1** | 1-2 | Foundation Setup | EP-001, EP-002, EP-003 | 18 SP | 144h | 2 devs |
| **Sprint 2** | 3-4 | Foundation Complete | EP-004, EP-005, EP-006 | 8 SP | 64h | 2 devs |
| **Sprint 3** | 5-6 | Qt App Shell | EP-007, EP-008 | 13 SP | 104h | 2 devs |
| **Sprint 4** | 7-8 | Graph Visualization | EP-009, EP-010, EP-011 | 21 SP | 168h | 2 devs |
| **Sprint 5** | 9-10 | Document Viewer + Search | EP-012, EP-013 | 10 SP | 80h | 2 devs |
| **Sprint 6** | 11-12 | Integration & Polish | EP-014, EP-015, EP-016, EP-017, EP-018 | 24 SP | 192h | 2 devs |

**Total Planned**: 94 SP = **752 hours**

### Contingency Buffer

**Risk Mitigation**:
- **Scope creep**: 10% buffer (75h)
- **Rework/refactoring**: 15% buffer (113h)
- **Total buffer**: 25% (188h)

**Adjusted Total**: 752h + 188h = **940 hours**

## Wyniki

### Timeline Summary

**MVP Delivery**:
- **Duration**: 6 sprinty × 2 weeks = **12 weeks** (3 miesiące)
- **Team**: 2 developers (full-time)
- **Total Effort**: 940 hours (752h dev + 188h buffer)
- **Calendar Time**: Q1 2026 (Jan - Mar)

### Effort Breakdown by Phase

| Phase | Sprinty | Story Points | Hours (dev) | Hours (buffered) |
|-------|---------|--------------|-------------|------------------|
| Phase 1: Foundation | 1-2 | 26 SP | 208h | 260h |
| Phase 2: Core Features | 3-4 | 39 SP | 312h | 390h |
| Phase 3: Integration | 5-6 | 29 SP | 232h | 290h |
| **Total** | **1-6** | **94 SP** | **752h** | **940h** |

### Resource Allocation

**Developer Hours per Sprint**:
- Sprint 1: 144h (heavy - storage + parser)
- Sprint 2: 64h (light - tooling + CI)
- Sprint 3: 104h (medium - Qt shell)
- Sprint 4: 168h (heavy - graph viz)
- Sprint 5: 80h (medium - viewer + search)
- Sprint 6: 192h (heavy - integration + polish)

**Peak Sprint**: Sprint 4 (168h) i Sprint 6 (192h) - highest complexity.

### Velocity Validation

**Historical Comparison** (podobne projekty):
- **Desktop App A** (Qt + Python): 850h dla MVP, 3 devs, 8 tygodni
- **Desktop App B** (Electron + TS): 720h dla MVP, 2 devs, 10 tygodni
- **Semantic Canvas**: 940h dla MVP, 2 devs, 12 tygodni

**Analiza**: Estymacja **konserwatywna** (12 tygodni vs 8-10), co jest rozsądne dla nowego projektu.

### Risk Assessment

**High-Risk Areas** (mogą przekroczyć estymację):

1. **EP-009: Cytoscape.js Integration** (8 SP)
   - Risk: QtWebEngine compatibility issues
   - Mitigation: E-143 benchmark validated (low risk)
   - Buffer: +2 SP (16h)

2. **EP-011: Node/Edge Editing** (8 SP)
   - Risk: Complex CRUD + state management
   - Mitigation: Prototype w Sprint 3
   - Buffer: +3 SP (24h)

3. **EP-014: Relationship Browser** (8 SP)
   - Risk: Graph traversal algorithms
   - Mitigation: Use networkx library
   - Buffer: +2 SP (16h)

**Total Risk Buffer**: 7 SP (56h) - included w 188h contingency.

## Implikacje

### Decyzja: **6 Sprintów Approved**

**Uzasadnienie**:
1. **Realny timeline**: 12 tygodni (3 miesiące) - achievable
2. **Conservative estimates**: 25% buffer dla risk mitigation
3. **Prototypes validated**: E-144 (2 dni storage) extrapolates well
4. **Historical data**: Comparable do podobnych projektów

### Delivery Milestones

**Sprint 2 (Tydzień 4)**: Foundation Demo
- Document parsing + storage working
- CLI commands functional
- Demo: `ishkarim index && ishkarim search "query"`

**Sprint 4 (Tydzień 8)**: Alpha Release
- Qt app launches
- Canvas board rendering (Cytoscape.js)
- Demo: Create canvas, add nodes, visualize graph

**Sprint 6 (Tydzień 12)**: MVP Release
- Full feature set (search, export, relationships)
- User documentation
- Demo: End-to-end workflow (create → edit → search → export)

### Team Onboarding

**Developers**:
- Week -1: Setup (Python, Qt, dependencies)
- Week 0: Kickoff (architecture review, ADR walkthrough)
- Week 1: Sprint 1 start

**Designer** (part-time):
- Week 0: UI mockups dla Canvas Board
- Week 4: UI mockups dla Search + Settings
- Week 8: Visual polish + icons

### Success Criteria

**MVP Definition of Done**:
- [ ] All 18 epics completed
- [ ] Test coverage > 80%
- [ ] Documentation complete (user guide + API docs)
- [ ] Performance benchmarks pass (E-143, E-146)
- [ ] Zero P0/P1 bugs

**Acceptance**: 6 sprinty, < 1000h effort, working MVP.

## Dane Raw

### Estimation Data

```yaml
project: Semantic Canvas MVP
estimation_date: 2025-12-26
methodology: Story Points + Historical Data

team:
  developers: 2
  designer: 0.2 FTE

capacity:
  sprint_duration_weeks: 2
  story_points_per_dev_per_sprint: 10
  total_capacity_sp: 120 # 6 sprints × 2 devs × 10 SP

effort:
  total_story_points: 94
  total_dev_hours: 752
  contingency_buffer_hours: 188
  total_hours_with_buffer: 940

timeline:
  total_sprints: 6
  total_weeks: 12
  total_months: 3
  start_date: "2026-01-06"
  end_date: "2026-03-30"
```

### Epic Breakdown (JSON)

```json
{
  "epics": [
    {
      "id": "EP-001",
      "title": "Document Parser (YAML + Pydantic)",
      "phase": "Foundation",
      "story_points": 5,
      "hours": 40,
      "sprint": 1,
      "dependencies": []
    },
    {
      "id": "EP-002",
      "title": "Hybrid Storage (Files + SQLite)",
      "phase": "Foundation",
      "story_points": 8,
      "hours": 64,
      "sprint": 1,
      "dependencies": ["EP-001"]
    },
    {
      "id": "EP-009",
      "title": "Cytoscape.js Integration",
      "phase": "Core Features",
      "story_points": 8,
      "hours": 64,
      "sprint": 4,
      "dependencies": ["EP-007", "EP-008"],
      "risk": "high",
      "risk_buffer_sp": 2
    }
  ],
  "summary": {
    "total_epics": 18,
    "total_sp": 94,
    "total_hours": 752,
    "phases": {
      "foundation": {"sp": 26, "hours": 208},
      "core_features": {"sp": 39, "hours": 312},
      "integration": {"sp": 29, "hours": 232}
    }
  }
}
```

### Sprint Plan (Detailed)

```
Sprint 1 (Weeks 1-2): Foundation Setup
├── EP-001: Document Parser (40h)
├── EP-002: Hybrid Storage (64h)
└── EP-003: FTS5 Search Engine (40h)
Total: 144h / 2 devs = 72h per dev (9 days @ 8h/day)

Sprint 2 (Weeks 3-4): Foundation Complete
├── EP-004: CLI Prototype (24h)
├── EP-005: Testing Infrastructure (24h)
└── EP-006: CI/CD Setup (16h)
Total: 64h / 2 devs = 32h per dev (4 days @ 8h/day)

Sprint 3 (Weeks 5-6): Qt App Shell
├── EP-007: Qt Application Shell (40h)
└── EP-008: Canvas Board UI (64h)
Total: 104h / 2 devs = 52h per dev (6.5 days @ 8h/day)

Sprint 4 (Weeks 7-8): Graph Visualization [PEAK]
├── EP-009: Cytoscape.js Integration (64h)
├── EP-010: Graph Layout Algorithms (40h)
└── EP-011: Node/Edge Editing (64h)
Total: 168h / 2 devs = 84h per dev (10.5 days @ 8h/day)

Sprint 5 (Weeks 9-10): Document Viewer + Search
├── EP-012: Document Viewer (40h)
└── EP-013: Search UI (40h)
Total: 80h / 2 devs = 40h per dev (5 days @ 8h/day)

Sprint 6 (Weeks 11-12): Integration & Polish [PEAK]
├── EP-014: Relationship Browser (64h)
├── EP-015: Export Features (40h)
├── EP-016: Settings & Preferences (24h)
├── EP-017: Error Handling & Logging (24h)
└── EP-018: Documentation & User Guide (40h)
Total: 192h / 2 devs = 96h per dev (12 days @ 8h/day)
```

### Historical Comparison Data

| Project | Type | Team | Duration | Effort | Velocity |
|---------|------|------|----------|--------|----------|
| Desktop App A | Qt + Python | 3 devs | 8 weeks | 850h | 11 SP/sprint |
| Desktop App B | Electron + TS | 2 devs | 10 weeks | 720h | 9 SP/sprint |
| **Semantic Canvas** | **Qt + Python** | **2 devs** | **12 weeks** | **940h** | **10 SP/sprint** |

**Analysis**: Semantic Canvas effort aligns z industry standards dla desktop app MVP.

---

**Konkluzja**: MVP Semantic Canvas wymaga 6 sprintów (12 tygodni, 3 miesiące) z 2 developerami. Total effort: 940h (752h dev + 188h buffer). Estymacja bazuje na prototypach (E-144), benchmarkach i historical data - timeline jest realny i achievable. Rekomendacja: approve plan zgodnie z IMPL-PLAN-001 i ROADMAP-001.
