---
title: Trading Journal
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [risk-management, trading-psychology, discipline, journaling]
aliases: [trade journal, trade log, trade diary, post-mortem]
related:
  - "[[trading-psychology]]"
  - "[[overtrading]]"
  - "[[loss-aversion]]"
  - "[[trade-repair-and-rolling]]"
  - "[[position-sizing]]"
  - "[[stop-loss]]"
  - "[[failure-modes]]"
domain: [risk-management]
difficulty: beginner
---

# Trading Journal

A trading journal is a systematic record of every trade taken, including the rationale, execution details, outcome, and emotional state, used to identify strengths, weaknesses, and patterns in a trader's performance.

## What to Record

- **Setup** — What signal or pattern triggered the trade
- **Entry/Exit** — Prices, times, and position size
- **Risk parameters** — Stop-loss, target, risk/reward ratio, max loss defined at entry
- **Outcome** — P&L, whether the plan was followed
- **Emotional state** — Confidence level, stress, frustration, or excitement at entry and exit
- **Market context** — Broader market conditions, volatility regime, news catalysts
- **Adjustments made** — Any rolls, hedges, or repairs applied during the trade's life (see [[trade-repair-and-rolling]])
- **Screenshots** — Chart images at entry and exit for later review

## Why It Matters

Without a journal, traders rely on memory, which is biased by recency and emotion. A journal provides objective data that reveals:

- Which setups have the highest win rate and expectancy
- Whether [[overtrading]] is occurring
- Emotional patterns (e.g., revenge trading after losses)
- Time-of-day or market-condition performance differences
- Whether adjustments (rolls, repairs) improved or worsened outcomes over time

## Post-Mortem Framework for Losing Trades

The first rule of professional trade management is to separate the *loss on the original trade* from the *decision about what to do next*. Before any adjustment, disciplined traders do a structured post-mortem. (Source: [[recovering-losing-options-positions]])

### Step 1: Diagnose the Failure Mode

Every losing trade fails for a reason. Identify which category applies:

| Failure Mode | Description | Indicator |
|-------------|-------------|-----------|
| **Wrong direction** | The thesis was directionally wrong | Stock moved opposite to expectation |
| **Wrong volatility** | Direction was right but volatility was mispriced | P&L driven by IV changes, not price movement |
| **Poor sizing** | Correct thesis but position too large for the drawdown | Loss exceeded plan's risk budget |
| **Poor timing** | Correct thesis but entered too early or too late | Catalyst arrived after expiration or was priced in |
| **Thesis invalidated** | Fundamental reason for the trade no longer holds | Earnings miss, sector rotation, broken pattern |
| **Black swan / regime change** | External shock overwhelmed the position | Geopolitical event, flash crash, circuit breaker |

### Step 2: Decide — Repair, Hedge, or Exit?

Based on the diagnosis, the trader chooses one of four paths:

```
Was the thesis valid?
├── NO → Close the position. Accept the loss. Do not repair a broken thesis.
└── YES → Was the failure timing or sizing?
    ├── TIMING → Consider rolling (see [[trade-repair-and-rolling]])
    │   ├── Can roll for a credit or small debit? → Roll
    │   └── Rolling adds significant risk? → Close and re-enter later
    ├── SIZING → Reduce position to acceptable risk level, then reassess
    └── VOLATILITY → Consider hedging overlay (see [[hedging]])
        ├── Add protective puts, collar, or index hedge
        └── Wait for IV to normalize if thesis is intact

After a string of losses:
└── Consider a trading break to reset emotional capital
```

### Step 3: Record the Decision and Outcome

Log not just the loss, but:
- Which failure mode was identified
- Which action was taken (roll, hedge, exit, break)
- Whether the adjustment improved or worsened the final outcome
- What you would do differently next time

Over time, this creates a personal database of adjustment effectiveness. Many traders discover that their rolls improve outcomes in timing failures but deepen losses when the thesis was actually broken — data that cannot be gathered without disciplined journaling.

## Review Cadence

| Frequency | Focus |
|-----------|-------|
| **After each trade** | Record the trade and any adjustments immediately while memory is fresh |
| **Weekly** | Review the week's trades: win rate, average win/loss, adherence to rules, emotional patterns |
| **Monthly** | Analyze P&L by strategy, setup type, and market condition. Identify which setups to increase, reduce, or eliminate |
| **Quarterly** | Portfolio-level review: overall Sharpe, drawdown history, strategy-level performance. Compare to benchmarks |

## Trading Relevance

Professional traders and prop firms almost universally require journaling. It is the primary tool for turning trading into a data-driven process. Regular review sessions are essential — a journal that is never reviewed provides no benefit. The post-mortem process, combined with the adjustment framework in [[trade-repair-and-rolling]], creates a feedback loop that systematically improves decision-making over time. (Source: [[recovering-losing-options-positions]])

## Tools

Options range from simple spreadsheets to dedicated platforms like Tradervue, Edgewonk, or TradesViz. The best journal is the one that is actually maintained consistently.

## Related

- [[trade-repair-and-rolling]] — what to do after a loss is diagnosed (repair, roll, or exit)
- [[failure-modes]] — how strategies die in the wild
- [[position-sizing]] — sizing determines whether losses are survivable
- [[stop-loss]] — pre-defined exit rules that remove emotion
- [[trading-psychology]] — the emotional dimension of trading decisions
- [[overtrading]] — a common pattern revealed by journal review
- [[loss-aversion]] — the bias that prevents cutting losses

## Sources

- (Source: [[recovering-losing-options-positions]])
