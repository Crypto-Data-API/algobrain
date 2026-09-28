---
title: "TradingView"
type: entity
created: 2026-04-06
updated: 2026-09-28
status: good
tags: [data-provider, platform, crypto, forex, technical-analysis, options]
entity_type: company
website: https://www.tradingview.com
founded: 2011
headquarters: "New York, USA (incorporated in the UK)"
related:
  - "[[yahoo-finance]]"
  - "[[alpha-vantage]]"
  - "[[options]]"
  - "[[technical-analysis]]"
  - "[[ai-backtesting-overview]]"
---

# TradingView

## Overview

TradingView is the most popular retail charting platform, providing multi-asset charts across stocks, crypto, forex, commodities, and indices. Beyond charting, it offers a community-driven ecosystem of custom indicators and strategies written in Pine Script, social features for sharing trade ideas, and built-in screening tools. While not a traditional data API, TradingView's charting capabilities and Pine Script language make it a critical tool for technical traders. The free tier is functional enough to be useful; paid tiers unlock the full power.

## Free Tier

- **Charts**: 1 chart per tab, up to 3 indicators per chart
- **Data**: delayed quotes (15-20 min) for most markets
- **Timeframes**: all standard timeframes available
- **Pine Script**: write and run custom indicators/strategies
- **Community**: access thousands of published indicators and ideas
- **Screener**: basic stock, forex, and crypto screening
- **Alerts**: 1 active alert
- **Limitations**: ads, single chart layout, no multi-timeframe in one view

## Paid Tiers

| Plan | Price | Key Features |
|------|-------|-------------|
| Essential | ~$15/mo | 2 charts/tab, 5 indicators, 20 alerts, no ads |
| Plus | ~$30/mo | 4 charts/tab, 10 indicators, 100 alerts |
| Premium | ~$60/mo | 8 charts/tab, 25 indicators, 400 alerts, second-based alerts |
| Expert/Ultimate | ~$100/mo | unlimited indicators, all features |

Real-time data requires additional exchange-specific subscriptions ($1-5/mo each).

## Alpha Edge

- Best free charting tool for [[technical-analysis]] across any asset class
- Pine Script enables building and backtesting custom indicators and strategies without coding infrastructure
- Community strategies provide ideas to test -- thousands of published systems
- Multi-asset charting lets you spot correlations between markets visually
- Alert system automates monitoring of technical setups across your watchlist
- Social features reveal retail sentiment and popular trade ideas

## API Details

TradingView does not offer a traditional REST API for data access. Integration options:

- **Pine Script**: TradingView's proprietary scripting language for custom indicators and strategies (executed on their platform)
- **Webhooks**: alerts can send HTTP requests to external systems (paid feature)
- **Charting library**: TradingView offers an embeddable charting widget for websites (separate licensing)
- **No data export API**: you cannot programmatically pull OHLCV data from TradingView

```pine
// Pine Script example - Simple moving average crossover
//@version=5
strategy("SMA Cross", overlay=true)
fast = ta.sma(close, 10)
slow = ta.sma(close, 50)
if ta.crossover(fast, slow)
    strategy.entry("Long", strategy.long)
if ta.crossunder(fast, slow)
    strategy.close("Long")
```

## Use Cases

- Primary charting platform for [[technical-analysis]] across all markets
- Rapid prototyping of trading strategies via Pine Script
- Visual market monitoring with multi-chart layouts (paid)
- Webhook-based alerts feeding into [[algorithmic-trading]] systems
- Screening for technical setups using built-in stock/crypto screeners
- Options chain visualization and implied volatility charting (paid tiers)

## Limitations

