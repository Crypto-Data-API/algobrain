---
title: "Hypothesis to Backtest Workflow"
type: concept
created: 2026-04-10
updated: 2026-07-19
status: excellent
tags: [strategy-development, backtesting, methodology, research]
aliases: ["Strategy Research Pipeline", "Idea to Production Workflow"]
domain: [strategy-development]
difficulty: intermediate
related: ["[[strategy-development-overview]]", "[[research-checklist]]", "[[overfitting-detection]]", "[[walk-forward-analysis]]", "[[transaction-cost-modeling]]", "[[live-journal]]", "[[backtesting]]", "[[deflated-sharpe-ratio]]", "[[edge-taxonomy]]", "[[when-to-retire-a-strategy]]", "[[survivorship-bias]]", "[[lookahead-bias]]", "[[machine-learning]]"]
---

# Hypothesis to Backtest Workflow

The end-to-end pipeline a strategy must travel from "I had an idea" to "this is running with real money." Each stage is a filter. The point is to kill bad ideas as cheaply and early as possible. The workflow is the operational backbone of disciplined [[backtesting]]: it converts the abstract warnings about [[overfitting-detection|overfitting]], [[lookahead-bias|look-ahead]], and [[survivorship-bias|survivorship]] into a sequence of concrete gates, each with a pass/kill decision.

## The Stages

```
Observation
   ↓
Hypothesis (mapped to edge category)
   ↓
Pre-mortem (research checklist)
   ↓
Data assembly
   ↓
Naive backtest (in-sample)
   ↓
Bug hunt (lookahead, survivorship, etc.)
   ↓
Out-of-sample test
   ↓
Walk-forward
   ↓
Sensitivity analysis
   ↓
Cost overlay
   ↓
Statistical correction (deflated Sharpe)
   ↓
Paper trade (1-3 months)
   ↓
Pilot capital (10% of intended size)
   ↓
Full capital
   ↓
Ongoing monitoring with kill criteria
```

Most strategies should die before stage 6. A research process that kills 95% of ideas is healthy. A research process that approves 50% of ideas is broken — you are deluding yourself somewhere in the pipeline.

## Stage Summary

The table fixes, for each gate, the question it answers, the cheap-and-fast test that passes or kills the idea, and the most common way the stage is gamed. Read it top-to-bottom as a checklist; never skip a row to "save time" — the skipped gate is exactly where the false positive hides.

| # | Stage | Question it answers | Pass / kill test | How it gets gamed |
|---|-------|---------------------|------------------|-------------------|
| 1 | Observation | Is there a real anomaly? | Written down before any analysis | Editing the observation post-hoc to fit results |
| 2 | Hypothesis | What/why/when-fails, falsifiable? | All three parts written in one sitting; maps to an [[edge-taxonomy]] category | A "why" that is just a restatement of the "what" |
| 3 | Pre-mortem | Who loses to me, and why? | Named counterparty in [[research-checklist]] | "The market is inefficient" with no named loser |
| 4 | Data assembly | Is the data point-in-time and clean? | Includes delisted names; filing-date timestamps | Using free, survivorship-biased data |
| 5 | Naive backtest | Does the raw effect exist? | Sharpe ≥ ~0.3 in-sample, no optimisation | Adding filters/stops to manufacture a signal |
| 6 | Bug hunt | Is the result an artefact? | Shuffled-data test shows ~0 performance | Skipping the shuffle test |
| 7 | Out-of-sample | Does it hold on untouched data? | OOS Sharpe ≥ ~½ in-sample, run **once** | Peeking at OOS then "tweaking" |
| 8 | Walk-forward | Would it have traded in real time? | Stable rolling [[walk-forward-analysis]] equity curve | Re-fitting windows until the curve looks good |
| 9 | Sensitivity | Is it a plateau, not a peak? | Sharpe stable under ±25% parameter shifts | Reporting the single best parameter cell |
| 10 | Cost overlay | Survives realistic friction? | Net-of-cost Sharpe still positive (see [[transaction-cost-modeling]]) | Modelling midpoint fills, zero impact |
| 11 | Statistical correction | Significant after multiple testing? | [[deflated-sharpe-ratio]] significant at p<0.05 | Not counting the trials you ran |
| 12 | Paper trade | Does live plumbing match backtest? | Paper P&L tracks backtest for the same window | Calling it "paper" while skipping it |
| 13 | Pilot capital | Survives real fills at small size? | One full strategy cycle at 5-10% size | Jumping straight to full size |
| 14 | Full capital | Scales without impact blowup? | Performance holds at intended AUM | Ignoring capacity limits |
| 15 | Monitoring | When do I kill it? | Pre-committed numeric kill criteria | "I'll know when to stop" |

## Stage-by-Stage Detail

### Stage 1: Observation

Where do ideas come from? In rough order of usefulness:

