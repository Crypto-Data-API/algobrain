---
title: "Execution Model Differences"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [backtesting, algorithmic]
aliases: ["Execution Model Differences", "Backtester Execution Models"]
domain: [backtesting]
difficulty: intermediate
prerequisites: ["[[event-driven-backtesting]]", "[[vectorized-backtesting]]"]
related:
  - "[[backtrader-framework]]"
  - "[[vectorbt]]"
  - "[[backtesting-py]]"
  - "[[event-driven-backtesting]]"
  - "[[vectorized-backtesting]]"
  - "[[slippage-modeling]]"
  - "[[slippage]]"
  - "[[transaction-cost-modeling]]"
  - "[[backtesting]]"
  - "[[backtesting-pitfalls]]"
  - "[[lookahead-bias]]"
---

# Execution Model Differences

Identical strategies produce different results across backtesting frameworks because each framework makes different assumptions about when and at what price orders are filled. These execution model differences can change annualized returns by 2-5% and turn a profitable strategy into a losing one (or vice versa). Understanding your framework's execution model is as important as understanding your strategy logic. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Fill-at-Close vs Fill-at-Next-Open

The single most impactful difference between frameworks.

### The Problem

Your strategy evaluates bar N's data and generates a buy signal. At what price does the buy order fill?

| Model | Fill Price | Assumption | Realistic? |
|-------|-----------|------------|------------|
| **Fill-at-close** | Bar N's close | You can trade at the price that generated the signal | **No** — you see the close, then need time to compute signal + submit order |
| **Fill-at-next-open** | Bar (N+1)'s open | You see bar N's close, trade at the next available price | **More realistic** — this is closer to how live trading works |
| **Fill-at-next-close** | Bar (N+1)'s close | Signal fires at close, order rests until next close | Conservative but too pessimistic for most strategies |

### Impact

On daily bars, the gap between close and next-day open averages 0.1-0.5% for liquid equities but can be 1-3% for volatile assets (crypto, small caps). Over hundreds of trades, this compounds:

- A strategy trading 200 times/year with a 0.3% average gap loses ~0.6% annually from fill-at-close optimism
- For a strategy with 5% annual return, that is 12% of the total return attributed to an unrealistic fill assumption

### Framework Defaults

| Framework | Default Fill Behavior |
|-----------|----------------------|
| [[backtrader-framework|Backtrader]] | **Next bar's open** (conservative, realistic) |
| [[backtesting-py|Backtesting.py]] | **Same bar's close** (optimistic — set `trade_on_close=False` to fix) |
| [[vectorbt|VectorBT]] | Depends on signal shifting — **user's responsibility** |
| [[zipline-framework|Zipline]] | **Next bar's open** (conservative, realistic) |
| [[quantconnect|QuantConnect]] | **Configurable** — fill models are pluggable |

---

## Bar Magnification

In [[event-driven-backtesting|event-driven backtests]], the order of operations **within a single bar** matters.

### The Problem

On a given daily bar: Open = $100, High = $105, Low = $95, Close = $102. You have a position with a stop-loss at $96 and a take-profit at $104. Both levels were hit during this bar. **Which triggered first?**

The honest answer: **you don't know.** With OHLC data, you cannot determine intraday sequencing.

### Framework Approaches

| Approach | Method | Effect |
|----------|--------|--------|
| **Pessimistic (stop first)** | If both SL and TP are hit, assume stop triggered first | Conservative — underestimates performance |
| **Optimistic (TP first)** | Assume take-profit triggered first | Overestimates performance |
| **OHLC order heuristic** | If Open is closer to High, assume High came first (up-then-down); otherwise down-then-up | Approximation — better than nothing |
| **Use higher-frequency data** | Drop to hourly or minute bars to resolve the ambiguity | Best solution but requires more data |

---

## Vectorized Look-Ahead Bias

[[vectorized-backtesting|Vectorized backtests]] process entire arrays at once. This creates a specific and common trap: forgetting to shift the signal array forward.

### The Bug

```python
# WRONG — look-ahead bias
signal = (fast_ma > slow_ma)  # Signal computed using bar N's close
entries = signal & ~signal.shift(1)  # Entry on crossover
pf = vbt.Portfolio.from_signals(close, entries, exits)  # Fills at bar N's close
```

The signal uses bar N's close, and the portfolio fills at bar N's close — the strategy is trading on information it could not have acted on in time.

### The Fix

```python
# CORRECT — signal shifted by one bar
signal = (fast_ma > slow_ma)
entries = (signal & ~signal.shift(1)).shift(1)  # Shift entries forward by 1 bar
pf = vbt.Portfolio.from_signals(close, entries, exits)
```

Now the entry fires on bar N+1, using bar N's signal. This is the vectorized equivalent of "fill at next bar."

This class of bug is **invisible in the backtest output** — the equity curve looks perfectly normal, just a bit too good. It is one of the most common sources of backtest-to-live discrepancy. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Slippage Application

