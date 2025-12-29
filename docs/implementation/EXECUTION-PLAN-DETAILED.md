---
id: EXEC-PLAN-DETAILED-001
title: "Szczegółowy Plan Wykonania Implementacji - Sprint by Sprint"
type: execution-plan
status: active
created: 2025-12-29
parent: IMPL-PLAN-001

dependencies:
  - id: IMPL-PLAN-001
    type: requires
  - id: TDD-001-V2
    type: requires
  - id: ROADMAP-001
    type: informs

context:
  approach: "Context-aware execution"
  strategy: "Read → Plan → Execute → Validate → Document cycle"
  session_management: "Maintain context through file reads between major tasks"
---

# Szczegółowy Plan Wykonania Implementacji

## 🎯 Filozofia Planu

**Problem**: Długie sesje implementacji bez odświeżania kontekstu prowadzą do:
- Niespójności z designem
- Zapomnienia o zależnościach
- Odchyleń od specyfikacji

**Rozwiązanie**: **Cykl Read-Plan-Execute-Validate-Document (RPEVD)**

Przed każdym **major task** (>100 linii kodu):
1. **READ** - Przeczytaj relevantne dokumenty (TDD, ADR, PRD)
2. **PLAN** - Zaplanuj konkretne kroki
3. **EXECUTE** - Implementuj zadanie
4. **VALIDATE** - Zwaliduj przeciwko specs
5. **DOCUMENT** - Dokumentuj co zostało zrobione

---

## 📋 SPRINT 1: Fundament (Parser + Modele)
**Timeline**: Tygodnie 1-2
**Deliverable**: Parser działający na 100+ przykładowych docs

### Phase 1.1: Setup Projektu (Dzień 1)

#### 📖 Context Read (przed rozpoczęciem):
```
1. Read TDD-001-V2 (section: Architecture Overview, Technology Stack)
2. Read ADR-006 (Parser Architecture)
3. Read IMPL-PLAN-001 (Sprint 1 details)
```

#### ✅ Tasks:
1. **Utworzenie struktury katalogów**
   - `mkdir -p ishkarim/{core,models,schemas,gui,tests}`
   - `touch ishkarim/__init__.py`

2. **Setup pyproject.toml**
   ```toml
   [project]
   name = "ishkarim"
   version = "0.1.0"
   dependencies = [
       "pydantic>=2.5",
       "pyyaml>=6.0",
       "python-frontmatter>=1.0",
       "markdown-it-py>=3.0",
       "networkx>=3.2",
       "PySide6>=6.6",
       "watchdog>=3.0"
   ]
   ```

3. **Walidacja setup**:
   - `python -m pytest --version` (sprawdź pytest)
   - `python -m pip install -e .` (editable install)

**Checkpoint**: ✅ Virtual environment setup, dependencies installed

---

### Phase 1.2: Models (Dni 2-3)

#### 📖 Context Read:
```
1. Read TDD-001-V2 (section: Data Models)
2. Read specs/specs_doc_types.md (all document types)
3. Read PRD-001-V2 (section: Core Entities)
```

#### ✅ Tasks:

**Task 1.2.1: Utworzenie `models/document.py`** (60 min)
- Przeczytaj: TDD-001-V2 lines 500-600 (Document model spec)
- Implementuj:
  ```python
  from pydantic import BaseModel, Field
  from pathlib import Path
  from typing import Literal, Optional

  class Document(BaseModel):
      id: str = Field(pattern=r"^[A-Z]+-\d{3}(-V\d+)?$")
      title: str = Field(min_length=5, max_length=200)
      type: str  # FIXME: Make Literal[...] after reading all types
      status: str
      path: Path
      content: str  # Markdown content (no frontmatter)
      metadata: dict  # Full YAML frontmatter

      class Config:
          arbitrary_types_allowed = True
  ```
- Waliduj: `pytest tests/test_document_model.py`

**Task 1.2.2: Utworzenie `models/gap.py`** (45 min)
- Przeczytaj: TDD-001-V2 (section: Gap Detection Engine)
- Przeczytaj: specs/specs_error_codes.md (all gap types E110-E180)
- Implementuj:
  ```python
  from enum import Enum
  from pydantic import BaseModel

  class GapSeverity(Enum):
      ERROR = "error"
      WARNING = "warning"
      INFO = "info"

  class Gap(BaseModel):
      code: str  # E110, E120, etc.
      severity: GapSeverity
      document_id: str
      message: str
      remediation: Optional[str] = None
  ```
- Waliduj: `pytest tests/test_gap_model.py`

