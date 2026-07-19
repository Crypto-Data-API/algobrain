---
title: "Put Spread"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, put-spread, debit-spread, bearish, defined-risk, ethereum]
aliases: ["Vertical Put Spread", "Bear Put Spread", "Long Put Spread", "Put Debit Spread", "Crypto Put Spread", "Deribit Put Spread"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[bear-put-spread]]", "[[bull-put-spread]]", "[[long-put]]", "[[credit-spread]]", "[[vertical-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Put Spread

## Overview

A **put spread** (vertical put spread) is a two-leg position built from a long put and a short put on the same underlying, same expiry, different strikes. The common form is the **bear put spread** — a *debit* put spread: buy a higher-strike [[put-option|put]] and sell a lower-strike put to express a **bounded bearish view** on BTC or ETH with a defined, capped cost and a defined, capped payoff. The mirror — selling the higher-strike put and buying the lower-strike put for a net *credit* — is the **[[bull-put-spread|bull put spread]]** (put credit spread), documented separately. This page covers the long/debit put spread unless noted.

On [[deribit]], the put spread is the cleanest defined-risk way to be bounded-bearish on crypto. As a net premium *buyer* it is net long [[vega]] and pays [[theta]], so it prefers a **low-[[dvol|DVOL]]** entry; a subsequent selloff (which spikes DVOL) helps twice. It has no standalone statistical edge — the "edge" is a correct directional/volatility view executed with better economics than an outright [[long-put]], partially financed by selling the deep put skew the trader does not expect to need.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Buy 1 put | ATM to slightly ITM/OTM (~45-60Δ) | the directional engine |
| 2 | Sell 1 put | lower, at your downside target (~25-35Δ) | finances the long, caps profit |

- **Strike selection:** buy strike A near spot; sell strike B lower, at or just past your BTC/ETH downside target. The sold leg sits deep on the fat crypto put skew, recapturing overpriced premium (often cutting net cost 30-60% vs an outright put).
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net debit** = long-put ask − short-put bid. Require **max profit ≥ max loss** (debit ≤ ~½ width) for a ≥1:1 structure.
- **Width** = strike A − strike B; sets the risk/reward.
- **Tenor:** 20-45 DTE to balance [[theta]] against time for the thesis to play out.

## Payoff & breakevens

- **Max profit** = width − net debit, when spot is at or below strike B at expiry.
- **Max loss** = net debit, when spot is at or above strike A at expiry (both puts expire worthless).
- **Breakeven** = strike A − net debit.

The expiry payoff is a ramp: flat at the max-loss floor above strike A, rising as spot falls between the strikes, flat at the max-profit ceiling below strike B.

## Greeks profile

- **Delta:** net short (bearish) — the directional engine.
- **Gamma:** net long from the bought leg, partly offset by the short leg — a muted single long put.
- **Theta:** net negative — but *less* than an outright long put, because the short leg's decay works for you.
- **Vega:** net long — but less so than an outright put; a **DVOL rise helps** (common in selloffs), a DVOL crush hurts.

## Market view / when to use

- You are **moderately bearish** on BTC or ETH over days-to-weeks — a *bounded* down-move, not a crash you expect to run far past strike B.
- **DVOL is low-to-moderate** so the long put is affordable; the short leg further cheapens it via the crypto put skew.
- You want **defined risk** and a lower [[theta]] bleed than a standalone [[long-put]], accepting a capped payoff at strike B.
- You have a downside target (a broken support, an unlock-driven flush) that maps to strike B.

## Adjustments & management

- **Profit target:** close for **50-75% of max value** (= width − debit) rather than holding to expiry.
- **Stop:** cut on thesis break (spot rallies back through strike A) or at roughly **−50-70% of the debit**.
- **Time stop:** manage/roll inside **~10-14 DTE** to limit [[gamma]] into the 08:00 UTC expiry.
- **Roll down-and-out** only if the thesis strengthens; never add debit to a losing directional trade.
- **No early-assignment management** — Deribit options are European and cash-settled, so the deep-ITM short-put assignment risk of equity put spreads does not apply.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] is effectively "the market" for BTC/ETH options. **Alt options (SOL and below) are too thin** to leg a clean put spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options so debit, width, and breakeven are clean USD numbers. **Inverse (coin-margined)** options settle in BTC/ETH and embed quanto curvature; a bearish inverse position also loses collateral USD value as spot falls, muddying the payoff. Use inverse only if the coin delta is intended.
- **DVOL regime:** debit put spreads want **cheap** vol. Enter when [[dvol|DVOL]] is depressed; a selloff then lifts DVOL and helps the net-long-vega position. Avoid buying after a spike has inflated both legs.
- **24/7 & weekend gaps:** no close and no gap protection, but continuous trading. A weekend risk-off gap works *for* the position; an adverse gap is capped at the debit. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index — **no exercise, assignment, or pin risk**.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — the payoff is ordinary short-term capital-gains in the US, trader-status-dependent in AU. After-tax net is materially below an SPX put spread's.
- **Perp-funding interaction:** crypto put skew is set by the [[perpetual-futures|perp]] book; after a selloff **put skew fattens**, making the short leg richer to sell — better financing for a *new* put spread. Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheaper OTM short leg and is a real drag on a two-leg structure.

## Risks

- **Being wrong on direction** — the dominant failure: BTC/ETH rallies or chops and the debit decays to zero.
- **Capped downside** — a crash *through* strike B earns no extra; the short leg gives the tail back. An outright [[long-put]] would have paid more.
- **DVOL crush** — if vol collapses after entry both legs lose; the spread cushions this vs a naked put but is still net long [[vega]].
- **Gamma near expiry** — spot settling between strikes at 08:00 UTC creates uncertain, gamma-heavy outcomes (though cash settlement removes assignment risk).
- **Cost erosion / skew headwind** — the fat crypto put skew makes the long leg expensive; two-leg costs on wide chains erode the edge. Use combo/RFQ execution ([[greeks-live]] / Paradigm).

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,200**; ETH DVOL **55** (moderate); 30 DTE. Thesis: drift to ~$2,900 over the next month.

**Trade (per 1-ETH contract):**
- Buy 50Δ put @ **$3,200** for **$210**.
- Sell 30Δ put @ **$2,900** for **$95**.
- **Net debit = $115.** Width = $300. **Max profit = $300 − $115 = $185.** **Max loss = $115.**
- **Breakeven = $3,200 − $115 = $3,085.** R:R ≈ 185 : 115 ≈ **1.6 : 1**.

**Outcome (thesis works).** At expiry ETH = $2,880: the $3,200 put is worth ~$320, the $2,900 put ~$20 → spread worth ~$300 (near full width). P&L ≈ **+$185/contract** (max). Had ETH stayed above $3,200, the full $115 debit is lost. Managed earlier: at $2,950 with 12 DTE the spread might mark ~$150 — closing there banks ~$35 and sheds the remaining gamma.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, put-skew behavior, taker-fee premium cap.
- The Options Industry Council (OIC), "Bear Put Spread" — https://www.optionseducation.org/strategies/all-strategies/bear-put-spread (mechanics; equity-specific assignment/tax do not port).
- Hull, J. C., *Options, Futures, and Other Derivatives* — vertical spreads chapter (pricing and payoff mechanics).
- tastytrade debit-spread management studies (50-75% profit-take) — mechanics port; sizing tightened for crypto gaps.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context used to *time* a put spread (buy cheap vol) and read the downside tail.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate — you want *compressed* for a debit put spread
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (downside dealer positioning; short-strike context)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): cascade risk below spot that would help the position
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the crypto put-skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; the deleveraging that drives a fast down-move

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history (find low-DVOL entry windows)
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for trend context and support/resistance mapping
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can time and manage the spread with the endpoints this section already cites:

