---
title: "AAII Investor Sentiment Survey"
type: concept
created: 2026-04-22
updated: 2026-06-12
status: good
tags: [data-provider, sentiment, behavioral-finance, indicators]
aliases: ["AAII Sentiment Survey", "AAII Sentiment", "AAII Bull-Bear Spread"]
domain: [behavioral-finance, indicators]
source_url: "https://www.aaii.com/sentimentsurvey"
related: ["[[sentiment]]", "[[herding]]", "[[behavioral-finance]]", "[[contrarian-trading]]", "[[fear-and-greed-index]]", "[[cot-data]]", "[[market-bubbles]]", "[[momentum]]"]
---

The AAII Investor Sentiment Survey is a weekly poll conducted by the American Association of Individual Investors measuring the percentage of respondents who are bullish, neutral, or bearish on the stock market over the next six months. Published every Thursday since 1987, it is one of the oldest and most widely followed retail [[sentiment]] indicators and a key input for [[contrarian-trading|contrarian]] strategies.

## Overview

Each week, AAII polls its membership (individual investors, not professionals) with a simple question: "Do you feel the direction of the stock market over the next six months will be up (bullish), no change (neutral), or down (bearish)?" The results are published as three percentages that sum to 100%.

### Historical Averages (1987-present)

| Sentiment | Historical Average |
|---|---|
| Bullish | ~37.5% |
| Neutral | ~31.5% |
| Bearish | ~31.0% |

The **bull-bear spread** (bullish % minus bearish %) averages approximately +6.5 percentage points.

## Contrarian Signal

The AAII survey's primary value is as a **contrarian indicator**. Extreme sentiment readings have historically preceded market reversals:

### Bullish Extremes (Bearish Signal)

When bullish sentiment exceeds ~50%:
- Most potential retail buyers have already committed capital
- Positioning is crowded on the long side
- Expectations are elevated, making disappointment more likely
- Historical data shows below-average forward 1-3 month S&P 500 returns after extreme bullish readings

### Bearish Extremes (Bullish Signal)

When bearish sentiment exceeds ~50%:
- Retail investors have already sold or are heavily hedged
- Cash levels are elevated (potential fuel for a rally)
- Expectations are depressed, making positive surprises more likely
- Historical data shows above-average forward 1-3 month returns after extreme bearish readings

### Notable Readings

- **March 2009** (market bottom): Bearish sentiment hit ~70%, one of the highest readings in survey history. The S&P 500 subsequently rallied over 60% in 12 months
- **January 2000** (near market top): Bullish sentiment exceeded 75%. The Nasdaq subsequently lost over 75% of its value
- **COVID crash (March 2020)**: Bearish sentiment spiked above 50%, preceding one of the fastest market recoveries in history

## Limitations

1. **Not a timing tool**: Extreme readings can persist for weeks or months. Sentiment is a condition, not a trigger — it tells you the environment is ripe for reversal, not when the reversal will begin
2. **Self-selection bias**: AAII members are a specific demographic (older, wealthier, US-based individual investors). Their sentiment may not represent broader market positioning
3. **Small sample size**: Typical weekly responses number in the hundreds, not thousands
4. **Retail only**: The survey does not capture institutional sentiment. Pair with [[cot-data|COT data]] for a more complete positioning picture
5. **Behavioral regime changes**: The relationship between sentiment and returns may weaken in periods of extreme intervention (e.g., Fed QE) or structural market changes

## How to Use in Practice

| Approach | Method |
|---|---|
| Contrarian filter | Avoid new long entries when bullish >50%; look for longs when bearish >50% |
| Bull-bear spread | Track the spread vs. its moving average; extreme deviations are more meaningful than absolute levels |
| Confirmation tool | Use alongside [[cot-data\|COT positioning]], put/call ratios, and [[fear-and-greed-index\|Fear & Greed Index]] for multi-source sentiment confirmation |
| Mean reversion | Extreme sentiment readings revert to the mean — the question is when, not if |

## Data Access

- **Free**: Current and historical data available at [aaii.com/sentimentsurvey](https://www.aaii.com/sentimentsurvey)
- **Frequency**: Published every Thursday at 12:30 PM ET
- **Historical data**: Downloadable for AAII members; summary data widely available

## Related

- [[sentiment]] — the broader concept of market mood measurement
- [[herding]] — the behavioral mechanism that drives sentiment to extremes
- [[contrarian-trading]] — the strategy framework that uses extreme sentiment readings
- [[cot-data]] — complementary institutional/speculative positioning data
- [[fear-and-greed-index]] — CNN's multi-factor sentiment composite
- [[market-bubbles]] — extreme bullish sentiment often accompanies bubble formation
- [[behavioral-finance]] — the field explaining why sentiment indicators work

## Sources

*No raw sources ingested yet. This page is based on publicly available AAII survey data and historical analysis.*
