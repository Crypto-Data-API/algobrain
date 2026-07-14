---
title: "Delta Hedging (Concept)"
type: concept
created: 2026-04-22
updated: 2026-07-14
status: good
tags: [options, derivatives, risk-management, volatility, crypto]
aliases: ["Delta Hedging", "Delta Neutral Hedging", "Dynamic Hedging", "Delta Neutral", "Delta Hedge", "delta-hedge"]
domain: [options, risk-management]
prerequisites: ["[[options]]", "[[greeks]]", "[[delta]]", "[[gamma]]", "[[black-scholes-model]]"]
difficulty: advanced
markets: [crypto, options]
related: ["[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[black-scholes-model]]", "[[gamma-scalping]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[deribit]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[dvol]]", "[[gamma-exposure]]"]
---

**Delta hedging** is the continuous adjustment of a position in the underlying to offset the directional exposure ([[delta]]) of an options position, holding the book delta-neutral. It is the mechanical foundation of options [[market-making]], [[gamma-scalping]], and every volatility-trading strategy: by stripping out direction, the hedger isolates exposure to volatility and time, so the residual P&L is a clean bet on [[implied-volatility|implied]] vs [[realized-volatility|realized]] vol. This page is the **theory/concept** treatment (mechanism, math, the Greeks, worked numbers, crypto grounding). For the buildable strategy — edge classification, backtest status, capacity, and kill-criteria — see the [[delta-hedging]] strategy page.

Strictly, delta hedging is a *technique*, not an edge. Applied to a fairly priced option with frictionless continuous hedging, its expected P&L is exactly zero; after costs it is negative. The edge lives entirely in the implied-vs-realized vol spread that hedging isolates (most commonly the short side of the [[variance-risk-premium]]).

## The mechanism

An option's [[delta]] is its price sensitivity to a $1 move in the underlying: `Δ = ∂C/∂S`, equal to `N(d1)` for a call under [[black-scholes-model|Black-Scholes]]. A trader long 10 BTC calls at delta 0.50 has an effective long position of 5 BTC. To neutralize it, they sell 5 BTC (spot or perp), bringing net delta to zero.

Delta is not constant — it changes as spot moves, and the rate of change is [[gamma]] (`Γ = ∂²C/∂S²`). So the hedge must be rebalanced continuously:

- Spot rises → call delta rises (say 0.50 → 0.60) → **sell more** underlying to re-flatten.
- Spot falls → call delta falls (0.50 → 0.40) → **buy back** underlying.

For a **long-gamma** book (bought options) each re-hedge sells high / buys low, locking in a small profit — this is [[gamma-scalping]]. For a **short-gamma** book (sold options) each re-hedge buys high / sells low, locking in a small loss — the price of collecting [[theta]] and the [[variance-risk-premium]].

## The P&L identity

The delta-hedged P&L of an option, in continuous time, reduces to a variance bet plus a mark-to-market vega term:

> dP&L ≈ 0.5 · Γ · S² · (σ²_realized − σ²_implied) · dt + ν · dσ_implied

- **Long-gamma** (Γ > 0): profit when realized variance exceeds the implied variance paid — you *want* movement.
- **Short-gamma** (Γ < 0): profit when implied variance exceeds realized — you *want* calm, and you collect the variance risk premium.

Because `0.5 · Γ · S² · σ²_implied · dt` equals the [[theta]] bleed under Black-Scholes, delta hedging turns an option into a pure wager on realized vs implied variance over the holding period.

## Residual Greeks

Delta hedging targets one Greek and deliberately leaves the others on. For the canonical **short-vol** hedged book (sell options, hedge delta):

| Greek | Sign | Role |
|-------|------|------|
| [[delta]] (Δ) | held ≈ 0 | The thing neutralized |
| [[gamma]] (Γ) | negative | The risk you are paid to bear |
| [[theta]] (Θ) | positive | The carry collected |
| [[vega]] (ν) | negative | Loss if [[implied-volatility|IV]] (crypto: [[dvol|DVOL]]) spikes |

Higher-order desks also flatten gamma and vega (see [[vega-hedging]]), accepting more transaction cost for a tighter "Greeks-flat" book.

## Hedging frequency: the core tradeoff

More frequent hedging keeps the book closer to neutral but pays more [[transaction-costs|transaction costs]] (spread, impact, and — in crypto — [[funding-rate|funding]]). Less frequent hedging saves cost but lets directional risk accumulate between rebalances. The canonical rebalancing schemes:

| Method | Trigger | Cost | P&L variance |
|--------|---------|------|--------------|
| Time-based | Fixed Δt (hourly, EOD) | Predictable, often higher | Lower if interval short |
| Threshold (move) | \|net Δ\| > band | Cheaper — trades only when needed | Higher between hedges |
| Whalley–Wilmott | band ∝ (cost/\|Γ\|)^(1/3) | Asymptotically cost-optimal | Balanced |
| Zakamouline | band scales with risk aversion + cost | Practical extension | Tunable |

The optimal band **widens with transaction costs and narrows with gamma**: hedge a high-gamma book tightly, a low-gamma book loosely, and always loosen as spreads widen. With N discrete hedges, the terminal hedging error is a zero-mean random variable with standard deviation ≈ 1/√N of the option premium (Boyle–Emanuel, 1980) — so even a correct vol view produces noisy month-to-month results.

## Worked example (BTC, short-vol)

