---
title: "Double Diagonal"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, double-diagonal, diagonal-spread, income, theta, crypto, derivatives]
aliases: ["Double Diagonal Spread", "Calendarized Iron Condor"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[diagonal-spread]]", "[[calendar-spread]]", "[[iron-condor]]", "[[short-strangle]]", "[[theta]]", "[[vega]]", "[[funding-rate]]", "[[deribit]]", "[[crypto-options-volatility-selling]]", "[[trade-repair-and-rolling]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Double Diagonal

## Overview

The double diagonal combines a **diagonal call spread** and a **diagonal put spread** into one position: sell a near-term OTM call and a near-term OTM put (a front-month [[short-strangle]]) and buy longer-dated OTM options further out on each side as protection. It blends **range-bound [[theta]] income** with **calendar structure** — the short-dated legs decay fast while the longer-dated wings retain value and define the risk. Think of it as a **[[iron-condor]] whose long wings are pushed to a later expiry**, giving a wider profit tent, net-long vega, and more room to adjust.

In crypto this is a way to **collect the [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] premium on a range-bound BTC/ETH view** while keeping genuinely capped tails — essential given crypto's fat-tailed, 24/7 gaps. It sits between the pure short-vol [[crypto-options-volatility-selling|premium-selling]] book and a defined-risk condor, adding a long-vega tilt from the back-month wings.

## Construction

Four legs, two expiries, on BTC or ETH [[deribit]] options, around spot:

| Leg | Action | Side | Strike | Tenor |
|---|---|---|---|---|
| Short | Sell call | Upper | OTM above spot | Front (21-45 DTE) |
| Long | Buy call | Upper | Further OTM | Back (60-120 DTE) |
| Short | Sell put | Lower | OTM below spot | Front (21-45 DTE) |
| Long | Buy put | Lower | Further OTM | Back (60-120 DTE) |

- **Net cost:** typically a small **debit or near-neutral** at entry; the front-month shorts fund most of the back-month wings.
- The **short strikes** set the profit zone; the **long back-month wings** define maximum risk and carry residual value after the front-month expiry.

## Payoff & Breakevens

| Scenario | Outcome |
|---|---|
| Spot stays between the short strikes | Front shorts decay, back wings retain value → **max-profit zone** |
| Spot drifts toward one short strike | That side pressured, the other decays favourably → partial profit |
| Spot breaks past a long strike | Loss on that side, capped by the back-month wing → **defined risk** |

- **Max profit:** spot between the two short strikes at **front-month expiry**.
- **Max loss:** bounded by the back-month wings, but the exact figure depends on the time value remaining in the long legs at the front expiry (not a fixed number like a same-expiry condor).
- **Breakevens:** just outside each short strike, adjusted for the net debit and the residual value of the long wings.

## Greeks Profile

- **[[delta]]:** ≈ neutral at entry (balanced call and put sides); tilts as spot approaches either short strike.
- **[[gamma]]:** **net short** near the short strikes into front expiry — the range-holding risk.
- **[[vega]]:** **net long** — the back-month longs carry more vega than the front shorts, so a rising [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] helps overall (a key contrast with a short-vega iron condor). Term structure matters: you are short front-month, long back-month vol.
- **[[theta]]:** **net positive** while spot sits inside the tent — the front shorts decay faster than the back longs.

## Market View / When to Use

- You expect BTC/ETH to be **range-bound near-term** but want flexibility if it drifts.
- You want **[[theta]] income** from the front-month strangle **plus** back-month protection — a wider, safer alternative to a bare [[short-strangle]].
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] term structure** favours it: front-month IV rich relative to back-month (a downward-sloping term structure) improves the sell-front/own-back economics.
- You are comfortable managing a **four-leg, two-expiry** book on [[deribit]].

## Adjustments & Management

- **Roll the front shorts:** as they decay or the front expiry nears, roll to the next cycle for fresh credit — the recurring income engine (see [[trade-repair-and-rolling]]).
- **Recentre on drift:** if spot trends toward one short strike, roll that side's short out/away and/or shift strikes to re-centre the tent.
- **Keep the wings:** after front-month expiry the back-month longs survive with residual value — reuse them as the protective side of the next front-month strangle.
- **Manage front-leg gamma by ~21 DTE**, sharper in crypto given weekend gap risk.
- **Vega awareness:** because the book is net-long vega, a DVOL collapse hurts if you must unwind early; a DVOL spike helps the wings but can widen the short-leg marks.

## Crypto Specifics

