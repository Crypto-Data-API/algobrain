---
title: "Pre-FOMC Announcement Drift"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, event-driven, sp500]
aliases: ["FOMC Drift", "Pre-FOMC Drift", "Lucca-Moench Anomaly", "Pre-FOMC Announcement Drift"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[federal-reserve]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[calendar-effects-anomalies]]", "[[time-series-momentum]]"]
---

# Pre-FOMC Announcement Drift

US equity returns in the 24 hours preceding Federal Open Market Committee (FOMC) announcements are abnormally high — so much so that, in Lucca & Moench's (2015) sample, the cumulative return on the S&P 500 in these windows accounted for roughly 80% of the equity risk premium since 1994. The effect has no satisfying rational explanation and has held up since publication.

## What

Starting at 2pm Eastern on the day *before* each scheduled FOMC statement release, compute the 24-hour return on the S&P 500 (or a futures equivalent, which is cleaner). Average across all FOMC meetings 1994-2011 in the original paper. The average return in this window is roughly 50 bps — compared to ~1-2 bps on an average 24-hour period, implying the eight FOMC meetings per year account for most of the annual equity return.

## Original Paper

Lucca, D. & Moench, E. (2015) "The Pre-FOMC Announcement Drift" — *Journal of Finance*.

## Mechanism

Remains genuinely puzzling. Candidates:

- **Risk premium for holding equities over the announcement** — investors demand compensation for FOMC-day uncertainty and buy in advance because the premium is earned before the resolution. This doesn't match the timing cleanly (the drift starts long before a reasonable risk window).
- **Anticipation of dovish surprises** — but Lucca-Moench found no correlation between the drift and the direction or surprise content of the eventual announcement
- **Information leakage** — the Fed has investigated and found no clear evidence of leaks
- **Liquidity provision / market-making capacity constraints** — dealers unwinding risk into announcements may produce upward flow pressure

Cieslak, Morse, Vissing-Jorgensen (2019) later documented a *broader* Fed cycle pattern where equity returns concentrate in even weeks after FOMC meetings (an 8-week cycle), which subsumes some of the pre-FOMC drift.

## Edge Category

Unclear. Part **structural** (dealer hedging flows) and part **informational** (something leaks, but researchers can't pin down what).

## Replication Status

Replicated in out-of-sample data by Cieslak, Morse, Vissing-Jorgensen (2019) and others. The effect has persisted since publication, which is unusual for a widely-known anomaly.

## Decay History

Surprisingly little decay. Post-2015 samples still show significant positive pre-FOMC returns, though magnitude has compressed somewhat. The persistence suggests a structural/flow mechanism rather than pure information.

## Current Viability

Directly tradeable for sophisticated investors — buy S&P 500 futures at 2pm the day before FOMC, close before the announcement. Eight trades per year, modest capacity. The simple strategy has roughly tracked the academic documentation post-publication, which is rare.

**Risks:** FOMC-day gaps can be large when the anomaly reverses (e.g. hawkish surprises), so sizing matters. Post-2022 the Fed's aggressive tightening cycle disrupted the pattern at specific meetings.

## Related Strategies

- [[time-series-momentum]] — FOMC drift contributes to equity time-series predictability
- [[calendar-effects-anomalies]] — broader family
- Fed-cycle based tactical asset allocation (Cieslak et al. 2019)

## Sources

- Lucca & Moench (2015) "The Pre-FOMC Announcement Drift" — *Journal of Finance*
- Cieslak, Morse, Vissing-Jorgensen (2019) "Stock Returns over the FOMC Cycle" — *Journal of Finance*
- Savor & Wilson (2013) on macroeconomic announcement risk premia

## Related

- [[anomalies-overview]]
- [[calendar-effects-anomalies]]
- [[time-series-momentum]]
