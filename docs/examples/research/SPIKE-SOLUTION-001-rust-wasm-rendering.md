# SPIKE-SOLUTION: SPIKE-001 - Czy Rust WASM przyspieszy renderowanie Canvas?

---

## Document Metadata

```yaml
id: SPIKE-001
doctype: SPIKE-SOLUTION
status: completed
version: 2.0
created: 2026-04-10
updated: 2026-04-12
owner: Tomasz Nowicki
project: Ishkarim Document Management System
spike_type: technical
timebox: 3 days
```

---

## Cross-References

```yaml
dependencies:
  - id: SPRINT-BACKLOG-Q2-2026
    type: research_input
    reason: "User Story US-156 blocked - potrzebujemy performance improvement dla Canvas rendering"

impacts:
  - id: USER-STORY-156
    type: blocks
    reason: "Spike redukuje uncertainty przed implementacją real-time Canvas collaboration"
  - id: ADR-045
    type: influences
    reason: "Wyniki spike'u mogą prowadzić do decyzji o adoption Rust/WASM"
```

---

## SEC-SPIKE-QUESTION: Pytanie badawcze

### Główne pytanie

**Czy możemy użyć Rust compiled do WebAssembly (WASM) aby przyspieszyć renderowanie dużych Canvas diagramów (1000+ nodes) w przeglądarce o minimum 50%?**

### Kontekst

Ishkarim wspiera `.canvas` files (node-based diagrams). Przy dużych diagramach (>500 nodes) obserwujemy:
- Initial render: 3.2s (Chrome), 4.5s (Firefox)
- Pan/zoom: janky (15-20 FPS, target 60 FPS)
- User complaints: "Laggy", "Unusable dla large diagrams"

Current implementation: Pure JavaScript + HTML5 Canvas API

### Related Work Items

- **US-156**: Real-time collaborative Canvas editing
  - BLOCKED: Performance must be acceptable before adding real-time sync complexity
  - Acceptance criteria: <1s initial render, 60 FPS pan/zoom

### Unknown/Risk

**What we don't know:**
- Czy WASM overhead (JS ↔ WASM boundary crossing) zniweluje performance gains?
- Czy bundle size impact (+2MB WASM module) jest acceptable?
- Czy browser compatibility wystarczająca? (target: 95%+ users)
- Jak trudne jest dev workflow (Rust compilation, debugging)?

**Risk:**
- Jeśli spike pokazuje "nie warto" → US-156 needs alternative approach (may delay Q2 roadmap)

---

## SEC-SPIKE-WHY: Dlaczego teraz (business value)

### Business Impact

- **Customer satisfaction:** 8 enterprise customers complained o Canvas performance (last 3 months)
- **Competitive pressure:** Miro, Figma render large boards instantly
- **Roadmap blocker:** US-156 (real-time collab) jest #2 feature request (247 votes)
- **Revenue risk:** 2 customers rozważają churn jeśli Canvas performance nie improve

### Blocker Status

- [x] **This spike blocks**: US-156 (Real-time Canvas collaboration)
- [ ] This spike is nice-to-have exploration

**Without spike:** Development team może waste 4 weeks implementing US-156 only to discover performance is still unacceptable.

### Cost of Delay

**Jeśli nie odpowiemy teraz:**
- US-156 delayed → Q2 roadmap at risk
- Customers leave → estimated -$15K MRR
- Team implements wrong solution → wasted 4-6 weeks effort

**Spike cost:** 3 days (1 developer) = $2,400
**Prevented waste:** 4 weeks wrong implementation = $32,000
**ROI:** 13x

### Value Proposition

- **De-risk US-156**: Know performance feasibility before heavy investment
- **Technical knowledge**: Team learns WASM (future-proofing skills)
- **Data-driven decision**: Empirical evidence vs speculation

---

## SEC-SPIKE-APPROACH: Podejście

### Timebox

- **Start:** 2026-04-10 (Wednesday)
- **End:** 2026-04-12 (Friday EOD)
- **Duration:** 3 dni (HARD STOP - no extensions!)

### Scope

**Will investigate:**
- Rust crate dla 2D rendering (candidate: `tiny-skia`, `raqote`)
- Compile Rust → WASM z `wasm-pack`
- Benchmark: Render 1000-node Canvas diagram
- Measure: Initial render time, FPS podczas pan/zoom
- Evaluate: Bundle size impact, browser compatibility

**Will NOT investigate:**
- Full Canvas implementation (tylko minimal prototype)
- Real-time collaboration logic (out of scope)
- Advanced features (layers, filters, exports)
- Production-ready error handling
- Complete Rust rewrite (only critical path: rendering loop)

### Methodology

**Approach: Build Minimal WASM Prototype**

