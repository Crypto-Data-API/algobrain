---
description: One iteration — absorb new CryptoDataAPI releases, then fix a wiki problem or build new/expanded content (balanced across iterations), ~60 min of sub-agent work, verify, then commit + push with a changelog entry
allowed-tools: Bash(git:*), Bash(python tools/*), Read, Write, Edit, Grep, Glob, Agent, WebFetch, mcp__algobrain__*
---
One iteration of the daily AlgoBrain improvement loop. Follow every rule in `CLAUDE.md`
throughout (frontmatter schema, wikilinks, scope, approved tags, verified CryptoDataAPI
endpoints only). This command is self-contained — it can be run standalone or as the
payload of the `/start-loops` recurring loop.

## 0. Check the local MCP server

Try a quick `mcp__algobrain__wiki_stats` (or `wiki_lint`) call. If the server isn't
reachable, run `<python> tools/manage_mcp.py start` (`python3` on macOS/Linux or `py` on
Windows; see `/start-servers`) and retry once. If it still fails, fall back to Grep/Glob
over `wiki/` directly for this iteration and note in the log (step 4) that the MCP was
unavailable.

## 1. Check the CryptoDataAPI changelog — every iteration

The wiki's canonical data layer ships changes continuously, and a wiki that documents a
renamed field or a dead endpoint is *wrong*, not merely incomplete. So every iteration
starts by reconciling against the upstream API changelog before choosing a track.

```
python tools/check_api_changelog.py
```

The watcher hits the public, key-free feed `https://cryptodataapi.com/api/v1/changelog`
(the human URL `https://cryptodataapi.com/changelog` serves the same JSON) and prints only
releases not yet recorded in `.claude/cryptodataapi-changelog-state.json`.

- **The feed retains only the last 10 releases** — there is no pagination and no history
  beyond that. If the tool prints a `GAP WARNING`, releases scrolled off unseen and are
  unrecoverable from the API; reconcile that window against
  https://cryptodataapi.com/api/docs instead and say so in the log.
- If the fetch fails (network, feed shape changed), say so in the log and carry on to
  Fix/Build — a changelog check is not worth burning an iteration on.

### Triage each unprocessed release

Classify every unprocessed release into exactly one of two dispositions:

- **material** — it changes something the wiki documents or should document: a new
  endpoint or endpoint family, a changed/renamed response field, a deprecated or removed
  route, a changed error contract, new categories/enum values, a new data family, or a
  plan/rate-limit change the wiki quotes.
- **noted** — a real change with no wiki-visible surface: internal fixes, infrastructure,
  site/marketing changes, or fixes to endpoints the wiki never documented.

Record the **noted** ones immediately — they cost nothing and keep the watermark moving:

```
python tools/check_api_changelog.py --mark-seen <version>... --disposition noted --note "why no wiki surface"
```

### Decide whether this is a Sync iteration

- **Any material release ⇒ this iteration is the Sync track**, and Sync takes priority
  over Fix and Build. A **breaking** release affecting a path the wiki documents outranks
  everything else in the loop.
- Sync is bounded like any other iteration (~60 min of sub-agent work, roughly 5-8 pages).
  If more material releases are pending than fit, do the highest-leverage ones — breaking
  first, then new endpoint families, then additive field changes — and **leave the rest
  unprocessed** for the next iteration rather than stretching the batch.
- **Sync iterations do not count toward the Fix/Build balance** in step 2. Log them as
  `iter N (Sync)`; step 2.0's balance check skips Sync entries when it classifies the last
  three *Fix/Build* iterations.
- If a Sync batch is small (one or two pages), finish it and then also do a normal
  Fix/Build pick in the same iteration — say so in the log.
- If nothing is material, mark everything noted and move on to step 2 as usual.

### How to integrate a material release

Every path you write must be verified against https://cryptodataapi.com/api/docs first —
the changelog is the *trigger*, the docs are the *authority*. CLAUDE.md's never-invent-an-
endpoint rule is absolute, and changelog prose sometimes describes routes loosely.

1. **New endpoint in an existing family** — add it to the endpoint table on the relevant
   `wiki/data-sources/cryptodataapi-<category>.md` page (path, what it returns, tier, key
   response fields), then grep for content pages whose `## Getting the Data (CryptoDataAPI)`
   section should now cite it.
2. **New category with no page** — create `wiki/data-sources/cryptodataapi-<category>.md`
   following the structure of its siblings, then register it in **all** of: the category
   map table on `cryptodataapi.md`, that page's `related:` frontmatter, the reverse
   `related:` links on adjacent category pages, and `data-sources-overview.md`.
3. **Changed or renamed response fields** — grep the whole wiki for the endpoint path and
   the old field names; fix every `## Getting the Data` section, curl example, and
   pseudocode block that shows the old shape. A stale field name in a strategy page's
   implementation sketch is a real bug for anyone following it.
4. **Deprecated or removed endpoints** — never delete silently (CLAUDE.md's ADD-never-
   destroy rule). Mark the entry deprecated with its date and point at the replacement, so
   readers hitting an old integration can find the migration.
5. **Rate limits, tiers, auth** — update the "Plans & rate limits" table on
   `cryptodataapi.md` plus any page or README line quoting the old numbers. Grep for the
   old figures; they get copied around.
6. **A genuinely new data family** (a new signal, regime, or metric — not just a new
   route) may warrant a new concept or strategy page, and new `### AI agent workflow`
   bullets on the strategy/indicator pages that can now use it. That is Sync doing
   Build-flavoured work; it still counts as Sync.

Then record what you did:

```
python tools/check_api_changelog.py --mark-seen <version>... --disposition material --note "pages touched"
```

## 2. Pick one bounded area — Fix or Build

If step 1 made this a full Sync iteration, skip to step 3 with the Sync plan.

This loop has two equally-valid tracks. Track A (**Fix**) finds and repairs problems.
Track B (**Build**) grows the wiki — new pages, expanded stubs, deeper existing content.
The loop must not become fix-only: a healthy wiki needs both, and lint noise is an
endless, self-replenishing well that will happily consume every iteration forever if you
let it. Deliberately balance the two — see step 0 below before picking.

### 0. Check the recent track balance

Read `.claude/wiki-improvement-backlog.md`'s last 3 **Fix/Build** entries under
`## Daily improvement loop` (skip Sync entries — they are driven by upstream releases, not
by a choice, so they neither satisfy nor create a balance debt) and classify each as Fix or
Build (a tag-audit/broken-link/schema-sync/dedup iteration is Fix; a new-page/stub-
expansion/section-deepening iteration is Build). **If 2 or more of the last 3 were Fix,
this iteration must be Build** — unless you find something urgent (e.g. a bug actively
corrupting data across hundreds of pages, on the order of the iter-3 lint.py parsing bug),
in which case do that fix but say explicitly in the log that Build is now overdue. Apply
the same logic in reverse if Build has dominated. Don't repeat the exact scope of the last
2-3 entries either way.

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

### Any track — final steps

1. Pick ONE area sized to roughly what a single sub-agent can do well in about an hour
   (comparable to a ~5-page batch in past campaigns — see the completed batches in
   `wiki-improvement-backlog.md` for calibration).
2. Write a short plan (2-5 sentences: what, why, expected file list, which track) before
   delegating.
3. "Nothing actionable" should be rare — if Fix comes back clean, that's exactly the
   signal to switch to Build (there is always a stub to expand or a gap to fill while any
   `stub`/`draft` pages or high-inbound forward links remain). Only stop without acting if
   you've genuinely checked all tracks and found nothing — say so explicitly and log it.

## 3. Delegate and verify

1. Delegate the actual editing to ONE sub-agent (`Agent` tool, run in the foreground since
   the next steps depend on its result) carrying: the plan, the relevant CLAUDE.md rules,
   and an explicit scope boundary — roughly 60 minutes of work, do not exceed this batch.
   Use a `general-purpose` agent by default. For a Sync batch, hand it the verbatim
   changelog entries plus the integration rules from step 1, and tell it explicitly to
   verify every endpoint path against https://cryptodataapi.com/api/docs before writing it.
2. When it reports back, verify the changes yourself: `git status --short`,
   `git diff --stat`, and spot-read 1-2 changed/created pages for frontmatter correctness,
   wikilink validity, and CLAUDE.md schema compliance (strategy pages need the full
   15-section structure; concept pages need `domain`/`prerequisites`/`difficulty`; etc.).
   On a Sync batch, additionally confirm each new/changed endpoint path really appears in
   the live docs — do not take the sub-agent's word for it. Fix small issues directly
   rather than re-delegating.

## 4. Record and ship

1. Append one entry to `.claude/wiki-improvement-backlog.md` under a
   `## Daily improvement loop` section (create it, once, if absent) — date, **track (Sync,
   Fix or Build)**, what was picked and why, what changed, before/after counts if relevant.
   State the track explicitly (e.g. "iter N (Build): ...") so the next iteration's step 2.0
   can classify it at a glance. For a Sync iteration, list the release versions absorbed
   and their dispositions. If nothing actionable was found in any track, log that instead
   of a change.
2. Update `wiki/log.md` per CLAUDE.md's Rules for the LLM if pages were created or
   substantively updated.
3. Confirm the changelog state file records every release you handled — the report is
   idempotent, so re-running `python tools/check_api_changelog.py` should now show only
   what you deliberately deferred. Commit
   `.claude/cryptodataapi-changelog-state.json` alongside the page edits so the watermark
   travels with the work it represents.
4. Update `CHANGELOG.md` at the repo root — newest entry first, dated, under
   Added/Changed/Fixed/Notes as applicable. Never write "CoinGecko" or "CoinMarketCap" —
   use neutral data-source phrasing instead.
5. If the change affects anything `README.md` describes (counts, features, setup steps,
   the MCP server, tooling, page counts, rate limits), update the relevant section in the
   same commit. If touching counts, true them all up against
   `find wiki -name '*.md' | wc -l` — counts only live in the README's intro line and the
   "What's inside" table, nowhere else.
6. Commit and push:
   - Check `git status --short` and stage the specific changed files (not a blind `-A`).
   - Write a concise, imperative commit message with no vendor names, ending with
     `Co-Authored-By: Claude <model running this iteration> <noreply@anthropic.com>`.
   - `git push`. If it fails (diverged/conflict/rejected), stop and report — do not
     force-push or reset.
7. Report a short summary: what was picked (including the track), what changed, and the
   resulting commit hash (or "nothing actionable" if no track had anything to do).

## Guardrails

- Check the API changelog every iteration (step 1) — a stale endpoint reference is a
  correctness bug, and the upstream feed only keeps 10 releases, so skipping checks loses
  history permanently.
- Never invent CryptoDataAPI endpoint paths, response fields, or tier limits — the
  changelog tells you *something* changed; https://cryptodataapi.com/api/docs is the only
  authority on what the shape now is.
- Balance Fix and Build (see step 2.0) — this loop exists to grow the wiki, not just keep
  lint's counters down. A streak of Fix-only iterations is a bug in how the loop is being
  run, not a sign the wiki is in great shape. Sync sits outside that balance.
- Bounded scope: one area per iteration, sized to ~60 minutes of sub-agent work — don't
  let it balloon into a multi-hour or dozens-of-files change. This applies to Sync too:
  defer surplus releases rather than growing the batch.
- ADD, never destroy: preserve existing hand-written content. Deleting/merging pages
  follows the same care as the completed A9 duplicate cleanup in
  `wiki-improvement-backlog.md` (audit first, merge unique content, then delete).
  Deprecated endpoints get marked, not deleted.
- Crypto/trading/macro/AI scope only (CLAUDE.md's Scope section) — no equity-specific
  content.
- Only approved tags (CLAUDE.md's Approved Tags list).
- Never commit `.env` or other secrets. The changelog feed needs no key — don't add one.
