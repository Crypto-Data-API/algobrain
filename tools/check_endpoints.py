#!/usr/bin/env python3
"""
CryptoDataAPI reference checker — validates every `/api/v1/...` citation in the wiki
against the live OpenAPI spec (https://cryptodataapi.com/api/openapi.json, public, no key).

Three checks:

  1. Paths   — every `/api/v1/...` path cited anywhere in `wiki/**/*.md` (prose, inline code,
               code blocks, curl lines, frontmatter) must match a spec route. `{param}` route
               segments are wildcards, so `/coins/BTC` matches `/coins/{symbol}`. Unknown paths
               get did-you-mean suggestions.
  2. Params  — every query parameter on a cited URL must be declared by the matched operation.
               Since API 2026-09-19 (/hyperliquid/*) and 2026-10-10 (indicators, quant/gex,
               quant/positioning, backtesting/klines, supply/unlocks, algobrain) those routes
               answer 400 `unknown_parameter`; elsewhere the API silently ignores the param,
               which is just as wrong. Literal values are also checked against declared
               `enum` / `pattern` / `minimum` / `maximum`. Params starting with `_` are ignored.
  3. Gates   — `gates:` lists in strategy frontmatter (schema in CLAUDE.md): structure (ids,
               roles, runnable, derived inputs), `endpoint` / `replay` through checks 1-2, and
               `field` / `replay_field` dotted paths resolved against the operation's 200
               response schema (`a.b`, `a[].b`, `a.{coin}.b`). Free-form schemas are reported
               as `unverifiable`, not as errors.

Citations are only checked when plausibly CryptoDataAPI: an explicit non-CryptoDataAPI host
(`https://api.santiment.net/api/v1/...`) is skipped, and a path whose first segment is not a
real CryptoDataAPI top-level segment is skipped unless its line mentions CryptoDataAPI /
X-API-Key. Wildcard prose (`/api/v1/backtesting/*`, `/api/v1/dex/...`) and bare family
references (`/api/v1/backtesting`) pass when the prefix exists.

Usage:
    python tools/check_endpoints.py                         # whole wiki, live spec
    python tools/check_endpoints.py --spec openapi.json     # offline, cached spec
    python tools/check_endpoints.py --only "wiki/strategies/**"
    python tools/check_endpoints.py --json report.json      # also write machine-readable report
    python tools/check_endpoints.py --verbose               # list every citation, not the first 5

Exit codes: 0 = no errors, 1 = errors found (or the spec could not be loaded).
Warnings and `unverifiable` fields never fail the run.
"""
import argparse
import difflib
import fnmatch
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install -r tools/requirements.txt")

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = REPO_ROOT / "wiki"
SPEC_URL = "https://cryptodataapi.com/api/openapi.json"
API_PREFIX = "/api/v1"
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head")

# Routes the changelog says answer 400 `unknown_parameter` for an unread query param.
# Everything else silently drops it (still an error: the caller gets data it did not ask for).
STRICT_PARAM_PREFIXES = (
    "/hyperliquid/",                       # 2026-09-19
    "/indicators/technical", "/indicators/signum-rgg", "/indicators/adx",  # 2026-10-10
    "/algobrain/search", "/algobrain/page",
    "/backtesting/klines",
    "/quant/gex", "/quant/positioning",
    "/supply/unlocks",
)

GATE_ROLES = {"universe", "entry", "filter", "exit", "stop", "sizing"}
GATE_INPUTS = {"position", "derived"}
GATE_KEYS = {"id", "role", "rule", "runnable", "endpoint", "field", "replay", "replay_field",
             "input", "inputs", "note"}
GATE_PLACEHOLDERS = {"coin", "symbol", "asset", "start", "end", "date", "interval",
                     "category", "chain"}
RUNNABLE_RANK = {True: 2, "partial": 1, False: 0}
# Common cross-route spellings: the API says `symbol` on most routes, `coin` on Hyperliquid ones.
PARAM_ALIASES = {
    "coin": ["symbol", "coins"], "symbol": ["coin", "symbols"], "coins": ["symbols", "symbol"],
    "symbols": ["coins", "coin"], "days": ["window_days", "hours", "from"],
    "period": ["ma_period", "interval"], "ma": ["ma_period"], "window": ["window_days", "minutes"],
    "from": ["start"], "to": ["end"], "start": ["from"], "end": ["to"], "timeframe": ["interval"],
}

CATEGORIES = [
    # (key, label, severity)
    ("unknown_path", "Unknown paths", "error"),
    ("unknown_param", "Unknown query parameters", "error"),
    ("enum_violation", "Enum / pattern violations", "error"),
    ("range_violation", "Out-of-range values", "error"),
    ("gate_field", "Gate field errors", "error"),
    ("gate_structure", "Gate structure errors", "error"),
    ("gate_warning", "Gate warnings", "warning"),
    ("unverifiable", "Unverifiable gate fields (free-form schema)", "info"),
    ("documented_missing", "Paths cited as retired / non-existent (line says so)", "info"),
    ("documented_error_example", "Bad params cited as examples of the API's 400 (line says so)", "info"),
    ("prefix_reference", "Prefix references (path stem of real routes, no query)", "info"),
]
SEVERITY = {k: s for k, _, s in CATEGORIES}

