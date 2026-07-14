---
title: "Greeks.live"
type: source
created: 2026-05-05
updated: 2026-06-21
status: excellent
tags: [data-provider, options, options-analytics, crypto, volatility, defi]
aliases: ["GreeksLive", "Greeks Live"]
related: ["[[deribit]]", "[[bitcoin-options]]", "[[ethereum-options]]", "[[implied-volatility]]", "[[options-greeks]]", "[[portfolio-greeks-aggregation]]", "[[volatility-surface]]"]
source_type: data
source_url: "https://greeks.live"
confidence: high
---

Greeks.live is a crypto-options analytics platform built primarily on top of [[deribit]] data, offering a real-time [[options-greeks|Greeks]] dashboard, [[volatility-surface|implied-vol surface]] visualization, position management, a block-trade tape, and an aggregated [[rfq|RFQ]] network for institutional size. It is the closest thing the crypto market has to a purpose-built equivalent of ORATS or LiveVol — a single workspace where a [[bitcoin-options|BTC]] or [[ethereum-options|ETH]] options trader can monitor [[implied-volatility|IV]], build positions, see institutional flow, and source liquidity that the lit book cannot absorb. As of 2025 it is the most widely used third-party analytics layer for the [[deribit]]-centric crypto options market, and a hub for the crypto-options community on Telegram and Discord.

## At-a-Glance