A desk sells a **30-day ATM BTC straddle** on Deribit with DVOL at **60%** while its realized-vol forecast is **45%**, BTC at $60,000. Straddle premium ≈ 0.8 · 60,000 · 0.60 · √(30/365) ≈ **$8,254** per BTC of notional. The straddle starts ≈ delta-neutral, so no opening hedge.

Over the next weeks BTC chops between $57k and $63k. Each time net delta breaches the band, the desk re-flattens by trading the [[perpetual-futures|perp]] — buying after dips, selling after rallies, each re-hedge locking in a small loss (short gamma) but far smaller than the theta collected. If realized vol comes in near 45% versus the 60% sold, the desk buys back the straddle having captured most of the ~15-vol-point spread, net of hedging costs *and* the funding paid/received on the perp hedge (the crypto-specific carry line, below). Had DVOL instead spiked to 90% mid-trade, the negative vega would have inflicted a large mark-to-market loss even before any realized move — the short-gamma death.

## Crypto specifics

### Hedging with perps and spot, not stock

Crypto delta hedges are executed in **spot or, more commonly, [[perpetual-futures|perpetual futures]]** (deepest liquidity, no expiry, easy shorting). This is the single biggest practical difference from equities: the hedge instrument is itself a derivative that pays or charges **[[funding-rate|funding]]** every few hours. Funding is the crypto analogue of equity financing/borrow cost:

- A **short-vol, short-gamma** book that ends up net *long* the perp hedge pays funding when funding is positive (crowded longs) — a persistent drag that must be added to the cost model alongside spread and impact.
- Conversely, negative funding pays you to hold the hedge. Funding can swing from a credit to a large drag, so a crypto delta-hedger treats funding as a live P&L line, not an afterthought.

### Inverse (coin-margined) delta

Deribit's standard options are **inverse** — coin-denominated. The delta Deribit shows is a coin delta; it must be converted to **cash (USD) delta** before hedging, because an inverse option's USD delta differs from the naive Black-Scholes number (the payoff currency moves with spot). Two consequences:

- The **coin collateral itself is a delta**: holding BTC as margin means your account carries long-BTC exposure that has to be counted in the net hedge.
- Mis-reading coin delta as cash delta systematically mis-sizes the hedge — a classic crypto rookie error. See [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]].

### 24/7 hedging, weekend gaps, and DVOL

- Crypto **never closes**, so hedging is genuinely continuous — closer to the Black-Scholes ideal than equities (no closed overnight session to gap through). But **weekend liquidity is thin**: books widen, moves get jumpy, and re-hedging is most expensive exactly when you most need it. Short-gamma books are most exposed on weekends and around 08:00 UTC Deribit expiries.
- The residual vega after hedging is exposure to **[[dvol|DVOL]]**, the crypto vol benchmark — a crypto delta-hedger monitors DVOL the way an equity desk watches the VIX (DVOL is a Deribit/Greeks.live number, not on CryptoDataAPI).
- **Dealer gamma matters to your slippage**: when Deribit market makers are net short gamma they hedge *with* the move (amplifying vol), when net long they hedge *against* it (suppressing vol). Their aggregate positioning ([[gamma-exposure|GEX]]) predicts the very realized-vol environment your hedge trades into.

## Getting the Data (CryptoDataAPI)

A delta-hedged crypto book is priced by three data streams — funding (hedge carry), vol regime (the IV-vs-RV edge), and dealer gamma (the hedging-flow environment):

- **Funding — the perp-hedge carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (cross-exchange) and `GET /api/v1/derivatives/binance/funding-rates`. See [[cryptodataapi-derivatives]].
- **Volatility regime — is realized vol likely to beat implied?** — `GET /api/v1/volatility/regime` and market-wide `GET /api/v1/volatility/regime/score`. See [[cryptodataapi-regimes]].
- **Dealer gamma (GEX) — hedging-flow environment** — `GET /api/v1/quant/gex` (market-maker inventory + liquidation profile). See [[cryptodataapi-regimes]].

The IV surface and **DVOL** are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/gex"
```

## Related

- [[delta-hedging]] — the strategy build-out (edge, backtest, capacity, kill-criteria)
- [[delta]], [[gamma]], [[theta]], [[vega]] — the Greeks this book targets and leaves on
- [[black-scholes-model]] — the replication argument that justifies delta hedging; crypto/inverse pricing
- [[gamma-scalping]] — the long-gamma mirror image of the short-vol hedged book
- [[vega-hedging]] — the next-order hedge beyond delta
- [[implied-volatility]], [[realized-volatility]] — what delta-hedging P&L depends on
- [[variance-risk-premium]] — the premium most short-vol hedged books harvest
- [[deribit]] — the venue; inverse contracts and the DVOL benchmark
- [[perpetual-futures]], [[funding-rate]] — the crypto hedge instrument and its carry
- [[dvol|DVOL]] — the residual-vega benchmark
- [[gamma-exposure]] — dealer positioning that shapes the realized-vol environment

## Sources

- Black, F. & Scholes, M. (1973), "The Pricing of Options and Corporate Liabilities", *Journal of Political Economy*
- Boyle, P. & Emanuel, D. (1980), "Discretely Adjusted Option Hedges", *Journal of Financial Economics* — discrete hedging error
- Leland, H. (1985), "Option Pricing and Replication with Transactions Costs", *Journal of Finance*
- Taleb, N. N. (1997), *Dynamic Hedging* — real-world hedging frictions
- Deribit public documentation — inverse contract specs and coin-Greeks
