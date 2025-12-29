---
id: ADR-002
title: "ADR-002: File Monitoring"
type: adr
status: approved
decision_date: 2025-12-19
parent: TDD-001-V2

evidence_ids:
  - "E-147"  # Watchdog reliability test (99.9% event detection)
  - "E-163"  # Native API comparison (platform-specific nightmare)

alternatives:
  - id: "OPT-NATIVE"
    title: "Native APIs (inotify/FSEvents/ReadDirectoryChangesW)"
    status: rejected
    reason: "Platform-specific code, complex, no cross-platform abstraction"

  - id: "OPT-POLLING"
    title: "Polling (check every N seconds)"
    status: rejected
    reason: "Inefficient (CPU waste), delay (user waits N seconds), battery drain"

  - id: "OPT-WATCHDOG"
    title: "Watchdog library"
    status: selected
    reason: "Cross-platform abstraction, reliable (99.9%), mature (10+ years), simple API"
---

# ADR-002: File Monitoring

**Decision**: Use **Watchdog 3.0+** library

**Status**: ✅ APPROVED

---

## Context

**Problem**: Auto-rebuild when .md files change (real-time UX).

**Requirements**:
1. Cross-platform (Linux/macOS/Windows)
2. Reliable (> 99% event detection)
3. Low latency (< 1s from change → rebuild)
4. Simple API

---

## Decision

### Watchdog 3.0+ ✅

**Why**:
- ✅ **Cross-platform**: Abstracts inotify (Linux), FSEvents (macOS), ReadDirectoryChangesW (Windows)
- ✅ **Reliable**: 99.9% event detection [E-147]
- ✅ **Mature**: 10+ years production use
- ✅ **Simple API**: Event handler pattern

**Usage**:
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DocHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.md'):
            rebuild(event.src_path)

observer = Observer()
observer.schedule(DocHandler(), "docs/", recursive=True)
observer.start()
```

**Evidence**: [E-147] Test: 10k file changes → 1 miss (99.99% success)

---

## Alternatives

### Native APIs ❌
**Cons**: Platform-specific code (3× implementations), complex, maintenance nightmare
**Rejected**: Watchdog abstracts this

### Polling ❌
**Cons**: CPU waste, battery drain, latency (N seconds delay)
**Rejected**: Event-driven superior

---

## Consequences

**Positive**:
- ✅ Real-time UX (user sees updates < 1s after save)
- ✅ Cross-platform (single code path)

**Negative**:
- ⚠️ Dependency (but lightweight, stable)

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
