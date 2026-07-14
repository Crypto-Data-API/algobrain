---
title: "Gamma Scalping (Concept)"
type: concept
created: 2026-04-22
updated: 2026-07-14
status: good
tags: [options, volatility, hedging, greeks, crypto]
aliases: ["Gamma Scalping", "Gamma Trading", "Long Gamma Scalping", "Volatility Scalping", "Delta-Neutral Gamma Trading"]
domain: [options, volatility]
prerequisites: ["[[options]]", "[[greeks]]", "[[gamma]]", "[[theta]]", "[[delta-hedging]]"]
difficulty: advanced
markets: [crypto, options]
related: ["[[gamma]]", "[[theta]]", "[[delta]]", "[[vega]]", "[[delta-hedging]]", "[[black-scholes-model]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[straddle]]", "[[deribit]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[dvol]]", "[[gamma-exposure]]"]
---

**Gamma scalping** is the long-volatility side of [[delta-hedging]]: a trader buys options (a long-[[gamma]] position, usually a [[straddle]] or strangle) and continuously delta-hedges the underlying, harvesting the realized price movement. It profits when the underlying's [[realized-volatility]] exceeds the [[implied-volatility]] paid for the options. This page is the **theory/concept** treatment (mechanism, math, Greeks, worked numbers, crypto grounding). For the delta-hedged options position it belongs to (the long-gamma configuration, construction, sizing), see [[delta-hedged-options]].

The name captures the mechanic: a long-gamma position gets **longer as price rises and shorter as it falls**, so hedging back to delta-neutral mechanically **sells high and buys low** in the underlying. Each scalp banks a small profit funded by the option's convexity; the daily cost is [[theta]].

## The gamma–theta engine

Every day, a delta-hedged long-gamma book earns from realized movement and pays theta:

> Daily P&L ≈ 0.5 · Γ · (realized move)² − Θ

Integrated over the trade, in continuous time:

> dP&L ≈ 0.5 · Γ · S² · (σ²_realized − σ²_implied) · dt + ν · dσ_implied

The first term is the realized-vs-implied variance bet (positive when [[realized-volatility]] beats the entry [[implied-volatility]]); the second is the mark-to-market [[vega]] P&L from IV changes. Because `0.5 · Γ · S² · σ²_implied · dt` **equals** the theta bleed under [[black-scholes-model|Black-Scholes]], gamma scalping is structurally a wager that realized variance exceeds implied — the exact inverse of a short-vol [[delta-hedging|delta-hedged]] book and the mirror image of harvesting the [[variance-risk-premium]].

## Greeks profile

A gamma scalp is **long gamma, long vega, short theta**, with delta managed to zero:

| Greek | Sign (long straddle) | Meaning here |
|-------|----------------------|--------------|
| [[delta]] (Δ) | ≈ 0, drifts | Flattened continuously by the scalp loop |
| [[gamma]] (Γ) | positive | The engine — convexity that lets you buy dips / sell rallies |
| [[theta]] (Θ) | negative | The rent paid per day; accelerates near expiry |
| [[vega]] (ν) | positive | Windfall if IV ([[dvol|DVOL]]) rises; a second loss if IV crushes |

Gamma peaks at-the-money and explodes near expiry; theta accelerates in tandem. The whole game is choosing tenor and hedge band so that captured gamma beats paid theta.

## Hedge-band selection

