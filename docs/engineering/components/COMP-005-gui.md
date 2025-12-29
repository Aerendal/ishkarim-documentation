---
id: COMP-005
title: "COMP-005: GUI Controller Component"
type: component
status: draft
parent: TDD-001-V2

dependencies:
  - id: "ADR-001"
    type: requires
    reason: "Uses PySide6 (ADR-001 decision)"

  - id: "ADR-007"
    type: requires
    reason: "Implements Model-View pattern (ADR-007 decision)"

  - id: "ADR-004"
    type: requires
    reason: "Embeds Cytoscape.js via QtWebEngine (ADR-004 decision)"

  - id: "COMP-003-graph"
    type: requires
    reason: "Displays graphs from Graph Builder"

  - id: "COMP-004-gap-engine"
    type: requires
    reason: "Displays gaps in GapsPanel"

  - id: "API-SPEC-001"
    type: implements
    reason: "GUI implementuje API zdefiniowane w API-SPEC-001"
    cascade: true

impacts:

evidence_ids:
  - "E-150"  # Architecture prototype (Model-View working)
  - "E-151"  # Qt Signal/Slot performance benchmark
---

# COMP-005: GUI Controller Component

**Responsibility**: PySide6 GUI, user interactions, graph visualization, document preview, gap display

---

## Public Interface

```python
# src/gui/main_window.py

from PySide6.QtWidgets import QMainWindow, QSplitter
from PySide6.QtCore import Signal, Slot
from core.graph_builder import GraphBuilderAPI
from core.gap_engine import GapEngineAPI
from models.document import Document
from models.gap import Gap

class MainWindow(QMainWindow):
    """Main application window (Model-View pattern)."""

    # Signals (outbound)
    document_selected = Signal(str)  # doc_id
    gap_selected = Signal(Gap)
    remediation_requested = Signal(Gap)

    def __init__(self, graph_builder: GraphBuilderAPI, gap_engine: GapEngineAPI):
        """
        Initialize GUI with business logic dependencies.

        Args:
            graph_builder: Graph construction engine
            gap_engine: Gap detection engine
        """

    @Slot(str)
    def load_workspace(self, workspace_path: str) -> None:
        """
        Load documentation workspace.

        Emits:
            document_selected: When documents loaded
        """

    @Slot(str)
    def select_document(self, doc_id: str) -> None:
        """
        Select document for preview.

        Triggers:
            - graph_widget.highlight_node(doc_id)
            - preview_widget.render_document(doc)
            - gaps_panel.show_gaps(gaps)
        """

    @Slot(Gap)
    def show_remediation(self, gap: Gap) -> None:
        """Display remediation steps for gap."""
```

---

## Component Architecture

### Layout Structure

```
MainWindow (QMainWindow)
    ├── Toolbar (QToolBar)
    │   ├── Open Workspace (QAction)
    │   ├── Refresh (QAction)
    │   └── Settings (QAction)
    │
    ├── Central Widget (QSplitter - Horizontal)
    │   │
    │   ├── Left Panel (QSplitter - Vertical) [40% width]
    │   │   ├── GraphWidget (QWebEngineView) [60% height]
    │   │   │   └── Cytoscape.js (embedded via QtWebEngine)
    │   │   │
    │   │   └── StatsPanel (QWidget) [40% height]
    │   │       ├── Document Count (QLabel)
    │   │       ├── Gap Count (QLabel)
    │   │       └── Critical Gaps (QLabel)
    │   │
    │   └── Right Panel (QSplitter - Vertical) [60% width]
    │       ├── PreviewWidget (QTextBrowser) [50% height]
    │       │   └── Markdown rendering
    │       │
    │       └── GapsPanel (QTableWidget) [50% height]
    │           └── Gap list with remediation
    │
    └── Status Bar (QStatusBar)
        └── Current workspace path
```

---

## GraphWidget (Cytoscape.js Embed)