**Task 1.2.3: Utworzenie `models/graph.py`** (30 min)
- Przeczytaj: TDD-001-V2 (section: Graph Builder)
- Przeczytaj: ADR-004 (Graph Visualization decision)
- Implementuj:
  ```python
  from networkx import DiGraph
  from typing import List

  class DocumentGraph:
      def __init__(self):
          self.graph = DiGraph()

      def add_document(self, doc: Document):
          self.graph.add_node(doc.id, document=doc)

      def add_dependency(self, source_id: str, target_id: str):
          self.graph.add_edge(source_id, target_id)
  ```
- Waliduj: `pytest tests/test_graph_model.py`

**Checkpoint**: ✅ All 3 models implemented, tests passing (coverage >80%)

---

### Phase 1.3: Parser Implementation (Dni 4-6)

#### 📖 Context Read:
```
1. Read TDD-001-V2 (section: Parser Component COMP-001)
2. Read ADR-006 (Parser Architecture - python-frontmatter decision)
3. Read E-149 (frontmatter benchmark)
4. Read E-162 (markdown parser comparison)
```

#### ✅ Tasks:

**Task 1.3.1: Utworzenie `core/parser.py` - Base** (90 min)
- Implementuj:
  ```python
  import frontmatter
  from pathlib import Path
  from typing import List
  from models.document import Document

  class DocumentParser:
      def __init__(self, docs_root: Path):
          self.docs_root = docs_root

      def parse_file(self, path: Path) -> Document:
          """Parse single markdown file with YAML frontmatter"""
          post = frontmatter.load(path)

          return Document(
              id=post.metadata.get('id', 'UNKNOWN'),
              title=post.metadata.get('title', 'Untitled'),
              type=post.metadata.get('type', 'unknown'),
              status=post.metadata.get('status', 'draft'),
              path=path,
              content=post.content,
              metadata=post.metadata
          )

      def parse_directory(self, pattern: str = "**/*.md") -> List[Document]:
          """Parse all matching markdown files"""
          documents = []
          for path in self.docs_root.glob(pattern):
              try:
                  doc = self.parse_file(path)
                  documents.append(doc)
              except Exception as e:
                  # TODO: Log error, continue parsing
                  pass
          return documents
  ```

**Task 1.3.2: Error Handling** (60 min)
- Przeczytaj: ADR-008 (Error Handling Strategy)
- Przeczytaj: E-008 (Error handling patterns survey)
- Refactor parser z custom exceptions:
  ```python
  class IshkarimError(Exception):
      """Base exception"""
      pass

  class ParseError(IshkarimError):
      """Document parsing failed"""
      pass

  # Update parse_file to raise ParseError on invalid YAML
  ```

**Task 1.3.3: Performance Testing** (45 min)
- Utworzenie 100 test documents w `tests/fixtures/docs/`
- Benchmark test:
  ```python
  def test_parser_performance():
      parser = DocumentParser(Path("tests/fixtures/docs"))
      start = time.perf_counter()
      docs = parser.parse_directory()
      elapsed = time.perf_counter() - start

      assert len(docs) == 100
      assert elapsed < 5.0  # NFR: < 5s dla 100 docs
  ```

**Checkpoint**: ✅ Parser complete, 100 docs parsed in <5s, tests passing

---

### Phase 1.4: Integration & Documentation (Dzień 7)

#### 📖 Context Read:
```
1. Review wszystkie zaimplementowane komponenty
2. Read TEST-PLAN-001 (test coverage requirements)
```

#### ✅ Tasks:

1. **Integration Test**
   - Utworzenie `tests/integration/test_parser_integration.py`
   - Test: Parse real docs from `docs/engineering/decisions/`
   - Validate: All ADRs parsed correctly

2. **Documentation**
   - Update IMPL-LOG-001 z progress Sprint 1
   - Utworzenie README.md w `ishkarim/` z usage examples

3. **Code Review Checklist**
   - [ ] All functions have docstrings
   - [ ] Type hints present
   - [ ] Error handling zgodne z ADR-008
   - [ ] Tests coverage ≥ 80%

**Deliverable Sprint 1**: ✅ Parser + Models complete, 80% coverage, documentation updated

---

## 📋 SPRINT 2: Validator (Walidacja Pydantic)
**Timeline**: Tygodnie 3-4
**Deliverable**: Validator wyłapuje wszystkie naruszenia schematu

### Phase 2.1: Schemas Definition (Dzień 8-9)

