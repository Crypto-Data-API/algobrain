---
title: "Strategy Research Checklist"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [strategy-development, research, methodology, checklist]
aliases: ["Pre-Mortem Checklist", "Strategy Pre-Flight"]
domain: [strategy-development]
difficulty: beginner
related: ["[[strategy-development-overview]]", "[[hypothesis-to-backtest-workflow]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
---

# Strategy Research Checklist

Twenty questions to answer *before* writing a single line of backtest code. If you cannot answer them all, the strategy is not yet ready to research.

The questions are loosely ordered: the early ones determine whether the idea is even worth investigating, the middle ones determine whether you can actually test it, and the later ones determine whether you can deploy it.

This checklist is the front end of the broader [[strategy-development-overview|strategy-development pipeline]]; it sits upstream of the [[hypothesis-to-backtest-workflow]] and is gated by the validation tools ([[overfitting-detection]], [[deflated-sharpe-ratio]], [[data-snooping-and-p-hacking]]).

## Stage Overview

| Stage | Questions | The gate it enforces | Kill if... |
|---|---|---|---|
| **I. Does the edge exist?** | 1-5 | Economic plausibility — is there a real loser? | You can't name the counterparty or the [[edge-taxonomy\|edge category]] |
| **II. Can I test it?** | 6-10 | Data feasibility — clean, point-in-time, tradable | Data is unavailable, not point-in-time, or survivorship-biased |
| **III. Will it survive validation?** | 11-14 | Statistical honesty — not a curve fit | Too many parameters; OOS contaminated; works on shuffled data |
| **IV. Will it survive deployment?** | 15-20 | Operational reality — can you actually run it | No kill criterion; unacceptable infra/regulatory/operational risk |

Each stage is a *gate*: a strategy must clear all of one stage before the next stage's questions are even worth asking. Most failed strategies die at Stage I (no real edge) or Stage III (overfit) — see [[failure-modes]].

## I. Does the Edge Exist?

### 1. Who is on the other side of my trade, and why are they willing to lose?

The single most important question. If you can't name the counterparty *and* explain why they keep showing up despite losing, you do not have an edge — you have a curve fit. See [[edge-taxonomy]] for the canonical losers in each edge category.

Acceptable answers:
- "Index funds forced to buy at the close"
- "Retail traders chasing momentum after CNBC features the stock"
- "Convertible arb desks hedging delta on issuance days"
- "Liquidity-takers paying the spread for immediacy"

Unacceptable answers:
- "The market"
- "Whoever is wrong"
- "Inefficient pricing"

### 2. Which of the six edge categories does this belong to?

Structural, behavioral, informational, analytical, latency, or risk-bearing. See [[edge-taxonomy]]. If "all of the above" or "none," go back to step 1.

### 3. Why hasn't this edge been arbitraged away?

If the edge is real and obvious, why is it still here? Possible answers:
- Capacity-constrained (too small for big funds)
- Capital-constrained (requires unusual leverage or funding)
- Skill-constrained (requires expertise few have)
- Reputation-constrained (looks bad on quarterly statements even if profitable)
- Unpopular (politically or aesthetically uncomfortable to run)
- Regulatorily protected (only certain participants can trade it)
- Recently discovered (true alpha decay window)

If none of these apply and the edge has been "known" for >5 years, assume it's been priced in.

### 4. Has anyone published this?

Search Google Scholar, SSRN, and arxiv for the underlying anomaly. If the answer is yes and the paper is older than 5 years, the edge has likely decayed (see [[failure-modes]] on alpha decay). If the paper is from this year, check whether it's already been replicated.

### 5. What's the theoretical maximum capacity?

Roughly: how much capital could trade this before the strategy moves the market against itself? A strategy that maxes out at $10M is a personal-account play; a strategy that scales to $1B is a fund. Be honest — many "great" strategies only work at sub-institutional sizes.

## II. Can I Actually Test It?

### 6. What data do I need, and is it available?

List every data series required:
- Price data (frequency, instruments, history depth)
- Fundamental data (point-in-time, restated handling)
- Alternative data (vendor, cost, lag)
- Reference data (corporate actions, splits, dividends, ticker changes)

If you don't have a path to acquiring all of it cleanly, the strategy is dead at the data step.

### 7. Is the data point-in-time?

Will the dataset reflect what was *knowable* at each historical moment, or has it been silently updated since? See [[lookahead-bias]]. The biggest hidden offenders:
- Fundamental data filed *after* fiscal period end
- Earnings estimates revised after the print
- Index constituents back-applied to dates before the constituent was added
- Macro data revised after first release (FRED is a major culprit)

### 8. Is the universe survivorship-free?

Will the dataset include companies that delisted, went bankrupt, or were acquired during the test period? See [[survivorship-bias]]. A long-only equity backtest on a survivorship-biased universe will overstate returns by 1-3% per year.

### 9. What's the smallest meaningful unit of capital, and can I trade it?

If the strategy generates 50 trades a day in 100 names, can your broker handle that volume? Are there minimum order sizes that break the strategy at small capital? Crypto strategies often look great in backtest and break against real exchange rate limits and minimum notional sizes.

### 10. What's the worst plausible slippage on each trade?

For each trade type, estimate: average bid-ask spread, market impact at your trade size, expected fill quality vs. mid. See [[transaction-cost-modeling]]. The dominant source of "real" P&L vs. "backtest" P&L divergence.

## III. Will It Survive Validation?

### 11. How many parameters does the strategy have?

Each parameter you tune is a degree of freedom that can absorb noise. A strategy with one parameter (e.g., a moving average length) and a 20-year backtest is *much* more credible than a strategy with 10 parameters and the same backtest. See [[overfitting-detection]] and the Bailey-Borwein-López de Prado work on backtest overfitting.

Rule of thumb: parameters × ranges tested should not exceed √(years of data). For 10 years of data, do not tune more than ~3 parameters seriously.

### 12. How many strategies have I already tried before this one?

If this is the 50th strategy you've tested on the same data, the best of 50 is biased upward by ~√(2 ln 50) ≈ 2.8 standard errors. See [[data-snooping-and-p-hacking]] and the [[deflated-sharpe-ratio]]. The deflated Sharpe ratio is the correct way to penalize this.

### 13. Will the in-sample / out-of-sample split be honest?

You must commit to the split *before* looking at any results. If you split, look at OOS, then go back and tweak based on what you saw, the OOS data is now contaminated and useless. The only honest path is "OOS exactly once, then either deploy or kill."

### 14. What does the strategy look like on shuffled data?

Run the same backtest on returns with the same volatility but no time-series structure (e.g., bootstrap-resampled returns). If the strategy still shows positive performance, there's a bug or a data leak.

### Validation toolkit

Stage III is where most "great" backtests die. The discipline is to penalize every degree of freedom and every trial. Map each risk to its tool:

| Risk | Symptom | Tool / page |
|---|---|---|
| Too many parameters | Smooth equity curve only at one parameter combo | [[overfitting-detection]]; parameter-count rule of thumb (≤ √years) |
| Many strategies tried | Best-of-N looks great by selection alone | [[deflated-sharpe-ratio]], [[data-snooping-and-p-hacking]] |
| OOS contamination | Tweaking after peeking at out-of-sample | Commit to the split first; "OOS exactly once" |
| Spurious time-series structure | Signal survives on shuffled/bootstrapped returns | Shuffle test, block bootstrap |
| Cost denial | Naive P&L ≫ realistic P&L | [[transaction-cost-modeling]] |
| Lookahead / restatement | Returns that vanish on point-in-time data | [[lookahead-bias]], [[survivorship-bias]] |

A naive backtest Sharpe means little until it is **deflated** for the number of trials and the parameter count. A strategy that survives the [[deflated-sharpe-ratio]] *and* the shuffle test *and* an honest cost overlay is a candidate; one that only survives the naive backtest is a curve fit waiting to disappoint.

## IV. Will It Survive Deployment?

### 15. What is the kill criterion?

Define in advance the numerical condition under which you will retire the strategy. Examples:
- "Kill if rolling 6-month Sharpe < 0"
- "Kill if drawdown exceeds 1.5× max historical drawdown"
- "Kill if cointegration p-value > 0.10 for 30 days"
- "Kill if turnover exceeds 1.5× research turnover"

A strategy without a kill criterion will live forever in your portfolio dragging down P&L because you can't bring yourself to turn it off. See [[when-to-retire-a-strategy]].

### 16. What infrastructure does it require?

- Data feeds (frequency, latency, reliability)
- Order routing (DMA, smart-order routing, broker API)
- Risk management (real-time position monitoring, kill switch)
- Logging and trade reconciliation
- Restart-and-recover behavior

A "simple" strategy with complex infrastructure requirements may be more expensive to run than a complex strategy with simple infrastructure.

### 17. What is the regulatory exposure?

- Pattern day trading rules (US equities, $25K minimum)
- Wash sale rules
- Short-sale restrictions (uptick rule, locate requirements)
- KYC/AML on certain venues
- Tax treatment (1256 contracts vs. equities, mark-to-market election)

### 18. What is the operational risk?

What happens if:
- A data feed goes down mid-day?
- The broker rejects an order?
- A position can't be closed (halt, circuit breaker)?
- The strategy gets caught in a flash crash (see [[flash-crash-2010]])?
- Your code crashes overnight with open positions?

Every strategy needs a manual override and a "flat everything now" button.

### 19. What's the failure mode?

How will this strategy *die*, eventually? Pick the most likely from [[failure-modes]] and write it down. Knowing the death scenario in advance lets you watch for early signs.

### 20. What's the monitoring plan?

Daily, weekly, monthly metrics. Who looks at them? What triggers an alert? What triggers a kill?

A strategy you deploy and don't monitor is a strategy you don't really run.

### Deployment-readiness summary

Before any capital goes live, every Stage IV line should have a written answer:

| Dimension | Question | Must have |
|---|---|---|
| Exit discipline | 15 | A numeric [[when-to-retire-a-strategy\|kill criterion]] committed in advance |
| Infrastructure | 16 | Data feed, order routing, kill switch, restart-recovery |
| Regulatory | 17 | PDT/wash-sale/short-locate/tax treatment understood |
| Operational | 18 | A "flat everything now" override for every failure mode |
| Failure mode | 19 | The most likely death scenario from [[failure-modes]] written down |
| Monitoring | 20 | Defined metrics, owner, alert and kill triggers |

## Using This Checklist

Print it out. Tape it next to your monitor. Force yourself to write a one-paragraph answer to each question *before* opening your IDE.

A strategy that fails this checklist is not "almost ready" — it is not ready. The discipline of refusing to research ideas that fail the pre-mortem is what separates a research process from idea-generation theater.

## Sources

- [[book-quantitative-trading-ernest-chan]] — chapters on idea evaluation
- [[book-advances-in-financial-machine-learning]] — López de Prado on the dangers of underconstrained research
- [[book-evidence-based-technical-analysis]] — Aronson on the file-drawer problem and pre-registration

## Related

- [[strategy-development-overview]]
- [[hypothesis-to-backtest-workflow]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[overfitting-detection]]
- [[data-snooping-and-p-hacking]]
- [[deflated-sharpe-ratio]] — the correct penalty for multiple trials
- [[transaction-cost-modeling]] — realistic slippage and impact
- [[lookahead-bias]] — point-in-time data discipline
- [[survivorship-bias]] — universe completeness
- [[when-to-retire-a-strategy]] — kill criteria in practice
- [[backtesting-pitfalls]] — the broader failure catalogue
