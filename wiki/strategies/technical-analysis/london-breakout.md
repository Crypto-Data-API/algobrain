---
title: "London Breakout Strategy (Crypto)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [crypto, session-trading, volatility-breakout, breakout, intraday, technical-analysis, asia-session, london-open]
aliases: ["London Breakout", "Crypto London Breakout", "Asia Range Breakout", "Session Breakout", "Crypto Session Breakout"]
strategy_type: technical
timeframe: intraday
markets: [crypto]
complexity: beginner
backtest_status: untested

# Edge characterization
edge_source: [structural, behavioral]
edge_mechanism: "The Asia-only hours are crypto's thinnest, so BTC/ETH coil into a narrow range; when the European/London session opens and, more powerfully, when US macro and cash-equity flow arrives, deeper participation and higher volatility break that range in one direction — but obvious range edges also attract stop-hunts and liquidation wicks that fake the break before the real move."

# Data and infrastructure requirements
data_required: [ohlcv-intraday, session-times, atr, funding-rates, open-interest, liquidations]
min_capital_usd: 1000
capacity_usd: 10000000
crowding_risk: medium

# Performance expectations (net of fees and slippage)
expected_sharpe: 0.3
expected_max_drawdown: 0.25
breakeven_cost_bps: 15

# Decay history
decay_evidence: "Session-breakout edges are widely known and mechanical, so they are easily front-run and faded. Crypto's session structure is also weaker and more diffuse than forex's because the market is 24/7 and, post-spot-ETF, an increasing share of BTC price discovery has migrated into US cash-equity hours (13:30-20:00 UTC) rather than the London open — so a US-session variant now often dominates the classic London-open version."

# Retirement conditions
kill_criteria: |
  - false-break rate on filtered ranges rises materially over a 40-trade sample
  - the session no longer produces a directional expansion (intraday seasonality has shifted)
  - realised slippage/spread at the session open consistently exceeds planned per-trade risk

related: ["[[opening-range-breakout]]", "[[volatility-breakout]]", "[[breakout-trading]]", "[[supply-demand-zones]]", "[[atr]]", "[[funding-rate]]", "[[open-interest]]", "[[liquidation]]", "[[volatility-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[cryptodataapi]]"]
---

# London Breakout Strategy (Crypto)

The **London Breakout**, adapted to crypto, is a session-based [[volatility-breakout]] method that trades the directional expansion which tends to follow the quiet Asia-only hours. Although crypto trades 24/7, it has a pronounced intraday *seasonality*: the Asia session (roughly **00:00-07:00 UTC**) is the market's thinnest window for BTC and ETH, so price often coils into a narrow consolidation range. When the **European/London session opens (~07:00-08:00 UTC)** — and, more powerfully in the post-ETF era, when **US macro data and cash-equity flow arrive (13:30-20:00 UTC)** — deeper participation and higher volatility break that range, frequently setting the tone for the rest of the day. The mechanics are simple: mark the Asia-session high and low, then trade the breakout in whichever direction the London/US session pushes price, with stops on the opposite side of the range. It works best on **deep-book majors (BTC, ETH, top perps)**; thin alts produce clean-looking ranges that are trivially swept.

## Edge source

Mapping to the six categories in [[edge-taxonomy]]:

1. **Structural.** Crypto liquidity is deeply uneven across the 24-hour cycle. During Asia-only hours, US and European institutional desks are dark, market-maker inventory is smaller, and volume is low, so the range compresses. Session transitions inject a step-change in participation — this volatility *seasonality* is a real, measurable structural feature (see [[volatility-regime]]), and it is the defensible core of the strategy.
2. **Behavioural.** The Asia-range high and low are obvious, mechanical levels that thousands of chart-watchers mark identically. That makes them reference points other participants anchor to — but it also makes them **stop-hunt targets**: price frequently spikes just past the range edge to trip the clustered buy/sell stops and a [[liquidation]] pocket, then reverses (the "judas swing" / false break) before the *real* directional move. The trader is paid for correctly distinguishing the fake break from the real one.

There is **no informational or latency edge** for a discretionary trader. The structural half (session volatility) is real; the behavioural half (which break is real) is where the difficulty and most of the losses live.

## Why this edge exists

The 24/7 crypto market inherited a session rhythm from the traditional venues its price is correlated with. US cash-equity hours host the deepest books, the spot-ETF creation/redemption flow, and the macro reaction function (CPI, FOMC, jobs); the Asia-only window hosts the least of all three. A day's worth of accumulated overnight orders and positioning is compressed into a quiet range and then released when the deeper sessions arrive. Two things follow:

