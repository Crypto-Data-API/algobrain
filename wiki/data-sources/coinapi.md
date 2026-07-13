---
title: "CoinAPI"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, crypto, derivatives, backtesting]
source_type: data
source_url: "https://www.coinapi.io"
aliases: ["CoinAPI", "CoinAPI.io"]
related: ["[[kaiko]]", "[[ccxt]]", "[[crypto-data-sources]]", "[[selection-bias-research]]", "[[crypto-perp-backtesting-pitfalls]]", "[[lookahead-bias]]", "[[point-in-time-data]]", "[[survivorship-bias]]"]
---

CoinAPI is a multi-exchange crypto data aggregator providing unified tick, OHLCV, and order-book data across 350+ venues through a single REST and WebSocket API. The firm publishes widely cited research on [[survivorship-bias|survivorship-bias]] correction in crypto backtesting, and maintains a dataset of delisted tokens and dead exchanges that is rare among commercial providers. Pricing sits between free retail aggregators and premium institutional feeds like [[kaiko|Kaiko]].

## Overview

CoinAPI was founded in 2017 to solve the "every exchange has a different API" problem for crypto traders. The product is a normalized layer: one schema for trades, OB, and OHLCV across hundreds of CEXes and DEXes, with consistent symbology (e.g., `BINANCE_SPOT_BTC_USDT`). The same data is available historically (REST + S3 flat files) and in real time (WebSocket + FIX).

## What CoinAPI Provides

### Market Data

| Product | Description |
|---|---|
| **Trades (tick)** | Every print across covered venues, normalized timestamps |
| **OHLCV** | 1s / 1m / 5m / 1h / 1d candles with volume |
| **Quotes (L1)** | Top-of-book bid/ask with size |
| **Order books (L2)** | Snapshots + delta updates for supported venues |
| **Symbology** | Consistent symbol IDs across all venues — solves cross-venue mapping |
| **Reference rates** | Cross-venue volume-weighted prices |

### Derivatives

- Perpetual and dated futures: marks, funding rates, open interest, liquidations on covered venues
- Options chains for Deribit and selected venues
- Index-level metrics (basis, funding spread)

### Survivorship-Bias-Corrected Universe

CoinAPI publishes the **delisted-and-dead** dataset: every symbol that ever existed on every covered exchange, including those that have since been removed or whose host exchange has shut down (e.g., FTX, Mt. Gox, BitGrail). This is the single most useful feature for backtesters trying to avoid [[survivorship-bias]].

## Coverage

| Category | Detail |
|---|---|
| **Total exchanges** | 350+ (largest of any commercial aggregator) |
| **Live exchanges** | ~250 currently operational |
| **Dead/delisted** | 100+ historical venues retained for backtests |
| **Symbols** | 1.5M+ historical; 250k+ active |
| **History depth** | Back to 2010 for the longest-running pairs |
| **DEX coverage** | Uniswap, PancakeSwap, Curve, and other major DEXes via on-chain reconstruction |

## Use Cases

### Multi-Exchange Backtests

A single API key replays the same strategy against Binance, Coinbase, Kraken, OKX, Bybit, [[hyperliquid|Hyperliquid]], and dozens of smaller venues simultaneously. This matters because crypto liquidity is fragmented and a strategy that works on Binance may fail on a thinner book.

### Normalized Symbology

CoinAPI's symbol IDs solve the headache that the same asset appears as `BTC/USDT`, `XBT/USDT`, `BTCUSDT`, or `tBTCUSD` across venues. Backtests can join venues by symbol ID without per-exchange mapping logic.

### Survivorship-Bias-Corrected Universe

A naive crypto backtest that pulls "all currently listed coins on Binance" implicitly excludes every coin that was delisted, rugged, or migrated to another chain. The strategy looks profitable because losers are missing. CoinAPI's delisted dataset lets a backtest include those tokens with their full historical price action — including the final spike-and-zero of a rug pull. See [[selection-bias-research]] and [[crypto-perp-backtesting-pitfalls]].

### Real-Time Multi-Venue Arbitrage

WebSocket streams from many venues into one client connection — useful for cross-exchange arbitrage research and execution prototypes.

## Survivorship Bias in Crypto

CoinAPI's research (cited in their blog and in the Cornell-affiliated *Journal of Financial Data Science*) shows that crypto backtests suffer from survivorship bias far worse than equity backtests, because:

1. Token mortality is much higher (10-30%/year for small caps vs. <1%/year for S&P 500 stocks)
2. Exchange mortality is non-trivial (FTX, BitGrail, Mt. Gox, Cryptopia, Bittrex Global, etc.)
3. Most aggregators silently drop delisted symbols, so the universe shrinks retroactively

Studies using a survivorship-biased universe overstate small-cap crypto strategy returns by 5-30% annually depending on the lookback period. Using CoinAPI's full delisted dataset (or an equivalent) is essential for any backtest of altcoin strategies. See [[lookahead-bias]] and [[point-in-time-data]] for adjacent biases.

## Comparison to Kaiko / Tardis / CCXT

| Provider | Best for | Tradeoff |
|---|---|---|
| **[[kaiko|Kaiko]]** | Institutional-grade tick + full OB, microstructure research | More expensive; smaller venue list |
| **CoinAPI** | Wide venue breadth, survivorship-corrected universe, mid-tier price | OB depth is L2 not L3; less microstructure focus |
| **Tardis** | Derivatives tick + OB at competitive prices | Fewer venues than CoinAPI |
| **[[ccxt|CCXT]]** | Free, live trading + market data, open source | Not a historical archive; rate-limited per venue; symbology is per-exchange |

Many quant teams use **CoinAPI for historical research** and **CCXT for live execution**, with Kaiko brought in only when full-depth OB reconstruction is required.

## Pricing Tiers (Approximate)

| Tier | Price | Features |
|---|---|---|
| **Free / trial** | $0 | One-time ~$25 signup credit (card required); 100 requests/day; no WebSocket/FIX |
| **Startup** | ~$79/month | ~1k REST credits/day, WebSocket trade data, email support |
| **Streamer** | ~$249/month | ~10k REST credits/day, WebSocket trade + quote data |
| **Pro** | ~$599/month | ~100k REST credits/day, full WebSocket (trade/quote/book), FIX |
| **Enterprise** | Custom | Full historical archive, S3 flat-file delivery, dedicated infra, SLA |

Pricing as of June 2026 (verify at coinapi.io/products/market-data-api/pricing). CoinAPI also offers pay-as-you-go credits beyond the plan allowance. Note the free tier is a one-time credit, not a recurring free quota — budget for the Startup tier minimum for any ongoing project.

## Sources

1. CoinAPI official site — https://www.coinapi.io
2. CoinAPI documentation — https://docs.coinapi.io
3. CoinAPI research: "How to Eliminate Survivorship Bias in Crypto Backtesting" — https://www.coinapi.io/blog/how-to-eliminate-survivorship-bias-in-crypto-backtesting

## Related

- [[kaiko|Kaiko]] — Institutional-grade alternative for full-depth OB
- [[ccxt|CCXT]] — Open-source library for live multi-venue access
- [[crypto-data-sources]] — Full catalog of crypto data providers
- [[selection-bias-research]] — Academic research on selection bias
- [[crypto-perp-backtesting-pitfalls]] — Crypto-specific backtest hazards
- [[lookahead-bias]] — Avoiding look-ahead bias in backtests
- [[point-in-time-data]] — Immutable historical data semantics
- [[survivorship-bias]] — General survivorship-bias concept
- [[hyperliquid|Hyperliquid]] — On-chain perp venue covered by CoinAPI
