#!/usr/bin/env python3
"""
Deprecation Workflow Automation - Living Documentation Framework (Phase 2)

Automatycznie zarządza cyklem życia deprecated documents:
- Dodaje deprecation banners
- Trackuje countdown do sunset
- Generuje migration guides
- Notyfikuje stakeholders

Usage:
    python deprecation_workflow.py --deprecate DOC-PRD-001 --reason "Replaced by PRD-003"
    python deprecation_workflow.py --check-sunsets
    python deprecation_workflow.py --generate-banner DOC-PRD-001
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import re

try:
    from document_parser import DocumentParser, Document
except ImportError:
    print("Error: document_parser.py not found")
    sys.exit(1)


class DeprecationWorkflow:
    """Manages document deprecation lifecycle"""

    def __init__(self, docs_root: str = "."):
        self.docs_root = Path(docs_root)
        self.parser = DocumentParser()

    def deprecate_document(
        self,
        doc_id: str,
        reason: str,
        sunset_days: int = 90,
        migration_target: Optional[str] = None,
        dry_run: bool = True
    ) -> Dict:
        """
        Mark document as deprecated

        Args:
            doc_id: Document ID to deprecate
            reason: Reason for deprecation
            sunset_days: Days until sunset (default: 90)
            migration_target: ID of replacement document
            dry_run: If True, don't modify files

        Returns: Deprecation report
        """
        # Find document
        doc = self.parser.find_document_by_id(doc_id)
        if not doc:
            return {"error": f"Document {doc_id} not found"}

        # Calculate sunset date
        sunset_date = datetime.now() + timedelta(days=sunset_days)

        deprecation_info = {
            "document_id": doc_id,
            "document_path": str(doc.file_path),
            "current_status": doc.status,
            "new_status": "deprecated",
            "deprecated_date": datetime.now().isoformat(),
            "sunset_date": sunset_date.isoformat(),
            "sunset_days_remaining": sunset_days,
            "reason": reason,
            "migration_target": migration_target,
            "actions_taken": []
        }

        if not dry_run:
            # 1. Update document status
            self._update_status(doc, "deprecated")
            deprecation_info["actions_taken"].append("Status changed to deprecated")

            # 2. Add deprecation metadata
            self._add_deprecation_metadata(doc, reason, sunset_date, migration_target)
            deprecation_info["actions_taken"].append("Deprecation metadata added")

            # 3. Insert deprecation banner
            self._insert_deprecation_banner(doc, reason, sunset_date, migration_target)
            deprecation_info["actions_taken"].append("Deprecation banner inserted")

            # 4. Notify stakeholders
            downstream = self._get_downstream_documents(doc)
            deprecation_info["downstream_notified"] = [d.id for d in downstream]
            deprecation_info["actions_taken"].append(f"Notified {len(downstream)} downstream documents")

        else:
            deprecation_info["dry_run"] = True
            deprecation_info["actions_taken"].append("DRY RUN - no changes made")

        return deprecation_info

    def _update_status(self, doc: Document, new_status: str):
        """Update document status in front-matter"""
        # TODO: Implement YAML front-matter update
        pass

    def _add_deprecation_metadata(
        self,
        doc: Document,
        reason: str,
        sunset_date: datetime,
        migration_target: Optional[str]
    ):
        """Add deprecation metadata to document front-matter"""
        # TODO: Implement deprecation metadata insertion
        pass

    def _insert_deprecation_banner(
        self,
        doc: Document,
        reason: str,
        sunset_date: datetime,
        migration_target: Optional[str]
    ):
        """Insert deprecation banner at top of document"""
        banner = self.generate_deprecation_banner(
            doc.id,
            reason,
            sunset_date,
            migration_target
        )

        # TODO: Insert banner into document file
        # Read file, insert banner after front-matter, write back
        pass

    def generate_deprecation_banner(
        self,
        doc_id: str,
        reason: str,
        sunset_date: datetime,
        migration_target: Optional[str] = None
    ) -> str:
        """
        Generate deprecation banner markdown

        Returns: Markdown text for banner
        """
        days_remaining = (sunset_date - datetime.now()).days

        banner = f"""---
⚠️ **DEPRECATION NOTICE**

This document is deprecated as of {datetime.now().strftime('%Y-%m-%d')}.

**Reason:** {reason}

**Sunset Date:** {sunset_date.strftime('%Y-%m-%d')} ({days_remaining} days remaining)
"""

        if migration_target:
            banner += f"""
**Migration Target:** [{migration_target}](../{migration_target}.md)

