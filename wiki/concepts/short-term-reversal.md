---
title: "Short-Term Reversal"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [mean-reversion, quantitative, anomalies, market-microstructure, stocks]
aliases: ["Short Term Reversal", "Short-Horizon Reversal", "Weekly Reversal", "Lehmann Reversal"]
related: ["[[mean-reversion]]", "[[momentum]]", "[[statistical-arbitrage]]", "[[liquidity]]", "[[market-microstructure]]", "[[pairs-trading]]", "[[idiosyncratic-volatility-anomaly]]"]
domain: [market-microstructure, behavioral-finance]
prerequisites: ["[[mean-reversion]]", "[[liquidity]]"]
difficulty: intermediate
---

Short-term reversal is the empirical regularity that stocks which outperform over a very short horizon (one day to one month, most classically one week) tend to *underperform* over the subsequent period, and vice versa. It is the short-horizon mirror image of [[momentum]] (which operates at 3-12 month horizons) and is widely interpreted as compensation for providing liquidity to traders who demand immediacy. The effect was documented by Lehmann (1990) and Jegadeesh (1990) and remains one of the most robust patterns in the cross-section of equity returns, though it is heavily eroded by transaction costs.

## Overview

The signal is mechanically simple. Rank stocks by their return over a recent short window (e.g. the past 5 trading days or the past month), buy the past losers, short the past winners, and hold for a similarly short window. A typical academic construction:

```
# weekly reversal, long-short
rank stocks by return over the past 5 trading days
short the top decile (recent winners)
long  the bottom decile (recent losers)
hold 1 week, then rebalance
```

The raw long-short spread in academic studies is large — Lehmann (1990) reported gross weekly profits of roughly 1.5-2% on a zero-cost portfolio using one-week formation and holding periods — but these are *before* trading costs, and the turnover is extreme (effectively 100% per week or more).

## Why the effect exists

There are two complementary explanations, and both matter for trading:

1. **Liquidity provision / price pressure (microstructure).** When an investor demands immediacy — a large order that must be filled now — they push the price away from fair value. Market makers and reversal traders supply that liquidity and are compensated when the price reverts. The reversal premium is, on this view, the *bid-ask bounce and inventory-risk premium* paid to liquidity suppliers (Grossman-Miller, Nagel 2012). Crucially, the reversal premium *rises sharply when liquidity is scarce* — Nagel (2012) showed that short-term reversal returns spike during high-VIX periods, behaving like the expected return to a market-making strategy.
2. **Overreaction (behavioral).** Investors overreact to recent news and order flow, and prices correct as the overreaction fades. This is the [[behavioral-finance|behavioral]] reading and overlaps with the [[mean-reversion]] literature.

The microstructure reading dominates the modern interpretation because it explains the *time variation*: reversal is most profitable exactly when liquidity is most expensive.

## Relationship to other effects

- **Momentum.** [[momentum]] works at intermediate horizons (3-12 months); short-term reversal works at 1-day to 1-month horizons. Standard momentum constructions deliberately *skip the most recent month* precisely to avoid contamination by short-term reversal.
- **Long-term reversal.** Over 3-5 year horizons, a separate reversal effect appears (De Bondt-Thaler 1985), driven by long-run overreaction to fundamentals rather than liquidity.
- **Idiosyncratic volatility.** Reversal is strongest in high-[[idiosyncratic-volatility-anomaly|idiosyncratic-volatility]], small, illiquid names — the same stocks where liquidity provision is most expensive.

## Trading relevance

Short-term reversal is the canonical example of a "real but uncapturable" anomaly for most participants:

- **Turnover and costs dominate.** With weekly or daily rebalancing, round-trip costs of even 10-20 bps can wipe out the entire gross edge. The strategy only survives net of costs for participants with very low marginal trading costs (statistical-arbitrage desks, high-frequency market makers) or who implement it as a *queue-position / execution overlay* rather than a standalone alpha.
- **It is effectively a market-making strategy.** Because the premium is liquidity provision, capturing it requires either being the passive side of trades (resting limit orders) or trading the least-liquid names where the premium is large enough to overcome costs.
- **Regime sensitivity.** The edge is largest in stressed, illiquid markets — but those are also when execution risk and adverse selection are highest. Sizing must scale down, not up, when realized volatility spikes despite the higher gross premium.
- **Capacity is small.** The names where reversal is strongest are illiquid; market impact caps deployable capital quickly. This is why short-term reversal is a desk strategy, not a fund-scale one.
- **Use as a filter.** Many practitioners use the short-term reversal signal not as a standalone trade but to *time entries* into longer-horizon positions — avoid buying a name that has just spiked, prefer adding after a short-term pullback.

See [[mean-reversion]] for the broader strategy family and [[statistical-arbitrage]] for the cost-aware implementation context.

## Related

- [[mean-reversion]] — the parent strategy family
- [[momentum]] — the intermediate-horizon counterpart
- [[statistical-arbitrage]] — cost-aware implementation vehicle
- [[liquidity]] — the source of the premium
- [[market-microstructure]] — the framework for the liquidity-provision explanation
- [[idiosyncratic-volatility-anomaly]] — where reversal is strongest
- [[pairs-trading]] — a related relative-value reversion approach

## Sources

- Lehmann, B. (1990). "Fads, Martingales, and Market Efficiency." *Quarterly Journal of Economics* — original weekly reversal evidence.
- Jegadeesh, N. (1990). "Evidence of Predictable Behavior of Security Returns." *Journal of Finance* — monthly reversal.
- De Bondt, W. and Thaler, R. (1985). "Does the Stock Market Overreact?" *Journal of Finance* — long-term reversal.
- Nagel, S. (2012). "Evaporating Liquidity." *Review of Financial Studies* — reversal as the return to liquidity provision; time variation with VIX.
- Grossman, S. and Miller, M. (1988). "Liquidity and Market Structure." *Journal of Finance* — the liquidity-provision framework.
