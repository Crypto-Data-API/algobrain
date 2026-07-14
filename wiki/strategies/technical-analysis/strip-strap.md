---
title: "Strip and Strap"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, strip, strap, volatility, straddle-variant, directional-vol, long-volatility]
aliases: ["Strip", "Strap", "Strip Straddle", "Strap Straddle"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[straddle-strangle]]", "[[straddle]]", "[[short-straddle]]", "[[reverse-iron-condor]]", "[[implied-volatility]]", "[[gamma-scalping]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[cryptodataapi]]"]
---

# Strip and Strap

## Overview

The **strip** and **strap** are directionally biased variants of the [[straddle-strangle|long straddle]]. Both are long-volatility structures that profit from a large move in either direction, but they load extra contracts on one side to express a **lean**. A **strip** buys 1 ATM call and **2 ATM puts** — a bearish-volatility bias that pays more if the underlying falls. A **strap** buys **2 ATM calls** and 1 ATM put — a bullish-volatility bias that pays more if it rallies. They are the tool for "I expect a big move and, if forced to guess, I lean *this* way" — common in crypto around asymmetric catalysts (a token unlock skews bearish; an ETF approval or upgrade skews bullish). Traded on [[deribit]] BTC/ETH.

## Construction

Same strike `K ≈ S`, same expiry `T`, unequal leg counts:

- **Strip** — buy **1 call + 2 puts** at strike `K`. Debit = call premium + 2 × put premium.
- **Strap** — buy **2 calls + 1 put** at strike `K`. Debit = 2 × call premium + put premium.

On Deribit each contract is 1 BTC / 1 ETH, cash-settled to the Deribit index. Use 21–45 DTE to give the move time while limiting the compounded [[theta]] of three long legs. USDC-margined (linear) contracts give clean USD P&L; inverse (coin-margined) contracts embed a coin delta on top of the intended structure.

## Payoff & breakevens

Let `D` = total debit. Both structures have **defined risk (`D`) and undefined reward**, but with an **asymmetric slope** — the favored side gains twice as fast because two contracts work there.

**Strap (bullish bias):**
- Upside breakeven = `K + D/2` (two calls halve the up-move needed)
- Downside breakeven = `K − D`
- Above `K`: profit = `2·(S_T − K) − D`; below `K`: profit = `(K − S_T) − D`

**Strip (bearish bias):**
- Downside breakeven = `K − D/2` (two puts halve the down-move needed)
- Upside breakeven = `K + D`
- Below `K`: profit = `2·(K − S_T) − D`; above `K`: profit = `(S_T − K) − D`

| Scenario | Strip | Strap |
|---|---|---|
| Large move **down** | 2 puts profit heavily | 1 put profits |
| Flat at `K` | Max loss = `D` | Max loss = `D` |
| Large move **up** | 1 call profits | 2 calls profit heavily |

## Greeks profile

Long gamma, long vega, short theta — like the straddle, but with a **directional delta tilt** at inception:

| Greek | Strip | Strap | Comment |
|---|---|---|---|
| [[delta]] | Net **negative** (≈ −0.5) | Net **positive** (≈ +0.5) | Extra put/call skews the neutral point |
| Gamma | Positive, extra on downside | Positive, extra on upside | Two same-side contracts double the convexity there |
| [[vega]] | Positive (larger than straddle) | Positive (larger than straddle) | Three long legs = more vega to a DVOL move |
| [[theta]] | Negative (larger than straddle) | Negative (larger than straddle) | Three legs decaying |

The larger vega means a **DVOL/IV expansion alone** can profit the position before any spot move — but the larger theta means a quiet tape bleeds faster than a plain straddle.

## Market view / when to use

- You expect a **large move** but hold a directional lean: a strip for a bearish tilt (impending unlock, deleveraging, macro risk-off), a strap for a bullish tilt (ETF/listing catalyst, upgrade, short-squeeze setup).
- **DVOL is cheap** (lower part of its trailing-year range / "compressed" [[volatility-regime|regime]]) so the extra leg is affordable.
- You want **more convexity in your favored direction than a straddle gives**, without abandoning the other-side protection entirely.
- A strap is often preferred over an outright long call when you want upside gamma *plus* crash insurance; a strip over an outright long put when you want downside gamma but respect crypto's violent relief rallies.

## Adjustments & management

- **Bank the favored side**: after a move your way, sell the two same-side contracts into strength and keep (or close) the lone opposite leg.
- **Rebalance to neutral**: if the move goes the "wrong" (lean-opposite) way but is large, the single leg on that side still profits — manage it like a straddle winner.
- **Delta-hedge into a gamma scalp**: neutralize the inception delta tilt on the Deribit perp and scalp the range; the hedge pays/collects [[funding-rate|funding]].
- **Roll before the theta cliff** (final 1–2 weeks) if the thesis is intact — three long legs decay quickly into expiry.
- **Cut on IV crush**: post-catalyst DVOL collapse hits three long-vega legs harder than a straddle's two.

