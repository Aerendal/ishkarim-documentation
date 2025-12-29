---
id: DOD-MASTER
title: "Master Definition of Done Checklist"
type: dod
status: approved
created: 2025-12-26
---

# Definition of Done (DoD) - Master Checklist

## Cel
Przed oznaczeniem jakiegokolwiek dokumentu jako "completed", upewnij się że spełnia kryteria DoD.

## Universal DoD (Wszystkie Dokumenty)

- [ ] **Wszystkie sekcje kompletne**: Brak placeholderów TODO/TBD w critical sections
- [ ] **Frontmatter kompletny**: Wszystkie wymagane pola wypełnione
- [ ] **Evidence zlinkowane**: Wszystkie referencje [E-XXX] istnieją
- [ ] **Cross-references valid**: Wszystkie linki do innych docs działają
- [ ] **Peer reviewed**: Przynajmniej 1 inna osoba zrewidowała
- [ ] **Stakeholder approved**: Właściwi stakeholderzy zaaprobowali
- [ ] **Gaps addressed**: 0 critical gaps wykrytych
- [ ] **Impacts updated**: Downstream docs powiadomione o completion

## DoD Per-Type

### PRD
- [ ] Wszystkie FR (functional requirements) zdefiniowane z AC
- [ ] Wszystkie NFR (non-functional) zdefiniowane z metrykami
- [ ] User stories kompletne
- [ ] RTM zainicjalizowane
- [ ] Gate REQ-FREEZE passed

### TDD
- [ ] Diagram architektury systemu kompletny
- [ ] Wszystkie komponenty wyspecyfikowane
- [ ] Data models zdefiniowane
- [ ] Kontrakty API udokumentowane
- [ ] Performance targets ustawione
- [ ] Gate DESIGN-COMPLETE passed

### Implementation Plan
- [ ] Wszystkie sprinty zaplanowane
- [ ] Taski estymowane
- [ ] Zależności zmapowane
- [ ] Alokacja zasobów potwierdzona

### Test Plan
- [ ] Poziomy testów zdefiniowane
- [ ] Cele coverage ustawione (≥80%)
- [ ] Środowisko skonfigurowane
- [ ] Acceptance criteria jasne

## Weryfikacja
Dokument nie może przejść do "approved" lub "completed" dopóki DoD nie jest spełnione.