- **Entry timing** — `GET /api/v1/volatility/regime` reading `compressed` is the buy-cheap-vol gate for a debit spread; `GET /api/v1/volatility/regime/{symbol}` (60-day history) finds how rare the current low-vol window is
- **Downside map** — `GET /api/v1/quant/gex` + `GET /api/v1/market-intelligence/liquidations` locate the liquidation fuel below spot that would carry price toward strike B
- **Regime gate** — `GET /api/v1/quant/market`: rising strong_trend_bear / vol_spike probabilities support the bearish thesis; a strong_trend_bull print argues to stand down
- **Backtest** — test the bounded-down-move thesis on `GET /api/v1/backtesting/klines` (ETHUSDT/BTCUSDT 1h/4h/1d back to 2017-08); strike-level IV and skew history are Deribit's, so P&L replays of the option legs need Deribit data
- **Tips** — poll the funding endpoint after a selloff: fattened put skew makes *new* spreads better financed, but marks existing long legs richer — a natural profit-take check

## Related

- [[bear-put-spread]] — the same debit put spread, indexed under its canonical name
- [[bull-put-spread]] — the credit (short put spread) mirror
- [[long-put]] — the un-spread, fully convex bearish building block
- [[credit-spread]] — general credit-spread concept
- [[vertical-spread]] — the four-flavour vertical-spread family overview
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[funding-rate]] — the perp linkage that shapes crypto put skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[delta]], [[theta]], [[vega]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
