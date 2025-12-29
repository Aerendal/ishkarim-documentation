#!/usr/bin/env python3
"""
Impact Propagation System - Living Documentation Framework (Phase 2)

Automatycznie wykrywa zmiany w dokumentach i propaguje impact do downstream documents.

Usage:
    python impact_propagation.py --check-all
    python impact_propagation.py --document engineering/requirements/prd.md
    python impact_propagation.py --notify --slack-webhook https://...
"""

import argparse
import sys
import os
import yaml
import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import hashlib

# Import document parser from same directory
try:
    from document_parser import DocumentParser, Document
except ImportError:
    print("Error: document_parser.py not found. Make sure it's in the same directory.")
    sys.exit(1)


class ImpactPropagation:
    """Impact propagation system for Living Documentation"""

    def __init__(self, docs_root: str = "."):
        self.docs_root = Path(docs_root)
        self.parser = DocumentParser()
        self.cache_file = self.docs_root / "automation" / "config" / "impact_cache.json"
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict:
        """Load impact cache (document checksums + last propagation dates)"""
        if self.cache_file.exists():
            with open(self.cache_file, 'r') as f:
                return json.load(f)
        return {"documents": {}, "last_run": None}

    def _save_cache(self):
        """Save impact cache"""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=2)

    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate MD5 checksum of file"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def detect_changes(self, since_hours: int = 24) -> List[Tuple[Document, str]]:
        """
        Detect documents that changed in last N hours

        Returns: List of (document, change_type) tuples
                 change_type: "new" | "modified" | "deleted"
        """
        changes = []
        cutoff_time = datetime.now() - timedelta(hours=since_hours)

        # Scan all markdown files
        for md_file in self.docs_root.rglob("*.md"):
            # Skip templates
            if "template" in str(md_file).lower():
                continue

            relative_path = str(md_file.relative_to(self.docs_root))

            # Calculate current checksum
            current_checksum = self._calculate_checksum(md_file)

            # Check if file is new or modified
            cached_info = self.cache["documents"].get(relative_path, {})
            cached_checksum = cached_info.get("checksum")

            if cached_checksum is None:
                # New file
                try:
                    doc = self.parser.parse(md_file)
                    if doc and doc.id:  # Only valid docs with ID
                        changes.append((doc, "new"))
                        # Update cache
                        self.cache["documents"][relative_path] = {
                            "checksum": current_checksum,
                            "last_modified": datetime.now().isoformat()
                        }
                except Exception as e:
                    print(f"Warning: Could not parse {md_file}: {e}")

            elif current_checksum != cached_checksum:
                # Modified file
                try:
                    doc = self.parser.parse(md_file)
                    if doc and doc.id:
                        changes.append((doc, "modified"))
                        # Update cache
                        self.cache["documents"][relative_path] = {
                            "checksum": current_checksum,
                            "last_modified": datetime.now().isoformat()
                        }
                except Exception as e:
                    print(f"Warning: Could not parse {md_file}: {e}")

        # TODO: Detect deleted files (in cache but not on disk)

        self._save_cache()
        return changes

    def get_downstream_documents(self, doc: Document) -> List[Document]:
        """
        Get all downstream documents that depend on this document

        Based on cross_references.impacts section in doc metadata
        """
        downstream = []

        if not hasattr(doc, 'cross_references') or not doc.cross_references:
            return downstream

        impacts = doc.cross_references.get('impacts', [])

        for impact in impacts:
            impact_id = impact.get('id')
            if impact_id:
                # Find document by ID
                target_doc = self.parser.find_document_by_id(impact_id)
                if target_doc:
                    downstream.append(target_doc)

        return downstream

    def calculate_impact_severity(self, doc: Document, change_type: str) -> str:
        """
        Calculate impact severity based on version change

        Returns: "low" | "medium" | "high" | "critical"
        """
        if change_type == "new":
            return "low"  # New doc doesn't impact existing

        # Check version change type
        version = getattr(doc, 'version', '1.0.0')
        version_parts = version.split('.')

        if len(version_parts) >= 1:
            major = int(version_parts[0])
            if major > 1:  # Major version bump
                return "critical"

        if len(version_parts) >= 2:
            minor = int(version_parts[1])
            if minor > 0:  # Minor version bump
                return "high"

        # Patch version bump or no version info
        return "medium"

    def propagate_impact(self, doc: Document, change_type: str, dry_run: bool = True) -> Dict:
        """
        Propagate impact to downstream documents

        Args:
            doc: Changed document
            change_type: "new" | "modified" | "deleted"
            dry_run: If True, don't modify files, just report what would be done

        Returns: Impact report
        """
        downstream_docs = self.get_downstream_documents(doc)
        severity = self.calculate_impact_severity(doc, change_type)

        report = {
            "source_document": {
                "id": doc.id,
                "version": getattr(doc, 'version', 'unknown'),
                "status": doc.status
            },
            "change_type": change_type,
            "severity": severity,
            "downstream_impacts": [],
            "notifications_sent": []
        }

        for downstream_doc in downstream_docs:
            impact_info = {
                "document_id": downstream_doc.id,
                "document_path": str(downstream_doc.file_path),
                "impact_type": "requires_review",
                "action_required": f"Review changes in {doc.id} v{getattr(doc, 'version', 'unknown')}"
            }

            if not dry_run:
                # TODO: Actually update downstream document metadata
                # Add to upstream_changes_pending in cross_reference_status
                impact_info["updated"] = True
            else:
                impact_info["updated"] = False

            report["downstream_impacts"].append(impact_info)

        return report

    def generate_notifications(self, impact_reports: List[Dict]) -> List[Dict]:
        """
        Generate notifications for impacted documents

        Returns: List of notifications to send
        """
        notifications = []

        for report in impact_reports:
            if report["severity"] in ["high", "critical"]:
                # High/critical severity → immediate notification
                for impact in report["downstream_impacts"]:
                    notification = {
                        "type": "immediate",
                        "channel": "slack",  # Slack for high severity
                        "severity": report["severity"],
                        "message": f"🚨 **{report['severity'].upper()} Impact Detected**\n\n"
                                   f"Source: {report['source_document']['id']} (v{report['source_document']['version']})\n"
                                   f"Impacted: {impact['document_id']}\n"
                                   f"Action: {impact['action_required']}"
                    }
                    notifications.append(notification)

            elif report["severity"] == "medium":
                # Medium severity → daily digest
                notification = {
                    "type": "digest",
                    "channel": "email",
                    "severity": "medium",
                    "impacts": report["downstream_impacts"]
                }
                notifications.append(notification)

        return notifications

    def run_check(self, since_hours: int = 24, dry_run: bool = True) -> Dict:
        """
        Run full impact propagation check

        Returns: Complete report
        """
        print(f"🔍 Checking for document changes in last {since_hours} hours...\n")

        changes = self.detect_changes(since_hours=since_hours)

        print(f"📊 Found {len(changes)} changed documents\n")

        impact_reports = []

        for doc, change_type in changes:
            print(f"📄 {doc.id} ({change_type})")
            report = self.propagate_impact(doc, change_type, dry_run=dry_run)
            impact_reports.append(report)

            if report["downstream_impacts"]:
                print(f"   ⚠️  Impacts {len(report['downstream_impacts'])} downstream documents")
                for impact in report["downstream_impacts"]:
                    print(f"      → {impact['document_id']}")
            else:
                print(f"   ✅ No downstream impacts")
            print()

        notifications = self.generate_notifications(impact_reports)

        full_report = {
            "run_date": datetime.now().isoformat(),
            "changes_detected": len(changes),
            "impact_reports": impact_reports,
            "notifications": notifications,
            "dry_run": dry_run
        }

        return full_report


