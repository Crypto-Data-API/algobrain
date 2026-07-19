---
title: "Long Put (Crypto)"
type: strategy
created: 2026-05-07
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, volatility, risk-management, bitcoin, ethereum]
aliases: ["Long Put", "Buy Put", "Protective Put", "Crypto Long Put"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[long-call]]", "[[protective-put]]", "[[collar]]", "[[synthetic-long]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[variance-risk-premium]]", "[[volatility-skew]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[cryptodataapi]]"]
---

# Long Put (Crypto)

## Overview

A long put is the canonical bearish [[options]] structure and the simplest coin-book downside hedge: the buyer pays a premium for the right to sell the underlying at a fixed strike on or before expiry. On [[deribit]] one BTC put controls **1 BTC** (1 ETH per ETH put), contracts are **European, cash-settled at 08:00 UTC** against the Deribit index, and premium/settlement are in the coin ([[deribit#Inverse settlement|inverse / coin-margined]]). The position has **bounded loss** (premium paid), **maximum profit as spot approaches zero**, and serves a dual role: a directional bet on a decline, and a convex hedge for a long-coin (or long-beta DeFi) book.

Held to expiry, a BTC put usually **loses** money in calm regimes — it pays the [[variance-risk-premium]] embedded in [[dvol|DVOL]]. Edge comes from (a) being right on a forecastable down-move catalyst, (b) using the put as a *hedge* whose value is realized in a correlated crypto sell-off, or (c) exploiting [[volatility-skew]] when the put wing is cheap relative to realized downside.

## Construction

1. **Buy 1 put** at the chosen strike/expiry on [[deribit]].
2. **Strike selection**:
   - **ATM** (Δ ≈ −0.50): balanced Greeks — short-dated bearish speculation.
   - **OTM** (Δ ≈ −0.15 to −0.30): cheap, high-convexity crash bet or portfolio "shoulder" hedge, typically 10-25% below spot.
   - **ITM** (Δ ≈ −0.65 to −0.80): capped-loss short-coin substitute.
3. **Tenor**: 7-30 DTE for speculation; 30-90 DTE rolled for continuous protection.
4. **Skew check**: crypto skew is **regime-dependent** — often *call* skew (upside calls bid) in bull euphoria, flipping to *put* skew in stress — so OTM puts are **not** always the expensive wing they are in equities. Buy puts when the downside wing is cheap by DVOL and skew standards.
5. **Settlement choice**: inverse (coin) by default on Deribit; use **linear (USDC)** where a clean USD hedge payoff is wanted.

## Payoff & breakevens

| Point | Value |
|---|---|
| **Max loss** | Premium paid (capped) |
| **Breakeven** | Strike − premium |
| **Max profit** | (Strike − premium) — realized as spot → 0 |

A long put is the downside hockey stick: flat loss (premium) above the strike, profit growing dollar-for-dollar as spot falls below it. Below breakeven it behaves like a leveraged short with a hard-capped loss.

## Greeks profile

| Greek | Sign | Behaviour as spot falls | Note |
|---|---|---|---|
| [[delta]] | Negative (−0.15 to −0.80 by strike) | Becomes more negative (toward −1.0) | Directional short that intensifies in a decline |
| [[gamma]] | Positive (largest ATM / near expiry) | Accelerates delta in your favour | The convexity that makes the put an effective tail hedge |
| [[vega]] | Positive | Rises with the DVOL spike that usually accompanies a crypto sell-off | A right thesis can pay on vega before spot even moves |
| [[theta]] | Negative | Bleeds daily, faster inside ~7-10 DTE | The carry cost — the variance premium paid to the seller |

A long put is **short delta, long gamma, long vega, short theta** — the structural opposite of a sold put (cash-secured put). Its defining feature for hedgers is **convexity**: as spot falls the hedge "grows teeth" (long gamma) exactly when needed, and the DVOL spike that typically accompanies a crypto crash adds a long-vega tailwind.

## Market view / when to use

- **Directional bearish** with a defined down-catalyst (macro risk-off, exchange/stablecoin stress, large unlock, leverage flush).
- **Portfolio hedge**: protect a long-coin or long-beta book against a drawdown while keeping the upside — the crypto analogue of index put protection.
- **Capped-risk alternative to a short perp**: a [[perpetual-futures|perp]] short gives linear downside but carries **liquidation risk** and pays funding when shorts are crowded; a long put caps loss at premium, can't be liquidated, and adds convexity + long vega — you trade funding/liquidation risk for theta.

## Adjustments & management

- **Take profit fast in a crash**: crypto sell-offs are violent and mean-revert; monetize a put into the DVOL spike rather than waiting for the crush that follows.
- **Roll the hedge on a schedule**: for continuous protection, roll monthly/quarterly regardless of the tape — discretionary "de-hedging" in calm markets is the classic failure.
- **Spread it off**: sell a lower put (put spread) to cut cost/theta once the easy down-move is in.
- **Collar it**: finance the put by selling an OTM call against long coin — a [[collar]], the workhorse crypto-treasury hedge.

## Crypto specifics

- **Deribit inverse (coin) settlement.** Premium and payoff are in coin, so a Deribit put's USD delta differs slightly from the naive number, and coin collateral itself carries long-delta that offsets the hedge. Use **linear (USDC)** contracts for a clean USD hedge. See [[deribit]] and [[black-scholes-model#Inverse vs linear settlement — the effect on price and Greeks]].
- **Skew flips.** Equity index puts carry a permanent, expensive crash-skew; crypto skew **oscillates** and can even favour calls in bull runs — a long put can be *cheaper* in crypto than intuition from equities suggests. Track skew via [[greeks-live]].
- **DVOL and the leverage effect.** Crypto DVOL spikes hard on down-moves (and sometimes up-moves), so the long put's vega leg is a strong tailwind in stress. [[dvol|DVOL]] is a Deribit / Greeks.live number, **not** on CryptoDataAPI.
- **24/7, no gap you can't trade.** No overnight/weekend close — but thin weekend liquidity makes crashes gappy and puts can reprice violently.
- **No §1256.** Crypto options get ordinary treatment, not the [[section-1256-contracts|§1256]] 60/40 shelter (jurisdiction-dependent).
- **Liquidity cliff beyond BTC/ETH.** Alt puts (SOL, XRP, etc.) have wide spreads and few strikes; a BTC/ETH put is often the practical hedge even for an alt-heavy book (accepting basis risk).

## Worked crypto example

**Setup (illustrative, hedge).** A desk holds **10 BTC** spot; BTC $60,000; wants a 30-day floor without selling.

- **Buy** 10 × $54,000 puts (10% OTM), 30 DTE, at ≈ **$1,500** each → **$15,000** total (≈ 0.7% of the $600k book/month).

| Outcome at expiry | Hedge P&L | Book P&L | Net |
|---|---|---|---|
| BTC to $48,000 | Puts pay (54−48)k × 10 = **+$60,000** | Spot −$120,000 | −$60,000 (drawdown halved) |
| BTC to $42,000 | Puts pay (54−42)k × 10 = **+$120,000** | Spot −$180,000 | −$60,000 (convex — protection deepens) |
| BTC flat/up | Puts expire → **−$15,000** | Book unaffected/up | −$15,000 (the premium, the cost of insurance) |

The put converts a thin, known monthly bleed into a large convex payoff exactly in the correlated sell-off where the book hurts most — without a short perp's liquidation risk.

## Getting the Data (CryptoDataAPI)

The Deribit chain, [[dvol|DVOL]], skew, and per-strike Greeks come from Deribit / [[greeks-live]]. [[cryptodataapi|CryptoDataAPI]] supplies positioning, vol-regime, and perp-carry context:

- **Options OI / max pain — positioning and expiry pins** — `GET /api/v1/market-intelligence/options`. See [[cryptodataapi-market-intelligence]].
- **Volatility regime — is the downside wing cheap?** — `GET /api/v1/volatility/regime` and `GET /api/v1/volatility/regime/score`. See [[cryptodataapi-regimes]].
- **Funding — the short-perp alternative carry** — `GET /api/v1/derivatives/funding-rates?coin=BTC`. See [[cryptodataapi-derivatives]].

The IV surface, skew, and **DVOL** are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Entry timing** — `GET /api/v1/volatility/regime/score` low + `GET /api/v1/volatility/regime` `compressed`: protection is cheapest before the stress bid arrives; a put bought during `vol_shock` pays peak premium for a move already priced.
- **Skew driver** — `GET /api/v1/derivatives/funding-rates?coin=BTC`: richly positive funding marks the call-skew regime where downside puts are relatively cheap — the best hedging windows.
- **Regime gate** — `GET /api/v1/quant/market`: rising `strong_trend_bear`/`vol_spike` probabilities argue for rolling protection up on schedule and monetising fast into spikes rather than holding through the V-recovery.
- **Expiry context** — `GET /api/v1/market-intelligence/options`: max-pain and OI concentration before making expiry-week hold/roll decisions.
- **Backtest** — hedge-payoff studies on `GET /api/v1/backtesting/klines` (Binance 1h/4h/1d since 2017-08 covers 2020-03, LUNA, and FTX); pair with `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time trigger states. Put premiums come from Deribit — CDA has no options archive.
- **Tips** — for continuous protection, have the agent roll monthly regardless of the tape; discretionary de-hedging in calm markets is the classic failure this page warns against.

## Related

- [[long-call]] — the bullish counterpart
- [[protective-put]] — long put paired with long coin (this page's hedge use, formalized)
- [[collar]] — put financed by a short call over long coin; the standard crypto-treasury hedge
- [[synthetic-long]] — the delta-one combo whose short-put leg is the opposite of a long put
- [[perpetual-futures]] / [[funding-rate]] — the short-perp alternative and its carry/liquidation trade-off
- [[deribit]] / [[greeks-live]] — venue, inverse settlement, skew, analytics
- [[dvol]] / [[volatility-skew]] — the vol and skew you pay
- [[implied-volatility]] / [[realized-volatility]] / [[variance-risk-premium]] — the headwind a held put faces
- [[delta]] / [[gamma]] / [[theta]] / [[vega]] — the position's Greek profile
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, coin- vs USDC-margined contracts, DVOL and skew
- Natenberg, S., *Option Volatility and Pricing* — put pricing, skew, term structure
- Taleb, N. N., *Dynamic Hedging* — the convexity case for systematic tail-hedging
