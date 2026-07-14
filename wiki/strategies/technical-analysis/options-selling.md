---
title: "Options Selling Strategies (Crypto)"
type: strategy
created: 2026-04-07
updated: 2026-07-14
status: good
tags: [options, crypto, income, premium-selling, volatility, derivatives, bitcoin, ethereum, theta]
aliases: ["Premium Selling", "Selling Premium", "Crypto Options Income", "Options Income Strategies"]
strategy_type: quantitative
timeframe: swing|position
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[crypto-options-volatility-selling]]", "[[covered-call]]", "[[cash-secured-put]]", "[[wheel-strategy]]", "[[iron-condor]]", "[[short-strangle]]", "[[options-income]]", "[[variance-risk-premium]]", "[[volatility-risk-premium]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[cryptodataapi]]"]
---

# Options Selling Strategies (Crypto)

## Overview

**Options selling** (premium selling / writing options) is the broad family of structures that profit from collecting option premium and benefiting from [[theta|time decay]], re-scoped here to crypto ([[bitcoin|BTC]]/[[ethereum|ETH]] on [[deribit]], plus on-chain vaults and BTC-ETF options). The core thesis is the [[variance-risk-premium|variance risk premium]]: option [[implied-volatility|IV]] — Deribit's [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] — systematically prices in *more* volatility than subsequently realizes, so disciplined sellers harvest the gap. In crypto that spread is structurally **fatter than equities'** (crypto DVOL routinely runs 2-4× the equity VRP) — richer premium, but underwriting a genuinely fatter tail.

This page is the **hub** for the crypto premium-selling family. The systematic, delta-hedged short-vol *book* on Deribit BTC/ETH is documented in depth on [[crypto-options-volatility-selling]]; the individual structures each have their own page (linked below).

## Construction

The family spans a risk spectrum:

**Covered (lower risk) — hold the coin:**
- **[[covered-call]]:** hold spot BTC/ETH, sell calls against it. Capped upside, premium cushions downside. The most common crypto income overlay.
- **[[cash-secured-put]]:** sell puts backed by USDC. Get paid to wait for a lower entry. The entry leg of the [[wheel-strategy]].

**Defined-risk spreads — no coin required:**
- **[[iron-condor]]:** sell an OTM call spread + OTM put spread. Profits if spot stays in a range; capped risk both sides — strongly preferred in crypto given the gap profile.
- **Credit spreads:** sell a nearer option, buy a further one — defined risk, lower capital.

**Naked (higher risk) — undefined tail:**
- **[[short-strangle]]:** sell an OTM call and OTM put unprotected. Highest premium, undefined risk — dangerous in crypto's fat tail; use only sized small and with hard kill switches.

## Payoff & breakevens

Every seller's payoff is the same shape: a **capped credit** if the underlying stays within the sold strikes, a **losing tail** beyond them.

| Structure | Max profit | Max loss |
|---|---|---|
| Covered call | (Strike − cost) + premium | Coin cost − premium (coin → 0) |
| Cash-secured put | Premium | Strike − premium (coin → 0) |
| Iron condor | Net credit | Wing width − net credit (defined) |
| Short strangle | Net credit | Undefined (both tails) |

Breakeven for a two-sided sell is the short strike ± total credit; for covered structures it is the coin cost minus premium (calls) or strike minus premium (puts).

## Greeks profile

The unifying signature of every short-premium structure:

| Greek | Sign | Meaning |
|---|---|---|
| [[theta]] | Positive | The income engine — sold options decay in the seller's favor, fastest 21-45 DTE |
| [[vega]] | Negative | A DVOL spike marks the shorts up (paper loss) even with spot flat |
| [[gamma]] | Negative | Losses accelerate as spot approaches a short strike near expiry — the crypto-gap hazard |
| [[delta]] | Structure-dependent | Long (covered call, short put), neutral (condor/strangle), or short depending on the build |

Positive theta / negative vega / negative gamma is the short-vol posture — the seller is paid for time and short volatility, exposed to the fast, deep move.

## Market view / when to use

- **Range-bound to mildly directional** views over weeks; you expect realized vol to come in **below** DVOL.
- **Elevated DVOL** (rich premium) but no expectation of a violent breakout — sell into fear, not into a live vol shock.
- You want a **non-directional carry** overlay that diversifies a directional/momentum crypto book and complements [[funding-rate|funding]] carry.

## Adjustments & management

