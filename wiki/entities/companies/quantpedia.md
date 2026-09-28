---
title: "Quantpedia"
type: entity
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [company, quantitative, strategy-development, anomalies, backtesting, education]
aliases: ["QuantPedia", "Quantpedia Premium", "Quantpedia Pro"]
entity_type: company
headquarters: "Bratislava, Slovakia"
website: "https://quantpedia.com"
related: ["[[quantpedia-strategy-encyclopedia]]", "[[external-strategy-sources]]", "[[alpha-decay]]", "[[data-snooping-and-p-hacking]]", "[[crypto-idea-generation]]", "[[research-checklist]]", "[[hypothesis-to-backtest-workflow]]", "[[anomalies-overview]]"]
---

**Quantpedia** is an online encyclopedia of systematic trading strategies distilled from academic finance papers. Each entry ("strategy card") restates a published anomaly in plain language with trading rules, a backtest summary and the source paper, making it one of the fastest ways to survey what the academic literature claims works (Source: [[quantpedia-strategy-encyclopedia]]).

## Overview

Quantpedia is run by a small quant research team led by Radovan Vojtko; its analysts also publish their own working papers (e.g. on Bitcoin seasonality, crypto rebalancing, commodity skewness), which then appear as cards in the database. Around 10-15 new strategies are added per month (Source: [[quantpedia-strategy-encyclopedia]]).

### Free vs paid

| Tier | What you get (as of 2026-09-28) |
|---|---|
| **Free** (sign-up) | ~65-70 strategy cards with full rules, headline stats, links to papers; blog articles |
| **Prime** | 100+ strategies, 7 reports, limited portfolio modelling |
| **Premium** | 900+ strategies, 1,000+ linked papers |
| **Pro** | Premium + ~800 out-of-sample backtests with Python code, API, portfolio modelling across 200+ ETFs and ~40 cryptocurrencies, ~40 reports |

Third-party reviews quote Premium at roughly $449 / 3 months, $599 / year, $1,199 / 3 years; treat as indicative (Source: [[quantpedia-strategy-encyclopedia]]).

### How a strategy card is structured

1. **Header stats** — rebalancing frequency, markets, backtest period, annual return, volatility, Sharpe, max drawdown, complexity
2. **Description** — the anomaly in plain English
3. **Fundamental reason** — the proposed economic/behavioural mechanism
4. **Simple trading strategy** — universe, signal, long/short legs, weighting, rebalance
5. **Source paper** — authors, title, abstract; plus "other papers" confirming or extending the effect
6. (Pro) out-of-sample backtest and code

## Biases to correct for

- **Pre-cost, in-sample headline numbers.** Card statistics are the paper's; they rarely include commissions, spreads, borrow or funding. High-turnover cards (weekly or daily rebalance) degrade most. Always apply a [[transaction-costs]] overlay before comparing.
- **Publication decay.** McLean and Pontiff (2016) find the average published anomaly loses ~58% of its return after publication (see [[alpha-decay]]). Many Quantpedia backtests end in 2000-2010; several cards themselves note deteriorating out-of-sample alpha (currency momentum, PPP value, WTI/Brent).
- **Selection / data-snooping.** An encyclopedia of *successful* published results is a survivor sample of a much larger set of tested ideas — see [[data-snooping-and-p-hacking]] and [[deflated-sharpe-ratio]].
- **Equity-heavy.** Of the ~80 free cards on 2026-09-28 roughly 85% are equity anomalies (out of scope here); only two were crypto-specific.
- **In-house authorship.** Some cards summarise Quantpedia's own working papers, which are not peer-reviewed; card data can contain inconsistencies (e.g. the crypto rebalancing card lists a −99.99% max drawdown next to 2.6% volatility).

## Using Quantpedia as a crypto idea source

1. **Harvest the mechanism, not the number.** Read "fundamental reason" and ask whether the same counterparty exists in crypto (see [[edge-taxonomy]]).
2. **Translate the universe.** Futures/FX cross-sectional ideas map to perp universes (e.g. commodity term structure → [[funding-rate]] carry; futures volume/OI reversal → perp OI data).
3. **Re-test on crypto data from scratch** via the [[hypothesis-to-backtest-workflow]] — never import the equity/futures Sharpe.
4. **Haircut** expected Sharpe by at least half for publication decay and apply realistic taker fees and funding.
5. Record the idea's origin in [[external-strategy-sources]].

### Pages harvested from Quantpedia

- Crypto: [[bitcoin-overnight-seasonality]], [[crypto-rebalancing-premium]], [[bitcoin-max-min-breakout]]
- Futures → crypto adaptation: [[volume-oi-conditioned-reversal]]
- Commodities: [[commodity-skewness-strategy]]
- FX: [[currency-value-ppp]], [[dollar-carry-trade]]
- Notes added to: [[carry-trade]], [[currency-momentum]], [[commodity-carry-strategy]], [[commodity-momentum]], [[time-series-momentum]], [[geographic-spread-trading]], [[rebalancing]]

## Related

- [[external-strategy-sources]] · [[crypto-idea-generation]] · [[anomalies-overview]] · [[alpha-decay]] · [[research-checklist]]

## Sources

- (Source: [[quantpedia-strategy-encyclopedia]])