#### 📖 Context Read:
```
1. Read TDD-001-V2 (section: Validator Component COMP-002)
2. Read ADR-003 (Validation Strategy - Pydantic decision)
3. Read specs/specs_doc_types.md (all 25+ document types)
4. Read E-145 (Pydantic vs OPA comparison)
5. Read E-164 (Pydantic 2.5 benchmark)
```

#### ✅ Tasks:

**Task 2.1.1: Utworzenie `schemas/base.py`** (60 min)
- Base schema dla wszystkich document types:
  ```python
  from pydantic import BaseModel, Field, validator
  from typing import Literal, Optional, List
  from datetime import date

  class BaseDocumentSchema(BaseModel):
      id: str = Field(pattern=r"^[A-Z]+-\d{3}(-V\d+)?$")
      title: str = Field(min_length=5, max_length=200)
      type: str  # Overridden in subclasses
      status: str  # Enum depends on type
      created: date
      updated: Optional[date] = None
      owner: str

      @validator('updated')
      def updated_after_created(cls, v, values):
          if v and 'created' in values and v < values['created']:
              raise ValueError("updated must be >= created")
          return v
  ```

**Task 2.1.2: Utworzenie schemas dla ADR, PRD, TDD** (120 min)
- Przeczytaj przykładowe ADR-001.md, PRD-001-V2.md, TDD-001-V2.md
- Dla każdego typu:
  ```python
  # schemas/adr.py
  from schemas.base import BaseDocumentSchema
  from typing import Literal

  class ADRSchema(BaseDocumentSchema):
      type: Literal["adr"]
      status: Literal["draft", "proposed", "accepted", "rejected", "deprecated"]
      decision_date: date
      author: List[str]

      # Custom validators dla ADR-specific rules
      @validator('id')
      def validate_adr_id(cls, v):
          if not v.startswith('ADR-'):
              raise ValueError("ADR ID must start with 'ADR-'")
          return v
  ```

**Task 2.1.3: Schema Registry** (45 min)
- Utworzenie `schemas/registry.py`:
  ```python
  from typing import Dict, Type
  from schemas.base import BaseDocumentSchema
  from schemas.adr import ADRSchema
  from schemas.prd import PRDSchema
  # ... import all schemas

  SCHEMA_REGISTRY: Dict[str, Type[BaseDocumentSchema]] = {
      "adr": ADRSchema,
      "prd": PRDSchema,
      "tdd": TDDSchema,
      # ... register all 7 schemas (MVP: focus on core types)
  }

  def get_schema(doc_type: str) -> Type[BaseDocumentSchema]:
      return SCHEMA_REGISTRY.get(doc_type, BaseDocumentSchema)
  ```

**Checkpoint**: ✅ 7+ schemas defined, registry working

---

### Phase 2.2: Validator Implementation (Dzień 10-11)

#### 📖 Context Read:
```
1. Read TDD-001-V2 (Validator component detailed spec)
2. Read specs/specs_error_codes.md (E110, E120 definitions)
3. Review ADR-003 (Pydantic usage patterns)
```

#### ✅ Tasks:

**Task 2.2.1: `core/validator.py` - Base** (90 min)
```python
from pydantic import ValidationError
from models.document import Document
from models.gap import Gap, GapSeverity
from schemas.registry import get_schema
from typing import List

class DocumentValidator:
    def validate(self, document: Document) -> List[Gap]:
        """Validate document against schema, return gaps"""
        gaps = []

        # Get appropriate schema
        schema_class = get_schema(document.type)

        try:
            # Validate metadata against schema
            schema_class(**document.metadata)
        except ValidationError as e:
            # Convert Pydantic errors to Gaps
            for error in e.errors():
                gap = Gap(
                    code="E110",  # Schema violation
                    severity=GapSeverity.ERROR,
                    document_id=document.id,
                    message=f"{error['loc'][0]}: {error['msg']}",
                    remediation=f"Fix field '{error['loc'][0]}' in {document.path}"
                )
                gaps.append(gap)

        return gaps
```

**Task 2.2.2: Gap Detection E120 (Missing Required Sections)** (60 min)
- Przeczytaj specs dla E120
- Dodaj do validator:
  ```python
  def _check_required_sections(self, document: Document) -> List[Gap]:
      """E120: Missing required sections"""
      required_sections = self._get_required_sections(document.type)
      content_sections = self._extract_sections(document.content)

      missing = set(required_sections) - set(content_sections)

      gaps = []
      for section in missing:
          gaps.append(Gap(
              code="E120",
              severity=GapSeverity.WARNING,
              document_id=document.id,
              message=f"Missing required section: {section}",
              remediation=f"Add '## {section}' section to {document.path}"
          ))
      return gaps
  ```

