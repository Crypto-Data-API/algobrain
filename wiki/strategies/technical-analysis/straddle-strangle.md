---
title: "Straddle & Strangle"
type: strategy
created: 2026-04-06
updated: 2026-10-17
status: good
tags: [options, crypto, volatility, straddle, strangle, event-driven, long-volatility, derivatives]
aliases: ["Long Straddle", "Long Strangle", "Buying Volatility", "Crypto Straddle", "BTC Straddle"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: intermediate
backtest_status: untested
related: ["[[straddle]]", "[[strangle]]", "[[short-straddle]]", "[[short-strangle]]", "[[iron-condor]]", "[[gamma-scalping]]", "[[delta-hedging]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-surface]]", "[[deribit]]", "[[greeks-live]]", "[[crypto-options-volatility-selling]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_deribit
    role: universe
    rule: "BTC or ETH options on Deribit; alt option chains are too wide and shallow"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "We do serve Deribit DVOL (current and about 180 days of daily history) and the ATM term structure for BTC and ETH, despite the page saying otherwise. Option quotes, the IV surface and fills come from Deribit."
  - id: catalyst_ahead
    role: entry
    rule: "Buy ahead of a discrete catalyst with uncertain direction: protocol upgrade or fork, spot-ETF decision, solvency or depeg scare, large unlock, FOMC or CPI, governance vote"
    runnable: partial
    endpoint: /api/v1/event/calendar?window_days=30
    field: items[].days_until
    note: "macro_print (FOMC, CPI and others), unlock and depeg rows are served with days_until. Upgrades, forks, ETF decisions, solvency scares and governance votes are not; the page sets no size for a 'large' unlock."
  - id: dvol_low_pctile
    role: entry
    rule: "DVOL below about the 40th percentile of its trailing year (implied vol cheap)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "Rank today's dvol against the served daily history, which is about 180 days (Pro Plus), not a year. The page calls this the single most important entry filter."
  - id: vol_regime_compressed
    role: entry
    rule: "Buy only from a compressed vol-regime read"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
  - id: vol_score_low
    role: filter
    rule: "A low market-wide vol-stress score flags cheap convexity"
    runnable: partial
    endpoint: /api/v1/volatility/regime/score
    field: composite_score
    replay: /api/v1/volatility/index/history?days=365
    replay_field: points[].composite_score
    note: "The page sets no cutoff for 'low'. The replay is one composite per UTC day."
  - id: realized_over_implied_view
    role: entry
    rule: "Expect realized vol over the holding period to exceed implied"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].vrp
    note: "vrp (dvol - realized_30) shows how implied compares with the last 30 days; whether future realized vol will exceed implied is a forecast."
  - id: not_into_elevated_dvol
    role: filter
    rule: "Avoid buying into an already-elevated DVOL right before the event; enter before the vol bid arrives"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol_change_24h
    note: "The page gives no threshold for 'elevated' or how early 'before' is."
  - id: structure_strikes
    role: entry
    rule: "Straddle: buy the ATM call and put at K close to spot. Strangle: buy about 25-delta OTM call and put"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].atm_iv
    note: "ATM is the listed strike nearest spot. No per-strike Greeks are served, so 25-delta strikes are a Black-Scholes approximation from atm_iv that ignores skew; premiums come from Deribit. The page names no tenor (the example is 30 DTE)."
  - id: dealers_short_gamma
    role: filter
    rule: "Short-gamma dealers amplify the move the straddle wants"
    runnable: partial
    endpoint: /api/v1/quant/gex?symbol={coin}
    field: coins.{coin}.regime.score
    note: "/quant/gex is a perp analog of dealer gamma (amplify at or above 0.35), not Deribit options GEX. The page uses it as context with no threshold."
  - id: take_profit_scale_out
    role: exit
    rule: "Scale out at 50-100% gain on the winning leg once a move develops"
    runnable: true
    input: position
    note: "Option marks come from the venue."
  - id: roll_before_final_weeks
    role: exit
    rule: "Roll up or out before the theta-heavy final 1-2 weeks if the thesis is intact but slow"
    runnable: true
    input: position
  - id: cut_on_iv_crush
    role: exit
    rule: "If the catalyst passes with a muted move and DVOL collapses, exit immediately"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "The catalyst date is on the calendar; 'muted' and 'collapses' have no thresholds (the example is DVOL 50 to 38 on a 2.5% move)."
  - id: gamma_scalp_hedge
    role: sizing
    rule: "Optional: delta-hedge on the perpetual and scalp gamma around the range; the hedge pays or collects funding"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=1
    field: current_rate
    note: "Position delta comes from the venue's Greeks; the page gives no rebalance band. Hyperliquid funding stands in for Deribit's perpetual."
  - id: risk_1_3pct
    role: sizing
    rule: "Risk at most 1-3% of the book per structure (the debit is the max loss)"
    runnable: true
    input: position