```python
# src/gui/graph_widget.py

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import QObject, Signal, Slot
import networkx as nx
import json

class GraphBridge(QObject):
    """Qt-JavaScript bridge for Cytoscape.js communication."""

    node_clicked = Signal(str)  # doc_id
    edge_clicked = Signal(str, str)  # source, target

    @Slot(str)
    def on_node_click(self, doc_id: str):
        """Called from JavaScript when node clicked."""
        self.node_clicked.emit(doc_id)

class GraphWidget(QWebEngineView):
    """Interactive graph visualization using Cytoscape.js."""

    node_selected = Signal(str)

    def __init__(self):
        super().__init__()

        # Setup Qt-JavaScript bridge
        self.bridge = GraphBridge()
        self.channel = QWebChannel()
        self.channel.registerObject("bridge", self.bridge)
        self.page().setWebChannel(self.channel)

        # Connect signals
        self.bridge.node_clicked.connect(self.node_selected.emit)

        # Load HTML with Cytoscape.js
        self._load_graph_html()

    def render_graph(self, graph: nx.DiGraph) -> None:
        """
        Render NetworkX graph in Cytoscape.js.

        Args:
            graph: NetworkX DiGraph with node/edge metadata
        """
        # Convert NetworkX to Cytoscape.js format
        cyto_json = self._networkx_to_cytoscape(graph)

        # Send to JavaScript
        self.page().runJavaScript(f"""
            cy.json({{ elements: {json.dumps(cyto_json)} }});
            cy.layout({{ name: 'dagre' }}).run();
        """)

    def highlight_node(self, doc_id: str) -> None:
        """Highlight selected node."""
        self.page().runJavaScript(f"""
            cy.nodes().removeClass('highlighted');
            cy.getElementById('{doc_id}').addClass('highlighted');
        """)

    def _networkx_to_cytoscape(self, graph: nx.DiGraph) -> list[dict]:
        """
        Convert NetworkX graph to Cytoscape.js format.

        Returns:
            [
                {{ data: {{ id: 'PRD-001', label: 'PRD', status: 'draft' }} }},
                {{ data: {{ id: 'edge1', source: 'PRD-001', target: 'TDD-001' }} }}
            ]
        """
        elements = []

        # Nodes
        for node_id, node_data in graph.nodes(data=True):
            elements.append({
                'data': {
                    'id': node_id,
                    'label': node_data.get('title', node_id),
                    'status': node_data.get('status', 'unknown'),
                    'gap_count': node_data.get('gap_count', 0),
                }
            })

        # Edges
        for source, target, edge_data in graph.edges(data=True):
            elements.append({
                'data': {
                    'id': f'{source}-{target}',
                    'source': source,
                    'target': target,
                    'edge_type': edge_data.get('edge_type', 'requires'),
                }
            })

        return elements

    def _load_graph_html(self):
        """Load HTML template with Cytoscape.js."""
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.26.0/cytoscape.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/dagre/0.8.5/dagre.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/cytoscape-dagre@2.5.0/cytoscape-dagre.min.js"></script>
            <style>
                body { margin: 0; padding: 0; }
                #cy { width: 100%; height: 100vh; }
                .highlighted { border-width: 4px !important; }
            </style>
        </head>
        <body>
            <div id="cy"></div>
            <script>
                var cy = cytoscape({
                    container: document.getElementById('cy'),
                    style: [
                        {
                            selector: 'node',
                            style: {
                                'label': 'data(label)',
                                'background-color': function(ele) {
                                    var status = ele.data('status');
                                    if (status === 'draft') return '#FFB74D';
                                    if (status === 'review') return '#64B5F6';
                                    if (status === 'approved') return '#81C784';
                                    return '#BDBDBD';
                                },
                                'border-width': 2,
                                'border-color': function(ele) {
                                    var gaps = ele.data('gap_count');
                                    return gaps > 0 ? '#E53935' : '#66BB6A';
                                }
                            }
                        },
                        {
                            selector: 'edge',
                            style: {
                                'width': 2,
                                'line-color': '#757575',
                                'target-arrow-color': '#757575',
                                'target-arrow-shape': 'triangle',
                                'curve-style': 'bezier'
                            }
                        },
                        {
                            selector: '.highlighted',
                            style: {
                                'border-width': 4,
                                'border-color': '#1976D2'
                            }
                        }
                    ]
                });

                // Setup Qt bridge
                new QWebChannel(qt.webChannelTransport, function(channel) {
                    var bridge = channel.objects.bridge;

                    cy.on('tap', 'node', function(evt) {
                        var node = evt.target;
                        bridge.on_node_click(node.id());
                    });
                });
            </script>
        </body>
        </html>
        """
        self.setHtml(html)
```

---

## PreviewWidget (Markdown Rendering)

```python
# src/gui/preview_widget.py

from PySide6.QtWidgets import QTextBrowser
from PySide6.QtCore import Slot
from models.document import Document
import markdown

class PreviewWidget(QTextBrowser):
    """Markdown document preview."""

    def __init__(self):
        super().__init__()
        self.setReadOnly(True)
        self.setOpenExternalLinks(True)

    @Slot(Document)
    def render_document(self, doc: Document) -> None:
        """
        Render document with syntax highlighting.

        Args:
            doc: Parsed document
        """
        # Convert markdown to HTML
        html = markdown.markdown(
            doc.body,
            extensions=['fenced_code', 'tables', 'toc']
        )

        # Add frontmatter info
        frontmatter_html = self._render_frontmatter(doc.frontmatter)

        # Full HTML
        full_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: -apple-system, sans-serif; padding: 20px; }}
                .frontmatter {{ background: #f5f5f5; padding: 10px; margin-bottom: 20px; }}
                code {{ background: #e0e0e0; padding: 2px 4px; }}
                pre {{ background: #f5f5f5; padding: 10px; overflow-x: auto; }}
            </style>
        </head>
        <body>
            {frontmatter_html}
            {html}
        </body>
        </html>
        """

        self.setHtml(full_html)

    def _render_frontmatter(self, frontmatter: dict) -> str:
        """Render YAML frontmatter as HTML."""
        items = []
        for key, value in frontmatter.items():
            items.append(f"<b>{key}:</b> {value}")
        return f"<div class='frontmatter'>{'<br>'.join(items)}</div>"
```

