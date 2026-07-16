#!/usr/bin/env python3
"""
ingest.py — Cross-platform helper for ingesting a new source into the trading wiki.

Equivalent to the original tools/ingest.sh, but pure Python so it works
on Windows without bash. Creates two files:
  1. raw/{type}s/{source_id}.{md|pdf}  — immutable source stub
  2. wiki/sources/{source_id}.md       — wiki summary stub with frontmatter

Usage:
    python tools/ingest.py article "https://example.com/x" "Article Title"
    python tools/ingest.py pdf "/path/to/paper.pdf" "Paper Title"
    python tools/ingest.py video "https://youtube.com/watch?v=..." "Video Title"
    python tools/ingest.py tweet "https://twitter.com/u/status/123" "Tweet Thread"
"""
import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent


def slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def write_raw(raw_dir: Path, source_id: str, source_type: str, source_path: str, title: str, now: str) -> Path:
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_file = raw_dir / f"{source_id}.md"

    if source_type == "article":
        body = (
            f"<!-- Source URL: {source_path} -->\n"
            f"<!-- Downloaded: {now} -->\n\n"
            f"# {title}\n\n"
            f"[Paste article content here]\n"
        )
    elif source_type == "pdf":
        src = Path(source_path)
        if not src.is_file():
            print(f"Error: PDF file not found: {source_path}", file=sys.stderr)
            sys.exit(1)
        shutil.copy2(src, raw_dir / f"{source_id}.pdf")
        body = (
            f"# {title}\n\n"
            f"PDF stored at: raw/pdfs/{source_id}.pdf\n\n"
            f"[Paste extracted text here]\n"
        )
    elif source_type == "video":
        body = (
            f"<!-- Video URL: {source_path} -->\n"
            f"<!-- Downloaded: {now} -->\n\n"
            f"# {title}\n\n"
            f"[Paste transcript here]\n"
        )
    elif source_type == "tweet":
        body = (
            f"<!-- Tweet URL: {source_path} -->\n"
            f"<!-- Saved: {now} -->\n\n"
            f"# {title}\n\n"
            f"[Paste tweet thread here]\n"
        )
    else:
        body = (
            f"<!-- Source: {source_path} -->\n"
            f"<!-- Saved: {now} -->\n\n"
            f"# {title}\n"
        )

    raw_file.write_text(body, encoding="utf-8")
    return raw_file


def write_summary(source_id: str, source_type: str, source_path: str, title: str, today: str) -> Path:
    summary_dir = WIKI_ROOT / "wiki" / "sources"
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_file = summary_dir / f"{source_id}.md"
    summary_file.write_text(
        f"""---
title: "{title}"
type: source
created: {today}
updated: {today}
status: stub
tags: []
source_type: {source_type}
source_url: "{source_path}"
source_author: ""
source_date: {today}
source_file: "raw/{source_type}s/{source_id}.md"
confidence: medium
claims_count: 0
---

# {title}

**Source**: [{title}]({source_path})
**Type**: {source_type}
**Confidence**: Pending review

## Summary

[TODO: Summarize this source]

## Key Claims

[TODO: Extract claims]

## Pages Created or Updated

[TODO: List affected pages]
""",
        encoding="utf-8",
    )
    return summary_file


def main() -> int:
    p = argparse.ArgumentParser(description="Ingest a new source into the trading wiki")
    p.add_argument("source_type", help="article|pdf|video|tweet|screenshot|data|book|misc")
    p.add_argument("source_path", help="URL or filesystem path to the source")
    p.add_argument("title", help="Human-readable title")
    args = p.parse_args()

    now_dt = datetime.now()
    today = now_dt.strftime("%Y-%m-%d")
    now = now_dt.strftime("%Y-%m-%d %H:%M")

    source_id = f"{today}-{slugify(args.title)}"
    raw_dir = WIKI_ROOT / "raw" / f"{args.source_type}s"

    raw_file = write_raw(raw_dir, source_id, args.source_type, args.source_path, args.title, now)
    summary_file = write_summary(source_id, args.source_type, args.source_path, args.title, today)

    print()
    print("=== Source Ingested ===")
    print(f"Raw file:    {raw_file}")
    print(f"Summary:     {summary_file}")
    print(f"Source ID:   {source_id}")
    print()
    print("Next steps:")
    print("  1. Populate the raw file with source content")
    print(f"  2. Ask Claude to process: 'Ingest source {source_id}'")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
