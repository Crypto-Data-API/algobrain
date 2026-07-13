---
title: "Ichimoku Cloud"
type: strategy
created: 2026-04-06
updated: 2026-04-20
status: good
tags: [trend-following, ichimoku, japanese-analysis, cloud, technical-analysis, support-resistance]
aliases: ["Ichimoku Kinko Hyo", "Ichimoku Cloud Strategy", "Kumo Trading"]
strategy_type: technical
timeframe: swing|position
markets: [stocks, crypto, forex]
complexity: intermediate
backtest_status: untested
related: ["[[moving-average-crossover]]", "[[supertrend]]", "[[support-and-resistance]]", "[[parabolic-sar]]", "[[goichi-hosoda]]", "[[ichimoku]]"]
---

# Ichimoku Cloud

## Overview

Ichimoku Kinko Hyo ("one glance equilibrium chart") is a comprehensive Japanese technical analysis system developed by journalist [[goichi-hosoda|Goichi Hosoda]] (pen name "Ichimoku Sanjin") in the late 1930s and published in a 7-volume series beginning 1969 after three decades of refinement. Hosoda paired the indicator system with three additional theoretical frameworks: Time Theory, Wave Theory, and Price (Target) Theory (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). Unlike most indicators that measure only one dimension (trend, momentum, or support/resistance), Ichimoku provides all three in a single view. It has become enormously popular in [[crypto]] trading and [[forex]] markets.

The system consists of five lines:
- **Tenkan-Sen (Conversion Line):** (9-period high + 9-period low) / 2. Fast signal line.
- **Kijun-Sen (Base Line):** (26-period high + 26-period low) / 2. Slower signal line and key support/resistance.
- **Senkou Span A (Leading Span A):** (Tenkan + Kijun) / 2, plotted 26 periods ahead. First cloud boundary.
- **Senkou Span B (Leading Span B):** (52-period high + 52-period low) / 2, plotted 26 periods ahead. Second cloud boundary.
- **Chikou Span (Lagging Span):** Current close plotted 26 periods behind. Confirmation line.

The area between Senkou Span A and B forms the **Kumo (Cloud)**, which is the defining visual feature and the heart of the system.

## Rules

### Entry
1. **Strong Bullish Signal:** Price is above the cloud, Tenkan-Sen crosses above Kijun-Sen (TK Cross) while above the cloud, and Chikou Span is above price from 26 periods ago. All five conditions align bullish.
2. **Strong Bearish Signal:** Price is below the cloud, Tenkan-Sen crosses below Kijun-Sen while below the cloud, and Chikou Span is below price from 26 periods ago.
3. **Kumo Breakout:** Price breaks above/below the cloud after being inside it. The thicker the cloud at the breakout point, the more significant the signal.
4. **Kumo Twist:** When Senkou Span A crosses Senkou Span B, the cloud changes color (bullish to bearish or vice versa). This signals a potential trend change and often occurs before price confirms.

### Exit
1. **TK Cross Reversal:** Tenkan-Sen crosses back through Kijun-Sen in the opposite direction.
2. **Cloud Re-entry:** Price re-enters the cloud from above (for longs) or below (for shorts).
3. **Kijun-Sen as Stop:** The Kijun-Sen (Base Line) serves as a natural trailing stop. Exit if price closes beyond it.
4. **Chikou Confirmation Loss:** If Chikou Span crosses back through historical price, the trend is weakening.

### Position Sizing
Risk 1-2% per trade. Use the Kijun-Sen or the opposite edge of the cloud as the stop-loss level.

## Indicators Used
- **Ichimoku Kinko Hyo** (all five components)
- [[volume]] for breakout confirmation
- [[rsi]] or [[macd]] as supplementary momentum filters (optional)

## Example Trade
**Asset:** BTC/USD, daily chart
1. BTC has been trading inside the cloud (indecision zone) for two weeks. The cloud is turning bullish (Kumo twist: Span A crossing above Span B).
2. BTC breaks above the cloud top at $45,000. Tenkan-Sen ($44,200) is above Kijun-Sen ($43,500). Chikou Span is above the price from 26 days ago. All signals align bullish.
3. Enter long at $45,200. Set stop-loss at the Kijun-Sen: $43,500 (risk of ~$1,700, or 3.8%).
4. BTC trends to $52,000 over 3 weeks. The Kijun-Sen trails upward to $48,000. Adjust stop to $48,000.
5. BTC pulls back sharply. Price closes below the Kijun-Sen at $47,800. Exit.
6. **Result:** Entry $45,200, exit $47,800 = +$2,600 (5.8% gain) with risk managed by the trailing Kijun.

## Performance Characteristics
- **Win Rate:** 45-55%. The multi-factor confirmation filters out many false signals.
- **Profit Factor:** 1.5-2.5. Strong signals (all five lines aligned) have significantly higher success rates.
- **Best Market Conditions:** Trending markets with clear directional momentum. Crypto markets where Ichimoku is widely followed.
- **Worst Market Conditions:** Tight, choppy ranges where price oscillates around the Kijun-Sen and within a thin cloud.

## Advantages
- Provides trend direction, momentum, and [[support-and-resistance]] in a single indicator
- The cloud visualizes future support/resistance zones (plotted 26 periods ahead)
- The Chikou Span acts as unique backward-looking confirmation found in no other indicator
- Multi-factor confirmation (5 lines must agree) produces higher-quality signals than single-indicator systems
- Extremely popular in crypto -- widespread adoption creates self-reinforcing levels

## Disadvantages
- **Visually complex:** The five overlapping lines and shaded cloud overwhelm beginners
- **Default parameters** (9, 26, 52) were designed for Japanese markets trading 6 days/week. Some traders adjust to 10, 30, 60 for modern 5-day markets or 20, 60, 120 for crypto (24/7)
- **Lagging:** Like all MA-based systems, signals arrive after the trend has started
- **Wide stops:** Using the Kijun-Sen or cloud edge as a stop can mean large risk per trade
- Performs poorly in range-bound conditions when price chops through the cloud repeatedly

## Backtesting Evidence

One illustrative backtesting study across US equities reported a 42.3% win rate for Ichimoku signals. The low win rate is expected for a trend-following system — Ichimoku generates most of its P&L from a few large trending winners, while producing many small losses during choppy conditions. Long dominant in Japanese equities and FX, the system spread globally only in the 1990s due to translation lag (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

For the indicator concept page, see [[ichimoku]].

## See Also
- [[moving-average-crossover]] -- a simpler trend system; the TK Cross is conceptually similar
- [[supertrend]] -- a cleaner, single-line trend indicator for traders who find Ichimoku too busy
- [[support-and-resistance]] -- the cloud provides dynamic S/R levels
- [[parabolic-sar]] -- another always-in-market trend indicator
- [[goichi-hosoda]] -- Ichimoku's creator
