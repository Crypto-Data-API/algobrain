---
title: "Narrative with Trend Confirmation"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, momentum, behavioral-finance, technical-analysis, trend-following, crypto, swing-trading, quantitative]
aliases: ["Trend-Gated Narrative Trade", "Narrative Breakout Confluence", "Narrative Momentum Filter"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, informational]
edge_mechanism: "Narrative capital flows are predictable once a story achieves consensus, but pure narrative entries frequently trap early buyers in drawdowns before the flow arrives; requiring a price-structure confirmation (breakout or higher-low above a moving average) as a second trigger filters out the 'narrative value trap' regime and enters only after market structure agrees that the story is *currently* attracting capital — capturing the behavioural inflow after it starts without chasing it."

data_required: [ohlcv-daily, ohlcv-4h, social-volume, sector-flows, moving-averages]
min_capital_usd: 2000
capacity_usd: 30000000
crowding_risk: high

expected_sharpe: 0.8
expected_max_drawdown: 0.30
breakeven_cost_bps: 25

decay_evidence: "Narrative trading is inherently high-crowding-risk — the same catalysts are visible to all participants, and as algorithmic social-sentiment tools proliferate, early narrative identification becomes crowded. The trend-confirmation gate adds the analytical discipline of waiting for price-structure confirmation, which survives some degree of narrative crowding because the confirmation is a real observable (higher-low / breakout), not just a social-volume threshold."

kill_criteria: |
  - strategy drawdown > 30% from high-water mark
  - rolling 6-month Sharpe < 0 on minimum 15 trades
  - trend-confirmation gate rate exceeds 80% rejections (narrative signals fire but trend rarely confirms — either narratives are being identified too early or the market has stopped caring about the current narrative class)
  - loss rate on confirmed entries exceeds 60% over 20+ consecutive signals (the trend confirmation is no longer a reliable filter in the current regime)

