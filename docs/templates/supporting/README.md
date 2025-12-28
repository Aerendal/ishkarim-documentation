# Supporting — Dokumenty Wspierające i Meta-Dokumentacja

## 📋 Przeznaczenie

Folder zawiera **dokumenty wspierające system szablonów** — meta-dokumentację, overviews, reference guides i inne materiały pomocnicze, które **nie są bezpośrednio szablonami projektowymi**, ale wspierają ich użycie.

## 🎯 Funkcja

Dokumenty w tym folderze służą do:
- **Zrozumienia systemu** (overviews, guides)
- **Referencji** (ASCII diagrams, tabele, TOC)
- **Meta-informacji** (o szablonach, o strukturze)
- **Podsumowań** (summaries różnych aspektów systemu)

## 👥 Kto używa?

- **Nowi użytkownicy** — overviews, initialization guides
- **Autorzy dokumentacji** — reference tables, TOC
- **Architekci systemu** — meta-documentation, structure analysis
- **Contributors** — extending guides, verification checklists

## ⏱️ Kiedy używać?

**Timing:**
- **Onboarding:** Gdy nowy użytkownik zaczyna pracę z systemem
- **Reference:** Gdy potrzebujesz quick lookup (tabele, diagramy)
- **Extension:** Gdy dodajesz nowe typy dokumentów
- **Verification:** Gdy sprawdzasz completeness systemu

## 📂 Struktura supporting/ (16 plików)

### 📁 meta/ (4 pliki)
Dokumenty **o samym systemie dokumentacji**:
- `documentation_meta_doc.md` — Meta-dokumentacja o dokumentacji
- `system_tests_framework_doc.md` — Framework testowania systemu
- `meta_protected_files_and_immutability.md` — Pliki chronione
- `questions_proposals.md` — Pytania i propozycje zmian

### 📁 reference/ (4 pliki)
**Quick reference** dla użytkowników:
- `ascii_diagram_zaleznosci.md` — ASCII diagram zależności
- `diagram_zaleznosci_dokumentacji.md` — Diagram zależności (Mermaid)
- `dokumentacja_tabela.md` — Tabela wszystkich dokumentów
- `toc_dokumentacja.md` — Table of Contents

### 📁 summaries/ (4 pliki)
**Podsumowania** różnych aspektów:
- `advanced_features.md` — Advanced features systemu
- `extending_new_types.md` — Jak dodawać nowe typy dokumentów
- `initialization_structure.md` — Struktura inicjalizacji
- `verification_toc.md` — Weryfikacja TOC

### 📁 templates-overviews/ (4 pliki)
**Overviews** grup szablonów (przed ekstrakcją):
- `roadmaps_satellite_templates_*.md` — Overview roadmaps + atomic templates
- `sprint_output_contract_*.md` — Overview sprint output contracts
- `sprinty_pliki_satelitarne_i_szablony_*.md` — Overview sprintów
- `templates_readme_and_samples.md` — README i przykłady

## 🔗 Powiązania

**Dependencies:**
- ⬅️ **Specs** → Meta-docs referencują specs (doc types, error codes)
- ⬅️ **All Templates** → Reference docs opisują wszystkie templates

**Impacts:**
- ➡️ **Onboarding** → Nowi użytkownicy zaczynają od supporting docs
- ➡️ **System evolution** → Extending guides wpływają na rozwój systemu
- ➡️ **Verification** → Verification docs zapewniają quality control

## 📊 Statystyki

- **Liczba plików:** 16
- **Pokrycie Cross-References:** ~50% (meta-docs nie zawsze wymagają CR)
- **Rola:** Supporting (non-project templates)
- **Średnia wielkość:** 50-200 linii per dokument

## 🚀 Quick Start dla nowych użytkowników

**Dzień 1: Onboarding**
1. `summaries/initialization_structure.md` — Zrozum strukturę systemu
2. `templates-overviews/templates_readme_and_samples.md` — Zobacz przykłady

**Dzień 2: Reference**
3. `reference/toc_dokumentacja.md` — Przeglądnij TOC wszystkich szablonów
4. `reference/dokumentacja_tabela.md` — Tabela quick reference

**Gdy chcesz rozszerzyć system:**
5. `summaries/extending_new_types.md` — Jak dodać nowy typ dokumentu
6. `meta/questions_proposals.md` — Zaproponuj zmianę

## ⚠️ Uwagi

- **Nie są to szablony projektowe:** Supporting docs nie są używane bezpośrednio w projektach
- **Meta-informacja:** Opisują system, nie są częścią systemu projektowego
- **Ewolucja:** Te dokumenty ewoluują wraz z systemem (są "żywe")
- **Reference tylko:** Niektóre docs są tylko read-only reference (np. tabele, diagramy)

## 📖 Zobacz też

- [../specs/](../specs/) — Specyfikacje systemu (doc types, error codes, gates)
- [../examples/](../examples/) — Przykłady wypełnionych szablonów
- [../../dependency_graph.md](../../dependency_graph.md) — Graf zależności
- [../dokumentacja_typy.md](../dokumentacja_typy.md) — Katalog wszystkich szablonów

---

**Wygenerowano:** 2025-12-28
**Kategoria:** Supporting (Meta-Documentation & Reference)
**Rola:** Wspieranie użytkowników systemu, nie bezpośrednie szablony projektowe
