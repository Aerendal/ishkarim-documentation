---
id: E-082
title: "Wywiad Użytkownika #2 - Product Manager"
type: evidence
evidence_type: survey
date: 2025-12-26

related_documents:
  - PRD-001-V2

source:
  type: user_feedback
  date_collected: 2025-12-21
---

# Wywiad Użytkownika #2 - Product Manager

## Kontekst
Wywiad z Product Managerem pracującym w firmie enterprise software (regulowany sektor - healthcare). Celem było zrozumienie potrzeb PM w zakresie dokumentacji produktowej, szczególnie w kontekście compliance i audytów.

## Metodologia
- **Format**: Wywiad semi-structured (75 minut)
- **Data**: 2025-12-21
- **Profil respondenta**:
  - Rola: Senior Product Manager
  - Firma: Healthcare SaaS (B2B, enterprise)
  - Doświadczenie: 5 lat jako PM
  - Team: Zarządza 2 produktami, 12 devs, 1 tech writer
  - Stack: Jira + Confluence + Productboard
  - Specifics: HIPAA compliance, FDA audyty, wymóg proof trails

## Wyniki

### Top 3 Pain Points

#### 1. Brak Widoczności Completeness
**Cytat**:
> "Przed audytem FDA zadają pytanie: 'Czy każda decyzja jest udokumentowana?' Nie mam POJĘCIA. Muszę przejrzeć 500 stron Confluence i zgadywać, czego brakuje. To koszmarne."

**Szczegóły**:
- FDA/HIPAA wymagają 100% completeness documentation
- Confluence nie pokazuje "coverage" ani luk
- Manual review: 3 tygodnie pracy PM + tech writer przed audytem
- **Koszt**: $40k lost productivity per audit (2× rocznie)
- **Ryzyko**: Non-compliance = kary $100k+

#### 2. Brak Proof Trails dla Decyzji
**Cytat**:
> "Audytor pyta: 'Dlaczego wybraliście architekturę X zamiast Y?' Odpowiadam: 'Mieliśmy ADR... gdzieś... chwila, poszukam...' To wygląda nieprofesjonalnie i ryzykownie."

**Szczegóły**:
- Decyzje są w Confluence, ale bez structured proof trails
- Brak linkowania: Decision → Evidence → Rationale
- Search jest chaotic (10 wersji tego samego ADR)
- **Rezultat**: 40% decyzji nie ma clear evidence trail

#### 3. Quality Gates dla Dokumentacji
**Cytat**:
> "Blokuję release kodu przez Jira. Ale nie mogę zablokować release'u spec bez dokumentacji. Devs pushują features, a ja dowiaduję się z Slacka 2 tygodnie później."

**Szczegóły**:
- Jira ma quality gates dla kodu (code review, tests)
- Confluence NIE MA gates dla docs
- Brak enforcement = docs opóźnione o 2-4 tygodnie vs kod
- **Problem**: Docs debt narastający, brak accountability

### Dodatkowe Insights

#### Compliance Requirements (Healthcare)
**Wymagania FDA/HIPAA**:
1. **Traceability**: Każda decyzja → rationale → evidence
2. **Completeness**: 100% coverage specs dla regulated features
3. **Auditability**: Proof trail must be reconstructable 5 lat wstecz
4. **Version control**: Kto, kiedy, dlaczego zmienił dokument

**Obecne gaps w Confluence**:
- ❌ Brak automatycznego trackingu completeness
- ❌ Brak structured proof trails
- ⚠️ Version history istnieje, ale nie semantyczny (diff, nie "why")
- ❌ Brak widoczności dependencies między decision/evidence/spec

#### Workflow Audytowy (Current)
1. **3 tygodnie przed audytem**: PM + tech writer robią manual review
2. **Week 1**: Identify gaps (przejrzeć 500 stron Confluence)
3. **Week 2**: Fill gaps (napisać brakujące ADRs, specs, test plans)
4. **Week 3**: Cross-check dependencies (manual linking)
5. **Day of audit**: Prayer that wszystko jest kompletne

**Cost**: 2 osoby × 3 tygodnie × 2 audyty/rok = **12 person-weeks = $48k/year**

#### Wishlist Features (Top 5)
1. **Completeness dashboard** - "Red/yellow/green dla każdego produktu"
2. **Proof trail visualization** - "Graph: Decision → Evidence → Spec → Tests"
3. **Quality gates** - "Nie pozwól na release bez 100% completeness"
4. **Audit mode** - "Jeden click = export complete proof trail jako PDF"
5. **Compliance templates** - "Pre-built templates dla FDA/HIPAA/SOC2"

