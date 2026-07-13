---
title: "Interactive Brokers Forecast Trader"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, prediction-markets, macro, recession, tail-risk, derivatives]
aliases: ["Forecast Trader", "IBKR Forecast Trader", "IBKR Prediction Markets"]
source_type: data
source_url: "https://www.interactivebrokers.com/campus/traders-insight/forecast-trader/"
confidence: high
related: ["[[interactive-brokers]]", "[[prediction-markets]]", "[[recession]]", "[[tail-risk]]", "[[macro-data-sources]]", "[[data-sources-overview]]", "[[ai-layoff-trap]]", "[[capital-vs-labor-asymmetry]]", "[[2026-03-bls-900k-jobs-revision]]"]
---

# Interactive Brokers Forecast Trader

**Forecast Trader** is [[interactive-brokers|Interactive Brokers]]' regulated prediction-market product offering futures-style contracts on macroeconomic indicators, scheduled economic releases, and other yes/no event outcomes. It functions as an institutional-grade [[prediction-markets|prediction market]] embedded directly inside the IBKR trading platform — useful both as a sentiment data source and as a hedging instrument for event-driven and recession-specific risk. (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])

## What It Tracks

Forecast Trader contracts cover macro and labor-market indicators that are difficult or expensive to hedge through equity or volatility instruments alone. Categories include:

- **US recession probability** — currently pricing **41% probability of a US technical recession by end of 2026** (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])
- **Unemployment rate thresholds** — yes/no contracts on whether the headline U-3 rate exceeds defined levels by a given date
- **Nonfarm payroll prints** — over/under contracts tied to scheduled BLS releases (see [[bls-benchmark-revisions]])
- **Inflation prints** — CPI / PPI surprise contracts
- **Interest-rate decisions** — outcome contracts on FOMC actions
- Other scheduled macro events and political outcomes

Each contract resolves to $1 (yes) or $0 (no), and the traded price between 0 and 1 is interpretable as the market-implied probability of the event.

## Why It Matters for AI-Recession Analysis

For traders monitoring an [[ai-layoff-trap|AI-driven recession]] scenario, Forecast Trader provides three things equity and volatility markets do not:

1. **Direct probability quotes for recession and unemployment** — no need to back out implied probabilities from credit spreads, yield curves, or VIX. The 41% end-2026 recession contract is a single number traders can chart, hedge against, and use as a reference. (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])
2. **A cheaper hedge than VIX or equity puts for recession-specific scenarios** — VIX hedges any volatility (geopolitical shocks, earnings, AI bubble pops), so its cost reflects all risks. A direct recession contract isolates the labor / GDP cascade IBKR's article frames as "a cheaper way to hedge recession job losses."
3. **A clean signal for the [[capital-vs-labor-asymmetry|capital-vs-labor lag]]** — equity markets can rally on AI capex while Forecast Trader recession probabilities climb on labor data. Divergence between the two is itself a tradable signal.

## Access

| Detail | Value |
|--------|-------|
| **Provider** | Interactive Brokers (regulated US broker-dealer) |
| **URL** | [interactivebrokers.com/campus/traders-insight/forecast-trader/](https://www.interactivebrokers.com/campus/traders-insight/forecast-trader/) |
| **Account requirement** | IBKR margin or cash account |
| **Contract style** | Binary, $1 max payout, exchange-listed event contracts |
| **Cost** | Per-contract commission; no paid data subscription required |

Quotes are visible inside the IBKR trading platform; some prices and commentary are also published on the public Traders' Insight blog.

## Gotchas / Caveats

- **Liquidity varies by contract.** Headline contracts (recession, unemployment) trade reasonably; long-dated and exotic contracts can be thin and bid-ask spreads wide.
- **Implied probabilities are not pure probabilities.** They embed a small risk premium and capital-cost. Treat them as a useful market-aggregated estimate, not a forecast model.
- **US-regulated event contract universe is restricted.** Available contracts are subject to CFTC oversight; not every macroeconomic question is offered.
- **Resolution depends on official data.** A contract on "unemployment rate > 5% by Dec 2026" resolves on the BLS release. If the [[bls-benchmark-revisions|BLS revises history]] later, the contract has already settled — the revision does not retroactively re-price.
- **Time decay.** As with any binary, theta accelerates near expiry. Traders using Forecast Trader as a hedge should ladder expiries to avoid being forced to roll at unfavorable prices.

## Use Cases

- **Recession-specific tail hedge.** Smaller capital outlay than buying SPX puts or VIX calls for an investor whose primary worry is a labor-driven downturn rather than generalized volatility.
- **Sanity-check on macro forecasters.** Compare Forecast Trader's implied probability against bank research (e.g., Goldman Sachs' 11M-jobs displacement forecast, Morgan Stanley labor research) to spot consensus vs. market disagreement.
- **Pair trade with VIX.** When recession contracts move but VIX is flat (or vice versa), the divergence often anticipates a regime shift in which risk the market is pricing.
- **Calibrating [[ai-layoff-trap]] scenario sizing.** If Citrini-style scenarios are public ([[citrini-research]]) but Forecast Trader recession probability is not moving, that is information about how seriously the market takes the scenario.

## Related

- [[interactive-brokers]]
- [[prediction-markets]]
- [[recession]]
- [[tail-risk]]
- [[bls-benchmark-revisions]]
- [[macro-data-sources]]
- [[data-sources-overview]]
- [[capital-vs-labor-asymmetry]]
- [[ai-layoff-trap]]
- [[citrini-research]]

## Sources

- (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])
- IBKR Traders' Insight: "A Cheaper Way to Hedge Recession Job Losses" — [interactivebrokers.com/campus/traders-insight/forecast-trader/a-cheaper-way-to-hedge-recession-job-losses/](https://www.interactivebrokers.com/campus/traders-insight/forecast-trader/a-cheaper-way-to-hedge-recession-job-losses/)
