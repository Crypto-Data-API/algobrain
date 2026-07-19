---
title: "Ratio Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, ratio-spread, directional, volatility, crypto, derivatives, advanced]
aliases: ["Call Ratio Spread", "Put Ratio Spread", "Ratio Vertical"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[backspread]]", "[[butterfly-spread]]", "[[broken-wing-butterfly]]", "[[calendar-spread]]", "[[iron-condor]]", "[[implied-volatility]]", "[[delta]]", "[[gamma]]", "[[vega]]", "[[funding-rate]]", "[[deribit]]", "[[crypto-options-volatility-selling]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Ratio Spread

## Overview

A ratio spread buys N options at one strike and sells M options at a further strike, with **M > N** (usually 1:2 or 1:3). The canonical form is the **call ratio spread**: buy 1 near-the-money call, sell 2 further-OTM calls. The extra short options finance the long, so the trade is typically **zero-cost or a net credit**. It profits from a *moderate* directional drift to the short strike, but the naked extra short(s) leave **unbounded risk** if the move overshoots — a serious problem in crypto, where 24/7 gaps have no session close to cap them.

Ratio spreads are the **inverse of a [[backspread]]**: backspreads want explosive moves, ratio spreads want controlled ones. The surplus short options make the position **net short [[vega]]**, so it also profits from falling implied volatility — in crypto terms, a declining [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]]. That makes the ratio spread a directional cousin of [[crypto-options-volatility-selling|short-vol premium selling]], and it carries the same short-gamma tail exposure.

## Construction

**Call ratio spread (bullish), on BTC or ETH [[deribit]] options:**

| Leg | Action | Qty | Strike (delta) |
|---|---|---|---|
| Long | Buy call | 1 | ATM / slightly ITM (~50Δ) |
| Short | Sell call | 2 | OTM (~25-30Δ) |

- **Put ratio spread (bearish):** buy 1 ATM/ITM put, sell 2 OTM puts at a lower strike.
- **Ratio:** 1:2 standard; 1:3 raises the credit and the risk while narrowing the profit tent.
- **Net debit/credit:** size strikes for **zero cost or a small credit**. Any debit should be minimal.
- **Tenor:** 21-45 DTE — enough time for the drift, not so much that the short vega is dominated by a [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] regime shift.

## Payoff & Breakevens

- **Max profit** at the short strike at expiry: `(short strike − long strike) + net credit` (or `− net debit`).
- **Max loss:** **unbounded** above the upper breakeven (call ratio) or down to zero-underlying (put ratio); each extra short adds one unit of naked exposure.
- **Upper breakeven (call ratio):** `short strike + max-profit amount`.
- **Downside (call ratio, credit entry):** none — all legs expire worthless and you keep the credit.
- Profit tent peaks sharply at the short strike and collapses beyond it.

## Greeks Profile

- **[[delta]]:** directional toward the long strike near entry; flips against you once price pushes through the short strikes.
- **[[gamma]]:** **net short** beyond the short strikes — the source of the accelerating loss and the reason for a hard time/price stop.
- **[[vega]]:** **net short** — benefits from falling [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]]; a vol spike inflates the two shorts faster than the single long.
- **[[theta]]:** **net positive** in the profit tent — time decay works for you while price sits below the short strike.

## Market View / When to Use

- You expect a **moderate, capped move** to a target level — not a runaway trend.
- You expect **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] to fall** (short vega tailwind) — best entered when DVOL sits in a mid-to-high percentile of its trailing year.
- You read the [[funding-rate|perp funding]] / skew as **overbid on the wing you are selling** (e.g. richly positive funding firming call skew → sell the call side).
- You want a **financed directional bet** with no upfront cost, and you can actively manage the naked leg.

## Adjustments & Management

- **Profit target:** close at **50-75% of max profit**; do not hold hoping for a perfect pin at the short strike into crypto's continuous gamma.
- **Cap the naked leg (primary adjustment):** if price approaches the short strike with momentum, **buy the next further-OTM option** to convert into a [[broken-wing-butterfly]] / [[butterfly-spread]] — removing the unbounded risk while keeping accrued P&L.
- **Hard stop:** flatten if the underlying breaches the short strike with momentum, or if [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] spikes hard against the short vega.
- **Roll:** if the thesis holds but timing slipped, roll the whole structure out; prioritise rolling the **naked leg**, which carries the [[gamma-risk]].
- **The ~21-DTE rule:** manage the naked-leg gamma trap by 21 DTE. It is sharper in crypto because there is **no overnight close** — a weekend gap can jump straight through the short strike (Source: [[trade-repair-and-rolling]]).

## Crypto Specifics

