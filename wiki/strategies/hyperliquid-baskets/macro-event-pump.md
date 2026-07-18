---
title: "Macro-Event Pump (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-07-13
status: good
tags: [crypto, perpetual-futures, hyperliquid, quantitative, event-driven, market-regime, momentum, risk-management]
aliases: ["Event Pump Basket", "FOMC Crypto Trade", "Macro Catalyst Basket", "Event-Driven Crypto Perp"]
related: ["[[hyperliquid-baskets-overview]]", "[[event-catalyst-regime]]", "[[policy-shock-regime]]", "[[crypto-macro-correlation-regime]]", "[[macro-events]]", "[[spot-etf-flows]]", "[[token-unlocks]]", "[[macro-relative-value]]", "[[regime-strategy-playbook]]", "[[crypto-market-regime-taxonomy]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[global-liquidity-expansion-contraction]]", "[[etf-and-institutional-flow]]", "[[breadth-and-momentum-divergence]]", "[[volatility-compression-breakout]]", "[[oi-confirmed-trend]]", "[[funding-rate-harvest]]", "[[support]]", "[[resistance]]", "[[atr-position-sizing]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
strategy_type: hybrid
timeframe: intraday
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [informational, behavioral]
edge_mechanism: "Consensus expectations for macro events are known pre-event; retail and systematic traders anchor to the expected outcome and over-react in the first minutes post-print, creating a buy-the-rumour/sell-the-news pattern or a mean-reversion opportunity in the initial overshoot that an informed, pre-positioned strategy can exploit."
data_required: [macro-calendar, ohlcv-intraday, etf-flows-daily, funding-rate, open-interest, options-implied-vol, historical-event-reactions]
min_capital_usd: 15000
capacity_usd: 30000000
crowding_risk: high
expected_sharpe: 0.8
expected_max_drawdown: 0.25
breakeven_cost_bps: 50
kill_criteria: |
  - drawdown > 25% on the basket over rolling 6 months
  - rolling 6-month Sharpe < 0
  - 5 consecutive events with no positive extraction (signal firing but not paying)
  - crowding metric (pre-event OI spike > 30% in 48h) present for 3+ consecutive events
---

# Macro-Event Pump (Hyperliquid Basket)

> **Not investment advice.** This is a design-doc draft for a systematic strategy sleeve. Performance figures are illustrative estimates only. Event reaction patterns are historical regularities, not guaranteed outcomes — individual events vary significantly.

An event-driven basket that positions ahead of or immediately after known macro catalysts: FOMC decisions, CPI prints, spot Bitcoin ETF flow data releases, and major regulatory announcements. The strategy captures two distinct behavioral patterns: the **pre-event drift** (assets trend toward the expected outcome in the days before a catalyst) and the **buy-the-rumour/sell-the-news reversal** (the initial move on the print fades as positioned traders exit into the reaction). Entries are predefined by event type; exits are tied to event resolution, not arbitrary time stops.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Informational** + **behavioral** (see [[edge-taxonomy]]).

- **Informational** — macro catalysts are scheduled and the consensus expectation is observable (Fed funds futures, CPI swap pricing, sell-side surveys). The gap between consensus, actual outcome, and price reaction is where informational edge lives. The strategy does not predict the outcome; it models the *reaction distribution* to different outcome scenarios relative to consensus.
- **Behavioral** — retail traders and under-hedged institutional flow create systematic patterns around known events: pre-event FOMO (chasing anticipated good news), post-event panic-covering (forced unwind), and the "sell the news" liquidation cascade when consensus is met but no incremental catalyst follows. These are well-documented in [[event-catalyst-regime]] and [[policy-shock-regime]].

## Why This Edge Exists

Crypto's high correlation to traditional risk assets during macro events ([[crypto-macro-correlation-regime]]) means that FOMC and CPI outcomes that move equity and rate markets also move BTC and ETH substantially — often more, given crypto's leverage and 24/7 market. The behavioral sequence is consistent:

1. **Pre-event positioning** — traders buy (sell) crypto in anticipation of a dovish (hawkish) surprise, creating a directional drift 24–72 hours before the event.
2. **Vol crush / squeeze pre-event** — as the event approaches, implied vol rises while realised vol compresses. Pre-positioned traders are exposed and must hedge; their hedging creates the compressed, range-bound tape immediately before the event.
3. **Initial reaction overshoot** — the print triggers algorithmic reactions and cascading orders before context is digested. The initial move frequently overshoots the "true" fundamental reaction by 30–60% in the first 15–30 minutes.
4. **Mean reversion** — informed participants fade the overshoot; the "sell the news" dynamic plays out over 30 minutes to 6 hours post-event.

The counterparty is the retail and systematic trader who reads the headline, reacts to the initial print direction, and enters the position *after* the overshoot — precisely when the informed short-term trader is exiting. See [[2025-10-crypto-liquidation-cascade]] for an extreme instance of post-event cascade dynamics.

## Null Hypothesis

Under "no edge," crypto's reaction to macro events is efficient: the pre-event drift reflects a rational updating of expectations given available information (e.g., Fed funds futures already embed most FOMC outcomes), and the post-event mean reversion is a round-trip that nets to zero after transaction costs. The apparent patterns in historical event reactions are the result of small-sample noise and selection bias (researchers observe salient events; the uneventful ones are forgotten).

**Disconfirming evidence to monitor:**

- Pre-event drift that continues through the event without reversing (consensus was right and the full reaction was proportionate — no "sell the news" dynamic).
- Events where crypto decouples from the macro catalyst entirely (crypto-idiosyncratic factor dominates, e.g., ETF news overrides an FOMC print).
- Crowding: pre-event OI spikes > 25–30% in 48 hours indicate the trade is consensus; post-event liquidations from overcrowded positioning create violent, un-fadeable moves rather than orderly mean reversions.

## Rules

**Event universe.** Track four event classes:

| Class | Events | Source | Crypto relevance |
|-------|--------|--------|-----------------|
| **Fed / rates** | FOMC decisions, Fed Chair press conferences, Jackson Hole | FOMC calendar | Highest: rate expectations drive DXY and risk appetite directly |
| **CPI / macro data** | US CPI, PCE, Non-Farm Payrolls | BLS calendar | High: inflation prints shift rate path expectations |
| **ETF flows** | Daily spot BTC/ETH ETF flow reports, large single-day flow outliers | [[spot-etf-flows]], Bloomberg | Direct: institutional demand signal; see [[etf-and-institutional-flow]] |
| **Regulatory / policy** | SEC decisions, Congressional crypto legislation, offshore exchange enforcement | News monitoring | Idiosyncratic: can override macro backdrop entirely |

**Pre-event setup (T−72h to T−1h):**

1. Identify consensus expectation (Fed funds futures implied cut/hold/hike; CPI swap vs. prior read; ETF flow trend).
2. Assess the *asymmetry*: is the market positioned for one outcome? Elevated long OI ahead of an expected dovish FOMC = crowded; a surprise hawkish outcome will cascade disproportionately.
3. Score the event setup: **Contrarian long** (market positioned short, dovish surprise likely); **Contrarian short** (market positioned long, hawkish or in-line likely to trigger "sell the news"); **Neutral** (mixed positioning, avoid pre-positioning).
4. If Contrarian signal is present: enter a small pre-position (0.5–1% of book) 24h before the event. Prefer [[funding-rate-harvest|funding-neutral or funded]] entry — longs pay shorts in pre-event vol crush phases, so a short pre-position can earn funding while waiting.

**Post-event fade (T+0 to T+30min):**

1. On print, observe the first-5-minute directional move.
2. If the initial move is > 2x the historical median absolute move for this event class, **fade the overshoot** with a 1–2% book position in the opposite direction.
3. Scale in: 50% at T+5min, 25% at T+15min if still moving in the same direction, 25% hold.
4. Target: 50–80% retracement of the initial move. Hard stop: 1.5x ATR beyond the initial extreme.

**Exit rules:**
- Close pre-position on the event itself (if it has moved favorably) or at the scheduled time.
- Close fade position within 4 hours post-event unless it is continuing to trend (which means it's not a fade — reverse or exit).
- Never hold an event-fade position overnight through a subsequent event.

## Implementation Pseudocode

```python
EVENT_CALENDAR = load_macro_calendar()  # FOMC dates, CPI dates, ETF flow release times

def macro_event_setup(event: Event, state) -> dict:
    """Determine pre-event positioning bias."""
    consensus_gap = event.consensus - event.prior  # e.g. expected CPI delta
    oi_change_48h = state.btc_oi_change(hours=48)  # crowding sensor
    funding_pre   = state.btc_funding_rate()

    # Crowding guard: if OI up >30% in 48h, the trade is consensus — skip
    if oi_change_48h > 0.30:
        return {"action": "skip", "reason": "crowded_pre_event"}

    # Score the positioning asymmetry
    market_bias = "long" if funding_pre > 0.05 else "short" if funding_pre < -0.05 else "neutral"

    if market_bias == "long" and event.type in ("FOMC", "CPI"):
        # Crowded long pre-dovish-expectation: asymmetric downside if hawkish
        return {"action": "short", "size": 0.01, "entry": "T-24h", "exit": "on_print"}
    elif market_bias == "short" and event.expected_outcome == "dovish":
        return {"action": "long",  "size": 0.01, "entry": "T-24h", "exit": "on_print"}
    else:
        return {"action": "none"}

def post_event_fade(event: Event, state) -> dict:
    """Fade the first-5-minute overshoot."""
    T5_move   = state.price_move(minutes=5, from_event=event)
    hist_med  = historical_median_move(event.type)
    atr_daily = state.atr(window=14, freq="1D")

    if abs(T5_move) > 2.0 * hist_med:
        direction = -1 * sign(T5_move)  # fade the overshoot
        stop      = state.event_extreme + direction * -1.5 * atr_daily
        target    = state.pre_event_price + 0.6 * T5_move  # 60% retracement
        return {
            "action": "fade", "direction": direction,
            "size_pct": 0.02, "stop": stop, "target": target,
            "max_hold": timedelta(hours=4)
        }
    return {"action": "none"}
```

## Indicators / Data Used

- **[[macro-events]] calendar** — FOMC decision dates/times, CPI/PCE/NFP release schedule, ECB and BoE meeting dates. Source: central bank websites; aggregated in economic calendar APIs.
- **[[spot-etf-flows]]** — daily BTC and ETH spot ETF inflow/outflow data; large single-day outliers (>$300–500M, illustrative threshold) are standalone tradeable events. See [[etf-and-institutional-flow]].
- **[[funding-rate]]** — pre-event funding as a crowding sensor (high positive funding = longs crowded; high negative = shorts crowded). See [[hyperliquid-funding-rate-microstructure]].
- **[[open-interest]]** — OI change in the 48 hours pre-event as a crowding indicator. Source: [[coinglass]], [[hypurrscan]].
- **Options implied vol** — pre-event IV for BTC/ETH options (term structure, near-dated IVs); vol crush post-event is a separate timing signal. Source: [[kaiko]] or Deribit API.
- **Historical event reactions** — the baseline distribution of BTC/ETH move magnitude and direction for each event class (FOMC, CPI, etc.). Built from historical data; re-calibrated quarterly.
- **[[support]] and [[resistance]]** — key technical levels that events are likely to test or bounce from; inform fade targets.

## Example Trade

**Illustrative scenario — not a backtest.** Setup: FOMC meeting; consensus expects a hold (no rate change); BTC funding rate at +0.08% per 8h (longs heavily crowded); OI up 15% in 48h pre-FOMC.

| Step | Action | Timing |
|------|--------|--------|
| Pre-event setup | Crowded long detected; pre-position 1% book short BTC-PERP | T−24h |
| Pre-event drift | BTC rallies +3% as "dovish hold" narrative builds; funding rises further | T−12h to T−1h |
| FOMC prints | Fed holds, language hawkish-neutral. BTC spikes +5% in first 5 min (2.5x median historical move) | T+0 to T+5min |
| Fade entry | Fade the spike: add 2% book short at T+5min, 1% at T+15min | T+5 to T+15min |
| Reversion | BTC retraces 65% of the spike over next 90 min as pre-positioned longs sell into the news | T+15min to T+2h |
| Exit | Close fade position at target; close pre-position for small gain | T+2h |

*Estimated net extraction (illustrative): pre-position ~0.6%, fade ~1.2%, net ~1.8% of book. Costs ~0.1–0.15%. Actual outcomes vary significantly by event.*

## Performance Characteristics

**Return shape:** event-clustered, high hit-rate but modest per-event extraction when right; occasional large losses when the event produces a persistent trend rather than mean-reversion.

**Expected Sharpe (illustrative):** ~0.7–1.0 over a calendar year with ~12–16 tradeable events (4 FOMC, 12 CPI, periodic ETF flow spikes). Higher in high-volatility macro environments where event reactions are large; lower in quiet, rate-stable periods where moves are small relative to transaction costs.

**Max drawdown (illustrative):** ~20–25%. Concentrated loss events occur when an FOMC or CPI triggers a genuine regime shift rather than a fade-able overshoot — e.g., an unexpected emergency rate cut or hike where the first move is the right move and the strategy fades into a trending 15–20% directional move.

**Crowding risk is high** — this is a widely-known pattern. Pre-event positioning and post-event fading are documented in academic literature and institutional playbooks. In heavily crowded setups, the fade-on-overshoot becomes itself a consensus trade, and the "true" directional move overwhelms the fade.

## Capacity Limits

The strategy is capacity-constrained by the precision and speed of execution required relative to market liquidity in the T+0 to T+15min window. Hyperliquid BTC-PERP is liquid but in the first 5 minutes post-FOMC, spreads widen and depth compresses. Strategy-level capacity for the **post-event fade** leg: ~$10–15M notional before market impact materially degrades the entry. The pre-event setup leg is slower (24h entry) and can scale to $25–30M without impact. Total strategy capacity: ~$30M.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Genuine regime-shifting events.** When a print is a true surprise that changes the macro regime (unexpected emergency policy action, a major regulatory ban), the initial move is not an overshoot — it is the signal. Fading into this loses at the worst time. This is the single most dangerous failure mode.
2. **Crowding.** Pre-event positioning and post-event fading are known patterns. If institutional flow consensus has already positioned the fade, the overshoot doesn't revert because there's no new fader left. OI crowding guard partially mitigates this.
3. **Event decoupling.** Crypto-specific catalysts (a large ETF outflow, an exchange hack) can override the macro catalyst and dominate the price move. A macro-event trade during an active crypto-specific shock is pure noise exposure.
4. **Execution latency.** The post-event fade depends on entering within T+5–15min. A 30-second execution lag at 2x the median move can be 60% of the available profit. Automated execution is effectively required.
5. **False precision in threshold calibration.** Historical median moves vary by regime; calibrating the "2x median" threshold in-sample will over-fit. See [[crypto-perp-backtesting-pitfalls]].

## Kill Criteria

Linked to [[when-to-retire-a-strategy]]:

- **Drawdown > 25%** over rolling 6 months → pause; full event-by-event review.
- **Rolling 6-month Sharpe < 0** → retire or restructure the signal.
- **5 consecutive events with no positive extraction** (signal fires but the trade loses or breaks even on every one) → the pattern has decayed; recalibrate or retire.
- **Crowding present (OI spike > 30% pre-event) for 3+ consecutive events** → the strategy is being front-run; stand down until crowding dissipates.

## Advantages

- **Calendar visibility** — unlike most strategies, the entry opportunities are known weeks in advance via the macro calendar. No ambiguity about when to watch.
- **Short holding periods** — most positions are held hours, not days; funding carry is a minimal factor.
- **Repeatable structure** — the buy-the-rumour/sell-the-news dynamic is consistent enough that a rules-based implementation can operationalize it without discretionary judgment on each event.
- **Complements slower baskets** — provides high-frequency tactical P&L on event days while [[global-liquidity-expansion-contraction]] and [[etf-and-institutional-flow]] provide the structural backdrop view.

## Disadvantages

- **High execution demands** — post-event fade requires sub-minute execution. Requires automated order management; manual execution degrades the edge materially.
- **High crowding risk** — widely-known pattern in both TradFi and crypto; crowding can make individual events lose despite the pattern being historically valid.
- **Infrequent** — ~12–20 events per year; in quiet macro environments the strategy is largely inactive.
- **Per-event binary risk** — a single genuine regime-shifting event can wipe several months of accumulated gains if the fade trade is entered at scale.

## Hyperliquid Execution Notes

This is an **intraday-to-swing basket** (most legs closed within hours; pre-event positions held 24h). Hyperliquid-specific considerations:

- **Funding carry over short holds** is minimal for the post-event fade (< 4h) but relevant for the pre-event position (24h). Monitor funding as a signal in its own right — extreme pre-event funding is itself a crowding indicator. See [[hyperliquid-funding-rate-microstructure]].
- **Isolated margin per leg** — always. Event-driven moves can be sudden and violent; isolated margin contains the loss to the allocated sleeve. See [[hyperliquid-liquidation-engine]] for single-mark-tick liquidation mechanics.
- **ADL during cascades** — a genuine regime-shifting event (the main failure mode) can trigger cascading liquidations that trigger ADL on winning fade positions at exactly the wrong moment. Ladder out of the fade in thirds rather than exiting all at once; the ADL risk is highest in the T+0 to T+30min window.
- **Spread widening at event time** — Hyperliquid's market maker liquidity partially withdraws around high-volatility macro events. Expect taker spreads 2–3x wider than normal in the T+0 to T+5min window. Price the execution cost into the expected-value calculation; the fade target must be large enough to absorb it.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — the 14-basket framework; [[event-catalyst-regime]] and [[policy-shock-regime]] are the direct regime contexts for this basket.
- [[event-catalyst-regime]] — the full regime page for event-driven catalysts.
- [[policy-shock-regime]] — regulatory and central bank policy shock patterns.
- [[crypto-macro-correlation-regime]] — the BTC/ETH macro-correlation backdrop that makes this strategy viable.
- [[spot-etf-flows]] — ETF flow events as a standalone catalyst class.
- [[2025-10-crypto-liquidation-cascade]] — worked example of post-event cascade dynamics and the limits of mean-reversion fades.
- [[coinglass]], [[hypurrscan]], [[kaiko]] — OI, funding, and flow data sources for setup scoring.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/event/calendar` — forward catalyst calendar up to 30d out (filter by type/symbol/bias)
- `GET /api/v1/event/regime/score` — event-risk composite (0-100)
- `GET /api/v1/event/regime/{symbol}` — per-symbol pending catalysts

**Historical data:**
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time snapshots for event backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/event/calendar"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

[[hyperliquid]] · [[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[perpetual-futures]] · [[market-regime]] · [[funding-rate]] · [[open-interest]] · [[liquidation]] · [[event-catalyst-regime]] · [[policy-shock-regime]] · [[crypto-macro-correlation-regime]] · [[macro-events]] · [[spot-etf-flows]] · [[macro-relative-value]] · [[regime-strategy-playbook]] · [[crypto-market-regime-taxonomy]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[global-liquidity-expansion-contraction]] · [[etf-and-institutional-flow]] · [[breadth-and-momentum-divergence]] · [[volatility-compression-breakout]] · [[oi-confirmed-trend]] · [[funding-rate-harvest]] · [[atr-position-sizing]] · [[support]] · [[resistance]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[coinglass]] · [[hypurrscan]] · [[kaiko]] · [[2025-10-crypto-liquidation-cascade]]
