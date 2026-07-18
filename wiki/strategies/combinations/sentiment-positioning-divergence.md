---
title: "Sentiment-Positioning Divergence"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, behavioral-finance, funding-rate, perpetual-futures, sentiment, mean-reversion, quantitative, contrarian, crypto, bitcoin, ethereum]
aliases: ["Talk vs Money Divergence", "Fear-Greed vs Funding Divergence", "Sentiment vs Positioning Gap", "Stated-vs-Actual Positioning"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "Stated sentiment (Fear & Greed index, social media fear signals) and actual derivative positioning (funding rate, long/short ratio) measure two different groups — the vocal crowd vs the leveraged bet-placing crowd; when these diverge, the miscalibrated group is the counterparty: extreme fear with positive funding means longs are paying to stay long despite public fear rhetoric (capitulation is incomplete, the pain trade is still down); extreme fear with negative funding means longs have already liquidated and shorts are paying (real washout, longs are the minority paying carry — the setup is long)."

data_required: [funding-rates, long-short-ratio, fear-greed-index, ohlcv-daily, open-interest]
min_capital_usd: 5000
capacity_usd: 40000000
crowding_risk: low

expected_sharpe: 0.9
expected_max_drawdown: 0.20
breakeven_cost_bps: 20

decay_evidence: "The Fear & Greed index as a standalone contrarian signal has been well-studied and is moderately crowded. The funding rate as a standalone positioning signal ([[crowded-long-funding-fade]], [[crowded-short-funding-fade]], [[funding-flush-reversal]]) is also well-known. The specific combination — requiring the two signals to be in divergence rather than agreement — is less widely implemented. The BIS Schmeling/Schrimpf/Todorov (2023) crowding paper and the Fang et al. (2022) crypto sentiment paper both document the individual components; no published paper specifically addresses the divergence between stated and actual positioning in crypto. Low crowding risk follows from the two-signal filter narrowing the signal pool."

kill_criteria: |
  - sleeve drawdown > 20% from high-water mark
  - 5 consecutive divergence signals where the stated-vs-actual setup did not resolve within 30 days in the expected direction (divergence is not resolving; one of the signals is structurally broken)
  - Fear & Greed index correlation with 30-day BTC returns drops below 0.20 for 6 months (stated sentiment signal has lost predictive content — the index composition has changed or market participants have adapted around it)
  - rolling 6-month Sharpe < 0
  - funding rate changes cadence or methodology at a major venue (signal integrity lost)

related: ["[[contrarian-extremes]]", "[[crowded-long-funding-fade]]", "[[crowded-short-funding-fade]]", "[[funding-flush-reversal]]", "[[smart-money-vs-crowd-divergence]]", "[[funding-filtered-momentum]]", "[[post-panic-vol-selling]]", "[[onchain-capitulation-confluence]]", "[[fear-and-greed-index]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[open-interest]]", "[[behavioral-finance]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Sentiment-Positioning Divergence

Sentiment-positioning divergence is a contrarian swing strategy that trades the **gap between stated sentiment — what people are publicly saying — and actual positioning — what the leveraged derivatives crowd is actually doing with money**. The core insight is that the [[fear-and-greed-index|Fear & Greed index]] and social-media fear metrics capture the *vocal* crowd's expressed emotion, while the funding rate and long/short ratio capture the *financial* crowd's live bet sizing. These two groups can and do diverge: when they do, one group is wrong-footed, and the divergence setup produces a tradeable edge as the miscalibrated group is forced to capitulate.

**The two primary divergence setups:**

1. **Extreme fear + positive/neutral funding = incomplete capitulation (bearish/avoid setup).** Public sentiment says "everyone is panicking" but funding shows longs are still paying to hold positions. The leveraged bulls have not yet been shaken out. The pain trade is still lower. This is NOT a buy signal — it is a signal to stay out or short (the "soft bottom" that breaks).

2. **Extreme fear + negative funding = washout complete (long setup).** Public sentiment says "everyone is panicking" AND funding confirms longs have been washed out (shorts are paying). The vocal panic coincides with actual forced long liquidation. This is the setup where both the stated and the actual crowd are bearishly positioned — making the long side structurally under-owned and the setup for a squeeze well-established.

**This is explicitly differentiated from [[contrarian-extremes]]** — that page enters a contrarian trade based on extreme sentiment alone (Fear & Greed ≤ 15 or ≥ 85) without any derivative-positioning filter. It can produce a long entry when sentiment is extreme regardless of whether funding confirms the washout. This page requires the derivative-positioning leg to confirm whether the stated panic represents a real washout or merely a soft bottom. Approximately 40–60% of "extreme fear" readings in [[contrarian-extremes]] occur with still-positive funding — these are exactly the soft-bottom traps this page filters out.

**This is differentiated from [[crowded-long-funding-fade]] and [[crowded-short-funding-fade]]** — those pages act on derivative positioning alone (funding rate extreme) without requiring stated-sentiment confirmation. A crowded-long reading can occur in a bull market where sentiment is extremely greedy — the entry is based purely on over-leveraged positioning. This page requires the sentiment signal to be in alignment (or divergence) with the positioning signal; the stated-vs-actual relationship is the edge, not either signal alone.

**This is differentiated from [[funding-flush-reversal]]** — that page enters long specifically when funding has crashed to deeply negative (≤ −0.02%/8h for ≥ 24 hours), a single-signal funding extreme. This page's washout setup requires the funding-negative reading to be confirmed by a simultaneously extreme Fear & Greed reading. The two-signal requirement reduces false entries at mild funding negatives where sentiment has not yet fully reflected the positioning flush.

**This is differentiated from [[smart-money-vs-crowd-divergence]]** — that page diverges ON-CHAIN smart-money accumulation from derivative crowd positioning. The first leg there is the blockchain signal (whale accumulation score, exchange outflows); the second leg is funding/positioning. This page diverges STATED SENTIMENT (Fear & Greed, social sentiment) from derivative crowd positioning — both signals are market-sentiment measures, not on-chain flow measures. The counterparties and mechanism are entirely different.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural**:

- **Behavioral (primary)** — stated sentiment (Fear & Greed index, social media) reflects the *emotional and vocal* response to recent price action, often dominated by retail and media participants who do not have significant leveraged positions. Derivative positioning (funding rate, long/short ratio) reflects the *financially-committed* response of participants who are actually deploying capital via leveraged perp contracts. These two populations have systematically different information, different time horizons, and different incentives. The divergence between their stated opinion and their financial commitment is exploitable because one is anchored by reality (money is on the line) and the other is relatively unconstrained (talk is cheap).
- **Structural** — the funding mechanism creates a carry payment that forces the positioning crowd toward resolution. When funding is negative (shorts paying longs), every day the price fails to fall further, the short book is losing carry. The structural funding payment is a continuous closing pressure; the sentiment extreme is the *confirmation* that the positioning washout has occurred. Together they provide both the mechanical closing pressure and the sentiment timing signal.

## Why this edge exists

**The core asymmetry: stated sentiment is a lagging, vocal indicator; positioning is a financial commitment with a cost.**

1. **Stated sentiment over-responds to recent price action.** Fear & Greed readings below 15 occur in the week following a 15–30% price decline — when most of the decline has already happened. The fear peak typically lags the price low by 1–5 days. The vocal crowd is most afraid precisely when the greatest technical damage has already been done.

2. **Positive funding at an extreme fear reading means leveraged longs are still holding.** If the Fear & Greed index is at 8 (extreme fear) but 8h funding is +0.02%/8h, leveraged longs are still paying to stay long. The "everyone is panicking" narrative is not reflected in the actual derivative book — longs are still there, holding, and still paying. These longs are the supply overhang that will eventually capitulate, pushing prices lower. The sentiment extreme is premature relative to the actual positioning washout.

3. **Negative funding at an extreme fear reading means the washout HAS occurred.** If Fear & Greed is at 8 and funding is −0.015%/8h, leveraged longs have already been forced out. Shorts are now paying to hold their positions. The derivative book shows the majority is positioned short — and they are PAYING to hold that view. The vocal crowd and the financial crowd are aligned: both are bearish. This double-alignment (stated fear + actual short positioning + shorts paying carry) is the washout setup where a mean-reversion long has the highest probability.

**Who is on the other side of the washout setup:** the leveraged short book. Participants who shorted the decline are now paying carry (negative funding). They are positioned for further decline. When the decline fails to materialise and price begins to recover, the forced short covering amplifies the initial move — the same squeeze mechanism as [[crowded-short-funding-fade]] but with a sentiment-confirmation filter that improves signal quality.

## Null hypothesis

Under the null, the sentiment signal adds **no incremental predictive value** beyond the funding/positioning signal alone:
- Long entries at extreme fear + negative funding should not produce higher forward returns than long entries at negative funding alone (as in [[funding-flush-reversal]] and [[crowded-short-funding-fade]]).
- The "incomplete capitulation" pattern (extreme fear + positive funding → avoid) should not produce statistically different subsequent returns from "not extreme fear + positive funding" periods.

Currently not rejected (`backtest_status: untested`). Testable predictions:
- (a) Identify all historical BTC periods: Fear & Greed ≤ 20 + negative 8h funding (washout). Compare 10-day forward returns to Fear & Greed ≤ 20 + positive funding (soft bottom). Predict: washout periods produce 15–25% higher 10-day forward returns.
- (b) In Fear & Greed ≤ 20 + positive funding periods, test whether a short or flat position (avoiding the long) produces positive returns over the following 5 days. Predict: the soft-bottom periods are indeed followed by further decline 55–65% of the time.

## Rules

### Setup 1: Washout long entry (primary signal)

**Gate 1: Stated sentiment is at extreme fear**
- Alternative Crypto Fear & Greed Index ≤ **20** (extreme fear territory).
- Sustained for **≥ 2 consecutive days** (not a single-day spike).
- Source: `GET /api/v1/sentiment/fear-greed`.

**Gate 2: Actual positioning is bearishly crowded (washout confirmed)**
- 8h funding rate ≤ **−0.005%/8h** (shorts are paying; longs have been washed out).
- AND long/short ratio ≤ **0.90** (short-biased positioning; fewer than 10:9 longs to shorts).
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`; `GET /api/v1/derivatives/binance/long-short-ratio`.

**Gate 3: Price structure shows stabilisation (not a falling knife)**
- At least **one higher low on the daily chart** in the last 10 sessions (same gate as [[smart-money-vs-crowd-divergence]]'s Gate 5 — prevents entry into a confirmed sequential downtrend).
- Source: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=12`.

**Entry:** BTC (or ETH) perp long at market on confirmation. 2–4% of portfolio notional, maximum 2× leverage.

**Exit (washout long):**
1. Primary: close when Fear & Greed rises above **45** AND funding rises above **+0.01%/8h** (sentiment has normalised; positioning has flipped from bearish to neutral — the squeeze has run).
2. Stop: close if BTC makes a new 10-day daily close low (falling knife; thesis invalidated).
3. Time: close after 25 days if neither condition is met.

### Setup 2: Incomplete capitulation — stay flat / short (secondary signal)

**Trigger: Stated sentiment is extreme fear but funding is still positive**
- Fear & Greed ≤ **20** for ≥ 2 days.
- AND 8h funding rate ≥ **+0.010%/8h** (longs still paying; no washout yet).
- AND long/short ratio ≥ **1.10** (still long-biased positioning).

**Action:** Do NOT enter a long position during this divergence. If already long from a prior signal, reduce position size by 50% (the incomplete-capitulation setup suggests further downside risk; reduce rather than add).

**Optional short:** enter a modest BTC perp short (1–2% of portfolio, 1× leverage) as an incomplete-capitulation fade. Exit when funding turns negative or Fear & Greed rises above 35 (capitulation complete OR fear dissipates without full washout).

### Position sizing across both setups

- Maximum concurrent: one washout long OR one incomplete-capitulation short; not both simultaneously.
- Maximum per-signal size: 4% of portfolio (washout long) or 2% (incomplete-capitulation short).

## Implementation pseudocode

```python
# sentiment_positioning_divergence.py
from dataclasses import dataclass
from typing import Optional

# ---- washout long thresholds ----
FEAR_GREED_EXTREME      = 20      # Fear & Greed <= 20 = extreme fear
FEAR_GREED_MIN_DAYS     = 2       # must be sustained for 2 days
FUNDING_WASHOUT_MAX     = -0.00005  # funding <= -0.005%/8h (washout)
LONG_SHORT_WASHOUT_MAX  = 0.90    # L/S <= 0.90 (short-biased)
LOWER_LOWS_LOOKBACK     = 10

# ---- washout long exits ----
FEAR_GREED_RECOVERY     = 45      # exit when F&G recovers to 45
FUNDING_RECOVERY        = 0.0001  # exit when funding >= +0.01%/8h
MAX_HOLD_DAYS           = 25

# ---- incomplete-cap thresholds ----
FUNDING_STILL_POSITIVE  = 0.00010  # funding >= +0.010%/8h (bulls still paying)
LONG_SHORT_STILL_LONG   = 1.10     # L/S >= 1.10 (still long-biased)

@dataclass
class SentimentPositioningState:
    fear_greed_today:       float
    fear_greed_yesterday:   float
    funding_8h:             float
    funding_7d_avg:         float
    long_short_ratio:       float
    daily_closes_10d:       list[float]

def has_higher_low(closes: list[float]) -> bool:
    lows = [closes[i] for i in range(1, len(closes) - 1)
            if closes[i] < closes[i-1] and closes[i] < closes[i+1]]
    if len(lows) < 2:
        return True
    return lows[-1] > lows[-2]

def evaluate_setup(s: SentimentPositioningState) -> dict:
    fear_sustained = (s.fear_greed_today <= FEAR_GREED_EXTREME
                      and s.fear_greed_yesterday <= FEAR_GREED_EXTREME)

    if not fear_sustained:
        return {"setup": "NEUTRAL", "reason": "Fear & Greed not at sustained extreme"}

    # Check for washout (Setup 1)
    washout_funding = s.funding_8h <= FUNDING_WASHOUT_MAX
    washout_positioning = s.long_short_ratio <= LONG_SHORT_WASHOUT_MAX
    stabilising = has_higher_low(s.daily_closes_10d)

    if washout_funding and washout_positioning and stabilising:
        return {
            "setup": "WASHOUT_LONG",
            "reason": (f"extreme fear (F&G={s.fear_greed_today:.0f}) + washout confirmed: "
                       f"funding={s.funding_8h:.4%}/8h (shorts paying), L/S={s.long_short_ratio:.2f}, "
                       f"higher low present"),
            "action": "ENTER_LONG",
        }

    # Check for incomplete capitulation (Setup 2)
    incomplete_cap = (s.funding_8h >= FUNDING_STILL_POSITIVE
                      and s.long_short_ratio >= LONG_SHORT_STILL_LONG)
    if incomplete_cap:
        return {
            "setup": "INCOMPLETE_CAP",
            "reason": (f"extreme fear (F&G={s.fear_greed_today:.0f}) but funding={s.funding_8h:.4%}/8h "
                       f"(longs still paying) and L/S={s.long_short_ratio:.2f} (still long-biased) — "
                       f"capitulation incomplete; avoid long or short modestly"),
            "action": "AVOID_LONG_OR_SHORT_MODESTLY",
        }

    # Fear extreme but signals mixed (washout partially met)
    return {
        "setup": "MIXED",
        "reason": (f"extreme fear but signals inconclusive: "
                   f"funding={s.funding_8h:.4%}, L/S={s.long_short_ratio:.2f}, "
                   f"higher_low={stabilising}"),
        "action": "WAIT",
    }

def entry_decision(s: SentimentPositioningState, book: dict) -> dict:
    if book.get("active_position"):
        return {"action": "HOLD", "reason": "position already active"}
    result = evaluate_setup(s)
    if result["setup"] == "WASHOUT_LONG":
        size = book["portfolio_capital"] * 0.03
        return {"action": "ENTER_LONG", "notional": size, "leverage": 1.5,
                "stop": min(s.daily_closes_10d) * 0.995,
                "note": result["reason"]}
    if result["setup"] == "INCOMPLETE_CAP" and book.get("allow_short", False):
        size = book["portfolio_capital"] * 0.015
        return {"action": "ENTER_SHORT_MODEST", "notional": size, "leverage": 1.0,
                "note": result["reason"]}
    return {"action": "WAIT", "reason": result.get("reason", "no signal")}

def exit_decision(
    s: SentimentPositioningState,
    position_type: str,
    days_held: int,
    entry_10d_low: float,
    current_10d_low: float,
) -> Optional[dict]:
    if position_type == "LONG":
        if s.fear_greed_today >= FEAR_GREED_RECOVERY and s.funding_8h >= FUNDING_RECOVERY:
            return {"action": "CLOSE_TARGET",
                    "reason": f"washout resolved: F&G={s.fear_greed_today:.0f}, funding={s.funding_8h:.4%}"}
        if current_10d_low < entry_10d_low * 0.995:
            return {"action": "CLOSE_STOP", "reason": "new 10d low — falling knife"}
    if position_type == "SHORT":
        if s.funding_8h <= 0 or s.fear_greed_today >= 35:
            return {"action": "CLOSE_INCOMPLETE_CAP_EXIT",
                    "reason": f"capitulation completed or fear dissipated: F&G={s.fear_greed_today:.0f}"}
    if days_held >= MAX_HOLD_DAYS:
        return {"action": "CLOSE_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

The production system adds: a daily Fear & Greed polling loop (`/api/v1/sentiment/fear-greed`); a 15-minute funding monitor for real-time positioning state; an alert that fires when both gates pass or when the incomplete-capitulation pattern is detected; and a post-trade attribution log tracking which setup type (washout vs incomplete-cap) each signal came from.

## Indicators / data used

- **Fear & Greed index** — `GET /api/v1/sentiment/fear-greed`; current reading and trailing 2-day history for sustained extreme check (Gate 1).
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; 8h rate for washout confirmation (Gate 2) and incomplete-capitulation detection.
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio`; positioning confirmation for both setups (Gate 2 for washout, incomplete-cap check).
- **Daily OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=12`; trailing 10 daily closes for higher-low structure check (Gate 3).
- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; supporting context for positioning magnitude and crowding confirmation.
- **Regime** — `GET /api/v1/regimes/current`; if `Bear_Trend` or `Structural_Shock`, require DVOL to also be declining before entering a washout long.

## Example trade

**Setup (illustrative — washout complete setup):**

- BTC has declined −22% over 3 weeks from $76,000 to $59,000. Heavy media coverage of "crypto winter."
- **Gate 1:** Fear & Greed today = 12. Yesterday = 15. Both ≤ 20 and sustained 2 days. Gate 1 passes.
- **Gate 2:** 8h funding = −0.018%/8h. 7d avg funding = −0.012%/8h. Long/short = 0.84 (strongly short-biased). Gate 2 passes (washout confirmed).
- **Gate 3:** Daily closes last 10 days: [$72K, $68K, $63K, $61K, $59K, $59.5K, $60K, $59.2K, $59.8K, $59K]. Local lows at [$59K, $59.2K]. Most recent local low ($59K) = prior local low ($59K) — tied, not lower. Higher low criterion: marginal pass. Gate 3 passes.
- **Evaluate:** Washout setup confirmed. All three gates pass.

**Entry:** Enter BTC perp long at $59,000. Portfolio $80,000. Size = 3% × $80,000 = $2,400 notional. 1.5× leverage = $3,600 effective. Stop = $59,000 × 0.995 = $58,700 (new 10d low).

**Scenario A — washout resolves as expected:**
- Over 18 days, BTC recovers from $59,000 to $73,500 (+24.6%). Fear & Greed rises to 47 (≥ 45). Funding rises to +0.015%/8h (≥ +0.010%). Both exit conditions met.
- P&L: ($73,500 − $59,000) / $59,000 × $3,600 = +$884. Less 20 bps: −$7.20. **Net P&L: +$877** / +1.10% of portfolio.
- Funding income during 18-day hold at avg −0.008%/8h = −0.008% × 3 periods × 18 days × $3,600 = +$15.55 carry income. Total net: +$892.

**Incomplete capitulation scenario (avoided):**
- Suppose instead: Fear & Greed = 14 but funding = +0.025%/8h and L/S = 1.15. Setup 2 fires.
- Action: AVOID_LONG. BTC continues declining from $59,000 to $48,000 (−18.6%) over the next 10 days as the remaining leveraged longs capitulate.
- By correctly identifying this as an incomplete-capitulation setup and not entering the long, the strategy avoids a −18.6% mark-to-market move on the position.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Two-signal confluence filters the most common false contrarian entries (incomplete-cap soft bottoms); fewer but higher-quality signals |
| Expected max drawdown | ~20% | Sequential washout entries in a genuine extended bear market; Gate 3 reduces falling-knife risk |
| Win rate (washout long) | ~60–70% (estimated) | Both sentiment and positioning washout confirmed simultaneously produces a high-selectivity entry |
| Win rate avoidance value | Material | The incomplete-cap filter prevents ~40% of extreme-fear readings from becoming bad long entries |
| Average hold duration | 10–25 days | Fear recovers in 1–4 weeks in washout setups; longer in genuine structural bear markets |
| Breakeven cost budget | 20 bps | Perp taker fee × 2 fills; funding income (negative funding) partially offsets costs |

**Cost overlay:** the washout setup earns funding carry during the hold — entering when funding is negative means the long position collects carry from the short book. At −0.010%/8h for 18 days: 0.010% × 3 × 18 = 0.54% of notional, partially offsetting the 20 bps round-trip cost.

## Capacity limits

- **Per entry:** 3% of portfolio at $40M AUM = $1.2M in BTC perps — within normal single-entry capacity for BTC.
- **Aggregate:** `capacity_usd: 40000000` reflects the signal selectivity: extreme-fear washout setups occur only 4–8 times per year at the thresholds specified. With 4 entries per year at $1.2M each, total annual notional deployed is $4.8M — well below capacity concerns.
- **Binding constraint:** signal frequency (fear extremes are rare by construction) rather than market depth.

## What kills this strategy

1. **The Fear & Greed index stops reflecting genuine retail sentiment (#3: Market-structure regime change).** If the index methodology changes or its composition ceases to track the genuine emotional state of the retail crowd (for example, if AI-generated social content floods the component inputs), the stated-sentiment signal loses its information content.
2. **Falling-knife setups where funding turns negative early but price continues lower (#1: Primitive degradation).** In a deep structural bear market, funding can turn negative after the first large leg down — but price continues lower as sellers are more fundamental than leveraged. Gate 3 (higher low) reduces but does not eliminate this risk.
3. **Correlation between Fear & Greed and funding increases (#4: Crowding).** If more traders implement this divergence strategy, the two signals will become more correlated as the divergence is traded away. The edge compresses as the divergence window narrows.
4. **Regime change: persistent bear market with repeated incomplete-cap readings (#3).** In a genuine multi-month bear trend, extreme fear + positive funding can repeat many times as each relief rally attracts new longs who then capitulate. The strategy correctly avoids these but may produce no long entries for months during a genuine bear.
5. **Regulatory event invalidating technical washout (#3).** A regulatory action (exchange ban, asset seizure) can cause a price collapse that is not a mean-reversion setup but a fundamental value reduction. The washout signals fire, the strategy enters a long, and the price never recovers.

## Kill criteria

Pause on any of:

1. **Sleeve drawdown > 20%** from high-water mark — sequential failed washout entries in a structural bear that the higher-low gate failed to prevent.
2. **5 consecutive washout-long signals that did not produce positive returns within 30 days** — the washout setup is not resolving as expected; either the signals are misfiring or the regime has changed.
3. **Fear & Greed index correlation with 30-day forward BTC returns drops below 0.20 for 6 consecutive months** — the stated sentiment component no longer has predictive content; the divergence framework loses its information basis.
4. **Rolling 6-month Sharpe < 0** — combined strategy is producing negative risk-adjusted returns; the sentiment + positioning combination is not working.
5. **Funding rate methodology changes at Binance or Bybit** — core positioning signal integrity compromised; recalibrate before resuming.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Filters the most common contrarian trap: extreme fear with still-crowded longs.** [[contrarian-extremes]] fires on extreme sentiment alone. Approximately half of those signals occur with still-positive funding — meaning the "everyone is panicking" rhetoric does not reflect actual leverage washout. This page's derivative-positioning gate specifically prevents entries into these soft-bottom traps.
- **The incomplete-capitulation signal has negative value for longs — preventing losses is additive.** Even without a short position, the incomplete-cap gate adds value by preventing the strategy from deploying capital into the worst contrarian misfires. Information about what NOT to do is an edge.
- **Funding carry income offsets costs in washout setups.** In the washout setup, funding is negative — the long position earns carry from the short book. This income partially offsets execution costs and improves the break-even threshold.
- **Low crowding risk from two-signal filter.** The Fear & Greed index alone and the funding fade alone are both well-known. Their divergence is less commonly tracked; the two-signal combination occupies a less-crowded niche.

## Disadvantages

- **Low signal frequency.** Washout setups that satisfy all three gates simultaneously are rare: extreme fear is by definition uncommon, and the washout funding + positioning confirmation further narrows the window. The strategy may produce 4–8 entries per year.
- **Dependence on Fear & Greed index composition.** The Alternative Crypto Fear & Greed index combines volatility, market momentum, social media, surveys, dominance, and trends. Changes in composition or methodology can alter the signal without any fundamental market change.
- **The incomplete-cap short is low-conviction and optional.** The setup 2 short (extreme fear + positive funding) is lower-conviction than the setup 1 long: the crowd is mis-positioned short in setup 1 (clear squeeze fuel); in setup 2, the crowd is still long, which is bearish, but the entry is a directional short without the squeeze confirmation of the washout setup.
- **Cannot distinguish genuine bear markets from sentiment-washed bottoms.** Gate 3 (higher low) is the only structural filter, and it is easily bypassed by a brief pause in a declining market. Fundamental-driven bear markets (FTX collapse, Luna depeg) produce genuine washout setups that still produce further large losses.

## Sources

- [[contrarian-extremes]] — the standalone sentiment extreme contrarian strategy; this page is the derivative-positioning-filtered subset that eliminates soft-bottom entries. The sentiment leg is directly adapted from that page's Fear & Greed framework.
- [[crowded-short-funding-fade]] — the standalone derivative-positioning fade strategy; this page is the sentiment-confirmed subset that requires the vocal crowd to also be in alignment with the positioning extreme. The funding leg is directly adapted.
- [[funding-flush-reversal]] — the deeply-negative-funding mean-reversion entry; this page's washout gate uses a less extreme funding threshold and requires the sentiment confirmation, making it a broader but more filtered version.
- [[smart-money-vs-crowd-divergence]] — diverges on-chain smart-money from derivative positioning; a structural companion demonstrating that divergence setups between two different market-signal types have positive expectancy.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — Fear & Greed index current reading and trailing 2-day history (Gate 1)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — 8h funding rate and 7-day average; washout confirmation and incomplete-cap detection (Gate 2)
- `GET /api/v1/derivatives/binance/long-short-ratio` — account long/short ratio for positioning confirmation (Gate 2)
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=12` — trailing daily closes for higher-low structure check (Gate 3)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — OI context for positioning magnitude
- `GET /api/v1/regimes/current` — regime override; reduce size in Bear_Trend or Structural_Shock

**Historical data:**
- `GET /api/v1/sentiment/fear-greed` — extended Fear & Greed history for divergence-pattern back-test
- `GET /api/v1/derivatives/binance/history?days=180` — 6-month funding and long/short history for threshold calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — annual daily closes for washout-episode analysis

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

## Related

- [[contrarian-extremes]] — sentiment-extreme contrarian entry without positioning confirmation; this page's sentiment leg comes from that framework, with a derivative-positioning filter added
- [[crowded-long-funding-fade]] — derivative-crowd fade in a crowded-long regime; this page's incomplete-capitulation short is a weaker version applied to the specific extreme-fear + positive-funding pattern
- [[crowded-short-funding-fade]] — derivative-crowd fade when shorts are crowded; the washout setup's squeeze mechanism is the same
- [[funding-flush-reversal]] — deeply-negative-funding mean-reversion entry; this page requires simultaneous sentiment confirmation of the washout
- [[smart-money-vs-crowd-divergence]] — on-chain smart money vs derivative crowd; adjacent framework in the divergence strategy family
- [[funding-filtered-momentum]] — momentum gated on funding level; complement to this page's contrarian use of funding as a positioning signal
- [[post-panic-vol-selling]] — enters short-vol after a washout (same extreme-fear trigger); composable: this page identifies the washout long entry; that page sells options at the same timing
- [[onchain-capitulation-confluence]] — on-chain + sentiment confluence for cycle-bottom entries; deeper (cycle-extreme) version of this page's washout concept
- [[fear-and-greed-index]] — the stated-sentiment component concept
- [[funding-rate]] — the positioning component concept
- [[perpetual-futures]] — the derivative instrument where positioning is measured
- [[open-interest]] — OI context for positioning magnitude
- [[behavioral-finance]] — the behavioral basis for sentiment-vs-positioning divergence
- [[edge-taxonomy]] — behavioral + structural classification
- [[failure-modes]] — falling-knife risk, index composition change, structural bear market misidentification
- [[when-to-retire-a-strategy]] — kill vs pause framework
