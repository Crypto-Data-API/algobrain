#!/usr/bin/env python3
"""
Wiki search tool — keyword search with BM25 scoring across wiki pages.

Usage:
    python tools/search.py "bitcoin etf"
    python tools/search.py --tag crypto
    python tools/search.py --type concept
    python tools/search.py --status stub
    python tools/search.py "risk management" --type strategy --limit 5
    python tools/search.py --json
"""
import argparse
import json as json_lib
import math
import re
import sys
from collections import Counter
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent / "wiki"


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


def load_documents() -> list[dict]:
    """Load all wiki markdown files."""
    docs = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(content)
        body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", content, flags=re.DOTALL)
        docs.append(
            {
                "path": str(md_file.relative_to(WIKI_ROOT.parent)),
                "frontmatter": fm,
                "body": body,
                "content": content,
            }
        )
    return docs


def tokenize(text: str) -> list[str]:
    """Simple whitespace + punctuation tokenizer, lowercase."""
    return re.findall(r"\b[a-z0-9]+\b", text.lower())


def bm25_search(
    docs: list[dict], query: str, k1: float = 1.5, b: float = 0.75
) -> list[tuple]:
    """BM25 scoring across documents."""
    query_terms = tokenize(query)
    n = len(docs)
    if n == 0:
        return []

    doc_tokens = []
    for doc in docs:
        tokens = tokenize(doc["body"] + " " + doc["frontmatter"].get("title", ""))
        doc_tokens.append(tokens)

    avg_dl = sum(len(t) for t in doc_tokens) / max(n, 1)

    # Document frequency
    df = Counter()
    for tokens in doc_tokens:
        for term in set(tokens):
            df[term] += 1

    # Score each document
    scores = []
    for i, doc in enumerate(docs):
        tokens = doc_tokens[i]
        tf = Counter(tokens)
        dl = len(tokens)
        score = 0.0
        for term in query_terms:
            if df[term] == 0:
                continue
            idf = math.log((n - df[term] + 0.5) / (df[term] + 0.5) + 1)
            term_tf = tf[term]
            tf_norm = (term_tf * (k1 + 1)) / (
                term_tf + k1 * (1 - b + b * dl / avg_dl)
            )
            score += idf * tf_norm

        # Boost for title match
        title = doc["frontmatter"].get("title", "").lower()
        if any(t in title for t in query_terms):
            score *= 1.5

        scores.append((score, doc))

    scores.sort(key=lambda x: x[0], reverse=True)
    return [(s, d) for s, d in scores if s > 0]


def filter_docs(
    docs: list[dict],
    tag: str | None = None,
    doc_type: str | None = None,
    status: str | None = None,
) -> list[dict]:
    """Filter documents by frontmatter fields."""
    filtered = docs
    if tag:
        filtered = [
            d
            for d in filtered
            if tag.lower() in d["frontmatter"].get("tags", "").lower()
        ]
    if doc_type:
        filtered = [
            d for d in filtered if d["frontmatter"].get("type", "") == doc_type
        ]
    if status:
        filtered = [
            d for d in filtered if d["frontmatter"].get("status", "") == status
        ]
    return filtered


def main():
    parser = argparse.ArgumentParser(description="Search the trading wiki")
    parser.add_argument("query", nargs="?", default="", help="Search query")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--type", help="Filter by page type")
    parser.add_argument("--status", help="Filter by status")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    docs = load_documents()
    docs = filter_docs(docs, tag=args.tag, doc_type=args.type, status=args.status)

    if args.query:
        results = bm25_search(docs, args.query)[: args.limit]
    else:
        results = [(0, d) for d in docs[: args.limit]]

    if args.json:
        output = [
            {
                "score": round(s, 4),
                "path": d["path"],
                "title": d["frontmatter"].get("title", ""),
                "status": d["frontmatter"].get("status", ""),
                "type": d["frontmatter"].get("type", ""),
            }
            for s, d in results
        ]
        print(json_lib.dumps(output, indent=2))
    else:
        if not results:
            print("No results found.")
            return
        for score, doc in results:
            title = doc["frontmatter"].get("title", "Untitled")
            status = doc["frontmatter"].get("status", "?")
            print(f"  [{score:.2f}] {doc['path']}")
            print(f"         {title} (status: {status})")
            print()


if __name__ == "__main__":
    main()
