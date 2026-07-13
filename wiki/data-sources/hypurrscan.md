---
title: "HypurrScan"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, crypto, defi, hyperliquid, on-chain, analytics]
aliases: ["Hypurr Scan", "Hyperliquid Scan", "HyperliquidScan"]
related: ["[[hyperliquid]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-vault-architecture]]", "[[hlp-cascade-alongside-playbook]]", "[[cascade-detection-signals]]"]
source_type: data
source_url: "https://hypurrscan.io"
confidence: high
---

HypurrScan is the leading on-chain analytics and explorer platform for [[hyperliquid|Hyperliquid]], the high-performance perp DEX built on its own custom L1 (HyperBVM). Functionally, it occupies the same niche for Hyperliquid that Etherscan does for Ethereum or Solscan does for [[solana|Solana]] -- a public-facing block explorer plus dashboards layered on top of indexed protocol state. Because Hyperliquid runs a fully transparent on-chain CLOB, HypurrScan is able to surface things that are normally invisible on a CEX: every open position, every liquidation, every [[hlp|HLP]] vault rebalance, and every whale's running P&L, all in near real time.

For traders running [[hyperliquid-hlp-basis-arbitrage|HLP basis arb]], cascade-following strategies, keeper bots, or doing on-chain due diligence on counterparties and vaults, HypurrScan is the de-facto front end. As of 2025/2026 it is community-built (by independent developers in the Hyperliquid ecosystem rather than the protocol team itself); verify current ownership, branding, and feature set on the site, since fast-moving DeFi explorers change frequently.

## Background

- **What it is:** A web-based explorer + analytics dashboard suite for the [[hyperliquid|Hyperliquid]] L1 and its perp/spot order books
- **Audience:** Hyperliquid traders, HLP depositors, on-chain researchers, keeper-bot operators, journalists, and vault due-diligence analysts
- **Data scope:** Hyperliquid only -- not multi-chain, not multi-venue
- **Update frequency:** Most dashboards refresh in near real time off Hyperliquid block data; some aggregate stats are batched (e.g., daily volume, leaderboards)
- **Positioning vs the native UI:** Hyperliquid's own app.hyperliquid.xyz front end is execution-focused and shows limited historical depth. HypurrScan fills the analytics gap -- historical funding, vault history, leaderboards, liquidation archives

## Core Features

### Vault Tracking

The flagship feature for [[hyperliquid-hlp-basis-arbitrage|HLP-aware traders]]:

- **HLP TVL over time** -- daily/weekly TVL chart, deposit/withdrawal flow
- **HLP APR history** -- realized yield on a rolling basis, useful for sizing the deposit-and-collect leg of [[hyperliquid-hlp-basis-arbitrage]]
- **HLP share price** -- the per-share value of the vault, which is the cleanest measure of underlying P&L (TVL alone confounds inflows with returns)
- **Depositor count and concentration** -- how many wallets are in HLP, and how concentrated they are
- **Position breakdown** -- which pairs HLP currently has exposure to, sized in USD notional
- **Drawdown markers** -- visualization of past HLP drawdowns (e.g., the JELLYJELLY incident in March 2025)
- **Other Hyperliquid vaults** -- non-HLP user-created vaults are also tracked, with leaderboards by AUM and APR (see [[hyperliquid-vault-architecture]])

### Wallet Leaderboards

Because Hyperliquid is a transparent on-chain CLOB, every wallet's positions and P&L are public:

- **Top traders by realized P&L** (24h, 7d, 30d, all-time)
- **Top long / top short by pair** -- who has the largest open exposure on each market
- **Whale flow** -- recent large entries and exits, useful as a cascade leading indicator
- **Wallet pages** -- per-wallet view of all open positions, P&L curve, historical fills, and (for nicknamed wallets like "James Wynn", "0x Sun", etc.) tracked identities

### Liquidation Feed

Real-time stream of liquidations on Hyperliquid:

- **Live liquidation list** -- pair, size, side, mark price, P&L impact, wallet
- **Aggregated liquidation stats** -- per-pair daily totals, useful for [[cascade-detection-signals]]
- **HLP's role in liquidations** -- HLP earns liquidation bonuses; the feed shows when HLP is on the take side
- **Cascade-friendly view** -- when liquidations cluster in time on one pair, the feed makes the cascade visible before mark/oracle data has to confirm it

### Funding Rate History

The native Hyperliquid UI shows current funding and a short rolling chart; HypurrScan keeps deeper history:

- Per-pair funding rate charts going back through Hyperliquid's history
- Cross-pair comparison -- which pairs are paying the most
- Spike detection -- helpful for catching the kind of [[funding-rate]] divergences that make [[funding-rate-arbitrage]] (and the cross-CEX leg of [[hyperliquid-hlp-basis-arbitrage]]) profitable
- Useful complement to [[coinglass]] and [[the-block]] for HL-specific funding context

