---
title: "Unlock-Aware Momentum"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, momentum, event-driven, on-chain, fundamental-analysis, quantitative, crypto, altcoins]
aliases: ["Supply-Calendar Momentum", "Unlock-Gated Trend Following", "Cliff-Aware Momentum Book"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural, informational]
edge_mechanism: "Retail and institutional momentum participants ignore scheduled token supply events and hold through cliff unlocks that predictably apply sell pressure from insider/VC allocations; the strategy de-risks long positions ahead of those events and re-enters after supply has been absorbed, avoiding the structural headwind that kills the majority of crypto momentum blow-ups in altcoins."

data_required: [ohlcv-daily, token-unlock-calendar, open-interest, funding-rates, on-chain-token-distribution]
min_capital_usd: 10000
capacity_usd: 30000000
crowding_risk: low

expected_sharpe: 1.0
expected_max_drawdown: 0.20
breakeven_cost_bps: 35

decay_evidence: "No published study on unlock-gated crypto momentum specifically. The token-unlock price impact is documented empirically: Cieslak and Morse (2023, NBER WP 31348) document persistent price declines around cliff unlock events across 50+ major tokens (median −6% in the 7 days around cliff unlocks). The momentum primitive has well-documented slow decay; the unlock gate is structurally informed, not behavioral, and should decay more slowly as long as unlock calendars remain public."

kill_criteria: |
  - strategy drawdown > 20% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 15-trade sample
  - unlock events no longer produce measurable price impact (average 7-day return around cliff unlocks reverts to zero over 30 events) — the market has pre-priced the supply
  - momentum signal frequency collapses below 2 entries per month across the universe for 3 consecutive months

