---
title: "HODL Waves"
type: concept
created: 2026-06-24
updated: 2026-07-13
status: draft
tags: [indicators, bitcoin, behavioral-finance]
aliases: ["HODL Waves", "hodl-waves", "HODL Wave", "Realized Cap HODL Waves", "RHODL"]
domain: [indicators]
prerequisites: ["[[on-chain-analysis]]", "[[bitcoin]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[on-chain-analysis]]"
  - "[[realized-price]]"
  - "[[mvrv]]"
  - "[[nupl]]"
  - "[[exchange-netflow]]"
  - "[[bitcoin]]"
  - "[[glassnode]]"
---

# HODL Waves

**HODL Waves** are an [[on-chain-analysis|on-chain]] visualization that breaks a coin's circulating supply into **age bands** — groups of coins defined by how long it has been since they last moved on-chain. Stacked as a colour-coded chart over time, the bands form "waves" that show how supply rotates between recently moved coins (younger, more speculative) and long-dormant coins (older, conviction holders). The name comes from the crypto term "HODL" (hold on for dear life), and the metric is primarily used for [[bitcoin]] to gauge accumulation versus distribution and the behaviour of long-term holders.

## How It Works

Every coin (more precisely, every unspent output) carries a timestamp of when it last moved. HODL Waves cohort the entire supply by that **coin age**:

1. **Age bands** — supply is bucketed into ranges such as <1 day, 1 day–1 week, 1 week–1 month, 1–3 months, 3–6 months, 6–12 months, 1–2 years, 2–3 years, 3–5 years, 5+ years (exact bands vary by provider; see [[glassnode]]).
2. **Stacked share** — each band is expressed as a *percentage of total supply* and stacked, so the chart always sums to 100%. The thickness of each band is the fraction of supply in that age cohort at that moment.
3. **Movement = reset** — when coins transact, they drop back into the youngest band; if they then sit untouched, they gradually "age up" through the bands, producing the rolling-wave appearance.

A common simplification splits supply into **long-term holders (LTH)** and **short-term holders (STH)** using an age threshold (often around 155 days), the age past which coins have historically had a low probability of being spent.

### Realized Cap HODL Waves (RHODL)

The standard HODL Waves weight each coin equally by *count*. The **Realized Cap HODL Waves** variant instead weights each age band by its **realized value** — each coin valued at the price when it last moved (its on-chain cost basis; see [[realized-price]] and the realized-cap discussion in [[on-chain-analysis]]). This shifts emphasis toward the *economic* weight of each cohort rather than raw coin count, and underlies derivative ratios (e.g. the RHODL ratio comparing younger-cohort to older-cohort realized value) used as cycle-timing signals.

## How Traders Use It

- **Accumulation vs distribution** — a **thickening of older bands** means coins are sitting still and ageing up: long-term holders are accumulating / refusing to sell (often read as a bullish supply backdrop). A **swelling of the youngest bands** means dormant coins are being re-activated and changing hands — classic late-cycle distribution from old holders to new buyers.
- **Cycle context** — historically, old-coin bands expand through bear markets (patient holders accumulate) and contract near cycle tops (old hands distribute into euphoria). RHODL-style ratios formalize this into a single overheating/undervaluation gauge.
- **Confluence** — HODL Waves are typically read alongside [[mvrv]], [[nupl]], and [[exchange-netflow]] to confirm whether holder behaviour and flow agree on the regime (see [[on-chain-analysis]]).

## Illustrative Example

Imagine a long, quiet bear market. On the HODL Waves chart, the older bands (1–2 years, 2–3 years, 5+ years) steadily thicken as coins bought earlier sit unmoved and age up — a visual signature of accumulation by conviction holders. Later, as price rallies sharply, those same old bands begin to *thin* while the <1-month bands balloon: long-dormant coins are waking up and being spent into strength, a distribution pattern that has historically clustered near cycle peaks. (Schematic — real band shifts are gradual and noisy.)

## Limitations and Pitfalls

- **Interpretation layer, not raw truth** — like all entity-flavoured on-chain metrics, age cohorts and LTH/STH labels are constructed by analytics providers; thresholds are conventions, not chain facts (see the data-caveat discussion in [[on-chain-analysis]]).
- **Self-transfers and re-org of holdings** — moving coins between one's own wallets, consolidating UTXOs, or exchange internal management resets coin age without any real change in ownership, distorting the youngest bands.
- **Lost coins inflate old bands** — provably lost or forgotten coins never move, so they permanently swell the oldest cohorts and overstate "diamond-hand" conviction.
- **Lagging and slow** — band shifts unfold over weeks to months; HODL Waves describe structural supply dynamics, not short-term timing.
- **Asset coverage** — most mature for Bitcoin's UTXO model; account-based chains and exchange-custodied supply complicate age attribution.

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

- [[on-chain-analysis]]
- [[realized-price]]
- [[mvrv]]
- [[nupl]]
- [[exchange-netflow]]
- [[bitcoin]]
- [[glassnode]]

## Sources

General market knowledge; no specific wiki source ingested yet.
