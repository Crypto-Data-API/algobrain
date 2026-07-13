---
title: Bollinger Bands
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [bollinger-bands, indicators, volatility]
aliases: [BB]
domain: [indicators]
prerequisites: ["[[volatility]]", "[[moving-averages]]"]
difficulty: beginner
related:
  - "[[moving-averages]]"
  - "[[volatility]]"
  - "[[atr]]"
  - "[[support-and-resistance]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[john-murphy]]"
  - "[[john-bollinger]]"
  - "[[commodities]]"
  - "[[natural-gas]]"
  - "[[gold]]"
  - "[[intermarket-analysis]]"
  - "[[keltner-channels]]"
  - "[[rsi]]"
---

# Bollinger Bands

Bollinger Bands are a [[volatility]] indicator consisting of a middle [[moving-averages|moving average]] band with upper and lower bands set at a specified number of standard deviations away.

## Overview

Created by John Bollinger in the 1980s, Bollinger Bands dynamically expand and contract based on market volatility (Source: [[book-technical-analysis-of-the-financial-markets]]). The default settings use a 20-period SMA as the middle band, with upper and lower bands at 2 standard deviations. Under a normal distribution, ±2 standard deviations would contain ~95% of observations, but Bollinger himself documented that in practice only about 88–89% of price action falls within the bands — because financial returns are fat-tailed (leptokurtic) rather than normally distributed.

## How It Works

- **Upper band**: 20-period SMA + (2 x standard deviation). Acts as dynamic resistance.
- **Middle band**: 20-period SMA. Acts as a mean-reversion target.
- **Lower band**: 20-period SMA - (2 x standard deviation). Acts as dynamic support.
- **Band width**: The distance between upper and lower bands measures current volatility.

## Key Signals

- **Squeeze**: Bands narrow significantly, indicating low volatility and compressed price action. A squeeze often precedes a large breakout move -- though it does not predict direction.
- **Breakout**: Price closing outside the bands can signal the start of a strong trending move or an overextended condition ripe for reversal. Context determines interpretation.
- **Walking the bands**: In strong trends, price can "ride" the upper or lower band for extended periods without it being a reversal signal.
- **W-bottoms and M-tops**: Bollinger identified double-bottom and double-top patterns formed relative to the bands as high-probability reversal setups.

## Trading Relevance

Bollinger Bands are most effective when combined with other indicators. A squeeze followed by a breakout confirmed by [[volume]] and [[momentum]] signals is a high-conviction setup. Mean-reversion traders buy at the lower band and sell at the upper band during range-bound conditions. Band width can be used as input for [[position-sizing]] -- trade smaller when bands are wide (high vol) and larger when narrow (low vol, pre-breakout).

## Commodity Applications

Bollinger Bands are particularly useful for commodity volatility assessment, where price distributions tend to be more leptokurtic (fat-tailed) than equities and volatility clustering is pronounced (Source: [[book-technical-analysis-of-the-financial-markets]]).

**Squeeze setups** in commodities are among the most watched signals:

- **[[natural-gas]]** squeezes before seasonal demand shifts (heading into winter heating season or summer cooling season) frequently precede 20-40% moves. Band width contracting to multi-month lows on weekly natural gas charts is a signal that CTAs actively monitor.
- **[[gold]]** squeezes before FOMC decisions and major macro announcements are widely tracked. Gold's tendency to compress into tight ranges ahead of interest rate decisions, then explode in one direction, makes Bollinger Band width a valuable timing tool for precious metals traders.
- **Agricultural commodities** often squeeze ahead of [[usda|USDA]] WASDE reports, with band width narrowing as traders await the fundamental catalyst.

**Band width as a strategy input**: Bollinger Band width on weekly commodity charts can serve as an input for [[commodity-momentum]] strategies -- narrow bands signal potential explosive moves and can be used as a position-sizing multiplier (wider expected move = smaller initial position, scale in after breakout direction is confirmed). Conversely, extremely wide bands (high volatility) in commodities often coincide with capitulation and can be contrarian entry signals for mean-reversion strategies.

The **Bollinger Band/[[keltner-channels|Keltner Channel]] squeeze** -- where Bollinger Bands contract inside Keltner Channels -- is a refined version of the squeeze that works well across commodity markets and is built into many CTA systematic models.

## About the Creator

[[john-bollinger|John Bollinger]], founder of Bollinger Capital Management, entered finance via managing his mother's pension and built an asset-management career and global publishing franchise on his bands. He published *Bollinger on Bollinger Bands* (2001), translated into eight languages, which codified the squeeze, walking-the-band, and **%b/BandWidth** oscillator strategies. %b measures where price sits relative to the bands (0 = lower band, 1 = upper band), while BandWidth quantifies the distance between bands as a percentage of the middle band — a key input for squeeze detection (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study across US equities reported Bollinger Bands with a 77.8% win rate — the second highest among all indicators tested, reflecting the effectiveness of mean-reversion strategies at the bands in range-bound regimes. As with all high-win-rate mean-reversion systems, the payoff ratio tends to be modest (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

**Bollinger + [[rsi|RSI]]** is a classic mean-reversion pair: price touching the lower band while RSI is oversold creates a high-probability bounce setup (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- John Bollinger, *Bollinger on Bollinger Bands* (McGraw-Hill, 2001) — the definitive treatment by the creator, covering %b, BandWidth, the squeeze, walking-the-band, and W-bottom/M-top patterns.
- bollingerbands.com — John Bollinger's official site and "22 Rules" for using the bands.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — covers Bollinger Bands as a volatility envelope tool.
- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers Bollinger Bands as a volatility envelope tool, including squeeze setups, band-walking behavior, and W-bottom/M-top pattern recognition
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Bollinger biographical details, %b/BandWidth oscillators, win-rate data, Bollinger+RSI combination

## Related

- [[volatility]] -- bands measure and visualize volatility
- [[moving-averages]] -- the middle band is an SMA
- [[atr]] -- complementary volatility measure
- [[support-and-resistance]] -- bands act as dynamic S/R
- [[bollinger-bands-vs-keltner-channels]] -- comparison with the ATR-based Keltner Channel alternative
- [[commodities]] -- bands are widely used for commodity volatility assessment
- [[natural-gas]] -- squeeze setups before seasonal shifts
- [[gold]] -- squeezes before FOMC decisions
- [[keltner-channels]] -- the BB/KC squeeze is a refined volatility setup
- [[intermarket-analysis]] -- band width comparisons across related commodities
- [[john-murphy]] -- covers Bollinger Bands in his volatility analysis framework
