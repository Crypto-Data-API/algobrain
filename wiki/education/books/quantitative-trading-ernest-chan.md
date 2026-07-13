---
title: "Quantitative Trading — Ernest Chan (2008)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, algorithmic, quantitative]
related:
  - "[[ml-trading-pipeline]]"
  - "[[backtesting-pitfalls]]"
  - "[[risk-management]]"
  - "[[algorithmic-trading-ernest-chan]]"
  - "[[quantitative-trading]]"
  - "[[backtesting]]"
  - "[[sharpe-ratio]]"
  - "[[kelly-criterion]]"
  - "[[mean-reversion]]"
---

## Overview

**Quantitative Trading: How to Build Your Own Algorithmic Trading Business** by Ernest P. Chan (2008) is the most practical guide for building an algorithmic trading business from scratch as an independent trader. Chan, a former quantitative researcher at institutional firms (including IBM Research, Morgan Stanley, and Credit Suisse) who went independent, walks through the entire process: finding strategy ideas in academic papers, evaluating whether they are worth pursuing, [[backtesting]] them properly, handling execution and transaction costs, managing risk, and going live with real capital. The book is refreshingly honest about what retail quants can and cannot compete on, steering readers toward strategies with limited capacity that large funds ignore.

It is widely regarded as the canonical "getting started" text for retail [[quantitative-trading|systematic trading]] and the foundation for Chan's two later books, [[algorithmic-trading-ernest-chan|*Algorithmic Trading*]] (2013) and *Machine Trading* (2017).

## Key Facts

| Field | Detail |
|-------|--------|
| **Author** | Ernest P. Chan (Ernie Chan), PhD physics (Cornell) |
| **Full title** | *Quantitative Trading: How to Build Your Own Algorithmic Trading Business* |
| **First published** | 2008 (Wiley Trading); 2nd edition 2021 |
| **Author background** | Quant researcher at IBM Research, Morgan Stanley, Credit Suisse; founder of QTS Capital Management |
| **Primary audience** | Aspiring independent / retail algorithmic traders |
| **Example tooling** | MATLAB (1st ed.); examples updated and Python-friendly resources in the ecosystem |
| **Core workflow** | Idea → evaluate → [[backtesting|backtest]] → execute → manage risk → scale |
| **Sequels** | [[algorithmic-trading-ernest-chan|*Algorithmic Trading*]] (2013), *Machine Trading* (2017) |
| **Difficulty** | Beginner-to-intermediate quant; assumes basic coding and statistics |

## Core Thesis

A disciplined individual can run a profitable systematic trading business without institutional resources — *if* they exploit the structural advantages of being small and avoid the traps that kill most retail strategies. The edge is not in raw firepower but in process: sourcing economically sensible ideas, validating them honestly against survivorship/look-ahead/cost biases, and applying rigorous [[risk-management]]. Small traders can profitably run low-capacity strategies (especially [[mean-reversion]] and statistical arbitrage on liquid instruments) that large funds cannot deploy without moving the market.

## Chapter / Section Themes

- **The whaling business of quant trading.** Whether an independent trader can realistically compete, and the lifestyle/business case.
- **Fishing for ideas.** Where to find strategies — academic papers (SSRN, NBER), journals, blogs, and trader forums — and how to filter the credible from the curve-fit.
- **Backtesting.** How to build an honest backtest and the biases that wreck it: survivorship, look-ahead, data-snooping, and unrealistic transaction-cost assumptions (see [[backtesting-pitfalls]]).
- **Setting up your business.** Brokers, data feeds, execution platforms, legal/tax structure, and the practical plumbing of going live.
- **Execution systems.** Automating order entry, paper trading, and minimizing the gap between backtest and live fills.
- **Money and risk management.** Position sizing via the [[kelly-criterion|Kelly criterion]], maximum-drawdown limits, leverage, and portfolio-level risk.
- **Special topics.** Mean-reversion vs. momentum, seasonal effects, high-leverage vs. high-beta, and the realities of strategy decay.
- **Conclusion: can independent traders succeed?** An honest appraisal of expectations and the discipline required.

