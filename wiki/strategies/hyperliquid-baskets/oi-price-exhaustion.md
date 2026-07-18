---
title: "OI / Price Exhaustion (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-07-13
status: good
tags: [crypto, perpetual-futures, hyperliquid, quantitative, swing-trading, mean-reversion, derivatives, market-microstructure, momentum]
aliases: ["OI Exhaustion", "Price-OI Divergence Short", "Open-Interest Trend Exhaustion", "OI Fade"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[technical-structural-regime]]", "[[oi-confirmed-trend]]", "[[distribution-post-peak-short-book]]", "[[crowded-long-funding-fade]]", "[[long-liquidation-cascade]]", "[[open-interest]]", "[[divergence]]", "[[mean-reversion]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[liquidation]]", "[[rsi]]", "[[bollinger-bands]]", "[[bollinger-band-reversion]]", "[[atr]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[2025-10-crypto-liquidation-cascade]]", "[[cryptodataapi]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [behavioral, structural]
edge_mechanism: "Late-trend participants chase price continuation while opening new positions into an increasingly thin and fragile market — declining OI reveals that existing smart-money positions are closing, not new capital entering, so price momentum is running on fumes; the basket fades the trend direction and captures the mean-reversion once the exhausted move rolls over."
data_required: [ohlcv-4h, ohlcv-daily, open-interest, funding-rate, liquidation-feed, perpetual-futures-depth]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.85
expected_max_drawdown: 0.20
breakeven_cost_bps: 40
kill_criteria: |
  - Rolling 6-month drawdown > 20% on the strategy book
  - OI divergence signal shows < 40% hit rate over trailing 30 signals (quantified)
  - Regime shifts to confirmed strong trend with expanding OI → disable and reassign capital
---

# OI / Price Exhaustion (Hyperliquid Basket)

> **Not investment advice** — this page documents the setup for the systematic trading framework. Fading a trend on exhaustion signals is a reversal strategy; it loses when the trend continues with a new wave of participants.

A mean-reversion basket that detects **trend exhaustion** by tracking divergence between price and [[open-interest|Open Interest]]. When price continues making new highs or new lows but OI is declining — meaning existing positions are *closing* rather than new capital *entering* — the trend is losing participation and is structurally fragile. The basket fades the trend direction, anticipating a mean reversion once the exhausted move rolls over.

This basket is the **reversal counterpart to [[oi-confirmed-trend]]**, which confirms and rides trends when OI is *expanding* alongside price. The two baskets share the same underlying data (price + OI) but express opposite views. Where OI-confirmed-trend requires alignment between price and OI as a trend-continuation signal, OI-price-exhaustion treats the *divergence* of the same two variables as a reversal signal. They should not be active simultaneously on the same asset.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral** + **structural** (see [[edge-taxonomy]]).

- **Behavioral:** Late-trend participants exhibit extrapolation bias — they open new positions expecting continuation precisely when the trend is running on momentum rather than new fundamental or structural support. They are buying a narrative at the point where the original thesis holders are quietly exiting.
- **Structural:** [[open-interest|Open Interest]] is a ledger of outstanding derivative positions. When OI declines on a price move, it reveals that position *closure* (profit-taking or stop-outs on the opposite side) is driving the price, not new conviction. A trend driven by closures rather than openings is inherently self-limiting — it runs out of sellers (in a downtrend) or buyers (in an uptrend) once existing positions are exhausted.

The combination of the behavioral and structural components creates a timing edge: the divergence appears *before* the reversal is obvious, giving the basket entry before the crowd recognizes the exhaustion.

## Why This Edge Exists

In a healthy trend, price and OI move together: new capital enters, new positions are opened, and the OI expansion confirms that real money is betting on continuation. When this relationship breaks down — price making new extremes but OI falling — the mechanism is one of two things:

1. **Winners taking profit:** Existing positions in the direction of the trend are being closed for gains. The price move continues in the short term on momentum, but the natural buyers/sellers who fuelled the trend are reducing, not adding.
2. **Losers being stopped out:** Positions *against* the trend are being forcibly closed (stopped out or liquidated), which pushes price further in the trend direction without new conviction capital entering. This is a self-limiting mechanism — once the shorts/longs against the trend are exhausted, the forced-close flow stops.

Both mechanisms describe the same structure: price is moving on *exhaust fumes* rather than fresh fuel. The reversal occurs when:
- The remaining momentum players are all in, leaving no new buyers (in an uptrend) or sellers (in a downtrend).
- The [[funding-rate]] has reached an extreme, making the carry cost prohibitive for remaining trend-followers.
- A minor adverse move triggers the first wave of stop-outs in the trend direction, which cascades.

**Counterparty:** late trend-chasers who open positions on "breakout" signals after OI has already started declining; algorithmic momentum strategies that do not incorporate OI into their signal stack; retail traders who equate "price making new highs" with "trend is strong."

**Contrast with [[oi-confirmed-trend]]:** OI-confirmed-trend is the bullish or bearish *continuation* signal — requires OI expansion on the breakout to enter. OI-price-exhaustion is the *reversal* signal — requires OI contraction on the price extreme to enter against the trend. Running both simultaneously on the same asset would produce offsetting signals; they are mutually exclusive at the single-asset level and should be gated by a regime detector.

## Null Hypothesis

Under "no edge," OI declining while price extends is random noise — price and OI decorrelate for many reasons (options hedging, rollover activity, collateral rebalancing) unrelated to trend exhaustion, and the subsequent price action is not systematically mean-reverting. Fading price extremes on declining OI nets to zero or negative after costs and the occasional continuation that stops the reversal position out.

**Disconfirming evidence to monitor:**
- Reversal trades triggered by OI divergence show < 40% win rate over a 30-trade sample (signal is not predictive).
- Large OI declines followed by *continued* price extension (new participants entering via different instruments — options, spot — that are not captured in the perp OI signal).
- The divergence signal appears and disappears without a clear reversal within the expected 3–10 day window (timing edge lost; signal needs a timeout rule).
- [[derivatives-native-regime|Derivatives-native regime]] shows structural OI declines (protocol-level withdrawal) rather than position-level closes — false positive at the regime level.

## Rules

**Universe.** All Hyperliquid perps with daily OI > $10M and > $20M daily perp volume. Focus on assets where:
1. A trend has been running for at least 10 days (avoids catching flat/choppy markets).
2. Price has made a new N-day high or low in the past 2 sessions.
3. OI over the same window has *declined* by at least 5% relative to the local OI peak.

**Entry conditions (all must hold):**
- Price has made a **new 20-day high or new 20-day low** within the past 2 candles (4H timeframe).
- OI is **≤ 95% of its 10-day peak** — i.e., has declined at least 5% from the local maximum.
- **OI divergence confirmed:** OI has been declining or flat for ≥ 3 consecutive 4H candles while price has continued advancing.
- [[funding-rate]] is at an extreme: > +0.08% per 8h (long exhaustion, fade the uptrend) or < −0.06% per 8h (short exhaustion, fade the downtrend). See [[hyperliquid-funding-rate-microstructure]].
- Price is **within 2 ATR of the N-day high/low** — do not enter if price has already begun reversing; the edge is in anticipating the turn, not confirming it.
- No major catalyst (earnings, listing, unlock) expected within 48h — event risk overrides the exhaustion signal.

**Position sizing:**
- Risk 0.75% of capital per entry.
- Size via ATR (14, 4H): position size = risk / (1.5 × ATR₄H).
- Maximum 5 concurrent positions in this basket.
- Do not run both OI-exhaustion and [[oi-confirmed-trend]] on the same asset simultaneously.

**Entry:**
- Enter the counter-trend position (short if fading an uptrend, long if fading a downtrend) at market on the 4H close that confirms all conditions.
- Alternatively, set a limit order at the most recent price high/low (fading the final push) with a tight leash — cancel if not filled within 2 candles.

**Stop-loss:**
- Stop above the entry-day high / below the entry-day low by 0.5 ATR (tight, because OI divergence should not be followed by a strong new price extension if the thesis is correct).
- If OI *re-expands* by > 5% (new participants entering), exit regardless of price — the divergence has closed and the thesis is false.

**Take-profit / exit:**
- Primary target: mean reversion to the 20-period EMA on the 4H chart (see [[exponential-moving-average]]).
- Secondary target: 50% retracement of the exhausted trend leg.
- Exit fully if OI begins expanding again in the trend direction (thesis invalidated).
- Maximum holding period: 10 days — if the reversal has not materialised, exit and reset.

## Implementation Pseudocode

```python
def oi_price_exhaustion(universe, state, capital):
    positions = []
    MAX_CONCURRENT = 5
    RISK_PER_TRADE = 0.0075 * capital
    N_DAY_WINDOW = 20
    OI_DECLINE_THRESHOLD = 0.05      # OI must be ≥5% below local peak
    FUNDING_LONG_EXTREME = 0.0008    # >0.08% per 8h → longs exhausted
    FUNDING_SHORT_EXTREME = -0.0006  # < −0.06% per 8h → shorts exhausted
    MAX_HOLD_DAYS = 10

    for asset in universe:
        if len(positions) >= MAX_CONCURRENT:
            break
        if state.has_oi_confirmed_trend_position(asset):
            continue   # mutually exclusive with the sibling basket

        p = get_price_data(asset, timeframe="4H", lookback=60)
        d = get_derivatives_data(asset)

        new_high = p.close[-1] >= max(p.close[-N_DAY_WINDOW:-1])
        new_low  = p.close[-1] <= min(p.close[-N_DAY_WINDOW:-1])
        if not (new_high or new_low):
            continue

        # OI divergence: OI declined from its 10-day peak while price extended
        oi_peak_10d = max(d.oi[-10:])
        oi_current  = d.oi[-1]
        oi_declined = (oi_peak_10d - oi_current) / oi_peak_10d >= OI_DECLINE_THRESHOLD
        oi_flat_3c  = all(d.oi[-i] <= d.oi[-i-1] * 1.01 for i in range(1, 4))

        if not (oi_declined and oi_flat_3c):
            continue

        funding = d.funding_rate[-1]
        fade_up   = new_high and funding > FUNDING_LONG_EXTREME
        fade_down = new_low  and funding < FUNDING_SHORT_EXTREME
        if not (fade_up or fade_down):
            continue

        atr = compute_atr(p, period=14)
        if abs(p.close[-1] - (max(p.close[-N_DAY_WINDOW:]) if fade_up
                               else min(p.close[-N_DAY_WINDOW:]))) > 2 * atr:
            continue  # price already reverting — missed entry

        direction = -1 if fade_up else 1  # short on uptrend fade, long on downtrend fade
        stop_dist = 1.5 * atr
        size = RISK_PER_TRADE / stop_dist
        stop = p.close[-1] + direction * (-stop_dist)  # above for short, below for long
        ema20 = compute_ema(p, period=20)
        tp1 = ema20[-1]
        tp2 = p.close[-1] + direction * (
            -0.5 * (max(p.close[-N_DAY_WINDOW:]) - min(p.close[-N_DAY_WINDOW:]))
        )

        positions.append(
            open_perp(asset, direction=direction, size=size,
                      stop=stop, tp1=tp1, tp2=tp2,
                      margin="isolated", leverage=3,
                      tag="oi_exhaustion", max_hold_days=MAX_HOLD_DAYS)
        )

    # --- Ongoing management ---
    for pos in state.open_oi_exhaustion_positions:
        d = get_derivatives_data(pos.asset)
        # Thesis invalidated: OI re-expands
        oi_reexpanded = d.oi[-1] > pos.oi_at_entry * 1.05
        if oi_reexpanded:
            close_position(pos, reason="oi_reexpansion_thesis_failed")
        if pos.age_days >= MAX_HOLD_DAYS:
            close_position(pos, reason="timeout")

    return positions
```

## Indicators / Data Used

- **Open Interest (OI)** — the core signal; 4H and daily OI on Hyperliquid. Sourced from the Hyperliquid API (`metaAndAssetCtxs`), Coinglass ([[coinglass]]), and Hypurrscan ([[hypurrscan]]). The 10-day OI peak and 5%+ decline are the quantitative thresholds.
- **Price** — 4H and daily OHLCV; N-day high/low detection. See OHLCV conventions in [[crypto-perp-backtesting-pitfalls]].
- **OI divergence metric** — `(oi_peak_10d − oi_current) / oi_peak_10d`; must exceed 5% while price is at a new 20-day extreme.
- **Funding rate** — extreme funding confirms the behavioral exhaustion story. Source: [[funding-rate]], [[hyperliquid-funding-rate-microstructure]].
- **ATR (14, 4H)** — entry price proximity filter (must be within 2 ATR of the extreme) and stop sizing. See [[average-true-range]], [[atr]].
- **EMA (20, 4H)** — mean-reversion target for take-profit. See [[exponential-moving-average]], [[moving-average]].
- **RSI (14, daily)** — secondary confirmation; RSI > 80 (uptrend exhaustion) or < 20 (downtrend exhaustion) reinforces the OI signal. See [[rsi]], [[relative-strength-index]].
- **Bollinger Bands (20, 2σ, 4H)** — price at or beyond the upper/lower band provides an additional exhaustion confirmation. See [[bollinger-bands]], [[bollinger-band-reversion]].

## Example Trade

**Illustrative — not a backtest. Figures are estimates to demonstrate setup logic.**

*Setup (uptrend exhaustion / short entry):* SOL-PERP has been in a strong 14-day uptrend, rising from $140 to $195. On day 14, SOL makes a new 20-day high at $196. However, OI has been declining for the past 4 candles (4H): OI peaked at $2.1B on day 11 and is now $1.87B — an 11% decline. Funding is at +0.11% per 8h (extreme). RSI (daily) is at 83. Price is 0.8 ATR from the 20-day high (within entry zone).

| Parameter | Value |
|---|---|
| Asset | SOL-PERP (illustrative) |
| Direction | Short (fading uptrend exhaustion) |
| Entry price | $196.00 |
| OI at entry | $1.87B (−11% from 10-day peak of $2.1B) |
| Funding | +0.11% per 8h |
| Stop | $202.00 (+$6.00 = 1.5 × ATR₄H $4.00) |
| Target 1 — EMA20 (4H) | $181.00 |
| Target 2 — 50% retrace | $167.50 |
| ATR (14, 4H) | $4.00 |
| Leverage | 3× isolated |
| Max hold | 10 days |

*Illustrative outcome:* After 2 days of sideways action at the highs, a moderate negative catalyst (broad risk-off) triggers the reversal. Price falls to $178 over 5 days. ½ position covered at $181 (EMA20, +7.7%), ½ covered at $172 (+12.2%). OI begins re-expanding at $175 (new participants entering the downtrend) — thesis morphs; exits are complete by then. Net: ~+10% on notional, holding for 5 days. Funding earned: +0.11% × 8h intervals × 5 days = ~+3.3% APR equivalent.

*Counter-example (continuation):* OI decline is due to options desk delta-hedging rebalancing; spot buyers (not captured in perp OI) enter aggressively. Price continues to $220. Stop at $202 is hit for −3.1% on notional. Signal was a false positive.

## Performance Characteristics

**All figures are ILLUSTRATIVE ESTIMATES. No walk-forward or live track record exists.**

| Metric | Estimate |
|---|---|
| Win rate (per signal) | ~50–60% (OI divergence is a moderately reliable signal; naive-backtested) |
| Average win / average loss | ~2.0:1 |
| Expected Sharpe (annual) | ~0.7–1.0 in ranging-to-distribution regimes |
| Expected max drawdown | ~15–20% on strategy book |
| Avg holding period | 3–8 days |
| Breakeven round-trip cost | ~40 bps |

The naive backtest (intraday OI + price data, HL perps, 2024–2025) showed the OI-divergence signal producing reversals > 50% of the time within a 10-day window, but survivorship bias and look-ahead OI data are significant concerns — see [[crypto-perp-backtesting-pitfalls]]. Walk-forward validation is needed before live deployment at full size.

**Regime dependence:** Best in [[derivatives-native-regime]] and [[technical-structural-regime]] conditions with ranging or late-trend price action. Underperforms when new fundamental catalysts (macro, institutional flow) produce genuine trend extensions after OI resets at a lower level.

## Capacity Limits

OI and perp depth scale together for major assets. BTC-PERP, ETH-PERP, and SOL-PERP support hundreds of millions in OI; the strategy's counter-trend entries are small relative to total market depth. Strategy-level capacity: **$75–100M** across the basket. The binding constraint is not market impact but signal dilution — if the strategy becomes large enough to move OI readings materially, the signal becomes self-referential. At scale, concentrate on assets with OI > $500M to maintain signal integrity.

Mid-cap alts: keep single-name position < 0.5% of daily perp volume. OI signals on small perps are noisier and more susceptible to manipulation.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Fundamental catalyst extends the trend.** A macro or on-chain catalyst (ETF announcement, major on-chain metric breakout) causes genuine new participants to enter, OI re-expands, and the exhaustion short/long is squeezed. This is the primary risk — the signal is a *positioning* read, not a fundamental one.
2. **OI data lag or manipulation.** Perp OI updates every block on Hyperliquid, but aggregated OI across venues (used for cross-venue confirmation) can have reporting delays. On-chain OI is also subject to wash-trading in smaller perps. See [[crypto-perp-backtesting-pitfalls]].
3. **Cross-venue leakage.** Decline in HL perp OI may be offset by rising OI on CME, Binance, or options markets — the participants haven't closed, they've moved venues. Single-venue OI is incomplete. Monitor [[coinglass]] for cross-venue OI aggregation.
4. **Regime mismatch (strong trend + [[oi-confirmed-trend]] regime).** Running OI-exhaustion against the confirmed-trend basket produces offsetting signals; in a confirmed trend with OI expansion, exhaustion fades are losing trades. Gate by regime.
5. **Short squeeze on the reversal short ([[2025-03-jellyjelly-hlp-attack|JELLY pattern]]).** Even a correct exhaustion signal can be overwhelmed by a coordinated squeeze on a thin perp. Isolated margin and per-name caps are essential.
6. **Funding stays extreme longer than expected.** Extreme funding can persist for days or weeks in a strong trend before exhaustion resolves. The 10-day max-hold timeout prevents runway losses but also cuts profitable positions prematurely if the reversal is slow.
7. **Overfitting the OI threshold.** The 5% OI decline threshold is calibrated on a naive backtest; the optimal threshold is likely regime-dependent and will overfit if not validated out-of-sample. See [[overfitting-detection]].

## Kill Criteria

Numeric conditions for retiring this basket (see [[when-to-retire-a-strategy]]):

- **Rolling 6-month drawdown > 20%** on the strategy book → flatten and reassess.
- **OI divergence signal < 40% win rate** over trailing 30 completed signals → signal is not predictive; pause new entries and re-examine the threshold.
- **[[derivatives-native-regime]] shifts to confirmed strong-trend / OI-expansion regime** → gate off; activate [[oi-confirmed-trend]] instead.
- **Any single position adverse move > 30% within 24h on thin volume** → cover immediately (squeeze guard).
- **Funding persistently < −0.15% per 8h** across short positions → crowded short; exit.
- **Rolling 6-month Sharpe < −0.5** → full review; default to flatten.
- **OI data source goes offline or shows > 30-minute lag** → pause new entries (signal integrity lost).

## Hyperliquid Execution Notes

- **Funding carry:** When fading an uptrend, this basket earns positive funding (shorts receive from longs) if entered at extreme funding. This is a meaningful carry tailwind — at +0.11% per 8h, a 5-day hold earns +3.3% APR. When fading a downtrend (long into exhausted selloff), the basket pays funding. Model the funding carry as part of the expected return; do not enter downtrend fades when funding is deeply negative. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** 3× isolated margin is the ceiling for multi-day holds. Size to survive a 15–20% adverse move. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** Mandatory. OI signals can be wrong; isolated margin limits cross-contamination between positions.
- **JELLY thin-alt squeeze:** Avoid OI exhaustion trades on perps with < $10M OI; the signal is unreliable and the squeeze risk is elevated. See [[2025-03-jellyjelly-hlp-attack]].
- **Transparent OI on Hyperliquid:** HL's real-time, on-chain OI data is a significant information advantage for this strategy — the OI reading is always current and trustworthy. Cross-validate with [[coinglass]] for cross-venue context. Source: [[hyperliquid-vault-architecture]].
- **ADL risk:** If the reversal move is large and fast (e.g., a cascade from the [[2025-10-crypto-liquidation-cascade|cascade]] pattern), the position may be auto-deleveraged. Monitor the ADL indicator and size accordingly.

## Advantages

- **Quantitative and rules-based** — the OI divergence metric is objective, avoiding the subjectivity of pattern recognition.
- **Timing advantage** — enters before the crowd recognizes exhaustion; earlier than price-only reversal signals.
- **Positive funding carry** (uptrend fades) — earns funding while positioned against an overbought trend.
- **Complementary to [[oi-confirmed-trend]]** — the same OI data generates both confirmation and exhaustion signals; the two baskets can be run as a system where oi-confirmed-trend is active in trending regimes and oi-price-exhaustion is active in late-trend / ranging regimes.
- **Hyperliquid OI transparency** — on-chain OI is real-time and reliable, reducing data-quality risk vs. centralized exchange OI.
- **Defined maximum holding period** — the 10-day timeout prevents open-ended drawdowns on slow reversals.

## Disadvantages

- **Naive backtest only** — the 5% OI threshold and 20-day price window have not been validated out-of-sample; overfitting risk is high.
- **Fundamental catalysts override the signal** — OI positioning reads are subservient to fundamental news events.
- **Cross-venue OI incompleteness** — Hyperliquid OI alone misses CME, Binance, and options positioning.
- **Signal timing uncertainty** — exhaustion can persist for days before resolving; the 10-day timeout creates a tension between staying in a correct position and avoiding open-ended losses.
- **Regime gate required** — running this basket in a confirmed trend with OI expansion produces reliable losses.
- **Short squeeze risk** on the reversal positions, particularly on smaller perps.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — OI + funding as derivatives-native regime signals; exhaustion patterns in the framework's basket #4 (Derivatives-Native regime).
- [[open-interest]] — definition and interpretation of open interest as a positioning signal.
- [[divergence]] — OI-price divergence as a reversal indicator.
- [[mean-reversion]] — theoretical basis for the reversal trade.
- [[derivatives-native-regime]] — the regime context in which this basket is designed to operate.
- [[crypto-perp-backtesting-pitfalls]] — OI data look-ahead bias and naive backtest limitations.
- [[hyperliquid-funding-rate-microstructure]] — extreme funding as a behavioral exhaustion signal.
- [[hyperliquid-liquidation-engine]] — liquidation and ADL mechanics relevant to reversal positioning.
- [[2025-10-crypto-liquidation-cascade]] — precedent for OI exhaustion resolving into a liquidation-driven cascade.
- [[coinglass]] — cross-venue OI aggregation for signal validation.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

[[hyperliquid]] · [[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[market-regime]] · [[oi-confirmed-trend]] · [[distribution-post-peak-short-book]] · [[crowded-long-funding-fade]]  · [[crowded-short-funding-fade]] · [[long-liquidation-cascade]] · [[bollinger-band-reversion]] · [[rsi-mean-reversion]] · [[open-interest]] · [[divergence]] · [[mean-reversion]] · [[funding-rate]] · [[perpetual-futures]] · [[liquidation]] · [[rsi]] · [[bollinger-bands]] · [[atr]] · [[derivatives-native-regime]] · [[technical-structural-regime]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[2025-03-jellyjelly-hlp-attack]] · [[2025-10-crypto-liquidation-cascade]] · [[coinglass]] · [[hypurrscan]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
