---
title: "Gut Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, guts, gut-spread, ITM, volatility, straddle-variant, advanced]
aliases: ["Long Guts", "Short Guts", "Guts", "Gut Strangle"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[straddle-strangle]]", "[[strangle]]", "[[straddle]]", "[[strip-strap]]", "[[reverse-iron-condor]]", "[[short-straddle]]", "[[implied-volatility]]", "[[gamma-scalping]]", "[[deribit]]", "[[greeks-live]]", "[[cryptodataapi]]"]
---

# Gut Spread

## Overview

A **gut spread** (or "guts") is a straddle-family structure built from **in-the-money** options instead of ATM or OTM ones. **Long guts** buys an ITM call and an ITM put; **short guts** sells both. Its expiry payoff is **functionally equivalent to a [[strangle]]** with the same strikes — the long version is a long-vol bet, the short version a short-vol bet — but because both legs carry large intrinsic value, the premium, capital use, and quoting mechanics differ. In crypto ([[deribit]] BTC/ETH) the guts is mostly a completeness/relative-value structure: you would only choose it over the equivalent strangle when the ITM strikes happen to be priced more favourably than the OTM wings.

## Construction

Note the strike ordering is the **reverse** of a strangle — the call strike sits *below* spot and the put strike *above* it:

- **Long guts** — buy 1 **ITM call** (strike `A < S`) + buy 1 **ITM put** (strike `B > S`), with `A < B`. Debit is large: each leg has intrinsic ≈ its distance from spot plus extrinsic.
- **Short guts** — sell both of the same legs; collect a large credit, of which most is the guaranteed intrinsic.

By put-call parity the long guts (ITM call `A` + ITM put `B`) has the **same expiry payoff as a long strangle** (OTM put `A` + OTM call `B`). Deribit contracts are 1 BTC / 1 ETH, **European-exercise and cash-settled to the index** — a fact that changes the short-guts calculus versus US equities (see *Crypto specifics*). Typical tenor 21–45 DTE.

## Payoff & breakevens

Let `W = B − A` (strike width) and `P` = net premium. **Between the strikes both legs are ITM**, so total intrinsic is a constant `W`; the position's only variable cost is the extrinsic paid.

**Long guts:**
- Between `A` and `B`: payoff = `W − P` → **max loss = `P − W` = the net extrinsic paid** (a flat-bottom trough), incurred anywhere in the band.
- Upper breakeven = `A + P`; lower breakeven = `B − P`
- Above `B` or below `A`: profit grows without bound — identical to the equivalent strangle.

**Short guts:**
- Between `A` and `B`: **max profit = net extrinsic collected** (`P − W`).
- Outside the breakevens: **loss grows without bound** — the classic short-vol tail.

Because the ITM legs' intrinsic passes straight through, the *risk that matters* is only the extrinsic slice — which is why the guts and the same-strike strangle share identical breakevens and identical max loss.

## Greeks profile

Since the guts is payoff-equivalent to a strangle, its Greeks match the strangle's — **lower gamma and lower vega than an ATM straddle** (ITM legs sit further from the vega/gamma peak):

| Greek | Long guts | Short guts | Comment |
|---|---|---|---|
| [[delta]] | ≈ 0 near mid-strike | ≈ 0 near mid-strike | ITM call (~+0.65) offsets ITM put (~−0.65) |
| Gamma | Positive, moderate | Negative, moderate | Lower than an ATM straddle |
| [[vega]] | Positive, moderate | Negative, moderate | ITM legs carry less vega than ATM |
| [[theta]] | Negative | Positive | Only the extrinsic decays; intrinsic is inert |

## Market view / when to use

- **Long guts** — a long-vol view (expect a big BTC/ETH move) where the **ITM strikes are quoted better** than the equivalent OTM strangle wings, or where you specifically want to hold intrinsic value. In crypto this is rare; the strangle is usually the cleaner expression.
- **Short guts** — a short-vol, range-bound view. Collects a large gross credit, but only the extrinsic is genuine profit; the intrinsic must be paid back. Because Deribit is **European cash-settled**, short guts carries **no early-assignment risk** (unlike US equity guts), but it retains full undefined-tail risk and is best capped into a defined-risk structure.

## Adjustments & management

- **Long guts** — take profit as the move develops; because most premium is intrinsic, mark-to-market tracks spot closely, so manage it like the equivalent strangle. Delta-hedge on the Deribit perp to [[gamma-scalping|gamma-scalp]] the residual.
- **Short guts** — define the tail by buying further-OTM wings (turning it into a [[reverse-iron-condor|condor-like]] risk-defined structure) or delta-hedge continuously; honour a DVOL-spike kill switch. Take profit at ~50% of the *extrinsic* credit, not the gross.
- **Prefer the strangle** whenever its wings are as cheap — same payoff, less capital tied up in intrinsic and tighter Deribit spreads near ATM/OTM.

## Crypto specifics

