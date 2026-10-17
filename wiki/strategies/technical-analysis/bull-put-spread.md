---
title: "Bull Put Spread"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, bull-put-spread, credit-spread, bullish, defined-risk, volatility, ethereum]
aliases: ["Put Credit Spread", "Short Put Spread", "Crypto Bull Put Spread", "Deribit Put Credit Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: beginner
backtest_status: untested
related: ["[[bear-call-spread]]", "[[bull-call-spread]]", "[[bear-put-spread]]", "[[iron-condor]]", "[[vertical-spread]]", "[[put-spread]]", "[[deribit]]", "[[dvol]]", "[[greeks-live]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[delta]]", "[[max-pain]]", "[[gamma-exposure]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit_only
    role: universe
    rule: "BTC and ETH Deribit options only; alt options are too thin for a clean two-leg credit spread"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied vol served. Option quotes come from Deribit itself."
  - id: above_support_view
    role: entry
    rule: "Bullish-to-neutral: expect spot to hold above a tested support level through expiry"
    runnable: partial
    endpoint: /api/v1/indicators/technical/{coin}
    field: sr.support[].price
    note: "Served support levels are algorithmic (strength and dist_pct alongside). Which level is 'tested', and the hold forecast, are the trader's call."
  - id: short_put_25_35_delta
    role: entry
    rule: "Sell one OTM put at about 25-35 delta, at or below the support level"
    runnable: false
    note: "Strikes by delta need Deribit's option chain with Greeks, which we do not serve."
  - id: long_wing_10_20_delta
    role: entry
    rule: "Buy one further-OTM put at about 10-20 delta, one to a few strikes lower, same expiry"
    runnable: false
    note: "Same gap as short_put_25_35_delta."
  - id: credit_third_of_width
    role: entry
    rule: "Collect about one third of the strike width as credit"
    runnable: false
    note: "Needs the legs' bid and ask; no option quotes are served."
  - id: tenor_21_45_dte
    role: entry
    rule: "Expiry 21-45 days out; no weeklies"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: dvol_40_90_pctile
    role: filter
    rule: "Open only with DVOL in the 40th-90th percentile of its trailing year"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    replay: /api/v1/volatility/implied
    replay_field: items[].history[].dvol
    note: "Rank the latest dvol within history. Only about 180 daily closes are served (Pro Plus), so the percentile is over six months, not a year."
  - id: vol_regime_gate
    role: filter
    rule: "Sell when the coin's vol regime reads expanding (elevated), never vol_shock"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "From the page's AI-agent workflow. No history of the per-coin label is served for replay."
  - id: put_skew_fat
    role: filter
    rule: "Put skew fat (typically after a shakeout), so the short put is richer"
    runnable: false
    note: "No put skew, 25-delta risk reversal or per-strike IV is served."
  - id: below_put_oi_wall
    role: entry
    rule: "Park the short strike below the put open-interest wall"
    runnable: false
    note: "No per-strike open interest is served; /market-intelligence/options carries only BTC aggregate OI, the put/call ratio and one max-pain strike."
  - id: bear_regime_stand_down
    role: filter
    rule: "Stand down while strong_trend_bear or vol_spike probabilities climb"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: explain.label_posteriors.strong_trend_bear
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].post_label_1
    note: "label_posteriors holds the current probability of each regime (vol_spike beside it; post_label_4 in the replay). 'Climb' has no window or threshold on the page."
  - id: profit_target_half_credit
    role: exit
    rule: "Close at 50% of max credit"
    runnable: true
    input: position
    note: "The spread's mark comes from Deribit; no option prices are served."
  - id: manage_at_21_dte
    role: exit
    rule: "Manage or roll at about 21 DTE; roll down and out for a credit only while the bullish-to-neutral thesis holds"
    runnable: true
    input: position
  - id: stop_2x_credit
    role: stop
    rule: "Close a tested spread when the buy-back cost reaches about 2x the credit received, or flatten on a vol-shock signal"
    runnable: true
    input: position
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "The vol-shock signal is regime vol_shock; the 2x test uses the spread's mark from Deribit."
  - id: long_flush_exit
    role: exit
    rule: "Close the spread into the first long-liquidation flush rather than waiting to see whether the wing holds"
    runnable: partial
    endpoint: /api/v1/market-intelligence/squeeze-alerts?symbol={coin}&include_quiet=true
    field: alerts[].direction
    replay: /api/v1/backtesting/hl-liquidation-bars?coin={coin}&interval=5m&start={start}
    replay_field: data[].long_usd
    note: "A triggered alert with direction long_flush (longs being liquidated) is the trigger. The page defines no flush size, so the alert's own severity cut (min_severity, default 0.35) stands in. OKX + Bybit + Hyperliquid, no Binance; replay is Hyperliquid only, from 2026-07-23."
---

# Bull Put Spread

## Overview

The bull put spread (a **put credit spread**) is a bullish-to-neutral, **defined-risk** structure that collects a net credit at entry. You sell a higher-strike [[put-option|put]] and buy a lower-strike put at the same expiry; the short put generates premium, the long put caps the loss. The position keeps the full credit when the underlying stays above the short strike at expiry. It is the bullish mirror of the [[bear-call-spread]] and the lower half of an [[iron-condor]] — one of the most widely traded credit structures because of its simplicity and favorable win probability.

On [[deribit]] BTC and ETH options, the bull put spread is a defined-risk way to sell **overpriced downside** — harvesting the [[variance-risk-premium]] and the persistent crypto put skew that fattens after selloffs. The long wing hard-caps the tail a naked short put leaves open, which in crypto is essential: BTC/ETH have printed −50% in 24h. It works best entered when [[dvol|DVOL]] is **elevated** and you expect BTC/ETH to hold above a support level; it bleeds in a crash or a vol shock.

## Construction

Two legs, one expiry, same underlying (BTC or ETH), cash-settled to the Deribit index:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| 1 | Sell 1 put | OTM below spot (~25-35Δ), at/below support | the income leg |
| 2 | Buy 1 put | further OTM (~10-20Δ) | protective lower wing, defines risk |

- **Strike selection:** sell the short put around 25-35 delta (≈65-75% probability of expiring OTM), at or below a tested support level. Buy the long wing one to a few strikes lower to define the loss.
- **Ratios:** 1:1 — one contract per leg (Deribit contracts are 1 BTC or 1 ETH each).
- **Net credit** = short-put bid − long-put ask. Aim to collect **~⅓ of the width** as credit; crypto put skew often makes the short put richer.
- **Width** = short strike − long strike; sets max loss.
- **Tenor:** 21-45 DTE is the theta-rich zone. Avoid weeklies (gamma too hot for crypto's continuous gaps).

## Payoff & breakevens

- **Max profit** = net credit, when the underlying is at or above the short strike at expiry.
- **Max loss** = width − net credit, when the underlying is at or below the long wing at expiry.
- **Breakeven** = short strike − net credit.

The expiry payoff is flat at the max-profit ceiling above the short strike, sloping down between the strikes, flat at the capped-loss floor below the long wing.

## Greeks profile

- **Delta:** net long (bullish) — the position wants spot to hold or rise.
- **Gamma:** net short near the short strike — it accelerates against you as spot falls toward the short put into expiry (the crypto gamma trap; no market close to cap an overnight move).
- **Theta:** net positive — time decay is the income engine.
- **Vega:** net short — a **DVOL crush after entry helps**, a DVOL spike (which accompanies selloffs) hurts.

## Market view / when to use

- You are **bullish-to-neutral** on BTC or ETH and expect spot to hold above a support level through expiry.
- **DVOL is elevated** (roughly the 40th-90th percentile of its trailing year): the put is rich enough to pay for the wing and the tail, without selling into an active vol shock.
- You want **defined-risk** downside-premium selling rather than a naked short put or [[cash-secured-put]] — essential in crypto's fat-tailed selloffs.
- The crypto **put skew is fat** (typically after a shakeout), making the short put you sell richer.

## Adjustments & management

- **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly).
- **Time stop / roll:** manage or roll at **~21 DTE** to limit end-of-life [[gamma]]; roll down-and-out for a credit only while the bullish/neutral thesis holds.
- **Defined-risk stop:** close on a tested spread when the buy-back cost reaches **~2× the credit received**, or flatten on a DVOL vol-shock signal.
- **No early-assignment management** — Deribit options are European and cash-settled; the ex-dividend early-assignment risk of equity short puts does not exist here.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] holds the vast majority of BTC/ETH options OI. **Alt options (SOL and below) are too thin** for a clean two-leg credit spread — stick to BTC/ETH.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** options for clean USD credit, width, and breakeven. **Inverse (coin-margined)** options settle in BTC/ETH and embed quanto curvature — your coin collateral's USD value *falls with spot exactly as the short put loses*, compounding the drawdown on the tested put wing. Use inverse only if the embedded coin delta is intended.
- **DVOL regime gate:** open new put-credit spreads inside the ~40th-90th [[dvol|DVOL]] percentile band. Below ~40th the credit is too thin to pay for the tail; above ~90th you are likely selling into a vol shock.
- **24/7 & weekend gaps:** no close, no gap protection, but continuous trading. A thin-liquidity weekend headline can gap spot through the short strike at 03:00 UTC with no chance to react — the reason the protective long wing (not a naked short put) is mandatory. Expiry is **08:00 UTC**, cash-settled to Deribit's ~30-minute TWAP index, so there is **no assignment or pin risk**.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 blended US tax treatment** — the credit is ordinary short-term income in the US, trader-status-dependent in AU. After-tax net is materially below an SPX put-credit spread's.
- **Perp-funding interaction:** crypto skew is set by the [[perpetual-futures|perp]] book. After a selloff, **put skew fattens** (leveraged longs unwind, downside demand rises), making the short put richer to sell — the best entry window. Delta-hedging the residual with the perp pays or collects funding.
- **Fees:** Deribit taker fee is 0.03% of the underlying, **capped at 12.5% of the option premium** — the cap dominates on the cheap OTM long wing and is a real drag on a two-leg structure.

