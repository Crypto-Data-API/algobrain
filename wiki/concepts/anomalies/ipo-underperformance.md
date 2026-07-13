---
title: "IPO Underperformance Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, behavioral-finance, stocks]
aliases: ["IPO Long-Run Underperformance", "Ritter Anomaly", "New Issues Puzzle", "IPO Underperformance", "IPO Underperformance Anomaly"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[net-share-issuance]]"]
difficulty: beginner
related: ["[[anomalies-overview]]", "[[net-share-issuance]]", "[[investor-sentiment]]", "[[value-anomaly]]"]
---

# IPO Long-Run Underperformance Anomaly

Companies that go public through initial public offerings (IPOs) systematically underperform the broader market in the 3-5 years following their listing. Ritter (1991) first documented this at a cross-section of US IPOs, and subsequent researchers have confirmed it in multiple markets and extended it to seasoned equity offerings (SEOs). The anomaly is striking because IPOs are frequently celebrated as "hot" investments, yet the long-run returns have been persistently disappointing.

## What

Take all US IPOs in a given year. Track their equal-weighted buy-and-hold return over the subsequent 3-5 years. Compare to an otherwise-matched portfolio of seasoned stocks of similar size and industry. Ritter's 1991 sample showed IPOs underperformed their match portfolio by roughly 30% cumulative over 3 years (~8% annualized). Loughran & Ritter (1995) extended the result to SEOs with similar magnitudes.

## Original Papers

- Ritter, J. (1991) "The Long-Run Performance of Initial Public Offerings" — *Journal of Finance*
- Loughran, T. & Ritter, J. (1995) "The New Issues Puzzle" — *Journal of Finance*

## Mechanism

- **Managerial market timing** — firms choose to go public when their industry valuations are elevated and the market is receptive; new investors pay inflated prices that mean-revert over time (see [[investor-sentiment]] and [[net-share-issuance]])
- **Windows of opportunity** — IPO clustering in hot-issue markets (1999-2000, 2020-2021) is highly correlated with subsequent underperformance
- **Overoptimism** — retail and sell-side narratives overstate growth prospects for newly-public firms
- **Lockup expirations** — insider selling after 6-month lockups creates predictable supply pressure
- **Agency costs** — underwriters have incentives to placate institutional clients by slightly underpricing the IPO, then the stock drifts based on the overoptimistic narrative

Schultz (2003) offered a partial rational rebuttal: the underperformance may be an artifact of how IPO cohorts are averaged (survivorship and clustering), and once properly weighted the underperformance shrinks.

## Edge Category

**Behavioral** (sentiment-driven overpricing) + **informational** (managers have insider-timing advantage).

## Replication Status

Replicated in most samples, though magnitudes have varied. Hot-issue vintages (late 1990s, 2020-2021) show massive underperformance; cold-issue vintages show modest or no underperformance. The average is consistently negative.

## Decay History

Has held up across decades. The 2020-2021 SPAC and IPO boom produced one of the largest cohort-level underperformances in history, with many vintage-2021 IPOs down 70-90% from their listing prices by 2023.

## Current Viability

Tradeable primarily as:

- **A long-only screen** — avoid recently-IPOd stocks for 2-5 years
- **A short-side bias** — sophisticated short-sellers target hot-issue IPO cohorts, though borrow is often expensive in the early months due to lockups
- **A regime signal** — IPO volume is itself a [[investor-sentiment]] indicator that predicts market-wide returns

## Related Strategies

- [[net-share-issuance]] — IPOs are an extreme case
- [[investor-sentiment]] — IPO volume is a Baker-Wurgler sentiment proxy
- [[value-anomaly]] — IPO underperformance mostly reflects their being expensive-glamour names

## Sources

- Ritter (1991) — foundational IPO paper
- Loughran & Ritter (1995) — extended to SEOs
- Loughran, Ritter, Rydqvist (1994) international IPO results
- Schultz (2003) partial rebuttal on clustering
- Ritter's ongoing IPO statistics at site.warrington.ufl.edu

## Related

- [[anomalies-overview]]
- [[net-share-issuance]]
- [[investor-sentiment]]
- [[value-anomaly]]
