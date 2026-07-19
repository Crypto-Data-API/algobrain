---
title: "Bear Call Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, bear-call-spread, credit-spread, bearish, defined-risk, volatility, bitcoin]
aliases: ["Call Credit Spread", "Short Call Spread", "Crypto Bear Call Spread", "Deribit Call Credit Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[bull-put-spread]]", "[[bear-put-spread]]", "[[bull-call-spread]]", "[[iron-condor]]", "[[vertical-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[delta]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Bear Call Spread

## Overview

The bear call spread (a **call credit spread**) is a bearish-to-neutral, **defined-risk** structure that collects a net credit at entry. You sell a lower-strike [[call-option|call]] and buy a higher-strike call at the same expiry; the short call generates premium, the long call caps the otherwise-unlimited upside risk. The position keeps the full credit when the underlying stays below the short strike at expiry. It is the bearish mirror of the [[bull-put-spread]] and the upper half of an [[iron-condor]].

On [[deribit]] BTC and ETH options, the bear call spread is a defined-risk way to sell **overpriced upside** — harvesting the [[variance-risk-premium]] on calls plus the call-demand of leveraged longs. The long wing hard-caps the tail that a naked short call leaves open, which in crypto is non-negotiable: BTC has printed +20% days on short squeezes and ETF headlines. It works best entered when [[dvol|DVOL]] is **elevated** and you expect BTC/ETH to stall below a resistance level; it bleeds in a melt-up.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Sell 1 call | OTM above spot (~25-35Δ), at/above resistance | the income leg |
| 2 | Buy 1 call | further OTM (~10-20Δ) | protective upper wing, defines risk |

- **Strike selection:** sell the short call around 25-35 delta (≈65-75% probability of expiring OTM), at or above a tested resistance level. Buy the long wing one to a few strikes higher to define the loss.
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net credit** = short-call bid − long-call ask. Aim to collect **~⅓ of the width** as credit; crypto call skew can be rich when funding runs hot, improving the credit.
- **Width** = long strike − short strike; sets max loss.
- **Tenor:** 21-45 DTE is the theta-rich zone. Avoid weeklies (gamma too hot for crypto's continuous gaps).

## Payoff & breakevens

- **Max profit** = net credit, when the underlying is at or below the short strike at expiry.
- **Max loss** = width − net credit, when the underlying is at or above the long wing at expiry.
- **Breakeven** = short strike + net credit.

The expiry payoff is flat at the max-profit ceiling below the short strike, sloping down between the strikes, flat at the capped-loss floor above the long wing.

## Greeks profile

- **Delta:** net short (bearish) — the position wants spot to stay put or fall.
- **Gamma:** net short near the short strike — it accelerates against you as spot approaches the short call into expiry (the crypto gamma trap, worse than equities because there is no market close).
- **Theta:** net positive — time decay is the income engine.
- **Vega:** net short — a **DVOL crush after entry helps**, a DVOL spike (which usually accompanies a sharp move) hurts.

## Market view / when to use

- You are **bearish-to-neutral** on BTC or ETH and expect spot to stay below a resistance level through expiry.
- **DVOL is elevated** (roughly the 40th-90th percentile of its trailing year): the call is rich enough to pay for the wing and the tail, but you are not selling into an active vol shock.
- You want **defined-risk** upside-premium selling rather than a naked short call — essential in crypto, where squeezes are violent.
- **Funding is richly positive:** leveraged longs paying funding firms OTM call skew, making the short call you sell richer (see *Crypto specifics*).

## Adjustments & management

- **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly).
- **Time stop / roll:** manage or roll at **~21 DTE** to limit end-of-life [[gamma]]; roll up-and-out for a credit only while the bearish/neutral thesis holds.
- **Defined-risk stop:** close on a tested spread when the buy-back cost reaches **~2× the credit received**, or flatten on a DVOL/funding regime flip that invalidates the view.
- **No early-assignment management** — Deribit options are European and cash-settled, so the ex-dividend early-assignment risk of equity short calls simply does not exist here.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the vast majority of BTC/ETH options OI. **Alt options (SOL and below) are too thin** for a clean two-leg credit spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options for clean USD credit, width, and breakeven. **Inverse (coin-margined)** options settle in the coin and embed quanto curvature — your BTC/ETH collateral's USD value moves with spot, distorting the payoff and adding wrong-way risk on a rally. Use inverse only deliberately.
- **DVOL regime gate:** open new call-credit spreads inside the ~40th-90th [[dvol|DVOL]] percentile band. Below ~40th the credit is too thin to pay for the tail; above ~90th you are likely selling into a vol shock.
- **24/7 & weekend gaps:** no close, no gap protection, but continuous trading. A weekend squeeze can gap spot through the short strike at 03:00 UTC with no chance to react — the reason the protective long wing (not a naked short call) is mandatory. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index, so there is **no assignment or pin risk**.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — the credit is ordinary short-term income in the US (full marginal rates), trader-status-dependent in AU. After-tax net is materially below an SPX call-credit spread's.
- **Perp-funding interaction:** crypto call skew is set by the [[perpetual-futures|perp]] book, not by equity hedgers. **Richly positive [[funding-rate|funding]] fattens OTM call skew**, making the short call richer to sell — the single best tailwind for this structure. After a squeeze exhausts, call skew flattens and the edge thins.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheap OTM long wing and is a real drag on a two-leg structure.

## Risks

- **Sharp rally / gap up** through the long wing (ETF inflow, short squeeze, macro melt-up): realises max loss, correlated across a broad crypto rally.
- **Volatility expansion** — a rising-DVOL rally marks the spread to a large unrealised loss before expiry (net short [[vega]]).
- **Gamma trap** — holding the short call inside ~21 DTE turns small up-moves into violent delta swings.
- **Edge compression** — thin call skew in a low-DVOL, low-funding regime fails to cover costs and tail risk.
- **Execution/liquidity** — far-OTM crypto call series can be wide; use combo/RFQ execution ([[greeks-live]] / Paradigm).

## Worked crypto example

**Setup (BTC, USDC-margined/linear).** BTC spot **$60,000**; BTC DVOL **52** (~60th percentile); 32 DTE; resistance near $63,000. Funding richly positive (+0.03%/8h → firm call skew).

**Trade (per 1-BTC contract):**
- Sell 33Δ call @ **$63,000** for **$1,900**.
- Buy 18Δ call @ **$66,000** for **$900**.
- **Net credit = $1,000.** Width = $3,000. **Max loss = $3,000 − $1,000 = $2,000.**
- **Breakeven = $63,000 + $1,000 = $64,000.** R:R ≈ 1,000 : 2,000 = **1 : 2**.

**Path A — base case (stall).** BTC fades to $57,000 as funding cools and DVOL drifts to 46. Both calls decay; close at 50% for **+$500/contract**.

**Path B — grind up, no breach.** BTC drifts to $62,500, just under the short strike; DVOL flat. At 21 DTE the mark is ~$700 loss; roll up-and-out to a $65,000/$68,000 spread for a small net credit, or close for a small loss.

**Path C — squeeze.** An ETF-inflow headline gaps BTC to $67,000; DVOL 52 → 74. The short $63,000 call is deep ITM but the long $66,000 wing caps the loss near the **−$2,000/contract** floor — the exact scenario the defined-risk wing exists to survive.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on call-credit-spread construction, gamma risk near expiry, and the [[variance-risk-premium]] these structures harvest (mechanics port to crypto; costs, tails, and tax do not).
- tastytrade 25-35Δ credit-spread / 50%-profit / 21-DTE management studies — mechanics port directly; sizing and stops must be tightened for the crypto squeeze tail.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context used to *time* the credit spread and read the upside tail.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate (want elevated/expanding, not vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (upside dealer positioning; short-strike context)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): squeeze/cascade risk above spot
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding, the call-skew driver and the best tailwind read
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; early warning for the short-squeeze that breaks a call-credit spread

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol and resistance mapping
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — sell the spread when `GET /api/v1/volatility/regime` reads elevated/`expanding` (not `vol_shock`) and `GET /api/v1/market-intelligence/options` places max pain at or below spot; park the short call above the call-OI wall
- **Regime gate** — `GET /api/v1/quant/market`: a leading `strong_trend_bull` probability is the veto — call-credit spreads die in squeezes; `/api/v1/quant/gex` short-dealer-gamma above spot is the squeeze-fuel confirmation
- **Backtest** — short-strike breach frequency per tenor from `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); no options-chain history is served, so proxy outcomes with underlying paths and pin entries to point-in-time regimes via `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — while short, poll `/api/v1/market-intelligence/liquidations`: a short-liquidation cascade is the early exit; funding flipping strongly positive on `/api/v1/derivatives/funding-rates?coin=BTC` fattens the upside tail against the position.

## Related

- [[bull-put-spread]] — the bullish credit-spread mirror
- [[bear-put-spread]] — the bearish *debit* alternative (buy cheap DVOL instead of selling rich)
- [[bull-call-spread]] — the bullish debit spread
- [[iron-condor]] — combines a bear call spread with a [[bull-put-spread]] into a neutral structure
- [[vertical-spread]] — the family this belongs to
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[variance-risk-premium]] — the structural source of the credit-spread edge
- [[funding-rate]] — the perp linkage that fattens crypto call skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning and squeeze context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