related: ["[[trend-following-cta]]", "[[momentum-rotation]]", "[[token-unlock-supply-event]]", "[[unlock-short-with-crowding-gate]]", "[[funding-filtered-momentum]]", "[[vol-targeted-trend-following]]", "[[narrative-trading]]", "[[token-unlocks]]", "[[open-interest]]", "[[funding-rate]]", "[[event-driven]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Unlock-Aware Momentum

Unlock-aware momentum is a [[trend-following-cta|momentum]] strategy on crypto altcoin perps and spot that systematically **pauses new long entries and de-risks existing longs** in the 5–10 days ahead of scheduled cliff unlocks and large linear emission events from the token's vesting calendar, and re-enters the momentum position after supply has been absorbed and price structure confirms continuation. The primitive edge is momentum persistence in altcoins; the overlay is a supply-calendar awareness layer that removes the single most predictable structural headwind to carrying altcoin longs.

This is differentiated from [[unlock-short-with-crowding-gate]] — that strategy *actively shorts* into unlocks when crowding conditions (positive funding, peak OI) are also present, expressing a bearish view on the unlock event itself. This page takes no view on the unlock direction — it simply *removes long exposure before the event* and *resets momentum entries after supply digestion*, acting as a risk gate on the long side rather than a directional unlock-fade.

## Edge source

Per [[edge-taxonomy]], this is a **behavioral + structural + informational** combination:

- **Behavioral (primary)** — momentum traders, retail holders, and even some institutional desks systematically ignore or underweight scheduled token unlock events when managing momentum positions. The unlock calendar is public; the failure to act on it is a behavioral error driven by recency bias (the trend has been working, so continue holding) and complexity aversion (tracking vesting schedules across a multi-asset portfolio is operationally inconvenient). The counterparty is the momentum holder who carries through the unlock and absorbs the insider/VC sell pressure.
- **Structural (secondary)** — cliff unlocks release a discrete, non-market-price-sensitive supply of tokens (insiders, VCs, early investors) that must be sold into the secondary market. This supply does not arrive because price is attractive — it arrives on a calendar date. The resulting sell pressure is structural and predictable, not informational. A momentum book that is long heading into the unlock absorbs this supply directly; one that has de-risked avoids it.
- **Informational (tertiary)** — unlock calendars are public information (Tokenomist, Vesting.vc, on-chain vesting contracts). The informational edge is modest — the data is available to anyone — but most systematic momentum strategies do not incorporate calendar data into their position management. The edge comes from acting on available information that peers systematically ignore, not from private access.

## Why this edge exists

Four mechanisms make the overlay additive:

1. **Predictable supply shocks in illiquid altcoins.** A 10% cliff unlock on a token with $100M market cap releases ~$10M in potential selling pressure into a market with perhaps $2-5M daily volume. Even if only 30% is sold immediately, that is ~$3M vs $4M daily turnover — a meaningful structural headwind that momentum cannot easily absorb.

2. **Momentum is strongest just before the unlock.** Paradoxically, tokens often trend strongly in the weeks before a large unlock (anticipatory buying, project team FUD management, narrative pumping ahead of the unlock to minimise insider losses). The momentum signal is genuine — the trend is real. But the unlock is the end of the trend, not a continuation opportunity. De-risking at the momentum peak before the unlock captures most of the trend and avoids the post-unlock reversal.

3. **Post-unlock supply digestion creates re-entry opportunities.** Once insiders have sold their allocation (typically within 7-14 days of the cliff unlock), the overhang is removed. If the fundamental/momentum thesis was valid before the unlock, the trend often resumes. The re-entry after digestion captures the second leg at lower risk.

4. **Calendar information is operationally costly to maintain.** Tracking unlock calendars for 20+ altcoins requires a systematic data infrastructure. Most discretionary and even many systematic traders do not build this. The edge is in the operational discipline.

**Who is on the other side:** the momentum holder who carries their altcoin long through the cliff unlock, absorbing insider and VC selling that predictably arrives on a publicly known date. Their failure is behavioral (recency bias + operational cost avoidance).

## Null hypothesis

Under the null, cliff unlock events carry no predictable price impact: the market fully pre-prices the supply event, and average returns in the 7-day window around the cliff are statistically indistinguishable from non-event windows. Specifically:
- The average 7-day return around cliff unlocks (in-event window) should equal the average 7-day return in non-event windows, after controlling for momentum regime.
- A momentum strategy with the unlock pause gate should have the same Sharpe and drawdown as an unfiltered momentum strategy.

Empirical evidence partially rejects the null. Cieslak and Morse (2023, NBER WP 31348) document median −6% 7-day returns around cliff unlocks across 50+ tokens. The null is further rejected in this wiki's related pages: [[token-unlock-supply-event]] documents specific Hyperliquid basket patterns around major unlocks. The null is not yet formally rejected for this specific combination strategy (`backtest_status: untested`).

## Rules

### Universe

- Altcoin perps and spot with scheduled token vesting events. **Not applicable to BTC, ETH, or fully-diluted tokens** (no more vesting supply). Target tokens with:
  - Circulating supply < 80% of max supply (meaningful remaining emissions).
  - At least one cliff unlock or scheduled linear emission event in the next 30 days, identifiable from a vesting calendar data source.
  - Minimum $20M daily spot volume and $10M daily perp volume (sufficient liquidity to exit positions quickly).

### Momentum signal

Any of the following defines an active momentum long:
1. Price above 20-day channel high (Donchian breakout).
2. EMA(12) above EMA(26) on the daily chart.
3. 20-day rate of change > +15%.

### Unlock pre-event risk management (long-side gate)

**5 days before a cliff unlock:**
- **Freeze new longs**: no new long momentum entries allowed for this asset. Existing entries may remain open.
- **Reduce existing longs by 50%**: trim the position by half on the 5th day before the unlock.

**2 days before a cliff unlock:**
- **Close all remaining longs**: exit the position fully. Do not hold any long through the cliff date ±2 days.

**During the cliff unlock window (−2 to +7 days from cliff date):**
- No new longs. The position is flat. Allow the market to process the supply.

### Post-event re-entry conditions

Re-entry is permitted after ALL of the following:
1. **Cliff unlock date has passed by ≥ 7 calendar days.**
2. **Price momentum is still active** — the same momentum signal that justified the original entry is still firing (price above breakout level, or EMA cross still positive).
3. **Price has not fallen more than 15% from the pre-unlock level.** If it has, the unlock was the catalyst for a larger reversal — wait for a new momentum signal.
4. **Funding is not stretched positive** — apply the same funding gate from [[funding-filtered-momentum]] (funding ≤ 0.04%/8h) to avoid re-entering into a newly crowded post-unlock trade.
5. **OI recovering** — 24h OI change is non-negative or mildly positive (new money re-entering post-supply digestion).

### Exit conditions for normal (non-unlock) positions

1. **Momentum reversal**: price breaks back below the 20-day channel low or EMA(12) crosses below EMA(26).
2. **Funding kill**: funding rises above 0.08%/8h → trim or exit (shared with [[funding-filtered-momentum]]).
3. **Unlock trigger fires**: pre-event gate activates (overrides all else on the long side).
4. **Time stop**: 10 days without positive mark-to-market.

### Position sizing

- Base sizing: ATR(14, daily) denominated; target 1% sleeve risk per position.
- **Post-digestion re-entry upweight**: on re-entry after confirmed supply digestion (unlock passed, momentum still active, OI recovering), apply 1.15× multiplier — supply overhang has been resolved, the continuation trade has a cleaner setup.
- Maximum single position: 10% of sleeve.
- Maximum concurrent: 4 assets (broader universe than single-asset momentum due to altcoin diversification benefit).

## Implementation pseudocode

```python
# unlock_aware_momentum.py — decision loop with calendar gate

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional, List

# ---- thresholds ----
MOMENTUM_LOOKBACK     = 20       # N-day channel for Donchian breakout
EMA_FAST, EMA_SLOW    = 12, 26   # daily EMA periods
ROC_MIN               = 0.15     # 20-day rate of change > 15% alternative
UNLOCK_PAUSE_DAYS     = 5        # freeze new entries this many days before unlock
UNLOCK_TRIM_DAYS      = 5        # trim existing 50% this many days before unlock
UNLOCK_CLOSE_DAYS     = 2        # close fully this many days before unlock
POST_UNLOCK_WAIT      = 7        # calendar days after unlock before re-entry allowed
MAX_POST_UNLOCK_DROP  = 0.15     # if price drops >15% post-unlock, wait for new signal
FUNDING_MAX_LONG      = 0.0004   # 0.04%/8h funding cap at re-entry
OI_MIN_CHANGE         = -0.05    # OI cannot be collapsing at re-entry
TARGET_RISK_PCT       = 0.01     # 1% of sleeve per trade
UPWEIGHT_REENTRY      = 1.15
MAX_POS_PCT           = 0.10
MAX_CONCURRENT        = 4
DRAWDOWN_KILL         = 0.20

@dataclass
class AssetSignal:
    asset: str
    price: float
    ema_fast: float; ema_slow: float
    channel_high_20d: float; channel_low_20d: float
    roc_20d: float
    funding_8h: float
    oi_change_24h_pct: float
    atr_14d: float
    next_cliff_date: Optional[date]   # None if no upcoming cliff
    pre_unlock_price: Optional[float] # price 1d before unlock (for drop check)
    days_since_entry: int

def days_to_unlock(sig: AssetSignal, today: date) -> Optional[int]:
    if sig.next_cliff_date is None:
        return None
    return (sig.next_cliff_date - today).days

def momentum_long(s: AssetSignal) -> bool:
    return ((s.price > s.channel_high_20d and s.ema_fast > s.ema_slow)
            or s.roc_20d > ROC_MIN)

def decide(s: AssetSignal, book: dict, today: date) -> dict:
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    dtl = days_to_unlock(s, today)
    pos = book["positions"].get(s.asset)

    if pos is not None:
        # --- unlock pre-event gates (override all other logic) ---
        if dtl is not None and dtl <= UNLOCK_CLOSE_DAYS:
            return {"action": "EXIT", "asset": s.asset,
                    "reason": f"unlock in {dtl}d: close all longs"}
        if dtl is not None and dtl <= UNLOCK_TRIM_DAYS:
            if not pos.get("trimmed_for_unlock"):
                return {"action": "TRIM_50PCT", "asset": s.asset,
                        "reason": f"unlock in {dtl}d: trim 50%"}
        # --- standard exits ---
        if not momentum_long(s):
            return {"action": "EXIT", "asset": s.asset, "reason": "momentum reversed"}
        if s.funding_8h > 0.0008:  # 0.08%/8h kill
            return {"action": "EXIT", "asset": s.asset, "reason": "funding kill"}
        if s.days_since_entry >= 10 and pos.get("unrealized_pnl", 0) <= 0:
            return {"action": "EXIT", "asset": s.asset, "reason": "time stop"}
        return {"action": "HOLD", "asset": s.asset}

    # --- new entry logic ---
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}

    # block if within unlock window
    if dtl is not None and dtl <= UNLOCK_PAUSE_DAYS:
        return {"action": "WAIT",
                "reason": f"unlock in {dtl}d: new entries blocked"}

    # block if too soon after unlock (post-event wait)
    if s.next_cliff_date and (today - s.next_cliff_date).days < POST_UNLOCK_WAIT:
        return {"action": "WAIT", "reason": "post-unlock supply digestion window"}

    if not momentum_long(s):
        return {"action": "WAIT", "reason": "no momentum signal"}
    if s.funding_8h > FUNDING_MAX_LONG:
        return {"action": "WAIT", "reason": "funding gate"}
    if s.oi_change_24h_pct < OI_MIN_CHANGE:
        return {"action": "WAIT", "reason": "OI collapsing"}

    # post-unlock re-entry: check price drop and apply upweight
    is_reentry = (s.next_cliff_date
                  and 7 <= (today - s.next_cliff_date).days <= 21)
    if is_reentry and s.pre_unlock_price:
        drop = (s.pre_unlock_price - s.price) / s.pre_unlock_price
        if drop > MAX_POST_UNLOCK_DROP:
            return {"action": "WAIT",
                    "reason": "post-unlock price drop >15%: wait for new signal"}

    multiplier = UPWEIGHT_REENTRY if is_reentry else 1.0
    notional = min(
        TARGET_RISK_PCT * book["sleeve_capital"] / (s.atr_14d / s.price),
        MAX_POS_PCT * book["sleeve_capital"]
    ) * multiplier
    label = "re-entry post-supply-digestion" if is_reentry else "momentum breakout"
    return {"action": "LONG", "asset": s.asset, "notional": notional, "reason": label}
```

The production system adds: daily unlock calendar ingestion from Tokenomist or Vesting.vc API; Slack/email alert 6 days before each cliff for manual review; CryptoDataAPI funding polling for re-entry gate; and integration with the broader momentum signal library.

## Indicators / data used

- **Momentum signals (daily)** — 20-day Donchian channel breakout, EMA(12)/EMA(26) cross, 20-day ROC > 15%. Any one suffices.
- **Token unlock calendar** — cliff dates, unlock sizes, and vesting schedules. Sources: Tokenomist.ai, Vesting.vc, token foundation disclosure, on-chain vesting contract state.
- **[[funding-rate]] (8h)** — re-entry gate; same threshold as [[funding-filtered-momentum]] (≤ 0.04%/8h).
- **[[open-interest]] (24h change)** — OI recovery check at re-entry.
- **ATR(14, daily)** — position sizing denominator.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Asset: LAYER-PERP on Hyperliquid (hypothetical Layer-1 token).
- Price has been in a strong uptrend for 3 weeks: +38% from $1.20 to $1.66. EMA(12) > EMA(26) daily. Momentum signal: **active**.
- Funding: +0.011%/8h — below the 0.04% gate. Momentum entry qualifies under unfiltered conditions.
- **Unlock calendar check**: LAYER has a cliff unlock on 2026-08-15 releasing 8% of total supply (VC tranche, $48M at current price).
- Today is 2026-08-10: 5 days to cliff. **Freeze new entries**, trim existing 50%.

**Without unlock awareness:** An unfiltered momentum trader holds through the cliff. On 2026-08-16, insiders sell $14M over 3 days. LAYER falls 19% to $1.34. Momentum signal reverses. Exit at $1.34. Entry at $1.36 (earlier). Net: −1.5% on notional, plus lost opportunity cost of 3 weeks of trend.

**With unlock awareness:**
- Entry at $1.36 (momentum breakout, 15 days before unlock) — initial long.
- Day 10 (5 days to cliff): trim 50% at $1.62 (+19.1% on trimmed half).
- Day 13 (2 days to cliff): close remaining 50% at $1.64 (+20.6% on second half).
- Post-unlock wait: observe price falls to $1.38 over 7 days as VCs sell. Day 22 (7 days post-cliff): check re-entry conditions.
  - Price $1.38 — within 15% of pre-unlock level ($1.64) → 15.9% drop — just above the 15% threshold, so re-entry requires new signal.
  - On day 25: price recovers to $1.42, EMA cross re-fires, funding at +0.008%, OI rising. Re-entry at $1.42 with 1.15× size.

**Net P&L (rough):** Leg 1 (50% at $1.36 → $1.62): +19.1%. Leg 2 (50% at $1.36 → $1.64): +20.6%. Re-entry not fully evaluated (separate trade). Versus holding through: +1.5% on notional at best (if held entry to $1.42 re-entry) — but with a 19% peak drawdown in between and a momentum reversal signal.

*(Illustrative. Not a backtest. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Altcoin momentum ~0.5-0.8 unfiltered; unlock gate removes the predictable structural headwind |
| Expected max drawdown | ~20% | Dominated by false breakouts in choppy markets; unlocks no longer the primary source of momentum drawdowns |
| Win rate per momentum cycle | ~45-55% | Momentum base rate; filter reduces frequency of unlock-caused reversals |
| Avg win / avg loss | ~2.5-3.0× | Altcoin momentum can produce large wins; filter captures more of the run before the supply hit |
| Breakeven cost budget | 35 bps | Higher than BTC momentum due to wider spreads on altcoin perps |
| Expected reduction in drawdown from unlock gate | 3-8 pct points | Based on median −6% 7-day impact around cliff unlocks (Cieslak-Morse 2023) for a 50% position trimmed 5 days before |

## Capacity limits

- **Per asset on altcoin perps**: ~$2-10M depending on liquidity. The unlock gate is most valuable on mid-cap altcoins where unlock-related selling is large relative to daily volume.
- **Cross-asset universe of 10-20 tokens**: ~$30M combined. More tokens = more unlock calendar management overhead.
- **Hard constraint**: at higher AUM, the trim-on-day-5 order and close-on-day-2 order become price-moving on thin altcoin perps. Exit execution must be gradual (TWAP over the final 48h window before close).

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Unlock calendar error (#7: Operational).** The primary risk: the calendar shows no upcoming unlock but an unannounced or misrecorded cliff occurs. This is a data quality problem — vesting calendars are not always perfectly maintained, and some tokens have complex multi-tranche schedules. Cross-check against on-chain vesting contract state and multiple calendar sources.
2. **Market pre-prices the unlock (#4).** If the market is so efficient that price has already corrected for the upcoming unlock before the 5-day gate fires, de-risking destroys good positions unnecessarily. The rule still has expected value (the median impact is −6%), but individual instances will be wrong. Accept this as a statistical trade-off.
3. **Momentum signal decays (#5: The Regime Changed).** In a choppy market with no trending, momentum has no edge; the unlock gate cannot save a broken primitive. The momentum condition for entry and re-entry handles this — if momentum is not active, no position is taken.
4. **Post-unlock recovery fails (#5).** The asset does not recover after supply digestion. The re-entry conditions (price not >15% below pre-unlock, momentum re-fires) provide a filter, but a fundamentally damaged asset can still trigger momentum by bouncing briefly before the next leg down.
5. **Unlock gate crowding (#4).** If many strategies adopt the same 5-day exit rule, the selling accelerates 5 days before (everyone trims simultaneously). This shifts the price impact to day −5 rather than day 0, potentially reducing the benefit of the early exit. Re-calibrate the pre-event window (try 7 or 10 days) if crowding is detected.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 20%** in any rolling 30-day window.
2. **Rolling 6-month Sharpe < 0** on a minimum 15-trade sample.
3. **Unlock events no longer predictive**: average 7-day return around cliff unlocks reverts to within ±2% of baseline non-event windows over 30 consecutive events — the market has pre-priced supply. Review calendar source quality and consider extending the pre-event window.
4. **Momentum signal frequency collapse**: fewer than 2 qualifying momentum entries per calendar month across the full universe for 3 consecutive months.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Removes the single most predictable structural headwind** to altcoin momentum: insider/VC selling on a publicly known calendar date.
- **Locks in trend gains before the supply hit**: the gradual trim + full exit captures the majority of the trend profit without requiring perfect timing of the unlock impact.
- **Creates a clean post-supply re-entry**: by stepping aside and re-entering after digestion, the strategy captures the second leg of the trend at a lower risk point.
- **Public information, operational edge**: the calendar data is freely available; the edge comes from acting on it systematically when most peers do not.
- **Stackable**: compatible with [[funding-filtered-momentum]] (apply the funding filter at both initial entry and re-entry), [[vol-targeted-trend-following]] (scale by realised volatility), and cross-sectional [[momentum-rotation]] (override the rotation to exit the token heading into unlock).

## Disadvantages

- **Operational overhead**: maintaining an accurate unlock calendar for 10-20 tokens requires a systematic data pipeline. Manual maintenance is error-prone and time-consuming.
- **Early exit cost**: the strategy exits before the unlock impact materialises. If the market does not react to the unlock (supply absorbed silently), the early exit sacrifices the remaining trend profit for no benefit.
- **Re-entry complexity**: the post-unlock re-entry rules add a second decision node after each unlock event. If the re-entry criteria are too strict, the strategy misses the post-supply continuation; too loose, it re-enters into a continuing decline.
- **Not applicable to fully diluted tokens**: BTC, ETH, and any token with ≥ 80% circulating supply have no meaningful unlock dynamics. The strategy's universe is limited to altcoins with remaining vesting schedules.
- **Calendar data quality risk**: vesting schedules change (delays, acceleration, protocol governance votes). The risk of a miscalibrated calendar is operationally managed, not hedged.

## Sources

- Cieslak, A. and Morse, A. (2023), *Token supply shock and crypto markets*, NBER Working Paper 31348. Median −6% 7-day price impact around cliff unlock events across 50+ tokens; primary empirical basis for the unlock gate. https://www.nber.org/papers/w31348
- [[token-unlock-supply-event]] — the Hyperliquid basket that trades unlock events directly; the complementary short-side strategy.
- [[unlock-short-with-crowding-gate]] — the active unlock short in this wiki; the nearest neighbor for the short side.
- [[token-unlocks]] — concept and calendar mechanics.
- [[trend-following-cta]] — the underlying momentum primitive.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=LAYER` — funding rate for re-entry gate check
- `GET /api/v1/derivatives/open-interest?coin=LAYER` — OI recovery confirmation at re-entry
- `GET /api/v1/event/regime/score` — event risk composite; complement to manual unlock calendar for high-impact event detection

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=LAYERUSDT&interval=1d&limit=200` — daily OHLCV for momentum signal computation (Donchian, EMA, ROC)
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI) for re-entry condition backtest
- `GET /api/v1/backtesting/funding` — funding archive for multi-regime backtest of funding gate at re-entry

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — daily klines (`GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=200`) compute the Donchian/EMA/ROC momentum stack
- **Event gate** — `GET /api/v1/event/calendar?type=unlock&days=14` and `GET /api/v1/event/regime/score` flatten momentum longs ahead of qualifying unlocks
- **Re-entry filter** — `GET /api/v1/derivatives/funding-rates?coin={TOKEN}` and `GET /api/v1/derivatives/open-interest?coin={TOKEN}` must normalize before the position is restored post-unlock
- **Backtest** — momentum replay on `GET /api/v1/backtesting/klines` (1d back to 2017-08 for majors; Hyperliquid daily candles only reach the 2023 launch); funding-gate replay windows: Hyperliquid hourly since 2023-05, Binance daily since 2026-03-30
- **Tips** — unlock names are usually recent listings — expect `new_listing` / `insufficient_history` flags, and cross-check the CDA calendar against an external unlock tracker for low-cap tokens

## Related

- [[trend-following-cta]] — the underlying momentum primitive; this page is the calendar-gate extension
- [[momentum-rotation]] — cross-sectional momentum rotation; stackable overlay
- [[funding-filtered-momentum]] — gates momentum on funding state; compatible overlay for re-entry
- [[vol-targeted-trend-following]] — scales momentum by realised volatility; stackable overlay
- [[token-unlock-supply-event]] — the Hyperliquid basket for unlock trading (same event, short-side expression)
- [[unlock-short-with-crowding-gate]] — active unlock short with crowding confirmation; the long-side complement
- [[narrative-trading]] — narrative plays often precede the pre-unlock price run; overlap in entry catalysts
- [[token-unlocks]] — unlock calendar mechanics and data sources
- [[open-interest]] — OI recovery check at re-entry
- [[funding-rate]] — re-entry funding gate
- [[behavioral-finance-overview]] — recency bias and operational cost avoidance
- [[event-driven]] — the broader category of calendar-triggered strategy adjustments
- [[edge-taxonomy]] — behavioral + structural + informational classification
- [[failure-modes]] — calendar-error and momentum-decay risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
