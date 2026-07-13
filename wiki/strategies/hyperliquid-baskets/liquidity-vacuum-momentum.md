---
title: "Liquidity-Vacuum Momentum (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, scalping, market-microstructure, momentum, quantitative, risk-management]
aliases: ["Liquidity Vacuum", "Book Thinness Momentum", "Order-Book Vacuum Scalp", "Vacuum Momentum Trade"]
related: ["[[hyperliquid-baskets-overview]]", "[[liquidity-depth-regime]]", "[[technical-structural-regime]]", "[[short-liquidation-squeeze]]", "[[long-liquidation-cascade]]", "[[volatility-compression-breakout]]", "[[breakout-trading]]", "[[liquidity]]", "[[order-flow]]", "[[bid-ask-spreads]]", "[[open-interest]]", "[[funding-rate]]", "[[atr]]", "[[leverage]]", "[[liquidation]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-oracle-mechanics]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[2024-03-hyperliquid-cascade]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, latency]
edge_mechanism: "When the order book becomes thin on one side — a 'liquidity vacuum' — a small order-flow imbalance produces a disproportionately large price move; market makers reprice rather than absorb flow, creating a momentum cascade that persists until liquidity re-enters; the basket captures this by entering in the direction of the vacuum before the cascade fires and exiting before liquidity normalises."
data_required: [level2-order-book, ohlcv-1m, ohlcv-5m, open-interest, liquidation-feed, perpetual-futures-depth, funding-rate]
min_capital_usd: 20000
capacity_usd: 20000000
crowding_risk: low
expected_sharpe: 1.10
expected_max_drawdown: 0.30
breakeven_cost_bps: 60
kill_criteria: |
  - Rolling 3-month drawdown > 30% on the strategy book
  - Win rate < 45% over trailing 50 trades (signal no longer identifying real vacuums)
  - Hyperliquid L2 book data unavailable or latency > 2 seconds → halt immediately
---

# Liquidity-Vacuum Momentum (Hyperliquid Basket)

> **Not investment advice** — this page documents the setup for the Alfred systematic framework. Liquidity-vacuum trades are among the highest-execution-sensitivity strategies in the basket library; slippage, latency, and adverse fills can invert the edge entirely. Treat as experimental until live-traded at small size.

A scalping [[trading-strategy-baskets|basket]] that identifies moments when [[hyperliquid|Hyperliquid]]'s [[perpetual-futures|perpetual futures]] order book becomes **thin on one side** — a "liquidity vacuum" — and enters in the direction of the vacuum to capture the fast momentum move before liquidity re-enters. When asks are thin relative to bids (vacuum above the price), a modest buy order can run price up rapidly with minimal resistance; the inverse holds when bids are thin. These are **short-duration, high-frequency reversal or momentum trades** designed to capture the impulsive move, not the subsequent normalisation. It is the [[liquidity-depth-regime]] microstructure expression within Alfred's [[market-regime]] framework.

*Part of the [[hyperliquid-baskets-overview|Alfred Hyperliquid basket library]].*

## Edge Source

**Structural** + **latency** (see [[edge-taxonomy]]).

- **Structural:** [[liquidity|Liquidity]] provision in perpetual futures is not continuous. Market makers widen spreads and pull quotes during uncertainty or when their inventory becomes imbalanced. A thinned book is not an arbitrage-free state — it is a structural vacuum where the next informed order will cause disproportionate price impact. The edge is in identifying these thin-book states *before* the directional order arrives.
- **Latency:** Hyperliquid's on-chain L2 order book is publicly visible and updates every block. A participant who monitors the L2 book in real time has a structural information advantage over participants trading on price alone. The "latency" component here is not microsecond colocation (Hyperliquid is a decentralised venue) but the advantage of systematically processing L2 depth data that most retail participants ignore.

## Why This Edge Exists

Market makers quote both sides of the book to earn the spread. When they face directional risk (their inventory is imbalanced) or uncertainty (a news event is expected, or a cascade is in progress), they widen their spread and reduce their quoted size — or pull quotes entirely on one side. This creates the vacuum: asks thin out above price (or bids thin out below), and the next net buyer (or seller) moves price significantly more than normal.

The cascade mechanism:
1. Book thins on one side; price rests near a technical level.
2. A trigger order (liquidation, stop, algorithmic entry) hits the thin side.
3. Price moves rapidly through the vacuum; no offsetting liquidity absorbs the flow.
4. The price move triggers additional stops/liquidations on the opposite side, amplifying the move.
5. Market makers re-enter the book after the move; price stabilises.

The basket's edge is in steps 2–4: entering after the book is identified as thin and the trigger is plausible, before the cascade fires. The exit is into step 5 — as liquidity normalises, the edge dissipates.

**Hyperliquid-specific structural advantages:**
- On-chain L2 book is public, real-time, and auditable — no exchange-level censorship or reporting delays.
- Large liquidations are visible on-chain before they propagate through the perp book — a leading signal.
- The venue has documented thin-book/cascade events ([[2025-03-jellyjelly-hlp-attack|JELLY, March 2025]], [[2024-03-hyperliquid-cascade|March 2024 cascade]]) confirming that vacuum momentum moves occur and are large.

**Counterparty:** market participants who miss the vacuum detection and are caught on the wrong side of the cascade; late-arriving market makers who reprice after the move; retail traders with wide stop-losses who provide the exit liquidity.

**Relationship to [[short-liquidation-squeeze]]:** A thin-ask-side vacuum often precedes or accompanies a short-liquidation squeeze; this basket can enter the same move, but it does so on the book structure, not the liquidation cascade signal itself. The two are complementary — liquidation-cascade entries are event-driven (a large liquidation fires), vacuum entries are structure-driven (the book is thin before any trigger). See [[short-liquidation-squeeze]] and [[long-liquidation-cascade]] for the cascade-specific baskets.

## Null Hypothesis

Under "no edge," thin order books are a noise signal: market makers pull quotes for many reasons unrelated to directional flow (end-of-day inventory, protocol maintenance, low-activity periods), and price moves on a thin book mean-revert just as often as they continue. The thin-book detection does not predict the direction or magnitude of the subsequent move with above-random accuracy.

**Disconfirming evidence to monitor:**
- Win rate < 45% over 50 trades (no directional edge in vacuum detection).
- Average move after vacuum detection is < breakeven round-trip cost (vacuum exists but is not large enough to trade profitably).
- Latency to detect + enter exceeds 3 seconds on average — the vacuum refills before entry; execution edge is gone.
- Vacuum signals cluster during low-volume hours but moves reverse rapidly (thin books in low-activity windows are not directional, just wide-spread).

## Rules

**Universe.** Hyperliquid perps with daily OI > $50M and > $50M daily volume. Focus on **BTC-PERP, ETH-PERP, SOL-PERP, and the top 5–10 liquid alts** — larger books make vacuum identification cleaner (a thin side is more significant). Avoid perps with < $10M OI — thin books are the *norm* there, not a signal.

**Vacuum detection (all must hold):**
- **L2 book imbalance:** the ratio of bid depth (sum of bid sizes within 0.5% of mid) to ask depth (sum of ask sizes within 0.5% of mid) is > 3:1 or < 1:3. Specifically:
  - **Ask-thin vacuum (buy signal):** ask depth / bid depth < 0.33 — asks are less than ⅓ of bid depth.
  - **Bid-thin vacuum (sell signal):** bid depth / ask depth < 0.33 — bids are less than ⅓ of ask depth.
- **Vacuum persistence:** the imbalance has held for ≥ 2 consecutive 1-minute candle closes (not a transient quote withdrawal).
- **Price is near a key level:** within 0.5% of a 4H swing high/low, VWAP ([[vwap]]), or a [[resistance]]/[[support]] cluster — the level increases the probability that a trigger order will fire into the vacuum.
- **Confirming catalyst (at least one):**
  - A large liquidation (> $500K notional) has fired in the prior 5 minutes on the opposing side (shorts liquidated → asks thin; longs liquidated → bids thin).
  - OI has spiked > 2% in the prior 30 minutes (new leveraged positions entering — more liquidation fuel).
  - Funding rate is at an extreme (> +0.08% or < −0.06% per 8h) on the thin side — extreme positioning aligns with the vacuum direction.
- **ATR filter:** 1-minute ATR is above its 20-period mean (confirming live volatility, not a dead market).

**Position sizing:**
- Risk 0.5% of capital per trade (scalp — higher frequency, tighter sizing).
- Size via 1-minute ATR: position size = risk / (1.0 × ATR₁ₘ).
- Maximum 2 concurrent positions in this basket (execution focus required; do not multi-task).

**Entry:**
- Market order into the vacuum direction immediately on signal confirmation. Limit orders are acceptable *only* on ask-thin signals (place a resting bid below mid to capture the liquidity that fills the vacuum); do not use limits on bid-thin signals (liquidity may never return at your level).
- Maximum 3-second delay from signal to entry; if delayed, skip the trade.

**Stop-loss:**
- Stop 1.0 × ATR₁ₘ adverse from entry. Tight — if the vacuum was real, price should move immediately.
- Hard stop at 2.0% adverse move regardless of ATR (circuit breaker for gap/cascade scenarios).

**Take-profit / exit:**
- Target 1: 1.5 × ATR₁ₘ in the direction of the vacuum.
- Target 2: 3.0 × ATR₁ₘ if momentum continues (trail with a 0.5 × ATR₁ₘ trailing stop).
- **Time-based exit:** close the position after 15 minutes regardless of P&L. The vacuum should resolve within this window; holding beyond it means trading on stale information.
- **Book refill exit:** if the thin side refills to within 2:1 depth ratio before target is hit, exit immediately — the structural edge has normalised.

## Implementation Pseudocode

```python
def liquidity_vacuum_momentum(universe, state, capital):
    positions = []
    MAX_CONCURRENT = 2
    RISK_PER_TRADE = 0.005 * capital
    VACUUM_RATIO = 0.33          # thin side < 1/3 of deep side within 0.5% of mid
    VACUUM_PERSIST_CANDLES = 2   # must hold for ≥2 consecutive 1m closes
    MAX_ENTRY_DELAY_SEC = 3
    MAX_HOLD_MINUTES = 15
    DEPTH_WINDOW_PCT = 0.005     # 0.5% of mid for depth aggregation

    for asset in universe:
        if len(positions) >= MAX_CONCURRENT:
            break

        book = get_l2_book(asset)          # real-time HL on-chain order book
        mid = (book.best_bid + book.best_ask) / 2
        bid_depth = sum(q for p, q in book.bids if p >= mid * (1 - DEPTH_WINDOW_PCT))
        ask_depth = sum(q for p, q in book.asks if p <= mid * (1 + DEPTH_WINDOW_PCT))

        ask_thin = ask_depth / bid_depth < VACUUM_RATIO if bid_depth > 0 else False
        bid_thin = bid_depth / ask_depth < VACUUM_RATIO if ask_depth > 0 else False

        if not (ask_thin or bid_thin):
            continue

        # Persistence check: vacuum held for ≥2 consecutive 1m candles
        if not vacuum_persisted(asset, direction="ask" if ask_thin else "bid",
                                candles=VACUUM_PERSIST_CANDLES):
            continue

        p = get_price_data(asset, timeframe="1m", lookback=30)
        atr_1m = compute_atr(p, period=14)
        if atr_1m < mean_atr_1m(p, lookback=20):  # dead market filter
            continue

        # Key level proximity
        near_level = is_near_key_level(asset, mid, tolerance_pct=0.005)
        if not near_level:
            continue

        # Confirming catalyst: at least one
        d = get_derivatives_data(asset)
        large_liquidation = recent_liquidation_notional(asset, seconds=300) > 500_000
        oi_spike = (d.oi[-1] - d.oi[-30]) / d.oi[-30] > 0.02
        funding_extreme = abs(d.funding_rate[-1]) > 0.0008
        catalyst = large_liquidation or oi_spike or funding_extreme
        if not catalyst:
            continue

        direction = 1 if ask_thin else -1   # long on ask-thin, short on bid-thin
        stop_dist = max(1.0 * atr_1m, 0.005 * mid)  # ≥ 0.5% hard floor
        size = RISK_PER_TRADE / stop_dist
        tp1 = mid + direction * 1.5 * atr_1m
        tp2 = mid + direction * 3.0 * atr_1m
        stop = mid - direction * stop_dist

        t_start = current_time()
        if (current_time() - t_start).seconds > MAX_ENTRY_DELAY_SEC:
            continue  # too slow; signal stale

        positions.append(
            open_perp(asset, direction=direction, size=size,
                      stop=stop, tp1=tp1, tp2=tp2,
                      margin="isolated", leverage=5,
                      tag="vacuum_momentum",
                      max_hold_minutes=MAX_HOLD_MINUTES,
                      book_refill_exit_ratio=2.0)
        )

    # --- Ongoing management ---
    for pos in state.open_vacuum_positions:
        book = get_l2_book(pos.asset)
        mid = (book.best_bid + book.best_ask) / 2
        bid_d = sum(q for p, q in book.bids if p >= mid * 0.995)
        ask_d = sum(q for p, q in book.asks if p <= mid * 1.005)
        refill_ratio = (ask_d / bid_d if pos.direction == 1 else bid_d / ask_d)
        if refill_ratio >= 2.0:
            close_position(pos, reason="book_refill")
        if pos.age_minutes >= MAX_HOLD_MINUTES:
            close_position(pos, reason="timeout")
        apply_trailing_stop(pos, atr_multiple=0.5, timeframe="1m")

    return positions
```

## Indicators / Data Used

- **L2 order book depth** — the core signal: real-time bid/ask depth within 0.5% of mid on Hyperliquid's on-chain book. Sourced from the Hyperliquid API (L2 order book endpoint). Depth ratio is the primary vacuum metric.
- **1-minute ATR** — volatility filter (ensures live market), stop sizing, and target computation. See [[average-true-range]], [[atr]].
- **Liquidation feed** — on-chain liquidation events as a confirming catalyst. Large liquidations signal forced flow that can trigger or amplify a vacuum move. Source: [[hyperliquid-liquidation-engine]], Hypurrscan ([[hypurrscan]]).
- **Open Interest (1m change)** — OI spike as a catalyst: new leveraged participants entering → more potential liquidation fuel. Source: [[open-interest]], Hyperliquid API.
- **Funding rate** — extreme funding confirms one-sided positioning in the vacuum direction. Source: [[funding-rate]], [[hyperliquid-funding-rate-microstructure]].
- **Key price levels** — 4H swing highs/lows, [[vwap]], [[resistance]]/[[support]] clusters as proximity filter for the vacuum. See [[vwap-trading]], [[market-cap-level-trading]].
- **[[order-flow]]** — directional flow at the book (market orders vs limit orders) as a real-time entry confirmer.
- **[[bid-ask-spreads]]** — spread widening is a secondary signal that market makers are pulling quotes (corroborates the depth imbalance reading).

**Data-feed mapping (cryptodataapi.com).** Every input is venue-native and read from cryptodataapi.com's Hyperliquid endpoints: the L2 order book (the depth-ratio vacuum metric), 1m/5m OHLCV (ATR filter), the liquidation feed (confirming catalyst), [[open-interest]] (1m change catalyst), [[funding-rate]] (extreme-positioning catalyst), and mark/oracle price (divergence guard). Because the entire edge is microstructure, real-time, low-latency cryptodataapi L2 and liquidation feeds are the strategy's critical dependency — the `L2 data unavailable or latency > 2 s → hard halt` kill criterion is a direct statement about this feed.

## Example Trade

**Illustrative — not a backtest. Figures demonstrate setup logic only.**

*Setup (ask-thin vacuum, long entry):* BTC-PERP is trading at $98,400. The L2 book shows bid depth of 45 BTC within 0.5% of mid; ask depth is only 8 BTC on the same side — an 18% ask/bid ratio (well below the 33% vacuum threshold). A $1.2M short liquidation fired 3 minutes ago. Funding is +0.09% per 8h. Price is 0.3% below a prior 4H swing high at $98,700. ATR (1m) is $120, above its 20-period mean. All conditions met.

| Parameter | Value |
|---|---|
| Asset | BTC-PERP (illustrative) |
| Direction | Long (ask-thin vacuum) |
| Entry price | $98,420 (market) |
| Ask depth / bid depth | 18% (8 BTC vs 45 BTC) |
| Vacuum persisted | 2 candles (confirmed) |
| Confirming catalyst | $1.2M short liquidation (3min prior), funding +0.09%/8h |
| Stop | $98,300 (−$120 = 1.0 × ATR₁ₘ) |
| Target 1 | $98,600 (+$180 = 1.5 × ATR₁ₘ) |
| Target 2 | $98,780 (+$360 = 3.0 × ATR₁ₘ; trailing stop) |
| ATR (1m) | $120 |
| Leverage | 5× isolated |
| Max hold | 15 minutes |

*Illustrative outcome:* The vacuum is real — BTC rips to $98,780 in 7 minutes as the thin ask side offers no resistance. ½ position covered at $98,600 (+$180/BTC, +0.18%), ½ trailed to $98,680 (+$260/BTC, +0.26%). Book refills by the 12-minute mark; position closed in full before the timeout. Gross return: ~+0.22% on notional. Round-trip cost: ~0.08% (taker fee × 2). Net: ~+0.14% on notional (small in %, but captured in 12 minutes; annualised on capital = significant).

*Counter-example (false vacuum):* The 18% ask/bid ratio is caused by a market maker reconfiguring quotes, not genuine distribution of supply. A large buy order replenishes the ask side within 90 seconds. Price barely moves (+$30). Position closed at the book-refill exit for approximately breakeven after fees (−0.04% on notional). The false positive is identified and not exited at a loss — the book-refill exit cuts it before the adverse move develops.

*Adverse scenario (gap through stop):* A macro shock (Fed speaker, exploit headline) causes a $300 BTC gap adverse in 10 seconds before the stop can fill. Slippage means the actual exit is at −$250/BTC vs the −$120 intended stop, a −2× stop-loss loss. This is the primary risk — use isolated margin and size to absorb a 2× stop slippage without cascading into other positions.

## Performance Characteristics

**All figures are ILLUSTRATIVE ESTIMATES. No walk-forward or live track record exists.**

| Metric | Estimate |
|---|---|
| Win rate (per signal) | ~55–65% (structure-driven; naive backtest) |
| Average win / average loss | ~1.5:1 (tight timeframe; wins are modest in %) |
| Trade frequency | 3–15 per day across the universe (regime-dependent) |
| Expected Sharpe (annual) | ~0.9–1.3 (execution-dependent; degrades sharply with latency) |
| Expected max drawdown | ~25–30% on strategy book |
| Avg holding period | 5–12 minutes |
| Breakeven round-trip cost | ~60 bps (taker fee + slippage; high for a scalp) |

The strategy is **execution-sensitive to an extreme degree.** The 60 bps breakeven cost is high for a scalp; it requires average wins of > 90 bps to be profitable at a 60% win rate. Any increase in execution latency, slippage, or fee tier can push the strategy below breakeven. The naive backtest used simulated fills at mid; live fills will be worse. **Paper-trade for ≥ 30 days before committing real capital.**

**Regime dependence:** Active during [[liquidity-depth-regime|liquidity-depth regime]] episodes of book thinning, especially during cascades, large liquidation events, and around key market structure levels. Inert (no signals) during deep liquidity / tight spread periods (institutional accumulation regimes, low-volatility windows).

## Capacity Limits

This is the most capacity-constrained basket in the library. The vacuum signal requires entering *before* the cascade fills the thin side — a large position on entry *is* the trigger that starts filling the vacuum, removing the edge. Strategy-level capacity: **$15–20M** across the basket, with a hard per-trade notional cap of **$2M per entry on BTC-PERP and $500K on alt perps**. Beyond these levels, the position size is large enough to move the thin side before the cascade develops, converting the signal into self-fulfilling and then self-defeating noise.

Mid-cap alt perps are largely unsuitable at any real capital level — the baseline liquidity is too thin to distinguish a vacuum signal from normal market conditions.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Execution latency.** The vacuum window is measured in seconds. A 5-second latency turns a profitable entry into a late entry chasing the move at the worst price. On Hyperliquid's on-chain venue, block time and RPC latency are the constraints. Any infrastructure degradation kills the edge immediately.
2. **Thin-book false positives.** Not every thin book is a vacuum before a move — sometimes it is a low-activity period with no directional catalyst. The persistence and catalyst filters reduce but do not eliminate false positives.
3. **Adverse gap through stop ([[2025-03-jellyjelly-hlp-attack|cascade scenario]]).** A macro shock or large liquidation cascade can gap price through the stop entirely; the actual exit is significantly worse than the intended stop. Isolated margin and hard 2% circuit breakers limit the damage per position.
4. **Market maker adaptation.** If this pattern becomes well-known and widely traded, market makers will adjust — posting thin apparent quotes as a trap (a "spoofed" vacuum that refills when a buy order arrives). The spoofing filter (persistence ≥ 2 candles) mitigates but does not eliminate this.
5. **Signal crowding.** Multiple systematic strategies detecting the same vacuum at the same time all enter together, fill the thin side immediately on entry, and there is no subsequent cascade — the crowd *is* the move, which then reverses against all of them.
6. **JELLY pattern ([[2025-03-jellyjelly-hlp-attack]]):** A coordinated manipulation creates a false vacuum (thin asks on a thin-OI perp) to bait a long entry, then a large sell crushes the book. Mitigation: only trade high-OI perps (> $50M daily volume).
7. **Data source failure.** The entire strategy depends on real-time L2 book data. Any API outage, data staleness, or RPC throttling halts the strategy immediately — this is why the "L2 data unavailable" kill criterion is a hard halt.

## Kill Criteria

Numeric conditions for retiring this basket (see [[when-to-retire-a-strategy]]):

- **Rolling 3-month drawdown > 30%** on the strategy book → flatten and halt.
- **Win rate < 45% over trailing 50 trades** → signal no longer identifying real vacuum moves; pause new entries and diagnose.
- **Average execution slippage > 40 bps per entry** → breakeven cost is too high at current execution quality; halt until infrastructure is improved.
- **L2 book data unavailable or latency > 2 seconds** → hard halt; this is a non-negotiable execution-quality threshold.
- **Any single position adverse gap > 5% before stop fill** → post-mortem and review position size limits.
- **Rolling 3-month Sharpe < 0.0** → full review; this strategy has zero margin for error — flat performance means the edge is gone.

## Hyperliquid Execution Notes

- **Funding carry:** Irrelevant at this timeframe (5–15 minute holds); funding accrues every 8 hours and has no material impact on scalp P&L. Funding is used only as a confirming catalyst signal, not as a carry consideration.
- **Single-mark-tick liquidation + ADL:** At 5× leverage, a 20% adverse move triggers liquidation. On a 15-minute scalp, this is an extreme scenario, but the ADL system can also deleverage winning positions during a cascade. Size to survive a 10% adverse spike without liquidation. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** Mandatory and non-negotiable for a strategy with this level of execution and gap risk. Never run vacuum trades on cross-margin.
- **JELLY thin-alt squeeze risk:** Exclusively trade high-OI, high-volume perps. Any perp with < $50M OI is off-limits for this basket. The baseline book on thin perps is structurally similar to a vacuum state, making signal discrimination impossible. See [[2025-03-jellyjelly-hlp-attack]].
- **Oracle / mark-price divergence:** During fast vacuum moves, the HL mark price (which is oracle-based) can diverge significantly from the actual perp book price. A position that is profitable on the perp book can still be liquidated if the mark price lags or diverges adversely. Monitor the oracle vs. book spread during entries. Source: [[hyperliquid-oracle-mechanics]].
- **Transparent L2 book:** Hyperliquid's on-chain book is the entire edge. Unlike centralized exchanges, the HL book cannot be censored, selectively shown, or rolled back — what you see is the real book. This is a significant structural advantage for this strategy. Source: [[hyperliquid-vault-architecture]].

## Advantages

- **Structural edge in a microstructure niche** — book-depth monitoring is computationally accessible but requires real-time L2 processing that most participants do not do.
- **Short duration** — 5–15 minute holds mean the strategy is not exposed to overnight risk, macro events, or funding fluctuations.
- **High trade frequency** — generates more data points for rapid model evaluation vs. swing strategies.
- **Hyperliquid-specific advantage** — the on-chain, transparent L2 book on Hyperliquid is more reliable than centralized exchange order book feeds, which are subject to fee-tiered data access and potential manipulation.
- **Complementary to cascade baskets** — the vacuum signal often fires *before* the cascade signal; pairing with [[short-liquidation-squeeze]] or [[long-liquidation-cascade]] baskets can provide earlier entries on the same underlying move.
- **Low crowding risk** — the combination of real-time L2 processing, sub-3-second entry discipline, and the narrow capacity cap keeps this niche uncrowded at meaningful capital levels.

## Disadvantages

- **Highest execution sensitivity of any basket** — latency, slippage, and fee rates are existential risks, not implementation details.
- **Naive backtest only with significant simulation bias** — live fill quality on a thin book is fundamentally worse than simulated mid-fills; the backtest overstates performance.
- **Low capacity** — $15–20M strategy cap; not scalable.
- **Continuous monitoring required** — unlike swing strategies that can be managed with daily check-ins, vacuum trading requires real-time infrastructure and immediate kill-switch capability.
- **Gap risk** — a macro event or cascade can gap price through the stop before it fills; isolated margin limits but does not eliminate the risk.
- **Infrastructure dependency** — the strategy is entirely dependent on reliable, low-latency L2 data; any data quality issue halts the strategy.
- **High round-trip cost** — 60 bps breakeven is demanding for a short-duration trade; leaves little margin for adverse fills.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Liquidity/Market Depth as basket #9 in the regime framework; OI vs. book depth as a fragility signal; vacuum states as a cascade precursor.
- [[liquidity-depth-regime]] — theoretical basis for order-book depth as a regime classifier.
- [[hyperliquid-liquidation-engine]] — liquidation mechanics, ADL, and mark-price divergence risks relevant to scalp positions.
- [[hyperliquid-oracle-mechanics]] — mark-price vs. book-price divergence during fast moves.
- [[hyperliquid-funding-rate-microstructure]] — funding rate as a positioning signal and confirming catalyst.
- [[hyperliquid-vault-architecture]] — on-chain L2 book transparency as a structural advantage.
- [[2025-03-jellyjelly-hlp-attack]] — documented thin-book manipulation (JELLY); precedent for the squeeze risk on low-OI perps.
- [[2024-03-hyperliquid-cascade]] — documented vacuum-driven cascade on Hyperliquid; real-world precedent for the move this basket targets.
- [[liquidity]] — theoretical framework for order-book liquidity and depth.
- [[order-flow]] — microstructure basis for directional momentum in thin markets.
- [[crypto-perp-backtesting-pitfalls]] — execution-quality bias in scalp strategy backtests.

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[market-regime]] · [[short-liquidation-squeeze]] · [[long-liquidation-cascade]] · [[volatility-compression-breakout]] · [[breakout-trading]] · [[failed-breakout-failed-breakdown]] · [[liquidity]] · [[order-flow]] · [[bid-ask-spreads]] · [[open-interest]] · [[funding-rate]] · [[atr]] · [[leverage]] · [[liquidation]] · [[perpetual-futures]] · [[vwap]] · [[resistance]] · [[support]] · [[liquidity-depth-regime]] · [[technical-structural-regime]] · [[derivatives-native-regime]] · [[hyperliquid]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-oracle-mechanics]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-vault-architecture]] · [[2025-03-jellyjelly-hlp-attack]] · [[2024-03-hyperliquid-cascade]] · [[coinglass]] · [[hypurrscan]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
