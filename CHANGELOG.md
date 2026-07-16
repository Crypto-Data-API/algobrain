# Changelog

All notable changes to **AlgoBrain** are recorded here, newest first. This tracks
project/tooling/data changes; `wiki/log.md` remains the fine-grained record of
individual wiki page operations.

## 2026-07-17 — README disclaimer + docs tidy

- Added a **Disclaimer** to the README (not financial / investment advice, DYOR,
  use at your own risk, no liability) to cover public use.
- Tidied changelog wording to generic data-source phrasing.

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