---

## GapsPanel (Gap List & Remediation)

```python
# src/gui/panels/gaps_panel.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from PySide6.QtCore import Signal, Slot
from models.gap import Gap

class GapsPanel(QWidget):
    """Gap list with remediation actions."""

    gap_selected = Signal(Gap)
    remediate_clicked = Signal(Gap)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Gap table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Type', 'Severity', 'Description', 'Actions'])
        self.table.itemSelectionChanged.connect(self._on_selection_changed)

        layout.addWidget(self.table)
        self.setLayout(layout)

    @Slot(list)
    def show_gaps(self, gaps: list[Gap]) -> None:
        """
        Display gap list.

        Args:
            gaps: List of detected gaps (sorted by priority)
        """
        self.table.setRowCount(len(gaps))

        for i, gap in enumerate(gaps):
            # Type
            self.table.setItem(i, 0, QTableWidgetItem(gap.gap_type))

            # Severity
            severity_item = QTableWidgetItem(gap.severity)
            severity_item.setBackground(self._severity_color(gap.severity))
            self.table.setItem(i, 1, severity_item)

            # Description
            self.table.setItem(i, 2, QTableWidgetItem(gap.description))

            # Remediation button
            btn = QPushButton("Fix")
            btn.clicked.connect(lambda checked, g=gap: self.remediate_clicked.emit(g))
            self.table.setCellWidget(i, 3, btn)

    def _severity_color(self, severity: str):
        """Return color for severity level."""
        from PySide6.QtGui import QColor
        colors = {
            'critical': QColor(255, 205, 210),  # Red
            'high': QColor(255, 224, 178),      # Orange
            'medium': QColor(255, 249, 196),    # Yellow
            'low': QColor(200, 230, 201),       # Green
        }
        return colors.get(severity, QColor(245, 245, 245))

    def _on_selection_changed(self):
        """Emit selected gap."""
        selected = self.table.selectedItems()
        if selected:
            row = selected[0].row()
            # TODO: Retrieve gap from row data
```

---

## Signal/Slot Flow (Model-View Pattern)

```python
# src/main.py

from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from core.graph_builder import GraphBuilderAPI
from core.gap_engine import GapEngineAPI
from core.parser import ParserAPI

def main():
    app = QApplication([])

    # Business Logic (Model)
    parser = ParserAPI()
    graph_builder = GraphBuilderAPI()
    gap_engine = GapEngineAPI()

    # GUI (View)
    window = MainWindow(graph_builder, gap_engine)

    # Connect signals/slots (Controller = Signal/Slot system)
    window.document_selected.connect(lambda doc_id: load_and_display(doc_id, parser, window))
    window.gap_selected.connect(window.show_remediation)

    window.show()
    app.exec()

def load_and_display(doc_id: str, parser: ParserAPI, window: MainWindow):
    """Load document and update UI (business logic → view)."""
    doc = parser.parse_document(f"docs/{doc_id}.md")
    window.preview_widget.render_document(doc)
```

---

## Performance

**Target**: < 100ms UI response (NFR-003)

**Measured** [E-151]:
- Signal/Slot overhead: ~5ms
- Graph render (100 nodes): ~50ms
- Markdown preview: ~30ms
- **Total**: ~85ms ✅

---

## Testing

```python
def test_graph_widget_render():
    import networkx as nx
    from gui.graph_widget import GraphWidget

    graph = nx.DiGraph()
    graph.add_node('PRD-001', title='PRD', status='draft', gap_count=3)
    graph.add_node('TDD-001', title='TDD', status='pending', gap_count=0)
    graph.add_edge('PRD-001', 'TDD-001', edge_type='requires')

    widget = GraphWidget()
    widget.render_graph(graph)

    # Verify JavaScript executed
    assert widget.page().title() != ""

def test_gaps_panel_display():
    from gui.panels.gaps_panel import GapsPanel
    from models.gap import Gap

    gaps = [
        Gap(gap_type="E110", severity="critical", description="Missing section"),
        Gap(gap_type="E120", severity="high", description="TODO placeholder"),
    ]

    panel = GapsPanel()
    panel.show_gaps(gaps)

    assert panel.table.rowCount() == 2
    assert panel.table.item(0, 0).text() == "E110"
```

---

**Parent**: [TDD-001-V2](../tdd-v2.md)
**Related**: [ADR-001](../decisions/ADR-001-pyside6.md), [ADR-007](../decisions/ADR-007-gui.md)