| Field | Detail |
|---|---|
| What it is | Crypto-options analytics + RFQ workbench layered on [[deribit]] data |
| Primary coverage | [[bitcoin-options|BTC]] and [[ethereum-options|ETH]] options on [[deribit]] |
| Core modules | IV [[volatility-surface\|surface]] heatmap, position-level [[options-greeks\|Greeks]], block-trade tape, [[rfq\|RFQ]] network |
| Volatility index | Visualizes [[deribit#DVOL Index — The "VIX of Crypto"\|DVOL]] (crypto's [[vix\|VIX]] analogue) |
| Audience | Pro/prosumer crypto-options traders, MMs, structured-product desks |
| Pricing | Generous free tier; Pro ~$30-$50/mo; institutional negotiated |
| Closest analogues | ORATS/LiveVol (TradFi); [[paradigm-rfq\|Paradigm]], [[laevitas]] (crypto) |
| Key caveat | Deribit-centric, single-venue concentration; not a backtesting engine |
| TradFi parallel | Greeks read identically to xsp-options/index-options desks -- only the venue differs |

## Background

- **Founded:** ~2019, by a team of crypto-options traders and quants
- **Core focus:** [[bitcoin-options|BTC]] and [[ethereum-options|ETH]] options listed on [[deribit]], the dominant venue for crypto options
- **Audience:** Professional and prosumer crypto-options traders, market makers, structured-product desks, and crypto-native funds; growing footprint with TradFi vol traders crossing into crypto
- **Community:** Operates a large Telegram and Discord community where traders post block-trade screenshots, debate positioning, and share strategy ideas; the community has become a recognized sentiment proxy for crypto options
- **Positioning:** "Pro tools for crypto options" — combining a Bloomberg-DLIB-style analytics workbench with a retail-accessible web UI

## Core Features

### Volatility Surface Heatmap
- Real-time [[volatility-surface|IV surface]] for BTC and ETH across the full Deribit listed chain
- Heatmap views of term structure (expiry axis) crossed with strike skew (moneyness axis)
- Snapshot and historical replay modes — useful for visualizing how the surface deformed during events like FTX collapse, ETF approval, or [[bitcoin-halving]]
- Skew metrics: 25-delta risk-reversal, 25-delta butterfly, ATM term structure

### Position-Level Greeks
- Build any combination of long/short calls and puts and instantly see net [[options-greeks|delta, gamma, vega, theta, rho]] and vanna/volga/charm exposures
- Payoff diagrams at expiry and at intermediate dates with vol-shock overlays (vol up/down 5/10/20 vol points)
- Multi-leg combo construction with strike and expiry pickers; supports calendars, diagonals, ratios, condors, etc.
- Aggregates a logged-in user's open Deribit positions into a single portfolio Greek view (see [[portfolio-greeks-aggregation]])

### Block-Trade Tape
- Streaming feed of block trades printing on [[deribit]] (Deribit's block facility has minimum sizes — 25 BTC for BTC options, 200 ETH for ETH options as of 2025)
- Each print is annotated with strike, expiry, side (call/put), buyer-or-seller flag (when inferable), notional, and IV
- Filters by expiry, strike range, notional, and structure type (single-leg vs spread vs combo)
- One of the few public real-time windows into institutional [[bitcoin-options|BTC options]] positioning

### RFQ Network
- Aggregates request-for-quote flow across multiple crypto-options market makers
- Counterparty pool reportedly includes [[gsr]], [[galaxy-digital|Galaxy]], [[akuna-capital|Akuna Crypto]], [[wintermute]], and other crypto OTC desks (subject to onboarding; specific MM lineup varies over time)
- Used to source size for trades that cannot be filled on the lit Deribit book without significant slippage
- Competes most directly with [[paradigm-rfq|Paradigm]], the institutional-leaning RFQ network used by larger funds

## Data Depth

- **Historical IV surfaces:** Several years of surface snapshots for BTC and ETH; depth grows over time as the platform accumulates data
- **Realized volatility:** Rolling realized vol for BTC and ETH at multiple windows (e.g. 7d, 14d, 30d, 90d), used for VRP analysis (see [[variance-risk-premium]])
- **Perp-funding context:** [[funding-rate|Funding rate]] panels alongside the options data to contextualize term structure (high positive funding often coexists with steep call skew at the front end)
- **Term-structure replay:** Scrub through past dates and watch how the term structure deformed around events
- **DVOL:** Pulls and visualizes [[deribit#DVOL Index — The "VIX of Crypto"|Deribit's DVOL]] index — the BTC and ETH equivalents of [[vix|VIX]]

## Pricing

(All pricing as of 2025; confirm current tiers on [greeks.live](https://greeks.live).)

- **Free tier:** Main dashboard with delayed or live IV surface, basic Greeks builder, public block-trade tape, community access
- **Pro tier (~$30-$50/month):** Historical surface data, alerting (vol-spike, skew-flip, block-trade-size triggers), API access, deeper position analytics
- **Institutional tier:** Custom integrations, larger API quota, RFQ-network onboarding, white-label dashboards for funds and OTC desks; pricing negotiated

The free tier is unusually generous compared to TradFi analogues — most retail crypto-options traders never need to upgrade. Pro is positioned for serious self-directed traders; institutional is for funds and desks.

## How Discretionary Crypto Options Traders Use It

For traders applying a professional options playbook to crypto rather than equities, Greeks.live is effectively the workbench:

- **Variance risk premium harvesting:** BTC [[implied-volatility|IV]] structurally trades meaningfully above realized vol — typically a wider spread than SPX's VRP. Greeks.live makes it easy to monitor IV-vs-RV in real time and structure short-premium books (iron condors, strangles, ratio spreads) at favorable skew points. See [[variance-risk-premium]] and [[short-volatility-strategies]]
- **Hedging crypto spot exposure:** Holders of [[bitcoin|BTC]] or [[ethereum|ETH]] spot use Greeks.live to size protective puts or put-spreads at quantified vega/theta cost; the position-builder shows the marginal cost of insurance under different vol regimes
- **Spotting institutional positioning:** The block-trade tape is one of the cleanest signals for "what are large desks doing" in crypto options. Heavy call-spread buying weeks before expiry is read as institutional bullishness; large downside-put accumulation is read as hedging or directional bearishness
- **Sourcing size via RFQ:** Trades above ~$5M notional often cannot be cleanly filled on the Deribit lit book without moving the surface. The RFQ network lets traders quietly request quotes from multiple MMs and lift the best offer
- **Event-driven structures:** Around CPI prints, FOMC, [[bitcoin-halving|halvings]], ETH protocol upgrades, or anticipated ETF news, Greeks.live's surface visualization makes event-vol premium easy to see and trade against (e.g. selling the front-week strangle while buying the second-week as a calendar)

## Comparable Tools

| Tool | Coverage | Strengths | Weaknesses vs Greeks.live |
|------|----------|-----------|---------------------------|
| **[[deribit]] native interface** | Deribit only | Authoritative chain, native execution | Weak surface viz, limited historical, no aggregated block tape |
| **[[paradigm-rfq|Paradigm]]** | Deribit + others, RFQ-first | Institutional-grade RFQ, deepest MM pool for size | Less of an analytics platform; no community layer |
| **[[laevitas]]** | Deribit + alt venues | Strong derivatives dashboards, options + futures + funding in one view | Less position-builder focus; thinner block tape |
| **[[amberdata]]** | Multi-venue, institutional | Enterprise-grade data feeds, normalized across exchanges | Enterprise pricing; not retail-friendly UI |
| **[[coinglass]]** | Multi-venue derivatives | Free, broad derivatives coverage including liquidations | Less options-focused; surface tools are shallow |
| **orats** | US listed equity options | Reference design for retail options analytics | Does not cover crypto |

For a crypto-only options trader, Greeks.live + Deribit's native UI + occasional Paradigm for size covers most workflows.

## Strengths

- **Purpose-built for crypto options** — only platform with this depth specifically tuned to BTC/ETH on Deribit
- **Tight integration with [[deribit]]** — the dominant venue, so coverage of "the market" is near-complete
- **Community layer** — Telegram/Discord channels add real-time qualitative context (positioning rumors, large prints commentary) that no pure-data tool provides
- **Generous free tier** — most self-directed traders can operate without paying
- **RFQ access** — lowers the barrier to institutional-style execution for prosumer accounts
- **Position-builder ergonomics** — fast multi-leg construction with intuitive payoff and Greek visualizations

## Weaknesses

- **Deribit-centric** — [[aevo]], [[lyra]], [[premia]], [[panoptic]], [[ribbon]], and other DeFi options venues are not natively covered, even though they hold a non-trivial share of decentralized options flow
- **Thin compared to TradFi institutional tools** — Bloomberg DLIB, ICE, and Numerix offer deeper analytics (exotics pricing, full-surface arb, custom payoffs) that Greeks.live does not match
- **Smaller-altcoin coverage is patchy** — Deribit's listed options are essentially BTC and ETH only; SOL and other altcoin options on Deribit (where listed) have thin liquidity and surface fits can be unstable
- **Single-venue concentration risk** — if Deribit data feed degrades or the venue has issues, the platform's signal value drops
- **Data quality on edge cases** — surface fitting in low-liquidity wings or near expiry can produce spurious skew readings
- **Not a backtesting platform** — historical data exists, but the workflow is geared toward observation and execution, not systematic strategy research; serious quants still pull raw Deribit data via API or [[amberdata]]

## Key Use Cases

For a trader applying a discretionary options methodology to crypto, Greeks.live is most useful for:

1. **VRP capture on BTC and ETH** — BTC's [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] often runs 50-80% while realized vol sits 35-55%, a substantially fatter premium than [[vix|VIX]] vs S&P realized. Short-premium strategies ([[iron-condor|iron condors]], [[short-strangle|short strangles]], [[ratio-spread|ratio spreads]]) sized off Greeks.live's surface and Greek tools
2. **Event hedging** — buying [[bitcoin-options|BTC]] or [[ethereum-options|ETH]] put-spreads ahead of [[bitcoin-halving|halvings]], protocol upgrades (Ethereum hard forks), CPI prints, or FOMC meetings, where IV typically rises into the event and crashes after; Greeks.live's surface replay makes it straightforward to see the historical event-vol pattern
3. **Dealer-flow signal** — large block-trade prints often precede multi-day directional moves as dealers hedge their resulting exposure; the block tape is a leading indicator analogous to [[gamma-exposure|GEX]] in equities
4. **Calendar and skew structures** — ratio calendar spreads and skew trades (risk reversals) are easier to construct and monitor in Greeks.live than in Deribit's native UI
5. **Cross-venue arb scouting** — comparing Greeks.live's Deribit IVs against [[cme|CME]] BTC options or [[binance]] options to find pricing discrepancies (occasional, but exploitable when they arise)

## Limitations to Note

- **Not a primary execution venue** — orders ultimately route to [[deribit]]; Greeks.live is the analytics and order-staging layer, not the matching engine
- **Account linking required for portfolio-level Greeks** — users must link a Deribit API key (read-only or trading) to aggregate positions; some funds avoid this for security policy reasons
- **Pricing and feature mix can change** — the platform iterates rapidly; verify current tiers and capabilities before committing workflow

### Caveats Summary

| Caveat | Why it matters | Mitigation |
|---|---|---|
| Deribit-centric | DeFi venues ([[aevo]], [[lyra]], etc.) and CEX options not natively covered | Cross-check [[laevitas]]/[[coinglass]] for off-Deribit flow |
| Single-venue concentration | Signal value drops if [[deribit]] feed degrades | Treat as one input, not the whole market |
| Surface-fit noise in wings | Low-liquidity far-OTM/near-expiry strikes can show spurious skew | Discount thin-wing readings; prefer ATM/liquid strikes |
| Not a backtesting platform | History exists but workflow is observation/execution | Pull raw Deribit/[[amberdata]] data for systematic research |
| Account linking for portfolio Greeks | Requires a Deribit API key; some funds disallow | Use read-only keys or manual position entry |
| Block-tape side inference | Buyer/seller flag is inferred, not authoritative | Treat directional reads as probabilistic |

These are reference cautions about how to interpret the platform's data, not allegations -- Greeks.live is widely regarded as the leading purpose-built crypto-options analytics layer; the limitations are inherent to a single-venue, real-time analytics tool.

## Related

- [[deribit]] — the underlying venue Greeks.live wraps
- [[bitcoin-options]] — BTC options market and strategy notes
- [[ethereum-options]] — ETH options market
- [[implied-volatility]] — IV concept and metrics
- [[options-greeks]] — delta, gamma, vega, theta, rho
- [[volatility-surface]] — surface fitting and visualization
- [[portfolio-greeks-aggregation]] — multi-position Greek netting
- [[variance-risk-premium]] — the structural edge crypto-options short-vol traders harvest
- [[paradigm-rfq]] — institutional RFQ network, Greeks.live's closest competitor on size sourcing
- [[laevitas]] — alternative crypto derivatives analytics platform
- [[amberdata]] — enterprise-grade multi-venue crypto data
- [[coinglass]] — free crypto-derivatives dashboards
- [[funding-rate]] — perp funding context Greeks.live displays alongside options data
- [[short-volatility-strategies]] — strategies natural to build on Greeks.live's tooling

## Sources

- General knowledge — Greeks.live product structure, feature set, and community presence as widely documented in crypto-options trader circles and in [[deribit]] ecosystem reporting through 2025
- Publicly available information from greeks.live regarding features and tiers (pricing and exact MM lineup as of 2025; confirm current state on the platform)
