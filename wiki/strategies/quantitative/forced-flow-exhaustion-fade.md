---
title: "Forced-Flow Exhaustion Fade (Live Event Stream)"
type: strategy
created: 2026-10-17
updated: 2026-10-17
status: draft
tags: [crypto, perpetual-futures, hyperliquid, liquidations, open-interest, mean-reversion, event-driven, scalping, market-microstructure]
aliases: ["Stream Exhaustion Fade", "OI-Confirmed Liquidation Fade", "SSE Forced-Flow Fade", "Deleveraging Exhaustion Long"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, latency]
edge_mechanism: "When a fast drop arrives with a burst of long liquidations AND open interest falling, the selling is positions being closed by force, not new shorts with a view. Once the forced flow stops, the price it pushed down tends to snap part of the way back; the counterparty is the liquidation engine and the panicked closer, who sell regardless of price."

data_required: [event-stream-sse, liquidation-fills, open-interest-5m, ohlcv-1m, gex-regime, mark-price]
min_capital_usd: 5000
capacity_usd: 1000000
crowding_risk: medium

expected_sharpe: 0.2   # prior only; the 5-minute-bar event study below is consistent with zero edge
expected_max_drawdown: 0.20
breakeven_cost_bps: 12

decay_evidence: "None measurable. The Hyperliquid liquidation tape behind the replay starts 2026-07-23, and the stream itself keeps only a short replay ring. Cascade fades as a family have shrunk as exchanges improved partial liquidation (see liquidation-cascade-fade)."

kill_criteria: |
  - mean net return per trade below 0 after 100 trades
  - win rate below 45% after 100 trades
  - sleeve drawdown above 10%
  - median signal-to-fill latency above 3 seconds over 20 trades

related: ["[[liquidation-cascade-fade]]", "[[off-hours-liquidation-playbook]]", "[[oi-flush-reversion]]", "[[cascade-detection-signals]]", "[[liquidation-depth-cascade-sizing]]", "[[cross-venue-cascade-dislocation]]", "[[hlp-cascade-alongside-playbook]]", "[[post-liquidation-rebound]]", "[[long-liquidation-cascade]]", "[[volume-oi-conditioned-reversal]]", "[[oi-price-exhaustion]]", "[[event-driven-backtesting]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi-mcp]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]"]

