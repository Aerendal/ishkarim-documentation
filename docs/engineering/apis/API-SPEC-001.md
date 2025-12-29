---
id: API-SPEC-001
title: "API-SPEC-001: API Specifications"
type: api-spec
status: draft
parent: TDD-001-V2

dependencies:
  - id: "DATA-MODEL-001"
    type: requires
    reason: "APIs use data models as request/response types"

# Bramki wyjścia (na co ten dokument wpływa)
impacts:
  - id: "COMP-001-parser"
    type: implemented_by
    reason: "Parser implementuje ParserAPI"
    cascade: true

  - id: "COMP-002-validator"
    type: implemented_by
    reason: "Validator implementuje ValidatorAPI"
    cascade: true

  - id: "COMP-003-graph"
    type: implemented_by
    reason: "Graph Builder implementuje GraphAPI"
    cascade: true

  - id: "COMP-004-gap-engine"
    type: implemented_by
    reason: "Gap Engine implementuje GapDetectorAPI"
    cascade: true

  - id: "COMP-005-gui"
    type: implemented_by
    reason: "GUI implementuje ApplicationAPI"
    cascade: true

  - id: "COMP-006-storage"
    type: implemented_by
    reason: "Storage implementuje StorageAPI"
    cascade: true

evidence_ids:
  - "E-157"  # API design evaluation
---

# API-SPEC-001: API Specifications

**Responsibility**: Complete API contracts dla wszystkich komponentów systemowych

---

## Spis Treści

