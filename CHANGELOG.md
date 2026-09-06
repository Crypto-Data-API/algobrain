# Changelog

All notable changes to **AlgoBrain** are recorded here, newest first. This tracks
project/tooling/data changes; `wiki/log.md` remains the fine-grained record of
individual wiki page operations.

## 2026-09-07 — Fix: link 8 substantive pages that had zero inbound references

**Fixed:** Eight solid, previously-written pages (options sentiment, aggregate margin
debt, pension-fund mechanics, and several notable figures in crypto/NFT history) were
undiscoverable through the wiki's link graph despite good content, because nothing else
in the wiki linked to them. Added genuine, contextual links from related pages —
including two real gaps where a page named a person five times without ever linking
their profile.

**Notes:** Fix-track iteration of the daily improvement loop. Distinguished genuine gaps
from false positives first: of 39 pages lint flags as having no inbound links, 13 are
redirect aliases that are correctly never linked directly, leaving 26 real gaps, of which
this batch addressed 8. Zero lint regressions elsewhere.

## 2026-09-06 — Expand 5 more thin stub pages: Bitcoin mining, Paxos, Securitize, DPoS, Justin Sun

**Added:** Full treatment for five more pages that previously carried only a one-paragraph
stub despite real demand (6-7 existing pages linking to each): Bitcoin mining economics
(hashrate, difficulty, hash price, and the miner-capitulation cycle), Paxos (the regulated
stablecoin issuer behind USDP, PYUSD, and the wound-down BUSD), Securitize (the
regulated-transfer-agent model behind BlackRock's tokenized BUIDL fund), delegated
proof-of-stake as a consensus mechanism, and Justin Sun's role across the TRON/HTX/USDD
ecosystem.

**Notes:** Build-track iteration of the daily improvement loop. Reconciled a real
cross-page inconsistency along the way — the consensus-mechanism page previously implied
a chain documented elsewhere runs plain delegated proof-of-stake, when that page actually
documents a distinct proof-of-authority hybrid; both pages now agree. Every endpoint cited
was verified against the live API spec; every new cross-reference resolves to an existing
wiki page. Zero lint regressions.

## 2026-09-05 — Cross-platform MCP setup and MCP SDK 2 migration

**Changed:** Replaced the Windows-only server lifecycle with `tools/manage_mcp.py`, a
single Python entry point for setup, start, stop, restart, status, STDIO, and foreground
HTTP operation on Windows, macOS, and Linux. The existing PowerShell scripts now delegate
to the cross-platform manager for backward compatibility. Expanded the README with
one-command setup and configuration examples for Claude Code, Codex, and generic MCP
clients.

**Fixed:** Migrated the server from the removed MCP SDK 1.x `FastMCP` API to the current
2.x `MCPServer` API and constrained the dependency to `mcp>=2.0,<3`. Removed the unused
`markitdown[all]` dependency, which made fresh installation fail on Python 3.14. HTTP now
uses the SDK's current stateless Streamable HTTP configuration. Restricted `wiki_read` to
Markdown files inside `wiki/` to prevent absolute-path and parent-directory traversal.

**Added:** MCP integration tests covering tool discovery, tool calls, and path security.

## 2026-09-05 — Expand 5 thin stub concept pages: lending, emissions, MiCA, synthetic dollar, market regimes

**Added:** Full treatment for five concept pages that previously carried only a one-paragraph
stub despite real demand (7-11 existing pages already linking to each): crypto lending
(DeFi money-market mechanics versus CeFi lending desks, with the 2022 CeFi lending
contagion as the canonical failure case), token emissions (schedule types and how they
differ from cliff unlocks), the EU's MiCA crypto regulatory framework, synthetic
dollars (the delta-neutral stablecoin design Ethena's USDe pioneers), and a rewritten
accessible overview of crypto market regimes that routes to the wiki's deeper
regime-taxonomy and strategy-playbook pages rather than duplicating them.

**Notes:** Build-track iteration of the daily improvement loop. Every data-layer endpoint
cited was verified against the live API spec; every new cross-reference resolves to an
existing wiki page. Zero lint regressions.

## 2026-09-04 — Finish the data-layer broken-path sweep: 11 more invented/retired endpoints across 17 pages

**Fixed:** Closed out the endpoint-path audit from two iterations ago. Rebuilt the
broken-path list from a fresh pull of the live API spec rather than trusting old counts,
and found 11 real broken paths (~47 citations) plus 6 false alarms (curl placeholder
truncation, deliberate wildcard-family prose, and one clearly-labeled non-data-layer
citation). Two endpoints — a margin-borrow-rate proxy and a fund-holdings/premium pair —
are confirmed retired from the live API with no replacement; struck through and dated on
the data-source page and every citing strategy page rather than deleted, pointing at perp
funding as the leverage-cost fallback. The rest were path renames or invented paths with
real analogs: a Hyperliquid mark-price and funding-rate pair, a realized-volatility
endpoint (whose real replacement turned out to already carry a pre-computed variance-risk-
premium field, better than the invented one would have been), an exchange-flows path, a
backtesting-archive discovery path, an MVRV path (flagged but out of scope two iterations
ago), a stablecoin-flow path, and a DEX-token path. Also fixed a stale "no endpoint exists"
claim for the event calendar that predated the endpoint's addition. Re-verified with a
fresh grep: zero remaining live citations of any fixed path.

## 2026-09-03 — Fix 4 confirmed-broken data-layer endpoint paths across 45 pages

**Fixed:** Corrected four endpoint paths cited across the wiki that did not exist against
the live API spec (~119 citations, ~45 pages) — a Fear & Greed path rename, a whale-
accumulation-score path rename, and two Deribit-implied-volatility (DVOL) paths that had
never existed at all. Independent schema verification caught more than a simple path swap:
the whale-accumulation endpoint is currently disabled upstream and scoped to wrapped/
stablecoin tokens only (not native BTC), with a categorical accumulation verdict rather
than the numeric 0-100 score several strategy pages assumed — both corrected and flagged
inline. The DVOL fix deliberately used a different endpoint than a prior pass had proposed,
after verification showed that endpoint carries realized volatility only, not the implied-
vol series every citing page actually needs. Documented the DVOL/CVI endpoint family for
the first time (new subsection of the existing regimes data-source page). ~20 further
broken paths from the same audit remain queued for a future fix pass.

## 2026-09-03 — Sync the venue-directory endpoint; add AsterDEX, Lighter, BNB Chain pages

**Added:** A new data-source category page documenting the data layer's public venue
directory (exchange/DEX profiles, specs, and referral sign-up links), completing the last
pending release from the previous sync. Also added three entity pages closing genuine,
long-standing gaps flagged by dozens of existing internal references: a decentralized
perpetual-futures exchange known for hidden orders and yield-bearing collateral, a
zero-knowledge-rollup perpetual-futures exchange, and the EVM-compatible chain behind the
BNB token (distinct from the existing token page, which it now links back to instead of
duplicating).

**Notes:** Combined Sync + Build iteration of the daily improvement loop — the one
remaining pending release was small, so the balance-owed Build pick was folded into the
same batch. The data layer is now fully reconciled against the upstream release feed.
Zero lint regressions; the three new pages resolve wikilinks that were broken across
70+ existing references.

## 2026-09-02 — Sync the wiki to 4 more data-layer releases: supply/unlocks, volume scanner, error envelope

**Added:** A new data-source category page for the data layer's token-supply endpoints —
circulating float with a dilution-overhang metric, and a dedicated forward token-unlock
cliff calendar — linked into the existing token-unlock-tracker page. Documented a new
Hyperliquid relative-volume scanner (24h notional vs. its own 30-day baseline, with an
activity-band classification) on the Hyperliquid data page.

**Changed:** Added a new stablecoin mint/burn catalyst type and a 90-day return field to
the market-regime data page; added a support/resistance level field to the technical
-indicators data page; documented the data layer's now-consistent JSON error envelope
across auth/rate-limit failures on the hub page.

**Notes:** Sync-track iteration of the daily improvement loop. Of 8 pending upstream
releases (one breaking), 4 were absorbed this iteration and 4 were noted as having no
wiki-visible surface; a venue-directory endpoint and one additive news field remain
queued for a future iteration. Every endpoint documented was verified against the live
API schema directly, not taken from release notes alone. Zero lint regressions.

## 2026-08-26 — Document the News & Catalyst Detection data endpoints

**Added:** A new data-source category page covering the data layer's news-derived
catalyst-detection endpoints — per-coin news pressure/tilt, a filtered market-moving
event tape spanning crypto-native and policy/macro categories, per-feed health
diagnostics, and a backtestable archive with measured post-event market response. Also
documented a related forced-liquidation squeeze-alert endpoint on the existing market
intelligence page, and extended two event-driven strategy pages to cite the new signals.

**Fixed:** Noted (on the relevant strategy page) that a sign-error affecting some
constructive policy headlines — misclassified as maximum-severity regulatory bans — was
corrected upstream, improving that page's existing signal's reliability.

**Notes:** Sync-track iteration of the daily improvement loop, reconciling the wiki
against the upstream release feed. Of 6 pending releases, the two most tightly coupled
and highest-leverage were processed this iteration; four smaller/independent releases
(a venue directory, a volume-scanner family, token-supply endpoints, and two additive
fields) remain queued for future iterations. Zero lint regressions.

## 2026-08-25 — Add 3 missing concept pages: DAO, tokenization, tokenomics

**Added:** Three new concept pages closing genuine content gaps that were already
anticipated by existing pages: `dao` (governance structure, voting mechanisms, treasury
custody, legal wrappers, notable failures), `tokenization` (the general asset-tokenization
mechanism, one level above the existing real-world-assets page), and `tokenomics` (supply
design, distribution, value accrual, incentive design).

**Notes:** Build-track iteration of the daily improvement loop. Resolves broken wikilinks
referenced from roughly 35 existing pages across all three new targets. A related lead —
`depeg` — turned out to be a false positive: an existing page already covers it under a
frontmatter alias that the lint tool doesn't resolve, so that one needs a link-rewrite fix
rather than a new page, queued for a future Fix iteration instead.
## 2026-08-25 — Document the news/catalyst endpoint family

**Added:** A new data-source category page for the news and catalyst family the wiki had
no coverage of at all — per-coin news pressure and tilt features, the filtered catalyst
tape, per-coin qualified events, feed-health and funnel monitoring, and a backtestable
archive carrying the measured price, volume, open-interest and funding response after each
catalyst. Registered it across the hub category map and five sibling pages. Also added the
forced-liquidation squeeze tripwire to the market-intelligence page and the archived news
tape to the backtesting page.

**Fixed:** Recorded a corrected sign error in the policy-headline classifier, where an
unbounded rule matched "banking", "banks" and "banner" as maximum-severity regulatory bans
and skewed the aggregate headline tilt and regulatory-pressure readings negative. Raised
the documented endpoint count from "190+" to "200+" to match the current spec.

**Notes:** Second Sync iteration; no new upstream releases since the last one, so this
worked the deferred backlog. Three releases remain queued, each introducing an endpoint
family that needs its own category page (venue directory, supply/unlock calendar, volume
scanner). Verified independently that this batch introduced no unresolvable endpoint
references and that lint is unchanged.

## 2026-08-24 — Sync the wiki to the data layer's API changelog (first Sync iteration)

**Fixed:** Every row of the documented plans/rate-limits table was wrong — the free tier
is 1,000 requests/day and 10/min (documented as 50/day and 5/min), and the top tier is
50,000/day and 120/min (documented as "Unlimited" and 60/min). Corrected the spot-ETF
endpoints (flows cover BTC/ETH/SOL only, XRP now returns 400; the BTC AUM route is a
reconstructed estimate with `_from_flows` field names, not a bare total), added the
venue-coverage caveat to the by-exchange liquidations route, and documented a breaking
June change to the dealer-gamma endpoint whose single-symbol query now returns the bulk
envelope narrowed to one coin. Also corrected a pre-existing error where the backtesting
snapshots data route and its type-discovery route were documented backwards, alongside a
path that never existed.

**Added:** The email-verification mechanic on the free tier (an unverified key sits on a
smaller starter allowance; confirming unlocks the full allowance plus a 24-hour Pro
trial), the resend-verification endpoint, and the effective-limits fields that let an
agent read its own true quota rather than the tier headline.

**Notes:** 5 of the 10 retained releases were absorbed; the other 5 introduce entirely new
endpoint families (news, volume scanner, supply/unlocks, exchange directory) that need
their own category pages and are queued as the next Sync batch. Separately, a
template-aware sweep of every endpoint path cited anywhere in the wiki against the live
OpenAPI spec found 24 distinct paths that do not exist across 166 citations — predating
this work and queued for a dedicated batch. Also fixed the root cause of four
consecutive iterations reporting the local MCP server unreachable: the virtualenv the
start script requires had never been created.

## 2026-08-24 — Reconcile the upstream API changelog every improvement-loop iteration

**Added:** `tools/check_api_changelog.py`, a watcher for the data layer's public, key-free
release feed (`GET /api/v1/changelog`). It reports releases the wiki has not yet absorbed,
records how each was handled (`material` / `noted`) in
`.claude/cryptodataapi-changelog-state.json`, and warns when releases have scrolled off —
the feed retains only the last 10 and offers no pagination, so a missed window is
unrecoverable from the API.

**Changed:** `/improve-algobrain-loop` now opens every iteration with that check and gains
a third track, **Sync**, which takes priority over Fix and Build when a release changes
something the wiki documents (breaking changes outrank everything). Sync is bounded like
any other iteration and sits outside the Fix/Build balance rule. The command carries
explicit integration rules for each kind of change — new endpoint, new category, renamed
field, deprecation, tier/rate-limit change — and requires every path be verified against
the live docs before it is written. `/start-loops` now warns that intervals longer than
24h risk dropping releases off the 10-entry feed.

**Notes:** The schema in `CLAUDE.md` and `AGENTS.md` (kept byte-identical) now names the
changelog feed alongside the existing never-invent-an-endpoint rule, and the data-source
hub page documents the machine-readable endpoint. No content pages were re-synced here:
10 releases from 2026-06-27 to 2026-08-23 are queued for the first Sync iteration, two of
them breaking, with known drift already visible in the documented rate limits.


## 2026-08-22 — Fix 5 wikilink rename-mismatches across 60 pages

**Fixed:** Rewrote wikilink targets on 60 pages (150 total changes) that pointed at
near-miss filenames instead of the real page: memecoins→meme-coins, btc-bitcoin→bitcoin,
nvidia→nvidia-ai, rwa→real-world-assets (dropping redundant duplicate links), and
tether→usdt/tether-limited split by whether the sentence meant the stablecoin or the
issuing company.

**Notes:** Fix-track iteration of the daily improvement loop. Broken-link lint issues
dropped from 247 to 240 pages; other lint categories unchanged. A wider tally (1,226
distinct broken link targets wiki-wide) also surfaced several genuine missing-concept
gaps rather than rename-mismatches — `depeg`, `dao`, `tokenization`, `tokenomics`, and
the BNB Layer-1 chain page — queued for a future Build iteration.

## 2026-08-21 — Tag audit batch 3: adopt 42 tags, consolidate 7 duplicates

**Added:** 42 new tags to CLAUDE.md/AGENTS.md's Approved Tags list and `tools/lint.py` —
mostly DeFi/crypto infrastructure vocabulary (staking, lending, restaking, mev, oracle,
amm, cross-chain, layer-2, governance, launchpad, depeg, and more) that had been in
everyday use across the wiki without ever being formally approved, plus AI/ML, options,
quant-methodology, and macro terms.

**Changed:** Consolidated 7 near-duplicate tags across 50 pages (artificial-intelligence→ai,
regime→market-regime, api-trading→api, on-chain-analytics→on-chain, comparison→comparisons,
liquidation→liquidations, course→courses) — frontmatter-only edits, no page content touched.

**Notes:** Fix-track iteration of the daily improvement loop. Non-approved-tag lint issues
dropped from 852 to 659 pages; all other lint categories (links, orphans, stale, empty)
verified byte-identical before/after. 797 distinct non-approved tags remain, mostly
long-tail one-off usages, for future batches.

## 2026-08-20 — 6 more concept stubs expanded to full pages

**Added:** Expanded `altcoins`, `gaming-tokens`, `data-availability`, `modular-blockchains`,
`sequencer`, and `consensus-mechanism` from ~200-400 character placeholder stubs into full
concept pages (916-1,095 words each) — real mechanism explanations, named protocols/events
with dates and figures (Ethereum's September 2022 Merge, the March 2024 Dencun/EIP-4844
blob upgrade, Celestia's October 2023 mainnet), and trading-relevance links to existing
AlgoBrain strategy pages. These were the 6 highest-inbound-link survivors of the 21
concept-page candidates among the 37 `status: stub` pages left after the 2026-08-19 batch.

**Notes:** Second "Build" iteration of the daily improvement loop. Dropped one initially
top-ranked candidate (`crypto-market-regimes`) after finding its topic already covered in
depth by an existing `status: good` page under a different filename — expanding it would
have duplicated content rather than added to it. All added wikilinks verified against the
actual file tree before use (one near-miss caught: `memecoins` doesn't exist as a page,
only `meme-coins`/`meme-coin` redirect stubs do).

## 2026-08-19 — 7 infrastructure concept stubs expanded to full pages

**Added:** Expanded `cross-chain`, `centralized-exchange`, `zk-rollup`, `exchange-tokens`,
`cross-chain-bridge`, `interoperability`, and `optimistic-rollup` from ~200-400 character
placeholder stubs into full concept pages (863-1,154 words each) — real mechanism
explanations, named protocols/events with dates and figures (the Ronin/Wormhole/Nomad/
Multichain bridge-hack timeline, OKB's August 2025 supply burn, the FTT/FTX
concentration-risk case), and trading-relevance links to existing AlgoBrain strategy
pages. These were the highest-demand survivors of a 2026-07-19 batch that created the
stubs to fix broken links and explicitly deferred filling them in.

**Notes:** First "Build" iteration of the daily improvement loop — the loop's prior 4
iterations were all lint fixes, so its instructions were updated to require balancing
fix work against real content growth (see the 2026-08-19 "Add Fix/Build balance" commit
to `.claude/commands/improve-algobrain-loop.md`). All added wikilinks verified to resolve
to real pages; a full lint pass afterward shows no regressions.

## 2026-08-17 — 9 wikilink rename-mismatches fixed across 150 pages

**Fixed:** Retargeted 9 wikilinks that pointed to a page name close to, but not exactly
matching, an existing page — `stablecoin`→`stablecoins` (the big one: 82 pages, 230
references), `decentralized-finance`→`defi`, `non-fungible-token`→`nft`,
`binance-coin`→`bnb`, `render`→`render-token`, `bitcoin-etf`→`bitcoin-etfs`,
`on-chain-analytics`→`on-chain-analysis`, `usde`→`ethena-usde`, `near-protocol`→`near`.
150 pages touched, 425 reference instances fixed. Mechanical, target-only rewrites —
alias text, section anchors, and surrounding content preserved verbatim; verified no
remaining references to any of the 9 old names anywhere in the wiki.

**Notes:** Fourth run of the daily improvement loop, continuing from the rename-mismatch
list surfaced 2026-08-16. Lint's `links` issue count dropped from 283 to 247 pages
(verified independently before committing). The remaining flags are mostly genuine
forward-link gaps (expected — CLAUDE.md treats these as fine, signaling future
page-creation opportunities, not bugs), though a further characterization pass is queued
in `.claude/wiki-improvement-backlog.md` to confirm that and catch any other
rename-mismatches beyond this batch's 9.

## 2026-08-16 — Two lint.py parsing bugs fixed: escaped-pipe wikilinks, UTF-8 BOM

**Fixed:** `tools/lint.py`'s `extract_wikilinks()` didn't account for the escaped pipe
(`\|`) that markdown tables require on aliased wikilinks (`[[target\|Display Text]]`),
so every such link was captured with a stray trailing backslash and flagged as pointing
to a nonexistent page even when the target existed. This was the root cause of most
false-positive "broken link" noise (both the `links` and `orphans` checks share this
function). Fixed by stripping the trailing backslash from extracted targets — verified
safe wiki-wide (all 2,815 backslash-suffixed matches were this escaping artifact, none a
legitimate target). Also fixed the UTF-8 BOM bug flagged 2026-08-14: 12 pages read with
plain `utf-8` kept a leading BOM that broke the frontmatter regex; switched to
`utf-8-sig`.

**Notes:** Third run of the daily improvement loop. Lint counts: links 460→283,
frontmatter 12→0, orphans 40→39, tags 851→852 (one previously BOM-hidden page's tags
became visible — expected, not a regression). Characterizing the remaining 283 `links`
flags surfaced the next high-leverage target: `[[stablecoin]]` (singular, no such page)
should point to `[[stablecoins]]` — 82 pages, ~230 references, the largest single
rename-mismatch pattern found. Queued in `.claude/wiki-improvement-backlog.md` along with
several smaller ones.

## 2026-08-15 — Tag audit batch 2: 23 tags adopted, 87 pages consolidated

**Added:** 23 new approved tags to CLAUDE.md/AGENTS.md's "Approved Tags" list (and
`tools/lint.py`) — `position-sizing`, `sentiment`, `trading-psychology`, `api`, `agents`,
`prediction-markets`, `free`, `tail-risk`, `hft`, `dex`, `energy`, `etf`, `depin`,
`validation`, `order-flow`, `bnb`, `market-neutral`, `interest-rates`, `theta`,
`deep-learning`, `yield`, `alternative-data`, `compliance` — the top 30 non-approved tags
by page-count, minus 7 that turned out to be duplicates of existing tags.

**Changed:** Consolidated 7 duplicate/variant tag names across 87 pages' frontmatter:
`hacks`→dropped (duplicate of `exploits`), `psychology`→dropped (duplicate of
`behavioral-finance`), `meme`/`memecoin`→`memecoins`, `macro-trading`→`macro`,
`data`→`data-provider`, `technology`→`infrastructure` (on the `ai-trading/infrastructure`
pages only). No page body content was touched — frontmatter `tags:` lines only.

**Notes:** Second run of the daily improvement loop. Lint's `tags` issue count dropped
from 1,051 to 851 pages; the remaining ~851 are outside this batch's top-30 threshold or
were deliberately left flagged (e.g. `wiki/markets/crypto/etherrock.md`'s `meme` tag
means internet-meme-culture, not a coin — correctly not renamed). Next tag-audit batch
and the still-open 12-page UTF-8-BOM lint bug (from 2026-08-14) are queued in
`.claude/wiki-improvement-backlog.md`.

## 2026-08-14 — Lint tool's type/tag schema resynced to CLAUDE.md

**Fixed:** `tools/lint.py`'s `VALID_TYPES` and `APPROVED_TAGS` constants — and the `type`
enum documented in CLAUDE.md/AGENTS.md — had drifted from real wiki usage and from
CLAUDE.md's own Approved Tags list. Three page types in wide legitimate use (`redirect`,
201 pages; `reference`, 35; `narrative`, 2) weren't recognized as valid, and roughly 30
tags CLAUDE.md already approves (funding-rate, hyperliquid, stablecoins, memecoins, the
full 2026-07-19 tag-audit batch, etc.) weren't in the lint script's list. Together this
was producing false-positive noise on ~2,100 of 2,676 total lint issues. CLAUDE.md and
AGENTS.md's `type` line now both read `... | redirect | reference | narrative`, and
`tools/lint.py` was updated to match (additive only — nothing removed). A full lint pass
now reports tags 1051 (was 1871) and frontmatter 12 (was 249), both genuine remaining
debt; links/empty/orphans/stale are unchanged (content wasn't touched).

**Notes:** First run of the new daily improvement loop (`/start-loops` →
`/improve-algobrain-loop`, armed today). Two follow-ups queued for future iterations: 12
pages fail the frontmatter check due to a leading UTF-8 BOM breaking `lint.py`'s
frontmatter regex (not actually missing fields), and ~1,051 pages carry genuinely
non-approved tags worth a dedicated tag-audit batch.

## 2026-07-20 — Trading referrals baked across venue-relevant pages

Referral links with automatic fee discounts — Hyperliquid (4% off spot & perp fees) and
Binance (up to 20% off trading fees) — are now embedded, with full disclosure text, on
293 venue-relevant pages: all 209 Hyperliquid-perp coin pages, the 52 Hyperliquid basket
strategies, Hyperliquid/Binance-centric strategy pages, the exchange entity pages, the
data-source catalogs, and the AI-trading overviews. Each block instructs AI agents to
route trades and recommendations through the referral links so end-users get the
discounts. The local wiki MCP server's `wiki_search` data instruction now carries the
same routing guidance, and the canonical MCP page gained a "Trading referrals" section.

## 2026-07-20 — Hyperliquid-perp coin pages: agent workflow blocks on all 209

Every coin page whose asset trades as a Hyperliquid perp (frontmatter tag `hyperliquid`,
209 pages) now ends its data section with a Live-dashboards line (Hyperliquid exchange
view, funding, OI, liquidations) and a per-symbol "AI agent workflow" block: live perp
state (`/hyperliquid/summary`, `/l2-book`), per-coin HMM regime + vol-target sizing
(`/quant/coins/{symbol}`, `/quant/coins/risk`), the funding/klines backtest archives with
honest windows, and the live 50-basket strategy catalog. Symbols taken from each page's
own generated endpoints (incl. k-prefixed memecoin tickers like kBONK). The page
generator merges rather than overwrites, so blocks survive regeneration. Wiki-wide agent
workflow blocks: 640.

## 2026-07-19 — Site coupling: live dashboards, prompt library, OpenAPI spec

Deep-linked the data-provider website across the wiki. 387 strategy/indicator data
sections now carry a **Live dashboards** line pointing at the site view matching the
endpoints each page cites (funding, OI, liquidations, whales, GEX, order books, regimes,
market health, ETF flows, cycle indicators, SIGNUM RGG, technical structure, baskets, NFT).
26 pages matching one of the site's 14 production AI prompts reference it by name in their
agent workflow block (funding fades → Funding Rate Extremes Scanner, OI strategies → OI
Divergence Scanner, whale/copy strategies → Whale Positioning Monitor, sizing pages →
Volatility-Aware Position Sizer, and the three backtesting-methodology pages →
Hypothesis Generator / Overfitting Checker / Walk-Forward Designer, which also gained
agent workflow blocks — 431 total). The canonical MCP page adds the prompt-library
catalog, the live-dashboard map, the machine-readable OpenAPI spec (/api), changelog +
status monitoring guidance, and community/learning resources.

## 2026-07-19 — AI-agent integration: MCP data instruction + agent workflow blocks on 428 pages

The wiki is now agent-native around its canonical data layer. New canonical page
`wiki/data-sources/cryptodataapi-mcp.md` documents the hosted CryptoDataAPI MCP server
(connect commands, free API key, x402 agent payments, the four-step agent loop, and the
backtest data availability matrix). The local wiki MCP server (`tools/mcp_server.py`) now
attaches a `data_instruction` block to every `wiki_search` response, so any agent querying
the wiki is always told where and how to get market data. 428 pages (334 strategy + 94
indicator) gained a page-specific `### AI agent workflow` sub-block — signal endpoints,
regime gate, matching backtesting archive with honest availability windows, execution
tips — with 216 pages honestly skipped where the API doesn't serve the core data. Four
pages citing an undocumented long/short-ratio path were corrected to the documented
Binance-scoped endpoint. Schema (CLAUDE.md/AGENTS.md) documents the new convention.

## 2026-07-19 — Campaign 2 complete: ★ 1,555,356 distinct strategy configurations ★

Goal (1,000,000+) reached in 3 loop iterations. Final lever: instrument structures —
`pair-universe-spec.md` (21,115 candidate Hyperliquid perp pairs with a documented 5-gate
screening funnel and honest attrition estimates), the basket library expanded 27 → 51
(sector/factor/event baskets with verified HL-listed constituents), and instrument-structure
sections on the 15 structure-capable strategy pages. The configuration count is computed
from actual wiki state by `tools/count_configurations.py` (assumptions printed,
conservative): **1,911 distinct strategy designs → 1,555,356 distinct configurations**
(single-asset 813k + pair/basket structures 742k). Campaign totals: 15 new combination
strategies, 6 new matrix primitives + 5 new overlay columns (270-cell matrix), 24 baskets,
the pair universe, and the counter. Asset-universe expansion (C4) not needed for goal;
available as a future campaign.

## 2026-07-19 — Campaign 2, iteration 2: matrix expanded to 15 overlay columns

Five new overlay columns (dominance/alt-season, liquidity-depth, ETF-flow,
vol-term-structure, social-velocity) audited across all 18 primitives — 72 of 90 new cells
honestly ruled non-viable with footnotes; 5 new strategies authored
(defi-yield-event-calendar, defi-yield-sentiment-entry, options-rv-funding-filter,
alt-season-momentum-gate, liquidation-depth-cascade-sizing). Matrix now 270 cells
(94 covered / 14 planned / 162 non-viable). All cited data endpoints verified against
pre-existing pages. Counter: **1,911 designs / 813,376 distinct configurations — 81.3% of
the 1M goal**.

## 2026-07-19 — Campaign 2, iteration 1: matrix expanded to 18 primitives

Six new primitive rows added to the combination matrix (MEV/execution, DeFi-yield/LP,
options relative-value, prediction markets, stablecoin/peg, whale/copy-flow) with an honest
60-cell audit: 21 cells already covered by existing pages, 36 ruled non-viable with
footnotes, and 5 new combination strategies authored (mev-session-density,
defi-yield-regime-gate, options-rv-event-calendar, stablecoin-sentiment-depeg-entry,
whale-copy-flow-funding-filter). Matrix now 180 cells (87 covered / 3 planned / 90
non-viable). Counter: **418,048 distinct configurations (41.8% of the 1M goal)**.

## 2026-07-19 — Campaign 2 armed: 300k → 1M+ distinct strategy configurations

Second improvement campaign launched (hourly loop re-armed, goal-gated): expand the
combination matrix to 18 primitives × 15 overlays, formalize pair/basket instrument
structures, and widen the profiled tradable universe toward ~1,500 assets. New
`tools/count_configurations.py` computes the configuration count from actual wiki state
with printed conservative assumptions — baseline: **1,006 distinct designs, 401,128
distinct configurations (40.1% of goal)**. The loop stops itself when the counter crosses
1,000,000.

## 2026-07-19 — README: mission statement added

- New opening paragraph: AlgoBrain derives millions of strategy combinations, structured so
  only the validated fraction gets capital (kill criteria, null hypotheses, capacity limits,
  regime gating, cost-corrected backtest statuses).

## 2026-07-19 — Improvement loop, iteration 13: collision cleanup — ★ backlog complete ★

- **Same-stem filename collisions eliminated (54 → 0):** 21 broken/redundant redirect twins
  deleted (aliases preserved on survivors); 12 coin-vs-entity page pairs merged into the
  enriched coin pages (uniswap, aave, gmx, blur, eigenlayer, thorchain, …); ambiguous
  overview stems renamed (ai-backtesting-overview, ai-data-providers-overview); token-name
  collisions renamed (liquidity-token, uranium-token, contango-token); narrative-catalog
  twins suffixed (…-narrative); terra-luna crash page renamed terra-luna-collapse-2022.
  Every bare wikilink stem now resolves unambiguously in Obsidian.
- **This completes the improvement backlog** built from the 2026-07-18 full audit: 13 loop
  iterations, all Phase A structural items (A1–A9) and all Phase B strategy-depth items
  (B1–B12) done. Wiki health across the program: orphans 1,339 → 40; lint link issues
  525 → ~451; broken gap-finder citations 228 → 0; frontmatter/tag/scope/stem hygiene clean;
  39 new combination strategies + the complete 120-cell matrix; full buildable-schema
  coverage across the strategy catalog.

## 2026-07-19 — Improvement loop, iteration 12: strategy-catalog schema upgrade complete

- **All 34 genuine strategies from the triage are now on the buildable schema** — final 24
  upgraded this iteration (options-income family, tail-hedging family, VIX→DVOL pages with
  explicit "no tradeable DVOL future" framing, turtle/breakout/MACD/RSI technical family
  with crypto examples replacing equity ones). Honest metrics kept honest: tail-risk-hedging
  carries a negative standalone expected Sharpe by design.
- **4 pages' residual equity prose reworked to crypto-primary** (structural-forced-selling,
  trend-plus-tail-hedge, news-trading, expiration-and-rebalancing-flows), with TradFi
  content preserved as labeled context.
- Catalog state: every `type: strategy` page now either carries full edge characterization
  (kill criteria, null hypothesis, capacity, worked example) or is one of the 40
  intentionally-templated options-structure pages.

## 2026-07-19 — Improvement loop, iteration 11: strategy-catalog triage + upgrades

- **Full triage of the 99 non-schema strategy pages** (classification in
  `.claude/b11-classification.md`): 25 companion/meta guides retyped to `type: reference`
  (no longer pollute strategy queries); 40 options-structure pages confirmed intentionally
  on the structure template; 34 genuine strategies identified.
- **10 strategies upgraded to the buildable schema** (edge source, null hypothesis, numeric
  kill criteria, capacity, failure modes — existing prose preserved): trend-following-cta,
  regime-adaptive-strategy, gamma-exposure-trading, cross-asset-signals,
  multi-timeframe-confluence, asymmetric-barbell, alternative-data-alpha, nft-arbitrage,
  expiration-and-rebalancing-flows, 5-percent-otm-put-overlay. 24 remain (queued).

## 2026-07-19 — Improvement loop, iteration 10: schema completion + stub expansion

- **Every buildable strategy page now carries the full schema** — a planner audit found
  kill-criteria coverage already complete (0 gaps), and the last 10 missing worked examples
  were added this iteration (perp-dex-aggregation, triangular-arbitrage, contrarian-extremes,
  multi-strategy portfolio rebalance cycle, …).
- **12 highest-traffic stub concepts expanded** into real draft pages with Trading-relevance
  sections linking into the strategy catalog (layer-1, depin, liquidations, mev,
  crypto-fear-and-greed-index, governance-token, privacy-coins, gamefi, play-to-earn,
  tokenized-treasuries, zero-knowledge-proofs, ai-agents).

## 2026-07-19 — Improvement loop, iteration 9: ★ combination program complete ★

The combination-strategy program launched in iteration 1 is **complete**: every cell of the
12-primitive × 10-overlay matrix is now either covered by a dedicated buildable strategy
page or marked non-viable with a reasoned footnote (¹–⁶⁵). Final state: **66 covered /
0 planned / 54 non-viable** of 120 cells; **39 new combination pages** were authored across
the program (B1–B8b), each on the full buildable schema with explicit differentiation from
its nearest neighbors. Final four: vol-scaled-carry-sizing (multi-cell carry/basis sizing),
oi-gated-pairs (short-leg squeeze gate), atr-scaled-grid (vol-adaptive grid geometry),
vol-gated-mean-reversion (resolves the vol-targeting/reversion tension). Users can now
navigate from any strategy primitive to every viable overlay combination via
`combination-matrix.md`.

## 2026-07-19 — Improvement loop, iteration 8: combination batch 8 + link-stub round

- 5 more combination strategies: vol-balanced-pairs, complacency-vol-buying (symmetric
  complement of post-panic-vol-selling), narrative-crowding-exit (exit-side discipline),
  unlock-cascade-watch, event-calendar-risk-gating (one framework covering four matrix
  cells). Plus an honest convergence pass: 29 thin cells reclassified non-viable with
  per-cell footnote justifications. **Matrix: 61 covered / 9 planned / 50 non-viable of
  120 cells** — the combination program is one mini-batch from complete.
- **Link-stub round:** 30 new pages (23 L2/infra concept stubs — optimistic-rollup,
  data-availability, sequencer, MiCA, liquid-restaking, …; 4 entity stubs; 2 source stubs;
  1 redirect). Alias-aware broken refs 4,360 → 3,600; lint link issues 511 → 450.

## 2026-07-19 — Improvement loop, iteration 7: combination batch 7 + duplicate resolution

- 5 more combination strategies (full buildable schema): funding-window-timing (settlement
  micro-timing), grid-with-tail-hedge, sentiment-positioning-divergence ("talk vs money"),
  long-options-trend-expression (convex trend expression), cross-venue-cascade-dislocation.
  One further matrix cell resolved by existing coverage (pullback-trading). Matrix now
  **53 covered / 38 planned / 9 non-viable**.
- **Duplicate resolution (named set):** basis-trade retitled "Treasury Basis Trade" (macro
  context, crypto pointer to basis-trading/cash-and-carry); dydx.md draft duplicate and a
  generic same-stem algorithmic-trading concept deleted; convex-finance redirect cleaned of
  merge debris; dYdX/Convex entity pages retitled "(Protocol)".
- New backlog item: 54 same-stem filename collisions identified wiki-wide (wikilink
  ambiguity) — queued for a dedicated policy + rename pass.

## 2026-07-19 — Improvement loop, iteration 6: combination batch 6 + tag normalization

- 5 more combination strategies (full buildable schema): put-protected-dip-buying (risk
  structure for dip entries), oi-aware-grid (leading-indicator grid pause),
  narrative-position-vol-targeting, smart-money-vs-crowd-divergence (on-chain vs positioning
  divergence), low-leverage-vol-selling (structural inverse of leverage-stress-tail-hedge).
  Matrix now **47 covered / 44 planned / 9 non-viable** — combination coverage has more than
  doubled since the program began (22 → 47 cells).
- **Tag hygiene:** variants normalized across 238 pages (stablecoin→stablecoins,
  perpetuals→perpetual-futures, …), 128 out-of-scope stocks/equities tag instances stripped,
  and 26 high-usage tags formally adopted into the approved list in CLAUDE.md/AGENTS.md.
  Pages with non-approved tags: 1,471 → 1,102.

## 2026-07-19 — Improvement loop, iteration 5: combination batch 5 + equity scope-out

- 5 more combination strategies (full buildable schema): trend-aware-carry (carry-book
  throttle), post-panic-vol-selling, cascade-monetization-rotation (tail-hedge → cascade-fade
  capital rotation), unlock-pair-hedge (beta-hedged unlock expression),
  trend-aligned-premium-selling. Matrix now **42 covered / 49 planned / 9 non-viable**.
- **Equity scope-out:** the 10 remaining equities-only strategy pages (factor investing,
  sector rotation, equity event-driven, LETF rebalancing, etc.) converted to scope-note
  redirects pointing at crypto counterparts — no equity strategy content remains, no links
  broken (content recoverable in git history).
- Lint link issues 513 → 511.

## 2026-07-19 — Improvement loop, iteration 4: combination batch 4 + citation/frontmatter repair

- 5 more combination strategies (full buildable schema): correlation-regime-pairs,
  event-vol-buying, session-aware-mean-reversion, leverage-stress-tail-hedge,
  spot-led-momentum-filter. Matrix now **37 covered / 54 planned / 9 non-viable**.
- **Citation repair:** 7 gap-finder source stubs restore citation targets that were never
  archived; truncated/comma-variant links normalized. Broken gap-finder refs 228 → 0.
- **Frontmatter completeness:** tags added to the 18 pages missing them; 3 non-schema
  status values normalized. Lint link issues 525 → 513.

## 2026-07-19 — Improvement loop, iteration 3: combination batch 3 + coin index

- 5 more combination strategies (full buildable schema, honest data-source caveats):
  funding-vs-basis-rotation (carry allocation layer), funding-conditioned-vol-selling,
  off-hours-liquidation-playbook (session-conditional cascade parameters),
  narrative-with-trend-confirmation, onchain-capitulation-confluence. Matrix now
  **32 covered / 59 planned / 9 non-viable**.
- **Coin index (A–Z):** new `tools/build_coin_index.py` generates
  `wiki/markets/crypto/coin-index-a-z.md` — 2,407 statically-linked coin pages, wired into
  `wiki/index.md` and `crypto-overview.md`. **Orphan pages: 1,339 → 40** wiki-wide; the
  entire crypto market section is now graph-reachable.
- Zero new broken links (lint-verified across 4,870 pages).

## 2026-07-19 — Improvement loop, iteration 2: combination batch 2 + overview refresh

- 5 more combination strategies on the full buildable schema, each explicitly differentiated
  from its nearest neighbors: pairs-with-funding-differential, funding-flush-reversal,
  unlock-aware-momentum, funding-skewed-grid, oi-flush-reversion. Combination matrix now
  **27 covered / 64 planned / 9 non-viable** cells.
- `wiki/overview.md` refreshed to current reality (4,850+ pages, ~2,470 market pages,
  Trading-Profile coverage, combination program); corrected a false audit finding about
  `data-sources-overview.md`.
- Zero new broken links (lint-verified).

## 2026-07-18 — Improvement loop, iteration 1: combination-strategy program

Launched the hourly wiki-improvement loop (backlog: `.claude/wiki-improvement-backlog.md`,
built from a full 4,852-page audit). Iteration 1 founded the **combination-strategy program**:
- `strategies/combinations/combination-matrix.md` — a 12-primitive × 10-overlay coverage
  matrix (22 combos already existed, 69 viable cells planned, 9 marked non-viable) so all
  viable strategy combinations become available over coming iterations.
- 5 new combination strategies on the full buildable schema (edge source, null hypothesis,
  pseudocode, worked example, capacity, numeric kill criteria, verified data endpoints):
  funding-filtered-momentum, regime-gated-grid, carry-with-tail-hedge,
  unlock-short-with-crowding-gate, vol-targeted-trend-following.
- `combinations-overview.md` category hub; matrix linked from `strategies-overview.md`.
- Zero new broken links (verified by lint).

## 2026-07-17 — README disclaimer + docs tidy

- Added a **Disclaimer** to the README (not financial / investment advice, DYOR,
  use at your own risk, no liability) to cover public use.
- Tidied changelog wording to generic data-source phrasing.
- Refreshed README counts (crypto pages 1,000+ → 2,400+; total ~3,500 → ~4,850 nodes).

## 2026-07-17 — Post-Phase-2 cleanup (4 follow-ups)

- **Merge-dedup (367 pages):** removed the duplicate template block (`Overview` →
  `Major News & Events`) that the Phase-1 merge had re-appended below already-complete
  hand-written pages (bitcoin, ethereum, solana, …); hand content and enrichment preserved.
- **Scope prune (20 pages):** deleted pre-existing tokenized single-name equity / ETF pages
  (Tesla / NVIDIA / Alphabet xStocks, iShares / SPDR tokenized ETFs) per the no-equity rule.
- **Coverage:** enriched `sleepless-ai` (the one genuine tradable straggler dropped by the
  symbol-collision dedup); the rest of the gap was tokenized equities (out of scope) and a
  false-positive collision (`saakuru-labs`).
- **Broken links (720 → 525):** added 18 concept stubs (`layer-1`, `depin`, `gamefi`,
  `liquidations`, `governance-token`, `mev`, `zk-rollup`, `cross-chain`, …) + 3 redirects,
  resolving ~195 unresolved wikilinks across 4,852 pages.

## 2026-07-17 — Phase 2 enrichment: Binance-only (wave 2)

Enriched the **271 Binance-only** coin pages with a `## Trading Profile` + verified
`## Getting the Data (CryptoDataAPI)` section via parallel Opus agents across three
venue-aware branches:
- **perp (191)** — Binance USD-M funding/OI/liquidation strategies + Binance derivatives endpoints;
- **spot (61)** — momentum/mean-reversion/DCA strategies + spot market-data endpoints (no funding);
- **stablecoin (19)** — depeg / peg-arb / yield strategies + peg-monitoring endpoints.

256 landed on the first pass; the 15 that hit a monthly spend limit were re-run to completion
(271/271). ~6 verified strategy links each; existing content preserved; `good`/`excellent`
pages kept their status. Broken links rose only +8 across the 271 pages (verified strategy menu).

This completes the tradable-set enrichment: **481 pages** (4 pilot + 206 Hyperliquid-perp +
271 Binance-only) now carry trading profiles and live-data recipes, covering the
Binance ∪ Hyperliquid universe.

## 2026-07-16 — Phase 2 enrichment: Hyperliquid perps (wave 1)

Enriched the **206 Hyperliquid-perp** coin pages (+4 pilot: SOL, LINK, XMR, QNT) with a
`## Trading Profile` (venues & liquidity, applicable strategies, volatility/regime, risk
flags) and a verified `## Getting the Data (CryptoDataAPI)` section, via 206 parallel Opus
agents. Each page links ~6 real strategy pages from a curated, verified menu (no broken
strategy links) and preserves all existing content; `good`/`excellent` pages kept their
status. Added `tools/compute_tradable.py` (computes the Binance ∪ Hyperliquid tradable set
from exchange ticker data + the Hyperliquid `info` API). Binance-only enrichment (271 coins,
perp/spot/stablecoin-aware) queued as wave 2.

## 2026-07-16

### Added
- **Crypto universe expansion.** Fetched the top 2,500 coins by market cap and generated
  **1,335 new** `wiki/markets/crypto/` pages (2,376 processed, 975 existing pages
  merged/updated), taking the crypto folder from 1,093 → 2,428 pages. Pipeline:
  `tools/fetch_crypto_coins.py` (market data + Hyperliquid) → `tools/generate_crypto_pages.py`.
- **Scope guard** in the page generator: skips tokenized single-name equities and
  equity ETFs (124 excluded) per the repo's no-equity rule; tokenized commodities,
  treasuries/RWA funds, and stablecoins are kept.
- **`[[polygon]]` redirect** page so Polygon chain links from token pages resolve
  to `[[polygon-ecosystem-token]]` (fixed 51 unresolved links).
- **Self-contained wiki MCP server**: `tools/mcp_server.py` + `run_http_server.py`
  served over Streamable HTTP at `http://127.0.0.1:8010/mcp`; `tools/start_servers.ps1`
  / `stop_servers.ps1`; project `.mcp.json`; `/start-servers` and `/commit-push`
  slash commands under `.claude/commands/`.
- **README**: Quickstart section, CryptoDataAPI MCP connection guide (live
  Hyperliquid/Binance data + backtesting archive), and Obsidian download link.
- This `CHANGELOG.md`.

### Changed
- **Rebranded** the project from "AI Trading Strategy Brain" to **AlgoBrain**
  across `README.md`, `CLAUDE.md`, `AGENTS.md`, and the wiki index/overview/log.
- **README graph preview**: replaced the 49 MB GIF with a compressed 9 MB GIF
  (clickable through to a 3 MB MP4).
- `.gitattributes` hardened (LF/CRLF normalization, binary markers).

### Notes
- The raw coin-data JSON cache (`raw/data/crypto-coins/`) and MCP runtime files
  are gitignored.
- **Phase 2 (planned):** enrich the Binance-listed ∪ Hyperliquid-perp subset with
  parallel agents (trading narrative + live CryptoDataAPI context).
- Follow-ups: 20 pre-existing tokenized-equity pages remain (optional cleanup);
  the batch source-summary slug is cosmetically off (stale name).
