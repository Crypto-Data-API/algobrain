---
title: "Cross-Sectional Relative Value (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, quantitative, pairs-trading, momentum, algorithmic, backtesting]
aliases: ["Sector Relative Value", "Perp Pairs Trading", "Long-Short Momentum Basket", "Intra-Sector RV"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[technical-structural-regime]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[momentum-rotation]]", "[[relative-strength]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[open-interest]]", "[[perpetual-futures]]", "[[basis]]", "[[liquidity]]", "[[bid-ask-spreads]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-vault-architecture]]", "[[ai-agent-tokens]]", "[[bitcoin-dominance-rotation]]", "[[when-to-retire-a-strategy]]", "[[atr-position-sizing]]", "[[overfitting-detection]]", "[[crypto-perp-backtesting-pitfalls]]", "[[regime-matrix]]", "[[multi-strategy-portfolio]]", "[[exchange-listing-delisting]]", "[[token-unlock-supply-event]]", "[[meme-coin-cycle]]", "[[coinglass]]", "[[2026-06-03-cryptodataapi-14-basket-regime-framework]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [analytical, structural]
edge_mechanism: "Within a correlated sector (L1s, DeFi, AI tokens), the strongest assets by composite momentum-funding-OI rank consistently outperform the weakest over 5–14 day windows; going long the top quintile and short the bottom quintile within each sector is dollar-neutral to broad crypto direction and profits from the within-sector spread."
data_required: [ohlcv-daily, ohlcv-1h, hyperliquid-perp-funding, hyperliquid-perp-oi, open-interest, bid-ask-spreads, sector-classification, momentum-signals]
min_capital_usd: 25000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 0.8
expected_max_drawdown: 0.18
breakeven_cost_bps: 30
kill_criteria: |
  - rolling 3-month strategy drawdown > 18%
  - rolling 6-month Sharpe < 0.2
  - within-sector spread (long minus short) returns show no autocorrelation at 5-day lag
  - sector correlations converge to > 0.95 (no dispersion left to harvest)
---

# Cross-Sectional Relative Value (Hyperliquid Basket)

A market-neutral (within-sector) long-short perpetual basket that ranks assets within a defined crypto sector — L1 blockchains, DeFi protocols, AI-agent tokens — by a composite of momentum, funding rate, and open-interest signals, then goes long the top quintile and short the bottom quintile of the ranking. The bet is on within-sector dispersion: the spread between outperformers and underperformers, not the direction of the sector as a whole. Broad crypto market moves cancel across the long-short book; the edge lives in the ranking signal's ability to identify durable relative trends before they fully resolve.

> **Not investment advice.** This is a design document for a systematic strategy. All performance figures are illustrative estimates, not backtest results.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Analytical + structural** (see [[edge-taxonomy]]).

- **Analytical** — the composite ranking (momentum + funding signal + OI momentum) combines three signals that have independent theoretical motivations: price momentum captures trend persistence; funding rate captures the positioning imbalance between leveraged longs and shorts; OI growth captures conviction behind a directional move vs. the broader sector. A composite score is more robust than any single factor.
- **Structural** — within a correlated sector, assets share macro drivers but differ on idiosyncratic factors (protocol-specific news, liquidity profile, developer activity, token unlock schedules). Dispersion across otherwise-correlated assets tends to mean-revert over 10–30 day windows, creating a systematic spread that patient, dollar-neutral positioning can harvest. The structural driver is the same logic underlying [[pairs-trading]] and [[statistical-arbitrage]] but applied cross-sectionally within crypto sectors rather than to a single pair.

## Why This Edge Exists

1. **Within-sector correlation is imperfect.** L1 tokens (SOL, AVAX, SUI, etc.) are correlated at the macro level (BTC risk-on/off drives all of them) but diverge substantially at the sector level based on developer adoption, throughput metrics, narrative heat, and token economics. The same is true for DeFi protocols (AAVE vs COMP vs UNI) and AI-agent tokens (see [[ai-agent-tokens]] for an example sector). A ranked dispersion position removes the macro correlation and isolates the idiosyncratic spread.
2. **Momentum persists at the sector-relative level.** Empirical evidence in equities (Fama-French, Jegadeesh-Titman) and in crypto (multiple academic studies) shows that recent relative outperformers within a sector tend to continue outperforming over 5–20 day windows. This is driven by underreaction to idiosyncratic news, capital rotation from sector-level thesis buyers, and reflexive momentum (rising relative price attracts more capital to that name within the sector).
3. **Funding rate is a positioning signal.** On Hyperliquid, the funding rate measures the imbalance between levered longs and shorts in real time. An asset within a sector that has persistently high positive funding (longs paying heavily) is likely to mean-revert — the overextended long position unwinds, dragging price relative to its peers. Conversely, deeply negative funding within a sector signals a crowded short that may cover, outperforming peers. Incorporating funding into the ranking turns a pure momentum signal into a positioning-adjusted momentum signal. Source: [[hyperliquid-funding-rate-microstructure]].
4. **OI momentum confirms conviction.** Rising OI into a price move (within the sector) confirms that new money is entering on the directional side; falling OI into a price move suggests the move is driven by position liquidation rather than new buying, and is less likely to persist. OI context allows the ranking to separate "conviction outperformers" from "short-squeeze survivors."
5. **Dollar-neutral construction reduces regime dependence.** Because the basket is long-short within each sector (equal dollar notional on long and short legs), broad market rallies and sell-offs cancel out in P&L terms. The strategy's return is largely independent of whether BTC is in a bull, bear, or chop regime — it depends only on the ranking signal's validity. This differentiates it from every other basket in the basket library, most of which carry directional market exposure.
6. **Counterparty analysis.** The underperformers that the basket shorts are held by: (a) passive index investors who rebalance slowly; (b) narratively-driven retail who chase the sector story without differentiating within it; (c) long-only funds that are fully invested in the sector and cannot easily reduce the weakest names. These holders do not respond to within-sector relative signals quickly enough to arb the spread.

This strategy is the perps cousin of [[pairs-trading]] and [[statistical-arbitrage]], applied cross-sectionally. Unlike a bilateral pair trade (e.g., SOL vs AVAX), which is exposed to the specific relationship between two assets, a cross-sectional portfolio of ranked pairs is diversified across the ranking signal's overall validity and is less vulnerable to a single pair relationship breaking down.

## Null Hypothesis

Under no-edge conditions, within-sector asset returns are random after removing the sector-common factor — the ranking signal (momentum + funding + OI) has no predictive power for the next 5–14 day within-sector spread. The top-quintile and bottom-quintile portfolios produce identical sector-relative returns, and any observed historical edge is in-sample overfitting.

**Disconfirming evidence to watch:**

- Within-sector spread (top-quintile return minus bottom-quintile return) shows no positive autocorrelation at the 5-day and 10-day lag in rolling 90-day windows — momentum is not persisting.
- Funding-adjusted ranking adds no incremental predictive power over pure momentum ranking (test this monthly; if the composite score is no better than a pure 14-day return sort, simplify or reweight).
- Sector correlations spike to > 0.95 during a risk-off event and stay elevated for > 30 days — no dispersion to harvest; suspend the strategy.
- Transaction costs consume > 80% of gross spread over a 3-month rolling window — edge is insufficient to cover friction at current sector liquidity.

## Rules

**Sector definitions (starting point — refine as markets evolve):**

| Sector | Example tokens with Hyperliquid perps |
|--------|--------------------------------------|
| L1 Blockchains | SOL, AVAX, SUI, APT, NEAR, TON |
| DeFi Protocols | AAVE, UNI, CRV, GMX, DYDX, JUP |
| AI / Agent Tokens | WLD, TAO, FET, RNDR, AGIX (see [[ai-agent-tokens]]) |
| Layer 2s | ARB, OP, MATIC, STRK, MANTA |
| Infrastructure / Oracles | LINK, PYTH, API3, BAND |

**Minimum sector size:** at least 4 assets with liquid Hyperliquid perps (> $3M daily volume each) to form a viable ranking.

**Composite ranking score (per asset, per sector):**

```
score = w_mom * momentum_score + w_fund * funding_score + w_oi * oi_score
```

Default weights: `w_mom = 0.50, w_fund = 0.25, w_oi = 0.25`. Tune monthly with walk-forward validation; see [[overfitting-detection]] and [[crypto-perp-backtesting-pitfalls]].

- **Momentum score:** rank of 14-day total return (price only) within sector. Rank 1 = worst, rank N = best. Normalize to [0, 1].
- **Funding score:** rank of average 8h funding rate over the past 7 days, *inverted* (high positive funding = overextended longs = future underperformance; rank lowest). Normalize to [0, 1].
- **OI score:** rank of 14-day OI change as a percentage of beginning-of-period OI. Rising OI confirms conviction. Normalize to [0, 1].

**Rebalancing cadence:** weekly (every 7 days), or upon a > 2 rank-position change for any asset in the current portfolio.

**Construction:**
- Long top quintile (or top 2 assets in a small sector); short bottom quintile (or bottom 2 assets).
- Dollar-neutral within each sector: total long notional = total short notional.
- Leverage: 2–3x per leg (both long and short), isolated margin per leg.
- Per-sector allocation: 1–3% of book on each side (long + short).

**Exit rules:**
- Hold until the weekly rebalance unless a position drops out of its quintile mid-cycle (rank changes by > 2 positions → trim or exit).
- Stop-loss: if a single leg moves > 20% against the position within 5 days, exit that leg.
- Funding exit: if the funding rate on a short leg turns persistently < −0.08% / 8h, cover — the market is paying you to be short but the squeeze risk has increased materially.

## Implementation Pseudocode

```python
SECTORS = {"L1": [...], "DeFi": [...], "AI": [...], "L2": [...], "Infra": [...]}
WEIGHTS = {"mom": 0.50, "fund": 0.25, "oi": 0.25}
REBAL_DAYS = 7
MIN_SECTOR_SIZE = 4
MIN_DAILY_VOL = 3_000_000
MAX_LEV = 3
SECTOR_BOOK_PCT = 0.02      # 2% of book per sector side (long or short)

def rank_sector(tokens, state):
    ranked = []
    for tok in tokens:
        if hl_daily_volume(tok) < MIN_DAILY_VOL:
            continue
        mom  = price_return(tok, days=14)
        fund = mean_funding(tok, hours=7*24)  # lower = better for long
        oi   = oi_change_pct(tok, days=14)

        # Normalize within sector later; collect raw values
        ranked.append({"token": tok, "mom": mom, "fund": fund, "oi": oi})

    if len(ranked) < MIN_SECTOR_SIZE:
        return None

    # Rank and normalize each signal within the sector
    for sig in ("mom", "oi"):
        vals = [r[sig] for r in ranked]
        for r in ranked:
            r[f"{sig}_rank"] = percentile_rank(r[sig], vals)

    for r in ranked:
        # Funding: invert — high positive funding is bad for longs
        r["fund_rank"] = 1.0 - percentile_rank(r["fund"], [x["fund"] for x in ranked])

    for r in ranked:
        r["score"] = (WEIGHTS["mom"]  * r["mom_rank"] +
                      WEIGHTS["fund"] * r["fund_rank"] +
                      WEIGHTS["oi"]   * r["oi_rank"])

    return sorted(ranked, key=lambda x: x["score"], reverse=True)

def build_sector_book(sector_name, tokens, book_size, state):
    ranked = rank_sector(tokens, state)
    if ranked is None:
        return []

    n = len(ranked)
    top    = ranked[:max(1, n // 5)]    # top quintile
    bottom = ranked[-(max(1, n // 5)):]  # bottom quintile

    size_per_leg = SECTOR_BOOK_PCT * book_size
    legs = []
    for asset in top:
        legs.append(long_perp(
            asset["token"],
            size=size_per_leg / len(top),
            leverage=MAX_LEV, margin="isolated",
            stop_loss_pct=0.20,
            hold_days=REBAL_DAYS
        ))
    for asset in bottom:
        legs.append(short_perp(
            asset["token"],
            size=size_per_leg / len(bottom),
            leverage=MAX_LEV, margin="isolated",
            stop_loss_pct=0.20,
            funding_exit_threshold=-0.0008,
            hold_days=REBAL_DAYS
        ))
    return legs

def rebalance_all_sectors(state, book_size):
    all_legs = []
    for sector_name, tokens in SECTORS.items():
        all_legs += build_sector_book(sector_name, tokens, book_size, state)
    return all_legs
```

## Indicators / Data Used

- **14-day momentum (price return)** — OHLCV daily close from Hyperliquid or CoinGecko, point-in-time. The backbone of the ranking signal.
- **Funding rate (7-day average, 8h intervals)** — from Hyperliquid API (`metaAndAssetCtxs`, `predictedFundings`). The positioning-imbalance signal. Source: [[hyperliquid-funding-rate-microstructure]].
- **OI change (14-day %)** — from Hyperliquid on-chain OI data. The conviction-confirmation signal. High OI growth into a price move = conviction; low or falling OI = short-squeeze or passive drift.
- **Daily trading volume (Hyperliquid perp)** — liquidity gate; ensures only assets with meaningful market depth enter the ranking.
- **Bid-ask spread (snapshot)** — for cost estimation at rebalance time; if spread > 30 bps on entry, defer rebalance until liquidity improves. See [[bid-ask-spreads]].
- **Relative strength (sector-adjusted)** — computed internally as the momentum score adjusted for the sector mean return; isolates the idiosyncratic component. Source: [[relative-strength]].
- **Coinglass** — cross-venue OI and funding data to confirm Hyperliquid signals are not outliers relative to Binance/Bybit. Source: [[coinglass]].
- **Bitcoin dominance** — a rising BTC dominance (see [[bitcoin-dominance-rotation]]) tends to compress intra-sector dispersion as capital flows from alts to BTC; monitor as a strategy-level filter.

## Example Trade

**Illustrative — not a backtest.** Intra-L1 sector trade.

| Asset | 14d Return | Avg Funding | OI Change | Composite Score | Position |
|-------|-----------|-------------|-----------|-----------------|----------|
| SOL | +18% | +0.02%/8h | +35% | 0.88 | **Long** |
| SUI | +14% | +0.01%/8h | +20% | 0.76 | **Long** |
| TON | +2% | +0.04%/8h | −5% | 0.52 | Neutral |
| NEAR | −8% | +0.08%/8h | +10% | 0.31 | Neutral |
| AVAX | −15% | +0.12%/8h | −20% | 0.12 | **Short** |

- **Entry:** Long SOL + SUI equally; Short AVAX. Dollar-neutral (long notional = short notional). 3x leverage, isolated margin per leg.
- **Holding period:** 7 days.
- **Outcome over 7 days (illustrative):** Sector (L1 basket) +4% (BTC rally lifts all L1s). SOL +12%, SUI +8%, AVAX +2%.
- **Spread capture:** Long book up +10% weighted; short book up +2% → spread P&L = +8% on 3x = +24% on capital deployed per side, less costs.
- **Gross P&L on 2% allocation each side:** +24% × 2% book = +0.48% of book. After 70 bps round-trip cost: ~+0.34% of book net.
- **Note:** the absolute +4% sector move cancels (long and short both go up, but long goes up more). Market-neutrality confirmed within the sector.

## Performance Characteristics

*Illustrative estimates — not derived from live or backtest results.*

- **Return distribution:** more normally distributed than event-driven baskets; no large spikes but more consistent non-zero returns across rebalancing periods. Approximately 55–65% of weekly rebalances produce positive spread P&L.
- **Expected Sharpe:** ~0.8 net. This is the highest Sharpe estimate of the four event/idiosyncratic baskets because the edge is diversified across multiple sector pairs simultaneously, reducing variance. However, the absolute P&L per rebalance is modest.
- **Expected max drawdown:** ~18% — most likely from a period of extreme sector correlation (all assets move together; no spread to harvest) or from a breakdown in the momentum signal (momentum reversal regime).
- **Funding carry:** can be positive (earn funding on short legs when longs are overextended) or negative (pay on long legs that have high funding) — net funding is unpredictable and treated as noise in the return estimate.
- **Transaction cost sensitivity:** the breakeven cost of 30 bps round trip is tight for a weekly-rebalanced strategy with 5–10 positions. Crossing the spread on illiquid perps (> 30 bps) will consume the edge. This is the primary operational risk.
- **Regime sensitivity:** the strategy is designed to be regime-neutral by construction, but it is most effective in [[technical-structural-regime]] chop environments where within-sector dispersion is high. In strong trending regimes (bull or bear), within-sector dispersion compresses as correlations spike.

## Capacity Limits

The cross-sectional RV basket has higher capacity than the event-driven strategies because it is diversified across many assets simultaneously. Per-sector capacity is approximately $5–15M per side (limited by the thinnest asset in the bottom quintile, which sets the position size ceiling). With 4–5 active sectors, total strategy capacity is approximately **$50M** before market impact degrades the rebalancing cost materially. The strategy is not liquidity-constrained by any single event; it scales with the number of viable sectors and assets on Hyperliquid. As Hyperliquid lists more perps, capacity grows naturally.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Sector correlation spike.** In a severe risk-off event (flash crash, black swan), all assets within a sector — and across sectors — become highly correlated. Long and short legs move together, and the spread is zero. The strategy earns nothing (or worse, the short squeezes while the long dumps if the correlation break is asymmetric). Monitor via [[bitcoin-dominance-rotation]] and cross-sector correlation.
2. **Momentum reversal / factor crash.** Short-term momentum factors periodically crash — a period where prior underperformers dramatically outperform. The bottom-quintile short gets squeezed while the top-quintile long underperforms. This is the classic "factor unwind" risk in quantitative investing. See [[overfitting-detection]].
3. **Funding signal breakdown.** The funding rate is a reliable positioning signal in normal conditions but can give false signals during extreme market events (e.g., funding stays positive on a collapsing asset because shorts are being liquidated faster than they are entering). Calibrate the weighting of the funding signal during regimes with high liquidation cascades ([[2025-10-crypto-liquidation-cascade]]).
4. **Sector classification staleness.** The AI-agent token sector of 2024 looks very different from 2026; assets migrate between sectors as narratives evolve. A stale sector classification will produce noisy rankings. Review sector membership monthly.
5. **Thin-perp liquidity.** If a bottom-quintile asset has low OI on Hyperliquid, the short position can be squeezed by a small coordinated spot bid (JELLY pattern — [[2025-03-jellyjelly-hlp-attack]]). The $3M daily volume gate reduces but does not eliminate this risk.
6. **Overfitting in the composite score.** The signal weights (0.50 / 0.25 / 0.25) are a starting point, not an optimized result. Excessive tuning to historical data produces a strategy that fails out-of-sample. See [[overfitting-detection]] and [[crypto-perp-backtesting-pitfalls]].
7. **High rebalancing costs in volatile markets.** During high-volatility periods, bid-ask spreads widen and the cost per rebalance can exceed 100 bps round trip — well above the 30 bps breakeven. The strategy should pause rebalancing when spreads are elevated.

## Kill Criteria

Numeric kill rules (see [[when-to-retire-a-strategy]]):

- Rolling 3-month strategy drawdown > **18%** → stop new rebalances; full review.
- Rolling 6-month Sharpe < **0.2** → edge has decayed below the cost of operation; retire or rebuild.
- Within-sector spread returns show no positive autocorrelation at the 5-day lag over a 90-day rolling window → momentum signal has stopped working; retire the momentum leg; retest with funding-only ranking.
- Sector correlations exceed **0.95** for > 30 consecutive days → no dispersion to harvest; suspend until correlations normalize.
- Average round-trip cost per rebalance > **80 bps** over a 30-day window → strategy is cost-negative; suspend until liquidity improves.

## Hyperliquid Execution Notes

**Thin-perp risk on short legs.** The bottom-quintile of any sector ranking often contains the weakest, lowest-liquidity tokens — exactly the thin-perp profile that generated the JELLY squeeze ([[2025-03-jellyjelly-hlp-attack]]). The $3M daily volume gate filters the worst cases, but within a small sector (4–6 assets) the "worst" asset may still be lightly traded. Use isolated margin on every short leg; hard stop at +20% from entry; prefer maker-side entries when available to reduce market impact.

**ADL risk on the long legs.** If a short-squeezed counterparty is liquidated, Hyperliquid's auto-deleveraging mechanism (ADL) may close the most profitable long position in the system at the bankruptcy price. This would close a long leg that is winning (because the sector is rallying) at an unfavorable price. Size long positions so that the ADL loss is < 0.5% of book in the worst case. Source: [[hyperliquid-liquidation-engine]].

**Funding rate as a real-time rebalancing input.** Rather than rebalancing purely on a weekly calendar, monitor funding rates continuously (hourly). If the funding on a long leg exceeds +0.15% / 8h (> 65% annualized carry cost), the position is expensive to hold and the ranking may be signaling future underperformance — consider early rebalancing. If a short leg's funding turns < −0.10% / 8h, that asset is potentially due for a bounce — consider covering early rather than holding through the squeeze.

**Dollar-neutral verification on-chain.** Hyperliquid provides transparent OI data per asset. After each rebalance, verify that the long-side and short-side notional values are within 5% of each other across the sector portfolio. Drift above 10% is a sign of fill imbalance and should be corrected.

**Marking to portfolio value.** Because the strategy holds multiple legs simultaneously across sectors, use Hyperliquid's account portfolio view (see [[hyperliquid-vault-architecture]]) to monitor the cross-leg P&L in aggregate. A leg that looks like a winner on its own may be masking losses elsewhere in the portfolio.

## Advantages

- Market-neutral within sectors — the most regime-independent basket in the basket library; earns in bull, bear, and chop.
- Diversified across multiple simultaneous positions; no single event drives P&L.
- Both the long and short legs are individually motivated by the composite ranking — not just a hedge.
- Funding as a signal and cost-capture opportunity: well-ranked assets often have attractive funding carry.
- Scalable: capacity grows as Hyperliquid lists more perps in more sectors.
- Can be combined cleanly with directional baskets in the broader [[multi-strategy-portfolio]] because it adds near-zero net directional exposure.

## Disadvantages

- The highest operational complexity in the event/idiosyncratic cluster: requires continuous data feeds, composite ranking computation, and weekly rebalancing across multiple sectors.
- Transaction costs are the primary adversary — 30 bps breakeven is tight; any execution degradation erodes edge rapidly.
- Sector correlation spikes suspend the strategy entirely with little warning.
- Momentum factor crashes are historically sharp, sudden, and hard to detect in advance.
- Requires careful overfitting discipline on signal weights — a risk that exists every time the weights are re-examined.
- The strategy is not designed to produce large absolute returns; it is a Sharpe-enhancer for the broader book.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — derivatives-native and technical-structural regime classification; basket framework
- [[pairs-trading]] — bilateral pairs trading foundation; the cross-sectional approach generalises this to N assets
- [[statistical-arbitrage]] — the formal statistical framework underlying cross-sectional RV
- [[momentum-rotation]] — momentum factor persistence evidence and decay patterns
- [[relative-strength]] — relative strength calculation and sector-adjusted momentum
- [[hyperliquid-funding-rate-microstructure]] — HL funding mechanics; funding as a positioning signal
- [[hyperliquid-liquidation-engine]] — ADL mechanics and thin-perp risks
- [[overfitting-detection]] — guidance on avoiding in-sample overfitting on signal weights
- [[crypto-perp-backtesting-pitfalls]] — backtesting hazards specific to perpetual futures
- [[ai-agent-tokens]] — example of a sector with significant cross-sectional dispersion
- [[coinglass]] — cross-venue OI and funding for corroboration
- [[2025-03-jellyjelly-hlp-attack]] — thin-perp short-squeeze case study

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[hyperliquid]] · [[pairs-trading]] · [[statistical-arbitrage]] · [[momentum-rotation]] · [[relative-strength]] · [[funding-rate]] · [[funding-rate-arbitrage]] · [[open-interest]] · [[perpetual-futures]] · [[basis]] · [[market-regime]] · [[derivatives-native-regime]] · [[technical-structural-regime]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-vault-architecture]] · [[ai-agent-tokens]] · [[bitcoin-dominance-rotation]] · [[overfitting-detection]] · [[crypto-perp-backtesting-pitfalls]] · [[regime-matrix]] · [[multi-strategy-portfolio]] · [[exchange-listing-delisting]] · [[token-unlock-supply-event]] · [[meme-coin-cycle]] · [[breadth-and-momentum-divergence]] · [[breakout-and-retest]] · [[crowded-short-funding-fade]] · [[defensive-majors]] · [[distribution-post-peak-short-book]] · [[coinglass]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]] · [[2026-06-03-cryptodataapi-14-basket-regime-framework]]
