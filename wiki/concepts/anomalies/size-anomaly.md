---
title: "Size Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, quantitative, stocks, valuation]
aliases: ["Size Anomaly", "Size Premium", "Small-Cap Effect", "SMB", "Small-Firm Effect"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[factor-investing]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[value-anomaly]]", "[[quality-anomaly]]", "[[january-effect]]", "[[factor-investing]]"]
---

# Size Anomaly

The size anomaly is the empirical finding that small-capitalization stocks historically earned higher average returns than large-capitalization stocks, beyond what the CAPM beta alone would predict. It was one of the first major cracks in the efficient-markets picture and became the "S" in Fama & French's original three-factor model (SMB: small-minus-big). It is also one of the most heavily decayed of the classical anomalies, with post-publication returns near zero in US large-cap-adjusted data.

## What

Sort the US equity universe by market capitalization at the end of each year. Form a long portfolio of the smallest-decile stocks and a short portfolio of the largest-decile stocks, rebalance annually, equal-weight. The resulting long-short portfolio earned roughly 3-5% annualized in the 1926-1980 sample used by Banz and subsequent researchers.

## Original Paper

Banz, R. (1981) "The Relationship Between Return and Market Value of Common Stocks" — *Journal of Financial Economics*. Fama & French (1992, 1993) formalized it into the three-factor model.

## Mechanism

Multiple competing explanations, none fully satisfying:

- **Illiquidity premium** — small-caps have higher bid-ask spreads and market impact, so patient investors should earn a premium for holding them
- **Distress risk** — small firms have higher bankruptcy rates and may load on an unpriced distress factor
- **Data and analyst coverage gaps** — fewer analysts produce pricing inefficiencies that patient fundamental investors can exploit
- **January concentration** — see [[january-effect]]; much of the historical size premium was earned in January alone, consistent with tax-loss-selling and reinvestment flows rather than a structural risk premium

## Edge Category

Hybrid of **structural** (liquidity and distress) and **behavioral** (neglect and coverage gaps). See [[edge-taxonomy]].

## Replication Status

Replicated in the original sample. The effect is weak or zero in post-1980 US data once controlling for quality (small, unprofitable firms are the ones that underperform — see [[quality-anomaly]] and Asness et al. 2018 "Size Matters, If You Control Your Junk"). It persists more robustly in international markets and among micro-caps that are too illiquid for most institutional capital.

## Decay History

Heavily decayed. McLean & Pontiff (2016) found the post-publication return is roughly zero. However, Asness, Frazzini, Israel, Moskowitz, Pedersen (2018) argue that the decay disappears when you control for quality — small-quality outperforms small-junk by a large margin, and size is only a dead anomaly among low-quality micro-caps.

## Current Viability

Raw size as a standalone signal is dead in US equities. Size *combined with quality* (small-cap quality tilts) is still defensible and implemented by many factor ETFs. Size also still has diversification value in multi-factor portfolios even if its standalone Sharpe is near zero.

## Related Strategies

- [[quality-anomaly]] — the filter that revives size
- [[value-anomaly]] — historically correlated with size
- Factor ETFs that implement small-cap quality tilts

## Sources

- Banz (1981) — original documentation
- Fama & French (1992, 1993) — three-factor model
- Asness, Frazzini, Israel, Moskowitz, Pedersen (2018) "Size Matters, If You Control Your Junk"
- McLean & Pontiff (2016) on post-publication decay

## Related

- [[anomalies-overview]]
- [[value-anomaly]]
- [[quality-anomaly]]
- [[january-effect]]
- [[factor-investing]]
