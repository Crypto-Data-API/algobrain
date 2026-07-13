---
title: "Trade Machine (Capital Market Laboratories)"
type: source
created: 2026-05-07
updated: 2026-06-12
status: good
tags: [data-provider, options, backtesting, derivatives, technology]
aliases: ["Trade Machine", "Trade Machine Pro", "CML Trade Machine", "Capital Market Labs Trade Machine"]
source_type: data
source_url: "https://www.cmlviz.com/trademachine"
confidence: medium
related:
  - "[[options-concentration-risk]]"
  - "[[backtesting]]"
  - "[[backtesting-overview]]"
  - "[[options-greeks]]"
  - "[[orats]]"
  - "[[orats-research]]"
  - "[[convex-trading]]"
  - "[[pivolio]]"
---

Trade Machine is a retail-facing options strategy backtester operated by Capital Market Laboratories (CML, also known as CMLviz), a research and analytics firm best known for systematic options-strategy publications. The tool lets retail and semi-professional traders backtest defined options strategies (covered calls, iron condors, calendars, earnings strangles, etc.) across thousands of underlyings using point-and-click rule construction rather than code. Trade Machine is positioned as the most accessible options-specific backtester for traders who don't want to build a Python framework but need more than a payoff diagram.

> **Note on naming**: "Trade Machine" / "Trade Machine Pro" is the CMLviz / Capital Market Laboratories product. [[orats|ORATS]] also has options-backtesting tooling under different product names; the two are distinct products from competing vendors.

## What It Produces

- **Rule-based options strategy backtests**: define entry rules (e.g., "open a 30 DTE 25-delta call spread on every Monday"), exit rules (e.g., "close at 50% profit or 21 DTE"), and run the backtest across history
- **Pre-built strategies**: dozens of templated strategies — covered calls, cash-secured puts, iron condors, calendars, diagonals, earnings plays — that can be applied to any underlying
- **Earnings-event strategies**: specifically focused on pre/post-earnings options trades, which is a CML / CMLviz signature use case
- **Symbol screening**: run a strategy across a universe of tickers and rank by historical performance
- **Trade-by-trade output**: each backtest produces a list of historical trades with entry, exit, P&L
- **Aggregate statistics**: win rate, average return, profit factor, max drawdown
- **Visualization**: equity curves, win/loss histograms, return distributions

## Pricing Tier

Standard pricing for **CML Trade Machine Pro** is **$129/month** as of mid-2026 (verified via cmlviz.com / trademachine.com, June 2026). CMLviz periodically runs promotional pricing (e.g. discounted lifetime-locked subscriptions capped at a fixed number of users registered before a deadline), so the effective price a given user pays can be lower. The product is also distributed through the dedicated **trademachine.com** registration domain alongside the main **cmlviz.com** site.

CMLviz / Capital Market Laboratories markets three products overall; Trade Machine Pro is the stock-and-options back-tester, bundled with a trade-discovery engine, the Pro Scanner, intraday alerts, and CML's proprietary technical signals (e.g. the "CML Mammoth Model"). Recent (2025-2026) feature additions include live options pricing with exact strike/expiration for actionable trades, ~7x faster backtests, and the ability to backtest up to ~200 tickers (and select up to ~50 at once) in a single run.

## How It's Used in Practice

Typical user workflows:

1. **Strategy validation**: a trader has read about (e.g.) "selling iron condors on QQQ at 30 DTE" and wants to know how it has performed historically. Trade Machine lets them run the backtest in a few minutes without writing code.

2. **Symbol selection**: given a strategy template, screen a universe of underlyings to find which symbols have historically been most profitable for that structure. Useful for picking earnings-strangle candidates.

3. **Parameter tuning**: vary entry delta, DTE, exit profit target, exit DTE — see how performance varies. The same overfitting risks as any backtest apply ([[backtesting-pitfalls]]).

4. **Earnings strategies**: CML publishes systematic earnings-event research; Trade Machine is the tool for replicating and customizing those backtests.

