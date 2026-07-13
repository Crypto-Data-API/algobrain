---
title: "Hyperliquid Fee Tiers and Maker Rebates"
type: concept
created: 2026-06-20
updated: 2026-07-13
status: draft
tags: [crypto, market-microstructure, liquidity, derivatives, arbitrage]
aliases: ["Hyperliquid Fees", "HL Fee Schedule", "Hyperliquid Maker Rebates", "Hyperliquid Fee Tiers"]
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hip-3-builder-deployed-perps]]", "[[hlp]]", "[[hyperliquid-margining-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[perp-dex-aggregation]]", "[[clob]]", "[[order-book]]", "[[market-microstructure]]", "[[arbitrage]]", "[[slippage]]", "[[market-impact]]", "[[cryptodataapi]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[clob]]", "[[order-book]]"]
difficulty: intermediate
---

# Hyperliquid Fee Tiers and Maker Rebates

The **Hyperliquid fee schedule** is a volume-tiered, community-directed pricing model layered directly on top of [[hypercore|HyperCore]]'s on-chain [[clob|central limit order book]]. Three properties make it materially different from a flat-fee venue and directly shape order-book strategy: (1) a trader's fee tier is set by **rolling 14-day trading volume**, with spot volume counting double toward the tier; (2) a **single fee tier** applies across perps, [[hip-3-builder-deployed-perps|HIP-3]] perps, and spot; and (3) **maker rebates are paid continuously** on each trade rather than accrued and settled later. All fees are directed to the community — to the [[hlp|HLP]] vault, an assistance fund, and deployers — rather than to a corporate operator (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

> **Scope note.** This page treats the *structure* of fees and how it interacts with order-book strategy. The research grounding it is qualitative on most specifics; this page therefore avoids quoting exact basis-point figures that the source does not state. For the live numeric schedule, consult the official Hyperliquid fees documentation linked under [[#Sources]].

## Why Fees Are an Order-Book Concept

On a [[clob|CLOB]], the maker/taker fee split is not an afterthought — it is the economic gradient that decides whether liquidity rests in the book or is pulled. A continuously-paid maker rebate subsidizes resting limit orders (passive liquidity), while the taker fee taxes liquidity removal (aggressive market orders). The relationship between the two sets the **breakeven half-spread** a market maker must quote and the **minimum edge** an arbitrageur must capture before crossing the book is profitable. Because Hyperliquid's fees are tied to a personalized rolling-volume tier, the *same* trade can be profitable for a high-tier maker and unprofitable for a low-tier taker — a structural asymmetry that concentrates passive liquidity in a small set of high-volume market makers.

## Fee-Tier Mechanics

| Mechanic | Description | Strategy consequence |
|---|---|---|
| **Rolling 14-day volume** | Tier is set by trailing two-week trading volume, not lifetime or monthly. | Tiers update continuously; a maker who pauses quoting decays back down a tier within two weeks. |
| **Spot volume counts double** | Spot trading contributes 2x toward the tier threshold relative to perps. | A market maker can "buy" a better perp tier by also running spot volume — a cross-product incentive. |
| **Single tier across products** | One tier spans perps, HIP-3 perps, and spot. | Volume earned anywhere lowers fees everywhere; encourages consolidating flow on one account. |
| **Continuous maker rebates** | Rebates are credited on each fill, not batched/settled later. | No accrual lag; passive-quoting PnL compounds in real time and is easy to attribute per fill. |

(Source: [[2026-04-22-gap-finder-hyperliquid-order-books]])

## Where the Fees Go

Hyperliquid directs trading fees back to the community rather than to a centralized operator. The recipients are:

| Recipient | Role |
|---|---|
| **[[hlp|HLP]]** (Hyperliquidity Provider vault) | Depositor-capitalized market-making and backstop vault; see [[hyperliquid-liquidation-engine]] for how HLP also absorbs liquidation flow. |
| **Assistance fund** | Protocol-level reserve. |
| **Deployers** | [[hip-3-builder-deployed-perps|HIP-3]] market deployers receive a configurable share of fees from the markets they list. |

This routing means fee economics, liquidity provision, and protocol governance are part of a single system: the rebates that incentivize tight quoting are funded by the same flow that capitalizes HLP and rewards deployers (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## HIP-3 Deployer Fee Shares and "Growth Mode"

[[hip-3-builder-deployed-perps|HIP-3]] builder-deployed perps share HyperCore's matching engine but let the deployer configure their own **fee share**. Two structural points matter for traders:

- **Deployer fee shares can stack on top of protocol fees.** Per the research, a deployer's configured share can in some configurations exceed 100%, causing protocol fees to rise *in lockstep* with the deployer's take. A long-tail HIP-3 market can therefore carry meaningfully different effective costs than a core market on the same engine.
- **"Growth mode"** is a regime in which protocol fees, rebates, and the volume that counts toward a trader's tier are **substantially reduced**. This changes the calculus for early liquidity providers on a new market: lower friction, but also reduced rebate income and reduced tier-credit for the volume done there.

The practical takeaway: before deploying capital into a HIP-3 market, a trader should treat its fee configuration as a first-class risk parameter alongside its oracle quality and leverage limits — two HIP-3 markets on identical infrastructure can have very different net economics (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Aligned-Quote-Asset Discounts

Certain spot pairs — notably those involving **aligned quote assets** — benefit from **reduced taker fees and improved maker rebates**. This alters the effective economics of providing liquidity in those specific markets, making passive quoting in aligned-quote pairs structurally more attractive than the base schedule implies (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Tying Fees to Order-Book Strategy

The fee schedule is not neutral with respect to strategy — it tilts the playing field in several concrete ways.

### When low taker fees enable arbitrage

[[arbitrage|Arbitrage]] and [[perp-dex-aggregation|cross-venue routing]] strategies are *takers* — they cross the book to capture a transient mispricing. Their profitability is gated by the round-trip taker cost. A trader who has climbed to a high volume tier (and therefore pays lower taker fees) can profitably act on smaller dislocations than a low-tier taker, who needs a larger gap to clear costs. Lower taker fees thus widen the set of exploitable mispricings — including funding-rate spreads against other venues (see [[hyperliquid-funding-rate-microstructure]]) and basis trades that route through Hyperliquid as a price-discovery venue.

### How high maker rebates justify aggressive quoting

A continuously-paid maker rebate means each resting fill earns income *independent of spread capture*. At high volume tiers, the rebate can offset a portion of adverse selection, letting a market maker quote tighter and deeper than the raw spread would justify. This is the mechanism by which rebates translate into observable order-book depth: the rebate subsidizes the inventory risk of resting liquidity. The same logic explains why passive liquidity concentrates in high-tier accounts — the marginal economics of quoting improve with tier.

### Fee-tier cliff effects

Because tiers are discrete thresholds on rolling 14-day volume, traders near a boundary face a **cliff effect**: pushing volume just over a threshold lowers fees on *all* subsequent flow, not just the marginal trades. This creates an incentive to "trade to the tier" near period boundaries — running extra volume (including double-weighted spot volume) specifically to cross a threshold. The behavioral consequence is bursts of volume from accounts straddling a tier, which can transiently affect book depth and spreads around those accounts.

## Worked Reasoning (illustrative, no figures invented)

A market maker deciding whether to rest a bid on a Hyperliquid perp weighs:

```
expected_maker_pnl_per_fill =
      spread_capture
    + maker_rebate(tier)            # continuous, credited per fill
    - adverse_selection_cost        # informed flow trading against the quote
    - inventory_funding_cost        # see [[funding-rate]]

# Higher tier -> larger rebate -> positive expected_maker_pnl at a tighter quote
# -> the MM can rest closer to mid -> observed book is deeper/tighter
```

The arbitrageur's mirror calculation:

```
expected_taker_pnl =
      mispricing_captured
    - taker_fee(tier)               # lower at higher tiers
    - slippage / [[market-impact]]
    - routing/latency cost

# Lower taker fee -> smaller mispricing_captured still clears -> more trades viable
```

These are structural relationships, not backtested numbers — the live coefficients come from the official fee schedule and depend on the trader's tier and the specific market (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order book snapshot
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest
- `GET /api/v1/hyperliquid/summary?coin=BTC` — all-in-one perp data

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BTC&limit=100` — current + historical funding
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

- [[hyperliquid]] — the venue; platform overview and competitive landscape
- [[hypercore]] — the L1 engine that hosts the order books these fees price
- [[hip-3-builder-deployed-perps]] — builder-deployed markets with configurable deployer fee shares and growth mode
- [[hlp]] — primary community recipient of fees and the depositor-capitalized vault
- [[hyperliquid-margining-modes]] — companion page on cross / isolated / no-cross margin
- [[hyperliquid-liquidation-engine]] — how HLP earns liquidation premium alongside fee income
- [[hyperliquid-funding-rate-microstructure]] — funding as a second cost/return component for perp positions
- [[funding-rate]] — general background on perpetual funding
- [[perp-dex-aggregation]] — cross-venue routing where Hyperliquid taker fees gate arbitrage
- [[clob]], [[order-book]] — the microstructure fees are applied to
- [[arbitrage]], [[slippage]], [[market-impact]] — taker-side cost components
- [[market-microstructure]] — domain parent

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — gap-finder deep research synthesizing Hyperliquid's official fee documentation and 2024–2026 developments.
- **Hyperliquid Docs — Fees.** https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees — rolling 14-day-volume tiers, spot-double counting, single tier across products, continuous maker rebates, community fee routing (HLP / assistance fund / deployers), aligned-quote-asset discounts.
- **Hyperliquid Docs — HIP-3 Builder-Deployed Perpetuals.** https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals — deployer fee shares and "growth mode" fee regime.
