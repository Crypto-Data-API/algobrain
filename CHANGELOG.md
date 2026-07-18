# Changelog

All notable changes to **AlgoBrain** are recorded here, newest first. This tracks
project/tooling/data changes; `wiki/log.md` remains the fine-grained record of
individual wiki page operations.

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
