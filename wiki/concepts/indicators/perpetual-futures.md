---
title: "Perpetual Futures"
type: concept
created: 2026-04-06
updated: 2026-07-19
status: excellent
confidence: medium
tags: [derivatives, crypto, futures, perpetual-futures]
aliases: ["Perps", "Perpetual Swaps", "Perpetual Contracts"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[futures]]", "[[leverage]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[funding-rate]]"
  - "[[liquidation]]"
  - "[[open-interest]]"
  - "[[leverage]]"
  - "[[margin]]"
  - "[[auto-deleveraging]]"
  - "[[funding-rate-arbitrage]]"
  - "[[crypto-perp-backtesting-pitfalls]]"
  - "[[liquidation-cascade-modeling]]"
  - "[[2025-10-crypto-liquidation-cascade]]"
---

# Perpetual Futures

**Perpetual futures** (commonly called **perps**) are a type of [[derivatives]] contract that allows traders to speculate on the price of an asset with [[leverage]] and *no expiration date*. Unlike traditional [[futures]] contracts that settle on a fixed date, perps can be held indefinitely, making them the dominant instrument in cryptocurrency [[derivatives]] trading.

## How Perps Work

A perpetual futures contract is an agreement to buy or sell an asset at a future time, but with no predetermined settlement date. Traders open **long** (buy) or **short** (sell) positions, posting [[margin]] as collateral. The contract tracks an underlying [[spot-price]] through a mechanism called the [[funding-rate]].

### Key Mechanics

1. **No Expiry**: Unlike quarterly or monthly [[futures]], perps never expire. A position remains open until the trader closes it or gets [[liquidation|liquidated]].
2. **Leverage**: Traders can open positions larger than their collateral. For example, 10x [[leverage]] means a $1,000 deposit controls a $10,000 position.
3. **Mark Price vs. Last Price**: The **mark price** is derived from the [[spot-price]] index and is used for [[liquidation]] calculations to prevent market manipulation via wicks on thin [[order-books]].
4. **Margin**: Traders post [[margin]] (collateral) which acts as a security deposit. This can be in the form of the quote asset (usually USDT/USDC) or the base asset (coin-margined).

## The Funding Rate Mechanism

The [[funding-rate]] is the core innovation that keeps perpetual futures prices tethered to the [[spot-price]]. It works as a periodic payment between longs and shorts:

- **When perp price > spot price** (premium): Longs pay shorts. This incentivizes selling the perp and buying spot, pushing the perp price down.
- **When perp price < spot price** (discount): Shorts pay longs. This incentivizes buying the perp and selling spot, pushing the perp price up.

Conceptually, the funding rate is calculated as:

```
Funding Rate = Average Premium Index + clamp(Interest Rate - Premium Index, -0.05%, 0.05%)
```

Where the **Premium Index** measures the deviation between the perp's mark price and the spot index price. Most exchanges use an interest rate component of 0.01% per 8-hour interval (roughly 0.03% per day) as a baseline.

Payments occur at regular intervals -- typically every 8 hours on most centralized exchanges, though [[hyperliquid]] uses hourly funding intervals for more granular price convergence.

### Funding-rate interpretation

The sign and magnitude of the [[funding-rate]] is itself a sentiment and positioning signal:

| Funding regime | Sign | What it implies | Who pays |
|---|---|---|---|
| Strongly positive (e.g. > ~0.05%/8h) | + | Aggressive leveraged longs; crowded, often late-trend | Longs pay shorts |
| Mildly positive (baseline ~0.01%/8h) | + | Normal contango-like state; longs slightly dominant | Longs pay shorts |
| Near zero | 0 | Balanced book; perp ≈ spot | Negligible |
| Negative | − | Leveraged shorts dominant; possible squeeze setup | Shorts pay longs |
| Deeply negative (capitulation) | − − | Forced shorting / fear; contrarian-long signal | Shorts pay longs |

### Funding worked example (illustrative)

*(Numbers below are illustrative, not a live quote.)* Suppose a trader holds a **$100,000 long** BTC perp position while funding sits at **+0.01% per 8-hour interval** (the common baseline):

```
Per-interval payment = 0.0001 × $100,000 = $10
Intervals per day    = 3  (every 8 hours)
Daily funding cost   = 3 × $10 = $30  (~0.03%/day, ~11% APY)
```

If funding spikes to **+0.10%/8h** in a euphoric rally, the same position bleeds `0.001 × 100,000 × 3 = $300/day` (~110% APY) — a cost that can dominate directional P&L and is the core of the [[funding-rate-arbitrage]] basis trade (short the expensive perp, hold spot, collect funding). See [[funding-rate]] for the full annualization conventions.

