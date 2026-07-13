---
title: "Asset Management: A Systematic Approach to Factor Investing — Andrew Ang (2014)"
type: source
created: 2026-04-15
updated: 2026-04-28
status: good
tags: [book, education, quantitative, portfolio-theory, factor-investing]
source_type: book
source_author: "Andrew Ang"
source_date: 2014
confidence: high
aliases: ["Asset Management Andrew Ang", "Ang Factor Investing", "Asset Management"]
related:
  - "[[factor-investing]]"
  - "[[smart-beta]]"
  - "[[risk-premia]]"
  - "[[portfolio-theory]]"
  - "[[fama-french-factors]]"
  - "[[momentum]]"
  - "[[low-volatility-anomaly]]"
---

## Overview

**Asset Management: A Systematic Approach to Factor Investing** by Andrew Ang, published in 2014, is widely regarded as the most rigorous practitioner-facing treatment of [[factor-investing]] available. Ang — a former Columbia Business School professor who became Head of Factor-Based Strategies at BlackRock — argues that asset class labels (stocks, bonds, hedge funds) are misleading and that investors should instead think in terms of underlying *factors* (value, momentum, carry, volatility, quality, low-vol) that drive returns across asset classes.

The central thesis: traditional asset allocation diversifies across labels but concentrates exposure to a handful of common factors. A 60/40 stock/bond portfolio is, in factor terms, 90% equity-risk premium because bonds are a much smaller risk contributor in volatility terms. True diversification requires diversifying across *factors*, not asset classes.

## Key Takeaways

- **Factors, not asset classes, are the building blocks of returns.** Equity risk, term, credit, value, momentum, carry, and volatility are the underlying drivers; asset classes are just bundles of these factors with various weights.
- **Most "alpha" is repackaged factor beta.** Hedge fund returns, after fees, can largely be replicated by static exposure to known factors. This is the basis of [[smart-beta]] and the case against high-fee active management.
- **Factor premia are compensation for bad-times risk.** Value, size, and momentum factors have positive long-run Sharpe ratios because they suffer in specific bad regimes (recessions, liquidity crises, momentum crashes). Investors who can stomach the bad regimes earn the premium.
- **Rebalancing is a hidden source of return.** Mechanically rebalancing back to target weights captures mean-reversion premium without any forecasting skill.
- **Liquidity is itself a factor.** Illiquid assets (private equity, real estate) earn an illiquidity premium — but the volatility and drawdown of these assets are systematically understated by stale pricing.
- **Active management costs more than its alpha.** Ang's analysis of net-of-fee active manager performance is devastating: the median active equity fund underperforms its benchmark, and the "winners" rarely persist.
- **Time-varying expected returns matter.** Equity premia, term premia, and credit premia all vary predictably with macro conditions. Portfolio policy should respond to these variations rather than assume static expected returns.
- **Liability-driven investing requires factor matching.** Pension funds and insurers should hedge their liability factor exposures (duration, inflation) before harvesting return-seeking factor premia.

## Who Should Read This

Allocators, portfolio managers, and serious individual investors who want to think rigorously about diversification. Quant practitioners building factor-based strategies will find the theoretical underpinnings useful. The book is dense — about 700 pages — but each chapter stands alone and the treatment of each factor is thorough.

## How It Applies to AI Trading

Ang's framework is the conceptual foundation for systematic equity and multi-asset strategies. The factor zoo (value, momentum, quality, low-vol, profitability, investment) is the universe from which most quant equity strategies are built — see [[fama-french-factors]] and [[smart-beta]]. The book's treatment of factor timing, factor crowding, and factor decay is directly relevant to anyone deploying live factor strategies.

For AI/ML trading specifically: Ang's central warning is that factor returns are not "free lunches" but compensation for specific risks. Models that learn to harvest factor premia must also model the bad-times risk they're getting paid for. A strategy that looks like alpha in backtest but is in fact loading on a known factor will deliver factor returns, not alpha — and will suffer the factor's drawdowns when they come.

## Rating

**9/10** — Rigorous, practitioner-relevant, and deeply researched. The most important book on portfolio construction since [[a-random-walk-down-wall-street|A Random Walk Down Wall Street]]. Read alongside [[expected-returns-antti-ilmanen|Expected Returns]] for a complete picture of factor investing.

## Sources

- Ang, Andrew (2014). *Asset Management: A Systematic Approach to Factor Investing*. Oxford University Press.

## Related

- [[factor-investing]] — The discipline Ang formalizes
- [[smart-beta]] — The product class derived from factor investing
- [[risk-premia]] — The economic justification for factor returns
- [[portfolio-theory]] — Classical framework Ang extends
- [[fama-french-factors]] — Foundational empirical work
- [[momentum]] — Most robust factor across markets
- [[low-volatility-anomaly]] — Factor that contradicts CAPM
- [[expected-returns-antti-ilmanen|Expected Returns (Ilmanen)]] — Companion text on factor premia