related: ["[[narrative-trading]]", "[[news-trading]]", "[[sentiment-trading]]", "[[meme-coin-cycle]]", "[[trend-following-cta]]", "[[breakout-trading]]", "[[momentum-rotation]]", "[[unlock-aware-momentum]]", "[[contrarian-extremes]]", "[[moving-average]]", "[[behavioral-finance-overview]]", "[[crypto-narratives]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Narrative with Trend Confirmation

Narrative with trend confirmation is [[narrative-trading]] — positioning into crypto assets that are the focus of a dominant, spreading market story — where a new entry requires **price-structure confirmation**: the asset must have broken above a key resistance level, or have formed a higher-low above a medium-term moving average, *after* the narrative has been identified. The primitive edge is narrative-driven capital rotation (the same social-attention and flow mechanism documented in [[narrative-trading]]); the overlay is a trend-gate that prevents entering into narratives that the broader market has not yet agreed with via price action, filtering out the "early narrative value trap" — the regime where a compelling story is visible but capital is not yet flowing.

This is differentiated from [[narrative-trading]] — that page describes the full narrative strategy including entry on narrative identification before price confirms. This page adds the **mandatory trend gate**: entry is blocked until price structure corroborates the narrative, specifically to avoid the common failure mode where the story is right but the timing is early — the "correct narrative, wrong entry" problem that generates large drawdowns in pure narrative strategies.

This is differentiated from [[unlock-aware-momentum]] — that page gates a momentum strategy on the unlock calendar (avoiding narrative-adjacent events that create supply). This page gates a *narrative strategy* on a *trend signal*, not on an event calendar.

## Edge source

Per [[edge-taxonomy]], **behavioral + informational**:

- **Behavioral (primary)** — [[narrative-trading]]'s core mechanism: capital and attention rotate into a spreading story faster than fundamentals can justify. The trend-confirmation gate improves the behavioral edge by entering *after* momentum has begun to reflect the flow, rather than before. This reduces the frequency of early-narrative drawdowns — the "pioneer penalty" where the early narrative buyer is correct in direction but absorbs the full volatility before the herd arrives.
- **Informational (secondary)** — narrative identification is inherently informational: recognising which story is spreading to a wider audience before it is consensus. The trend gate adds a second informational layer: the price structure tells you that *capital* has already begun confirming the narrative, not just social volume or media tone. Combining both improves the quality of the informational signal over either alone.

## Why this edge exists

**The combination solves the "correct narrative, wrong timing" failure mode:**

1. **Early narrative entries suffer a high drawdown-before-profit profile.** A compelling narrative — AI integration, Layer-2 adoption, real-world asset tokenisation — can be identified months before capital flows at scale. The early buyer absorbs the distribution period (large holders selling into the emerging story), the false-start moves, and the wait for retail FOMO. The trend-gate requirement eliminates these pre-flow entries by enforcing that price has already moved: at minimum, a higher-low above the 50-day moving average means the asset has survived at least one distribution and has re-established accumulation structure.

2. **Price confirmation identifies the "flow has started" transition.** The trend-confirmation rule is not a prediction; it is an observation. A breakout above a consolidation level after a narrative catalyst means: (a) sellers at the old resistance have been absorbed, (b) fresh capital (not just early buyers re-averaging) has cleared the supply. The narrative trader who waits for this confirmation enters later but into a cleaner setup with a natural stop below the confirmation level.

3. **Dual-exit discipline reduces holding through narrative decay.** The strategy exits on either narrative decay *or* trend break — whichever fires first. This is additive over pure narrative trading, which often lacks a mechanistic exit for the post-peak distribution phase. When the trend breaks, the narrative may still be spreading (the story survives the price break), but the price action tells you that the next phase of capital flow has paused or reversed. Cutting on the trend break avoids sitting through a secondary top.

**Who is on the other side:** the early narrative buyer who entered before trend confirmation (and may be trapped on the wrong side of the distribution), and the late FOMO buyer who enters after the narrative is fully consensus (at which point the trend is already exhausted).

## Null hypothesis

Under the null, trend confirmation at narrative-entry time carries **no incremental information** about forward return: narrative entries with trend confirmation should perform identically to narrative entries without it (same distribution of forward returns over the following 20 days). Specifically:
- The average 20-day forward return of trend-confirmed narrative entries should not differ from non-confirmed entries on the same narrative set.
- The win rate of trend-confirmed entries should not exceed the win rate of narrative-only entries.
- The drawdown before profit (maximum adverse excursion to maximum favourable excursion ratio) should not improve for trend-confirmed vs unconfirmed entries.

Currently not rejected (`backtest_status: untested`). Testable prediction: for a defined universe of historical narrative catalysts (social-volume spike, sector-flow rotation, news event) on crypto majors, partition entries by whether a trend-confirmation rule was also satisfied at the time; compare forward P&L distributions. Prediction: confirmed entries have lower maximum adverse excursion, higher win rate, and similar or better average win — at the cost of lower signal frequency and potentially slightly higher average entry price.

## Rules

### Step 1 — Narrative identification

The narrative must meet at least one of the following:
1. **Social-volume spike:** the asset's social mention volume is in the top 15% of its 90-day history for 2+ consecutive days.
2. **Sector-flow acceleration:** capital flows into the asset's sector (e.g. Layer-2, AI, DePIN) are rising at 2× the prior 30-day rate.
3. **News catalyst:** a specific, verifiable event (partnership announcement, protocol upgrade, major exchange listing) has been published from a non-anonymous, credible source within the last 72 hours.
4. **Narrative classification:** the asset appears in the wiki's [[crypto-narratives]] catalog as a currently active narrative with momentum score > 50.

A narrative identification that fails all four criteria is not a signal — it is speculation.

### Step 2 — Trend confirmation gate

**Entry is blocked until BOTH are true simultaneously:**

1. **Breakout:** price has closed above the asset's **20-day channel high** on the daily or 4h chart. OR
2. **Higher-low structure:** the most recent daily swing low is higher than the prior swing low, AND the current price is above the **50-day simple moving average**.

The trend confirmation must have occurred *after* the narrative signal fired (within the prior 5 trading days). A pre-existing uptrend that was already established before the narrative is not a confirmation — it is a different entry type (pure momentum). The confirmation must be a *response* to the narrative catalyst.

### Entry

- Enter at the close of the confirming candle (daily or 4h, whichever timeframe fires the confirmation).
- Position: long spot or low-leverage perp (≤ 2×) on the narrative asset.
- **No short entries:** this strategy does not short at narrative *peak*; it enters only when trend is confirming the narrative. Short entries against exhausted narratives are a different setup ([[crowded-long-funding-fade]], [[unlock-short-with-crowding-gate]]).

### Dual-exit discipline

Exit on whichever fires first:

1. **Narrative decay exit:** the narrative signal has reversed — social volume drops below the 30th percentile of the prior 30 days for 3+ consecutive days, or the sector flow has reversed. This is the "story is over" exit.
2. **Trend break exit:** price closes below the 20-day channel low (Donchian low), OR below the 50-day MA by more than one ATR (to avoid false breaks).
3. **Time stop:** if the position has not shown a 5%+ unrealised gain within 10 trading days from entry, close. The trend-confirmed narrative should start paying quickly; if it does not, the confirmation was false.
4. **Stop loss:** hard stop at 8% adverse from entry price.

### Position sizing

- Base size: 2-3% of sleeve per trade (narrative trades have high crowding risk and high event-driven volatility; small base size preserves capital across multiple signals).
- **Confluence bonus:** if both the breakout trigger (20-day high) AND the higher-low structure are satisfied simultaneously, apply a 1.2× size multiplier — double confirmation of trend momentum.
- Maximum concurrent narrative positions: 3 (to avoid theme concentration when narratives are correlated).

## Implementation pseudocode

```python
# narrative_with_trend_confirmation.py

from dataclasses import dataclass
from typing import Optional

# ---- thresholds ----
SOCIAL_VOL_PCTILE       = 85      # top 15% of 90d history
SECTOR_FLOW_ACCEL       = 2.0     # 2x prior 30d rate
NEWS_MAX_AGE_DAYS       = 3
NARRATIVE_MIN_SCORE     = 50      # from crypto-narratives catalog
CONFIRM_MAX_DAYS_AFTER  = 5       # confirmation must follow narrative within 5 days
TREND_CONFIRM_DAYS      = 20      # Donchian channel period
MA_PERIOD               = 50      # SMA for higher-low check
TIME_STOP_DAYS          = 10
MIN_GAIN_PCT            = 0.05    # 5% gain expected within time stop
HARD_STOP_PCT           = 0.08    # 8% hard stop
NARRATIVE_DECAY_DAYS    = 3       # consecutive days below social-vol 30th pctile
BASE_SIZE_PCT           = 0.025   # 2.5% of sleeve
CONFLUENCE_MULT         = 1.2
MAX_CONCURRENT          = 3
DRAWDOWN_KILL           = 0.30

@dataclass
class NarrativeSignal:
    asset: str
    narrative_fired_date: int    # days ago (0 = today)
    social_vol_pctile: float     # current social vol percentile vs 90d
    sector_flow_accel: float     # current vs prior 30d rate
    has_news_catalyst: bool
    narrative_score: Optional[float]

@dataclass
class TrendState:
    price: float
    channel_high_20d: float      # Donchian 20d high
    channel_low_20d: float       # Donchian 20d low
    sma_50d: float
    recent_swing_low: float
    prior_swing_low: float
    atr_14d: float

def narrative_qualifies(sig: NarrativeSignal) -> bool:
    return (sig.social_vol_pctile >= SOCIAL_VOL_PCTILE or
            sig.sector_flow_accel >= SECTOR_FLOW_ACCEL or
            sig.has_news_catalyst and sig.narrative_fired_date <= NEWS_MAX_AGE_DAYS or
            (sig.narrative_score is not None and sig.narrative_score >= NARRATIVE_MIN_SCORE))

def trend_confirmed(sig: NarrativeSignal, trend: TrendState) -> dict:
    """Returns confirmation type and whether double-confirmed (confluence bonus)."""
    breakout = trend.price > trend.channel_high_20d
    higher_low = (trend.recent_swing_low > trend.prior_swing_low and
                  trend.price > trend.sma_50d)

    if sig.narrative_fired_date > CONFIRM_MAX_DAYS_AFTER:
        return {"confirmed": False, "reason": "narrative too old for this confirmation"}
    if breakout or higher_low:
        return {"confirmed": True, "breakout": breakout, "higher_low": higher_low,
                "confluence": breakout and higher_low}
    return {"confirmed": False, "reason": "no breakout or higher-low above MA"}

def decide_entry(sig: NarrativeSignal, trend: TrendState, book: dict) -> dict:
    if book.get("sleeve_drawdown", 0) > DRAWDOWN_KILL:
        return {"action": "FLAT", "reason": "drawdown kill"}
    if len(book.get("positions", {})) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent positions"}

    if not narrative_qualifies(sig):
        return {"action": "WAIT", "reason": "narrative threshold not met"}

    confirm = trend_confirmed(sig, trend)
    if not confirm["confirmed"]:
        return {"action": "WAIT", "reason": confirm["reason"],
                "narrative_active": True, "note": "waiting for trend confirmation"}

    multiplier = CONFLUENCE_MULT if confirm.get("confluence") else 1.0
    notional = book["sleeve_capital"] * BASE_SIZE_PCT * multiplier

    return {
        "action": "LONG",
        "asset": sig.asset,
        "notional": notional,
        "stop_price": trend.price * (1 - HARD_STOP_PCT),
        "time_stop_days": TIME_STOP_DAYS,
        "confirm_type": ("both" if confirm.get("confluence")
                         else "breakout" if confirm.get("breakout")
                         else "higher_low"),
        "note": f"narrative score ok, trend confirmed, mult={multiplier}x",
    }

def decide_exit(pos: dict, sig: NarrativeSignal, trend: TrendState,
                days_held: int) -> Optional[dict]:
    # narrative decay
    if sig.social_vol_pctile < 30 and getattr(sig, "decay_day_streak", 0) >= NARRATIVE_DECAY_DAYS:
        return {"action": "EXIT", "reason": "narrative decay — social vol below 30th pctile 3d+"}
    # trend break
    if trend.price < trend.channel_low_20d:
        return {"action": "EXIT", "reason": "trend break — price below 20d Donchian low"}
    if trend.price < trend.sma_50d - trend.atr_14d:
        return {"action": "EXIT", "reason": "trend break — price below SMA50 by > 1 ATR"}
    # time stop
    if days_held >= TIME_STOP_DAYS and pos.get("unrealized_return", 0) < MIN_GAIN_PCT:
        return {"action": "EXIT", "reason": "time stop — no 5% gain in 10 days"}
    # hard stop
    if pos.get("unrealized_return", 0) < -HARD_STOP_PCT:
        return {"action": "EXIT", "reason": "hard stop — 8% adverse"}
    return None
```

## Indicators / data used

- **Social volume / social mentions** — the narrative signal source; measured as a percentile vs the asset's own 90-day history to normalise for follower count differences.
- **Sector flow data** — capital rotating into the relevant sector (AI, Layer-2, DeFi, etc.); the flow acceleration criterion.
- **20-day Donchian channel (high/low)** — the breakout confirmation trigger and trend-break exit.
- **50-day simple moving average** — the higher-low structure filter and trend-break exit.
- **ATR(14) daily** — for the SMA-break exit threshold (> 1 ATR from SMA50).
- **[[crypto-narratives]] catalog** — the wiki's backtester-ready narrative impact catalog; provides the narrative score input.

## Example trade

**Setup — AI-agent narrative (illustrative):**

- Asset: TAO (Bittensor) — a protocol whose narrative (decentralised AI compute marketplace) is gaining traction.
- Narrative signal (Day 0): Social volume for TAO is at the 91st percentile of its 90-day history (social-vol gate passes). Narrative score in [[crypto-narratives]] catalog: 72 > 50 (passes). Narrative confirmed.
- Trend state (Day 0): TAO price = $380. 20-day channel high = $378 (price just broke above → breakout gate fires). 50-day SMA = $355. Prior swing low = $320, recent swing low = $342 > $320 (higher-low structure also satisfied).
- Double confirmation (confluence): both breakout AND higher-low above SMA50 → 1.2× size multiplier.
- Sleeve: $50,000. Base size = 2.5% = $1,250. Multiplier 1.2× = **$1,500 notional**.
- Entry: $380. Hard stop: $380 × 0.92 = $349.60.

**Hold (14 days):**
- Day 5: TAO reaches $432 (+13.7%). Social volume remains elevated (85th percentile).
- Day 10: TAO pulls back to $410. 20-day Donchian low = $375 — still above; no trend-break exit. Social volume dips to 65th percentile (not a decay signal yet; 3-day streak not reached).
- Day 12: Narrative score drops to 41 (< 50). Social volume falls to 28th percentile. Decay day streak: 1.
- Day 14: Social volume at 24th percentile — streak = 2 (not yet 3; hold).
- Day 15: Social volume at 21st percentile — streak = 3. **Narrative decay exit fires.**

**Exit at $415.** P&L: ($415 − $380) / $380 × $1,500 = **+$138 on $1,500 deployed** (+9.2% in 15 days). Minus entry taker $0.45 (0.03%), exit taker $0.50 ≈ **net +$137**.

**If trend-confirmation was skipped:** entry on Day 0 at $378 (below the channel high) with pure narrative. TAO had previously tested $395 and failed, retesting $342 (the prior low) before the confirmed breakout. An unconfirmed narrative entry at $378 on Day 0 would have first moved to $342 (-9.5%) before the eventual rally — triggering the 8% hard stop at $347.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.8 | Narrative trading baseline is typically 0.5-0.7 (high crowding risk, moderate edge); trend gate adds ~0.1-0.2 by removing pre-confirmation drawdowns |
| Expected max drawdown | ~30% | Narrative trades in correlated sectors can all reverse simultaneously; the 3-position max limits concentration |
| Win rate | ~50-60% | Higher than pure narrative due to trend filter; the confirmed entry removes the worst-case distribution-phase traps |
| Avg win / avg loss | ~2.0-2.5× | Narrative continuation produces medium-length winners; the dual-exit discipline cuts losses on breakdown |
| Breakeven cost budget | 25 bps | Spot or low-leverage perp taker; social data cost is not in bps terms |
| Signal frequency | Low-moderate | Narrative identifications may be frequent; the confirmation gate rejects an estimated 40-60% |

## Capacity limits

- **Per narrative asset:** narrative assets are typically mid-to-large-cap crypto tokens; capacity to $5-15M per asset depending on liquidity.
- **Aggregate:** `capacity_usd: 30000000` — narrative trades in the same sector (e.g., multiple AI tokens simultaneously) compound crowding risk. At $30M aggregate, the strategy is approaching the level where its own entries begin to move the narrative assets it is trading.
- **Key constraint:** narratives in thin assets (memecoins, micro-caps) have far lower capacity — the social-volume filter must be combined with a minimum market-cap filter (e.g., $100M+) for capacity-constrained deployments.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Narrative crowding (#4).** If social-volume-based narrative identification becomes universal (via free tools like LunarCrush, Santiment, or on-chain sentiment APIs), the confirmation breakout already has competing buyers at lower prices, compressing the available premium. This is the primary risk.
2. **False trend confirmation in chop (#5 / Regime).** In a choppy, low-trend market, a 20-day channel high breakout followed by immediate reversal is common. The trend-gate fires, the entry is made, and the narrative story evaporates within the time stop. Multiple failed confirmations in a row constitute the loss regime for this strategy.
3. **Correlated narrative collapse (#6).** When the macro environment turns risk-off, all narrative assets in the same sector (e.g., all AI tokens) decline simultaneously, and the 3-position maximum is hit with correlated losses. The dual exit and 8% hard stop limit per-trade loss but do not eliminate correlated drawdown.
4. **Narrative identification latency (#3 / Informational).** If the trader's narrative identification lags faster automated tools, the trend-confirmation is already priced by the time the signal fires — the "non-consensus entry" quality is lost.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 30%** in any rolling 60-day window.
2. **Rolling 6-month Sharpe < 0** on minimum 15 trades.
3. **Trend-gate rejection rate > 80%:** the trend rarely confirms after a narrative fires — either identification is too early or the current regime has decoupled narrative flow from price structure.
4. **Loss rate on confirmed entries > 60%** over 20+ consecutive signals — the trend confirmation has stopped being a reliable quality filter.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Removes the most common failure mode of narrative trading:** the "pioneer penalty" — entering before the flow arrives and absorbing the full distribution-phase drawdown. The confirmation gate forces the entry to be *after* the price structure corroborates the narrative.
- **Dual-exit discipline:** exits on either narrative decay OR trend break — whichever is first — rather than waiting for the full narrative cycle to play out. This systematically avoids the secondary-top problem in narrative trades.
- **Interpretable stop levels:** the trend-break exit has a clear level (20-day Donchian low or SMA50 − 1 ATR) that is mechanically observable and not subject to re-interpretation.
- **Composable with size:** the confluence multiplier rewards the strongest setups (both breakout and higher-low confirmed) without requiring a separate strategy.
- **Applicable across narrative types:** the framework is agnostic to narrative content — AI, DePIN, RWA, memecoins — as long as the social-volume / sector-flow / news-catalyst identification is calibrated for the narrative class.

## Disadvantages

- **Higher average entry price than pure narrative:** waiting for the trend confirmation means entering later — after the initial narrative-driven price move has begun. The strategy sacrifices some of the narrative-entry discount for a cleaner structure.
- **Reduced signal frequency:** approximately 40-60% of narrative signals are rejected by the trend gate. In strong bull markets where narratives routinely confirm trend quickly, this is a small cost; in choppy markets, the gate fires frequently and the strategy produces few entries.
- **Social data cost and latency:** reliable social-volume data (LunarCrush, Santiment, The Tie) requires a subscription and has latency; the narrative identification step is the most operationally complex part of the strategy.
- **Does not short:** this strategy only takes long entries. Shorting exhausted narratives is a different (and higher-risk) setup not covered here; see [[crowded-long-funding-fade]] and [[unlock-short-with-crowding-gate]] for short-side narrative expressions.

## Sources

- [[narrative-trading]] — the underlying narrative primitive; all social-attention and flow mechanism documentation from that page applies.
- [[trend-following-cta]] — the trend-following theory underlying the confirmation gate; Donchian channel breakouts and moving-average structures.
- Moskowitz, T., Ooi, Y., Pedersen, L. (2012), *Time series momentum*, Journal of Financial Economics. The momentum persistence that the trend confirmation gate is designed to identify at the asset level.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI does not document specific social-volume endpoints (social data typically comes from LunarCrush, Santiment, or The Tie). The platform contributes the regime and sentiment context used to qualify the setup:

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — market-wide Fear & Greed index; context for narrative regime receptivity (narratives spread faster in greed-dominated markets)
- `GET /api/v1/regimes/current` — current 10-state market regime; avoid narrative long entries in `Established Bear` or `Structural Shock`
- `GET /api/v1/quant/market` — HMM regime probabilities; secondary regime filter

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=<TOKEN>USDT&interval=1d&limit=100` — OHLCV for Donchian channel, SMA50, ATR computation
- `GET /api/v1/market-data/klines?symbol=<TOKEN>USDT&interval=4h&limit=200` — 4h OHLCV for intraday trend-confirmation checks
- `GET /api/v1/market-intelligence/fear-greed-history` — historical Fear & Greed for regime-context backtesting

Social-volume data: external providers (LunarCrush `/coins/{id}/v2`, Santiment `/api/v1/social_volume`, The Tie terminal) must be used for the narrative identification inputs; these are not CryptoDataAPI endpoints.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]], [[cryptodataapi-sentiment]].

**Live dashboards:** [fear & greed](https://cryptodataapi.com/fear-greed) · [long-term regimes](https://cryptodataapi.com/regimes) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the confirmable half of this strategy end-to-end:

- **Regime gate** — `GET /api/v1/regimes/current` and `GET /api/v1/quant/market` run first: no narrative long entries in `Established Bear` / `Structural Shock` or on high `strong_trend_bear` probability
- **Signal** — `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=100` computes the Donchian/SMA50/ATR trend confirmation that qualifies the externally sourced narrative signal
- **Sentiment filter** — `GET /api/v1/sentiment/fear-greed`; narratives propagate faster in greed regimes, so widen the position count only above neutral
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) for the trend leg plus `GET /api/v1/market-intelligence/fear-greed-history` for sentiment context; use `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time regime labels
- **Tips** — the narrative-identification leg stays external (LunarCrush/Santiment); the agent should only autonomously manage the CDA-verifiable trend and regime half, and flag `new_listing` tokens for manual review

## Related

- [[narrative-trading]] — the underlying narrative primitive; this page adds the mandatory trend gate
- [[news-trading]] — event-driven entries; shares the news-catalyst identification step
- [[sentiment-trading]] — sentiment-based entries; overlaps with the social-volume gate
- [[meme-coin-cycle]] — the meme-coin expression of narrative trading; the trend gate is especially valuable here given meme volatility
- [[trend-following-cta]] — the trend primitive providing the confirmation logic
- [[breakout-trading]] — the entry mechanics for the 20-day channel high confirmation
- [[momentum-rotation]] — cross-sectional rotation; narrative assets naturally sort to the top of rotation screens once trend confirms
- [[unlock-aware-momentum]] — momentum gated on an event calendar; different gating mechanism on the same momentum structure
- [[contrarian-extremes]] — the inverse stance: entering when narratives have crashed to sentiment extremes
- [[crypto-narratives]] — the wiki's narrative catalog providing the narrative-score input
- [[moving-average]] — the SMA50 used in the higher-low confirmation rule
- [[edge-taxonomy]] — behavioral + informational edge classification
- [[failure-modes]] — crowding, false confirmation, correlated collapse risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