### Annualizing funding

| Per-8h funding | Approx daily | Approx APY |
|---|---|---|
| 0.01% (baseline) | 0.03% | ~11% |
| 0.03% | 0.09% | ~33% |
| 0.05% | 0.15% | ~55% |
| 0.10% | 0.30% | ~110% |

APY ≈ per-interval rate × intervals-per-year (3 × 365 = 1,095 for 8h funding; 24 × 365 = 8,760 for [[hyperliquid]]'s hourly funding). Compounding makes the true figure slightly higher.

## Leverage and Margin

Perpetual futures offer varying levels of [[leverage]] depending on the exchange and the asset:

| Asset | Typical Max Leverage | Example Exchange |
|-------|---------------------|-----------------|
| BTC | 40x-125x | [[hyperliquid]] (40x), [[binance]] (125x) |
| ETH | 40x-100x | Most major exchanges |
| Altcoins | 5x-50x | Varies by [[liquidity]] |
| Memecoins | 3x-20x | Lower due to [[volatility]] |

Higher [[leverage]] means a smaller price movement triggers [[liquidation]]. At 40x leverage, a ~2.5% adverse move (before fees) wipes out the position entirely. See [[liquidation]] for detailed mechanics.

### Leverage and liquidation distance

The relationship between leverage and the adverse move that wipes out [[margin]] (ignoring maintenance margin and fees, illustrative):

| Leverage | Approx. liquidation distance | Risk character |
|---|---|---|
| 2x | ~50% | Conservative; survives major drawdowns |
| 5x | ~20% | Moderate |
| 10x | ~10% | Aggressive; one bad day can liquidate |
| 25x | ~4% | Speculative; routine [[volatility]] is dangerous |
| 40x | ~2.5% | Near-gambling; common at liquidation in cascades |
| 100x+ | ~1% | Almost always liquidated; favoured by exchanges for fee/liquidation revenue |

Maintenance-margin tiers shrink these distances further. See [[liquidation]] and [[liquidation-cascade-modeling]].

## Perps vs Dated Futures

| Dimension | Perpetual futures | Dated (quarterly/monthly) futures |
|---|---|---|
| Expiry | None | Fixed settlement date |
| Price anchor | [[funding-rate]] (periodic payment) | Convergence to spot at expiry |
| Roll cost | None (no roll) | Must roll; exposed to [[contango]]/[[backwardation]] |
| Basis behaviour | Mean-reverts via funding | Decays to zero toward expiry |
| Dominant venue | Crypto CEX/DEX | TradFi (CME) and crypto quarterly |
| Carry signal | Funding rate | Calendar basis / term structure |
| Typical user | Crypto speculators, basis arbs | Hedgers, institutional term traders |

The absence of a roll is the headline advantage of perps; the price is the recurring funding cash flow, which the dated contract does not have.

## Live Market Data

> **Data note:** the snapshot below is a point-in-time illustration from when this page was last sourced, not a live feed. Use it for scale, not for current quotes.

As of the latest data from [[hyperliquid]], which operates 229 perpetual markets:

- **BTC Perp**: Trading at $69,192 with 28,766 BTC in [[open-interest]] (~$2 billion notional). Maximum leverage: 40x.
- **ETH Perp**: 560,526 ETH in open interest (~$1.2 billion notional).
- **HYPE Perp**: 21.8 million tokens in open interest.

These figures illustrate the massive capital deployed in perpetual futures markets, rivaling and often exceeding spot market [[volume]] on many assets.

## Who Trades Perps

1. **Retail Speculators**: The largest user base. Attracted by leverage and the ability to profit from both rising and falling markets. Most retail traders lose money due to poor [[risk-management]] and excessive [[leverage]].
2. **Market Makers**: Provide [[liquidity]] by quoting both sides of the [[order-book]]. They profit from the [[bid-ask-spread]] while hedging directional exposure on [[spot-markets]] or other venues.
3. **Hedgers**: Miners, token treasuries, and [[portfolio-theory|portfolio managers]] use perps to hedge price exposure without selling the underlying asset.
4. **Arbitrageurs**: Exploit price discrepancies between perp and [[spot-price]], or capture [[funding-rate]] payments through delta-neutral strategies. See [[arbitrage]].

## History

Perpetual futures were invented by **BitMEX** (founded by Arthur Hayes) around 2016. The BitMEX XBTUSD contract became the most traded instrument in crypto, often processing billions in daily [[volume]]. The innovation was adapting a concept from traditional finance (perpetual swaps in interest rate markets) to cryptocurrency.

Since then, perps have proliferated across:

- **Centralized exchanges**: [[binance]], Bybit, OKX, Bitget
- **Decentralized protocols**: [[hyperliquid]], [[dydx]], [[gmx]], Drift, Vertex
- [[hyperliquid]] has emerged as a leading decentralized perps venue with its own Layer 1 blockchain, offering 229 perp markets with deep [[liquidity]]

## Advantages

- **No expiry**: No need to roll contracts, avoiding [[contango]] and [[backwardation]] costs
- **High [[leverage]]**: Capital-efficient exposure
- **Two-way trading**: Easily go long or short without borrowing the asset
- **Deep [[liquidity]]**: Perp markets often have tighter [[bid-ask-spread|spreads]] than spot
- **Price discovery**: Perps often lead [[spot-price]] movements, making them important for [[market-microstructure]]

## Disadvantages

- **[[funding-rate]] costs**: Holding positions during periods of high funding can be expensive
- **[[liquidation]] risk**: Leveraged positions can be forcibly closed, resulting in total loss of [[margin]]
- **Complexity**: Margin calculations, funding payments, and mark price mechanics add layers of complexity
- **Exchange risk**: Counterparty risk on centralized exchanges; smart contract risk on decentralized ones
- **Regulatory uncertainty**: Many jurisdictions restrict or ban leveraged crypto trading

## Common Misconceptions

1. **"Perps are just like spot trading with leverage"** -- They are not. Perps introduce [[funding-rate]] costs, [[liquidation]] risk, and mark price mechanics that fundamentally change the risk profile.
2. **"Higher leverage = higher profit"** -- Higher [[leverage]] increases both potential profit and potential loss. It also brings [[liquidation]] price closer, increasing the probability of total loss.
3. **"Funding rate is always a cost"** -- Funding can be positive or negative. Traders on the less crowded side *receive* funding payments, which can be a source of income.
4. **"Perp price always equals spot price"** -- It generally tracks closely due to the [[funding-rate]] mechanism, but can deviate significantly during extreme [[volatility]] or when [[liquidity]] is thin.
5. **"You can't lose more than your margin"** -- While most modern exchanges prevent negative balances through [[liquidation]] engines and [[insurance-fund|insurance funds]], in extreme cases ADL (auto-deleveraging) can affect profitable positions. See [[liquidation]].

## Auto-Deleveraging (ADL)

Auto-deleveraging is the *last-resort* loss-socialisation mechanism that engages when an exchange's [[insurance-fund|insurance fund]] cannot fully absorb a bankrupt position. Instead of leaving the bankrupt account with a negative balance — which an exchange cannot legally claw back — the platform **force-closes opposing profitable positions** at the bankruptcy price until the book is balanced. The trader on the wrong side of ADL has a *winning* position involuntarily liquidated, not a losing one.

### When ADL fires

ADL is triggered when, in sequence:

1. A position becomes bankrupt (margin breached past zero).
2. Mark-price liquidations cannot fill at or better than the bankruptcy price (typically because the order book is too thin or the move is too violent).
3. The insurance fund is insufficient to cover the residual deficit.

This is rare in normal markets but becomes a central risk during cascade events — the [[2025-10-crypto-liquidation-cascade|October 10-11 2025 crash]] socialised billions through ADL across multiple venues simultaneously.

### Priority queue mechanics

Each exchange maintains an **ADL ranking** for every account holding a perp position. Ranking inputs are typically:

- **Profit ratio** of the position (% PnL on margin used)
- **Effective leverage** in use

Higher profit + higher leverage = higher ADL priority (closed first). The ranking is usually exposed to the user as a five-segment indicator. Hedgers on max leverage with deeply ITM positions face the greatest exposure.

### Cross-venue differences

| Exchange | ADL trigger | Priority formula | Notable details |
|----------|-------------|------------------|-----------------|
| **Binance** | After insurance fund + counterparty liquidation; isolated and cross | Profit % × effective leverage | Per-instrument rankings; ADL light visible in UI; events relatively rare on BTC/ETH |
| **Bybit** | After insurance fund; per-symbol | Similar profit × leverage | Was central to the Oct 2025 cascade; ranking and events are publicly disclosed post-event |
| **OKX** | Tiered insurance per margin mode; ADL as last resort | Profit × leverage with portfolio-margin nuances | Portfolio-margin accounts can be deleveraged on a *position-by-position* basis |
| **Hyperliquid** | On-chain ADL via the clearinghouse contract | Higher PnL → higher rank, transparent on-chain | All ADL events permanently visible on-chain; the L1 clearinghouse logs them with block-level timestamps |

The implication for traders is that an apparently delta-neutral basis or [[funding-rate-arbitrage]] trade is *not* truly neutral on a venue with ADL — the hedge leg can be ripped off mid-cascade. See [[auto-deleveraging]] for the full treatment and [[liquidation-cascade-modeling]] for how to size this risk.

## Funding-Rate Regime History

Funding-rate dynamics have shifted markedly between perp eras. Modelling perps without acknowledging the regime is one of the more expensive mistakes in the [[crypto-perp-backtesting-pitfalls]] catalogue.

- **Pre-2024 baseline**: BTC/ETH perp funding annualised in the 5-12% range outside of strong-trend episodes. The basis carry trade (long spot, short perp) was a genuine institutional opportunity but capacity-limited and not widely crowded.
- **2024 peak**: Spot ETF approvals (BTC in January 2024, ETH in July 2024) opened a regulated leg of the cash-and-carry trade. As ETF inflows sustained spot demand, perp funding repeatedly ran at ~15-25% APY annualised on BTC/ETH; aggregate basis trade APY peaked near **19%** in late 2024.
- **2025 compression**: Crowding into the basis trade and proliferation of structured products that arb funding pulled rates down sharply. By mid-2025, all-in basis APY had compressed below **4%** — frequently lower than US Treasury bills. The October 10-11 2025 cascade and the resulting ADL scars accelerated this: many participants who had previously assumed the trade was risk-free recalibrated and exited, but the collapse in willing longs *and* the corresponding decay of the funding signal both compressed and de-anchored the rate.
- **Post-cascade era (late 2025 onwards)**: funding rates have remained structurally lower and more regime-dependent; the trade has become a tactical position rather than a perpetual carry.

A backtest that uses 2024-funding history to project forward returns will dramatically overstate strategy viability. Either segment by regime or use [[market-regime-detection-ml|regime detection]] to switch funding models.

## Implications for Backtesters

Anyone building or evaluating a perp-based strategy should treat the standard pitfalls list ([[backtesting-pitfalls]]) as the floor, not the ceiling. Crypto perps add a layer of failure modes — auto-deleveraging breaking nominally hedged trades, depth-aware slippage during cascades, point-in-time on-chain data, fragmentation across CEX/DEX venues, stablecoin collateral risk, and oracle manipulation in DeFi-integrated strategies. The dedicated [[crypto-perp-backtesting-pitfalls]] page collects these with calibration recipes and references the relevant data vendors ([[coinglass]], [[glassnode]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this instrument's data directly:

- **Fetch** — `GET /api/v1/hyperliquid/summary?coin=BTC` bundles price, funding, and OI for one perp in a single call; `GET /api/v1/hyperliquid/prices` and `GET /api/v1/hyperliquid/open-interest` cover all ~230 Hyperliquid perps at once, with Binance-side positioning via `GET /api/v1/derivatives/summary`
- **Candles** — `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` is the perp OHLCV backbone; `GET /api/v1/hyperliquid/l2-book` adds an order-book depth snapshot before execution
- **Backtest** — `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30), `GET /api/v1/backtesting/klines` (Hyperliquid daily to 2023 launch, 1h/4h several months; Binance spot to 2017-08), `GET /api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30) — model funding payments and liquidation risk explicitly, not just price P&L
- **Tip** — perp backtests fail most often on the funding leg: charge/credit funding every interval the position is open, and segment results by funding regime — 2021-style persistent positive funding does not extrapolate

## Sources

- Exchange documentation: [[binance]], Bybit, OKX, and [[hyperliquid]] perpetual-contract and funding-rate specifications (mechanics and ADL priority formulas)
- [[coinglass]] and [[glassnode]] -- aggregate funding-rate, open-interest, and liquidation data referenced in the regime history
- BitMEX (Arthur Hayes) -- original XBTUSD perpetual swap design (2016), the foundational reference for the instrument
- General market knowledge; no specific wiki source ingested yet for the quantitative figures, which are illustrative unless attributed.

## Further Reading

- [[funding-rate]] -- Deep dive into the mechanism that keeps perps anchored
- [[funding-rate-arbitrage]] -- The dominant perp-native carry strategy and its 2025 regime shift
- [[open-interest]] -- Understanding the total outstanding contracts
- [[liquidation]] -- How and when positions get forcibly closed
- [[auto-deleveraging]] -- The cascade mechanism that closes profitable positions
- [[liquidation-cascade-modeling]] -- Quantifying systemic liquidation risk
- [[2025-10-crypto-liquidation-cascade]] -- The defining recent stress event
- [[crypto-perp-backtesting-pitfalls]] -- Perp-specific backtesting failure modes
- [[risk-management]] -- Essential practices for trading leveraged instruments
- [[leverage]] -- Understanding magnified exposure
- [[margin]] -- Collateral requirements and types
