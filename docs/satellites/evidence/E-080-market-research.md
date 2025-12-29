---
id: E-080
title: "Badanie Rynku - Narzędzia Dokumentacji Semantycznej"
type: evidence
evidence_type: analysis
date: 2025-12-26

related_documents:
  - VISION-001-V2
  - BIZ-CASE-001-V2

source:
  type: external_research
  date_collected: 2025-12-26
---

# Badanie Rynku - Narzędzia Dokumentacji Semantycznej

## Kontekst
W ramach walidacji unikalności koncepcji Ishkarim oraz identyfikacji luk rynkowych, przeprowadzono analizę 10 konkurencyjnych narzędzi dokumentacji. Celem było zrozumienie, które funkcjonalności są standardem branżowym, a które stanowią innowację Ishkarim.

## Metodologia
- **Okres badania**: Listopad-Grudzień 2025
- **Źródła**: Strony produktów, dokumentacja publiczna, darmowe wersje trial, recenzje G2/Capterra
- **Kryteria oceny**:
  - Wsparcie dla relacji semantycznych między dokumentami
  - Automatyczna detekcja luk w dokumentacji
  - System dowodów (proof-based documentation)
  - Wizualizacja grafu zależności
  - Trackowanie completeness
  - Bramki jakości (quality gates)

## Wyniki

### Narzędzia Przeanalizowane
1. **Confluence** (Atlassian) - wiki enterprise
2. **Notion** - workspace all-in-one
3. **Obsidian** - personal knowledge base
4. **Roam Research** - networked thought
5. **Coda** - docs + apps
6. **Docusaurus** - docs dla projektów open source
7. **GitBook** - dokumentacja produktowa
8. **MkDocs** - static site generator
9. **Nuclino** - collaborative wiki
10. **Tettra** - internal knowledge base

### Gap Analysis - Kluczowe Wnioski

| Feature | Confluence | Notion | Obsidian | Roam | Coda | **Ishkarim** |
|---------|------------|--------|----------|------|------|--------------|
| Linki między dokumentami | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Grafy zależności | ⚠️ (plugin) | ❌ | ✅ | ✅ | ❌ | ✅ |
| Semantyczne relacje | ❌ | ❌ | ⚠️ (tags) | ⚠️ (tags) | ❌ | ✅ |
| Gap detection | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Proof system | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Completeness tracking | ❌ | ⚠️ (manual) | ❌ | ❌ | ⚠️ (manual) | ✅ |
| Quality gates | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Automatyczna walidacja | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

**Legenda**: ✅ pełne wsparcie | ⚠️ częściowe/manualne | ❌ brak

### Kluczowe Luki Rynkowe
1. **Brak proof-based systems** - żadne narzędzie nie wymusza dowodów dla twierdzeń
2. **Manualne sprawdzanie completeness** - brak automatyzacji detekcji luk
3. **Słabe trackowanie zależności** - podstawowe linki, bez semantyki
4. **Brak bramek jakości** - nie można zablokować publikacji niekompletnych docs
5. **Wizualizacje podstawowe** - grafy dostępne tylko w Obsidian/Roam, bez analizy luk

## Implikacje
1. **Unikalna propozycja wartości**: Ishkarim wypełnia 5 kluczowych luk rynkowych
2. **Strategia pozycjonowania**: "First proof-based documentation system"
3. **Target users**: Teams wymagające compliance, auditability, high-quality docs (tech writers, PM, regulated industries)
4. **Konkurencja**: Obsidian + Roam (grafy) to najbliżsi konkurenci, ale bez proof system
5. **Go-to-market**: Positioning jako nadbudowa semantyczna nad istniejącymi narzędziami (import z Markdown)

## Dane Raw

### Cytaty z Recenzji Użytkowników

**Confluence (G2 Reviews)**:
> "We spend hours manually checking if all sections are filled. There's no way to enforce completeness." - PM, Enterprise Software

**Notion**:
> "Great for notes, but terrible for tracking what's missing across 200+ pages." - Technical Writer, SaaS

**Obsidian**:
> "Love the graph view, but I still have to manually verify dependencies are documented." - Developer, Open Source

### Cennik Konkurencji
- Confluence: $5.50/user/month (Standard)
- Notion: $10/user/month (Plus)
- Obsidian: $50/user/year (Commercial License)
- Roam Research: $15/user/month
- Coda: $10/user/month

**Ishkarim pricing strategy**: Free dla personal use, $8-12/user/month dla teams (competitive)

### Wskaźniki Popularności
- Confluence: ~60k enterprise customers
- Notion: ~30M users (2024)
- Obsidian: ~1M active users
- Roam Research: ~100k users

**Target market share**: 0.1% w ciągu 2 lat = 30k users (realistyczne dla niche tool)
