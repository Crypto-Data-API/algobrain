---
title: "Crypto Options Volatility Selling"
type: strategy
created: 2026-07-14
updated: 2026-07-19
status: good
tags: [quantitative, options, volatility, derivatives, crypto, bitcoin, ethereum, mean-reversion]
aliases: ["Crypto Short Vol", "Deribit Vol Selling", "BTC/ETH Premium Selling", "Crypto VRP Harvesting", "DVOL Volatility Selling"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: paper-traded

# Edge characterization
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Crypto spot holders, leveraged perp longs, and lottery-ticket call buyers persistently overpay for convexity; the vol seller underwrites that insurance and collects the spread between Deribit implied vol (DVOL) and subsequently realized vol — a variance risk premium that runs fatter than the S&P's because crypto's tail is genuinely fatter."

# Data and infrastructure requirements
data_required: [options-chain, dvol-history, realized-vol-calc, funding-rates, perp-open-interest, max-pain]
min_capital_usd: 25000
capacity_usd: 300000000
crowding_risk: medium

# Performance expectations (net of fees, spreads, and delta-hedge slippage)
expected_sharpe: 0.9
expected_max_drawdown: 0.45
breakeven_cost_bps: 60

# Decay history
decay_evidence: "BTC DVOL structurally declined from routine 70-90% readings in 2021 to 40-55% baselines through 2024-2025 as the options market deepened, ETF-driven spot ownership diluted the leveraged-long share, and covered-call ETFs plus on-chain vaults (Ribbon/Aevo, Deribit auction flow) industrialised systematic call-writing. The IV-RV spread has compressed roughly in step, but crypto's crash frequency (2020-03, 2022 LUNA/FTX, 2025-10-10) keeps the tail-risk premium alive."

# Lifecycle (paper-traded, not yet live)
capital_allocation: "paper sleeve, max 1% NAV short vega per vol point, max 4 laddered expiries"
kill_criteria: |
  - DVOL rises > 50% in a single session (vol-shock circuit breaker)
  - realized vol exceeds implied (DVOL) for 20+ consecutive days
  - sleeve drawdown > 30%
  - Deribit auto-liquidation / socialised-loss event on the venue
last_review: 2026-07-14
next_review: 2026-08-14

related: ["[[volatility-carry]]", "[[variance-risk-premium]]", "[[short-volatility-strategies]]", "[[options-premium-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[skew-trading]]", "[[risk-reversal]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[realized-volatility]]", "[[gamma-exposure]]", "[[section-1256-contracts]]", "[[tail-risk-hedging]]", "[[funding-rate]]", "[[crypto-options-dispersion]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[crowding-risk]]", "[[cryptodataapi]]"]
---

# Crypto Options Volatility Selling

Crypto options volatility selling is the systematic sale of [[bitcoin]] and [[ethereum]] options on [[deribit]] when implied volatility — measured by Deribit's [[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] index — trades persistently above the realized volatility that subsequently delivers. It is the crypto-native cousin of the S&P [[volatility-carry|vol carry]] trade, harvesting the same [[variance-risk-premium|variance risk premium (VRP)]], but on a market with a wider structural premium, coin-margined (inverse) settlement quirks, a skew shaped by the perpetual-futures book rather than by pension-fund hedging, and **no [[section-1256-contracts|§1256]] tax shelter**. Positions are DVOL-percentile-gated strangles and iron condors, sized by short vega, delta-hedged on a defined cadence, and protected by hard vol-shock kill switches calibrated to crypto's genuinely fatter tail (2020-03, LUNA, FTX, 2025-10-10).

This page covers the **canonical short-vol carry book on Deribit BTC/ETH**. The relative-value cousin — trading the *spread* between index and single-name implied vol — is [[crypto-options-dispersion]].

## Edge Source

Mapping to the six categories in [[edge-taxonomy]], crypto vol selling is a three-way hybrid, the same shape as equity [[volatility-carry]] but with a crypto-specific twist on each leg:

- **Behavioral (primary).** Crypto is the purest expression of convexity-preference. Retail buys OTM calls as lottery tickets ("100x to Valhalla"); leveraged spot holders buy protective puts after every crash, exactly when they are most expensive; and the entire market is trained by 80%+ drawdowns to overpay for downside insurance. The clearing price for that insurance is biased high — DVOL systematically prices in *more* realized volatility than arrives.
- **Structural.** The supply of vol sellers is small and capital-constrained. Deribit is offshore, requires crypto collateral, and the set of desks able and willing to warehouse crypto tail risk through a Black-Thursday-style event is tiny. Limited risk-bearing capacity keeps the premium elevated. Additionally, the option skew is *mechanically* linked to the [[perpetual-futures|perp]] market: when [[funding-rate|funding]] is richly positive (leveraged longs paying), call skew firms; the vol surface inherits the perp book's positioning rather than being set by hedgers.
- **Risk-bearing.** The seller is paid to underwrite the exact tail the buyer is fleeing. Crypto's tail is not a modelling artefact — BTC has printed −50% in 24 hours (2020-03-12) and −12% in 60 seconds (2025-10-10). The VRP is compensation for standing in front of that. Periods where the seller gives it all back (any of the named crashes) are the price of the premium, not evidence the edge is fake.

The trade does **not** rely on informational, analytical, or latency edge. DVOL and the full [[volatility-surface|surface]] are visible to anyone with a [[greeks-live]] login. The edge is operational: being able to warehouse short gamma at scale, hedge it, and survive the tail.

## Why This Edge Exists

Three reinforcing mechanisms keep BTC/ETH implied vol above realized:

1. **Insurance-demand asymmetry, amplified.** Crypto returns are more negatively skewed and far fatter-tailed than equities. Holders who have lived through multiple 80% drawdowns are structurally loss-averse and rationally overpay for downside protection. The VRP is the equilibrium price of that insurance — and because the perceived tail is larger, the equilibrium premium is larger. BTC DVOL frequently runs 50-80% while 30-day realized vol sits 35-55%; the resulting IV−RV spread is materially wider than [[vix|VIX]] minus S&P realized (Source: [[greeks-live]]; [[variance-risk-premium]]).
2. **Concentrated, capital-constrained supply.** Selling crypto vol requires posting crypto (or USDC) collateral on an offshore venue, tolerating coin-margined P&L non-linearity, and surviving margin spirals during 100%+ DVOL spikes. The agents who can do this are few; their required return is high; the premium is their compensation. This is the [[crowding-risk|crowding]] argument run in reverse — crypto vol is *less* crowded than SPX vol, which is part of why the raw premium is fatter (and also why it is more fragile).
3. **The perp book sets the skew.** Unlike equities, where persistent put skew reflects hedging demand, crypto skew oscillates: in leveraged bull runs, [[funding-rate|funding]] is deeply positive and 25-delta call skew can trade *rich to puts* — a "perpetual-heavy skew" where the options surface mirrors the crowded long-perp positioning. A vol seller who reads funding and perp OI can lean into whichever wing the leveraged crowd has overbid.

## Null Hypothesis

Under no-edge conditions, **DVOL ≈ subsequent realized vol** in expectation, so a delta-hedged short strangle earns ~zero gross and, after Deribit's wider bid-ask, delta-hedge slippage, and settlement frictions, a modestly negative net. In that world:

- The 30-day IV−RV spread would oscillate around zero with no persistence.
- DVOL percentile would carry no information about forward strangle P&L.
- Gamma-scalp P&L would offset theta exactly (IV correctly priced).
- Realized vol *after* a DVOL spike would not decay faster than before — no premium being paid down.

Empirically none of these hold across the 2019-2026 window: the BTC IV−RV spread is positive on average and persistent, DVOL percentile is a usable entry filter, and realized vol decays after DVOL spikes. **But** the null is *not* rejected during regime-break crashes — when a crash is the opening move of a new bear (LUNA, FTX), realized vol overshoots implied and stays there for weeks. The strategy earns the premium in the 85-90% of the time that is "normal-to-elevated-but-stable" and hands large chunks back in the 10-15% that is "crash." Distinguishing the two ex ante is the open problem — which is why the kill switches, not the entry signal, are the load-bearing part of the design.

## Rules

### Entry

- **Venue / underlyings:** [[deribit]] BTC and ETH options (Deribit holds the overwhelming majority of crypto options open interest; it is effectively "the market"). Use USDC-margined (linear) options where the trade needs clean USD P&L; use coin-margined (inverse) options only when the embedded crypto delta is intended (see *Inverse vs linear settlement* below).
- **Structure:** short ~15-25 delta [[short-strangle|strangle]] or defined-risk [[iron-condor]]. Iron condors cap the tail per position — strongly preferred over naked strangles in crypto given the gap risk.
- **Tenor:** 21-45 DTE at entry — the [[theta]]-rich zone. Avoid weeklies (gamma too hot for the gap profile) and avoid > 60 DTE (vega exposure to a DVOL regime shift dominates).
- **DVOL regime gate (the core filter):** open new short vol **only** when DVOL is between roughly the **40th and 90th percentile** of its trailing 1-year distribution. Below ~40th percentile the premium is too thin to pay for the tail; above ~90th percentile you are likely selling into an active vol-shock (buying a falling knife of vega) — sit out or wait for the spike to roll over.
- **VRP confirmation:** require **DVOL − 30-day realized vol > 5 vol points** (crypto's healthy-premium threshold; wider than the 2-point SPX rule because both DVOL and RV are higher and noisier).
- **Skew selection:** read [[funding-rate|perp funding]] and 25-delta [[risk-reversal]]. When funding is richly positive and call skew is bid, weight the short toward the call wing; when puts are bid post-selloff, weight toward puts. Sell the wing the leveraged crowd has overpaid for.

### Sizing

- **Vega budget:** short vega ≤ **1% of NAV per 1 vol point** of DVOL (a 10-vol DVOL spike costs ≤ ~10% of NAV before hedging). Crypto DVOL can move 20-40 vol points in a session, so this cap is deliberately tighter than an equity book would run.
- **Per-expiry cap and laddering:** ≤ 4 laddered expiries; no single expiry > 40% of total short vega. Avoids concentrating the book in one roll cycle or one event window (CPI, FOMC, halving, major unlock).
- **Margin headroom:** keep initial margin utilisation ≤ 25% of Deribit portfolio margin — spike-driven margin expansion is the single most common way a crypto vol book gets force-liquidated at the worst tick.

### Delta hedging cadence

- Hedge with the Deribit **perpetual** (or dated future) on a **band + schedule** rule: re-hedge whenever net position delta drifts beyond **±0.5% of NAV-equivalent notional**, and mandatorily at least once per 8-hour funding boundary.
- On vol-shock days (DVOL +25% intraday) switch to **continuous** hedging — the gamma is largest exactly when you can least afford unhedged delta.
- Hedging on the perp means paying/collecting [[funding-rate|funding]] on the hedge leg: budget it. In a positive-funding regime a short-delta hedge *collects* funding (a tailwind); in negative funding it is a drag.

### Exit

Three triggers, whichever fires first:

1. **Profit target:** close at **50% of max credit** (the tastytrade-standard rule ports directly; it balances hit rate against duration risk).
2. **Time stop:** close at **10-14 DTE** — crypto gamma accelerates faster into expiry than equity gamma because overnight gaps are unbounded and continuous (no market close to cap the move).
3. **Vol-shock kill:** close immediately if DVOL rises **> 50% in a session** OR position delta exceeds **2× entry delta**. This is the explicit tail circuit-breaker (see Kill Criteria).

## Implementation Pseudocode

```python
# crypto_vol_sell.py — Deribit BTC/ETH short-vol book
# Status: paper-traded reference. DVOL from Deribit; RV computed from klines.

MIN_DVOL_PCTL   = 0.40   # don't sell below 40th percentile (premium too thin)
MAX_DVOL_PCTL   = 0.90   # don't sell above 90th (likely into a vol shock)
MIN_VRP_POINTS  = 5.0    # DVOL - RV30 must exceed 5 vol points
TARGET_DTE      = 35
SHORT_DELTA     = 0.20   # ~20-delta wings
VEGA_PER_VOLPT  = 0.01   # <=1% NAV short vega per vol point
DELTA_BAND      = 0.005  # re-hedge at +/-0.5% NAV-equiv delta
PROFIT_TARGET   = 0.50   # close at 50% of max credit
TIME_STOP_DTE   = 12
DVOL_SHOCK_KILL = 0.50   # +50% DVOL in a session -> flatten

def manage_book(book, mkt):
    # ---- kill switch first ----
    if mkt.dvol_session_change >= DVOL_SHOCK_KILL:
        return flatten_all(book, reason="dvol_shock_kill")

    for pos in book.positions:
        if pos.pnl >= PROFIT_TARGET * pos.max_credit:
            close(pos, "50pct_profit"); continue
        if pos.dte <= TIME_STOP_DTE:
            close(pos, "time_stop"); continue
        if abs(pos.delta) >= 2 * pos.entry_delta:
            close(pos, "delta_2x_kill"); continue

    # ---- delta hedge (band + funding-boundary schedule) ----
    net_delta = book.net_delta()
    if abs(net_delta) > DELTA_BAND * book.nav or mkt.funding_boundary:
        hedge_with_perp(book, target_delta=0.0)   # collects/pays funding

def try_open(book, mkt):
    if not (MIN_DVOL_PCTL <= mkt.dvol_pctl <= MAX_DVOL_PCTL):
        return
    if (mkt.dvol - mkt.rv30) < MIN_VRP_POINTS:
        return
    if book.short_vega_per_volpt() >= VEGA_PER_VOLPT * book.nav:
        return
    exp = select_expiry(mkt.chain, TARGET_DTE)
    # skew-aware: overweight the wing the perp crowd overbid
    call_k = strike_at_delta(exp, +SHORT_DELTA)
    put_k  = strike_at_delta(exp, -SHORT_DELTA)
    wing   = "call" if mkt.funding_8h > 0.0003 else "balanced"
    # defined-risk iron condor: buy 10-delta protective wings
    sell_iron_condor(exp, call_k, put_k, protect_delta=0.10,
                     skew_tilt=wing, size=vega_sized(book, exp))
```

## Indicators / Data Used

- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]]** (BTC and ETH) — the 30-day forward IV index; the primary entry gate. Pull live and historical from Deribit / [[greeks-live]].
- **[[volatility-surface|IV surface]] + 25-delta [[risk-reversal]]/butterfly** — for strike and wing selection. [[greeks-live]] is the purpose-built workbench for this (surface heatmap, position Greeks, block-trade tape).
- **[[realized-volatility]] (10/21/30-day, close-to-close and Parkinson)** — computed from BTC/ETH klines; the RV in the IV−RV spread.
- **[[funding-rate]] + perp [[open-interest]]** — the skew driver; deeply positive funding flags call-skew richness and a leveraged-long crowd.
- **[[max-pain]] and options OI by strike** — dealer-positioning context; large OI walls pin price into monthly expiries.
- **[[gamma-exposure|GEX]] / dealer gamma** — whether market makers are long or short gamma tells you if spot will be dampened (long-gamma dealers) or amplified (short-gamma dealers, cascade-prone).
- **Cross-exchange liquidations** — an early-warning tape for the vol shock that triggers the kill switch.

