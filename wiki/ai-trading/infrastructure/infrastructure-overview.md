---
title: "Trading Infrastructure"
type: index
created: 2026-04-06
updated: 2026-06-12
status: good
tags: [ai-trading, infrastructure, index]
---

# Trading Infrastructure

Systems, networking, and infrastructure that powers trading operations.

Infrastructure is the hidden layer that determines whether a profitable strategy actually makes money in production. This section covers the engineering side of trading: [[cloud-trading-infrastructure|cloud vs. co-located deployments]], [[low-latency-trading|low-latency networking]], order management systems, execution management systems, and the [[fix-protocol|FIX protocol]] that connects most institutional participants.

Retail traders running bots on a VPS and institutional desks with FPGA-accelerated order routers face the same fundamental problems -- reliability, latency, monitoring, and failover -- at very different scales. Understanding these trade-offs helps you build systems that do not lose money to downtime or slow fills.

## Start Here

- [[cloud-trading-infrastructure]] -- AWS, GCP, and co-location trade-offs
- [[low-latency-trading]] -- Minimizing execution delay from signal to fill
- [[fix-protocol]] -- The standard messaging protocol for electronic trading

## Connectivity & Execution

- [[broker-api]] -- Programmatic order placement, market data, and account access
- [[fpga]] -- Hardware-accelerated tick-to-trade at the latency frontier
- [[deployment]] -- Taking a backtested strategy live safely

## Data Layer

- [[data-management]] -- Point-in-time storage, corporate actions, research/production parity
- [[databento]] -- Normalized historical and real-time market data API
- [[edgar]] -- SEC filings, XBRL fundamentals, and full-text search

## Platforms & Risk Tools

- [[ninjatrader]] -- Retail futures platform, brokerage, and NinjaScript backtesting
- [[sierra-chart]] -- Professional charting and order-flow platform
- [[ibkr-risk-navigator]] -- Free real-time portfolio risk and stress testing on IBKR

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/ai-trading/infrastructure"
WHERE type != "index"
SORT updated DESC
```

## Key Topics to Cover

- Co-location and low-latency networking
- Order management systems (OMS)
- Execution management systems (EMS)
- FIX protocol
- Cloud vs on-premise trading infrastructure
- Monitoring and alerting
