# [Tytuł Dokumentu META]

> **Framework:** [arc42 / C4 / IEEE 42010 / etc.]  
> **Data opracowania:** [YYYY-MM-DD]  
> **Wersja dokumentu:** [X.Y]  
> **Autor:** [Imię/Zespół]  
> **Status:** [Draft / Review / Approved]  
> **Powiązane dokumenty:** [← Poprzedni], [→ Następny], [→ Powiązane]

---

## Document Cross-References

### Dependencies (Co napędza ten dokument)

```yaml
dependencies:
  - id: PROJECT-CHARTER
    type: context_source
    from_sections:
      - project_goals
      - stakeholders
      - success_criteria
    to_sections:
      - document_purpose
      - target_audience
      - success_metrics
    influence: "Charter projektu definiuje kontekst i cele dokumentacji"
    when:
      condition: document.type == "meta"
      applies: always

  - id: DOCUMENTATION-STANDARDS
    type: formatting_requirements
    from_sections:
      - structure_guidelines
      - quality_criteria
    to_sections:
      - document_format
      - quality_checklist
    influence: "Standardy określają wymagania formatowania i jakości"
    when:
      condition: project.has_documentation_standards == true
      applies: always
```

### Impacts (Co ten dokument popycha do przodu)

```yaml
impacts:
  - id: ALL-OTHER-DOCUMENTS
    type: template_source
    from_sections:
      - document_structure
      - quality_standards
      - completion_criteria
    to_sections:
      - document_scaffolding
      - quality_gates
    influence: "Meta dokument definiuje strukturę innych dokumentów"
    when:
      condition: document.is_template == true
      applies: always

  - id: DOCUMENTATION-QUALITY-REPORT
    type: compliance_measurement
    from_sections:
      - completeness_checklist
      - quality_criteria
    to_sections:
      - compliance_metrics
      - quality_scores
    influence: "Meta-standardy są mierzone w raporcie jakości dokumentacji"
    when:
      condition: quality.tracked == true
      applies: conditionally
```

### Related Documents (Powiązane dokumenty)

```yaml
related:
  - id: STYLE-GUIDE
    relationship: writing_standards
    sections_mapping:
      - from: writing_conventions
        to: content_guidelines
    usage: "Style guide określa konwencje pisania dokumentacji"

  - id: DOCUMENTATION-TOOLCHAIN
    relationship: technical_infrastructure
    sections_mapping:
      - from: tools_configuration
        to: document_generation
    usage: "Toolchain automatyzuje generowanie dokumentacji"
```

### Satellite Documents

```yaml
satellites:
  - name: DOCUMENT-TEMPLATES
    purpose: "Szablony dla każdego typu dokumentu"
    trigger: per_document_type
    lifecycle: permanent
    retention: permanent

  - name: DOCUMENTATION-METRICS-DASHBOARD
    purpose: "Dashboard pokazujący pokrycie i jakość dokumentacji"
    trigger: continuous
    lifecycle: realtime
    retention: 6_months_historical
```

---

## EXECUTIVE SUMMARY

### Cel Dokumentu
[Dlaczego ten dokument istnieje - jaką wartość dodaje, dla kogo jest, 2-3 zdania]

### Kluczowe Wnioski
[3-5 najważniejszych wniosków/rekomendacji z tego dokumentu]

1. **[Wniosek 1]:** [Szczegóły - 1 zdanie]
2. **[Wniosek 2]:** [Szczegóły - 1 zdanie]
3. **[Wniosek 3]:** [Szczegóły - 1 zdanie]

### Zakres
[Co jest w zakresie tego dokumentu, co jest poza zakresem - bullet points]

**W zakresie:**
- [Element 1]
- [Element 2]
- [Element 3]

**Poza zakresem:**
- [Element 1]
- [Element 2]

### Dashboard / Metryki Kluczowe
[Tabela z najważniejszymi metrykami/statusem projektu]

| Metryka | Wartość | Trend | Target | Status |
|---------|---------|-------|--------|--------|
| [Metryka 1] | [X] | ↑/→/↓ | [Y] | ✓/⚠️/✗ |
| [Metryka 2] | [X] | ↑/→/↓ | [Y] | ✓/⚠️/✗ |
| [Metryka 3] | [X] | ↑/→/↓ | [Y] | ✓/⚠️/✗ |

---

## 1. KONTEKST I CELE

### 1.1. Kontekst Biznesowy
[Dlaczego to robimy z perspektywy biznesu - problem, opportunity, 1-2 akapity]

### 1.2. Cel Techniczny
[Cel techniczny - co chcemy osiągnąć technicznie, 1-2 akapity]

