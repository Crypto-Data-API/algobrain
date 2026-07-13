---
title: "Trading Bot Architecture"
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [ai-trading, trading-bots, architecture]
related:
  - "[[custom-python-bots]]"
  - "[[freqtrade]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[backtesting-pitfalls]]"
---

# Trading Bot Architecture

How automated trading systems are structured. Whether you use [[freqtrade]], [[hummingbot]], or build [[custom-python-bots|your own]], every trading bot shares the same fundamental components.

---

## Overview

A trading bot is a software system that ingests market data, generates trading signals, manages risk, executes orders, and monitors performance -- all without human intervention. The architecture must handle real-time data, make decisions under uncertainty, interact with unreliable external APIs, and recover gracefully from failures. Getting the architecture right is the difference between a bot that runs reliably for months and one that [[bot-risks-and-pitfalls|blows up overnight]].

---

## Core Components

### 1. Data Ingestion

Two approaches: **REST API Polling** (simple, reliable, higher latency) and **WebSocket Streaming** (real-time, lower latency, complex reconnection logic). Production bots typically use WebSocket for live data and REST for reconciliation.

### 2. Strategy Engine

Receives market data, produces signals. Calculates indicators, runs models, evaluates entry/exit conditions. Should be stateless where possible -- same inputs, same outputs -- which makes [[backtesting-pitfalls|backtesting]] reliable.

### 3. Risk Manager

Sits between strategy and execution. Position sizing (Kelly, fixed fractional, volatility-based), max drawdown halts, exposure limits, daily PnL limits. Can veto or resize any trade the strategy proposes.

### 4. Execution Engine

Translates signals into orders. Handles order placement, partial fills, retry logic with exponential backoff, [[slippage]] control via order book depth, and order batching.

### 5. Portfolio Tracker

Balance monitoring, PnL tracking (realized + unrealized), trade history logging, periodic reconciliation between local and exchange state.

### 6. Alerting System

Notifications via Telegram/Discord/email for trade executions, errors, drawdown thresholds, and heartbeat monitoring.

---

## Event-Driven vs Polling

| Approach | How It Works | Best For |
|---|---|---|
| **Event-Driven** | Components communicate via events/messages; each event triggers downstream processing | Low-latency, complex strategies, production systems |
| **Polling** | Main loop checks data at fixed intervals, runs strategy, executes trades | Simpler strategies, higher timeframes (15m+), prototyping |

[[freqtrade]] uses a polling architecture (check every candle). More sophisticated systems use event-driven designs with message queues (Redis, RabbitMQ).

---

## State Management and Crash Recovery

Bots crash. Exchanges go down. Networks fail. The bot must:

- **Persist state to disk/database** before every significant action
- **On restart**: Check open orders, reconcile positions, resume from last known state
- **Idempotency**: Ensure duplicate signals do not create duplicate orders
- **Kill switch**: A mechanism to flatten all positions and halt trading immediately

---

## See Also

- [[custom-python-bots]] -- Building these components in Python
- [[bot-risks-and-pitfalls]] -- What goes wrong when architecture fails
- [[freqtrade]] -- Framework that implements this architecture for crypto
- [[hummingbot]] -- Architecture specialized for market making
