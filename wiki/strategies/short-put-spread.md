---
title: "Short Put Spread"
type: strategy
created: 2026-05-07
updated: 2026-10-17
status: good
tags: [options, crypto, derivatives, volatility, swing-trading, bitcoin, ethereum]
aliases: ["Bull Put Spread", "Put Credit Spread", "Vertical Put Credit Spread", "Short Put Vertical", "Crypto Bull Put Spread"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[credit-spread]]", "[[iron-condor]]", "[[short-strangle]]", "[[cash-secured-puts]]", "[[crypto-options-volatility-selling]]", "[[deribit]]", "[[greeks-live]]", "[[dvol]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[funding-rate]]", "[[variance-risk-premium]]", "[[skew]]", "[[max-pain]]", "[[gamma-exposure]]", "[[section-1256-contracts]]", "[[theta]]", "[[vega]]", "[[gamma]]", "[[delta]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit_only
    role: universe
    rule: "BTC and ETH Deribit options only; alt options are too thin for a clean defined-risk vertical"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "These are the two coins with Deribit implied-vol data served. Option quotes come from Deribit itself."
  - id: short_put_20_30_delta
    role: entry
    rule: "Sell one put at about 20-30 delta, below spot"
    runnable: false
    note: "No option chain, per-strike IV or Greeks are served; the strike by delta comes from Deribit's chain."
  - id: long_wing_8_12_delta
    role: entry
    rule: "Buy one put at about 8-12 delta, one to a few strikes lower, same expiry"
    runnable: false
    note: "Same gap as short_put_20_30_delta: strike by delta needs Deribit's chain."
  - id: credit_vs_width
    role: entry
    rule: "Net credit at least 25-33% of the strike width"
    runnable: false
    note: "Needs the two legs' bid and ask; no option quotes are served."
  - id: tenor_21_45_dte
    role: entry
    rule: "Expiry 21-45 days out; no weeklies and nothing past 60 DTE"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "term_structure lists the nearest 12 Deribit expiries. It is Pro Plus and empty on lower tiers."
  - id: dvol_40_90_pctile
    role: filter
    rule: "Enter only with DVOL in its 40th-90th percentile band: skip a low-DVOL grind and an active vol shock"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    replay: /api/v1/volatility/implied
    replay_field: items[].history[].dvol
    note: "Rank the latest dvol within history (about 180 daily closes; Pro Plus). The page names no lookback window; 180 days is the longest served, so a one-year percentile is not possible."
  - id: vrp_above_5
    role: filter
    rule: "DVOL minus 30-day realized vol above about 5 vol points"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].vrp
    note: "vrp = dvol - realized_30, where realized_30 is the 30-day Garman-Klass estimate rather than close-to-close. For replay, pair items[].history[].dvol with history[].rv_gk_30 on /api/v1/volatility/regime/{symbol} (60 days deep)."
  - id: not_vol_shock
    role: filter
    rule: "No entry while the coin's vol regime reads vol_shock"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
  - id: put_skew_rich
    role: filter
    rule: "Put skew fat, so the short put specifically pays well"
    runnable: false
    note: "No put skew, 25-delta risk reversal or per-strike IV is served. The page's proxy is funding_flip_skew."
  - id: funding_flip_skew
    role: filter
    rule: "Prefer entry after a selloff in which perp funding has flipped, the signal that put skew has fattened"
    runnable: partial
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=48
    field: history[].funding_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1h&start={start}
    replay_field: data[].funding_rate_mean
    note: "A sign change from positive to negative over the window is the flip. The page gives no window or size for the selloff, and the skew it stands for is not served. Binance funding is binance.current_rate on /api/v1/derivatives/funding-rates?coin={coin}."
  - id: bullish_thesis_check
    role: filter
    rule: "Stand aside while the market regime shows sustained strong_trend_bear probability: a persistent bear is this spread's weakness"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's AI-agent workflow. 'Sustained' has no length; regime.in_regime_since and candles_in_regime give how long the label has held. The coin's own read is /api/v1/quant/coins/{symbol}."
  - id: profit_target_half_credit
    role: exit
    rule: "Close at 50% of max credit (50-75% for tighter spreads)"
    runnable: true
    input: position
    note: "The spread's current mark comes from Deribit; no option prices are served."
  - id: time_stop_21_dte
    role: exit
    rule: "Close or roll at about 21 DTE if the target has not hit"
    runnable: true
    input: position
  - id: loss_cap_2x_credit
    role: stop
    rule: "Close when the loss reaches about 2x the credit received"
    runnable: true
    input: position
  - id: one_roll_only
    role: exit
    rule: "If the short strike is breached but the thesis holds, roll down and out once for a net credit, never a second time"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].oracle_price
    note: "The breach (spot below the short strike) and the roll count are mechanical; 'thesis holds' is the trader's judgement. oracle_price is a CEX spot composite close to Deribit's index."
  - id: dvol_shock_kill
    role: stop
    rule: "Flatten if DVOL rises more than 50% in a session, or the position delta exceeds about 2x its entry delta"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "Crypto has no session; the nearest served step is the latest dvol against the prior day's close in history (daily closes only, no intraday DVOL). Position delta comes from Deribit; no Greeks are served."
  - id: down_gap_warning
    role: stop
    rule: "Watch liquidations and dealer gamma for the cascade that gaps through the long wing"
    runnable: partial
    endpoint: /api/v1/market-intelligence/liquidations?symbol={coin}
    field: data[].liquidation_usd_1h
    note: "From the page's AI-agent workflow, with no threshold. OKX + Bybit + Hyperliquid (no Binance). The gamma input is coins.{coin}.regime.score on /api/v1/quant/gex?symbol={coin}, a perp analog, not Deribit dealer gamma."