### Position Visibility

Hyperliquid's transparent CLOB is unusual -- on a centralized perp venue (Binance, Bybit, OKX) you cannot see other traders' positions; on Hyperliquid, you can. HypurrScan aggregates and visualizes:

- **All open positions** for any wallet
- **Liquidation prices** for each position (on-chain margin and mark price are public)
- **Cluster maps** of where collective open interest sits relative to mark price -- effectively a public liquidation-density heatmap
- **Top-of-book skew** by pair

This is the on-chain analog of what [[coinglass|Coinglass]] estimates for CEX venues, except here it is exact rather than estimated.

### Token and Airdrop Tracking

- **HYPE staking and delegation** -- validator stake distribution, staking yield
- **Points farming / eligibility tracking** -- where applicable for Hyperliquid's incentive programs
- **Holder distribution** for HYPE and any spot tokens listed on Hyperliquid's spot order book
- **Airdrop history** including the November 2024 HYPE distribution

## Comparison to Alternatives

- **vs Hyperliquid native UI (app.hyperliquid.xyz):** The native UI is execution-first -- order entry, current positions, current funding. It shows limited history and no leaderboards. HypurrScan is the analytics layer the native UI deliberately omits
- **vs [[quicknode|QuickNode SQL Explorer]]:** QuickNode exposes the raw Hyperliquid L1 tables via SQL -- 29 tables including trades, fills, funding, liquidations, vault equities, oracle prices (see [[2026-04-06-quicknode-hyperliquid-sql-explorer]]). It is more powerful and more flexible, but requires writing SQL and an API key. HypurrScan is the no-code / GUI alternative; QuickNode is the programmatic alternative. Most operators use both -- HypurrScan for daily monitoring, QuickNode for backtests and custom analytics
- **vs [[coinglass|Coinglass]]:** Coinglass is multi-venue (Binance, Bybit, OKX, Hyperliquid, etc.) and aggregates funding, OI, liquidations, long/short ratios. Coinglass covers Hyperliquid but with less depth; HypurrScan is HL-only but goes deeper on HLP, vault state, wallet-level visibility
- **vs [[defillama|DeFiLlama]]:** DeFiLlama tracks Hyperliquid TVL and aggregate volume at a high level for cross-protocol comparison. It does not surface individual vault positions, leaderboards, or liquidation feeds
- **vs [[dune-analytics|Dune Analytics]]:** Dune lets you write custom SQL on indexed Hyperliquid data (where coverage exists). HypurrScan is curated and pre-built; Dune is bespoke

## Pricing

As of 2025/2026, HypurrScan is **mostly free** for public dashboards, explorer pages, leaderboards, vault tracking, liquidation feeds, and funding history. Some advanced features may require a paid tier:

- **Whale alerts / push notifications** -- alerting on specific wallet or vault activity
- **Tracker bots** (Telegram/Discord webhook integrations)
- **Custom dashboards or saved queries**
- **Higher-rate API access**

This is consistent with the Etherscan / Solscan pattern: free explorer + paid pro tier with API and alerting. **Verify current pricing and feature gating on hypurrscan.io directly** -- this changes frequently in fast-moving ecosystems.

## How HLP-Aware Traders Use It

For traders running [[hyperliquid-hlp-basis-arbitrage]], HypurrScan is part of the daily routine:

- **Daily HLP TVL/APR check** -- has APR drifted below the deposit threshold? Has TVL spiked, signaling APR compression ahead? Set the kill-criteria thresholds from the strategy page
- **Pre-cascade signal:** monitor whether HLP exposure on a single pair has become large. HLP's known weakness is concentration in a single illiquid pair -- the JELLYJELLY incident in March 2025 was exactly this failure mode (~$13M paper loss before governance intervention)
- **Post-cascade validation:** after a market-wide liquidation event, check HLP's drawdown and recovery curve. HypurrScan's share-price chart is the cleanest read on actual P&L impact
- **Deposit/withdrawal timing:** flow data shows whether sophisticated capital is exiting HLP ahead of a perceived risk event -- useful as a contrarian or follow-the-smart-money signal
- **Counterparty due diligence on user vaults** -- before depositing into a non-HLP vault, the leaderboard and history pages are the standard check

## How Cascade Traders Use It

For traders running [[liquidation-cascade-arbitrage]] or following the [[hlp-cascade-alongside-playbook]]:

- **Real-time liquidation feed** -- the primary live signal. When liquidations on a pair cluster in time, that is a forming cascade
- **Funding rate spikes** -- early warning that positioning is one-sided. Combined with [[cascade-detection-signals]], a sustained funding > 0.05%/8h on a thin-OI pair is the kind of setup that precedes forced unwinds
- **Mark vs oracle deviation** -- in-cascade signal that the mark price is being driven by forced flow rather than informational flow. Hyperliquid's oracle price is on-chain; HypurrScan surfaces the deviation
- **Open-interest concentration on a single wallet** -- when one whale's liquidation price is the load-bearing risk on a pair, the cascade is binary on that wallet's stop-out