- **Range expansion is real.** Volatility genuinely rises at the London and US opens relative to the Asia lull — that part is structural and backtestable.
- **The first break is often a trap.** Because the range edges are obvious, the *first* push past them is frequently an engineered sweep of clustered stops/liquidations rather than the real move. The real directional expansion often begins only after that sweep reverses.

The trader's job is to filter for a range worth trading, then trade the break that *holds* rather than the one that merely tags the level.

## Session structure (UTC)

Crypto has no cash close, so all times are UTC and the "range" is a rolling window, not an exchange session:

| Window | UTC | Role |
|--------|-----|------|
| **Asia (range formation)** | 00:00-07:00 | Thinnest liquidity; BTC/ETH coil into a narrow range. Mark the high and low. |
| **London open (breakout trigger)** | 07:00-08:00 | First major liquidity injection; the classic breakout window. |
| **US macro / cash-equity open** | 13:30-14:30 | The strongest expansion window post-ETF; macro prints land here. |
| **Trade window** | 07:00-16:00 | Most of the day's directional move. |
| **Wind-down** | after ~20:00 | US session fades; avoid initiating new session-breakout trades. |

The **US-open variant** — mark the London/pre-US range, trade the break at the 13:30 UTC macro/equity open — is now often the higher-quality version for BTC/ETH because that is where post-ETF price discovery concentrates.

## Rules and signals

### Range and filter
1. At 07:00 UTC (London) or before 13:30 UTC (US variant), mark the **Asia/pre-session high and low** on the 15-minute or 1-hour chart. Add a **buffer** — in crypto use a **% of price or an [[atr]] fraction**, never a fixed pip count (e.g. buffer ≈ 0.15-0.25% for BTC, or 0.25× the session ATR).
2. **Range-size filter (as a % of price / ATR).** Trade only "Goldilocks" ranges: skip if the range is *too wide* (the expansion already happened) or *too tight* (false-break prone). A workable BTC guide is a session range of ~0.5-1.5% of price; calibrate per asset with [[atr]].
3. **Avoid high-impact macro *inside* the setup.** If a major print (CPI, FOMC, NFP, a scheduled ETF or regulatory decision) lands during the trade window, either skip or trade only *after* the spike resolves — these now move crypto hard via its equity/macro correlation.
4. **Liquidity/venue filter.** Only run this on deep-book majors (BTC, ETH, top-OI perps). Thin alts and weekend ranges produce clean-looking boxes that are cheap to sweep.

### Entry
5. **Stop-entry orders:** buy-stop at range-high + buffer, sell-stop at range-low - buffer; when one fills, cancel the other (OCO).
6. **Confirmation variant (higher hit rate):** instead of the raw stop, wait for a 15m/1h *close* beyond the range edge, or re-enter on the retest after an initial sweep-and-reclaim — this filters most judas-swing fakeouts.

### Stop-loss
7. Place the protective stop on the **opposite side of the range** (or its midpoint for a tighter stop), with a buffer *beyond* the likely stop-hunt wick. Size the stop with [[atr]], not a fixed distance.

### Targets
8. Target **1:2 reward-to-risk** as the base case; measured-move (range height projected from the break) is a common objective.
9. **Partial at 1:1**, move stop to breakeven, trail the remainder behind intraday structure or a moving average.
10. **Time-based exit:** if the trade has not worked by the late US session (~16:00-18:00 UTC), close it — the day's directional momentum fades and holding into the thin Asia hours re-exposes you to a low-liquidity reversal.

### Derivatives overlay (crypto edge)
11. A break *with* rising [[open-interest]] and neutral-to-supportive [[funding-rate]] is fresh directional positioning — trust it. A break on flat/falling OI, or one that immediately spikes funding, is more likely a squeeze/sweep that reverts.

## Implementation pseudocode

