---
title: "Christmas Tree Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, bitcoin, ethereum]
aliases: ["Ladder Spread", "Christmas Tree", "Call Ladder", "Put Ladder", "Crypto Christmas Tree"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[butterfly-spread]]", "[[broken-wing-butterfly]]", "[[ratio-spread]]", "[[jade-lizard]]", "[[iron-condor]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Christmas Tree Spread

## Overview

The christmas tree spread — also called a **ladder spread** — uses options at three (or more) strikes in a ladder-like progression to express a **moderate directional** view at very low cost. The classic call christmas tree **buys 1 ATM call, sells 1 OTM call, and sells 1 further-OTM call**, financing a directional long into a target zone. The name comes from the peaked, narrowing shape on a risk graph. It profits from a controlled move *to* the first short strike, but the second (uncovered) short creates **open-ended risk beyond the outer strike** — a critical hazard in a 24/7, gap-prone crypto market.

On [[deribit]] BTC/ETH, the christmas tree is a cheap way to say "I expect a move to roughly level X but not far beyond." Unlike the [[butterfly-spread]] (defined risk both sides) or the [[jade-lizard]] (capped one side), the naked outer short means this structure carries a genuine **tail** that the crypto tape can hit — which is why strike placement and hard stops matter more here than in equities.

## Construction

Three strikes, three legs (a ladder), one expiry, cash-settled:

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Buy 1 call | ATM (K0) | directional long |
| 2 | Sell 1 call | OTM (K1, e.g. +$8k-$12k on BTC) | first short (finances the long) |
| 3 | Sell 1 call | further OTM (K2, e.g. +$18k-$22k) | second short (uncovered) |

- **Strike selection:** long ATM; the two shorts placed at the target zone and beyond. Strikes need not be equally spaced, though equal spacing is common. A **put christmas tree** mirrors this for a bearish view.
- **Ratios:** 1 long : 2 short (net short one extra option — the source of the uncovered tail).
- **Net cost:** small **debit or near-zero** — the two shorts largely finance the long.
- **Tenor:** 30-60 DTE so the directional move has time to arrive.

## Payoff & breakevens

For the call christmas tree (long K0, short K1, short K2, small net debit d):

- **Max profit** = (K1 − K0) − d, on a settle at the first short strike K1 (extends as a plateau from K1 to K2).
- **Downside max loss** = the net debit d, if price does not move (all calls expire worthless).
- **Upside tail (beyond K2):** losses **escalate $1-for-$1** past the upper breakeven — one uncovered short call. This is naked-short exposure.
- **Lower breakeven** = K0 + d.
- **Upper breakeven** = K2 + max profit (approx.); above it, open-ended loss.

The graph rises from a small loss (no move) to a wide profit plateau between K1 and K2, then turns down through the upper breakeven into escalating loss — the "tree" that keeps falling on the far side.

## Greeks profile

- **Delta:** **directional** at entry (long the ATM call → net long delta for a call tree); it flips negative once price runs past the shorts into the naked region.
- **Gamma:** long near the ATM strike early, turning **increasingly negative** past the shorts — and dangerously so beyond K2 where the uncovered short dominates near expiry.
- **Theta:** mixed early; **positive** once price sits inside the K1-K2 profit plateau (net short two options there).
- **Vega:** roughly **negative** overall (net short two options); a DVOL spike while price is in the naked region is doubly painful.

## Market view / when to use

- You expect a **moderate, bounded move** to a specific target zone — not a runaway trend, not a range.
- You want a **very cheap or free** directional expression and will accept a capped downside (the debit) plus a monitored tail.
- **Moderate-to-elevated DVOL** so the two shorts finance the long — but you must be confident the move *stops* in the plateau.
- You have a strong view on a ceiling/floor (a resistance level, an OI wall) beyond which you do not expect price to travel.

## Adjustments & management

- **Profit target:** close at **50-75% of max profit** when price is in the K1-K2 plateau. Do not hold the uncovered short into expiry-week gamma.
- **Hard stop on the tail:** if price blows **through K2 with momentum**, close immediately — beyond this point losses accelerate like a naked short. This stop is non-negotiable in crypto.
- **No move:** if the catalyst passes and price sits below K0, accept the small debit loss; do not roll indefinitely.
- **Buy back the outer short** (convert to a [[butterfly-spread]] or [[broken-wing-butterfly]]) to cap the tail if you want to hold through an event.
- **Roll out** in time only if the moderate-move thesis is intact but slow.

## Crypto specifics

- **The uncovered short is the crypto hazard.** Equities have a close each day; **crypto trades 24/7 and gaps on weekends**, so a melt-up (or, for a put tree, a liquidation cascade) can blow through K2 at 03:00 UTC with the naked short fully exposed and no chance to react. Treat the tail as real: size small, set alerts, and prefer converting to a defined-risk fly before major catalysts.
- **Venue & underlyings:** [[deribit]] BTC/ETH only — the ladder needs strike granularity and depth; **alt options are too thin** and their gap risk on the naked leg is worse.
- **Inverse vs linear/USDC settlement:** use **USDC-margined (linear)** so the debit, plateau, and breakevens are clean USD; inverse (coin-margined) distorts the ladder and worsens wrong-way risk on the naked leg.
- **Portfolio-margin blow-up risk:** the uncovered short consumes Deribit **portfolio margin that balloons in a DVOL spike** — the classic short-gamma margin spiral, sharper in crypto. A gap toward the naked leg can force-liquidate the position at the worst tick.
- **DVOL regime:** moderate-to-elevated DVOL funds the shorts; but selling naked convexity into a DVOL that then spikes is the losing setup — the naked leg's vega and gamma both turn against you.
- **No [[section-1256-contracts|§1256]]:** gains and the naked-leg P&L are ordinary capital-gains events on offshore Deribit — no 60/40 US shelter; record-keeping across legs is onerous.
- **Cash settlement (08:00 UTC):** removes single-stock-style assignment/pin risk, but does **not** remove the economic tail of the uncovered short.
- **Perp funding / dealer gamma:** heavy dealer short-gamma above spot makes a melt-up cascade more likely — a warning for a call tree's naked upper leg. Funding-driven call skew makes the shorts richer (better financing) but also flags a crowded long-perp book that can squeeze.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$108,000**; you expect a rally to ~**$118,000** on ETF-flow momentum but not beyond ~$128,000; DVOL **46**. 40 DTE. Call christmas tree.

**Trade (per 1-BTC contract):**
- Buy 1 $108,000 call for **$6,500**.
- Sell 1 $118,000 call for **$3,200**.
- Sell 1 $128,000 call for **$1,600**.
- **Net debit = $6,500 − $3,200 − $1,600 = $1,700 = downside max loss.**
- **Max profit = ($118,000 − $108,000) − $1,700 = $8,300**, on a settle between $118,000 and $128,000.
- **Lower breakeven = $108,000 + $1,700 = $109,700.**
- **Upper breakeven = $128,000 + $8,300 = $136,300** — **above this, escalating naked-short losses.**

Payoff at expiration:

| BTC at expiry | P&L (per contract) | Note |
|---|---|---|
| ≤ $108,000 | −$1,700 | debit lost (no move) |
| $109,700 | $0 | lower breakeven |
| $118,000 - $128,000 | +$8,300 | max-profit plateau |
| $136,300 | $0 | upper breakeven |
| $146,300 | −$10,000 | naked short: $1-for-$1 loss above breakeven |

**Path A — target hit.** BTC grinds to $120,000 by expiry (inside the plateau) → close for **~+$6,000/contract** (bank ~70% of max; do not carry the naked $128k short into expiry week).

**Path B — no move.** BTC chops around $107,000; all calls expire worthless → **−$1,700/contract** (the debit).

**Path C — runaway (the tail).** A weekend short squeeze gaps BTC to $142,000. Above the $136,300 breakeven the naked $128k short bleeds $1-for-$1 → mark ≈ **−$5,700/contract** and climbing. The **hard stop at K2 ($128,000)** exists precisely to close before this — a 24/7 gap can skip the stop, which is why the position is sized small and converted to a fly before known catalysts.

## Sources

- [[greeks-live]] / [[deribit]] documentation — IV surface, USDC-margined vs inverse settlement, portfolio-margin behavior in vol spikes, 08:00 UTC cash settlement.
- [[book-option-volatility-and-pricing]] — Natenberg on ladders and ratio structures with an uncovered short (mechanics port to crypto; the tail is worse in a 24/7 market).
- Crypto liquidation-cascade record (2020-03, 2022 LUNA/FTX, 2025-10-10) — why the naked leg's gap risk is real, not theoretical.

## Getting the Data (CryptoDataAPI)

The IV surface used to price the ladder comes from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the flow, dealer-gamma, funding, liquidation, and volatility-regime context used to place the target zone and watch the naked-leg tail.

**Live:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (resistance/OI walls to place K1/K2 against)
- `GET /api/v1/quant/gex` — Gamma Exposure; short-dealer-gamma above spot flags squeeze/cascade risk toward the naked leg
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the runaway move that hits the tail
- `GET /api/v1/volatility/regime` — per-asset vol regime; avoid selling naked convexity into an expanding-vol read
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver and a crowded-positioning gauge

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol / range context and target sizing
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the move distribution

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

## Related

- [[butterfly-spread]] — the defined-risk cousin (convert the tree to a fly to cap the tail)
- [[broken-wing-butterfly]] — asymmetric structure with a *capped* tail instead of a naked one
- [[ratio-spread]] — the christmas tree is a ratio spread with an extra short leg
- [[jade-lizard]] — a premium structure that caps the upside instead of leaving it naked
- [[iron-condor]] — defined-risk range structure for comparison
- [[crypto-options-volatility-selling]] — the short-premium context
- [[deribit]], [[greeks-live]] — venue and analytics; surface source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[gamma-exposure]], [[max-pain]] — positioning, squeeze, and level context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
