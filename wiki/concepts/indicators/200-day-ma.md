---
title: "200-Day Moving Average"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [technical-analysis, indicators, moving-averages, trend]
aliases: ["200-day MA", "200-day SMA", "200-day moving average", "200-day-MA", "200 DMA", "200 Day Moving Average", "200-day-moving-average"]
domain: [indicators]
prerequisites: ["[[moving-averages]]"]
difficulty: beginner
related: ["[[moving-averages]]", "[[golden-cross]]", "[[death-cross]]", "[[trend]]", "[[momentum-screening]]", "[[relative-strength]]", "[[support-and-resistance]]"]
---

The 200-day moving average (200 DMA) is the single most widely watched [[technical-analysis|technical indicator]] in equity markets. It represents the average closing price over the past 200 trading days — approximately 10 calendar months, or roughly one full trading year — and serves as the primary dividing line between bullish and bearish long-term trends. Its ubiquity is self-reinforcing: because so many market participants watch the 200 DMA, it frequently acts as [[support-and-resistance|support or resistance]], making it a genuine factor in price action.

## Why 200 Days

The 200-day lookback period was popularized by technical analysts in the mid-20th century for several practical reasons:

- **Roughly one trading year** — There are approximately 252 trading days per year. A 200-day average captures most of the annual price action while smoothing out seasonal effects and short-term noise.
- **Smoothness** — Shorter averages (20, 50 days) are responsive but noisy. The 200 DMA changes slowly, making it a reliable indicator of the underlying trend direction rather than short-term fluctuations.
- **Institutional adoption** — Because it became the standard, institutional fund managers, risk committees, and algorithmic trading systems all reference it, creating a feedback loop of relevance.

## Trend Identification

The simplest and most common use of the 200 DMA is as a binary trend filter:

- **Price above the 200 DMA** — The stock or index is in a long-term uptrend. Bullish bias.
- **Price below the 200 DMA** — The stock or index is in a long-term downtrend. Bearish bias.

This filter alone has historically improved risk-adjusted returns. Faber (2007) demonstrated that a simple strategy of holding the S&P 500 only when it trades above its 10-month moving average (roughly equivalent to the 200 DMA) produced equity-like returns with significantly reduced drawdowns, avoiding the worst of bear markets.

## Golden Cross and Death Cross

Two of the most recognizable signals in [[technical-analysis]] involve the 200 DMA and the 50-day moving average:

- **Golden Cross** — The 50 DMA crosses above the 200 DMA. Interpreted as a bullish signal confirming the start of a new uptrend. Historical examples include the S&P 500 golden cross in June 2020, which preceded a strong rally.
- **Death Cross** — The 50 DMA crosses below the 200 DMA. Interpreted as a bearish signal confirming a downtrend. The S&P 500 death cross in March 2022 preceded several months of further decline.

These signals are lagging by nature — by the time the cross occurs, a significant portion of the move has already happened. Their primary value is in confirming trend changes rather than predicting them.

## Institutional Risk Management

Many institutional investors and fund managers use the 200 DMA as a risk management overlay:

- **Reducing equity exposure** when the S&P 500 drops below its 200 DMA — a common rule in tactical asset allocation
- **Avoiding individual stocks** trading below their 200 DMA, as these are in confirmed downtrends regardless of fundamental attractiveness
- **Stop-loss reference** — some systematic strategies use a close below the 200 DMA as a sell signal for individual positions

The widespread institutional use of this level explains why the S&P 500 frequently bounces at or near its 200 DMA during bull market corrections — institutional buying programs kick in at this level.

## Use in Momentum Screens

In [[momentum-screening]], the 200 DMA functions as a binary pass/fail filter rather than a ranked criterion. The rule is straightforward: **only consider stocks trading above their 200 DMA**. This eliminates stocks in structural downtrends, even those showing short-term price strength from a dead-cat bounce or oversold rally. In the [[sector-rotation|sector rotation + momentum screen]] framework, the 200 DMA filter typically receives a 10% weight as a binary qualifier.

## SMA vs. EMA

The standard 200 DMA uses a [[simple-moving-average|simple moving average]] (SMA), weighting all 200 days equally. Some traders prefer the 200-day [[exponential-moving-average|exponential moving average]] (EMA), which weights recent prices more heavily, making it slightly more responsive to current conditions. In practice, the difference between the 200-day SMA and 200-day EMA is usually small (a few percentage points at most), and both serve the same trend-identification purpose. The SMA remains the institutional standard.

## Related

- [[moving-averages]] — The family of indicators to which the 200 DMA belongs
- [[trend]] — The 200 DMA is the primary tool for identifying long-term trend direction
- [[momentum-screening]] — Uses the 200 DMA as a trend confirmation filter
- [[support-and-resistance]] — The 200 DMA frequently acts as a dynamic support/resistance level

## Sources

- Faber, Mebane T. (2007), "A Quantitative Approach to Tactical Asset Allocation," *Journal of Wealth Management* — demonstrates that holding the S&P 500 only when it trades above its 10-month (≈200-day) moving average produces equity-like returns with materially lower drawdowns.
- Murphy, John J. (1999), *Technical Analysis of the Financial Markets* (NYIF) — treats the 200-day MA as the primary long-term trend filter and dynamic support/resistance level.
- Brock, Lakonishok & LeBaron (1992), "Simple Technical Trading Rules and the Stochastic Properties of Stock Returns," *Journal of Finance* — early academic evidence on the predictive value of moving-average crossover rules including the 50/200 system.
