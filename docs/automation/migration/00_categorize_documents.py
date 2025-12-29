#!/usr/bin/env python3
"""
Living Documentation Framework - Document Categorization

Categorizes documents into migration batches:
- Batch A: Living Documentation (full metadata)
- Batch B: Core Documents (basic metadata)
- Batch C: Satellite Documents (evidence, approvals, etc.)
- Excluded: Templates

Usage:
    python 00_categorize_documents.py
"""

import sys
from pathlib import Path
from collections import defaultdict
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from document_parser import DocumentParser


def categorize_documents(base_path: Path):
    """Categorize all documents for migration"""

    parser = DocumentParser(base_path)
    documents = parser.parse_directory(base_path, skip_templates=True)

    # Categorization
    batch_a = []  # Living Documentation (full metadata)
    batch_b = []  # Core Documents (basic metadata)
    batch_c = []  # Satellites (evidence, approvals, etc.)

    for doc in documents:
        file_rel = doc.file_path.relative_to(base_path)
        file_str = str(file_rel)

        # Batch A: Living Documentation (has extended metadata)
        if doc.has_living_doc_metadata:
            batch_a.append({
                'id': doc.id,
                'title': doc.title,
                'file': file_str,
                'type': doc.type,
                'status': doc.status
            })

        # Batch C: Satellites (Evidence, Approvals, TODOs, etc.)
        elif any(keyword in file_str for keyword in ['satellites/', 'evidence/', 'E-0', 'approvals/', 'todos/']):
            batch_c.append({
                'id': doc.id,
                'title': doc.title,
                'file': file_str,
                'type': doc.type,
                'status': doc.status
            })

        # Batch B: Core Documents (everything else)
        else:
            batch_b.append({
                'id': doc.id,
                'title': doc.title,
                'file': file_str,
                'type': doc.type,
                'status': doc.status
            })

    # Report
    report = {
        'generated': str(Path.cwd()),
        'total_documents': len(documents),
        'batch_a_living_docs': {
            'count': len(batch_a),
            'documents': sorted(batch_a, key=lambda x: x['id'])
        },
        'batch_b_core': {
            'count': len(batch_b),
            'documents': sorted(batch_b, key=lambda x: x['id'])
        },
        'batch_c_satellites': {
            'count': len(batch_c),
            'documents': sorted(batch_c, key=lambda x: x['id'])
        }
    }

    return report


def print_report(report: dict):
    """Print categorization report"""

    print("=" * 80)
    print("DOCUMENT CATEGORIZATION FOR MIGRATION")
    print("=" * 80)
    print()

    print(f"Total documents found: {report['total_documents']}")
    print()

    print("-" * 80)
    print(f"BATCH A: Living Documentation (Full Metadata) - {report['batch_a_living_docs']['count']} documents")
    print("-" * 80)
    for doc in report['batch_a_living_docs']['documents']:
        print(f"  {doc['id']:20s} | {doc['type']:15s} | {doc['file']}")
    print()

    print("-" * 80)
    print(f"BATCH B: Core Documents (Basic Metadata) - {report['batch_b_core']['count']} documents")
    print("-" * 80)
    for doc in report['batch_b_core']['documents']:
        print(f"  {doc['id']:20s} | {doc['type']:15s} | {doc['file']}")
    print()

    print("-" * 80)
    print(f"BATCH C: Satellite Documents (Evidence, Approvals, etc.) - {report['batch_c_satellites']['count']} documents")
    print("-" * 80)
    for doc in report['batch_c_satellites']['documents']:
        print(f"  {doc['id']:20s} | {doc['type']:15s} | {doc['file']}")
    print()

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  Batch A (Living Docs):  {report['batch_a_living_docs']['count']:3d}")
    print(f"  Batch B (Core):         {report['batch_b_core']['count']:3d}")
    print(f"  Batch C (Satellites):   {report['batch_c_satellites']['count']:3d}")
    print(f"  {'':21s}  {'─' * 5}")
    print(f"  Total:                  {report['total_documents']:3d}")
    print()


def main():
    base_path = Path(__file__).parent.parent.parent  # docs/

    print("Categorizing documents...\n")
    report = categorize_documents(base_path)

    # Print terminal report
    print_report(report)

    # Save JSON report
    output_file = Path(__file__).parent / "categorization-report.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"✓ JSON report saved to: {output_file}")
    print()


if __name__ == "__main__":
    main()
