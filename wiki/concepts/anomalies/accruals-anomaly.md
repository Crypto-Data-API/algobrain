---
title: "Accruals Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, factors, fundamentals, earnings-quality, academic-research]
aliases: ["Sloan Accruals", "Earnings Quality Anomaly"]
domain: [anomalies]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[post-earnings-announcement-drift]]", "[[quality-anomaly]]"]
---

# Accruals Anomaly

Firms whose reported earnings are driven more by *accruals* (non-cash accounting adjustments) than by *cash flow from operations* subsequently earn lower returns. Investors appear to fixate on the headline earnings number without unpacking its quality, leaving a persistent spread between high-accrual and low-accrual firms. Sloan (1996) is one of the most-cited papers in empirical accounting and a foundational "earnings quality" anomaly.

## What

For each firm, decompose earnings into cash flow and accruals:

```
accruals = (ΔCA − ΔCash) − (ΔCL − ΔSTD − ΔTP) − Dep
```

Rank firms by accruals scaled by total assets. Long the lowest decile (low accruals = high earnings quality), short the highest decile (high accruals = low earnings quality). Sloan reported a ~10% annual hedge return over 1962-1991.

## Original Paper

Sloan, R. (1996) "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?" — *The Accounting Review*.

## Mechanism

**Behavioral mispricing:** investors anchor on headline earnings and fail to distinguish persistent cash-based earnings from transitory accrual-based earnings. Accruals eventually reverse — a firm that aggressively accrues today reports lower earnings tomorrow — and the market is systematically surprised when this happens.

Aggressive accruals are also correlated with earnings management and accounting fraud, so part of the effect may be a distress/fraud premium rather than pure behavioral bias.

## Edge Category

**Behavioral** and **analytical**: investors underweight statement-of-cash-flows data, and rigorous analysts can extract it. See [[edge-taxonomy]].

## Replication Status

Replicated across markets, time periods, and accrual definitions. Survives the Hou-Xue-Zhang (2020) replication gauntlet but with lower magnitude than in Sloan's original sample.

## Decay History

Decayed substantially but not to zero. Richardson, Sloan, Soliman, Tuna (2005) refined the measurement and showed the effect persists with the refined definition. Post-2000 the long-short spread is roughly half the Sloan-era magnitude but still positive.

## Current Viability

Tradeable by sophisticated fundamental quant funds, but the signal is now widely known and implemented. Best used as one component of a multi-factor quality/fundamentals model rather than a standalone strategy.

## Related Strategies

- [[quality-anomaly]] — accruals are a component of most quality definitions
- [[post-earnings-announcement-drift]] — complementary behavioral earnings anomaly
- Earnings-quality overlays on long-only equity portfolios

## Sources

- Sloan (1996) — original paper
- Richardson, Sloan, Soliman, Tuna (2005) — refined accruals measure
- Hou, Xue, Zhang (2020) "Replicating Anomalies"
- Dechow, Ge, Schrand (2010) survey of earnings-quality research

## Related

- [[anomalies-overview]]
- [[quality-anomaly]]
- [[post-earnings-announcement-drift]]
- [[factor-investing]]
