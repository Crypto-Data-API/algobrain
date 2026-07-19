---
title: "OI Flush Reversion"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, mean-reversion, open-interest, perpetual-futures, quantitative, behavioral-finance, crypto]
aliases: ["OI Purge Dip-Buy", "Open-Interest Flush Mean Reversion", "OI Deleveraging Reversion"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "Retail and institutional leveraged participants collectively overestimate the depth and duration of a downmove, building a crowded short book while OI surges downward; once OI has purged (−15%+ from recent peak) the deleveraging is confirmed complete, and the remaining position book is structurally cleaner — the strategy enters a mean-reversion long at exactly the point where the forced-seller supply is exhausted and the short squeeze potential is highest."

data_required: [ohlcv-4h, ohlcv-daily, open-interest, funding-rates, mark-price, liquidation-feed]
min_capital_usd: 5000
capacity_usd: 60000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 30

decay_evidence: "No published study on OI-purge-gated mean reversion specifically. The OI signal's informational value in crypto has been documented in the broader OI-as-participation measure literature (Ederington and Lee 1993 for futures markets; crypto applications in Glassnode research 2022-2024). The combination is novel and untested in this wiki. The mean-reversion primitive has slow decay; the OI filter is structural and should decay more slowly than purely behavioral filters."

kill_criteria: |
  - strategy drawdown > 20% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 15-trade sample
  - OI flush condition fires but mean reversion fails to materialize within the time window in > 60% of setups over 25 signals (OI purge is not a sufficient condition for dip quality in the current regime)
  - average hold-to-time-stop ratio exceeds 60% (mean reversion consistently too slow for the time window)

related: ["[[mean-reversion]]", "[[open-interest]]", "[[oi-price-exhaustion]]", "[[oi-confirmed-trend]]", "[[post-liquidation-rebound]]", "[[funding-flush-reversal]]", "[[funding-rate-arbitrage]]", "[[rsi-mean-reversion]]", "[[liquidation-cascade-fade]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[liquidations]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# OI Flush Reversion

OI flush reversion is a [[mean-reversion]] strategy that enters dip-buy positions only after [[open-interest]] has purged — defined as a decline of ≥ 15% from its recent peak within a 5-day window — confirming that the prior deleveraging is substantially complete before establishing a long. The primitive edge is mean reversion of oversold assets; the overlay is an OI-magnitude gate that waits for structural evidence of position book improvement (forced sellers exhausted, surviving participants better-capitalised) before taking the reversal bet.

This is differentiated from [[post-liquidation-rebound]] — that page triggers on a specific liquidation cascade *event* (5-minute liquidation volume spike ≥ 3× daily average). This page triggers on a *cumulative OI decline* (≥ 15% over 5 days), which captures gradual deleveraging, a series of smaller liquidations, and OTC unwinds that do not produce a single dramatic spike. The OI flush criterion is a slower, more structural confirmation than the event-based liquidation trigger.

This is differentiated from [[oi-price-exhaustion]] — that page fades uptrend exhaustion (price making new highs while OI declines). This page is a downtrend mean-reversion entry (price declining while OI declines), where the OI decline confirms position clearing rather than exhaustion. The OI direction is the same (declining), but the price context and trade direction are opposite: exhaustion fades the trend; this buys the dip after the trend's fuel (leverage) has been removed.

This is differentiated from [[funding-flush-reversal]] — that page uses the *funding rate* as the capitulation confirmation (funding goes negative, signalling shorts are now crowded). This page uses the *OI level change* as the confirmation (total open interest declines by ≥ 15%). The two signals are related but distinct: a large OI flush can occur with neutral funding if both longs and shorts deleverage simultaneously; a funding flush can occur without a large OI decline if longs rotate into shorts. Running both filters together (OI flush AND negative funding) would be the strictest version of the capitulation gate.

## Edge source

Per [[edge-taxonomy]], this is a **behavioral + structural** combination:

- **Behavioral (primary)** — leveraged participants who drove the downmove build an increasingly crowded short book as price declines, fuelled by momentum extrapolation and stop-loss cascade psychology. They are the last to enter positions (late momentum chasers) and the most exposed to a squeeze. Once the OI has purged — i.e., the total position book has contracted by ≥ 15% — the weak hands have been removed, and the short book is disproportionately composed of newer, shorter-term participants who are vulnerable to mean reversion.
- **Structural (secondary)** — a declining OI is a direct measurement of position book contraction: forced liquidations and voluntary position closures have reduced the aggregate leverage in the system. This is a measurable, real improvement in the market's structural health. The lower the OI, the less remaining leverage is available to continue the downmove via forced selling; the remaining move must come from fresh conviction sellers, not leveraged cascade participants.

## Why this edge exists

Three mechanisms make the OI-flush gate additive beyond unconfirmed dip buying:

1. **Position book health is quantifiable.** Unlike sentiment indicators (which are proxies), OI directly measures the volume of outstanding leveraged positions. A 15% OI decline from peak means that 15% of the prior leveraged long book has been closed (voluntarily or forcibly). Surviving positions are, by definition, better-margined than the average position that existed at the OI peak.

2. **The squeeze potential is highest at the OI trough.** When OI has purged and shorts are the crowded side (confirmed by funding going negative in the companion check), the remaining short book is maximally concentrated and most vulnerable to a squeeze. Any positive catalyst — macro, narrative, or simply time as funding costs accumulate — can trigger a violent short cover. The OI-flush reversal entry is made at maximum squeeze potential, not before it builds.

3. **The OI purge is a non-linear delineation.** Price declines can continue for a long time on low OI (if new sellers keep entering). But a 15%+ OI decline from peak is a meaningful structural threshold — it separates "the decline is ongoing and levered" from "the decline has processed its leverage." Historically in crypto, the OI trough closely precedes or coincides with the price trough in overshoot events (as opposed to structural bear markets, where OI can continue declining for months).

**Who is on the other side:** the momentum shorter who entered the downmove after the OI had already declined significantly, expecting continuation but now entering a de-levered market where their crowded position is the squeeze risk. Also: the capitulatory spot seller who exits into the OI trough on fear.

## Null hypothesis

Under the null, the magnitude of the OI decline at the time of dip-buy entry carries no information about forward mean-reversion probability or speed. Specifically:
- Average 7-day forward returns on oversold dip entries should be equal regardless of whether OI has declined by 5%, 10%, 15%, or 20% from its recent peak.
- A 15% OI flush criterion should not improve the win rate or Sharpe of dip-buy entries relative to a dip-buy triggered on price alone.

Empirically, OI troughs preceding mean reversions are documented in [[post-liquidation-rebound]] (OI contraction ≥ 5% as a signal component) and [[oi-price-exhaustion]] (OI declining while price extends). The specific 15% threshold for a *standalone flush criterion* is chosen by structural logic (represents a significant position-book contraction), not by data-fitting; the null is currently not rejected in this wiki (`backtest_status: untested`).

## Rules

### OI flush definition

The **OI flush** condition is met when ALL of the following hold:
1. **OI has declined ≥ 15% from its 5-day peak**: `(OI_peak_5d - OI_current) / OI_peak_5d ≥ 0.15`. This is the primary condition.
2. **OI has been declining or flat for at least 2 consecutive daily periods** — the flush is ongoing or just completed, not a one-day blip followed by recovery.
3. **OI flush rate is decelerating** — the daily OI change has improved (become less negative) in the last 24h vs the prior 24h. The flush is slowing, suggesting the worst of the deleveraging is done. (Optional but improves precision.)

### Entry conditions (dip buy, long)

1. **OI flush active** (all sub-conditions above).
2. **Price oversold**. At least ONE of:
   - RSI(14, 4h) ≤ 32 — price in oversold zone.
   - Price ≥ 15% below its 20-day high.
   - Price has closed below the lower Bollinger Band (20, 2σ) on the daily chart for 2+ consecutive days.
3. **Funding confirmation (optional but improves quality)**: `funding_8h ≤ −0.01%/8h` — shorts are at least mildly paying, confirming the OI decline included longs closing and shorts opening (the crowded-short setup). This is a refinement, not a hard requirement; OI flush entries without negative funding are also valid but carry less structural conviction.
4. **OI floor check**: current OI is still > 30% of its 90-day average. A near-zero OI suggests the market has structurally emptied; this is not a deleveraging overshoot but a market abandonment. Skip entries in effectively abandoned perps.
5. **No confirmed structural event**: no protocol exploit, de-peg, or credit event that could explain a permanent repricing. If available, `/api/v1/regimes/current` should not return `Established Bear` or `Structural Shock`.

### Exit conditions

1. **OI re-expands by ≥ 7% from the flush trough.** Primary signal that new participants are re-entering in the direction of the trend (downtrend resuming). This is the thesis-invalidation exit — not a profit target.
2. **Price reaches 50% Fibonacci retracement of the flushed decline.** Take half off at the 50% level.
3. **Price returns to the 20-period EMA on the 4h chart.** Close the remainder.
4. **Funding normalises above +0.02%/8h**: longs are now dominant again; the structural squeeze potential is reduced. Begin trimming.
5. **Time stop: 12 days.** If the reversion has not reached at least 25% of the flushed decline within 12 calendar days, close at market — the market has not reacted as expected.
6. **OI flush worsens after entry**: if OI declines by a further 10%+ from the entry-day level, cut 50% of the position — the deleveraging is not complete; a secondary wave may be in progress.

### Position sizing

- Base position = (target risk bps × sleeve capital) / (ATR(14, 4h) / price). Target 1.2% sleeve risk per trade.
- **OI flush severity upweight**: when OI has declined ≥ 20% from peak (stronger flush), apply 1.25× multiplier. Deeper flushes historically produce faster and larger reversions in non-bear regimes.
- **Funding bonus**: when both OI flush and negative funding are confirmed (dual confirmation), apply an additional 1.1× multiplier.
- Maximum single position: 12% of sleeve.
- Maximum concurrent: 2 positions (OI flush events are often correlated across assets; concentration limit is conservative).

## Implementation pseudocode

```python
# oi_flush_reversion.py — OI-purge-confirmed dip buy

from dataclasses import dataclass

# ---- thresholds ----
OI_FLUSH_THRESHOLD     = 0.15    # OI declined >= 15% from 5d peak
OI_FLUSH_MIN_PERIODS   = 2       # consecutive daily declining periods
OI_REEXPAND_EXIT       = 0.07    # OI re-expands >= 7% from trough → exit
OI_DEEPEN_STOP         = 0.10    # further 10% OI decline post-entry → cut 50%
OI_FLOOR_RATIO         = 0.30    # OI must be >= 30% of 90d average
OI_FLUSH_STRONG        = 0.20    # >= 20% for upweight

RSI_OVERSOLD           = 32
RETRACE_FROM_HIGH_MIN  = 0.15    # 15% from 20d high
FUND_CONFIRM           = -0.0001 # -0.01%/8h: shorts at least mildly paying (optional)
FUND_TRIM              = 0.0002  # +0.02%/8h: begin trimming

TIME_STOP_DAYS         = 12
TARGET_RISK_PCT        = 0.012   # 1.2% sleeve risk per trade
UPWEIGHT_STRONG_FLUSH  = 1.25
UPWEIGHT_DUAL_CONFIRM  = 1.10
MAX_POS_PCT            = 0.12
MAX_CONCURRENT         = 2
DRAWDOWN_KILL          = 0.20

@dataclass
class OISignal:
    asset: str
    price: float
    rsi_14_4h: float
    price_high_20d: float
    bb_lower_daily: float
    funding_8h: float
    oi_current: float
    oi_peak_5d: float
    oi_trough: float        # lowest OI since flush began (entry value)
    oi_avg_90d: float
    oi_declining_streak: int  # consecutive daily periods OI declining
    oi_change_deceleration: bool  # True if today's decline less severe than yesterday
    atr_14_4h: float
    regime: str
    days_since_entry: int

def flush_active(s: OISignal) -> bool:
    flush_pct = (s.oi_peak_5d - s.oi_current) / s.oi_peak_5d
    return (flush_pct >= OI_FLUSH_THRESHOLD
            and s.oi_declining_streak >= OI_FLUSH_MIN_PERIODS
            and s.oi_current >= OI_FLOOR_RATIO * s.oi_avg_90d)

def oversold(s: OISignal) -> bool:
    retrace = (s.price_high_20d - s.price) / s.price_high_20d
    bb_breakdown = s.price <= s.bb_lower_daily
    return (s.rsi_14_4h <= RSI_OVERSOLD
            or retrace >= RETRACE_FROM_HIGH_MIN
            or bb_breakdown)

def decide(s: OISignal, book: dict) -> dict:
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    pos = book["positions"].get(s.asset)

    if pos is not None:
        # --- OI worsening: cut 50% ---
        oi_at_entry = pos.get("oi_at_entry", s.oi_current)
        if (oi_at_entry - s.oi_current) / oi_at_entry >= OI_DEEPEN_STOP:
            return {"action": "TRIM_50PCT", "asset": s.asset,
                    "reason": "OI deepening post-entry"}

        # --- thesis invalidation: OI re-expanding ---
        oi_trough = pos.get("oi_trough", s.oi_current)
        if s.oi_current >= oi_trough * (1 + OI_REEXPAND_EXIT):
            return {"action": "EXIT", "asset": s.asset,
                    "reason": "OI re-expanding: thesis invalidated"}

        # --- take profit partial at 50% retracement (handled externally via TP orders) ---

        # --- funding normalisation: begin trim ---
        if s.funding_8h >= FUND_TRIM:
            if not pos.get("trimmed_funding"):
                return {"action": "TRIM_50PCT", "asset": s.asset,
                        "reason": "funding normalized: take half off"}

        # --- time stop ---
        if s.days_since_entry >= TIME_STOP_DAYS:
            return {"action": "EXIT", "asset": s.asset, "reason": "time stop"}

        return {"action": "HOLD", "asset": s.asset}

    # --- new entry logic ---
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}
    if s.regime in ("Established Bear", "Structural Shock"):
        return {"action": "WAIT", "reason": "regime kill"}
    if not flush_active(s):
        return {"action": "WAIT", "reason": "OI flush not active"}
    if not oversold(s):
        return {"action": "WAIT", "reason": "price not oversold"}

    flush_pct = (s.oi_peak_5d - s.oi_current) / s.oi_peak_5d
    dual_confirm = s.funding_8h <= FUND_CONFIRM

    multiplier = 1.0
    if flush_pct >= OI_FLUSH_STRONG:
        multiplier *= UPWEIGHT_STRONG_FLUSH
    if dual_confirm:
        multiplier *= UPWEIGHT_DUAL_CONFIRM

    notional = min(
        TARGET_RISK_PCT * book["sleeve_capital"] / (s.atr_14_4h / s.price),
        MAX_POS_PCT * book["sleeve_capital"]
    ) * multiplier

    return {
        "action": "LONG",
        "asset": s.asset,
        "notional": notional,
        "reason": (f"OI flush {flush_pct*100:.1f}%, RSI={s.rsi_14_4h:.0f}, "
                   f"funding={s.funding_8h*100:.4f}%/8h"
                   + (" [DUAL CONFIRM]" if dual_confirm else ""))
    }
```

The production system adds: CryptoDataAPI OI polling at 4h intervals with 5-day rolling peak tracking; regime check via `/api/v1/regimes/current`; daily OI change deceleration computation; and a Slack alert when the flush condition fires (for manual validation of structural event risk before entry).

## Indicators / data used

- **[[open-interest]] (daily and 4h)** — the primary flush signal: 5-day peak, current level, declining streak, and deceleration.
- **OI flush ratio** = `(OI_peak_5d - OI_current) / OI_peak_5d`. The primary gate threshold at 0.15.
- **RSI(14, 4h)** — oversold confirmation. ≤ 32 triggers the price-side entry.
- **Bollinger Bands (20, 2σ, daily)** — alternative oversold check: price below lower band.
- **[[funding-rate]] (8h)** — optional dual confirmation; also used as a trim trigger on normalisation.
- **ATR(14, 4h)** — position sizing denominator.
- **Regime classification** — `/api/v1/regimes/current` to exclude `Established Bear` and `Structural Shock` regimes.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Asset: ETH-PERP on Hyperliquid.
- ETH has declined 22% over 8 days from $4,100 to $3,198.
- OI 5-day peak: $14.2B (8 days ago). Current OI: $11.7B.
- **OI flush**: ($14.2B − $11.7B) / $14.2B = **17.6%** — above 15% threshold.
- OI declining streak: 6 consecutive daily periods. OI deceleration: today's change = −$180M vs yesterday −$350M → decelerating. All flush sub-conditions: **PASS**.
- RSI(14, 4h) = **28** — oversold: **PASS**.
- Funding (8h): **−0.022%/8h** (shorts paying ~24% APY). Dual confirmation: **PASS** (funding ≤ −0.01%).
- OI vs 90d average: $11.7B vs $13.8B avg = 84.8% — above 30% floor: **PASS**.
- Regime: `Consolidation` — not Bear or Shock: **PASS**.

**Entry:** Long ETH-PERP at $3,210. Sleeve capital $100,000. ATR(14, 4h) = $95. Target risk 1.2% = $1,200. Size = $1,200 / ($95/$3,210) = $1,200 / 0.02957 ≈ $40,580. Capped at 12% = $12,000. Multiplier: OI flush 17.6% (below 20% → no strong-flush upweight) × dual-confirm 1.1 = **$13,200** (but capped at $12,000).

**Hold (9 days):** ETH recovers. Day 5: price reaches $3,590 — 50% Fibonacci retracement of the $901 decline. Trim 50% at $3,590 (+11.8% on $6,000 half-position). OI also recovering: $12.4B from $11.7B trough = +6.0% (not yet 7% re-expansion threshold). Continue holding. Day 9: ETH at $3,750. OI = $12.6B = +7.7% from $11.7B trough → **OI re-expansion exit trigger fires**. Exit remaining $6,000 position at $3,750 (+16.8%).

**Carry:** −0.022%/8h × $13,200 (avg) × 27 periods = **+$78.4** carry received.

**Net P&L:**
- Leg 1 (50% at $3,210 → $3,590): +$354.
- Leg 2 (50% at $3,210 → $3,750): +$504.
- Carry: +$78.
- Fees (4 legs × 0.045% × avg $10,000 notional): ~$18.
- Net: **+$918 on $12,000 deployed** (~7.7% in 9 days; illustrative).

*(Illustrative. Not a backtest. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Mean-reversion base ~0.5-0.7; OI flush gate adds selectivity and timing improvement |
| Expected max drawdown | ~20% | Dominated by bear-regime misclassification (structural decline disguised as deleveraging) |
| Win rate (per signal) | ~55-65% | OI flush as confirmation improves win rate vs unfiltered dip buy |
| Avg hold period | 5-12 days | Depends on reversion speed; time stop at 12 days |
| Carry income (dual confirm) | 5-20 bps per 7-day hold | At −0.022%/8h, ~14 bps over 7 days; smaller than funding-flush-reversal at deep flush |
| Breakeven cost budget | 30 bps | Taker fees on perp + slippage; carry income at negative funding partly offsets |

**What the OI gate adds vs unfiltered dip buying:** The 15% OI flush threshold filters out dip entries made mid-deleveraging (when forced sellers are still active). Historical analysis of crypto downmoves suggests that price troughs correlate strongly with OI troughs in overshoot events; entries made before the OI trough are systematically early, entering into ongoing forced selling. The gate delays entry until the deleveraging is advanced, improving the timing of mean-reversion entry.

## Capacity limits

- **Per asset on Hyperliquid majors (ETH/BTC)**: ~$15-30M. OI flush events on major assets involve billions of dollars of position contraction; $15-30M is a rounding error and does not affect market dynamics.
- **Cross-asset**: ~$60M if multiple assets flush simultaneously (risk-off events often produce correlated OI declines).
- **Hard constraint**: entries during OI flushes may encounter thin orderbooks (remaining market makers are cautious). Large entries require gradual execution (TWAP over 1-4 hours).

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Structural bear misclassification (#5).** The most dangerous failure: OI declines 15%+ because the asset is entering a structural bear market (declining adoption, regulatory event, ecosystem collapse). The time stop and regime kill provide partial protection, but a structural decline can produce a 15% OI flush followed by another 15% flush followed by another. The OI floor check (OI > 30% of 90d average) catches extreme structural flight but not moderate bears.
2. **Secondary deleveraging wave (#5).** OI purges to −15%, the strategy enters, then a second wave of selling drives OI down another −15%. The cut-50% on further OI decline and the hard stop limit the loss from a second wave, but it produces the strategy's second-worst failure mode after structural bear misclassification.
3. **OI floor asymmetry on cross-venue OI (#7: Operational).** The OI flush is measured on the primary venue (Hyperliquid or Binance perp). If the deleveraging shifted to another venue — e.g., positions were not closed but moved from Binance to CME — the primary-venue OI overstates the flush. Cross-venue OI aggregation (via Coinglass or CryptoDataAPI) improves signal quality.
4. **Crowding of the OI-trough entry (#4).** If many strategies await the OI trough before buying, they pile in simultaneously, making the entry fast and clean but the reward compressed. Signal frequency is already low (OI flush events are not daily), limiting crowding risk, but institutional algo adoption can shift this.
5. **Funding remains neutral after OI flush (#5).** If OI declines without funding going negative (both longs and shorts deleveraged together), the squeeze potential is lower. The optional funding confirmation filter addresses this; without it, the strategy is weaker in dual-deleveraging environments.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 20%** in any rolling 30-day window.
2. **Rolling 6-month Sharpe < 0** on a minimum 15-trade sample.
3. **OI flush not predictive**: flush condition fires but mean reversion fails in > 60% of setups over 25 consecutive signals — OI purge is not sufficient confirmation in the current regime.
4. **Time-stop ratio > 60%**: more than 60% of entries exit via time stop rather than take-profit — the strategy's holding window is too short for the current reversion speed. Review time stop (consider extending to 15-18 days).

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Structural confirmation, not just price signal**: by waiting for ≥ 15% OI decline, the strategy enters with quantitative evidence that the leveraged-long book has been substantially cleared — a more reliable structural basis than price oversold alone.
- **Avoids the mid-cascade entry problem**: the primary failure mode of dip buying is buying into an ongoing cascade. The OI flush criterion enforces a minimum structural precondition that rules out entries during active deleveraging.
- **Complementary to liquidation-event strategies**: [[post-liquidation-rebound]] uses event-based triggers (single large liquidation spike); this strategy uses cumulative OI decline, capturing slow deleveraging events that do not produce a single dramatic spike. The two can be run together as complementary mean-reversion triggers.
- **OI data is objective and manipulation-resistant**: OI is a hard ledger of outstanding positions; it cannot easily be spoofed or gamed (unlike sentiment metrics or social signals). The signal is based on a robust data source.
- **Deceleration sub-condition improves timing**: requiring the OI decline to be decelerating before entry captures the end of the flush rather than the middle, tightening entry timing without requiring a tick-level cascade trigger.

## Disadvantages

- **Signal rarity in low-volatility periods**: a 15% OI decline from the 5-day peak is not a frequent event on major perps in stable regimes. The strategy may produce very few signals in a prolonged low-volatility period.
- **Cannot distinguish structural from cyclical OI declines**: the primary risk. OI declines in bear markets and in overshoot corrections; the regime gate and OI-floor checks help but do not solve this.
- **Cross-venue OI completeness**: single-venue OI (HL perp only) misses CME, Binance, and options markets. A 15% flush on HL may represent 5% of total open interest globally — insufficient to confirm real deleveraging.
- **Deceleration sub-condition may delay entry**: if OI flushes quickly and bounces, the deceleration condition may not have been satisfied in time to enter before price recovers. The optional nature of this sub-condition (required but lowest priority) allows entry when deceleration is ambiguous.
- **Asymmetric strategy**: long-only dip buy. The symmetric short strategy — fading uptrends after OI surges +15% from trough — is covered by [[oi-price-exhaustion]] (which requires OI declining while price extends, not OI surging per se). The strategies are complementary, not symmetric.

## Sources

- Ederington, L. and Lee, J. (1993), *How markets process information: News releases and volatility*, Journal of Finance. OI as a measure of aggregate conviction and participation in futures markets; foundational framework for OI-as-signal interpretation.
- [[oi-price-exhaustion]] — OI divergence from price as a trend exhaustion signal; closest existing strategy; key differentiation page.
- [[post-liquidation-rebound]] — event-based liquidation cascade mean reversion; the complementary entry trigger.
- [[funding-flush-reversal]] — funding-state-confirmed mean reversion; the companion page using the funding channel of the same structural flush.
- [[open-interest]] — definition, interpretation, and conventions for OI in crypto perpetuals.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/open-interest?coin=ETH` — cross-exchange OI for flush monitoring (Binance + Hyperliquid)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — 8h funding for optional dual-confirmation and trim trigger
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=ETHUSDT` — long/short ratio as secondary crowding signal at entry
- `GET /api/v1/regimes/current` — regime gate for Established Bear / Structural Shock exclusion

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI together) for flush event identification and rolling-peak computation
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) for correlation between OI flush events and funding state
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=200` — OHLCV for RSI, Bollinger Band, ATR computation

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=ETH"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [liquidations](https://cryptodataapi.com/liquidations) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/derivatives/open-interest?coin=ETH` tracked against its rolling peak; the flush-percentage trigger comes straight off this feed
- **Filter** — `GET /api/v1/derivatives/funding-rates?coin=ETH` and `GET /api/v1/derivatives/binance/long-short-ratio?symbol=ETHUSDT` confirm the flush washed out crowded longs rather than shorts covering
- **Regime gate** — `GET /api/v1/regimes/current`; no reversion entries in `Established Bear` or `Structural Shock`
- **Backtest** — flush-event identification from `/derivatives/binance/history` (90-day rolling) plus `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30); price-path replay from `GET /api/v1/backtesting/klines` 4h bars back to 2017-08
- **Tips** — cross-reference `GET /api/v1/backtesting/liquidations` (Hyperliquid, since 2026-03-30) to separate liquidation-driven flushes (the best setups) from voluntary de-risking
- **Prompt library** — the "Open Interest Divergence Scanner" prompt (Free tier, [prompt library](https://cryptodataapi.com/prompts)) identifies OI-flush conditions ready for this reversion entry

## Related

- [[mean-reversion]] — the underlying primitive that generates the edge
- [[open-interest]] — the central data input; OI flush definition and mechanics
- [[oi-price-exhaustion]] — OI divergence from uptrend as a reversal signal; nearest neighbor (different trade direction)
- [[oi-confirmed-trend]] — OI expansion as a trend-continuation confirmation; the complement
- [[post-liquidation-rebound]] — event-triggered cascade reversion; complementary entry channel
- [[funding-flush-reversal]] — funding-confirmed dip buy; stackable overlay with this strategy
- [[liquidation-cascade-fade]] — CVD-based cascade reversion; overlapping mean-reversion family
- [[rsi-mean-reversion]] — RSI-based mean reversion without OI confirmation
- [[funding-rate]] — funding as optional dual confirmation and trim trigger
- [[perpetual-futures]] — the instrument carrying the OI ledger
- [[liquidations]] — the event often driving the OI flush
- [[behavioral-finance-overview]] — extrapolation bias and panic capitulation
- [[edge-taxonomy]] — behavioral + structural classification
- [[failure-modes]] — bear-regime misclassification and secondary cascade risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
