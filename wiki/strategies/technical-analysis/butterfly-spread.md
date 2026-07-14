---
title: "Butterfly Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, mean-reversion, bitcoin, ethereum]
aliases: ["Long Butterfly", "Call Butterfly", "Put Butterfly", "Crypto Butterfly"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[crypto-options-volatility-selling]]", "[[iron-butterfly]]", "[[iron-condor]]", "[[broken-wing-butterfly]]", "[[christmas-tree-spread]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Butterfly Spread

## Overview

The butterfly spread is a **defined-risk, low-cost** options structure that profits when the underlying finishes near a specific target price at expiry. The classic long call butterfly buys 1 lower-strike call, sells 2 middle-strike calls, and buys 1 upper-strike call — all same expiry, equally spaced. The middle strike is the price you expect the underlying to settle at. It costs a small debit and offers a favorable reward-to-risk if spot pins near the center. It is the **debit** twin of the [[iron-butterfly]] (same tent payoff, opposite entry) and a targeted bet on **low realized volatility** or a specific price magnet.

On [[deribit]] BTC/ETH, the butterfly is a cheap way to express "I think price ends near level X" — around a [[max-pain]] magnet, a large OI wall, or a technical level — with the entire risk capped at the tiny debit. Because it is long the wings and short the body, it is short vega and profits from a DVOL crush toward a quiet outcome.

## Construction

Three strikes, four option legs (2:1:1 by count), one expiry, cash-settled:

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Buy 1 call | lower strike (K−w) | lower wing |
| 2 | Sell 2 calls | center strike (K) | the body / target |
| 3 | Buy 1 call | upper strike (K+w) | upper wing |

- **Strike selection:** center (K) at the expected settlement / magnet; wings equally spaced by width w. A **put butterfly** is identical using puts; both give the same payoff.
- **Ratios:** 1 : −2 : 1. The two short center options finance most of the structure.
- **Net debit** = (lower call + upper call) − 2 × (center call). A small fraction of the wing width w (e.g. a $6,000-wide BTC fly for a ~$1,000 debit).
- **Tenor:** 14-45 DTE. Shorter offers more leverage (cheaper debit, sharper tent) but demands a more precise pin.

## Payoff & breakevens

- **Max profit** = wing width w − net debit, on a pin at the center strike at expiry.
- **Max loss** = the net debit paid, at or beyond either wing.
- **Lower breakeven** = lower strike + net debit.
- **Upper breakeven** = upper strike − net debit.

A symmetric tent centered on K, capped-loss floors at both wings — the exact shape of an [[iron-butterfly]], just entered for a debit instead of a credit.

## Greeks profile

- **Delta:** ~0 at entry when centered on spot; nonzero if the body is placed above/below spot to express a directional target.
- **Gamma:** **negative near the center, positive out by the wings** — the short body dominates around K, so the fly dislikes movement once spot is inside the wings; near expiry the center gamma is concentrated (and *helps* the holder if spot is pinned, as theta bites hard).
- **Theta:** **positive when spot is near the center** (time decay pulls the tent toward max profit), negative when spot sits out near a wing.
- **Vega:** **negative** — long the cheap wings, short the rich body; a DVOL crush toward a quiet outcome marks the fly up.

## Market view / when to use

- You have a **specific price target** where BTC/ETH is likely to settle, and expect **low realized volatility** getting there.
- Elevated-to-moderate DVOL that you expect to **crush** — the fly is relatively cheaper when you expect IV to fall.
- Placing the body at a **[[max-pain]] magnet** or heavy OI wall into a monthly expiry, where dealer gamma tends to pin price.
- You want a very cheap, hard-capped bet — risk is the small debit only.

## Adjustments & management

- **Profit target:** close at **50-75% of max profit**; the perfect pin is unrealistic, so bank partial profit.
- **Time management:** if spot is near the center in the final week, holding lets theta work aggressively; if spot is out near a wing, close to salvage value.
- **Recenter (roll the body):** if spot drifts off the center early with time left, close the fly and re-open centered on the new price.
- **Convert to a [[broken-wing-butterfly]]:** widen one wing (buy a further-OTM option on the threatened side) to shift the risk and often reduce the debit.
- **Convert to an [[iron-butterfly]]:** add the opposite-side spread at the same center to collect a credit and widen the effective zone.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] BTC/ETH. The three-strike structure needs the strike granularity and depth that only BTC/ETH provide; **alt-option chains are too sparse** to build a clean fly.
- **Inverse vs linear/USDC settlement:** use **USDC-margined (linear)** options so the debit, tent, and breakevens are clean USD numbers. Inverse (coin-margined) options distort the symmetric tent because collateral value moves with spot.
- **DVOL regime:** the fly is short vega; it is relatively cheaper and more attractive when **DVOL is elevated and expected to crush** toward a quiet, pinned outcome. Buying a fly in a compressed-DVOL regime that then expands is the losing setup.
- **24/7 & weekend gaps:** the narrow tent is vulnerable to crypto's continuous gaps — a weekend move away from the center at 03:00 UTC cannot be managed until you wake, and max profit requires a genuine pin. But risk is capped at the small debit, so a gap is annoying, not ruinous. Expiry **08:00 UTC**, cash-settled to the Deribit index — settling at the center is the max-profit outcome, with **no assignment/pin-risk** on the short body (unlike US single-stock flies).
- **No [[section-1256-contracts|§1256]]:** gains are ordinary capital-gains events on offshore Deribit — no 60/40 US shelter.
- **Perp funding / dealer gamma interaction:** a fly placed at a heavy call-wall works best when [[gamma-exposure|dealer gamma]] is long (spot dampened toward the wall); funding-driven skew shifts which wing is cheaper to buy.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$108,000**; you expect it to gravitate toward the **$110,000** monthly max-pain magnet and stay quiet; DVOL **50** and expected to ease. 30 DTE. Wings **$6,000** wide ($104k / $110k / $116k), body slightly above spot (mildly bullish target).

