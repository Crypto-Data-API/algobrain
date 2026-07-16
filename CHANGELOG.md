# Changelog

All notable changes to **AlgoBrain** are recorded here, newest first. This tracks
project/tooling/data changes; `wiki/log.md` remains the fine-grained record of
individual wiki page operations.

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
  the batch source-summary slug is still a stale batch name (cosmetic).
