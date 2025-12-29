---
id: E-083
title: "Wywiad Użytkownika #3 - Developer"
type: evidence
evidence_type: survey
date: 2025-12-26

related_documents:
  - PRD-001-V2

source:
  type: user_feedback
  date_collected: 2025-12-22
---

# Wywiad Użytkownika #3 - Developer

## Kontekst
Wywiad z Senior Software Developerem pracującym w zespole backend (fintech startup, 50 osób). Celem było zrozumienie perspektywy developera jako konsumenta dokumentacji oraz kontrybutora.

## Metodologia
- **Format**: Wywiad semi-structured (60 minut)
- **Data**: 2025-12-22
- **Profil respondenta**:
  - Rola: Senior Backend Developer
  - Firma: Fintech startup (Series B)
  - Doświadczenie: 8 lat jako developer
  - Team: 6 backend devs, 4 frontend devs, 2 PMs
  - Stack tech: Python, PostgreSQL, AWS, GitHub
  - Stack docs: Confluence + GitHub wiki + Notion (chaos)
  - Odpowiada za: API development, code reviews, technical design docs

## Wyniki

### Top 3 Pain Points

#### 1. Outdated Documentation
**Cytat**:
> "50% czasu gubię na czytaniu docs, które są przestarzałe. Próbuję zintegrować API endpoint według dokumentacji z Confluence, ale dostaję 404. Sprawdzam kod - endpoint został zmieniony 3 miesiące temu, docs nie. Frustrated? Hell yeah."

**Szczegóły**:
- **Częstotliwość**: 2-3× tygodniowo napotyka outdated docs
- **Impact**: 3-4h/tydzień stracone na debugging docs vs reality
- **Root cause**: Docs updatowane asynchronicznie vs kod
- **Frustration level**: 8/10 ("to mnie najbardziej wkurza w pracy")

#### 2. Brak Bidirectional Links Code ↔ Docs
**Cytat**:
> "Zmieniam funkcję w kodzie. Gdzie jest dokumentacja dla tej funkcji? Nie mam pojęcia. Musiałbym przeszukać całe Confluence. W 99% przypadków nie updatuję docs, bo to zbyt trudne. Sorry not sorry."

**Szczegóły**:
- **Problem**: Brak mechanizmu łączącego kod → docs
- **Obecne rozwiązanie**: Manual search (nikt tego nie robi)
- **Rezultat**: 80% zmian w kodzie NIE updatuje docs
- **Tech debt**: Narastający gap między kodem a dokumentacją

#### 3. Brak Automatyzacji Walidacji Docs
**Cytat**:
> "Mamy CI/CD dla kodu - testy, linting, coverage. Dlaczego nie mamy tego dla docs? Chciałbym, żeby bot krzyczał: 'Hej, dodałeś nowy endpoint, gdzie jest dokumentacja?!' Automation > humans."

**Szczegóły**:
- **CI/CD dla kodu**: 100% automated (GitHub Actions, pytest, black, mypy)
- **CI/CD dla docs**: 0% automated
- **Wishlist**: Pre-commit hook sprawdzający completeness docs
- **Benefit**: "Enforcement by tooling, not by nagging PMs"

### Dodatkowe Insights

#### Developer Workflow (Obecny)
1. **Pisze kod** (Python, 80% czasu)
2. **Code review** (GitHub, 10% czasu)
3. **Docs** (Confluence, <5% czasu - "jak PM przypomni")
4. **Debugging** (często walka z outdated docs, 5% czasu)

**Problem**: Docs są "afterthought", nie "first-class citizen"

#### Narzędzia Używane (Stack Chaos)
- **GitHub wiki**: API reference (50% outdated)
- **Confluence**: Architecture docs, design docs (70% outdated)
- **Notion**: Team notes, brainstormy (never updated)
- **Docstrings w kodzie**: Jedyne źródło prawdy (ale nie wystarczające)

**Chaos**:
> "Mamy 3 sources of truth, więc de facto 0 sources of truth. Dla każdego API muszę sprawdzić: (1) GitHub wiki, (2) Confluence, (3) Kod. Wszystkie 3 mówią co innego. Która jest aktualna? Kod. Zawsze kod."

#### Wishlist Features (Developer Perspective)

1. **Bidirectional links Code ↔ Docs**
   - Zmiana funkcji w kodzie → highlight dokumentów do update
   - Link w docs → jump to kod (podobnie jak Javadoc/Doxygen, ale lepiej)

2. **Automated validation w CI/CD**
   - Pre-commit hook: "Dodałeś nowy endpoint? Dodaj docs."
   - PR blocker: "API nie ma docs → PR rejected"
   - Coverage report dla docs (jak test coverage)

3. **Docs as code**
   - Markdown w repo (nie Confluence)
   - Git history dla docs (nie Confluence version history)
   - Review docs jak kod (PR, not Confluence comments)

4. **Auto-generated skeleton docs**
   - Parser wyszukuje nowe API endpoints
   - Generuje szkielet docs (title, params, empty sections)
   - Dev wypełnia details, bot weryfikuje completeness

5. **Graph view dependencies**
   - "Zmieniam moduł Auth. Które docs są affected?"
   - Visual graph showing impact radius

