---
title: "Broken Wing Butterfly"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, volatility, bitcoin, ethereum]
aliases: ["BWB", "Skip-Strike Butterfly", "Unbalanced Butterfly", "Crypto Broken Wing Butterfly"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[butterfly-spread]]", "[[iron-butterfly]]", "[[iron-condor]]", "[[christmas-tree-spread]]", "[[jade-lizard]]", "[[ratio-spread]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit_only
    role: universe
    rule: "BTC and ETH Deribit options only: the skipped-strike build needs strike granularity alt chains do not have"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied vol served. Option quotes and the strike grid come from Deribit."
  - id: bwb_strikes
    role: entry
    rule: "Put BWB: buy 1 put at body + n, sell 2 puts at the body, buy 1 put at body - f with the wide wing f larger than the narrow wing n (call BWB mirrors it)"
    runnable: false
    note: "Needs Deribit's strike grid and quotes; no option chain is served. Spot for placing the body is oracle_price on /api/v1/hyperliquid/open-interest."
  - id: zero_cost_or_credit
    role: entry
    rule: "Enter for zero cost or a small credit, the cheap wide-wing long financed by the two short body options"
    runnable: false
    note: "Needs the legs' bid and ask; no option quotes are served."
  - id: tenor_30_45_dte
    role: entry
    rule: "Expiry 30-45 days out"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: vol_elevated_for_credit
    role: filter
    rule: "Build when vol is elevated so the short body options pay for a credit; in compressed DVOL the structure costs a debit"
    runnable: partial
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "The page's AI workflow says the vol regime should read elevated, a word the regime labels do not use; expanding is the nearest, and compressed is the stated no-credit case. DVOL itself is items[].dvol on /api/v1/volatility/implied. Whether a credit is actually available needs Deribit quotes."
  - id: body_at_max_pain
    role: entry
    rule: "Place the body at the max-pain strike"
    runnable: partial
    endpoint: /api/v1/market-intelligence/options
    field: data[].max_pain
    replay: /api/v1/backtesting/snapshots?data_type=coinglass_options&start={start}
    replay_field: snapshots[].data[].max_pain
    note: "BTC only (no ETH max pain). It is computed on the Deribit expiry with the largest open interest, which may not be the structure's expiry."
  - id: skew_side_from_funding
    role: entry
    rule: "Let funding decide which side's skew funds the skipped wing (put BWB vs call BWB)"
    runnable: partial
    endpoint: /api/v1/derivatives/funding-rates?coin={coin}
    field: binance.current_rate
    note: "Funding is served; the skew it stands for is not. The page gives no threshold: positive funding usually means firm call skew, negative a bid put skew."
  - id: range_regime_favoured
    role: filter
    rule: "Favour a leading range_low_vol market regime; a rising vol_spike probability threatens the risk-bearing side"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: explain.label_posteriors.range_low_vol
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].post_label_2
    note: "label_posteriors holds the current probability of each regime (vol_spike beside it; post_label_4 in the replay). 'Favour' and 'rising' have no thresholds on the page."
  - id: profit_target_50_75
    role: exit
    rule: "Close at 50-75% of max profit when spot is near the body"
    runnable: true
    input: position
    note: "The structure's mark comes from Deribit; no option prices are served."
  - id: wide_wing_decision
    role: exit
    rule: "If price moves toward the wide wing, hold to the capped floor or close early"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "The move toward the wing is mechanical; hold or close is the trader's call."
  - id: vol_shock_close
    role: stop
    rule: "If DVOL explodes while you are short the body's gamma, close at the defined floor rather than ride pin uncertainty"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol_change_24h
    note: "dvol_change_24h is in vol points; the page gives no size for 'explodes'. vol_shock on /api/v1/volatility/regime/{symbol} is a served shock label."
  - id: dealer_flip_exit
    role: exit
    rule: "Adjust or exit when dealers flip to short gamma on the unprotected side, before price gets there"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    note: "/quant/gex is a perp analog of dealer gamma, not Deribit options gamma; a score at or above 0.35 is the amplify (short-gamma) state. The API does not split the read by side of spot."
---

# Broken Wing Butterfly

## Overview

The broken wing butterfly (BWB) is an **asymmetric** variant of the [[butterfly-spread]] in which one wing is wider than the other (a "skipped" strike). By making one wing wider, the structure can be entered for a **net credit or zero cost** and eliminates loss entirely on *one* side, while retaining a narrow max-profit tent shifted directionally. It trades the standard fly's symmetry for a directional lean, cheaper (or credit) entry, and a "no-loss" side — at the cost of a capped tail on the wider side.