The most consequential implementation choice — identical machinery to [[delta-hedging#Hedging frequency: the core tradeoff]], opposite gamma sign:

| Method | Trigger | Trade-off |
|--------|---------|-----------|
| Fixed delta band | re-hedge when \|net Δ\| > X | cost-efficient; band must be re-tuned as Γ, vol change |
| Fixed time interval | every Δt | simple; misses fast moves, over-trades quiet tape |
| Fixed price grid | every k × expected move | captures swings symmetrically; whipsaw if mis-spaced |
| Whalley–Wilmott | band ∝ (cost/Γ)^(1/3) | asymptotically cost-optimal |

Wider bands capture larger swings but risk giving back accumulated delta on a reversal; tighter bands monetise chop but pay more spread (and, in crypto, more [[funding-rate|funding]] churn). Discrete hedging captures only the squared moves *at the hedge points*, introducing Boyle–Emanuel error ≈ 1/√N of premium for N hedges.

## Why it isn't free money

Unconditionally, implied vol exceeds realized most of the time — the [[variance-risk-premium]] runs *against* the long-gamma side. An always-on gamma-scalping program bleeds. The edge exists only **selectively**: pre-catalyst lulls where IV underprices a coming move, post-crush overshoots, or names/assets where realized persistently beats implied. Selectivity (cheap IV + a credible realized-vol catalyst inside the option's life) is the entire game.

## Worked example (BTC)

A trader buys a **30-day ATM BTC straddle** on Deribit at DVOL **45%** when their realized-vol forecast is **60%**, BTC at $60,000. Premium ≈ 0.8 · 60,000 · 0.45 · √(30/365) ≈ **$6,190** per BTC of notional, with daily theta of roughly $100–110/BTC early on.

The 45% DVOL implies a daily expected move of about 45%/√365 · $60,000 ≈ **$1,413** (calendar-day vol, because crypto trades 24/7). BTC then swings ~$2,500/day. Each time delta breaches the band, the trader hedges the [[perpetual-futures|perp]] — selling into rallies, buying dips — banking scalps that, at ~60% realized (60² = 3,600) versus 45% priced (45² = 2,025), run well above the theta paid. If DVOL also rises to 55% mid-trade, the positive vega adds a windfall on top of the gamma harvest. If instead BTC goes quiet (~$800/day) the theta grinds the premium away — the standard long-gamma death.

## Crypto specifics

### Long gamma loves 24/7 volatility and weekend gaps

Crypto's high realized vol and its **round-the-clock, weekend-inclusive** trading are structurally friendly to long gamma. Unlike equity options, where a weekend or overnight gap happens while the market is *closed* and cannot be scalped, crypto gaps happen live — a long-gamma scalper can hedge the move and bank it. Thin weekend books produce exactly the sharp, jumpy moves that long gamma monetises. The flip side: [[theta]] also accrues continuously, weekends included, so a quiet weekend still costs rent.

### Hedge with perps; funding is a carry line

Scalps are executed in **spot or [[perpetual-futures|perps]]** (deepest liquidity). Every perp hedge pays or receives **[[funding-rate|funding]]**, which becomes a running P&L line on top of spread and impact — a crypto-specific cost/credit absent in equity gamma scalping. Persistent positive funding while you carry net-long perp hedges is a drag to net against the gamma harvest.

### Inverse (coin) delta and DVOL

Deribit options are **inverse** (coin-margined): the coin delta they display must be converted to **cash/USD delta** before hedging, and the coin collateral itself carries delta (see [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]]). The implied vol you compare your realized forecast against is **[[dvol|DVOL]]**, Deribit's 30-day IV index (a Deribit/Greeks.live number, not on CryptoDataAPI) — buy gamma when DVOL is cheap relative to your realized-vol forecast and a catalyst sits inside the option's life.

### Dealer gamma (GEX) tells you when scalping pays

When Deribit market makers are **net short gamma** (negative [[gamma-exposure|GEX]]) they hedge *with* the move — buying rallies, selling dips — which **amplifies realized volatility**, precisely the environment a long-gamma scalper wants. When dealers are net long gamma they suppress vol, and long-gamma scalps struggle against theta. Reading aggregate dealer GEX is therefore a direct signal for when gamma scalping is likely to be paid.

## Getting the Data (CryptoDataAPI)

Gamma scalping is driven by realized-vs-implied vol, dealer positioning, and hedge carry:

- **Volatility regime — realized vs implied context** — `GET /api/v1/volatility/regime` and market-wide `GET /api/v1/volatility/regime/score` (compressed vol regimes flag when long gamma is cheap and coiled). See [[cryptodataapi-regimes]].
- **Dealer gamma (GEX)** — `GET /api/v1/quant/gex`; negative GEX = amplified realized vol = friendly to long gamma. See [[cryptodataapi-regimes]].
- **Funding — the perp-hedge carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC`. See [[cryptodataapi-derivatives]].

The IV surface and **DVOL** are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

## Related

- [[delta-hedged-options]] — the delta-hedged options structure (long-gamma configuration)
- [[delta-hedging]] — the shared hedging machinery; the short-vol mirror image
- [[gamma]], [[theta]], [[delta]], [[vega]] — the Greeks that drive the trade
- [[black-scholes-model]] — the gamma–theta identity; crypto/inverse pricing
- [[implied-volatility]], [[realized-volatility]] — the two vols the trade compares
- [[variance-risk-premium]] — the structural headwind to long-gamma trading
- [[straddle]] — the usual long-gamma structure
- [[deribit]] — the venue; inverse contracts and DVOL
- [[perpetual-futures]], [[funding-rate]] — the crypto hedge instrument and its carry
- [[dvol|DVOL]] — the implied-vol benchmark the trade bets against
- [[gamma-exposure]] — dealer positioning that shapes realized vol

## Sources

- Sinclair, E. (2013), *Volatility Trading* (2nd ed.), Wiley — gamma-scalping and hedge-band selection
- [[book-option-volatility-and-pricing]] — Natenberg on dynamic hedging and the gamma-theta trade-off
- Carr, P. & Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* — the headwind long gamma must overcome
- Deribit public documentation — inverse contract specs and the DVOL index