## Relationship to Options Concentration Risk

Trade Machine is not primarily a portfolio-concentration tool — it is a backtester. Its relevance to [[options-concentration-risk]] is indirect:

- **Strategy-level historical risk**: backtesting a candidate strategy reveals its drawdown profile, which informs sizing and concentration limits
- **Cross-symbol comparison**: running a strategy across multiple symbols can reveal which underlyings the strategy has worked on, helping a trader avoid blindly piling up the same strategy on correlated names
- **Earnings cluster awareness**: the earnings-strategy focus surfaces the natural earnings clustering risk discussed in [[options-concentration-risk]]

What Trade Machine does *not* do:

- Real-time portfolio aggregation (that's what [[ibkr-risk-navigator]], [[pivolio]], or [[convex-trading]] are for)
- Factor decomposition (that's [[barra]] / [[axioma]] / [[northfield]])
- Cross-position Greeks rollup
- Stress testing of an existing book

For concentration management, Trade Machine is upstream of the live portfolio — it helps decide which strategies are worth running, not how to size and limit them once running.

## Strengths

- **No-code interface**: accessible to options traders without programming background
- **Options-specific**: built for options strategies; covers earnings, IV-rank-based entries, defined-risk structures natively
- **Pre-built templates**: most common retail options strategies are one click away
- **CML research integration**: tied to CMLviz's published systematic research; users can replicate and customize the published studies
- **Speed**: backtests run in seconds vs minutes/hours for code-based frameworks

## Limitations

- **Backtest-only**: no live trading, no portfolio aggregation, no concentration management
- **Historical option data**: quality of backtests depends on the underlying option data feed; for retail-facing tools, the data tends to be end-of-day mid-prices, which underestimates real-world transaction costs and slippage
- **Overfitting risk**: easy point-and-click parameter optimization is the most common path to [[backtesting-pitfalls|overfit backtests]]
- **Limited customization**: rule constructor handles common patterns but not arbitrary logic; for complex multi-leg dynamic strategies, code-based frameworks (Python with [[orats]] or [[optionmetrics]] data) are more flexible
- **Cost stack**: monthly subscription adds up; for serious quants, building a custom backtester with bulk data once is often cheaper long-term
- **Not a portfolio risk tool**: explicitly outside the concentration / Greeks-aggregation use case

## Compared to Alternatives

| Tool | Position | Concentration use? |
|------|----------|-------------------|
| **Trade Machine (CML)** | Retail options backtester, no-code | No (backtester only) |
| ORATS Backtesting | Backtester from ORATS, often code-driven | No (backtester only) |
| [[backtesting-py]] / Python frameworks | Code-based, fully customizable | Build it yourself |
| [[ibkr-risk-navigator]] | Live portfolio risk | Yes |
| [[bloomberg-terminal]] OSA | Both backtest and portfolio risk | Yes (institutional) |

## Related

- [[options-concentration-risk]] — Trade Machine is upstream of concentration management
- [[backtesting]] — broader backtesting context
- [[backtesting-overview]] — framework comparison
- [[backtesting-pitfalls]] — overfitting risks particularly relevant to no-code backtesters
- [[orats]] — competing options data + backtesting vendor
- [[orats-research]] — alternative systematic options research source
- [[convex-trading]] — comparable third-party options analytics
- [[pivolio]] — comparable third-party options portfolio tool
- [[options-greeks]] — what backtests aggregate at the trade level

## Sources

- CMLviz / Capital Market Laboratories public documentation — https://www.cmlviz.com/option-back-tester and https://www.trademachine.com (pricing $129/mo and feature set verified via web search, June 2026)
- Capital Market Laboratories products page — https://www.capitalmarketlabs.com/products/
- Referenced in [[options-concentration-risk]] as a third-party options analytics tool
- Note: confirmed Trade Machine is the CML product; not to be confused with ORATS' separate backtesting suite
