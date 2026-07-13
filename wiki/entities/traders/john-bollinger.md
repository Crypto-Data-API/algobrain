---
title: "John Bollinger"
type: entity
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [person, technical-analysis, indicators, volatility]
aliases: ["Bollinger"]
entity_type: person
founded: 1950
headquarters: "Manhattan Beach, California, USA"
website: "https://www.bollingerbands.com"
related: ["[[bollinger-bands]]", "[[bollinger-band-reversion]]", "[[volatility]]", "[[technical-analysis]]"]
---

# John Bollinger

John Bollinger (born 1950) is an American technical analyst, founder of Bollinger Capital Management, and creator of [[bollinger-bands|Bollinger Bands]] in the early 1980s. He entered finance via managing his mother's pension and went on to build an asset-management career and global publishing franchise on his bands (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). He was the first analyst to hold both the CFA and CMT designations, and his bands remain among the most widely used volatility indicators on every major charting platform.

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | John A. Bollinger |
| Born | 1950 (United States) |
| Nationality | American |
| Known for | [[bollinger-bands|Bollinger Bands]]; %b and BandWidth indicators; the "Squeeze" |
| Firm | Bollinger Capital Management (Manhattan Beach, California) |
| Early platform | Chief market analyst, Financial News Network (FNN), 1980s |
| Credentials | First to hold both **CFA** and **CMT** |
| Key book | *Bollinger on Bollinger Bands* (McGraw-Hill, 2001) |
| Discipline | [[technical-analysis]], [[volatility]], [[mean-reversion]] |
| Status | Active (publishing market commentary as of 2024–2026) |

## Overview

