---
title: "Bear Put Spread"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [options, crypto, derivatives, bear-put-spread, debit-spread, bearish, defined-risk, ethereum]
aliases: ["Put Debit Spread", "Long Put Spread", "Crypto Bear Put Spread", "Deribit Put Debit Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[bull-call-spread]]", "[[bear-call-spread]]", "[[bull-put-spread]]", "[[put-spread]]", "[[vertical-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
---

# Bear Put Spread

## Overview

The bear put spread (a **put debit spread**) is a bearish, **defined-risk** structure that pays a net debit at entry. You buy a higher-strike [[put-option|put]] and sell a lower-strike put at the same expiry; the long put gives the downside, the short put cheapens the position and caps the profit. It is the bearish mirror of the [[bull-call-spread]] and the debit-based, directional cousin of the credit-collecting [[bear-call-spread]].

On [[deribit]] BTC and ETH options, the bear put spread is the cleanest way to express a *bounded* bearish view on crypto with a loss fully known before you enter. As a net premium *buyer* it is net long [[vega]] and pays [[theta]]: it works best entered when [[dvol|DVOL]] is **low**, so the long put is cheap, and a subsequent selloff (which usually spikes DVOL) helps twice. It does **not** harvest the [[variance-risk-premium]]; the edge is a correct directional forecast, cheapened by giving up gains below the short strike. Note the built-in headwind: crypto **put skew** makes long puts relatively expensive, so the sold lower-strike put — sitting further down that skew — is a valuable partial finance.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Buy 1 put | ATM to slightly ITM (~50-65Δ) | the directional engine |
| 2 | Sell 1 put | OTM, at your downside target (~30-40Δ) | finances the long, caps profit |

- **Strike selection:** buy the long put at-the-money to slightly in-the-money for a higher-probability spread; buy slightly OTM for a cheaper, higher-payoff structure. Place the short put at or just past your BTC/ETH downside target — deep on the fat put skew, which cheapens the spread.
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net debit** = long-put ask − short-put bid. Discipline: pay no more than **~⅔ of the spread width** so max profit ≥ ~0.5× max loss.
- **Width** = long strike − short strike; roughly 5-15% of spot is typical.
- **Tenor:** 21-45 DTE. Longer tenors limit [[theta]] drag on the long leg and give the move time.

## Payoff & breakevens

- **Max profit** = width − net debit, when the underlying is at or below the short strike at expiry.
- **Max loss** = net debit, when the underlying is at or above the long strike at expiry (both puts expire worthless).
- **Breakeven** = long strike − net debit.

The expiry payoff is a ramp: flat at the max-loss floor above the long strike, rising as spot falls between the strikes, flat at the max-profit ceiling below the short strike.

## Greeks profile

- **Delta:** net short (bearish) — the directional engine.
- **Gamma:** net long from the bought leg, partly offset by the short leg — a muted single long put.
- **Theta:** net negative — time decay works against you while spot sits above the long strike.
- **Vega:** net long — a **DVOL rise after entry helps** (common in selloffs), a DVOL crush hurts. Hence the preference to enter in a low-DVOL regime.

## Market view / when to use

- You are **moderately bearish** on BTC or ETH and expect spot at or below the short strike by expiry, ideally on an identifiable catalyst (unlock, macro risk-off, exhaustion at resistance).
- **DVOL is low-to-moderate** (roughly the 10th-50th percentile of its trailing year) so the long put is cheap — the mirror of the credit-spread regime.
- You want **defined risk** rather than an open-ended short perp position or the [[theta]] bleed of an outright long put.
- You want a cheaper alternative to a standalone protective put, financed by selling deep put skew you do not expect to need.

## Adjustments & management

- **Profit target:** take profits at **50-75% of max value** rather than grinding into expiry-week [[gamma]].
- **Stop:** cut at roughly **−50-60% of the debit** or on thesis invalidation (support reclaimed, catalyst resolved bullishly).
- **Time stop:** close by **~10-14 DTE** if neither target nor stop is hit — crypto gamma accelerates into the 08:00 UTC expiry.
- **Roll down-and-out** for additional debit only if the thesis strengthens; never chase a losing directional debit with more premium.
- **No early-assignment management needed** — Deribit options are European and cash-settled, removing the deep-ITM early-assignment risk that equity short puts carry.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] is effectively "the market" for BTC/ETH options. **Alt options (SOL and below) are too thin** to leg a clean spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options so the debit, width, and breakeven are clean USD numbers. **Inverse (coin-margined)** options settle in BTC/ETH and embed a quanto-like curvature; a bearish inverse position also sees its coin collateral lose USD value as spot falls, muddying the payoff. Use inverse only if the embedded coin delta is intended.
- **DVOL regime:** debit structures want **cheap** vol. Enter when [[dvol|DVOL]] is depressed; a selloff then lifts DVOL and helps the net-long-vega position. Avoid buying after a vol spike has already inflated both legs.
- **24/7 & weekend gaps:** no close and no gap protection, but continuous trading. A weekend risk-off gap works *for* this position, but a gap the wrong way is capped at the debit. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index — **no exercise, assignment, or pin risk**.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — every leg is an ordinary short-term capital-gains event in the US, trader-status-dependent in AU. After-tax net is materially below an SPX put spread's.
- **Perp-funding interaction:** crypto put skew is set by the [[perpetual-futures|perp]] book. After a selloff, **put skew fattens**, making the short put you sell richer — better financing for a *new* bear put spread, though it also means you paid up for the long leg. Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheaper OTM short leg and is a real drag on a two-leg structure.

