---
title: "Iron Condor"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, crypto, derivatives, volatility, mean-reversion, bitcoin, ethereum]
aliases: ["IC", "Iron Condor Spread", "Crypto Iron Condor"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[crypto-options-volatility-selling]]", "[[iron-butterfly]]", "[[reverse-iron-condor]]", "[[jade-lizard]]", "[[short-strangle]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Iron Condor

## Overview

The iron condor is a **market-neutral, defined-risk** options structure that profits when the underlying stays inside a range. It is two [[credit-spread|credit spreads]] sold simultaneously: a short put spread below spot and a short call spread above it. You collect premium from both wings and keep the maximum credit if the underlying finishes between the two short strikes at expiry. Maximum loss is capped at the width of the wider spread minus the total credit received. It is the workhorse [[crypto-options-volatility-selling|short-volatility]] structure — a defined-risk way to sell the [[variance-risk-premium]] on a market whose tail is genuinely fat.

On [[deribit]] BTC and ETH options, the iron condor is the preferred expression of a short-vol view because the long protective wings hard-cap the tail that a naked [[short-strangle]] leaves open — and in crypto that tail is not theoretical (BTC has printed −50% in 24h and −12% in 60s). The trade thrives when DVOL (Deribit's 30-day implied-vol index) is elevated relative to subsequently realized volatility, and it bleeds in a trend or a vol shock.

## Construction

Four legs, one expiry, cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Sell 1 put | ~15-20Δ OTM below spot | short put spread |
| 2 | Buy 1 put | ~8-10Δ, further OTM | protective lower wing |
| 3 | Sell 1 call | ~15-20Δ OTM above spot | short call spread |
| 4 | Buy 1 call | ~8-10Δ, further OTM | protective upper wing |

- **Strike selection:** short strikes at 15-20 delta target ~70-85% probability of expiring OTM. Long wings sit one to a few strikes further out and define the loss.
- **Ratios:** 1:1:1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net credit:** the sum of the two short premiums minus the two long-wing premiums. Aim to collect **≥ 1/3 of a wing's width** as credit. Balanced condors use equal-width wings; skew-tilted condors widen the richer wing (see *Crypto specifics*).
- **Tenor:** 21-45 DTE is the theta-rich zone. Avoid weeklies (gamma too hot for crypto's continuous gaps) and > 60 DTE (vega exposure to a DVOL regime shift dominates).

## Payoff & breakevens

- **Max profit** = net credit, when spot is between the two short strikes at expiry.
- **Max loss** = wider spread width − net credit, when spot is at or beyond either long wing.
- **Lower breakeven** = short put strike − net credit.
- **Upper breakeven** = short call strike + net credit.

The payoff is a flat-topped plateau (the full-credit zone between the shorts) sloping down to two capped-loss floors at the wings — a "table" rather than the iron fly's "tent."

## Greeks profile

- **Delta:** ~0 at entry (balanced). Flips positive if spot falls toward the put spread, negative if it rises toward the call spread. A skew-tilted condor carries a small starting delta.
- **Gamma:** negative throughout — the position dislikes movement, and the short gamma accelerates as spot approaches a short strike near expiry. In crypto this bites continuously (no market close to cap an overnight move).
- **Theta:** positive — the income engine. Decay is slower than an [[iron-butterfly]] (strikes are OTM, less extrinsic value) but the profit zone is far wider.
- **Vega:** negative — the structure profits from falling implied vol (DVOL crush after entry) and loses when DVOL spikes. This is the dominant early-life P&L driver.

## Market view / when to use

- You expect BTC/ETH to **range** or grind through the life of the trade — no trend, no vol shock.
- **DVOL is elevated** (roughly the 40th-90th percentile of its trailing year): premium is fat enough to pay for the wings and the tail, but you are not selling into an active vol shock.
- **VRP confirmation:** DVOL − 30-day realized vol > ~5 vol points (crypto's healthy-premium threshold; wider than the SPX ~2-point rule because both readings run higher and noisier).
- You want a **defined-risk** short-vol expression rather than a naked strangle — essential in crypto.

## Adjustments & management

- **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly). Do not grind for the last few dollars into expiry-week gamma.
- **Time stop:** close at **10-14 DTE** — crypto gamma accelerates faster into expiry than equity gamma because gaps are unbounded and continuous.
- **Roll the tested side:** if spot approaches one short strike, buy back the threatened spread and sell a new one further out in price and/or time for a credit. Rolling the *untested* side down/up toward spot collects extra credit but narrows the range.
- **Vol-shock kill:** flatten immediately if DVOL rises **> 50% in a session** or position delta exceeds **2× entry delta**. This is the explicit tail circuit-breaker.
- **Convert to an [[iron-butterfly]]** or add a same-strike spread only if you are deliberately re-centering; otherwise close and re-open cleanly.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the overwhelming majority of crypto options open interest — for BTC and ETH it is effectively "the market." OKX and Binance run smaller books. **Alt options (SOL and below) are too thin for a clean four-leg condor** — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options so the payoff diagram and breakevens are clean USD numbers. **Inverse (coin-margined) options embed a quanto-like curvature** — your collateral is BTC/ETH, so its USD value moves with spot exactly as the position does, distorting the textbook plateau and adding wrong-way risk on the put wing. Only use inverse if the embedded coin delta is intended.
- **DVOL regime gate:** open new condors only inside the ~40th-90th DVOL percentile band. Below ~40th the premium is too thin to pay for the tail; above ~90th you are likely selling into a vol shock.
- **24/7 & weekend gaps:** there is no close and no overnight gap protection, but also continuous trading. Weekend books thin out; a thin-liquidity weekend headline can gap spot through a short strike at 03:00 UTC with no chance to react — the reason defined-risk wings (not a naked strangle) are non-negotiable. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index, so there is **no pin/assignment risk** the way US single-stock condors have.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — every leg is an ordinary capital-gains event (short-term at full marginal rates in the US; trader-status-dependent CGT/income treatment in AU). The after-tax net is materially below an SPX condor's.
- **Perp funding interaction:** crypto skew is set by the [[perpetual-futures|perp]] book, not by hedgers. When [[funding-rate|funding]] is richly positive (leveraged longs paying), 25-delta call skew firms and the call wing is richer to sell; after a selloff, put skew fattens. Delta-hedging the condor's residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on cheap OTM wings and is a real drag on a four-leg structure.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **52** (≈60th percentile); 30-day realized vol **44** → VRP = 52 − 44 = **8 vol points** (healthy). 33 DTE. Funding mildly positive (+0.02%/8h → slight call-skew richness).

**Trade (per 1-ETH contract):**
- Sell 18Δ call @ **$3,400** for **$40**; buy 8Δ call @ **$3,650** for **$16** → call spread credit $24.
- Sell 18Δ put @ **$2,600** for **$48**; buy 8Δ put @ **$2,350** for **$20** → put spread credit $28.
- **Net credit = $52.** Wing width = $250 each. **Max loss = $250 − $52 = $198.**
- **Breakevens:** $3,400 + $52 = **$3,452** (up); $2,600 − $52 = **$2,548** (down).

**Path A — base case (range).** Over three weeks ETH oscillates $2,850-$3,150 and DVOL drifts to 46. The condor decays to ~$24; close at 54% of credit for **+$28/contract**. Perp delta-hedging roughly nets to zero (small funding collection offsets slippage).

**Path B — moderate spike.** A macro headline pushes ETH −6% and DVOL 52 → 70. The put wing is tested; hedging goes continuous. Mark −$40. Vol reverts over the next week; close at the 12-DTE time stop for **+$15/contract** (the long put wing capped the drawdown).

**Path C — vol shock.** ETH gaps −18% overnight; DVOL 52 → 110. **Vol-shock kill triggers at the open.** The short put is deep ITM but the long $2,350 put caps the loss near the $198 floor. Net ≈ **−$180/contract** — roughly the sleeve's monthly carry, and the exact scenario the defined-risk wings exist to survive.

## Sources

- [[greeks-live]] / [[deribit]] documentation — DVOL construction, IV surface, USDC-margined (linear) vs inverse option settlement, taker-fee premium cap, 08:00 UTC cash settlement.
- [[book-option-volatility-and-pricing]] — Natenberg on multi-leg credit spreads, gamma risk near expiry, and the volatility risk premium these structures harvest (mechanics port to crypto; costs and tails do not).
- tastytrade 15-20Δ condor / 50%-profit / time-stop management studies — mechanics port directly; sizing and stops must be tightened for the crypto tail.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the complementary options-flow, volatility-regime, dealer-gamma, and funding context used to *time* the condor and read the tape.

**Live:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (dealer-positioning context for strike selection)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): the entry gate
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): whether spot is likely pinned or cascade-prone
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crypto skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the vol shock that breaks a short-premium structure

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

## Related

- [[crypto-options-volatility-selling]] — the parent short-vol book; the iron condor is its core defined-risk structure
- [[iron-butterfly]] — the ATM-bodied cousin: higher credit, narrower zone
- [[reverse-iron-condor]] — the mirror trade (long vol / breakout)
- [[jade-lizard]] — short put + short call spread; no upside risk
- [[short-strangle]] — the undefined-risk version this improves on
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and surface source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[gamma-exposure]], [[max-pain]] — dealer-positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
