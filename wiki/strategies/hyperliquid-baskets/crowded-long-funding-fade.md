---
title: "Crowded-Long Funding Fade (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, funding-rate, mean-reversion, behavioral-finance, market-microstructure, derivatives]
aliases: ["Long Squeeze Funding Play", "Positive Funding Short", "Crowded Long Fade", "Funding Rate Short Bias"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[basis-carry-regime]]", "[[crowded-short-funding-fade]]", "[[funding-rate-harvest]]", "[[long-liquidation-cascade]]", "[[post-liquidation-rebound]]", "[[liquidation-cascade-fade]]", "[[funding-rate-arbitrage]]", "[[funding-rate]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-liquidation-engine]]", "[[open-interest]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[coinglass]]", "[[hypurrscan]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: pilot
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Retail and momentum traders pile into long positions during bull runs; crowded longs paying positive funding signals an overcrowded trade — going short collects the funding carry and positions for mean-reversion or a long squeeze when sentiment reverses."
data_required: [perp-funding, open-interest, liquidation-feed, order-book-depth, funding-rate-history]
min_capital_usd: 5000
capacity_usd: 15000000
crowding_risk: medium
expected_sharpe: 0.85
expected_max_drawdown: 0.25
breakeven_cost_bps: 35
kill_criteria: |
  - Rolling 3-month Sharpe < 0 after minimum 15 trades
  - Three consecutive full stop-outs (each > 8% drawdown on position)
  - Funding never reaches the +0.05%/h entry threshold for 60 consecutive days
  - Drawdown > 22% on this basket over rolling 6 months
---

# Crowded-Long Funding Fade (Hyperliquid Basket)

When crypto assets rally sharply, retail and momentum traders pile into long perpetual positions expecting further upside. As the long book swells, [[funding-rate|funding]] turns significantly positive — meaning **longs are paying shorts** — signalling an overcrowded trade. This basket goes **short** into that positivity: it collects the funding payment, positions for mean-reversion as the crowded long trade exhausts itself, and exits when funding normalises or the correction completes. The edge is both a carry trade (earn funding while waiting) and a behavioural fade (crowded longs historically resolve against the crowd at extremes).

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

> **Live status (2026-06-16 dashboard snapshot):** 2 open signals detected (conditions exist and entry criteria are met or close to met), but **$0 deployed** — full entry criteria have not yet been satisfied. Monitoring in standby.

---

## Edge Source

**Behavioral** + **structural** + **risk-bearing** (see [[edge-taxonomy]]).

- **Behavioral (primary).** Retail traders extrapolate recent price gains, establishing longs near local highs and paying the highest funding rates. The crowded long reverses when price fails to continue — every long is also a latent seller (closing), and forced stop-outs cascade into covering pressure. Positive funding is a quantified measure of how far the consensus long has extended.
- **Structural (secondary).** [[hyperliquid|Hyperliquid]]'s [[hyperliquid-funding-rate-microstructure|hourly funding settlement]] means overcrowding is flagged within hours of onset, not days. At +0.05%/h (+43% APY annualised), longs are paying 0.05% every hour to maintain their positions — a compounding cost that mechanically erodes the long book even without a price catalyst.
- **Risk-bearing (tertiary).** Shorting into a rallying market requires absorbing mark-to-market pain if the rally continues. The funding payment is the risk premium for bearing that exposure.

---

## Why This Edge Exists

**Positive funding = longs pay shorts.** When funding is significantly positive, the crowd is long, and those longs are bleeding carry every hour. This creates compounding pressure on the crowded trade:

1. **Carry cost erodes long P&L** even if price is flat, making longs increasingly unwilling to hold without further price appreciation.
2. **Any price stabilisation or reversal accelerates unwinding** — longs close to protect profits, reducing the bid, which closes more longs below them.
3. **Self-reinforcing correction:** unwinding longs sell the perp, lowering mark price, triggering further longs to close at marginal profits or cuts, pulling more stops.

**Who is on the other side?** The momentum long-buyer who entered after a price rally and is now paying 40–100% APY in funding to hold the position, expecting continued appreciation. Historically this cohort is wrong at extremes: they entered late, they pay to hold, and their closing flow (selling) drives the correction when sentiment peaks. (Source: [[hyperliquid-funding-rate-microstructure]])

The Hyperliquid `predictedFundings` API surfaces the in-flight TWAP roughly 30 minutes before each hourly settlement — allowing early entry ahead of the print and precise timing of the carry start.

---

## Null Hypothesis

Under "no edge," strongly positive funding is simply fair compensation for long-side carry risk in a genuine bull market: the expected continuation payoff for longs exceeds the funding cost, and shorts fading them would lose more on mark-to-market than they collect in funding.

**Disconfirming evidence to monitor:**
- Win rate on completed trades falls below 52% over a trailing 30-trade window.
- Average holding period consistently reaches the time stop (4 days) — price is trending against the fade, not reverting.
- [[open-interest]] continues to *increase* after entry — new longs are entering faster than the current book is closing, crowd is growing.
- Strong macro context justifies the bull move: sustained inflow data ([[spot-etf-flows]], [[on-chain-regime]] signals), genuine fundamental catalyst, or central bank accommodation that would rationally sustain elevated funding.

---

## Rules

**Universe.** Same as [[crowded-short-funding-fade]]: Hyperliquid perp markets with:
- Daily volume > $20M
- Open interest > $10M
- Hedgeable via spot or equivalent CEX perp

Priority: BTC, ETH, SOL (most liquid, lowest squeeze risk on the short side). Mid-caps with caution; thin or memecoin perps excluded from this basket — a thin crowded long on a memecoin can squeeze to extreme levels (see JELLY, [[2025-03-jellyjelly-hlp-attack]]). This basket targets **crowded longs on majors and liquid mid-caps only**.

**Entry signal:**
1. Hourly funding rate > +0.05%/h (+43% APY annualised) on the target pair — sustained for at least 2 consecutive hours.
2. Open interest ≥ 1.3× the 30-day rolling mean (confirms long book is abnormally elevated, not just baseline bullishness).
3. Price is within 5% of a notable [[resistance]] level or has extended > 15% from its 20-day moving average without a meaningful pullback (overbought condition).
4. No confirmed major bullish catalyst expected in next 24 hours (protocol upgrade, ETF approval, central bank pivot) that could sustain elevated longs rationally.

**Entry execution:** Market short on the perp, **isolated margin**, 2–3× leverage maximum. On Hyperliquid, the JELLY incident (March 2025) demonstrated that *even large-cap pairs* can see governance-level short-squeeze interventions if the HLP is adversely exposed. Isolated margin is non-negotiable.

**Exit — take profit:**
- Funding normalises below +0.01%/h — close 50% of position (crowding has reversed).
- Price drops 8–12% from entry (short has profited from the correction) — close remaining 50%.
- Open interest falls back to the 30-day mean (long book has unwound) — close all.

**Exit — stop:**
- Hard stop at −8% from entry on the position.
- Time stop: 4 calendar days. A crowded long that does not correct in 4 days may reflect a genuine bull regime, not just overcrowding — exit and reassess.

**Sizing:** 3–6% of basket equity per trade. Max 2 concurrent short positions. Reduce to 2% sizing if aggregate Hyperliquid funding is strongly positive across > 5 major pairs — systemic bull regime risk increases the chance of simultaneous adverse moves and a squeeze event. In systemic bull markets this basket may simply stay inactive.

---

## Implementation Pseudocode

```python
# Crowded-Long Funding Fade — basket module
# Regime: derivatives-native-regime + basis-carry-regime
# LIVE: 2 signals detected 2026-06-16; $0 deployed (pre-entry conditions partial)

FUNDING_ENTRY_THRESHOLD = 0.0005    # +0.05%/h = +43% APY annualised
OI_RELATIVE_MIN        = 1.30       # OI >= 130% of 30-day mean
RESISTANCE_PROXIMITY   = 0.05       # within 5% of resistance / 15% above 20d MA
FUNDING_EXIT           = 0.0001     # +0.01%/h — crowding cleared
MAX_POSITION_DAYS      = 4
STOP_LOSS_PCT          = 0.08
LEVERAGE               = 2.5
POSITION_SIZE_PCT      = 0.05

def evaluate_crowded_long_fade(pair, state, equity):
    funding_now  = get_hourly_funding(pair)
    funding_prev = get_hourly_funding(pair, lag=1)
    oi_now       = get_open_interest(pair)
    oi_30d_mean  = rolling_mean(get_oi_history(pair), days=30)
    resistance   = get_nearest_resistance(pair)
    price        = get_mark_price(pair)
    ma20         = get_moving_average(pair, days=20)
    extended     = (price - ma20) / ma20 >= 0.15    # >15% above 20d MA

    # Squeeze risk guard — skip thin/memecoin pairs entirely
    if get_daily_volume(pair) < MIN_LIQUIDITY or is_memecoin(pair):
        return  # avoid JELLY-class squeeze

    crowded_long = (
        funding_now > FUNDING_ENTRY_THRESHOLD and
        funding_prev > FUNDING_ENTRY_THRESHOLD and
        oi_now >= OI_RELATIVE_MIN * oi_30d_mean and
        (abs(price - resistance) / price <= RESISTANCE_PROXIMITY or extended) and
        not state.macro_bullish_catalyst_next_24h
    )

    if crowded_long and not state.has_position(pair):
        notional = equity * POSITION_SIZE_PCT * LEVERAGE
        entry_px = price
        stop_px  = entry_px * (1 + STOP_LOSS_PCT)   # stop above entry for short
        baseline_px = state.price_when_funding_first_crossed(
            pair, FUNDING_ENTRY_THRESHOLD
        )
        # Target: revert to pre-crowding-onset baseline
        target_px = baseline_px * 0.92               # ~8% correction from baseline
        state.open_short(pair, notional, entry_px, stop_px,
                         target_px=target_px,
                         deadline_days=MAX_POSITION_DAYS)
        state.tag_position(pair, reason="crowded-long-fade",
                           signals=["2 detected 2026-06-16"])

    if state.has_position(pair):
        pos  = state.get_position(pair)
        funding_now = get_hourly_funding(pair)
        price = get_mark_price(pair)

        if funding_now <= FUNDING_EXIT and not pos.half_closed:
            state.close_partial(pair, fraction=0.5, tag="funding-normalised")
        if price <= pos.target_px:
            state.close_all(pair, tag="price-target")
        if get_open_interest(pair) <= oi_30d_mean and not pos.half_closed:
            state.close_all(pair, tag="oi-unwind")
        if price >= pos.stop_px:
            state.close_all(pair, tag="stop-loss")
        if state.days_held(pair) >= MAX_POSITION_DAYS:
            state.close_all(pair, tag="time-stop")
```

---

## Indicators / Data Used

- **[[funding-rate|Funding rate]] (hourly)** — primary signal; longs paying > 0.05%/h confirms crowding. Source: Hyperliquid `predictedFundings` API, [[coinglass]], [[hypurrscan]].
- **[[open-interest]]** — confirms long book is abnormally elevated. Source: [[coinglass]], native HL API.
- **[[resistance]] levels / moving average extension** — identifies overbought zones where the correction is most likely to originate.
- **[[liquidation]] heatmaps** — long liquidation clusters *below* price indicate where mechanical selling accelerates on a correction. Source: [[coinglass]] heatmap.
- **Volume profile / [[vwap]]** — high-volume node analysis to identify likely mean-reversion targets.
- **[[spot-etf-flows]]** — bullish macro context check; sustained ETF inflows reduce the probability that high funding is simple overcrowding vs justified bull market.

---

## Example Trade

**Illustrative only — not a backtest.**

Scenario: Q1 2026, ETH/USDC-PERP on Hyperliquid. ETH rallies 25% in 10 days following a DeFi narrative. Funding reaches +0.08%/h (+70% APY annualised). OI is 160% of the 30-day mean. Price is 4% below a major prior ATH resistance.

| Step | Detail |
|---|---|
| **Entry** | Short ETH perp @ $3,200, 2.5× leverage, isolated margin |
| **Funding collected** | +0.08%/h × 2.5× leverage × 40h hold = 8.0% on position notional |
| **Correction trigger** | OI plateaus at h+20; price begins stalling h+25 |
| **Partial exit (50%)** | Funding drops to +0.008%/h at h+38 @ $2,976 (−7.0%) |
| **Full exit (50%)** | Price reaches 8% correction at $2,944 at h+52 |
| **Net position P&L** | ~+7.5% blended on notional, plus 8.0% funding carry |

*Illustrative, not a backtest. Costs (taker × 2 ≈ 9 bps) not included. Not investment advice — this page documents the basket setup.*

---

## Performance Characteristics

Estimates are illustrative. A pilot track record is beginning to accumulate as of June 2026 (2 signals in observation, $0 deployed).

- **Return shape:** positive carry while waiting, then a moderate directional payoff from correction. Win rate expected 55–63% — slightly lower than the crowded-short variant because bull markets can persist longer than bear squeezes.
- **Expected Sharpe:** ~0.85 net in a derivatives-native or basis-carry regime. Degrades in sustained bull regimes where high funding is rational.
- **Realistic cost overlay:** ~20–30 bps round trip (2 × taker + slippage). Funding carry at +0.05%/h covers ~2.5 days of holding costs at these fees.
- **Drawdown profile:** largest losses occur during genuine bull regime continuation — if the rally extends significantly after entry before correcting, the stop is hit at −8%. Multiple simultaneous stops (correlated bull move across majors) is the tail risk.
- **Asymmetry vs [[crowded-short-funding-fade]]:** short-side fades carry more squeeze risk (particularly on thin pairs) and lower win rates due to bull-regime persistence. This basket is intentionally more conservative in pair selection.

---

## Capacity Limits

Bounded by Hyperliquid short-side liquidity and the squeeze risk premium. On BTC/ETH: comfortable up to $5–8M per trade. On SOL/mid-caps: $1–2M. Aggregate basket capacity **$15M** — larger positions on the short side meaningfully increase squeeze risk and can move the funding signal itself (a very large short reduces the net long book, lowering funding). Do not run this basket at scale simultaneously with [[funding-rate-harvest]] (which may run short positions on the same pairs).

---

## What Kills This Strategy

See [[failure-modes]]:

1. **Bull regime misclassification.** The primary failure mode: positive funding in a genuine bull market (strong macro, ETF inflows, fundamental catalyst) is rational, not overcrowded. Fading it means shorting into a justified uptrend. Mitigation: macro context filter and the 4-day time stop.
2. **Short squeeze on thin or narrative-driven pairs.** Even liquid pairs can see sharp squeeze moves if a narrative catalyst fires (see [[2025-03-jellyjelly-hlp-attack]]). The basket restricts to majors + liquid mid-caps, but this risk is never zero. Isolated margin and the −8% stop are the primary mitigation.
3. **Sustained high funding without correction.** In strong bull regimes, funding can remain elevated for weeks as new retail capital continues entering. The time stop prevents indefinite capital lockup but guarantees a loss on such trades.
4. **ADL.** A profitable short position during a cascade event may be force-closed by Hyperliquid's auto-deleveraging mechanism. See [[hyperliquid-liquidation-engine]].
5. **Crowding of the fade strategy itself.** If this basket becomes widely replicated, the short-side pressure compresses funding faster than the price correction occurs — the carry is captured quickly but the directional leg produces little additional return.

---

## Kill Criteria

Per [[when-to-retire-a-strategy]]:

- **Rolling 3-month Sharpe < 0** after a minimum of 15 completed trades.
- **Three consecutive full stop-outs** (> 8% loss each) — entry filter is failing to distinguish crowding from genuine bull trend.
- **Entry threshold never reached** for 60 consecutive days — market is in a low-leverage, low-funding regime. Pause basket.
- **Drawdown > 22%** on this basket over rolling 6 months.

---

## Advantages

- **Positive carry while waiting** — at +0.05%/h, the short collects the funding even if price stays flat.
- **Hard, API-readable signal** — funding rate is not a subjective crowding indicator; it is a real-time, quantified ledger entry.
- **Hourly cadence** — Hyperliquid's settlement granularity means crowding signals resolve faster than on CEXs.
- **Natural portfolio hedge** — tends to fire in bull markets, when trend-following and long-momentum strategies are most profitable, providing an offset.
- **Conservative pair selection** — restricting to high-liquidity perps substantially reduces squeeze tail risk vs a similar strategy running on memecoins.

---

## Disadvantages

- **Lower win rate than crowded-short fade** — bull markets trend more persistently than bear moves in crypto; the crowd can be right for longer.
- **Squeeze risk is real** — even major pairs experience short squeezes; the JELLY incident is a reminder that governance-level intervention can occur.
- **Systemic bull risk** — multiple pairs can simultaneously have elevated funding in a genuine bull market; running concurrent short positions amplifies drawdown during a coordinated rally.
- **Carry advantage erodes in low-funding regimes** — if the market shifts to a low-leverage, low-funding environment, this basket may generate few entry signals and sits idle.
- **Venue dependency** — single-venue (Hyperliquid) execution; oracle risk, ADL, and chain outage all threaten open positions.

---

## Hyperliquid Execution Notes

**Funding direction precision:** **Positive funding = longs pay shorts.** At +0.05%/h, a long position on $100,000 notional pays $50 *per hour* to the opposing short. This basket is the short receiver of that payment. Confirm via the `fundingHistory` API: positive `fundingRate` values indicate longs are paying. Note: Hyperliquid displays funding from the *long* perspective — a positive rate is paid *by* the long *to* the short.

**Isolated margin is mandatory** — this is a short position and a short squeeze can move exponentially faster than a long squeeze. Cross-margin exposure could drain the full account on a squeeze event.

**JELLY precedent — asymmetric risk on the short side.** The [[2025-03-jellyjelly-hlp-attack]] demonstrated that Hyperliquid's HLP vault can become adversely exposed when large short positions are squeezed, potentially triggering governance delists or force-settlements. For this basket (which is *short*), the risk is that a squeeze forces buybacks at far above market price before the stop can fire. Mitigation: majors-only universe, low leverage, isolated margin.

**Liquidation single-tick risk.** Hyperliquid can liquidate a position on a single mark-price tick. At 2.5× leverage, the mark-to-maintenance margin buffer is ~16% — which should survive most intraday volatility events, but not a JELLY-class 400% spike on a thin pair. Universe filter (liquid pairs only) is the primary guard.

**Sibling baskets:** [[crowded-short-funding-fade]] (the mirror long basket), [[funding-rate-harvest]] (delta-neutral carry without the directional fade), [[long-liquidation-cascade]] (the more aggressive version that specifically rides the mechanical cascade when longs begin liquidating).

**Cross-reference to [[2026-06-03-cryptodataapi-14-basket-regime-framework]]:** This basket is mapped to the **derivatives-native-regime** and **basis-carry-regime** in the regime framework. In a macro-trend-regime or on-chain-regime, this basket's entry criteria may be structurally satisfied but the underlying signal may be a rational bull market rather than overcrowding — context filters are especially important in those regimes.

---

## Sources

- [[hyperliquid-funding-rate-microstructure]] — hourly funding mechanics, sign conventions, crowding signals.
- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — basket design and regime mapping.
- [[coinglass]] — funding aggregation and OI data.
- [[hypurrscan]] — HL-native analytics.
- [[2025-03-jellyjelly-hlp-attack]] — squeeze incident; execution risk context for short positions on Hyperliquid.
- [[funding-rate-arbitrage]] — strategy family parent.
- [[edge-taxonomy]] — edge classification.

---

## Related

[[crowded-short-funding-fade]] · [[funding-rate-harvest]] · [[oi-confirmed-trend]] · [[range-mean-reversion]] · [[long-liquidation-cascade]] · [[post-liquidation-rebound]] · [[short-liquidation-squeeze]] · [[liquidation-cascade-fade]] · [[liquidation]] · [[funding-rate-arbitrage]] · [[funding-rate]] · [[open-interest]] · [[perpetual-futures]] · [[hyperliquid]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[derivatives-native-regime]] · [[basis-carry-regime]] · [[market-regime]] · [[trading-strategy-baskets]] · [[coinglass]] · [[hypurrscan]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