How frameworks model the difference between your intended fill price and the actual fill price:

| Method | Description | Frameworks |
|--------|-------------|------------|
| **Fixed pip/point** | Add/subtract a fixed amount per trade | Backtrader (configurable) |
| **Fixed percentage** | Add/subtract X% of the fill price | VectorBT (default), Backtesting.py |
| **Volume-based** | Slippage increases with order size relative to bar volume | QuantConnect, custom models |
| **None (default)** | Many frameworks default to zero slippage | Most — **you must add it yourself** |

Zero slippage is unrealistic for all but the most liquid instruments at small sizes. For a realistic backtest:
- **Equities (liquid):** 1-5 bps round-trip
- **Equities (small cap):** 10-50 bps
- **Crypto (major pairs):** 5-15 bps
- **Crypto (altcoins):** 20-100+ bps
- **Futures:** 0.5-2 bps (very liquid) to 10+ bps (thin markets)

See [[slippage-modeling]] and [[transaction-cost-modeling]] for detailed treatment.

---

## Commission Models

Closely related to slippage — different frameworks model commissions differently:

- **Flat fee per trade:** $1 per trade regardless of size (e.g., Backtrader default)
- **Percentage of trade value:** 0.1% of notional (common for crypto exchanges)
- **Per-share fee:** $0.005/share (US equities broker model)
- **Tiered:** Different rates for different volume levels
- **Maker/taker:** Different fees for providing vs taking liquidity (crypto, futures)

Ensure your framework matches the fee structure of your target broker/exchange.

---

## Fill-Assumption Summary

Every backtester encodes a set of answers to "when and at what price does an order fill?" The five assumptions below, taken together, are the *execution model*. Getting any one wrong can flip a strategy's sign.

| Assumption | Optimistic (over-states returns) | Realistic / conservative | Why it matters |
|---|---|---|---|
| **Signal timing** | Fill at the same bar's close that generated the signal | Fill at next bar's open (one-bar lag) | The optimistic case trades on information not yet actionable — a soft [[lookahead-bias]] |
| **Intrabar sequencing** | Assume take-profit hit before stop (bar magnification) | Assume stop hit first, or use intrabar data | OHLC cannot resolve which level traded first |
| **Slippage** | Zero | Asset-appropriate bps round-trip (see [[slippage]]) | Zero slippage is unrealistic for all but the most liquid names |
| **Commission** | Zero or mismatched fee model | Match the target broker/exchange schedule | Compounds over high-turnover strategies |
| **Liquidity / fill size** | Unlimited fill at quoted price | Volume-capped, size-aware fills | Large orders move the market; assumes capacity that isn't there |

A backtest that is optimistic on *all five* can show a healthy equity curve for a strategy that loses money live. The discrepancy is the execution model, not the alpha. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

## Worked Example (illustrative)

Consider a daily-bar mean-reversion strategy that trades 200 round-trips per year and shows a naive backtest CAGR of 5%.

- **Fill-at-close optimism:** assuming a 0.3% average close-to-next-open gap, switching from fill-at-close to the realistic fill-at-next-open removes ~0.6% per year — about 12% of the headline return.
- **Slippage:** at a modest 3 bps round-trip on liquid equities (see [[slippage]]), 200 trades cost ~0.6% per year.
- **Commission:** a per-share or flat-fee model on 200 trades can subtract another few tenths of a percent.

Stacked, these realistic frictions can turn a 5% backtest into a ~3.5% live expectation — and a thinner-edged strategy into a negative one. None of the numbers above are measured results; they illustrate how ordinary, defensible execution assumptions consume a large fraction of a modest edge. The lesson is the lesson of [[backtesting-pitfalls]]: the execution model is part of the strategy.

---

## Practical Recommendations

1. **Know your framework's default fill model** — read the documentation specifically on order execution
2. **When in doubt, use fill-at-next-open** — more conservative and more realistic
3. **Always add slippage and commission** — even a small estimate is better than zero
4. **Validate with two frameworks** — if the same strategy logic produces very different results in Backtrader and VectorBT, the difference is the execution model, not the strategy
5. **Use higher-frequency data** to resolve bar magnification ambiguity when stop-loss and take-profit distances are tight
6. **In vectorized backtests, always `.shift(1)` your signal** unless you have explicitly confirmed that your framework handles the temporal offset

---

## Related

- [[backtesting]] — the parent discipline
- [[event-driven-backtesting]] — where bar-magnification ambiguity lives
- [[vectorized-backtesting]] — where the `.shift(1)` look-ahead trap lives
- [[backtesting-pitfalls]] — the broader catalog of ways backtests mislead
- [[lookahead-bias]] — the failure mode that fill-at-close and unshifted signals create
- [[slippage]] / [[slippage-modeling]] — modeling the intended-vs-actual fill gap
- [[transaction-cost-modeling]] — commissions, fees, and market impact
- [[backtrader-framework]] / [[vectorbt]] / [[backtesting-py]] — frameworks with differing execution defaults

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
