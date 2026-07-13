---
title: "Technical Indicators"
type: index
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [indicators, concepts, index]
aliases: ["Technical Indicators", "Indicators Overview", "Indicator Index"]
related: ["[[technical-analysis-overview]]", "[[triple-screen-system]]", "[[regime-matrix]]", "[[rsi]]", "[[macd]]", "[[bollinger-bands]]", "[[vwap]]"]
---

# Technical Indicators

Technical indicators are mathematical transformations of price, volume, and (sometimes) open-interest data designed to help traders interpret market behaviour, identify trends, gauge momentum, measure volatility, and time entries and exits.

No single indicator is a crystal ball. The best practitioners combine complementary indicators -- a trend filter like a moving average with a momentum oscillator like [[rsi|RSI]] or [[macd|MACD]] -- and confirm signals with volume tools like [[vwap|VWAP]]. [[bollinger-bands|Bollinger Bands]] add a volatility envelope that adapts to changing market conditions.

## Start Here

- [[rsi]] -- Relative Strength Index, the most popular momentum oscillator
- [[macd]] -- Moving Average Convergence Divergence for trend and momentum
- [[bollinger-bands]] -- Volatility bands that adapt to price action
- [[vwap]] -- Volume-Weighted Average Price, the institutional benchmark
- [[ichimoku]] -- Ichimoku Kinko Hyo, the all-in-one equilibrium chart
- [[donchian-channels]] -- Breakout channels behind the Turtle Trading system

## Five Indicator Categories

Indicators broadly fall into five categories (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]):

### Master Index (at a glance)

| Indicator | Category | Measures | Best regime | Concept page |
|---|---|---|---|---|
| Moving averages (SMA/EMA) | Trend | Direction, smoothed price | Trending | [[moving-averages]] |
| ADX / DMI | Trend | Trend *strength* (0-100) | Any (as a filter) | [[adx]] |
| Ichimoku | Trend (all-in-one) | Trend, momentum, S/R, time | Trending | [[ichimoku]] |
| RSI | Momentum | Overbought/oversold (0-100) | Ranging | [[rsi]] |
| MACD | Momentum | Trend-following momentum | Trending | [[macd]] |
| Stochastic | Momentum | %K/%D range position | Ranging | [[stochastic]] |
| Williams %R | Momentum | Range position (0 to -100) | Ranging | [[williams-percent-r]] |
| CCI | Momentum | Deviation from mean | Ranging/cyclical | [[cci]] |
| Aroon | Momentum | Time since high/low | Trend onset | [[aroon]] |
| Bollinger Bands | Volatility | Std-dev envelope | Ranging (squeeze→breakout) | [[bollinger-bands]] |
| ATR | Volatility | Average true range | Any (sizing/stops) | [[atr]] |
| Keltner Channels | Volatility | ATR envelope | Trending | [[keltner-channels]] |
| Donchian Channels | Volatility/breakout | N-period high/low | Trending (breakout) | [[donchian-channels]] |
| VIX | Volatility | Implied vol index | Risk regime gauge | [[vix]] |
| VWAP | Volume | Volume-weighted avg price | Intraday | [[vwap]] |
| OBV | Volume | Cumulative volume flow | Confirmation | [[obv]] |
| Chaikin Money Flow | Volume | Accumulation/distribution | Confirmation | [[chaikin-money-flow]] |
| Money Flow Index | Volume | Volume-weighted RSI | Ranging | [[money-flow-index]] |
| Volume Profile | Volume | Price-volume distribution | Any (S/R mapping) | [[volume-profile]] |
| Market Breadth | Breadth | Advance/decline | Index-level | [[market-breadth]] |
| McClellan Oscillator | Breadth | NYSE breadth momentum | Index-level | [[mcclellan-oscillator]] |
| Arms Index (TRIN) | Breadth | Market internals | Index-level | [[arms-index]] |

The detailed category breakdown follows.

### Trend
Identify the direction and persistence of price movement.
- [[moving-averages]] (SMA, EMA), [[golden-cross]], [[death-cross]]
- [[adx|ADX/DMI]] -- trend strength on a 0-100 scale
- [[ichimoku]] -- all-in-one trend, momentum, and S/R
- [[dow-theory]] -- the foundational trend framework