#### Integracja z Workflow
**Cytat**:
> "Jeśli tool wymaga opuszczenia IDE/terminal, nie będę go używać. Docs muszą być w moim workflow: commit → bot check → fail jeśli brakuje docs → fix → push. Zero friction."

**Key requirement**: CLI/Git hooks/IDE plugins, NIE TYLKO GUI

## Implikacje

### Product Requirements (PRD-001-V2)

1. **Must-have**: Bidirectional linking (FR-010 extension)
   - Link docs → code (via file paths)
   - Alert przy zmianie kodu: "Affected docs: X, Y, Z"

2. **Must-have**: CI/CD integration (FR-050 - nowy requirement!)
   - Pre-commit hooks
   - PR status checks (docs completeness)
   - GitHub Actions / GitLab CI integration

3. **Should-have**: Markdown-first (FR-060 - nowy requirement!)
   - Docs w repo (Git version control)
   - Import/export Markdown
   - Confluence jako secondary output

4. **Should-have**: Auto-skeleton generation (FR-070 - nowy requirement!)
   - Parser kodu (Python, JS, etc.)
   - Generate empty doc templates dla nowych funkcji/endpoints
   - Dev fills details

5. **Nice-to-have**: CLI + IDE plugins
   - `ishkarim check` w terminalu
   - VS Code extension showing doc status

### Target Persona Validation
✅ **Developer Persona**:
- Pain: Outdated docs, brak bidirectional links, brak automation
- Jobs to be done: Quickly find relevant docs, update docs with minimal friction, trust docs are current
- Current tools: GitHub, Confluence (reluctantly), IDE
- Workflow preference: CLI/Git > GUI
- Willingness to pay: "If it's mandated by company, sure. I won't pay personally."

### Architecture Implications (ADR-003?)

**Requirement**: Ishkarim musi wspierać "docs as code" model
- Markdown files w Git repo
- Parser integrujący się z codebase
- Hooks dla Git (pre-commit, pre-push)
- API dla CI/CD tools (GitHub Actions)

**Konkurencja**: Docusaurus, MkDocs robią "docs as code", ale bez:
- Semantic linking
- Gap detection
- Proof system
- Bidirectional code-docs links

**Ishkarim USP dla devs**: "Docs as code + semantic validation + automation"

## Dane Raw

### Transkrypt - Kluczowe Fragmenty

**Q: Jak często czytasz dokumentację w pracy?**
> "Daily. Ale to frustrating experience. Szukam 'How to authenticate API calls' w Confluence search. Dostaję 15 wyników, half są z 2022 roku, half są drafts. Który jest aktualny? Trial and error. Ostatecznie przechodzę do kodu i czytam implementation. Docs są useless 50% czasu."

**Q: Dlaczego nie updatujesz docs jak zmieniasz kod?**
> "Szczerze? Bo to pain. Muszę: (1) Znaleźć właściwy doc w Confluence (5 minut searching), (2) Otworzyć editor (slow, clunky), (3) Znaleźć właściwą sekcję (kolejne 5 minut), (4) Edit + save (często konflikt version, ktoś inny też editował). Total: 15-20 minut. Vs code change: 2 minuty. Ratio: 10:1. Ekonomicznie się nie opłaca."

**Q: Co by cię zmotywowało do updatowania docs?**
> "Automation. Gdyby bot powiedział: 'Hej, zmieniłeś AuthService.login(), dodaj 3 zdania do docs/auth.md, inaczej PR rejected.' OK, dodam 3 zdania. To 2 minuty, not 20. Plus byłoby w Markdown w repo, więc git diff pokazuje zmiany - review docs jak kod. To fair."

**Q: Czy używałbyś GUI tool jak Ishkarim, czy wolisz CLI?**
> "Zależy. Do browsing docs - GUI jest OK (graph view sounds cool). Do updatowania docs - CLI/Git. Hybrid approach: GUI do exploration, Git/CLI do contribution. Best of both worlds."

**Q: Czy zapłaciłbyś za taki tool?**
> "Personally? No. Ale firma powinna. Jeśli tool zmusi wszystkich do updatowania docs (via CI/CD enforcement), docs będą aktualne, co zaoszczędzi mi 4h/tydzień debugging. Worth it dla firmy."

### Metryki z Wywiadu
- **Czas stracony na outdated docs**: 3-4h/tydzień
- **Częstotliwość napotykania stale docs**: 2-3×/tydzień
- **% zmian kodu NIE updatujących docs**: 80%
- **Czas na update docs (current flow)**: 15-20 minut
- **Czas na update docs (desired flow)**: 2-5 minut
- **Willingness to pay**: $0 (personal), $20-50/user/month (company)
- **Preferred workflow**: CLI/Git > GUI

### Developer Wishlist - Priorytetyzacja (MoSCoW)

**Must Have**:
1. Bidirectional code-docs links
2. CI/CD integration (PR blockers)
3. Markdown support (docs as code)

**Should Have**:
4. Auto-skeleton generation
5. CLI tools

**Could Have**:
6. IDE plugins (VS Code, IntelliJ)
7. Git hooks (pre-commit)

**Won't Have (for MVP)**:
8. AI auto-documentation (too ambitious)
