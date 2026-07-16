#!/usr/bin/env python3
"""
MCP Server for Trading Wiki — exposes wiki operations as Claude-accessible tools.

Provides tools:
  - wiki_search: Search wiki pages by query, tag, type, status
  - wiki_ingest: Start ingestion of a new source
  - wiki_lint: Run health checks on the wiki
  - wiki_read: Read a specific wiki page by path
  - wiki_stats: Get wiki statistics

Run:
    .venv/bin/python tools/mcp_server.py

Register in Claude Code settings or claude_desktop_config.json (the command
must point at the project venv's interpreter — system python3 does not have
the `mcp` package installed):
    {
      "mcpServers": {
        "trading-wiki": {
          "command": "/Users/samd/websites/trader-wiki/.venv/bin/python",
          "args": ["/Users/samd/websites/trader-wiki/tools/mcp_server.py"]
        }
      }
    }
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print(
        "MCP SDK not installed. Run: pip install mcp",
        file=sys.stderr,
    )
    sys.exit(1)

server = FastMCP("trading-wiki")


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip().strip('"').strip("'")
    return fm


def load_wiki_pages() -> list[dict]:
    """Load all wiki markdown files."""
    wiki_dir = WIKI_ROOT / "wiki"
    pages = []
    for md_file in wiki_dir.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(content)
        pages.append(
            {
                "path": str(md_file.relative_to(WIKI_ROOT)),
                "frontmatter": fm,
                "content": content,
            }
        )
    return pages


@server.tool()
async def wiki_search(
    query: str = "",
    tag: str = "",
    type: str = "",
    status: str = "",
    limit: int = 10,
) -> str:
    """Search wiki pages by keyword, tag, type, or status. Returns matching pages ranked by relevance."""
    cmd = [sys.executable, str(WIKI_ROOT / "tools" / "search.py"), "--json"]
    if query:
        cmd.append(query)
    if tag:
        cmd.extend(["--tag", tag])
    if type:
        cmd.extend(["--type", type])
    if status:
        cmd.extend(["--status", status])
    cmd.extend(["--limit", str(limit)])

    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(WIKI_ROOT),
        stdin=subprocess.DEVNULL,
    )
    return result.stdout or result.stderr


@server.tool()
async def wiki_ingest(source_type: str, source_path: str, title: str) -> str:
    """Start ingesting a new source. Creates raw stub and source summary page. source_type: article|pdf|video|tweet|screenshot|data|book|misc"""
    cmd = [
        sys.executable,
        str(WIKI_ROOT / "tools" / "ingest.py"),
        source_type,
        source_path,
        title,
    ]
    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(WIKI_ROOT),
        stdin=subprocess.DEVNULL,
    )
    return result.stdout or result.stderr


@server.tool()
async def wiki_lint(check: str = "") -> str:
    """Run wiki health checks. Optionally specify a check: frontmatter, links, orphans, stale, empty, tags."""
    cmd = [sys.executable, str(WIKI_ROOT / "tools" / "lint.py"), "--json"]
    if check:
        cmd.extend(["--check", check])

    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(WIKI_ROOT),
        stdin=subprocess.DEVNULL,
    )
    return result.stdout or result.stderr


@server.tool()
async def wiki_read(page_path: str) -> str:
    """Read a wiki page by its path relative to repo root. Example: 'wiki/markets/crypto/_index.md'"""
    full_path = WIKI_ROOT / page_path
    if full_path.exists():
        return full_path.read_text(encoding="utf-8")
    return f"Page not found: {page_path}"


@server.tool()
async def wiki_stats() -> str:
    """Get wiki statistics: page counts by type, status distribution, source count, category breakdown."""
    pages = load_wiki_pages()

    by_type: dict[str, int] = Counter()
    by_status: dict[str, int] = Counter()
    by_category: dict[str, int] = defaultdict(int)

    for page in pages:
        fm = page["frontmatter"]
        by_type[fm.get("type", "unknown")] += 1
        by_status[fm.get("status", "unknown")] += 1

        # Extract top-level category from path
        parts = page["path"].split("/")
        if len(parts) >= 2:
            by_category[parts[1]] += 1

    stats = {
        "total_pages": len(pages),
        "by_type": dict(by_type),
        "by_status": dict(by_status),
        "by_category": dict(by_category),
    }
    return json.dumps(stats, indent=2)


if __name__ == "__main__":
    server.run()
