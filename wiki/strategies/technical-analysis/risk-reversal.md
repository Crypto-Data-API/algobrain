---
title: "Risk Reversal"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, risk-reversal, directional, synthetic, skew, hedging, derivatives]
aliases: ["Combo", "Synthetic Forward", "25-Delta Risk Reversal", "Crypto Risk Reversal", "Collar Without Coin"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[skew-trading]]", "[[seagull-option]]", "[[covered-call]]", "[[jade-lizard]]", "[[straddle-strangle]]", "[[crypto-options-volatility-selling]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[delta]]", "[[vega]]", "[[deribit]]", "[[greeks-live]]", "[[cryptodataapi]]"]
---

# Risk Reversal

## Overview

A **risk reversal** combines a **long OTM call with a short OTM put** (bullish) or a **long OTM put with a short OTM call** (bearish). The short leg finances the long leg, usually producing a **zero-cost or very low-cost** entry, and the result behaves like a **synthetic forward** — strong directional exposure with leverage and little upfront capital. In crypto it is doubly important: beyond being a directional structure, the **25-delta risk reversal is the market's standard measure of [[volatility-surface|volatility skew]]** — the price of the call wing minus the put wing — quoted continuously by [[deribit]] and [[greeks-live]]. Trading a risk reversal is therefore both a directional bet and a **skew bet**: you sell whichever wing the leveraged crowd has overbid and buy the cheaper one (see [[skew-trading]]).

## Construction

Two OTM legs, same expiry `T`, on [[deribit]] BTC/ETH:

- **Bullish risk reversal** — sell 1 OTM put (e.g. 25-delta, strike `K_p < S`) + buy 1 OTM call (e.g. 25-delta, strike `K_c > S`).
- **Bearish risk reversal** — sell 1 OTM call + buy 1 OTM put.
- **Strikes** are chosen at matching deltas (the "25-delta risk reversal" convention) or skewed to conviction. Wider strikes → less premium, wider dead zone.
- **Net cost** depends on skew: if the short wing is richer than the long wing, the structure prints a **credit**; if the long wing is richer, a small **debit**. In crypto, whether puts or calls are richer flips with [[funding-rate|perp funding]] and market regime — unlike equities' near-permanent put skew.

Deribit contracts are 1 BTC / 1 ETH, **European-exercise and cash-settled** (no early assignment). Choose USDC-margined (linear) for clean USD P&L; inverse (coin-margined) embeds a coin delta on the short-put collateral.

## Payoff & breakevens

A bullish risk reversal replicates a **long synthetic forward with a gap** between the strikes:

- **Above `K_c`**: profit rises ~1:1 with spot (the long call) — **unbounded upside**.
- **Below `K_p`**: loss grows ~1:1 with spot (the short put) — **downside like a long spot/perp position** below the put strike.
- **Between `K_p` and `K_c` (the "dead zone")**: both legs are OTM; P&L ≈ the net credit/debit, roughly flat.
- **Breakeven**: near `K_p + |debit|` or below `K_c − credit` depending on net cost; for a true zero-cost RR, breakeven sits inside the dead zone near spot.
- **Max loss (bullish)**: `K_p − 0` in the limit (short put to zero), i.e. essentially the full downside of a long position below `K_p`, minus any credit. **Max gain**: unbounded.

The bearish risk reversal is the mirror: unbounded profit as spot falls below `K_p`, unbounded-like loss as it rises above `K_c`.

## Greeks profile

A risk reversal is primarily a **delta and skew** trade, with small gamma and small *level*-vega when the wings are symmetric:

| Greek | Bullish RR | Comment |
|---|---|---|
| [[delta]] | Strongly **positive** (~+0.5) | The point of the trade — synthetic long exposure |
| Gamma | ≈ 0 | Long-call gamma offsets short-put gamma |
| [[vega]] | ≈ 0 to level, **long skew** | Insensitive to parallel IV shifts; sensitive to the *put-vs-call* skew — gains if call skew firms relative to puts |
| [[theta]] | Small, sign depends on net credit/debit | A credit RR collects small theta; a debit RR pays it |

The key exposure is **skew (differential vega across the wings)**: a bullish risk reversal is long call-skew / short put-skew. When the 25-delta risk-reversal number moves in your favour (calls bid up relative to puts), the position gains independently of spot.

## Market view / when to use

- **Directional conviction with a skew tailwind.** Put on a bullish RR when you are bullish **and** put skew is rich (puts overpriced) — you get paid to be long. Put on a bearish RR when you are bearish **and** call skew is rich (crowded leveraged longs, richly positive funding).
- **Skew relative value (`[[skew-trading]]`).** Even delta-hedged, the RR expresses "the market is paying too much for downside vs upside" (or vice versa) — a mean-reversion bet on the 25-delta risk-reversal number back toward its regime norm.
- **Leveraged replacement for spot/perp.** A zero-cost bullish RR gives long BTC/ETH exposure without posting the full notional — cheaper carry than a leveraged perp long in some funding regimes (no funding on the option legs), at the cost of the dead zone and the short-put tail.
- **Financing a hedge.** A bearish RR (long put funded by short call) protects a spot bag cheaply — the crypto analogue of a [[collar]] without the coin.

## Adjustments & management