- [x] **Day 1 - Setup & Proof of Concept:**
  - Install Rust toolchain, `wasm-pack`
  - Create minimal Rust project (render single rectangle na Canvas)
  - Verify WASM compilation works, can call from JavaScript

- [x] **Day 2 - Benchmark Implementation:**
  - Implement rendering loop dla 1000 nodes (boxes + connections)
  - Benchmark WASM vs pure JS implementation
  - Measure initial render, pan/zoom FPS

- [x] **Day 3 - Evaluation & Decision:**
  - Bundle size analysis (+X MB?)
  - Browser compatibility testing (Chrome, Firefox, Safari, Edge)
  - Developer experience assessment (compile time, debugging)
  - Write recommendation: YES/NO/CONDITIONAL

### Tools & Resources

- **Rust 1.77** + `wasm-pack`
- **tiny-skia** - pure Rust 2D rendering library (no GPU dependencies)
- **Chrome DevTools** - Performance profiling
- **BrowserStack** - Cross-browser testing
- **Webpack** - Bundle size analysis

### Success Criteria

**Spike is successful if:**
- [x] Answer question clearly: YES/NO/CONDITIONAL
- [x] Empirical data backing answer (benchmarks, not opinions)
- [x] Completed within 3-day timebox
- [x] Deliverable: Working prototype OR clear "не стоит" verdict

---

## SEC-SPIKE-FINDINGS: Odkrycia

### Day 1: 2026-04-10 (Setup & PoC)

**Activities:**
- ✅ Installed Rust 1.77, wasm-pack
- ✅ Created `canvas-wasm` project
- ✅ Implemented minimal example: Rust function `draw_rectangle()` callable z JS
- ✅ Verified WASM compilation works (2.3s compile time, 45KB wasm file dla hello world)

**Discoveries:**
- Rust → WASM tooling surprisingly mature! `wasm-pack` "just works"
- Compile times fast (2-3s dla simple project)
- JS ↔ WASM interop straightforward (via `wasm-bindgen`)

**Notes:**
Initial PoC encouraging. Tooling better than expected. Ready dla benchmark tomorrow.

---

### Day 2: 2026-04-11 (Benchmark Implementation)

**Activities:**
- ✅ Implemented Rust rendering loop: 1000 nodes (boxes + connections)
- ✅ JavaScript baseline: Same 1000 nodes, pure JS
- ✅ Ran benchmarks: Chrome Canary (10 runs each)

**Discoveries:**

**Initial Render Benchmark (1000 nodes):**
- **JavaScript baseline:** 3.1s average (consistent z production issue)
- **Rust WASM:** 0.9s average ✅ **71% faster!**
- Improvement: **-2.2s (-71%)**

**Pan/Zoom FPS Benchmark:**
- **JavaScript baseline:** 18 FPS (janky, visible lag)
- **Rust WASM:** 58 FPS ✅ **3.2x improvement!**
- Near 60 FPS target achieved

**Memory usage:**
- JavaScript: 185MB heap
- Rust WASM: 142MB heap (-23% improvement!)

**Bundle size:**
- WASM module: +1.8MB (compressed: +620KB gzip)
- Concern: Material but not showstopper

**Notes:**
Results blown away expectations! WASM dramatically faster. Performance target MET.

---

### Day 3: 2026-04-12 (Evaluation & Decision)

**Activities:**
- ✅ Browser compatibility testing (BrowserStack)
- ✅ Bundle size optimization (wasm-opt)
- ✅ Developer experience assessment
- ✅ Decision writeup

**Discoveries:**

**Browser Compatibility:**
- Chrome 90+: ✅ Full support (96% users)
- Firefox 85+: ✅ Full support
- Safari 14+: ✅ Full support (iOS included)
- Edge 90+: ✅ Full support
- **Coverage: 97.2% of our user base** ✅

IE11: ❌ No WASM support (but we dropped IE11 support Q1 2026 anyway)

**Bundle Size Optimization:**
- Raw WASM: 1.8MB
- After `wasm-opt -O3`: 1.1MB
- After gzip: **580KB** ✅ Acceptable!

**Developer Experience:**
- **Compile time:** 2-4s (fast feedback loop)
- **Debugging:** Source maps work w Chrome DevTools (surprising!)
- **Learning curve:** Steep for non-Rust devs (3/5 team members unfamiliar)
- **Build integration:** Easy (Webpack plugin works smoothly)

**Concerns:**
- Team expertise: Only 1/5 developers know Rust → training needed
- Maintenance burden: New language in stack → consider long-term
- Fallback strategy: Need JS fallback dla <3% unsupported browsers

---

### Key Learnings Summary

**✅ What Worked:**
- WASM performance gains REAL (71% faster render, 3.2x FPS)
- Tooling mature (wasm-pack, wasm-bindgen excellent)
- Browser support excellent (97%+ users)
- Bundle size acceptable after optimization (580KB gzipped)