gates:
  - id: universe_perps
    role: universe
    rule: "BTC, ETH, SOL and HYPE perps on Hyperliquid, each with at least $200M of 24h volume"
    runnable: true
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].day_volume
    note: "On 2026-10-17: BTC $2,716M, ETH $924M, SOL $304M, HYPE $283M. All four have the Hyperliquid liquidation tape the replay needs."
  - id: price_drop_5m
    role: entry
    rule: "The coin's price_move events over the trailing 300 seconds sum to -0.6% or less (BTC), -0.8% (ETH), -1.0% (SOL) or -1.2% (HYPE)"
    runnable: true
    endpoint: /api/v1/stream?types=price_move&symbols={coin}
    field: pct
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1m&start={start}
    replay_field: klines[].c
    note: "Each SSE message's data is one event object: id, ts (ms), type, venue, symbol, pct, price, prev_price, window_s. price_move only fires for 1-minute moves of 0.10% or more on perps trading $1M+/day, so the sum is a slight underestimate of the 5-minute move. window_s read 51-61 (and sometimes 6-7) live, not exactly 60. Replay: compare 1m closes 5 bars apart."
  - id: hl_long_liq_floor
    role: entry
    rule: "Hyperliquid long liquidations (venue hyperliquid, side long) over the same 300 seconds total at least $1M (BTC, ETH) or $250k (SOL, HYPE)"
    runnable: true
    endpoint: /api/v1/stream?types=liquidation&symbols={coin}
    field: usd
    replay: /api/v1/backtesting/hl-liquidation-bars?coin={coin}&interval=5m&start={start}
    replay_field: data[].long_usd
    note: "side is the LIQUIDATED position's side. The stream also carries OKX and Bybit liquidations ($250+), but the archive is Hyperliquid only, so the rule counts Hyperliquid alone to keep live and replay identical. For exact 300-second windows, replay from the fill tape /backtesting/hl-liquidations (field usd), from 2026-07-23."
  - id: liq_vs_baseline
    role: entry
    rule: "That 300-second Hyperliquid long-liquidation total is at least 10x the coin's trailing-7-day mean per 5 minutes"
    runnable: true
    endpoint: /api/v1/backtesting/hl-liquidation-bars?coin={coin}&interval=5m&start={start}
    field: data[].long_usd
    note: "start = 7 days back. Sum long_usd and divide by 2,016 (buckets with no fills are omitted, not zero). For ETH in the week to 2026-10-07 the mean was $6.3k per 5 minutes, so the $1M floor was the binding gate."
  - id: oi_falling
    role: entry
    rule: "The coin's oi_delta events over the same 300 seconds sum to -0.2% or less: positions are closing, not opening"
    runnable: true
    endpoint: /api/v1/stream?types=oi_delta&symbols={coin}
    field: pct
    replay: /api/v1/backtesting/funding?symbol={coin}&exchange=hyperliquid&start={start}
    replay_field: data[].open_interest
    note: "Replay with the 5-minute open_interest samples on /backtesting/funding (default grain snapshot_5m; never sum its funding_rate). /backtesting/hl-funding-bars only has oi_change_pct per 1h bar, which is too coarse for this gate."
  - id: exhaustion
    role: entry
    rule: "60 seconds pass with no new downward price_move (-0.10% or worse) for the coin after the three trigger gates hold"
    runnable: true
    endpoint: /api/v1/stream?types=price_move&symbols={coin}
    field: pct
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1m&start={start}
    replay_field: klines[].l
    note: "Replay: the first closed 1m bar whose close is no more than 0.10% below the previous close."
  - id: not_amplify
    role: filter
    rule: "Skip the trade when the coin's /quant/gex regime.state is amplify (score 0.35 or more): the API's own legend says forced flow follows through there"
    runnable: true
    endpoint: /api/v1/quant/gex?coin={coin}
    field: coins.{coin}.regime.state
    replay: /api/v1/quant/gex/history?symbol={coin}&from={start}
    replay_field: points[].regime_score
    note: "The history ring is timestamped from 2026-09-09 and holds about 30 days. For older dates use the gamma_exposure snapshot type (from 2026-07-06). ETH read -0.15 (transitional) around the 2026-10-07 example."
  - id: stream_gapless
    role: filter
    rule: "Act only when the client saw the whole 300-second window: after any reconnect, backfill with since_id (or Last-Event-ID) before evaluating"
    runnable: true
    endpoint: /api/v1/stream/recent?symbols={coin}&limit=1
    field: last_id
    note: "Compare last_id with the last id received. A since_id=1 replay at 06:13 UTC on 2026-10-17 began at 05:59:10 UTC, about 14 minutes back rather than the ~2h ring the spec describes, so a long disconnect cannot be fully recovered."
  - id: entry_market
    role: entry
    rule: "Buy at the mark when the exhaustion gate clears (long only)"
    runnable: true
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: take_profit
    role: exit
    rule: "Take profit when price recovers half the gap between the entry fill and the pre-move price (the price at the start of the trigger window)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: stop_loss
    role: stop
    rule: "Stop at the move's extreme low minus 25% of the move (pre-move price minus the low)"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: time_stop
    role: stop
    rule: "Close 60 minutes after entry"
    runnable: true
    input: position
  - id: risk_size
    role: sizing
    rule: "Risk 0.25% of the sleeve between entry and stop, with notional capped at 25% of the sleeve"
    runnable: true
    input: position
  - id: concurrency
    role: sizing
    rule: "One position per coin and two in total, with a 60-minute cooldown on a coin after an exit"
    runnable: true
    input: position
  - id: drawdown_pause
    role: filter
    rule: "Stay flat while the sleeve's drawdown is above 10%"
    runnable: true
    input: position
