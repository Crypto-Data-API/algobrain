---
title: "Delta-Hedged Options (Crypto)"
type: strategy
created: 2026-06-22
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, risk-management, bitcoin]
aliases: ["Delta-Hedged Options", "Delta-Neutral Options", "Volatility Isolation", "Crypto Delta-Hedged Options"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[delta-hedging]]", "[[gamma-scalping]]", "[[straddle]]", "[[strangle]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[deribit]]", "[[greeks-live]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[dvol]]", "[[gamma-exposure]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[cryptodataapi]]"]
---

# Delta-Hedged Options (Crypto)

## Overview

Delta-hedged options is the structure of holding an [[options]] position and continuously trading the underlying to keep net [[delta]] near zero, so the position's P&L is driven by **volatility (gamma) rather than direction**. Neutralizing delta isolates the gap between the **[[realized-volatility]]** the coin actually delivers and the **[[implied-volatility]]** ([[dvol|DVOL]]) embedded in the option price. It is the foundational structure of options market-making and volatility trading, and it has two configurations:

- **Long-gamma** (buy options, hedge delta) — profits when realized vol **exceeds** implied. This is [[gamma-scalping]].
- **Short-gamma** (sell options, hedge delta) — profits when realized vol stays **below** implied, harvesting the [[variance-risk-premium]].

Delta hedging is the shared *mechanism* (see the [[delta-hedging]] concept page for the math); this page treats the *structure* — the delta-hedged options position itself, how it is built, and its crypto specifics on [[deribit]] with [[perpetual-futures|perp]] hedging.

## Construction