### 1.3. Interesariusze (IEEE 42010)

| Rola | Osoba/Zespół | Concerns | Wpływ | Zaangażowanie |
|------|--------------|----------|-------|---------------|
| [Product Owner] | [Nazwa] | [Business value, ROI] | Wysoki | Tygodniowy |
| [Tech Lead] | [Nazwa] | [Architecture, quality] | Wysoki | Dzienny |
| [Developer] | [Nazwa] | [Implementation] | Średni | Dzienny |
| [Stakeholder] | [Nazwa] | [Specific concern] | Średni | Miesięczny |

### 1.4. Historia i Ewolucja
[Jak doszliśmy do tego punktu - krótka historia projektu/decyzji]

- **[YYYY-MM-DD]:** [Milestone 1]
- **[YYYY-MM-DD]:** [Milestone 2]
- **[YYYY-MM-DD]:** [Milestone 3]

---

## 2. [SEKCJA GŁÓWNA 1]

### 2.1. [Podsekcja 1.1]
[Treść - opisy, diagramy, tabele, przykłady kodu]

#### 2.1.1. [Pod-podsekcja jeśli potrzebna]
[Szczegóły]

### 2.2. [Podsekcja 1.2]
[Treść]

### 2.3. [Podsekcja 1.3]
[Treść]

---

## 3. [SEKCJA GŁÓWNA 2]

[Analogicznie jak sekcja 2]

---

## 4. [SEKCJA GŁÓWNA 3]

[Analogicznie]

---

## 5. DIAGRAMY I WIZUALIZACJE

### 5.1. [Nazwa Diagramu 1]

**Typ:** [C4 Context / Container / Component / Sequence / etc.]

```
[ASCII diagram lub opis gdzie znajduje się plik .png/.svg]

┌─────────────┐         ┌─────────────┐
│   System A  │────────▶│   System B  │
└─────────────┘         └─────────────┘
```

**Opis:**
[Co pokazuje ten diagram, kluczowe elementy]

### 5.2. [Nazwa Diagramu 2]

[Analogicznie]

---

## 6. DANE I MODELE

### 6.1. [Model Danych 1]

**Format:** [JSON / YAML / SQL / etc.]

**Schema:**
```json
{
  "type": "object",
  "properties": {
    "field1": {"type": "string"},
    "field2": {"type": "integer"}
  },
  "required": ["field1"]
}
```

**Przykład:**
```json
{
  "field1": "example value",
  "field2": 42
}
```

### 6.2. [Model Danych 2]

[Analogicznie]

---

## 7. METRYKI I KPI

### 7.1. Metryki Techniczne

| Metryka | Baseline | Current | Target | % do celu |
|---------|----------|---------|--------|-----------|
| [Metryka 1] | [X] | [Y] | [Z] | [W%] |
| [Metryka 2] | [X] | [Y] | [Z] | [W%] |

### 7.2. Metryki Biznesowe

| Metryka | Baseline | Current | Target | Impact |
|---------|----------|---------|--------|--------|
| [Metryka 1] | [X] | [Y] | [Z] | [Opis wpływu] |

### 7.3. Tracking

**Frequency:** [Daily / Weekly / Monthly]

**Responsibility:** [Kto aktualizuje]

**Dashboards:** [Link do Grafana/etc.]

---

## 8. IDENTYFIKACJA PROBLEMÓW

### 8.1. Top Problemy

| ID | Problem | Severity | Impact | Effort | Owner | Status |
|----|---------|----------|--------|--------|-------|--------|
| [P-001] | [Opis] | P0 | [Area] | XL | [Zespół] | Open |
| [P-002] | [Opis] | P1 | [Area] | M | [Zespół] | In Progress |

### 8.2. Root Cause Analysis

**Problem [P-001]:**
- **Symptom:** [Co obserwujemy]
- **Root Cause:** [Głębsza przyczyna]
- **Impact:** [Wpływ na system/biznes]
- **Solution:** [Proponowane rozwiązanie]

---

## 9. REKOMENDACJE I NASTĘPNE KROKI

### 9.1. Immediate Actions (Week 1-2)

- [ ] [Akcja 1 - opis, owner, deadline]
- [ ] [Akcja 2]
- [ ] [Akcja 3]

**Effort:** [X person-days]  
**Owner:** [Zespół]

### 9.2. Short-term (Month 1)

- [ ] [Akcja 1]
- [ ] [Akcja 2]

**Effort:** [X person-days]  
**Owner:** [Zespół]

### 9.3. Medium-term (Month 2-3)

- [ ] [Akcja 1]
- [ ] [Akcja 2]

### 9.4. Long-term (Month 4-6)