[[bollinger-bands|Bollinger Bands]] plot a 20-period SMA with upper/lower envelopes at ±2 standard deviations, adapting to realised volatility. Strategies include squeezes (volatility compression preceding breakouts), walking-the-band trend rides, and %b/BandWidth oscillators (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

Bollinger developed the bands while serving as chief market analyst at Financial News Network (FNN, the predecessor of CNBC) in the 1980s, where he appeared on air daily for several years. He later founded **Bollinger Capital Management**, a money-management and research firm based in Manhattan Beach, California, and published the *Capital Growth Letter*. He derived two companion indicators from the bands — **%b** (position of price within the bands) and **BandWidth** (band spread normalized by the middle band, used to define the Squeeze) — and operates BollingerBands.com as the official educational hub.

## The Method: How Bollinger Bands Work

Bollinger's key insight was that a trading band should *adapt to volatility* rather than sit at a fixed percentage distance from price. Earlier "trading bands" (e.g., percentage envelopes, and the percentage-band work of Marc Chaikin and others) used constant-width offsets that were too wide in quiet markets and too narrow in turbulent ones. Bollinger replaced the fixed offset with a measure of [[standard-deviation|standard deviation]] — a statistical estimate of dispersion — so the bands automatically widen when volatility rises and contract when it falls.

The default construction (20-period, 2 standard deviations) is:

```
Middle Band = SMA(close, 20)                          # 20-period simple moving average
σ           = standard deviation of the last 20 closes # population standard deviation
Upper Band  = Middle Band + 2 × σ
Lower Band  = Middle Band − 2 × σ
```

Because price relative to a moving average is roughly bell-shaped over short windows, the ±2σ envelope is expected to contain the large majority of recent closes; sustained excursions outside it flag either an unusually strong trend ("walking the band") or a stretched, mean-reverting extreme. Bollinger deliberately chose 20 periods and 2σ as defaults but stressed that they should be tuned per instrument and timeframe (a longer SMA warrants a wider multiplier).

Two derived indicators complete the toolkit:

- **%b** = (Price − Lower Band) / (Upper Band − Lower Band). This normalizes price to the bands: %b = 1 at the upper band, 0 at the lower band, 0.5 at the middle band, and can exceed 1 or fall below 0 during strong moves. It is the basis for relating price to the bands quantitatively (e.g., divergence and confirmation against [[rsi]] or [[macd]]).
- **BandWidth** = (Upper Band − Lower Band) / Middle Band. This measures the relative width of the bands. Extreme lows in BandWidth define the **Squeeze** — a volatility compression that historically precedes large directional expansion.

### Signature setups

- **The Squeeze**: BandWidth contracts to a multi-month low (volatility coils), then expands as a breakout begins. The direction is confirmed by price, volume, and %b rather than by the Squeeze itself.
- **Walking the band**: in strong trends price hugs (or rides above/below) one band; this is a *continuation* signal, not an exhaustion signal — a common beginner error is to fade it.
- **Band-tag mean reversion**: in range-bound markets, tags of the outer bands accompanied by momentum divergence offer [[mean-reversion]] entries (see [[bollinger-band-reversion]]).
- **M-tops and W-bottoms**: classic reversal shapes where the second extreme fails to make a new %b high/low, signalling waning momentum.

## Credentials and Recognition

- First practitioner to hold both the **CFA** (Chartered Financial Analyst) and **CMT** (Chartered Market Technician) designations
- Past contributor to and award recipient of the CMT Association (formerly Market Technicians Association); received its Annual Award in 1995 for outstanding contribution to technical analysis
- Active in the International Federation of Technical Analysts (IFTA)
- As of 2025–2026, still active publishing market commentary, interviews, and educational content via BollingerBands.com and social media

## Publications

Published *Bollinger on Bollinger Bands* (McGraw-Hill, 2001), translated into at least eight languages — the definitive treatment of the bands, the Squeeze, and the %b/BandWidth toolkit.

## Influence and Legacy

- **Ubiquity**: Bollinger Bands are a default overlay on virtually every charting platform (TradingView, MetaTrader, thinkorswim, Bloomberg, and others) and one of the handful of indicators that crossed from professional desks into mass retail use essentially unchanged.
- **A grammar for volatility**: by reframing "where is price?" as "where is price *relative to current volatility*?", Bollinger gave discretionary chartists a quantitative bridge toward statistical thinking — %b and BandWidth are still cited in systematic [[backtesting|backtests]] and volatility-regime models.
- **Cross-pollination with [[keltner-channels|Keltner Channels]]**: the popular **TTM Squeeze** combines Bollinger Bands and [[keltner-channels|Keltner Channels]] — when the standard-deviation bands contract *inside* the [[average-true-range|ATR]]-based Keltner Channel, it flags an unusually tight volatility coil. This pairing made Bollinger's work foundational to a whole sub-genre of squeeze trading (see [[bollinger-bands-vs-keltner-channels]]).
- **Educator and standard-bearer**: through *Bollinger on Bollinger Bands*, decades of media appearances, and BollingerBands.com, he shaped how a generation of traders reasons about [[volatility]] and risk.

## Trading Relevance

Bollinger Bands are core infrastructure for [[volatility]]-aware trading: mean-reversion entries at band extremes (see [[bollinger-band-reversion]]), Squeeze setups that anticipate volatility expansion, and trend confirmation when price "walks the band." Because the bands adapt to realised volatility rather than fixed percentages, they remain one of the few 1980s-era indicators still used essentially unchanged across equities, futures, forex, and crypto. They are frequently combined with momentum oscillators ([[rsi]], [[macd]]) and volume tools to filter false band tags, and with [[average-true-range|ATR]]-based stops for position management.

## Related

- [[bollinger-bands]]
- [[bollinger-band-reversion]]
- [[bollinger-bands-vs-keltner-channels]]
- [[standard-deviation]]
- [[volatility]]
- [[technical-analysis]]
- [[indicators-overview]]
- [[mean-reversion]]
- [[keltner-channels]]
- [[chester-keltner]]
- [[rsi]]
- [[macd]]
- [[average-true-range]]

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- John Bollinger, *Bollinger on Bollinger Bands* (McGraw-Hill, 2001)
- Official site — https://www.bollingerbands.com
- Verified via Perplexity (sonar), 2026-06-10 (born 1950; bands developed early 1980s at FNN; CFA + CMT; still active 2024–2026)