Note: DVOL and the raw surface are Deribit products, surfaced through [[greeks-live]] and Deribit's own API; [[cryptodataapi]] provides the complementary options OI/max-pain, volatility-regime, GEX, and funding series (see *Getting the Data* below).

## Example Trade

**Setup (2026-05, ETH).** ETH spot $3,050. ETH DVOL at 58 (63rd percentile of trailing year). 30-day realized vol 44. VRP = 58 − 44 = **14 vol points** — a healthy entry. Funding on the ETH perp is +0.03%/8h (moderately positive → mild call-skew richness).

**Trade:** sell a 35-DTE iron condor on ETH (USDC-margined, linear):
- Short 15-delta call @ $3,450, long 8-delta call @ $3,700 (protective wing).
- Short 15-delta put @ $2,650, long 8-delta put @ $2,450 (protective wing).
- Net credit ≈ $70 per 1-ETH condor; max loss capped at ~$180 by the long wings.
- Size to 1%-NAV-per-vol-point vega; delta-hedge the residual with ETH perp at the ±0.5% band.

**Path A — base case (~70% historical):** over 3 weeks ETH oscillates $2,900-$3,200, DVOL drifts to 50. Condor decays to ~$32; close at 54% of credit for **+$38/condor**. Delta hedging on the perp roughly nets to zero (small funding collection on the short-delta hedge offsets hedge slippage).

