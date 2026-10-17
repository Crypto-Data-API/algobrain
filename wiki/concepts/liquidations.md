---
title: "Liquidations"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
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

*Correction (2026-10-17):* ADL is not spread evenly across all profitable holders. Venues rank opposing positions by profit and leverage and force-close the highest-ranked ones first, at the bankruptcy price. A highly profitable, highly leveraged position, such as the short hedge leg of a basis trade, is the first to be closed. The October 10-11, 2025 cascade was the first systemic ADL event: it force-closed profitable hedge legs across Binance, Bybit, OKX and [[hyperliquid|Hyperliquid]] (see [[auto-deleveraging]] and [[2025-10-crypto-liquidation-cascade]]).

### Where liquidation flow comes from (and what you cannot see)

- **CEX perps** (Binance, Bybit, OKX): liquidation orders are reported through public websocket streams. These streams are throttled or aggregated (Binance's force-order stream pushes only the latest liquidation per symbol per 1,000 ms snapshot), so reported totals are a *lower bound*.
- **Hyperliquid**: every liquidation is an on-chain fill. Per-fill capture is exact, and positions are public, so the *forward* liquidation map (where resting positions would liquidate) can be computed rather than estimated.
- **On-chain lending** (Aave, Compound, Maker/Sky): liquidations are permissionless calls that pay a bonus to the keeper. This is the MEV side covered by [[liquidation-cascade-arbitrage]].
- **"Liquidation heatmaps"** sold by data vendors are mostly *modelled* liquidation levels inferred from OI changes and assumed leverage, not observed positions. Treat them as estimates outside Hyperliquid.

## Concrete Examples

- **March 12, 2020 ("Black Thursday"):** BTC fell 50% in ~24 hours. BitMEX's liquidation engine could not absorb the volume — the exchange briefly went to zero bid on its own order book. Total liquidations across crypto exceeded $1 billion in a single day. An estimated $8.3 million in underbid MakerDAO liquidation auctions were claimed for near-zero during the chaos. *(Review note 2026-10-17: the widely reported BitMEX detail is a ~25-minute outage early on March 13, which some traders credit with halting the cascade. The "zero bid" claim above is unverified; the zero-bid episode is well documented for MakerDAO's collateral auctions. See [[covid-crash]].)*
- **May 19, 2021:** In a single day, over $8 billion in crypto positions were liquidated as BTC fell from ~$58,000 to ~$30,000 within 24 hours. The cascade was triggered by Elon Musk's Bitcoin mining tweets and China's first-wave crypto crackdown announcement. *(Correction 2026-10-17: the intraday move on May 19 was ~$43K → ~$30K, about −30%. BTC was last near $58K around May 10, so the "$58K to $30K in 24h" framing merges a nine-day decline into one day. [[crypto-flash-crashes]] records −30% ($43K → $30K) and [[liquidation-cascade-modeling]] records ~$8.6B liquidated.)*
- **November 2022 (FTX collapse):** FTX's solvency crisis triggered forced liquidations of FTT, SOL, and related tokens. Alameda Research's massive leveraged positions in these assets amplified the cascade as they were force-closed.
- **Hyperliquid, Q4 2024:** A "whale" position in a thinly-traded HIP-3 perp was liquidated and temporarily impacted the HLP (Hyperliquid's liquidity provider vault), demonstrating that even well-designed liquidation engines face stress in thin markets. *(Correction 2026-10-17: the wiki's dated record puts this in **March 2025**, in the JELLYJELLY perp, where [[hlp|HLP]] absorbed a self-liquidated short and took a ~$13M paper loss before validators settled the market. See [[2025-03-jellyjelly-hlp-attack]]. It could not have been a HIP-3 market, because [[hip-3-builder-deployed-perps|HIP-3]] only activated in October 2025. See Contradictions below.)*
- **October 10-11, 2025:** the largest forced-liquidation event on record, with roughly $19-20B liquidated across Binance, Bybit, OKX and Hyperliquid. BTC fell ~$118K → ~$104K and alts fell much further as cross-margin collateral was marked down. ADL closed profitable hedge legs, so "delta-neutral" books took directional losses. See [[2025-10-crypto-liquidation-cascade]].

## Trading Relevance

Liquidation data and dynamics are central to several AlgoBrain strategies:

- **[[liquidation-cascade-arbitrage]]:** Actively hunts the post-cascade regime — entering counter-trend after a liquidation flush exhausts the forced selling. The core thesis is that the cascade overshoots fair value, creating a reversion opportunity.
- **[[contrarian-extremes]]:** Extreme liquidation volume is a component of the fear/panic signal. Large liquidation events often coincide with extreme Fear & Greed readings and deeply negative funding rates — the conditions the strategy targets.
- **[[funding-rate-arbitrage]]:** Liquidation cascades temporarily create very negative funding (remaining longs flee, shorts are overloaded), which is the exact condition that maximises the reward for a delta-neutral long-spot/short-perp carry position.
- **[[mev-execution-guide]]:** On-chain liquidations (Aave, Compound, MakerDAO) are one of the most reliable MEV opportunities. Searchers compete to be the first to trigger and capture the liquidation bonus (typically 5-10% of the collateral) paid by the protocol.
- **[[liquidation-price-aware-sizing]]:** The inverse use — sizing your *own* positions so that a named wick or vol spike cannot reach your liquidation price. This is a core position-sizing discipline in the [[multi-strategy-crypto-portfolio]].
- **[[on-chain-analysis]]:** CryptoDataAPI's liquidation data endpoints provide real-time and historical liquidation flows, which are useful as a proxy for local crowding and positioning extremes.