1. [Parser API](#parser-api)
2. [Validator API](#validator-api)
3. [Graph Builder API](#graph-builder-api)
4. [Gap Engine API](#gap-engine-api)
5. [Gate Manager API](#gate-manager-api)
6. [Storage API](#storage-api)
7. [GUI API](#gui-api)
8. [Domain API](#domain-api)

---

## Parser API

**Module**: `src/core/parser.py`

### ParserAPI Class

```python
from pathlib import Path
from typing import Optional
from models.document import Document, Section

class ParserAPI:
    """
    Markdown document parser with frontmatter extraction.

    Thread-safety: Safe for concurrent use (no shared state)
    Performance: < 50ms per document (NFR-001)
    """

    def parse_document(self, file_path: Path) -> Document:
        """
        Parse markdown file to Document object.

        Args:
            file_path: Absolute path to .md file

        Returns:
            Document: Fully parsed document with:
                - Frontmatter metadata
                - Hierarchical sections
                - Detected references
                - File metadata

        Raises:
            FileNotFoundError: If file doesn't exist
            YAMLError: If frontmatter YAML is invalid
            ParseError: If markdown parsing fails

        Performance:
            - Simple doc (< 100 lines): ~5ms
            - Complex doc (500 lines, 20 sections): ~15ms
            - Large doc (2000 lines): ~40ms

        Example:
            >>> parser = ParserAPI()
            >>> doc = parser.parse_document(Path("docs/prd.md"))
            >>> print(doc.id, doc.title)
            PRD-001-V2 Product Requirements Document
        """

    def parse_string(
        self,
        content: str,
        file_path: Optional[Path] = None
    ) -> Document:
        """
        Parse markdown string (for testing or in-memory documents).

        Args:
            content: Markdown string with frontmatter
            file_path: Optional path (for metadata only)

        Returns:
            Document: Parsed document

        Raises:
            YAMLError: If frontmatter invalid
            ParseError: If markdown parsing fails

        Example:
            >>> content = '''---
            ... id: TEST-001
            ... title: Test
            ... ---
            ... # Section
            ... Content here.
            ... '''
            >>> doc = parser.parse_string(content)
        """

    def extract_frontmatter(self, content: str) -> dict:
        """
        Extract YAML frontmatter only (no markdown parsing).

        Args:
            content: Markdown string

        Returns:
            dict: Parsed YAML frontmatter (empty dict if no frontmatter)

        Raises:
            YAMLError: If frontmatter syntax invalid

        Performance: ~2ms per document

        Example:
            >>> content = "---\\nid: TEST-001\\n---\\n# Body"
            >>> fm = parser.extract_frontmatter(content)
            >>> fm['id']
            'TEST-001'
        """

    def parse_sections(self, markdown: str) -> list[Section]:
        """
        Parse markdown to hierarchical section tree.

        Args:
            markdown: Markdown body (no frontmatter)

        Returns:
            list[Section]: Top-level sections with nested children

        Algorithm:
            Stack-based hierarchy construction (O(n))

        Example:
            >>> markdown = "# H1\\n## H2\\n### H3\\n## H2-2"
            >>> sections = parser.parse_sections(markdown)
            >>> len(sections)  # One H1 with children
            1
            >>> len(sections[0].children)  # Two H2 children
            2
        """

    def detect_references(self, content: str) -> dict[str, list[str]]:
        """
        Detect inline references in content.

        Detects:
            - Evidence notes: [E-XXX]
            - Document refs: PRD-001, TDD-001, etc.
            - ADR refs: ADR-005

        Args:
            content: Markdown content

        Returns:
            dict with keys:
                - 'evidence': list of [E-XXX] IDs
                - 'documents': list of document IDs
                - 'adrs': list of ADR IDs

        Performance: ~1ms per document

        Example:
            >>> content = "See [E-001] and PRD-001 and ADR-005"
            >>> refs = parser.detect_references(content)
            >>> refs['evidence']
            ['E-001']
            >>> refs['documents']
            ['PRD-001']
            >>> refs['adrs']
            ['ADR-005']
        """
```

---

## Validator API

**Module**: `src/core/validator.py`

### ValidatorAPI Class

```python
from models.document import Document
from models.schema import DocumentSchema
from models.gap import Gap, ValidationResult

class ValidatorAPI:
    """
    Document validation against type schemas.

    Thread-safety: Safe for concurrent use
    Performance: < 50ms per document (NFR-001)
    """

    def validate_document(
        self,
        doc: Document,
        schema: DocumentSchema
    ) -> ValidationResult:
        """
        Validate document against schema.

        Checks:
            1. Frontmatter fields (required, constraints)
            2. Required sections (presence, min_items)
            3. Placeholders (TODO, TBD, etc.)
            4. Evidence notes count
            5. Storytelling vs bullet lists

        Args:
            doc: Parsed document
            schema: Document type schema

        Returns:
            ValidationResult with:
                - valid: bool
                - gaps: list[Gap]
                - errors: list[str]
                - warnings: list[str]

        Performance: ~8ms per document

        Example:
            >>> validator = ValidatorAPI()
            >>> schema = loader.load_schema("prd")
            >>> result = validator.validate_document(doc, schema)
            >>> if not result.valid:
            ...     print(f"Found {len(result.gaps)} gaps")
        """

    def load_schema(self, doc_type: str) -> DocumentSchema:
        """
        Load schema from YAML file.

        Args:
            doc_type: Document type (prd, tdd, adr, etc.)

        Returns:
            DocumentSchema: Loaded and cached schema

        Raises:
            FileNotFoundError: If schema file not found

        Caching: Schemas cached in memory after first load

        Example:
            >>> schema = validator.load_schema("prd")
            >>> schema.document_type
            'prd'
        """

    def check_required_sections(
        self,
        doc: Document,
        schema: DocumentSchema
    ) -> list[Gap]:
        """
        Check for missing required sections (E110).

        Args:
            doc: Document to check
            schema: Schema with required_sections

        Returns:
            list[Gap]: E110 gaps for missing sections

        Example:
            >>> gaps = validator.check_required_sections(doc, schema)
            >>> for gap in gaps:
            ...     print(gap.description)
            Missing required section: User Personas
        """

    def detect_placeholders(self, doc: Document) -> list[Gap]:
        """
        Detect TODO/TBD/PLACEHOLDER markers (E120).

        Patterns:
            - TODO, TBD, PLACEHOLDER, XXX, FIXME
            - [], ..., ???

        Args:
            doc: Document to check

        Returns:
            list[Gap]: E120 gaps with line numbers

        Example:
            >>> gaps = validator.detect_placeholders(doc)
            >>> gaps[0].location
            'Line 45'
        """

    def check_evidence_notes(
        self,
        doc: Document,
        min_count: int = 5
    ) -> list[Gap]:
        """
        Check for sufficient evidence notes (E170).

        Args:
            doc: Document to check
            min_count: Minimum [E-XXX] references required

        Returns:
            list[Gap]: E170 gap if count < min_count

        Example:
            >>> gap = validator.check_evidence_notes(doc, min_count=10)
            >>> if gap:
            ...     print(f"Found {len(doc.evidence_ids)} evidence notes, need 10")
        """

    def check_storytelling(self, doc: Document) -> list[Gap]:
        """
        Check for storytelling vs bullet lists (E180).

        Heuristic:
            - Ratio of bullet points to paragraphs
            - Sections with only lists (no prose)
            - Lack of narrative connectors

        Args:
            doc: Document to check

        Returns:
            list[Gap]: E180 gaps for sections lacking narrative

        Example:
            >>> gaps = validator.check_storytelling(doc)
        """

    def check_alternatives(self, doc: Document) -> list[Gap]:
        """
        Check for documented alternatives (E190).

        Applicable to:
            - Decision documents (ADR, TDD, RFC)
            - Documents with 'alternatives' in frontmatter

        Args:
            doc: Document to check

        Returns:
            list[Gap]: E190 gap if alternatives missing

        Example:
            >>> gap = validator.check_alternatives(adr_doc)
            >>> gap.description
            'Missing alternatives section in decision document'
        """

    def check_postmortem(self, doc: Document) -> list[Gap]:
        """
        Check for post-mortem (E200).

        Trigger:
            - Doc status = 'completed' or 'deployed'
            - > 90 days since completion
            - No post-mortem satellite

        Args:
            doc: Document to check

        Returns:
            list[Gap]: E200 gap if post-mortem needed but missing
        """
```

---

## Graph Builder API

**Module**: `src/core/graph_builder.py`

### GraphBuilderAPI Class

```python
import networkx as nx
from models.document import Document
from typing import Optional

class GraphBuilderAPI:
    """
    Dependency graph construction and analysis.

    Thread-safety: NOT thread-safe (graph mutation)
    Performance: < 2s for 100 documents (NFR-002)
    """

    def build_graph(self, docs: list[Document]) -> nx.DiGraph:
        """
        Build directed graph from documents.

        Graph structure:
            - Nodes = documents (metadata as node attributes)
            - Edges = typed dependencies (requires, informs, etc.)

        Args:
            docs: List of parsed documents

        Returns:
            nx.DiGraph with:
                - Node attributes: doc_type, status, gap_count, etc.
                - Edge attributes: edge_type, reason, cascade, etc.

        Performance:
            - 10 docs: ~80ms
            - 100 docs: ~800ms
            - 1000 docs: ~12s

        Example:
            >>> builder = GraphBuilderAPI()
            >>> graph = builder.build_graph(documents)
            >>> len(graph.nodes())
            42
            >>> len(graph.edges())
            67
        """

    def add_document(self, graph: nx.DiGraph, doc: Document) -> None:
        """
        Add/update single document in graph (incremental update).

        Steps:
            1. Remove old node (if exists)
            2. Add new node with metadata
            3. Parse dependencies from frontmatter
            4. Add edges
            5. Update hierarchy (incremental)

        Args:
            graph: Existing graph (modified in-place)
            doc: Document to add

        Performance: ~10ms (vs 800ms full rebuild for 100 docs)

        Example:
            >>> builder.add_document(graph, new_doc)
        """

    def remove_document(self, graph: nx.DiGraph, doc_id: str) -> None:
        """
        Remove document from graph.

        Args:
            graph: Graph (modified in-place)
            doc_id: Document ID to remove

        Side effects:
            - Removes node
            - Removes all edges to/from node
            - Updates hierarchy
        """

    def detect_cycles(self, graph: nx.DiGraph) -> list[list[str]]:
        """
        Detect circular dependencies.

        Algorithm:
            Johnson's algorithm via NetworkX (O(V + E + C))

        Args:
            graph: Dependency graph

        Returns:
            list of cycles, each cycle = list of node IDs
            Empty list if DAG (no cycles)

        Example:
            >>> cycles = builder.detect_cycles(graph)
            >>> if cycles:
            ...     print(f"Found {len(cycles)} cycles:")
            ...     for cycle in cycles:
            ...         print(" → ".join(cycle))
            Found 1 cycles:
            PRD-001 → TDD-001 → PRD-001
        """

    def calculate_hierarchy(self, graph: nx.DiGraph) -> dict[str, int]:
        """
        Calculate emergent hierarchy levels.

        Algorithm:
            Topological sort, level = max(parent_levels) + 1

        Args:
            graph: Dependency graph

        Returns:
            dict mapping doc_id → level (0 = root/orphan)

        Example:
            >>> hierarchy = builder.calculate_hierarchy(graph)
            >>> hierarchy['PRD-001']
            0
            >>> hierarchy['TDD-001']
            1
        """

    def find_path(
        self,
        graph: nx.DiGraph,
        source: str,
        target: str
    ) -> Optional[list[str]]:
        """
        Find shortest dependency path.

        Args:
            graph: Dependency graph
            source: Starting document ID
            target: Target document ID

        Returns:
            list[str]: Path as document IDs, or None if no path

        Example:
            >>> path = builder.find_path(graph, "PRD-001", "IMPL-005")
            >>> path
            ['PRD-001', 'TDD-001', 'IMPL-005']
        """

    def get_subgraph(
        self,
        graph: nx.DiGraph,
        doc_ids: list[str]
    ) -> nx.DiGraph:
        """
        Extract subgraph containing only specified documents.

        Args:
            graph: Full graph
            doc_ids: Document IDs to include

        Returns:
            nx.DiGraph: Subgraph with only specified nodes and edges between them

        Example:
            >>> subgraph = builder.get_subgraph(graph, ["PRD-001", "TDD-001"])
        """
```

---

## Gap Engine API

**Module**: `src/core/gap_engine.py`

### GapEngineAPI Class

```python
from models.document import Document
from models.gap import Gap
import networkx as nx

class GapEngineAPI:
    """
    Comprehensive gap detection (E110-E200).

    Thread-safety: Safe for concurrent use
    Performance: < 2s for 100 documents (NFR)
    """

    def detect_all_gaps(
        self,
        docs: list[Document],
        graph: nx.DiGraph
    ) -> list[Gap]:
        """
        Detect all gap types across documents.

        Gap types:
            - E110-E120, E170-E200: Validator gaps
            - E130-E160: Graph gaps

        Args:
            docs: All documents
            graph: Dependency graph

        Returns:
            list[Gap]: All detected gaps, sorted by priority

        Performance:
            - 100 docs: ~1.2s
            - 1000 docs: ~18s

        Example:
            >>> engine = GapEngineAPI()
            >>> gaps = engine.detect_all_gaps(documents, graph)
            >>> critical = [g for g in gaps if g.severity == 'critical']
            >>> print(f"{len(critical)} critical gaps")
        """

    def detect_graph_gaps(self, graph: nx.DiGraph) -> list[Gap]:
        """
        Detect graph-based gaps (E130, E140, E150, E160).

        Args:
            graph: Dependency graph

        Returns:
            list[Gap]: Graph-related gaps
        """

    def detect_validator_gaps(self, docs: list[Document]) -> list[Gap]:
        """
        Detect validator gaps (E110, E120, E170, E180, E190, E200).

        Args:
            docs: Documents to validate

        Returns:
            list[Gap]: Validation gaps
        """

    def generate_remediation(self, gap: Gap) -> list[str]:
        """
        Generate actionable remediation steps.

        Uses gap-type-specific templates with context filling.

        Args:
            gap: Gap to remediate

        Returns:
            list[str]: Concrete steps (e.g., "Create docs/evidence/E-042.md")

        Example:
            >>> steps = engine.generate_remediation(gap)
            >>> for step in steps:
            ...     print(f"→ {step}")
            → Add section matching pattern: ^## User Personas
            → Use template: templates/prd-template.md
        """

    def prioritize_gaps(self, gaps: list[Gap]) -> list[Gap]:
        """
        Sort gaps by priority (severity × impact).

        Priority formula:
            priority = severity_weight × impact_factor
            - severity: critical=100, high=50, medium=20, low=5
            - impact: blocks_cascade=3, critical_path=2, standard=1

        Args:
            gaps: Unsorted gaps

        Returns:
            list[Gap]: Sorted by priority (descending)

        Example:
            >>> sorted_gaps = engine.prioritize_gaps(gaps)
            >>> sorted_gaps[0].priority_score
            300  # Critical gap blocking cascade
        """

    def generate_todo_list(self, gaps: list[Gap]) -> str:
        """
        Generate TODO.md markdown from gaps.

        Format:
            # TODO List (Generated from Gaps)

            ## PRD-001 (3 gaps)
            - [ ] **[E110-CRITICAL]** Add section: User Personas
              - Add section matching pattern: ^## User Personas
            - [ ] **[E120-HIGH]** Replace TODO at line 45

        Args:
            gaps: Detected gaps

        Returns:
            str: Formatted markdown TODO list

        Example:
            >>> todo_md = engine.generate_todo_list(gaps)
            >>> Path("TODO.md").write_text(todo_md)
        """
```

---

## Gate Manager API

**Module**: `src/core/gate_manager.py`

### GateManagerAPI Class

```python
from models.document import Document
from models.gap import Gap
import networkx as nx

class GateManagerAPI:
    """
    Quality gate management (DoR, DoD, Implementation Log).

    Thread-safety: Safe for concurrent use
    """

    def check_gate(
        self,
        doc: Document,
        gate_name: str,
        gaps: list[Gap]
    ) -> dict:
        """
        Check if document passes quality gate.

        Args:
            doc: Document to check
            gate_name: Gate name (e.g., "REQ-FREEZE", "DESIGN-COMPLETE")
            gaps: Current gaps for document

        Returns:
            dict with:
                - passed: bool
                - blockers: list[str] (gap IDs blocking gate)
                - warnings: list[str]

        Example:
            >>> result = gate_mgr.check_gate(doc, "REQ-FREEZE", gaps)
            >>> if not result['passed']:
            ...     print(f"Blocked by: {result['blockers']}")
        """

    def evaluate_dor(self, doc: Document) -> dict:
        """
        Evaluate Definition of Ready.

        Checks:
            - All dependencies completed
            - No critical gaps
            - Required evidence present

        Args:
            doc: Document to evaluate

        Returns:
            dict with passed, blockers, warnings
        """

    def evaluate_dod(self, doc: Document, graph: nx.DiGraph) -> dict:
        """
        Evaluate Definition of Done.

        Checks:
            - All acceptance criteria met
            - No gaps (or only low severity)
            - Approvals obtained
            - Implementation log complete (if applicable)

        Args:
            doc: Document to evaluate
            graph: Graph (for dependency checks)

        Returns:
            dict with passed, blockers, warnings
        """
```

---

## Storage API

**Module**: `src/storage/storage_api.py`

```python
from pathlib import Path
from typing import Optional
from models.document import Document
from models.provenance import ProvenanceRecord

class StorageAPI:
    """
    Hybrid storage facade (files + SQLite index).

    Thread-safety: Thread-safe for reads, NOT for writes (use locks)
    """

    def __init__(self, workspace_path: Path, db_path: Path):
        """
        Initialize hybrid storage.

        Args:
            workspace_path: Root of markdown files
            db_path: SQLite database file
        """

    def get_document(self, doc_id: str) -> Optional[Document]:
        """
        Get document by ID.

        Strategy:
            1. Check SQLite cache (metadata + hash)
            2. If stale or missing → read from file
            3. Update cache if needed

        Args:
            doc_id: Document ID

        Returns:
            Document or None if not found

        Performance:
            - Cache hit: ~5ms
            - Cache miss: ~20ms (parse + index)

        Example:
            >>> doc = storage.get_document("PRD-001-V2")
        """

    def search_documents(self, query: str, limit: int = 100) -> list[Document]:
        """
        Full-text search using SQLite FTS5.

        Query syntax:
            - "parser validation" → both terms (AND)
            - "parser OR validation" → either term
            - "parser -validation" → exclude term
            - '"exact phrase"' → phrase match

        Args:
            query: FTS5 search query
            limit: Max results

        Returns:
            list[Document]: Ranked by relevance

        Performance: < 100ms for 10k documents (NFR)

        Example:
            >>> results = storage.search_documents("architecture decision")
            >>> for doc in results[:5]:
            ...     print(doc.title)
        """

    def save_document(self, doc: Document) -> None:
        """
        Save document to file and update index.

        Steps:
            1. Write markdown file
            2. Update SQLite index
            3. Record provenance

        Args:
            doc: Document to save

        Side effects:
            - Writes {workspace}/{doc.type}/{doc.id}.md
            - Updates SQLite index
            - Creates provenance record

        Example:
            >>> storage.save_document(doc)
        """

    def rebuild_index(self) -> None:
        """
        Rebuild SQLite index from all files.

        Use cases:
            - Database corrupted
            - Schema upgrade
            - Manual cache clear

        Performance:
            - 100 docs: ~2s
            - 1000 docs: ~18s

        Example:
            >>> storage.rebuild_index()
        """

    def get_provenance(self, doc_id: str) -> list[ProvenanceRecord]:
        """
        Get provenance trail for document.

        Args:
            doc_id: Document ID

        Returns:
            list[ProvenanceRecord]: All changes (CREATE, UPDATE, DELETE)

        Example:
            >>> trail = storage.get_provenance("PRD-001")
            >>> for record in trail:
            ...     print(f"{record.timestamp}: {record.operation}")
        """
```

---

## GUI API

**Module**: `src/gui/main_window.py`

### Signal/Slot Interface

```python
from PySide6.QtCore import Signal, Slot, QObject
from models.document import Document
from models.gap import Gap

class MainWindow(QMainWindow):
    """
    Main application window.

    Signals (outbound):
        - document_selected(str): User selected document
        - gap_selected(Gap): User selected gap
        - remediation_requested(Gap): User clicked "Fix"
    """

    # Signals
    document_selected = Signal(str)  # doc_id
    gap_selected = Signal(Gap)
    remediation_requested = Signal(Gap)

    @Slot(str)
    def load_workspace(self, workspace_path: str) -> None:
        """
        Load documentation workspace.

        Args:
            workspace_path: Path to docs directory

        Emits:
            document_selected: After loading first document
        """

    @Slot(str)
    def select_document(self, doc_id: str) -> None:
        """
        Select document for preview.

        Side effects:
            - Highlights node in graph
            - Renders markdown in preview
            - Shows gaps in panel

        Args:
            doc_id: Document ID
        """

    @Slot(Gap)
    def show_remediation(self, gap: Gap) -> None:
        """
        Display remediation dialog for gap.

        Args:
            gap: Gap to remediate
        """
```

---

## Domain API

**Module**: `src/domains/base_domain.py`

### BaseDomain Class

```python
from abc import ABC, abstractmethod
from models.document import Document
from models.gap import Gap

class BaseDomain(ABC):
    """
    Abstract base class for logical domains.

    Domains:
        - requirements
        - architecture
        - testing
        - operations
    """

    @abstractmethod
    def validate_domain_rules(self, doc: Document) -> list[Gap]:
        """
        Domain-specific validation rules.

        Args:
            doc: Document to validate

        Returns:
            list[Gap]: Domain-specific gaps

        Example (Requirements domain):
            - Check FR → Test coverage
            - Check stakeholder approvals
        """

    @abstractmethod
    def get_templates(self) -> list[str]:
        """
        Get template file names for domain.

        Returns:
            list[str]: Template filenames (e.g., ["prd-template.md"])
        """
```

---

## Error Codes

**Standard error responses**:

```python
class APIError(Exception):
    """Base API error."""

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

# Error codes
E_FILE_NOT_FOUND = "FILE_NOT_FOUND"
E_INVALID_YAML = "INVALID_YAML"
E_PARSE_ERROR = "PARSE_ERROR"
E_VALIDATION_ERROR = "VALIDATION_ERROR"
E_SCHEMA_NOT_FOUND = "SCHEMA_NOT_FOUND"
E_GRAPH_CYCLE = "GRAPH_CYCLE"
E_DATABASE_ERROR = "DATABASE_ERROR"
```

---

## Performance Summary

| API | Operation | Target | Achieved |
|-----|-----------|--------|----------|
| **Parser** | parse_document | < 50ms | ~10ms ✅ |
| **Validator** | validate_document | < 50ms | ~8ms ✅ |
| **Graph** | build_graph (100 docs) | < 2s | ~800ms ✅ |
| **Gap** | detect_all_gaps (100 docs) | < 2s | ~1.2s ✅ |
| **Storage** | search (10k docs) | < 100ms | ~60ms ✅ |
| **GUI** | UI response | < 100ms | ~50ms ✅ |

**Evidence**: [E-143], [E-145], [E-146], [E-149], [E-151], [E-153]

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [DATA-MODEL-001](../data-models/DATA-MODEL-001.md)
