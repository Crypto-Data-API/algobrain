# AlgoBrain

> AlgoBrain can derive millions of unique crypto trading strategies, and is specifically structured to ensure the highest quality context is provided to AI Agents through a free local MCP server.

An LLM Wiki-Brain knowledge base for **crypto trading strategy generation**. Expert knowledge of crypto, blockchain, DeFi, trading, algorithms, markets, macro and AI context. ~4,900 interlinked markdown nodes.

[![Obsidian graph view of the AlgoBrain vault](attachments/algobrain-obsidian-graph-view.gif)](attachments/algobrain-obsidian-graph-view.mp4)

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

This launches the wiki MCP server over Streamable HTTP at **http://127.0.0.1:8010/mcp**, exposing `wiki_search`, `wiki_read`, `wiki_stats`, `wiki_lint`, and `wiki_ingest` over the full vault. It's already registered for this repo via `.mcp.json` — approve it when Claude Code prompts. Stop it again with `tools/stop_servers.ps1`.

## What's inside

| Area | Content |
|------|---------|
| `wiki/strategies/` | ~445 strategy pages: funding-rate harvesting, basis/carry, liquidation plays, MEV, memecoin sniping, grid/mean-reversion/momentum, a 51-basket Hyperliquid signal library, 100+ page arbitrage encyclopedia, a complete 270-cell combination-strategy matrix, and a documented pair universe — **1.55M+ distinct, specifiable strategy configurations** (computed from wiki state by `tools/count_configurations.py`, conservative assumptions printed; validation discipline applies — see Disclaimer) |
| `wiki/strategy-development/` | Methodology for *producing* strategies: edge taxonomy, hypothesis-to-backtest workflow, overfitting & p-hacking detection, capacity/failure-mode analysis, and per-venue trading maps (Hyperliquid, low-cap, arbitrage) |
| `wiki/concepts/` | ~1,000 concept pages: microstructure, indicators, risk, portfolio theory, backtesting, behavioral finance, on-chain metrics, options mechanics |
| `wiki/markets/` | 2,400+ crypto asset pages + commodities/forex/bonds macro context |
| `wiki/entities/` | Crypto exchanges, DeFi protocols, quant/crypto funds, trading legends, miners, regulators |
| `wiki/crypto-narratives/` | Backtester-ready narrative catalog: 69 archetypes, 290 quantified historical instances (JSON) |
| `wiki/ai-trading/` + `wiki/artificial-intelligence/` | ML models, bots, backtesting frameworks, LLM finance, general AI knowledge |
| `wiki/data-sources/` | Data provider catalog — **CryptoDataAPI is the canonical data layer** |

Start at `wiki/index.md` (master table of contents) or `wiki/overview.md` (state of the wiki).

## Data layer: CryptoDataAPI

