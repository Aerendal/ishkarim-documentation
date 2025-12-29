---
id: ADR-002
title: "ADR-002: File Monitoring"
type: adr
domain: architecture
status: approved
created: 2025-12-26
updated: 2025-12-29
decision_date: 2025-12-19
author: ["Tech Lead"]
parent: TDD-001-V2

# === Living Documentation Framework (PROPOZYCJA-2) ===

# Status Metadata
status_metadata:
  previous_status: draft
  status_changed_date: "2025-12-19"
  status_reason: "Decision approved after reliability testing - Watchdog selected"
  next_review_date: "2026-12-19"
  review_frequency: "annual"

# Lifecycle Tracking
lifecycle:
  created: "2025-12-26"
  first_approved: "2025-12-19"
  last_modified: "2025-12-29"
  last_reviewed: "2025-12-29"
  sunset_date: null
  migration_target: null
  note: "ADRs are typically long-lived - reviewed annually or when triggered"

# Version Metadata (Semantic Versioning)
version: "1.0.0"
version_metadata:
  major: 1
  minor: 0
  patch: 0
  breaking_changes: false
  backward_compatible_with: []
  note: "ADR approved - establishes file monitoring library choice"

version_history:
  - version: "1.0.0"
    date: "2025-12-19"
    author: "Tech Lead"
    type: "major"
    summary: "Decision approved: Watchdog 3.0+ selected for file monitoring"
    breaking: false
    changes:
      - "Evaluated 3 options: Native APIs, Polling, Watchdog"
      - "Selected Watchdog 3.0+ (cross-platform, 99.9% reliable, mature)"
      - "Rejected Native APIs (platform-specific nightmare)"
      - "Rejected Polling (CPU waste, latency issues)"
    impacts:
      - id: "TDD-001-V2"
        impact_type: "informs"
        description: "Architecture includes Watchdog for file monitoring"

# Cross-Reference Status
cross_reference_status:
  upstream_changes_pending: []
  downstream_impacts_pending: []

# Document Health
document_health:
  status: "healthy"
  last_health_check: "2025-12-29"
  checks:
    - name: "Freshness Check"
      status: "healthy"
      last_modified: "2025-12-29"
      threshold_days: 365
      days_since_modified: 10
      note: "ADRs have longer freshness threshold (365 days)"

    - name: "Dependency Validity"
      status: "healthy"
      invalid_dependencies: []
      all_dependencies_valid: true

    - name: "Cross-Reference Consistency"
      status: "healthy"
      all_references_valid: true
      broken_references: []

    - name: "Owner Assignment"
      status: "healthy"
      owner: "Tech Lead"
      owner_active: true

    - name: "Required Sections Completeness"
      status: "healthy"
      missing_sections: []
      completeness: "100%"

    - name: "Upstream Changes Pending"
      status: "healthy"
      pending_changes: 0

    - name: "Satellite Completeness"
      status: "healthy"
      missing_satellites: []
      note: "Evidence E-147, E-163 support decision"

# Deprecation
deprecation: null

dependencies:
  - id: "TDD-001-V2"
    type: requires
    reason: "Real-time UX requirement demands file monitoring"

impacts:
  - id: "TDD-001-V2"
    type: informs
    reason: "Architecture updated with Watchdog library"

context_snapshot:
  date: "2025-12-19"
  requirements:
    - "Cross-platform (Linux/macOS/Windows)"
    - "Reliable (> 99% event detection)"
    - "Low latency (< 1s from change to rebuild)"
    - "Simple API"

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
