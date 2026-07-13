---
title: "MVRV Ratio"
type: concept
created: 2026-06-24
updated: 2026-07-13
status: draft
tags: [crypto, bitcoin, indicators, valuation, market-microstructure, behavioral-finance]
aliases: ["MVRV", "Market Value to Realized Value", "MVRV Ratio", "market-value-to-realized-value"]
domain: [market-microstructure]
prerequisites: ["[[on-chain-analysis]]", "[[realized-price]]"]
difficulty: intermediate
related: ["[[realized-price]]", "[[mvrv-z-score]]", "[[nupl]]", "[[sopr]]", "[[on-chain-analysis]]", "[[market-capitalization]]", "[[bitcoin]]", "[[market-cycle]]", "[[glassnode]]", "[[cryptoquant]]", "[[behavioral-finance]]", "[[cryptodataapi]]"]
---

The **MVRV Ratio** (Market Value to Realized Value) is an on-chain [[on-chain-analysis|valuation metric]] that divides an asset's [[market-capitalization|market cap]] by its [[realized-price|realized cap]]. Because realized cap values every coin at the price it last moved (its aggregate on-chain cost basis), MVRV measures how far the current market price has stretched above or below the average price the supply was acquired at — making it a proxy for the **aggregate unrealized profit or loss** held across all holders. It is one of the most widely cited [[bitcoin]] cycle-valuation tools, popularised by analytics platforms such as [[glassnode]] and [[cryptoquant]].

## How It Is Computed

```
MVRV = Market Cap / Realized Cap
```

- **Market Cap** = current price × circulating supply — what the supply is worth *today*.
- **[[realized-price|Realized Cap]]** = Σ (each coin valued at the price it last moved on-chain) — what the supply *cost*, in aggregate. See [[realized-price]] for the full construction.

Conceptually, MVRV is the ratio of "current value" to "cost basis." An MVRV of 2.0 means the market is, on average, holding roughly 2× the price it paid — substantial aggregate unrealized profit. An MVRV of 1.0 means the market in aggregate is at break-even (price equals average cost basis). An MVRV below 1.0 means the average holder is underwater.

A common refinement is **Short-Term Holder (STH) MVRV** and **Long-Term Holder (LTH) MVRV**, which restrict the calculation to coins younger or older than a dormancy threshold (commonly ~155 days), separating recent speculators from seasoned holders.

## Interpretation / How Traders Use It

MVRV is read as an over/undervaluation oscillator across a [[market-cycle]]:

- **High MVRV** (large multiples of cost basis): the supply carries heavy unrealized profit, which historically raises distribution risk — holders are increasingly incentivised to take gains. Elevated readings have *qualitatively* coincided with overheated, late-cycle conditions.
- **MVRV near 1.0**: price is meeting the aggregate cost basis. This zone is often watched as a pivot — the [[realized-price]] frequently acts as support in uptrends and resistance in downtrends.
- **Low / sub-1.0 MVRV**: the average holder is at a loss. Deeply depressed readings have *historically* aligned with capitulation phases and cycle-low accumulation zones, though no fixed numeric threshold is reliable across cycles.

Traders rarely use MVRV as a standalone trigger; it is typically combined with [[sopr]] (are coins actually being spent at a profit/loss?), [[nupl]] (the same profit/loss expressed as a percentage), and flow metrics like [[exchange-netflow]] to confirm whether paper gains are being realised. The standardised cousin [[mvrv-z-score]] rescales MVRV to flag statistical extremes more cleanly.

## Illustrative Example

Suppose [[bitcoin]] has a market cap reflecting a current price well above the average price at which the supply last moved, so realized cap is roughly half of market cap. MVRV would read about 2.0: the aggregate holder base sits on substantial unrealized profit, signalling an environment where profit-taking pressure tends to build. If price later falls back toward the realized price, MVRV compresses toward 1.0 and the market approaches its aggregate break-even — a zone analysts watch for either a defended support bounce or a break into holder-loss territory.

## Limitations and Pitfalls

- **Lagging in fast moves**: MVRV is a *valuation* gauge, not a timing trigger. It can stay elevated or depressed for extended periods; extremes describe risk, not exact tops/bottoms.
- **Lost and dormant supply**: realized cap (the denominator) assumes coins reflect a real cost basis, but provably lost coins, burned coins, and ancient dormant supply distort the aggregate. This biases the cost basis downward and can inflate MVRV.
- **Exchange and entity adjustments**: internal exchange transfers and custodial reshuffles can move coins without a genuine change of ownership, polluting the "last-moved price." Entity-adjusted variants attempt to strip these, but the label layer is provider-produced and revised over time (see [[on-chain-analysis#Leading vs Lagging, and Data Caveats]]).
- **Cross-cycle threshold drift**: the MVRV levels that marked tops and bottoms in earlier cycles have not repeated precisely; market maturation, ETFs, and institutional custody shift the bands. Treat historical zones qualitatively, never as fixed lines.
- **Asset specificity**: MVRV is best understood for [[bitcoin]] and large-cap assets with deep, mature on-chain data; for thin or newer chains the realized cap is noisier and the signal weaker.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — CEX inflow/outflow (1h/6h/24h/7d, per-exchange breakdown)
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — stablecoin dry-powder z-score signal
- `GET /api/v1/on-chain/miners/reserves` — BTC miner pool reserves + flows
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (capitulation/recovery/normal)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + supply-shock zone classification
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100)

**Historical data:**
- `GET /api/v1/on-chain/whale-score/{symbol}` — whale accumulation score timeseries
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin market-cap timeseries

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]].

## Related

- [[realized-price]] — Realized cap is the denominator of MVRV
- [[mvrv-z-score]] — Standardised version that flags statistical extremes
- [[nupl]] — Same unrealized profit/loss expressed as a percentage of market cap
- [[sopr]] — Whether coins are actually spent at a profit or loss
- [[on-chain-analysis]] — Parent mechanics page for on-chain metrics
- [[market-cycle]] — The cycle structure MVRV is read against
- [[market-capitalization]] — The numerator of MVRV
- [[glassnode]], [[cryptoquant]] — Providers that popularised the metric

## Sources

General market knowledge; no specific wiki source ingested yet.
