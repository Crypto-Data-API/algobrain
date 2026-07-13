---
title: "Backtesting.py"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [backtesting, python, algorithmic]
aliases: ["Backtesting.py", "backtesting.py"]
domain: [backtesting]
difficulty: beginner
related:
  - "[[backtrader-framework]]"
  - "[[vectorbt]]"
  - "[[optuna]]"
  - "[[event-driven-backtesting]]"
  - "[[backtesting-pitfalls]]"
  - "[[pybroker]]"
  - "[[execution-model-differences]]"
  - "[[lookahead-bias]]"
  - "[[backtesting]]"
  - "[[walk-forward-analysis]]"
---

# Backtesting.py

**Backtesting.py** is a lightweight, event-driven backtesting library for Python with a cleaner, more Pythonic API than [[backtrader-framework|Backtrader]]. It is well-suited for quick prototyping and single-asset strategy development, with a built-in grid optimizer and interactive HTML chart output. Install with `pip install backtesting`. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Overview

Backtesting.py occupies the "simple and fast to set up" niche in the Python backtesting ecosystem. Where [[backtrader-framework|Backtrader]] has a steep learning curve and [[vectorbt|VectorBT]] requires thinking in vectorized arrays, Backtesting.py lets you define a strategy in under 20 lines with a familiar class-based pattern.

### At a Glance

| Attribute | Detail |
|-----------|--------|
| **Author / maintainer** | `kernc` (open-source) |
| **Install** | `pip install backtesting` |
| **Engine type** | [[event-driven-backtesting\|Event-driven]] (bar-by-bar `next()` loop) |
| **Asset scope** | Single asset / single instrument per `Backtest` instance |
| **Indicator wrapper** | `self.I(func, *args)` — registers and plots indicators |
| **Optimizer** | Built-in brute-force grid (`bt.optimize`) |
| **Plotting** | Bokeh interactive HTML |
| **Data input** | A pandas DataFrame with `Open, High, Low, Close, Volume` columns and a datetime index |
| **License** | AGPL-3.0 (relevant for closed-source/commercial deployment) |
| **Live trading** | Not supported — research/backtest only |

The data-input contract is strict: column names are case-sensitive (`Open`, `High`, `Low`, `Close`, optionally `Volume`) and the index must be a `DatetimeIndex`. This rigidity is part of what keeps the API small. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Core API

```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

class SmaCross(Strategy):
    fast_period = 10
    slow_period = 30

    def init(self):
        self.fast_ma = self.I(SMA, self.data.Close, self.fast_period)
        self.slow_ma = self.I(SMA, self.data.Close, self.slow_period)

    def next(self):
        if crossover(self.fast_ma, self.slow_ma):
            self.buy()
        elif crossover(self.slow_ma, self.fast_ma):
            self.sell()

bt = Backtest(data, SmaCross, cash=100_000, commission=0.002)
stats = bt.run()
bt.plot()  # Interactive HTML chart (Bokeh)
```

Two methods define the entire strategy:
- **`init()`** — compute indicators once upfront using `self.I()` wrapper
- **`next()`** — called on each bar; make buy/sell decisions using current indicator values

Inside `next()`, the strategy interacts with the broker through a small object surface:

| Object / call | Purpose |
|---------------|---------|
| `self.buy(size=..., sl=..., tp=...)` | Open/extend a long; optional stop-loss and take-profit |
| `self.sell(...)` | Open/extend a short (or close a long) |
| `self.position` | Current position object — `.size`, `.pl`, `.pl_pct`, `.close()` |
| `self.trades` / `self.closed_trades` | Open and historical trade records |
| `self.data` | Rolling view of OHLCV up to the current bar (no future bars exposed) |
| `self.equity` | Current account equity |