## Key Concepts and Takeaways

| Concept | What it means |
|---------|---------------|
| **Find strategies in academic papers** | Published research (SSRN, NBER, journals) is the best free source of ideas. |
| **Evaluate before you build** | Check Sharpe, max drawdown, capacity, and economic rationale *before* writing code. |
| **Backtest properly or not at all** | Survivorship bias, look-ahead bias, and unrealistic cost assumptions are the three biggest backtest killers. |
| **[[sharpe-ratio|Sharpe ratio]] is the universal metric** | Lets you compare strategies across timeframes and asset classes; Chan suggests aiming high (Sharpe > ~2) for retail strategies. |
| **Start small and scale up** | Begin with minimal capital, confirm live matches backtest, then increase size gradually. |
| **Execution matters more than you think** | Slippage and commissions can turn a profitable backtest into a live loser. |
| **[[risk-management]] is non-negotiable** | [[kelly-criterion|Kelly]] (often fractional) sizing, drawdown limits, and correlation-aware allocation. |
| **Independent quants have edges** | No career risk, no bureaucracy, and the ability to trade low-capacity strategies funds ignore. |
| **Mean reversion suits the small trader** | Liquid, low-capacity [[mean-reversion]] and stat-arb setups are where retail can realistically win. |

## Criticisms and Limitations

- **Dated tooling and examples.** The 1st edition leans on MATLAB and pre-2008 market structure; some data sources and platforms named are obsolete (partly addressed by the 2021 2nd edition).
- **Optimistic Sharpe targets.** Critics note that the implied "Sharpe > 2" bar and example results are hard to reproduce live once realistic costs, slippage, and strategy decay are included.
- **Light statistical depth.** As an introduction it stays shallow on the statistics; rigorous overfitting detection (e.g., deflated Sharpe, the work of Marcos López de Prado) is barely touched — for that, see [[advances-in-financial-ml]].
- **Capacity reality check.** Many of the showcased low-capacity edges erode quickly as they become widely known; the book underplays how fast retail edges decay.
- **Execution gap.** Real-world infrastructure, latency, and broker quirks are harder than the book's tidy framework suggests.

## Who Should Read This

Aspiring independent algorithmic traders. Software engineers or data scientists who want to apply their skills to markets. Anyone who wants a realistic, step-by-step roadmap from idea to live trading. It is the best "getting started" book for systematic trading — read it before the heavier [[advances-in-financial-ml]].

## How It Applies to AI Trading

Chan's step-by-step framework maps directly to the [[ml-trading-pipeline]]. His process — source ideas, formulate hypotheses, engineer features, backtest rigorously, validate out-of-sample, go live with proper risk management — is identical whether you are testing a simple [[mean-reversion]] rule or training an XGBoost model. His emphasis on evaluating strategy capacity, realistic transaction costs, and proper [[backtesting|validation]] applies equally to ML strategies. The criteria he uses to filter strategies ([[sharpe-ratio|Sharpe]], drawdown, economic rationale) are the same filters you apply to ML model outputs. This book provides the business and operational framework around which you build an AI trading system.

## Rating

**8/10** — The most practical, retail-friendly quant trading book available. Some technical content is dated, but the framework and methodology are timeless. Read this before [[advances-in-financial-ml]] for the foundational context.

## Related

- [[algorithmic-trading-ernest-chan]] — The advanced sequel covering specific strategy types
- [[ml-trading-pipeline]] — Modern version of the workflow Chan describes
- [[backtesting-pitfalls]] — Expanded treatment of the validation issues Chan warns about
- [[risk-management]] — Kelly criterion and portfolio-level risk from Chan's framework
- [[quantitative-trading]] — The discipline this book introduces
- [[backtesting]] — The core validation step Chan stresses
- [[sharpe-ratio]] — Chan's universal strategy-comparison metric
- [[kelly-criterion]] — The position-sizing rule Chan applies
- [[mean-reversion]] — The strategy family best suited to small independent traders

## Sources

General market knowledge; no specific wiki source ingested yet.