---

# Forced-Flow Exhaustion Fade (Live Event Stream)

The forced-flow exhaustion fade buys the end of a **liquidation-driven drop**, but only when the stream shows the drop was *deleveraging*. Three things must coincide in five minutes: a fast fall in price, a burst of long liquidations, and **open interest falling**. The trade waits 60 seconds with no new down-move, then buys, targets half the gap back to the pre-move price, and holds for at most an hour. It is built for `GET /api/v1/stream` (Server-Sent Events, Pro and Pro Plus), which pushes `price_move`, `liquidation` and `oi_delta` events as they happen. The backtest is assembled from archived equivalents, because the stream's replay buffer is short.

**How this differs from the existing cascade pages.** [[liquidation-cascade-fade]] triggers on a 15-minute liquidation spike plus a 2% drop, and times entry on CVD flattening. [[off-hours-liquidation-playbook]] adapts that fade to the session. [[liquidation-depth-cascade-sizing]] sizes it on book depth. None of them asks whether open interest *fell*. That is this page's distinguishing gate: a drop on rising OI means new shorts are opening into the move, which is information, so the page stands aside. [[oi-flush-reversion]] uses an OI purge too, but over days (−15% from a 5-day peak), not minutes. [[cross-venue-cascade-dislocation]] trades the cross-venue spread, not the outright price. [[cascade-detection-signals]] catalogues the detection primitives this page combines. This is also the first wiki page specified **directly on the stream's event types**, with a stated recipe for replaying them.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + latency**.

- **Structural.** [[hyperliquid-liquidation-engine|Liquidation engines]] sell at market without regard to price. Once the forced flow ends, the price it printed is not a consensus price.
- **Behavioral.** Panicked closers (OI falling, not rising) add to the overshoot, the same over-reaction [[volume-oi-conditioned-reversal]] exploits on a weekly horizon.
- **Latency.** The stream delivers events fast. In the live sample, `recv_ts` minus `ts` had a median of 12 ms for `price_move`, 17 ms for `oi_delta` and 419 ms for `liquidation` (90th percentile 1.1 s). Most retail fades key off 1- or 5-minute candles and arrive later.

## Why this edge exists

**Who is on the other side:** the liquidated long, who is closed at market by the engine, and the trader who panics out alongside it. Neither chooses the price.

**Why OI matters.** A 1% drop can be (a) longs being forced or scared out, or (b) new shorts opening because someone knows something. In case (a), OI falls and the selling ends when the leverage is gone. In case (b), OI rises, and a fade is a bet against an informed seller. `oi_delta` separates the two within a minute.

**Why it might not work:** cascades often come in waves. A first exhaustion can be the pause before the next layer of liquidations, which is exactly the `amplify` state that `/quant/gex` flags. Liquidation engines now liquidate partially, and backstops (HLP on Hyperliquid) absorb flow, so overshoots are smaller than they were in 2020-2021 (see [[liquidation-cascade-fade]]).

## Null hypothesis

Under no edge, price after the exhaustion signal is a random walk. The **mean 60-minute return after entry is 0**, the win rate is **50%**, and the mean net return is **minus the round-trip cost (about 10-12 bps)**.

**Exploratory event study at 5-minute resolution.** This is not a backtest: no costs, no target or stop (a flat 60-minute hold), and 5-minute bars standing in for the stream. It covers Hyperliquid BTC, ETH, SOL and HYPE from 2026-07-23 08:00 to 2026-10-16 17:00 (85 days). An event needed: a 5m bar moving at least 0.6/0.8/1.0/1.2%; same-side Hyperliquid liquidations in that bar of at least $1M (BTC/ETH) or $250k (SOL/HYPE) *and* at least 10x the trailing-7-day mean; OI change over the bar (5-minute `open_interest` samples) of −0.2% or less; and a next bar with no new extreme. Entry was at that bar's close, with one event per coin per hour. Both directions were run, fading squeezes as well as dumps.