# --- citation extraction ----------------------------------------------------------------

# Path chars: plain URL chars plus whole `{...}` / `<...>` placeholder tokens.
_PATH_CHARS = r"(?:\{[^{}\s`]*\}|<[A-Za-z0-9_\-]+>|[A-Za-z0-9_\-./*:$…%])"
_QUERY_CHARS = r"(?:\{[^{}\s`]*\}|<[A-Za-z0-9_\-]+>|[^\s#'\"`)\]|<>{}])"
CITATION_RE = re.compile(
    r"(?P<host>https?://[A-Za-z0-9.\-:]+|\$\{?[A-Za-z_]+\}?|\{[A-Za-z_]+\})?"
    r"(?P<path>" + re.escape(API_PREFIX) + r"(?![A-Za-z0-9_\-])" + _PATH_CHARS + r"*)"
    r"(?:\?(?P<query>" + _QUERY_CHARS + r"*))?"
)
CDA_LINE_HINT = re.compile(r"cryptodataapi|x-api-key|\bCDA\b", re.I)
# A non-CryptoDataAPI first segment on a line naming another vendor is that vendor's API.
THIRD_PARTY_HINT = re.compile(
    r"santiment|lunarcrush|coingecko|coinmarketcap|glassnode|coinglass|cryptoquant|nansen|"
    r"messari|kaiko|amberdata|defillama|dune|the tie|laevitas|tardis|alternative\.me|etherscan|"
    r"non-cryptodataapi|not (?:a )?cryptodataapi", re.I)
# Short-form citations (`/hyperliquid/candles?coin=BTC`, no /api/v1) are only read from inline
# code, and only for top-level segments that are not also common words / wiki folder names.
SHORT_FORM_EXCLUDE = {"auth", "payments", "wallet", "health", "stream", "webhooks", "pricing",
                      "changelog", "strategies", "news", "exchanges", "volume"}
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
SHORT_FORM_RE = re.compile(
    r"^(?:(?:GET|POST|PUT|PATCH|DELETE)\s+)?(?P<path>/[a-z][a-z0-9\-]*" + _PATH_CHARS + r"*)"
    r"(?:\?(?P<query>" + _QUERY_CHARS + r"*))?")
STRIKE_RE = re.compile(r"~~.+?~~")
# Lines that cite a path in order to say it does NOT exist (retired, invented, renamed).
# Unknown paths on such lines are reported as `documented_missing` (info), not errors.
NEGATION_HINT = re.compile(
    r"retired|no longer|never existed|does not exist|doesn't exist|not (?:a|an) cryptodataapi|"
    r"no `?[^`]{0,40}`? ?route exists|used to be|path history|invented|was renamed|renamed to|"
    r"coming soon|\bdisabled\b|not in the (?:live )?(?:openapi )?spec|not a real (?:path|route|endpoint)", re.I)
# Lines that cite a bad URL as an example of the API's error behaviour (400 / 404 bodies).
ERROR_EXAMPLE_HINT = re.compile(
    r"\b40[04]s?\b|unknown_parameter|unknown_coin|\bhints? at\b|\babsent\b|silent-ignore|"
    r"used to ignore|returned the whole|instead of ignoring", re.I)
PLACEHOLDER_SEG = re.compile(r"^(\{[^{}]*\}|<[^<>]*>|:[A-Za-z_]+|\$\{?[A-Za-z_]+\}?|\.\.\.|…)$")
TRAILING_JUNK = ".,;:!\\'\"`)*"


PLACEHOLDER_WORDS = {"SYMBOL", "COIN", "ASSET", "ADDRESS", "START", "END", "DATE", "INTERVAL",
                     "N", "X", "VALUE", "KEY", "TS", "MS"}


def is_placeholder_value(v):
    return (not v or "{" in v or "<" in v or "$" in v or "..." in v or "…" in v
            or v in PLACEHOLDER_WORDS)


# --- spec loading -----------------------------------------------------------------------