**❌ What Didn't Work:**
- N/A - spike exceeded expectations

**⚠️ Concerns/Risks:**
- Team Rust expertise low (4/5 devs need training)
- Stack complexity +1 language
- Debugging slightly harder than pure JS (but manageable)

**💡 Unexpected Findings:**
- Memory usage LOWER w WASM (142MB vs 185MB) - bonus!
- Source maps work - debugging better than expected
- Compile times faster than anticipated (2-4s, not minutes)

---

## SEC-SPIKE-ANSWER: Odpowiedź na pytanie

### Answer

**YES, with conditions** ✅

Rust WASM **dramatically** improves Canvas rendering performance:
- 71% faster initial render (3.1s → 0.9s)
- 3.2x FPS improvement (18 FPS → 58 FPS)
- Meets all performance targets dla US-156

**However, requires investment:**
- Team Rust training (3-4 weeks ramp-up)
- JS fallback implementation (1 week effort)
- Ongoing maintenance (new language in stack)

### Explanation

WASM delivers on performance promise. The performance gains are substantial enough to justify adoption **for this specific use case** (Canvas rendering hot path).

**Why WASM wins:**
- CPU-bound rendering loop - perfect fit dla compiled language
- No DOM manipulation overhead (direct Canvas API)
- Memory efficiency - Rust's zero-cost abstractions

**Not just marginal - transformative improvement.**

### Supporting Evidence

1. **Benchmark data:** 10 runs, consistent results (±5% variance)
2. **Browser compatibility:** 97.2% user coverage tested
3. **Bundle size:** Optimized to 580KB (acceptable dla feature value)
4. **Dev experience:** Prototype built w 2 days (tooling works)

### Confidence Level

**High (90%)** - wyniki clear, reproducible, empirical

**Why not 100%:**
- Spike prototype != production code (edge cases nie tested)
- Long-term maintenance burden unknown
- Team learning curve may reveal hidden friction

### Conditions/Caveats

**Adoption requires:**

1. **Team Training:**
   - 2 developers complete Rust fundamentals course (4 weeks)
   - Code review standards dla Rust code
   - Documentation standards (Rust harder to read for non-experts)

2. **Fallback Implementation:**
   - Pure JS version dla <3% browsers without WASM support
   - Feature detection + graceful degradation

3. **Scope Limitation:**
   - Use WASM **only** dla rendering hot path (not entire Canvas codebase)
   - Keep business logic w TypeScript (team expertise, maintainability)
   - Minimize JS ↔ WASM boundary crossings (overhead)

4. **Build Pipeline:**
   - Integrate Rust compilation w CI/CD
   - Setup Rust linting (clippy) + formatting (rustfmt)

### Alternatives Considered

| Alternative | Pros | Cons | Verdict |
|------------|------|------|---------|
| **WASM (Rust)** | 71% faster, mature tooling | Team training needed | ✅ **RECOMMENDED** |
| **Web Workers (JS)** | No new language, easy | Only ~20% improvement (tested briefly) | ❌ Insufficient gains |
| **OffscreenCanvas API** | Native browser, no overhead | Limited browser support (85%), complex API | ⚠️ Consider for v2 |
| **WebGL (GPU)** | Extreme performance | Massive complexity, overkill dla 2D | ❌ Too complex |

---

## SEC-SPIKE-ACTIONS: Akcje wynikowe

### Immediate Actions

- [x] **2026-04-12**: Present spike results to team - **DONE** ✅
- [ ] **2026-04-15**: Create ADR-045: Adopt Rust/WASM for Canvas rendering
- [ ] **2026-04-17**: Update US-156: Split implementation (WASM + fallback)
- [ ] **2026-04-20**: Enroll 2 developers w Rust training course

### Documentation Updates

- [ ] **Create ADR-045**: "Use Rust WASM for Canvas Rendering Hot Path"
  - Context: Performance requirements
  - Decision: WASM dla rendering, JS dla business logic
  - Consequences: Training needed, build complexity

- [ ] **Update US-156**: Acceptance criteria met, implementation approach defined
  - Implementation plan: WASM rendering + JS fallback
  - Effort estimate: 3 weeks (2 weeks WASM, 1 week fallback + testing)

- [ ] **Create TDD-Canvas-WASM**: Technical design
  - Architecture: WASM module API
  - Integration: Webpack build, feature detection
  - Testing strategy: benchmark regression tests

### Follow-up Work Items

- [ ] **TASK-201**: Rust training dla Tomasz + Kasia (4 weeks, online course)
- [ ] **TASK-202**: Production WASM rendering implementation (2 weeks)
- [ ] **TASK-203**: JS fallback implementation + feature detection (1 week)
- [ ] **TASK-204**: Performance regression test suite (3 days)
- [ ] **TASK-205**: Documentation: Rust code standards, debugging guide (2 days)

