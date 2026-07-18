---
title: Float
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, liquidity]
aliases: [public float, free float, floating shares, float-adjusted]
domain: [market-microstructure]
prerequisites: ["[[liquidity]]"]
difficulty: beginner
related:
  - "[[short-interest]]"
  - "[[short-squeeze]]"
  - "[[gamma-squeeze]]"
  - "[[liquidity-risk]]"
  - "[[trading-volume]]"
  - "[[liquidity]]"
  - "[[market-capitalization]]"
---

# Float

The float is the number of a company's shares that are available for public trading, calculated by subtracting restricted shares (insider holdings, locked-up shares, and closely held blocks) from the total shares outstanding.

## Float vs. Shares Outstanding

- **Shares Outstanding** - Total number of shares that exist, including restricted shares
- **Float** - The subset of shares outstanding that are freely tradeable on the open market

For example, a company with 100 million shares outstanding where insiders hold 40 million has a float of 60 million shares.

The restricted bucket that is subtracted typically includes: founder, officer, and director holdings; large strategic or controlling blocks (often defined as holders of >5%); shares still under lock-up after an IPO; and ESOP/treasury shares. As lock-ups expire or insiders sell, the float *grows* — an event that can pressure price by increasing tradeable supply. Conversely, buybacks and new insider accumulation *shrink* the float.

## Why Float Matters

- **Volatility** - Low-float stocks are more volatile because fewer available shares mean each trade has a larger price impact
- **Squeeze potential** - A low float combined with high [[short-interest]] creates the conditions for a [[short-squeeze]] or [[gamma-squeeze]]
- **Liquidity** - Lower float generally means less [[trading-volume]] and wider bid-ask spreads
- **Index eligibility** - Many indices require a minimum float for inclusion (float-adjusted weighting)

## Float Categories (Informal)

- **Micro float** - Under 10 million shares (highly volatile, prone to manipulation)
- **Low float** - 10-50 million shares (popular with day traders for volatility)
- **Standard float** - 50 million+ shares (typical institutional-grade stock)

## Trading Relevance

Day traders and momentum traders specifically screen for low-float stocks because they offer larger percentage moves. However, low float also means higher [[liquidity-risk]] -- getting out of a position can be difficult when the trade goes wrong. Always size positions appropriately relative to the stock's average daily volume and float.

The key derived metric is **days-to-cover** (short interest divided by average daily volume) and **short interest as a percentage of float**: when a large fraction of a small float is sold short, even modest buying pressure can force shorts to cover into a thin supply, producing the violent rallies characteristic of a [[short-squeeze]]. The 2021 GameStop episode is the canonical example — short interest exceeded 100% of the free float, meaning more shares were borrowed and shorted than were freely available to buy back.

Float also drives **index weighting**: major indices (S&P 500, MSCI, FTSE) use **float-adjusted market capitalization** rather than total market cap, so only freely tradeable shares count toward a constituent's weight. This means a company with large insider or government holdings is underweighted relative to its headline market cap, and changes to estimated float can trigger mechanical rebalancing flows from index funds.

## Sources

- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* — supply, liquidity, and price impact ([[book-trading-and-exchanges]])
- S&P Dow Jones Indices — *Float Adjustment Methodology* (Investable Weight Factor) (spglobal.com)
- MSCI — Global Investable Market Indexes Methodology (float-adjustment rules)
- SEC — definitions of "public float" and restricted securities (Rule 144), used in filing requirements
- General equity market-microstructure literature on low-float volatility and squeeze dynamics