- [ ] [Akcja 1]
- [ ] [Akcja 2]

---

## 10. RYZYKA I MITIGACJE

### 10.1. Risk Register

| ID | Risk | Probability | Impact | Score | Mitigation |
|----|------|-------------|--------|-------|------------|
| R-001 | [Opis ryzyka] | High/Med/Low | High/Med/Low | [P×I] | [Strategia mitigacji] |
| R-002 | [Opis] | Med | High | 12 | [Strategia] |

### 10.2. Contingency Plans

**If [Ryzyko R-001] materializuje się:**
- **Plan A:** [Pierwsza opcja]
- **Plan B:** [Druga opcja - jeśli A nie działa]
- **Escalation:** [Do kogo eskalować]

---

## 11. DEPENDENCIES I ZAŁOŻENIA

### 11.1. Dependencies

**Wewnętrzne (w projekcie):**
- **[Dependency 1]:** [Opis - od czego zależy ten element]
- **[Dependency 2]:** [Opis]

**Zewnętrzne (poza projektem):**
- **[External Dep 1]:** [Opis - vendor, service, etc.]
- **[External Dep 2]:** [Opis]

### 11.2. Założenia

1. **[Założenie 1]:** [Opis założenia - co zakładamy jako prawdziwe]
2. **[Założenie 2]:** [Opis]
3. **[Założenie 3]:** [Opis]

**Verification:** [Jak zweryfikujemy że założenia są prawdziwe]

---

## 12. TIMELINE I MILESTONES

### 12.1. Gantt Chart (High-level)

```
Task                | W1 | W2 | W3 | W4 | W5 | W6 |
--------------------|----|----|----|----|----|----|
[Task 1]            |████|████|    |    |    |    |
[Task 2]            |    |████|████|    |    |    |
[Task 3]            |    |    |████|████|    |    |
[Task 4]            |    |    |    |████|████|████|
```

### 12.2. Milestones

| Milestone | Date | Deliverables | Status |
|-----------|------|--------------|--------|
| [M1: Kick-off] | [YYYY-MM-DD] | [Lista deliverables] | ✓ Completed |
| [M2: Phase 1] | [YYYY-MM-DD] | [Lista] | 🔄 In Progress |
| [M3: Phase 2] | [YYYY-MM-DD] | [Lista] | ⏳ Pending |

---

## 13. SUCCESS CRITERIA (DEFINITION OF DONE)

### 13.1. Acceptance Criteria

**Must Have (P0):**
- [ ] [Kryterium 1 - co MUSI być spełnione]
- [ ] [Kryterium 2]
- [ ] [Kryterium 3]

**Should Have (P1):**
- [ ] [Kryterium 1 - dobrze mieć, ale nie krytyczne]
- [ ] [Kryterium 2]

**Nice to Have (P2):**
- [ ] [Kryterium 1 - bonus features]

### 13.2. Quality Gates

- [ ] All tests pass (unit, integration, E2E)
- [ ] Test coverage > 85%
- [ ] No Critical security issues
- [ ] Performance SLA met
- [ ] Documentation complete
- [ ] Peer review approved (2+ reviewers)
- [ ] Architect review approved

---

## 14. WNIOSKI I PODSUMOWANIE

### 14.1. Mocne Strony ✓

1. **[Mocna strona 1]:** [Opis - co robimy dobrze]
2. **[Mocna strona 2]:** [Opis]
3. **[Mocna strona 3]:** [Opis]

### 14.2. Słabe Strony / Wyzwania ⚠️

1. **[Słaba strona 1]:** [Opis - co wymaga poprawy]
2. **[Słaba strona 2]:** [Opis]
3. **[Słaba strona 3]:** [Opis]

### 14.3. Opportunities (SWOT)

1. **[Opportunity 1]:** [Opis szansy/możliwości]
2. **[Opportunity 2]:** [Opis]

### 14.4. Threats (SWOT)

1. **[Threat 1]:** [Opis zagrożenia]
2. **[Threat 2]:** [Opis]

### 14.5. Główne Rekomendacje

**Top 3 Priority Actions:**
1. **[Akcja 1]:** [Opis - dlaczego najważniejsza]
   - **Effort:** [XS/S/M/L/XL]
   - **Impact:** [High/Medium/Low]
   - **Owner:** [Zespół]
   - **Deadline:** [YYYY-MM-DD]

2. **[Akcja 2]:** [Analogicznie]

3. **[Akcja 3]:** [Analogicznie]

---

## ZAŁĄCZNIKI

### A. Słownik Pojęć