[CryptoDataAPI](https://cryptodataapi.com) provides the wiki's live and historical data: 190+ REST endpoints (auth: `X-API-Key` header) covering prices, funding rates, open interest, liquidations, order-book depth, market/volatility/meme/event/security/policy regimes, HMM quant probabilities, on-chain flows, whale tracking, Hyperliquid trader intelligence, sentiment, ETF flows, NFTs, and a Parquet backtesting archive back to 2020.

- Hub: `wiki/data-sources/cryptodataapi.md`, with per-category pages `cryptodataapi-*.md`; agent guide: `wiki/data-sources/cryptodataapi-mcp.md`
- Wiki pages that map to an endpoint include a **"Getting the Data (CryptoDataAPI)"** section with live + historical access and a curl example
- 640 pages additionally carry an **"AI agent workflow"** block — every applicable strategy, indicator, and methodology page plus all 209 coins with Hyperliquid perps: the page-specific signal endpoints (parameterized by perp symbol on coin pages), regime gate, matching backtesting archive (with honest data-availability windows), and execution tips for an agent running that strategy
- The local wiki MCP server attaches a `data_instruction` block to every `wiki_search` response, so any connected agent is always pointed at CryptoDataAPI for market data (MCP connect + free API key)
- Data sections deep-link the matching **live dashboards** on cryptodataapi.com (funding, OI, liquidations, whales, GEX, regimes, ETF flows…), and pages matching one of the site's 14 **[AI prompt-library](https://cryptodataapi.com/prompts)** prompts reference it directly (funding-fade → Funding Rate Extremes Scanner, overfitting checklist → Backtest Overfitting Checker, …)
- Trading-venue pages carry **referral links with automatic fee discounts** — [Hyperliquid](https://app.hyperliquid.xyz/join/CRYPTODATAAPI) (4% off spot & perp fees) and [Binance](https://www.binance.com/register?ref=RZSKG1XM) (up to 20% off trading fees); AI agents routing trades are instructed (per page and via `wiki_search`) to use them so end-users get the discounts *(referral links — a commission may be earned, at no cost to you)*

### Live data: connect to the CryptoDataAPI MCP server

To run strategies against live markets, connect your agent to the hosted **[CryptoDataAPI MCP server](https://cryptodataapi.com/ai-agents/mcp-server)**. It streams live prices, funding rates, open interest, liquidations, and order-book depth for **Hyperliquid** and **Binance**, market/volatility regimes and whale activity, plus the historical **backtesting archive** (klines / funding / liquidations, Parquet back to 2020).

Add it to Claude Code — browser login, no API key needed (an OAuth flow opens on the first tool call):

```bash
claude mcp add --transport http cryptodataapi https://cryptodataapi.com/mcp
```

Or authenticate with an API key via the `X-API-Key` header:

```bash
export CRYPTODATA_API_KEY="cdk_live_YOUR_KEY"
claude mcp add --transport http cryptodataapi https://cryptodataapi.com/mcp \
  --header 'X-API-Key: ${CRYPTODATA_API_KEY}'
```

For any MCP client, add it to your config JSON:

```json
{
  "mcpServers": {
    "cryptodataapi": {
      "url": "https://cryptodataapi.com/mcp",
      "headers": { "X-API-Key": "cdk_live_YOUR_KEY" }
    }
  }
}
```

Tools include `get_price`, `get_hyperliquid_prices`, `get_funding_rates`, `get_open_interest`, `get_liquidations`, `get_order_book`, `get_market_regime`, `get_etf_flows`, and `get_whale_activity` (Pro). Get a free key at [cryptodataapi.com/login](https://cryptodataapi.com/login) (no card), or by email:

```bash
curl -X POST https://cryptodataapi.com/api/v1/auth/keys \
  -H "Content-Type: application/json" \
  -d '{"email":"you@example.com"}'
```

Rate limits: Free 5 req/min · Pro 30 · Pro Plus 60.

## The LLM Wiki pattern

The wiki is designed to be maintained by an LLM agent (Claude Code or similar):

- **Schema**: `CLAUDE.md` / `AGENTS.md` define page types, YAML frontmatter, naming conventions, ingest/lint workflows
- **Templates**: `templates/` holds page skeletons for each type
- **Log**: `wiki/log.md` is an append-only record of every wiki operation
- Every page carries frontmatter (`type`, `status`, `tags`, `related`) enabling Dataview queries and graph coloring

## Opening in Obsidian

Download **[Obsidian](https://obsidian.md/download)** (free — macOS, Windows, Linux, iOS, Android) and open this repository folder as a vault. On first launch Obsidian will prompt to enable the community plugins listed in `.obsidian/community-plugins.json`:

- **Dataview** (required — index pages use it), **Templater**, **Obsidian Git**, **Graph Analysis**, **Marp Slides**, **Webpage HTML Export**

The graph view is pre-configured with per-folder color groups (`.obsidian/graph.json`). Attachments save to `attachments/`.

## Disclaimer

AlgoBrain is a research and educational knowledge base. **Nothing in this repository is financial, investment, legal, or tax advice.** All content — strategy pages, data recipes, figures, and any linked tools or APIs — is provided **"as is"**, for informational purposes only, and may be inaccurate, incomplete, or out of date.

Trading cryptocurrencies and derivatives carries a **substantial risk of loss**, and past performance does not indicate future results. **Do your own research (DYOR)** and consult a licensed financial professional before making any decision. You use this material **entirely at your own risk**: the authors, contributors, and maintainers accept **no liability** for any loss or damage of any kind arising from its use. Nothing here is a solicitation or recommendation to buy, sell, or hold any asset.