---

# Short Put Spread

## Overview

A short put spread (also **bull put spread** or **put credit spread**) sells a higher-strike put and simultaneously buys a lower-strike put, same expiry — collecting a net credit. It is the **defined-risk, bullish-biased** member of the [[credit-spread]] family: profitable if the underlying stays above the short strike, with a hard max loss equal to the strike width minus the credit. It sits between [[cash-secured-puts]] (capital-intensive, undefined notional) and a naked short put or [[short-strangle]] (capital-efficient, undefined risk), and pairing it with a short call spread yields a neutral [[iron-condor]].

In crypto this is the go-to way to express **"BTC/ETH won't fall hard"** with a capped tail on [[deribit]]. The seller harvests the crypto [[variance-risk-premium]] and specifically the **put-skew premium** — Deribit put wings are persistently bid because the tail is real (liquidation cascades, −50% days), so the short put is genuinely rich. The long lower-strike put re-insures that tail. Deribit options are **European and cash-settled**, so there is no early assignment and no ex-dividend trap (crypto pays no dividends); the residual risks are 24/7 gap risk and a DVOL spike marking the spread against you.

## Construction

Two puts, one expiry, cash-settled to the Deribit index, on BTC or ETH:

| Leg | Action | Strike (delta) | Purpose |
|---|---|---|---|
| Short | Sell 1 put | ~20-30Δ, below spot | credit + bullish tilt |
| Long | Buy 1 put | ~8-12Δ, further below | protective lower wing |