## Crypto specifics

- **Venue & underlyings**: [[deribit]] BTC/ETH; [[greeks-live]] for building and monitoring the three-leg Greeks. Alt option chains are too thin for a clean strip/strap.
- **Inverse vs linear settlement**: inverse (coin-margined) contracts add a coin delta that *compounds* the deliberate directional lean — usually undesirable; **USDC-margined (linear)** keeps the tilt clean.
- **DVOL**: buy the structure when [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] is low; the extra leg's premium makes cheap vol even more important than for a straddle. **DVOL/IV come from Deribit / [[greeks-live]], not CryptoDataAPI.**
- **24/7 & weekend gaps**: continuous trading and thin-weekend air-pockets feed the long-gamma legs; the directional lean pays off best precisely on the unbounded weekend gap.
- **No §1256**: offshore Deribit contracts get no [[section-1256-contracts|§1256]] 60/40 treatment.
- **Perp-funding interaction**: [[funding-rate|funding]] biases the surface — richly positive funding firms call skew, cheapening the strap's calls; deeply negative funding cheapens the strip's puts. Read funding when choosing which variant and how to hedge.
- **Alt-option liquidity**: BTC/ETH only in practice.

## Risks

- **Higher premium and higher theta** than a plain straddle — three legs decaying means a quiet tape bleeds faster.
- **Wrong lean**: if the big move comes against the bias, the single leg still profits but you overpaid for the doubled side.
- **[[iv-crush|DVOL crush]]** hits the larger vega harder.
- **Wide Deribit bid-ask across three legs** plus premium-capped taker fees raise the move you actually need.
- **Coin-margin non-linearity** on inverse contracts amplifies the lean unintentionally.

## Worked crypto example

**Setup (BTC, 30 DTE, bullish lean → strap).** BTC spot **$60,000**, DVOL **50** and compressed; a spot-ETF options-listing decision (skewed bullish) lands inside the month. ATM 60,000 call ≈ $3,450, ATM 60,000 put ≈ $3,450.

**Trade — strap (USDC-margined):** buy **2 × 60,000 calls + 1 × 60,000 put**. Debit `D` = 2×3,450 + 3,450 = **$10,350**.
- Upside breakeven = 60,000 + 10,350/2 = **$65,175** (needs +8.6%)
- Downside breakeven = 60,000 − 10,350 = **$49,650** (needs −17.25%)

**Path A — bullish resolution (the target).** BTC rallies to **$70,000**. The two calls are worth ≈ 2×$10,300 = $20,600; the put ≈ $0. Value ≈ $20,600, profit ≈ **+$10,250 (+99%)** — roughly double what the same $10k in a straddle would have made on this up-move.

**Path B — sharp drop (still protected).** BTC falls to **$50,000**. The lone put is worth ≈ $10,000; the calls ≈ $0. Value ≈ $10,000, ≈ **−$350** — near breakeven; the down-side single leg cushions the "wrong-way" move.

**Path C — muted move + IV crush (the loss).** BTC drifts to $61,000 and DVOL crushes 50 → 38. All three legs bleed; value ≈ $4,500, loss ≈ **−$5,850 (−57%)** — the modal outcome, worse than a straddle because of the extra long leg. Size ≤ 1–3% of book.

## Getting the Data (CryptoDataAPI)

Implied vol / **DVOL** — the cheap-vs-rich gauge for buying a strip/strap — is a **Deribit / [[greeks-live]]** product, not served by CryptoDataAPI. [[cryptodataapi]] supplies the surrounding context: vol regime, the catalyst calendar (to time and *direct* the lean), options OI/max-pain, dealer gamma, and funding (the skew driver).

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime; "compressed" flags cheap-vol setups to buy
- `GET /api/v1/event/calendar` — forward catalyst calendar (unlock/macro/listing bias) to choose strip vs strap
- `GET /api/v1/event/regime` — catalyst regime + directional bias
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver informing the lean
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]]
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory / cascade risk)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (RV vs DVOL)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[straddle-strangle]] — the symmetric long-vol parent
- [[straddle]] — the conceptual umbrella
- [[short-straddle]] — the short-vol opposite
- [[reverse-iron-condor]] — a defined-risk breakout alternative
- [[gamma-scalping]] — dynamically hedging the long gamma
- [[deribit]], [[greeks-live]] — venue and DVOL/surface source
- [[funding-rate]] — the perp linkage that biases crypto skew
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — strip and strap construction and payoff.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — directional-volatility structures and their Greeks.
- [[deribit]] / [[greeks-live]] documentation — contract specs, DVOL, inverse vs USDC-margined settlement.