Crucially, `self.data` inside `next()` is a *windowed* array that only exposes bars up to and including the current one, which structurally prevents the array-indexing form of [[lookahead-bias|look-ahead bias]] (source #7 in that page). The remaining leakage risk is the same-bar fill behavior, covered in [[#Execution Model|Execution Model]] below.

---

## Built-In Optimizer

Backtesting.py includes a grid-based optimizer:

```python
stats, heatmap = bt.optimize(
    fast_period=range(5, 50, 5),
    slow_period=range(50, 200, 10),
    maximize="Sharpe Ratio",
    return_heatmap=True
)
```

This tests all combinations of `fast_period` and `slow_period` and returns the parameter set that maximizes the chosen metric. The heatmap output is useful for visualizing parameter sensitivity.

**Limitation:** The optimizer is brute-force grid search — it tests every combination, which becomes impractical for large parameter spaces (3+ parameters with fine granularity). For smarter optimization, wrap Backtesting.py in an [[optuna|Optuna]] objective function instead:

```python
import optuna

def objective(trial):
    fast = trial.suggest_int("fast", 5, 50)
    slow = trial.suggest_int("slow", 50, 200)
    stats = bt.run(fast_period=fast, slow_period=slow)
    return stats["Sharpe Ratio"]

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)
```

---

## Interactive HTML Output

One of Backtesting.py's standout features is its Bokeh-based interactive HTML chart:
- Equity curve with drawdown shading
- Trade markers (entry/exit) overlaid on price chart
- Indicator subplots
- Zoom, pan, and hover for trade details
- Exportable as standalone HTML file

This makes it excellent for visual trade review and strategy presentation.

---

## How Trading and AI Systems Use It

Backtesting.py is most commonly used at the *front* of a research pipeline, before a strategy graduates to a heavier framework:

- **Rapid hypothesis screening.** Because a strategy is ~20 lines, a researcher can vet a dozen indicator ideas in an afternoon, discarding the obvious non-starters before investing in [[walk-forward-analysis|walk-forward]] rigor.
- **Wrapping for smarter optimization.** The class-based `Strategy` is easy to wrap in an [[optuna|Optuna]] objective (see code below) to escape the brute-force grid and use Bayesian/TPE search instead.
- **ML signal as an input, not an engine.** Backtesting.py has no native ML loop. The common pattern is to train a model *outside* the backtest, write its per-bar predictions into a column of the input DataFrame, and read that column inside `next()`. This works but puts the burden on the researcher to avoid leaking future data into the precomputed predictions — exactly the failure mode that [[pybroker]] automates away with temporal windowing and [[purged-kfold-cv|purged CV]].
- **Teaching and demonstration.** Its readability and interactive charts make it a standard choice for tutorials and for communicating a strategy's behavior to non-coders.

The boundary is clear: Backtesting.py is a **single-asset event-driven prototyper**. Portfolio construction, ML-native training, and high-throughput parameter sweeps belong to [[vectorbt]], [[pybroker]], or [[backtrader-framework|Backtrader]].

| Need | Better tool |
|------|-------------|
| Multi-asset / portfolio rebalancing | [[vectorbt]], [[backtrader-framework\|Backtrader]] |
| Model trained inside the loop with leak protection | [[pybroker]] |
| Thousands of parameter combinations, fast | [[vectorbt]] (vectorized, ~100–1000× faster) |
| Live trading / broker connectivity | [[backtrader-framework\|Backtrader]], Zipline/Alpaca |

---

## Execution Model

**Important caveat:** Backtesting.py fills orders at the **close of the bar that generated the signal**. If your `next()` method sees bar N's close price and issues a buy, that buy fills at bar N's close — the very price that was used to make the decision. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

This is more optimistic than reality. In live trading, you cannot trade at the price you used to generate the signal — by the time your order reaches the exchange, the price has moved. Compare with [[backtrader-framework|Backtrader]], which defaults to filling at the **next bar's open** (more conservative and realistic).

See [[execution-model-differences]] for a detailed comparison of how different frameworks handle fill assumptions and why this matters.

**Mitigation:** Set `trade_on_close=False` in the `Backtest` constructor to force fill-at-next-open behavior, or add a conservative slippage/commission assumption to compensate.

---

## Limitations

| Limitation | Impact | Workaround |
|-----------|--------|------------|
| **Single-asset only** | Cannot test portfolio-level strategies, no correlation/hedging | Use [[vectorbt]] or [[backtrader-framework|Backtrader]] for multi-asset |
| **Grid optimizer** | Brute-force; slow for large parameter spaces | Use [[optuna]] wrapper |
| **No native ML integration** | Cannot train models inside the backtest loop | Use [[pybroker]] for ML strategies |
| **Fill-at-close default** | Potential [[lookahead-bias|look-ahead bias]] | Set `trade_on_close=False` |
| **No live trading** | Research/backtest only | Deploy via separate framework |
| **Limited order types** | Market orders only; no limit/stop-limit | Use Backtrader or custom solution for complex order logic |

---

## When to Use Backtesting.py

**Good for:**
- Quick prototyping of single-asset strategies
- Visual trade review with interactive charts
- Educational purposes — easiest framework to learn
- Strategies with 1-2 parameters to optimize

**Not good for:**
- Portfolio-level backtesting (multi-asset, rebalancing)
- ML-driven strategies (use [[pybroker]])
- Large-scale parameter optimization (use [[vectorbt]] + [[optuna]])
- Production deployment / live trading

---

## Caveats and Gotchas

- **AGPL-3.0 license.** Embedding Backtesting.py in a closed-source commercial product can trigger copyleft obligations. Check before shipping.
- **Same-bar fill is the default.** As detailed in [[#Execution Model|Execution Model]], the default optimistic fill inflates results; set `trade_on_close=False` and add realistic [[execution-model-differences|slippage/commission assumptions]].
- **Grid optimizer overfits silently.** Maximizing Sharpe over a dense grid is a multiple-testing exercise; a high in-sample Sharpe says little without [[walk-forward-analysis|walk-forward]] confirmation and a [[deflated-sharpe-ratio|deflated-Sharpe]] sanity check. See [[backtesting-pitfalls]].
- **Single-asset framing hides portfolio risk.** A strategy that looks great on one ticker may be uncorrelated-but-fragile across a book; Backtesting.py cannot surface that.

---

## Related

- [[backtrader-framework]] — event-driven alternative with next-bar-open fills and live trading
- [[vectorbt]] — vectorized engine for fast multi-asset sweeps
- [[pybroker]] — ML-first framework with built-in leak protection
- [[optuna]] — smarter optimizer to wrap around the grid search
- [[event-driven-backtesting]] — the engine paradigm Backtesting.py implements
- [[execution-model-differences]] — why fill assumptions change results
- [[lookahead-bias]] — the bias the windowed `self.data` mostly prevents
- [[backtesting-pitfalls]] / [[backtesting]] — broader backtest hygiene
- [[walk-forward-analysis]] — validation step after prototyping here

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- Backtesting.py documentation: https://kernc.github.io/backtesting.py/