## How Keeper Bots Use It (Read-Only)

Keeper bots (liquidation bots, on-chain market makers, arb routers) typically run against the Hyperliquid native API or QuickNode SQL for execution-path data. HypurrScan is used as:

- **Backtest data feed** -- pulling historical funding, liquidation, and vault-state data for strategy research without writing custom indexers
- **Fallback when the native API is rate-limited** -- read-only views work via the web front end even when the websocket is throttled
- **Monitoring dashboard** -- non-execution-path observability for bot operators (alerts on HLP drawdown, on funding spikes, on competitor wallets)

Keeper bots should not depend on HypurrScan for execution -- explorers can lag, indexes can have bugs, and the latency budget is wrong. Use it for monitoring, not for the trade decision itself.

## Data Quality and Limitations

- **HypurrScan reflects what is on-chain on Hyperliquid.** If the Hyperliquid L1 has a chain-level outage, halt, or reorg, HypurrScan inherits that. The same applies to indexer downtime
- **Indexing bugs are possible** -- as with any community-built explorer. Cross-check a load-bearing claim against [[quicknode|QuickNode SQL Explorer]] (which queries directly against an independent index) before sizing a trade on it
- **No multi-venue context** -- HypurrScan is HL-only by design. For cross-CEX comparisons (e.g., the cross-venue funding leg of [[hyperliquid-hlp-basis-arbitrage]]), use [[coinglass]] or roll your own
- **Centralization risk on the explorer itself** -- if HypurrScan goes down, the underlying chain data is still queryable directly via the Hyperliquid node API or QuickNode, but the curated dashboards are gone. Do not build production tooling that hard-depends on HypurrScan
- **Editorialization on leaderboards** -- which wallets get nicknamed, featured, or hidden is a curatorial decision. Treat wallet labels as suggestive, not authoritative
- **Aggregate stat cadence** -- some dashboards (e.g., daily volume, leaderboards) are batched, not real-time. Fine for positioning analysis, not for execution
- **No coverage of off-chain / pre-settlement activity** -- Hyperliquid is fully on-chain so this is mostly moot, but anything routed through builder/integrator front ends shows up only via builder fee fields

## Tools and APIs

As of 2025/2026, HypurrScan has surfaced (verify availability on the site):

- **Web app** -- the primary interface
- **API access** -- a programmatic API for some endpoints; rate limits and pricing vary by tier
- **Webhook / alert subscriptions** -- whale movements, vault drawdowns, liquidation thresholds
- **Telegram / Discord bots** -- community integrations that surface HypurrScan data into chat
- **Mobile experience** -- responsive web; native app status varies, verify on the site

For programmatic data pulls at scale, [[quicknode|QuickNode SQL Explorer]] is generally the more reliable backend (see [[2026-04-06-quicknode-hyperliquid-sql-explorer]]). HypurrScan's API is best for "fetch the same numbers a human would see on the dashboard" use cases.

## Related

- [[hyperliquid]] -- the underlying protocol
- [[hyperliquid-hlp-basis-arbitrage]] -- core strategy that uses HypurrScan as primary monitoring tool
- [[hyperliquid-vault-architecture]] -- HLP and user vault structure
- [[hlp-cascade-alongside-playbook]] -- how cascade traders coordinate with HLP's behavior
- [[cascade-detection-signals]] -- the live signals HypurrScan exposes
- [[liquidation-cascade-arbitrage]] -- adjacent cascade-trading strategy
- [[funding-rate-arbitrage]] -- uses HypurrScan funding history for pair selection
- [[quicknode]] -- programmatic SQL alternative for HL on-chain data
- [[2026-04-06-quicknode-hyperliquid-sql-explorer]] -- companion source on the SQL data layer
- [[coinglass]] -- multi-venue comparison
- [[defillama]] -- high-level TVL and yield aggregation
- [[the-block]] -- broader crypto data context
- [[dune-analytics]] -- bespoke SQL on indexed chain data
- [[crypto-data-sources]] -- broader catalog

## Sources

- General knowledge of HypurrScan based on public dashboards at hypurrscan.io as of 2025/2026
- Cross-referenced with [[hyperliquid]] protocol documentation and [[2026-04-06-quicknode-hyperliquid-sql-explorer]] for the underlying chain-data model
- JELLYJELLY incident details from [[hyperliquid-hlp-basis-arbitrage]] case-study notes (March 2025)
- All specific feature, pricing, and API claims should be verified directly on hypurrscan.io -- the platform iterates frequently
