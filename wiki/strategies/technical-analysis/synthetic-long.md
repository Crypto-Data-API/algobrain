---
title: "Synthetic Long (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, synthetic, replication, leverage, derivatives, bitcoin, ethereum]
aliases: ["Synthetic Short", "Combo", "Crypto Synthetic Long", "Synthetic Forward"]
strategy_type: quantitative
timeframe: swing|position
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[risk-reversal]]", "[[collar]]", "[[covered-call]]", "[[married-put]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[section-1256-contracts]]", "[[staking]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Synthetic Long (Crypto)

## Overview

A synthetic long replicates the P&L of holding a coin by **buying an ATM [[call-option|call]] and selling an ATM [[put-option|put]] at the same strike and expiration** on [[deribit]]. The combined [[delta]] is ≈ +1.0 per contract — identical to holding 1 BTC/ETH — but requires little to no upfront coin, because you never buy spot. The mirror image (sell the call, buy the put at the same strike) is a **synthetic short**, replicating a short coin position. By [[put-call-parity|put-call parity]], the net debit/credit of the combo prices the **implied forward** — in crypto this embeds the cost of carry, which is tightly linked to [[funding-rate|perp funding]] and futures basis.

In crypto, the [[perpetual-futures|perpetual future]] is already the dominant "synthetic long," so the options synthetic competes directly with simply longing the perp. The options combo's edge is that it locks a **fixed forward to a dated expiry** (no floating funding), and — paired against a perp or dated future — it is the building block of the crypto **reversal / basis-capture** trade.

## Construction

1. **Buy 1 ATM call** at the strike nearest spot.
2. **Sell 1 ATM put** at the same strike and expiration.
3. **Tenor:** 30-120 DTE — enough time for the thesis while keeping [[theta]] and pin risk manageable.
4. **Net cost** is near zero, offset by the implied-forward premium/discount (skew, rates, and the futures basis).
5. **Synthetic short:** reverse the legs (sell call, buy put).
6. Choose **USDC-margined (linear)** for clean USD exposure; coin-margined (inverse) introduces quanto-like non-linearity.

## Payoff & breakevens

The synthetic long tracks the coin one-for-one in both directions.

| Point | Value |
|---|---|
| **Breakeven** | Strike + net debit (or − net credit) |
| **Max profit** | Unlimited (coin can rise without bound) |
| **Max loss** | Substantial — the short put carries full downside to zero (coin → 0) |

The position is economically **long the forward**: profit and loss mirror owning the coin, adjusted by the implied-forward premium locked at entry.

## Greeks profile

| Greek | Sign | Note |
|---|---|---|
| [[delta]] | ≈ +1.0 (−1.0 for synthetic short) | Share-for-share coin exposure |
| [[gamma]] | ≈ 0 away from expiry; spikes ATM near expiry | The long call and short put gammas cancel except near the strike at expiry (pin risk) |
| [[theta]] | ≈ 0 | Long-call decay offset by short-put decay — a synthetic forward barely bleeds time |
| [[vega]] | ≈ 0 | Long-call vega offset by short-put vega — near vol-neutral; residual comes from skew |

The near-zero theta and vega are the point: a synthetic long is a **pure directional (delta-one) instrument**, not a volatility trade — its behavior differs sharply from a single long call or the [[covered-call]]/[[protective-put]] overlays.

## Market view / when to use

- You want **delta-one long (or short) coin exposure** with minimal capital outlay.
- You want to **lock a fixed forward to a dated expiry** rather than pay floating [[funding-rate|funding]] on a perp.
- **Basis / reversal capture:** synthetic long via options + short perp (or short dated future) harvests the spread between the options-implied forward and the perp/futures price.
- Establishing a quick **delta-equivalent leg** for a spread, [[pairs-trading]], or hedging book.

## Adjustments & management

- **Roll before expiry** to avoid pin risk if you want to maintain exposure (close the combo, reopen at a later expiry).
- **Convert to defined-risk:** buy a lower put (turn the short put into a put spread) to cap the downside if the view sours — this converts the synthetic long toward a [[risk-reversal]] with protection.
- **Manage the short-put margin:** a DVOL spike inflates the short put's margin; keep headroom so a vol shock does not force liquidation.
- **Watch the basis:** if running against a perp, monitor funding — the trade's carry is the funding you collect/pay on the hedge leg.

## Crypto specifics

- **Competes with the perp.** The [[perpetual-futures|perpetual future]] is crypto's native synthetic long; the options combo differs by locking a **dated forward** (no floating funding) and by embedding skew. Choose the options synthetic when you want fixed-tenor exposure or a basis trade; choose the perp for simple floating-rate leverage.
- **Put-call parity prices the funding/basis.** The combo's net debit/credit is the implied forward minus spot — in crypto this reflects the futures basis and, indirectly, [[funding-rate|funding]]. A rich positive basis makes the synthetic long carry a premium (you pay up to be long via options); a discount makes it cheap.
- **Reversal / basis arb.** Synthetic long (options) + short perp = a market-neutral **reversal** that captures the options-vs-perp basis — a staple crypto options-desk trade; the inverse (synthetic short + long perp) captures the opposite dislocation.
- **Inverse vs linear settlement.** USDC-margined combos give clean USD delta; coin-margined (inverse) combos are quanto-like, so the effective delta drifts with spot.
- **Cash settlement, no early assignment.** Deribit's European options mean the short put cannot be assigned early; both legs cash-settle to the index at expiry. **Pin risk** near the strike at expiry is the main expiry hazard.
- **No coin, no staking yield.** You do not hold the coin, so you forgo [[staking|staking yield]] and any on-chain use — a real carry disadvantage versus holding (or staking) spot.
- **No [[section-1256-contracts|§1256]].** Ordinary treatment; the combo does not get the 60/40 shelter a broad-based index synthetic would.
- **24/7 markets.** Continuous gap risk on the short-put downside; no session close to cap an overnight move.

## Risks

- **Full downside via the short put:** the coin can fall to (near) zero; the synthetic long loses like spot, but on little posted capital, so **effective leverage is high**.
- **Margin spiral:** a DVOL spike inflates short-put margin at the worst moment.
- **Pin risk** at expiry if spot sits at the strike.
- **No staking/dividend carry** — a persistent drag versus holding spot.
- **Coin-margined non-linearity** if inverse contracts are used.
- **Basis risk** if run as a reversal and the options-vs-perp spread moves against you before convergence.

## Worked crypto example

**Setup (illustrative).** BTC spot $68,000; you want long exposure to 1 BTC for 60 days without buying spot.

- **Buy** 1 × $68,000 call (60 DTE) at $5,200
- **Sell** 1 × $68,000 put (60 DTE) at $4,900
- **Net debit** $300 (the implied forward sits ~$300 above spot — a mild positive basis)

| Outcome at expiry | P&L |
|---|---|
| BTC to $80,000 | Call worth $12,000, put worthless → **+$11,700** (≈ spot gain of $12,000 − $300 basis) |
| BTC at $68,000 | Both near zero → **−$300** (the basis paid) |
| BTC to $56,000 | Call worthless, short put −$12,000 → **−$12,300** (mirrors spot, minus basis) |

The combo mirrors 1 BTC of spot P&L, shifted by the $300 forward premium — achieved with margin rather than $68,000 of coin. **Reversal variant:** hold this synthetic long and short 1 BTC perp; you are delta-neutral and earn the convergence of the options-implied forward to the perp price plus/minus funding on the perp leg.

## Getting the Data (CryptoDataAPI)

The options-implied forward comes from the Deribit chain ([[greeks-live]]); [[cryptodataapi]] supplies the funding and basis context that prices the synthetic and drives the reversal trade.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding (the carry the options forward is priced against)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange OI (positioning/basis context)
- `GET /api/v1/market-intelligence/options` — BTC options OI / [[max-pain]] (pin-risk context near expiry)
- `GET /api/v1/volatility/regime` — vol regime (short-put margin risk)

**Historical data:**
- `GET /api/v1/backtesting/funding` — historical funding for basis/reversal backtests
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for delta and basis tracking

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-derivatives]]; options-implied forward from Deribit / [[greeks-live]].

## Related

- [[risk-reversal]] — the closely related OTM combo (long call / short put at different strikes); add a protective wing to define the synthetic's risk
- [[collar]] — the opposite-signed protective structure on a spot position
- [[covered-call]] / [[married-put]] — overlays that require (or protect) actual coin, unlike the synthetic
- [[perpetual-futures]] — crypto's native synthetic long; the competing/hedging instrument
- [[funding-rate]] / [[cash-and-carry]] — the carry the implied forward is priced against; the reversal-trade counterpart
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin-margined vs USDC-margined combos, put-call parity and the implied forward
- [[perpetual-futures]] / [[funding-rate]] — how the perp funding and futures basis price the options synthetic and drive the reversal trade
