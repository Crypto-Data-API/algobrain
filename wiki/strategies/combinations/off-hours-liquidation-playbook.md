---
title: "Off-Hours Liquidation Playbook"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, liquidations, mean-reversion, market-microstructure, perpetual-futures, crypto, quantitative, behavioral-finance]
aliases: ["Session-Aware Cascade Fade", "Weekend Liquidation Fade", "Thin-Book Cascade Playbook", "Off-Hours Cascade Fade"]
strategy_type: hybrid
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Forced liquidation cascades in thin off-hours and weekend books overshoot proportionally further per dollar of forced flow than cascades during peak liquidity hours; the playbook adapts the cascade-fade entry trigger, minimum cascade size, position sizing, and slippage budget by session window, concentrating risk when the reversion edge is amplified by thin liquidity rather than applying the same parameters in all sessions."

data_required: [liquidation-feed, ohlcv-15m, ohlcv-1h, mark-price, order-book-l2, funding-rates]
min_capital_usd: 5000
capacity_usd: 1000000
crowding_risk: low

expected_sharpe: 1.1
expected_max_drawdown: 0.40
breakeven_cost_bps: 30

decay_evidence: "Liquidation cascade dynamics are not stationary: exchanges have progressively tightened insurance funds and introduced partial liquidation, reducing the depth and duration of cascades (compare 2020-03-12 to 2025-10-10 — faster recovery, shallower absolute move). Weekend thinness persists post-ETF era per crypto-weekday-weekend-etf-era but the magnitude of the edge is smaller than pre-2024. No published study on session-conditioning of cascade-fade performance."

kill_criteria: |
  - strategy drawdown > 35% from high-water mark (cascade fade already has a wide drawdown budget; this is a hard stop)
  - off-hours cascade fade win rate falls below 45% on minimum 30 signals in any 90-day window (fade dynamics have changed — exchanges may have tightened parameters)
  - average reversion magnitude drops below 0.8× the entry-trigger move size for 20+ consecutive signals (overshoot no longer occurring; fundamentals of the edge gone)
  - session classification is no longer predictive of cascade depth: t-test on post-cascade reversion (off-hours vs peak hours) yields p > 0.10 over 50+ signals (session overlay is not adding information)

