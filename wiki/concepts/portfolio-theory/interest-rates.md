---
title: Interest Rates
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [interest-rates, macro, valuation, volatility]
aliases: [rates, interest-rate, "Interest Rates"]
domain: [portfolio-theory, market-microstructure]
prerequisites: ["[[macroeconomics]]", "[[bond-market]]"]
difficulty: intermediate
related:
  - "[[macroeconomics]]"
  - "[[monetary-policy]]"
  - "[[fed-policy]]"
  - "[[yield-curve]]"
  - "[[inflation]]"
  - "[[bond-market]]"
  - "[[interest-rate-swaps]]"
  - "[[fundamental-analysis]]"
  - "[[volatility]]"
  - "[[diversification]]"
  - "[[futures]]"
---

# Interest Rates

Interest rates represent the cost of borrowing money, set by central banks (policy rates) and determined by bond markets (market rates), with far-reaching effects on all financial assets.

## Overview

Interest rates are the single most important macroeconomic variable for financial markets. They influence everything from stock valuations and bond prices to mortgage rates and currency values. Central banks -- particularly the U.S. Federal Reserve -- use interest rates as their primary tool to manage inflation and economic growth.

## Key Details

### Policy Rates

- **Federal funds rate**: The rate at which U.S. banks lend reserves to each other overnight. The Fed sets a target range and uses open market operations to maintain it.
- **Rate hikes**: The central bank raises rates to cool inflation and slow economic growth. Generally bearish for equities and bullish for the domestic currency.
- **Rate cuts**: The central bank lowers rates to stimulate borrowing and economic activity. Generally bullish for equities and bearish for the domestic currency.

### Market Rates

- **Bond yields**: Market-determined interest rates. The 10-year Treasury yield is the most watched benchmark globally.
- **Yield curve**: Plots bond yields across maturities. A normal curve slopes upward (long > short). An inverted curve (short > long) has historically preceded recessions.
- **Real rates**: Nominal rate minus inflation. Real rates are the "true" cost of borrowing and a key driver of asset allocation decisions. By the Fisher relation, `nominal_rate ≈ real_rate + expected_inflation`; the market-implied real rate is read directly off TIPS (Treasury Inflation-Protected Securities), and the gap between nominal and TIPS yields is the **breakeven inflation** rate.

### Why Rates Drive Valuations

The mechanical link from rates to asset prices runs through the discount rate. A simplified equity present value:

```
price = Σ  CF_t / (1 + r)^t       where r = risk_free_rate + equity_risk_premium
```

Because long-duration cash flows (growth stocks, with earnings far in the future) are discounted by more periods of `r`, they are far more sensitive to a change in rates than near-cash-flow value stocks — the same duration logic that makes a 30-year bond move more than a 2-year bond for a given yield change. This is why a 100bp rise in the [[yield-curve|10-year yield]] compresses growth-stock multiples sharply while leaving deep-value names relatively unscathed.

### The Taylor Rule

Central-bank policy rates are loosely benchmarked against the **Taylor rule**, a reaction function:

```
target_rate = neutral_rate + inflation + 0.5*(inflation - target) + 0.5*(output_gap)
```

Traders use Taylor-rule estimates to judge whether policy is "behind the curve" (too loose given inflation) or restrictive, which informs the expected path of [[fed-policy|Fed]] hikes/cuts.

### Impact on Markets

- **Equities**: Higher rates reduce the present value of future earnings (lower valuations, especially growth stocks). Lower rates do the opposite.
- **Bonds**: Bond prices move inversely to yields. When rates rise, existing bond prices fall.
- **Crypto**: Crypto has shown increasing sensitivity to rate expectations. Tightening cycles tend to reduce speculative appetite; easing cycles fuel it.
- **Currencies**: Higher rates attract foreign capital, strengthening the currency.

## Trading Relevance

Interest rate decisions and forward guidance from central banks are among the highest-impact events on the economic calendar. Traders monitor Fed meeting dates, dot plots, inflation data (CPI, PCE), and employment reports to anticipate rate moves. Bond [[futures]] and Fed Funds futures allow direct speculation on rate expectations, while [[interest-rate-swaps]] let institutions add or strip rate exposure with minimal capital. Understanding the rate environment is essential context for any trading strategy.

## Sources

- Federal Reserve — FOMC statements, the Summary of Economic Projections ("dot plot"), and the federal funds target range.
- US Treasury / FRED — constant-maturity Treasury yields, TIPS yields, and breakeven inflation series.
- Taylor, J.B. (1993). *"Discretion versus Policy Rules in Practice."* Carnegie-Rochester Conference Series — the original Taylor rule.
- CME FedWatch Tool — market-implied probabilities of rate moves from fed funds futures.

## Related

- [[macroeconomics]] — interest rates are the most important macro variable
- [[monetary-policy]] — how central banks set and manage rates
- [[fed-policy]] — Federal Reserve rate decisions specifically
- [[central-bank]] — the institutions that control policy rates
- [[inflation]] — rates are the primary tool against inflation
- [[bond-market]] — bond prices move inversely to yields
- [[yield-curve]] — the term structure of interest rates
- [[credit-cycle]] — rates drive the expansion and contraction of credit
- [[currency-dynamics]] — rate differentials drive exchange rates
- [[sovereign-debt]] — government borrowing costs tied directly to rates
- [[financial-conditions]] — rates as a component of financial conditions
- [[fundamental-analysis]] — rates are a core macro input
- [[volatility]] — rate decisions drive volatility spikes
- [[futures]] — bond and rate futures enable rate trading
- [[diversification]] — bonds diversify equity risk via rate dynamics