- **Venue & settlement.** [[deribit]] BTC/ETH options are **European, cash-settled** to the index — **no early assignment** on the front shorts and no delivery on any leg, which materially simplifies a four-leg, two-expiry structure versus American equity options.
- **Fat tails make the wings non-negotiable.** Crypto can gap far past a short strike; the back-month long wings are what turn a naked short-strangle into a defined-risk trade — do not run this without them.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] term structure is the core edge.** The trade is explicitly short front-month vol and long back-month vol; a rich front / cheaper back structure is the ideal entry, and DVOL is the reference for both points.
- **Inverse vs linear.** **USDC-margined (linear)** contracts give clean USD P&L and a symmetric tent — preferred here. **Coin-margined (inverse)** contracts skew the payoff because collateral value moves with spot, distorting the "range-bound, delta-neutral" intent.
- **[[funding-rate|Perp-funding]] interaction.** Funding and 25-delta skew reveal which wing the leveraged crowd has overbid; tilt the short strikes to sell the richer wing. A residual delta can be hedged with the Deribit perp, paying/collecting funding on the hedge.
- **24/7.** Continuous trading gives more adjustment windows but also removes the overnight halt that would otherwise cap an adverse move against the front shorts.
- **No [[section-1256-contracts|§1256]].** No 60/40 treatment; the income is ordinary/short-term.
- **Alt-option liquidity limits.** Four legs across two expiries need real depth — practical only on BTC and ETH; alt options are too thin and their dated-expiry coverage too sparse.

## Risks

- **Range-break loss** if spot trends hard past a short strike — capped by the wings but still the primary loss mode.
- **Time-value uncertainty at front expiry:** max loss is not a clean fixed number because it depends on the back-month legs' remaining value.
- **Net-long-vega give-back:** a DVOL collapse hurts the back-month wings if you must exit early.
- **Execution & cost:** four simultaneous legs across two expiries in crypto's wider bid-ask raise entry/exit cost meaningfully — use combo/RFQ.
- **Management intensity:** rolling front legs, monitoring two expiries, and recentring on drift make this an active book.
- **Short-leg [[gamma-risk]]** into front expiry, worse without a session close.

## Worked Crypto Example

**Setup.** ETH at **$3,000** on [[deribit]] (USDC-margined). You expect ETH to hold roughly **$2,600-$3,400** near-term; front-month [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] (~60) sits rich to the back-month (~52).

1. **Sell 1 ETH $3,300 call** (front, 30 DTE) at **$120**.
2. **Buy 1 ETH $3,600 call** (back, 90 DTE) at **$110**.
3. **Sell 1 ETH $2,700 put** (front, 30 DTE) at **$115**.
4. **Buy 1 ETH $2,400 put** (back, 90 DTE) at **$105**.
5. **Net cost ≈ ($120 + $115) − ($110 + $105) = +$20 credit** per structure (near-neutral entry).
6. **Path — range holds:** ETH oscillates $2,800-$3,150 into front expiry; both front shorts expire worthless (keep ~$235 of decay), the back-month longs retain most of their value. **Roll a new front-month strangle** against the surviving wings for another cycle.
7. **Path — drift up:** ETH pushes to $3,350 near front expiry; roll the $3,300 short call up-and-out for credit and let the $3,600 back call cap the risk.
8. **Path — sharp break:** ETH gaps to $3,750; the front short call is ITM but the $3,600 back-month long wing caps the loss — the defined-risk feature doing its job.

## Getting the Data (CryptoDataAPI)

Strike/expiry selection and the [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] term structure come from [[deribit]] / [[greeks-live]]. [[cryptodataapi]] supplies the **volatility-regime, funding/skew, options-flow, and dealer-gamma** context for range assessment and short-leg timing.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime; sell the front strangle into *mean_reverting* / *normal*, avoid *vol_shock*
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (range/pinning context for strike placement)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — funding / skew read for wing tilt
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (long-gamma dealers dampen range; short-gamma amplify breakouts)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (breakout / vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/backtesting/klines` — deep OHLCV archive to study realized range vs the profit tent

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]] and volatility-regime detail on [[cryptodataapi]]. IV/DVOL surface and term structure are Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — sell the front strangle when `GET /api/v1/volatility/regime` reads `mean_reverting`/`normal` and `GET /api/v1/market-intelligence/options` max pain sits inside the intended range
- **Regime gate** — `GET /api/v1/quant/market`: leading `range_low_vol` probability is the range thesis; rising `squeeze`/`vol_spike` reads mean widen the strikes or stand down
- **Backtest** — realized range vs the profit tent from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); vol-state timing validated point-in-time against `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — `/api/v1/quant/gex` decides front-leg management: long dealer gamma favors letting the shorts decay, short gamma favors rolling early; treat a `/api/v1/market-intelligence/liquidations` cascade as the breakout early-warning for the wings.

## Related

- [[diagonal-spread]] — the single-side building block of the double diagonal
- [[calendar-spread]] — the same-strike two-expiry structure it generalises
- [[iron-condor]] — the same-expiry range trade; the double diagonal is its calendarised, net-long-vega cousin
- [[short-strangle]] — the front-month core the wings protect
- [[crypto-options-volatility-selling]] — the DVOL-premium engine this taps in a defined-risk form
- [[funding-rate]] — the perp linkage shaping skew and wing tilt
- [[trade-repair-and-rolling]] — the front-leg rolling framework
- [[deribit]] — venue; European cash settlement, DVOL and term-structure source
- [[section-1256-contracts]] — the tax treatment crypto options do **not** receive