related: ["[[liquidation-cascade-fade]]", "[[long-liquidation-cascade]]", "[[post-liquidation-rebound]]", "[[session-overlap-momentum]]", "[[crypto-weekday-weekend-etf-era]]", "[[funding-flush-reversal]]", "[[contrarian-extremes]]", "[[market-microstructure]]", "[[liquidations]]", "[[perpetual-futures]]", "[[order-flow]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Off-Hours Liquidation Playbook

The off-hours liquidation playbook is the [[liquidation-cascade-fade]] strategy with **session-conditional parameter adaptation**: it applies different entry thresholds, minimum cascade sizes, position sizing multipliers, and slippage assumptions depending on whether the cascade occurs during a US/EU peak-liquidity session, an Asian off-peak session, overnight (00:00–07:00 UTC), or a weekend window. The primitive edge is liquidation-cascade mean reversion — forced selling overshoots fair value and the fade captures the snapback. The overlay is the empirical observation, documented in [[crypto-weekday-weekend-etf-era]], that thin-book off-hours cascades travel *further per dollar of forced flow* than peak-hours cascades, creating a larger reversion opportunity but requiring adjusted risk parameters.

This is the **session-conditioning layer on the cascade primitives** and is explicitly not a replacement for them:
- [[liquidation-cascade-fade]] — the canonical cascade-fade strategy with parameters calibrated for all sessions. This page *extends* that strategy, not replaces it.
- [[long-liquidation-cascade]] — the Hyperliquid-basket version focused on concentrated long-cascade events. This page's session-conditioning applies to that setup as well.
- [[post-liquidation-rebound]] — the rebound strategy focused on the recovery phase (hours after the cascade). This page focuses on the *entry* mechanics at the cascade trough, not the extended recovery.
- [[session-overlap-momentum]] — the session-overlap page documents the liquidity-driven momentum at London-NY overlap; this page uses the same session framework but for the *opposite* strategy: cascade-fade mean reversion in thin sessions rather than overlap-driven momentum.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — the liquidation cascade itself is driven by stop-loss and liquidation engine behaviour: mechanical, non-economic forced selling into a book that has lost its discretionary bid. This is the same behavioural overshoot as [[liquidation-cascade-fade]]. The session overlay adds a *second* behavioural layer: in thin off-hours books, discretionary market-makers and institutional providers are offline or running reduced risk limits, exacerbating the overshoot. The fade provider absorbs the panic that has been amplified by the thin book.
- **Structural** — the perpetual futures mechanism creates a structurally thin off-hours book. Post-ETF era, large institutional spot liquidity has a US-hour bias ([[crypto-weekday-weekend-etf-era]]): CME futures are closed on weekends; US desk liquidity withdraws outside NYSE hours. This is a structural, recurring liquidity cycle, not a random state.
- **Risk-bearing** — the session-aware fade provider is absorbing the exact risk that peak-hours providers are physically absent for. The premium for providing that liquidity in the thin window is the additional overshoot: the bounce from a 4% overnight cascade is often larger than from a 4% midday cascade because the midday cascade already attracted competing fade providers at shallower levels.

## Why this edge exists

**Three reinforcing mechanisms make off-hours cascades bigger per dollar of flow:**

1. **Liquidity provider absence.** During US/EU trading hours, professional market makers, HFT firms, and algorithmic spread providers maintain tight books. During Asian overnight (00:00–07:00 UTC) and weekends, many of these participants operate with reduced inventory limits or are absent entirely. The same $50M of liquidation flow that moves BTC 2% at 2pm ET moves it 4-6% at 2am UTC — the book is half-depth or less.

2. **Cascade self-amplification in thin books.** A cascade is self-reinforcing: liquidations lower the mark price, which breaches more liquidation levels, which generates more market sells. In a thin book, each successive liquidation level is hit faster because there are fewer resting bids to absorb the flow. The acceleration of the cascade in thin sessions means the overshoot is not only proportionally larger — it arrives faster, creating a sharper V-shaped recovery opportunity.

3. **Weekend/overnight: no new directional catalysts.** Cascades in peak-liquidity sessions are sometimes continuation moves (macro news drives the initial break *and* the liquidations; recovery is slow). Cascades in thin overnight sessions are rarely triggered by new fundamental information — they are predominantly leverage-flush events from a preceding session's overextension. Without a new fundamental catalyst, the overshooting price is more likely to revert to the prior session's fair value, supporting a higher probability of the fade working.

**Who is on the other side:** the forced-liquidation engine and stop-triggering participant who must sell at the market at the exact moment the book is thinnest; and the momentum-follower who piles short into the cascade, expecting a trend, in a session where the cascade is driven by mechanics rather than fundamentals.

## Null hypothesis

Under the null, cascade-fade performance is **not session-dependent**: cascades of equivalent size, trigger conditions, and pre-cascade OI structure produce the same distribution of subsequent reversion — regardless of whether they occur at peak-liquidity or thin-liquidity hours. Session conditioning adds no information; using different parameters per session only introduces complexity without improving performance.

Specifically:
- Average reversion magnitude (high-to-close over next 2 hours) should not differ across session bins for equivalent cascade sizes.
- Win rate of the fade should not be higher in off-hours sessions than peak-hours sessions, after controlling for cascade size.
- Tighter bid-ask spreads in peak sessions should be offset by smaller overshoot, leaving net fade P&L equivalent.

Currently not rejected (`backtest_status: untested`). Testable prediction: classify all cascade events (liquidation volume ≥ 3× 24h average within 15 minutes, price drop ≥ 2%) by session; run the cascade-fade P&L separately per session bucket; predict off-hours sessions show both larger absolute reversion and higher Sharpe than peak-hours sessions.

## Rules

### Session classification

Define four session windows (UTC):

| Window | UTC Range | Classification | Liquidity Profile |
|---|---|---|---|
| **US Peak** | 13:30–22:00 | Peak | NYSE/CME open; deepest books; institutional active |
| **EU Peak** | 07:00–13:30 | Peak | LSE/Euronext open; moderate depth; EU desks active |
| **Asia/Overnight** | 22:00–07:00 | Off-peak | Thin; US/EU providers offline; retail-dominant |
| **Weekend** | Fri 22:00–Mon 07:00 UTC | Weekend | Thinnest; ETF-era structural liquidity withdrawal |

*Note: these windows are approximate and may shift seasonally. Monitor Bollinger Bandwidth and book depth at 15m resolution to confirm the current liquidity state; do not rely on the clock alone.*

### Session-adjusted parameters

| Parameter | Peak sessions | Asia/Overnight | Weekend |
|---|---|---|---|
| Min cascade size (liquidation spike) | ≥ 5× 24h avg / 15m window | ≥ 3× 24h avg | ≥ 2.5× 24h avg |
| Min price drop to trigger | ≥ 2.5% in 15 min | ≥ 2.0% in 15 min | ≥ 1.8% in 15 min |
| CVD confirmation threshold | CVD must be showing sell exhaustion (≥ 3 min of flattening) | ≥ 2 min | ≥ 1.5 min |
| Entry size multiplier | 0.8× base | 1.0× base | 1.2× base |
| Target reversion | 1.0–1.5% above cascade low | 1.5–2.5% | 2.0–3.5% |
| Time stop | 45 min | 60 min | 90 min |
| Stop loss (from entry) | 1.5% | 1.5% | 2.0% |
| Slippage budget (entry) | 8–15 bps | 15–25 bps | 20–35 bps |
| Max position size | 1.5% of sleeve | 1.0% of sleeve | 0.75% of sleeve |

**Rationale for parameter adjustments:**
- Lower minimum cascade size in off-hours: a 2× spike in thin hours represents the same mechanical-overshoot dynamic as a 5× spike in peak hours because the baseline book depth is lower.
- Larger entry size in Asia/overnight vs peak: the overshoot is bigger, the competition fewer — the expected value of the fade is higher, warranting more capital.
- *Smaller* entry size on weekends: weekend cascades have the largest expected overshoot but also the highest slippage on exit; the sizing is reduced to compensate for exit friction.
- Wider stop loss on weekends: in thin weekend books, a 1.5% stop loss can be triggered by a single large market order; extending to 2% avoids stop-hunting while keeping overall risk bounded by the smaller size.

### Entry logic (extends [[liquidation-cascade-fade]])

The cascade-fade entry is unchanged from [[liquidation-cascade-fade]]:
1. Liquidation volume spike ≥ session threshold (see table).
2. Mark price drop ≥ session threshold.
3. CVD shows aggressive selling beginning to flatten (session-adjusted minimum time).
4. Entry: limit order at 0.2–0.3% above current mark price (improving fill, accepting partial fills).

**New session-layer additions:**
5. **Session classification confirmed:** verify the current UTC time falls in the appropriate session window.
6. **Book depth check:** order-book depth at ±1% must be below the 30th percentile of its 24h history — confirms the book is genuinely thin, not just classified as off-hours. A peak-hours cascade with temporary depth withdrawal should be treated as off-hours for parameter purposes.
7. **Weekend holiday expansion:** major US/EU public holidays (Christmas, Thanksgiving, NY-area holidays) expand the "weekend" parameter set by ±12 hours around the holiday date.

### Exit logic

Same as [[liquidation-cascade-fade]]:
1. Profit target (session-adjusted reversion range from table).
2. Time stop (session-adjusted).
3. Stop loss (session-adjusted).
4. Funding-state check: if funding spikes deeply negative mid-hold (shorts flooding in), reduce exposure — the cascade is attracting momentum sellers, not just triggering a technical flush.

## Implementation pseudocode

```python
# off_hours_liquidation_playbook.py
# Session-aware extension of liquidation-cascade-fade

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

# ---- session windows (UTC hour) ----
US_PEAK_START, US_PEAK_END   = 13.5, 22.0   # 13:30–22:00 UTC
EU_PEAK_START, EU_PEAK_END   = 7.0,  13.5   # 07:00–13:30 UTC
WEEKEND_START_FRI_UTC        = 22.0          # Fri 22:00 UTC
WEEKEND_END_MON_UTC          = 7.0           # Mon 07:00 UTC

@dataclass
class SessionParams:
    name: str
    min_liq_spike_mult: float   # minimum liquidation volume multiplier vs 24h avg
    min_price_drop_pct: float   # minimum price drop in 15m window
    cvd_flatten_min:    float   # minutes CVD must be flattening before entry
    size_multiplier:    float   # vs base position size
    target_reversion_pct: tuple # (low, high) in %
    time_stop_min:      int
    stop_loss_pct:      float
    slippage_budget_bps:float
    max_size_pct:       float   # % of sleeve

PARAMS = {
    "peak":    SessionParams("peak",    5.0, 2.5, 3.0, 0.8, (1.0, 1.5), 45, 1.5, 10, 1.5),
    "offpeak": SessionParams("offpeak", 3.0, 2.0, 2.0, 1.0, (1.5, 2.5), 60, 1.5, 20, 1.0),
    "weekend": SessionParams("weekend", 2.5, 1.8, 1.5, 1.2, (2.0, 3.5), 90, 2.0, 28, 0.75),
}

def classify_session(dt: datetime) -> str:
    h = dt.hour + dt.minute / 60.0
    wd = dt.weekday()  # 0=Mon ... 4=Fri, 5=Sat, 6=Sun
    # weekend window: Fri 22:00 → Mon 07:00
    if wd == 5 or wd == 6:
        return "weekend"
    if wd == 4 and h >= WEEKEND_START_FRI_UTC:
        return "weekend"
    if wd == 0 and h < WEEKEND_END_MON_UTC:
        return "weekend"
    # peak windows
    if EU_PEAK_START <= h < EU_PEAK_START + (EU_PEAK_END - EU_PEAK_START):
        return "peak"
    if US_PEAK_START <= h < US_PEAK_END:
        return "peak"
    return "offpeak"

def book_depth_thin(order_book_depth: float, depth_pctile_24h: float) -> bool:
    """True if current depth is in the bottom 30th percentile of 24h history."""
    return depth_pctile_24h < 30.0

@dataclass
class CascadeSignal:
    liq_spike_mult: float   # liquidation volume / 24h avg
    price_drop_15m_pct: float
    cvd_flatten_minutes: float
    funding_8h: float
    book_depth_pctile: float

def cascade_qualifies(sig: CascadeSignal, params: SessionParams) -> bool:
    return (sig.liq_spike_mult       >= params.min_liq_spike_mult and
            sig.price_drop_15m_pct   >= params.min_price_drop_pct and
            sig.cvd_flatten_minutes  >= params.cvd_flatten_min)

def off_hours_cascade_decision(sig: CascadeSignal, book: dict, dt: datetime) -> dict:
    if book.get("sleeve_drawdown", 0) > 0.35:
        return {"action": "FLAT", "reason": "drawdown kill"}

    session = classify_session(dt)
    # upgrade to off-peak params if book is thin even during classified peak
    if session == "peak" and book_depth_thin(None, sig.book_depth_pctile):
        session = "offpeak"

    params = PARAMS[session]

    if not cascade_qualifies(sig, params):
        return {"action": "WAIT", "session": session,
                "reason": "cascade thresholds not met for this session"}

    base_size = book["sleeve_capital"] * 0.005  # 0.5% base
    notional  = min(base_size * params.size_multiplier,
                    book["sleeve_capital"] * params.max_size_pct / 100)

    return {
        "action":       "FADE_LONG",
        "session":      session,
        "notional":     notional,
        "target_pct":   params.target_reversion_pct[0],
        "stop_pct":     params.stop_loss_pct,
        "time_stop_min":params.time_stop_min,
        "slippage_bps": params.slippage_budget_bps,
        "note": (f"session={session}, liq_mult={sig.liq_spike_mult:.1f}x, "
                 f"drop={sig.price_drop_15m_pct:.2f}%, "
                 f"size_mult={params.size_multiplier}x"),
    }
```

The production system adds: real-time liquidation feed from CryptoDataAPI; L2 order-book depth monitoring; session classification as a continuous variable (not just 3 buckets) via a rolling-window depth percentile; and a daily attribution report separating session-bucket P&L.

## Indicators / data used

- **Liquidation volume (real-time, cross-exchange)** — `/api/v1/market-intelligence/liquidations` and `/api/v1/market-intelligence/liquidations/by-exchange`; the primary cascade trigger.
- **[[order-flow]] / CVD (tick or 1-min aggregation)** — confirms forced selling is exhausting; required for entry gating.
- **Order-book L2 depth** — `/api/v1/liquidity/depth` or exchange-native L2 feed; used to classify effective session liquidity (a peak-hours cascade with thin depth is treated as off-hours).
- **[[funding-rate]] (8h)** — monitors mid-hold for momentum-seller flooding (deeply negative funding mid-trade signals cascade continuation, not reversion).
- **Mark price (real-time)** — trigger price and exit level measurement.
- **Session window (UTC clock)** — classification of the session bucket; cross-referenced with book depth for the hybrid thin-peak classification.

## Example trade

**Setup — Weekend cascade (illustrative):**

- Asset: SOL-PERP on Hyperliquid.
- Time: Saturday 04:17 UTC (weekend session bucket).
- SOL spot: $145.00 (prior close).
- Cascade trigger (04:17 UTC): SOL drops 2.2% in 13 minutes to $141.82. Liquidation feed: 2.8× the 24h average per 15m window — exceeds the 2.5× weekend threshold. Book depth: 22nd percentile of 24h history (thin book confirmed). CVD: showed aggressive selling for 90 seconds, now flattening over the last 1.6 minutes — exceeds 1.5 min weekend threshold.
- Sleeve: $20,000. Base size: 0.5% = $100. Weekend multiplier 1.2×: $120 notional. Max size cap: 0.75% = $150. Final size: **$120 notional**.
- Entry: limit at $141.95 (0.09% above current mark, within 20-35 bps slippage budget). Filled.
- Stop: 2.0% below entry = $139.12. Target: 2.0–3.5% reversion → $144.78–$146.90.

**Hold (43 minutes):** SOL recovers to $144.20 (+1.6% from entry). Target midpoint passed at 2.0% reversion ($144.78 missed by a tick; close at $144.20 for clean exit).

**Net P&L:** Entry $141.95 → exit $144.20. Gain: +$2.25 / $141.95 × $120 = **+$1.90 on $120 deployed** (+1.6% in 43 minutes). Slippage: entry taker $0.06 + exit taker $0.06 = $0.12. **Net: +$1.78**.

**Comparison — if treated as peak-session:** peak parameters require ≥ 5× liquidation spike (this was 2.8× — *would not have triggered*). Session conditioning caused this trade to exist at all.

**Risk exposure:** stop at $139.12 would have cost: $141.95 → $139.12 = −$2.83 / $141.95 × $120 = **−$2.39** on $120, plus exit slippage ≈ −$2.46 total. Risk:reward on this setup ≈ 1:0.72 per trade — below 1:1 but the higher win rate in off-hours cascades is expected to compensate over many signals.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Liquidation-cascade-fade baseline ~1.2; off-hours playbook reduces signal frequency (higher quality selection) but adds slippage in thinner markets |
| Expected max drawdown | ~40% | Cascade fade has a wide draw profile; the kill trigger at 35% provides a hard stop |
| Win rate (per signal) | ~55–65% (off-hours), ~50–55% (peak) | Off-hours cascades expected to have higher mean-reversion probability per the session-conditioning thesis |
| Average win / average loss | ~1.2–1.8× | Cascade fades are low-win-multiple strategies; the edge is in win rate, not large individual wins |
| Breakeven cost budget | 30 bps | Peak-session cascade fades have ≤15 bps cost; weekend sessions have 20-35 bps slippage budget — blended breakeven is 30 bps |
| Signal frequency | Low | Cascades are episodic; off-hours cascades meeting the thresholds: estimated 2-6 per month across BTC/ETH/SOL |

**Session-bucket cost overlay:**

| Session | Slippage at entry | Exit friction | Net per trade (est.) |
|---|---|---|---|
| Peak | 8-15 bps | 5-10 bps | 13-25 bps total |
| Asia/Overnight | 15-25 bps | 10-20 bps | 25-45 bps total |
| Weekend | 20-35 bps | 15-25 bps | 35-60 bps total |

Weekend trades require larger reversion to be profitable after costs, which is reflected in the larger target reversion (2.0-3.5% vs 1.0-1.5% in peak).

## Capacity limits

- **Per signal:** cascade fades are inherently limited by book depth at the point of entry. In thin weekend books, a $200K entry is already moving the market; effective per-signal size is $50–$200K depending on the asset.
- **Aggregate strategy:** `capacity_usd: 1000000` — the strategy cannot scale beyond approximately $1M per asset given its reliance on being a *taker of liquidity in thin books*. As AUM grows, the entry itself consumes the overshoot opportunity.
- **Contrast with the underlying primitive:** [[liquidation-cascade-fade]] estimates $2M capacity; this strategy's weekend entries have *lower* capacity than the peak-session base strategy because book depth is thinner.

## What kills this strategy

1. **Exchange risk engineering improvement (#5).** Progressive improvements to partial liquidation, insurance funds, and ADL mechanisms (as already observed: 2020-03-12 vs 2025-10-10) reduce cascade depths globally. If weekend/off-hours cascades become structurally shallower (because exchanges have improved their engines), the session advantage narrows.
2. **Off-hours liquidity provision by HFT (#4).** As global HFT firms extend their crypto coverage hours, the thin-book advantage shrinks. The 2024-onwards normalisation of continuous algorithmic market-making on Hyperliquid and Binance has already partially reduced the off-hours depth premium.
3. **Cascade self-acceleration stops (#5: Regime change).** In a regime where funding is persistently near-zero (no crowded longs to flush), cascades lose their forced-flow overshoot characteristic — they become trend-continuation moves, not reversion setups. The session-conditioning does not help if the fundamental cascade mechanics have changed.
4. **Slippage underestimation in extreme events (#7: Operational).** In the thinnest books (weekend 2am UTC cascade), entry slippage can exceed 50 bps on large orders. If actual slippage consistently exceeds the budget, the strategy is systematically loss-generating.
5. **Crowding of the session-aware fade (#4).** If the off-hours cascade fade becomes widely known, competing fade providers will enter at better prices (shallower cascade depths), eliminating the overshoot that makes the trade viable.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 35%** in any rolling 30-day window.
2. **Off-hours cascade fade win rate < 45%** on minimum 30 signals in any 90-day window — the overshoot/reversion dynamic has changed; recalibrate or pause.
3. **Average reversion < 0.8× the entry-trigger price drop** over 20+ consecutive signals — the cascades are no longer overshooting; the mean-reversion edge is gone.
4. **Session classification not predictive:** t-test on post-cascade reversion (off-hours vs peak hours) yields p > 0.10 over 50+ signals — session overlay is adding noise, not signal; remove it and revert to the baseline.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Targets the highest-quality cascade subsets:** off-hours cascades with confirmed thin books have structurally larger overshoots — the strategy concentrates on the instances where the reversion edge is amplified, not diluted.
- **Low crowding:** most cascade-fade implementations use uniform parameters; session-aware sizing and trigger adjustment is less common, reducing competition at the exact point of entry.
- **Parameter logic is verifiable:** the session-conditional edge is testable — the hypothesis (off-hours cascades have higher win rate and larger reversion) can be validated or rejected on historical data without fitting individual parameters.
- **Composable with funding state:** the mid-hold funding check (if deeply negative funding appears, reduce exposure) integrates naturally with [[funding-flush-reversal]] logic for the extended hold.
- **Naturally low frequency:** the signal only fires on genuine cascade events that also meet session-adjusted thresholds — avoids whipsawing on marginal setups.

## Disadvantages

- **High slippage in thin sessions:** the sessions where the edge is largest are also where execution quality is worst. Weekend taker slippage of 20-35 bps is a meaningful fraction of the target 2.0% reversion — a much tighter margin than peak-session entries.
- **Session windows are approximate:** the UTC clock-based classification does not always reflect actual book depth (US holidays in the middle of the week, Asian public holidays). Overriding with real-time depth percentile adds complexity.
- **Small position sizes in key sessions:** weekend maximum size of 0.75% of sleeve is small. A 2% reversion on $150 (0.75% of $20K sleeve) is $3 gross — the strategy is not a meaningful P&L driver at small book sizes; it needs at least $50K sleeve to be operationally worthwhile.
- **Cascade dynamics are non-stationary:** as documented in [[liquidation-cascade-fade]], cascade depth has shrunk with exchange improvements. The session-conditional parameters must be recalibrated as exchange mechanics evolve.
- **Psychological difficulty:** entering a long into a weekend overnight cascade requires conviction that is genuinely hard to maintain — the book is thin, the cascade looks like a trend, and the time stop may force an exit before the reversion occurs.

## Sources

- [[liquidation-cascade-fade]] — the underlying cascade-fade primitive; all structural framing, CVD confirmation logic, and baseline performance from that page apply to this strategy.
- [[crypto-weekday-weekend-etf-era]] — documents the ETF-era structural liquidity split; the empirical basis for the session-conditioning thesis.
- [[long-liquidation-cascade]] — the Hyperliquid basket page for concentrated long cascades; the session parameters in this playbook apply to that setup.
- [[post-liquidation-rebound]] — the extended-recovery phase strategy; this playbook focuses on the cascade trough entry, not the subsequent hours.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (top coins, default Hyperliquid); the primary cascade trigger feed
- `GET /api/v1/market-intelligence/liquidations/by-exchange` — liquidations by venue, BTC, 4h window; venue-specific depth context
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding for mid-hold momentum check
- `GET /api/v1/liquidity/depth` — real-time order-book depth; session-classification override

**Historical data:**
- `GET /api/v1/backtesting/liquidations` — deep liquidation archive for session-conditional backtest
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200` — 15m OHLCV for cascade trigger measurement
- `GET /api/v1/derivatives/binance/history?days=90` — derivatives context for funding state analysis

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/liquidations"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-derivatives]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this playbook end-to-end:

- **Signal** — poll `GET /api/v1/market-intelligence/liquidations` through the off-hours window (Asia weekend / US overnight UTC buckets); a cascade spike in a thin session arms the fade entry
- **Filter** — `GET /api/v1/liquidity/depth` confirms the session is genuinely thin, and `GET /api/v1/derivatives/funding-rates?coin=BTC` checks momentum mid-hold
- **Execution** — venue context from `GET /api/v1/market-intelligence/liquidations/by-exchange` tells the agent which book absorbed the flow before it sizes the fade
- **Backtest** — `GET /api/v1/backtesting/liquidations` (Hyperliquid only, since 2026-03-30) joined to `GET /api/v1/backtesting/klines` 1m bars (also since 2026-03-30) for wick-level cascade replay; 1h bars reach back to 2017-08 for coarser session statistics
- **Tips** — the liquidation archive is only months deep, so session-conditional edge estimates carry wide error bars; treat this as a forward-accumulating dataset and re-fit quarterly

## Related

- [[liquidation-cascade-fade]] — the underlying cascade-fade primitive; this page adds session conditioning on top
- [[long-liquidation-cascade]] — the Hyperliquid-focused long cascade basket; session parameters from this playbook apply
- [[post-liquidation-rebound]] — the extended recovery phase after the cascade trough
- [[session-overlap-momentum]] — session-driven momentum at peak overlap; the liquidity framework from the opposite strategy direction
- [[crypto-weekday-weekend-etf-era]] — the ETF-era structural basis for the session-conditioning thesis
- [[funding-flush-reversal]] — funding-state confirmed mean reversion; complements mid-hold funding monitoring
- [[contrarian-extremes]] — broader sentiment-extreme contrarian strategy; the cascade fade is a microstructure-level expression of the same thesis
- [[liquidations]] — the contract mechanism generating the cascade
- [[market-microstructure]] — the theory of liquidity and its session variation
- [[order-flow]] — CVD and taker flow monitoring at cascade entry
- [[perpetual-futures]] — the instrument carrying the cascade mechanics
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — exchange engineering improvement, HFT competition, slippage risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
