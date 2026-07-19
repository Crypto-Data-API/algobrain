---
title: "Jade Lizard"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, volatility, bitcoin, ethereum]
aliases: ["Jade Lizard Spread", "Crypto Jade Lizard"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[iron-condor]]", "[[short-strangle]]", "[[broken-wing-butterfly]]", "[[christmas-tree-spread]]", "[[risk-reversal]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[max-pain]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
---

# Jade Lizard

## Overview

The jade lizard is a **three-leg premium-selling** structure that combines a **short put** with a **short call spread** (short OTM call + long further-OTM call). When the total premium collected exceeds the width of the call spread, the structure has **no risk to the upside** — a rally past the call spread nets to zero-or-positive. The only risk is to the downside, like a short put below the breakeven. It is a **neutral-to-slightly-bullish** [[crypto-options-volatility-selling|short-vol]] trade that collects premium from both sides while capping (in fact eliminating) upside risk.

On [[deribit]] BTC/ETH, the jade lizard fits a market where you are willing to be long on a dip (short put) and think a large rally is unlikely (short call spread), and where you want to **lean into crypto's funding-driven call skew** — selling the overbid call wing while the perp crowd is long. Versus a [[short-strangle]], it removes the unbounded upside; versus an [[iron-condor]], it collects more premium by leaving the downside as a defined-but-larger short-put risk.

## Construction

Three legs, one expiry, cash-settled:

| Leg | Action | Strike | Purpose |
|---|---|---|---|
| 1 | Sell 1 put | OTM below spot (~25-30Δ) | the primary risk leg |
| 2 | Sell 1 call | OTM above spot (~15-25Δ) | short side of call spread |
| 3 | Buy 1 call | further OTM above | caps the upside |

- **The critical rule:** **total credit ≥ call-spread width** → **no upside risk**. If the call spread is $200 wide, the combined credit from all three legs must exceed $200.
- **Ratios:** 1 short put : 1 short call : 1 long call (net short two, long one).
- **Net credit:** the sum of all three premiums (short put + short call − long call).
- **Tenor:** 21-45 DTE for the theta profile.

## Payoff & breakevens

- **Max profit** = total credit, when spot finishes between the short put and short call strikes.
- **Upside** (above the long call): call spread realizes its max loss (its width), but total credit ≥ width → **net zero or small profit; no loss**.
- **Downside** (below the short put): behaves like a short put — loss grows point-for-point.
- **Downside breakeven** = short put strike − total credit.
- **Max loss** = short put strike − total credit (approached only on a collapse toward zero; in practice bounded by how far crypto gaps).

The payoff is a wide profit shelf between the shorts, a flat no-loss (or tiny-profit) shelf on the upside, and a downward-sloping short-put loss on the downside.

## Greeks profile

- **Delta:** **slightly positive** (long-biased) at entry — the short put dominates the directional exposure; you profit from stable-to-rising spot.
- **Gamma:** **negative** — short two options net; the position dislikes large moves, worst near the short put in a selloff and near expiry.
- **Theta:** **positive** — three short legs (net) make time decay the primary profit engine.
- **Vega:** **negative** — a DVOL spike marks the shorts to a loss; elevated DVOL at entry means a richer credit.

## Market view / when to use

- **Neutral-to-slightly-bullish:** you are comfortable being assigned/long BTC or ETH on a dip (the short put) and think a large rally is unlikely.
- **Elevated DVOL** (roughly 40th-90th percentile) so the credit comfortably exceeds the call-spread width — the condition for no upside risk.
- **Rich call skew / positive funding:** the perp crowd is long, call vol is bid — sell the overbid call wing into that.
- You want more premium than an [[iron-condor]] and will accept the larger, undefined-ish downside of a short put in exchange for zero upside risk.

## Adjustments & management

- **Profit target:** close the whole structure at **50% of max profit** (buy it all back for half the original credit).
- **Downside management:** if the short put is breached, manage as any tested short put — **roll down and out for a credit**, or close for a loss. This is the leg that hurts.
- **Upside:** if spot rallies through the call spread, there is nothing to fix — the credit ≥ width means no net loss; let it expire or close for near-max.
- **Time stop:** close with **7-10 DTE** remaining to avoid crypto's continuous expiry-week gamma on the short put.
- **Vol-shock kill:** flatten if DVOL rises **> 50% in a session** — the short put's downside is the crypto tail this structure is most exposed to.

## Crypto specifics

- **The short put is the crypto tail.** BTC/ETH can gap −20% over a weekend; the short put carries that downside with no lower wing. Size it like a **cash-secured put you would be happy to be assigned** — the whole trade rests on being willing to own the coin lower. This is the single most important risk here.
- **Inverse vs linear/USDC settlement:** strongly prefer **USDC-margined (linear)**. On **inverse (coin-margined)** options the short put's loss compounds with a falling collateral value — a quanto-like double hit exactly when a selloff tests the put. Mismatching collateral to the intended exposure is a silent killer.
- **Funding-driven skew is the edge angle:** in a positive-[[funding-rate|funding]] bull regime the perp crowd is long and **call skew is rich** — the jade lizard sells that overbid call wing while the short put leans with the bullish tape. Read the 25-delta [[risk-reversal]] before placing the call spread.
- **DVOL regime gate:** sell only inside the ~40th-90th DVOL percentile band, and require **total credit ≥ call-spread width** so the no-upside-risk condition actually holds (thin DVOL makes that hard).
- **24/7 & weekend gaps:** the short put can be tested at 03:00 UTC with no close to cap the move; the 7-10 DTE time stop and DVOL kill are the defenses. Expiry **08:00 UTC**, cash-settled to the Deribit index — **no physical assignment**; a breached put settles to cash, removing the equity-style overnight assignment scramble.
- **No [[section-1256-contracts|§1256]]:** the credit is taxed as ordinary capital gains on offshore Deribit — no 60/40 US shelter; AU treatment is trader-status-dependent.
- **Venue & liquidity:** [[deribit]] BTC/ETH only; **alt-option chains are too thin** for the three-leg structure.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **52** (elevated); funding +0.03%/8h (positive → call skew firm); you are neutral-to-bullish and happy to be long ETH near $2,900. 35 DTE.

**Trade (per 1-ETH contract):**
- Sell 1 $2,900 put (~28Δ) for **$130**.
- Sell 1 $3,200 call (~20Δ) for **$70**.
- Buy 1 $3,350 call for **$40** (caps upside).
- **Total credit = $130 + $70 − $40 = $160.** Call-spread width = $150.
- **Credit $160 > width $150 → no upside risk** (net **+$10** even if ETH rips above $3,350).
- **Max profit = $160**, with ETH between $2,900 and $3,200 at expiry.
- **Downside breakeven = $2,900 − $160 = $2,740.**

Payoff at expiration:

| ETH at expiry | P&L (per contract) | Note |
|---|---|---|
| ≥ $3,350 | +$10 | no upside loss (credit > spread width) |
| $3,200 - $3,350 | +$10 to +$160 | call spread partially in the money |
| $2,900 - $3,200 | +$160 | max profit shelf |
| $2,740 | $0 | downside breakeven |
| $2,600 | −$140 | short-put loss region |
| → $0 | −$2,740 | short-put tail (bounded by how far ETH gaps) |

**Path A — range/grind.** ETH oscillates $2,900-$3,150 and DVOL eases to 46; close at 50% for **+$80/contract**.

**Path B — rally.** ETH rips to $3,500; the call spread hits its $150 max loss but the $160 credit covers it → **+$10/contract**. You were right on direction and lost nothing on the capped upside.

**Path C — selloff (the tail).** ETH gaps −12% to $2,640 over a weekend, below the $2,740 breakeven. The short put marks a loss (~**−$100/contract** at $2,640, worse if it keeps falling). Manage as a tested short put: roll down-and-out for a credit if the thesis holds, or take the loss. This is the leg the whole risk framework watches.

## Sources

- [[greeks-live]] / [[deribit]] documentation — IV surface, 25-delta skew/[[risk-reversal]], USDC-margined vs inverse settlement, 08:00 UTC cash settlement (no physical assignment on a breached put).
- [[book-option-volatility-and-pricing]] — Natenberg on combined short-put / short-call-spread structures (mechanics port to crypto).
- tastytrade jade-lizard construction and management (the "no upside risk" credit ≥ width rule, 50%-profit management) — mechanics port directly; downside sizing must respect the crypto tail.

## Getting the Data (CryptoDataAPI)

The IV surface and 25-delta skew used to place the call spread and confirm the no-upside-risk credit come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the funding, flow, dealer-gamma, liquidation, and volatility-regime context.

**Live:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the crypto skew driver; positive funding = rich call wing to sell
- `GET /api/v1/volatility/regime` — per-asset vol regime; the entry gate (sell only when elevated, not vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (context for the short strikes)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the downside shock that tests the short put

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation and downside sizing
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. The IV surface and DVOL itself come from Deribit / [[greeks-live]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — sell when `GET /api/v1/volatility/regime` is elevated and `GET /api/v1/derivatives/funding-rates?coin=BTC` is positive: a rich call wing is what makes the credit ≥ call-spread-width (no-upside-risk) condition achievable
- **Regime gate** — `GET /api/v1/quant/market`: the lizard's open risk is the downside — rising `strong_trend_bear`/`vol_spike` probability vetoes entry regardless of how rich the premium looks
- **Backtest** — short-put breach frequency and drawdown from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); tag flush days with `/api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30) to study the naked-put tail separately
- **Tips** — verify the credit ≥ call-spread-width invariant at *fill*, not at quote — legging risk quietly reintroduces upside risk; while short, a `/api/v1/market-intelligence/liquidations` long-liquidation cascade is what tests the naked put, so treat it as the exit bell.

## Related

- [[iron-condor]] — defined risk both sides, less premium; the jade lizard trades that for no upside risk + a larger short-put downside
- [[short-strangle]] — the jade lizard caps the strangle's unbounded upside
- [[broken-wing-butterfly]] — another "no-loss on one side" premium structure
- [[christmas-tree-spread]] — a directional multi-leg cousin (with a naked leg instead of a capped one)
- [[risk-reversal]] — the 25-delta skew tool for placing the call spread
- [[crypto-options-volatility-selling]] — the short-vol context
- [[deribit]], [[greeks-live]] — venue and analytics; surface and skew source
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[gamma-exposure]], [[max-pain]] — skew, positioning, and level context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
