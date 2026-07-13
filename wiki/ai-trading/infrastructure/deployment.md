---
title: "Deployment (Trading Systems)"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [technology, algorithmic, backtesting, risk-management]
aliases: ["Deployment", "Strategy Deployment", "Going Live"]
domain: [market-microstructure]
related:
  - "[[trading-system-deployment]]"
  - "[[cloud-trading-infrastructure]]"
  - "[[broker-api]]"
  - "[[data-management]]"
  - "[[backtesting]]"
  - "[[paper-trading]]"
  - "[[risk-management]]"
---

Deployment is the process of taking a backtested strategy and running it against the live market — reliably, safely, and with the same behavior the backtest predicted. It is where most of the engineering effort in a trading system actually lives, and where strategies quietly lose money to bugs, latency, downtime, and the gap between simulated and real execution.

> For the broader lifecycle and a fuller treatment, see [[trading-system-deployment]] and [[cloud-trading-infrastructure]]. This page is the infrastructure-section overview of the deployment problem.

## The Backtest-to-Live Gap

A passing backtest is necessary but not sufficient. Common ways live diverges from simulation:

- **Execution realism** — real fills suffer slippage, partial fills, and rejects the backtest ignored (see [[broker-api]]).
- **Latency** — signal-to-order delay that didn't exist in vectorized simulation.
- **Data parity** — live feature pipeline differs from the research one (see [[data-management]]).
- **Look-ahead leakage** that only surfaces when data arrives in real time.
- **Costs** — commissions, financing, and market impact under-modeled.

## Deployment Stages

1. **Paper trading** — run the live code path against the live market with simulated capital ([[paper-trading]]). Validates the whole stack — data, signals, order routing — without risk.
2. **Pilot / small size** — deploy real capital at a fraction of target size; confirm fills, P&L, and slippage match expectations.
3. **Scale up** — increase size gradually while monitoring capacity and market impact.

## Production Engineering Concerns

- **Reliability & failover** — process supervision, automatic restart, redundant connectivity; a crash mid-position is a risk event.
- **State management** — persist positions and open orders so a restart reconciles rather than double-trades; use idempotent client order IDs.
- **Monitoring & alerting** — heartbeats, fill latency, P&L vs. expected, data-staleness alarms, kill-switch on anomalies.
- **Risk controls** — pre-trade limits (max position, max order size, fat-finger checks) and a hard kill switch independent of strategy logic (see [[risk-management]]).
- **Reconciliation** — end-of-day match of broker positions/cash against internal state.
- **Where it runs** — VPS, cloud (AWS/GCP), or co-location depending on latency needs (see [[cloud-trading-infrastructure]]).

## Trading Relevance

Many profitable-on-paper strategies never make money because deployment is treated as an afterthought. The discipline — paper first, pilot small, monitor everything, fail safe — is what converts a research result into realized P&L. Deployment quality is a real, repeatable edge: firms that operationalize well capture the alpha that sloppy ones leak to downtime and bad fills.

## Related

- [[trading-system-deployment]] — fuller lifecycle treatment
- [[cloud-trading-infrastructure]] — where and how a system runs
- [[broker-api]] — the execution interface
- [[data-management]] — research/production data parity
- [[backtesting]] / [[paper-trading]] — the stages before live capital
- [[risk-management]] — pre-trade controls and kill switches

## Sources

- General knowledge of production trading-system engineering. No raw sources ingested yet.