def load_spec(path=None, timeout=60):
    if path:
        text = Path(path).read_text(encoding="utf-8-sig")
        source = str(path)
    else:
        req = urllib.request.Request(SPEC_URL, headers={
            "Accept": "application/json", "User-Agent": "AlgoBrain-endpoint-checker/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            text = resp.read().decode("utf-8-sig")
        source = SPEC_URL
    spec = json.loads(text)
    if not isinstance(spec.get("paths"), dict):
        raise ValueError("spec has no `paths` object")
    return spec, source


class Spec:
    def __init__(self, spec):
        self.raw = spec
        self.schemas = spec.get("components", {}).get("schemas", {})
        self.comp_params = spec.get("components", {}).get("parameters", {})
        self.routes = []  # (template, segments, ops)
        for template, ops in spec["paths"].items():
            if not template.startswith(API_PREFIX):
                continue
            rel = template[len(API_PREFIX):] or "/"
            segs = [s for s in rel.split("/") if s]
            ops = {m: o for m, o in ops.items() if m in HTTP_METHODS and isinstance(o, dict)}
            self.routes.append((template, segs, ops))
        self.top_segments = {segs[0] for _, segs, _ in self.routes if segs}
        self.templates = [t for t, _, _ in self.routes]
        self.by_template = {t: (segs, ops) for t, segs, ops in self.routes}

    # -- refs / schemas --
    def deref(self, node, _depth=0):
        while isinstance(node, dict) and "$ref" in node and _depth < 50:
            ref = node["$ref"]
            name = ref.rsplit("/", 1)[-1]
            if "/parameters/" in ref:
                node = self.comp_params.get(name, {})
            else:
                node = self.schemas.get(name, {})
            _depth += 1
        return node if isinstance(node, dict) else {}

    # -- route matching --
    def match(self, segs):
        """Best matching route for cited segments, or None. Cited placeholders only match
        spec params; cited literals match spec literals (preferred) or spec params."""
        best, best_score = None, -1
        for template, rsegs, ops in self.routes:
            if len(rsegs) != len(segs):
                continue
            score = 0
            for c, r in zip(segs, rsegs):
                r_param = r.startswith("{")
                c_ph = bool(PLACEHOLDER_SEG.match(c))
                if r_param:
                    score += 2 if c_ph else 1
                elif c_ph:
                    score = -1
                    break
                elif c == r:
                    score += 3
                else:
                    score = -1
                    break
            if score > best_score:
                best, best_score = template, score
        return best

    def has_prefix(self, segs, partial=""):
        """Some route starts with `segs` (and, if given, a next segment starting `partial`)."""
        n = len(segs)
        return any(len(r) >= n + (1 if partial else 0)
                   and all(c == x or x.startswith("{") or PLACEHOLDER_SEG.match(c)
                           for c, x in zip(segs, r[:n]))
                   and (not partial or r[n].startswith(partial) or r[n].startswith("{"))
                   for _, r, _ in self.routes)

    def suggest_paths(self, cited_rel, n=3):
        cands = [t[len(API_PREFIX):] for t in self.templates]
        segs = [s for s in cited_rel.split("/") if s]
        fam = [c for c in cands if segs and c.split("/")[1:2] == segs[:1]]
        out = difflib.get_close_matches(cited_rel, fam, n=n, cutoff=0.5)
        for c in difflib.get_close_matches(cited_rel, cands, n=n, cutoff=0.6):
            if c not in out:
                out.append(c)
        if not out and fam:
            out = fam[:n]
        return [API_PREFIX + c for c in out[:n]]

    def params(self, template):
        """{name: param} over all operations of a route (GET first)."""
        _, ops = self.by_template[template]
        out = {}
        for m in sorted(ops, key=lambda m: m != "get"):
            for p in ops[m].get("parameters", []) or []:
                p = self.deref(p)
                if p.get("in") in ("query", "path") and p.get("name"):
                    out.setdefault(p["name"], p)
        return out

    def response_schema(self, template):
        _, ops = self.by_template[template]
        for m in ("get", "post"):
            op = ops.get(m)
            if not op:
                continue
            for code in ("200", "201", "2XX", "default"):
                r = op.get("responses", {}).get(code)
                if not r:
                    continue
                content = self.deref(r).get("content", {})
                for ct in ("application/json", *content.keys()):
                    sch = content.get(ct, {}).get("schema")
                    if sch is not None:
                        return sch
        return None

    def routes_declaring(self, family, names):
        out = []
        for template, segs, _ in self.routes:
            if segs and segs[0] == family and all(n in self.params(template) for n in names):
                out.append(template)
        return out

    # -- field resolution --
    def _branches(self, node):
        """Expand a schema into concrete alternatives (allOf merged, anyOf/oneOf split)."""
        node = self.deref(node)
        if "allOf" in node:
            merged = {k: v for k, v in node.items() if k != "allOf"}
            props = dict(merged.get("properties", {}))
            for sub in node["allOf"]:
                for b in self._branches(sub):
                    props.update(b.get("properties", {}))
                    for k in ("type", "items", "additionalProperties"):
                        if k in b and k not in merged:
                            merged[k] = b[k]
            if props:
                merged["properties"] = props
            return [merged]
        alts = node.get("anyOf") or node.get("oneOf")
        if alts:
            out = []
            for a in alts:
                for b in self._branches(a):
                    if b.get("type") != "null":
                        out.append(b)
            return out or [{}]
        return [node]

    def resolve_field(self, schema, field):
        """Returns ('ok'|'unverifiable'|'error', message)."""
        if schema is None:
            return "unverifiable", "operation declares no response schema"
        tokens = []
        for part in field.split("."):
            m = re.match(r"^([^\[\]]*)((?:\[\d*\])*)$", part)
            if not m:
                return "error", f"cannot parse field segment `{part}`"
            if m.group(1):
                tokens.append(("key", m.group(1)))
            tokens.extend(("items", None) for _ in re.findall(r"\[\d*\]", m.group(2)))
        return self._walk(schema, tokens, [])

    def _walk(self, node, tokens, trail):
        if not tokens:
            return "ok", ""
        kind, key = tokens[0]
        here = ".".join(trail) or "<root>"
        results = []
        for b in self._branches(node):
            results.append(self._step(b, kind, key, tokens, trail, here))
        for status in ("ok", "unverifiable"):
            for r in results:
                if r[0] == status:
                    return r
        return results[0]

    def _step(self, b, kind, key, tokens, trail, here):
        props = b.get("properties") or {}
        addl = b.get("additionalProperties")
        free = (not props and not b.get("items") and (addl in (None, True, {}))
                and b.get("type") in (None, "object"))
        if kind == "items":
            if b.get("type") == "array" or "items" in b:
                items = b.get("items")
                if items in (None, {}, True):
                    return "unverifiable", f"`{here}[]` items are free-form"
                return self._walk(items, tokens[1:], trail[:-1] + [trail[-1] + "[]"] if trail else ["[]"])
            if free:
                return "unverifiable", f"`{here}` is free-form"
            return "error", f"`{here}` is not an array (type {b.get('type') or 'object'})"
        # key step
        if key in props:
            return self._walk(props[key], tokens[1:], trail + [key])
        is_ph = bool(re.match(r"^\{[^{}]*\}$", key))
        if isinstance(addl, dict) and addl:
            return self._walk(addl, tokens[1:], trail + [key])
        if free or addl is True:
            return "unverifiable", f"`{here}` is free-form (no declared properties)"
        if b.get("type") in ("string", "number", "integer", "boolean"):
            return "error", f"`{here}` is a {b['type']}, cannot descend into `{key}`"
        if b.get("type") == "array" or "items" in b:
            return "error", f"`{here}` is an array; use `{trail[-1] if trail else ''}[].{key}`"
        names = sorted(props)
        sugg = difflib.get_close_matches(key, names, n=3, cutoff=0.5)
        msg = f"no `{key}` under `{here}`" + (" (coin-keyed map not declared)" if is_ph else "")
        if sugg:
            msg += f"; did you mean {', '.join('`'+s+'`' for s in sugg)}?"
        elif names:
            msg += f"; has {', '.join('`'+n+'`' for n in names[:12])}" + (" ..." if len(names) > 12 else "")
        return "error", msg


# --- checking ---------------------------------------------------------------------------

class Report:
    def __init__(self):
        self.findings = []
        self.stats = defaultdict(int)

    def add(self, category, file, line, message, **extra):
        f = {"category": category, "severity": SEVERITY[category], "file": file,
             "line": line, "message": message}
        f.update({k: v for k, v in extra.items() if v is not None})
        self.findings.append(f)


def clean_citation(path, query):
    path = path.replace("\\_", "_")
    if query is not None:
        query = query.replace("&amp;", "&").replace("\\_", "_").replace("\\&", "&")
        query = query.rstrip(TRAILING_JUNK)
    else:
        stripped = path.rstrip(TRAILING_JUNK)
        tail = path[len(stripped):]
        # keep one `*` as a wildcard (`/backtesting/*`, `/on-chain/whales*`); `**` is bold
        if tail.startswith("*") and not tail.startswith("**"):
            stripped += "*"
        path = stripped
    if path.endswith("/") and len(path) > len(API_PREFIX) + 1:
        path = path.rstrip("/")
    return path, query


def check_url(spec, report, rel_file, line_no, path, query, context, gate_id=None,
              gate_key=None, line_text="", third_party_line=False):
    """Path + query checks for one citation. Returns the matched template or None."""
    rel = path[len(API_PREFIX):]
    segs = [s for s in rel.split("/") if s]
    base = dict(file=rel_file, line=line_no, cited=path + (f"?{query}" if query else ""),
                context=context, gate_id=gate_id, gate_key=gate_key)
    if not segs:
        report.stats["skipped_bare_prefix"] += 1
        return None
    # wildcard prose: /api/v1/backtesting/*, /api/v1/dex/...
    wild_idx = next((i for i, s in enumerate(segs) if "*" in s or s in ("...", "…")), None)
    if wild_idx is not None:
        partial = segs[wild_idx].split("*")[0] if "*" in segs[wild_idx] else ""
        if spec.has_prefix(segs[:wild_idx], partial):
            report.stats["wildcard_ok"] += 1
            return None
        stem = f"{API_PREFIX}/{'/'.join(segs[:wild_idx] + ([partial] if partial else []))}*"
        cat = "documented_missing" if context != "gate" and (
            NEGATION_HINT.search(line_text) or ERROR_EXAMPLE_HINT.search(line_text)) else "unknown_path"
        report.add(cat, message=f"wildcard `{stem}` matches no route",
                   pattern=stem,
                   suggestion=spec.suggest_paths("/" + "/".join(segs[:wild_idx])), **base)
        return None
    template = spec.match(segs)
    if template is None:
        if len(segs) == 1 and segs[0] in spec.top_segments and not query and context != "gate":
            report.stats["family_reference_ok"] += 1
            return None
        norm = "/" + "/".join("{}" if PLACEHOLDER_SEG.match(s) else s for s in segs)
        if context != "gate" and (NEGATION_HINT.search(line_text) or ERROR_EXAMPLE_HINT.search(line_text)):
            report.add("documented_missing", message=f"`{path}` matches no route (line documents it as missing)",
                       pattern=API_PREFIX + norm, **base)
            return None
        if third_party_line:
            # short form that matches no route on a line naming another vendor: their API
            report.stats["skipped_third_party_short"] += 1
            report.skipped.append({"file": rel_file, "line": line_no, "cited": path,
                                   "reason": "unmatched short form on a line naming another vendor"})
            return None
        if context != "gate" and not query and spec.has_prefix(segs):
            report.add("prefix_reference", message=f"`{path}` is only a stem of real routes",
                       pattern=API_PREFIX + norm, suggestion=spec.suggest_paths("/" + "/".join(segs)), **base)
            return None
        report.add("unknown_path", message=f"`{path}` matches no route",
                   pattern=API_PREFIX + norm, suggestion=spec.suggest_paths("/" + "/".join(segs)),
                   **base)
        return None
    report.stats["paths_ok"] += 1
    if query:
        example = context != "gate" and bool(ERROR_EXAMPLE_HINT.search(line_text))
        check_query(spec, report, template, query, base, example)
    return template


def check_query(spec, report, template, query, base, example=False):
    declared = spec.params(template)
    rel_t = template[len(API_PREFIX):]
    strict = any(rel_t.startswith(p) for p in STRICT_PARAM_PREFIXES)
    unknown = []
    for pair in query.split("&"):
        if not pair:
            continue
        name, _, value = pair.partition("=")
        name = name.strip()
        if not name or name.startswith("_") or not re.match(r"^[A-Za-z0-9_\-\[\].]+$", name):
            continue
        p = declared.get(name)
        if p is None:
            unknown.append(name)
            continue
        report.stats["params_ok"] += 1
        check_value(spec, report, template, name, value, p, base)
    for name in unknown:
        names = sorted(n for n, p in declared.items() if p.get("in") == "query")
        sugg = [a for a in PARAM_ALIASES.get(name, []) if a in names]
        sugg += [s for s in difflib.get_close_matches(name, names, n=2, cutoff=0.6) if s not in sugg]
        family = rel_t.split("/")[1]
        others = [t for t in spec.routes_declaring(family, [name]) if t != template]
        if others:
            others.sort(key=lambda t: -difflib.SequenceMatcher(None, t, template).ratio())
        msg = (f"`{name}` is not a parameter of `{template}`"
               + (" (400 unknown_parameter)" if strict else " (silently ignored)")
               + f"; accepts: {', '.join(names) or 'no query params'}")
        report.add("documented_error_example" if example else "unknown_param",
                   message=msg, route=template, param=name, strict=strict,
                   pattern=f"{template}?{name}=",
                   suggestion=([f"?{s}=" for s in sugg] + [f"{t}?{name}=" for t in others[:2]]) or None,
                   **base)


def check_value(spec, report, template, name, value, p, base):
    if is_placeholder_value(value):
        return
    sch = spec.deref(p.get("schema", {}))
    alts = [sch] + [spec.deref(a) for a in sch.get("anyOf", []) + sch.get("oneOf", [])]
    enums, patterns, rng = [], [], None
    for a in alts:
        enums += a.get("enum", [])
        if a.get("pattern"):
            patterns.append(a["pattern"])
        if a.get("type") in ("integer", "number") and ("minimum" in a or "maximum" in a):
            rng = (a.get("minimum"), a.get("maximum"), a.get("type"))
    # comma lists on enum params; `1h/4h` alternatives in prose
    values = [v for v in re.split(r"[,/]", value) if v] or [value]
    if enums or patterns:
        bad = [v for v in values
               if not (v in [str(e) for e in enums] or any(re.fullmatch(pt, v) for pt in patterns))]
        if bad:
            allowed = [str(e) for e in enums] + [f"/{pt}/" for pt in patterns]
            report.add("enum_violation",
                       message=f"`{name}={value}` not allowed on `{template}`; allowed: {', '.join(allowed)}",
                       route=template, param=name, value=value, pattern=f"{template}?{name}={value}",
                       suggestion=difflib.get_close_matches(bad[0], [str(e) for e in enums], n=1, cutoff=0.3) or None,
                       **base)
            return
    if rng:
        try:
            num = float(value)
        except ValueError:
            return
        lo, hi, _ = rng
        if (lo is not None and num < lo) or (hi is not None and num > hi):
            report.add("range_violation",
                       message=f"`{name}={value}` outside [{lo}, {hi}] on `{template}`",
                       route=template, param=name, value=value,
                       pattern=f"{template}?{name}=<out of [{lo},{hi}]>", **base)


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, 0
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.DOTALL)
    if not m:
        return None, 0
    return m.group(1), m.group(1).count("\n") + 2  # last frontmatter line number (closing ---)


def gate_block_lines(fm_text):
    """Line numbers (1-based, file) of `endpoint:` / `replay:` keys inside the gates block."""
    lines = fm_text.split("\n")
    skip, in_gates = set(), False
    for i, ln in enumerate(lines, start=2):
        if re.match(r"^gates\s*:", ln):
            in_gates = True
            continue
        if in_gates and re.match(r"^\S", ln):
            in_gates = False
        if in_gates and re.match(r"^\s*-?\s*(endpoint|replay)\s*:", ln):
            skip.add(i)
    return skip


def scan_text(spec, report, rel_file, text, skip_lines, short_form=True):
    short_segs = spec.top_segments - SHORT_FORM_EXCLUDE
    for line_no, line in enumerate(text.split("\n"), start=1):
        if line_no in skip_lines:
            continue
        struck = [m.span() for m in STRIKE_RE.finditer(line)] if "~~" in line else []
        if API_PREFIX in line:
            for m in CITATION_RE.finditer(line):
                host = m.group("host") or ""
                path, query = clean_citation(m.group("path"), m.group("query"))
                report.stats["citations"] += 1
                if any(a <= m.start() < b for a, b in struck):
                    # ~~/api/v1/...~~ = deliberately documented as retired
                    report.stats["skipped_struck_through"] += 1
                    continue
                if host.startswith("http") and "cryptodataapi" not in host.lower() \
                        and not re.search(r"localhost|127\.0\.0\.1", host):
                    report.stats["skipped_third_party_host"] += 1
                    report.skipped.append({"file": rel_file, "line": line_no, "cited": m.group(0),
                                           "reason": "third-party host"})
                    continue
                segs = [s for s in path[len(API_PREFIX):].split("/") if s]
                if segs and segs[0] not in spec.top_segments and not host.startswith("http") \
                        and (not CDA_LINE_HINT.search(line) or THIRD_PARTY_HINT.search(line)):
                    report.stats["skipped_non_cda_segment"] += 1
                    report.skipped.append({"file": rel_file, "line": line_no, "cited": m.group(0),
                                           "reason": "non-CryptoDataAPI first segment"})
                    continue
                check_url(spec, report, rel_file, line_no, path, query, "text", line_text=line)
        if short_form and "`/" in line:
            for cm in INLINE_CODE_RE.finditer(line):
                sm = SHORT_FORM_RE.match(cm.group(1).strip())
                if not sm:
                    continue
                rel_path = sm.group("path")
                segs = [s for s in rel_path.split("/") if s]
                if not segs or segs[0] not in short_segs or rel_path.endswith(".md"):
                    continue
                if any(a <= cm.start() < b for a, b in struck):
                    report.stats["skipped_struck_through"] += 1
                    continue
                path, query = clean_citation(API_PREFIX + rel_path, sm.group("query"))
                report.stats["citations_short_form"] += 1
                check_url(spec, report, rel_file, line_no, path, query, "short-form", line_text=line,
                          third_party_line=bool(THIRD_PARTY_HINT.search(line)))


def check_gates(spec, report, rel_file, text, fm_text):
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as e:
        if re.search(r"^gates\s*:", fm_text, re.M):
            report.add("gate_structure", rel_file, 1, f"frontmatter YAML does not parse: {e}".split("\n")[0],
                       pattern="frontmatter YAML parse error")
        return
    if not isinstance(fm, dict) or "gates" not in fm:
        return
    gates = fm["gates"]
    fm_lines = fm_text.split("\n")

    # File line of each gate's first line (`- id:` / `- role:` ...), in list order.
    gate_starts, in_gates, gate_indent = [], False, 0
    for i, ln in enumerate(fm_lines, start=2):
        if re.match(r"^gates\s*:", ln):
            in_gates = True
            continue
        if in_gates and re.match(r"^\S", ln):
            break
        if in_gates and re.match(r"^\s*-\s+\w+\s*:", ln) and \
                (not gate_starts or len(ln) - len(ln.lstrip()) <= gate_indent):
            if not gate_starts:
                gate_indent = len(ln) - len(ln.lstrip())
            gate_starts.append(i)

    def line_of(idx, key=None):
        start = gate_starts[idx] if idx < len(gate_starts) else 1
        if key is None or start == 1:
            return start
        for i in range(start, len(fm_lines) + 2):
            ln = fm_lines[i - 2]
            if i > start and (re.match(r"^\s*-\s", ln) and len(ln) - len(ln.lstrip()) <= gate_indent
                              or re.match(r"^\S", ln)):
                break
            if re.match(r"^\s*-?\s*" + re.escape(key) + r"\s*:", ln):
                return i
        return start

    if not isinstance(gates, list):
        report.add("gate_structure", rel_file, 1, "`gates` is not a list", pattern="gates not a list")
        return
    report.stats["gate_pages"] += 1
    ids = [g.get("id") for g in gates if isinstance(g, dict)]
    by_id = {g.get("id"): g for g in gates if isinstance(g, dict)}
    seen = set()
    for idx, g in enumerate(gates):
        report.stats["gates"] += 1
        if not isinstance(g, dict):
            report.add("gate_structure", rel_file, 1, f"gate #{idx + 1} is not a mapping", pattern="gate not a mapping")
            continue
        gid = g.get("id")
        ln = line_of(idx)

        def err(msg, pattern, key=None, cat="gate_structure", **extra):
            report.add(cat, rel_file, line_of(idx, key) if key else ln, msg,
                       gate_id=gid, pattern=pattern, context="gate", **extra)

        if not gid or not isinstance(gid, str):
            err(f"gate #{idx + 1} has no string `id`", "missing id")
        else:
            if not re.match(r"^[a-z][a-z0-9_]*$", gid):
                err(f"id `{gid}` is not snake_case", "id not snake_case")
            if gid in seen:
                err(f"duplicate id `{gid}`", "duplicate id")
            seen.add(gid)
        for k in g:
            if k not in GATE_KEYS:
                err(f"unknown gate key `{k}`", f"unknown key `{k}`", key=k)
        if g.get("role") not in GATE_ROLES:
            err(f"role `{g.get('role')}` not in {sorted(GATE_ROLES)}", "bad role", key="role")
        runnable = g.get("runnable")
        if not (runnable is True or runnable is False or runnable == "partial"):
            err(f"runnable `{runnable!r}` not in (true, partial, false)", "bad runnable", key="runnable")
            runnable = None
        if not g.get("rule"):
            err("gate has no `rule`", "missing rule")
        inp = g.get("input")
        if inp is not None and inp not in GATE_INPUTS:
            err(f"input `{inp}` not in {sorted(GATE_INPUTS)}", "bad input", key="input")
        endpoint, field = g.get("endpoint"), g.get("field")
        replay, replay_field = g.get("replay"), g.get("replay_field")
        if runnable is False and (endpoint or field):
            err("runnable:false gate names an endpoint/field", "runnable:false with endpoint/field")
        if inp == "derived":
            inputs = g.get("inputs")
            if not isinstance(inputs, list) or not inputs:
                err("input:derived gate has no `inputs` list", "derived without inputs")
            else:
                for ref in inputs:
                    if ref == gid:
                        err(f"derived gate lists itself in inputs", "derived self-reference", key="inputs")
                    elif ref not in ids:
                        err(f"inputs references unknown gate id `{ref}`", "derived input missing", key="inputs")
                ranks = [RUNNABLE_RANK.get(by_id[r].get("runnable")) for r in inputs
                         if r in by_id and r != gid and by_id[r].get("runnable") in RUNNABLE_RANK]
                if runnable in RUNNABLE_RANK and ranks and RUNNABLE_RANK[runnable] > min(ranks):
                    err(f"derived gate is runnable `{runnable}` but its weakest input is "
                        f"`{[k for k, v in RUNNABLE_RANK.items() if v == min(ranks)][0]}`",
                        "derived more runnable than weakest input", key="runnable")
        elif g.get("inputs") is not None:
            err("`inputs` given without `input: derived`", "inputs without derived", key="inputs")
        if runnable in (True, "partial") and inp not in ("derived", "position") and not endpoint:
            err(f"runnable `{runnable}` gate has no endpoint", "runnable without endpoint")
        if endpoint and not field:
            err("endpoint given without field", "endpoint without field", key="endpoint")
        if field and not endpoint:
            err("field given without endpoint", "field without endpoint", key="field")
        if replay and not replay_field:
            err("replay given without replay_field", "replay without replay_field", key="replay")
        if replay_field and not replay:
            err("replay_field given without replay", "replay_field without replay", key="replay_field")

        for ep_key, f_key in (("endpoint", "field"), ("replay", "replay_field")):
            ep, fld = g.get(ep_key), g.get(f_key)
            if not ep:
                continue
            ep = str(ep).strip()
            for ph in re.findall(r"\{([^{}]*)\}", ep + " " + str(fld or "")):
                if ph not in GATE_PLACEHOLDERS:
                    report.add("gate_warning", rel_file, line_of(idx, ep_key), f"placeholder `{{{ph}}}` "
                               f"is not one of {sorted(GATE_PLACEHOLDERS)}", gate_id=gid,
                               pattern=f"placeholder {{{ph}}}", context="gate")
            if not ep.startswith(API_PREFIX):
                if ep.startswith("/"):
                    report.add("gate_structure", rel_file, line_of(idx, ep_key),
                               f"{ep_key} `{ep}` lacks the `{API_PREFIX}` prefix", gate_id=gid,
                               pattern=f"{ep_key} without {API_PREFIX}", context="gate")
                    ep = API_PREFIX + ep
                else:
                    report.add("unknown_path", rel_file, line_of(idx, ep_key), f"{ep_key} `{ep}` is not a path",
                               gate_id=gid, pattern=f"{ep_key} not a path", context="gate", cited=ep)
                    continue
            path, _, query = ep.partition("?")
            template = check_url(spec, report, rel_file, line_of(idx, ep_key), path.rstrip("/") or path,
                                 query or None, "gate", gate_id=gid, gate_key=ep_key)
            if template is None or not fld:
                continue
            status, msg = spec.resolve_field(spec.response_schema(template), str(fld).strip())
            fl = line_of(idx, f_key)
            if status == "ok":
                report.stats["gate_fields_ok"] += 1
            elif status == "unverifiable":
                report.add("unverifiable", rel_file, fl, f"{f_key} `{fld}` on `{template}`: {msg}",
                           gate_id=gid, gate_key=f_key, route=template, field=fld,
                           pattern=f"{template} :: {msg.split('`')[1] if '`' in msg else msg}",
                           context="gate")
            else:
                report.add("gate_field", rel_file, fl, f"{f_key} `{fld}` on `{template}`: {msg}",
                           gate_id=gid, gate_key=f_key, route=template, field=fld,
                           pattern=f"{template} :: {fld}", context="gate")


# --- output -----------------------------------------------------------------------------

def group_patterns(findings):
    groups = defaultdict(list)
    for f in findings:
        groups[(f["category"], f.get("pattern") or f["message"])].append(f)
    out = []
    for (cat, pat), fs in groups.items():
        sugg = next((f.get("suggestion") for f in fs if f.get("suggestion")), None)
        out.append({"category": cat, "pattern": pat, "count": len(fs),
                    "files": len({f["file"] for f in fs}), "suggestion": sugg,
                    "strict": fs[0].get("strict"), "message": fs[0]["message"],
                    "values": sorted({f["value"] for f in fs if f.get("value")}) or None,
                    "contexts": sorted({f.get("context", "text") for f in fs}),
                    "locations": [f"{f['file']}:{f['line']}" for f in fs]})
    out.sort(key=lambda g: (g["category"], -g["count"], g["pattern"]))
    return out


def print_report(report, patterns, spec_info, verbose):
    print(f"CryptoDataAPI reference check — spec {spec_info['version']} "
          f"({spec_info['paths']} paths) from {spec_info['source']}\n")
    for cat, label, sev in CATEGORIES:
        pats = [p for p in patterns if p["category"] == cat]
        if not pats or (cat == "unverifiable" and not verbose):
            continue
        total = sum(p["count"] for p in pats)
        print(f"== {label} [{sev}] — {total} citation(s), {len(pats)} pattern(s) ==")
        for p in pats:
            tag = " [400]" if p.get("strict") else ""
            print(f"  {p['pattern']}{tag}  x{p['count']} in {p['files']} file(s)")
            print(f"      {p['message']}")
            if p.get("values") and len(p["values"]) > 1:
                print(f"      values: {', '.join(p['values'])}")
            if p["suggestion"]:
                s = p["suggestion"]
                print(f"      suggest: {', '.join(s) if isinstance(s, list) else s}")
            locs = p["locations"] if verbose else p["locations"][:5]
            for loc in locs:
                print(f"      - {loc}")
            if len(p["locations"]) > len(locs):
                print(f"      ... {len(p['locations']) - len(locs)} more (--verbose)")
        print()
    if not verbose:
        unv = [p for p in patterns if p["category"] == "unverifiable"]
        if unv:
            print(f"(unverifiable: {sum(p['count'] for p in unv)} gate field(s) across "
                  f"{len(unv)} free-form schema node(s); --verbose to list)\n")
    s = report.summary
    print("Summary")
    for k, v in s.items():
        print(f"  {k:28} {v}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", help="read the OpenAPI spec from this file instead of fetching it")
    ap.add_argument("--json", metavar="PATH", help="write the machine-readable report here")
    ap.add_argument("--only", action="append", metavar="GLOB",
                    help="restrict to files matching this glob (repo-relative, e.g. 'wiki/strategies/**'); repeatable")
    ap.add_argument("--verbose", "-v", action="store_true", help="list every location and unverifiable fields")
    ap.add_argument("--include-log", action="store_true",
                    help="also check wiki/log.md (skipped by default: it records history, not live references)")
    ap.add_argument("--no-short-form", action="store_true",
                    help="only check /api/v1/... citations, not inline-code `/hyperliquid/...` short forms")
    args = ap.parse_args()

    try:
        raw, source = load_spec(args.spec)
    except Exception as e:  # network / parse failure
        print(f"error: could not load spec ({e})", file=sys.stderr)
        return 1
    spec = Spec(raw)
    spec_info = {"source": source, "version": raw.get("info", {}).get("version"),
                 "paths": len(spec.routes)}

    report = Report()
    report.skipped = []
    files = sorted(WIKI_ROOT.rglob("*.md"))
    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix()
        if args.only and not any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(path.name, g) for g in args.only):
            continue
        if rel == "wiki/log.md" and not args.include_log:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        report.stats["files_scanned"] += 1
        fm_text, _ = split_frontmatter(text)
        skip = gate_block_lines(fm_text) if fm_text else set()
        if API_PREFIX in text:
            report.stats["files_citing"] += 1
        if API_PREFIX in text or (not args.no_short_form and "`/" in text):
            scan_text(spec, report, rel, text, skip, short_form=not args.no_short_form)
        if fm_text and re.search(r"^gates\s*:", fm_text, re.M):
            check_gates(spec, report, rel, text, fm_text)

    counts = defaultdict(int)
    for f in report.findings:
        counts[f["category"]] += 1
    errors = sum(v for k, v in counts.items() if SEVERITY[k] == "error")
    report.summary = {
        "files_scanned": report.stats["files_scanned"],
        "files_citing_api": report.stats["files_citing"],
        "citations_seen": report.stats["citations"],
        "short_form_citations_seen": report.stats["citations_short_form"],
        "paths_ok": report.stats["paths_ok"],
        "params_ok": report.stats["params_ok"],
        "gate_pages": report.stats["gate_pages"],
        "gates": report.stats["gates"],
        "gate_fields_ok": report.stats["gate_fields_ok"],
        **{k: counts.get(k, 0) for k, _, _ in CATEGORIES},
        "unknown_param_400": sum(1 for f in report.findings if f["category"] == "unknown_param" and f.get("strict")),
        "skipped_third_party": report.stats["skipped_third_party_host"] + report.stats["skipped_non_cda_segment"]
                               + report.stats["skipped_third_party_short"],
        "skipped_struck_through": report.stats["skipped_struck_through"],
        "skipped_wildcard_or_family": report.stats["wildcard_ok"] + report.stats["family_reference_ok"]
                                      + report.stats["skipped_bare_prefix"],
        "errors": errors,
    }
    patterns = group_patterns(report.findings)
    print_report(report, patterns, spec_info, args.verbose)

    if args.json:
        out = {"spec": spec_info, "summary": report.summary, "patterns": patterns,
               "findings": report.findings, "skipped_non_cda": report.skipped}
        Path(args.json).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nJSON report written to {args.json}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
