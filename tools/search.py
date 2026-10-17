#!/usr/bin/env python3
"""
Wiki search tool: tiered BM25 search across wiki pages.

Mirrors the hosted CryptoDataAPI ``/api/v1/algobrain/search`` behaviour:

* Results are ranked by tier, and each result's ``match`` names its tier:
  ``exact_title`` (the query names the page: its title, an acronym in its
  title such as "(ADX)", or an alias) > ``title_phrase`` (the whole query as a
  phrase in the title or aliases) > ``title_terms`` (every term there) >
  ``all_terms`` (every term anywhere) > ``any_term``. Within a tier the
  generated per-coin pages (wiki/markets/crypto/*, type entity) rank below
  everything else, and the BM25 ``score`` orders the rest.
* A bare call (no query, no filter), or a query with no letters or digits,
  returns the newest pages by ``updated`` (score null). A filter-only call
  returns the matching pages in title order.
* Strategy filters (each an any-of match, comma-separated): backtest_status,
  horizon (frontmatter ``timeframe``), strategy_type, complexity,
  crowding_risk, market (frontmatter ``markets``), runnable (all|partial|none).

The index is built once per process and rebuilt only when a wiki file changes
(checked at most every few seconds), so callers such as the MCP server can
import this module and call ``search()`` / ``read_page()`` / ``stats()``.

Usage:
    python tools/search.py "bitcoin etf"
    python tools/search.py --tag crypto
    python tools/search.py --type concept
    python tools/search.py --status stub
    python tools/search.py "risk management" --type strategy --limit 5
    python tools/search.py --backtest-status live --horizon swing
    python tools/search.py --runnable partial --json
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json as json_lib
import math
import os
import re
import sys
import threading
import time
from collections import Counter
from pathlib import Path

try:  # PyYAML is optional: a small built-in parser covers the wiki's frontmatter.
    import yaml

    _YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
except ImportError:  # pragma: no cover - exercised only without PyYAML
    yaml = None
    _YAML_LOADER = None

WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"
REPO_ROOT = WIKI_ROOT.parent

# How often (seconds) the cached index re-checks the wiki for changed files.
INDEX_CHECK_INTERVAL = 3.0
SNIPPET_CHARS = 200
SNIPPET_LEAD = 60
MAX_LIMIT = 500

TIERS = ("exact_title", "title_phrase", "title_terms", "all_terms", "any_term")
RUNNABLE_VALUES = ("all", "partial", "none")
STRATEGY_FILTERS = (
    "backtest_status",
    "horizon",
    "strategy_type",
    "complexity",
    "crowding_risk",
    "market",
    "runnable",
)

BM25_K1 = 1.5
BM25_B = 0.75
TITLE_BOOST = 1.5

_TOKEN_RE = re.compile(r"[a-z0-9]+")
_PAREN_RE = re.compile(r"\(([^()]*)\)")
_ACRONYM_RE = re.compile(r"(?=[^a-z]*[A-Z])[A-Z0-9][A-Z0-9&/.\-]*")


# --------------------------------------------------------------------------- #
# Frontmatter parsing
# --------------------------------------------------------------------------- #
def split_frontmatter(content: str) -> tuple[str | None, str]:
    """Return (frontmatter_text, body). frontmatter_text is None if absent."""
    if content.startswith("﻿"):
        content = content[1:]
    content = content.replace("\r\n", "\n")
    if not content.startswith("---"):
        return None, content
    lines = content.split("\n")
    if lines[0].strip() != "---":
        return None, content
    for i in range(1, len(lines)):
        if lines[i].rstrip() in ("---", "..."):
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1 :])
    return None, content


def _scalar(value: str):
    """Interpret a YAML-ish scalar for the fallback parser."""
    v = value.strip()
    if not v:
        return None
    if (v[0] == v[-1]) and v[0] in "\"'" and len(v) >= 2:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(p) for p in _split_flow(inner)]
    low = v.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "~"):
        return None
    if " #" in v:
        v = v.split(" #", 1)[0].rstrip()
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


def _split_flow(text: str) -> list[str]:
    """Split a flow-sequence body on commas outside quotes/brackets."""
    parts, buf, depth, quote = [], [], 0, ""
    for ch in text:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = ""
            continue
        if ch in "\"'":
            quote = ch
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
            continue
        buf.append(ch)
    if buf:
        parts.append("".join(buf))
    return [p for p in (s.strip() for s in parts) if p]


def _fallback_parse(text: str) -> dict:
    """Tolerant subset parser: top-level scalars, flow lists, block lists of
    scalars and block lists of flat mappings (enough for tags/aliases/gates).
    Block scalars (``|``/``>``) are kept as joined text."""
    fm: dict = {}
    lines = text.split("\n")
    i = 0
    key_re = re.compile(r"^([A-Za-z0-9_][\w\-]*)\s*:(.*)$")
    while i < len(lines):
        line = lines[i]
        m = key_re.match(line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        i += 1
        if rest in ("|", ">", "|-", ">-", "|+", ">+"):
            block = []
            while i < len(lines) and (not lines[i].strip() or lines[i][:1] in " \t"):
                block.append(lines[i].strip())
                i += 1
            fm[key] = "\n".join(block).strip()
            continue
        if rest:
            fm[key] = _scalar(rest)
            continue
        # Block sequence (or nested mapping, which we skip).
        items: list = []
        current: dict | None = None
        while i < len(lines) and (not lines[i].strip() or lines[i][:1] in " \t-"):
            raw = lines[i]
            stripped = raw.strip()
            i += 1
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("- ") or stripped == "-":
                entry = stripped[1:].strip()
                km = key_re.match(entry)
                if km:
                    current = {km.group(1): _scalar(km.group(2))}
                    items.append(current)
                else:
                    current = None
                    items.append(_scalar(entry))
            elif current is not None:
                km = key_re.match(stripped)
                if km:
                    current[km.group(1)] = _scalar(km.group(2))
        fm[key] = items if items else None
    return fm


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content (never raises)."""
    text, _ = split_frontmatter(content)
    return _parse_frontmatter_text(text)


