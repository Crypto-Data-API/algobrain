---
title: "Bar Resolution Selection"
type: concept
created: 2026-06-02
updated: 2026-06-11
status: good
tags: [backtesting, methodology, market-microstructure, crypto, derivatives]
aliases: ["Bar Resolution", "Timeframe Selection", "Candle Resolution", "1m vs 5m vs 15m"]
domain: [backtesting, market-microstructure]
difficulty: advanced
related: ["[[intrabar-fill-modeling]]", "[[multiple-timeframe-analysis]]", "[[microstructure-noise-low-timeframe]]", "[[overfitting]]", "[[crypto-perp-backtesting-pitfalls]]", "[[execution-model-differences]]", "[[slippage-modeling]]", "[[scalping]]", "[[hyperliquid]]", "[[hyperliquid-funding-rate-microstructure]]", "[[perpetual-futures]]", "[[day-trading-overview]]"]
---

# Bar Resolution Selection

Bar resolution is the time width of each candle a strategy is sampled on — 1-minute, 3-minute, 5-minute, 15-minute, and so on. On a low-timeframe crypto-perpetual book the choice between 1m, 3m, 5m, and 15m is one of the most consequential and most quietly overfit decisions in the entire backtest: it silently sets the signal-to-noise ratio, the number of independent bets, the severity of [[intrabar-fill-modeling|intrabar fill ambiguity]], and whether the edge clears cost at all. Most low-timeframe perp strategies that "work in backtest and die live" died at the resolution-selection step, not at the signal step.

## The Core Trade-Off

Bar resolution trades granularity against noise, and trades degrees of freedom against robustness. There is no free lunch in either direction.

Finer bars (1m, 3m) buy:
- **More signal granularity** — entries and exits land closer to the actual turn; stops can sit tighter against structure.
- **More bars to fit** — and that is the problem. More bars means more chances to curve-fit a rule to the specific noise of one history (see [[overfitting]]). A 1m strategy sees ~1440 bars/day; a parameter that "works" across that many bars can still be fitting bid-ask bounce.
- **Lower signal-to-noise.** At 1m the candle's body is often dominated by [[microstructure-noise-low-timeframe|microstructure noise]] — bid-ask bounce, fleeting depth, single large prints — rather than directional information.
- **Higher sensitivity to fill assumptions.** When the true move per bar is small, the difference between fill-at-close and fill-at-next-open ([[execution-model-differences]]), or the [[intrabar-fill-modeling|high-or-low-first]] ordering of a stop and target inside one candle, becomes a large fraction of the move.

Coarser bars (5m, 15m) buy:
- **More stable signal** — each candle aggregates more order flow, so the directional component dominates the noise component.
- **Fewer, more independent trades** — fewer chances to overfit, but also fewer bets, which lengthens the time needed to reach statistical significance.
- **Proportionally more expensive fill errors in absolute terms** — but only because each trade is larger; relative to the per-trade edge, fill errors hurt less because the edge is bigger.
- **Stops that sit further away** — a structure-based stop on a 15m bar is wider, so position size per unit risk is smaller, and a single bad bar costs more.

## Resolution-by-Resolution

| Resolution | Bars/day | Typical use | Noise level | Intrabar ambiguity | Overfitting risk | Funding cycles per bar (HL, hourly) | Round-trip cost vs typical bar range |
|---|---|---|---|---|---|---|---|
| **1m** | 1440 | High-frequency scalps, [[scalping|scalping]], microstructure signals | Very high — body often < spread on alts | Severe; stop+target frequently in same bar | Very high (huge bar count) | 1 funding event per ~60 bars | Cost ~4–8 bps vs ~3–8 bps range → cost ≈ the move |
| **3m** | 480 | Fast intraday, momentum bursts | High | High | High | 1 per ~20 bars | Cost ~4–8 bps vs ~6–15 bps range → cost eats ~half |
| **5m** | 288 | Intraday trend/entry, common scalp baseline | Moderate | Moderate | Moderate | 1 per ~12 bars | Cost ~4–8 bps vs ~10–25 bps range → cost ~30–50% |
| **15m** | 96 | Intraday swing, [[multiple-timeframe-analysis|entry TF under an H1/H4 bias]] | Low–moderate | Low | Lower (fewer bars) | 1 per ~4 bars | Cost ~4–8 bps vs ~15–40 bps range → cost ~15–30% |

