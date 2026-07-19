# Changelog

All notable changes to **AlgoBrain** are recorded here, newest first. This tracks
project/tooling/data changes; `wiki/log.md` remains the fine-grained record of
individual wiki page operations.

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