---

# Straddle & Strangle

## Overview

Straddles and strangles are **long-volatility** option structures that profit from a large move in either direction. A **long straddle** buys a [[call-option]] and a [[put-option]] at the **same strike** and expiration; a **long strangle** buys an OTM call and an OTM put at **different strikes** — cheaper, but needing a bigger move to pay off. Both are directionally agnostic: the buyer does not care *which* way [[bitcoin]] or [[ethereum]] goes, only that it moves *enough* to beat the combined premium plus [[theta]] decay. They are the canonical way to be **long gamma and long vega** into an uncertain, potentially explosive move.

In crypto these structures are traded almost entirely on [[deribit]] (BTC and ETH hold the overwhelming majority of listed-option open interest). The core bet is that realized volatility over the holding period will exceed the [[implied-volatility]] embedded in the premium — i.e. that Deribit's [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] index is *underpricing* the move. This is the buy-side mirror of [[crypto-options-volatility-selling]]: the straddle buyer pays the variance risk premium that the vol seller collects, and wins only when the tail actually arrives. The umbrella definition of the structure (long and short, straddle vs strangle vs butterfly) lives on [[straddle]]; this page is the tradeable **long-vol** playbook.

## Construction

**Long straddle** — one long ATM call + one long ATM put, same strike `K ≈ S` (spot), same expiry `T`:

- Buy 1 ATM call (strike `K`, delta ≈ +0.5)
- Buy 1 ATM put (strike `K`, delta ≈ −0.5)
- Debit = call premium + put premium. Because both legs are ATM, the debit ≈ the market's expected absolute move over `T` (the Black-Scholes ATM-straddle approximation).

**Long strangle** — one long OTM call + one long OTM put, different strikes:

- Buy 1 OTM call (strike `K_c > S`, e.g. 25-delta)
- Buy 1 OTM put (strike `K_p < S`, e.g. 25-delta)
- Debit is smaller (OTM legs are cheaper), but the two breakevens sit further apart.

On Deribit each BTC option contract represents **1 BTC** and each ETH contract **1 ETH**; options are **cash-settled to the Deribit index** at expiry (no physical delivery, no assignment mechanics). Premium on classic inverse contracts is quoted and paid **in the coin** (BTC/ETH); on the newer USDC-margined line it is quoted in **USDC** — see *Crypto specifics*.

| Choice | Straddle | Strangle |
|---|---|---|
| Strikes | Both at `K ≈ S` | Split OTM (`K_p < S < K_c`) |
| Premium | Higher (ATM is dearest) | Lower |
| Move needed to profit | Smaller | Larger |
| Max gamma | Higher, concentrated at `K` | Lower, spread across two strikes |

## Payoff & breakevens

Both structures have **defined risk (the debit) and undefined reward**. Payoff at expiry:

- **Long straddle**: `max(S_T − K, 0) + max(K − S_T, 0) − debit`
  - Upper breakeven = `K + debit`
  - Lower breakeven = `K − debit`
  - Max loss = `debit`, at `S_T = K` (both legs expire worthless)
  - Profit is a "V" that widens without bound as `S_T` runs away from `K` in either direction.
