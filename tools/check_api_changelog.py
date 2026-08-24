#!/usr/bin/env python3
"""
CryptoDataAPI changelog watcher — reports API releases the wiki has not yet absorbed.

The canonical feed is the public, key-free endpoint https://cryptodataapi.com/api/v1/changelog
(the human URL https://cryptodataapi.com/changelog serves the same JSON). It returns
`api_version` (CalVer YYYY-MM-DD, bumped on any breaking or notable response-shape change)
plus `changelog[]`, newest-first, each entry `{version, date, breaking, changes[]}`.

IMPORTANT: the feed only retains the **last 10 releases**. Anything older has scrolled off
permanently — there is no pagination; `?limit=`, `?since=` and `?all=` are all ignored. This
tool therefore warns when the local watermark is older than the oldest entry still served,
because releases in that window were never seen and cannot be recovered from the API.

State lives in `.claude/cryptodataapi-changelog-state.json` and records which versions have
been triaged, with a disposition:
    material — the release changed something the wiki documents; pages were edited
    noted    — real change, no wiki-visible surface (rate limits, internal fixes, infra)
    baseline — marked seen without triage (only via --init)

Usage:
    python tools/check_api_changelog.py                  # human-readable report of unprocessed releases
    python tools/check_api_changelog.py --json           # same, machine-readable
    python tools/check_api_changelog.py --all            # include already-processed releases
    python tools/check_api_changelog.py --mark-seen 2026-08-23 --disposition material --note "..."
    python tools/check_api_changelog.py --mark-seen 2026-08-22 2026-08-21 --disposition noted --note "..."
    python tools/check_api_changelog.py --init           # first run only: mark everything served as baseline

Exit codes: 0 = ran fine (with or without new releases), 1 = fetch/parse failure.
Check the output (or --json `unprocessed_count`) to branch on whether work is pending.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

# Windows consoles default to a non-UTF-8 codepage; changelog prose is full of em dashes.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):  # non-reconfigurable stream (pipe wrapper, older runtime)
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = REPO_ROOT / ".claude" / "cryptodataapi-changelog-state.json"
FEED_URL = "https://cryptodataapi.com/api/v1/changelog"
HUMAN_URL = "https://cryptodataapi.com/changelog"
DOCS_URL = "https://cryptodataapi.com/api/docs"
DISPOSITIONS = ("material", "noted", "baseline")


def fetch_changelog(url=FEED_URL, timeout=30):
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "AlgoBrain-changelog-watcher/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    if not isinstance(payload.get("changelog"), list):
        raise ValueError("response has no `changelog` array — feed shape changed?")
    return payload


def load_state():
    if not STATE_PATH.exists():
        return {"last_checked": None, "api_version_seen": None, "processed": []}
    with STATE_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def save_state(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(state, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def processed_versions(state):
    return {row["version"] for row in state.get("processed", [])}


def triage(payload, state):
    """Split the served releases into processed / unprocessed and detect a scroll-off gap."""
    seen = processed_versions(state)
    entries = sorted(payload["changelog"], key=lambda e: e.get("version", ""), reverse=True)
    unprocessed = [e for e in entries if e.get("version") not in seen]

    gap = None
    if seen and entries:
        newest_seen = max(seen)
        oldest_served = min(e.get("version", "") for e in entries)
        if oldest_served > newest_seen:
            gap = {
                "newest_processed": newest_seen,
                "oldest_still_served": oldest_served,
                "message": (
                    "releases between {} and {} scrolled off the 10-entry feed and were never "
                    "triaged — they are unrecoverable from the API; reconcile against {} instead"
                ).format(newest_seen, oldest_served, DOCS_URL),
            }
    return entries, unprocessed, gap


def render_entry(entry, index=None):
    head = "[{}] ".format(index) if index is not None else ""
    flag = "  ** BREAKING **" if entry.get("breaking") else ""
    lines = ["{}{} ({}){}".format(head, entry.get("version"), entry.get("date"), flag)]
    for change in entry.get("changes", []):
        lines.append("    - {}".format(change))
    return "\n".join(lines)


def cmd_report(args):
    try:
        payload = fetch_changelog()
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, json.JSONDecodeError) as exc:
        print("ERROR: could not fetch {}: {}".format(FEED_URL, exc), file=sys.stderr)
        print("       fall back to {} or {} for this iteration.".format(HUMAN_URL, DOCS_URL), file=sys.stderr)
        return 1

    state = load_state()
    entries, unprocessed, gap = triage(payload, state)

    state["last_checked"] = date.today().isoformat()
    state["api_version_seen"] = payload.get("api_version")
    save_state(state)

    if args.json:
        print(json.dumps({
            "api_version": payload.get("api_version"),
            "served_count": len(entries),
            "unprocessed_count": len(unprocessed),
            "breaking_unprocessed": [e["version"] for e in unprocessed if e.get("breaking")],
            "unprocessed": unprocessed,
            "entries": entries if args.all else None,
            "gap": gap,
            "state_path": str(STATE_PATH.relative_to(REPO_ROOT)),
        }, indent=2, ensure_ascii=False))
        return 0

    print("CryptoDataAPI changelog — api_version {}".format(payload.get("api_version")))
    print("feed: {}  (public, no key; last {} releases only)".format(FEED_URL, len(entries)))
    print("state: {}\n".format(STATE_PATH.relative_to(REPO_ROOT)))

    if gap:
        print("!! GAP WARNING: " + gap["message"] + "\n")

    shown = entries if args.all else unprocessed
    if not shown:
        print("No unprocessed releases — the wiki is level with the API changelog.")
        return 0

    label = "all served" if args.all else "UNPROCESSED"
    breaking = [e["version"] for e in shown if e.get("breaking")]
    print("{} {} release(s)".format(len(shown), label)
          + (" — BREAKING: {}".format(", ".join(breaking)) if breaking else "") + "\n")
    for i, entry in enumerate(shown, 1):
        print(render_entry(entry, i))
        print()

    if not args.all:
        print("Triage each against the wiki, then record the outcome:")
        print("  python tools/check_api_changelog.py --mark-seen <version>... "
              "--disposition material|noted --note \"what was done\"")
    return 0


def cmd_mark_seen(args):
    state = load_state()
    seen = processed_versions(state)
    today = date.today().isoformat()
    added = []
    for version in args.mark_seen:
        if version in seen:
            print("already recorded: {}".format(version))
            continue
        state.setdefault("processed", []).append({
            "version": version,
            "processed_on": today,
            "disposition": args.disposition,
            "note": args.note or "",
        })
        added.append(version)
    state["processed"].sort(key=lambda r: r["version"], reverse=True)
    state["last_checked"] = today
    save_state(state)
    print("recorded {} release(s) as {}".format(len(added), args.disposition)
          + (": {}".format(", ".join(added)) if added else ""))
    return 0


def cmd_init(args):
    state = load_state()
    if processed_versions(state):
        print("state file already has processed releases — refusing to re-baseline. "
              "Use --mark-seen for individual versions.", file=sys.stderr)
        return 1
    try:
        payload = fetch_changelog()
    except Exception as exc:  # noqa: BLE001 — any fetch/parse failure is equally fatal here
        print("ERROR: could not fetch {}: {}".format(FEED_URL, exc), file=sys.stderr)
        return 1
    today = date.today().isoformat()
    state["processed"] = [
        {
            "version": e["version"],
            "processed_on": today,
            "disposition": "baseline",
            "note": args.note or "baselined without triage",
        }
        for e in sorted(payload["changelog"], key=lambda e: e.get("version", ""), reverse=True)
    ]
    state["last_checked"] = today
    state["api_version_seen"] = payload.get("api_version")
    save_state(state)
    print("baselined {} release(s) — nothing was triaged against the wiki.".format(len(state["processed"])))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--all", action="store_true", help="include already-processed releases")
    parser.add_argument("--mark-seen", nargs="+", metavar="VERSION",
                        help="record these releases as triaged")
    parser.add_argument("--disposition", choices=DISPOSITIONS, default="noted",
                        help="how the release was handled (default: noted)")
    parser.add_argument("--note", help="one-line record of what was done")
    parser.add_argument("--init", action="store_true",
                        help="first run only: mark every served release as baseline without triage")
    args = parser.parse_args()

    if args.init:
        return cmd_init(args)
    if args.mark_seen:
        return cmd_mark_seen(args)
    return cmd_report(args)


if __name__ == "__main__":
    sys.exit(main())
