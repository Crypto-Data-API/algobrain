---
title: "Funding Flush Reversal"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, mean-reversion, funding-rate, perpetual-futures, behavioral-finance, quantitative, crypto]
aliases: ["Funding-Confirmed Dip Buy", "Post-Flush Funding Reversion", "Deleveraging-Confirmed Mean Reversion"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "Retail longs are forced out (funding flushes negative) precisely when sentiment and leverage are most extended against them; the strategy enters a mean-reversion long only after this capitulation has been confirmed by a sustained negative funding shift, buying the dip when shorts are now the crowded side paying carry, not longs — the structural setup has flipped in the buyer's favour."

data_required: [ohlcv-4h, ohlcv-daily, funding-rates, open-interest, mark-price]
min_capital_usd: 5000
capacity_usd: 75000000
crowding_risk: medium

expected_sharpe: 0.95
expected_max_drawdown: 0.22
breakeven_cost_bps: 30

decay_evidence: "No published study specific to funding-flush-confirmed crypto mean reversion. The structural rationale — that post-capitulation, crowded-short funding is a carry tailwind for new longs — is an application of the BIS funding-as-crowding-signal framework (Schmeling, Schrimpf, Todorov 2023). The mean-reversion edge in crypto dips has been documented in post-liquidation studies (Liquidation Cascade Fade wiki page) but the funding-state confirmation layer is novel and untested."

kill_criteria: |
  - strategy drawdown > 22% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 15-trade sample
  - funding flush criterion is satisfied but mean reversion fails to materialize within the time window in > 60% of setups over 30 signals (the flush is not a sufficient condition for dip quality in the current regime)
  - negative funding persists for > 21 days without reversion (structural bear trend, not a temporary flush)

related: ["[[mean-reversion]]", "[[funding-rate-arbitrage]]", "[[crowded-short-funding-fade]]", "[[crowded-long-funding-fade]]", "[[post-liquidation-rebound]]", "[[funding-filtered-momentum]]", "[[rsi-mean-reversion]]", "[[bollinger-band-reversion]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[liquidations]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Funding Flush Reversal

Funding flush reversal is a [[mean-reversion]] strategy that buys crypto dips on spot or perpetuals only after funding has flushed deeply negative — confirming that the preceding downmove has forced out the leveraged long side and that shorts are now the crowded party paying carry. The primitive edge is mean reversion of oversold assets; the overlay is a funding-state confirmation that the deleveraging is complete: the crowd has flipped from paying-to-be-long to paying-to-be-short, and a new long entry now has the structural funding advantage.

This is differentiated from [[post-liquidation-rebound]] — that strategy requires a specific liquidation cascade event (5× spike in liquidation volume within minutes) as its trigger. This page does not require a spike event; it requires a *sustained* funding flush (funding negative for a minimum consecutive period), which may arise from gradual deleveraging, OTC selling, or a series of smaller liquidations rather than a single cascade. The funding state is the trigger, not the liquidation volume.

This is differentiated from [[crowded-short-funding-fade]] — that strategy fades the momentum of a *short-crowded* market (entering long because shorts are squeezable). This page is a mean-reversion entry after a downmove, where the funding flush merely confirms the capitulation precondition; the primary driver is the price dip and the expectation of reversion, not a squeeze thesis.

## Edge source

Per [[edge-taxonomy]], this is a **behavioral + structural** hybrid:

- **Behavioral (primary)** — the transition to deeply negative funding is the market's behavioral signature of capitulation: leveraged longs, who funded their bullish bias via perps, have been forced out (or voluntarily stopped out) at a loss. The survivors of the downmove are better-capitalised. The new marginal short-opener at negative funding is a fear/momentum-chasing participant, not a fundamentally motivated one — they are shorting into weakness, paying elevated negative funding as the cost of their bearish conviction. History shows these crowded shorts tend to cover into any bounce, accelerating the rebound.
- **Structural (secondary)** — when funding is negative (e.g., −0.03%/8h = −33% APY), longs *receive* carry and shorts *pay* carry. A new long entry at negative funding does not just capture mean reversion — it collects a structural funding income every 8 hours while waiting for the reversion. The carry income is the strategy's "paid to wait" benefit: it improves the risk-adjusted break-even versus an unfunded dip buy.

## Why this edge exists

Three mechanisms create an additive edge beyond unconfirmed dip buying:

1. **Post-flush clean market structure.** After a significant funding flush, the leveraged long book has been partially or fully liquidated. The surviving longs have larger margin buffers; the remaining book is structurally healthier. This reduces the probability of a secondary cascade and improves the odds that the next meaningful move is upward.

2. **Crowded short creates squeeze potential.** When shorts have piled in to push funding negative, they become the squeeze risk. Any positive catalyst — or simply the passage of time as carry costs accumulate — can trigger short covering that accelerates the mean reversion. The strategy does not need to predict the catalyst; it needs only to be positioned before the covering begins.

3. **Carry income reduces the required move.** A mean-reversion dip buy at −0.03%/8h funding receives ~33% APY in carry. Over a 7-day hold, that is ~0.63% in carry income. If the break-even on the trade (cost of capital + fees) requires a 0.5% upward move, the carry alone covers it. The hurdle for the mean reversion is lower when funding is paying the long side.

**Who is on the other side:** the momentum-following shorter who enters at the bottom of the funding flush, paying −0.03%/8h or worse for the privilege of being short at a market extreme; and the retail participant who sells spot into the flush on fear rather than fundamental deterioration.

## Null hypothesis

Under the null, the funding state at a dip-buy entry carries zero information about forward mean reversion speed or magnitude. Specifically:
- Average 7-day forward returns on oversold dip entries should be equal regardless of whether funding was positive, neutral, or negative at entry.
- The win rate and Sharpe of dip entries filtered to negative-funding setups should be statistically indistinguishable from unfiltered dip entries on the same assets and periods.

The null is currently not rejected in this wiki (`backtest_status: untested`). Testable prediction: sort historical oversold dip entries by funding quintile at entry; the most-negative funding quintile should show materially better forward Sharpe, lower time-to-reversion, and higher carry-adjusted returns than the flat or positive funding quintiles.

## Rules

### Funding flush definition

The **funding flush** condition is met when ALL of the following hold:
1. **Current 8h funding rate ≤ −0.02%/8h** (−22% APY annualised) on the primary perp venue. This is the minimum threshold confirming shorts are paying materially.
2. **Funding has been negative (≤ 0) for at least 3 consecutive 8h periods** (24h). A single negative print may be noise; 24h of persistent negative funding indicates a genuine crowd-short regime.
3. **Funding z-score** (8h funding normalized over its trailing 30-day distribution) is ≤ −1.5 — funding is in the lower quartile of its own recent history, confirming this is unusually negative relative to the recent regime.

### Entry conditions (long, spot or perp)

1. **Funding flush active** (all three sub-conditions above).
2. **Price oversold.** At least ONE of:
   - RSI(14, 4h) ≤ 30 — price is in the oversold zone.
   - Price is ≥ 2 ATR(14, 4h) below the 20-period EMA on the 4h chart.
   - Price has retraced ≥ 15% from its 20-day high.
3. **OI has not collapsed to zero.** Open interest is still > 50% of its 30-day average — the market has not emptied out entirely. A completely empty OI suggests a structural issue, not a sentiment flush.
4. **No confirmed structural event.** No protocol exploit, de-peg, or credit event that could explain a permanent repricing. The flush is a sentiment/leverage event, not a fundamental one.
5. **No regime kill active.** The market-wide regime from `/api/v1/regimes/current` is not `Established Bear` (persistent, structure-confirmed downtrend with declining OI and negative funding as the new normal, not a temporary flush).

### Exit conditions

1. **Funding normalises above 0.** When funding returns to ≥ 0 (crowded shorts have covered, the carry advantage is gone), begin trimming.
2. **Price reaches 50% retracement of the flushed move.** Take half off at the 50% Fibonacci retracement of the decline from 20-day high to the flush low.
3. **Price returns to 20-period EMA on 4h.** The mean-reversion target; close the remainder.
4. **Time stop: 10 days.** If reversion has not occurred to at least 25% of the flushed move within 10 calendar days, close at market — the market is in a structural bear, not a temporary flush.
5. **Funding worsens to ≤ −0.07%/8h** after entry and continues for 3+ periods — the flush is deepening, not reversing; a secondary capitulation wave may be in progress. Cut position by 50%, hold remainder for recovery.

### Position sizing

- Base position = (target risk bps × sleeve capital) / (ATR(14, 4h) × contract face). Target 1.5% sleeve risk per trade.
- **Funding upweight**: when funding is ≤ −0.04%/8h (≤ −44% APY) AND price is oversold AND OI is contracting, apply a 1.2× size multiplier — a deeper flush is a stronger signal.
- Maximum single position: 15% of sleeve (larger than momentum because the hedge is in the structural carry, not in a separate instrument).
- Maximum 2 concurrent flush-reversal positions across different assets.

## Implementation pseudocode

```python
# funding_flush_reversal.py — decision loop
from dataclasses import dataclass

# ---- thresholds ----
FLUSH_RATE_MIN       = -0.0002   # -0.02%/8h: minimum negative funding for flush
FLUSH_CONSEC_PERIODS = 3         # 24h of continuous negative funding required
FLUSH_Z_MAX          = -1.5      # funding z-score threshold (unusually negative)
RSI_OVERSOLD         = 30
EMA_PERIOD           = 20
ATR_MULTIPLIER       = 2.0       # price must be >= 2 ATR below EMA for oversold alt check
RETRACE_PCT          = 0.15      # 15% from 20d high for third oversold signal
OI_MIN_RATIO         = 0.50      # OI >= 50% of 30d average
EXIT_FUNDING_NEUTRAL = 0.0       # funding back at 0 → start trimming
EXIT_EMA_TARGET      = True      # price back at EMA → close remainder
TIME_STOP_DAYS       = 10
DEEPEN_RATE          = -0.0007   # -0.07%/8h deepening flush → cut 50%
TARGET_RISK_PCT      = 0.015     # 1.5% of sleeve per trade
UPWEIGHT_FACTOR      = 1.2
MAX_POS_PCT          = 0.15
MAX_CONCURRENT       = 2
DRAWDOWN_KILL        = 0.22

@dataclass
class Signal:
    asset: str
    funding_8h: float
    funding_z_30d: float
    funding_negative_streak: int  # consecutive 8h periods with funding <= 0
    rsi_14_4h: float
    price: float
    ema20_4h: float
    atr14_4h: float
    price_high_20d: float
    oi_current: float
    oi_avg_30d: float
    regime: str
    days_since_entry: int         # 0 if not in position

def flush_active(s: Signal) -> bool:
    return (s.funding_8h <= FLUSH_RATE_MIN
            and s.funding_negative_streak >= FLUSH_CONSEC_PERIODS
            and s.funding_z_30d <= FLUSH_Z_MAX)

def oversold(s: Signal) -> bool:
    ema_dist = (s.ema20_4h - s.price) / s.atr14_4h
    retrace = (s.price_high_20d - s.price) / s.price_high_20d
    return (s.rsi_14_4h <= RSI_OVERSOLD
            or ema_dist >= ATR_MULTIPLIER
            or retrace >= RETRACE_PCT)

def decide(s: Signal, book: dict) -> dict:
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    pos = book["positions"].get(s.asset)

    if pos is not None:
        # --- deepening flush: cut half ---
        if s.funding_8h <= DEEPEN_RATE:
            return {"action": "TRIM_50PCT", "asset": s.asset,
                    "reason": "flush deepening: funding too negative"}
        # --- exits ---
        if s.funding_8h >= EXIT_FUNDING_NEUTRAL:
            return {"action": "TRIM_50PCT", "asset": s.asset,
                    "reason": "funding normalized: take half off"}
        if s.price >= s.ema20_4h:
            return {"action": "EXIT", "asset": s.asset,
                    "reason": "price at EMA20 mean reversion target"}
        if s.days_since_entry >= TIME_STOP_DAYS:
            return {"action": "EXIT", "asset": s.asset, "reason": "time stop"}
        return {"action": "HOLD", "asset": s.asset}

    # --- entries ---
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}
    if s.regime == "Established Bear":
        return {"action": "WAIT", "reason": "regime kill: established bear"}
    if s.oi_current < OI_MIN_RATIO * s.oi_avg_30d:
        return {"action": "WAIT", "reason": "OI too depleted"}

    if flush_active(s) and oversold(s):
        multiplier = UPWEIGHT_FACTOR if s.funding_8h <= -0.0004 else 1.0
        notional = min(
            TARGET_RISK_PCT * book["sleeve_capital"] / (s.atr14_4h / s.price),
            MAX_POS_PCT * book["sleeve_capital"]
        ) * multiplier
        return {
            "action": "LONG",
            "asset": s.asset,
            "notional": notional,
            "reason": (f"flush confirmed: funding {s.funding_8h*100:.4f}%/8h "
                       f"(z={s.funding_z_30d:.1f}), RSI={s.rsi_14_4h:.1f}")
        }

    return {"action": "WAIT", "reason": "flush or oversold condition not met"}
```

The production system adds: regime check via `/api/v1/regimes/current` before each signal evaluation; real-time funding z-score computation against rolling 30-day history; and a manual kill switch for confirmed structural events (exploits, de-pegs).

## Indicators / data used

- **[[funding-rate]] (8h)** — primary flush signal. Both the absolute level and the z-score relative to 30-day history.
- **Funding consecutive-period counter** — number of continuous 8h periods with funding ≤ 0. Distinguishes genuine sustained flush from single-period noise.
- **RSI(14, 4h)** — oversold confirmation. ≤ 30 triggers the price-side entry condition.
- **EMA(20, 4h)** — mean-reversion target; also used for the "price below EMA by 2 ATR" oversold check.
- **ATR(14, 4h)** — position sizing denominator and oversold-distance check.
- **[[open-interest]] ratio** — OI vs 30-day average; ensures market is not structurally evacuated.
- **Regime classification** — `/api/v1/regimes/current` to block entries in confirmed bear regimes.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Asset: BTC-PERP on Hyperliquid.
- BTC has fallen 18% over 6 days from $105,000 to $86,100.
- 8h funding: **−0.031%/8h** (−34% APY). Funding has been negative for **9 consecutive 8h periods** (3 days). Funding z-score vs 30-day history: **−2.1**. All three flush conditions: **PASS**.
- RSI(14, 4h) = **27** (oversold). Oversold condition: **PASS**.
- OI current: $8.1B vs 30-day average $9.4B = 86% — above 50% threshold: **PASS**.
- Regime: `Post-Crash Recovery` — not `Established Bear`: **PASS**.
- Sleeve capital: $50,000. ATR(14, 4h) = $2,200. Target risk = 1.5% = $750. Size = 750 / (2,200/86,100) = 750/0.0256 ≈ $29,300 notional. Max cap 15% of $50,000 = $7,500. Final: $7,500 notional (cap applied). Funding ≤ −0.03%: 1.2× multiplier → $9,000 (but hard-capped at $7,500).

**Entry:** Long BTC-PERP at $86,100, $7,500 notional. Carry received: 0.031%/8h × $7,500 ≈ $2.33/8h = **$7.00/day carry income**.

**Hold (7 days):** BTC rallies to $96,400 (+12%). Funding normalises to +0.003%/8h on day 5 — trim trigger fires; sell 50% at $93,800 (day 5). Remainder exits at EMA20 target $96,400 (day 7). Carry accrued: ~7 × $7.00 = $49.

**Net P&L (rough):**
- Leg 1 (50%): entry $3,750 at $86,100 → exit at $93,800 (+8.9%) ≈ +$334.
- Leg 2 (50%): entry $3,750 at $86,100 → exit at $96,400 (+12.0%) ≈ +$450.
- Carry income: +$49. Fees: ~$13.50. Net: **+$820 on $7,500 deployed** (~10.9% in 7 days; illustrative exceptional result). Contrast with unfunded dip buy: same P&L but carry income of $49 is absent, and the trade might have been avoided during the flush period (which is the primary edge benefit — waiting for funding confirmation).

*(Illustrative round-trip. Not a backtest. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.95 | Mean reversion base ~0.5-0.7 unfiltered; flush filter adds ~0.2-0.3 selectivity and carry |
| Expected max drawdown | ~22% | Driven by structural-bear misclassification events (LUNA/FTX class) |
| Win rate (per signal) | ~55-65% | Oversold dip buys in crypto: above-50% win rate in non-bear regimes |
| Avg win / avg loss | ~2.0-2.5× | Mean reversion: moderate win size, sharp stop-out losses on bear regime misclassification |
| Breakeven cost budget | 30 bps round-trip | Taker fees on perp + slippage; carry income partially offsets |
| Carry income per 7-day hold | 5-25 bps | Depends on funding level; at −0.03%/8h, ~15 bps over 7 days |

**What the filter buys (rough estimate):** By requiring 24h of sustained negative funding before entry, the strategy avoids buying dips that are mid-cascade (funding still falling). Historical dip-buy performance is significantly better when the flush has stabilised vs when the decline is still in progress. The carry income at negative funding is a bonus, but the primary value is the wait-for-capitulation-confirmation discipline.

## Capacity limits

- **Per-asset on Hyperliquid majors (BTC/ETH)**: ~$20-40M notional per event — the mean-reversion entry window is not a single tick; capacity is large for a mean-reversion strategy.
- **Cross-asset**: ~$75M combined if 2-3 assets flush simultaneously.
- **Hard constraint**: at scale, entry orders must shift to maker fills to avoid self-reinforcing the rebound. This reduces the "cleanness" of entry but is manageable.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Structural bear misclassification (#5).** The most dangerous failure: funding is deeply negative because the asset is permanently repricing lower (protocol collapse, ecosystem exit, credit event). The time stop and the OI check limit losses, but cannot fully prevent entering into an asset that is going to zero. The regime kill (`Established Bear`) provides a first-order guard.
2. **Extended flush duration (#5).** In severe bear markets, funding can remain deeply negative for weeks, not days. The time stop exits the trade at a loss before the eventual reversion. This is the correct behavior (limit exposure to prolonged negative funding), but it produces a run of time-stop losses that accumulates into drawdown.
3. **Secondary cascade during hold (#6).** A second liquidation wave arrives after the first flush — the entry was too early. The "funding deepening exit" (cut 50% at −0.07%/8h) provides partial protection; the overall stop limits total loss.
4. **Crowding of the flush signal (#4).** If many traders await a funding flush before buying, they pile in simultaneously, making the rebound faster but creating a crowded long immediately after entry. The strategy's edge is compressed as the crowd enters at the same signal.
5. **Funding data staleness (#7: Operational).** 8h funding is known only at settlement; between settlements, the predicted funding (from `/api/v1/derivatives/funding-rates`) may differ from the final settled rate. Use predicted funding for the consecutive-period check when available.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 22%** in any rolling 30-day window.
2. **Rolling 6-month Sharpe < 0** on a minimum 15-trade sample.
3. **Flush criterion not predictive**: the funding flush condition fires but mean reversion fails to materialise in > 60% of setups over 30 consecutive signals — the flush is not sufficient confirmation in the current regime.
4. **Structural bear**: negative funding persists for > 21 consecutive days with OI continuing to decline and no mean-reversion bounce — this is a bear trend, not a temporary flush.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Waits for capitulation confirmation**: by requiring 24h of sustained negative funding before entry, the strategy avoids the single worst failure mode of dip-buying — buying a cascade mid-fall.
- **Structural carry income**: the long entry at negative funding receives carry, lowering the minimum required price move to break even and extending the patience window.
- **Inverts squeeze asymmetry**: entering when shorts are the crowded party means a short-squeeze tailwind accelerates any recovery, rather than a long-liquidation cascade punishing the position.
- **Simple additional data point**: requires only the funding rate and its recent history — no exotic indicators or ML models.
- **Complementary to momentum strategies**: mean-reversion entries at funding flushes are uncorrelated with momentum entries at non-crowded breakouts (funding-filtered-momentum fires at flat/neutral funding; this fires at deeply negative funding). The two can coexist in the same book.

## Disadvantages

- **Signal is rare in mild markets**: genuine funding flushes (funding ≤ −0.02%/8h for 24h) are not daily occurrences on major perps; in low-volatility periods the strategy may produce very few signals.
- **Cannot distinguish flush from structural repricing**: the most dangerous failure mode — funding deeply negative because the asset is going lower permanently — is not distinguishable from funding deeply negative because of a temporary deleveraging. The regime check and OI gate help but do not solve this.
- **Bear-regime exposure is the dominant risk**: if the bear-regime kill is miscalibrated or the regime flip is slow to register, the strategy enters into a structural decline. Drawdown from a single such misclassification can trigger the kill criteria.
- **Asymmetric signal**: the strategy is long-only (buying dips confirmed by negative funding). A symmetric short strategy would require positive funding confirmed by overbought conditions — that is closer to [[crowded-long-funding-fade]], which is already covered separately.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (BIS, 2023). Funding as a crowding signal: leveraged retail drives extreme funding on both sides. https://www.bis.org/publ/work1087.pdf
- [[post-liquidation-rebound]] — the closely related liquidation-cascade mean reversion strategy; the primary differentiation page.
- [[crowded-short-funding-fade]] — fades directional short crowding; the most similar existing strategy; key differentiation: this page is a dip-buy, not a fade.
- [[liquidation-cascade-fade]] — the tightest CVD-based post-cascade entry; shares mean-reversion rationale.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange 8h funding (Binance + Hyperliquid); required for flush condition monitoring
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI for the OI-ratio gate and the deleveraging confirmation
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — long/short ratio as a secondary crowding signal post-flush
- `GET /api/v1/regimes/current` — market regime for regime kill

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for z-score computation and backtest signal reconstruction
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI together) for multi-period analysis
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) to identify all historical flush events
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — OHLCV for RSI, EMA, ATR computation

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

## Related

- [[mean-reversion]] — the underlying primitive that generates the edge
- [[funding-rate]] — the contract mechanism and funding sign conventions
- [[post-liquidation-rebound]] — nearest neighbor: cascade-triggered vs flush-state-triggered mean reversion
- [[crowded-short-funding-fade]] — fades directional short crowding (same funding-state logic, different trade type)
- [[crowded-long-funding-fade]] — fades directional long crowding (the mirror image of this strategy)
- [[funding-filtered-momentum]] — gates directional momentum on flat funding; shares the funding-state overlay
- [[rsi-mean-reversion]] — RSI-based mean reversion without funding confirmation
- [[bollinger-band-reversion]] — band-based mean reversion; complementary oversold signal
- [[perpetual-futures]] — the instrument carrying the funding mechanism
- [[liquidations]] — the event often preceding the funding flush
- [[behavioral-finance-overview]] — recency bias and fear-driven capitulation
- [[edge-taxonomy]] — behavioral + structural classification
- [[failure-modes]] — bear-regime misclassification and cascade extension risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