def _parse_frontmatter_text(text: str | None) -> dict:
    if not text:
        return {}
    if yaml is not None:
        try:
            data = yaml.load(text, Loader=_YAML_LOADER)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
    try:
        return _fallback_parse(text)
    except Exception:
        return {}


def jsonable(value):
    """Recursively convert YAML values (dates, sets, ...) into JSON-safe ones."""
    if isinstance(value, (_dt.date, _dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(v) for v in value]
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens."""
    return _TOKEN_RE.findall(text.lower())


def norm(text: str) -> str:
    return " ".join(tokenize(text))


def _str_or_none(value) -> str | None:
    if value is None or value == "":
        return None
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value) if value else None
    return str(jsonable(value))


def _str_list(value) -> list[str]:
    if value is None or value == "":
        return []
    if isinstance(value, (list, tuple, set)):
        return [str(jsonable(v)) for v in value if v is not None and v != ""]
    if isinstance(value, str):
        s = value.strip()
        if s.startswith("[") and s.endswith("]"):
            s = s[1:-1]
        return [p.strip().strip("\"'") for p in s.split(",") if p.strip()]
    return [str(jsonable(value))]


def _split_labels(value) -> list[str]:
    """'swing|position' / ['swing', 'position'] -> ['swing', 'position']."""
    out: list[str] = []
    for item in _str_list(value):
        for part in re.split(r"[|,]", item):
            part = part.strip()
            if part and part not in out:
                out.append(part)
    return out


def _to_float(value) -> float | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(str(value).strip())
    except ValueError:
        return None


def _gate_runnable(value) -> str:
    """Normalise a gate's runnable flag to 'true' | 'partial' | 'false'."""
    if value is True:
        return "true"
    if isinstance(value, str):
        v = value.strip().lower()
        if v in ("true", "yes"):
            return "true"
        if v == "partial":
            return "partial"
    return "false"


def _values(value) -> list[str]:
    """Filter argument (str with commas, or list) -> lowercase value list."""
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        raw = [str(v) for v in value]
    else:
        raw = str(value).split(",")
    return [v.strip().lower() for v in raw if v.strip()]


# --------------------------------------------------------------------------- #
# Documents and index
# --------------------------------------------------------------------------- #
def _build_strategy(fm: dict, gates: list | None) -> dict | None:
    if fm.get("type") != "strategy" and "backtest_status" not in fm:
        return None
    runnable = None
    gate_counts: dict = {}
    if gates:
        flags = [_gate_runnable(g.get("runnable")) for g in gates]
        n_true = flags.count("true")
        n_partial = flags.count("partial")
        n_false = flags.count("false")
        gate_counts = {
            "total": len(flags),
            "runnable": n_true,
            "partial": n_partial,
            "not_runnable": n_false,
        }
        if n_true == len(flags):
            runnable = "all"
        elif n_true == 0 and n_partial == 0:
            runnable = "none"
        else:
            runnable = "partial"
    return {
        "backtest_status": _str_or_none(fm.get("backtest_status")),
        "horizon": _split_labels(fm.get("timeframe")),
        "strategy_type": _str_or_none(fm.get("strategy_type")),
        "complexity": _str_or_none(fm.get("complexity")),
        "crowding_risk": _str_or_none(fm.get("crowding_risk")),
        "markets": _str_list(fm.get("markets")),
        "edge_source": _str_list(fm.get("edge_source")),
        "expected_sharpe": _to_float(fm.get("expected_sharpe")),
        "expected_max_drawdown": _to_float(fm.get("expected_max_drawdown")),
        "breakeven_cost_bps": _to_float(fm.get("breakeven_cost_bps")),
        "expected_sharpe_source": "author_estimate",
        "runnable": runnable,
        "gate_counts": gate_counts,
    }


def _load_doc(md_file: Path) -> dict:
    try:
        content = md_file.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        content = ""
    fm_text, body = split_frontmatter(content)
    fm = _parse_frontmatter_text(fm_text)
    rel = md_file.relative_to(REPO_ROOT)
    path = rel.as_posix()
    parts = rel.parts  # ('wiki', 'markets', 'crypto', 'x.md')
    category = parts[1] if len(parts) > 2 else "(root)"

    title = _str_or_none(fm.get("title")) or md_file.stem
    doc_type = _str_or_none(fm.get("type")) or "unknown"
    tags = _str_list(fm.get("tags"))
    aliases = _str_list(fm.get("aliases"))

    raw_gates = fm.get("gates")
    gates = None
    if isinstance(raw_gates, list):
        gates = [jsonable(g) for g in raw_gates if isinstance(g, dict)] or None
    strategy = _build_strategy(fm, gates)

    # Names the page answers to (for the exact_title tier).
    title_norm = norm(title)
    exact_names = {title_norm}
    stripped = norm(_PAREN_RE.sub(" ", title))
    if stripped:
        exact_names.add(stripped)
    for inner in _PAREN_RE.findall(title):
        # Only an acronym in parentheses names the page, e.g. "(ADX)"; not a
        # qualifier such as "(Bitcoin)" or "(Hyperliquid Basket)".
        inner = inner.strip()
        if _ACRONYM_RE.fullmatch(inner):
            exact_names.add(norm(inner))
    alias_norms = [norm(a) for a in aliases if norm(a)]
    exact_names.update(alias_norms)
    exact_names.discard("")

    name_strings = [title_norm] + alias_norms
    name_tokens = set()
    for s in name_strings:
        name_tokens.update(s.split())

    tokens = tokenize(f"{title} {' '.join(aliases)} {body}")

    return {
        "path": path,
        "rel": path[len("wiki/") :] if path.startswith("wiki/") else path,
        "stem": md_file.stem.lower(),
        "frontmatter": fm,
        "title": title,
        "type": doc_type,
        "status": _str_or_none(fm.get("status")) or "unknown",
        "category": category,
        "tags": tags,
        "tags_lower": {t.lower() for t in tags},
        "aliases": aliases,
        "updated": _str_or_none(fm.get("updated")) or "",
        "body": body,
        "strategy": strategy,
        "gates": gates,
        "exact_names": exact_names,
        "name_padded": [f" {s} " for s in name_strings],
        "name_tokens": name_tokens,
        "tf": Counter(tokens),
        "dl": len(tokens),
        "coin_page": path.startswith("wiki/markets/crypto/") and doc_type == "entity",
        "_flat": None,
    }


class WikiIndex:
    """In-memory index of every wiki page with a BM25 inverted index."""

    def __init__(self, docs: list[dict], signature: tuple):
        self.docs = sorted(docs, key=lambda d: d["path"])
        self.signature = signature
        self.built_at = time.time()
        self.by_path = {d["path"].lower(): d for d in self.docs}
        self.by_rel = {d["rel"].lower(): d for d in self.docs}
        self.by_stem: dict[str, list[dict]] = {}
        self.postings: dict[str, list[tuple[int, int]]] = {}
        total = 0
        for i, d in enumerate(self.docs):
            self.by_stem.setdefault(d["stem"], []).append(d)
            total += d["dl"]
            for term, count in d["tf"].items():
                self.postings.setdefault(term, []).append((i, count))
        self.n = len(self.docs)
        self.avg_dl = total / max(self.n, 1)

    def bm25(self, terms: list[str], candidates: set[int] | None) -> dict[int, float]:
        scores: dict[int, float] = {}
        n, avg_dl = self.n, self.avg_dl
        for term in set(terms):
            plist = self.postings.get(term)
            if not plist:
                continue
            df = len(plist)
            idf = math.log((n - df + 0.5) / (df + 0.5) + 1)
            for i, tf in plist:
                if candidates is not None and i not in candidates:
                    continue
                dl = self.docs[i]["dl"]
                tf_norm = (tf * (BM25_K1 + 1)) / (
                    tf + BM25_K1 * (1 - BM25_B + BM25_B * dl / avg_dl)
                )
                scores[i] = scores.get(i, 0.0) + idf * tf_norm
        # Title/alias boost (as before): pages whose name holds a query term.
        unique = set(terms)
        for i in scores:
            if unique & self.docs[i]["name_tokens"]:
                scores[i] *= TITLE_BOOST
        return scores


_INDEX: WikiIndex | None = None
_LAST_CHECK = 0.0
_LOCK = threading.Lock()


def _wiki_signature() -> tuple:
    """Cheap change detector: file count plus max mtime of files and dirs."""
    count = 0
    latest = 0
    stack = [str(WIKI_ROOT)]
    while stack:
        top = stack.pop()
        try:
            latest = max(latest, os.stat(top).st_mtime_ns)
            with os.scandir(top) as it:
                for entry in it:
                    if entry.is_dir(follow_symlinks=False):
                        stack.append(entry.path)
                    elif entry.name.endswith(".md"):
                        count += 1
                        latest = max(latest, entry.stat().st_mtime_ns)
        except OSError:
            continue
    return (count, latest)


def _build_index(signature: tuple) -> WikiIndex:
    docs = []
    for md_file in WIKI_ROOT.rglob("*.md"):
        try:
            docs.append(_load_doc(md_file))
        except Exception as exc:  # one bad page must not break search
            print(f"search.py: skipped {md_file}: {exc}", file=sys.stderr)
    return WikiIndex(docs, signature)


def get_index(force: bool = False) -> WikiIndex:
    """Return the cached index, rebuilding it if the wiki changed."""
    global _INDEX, _LAST_CHECK
    with _LOCK:
        now = time.monotonic()
        if _INDEX is not None and not force and now - _LAST_CHECK < INDEX_CHECK_INTERVAL:
            return _INDEX
        signature = _wiki_signature()
        _LAST_CHECK = now
        if force or _INDEX is None or _INDEX.signature != signature:
            _INDEX = _build_index(signature)
        return _INDEX


def load_documents() -> list[dict]:
    """All indexed wiki documents (backwards-compatible helper)."""
    return get_index().docs


# --------------------------------------------------------------------------- #
# Search
# --------------------------------------------------------------------------- #
def _flat_body(doc: dict) -> str:
    if doc["_flat"] is None:
        doc["_flat"] = " ".join(doc["body"].split())
    return doc["_flat"]


def make_snippet(doc: dict, terms: list[str]) -> str:
    text = _flat_body(doc)
    if not terms:
        return text[:SNIPPET_CHARS]
    pattern = re.compile(
        r"(?<![a-z0-9])(?:" + "|".join(re.escape(t) for t in terms) + r")(?![a-z0-9])",
        re.IGNORECASE,
    )
    m = pattern.search(text)
    start = 0
    if m and m.end() > SNIPPET_CHARS - SNIPPET_LEAD // 2:
        start = max(0, m.start() - SNIPPET_LEAD)
        if start > 0:
            space = text.find(" ", start)
            start = space + 1 if 0 <= space < m.start() else m.start()
    end = min(len(text), start + SNIPPET_CHARS)
    if end < len(text):
        space = text.rfind(" ", start, end)
        if space > start + SNIPPET_CHARS // 2:
            end = space
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "… " + snippet
    if end < len(text):
        snippet += " …"
    return snippet


def _tier(doc: dict, q_norm: str, terms: list[str]) -> str:
    if q_norm in doc["exact_names"]:
        return "exact_title"
    if len(terms) > 1:
        padded = f" {q_norm} "
        if any(padded in name for name in doc["name_padded"]):
            return "title_phrase"
    unique = set(terms)
    if unique <= doc["name_tokens"]:
        return "title_terms"
    if all(t in doc["tf"] for t in unique):
        return "all_terms"
    return "any_term"


def _matches_filters(doc: dict, f: dict) -> bool:
    if f["tag"] and not (f["tag"] & doc["tags_lower"]):
        return False
    if f["type"] and doc["type"].lower() not in f["type"]:
        return False
    if f["status"] and doc["status"].lower() not in f["status"]:
        return False
    if not f["strategy_active"]:
        return True
    s = doc["strategy"]
    if s is None:
        return False

    def one(field_values, actual) -> bool:
        if not field_values:
            return True
        labels = {v.lower() for v in _split_labels(actual)}
        return bool(labels & set(field_values))

    def many(field_values, actual_list) -> bool:
        if not field_values:
            return True
        return bool({v.lower() for v in actual_list} & set(field_values))

    if not one(f["backtest_status"], s["backtest_status"]):
        return False
    if not many(f["horizon"], s["horizon"]):
        return False
    if not one(f["strategy_type"], s["strategy_type"]):
        return False
    if not one(f["complexity"], s["complexity"]):
        return False
    if not one(f["crowding_risk"], s["crowding_risk"]):
        return False
    if not many(f["market"], s["markets"]):
        return False
    if f["runnable"] and s["runnable"] not in f["runnable"]:
        return False
    return True


def result_row(doc: dict, score: float | None, match: str | None, terms: list[str]) -> dict:
    return {
        "path": doc["path"],
        "title": doc["title"],
        "type": doc["type"],
        "status": doc["status"],
        "category": doc["category"],
        "tags": doc["tags"],
        "updated": doc["updated"] or None,
        "score": None if score is None else round(score, 4),
        "match": match,
        "snippet": make_snippet(doc, terms),
        "strategy": doc["strategy"],
    }


def search(
    query: str = "",
    tag=None,
    type=None,  # noqa: A002 - mirrors the CLI/MCP parameter name
    status=None,
    limit: int = 10,
    backtest_status=None,
    horizon=None,
    strategy_type=None,
    complexity=None,
    crowding_risk=None,
    market=None,
    runnable=None,
) -> dict:
    """Run a search. Returns {query, count, order, results}.

    Every filter accepts a comma-separated string or a list (any-of match).
    Raises ValueError for an invalid ``runnable`` value.
    """
    filters = {
        "tag": set(_values(tag)),
        "type": _values(type),
        "status": _values(status),
        "backtest_status": _values(backtest_status),
        "horizon": _values(horizon),
        "strategy_type": _values(strategy_type),
        "complexity": _values(complexity),
        "crowding_risk": _values(crowding_risk),
        "market": _values(market),
        "runnable": _values(runnable),
    }
    bad = [v for v in filters["runnable"] if v not in RUNNABLE_VALUES]
    if bad:
        raise ValueError(
            f"invalid runnable value {bad[0]!r}; valid values: {', '.join(RUNNABLE_VALUES)}"
        )
    filters["strategy_active"] = any(filters[k] for k in STRATEGY_FILTERS)
    any_filter = filters["strategy_active"] or any(
        filters[k] for k in ("tag", "type", "status")
    )
    try:
        limit = int(limit)
    except (TypeError, ValueError):
        limit = 10
    limit = max(1, min(limit, MAX_LIMIT))

    index = get_index()
    terms = tokenize(query or "")
    candidates = (
        [i for i, d in enumerate(index.docs) if _matches_filters(d, filters)]
        if any_filter
        else None
    )

    if not terms:
        pool = index.docs if candidates is None else [index.docs[i] for i in candidates]
        if any_filter:
            order = "title"
            pool = sorted(pool, key=lambda d: (d["title"].lower(), d["path"]))
        else:
            order = "newest"
            pool = sorted(pool, key=lambda d: d["path"])
            pool = sorted(pool, key=lambda d: d["updated"], reverse=True)
        rows = [result_row(d, None, None, []) for d in pool[:limit]]
        return {"query": query or "", "count": len(rows), "order": order, "results": rows}

    scores = index.bm25(terms, None if candidates is None else set(candidates))
    q_norm = " ".join(terms)
    ranked = []
    for i, score in scores.items():
        doc = index.docs[i]
        tier = _tier(doc, q_norm, terms)
        ranked.append((TIERS.index(tier), 1 if doc["coin_page"] else 0, -score, doc["path"], tier, doc, score))
    ranked.sort(key=lambda r: r[:4])
    rows = [result_row(r[5], r[6], r[4], terms) for r in ranked[:limit]]
    return {"query": query, "count": len(rows), "order": "relevance", "results": rows}


# --------------------------------------------------------------------------- #
# Page lookup
# --------------------------------------------------------------------------- #
class InvalidPath(ValueError):
    pass


def _suggestions(text: str, index: WikiIndex) -> list[str]:
    words = tokenize(re.sub(r"\.md$", "", text, flags=re.IGNORECASE).replace("wiki/", " "))
    if words:
        found = search(" ".join(words), limit=5)["results"]
        if found:
            return [r["path"] for r in found]
    newest = sorted(index.docs, key=lambda d: d["updated"], reverse=True)[:5]
    return [d["path"] for d in newest]


def resolve_page(page_path: str) -> tuple[dict | None, list[str]]:
    """Resolve a full or short page path.

    Accepts 'wiki/strategies/x.md', 'strategies/x.md', 'strategies/x', 'x'.
    Returns (doc, []) when found, (None, suggestions) when not.
    Raises InvalidPath for paths outside wiki/ or non-Markdown files.
    """
    raw = (page_path or "").strip()
    if not raw:
        raise InvalidPath("Invalid page path: paths must refer to Markdown files inside wiki/.")
    wiki_dir = WIKI_ROOT.resolve()
    candidate = Path(raw)
    if candidate.is_absolute() or ".." in Path(raw.replace("\\", "/")).parts:
        full = (REPO_ROOT / candidate).resolve()
        if not full.is_relative_to(wiki_dir) or full.suffix.lower() != ".md":
            raise InvalidPath(
                "Invalid page path: paths must refer to Markdown files inside wiki/."
            )
        raw = full.relative_to(REPO_ROOT.resolve()).as_posix()
    else:
        # An existing repo file outside wiki/ (README.md, tools/x.py) is refused.
        outside = (REPO_ROOT / raw).resolve()
        if outside.is_file() and not outside.is_relative_to(wiki_dir):
            raise InvalidPath(
                "Invalid page path: paths must refer to Markdown files inside wiki/."
            )

    key = raw.replace("\\", "/").strip("/")
    while key.startswith("./"):
        key = key[2:]
    key = key.lower()
    if key.startswith("wiki/"):
        key = key[len("wiki/") :]
    suffix = Path(key).suffix
    if suffix and suffix != ".md":
        key_md = key + ".md"
    else:
        key_md = key if key.endswith(".md") else key + ".md"

    index = get_index()
    doc = index.by_rel.get(key_md)
    if doc is not None:
        return doc, []

    # Fresh file not yet in the cached index.
    disk = (WIKI_ROOT / key_md).resolve()
    if disk.is_relative_to(wiki_dir) and disk.is_file():
        index = get_index(force=True)
        doc = index.by_rel.get(disk.relative_to(wiki_dir).as_posix().lower())
        if doc is not None:
            return doc, []

    # Short path: unique match on trailing path segments.
    stem = Path(key_md).stem
    tail = "/" + key_md
    matches = [d for d in index.by_stem.get(stem, []) if ("/" + d["rel"].lower()).endswith(tail)]
    if len(matches) == 1:
        return matches[0], []
    if len(matches) > 1:
        return None, [d["path"] for d in matches[:5]]
    if suffix and suffix != ".md":
        raise InvalidPath("Invalid page path: paths must refer to Markdown files inside wiki/.")
    return None, _suggestions(raw, index)


def read_raw(doc: dict) -> str:
    return (REPO_ROOT / doc["path"]).read_text(encoding="utf-8")


def page_json(doc: dict) -> dict:
    return {
        "path": doc["path"],
        "title": doc["title"],
        "type": doc["type"],
        "status": doc["status"],
        "category": doc["category"],
        "tags": doc["tags"],
        "aliases": doc["aliases"],
        "updated": doc["updated"] or None,
        "strategy": doc["strategy"],
        "gates": doc["gates"],
        "markdown": doc["body"].lstrip("\n"),
    }


# --------------------------------------------------------------------------- #
# Stats
# --------------------------------------------------------------------------- #
def stats() -> dict:
    index = get_index()
    by_type: Counter = Counter()
    by_status: Counter = Counter()
    by_category: Counter = Counter()
    by_backtest: Counter = Counter()
    by_runnable: Counter = Counter()
    for d in index.docs:
        by_type[d["type"]] += 1
        by_status[d["status"]] += 1
        by_category[d["category"]] += 1
        s = d["strategy"]
        if s is not None:
            if s["backtest_status"]:
                by_backtest[s["backtest_status"]] += 1
            if s["runnable"]:
                by_runnable[s["runnable"]] += 1

    def ordered(c: Counter) -> dict:
        return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))

    return {
        "total_pages": index.n,
        "built_at": int(index.built_at),
        "by_type": ordered(by_type),
        "by_status": ordered(by_status),
        "by_category": ordered(by_category),
        "by_backtest_status": ordered(by_backtest),
        "by_runnable": ordered(by_runnable),
    }


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main():
    parser = argparse.ArgumentParser(description="Search the trading wiki")
    parser.add_argument("query", nargs="?", default="", help="Search query")
    parser.add_argument("--tag", help="Filter by tag (comma-separated = any of)")
    parser.add_argument("--type", help="Filter by page type")
    parser.add_argument("--status", help="Filter by status")
    parser.add_argument("--backtest-status", help="Strategy filter: backtest_status")
    parser.add_argument(
        "--horizon", help="Strategy filter: holding style (scalp, intraday, swing, position)"
    )
    parser.add_argument("--strategy-type", help="Strategy filter: strategy_type")
    parser.add_argument("--complexity", help="Strategy filter: complexity")
    parser.add_argument("--crowding-risk", help="Strategy filter: crowding_risk")
    parser.add_argument("--market", help="Strategy filter: markets list (e.g. crypto)")
    parser.add_argument("--runnable", help="Strategy filter: gate runnability (all, partial, none)")
    parser.add_argument("--limit", type=int, default=10, help="Max results")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    args = parser.parse_args()

    try:
        out = search(
            args.query,
            tag=args.tag,
            type=args.type,
            status=args.status,
            limit=args.limit,
            backtest_status=args.backtest_status,
            horizon=args.horizon,
            strategy_type=args.strategy_type,
            complexity=args.complexity,
            crowding_risk=args.crowding_risk,
            market=args.market,
            runnable=args.runnable,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    results = out["results"]
    if args.json:
        print(json_lib.dumps(results, indent=2, ensure_ascii=False))
        return
    if not results:
        print("No results found.")
        return
    for r in results:
        score = "  -  " if r["score"] is None else f"{r['score']:.2f}"
        tier = r["match"] or out["order"]
        print(f"  [{score}] {tier:<12} {r['path']}")
        line = f"         {r['title']} (type: {r['type']}, status: {r['status']}, updated: {r['updated']})"
        s = r["strategy"]
        if s:
            line += (
                f"\n         backtest: {s['backtest_status']}, horizon: {'/'.join(s['horizon']) or '-'}"
                f", runnable: {s['runnable']}"
            )
        print(line)
        print()


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