**Path B — moderate spike (~22%):** a macro headline pushes ETH −6% and DVOL from 58 → 74 (+28%, below the 50% kill). The put wing goes ITM-ward; delta hedging kicks to continuous. Position marks −$45. Vol reverts over the next week, ETH recovers, close at 12 DTE time stop for **+$18/condor** (the protective long put capped the drawdown and the gamma scalp on the hedge clawed some back).

**Path C — Black-Thursday-style shock (~8%):** ETH gaps −22% overnight, DVOL 58 → 120 (+107%). **Vol-shock kill triggers at the open.** The condor's short put is deep ITM but the long put wing caps the loss at ~$180/condor; the delta hedge, if it filled, offset part of the spot move. Net loss ~−$150/condor (≈ the sleeve's monthly carry). This is the trade the whole risk framework exists to survive — and the reason the structure is a *defined-risk condor*, not a naked strangle, in crypto.

## Performance Characteristics

Realistic, cost-corrected picture (2023-2026 regime, paper-traded):

| Metric | Estimate | Note |
|---|---|---|
| Gross VRP captured | 8-16 vol points avg IV−RV | Fatter than SPX's ~3-5; also more volatile |
| Net Sharpe | 0.8-1.1 | Below the raw-premium implication after crypto-sized costs and tails |
| Max drawdown (realistic) | 35-45% | Concentrated in named crashes; defined-risk wings cap per-position loss |
| Hit rate per trade (50% target) | 68-78% | High hit rate masking negative skew |
| Skewness | Strongly negative | The defining feature; cannot be engineered away |
| Correlation to BTC | Slightly positive normal, → +1 in crashes | The "wrong-way" correlation that *is* the premium |

