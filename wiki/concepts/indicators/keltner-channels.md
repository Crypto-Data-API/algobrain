---
title: "Keltner Channels"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [technical-analysis, indicators, volatility]
aliases: ["Keltner Channel", "Keltner Bands"]
related: ["[[bollinger-bands]]", "[[atr]]", "[[exponential-moving-average]]", "[[trend-following]]", "[[volatility]]", "[[squeeze]]"]
domain: [technical-analysis]
difficulty: intermediate
---

Keltner Channels are a volatility-based envelope indicator consisting of three lines: a central [[exponential-moving-average|EMA]] (typically 20-period) with upper and lower bands set at a multiple of the [[atr|Average True Range]] above and below it. Developed by Chester Keltner in the 1960s and modernized by Linda Raschke, Keltner Channels provide dynamic overbought/oversold zones and trend-strength signals. They are similar in concept to [[bollinger-bands]] but use ATR rather than standard deviation, giving them different sensitivity characteristics.

## Overview

The original Keltner Channel used a 10-period SMA with bands at the high-low range. The modern version, popularized by [[linda-raschke]], uses:

- **Centerline**: 20-period EMA
- **Upper Band**: 20-EMA + (1.5 x ATR(10))
- **Lower Band**: 20-EMA - (1.5 x ATR(10))

The ATR multiplier and EMA period are adjustable. Common settings include 1.5x ATR (tighter, more signals) and 2.0x ATR (wider, fewer but higher-quality signals).

Because the [[atr]] measures actual price range including gaps, Keltner Channels adapt to the true volatility of the instrument. In high-volatility environments, the channels widen; in low-volatility environments, they narrow. This adaptive quality makes them useful across different instruments and timeframes without constant parameter adjustment.

## How It Works

### Trend Identification

The centerline (20-EMA) determines the trend direction:
- **Rising EMA with price above it**: uptrend
- **Falling EMA with price below it**: downtrend
- **Flat EMA with price oscillating around it**: range-bound

The angle and slope of the channels themselves provide additional information. In a strong trend, the bands angle sharply and price rides along the outer band. In a weak or failing trend, the bands flatten and price gravitates toward the centerline.

### Overbought/Oversold Zones

Price reaching or exceeding the upper band suggests the market is stretched above its average -- potentially overbought. Price at the lower band suggests it is stretched below -- potentially oversold. However, the interpretation depends on the trend context:

- **In a strong trend**: price touching the outer band is a sign of strength, not reversal. Pullbacks to the centerline (20-EMA) are buying/selling opportunities.
- **In a range**: price touching the outer bands is more likely to mean-revert. Fade moves at the bands, target the centerline.

### Channel Breakouts

A decisive close beyond the upper or lower Keltner Channel can signal the start of a new trend or a momentum acceleration:
- Close above the upper band in a rising market suggests strong bullish momentum
- Close below the lower band in a declining market suggests accelerating selling pressure
- Multiple consecutive closes outside the band confirm the trend's strength

### Keltner Channels vs. Bollinger Bands

| Feature | Keltner Channels | [[bollinger-bands]] |
|---------|-----------------|---------------------|
| Centerline | EMA | SMA |
| Band width | ATR-based | Standard deviation-based |
| Sensitivity to spikes | Lower (ATR smooths outliers) | Higher (SD amplifies outliers) |
| Band shape | Smoother | More reactive/jagged |
| Squeeze detection | Used as the outer reference | Used as the inner reference |

The smoother nature of Keltner Channels makes them better for trend-following applications, while Bollinger Bands' greater reactivity suits mean-reversion and volatility-expansion trades.

### The Squeeze (TTM Squeeze)

One of the most popular uses of Keltner Channels is in the **Squeeze** setup (developed by John Carter):
- When [[bollinger-bands]] contract inside the Keltner Channels, the market is in a low-volatility "squeeze"
- This compression signals that a significant directional move is building
- The squeeze "fires" when the Bollinger Bands expand back outside the Keltner Channels
- The direction of the move is determined by momentum indicators (e.g., a momentum oscillator or [[macd]])

The Squeeze is powerful because it identifies the transition from low [[volatility]] to high volatility -- exactly when trend-following entries are most favorable.

## Trading Applications

### Keltner Channel Breakout Strategy
1. Wait for price to close above the upper Keltner Channel
2. Confirm the trend is rising (20-EMA sloping up)
3. Enter long on the next bar
4. Set stop below the lower Keltner Channel or the centerline (20-EMA)
5. Trail stop using the centerline -- exit if price closes below the 20-EMA

### Pullback to Centerline
1. Identify a trending market (price consistently above/below the 20-EMA)
2. Wait for a pullback to the 20-EMA centerline
3. Enter when price bounces off the centerline with a confirming [[candlestick-patterns|candlestick pattern]]
4. Stop below the recent swing low (uptrend) or above swing high (downtrend)
5. Target the outer band or a measured move

### Squeeze Setup
1. Identify when Bollinger Bands are inside Keltner Channels (the squeeze is on)
2. Wait for the squeeze to fire (Bollinger Bands expand outside Keltner)
3. Enter in the direction of the momentum reading
4. Stop on the opposite side of the centerline
5. Target 1-2x the height of the Keltner Channel at the squeeze point

### Limitations
- Like all envelope indicators, Keltner Channels lag the market
- In strongly trending markets, price can ride the outer band for extended periods, making the bands ineffective as reversal signals
- The ATR lookback and multiplier require optimization for different instruments and timeframes
- False squeeze signals can occur in low-volatility, directionless markets

## Related

- [[bollinger-bands]] -- standard deviation-based volatility bands
- [[atr]] -- the volatility measure underlying Keltner band width
- [[exponential-moving-average]] -- the centerline of Keltner Channels
- [[volatility]] -- the broader concept Keltner Channels measure
- [[trend-following]] -- strategy style that benefits from Keltner breakouts
- [[linda-raschke]] -- popularized the modern Keltner Channel formulation
- [[bollinger-bands-vs-keltner-channels]] -- detailed comparison of these two volatility band indicators

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- context for volatility-based indicators and channel analysis