1. **Anomalies in your own trading data** — strategies you're already running show unexpected patterns
2. **Market microstructure observations** — you notice the same bid getting hit at the same time of day
3. **Conversations with other traders** — but always re-derive, never trust hearsay
4. **Academic papers** — high quality, but heavily fished. See [[anomalies-overview]].
5. **Books and talks** — older the better, since fresh ideas are usually crowded
6. **News events that "shouldn't" have moved markets the way they did**
7. **Twitter/social** — almost always already priced in by the time you see it

Write the observation down in a notebook *before* you do any analysis. The exact form of the observation will bias your backtest later — if you don't lock it in, you'll unconsciously edit it to match what worked.

### Stage 2: Hypothesis

Convert the observation into a falsifiable hypothesis with three components:

1. **What** — the precise pattern or regularity claimed
2. **Why** — the mechanism that produces it (must map to one of the six edge categories — see [[edge-taxonomy]])
3. **When it should fail** — the conditions under which the hypothesis predicts no edge

Example:

> **What:** Stocks that gap up >5% on >2x average volume tend to continue higher for the next 5 trading days.
>
> **Why:** Behavioral edge — institutional investors anchor on previous closing prices and underreact to new information, causing gradual repricing over multiple sessions.
>
> **When it should fail:** During earnings season for the gapping stock (information is fully discounted), in low-volume markets (no institutional follow-through), or when the broader market is in a high-volatility regime (noise dominates the signal).

If you can't write all three parts in one sitting, the idea is not yet a hypothesis. Send it back to the notebook.

### Stage 3: Pre-mortem

Before writing any code, answer the questions in [[research-checklist]]. The point is to identify ways the strategy could fail *before* you become emotionally invested in it.

The single most important question: **who is on the other side of my trade, and why are they willing to lose?** If you cannot name the loser, there is no edge.

### Stage 4: Data Assembly

The hardest and most under-appreciated stage. Most strategies fail here even though the failure looks like it happened later.

Requirements for honest data:

- **Point-in-time** — every data point reflects what was *knowable at that moment*. Earnings revisions, restatements, ticker changes, splits, dividends, corporate actions all need to be applied as-of, not retroactively.
- **Survivorship-bias free** — must include delisted, bankrupt, and merged companies. See [[survivorship-bias]].
- **Look-ahead free** — no future information leaking into past timestamps. See [[lookahead-bias]]. Common offenders: same-day close prices used as "available" intraday, fundamental data timestamped at fiscal period end rather than filing date, alternative data with reporting lag not modeled.
- **Universe-stable** — your universe selection rule must itself be applied point-in-time. "Top 500 by market cap *as of today*" is a snapshot; "top 500 by market cap *as of each historical date*" is point-in-time.
- **Transaction-level when possible** — daily OHLCV is fine for slow strategies, but anything claiming to fill at "the open" is making a heroic assumption. Use trades and quotes if your strategy is intraday.

Common cheap-but-biased data sources to avoid for serious work: Yahoo Finance (survivorship-biased), FRED (revised data, not original prints), most free crypto APIs (no historical orderbook).

Spend 2-3x as long on data assembly as you think you need to. It is the dominant source of false positives in backtesting.

**Data integrity checklist** — every box must be ticked before the data is trusted:

| Check | Failure looks like | Fix |
|-------|--------------------|-----|
| Point-in-time fundamentals | Restated GAAP numbers; data timestamped at fiscal-period end | Use filing-date as-of timestamps |
| Survivorship-free universe | No delisted/bankrupt/merged names | Include the full historical roster — see [[survivorship-bias]] |
| Look-ahead-free signals | Same-day close used "intraday"; lagged alt-data with no lag modelled | Shift every input to its true availability time — see [[lookahead-bias]] |
| Point-in-time universe | "Top 500 today" applied to history | Reconstruct universe membership per historical date |
| Corporate actions applied as-of | Splits/dividends/ticker changes back-applied | Apply each action on its effective date |
| Adequate granularity | Daily bars on an intraday strategy | Use trades/quotes when fills matter |

### Stage 5: Naive Backtest

Implement the strategy in the simplest possible way that captures the hypothesis. Do not optimize parameters. Do not add filters. Do not add stop-losses. Just run the rules.

The goal at this stage is *not* to see good performance. The goal is to see whether the basic effect exists. If a strategy needs three filters and a stop-loss to be profitable in-sample, it has no edge — it has a fitting artifact.

A useful heuristic: the simplest version of the strategy should produce a Sharpe ≥ 0.3 in-sample with no parameter optimization. If it doesn't, the underlying effect is probably noise.

### Stage 6: Bug Hunt

Before celebrating any in-sample result, hunt for bugs. The most common:

