---
title: "Cboe S&P 500 PutWrite Index (PUT)"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, indicators, benchmarks, options-premium-selling, sp500]
aliases: ["PUT", "Cboe PutWrite Index", "S&P 500 PutWrite Index", "PUT Index", "put-index", "CBOE PutWrite Index"]
related: ["[[cash-secured-puts]]", "[[cboe-bxm-buywrite-index]]", "[[options-premium-selling]]", "[[volatility-risk-premium]]", "[[wheel-strategy]]", "[[sp500]]"]
domain: [options, portfolio-theory]
prerequisites: ["[[put-option]]", "[[options-premium-selling]]"]
difficulty: intermediate
---

The **Cboe S&P 500 PutWrite Index (PUT)** is a total-return benchmark that measures the performance of a passive cash-secured put-writing strategy on the [[sp500|S&P 500 Index]]. The index holds Treasury bills as collateral and sells fully-collateralized at-the-money [[sp500|SPX]] [[put-option|put options]] each month. Launched in June 2007 with backfill to June 1986, PUT is the standard benchmark for [[cash-secured-puts|cash-secured put]] and [[wheel-strategy|wheel-style]] [[options-premium-selling]] strategies.

## Overview

PUT was designed by the Cboe to provide an option-based equivalent to the [[cboe-bxm-buywrite-index|BXM BuyWrite Index]]. Where BXM uses a long-stock + short-call construction, PUT uses a cash + short-put construction -- two payoff profiles that, by put-call parity, are theoretically equivalent before friction.

PUT has frequently outperformed BXM in live trading, despite their theoretical equivalence -- a long-running empirical puzzle in the academic options literature.

## Methodology

The PUT index follows mechanical monthly rules:

- **Collateral**: Treasury bills sufficient to fully collateralize the short put position at the strike (i.e., no leverage)
- **Put written**: one SPX put option, at-the-money, with one-month tenor
- **When written**: at the close (PUT uses the close, while BXM uses the open) on the third Friday of each month
- **Strike selection**: the listed strike just below the prevailing S&P 500 level
- **Premium received**: added to the T-bill collateral pool
- **Held to expiration**: no active management mid-month
- **At expiration**: cash settlement; if the put finishes in-the-money, the loss is paid out of collateral

Because the strategy is fully collateralized, it is not leveraged -- maximum loss equals the strike minus zero, less premium received.

## Historical Performance

Across the long backfilled history (1986-present):

- **Total return comparable to S&P 500** over multi-decade windows
- **Lower realized volatility** than SPX (typically 10-30% lower depending on regime)
- **Lower maximum drawdown** than SPX in most major drawdown periods, though PUT still lost meaningful capital in 2008 and 2020
- **Higher risk-adjusted return** ([[sharpe-ratio|Sharpe]] and Sortino) than both SPX and BXM in many studies
- **Lagging in sharp bull markets** -- like BXM, the short option leg caps upside

PUT is widely cited as one of the more attractive long-run [[volatility-risk-premium]] harvesting benchmarks because it combines premium income with T-bill yield.

## Synthetic Equivalence to BXM

By [[put-call-parity]]:

> short ATM put + cash collateral = long underlying + short ATM call (for the same strike and tenor)

In theory, PUT and BXM should produce identical payoffs each month. In practice, PUT has often outperformed BXM by 50-150 basis points per year. Hypotheses for the empirical divergence:

- **Execution timing** -- BXM rolls at the open, PUT at the close. The "Monday-morning effect" and overnight gap risk affect the two indices differently
- **Strike selection rounding** -- BXM's slightly OTM call vs. PUT's slightly OTM put differ in delta and premium relative to a true ATM
- **Dividend treatment** -- BXM holds the underlying and receives dividends, PUT holds T-bills and earns the risk-free rate; in regimes where T-bills > dividend yield, PUT benefits
- **Liquidity asymmetries** -- SPX puts and calls have different bid-ask dynamics, particularly for OTM strikes
- **Skew premium** -- because [[volatility-skew|implied volatility skew]] makes ATM puts richer than ATM calls (the [[cboe-skew-index|SKEW]] effect), the put writer collects a fatter premium per unit of risk

The empirical gap is robust enough that practitioners often prefer PUT over BXM as the cleaner expression of premium selling.

## Live Tracking Funds

ETF and mutual-fund products that track PUT or PUT-like strategies:

- **PUTW** (WisdomTree CBOE S&P 500 PutWrite Strategy Fund) -- the most direct retail proxy, designed to track PUT; modest AUM
- **HSPX** (Global X S&P 500 Covered Call & Growth ETF) -- mixed buy-write/put-write methodology
- **WTPI** (institutional and white-label products) -- various separate accounts run by AQR, JPMorgan, Parametric, and others apply put-write mandates against SPX or single names

Compared to the buy-write fund landscape, the put-write space is smaller but growing, partly because tax treatment of cash-secured-put income can be more efficient than equity dividends + call writing.

## ITPM Use

In an ITPM-style portfolio, PUT functions as:

- **An income overlay benchmark** -- any active put-selling program should be compared to PUT to determine whether the manager adds value
- **An uncorrelated yield source** -- PUT's return profile differs from credit, dividend equity, and rates yield, and so it can diversify a multi-source income book
- **A regime sensor** -- PUT outperforms SPX in flat, choppy, and modestly down years; underperforms in strong bulls. A rolling PUT-vs-SPX spread is a usable regime indicator
- **A pairing component** -- combined with [[cboe-bxm-buywrite-index|BXM]], a 50/50 blend provides diversification across buy-write and put-write execution paths
- **A capacity reference** -- PUT's mechanical rules approximate what a real fund can execute, unlike many backtests that assume frictionless fills
- **A wheel-strategy benchmark** -- the [[wheel-strategy]] is essentially a discretionary version of PUT; PUT provides a passive comparator

## Critique

- **Caps upside** -- like all premium-selling strategies, PUT gives up convexity to the right tail
- **Tail risk** -- PUT is fully exposed to large drawdowns; the premium received is small comfort during a 2008 or 2020 event
- **Negative skew** -- payoff distribution has fatter left tail than right; not a natural fit for risk-averse mandates without overlay protection
- **Sensitive to T-bill yields** -- in zero-rate environments, the collateral leg contributes little; the strategy economics worsen when short rates compress
- **Concentration risk** -- only one expiration per month creates path-dependence; weekly or laddered execution typically reduces variance vs. PUT itself
- **Regime fragility** -- PUT can suffer cluster losses in short, sharp drawdowns where realized vol exceeds the previously priced [[implied-volatility]]

## Related

- [[cash-secured-puts]] -- the trade structure PUT mechanizes
- [[cboe-bxm-buywrite-index]] -- the synthetic-equivalent buy-write benchmark
- [[options-premium-selling]] -- the broader strategy family
- [[volatility-risk-premium]] -- the persistent premium PUT harvests
- [[wheel-strategy]] -- a discretionary single-name version of put-writing
- [[sp500]]
- [[put-option]]
- [[put-call-parity]]
- [[implied-volatility]]

## Sources

- Cboe PUT Index methodology and historical data (Chicago Board Options Exchange)
- Ungar, J. and Moran, M., "The Cash-secured PutWrite Strategy and Performance of Related Benchmark Indexes," *Journal of Alternative Investments* (2009)
- Israelov, R. and Klein, M., "Risk and Return of Equity Index Collar Strategies," *Journal of Alternative Investments* (2016)
