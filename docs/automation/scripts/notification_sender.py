#!/usr/bin/env python3
"""
Notification Sender - Living Documentation Framework (Phase 2)

Wysyła notyfikacje o zmianach w dokumentach przez różne kanały:
- Email (daily digest)
- Slack (instant for high severity)
- GitHub Issues (auto-created)

Usage:
    python notification_sender.py --channel slack --webhook $SLACK_WEBHOOK
    python notification_sender.py --channel email --to team@example.com
    python notification_sender.py --test
"""

import argparse
import sys
import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path


class NotificationSender:
    """Send notifications via multiple channels"""

    def __init__(self, config_file: Optional[str] = None):
        self.config = self._load_config(config_file)

    def _load_config(self, config_file: Optional[str]) -> Dict:
        """Load notification configuration"""
        if config_file and Path(config_file).exists():
            with open(config_file, 'r') as f:
                return json.load(f)

        # Default config
        return {
            "slack": {
                "webhook_url": os.getenv("SLACK_WEBHOOK_URL"),
                "channel": "#documentation",
                "username": "Living Docs Bot"
            },
            "email": {
                "smtp_server": os.getenv("SMTP_SERVER", "smtp.gmail.com"),
                "smtp_port": int(os.getenv("SMTP_PORT", "587")),
                "from_email": os.getenv("FROM_EMAIL"),
                "from_password": os.getenv("FROM_PASSWORD")
            },
            "github": {
                "token": os.getenv("GITHUB_TOKEN"),
                "repo": os.getenv("GITHUB_REPO")
            }
        }

    def send_slack(self, message: str, severity: str = "info") -> bool:
        """
        Send Slack notification

        Args:
            message: Message text (supports markdown)
            severity: "info" | "warning" | "critical"

        Returns: True if sent successfully
        """
        webhook_url = self.config["slack"].get("webhook_url")
        if not webhook_url:
            print("Error: SLACK_WEBHOOK_URL not configured")
            return False

        # Choose emoji based on severity
        emoji = {
            "info": ":information_source:",
            "warning": ":warning:",
            "critical": ":rotating_light:"
        }.get(severity, ":bell:")

        payload = {
            "channel": self.config["slack"].get("channel", "#documentation"),
            "username": self.config["slack"].get("username", "Living Docs Bot"),
            "icon_emoji": emoji,
            "text": message
        }

        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ Slack notification sent ({severity})")
                return True
            else:
                print(f"❌ Slack notification failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Slack notification error: {e}")
            return False

    def send_email(self, to: str, subject: str, body: str, html: bool = False) -> bool:
        """
        Send email notification

        Args:
            to: Recipient email
            subject: Email subject
            body: Email body (plain text or HTML)
            html: If True, body is HTML

        Returns: True if sent successfully
        """
        # TODO: Implement email sending via SMTP
        print(f"📧 Email notification (not implemented yet)")
        print(f"   To: {to}")
        print(f"   Subject: {subject}")
        return False

    def create_github_issue(self, title: str, body: str, labels: List[str] = None) -> bool:
        """
        Create GitHub issue

        Args:
            title: Issue title
            body: Issue body (markdown)
            labels: List of labels

        Returns: True if created successfully
        """
        token = self.config["github"].get("token")
        repo = self.config["github"].get("repo")

        if not token or not repo:
            print("Error: GITHUB_TOKEN or GITHUB_REPO not configured")
            return False

        url = f"https://api.github.com/repos/{repo}/issues"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        payload = {
            "title": title,
            "body": body,
            "labels": labels or ["documentation", "automated"]
        }

        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.status_code == 201:
                issue_url = response.json().get("html_url")
                print(f"✅ GitHub issue created: {issue_url}")
                return True
            else:
                print(f"❌ GitHub issue creation failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ GitHub issue error: {e}")
            return False

    def send_impact_notification(self, impact_report: Dict, channel: str = "slack") -> bool:
        """
        Send notification about document impact

        Args:
            impact_report: Impact report from impact_propagation.py
            channel: "slack" | "email" | "github"

        Returns: True if sent
        """
        source_doc = impact_report["source_document"]
        severity = impact_report["severity"]
        downstream = impact_report["downstream_impacts"]

        # Format message
        message = f"""**Document Impact Detected**

**Source:** {source_doc['id']} (v{source_doc['version']})
**Severity:** {severity.upper()}
**Impacted Documents:** {len(downstream)}

**Action Required:**
"""

        for impact in downstream[:5]:  # Show first 5
            message += f"\n- {impact['document_id']}: {impact['action_required']}"

        if len(downstream) > 5:
            message += f"\n... and {len(downstream) - 5} more"

        # Send via chosen channel
        if channel == "slack":
            return self.send_slack(message, severity=severity)
        elif channel == "email":
            # TODO: Get recipient from config
            return self.send_email(
                to="team@example.com",
                subject=f"[Living Docs] {severity.upper()} Impact: {source_doc['id']}",
                body=message
            )
        elif channel == "github":
            return self.create_github_issue(
                title=f"Document Impact: {source_doc['id']} → {len(downstream)} downstream docs",
                body=message,
                labels=["documentation", severity]
            )
        else:
            print(f"Unknown channel: {channel}")
            return False

    def send_health_digest(self, health_report: Dict, channel: str = "email") -> bool:
        """
        Send daily health digest

        Args:
            health_report: Report from health_check.py
            channel: "email" | "slack"

        Returns: True if sent
        """
        # TODO: Format health report
        message = "Daily Health Digest (not implemented yet)"
        return self.send_slack(message, severity="info")


def main():
    parser = argparse.ArgumentParser(
        description="Notification Sender - Living Documentation Framework"
    )
    parser.add_argument(
        "--channel",
        choices=["slack", "email", "github"],
        default="slack",
        help="Notification channel"
    )
    parser.add_argument(
        "--webhook",
        type=str,
        help="Slack webhook URL (overrides env var)"
    )
    parser.add_argument(
        "--message",
        type=str,
        help="Message to send (for testing)"
    )
    parser.add_argument(
        "--severity",
        choices=["info", "warning", "critical"],
        default="info",
        help="Notification severity"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Send test notification"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to config JSON file"
    )

    args = parser.parse_args()

    # Override webhook if provided
    if args.webhook:
        os.environ["SLACK_WEBHOOK_URL"] = args.webhook

    sender = NotificationSender(config_file=args.config)

    if args.test:
        message = args.message or "🧪 Test notification from Living Documentation Framework"
        print(f"Sending test notification via {args.channel}...\n")

        if args.channel == "slack":
            success = sender.send_slack(message, severity=args.severity)
        elif args.channel == "email":
            success = sender.send_email(
                to="test@example.com",
                subject="Test Notification",
                body=message
            )
        elif args.channel == "github":
            success = sender.create_github_issue(
                title="Test Issue from Living Docs",
                body=message
            )

        if success:
            print("\n✅ Test notification sent successfully!")
        else:
            print("\n❌ Test notification failed")
            sys.exit(1)

    elif args.message:
        # Send custom message
        if args.channel == "slack":
            sender.send_slack(args.message, severity=args.severity)
        elif args.channel == "email":
            print("Email sending requires --to parameter")
        elif args.channel == "github":
            sender.create_github_issue(
                title="Custom Notification",
                body=args.message
            )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