def main():
    parser = argparse.ArgumentParser(
        description="Impact Propagation System - Living Documentation Framework"
    )
    parser.add_argument(
        "--check-all",
        action="store_true",
        help="Check all documents for changes in last 24h"
    )
    parser.add_argument(
        "--document",
        type=str,
        help="Check specific document for downstream impacts"
    )
    parser.add_argument(
        "--since-hours",
        type=int,
        default=24,
        help="Check changes in last N hours (default: 24)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Dry run mode - don't modify files (default: true)"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually apply changes (disable dry-run)"
    )
    parser.add_argument(
        "--format",
        choices=["terminal", "json", "markdown"],
        default="terminal",
        help="Output format"
    )

    args = parser.parse_args()

    # Determine dry run mode
    dry_run = not args.apply

    # Initialize impact propagation
    propagation = ImpactPropagation(docs_root=".")

    if args.check_all:
        # Run full check
        report = propagation.run_check(since_hours=args.since_hours, dry_run=dry_run)

        if args.format == "json":
            print(json.dumps(report, indent=2))
        elif args.format == "markdown":
            # TODO: Format as markdown
            print("# Impact Propagation Report\n")
            print(f"**Date:** {report['run_date']}\n")
            print(f"**Changes Detected:** {report['changes_detected']}\n")
            print(f"**Notifications:** {len(report['notifications'])}\n")
        else:
            # Terminal format (already printed by run_check)
            print(f"\n{'='*60}")
            print(f"✅ Impact propagation check complete")
            print(f"   Changes: {report['changes_detected']}")
            print(f"   Notifications: {len(report['notifications'])}")
            if dry_run:
                print(f"   Mode: DRY RUN (use --apply to actually update files)")
            print(f"{'='*60}")

    elif args.document:
        # Check specific document
        print(f"🔍 Analyzing impact for: {args.document}")
        # TODO: Implement single document check
        print("Not implemented yet. Use --check-all for now.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
