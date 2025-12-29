# EXPERIMENT-LOG: [Experiment ID] - [Short Description]

---

## Document Metadata

```yaml
id: EXPERIMENT-[XXX]
doctype: EXPERIMENT-LOG
status: draft  # draft | in-progress | completed | failed | inconclusive
version: 1.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
owner: [Owner Name]
project: [Project Name]
experiment_id: EXP-[XXX]
hypothesis_id: HYPOTHESIS-[XXX]
```

---

## Cross-References

```yaml
dependencies:
  - id: HYPOTHESIS-DOC
    type: requires
    reason: "Eksperyment waliduje konkretną hipotezę"

impacts:
  - id: RESEARCH-FINDINGS
    type: blocks
    reason: "Research Findings agregują wyniki z wielu eksperymentów"
  - id: ADR
    type: informs
    reason: "Dane eksperymentalne wspierają decyzje architektoniczne"
  - id: TECH-DEBT-REGISTER
    type: influences
    reason: "Eksperyment może ujawnić problemy wymagające refaktoringu"
```

---

## SEC-EXP-HYPOTHESIS: Link do hipotezy

### Hipoteza testowana
**ID:** [HYPOTHESIS-XXX]
**Stwierdzenie:** [Krótkie powtórzenie hipotezy H1]

### Success criteria (z hipotezy)
- [ ] [Kryterium 1]
- [ ] [Kryterium 2]
- [ ] [Kryterium 3]

---

## SEC-EXP-SETUP: Setup eksperymentu

### Środowisko
- **Platform:** [AWS/Azure/GCP/On-premise/etc.]
- **Instance type:** [t3.medium, etc.]
- **OS:** [Linux/Windows/macOS]
- **Network:** [Configuration]

### Konfiguracja
```yaml
# Example configuration
parameter_1: value_1
parameter_2: value_2
```

### Dataset
- **Source:** [Źródło danych]
- **Size:** [X records, Y GB]
- **Characteristics:** [Opis charakterystyki danych]

### Narzędzia
- [Narzędzie 1]: [Wersja]
- [Narzędzie 2]: [Wersja]

### Baseline
[Opis baseline/control group dla porównania]

---

## SEC-EXP-PROCEDURE: Procedura wykonania

### Kroki eksperymentu
1. [Krok 1 - szczegółowy opis]
2. [Krok 2 - szczegółowy opis]
3. [Krok 3 - szczegółowy opis]

### Variables
**Independent variables (controlled):**
- [Zmienna 1]: [Wartości testowane]
- [Zmienna 2]: [Wartości testowane]

**Dependent variables (measured):**
- [Zmienna 1]: [Jak mierzona]
- [Zmienna 2]: [Jak mierzona]

**Control variables (constant):**
- [Zmienna 1]: [Wartość stała]
- [Zmienna 2]: [Wartość stała]

---

## SEC-EXP-OBSERVATIONS: Obserwacje (timestamped)

### [YYYY-MM-DD HH:MM] - [Milestone/Event Name]
**Status:** [Setup | Running | Paused | Issue detected | Completed]

**Observations:**
- [Obserwacja 1]
- [Obserwacja 2]

**Actions taken:**
- [Akcja 1]
- [Akcja 2]

---

### [YYYY-MM-DD HH:MM] - [Milestone/Event Name]
**Status:** [Status]

**Observations:**
- [Obserwacja 1]
- [Obserwacja 2]

**Actions taken:**
- [Akcja 1]
- [Akcja 2]

---

### Anomalie i problemy
| Timestamp | Problem | Impact | Resolution |
|-----------|---------|--------|------------|
| YYYY-MM-DD HH:MM | [Problem] | [High/Medium/Low] | [Jak rozwiązano] |
|  |  |  |  |

---

## SEC-EXP-DATA: Dane i metryki

### Raw Data
[Link do raw data files, notebooks, databases]
- [Dataset 1]: [Lokalizacja]
- [Dataset 2]: [Lokalizacja]

### Metryki zebrane