1. **Lookahead bias** — using data not available at the decision time. Even one bar of leakage can turn a Sharpe of 0 into a Sharpe of 3.
2. **Off-by-one fills** — assuming you can buy at the close and sell at the close of the same bar.
3. **Universe leakage** — back-applying today's universe to historical dates.
4. **Restated fundamentals** — using GAAP numbers as they exist today, not as they were originally reported.
5. **Trade rounding** — assuming you can buy 0.0001 shares of a $200 stock.
6. **Free fills** — no commissions, no slippage, fills at midpoint.

Run the strategy on shuffled data (random returns with the same volatility). If it still shows positive performance, you have a bug.

### Stage 7: Out-of-Sample Test

Set aside 30-50% of your data *before doing anything* and do not touch it during stages 5-6. Once the strategy is finalized, run it on the held-out set exactly once. Whatever number you get is the closest thing you have to an honest performance estimate.

If the out-of-sample Sharpe is less than half the in-sample Sharpe, the strategy is overfit and should be killed.

**Critical rule:** if you look at the OOS result and then go back and tweak the strategy, you have just *contaminated* the OOS set. You no longer have any honest performance estimate. The only way to recover is to acquire new data that didn't exist when the tweak was made.

### Stage 8: Walk-Forward Analysis

A more honest version of OOS testing. See [[walk-forward-analysis]] for the full method. The short version: train on a rolling window, test on the immediately following window, slide forward, repeat. The walk-forward equity curve is what you would have actually traded had you been doing this in real time.

### Stage 9: Sensitivity Analysis

Vary every parameter by ±25% and check that performance is roughly stable. A strategy whose Sharpe collapses if you change the lookback window from 20 to 22 days is fitting the specific historical noise of those two days.

Plot a heatmap of Sharpe over the parameter space. You want a *plateau* of good performance, not a *peak*. A peak is overfitting; a plateau is robustness.

### Stage 10: Cost Overlay

Add realistic costs. See [[transaction-cost-modeling]]. The big ones:

- **Commissions** — small but real, especially for high-turnover strategies
- **Bid-ask spread** — half-spread per side at minimum
- **Market impact** — square-root law: impact ≈ k × σ × √(trade size / ADV)
- **Borrow costs** — for shorts, especially in small caps and crypto
- **Funding rates** — for perpetual futures
- **Financing** — for leveraged positions
- **Taxes** — short-term capital gains rates if applicable

A strategy that's profitable gross but unprofitable net is a *capacity constraint discovery*, not a strategy. Sometimes you can shrink position size or change venues to fix it; usually you can't.

### Stage 11: Statistical Correction

If you tested N strategies and picked the best one, the best one's Sharpe is biased upward by approximately √(2 × ln(N)). See [[deflated-sharpe-ratio]] and [[data-snooping-and-p-hacking]].

Compute the deflated Sharpe ratio. If it's not significant at p < 0.05 *after* correction, you're looking at noise.

This is the stage that kills the most strategies. Embrace it. A real edge will survive it. A fake one won't.

### Stage 12: Paper Trade

Run the strategy live with no capital for 1-3 months. Compare the paper P&L to what your backtest would have predicted for the same period. If they diverge significantly, your backtest is missing something — usually transaction costs, slippage, or a data-source difference between research and production.

Paper trading is also where you discover infrastructure bugs: clock skew, missed bars, broken data feeds, exchange downtime.

### Stage 13: Pilot Capital

Start with 5-10% of intended capital. Run for at least one full cycle of the strategy (whatever that means — a quarter for slow strategies, a week for fast ones). Watch for divergence from paper trading.

### Stage 14: Full Capital

Scale to full size. Do not skip the pilot stage. The number of strategies that look great in paper trading and break in pilot is non-trivial.

### Stage 15: Ongoing Monitoring with Kill Criteria

Define *in advance* the conditions under which you will kill the strategy:

- Drawdown exceeds X%
- Rolling 3-month Sharpe falls below Y
- Realized turnover exceeds Z (transaction cost blowup)
- Hypothesis-specific kill: e.g., "if cointegration p-value > 0.10 for 30 days, kill the pair"

The single hardest discipline in trading is killing strategies you used to love. Pre-committing to numerical criteria removes the emotion. See [[when-to-retire-a-strategy]].

## How Long Should This Take?

A serious end-to-end research cycle for a single strategy is usually 4-12 weeks of focused work. Anyone claiming to ship multiple new strategies per week is either (a) running a research factory with deep infrastructure, (b) overfitting, or (c) shipping noise.

## Worked Example: One Idea Through the Pipeline

Tracing the gap-and-go hypothesis from Stage 2 through the gates makes the filtering concrete. All numbers below are *illustrative* — they show how a decision is reached at each gate, not a real backtest result.

