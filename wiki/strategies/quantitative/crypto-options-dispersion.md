---
title: "Crypto Options Dispersion"
type: strategy
created: 2026-07-14
updated: 2026-07-19
status: good
tags: [quantitative, options, volatility, correlation, derivatives, crypto, bitcoin, ethereum]
aliases: ["Crypto Dispersion Trade", "Implied Correlation Trade", "Crypto Correlation Dispersion", "BTC-ETH Dispersion", "Index vs Single-Name Vol"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: paper-traded

# Edge characterization
edge_source: [structural, behavioral, risk-bearing]
edge_mechanism: "Index-level (BTC/ETH major-basket) implied vol prices in a higher forward correlation than crypto's single names subsequently realize outside of risk-off crashes; you sell the richly-priced index/major vol and buy cheaper single-name vol, getting paid the implied-minus-realized correlation gap plus the mean-reversion of crypto correlation away from its crisis-time extreme of ~1."

# Data and infrastructure requirements
data_required: [options-chain, dvol-history, realized-vol-calc, realized-correlation-calc, cross-asset-price]
min_capital_usd: 50000
capacity_usd: 75000000
crowding_risk: low

# Performance expectations (net of spreads, slippage, and delta-hedge cost)
expected_sharpe: 0.8
expected_max_drawdown: 0.35
breakeven_cost_bps: 90

# Decay history
decay_evidence: "Crypto's single-name options liquidity has broadened only slowly beyond BTC/ETH: SOL options on Deribit remain an order of magnitude thinner, and most large-cap alts have no listed options at all, capping the trade's scalability. Implied-correlation richness has compressed as ETH/BTC vol-of-ratio products and structured desks arbitraged the most obvious BTC-ETH leg since 2023."

# Lifecycle (paper-traded)
capital_allocation: "paper sleeve, correlation-neutral, max 2 concurrent dispersion books"
kill_criteria: |
  - realized correlation regime-shifts to sustained ~1 (risk-off) for 15+ days
  - single-name (SOL/alt) option bid-ask exceeds 10 vol points (liquidity gone)
  - sleeve drawdown > 25%
  - Deribit outage or alt-option delisting breaking a leg
last_review: 2026-07-14
next_review: 2026-08-14

related: ["[[crypto-options-volatility-selling]]", "[[volatility-carry]]", "[[variance-risk-premium]]", "[[skew-trading]]", "[[short-strangle]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[correlation]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[deribit]]", "[[greeks-live]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[realized-volatility]]", "[[btc-dominance]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[crowding-risk]]", "[[cryptodataapi]]"]
---

# Crypto Options Dispersion

Crypto options dispersion is a **correlation trade**: sell the relatively rich implied volatility of the crypto "index" (a BTC/ETH major basket, or the dominant single name BTC used as the index proxy) and buy the relatively cheaper implied volatility of single-name constituents (ETH, and where liquid, SOL and a small set of large-cap alts). The position is vega- and delta-neutralised so the residual exposure is to **implied vs realized correlation**: it profits when crypto's cross-asset correlation *falls* (constituents move idiosyncratically, so realized index vol comes in below the implied that was sold), and loses when correlation spikes toward 1 — which is precisely what happens in a risk-off crash. It is the crypto adaptation of the classic equity dispersion trade (sell index vol, buy single-stock vol), heavily constrained by the shallow depth of listed crypto single-name options outside BTC and ETH.

This page is the relative-value cousin of [[crypto-options-volatility-selling]] (outright short vol). Here the *level* of vol is hedged out; the bet is purely on **correlation mean-reversion**.

## Edge Source

Per [[edge-taxonomy]], three edges combine:

- **Structural (primary).** Index/major implied vol embeds an **implied correlation** — the correlation the market prices among constituents. In crypto, the dominant BTC/ETH complex trades as if forward correlation is high (because in crashes it *is* ~1), so index-level implied vol is rich relative to the vol-weighted sum of single-name implied vols. Outside of crashes, realized correlation mean-reverts lower (0.5-0.8), so realized index vol comes in below what was sold. The dispersion trader captures the structural gap between priced-in and delivered correlation.
- **Behavioral.** The same convexity-overpayment that drives outright [[crypto-options-volatility-selling|vol selling]] is *unevenly distributed*: BTC/ETH options are the most liquid and most systematically bought (ETF hedgers, covered-call ETFs, the biggest lottery-ticket flow), so their implied vol carries the fattest premium, while thinner single-name options are under-traded and under-bid. Selling the over-loved leg and buying the neglected leg harvests that imbalance.
- **Risk-bearing.** The trade is short correlation, i.e. **short the crash** — correlation → 1 exactly when everything falls together. You are paid a premium to warehouse that "everything correlates in a panic" risk. Like all dispersion, it is a positive-carry, negatively-skewed position.

The edge is *not* informational or latency. Realized and implied correlation are computable by anyone with the [[volatility-surface|surfaces]] on [[greeks-live]]. The edge is the willingness and operational ability to run a multi-leg, delta- and vega-hedged book on a market where two of the legs (alt single-names) are semi-liquid.

## Why This Edge Exists

1. **Crypto correlation genuinely mean-reverts — from a high, crash-anchored base.** BTC-ETH 30-day realized correlation swings between ~0.5 in idiosyncratic-narrative regimes (an ETH-specific upgrade, a SOL ecosystem run) and ~0.95+ in macro risk-off. The market, scarred by crashes, prices forward correlation nearer the high end most of the time. When idiosyncratic regimes arrive, realized correlation undershoots the implied, and the short-correlation (dispersion) book prints.
2. **Liquidity asymmetry across the term-and-name structure.** BTC and ETH options are deep; SOL options on [[deribit]] exist but are an order of magnitude thinner; almost no other large-cap alt has listed options with a tradeable surface. This asymmetry means the *most-hedged, most-systematically-sold* names (BTC/ETH) carry the richest implied vol, creating the sell-index/buy-name spread — but it *also* caps capacity and makes execution the binding constraint.
3. **Structured-product and covered-call flow concentrates on the majors.** Covered-call ETFs and on-chain option vaults write BTC/ETH calls, depressing single-name-relative-to-index dynamics and reinforcing the richness of the index/major vol that dispersion sells.

## Null Hypothesis

Under no-edge conditions, **implied correlation ≈ subsequent realized correlation**, so a vega-neutral sell-index/buy-name book earns ~zero gross and, after the wide bid-ask on the thin single-name legs, a negative net. In that world:

- The implied-minus-realized correlation spread oscillates around zero with no persistence.
- Conditioning entry on high implied correlation would not improve forward P&L.
- The dispersion book's returns would be indistinguishable from noise plus a negative cost drift.

Empirically, in the BTC-ETH complex the implied-realized correlation spread has been positive on average outside crash windows — but the sample is short and dominated by a handful of correlation-spike events that erase multiple quarters of carry. **The null is emphatically not rejected during risk-off**: when correlation pins at 1 (2022 cascades, 2024-08-05 yen unwind, 2025-10-10), realized index vol *exceeds* the sold implied and the trade loses on both the correlation move and the vol-level gap. As with all dispersion, the strategy is long a small, steady coupon and short a rare, violent tail.

## Rules

### Entry

- **Index leg (sell vol):** short a delta-hedged straddle/strangle on the **index proxy** — either a BTC/ETH-weighted synthetic basket, or BTC itself used as the market proxy (BTC is ~50-60% of total crypto cap; its vol is the closest thing to "index vol").
- **Single-name legs (buy vol):** long delta-hedged straddles/strangles on **ETH** and, only when liquid, **SOL** and at most one or two other large-cap alts with a tradeable Deribit surface. Weight each name by its basket weight so the book is vega-neutral at inception.
- **Implied-correlation gate:** open only when **implied correlation (backed out from index vs single-name implied vols) is in the top ~30% of its trailing range** — i.e. the market is paying up for correlation. Do not initiate when implied correlation is already cheap.
- **Realized-correlation confirmation:** require **implied correlation − 30-day realized correlation > 0.10** (implied is meaningfully richer than what is currently delivering).
- **Tenor:** 21-45 DTE, matched across all legs to avoid a term-structure mismatch masquerading as a correlation bet.

### Sizing

- **Vega-neutral at inception:** Σ(single-name long vega, basket-weighted) ≈ short index vega. The residual is correlation exposure, not vol-level exposure.
- **Correlation exposure cap:** size so a move of realized correlation to 1.0 costs ≤ **12% of the sleeve** (the trade's defining tail; the cap is tight because the move is discrete and fast).
- **Leg-liquidity cap:** no single-name leg larger than **10% of that option's daily volume** — the binding constraint in crypto dispersion is almost always the alt leg's depth, not capital.
- **Max 2 concurrent dispersion books** to bound operational complexity (each book is 3-6 option legs plus perp hedges).

### Delta hedging

- Delta-hedge **every leg independently** with its own perp/future on a ±0.5%-NAV band. A dispersion book that is vega-neutral but delta-sloppy just becomes a basket of directional bets.
- Re-hedge mandatorily at each 8-hour funding boundary; switch to continuous hedging on any leg whose DVOL/IV jumps > 25% intraday.
- Budget the funding paid/collected on each hedge leg separately — the alt-perp hedge legs often carry richer (and more volatile) funding than BTC.

### Exit

- **Convergence target:** close when the implied-realized correlation spread compresses to near zero, or when realized correlation has fallen enough that the index short has decayed to **50% of its entry credit**.
- **Time stop:** 10-14 DTE (crypto gamma acceleration, same rationale as outright vol selling).
- **Correlation-spike kill:** flatten the whole book if 5-day realized correlation regime-shifts above ~0.95 and holds — the dispersion thesis has inverted (see Kill Criteria).

## Implementation Pseudocode

```python
# crypto_dispersion.py — sell index vol, buy single-name vol; net short correlation
# Status: paper-traded. Legs on Deribit; realized corr from cross-asset klines.

MIN_IMPLIED_CORR_PCTL = 0.70   # only when market pays up for correlation
MIN_IC_MINUS_RC       = 0.10   # implied corr richer than realized by >0.10
TARGET_DTE            = 35
CORR_SPIKE_KILL       = 0.95   # 5d realized corr regime-shift -> flatten
PROFIT_CONVERGE       = 0.50   # index short decayed to 50% of credit
TIME_STOP_DTE         = 12

def try_open(book, mkt):
    ic  = implied_correlation(mkt.index_iv, mkt.name_ivs, mkt.weights)
    rc  = realized_correlation(mkt.name_returns, window=30)
    if percentile(ic, mkt.ic_history) < MIN_IMPLIED_CORR_PCTL:
        return
    if (ic - rc) < MIN_IC_MINUS_RC:
        return
    exp = select_expiry(mkt.chain, TARGET_DTE)
    # SELL index vol (BTC proxy or BTC/ETH basket)
    idx_leg = sell_straddle("INDEX", exp, delta_hedge=True)
    # BUY single-name vol, basket-weighted, only where liquid
    name_legs = []
    for name, w in mkt.weights.items():
        if mkt.bidask_volpts[name] > 10:      # alt liquidity gate
            continue                           # skip illiquid leg
        name_legs.append(buy_straddle(name, exp, weight=w, delta_hedge=True))
    make_vega_neutral(idx_leg, name_legs)      # residual = correlation only
    book.add(idx_leg, name_legs)

def manage(book, mkt):
    if realized_correlation(mkt.name_returns, window=5) >= CORR_SPIKE_KILL:
        return flatten_all(book, "corr_spike_kill")
    for bk in book.dispersion_books:
        if bk.index_short_decay() >= PROFIT_CONVERGE:
            close(bk, "correlation_converged")
        elif bk.min_dte() <= TIME_STOP_DTE:
            close(bk, "time_stop")
        else:
            delta_hedge_all_legs(bk, mkt)      # each leg independently
```

## Indicators / Data Used

- **Implied correlation** — backed out from index (BTC / BTC-ETH basket) implied vol vs the basket-weighted single-name implied vols; the core signal. Surfaces from [[deribit]] via [[greeks-live]].
- **Realized correlation (5/30-day)** — computed from cross-asset returns (BTC, ETH, SOL...); the thing implied correlation is measured against.
- **[[deribit#DVOL Index — The "VIX of Crypto"|DVOL]] (BTC and ETH)** — index-level implied-vol reference and regime context.
- **Single-name [[volatility-surface|IV surfaces]] and bid-ask width** — the liquidity gate; alt option depth determines whether a leg is tradeable at all.
- **[[btc-dominance|BTC dominance]]** — a rising/falling dominance trend is a leading tell for whether crypto is entering an idiosyncratic (dispersion-friendly, alts decoupling) or a correlated (dispersion-hostile) regime.
- **[[funding-rate]] per leg** — cost of the perp delta-hedges and a positioning read on each name.
- **Cross-exchange liquidations** — correlation-spike early warning (everything liquidating together).

## Example Trade

**Setup (2026-04, BTC index vs ETH+SOL).** Crypto is in an idiosyncratic-narrative regime: ETH rallying on an upgrade, SOL on ecosystem flow, BTC range-bound. BTC-ETH 30-day realized correlation has fallen to **0.58**, but implied correlation backed out of the surfaces is **0.82** (top-quartile). IC − RC = **0.24** — a strong entry.

**Trade (35 DTE, vega-neutral):**
- **Sell** a delta-hedged BTC straddle (the index proxy) for ~$4,200 credit/BTC-notional.
- **Buy** delta-hedged ETH and SOL straddles, basket-weighted, for ~$3,900 combined debit.
- Net credit ~$300; residual exposure is short BTC-vs-(ETH,SOL) correlation. All three legs delta-hedged on their own perps.

**Path A — thesis works (~65%):** over 3 weeks ETH and SOL keep moving idiosyncratically while BTC chops. Realized index vol comes in *below* the sold BTC implied; realized correlation stays ~0.6. The BTC short straddle decays faster than the long name straddles bleed theta, and the correlation gap converges. Close at ~50% of index credit for a **net gain** roughly equal to the captured correlation spread minus costs.

**Path B — correlation drifts up (~25%):** a soft macro week pulls everything together, realized correlation rises to 0.85. The book marks slightly negative as the index short and the name longs move more in tandem. Close at time stop near breakeven-to-small-loss; no thesis break, just no payoff.

**Path C — risk-off correlation spike (~10%):** a macro shock (rate scare, exchange event) sends everything down together; 5-day realized correlation pins **> 0.95**. The **correlation-spike kill triggers**. The BTC index short you sold now realizes *more* vol than priced, and the name longs do not offset because everything fell in lockstep. Loss ≈ the sleeve's tail-cap (~12%). This is the dispersion tail — short correlation is short the crash.

## Performance Characteristics

Realistic, cost-corrected (paper-traded, short crypto sample — treat with caution):

| Metric | Estimate | Note |
|---|---|---|
| Gross correlation spread captured | 0.10-0.25 IC−RC in favourable regimes | Only BTC-ETH(-SOL); no broad basket exists |
| Net Sharpe | 0.6-0.9 | Dragged hard by the wide alt-leg spreads |
| Max drawdown | 25-35% | Correlation-spike events dominate |
| Hit rate | 60-70% | High-hit-rate, negative-skew, like all dispersion |
| Correlation to BTC | ~0 by construction, → negative in crashes | The trade *is* short crash-correlation |

**Cost overlay — the single-name legs dominate the friction budget:**

| Friction | Magnitude | Note |
|---|---|---|
| BTC/ETH option bid-ask | 3-8 vol points round-trip | Manageable (deep legs) |
| SOL / alt option bid-ask | 8-20+ vol points round-trip | The binding cost; often kills the trade before it starts |
| Deribit taker fee | 0.03% of underlying, capped 12.5% of premium | Paid on every leg — multiplied by 3-6 legs |
| Delta-hedge slippage (per leg) | 2-6 bps | Multiple hedges × multiple legs |
| Funding on hedge legs | ±5-20% APY, richer/noisier on alts | A real, asymmetric drag |

Because the trade has 3-6 option legs plus independent perp hedges, its `breakeven_cost_bps: 90` is the highest of the five crypto strategies here — nearly all of it in the thin alt legs. The trade is only worth doing when the implied-realized correlation gap is genuinely wide (top-quartile implied correlation, IC−RC > 0.10). In compressed-correlation regimes it is pure cost.

## Capacity Limits

Brutally capacity-constrained — the lowest-capacity of the five strategies here:

- The binding constraint is **single-name alt option depth**, not capital. SOL options on Deribit trade a fraction of ETH volume; beyond a small size the leg cannot be filled without moving the surface 10+ vol points.
- Practical operator capacity: roughly **$5-75M** notional, concentrated in the BTC-ETH leg with SOL as a minor satellite — reflected in `capacity_usd: 75000000`. Adding more names is impossible because there simply are no other liquid listed crypto single-name option surfaces.
- This is a **satellite / relative-value sleeve**, not a primary book. Its value is diversification (short correlation) against an outright short-vol or directional book, not standalone scale.

## What Kills This Strategy

Mapped to [[failure-modes]]:

1. **Correlation-spike / risk-off crash (Failure Mode #6: Tail Realised).** The dominant risk. When everything falls together, correlation → 1 and the short-correlation book loses on both the correlation move and the vol-level. 2022 (LUNA→FTX), 2024-08-05, and 2025-10-10 are the canonical cases.
2. **Single-name liquidity evaporation (Failure Mode #7: Operational Collapse).** In stress, the thin alt-option legs widen to un-tradeable spreads or stop quoting entirely — you cannot rebalance or exit the leg you need most. A structurally crypto-specific killer with no equity analogue.
3. **Regime change (Failure Mode #5).** A prolonged macro-correlated regime (crypto trading as one high-beta risk asset) removes the idiosyncratic moves the trade needs; the correlation gap stays closed for months.
4. **Delisting / venue concentration.** Deribit delisting or thinning an alt option series breaks a leg; single-venue dependency (Deribit for all listed crypto options) means an outage during a correlation event is un-hedgeable.
5. **Crowding on the BTC-ETH leg (Failure Mode #4).** The one liquid dispersion pair (BTC vs ETH) is the first place structured desks arbitrage the implied-correlation richness, compressing the most-tradeable version of the edge.

## Kill Criteria

Paused on any of:

1. **5-day realized correlation ≥ 0.95 and rising** → flatten all dispersion books immediately (thesis inverted).
2. **Any single-name leg's bid-ask > 10 vol points** → that book cannot be managed; close what remains tradeable and stand down.
3. **Sleeve drawdown > 25%** → pause 30 days; > 35% → retire.
4. **Implied − realized correlation spread negative on a 30-day average** → the structural premium has disappeared; suspend until it re-opens above +0.10.
5. **Deribit outage or alt-option delisting** breaking a leg → flatten.

Re-deploy: correlation regime back to mid-range, alt legs quoting inside 8 vol points, and top-quartile implied correlation with IC−RC > 0.10. See [[when-to-retire-a-strategy]].

## Advantages

- **Genuinely diversifying** — short correlation is close to orthogonal to outright vol selling and to directional books; adds a return stream that pays in *calm-but-dispersed* regimes.
- **Structural, well-understood mechanism** — dispersion is a mature equity-vol trade with decades of theory; the crypto version inherits the framework.
- **Low crowding** — outside the BTC-ETH leg, almost no one can run crypto dispersion because the single-name surfaces do not exist; the operator who *can* faces little competition.
- **Vega-neutral by construction** — insulated from the outright DVOL level that dominates [[crypto-options-volatility-selling]]; a cleaner correlation bet.
- **Cash-settled legs** — no physical assignment on Deribit.

## Disadvantages

- **Severe capacity and liquidity constraints** — the alt legs cap the trade at satellite size and can vanish exactly when needed.
- **Highest cost floor of the set** — 3-6 legs plus hedges, with the thin alt legs dominating (`breakeven_cost_bps: 90`).
- **Short-crash tail** — short correlation is short the crash; the payoff profile is negatively skewed like all dispersion.
- **No [[section-1256-contracts|§1256]] treatment** — offshore Deribit options; ordinary tax treatment, onerous multi-leg record-keeping.
- **Single-venue (Deribit) dependency** across every leg.
- **Short, regime-dominated sample** — crypto dispersion history is thin and dominated by a few correlation-spike events; parameter confidence is lower than for outright vol selling.
- **Operationally heavy** — many legs, many independent hedges, many funding streams to track.

## Sources

- [[greeks-live]] / [[deribit]] — BTC/ETH (and thin SOL) option surfaces, DVOL, block minimums; the practical source for implied vols and the liquidity reality of single-name crypto options.
- Equity dispersion literature (Driessen, Maenhout & Vilkov, "The Price of Correlation Risk", *Journal of Finance* 2009; and dealer-desk dispersion notes) — the framework the crypto version adapts; documents that index-implied correlation exceeds realized (the correlation risk premium).
- [[variance-risk-premium]], [[volatility-carry]], [[crypto-options-volatility-selling]] — the vol-selling context each leg lives inside.
- Regime/event record: 2022 LUNA/FTX, 2024-08-05 yen unwind, 2025-10-10 cascade — the correlation-spike kill cases (see [[liquidation-cascade-fade]]).

## Getting the Data (CryptoDataAPI)

Implied vols/surfaces and DVOL come from Deribit / [[greeks-live]]. [[cryptodataapi]] supplies the cross-asset price, realized-vol/correlation inputs, options-flow, and regime context.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]] (index-leg context)
- `GET /api/v1/volatility/regime` — per-asset vol regime for BTC/ETH/SOL (leg-by-leg regime read)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (correlation-spike early warning)
- `GET /api/v1/coins/top?limit=20` — constituent selection / basket weights by market cap
- `GET /api/v1/derivatives/funding-rates?coin=SOL` — hedge-leg funding per name

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=90` — OHLCV per name for realized-vol and realized-correlation computation
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/backtesting/klines` — deep multi-asset kline archive for correlation backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=90"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; per-asset vol regime on [[cryptodataapi]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the CDA-side half of this strategy end-to-end (implied vols stay on Deribit):

- **Compute** — pull `GET /api/v1/market-data/klines?symbol=...&interval=1d` per name (BTC/ETH/SOL) and compute 5/30-day realized correlation — the RC leg of the IC−RC entry gate; `GET /api/v1/coins/top?limit=20` sets basket weights
- **Regime gate** — `GET /api/v1/volatility/regime/score` plus `GET /api/v1/market-intelligence/liquidations` as the correlation-spike early warning; automate the flatten trigger on 5-day realized correlation ≥ 0.95
- **Hedge legs** — `GET /api/v1/derivatives/funding-rates?coin=SOL` per name to budget the perp delta-hedge carry on each leg separately
- **Backtest** — `GET /api/v1/backtesting/klines` gives multi-asset Binance spot 1h/4h/1d back to 2017-08 for realized-correlation regime studies (which regimes deliver dispersion vs correlation-pinning); implied-correlation history must come from Deribit
- **Tips** — `GET /api/v1/volatility/regime` classifies every leg's vol state in one batched call; `?format=markdown` keeps the multi-leg context compact in the agent's window

## Related

- [[crypto-options-volatility-selling]] — the outright short-vol cousin (this trade hedges the vol level out)
- [[volatility-carry]], [[variance-risk-premium]] — the vol-premium context each leg sits in
- [[skew-trading]] — adjacent vol-surface relative-value
- [[correlation]] — the variable being traded
- [[pairs-trading]], [[statistical-arbitrage]] — the relative-value strategy family
- [[short-strangle]] — the per-leg structure
- [[delta-hedging]], [[gamma-scalping]] — per-leg hedging
- [[deribit]] — the venue; the liquidity constraint lives here
- [[greeks-live]] — the multi-leg analytics workbench
- [[implied-volatility]], [[volatility-surface]], [[realized-volatility]] — the vol inputs
- [[btc-dominance]] — the idiosyncratic-vs-correlated regime tell
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]], [[crowding-risk]] — methodology