- **No data export API**: you cannot programmatically pull OHLCV data from TradingView for external backtesting. For systematic [[ai-backtesting-overview|backtesting]], use [[alpha-vantage]], [[polygon]], or [[databento]] instead
- **Pine Script is platform-locked**: strategies written in Pine Script can only run on TradingView's infrastructure — no local execution, no custom data feeds, no integration with Python/C++ trading systems
- **Backtest engine is naive**: Pine Script's Strategy Tester uses simple fill assumptions (no slippage model, no realistic market impact, fills at bar close). Results should be treated as directional indicators, not production-grade backtests. See [[backtesting-pitfalls]]
- **Delayed data on free tier**: 15-20 minute delay on most markets. Real-time data requires paid exchange subscriptions ($1-5/mo per exchange)
- **Alert limits**: free tier gets 1 alert; even Premium ($60/mo) caps at 400. Active traders monitoring many setups can hit this ceiling
- **No multi-broker execution**: TradingView supports broker integration for some partners, but execution capabilities are limited compared to dedicated platforms like interactive-brokers

## Competitive Positioning

| Platform | Strength | Weakness vs TradingView |
|----------|----------|------------------------|
| **Bloomberg Terminal** | Institutional-grade data, news, analytics | $24,000/year; overkill for retail |
| **finviz** | Fast screening, heatmaps | No charting depth, no Pine Script |
| **MetaTrader 4/5** | Forex-focused, broker-integrated execution | Worse charting UX, smaller community |
| **Thinkorswim** (Schwab) | Excellent options analytics | Broker-locked, US-only |
| **TC2000** | Fast scanning, clean charts | Smaller community, no crypto |

TradingView dominates retail charting because it combines good-enough functionality across all asset classes with the best UI/UX and the largest community. It is not the best at any single thing (Bloomberg for data, Thinkorswim for options, MetaTrader for forex execution), but it is the best *generalist* platform for retail traders.

## Community Scripts as an Idea Source

TradingView's public script library is the biggest retail catalogue of [[pine-script|Pine Script]] indicators and strategies. It is a good place to find **ideas**. It is not a place to find **evidence**. Treat every script as an unfalsified hypothesis, and re-test anything worth keeping outside TradingView with fees on and over the full history (Source: [[tradingview-community-scripts]]). See [[external-strategy-sources]] for how it compares with other idea pools.

### Finding scripts

- **On the chart:** Indicators (the `fx` button) > **Community Scripts**. Search by name or concept, for example "squeeze", "wavetrend" or "supertrend".
- **On the web:** `tradingview.com/scripts`. Use **Editors' picks** for curated, usually well-documented scripts. Use **Popular** with "most popular" sorting to see what the crowd has adopted. Tick **Open-source only** so you can read the logic. The type filter separates indicators, strategies and libraries.
- **By author:** long-running open-source authors such as LazyBear, everget, KivancOzbilgic, QuantNomad and Mihkel00 publish reference implementations that later scripts copy. The original is usually the cleanest version to audit (Source: [[tradingview-community-scripts]]).

### Open-source vs protected vs invite-only

| Visibility | Code visible? | Typical use | Research value |
|---|---|---|---|
| **Open-source** | Yes | Free community tools | High. You can audit it and port it |
| **Protected** | No (author only) | Free, but the author keeps the logic private | Low. You cannot check for repainting or lookahead |
| **Invite-only** | No, and access is gated | Paid "vendor" scripts | Very low. Often repackaged open-source logic. everget's HalfTrend page warns about paid clones of free indicators |

Open-source scripts default to the **Mozilla Public License 2.0** unless the author declares another licence. The **House Rules** override the licence. If you republish someone's code, credit the author, make a meaningful improvement (renaming variables, changing inputs or converting Pine versions does not count), and keep it open-source unless the author agrees otherwise. Private use and porting for your own research are fine. If you redistribute a port, credit the original author and follow MPL-2.0 file-level copyleft (Source: [[tradingview-community-scripts]]).

### Vetting checklist

Run every script through these checks before trusting its chart or Strategy Tester output:

1. **Repainting through `request.security()`.** Watch for `lookahead = barmerge.lookahead_on` without a `[1]` offset on the requested series, or higher-timeframe values read before that bar has closed. Historical bars then "know" the HTF close, so signals look perfect on the chart and could never have fired live. See [[lookahead-bias]] and [[repainting]].
2. **`calc_on_every_tick = true`.** Realtime bars recalculate on every tick, but history only has closes. Live signals flicker and backtest fills do not match live fills. The same applies to scripts that act on `close` of the unconfirmed bar without `barstate.isconfirmed`.
3. **Other repaint sources.** Pivots and zigzags that confirm N bars later but plot back at the pivot bar, `ta.valuewhen` on future-confirmed events, and signals computed on [[heikin-ashi]] candles while fills use HA prices instead of real prices.
4. **Strategy Tester defaults.** Commission and slippage both default to **0**, and default sizing and capital are arbitrary. Set realistic crypto costs (for example 4-10 bps taker per side plus 1-5 bps slippage) and check whether the edge survives. See [[transaction-costs]].
5. **Unrealistic fills.** Orders filling at the signal bar's close, "process orders on close", intrabar stop/limit assumptions without Bar Magnifier, and profit targets that assume the wick was tradable.
6. **Curve-fit inputs.** Odd parameter values (a 17-period RSI with a 1.37 multiplier), many inputs, or results that collapse when a parameter moves by ±20%. See [[overfitting]] and [[overfitting-detection]].
7. **Too few trades.** A headline built on 20-40 trades, one symbol, or one bull-market window is not statistically meaningful. Look for 100+ trades across multiple regimes, and deflate for the number of variants tried ([[deflated-sharpe-ratio]]).
8. **Chart-specific history.** Results depend on the bar count your plan loads and on the symbol's exchange feed. A BINANCE:BTCUSDT backtest does not carry over to a perp on another venue without re-testing.

### LLM-assisted port workflow

A practical route from a community script to a research-grade test:

1. **Copy the open-source Pine code** and give it to an LLM. Ask it to explain every input, list any repainting or lookahead risks it finds (`request.security`, `calc_on_every_tick`, pivots), and state the exact entry and exit rules in plain English.
2. **Ask for "fees on, full history".** Have the LLM rewrite the `strategy()` header with explicit `commission_type = strategy.commission.percent`, a realistic `commission_value` and `slippage`, fixed-fraction sizing, and `request.security(..., lookahead = barmerge.lookahead_off)` or offset HTF calls. Re-run on the longest history your plan allows, and compare against the author's headline.
3. **Port to Python.** Have the LLM translate the logic into [[python|Python]] (pandas, or [[vectorbt]] / [[backtrader]]) and compute signals only from confirmed bars. Feed it [[cryptodataapi-backtesting|CryptoDataAPI]] klines (`GET /api/v1/backtesting/klines` for the deep archive, `GET /api/v1/market-data/klines` for recent bars) and add perp funding from `GET /api/v1/backtesting/funding` if the strategy holds leveraged positions.
4. **Validate the port.** Check that the Python signal series matches the TradingView plot bar-for-bar on a recent window before you trust any statistic. Then run [[walk-forward-analysis]], parameter-sensitivity sweeps and a cost overlay, and hand the result to the [[overfitting-detection]] checklist.
5. **Document the result.** Record the port on the wiki with `backtest_status: untested` until it passes, crediting the original author by TradingView username.

## Related

- [[pine-script]]: the language behind every community script
- [[tradingview-community-scripts]]: source summary of the library, licence rules and popular scripts
- [[external-strategy-sources]]: TradingView alongside other strategy idea pools
- [[backtesting-pitfalls]]: general traps the vetting checklist builds on
- [[squeeze-momentum-indicator]], [[wavetrend-oscillator]], [[qqe]], [[ut-bot-alerts]], [[ssl-channel]], [[halftrend]]: popular open-source scripts documented from the library