**Task 2.2.3: Integration with Parser** (30 min)
- Utworzenie `core/pipeline.py`:
  ```python
  class DocumentPipeline:
      def __init__(self, docs_root: Path):
          self.parser = DocumentParser(docs_root)
          self.validator = DocumentValidator()

      def process(self) -> tuple[List[Document], List[Gap]]:
          """Parse all docs, validate, return docs + gaps"""
          documents = self.parser.parse_directory()

          all_gaps = []
          for doc in documents:
              gaps = self.validator.validate(doc)
              all_gaps.extend(gaps)

          return documents, all_gaps
  ```

**Checkpoint**: ✅ Validator detecting E110, E120 gaps, integration tests passing

---

### Phase 2.3: Testing & Validation (Dzień 12-13)

#### 📖 Context Read:
```
1. Read TEST-PLAN-001 (validation test cases)
2. Review implemented validator code
```

#### ✅ Tasks:

1. **Unit Tests** (90 min)
   - `tests/test_validator.py` - test każdego schema
   - Test invalid documents (missing fields, wrong types)
   - Test valid documents (should pass)

2. **Integration Tests** (60 min)
   - Parse real ADRs, validate, check gaps
   - Expect 0 gaps dla well-formed docs

3. **Performance Test** (30 min)
   - Validate 100 docs w <1s (Pydantic 2.5 Rust core)

**Deliverable Sprint 2**: ✅ Validator complete, E110+E120 working, 80% coverage

---

## 📋 SPRINT 3: Graph Builder (NetworkX)
**Timeline**: Tygodnie 5-6
**Deliverable**: Wizualizacja grafu zależności w CLI

### Phase 3.1: Graph Builder Implementation (Dzień 14-16)

#### 📖 Context Read:
```
1. Read TDD-001-V2 (section: Graph Builder COMP-003)
2. Read ADR-004 (Graph Visualization - NetworkX decision)
3. Read E-148 (NetworkX algorithms evaluation)
4. Read E-165 (NetworkX vs igraph comparison)
5. Read dependency_graph.md (all graph examples)
```

#### ✅ Tasks:

**Task 3.1.1: `core/graph_builder.py` - Base** (120 min)
```python
import networkx as nx
from models.document import Document
from models.gap import Gap, GapSeverity
from typing import List, Set

class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build(self, documents: List[Document]) -> nx.DiGraph:
        """Build dependency graph from documents"""
        # Add all documents as nodes
        for doc in documents:
            self.graph.add_node(
                doc.id,
                document=doc,
                type=doc.type,
                status=doc.status
            )

        # Add dependency edges
        for doc in documents:
            deps = doc.metadata.get('dependencies', [])
            for dep in deps:
                dep_id = dep.get('id') if isinstance(dep, dict) else dep
                if dep_id:
                    self.graph.add_edge(doc.id, dep_id)

        return self.graph

    def detect_cycles(self) -> List[List[str]]:
        """Find circular dependencies"""
        try:
            cycles = list(nx.find_cycle(self.graph))
            return cycles
        except nx.NetworkXNoCycle:
            return []

    def get_topological_order(self) -> List[str]:
        """Get build order (dependencies first)"""
        try:
            return list(nx.topological_sort(self.graph))
        except nx.NetworkXError:
            # Cycles detected
            return []
```

**Task 3.1.2: Gap Detection E140 (Broken Dependencies)** (90 min)
- Przeczytaj specs E140
- Implementuj:
  ```python
  def detect_broken_dependencies(self, documents: List[Document]) -> List[Gap]:
      """E140: Referenced document doesn't exist"""
      gaps = []
      doc_ids = {doc.id for doc in documents}

      for doc in documents:
          deps = doc.metadata.get('dependencies', [])
          for dep in deps:
              dep_id = dep.get('id') if isinstance(dep, dict) else dep
              if dep_id and dep_id not in doc_ids:
                  gaps.append(Gap(
                      code="E140",
                      severity=GapSeverity.ERROR,
                      document_id=doc.id,
                      message=f"Broken dependency: {dep_id} not found",
                      remediation=f"Create {dep_id} or remove from dependencies"
                  ))
      return gaps
  ```

**Task 3.1.3: CLI Visualization** (60 min)
- Simple ASCII graph dla testing:
  ```python
  def print_graph_ascii(graph: nx.DiGraph):
      """Print graph as ASCII tree"""
      # Topological sort
      try:
          order = list(nx.topological_sort(graph))
          for node in order:
              deps = list(graph.successors(node))
              print(f"{node} -> {', '.join(deps) if deps else '(no deps)'}")
      except nx.NetworkXError:
          print("ERROR: Graph has cycles!")
  ```