| Direction | Events | Mean 60-min fade return | Median | Positive |
|---|---|---|---|---|
| Downside (long fades) | 17 | +0.06% | +0.15% | 9 of 17 |
| Upside (short fades of squeezes) | 16 | −0.67% | −0.34% | 5 of 16 |
| **All with OI ≤ −0.2%** | **33** | **−0.30%** | −0.06% | 42% |
| Control: OI > −0.2% | 10 | +0.08% | | 50% |

The null is **not rejected**, and the two-sided version lost money. This page's rule is **long-only**, but that choice was made *after* seeing the split above. Those 17 events are in-sample and count as no evidence. The out-of-sample clock starts on 2026-10-17.

**Statistical power.** The fade returns had a standard deviation of about 0.98%. Detecting a +0.20% mean edge (twice the cost) at 80% power and 5% two-sided needs about **190 events** (n ≈ (2.8 × 0.98 / 0.20)²). At roughly 6 long events a month on four coins, that is **about 2.5 years**. Adding more of the 25 coins the archive serves per call would shorten it, but only if those coins are not just echoing BTC.

## Rules

**Universe:** Hyperliquid BTC, ETH, SOL and HYPE (each at least $200M of 24h volume).

**Trigger.** All three must hold over the trailing **300 seconds** of stream events for one coin:
1. **Price:** the `price_move` `pct` sum is at most **−0.6%** (BTC), **−0.8%** (ETH), **−1.0%** (SOL) or **−1.2%** (HYPE).
2. **Forced flow:** Hyperliquid `liquidation` events with `side: long` total at least **$1M** (BTC, ETH) or **$250k** (SOL, HYPE), *and* at least **10x** the coin's trailing-7-day mean per 5 minutes.
3. **Deleveraging:** the `oi_delta` `pct` sum is at most **−0.2%**.

**Filters:**
- **Regime:** skip when `/quant/gex` `regime.state` is `amplify`.
- **Data:** act only when the stream covered the whole window. Backfill with `since_id` after a reconnect.

**Entry:** wait until **60 seconds pass with no new downward `price_move`** (−0.10% or worse), then buy at the mark. Long only.

**Exits:**
- **Take profit:** half the gap from entry back to the pre-move price, where the pre-move price is the price at the start of the 300-second window.
- **Stop:** the extreme low minus 25% of the move.
- **Time stop:** 60 minutes.

**Sizing:** risk 0.25% of the sleeve between entry and stop, with notional capped at 25% of the sleeve. One position per coin and two in total, with a 60-minute cooldown per coin. Stay flat while the sleeve's drawdown exceeds 10%.

## Implementation pseudocode

```python
# forced_flow_exhaustion_fade.py — SSE consumer (sketch)
import json, collections, time
DROP = {"BTC": -0.6, "ETH": -0.8, "SOL": -1.0, "HYPE": -1.2}
LIQ_FLOOR = {"BTC": 1e6, "ETH": 1e6, "SOL": 2.5e5, "HYPE": 2.5e5}
WIN_MS = 300_000

buf = collections.defaultdict(collections.deque)   # coin -> recent events
armed = {}                                          # coin -> trigger state

def window(coin, now_ms):
    q = buf[coin]
    while q and now_ms - q[0]["ts"] > WIN_MS:
        q.popleft()
    return q

def on_event(ev, baseline_5m, regime_state):
    coin = ev["symbol"]
    if coin not in DROP:
        return None
    buf[coin].append(ev)
    q = window(coin, ev["ts"])
    moves = [e for e in q if e["type"] == "price_move"]
    drop = sum(e["pct"] for e in moves)
    liq = sum(e["usd"] for e in q if e["type"] == "liquidation"
              and e["venue"] == "hyperliquid" and e["side"] == "long")
    doi = sum(e["pct"] for e in q if e["type"] == "oi_delta")
    if (coin not in armed and drop <= DROP[coin]
            and liq >= max(LIQ_FLOOR[coin], 10 * baseline_5m[coin]) and doi <= -0.2
            and regime_state[coin] != "amplify"):
        pre = moves[0]["prev_price"] if moves else ev.get("price")
        armed[coin] = {"pre": pre, "low": min(e["price"] for e in moves), "last_down": ev["ts"]}
    a = armed.get(coin)
    if a and ev["type"] == "price_move":
        a["low"] = min(a["low"], ev["price"])
        if ev["pct"] <= -0.10:
            a["last_down"] = ev["ts"]
    return a

def check_entry(coin, now_ms, mark):
    a = armed.get(coin)
    if a and now_ms - a["last_down"] >= 60_000:          # exhaustion
        move = a["pre"] - a["low"]
        tp = mark + 0.5 * (a["pre"] - mark)
        sl = a["low"] - 0.25 * move
        armed.pop(coin)
        return {"coin": coin, "side": "long", "tp": tp, "sl": sl, "expires_ms": now_ms + 3_600_000}
    return None
# connect: GET /api/v1/stream?types=price_move,liquidation,oi_delta&symbols=BTC,ETH,SOL,HYPE
# remember the last `id`; on reconnect pass since_id=<last id> and rebuild buf before trading
```