#### Willingness to Pay
**Cytat**:
> "Jeśli tool zaoszczędzi mi 12 person-weeks rocznie i zredukuje ryzyko non-compliance, zapłacę $500-1000/miesiąc. To peanuts vs koszt audytu."

**Budget context**:
- Confluence: $10/user/month × 50 users = $500/month
- Jira: $7/user/month × 50 users = $350/month
- **Ishkarim budget**: $500-1000/month (competitive dla enterprise)

## Implikacje

### Product Requirements (PRD-001-V2)
1. **Must-have**: Completeness tracking + dashboard (FR-020)
2. **Must-have**: Proof trail system (FR-030)
3. **Must-have**: Quality gates (FR-040)
4. **Should-have**: Audit export mode (PDF/HTML z full proof trail)
5. **Nice-to-have**: Compliance templates (FDA/HIPAA/SOC2)

### Target Persona Validation
✅ **Product Manager Persona (Regulated Industries)**:
- Pain: Compliance, auditability, proof trails, completeness visibility
- Jobs to be done: Przygotować audyty, enforce quality, reduce compliance risk
- Current tools: Confluence, Jira, Productboard
- Willingness to pay: $500-1000/miesiąc (team license)
- **Vertical**: Healthcare, fintech, government contractors (high compliance)

### Business Case (BIZ-CASE-001-V2)
- **Target market**: Regulated industries (healthcare, fintech, gov)
- **Market size**: ~50k companies w US (healthcare SaaS alone)
- **ROI dla klienta**: $48k/year oszczędności (audit prep) vs $6-12k/year (Ishkarim)
- **Payback period**: <3 miesiące

### Competitive Advantage
- **Confluence/Notion**: Brak compliance features
- **Ishkarim USP**: "First documentation system designed for regulated industries"

## Dane Raw

### Transkrypt - Kluczowe Fragmenty

**Q: Opisz ostatni audyt FDA.**
> "Koszmar. 2 tygodnie przed audytem dostaję email: 'Please provide complete documentation for Product X, including all design decisions, test coverage, risk assessments.' Panikuję. Confluence search zwraca 500 wyników. Nie wiem, co jest aktualne, co przestarzałe, czego brakuje. Z tech writerem siedzimy 60 godzin (!) i ręcznie budujemy 'audit package' - Google Doc z linkami do Confluence. Audytor patrzy i mówi: 'Where's the evidence for decision Y?' Ja: 'Ummm... let me search...' To upokarzające."

**Q: Co by się stało, gdyby audyt was nie przeszedł?**
> "Worst case: FDA wstrzymuje approval nowych features, co blokuje $5M ARR pipeline. Best case: Warning letter + 6-miesięczny remediation plan. Obydwa scenariusze = katastrofa. Dlatego compliance to #1 priority, ale tooling nas nie wspiera."

**Q: Czy próbowaliście innych narzędzi poza Confluence?**
> "Testowaliśmy Notion - za mało enterprise features. Productboard - świetny do roadmap, słaby do docs. SharePoint - przestarzały. Confluence jest 'najmniej zły', ale nadal brakuje mu compliance DNA. Nikt nie buduje tools dla regulated industries."

**Q: Ile byś zapłacił za tool, który rozwiązuje te problemy?**
> "Audyt kosztuje nas $48k/year w lost productivity + $20k external consultants = $68k/year. Jeśli tool zredukuje to o 70%, oszczędzam $47k/year. Zapłacę $12k/year ($1000/miesiąc) bez mrugnięcia okiem. To 4:1 ROI."

### Metryki z Wywiadu
- **Koszt przygotowania audytu**: $48k/year (internal) + $20k (consultants) = $68k/year
- **Czas na audit prep**: 12 person-weeks/year
- **Ryzyko non-compliance**: $100k-5M (FDA penalties + lost revenue)
- **Dokumenty pod nadzorem**: 500+ pages w Confluence
- **Decyzje bez proof trails**: 40%
- **Willingness to pay**: $500-1000/miesiąc (team), $10k+/year (enterprise)
- **Team size**: 50 users (devs, PMs, QA, tech writers)

### Compliance Checklist (FDA/HIPAA)
Obecny manual checklist używany przed audytami:
- [ ] Każda design decision ma ADR
- [ ] Każdy ADR ma evidence (benchmarks, user research, prototypes)
- [ ] Każdy requirement ma test coverage
- [ ] Każdy risk ma mitigation plan
- [ ] Każda zmiana ma change log
- [ ] Version history jest complete
- [ ] Dependencies są udokumentowane
- [ ] **Manual effort**: 3 tygodnie, 2 osoby

**Ishkarim automation**: ✅ Wszystko to można zautomatyzować via proof system + gap detection