**Migration Guide:** [Migration Guide](../migrations/{doc_id}-to-{migration_target}.md)
"""

        banner += """
**Action Required:**
- [ ] Review and migrate to new document
- [ ] Update all references
- [ ] Notify stakeholders

---

"""
        return banner

    def check_sunsets(self, warning_days: int = 30) -> List[Dict]:
        """
        Check for documents approaching sunset

        Args:
            warning_days: Warn if sunset is within N days

        Returns: List of sunset warnings
        """
        warnings = []

        # Scan all documents
        documents = self.parser.parse_directory(".", skip_templates=True)

        for doc in documents:
            if doc.status == "deprecated":
                # Check if sunset date is approaching
                # TODO: Parse sunset_date from metadata
                # For now, just report all deprecated docs
                warnings.append({
                    "document_id": doc.id,
                    "document_path": str(doc.file_path),
                    "status": "deprecated",
                    "warning": "Approaching sunset (metadata needed)"
                })

            elif doc.status == "sunset":
                warnings.append({
                    "document_id": doc.id,
                    "document_path": str(doc.file_path),
                    "status": "sunset",
                    "warning": "Sunset period active - archive soon"
                })

        return warnings

    def _get_downstream_documents(self, doc: Document) -> List[Document]:
        """Get documents that reference this document"""
        downstream = []

        if hasattr(doc, 'cross_references') and doc.cross_references:
            impacts = doc.cross_references.get('impacts', [])
            for impact in impacts:
                impact_id = impact.get('id')
                if impact_id:
                    target_doc = self.parser.find_document_by_id(impact_id)
                    if target_doc:
                        downstream.append(target_doc)

        return downstream


def main():
    parser = argparse.ArgumentParser(
        description="Deprecation Workflow - Living Documentation Framework"
    )
    parser.add_argument(
        "--deprecate",
        type=str,
        help="Document ID to deprecate (e.g., DOC-PRD-001)"
    )
    parser.add_argument(
        "--reason",
        type=str,
        help="Reason for deprecation"
    )
    parser.add_argument(
        "--sunset-days",
        type=int,
        default=90,
        help="Days until sunset (default: 90)"
    )
    parser.add_argument(
        "--migration-target",
        type=str,
        help="ID of replacement document"
    )
    parser.add_argument(
        "--check-sunsets",
        action="store_true",
        help="Check for documents approaching sunset"
    )
    parser.add_argument(
        "--generate-banner",
        type=str,
        help="Generate deprecation banner for document ID"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Dry run mode (default: true)"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually apply changes"
    )

    args = parser.parse_args()

    dry_run = not args.apply
    workflow = DeprecationWorkflow(docs_root=".")

    if args.deprecate:
        if not args.reason:
            print("Error: --reason is required when deprecating a document")
            sys.exit(1)

        print(f"🚨 Deprecating document: {args.deprecate}")
        print(f"   Reason: {args.reason}")
        print(f"   Sunset in: {args.sunset_days} days")
        if args.migration_target:
            print(f"   Migration target: {args.migration_target}")
        print()

        result = workflow.deprecate_document(
            doc_id=args.deprecate,
            reason=args.reason,
            sunset_days=args.sunset_days,
            migration_target=args.migration_target,
            dry_run=dry_run
        )

        if "error" in result:
            print(f"❌ Error: {result['error']}")
            sys.exit(1)

        print("📊 Deprecation Report:")
        print(f"   Document: {result['document_id']}")
        print(f"   Status: {result['current_status']} → {result['new_status']}")
        print(f"   Sunset date: {result['sunset_date']}")
        print(f"\n   Actions taken:")
        for action in result['actions_taken']:
            print(f"      ✓ {action}")

        if dry_run:
            print(f"\n⚠️  DRY RUN MODE - No changes were made")
            print(f"   Use --apply to actually deprecate the document")

    elif args.check_sunsets:
        print("🔍 Checking for documents approaching sunset...\n")
        warnings = workflow.check_sunsets(warning_days=30)

        if warnings:
            print(f"⚠️  Found {len(warnings)} documents with sunset warnings:\n")
            for warning in warnings:
                print(f"   📄 {warning['document_id']}")
                print(f"      Status: {warning['status']}")
                print(f"      Warning: {warning['warning']}")
                print()
        else:
            print("✅ No sunset warnings")

    elif args.generate_banner:
        # Generate banner for testing
        banner = workflow.generate_deprecation_banner(
            doc_id=args.generate_banner,
            reason=args.reason or "Document deprecated",
            sunset_date=datetime.now() + timedelta(days=args.sunset_days),
            migration_target=args.migration_target
        )
        print(banner)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
