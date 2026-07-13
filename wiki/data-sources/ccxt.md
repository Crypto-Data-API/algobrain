---
title: "CCXT"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, crypto, exchange, algorithmic, api-trading]
source_type: data
source_url: "https://github.com/ccxt/ccxt"
aliases: ["ccxt", "CCXT Pro", "ccxt.pro"]
related: ["[[kaiko]]", "[[coinapi]]", "[[crypto-data-sources]]", "[[crypto-perp-backtesting-pitfalls]]", "[[exchange-api-reference]]", "[[binance]]", "[[bybit]]", "[[hyperliquid]]"]
---

CCXT (CryptoCurrency eXchange Trading Library) is the de-facto open-source library providing a unified API across 100+ crypto exchanges for both market-data fetching and live trading. Available in Python, JavaScript/TypeScript, PHP, and C#, it is the most-installed dependency in crypto quant tooling and powers a large fraction of retail bots, research notebooks, and prototype execution systems. The MIT-licensed core is free; **CCXT Pro** extends it with WebSocket support under a commercial license.

## Overview

CCXT was started in 2017 to solve the same problem [[coinapi|CoinAPI]] solves — every exchange has its own API — but as an open-source client library rather than a hosted data feed. Users connect directly to each exchange (with their own API keys) and CCXT normalizes the request/response schema. This makes it the natural starting point for any crypto algorithmic project that needs to read live data or place orders.

## What CCXT Does

### Unified Market-Data Interface

```python
import ccxt
binance = ccxt.binance()
ohlcv = binance.fetch_ohlcv('BTC/USDT', '1h')
ticker = binance.fetch_ticker('BTC/USDT')
ob = binance.fetch_order_book('BTC/USDT', limit=50)
```

The same three methods work against [[bybit|Bybit]], [[hyperliquid|Hyperliquid]], OKX, Kraken, etc. — only the exchange constructor changes.

### Unified Trading Interface

```python
binance.create_order('BTC/USDT', 'limit', 'buy', 0.01, 50000)
binance.fetch_open_orders('BTC/USDT')
binance.cancel_order(order_id, 'BTC/USDT')
binance.fetch_balance()
```

Place, cancel, query orders; fetch positions and balances; all with one schema. Derivatives, margin, and futures methods are exposed where the venue supports them.

### REST and WebSocket

- **CCXT (free, MIT)**: REST polling — works for OHLCV, OB snapshots, order placement
- **CCXT Pro (commercial)**: WebSocket subscriptions for real-time tickers, trades, OB updates, user data streams
- WebSocket access is typically required for any latency-sensitive strategy; pricing is roughly $200-500/month depending on tier

### Exchange-Specific Method Pass-Through

When the unified API doesn't cover a venue-specific endpoint (e.g., Hyperliquid's vault deposit, Binance's portfolio margin), CCXT exposes a raw `request()` method to call any private endpoint with proper signing handled.

## Supported Exchanges

100+ venues including:

| Category | Examples |
|---|---|
| **Top spot CEXes** | [[binance|Binance]], Coinbase, Kraken, OKX, [[bybit|Bybit]], Kucoin, Gate.io, Bitfinex, Gemini, Bitstamp |
| **Top derivatives** | Binance Futures, OKX, [[bybit|Bybit]], [[bitmex|BitMEX]], Deribit, Phemex |
| **DEX / on-chain** | [[hyperliquid|Hyperliquid]], dYdX, Vertex |
| **Regional** | Upbit (KR), Bithumb (KR), Bitget, MEXC, BitFlyer (JP), CoinSpot (AU), WazirX (IN) |
| **Long tail** | 50+ smaller venues for arbitrage and altcoin coverage |

Full and current list lives at https://github.com/ccxt/ccxt#supported-cryptocurrency-exchange-markets.

## Use Cases

### Multi-Venue Backtesting Harness (Live + Recent History Only)

CCXT's `fetch_ohlcv` works against most venues for the recent N days/months (varies — Binance gives ~1500 1-minute candles per request, deeper history requires pagination). For shallow lookbacks or live forward-tests, this is fine. **For deep historical research, pair with [[coinapi|CoinAPI]] or [[kaiko|Kaiko]]**.

### Multi-Exchange Execution

