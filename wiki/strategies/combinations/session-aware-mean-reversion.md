---
title: "Session-Aware Mean Reversion"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, mean-reversion, market-microstructure, quantitative, behavioral-finance, crypto, technical-analysis, day-trading]
aliases: ["Session-Conditioned Mean Reversion", "Session-Filtered Reversion", "Overnight Drift-and-Revert", "Session-Structure Reversion"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Thin-book overnight and weekend sessions produce systematic drift-and-revert patterns — price is pushed by low-liquidity momentum to an extreme that discretionary participants then fade at major session opens; conditioning mean-reversion entries on session structure (requiring entries during or after confirmed thin-book overshoot, sized and parameterized for the current liquidity window) extracts the routine reversion edge that is session-structural, not random noise."

data_required: [ohlcv-15m, ohlcv-1h, order-book-l2, funding-rates, ohlcv-daily]
min_capital_usd: 5000
capacity_usd: 2000000
crowding_risk: low

expected_sharpe: 1.0
expected_max_drawdown: 0.25
breakeven_cost_bps: 30

decay_evidence: "Session effects in crypto — overnight drift, weekend thin-book patterns — are documented in crypto-weekday-weekend-etf-era (wiki). Post-ETF era (2024+), spot ETF flows have increased US-session price formation dominance, potentially strengthening the off-hours drift-and-revert pattern as ETF-driven liquidity withdraws more consistently outside NYSE hours. No published study on session-conditioned mean-reversion P&L specifically; the session structure premise is supported by multiple market-microstructure studies."

kill_criteria: |
  - strategy drawdown > 25% from high-water mark
  - rolling 60-day Sharpe < 0 on a minimum 30 signals
  - session-specific win rate falls below 45% on any session bucket over 30+ signals (session classification is not adding predictive value for that bucket)
  - average reversion magnitude < 60% of entry-trigger move for 20 consecutive signals (overshoot is not occurring; price is trending rather than reverting)
  - session L2 depth percentile is no longer predictive of reversion probability on a 40-signal sample (liquidity structure has changed)

related: ["[[off-hours-liquidation-playbook]]", "[[range-mean-reversion]]", "[[rsi-mean-reversion]]", "[[session-overlap-momentum]]", "[[crypto-weekday-weekend-etf-era]]", "[[session-overlap-liquidity]]", "[[mean-reversion]]", "[[funding-flush-reversal]]", "[[market-microstructure]]", "[[order-flow]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Session-Aware Mean Reversion

Session-aware mean reversion is a [[mean-reversion]] strategy on crypto perpetuals and spot markets that conditions **entry timing, parameter calibration, and position sizing on the current trading session**. The primitive edge is mean reversion — price overshoots and reverts to equilibrium; the overlay is a session/time filter that recognises the structural liquidity cycle of crypto markets: overnight and weekend sessions produce systematic drift-and-revert patterns (thin-book momentum pushing to an extreme that major-session participants fade at open), while major-session opens (EU open, NY open, London-NY overlap) produce sharp reversion after off-hours overextensions. Parameters — RSI threshold, deviation from VWAP or moving average, position size, target, stop, and slippage budget — are calibrated per session window rather than applied uniformly.

This is explicitly differentiated from [[off-hours-liquidation-playbook]] (B3 page) — that strategy is triggered by **cascade events** (acute liquidation spikes: forced flow 2.5–5× the 24h average in a 15-minute window, price drop ≥ 1.8–2.5%). This page targets **routine session reversion** — the everyday drift-and-revert tendencies that recur in thin-book sessions without requiring a cascade event. Most overnight reversion setups are NOT liquidation events; they are ordinary thin-book momentum overshoots driven by low participation. The parameter tables overlap in structure but serve different entry conditions.

This is differentiated from [[range-mean-reversion]] — that page identifies ranging market conditions via ATR/Bollinger metrics and fades extremes generically. This page does not require a ranging regime classification; it conditions on the *session structure* specifically, recognising that even in trending macro regimes, off-hours thin-book sessions produce local mean-reversion tendencies at the session level.

This is differentiated from [[rsi-mean-reversion]] — that page uses RSI extremes as the entry trigger. This page can use RSI as one component of the entry signal but adds the session conditioning layer: an RSI extreme at 3am UTC on a Sunday has different reversion probability and magnitude than the same RSI reading at 2pm UTC on a Tuesday. Session-aware mean reversion adjusts both the RSI threshold and the expected reversion target by session.

This is differentiated from [[session-overlap-momentum]] — that page trades *momentum at the major-session overlap* (London-NY open, 13:00–15:00 UTC), capturing the directional liquidity surge at overlap. This page trades *reversion* in thin off-hours sessions, or the *fading* of the off-hours overshoot at the subsequent major-session open. The two strategies operate in structurally opposite regimes: overlap momentum follows the direction of the liquidity surge; this page fades the pre-overlap drift.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — in thin overnight and weekend sessions, a small number of retail participants and automated retail bots drive price above or below its prior-session value in the absence of large discretionary and institutional participants. This is the same behavioural mechanism documented in [[crypto-weekday-weekend-etf-era]]: price is moved by noise participants who face no sophisticated counterparty during the thin session. When major-session participants return (EU open, NY open), they observe the off-hours price as disconnected from equilibrium and provide the opposing flow that drives the reversion.
- **Structural** — the liquidity cycle in crypto is structural and recurring: [[crypto-weekday-weekend-etf-era]] documents that weekend/overnight sessions have 30–60% lower bid-ask depth relative to peak sessions. The arrival of institutional order flow at major-session opens is a predictable structural event that creates a predictable reversion opportunity for the participant who entered the trade before the institutional arrival.
- **Risk-bearing** — the session-aware mean reversion provider holds a position during the thin session (when reversion may not arrive immediately) and absorbs the risk that the off-hours drift continues further. The compensation for bearing that risk is the eventual reversion at session open, which overshoots slightly in the opposite direction as institutional participants reverse the thin-book extreme.

## Why this edge exists

**Session structure creates three recurring reversion patterns:**

1. **Overnight drift-and-revert at EU/NY open.** During the Asian overnight session (22:00–07:00 UTC), retail-driven momentum frequently drifts price 0.5–2% away from the US-session close. At EU open (07:00–08:30 UTC), European traders observe the overnight gap as a buying or selling opportunity and fade it, generating a mean reversion impulse of comparable magnitude. The pattern is documented as the "Asia session gap" in microstructure research on 24/7 markets.

2. **Weekend thin-book overshoot and Monday reversal.** Friday evening to Monday morning sessions produce some of the highest intra-weekend volatility in crypto but historically also the strongest Monday mean-reversion effect (per [[crypto-weekday-weekend-etf-era]]): price moves generated in the thin weekend session often partially reverse as US trading desks return Monday at the NYSE open. Pre-ETF, this was attributed to retail dominance; post-ETF era (2024+), the effect persists because institutional ETF flows are NYSE-session-dominated.

3. **Session-end overshoot fading.** The end of the NY session (22:00 UTC) sometimes produces a sharp directional spike as the last institutional flow of the day exhausts the book; this spike partially reverts as the book replenishes in Asian hours. The magnitude of the reversion is proportional to the depth depletion at the end of the NY session.

**Who is on the other side:** the thin-book retail or algorithmic participant who drives price during the session and finds no institutional counterparty until the next major session opens; and the momentum-following bot that extends the drift without regard to the return to institutional equilibrium.

## Null hypothesis

Under the null, session classification provides **no incremental predictive value** for mean-reversion probability or magnitude over and above the standard mean-reversion signals (RSI extreme, deviation from VWAP/MA):
- A mean-reversion entry signal generated at 03:00 UTC (thin session) should produce the same forward 2-hour return distribution as the same signal generated at 14:00 UTC (peak session).
- Session-adjusted parameters (lower RSI threshold in thin sessions, higher target in thin sessions) should not produce a higher Sharpe than the same uniform parameters across all sessions.
- L2 book depth percentile at entry time should not predict subsequent reversion magnitude or probability.

Currently not rejected (`backtest_status: untested`). Testable prediction: classify all RSI-extreme entries (RSI ≤ 25 or ≥ 75 on 1h bars) by session bucket; compute forward 4h return toward mean and maximum adverse excursion; predict that entries in thin sessions with low book depth percentile show higher win rate and larger reversion magnitude than identical signals in peak sessions.

## Rules

### Session classification

| Window | UTC Range | Classification | Characteristic |
|---|---|---|---|
| **NY Peak** | 13:30–22:00 | Peak | Deepest books; institutional dominant; ETF flows active |
| **EU Peak** | 07:00–13:30 | Peak | Moderate depth; European desk activity |
| **Asia/Overnight** | 22:00–07:00 | Off-peak | Thin; retail and Asian institutional dominant |
| **Weekend** | Fri 22:00–Mon 07:00 UTC | Weekend | Thinnest; structural institutional withdrawal |
| **Session transitions** | ±30 min of session starts | Transition | Fading off-hours extreme; sharpest reversion entry |

*Session transition windows (EU open 07:00–07:30 UTC, NY open 13:30–14:00 UTC) are the highest-conviction reversion entry windows for overnight overextensions.*

### Session-adjusted parameters

| Parameter | Peak sessions | Asia/Overnight | Weekend |
|---|---|---|---|
| RSI entry threshold (long) | ≤ 22 (deep oversold) | ≤ 26 | ≤ 28 |
| RSI entry threshold (short) | ≥ 78 (deep overbought) | ≥ 74 | ≥ 72 |
| VWAP deviation required (entry) | ≥ 1.5% from session VWAP | ≥ 1.0% | ≥ 0.8% |
| Book depth percentile check | < 40th percentile confirms thin overshoot | < 35th | < 30th (standard for weekend) |
| Entry size multiplier | 0.8× base (peak is lower conviction) | 1.0× base | 0.9× base (thin slippage penalty) |
| Target reversion | 0.8–1.2% | 1.0–1.8% | 1.2–2.5% |
| Time stop | 2 hours | 3 hours | 4 hours |
| Stop loss (from entry) | 1.2% | 1.5% | 2.0% |
| Slippage budget (entry) | 5–10 bps | 10–20 bps | 15–30 bps |
| Session-open bonus | +0.2× size multiplier if entering at EU or NY open | — | — |

**Rationale for parameter adjustments:**
- Lower RSI threshold required in peak sessions: peak sessions need a more extreme RSI reading to confirm genuine overshoot (more participants are active; normal volatility is higher in terms of random directional moves).
- Lower VWAP deviation required in off-peak sessions: a 1% deviation in a thin overnight session represents a more extreme move relative to the baseline volatility than a 1.5% deviation in a peak session.
- Weekend entries have smaller size despite being the highest-overshoot sessions: slippage on entry and exit in thin weekend books can eat 40–60 bps of the target reversion.
- Session-transition entries (fading the off-hours extreme at EU or NY open): size multiplier increases 0.2× because institutional session-open flow provides timing confirmation that the reversion is beginning.

### Entry conditions

1. **Session classified** per the table above.
2. **Mean-reversion signal active (require at least one of):**
   - RSI (14-period, 1h bars) is ≤ long-threshold or ≥ short-threshold for the current session.
   - Price is ≥ session-adjusted VWAP deviation below (long) or above (short) the rolling VWAP.
   - Bollinger Band outer touch: 1h close outside the 2σ Bollinger Band (20-period), with the band width at or below the 30th percentile of its 24h range (band is not already extreme from prior volatility).
3. **Book depth confirmation:** real-time L2 depth at ±1% is below the session-adjusted depth percentile (confirms the book is thin, supporting the overshoot hypothesis).
4. **No cascade event active:** if liquidation volume spike is ≥ 2.5× the 24h average (an [[off-hours-liquidation-playbook]] trigger), defer to that strategy's parameters — do not double-up with session-reversion sizing.
5. **Funding check:** 8h funding rate is not deeply negative (below −0.03%/8h). Deeply negative funding during an oversold signal means shorts are crowded — the reversion may be a momentum continuation, not a mean reversion.

### Exit conditions

1. **Profit target:** reversion of the session-adjusted target (see table) from entry.
2. **Session open exit (preferred for off-peak entries):** if entered in Asia/overnight, exit at or near EU open (07:00–07:30 UTC) regardless of whether the full target has been met — the session-open flow is the edge; don't overstay.
3. **Time stop:** session-adjusted time stop from entry (see table).
4. **Stop loss:** session-adjusted stop from entry.
5. **RSI normalisation:** if RSI normalises back toward 50 before the price target is reached (within 1 hour), the overshoot was absorbed quickly — close at market to avoid the time stop eroding gains.

### Position sizing

- **Base size:** 1.0% of the strategy sleeve.
- **Session multiplier:** apply the session-adjusted multiplier from the table.
- **Session-open bonus:** +0.2× if entering at the EU or NY open transition window.
- **Maximum concurrent positions:** 2 (total ≤ 2% of sleeve at maximum deployment).

## Implementation pseudocode

```python
# session_aware_mean_reversion.py

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

# ---- session windows (UTC) ----
EU_PEAK_START, EU_PEAK_END   = 7.0,  13.5
US_PEAK_START, US_PEAK_END   = 13.5, 22.0
WEEKEND_START_FRI            = 22.0
WEEKEND_END_MON              = 7.0
SESSION_OPEN_WINDOW          = 0.5   # ±30 min around session start

@dataclass
class SessionParams:
    name:             str
    rsi_long:         float   # RSI ≤ this → potential long
    rsi_short:        float   # RSI ≥ this → potential short
    vwap_dev_pct:     float   # minimum |VWAP deviation| to qualify
    depth_pctile:     float   # L2 depth must be below this percentile
    size_multiplier:  float
    target_pct:       tuple   # (low, high) reversion target %
    time_stop_h:      float
    stop_loss_pct:    float
    slippage_bps:     float

PARAMS = {
    "peak":    SessionParams("peak",    22.0, 78.0, 1.5, 40, 0.8, (0.8,  1.2),  2.0, 1.2, 7.5),
    "offpeak": SessionParams("offpeak", 26.0, 74.0, 1.0, 35, 1.0, (1.0,  1.8),  3.0, 1.5, 15.0),
    "weekend": SessionParams("weekend", 28.0, 72.0, 0.8, 30, 0.9, (1.2,  2.5),  4.0, 2.0, 22.5),
}
SESSION_OPEN_BONUS = 0.2   # additional size multiplier at transition windows

def classify_session(dt: datetime) -> tuple[str, bool]:
    """Returns (session_name, is_session_open_transition)."""
    h  = dt.hour + dt.minute / 60.0
    wd = dt.weekday()
    # weekend
    if wd == 5 or wd == 6:
        return "weekend", False
    if wd == 4 and h >= WEEKEND_START_FRI:
        return "weekend", False
    if wd == 0 and h < WEEKEND_END_MON:
        return "weekend", False
    # session-open transition windows
    is_transition = (abs(h - EU_PEAK_START) < SESSION_OPEN_WINDOW or
                     abs(h - US_PEAK_START) < SESSION_OPEN_WINDOW)
    if EU_PEAK_START <= h < EU_PEAK_END:
        return "peak", is_transition
    if US_PEAK_START <= h < US_PEAK_END:
        return "peak", is_transition
    return "offpeak", is_transition

@dataclass
class ReversionSignal:
    rsi_1h:           float
    vwap_dev_pct:     float   # positive = above VWAP, negative = below
    bb_outer_touch:   bool
    depth_pctile_24h: float
    funding_8h:       float
    liq_spike_mult:   float  # liquidation volume spike multiplier (vs 24h avg)

def signal_qualifies(sig: ReversionSignal, params: SessionParams) -> tuple[bool, str]:
    # check L2 depth thin
    if sig.depth_pctile_24h >= params.depth_pctile:
        return False, f"book not thin: depth at {sig.depth_pctile_24h:.0f}th pctile (need <{params.depth_pctile})"
    # avoid cascade events — defer to off-hours-liquidation-playbook
    if sig.liq_spike_mult >= 2.5:
        return False, "cascade event active — use off-hours-liquidation-playbook params"
    # funding check for longs
    if sig.rsi_1h <= params.rsi_long and sig.funding_8h < -0.03:
        return False, f"funding deeply negative ({sig.funding_8h:.3f}% 8h) — crowded shorts; skip long"
    # primary reversion signal: any one of three
    rsi_long  = sig.rsi_1h <= params.rsi_long
    rsi_short = sig.rsi_1h >= params.rsi_short
    vwap_long  = sig.vwap_dev_pct <= -params.vwap_dev_pct
    vwap_short = sig.vwap_dev_pct >=  params.vwap_dev_pct
    bb_signal  = sig.bb_outer_touch
    if not (rsi_long or rsi_short or vwap_long or vwap_short or bb_signal):
        return False, "no mean-reversion signal (RSI, VWAP deviation, or BB touch)"
    return True, ""

def session_reversion_decision(sig: ReversionSignal, book: dict, dt: datetime) -> dict:
    if book.get("drawdown", 0) > 0.25:
        return {"action": "FLAT", "reason": "drawdown kill"}

    session, is_transition = classify_session(dt)
    params = PARAMS[session]

    ok, reason = signal_qualifies(sig, params)
    if not ok:
        return {"action": "WAIT", "session": session, "reason": reason}

    # determine direction
    direction = None
    if sig.rsi_1h <= params.rsi_long or sig.vwap_dev_pct <= -params.vwap_dev_pct:
        direction = "LONG"
    elif sig.rsi_1h >= params.rsi_short or sig.vwap_dev_pct >= params.vwap_dev_pct:
        direction = "SHORT"
    else:
        direction = "LONG"  # BB touch: use price location to determine (external)

    size_mult = params.size_multiplier + (SESSION_OPEN_BONUS if is_transition else 0)
    notional  = book["sleeve_capital"] * 0.010 * size_mult
    notional  = min(notional, book["sleeve_capital"] * 0.02)  # cap at 2% sleeve

    return {
        "action":        f"FADE_{direction}",
        "session":       session,
        "is_transition": is_transition,
        "notional":      notional,
        "target_pct":    params.target_pct[0],
        "stop_pct":      params.stop_loss_pct,
        "time_stop_h":   params.time_stop_h,
        "slippage_bps":  params.slippage_bps,
        "note": (f"session={session}, rsi={sig.rsi_1h:.1f}, "
                 f"vwap_dev={sig.vwap_dev_pct:.2f}%, depth_pctile={sig.depth_pctile_24h:.0f}, "
                 f"size_mult={size_mult:.2f}x, transition={is_transition}"),
    }
```

The production system adds: real-time L2 depth monitoring to confirm the depth-percentile gate dynamically; a session-open notifier that triggers the transition-window size bonus automatically at 07:00 and 13:30 UTC; and a daily P&L attribution table by session bucket to monitor whether each session is contributing positively.

## Indicators / data used

- **RSI (14-period, 1h bars)** — computed from `/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=60`. Primary mean-reversion entry signal.
- **Session VWAP** — computed intraday from the 15m klines; no dedicated CDA endpoint. `/api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=96` provides 24h of 15m bars for rolling VWAP.
- **Bollinger Bands (20-period, 2σ, 1h)** — computed from 1h klines. No dedicated endpoint; compute from klines.
- **L2 order-book depth** — `/api/v1/liquidity/depth` for real-time depth monitoring; the depth-percentile gate requires historical depth series to compute the current percentile. Alternatively, use CDA's depth endpoint at entry time and compare to prior readings.
- **Funding rate (8h)** — `/api/v1/derivatives/funding-rates?coin=BTC` — the funding check that blocks long entries when funding is deeply negative.
- **Liquidation volume (for cascade exclusion)** — `/api/v1/market-intelligence/liquidations` — if a cascade event is occurring, defer to [[off-hours-liquidation-playbook]].
- **Session classification (UTC clock)** — no API; implemented via the `classify_session()` function in pseudocode above.

## Example trade

**Setup — overnight overshoot fading at EU open (illustrative):**

- Asset: ETH-PERP on Binance.
- Session: Asia/Overnight (02:40 UTC Monday).
- ETH prior NY close: $3,180.
- **Signal (02:40 UTC):** retail selling in Asia session pushed ETH down to $3,102 (−2.4%). RSI 14-period 1h = 24.2 (below the 26 off-peak threshold). VWAP deviation from session VWAP: −1.6% (exceeds the 1.0% off-peak threshold). Book depth: 28th percentile of 24h history (below 35th pctile off-peak threshold). Funding: −0.010%/8h (above the −0.03% kill threshold; no kill). Liquidation spike: 1.2× 24h average (below 2.5× cascade threshold; no cascade).
- **Entry:** signal qualifies. Off-peak size multiplier = 1.0×. Base size = 1.0% of $50,000 sleeve = $500. Actual size: $500. Limit long at $3,106 (0.13% above mark price).
- **Stop:** 1.5% below entry = $3,059.
- **Target:** 1.0–1.8% reversion from entry → $3,137–$3,162.
- **Time stop:** 3 hours from entry (if not at target by 05:40 UTC, close).

**Hold:** ETH stabilises at $3,100–3,110 through 04:30 UTC. At EU open (07:10 UTC), European buyers observe the overnight gap (−2.4% from NY close) and buy. By 07:45 UTC ETH recovers to $3,148.

- Exit at $3,148 (via session-open exit rule — beyond the nominal 3h time stop but within the EU-open fading window; human override at session open is appropriate).
- **Trade P&L:** $3,106 → $3,148 = +1.35% × $500 = **+$6.75 gross**. Slippage (entry + exit, off-peak ~15 bps combined): −$0.75. **Net: +$6.00** (+1.2% on $500, +0.012% of sleeve).

**Session-open bonus scenario:** if this had been entered exactly at EU open (07:00–07:30 UTC transition window): size multiplier = 1.0 + 0.2 = 1.2×; size = $600. Same trade = **+$7.20 net** at the exact session-open entry timing.

**Stop-loss scenario:** if Asia selling continued overnight and ETH fell to $3,059: close at stop, −$0.70 (−1.5% × $500 = −$7.50 gross) minus exit slippage ≈ −$8.25. Net: −8.25 loss on $500 = −1.65% of deployed, −0.016% of sleeve. Session reversion trades are sized conservatively for this reason.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Intraday mean reversion with session conditioning; cost overlay is manageable |
| Expected max drawdown | ~25% | Low per-trade sizing (≤2% of sleeve) means sequences of losses require many consecutive failures to produce the strategy-level drawdown |
| Win rate (per signal) | ~58–65% | Mean-reversion strategies in thin sessions expected higher win rate than in peak sessions (per session-conditioning thesis); blended estimate |
| Average win / average loss | ~1.1–1.5× | Target reversion of 1–2% vs stop of 1.2–2%; modest win multiples, edge comes from win rate |
| Breakeven cost budget | 30 bps | 15m and 1h entries: taker costs 5–10 bps per fill × 2 fills = 10–20 bps total. Weekend 15–30 bps budget. Blended: ~20 bps. |
| Signal frequency | Medium | 1–3 qualifying setups per session per asset; 2–3 assets active = 4–9 potential signals per day across all sessions |

**Session-bucket expected P&L contribution:**

| Session | Expected win rate | Expected avg reversion | Net contribution |
|---|---|---|---|
| Peak (NY/EU) | ~52% | 0.8–1.2% | Lowest; tightest RSI/VWAP threshold needed |
| Asia/Overnight | ~60% | 1.0–1.8% | Medium; routine pattern |
| Weekend | ~58% | 1.2–2.5% | Highest gross but highest slippage |
| EU/NY open transition | ~65% | 1.0–2.0% | Highest quality; institutional confirmation |

## Capacity limits

- **Per signal:** the strategy enters in thin-book conditions by definition; per-entry notional is capped at 2% of sleeve to limit market impact in the thin session. Beyond $500K sleeve, entry orders begin to move the market in Asia overnight sessions.
- **Aggregate capacity:** `capacity_usd: 2000000` — at $2M AUM, a 1% entry = $20K notional per signal, which is visible in thin-book weekend sessions on mid-caps. BTC/ETH sessions can support larger ($100K+ per signal), but the strategy's edge is highest in the instruments with the clearest session structure, which are also thinner at entry.

## What kills this strategy

1. **24/7 institutional presence (#5: Regime change).** If large institutional market-makers extend continuous algorithmic coverage to overnight and weekend hours (as has been occurring gradually since 2023 on Hyperliquid and Binance), the thin-book overshoot is absorbed in real-time rather than persisting to session open. The reversion still happens but the magnitude shrinks, compressing the net P&L per signal.
2. **ETF-era structural change continues (#5).** The post-2024 ETF era has already strengthened the session structure in one respect (US-session dominance), but it has also introduced ETF arbitrage market-makers who may bridge the overnight gap more efficiently. If ETF flow-driven off-hours arb eliminates the overnight gap pattern, the drift-and-revert edge disappears for the overnight/weekend bucket.
3. **Funding regime mismatch (#2: Cost structure).** If the crypto market enters a persistent bear or negative-funding regime, the "do not enter long when funding < −0.03%" gate blocks most of the natural overnight oversold entries (bear markets produce deeply negative funding during oversold conditions). The strategy becomes one-sided or inactive.
4. **Weekend liquidity normalisation (#5).** As 24-hour U.S. CME futures (if expanded) and regulated spot ETF trading on weekends develops, the structural liquidity withdrawal over weekends may lessen, reducing the weekend bucket's edge to near-zero.
5. **Parameter obsolescence without recalibration (Operational #7).** The session-adjusted RSI and VWAP thresholds are derived from the current liquidity structure. If liquidity patterns shift (e.g., Asian session becomes deeper due to Japanese or Korean institutional adoption), parameters need re-estimation. Running on stale parameters is worse than running no filter at all.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 25%** in any rolling 60-day window.
2. **Rolling 60-day Sharpe < 0** on a minimum of 30 completed signals.
3. **Session-specific win rate < 45%** on any session bucket over 30+ signals — that bucket's classification is not predicting reversion; remove or recalibrate that bucket's parameters.
4. **Average reversion magnitude < 60% of entry-trigger move** for 20 consecutive signals across any single session bucket — overshoots are no longer occurring at that session; the structural basis for that bucket's edge has changed.
5. **L2 depth percentile not predictive** of reversion probability on a 40-signal sample (p > 0.10 on Mann-Whitney test) — the depth confirmation gate is adding noise; remove and reassess.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **No cascade event required:** unlike [[off-hours-liquidation-playbook]], this strategy does not need a 3–5× liquidation spike to trigger. The routine overnight drift-and-revert pattern fires 1–3 times per session per asset, generating more frequent signal flow.
- **Low crowding in session-conditioned entries:** most mean-reversion implementations (RSI, Bollinger Band) use uniform parameters. Session-conditional parameter adjustment is less widely implemented, reducing competition at the specific entry points this strategy targets.
- **Session structure is empirically verifiable:** the hypothesis (thin-book sessions produce more reversions) is testable against historical klines by session bucket, providing a falsifiable foundation for parameter tuning.
- **Composable with off-hours liquidation playbook:** when a cascade event *does* occur, [[off-hours-liquidation-playbook]] handles the acute cascade with its larger entry and wider parameters; session-aware mean reversion handles the routine non-cascade drift. The two strategies are complementary and can run on the same book with non-overlapping triggers.
- **Intraday holding period:** sessions mean positions are held for hours, not days. Capital recycles frequently; drawdown periods are shorter in calendar time.

## Disadvantages

- **Thin-session slippage is the primary cost driver:** entries in Asia/overnight and weekend sessions face 10–30 bps of slippage on entry + exit. On a target reversion of 1.0–1.8%, a 25 bps round-trip cost is a significant portion of the expected P&L. Position sizing must be conservative.
- **Overnight hold risk:** entries in the Asia session hold through 2–4 hours of continued potential drift before EU open provides the institutional reversion flow. The time stop protects against this, but a true overnight trend (macro event, exchange hack) can gap through the stop.
- **Session boundary ambiguity in transitions:** the EU and NY open transitions are the highest-conviction windows but are also the shortest (30 minutes). If fill timing is off by 20 minutes, the session-open institutional flow has already begun and the entry is into the reversion-in-progress, reducing the remaining reversion target.
- **Parameter maintenance overhead:** four session buckets × three entry signals × two directions = substantial parameter space to monitor and recalibrate quarterly. Running stale parameters is a hidden P&L drag.
- **Low absolute P&L per trade at small book sizes:** 1–1.2% of 2% sleeve per signal = 0.02% of portfolio per winning trade. At $20K AUM this is $4 per trade gross — not operational. The minimum book size for this strategy to be worthwhile is approximately $50–100K.

## Sources

- [[off-hours-liquidation-playbook]] — the cascade-event-driven counterpart; session parameter table structure inspired by that page; differentiated by entry trigger (cascade vs routine drift).
- [[crypto-weekday-weekend-etf-era]] — documents the ETF-era structural liquidity split that provides the empirical basis for the session-conditioning thesis; the weekend liquidity withdrawal and Monday reversal effect.
- [[session-overlap-liquidity]] — the theoretical framework for how session-opening institutional liquidity arrival creates reversion pressure on off-hours drifts.
- [[rsi-mean-reversion]] — the canonical RSI-based mean-reversion strategy; this page adds the session-conditioning layer to that primitive.
- [[range-mean-reversion]] — range-based mean reversion (Bollinger Band); this page uses similar entry signals with session-conditional parameter adjustment.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=60` — 1h OHLCV for RSI(14) computation and session VWAP
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=15m&limit=96` — 15m OHLCV (24h window) for intraday VWAP and Bollinger Band
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — 8h funding rate; blocks deeply negative funding long entries
- `GET /api/v1/market-intelligence/liquidations` — liquidation spike check; if 2.5× threshold, defer to off-hours-liquidation-playbook
- `GET /api/v1/liquidity/depth` — real-time L2 book depth; confirms the depth-percentile gate

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=1000` — extended 1h klines for RSI, Bollinger Band backtesting by session bucket
- `GET /api/v1/backtesting/liquidations` — historical liquidation context; excludes cascade periods from the session-reversion analysis

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=60"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — 1h and 15m klines (`GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=60`, `interval=15m&limit=96`) drive RSI(14) and session-VWAP deviation per UTC bucket
- **Filter** — `GET /api/v1/derivatives/funding-rates?coin=ETH` blocks longs into deeply negative funding; `GET /api/v1/market-intelligence/liquidations` defers to the [[off-hours-liquidation-playbook]] when a cascade is live
- **Execution** — `GET /api/v1/liquidity/depth` enforces the depth-percentile gate before quoting in thin sessions
- **Backtest** — session-bucket statistics from `GET /api/v1/backtesting/klines` (Binance spot 1h back to 2017-08); minute-level VWAP replay only since 2026-03-30 (1m klines), and cascade exclusion via `GET /api/v1/backtesting/liquidations` also starts 2026-03-30
- **Tips** — session boundaries are UTC constants but liquidity migrates with DST and venue listings; re-estimate per-bucket depth percentiles from `/liquidity/depth` monthly

## Related

- [[off-hours-liquidation-playbook]] — the cascade-event counterpart: same session-aware framework, acute liquidation trigger; this page handles the routine drift, not the cascade
- [[range-mean-reversion]] — range-based mean-reversion primitive; this page adds session conditioning
- [[rsi-mean-reversion]] — RSI-based mean-reversion primitive; this page adds session conditioning
- [[session-overlap-momentum]] — the directional counterpart: momentum at peak overlap; this page fades the drift that occurs outside the overlap window
- [[crypto-weekday-weekend-etf-era]] — the empirical basis for session structure effects; weekend liquidity withdrawal and Monday reversion
- [[session-overlap-liquidity]] — the theoretical microstructure framework for session-opening liquidity
- [[mean-reversion]] — the general mean-reversion concept
- [[funding-flush-reversal]] — mean-reversion confirmed by funding flush; this page is session-triggered rather than funding-triggered
- [[market-microstructure]] — theory of liquidity cycles and session structure
- [[order-flow]] — CVD and taker flow monitoring at entry for signal confirmation
- [[behavioral-finance-overview]] — thin-book behavioural mechanics driving the off-hours overshoot
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — 24/7 institutional coverage, ETF-era normalisation, parameter obsolescence
- [[when-to-retire-a-strategy]] — kill vs pause framework