## Risks

- **Sideways/up drift** — the most common killer: BTC/ETH fails to fall, [[theta]] erodes the long put, the debit decays.
- **DVOL crush** — buying puts into an elevated-DVOL, already-skewed surface then suffering a vol collapse leaves the position underwater even on a small favorable move (net long [[vega]]).
- **Adverse gap up** — a squeeze or ETF-inflow gap above the long strike realises the full debit; capped, but total.
- **Capped downside profit** — a crash earns no more than max profit beyond the short strike; the give-up versus an outright put.
- **Skew headwind + execution** — the fat crypto put skew makes long puts expensive, a structural drag; two-leg execution costs bite. Use combo/RFQ ([[greeks-live]] / Paradigm).

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **50** (~40th percentile, moderate); 35 DTE. Moderately bearish into a macro risk-off thesis.

**Trade (per 1-ETH contract):**
- Buy 55Δ put @ **$3,000** for **$180**.
- Sell 33Δ put @ **$2,700** for **$75**.
- **Net debit = $105.** Width = $300. **Max profit = $300 − $105 = $195.** **Max loss = $105.**
- **Breakeven = $3,000 − $105 = $2,895.** R:R ≈ 195 : 105 ≈ **1.86 : 1**.

**Path A — thesis works.** ETH slides to $2,650 over two weeks and DVOL jumps to 62. The spread marks near full width (~$300 intrinsic minus the OTM short-put value); close at ~$210 realized (past the 75% target).

**Path B — chop.** ETH oscillates $2,950-$3,100 and DVOL fades to 44. Theta and the DVOL fade erode the mark to ~$55; the time stop at 12 DTE closes it for **−$50/contract** (partial debit lost).

**Path C — squeeze up.** ETH gaps to $3,250; both puts collapse. The position is worth ~$15; close for **≈ −$90/contract**, near the defined max loss the structure caps at.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, put-skew behavior, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on vertical-spread construction, payoff, and how [[implied-volatility]] and skew determine debit-spread cost (mechanics port to crypto; costs, tails, and tax do not).
- tastytrade debit-spread management studies (50-75% profit-take, directional cost discipline) — mechanics port; sizing and stops tightened for crypto's continuous gaps.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context used to *time* a debit spread (buy cheap vol) and read the downside tail.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate — you want *compressed* for a debit spread
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (downside dealer positioning; short-strike context)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): cascade risk below spot that would help the position
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the crypto put-skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; the deleveraging that drives a fast down-move

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history (find low-DVOL entry windows)
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for trend context and resistance mapping
- `GET /api/v1/backtesting/klines` — deep kline archive for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — buy the debit spread when `GET /api/v1/volatility/regime` reads `compressed` (vol is cheap) while `GET /api/v1/derivatives/funding-rates?coin=ETH` stays positive — crowded longs are the fuel for the down-move the spread needs
- **Regime gate** — `GET /api/v1/quant/market`: rising `strong_trend_bear` or `vol_spike` probability supports entry; a stable `range_low_vol` state means the debit decays unspent
- **Backtest** — measure how often N%-down moves complete within the tenor using `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08); pair each simulated entry with point-in-time regime state from `/api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — `/api/v1/market-intelligence/liquidations` shows the deleveraging flush the spread profits from — take profits into the cascade rather than holding for max value; use the 60-day `/api/v1/volatility/regime/{symbol}` history to confirm the vol window is genuinely cheap, not just recently crushed.

## Related

- [[bull-call-spread]] — the bullish debit-spread mirror
- [[bear-call-spread]] — the bearish *credit* alternative (sell rich DVOL instead of buying cheap)
- [[bull-put-spread]] — the bullish credit spread
- [[put-spread]] — the put-vertical family overview
- [[vertical-spread]] — the four-flavour vertical-spread family
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[funding-rate]] — the perp linkage that shapes crypto put skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[delta]], [[theta]], [[vega]], [[gamma]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