### Momentum
Measure the speed and magnitude of price changes.
- [[rsi]] -- bounded 0-100, overbought/oversold
- [[macd]] -- trend-following momentum via EMA crossover
- [[stochastic]] -- %K/%D range positioning
- [[williams-percent-r]] -- mirror of stochastic, 0 to -100
- [[cci]] -- cyclical deviation from statistical mean
- [[aroon]] -- time since recent high/low

### Volatility
Quantify the degree of price fluctuation.
- [[bollinger-bands]] -- standard deviation envelope
- [[atr]] -- average true range for stop/position sizing
- [[keltner-channels]] -- ATR-based envelope
- [[donchian-channels]] -- N-period high/low breakout channel
- [[vix]] -- implied volatility index

### Volume
Confirm price moves with participation data.
- [[vwap]] -- institutional execution benchmark
- [[obv]] -- cumulative volume flow (Granville, 1963)
- [[chaikin-money-flow]] -- institutional accumulation/distribution
- [[money-flow-index]] -- volume-weighted RSI
- [[volume-profile]] -- price-volume distribution

### Breadth / Sentiment
Measure market-wide participation.
- [[market-breadth]] -- advance/decline analysis
- [[mcclellan-oscillator]] -- NYSE breadth momentum (McClellan, 1969)
- [[arms-index]] -- TRIN, market internals (Arms, 1967)

## Historical Timeline

Technical analysis traces back to 18th-century Japan, where rice merchant [[munehisa-homma|Munehisa Homma]] developed [[candlestick-patterns|candlestick charting]] at the Dojima Rice Exchange. In the West, [[dow-theory|Charles Dow]] co-founded the Wall Street Journal and formalised Dow Theory in the 1880s-1890s, introducing the DJIA (1896).

Early 20th-century pioneers -- William Peter Hamilton, Robert Rhea, Richard Schabacker (head-and-shoulders, triangles), and Richard Wyckoff (accumulation/distribution) -- systematised chart reading. [[jesse-livermore|Jesse Livermore]] popularised tape-reading in the 1920s. John Magee and Robert Edwards codified it all in *Technical Analysis of Stock Trends* (1948).

The **modern indicator era** arrived with mass computing in the 1970s-1980s, driven by:
- [[j-welles-wilder|J. Welles Wilder Jr.]] — RSI, ATR, ADX, Parabolic SAR (1978)
- [[gerald-appel|Gerald Appel]] — MACD (late 1970s)
- [[john-bollinger|John Bollinger]] — Bollinger Bands (1980s)
- [[goichi-hosoda|Goichi Hosoda]] — Ichimoku (1930s dev, 1969 pub)
- [[richard-donchian|Richard Donchian]] — Donchian Channels (1950s-60s)
- [[tushar-chande|Tushar Chande]] — Aroon (1995)
- [[donald-lambert|Donald Lambert]] — CCI (1980)

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## Markets and Asset Class Applicability

| Market | Most-Used Indicators | Notes |
|---|---|---|
| US/Global equities | MAs, RSI, MACD, Bollinger, VWAP, OBV | VWAP dominant intraday; breadth (McClellan, TRIN) for index traders |
| Futures/commodities | ATR, ADX, Donchian, Parabolic SAR, CCI, Ichimoku | Wilder's suite designed for commodities; Turtle system |
| Forex | Ichimoku, Fibonacci, MACD, Bollinger, Pivot Points | Ichimoku entrenched among Japanese FX desks |
| Crypto | RSI, MACD, Bollinger, VWAP, Ichimoku, Supertrend | 24/7 markets amplify volatility-based indicators |

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## Best-Practice Combinations

Professional traders typically layer 2-4 complementary indicators across different categories (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]):

1. **Trend + Momentum + Volatility + Volume**: 50/200 EMA + [[rsi|RSI]] + [[bollinger-bands|Bollinger Bands]] + [[obv|OBV]]
2. **Turtle-style breakout stack**: [[donchian-channels|Donchian]] 20/55 + [[atr|ATR]] sizing + [[adx|ADX]] filter
3. **Ichimoku standalone**: [[ichimoku]] already bundles trend, momentum, S/R, and time
4. **Bollinger + RSI**: Classic mean-reversion pair for range markets
5. **VWAP + MACD**: Intraday institutional bias + momentum confirmation

### Layering across timeframes