**Cost overlay — this is not a naive backtest.** Crypto options are meaningfully more expensive to trade than SPX:

| Friction | Magnitude | Note |
|---|---|---|
| Deribit taker fee | 0.03% of underlying, **capped at 12.5% of option premium** | The 12.5%-of-premium cap dominates for OTM wings — a real drag on cheap options |
| Bid-ask on 15-delta wings | 3-8 vol points round-trip | Far wider than SPX; worst in the wings and near expiry |
| Delta-hedge slippage | 2-5 bps per hedge on BTC/ETH perp | Multiple hedges per position over 3 weeks |
| Funding on the hedge leg | ±5-15% APY on hedge notional | A tailwind in positive funding, a drag in negative |
| Settlement / assignment | Cash-settled to index; minimal pin risk | One genuine advantage over US single-stock options |

Netting these, a gross ~mid-teens-vol-point premium is whittled to a modest positive net in calm/normal regimes and goes sharply negative in stressed regimes — the **same distributional shape as [[volatility-carry]], shifted onto a fatter-tailed underlying**. Because the wings are wide, the breakeven cost budget (`breakeven_cost_bps: 60`) is roughly double an SPX book's.

## Capacity Limits

Bounded by Deribit's depth and the size the surface can absorb without moving:

- **Single expiry / single wing:** clean fills to roughly **$5-25M vega-notional** on front-month BTC; ETH thinner. Beyond that you move the surface against yourself and must work orders or use the [[greeks-live]]/Paradigm RFQ network.
- **Whole book:** an individual/small-fund operator caps around **$50-300M** notional before market impact on rolls dominates — reflected in `capacity_usd: 300000000`. This is one to two orders of magnitude smaller than an SPX vol book, because the entire crypto options market (~$20-40B OI, Deribit-dominated) is a fraction of listed US index options.
- **Systemic capacity** is set by how much long-vol demand exists to sell into. As covered-call ETFs and on-chain option vaults scale, systematic call-writing supply grows and compresses the call-side premium — the crypto analogue of the equity vol-crowding dynamic.

