#!/usr/bin/env python3
"""
Living Documentation Framework - Document Parser

Parses markdown documents with YAML front-matter and extracts
Living Documentation metadata.

Usage:
    from document_parser import DocumentParser

    parser = DocumentParser()
    doc = parser.parse("path/to/document.md")
    print(doc.id, doc.version, doc.status)
"""

import frontmatter
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Document:
    """Represents a parsed document with Living Documentation metadata"""

    # Basic metadata
    file_path: Path
    id: str
    title: str
    type: str
    domain: str
    status: str
    created: str
    updated: str
    owner: str

    # Living Documentation metadata
    version: Optional[str] = None
    version_metadata: Optional[Dict[str, Any]] = None
    version_history: List[Dict[str, Any]] = field(default_factory=list)

    status_metadata: Optional[Dict[str, Any]] = None
    lifecycle: Optional[Dict[str, Any]] = None

    cross_reference_status: Optional[Dict[str, Any]] = None
    document_health: Optional[Dict[str, Any]] = None
    deprecation: Optional[Dict[str, Any]] = None

    # Dependencies and impacts
    dependencies: List[str] = field(default_factory=list)
    impacts: List[str] = field(default_factory=list)

    # Raw front-matter
    front_matter: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Extract dependency and impact IDs from front-matter"""
        if not self.dependencies:
            deps = self.front_matter.get('dependencies', [])
            if isinstance(deps, list):
                self.dependencies = [d.get('id', d) if isinstance(d, dict) else d
                                   for d in deps]

        if not self.impacts:
            imps = self.front_matter.get('impacts', [])
            if isinstance(imps, list):
                self.impacts = [i.get('id', i) if isinstance(i, dict) else i
                              for i in imps]

    @property
    def has_living_doc_metadata(self) -> bool:
        """Check if document has Living Documentation Framework metadata"""
        return (
            self.version_metadata is not None or
            self.lifecycle is not None or
            self.document_health is not None
        )

    @property
    def health_status(self) -> Optional[str]:
        """Get document health status"""
        if self.document_health:
            return self.document_health.get('status')
        return None

    @property
    def is_deprecated(self) -> bool:
        """Check if document is deprecated"""
        return self.deprecation is not None and self.deprecation.get('status') == 'deprecated'

    @property
    def major_version(self) -> Optional[int]:
        """Get major version number"""
        if self.version_metadata:
            return self.version_metadata.get('major')
        return None

    @property
    def minor_version(self) -> Optional[int]:
        """Get minor version number"""
        if self.version_metadata:
            return self.version_metadata.get('minor')
        return None

    @property
    def patch_version(self) -> Optional[int]:
        """Get patch version number"""
        if self.version_metadata:
            return self.version_metadata.get('patch')
        return None


class DocumentParser:
    """Parser for Living Documentation Framework documents"""

    def __init__(self, base_path: Optional[Path] = None):
        """
        Initialize document parser

        Args:
            base_path: Base directory for resolving relative paths (default: current dir)
        """
        self.base_path = base_path or Path.cwd()

    def parse(self, file_path: str | Path) -> Document:
        """
        Parse a markdown document with YAML front-matter

        Args:
            file_path: Path to markdown file

        Returns:
            Document object with parsed metadata

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If required metadata is missing
        """
        file_path = Path(file_path)

        if not file_path.is_absolute():
            file_path = self.base_path / file_path

        if not file_path.exists():
            raise FileNotFoundError(f"Document not found: {file_path}")

        # Parse front-matter
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        metadata = post.metadata

        # Extract required fields
        try:
            doc = Document(
                file_path=file_path,
                id=metadata['id'],
                title=metadata['title'],
                type=metadata['type'],
                domain=metadata['domain'],
                status=metadata['status'],
                created=metadata['created'],
                updated=metadata['updated'],
                owner=metadata['owner'],

                # Living Documentation metadata
                version=metadata.get('version'),
                version_metadata=metadata.get('version_metadata'),
                version_history=metadata.get('version_history', []),

                status_metadata=metadata.get('status_metadata'),
                lifecycle=metadata.get('lifecycle'),

                cross_reference_status=metadata.get('cross_reference_status'),
                document_health=metadata.get('document_health'),
                deprecation=metadata.get('deprecation'),

                front_matter=metadata
            )
        except KeyError as e:
            raise ValueError(f"Missing required metadata field in {file_path}: {e}")

        return doc

    def parse_directory(self, directory: str | Path,
                       pattern: str = "**/*.md",
                       skip_templates: bool = True) -> List[Document]:
        """
        Parse all markdown documents in a directory

        Args:
            directory: Directory to scan
            pattern: Glob pattern for matching files (default: **/*.md)
            skip_templates: Skip files in templates/ directory (default: True)

        Returns:
            List of parsed Document objects
        """
        directory = Path(directory)

        if not directory.is_absolute():
            directory = self.base_path / directory

        documents = []

        for file_path in directory.glob(pattern):
            # Skip templates if requested
            if skip_templates and 'templates' in file_path.parts:
                continue

            try:
                doc = self.parse(file_path)
                documents.append(doc)
            except (ValueError, FileNotFoundError, yaml.YAMLError) as e:
                print(f"Warning: Failed to parse {file_path}: {e}")
                continue

        return documents

    def find_document_by_id(self, doc_id: str,
                           search_path: Optional[Path] = None) -> Optional[Document]:
        """
        Find a document by its ID

        Args:
            doc_id: Document ID to search for
            search_path: Directory to search (default: base_path)

        Returns:
            Document if found, None otherwise
        """
        search_path = search_path or self.base_path
        documents = self.parse_directory(search_path)

        for doc in documents:
            if doc.id == doc_id:
                return doc

        return None


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) < 2:
        print("Usage: python document_parser.py <path-to-markdown-file>")
        sys.exit(1)

    parser = DocumentParser()

    try:
        doc = parser.parse(sys.argv[1])

        print(f"Document ID: {doc.id}")
        print(f"Title: {doc.title}")
        print(f"Type: {doc.type}")
        print(f"Status: {doc.status}")
        print(f"Version: {doc.version}")
        print(f"Health: {doc.health_status}")
        print(f"Has Living Doc Metadata: {doc.has_living_doc_metadata}")
        print(f"Dependencies: {', '.join(doc.dependencies)}")
        print(f"Impacts: {', '.join(doc.impacts)}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
