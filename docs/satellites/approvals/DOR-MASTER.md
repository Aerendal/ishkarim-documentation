---
id: DOR-MASTER
title: "Master Definition of Ready Checklist"
type: dor
status: approved
created: 2025-12-26
---

# Definition of Ready (DoR) - Master Checklist

## Cel
Przed rozpoczęciem pracy nad jakimkolwiek dokumentem, upewnij się że spełnia kryteria DoR.

## Universal DoR (Wszystkie Dokumenty)

- [ ] **Zależności resolved**: Wszystkie upstream docs istnieją i mają poprawny status
- [ ] **Użyto template**: Dokument utworzony z odpowiedniego szablonu
- [ ] **Frontmatter kompletny**: Wszystkie wymagane pola YAML wypełnione
- [ ] **Status poprawny**: Początkowy status odpowiedni dla typu dokumentu
- [ ] **Owner assigned**: Wyraźny owner/odpowiedzialność
- [ ] **Evidence dostępne**: Referencjonowane noty dowodowe istnieją

## DoR Per-Type

### PRD (Product Requirements Document)
- [ ] Vision i Business Case zatwierdzone
- [ ] Dokument Concepts sfinalizowany
- [ ] Stakeholderzy zidentyfikowani
- [ ] User research ukończony

### TDD (Technical Design Document)
- [ ] PRD w statusie "req-freeze" lub "approved"
- [ ] Wszystkie ADR dla kluczowych decyzji istnieją
- [ ] Tech stack uzasadniony
- [ ] Performance benchmarki dostępne

### Implementation Plan
- [ ] TDD w statusie "design-complete"
- [ ] Milestone'y roadmapy zdefiniowane
- [ ] Alokacja zasobów potwierdzona
- [ ] Mitigation ryzyka zaplanowane

### Test Plan
- [ ] Wymagania PRD zamrożone
- [ ] Design TDD ukończony
- [ ] Środowisko testowe dostępne
- [ ] Cele coverage zdefiniowane

## Weryfikacja
Dokument nie może przejść z "draft" do "in-progress" dopóki DoR nie jest spełnione.
