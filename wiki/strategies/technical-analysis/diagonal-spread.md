---
title: "Diagonal Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, diagonal-spread, directional, theta, income, crypto, derivatives]
aliases: ["Poor Man's Covered Call", "PMCC", "Diagonal Calendar", "Crypto PMCC"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[calendar-spread]]", "[[covered-call]]", "[[double-diagonal]]", "[[butterfly-spread]]", "[[implied-volatility]]", "[[theta]]", "[[delta]]", "[[funding-rate]]", "[[deribit]]", "[[crypto-options-volatility-selling]]", "[[trade-repair-and-rolling]]", "[[gamma-risk]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
---

# Diagonal Spread

## Overview

A diagonal spread buys a **longer-dated** option at one strike and sells a **shorter-dated** option at a **different** strike — a hybrid of a [[calendar-spread]] (different expiries) and a vertical (different strikes). The best-known variant is the **"Poor Man's Covered Call" (PMCC)**: buy a deep-ITM, longer-dated [[call-option]] as a stock substitute and sell a near-term OTM call against it, replicating a [[covered-call]] at a fraction of the capital. The long leg supplies directional exposure; the short leg harvests [[theta]] income cycle after cycle.

In crypto this is a **capital-efficient way to be long BTC/ETH with a yield overlay** on [[deribit]]. A deep-ITM 6-month BTC call costs a fraction of buying spot BTC, freeing collateral, while the rolled short calls monetise the persistent crypto variance premium (the same premium harvested by [[crypto-options-volatility-selling]]). The main crypto constraint is **tenor**: Deribit's longest listed options run to roughly a year, shorter than US equity LEAPS, so the "long-dated" leg is measured in months, not years.

## Construction

**PMCC (bullish call diagonal), on BTC or ETH [[deribit]] options:**

| Leg | Action | Strike (delta) | Tenor |
|---|---|---|---|
| Long | Buy call | Deep ITM (~0.70-0.85Δ) | 3-12 months |
| Short | Sell call | OTM (~0.20-0.35Δ) | 21-45 DTE |

- **Bearish variant:** buy a deep-ITM longer-dated put, sell a near-term OTM put ("poor man's covered put").
- **Net debit** = long premium − short credit. Keep the debit **below the strike width** so max profit is positive.
- **Minimise the long's extrinsic value:** deeper ITM = mostly intrinsic = less time decay working against you.
- **Expiry gap:** the long should carry **≥ 3-4×** the short's DTE.

## Payoff & Breakevens

- **Max profit:** the underlying at the short-call strike at the *short* expiry — the short expires worthless while the long retains maximum intrinsic + remaining extrinsic value.
- **Max loss:** the **net debit paid**, if the underlying falls hard and the long call decays.
- **Breakeven:** ≈ `long strike + net debit` (adjusted for the long's residual extrinsic value).
- **Recurring income:** each rolled short call adds credit, lowering the effective cost basis over time.

## Greeks Profile

- **[[delta]]:** **net long** and positive — the deep-ITM long dominates; the position behaves like a discounted long-spot substitute.
- **[[gamma]]:** modest; concentrated in the **short leg** near its expiry (the long's gamma is low and stable).
- **[[vega]]:** **net long** — the longer-dated leg has more vega than the short, so the position benefits on balance from rising [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] (opposite sign to a pure short-vol trade).
- **[[theta]]:** the short leg decays faster than the long, producing the **net income** the trade is built to collect while price sits below the short strike.

## Market View / When to Use

- **Bullish-to-neutral** on BTC/ETH over months, wanting exposure with a **yield overlay** and far less capital than spot.
- You expect price to **grind up or sideways** — ideal for repeatedly selling and rolling the short call.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] elevated** so the short calls carry fat premium, but you still want net-long vega/delta rather than a pure short-vol book.
- You want a **defined, capital-light** alternative to holding spot BTC or running a fully-collateralised [[covered-call]].

## Adjustments & Management

The diagonal is inherently a **rolling** strategy — the short leg is the income engine (see [[trade-repair-and-rolling]]).

- **Roll the short call:** at ~75% profit or each cycle, sell a new 21-45 DTE short call; the repeated credits lower cost basis.
- **Short call threatened (rally):** roll **up and out** for a net credit, or close the diagonal and bank the gain — never pay significant debit chasing a rallying market.
- **Thesis broken (drop):** close both legs; the loss is capped at the debit.
- **The ~21-DTE rule:** roll/close the short leg by ~21 DTE to avoid the [[gamma-risk]] zone — sharper in crypto, where a weekend gap through the short strike cannot be reacted to intraday.
- **Take profit on the whole spread** if a strong rally puts both legs deep ITM.

## Crypto Specifics

- **Venue & settlement.** [[deribit]] BTC/ETH options are **European, cash-settled** — the short call **cannot be assigned early**, removing the "called-away" hazard that complicates equity PMCCs. Both legs mark to the Deribit index; a rally simply nets the combined value at each expiry.
- **Tenor ceiling.** Deribit lists tenors from daily/weekly out to roughly **a year** (quarterly "LEAPS-style" expiries), with fewer far-dated strikes than US equity LEAPS. The long leg is a *months*-long substitute, not a multi-year one — plan rolls of the long accordingly.
- **Inverse vs linear.** On **coin-margined (inverse)** contracts both legs and P&L are BTC/ETH-denominated — the classic "covered call on your coins" that also carries collateral price risk. **USDC-margined (linear)** contracts give clean USD P&L and a cleaner directional read. Choose to match whether you *want* the embedded coin exposure.
- **[[funding-rate|Perp-funding]] alternative & interaction.** The long-delta leg can alternatively be expressed with a **Deribit perp/future**, turning the PMCC into a **funding-aware covered call**: in a positive-funding regime the perp long pays funding (a drag), so the option-based long leg may be cheaper carry; compare the two each cycle.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] term structure matters.** The trade is long the back-month, short the front-month vega; a steep DVOL term structure (front rich vs back) improves the roll economics.
- **24/7.** Continuous trading means rolls can be timed to any hour, but also that the short strike can be breached overnight — favour rolling early.
- **No [[section-1256-contracts|§1256]].** No 60/40 treatment; the rolled-credit income is ordinary/short-term.
- **Alt-option liquidity limits.** BTC/ETH have the depth and dated-expiry coverage for a diagonal; alt options rarely list usable long-dated strikes.

## Risks

- **Downside is the full debit:** a crypto crash can gut even a deep-ITM long call — the position is still meaningfully long delta.
- **Long-leg extrinsic decay:** the long call carries some time value that bleeds, especially over multi-month holds and if [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] falls (a net-long-vega drag).
- **Rally through the short strike** caps the upside; poorly managed rolls can lock in a debit chasing price.
- **Active management required:** every 21-45 day cycle needs a roll — not a set-and-forget trade.
- **Short-leg [[gamma-risk]]** into expiry, worse without an overnight close.

## Worked Crypto Example

**Setup.** BTC at **$60,000** on [[deribit]] (USDC-margined). Bullish over ~6 months; want exposure with income and low capital.

1. **Buy 1 BTC $50,000 call** (~0.80Δ, 180 DTE) at **$12,000**.
2. **Sell 1 BTC $66,000 call** (~0.25Δ, 35 DTE) at **$1,300**.
3. **Net debit = $12,000 − $1,300 = $10,700** per structure — versus **$60,000** to hold 1 BTC spot.
4. BTC drifts to **$63,000** in 30 days; the short $66k call decays to ~$400. **Buy it back** for $400 (locking ~$900 on the short leg).
5. **Sell a new $68,000 call** (35 DTE) for **$1,200**. Effective cost basis now `$10,700 − $900 − $1,200 = $8,600`.
6. After several cycles collecting ~$1,000-1,300 each, the basis keeps dropping and further appreciation in the long call is largely profit.
7. **Capital efficiency:** ~$10,700 controls ~$60,000 of directional BTC exposure with a recurring income overlay.

## Getting the Data (CryptoDataAPI)

Strike/expiry selection, the [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] level and its term structure come from [[deribit]] / [[greeks-live]]. [[cryptodataapi]] supplies the **volatility-regime, funding, and options-flow** context for timing the short-call rolls and comparing perp-vs-option carry.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime; sell short calls into *expanding* / elevated regimes
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, for the perp-vs-option long-leg carry comparison
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (strike-pinning context for the short call)
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (pinning vs cascade context near the short strike)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/btc-price-history?days=180` — BTC price + 200D MA for the multi-month directional backdrop
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for roll/backtest studies

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]] and volatility-regime detail on [[cryptodataapi]]. IV/DVOL surface is Deribit / [[greeks-live]].

## Related

- [[calendar-spread]] — the same-strike time spread; a diagonal is a calendar with a strike offset
- [[covered-call]] — the fully-collateralised strategy the PMCC replicates capital-efficiently
- [[double-diagonal]] — two diagonals (call + put) for range-bound coverage
- [[crypto-options-volatility-selling]] — the variance-premium engine the rolled short calls tap
- [[funding-rate]] — the perp carry to compare against the long-leg option
- [[trade-repair-and-rolling]] / [[gamma-risk]] — the rolling framework and the 21-DTE short-leg trap
- [[deribit]] — venue; European cash settlement removes early-assignment risk
- [[section-1256-contracts]] — the tax treatment crypto options do **not** receive

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg on the delta/theta/vega interplay across expiries that makes diagonals work; mechanics port to crypto, re-scoped to Deribit's European cash-settled BTC/ETH options and shorter tenor ceiling.
