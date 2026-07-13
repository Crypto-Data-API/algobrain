---
title: "Broker API"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [technology, algorithmic, market-microstructure, order-types]
aliases: ["Broker API", "Broker APIs", "Trading API"]
domain: [market-microstructure]
related:
  - "[[fix-protocol]]"
  - "[[low-latency-trading]]"
  - "[[cloud-trading-infrastructure]]"
  - "[[order-types]]"
  - "[[algorithmic]]"
  - "[[deployment]]"
---

A broker API is a programmatic interface that lets software place, modify, and cancel orders, query positions and balances, and stream market data from a brokerage — without a human clicking a GUI. It is the connective tissue between a trading strategy's code and the market, and the choice of API shapes everything downstream: supported order types, latency, asset coverage, rate limits, and how a bot fails when something goes wrong.

## How It Works

A broker API exposes two logical channels:

1. **Trading / account** — submit orders, cancel/replace, fetch open orders, positions, P&L, margin, and account status. Usually authenticated via API key + secret (REST/WebSocket brokers) or a gateway session (IBKR).
2. **Market data** — streaming quotes, trades, and sometimes order-book depth, plus historical bars for [[backtesting]].

Common transport styles:

- **REST + WebSocket** — REST for orders/account queries, WebSocket for real-time fills and quotes. Typical of crypto exchanges and modern equity brokers (Alpaca, Tradier, Coinbase, Binance).
- **Native gateway / SDK** — IBKR's TWS API and Client Portal API, where a local gateway process bridges your code to IBKR's servers. Rich but stateful and finicky.
- **[[fix-protocol|FIX]]** — the institutional standard; a low-latency, session-based binary/tag-value protocol used by prime brokers and direct-market-access providers.

## Key Selection Criteria

- **Order types** — does it support brackets, OCO, trailing stops, IOC/FOK, post-only, algos? (See [[order-types]].)
- **Latency** — REST round-trips add tens to hundreds of milliseconds; FIX and colocated sessions are microsecond-class (see [[low-latency-trading]]). Most retail/swing bots are fine on REST.
- **Rate limits** — orders/sec and requests/min caps; exceeding them gets you throttled or banned mid-session.
- **Asset coverage** — equities, options, futures, FX, crypto; multi-asset (IBKR) vs. single-market.
- **Paper trading** — a sandbox is essential before deploying real capital (see [[deployment]]).
- **Idempotency & reconnection** — client order IDs and replay-safe submission so a network blip doesn't double-fill.

## Major Broker APIs

| Broker / venue | Interface | Notes |
|---|---|---|
| Interactive Brokers | TWS API, Client Portal API, FIX | Broadest multi-asset coverage; powerful but stateful gateway |
| Alpaca | REST + WebSocket | Commission-free US equities/crypto; developer-friendly, good docs |
| Tradier | REST | Equities + options, simple API |
| Binance / Coinbase / Kraken | REST + WebSocket / FIX | Crypto; high rate limits, deep order-book streams |
| TradeStation, Tastytrade, Schwab | REST | Equities/options retail APIs |
| Prime brokers / DMA | FIX | Institutional, lowest latency |

## Trading Relevance

The broker API is where a strategy meets execution reality. A backtest assuming instant mid-price fills collapses if the live API has 200ms latency, rejects the order type you assumed, or rate-limits you during a fast market. Building robust execution — handling partial fills, rejects, reconnections, and idempotent retries — is as important to live P&L as the alpha itself. This is a core concern of [[deployment]] and [[trading-system-deployment]].

## Related

- [[fix-protocol]] — the institutional broker-API standard
- [[order-types]] — what the API must support
- [[low-latency-trading]] — when API latency matters
- [[deployment]] — running a bot against a broker API in production
- [[cloud-trading-infrastructure]] — where the bot connecting to the API runs

## Sources

- Broker API documentation (Interactive Brokers, Alpaca, Binance, Coinbase); general knowledge of trading-system integration. No raw sources ingested yet.