- **Venue & settlement.** [[deribit]] BTC/ETH options are **European, cash-settled** — so the naked short leg carries **no early-assignment or physical-delivery risk** and no pin-assignment surprise; it settles to the Deribit index. That removes one equity-style hazard, but does nothing for the underlying gap risk.
- **Inverse vs linear.** On **coin-margined (inverse)** contracts the P&L and collateral are denominated in BTC/ETH, so a losing call ratio hurts *and* your collateral's USD value may be moving too. **USDC-margined (linear)** contracts give clean USD P&L. Prefer linear unless you specifically want the embedded coin delta.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] drives the short vega.** The ratio spread is net short vol; entering into elevated DVOL and a subsequent decline is a tailwind, while a DVOL shock is the core risk — the same variance-premium logic as [[crypto-options-volatility-selling]].
- **24/7 gap risk.** No session close means the naked leg can be blown through overnight or over a weekend with no ability to react — the unbounded side is genuinely more dangerous than in equities. Defined-risk conversion (adding a wing) is strongly preferred over running a truly naked ratio.
- **[[funding-rate|Perp-funding]] interaction.** Funding and 25-delta skew tell you which wing the leveraged crowd has overbid; sell the rich wing. A short-delta perp hedge on a call ratio can *collect* funding in a positive-funding regime.
- **No [[section-1256-contracts|§1256]].** No 60/40 treatment; crypto ratio-spread P&L is ordinary/short-term.
- **Alt-option liquidity limits.** BTC/ETH only for reliable multi-leg fills; alt options are too thin to leg a ratio without paying away the credit.

## Risks

- **Unbounded loss on the naked side** — the defining risk, amplified by crypto's fat tails and continuous trading.
- **Vol-spike whipsaw:** a [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] jump inflates the two short options faster than the long, marking the position sharply negative even before spot moves.
- **Short-gamma acceleration into expiry** — the [[gamma-risk]] trap, worse without an overnight close.
- **Margin expansion:** Deribit portfolio margin on the naked leg balloons in a vol shock, risking auto-liquidation at the worst tick.
- **Narrow optimal outcome:** full max profit only at one price; partial fills of the thesis are the norm.

## Worked Crypto Example

**Setup.** ETH at **$3,000** on [[deribit]] (USDC-margined), 35 DTE, [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] elevated (~60, 70th percentile) after a pullback. You expect a bounce toward **$3,300** but not through **$3,600**, and you expect DVOL to fall.

1. **Buy 1 ETH $3,000 call** at **$180**.
2. **Sell 2 ETH $3,300 calls** at **$90** each → **$180 credit**.
3. **Net cost = $0** (zero-cost entry).
4. **Max profit at $3,300 at expiry:** `$3,300 − $3,000 = $300` per 1-ETH structure.
5. **Upper breakeven:** `$3,300 + $300 = $3,600`. Above this, losses begin and are **unbounded**.
6. **Below $3,000:** all legs expire worthless → **P&L = $0** (no downside on the credit entry).
7. **Path — thesis works:** ETH rises to ~$3,280 over three weeks while DVOL falls to ~50 (short-vega tailwind). Close for ≈ **+$220** per structure and book it — do not carry the naked leg into the last 21 days.
8. **Path — overshoot risk:** if ETH rips through $3,600, add a long $3,900 call to cap the runaway short before the loss compounds.

## Getting the Data (CryptoDataAPI)

Strike/wing selection and [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] come from [[deribit]] / [[greeks-live]]. [[cryptodataapi]] supplies the **volatility-regime, funding/skew, dealer-gamma, and liquidation** context that gates entry and warns of the vol shock that threatens the naked leg.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal) for the short-vega timing
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — funding, the skew/wing-selection read
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]]
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for realized-vol / payoff backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]] and volatility-regime detail on [[cryptodataapi]]. IV/DVOL surface is Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can manage the ratio spread's context end-to-end (strikes and DVOL stay on Deribit / [[greeks-live]]):

- **Entry timing** — `GET /api/v1/volatility/regime` — the short-vega structure wants an `expanding`/`normal` read likely to mean-revert down; never open into `vol_shock`.
- **Wing selection** — `GET /api/v1/derivatives/funding-rates?coin=ETH` — sell the wing the leveraged crowd has overbid (richly positive funding → the call side).
- **Naked-leg watch** — `GET /api/v1/quant/gex` + `GET /api/v1/market-intelligence/liquidations` — short dealer gamma plus cascade activity is the overshoot scenario that blows through the short strike; use it to trigger the buy-the-further-wing conversion to a [[broken-wing-butterfly]].
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08) to measure how often BTC/ETH overshoot the short-strike distance within candidate tenors — the tail frequency the naked leg is underwriting.
- **Tips** — automate a spot-vs-short-strike distance alert and the ~21-DTE management rule as scheduled jobs, not discretionary checks.

## Related

- [[backspread]] — the mirror structure: buy more than you sell, for unbounded profit on big moves
- [[butterfly-spread]] / [[broken-wing-butterfly]] — a ratio spread with the risk capped by an extra long wing (the standard repair)
- [[crypto-options-volatility-selling]] — the short-vol premium book this shares its short-vega/short-gamma character with
- [[iron-condor]] — a fully defined-risk range trade
- [[trade-repair-and-rolling]] / [[gamma-risk]] — managing the naked leg and the 21-DTE trap
- [[funding-rate]] — the perp linkage that shapes crypto skew and wing selection
- [[deribit]] — venue; European cash settlement removes assignment risk
- [[section-1256-contracts]] — the tax treatment crypto options do **not** receive
