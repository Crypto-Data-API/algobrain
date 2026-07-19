---
title: Trend Following
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [trend-following, momentum, technical-analysis, algorithmic, position-trading]
aliases: ["Trend Trading", "Riding the Trend", "trend-following"]
domain: [technical-analysis]
prerequisites: ["[[trend]]", "[[moving-averages]]", "[[risk-management]]"]
difficulty: intermediate
related:
  - "[[trend]]"
  - "[[momentum]]"
  - "[[trend-following-cta]]"
  - "[[adx]]"
  - "[[breakout-trading]]"
  - "[[turtle-trading]]"
  - "[[moving-average-crossover]]"
  - "[[crisis-alpha]]"
  - "[[trend-plus-tail-hedge]]"
  - "[[trading-psychology]]"
---

Trend following is the discipline of entering positions in the direction of an established [[trend|trend]] and holding them until the trend reverses, aiming to capture the bulk of large directional moves while cutting losers quickly. It is reactive rather than predictive — the trend follower does not forecast tops and bottoms but follows price, accepting many small losses in exchange for occasional outsized winners. As a *concept* it underpins a broad family of implementations; the canonical systematic deployment in futures is documented in [[trend-following-cta]].

## Core Principles

1. **Markets trend.** Prices exhibit sustained directional moves driven by herding, the slow diffusion of information, and [[momentum]] — the empirical tendency of recent winners to keep winning.
2. **Cut losers, let winners run.** Position management is asymmetric: small, pre-defined losses on failed setups are funded by a minority of trades that produce very large gains. The return distribution is **positively skewed** (low win rate, high payoff ratio).
3. **No prediction.** Entries and exits are triggered by price itself — breakouts, moving-average crosses, channel breaks — not by views on fair value.

## How It Works

A trend-following system has three components: an entry/exit signal, a position-sizing rule, and an exit/stop framework.

- **Entry signals** — moving-average crossovers (e.g. 50/200-day "golden/death cross"), [[breakout-trading|Donchian channel breakouts]] (the basis of [[turtle-trading]]), or time-series momentum (sign of the trailing 3–12 month return).
- **Trend filters** — [[adx|ADX]] or moving-average slope to trade only when a genuine trend is present and to stand aside in chop.
- **Position sizing** — typically volatility-scaled (e.g. risk a fixed fraction of equity per trade using [[atr|ATR]] to set unit size), so each market contributes comparable risk.
- **Exits** — trailing stops that ratchet in the trend's direction, locking in profit as the move extends and exiting on a defined reversal.

### Illustrative logic

```
atr = average_true_range(price, 20)
if price > highest_high(price, 55):        # Donchian breakout
    enter_long(size = risk_per_trade / (2 * atr))
trailing_stop = highest_close_since_entry - 3 * atr
if price < trailing_stop:
    exit()
```

## Trading Relevance

Trend following has one of the longest documented track records of any systematic approach, spanning equities, commodities, currencies, rates, and futures. Managed-futures funds (CTAs) are its best-known practitioners; see [[trend-following-cta]]. Its defining portfolio property is **[[crisis-alpha]]**: because it can go short and ride extended moves, it has historically performed well during prolonged equity bear markets and crises (2000–02, 2008, early 2020), giving it positive convexity and low correlation to long-only books — the rationale for combinations like the [[trend-plus-tail-hedge|trend + tail-hedge]] and dragon-portfolio constructions.

## Key Challenges

- **Whipsaws** — frequent false signals in sideways, range-bound markets erode capital; trend filters mitigate but never eliminate this.
- **Late entry and exit** — by construction the strategy misses the start and the end of every move, capturing only the middle.
- **Low win rate** — typically below 50%, with profitability resting on a few large winners; this demands strict adherence to the let-winners-run rule.
- **Psychological difficulty** — long, shallow drawdowns between trending episodes test discipline, making [[trading-psychology]] and mechanical execution essential.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN trend classifier across the asset universe
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC with the 200D MA precomputed, the classic trend filter
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV for Donchian channels, MA crosses, and ATR sizing

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep kline archive for multi-year trend-system backtests
- `GET /api/v1/indicators/signum-rgg/{symbol}` — per-asset detail + 60d RGG history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/signum-rgg"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

**Live dashboards:** [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/indicators/signum-rgg` is a ready-made trend gate: take longs only in GREEN, shorts or flat in RED, stand aside in GREY chop
- **Compute** — the illustrative Donchian/ATR logic on this page runs directly on `GET /api/v1/market-data/klines` bars (highest-high channels, ATR from true ranges)
- **Backtest** — replay breakout and MA-cross systems against `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 — spanning full trending and ranging cycles)
- **Tip** — layer the HMM state from `GET /api/v1/quant/market` over RGG: whipsaw losses concentrate where the regime reads `range_low_vol`/`choppy_high_vol`, exactly the chop a trend book should sit out

## Related

- [[trend]] — the underlying market phenomenon.
- [[trend-following-cta]] — the systematic managed-futures implementation.
- [[momentum]] — the closely related cross-sectional/time-series effect.
- [[turtle-trading]] — the classic rules-based breakout system.
- [[crisis-alpha]] — why trend following diversifies a long book.

## Sources

- Michael Covel, *Trend Following* (2004) — survey of practitioners and the philosophy.
- Curtis Faith, *Way of the Turtle* (2007) — the Donchian-breakout Turtle system.
- Moskowitz, Ooi & Pedersen, "Time Series Momentum," *Journal of Financial Economics* (2012) — empirical evidence across 58 instruments.
- Hurst, Ooi & Pedersen (AQR), "A Century of Evidence on Trend-Following Investing" (2017) — long-horizon performance and crisis-alpha analysis.
