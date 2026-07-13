---
title: "Investment Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, fundamental-analysis, stocks]
aliases: ["Investment Factor", "Capex Anomaly", "CMA", "Investment Anomaly"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[asset-growth-anomaly]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[asset-growth-anomaly]]", "[[quality-anomaly]]", "[[value-anomaly]]"]
---

# Investment Anomaly

Firms that invest more aggressively — high capital expenditure, high asset growth, large acquisitions — subsequently earn *lower* returns than firms that invest conservatively. This contradicts the naive intuition that growth-oriented firms should outperform and is one of the most robust fundamentals-based anomalies in the literature. It is the "CMA" (conservative minus aggressive) factor in the Fama-French five-factor model (2015).

## What

Rank US firms annually on a measure of investment (typically year-over-year growth in total assets, or capex/assets). Long the bottom quintile (low investment), short the top quintile (high investment). The resulting long-short portfolio has earned roughly 4-6% annualized over multi-decade samples, with a Sharpe comparable to value and momentum.

## Original Paper

Cooper, Gulen, Schill (2008) "Asset Growth and the Cross-Section of Stock Returns" — *Journal of Finance*. Formalized into the five-factor model by Fama & French (2015). See also Hou, Xue, Zhang (2015) q-factor model.

## Mechanism

Two leading theories:

- **Q-theory / real-options (rational):** in a frictionless q-theory model, firms invest more when their cost of capital is low, which means their expected return is also low. High investment is a *symptom* of low expected returns, not a cause of underperformance. This is the Hou-Xue-Zhang interpretation.
- **Behavioral overextrapolation:** managers over-invest when recent performance is strong and the market rewards growth narratives; these investments disappoint on average (empire-building, agency problems, overconfident M&A).

Empirically the two are hard to distinguish, and the anomaly works whether you believe the risk story or the behavioral story.

## Edge Category

Analytical/fundamental, with behavioral overlay. See [[edge-taxonomy]].

## Replication Status

Replicated across markets and across definitions of "investment" (capex, asset growth, total external financing, acquisitions). It survives Hou-Xue-Zhang's (2020) replication gauntlet — one of the anomalies that *does* hold up under rigorous controls.

## Decay History

Has held up reasonably well since the 2008 Cooper-Gulen-Schill paper, with some compression. It is already implemented by most factor ETFs, which caps capacity.

## Current Viability

Tradeable as part of a multi-factor composite. Standalone Sharpe is moderate (0.4-0.6 gross of costs), with capacity in the billions. Diversifies value and momentum well.

## Related Strategies

- [[asset-growth-anomaly]] — closely related measurement
- [[quality-anomaly]] — often combined with investment in factor models
- Fama-French five-factor implementations

## Sources

- Cooper, Gulen, Schill (2008) — original paper
- Fama & French (2015) five-factor model
- Hou, Xue, Zhang (2015) q-factor model and (2020) replication study

## Related

- [[anomalies-overview]]
- [[asset-growth-anomaly]]
- [[value-anomaly]]
- [[quality-anomaly]]
- [[factor-investing]]