- **Roll the short wing** down-and-out (bullish RR, if spot approaches the short put) to avoid the tail; or buy it back to remove the undefined leg.
- **Cap the tail → seagull.** Add a further-OTM long option beyond the short wing to convert the RR into a defined-risk [[seagull-option]] — the standard way to bound the naked side.
- **Bank the skew.** If the trade was a skew bet and the 25-delta RR has reverted, close for the skew P&L regardless of spot.
- **Delta-hedge the level** on the Deribit perp if you only want the skew exposure; the hedge pays/collects [[funding-rate|funding]].
- **Manage into expiry** as the dead zone shrinks — a small spot move near expiry flips the position from flat to directional quickly.

## Crypto specifics

- **The RR *is* the crypto skew metric.** The **25-delta risk reversal** (call IV − put IV) published by [[deribit]] / [[greeks-live]] is the headline skew gauge for BTC/ETH. Trading the structure is trading that number.
- **Skew oscillates with funding.** Unlike equities' permanent put skew, crypto skew flips: in leveraged bull runs with richly positive [[funding-rate|funding]], **call skew can trade rich to puts** (a "perpetual-heavy" surface), making bearish risk reversals a credit; after a crash, put skew firms and bullish risk reversals pay. Read funding and perp OI before choosing the direction.
- **Inverse vs linear settlement.** On inverse (coin-margined) contracts the short put's assignment-equivalent exposure and its collateral are both in the coin — a quanto-like double hit if spot falls; **USDC-margined (linear)** removes it. Match collateral to intent.
- **European, cash-settled → no early assignment**, but the short wing still carries full undefined tail risk to the index at expiry.
- **24/7 & weekend gaps.** The short wing can be blown through by an unbounded weekend gap with no ability to trade out — the single biggest hazard of an uncapped crypto RR. Size the short leg for a Black-Thursday move, not an average day.
- **No §1256.** Offshore Deribit contracts get no [[section-1256-contracts|§1256]] 60/40 treatment.
- **Alt-option liquidity.** Clean 25-delta wings exist mainly on BTC/ETH; alt risk reversals are wide and shallow.

## Risks

- **Naked short-wing tail** — a bullish RR loses like long spot below `K_p`, and crypto's weekend/overnight gaps are unbounded. This is the defining risk.
- **Skew regime shift** — the skew you sold can get *richer* before it reverts (the RR number runs against you).
- **Dead-zone drag** — range-bound tape leaves the trade flat while capital/margin is committed.
- **Margin intensity** — the short wing consumes Deribit portfolio margin that expands on a DVOL spike.
- **Coin-margin wrong-way risk** on inverse contracts.
- **Directional dependency** — a pure RR needs the move; without a skew or spot thesis it is idle risk.

## Worked crypto example

**Setup (ETH, 30 DTE, bullish + put skew rich).** ETH spot **$3,000** after a sharp dip; DVOL elevated and **put skew rich** (25-delta risk reversal deeply negative — puts bid). You are bullish on a recovery.

**Trade — bullish risk reversal (USDC-margined):**
- **Sell** 1 ETH 25-delta **put @ $2,600** for ≈ **$130**
- **Buy** 1 ETH 25-delta **call @ $3,450** for ≈ **$110**
- **Net credit ≈ $20**; delta ≈ +0.5 (synthetic long). Dead zone $2,600–$3,450.

**Path A — recovery (the win).** ETH rallies to **$3,700**. The call is worth ≈ $250, the short put expires worthless. Profit ≈ $250 + $20 = **≈ +$270** on near-zero capital. If put skew *also* normalized on the way up, the short put decayed even faster — a skew tailwind on top of the delta gain.

**Path B — dead zone.** ETH finishes at **$3,100** (between strikes). Both legs expire worthless. P&L = **+$20** (the credit).

**Path C — further crash (the tail).** ETH gaps to **$2,300** over a weekend. The short put is ≈ $300 ITM. Loss ≈ $300 − $20 = **≈ −$280**, and worse the further it falls — identical downside to holding spot below $2,600. This is why a disciplined desk caps it into a [[seagull-option]] by buying a $2,300 put.

## Getting the Data (CryptoDataAPI)

The **skew inputs** a risk reversal trades — the 25-delta risk-reversal number and the raw IV surface — are **Deribit / [[greeks-live]]** products and are *not* served by CryptoDataAPI. [[cryptodataapi]] supplies the drivers and context: funding (the skew driver), options OI/max-pain, dealer gamma, and vol regime.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding; richly positive → call-skew rich (favours bearish RR credit)
- `GET /api/v1/market-intelligence/funding-rates` — cross-exchange funding
- `GET /api/v1/derivatives/open-interest?coin=BTC` — perp OI (crowded-long context for skew)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] strike
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory / cascade risk into the short wing)
- `GET /api/v1/volatility/regime` — vol regime (context for wing pricing)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history (skew-driver backtest)
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]]

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[skew-trading]] — trading the 25-delta risk-reversal number itself
- [[seagull-option]] — extends the RR with a third leg to cap the naked tail
- [[covered-call]], [[collar]] — related directional/hedging structures
- [[jade-lizard]] — short put + call spread, a cousin credit structure
- [[straddle-strangle]] — non-directional vol vs the RR's directional/skew nature
- [[crypto-options-volatility-selling]] — where skew selection informs the vol book's wings
- [[funding-rate]] — the perp linkage that flips crypto skew
- [[volatility-surface]], [[implied-volatility]] — what the wings price
- [[deribit]], [[greeks-live]] — venue and skew/surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — combos / synthetic forwards and their risk profile.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — risk reversals and volatility skew.
- [[deribit]] / [[greeks-live]] documentation — 25-delta risk-reversal skew quoting, European cash settlement, inverse vs USDC-margined contracts.
