---
title: "NNFX Crypto Daily System"
type: strategy
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [trend-following, technical-analysis, algorithmic, swing-trading, crypto, perpetual-futures, funding-rate, position-sizing, risk-management, indicators]
aliases: ["Crypto NNFX", "NNFX Crypto", "McGinley-STC-Vortex System"]
related: ["[[nnfx-method]]", "[[stonehill-forex]]", "[[stonehill-forex-nnfx]]", "[[mcginley-dynamic]]", "[[schaff-trend-cycle]]", "[[vortex-indicator]]", "[[choppiness-index]]", "[[waddah-attar-explosion]]", "[[atr]]", "[[atr-position-sizing]]", "[[turtle-trading]]", "[[supertrend]]", "[[trend-following]]", "[[funding-rate]]", "[[beta]]", "[[external-strategy-sources]]"]
strategy_type: algorithmic
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

# Edge characterization
edge_source: [behavioral, analytical]
edge_mechanism: "Behavioral: crypto trends persist because participants under-react to new directional information and then chase late, so a daily trend filter plus momentum trigger captures part of the move; the counterparties are range-faders and late entrants. Analytical: fixed-fractional ATR sizing with half-off-at-1-ATR management converts a modest-hit-rate trend signal into bounded losses and occasional large runners."

# Data and infrastructure requirements
data_required: [ohlcv-daily, funding-rates, event-calendar]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: medium

# Performance expectations (priors, not measured)
expected_sharpe: 0.5
expected_max_drawdown: 0.30
breakeven_cost_bps: 40

decay_evidence: "None measured. Generic daily trend-following in crypto is widely known and crowded; see [[failure-modes]]."

kill_criteria: |
  - equity drawdown > 25% from peak
  - rolling 12-month net Sharpe < 0 after at least 40 closed signals
  - average R per trade over last 30 signals < 0
  - funding cost exceeds 30% of gross runner profit over a rolling 6 months
---

# NNFX Crypto Daily System

A fully specified [[nnfx-method|NNFX]]-style trend system for liquid crypto perpetuals on the **00:00 UTC daily close**: [[mcginley-dynamic|McGinley Dynamic]] baseline, [[schaff-trend-cycle|Schaff Trend Cycle]] as C1, [[vortex-indicator|Vortex]] as C2, [[choppiness-index|Choppiness Index]] as the volatility filter, and C1-flip / baseline-cross exits, with 1.5% risk per signal split into two orders and a BTC-beta exposure cap. Indicator choices are drawn from roles profiled by [[stonehill-forex|Stonehill Forex]] (Source: [[stonehill-forex-nnfx]]); the configuration itself is this wiki's assembly and is **untested**.

## Edge source

**Behavioral** and **analytical** (see [[edge-taxonomy]]). The entry stack is a conventional trend-following filter; the durable contribution is the money-management frame — consistent risk, capped correlated exposure, and asymmetric trade management.

## Why this edge exists

Time-series momentum in crypto is documented at daily-to-weekly horizons (see [[trend-following]], [[time-series-momentum]]). Participants anchor on prior prices, react slowly to regime changes, and then chase; range-faders and short-dated option sellers take the other side of breakouts. The NNFX filters try to restrict entries to the early part of moves (1 x ATR band, 7-candle rule) and to trending conditions (CHOP gate), where that under-reaction is largest. Whether the specific indicators add anything over a plain moving-average filter is an open empirical question.

## Null hypothesis

Under no edge, entries are equivalent to random-direction entries in the baseline's direction: order 1 hits +1 x ATR before −2 x ATR roughly 2/3 of the time by random-walk arithmetic, order 2 is scratched at breakeven or stopped, and expectancy is ≈ 0 **before** costs and negative after fees and funding. Test by comparing against (a) the same money management with entries on random days in the baseline's direction and (b) a plain 20-day EMA cross; the stack must beat both net of costs.

## Rules

**Universe**: BTC, ETH, SOL, BNB, XRP perpetuals (Binance or [[hyperliquid|Hyperliquid]]); add others only if 30-day average daily volume > USD 200M.

**Schedule**: evaluate once per day on the **closed** 00:00 UTC candle; place orders within the first 15 minutes of the new candle.

**Components**
- ATR: [[atr|ATR]](14), Wilder smoothing
- Baseline: [[mcginley-dynamic]] (N = 14)
- C1: [[schaff-trend-cycle]] (fast 23, slow 50, cycle 10); signal = cross of 25 up / 75 down
- C2: [[vortex-indicator]] (14); agrees when VI+ > VI− (long) by at least 0.03
- Volatility filter: [[choppiness-index]] (14) < 55
- Exit: no dedicated exit indicator — runner exits on C1 opposite signal or close across the baseline (NNFX default)

