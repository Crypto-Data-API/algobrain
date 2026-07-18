---
title: "Liquidations"
type: concept
created: 2026-07-17
updated: 2026-07-19
status: draft
tags: [liquidations, perpetual-futures, leverage, derivatives, market-microstructure, crypto]
aliases: ["Forced Liquidation", "Margin Call", "Liquidation Cascade"]
domain: [market-microstructure, risk-management]
difficulty: intermediate
prerequisites: ["[[perpetual-futures]]", "[[leverage]]", "[[margin]]"]
---

# Liquidations

A **liquidation** is the forced closure of a leveraged trading position when the trader's margin equity falls below the exchange's maintenance margin requirement. On crypto perpetual futures exchanges, the liquidation engine automatically takes over the position and closes it — either via a market order into the order book, or via a dedicated liquidation mechanism like Hyperliquid's [[hyperliquid-liquidation-engine|backstop liquidation system]]. Clustered liquidations — where many positions are closed at similar price levels — drive cascade volatility: the forced selling pushes price further in the adverse direction, triggering more liquidations in a feedback loop.

## How It Works

### The margin lifecycle of a leveraged position

A trader opens a 10× leveraged long on BTC at $60,000:
- **Notional:** $60,000
- **Initial margin deposited:** $6,000 (10% of notional)
- **Maintenance margin (exchange minimum):** typically 0.5–5% of notional = $300–$3,000

If BTC falls from $60,000 to $54,000 (−10%), the position has lost $6,000 of notional value, wiping out the entire initial margin. The **liquidation price** is slightly above this — the exchange closes the position before equity goes to zero, using the maintenance margin buffer to cover exchange losses:

> **Liquidation price (long) ≈ entry_price × (1 − initial_margin_rate + maintenance_margin_rate)**
> 
> At 10× leverage with 0.5% maintenance: $60,000 × (1 − 0.10 + 0.005) = $54,300

The exchange's liquidation engine fires at $54,300, not $54,000, so the exchange is protected against the position going below zero.

### Liquidation cascade mechanics

1. A price move pushes a cluster of positions to their liquidation prices.
2. The exchange closes them via market or limit orders, adding sell pressure.
3. This additional selling pushes price down further.
4. New positions hit *their* liquidation prices.
5. The cascade continues until: (a) liquidatable positions are exhausted, (b) price stabilises at a natural buy zone, or (c) an insurance fund or backstop buyer absorbs the flow.

On Binance, Bybit, and other CEX perp exchanges, liquidations become visible on the "liquidation heatmap" — a density map of stop/liquidation clusters at price levels. Hyperliquid's [[hyperliquid-liquidation-engine|liquidation engine]] is designed to handle these via an internal market maker before orders hit the public order book.

### Insurance funds and socialised loss

Most exchanges maintain an **insurance fund** (funded by fees and partial liquidation proceeds) to cover cases where the liquidated position cannot cover its losses. If the insurance fund is insufficient, the loss is **socialised** across all profitable position holders on the other side — called "auto-deleveraging" (ADL) on Binance and OKX. ADL is a significant counterparty risk for profitable traders in volatile conditions.

## Concrete Examples

- **March 12, 2020 ("Black Thursday"):** BTC fell 50% in ~24 hours. BitMEX's liquidation engine could not absorb the volume — the exchange briefly went to zero bid on its own order book. Total liquidations across crypto exceeded $1 billion in a single day. An estimated $8.3 million in underbid MakerDAO liquidation auctions were claimed for near-zero during the chaos.
- **May 19, 2021:** In a single day, over $8 billion in crypto positions were liquidated as BTC fell from ~$58,000 to ~$30,000 within 24 hours. The cascade was triggered by Elon Musk's Bitcoin mining tweets and China's first-wave crypto crackdown announcement.
- **November 2022 (FTX collapse):** FTX's solvency crisis triggered forced liquidations of FTT, SOL, and related tokens. Alameda Research's massive leveraged positions in these assets amplified the cascade as they were force-closed.
- **Hyperliquid, Q4 2024:** A "whale" position in a thinly-traded HIP-3 perp was liquidated and temporarily impacted the HLP (Hyperliquid's liquidity provider vault), demonstrating that even well-designed liquidation engines face stress in thin markets.

## Trading Relevance

Liquidation data and dynamics are central to several AlgoBrain strategies:

- **[[liquidation-cascade-arbitrage]]:** Actively hunts the post-cascade regime — entering counter-trend after a liquidation flush exhausts the forced selling. The core thesis is that the cascade overshoots fair value, creating a reversion opportunity.
- **[[contrarian-extremes]]:** Extreme liquidation volume is a component of the fear/panic signal. Large liquidation events often coincide with extreme Fear & Greed readings and deeply negative funding rates — the conditions the strategy targets.
- **[[funding-rate-arbitrage]]:** Liquidation cascades temporarily create very negative funding (remaining longs flee, shorts are overloaded), which is the exact condition that maximises the reward for a delta-neutral long-spot/short-perp carry position.
- **[[mev-execution-guide]]:** On-chain liquidations (Aave, Compound, MakerDAO) are one of the most reliable MEV opportunities. Searchers compete to be the first to trigger and capture the liquidation bonus (typically 5-10% of the collateral) paid by the protocol.
- **[[liquidation-price-aware-sizing]]:** The inverse use — sizing your *own* positions so that a named wick or vol spike cannot reach your liquidation price. This is a core position-sizing discipline in the [[multi-strategy-crypto-portfolio]].
- **[[on-chain-analysis]]:** CryptoDataAPI's liquidation data endpoints provide real-time and historical liquidation flows, which are useful as a proxy for local crowding and positioning extremes.

## Related

- [[perpetual-futures]] — the instrument where crypto liquidations most commonly occur
- [[funding-rate]] — funding rates and liquidation frequency are co-indicators of leverage extremes
- [[open-interest]] — rising OI with negative funding is a precursor to long-side liquidation cascades
- [[liquidation-cascade-arbitrage]] — the strategy that trades the post-cascade regime
- [[hyperliquid-liquidation-engine]] — Hyperliquid's specific backstop system
- [[mev-execution-guide]] — captures on-chain liquidation bonuses via MEV bundles
- [[contrarian-extremes]] — liquidation spikes confirm extreme sentiment readings
- [[funding-rate-arbitrage]] — benefits from the funding environment created by liquidation cascades
- [[cross-margin-vs-isolated-margin]] — margin mode determines whether a liquidation on one position affects others
- [[market-impact]] — large liquidations cause market impact that triggers further liquidations

## Sources

- General crypto/derivatives knowledge; no specific wiki source ingested yet.
