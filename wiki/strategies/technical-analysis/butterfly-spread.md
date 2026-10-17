---
title: "Butterfly Spread"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, volatility, mean-reversion, bitcoin, ethereum]
aliases: ["Long Butterfly", "Call Butterfly", "Put Butterfly", "Crypto Butterfly"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[crypto-options-volatility-selling]]", "[[iron-butterfly]]", "[[iron-condor]]", "[[broken-wing-butterfly]]", "[[christmas-tree-spread]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit_only
    role: universe
    rule: "BTC and ETH Deribit options only; alt-option chains are too sparse to build a clean fly"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied vol served. Option quotes and the strike grid come from Deribit."
  - id: body_at_max_pain
    role: entry
    rule: "Center the body (K) on the expected settlement magnet: the max-pain strike into expiry"
    runnable: partial
    endpoint: /api/v1/market-intelligence/options
    field: data[].max_pain
    replay: /api/v1/backtesting/snapshots?data_type=coinglass_options&start={start}
    replay_field: snapshots[].data[].max_pain
    note: "BTC only (no ETH max pain). It is computed on the Deribit expiry with the largest open interest, which may not be the fly's expiry; the page also allows a heavy OI wall, which is not served (no per-strike OI)."
  - id: fly_strikes
    role: entry
    rule: "Buy 1 at K - w, sell 2 at K, buy 1 at K + w (calls or puts), equally spaced wings"
    runnable: false
    note: "Needs Deribit's strike grid and quotes; no option chain is served."
  - id: small_debit
    role: entry
    rule: "Net debit a small fraction of the wing width (the example: a $6,000-wide BTC fly for about $1,000)"
    runnable: false
    note: "Needs the legs' bid and ask; no option quotes are served."
  - id: tenor_14_45_dte
    role: entry
    rule: "Expiry 14-45 days out (shorter = cheaper but needs a more precise pin)"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: long_dealer_gamma_pin
    role: filter
    rule: "A long-dealer-gamma read confirms the pin thesis the fly monetises"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "/quant/gex is a perp analog of dealer gamma (Hyperliquid market-maker inventory and liquidation clusters), not Deribit options dealer gamma. A score at or below -0.20 is the dampen (long-gamma) state."
  - id: range_regime_leading
    role: filter
    rule: "range_low_vol has the leading market-regime probability at entry"
    runnable: true
    endpoint: /api/v1/quant/market
    field: explain.label_posteriors.range_low_vol
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].post_label_2
    note: "Leading = the highest of the six values in label_posteriors (post_label_0 to 5 in the replay)."
  - id: vol_elevated_to_crush
    role: filter
    rule: "Vol elevated at entry and expected to crush toward a quiet outcome; never buy the fly in a compressed regime that then expands"
    runnable: partial
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "The regime labels have no 'elevated'; expanding is the nearest, and compressed is the stated losing setup. The expected crush is a forecast. DVOL is items[].dvol on /api/v1/volatility/implied."
  - id: profit_target_50_75
    role: exit
    rule: "Close at 50-75% of max profit; do not wait for the perfect pin"
    runnable: true
    input: position
    note: "The fly's mark comes from Deribit; no option prices are served."
  - id: final_week_management
    role: exit
    rule: "In the final week, hold if spot is near the center; close to salvage value if spot is out near a wing"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "Spot against the strikes is mechanical; 'near' has no distance on the page."
  - id: recenter_on_drift
    role: exit
    rule: "If spot drifts off the center early with time left, close and re-open centered on the new price"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "No drift distance or time threshold is given."
  - id: max_pain_migration_roll
    role: exit
    rule: "A max-pain migration away from the body in expiry week is the roll signal"
    runnable: partial
    endpoint: /api/v1/market-intelligence/options
    field: data[].max_pain
    note: "BTC only, and on the largest-OI expiry, which may differ from the fly's. Poll it more often in expiry week; the page gives no migration distance."
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
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for backtesting pin behavior

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [gamma exposure](https://cryptodataapi.com/quant-gamma) · [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — center the body on the `GET /api/v1/market-intelligence/options` max-pain strike into expiry; a long-dealer-gamma read from `GET /api/v1/quant/gex` confirms the pin thesis the fly monetises
- **Regime gate** — `GET /api/v1/quant/market` with `range_low_vol` probability leading, plus `GET /api/v1/volatility/regime` elevated at entry (rich wings to sell against) and expected to crush toward a quiet outcome
- **Backtest** — measure pin behavior around monthly expiries with `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09); validate entry vol states against `/api/v1/backtesting/daily-snapshots` (since 2026-03-02) to keep timing point-in-time
- **Tips** — the fly's P&L is decided in the final days: raise polling of `/api/v1/quant/gex` and max pain in expiry week; a max-pain migration away from the body is the roll signal, not a reason to hope.

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