1. **Choose the options leg**: a [[straddle]] or [[strangle]] for a vega-rich, gamma-heavy exposure; a single option or spread for a targeted one.
2. **Set the sign**: long the leg for long-gamma (RV > IV view); short the leg for short-gamma (IV > RV view / variance-premium harvest).
3. **Hedge to neutral at inception** by trading spot or, more commonly, the [[perpetual-futures|perp]].
4. **Re-hedge on a rule**: fixed time interval, fixed delta band (re-hedge when |Δ| exceeds a threshold), or fixed price grid. Tighter hedging cuts P&L variance but pays more cost — the central trade-off (see [[delta-hedging#Hedging frequency: the core tradeoff]]).
5. **Size to stressed gamma/vega**, not to expected carry — for short-gamma especially, cap notional so a multi-sigma weekend move is survivable.

## Payoff & breakevens

A delta-hedged options position has **no fixed payoff diagram** — it is a path-dependent bet on realized vs implied variance. In continuous time:

> dP&L ≈ 0.5 · Γ · S² · (σ²_realized − σ²_implied) · dt + ν · dσ_implied

- **Long gamma** (Γ > 0): profit when realized variance beats the implied variance paid — you *want* movement.
- **Short gamma** (Γ < 0): profit when implied beats realized — you *want* calm, and you collect the variance risk premium.

Because `0.5 · Γ · S² · σ²_implied · dt` equals the [[theta]] bleed under [[black-scholes-model|Black-Scholes]], the structure is a clean wager on which volatility wins over the holding period.

## Greeks profile

| Greek | Long-gamma | Short-gamma | Role |
|---|---|---|---|
| [[delta]] (Δ) | ≈ 0 | ≈ 0 | The thing neutralized (re-hedged via perp/spot) |
| [[gamma]] (Γ) | positive | negative | The engine (long) / the risk you're paid to bear (short) |
| [[theta]] (Θ) | negative | positive | The rent paid (long) / the carry collected (short) |
| [[vega]] (ν) | positive | negative | Windfall or loss when [[dvol|DVOL]] moves |

## Market view / when to use

- **Long-gamma** when DVOL is cheap versus a credible realized-vol catalyst inside the option's life — pre-event lulls, post-crush overshoots, or assets where realized persistently beats implied.
- **Short-gamma** when DVOL is rich and range-bound conditions look likely — harvesting the crypto variance risk premium, sized for the tail.
- The choice is a view on the implied-vs-realized spread; dealer positioning ([[gamma-exposure|GEX]]) tells you which realized-vol environment your hedge will trade into.

## Adjustments & management

- **Re-tune the band** as gamma and vol change — widen it as spreads/funding churn rise, tighten it as gamma rises (Whalley–Wilmott asymptotics).
- **Roll** to keep gamma alive if the thesis persists; **close** when the vol view is realized or the catalyst passes.
- **Short-gamma tail guard**: cut fast on a DVOL spike before negative gamma compounds — the weekend/expiry hours are the danger window.

## Crypto specifics

- **Hedge with perps; funding is a live P&L line.** Delta is flattened in spot or, usually, the [[perpetual-futures|perpetual future]] (deepest liquidity, easy shorting). Every perp hedge pays or receives **[[funding-rate|funding]]** — the crypto analogue of equity financing/borrow. A short-gamma book that ends up net-long the perp pays funding when funding is positive (crowded longs); net-short earns it. Funding must sit in the cost model alongside spread and impact, not as an afterthought.
- **Inverse (coin) delta.** Deribit's flagship BTC/ETH options are coin-margined — the delta shown is a **coin delta** and must be converted to **cash (USD) delta** before hedging, and the coin collateral itself carries delta. Mis-reading coin delta as cash delta systematically mis-sizes the hedge. See [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]].
- **24/7 hedging, thin weekends.** Crypto never closes, so hedging is genuinely continuous (closer to the Black-Scholes ideal). But weekend liquidity is thin — re-hedging is most expensive exactly when short-gamma books are most exposed, and around 08:00 UTC Deribit expiries.
- **DVOL is the residual-vega benchmark.** After hedging delta, the live exposure is to [[dvol|DVOL]] — monitored the way an equity desk watches the VIX (a Deribit / [[greeks-live]] number, **not** on CryptoDataAPI).
- **Dealer gamma shapes your slippage.** When Deribit market makers are net short gamma they hedge *with* the move (amplifying realized vol — friendly to long gamma); net long, they suppress it. Aggregate [[gamma-exposure|GEX]] predicts the very realized-vol environment your hedge trades into.
- **Liquidity cliff beyond BTC/ETH.** Alt-coin option books are thin; hedge slippage and wide option spreads cap size quickly outside BTC/ETH.

## Risks

- **Short-gamma tail** — a vol spike (weekend gap, exchange/stablecoin shock, leverage flush) with negative gamma realizes the full convexity loss with no chance to re-hedge.
- **Cost bleed** — over-frequent hedging pays spread, impact, and funding on noise; the re-hedge frequency is the key cost lever.
- **Long-gamma carry drag** — theta plus funding grind the position when realized vol disappoints.
- **Inverse-delta mis-hedge** — treating coin delta as cash delta.
- **Operationally demanding** — continuous monitoring and re-hedging, 24/7.

## Worked crypto example

**Setup (illustrative, long-gamma).** BTC $60,000; a trader buys a **30-day ATM straddle** on Deribit at DVOL **45%** (premium ≈ $6,190/BTC) while forecasting ~60% realized. 45% DVOL implies a daily expected move of ≈ 45%/√365 · $60,000 ≈ **$1,413** (calendar-day vol — crypto trades 24/7).

BTC then swings ~$2,500/day. Each time delta breaches the band, the trader hedges the [[perpetual-futures|perp]] — selling rallies, buying dips — banking scalps that at ~60% realized (60² = 3,600) versus 45% priced (45² = 2,025) run well above the theta paid. If DVOL also rises to 55% mid-trade, positive vega adds a windfall. If instead BTC goes quiet (~$800/day), theta plus any funding drag grinds the premium away — the standard long-gamma death. A **short**-gamma desk would have the mirror outcome: profit in the quiet tape, loss in the $2,500/day chop.

## Getting the Data (CryptoDataAPI)

A delta-hedged crypto book is priced by three streams — funding (hedge carry), vol regime (the IV-vs-RV edge), and dealer gamma (the hedging-flow environment):

- **Funding — the perp-hedge carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC`. See [[cryptodataapi-derivatives]].
- **Volatility regime — is realized vol likely to beat implied?** — `GET /api/v1/volatility/regime` and `GET /api/v1/volatility/regime/score`. See [[cryptodataapi-regimes]].
- **Dealer gamma (GEX) — hedging-flow environment** — `GET /api/v1/quant/gex` (market-maker inventory + liquidation profile). See [[cryptodataapi-regimes]].

The IV surface and **DVOL** are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

## Related

- [[delta-hedging]] — the shared hedging mechanism and its math
- [[gamma-scalping]] — the long-gamma configuration of this structure
- [[straddle]] / [[strangle]] — the usual vega-rich options legs
- [[implied-volatility]] / [[realized-volatility]] — the priced-vs-delivered vol this structure isolates
- [[variance-risk-premium]] — what the short-gamma configuration harvests
- [[deribit]] / [[greeks-live]] — venue, inverse settlement, DVOL, analytics
- [[perpetual-futures]] / [[funding-rate]] — the crypto hedge instrument and its carry
- [[dvol]] — the residual-vega benchmark
- [[gamma-exposure]] — dealer positioning that shapes realized vol
- [[delta]] / [[gamma]] / [[theta]] / [[vega]] — the Greeks managed and left on

## Sources

- Black, F. & Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy* — the replication argument
- Boyle, P. & Emanuel, D. (1980), "Discretely Adjusted Option Hedges", *Journal of Financial Economics* — discrete hedging error
- Carr, P. & Wu, L. (2009), "Variance Risk Premiums", *Review of Financial Studies* — the variance risk premium
- Deribit / [[greeks-live]] documentation — inverse contract specs, coin-Greeks, DVOL