```python
# Crypto session-breakout (illustrative; not investment advice). All times UTC.
def session_breakout(bars_15m, session, deriv, atr):
    rng = asia_range(bars_15m, start="00:00", end="07:00")   # or pre-US window
    width_pct = (rng.high - rng.low) / rng.mid
    if not (0.005 <= width_pct <= 0.015):                    # BTC guide; calibrate per asset
        return None                                          # range too tight or too wide
    if macro_event_in_window(session):
        return None                                          # stand aside around CPI/FOMC/ETF

    buf = max(0.0015 * rng.mid, 0.25 * atr)                  # % or ATR buffer, never fixed ticks

    signal = orco_stops(buy=rng.high + buf, sell=rng.low - buf)   # OCO stop-entry
    fill = wait_for_fill_or_close_beyond(signal, confirm="15m_close")

    if fill is None:
        return None
    # crypto overlay: trust breaks backed by fresh OI, fade squeeze-only pushes
    if deriv["oi_change"] <= 0 or abs(deriv["funding_spike"]) > FUNDING_SPIKE_MAX:
        conviction = "low"                                   # likely sweep -> smaller size / skip
    else:
        conviction = "normal"

    stop   = rng.low - buf if fill.side == "buy" else rng.high + buf
    target = fill.price + 2 * abs(fill.price - stop) * fill.dir
    return Order(fill.side, fill.price, stop, target,
                 partial_at=fill.price + abs(fill.price - stop) * fill.dir,
                 time_exit="16:00", conviction=conviction)
```

## Indicators / data used

- **Asia/pre-session high and low** — the range whose break is traded.
- **Session times in UTC** — London (~07:00) and US macro/equity (13:30) expansion windows.
- **[[atr]]** — range-size filter, buffer, and stop sizing (replaces the forex "pip" units entirely).
- **[[open-interest]] and [[funding-rate]]** — separate fresh directional breaks from squeeze-driven fakeouts.
- **[[liquidation]] clusters** — where the sweep pocket sits just beyond the range edge.
- **[[volatility-regime]]** — is the market in a compressed (breakout-favourable) or already-expanding regime?
- **Macro calendar** — CPI/FOMC/NFP/ETF decisions that now move crypto through its correlation.

## Example trade

**Asset:** BTC/USDT, 15-minute chart (illustrative, not a recorded trade).

1. Asia session (00:00-07:00 UTC): BTC ranges between **$61,200 (high)** and **$60,600 (low)** — a range of $600, ~1.0% of price. Within the workable band.
2. Buffer = 0.15% ≈ $92. Place buy-stop at **$61,292** and sell-stop at **$60,508** (OCO).
3. At 07:20 UTC the London open drives BTC up; it tags $61,300, trips buy stops, then **wicks straight back into the range to $60,900** — a classic judas swing that fills the naive buy-stop and stops it out. (The confirmation variant would have avoided this: no 15m *close* held above the range.)
4. The confirming trader waits. At 13:30 UTC a soft US CPI print lands; BTC breaks the range high again, this time **closing** the 15m candle at **$61,450** with **OI building** and funding neutral. Enter long on the retest at **$61,350**.
5. Stop below the range with a buffer: **$60,450** (risk ~$900, ~1.5%). Target 1:2 = **$63,150**.
6. Take 50% at **$62,250** (1:1), move stop to breakeven. BTC trends through the US session to **$63,000** by 16:00 UTC; close the remainder.
7. **Result:** first half +$900, second half +$1,650. Blended ~+$1,275 on $900 risk ≈ **1.4:1**. The confirmation filter turned a stop-out (the raw judas swing) into a winner — the single most important adaptation for crypto.

## Performance characteristics

Session breakout is a low-Sharpe, mechanical intraday edge whose profitability lives almost entirely in the false-break filter:

| Metric | Value | Note |
|---|---|---|
| Net Sharpe (target) | ~0.3 | Modest; sensitive to the false-break rate and slippage. |
| Win rate | 35-45% raw stop-entry; higher with close-confirmation | Positive expectancy only via 1:2+ payoff. |
| Max drawdown | 20-25% | Clusters in range-bound days with no clean expansion. |
| Best regime | compressed volatility → expansion (see [[volatility-regime]]) | Worst in already-trending or dead-flat regimes. |
| Breakeven cost budget | ~15 bps round trip | Spot/perp taker + session-open spread widening. |

Backtests are highly sensitive to the buffer, the range-size filter, and whether entry is raw-stop or close-confirmed — codify all three or the result is unstable across periods.

## Capacity limits