The numbers are order-of-magnitude for a liquid BTC/ETH perp in a normal-vol regime; alt-perps shift every "noise" and "cost vs range" cell sharply worse. The structural point holds regardless of the exact figures: **bars/day quadruples from 15m to 5m and is 15x at 1m, while round-trip cost is roughly fixed and bar range shrinks roughly with resolution.**

## Crypto-Perp / Hyperliquid Specifics

Three features of crypto perps, and Hyperliquid in particular, change the resolution calculus relative to equities.

- **Hourly funding.** Hyperliquid posts and pays funding every hour, versus the 8-hour cycle on most CEXs ([Hyperliquid docs](https://hyperliquid.gitbook.io/hyperliquid-docs); see [[hyperliquid-funding-rate-microstructure]]). On a 1m chart a position spans one funding event roughly every 60 bars; on 15m, every 4 bars. A backtest that ignores funding is wrong at every resolution, but the *frequency* of the correction scales with bar width — coarser bars cross more funding boundaries per held trade, so funding becomes a first-order PnL term faster.
- **24/7 trading, no session reset.** Equity intraday strategies get a free denoising boundary every day — the overnight gap and the open auction reset stale orders and re-anchor price. Perps have none of this. There is no session to batch by, no open to denoise on, so noise that an equity strategy sheds at the daily boundary stays in the perp series at every resolution.
- **Event-time data below 1m.** Hyperliquid exposes L2 book snapshots and a trade/fills feed ([Hyperliquid docs](https://hyperliquid.gitbook.io/hyperliquid-docs)), which enables work in *event time* (trades, book updates) rather than clock time, and supports realistic [[intrabar-fill-modeling|intrabar fill modeling]] below the 1m bar. This is the principled escape hatch: if a signal genuinely lives below 1m, model it on the trade/book feed with explicit fills, not on a 1m OHLC candle that hides the within-bar path.
- **Bid-ask bounce on 1m alt-perps.** On a thin Hyperliquid alt-perp, the 1m candle's true range can be a large fraction bid-ask bounce — the high and low are the two sides of the book rather than directional extent. A "breakout of the 1m high" on such a contract is frequently a breakout of the offer, not of anything informative (see [[microstructure-noise-low-timeframe]]).

## The Nyquist / Signal-vs-Cost Argument

The governing constraint is simple: **the edge must clear cost on every bar the strategy actually trades.** Holding period and bar width are linked, and cost does not shrink when the bar does.

As resolution drops from 15m toward 1m, the typical per-bar price range shrinks roughly linearly with the time width, but the round-trip cost — spread + taker/maker fees + [[slippage-modeling|slippage]] — is approximately fixed in basis points. So the ratio of edge to cost collapses.

A worked illustration on BTC perp in a normal-vol regime:

- **15m bar:** typical true range ≈ 0.15–0.40% (15–40 bps). Round-trip cost ≈ 4–8 bps. Even a strategy that captures a third of the bar's range nets ~5–13 bps before cost, ~−3 to +9 bps after. Marginal but workable.
- **1m bar:** typical true range ≈ 0.03–0.08% (3–8 bps). Round-trip cost ≈ 4–8 bps — *unchanged*. Now the cost is on the order of the entire bar's range. A strategy must capture nearly all of the bar's directional extent, repeatedly, just to break even. That is not a real edge; it is a coin flip against a fixed tax.

This is the resolution analog of a sampling argument: pushing to finer bars to "see more" buys mostly noise (the signal you wanted was already present at coarser resolution), while the fixed cost-per-trade tax compounds against you on every additional bar you trade. Finer is not more information; it is more cost.

## How to Actually Choose

1. **Start from the edge's economics, not from a default chart.** Estimate the signal's economic half-life — how long the inefficiency persists — and pick the *coarsest* bar that still captures it. If the edge plays out over ~30–60 minutes, 5m or 15m captures it; 1m just adds noise and cost.
2. **Demand a 3x cost cushion.** On the chosen resolution, require the modeled per-trade edge to clear roughly 3x the modeled round-trip cost (spread + fees + slippage + a funding allowance). An edge that only clears 1–1.5x cost in backtest is negative live once costs are honest (see [[crypto-perp-backtesting-pitfalls]], [[slippage-modeling]]).
3. **Test robustness across adjacent resolutions.** Run the same logic at 1m, 3m, 5m, and 15m. A genuine edge degrades *gracefully* across neighbors. A strategy that prints at 1m and dies at 3m/5m is almost certainly fitting microstructure noise — the resolution is the parameter, and it is overfit (see [[overfitting]]).
4. **Use multi-timeframe structure instead of one ultra-fine bar.** Take directional bias from a higher timeframe (H1/H4) and time entries on a lower one (5m/15m), rather than asking a single 1m series to carry both bias and execution ([[multiple-timeframe-analysis]], [[day-trading-overview]]). This separates the slow, robust signal from the fast, cost-sensitive trigger.

## Common Mistakes

- **Defaulting to 1m because "more data is better."** More bars is more noise and more cost, not more information. The right default is the coarsest resolution that captures the signal.
- **Ignoring intrabar ambiguity multiplication.** Finer bars multiply the [[intrabar-fill-modeling|high-or-low-first]] problem: more bars contain both the stop and the target, and each one forces an assumption the live market does not honor.
- **Reporting Sharpe without noting bars-per-year inflation.** A 1m strategy books ~525,600 bars/year versus ~35,040 at 15m. Annualization and significance tests that assume independent observations badly overstate confidence when bars are autocorrelated noise; the inflated bar count flatters the Sharpe.
- **Resolution-shopping.** Trying all four resolutions and keeping the best is a textbook in-sample search over an undeclared parameter — a direct form of [[overfitting]]. If resolution is searched, it must be inside walk-forward folds and counted against the degrees-of-freedom budget, not picked by hindsight.

## Sources

- [[crypto-perp-backtesting-pitfalls]] — funding, slippage, and 24/7 hazards that interact with resolution choice.
- [[hyperliquid-funding-rate-microstructure]] — hourly funding cadence and its per-bar implications.
- [[intrabar-fill-modeling]] — within-bar path ambiguity that worsens at finer resolutions.
- [[microstructure-noise-low-timeframe]] — bid-ask bounce and noise dominance on 1m bars.
- [[slippage-modeling]], [[execution-model-differences]], [[overfitting]], [[multiple-timeframe-analysis]] — methodological inputs.
- Hyperliquid documentation: https://hyperliquid.gitbook.io/hyperliquid-docs (hourly funding, L2 book snapshots, trade/fills feed).
- [[2026-04-22-gap-finder-hyperliquid-crypto-perpetual-exchange-lo]] — gap-finder report identifying Hyperliquid low-timeframe backtesting coverage gaps.

## Related

- [[intrabar-fill-modeling]]
- [[multiple-timeframe-analysis]]
- [[microstructure-noise-low-timeframe]]
- [[overfitting]]
- [[crypto-perp-backtesting-pitfalls]]
- [[execution-model-differences]]
- [[slippage-modeling]]
- [[scalping]]
- [[hyperliquid]]
- [[hyperliquid-funding-rate-microstructure]]
- [[perpetual-futures]]
- [[day-trading-overview]]
