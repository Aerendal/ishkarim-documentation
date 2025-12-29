#!/usr/bin/env python3
"""
Living Documentation Framework - Health Check

Performs automated health checks on Living Documentation documents.

7 Health Checks:
1. Freshness Check - last modified vs threshold
2. Dependency Validity - dependencies exist and are valid
3. Cross-Reference Consistency - references are valid
4. Owner Assignment - owner is assigned
5. Required Sections Completeness - required sections exist
6. Upstream Changes Pending - unhandled upstream changes
7. Satellite Completeness - satellites are complete

Usage:
    python health_check.py --format markdown > health-report.md
    python health_check.py --format terminal
    python health_check.py --format json > health-report.json
    python health_check.py --critical-only
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass, asdict

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from document_parser import DocumentParser, Document


@dataclass
class HealthCheckResult:
    """Result of a single health check"""
    check_name: str
    status: str  # "healthy", "warning", "critical"
    message: str
    details: Dict[str, Any]


@dataclass
class DocumentHealthReport:
    """Health report for a single document"""
    document_id: str
    document_title: str
    file_path: str
    overall_status: str  # "healthy", "warning", "critical"
    checks: List[HealthCheckResult]

    @property
    def has_critical(self) -> bool:
        return any(c.status == "critical" for c in self.checks)

    @property
    def has_warning(self) -> bool:
        return any(c.status == "warning" for c in self.checks)

    @property
    def healthy_count(self) -> int:
        return sum(1 for c in self.checks if c.status == "healthy")

    @property
    def warning_count(self) -> int:
        return sum(1 for c in self.checks if c.status == "warning")

    @property
    def critical_count(self) -> int:
        return sum(1 for c in self.checks if c.status == "critical")


class HealthChecker:
    """Performs health checks on Living Documentation documents"""

    # Freshness thresholds (days)
    FRESHNESS_THRESHOLDS = {
        'prd': 90,
        'tdd': 90,
        'adr': 365,
        'vision': 180,
        'business-case': 90,
        'default': 90
    }

    def __init__(self, base_path: Path):
        """
        Initialize health checker

        Args:
            base_path: Base directory for document resolution
        """
        self.base_path = base_path
        self.parser = DocumentParser(base_path)

    def check_document_health(self, doc: Document) -> DocumentHealthReport:
        """
        Perform all health checks on a document

        Args:
            doc: Document to check

        Returns:
            DocumentHealthReport with results of all checks
        """
        checks = [
            self.check_freshness(doc),
            self.check_dependency_validity(doc),
            self.check_cross_reference_consistency(doc),
            self.check_owner_assignment(doc),
            self.check_required_sections(doc),
            self.check_upstream_changes(doc),
            self.check_satellite_completeness(doc)
        ]

        # Determine overall status
        if any(c.status == "critical" for c in checks):
            overall_status = "critical"
        elif any(c.status == "warning" for c in checks):
            overall_status = "warning"
        else:
            overall_status = "healthy"

        return DocumentHealthReport(
            document_id=doc.id,
            document_title=doc.title,
            file_path=str(doc.file_path.relative_to(self.base_path)),
            overall_status=overall_status,
            checks=checks
        )

    def check_freshness(self, doc: Document) -> HealthCheckResult:
        """Check if document has been modified recently"""
        if not doc.lifecycle:
            return HealthCheckResult(
                check_name="Freshness Check",
                status="warning",
                message="No lifecycle metadata found",
                details={}
            )

        last_modified_str = doc.lifecycle.get('last_modified')
        if not last_modified_str:
            return HealthCheckResult(
                check_name="Freshness Check",
                status="warning",
                message="No last_modified date in lifecycle",
                details={}
            )

        try:
            last_modified = datetime.fromisoformat(last_modified_str)
            days_since_modified = (datetime.now() - last_modified).days

            threshold = self.FRESHNESS_THRESHOLDS.get(
                doc.type, self.FRESHNESS_THRESHOLDS['default']
            )

            if days_since_modified > threshold:
                status = "warning"
                message = f"Document not modified in {days_since_modified} days (threshold: {threshold})"
            else:
                status = "healthy"
                message = f"Document modified {days_since_modified} days ago"

            return HealthCheckResult(
                check_name="Freshness Check",
                status=status,
                message=message,
                details={
                    "last_modified": last_modified_str,
                    "days_since_modified": days_since_modified,
                    "threshold_days": threshold
                }
            )

        except (ValueError, TypeError) as e:
            return HealthCheckResult(
                check_name="Freshness Check",
                status="warning",
                message=f"Invalid last_modified date format: {e}",
                details={}
            )

    def check_dependency_validity(self, doc: Document) -> HealthCheckResult:
        """Check if all dependencies exist and are valid"""
        if not doc.dependencies:
            return HealthCheckResult(
                check_name="Dependency Validity",
                status="healthy",
                message="No dependencies",
                details={"dependencies": []}
            )

        invalid_deps = []

        for dep_id in doc.dependencies:
            dep_doc = self.parser.find_document_by_id(dep_id)

            if dep_doc is None:
                invalid_deps.append({
                    "id": dep_id,
                    "reason": "Document not found"
                })
            elif dep_doc.status in ['deprecated', 'sunset', 'archived']:
                invalid_deps.append({
                    "id": dep_id,
                    "reason": f"Dependency is {dep_doc.status}"
                })

        if invalid_deps:
            status = "critical" if len(invalid_deps) == len(doc.dependencies) else "warning"
            message = f"{len(invalid_deps)} invalid dependencies"
        else:
            status = "healthy"
            message = "All dependencies valid"

        return HealthCheckResult(
            check_name="Dependency Validity",
            status=status,
            message=message,
            details={
                "total_dependencies": len(doc.dependencies),
                "invalid_dependencies": invalid_deps
            }
        )

    def check_cross_reference_consistency(self, doc: Document) -> HealthCheckResult:
        """Check if cross-references are consistent"""
        if not doc.cross_reference_status:
            return HealthCheckResult(
                check_name="Cross-Reference Consistency",
                status="healthy",
                message="No cross-reference metadata",
                details={}
            )

        upstream_pending = doc.cross_reference_status.get('upstream_changes_pending', [])
        downstream_pending = doc.cross_reference_status.get('downstream_impacts_pending', [])

        unacknowledged_upstream = [
            u for u in upstream_pending
            if not u.get('acknowledged', False)
        ]

        if unacknowledged_upstream:
            status = "warning"
            message = f"{len(unacknowledged_upstream)} unacknowledged upstream changes"
        else:
            status = "healthy"
            message = "All cross-references consistent"

        return HealthCheckResult(
            check_name="Cross-Reference Consistency",
            status=status,
            message=message,
            details={
                "upstream_pending": len(upstream_pending),
                "downstream_pending": len(downstream_pending),
                "unacknowledged_upstream": len(unacknowledged_upstream)
            }
        )

    def check_owner_assignment(self, doc: Document) -> HealthCheckResult:
        """Check if document has an assigned owner"""
        if not doc.owner or doc.owner.strip() == "":
            return HealthCheckResult(
                check_name="Owner Assignment",
                status="critical",
                message="No owner assigned",
                details={}
            )

        return HealthCheckResult(
            check_name="Owner Assignment",
            status="healthy",
            message=f"Owner: {doc.owner}",
            details={"owner": doc.owner}
        )

    def check_required_sections(self, doc: Document) -> HealthCheckResult:
        """Check if required sections are complete"""
        if not doc.document_health:
            return HealthCheckResult(
                check_name="Required Sections Completeness",
                status="warning",
                message="No health metadata found",
                details={}
            )

        checks = doc.document_health.get('checks', [])
        completeness_check = next(
            (c for c in checks if c.get('name') == 'Required Sections Completeness'),
            None
        )

        if not completeness_check:
            return HealthCheckResult(
                check_name="Required Sections Completeness",
                status="healthy",
                message="No completeness check in metadata",
                details={}
            )

        missing_sections = completeness_check.get('missing_sections', [])
        completeness = completeness_check.get('completeness', '100%')

        if missing_sections:
            status = "warning"
            message = f"Missing {len(missing_sections)} sections ({completeness})"
        else:
            status = "healthy"
            message = f"All required sections present ({completeness})"

        return HealthCheckResult(
            check_name="Required Sections Completeness",
            status=status,
            message=message,
            details={
                "completeness": completeness,
                "missing_sections": missing_sections
            }
        )

    def check_upstream_changes(self, doc: Document) -> HealthCheckResult:
        """Check for pending upstream changes"""
        if not doc.cross_reference_status:
            return HealthCheckResult(
                check_name="Upstream Changes Pending",
                status="healthy",
                message="No cross-reference metadata",
                details={}
            )

        upstream_pending = doc.cross_reference_status.get('upstream_changes_pending', [])

        if not upstream_pending:
            return HealthCheckResult(
                check_name="Upstream Changes Pending",
                status="healthy",
                message="No pending upstream changes",
                details={}
            )

        high_severity = [u for u in upstream_pending if u.get('impact_severity') == 'high']

        if high_severity:
            status = "warning"
            message = f"{len(high_severity)} high severity upstream changes pending"
        else:
            status = "healthy"
            message = f"{len(upstream_pending)} upstream changes (acknowledged)"

        return HealthCheckResult(
            check_name="Upstream Changes Pending",
            status=status,
            message=message,
            details={
                "total_pending": len(upstream_pending),
                "high_severity": len(high_severity)
            }
        )

    def check_satellite_completeness(self, doc: Document) -> HealthCheckResult:
        """Check if satellite documents are complete"""
        if not doc.document_health:
            return HealthCheckResult(
                check_name="Satellite Completeness",
                status="healthy",
                message="No health metadata",
                details={}
            )

        checks = doc.document_health.get('checks', [])
        satellite_check = next(
            (c for c in checks if c.get('name') == 'Satellite Completeness'),
            None
        )

        if not satellite_check:
            return HealthCheckResult(
                check_name="Satellite Completeness",
                status="healthy",
                message="No satellite check in metadata",
                details={}
            )

        missing_satellites = satellite_check.get('missing_satellites', [])

        if missing_satellites:
            status = "warning"
            message = f"Missing {len(missing_satellites)} satellites"
        else:
            status = "healthy"
            message = "All satellites present"

        return HealthCheckResult(
            check_name="Satellite Completeness",
            status=status,
            message=message,
            details={"missing_satellites": missing_satellites}
        )


def format_markdown(reports: List[DocumentHealthReport]) -> str:
    """Format health reports as Markdown"""
    lines = []

    lines.append("# Living Documentation Health Report")
    lines.append(f"\n**Generated:** {datetime.now().isoformat()}\n")

    # Summary
    total = len(reports)
    healthy = sum(1 for r in reports if r.overall_status == "healthy")
    warning = sum(1 for r in reports if r.overall_status == "warning")
    critical = sum(1 for r in reports if r.overall_status == "critical")

    lines.append("## Summary\n")
    lines.append(f"- **Total Documents:** {total}")
    lines.append(f"- 🟢 **Healthy:** {healthy}")
    lines.append(f"- 🟡 **Warning:** {warning}")
    lines.append(f"- 🔴 **Critical:** {critical}\n")

    # Document reports
    lines.append("## Document Health\n")

    for report in sorted(reports, key=lambda r: (r.overall_status != "critical", r.overall_status != "warning", r.document_id)):
        status_icon = {"healthy": "🟢", "warning": "🟡", "critical": "🔴"}[report.overall_status]

        lines.append(f"### {status_icon} {report.document_id} - {report.document_title}\n")
        lines.append(f"**File:** `{report.file_path}`")
        lines.append(f"**Status:** {report.overall_status.upper()}")
        lines.append(f"**Checks:** {report.healthy_count}/7 healthy, {report.warning_count} warnings, {report.critical_count} critical\n")

        if report.warning_count > 0 or report.critical_count > 0:
            lines.append("**Issues:**\n")
            for check in report.checks:
                if check.status != "healthy":
                    icon = "🟡" if check.status == "warning" else "🔴"
                    lines.append(f"- {icon} **{check.check_name}:** {check.message}")

        lines.append("")

    return "\n".join(lines)


def format_terminal(reports: List[DocumentHealthReport]) -> str:
    """Format health reports for terminal output"""
    try:
        from rich.console import Console
        from rich.table import Table
        from rich import box

        console = Console()

        # Summary table
        summary_table = Table(title="Living Documentation Health Summary", box=box.ROUNDED)
        summary_table.add_column("Status", style="bold")
        summary_table.add_column("Count", justify="right")

        total = len(reports)
        healthy = sum(1 for r in reports if r.overall_status == "healthy")
        warning = sum(1 for r in reports if r.overall_status == "warning")
        critical = sum(1 for r in reports if r.overall_status == "critical")

        summary_table.add_row("🟢 Healthy", str(healthy))
        summary_table.add_row("🟡 Warning", str(warning))
        summary_table.add_row("🔴 Critical", str(critical))
        summary_table.add_row("[bold]Total[/bold]", f"[bold]{total}[/bold]")

        console.print(summary_table)
        console.print()

        # Document details table
        details_table = Table(title="Document Health Details", box=box.SIMPLE)
        details_table.add_column("Status", width=8)
        details_table.add_column("Document ID", style="cyan")
        details_table.add_column("Checks", justify="center")
        details_table.add_column("Issues")

        for report in sorted(reports, key=lambda r: (r.overall_status != "critical", r.overall_status != "warning")):
            status_icon = {"healthy": "🟢", "warning": "🟡", "critical": "🔴"}[report.overall_status]
            checks_str = f"{report.healthy_count}/7"

            issues = []
            for check in report.checks:
                if check.status != "healthy":
                    issues.append(f"{check.check_name}")

            details_table.add_row(
                status_icon,
                report.document_id,
                checks_str,
                ", ".join(issues) if issues else "-"
            )

        console.print(details_table)

        return ""  # Rich prints directly

    except ImportError:
        # Fallback to simple text format if rich is not available
        return format_markdown(reports)


def format_json(reports: List[DocumentHealthReport]) -> str:
    """Format health reports as JSON"""
    data = {
        "generated": datetime.now().isoformat(),
        "summary": {
            "total": len(reports),
            "healthy": sum(1 for r in reports if r.overall_status == "healthy"),
            "warning": sum(1 for r in reports if r.overall_status == "warning"),
            "critical": sum(1 for r in reports if r.overall_status == "critical")
        },
        "documents": [asdict(report) for report in reports]
    }

    return json.dumps(data, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Living Documentation Framework - Health Check"
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "terminal", "json"],
        default="terminal",
        help="Output format (default: terminal)"
    )
    parser.add_argument(
        "--critical-only",
        action="store_true",
        help="Show only documents with critical issues"
    )
    parser.add_argument(
        "--base-path",
        type=Path,
        default=Path.cwd().parent.parent,  # Assume running from automation/scripts/
        help="Base path for document resolution"
    )

    args = parser.parse_args()

    # Initialize checker
    checker = HealthChecker(args.base_path)

    # Parse all documents
    doc_parser = DocumentParser(args.base_path)
    documents = doc_parser.parse_directory(args.base_path, skip_templates=True)

    # Filter to Living Documentation documents only
    living_docs = [doc for doc in documents if doc.has_living_doc_metadata]

    if not living_docs:
        print("No Living Documentation documents found.", file=sys.stderr)
        sys.exit(1)

    # Perform health checks
    reports = [checker.check_document_health(doc) for doc in living_docs]

    # Filter critical only if requested
    if args.critical_only:
        reports = [r for r in reports if r.has_critical]

    # Output results
    if args.format == "markdown":
        print(format_markdown(reports))
    elif args.format == "json":
        print(format_json(reports))
    else:  # terminal
        format_terminal(reports)

    # Exit code: 0 if all healthy, 1 if any warnings/critical
    exit_code = 0 if all(r.overall_status == "healthy" for r in reports) else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
