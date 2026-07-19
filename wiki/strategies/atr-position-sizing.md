---
title: "ATR Position Sizing"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [risk-management, technical-analysis, position-trading, volatility]
aliases: ["ATR Position Sizing", "Volatility-Based Position Sizing", "Volatility Normalization", "ATR-Based Sizing"]
related: ["[[average-true-range]]", "[[atr-trailing-stop]]", "[[kelly-criterion]]", "[[risk-of-ruin]]", "[[stop-loss]]", "[[trend-following-cta]]", "[[position-sizing]]"]
strategy_type: technical
timeframe: swing
markets: [stocks, futures, forex, crypto]
complexity: intermediate
backtest_status: walk-forward-validated
edge_source: [risk-bearing]
edge_mechanism: "Not a return-generating edge by itself — it is a risk-normalization overlay. By equalizing dollar risk per trade across instruments of different volatility, it prevents a handful of high-volatility positions from dominating portfolio P&L and improves the geometric (compounded) growth rate of any underlying signal."
data_required: [ohlcv-daily]
min_capital_usd: 10000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: 0.0
expected_max_drawdown: 0.0
breakeven_cost_bps: 0
---

ATR position sizing is a risk-management overlay that sets position size so that a fixed fraction of account equity is at risk on each trade, using the [[average-true-range|Average True Range (ATR)]] as the measure of expected per-unit price movement. Instead of buying a round number of shares or a fixed dollar amount, the trader sizes each position inversely to the instrument's volatility, so a low-volatility name and a high-volatility name carry the same dollar risk. It is the sizing backbone of most systematic [[trend-following-cta|trend-following]] and [[managed-futures]] programs and was popularized for retail traders by the Turtle Traders' "unit" sizing scheme.

## Edge source

This is a **risk-bearing / risk-management** technique from the [[edge-taxonomy]], not a standalone return edge. ATR position sizing produces no expected return on its own — applied to a coin-flip signal it still loses to costs. Its contribution is to the *shape* of the equity curve: by normalizing volatility, it raises the geometric growth rate (see [[kelly-criterion]]) and lowers the probability of catastrophic drawdown ([[risk-of-ruin]]) relative to naive fixed-share or fixed-notional sizing.

## Why this edge exists

Different instruments move by wildly different dollar amounts for the same percentage move, and even a single instrument's volatility regime shifts over time. If you allocate a fixed dollar notional to every position, your portfolio P&L becomes dominated by whichever holdings happen to be most volatile, concentrating risk you never chose to take. By contrast, sizing inversely to ATR keeps the *risk contribution* of each position roughly equal. The mechanism that makes this valuable is the gap between arithmetic and geometric returns: large drawdowns hurt compounded wealth disproportionately (a 50% loss requires a 100% gain to recover), so smoothing per-trade risk improves long-run compounding even when it does not change the average trade. The "other side" is the undisciplined trader whose oversized volatile positions blow up the account in a bad streak.

## Null hypothesis

Under the null, ATR sizing should produce the *same expected per-trade return* as any other sizing method applied to the same signal — because sizing does not create alpha. The testable claim is narrower: that ATR sizing delivers a **higher risk-adjusted return (Sharpe)** and **lower maximum drawdown** than fixed-notional or fixed-share sizing on the same signal, across instruments and regimes. If a backtest shows ATR sizing producing equal or worse drawdown and Sharpe than naive sizing on a diversified universe, the supposed benefit is absent and you are merely adding complexity.

## Rules

