---
title: "FXCM"
type: entity
created: 2026-04-14
updated: 2026-06-10
status: good
tags: [exchange, forex, data-provider, algorithmic]
aliases: ["FXCM", "Forex Capital Markets"]
entity_type: company
founded: 1999
headquarters: "London, United Kingdom"
website: "https://www.fxcm.com"
related:
  - "[[python-for-algorithmic-trading]]"
  - "[[oanda]]"
  - "[[custom-python-bots]]"
  - "[[trading-system-deployment]]"
  - "[[forex]]"
  - "[[tail-risk]]"
  - "[[book-python-for-algorithmic-trading]]"
---

FXCM (Forex Capital Markets) is a [[forex]] and CFD broker, founded in 1999, that historically provided the `fxcmpy` Python library for API connectivity and was used alongside [[oanda|OANDA]] in Hilpisch's *[[python-for-algorithmic-trading|Python for Algorithmic Trading]]* (Source: [[book-python-for-algorithmic-trading]]). As of June 2026 FXCM is a wholly owned subsidiary of Jefferies Financial Group under the renamed parent **Stratos Group International**, and Jefferies is migrating new retail clients to its newer **Tradu** multi-asset platform — FXCM is no longer an independent public-market story.

## Corporate Status (2023-2026)

- **September 2023** — Jefferies Financial Group obtained 100% ownership of FXCM Group via foreclosure on pledged collateral (Jefferies' Leucadia predecessor had held a majority economic interest since the 2015 bailout). FXCM Group's parent was renamed **Stratos Group International, LLC**.
- **2024** — Jefferies launched **Tradu**, a multi-asset retail trading platform (FX, CFDs, stocks, crypto), built on the Stratos/FXCM infrastructure.
- **2025-2026** — FXCM continues to operate as a brand in several jurisdictions, but FXCM UK states that new accounts are now opened via Tradu; both brands sit inside the same FCA-regulated entity. The `fxcmpy` Python library is no longer actively maintained — algorithmic traders building new systems should treat the Hilpisch FXCM examples as historical and prefer [[oanda|OANDA]]'s v20 API or other brokers for live work.

## Algo Trading Relevance

FXCM is relevant to algorithmic traders primarily through its Python API:

- **fxcmpy library** -- A Python wrapper for FXCM's REST API, used by Hilpisch for live trading examples in his book. Provides order management, position tracking, and historical data access.
- **Free demo accounts** -- Paper trading environment for [[trading-system-deployment|testing strategies]] before live deployment
- **Historical data access** -- Tick and candle data available through the API for [[backtesting-overview|backtesting]]
- **Streaming prices** -- Real-time price feeds via the API for live strategy execution

## The Swiss Franc Crisis (2015)

FXCM's corporate history includes one of the most dramatic events in retail forex: the **Swiss National Bank (SNB) EUR/CHF floor removal** on January 15, 2015.

- The SNB had maintained a floor of 1.20 on EUR/CHF since 2011, and most market participants (including FXCM's clients) had positioned accordingly
- When the SNB abruptly removed the floor, EUR/CHF plunged ~30% in minutes -- an unprecedented move for a major currency pair
- Client losses of **$225 million** exceeded FXCM's regulatory capital, pushing the company to the brink of insolvency
- **Leucadia National** (now Jefferies Financial Group) provided a $300 million emergency bailout in exchange for a majority stake
- FXCM was subsequently fined by the CFTC and NFA for misleading clients about its execution model, and lost its US operating license in 2017

This event is a case study in [[tail-risk]] for retail forex brokers and their clients. It demonstrated that even "impossible" moves (a 30% move in a major currency in minutes) can and do happen, and that broker counterparty risk is a real concern in the CFD/forex market (Source: [[book-python-for-algorithmic-trading]]).

## Products

- **Forex** -- Major, minor, and exotic currency pairs
- **CFDs** -- Indices, commodities, cryptocurrencies
- **Spread betting** -- Available in the UK

## API Features

| Feature | Description |
|---------|-------------|
| fxcmpy | Python library wrapping the REST API |
| Historical data | Tick and candle data at various granularities |
| Streaming | Real-time price updates |
| Order management | Market, limit, stop orders via API |
| Account info | Balance, margin, position data |

## Limitations

- **Forex/CFD only** -- Like [[oanda|OANDA]], cannot trade equities, exchange-traded [[futures]], or listed [[options-overview|options]]
- **Market maker model** -- FXCM is the counterparty to trades, creating potential conflicts of interest
- **Corporate history concerns** -- The 2015 crisis and subsequent regulatory actions raise questions about risk management
- **Less clean API** -- The fxcmpy library is functional but less polished than OANDA's v20 API documentation
- **Reduced US presence** -- Lost CFTC registration in 2017; primarily serves non-US clients

## Competitors

See [[oanda]] for a comparison table of forex brokers suitable for algorithmic trading.

## Related

- [[python-for-algorithmic-trading]] -- Uses FXCM as a secondary broker API
- [[oanda]] -- Primary broker in Hilpisch's examples, direct competitor
- [[custom-python-bots]] -- FXCM as a deployment target
- [[trading-system-deployment]] -- Deployment patterns applicable to FXCM
- [[forex]] -- FXCM's primary market
- [[tail-risk]] -- The 2015 SNB event as a case study

## Sources

- (Source: [[book-python-for-algorithmic-trading]]) -- Reference for FXCM API usage in algorithmic trading
- Jefferies/Stratos ownership history: https://pestel-analysis.com/blogs/owners/fxcm
- FXCM UK on Tradu account migration: https://www.fxcm.com/uk/help/c/accounts/tradu/
- Verified via Perplexity (sonar), 2026-06-10
