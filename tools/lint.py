#!/usr/bin/env python3
"""
Wiki lint tool — checks wiki health and reports issues.

Usage:
    python tools/lint.py              # Full lint
    python tools/lint.py --check frontmatter
    python tools/lint.py --check links
    python tools/lint.py --check orphans
    python tools/lint.py --check stale
    python tools/lint.py --check empty
    python tools/lint.py --json       # JSON output
"""
import argparse
import json as json_lib
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"
REQUIRED_FIELDS = ["title", "type", "created", "updated", "status", "tags"]
VALID_TYPES = {
    "concept", "strategy", "entity", "market", "comparison",
    "news", "source", "index", "overview",
}
VALID_STATUSES = {"stub", "draft", "review", "good", "excellent"}
APPROVED_TAGS = {
    # Markets
    "crypto", "stocks", "forex", "commodities", "options", "futures", "bonds",
    "defi", "nft",
    # Strategy types
    "technical-analysis", "fundamental-analysis", "quantitative", "algorithmic",
    "day-trading", "swing-trading", "position-trading", "scalping", "arbitrage",
    "mean-reversion", "trend-following", "momentum", "breakout", "pairs-trading",
    # Concepts
    "risk-management", "portfolio-theory", "market-microstructure", "order-types",
    "indicators", "behavioral-finance", "valuation", "leverage", "margin",
    "derivatives", "volatility", "correlation", "liquidity", "slippage",
    # Asset-specific
    "bitcoin", "ethereum", "altcoins", "sp500", "nasdaq", "gold", "oil", "treasuries",
    # Meta
    "history", "news", "education", "book", "person", "company", "exchange",
    "regulation", "ai-trading", "machine-learning", "backtesting", "data-provider",
    "index", "log", "meta", "overview", "sources", "raw", "comparisons",
    "traders", "hedge-funds", "exchanges", "regulators", "protocols",
    "trading-bots", "infrastructure", "courses", "resources",
    "crashes", "bull-markets", "bear-markets", "notable-trades", "market-evolution",
    "strategies", "concepts", "entities", "markets",
}


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"').strip("'")
            fm[key.strip()] = value
    return fm


def get_body(content: str) -> str:
    """Get content after frontmatter."""
    return re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)


def load_pages() -> list[dict]:
    """Load all wiki pages."""
    pages = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(content)
        body = get_body(content)
        rel_path = str(md_file.relative_to(WIKI_ROOT.parent))
        stem = md_file.stem
        pages.append({
            "path": rel_path,
            "stem": stem,
            "frontmatter": fm,
            "body": body,
            "content": content,
        })
    return pages


def extract_wikilinks(text: str) -> list[str]:
    """Extract all [[wikilink]] targets from text."""
    return re.findall(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]", text)


def check_frontmatter(pages: list[dict]) -> list[dict]:
    """Check that all pages have required frontmatter fields."""
    issues = []
    for page in pages:
        fm = page["frontmatter"]
        missing = [f for f in REQUIRED_FIELDS if f not in fm]
        if missing:
            issues.append({
                "check": "frontmatter",
                "severity": "error",
                "path": page["path"],
                "message": f"Missing required fields: {', '.join(missing)}",
            })
        if "type" in fm and fm["type"] not in VALID_TYPES:
            issues.append({
                "check": "frontmatter",
                "severity": "warning",
                "path": page["path"],
                "message": f"Invalid type: {fm['type']}",
            })
        if "status" in fm and fm["status"] not in VALID_STATUSES:
            issues.append({
                "check": "frontmatter",
                "severity": "warning",
                "path": page["path"],
                "message": f"Invalid status: {fm['status']}",
            })
    return issues


def check_wikilinks(pages: list[dict]) -> list[dict]:
    """Check for broken wikilinks (pages with >5 broken links)."""
    issues = []
    all_stems = {p["stem"] for p in pages}

    for page in pages:
        links = extract_wikilinks(page["content"])
        broken = []
        for link in links:
            # Strip any path components, just use the final segment
            target = link.split("/")[-1].split("#")[0].strip()
            if target and target not in all_stems:
                broken.append(target)
        if len(broken) > 5:
            issues.append({
                "check": "links",
                "severity": "warning",
                "path": page["path"],
                "message": f"{len(broken)} broken wikilinks: {', '.join(broken[:5])}...",
            })
    return issues