**Trade (per 1-BTC contract, call butterfly):**
- Buy 1 $104,000 call for **$7,200**.
- Sell 2 $110,000 calls for **$4,300** each ($8,600 credit).
- Buy 1 $116,000 call for **$2,400**.
- **Net debit = $7,200 + $2,400 − $8,600 = $1,000.** Wing width = $6,000.
- **Max profit = $6,000 − $1,000 = $5,000** on a $110,000 pin. **Max loss = $1,000** (the debit).
- **Breakevens:** $104,000 + $1,000 = **$105,000**; $116,000 − $1,000 = **$115,000**.
- **Reward:risk ≈ 5:1** (but max profit needs a near-perfect pin).

**Path A — pins near target.** BTC drifts to $110,500 by expiry; DVOL crushes 50 → 43. The fly is worth ~$4,600 at expiry; close a day early for **+~$3,600/contract** (~72% of max). Theta + IV crush did the work.

**Path B — quiet but off-center.** BTC ends at $107,000 (below the lower breakeven $105k? no — $107k > $105k, so still profitable). The $104k call is worth $3,000, the $110k/$116k calls worthless → payoff $3,000 − $1,000 debit = **+$2,000/contract**.

**Path C — trend away.** BTC rallies hard to $120,000 (above the upper wing). All the tent's value is lost; the fly expires at max loss = **−$1,000/contract** (the debit). Capped and small — the reason the structure is attractive despite the narrow zone.

## Sources

- [[greeks-live]] / [[deribit]] documentation — IV surface, USDC-margined vs inverse settlement, 08:00 UTC cash settlement (center pin = max profit, no assignment).
- [[book-option-volatility-and-pricing]] — Natenberg on butterfly construction, Greek profiles at entry, and the butterfly-pricing/volatility relationship (mechanics port to crypto).
- Deribit / [[max-pain]] pinning research — OI-wall magnets into monthly expiries as body-placement targets.

## Getting the Data (CryptoDataAPI)

The IV surface used to price the wings comes from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the options-flow, pinning, dealer-gamma, and volatility-regime context used to place and time the fly.

**Live:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike — the magnet to center the body on
- `GET /api/v1/quant/gex` — Gamma Exposure; long-dealer-gamma regimes pin spot toward walls (favorable for a fly)
- `GET /api/v1/volatility/regime` — per-asset vol regime; a fly wants elevated DVOL expected to crush toward a quiet outcome
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver (which wing is cheaper to buy)

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol / range context around the target
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting pin behavior

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

## Related

- [[iron-butterfly]] — the credit version of the same tent payoff
- [[iron-condor]] — wider profit zone, lower max profit, similar low-vol thesis
- [[broken-wing-butterfly]] — the asymmetric variant that shifts risk to one side
- [[christmas-tree-spread]] — a directional multi-leg cousin (ladder)
- [[crypto-options-volatility-selling]] — the short-vol context
- [[deribit]], [[greeks-live]] — venue and analytics; surface source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[gamma-exposure]], [[max-pain]] — placement and pin context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
