---
title: "Market Neutral"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [portfolio-theory, hedge-funds, risk-management]
aliases: ["Market Neutral Strategy", "Market-Neutral", "Zero Beta"]
related: ["[[long-short-equity]]", "[[pairs-trading]]", "[[ed-thorp]]", "[[delta-neutral]]", "[[statistical-arbitrage]]", "[[hedging]]", "[[beta]]"]
domain: [portfolio-theory, risk-management]
difficulty: advanced
---

**Market neutral** refers to a portfolio construction approach that aims for zero (or near-zero) exposure to overall market movements. A market-neutral portfolio is designed to generate returns from stock selection, relative value, or structural inefficiencies, rather than from the direction of the broad market. It is a foundational concept in [[hedge-funds|hedge fund]] investing and [[quantitative]] finance.

## Overview

The core idea is simple but powerful: if a portfolio has no net market exposure, its returns are independent of whether the market goes up or down. The portfolio profits only from the manager's ability to identify mispricings -- buying undervalued securities and shorting overvalued ones, with the long and short sides roughly offsetting each other's market risk.

[[ed-thorp|Ed Thorp]] pioneered market-neutral investing in the late 1960s and 1970s, first with convertible bond arbitrage and later with [[statistical-arbitrage]]. His Princeton Newport Partners fund demonstrated that consistent, low-volatility returns were achievable by carefully neutralizing market exposure. This approach directly influenced the development of the modern hedge fund industry.

Market neutrality can be defined in several ways, each with different levels of precision:

- **Dollar neutral**: Equal dollar amounts long and short (e.g., $10M long, $10M short). Simple but imprecise -- a portfolio of high-beta longs and low-beta shorts would still have significant market exposure.
- **Beta neutral**: The weighted beta of the long portfolio equals the weighted beta of the short portfolio. More precise than dollar neutral because it accounts for each stock's sensitivity to the market.
- **Factor neutral**: Neutral not only to the market but to additional risk factors such as size, value, momentum, and sector. This is the most rigorous definition and the one used by sophisticated quantitative funds.

## How It Works

### Constructing a Market-Neutral Portfolio

1. **Identify longs and shorts**: Use a ranking model (fundamental, quantitative, or hybrid) to identify securities expected to outperform (go long) and underperform (go short).
2. **Size positions to achieve neutrality**: Adjust position sizes so that the portfolio's net beta (or net dollar exposure) is approximately zero. If longs have higher average beta, the short side needs more dollar exposure to compensate.
3. **Maintain neutrality over time**: As prices change, betas shift and new positions are added or removed. Continuous monitoring and rebalancing is required to stay neutral.
4. **Manage residual exposures**: Even a beta-neutral portfolio may have unintended exposures to sectors, factors, or countries. Multi-factor risk models help identify and neutralize these residual risks.

### Sources of Return

A market-neutral portfolio generates returns from:

- **Alpha (stock selection)**: The long stocks outperform the short stocks on average. This is the primary intended source of return.
- **Short rebate**: Cash from short sales earns interest (the "short rebate"), which contributes to returns, especially in higher interest rate environments.
- **Leverage**: Because the market risk is hedged, managers can apply leverage to amplify the (hopefully positive) alpha. This is why market-neutral funds often use 2-4x gross leverage.
- **Mean reversion**: Many market-neutral strategies exploit short-term mean reversion -- buying recent losers and shorting recent winners within a sector or factor group.

### Risks

Market neutral does not mean risk-free:

- **Model risk**: If the ranking model is wrong, longs underperform shorts and the fund loses money regardless of market direction.
- **Short squeeze risk**: Short positions can experience rapid, forced covering if a stock rallies sharply, creating outsized losses.
- **Crowding risk**: When many funds hold similar positions, forced unwinding by one fund can cascade, as occurred during the August 2007 quant crisis.
- **Factor exposure**: A portfolio that is market-neutral but heavily exposed to a single factor (e.g., momentum) can suffer large drawdowns when that factor reverses.
- **Leverage amplifies losses**: The leverage used to make alpha meaningful also amplifies any mispricing in the model.

## Trading Applications

- **[[statistical-arbitrage|Statistical arbitrage]]**: High-frequency or medium-frequency quantitative strategies that trade hundreds or thousands of stocks simultaneously, maintaining strict market neutrality while exploiting short-term pricing inefficiencies.
- **[[pairs-trading]]**: The simplest form of market-neutral strategy -- going long one stock and short a correlated peer. The pair's spread is the source of P&L, not the market direction.
- **[[long-short-equity]]**: While not always market neutral (many L/S equity funds run with a net long bias), the purest form targets zero beta exposure.
- **Convertible arbitrage**: Buying convertible bonds and shorting the underlying stock to isolate the embedded option value. This was [[ed-thorp]]'s original hedge fund strategy.
- **Merger arbitrage**: Going long the target and short the acquirer in announced deals, profiting from the deal spread while being approximately market neutral.

## Related

- [[long-short-equity]]
- [[pairs-trading]]
- [[statistical-arbitrage]]
- [[ed-thorp]]
- [[delta-neutral]]
- [[hedging]]
- [[beta]]
- [[risk-management]]

## Sources

- [[book-inside-the-black-box]] -- Narang explains how quantitative funds construct and maintain market-neutral portfolios using multi-factor risk models
- [[book-a-man-for-all-markets]] -- Thorp's memoir details his pioneering market-neutral strategies, from convertible arbitrage to statistical arbitrage, and the mathematical framework underlying portfolio neutralization
