---
title: "Long-Liquidation Cascade (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, liquidation, market-microstructure, algorithmic, scalping, derivatives]
aliases: ["Long Flush Short", "Liquidation Heatmap Short", "Cascade Rider Short", "Long Liquidation Rider"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[liquidity-depth-regime]]", "[[short-liquidation-squeeze]]", "[[post-liquidation-rebound]]", "[[crowded-long-funding-fade]]", "[[liquidation-cascade-fade]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-10-crypto-liquidation-cascade]]", "[[2024-03-hyperliquid-cascade]]", "[[long-liquidation]]", "[[liquidation]]", "[[open-interest]]", "[[leverage]]", "[[order-flow]]", "[[funding-rate]]", "[[coinglass]]", "[[hypurrscan]]", "[[atr-position-sizing]]", "[[atr-trailing-stop]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [structural, latency]
edge_mechanism: "Long liquidation engines are forced to sell the perp as price falls through maintenance margin thresholds — mechanical, price-insensitive selling that is self-reinforcing; positioning short just above clustered long liquidation levels captures the forced selling cascade as it fires."
data_required: [perp-funding, open-interest, liquidation-feed, order-book-depth, liquidation-heatmap, mark-price]
min_capital_usd: 10000
capacity_usd: 5000000
crowding_risk: medium
expected_sharpe: 1.0
expected_max_drawdown: 0.32
breakeven_cost_bps: 45
kill_criteria: |
  - Win rate drops below 48% over trailing 20 completed trades
  - Three consecutive full stop-outs (each > 10% drawdown on position)
  - Drawdown > 28% on this basket over rolling 6 months
  - Liquidation heatmap data source becomes unavailable or unreliable
---

# Long-Liquidation Cascade (Hyperliquid Basket)

**Not investment advice — this page documents the basket setup.**

When a cluster of leveraged long positions accumulates near a price level, a sustained offer at that level triggers a mechanical chain reaction: as mark price falls through the long liquidation thresholds, Hyperliquid's liquidation engine is forced to close (sell) those longs into the order book. Each liquidation-forced sell pushes price lower, triggering the next tier of long liquidations below — a self-reinforcing cascade of mechanical selling. This basket enters **short just above the identified liquidation cluster**, riding the non-economic forced selling down through the cascade. It is the direct mirror of [[short-liquidation-squeeze]]; where that basket rides forced *buying* upward, this basket rides forced *selling* downward.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

---

## Edge Source

**Structural** + **latency** (see [[edge-taxonomy]]).

- **Structural (primary).** [[long-liquidation|Long liquidation]] engines on Hyperliquid ([[hyperliquid-liquidation-engine]]) are *forced* to market-sell the perp when a long position's margin falls below the maintenance threshold. This selling is non-economic — the engine will sell at whatever price the book supports because *not selling* means the insurance fund bears the shortfall. Below a clustered set of long liquidation levels, price is therefore exposed to a wave of guaranteed, non-price-sensitive sell orders.
- **Latency (secondary).** Liquidation heatmaps ([[coinglass]], [[hypurrscan]]) provide a forward view of *where* clustered long positions sit below current price. A trader who reads this data, recognises that price is approaching those levels, and enters short before the liquidations fire has a timing and informational advantage that translates into better average entry prices than reacting after the cascade begins.

**Critical differentiation from [[liquidation-cascade-fade]]:** The [[liquidation-cascade-fade]] is a *contrarian* strategy that **enters long after** a cascade has completed — buying the overshooting bottom and targeting a mean-reversion snap-back. This basket is a *trend-following* strategy that **enters short before** the cascade fires — riding the mechanical selling downward through the cluster. The two strategies trade on the same underlying event but on opposite sides and at opposite points in the lifecycle:

- [[long-liquidation-cascade]] (this basket): enter *before* cascade → ride the downward move → exit *as* cascade exhausts.
- [[liquidation-cascade-fade]]: enter *after* cascade exhausts → ride the snapback → exit at prior-level mean reversion.

A complete setup provides both signals in sequence; they should not be run simultaneously on the same pair event, but can be sequenced one after the other.

**Differentiation from [[crowded-long-funding-fade]]:** The funding fade is a macro swing signal (elevated positive funding over hours/days; enter short; target multi-day correction). This basket is a micro signal (specific liquidation levels identified; mechanical selling imminent; enter short; target scalp). They can fire together; the funding fade provides the context, this basket provides the precise scalp entry.

---

## Why This Edge Exists

The long-liquidation cascade mirrors the short-squeeze mechanics in reverse:

1. **Accumulation phase.** Price has been rising; retail traders established longs expecting continuation. These longs cluster at similar margin levels — many entered at the same price range using similar leverage.
2. **Clustering visible on heatmaps.** Coinglass and Hypurrscan heatmaps show the notional of long positions with maintenance margins that would be breached at each price level below current price.
3. **Price approaches the cluster.** Some selling pressure (macro news, large sell order, spot ETF outflow, whale exit) drives price down toward the cluster.
4. **Entry trigger.** The basket enters short when price is within the [[atr|ATR]] of the cluster — the cascade is imminent but hasn't fired yet.
5. **Cascade fires.** Price touches the first long liquidation threshold. Hyperliquid's engine closes those longs by market-selling the perp. The forced selling pushes price below the next threshold. More longs are liquidated. The feedback is self-reinforcing as long as the density of liquidation levels outweighs the available bids.
6. **Cascade exhaustion.** The final clustered long is liquidated; forced selling ceases. Price stabilises (often sharply — see [[post-liquidation-rebound]] for the next phase).
7. **Exit.** The basket exits near cascade exhaustion.

**Who is on the other side?** The leveraged long being liquidated — executing mechanically at whatever price the book allows, with no optionality. These are the most reliable, most predictable counterparties to trade against.

**Empirical reference:** The [[2025-10-crypto-liquidation-cascade]] (October 2025 Trump tariff event, $3.21B in a single 60-second window, [[2025-10-crypto-liquidation-cascade]]) is an extreme instance of this mechanic at full scale. The [[2024-03-hyperliquid-cascade]] is a Hyperliquid-specific example.

---

## Null Hypothesis

Under "no edge," long liquidation clusters on heatmaps are already priced in: buyers step up to defend those levels, absorbing the incoming selling before it cascades, and price never reaches the liquidation thresholds. Or: the cascade fires, but immediately reverses (bid absorption is fast, and the cascade overshoot is minimal — see [[liquidation-cascade-fade]]) such that a short position entered above the cluster is quickly stopped out.

**Disconfirming evidence to monitor:**
- Majority of trades reach the time stop without hitting the target — cascades are not completing.
- Liquidation cluster levels are consistently defended by buy orders — the market is pricing in the cluster and defending against it.
- Backtested win rate falls below 48% — heatmap predictive value insufficient.
- Post-cascade analysis shows immediate snapback above entry price within 1 hour — the cascade overshoots so briefly that scalp exits are not achievable.

---

## Rules

**Universe:** BTC, ETH, SOL as primaries; liquid HL mid-caps as secondaries. Do NOT run this basket on thin or memecoin pairs — thin pairs have extreme slippage on cascades, and a short position on a thin pair during a cascade can be difficult to close as bids disappear. (Note: the JELLY incident, [[2025-03-jellyjelly-hlp-attack]], involved a *short squeeze* rather than a long cascade, but it illustrates the thin-pair liquidity problem for both sides.)

**Entry criteria:**
1. **Heatmap cluster identified:** A long liquidation cluster of notional size ≥ 2× the average daily liquidation volume for that pair exists in the price range [current price − 6 ATR, current price − 1 ATR] — within reach, but the cascade hasn't started yet.
2. **Positive-funding confirmation (optional but preferred):** Current hourly funding is positive or near-zero — confirms the crowd is net long. See [[hyperliquid-funding-rate-microstructure]] for sign convention.
3. **Price momentum toward the cluster:** Last 1-hour candle is bearish or neutral; price is drifting toward the cluster.
4. **Order flow confirmation:** Sell-side volume exceeds buy-side in last 15 minutes.
5. **Open interest elevation:** OI ≥ 1.2× 7-day mean — confirms the long book is populated.

**Entry execution:** Market short, isolated margin, 3–5× leverage. As with [[short-liquidation-squeeze]], higher leverage is acceptable for the short duration hold.

**Exit — take profit:**
- Price reaches the bottom of the identified liquidation cluster (lowest-density heatmap level in the cluster) — close 60% of position.
- Price extends 2% below the cluster bottom (overshoot) — close remaining 40%.

**Exit — stop:**
- Hard stop at −5% from entry (price moves against the short — upward).
- ATR trailing stop: trail at entry price + 1.5 × ATR above current price.
- Time stop: 4 hours. A cascade that hasn't fired in 4 hours is likely not firing from this setup.

**Sizing:** 4–7% of basket equity per trade. Max 1 concurrent position. Never pyramid into a cascade — it increases exposure precisely when the risk is highest.

---

## Implementation Pseudocode

```python
# Long-Liquidation Cascade — basket module
# Regime: derivatives-native-regime + liquidity-depth-regime
# Mirror of short-liquidation-squeeze; rides cascade DOWN

CLUSTER_DAILY_LIQ_MULTIPLIER = 2.0
ATR_MIN_RANGE    = 1            # cluster starts 1 ATR below price
ATR_MAX_RANGE    = 6            # cluster ends 6 ATR below price
OI_RELATIVE_MIN  = 1.20
ENTRY_LEVERAGE   = 4.0
STOP_LOSS_PCT    = 0.05         # stop 5% ABOVE entry (short stop)
PARTIAL_EXIT_PCT = 0.60
TIME_STOP_HOURS  = 4
POSITION_SIZE    = 0.05

def evaluate_long_cascade(pair, state, equity):
    price   = get_mark_price(pair)
    atr     = get_atr(pair, period=14, timeframe='1h')
    funding = get_hourly_funding(pair)
    oi_now  = get_open_interest(pair)
    oi_7d   = rolling_mean(get_oi_history(pair), days=7)
    volume_balance = get_buy_sell_volume_ratio(pair, minutes=15)

    # Skip thin/memecoin pairs — cascade slippage too severe
    if get_daily_volume(pair) < MIN_LIQUIDITY or is_memecoin(pair):
        return

    # Identify long liquidation cluster below price
    cluster = get_liquidation_cluster(
        pair,
        direction='long',           # long positions that will be closed (sold)
        price_min=price - ATR_MAX_RANGE * atr,
        price_max=price - ATR_MIN_RANGE * atr,
        min_notional=CLUSTER_DAILY_LIQ_MULTIPLIER * get_avg_daily_liq(pair)
    )

    if cluster is None:
        return

    confirmations = [
        funding >= 0,               # crowd is long (optional confirmation)
        volume_balance < 0.97,      # mild sell-side dominance
        oi_now >= OI_RELATIVE_MIN * oi_7d,
    ]

    if sum(confirmations) >= 2 and not state.has_position(pair):
        notional  = equity * POSITION_SIZE * ENTRY_LEVERAGE
        entry_px  = price
        stop_px   = entry_px * (1 + STOP_LOSS_PCT)   # stop is ABOVE entry
        target_1  = cluster.bottom                    # bottom of cluster
        target_2  = cluster.bottom * 0.98             # 2% below cluster bottom
        state.open_short(pair, notional, entry_px, stop_px,
                         tag="long-cascade",
                         cluster_bottom=cluster.bottom,
                         deadline_hours=TIME_STOP_HOURS)

    if state.has_position(pair):
        pos   = state.get_position(pair)
        price = get_mark_price(pair)
        atr_trail_stop = pos.entry * (1 + 1.5 * atr / pos.entry)

        if price <= pos.cluster_bottom and not pos.half_exited:
            state.close_partial(pair, fraction=PARTIAL_EXIT_PCT, tag="cluster-bottom")
        if price <= pos.cluster_bottom * 0.98:
            state.close_all(pair, tag="overshoot-target")
        if price >= pos.stop_px or price >= atr_trail_stop:
            state.close_all(pair, tag="stop")
        if state.hours_held(pair) >= TIME_STOP_HOURS:
            state.close_all(pair, tag="time-stop")
```

---

## Indicators / Data Used

- **Liquidation heatmaps (long-side)** — primary signal; identifies clustered long positions below current price. Source: [[coinglass]] heatmap, [[hypurrscan]].
- **[[open-interest]]** — confirms the long book is populated and real at entry time.
- **[[atr|ATR]]** — defines entry zone relative to cluster; sizes the trailing stop. See [[atr-position-sizing]], [[atr-trailing-stop]].
- **[[order-flow]] (sell/buy volume ratio)** — confirms directional momentum toward the cluster.
- **[[funding-rate]] (hourly)** — contextual confirmation that the crowd is long. Positive funding is a preferred (but not required) co-condition.
- **Mark price feed** — monitor for mark-vs-oracle divergence that could indicate a cascade is already underway (early exit if cascade starts while entry is still being evaluated).

---

## Example Trade

**Illustrative only — not a backtest.**

Scenario: SOL/USDC-PERP on Hyperliquid, October 2025. SOL has rallied 40% and is now at $185. Coinglass heatmap shows $60M in long liquidations clustered between $158 and $168 (current price $185; cluster starts 2.2 ATR below). Funding is +0.04%/h (longs paying). OI is 145% of 7-day mean. Macro uncertainty event (tariff news) begins suppressing bids.

| Step | Detail |
|---|---|
| **Cluster identified** | $60M longs at $158–$168; price $185; cluster starts 2.2 ATR below |
| **Entry** | Short SOL perp @ $182.50, 4× leverage, isolated margin |
| **Stop** | $191.63 (+5%) |
| **Cascade fires** | Price reaches $168.30; liquidation engine begins forced selling |
| **Cascade extends** | $42M of $60M cluster liquidated; price reaches $157.80 |
| **Partial exit (60%)** | @ $158.50 (price down ~13.1% from entry) at cluster bottom |
| **Overshoot + full exit** | Price extends to $154.70 (down ~15.2%); remaining 40% closed |
| **Net P&L (blended)** | A short profits as price falls — roughly +13.9% on notional |

*A short position profits on a price decline, so the ~13.9% downward move on notional translates to a positive return on the short. Levered 4×, that is roughly +55% on the margin posted over ~2 hours. Position sizing caps the contribution: 5% equity × 4× = 20% of equity deployed; +55% on that ≈ +11% on basket equity for this single trade. **Illustrative only — not a backtest. Costs, funding, and slippage are not included and would reduce the realised figure.***

---

## Performance Characteristics

Estimates are illustrative; naive-backtested only.

- **Return shape:** fast spikes of profit during cascade events; small losses on failed setups. The short-side cascade tends to be faster and more violent than the long-side squeeze — liquidation cascades historically move 1.5–2× further and faster than equivalent squeezes, due to the "falling knife" dynamics of bid withdrawal.
- **Expected Sharpe:** ~1.0, slightly lower than the squeeze basket due to the higher volatility of downside cascades (larger wins, larger losses, similar win rate).
- **Expected max drawdown:** ~32%, higher than the squeeze basket, reflecting the sharper adverse moves if the entry is wrong during a bullish market reversal.
- **Correlation:** negative correlation to [[short-liquidation-squeeze]] (both cannot fire at the same time on the same pair) and to [[crowded-short-funding-fade]] (which is long). Tends to be positively correlated with [[crowded-long-funding-fade]]. In a multi-basket portfolio, this basket provides downside exposure that partially offsets long-biased baskets during cascades.

---

## Capacity Limits

Same constraints as [[short-liquidation-squeeze]]: position must stay below 10% of the targeted cluster notional to avoid self-accelerating the cascade in a detrimental way. Aggregate capacity: **$5M** on major pairs. On mid-caps, $500K–$1M. The short side of cascades has additional slippage risk — when bids disappear during a cascade, closing a large short can be difficult and the final close price may be significantly below the target.

---

## What Kills This Strategy

See [[failure-modes]]:

1. **Bid defence of cluster levels.** A large buyer who specifically enters to defend the cluster level (a whale, an exchange backstop, a protocol treasury) can absorb the liquidation selling without triggering further cascade. The entry stop-loss catches this scenario.
2. **Immediate bounce after cluster fires.** The [[liquidation-cascade-fade]] strategy specifically bets on a sharp bounce after cascades. If the bounce is faster than the basket can exit, the short entered *above* the cluster bounces back above the stop before the target is hit.
3. **Heatmap data latency.** Long positions closed manually before reaching the liquidation threshold leave the heatmap with phantom clusters. If a significant portion of the cluster is manually closed as price approaches, the actual cascade is smaller than expected.
4. **Bid withdrawal → unexpected gap.** During violent cascades, the book can gap significantly below the target. A close below the target generates a larger-than-expected profit but can also make it difficult to close at a clean price if the basket needs to reverse rapidly.
5. **Macro reversal during hold.** A surprise bullish macro catalyst (Fed pivot, ETF approval) during the 4-hour hold can reverse a cascade-in-progress. The stop-loss and time stop handle this, but the loss on a 4× levered short can be significant.

---

## Kill Criteria

Per [[when-to-retire-a-strategy]]:

- **Win rate < 48%** over trailing 20 completed trades.
- **Three consecutive full stop-outs** (> 10% loss on position margin per trade).
- **Drawdown > 28%** on this basket over rolling 6 months.
- **Heatmap data source unavailable** — pause immediately, same as [[short-liquidation-squeeze]].

---

## Advantages

- **Mechanical, predictable selling.** The cascade trigger is non-economic, making it more reliable than sentiment-driven short setups once it fires.
- **Visible entry zone.** Heatmap data gives advance notice of the trigger level.
- **Short holding period.** Capital deployed for minutes to hours.
- **Funding carry bonus.** In positive-funding environments (crowd is long), the short position *collects* funding income during the hold.
- **Portfolio hedge.** The cascade basket fires precisely when long-biased strategies are losing — strong natural portfolio diversification.

---

## Disadvantages

- **Short selling risk.** Short positions have theoretically unlimited loss potential on adverse price moves. The stop-loss is essential but can be gapped through in extreme bull events.
- **Thin bid risk.** During cascades, the bid side of the book evaporates. Closing a large short position at target can cause significant upward slippage if done too aggressively.
- **JELLY-class governance risk (inverse).** Though the JELLY incident hurt *shorts*, governance delists can settle positions at arbitrary prices — monitor Hyperliquid HLP positioning.
- **Cascade immediately faded.** The [[liquidation-cascade-fade]] strategy and similar mean-reversion bots actively bid the bottom of cascades. A very fast bounce can close the cascade window before this basket reaches its target.
- **Not investment advice** — leveraged short selling with concentrated positions.

---

## Hyperliquid Execution Notes

**Mark-price cascade propagation.** Hyperliquid liquidates on *mark price*, not last-trade. The mark price during a cascade lags actual trade execution prices. Monitoring mark price (not last trade) prevents false cascade triggers from single-tick last-price prints.

**ADL risk for profitable shorts.** If Hyperliquid's insurance fund is depleted on the long side during a cascade, profitable short positions (the basket) may be ADL'd — force-closed at the bankruptcy price of the long being liquidated. This is rare but means the basket must be sized conservatively enough that an ADL event does not threaten the overall book. See [[hyperliquid-liquidation-engine]].

**Isolated margin is mandatory.** A cascade that continues beyond the cluster (genuine bear regime) can produce losses far larger than the 5% stop in extreme cases (stop gapping). Isolated margin ensures the loss is bounded to the position, not the full account.

**Exit execution during cascade.** Close short positions with limit orders just inside the bid during the cascade, or use small market chunks to reduce impact. A single large market close during a cascade can move price up significantly (buying into declining bids), slippage worsening the realised P&L.

**[[2025-10-crypto-liquidation-cascade]] reference.** The October 2025 cascade saw $3.21B of forced selling in 60 seconds. This basket would have been active during that event. Key lessons: 1) exits must be pre-set as limit orders (can't react in real time during a 60-second window); 2) the cascade bounced sharply within hours (confirming [[post-liquidation-rebound]] and [[liquidation-cascade-fade]] setups immediately after); 3) slippage on close was significant on small-caps during that window. Source: [[2025-10-crypto-liquidation-cascade]].

**Sibling baskets:** [[short-liquidation-squeeze]] (the mirror long basket riding forced buying upward), [[post-liquidation-rebound]] (the mean-reversion basket that enters after cascades from either direction complete), [[crowded-long-funding-fade]] (the swing-timeframe precursor), [[liquidation-cascade-fade]] (the contrarian fade basket — enters long after this basket would ideally have already exited).

---

## Sources

- [[hyperliquid-liquidation-engine]] — mark-price liquidation mechanics, cascade propagation, ADL.
- [[hyperliquid-funding-rate-microstructure]] — positive funding as crowd-is-long confirmation.
- [[2025-10-crypto-liquidation-cascade]] — empirical large-scale cascade event; timing, volume, and recovery dynamics.
- [[2024-03-hyperliquid-cascade]] — Hyperliquid-specific cascade event reference.
- [[2025-03-jellyjelly-hlp-attack]] — governance intervention precedent; thin-pair dynamics.
- [[liquidation-cascade-fade]] — the contrarian fade; relationship and sequencing.
- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — basket design and regime mapping.
- [[coinglass]] — liquidation heatmap data.
- [[hypurrscan]] — Hyperliquid-native analytics.
- [[edge-taxonomy]], [[failure-modes]] — classification frameworks.

---

## Related

[[hyperliquid]] · [[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[perpetual-futures]] · [[market-regime]] · [[short-liquidation-squeeze]] · [[post-liquidation-rebound]] · [[crowded-long-funding-fade]] · [[liquidation-cascade-fade]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[2025-10-crypto-liquidation-cascade]] · [[2024-03-hyperliquid-cascade]] · [[2025-03-jellyjelly-hlp-attack]] · [[long-liquidation]] · [[liquidation]] · [[open-interest]] · [[leverage]] · [[order-flow]] · [[funding-rate]] · [[atr-position-sizing]] · [[atr-trailing-stop]] · [[coinglass]] · [[hypurrscan]] · [[derivatives-native-regime]] · [[liquidity-depth-regime]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