The most disciplined way to combine indicators is not just by category but by *timeframe*: use a slow trend tool on a high timeframe to set direction, then a fast oscillator on a lower timeframe to time entries. This is exactly the structure of Elder's [[triple-screen-system|Triple Screen]] (weekly [[macd|MACD]]-Histogram for trend, daily oscillator for timing) and the general principle of [[multi-timeframe-confluence]]. See the [[technical-analysis-overview]] strategy hub for the strategies that operationalise these combinations.

## Choosing an Indicator (decision aid)

| If you want to know... | Reach for | Avoid |
|---|---|---|
| *Which way is the market going?* | [[moving-averages]], [[macd]], [[ichimoku]] | Oscillators (they say nothing about direction) |
| *Is the trend strong enough to ride?* | [[adx]] | Lagging MAs alone |
| *Is price stretched (mean-reversion)?* | [[rsi]], [[stochastic]], [[bollinger-bands]] | Trend tools (they stay "overbought" in trends) |
| *How big should my stop / position be?* | [[atr]] | Fixed-point stops |
| *Are buyers/sellers actually participating?* | [[vwap]], [[obv]], [[chaikin-money-flow]] | Price-only indicators |
| *Is the whole market healthy?* | [[market-breadth]], [[mcclellan-oscillator]], [[arms-index]] | Single-stock indicators |
| *What's the volatility regime?* | [[vix]], [[bollinger-bands]] width, [[atr]] | — |

The pairing logic is to **combine across categories** (one trend + one momentum + one volume/volatility) so each indicator covers a different blind spot. Two indicators from the *same* category mostly repeat the same information.

## Win-Rate Snapshot (Illustrative)

One backtesting summary across US equities reported the following win rates. **Caveat**: win-rate alone is misleading — high-win-rate mean-reversion systems often have poor payoff ratios, while lower-win-rate trend systems generate most P&L from a few large winners.

| Indicator | Reported Win Rate | Type |
|---|---|---|
| RSI(14) | 79.4% | Mean-reversion |
| Bollinger Bands | 77.8% | Mean-reversion |
| Donchian Channels | 74.1% | Breakout |
| Williams %R | 71.7% | Mean-reversion |
| ADX | 53.6% | Trend filter |
| Stochastics | 44.9% | Mean-reversion |
| Parabolic SAR | 44.7% | Trend/exit |
| Ichimoku | 42.3% | Trend |
| MACD | 40.1% | Trend |
| CCI(20) | 35.1% | Momentum |
| EMA(50) | 30.7% | Trend |

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

## Limitations and Academic Perspective

Comparative studies find that while technical indicators (especially RSI, MACD, Bollinger) can identify short-term opportunities, their predictive power in commodity markets is mixed relative to fundamental factors, and most edges decay as more participants adopt them. No indicator is predictive in isolation — they are conditional tools whose value depends on regime, timeframe, and risk management. The enduring lesson from every pioneer — Homma, Dow, Wilder, Bollinger, Dennis — is that indicators serve discipline and position sizing, not prophecy (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Additional Frameworks

The following have dedicated strategy pages rather than indicator concept pages:
- [[elliott-wave]] — 5-wave impulse + 3-wave correction pattern theory ([[ralph-nelson-elliott]])
- [[parabolic-sar]] — Wilder's trailing stop/reversal dot system
- [[point-and-figure]] — De Villiers/Wheelan price-filter charting method

## All Indicator Pages

```dataview
TABLE status, updated, tags
FROM "wiki/concepts/indicators"
WHERE type != "index"
SORT updated DESC
```

## Related

- [[technical-analysis-overview]] — the strategy hub that turns these indicators into tradeable systems
- [[triple-screen-system]] — flagship method layering a trend indicator and an oscillator across timeframes
- [[multi-timeframe-confluence]] — the principle of confirming signals across timeframes
- [[regime-matrix]] — which indicator families fit which market regime
- [[rsi]], [[macd]], [[bollinger-bands]], [[vwap]], [[ichimoku]] — the most-used individual indicators
- [[candlestick-patterns]] — price-pattern reading that predates indicators

## Sources

- Robert D. Edwards & John Magee, *Technical Analysis of Stock Trends* (1948) — the foundational codification of Western chart analysis.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — standard reference covering the major indicator families.
- J. Welles Wilder Jr., *New Concepts in Technical Trading Systems* (Trend Research, 1978) — origin of RSI, ATR, ADX, and Parabolic SAR.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
