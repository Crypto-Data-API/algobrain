---
title: "OANDA"
type: entity
created: 2026-04-14
updated: 2026-06-10
status: good
tags: [exchange, forex, data-provider, algorithmic]
aliases: ["OANDA", "Oanda"]
entity_type: company
founded: 1996
headquarters: "New York, USA"
website: "https://www.oanda.com"
related:
  - "[[python-for-algorithmic-trading]]"
  - "[[fxcm]]"
  - "[[custom-python-bots]]"
  - "[[trading-system-deployment]]"
  - "[[forex]]"
  - "[[book-python-for-algorithmic-trading]]"
---

OANDA is a [[forex]] and CFD broker widely used in algorithmic trading education and practice. Founded in 1996, OANDA was one of the early online forex brokers and has built a reputation for clean, well-documented APIs that make it a natural choice for automated trading. Hilpisch uses OANDA's API extensively in *[[python-for-algorithmic-trading|Python for Algorithmic Trading]]* as the primary broker for live [[trading-system-deployment|trading deployment]] examples (Source: [[book-python-for-algorithmic-trading]]).

## Ownership & 2025-2026 Developments

- **Acquired by FTMO (completed 1 December 2025).** Prague-based prop-trading firm FTMO signed a purchase agreement with previous owner **CVC Asia Fund IV** in early 2025 and closed the deal on 1 December 2025 after securing approvals from five regulators over roughly eight months. Transaction value undisclosed. FTMO has stated it will run OANDA as a **fully standalone business**; the combination pairs modern prop-trading (FTMO challenges/funded accounts) with a regulated multi-jurisdiction broker.
- Prior ownership history: founded 1996 by Michael Stumm and Richard Olsen; CVC Capital Partners acquired OANDA in 2018 before selling to FTMO.
- For traders, the practical watch items are whether spreads, API access (v20), and regulatory coverage (CFTC/NFA in the US, FCA in the UK, ASIC, etc.) remain unchanged under FTMO ownership — no degradation reported as of June 2026.

## Why OANDA Matters for Algo Traders

OANDA's appeal for algorithmic traders stems from its API quality and accessibility:

- **Well-documented REST and streaming APIs** -- The v20 REST API is one of the cleanest broker APIs available, with consistent endpoint design, clear error messages, and comprehensive documentation. This is the primary reason Hilpisch chose OANDA for his book.
- **Free practice/demo accounts** -- Realistic market data and order execution in a risk-free environment, essential for [[trading-system-deployment|paper trading]] before live deployment
- **Fractional lot sizes** -- No minimum trade size, allowing precise [[position-sizing|position sizing]] even with small accounts
- **Competitive forex spreads** -- Tight spreads on major pairs, though widening during off-hours and high-volatility events
- **Historical data API** -- Free access to historical candle data for [[backtesting-overview|backtesting]], though with limitations on granularity and history depth
- **Python SDK** -- The `oandapyV20` library provides a Pythonic wrapper around the REST API, simplifying integration

## Products

- **Forex** -- 70+ currency pairs (majors, minors, exotics)
- **CFDs** -- Indices (S&P 500, NASDAQ, DAX), commodities ([[gold]], [[crude-oil|oil]]), metals, bonds
- **Cryptocurrency CFDs** -- Limited selection (BTC, ETH, LTC) via CFD, not spot

## API Features

OANDA's v20 API provides:

| Feature | Endpoint | Description |
|---------|----------|-------------|
| Pricing | REST + Streaming | Real-time bid/ask prices via REST polling or WebSocket streaming |
| Orders | REST | Create, modify, cancel orders (market, limit, stop, trailing stop) |
| Positions | REST | Current open positions, unrealized P&L |
| Account | REST | Balance, margin, NAV, transaction history |
| Historical candles | REST | OHLCV data at various granularities (S5 to monthly) |
| Instruments | REST | Available tradeable instruments and their specifications |

The streaming API is particularly important for [[trading-system-deployment|live deployment]] -- it provides real-time price updates without the latency and rate-limit concerns of REST polling (Source: [[book-python-for-algorithmic-trading]]).

## Limitations for Serious Algo Trading

- **Forex/CFD only** -- Cannot trade equities, exchange-traded [[futures]], or listed [[options-overview|options]]. Traders needing broader market access must use [[interactive-brokers|Interactive Brokers]] or similar.
- **Market maker model** -- OANDA is the counterparty to all trades. While they claim to hedge exposure, this creates a potential conflict of interest absent in exchange-traded markets.
- **Retail forex regulation** -- Subject to retail forex rules in many jurisdictions, including leverage caps (50:1 in the US, 30:1 in the EU) and negative balance protection requirements
- **Not suitable for high-frequency trading** -- REST/WebSocket latency and rate limits make OANDA inappropriate for latency-sensitive strategies
- **Limited cryptocurrency offering** -- Only a handful of crypto CFDs, far fewer than dedicated crypto exchanges

## Competitors

| Broker | Strength vs OANDA | Weakness vs OANDA |
|--------|-------------------|-------------------|
| [[interactive-brokers]] | Broader market access (equities, futures, options) | More complex API, higher minimum balance |
| [[alpaca]] | Free US equity commissions, modern REST API | US equities only, no forex |
| [[fxcm]] | Similar forex focus, fxcmpy library | Less clean API, corporate history concerns |
| Alpari, IG Markets | Similar product range | Less developer-friendly APIs |

## Related

- [[python-for-algorithmic-trading]] -- Uses OANDA as the primary broker API throughout
- [[fxcm]] -- Secondary broker used in Hilpisch's examples
- [[custom-python-bots]] -- OANDA is a common deployment target for Python bots
- [[trading-system-deployment]] -- OANDA's API quality makes it ideal for learning deployment
- [[forex]] -- OANDA's primary market

## Sources

- (Source: [[book-python-for-algorithmic-trading]]) -- Primary reference for OANDA API usage in algorithmic trading
- FTMO press release, "FTMO Completes Acquisition of OANDA from CVC" (2 Dec 2025): https://ftmo.com/en/press-release/ftmo-completes-acquisition-of-oanda-from-cvc/
- OANDA media center: https://www.oanda.com/group/media-center/press-releases/oanda-acquired-by-ftmo/
- GlobeNewswire (2 Dec 2025): https://www.globenewswire.com/news-release/2025/12/02/3197594/0/en/FTMO-Building-Global-Trading-Powerhouse-Completes-Acquisition-of-OANDA-from-CVC.html
- Verified via web search, 2026-06-10.