## Risks

- **Sharp gap down** through the long wing (macro shock, deleveraging cascade): realises max loss with no chance to manage, correlated across a market-wide selloff — the dominant tail for premium sellers.
- **Volatility expansion** — a rising-DVOL selloff marks the spread to a large unrealised loss before expiry (net short [[vega]]).
- **Over-sizing / correlation** — many correlated short-put spreads turn one bad day into an account-threatening loss ("picking up pennies in front of a steamroller").
- **Gamma trap** — holding the short put inside ~21 DTE amplifies delta swings.
- **Edge compression** — a persistently low-DVOL regime offers premium too thin to cover costs and tail risk.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH DVOL **58** (~65th percentile, put skew fat after a shakeout); 30 DTE; support near $2,800.

**Trade (per 1-ETH contract):**
- Sell 30Δ put @ **$2,800** for **$72**.
- Buy 15Δ put @ **$2,600** for **$28**.
- **Net credit = $44.** Width = $200. **Max loss = $200 − $44 = $156.**
- **Breakeven = $2,800 − $44 = $2,756.** R:R ≈ 44 : 156 ≈ **1 : 3.5** (high win probability, small reward, large tail).

**Path A — base case (holds).** ETH ranges $2,900-$3,150 and DVOL fades to 50. The short put decays; close at 50% for **+$22/contract**.