## Indicators / data used

**The stream** (spec 2026-10-14; live checks on 2026-10-17):
- `GET /api/v1/stream` is SSE. The spec marks it `x-streaming`: the response never completes. It is **Pro and Pro Plus**, with up to 3 concurrent streams per key. Parameters: `types` (comma list of `liquidation`, `whale_transfer`, `whale_position`, `funding`, `oi_delta`, `price_move`), `symbols` (base coins), `min_usd` (drops smaller events carrying `usd`; `funding` and `price_move` always pass) and `since_id` (replay buffered events, a ~2h ring per the spec; the `Last-Event-ID` header wins if both are sent).
- Every event carries `id`, `ts` (event time, ms), `recv_ts` (when CryptoDataAPI saw it), `type`, `venue` and `symbol`, plus type fields. `liquidation`: `side` (the **liquidated** side) and `usd`, plus `px` and `sz` on Hyperliquid, from OKX, Bybit and Hyperliquid at $250+. `oi_delta`: signed `usd`, `pct`, `window_s` and `oi_usd`. `price_move`: `pct`, `price`, `prev_price` and `window_s`, for 1-minute moves of 0.10%+ on perps trading $1M+/day. `funding`: `rate_1h`, `prev_rate_1h` and `settle`. `whale_transfer` mirrors the exchange-flow spike alerts (see [[exchange-flow-spike-reaction]]).
- **Live notes.** The stream opens with `retry: 3000`. A `/stream/recent?limit=500` call returned 500 events spanning only 5 minutes 10 seconds (230 `funding`, 128 `oi_delta`, 126 `price_move`, 16 `liquidation`), so it is a backfill tool, not history. A `since_id=1` replay reached back about 14 minutes, not 2 hours. `window_s` values were 51-61 and 6-7, not exactly 60 or 300.
- `GET /api/v1/stream/recent` returns JSON for any key (Free included): the newest 1-500 events, oldest first, with `last_id` to pass as `since_id`. `GET /api/v1/stream/delayed` is a keyless preview of a window that ended 30 minutes ago, with `server_now`, `delay_ms`, `window_start`/`window_end` and `events_per_min`. The spec says the window is 5 minutes; the 2026-10-17 response spanned 3 minutes, with 138 events at 46 per minute. Both are for testing a parser, not a strategy.

**Building the backtest from archives.** The stream cannot be replayed beyond its ring, so each event type is rebuilt from the closest archive ([[cryptodataapi-backtesting]]):

