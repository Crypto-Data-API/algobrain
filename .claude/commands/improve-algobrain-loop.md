---
description: One iteration — pick one bounded area of the AlgoBrain wiki to improve (~60 min of sub-agent work), verify, then commit + push with a changelog entry
allowed-tools: Bash(git:*), Read, Write, Edit, Grep, Glob, Agent, mcp__algobrain__*
---
One iteration of the daily AlgoBrain improvement loop. Follow every rule in `CLAUDE.md`
throughout (frontmatter schema, wikilinks, scope, approved tags, verified CryptoDataAPI
endpoints only). This command is self-contained — it can be run standalone or as the
payload of the `/start-loops` recurring loop.

## 0. Check the local MCP server

Try a quick `mcp__algobrain__wiki_stats` (or `wiki_lint`) call. If the server isn't
reachable, run `powershell -ExecutionPolicy Bypass -File tools/start_servers.ps1` (see
`/start-servers`) and retry once. If it still fails, fall back to Grep/Glob over `wiki/`
directly for this iteration and note in the log (step 3) that the MCP was unavailable.

## 1. Pick one bounded area

1. Read `.claude/wiki-improvement-backlog.md`, specifically the most recent entries under
   whatever "progress log" section is current. The structured Campaign 1/2 backlog is
   already complete — do not re-run finished items. Don't repeat the exact scope of the
   last 2-3 daily-loop entries.
2. Get a fresh read on wiki health via `wiki_lint` / `wiki_stats`, covering CLAUDE.md's
   Lint Workflow checklist: broken wikilinks, orphan pages, stale pages (status below
   `good` and not updated in >90 days), missing/incomplete frontmatter, empty pages,
   missing source citations, non-approved tags, duplicate content, scope drift
   (equity-specific content).
3. Also weigh: unresolved forward links surfaced by lint/grep, thin `stub`/`draft` pages
   with unusually high inbound-link counts, and any `## Contradictions` sections still
   marked pending resolution.
4. Pick ONE area sized to roughly what a single sub-agent can do well in about an hour
   (comparable to a ~5-page batch in past campaigns — see the completed batches in
   `wiki-improvement-backlog.md` for calibration). Prefer whichever issue is highest
   leverage (most pages affected, most inbound links, or a correctness problem) over
   purely cosmetic ones.
5. Write a short plan (2-5 sentences: what, why, expected file list) before delegating.
6. If a full lint pass comes back clean with nothing worth an hour of work, say so
   explicitly, skip straight to logging that ("nothing actionable found") and stop —
   do not manufacture busywork.

## 2. Delegate and verify

1. Delegate the actual editing to ONE sub-agent (`Agent` tool, run in the foreground since
   the next steps depend on its result) carrying: the plan, the relevant CLAUDE.md rules,
   and an explicit scope boundary — roughly 60 minutes of work, do not exceed this batch.
   Use a `general-purpose` agent by default.
2. When it reports back, verify the changes yourself: `git status --short`,
   `git diff --stat`, and spot-read 1-2 changed/created pages for frontmatter correctness,
   wikilink validity, and CLAUDE.md schema compliance (strategy pages need the full
   15-section structure; concept pages need `domain`/`prerequisites`/`difficulty`; etc.).
   Fix small issues directly rather than re-delegating.

## 3. Record and ship

1. Append one entry to `.claude/wiki-improvement-backlog.md` under a
   `## Daily improvement loop` section (create it, once, if absent) — date, what was
   picked and why, what changed, before/after counts if relevant. If step 1.6 found
   nothing actionable, log that instead of a change.
2. Update `wiki/log.md` per CLAUDE.md's Rules for the LLM if pages were created or
   substantively updated.
3. Update `CHANGELOG.md` at the repo root — newest entry first, dated, under
   Added/Changed/Fixed/Notes as applicable. Never write "CoinGecko" or "CoinMarketCap" —
   use neutral data-source phrasing instead.
4. If the change affects anything `README.md` describes (counts, features, setup steps,
   the MCP server, tooling, page counts), update the relevant section in the same commit.
   If touching counts, true them all up against `find wiki -name '*.md' | wc -l` — counts
   only live in the README's intro line and the "What's inside" table, nowhere else.
5. Commit and push:
   - Check `git status --short` and stage the specific changed files (not a blind `-A`).
   - Write a concise, imperative commit message with no vendor names, ending with
     `Co-Authored-By: Claude <model running this iteration> <noreply@anthropic.com>`.
   - `git push`. If it fails (diverged/conflict/rejected), stop and report — do not
     force-push or reset.
6. Report a short summary: what was picked, what changed, and the resulting commit hash
   (or "nothing actionable" if step 1.6 applied).

## Guardrails

- Bounded scope: one area per iteration, sized to ~60 minutes of sub-agent work — don't
  let it balloon into a multi-hour or dozens-of-files change.
- ADD, never destroy: preserve existing hand-written content. Deleting/merging pages
  follows the same care as the completed A9 duplicate cleanup in
  `wiki-improvement-backlog.md` (audit first, merge unique content, then delete).
- Crypto/trading/macro/AI scope only (CLAUDE.md's Scope section) — no equity-specific
  content.
- Only approved tags (CLAUDE.md's Approved Tags list) and verified CryptoDataAPI
  endpoints — never invent endpoint paths; check https://cryptodataapi.com/api/docs.
- Never commit `.env` or other secrets.
