# AlgoBrain

An LLM Wiki-Brain knowledge base for **crypto trading strategy generation**. Expert knowledge of crypto, blockchain, DeFi, trading, algorithms, markets, macro and AI context. ~3,500 interlinked markdown nodes.

<video src="https://github.com/Crypto-Data-API/algobrain/raw/main/attachments/algobrain-obsidian-graph-view.mp4" controls muted loop width="100%">
  Obsidian graph view of the AlgoBrain vault —
  <a href="attachments/algobrain-obsidian-graph-view.mp4">download the clip</a>.
</video>

Scoped to crypto: stock-market entities, equity fundamentals, and personal content are excluded; macro context (FX, rates, commodities, market history), the AI knowledge base, and asset-agnostic trading knowledge are included.

## Quickstart

Serve the vault to Claude Code (or any MCP client) as a local wiki API:

```powershell
# One-time setup
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r tools/requirements.txt
```

Then start the server with the **`/start-servers`** slash command in Claude Code — or run it directly:

```powershell
powershell -ExecutionPolicy Bypass -File tools/start_servers.ps1
```

This launches the wiki MCP server over Streamable HTTP at **http://127.0.0.1:8010/mcp**, exposing `wiki_search`, `wiki_read`, `wiki_stats`, `wiki_lint`, and `wiki_ingest` over the ~3,500-node vault. It's already registered for this repo via `.mcp.json` — approve it when Claude Code prompts. Stop it again with `tools/stop_servers.ps1`.

## What's inside

| Area | Content |
|------|---------|
| `wiki/strategies/` | ~370 strategy pages: funding-rate harvesting, basis/carry, liquidation plays, MEV, memecoin sniping, grid/mean-reversion/momentum, the 27-basket Hyperliquid signal library, 100+ page arbitrage encyclopedia |
| `wiki/strategy-development/` | Methodology for *producing* strategies: edge taxonomy, hypothesis-to-backtest workflow, overfitting & p-hacking detection, capacity/failure-mode analysis, and per-venue trading maps (Hyperliquid, low-cap, arbitrage) |
| `wiki/concepts/` | ~1,000 concept pages: microstructure, indicators, risk, portfolio theory, backtesting, behavioral finance, on-chain metrics, options mechanics |
| `wiki/markets/` | 1,000+ crypto asset pages + commodities/forex/bonds macro context |
| `wiki/entities/` | Crypto exchanges, DeFi protocols, quant/crypto funds, trading legends, miners, regulators |
| `wiki/crypto-narratives/` | Backtester-ready narrative catalog: 69 archetypes, 290 quantified historical instances (JSON) |
| `wiki/ai-trading/` + `wiki/artificial-intelligence/` | ML models, bots, backtesting frameworks, LLM finance, general AI knowledge |
| `wiki/data-sources/` | Data provider catalog — **CryptoDataAPI is the canonical data layer** |

Start at `wiki/index.md` (master table of contents) or `wiki/overview.md` (state of the wiki).

## Data layer: CryptoDataAPI

[CryptoDataAPI](https://cryptodataapi.com) provides the wiki's live and historical data: 190+ REST endpoints (auth: `X-API-Key` header) covering prices, funding rates, open interest, liquidations, order-book depth, market/volatility/meme/event/security/policy regimes, HMM quant probabilities, on-chain flows, whale tracking, Hyperliquid trader intelligence, sentiment, ETF flows, NFTs, and a Parquet backtesting archive back to 2020.

- Hub: `wiki/data-sources/cryptodataapi.md`, with per-category pages `cryptodataapi-*.md`
- Wiki pages that map to an endpoint include a **"Getting the Data (CryptoDataAPI)"** section with live + historical access and a curl example

## The LLM Wiki pattern

The wiki is designed to be maintained by an LLM agent (Claude Code or similar):

- **Schema**: `CLAUDE.md` / `AGENTS.md` define page types, YAML frontmatter, naming conventions, ingest/lint workflows
- **Templates**: `templates/` holds page skeletons for each type
- **Log**: `wiki/log.md` is an append-only record of every wiki operation
- Every page carries frontmatter (`type`, `status`, `tags`, `related`) enabling Dataview queries and graph coloring

## Opening in Obsidian

Open this repository folder as a vault. On first launch Obsidian will prompt to enable the community plugins listed in `.obsidian/community-plugins.json`:

- **Dataview** (required — index pages use it), **Templater**, **Obsidian Git**, **Graph Analysis**, **Marp Slides**, **Webpage HTML Export**

The graph view is pre-configured with per-folder color groups (`.obsidian/graph.json`). Attachments save to `attachments/`.