**Total effort estimate:** 5 weeks (US-156 timeline feasible!)

### Recommendations

**For implementation:**

1. **Incremental adoption:**
   - Start z WASM dla rendering loop (highest ROI)
   - Keep interaction logic w TypeScript (lower risk)
   - Gradually expand WASM scope if successful

2. **Risk mitigation:**
   - Feature flag: enable/disable WASM (rollback safety)
   - A/B test: WASM vs JS dla 10% users first
   - Monitoring: Track performance metrics, error rates

3. **Team enablement:**
   - Pair programming: Rust expert + JS developers
   - Code reviews: Document Rust patterns, anti-patterns
   - Slack channel: #rust-help dla Q&A

**For further research:**

- **OffscreenCanvas API**: Revisit w 6 months (browser support improving)
- **AssemblyScript**: Alternative to Rust (TypeScript-like syntax, WASM output)
- **Web Workers + WASM**: Combine for non-blocking rendering

**For team:**

- **Training priority**: Rust fundamentals > advanced topics
- **Onboarding docs**: "Rust dla JavaScript Developers" guide
- **Tooling setup**: VS Code extensions, Rust analyzer, clippy

---

## Code/Prototype

### Repository Info

```
Repository: https://github.com/ishkarim/canvas-wasm-spike
Branch: main
Commit: e7d4a92 (final spike version)
```

### Key Files

- `src/lib.rs`: Rust rendering implementation (350 LOC)
- `www/index.js`: JavaScript integration + benchmark harness
- `benches/render_benchmark.rs`: Rust-side benchmarks
- `README.md`: Setup instructions, findings summary

### Running the Prototype

```bash
# Prerequisites: Rust 1.77+, Node 18+, wasm-pack
git clone https://github.com/ishkarim/canvas-wasm-spike
cd canvas-wasm-spike

# Build WASM module
wasm-pack build --target web

# Run dev server
cd www && npm install && npm start

# Open browser: http://localhost:8080
# Toggle WASM on/off, compare performance
```

### Benchmark Command

```bash
# Run Rust benchmarks
cargo bench

# Run JS benchmarks (Chrome DevTools)
npm run benchmark
```

### Screenshots/Demos

**Performance Comparison:**
![WASM vs JS Performance](../artifacts/spike-001-performance.png)

**Chrome DevTools Flame Graph:**
- JS version: 3.1s total (rendering hot)
- WASM version: 0.9s total (massive improvement)

**Bundle Size Analysis:**
![Webpack Bundle Analyzer](../artifacts/spike-001-bundle-size.png)

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| 2026-04-10 | 1.0 | Tomasz Nowicki | Spike initiated, Day 1 complete (PoC works) |
| 2026-04-11 | 1.5 | Tomasz Nowicki | Day 2 complete, benchmarks exceed expectations |
| 2026-04-12 | 2.0 | Tomasz Nowicki | Spike completed, answer: YES with conditions |

---

## Notatki i uwagi

### Refleksje po spike

**Co mnie zaskoczyło:**
Nie spodziewałem się TAK dużej poprawy (71%!). Oczekiwałem może 40-50%. WASM seriously powerful dla CPU-bound tasks.

**Co było trudne:**
Początkowo Rust ownership system confusing (especially lifetimes). Ale tutorial + StackOverflow wystarczyły. Po Day 1 poszło smooth.

**Co bym zrobił inaczej:**
Zaplanowałbym 4 dni zamiast 3. Day 3 był rushed (testing + writeup). Ale zdążyłem, więc OK.

**Kluczowa lekcja:**
WASM nie jest silver bullet - ale dla konkretnych use cases (rendering loops, parsery, compression) to game changer. Worth the complexity **for the right problem**.

### Team Feedback (post-spike demo)

**Anna (PO):**
> "71% improvement to exactly what we need dla US-156! Customer wow factor guaranteed."

**Piotr (Backend Dev):**
> "I'm excited to learn Rust! Performance wyniki speaks for themselves. Let's do this."

**Kasia (Frontend Dev):**
> "Trochę obawiam się Rust learning curve, ale gotowa spróbować. Pair programming pomoże."

**Jan (CTO):**
> "Approved. Invest w training, proceed z implementation. Monitor closely, iterate."

### Risks dla implementation

1. **Rust expertise gap:** Mitigated przez training + pair programming
2. **Build complexity:** Mitigated przez Webpack integration (already working)
3. **Browser compatibility edge cases:** Mitigated przez JS fallback + feature detection
4. **Performance regression:** Mitigated przez automated benchmark tests w CI

**Overall:** Risks acceptable given massive performance upside.

---

**Spike outcome:** ✅ **SUCCESS** - Clear answer, actionable next steps, team aligned

**Next:** Create ADR-045, kick off US-156 implementation! 🚀

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** technical