- **Short strike:** 20-30Δ (nearer the money than a neutral condor's 15-20Δ). The wider delta captures more credit at a deliberately higher loss probability — that *is* the bullish-tilt intent.
- **Long wing:** 8-12Δ, one to a few strikes lower; it defines and caps the loss.
- **Net credit:** target **≥ 25-33% of the spread width**; below that the risk/reward is not worth it.
- **Tenor:** 21-45 DTE — the theta-rich zone; avoid weeklies (crypto gamma) and > 60 DTE (DVOL-regime vega).
- **[[dvol|DVOL]] gate:** enter in the ~40th-90th DVOL percentile band; skip a low-DVOL grind (thin credit) and an active vol shock (selling into the spike).

## Payoff & breakevens

Short put `Ks`, long put `Kl` (`Kl < Ks`), net credit `C`:

- **Max profit** = `C`, when spot ≥ `Ks` at expiry.
- **Max loss** = `(Ks − Kl) − C`, when spot ≤ `Kl`.
- **Breakeven** = `Ks − C`.

```
Short put spread P&L at expiration

 +C  ┤                       ┌────────────────  (spot ≥ Ks: keep full credit)
     │                      /
  0 ─┼─────────────────────/───────────────────
     │                    / breakeven = Ks − C
 −ML ┤━━━━━━━━━━━━━━━━━━━━/   (spot ≤ Kl: max loss = width − C)
     └──────────────────────────────────────────
          Kl(long)     Ks(short)
```

Two-step, capped payoff: full credit above the short strike, a linear loss zone between the strikes, a flat max-loss floor at and below the long strike. The long wing turns the open-ended short-put tail into a known rectangle.

## Greeks profile

- **[[delta]]:** **positive** (bullish) — the 20-30Δ short strike gives the deliberate long tilt versus a neutral [[iron-condor]].
- **[[gamma]]:** **negative**, but capped by the long wing near/through `Kl`.
- **[[theta]]:** **positive** — the daily income leg; smaller than a naked put because the wing pays out some theta.
- **[[vega]]:** **negative**, muted — net short vega, but the long wing offsets a chunk, so the spread reprices more gently than a naked put in a [[dvol|DVOL]] shock.

Every Greek sits **between** a naked short put and a fully neutral condor: less credit, less theta, less vega — but a hard, known loss ceiling.

## Market view / when to use

- **Bullish-to-neutral** on BTC/ETH — you expect spot to hold above the short strike, not necessarily rally.
- **[[dvol|DVOL]] elevated** (40th-90th percentile) so the credit is rich; **put skew fat** so the short put specifically pays well.
- **VRP confirmation:** DVOL − 30-day realized vol > ~5 vol points.
- You want a **defined-risk, capital-light** bullish premium play — lower buying-power use than a cash-secured put, hard tail cap unlike a naked short put.

## Adjustments & management

- **Profit target:** close at **50% of max credit** (or 50-75% for tighter spreads).
- **Time stop:** close or roll at **~21 DTE** if not at target — crypto gamma accelerates into expiry.
- **Loss cap:** close at **~2× the credit** received.
- **Tested-strike roll:** if the short strike is breached but the thesis holds, roll **down and out** one time for a net credit — never more; rolling a broken thesis just deepens the loss.
- **DVOL-shock kill:** flatten if DVOL rises **> 50% in a session** or delta exceeds ~2× entry — the tail circuit-breaker.

## Crypto specifics

- **Venue & underlyings:** [[deribit]] dominates BTC/ETH options open interest and is effectively "the market." **Alt options are too thin for a clean defined-risk vertical** — BTC/ETH only.
- **Put-skew premium is the specific edge:** crypto put skew is set by the [[perpetual-futures|perp]] book and liquidation-cascade fear, not pension hedging. After a selloff, [[funding-rate|funding]] flips and put skew fattens — the short put gets richer exactly when you want to sell it (carefully, respecting the DVOL gate). See [[skew]].
- **European cash settlement — no assignment, no ex-dividend trap:** European, cash-settled to the ~30-minute index TWAP at **08:00 UTC**. The short put **cannot be assigned early**, and with **no dividends** in crypto the ex-dividend exercise hazard is absent. No pin/assignment risk.
- **Inverse vs linear/USDC settlement:** prefer **USDC-margined (linear)** for a clean USD credit and breakeven. **Inverse (coin-margined)** puts are BTC/ETH-settled and embed a quanto-like curvature — worst-case, your collateral loses USD value in exactly the down-move that tests the put. Use inverse only if you *want* embedded coin exposure.
- **24/7 & weekend gaps:** no close; a thin-weekend headline can gap spot straight through the short put at 03:00 UTC — the long wing (not a naked put) is non-negotiable.
- **No [[section-1256-contracts|§1256]]:** offshore Deribit contracts get **no 60/40 treatment** — the credit is ordinary/short-term (US) or trader-status-dependent (AU).
- **Fees:** Deribit taker fee 0.03% of underlying, **capped at 12.5% of the option premium** — the cap bites hardest on the cheap OTM long wing.

## Risks

- **Gap below the long strike:** max loss realises immediately; a 10%+ overnight gap through the spread maxes it out.
- **Sustained downtrend:** the bullish tilt is wrong-footed — the structure bleeds steadily (though capped) as the short strike is repeatedly tested. A persistent bear market, not a single vol shock (which is capped), is its specific weakness.
- **DVOL spike:** negative vega marks the spread against you even before spot moves.
- **Premium compression:** low-DVOL entries earn too little credit versus the max loss.
- **Skew flattening:** if put skew compresses, the put side loses its specific edge — watch skew alongside DVOL.
- **Discretionary over-rolling:** rolling losing spreads repeatedly converts a defined-risk loss into an open-ended time loss.

## Worked crypto example

**Setup (ETH, USDC-margined/linear).** ETH spot **$3,000**; ETH [[dvol|DVOL]] **58** (≈55th percentile); 30-day realized vol **48** → VRP = **10 vol points**. Put skew firm after a recent dip. 35 DTE. Bullish-to-neutral.

**Trade (per 1-ETH contract):**
- Sell 25Δ put @ **$2,700** for **$78**.
- Buy 10Δ put @ **$2,400** for **$30**.
- **Net credit = $48.** Width = $300. **Max loss = $300 − $48 = $252.** Credit/width = 16% → in practice tighten to a $200 wing or push the short to 28-30Δ to clear the 25% gate; shown as-is for the arithmetic.
- **Breakeven:** $2,700 − $48 = **$2,652.**

**Path A — base case (hold/grind up).** ETH drifts $2,900-$3,150 and DVOL eases to 52. The spread decays to ~$22; close at ~54% of credit for **+$26/contract**.

**Path B — tested, thesis intact.** ETH slips −6% to ~$2,820; the short put is threatened but the trend still looks up. Roll **down and out** to a $2,400/$2,150 spread 30 days later for a small net credit, lowering the danger zone.

**Path C — vol shock.** ETH gaps −18% overnight to ~$2,460; DVOL 58 → 108. **Kill triggers at the open.** Short $2,700 put deep ITM but the long $2,400 put caps the loss near the $252 floor. Net ≈ **−$240/contract** — the wing doing its job.

## Sources

- [[greeks-live]] / [[deribit]] documentation — [[dvol|DVOL]] index, IV surface and put skew, USDC (linear) vs inverse settlement, taker-fee premium cap, European 08:00 UTC cash settlement.
- Bondarenko (2014), "Why Are Put Options So Expensive?" and Carr & Wu (2009), "Variance Risk Premiums" — the put-skew and variance premia the short leg harvests (documented for equity indices; crypto's are larger and driven by the perp/liquidation complex).
- [[book-option-volatility-and-pricing]] — Natenberg on vertical credit spreads and gamma near expiry; mechanics port to crypto, re-scoped to Deribit's European cash-settled BTC/ETH options.

## Getting the Data (CryptoDataAPI)

[[dvol|DVOL]], the IV surface, and put skew come from **Deribit / [[greeks-live]]**, not CryptoDataAPI. [[cryptodataapi|CryptoDataAPI]] supplies the volatility-regime, funding, dealer-gamma, and options-flow context to time the spread and read the skew.

**Live:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal): the entry gate
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding; a funding flip signals the put-skew fattening that enriches the short put
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] strike (positioning context)
- `GET /api/v1/quant/gex` — dealer Gamma Exposure (pin vs cascade context near the short strike)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations, early warning for the down-gap that maxes the loss

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` — OHLCV for realized-vol vs DVOL
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — OHLCV history for backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=ETH"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]]. IV/DVOL/skew is Deribit / [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can gate and manage the spread with the endpoints above:

- **Entry gate** — `GET /api/v1/volatility/regime` must not read `vol_shock`; realized vol from `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=90` supplies the RV side of the DVOL−RV > 5 check (DVOL from Deribit)
- **Skew signal** — `GET /api/v1/derivatives/funding-rates?coin=ETH`: a funding flip after a selloff flags the put-skew fattening that makes the short put rich to sell — the page's specific edge
- **Bullish-thesis check** — `GET /api/v1/quant/market`: sustained strong_trend_bear probability contradicts the bullish tilt (the strategy's weakness is a persistent bear, not a single capped shock)
- **Down-gap warning** — `GET /api/v1/market-intelligence/liquidations` + `GET /api/v1/quant/gex` watch for the cascade that gaps through the long wing and maxes the loss
- **Backtest** — replay short-strike breach frequency on `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) with point-in-time regimes from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02)
- **Tips** — automate the one-roll-only rule: log rolls per position and hard-stop the second roll attempt

## Related

- [[credit-spread]] — the two-sided parent family (bull put + bear call)
- [[iron-condor]] — short put spread + short call spread combined (neutral)
- [[short-strangle]] — the undefined-risk sibling this improves on
- [[cash-secured-puts]] — the capital-intensive bullish-premium equivalent
- [[crypto-options-volatility-selling]] — the parent short-vol book
- [[deribit]], [[greeks-live]] — venue and analytics/RFQ workbench; DVOL and skew source
- [[dvol]], [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[funding-rate]], [[skew]] — the perp/skew linkage that gives the put side its specific edge
- [[variance-risk-premium]] — the premium harvested
- [[max-pain]], [[gamma-exposure]] — dealer-positioning context
- [[section-1256-contracts]] — the tax treatment crypto options do *not* get
- [[theta]], [[vega]], [[gamma]], [[delta]] — the Greeks that define the profile
- [[cryptodataapi]], [[cryptodataapi-market-intelligence]] — the data layer