**Checkpoint**: ✅ Graph built, cycles detected, broken deps identified (E140)

---

### Phase 3.2: Performance & Testing (Dzień 17-18)

#### 📖 Context Read:
```
1. Review NFR-002 (Performance requirements)
2. Read E-148 (algorithm performance benchmarks)
```

#### ✅ Tasks:

1. **Performance Benchmark** (60 min)
   ```python
   def test_graph_performance():
       # 100 documents with dependencies
       builder = GraphBuilder()
       start = time.perf_counter()
       graph = builder.build(documents)
       elapsed = time.perf_counter() - start

       assert elapsed < 2.0  # NFR: < 2s dla 100 docs
   ```

2. **Algorithm Tests** (90 min)
   - Test cycle detection
   - Test topological sort
   - Test shortest path (bonus)

3. **Integration Test** (45 min)
   - Parse + Validate + Build Graph pipeline
   - Verify all components work together

**Deliverable Sprint 3**: ✅ Graph builder complete, E140 working, <2s dla 100 docs

---

## 📋 SPRINT 4-6: GUI, Cytoscape.js, Gap Engine
*(Details similar format - każdy sprint ma Context Read → Tasks → Validation cycle)*

---

## 🔄 Context Management Strategy

### Przed Każdą Sesją Kodowania:

**Morning Standup (5-10 min)**:
1. Review: Co zostało zrobione yesterday?
2. Read: Jakie dokumenty są relevantne today?
3. Plan: Konkretne tasks na today (z tego planu)

**Example Session Start**:
```
Today: Implementuję Task 2.1.2 (ADR/PRD/TDD schemas)

Context Read List:
1. ✅ Read ADR-001.md (example ADR structure)
2. ✅ Read PRD-001-V2.md (example PRD structure)
3. ✅ Read TDD-001-V2.md (example TDD structure)
4. ✅ Read specs/specs_doc_types.md (schema requirements)

Plan:
- [ ] Create schemas/adr.py (30 min)
- [ ] Create schemas/prd.py (30 min)
- [ ] Create schemas/tdd.py (30 min)
- [ ] Test all 3 schemas (30 min)
```

### Po Każdym Major Task:

**Update Progress**:
1. Mark task complete w tym planie
2. Update IMPL-LOG-001 z wykonanym progress
3. Commit code z descriptive message
4. Document any deviations from plan

---

## 📊 Tracking Progress

### Milestone Checklist:

- [ ] **Sprint 1 Complete**: Parser + Models (Week 2)
  - [ ] Phase 1.1: Setup ✅
  - [ ] Phase 1.2: Models ✅
  - [ ] Phase 1.3: Parser ✅
  - [ ] Phase 1.4: Integration ✅

- [ ] **Sprint 2 Complete**: Validator (Week 4)
  - [ ] Phase 2.1: Schemas ✅
  - [ ] Phase 2.2: Validator ✅
  - [ ] Phase 2.3: Testing ✅

- [ ] **Sprint 3 Complete**: Graph (Week 6)
  - [ ] Phase 3.1: Graph Builder ✅
  - [ ] Phase 3.2: Performance ✅

- [ ] **Sprint 4 Complete**: GUI Foundation (Week 8)
- [ ] **Sprint 5 Complete**: Cytoscape.js (Week 10)
- [ ] **Sprint 6 Complete**: Gap Engine Full (Week 12)

---

## 🚨 Critical Success Factors

### NEVER Skip:
1. ❌ **Context Read** przed major task
2. ❌ **Validation** po każdym task
3. ❌ **Tests** (maintain 80% coverage)
4. ❌ **Documentation** updates

### ALWAYS Do:
1. ✅ Read relevantne specs przed implementacją
2. ✅ Commit frequently (małe, atomic commits)
3. ✅ Test performance przeciwko NFRs
4. ✅ Update progress tracking

---

## 📝 Next Steps (Immediate)

**Start Sprint 1 Phase 1.1** (Today):
1. Read: TDD-001-V2, ADR-006, IMPL-PLAN-001
2. Setup: Create directory structure
3. Setup: Configure pyproject.toml
4. Validate: Install dependencies, run tests

**Tomorrow**:
- Start Phase 1.2 (Models implementation)
- Read: TDD-001-V2 Data Models section
- Implement: Document, Gap, Graph models

---

**Status**: READY TO START ✅
**Next Action**: Begin Phase 1.1 Setup Projektu
