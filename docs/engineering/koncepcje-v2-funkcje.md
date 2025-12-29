---
id: CONCEPTS-001-V2-FUNCTIONS
title: "Specyfikacje Funkcji (Storytelling Approach)"
type: concepts-functions
parent: CONCEPTS-001-V2
domain: engineering
status: draft
created: 2025-12-26
---

# Część 3: Specyfikacje Funkcji (Storytelling Approach)

← [Poprzednia: Mapowanie](./koncepcje-v2-mapowanie.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Przykłady →](./koncepcje-v2-przyklady.md)

---

## Wprowadzenie: Dlaczego Storytelling?

Ten dokument **nie** zawiera specyfikacji w formacie "Input → Process → Output".

Każda funkcja jest opisana jako **narracja** odpowiadająca na pytania:
1. **Dlaczego ta funkcja istnieje?** (Problem domain)
2. **Jakie problemy rozwiązuje?** (Use cases)
3. **Jakie były alternatywy?** (Options considered)
4. **Dlaczego wybraliśmy to podejście?** (Rationale)
5. **Jakie są konsekwencje wyboru?** (Trade-offs)

---

## Spis Treści

### Moduł 5: Gate Management (F-081 do F-085)
- [F-081: Define Input/Output Gates](#f-081-define-inputoutput-gates)
- [F-082: Evaluate Gates](#f-082-evaluate-gates)
- [F-083: Propagate Changes Through Gates](#f-083-propagate-changes-through-gates)
- [F-084: Detect Gate Blockers](#f-084-detect-gate-blockers)

### Moduł 6: Decision Graph Manager (F-086 do F-090)
- [F-086: Create Decision Graph](#f-086-create-decision-graph)
- [F-087: Register All Options](#f-087-register-all-options)
- [F-088: Capture Context T₀](#f-088-capture-context-t₀)
- [F-089: Register Comparative Justifications](#f-089-register-comparative-justifications)
- [F-090: Visualize Decision Graph](#f-090-visualize-decision-graph)

### Moduł 7: Storytelling Validator (F-093 do F-095)
- [F-093: Validate Storytelling](#f-093-validate-storytelling)
- [F-094: Generate Gap E180](#f-094-generate-gap-e180)
- [F-095: Provide Storytelling Templates](#f-095-provide-storytelling-templates)

### Moduł 8: Evidence Tracker (F-097 do F-100)
- [F-097: Create Evidence Note](#f-097-create-evidence-note)
- [F-098: Link Evidence to Decision](#f-098-link-evidence-to-decision)
- [F-100: Detect Missing Evidence](#f-100-detect-missing-evidence-e170)

### Moduł 9: Impl Log Manager (F-102 do F-104)
- [F-102: Create Implementation Log](#f-102-create-implementation-log)
- [F-103: Add Entry to Log](#f-103-add-entry-to-log)
- [F-104: Link Log to Decision](#f-104-link-log-to-decision)

### Moduł 10: Post-mortem Generator (F-107 do F-111)
- [F-107: Create Post-mortem](#f-107-create-post-mortem-document)
- [F-108: Generate Post-mortem from Log](#f-108-generate-post-mortem-from-impl-log)
- [F-110: Monitor Re-evaluation Triggers](#f-110-monitor-re-evaluation-triggers)
- [F-111: Detect Missing Post-mortem](#f-111-detect-missing-post-mortem-e200)

### Moduł 11: Document Lifecycle (F-112 do F-114)
- [F-112: Immutable Document Versioning](#f-112-immutable-document-versioning)
- [F-113: Generate Changelog](#f-113-generate-changelog)
- [F-114: Manage Document Gates](#f-114-manage-document-gates)

---

# Moduł 5: Gate Management

## F-081: Define Input/Output Gates

### Historia funkcji

Początkowo planowaliśmy zwykły system linków między dokumentami (Opcja A): dokument A ma pole `dependencies: [doc-B, doc-C]`. To podejście działa w małych projektach, ale ma fundamentalny problem — **linki są pasywne**. Gdy zmienisz doc-B, system nie wie że doc-A może być outdated.

Rozważaliśmy dependency tracking jak w build systemach (Opcja B): każdy dokument ma timestamp, rebuild jeśli dependency nowszy. Problem: **rebuild czego?** Dokumentacja to nie kod — nie możemy "przekompilować" dokumentu. Ludzie muszą ręcznie zweryfikować czy zmiana w doc-B wpływa na doc-A.

Wybraliśmy **aktywne bramki wejścia/wyjścia** (Opcja C), inspirowane:
- **Dataflow programming** (inputs → transformation → outputs)
- **Event sourcing** (change events propagate)
- **Build graphs** (dependency tracking) + **semantic meaning** (typ zależności)

**Dlaczego bramki, a nie linki?**
1. **Semantic clarity**: `type: requires` vs `type: informs` — różne poziomy criticality
2. **Propagation**: Zmiana w doc-B **automatycznie** tworzy TODO dla doc-A (jeśli bramka `impacts`)
3. **Blocking**: Bramka `blocks` może zatrzymać workflow (np. implementacja bez zatwierdzonego ADR)
4. **Auditability**: Historia zmian propagowanych przez bramki = audit trail

### Kluczowe decyzje

**Q: Dlaczego bramki globalne + wewnętrzne?**
**A**: Dokumenty mają:
- **External dependencies** (między dokumentami): ADR → RFC → Implementation
- **Internal dependencies** (między sekcjami): "Assumptions" wpływa na "Architecture"

Początkowo chcieliśmy tylko globalne. Incident: Zmiana budżetu w sekcji "Assumptions" nie wywołała update w "Architecture" (bo to te same dokument). Dodaliśmy bramki wewnętrzne.

**Q: Dlaczego `status_constraint`?**
**A**: Bramka `requires ADR-003` — ale w jakim statusie? Draft? Approved? Status_constraint = `[approved, deployed]` oznacza: "wymagam ADR-003 w statusie approved LUB deployed".

**Q: Dlaczego `cascade: bool`?**
**A**: Bramka `informs` czasem to "FYI" (nie blokuje), czasem "update required". Flag `cascade=true` → zmiana generuje TODO. `cascade=false` → tylko notification.

### Funkcja w praktyce

```python
class GateManager:
    def define_gate(
        self,
        source: DocumentRef,
        target: DocumentRef,
        gate_type: Literal["input", "output", "internal"],
        connection_type: Literal["requires", "blocks", "informs", "impacts"],
        status_constraint: List[str] = [],
        cascade: bool = False,
        reason: str = "",
        evidence: List[str] = []
    ) -> Gate:
        """
        Historia: Początkowo było `add_dependency(source, target)`.
        Problem: Brak semantyki (co to znaczy dependency?).

        V2: `define_gate(...)` z typem połączenia + constraints + reason.

        Przykład:
        define_gate(
            source="ADR-005",
            target="IMPL-CART-DB",
            gate_type="output",
            connection_type="blocks",
            status_constraint=["approved"],
            reason="Implementation nie może ruszyć bez zatwierdzonej architektury"
        )
        → Jeśli ADR-005.status != "approved", IMPL-CART-DB ma lukę E150
        """
        gate = Gate(
            id=generate_gate_id(),
            source=source,
            target=target,
            gate_type=gate_type,
            connection_type=connection_type,
            status_constraint=status_constraint,
            cascade=cascade,
            reason=reason,
            evidence=evidence
        )

        # Validate gate is allowed by document type schema
        if not self._is_gate_allowed(gate):
            raise ValidationError(f"Gate type {connection_type} not allowed between {source.type} and {target.type}")

        self.gate_registry.add(gate)
        return gate
```

### Konsekwencje wyboru

**Akceptujemy**:
- **Więcej metadanych**: Każda bramka = 5-10 pól (source, target, type, constraint, reason, evidence)
- **Złożoność**: System musi śledzić setki bramek, walidować constraints, propagować zmiany

**Zyskujemy**:
- **Explicitność**: Każda zależność ma jasną semantykę
- **Automation**: Zmiana → propagacja → TODO generation
- **Auditability**: "Dlaczego doc-A zmienił się po zmianie doc-B?" → Bramka X (type: impacts)

**Re-evaluation trigger**: Jeśli > 50% bramek to `informs` (słabe zależności), rozważyć uproszczenie.

---

## F-082: Evaluate Gates

### Historia funkcji

Gdy wprowadziliśmy bramki (F-081), pojawił się problem: **kiedy bramka jest spełniona?**

Przykład: Bramka `ADR-003 requires RFC-2024-08 (status: approved)`.
- Jeśli RFC-2024-08 nie istnieje → luka E140 (broken dependency)
- Jeśli RFC-2024-08.status = "draft" → luka E150 (gate blocker)
- Jeśli RFC-2024-08.status = "approved" → bramka spełniona ✓

Początkowo sprawdzaliśmy to ad-hoc w różnych miejscach kodu (Opcja A). Rezultat: inconsistent logic, bugs (niektóre bramki sprawdzane, inne nie).

Rozważaliśmy SQL-like query language (Opcja B): `WHERE status IN ('approved', 'deployed')`. Problem: Over-engineering, trudne do debugowania.

Wybraliśmy **centralizowaną evaluację bramek** (Opcja C): Jedna funkcja `evaluate_gate()`, wywołana w kluczowych momentach:
- Po zmianie statusu dokumentu
- Po update metadata
- Po dodaniu/usunięciu dokumentu
- Na żądanie (manual trigger)

### Funkcja w praktyce

```python
class GateEvaluator:
    def evaluate_gate(self, gate: Gate) -> GateEvaluation:
        """
        Historia: Początkowo zwracaliśmy bool (satisfied: True/False).
        Problem: Nie wiadomo DLACZEGO bramka nie jest spełniona.

        V2: Zwracamy GateEvaluation z:
        - satisfied: bool
        - blocking: bool (czy to blokuje workflow)
        - message: str (czytelny komunikat)
        - remediation: List[str] (co zrobić)

        Przykład:
        Gate: "ADR-005 requires RFC-2024-08 (status: approved)"
        RFC-2024-08.status = "draft"

        Rezultat:
        GateEvaluation(
            satisfied=False,
            blocking=True,
            message="RFC-2024-08 is in 'draft', required status: 'approved'",
            remediation=[
                "Complete RFC-2024-08 review",
                "Obtain stakeholder approvals",
                "Change status to 'approved'"
            ]
        )
        """
        # Check if target exists
        target_doc = self.document_store.get(gate.target.id)
        if not target_doc:
            return GateEvaluation(
                gate=gate,
                satisfied=False,
                blocking=True,
                message=f"Target document {gate.target.id} not found",
                remediation=[f"Create document {gate.target.id}"]
            )

        # Check status constraint
        if gate.status_constraint:
            if target_doc.status not in gate.status_constraint:
                return GateEvaluation(
                    gate=gate,
                    satisfied=False,
                    blocking=gate.connection_type in ["requires", "blocks"],
                    message=f"{gate.target.id} is in '{target_doc.status}', required: {gate.status_constraint}",
                    remediation=self._generate_status_remediation(target_doc, gate.status_constraint)
                )

        # Check internal gates (if applicable)
        if gate.gate_type == "internal":
            return self._evaluate_internal_gate(gate)

        return GateEvaluation(
            gate=gate,
            satisfied=True,
            blocking=False,
            message=f"Gate satisfied",
            remediation=[]
        )

    def evaluate_all_gates(self, document_id: str) -> List[GateEvaluation]:
        """
        Ewaluuj wszystkie bramki powiązane z dokumentem (input + output).

        Use case: Po zmianie ADR-005.status = "approved":
        - Sprawdź output gates → IMPL-CART-DB może teraz ruszyć (unblock)
        - Sprawdź input gates → Czy wszystkie dependencies nadal OK
        """
        gates = self.gate_registry.get_gates_for_document(document_id)
        return [self.evaluate_gate(gate) for gate in gates]
```

### Kluczowe decyzje

**Q: Dlaczego nie real-time evaluation (przy każdym read)?**
**A**: Performance. Ewaluacja bramki = query do document store + potencjalnie recursive checks. Zamiast tego:
- **Trigger-based**: Evaluate on change events
- **Cache results**: Store evaluation results, invalidate on change
- **Batch mode**: Evaluate all gates co 5 min (dla low-priority bramek)

**Q: Dlaczego `blocking: bool`?**
**A**: Nie wszystkie bramki są critical. `informs` = nie blokuje workflow (może iść dalej mimo niesatesfied). `requires`/`blocks` = STOP (generuje lukę E150).

### Konsekwencje wyboru

**Akceptujemy**:
- **Eventual consistency**: Bramki nie zawsze evaluated instantly (cache, batch)
- **Performance cost**: 1000 dokumentów × 5 bramek/doc = 5000 evaluations

**Zyskujemy**:
- **Centralization**: Jedna logika, łatwy debugging
- **Remediation**: System podpowiada CO zrobić (nie tylko "gate not satisfied")
- **Auditability**: Historia evaluacji = audit log

---

## F-083: Propagate Changes Through Gates

### Historia funkcji

Gate evaluation (F-082) mówi CZY bramka spełniona. Ale co dalej gdy bramka NIE jest spełniona?

Przykład:
```
ADR-005 (Database choice) --impacts--> OPS-RUNBOOK-07 (Backup strategy)
ADR-005: zmiana PostgreSQL → MongoDB
```

**Co powinno się stać?**
1. OPS-RUNBOOK-07 jest **outdated** (backup strategy dla PostgreSQL nie działa dla MongoDB)
2. System powinien **automatycznie** utworzyć TODO: "Update OPS-RUNBOOK-07 after ADR-005 change"
3. Opcjonalnie: **zablokować** deployment dopóki runbook nie jest zaktualizowany

Początkowo to była **ręczna odpowiedzialność** (Opcja A): Developer zmienia ADR-005, pamięta (lub nie) żeby zaktualizować runbook. Rezultat: Outdated docs, incydenty (używaliśmy starego runbooka).

Rozważaliśmy **notification-only** (Opcja B): System wysyła email "ADR-005 zmieniony, sprawdź OPS-RUNBOOK-07". Problem: Emails ignorowane, brak trackingu (czy ktoś zaktualizował?).

Wybraliśmy **aktywną propagację** (Opcja C): Zmiana w source → system automatycznie:
1. Tworzy TODO-XXX z krokami update
2. (Opcjonalnie) Blokuje target do czasu review
3. Loguje propagację (audit trail)

### Funkcja w praktyce

```python
class ChangePropagator:
    def propagate_change(
        self,
        source_doc_id: str,
        change_type: ChangeType,  # status_change | content_update | metadata_update
        change_description: str
    ):
        """
        Historia: Dlaczego propagacja, a nie tylko notifications?

        Incident 2024-07-15:
        - ADR-003 zmienił wymaganie ACID → eventual consistency OK
        - ADR-005 (Database choice) nadal wymagał ACID (outdated)
        - Zespół wybrał PostgreSQL (ACID) zamiast Cassandra (eventual consistency)
        - Overpaid $1.5k/miesiąc przez 6 miesięcy ($9k strata)
        - Root cause: Brak automatycznej propagacji zmian

        V2: Propagacja automatyczna z TODO generation.

        Przykład:
        propagate_change(
            source_doc_id="ADR-003",
            change_type=ChangeType.CONTENT_UPDATE,
            change_description="Changed ACID requirement to eventual consistency"
        )
        → Znajduje wszystkie output gates z cascade=true
        → Tworzy TODO dla każdego impacted document
        → (Opcjonalnie) Blokuje deployment jeśli gate.blocking=true
        """
        # Find all output gates from source
        output_gates = self.gate_registry.get_output_gates(source_doc_id)

        for gate in output_gates:
            if not gate.cascade:
                # Non-cascading gate → tylko log, nie TODO
                self.audit_log.log_change(source_doc_id, gate.target.id, change_description)
                continue

            # Cascading gate → propagate
            self._propagate_to_target(gate, source_doc_id, change_type, change_description)

    def _propagate_to_target(
        self,
        gate: Gate,
        source_doc_id: str,
        change_type: ChangeType,
        change_description: str
    ):
        """
        Propagacja do target document:
        1. Sprawdź czy target istnieje
        2. Utwórz TODO z krokami update
        3. Jeśli gate.blocking=true → utwórz lukę E150
        4. Log propagację (audit trail)
        """
        target_doc = self.document_store.get(gate.target.id)

        if not target_doc:
            # Target nie istnieje → luka E140
            self.gap_engine.create_gap(
                type="E140",
                source=gate.source.id,
                target=gate.target.id,
                message=f"Target {gate.target.id} referenced but not found"
            )
            return

        # Create TODO satellite
        todo_id = self.satellite_generator.create_todo(
            parent_doc=gate.target.id,
            title=f"Review impact of {source_doc_id} change",
            tasks=[
                f"Read change in {source_doc_id}: {change_description}",
                f"Analyze impact on {gate.target.id}",
                f"Update {gate.target.id} if necessary",
                f"Mark TODO as complete"
            ],
            priority="high" if gate.blocking else "medium",
            reason=gate.reason,
            evidence=gate.evidence
        )

        # If blocking gate → create E150 gap
        if gate.blocking:
            self.gap_engine.create_gap(
                type="E150",
                source=gate.source.id,
                target=gate.target.id,
                message=f"Blocking gate not satisfied: {gate.reason}",
                remediation=[f"Complete TODO-{todo_id}"]
            )

        # Audit log
        self.audit_log.log_propagation(
            source=gate.source.id,
            target=gate.target.id,
            change_type=change_type,
            todo_created=todo_id,
            blocked=gate.blocking
        )
```

### Kluczowe decyzje

**Q: Dlaczego TODO auto-generation zamiast manual tracking?**
**A**: Ludzie zapominają. TODO = trackable, visible w dashboardzie, można assign owner.

**Q: Dlaczego `cascade: bool` flag?**
**A**: Nie każda zmiana wymaga update wszystkich impacted docs. Przykład: Typo fix w ADR → `cascade=false` (informative only). Major change (ACID → eventual consistency) → `cascade=true` (requires review).

**Q: Kiedy triggerujemy propagację?**
**A**:
- **Zawsze**: `content_update` jeśli sekcje critical (Decision, Architecture)
- **Zawsze**: `status_change` (draft → approved → deployed)
- **Opcjonalnie**: `metadata_update` (niektóre pola jak `owner` nie wymagają propagacji)

### Konsekwencje wyboru

**Akceptujemy**:
- **TODO overload**: Dużo zmian = dużo TODO. Rozwiązanie: Batch similar TODOs, priorytetyzacja.
- **False positives**: Czasem zmiana nie wpływa (mimo bramki). Rozwiązanie: User może oznaczyć TODO jako "no action needed".

**Zyskujemy**:
- **Proactive updates**: Nie czekamy aż ktoś zauważy outdated doc
- **Audit trail**: Historia propagacji = dowód due diligence
- **Reduced incidents**: Mniej outdated docs = mniej błędów w produkcji

---

## F-084: Detect Gate Blockers

### Historia funkcji

Gate evaluation (F-082) + propagation (F-083) działają, ale potrzebujemy **widoku agregowanego**: Które dokumenty są **zablokowane** przez niesatesfied gates?

Use case: Product Manager pyta "Czy możemy deployować feature X?"
- Feature X wymaga IMPL-CART-DB (implementation)
- IMPL-CART-DB ma bramkę `requires ADR-005 (status: approved)`
- ADR-005.status = "review" (nie approved)
- **Wniosek**: NIE, zablokowane przez ADR-005

Początkowo sprawdzaliśmy to ręcznie (Opcja A): Czytamy dokument, sprawdzamy dependencies, sprawdzamy status każdego dependency. Czasochłonne, error-prone.

Rozważaliśmy dashboard z "wszystkimi lukami" (Opcja B): Pokazuje E150 gaps. Problem: Luka E150 to "gate blocker", ale nie pokazuje **całego łańcucha blokad**.

Przykład:
```
DEPLOY-FEATURE-X --requires--> IMPL-CART-DB --requires--> ADR-005 --requires--> RFC-2024-08
RFC-2024-08.status = "draft"
```

Luka E150 jest na ADR-005 (wymaga RFC-2024-08 approved). Ale **efekt końcowy**: DEPLOY-FEATURE-X jest zablokowane (przez transitive dependency).

Wybraliśmy **blocker detection z transitive analysis** (Opcja C): System śledzi cały dependency chain, identyfikuje root blocker.

### Funkcja w praktyce

```python
class GateBlockerDetector:
    def detect_blockers(self, target_doc_id: str) -> BlockerReport:
        """
        Historia: Dlaczego transitive analysis?

        Incident 2024-08-05:
        - Team chciał deploy feature
        - Sprawdzili IMPL dokument → wszystkie gates OK ✓
        - Deploy → FAILED
        - Root cause: IMPL wymagał ADR, ADR wymagał RFC, RFC był "draft"
        - Nie zauważyli transitive dependency

        V2: Detect blockers rekursywnie.

        Przykład:
        detect_blockers("DEPLOY-FEATURE-X")
        → Returns:
        BlockerReport(
            document="DEPLOY-FEATURE-X",
            is_blocked=True,
            direct_blockers=["IMPL-CART-DB"],
            root_blockers=["RFC-2024-08"],
            blocker_chain=[
                "DEPLOY-FEATURE-X → IMPL-CART-DB (gate: requires, satisfied: False)",
                "IMPL-CART-DB → ADR-005 (gate: requires, satisfied: False)",
                "ADR-005 → RFC-2024-08 (gate: requires, satisfied: False, reason: status='draft')"
            ],
            remediation=[
                "Complete RFC-2024-08 review",
                "Change RFC-2024-08 status to 'approved'",
                "Re-evaluate ADR-005 gates",
                "Re-evaluate IMPL-CART-DB gates",
                "Re-evaluate DEPLOY-FEATURE-X gates"
            ]
        )
        """
        visited = set()
        blocker_chain = []
        root_blockers = []

        def _traverse_dependencies(doc_id: str, depth: int = 0):
            if doc_id in visited:
                return  # Avoid cycles

            visited.add(doc_id)

            # Get input gates (dependencies)
            input_gates = self.gate_registry.get_input_gates(doc_id)

            for gate in input_gates:
                evaluation = self.gate_evaluator.evaluate_gate(gate)

                if not evaluation.satisfied and evaluation.blocking:
                    # Blocker found
                    blocker_chain.append(
                        f"{'  ' * depth}{doc_id} → {gate.source.id} "
                        f"(gate: {gate.connection_type}, reason: {evaluation.message})"
                    )

                    # Recursively check if blocker has blockers
                    if self._has_input_gates(gate.source.id):
                        _traverse_dependencies(gate.source.id, depth + 1)
                    else:
                        # Root blocker (no further dependencies)
                        root_blockers.append(gate.source.id)

        _traverse_dependencies(target_doc_id)

        return BlockerReport(
            document=target_doc_id,
            is_blocked=len(blocker_chain) > 0,
            direct_blockers=[chain.split(" → ")[1].split(" ")[0] for chain in blocker_chain if "  " not in chain],
            root_blockers=list(set(root_blockers)),
            blocker_chain=blocker_chain,
            remediation=self._generate_blocker_remediation(root_blockers)
        )

    def get_all_blocked_documents(self) -> List[BlockerReport]:
        """
        Dashboard view: Wszystkie dokumenty zablokowane przez gates.

        Use case: Weekly review meeting
        - PM: "Co jest zablokowane?"
        - System: Returns list of blocked docs + root causes
        - Team priorytetyzuje unblocking

        Sortowanie: Po liczbie dependents (najpierw dokumenty blokujące najwięcej innych).
        """
        all_docs = self.document_store.get_all()
        blocked_docs = []

        for doc in all_docs:
            report = self.detect_blockers(doc.id)
            if report.is_blocked:
                blocked_docs.append(report)

        # Sort by impact (how many other docs are blocked by this)
        blocked_docs.sort(key=lambda r: len(self._get_dependents(r.document)), reverse=True)

        return blocked_docs
```

### Kluczowe decyzje

**Q: Dlaczego transitive analysis zamiast tylko direct dependencies?**
**A**: Real-world dependencies są multi-level. Ignorowanie transitive = niepełny obraz.

**Q: Dlaczego `root_blockers` osobno?**
**A**: To są dokumenty "leaf nodes" — nie mają dalszych dependencies. **Priorytet**: Odblokować root → reszta odblokuje się automatycznie.

**Q: Jak handling cycles?**
**A**: `visited` set. Jeśli cykl wykryty → luka E-XXX (nowy typ: circular dependency).

### Konsekwencje wyboru

**Akceptujemy**:
- **Performance cost**: Rekursywny traversal dla każdego dokumentu
- **Complexity**: Algorytm DFS/BFS z cycle detection

**Zyskujemy**:
- **Full visibility**: Widzimy cały blocker chain
- **Prioritization**: Root blockers = gdzie działać najpierw
- **Proactive**: Wykrywamy blokady zanim ktoś próbuje deploy

---

# Moduł 6: Decision Graph Manager

## F-086: Create Decision Graph

### Historia funkcji

Tradycyjna dokumentacja pokazuje **wynik decyzji** (wybraliśmy PostgreSQL). Ale:
- **Nie pokazuje alternatyw** (co jeszcze rozważaliśmy?)
- **Nie pokazuje kontekstu** (dlaczego w tamtym momencie to miało sens?)
- **Nie pokazuje uzasadnienia** (dlaczego PostgreSQL a nie MongoDB/MySQL/DynamoDB?)

Incident 2024-06-20:
- Nowy developer: "Dlaczego PostgreSQL? MongoDB byłby szybszy."
- Senior: "Potrzebowaliśmy ACID."
- Developer: "Ale MongoDB ma transactions od wersji 4.0."
- Senior: "...nie pamiętam. To było 2 lata temu."

**Problem**: Wiedza w głowach ludzi, nie w dokumentach.

Początkowo dodaliśmy sekcję "Alternatives Considered" (Opcja A): Lista opcji A, B, C z krótkim opisem. Problem:
- **Niestrukturalne**: Każdy pisze inaczej
- **Niekompletne**: Często brakuje "dlaczego NIE opcja X"
- **No evidence**: Brak linków do benchmarków/testów

Rozważaliśmy ADR template z forced sections (Opcja B): "Options", "Decision", "Consequences". Lepiej, ale:
- **Static text**: Trudno queryować (nie możesz zapytać "all decisions where cost > $5k")
- **No relationships**: Nie wiesz które decyzje są powiązane

Wybraliśmy **Decision Graph jako structured data** (Opcja C):
- **Nodes**: Decision, Options (selected + rejected), Context, Evidence
- **Edges**: Option → Decision, Evidence → Option, Context → Decision
- **Queryable**: SQL/Cypher queries nad grafem
- **Visualizable**: Mermaid/Cytoscape graphs

### Funkcja w praktyce

```python
class DecisionGraphBuilder:
    def create_decision_graph(
        self,
        document_id: str,
        decision_title: str,
        decision_date: str,
        decision_maker: List[str]
    ) -> DecisionGraph:
        """
        Historia: Dlaczego osobny DecisionGraph zamiast tylko metadata?

        Próbowaliśmy trzymać wszystko w YAML frontmatter (Opcja A):
        alternatives:
          - MongoDB (rejected: no ACID)
          - MySQL (rejected: slow writes)
          - PostgreSQL (selected)

        Problem: YAML nie wspiera relationships. Nie możesz zapytać:
        "Pokaż wszystkie decyzje gdzie odrzuciliśmy MongoDB z powodu braku ACID"

        V2: DecisionGraph jako separate entity z relational structure.

        Przykład:
        create_decision_graph(
            document_id="ADR-005",
            decision_title="Database choice for Cart Service",
            decision_date="2024-08-15",
            decision_maker=["Tech Lead", "Backend Team"]
        )
        → Creates DecisionGraph with:
          - Decision node (ADR-005)
          - Empty options (to be added via register_option)
          - Empty context (to be added via capture_context)
        """
        graph_id = f"DEC-{document_id}"

        decision_node = DecisionNode(
            id=graph_id,
            document_id=document_id,
            title=decision_title,
            date=decision_date,
            decision_maker=decision_maker,
            status="in-progress"  # Until options registered
        )

        graph = DecisionGraph(
            id=graph_id,
            decision_node=decision_node,
            option_nodes=[],
            context_nodes=[],
            evidence_nodes=[],
            edges=[]
        )

        self.graph_store.save(graph)
        return graph
```

### Konsekwencje wyboru

**Akceptujemy**:
- **More structure**: Trzeba wypełnić wszystkie nodes/edges (nie tylko text)
- **Learning curve**: Zespół musi nauczyć się używać graph API

**Zyskujemy**:
- **Queryability**: "Find all decisions where we rejected option X due to cost"
- **Visualization**: Auto-generated Mermaid diagrams
- **Auditability**: Full decision trail z evidence

---

## F-087: Register All Options

### Historia funkcji

Kluczowy aspekt Decision Graph: **rejestrujemy WSZYSTKIE opcje**, nie tylko wybraną.

**Dlaczego?**

Incident 2024-09-10:
- Team review: "Dlaczego nie używamy DynamoDB? Jest 2x szybszy."
- Response: "Over budget."
- Question: "Ale teraz mamy większy budżet. Może migrować?"
- Problem: **Nie pamiętamy benchmarków DynamoDB** (nie zapisaliśmy bo "nie wybraliśmy")

Opcje odrzucone są **równie ważne** jak wybrane, ponieważ:
1. **Re-evaluation**: Jeśli context zmieni się (np. budżet rośnie), możemy wrócić do odrzuconej opcji
2. **Learning**: Nowi członkowie widzą **cały proces myślowy**
3. **Avoid repetition**: Ktoś nowy proponuje "a co z DynamoDB?" → pokazujemy "już rozważaliśmy, oto dlaczego NIE"

### Funkcja w praktyce

```python
def register_option(
    self,
    graph_id: str,
    option_id: str,
    title: str,
    status: Literal["selected", "rejected", "deferred"],
    benchmark: Dict = None,
    cost: str = None,
    rationale: str = "",
    evidence: List[str] = []
) -> OptionNode:
    """
    Historia: Początkowo mieliśmy tylko `selected_option` (singiel).
    Problem: Gdzie zapisać opcje odrzucone?

    V2: register_option() dla WSZYSTKICH opcji (selected + rejected + deferred).

    Przykład REJECTED option:
    register_option(
        graph_id="DEC-ADR-005",
        option_id="OPTION-D",
        title="DynamoDB",
        status="rejected",
        benchmark={
            "throughput": "25k writes/s",
            "latency_p99": "30ms"
        },
        cost="$6k/month (provisioned)",
        rationale="Over budget ($6k > $5k) + vendor lock-in",
        evidence=["E-045"]  # Cost calculation
    )
    → Saved in graph, queryable later
    """
    option_node = OptionNode(
        id=option_id,
        title=title,
        status=status,
        benchmark=benchmark,
        cost=cost,
        rationale=rationale,
        evidence=evidence
    )

    graph = self.graph_store.get(graph_id)
    graph.option_nodes.append(option_node)

    # Create edge: Option → Decision
    edge = Edge(
        from_node=option_id,
        to_node=graph.decision_node.id,
        edge_type="belongs_to",
        metadata={"status": status}
    )
    graph.edges.append(edge)

    # Create edges: Evidence → Option
    for evidence_id in evidence:
        graph.edges.append(Edge(
            from_node=evidence_id,
            to_node=option_id,
            edge_type="supports"
        ))

    self.graph_store.save(graph)
    return option_node
```

### Kluczowe decyzje

**Q: Dlaczego `status: deferred` (oprócz selected/rejected)?**
**A**: Czasem opcja jest dobra, ale "not now". Przykład: Kubernetes (deferred bo team za mały, revisit gdy 10+ services).

**Q: Dlaczego `benchmark: Dict` zamiast free text?**
**A**: Structured data → queryable. Możesz zapytać "show all rejected options where throughput > selected option".

**Q: Dlaczego każda opcja ma `evidence`?**
**A**: Opcja bez evidence = spekulacja. Każda opcja musi mieć benchmark/test/analysis.

### Konsekwencje wyboru

**Akceptujemy**:
- **More work**: Musimy dokumentować wszystkie opcje, nie tylko wybraną
- **Evidence burden**: Każda opcja = minimum 1 evidence note

**Zyskujemy**:
- **Re-evaluation**: Możemy wrócić do opcji gdy context zmieni się
- **Knowledge transfer**: Nowi członkowie widzą full process
- **Avoid repetition**: "To już sprawdzaliśmy, oto wyniki"

---

## F-088: Capture Context T₀

### Historia funkcji

Decyzja zależy od **kontekstu w momencie podejmowania**. Ten sam problem, inny context = inna decyzja.

Przykład:
- **2024**: Budget $5k/m, team 2 devs → wybór: PostgreSQL
- **2026**: Budget $20k/m, team 10 devs → ten sam problem, lepszy wybór: DynamoDB + caching layer

Jeśli nie zapisujemy context T₀, przyszłe review pytają: "Dlaczego wybrali PostgreSQL a nie DynamoDB?" → odpowiedź brzmi "bo budget" ale **nie zapisaliśmy budżetu**.

Początkowo zakładaliśmy że "context jest oczywisty" (Opcja A). Problem: Po 2 latach NIE JEST oczywisty.

Rozważaliśmy link do external docs (Opcja B): "Context: patrz Business Case doc". Problem:
- Business Case może się zmienić (edit in place)
- Nie wiemy **dokładnie jaki był stan** w momencie decyzji

Wybraliśmy **snapshot context T₀** (Opcja C): W momencie decyzji zapisujemy:
- Budget
- Team size/skills
- Timeline
- Business constraints
- Tech landscape (dostępne wersje technologii)
- Previous decisions (które już podjęliśmy)

**Immutable**: Nawet jeśli Business Case się zmieni, context T₀ pozostaje.

### Funkcja w praktyce

```python
def capture_context_T0(
    self,
    graph_id: str,
    timestamp: str,
    global_context: Dict,
    internal_context: Dict
) -> ContextNode:
    """
    Historia: Dlaczego snapshot zamiast link?

    Incident 2024-10-05:
    - Review decyzji z 2022: "Dlaczego wybrali MySQL?"
    - Document: "Context: see BIZ-CASE-001"
    - BIZ-CASE-001: Updated 10 razy, budget zmieniony z $2k → $50k
    - Nie wiemy jaki był budget w 2022 (lost context)

    V2: Snapshot context immutable.

    Przykład:
    capture_context_T0(
        graph_id="DEC-ADR-005",
        timestamp="2024-08-15T10:00:00Z",
        global_context={
            "budget": "$5k/month",
            "team": "2 backend devs (SQL experience, no NoSQL)",
            "timeline": "Launch by 2024-10-01",
            "business_constraints": [
                "GDPR compliance (data in EU)",
                "99.9% uptime SLA"
            ],
            "tech_landscape": [
                "PostgreSQL 16 available",
                "MySQL 8.0 available",
                "MongoDB 7.0 available"
            ]
        },
        internal_context={
            "previous_decisions": [
                {"id": "ADR-003", "title": "Standardy persystencji", "constraint": "ACID required"}
            ],
            "baseline_assumptions": [
                "Expected traffic: 10k req/s",
                "Write-heavy workload (70% writes)"
            ]
        }
    )
    → Saved immutably, queryable later
    """
    context_node = ContextNode(
        id=f"CTX-{graph_id}-{timestamp}",
        timestamp=timestamp,
        global_context=global_context,
        internal_context=internal_context
    )

    graph = self.graph_store.get(graph_id)
    graph.context_nodes.append(context_node)

    # Edge: Context → Decision
    graph.edges.append(Edge(
        from_node=context_node.id,
        to_node=graph.decision_node.id,
        edge_type="influences"
    ))

    self.graph_store.save(graph)
    return context_node
```

### Kluczowe decyzje

**Q: Dlaczego `global_context` + `internal_context`?**
**A**:
- **Global**: External factors (budget, timeline, regulations)
- **Internal**: Previous decisions within project (ADR-003 wymaga ACID)

**Q: Kiedy capture context?**
**A**: W momencie rozpoczęcia analysis (przed wyborem opcji). Jeśli capture po wyborze → bias (context dostosowany do wyboru).

**Q: Czy context można edytować?**
**A**: **NIE**. Context T₀ jest immutable. Jeśli context zmieni się → create new decision graph (re-evaluation).

### Konsekwencje wyboru

**Akceptujemy**:
- **Redundancy**: Context może duplikować info z innych dokumentów
- **Staleness**: Context T₀ może być outdated (ale to OK, reprezentuje stan w momencie decyzji)

**Zyskujemy**:
- **Time travel**: Możemy "wrócić w czasie" i zrozumieć decyzję w kontekście
- **Re-evaluation**: Widzimy ŻE context zmienił się (budget $5k → $20k) → trigger re-evaluation

---

[Dokument kontynuowany z pozostałymi funkcjami...]

## Podsumowanie Storytelling Approach

Każda funkcja opisana jako:
1. **Historia**: Dlaczego funkcja powstała (problem domain)
2. **Opcje**: Co rozważaliśmy (alternatives)
3. **Wybór**: Dlaczego ta implementacja (rationale)
4. **Konsekwencje**: Co akceptujemy vs zyskujemy (trade-offs)

**To nie jest dokumentacja techniczna — to mapa myślenia.**

---

← [Poprzednia: Mapowanie](./koncepcje-v2-mapowanie.md) | [Powrót do głównego dokumentu](./koncepcje-v2.md) | [Następna: Przykłady →](./koncepcje-v2-przyklady.md)
