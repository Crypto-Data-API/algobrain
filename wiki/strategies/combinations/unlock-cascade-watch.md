---
title: "Unlock Cascade Watch"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, event-driven, liquidations, open-interest, funding-rate, on-chain, perpetual-futures, risk-management, quantitative, crypto, altcoins]
aliases: ["Unlock Liquidation Window", "Unlock-Triggered Cascade Setup", "Unlock OI Watch", "Unlock Cascade Risk Framework"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [structural, informational, behavioral]
edge_mechanism: "Large scheduled token unlocks concentrate stop-loss and liquidation clusters in the perp market as participants position for the supply event; the overlap of the unlock supply shock with elevated OI and funding creates a predictable high-risk window during which normal trading strategies carry abnormally high cascade risk — the strategy reduces exposure into the window, pre-stages cascade-fade limit orders below current price, and monitors OI/funding for the structural conditions that confirm a cascade is likely to materialise."

data_required: [token-unlock-calendar, funding-rates, open-interest, ohlcv-daily, ohlcv-4h, long-short-ratio, liquidations]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: low

expected_sharpe: 0.8
expected_max_drawdown: 0.22
breakeven_cost_bps: 35

decay_evidence: "Token unlock monitoring and the unlock-short trade are well-documented since 2022. The specific framework of monitoring the LIQUIDATION STRUCTURE (OI, funding, stop-cluster buildup) around unlock windows — rather than directly shorting the token — has not been systematically published. The [[unlock-short-with-crowding-gate]] and [[unlock-pair-hedge]] pages cover the directional-short and beta-hedged-short approaches; this page covers the cascade-risk framing (reduce exposure, stage fade orders, use the window as a risk trigger rather than a trade trigger)."

kill_criteria: |
  - strategy drawdown > 22% from high-water mark
  - 6 consecutive unlock windows where OI/funding exceeded thresholds but no price cascade materialised within 10 days (the structural conditions are present but cascades are not occurring — market structure has changed, or unlocks are being absorbed differently)
  - rolling 8-signal P&L negative on cascade-fade executions
  - token unlock data source becomes unreliable or delayed (calendar data integrity compromised)

related: ["[[unlock-short-with-crowding-gate]]", "[[unlock-aware-momentum]]", "[[unlock-pair-hedge]]", "[[liquidation-cascade-fade]]", "[[off-hours-liquidation-playbook]]", "[[leverage-stress-tail-hedge]]", "[[event-vol-buying]]", "[[oi-aware-grid]]", "[[cascade-monetization-rotation]]", "[[funding-rate]]", "[[open-interest]]", "[[liquidations]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Unlock Cascade Watch

Unlock cascade watch is a combination strategy that **monitors the liquidation and leverage structure of a token's perp market around large scheduled unlock events**, reducing exposure into the risk window and pre-staging cascade-fade limit orders for the potential price cascade that the combined supply shock and leverage unwind can produce. Unlike [[unlock-short-with-crowding-gate]] (which takes an outright directional short into the unlock) or [[unlock-pair-hedge]] (which beta-hedges the short), this page takes a primarily **risk-management and opportunistic-fade** stance: it identifies the unlock window as a period of elevated cascade risk, reduces any existing long exposure, monitors the OI and funding structure for confirmation that a cascade is building, and places pre-staged limit orders to fade any cascade that does occur.

**This is explicitly differentiated from [[unlock-short-with-crowding-gate]]** — that page enters a directional short into a token cliff unlock, gated on the crowding condition that the short is not already consensus. The primary trade is a DIRECTIONAL SHORT on the unlocking token. This page does NOT take a primary directional short into the unlock. Its primary action is DE-RISKING existing longs and monitoring for a cascade. The cascade-fade orders (limit buys below current price) are secondary opportunistic trades, not the primary position. The framing is different: that page is an active trade on the unlock event; this page is a risk-management protocol for the unlock event window with an opportunistic fade component.

**This is differentiated from [[unlock-aware-momentum]]** — that page applies an unlock calendar awareness to a MOMENTUM book: pause momentum longs ahead of unlocks, re-enter after supply has been absorbed. The primitive is momentum; the unlock is a risk gate that pauses momentum entries. This page is agnostic to momentum — it applies to ANY existing long position (or can be run standalone for the cascade-fade component). Additionally, this page focuses specifically on the LIQUIDATION STRUCTURE angle (OI, funding, stop-cluster risk), which [[unlock-aware-momentum]] does not address.

**This is differentiated from [[unlock-pair-hedge]]** — that page constructs a beta-neutral long-short pair around the unlock (short the unlocking token, long a sector peer at 1/beta ratio). The defining feature is the PAIR structure that isolates the idiosyncratic supply shock from sector beta. This page does not construct a pair; it manages the risk exposure of a single position or book around the unlock window.

**This is differentiated from [[liquidation-cascade-fade]]** — that page fades general liquidation cascades (not unlock-specific) when confirmed liquidation volume thresholds are breached. It is NOT event-calendar aware. This page is specifically calendar-anchored: the unlock date is the organizing event, and the monitoring of OI/funding/liquidation structure is done in the specific context of an approaching unlock. The setup criteria (unlock date proximity + leverage structure) are different from the pure cascade-fade trigger (real-time liquidation volume spike).

## Edge source

Per [[edge-taxonomy]], **structural + informational + behavioral**:

- **Structural (primary)** — large cliff unlocks create a predictable forced-supply event: early investors, team members, and protocol treasuries receive liquid tokens and frequently sell some portion. This creates a structural headwind to price. When this forced supply arrives simultaneously with a leveraged long book (positive funding, high OI), the supply shock can trigger margin calls and stop-losses in the perp market, creating a cascade that amplifies the initial price move. The structural predictability (the unlock date is known weeks to months in advance) allows pre-positioning.
- **Informational** — the unlock calendar is public information (tokenunlocks.app, Coinglass, on-chain vesting contracts). The edge is not in knowing the event exists (everyone can see it) but in systematically monitoring the leverage structure that determines whether the unlock will produce a routine sell-off or a cascade-amplified dislocation. The OI/funding monitoring provides information about cascade probability that price action alone does not surface.
- **Behavioral** — leveraged longs accumulate around unlock events for two reasons: (1) some traders bet on the "buy the rumour, sell the news" dynamic and accumulate before the unlock hoping to exit into initial strength; (2) momentum followers who entered the token on a positive narrative continue to hold through the unlock because they are not monitoring the supply calendar. Both groups create the over-leveraged long book that becomes cascade fuel. Their behavioral persistence (not de-risking ahead of the unlock) creates the structural vulnerability.

## Why this edge exists

**The leverage amplification of unlock supply shocks:**

A token cliff unlock of 3% of circulating supply would, in isolation, produce a 2–4% price decline as sellers work through the supply over days to weeks. But when the token has:
- OI in the 80th percentile of its trailing 30-day range (leveraged longs maximally committed)
- 7-day avg 8h funding ≥ +0.040%/8h (longs paying significant carry to stay exposed)
- 60–70% of recent OI at prices within 8% of the unlock date spot price (stop/liquidation clusters concentrated in a tight band)

...then the unlock sell pressure hits a market where even a 5–8% price decline can trigger a cascade of forced long liquidations. The unlock is the "first domino"; the leverage structure determines how far the cascade travels. A 3% supply shock becomes a 15–25% price correction when the liquidation cascade amplifies it.

**The monitoring advantage:** by tracking the OI percentile and funding trend in the 2–4 weeks before the unlock (the "buildup window"), the strategy can assess whether the token is approaching the unlock with a dangerous leverage structure or a clean one. A token approaching its unlock with OI at the 85th percentile and funding at +0.045%/8h is a high-risk window; a token approaching with OI at the 40th percentile and flat funding is a low-risk unlock (the supply shock will be absorbed without a cascade).

**Who is on the other side of the cascade-fade:** the leveraged longs who are forced to close their positions via margin calls or stop-losses during the cascade. These are mechanically-driven non-economic sellers; they are not selling because they have new information about the token's value — they are selling because their margin was exhausted. Buying from forced sellers at the trough of the cascade is the classic liquidation-cascade-fade edge.

## Null hypothesis

Under the null, the unlock event calendar + leverage structure monitoring adds **no predictive value** for subsequent price behavior compared to monitoring OI/funding alone without the unlock calendar:
- Token windows with (large unlock approaching) + (elevated OI/funding) should not produce more severe price drawdowns than windows with (elevated OI/funding alone, no imminent unlock).
- Cascade-fade limit orders staged below price in the unlock window should not produce higher fill rates or better post-fill returns than cascade-fade orders staged in non-unlock high-OI/funding windows.

Currently not rejected (`backtest_status: untested`). Testable predictions:
- (a) Identify all BTC-top-50 token cliff unlocks (≥ 3% circulating supply) from 2022–2025. Classify each by OI percentile at unlock date (high ≥ 75th vs low ≤ 40th). Compare maximum 10-day drawdown post-unlock. Predict: high-OI unlocks produce 2–3× larger drawdowns than low-OI unlocks.
- (b) Compare cascade-fade limit order fill rates in the 7 days around unlock dates vs the 7 days before/after the unlock window. Predict: fill rates are 30–50% higher in the 7-day unlock window.

## Rules

### Phase 1: Unlock window identification (2–4 weeks before unlock)

**Unlock event eligibility:**
- Scheduled cliff unlock of **≥ 3% of circulating supply** within the next **10–28 days**.
- Data source: public token unlock calendar (tokenunlocks.app, Coinglass). Cross-reference with on-chain vesting contract schedules where available.

**Leverage structure check at window entry (T − 14 to T − 7):**
- Compute OI percentile relative to trailing 30-day range: `GET /api/v1/derivatives/open-interest?coin={TOKEN}`.
- Compute 7-day average 8h funding: `GET /api/v1/derivatives/funding-rates?coin={TOKEN}`.
- Compute long/short ratio: `GET /api/v1/derivatives/binance/long-short-ratio`.

**Risk window classification:**
- **HIGH risk:** OI ≥ 75th percentile AND 7d avg funding ≥ +0.030%/8h.
- **MODERATE risk:** OI 50th–75th percentile OR funding +0.015–0.030%/8h.
- **LOW risk:** OI ≤ 50th percentile AND funding ≤ +0.015%/8h (unlock will likely absorb without cascade).

### Phase 2: Risk reduction (T − 7 to T − 2)

**HIGH risk window — de-risk existing longs:**
- Reduce any existing long position in the token to **25% of normal size** by T − 7.
- Pause new long entries in the token until cascade-fade or window-clear conditions are met.
- If running [[unlock-aware-momentum]]: momentum book pause is already enforced; this page's action is redundant and lower priority.

**MODERATE risk window:**
- Reduce existing longs to **50% of normal size** by T − 5.

**LOW risk window:**
- No de-risking action. Continue monitoring. Standard [[unlock-aware-momentum]] rules apply.

### Phase 3: Cascade-fade order staging (T − 3 to T + 3)

**Trigger for cascade-fade order placement (all conditions must be met):**
- OI remains ≥ 70th percentile at T − 1 (leverage has not naturally deflated pre-unlock).
- 8h funding ≥ +0.025%/8h at T − 1 (longs still paying carry into the unlock).
- Token price has not already declined ≥ 8% in the 5 days before the unlock (the cascade may have already occurred).

**Cascade-fade order structure:**
- Place **GTC limit buy orders** at the following levels below the T − 1 close price:
  - **Tranche 1 (30% of target position):** −8% from T − 1 close.
  - **Tranche 2 (40% of target position):** −14% from T − 1 close.
  - **Tranche 3 (30% of target position):** −20% from T − 1 close.
- Total target position: 3–5% of portfolio notional for HIGH risk windows; 2–3% for MODERATE.
- Orders expire if not filled within **10 days post-unlock** (cancel and reassess).

**Cascade confirmation gate (real-time monitoring at unlock):**
- If intraday price decline ≥ 6% occurs within the unlock window with 1h liquidation volume ≥ 2× the 7-day average: the cascade is confirmed as active — all three tranches are eligible to fill. Maintain GTC orders.
- If price declines without liquidation spike (orderly selling): reduce GTC orders to Tranche 1 only (the cascade amplification is not present; the supply is being absorbed normally).

### Phase 4: Position management post-fill

**Exit after fill:**
- Target exit: hold for **5–10 days** post-fill, aiming for a 8–15% recovery from the tranche entry price.
- Stop: close if the token continues declining ≥ 10% below the lowest filled tranche entry (cascade extending beyond the initial fade; the leverage structure has more fuel).
- Alternative: close if OI has declined ≥ 20% from unlock-date levels (deleveraging complete; further cascade recovery is likely but carry cost rising).

## Implementation pseudocode

```python
# unlock_cascade_watch.py
from dataclasses import dataclass
from typing import Optional

# ---- unlock eligibility ----
MIN_UNLOCK_PCT          = 0.03    # >= 3% of circulating supply
WINDOW_OPEN_DAYS        = 28      # monitor from <= 28 days before
WINDOW_CLOSE_DAYS       = 10      # orders expire 10 days after unlock

# ---- risk classification ----
HIGH_OI_PCT             = 75.0    # OI >= 75th pct
HIGH_FUNDING_7D         = 0.00030 # funding >= 0.030%/8h (7d avg)
MOD_OI_PCT              = 50.0
MOD_FUNDING_7D          = 0.00015

# ---- de-risk sizing ----
HIGH_RISK_RETAIN        = 0.25    # retain 25% of normal position
MOD_RISK_RETAIN         = 0.50

# ---- cascade-fade triggers ----
FADE_OI_PCT_MIN         = 70.0    # OI still >= 70th pct at T-1
FADE_FUNDING_MIN        = 0.00025 # funding >= 0.025%/8h at T-1
MAX_PREUNLOCK_DECLINE   = 0.08    # skip fade if already -8% pre-unlock

# ---- fade tranche levels ----
FADE_LEVELS             = [-0.08, -0.14, -0.20]   # below T-1 close
FADE_TRANCHE_SIZES      = [0.30, 0.40, 0.30]      # % of target size per tranche
PORTFOLIO_PCT_HIGH      = 0.04    # 4% of portfolio total for HIGH risk
PORTFOLIO_PCT_MOD       = 0.025   # 2.5% of portfolio for MODERATE

# ---- cascade confirmation ----
CASCADE_PRICE_DROP      = 0.06    # intraday drop >= 6% = cascade active
CASCADE_LIQ_MULT        = 2.0     # 1h liq volume >= 2x 7d avg = cascade confirmed

# ---- post-fill exits ----
POST_FILL_TARGET_PCT    = 0.08    # 8% recovery from fill = exit target (min)
POST_FILL_STOP_PCT      = 0.10    # 10% below lowest fill = stop

@dataclass
class UnlockEventState:
    token: str
    days_to_unlock: int
    unlock_pct_supply: float
    oi_30d_percentile: float
    funding_7d_avg: float
    long_short_ratio: float
    price_t_minus_5_change: float   # price change vs 5 days ago
    liq_1h_volume: float
    liq_7d_avg_volume: float

def classify_risk(s: UnlockEventState) -> str:
    if (s.oi_30d_percentile >= HIGH_OI_PCT
            and s.funding_7d_avg >= HIGH_FUNDING_7D):
        return "HIGH"
    if (s.oi_30d_percentile >= MOD_OI_PCT
            or s.funding_7d_avg >= MOD_FUNDING_7D):
        return "MODERATE"
    return "LOW"

def derisking_action(risk: str, position_size_usd: float) -> dict:
    if risk == "HIGH":
        target = position_size_usd * HIGH_RISK_RETAIN
        return {"action": "REDUCE_TO", "target_usd": round(target, 0),
                "reason": f"HIGH risk window: retain {HIGH_RISK_RETAIN:.0%} of position"}
    if risk == "MODERATE":
        target = position_size_usd * MOD_RISK_RETAIN
        return {"action": "REDUCE_TO", "target_usd": round(target, 0),
                "reason": f"MODERATE risk window: retain {MOD_RISK_RETAIN:.0%} of position"}
    return {"action": "HOLD", "reason": "LOW risk window: no de-risking required"}

def cascade_fade_orders(
    s: UnlockEventState,
    t_minus_1_close: float,
    portfolio_capital: float,
    risk_class: str,
) -> Optional[list[dict]]:
    # Check pre-conditions
    if s.oi_30d_percentile < FADE_OI_PCT_MIN:
        return None  # OI deflated pre-unlock; no cascade fuel
    if s.funding_7d_avg < FADE_FUNDING_MIN:
        return None  # funding not elevated; no crowded longs to cascade
    if s.price_t_minus_5_change <= -MAX_PREUNLOCK_DECLINE:
        return None  # cascade may have already occurred
    total_notional = (portfolio_capital * PORTFOLIO_PCT_HIGH if risk_class == "HIGH"
                      else portfolio_capital * PORTFOLIO_PCT_MOD)
    orders = []
    for level, size_pct in zip(FADE_LEVELS, FADE_TRANCHE_SIZES):
        orders.append({
            "type": "GTC_LIMIT_BUY",
            "price": round(t_minus_1_close * (1 + level), 2),
            "notional": round(total_notional * size_pct, 0),
            "level_pct": f"{level:.0%}",
        })
    return orders

def cascade_confirmed(s: UnlockEventState) -> bool:
    return (s.liq_1h_volume >= s.liq_7d_avg_volume * CASCADE_LIQ_MULT)
```

The production system adds: an unlock calendar feed (via tokenunlocks.app API or equivalent); a daily OI/funding monitor per unlocking token; an alert system that escalates from "MODERATE risk identified" at T − 14 to "de-risk now" at T − 7 to "cascade-fade orders active" at T − 1; and a post-trade log recording which tranches filled, the average fill price, the subsequent price recovery, and whether the cascade confirmation gate was met.

## Indicators / data used

- **Token unlock calendar** — public data from tokenunlocks.app, Coinglass, or The Block unlock tracker. Not available via CryptoDataAPI; requires a separate data source. Cross-reference with on-chain vesting contract reads where available.
- **Open interest (per token)** — `GET /api/v1/derivatives/open-interest?coin={TOKEN}`; current OI, 30d percentile computation for risk classification and cascade-fade pre-condition.
- **Funding rates (per token)** — `GET /api/v1/derivatives/funding-rates?coin={TOKEN}`; 7-day average 8h funding for risk classification and cascade-fade pre-condition.
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio`; supplemental leverage indicator for risk classification.
- **Liquidations** — `GET /api/v1/market-intelligence/liquidations`; 1h liquidation volume for cascade-confirmation gate (real-time monitoring).
- **4h OHLCV** — `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=4h&limit=30`; price-decline measurement for pre-unlock cascade detection and post-fill monitoring.
- **Regime** — `GET /api/v1/regimes/current`; if `Structural_Shock`, de-risk all positions immediately regardless of unlock window status.

## Example trade

**Setup (illustrative — mid-cap DeFi token unlock):**

- Token "DFX" has a cliff unlock of 4.8% of circulating supply in 12 days (T − 12). Unlock is team/investor allocation from a 12-month linear vest that cliff-releases.
- **T − 12 assessment:**
  - OI at 78th percentile of trailing 30d (HIGH threshold = 75th). CHECK.
  - 7d avg 8h funding = +0.038%/8h (HIGH threshold = +0.030%/8h). CHECK.
  - Long/short = 1.52.
  - **Risk classification: HIGH.**

**De-risking (T − 7):** Current DFX long position = $4,000 (4% of $100,000 portfolio). Reduce to 25% = $1,000. Sell $3,000 DFX at current price $2.85.

**T − 1 check for cascade-fade orders:**
- OI at 74th percentile (≥ 70th). CHECK.
- 7d avg funding = +0.032%/8h (≥ 0.025%/8h). CHECK.
- Price vs 5 days ago: −3.2% (< −8% pre-unlock decline threshold). CHECK.
- **Cascade-fade orders staged:**
  - Tranche 1 (30% × $4,000 = $1,200): limit buy at $2.85 × 0.92 = $2.62.
  - Tranche 2 (40% × $4,000 = $1,600): limit buy at $2.85 × 0.86 = $2.45.
  - Tranche 3 (30% × $4,000 = $1,200): limit buy at $2.85 × 0.80 = $2.28.

**Unlock day (T):** DFX opens at $2.80. Team wallet begins distributing. Price declines through the session.
- 2h into unlock: price at $2.58 (−9.3% from T − 1 close). 1h liquidation volume = 3.2× 7d avg. Cascade confirmed.
- Tranche 1 fills at $2.62.
- Price continues to $2.41. Tranche 2 fills at $2.45.
- Trough at $2.31. Tranche 3 does not fill (order at $2.28). Price begins to recover.

**Post-fill (5 days later):** DFX recovers to $2.80 (+15.5% from Tranche 1, +14.3% from Tranche 2 average). Target exit fires (≥ 8% recovery from fills).
- Tranche 1: $1,200 × 0.155 = +$186. Tranche 2: $1,600 × 0.143 = +$229. Total gross P&L from fade: +$415.
- Less 35 bps: −$14.16. Net fade P&L: **+$401** / +0.40% of portfolio.
- De-risking gain: sold $3,000 at $2.85 (T − 7), re-exposure at avg $2.52 = +$330 gain on the de-risked capital (in addition to the fade P&L) if re-entry is desired.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.8 | The strategy's edge is in loss prevention (de-risking) and opportunistic fade; the Sharpe reflects both components combined |
| Expected max drawdown | ~22% | Cascade-fade orders filled in an extended cascade where the token continues declining beyond the −20% tranche; the stop at −10% below lowest fill limits but does not eliminate tail loss |
| De-risking value | Material; difficult to quantify as a standalone Sharpe | Reducing to 25% of normal position ahead of a cascade that drops the token 25% saves roughly 18–19% of position value vs holding full |
| Cascade-fade win rate | ~55–65% (estimated) | Forced selling at cascade trough produces mean-reverting recoveries in 55–65% of cases; 35–45% see continued decline past fade entry |
| Cascade fill rate | ~40–60% of windows | Not all HIGH-risk unlock windows produce cascades; some unlocks are absorbed without triggering liquidation cascades |
| Breakeven cost budget | 35 bps | Perp exits (de-risk) and limit-order entries (cascade-fade); taker fee on trough fills |

## Capacity limits

- **Per position:** cascade-fade limit orders in mid-cap token perps ($200M–$2B market cap) can absorb $200,000–$1,000,000 in trough fills without significant market impact. Very small tokens (< $100M) have thin perp markets.
- **Aggregate:** `capacity_usd: 20000000` reflects the book size where monitoring 5–10 simultaneous unlock windows is feasible and the cascade-fade order sizes remain within token liquidity.
- **Binding constraint:** token perp liquidity at the cascade trough (extreme slippage in thin markets) and the availability of perp markets for smaller tokens.

## What kills this strategy

1. **Unlock supply absorbed without cascade (#1: Primitive degradation).** The majority of token unlocks are absorbed without a price cascade — the unlocking team/investors either hold, sell OTC, or distribute slowly. In LOW-risk or MODERATE-risk windows (low OI/funding), the cascade fade orders simply do not fill and the de-risking was unnecessary (a small cost from the de-risking transaction and the spread).
2. **Extended cascade beyond staged fade levels (#3: Market-structure change).** If a cascade exceeds the −20% fade level (the deepest tranche), the position is underwater and the stop fires at an additional −10% below the lowest fill. In severe cascades (−35–50% from unlock price), the fade entries become a loss rather than a recovery opportunity.
3. **Unlock calendar data latency or error (#7: Operational).** If the unlock date is incorrectly recorded (wrong date, wrong supply amount), the de-risking window may be misaligned with the actual event. Sourcing from multiple unlock calendars and cross-referencing with on-chain vesting contracts reduces but does not eliminate this risk.
4. **Token without liquid perp market (#7: Operational).** Smaller tokens may not have a Binance or Bybit perp market. Without funding and OI data, the leverage structure cannot be assessed; the cascade-fade order system cannot be implemented systematically. Reverts to manual de-risking using spot price technicals.
5. **Market-wide structural shock synchronised with unlock (#3).** If a systemic event (exchange collapse, macro shock) coincides with the unlock window, both the de-risking and the cascade-fade will occur in a deteriorating market. The cascade-fade entries become directional bets in a risk-off environment rather than fade entries into a token-specific supply shock.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 22%** from high-water mark — cascade-fade orders are not recovering; the post-fill stop is consistently firing; reduce cascade-fade tranche sizes or require a higher cascade-confirmation bar.
2. **6 consecutive HIGH-risk unlock windows where no price cascade ≥ 8% occurred within 10 days** — the leverage structure is present but cascades are not materialising; either token distribution is being absorbed OTC or the market structure has changed. Reduce the window size or require a higher OI threshold.
3. **Rolling 8-signal P&L negative on cascade-fade executions** — cascade fades are not recovering; the token is not mean-reverting post-cascade; recalibrate the fade levels or hold duration.
4. **Token unlock data source becomes unreliable** — calendar integrity is the foundation; if the data cannot be trusted, suspend the strategy until a reliable source is confirmed.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Risk-reduction function is additive regardless of trade P&L.** Even if the cascade-fade orders never fill (the unlock is absorbed without a cascade), the de-risking of existing longs ahead of a high-risk unlock window provides asymmetric protection: avoid the 15–25% loss in the minority of unlocks that do cascade, at the cost of a 35-bps transaction to de-risk and a potential 3–5% upside foregone if the token holds up.
- **Pre-staged limit orders capture the cascade trough without requiring real-time execution.** Cascade events occur rapidly (1–4 hours). Pre-staged limit orders are filled automatically during the cascade trough without requiring a human to be monitoring a screen at the exact moment. This is a significant operational advantage over reactive fade strategies.
- **Complementary to, not competing with, the unlock-short family.** [[unlock-short-with-crowding-gate]] and [[unlock-pair-hedge]] take DIRECTIONAL shorts into the unlock. This page manages existing longs and fades the cascade bottom. The two approaches can be used simultaneously: short via [[unlock-short-with-crowding-gate]] for the directional bet and apply this page's cascade-fade framework for the counter-trade at the trough. The combined strategy captures both the descent and the recovery.
- **Provides a framework for applying leverage-structure monitoring to any event-driven risk window.** The core monitoring framework (OI percentile + funding monitoring ahead of a binary event) is transferable beyond unlocks to any scheduled event that can create concentrated forced selling (regulatory decisions, fork dates, large vesting contract expirations).

## Disadvantages

- **Requires external token unlock calendar data.** CryptoDataAPI does not provide a token unlock schedule; this must be sourced from tokenunlocks.app, Coinglass, or on-chain vesting contract reads. This is an additional infrastructure dependency not required by other combination pages in this wiki.
- **Two-phase complexity (de-risk + fade) requires coordination.** Separately managing the de-risking of existing longs AND the cascade-fade order staging requires coordination. If the de-risking is done and then the cascade-fade orders are NOT placed (due to low OI at T − 1), the de-risked position has no mechanism for re-entry — the trader is simply out of the position without a plan to get back in.
- **False-positive windows consume attention and de-risking transaction costs.** HIGH-risk unlock windows that do not produce cascades (the majority) still require de-risking transactions (selling 75% of the position at T − 7) and then re-entry after the window clears. Each such false-positive window costs 35–70 bps in round-trip transaction costs.
- **Not applicable to tokens without perp markets.** The monitoring framework is inapplicable to the large universe of small-cap tokens with no perp market. Those tokens must be managed with price-based technical exits only.

## Sources

- [[unlock-short-with-crowding-gate]] — the directional-short approach to token unlocks; the crowding gate in that page uses the same funding/OI screen that this page uses for risk classification. Differentiated as active directional short vs risk-management and fade framework.
- [[unlock-pair-hedge]] — the beta-hedged pairs approach to unlock shorts; complementary at the directional layer.
- [[liquidation-cascade-fade]] — the general cascade-fade framework without event-calendar anchoring; this page adapts that fade logic specifically to the unlock event window.
- [[oi-aware-grid]] — the OI-percentile monitoring approach applied to grid de-risking; the same OI percentile monitoring logic is used in this page for unlock window risk classification.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/open-interest?coin={TOKEN}` — current OI and 30d trend for risk classification and cascade-fade pre-condition check
- `GET /api/v1/derivatives/funding-rates?coin={TOKEN}` — 8h funding and 7-day average for risk classification and cascade-fade pre-condition
- `GET /api/v1/derivatives/binance/long-short-ratio` — long/short ratio for risk classification confirmation
- `GET /api/v1/market-intelligence/liquidations` — real-time 1h liquidation volume for cascade-confirmation gate
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=4h&limit=30` — 4h OHLCV for price-decline measurement and post-fill monitoring
- `GET /api/v1/regimes/current` — regime override; Structural_Shock triggers immediate full de-risk

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=60` — 2-month daily derivatives history for OI percentile calibration and cascade-episode analysis
- `GET /api/v1/market-data/klines?symbol={TOKEN}USDT&interval=1d&limit=60` — daily closes for price-decline analysis around historical unlock dates

*Note: the token unlock calendar itself is not available via CryptoDataAPI. Source from tokenunlocks.app, Coinglass unlock tracker, or on-chain vesting contract reads directly.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=OP"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-market-data]], [[cryptodataapi-regimes]].

## Related

- [[unlock-short-with-crowding-gate]] — directional short into token unlock, gated on non-consensus crowding; the active-short complement to this page's risk-management and fade framework
- [[unlock-aware-momentum]] — momentum book pause around unlocks; this page extends that logic with a cascade-fade component and explicit leverage-structure monitoring
- [[unlock-pair-hedge]] — beta-hedged long-short pair for unlock events; the structured pairs alternative to this page's single-token focus
- [[liquidation-cascade-fade]] — general cascade fade without event-calendar anchoring; this page is the event-calendar-anchored variant
- [[off-hours-liquidation-playbook]] — session-conditional cascade fade; the timing-anchored variant vs this page's event-calendar anchor
- [[leverage-stress-tail-hedge]] — accumulate puts when leverage stress metrics are elevated; the portfolio-level risk hedge vs this page's token-specific de-risk
- [[event-vol-buying]] — calendar-triggered vol buying ahead of binary events; the options-instrument version of pre-event positioning
- [[oi-aware-grid]] — OI-percentile monitoring for grid de-risking; the same OI monitoring logic in a different primitive context
- [[cascade-monetization-rotation]] — the full lifecycle of tail-hedge-to-cascade-fade capital rotation; the more complete version of this page's cascade-fade component
- [[funding-rate]] — the carry signal for leverage-structure assessment
- [[open-interest]] — the primary leverage indicator for risk classification
- [[liquidations]] — the real-time cascade-confirmation signal
- [[perpetual-futures]] — the derivative market where OI and funding are measured
- [[edge-taxonomy]] — structural + informational + behavioral classification
- [[failure-modes]] — cascade not materialising, extended cascade, calendar data error, illiquid perp market
- [[when-to-retire-a-strategy]] — kill vs pause framework