On [[deribit]] BTC/ETH, the BWB is a favored way to take a **directional-but-hedged** view: e.g., a put BWB that keeps its full value if BTC rallies, pays best if BTC drifts toward the body, and caps the loss to a small, defined amount only if BTC crashes through the wide wing. Crypto's persistent put skew (puts richer than equidistant calls) makes credit/zero-cost put BWBs relatively easy to build.

## Construction

Three strikes, four legs, one wing wider than the other, cash-settled:

**Put BWB (neutral-to-mildly-bearish body, no upside risk):**

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Buy 1 put | upper strike (K+n) | narrow-wing long |
| 2 | Sell 2 puts | body strike (K) | the target |
| 3 | Buy 1 put | lower strike (K−f), **skipped further out** | wide-wing long (cheap protection) |

- **Narrow wing** width n = (upper − body); **wide wing** width f = (body − lower), with **f > n**.
- **Ratios:** 1 : −2 : 1.
- **Net entry:** because the wide-wing long is far OTM and cheap, the position often nets to **zero or a small credit**. Crypto put skew helps: the two short body puts are relatively rich.
- **No-loss side:** for a put BWB, if price rises above the top strike all puts expire worthless → P&L = net credit (no loss). The at-risk side is the wide (lower) wing.
- **Call BWB** mirrors this for a neutral-to-mildly-bullish body with no downside risk.
- **Tenor:** 30-45 DTE for the theta profile.

## Payoff & breakevens

For the put BWB above (body K, narrow wing n up, wide wing f down, entered at ~zero cost):

- **Max profit** = narrow wing width n + net credit, on a body pin at expiry.
- **No-loss side** (upside): above the top strike, P&L = net credit (zero-cost → $0, no loss).
- **Max loss** (wide/lower side): (wide wing f − narrow wing n) − net credit, below the lowest strike. This is the only at-risk side, and it is capped.
- **Downside breakeven** = between the body and the lowest strike, where the descending payoff crosses zero.

The tent is lopsided: a flat no-loss shelf on one side, a peak at the body, and a short slope to a small capped-loss floor on the wide side.

## Greeks profile