## What Kills This Strategy

Mapped to [[failure-modes]]:

1. **Vol-of-vol expansion / Black-Thursday shock (Failure Mode #6: Tail Realised).** DVOL jumping 50-100%+ in hours. The canonical cases: **2020-03-12** (BTC −50% in 24h; IV exploded before DVOL existed), **2022-05 LUNA** (weeks of RV > IV), **2022-11 FTX** (DVOL spiked into the 90s-100s+), and **2025-10-10** (BTC −12% in 60 seconds, ~$19B liquidated). Each is a short-vol book's worst day.
2. **Regime change in VRP (Failure Mode #5).** Persistent RV > IV for weeks — the strategy bleeds throughout. Happened across LUNA→3AC→FTX in 2022.
3. **Coin-margined settlement wrong-way risk (crypto-specific).** On inverse (BTC/ETH-collateralised) options, your *collateral* falls in USD terms exactly as a short put goes against you — a quanto-like double hit. Using USDC-margined (linear) options removes this, at the cost of tying up stablecoin collateral. Mismatching collateral to intended exposure is a silent killer.
4. **Margin spiral / auto-liquidation (Failure Mode #7).** A DVOL spike multiplies Deribit portfolio-margin requirements; if you cannot top up, the venue force-closes at the worst prices. Deribit's liquidation engine is the crypto analogue of the broker-forced-liquidation risk that defines equity vol blow-ups.
5. **Single-venue concentration.** Deribit *is* the market. A Deribit outage, hack, or insolvency during a vol event is an existential, un-hedgeable risk — there is no deep second venue to roll into.
6. **Crowding on the call wing.** Systematic covered-call and vault flow compressing call-side premium (Failure Mode #4), degrading the fatter half of the historical edge.

## Kill Criteria

The sleeve is paused (not retired — the VRP mechanism persists) on any of:

1. **DVOL rises > 50% in a single session** → flatten all short vega immediately.
2. **Realized vol exceeds DVOL for 20+ consecutive days** → the structural premium has inverted; suspend.
3. **Sleeve drawdown > 30%** from peak → pause 30 days, re-parameterise; **> 40%** → retire and recapitalise.
4. **Deribit portfolio-margin utilisation > 60%** intraday → cut size 50% regardless of P&L.
5. **Any Deribit auto-liquidation, socialised-loss, or unscheduled-outage event** → flatten and stand down until resolved.
6. **Rolling 6-month Sharpe < 0** → pause and review whether crowding has structurally compressed the premium.

Re-deploy (un-kill): all clear, DVOL back inside the 40-90th percentile band, and 14-day IV−RV spread positive above 5 vol points. See [[when-to-retire-a-strategy]].

## Advantages

- **Fatter structural premium than equities.** Crypto IV−RV routinely runs 2-4× the SPX VRP, giving more room to absorb costs.
- **Cash-settled to index** — no physical assignment, minimal pin risk versus US single-stock options.
- **Skew is tradeable and readable.** The perp/funding link means the overbid wing is often *observable in advance*, unlike equities' near-static put skew.
- **Less crowded** than the SPX vol complex — fewer capital-constrained sellers means the seller who *can* warehouse the risk is better compensated.
- **Defined-risk expression available** (iron condors) with genuinely capped tail per position — essential and easy in crypto.
- **Non-directional**; diversifies a directional/momentum crypto book and complements [[funding-rate-arbitrage]] carry.

## Disadvantages

- **No [[section-1256-contracts|§1256]] shelter.** Unlike US broad-based index options (SPX) which enjoy the 60/40 blended rate and cash settlement, crypto options get **no §1256 treatment** — offshore Deribit contracts are ordinary capital-gains events (short-term at full marginal rates in the US; ordinary CGT / income treatment in AU depending on trader status). The after-tax net is materially lower than the SPX version's, and record-keeping across coin-margined P&L is onerous.
- **Genuinely fatter tail.** BTC/ETH can gap further and faster than any equity index; a single shock can erase a year of carry.
- **Single-venue (Deribit) dependency** with no deep fallback.
- **Coin-margined non-linearity** if you use inverse options — collateral and payoff both move with spot.
- **Wide bid-ask and premium-capped fees** raise the cost floor well above SPX.
- **Negative skew is psychologically punishing** — smooth equity curve, then a cliff.
- **Margin expands exactly when liquidity vanishes** — the classic short-vol margin spiral, sharper in crypto.

## Sources

- [[greeks-live]] / [[deribit]] documentation — DVOL construction, IV surface, block minimums (25 BTC / 200 ETH), coin-margined vs USDC-margined (linear) option settlement.
- Bakshi & Kapadia (2003), Carr & Wu (2009), Bondarenko (2014) — foundational variance-risk-premium literature that ports to crypto (see [[variance-risk-premium]] and [[volatility-carry]] for full citations).
- Alexander & Imeraj, and Deribit Insights research on DVOL and the crypto variance risk premium — document BTC IV−RV spreads structurally wider than SPX's.
- tastytrade 25-delta strangle / 50%-profit / time-stop management studies — mechanics port directly; sizing and stops must be tightened for crypto tails.
- Regime/event record: 2020-03-12 Black Thursday, 2022-05 LUNA, 2022-11 FTX, 2025-10-10 liquidation cascade — the canonical vol-shock kill cases (cross-referenced on [[liquidation-cascade-fade]] and the wiki history pages).

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from Deribit / [[greeks-live]]. [[cryptodataapi]] supplies the complementary options-flow, volatility-regime, dealer-gamma, and funding context used for gating and hedging.

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
- `GET /api/v1/backtesting/klines` — deep kline archive for RV backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the gating, hedging, and kill-switch layers of this book (DVOL and the surface stay on Deribit):

- **Signal context** — `GET /api/v1/market-intelligence/options` for BTC options OI/volume/max-pain; compute the RV side of the IV−RV gate from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`
- **Skew read** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (richly positive funding → call wing overbid) plus `GET /api/v1/quant/gex` for dealer-gamma/liquidation-profile context before choosing which wing to sell
- **Regime gate** — `GET /api/v1/volatility/regime`: open new short vega only in `normal`/`mean_reverting`; treat `vol_shock`/`expanding` as an automatic stand-down, and wire `GET /api/v1/market-intelligence/liquidations` as the cascade early warning ahead of the DVOL +50% kill
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/1d to 2017-08) rebuilds the realized-vol series for multi-cycle IV−RV studies; pair with point-in-time context from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid [[lookahead-bias]] in regime-conditioned entries
- **Tips** — run the vol-shock kill as an agent-side circuit breaker checked every refresh, not a daily job; `/volatility/regime/{symbol}` keeps a 60-day state history for validating the 40th-90th percentile DVOL gate against regime persistence

## Related

- [[volatility-carry]] — the equity-index parent trade this is the crypto analogue of
- [[variance-risk-premium]] — the premium being harvested
- [[crypto-options-dispersion]] — the relative-value cousin (index vs single-name vol)
- [[short-volatility-strategies]], [[options-premium-selling]] — strategy family
- [[short-strangle]], [[iron-condor]] — the structures used
- [[delta-hedging]], [[gamma-scalping]] — hedging and its diagnostic
- [[skew-trading]], [[risk-reversal]] — wing-selection tools
- [[deribit]] — the venue; DVOL and surface source
- [[greeks-live]] — the analytics/RFQ workbench
- [[implied-volatility]], [[volatility-surface]], [[realized-volatility]] — the vol inputs
- [[gamma-exposure]] — dealer-gamma context
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get
- [[tail-risk-hedging]] — the buy-side counterpart paying the premium
- [[funding-rate]] — the perp linkage that shapes crypto skew
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]], [[crowding-risk]] — methodology
