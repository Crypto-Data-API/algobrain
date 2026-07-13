---
title: "Cboe S&P 500 BuyWrite Index (BXM)"
type: concept
created: 2026-05-06
updated: 2026-06-11
status: good
tags: [options, indicators, benchmarks, options-premium-selling, sp500]
aliases: ["BXM", "Cboe BuyWrite Index", "S&P 500 BuyWrite Index", "BXM Index", "bxm-index", "CBOE Buy-Write Index", "BXY", "BXY Index"]
related: ["[[covered-call]]", "[[options-premium-selling]]", "[[options-equity-overlay]]", "[[cboe-put-putwrite-index]]", "[[volatility-risk-premium]]", "[[sp500]]"]
domain: [options, portfolio-theory]
difficulty: intermediate
---

The **Cboe S&P 500 BuyWrite Index (BXM)** is a total-return benchmark that measures the performance of a passive [[covered-call|buy-write]] strategy on the [[sp500|S&P 500 Index]]. The index holds the S&P 500 portfolio and writes a one-month, at-the-money [[sp500|SPX]] [[call-option|call option]] each month, held to expiration. Launched in April 2002, BXM is the primary academic and industry benchmark for evaluating [[options-premium-selling|covered-call strategies]].

## Overview

BXM was developed by the Cboe in collaboration with Standard & Poor's and quickly became the reference benchmark for buy-write performance. Its mechanical, transparent rules make it useful for:

- Evaluating actively managed covered-call funds
- Studying the [[volatility-risk-premium]] in equity index options
- Backfilled history extends to June 1988, providing 35+ years of out-of-sample data

A close cousin, the BXY index (Cboe S&P 500 2% OTM BuyWrite Index), uses 2%-out-of-the-money calls instead of at-the-money to give up some premium income in exchange for capped upside participation.

## Methodology

The BXM is constructed each month according to fixed rules:

- **Underlying portfolio**: long the S&P 500 Index (total-return basis)
- **Call written**: one SPX call option, at-the-money, with one-month tenor
- **When written**: at the open on the third Friday of each month (the morning of the prior month's expiration)
- **Strike selection**: the listed strike just above the prevailing S&P 500 level (i.e., slightly out-of-the-money in practice)
- **Premium received**: reinvested into the S&P 500 portfolio
- **Held to expiration**: no intra-month management
- **At expiration**: if the call finishes in-the-money, settlement is paid out of the portfolio; a new call is written for the next cycle

This is a fully systematic, fully covered, no-leverage strategy.

## Historical Performance vs SPX

Across the long backfilled history, BXM has exhibited:

- **Comparable long-run total return** to the S&P 500 (over multi-decade windows the gap has been small)
- **Roughly 30% lower realized volatility** -- the short-call leg trims the upper tail of returns
- **Higher [[sharpe-ratio]] in many sub-periods** due to the volatility reduction
- **Underperformance in strong bull runs** -- when SPX rallies sharply, the short calls cap upside
- **Outperformance in flat and modestly down markets** -- premium income carries the index when the underlying drifts sideways
- **Limited downside protection** -- the call premium offsets only a small fraction of large drawdowns; BXM still lost substantial value in 2008 and 2020

A frequently cited finding is that on a *per-unit-of-volatility* basis, BXM matched or exceeded SPX over long horizons -- the source of the common claim that covered-call writing harvests the [[volatility-risk-premium]] embedded in SPX index options.

## Why It Matters

BXM is the standard benchmark for:

- **Covered-call mutual funds and ETFs** -- regulators and investors compare active strategies against BXM
- **Options overlay programs** -- pension and endowment overlay mandates often reference BXM
- **Academic research** -- the Whaley (2002), Feldman-Roy, and Ibbotson papers on buy-write strategies use BXM as the empirical workhorse
- **VRP studies** -- BXM's realized return minus SPX return approximates a long-VRP harvesting payoff

Without a transparent benchmark, evaluating whether an active covered-call strategy adds value would be impossible.

## Live Funds That Track Variants

A number of ETFs and mutual funds run buy-write strategies in the spirit of BXM, though most use modified rules (different strikes, weekly rather than monthly cycles, single-name calls instead of index, or active strike selection):

- **JEPI** (JPMorgan Equity Premium Income ETF) -- equity-linked-note based, uses S&P 500 underlying with active call overlay; very large AUM
- **JEPQ** (JPMorgan Nasdaq Equity Premium Income ETF) -- Nasdaq-100 version of JEPI
- **QYLD** (Global X Nasdaq 100 Covered Call ETF) -- writes ATM monthly Nasdaq-100 calls; the most BXM-faithful methodology applied to Nasdaq
- **XYLD** (Global X S&P 500 Covered Call ETF) -- the closest direct retail proxy for BXM itself
- **DIVO** (Amplify CWP Enhanced Dividend Income ETF) -- single-name covered calls layered on a dividend portfolio

These funds differ in expense ratios, strike selection logic, distribution policy, and tax treatment, but all share the core buy-write economic profile.

## Critique

- **Caps upside in bull markets** -- in years like 2013 (+32% SPX), 2019 (+31%), and 2021 (+28%), BXM materially underperformed SPX
- **Negative skew amplification** -- the short call truncates the right tail without reducing left-tail exposure, producing a payoff with worse skew than SPX
- **Tax inefficiency for taxable accounts** -- monthly call writing realizes short-term gains/losses
- **Path dependence on monthly roll** -- using third-Friday opens means the strategy can be unlucky if a sharp move occurs around a roll date
- **Modern academic critiques** (Israelov, Nielsen and others at AQR) argue that naive covered-call writing is dominated by a delta-managed short-vol strategy, and that BXM's outperformance per unit of volatility is largely an artifact of beta-reduction rather than genuine alpha

## ITPM Use

In an ITPM-style portfolio, BXM serves as:

- **A baseline benchmark** for any premium-selling overlay -- if an active strategy does not beat BXM net of costs, the manager is not adding value over a mechanical rule
- **A regime gauge** -- BXM's rolling outperformance vs. SPX flips in predictable regimes (sideways/flat markets favor BXM; trending bull markets penalize it)
- **An execution reference** -- BXM's rules approximate what a small fund can actually replicate, unlike many academic backtests that ignore execution constraints
- **A pairing target** -- BXM combined with [[cboe-put-putwrite-index|PUT]] (PutWrite) produces a more diversified premium-selling exposure than either alone

## Related

- [[covered-call]] -- the underlying strategy BXM mechanizes
- [[options-premium-selling]] -- the broader strategy family
- [[options-equity-overlay]] -- using options to modify an existing equity exposure
- [[cboe-put-putwrite-index]] -- the synthetic-equivalent put-write benchmark (PUT)
- [[volatility-risk-premium]] -- the persistent premium that BXM partially harvests
- [[sp500]]
- [[call-option]]
- [[implied-volatility]]

## Sources

- Cboe BXM Index methodology and historical data (Chicago Board Options Exchange)
- Whaley, R., "Return and Risk of CBOE BuyWrite Monthly Index," *Journal of Derivatives* (2002)
- Feldman, B. and Roy, D., "Passive Options-Based Investment Strategies: The Case of the CBOE S&P 500 BuyWrite Index," *Journal of Investing* (2005)
- Israelov, R. and Nielsen, L., "Covered Calls Uncovered," *Financial Analysts Journal* (2014)