| Termin | Definicja | Alias |
|--------|-----------|-------|
| [Termin 1] | [Definicja - co to znaczy w kontekście tego projektu] | [Inne nazwy] |
| [Termin 2] | [Definicja] | [Alias] |

### B. Referencje

**Dokumenty:**
- [Tytuł dokumentu 1] - `link/do/dokumentu`
- [Tytuł dokumentu 2] - `link`

**Standardy:**
- arc42: https://arc42.org/
- C4 Model: https://c4model.com/
- IEEE 42010: https://www.iso.org/standard/50508.html

**Narzędzia:**
- [Narzędzie 1]: [Link + opis]
- [Narzędzie 2]: [Link + opis]

### C. Historia Zmian

| Wersja | Data | Autor | Zmiany |
|--------|------|-------|--------|
| 0.1 | [YYYY-MM-DD] | [Autor] | Draft początkowy |
| 0.2 | [YYYY-MM-DD] | [Autor] | Review feedback incorporated |
| 1.0 | [YYYY-MM-DD] | [Autor] | Wersja zatwierdzona |

### D. Approvals

| Rola | Osoba | Data | Signature |
|------|-------|------|-----------|
| Architect | [Nazwa] | [YYYY-MM-DD] | [Approved / Pending] |
| Tech Lead | [Nazwa] | [YYYY-MM-DD] | [Approved / Pending] |
| Product Owner | [Nazwa] | [YYYY-MM-DD] | [Approved / Pending] |

---

## CHECKLIST KOMPLETNOŚCI

**Przed zatwierdzeniem tego dokumentu, sprawdź:**

**Struktura:**
- [x] Executive Summary (cel, wnioski, zakres, dashboard)
- [x] Kontekst i cele (biznesowy, techniczny, interesariusze, historia)
- [x] Sekcje główne (3-5 sekcji tematycznych, H2 level)
- [x] Diagramy i wizualizacje (minimum 2-3)
- [x] Dane i modele (jeśli applicable)
- [x] Metryki i KPI (techniczne, biznesowe, tracking)
- [x] Identyfikacja problemów (top issues, root cause)
- [x] Rekomendacje (immediate, short-term, long-term)
- [x] Ryzyka i mitigacje (register, contingency)
- [x] Dependencies i założenia
- [x] Timeline i milestones
- [x] Success criteria (acceptance, quality gates)
- [x] Wnioski (mocne/słabe strony, SWOT, rekomendacje)
- [x] Załączniki (słownik, referencje, historia, approvals)

**Jakość:**
- [ ] Wszystkie sekcje wypełnione (brak [placeholder])
- [ ] Diagramy czytelne i opisane
- [ ] Tabele kompletne
- [ ] Cross-references działają (linki do innych dokumentów)
- [ ] Metryki aktualne (data < 1 miesiąc)
- [ ] Spelling/grammar checked
- [ ] Reviewed przez 2+ osoby
- [ ] Approved przez kluczowych stakeholders

**Użyteczność:**
- [ ] Dokument odpowiada na pytania: Co? Dlaczego? Jak? Kto? Kiedy?
- [ ] Executive Summary wystarczające dla high-level overview
- [ ] Akcje są specific, measurable, assignable, realistic, time-bound (SMART)
- [ ] Może być użyty jako źródło prawdy przez zespół

---

**Następny dokument:** [→ Link do następnego dokumentu]  
**Poprzedni dokument:** [← Link do poprzedniego dokumentu]  
**Powiązane:** [→ Link 1], [→ Link 2]

---

## UWAGI UŻYTKOWANIA SZABLONU

**Dla autora wypełniającego szablon:**

1. **Usuń sekcje nieaplikacyjne:** Jeśli jakaś sekcja nie ma sensu dla Twojego dokumentu, usuń ją (np. "Dane i modele" jeśli nie ma modeli danych).

2. **Dostosuj głębokość:** Jeśli potrzebujesz więcej poziomów (H4, H5), dodaj. Jeśli 2 poziomy wystarczą, nie dodawaj H3.

3. **Zachowaj spójność:** Wszystkie dokumenty META powinny mieć podobną strukturę (Executive Summary, sekcje główne, załączniki).

4. **Cross-reference:** Linkuj do innych dokumentów (AS-IS, TO-BE, PROBLEMY, PROCES, etc.).

5. **Checklistę użyj:** Przed submission, przejdź przez checklistę kompletności.

6. **Placeholder values:** Zamień WSZYSTKIE `[placeholders]` na rzeczywiste wartości przed zatwierdzeniem.

7. **Versioning:** Aktualizuj wersję dokumentu przy każdej znaczącej zmianie.

8. **Approval:** Dokument ma status Draft dopóki nie przejdzie review i approval process.
