---
id: E-081
title: "Wywiad Użytkownika #1 - Technical Writer"
type: evidence
evidence_type: survey
date: 2025-12-26

related_documents:
  - PRD-001-V2

source:
  type: user_feedback
  date_collected: 2025-12-20
---

# Wywiad Użytkownika #1 - Technical Writer

## Kontekst
W ramach user research przeprowadzono wywiad z doświadczonym technical writerem pracującym w firmie SaaS (150+ osób). Celem było zidentyfikowanie pain points związanych z tworzeniem i utrzymywaniem dokumentacji technicznej.

## Metodologia
- **Format**: Wywiad semi-structured (60 minut)
- **Data**: 2025-12-20
- **Profil respondenta**:
  - Rola: Senior Technical Writer
  - Firma: B2B SaaS (fintech)
  - Doświadczenie: 7 lat
  - Team: 3 technical writers, wspiera 15 devs + 5 PMs
  - Stack: Confluence + Google Docs + GitHub wiki
  - Odpowiada za: API docs, user guides, internal documentation

## Wyniki

### Top 3 Pain Points

#### 1. Brak Automatycznego Trackingu Zależności
**Cytat**:
> "Kiedy PM zmienia feature spec, nie mam pojęcia które 10 innych dokumentów muszę zaktualizować. Spędzam godziny na ręcznym szukaniu przez Confluence."

**Szczegóły**:
- Zmiana w 1 dokumencie wymaga update 5-15 powiązanych docs
- Brak widoczności impact chain
- Manual searching przez search bar + memory
- **Czas stracony**: ~5h/tydzień na hunting dependencies

#### 2. Manualna Walidacja Completeness
**Cytat**:
> "Przed każdym release robię checklist: czy wszystkie sekcje wypełnione? Czy są screenshots? Czy API endpoints udokumentowane? To 2 godziny czystej mechanicznej pracy KAŻDEGO dnia."

**Szczegóły**:
- Pre-release checklist: 47 pozycji
- Sprawdzanie ręczne każdej sekcji w 20-30 dokumentach
- **Czas stracony**: 2h/dzień = 10h/tydzień
- Błędy ludzkie: ~3 gaps per release wychodzi do produkcji

#### 3. Brak Quality Gates
**Cytat**:
> "Developerzy pushują kod bez docs. PM publishuje spec bez przykładów. Nie mogę zablokować ich, bo nie mam mechanizmu enforcement. To frustrujące."

**Szczegóły**:
- Brak sposobu na wymuszenie kompletności przed publikacją
- Confluence nie ma bramek jakości
- Rely na "dobre intencje" + manual review (nieśkalowalne)
- **Rezultat**: 40% dokumentów niekompletnych w momencie publikacji

### Dodatkowe Insights

#### Workflow Obecny
1. PM pisze spec w Google Docs
2. Technical writer przenosi do Confluence + dodaje szczegóły
3. Devs updatują API reference w GitHub wiki
4. Tech writer synchronizuje wszystko ręcznie
5. Pre-release: 2h manual validation

**Problemy**:
- 3 źródła prawdy (Google Docs, Confluence, GitHub)
- No single source of truth
- Manual sync = delays + errors

#### Narzędzia Używane
- **Confluence**: Main docs platform
- **Google Docs**: Drafts + collaboration
- **GitHub wiki**: API reference
- **Loom**: Video walkthroughs
- **Grammarly**: Spell check

**Braki**:
- Brak dependency tracking
- Brak completeness validation
- Brak proof system
- No graph visualization

#### Wishlist Features (Top 5)
1. **Automatyczna detekcja luk** - "Powiedz mi, czego brakuje"
2. **Dependency graph** - "Pokaż mi, co muszę zaktualizować"
3. **Quality gates** - "Nie pozwól publishować niekompletnych docs"
4. **Proof enforcement** - "Wymuś screenshots + examples dla każdego feature"
5. **Single source of truth** - "Jeden system zamiast 3"

## Implikacje

### Product Requirements (PRD-001-V2)
1. **Must-have**: Gap detection engine (FR-020)
2. **Must-have**: Dependency tracking + visualization (FR-010)
3. **Must-have**: Quality gates (FR-040)
4. **Should-have**: Proof system (FR-030)
5. **Nice-to-have**: Import z Confluence/Google Docs

### Value Proposition
- **Oszczędność czasu**: 2h/dzień (validation) + 1h/dzień (dependency hunting) = **15h/tydzień = 60h/miesiąc**
- **ROI calculation**: 60h × $50/h = **$3000/miesiąc oszczędności per tech writer**
- **Quality improvement**: Redukcja gaps w produkcji z 40% do <5%

### Target Persona Validation
✅ **Technical Writer Persona**:
- Pain: Manual validation, dependency tracking, quality enforcement
- Jobs to be done: Ensure completeness, maintain consistency, reduce errors
- Current tools: Confluence, Google Docs, GitHub wiki
- Willingness to pay: "If it saves me 15h/week, I'd pay $50/month myself"

## Dane Raw

### Transkrypt - Kluczowe Fragmenty

**Q: Opisz typowy pre-release workflow.**
> "Tydzień przed release dostaję ping od PM: 'Docs ready?'. Wtedy zaczynam 2-dniowy marathon. Otwieram checklist w Excelu - 47 pozycji. Dla każdego feature sprawdzam: (1) Czy jest user guide? (2) Czy są screenshots? (3) Czy API endpoint jest w docs? (4) Czy są code examples? To jest CZYSTA mechaniczna praca. Komputer powinien to robić, nie ja."

**Q: Co się dzieje, jak znajdziesz gap?**
> "Slack do PM albo deva: 'Hey, brakuje screenshot dla feature X'. Czekam 2h-2 dni na odpowiedź. W międzyczasie blokuję release albo puszczam z luką (zależy od pressure). 30% gaps naprawiam sama, robiąc screenshots w staging."

**Q: Jak trackujesz zależności między dokumentami?**
> "W głowie + notes. Serio. Mam prywatny Google Doc 'Doc Dependencies Map' - lista 200+ linków. Jak coś się zmienia, ctrl+F przez ten doc, potem manual update. To absurdalne, ale nie mam lepszego sposobu."

**Q: Gdybyś mogła stworzyć idealny tool, co by miał?**
> "Otworzyłabym dokument, system pokazałby mi: (1) Co brakuje (auto-detected gaps), (2) Które inne docs są powiązane (graph view), (3) Czerwony alert jak próbuję publishować niekompletny doc (quality gate). Bonus: AI suggestions co dodać. Zapłaciłabym dużo za taki tool."

### Metryki z Wywiadu
- **Czas na dependency hunting**: 5h/tydzień
- **Czas na manual validation**: 10h/tydzień
- **Błędy per release**: 3 gaps wychodzą do produkcji
- **Dokumenty pod nadzorem**: ~150 pages w Confluence
- **Pre-release checklist**: 47 pozycji
- **Willingness to pay**: $50/miesiąc (personal), $200+/miesiąc (team license)