Production systems use CCXT (or CCXT Pro) as the execution layer: one strategy decides what to trade, CCXT routes orders to whichever venue has the best price/depth. Funding-rate arbitrage, triangular arbitrage, and cross-exchange market-making are common patterns. See [[crypto-perp-backtesting-pitfalls]] for caveats.

### Paper-Trading Scaffolding

Most CCXT users start with `sandbox = True` (where the venue offers a testnet — Binance, [[bybit|Bybit]], OKX, Deribit, [[hyperliquid|Hyperliquid]]). The same code paths run against live keys when ready, reducing the gap between paper and production.

### Bot Frameworks Built on CCXT

Freqtrade, Hummingbot, Jesse, OctoBot, and most retail open-source bots use CCXT as their exchange-connectivity layer. This is itself a signal of CCXT's robustness — it has been hardened by years of bot users finding edge cases.

## Limitations

1. **Not a historical archive**: CCXT pulls live data and limited recent OHLCV. There is no "give me 2018 BTC trades" — the venue probably doesn't expose that, and CCXT can't conjure it. Use [[coinapi|CoinAPI]] / [[kaiko|Kaiko]] for deep history.
2. **Rate limits per venue**: each exchange caps requests/sec. CCXT respects them by default but a multi-venue script can still trip a single venue if poorly written.
3. **Not PIT-clean for older periods**: OHLCV pulled today is the OHLCV the venue currently reports — if the venue retroactively adjusted (rare but possible) you get the adjusted data, with no audit trail. For [[point-in-time-data|point-in-time]] guarantees use Kaiko / CoinAPI.
4. **Symbology is per-exchange**: CCXT normalizes the request format but symbols are still venue-specific (`BTC/USDT` on Binance vs. `BTC/USDC` on Coinbase). Cross-venue joins still need a mapping layer — CoinAPI's universal symbol IDs handle this more cleanly.
5. **Latency**: REST polling adds 50-300ms per request depending on geography. CCXT Pro WebSockets cut this dramatically but cost money and add complexity.
6. **Venue API quirks**: where a venue has weird semantics (e.g., post-only order behavior, margin mode toggles, sub-account routing) you still have to read the venue's docs. CCXT smooths the common 80% of calls, not 100%.

## When to Pair CCXT with Kaiko / CoinAPI

| Need | Tool |
|---|---|
| Live trading + recent OHLCV | **CCXT** alone |
| Multi-year historical backtest | **CCXT for live, CoinAPI / Kaiko for history** |
| Survivorship-bias-corrected altcoin universe | **CoinAPI** (delisted dataset) — CCXT can't see dead exchanges |
| Full-depth OB reconstruction | **Kaiko** — CCXT only fetches snapshots |
| Real-time multi-venue arbitrage | **CCXT Pro** WebSockets |

## License and Community

- **License**: MIT (core library) — fully open source, free for commercial use
- **CCXT Pro**: commercial license required, ~$200-500/month tiered
- **GitHub**: https://github.com/ccxt/ccxt — 30,000+ stars, 1,500+ contributors, multiple commits per day
- **Languages**: Python, JavaScript, TypeScript, PHP, C#
- **Documentation**: https://docs.ccxt.com
- Active Discord and GitHub Issues; new exchange integrations land within weeks of major-venue launches

The maintainer cadence is exceptional — CCXT typically supports a new top-100 exchange within 1-2 months of its launch, which makes it the safest assumption for any greenfield crypto project.

## Sources

1. CCXT GitHub repository — https://github.com/ccxt/ccxt
2. CCXT documentation — https://docs.ccxt.com
3. CCXT Pro documentation — https://docs.ccxt.com/#/ccxt.pro.manual

## Related

- [[kaiko|Kaiko]] — Institutional historical and OB data, complement to CCXT
- [[coinapi|CoinAPI]] — Multi-venue historical aggregator with survivorship-corrected universe
- [[crypto-data-sources]] — Full catalog of crypto data providers
- [[crypto-perp-backtesting-pitfalls]] — Crypto-specific backtest hazards
- [[exchange-api-reference]] — Notes on exchange APIs that CCXT wraps
- [[binance|Binance]] — Most-used venue with CCXT
- [[bybit|Bybit]] — Major derivatives venue
- [[hyperliquid|Hyperliquid]] — On-chain perp venue with CCXT support
