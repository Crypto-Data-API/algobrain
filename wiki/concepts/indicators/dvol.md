---
title: "DVOL — Deribit Volatility Index"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [crypto, options, volatility, indicators, derivatives, deribit, sentiment]
aliases: ["DVOL", "Deribit Volatility Index", "Crypto VIX", "BTC DVOL", "ETH DVOL"]
domain: [market-microstructure, options]
prerequisites: ["[[implied-volatility]]", "[[options]]"]
difficulty: intermediate
related: ["[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[volatility-regime]]", "[[crypto-options-volatility-selling]]", "[[vix]]", "[[variance-risk-premium]]", "[[gamma-exposure]]", "[[crypto-signal-library]]"]
---

**DVOL** (the **Deribit Volatility Index**) is the crypto market's equivalent of the [[vix|VIX]] — a 30-day forward-looking implied-volatility index for [[bitcoin|BTC]] and [[ethereum|ETH]], published by [[deribit|Deribit]] (the venue that clears the large majority of crypto options volume). It is the single most-cited gauge of the price of optionality in crypto, and the reference input for volatility regime detection, options premium-selling, and skew/vol-carry strategies across this wiki.

## Construction

DVOL is computed from the full [[deribit|Deribit]] options order book using a model-free, variance-swap-style integration across the strike surface (the same family of method as the VIX, adapted to crypto's expiry ladder), then interpolated to a constant **30-day** horizon and expressed in **annualised volatility points** (e.g. DVOL = 55 means ~55% annualised implied vol). Deribit publishes a live DVOL for BTC and ETH plus a historical DVOL candle series.

- **Model-free**: aggregates the whole listed strike surface rather than a single at-the-money quote, so it reflects the market-implied *variance* including skew and wings.
- **30-day constant maturity**: interpolated from the two bracketing listed expiries, so it is comparable through time.
- **Annualised vol points**: DVOL / √365 ≈ the implied 1-day move in %.

## How to read it

- **Level** — the outright price of 30-day vol. Historically BTC DVOL has ranged roughly from the high-20s (deep calm) to 130+ during shocks (COVID-March-2020, LUNA, FTX, the 2025-10-10 cascade). ETH DVOL typically prints a few points above BTC.
- **Percentile / rank** — because the *level* drifts with regime, most strategies gate on DVOL **percentile** over a trailing window (e.g. 1y) rather than the raw number — the crypto analogue of IV-rank. High percentile = options rich (favour selling); low percentile = options cheap (favour buying). See [[crypto-options-volatility-selling]] and [[iv-rank-and-iv-percentile]].
- **Term structure** — comparing DVOL to shorter/longer implied vol reveals contango (calm, carry-friendly) vs backwardation (stress, event-driven), which drives calendar and [[volatility-carry]] structures.
- **Vs realized** — DVOL minus trailing [[realized-volatility]] is the [[variance-risk-premium|variance risk premium]]: persistently positive, which is *why* systematic vol-selling has an edge (and why it blows up in the tail).

## Crypto specifics (vs the VIX)

- **24/7 & weekend gaps** — crypto trades continuously, so DVOL prices weekend gamma and holiday-thin liquidity that the equity VIX (market-hours) never faces.
- **Funding linkage** — perpetual [[funding-rate|funding]] and the [[options-skew|options skew]] co-move; crypto skew flips to *call*-skew in euphoric funding regimes, unlike equities' near-permanent put-skew, which changes DVOL's internal composition.
- **Two indices, thin alts** — liquid DVOL exists only for BTC and ETH; there is no deep listed-vol index for most alts, capping vol strategies to the majors.
- **No fear-only reading** — because crypto rallies can be as violent as sell-offs, a DVOL spike is not automatically "fear"; it can be melt-up gamma.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface are published by **Deribit** directly (and mirrored by [[greeks-live|Greeks.live]]) — CryptoDataAPI does **not** serve the DVOL index itself. CryptoDataAPI does provide the complementary volatility and options context:

**Live:**
- `GET /api/v1/volatility/regime/score` — market-wide volatility-stress composite (0–100)
- `GET /api/v1/volatility/regime/{symbol}` — per-asset volatility regime
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain
- `GET /api/v1/quant/gex` — dealer gamma exposure

**Historical:**
- `GET /api/v1/backtesting/klines` — price series to compute realized vol for the DVOL-minus-RV variance-risk-premium

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

For the DVOL index/history and full IV surface, use the Deribit API (`/api/v2/public/get_volatility_index_data`) or Greeks.live. See [[cryptodataapi-regimes]] and [[cryptodataapi-market-intelligence]].

## Trading applications

- **Regime gating** — DVOL percentile gates premium-selling (sell high, stand aside low): [[crypto-options-volatility-selling]], [[short-volatility-strategies]].
- **Vol timing** — buy convexity when DVOL is cheap ahead of catalysts (halving, ETF, unlocks): [[long-volatility-strategies]], [[crypto-options-dispersion]].
- **Carry** — term-structure shape drives [[volatility-carry]] and calendar structures.
- **Risk overlay** — a rising DVOL is a position-sizing and de-grossing signal for directional books ([[crypto-portfolio-heat]], [[funding-aware-position-sizing]]).

## Related

- [[deribit]] — the venue that computes and publishes DVOL
- [[greeks-live]] — third-party crypto options analytics / IV surface
- [[vix]] — the equity analogue
- [[volatility-regime]], [[variance-risk-premium]] — how DVOL feeds regime and premium
- [[crypto-signal-library]] — DVOL as a tradeable crypto signal

## Sources

- Deribit, "DVOL — Deribit Implied Volatility Index" methodology
- Greeks.live crypto options analytics