| Stage | What happens to the gap-and-go idea | Decision |
|-------|-------------------------------------|----------|
| 1 Observation | Noticed several large-gap names drifting higher over a week | Logged in notebook |
| 2 Hypothesis | What: >5% gap on >2× volume drifts up 5 days. Why: behavioural under-reaction. When-fails: earnings season, low volume, high-vol regime | Passes — falsifiable, mapped to behavioural edge |
| 3 Pre-mortem | Loser named: slow institutional rebalancers anchored to prior close | Passes — counterparty identified |
| 4 Data | Need survivorship-free, point-in-time prices + volume + the gappers' delisting history | Passes after sourcing clean data |
| 5 Naive backtest | Raw rule (buy gap, hold 5 days) yields ~0.4 Sharpe in-sample | Passes the ~0.3 floor |
| 6 Bug hunt | Shuffled-returns run shows ~0 Sharpe; no look-ahead in the gap calc | Passes |
| 7 OOS | Held-out set shows ~0.25 Sharpe (just over half of in-sample) | Passes, marginally — run once |
| 8 Walk-forward | Rolling windows show edge concentrated pre-2018, decaying since | Warning — possible crowding/decay |
| 9 Sensitivity | Sharpe stable from 4-6% gap and 1.8-2.5× volume — a plateau | Passes |
| 10 Cost overlay | Half-spread + impact cuts net Sharpe to ~0.1 (high turnover, small caps) | **Likely kill** — capacity-constrained |
| 11 Deflated Sharpe | After counting ~40 trials, deflated Sharpe not significant | **Kill** |

This idea dies at the cost/statistical gates — the common fate. The lesson: the early stages can all "pass" while costs and multiple-testing correction reveal there was never an exploitable edge. Killing it here is the system working, not failing.

## Common Pitfalls Across the Whole Pipeline

1. **OOS contamination.** Looking at the held-out result and then tweaking the strategy destroys the only honest estimate you had (Stage 7). The fix requires *new* data, not a fresh split of the old.
2. **Optimising before validating.** Adding filters and stops in the naive-backtest stage manufactures in-sample performance that won't survive OOS. Keep Stage 5 dumb on purpose.
3. **Under-counting trials.** The deflated Sharpe correction needs the *true* number of configurations tried — including the ones you discarded mentally. Under-counting N inflates significance.
4. **Treating a gross-profitable strategy as live-ready.** A net-unprofitable strategy is a capacity discovery, not a strategy (Stage 10).
5. **Skipping paper/pilot.** The strategies that look great in backtest and break in production are exactly the ones that skip the live-plumbing gates (Stages 12-13).
6. **No pre-committed kill criteria.** Without numeric kill rules set in advance, you will rationalise holding a dead strategy. See [[when-to-retire-a-strategy]].
7. **Over-trusting ML stages.** [[machine-learning|ML]] classifiers multiply the number of implicit trials enormously; the deflated-Sharpe correction and walk-forward discipline matter *more*, not less, when ML is in the loop.

## What Goes In the Strategy Page

Every strategy page in the wiki should record where it currently sits in the pipeline via the `backtest_status` frontmatter field. Consider extending the enum:

```
untested → naive-backtested → walk-forward-validated → cost-corrected →
deflated-sharpe-significant → paper-traded → pilot → live → retired
```

This makes it trivial to see at a glance which strategies are research-quality vs. production-quality.

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan's research workflow chapter
- [[book-advances-in-financial-machine-learning]] — López de Prado on each stage
- [[book-evidence-based-technical-analysis]] — Aronson on the discipline of falsification

## Getting the Data (CryptoDataAPI)

The pipeline's data legs run on the [[cryptodataapi-backtesting|CryptoDataAPI backtesting archive]]: `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d since 2017-08), `GET /api/v1/backtesting/funding`, `GET /api/v1/backtesting/daily-snapshots` (point-in-time full-market snapshots since 2026-03-02), and `GET /api/v1/quant/regimes/history` (hourly regime probabilities since 2020).

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the front of this pipeline:

- **Idea generation** — the "Strategy Hypothesis Generator" prompt (Pro Plus tier, [prompt library](https://cryptodataapi.com/prompts)) converts historical daily snapshots into falsifiable hypotheses, each forced to state premise/mechanism, entry rule, and exit rule — exactly the Stage 1→2 gate on this page
- **Point-in-time discipline** — replay `/api/v1/backtesting/daily-snapshots/{date}` rather than today's labels, avoiding [[lookahead-bias]] at the hypothesis stage
- **Kill cheaply** — cap generated hypotheses (the prompt enforces 2-3 max) so [[data-snooping-and-p-hacking|multiple-testing]] corrections stay honest

## Related

- [[strategy-development-overview]]
- [[research-checklist]]
- [[overfitting-detection]]
- [[walk-forward-analysis]]
- [[transaction-cost-modeling]]
- [[deflated-sharpe-ratio]]
- [[when-to-retire-a-strategy]]