- **Long strangle**: pays nothing between `K_p` and `K_c`; loses the full debit if `S_T` lands in that band.
  - Upper breakeven = `K_c + debit`
  - Lower breakeven = `K_p − debit`
  - Max loss = `debit`, anywhere between the strikes.

Because crypto ATM implied vol is high (BTC DVOL commonly 40–60%, versus VIX in the teens), the **breakevens are wide in percentage terms** — a 30-day BTC straddle often needs a ~10–13% move just to break even. That is the central tension: crypto moves are large, but so is the premium you pay for them.

## Greeks profile

A long straddle/strangle is a stacked long-call + long-put, so the Greeks add:

| Greek | Long straddle / strangle | Comment |
|---|---|---|
| [[delta]] | ≈ 0 at inception | ATM call +0.5 offsets ATM put −0.5; strangle starts near-neutral too |
| Gamma | **Positive** (largest ATM) | The engine: gains accelerate as spot moves; concentrates into expiry |
| [[vega]] | **Positive** | Both legs gain if DVOL/IV rises — a DVOL spike alone can profit the position |
| [[theta]] | **Negative** | Both legs decay every day; the cost of waiting for the move |
| Rho | Small | Minor in crypto's typical tenors |

The position is **long gamma / long vega / short theta**. Two ways to win: (1) spot moves far enough (gamma monetized at expiry or via [[gamma-scalping]]), or (2) DVOL/IV expands while you hold (vega), letting you sell the structure back for more than you paid *before* any big move. The enemy is a quiet, range-bound tape where theta bleeds you and — worse — DVOL contracts (negative vega compounding the loss). See [[iv-crush]].

## Market view / when to use

Deploy a long straddle/strangle when you expect **realized vol to exceed implied**, especially:

- **Ahead of a discrete crypto catalyst** with uncertain direction: a major protocol upgrade or hard fork, a spot-ETF decision, an exchange-solvency or depeg scare, a large token unlock, a US [[fomc]] / CPI print (crypto trades macro), or a known on-chain governance vote.
- **When DVOL sits in the lower part of its range** (say < ~40th percentile of the trailing year) so implied vol is *cheap* and the [[volatility-regime|vol regime]] is "compressed" — coiled ranges that historically resolve violently. Buying vol when it is cheap is the structural counterpart to selling it when it is rich.
- **Straddle vs strangle choice**: straddle when you want maximum gamma concentration at a specific catalyst price and can afford the ATM premium; strangle when you want cheaper, wider exposure and believe the move will be *very* large (breakout out of a long consolidation).

Avoid buying into an already-elevated DVOL right before the event — the crowd has bid the premium up and the post-event [[iv-crush]] can sink the position even on a real move. The ideal entry is *before* the vol bid arrives.

## Adjustments & management

- **Profit-taking**: scale out at 50–100% on the winning leg once a move develops; do not wait for the theoretical max.
- **Leg out / roll to a directional stub**: after a decisive move, sell the profitable leg and either bank it or leave the near-worthless losing leg as a cheap lottery ticket. You can also roll the untested leg toward the money to lock gains.
- **Convert to a gamma scalp**: delta-hedge the residual delta with the Deribit **perpetual** (or dated future) and harvest [[gamma-scalping|gamma]] by trading the hedge around the range — turns a static long-vol bet into a dynamic one and offsets theta. Note the hedge leg pays/collects [[funding-rate|perp funding]].
- **Roll up/out** before the [[theta]]-heavy final 1–2 weeks if the thesis is intact but slow to play out (crypto gamma accelerates hard into expiry because gaps are unbounded and continuous).
- **Cut on IV crush**: if the catalyst passes with a muted move and DVOL collapses, exit immediately rather than nursing a double-decay (theta + falling vega).
- **Downgrade to defined-width**: converting a long strangle into a **reverse iron condor** (sell further-OTM wings) cheapens the structure at the cost of capping the reward — see [[reverse-iron-condor]].