| Stream input | Archived equivalent | Resolution | Available from | Caveat |
|---|---|---|---|---|
| `price_move` | `/backtesting/klines?exchange=hyperliquid&interval=1m` | 1m bars | local rows from 2026-05-09 (ETH) | Sum of 1m closes approximates the event sum. The stream drops sub-0.10% minutes |
| `liquidation` (Hyperliquid) | `/backtesting/hl-liquidations` (fills) or `/backtesting/hl-liquidation-bars?interval=5m` | per fill / 5m | 2026-07-23 (pilot 2026-04-24 to 05-05) | OKX and Bybit stream liquidations have no flow archive. `/backtesting/liquidations` is a rolling window and must not be differenced |
| `oi_delta` | `/backtesting/funding?exchange=hyperliquid` `open_interest` | 5-min samples | 2026-03-30 | `/backtesting/hl-funding-bars` `oi_change_pct` is per 1h bar, too coarse for the 300-second gate |
| `funding` | `/backtesting/hl-funding-bars` `funding_rate_mean` | 1h | 2026-03-30 | Not used by this rule |
| (no stream equivalent) taker CVD | `/backtesting/hl-trade-flow` | 1m | 2026-09-09 | Optional cross-check of "selling stopped" |
| `regime.state` | `/quant/gex/history` `regime_score`, or `gamma_exposure` snapshots | ~1h / 5m | 2026-09-09 / 2026-07-06 | Amplify means a score of 0.35 or more |

The **joint replay window** for the core rule runs from 2026-07-23 to the present, about 12 weeks, or 7 weeks if the regime gate is replayed from the history ring.

## Example trade

**ETH, 2026-10-07**, replayed minute by minute from Hyperliquid 1m klines, the fill tape and 5-minute OI.

- **Trigger (window 01:56-02:01 UTC):** ETH fell from **$2,679.4** (the 01:55 close, the pre-move price) through closes of 2,674.9, 2,670.2, 2,664.6, 2,656.4 and 2,643.8. The 1-minute moves sum to **−1.34%**, past the −0.8% ETH threshold. The fill tape (`/backtesting/hl-liquidations`) shows **737 long liquidation fills worth $9.08M** in that window, against a 7-day mean of $6.3k per 5 minutes and a $1M floor. OI fell from 1,171,379 to 1,157,175 ETH (**−1.21%**). `/quant/gex/history` read `regime_score` **−0.15** (transitional, not amplify). The trade was armed.
- **Exhaustion:** the drop kept going. The 02:01 minute fell another 0.86%, with a wick to **$2,588.1**. Taker sells were $34.6M in the 02:00 minute and $73.5M in the 02:01 minute. The 02:02 and 02:03 minutes closed −0.12% and −0.32%, each resetting the clock. 02:04 closed +0.08%, so the 60-second gate cleared at 02:05.
- **Entry:** long at **$2,611.8** (02:05 open). Take profit = 2,611.8 + 0.5 × (2,679.4 − 2,611.8) = **$2,645.6** (+1.29%). Stop = 2,588.1 − 0.25 × (2,679.4 − 2,588.1) = **$2,565.3** (−1.78%). Risk 0.25% of a $50k sleeve = $125, so the notional was $125 / 1.78% ≈ **$7,000**.
- **Path:** the high over the next hour was $2,620.7 (02:20), so the target was missed. The low was $2,590.0 (02:05), so the stop was untouched. Taker flow was net buying in four of the five minutes from 02:02.
- **Exit:** time stop at 03:05, $2,614.9: **+0.12% gross**, about **0.0% net** after 9 bps of taker fees and a few bps of slippage. The flush was real, the bounce came early (inside the exhaustion wait), and the fade caught none of it.