**Path B — tested but holds.** ETH dips to $2,820, just above the short strike; DVOL ticks up. At 21 DTE the mark is ~$70 loss; roll down-and-out to a $2,650/$2,450 spread for a small credit, or close for a small loss.

**Path C — flush.** A deleveraging cascade gaps ETH to $2,500 overnight; DVOL 58 → 95. The short $2,800 put is deep ITM but the long $2,600 wing caps the loss near the **−$156/contract** floor — the exact scenario the defined-risk wing exists to survive.

## Sources

- [[deribit]] / [[greeks-live]] documentation — European cash settlement, 08:00 UTC expiry, DVOL construction, USDC-margined (linear) vs inverse settlement, put-skew behavior, taker-fee premium cap.
- [[book-option-volatility-and-pricing]] — Natenberg on put-credit-spread construction, gamma near expiry, and the [[variance-risk-premium]] these structures harvest (mechanics port to crypto; costs, tails, and tax do not).
- tastytrade 25-35Δ credit-spread / 50%-profit / 21-DTE management studies — mechanics port directly; sizing and stops must be tightened for the crypto crash tail.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV/skew surface come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, options-flow, dealer-gamma, and funding context used to *time* the credit spread and read the downside tail.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime: the entry gate (want elevated/expanding, not vol_shock)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (downside dealer positioning; short-strike context)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile): cascade risk below spot
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — perp funding, the put-skew driver
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; early warning for the deleveraging flush that breaks a put-credit spread

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for realized-vol and support mapping
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for backtesting the structure

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew are Deribit / [[greeks-live]] products, not CDA.

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — sell the put spread when `GET /api/v1/volatility/regime` reads elevated/`expanding` (not `vol_shock`) and `GET /api/v1/market-intelligence/options` shows the put-OI wall below which to park the short strike
- **Regime gate** — `GET /api/v1/quant/market`: stand down while `strong_trend_bear`/`vol_spike` probabilities climb — the downside tail is the only thing that breaks this structure
- **Backtest** — short-strike breach frequency per tenor on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09); tag cascade days with `/api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30) to study the flush scenario separately
- **Tips** — while short, poll `/api/v1/market-intelligence/liquidations`: close the spread into the first long-liquidation flush rather than waiting to see whether the wing holds — the credit never justifies riding a cascade.

## Related

- [[bear-call-spread]] — the bearish credit-spread mirror
- [[bear-put-spread]] — the bearish *debit* put spread
- [[bull-call-spread]] — the bullish debit alternative (buy cheap DVOL instead of selling rich)
- [[iron-condor]] — combines a bull put spread and a [[bear-call-spread]] into a neutral structure
- [[vertical-spread]], [[put-spread]] — the families this belongs to
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]] — the vol inputs; DVOL regime gates entry
- [[variance-risk-premium]] — the structural source of the credit-spread edge
- [[funding-rate]] — the perp linkage that fattens crypto put skew
- [[max-pain]], [[gamma-exposure]] — dealer-positioning and cascade context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[theta]], [[vega]], [[delta]] — the Greeks that drive the position
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
