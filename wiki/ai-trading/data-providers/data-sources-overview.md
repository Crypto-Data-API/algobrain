---
title: "Trading Data Sources — Complete Guide"
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, guide, alpha-edge]
aliases: ["Data Sources", "Market Data Guide"]
related: ["[[alternative-data-alpha]]", "[[quicknode]]", "[[algorithmic-trading]]"]
---

# Trading Data Sources — Complete Guide

How much alpha can you get for free? More than most people think. This page maps every major data source by cost tier and asset class, showing exactly where the free-to-paid edge boundary sits.

## The Free Alpha Stack

A trader spending $0/month can access:

| Data Type | Best Free Source | What You Get | Alpha Edge |
|-----------|-----------------|-------------|-----------|
| Stock prices & fundamentals | [[yahoo-finance]] | 5yr financials, delayed quotes, options chains | Screen for value/growth, track earnings |
| Stock screening | [[finviz]] | Heatmaps, fundamental/technical filters | Quick sector overview, momentum screening |
| Charting (all assets) | [[tradingview-platform]] | Multi-asset charts, 3 indicators, community scripts | Best free charting, Pine Script backtesting |
| Crypto prices | [[coingecko]] | 10K+ coins, market cap, volume, exchange data | Altcoin momentum, market dominance shifts |
| DeFi analytics | [[defilama]] | TVL, yields, stablecoin flows, bridge volume | Capital flow tracking, yield opportunities |
| On-chain (Ethereum) | [[etherscan]] | Transactions, wallets, contracts, gas | Whale tracking, contract monitoring |
| On-chain (custom SQL) | [[dune-analytics]] | Community dashboards, custom queries | Custom on-chain analysis, whale tracking |
| DEX trading | [[dex-screener]] | Real-time token prices, new pairs, liquidity | Early token discovery, on-chain momentum |
| Crypto derivatives | [[coinglass]] | Funding rates, OI, liquidations, long/short ratios | Predict cascades, funding arb signals |
| Economic data | [[fred]] | 800K+ macro time series, 120 req/min API | Regime analysis, recession probability |
| Sentiment | [[fear-and-greed-index]] | CNN F&G (stocks) + Alternative.me (crypto) | Contrarian timing at extremes |
| Market data API | [[alpha-vantage]] | Stocks, forex, crypto, technicals (25 req/day) | Build basic algo strategies |
| Blockchain SQL | [[quicknode]] | Hyperliquid + other chain data via SQL API | On-chain verified trading data |

**Verdict**: The free stack is genuinely powerful for crypto trading. For stocks, you get enough for fundamental screening and swing trading but lack real-time data and options flow.

## Where Paid Data Creates Edge

The free-to-paid boundary differs by trading style:

### You NEED paid data for:
- **Real-time stock/options execution** — Free data is delayed 15-20 min. Useless for day trading.
- **Options flow analysis** — [[unusual-whales]] or [[spotgamma]] show institutional positioning that free tools can't
- **Institutional on-chain tracking** — [[nansen]] labels wallets (free data shows transactions but not WHO)
- **Professional derivatives analytics** — [[laevitas]] for vol surfaces, [[spotgamma]] for GEX
- **Alternative data** — [[quiver-quant]] for Congress trades, satellite data (no free source exists)

### You DON'T need paid data for:
- **Crypto spot/perp trading** — Free data stack covers 90% of needs
- **Long-term investing** — [[yahoo-finance]] + [[finviz]] + [[fred]] is sufficient
- **DeFi analytics** — [[defilama]] + [[dune-analytics]] + [[dex-screener]] = comprehensive
- **Macro analysis** — [[fred]] is the gold standard and completely free
- **Basic technical analysis** — [[tradingview-platform]] free tier works

## Paid Data by Tier

### Budget ($0-50/mo)
| Tool | Cost | Edge |
|------|------|------|
| [[tradingview-platform]] Pro | $15/mo | Unlimited indicators, alerts, multiple charts |
| [[unusual-whales]] Basic | $50/mo | Options flow alerts, Congress tracker |
| [[koyfin]] Pro | $50/mo | Bloomberg-lite fundamentals and screening |

### Mid-Range ($50-200/mo)
| Tool | Cost | Edge |
|------|------|------|
| [[polygon-io]] | $99/mo | SIP-grade real-time stock + options API |
| [[quiver-quant]] | $50-200/mo | Congress trading, gov contracts, alt data |
| [[santiment]] Pro | $50-300/mo | Crypto sentiment + dev activity signals |
| [[laevitas]] Pro | $100+/mo | Crypto options vol surface, basis analytics |

### Professional ($200-1000/mo)
| Tool | Cost | Edge |
|------|------|------|
| [[spotgamma]] | $200-500/mo | GEX levels predict S&P behavior |
| [[nansen]] | $150-1000/mo | Smart money wallet tracking |
| [[glassnode]] Pro | $500+/mo | 200+ Bitcoin on-chain metrics |
| [[arkham-intelligence]] | $500+/mo | Cross-chain entity deanonymization |

### Institutional ($1000+/mo)
| Tool | Cost | Edge |
|------|------|------|
| [[bloomberg-terminal]] | $2K/mo/seat | Everything. The gold standard. |

## Recommended Stacks by Trading Style

### Crypto Degen (Free)
[[coingecko]] + [[dex-screener]] + [[coinglass]] + [[defilama]] + [[dune-analytics]] + [[etherscan]]

### Crypto Professional ($200-500/mo)
Free stack + [[nansen]] + [[laevitas]] + [[quicknode]]

### Stock Swing Trader (Free)
[[yahoo-finance]] + [[finviz]] + [[tradingview-platform]] + [[fred]]

### Stock Options Trader ($100-300/mo)
[[tradingview-platform]] Pro + [[unusual-whales]] + [[spotgamma]]

### Quant/Algo ($100-200/mo)
[[alpha-vantage]] Premium + [[polygon-io]] + [[fred]] + Python/pandas

### Macro Investor (Free)
[[fred]] + [[koyfin]] free + [[tradingview-platform]] + [[fear-and-greed-index]]

## See Also

- [[alternative-data-alpha]] — How to combine data sources for informational edge
- [[cross-asset-signals]] — Using one market's data to trade another
- [[data-providers]] — Category index
- [[quicknode]] — QuickNode SQL Explorer (Hyperliquid data)