- **Close winners early:** take profit at 50% of max credit rather than holding to expiry.
- **Cut / roll losers:** manage or roll when a position reaches ~1.5-2× the credit received, or when a short strike is tested.
- **Manage before the last week:** with 24/7 markets and no session close, close/roll ~7-14 DTE to sidestep the hottest [[gamma]] on a weekend gap.
- **Prefer defined risk:** use condors/spreads over naked strangles in crypto — the tail is real.
- **Hard vol-shock kill switch:** flatten short vega if DVOL spikes (e.g., +50% in a session) — the kill switch, not the entry signal, is the load-bearing risk control (see [[crypto-options-volatility-selling]]).
- **Size by vega, not count:** cap short vega per DVOL point of NAV; crypto DVOL can move 20-40 points in a session.

## Crypto specifics

- **Deribit is the market.** The vast majority of crypto options OI is on Deribit; premium selling is executed there (or via on-chain vaults / BTC-ETF options).
- **Cash settlement, no early assignment.** Deribit's European, cash-settled options mean no early [[assignment]] and no delivery — capped/assigned outcomes settle in cash, and you keep any spot/staked coin. A genuine simplification versus American equity options.
- **Inverse vs linear settlement.** Sell in **USDC (linear)** for clean USD P&L, or **coin-margined (inverse)** to keep collateral in coin (quanto-like non-linearity).
- **DVOL-rich premium, fatter tail.** The crypto VRP is wider than equities' — more room to absorb costs — but the crash frequency (2020-03, LUNA, FTX, 2025-10-10) keeps the tail-risk premium alive and the kill switches essential.
- **Perp-funding sets the skew.** Unlike equities' static put skew, crypto skew swings with [[funding-rate|funding]]: richly positive funding firms call skew, letting the seller lean into whichever wing the leveraged crowd overbid.
- **24/7 markets.** Continuous theta and continuous gap risk; weeklies are especially gamma-hot with no market close to cap a move.
- **No [[section-1256-contracts|§1256]].** Crypto (and crypto-ETF) options get no 60/40 shelter — premium is ordinary/short-term income, materially lowering the after-tax yield versus an SPX program.
- **Industrialized supply.** On-chain covered-call/put-selling vaults and BTC covered-call ETFs systematically write premium, compressing call-side VRP over time — the crypto analogue of equity vol-crowding.

## Risks

- **Fat-tail blow-up:** a single Black-Thursday-style gap (see [[black-swan]]) can erase months of premium — the defining risk; defined-risk structures cap it per position.
- **Negative skew:** smooth equity curve punctuated by cliffs — psychologically punishing.
- **Vol-of-vol / margin spiral:** a DVOL spike inflates portfolio margin exactly when liquidity vanishes, risking force-liquidation.
- **VRP compression:** vault/ETF supply thinning the premium.
- **Venue concentration:** Deribit outage/insolvency during a vol event is hard to hedge.

## Worked crypto example

**Setup (illustrative).** BTC spot $68,000, DVOL 55 (upper-half of range, rich), 30-day realized vol 40 → VRP ≈ 15 points. Sell a 35-DTE **iron condor** on BTC (USDC-margined):

- Short $76,000 call / long $80,000 call (call spread)
- Short $60,000 put / long $56,000 put (put spread)
- Net credit ≈ $1,100/BTC; max loss capped at ~$2,900 by the long wings.

- **BTC stays $60k-$76k (base case):** condor decays; close at 50% of credit for **+$550/BTC**.
- **BTC drifts to $58k (put spread tested):** manage/roll near the short put or take a partial loss into the defined wing.
- **BTC gaps to $52k (tail):** vol-shock kill fires at the open; the long $56,000 put caps the loss near **−$2,900/BTC** — the reason the structure is a *defined-risk condor*, not a naked strangle.

## Getting the Data (CryptoDataAPI)

DVOL and the IV surface come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the options-flow, vol-regime, dealer-gamma, funding, and liquidation context for gating entries and firing the kill switch.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew driver)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for VRP backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

## Related

- [[crypto-options-volatility-selling]] — the systematic, delta-hedged short-vol book (the deep treatment)
- [[covered-call]] — the beginner-friendly entry point
- [[cash-secured-put]] — conservative put selling with USDC collateral
- [[wheel-strategy]] — the full CSP + covered-call income cycle
- [[iron-condor]] — defined-risk two-sided premium selling
- [[short-strangle]] — undefined-risk premium selling
- [[options-income]] — the broader income-strategy class
- [[variance-risk-premium]] / [[volatility-risk-premium]] — the theoretical basis for selling premium
- [[funding-rate]] — the perp linkage shaping crypto skew
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[black-swan]] — the tail event the whole risk framework exists to survive
- [[deribit]] / [[greeks-live]] — venue and analytics

## Sources

- [[crypto-options-volatility-selling]] — the wiki's canonical treatment of the crypto variance risk premium and its kill-switch risk framework
- [[deribit]] / [[greeks-live]] documentation — DVOL, European cash settlement, coin-margined vs USDC-margined mechanics
