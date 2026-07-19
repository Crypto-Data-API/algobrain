---
title: "Credit Spread"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, volatility, swing-trading, bitcoin, ethereum]
aliases: ["Credit Spread", "Credit Spreads", "Vertical Credit Spread", "Bull Put Spread", "Bear Call Spread", "Crypto Credit Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[short-put-spread]]", "[[iron-condor]]", "[[vertical-spread]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[variance-risk-premium]]", "[[max-pain]]", "[[gamma-exposure]]", "[[section-1256-contracts]]", "[[trade-repair-and-rolling]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Credit Spread

## Overview

A credit spread sells a higher-premium option and buys a lower-premium option of the **same type** (both calls or both puts), **same expiry**, different strikes — collecting a net credit at entry. It is the canonical **defined-risk, positive-theta, short-vega** building block of premium selling: the sold near-money leg decays faster than the bought further-OTM leg, and the full credit is kept if both expire worthless. Maximum loss is capped at the strike width minus the credit, so unlike a naked short option the tail is hard-bounded. It comes in two directional forms — the **bull put spread** (bullish) and the **bear call spread** (bearish) — and two of them stacked make an [[iron-condor]].

In crypto this is the workhorse defined-risk expression of a short-vol or directional-lean view on [[deribit]] BTC/ETH options. The seller harvests the crypto [[variance-risk-premium]] (DVOL persistently rich to subsequently realized vol) while the long wing hard-caps a tail that in crypto is not theoretical — BTC has printed −50% in a day. Because Deribit options are **European and cash-settled**, there is no early assignment and no ex-dividend exercise trap (crypto pays no dividends), so the two classic equity credit-spread hazards simply do not exist; what replaces them is 24/7 gap risk and DVOL-shock vega.

## Construction

Two legs, one expiry, cash-settled to the Deribit index, on BTC or ETH:

| Variant | Sell (short, near-money) | Buy (long wing, further OTM) | Bias |
|---|---|---|---|
| **Bull put spread** | put at ~15-25Δ below spot | put ~8-12Δ, lower | bullish / neutral-up |
| **Bear call spread** | call at ~15-25Δ above spot | call ~8-12Δ, higher | bearish / neutral-down |

- **Strike selection:** the short strike's delta ≈ its probability of finishing ITM. A 20Δ short targets ~80% probability of expiring OTM (full credit). Wider (25-30Δ) = more credit, lower win rate, more directional tilt.
- **Width:** the gap between short and long strike sets max loss. Wider = more credit but more risk.
- **Net credit:** aim to collect **≥ 1/3 of the width**. Below ~25% the risk/reward is not worth the tail.
- **Tenor:** 21-45 DTE is the theta-rich zone. Avoid weeklies (gamma too hot for crypto's continuous gaps) and > 60 DTE (DVOL-regime vega dominates).
- **Direction from the tape:** pick the put side when the view is up/neutral, the call side when down/neutral. Crypto skew (set by the perp book) makes one side richer to sell than the other — see *Crypto specifics*.

## Payoff & breakevens

For a **bull put spread** (short put `Ks`, long put `Kl`, `Kl < Ks`, net credit `C`):

- **Max profit** = `C`, when spot ≥ `Ks` at expiry.
- **Max loss** = `(Ks − Kl) − C`, when spot ≤ `Kl`.
- **Breakeven** = `Ks − C`.

The bear call spread is the mirror: max profit `C` when spot ≤ short call; breakeven = short call `+ C`; max loss = width − `C` above the long call.

```
Bull put spread P&L at expiration

 +C  ┤                       ┌────────────────  (spot ≥ Ks: keep full credit)
     │                      /
  0 ─┼─────────────────────/───────────────────
     │                    / breakeven = Ks − C
 −ML ┤━━━━━━━━━━━━━━━━━━━━/   (spot ≤ Kl: max loss = width − C)
     └──────────────────────────────────────────
          Kl(long)     Ks(short)
```

The long wing is the single most important structural property: it flattens the loss beyond `Kl`, converting naked-short-option risk into a defined rectangle.

## Greeks profile

Bull put spread (bear call is the delta-mirror):

- **[[delta]]:** small **positive** (bullish tilt) for a put spread, small **negative** for a call spread. Grows toward the tested side as spot approaches the short strike.
- **[[gamma]]:** **negative**, but capped by the long wing. Spikes as spot nears the short strike near expiry — the basis of the time stop.
- **[[theta]]:** **positive** — the income engine; the short near-money leg decays faster than the long wing.
- **[[vega]]:** **negative**, muted by the wing — profits from falling [[dvol|DVOL]] after entry, loses on a DVOL spike. The dominant early-life P&L driver, and a real source of mid-trade drawdown even if spot has not moved.

## Market view / when to use

- **Directional lean with defined risk:** bullish → bull put spread; bearish → bear call spread. For a pure range view, stack both into an [[iron-condor]].
- **[[dvol|DVOL]] elevated** (roughly the 40th-90th percentile of its trailing year): rich premium pays for the wing and the tail, without selling into an active vol shock.
- **VRP confirmation:** DVOL − 30-day realized vol > ~5 vol points (crypto's healthy-premium threshold; wider than the SPX ~2-point rule because both readings run higher and noisier).
- You want **capital efficiency and a hard max loss** — a defined-risk alternative to a naked short put/call, essential given crypto's gap tail.

## Adjustments & management

- **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly). Do not grind the last few dollars into expiry-week gamma.
- **Loss cap:** close at **~2× the credit** received, or on a decisive breach of the short strike with the thesis broken.
- **Time stop:** close or roll at **~21 DTE** (crypto gamma accelerates faster into expiry than equity gamma — gaps are continuous and unbounded).
- **Roll out / out-and-away:** if the short strike is threatened but the thesis holds, buy back the spread and sell a new one further from spot and/or later in time **for a credit** — never pay a meaningful debit chasing price (see [[trade-repair-and-rolling]]).
- **Convert to an [[iron-condor]]:** if a put spread is tested but you expect spot to stabilise, add a bear call spread above spot to collect offsetting credit — at the cost of new upside risk.
- **DVOL-shock kill:** flatten if DVOL rises **> 50% in a session** or position delta exceeds **~2× entry delta** — the explicit tail circuit-breaker.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the overwhelming majority of crypto options open interest — for BTC and ETH it is effectively "the market." OKX and Binance run smaller books. **Alt options (SOL and below) are too thin for a clean defined-risk vertical** — stick to BTC/ETH.
- **European cash settlement — no assignment, no ex-dividend trap:** Deribit options are European, cash-settled to the ~30-minute index TWAP at **08:00 UTC**. The short leg **cannot be assigned early**, and because crypto pays **no dividends** the ex-dividend early-exercise hazard that complicates equity credit spreads simply does not exist. There is no pin/assignment risk the way US single-stock spreads have.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options for clean USD credit, breakevens, and P&L. **Inverse (coin-margined)** options are BTC/ETH-settled and embed a quanto-like curvature — the collateral's USD value moves with spot, distorting the textbook payoff and adding wrong-way risk on the put side. Use inverse only if the embedded coin delta is intended.
- **[[dvol|DVOL]] regime gate:** open new spreads inside the ~40th-90th DVOL percentile band. Below ~40th the credit is too thin to pay for the tail; above ~90th you are likely selling into a vol shock.
- **24/7 & weekend gaps:** no close and no overnight gap protection. A thin-liquidity weekend headline can gap spot through the short strike at 03:00 UTC with no chance to react — the reason the defined-risk long wing (not a naked short) is non-negotiable.
- **[[funding-rate|Perp-funding]] shapes which side to sell:** crypto skew is set by the [[perpetual-futures|perp]] book, not by hedgers. Richly positive funding (leveraged longs paying) firms 25Δ call skew, making the **call** side richer to sell; after a selloff, put skew fattens and the **put** side pays more. Delta-hedging the residual with the perp pays or collects funding.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — every leg is an ordinary short-term capital-gains event (US) or trader-status-dependent (AU). After-tax net is materially below an SPX spread's.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on cheap OTM wings and is a real drag on a two-leg structure.

## Risks

- **Vol shock / gap:** an overnight gap through both strikes produces near-instant max loss with no chance to manage — the canonical short-premium failure. The wing caps it; sizing makes it survivable.
- **Negative-vega drawdown:** a DVOL spike marks the spread against you even if spot has not moved.
- **Unfavourable risk/reward:** max loss typically exceeds max profit by 2-4×; the high win rate means one loss erases several wins — a high win rate is **not** evidence of edge.
- **Directional whipsaw:** repeated tests of the short strike in a choppy tape stack up roll costs.
- **Premium compression:** a sustained low-DVOL regime shrinks the credit until it no longer clears the tail — forcing trades there is negative-expectancy.
- **Discipline decay:** a long structurally-guaranteed winning streak tempts oversizing right before the loss cluster — the classic short-vol blowup pattern.

## Worked crypto example

**Setup (BTC, USDC-margined/linear), bull put spread.** BTC spot **$60,000**; BTC [[dvol|DVOL]] **55** (≈60th percentile); 30-day realized vol **46** → VRP = 55 − 46 = **9 vol points** (healthy). 30 DTE. Funding mildly positive. Mildly bullish-to-neutral view.

**Trade (per 1-BTC contract):**
- Sell 20Δ put @ **$54,000** for **$1,150**.
- Buy 10Δ put @ **$50,000** for **$520**.
- **Net credit = $630.** Width = $4,000. **Max loss = $4,000 − $630 = $3,370.** Credit/width ≈ 16% — thin, so in practice tighten the wing to $3,000 or move the short to 25Δ to lift the ratio; shown as-is for arithmetic.
- **Breakeven:** $54,000 − $630 = **$53,370.**

**Path A — base case.** Over three weeks BTC grinds $58k-$64k and DVOL drifts to 49. The spread decays to ~$300; close at ~52% of credit for **+$330/contract**.

**Path B — tested, thesis intact.** A macro headline pushes BTC −7% toward $55,800; the short put is threatened. Roll out-and-away to a $50,000/$46,000 spread 30 days later for a small net credit, lowering the danger zone and adding time.

**Path C — vol shock.** BTC gaps −16% overnight to ~$50,400; DVOL 55 → 105. **Kill triggers at the open.** The short $54k put is deep ITM but the long $50k put caps the loss near the $3,370 floor. Net ≈ **−$3,300/contract** — the exact scenario the wing exists to survive.

## Sources

- [[greeks-live]] / [[deribit]] documentation — [[dvol|DVOL]] construction, IV surface, USDC (linear) vs inverse settlement, taker-fee premium cap, European 08:00 UTC cash settlement.
- [[book-option-volatility-and-pricing]] — Natenberg on vertical spreads, gamma near expiry, and the variance risk premium these structures harvest (mechanics port to crypto; costs and tails do not).
- Carr & Wu (2009), "Variance Risk Premiums," *Review of Financial Studies* — the premium the short leg collects (documented for equity indices; crypto's VRP is larger and noisier).
- tastytrade 15-25Δ / 50%-profit / 21-DTE management studies — mechanics port directly; sizing and stops must be tightened for the crypto tail.

## Getting the Data (CryptoDataAPI)

[[dvol|DVOL]] and the raw IV surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the complementary options-flow, volatility-regime, dealer-gamma, and funding context used to *time* the spread and read the tape.

**Live:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (dealer-positioning context for strike selection)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): the entry gate
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): whether spot is likely pinned or cascade-prone
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the crypto skew driver (which side is richer to sell)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the vol shock that breaks a short-premium structure

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Entry gate** — `GET /api/v1/volatility/regime`: open spreads in `normal`/`mean_reverting`, never into `vol_shock`; cross-check the VRP by comparing Deribit DVOL to realized vol from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`.
- **Side selection** — `GET /api/v1/derivatives/funding-rates?coin=BTC`: richly positive funding firms call skew (sell the bear call spread); post-selloff bid put skew pays the bull put spread better.
- **Strike placement** — `GET /api/v1/market-intelligence/options` + `GET /api/v1/quant/gex`: keep short strikes clear of max-pain pin zones and cascade-prone short-gamma pockets.
- **Kill switch** — `GET /api/v1/quant/market`: a jump in `vol_spike` probability is the machine-readable form of the "DVOL +50% in a session" flatten rule; pair with `GET /api/v1/market-intelligence/liquidations` while a short strike is being tested.
- **Backtest** — spot paths from `GET /api/v1/backtesting/klines` (Binance 1h/4h/1d since 2017-08) with point-in-time regime states from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to test the entry gate honestly; option credits must come from Deribit history — CDA has no options-chain archive.
- **Tips** — poll the cached `GET /api/v1/daily` bundle hourly between management checks; append `?format=markdown` for cleaner context windows.

## Related

- [[short-put-spread]] — the bull put spread specifically; the bullish specialisation of this structure
- [[iron-condor]] — a bull put spread + a bear call spread combined (neutral, defined risk both sides)
- [[vertical-spread]] — the general vertical framework (a credit spread is a vertical sold for a credit)
- [[crypto-options-volatility-selling]] — the parent short-vol book
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and surface source
- [[dvol]], [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]] — the perp linkage that shapes crypto skew and which side to sell
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[variance-risk-premium]] — the economic source of the credit
- [[trade-repair-and-rolling]] — the rolling and adjustment framework
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