| Metryka | Baseline | Experiment | Delta | Target | Status |
|---------|----------|------------|-------|--------|--------|
| [Metryka 1] | [Wartość] | [Wartość] | [±X%] | [Target] | ✅/❌/⚠️ |
| [Metryka 2] | [Wartość] | [Wartość] | [±X%] | [Target] | ✅/❌/⚠️ |

### Visualizations
[Wykresy, grafy, dashboardy - embed lub link]
- [Chart 1]: [Link lub embed]
- [Chart 2]: [Link lub embed]

---

## SEC-EXP-ANALYSIS: Analiza wyników

### Statistical Analysis
**Metoda:** [T-test, ANOVA, Chi-square, etc.]
**Confidence level:** [95%, 99%]
**p-value:** [Wartość]
**Significance:** [Statistically significant: Yes/No]

### Interpretacja wyników
[Szczegółowa interpretacja danych - co oznaczają wyniki]

### Correlation vs Causation
[Czy obserwujemy korelację czy przyczynowość? Uzasadnienie]

### Threats to Validity
**Internal validity:**
- [Threat 1]

**External validity:**
- [Threat 1]

**Mitigation:**
- [Jak zmitygowano zagrożenia]

---

## SEC-EXP-CONCLUSION: Wnioski

### Wynik względem hipotezy

**Hipoteza H1:** [Powtórzenie hipotezy]

**Verdict:**
- ✅ **POTWIERDZONA** - Dane wspierają H1
- ❌ **ODRZUCONA** - Dane wspierają H0
- ⚠️ **NIEKONKLUZYWNA** - Wyniki mieszane/niewystarczające dane

### Success Criteria Assessment
- [x] [Kryterium 1]: ✅ Spełnione - [Szczegóły]
- [ ] [Kryterium 2]: ❌ Niespełnione - [Szczegóły]
- [x] [Kryterium 3]: ⚠️ Częściowo - [Szczegóły]

### Kluczowe odkrycia
1. [Odkrycie 1]
2. [Odkrycie 2]
3. [Odkrycie 3]

### Niespodzianki
[Obserwacje, które nie były przewidziane w hipotezie]

### Limitations
[Ograniczenia eksperymentu, które mogą wpływać na wnioski]

---

## SEC-EXP-NEXT-STEPS: Kolejne kroki

### Immediate actions
- [ ] [Akcja 1]
- [ ] [Akcja 2]

### Follow-up experiments
- [ ] [Eksperyment follow-up 1]
- [ ] [Eksperyment follow-up 2]

### Documentation updates
- [ ] Update [HYPOTHESIS-DOC] with validated/invalidated status
- [ ] Create [RESEARCH-FINDINGS] aggregating multiple experiments
- [ ] Create [ADR] if decision is needed

### Recommendations
**If hypothesis confirmed:**
- [Rekomendacja 1]
- [Rekomendacja 2]

**If hypothesis rejected:**
- [Rekomendacja 1]
- [Rekomendacja 2]

---

## EVIDENCE: Dowody i artefakty

### Artifacts generated
- [Artifact 1]: [Link]
- [Artifact 2]: [Link]

### Screenshots/Recordings
[Screenshots kluczowych momentów eksperymentu]

### Code/Scripts
[Linki do kodu użytego w eksperymencie]
```
Repository: [Link]
Branch: [Branch name]
Commit: [Commit hash]
```

---

## CHANGELOG: Historia zmian

| Data | Wersja | Autor | Zmiana |
|------|--------|-------|--------|
| YYYY-MM-DD | 1.0 | [Imię Nazwisko] | Initial creation |
| YYYY-MM-DD | 1.1 | [Imię Nazwisko] | Experiment started |
| YYYY-MM-DD | 2.0 | [Imię Nazwisko] | Experiment completed, results added |
|  |  |  |  |

---

## Notatki i uwagi

[Miejsce na dodatkowe notatki, lessons learned, refleksje]

---

**Template version:** 1.0
**Based on:** PROPOZYCJA-1-Research-Branch-Templates.md
**Group:** research
**Domain:** innovation
