---
title: "Put-Protected Dip Buying"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, derivatives, mean-reversion, tail-risk, risk-management, behavioral-finance, quantitative, crypto, bitcoin, ethereum]
aliases: ["Defined-Stop Dip Buy", "OTM-Put-Hedged Capitulation Entry", "Knife-Catch with Floor", "Protected Mean-Reversion Buy"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Post-capitulation spot sellers and liquidated longs create a mean-reversion discount at cycle lows; OTM puts purchased alongside the dip entry hard-cap the disaster scenario so the buyer cannot gap through a defined floor — the counterparty absorbing the disaster risk is the vol-seller who prices that floor as a premium; the buyer pays a defined insurance cost to hold the entry through the noise with certainty that catastrophic tail loss is bounded."

data_required: [ohlcv-daily, ohlcv-4h, funding-rates, open-interest, options-chain, dvol-history, fear-greed-index, exchange-netflow, liquidation-feed]
min_capital_usd: 20000
capacity_usd: 75000000
crowding_risk: low

expected_sharpe: 0.85
expected_max_drawdown: 0.20
breakeven_cost_bps: 70

decay_evidence: "Post-capitulation mean reversion in crypto is documented in Liquidation Cascade Fade and OI Flush Reversion pages; the marginal value of the put overlay (defined stop preventing gap-through) has no published crypto study. The insurance cost scales with DVOL — in high-DVOL post-panic windows the overlay becomes expensive and the strategy's net edge is more compressed. The combination is additive as long as the put cost is less than the mean-reversion premium captured."

kill_criteria: |
  - sleeve drawdown > 20% from high-water mark
  - 5 consecutive dip entries where the dip continued ≥ 20% beyond entry before recovering (the entry timing is wrong, not just the overlay)
  - average put cost-as-% of position gain > 60% over rolling 10 events (overlay cost consuming majority of mean-reversion premium; recalibrate strike selection or entry timing)
  - put expires worthless AND mean-reversion target never reached across 4 consecutive events (the reversion is not occurring within the option's DTE window; mismatch between DTE and reversion speed)
  - DVOL ≥ 95th percentile at entry for 3 consecutive events: overlay is consistently purchased at worst-value pricing; recalibrate entry to require lower DVOL

related: ["[[funding-flush-reversal]]", "[[oi-flush-reversion]]", "[[onchain-capitulation-confluence]]", "[[leverage-stress-tail-hedge]]", "[[protective-put]]", "[[cascade-monetization-rotation]]", "[[post-panic-vol-selling]]", "[[crowded-short-funding-fade]]", "[[liquidation-cascade-fade]]", "[[post-liquidation-rebound]]", "[[deribit]]", "[[dvol]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[open-interest]]", "[[funding-rate]]", "[[fear-and-greed-index]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Put-Protected Dip Buying

Put-protected dip buying is a **mean-reversion entry with a hard disaster floor**: a dip-buy position (spot or perp long) in BTC or ETH at a post-capitulation discount is opened simultaneously with an OTM put on the same underlying, so the maximum loss on the downside is bounded at the put strike rather than being open-ended. The defining feature is that the disaster stop **cannot gap through** — unlike a stop-loss order, which fails in a flash-crash or overnight gap, the put option is a contractual payoff that delivers regardless of how far and how fast the underlying falls. The primitive is mean-reversion at capitulation lows (the same thesis as [[funding-flush-reversal]], [[oi-flush-reversion]], and [[onchain-capitulation-confluence]]); the overlay is the OTM put that converts the infinite downside tail into a defined, pre-paid cost.

**This is explicitly differentiated from [[funding-flush-reversal]]** — that page defines WHEN to enter a dip-buy (after funding has sustained below −0.02%/8h for 24h+ confirming deleveraging is complete). This page defines the RISK STRUCTURE of the buy, not the timing signal. Put-protected dip buying can be combined with any of the three capitulation entry signals ([[funding-flush-reversal]], [[oi-flush-reversion]], [[onchain-capitulation-confluence]]) — they define the entry trigger; this page defines how the position is protected once entered.

**This is differentiated from [[leverage-stress-tail-hedge]]** — that page accumulates OTM puts in advance, during the stress-buildup phase, as a standalone tail hedge (no spot/perp long entry). This page buys the put simultaneously with a spot/perp long, specifically as a protective overlay at the time of entry. The put here is a capped disaster stop, not a pre-positioned crash hedge.

**This is differentiated from [[cascade-monetization-rotation]]** — that strategy is a lifecycle: accumulate puts, monetise in the crash, rotate the payoff into a fade entry. This page is simpler and synchronous: enter the long AND buy the protective put at the same time. There is no prior put book, no rotation mechanics.

**This is differentiated from [[crowded-short-funding-fade]]** — that page goes long when shorts are crowded and funding is negative (purely positioning-based entry, no tail protection overlay). This page adds the put overlay to cap the disaster scenario regardless of the entry trigger used.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — post-capitulation spots and perp markets are driven by forced sellers, panic liquidations, and emotional retail participants whose selling pressure overshoots fair value. This creates the mean-reversion discount that the dip-buy leg harvests — the same behavioral mechanism as [[funding-flush-reversal]] and [[liquidation-cascade-fade]].
- **Structural** — the OTM put provides structural protection against the exact scenario that kills naked dip-buying: a cascade that continues beyond the entry level. The put floor converts what would be an unlimited downside into a bounded, pre-paid cost.
- **Risk-bearing** — the strategy bears two risks: (a) the mean-reversion does not occur within the option's DTE window (the long reaches time-exit with a small gain or loss, and the put expires worthless, net of theta); (b) the entry is early and the cascade has further legs, but the put limits the loss to the floor. The premium paid is the compensation demanded by the option seller for taking on that conditional tail risk.

## Why this edge exists

**The edge is the combination of a known mean-reversion premium with a catastrophic tail that is explicitly priced and pre-paid:**

1. **Naked dip-buying is psychologically difficult to hold through secondary drops.** Most mean-reversion dip-buyers exit at the worst possible time: when the price drops further after their entry, triggering their stop-loss or emotional exit. The put overlay changes the psychology of the hold. Because the maximum loss is hard-floored at the put strike, the holder does not face ruin in the secondary-cascade scenario — they face a known maximum loss. This allows them to hold through the noise until the mean-reversion materialises, which is the key to capturing the full reversion premium.

2. **The put converts a probabilistic stop into a contractual floor.** A stop-loss order at, say, 15% below entry is an intention, not a guarantee: in a flash-crash or after-hours liquidity vacuum, the fill can be 20–30% below the stop level. A put at the same strike delivers its intrinsic value regardless of how the market moves. This is especially valuable in crypto, where gap-opens and weekend liquidations are common.

3. **OTM put pricing in crypto post-capitulation is imperfect.** In the days immediately following a large cascade, DVOL is elevated (the surface has repriced the recent crash risk), but the near-term risk of a second cascade is actually declining (the leveraged fuel has been purged — see [[oi-flush-reversion]]). The put is expensive in absolute terms but may be appropriately or even under-priced relative to the residual tail risk at entry. The strategy pays a defined cost for a protection that is structurally worth more than its Black-Scholes price in a market where bid-ask spreads are wide and vol uncertainty is high.

**Who is on the other side:** the option seller (typically a Deribit market-maker or systematic vol-seller) who prices the put premium based on current DVOL — which is elevated post-panic. The strategy pays the post-panic premium for a protection that it then treats as the disaster stop. The option seller captures the fear premium; the dip-buyer uses that same premium to eliminate the ruin scenario.

## Null hypothesis

Under the null, adding a protective OTM put to a dip-buy entry produces **no incremental Sharpe improvement** over a naked dip-buy with a hard stop-loss at the equivalent strike:
- The put overlay should not produce a higher average P&L per entry than a stop-loss order placed at the same level as the put strike, net of the put premium vs stop-loss slippage.
- The survivorship benefit (avoiding flash-crash gap-through) should be offset by the cost of put premium, which is non-zero and always paid even when no extreme crash occurs.
- The psychological benefit (holding through secondary dips without exiting) should not translate into measurably higher capture of the mean-reversion move relative to a disciplined stop-loss user.

Currently not rejected (`backtest_status: untested`). The null is plausible: in liquid markets with tight bid-ask spreads on options and good stop-loss fill quality, the put overlay may add cost without adding proportionate protection. The edge case is the flash-crash / gap-open scenario where a stop-loss fills 10–25% below its intended price — the put delivers its intrinsic value regardless.

## Rules

### Entry trigger (choose one of the three capitulation confirmation methods)

**Method A — Funding flush confirmation (from [[funding-flush-reversal]])**
- 8h funding has sustained below **−0.02%/8h** for **24+ consecutive hours**.
- BTC/ETH has declined ≥ **8%** from its recent 5-day high.
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.

**Method B — OI flush confirmation (from [[oi-flush-reversion]])**
- BTC/ETH OI has declined ≥ **15%** from its 5-day peak.
- Price is ≥ **6%** below the high at the time of peak OI.
- Source: `GET /api/v1/derivatives/open-interest?coin=BTC`.

**Method C — On-chain + sentiment confluence (from [[onchain-capitulation-confluence]])**
- On-chain capitulation signal active: exchange inflow spike (top-decile, from `/api/v1/on-chain/exchange-flows/spike-alerts`) AND Fear & Greed ≤ 20 for 2+ consecutive days.
- Source: `/api/v1/on-chain/exchange-flows/BTC` and `/api/v1/sentiment/fear-greed-index`.

Any one of the three methods qualifying is sufficient to activate the entry timer. Preference ranking: Method C (strongest confluence) > Method A > Method B.

### Protective put selection

**Strike selection:**
- Buy the OTM put at a strike **15–20% below the spot entry price**. This strike defines the hard floor; losses below this level are covered by the put payoff.
- Example: BTC entry at $74,000 → buy 25-delta (approximately 15–20% OTM) BTC put, strike ≈ $61,000–$63,000.

**Expiry selection:**
- DTE ≥ **21 days** and ≤ **45 days**. The expiry must be long enough to allow the mean-reversion to materialise; do not use front-week options where theta is punishing and the reversion window is too narrow.

**Premium budget:**
- Cap the put cost at **1.5–2.5%** of the notional long position. If the current DVOL implies a put premium higher than 2.5% of notional at the 15–20% OTM strike, do not enter — the overlay is too expensive relative to the mean-reversion premium being targeted.
- Source: Deribit API for option pricing; DVOL from `GET /api/v1/market-intelligence/dvol-history`.

### Position sizing

- **Long position notional:** size the spot or perp long to risk no more than **2–3% of portfolio** on the full position (including the put premium as a cost).
- **Maximum concurrent positions:** 1 protected dip-buy at a time. Multiple concurrent dip-buys would represent directional concentration inconsistent with the defined-stop discipline.

### Exit rules

**Profit exit (mean-reversion target):**
- Close the long position when BTC/ETH recovers to **50–70% of the decline from the 5-day high** (i.e., partial recovery of the capitulation move). At this point, the put still has residual time value — sell it back on Deribit or let it decay (cheap at this point).

**Stop exit (put floor reached):**
- If spot falls to the put strike, the position is fully hedged below that level. Close the long position and exercise/sell the put to realise the payoff. The net loss on the combined position is bounded: maximum loss = initial entry price − put strike + put premium paid (expressed as % of notional).

**Time exit:**
- If neither profit target nor put floor is reached, close both the long and the put at expiry −3 days to recapture any remaining time value in the put.

## Implementation pseudocode

```python
# put_protected_dip_buying.py

from dataclasses import dataclass
from typing import Optional

# ---- entry thresholds ----
FUNDING_FLUSH_THRESHOLD   = -0.0002   # -0.02%/8h
FUNDING_FLUSH_HOURS       = 24        # sustained for 24+ hours
OI_FLUSH_THRESHOLD        = 0.15      # OI dropped >= 15% from 5d peak
PRICE_DIP_FROM_PEAK_MIN   = 0.06      # price >= 6% below OI-peak high
FEAR_GREED_EXTREME        = 20        # Fear & Greed <= 20
FEAR_DAYS_REQUIRED        = 2         # consecutive days at extreme fear

# ---- put overlay ----
PUT_STRIKE_OTM_PCT        = 0.175     # put strike = entry_price * (1 - 0.175)
PUT_DTE_MIN               = 21        # minimum 21 days to expiry
PUT_DTE_MAX               = 45        # maximum 45 days
PUT_MAX_COST_PCT_NOTIONAL = 0.025     # put premium <= 2.5% of long notional
DVOL_MAX_FOR_ENTRY        = None      # computed dynamically; skip if put > 2.5% of notional

# ---- exit rules ----
RECOVERY_TARGET_FRACTION  = 0.60      # close long at 60% recovery of capitulation decline
MAX_PORTFOLIO_RISK_PCT    = 0.03      # max 3% of portfolio at risk per position

@dataclass
class MarketState:
    spot_price:          float
    oi_current:          float
    oi_5d_peak:          float
    funding_8h_history:  list[float]   # last 3 readings (24h of 8h intervals)
    fear_greed:          float
    fear_greed_prev:     float
    exchange_inflow_spike: bool        # top-decile exchange inflow alert
    dvol_current:        float

@dataclass
class ProtectedPosition:
    entry_price:         float
    put_strike:          float
    put_premium_pct:     float    # as fraction of notional
    dte:                 int
    high_at_peak:        float    # 5d high at entry time (for recovery calc)

def funding_flush_confirmed(s: MarketState) -> bool:
    return all(f < FUNDING_FLUSH_THRESHOLD for f in s.funding_8h_history)

def oi_flush_confirmed(s: MarketState) -> bool:
    oi_drop = (s.oi_5d_peak - s.oi_current) / s.oi_5d_peak
    return oi_drop >= OI_FLUSH_THRESHOLD

def onchain_sentiment_confirmed(s: MarketState) -> bool:
    return (s.exchange_inflow_spike
            and s.fear_greed <= FEAR_GREED_EXTREME
            and s.fear_greed_prev <= FEAR_GREED_EXTREME)

def estimate_put_cost(entry_price: float, put_strike: float,
                      dvol: float, dte: int) -> float:
    """Approximate BS put premium as % of entry_price — simplified for gate check.
    In production: query Deribit /api/v2/public/get_order_book for live bid."""
    import math
    sigma = dvol / 100
    t = dte / 365
    moneyness = put_strike / entry_price
    approx_delta = max(0.05, min(0.40, 0.5 - (1 - moneyness) / (sigma * math.sqrt(t) * 2)))
    premium_approx = approx_delta * sigma * math.sqrt(t) * entry_price
    return premium_approx / entry_price

def entry_decision(s: MarketState, portfolio_capital: float) -> Optional[dict]:
    # Check any entry method passes
    method_a = funding_flush_confirmed(s)
    method_b = oi_flush_confirmed(s)
    method_c = onchain_sentiment_confirmed(s)
    if not (method_a or method_b or method_c):
        return None

    # Determine put parameters
    put_strike = s.spot_price * (1 - PUT_STRIKE_OTM_PCT)
    put_cost_pct = estimate_put_cost(s.spot_price, put_strike, s.dvol_current, PUT_DTE_MIN + 7)
    if put_cost_pct > PUT_MAX_COST_PCT_NOTIONAL:
        return {"action": "SKIP",
                "reason": f"put too expensive: {put_cost_pct:.2%} > {PUT_MAX_COST_PCT_NOTIONAL:.2%}; DVOL={s.dvol_current:.1f}"}

    # Size the position: risk = (entry - put_strike) + put_premium = floor width + cost
    floor_width_pct  = PUT_STRIKE_OTM_PCT
    total_risk_pct   = floor_width_pct + put_cost_pct      # max loss as % of notional
    max_notional     = portfolio_capital * MAX_PORTFOLIO_RISK_PCT / total_risk_pct
    method_label     = ("C (on-chain+sentiment)" if method_c
                        else "A (funding-flush)" if method_a
                        else "B (OI-flush)")
    return {
        "action":         "ENTER_LONG_WITH_PUT",
        "entry_price":    s.spot_price,
        "long_notional":  max_notional,
        "put_strike":     put_strike,
        "put_cost_pct":   put_cost_pct,
        "max_loss_pct":   total_risk_pct,
        "method":         method_label,
        "note": (f"capitulation entry confirmed via Method {method_label}; "
                 f"buy put strike={put_strike:.0f} ({PUT_STRIKE_OTM_PCT:.0%} OTM), "
                 f"DTE=21-45, cost≈{put_cost_pct:.2%} of notional, "
                 f"hard floor at {put_strike:.0f}"),
    }

def exit_decision(pos: ProtectedPosition, current_price: float, dte_remaining: int) -> Optional[dict]:
    decline_from_peak = pos.high_at_peak - pos.entry_price
    recovery = (current_price - pos.entry_price) / decline_from_peak if decline_from_peak > 0 else 0
    if recovery >= RECOVERY_TARGET_FRACTION:
        return {"action": "CLOSE_PROFIT",
                "reason": f"{recovery:.0%} recovery of capitulation decline — mean-reversion target reached"}
    if current_price <= pos.put_strike:
        return {"action": "CLOSE_PUT_FLOOR",
                "reason": f"spot {current_price:.0f} at/below put strike {pos.put_strike:.0f}; close long, realise put payoff"}
    if dte_remaining <= 3:
        return {"action": "CLOSE_TIME",
                "reason": f"DTE={dte_remaining} — expiry-3d time exit; close long, sell residual put time value"}
    return None
```

The production system adds: Deribit WebSocket for live put pricing and delta-hedge monitoring; a daily put-cost recalculation to confirm the overlay is still within budget; and an alert system that fires within 30 minutes of any capitulation-method confirmation so the entry and simultaneous put purchase can be executed before the market moves away from the capitulation low.

## Indicators / data used

- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (Method A: sustained negative funding confirming deleveraging)
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC` (Method B: OI decline ≥ 15% from 5d peak)
- **Exchange flows (BTC inflow spike)** — `GET /api/v1/on-chain/exchange-flows/BTC` and `GET /api/v1/on-chain/exchange-flows/spike-alerts` (Method C: on-chain capitulation signal)
- **Fear & Greed index** — `GET /api/v1/sentiment/fear-greed-index` (Method C: sentiment extreme gate; also provides context for put timing)
- **DVOL** — `GET /api/v1/market-intelligence/dvol-history`; current DVOL used to estimate put premium budget gate and compare to 30-day average for context
- **4h OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50`; recent price action for entry timing and 5-day high reference
- **Liquidations** — `GET /api/v1/market-intelligence/liquidations?coin=BTC`; context check — if cascades are still occurring, defer entry even if capitulation signal fires
- **Regime** — `GET /api/v1/regimes/current`; if `Structural_Shock`, defer entry (ongoing systemic shock)
- **OTM put pricing (Deribit)** — specific strike pricing NOT available via CryptoDataAPI; source from [[deribit]] API directly (`GET /api/v2/public/get_order_book?instrument_name=BTC-{date}-{strike}-P`)

*Note: OTM put pricing for specific strikes requires [[deribit]] API access. This is consistent with [[leverage-stress-tail-hedge]], [[post-panic-vol-selling]], and [[cascade-monetization-rotation]].*

## Example trade

**Setup (illustrative — OI-flush-confirmed entry with put overlay):**

- BTC has declined from $82,000 (5-day high) to $70,200 (−14.4% over 4 days) following a large exchange-halt headline.
- **Method B confirmation:** OI peaked at $24.5B, now $20.0B (−18.4% — above 15% threshold); price is 14.4% below the OI-peak high (above 6% threshold). Entry method confirmed.
- **DVOL check:** DVOL = 84 vol points (elevated post-panic). 30d average = 58. Put at 17.5% OTM strike:
  - Entry price: $70,200. Put strike: $70,200 × (1 − 0.175) = **$57,915**.
  - Estimated put premium at DTE=28, strike=$57,915, DVOL=84: approximately 1.9% of spot = $1,334/unit.
  - 1.9% < 2.5% budget → entry proceeds.

- **Portfolio:** $200,000. Max portfolio risk = 3% = $6,000.
  - Floor width = 17.5% of notional; put cost = 1.9%. Total risk per notional = 19.4%.
  - Max notional = $6,000 / 0.194 = **$30,928**.
  - Long: ~0.44 BTC at $70,200. Put: buy 0.44 units of the $57,915 put. Put premium paid: 0.44 × $1,334 = **$587**.

**Scenario A — mean-reversion materialises:**
- Over 12 days, BTC recovers. 5-day-high was $82,000; entry at $70,200; decline = $11,800.
- 60% recovery target = $70,200 + 0.60 × $11,800 = **$77,280**.
- BTC reaches $77,280. Close long. Net gain: ($77,280 − $70,200) × 0.44 = **+$3,115** gross.
- Put residual value at $77,280 spot, 16 DTE remaining: approximately 0.4% of spot = $309 each × 0.44 = **+$136** (sell the put back).
- Total gross P&L: $3,115 + $136 − $587 (put cost) = **+$2,664** / +1.33% of portfolio.

**Scenario B — second cascade fires (put floor activated):**
- After entry, a second large cascade occurs. BTC drops to $54,000 (below put strike of $57,915).
- The put is exercised. Put intrinsic value: $57,915 − $54,000 = $3,915 per unit.
- Long loss: ($54,000 − $70,200) × 0.44 = −$7,128.
- Put payoff: $3,915 × 0.44 = +$1,723.
- Net loss: −$7,128 + $1,723 − $587 = **−$5,992** / −3.0% of portfolio. Hard-floored.
- Without the put, if BTC had dropped to $54,000: loss = −$7,128 − $587 = −$7,715 (plus any potential for further gap-down below $54,000). The put saved the gap-through scenario entirely.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.85 | Mean-reversion edge net of put premium drag; higher than naked dip-buy in high-vol regimes due to drawdown reduction |
| Expected max drawdown | ~20% | Hard floor from put structure; worst case is sequential entries into a bearish regime where entries are early each time |
| Win rate (per entry) | ~60–70% (estimated) | Post-OI-flush and post-funding-flush recoveries historically occur; put floor prevents the ruin scenarios that kill the win rate |
| Put cost drag | 1.5–2.5% of notional per trade | The dominant cost; theta decay on each put; must be less than mean-reversion premium captured |
| Breakeven cost budget | 70 bps | Spot/perp entry fees ≈ 4–10 bps; Deribit put fees ≈ 3–6 bps; put premium is the dominant cost and is reflected in expected_sharpe |
| Entry frequency | 4–8 per year | Post-capitulation qualifying events (funding flush, OI flush, or on-chain confluence); less frequent than raw dip-buy signals |

**Cost overlay:** the put premium is paid up-front and is non-recoverable if the market recovers without touching the floor (Scenario A). In Scenario A, the strategy is paying 1.5–2.5% of notional for insurance that was not needed — a real cost. The justification is that the put prevents the rare but catastrophic Scenario B from wiping out the equity. The strategy's Sharpe improvement over naked dip-buying comes from eliminating the fat-tailed left tail, not from higher average wins.

## Capacity limits

- **Per entry:** Deribit BTC 25-delta put OI in the relevant expiry can support $10–30M in notional put protection. The long position capacity is set by Binance/Hyperliquid BTC perp liquidity (effectively unlimited at $75M scale).
- **Aggregate:** `capacity_usd: 75000000` reflects the binding constraint of Deribit OTM put market depth at 15–20% OTM strikes during post-panic periods, when bid-ask spreads widen substantially.
- **Post-panic timing:** the strategy typically enters during or just after a large cascade, when Deribit liquidity is thinnest. Execution of the put leg must be patient (limit orders at mid, accepting partial fills) rather than market orders.

## What kills this strategy

1. **Put premium cost exceeds mean-reversion premium captured (#2: Cost structure).** In persistent high-DVOL environments (post-systemic crisis, extended bear market), the 15–20% OTM put is priced at 2.5–4% of notional, eating most or all of the expected mean-reversion gain. The 2.5% cap on put cost prevents entry but also means the strategy is idle during the highest-risk windows.
2. **Mean-reversion does not occur within DTE (#3: Market-structure regime change).** In a structural bear market (LUNA 2022, FTX 2022), dip entries that pass the capitulation signals are followed by continued downside over multiple months. The put expires worthless, the long is stopped at time-exit, and the strategy misses the eventual recovery.
3. **Entry is too early in the cascade (#1: Primitive degradation).** If the OI-flush or funding-flush signal fires before the cascade is genuinely complete, the entry captures the midpoint of a multi-leg drop. The put floor limits the damage but does not eliminate loss.
4. **Deribit dependency in post-panic windows (#7: Operational).** Post-panic, Deribit bid-ask spreads on OTM puts can be 5–15 vol points wide. The actual put premium paid may be significantly higher than the mid-market estimate. The 2.5% cap may trigger on mid-market but the actual fill may exceed it.
5. **Crowding (#4: Crowding).** If a large cohort of dip-buyers all simultaneously purchase put protection post-capitulation, the demand for OTM puts drives DVOL further and makes the overlay more expensive, creating a self-defeating feedback.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 20% from high-water mark** — consecutive early entries into a bearish regime; the timing or the capitulation signals are failing.
2. **5 consecutive dip entries where BTC/ETH continued ≥ 20% beyond entry** before the recovery target was reached — the entry signals are not correctly identifying the capitulation level; recalibrate.
3. **Average put cost-as-% of position gain > 60% across rolling 10 events** — the overlay is consuming the majority of the mean-reversion premium; strike selection or entry timing requires recalibration.
4. **Put expires worthless AND mean-reversion target not reached in 4 consecutive events** — the reversion speed is slower than the option's DTE; extend DTE to ≥ 45 days or reconsider the overlay structure.
5. **DVOL ≥ 95th percentile at entry for 3 consecutive events** — the strategy is consistently entering during the highest-cost regime; apply a DVOL cap as an additional entry filter.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Catastrophic tail is contractually bounded** — unlike a stop-loss order, the put floor cannot be gapped through in a flash-crash, weekend cascade, or exchange-halt event. The maximum loss is pre-paid and known at entry.
- **Allows holding through secondary dips** — knowing the floor is absolute changes the holding behaviour: the position can remain open through intraday noise and secondary shakeouts that would trigger a stop-loss, increasing the probability of capturing the full mean-reversion move.
- **Combines three entry signals** — the strategy is entry-signal-agnostic; any of the three capitulation confirmation methods (funding flush, OI flush, on-chain + sentiment) can trigger entry, increasing signal frequency relative to each individual page.
- **Defined cost structure** — the put premium cap (2.5% of notional) creates a hard economic filter: if protection is too expensive to justify, the entry is skipped. This prevents entering when the overlay cost makes the trade unattractive.

## Disadvantages

- **Put premium is an always-paid cost** — in every trade, whether Scenario A (recovery) or Scenario B (put floor hit), the premium is paid. In the majority of trades (Scenario A), the put expires with reduced value and the premium represents pure insurance cost with no payoff.
- **Deribit dependency with wide post-panic spreads** — executing a put order during or immediately after a panic event, when spreads are widest, is operationally challenging. Aggressive fills are expensive; patient limit orders may miss the optimal entry window.
- **DTE mismatch risk** — if the mean-reversion takes longer than the put's DTE, the position reaches time-exit with the put nearly worthless. The strategy must then either roll the put (paying additional premium) or exit the long position at an unfavourable time.
- **Complexity vs. stop-loss** — for most practitioners, a well-placed hard stop-loss order on a liquid exchange with a small gap-risk premium is operationally simpler than purchasing a Deribit put alongside a Binance/Hyperliquid long. The strategy is appropriate only for practitioners with dual-venue execution capability.

## Sources

- [[funding-flush-reversal]] — Method A entry logic; the funding-flush confirmation is directly adapted as an entry trigger for the long leg.
- [[oi-flush-reversion]] — Method B entry logic; the OI-purge confirmation gate is directly adapted.
- [[onchain-capitulation-confluence]] — Method C entry logic; the dual on-chain + sentiment confluence gate is directly adapted.
- [[protective-put]] — the canonical options structure underlying the overlay; the [[protective-put]] page defines the mechanics of holding a long position alongside an OTM put.
- [[leverage-stress-tail-hedge]] — the nearest relative in the tail-hedge family; that page buys puts pre-crash without a simultaneous long; this page buys puts at-crash alongside the long.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — Method A: sustained negative funding confirming flush
- `GET /api/v1/derivatives/open-interest?coin=BTC` — Method B: OI decline from 5-day peak
- `GET /api/v1/on-chain/exchange-flows/BTC` — Method C: per-symbol inflow/outflow windows
- `GET /api/v1/on-chain/exchange-flows/spike-alerts` — Method C: real-time large transfer alerts for whale deposits (on-chain capitulation signal)
- `GET /api/v1/sentiment/fear-greed-index` — Method C: consecutive extreme-fear readings
- `GET /api/v1/market-intelligence/dvol-history` — put premium budget gate; DVOL percentile context
- `GET /api/v1/market-intelligence/liquidations?coin=BTC` — cascade-clear confirmation before entry
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=50` — entry timing and 5-day high reference
- `GET /api/v1/regimes/current` — structural shock check; defer entry if `Structural_Shock`

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=90` — funding and OI history for capitulation-threshold calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — daily OHLCV for post-capitulation recovery backtesting

*Note: OTM put pricing at specific strikes requires [[deribit]] API access directly (`GET /api/v2/public/get_order_book`, `GET /api/v2/public/get_instruments`). DVOL history is available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/open-interest?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-on-chain]], [[cryptodataapi-market-intelligence]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — capitulation detection across `GET /api/v1/derivatives/funding-rates?coin=BTC` (sustained negative), `GET /api/v1/derivatives/open-interest?coin=BTC` (decline from 5d peak), and `GET /api/v1/on-chain/exchange-flows/spike-alerts` (whale deposits)
- **Filter** — `GET /api/v1/market-intelligence/liquidations?coin=BTC` must show the cascade has cleared; `GET /api/v1/market-intelligence/dvol-history` sets the put-premium budget gate
- **Regime gate** — `GET /api/v1/regimes/current`; defer while `Structural_Shock` persists
- **Backtest** — post-capitulation recovery paths from `GET /api/v1/backtesting/klines` (1d back to 2017-08); the cascade-clear condition replays only since 2026-03-30 (`GET /api/v1/backtesting/liquidations`, Hyperliquid), so older backtests must proxy it from funding and OI alone
- **Tips** — the protective put is priced on Deribit; re-check the DVOL percentile at fill time — premium budgets set at signal time go stale fast in post-panic tape

## Related

- [[funding-flush-reversal]] — Method A entry trigger; defines the funding-flush confirmation gate used for the long leg
- [[oi-flush-reversion]] — Method B entry trigger; defines the OI-purge confirmation gate
- [[onchain-capitulation-confluence]] — Method C entry trigger; the dual on-chain + sentiment confluence
- [[protective-put]] — the canonical options structure for the overlay
- [[leverage-stress-tail-hedge]] — buys puts pre-crash without a long; the accumulation-phase complement to this page's simultaneous-entry structure
- [[cascade-monetization-rotation]] — lifecycle strategy: accumulate puts pre-crash, monetise, rotate into fade; a more complex alternative
- [[post-panic-vol-selling]] — on the opposite side of post-panic IV: sells vol after the crash; this page buys puts alongside the long entry
- [[crowded-short-funding-fade]] — long entry when shorts are crowded; this page adds the put overlay to that entry type
- [[liquidation-cascade-fade]] — standalone cascade fade without put protection; the unprotected analog
- [[post-liquidation-rebound]] — the recovery dynamics this page captures with defined downside
- [[deribit]] — the options execution venue for the put overlay
- [[dvol]] — DVOL index; used to gate put cost and assess surface regime
- [[implied-volatility]] — the options surface concept underlying put pricing
- [[variance-risk-premium]] — the VRP that makes put overlay expensive in high-DVOL windows
- [[fear-and-greed-index]] — the sentiment indicator used in Method C
- [[open-interest]] — OI/MC signal used in Method B
- [[funding-rate]] — funding signal used in Method A
- [[perpetual-futures]] — the perp instrument for the long leg
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — put cost drag, DTE mismatch, early entry
- [[when-to-retire-a-strategy]] — kill vs pause framework
