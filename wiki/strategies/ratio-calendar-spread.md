---
title: "Ratio Calendar Spread"
type: strategy
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, swing-trading, bitcoin, ethereum]
aliases: ["Ratio Calendar Spread", "Asymmetric Calendar", "Unbalanced Calendar", "Ratio Time Spread", "Crypto Ratio Calendar"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[calendar-spread]]", "[[diagonal-spread]]", "[[ratio-spread]]", "[[iron-condor]]", "[[short-strangle]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[variance-risk-premium]]", "[[max-pain]]", "[[gamma-exposure]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Ratio Calendar Spread

## Overview

A ratio calendar spread is a [[calendar-spread]] (long and short options at the **same strike, different expiries**) built with an **unequal** number of contracts on the two legs — 1:2, 2:1, 1:3, etc. The 1:1 calendar is a pure vega/term-structure bet; adding a ratio injects a deliberate tilt. **Long-heavy** (more far-dated longs, e.g. 1 short / 2 long) makes it a **convexity trade** — income first, then a long-options payoff if spot runs. **Short-heavy** (more near-dated shorts, e.g. 2 short / 1 long) makes it an **income / theta trade** with a far-dated wing for catastrophe protection.

In crypto this is an advanced [[deribit]] BTC/ETH structure that trades the **[[dvol|DVOL]] term structure** with a directional or income tilt. Deribit's **European cash settlement** removes the pin/assignment risk that plagues American ratio calendars, and **no dividends** removes ratio-distorting corporate actions — a cleaner structure to run than its equity cousin. The catch is crypto-specific and severe: the **short-heavy** variant leaves a residual near-dated short (naked-like) whose tail the slow far-dated wing cannot cover against an unbounded 24/7 gap. The Greeks also **shape-shift** as the near leg decays, so knowing which phase you are in is the whole game.

## Construction

Same strike, two expiries, unequal quantities, on BTC or ETH [[deribit]] options.

**Standard direction — sell near, buy far** (the dominant build):

| Sub-variant | Short (near) | Long (far) | Net cash | Character |
|---|---|---|---|---|
| **Long-heavy 1:2 / 1:3** (convexity) | Sell 1 near, ~10-21 DTE | Buy 2-3 far, ~45-90 DTE | small debit | income then long-options payoff |
| **Short-heavy 2:1 / 3:1** (income) | Sell 2-3 near, ~10-21 DTE | Buy 1 far, ~60-120 DTE (wing) | net credit | steady decay, far-wing tail cover |

**Reverse direction — buy near, sell far** (rarer): long near / short far, for when you expect **near-term DVOL to spike** relative to the back (e.g. into a known catalyst) — net long gamma, short vega.

- **Strike:** ATM for neutral; slightly OTM in the tilt direction for a directional lean.
- **Ratio = the view:** specify the directional, vol, and term-structure view *first*, then choose the ratio. The ratio is a consequence of the view, not the starting point.
- **Size by net cash outlay**, not contract count; short-heavy credits understate the tail.

## Payoff & breakevens

There is **no single static payoff** — the legs expire at different times. The clean snapshot is **at near-leg expiration**, the moment the short leg dies and the structure collapses to a residual position (a naked/near-naked long for long-heavy; a residual short or vertical for short-heavy). Before that, marks are driven by the **theta-decay differential** and the **relative [[vega]]** of the two tenors.

Long-heavy (1:2) at near-leg expiry, call version, ATM short strike `K`:

```
   P&L
    |                                   *
    |                                  *   ← surviving long back-month legs run
    |                                 *      after the short dies → convex upside
    |              ___               *
    |            /     \           *
    |          /  credit  \       *
  0 +--------/---zone at K--\----*--------------  spot at near expiry
    |       /                \
    |    (net debit drag if spot stalls / small move)
    |    ______________ K ________________
```

- **Long-heavy max loss:** roughly the net debit if spot stalls and the far legs bleed; **uncapped upside** once the short dies.
- **Short-heavy max profit:** the collected credit if spot pins near `K`; **loss bounded only by the far wing** — which is slow, so a fast gap can exceed the credit badly before the wing helps.
- **Breakevens** depend on back-month DVOL at near expiry and cannot be pinned exactly at entry.

## Greeks profile

The defining feature is that the Greeks **evolve in two phases** around the near expiry:

| Greek | Long-heavy 1:2 (convexity) | Short-heavy 2:1 (income) |
|---|---|---|
| [[delta]] | small near entry; grows toward the long-leg direction after the short dies | small near entry; converts to a directional short if a side is breached |
| [[gamma]] | slightly **short** before near-expiry (near-leg gamma dominates), flips **long** once the short dies | net **short** — the income-killer; a gap past the short strikes hurts before the far wing helps |
| [[theta]] | mildly **negative** early (paying for the far legs); a decay liability after the short closes | **positive** — the whole point; collects more near-leg decay than the single far leg pays |
| [[vega]] | net **long** — benefits from rising back-month [[dvol|DVOL]] / term-structure steepening | net **short** — benefits from DVOL compression; hurt by a spike until the far wing offsets |

Single most important fact: a long-heavy ratio calendar is **short gamma / long vega before the near expiry and long gamma / long vega after it.** Misreading which phase you are in is the classic way to mis-hedge this structure.

## Market view / when to use

- **Long-heavy (convexity):** you expect BTC/ETH to be quiet near-term (harvest the near-leg credit) then make a **directional move** the far legs can ride — ideal when a catalyst falls *after* the near expiry but *before* the far. Low-to-mid [[dvol|DVOL]] with expected back-month expansion.
- **Short-heavy (income):** you expect BTC/ETH **range-bound and DVOL to compress**, and you accept a tail you have only partially insured with the far wing. Use sparingly and small in crypto.
- **Reverse (buy near / sell far):** you expect a **near-term DVOL spike** (into a known event) larger than the back-month's — long near gamma.
- **Term-structure precondition:** standard direction needs **contango or flat** (front DVOL ≤ back); steep backwardation fights the curve.

## Adjustments & management

- **Short-leg target:** buy back the near leg at **50-85% of its max decay** (long-heavy: 75-85%; short-heavy: ~50% — take the tail off early).
- **Disposition after the near closes:** long-heavy — hold or roll the surviving far legs as a directional/convex bet; short-heavy — decide whether to close the far wing or leave it as residual protection.
- **Loss thresholds:** exit at ~**2-3× credit** (short-heavy) or ~**50% premium loss** (long-heavy).
- **Time stop:** close if spot has not moved as expected by the near leg's mid-life (~50% of DTE elapsed).
- **DVOL-regime flip:** a term-structure inversion mid-trade (front DVOL jumping above back) is a strong exit — the calendar's edge has flipped.
- **Never carry the near shorts into their final days near the money** — crypto's 24/7 gaps make short-heavy gamma acutely dangerous with no session close.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] BTC/ETH only — a ratio calendar needs **liquid same-strike depth in two expiries**, which alt options do not offer.
- **[[dvol|DVOL]] term structure is the substrate:** the trade is long or short back-month vega against the front; the *slope* of the DVOL curve sets entry economics. Contango favours standard direction; backwardation favours the reverse.
- **European cash settlement — no pin/assignment, no corporate-action drift:** European, cash-settled to the ~30-minute index TWAP at **08:00 UTC**. The near shorts **cannot be assigned early**, and with **no dividends or splits** in crypto the ratio never gets distorted by corporate actions — two of the equity ratio calendar's worst headaches vanish.
- **Inverse vs linear/USDC:** prefer **USDC-margined (linear)** so the ratio's P&L and breakevens are clean USD. **Inverse (coin-margined)** legs are BTC/ETH-settled with quanto curvature that compounds the already-complex shape — use only if the embedded coin delta is intended.
- **24/7 & the short-heavy tail:** the far wing is *slow*; a fast overnight gap can blow past the near shorts before the wing appreciates. In crypto this makes the **short-heavy variant materially more dangerous than in equities** — size it small or avoid it in an unsettled tape.
- **[[funding-rate|Perp-funding]] interaction:** funding shapes skew and near-term vol, tilting whether a call- or put-side ratio and which strike is the cheaper build; the residual directional leg can be delta-hedged with the perp, paying or collecting funding.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 treatment** — credits and gains are ordinary/short-term (US) or trader-status-dependent (AU).
- **Margin:** Deribit portfolio margin nets the legs, but a ratio's residual (extra long or extra short) carries standalone margin/tail — check the margin the platform assigns to the *net* short in a short-heavy build.

## Risks

- **Term-structure inversion mid-trade:** a DVOL spike inverts contango; long-heavy variants get crushed (long-vega far leg benefits less than the short-vega near leg loses when the curve re-flattens).
- **Wrong-ratio-for-regime:** long-heavy in a quiet, contango, range-bound tape just drains theta; short-heavy in a vol-spike regime exposes the net short to a fast gap before the wing kicks in.
- **Short-heavy gap tail:** the crypto-specific killer — an unbounded 24/7 gap past the near shorts, far exceeding the credit, before the slow far wing helps. Resembles a [[short-strangle]] tail until the wing offsets.
- **Back-leg liquidity:** far-dated same-strike depth is thinner even on BTC/ETH; repair slippage can be 2-3× entry.
- **Greeks-phase misjudgement:** hedging as if long gamma when still short gamma (or vice versa) before the near expiry.
- **DVOL crush on the long legs** (long-heavy): the far legs bleed vega even if spot cooperates.

## Worked crypto example

**Long-heavy 1:2 call ratio calendar on BTC, bullish thesis, contango term structure (USDC-margined).**

- 5 July 2026: BTC **$60,000**. Near-month (Jul, 14 DTE) [[dvol|DVOL]] 46, back-month (Sep, 68 DTE) DVOL 52 — contango. A large catalyst (major ETF decision) sits in early September, after the near expiry and before the far.
- **Trade:** SELL 1 BTC Jul $62,000 call @ **$1,400**; BUY 2 BTC Sep $62,000 calls @ **$3,600** each.
- **Net cost:** −$1,400 + $7,200 = **$5,800 debit** per structure.
- **19 Jul (near expiry):** BTC drifts to $59,500; the Jul $62k call decays to ~$300. Buy it back → captured ~$1,100 of the $1,400 (≈79%). Surviving position: **long 2 Sep $62k calls** at adjusted basis ($7,200 − $1,100) = $6,100 / 2 = $3,050 each.
- **Early Sep (catalyst):** the ETF decision sends BTC to $70,000; the Sep $62k calls jump to ~$9,200 each. Close both for **$18,400**. Net P&L: $18,400 − $6,100 = **+$12,300** (≈ +212% on the adjusted basis; +212% context vs the $5,800 initial debit).
- **Failure branch:** if BTC had stalled near $60k into September and DVOL crushed, the two Sep longs would bleed toward the net debit — loss capped near the ~$5,800 debit less the ~$1,100 near-leg credit already banked.

## Sources

- [[greeks-live]] / [[deribit]] documentation — [[dvol|DVOL]] index and term structure, IV surface, USDC (linear) vs inverse settlement, European 08:00 UTC cash settlement, portfolio-margin netting.
- Natenberg, *Option Volatility & Pricing* — calendar/ratio Greeks and term structure (the phase-shifting gamma/vega); McMillan, *Options as a Strategic Investment* — calendar and diagonal ratios. Mechanics port to crypto; the short-heavy gap tail and DVOL-crush risk are sharper.

## Getting the Data (CryptoDataAPI)

The [[dvol|DVOL]] level, its **term structure**, and per-strike IV come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, funding, dealer-gamma, and options-flow context to time the ratio and choose the tilt.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): picks long-heavy vs short-heavy
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (pin vs cascade context near the shared strike)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the skew/term-structure driver
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (positioning context)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the gap that breaks a short-heavy ratio

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol vs DVOL
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for roll/backtest studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface, DVOL, and term structure come from Deribit / [[greeks-live]].

## Related

- [[calendar-spread]] — the 1:1 parent structure
- [[diagonal-spread]] — a calendar with a strike offset
- [[ratio-spread]] — the same-expiration ratio (sibling structure)
- [[iron-condor]], [[short-strangle]] — short-vol siblings whose tail the short-heavy variant resembles
- [[crypto-options-volatility-selling]] — the parent short-vol book
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and term-structure source
- [[dvol]], [[implied-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]] — the perp linkage shaping skew and the residual delta hedge
- [[variance-risk-premium]] — the structural edge in the near leg
- [[max-pain]], [[gamma-exposure]] — dealer-positioning / pinning context
- [[section-1256-contracts]] — the tax treatment crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that shape-shift across the near expiry
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
