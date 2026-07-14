---
title: "Volatility Trading"
type: strategy
created: 2026-04-15
updated: 2026-07-14
status: good
tags: [options, derivatives, volatility, quantitative, crypto, bitcoin, ethereum]
aliases: ["Volatility Trading", "Vol Trading", "Volatility Strategies", "Crypto Vol Trading"]
related: ["[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[gamma-scalping]]", "[[crypto-options-volatility-selling]]", "[[short-volatility-strategies]]", "[[long-volatility-strategies]]", "[[volatility-carry]]", "[[variance-swap]]", "[[volatility-swap]]", "[[funding-rate]]", "[[options]]", "[[straddle]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
edge_source: [risk-bearing, behavioral]
edge_mechanism: "Crypto spot holders, leveraged perp longs, and lottery-ticket call buyers systematically overpay for convexity, so Deribit implied vol (DVOL) exceeds subsequently realized vol most of the time; disciplined sellers (and accurate vol forecasters) harvest that spread in exchange for bearing crypto's genuinely fatter tail."
data_required: [options-chain, dvol-history, realized-vol-calc, funding-rates, perp-open-interest]
min_capital_usd: 25000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 0.7
expected_max_drawdown: 0.45
breakeven_cost_bps: 60
decay_evidence: "BTC DVOL structurally declined from routine 70-90% readings in 2021 to 40-55% baselines through 2024-2025 as the options market deepened, ETF-driven spot ownership diluted the leveraged-long share, and covered-call ETFs plus on-chain option vaults industrialised systematic call-writing. The IV-RV spread compressed roughly in step, but crypto's crash frequency (2020-03, 2022 LUNA/FTX, 2025-10-10) keeps the tail-risk premium alive."
---

# Volatility Trading

Volatility trading encompasses a family of strategies that seek to profit from changes in the level of market volatility rather than from the direction of the underlying asset's price. In crypto this means trading the spread between [[implied-volatility]] — measured by [[dvol|DVOL]], Deribit's 30-day implied-volatility index for [[bitcoin|BTC]] and [[ethereum|ETH]] — and subsequently realized volatility, or taking directional views on whether vol itself will rise or fall. It is a core discipline in professional [[deribit|Deribit]] options trading and the backbone of most institutional crypto risk-management overlays. This page surveys the strategy family; the canonical rules, pseudocode, and example below are anchored on the most implementable variant — systematically harvesting the crypto [[variance-risk-premium|variance risk premium]] via delta-hedged short BTC/ETH options. For the dedicated, buildable version of that trade see [[crypto-options-volatility-selling]] and [[volatility-carry]].

## Overview

In most traditional trading, the profit or loss depends on whether an asset goes up or down. Volatility trading adds a second dimension: how much an asset moves, regardless of direction. A vol trader might profit from BTC that swings wildly between $58k and $70k even if it ends the month where it started, or from an asset that sits still if they bet on low volatility.

The foundation is the distinction between implied volatility (IV) — the market's forward-looking estimate of future price variation embedded in options prices — and realized volatility (RV) — the actual historical standard deviation of returns over a given period. When IV exceeds RV, options are "expensive" and selling premium tends to be profitable. When RV exceeds IV, options are "cheap" and buying premium tends to pay off. Professional vol traders systematically identify and exploit these mispricings.

The [[dvol|DVOL index]] is the crypto analogue of the equity [[vix|VIX]]: a model-free, variance-swap-style measure of 30-day forward implied vol on BTC and ETH, published by [[deribit|Deribit]] (which clears the large majority of crypto options volume). BTC DVOL has ranged from the high-20s in deep calm to 130+ during shocks; ETH DVOL typically prints a few points higher. Because the *level* drifts with regime, most systematic strategies gate on DVOL **percentile** over a trailing window (the crypto version of IV-rank) rather than the raw number.

## Edge source

Per the [[edge-taxonomy]], crypto volatility trading draws on two of the five edge categories:

- **Risk-bearing** (primary, for short-vol variants): the [[variance-risk-premium]] is compensation paid by hedgers to insurers. Selling BTC/ETH options is structurally similar to selling insurance — positive expected value in exchange for absorbing rare, large losses. This edge does not require outsmarting anyone; it requires surviving the tail, and crypto's tail is genuinely fatter than equities'.
- **Analytical** (primary, for vol-arb variants): the realized-vs-implied spread trade pays whoever forecasts realized vol more accurately than the market consensus embedded in DVOL and the [[volatility-surface|surface]]. Realized-vol estimators, funding/perp-positioning reads, and the crypto event calendar (halvings, unlocks, ETF flows, macro prints) give systematic forecasters a measurable edge.
- **Behavioral** (secondary): demand for lottery-like OTM calls ("100x to Valhalla") and crash-protective OTM puts is partly driven by fear and greed rather than fair value, steepening (or, in euphoric funding regimes, *inverting*) the [[skew-trading|skew]] beyond what realized outcomes justify.

## Why this edge exists

Implied vol on BTC/ETH options has exceeded subsequently realized vol the large majority of the time — the same [[variance-risk-premium]] documented for equities (Bakshi & Kapadia 2003; Carr & Wu 2009), but structurally *wider* on crypto because the perceived tail is larger. It persists because:

- **Who is on the other side**: leveraged perp longs and spot holders buying protective puts after every drawdown; retail buyers of lottery-ticket calls; treasuries and miners hedging known exposures. These flows are price-insensitive.
- **Why they keep losing** (in expectation): they are not trying to win — they are buying insurance, and insurance has negative expected value by design. The premium they overpay is rational (it truncates ruinous outcomes) and is income for the seller willing to warehouse tail risk.
- **Why it isn't arbitraged away**: harvesting the premium requires posting crypto/USDC collateral on an offshore venue and tolerating violent, concave drawdowns (2020-03, LUNA, FTX, 2025-10-10). The set of desks that can genuinely hold through a Black-Thursday-style spike is small, so the premium survives — though it has compressed as covered-call ETFs and on-chain vaults have scaled systematic option-selling supply.

## Crypto specifics

Everything above is the transferable theory. What makes crypto vol trading its own discipline:

- **DVOL, not VIX.** The benchmark is [[dvol|DVOL]] (BTC and ETH), read on percentile terms. There is no CBOE-style methodology monopoly — DVOL is a single-venue ([[deribit|Deribit]]) product mirrored by [[greeks-live|Greeks.live]].
- **24/7, no close.** Crypto never stops trading, so gap risk is *continuous*, not overnight — there is no market close to cap a move, and gamma runs hot through thin **weekend** and holiday liquidity. DVOL prices that weekend gamma explicitly.
- **Perp-funding sets the skew.** Unlike equities' near-permanent put skew (pension hedging), crypto skew oscillates with the perpetual-futures book: when [[funding-rate|funding]] is richly positive, 25-delta *call* skew can trade rich to puts — a "perp-heavy skew." A vol trader who reads funding and perp OI can lean into whichever wing the leveraged crowd overbid.
- **Inverse vs linear settlement.** Deribit lists coin-margined (**inverse**) options, where your collateral moves with spot (a quanto-like double hit), and USDC-margined (**linear**) options with clean USD P&L. Mismatching collateral to intended exposure is a silent killer.
- **Deribit is the market.** ~85-90%+ of crypto options OI clears on one venue. Single-venue outage, hack, or insolvency during a vol event is an existential, un-hedgeable risk with no deep second venue to roll into.
- **Majors only.** Liquid DVOL and options exist for BTC and ETH; most alts have thin-to-nonexistent options markets, so vol strategies are effectively capped to the two majors.
- **No §1256 shelter.** Offshore crypto options get **no** [[section-1256-contracts|§1256]] 60/40 treatment (ordinary rates in the US; income/CGT in AU by trader status) — the after-tax net is materially lower than the SPX version's.
- **Crypto vol-shock calendar.** The canonical kill events are **2020-03-12** (BTC −50% in 24h; pre-DVOL era), **2022-05 LUNA/UST** (weeks of RV > IV, 3AC contagion), **2022-11 FTX** (DVOL into the 90s-100s+), and **2025-10-10** (BTC −12% in ~60 seconds, ~$19B liquidated — the largest crypto liquidation cascade to date). See [[liquidation-cascade-fade]].

## Null hypothesis

Under no-edge conditions, DVOL would be an unbiased forecast of RV: the average IV-RV spread would be zero, delta-hedged short option positions would break even before costs and lose after Deribit's wider spreads, and a short-variance program would show profits in calm months exactly offset by spike losses. Concretely: if 30-day BTC implied vol averaged the same as subsequent 30-day realized vol over a multi-year sample, the strategy has no edge and any backtest profit is path luck. The null is rejected historically — the BTC IV-RV spread has averaged materially above zero and wider than the SPX 2-4 vol-point spread — but each implementation must re-test on its own market and era, because single-name alt "options" (where they exist at all) and short windows can show zero or negative premia after costs.

## Rules

Canonical variant: systematic short crypto variance risk premium on BTC/ETH options, delta-hedged on the perp.

**Entry**
- Compute DVOL (or ATM implied vol) and a realized-vol forecast (e.g., 20-30 day close-to-close / Parkinson estimator).
- Enter short premium only when **DVOL percentile is ~40th-90th** of its trailing year AND **DVOL minus forecast RV > 5 vol points** (crypto's healthy-premium threshold — wider than the SPX 2-point rule because both DVOL and RV run higher and noisier).
- Structure: sell a 21-45 DTE [[strangle]] or defined-risk [[iron-condor]] (strongly preferred in crypto given gap risk), delta-hedged on the Deribit perp at a band + funding-boundary schedule.
- Do NOT enter into an active vol shock (DVOL > ~90th percentile) or the day of a major scheduled catalyst (FOMC, CPI, large token unlock, ETF decision).

**Exit**
- Take profit at 50% of maximum premium collected, or
- Close/roll at 10-14 DTE to avoid the crypto gamma cliff (which accelerates faster than equities' because overnight gaps are unbounded and continuous), whichever comes first.
- Vol-shock kill: flatten immediately if **DVOL rises > 50% in a single session** or position delta exceeds 2× entry delta.

**Position sizing**
- Size by short vega: **≤ 1% of NAV per 1 vol point** of DVOL. Crypto DVOL can move 20-40 vol points in a session, so this cap is deliberately tighter than an equity book would run.
- Keep Deribit portfolio-margin utilisation ≤ 25% at entry to survive spike-driven margin expansion — the single most common way a crypto vol book gets force-liquidated at the worst tick.
- Never run undefined-risk short vol without a live long-vol overlay (deep-OTM BTC puts or DVOL-referenced convexity).

Long-vol and vol-arb variants invert the entry condition (buy premium / [[gamma-scalping|gamma scalp]] when forecast RV exceeds DVOL by a margin) — see Strategy Variants below.

## Implementation pseudocode

```python
# Daily / per-funding-boundary — Deribit BTC/ETH short-VRP core
dvol       = deribit_dvol(underlying)                 # BTC or ETH
dvol_pctl  = percentile_rank(dvol, lookback_days=365)
rv_forecast = realized_vol(klines(underlying), horizon=30)

spread = dvol - rv_forecast

if no_position:
    if 0.40 <= dvol_pctl <= 0.90 and spread >= 5.0 and not catalyst_within(days=1):
        legs = sell_strangle(dte=35, delta=0.16)      # or defined-risk iron condor
        premium = legs.credit
        size = vega_sized(max_vega_per_volpt=0.01)    # <=1% NAV per vol point
        open_position(legs, size)

else:
    delta_hedge_on_perp(target_delta=0)               # band + funding-boundary; pays/collects funding

    pnl = mark_to_market()
    if pnl >= 0.5 * premium:          close()         # profit take
    elif dte_remaining() <= 12:       close_or_roll() # crypto gamma cliff
    elif dvol_session_change >= 0.50: cut_all_short_vega()   # vol-shock kill
```

## Indicators / data used

- **[[dvol|DVOL]]** (BTC and ETH) — the 30-day forward IV index and primary entry gate; percentile-ranked. Live/historical from Deribit / [[greeks-live]].
- **[[volatility-surface|IV surface]] + 25-delta [[risk-reversal]]/butterfly** — strike and wing selection.
- **[[realized-volatility]]** (10/21/30-day, close-to-close and Parkinson) — computed from BTC/ETH klines; the RV in the IV-RV spread.
- **[[funding-rate]] + perp [[open-interest]]** — the crypto skew driver; deeply positive funding flags call-skew richness and a leveraged-long crowd.
- **[[max-pain]] and options OI by strike** — dealer-positioning context; large OI walls pin price into monthly expiries.
- **[[gamma-exposure|GEX]] / dealer gamma** — whether market makers are long or short gamma (spot dampened vs cascade-prone).
- **Event calendar** — halvings, token unlocks, ETF flow days, FOMC/CPI (crypto vol behaves discontinuously around these).

## Payoff & Greeks

Because volatility trading is a *family*, the payoff depends on the variant. The canonical short-VRP variant — a delta-hedged short BTC/ETH [[straddle]]/strangle — has a **concave** payoff: a tent that pays the collected premium in a quiet, pinned market and loses increasingly fast as the underlying moves away from the short strikes in either direction. Hedging on the perp flattens the linear (delta) exposure so the residual P&L is the [[gamma]]-vs-[[theta]] race: the position earns theta every quiet day and pays out gamma on every large realized move. Long-vol variants ([[gamma-scalping]], long BTC puts, long [[variance-swap|variance/vol swaps]]) invert this into a **convex** payoff.

Short delta-hedged strangle, P&L vs underlying move at expiry (delta neutralized):

```
   P&L
    |        _______________________            <- max gain ≈ net premium
    |       /                       \              collected (quiet market)
    |      /                         \
  0 +-----/---------- 0 move ---------\---------- underlying move
    |    /                             \
    |   /  (loss accelerates           \   <- concave: large move = large loss
    |  /     past the short strikes)     \
```

Net Greeks contrast — the two sides of the crypto vol-trading book:

| Greek | Short vol (delta-hedged short strangle) | Long vol (long straddle / [[gamma-scalping]]) |
|---|---|---|
| [[delta]] | Hedged to ~0 (re-hedged on the perp) | Hedged to ~0 (re-hedged to scalp) |
| [[gamma]] | **Short** — the killer; big moves lose disproportionately, and crypto gaps 24/7 | **Long** — big moves profit disproportionately |
| [[theta]] | **Positive** — the carry; earns time decay every calm day | **Negative** — bleeds time decay; must out-realize DVOL |
| [[vega]] | **Short** — a DVOL spike marks the book against you (FTX, 2025-10-10) | **Long** — profits when DVOL rises |

The short-vol trader is **short gamma, short vega, long theta** — paid to insure, exposed to the tail. The long-vol trader is the mirror image. The whole discipline is managing the gamma/theta/vega triangle: collect theta without being run over by gamma, and cap short-vega so a DVOL spike (see "What kills this strategy") cannot end the book.

## Example trade

2026-05 hypothetical, ETH vol premium harvest: ETH at $3,050; ETH DVOL 58 (63rd percentile of the trailing year); 30-day realized vol 44 — a 14-vol-point spread, above the 5-point crypto threshold, no macro catalyst inside 24h; ETH perp funding +0.03%/8h (mild call-skew richness). Sell the 35-DTE 15-delta iron condor on ETH (USDC-margined, linear): short 15-delta call @ $3,450 / short 15-delta put @ $2,650, protective 8-delta wings, net credit ≈ $70 per 1-ETH condor, max loss capped ~$180. Vega-size to 1%-NAV-per-vol-point; delta-hedge the residual on the ETH perp at a ±0.5% band. Over three weeks ETH oscillates $2,900-$3,200 and DVOL drifts to 50; the condor decays to ~$32 and is closed at 54% of credit for **+$38/condor**. Perp hedging roughly nets to zero (small funding collection on the short-delta hedge offsets slippage). The same position held through a 2025-10-10-style shock (ETH gapping −22%, DVOL 58 → 120) would have hit the vol-shock kill at the open, with the defined-risk long wings capping the loss near ~$180/condor — which is exactly why the structure is a condor, not a naked strangle.

## Performance characteristics

With realistic costs (Deribit taker fee 0.03% of underlying capped at 12.5% of premium; 3-8 vol-point round-trip bid-ask on 15-delta wings; perp-hedge slippage; funding on the hedge leg):

- **Expected Sharpe**: ~0.6-0.9 net for disciplined BTC/ETH VRP harvesting at modest size. Naive backtests that sell at mid and ignore hedging/funding costs show 1.5+; do not trust them. Vol-arb desks with superior forecasting and RFQ/block execution do better but require infrastructure.
- **Return profile**: strongly negatively skewed for short vol — many small gains, rare large losses. Monthly hit rates of ~70-80% with occasional months losing multiples of the average monthly gain. The gross premium is fatter than SPX (8-16 vol points avg IV-RV vs ~3-5) but also more volatile and more expensive to trade.
- **Cost sensitivity**: the strategy lives on the IV-RV spread; crypto's wider spreads and premium-capped fees push the breakeven cost budget to roughly double an SPX book's — it works on BTC/ETH and fails outright on illiquid alt chains.
- **Long-vol variants** are negative-carry: they bleed theta most months and pay off in spikes; expect a standalone negative Sharpe, justified only as portfolio insurance ([[long-vol-overlay]]).

### Behaviour by market regime

The single most important predictor of vol-trading P&L is the [[market-regime]]. The same short-VRP book swings from steady income to existential threat:

| Regime | Short-vol result | Long-vol result |
|---|---|---|
| Low, stable DVOL (contango vol term structure) | Steady theta income; best months | Bleed — negative carry |
| Choppy / mean-reverting vol | Mixed; depends on IV-RV spread sign | Occasional gamma-scalp gains |
| DVOL spike / crash (backwardation) | Catastrophic — the Black-Thursday / FTX / 2025-10-10 tail | The payoff regime — convexity monetizes |
| Post-spike normalization | Re-widened VRP; attractive re-entry | Theta resumes bleeding |

This regime-dependence is why a complete crypto vol book pairs a short-VRP engine (see [[crypto-options-volatility-selling]], [[short-volatility-strategies]]) with a permanent [[long-vol-overlay|long-vol overlay]] rather than running either alone.

## Capacity limits

Crypto options are a fraction of listed equity index options: the entire complex is ~$20-40B open interest, Deribit-dominated. Clean fills run to roughly $5-25M vega-notional on front-month BTC (ETH thinner) before you move the surface; a single disciplined book caps around **$50-300M** notional before roll impact dominates — hence `capacity_usd: 200000000` as a representative figure, one to two orders of magnitude smaller than an SPX vol book. Constraints arrive far earlier on alts, which have essentially no listed-vol depth. Note that the *aggregate* short-vol trade is less crowded than SPX vol (fewer capital-constrained sellers) but growing as covered-call ETFs and on-chain vaults scale — that supply compresses the call-side premium and amplifies squeeze risk.

## What kills this strategy

- **Volatility spike / gap risk**: the canonical killer. Crypto shocks are faster and larger than equities': BTC printed −50% in 24h on **2020-03-12** and −12% in ~60 seconds on **2025-10-10** (~$19B liquidated). Short-vol books that survive calm months can be destroyed in one session, and there is no market close to stop the bleed.
- **Crowding / deleveraging cascades**: when leveraged longs and short-vol sellers all need to cover into the same move, [[liquidation-cascade-fade|liquidation cascades]] drive DVOL higher — the crypto analogue of the Volmageddon feedback loop.
- **Premium compression**: growth of systematic call-writing (covered-call ETFs, on-chain option vaults) narrows the IV-RV spread until it no longer covers crypto's wide costs.
- **Coin-margined wrong-way risk**: on inverse options, collateral falls in USD terms exactly as a short put goes against you — a quanto-like double hit avoided only by using linear (USDC-margined) contracts.
- **Single-venue dependency**: a Deribit outage/hack/insolvency during a vol event is existential and un-hedgeable.
- **Discipline failure**: doubling down into a spike, or removing hedges to "save theta," converts a survivable drawdown into ruin. See [[failure-modes]].

## Kill criteria

Retire or suspend the program when any of the following holds:

- DVOL rises **> 50% in a single session** → flatten all short vega immediately.
- Drawdown exceeds **30%** of allocated capital → pause 30 days; **> 45%** is the modeled worst case (crypto tails are fatter than equities').
- Realized vol exceeds DVOL for **20+ consecutive days** → the structural premium has inverted; suspend.
- Trailing **6-month** average BTC/ETH IV-RV spread **< +3 vol points** (premium compressed below crypto costs — stand aside, re-enter if it normalizes).
- **Deribit portfolio-margin utilisation > 60%** intraday → cut size 50% regardless of P&L.
- Any Deribit auto-liquidation, socialised-loss, or unscheduled-outage event → flatten and stand down.

## Advantages

- **Non-directional**: profits regardless of whether crypto goes up or down.
- **Fatter structural premium than equities**: crypto IV-RV routinely runs 2-4× the SPX VRP, giving more room to absorb costs.
- **Skew is tradeable and readable**: the perp/funding link means the overbid wing is often observable in advance, unlike equities' near-static put skew.
- **Diversifying**: vol strategies have low correlation with directional/momentum crypto books and complement [[funding-rate-arbitrage]] carry.
- **Rich instrument ecosystem** on BTC/ETH: options, DVOL-referenced futures, OTC variance/vol swaps.

## Disadvantages

- **Genuinely fatter tail for short vol**: BTC/ETH gap further and faster than any equity index; a single shock can erase a year of carry.
- **No §1256 shelter**: crypto options get no 60/40 treatment; after-tax net is materially lower than the SPX version's.
- **Single-venue (Deribit) dependency** with no deep fallback.
- **Wide bid-ask and premium-capped fees** raise the cost floor well above SPX; majors only.
- **Coin-margined non-linearity** if you use inverse options.
- **Negative skew**: short-vol P&L is many small wins punctuated by rare large losses — psychologically and statistically treacherous.

## Strategy Variants

### Long Volatility Strategies

Long vol strategies profit when realized volatility exceeds implied volatility, or when DVOL itself rises. See [[long-volatility-strategies]].

**Buying Straddles and Strangles** — The simplest long vol trade is purchasing a [[straddle]] (call + put at the same strike) or [[strangle]] (OTM call + OTM put) on BTC/ETH. The trader pays a premium (theta cost) and profits if the underlying moves enough in either direction to overcome it. The retail-accessible way to go long crypto vol.

**Gamma Scalping** — A more sophisticated approach (see [[gamma-scalping]]): buy options and continuously delta-hedge on the perp, capturing realized moves. Profitable when realized vol > implied vol — crypto's 24/7 tape offers more scalping opportunities but also pays/collects funding on every hedge.

**Long BTC/ETH puts and DVOL convexity** — Deep-OTM Deribit puts (and, where used, DVOL-referenced structures) provide leveraged exposure to a vol spike. Primarily a tail-risk hedge rather than a profit center, since crypto convexity is expensive — see [[long-vol-overlay]].

**Long Variance / Volatility Swaps** — OTC contracts that pay the difference between realized variance (or vol) and a fixed strike. A pure bet on realized vol exceeding the strike. In crypto these are thin, dealer-quoted (via the Deribit block / Paradigm network), with Deribit's DVOL-referenced futures the nearest listed proxy. See [[variance-swap]] and [[volatility-swap]].

### Short Volatility Strategies

Short vol strategies profit when implied vol exceeds realized vol — which it does the large majority of the time on BTC/ETH. See [[short-volatility-strategies]] and [[crypto-options-volatility-selling]].

**Selling Premium** — Selling strangles, iron condors, or credit spreads collects upfront premium and profits when the underlying stays within a range. The risk is that a large move produces losses exceeding the premium collected, especially for naked positions — which in crypto means defined-risk condors are strongly preferred.

**Covered Calls and Cash-Secured Puts** — Selling options against existing spot or stablecoin ([[covered-calls]], cash-secured puts). Harvests the VRP more conservatively; industrialised in crypto by covered-call ETFs and on-chain option vaults, whose growing supply compresses the call-side premium.

**DVOL-referenced and vol-term-structure carry** — Selling forward vol via Deribit's DVOL futures or calendar structures exploits the tendency of the crypto vol term structure to sit in contango in calm regimes — the analogue of the old short-VIX-futures trade, and equally catastrophic in a spike.

### Volatility Arbitrage

Vol-arb strategies seek to profit from specific mispricings between implied and realized volatility without a net directional vol bet.

**Realized vs Implied Spread** — The classic vol arb: buy options when DVOL < expected RV, sell when DVOL > expected RV, and delta-hedge continuously on the perp. The edge comes from superior realized-vol forecasting.

**Term Structure Trades** — Exploit mispricings along the DVOL/vol term structure (front vs back expiry). See [[calendar-spread]].

**Skew and Dispersion Trades** — Trade the difference between implied vols at different strikes (the crypto skew, which flips call-heavy in euphoric funding), or between index and single-name (BTC/ETH) vol. See [[skew-trading]] and [[crypto-options-dispersion]].

## Instruments

| Instrument | Access | Notes |
|-----------|--------|-------|
| Deribit BTC/ETH options | Retail and institutional | The core; cash-settled to index, coin-margined (inverse) or USDC-margined (linear) |
| [[dvol|DVOL]] index | Data feed | The 30-day IV benchmark; percentile-gated |
| DVOL futures | Retail (Deribit) | Exchange-listed volatility futures settled on DVOL — nearest crypto analogue to a listed vol future |
| Variance / volatility swaps | Institutional (OTC) | Thin; dealer-quoted via block/Paradigm; see [[variance-swap]] / [[volatility-swap]] |
| Perp / dated futures | Retail and institutional | The delta-hedge leg; funding is paid/collected on the hedge |

## Key Concepts

- **Variance Risk Premium**: DVOL exceeds RV on average, compensating option sellers for bearing crypto's fat tail. The foundation of most short-vol strategies. See [[variance-risk-premium]].
- **Mean Reversion**: DVOL tends to revert to regime-dependent averages, making extreme percentile readings actionable.
- **Volatility Clustering**: high-vol periods follow high-vol periods; crypto vol trends in the short term even as it reverts over longer horizons.
- **Convexity**: long vol positions have convex payoffs (disproportionately more in large moves); short vol positions are concave (disproportionately more loss).
- **Perp-funding / skew linkage**: the crypto-specific fact that the options skew inherits the perpetual-futures book's positioning.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface are published by **Deribit** directly (and mirrored by [[greeks-live|Greeks.live]]) — CryptoDataAPI does **not** serve the DVOL index itself. [[cryptodataapi|CryptoDataAPI]] supplies the complementary volatility-regime, options-flow, dealer-gamma, and funding context.

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/quant/gex` — dealer gamma exposure (MM inventory + liquidation profile)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (the skew driver)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for RV backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog on [[cryptodataapi]]; for the DVOL index/history and full surface use the Deribit API or [[greeks-live]].

## Sources

- Bakshi, G. & Kapadia, N. (2003). "Delta-Hedged Gains and the Negative Market Volatility Risk Premium." *Review of Financial Studies* 16(2).
- Carr, P. & Wu, L. (2009). "Variance Risk Premiums." *Review of Financial Studies* 22(3).
- Sinclair, E. (2013). *Volatility Trading*, 2nd ed. Wiley (the foundational vol-trading mechanics; ports to crypto).
- Deribit / [[greeks-live]] documentation — DVOL construction, IV surface, coin-margined vs USDC-margined settlement, DVOL futures.
- Alexander & Imeraj, and Deribit Insights research on DVOL and the crypto variance risk premium.
- Crypto vol-shock record: 2020-03-12 Black Thursday, 2022-05 LUNA, 2022-11 FTX, 2025-10-10 liquidation cascade.

## Related

- [[dvol]] — the primary benchmark for crypto volatility
- [[deribit]] — the venue that clears and prices crypto options
- [[greeks-live]] — third-party crypto options analytics / IV surface
- [[implied-volatility]] / [[realized-volatility]] — the two measures whose gap is the edge
- [[crypto-options-volatility-selling]] — the buildable short-VRP strategy
- [[volatility-carry]] — the equity-index parent trade and its crypto framing
- [[short-volatility-strategies]] / [[long-volatility-strategies]] — the two sides of the family
- [[long-vol-overlay]] — the overlay that makes short vol survivable
- [[gamma-scalping]] — a core long-vol strategy
- [[variance-swap]] / [[volatility-swap]] — institutional pure-vol instruments
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[skew-trading]] / [[crypto-options-dispersion]] — surface and relative-value trades
- [[edge-taxonomy]] — where vol trading's edges fit
- [[failure-modes]] — general strategy failure catalog
- [[market-regime]] — vol behaves discontinuously across regimes
- [[theta]], [[vega]], [[delta]], [[gamma]] — the Greeks the strategy manages
