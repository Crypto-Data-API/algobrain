---
title: "Liquidation-Density Magnet / Repellent"
type: strategy
created: 2026-10-17
updated: 2026-10-17
status: draft
tags: [crypto, perpetual-futures, hyperliquid, liquidations, market-microstructure, quantitative, day-trading, backtesting]
aliases: ["Liquidation Magnet", "Liquidation-Density Imbalance", "Liquidation Cluster Magnet Test", "Density Asymmetry Trade"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "If a large, one-sided block of leveraged positions sits 1-2% from the mark, traders who can see it (and the liquidation engine once price arrives) have a reason to push price toward it; the trade bets on that drift and exits at or before the sweep. The counterparty is the crowded, over-leveraged side whose liquidation prices are public on Hyperliquid."

data_required: [liquidation-density-5m, liquidation-ladder, taker-trade-flow-1m, ohlcv-1h, mark-price]
min_capital_usd: 5000
capacity_usd: 2000000
crowding_risk: medium

expected_sharpe: 0.3   # prior only; the exploratory first-touch counts below are consistent with zero edge
expected_max_drawdown: 0.25
breakeven_cost_bps: 15

decay_evidence: "None measurable yet. The full-universe density history starts 2026-06-26 13:20 UTC, under four months at the time of writing. Liquidation heatmaps (Coinglass, Hypurrscan) have been public for years, so any magnet effect may already be traded away."

kill_criteria: |
  - take-profit share of resolved trades below 50% after 150 resolved trades
  - mean net return per trade below 0 after 150 trades
  - sleeve drawdown above 15%
  - realised cost per round trip above 15 bps on a rolling 50-trade window

related: ["[[short-liquidation-squeeze]]", "[[long-liquidation-cascade]]", "[[stop-hunting-and-liquidity-sweeps]]", "[[liquidation-cascade-fade]]", "[[liquidation-depth-cascade-sizing]]", "[[gamma-exposure-trading]]", "[[post-liquidation-rebound]]", "[[cascade-detection-signals]]", "[[hyperliquid-liquidation-engine]]", "[[crowding-indicators]]", "[[liquidations]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-mcp]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]"]

gates:
  - id: density_coin
    role: universe
    rule: "BTC, ETH, SOL and HYPE, plus any Hyperliquid perp the density route serves (up to 25 per call)"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=5m&splits=none
    field: data[].coin
    note: "The route is Pro Plus. History starts 2026-06-26 13:20 UTC. The newest 5-minute point was about 7 minutes old when checked on 2026-10-17."
  - id: band_total_p90
    role: entry
    rule: "Total liquidation notional inside 2% of the mark (long_below.2 + short_above.2) is at or above its own 90th percentile over the trailing 30 days of hourly points"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=trader_type
    field: data[].long_below.2
    replay: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=none
    replay_field: data[].long_below.2
    note: "Add data[].short_above.2 to get the total. start = 30 days back; rank the newest point against the 720 before it. Bands are cumulative and the rows are stock, not flow (grain.kind level_snapshot, sum_ok false), so never sum across rows."
  - id: one_sided
    role: entry
    rule: "Imbalance I = (short_above.2 - long_below.2) / total has |I| >= 0.6. I > 0 (shorts above) means go long; I < 0 (longs below) means go short"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=trader_type
    field: data[].short_above.2
    replay: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=none
    replay_field: data[].short_above.2
    note: "Uses the same point as band_total_p90."
  - id: heavy_side_floor
    role: filter
    rule: "The heavy side's 2% band holds at least $2M"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=trader_type
    field: data[].long_below.2
    note: "Read short_above.2 instead when the heavy side is shorts. The 30-day median 2% band for SOL and HYPE was $0 on 2026-10-17 (BTC $37.9M, ETH $8.9M), so on small perps one account can make a percentile spike."
  - id: cluster_in_ring
    role: entry
    rule: "The heavy side's 1% band holds less than half of its 2% band, so the cluster sits 1-2% from the mark rather than at it"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=trader_type
    field: data[].long_below.1
    note: "Compare with long_below.2 (or short_above.1 with short_above.2). Inside 1% the trade is a bet on the sweep itself, which this page does not take."
  - id: not_dealer_book
    role: filter
    rule: "Vault plus market-maker accounts hold at most 30% of the heavy side's 2% band"
    runnable: true
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=1h&splits=trader_type
    field: data[].by_trader_type.market_maker.long_below.2
    note: "Add by_trader_type.vault on the same side. Market-maker liquidations are largely hedged, so they are weak fuel."
  - id: multi_account
    role: filter
    rule: "The nearest heavy-side cluster in the live ladder has n_accounts >= 2, so one account cannot remove it by adding margin"
    runnable: partial
    endpoint: /api/v1/quant/positioning/ladder?symbol={coin}
    field: levels[].n_accounts
    note: "Live only (Pro Plus). n_accounts counts account-positions in the bin, not distinct wallets. The ladder bins on a 0.5% grid and can disagree with the density bands at the 2% edge: on 2026-10-17 06:25 UTC the density route put $35.2M of ETH shorts inside +2%, while the ladder placed the $29.1M short cluster (1 account) at +2.25%. No replay route serves levels; the archived liquidation_map snapshots were not checked for it."
  - id: flow_toward
    role: entry
    rule: "Taker flow over the last 60 closed minutes points toward the cluster: buy notional above sell notional for shorts above, sell above buy for longs below"
    runnable: true
    endpoint: /api/v1/hyperliquid/trade-flow?coin={coin}&minutes=60
    field: data[].buy_notional
    replay: /api/v1/backtesting/hl-trade-flow?coin={coin}&start={start}
    replay_field: data[].buy_notional
    note: "Sum buy_notional and sell_notional over the rows. Skip rows with partial true; their null notional is not a zero. The replay starts 2026-09-09, so the full rule can only be replayed from then."
  - id: entry_next_hour
    role: entry
    rule: "Enter at the open of the next hour in the cluster's direction"
    runnable: true
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: one_position
    role: sizing
    rule: "At most one open position per coin and three in total"
    runnable: true
    input: position
  - id: risk_size
    role: sizing
    rule: "Risk 0.5% of the sleeve to the stop: notional = 0.5% / 1.5% = 33% of the sleeve, at no more than 3x leverage"
    runnable: true
    input: position
  - id: take_profit
    role: exit
    rule: "Close at a 1.5% move from the entry fill in the cluster's direction"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: sweep_exit
    role: exit
    rule: "Close early if the heavy side's 2% band falls 70% or more below its value at entry while price has moved toward it (the cluster has been swept)"
    runnable: true
    input: position
    endpoint: /api/v1/backtesting/liquidation-density?coin={coin}&start={start}&interval=5m&splits=none
    field: data[].long_below.2
    note: "Confirm the sweep with data[].long_usd (or short_usd) on /backtesting/hl-liquidation-bars for the same coin. A band can also fall because price moved away, which is why the rule also asks for a move toward it."
  - id: stop_loss
    role: stop
    rule: "Stop 1.5% against the entry fill"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: time_stop
    role: stop
    rule: "Close 24 hours after entry"
    runnable: true
    input: position
  - id: drawdown_pause
    role: filter
    rule: "Stay flat while the sleeve's drawdown is above 15%"
    runnable: true
    input: position
---

# Liquidation-Density Magnet / Repellent

The liquidation-density magnet trades the idea that price is **drawn toward a large, one-sided block of liquidation levels sitting near the mark**. When most of the leveraged notional within 2% of the mark belongs to one side, and that block is 1-2% away, the strategy enters in the cluster's direction: long toward shorts stacked above, short toward longs stacked below. It exits at a symmetric 1.5% target, or early once the cluster has been swept. It reads Hyperliquid's public liquidation map as a time series through `GET /api/v1/backtesting/liquidation-density` (Pro Plus), which turns the hypothesis into something that can be tested with symmetric barriers.

**How this differs from the existing liquidation pages.** [[short-liquidation-squeeze]] and [[long-liquidation-cascade]] are one-sided *riders*. They buy just under a short cluster (or sell above a long one) and aim to hold *through* the sweep into the overshoot, using the three nearest `levels` from `/quant/gex`. This page is two-sided and *exits at or before* the cluster. It conditions on the coin's own density percentile and on *who* holds the cluster (`by_trader_type`), and it is built to be backtested on the density history. [[stop-hunting-and-liquidity-sweeps]] trades the wick *after* a stop cluster is hit. [[liquidation-cascade-fade]] and [[post-liquidation-rebound]] fade the cascade once it has happened. [[liquidation-depth-cascade-sizing]] sizes that fade on order-book depth. Here, what happens *after* the sweep (magnet becomes repellent, or price accelerates) is measured but **not traded**. That question is still open (see [[#Null hypothesis]]).

## Edge source

Per [[edge-taxonomy]], **behavioral + structural**.

- **Structural.** Hyperliquid positions and their liquidation prices are public, and [[hyperliquid-liquidation-engine|the liquidation engine]] closes them at market once the mark crosses. A dense one-sided band within 2% is therefore *known* forced flow that is waiting to be triggered.
- **Behavioral.** The holders of the cluster are over-leveraged (on 2026-10-16 the BTC 2% long band was almost all 40x positions, and whales held $149.8M of its $149.9M). Traders who can see the map have an incentive to lean toward it, which is the folk "liquidity hunting" story.

## Why this edge exists

The claimed mechanism has three parts. Each can fail.

1. **The fuel is visible.** On Hyperliquid, anyone can compute where a position liquidates. Aggregators publish it as a heatmap ([[coinglass]], [[hypurrscan]]) and CryptoDataAPI serves it as the ladder and the density series.
2. **Someone profits from triggering it.** A large trader who pushes price into a long cluster below can buy back the forced selling at a discount. The cluster is liquidity on demand, the same logic as [[stop-hunting-and-liquidity-sweeps]].
3. **The holders are slow to defend.** The cluster's owners can add margin or cut size. A whale that tops up moves its liquidation price away, so the cluster *retreats* ahead of price (see [[#Example trade]]). The edge exists only if enough of the cluster stays put.

**Who is on the other side:** the crowded, high-leverage holder whose liquidation price is published, plus anyone who fades the drift toward that holder.

**Why it may not exist:** if the map is widely watched, the drift is priced in before the band reaches the 90th percentile. And because a cluster is only *potential* flow, a single account can delete it by adding margin.

## Null hypothesis

Under no edge, price is a driftless random walk relative to the cluster. With **symmetric ±1.5% barriers**, the take-profit is hit first with probability **0.50**. The mean gross return per trade is **0**, and the mean net return is **minus the round-trip cost (about 9-12 bps)**.

**Exploratory first-touch count. This is not a backtest:** it has no costs, overlapping events and no out-of-sample split. The data is hourly `/backtesting/liquidation-density` for BTC, ETH, SOL and HYPE from 2026-06-26 to 2026-10-17. Events are hours where the 2% total was at or above its trailing-30-day 90th percentile and |I| >= 0.6, spaced at least 12 hours apart, with the ring and flow filters not applied. Results:

| Coin | Events | Hit +1.5% toward cluster first | Hit 1.5% away first | Neither in 24h |
|---|---|---|---|---|
| BTC | 23 | 2 | 2 | 19 |
| ETH | 45 | 15 | 20 | 10 |
| SOL | 49 | 18 | 22 | 9 |
| HYPE | 43 | 24 | 18 | 1 |
| **Total** | **160** | **59** | **62** | **39** |

That is 59 toward and 62 away: **no visible magnet**. The full rule set (ring, flow and the $2M floor) can only be replayed from 2026-09-09, when the trade-flow archive starts. From 2026-09-10 to 2026-10-17 it produced 78 trades: 40 take-profits, 32 stops and 6 time stops. The take-profit share of resolved trades is 55.6% (binomial p ≈ 0.35 against 0.50). The gross return was +0.14% per trade, most of it from HYPE (25 trades, +10.5% gross). The null is **not rejected**.

**Post-sweep behaviour (the "repellent" half).** There were 48 hourly sweeps, where a heavy side at or above its 80th percentile fell by at least 70% in one hour while price moved at least 0.75% toward it. Price continued in the sweep direction over the next 4 hours in 50% of them, with a mean of -0.06%. Over 12 hours it continued in 56%, with a mean of +0.42%. Both are indistinguishable from 50/50. The page does not trade either direction after a sweep.

**Statistical power.** To tell a 55% take-profit rate from 50% at 80% power and 5% two-sided significance takes about **780 resolved trades**. The September-October rate was about 63 trades a month, so that is about a year of data. It takes longer in practice, because BTC and ETH signals are correlated and do not count as independent trials. With under four months of history, even a 60% rate (about 190 trades) is only borderline testable today. Treat anything this page reports as a hypothesis, not a result.

## Rules

All reads use the first snapshot of each UTC hour (`interval=1h`), the same grid the archive replays.

**Universe.** Any Hyperliquid perp the density route serves, starting with BTC, ETH, SOL and HYPE.

**Entry**, when all of these hold:
1. **Dense:** `long_below.2 + short_above.2` is at or above its own trailing-30-day 90th percentile.
2. **One-sided:** I = (`short_above.2` − `long_below.2`) / total, with |I| ≥ 0.6. The sign of I sets the direction: long when I > 0, short when I < 0.
3. **Big enough:** the heavy side's 2% band is at least $2M.
4. **In the ring:** the heavy side's 1% band is under half its 2% band.
5. **Not a dealer book:** vault plus market-maker accounts hold at most 30% of the heavy side.
6. **More than one account (live only):** the nearest heavy-side `levels[]` entry on `/quant/positioning/ladder` has `n_accounts` ≥ 2.
7. **Flow agrees:** over the last 60 closed minutes, taker buys exceed sells (cluster above), or sells exceed buys (cluster below).
8. Enter at the next hour's open, one position per coin, at most three open.

**Exit**, whichever comes first:
- **Take profit:** +1.5% in the cluster's direction from the entry fill.
- **Sweep exit:** the heavy side's 2% band has fallen at least 70% below its entry value while price moved toward it. The fuel is gone, so close.
- **Stop:** 1.5% against.
- **Time stop:** 24 hours.

**Sizing.** Risk 0.5% of the sleeve to the stop: notional = 0.5% / 1.5% = 33% of the sleeve, at no more than 3x leverage. Stay flat while the sleeve's drawdown exceeds 15%.

## Implementation pseudocode

```python
# liquidation_density_magnet.py — hourly decision loop (sketch)
TP, SL, TIME_STOP_H = 0.015, 0.015, 24

def heavy_side(pt):
    lb, sa = pt["long_below"]["2"], pt["short_above"]["2"]
    total = lb + sa
    if total == 0:
        return None
    imb = (sa - lb) / total
    side = "short_above" if imb > 0 else "long_below"
    return total, imb, side

def signal(coin, hist, pt, ladder, flow):
    """hist: trailing 720 hourly points from /backtesting/liquidation-density (splits=trader_type)."""
    hs = heavy_side(pt)
    if hs is None:
        return None
    total, imb, side = hs
    p90 = percentile([p["long_below"]["2"] + p["short_above"]["2"] for p in hist], 90)
    if total < p90 or abs(imb) < 0.6:
        return None
    if pt[side]["2"] < 2e6:                          # heavy_side_floor
        return None
    if pt[side]["1"] >= 0.5 * pt[side]["2"]:         # cluster_in_ring: already at the mark
        return None
    tt = pt["by_trader_type"]
    dealer = tt["market_maker"][side]["2"] + tt["vault"][side]["2"]
    if dealer > 0.3 * pt[side]["2"]:                 # not_dealer_book
        return None
    want = "short" if side == "short_above" else "long"   # liquidation side we are walking toward
    near = min((l for l in ladder["levels"] if l["side"] == want), key=lambda l: abs(l["dist_pct"]), default=None)
    if near is None or near["n_accounts"] < 2:       # multi_account (live only)
        return None
    rows = [r for r in flow["data"] if not r["partial"]]
    buy, sell = sum(r["buy_notional"] for r in rows), sum(r["sell_notional"] for r in rows)
    direction = +1 if imb > 0 else -1
    if (direction > 0 and buy <= sell) or (direction < 0 and sell <= buy):
        return None
    return {"coin": coin, "dir": direction, "entry_band": pt[side]["2"], "side": side}

def manage(pos, mark, band_now, hours_held):
    move = (mark / pos["entry"] - 1) * pos["dir"]
    if move >= TP:                                    return "take_profit"
    if move > 0 and band_now <= 0.3 * pos["entry_band"]: return "sweep_exit"
    if move <= -SL:                                   return "stop"
    if hours_held >= TIME_STOP_H:                     return "time_stop"
    return "hold"
```

## Indicators / data used

- **Liquidation density** ([[cryptodataapi-backtesting]]): `GET /api/v1/backtesting/liquidation-density`, Pro Plus. Each point is one coin at one 5-minute snapshot. It gives `mark`, plus cumulative ±0.5/1/2/3/5% bands of `long_below` (longs liquidating below the mark) and `short_above` (shorts liquidating above it), split `by_trader_type` (vault, market_maker, whale, smart_money, high_leverage, other) and `by_leverage` (3-100x). Rows are stock, not flow: `grain.kind` is `level_snapshot` and `sum_ok` is false. History starts 2026-06-26 13:20 UTC (`coverage.archive_hint`). Calls are limited to 93 days and 25 coins.
- **Live ladder** ([[cryptodataapi-regimes]]): `GET /api/v1/quant/positioning/ladder?symbol=` (Pro Plus) bins every account of $100k or more on a 0.5%-of-mark grid. It serves `bins`, `bins_directional` (market-maker and vault liquidations removed) and `bins_by_class`, plus `levels`: the three nearest clusters above and below, each with `n_accounts`. It uses the same builder as the archived `liquidation_map` snapshot type, which holds 31,514 snapshots from 2026-06-26.
- **GEX levels** ([[cryptodataapi-regimes]]): `GET /api/v1/quant/gex?coin=` (Pro) serves the same `levels` and a `regime.state` of amplify (score ≥ 0.35), dampen (≤ −0.20) or transitional. Its `distribution_context.near_density_pctile` ranks the near-mark density against the coin's own 30 days. It is useful context but is not a gate here.
- **No Hyperliquid-family liquidation map.** The `/api/v1/hyperliquid/*` routes in the 2026-10-17 spec have no liquidation-map endpoint. The live map is the ladder above, and history is the density series or the `liquidation_map` / `liquidation_levels` snapshot types on `/backtesting/snapshots`.
- **Taker flow** ([[cryptodataapi-hyperliquid]]): `/hyperliquid/trade-flow` live, `/backtesting/hl-trade-flow` since 2026-09-09.
- **Realised liquidations:** `/backtesting/hl-liquidation-bars` (5m/15m/1h, Hyperliquid fill tape, from 2026-07-23), to confirm that a band drained because positions were actually liquidated.

## Example trade

This is a real, rule-by-rule replay on ETH, 2026-10-10 to 2026-10-13, using hourly density, Hyperliquid 1h klines and archived trade flow. All four trades were shorts toward a long cluster below.

**The cluster.** From 2026-10-10 a block of about $36-54M in ETH long liquidations sat 1-3% under the mark, with almost nothing on the short side (I between −0.72 and −1.00). At the 2026-10-12 03:00 snapshot (mark $2,543.45) whales held $43.8M of the $43.9M `long_below.2` band. Market makers and vaults held $0. An hour later (mark $2,545.65) the 2% band read **$0** while the 3% band held $45.2M. A 0.09% move in the mark had pushed the block across the 2% edge, which places it at about $2,493-2,495, held by very few accounts.

| # | Signal (UTC) | Entry (next open) | Outcome |
|---|---|---|---|
| 1 | 10-10 17:00, I = −0.72, $36.4M | short $2,507.2 at 10-10 18:00 | **stopped** (price up 1.5%) at $2,544.8, 10-11 16:00 |
| 2 | 10-11 18:00, I = −0.97, $44.6M | short $2,533.9 at 10-11 19:00 | **stopped** at $2,571.9, 10-12 06:00 |
| 3 | 10-12 09:00, I = −0.89, $53.1M | short $2,559.2 at 10-12 10:00 | **take profit** −1.5% at $2,520.8, 10-12 12:00 |
| 4 | 10-12 13:00, I = −1.00, $43.6M | short $2,541.0 at 10-12 14:00 | **take profit** at $2,502.9, 10-12 21:00 |

That is two wins and two losses: **0.0% gross, about −0.36% net** after four round trips at Hyperliquid's base taker fee of 0.045% per side (`/hyperliquid/meta` `fees`).

**What the cluster did next.** Price did travel to it, falling about 5% over three days. But it **retreated** as price arrived. At 22:00 the 1% band held $28.9M with the mark at $2,488. At 23:00 the 0.5% band held $22.2M with the mark at $2,465. The holders were adding margin, which moves their liquidation prices lower. The cluster finally broke in the 00:00 hour on 2026-10-13: `hl-liquidation-bars` shows **$14.93M of long liquidations** from 1,021 fills, and the low was $2,408.0. Price then rebounded 5.1% to $2,530.9 by 05:00. At the 23:00 snapshot the 1% band held 75% of the 2% band, so `cluster_in_ring` blocked a fifth short right into that rebound.

The lesson: the magnet looked real, but symmetric barriers turned it into a coin flip. Single-whale clusters move.

*(Historical replay for illustration. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.3 (prior) | No result supports more. Exploratory counts are consistent with 0 |
| Take-profit share of resolved trades | 55.6% (40/72), Sep-Oct 2026 replay | Binomial p ≈ 0.35. The break-even share at 10 bps cost is about 53% |
| Gross per trade | +0.14% | Most of it from HYPE. BTC produced only 5 trades in 37 days |
| Round-trip cost | 9 bps fees + 1-5 bps slippage | Taker both sides at the base tier. Funding over a ≤24h hold is ±1-5 bps at normal rates |
| Breakeven cost | ~15 bps | Only if the true take-profit share is about 55% |
| Signal frequency | ~60 trades/month across four coins | Dominated by ETH, SOL and HYPE. BTC rarely passes the ring filter |
| Max drawdown (expected) | ~25% | Losing streaks of 4-6 at 0.5% risk each are routine at a 50% hit rate |

With 1:1 barriers the strategy needs a hit rate above about 53% to clear costs. Any edge has to come from the hit rate.

## Capacity limits

- **Per trade:** BTC and ETH take $1-2M notional without much slippage on Hyperliquid. SOL and HYPE books thin out below that, and SOL and HYPE are where most of the signals come from.
- **Aggregate:** `capacity_usd: 2000000`. A large entry toward a cluster is itself the push that the magnet story relies on. Past a few million, the trader becomes the hunter and the edge, if any, becomes market impact.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **The cluster retreats (structural).** Holders add margin and the liquidation price walks away, as in the example. Single-account clusters are the worst case, which is why `multi_account` exists. That gate is live-only and cannot be replayed.
2. **No edge to begin with (#1, false discovery).** The exploratory counts already look like a coin flip. With four coins, several thresholds and a short history, a positive replay would mostly measure noise. Run [[overfitting-detection]] and a [[deflated-sharpe-ratio]] before believing any number.
3. **Crowding (#4).** Liquidation heatmaps are among the most-watched retail tools. If everyone leans toward the same cluster, the drift happens before the 90th-percentile trigger fires.
4. **Data artefacts (#7).** Band edges are cumulative and recomputed every 5 minutes against a moving mark, so a single position can flicker in and out of the 2% band, as with ETH at 03:00 versus 04:00. The ladder and the density series use different grids and can disagree.
5. **Regime change.** Hyperliquid's margin tiers changed (the API corrected its served table on 2026-10-10), and engine changes can move liquidation prices for the same positions.

## Kill criteria

Retire or pause (see [[when-to-retire-a-strategy]]) on any of:

1. **Take-profit share below 50%** after 150 resolved trades counted from the first forward trade.
2. **Mean net return per trade below 0** after 150 trades.
3. **Sleeve drawdown above 15%** (also a live gate).
4. **Realised cost above 15 bps per round trip** on a rolling 50-trade window. At that point a 55% hit rate no longer pays.
5. **Data failure:** the density route stops updating for more than 2 hours, or the ladder and density disagree on the heavy side's direction in more than 20% of signals over a month.

## Advantages

- **Testable by design.** Symmetric barriers make the null exact (50%), and the density archive replays every gate except `multi_account`.
- **Uses data most traders only see as a picture.** The `by_trader_type` and `by_leverage` splits say *whose* liquidations they are, which a heatmap does not.
- **Bounded holds.** At most 24 hours, so funding is a rounding error and overnight gaps don't matter.
- **Two-sided.** It is not structurally long or short crypto.

## Disadvantages

- **Short history.** Under four months for density and five weeks for the full rule. No regime breadth.
- **The exploratory evidence is flat.** The page documents a hypothesis that has not yet shown an edge.
- **Pro Plus.** The density route and the ladder both need the top tier.
- **Concentrated in small perps.** BTC, the most liquid market, rarely signals once the ring filter applies.
- **The best gate is live-only.** Single-account detection cannot be replayed, so the backtest overstates how many trades the live system takes.

## Sources

- [[cryptodataapi-backtesting]]: the `/backtesting/liquidation-density` description (bands, splits, history from 2026-06-26), the `hl-liquidation-bars` grain and coverage, and the `hl-trade-flow` start date.
- [[cryptodataapi-regimes]]: `/quant/positioning/ladder` and `/quant/gex` `levels`, `regime` thresholds and `distribution_context`.
- [[cryptodataapi-hyperliquid]]: `/hyperliquid/trade-flow` `partial` semantics and the fee schedule on `/hyperliquid/meta`.
- Live OpenAPI spec and live calls, 2026-10-17: the density point shapes and `grain`/`coverage` blocks; hourly density for BTC, ETH, SOL and HYPE from 2026-06-26 to 2026-10-17 (10,820 points); the ETH example (density, `hl-liquidation-bars`, Hyperliquid klines and `hl-trade-flow`); and the live ETH ladder and GEX reads at 06:10-06:32 UTC. All exploratory counts on this page come from those pulls.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/backtesting/liquidation-density?coin=BTC,ETH,SOL,HYPE&start=<30 days ago>&interval=5m&splits=trader_type`: the newest density point, about 5-10 minutes behind real time
- `GET /api/v1/quant/positioning/ladder?symbol=ETH`: the live ladder with `levels[].n_accounts` (Pro Plus)
- `GET /api/v1/quant/gex?coin=ETH`: `coins.ETH.levels` and the amplify/dampen `regime` (Pro)
- `GET /api/v1/hyperliquid/trade-flow?coin=ETH&minutes=60`: taker flow toward the cluster

**Historical data:**
- `GET /api/v1/backtesting/liquidation-density?coin=ETH&start=2026-06-26&end=2026-09-20&interval=1h&splits=none`: hourly bands from 2026-06-26 (93 days per call)
- `GET /api/v1/backtesting/hl-liquidation-bars?coin=ETH&interval=1h&start=2026-10-12`: realised long and short liquidations, to confirm sweeps
- `GET /api/v1/backtesting/hl-trade-flow?coin=ETH&start=2026-09-09`: replay for `flow_toward`
- `GET /api/v1/backtesting/klines?symbol=ETH&exchange=hyperliquid&interval=1h&start=2026-06-26`: Hyperliquid price bars for the barriers

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/backtesting/liquidation-density?coin=ETH&start=2026-10-12T00:00:00Z&end=2026-10-13T06:00:00Z&interval=1h&splits=trader_type"
```

Endpoint catalogs: [[cryptodataapi-backtesting]], [[cryptodataapi-regimes]], [[cryptodataapi-hyperliquid]].

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this page as follows:

- **Signal:** pull one `liquidation-density` call per hour for up to 25 coins with `splits=trader_type`, then compute total, I and the 1%/2% ring per coin. Rank each coin's total against its own previous 720 hourly points, which comes from the same route.
- **Filter:** keep coins where vault plus market-maker accounts hold at most 30% of the heavy side. Then call `/quant/positioning/ladder` for the survivors only, because it is one coin per call, and drop any cluster with `n_accounts` of 1.
- **Execution:** check `/hyperliquid/trade-flow?minutes=60` for flow toward the cluster, skipping `partial` minutes. Enter at the hour's open, and watch the 5-minute density for the 70% band drain that triggers `sweep_exit`.
- **Backtest:** replay from 2026-09-09 (the trade-flow start) with `liquidation-density` (1h), `backtesting/klines` (`exchange=hyperliquid`) and `hl-trade-flow`. Score first touch of ±1.5% against the exact 50% null, and report the binomial p-value, not a Sharpe ratio.
- **Tips:** never sum density rows across time (`sum_ok: false`). Treat the 2% edge as noisy, because one position can flicker across it.

## Related

- [[short-liquidation-squeeze]]: rides through a short cluster into the overshoot; this page exits at or before it
- [[long-liquidation-cascade]]: the short-side rider through long clusters
- [[stop-hunting-and-liquidity-sweeps]]: trades the wick after a stop cluster is hit
- [[liquidation-cascade-fade]]: fades the cascade once it is printing
- [[post-liquidation-rebound]]: the recovery after the flush
- [[liquidation-depth-cascade-sizing]]: book-depth gate on cascade fades
- [[gamma-exposure-trading]]: options and perp positioning magnets (max pain, GEX)
- [[cascade-detection-signals]]: detection primitives, including the density route
- [[hyperliquid-liquidation-engine]]: how the clusters actually get liquidated
- [[crowding-indicators]]: liquidation density as a crowding measure
- [[liquidations]], [[liquidation-cascade]], [[open-interest]], [[order-flow]]
- [[exchange-flow-spike-reaction]], [[forced-flow-exhaustion-fade]]: the other two pages built on the 2026-10 data releases
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]], [[overfitting-detection]]