**Entries** (per [[nnfx-method#Entry rules]])
1. *Standard*: C1 signals, close on the C1 side of the baseline and within 1.0 x ATR of it, C2 agrees, CHOP < 55.
2. *Baseline cross*: close crosses the baseline, C1 agrees and its last signal was < 7 candles ago, within 1.0 x ATR, C2 agrees, CHOP < 55.
3. *Pullback*: baseline signal but close > 1.0 x ATR away; enter next day only if the close returns within 1.0 x ATR with all filters agreeing.
4. *Continuation*: after a prior entry in the same direction with no baseline cross since, a new C1 signal with baseline and C2 agreeing (no ATR band, no CHOP gate).
5. *One-candle rule*: if C2 or CHOP fails on the trigger day, recheck once on the next close.
6. *Event veto*: no new entries within 24h before FOMC, US CPI, or a scheduled unlock/listing event for the asset.

**Exits**
- Stop: both orders at **2.0 x ATR** from entry (crypto widening of NNFX's 1.5 x).
- Order 1: take profit at **1.0 x ATR**.
- Order 2: on TP1 fill, stop to breakeven; once 2.5 x ATR in profit, trail at 2.0 x ATR, ratcheting every 0.5 x ATR.
- Close runner on C1 opposite signal or daily close across the baseline.

**Position sizing**
- Risk 1.5% of equity per signal: two orders at 0.75% each; qty per order = `0.0075 x equity / (2.0 x ATR)`.
- Beta cap: 60-day beta to BTC per asset; same-side beta-adjusted open risk ≤ 3%; total open risk ≤ 6%.
- Leverage only as needed to fit size; liquidation price must be > 3 x ATR from entry.

## Implementation pseudocode

```python
P = dict(atr=14, md=14, stc=(23, 50, 10), vi=14, vi_gap=0.03, chop=14, chop_max=55,
         band=1.0, stop=2.0, tp1=1.0, trail_arm=2.5, trail=2.0, step=0.5,
         risk_signal=0.015, beta_cap=0.03, total_cap=0.06)

def daily(sym, bars, book, events):
    a   = atr(bars, P["atr"])[-1]
    md  = mcginley(bars.close, P["md"])
    stc = schaff(bars.close, *P["stc"])          # 0..100
    vip, vim = vortex(bars, P["vi"])
    ch  = chop(bars, P["chop"])[-1]
    c   = bars.close[-1]
    c1_state = +1 if stc[-1] > 50 else -1
    c1_sig   = (+1 if stc[-2] <= 25 < stc[-1] else -1 if stc[-2] >= 75 > stc[-1] else 0)
    c2_state = (+1 if vip[-1] - vim[-1] >= P["vi_gap"] else
                -1 if vim[-1] - vip[-1] >= P["vi_gap"] else 0)
    base_side = +1 if c > md[-1] else -1
    in_band   = abs(c - md[-1]) <= P["band"] * a

    for t in book.open(sym):                                 # manage
        if c1_sig == -t.side or base_side == -t.side:
            book.close(t); continue
        if t.tp1_done: t.trail(a, P["trail_arm"], P["trail"], P["step"])

    if book.has(sym) and not continuation_ok(sym, md): return
    if events.high_impact_within(sym, hours=24): return

    side = entry_type(c1_sig, c1_state, base_side, in_band, bars_since(stc_signal), book, sym)
    if not side or c2_state != side: return
    if not book.is_continuation(sym) and ch >= P["chop_max"]:
        book.queue_retry(sym, bars=1); return                 # one-candle rule

    r = P["risk_signal"] / 2 * book.equity
    if book.beta_risk(side) + 2 * r * beta_btc(sym, 60) > P["beta_cap"] * book.equity: return
    if book.total_risk() + 2 * r > P["total_cap"] * book.equity: return
    q = r / (P["stop"] * a)
    book.market(sym, side, q, stop=P["stop"] * a, tp=P["tp1"] * a, tag="TP1")
    book.market(sym, side, q, stop=P["stop"] * a, tp=None,         tag="RUNNER")
```

## Indicators / data used

| Input | Use | CryptoDataAPI |
|---|---|---|
| Daily OHLCV (00:00 UTC) | All indicators | `GET /api/v1/market-data/klines`; archive `GET /api/v1/backtesting/klines` |
| Funding | Carry on runners | `GET /api/v1/derivatives/funding-rates`; archive `GET /api/v1/backtesting/funding` |
| Event calendar | Entry veto | `GET /api/v1/event/calendar` |
| Volatility regime | Optional shock veto | `GET /api/v1/volatility/regime/{symbol}` |

## Example trade

*Illustrative numbers, not a backtest.* Account USD 100,000. ETH closes at 3,000 on day T; ATR(14) = 120; McGinley at 2,920 (close is 0.67 x ATR above — inside the band). STC crosses up through 25 (C1 signal), VI+ − VI− = 0.06 (C2 agrees), CHOP = 48 (passes). BTC-beta of ETH = 1.2; no other open longs, so beta-adjusted risk 1.8% < 3%.
- Risk per order: USD 750; stop distance 2.0 x 120 = 240 → qty 3.125 ETH per order.
- Stop 2,760 on both; TP1 3,120.
- Day T+3: TP1 fills, +USD 375; runner stop to 3,000.
- Price reaches 3,300 (2.5 x ATR) → trail arms at 3,060; on T+15 STC falls through 75 at a close of 3,420 → runner exits for +USD 1,312.
- Net ≈ +USD 1,687 before fees and ~12 days of funding on 3.1 ETH (at 0.01%/8h ≈ USD 34).

## Performance characteristics

No backtest exists. Priors from generic NNFX practice and crypto trend-following: hit rate on order 1 around 55–65%, runner outcomes highly skewed, expectancy concentrated in a few trending months per year, long flat or negative stretches in ranges (2019, mid-2021, 2022-H2, parts of 2025). Stonehill's own indicator results are default-setting, 3-year, pre-cost figures and are not evidence for this configuration (Source: [[stonehill-forex-nnfx]]).

**Cost overlay** (must be applied before any claim): taker fees ~4–5 bps per side on majors, 5–15 bps slippage on alts at the daily open, and funding that historically averages positive for longs in bull markets (a drag on long runners, a credit on shorts). Daily frequency and ~20–40 signals per asset per year keep fee drag small; funding on runners is the larger cost. `breakeven_cost_bps: 40` is a prior.

## Capacity limits

Entries cluster at 00:00 UTC, when many daily systems act. For BTC/ETH, orders up to low single-digit USD millions per signal are absorbable with a short TWAP; for SOL/BNB/XRP roughly a few hundred thousand per signal. Estimated strategy capacity ~USD 20M before impact at the daily open dominates.

## What kills this strategy

From [[failure-modes]]:
- **Overfitting** — the stack was chosen from a large menu; any parameter tuning on the same data inflates results ([[overfitting-detection]]).
- **Regime** — prolonged ranges produce repeated 2 x ATR losses the CHOP gate does not fully block.
- **Crowding at the daily open** — slippage from synchronized daily-close systems.
- **Correlation spike** — in crashes all alts behave like 1.5 x BTC; the beta cap limits but does not remove this.
- **Funding regime** — sustained high positive funding erodes long runners.
- **Gap-like wicks** — liquidation cascades can blow through the 2 x ATR stop.

## Kill criteria

See frontmatter; retire or pause per [[when-to-retire-a-strategy]]: drawdown > 25%, rolling 12-month net Sharpe < 0 after 40+ signals, 30-signal average R < 0, or funding > 30% of gross runner profit over 6 months.

## Advantages

- Fully rule-based, once-a-day, easy to automate and audit.
- Every component is independently testable ([[nnfx-method#Testing an indicator in isolation]]).
- Bounded per-trade loss and explicit correlated-exposure control.
- Half-off-at-1-ATR smooths the equity curve relative to all-in trend systems.

## Disadvantages

- Many parameters across five indicators — high overfitting risk.
- TP1 at 1 x ATR caps half the position in the strongest trends.
- Daily-close execution concentrates slippage at 00:00 UTC.
- Untested; indicator choices rest on FX-centric, default-setting, pre-cost evidence.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1d&limit=200` — closed daily bars for all five indicators
- `GET /api/v1/derivatives/funding-rates` — current funding for runner carry
- `GET /api/v1/event/calendar` — catalysts for the 24h entry veto
- `GET /api/v1/volatility/regime/{symbol}` — optional volatility-shock veto

**Historical data:**
- `GET /api/v1/backtesting/klines` — daily archive since 2020 for the full backtest
- `GET /api/v1/backtesting/funding` — historical funding to charge runners
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time universe (volume filter as of each date)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/klines"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Backtest honestly first** — rebuild the stack on `/api/v1/backtesting/klines` (2020–2025 in-sample, 2026 held out), charge fees plus `/api/v1/backtesting/funding`, and compare with the random-entry and EMA-cross nulls before any live use.
- **Run the daily decision at 00:00 UTC** — fetch the closed bar from `/api/v1/market-data/klines`, compute STC/VI/CHOP/McGinley, and emit orders only for entries that pass all gates.
- **Apply the event veto** — query `/api/v1/event/calendar` for the asset and macro events within 24h; skip new entries, keep managing open ones.
- **Enforce the beta cap** — compute 60-day beta to BTC from the same klines and reject orders breaching the 3% same-side cap.
- **Watch carry** — check `/api/v1/derivatives/funding-rates` daily for open runners and log accrued funding versus the kill criterion.

## Sources

- [[stonehill-forex-nnfx]] — NNFX rule set, Stonehill indicator library and testing protocol (fetched 2026-09-28)
- Configuration, crypto parameters and priors are this wiki's synthesis; no performance claim is sourced.

## Related

- [[nnfx-method]] — the framework
- [[mcginley-dynamic]] · [[schaff-trend-cycle]] · [[vortex-indicator]] · [[choppiness-index]] · [[waddah-attar-explosion]] — components and alternates
- [[atr]] · [[atr-position-sizing]] · [[atr-trailing-stop]] · [[beta]] · [[funding-rate]]
- [[turtle-trading]] · [[supertrend]] · [[moving-average-crossover]] · [[triple-screen-system]] — other rule-complete trend systems
- [[external-strategy-sources]] · [[stonehill-forex]]