## Crypto specifics

- **Venue & underlyings.** [[deribit]] is effectively "the market" for BTC and ETH options; liquid listed straddles/strangles beyond BTC/ETH are scarce. [[greeks-live]] is the standard workbench for building and monitoring the position (surface, per-leg Greeks, block tape).
- **Inverse vs linear settlement.** Classic Deribit BTC/ETH options are **inverse (coin-margined)**: premium and P&L are denominated in the coin, so your collateral itself moves with spot — a straddle bought with BTC collateral has an embedded currency effect on the payoff. Deribit's newer **USDC-margined (linear)** options give clean USD P&L. Choose linear when you want the straddle's payoff to be pure vol exposure; choose inverse only if the embedded coin delta is intended.
- **DVOL as the "cheap/rich" gauge.** [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] is Deribit's 30-day forward implied-vol index — the crypto VIX. Buy vol when DVOL is low in its own history; it is the single most important entry filter. **DVOL and the raw IV surface come from Deribit / [[greeks-live]], not from CryptoDataAPI** (CDA supplies the *complementary* regime, OI, GEX and funding context — see below).
- **24/7 and weekend gaps.** Crypto never closes, so there is no overnight-gap *cap* the way equities gap only at the open — but thin **weekend** liquidity produces sudden air-pockets that are pure gamma fuel for a long straddle. Continuous trading also means gamma keeps working through weekends and holidays when an equity straddle would sit dead.
- **No §1256.** Offshore Deribit options get **no [[section-1256-contracts|§1256]] 60/40 treatment**. In the US these are ordinary capital-gains events (short-term at full marginal rates); AU treatment is CGT/income depending on trader status. The after-tax math is worse than the SPX equivalent, and coin-margined P&L record-keeping is onerous.
- **Perp-funding interaction.** [[funding-rate|Perp funding]] shapes the option skew: richly positive funding (crowded leveraged longs) firms call skew and cheapens puts relative to calls, which nudges a directional lean into strangle strike selection and matters when you later delta-hedge on the perp.
- **Alt-option liquidity.** Options on SOL and other alts exist (Deribit, and thinner OKX/Bybit books) but bid-ask is wide and depth is shallow; long straddles on alts are best expressed on BTC/ETH or via perps, not illiquid alt option chains.

## Risks

- **[[iv-crush|IV/DVOL crush]]** after the catalyst — the dominant way a long straddle loses even on a real move.
- **Theta bleed** in a quiet, range-bound tape; every day without movement erodes both legs.
- **Wide bid-ask** on Deribit wings (several vol points round-trip) plus taker fees (0.03% of underlying, capped at 12.5% of premium) raise the breakeven move you actually need.
- **Timing risk**: too early bleeds theta; too late means peak IV and maximal cost.
- **Coin-margin non-linearity** on inverse contracts — collateral and payoff both move with spot.
- **Low base-rate hit rate**: most events resolve smaller than implied, so the majority of individual straddles lose; the strategy relies on the occasional large winner and disciplined sizing (risk ≤ 1–3% of book per structure).

## Worked crypto example

**Setup (BTC, 30 DTE).** BTC spot **$60,000**. DVOL **50** and sitting in the lower third of its trailing-year range (a "compressed" [[volatility-regime|vol regime]]); a spot-ETF options-listing decision and a US CPI print both land inside the next month. Direction genuinely unclear.

**Trade — long straddle (USDC-margined, linear):**
- Buy 1 BTC 60,000 call ≈ **$3,450**
- Buy 1 BTC 60,000 put ≈ **$3,450**
- Debit ≈ **$6,900** per 1-BTC straddle (≈ 11.5% of spot)
- Breakevens: **$53,100** and **$66,900**; max loss = $6,900 at $60,000.