*(Historical replay for illustration. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.2 (prior) | Long-side event study: +0.06% mean on 17 in-sample events. No evidence of edge |
| Round-trip cost | ~10-12 bps | Hyperliquid taker 4.5 bps per side plus 1-3 bps slippage on majors in a flush (more on SOL and HYPE) |
| Breakeven cost | ~12 bps | Equal to the cost: the strategy needs a real edge just to break even |
| Signal frequency | ~6 per month across four coins (long side) | Episodic and clustered: several coins fire in the same market-wide flush (all four on 2026-10-15 02:20) |
| Hold time | 5-60 minutes | The time stop binds often |
| Latency budget | under 3 seconds from event to order | Beyond that the exhaustion bounce is gone |

Events cluster in time. On 2026-10-15 at 02:20 UTC all four coins triggered together, so four "trades" were really one market bet. Count events per flush, not per coin, when judging significance.

## Capacity limits

- **Per trade:** the entry buys into a book that has just been swept. BTC and ETH can absorb $0.5-1M at a few bps, but SOL and HYPE are much thinner right after a flush.
- **Aggregate:** `capacity_usd: 1000000`. Cascade fades compete with HLP, market makers and other fade bots for the same bounce, and size beyond this turns the trader into the buyer that ends the overshoot.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Waves, not one flush (#5, regime).** A second layer of liquidations below the first. The `amplify` filter and the stop below the low limit the damage but do not prevent it.
2. **Latency and coverage (#7, operational).** A dropped connection during the trigger window, a replay ring shorter than advertised (about 14 minutes in the live test), or an order that lands seconds late. Every one of them silently changes the strategy.
3. **Venue mismatch.** The stream sees OKX, Bybit and Hyperliquid liquidations, while the rule and archive use Hyperliquid alone. Binance liquidations are not in the stream. A cascade concentrated off Hyperliquid can look small here.
4. **No edge (#1).** The two-sided study lost money, and the long-only choice is post hoc. With about 6 events a month the true sign will stay uncertain for years.
5. **Competition (#4).** HLP and professional market makers are paid to provide exactly this liquidity, and they are faster.

## Kill criteria

Retire or pause (see [[when-to-retire-a-strategy]]) on any of:

1. **Mean net return per trade below 0** after 100 trades counted from 2026-10-17.
2. **Win rate below 45%** after 100 trades.
3. **Sleeve drawdown above 10%.**
4. **Median latency above 3 seconds** from event `ts` to fill over any 20 trades.
5. **More than 2 missed windows a month**, where `stream_gapless` failed during a trigger, because the live system then is not the system tested.

## Advantages

- **Fast, specific inputs.** One subscription supplies price, forced flow and OI change within a second, where candle-based fades see them minutes late.
- **The OI gate is a real distinction.** It separates deleveraging from new positioning, which most cascade fades ignore.
- **Fully replayable core.** Each stream input has a stated archive equivalent, so the out-of-sample record can be checked against a replay of the same window.
- **Short holds.** Exposure lasts under an hour, funding is irrelevant, and the risk per trade is small.

## Disadvantages

- **No evidence yet**, and the in-sample split that picked long-only must be treated as spent.
- **Short replay history:** about 12 weeks of Hyperliquid liquidation flow.
- **Infrastructure-heavy:** an always-on SSE client, reconnect logic and a sub-3-second execution path.
- **Pro tier required** for the live stream. Free keys only get `/stream/recent` and the delayed preview.
- **Signals cluster** across coins, so diversification across the universe is much smaller than it looks.

## Sources

- [[cryptodataapi-backtesting]]: the `hl-liquidation-bars`, `hl-liquidations`, `hl-trade-flow`, `hl-funding-bars` and `/backtesting/funding` grains, coverage and start dates, and the rolling-window warning on `/backtesting/liquidations`.
- [[cryptodataapi-regimes]]: the `/quant/gex` regime states and `/quant/gex/history`.
- [[cryptodataapi-hyperliquid]]: trade-flow semantics and fees.
- [[cryptodataapi]]: the `x-streaming` extension on `/stream`.
- Live OpenAPI spec and live calls, 2026-10-17: the `/stream`, `/stream/recent` and `/stream/delayed` descriptions and parameters; a 75-second SSE capture with `since_id` replay (548 events); a 500-event `/stream/recent` pull; the delayed preview; and 5m Hyperliquid klines, 5-minute OI and 5m liquidation bars for BTC, ETH, SOL and HYPE from 2026-07-23 to 2026-10-16 (the event study). The ETH example used 1m klines, the fill tape, `hl-trade-flow` and `/quant/gex/history`.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/stream?types=price_move,liquidation,oi_delta&symbols=BTC,ETH,SOL,HYPE`: the SSE feed (Pro; keep the last `id`)
- `GET /api/v1/stream/recent?types=liquidation&symbols=ETH&limit=500`: JSON backfill and `last_id` for a gap-free reconnect
- `GET /api/v1/stream/delayed`: keyless 30-minute-delayed sample for parser tests
- `GET /api/v1/quant/gex?coin=ETH`: `regime.state` for the amplify filter

**Historical data:**
- `GET /api/v1/backtesting/hl-liquidations?coin=ETH&start=2026-10-07T01:56:00Z&end=2026-10-07T02:01:00Z`: exact Hyperliquid liquidation fills
- `GET /api/v1/backtesting/hl-liquidation-bars?coin=ETH&interval=5m&start=2026-07-23`: 5m long and short liquidation flow and the 7-day baseline
- `GET /api/v1/backtesting/funding?symbol=ETH&exchange=hyperliquid&start=2026-07-23`: 5-minute `open_interest` for the OI gate
- `GET /api/v1/backtesting/klines?symbol=ETH&exchange=hyperliquid&interval=1m&start=2026-07-23`: 1m price for the trigger and exhaustion gates
- `GET /api/v1/quant/gex/history?symbol=ETH&from=2026-09-09T00:00:00Z`: hourly `regime_score`

```bash
curl -N -H "X-API-Key: $CDA_KEY" -H "Accept: text/event-stream" \
  "https://cryptodataapi.com/api/v1/stream?types=price_move,liquidation,oi_delta&symbols=BTC,ETH,SOL,HYPE"
```

Endpoint catalogs: [[cryptodataapi-backtesting]], [[cryptodataapi-hyperliquid]], [[cryptodataapi-regimes]].

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can test and run this page as follows:

- **Test the parser first:** call `/stream/delayed` (keyless) and `/stream/recent?limit=500`, then check that your 300-second window logic reproduces the price, liquidation and OI sums by hand before opening the live stream.
- **Signal:** hold one `/stream` connection filtered to `price_move,liquidation,oi_delta` on the four coins. Sum each type per coin over 300 seconds, counting only `venue: hyperliquid` liquidations with `side: long`.
- **Regime gate:** refresh `/quant/gex?coin=` `regime.state` every few minutes, and never arm a coin in `amplify`.
- **Backtest:** rebuild each event type from its archive (table above). Use the `hl-liquidations` fill tape for exact 300-second windows, and 5-minute `open_interest` from `/backtesting/funding`, not `hl-funding-bars`. Report results per flush, not per coin.
- **Execution:** after any disconnect, reconnect with `since_id` and rebuild the window before trading. If the gap is older than the ring (about 14 minutes when tested), skip that window.

## Related

- [[liquidation-cascade-fade]]: the canonical 15-minute cascade fade; this page adds the OI-falling gate and minute-level stream timing
- [[off-hours-liquidation-playbook]]: session-conditioned cascade fade
- [[oi-flush-reversion]]: OI purge over days; this page uses it over minutes
- [[cascade-detection-signals]]: the detection primitives
- [[liquidation-depth-cascade-sizing]]: book-depth sizing for cascade fades
- [[cross-venue-cascade-dislocation]]: the cross-venue spread version
- [[hlp-cascade-alongside-playbook]]: being paid by the same cascades as a liquidity provider
- [[post-liquidation-rebound]], [[long-liquidation-cascade]]: Hyperliquid basket views of the flush and recovery
- [[volume-oi-conditioned-reversal]], [[oi-price-exhaustion]]: other OI-conditioned reversal ideas
- [[event-driven-backtesting]]: replaying event streams honestly
- [[liquidation-density-magnet]], [[exchange-flow-spike-reaction]]: the other two pages built on the 2026-10 data releases
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]]