- **Risk budget**: decide the fraction of equity to risk per trade, typically 0.5%–2% (the Turtles used ~1% per "unit").
- **Volatility input**: compute ATR over a lookback (commonly 14 or 20 periods) using [[wilders-smoothing|Wilder's smoothing]].
- **Stop distance**: define the stop as a multiple of ATR (e.g., 2x ATR below entry for a long).
- **Position size formula**: `size = (equity × risk_fraction) / (ATR_multiple × ATR)`.
- **Entry/exit**: the underlying signal (breakout, trend filter, etc.) dictates *when* to trade; ATR sizing only dictates *how much*. Exit on the ATR-based stop (see [[atr-trailing-stop]]) or the signal's own exit.
- **Re-sizing**: recompute size at each new entry using current equity and current ATR; do not pyramid beyond the volatility budget.
- **Caps**: cap total exposure per instrument and per correlated cluster so that correlated positions do not stack into a single large bet.

## Implementation pseudocode

```python
def atr_position_size(equity, risk_fraction, atr, atr_stop_mult,
                      price, max_position_frac=0.20):
    # dollars willing to lose if stop is hit
    dollar_risk = equity * risk_fraction          # e.g. 100_000 * 0.01 = 1_000
    # dollars lost per unit if price moves to the stop
    risk_per_unit = atr_stop_mult * atr           # e.g. 2 * 3.50 = 7.00
    if risk_per_unit <= 0:
        return 0
    units = dollar_risk / risk_per_unit           # 1000 / 7 = 142 shares
    # cap notional exposure to avoid over-concentration in low-vol names
    max_units = (equity * max_position_frac) / price
    return int(min(units, max_units))

# correlation cap: sum risk across a correlated cluster, scale down if > budget
```

## Indicators / data used

- [[average-true-range|ATR]] (14- or 20-period, Wilder-smoothed) — the volatility input
- Daily (or intraday) OHLCV for the traded universe
- Account equity (recomputed each entry)
- Optional: a correlation matrix for cluster-level risk caps

## Example trade

Account equity $100,000, risk fraction 1% ($1,000 per trade), ATR stop multiple 2x. Stock A trades at $50 with a 14-day ATR of $1.00; Stock B trades at $50 with an ATR of $4.00. For A, risk-per-unit = 2 × $1.00 = $2.00, so size = $1,000 / $2.00 = 500 shares ($25,000 notional). For B, risk-per-unit = 2 × $4.00 = $8.00, so size = $1,000 / $8.00 = 125 shares ($6,250 notional). Despite identical price and identical $1,000 risk budget, the volatile stock gets a quarter of the notional — exactly the normalization the method is designed to deliver. If either stop is hit, the loss is ~$1,000 on each.

## Performance characteristics

ATR sizing does not have a standalone return profile; it modifies whatever signal it overlays. Empirically, on diversified trend-following universes, swapping fixed-notional for ATR (volatility-target) sizing typically (a) reduces realized portfolio volatility clustering, (b) cuts maximum drawdown by a meaningful margin, and (c) raises Sharpe modestly — at the cost of more frequent rebalancing turnover. Because volatility is persistent and forecastable while returns are not, the volatility-normalization benefit is one of the more robust findings in the systematic-trading literature. Costs are limited to the incremental turnover from re-sizing as ATR drifts.

## Capacity limits

Capacity is governed by the underlying signal and the instrument universe, not by the sizing rule. The overlay itself scales to institutional size; volatility-target sizing is standard at multi-billion-dollar [[managed-futures]] funds. The only sizing-specific constraint is that very low-ATR instruments can produce large computed positions — the `max_position_frac` cap and liquidity/ADV limits must bind before market impact erodes the underlying edge.

## What kills this strategy

- **Bad ATR estimate during regime shifts**: ATR is backward-looking; a sudden volatility spike (gap, crash) means yesterday's ATR understated true risk and the position was too large. See [[failure-modes]].
- **Correlation blindness**: sizing each position independently while ignoring correlation lets many "1% risk" positions become one large correlated bet that loses simultaneously.
- **Stop slippage**: the method assumes the loss equals ATR_multiple × ATR; gaps through the stop make realized losses exceed the budget.
- **Over-leveraging low-vol names**: in quiet regimes ATR shrinks, the formula buys huge size, and a vol expansion then inflicts an outsized loss — the classic short-volatility trap.

## Kill criteria

- Realized per-trade loss repeatedly exceeds 2x the intended risk budget (indicates ATR is systematically understating risk → widen multiple or shorten lookback).
- Portfolio drawdown exceeds 1.5x the level implied by the per-trade risk budget and position count (indicates correlation stacking → tighten cluster caps).
- Rolling 12-month Sharpe of the ATR-sized version falls below the fixed-notional baseline on the same signal (the overlay is adding cost without benefit → revert).

## Advantages

- Equalizes dollar risk across instruments of different volatility.
- Adapts automatically to changing volatility regimes (positions shrink as vol rises).
- Improves geometric growth and reduces drawdown vs. naive sizing.
- Simple, transparent, and broadly applicable across asset classes.

## Disadvantages

- Adds no return on its own; only useful with a real signal.
- Backward-looking — lags sudden volatility expansions.
- Ignores correlation unless explicitly extended with cluster caps.
- Can over-size in unusually quiet regimes, creating hidden short-volatility exposure.

## Getting the Data (CryptoDataAPI)

For crypto books, [[cryptodataapi|CryptoDataAPI]] supplies the OHLCV bars the ATR is computed from, plus a pre-built per-coin volatility/risk model that can replace or sanity-check hand-rolled sizing.

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100` — daily OHLCV per instrument for the 14/20-period Wilder ATR
- `GET /api/v1/quant/coins/risk` — bulk per-coin risk model with vol-target multipliers across 180+ coins (Pro): an API-side volatility-normalised sizing input
- `GET /api/v1/volatility/regime` — per-asset vol regime (`compressed` / `expanding` / `vol_shock`): flags the quiet-regime over-sizing trap before ATR reacts

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive (Binance spot 1h/4h/1d back to 2017-08; Hyperliquid daily to 2023) for ATR-sizing vs fixed-notional comparison backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=100"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Sizing input** — `GET /api/v1/market-data/klines` per instrument (daily bars → Wilder ATR → the size formula above), or skip the hand-rolled math and batch `GET /api/v1/quant/coins/risk` for vol-target multipliers across the whole universe in one call.
- **Regime gate** — `GET /api/v1/volatility/regime`: a `compressed` reading warns that ATR is understating true risk (the classic short-vol trap) — widen the stop multiple or cap size before the expansion arrives.
- **Correlation guard** — `GET /api/v1/coins/category-groups`: cluster the universe by theme so multiple "1% risk" positions in the same narrative do not stack into one correlated bet.
- **Backtest** — replay ATR sizing vs fixed-notional on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d since 2017-08); pair entries with point-in-time regime states from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) to avoid lookahead in any regime-conditional sizing rule.
- **Tips** — respect `insufficient_history`/`new_listing` flags before sizing a newly listed coin; recompute size at entries only, not every tick, to avoid churning the book as ATR drifts.
- **Prompt library** — the "Volatility-Aware Position Sizer" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) implements `risk_dollars / (1.5 × volatility) × vol_target_multiplier` off /api/v1/quant/coins/risk — the API-native sibling of ATR sizing

## Sources

- Curtis Faith, *Way of the Turtle* (2007) — the original Turtle "unit" / N-based (ATR) position-sizing rules.
- J. Welles Wilder, *New Concepts in Technical Trading Systems* (1978) — definition of ATR (see [[j-welles-wilder]]).
- Van K. Tharp, *Trade Your Way to Financial Freedom* — position sizing and the role of volatility in expectancy.

## Related

- [[average-true-range]]
- [[atr-trailing-stop]]
- [[kelly-criterion]]
- [[risk-of-ruin]]
- [[stop-loss]]
- [[trend-following-cta]]
- [[managed-futures]]