- **Delta:** carries a **directional lean** at entry (unlike a balanced fly) — a put BWB is slightly short delta (leans toward the body below spot / protected above), a call BWB slightly long.
- **Gamma:** negative around the body (short two options there), flattening toward the no-loss side; concentrated near expiry at the body.
- **Theta:** positive when spot is near or above the body (for a put BWB) — the no-loss side means time decay is largely a tailwind.
- **Vega:** roughly negative (net short the body's extrinsic value); elevated DVOL helps build the credit at entry.

## Market view / when to use

- You lean **mildly directional** (or neutral) and want a structure that costs nothing if you are wrong on the protected side.
- For a **put BWB:** you do not expect a rally to hurt you (no upside loss), you would like a drift toward the body, and you accept a small capped loss only on a crash.
- **Elevated DVOL / rich skew** so the two short body options finance the structure to a credit or zero cost.
- You want a defined, small tail rather than the naked exposure of a [[ratio-spread]].

## Adjustments & management

- **Profit target:** close at **50-75% of max profit** when spot is near the body.
- **No-loss side:** if price moves onto the protected side, there is nothing to manage — the credit is safe; let it ride or close for the credit.
- **Wide-wing side:** if price moves toward the wide wing, the loss is already capped; decide whether to hold to the defined floor or close early.
- **Time management:** theta helps near the body/protected side; the profit zone widens into expiry.
- **Vol-shock kill:** in a crash toward the wide wing, the loss is capped — but if DVOL explodes and you are short the body's gamma, closing at the defined floor is cleaner than riding pin uncertainty.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] BTC/ETH — the skipped-strike construction needs the strike granularity that only BTC/ETH chains offer; **alts are too sparse**.
- **Inverse vs linear/USDC settlement:** use **USDC-margined (linear)** so the credit, breakeven, and capped loss are clean USD figures. Inverse (coin-margined) options distort the asymmetric payoff badly — the "no-loss" side is only truly no-loss in the settlement currency, and coin collateral moving with spot can reintroduce loss on a put BWB during a selloff.
- **Crypto put skew builds the credit:** BTC/ETH puts are usually richer than equidistant calls, so a **put BWB reaches zero-cost or credit more easily** than in equities. Read the 25-delta [[risk-reversal]] / skew before choosing the direction.
- **DVOL regime:** elevated DVOL fattens the two short body options → easier credit. In compressed DVOL the structure tends to cost a debit (behaves more like a plain butterfly).
- **24/7 & weekend gaps:** the capped, defined loss on the wide side is exactly what you want in a market that can gap −20% over a weekend — the BWB's tail is pre-limited. Expiry **08:00 UTC**, cash-settled to the Deribit index: **no assignment/pin-risk** on the short body (unlike US single-stock BWBs).
- **No [[section-1256-contracts|§1256]]:** the credit and any gains are ordinary capital-gains events on offshore Deribit — no 60/40 US shelter.
- **Perp funding interaction:** funding-driven skew tells you which side to protect cheaply; a richly-positive-funding regime (call skew firm) can make a **call BWB** the easier credit build.

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$108,000**; DVOL **48** (elevated enough to build a credit); you do not expect a rally to hurt you, would welcome a drift to ~$106k, and want a capped tail on a crash. 35 DTE. Put BWB: narrow upper wing **$6,000** ($112k → $106k), wide lower wing **$10,000** ($106k → $96k).

**Trade (per 1-BTC contract, put BWB):**
- Buy 1 $112,000 put for **$5,000**.
- Sell 2 $106,000 puts for **$3,000** each ($6,000 credit).
- Buy 1 $96,000 put for **$1,000**.
- **Net = −$5,000 + $6,000 − $1,000 = $0 (zero cost).**
- **Max profit = narrow wing $6,000 + credit $0 = $6,000** on a $106,000 pin.
- **No upside loss:** above $112,000 all puts expire worthless → **P&L $0** (no loss if BTC rallies).
- **Downside breakeven = $100,000.** **Max loss = (wide $10,000 − narrow $6,000) − $0 = $4,000**, reached below $96,000.

Payoff at expiration:

| BTC at expiry | P&L (per contract) | Note |
|---|---|---|
| ≥ $112,000 | $0 | no-loss upside shelf |
| $106,000 | +$6,000 | max profit (body pin) |
| $100,000 | $0 | downside breakeven |
| $96,000 | −$4,000 | max loss reached |
| ≤ $96,000 | −$4,000 | capped floor |

**Path A — quiet/drift.** BTC eases to $105,500 by expiry → close near max for **+~$4,500/contract** (bank 50-75%, do not chase the exact pin).

**Path B — rally.** BTC rips to $118,000; all puts expire worthless → **P&L $0**. You were "wrong" directionally and lost nothing — the point of the structure.

**Path C — crash.** BTC gaps −15% to $92,000 over a weekend. The loss is pre-capped at **−$4,000/contract** by the long $96,000 wing — a defined, survivable tail versus the open risk of a naked short put.

## Sources

- [[greeks-live]] / [[deribit]] documentation — IV surface, 25-delta skew/[[risk-reversal]], USDC-margined vs inverse settlement, 08:00 UTC cash settlement.
- [[book-option-volatility-and-pricing]] — Natenberg on unbalanced/skip-strike butterflies and ratioed structures (mechanics port to crypto).
- Deribit / crypto-skew research — persistent put-skew that makes credit/zero-cost put BWBs achievable.

## Getting the Data (CryptoDataAPI)

The IV surface and 25-delta skew used to choose the direction and build the credit come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the options-flow, dealer-gamma, funding, and volatility-regime context.

**Live:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the crypto skew driver (which side to protect cheaply)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (body-placement magnet)
- `GET /api/v1/volatility/regime` — per-asset vol regime; elevated DVOL builds the credit
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol / range context
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — build the BWB when `GET /api/v1/volatility/regime` is elevated (credit available) and `GET /api/v1/market-intelligence/options` max pain marks the body placement; `GET /api/v1/derivatives/funding-rates?coin=BTC` decides which side's skew funds the skipped wing
- **Regime gate** — `GET /api/v1/quant/market`: favour leading `range_low_vol` probability; a rising `vol_spike` bucket threatens the risk-bearing side of the asymmetric structure
- **Backtest** — options-chain history is not served, so proxy the structure against underlying paths from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09), pinning each entry to point-in-time vol state via `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — re-check `/api/v1/quant/gex` after entry: a dealer flip to short gamma on the unprotected side is the adjust/exit trigger before price gets there.

## Related

- [[butterfly-spread]] — the symmetric parent structure
- [[iron-butterfly]] — credit ATM version of the balanced fly
- [[christmas-tree-spread]] — another asymmetric multi-leg directional structure
- [[jade-lizard]] — another "no-loss on one side" premium structure (no upside risk)
- [[ratio-spread]] — the BWB without the protective wing (undefined risk)
- [[crypto-options-volatility-selling]] — the short-vol context
- [[deribit]], [[greeks-live]] — venue and analytics; surface and skew source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[gamma-exposure]], [[max-pain]] — skew and positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
