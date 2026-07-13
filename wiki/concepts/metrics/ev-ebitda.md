---
title: "EV/EBITDA"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, metrics]
aliases: ["EV/EBITDA", "ev-ebitda", "enterprise value to EBITDA", "EV multiple"]
domain: [fundamental-analysis]
prerequisites: ["[[enterprise-value]]", "[[ebitda]]"]
difficulty: intermediate
related: ["[[ebitda]]", "[[price-to-earnings-ratio]]", "[[enterprise-value]]", "[[free-cash-flow]]", "[[peer-comparison]]"]
---

**EV/EBITDA** is the ratio of a company's [[enterprise-value|enterprise value]] to its [[ebitda|EBITDA]]. It is the dominant valuation multiple in private equity, M&A, and cross-border equity research because it is neutral to capital structure, tax jurisdiction, and accounting policy in a way that [[price-to-earnings-ratio|P/E]] is not.

## Formula

```
EV/EBITDA = Enterprise Value / EBITDA

where:
Enterprise Value = Market Cap + Total Debt − Cash & Equivalents
                 (+ Preferred Equity + Minority Interest, if present)
```

Enterprise value represents the theoretical takeout price of the entire business — what an acquirer would pay to own the operations free and clear of the existing capital stack.

## Why It Beats P/E for Comparison

P/E mixes operating results with financing choices. A company that issues debt to buy back stock will mechanically raise its EPS and lower its P/E without any improvement in the underlying business. EV/EBITDA sees through this: the buyback raises debt (and thus EV) by the same amount cash falls, and EBITDA is unchanged. The multiple stays flat, correctly reflecting that nothing real happened.

EV/EBITDA is also **currency-neutral** (both numerator and denominator scale identically) and **tax-policy-neutral** (EBITDA is pre-tax), making it the standard for comparing, say, a German chemicals firm against a U.S. one.

## Typical Ranges by Sector

| Sector | Typical EV/EBITDA |
|---|---|
| Utilities | 8-12x |
| Mature industrials | 6-10x |
| Consumer staples | 10-14x |
| Software / SaaS | 15-30x |
| Biotech (with revenue) | 20-50x |
| Cyclical commodities | 4-8x at peak |

The long-run S&P 500 median sits near 11-12x. Readings above 15x for the broad market historically indicate expensive conditions.

## Where It Fails

EV/EBITDA **overstates value for capital-intensive businesses** — an airline at 6x EV/EBITDA may look cheap until you subtract the multi-billion annual capex required just to keep planes flying. For such firms, EV/(EBITDA − Capex) or an EV/[[free-cash-flow]] multiple is more honest.

It is also **unusable for banks, insurers, and other financials**, where interest is a revenue line rather than a financing cost and EBITDA is not a meaningful concept. Use P/B or P/E for those instead.

In private equity, EV/EBITDA drives the LBO model: sponsors typically "buy at 8x, sell at 10x" and use leverage turns to amplify equity returns.

## Trading Relevance

EV/EBITDA is a core ranking factor in systematic value strategies and in [[peer-comparison|peer-comparison]] screens: comparing a stock's multiple against its sector median flags relative cheapness or richness in a capital-structure-neutral way. Multiple expansion or compression (the change in the multiple, separate from EBITDA growth) is a key driver of equity returns that quants decompose explicitly. In merger arbitrage and event-driven trading, the EV/EBITDA at which comparable deals have printed sets the expected takeout multiple for a target. Because the metric breaks for financials and overstates value for high-capex businesses, traders pair it with EV/FCF or P/B where appropriate.

## Related

- [[ebitda]], [[enterprise-value]]
- [[price-to-earnings-ratio]] — the retail-investor counterpart
- [[free-cash-flow]], [[peer-comparison]]

## Sources

- Damodaran, A., *Investment Valuation* and "Enterprise Value Multiples" data — sector EV/EBITDA norms and pitfalls
- Rosenbaum, J. & Pearl, J., *Investment Banking: Valuation, LBOs, and Mergers & Acquisitions* — EV/EBITDA in comparable-company and LBO analysis
- CFA Institute curriculum, *Equity Investments* — enterprise-value multiples