Bounded by intraday book depth at the moment of the break. On BTC/ETH majors, an individual can work **$100k-$10M** per session before the stop-entry itself moves the book at the range edge (exactly where liquidity thins). On thin alts, capacity is tiny — buy-stops above the range high sit precisely where the book is emptiest, so size both moves the market and invites the sweep. As a once-per-session, low-frequency method it is naturally higher-capacity but slow to validate statistically.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **False breaks / stop-hunts (dominant loss mode, crypto-acute).** Price tags the obvious range edge to trip stops and a [[liquidation]] pocket, then reverses. Raw stop-entry with a small buffer bleeds continuously; the close-confirmation filter is the primary defence.
2. **No expansion (wrong regime).** On a dead, range-bound day the break never comes and every entry chops. Filtering by [[volatility-regime]] (trade only from compressed regimes) mitigates this.
3. **Macro whipsaw.** A CPI/FOMC/ETF headline inside the trade window produces a violent two-sided spike that stops out both directions. Trading around these events, not into them, is essential.
4. **Session drift (regime change).** Post-ETF, the London-open expansion has weakened relative to the US-open window; a strategy still keyed to 07:00 UTC decays as price discovery migrates to 13:30 UTC.
5. **Weekend / thin-alt ranges.** Low-liquidity ranges look clean but are the easiest to sweep — false-break rates spike.
6. **Crowding.** The setup is mechanical and widely taught, so the obvious stop placements are consensus liquidity for the very sweeps that fake the break.

## Kill criteria

Pause or revise if: the false-break rate on filtered ranges rises materially over a 40-trade sample; the target session stops producing a directional expansion (intraday seasonality has shifted — re-fit to the US window); or realised slippage/spread at the session open consistently exceeds the planned per-trade risk. See [[when-to-retire-a-strategy]].

## Advantages

- Simple, mechanical rules — mark the range, place OCO stops, manage, done by the late US session; suits part-time traders.
- Exploits a real, backtestable structural feature (crypto intraday volatility seasonality).
- Objective structure — the range edges, buffer, and opposite side make stops and targets concrete.
- The crypto derivatives overlay (OI/funding/liquidations) adds a genuine fresh-vs-squeeze filter unavailable in the original forex version.

## Disadvantages

- **False breaks are the norm, not the exception** — without a close-confirmation or sweep-reclaim filter, the raw system bleeds.
- Low Sharpe and regime-dependent; needs the volatility-regime and macro-calendar filters to be viable.
- Session structure is weaker and more diffuse in 24/7 crypto than in forex, and is drifting toward US hours post-ETF.
- Mechanical and widely known, so the obvious stops are crowded and easily targeted.
- Only reliable on deep-book majors; thin alts and weekend ranges are traps.

## Getting the Data (CryptoDataAPI)

Session breakout needs intraday OHLCV to build the range, depth to judge whether the break is real, volatility-regime context to decide *if* to trade, and derivatives/liquidation data to filter squeeze-driven fakeouts. See [[cryptodataapi-market-data]], [[cryptodataapi-regimes]], and [[cryptodataapi-derivatives]].

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=500` — intraday OHLCV to mark the Asia/pre-session range.
- `GET /api/v1/liquidity/depth/BTC` — depth/spread at the range edges; flags thin books that will fake the break.
- `GET /api/v1/volatility/regime` — compressed vs expanding regime; trade breakouts out of compression.
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI building on the break = fresh directional flow, not a squeeze.
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — a funding spike on the break warns of a sweep.
- `GET /api/v1/market-intelligence/liquidations` — the forced-order pocket sitting just past the range edge.

**Historical data (backtest the session and the filters):**
- `GET /api/v1/backtesting/klines` — full intraday archive from 2020 to test range-size filters and the London-vs-US session by hour.

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=500"
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/volatility/regime"
```

Auth: `X-API-Key` header. Full market-data catalog: [[cryptodataapi-market-data]].

## Related

- [[opening-range-breakout]] — the same range-break concept applied to any session open; crypto's session-breakout is its 24/7 sibling.
- [[volatility-breakout]] — session breakout is a specific application of the general volatility-breakout framework.
- [[breakout-trading]] — the parent breakout family.
- [[supply-demand-zones]] — zones formed in the Asia range can reinforce or invalidate the break direction.
- [[volatility-regime]] — the filter that decides whether a breakout is worth taking.
- [[funding-rate]] / [[open-interest]] / [[liquidation]] — the derivatives overlay separating real breaks from sweeps.
- [[atr]] — the crypto-native unit for the range filter, buffer, and stops.
- [[edge-taxonomy]] — where this strategy sits among the edge categories.
- [[failure-modes]] — the catalog this strategy's kill criteria draw from.

## Sources

- Original forex "London Breakout" session-trading literature — the Asia-range/session-open breakout template adapted here for 24/7 crypto.
- Public exchange documentation (Binance, Coinbase, Hyperliquid) — 24/7 trading and the intraday liquidity/volatility seasonality that gives crypto its session structure.
- CryptoDataAPI volatility-regime methodology ([[cryptodataapi-regimes]]) — compressed/expanding regime classification used as the entry filter.