def check_orphans(pages: list[dict]) -> list[dict]:
    """Find pages with no inbound links."""
    issues = []
    inbound: dict[str, int] = defaultdict(int)

    for page in pages:
        links = extract_wikilinks(page["content"])
        for link in links:
            target = link.split("/")[-1].split("#")[0].strip()
            inbound[target] += 1

    for page in pages:
        fm = page["frontmatter"]
        if fm.get("type") in ("index", "overview"):
            continue  # Index/overview pages don't need inbound links
        if page["stem"] in ("index", "log", "overview", "_source_index"):
            continue
        if inbound.get(page["stem"], 0) == 0:
            issues.append({
                "check": "orphans",
                "severity": "info",
                "path": page["path"],
                "message": "No inbound links (orphan page)",
            })
    return issues


def check_stale(pages: list[dict]) -> list[dict]:
    """Find pages not updated in >90 days with status below good."""
    issues = []
    cutoff = datetime.now() - timedelta(days=90)

    for page in pages:
        fm = page["frontmatter"]
        updated = fm.get("updated", "")
        status = fm.get("status", "")
        if status in ("good", "excellent"):
            continue
        try:
            updated_date = datetime.strptime(updated, "%Y-%m-%d")
            if updated_date < cutoff:
                issues.append({
                    "check": "stale",
                    "severity": "info",
                    "path": page["path"],
                    "message": f"Last updated {updated}, status: {status}",
                })
        except ValueError:
            pass
    return issues


def check_empty(pages: list[dict]) -> list[dict]:
    """Find pages with no content beyond frontmatter."""
    issues = []
    for page in pages:
        body = page["body"].strip()
        # Ignore dataview blocks and headings-only
        clean = re.sub(r"```dataview.*?```", "", body, flags=re.DOTALL)
        clean = re.sub(r"^#+.*$", "", clean, flags=re.MULTILINE)
        clean = re.sub(r"^[-*].*$", "", clean, flags=re.MULTILINE)
        clean = clean.strip()
        if len(clean) < 20 and page["frontmatter"].get("type") not in ("index",):
            issues.append({
                "check": "empty",
                "severity": "info",
                "path": page["path"],
                "message": "Page has very little content beyond structure",
            })
    return issues


def check_tags(pages: list[dict]) -> list[dict]:
    """Flag non-approved tags."""
    issues = []
    for page in pages:
        tags_str = page["frontmatter"].get("tags", "")
        # Parse tags from the string representation
        tags = re.findall(r"[a-z0-9-]+", tags_str.lower())
        bad_tags = [t for t in tags if t not in APPROVED_TAGS]
        if bad_tags:
            issues.append({
                "check": "tags",
                "severity": "info",
                "path": page["path"],
                "message": f"Non-approved tags: {', '.join(bad_tags)}",
            })
    return issues


ALL_CHECKS = {
    "frontmatter": check_frontmatter,
    "links": check_wikilinks,
    "orphans": check_orphans,
    "stale": check_stale,
    "empty": check_empty,
    "tags": check_tags,
}


def main():
    parser = argparse.ArgumentParser(description="Lint the trading wiki")
    parser.add_argument(
        "--check", choices=list(ALL_CHECKS.keys()), help="Run a specific check only"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    pages = load_pages()

    if args.check:
        checks = {args.check: ALL_CHECKS[args.check]}
    else:
        checks = ALL_CHECKS

    all_issues = []
    for name, check_fn in checks.items():
        all_issues.extend(check_fn(pages))

    if args.json:
        print(json_lib.dumps(all_issues, indent=2))
    else:
        if not all_issues:
            print(f"All clear! {len(pages)} pages checked, no issues found.")
            return

        # Group by severity
        by_severity: dict[str, list] = defaultdict(list)
        for issue in all_issues:
            by_severity[issue["severity"]].append(issue)

        print(f"Checked {len(pages)} pages, found {len(all_issues)} issues:\n")

        for severity in ("error", "warning", "info"):
            items = by_severity.get(severity, [])
            if not items:
                continue
            label = severity.upper()
            print(f"--- {label} ({len(items)}) ---")
            for issue in items:
                print(f"  [{issue['check']}] {issue['path']}")
                print(f"    {issue['message']}")
            print()

    sys.exit(1 if any(i["severity"] == "error" for i in all_issues) else 0)


if __name__ == "__main__":
    main()