*Correction (2026-10-17):* the first bullet above describes [[liquidation-cascade-arbitrage]] as a counter-trend fade. That page is actually the **keeper/MEV** strategy: it captures the 5-13% liquidation bonus on lending protocols and on-chain perps. The counter-trend post-flush trade is [[liquidation-cascade-fade]]. The wider set of strategies that trade CEX/Hyperliquid liquidation flow:

| Strategy | How it uses liquidations |
|---|---|
| [[liquidation-cascade-fade]] / [[post-liquidation-rebound]] | Fade the overshoot after a long-liquidation flush |
| [[long-liquidation-cascade]] | Trade *with* the cascade while it is running |
| [[liquidation-density-magnet]] | Price is drawn toward dense resting liquidation bands |
| [[funding-flush-reversal]] / [[oi-flush-reversion]] | Liquidations reset funding and OI; enter after the reset |
| [[cross-venue-cascade-dislocation]] | Cascades hit venues unevenly, so cross-venue spreads open |
| [[cascade-monetization-rotation]] | Rotate post-cascade proceeds into the strongest rebounders |
| [[stop-hunting-and-liquidity-sweeps]] | Liquidity sweeps through stop and liquidation clusters |
| [[liquidation-price-aware-sizing]] | Defensive: keep your own liquidation price outside plausible wicks |

## Contradictions

> **Claim A** (Source: this page, pre-2026-10-17 text, confidence: LOW): the Hyperliquid HLP liquidation stress event was "Q4 2024" in "a thinly-traded HIP-3 perp".
> **Claim B** (Source: [[2025-03-jellyjelly-hlp-attack]], [[hyperliquid-vault-architecture]], confidence: MEDIUM): the event was JELLYJELLY in March 2025, with ~$13M HLP paper loss. [[hyperliquid-liquidation-engine]] also calls JELLYJELLY "a thin-liquidity HIP-3 listing".
> **Claim C** (Source: [[hyperliquid]], [[stock-perp-oracle-basis]], confidence: MEDIUM): HIP-3 activated in October 2025.
> **Resolution**: Claim B's date is favoured. Given Claim C, JELLYJELLY was a validator-listed core perp, not a HIP-3 market, so the "HIP-3" label on both this page and [[hyperliquid-liquidation-engine]] looks wrong. Pending a check of the Hyperliquid docs.

> **Claim A** (Source: [[volatility-trading]], confidence: MEDIUM): ~$19B liquidated on 2025-10-10.
> **Claim B** (Source: [[crypto-flash-crashes]], [[2025-10-crypto-liquidation-cascade]], confidence: MEDIUM): ~$20B liquidated.
> **Resolution**: Both figures are consistent with each other within rounding and differ in venue coverage. Since every public total undercounts Binance (see above), treat ~$19-20B as a floor.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/liquidations?symbol=BTC` — realized long/short liquidation USD over 1h/4h/12h/24h windows (OKX + Bybit + Hyperliquid; Binance geo-blocks its stream, so totals run *under* an all-exchange number)
- `GET /api/v1/market-intelligence/liquidations/by-exchange` — BTC trailing-4h split by venue
- `GET /api/v1/market-intelligence/squeeze-alerts?window_s=300&min_severity=0.5` — short-window squeeze/cascade alerts

**Historical data:**
- `GET /api/v1/backtesting/hl-liquidation-bars?coin=BTC&interval=15m&start=2026-01-01` — incremental Hyperliquid liquidation flow per bucket from exact fills (use this for burst detection)
- `GET /api/v1/backtesting/hl-liquidations?coin=BTC&start=2026-01-01` — the individual Hyperliquid liquidation fills
- `GET /api/v1/backtesting/liquidations?symbol=BTC&start=2026-01-01` — venue-merged **rolling-24h level** sampled every 5 minutes. Do not difference or sum consecutive rows to get flow.
- `GET /api/v1/backtesting/liquidation-density?coin=BTC&start=2026-07-01` — Hyperliquid liquidation density within ±0.5-5% of mark, split by trader type and leverage bucket (history from 2026-06-26)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations?symbol=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-market-intelligence]], [[cryptodataapi-backtesting]]. Backtest traps (rolling-level vs flow, venue coverage) are covered in [[crypto-perp-backtesting-pitfalls]].

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