- **Venue & underlyings**: [[deribit]] BTC/ETH; [[greeks-live]] for the surface and per-leg Greeks. Deep-ITM strikes on Deribit are usually **less liquid** (wider bid-ask) than ATM/OTM — the *opposite* of the occasional equities rationale for guts, and a reason the plain strangle is normally preferred.
- **European, cash-settled → no early assignment**: all Deribit options are European-exercise and cash-settle to the index. Short guts therefore has **no early-assignment risk**, the biggest practical hazard of US-equity short guts — but this is true of *every* Deribit short-vol structure, so it confers no edge unique to the guts.
- **Inverse vs linear settlement**: on classic inverse (coin-margined) contracts the large intrinsic value is denominated in the coin, so the guts' P&L inherits a coin delta; **USDC-margined (linear)** contracts keep it clean. Inverse settlement also ties up more coin collateral because of the fat intrinsic component.
- **DVOL**: buy guts when [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] is low, sell when it is rich — same gate as any vol structure. **DVOL/IV come from Deribit / [[greeks-live]], not CryptoDataAPI.**
- **24/7 & weekend gaps**: continuous trading; long guts benefits from unbounded weekend gaps, short guts is exposed to them.
- **No §1256**: offshore Deribit contracts get no [[section-1256-contracts|§1256]] 60/40 treatment.
- **Perp-funding interaction**: [[funding-rate|funding]] shapes the skew; it prices the delta-hedge on the perp.
- **Alt-option liquidity**: BTC/ETH only in practice — ITM alt strikes are effectively untradeable.

## Risks

- **Large capital tied up in intrinsic** — a long guts costs far more upfront than the equivalent strangle for the same payoff; the extra is just intrinsic you get back, but it is dead collateral meanwhile.
- **Wider Deribit bid-ask on deep-ITM strikes** — the main practical drag versus a strangle.
- **Short guts undefined tail** — full exposure to crypto gap moves (2020-03-12, LUNA, FTX, 2025-10-10); no early-assignment risk, but a DVOL spike still forces margin expansion and possible auto-liquidation.
- **Coin-margin non-linearity** on inverse contracts amplified by the intrinsic component.
- **Analytical complexity** — the large intrinsic obscures the small extrinsic slice that actually carries the P&L.

## Worked crypto example

**Setup (BTC, 30 DTE).** BTC spot **$60,000**, DVOL **50**. Long-vol view.

**Trade — long guts (USDC-margined):**
- Buy 1 BTC **55,000 call** (ITM): intrinsic $5,000 + extrinsic ≈ $1,500 = **$6,500**
- Buy 1 BTC **65,000 put** (ITM): intrinsic $5,000 + extrinsic ≈ $1,500 = **$6,500**
- Debit `P` = **$13,000**; strike width `W` = $10,000 → **net extrinsic (max loss) = $3,000**.
- Breakevens: upper = 55,000 + 13,000 = **$68,000**; lower = 65,000 − 13,000 = **$52,000**.

**Equivalence check.** A long strangle buying the **55,000 put + 65,000 call** for ≈ **$3,000** of extrinsic has the *same* breakevens ($52,000 / $68,000) and the *same* $3,000 max loss — for one-quarter of the upfront capital. That is why, absent a pricing quirk in the ITM strikes, the strangle wins on capital efficiency.

**Path A — big move.** BTC to **$72,000**: the 55,000 call is worth $17,000, the 65,000 put ≈ $0 → value $17,000, profit ≈ **+$4,000**. (Identical to the equivalent strangle's outcome.)

**Path B — range-bound (max loss).** BTC finishes at **$59,000** (inside the band): value = `W` = $10,000, loss = $13,000 − $10,000 = **−$3,000** (the extrinsic) — no worse than the equivalent strangle, but you parked $13,000 to risk $3,000.

## Getting the Data (CryptoDataAPI)

Implied vol / **DVOL** (the cheap-vs-rich gate for a guts) is a **Deribit / [[greeks-live]]** product and is *not* served by CryptoDataAPI. [[cryptodataapi]] supplies the surrounding regime, OI/max-pain, dealer-gamma, and funding context.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed = buy vol; vol_shock = sell)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] strike
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory / cascade risk)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (RV vs DVOL)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — direction of the guts follows `GET /api/v1/volatility/regime`: `compressed` favors buying the ITM pair, elevated/`vol_shock` favors the short guts; close the loop with realized vol computed from `GET /api/v1/market-data/klines`
- **Regime gate** — `GET /api/v1/quant/market`: `squeeze`/`vol_spike` probabilities support long guts, `range_low_vol` supports the short side — same gate as the equivalent strangle
- **Backtest** — band-vs-close outcomes on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08), with entry vol states pinned via `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — a guts parks far more capital than the payoff-equivalent strangle: have the agent price both and decide on liquidity via `/api/v1/market-intelligence/options` OI, since deep-ITM crypto strikes are often near-quoteless.

## Related

- [[strangle]] — the payoff-equivalent, more capital-efficient structure
- [[straddle-strangle]] — the ATM/OTM long-vol parent
- [[straddle]] — the conceptual umbrella
- [[strip-strap]] — directional straddle variants
- [[reverse-iron-condor]] — a defined-risk way to cap short-guts tail
- [[short-straddle]] — the common ATM premium-selling alternative
- [[gamma-scalping]] — dynamically hedging the long gamma
- [[deribit]], [[greeks-live]] — venue and DVOL/surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get

## Sources

- McMillan, *Options as a Strategic Investment* (5th ed.) — guts / gut spreads and their equivalence to strangles.
- Natenberg, *Option Volatility and Pricing* (2nd ed.) — ITM-vs-OTM structure choice and put-call parity.
- [[deribit]] / [[greeks-live]] documentation — European cash settlement, contract specs, inverse vs USDC-margined contracts.
