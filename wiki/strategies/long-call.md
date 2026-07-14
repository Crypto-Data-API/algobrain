---
title: "Long Call (Crypto)"
type: strategy
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, bitcoin, ethereum]
aliases: ["Long Call", "Buy Call", "Crypto Long Call"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[long-put]]", "[[synthetic-long]]", "[[risk-reversal]]", "[[straddle]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[cryptodataapi]]"]
---

# Long Call (Crypto)

## Overview

A long call is the canonical bullish [[options]] structure: the buyer pays a premium for the right (not the obligation) to buy the underlying coin at a fixed strike on or before expiry. On [[deribit]] — where ~85-90% of BTC/ETH options flow trades — one BTC option controls **1 BTC** (one ETH option controls 1 ETH), contracts are **European, cash-settled at 08:00 UTC** against the Deribit index, and the premium is paid and settled in the coin itself ([[deribit#Inverse settlement|inverse / coin-margined]]). It is the cleanest way to express a directional bullish view with **bounded loss** (the premium paid) and **unbounded upside** (any settlement above strike + premium). Every richer bullish structure — [[risk-reversal]], [[synthetic-long]], call spread, [[diagonal-spread]] — is a modification of this primitive.

The long call is **not** a positive-edge trade in isolation. A held-to-expiry BTC call bleeds [[theta]] daily and typically pays the [[variance-risk-premium|variance risk premium]] (crypto IV, benchmarked by [[dvol|DVOL]], usually prints above subsequently realized vol). Edge comes from **selectivity**: buying calls only when the implied move (DVOL) understates a forecastable realized move, or when the call is the long-vol / long-convexity leg of a larger book.

## Construction

1. **Buy 1 call** at the chosen strike and expiry on [[deribit]] (or Greeks.live for RFQ/blocks).
2. **Strike selection** (delta as the intuitive dial):
   - **ATM** (Δ ≈ 0.50): balanced gamma/theta/vega — short-dated directional speculation.
   - **OTM** (Δ ≈ 0.20-0.35): cheaper, higher leverage, needs a bigger move — popular around catalysts (ETF flows, unlocks, halving narratives).
   - **ITM** (Δ ≈ 0.65-0.80): more delta-like, lower theta drag — a capped-downside coin substitute.
3. **Tenor**: 7-30 DTE for event/swing plays (Deribit lists daily, weekly, and monthly expiries); 60-180 DTE for slower theses.
4. **DVOL check**: compare [[dvol|DVOL]] (and the ATM term structure) to its own range. Avoid buying straight into a DVOL spike — crypto vol crushes hard after the event prices in.
5. **Settlement choice**: Deribit's flagship BTC/ETH options are **inverse (coin-settled)**; some venues list **linear (USDC-margined)** options that give clean USD payoff. Pick linear when you want the P&L in dollars without the coin-settlement convexity.

## Payoff & breakevens

| Point | Value |
|---|---|
| **Max loss** | Premium paid (capped) |
| **Breakeven** | Strike + premium |
| **Max profit** | Unbounded — coin can rise without limit |

The long call is the upside hockey stick: flat loss (the premium) below the strike, then dollar-for-dollar profit above it, accelerating as [[delta]] climbs toward 1.0.

## Greeks profile

| Greek | Sign | Behaviour as spot rises | Note |
|---|---|---|---|
| [[delta]] | Positive (+0.20 to +0.80 by strike) | Climbs toward +1.0 | Directional long that intensifies as it works |
| [[gamma]] | Positive (largest ATM / near expiry) | Accelerates delta in your favour | The convexity that lets winners run |
| [[vega]] | Positive | Helps if [[dvol|DVOL]] rises with spot; hurts on post-event vol crush | The "right thesis, wrong vehicle" loss lives here |
| [[theta]] | Negative | Bleeds daily, faster inside ~7-10 DTE | The carrying cost — being right but late still loses |

A long call is **long delta, long gamma, long vega, short theta** — the bullish mirror of the [[long-put]] and the structural opposite of a sold call (the short-call leg inside a covered call or [[risk-reversal]]). Its appeal is **positive convexity**: capped premium at risk, uncapped upside.

## Market view / when to use

- **Directional bullish** with a defined catalyst window inside the option's life (ETF flow prints, token unlocks, FOMC/CPI, protocol upgrades, halving-narrative momentum).
- **Cheap convexity**: DVOL in the lower part of its range while a credible up-move catalyst approaches.
- **Capped-risk alternative to the perp**: a [[perpetual-futures|perp]] long gives linear leverage but carries **liquidation risk** and pays [[funding-rate|funding]] when longs are crowded; a long call caps the loss at premium, can't be liquidated, and needs no maintenance margin — you trade funding/liquidation risk for theta.
- **A long-vol leg** inside a book that is otherwise short gamma.

## Adjustments & management

- **Take profit / roll up**: bank a large gain and roll to a higher strike to stay long with less capital at risk.
- **Time stop**: crypto catalysts often price into DVOL before the event; if the catalyst passes without the move, exit rather than feed theta.
- **Spread it off**: sell a higher call against it (turn the long call into a call spread) to cut theta and cost once the easy move is in.
- **Watch expiry pin**: near 08:00 UTC expiry, [[max-pain]] and dealer gamma can pin spot toward high-open-interest strikes.

## Crypto specifics

- **Deribit inverse (coin) settlement.** Premium is paid in BTC/ETH and the payoff settles in coin, so the USD delta of a Deribit call differs slightly from the naive Black-Scholes number — the payoff currency itself moves with spot. For clean USD exposure use **linear (USDC-margined)** contracts. See [[deribit]] and [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]].
- **DVOL, not the VIX.** The implied vol you pay is benchmarked by [[dvol|DVOL]], Deribit's 30-day IV index (a Deribit / [[greeks-live]] number, **not** on CryptoDataAPI). Buy calls when DVOL is cheap versus your realized-vol forecast; beware the post-event DVOL crush.
- **24/7, no session gaps.** Crypto never closes, so there is no overnight/weekend gap you cannot trade — but **weekend books are thin**, so realized moves are jumpier and options can gap in price.
- **Competes with the perp.** The [[perpetual-futures|perpetual future]] is crypto's default leverage; the long call differs by capping loss, removing liquidation risk, and locking exposure to a dated expiry (no floating funding).
- **No §1256.** Crypto options do **not** get the [[section-1256-contracts|§1256]] 60/40 tax treatment a broad-based US index option would; expect ordinary treatment (jurisdiction-dependent).
- **Liquidity cliff beyond BTC/ETH.** BTC and ETH chains are deep; alt-coin options (SOL, XRP, and others) have **wide spreads and sparse strikes**, so slippage — not theta — is often the binding cost there.

## Worked crypto example

**Setup (illustrative).** BTC spot $60,000; [[dvol|DVOL]] 55%; bullish into an anticipated ETF-inflow print 12 days out.

- **Buy** 1 × $60,000 call, 30 DTE, at ≈ **$3,800** (≈ 0.063 BTC premium, ATM ≈ 0.4·S·σ·√T).
- Breakeven $63,800; max loss $3,800; max gain unbounded.

| Outcome at expiry | P&L |
|---|---|
| BTC to $72,000, DVOL steady | Call worth $12,000 → **+$8,200** (+216%) |
| BTC flat $60,000, DVOL crushes to 40% | Decays toward zero → **−$3,800** (−100%); the time-stop should exit earlier |
| BTC to $54,000 | Call worthless → **−$3,800** (−100%) |

The capped $3,800 outlay controls 1 BTC of upside — a fraction of the $60,000 needed to hold spot and with no liquidation risk, at the cost of theta and the coin-settlement wrinkle on the payoff.

## Getting the Data (CryptoDataAPI)

The Deribit chain, [[dvol|DVOL]], and per-strike Greeks come from Deribit / [[greeks-live]]. [[cryptodataapi|CryptoDataAPI]] supplies the positioning, vol-regime, and perp-carry context around the trade:

- **Options OI / max pain — positioning and expiry pins** — `GET /api/v1/market-intelligence/options` (BTC options OI, volume, max pain). See [[cryptodataapi-market-intelligence]].
- **Volatility regime — is IV cheap or rich?** — `GET /api/v1/volatility/regime` and market-wide `GET /api/v1/volatility/regime/score`. See [[cryptodataapi-regimes]].
- **Funding — the perp-alternative carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC`. See [[cryptodataapi-derivatives]].

The IV surface and **DVOL** are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

## Related

- [[long-put]] — the bearish counterpart
- [[synthetic-long]] — long call + short put = delta-one coin exposure
- [[risk-reversal]] — long call financed by a short put (or vice versa)
- [[straddle]] — long call + long put for a pure long-vol view
- [[perpetual-futures]] / [[funding-rate]] — crypto's native leverage and its carry; the long call's main competitor
- [[deribit]] / [[greeks-live]] — venue, inverse settlement, and analytics
- [[dvol]] — the implied-vol benchmark you pay
- [[implied-volatility]] / [[realized-volatility]] / [[variance-risk-premium]] — the vol headwind a held call faces
- [[delta]] / [[gamma]] / [[theta]] / [[vega]] — the position's Greek profile
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin-margined vs USDC-margined contracts, DVOL
- Natenberg, S., *Option Volatility and Pricing* — call pricing, Greeks, vol-surface mechanics
- Taleb, N. N., *Dynamic Hedging* — the convexity argument for long-gamma / long-optionality positions
