---
description: One iteration — fix a wiki problem or build new/expanded content (balanced across iterations), ~60 min of sub-agent work, verify, then commit + push with a changelog entry
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

## 1. Pick one bounded area — Fix or Build

This loop has two equally-valid tracks. Track A (**Fix**) finds and repairs problems.
Track B (**Build**) grows the wiki — new pages, expanded stubs, deeper existing content.
The loop must not become fix-only: a healthy wiki needs both, and lint noise is an
endless, self-replenishing well that will happily consume every iteration forever if you
let it. Deliberately balance the two — see step 0 below before picking.

### 0. Check the recent track balance

Read `.claude/wiki-improvement-backlog.md`'s last 3 `## Daily improvement loop` entries
and classify each as Fix or Build (a tag-audit/broken-link/schema-sync/dedup iteration is
Fix; a new-page/stub-expansion/section-deepening iteration is Build). **If 2 or more of
the last 3 were Fix, this iteration must be Build** — unless you find something urgent
(e.g. a bug actively corrupting data across hundreds of pages, on the order of the
iter-3 lint.py parsing bug), in which case do that fix but say explicitly in the log that
Build is now overdue. Apply the same logic in reverse if Build has dominated. Don't repeat
the exact scope of the last 2-3 entries either way.

### If this iteration is Fix

1. Get a fresh read on wiki health via `wiki_lint` / `wiki_stats`, covering CLAUDE.md's
   Lint Workflow checklist: broken wikilinks, orphan pages, stale pages (status below
   `good` and not updated in >90 days), missing/incomplete frontmatter, empty pages,
   missing source citations, non-approved tags, duplicate content, scope drift
   (equity-specific content).
2. Also weigh: unresolved forward links surfaced by lint/grep, and any `## Contradictions`
   sections still marked pending resolution.
3. Prefer whichever issue is highest leverage (most pages affected, most inbound links,
   or a correctness/tooling bug distorting the lint signal itself) over cosmetic ones.

### If this iteration is Build

Look for real, in-scope content the wiki should have and doesn't — not problems to patch,
things to add or deepen. Candidates, roughly in priority order:

1. **Expand stub/draft pages.** Find `status: stub` or `status: draft` pages with
   unusually high inbound-link counts (real demand for content that isn't there yet) via
   `wiki_lint`/grep, and bring 3-6 of them up to a full page for their type (concept pages
   get real explanation + examples + `## Getting the Data` where applicable; strategy
   pages get the full 15-section structure from CLAUDE.md's "Strategy page sections").
2. **Fill genuine forward-link gaps.** Unresolved `[[wikilinks]]` are fine by design
   (CLAUDE.md), but the ones with many inbound references across multiple pages are
   signals of real, wanted content — not the whole long tail of every unresolved link.
   Pick a cluster of 3-6 clearly-wanted missing pages and author them.
3. **Deepen existing pages missing standard sections.** A `good`/`review` page that's
   missing its `## Getting the Data (CryptoDataAPI)` section, the strategy `### AI agent
   workflow` sub-block, a worked example, or kill criteria (see the completed B9/B10/B12
   batches in `wiki-improvement-backlog.md` for the pattern) is underbuilt even though it
   isn't "broken" by lint's standards.
4. **Cover genuine gaps**: a real protocol/strategy-type/data-source/concept that's
   in-scope (crypto/trading/macro/AI per CLAUDE.md's Scope section) and plausibly
   important, but has no page and no inbound links pointing at it yet either — something
   you'd expect a well-read crypto-trading wiki to cover. Verify it's not already covered
   under an alias before creating it.
5. New pages must follow CLAUDE.md's schema fully (frontmatter, buildable strategy
   sections, verified CryptoDataAPI endpoints, wikilinks to related pages) — a rushed
   thin page is worse than not creating one, since it then needs its own future Fix pass.

### Either track — final steps

1. Pick ONE area sized to roughly what a single sub-agent can do well in about an hour
   (comparable to a ~5-page batch in past campaigns — see the completed batches in
   `wiki-improvement-backlog.md` for calibration).
2. Write a short plan (2-5 sentences: what, why, expected file list, which track) before
   delegating.
3. "Nothing actionable" should be rare — if Fix comes back clean, that's exactly the
   signal to switch to Build (there is always a stub to expand or a gap to fill while any
   `stub`/`draft` pages or high-inbound forward links remain). Only stop without acting if
   you've genuinely checked both tracks and found nothing — say so explicitly and log it.

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
   `## Daily improvement loop` section (create it, once, if absent) — date, **track
   (Fix or Build)**, what was picked and why, what changed, before/after counts if
   relevant. State the track explicitly (e.g. "iter N (Build): ...") so the next
   iteration's step 0 can classify it at a glance. If nothing actionable was found in
   either track, log that instead of a change.
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
6. Report a short summary: what was picked (including the track), what changed, and the
   resulting commit hash (or "nothing actionable" if neither track had anything to do).

## Guardrails

- Balance Fix and Build (see step 1.0) — this loop exists to grow the wiki, not just keep
  lint's counters down. A streak of Fix-only iterations is a bug in how the loop is being
  run, not a sign the wiki is in great shape.
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