**Path A — big move (the win).** ETF headline hits; BTC gaps to **$70,000** over a week. The call is worth ≈ $10,300, the put ≈ $0. Structure ≈ $10,300, profit ≈ **+$3,400 (+49%)**. Had DVOL *also* spiked, the call's remaining extrinsic would add to the mark. Alternatively, delta-hedging on the Deribit perp along the way would have gamma-scalped extra P&L out of the swing.

**Path B — muted move + IV crush (the common loss).** Both events pass, BTC drifts to **$61,500**, and DVOL crushes from 50 → 38. The call is worth ≈ $2,300, the put ≈ $900 → structure ≈ $3,200. Loss ≈ **−$3,700 (−54%)**: the small move and the vega hit together. This is the modal outcome and why sizing is 1–3% of book.

**Path C — long strangle variant.** The same view via a 25-delta strangle (buy 66,000 call + 54,000 put) costs ≈ **$3,800**, breakevens ≈ **$50,200 / $69,800** — cheaper to hold, but BTC must travel *further* before it pays.

## Getting the Data (CryptoDataAPI)

**IV and DVOL themselves come from Deribit / [[greeks-live]]** (the 30-day DVOL index and the raw IV surface are Deribit products; CDA does not serve them). [[cryptodataapi]] supplies the **complementary** context used to time and size a long-vol entry — the vol *regime*, options OI / max pain, dealer gamma, funding, and the catalyst calendar.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal); "compressed" flags cheap-vol setups to buy
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (pin/positioning context)
- `GET /api/v1/quant/gex` — [[gamma-exposure|Gamma Exposure]] (dealer inventory; short-gamma dealers amplify the move a straddle wants)
- `GET /api/v1/event/calendar` — forward catalyst calendar (unlocks / macro / listings) for timing the entry
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the skew driver

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for [[realized-volatility]] (compare RV to DVOL to judge whether vol is cheap)
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for RV backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the long-vol loop end-to-end (DVOL and the legs stay on Deribit / [[greeks-live]]):

- **Setup screen** — `GET /api/v1/volatility/regime` — buy only from a `compressed` read; a low `GET /api/v1/volatility/regime/score` flags cheap convexity market-wide.
- **Catalyst timing** — `GET /api/v1/event/calendar` — enter *before* the vol bid arrives for dated unlocks/macro/listings; the post-event IV crush is the modal loss path.
- **Amplifier check** — `GET /api/v1/quant/gex` — short-gamma dealers amplify exactly the move a straddle wants; `GET /api/v1/derivatives/funding-rates?coin=BTC` leans strangle strike selection toward the cheap wing.
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) for realized-move distributions after compression windows versus breakeven widths; `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) replays the compressed-regime flag point-in-time.
- **Tips** — automate the IV-crush exit: catalyst passed + muted move = cut immediately rather than nursing theta and falling vega.

## Related

- [[straddle]] — the conceptual umbrella (long vs short, definition, Greeks)
- [[strangle]] — the split-strike cousin covered here
- [[short-straddle]], [[short-strangle]] — the inverse (selling volatility)
- [[crypto-options-volatility-selling]] — the seller on the other side of this trade
- [[iron-condor]], [[reverse-iron-condor]] — defined-width relatives
- [[strip-strap]] — directionally biased straddle variants
- [[gut-spread]] — the ITM-strike equivalent
- [[gamma-scalping]], [[delta-hedging]] — how to monetize the long gamma
- [[implied-volatility]], [[realized-volatility]], [[volatility-surface]] — the vol inputs
- [[deribit]], [[greeks-live]] — venue and analytics; DVOL and surface source
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[funding-rate]] — the perp linkage that shapes crypto skew

## Sources

- Natenberg, *Option Volatility and Pricing* (2nd ed.) — straddle/strangle mechanics, the implied-vs-realized relationship, and gamma's role in long-volatility positions.
- McMillan, *Options as a Strategic Investment* (5th ed.) — straddle/strangle/butterfly construction and management.
- [[deribit]] / [[greeks-live]] documentation — DVOL construction, IV surface, cash settlement, inverse vs USDC-margined contracts.
