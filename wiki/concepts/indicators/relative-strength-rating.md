---
title: "Relative Strength Rating"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [momentum, technical-analysis, indicators, stock-screening]
aliases: ["relative strength rating", "RS rating", "RS line", "relative-strength-rating"]
domain: [technical-analysis]
difficulty: beginner
related: ["[[relative-strength]]", "[[ibd]]", "[[canslim]]", "[[momentum-screening]]", "[[momentum-trading]]"]
---

The Relative Strength Rating (RS Rating) is a proprietary metric developed by [[ibd|Investor's Business Daily]] that ranks a stock's price performance against all other stocks in the database on a scale of 1 to 99. A stock with an RS Rating of 95 has outperformed 95% of all stocks over the trailing 12-month period. The metric was created by William O'Neil as a core component of his [[canslim|CANSLIM]] investment methodology and remains one of the most widely used momentum ranking tools in growth stock investing.

## How the RS Rating Is Calculated

The RS Rating compares a stock's 12-month price change to all other stocks and assigns a percentile rank. Critically, the calculation weights recent performance more heavily:

- **Last 3 months**: ~40% of the weight
- **Prior 3 months (months 4-6)**: ~20%
- **Prior 3 months (months 7-9)**: ~20%
- **Prior 3 months (months 10-12)**: ~20%

This weighting scheme means a stock that has accelerated in the most recent quarter will have a higher RS Rating than one with the same total 12-month return but whose strength came earlier. The recency bias is intentional — O'Neil's research found that stocks beginning major advances typically show accelerating relative strength in the months leading up to the move.

## RS Rating vs. RSI

The RS Rating and the [[rsi|Relative Strength Index (RSI)]] are frequently confused despite measuring completely different things:

| | RS Rating | RSI |
|---|---|---|
| **What it measures** | Stock performance vs. all other stocks | Overbought/oversold of a single stock vs. itself |
| **Scale** | 1-99 (percentile rank) | 0-100 (oscillator) |
| **Lookback** | 12 months, weighted | Typically 14 periods |
| **Interpretation** | Higher = stronger vs. market | Above 70 = overbought, below 30 = oversold |
| **Creator** | William O'Neil / [[ibd]] | J. Welles Wilder |

A stock can have an RS Rating of 95 (massive outperformance vs. the market) and an RSI of 75 (overbought in the short term) simultaneously. They answer different questions.

## The RS Line

Closely related to the RS Rating is the **RS Line**, which plots a stock's price divided by the S&P 500 index over time. A rising RS Line means the stock is outperforming the S&P 500; a falling RS Line means underperformance. The RS Line is displayed on every IBD stock chart and is one of the first things CANSLIM practitioners check.

Key RS Line signals:
- **RS Line at a new high before price reaches a new high** — Bullish. The stock is outperforming even before breaking out, suggesting strong institutional accumulation.
- **RS Line declining while price rises** — Bearish divergence. The stock is going up but lagging the market — a warning sign that the rally may not have legs.
- **RS Line in a sustained uptrend** — Confirms the stock is a genuine leader, not just riding a bull market tide.

## O'Neil's RS Rating Selection Criteria

In the [[canslim|CANSLIM methodology]], O'Neil recommends buying only stocks with an RS Rating of **80 or higher** — meaning the stock is outperforming at least 80% of all stocks. His research on historical superperformers (stocks that doubled or more) found that the median RS Rating at the start of their major advances was 87. Stocks with RS Ratings below 70 were rarely worth buying for growth purposes.

## Using RS Ratings in Momentum Screens

The RS Rating is a natural fit for [[momentum-screening]] because it provides a pre-computed, normalized momentum rank. In a systematic screen, typical implementation includes:

- **Minimum RS Rating threshold** (e.g., RS ≥ 80) as a binary pass/fail filter
- **RS Rating as a ranking factor** within stocks passing other screens (higher RS = better rank)
- **RS Rating trend** — a stock whose RS Rating has risen from 70 to 90 over the past 3 months shows accelerating momentum, which is more bullish than a stock that has been at 90 for six months

## Limitations

The RS Rating is backward-looking — it measures what has already happened. A stock that crashed 50% this week but was a strong performer for the prior 11 months may still show a high RS Rating until the data catches up. It also does not account for [[volatility]] — a stock that doubled but with 60% drawdowns along the way gets the same RS Rating as one that rose steadily.

## Related

- [[relative-strength]] — The broader concept of comparative performance measurement
- [[canslim]] — O'Neil's full methodology, where RS Rating is a key selection criterion
- [[momentum-screening]] — RS Rating is a core input in systematic momentum screens
- [[ibd]] — Publisher and data provider for RS Ratings

## Sources

- O'Neil, W. J., *How to Make Money in Stocks* (4th ed.) — the definitive source for RS Rating, the RS Line, and the CANSLIM selection thresholds
- Investor's Business Daily, "IBD Relative Strength Rating" educational materials — official description of the 1-99 percentile metric
- Greenblatt et al. and the broader momentum literature (e.g., Jegadeesh & Titman, 1993) — academic basis for the recency-weighted relative-strength effect
