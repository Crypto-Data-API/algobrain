---
title: "AI & Algorithmic Backtesting — Overview"
type: index
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [backtesting, ai-trading, index]
aliases: ["Backtesting Overview", "Backtest Methodology"]
related: ["[[backtesting-pitfalls]]", "[[walk-forward-optimization]]", "[[overfitting-in-trading]]", "[[deflated-sharpe-ratio]]", "[[regime-matrix]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Backtesting

Strategy backtesting methodology, frameworks, and best practices.

Backtesting is how traders simulate a strategy against historical data before risking real capital. Done well, it builds justified confidence; done poorly, it produces dangerously misleading results. This section covers the frameworks (Backtrader, Zipline, QuantConnect), the methodology ([[walk-forward-optimization]], out-of-sample testing), and the pitfalls ([[look-ahead-bias]], [[survivorship-bias]], [[overfitting-in-trading|overfitting]]) that separate rigorous research from curve-fitting.

A reliable backtest is the foundation of every systematic strategy. Before you deploy anything live, make sure you understand what can go wrong.

## Start Here

- [[backtesting-pitfalls]] -- The most common mistakes and how to avoid them
- [[walk-forward-optimization]] -- Rolling-window validation for robust parameter tuning
- [[backtrader-framework]] -- Python-based backtesting with flexible data feeds

## Types of Backtesting

### Vectorized Backtesting

Processes the entire price history at once using array operations (NumPy/pandas):

- **Speed**: Extremely fast -- suitable for scanning thousands of parameter combinations
- **Implementation**: Simple; strategy logic expressed as boolean masks on DataFrames
- **Limitations**: Cannot model order-dependent logic (e.g., partial fills, order queues), position sizing that depends on fill prices, or complex execution dynamics
- **Tools**: [[vectorbt]], pandas, NumPy
- **Best for**: Initial screening, parameter sweeps, simple strategies (moving average crossovers, mean-reversion signals)

```python
# Vectorized backtest example (simplified)
import pandas as pd

signals = (prices.rolling(50).mean() > prices.rolling(200).mean()).astype(int)
returns = prices.pct_change() * signals.shift(1)  # shift to avoid look-ahead
sharpe = returns.mean() / returns.std() * (252 ** 0.5)
```

### Event-Driven Backtesting

Processes each bar (or tick) sequentially, simulating the real-time decision process:

- **Accuracy**: Can model realistic execution: slippage, partial fills, order book dynamics, margin calls
- **Complexity**: Requires more code and runs slower than vectorized approaches
- **Tools**: [[backtrader-framework|Backtrader]], [[quantconnect]], Zipline
- **Best for**: Strategies with complex execution logic, position management, portfolio-level risk controls

Event-driven backtesting is essential for strategies where execution quality significantly impacts returns (e.g., high-frequency, market making, strategies with tight stop losses).

### Walk-Forward Backtesting

A validation methodology that tests strategy robustness:

1. **In-sample period**: Optimize parameters on a training window (e.g., 2 years)
2. **Out-of-sample period**: Test optimized parameters on the next unseen window (e.g., 6 months)
3. **Roll forward**: Move the windows forward and repeat
4. **Aggregate**: Combine all out-of-sample periods to get the "true" performance estimate

See [[walk-forward-optimization]] for detailed methodology.

### Choosing a Backtest Type

The three types are not competitors — they are stages. Use the cheapest tool that answers the current question:

| Question you are asking | Use | Why |
|---|---|---|
| "Does this idea have *any* signal?" | Vectorized | Fast parameter sweeps; cheap to falsify a dead idea early |
| "Does it survive realistic execution?" | Event-driven | Models slippage, partial fills, stops, margin |
| "Will the parameters hold out-of-sample?" | Walk-forward | The only honest estimate of forward performance |
| "Is the Sharpe real or a multiple-testing artifact?" | Walk-forward + [[deflated-sharpe-ratio]] | Corrects for the number of variations tried |
| "Does it work in this market structure?" (perps, options) | Event-driven, asset-specific | Funding, ADL, assignment, borrow are not capturable in vectorized form |

A common and costly mistake is to optimize parameters in a vectorized sweep and then report that in-sample Sharpe as if it were the strategy's edge. The vectorized sweep is for *screening*; the walk-forward run is for *belief*. See [[overfitting-in-trading]].

## Key Backtesting Metrics

### Return Metrics

| Metric | What It Measures | Good Threshold |
|--------|-----------------|----------------|
| CAGR | Compound annual growth rate | Depends on risk; 10-20% for moderate strategies |
| Total return | Cumulative return over the test period | Context-dependent |
| Annualized return | Average yearly return | Must exceed risk-free rate + risk premium |

### Risk-Adjusted Metrics

| Metric | Formula | Good Threshold |
|--------|---------|----------------|
| [[sharpe-ratio\|Sharpe ratio]] | (Return - Rf) / StdDev | > 1.0 (> 2.0 is strong) |
| [[sortino-ratio\|Sortino ratio]] | (Return - Rf) / Downside StdDev | > 1.5 |
| [[sharpe-sortino-calmar\|Calmar ratio]] | CAGR / Max Drawdown | > 0.5 |

### Risk Metrics

| Metric | What It Measures | Warning Level |
|--------|-----------------|---------------|
| [[maximum-drawdown\|Max drawdown]] | Largest peak-to-trough decline | Strategy-dependent; > 30% is concerning |
| [[drawdown\|Drawdown duration]] | Longest time underwater | > 1 year is concerning for most strategies |
| [[volatility\|Annual volatility]] | Standard deviation of returns annualized | Strategy-dependent |
| [[value-at-risk\|VaR (95%)]] | Maximum expected daily loss at 95% confidence | Strategy-dependent |

### Trade-Level Metrics

| Metric | What It Measures | Healthy Range |
|--------|-----------------|---------------|
| Win rate | % of trades that are profitable | 30-70% depending on payoff ratio |
| Profit factor | Gross profit / Gross loss | > 1.5 |
| Average win / Average loss | Payoff ratio | > 1.5 for low-win-rate strategies |
| Average trade duration | Time in each position | Strategy-dependent |
| Number of trades | Statistical significance | > 100 for confidence; > 500 preferred |

### Advanced Validation Metrics

| Metric | Purpose |
|--------|---------|
| [[deflated-sharpe-ratio\|Deflated Sharpe ratio]] | Adjusts Sharpe for multiple testing (number of strategies tried) |
| [[probabilistic-sharpe-ratio\|Probabilistic Sharpe ratio]] | Probability that the true Sharpe exceeds a threshold |
| Information ratio | Active return vs tracking error relative to a benchmark |
| Stability of returns | R-squared of the cumulative return curve vs a straight line |

## Overfitting: The Central Danger

[[overfitting-in-trading|Overfitting]] is the single greatest threat to backtested strategies. An overfitted strategy has learned the noise in historical data rather than genuine patterns, producing excellent backtest results but poor live performance.

### How Overfitting Happens

1. **Too many parameters**: A strategy with 10+ tunable parameters can fit almost any historical data
2. **Data snooping**: Testing many variations and only reporting the best one (see [[deflated-sharpe-ratio]])
3. **Small sample size**: Not enough trades for statistical significance
4. **Optimization without validation**: Tuning parameters on the same data used for testing
5. **Survivorship bias**: Only testing on assets that still exist today (winners)

### Detecting Overfitting

- **In-sample vs out-of-sample gap**: If IS Sharpe is 3.0 but OOS Sharpe is 0.5, the strategy is overfitted
- **Parameter sensitivity**: If small parameter changes dramatically affect results, the strategy is fragile
- **Degradation across time**: If performance is concentrated in a few periods, it may be curve-fit to those periods
- **Number of parameters vs trades**: Rule of thumb -- need at least 50-100 trades per free parameter
- **[[deflated-sharpe-ratio]]**: Accounts for the number of strategies tested; a Sharpe of 2.0 means nothing if you tested 1,000 variations

See [[overfitting-in-trading]] and [[overfitting-detection]] for comprehensive guides.

### Preventing Overfitting

1. **Walk-forward validation**: Never optimize and test on the same data
2. **Keep strategies simple**: Fewer parameters = harder to overfit
3. **Use [[deflated-sharpe-ratio]]**: Account for multiple testing
4. **Paper trade before live**: Validate on real-time data before committing capital
5. **Economic rationale**: Every strategy should have a reason to work beyond "the numbers look good"

## Common Backtesting Pitfalls

### Survivorship Bias

Only testing on assets that still exist today excludes all the stocks/tokens that went to zero:

- Results are biased upward because you never see the losers
- Especially dangerous for crypto (thousands of dead coins) and small-cap stocks
- Solution: Use point-in-time datasets that include delisted assets
- See [[survivorship-bias]]

### Look-Ahead Bias

Using information that would not have been available at the time of the trade:

- Using end-of-day data for intraday decisions
- Using revised economic data (GDP revisions, restated earnings) instead of the original release
- Calculating indicators using future data points
- Solution: Strictly use point-in-time data; shift signals by at least one bar
- See [[look-ahead-bias]]

### Data Snooping

Testing many hypotheses on the same dataset and selecting the best:

- If you test 100 strategies and pick the best one, the "best" is likely to be overfitted
- The more strategies tested, the higher the bar for statistical significance
- Solution: Use [[deflated-sharpe-ratio]], pre-register hypotheses, use holdout data
- Related: [[signal-vs-noise]]

### Ignoring Transaction Costs

Backtests that do not model realistic costs produce fantasy results:

- **Commissions**: Per-trade fees (less relevant with commission-free brokers, but still exist for futures/options)
- **[[slippage]]**: Difference between expected and actual fill price; critical for strategies that trade frequently
- **[[market-impact]]**: Large orders moving the price against you; scales with position size
- **Spread costs**: The [[bid-ask-spread]] is a real cost on every round-trip trade
- **Financing/carry**: Costs of holding leveraged positions overnight

Rule of thumb: if a strategy does not survive 5-10 bps of round-trip costs, it probably is not real.

#### Cost Floors by Asset Class

The "5-10 bps" rule is a floor for liquid equities; other markets carry structurally different cost stacks that a backtest must model explicitly:

| Asset class | Dominant costs | Indicative round-trip floor | Backtest-specific trap |
|---|---|---|---|
| **Large-cap equities** | Spread + commission | ~3-10 bps | Assuming close-price fills |
| **Small-cap equities** | Spread + [[market-impact]] + borrow (shorts) | 20-50+ bps | [[survivorship-bias]] (delisted names) |
| **Crypto spot** | Taker fee + spread | ~10-20 bps | No point-in-time delisted-coin data |
| **Crypto perps** | Taker fee + [[funding-rate\|funding]] + slippage | ~20-40 bps + funding | Funding-regime-dependent carry; ADL not modeled (see [[crypto-perp-backtesting-pitfalls]]) |
| **Options** | Spread (wide) + assignment + slippage | 50-200+ bps | Stale-quote / mid-fill assumption; vol-surface look-ahead |
| **Futures** | Commission + spread + roll | ~2-8 bps + roll | Continuous-contract construction artifacts |

A backtest that uses one flat cost number across asset classes is misleading. The funding term on a perp strategy, the borrow term on an equity short, and the roll cost on a futures strategy each behave like a *regime-dependent* expense that benign historical windows understate — this is exactly the failure the [[session-overlap-momentum]] and white-collar-ai-displacement-short pages flag in their cost overlays.

### Other Pitfalls

- **Short-sale constraints**: Backtests assume you can always short; in reality, shares may be unavailable or expensive to borrow
- **Fill assumptions**: Assuming market orders fill at the close price; in reality, execution varies
- **Regime dependence**: A strategy that worked in a bull market may fail in a bear market
- **Insufficient trade count**: 30 trades is not statistically significant; aim for 100+

See [[backtesting-pitfalls]] for the exhaustive list.

## Backtesting Tools

### Python Frameworks

| Framework | Type | Strengths | Weaknesses |
|-----------|------|-----------|------------|
| [[backtrader-framework\|Backtrader]] | Event-driven | Flexible, great docs, large community | Slower than vectorized, development slowed |
| [[quantconnect]] | Event-driven | Cloud-based, institutional data, live deployment | Learning curve, proprietary API |
| Zipline | Event-driven | Clean API, originally by Quantopian | Limited maintenance since Quantopian shut down |
| [[vectorbt]] | Vectorized | Extremely fast, pandas-based | Limited execution modeling |
| bt | Vectorized | Portfolio-level testing, flexible | Less community support |

See [[backtrader-vs-zipline-vs-quantconnect]] for a detailed comparison.

### Cost Modeling

Every serious backtest must include realistic cost modeling:

1. **Commission model**: Fixed per trade, per share, or percentage
2. **Slippage model**: Fixed (e.g., 1 tick), percentage, or volume-based
3. **Market impact model**: Linear or square-root impact based on order size relative to ADV
4. **Spread model**: Half-spread cost on entry and exit
5. **Financing cost**: For leveraged or short positions

```python
# Simple cost model example
commission_per_trade = 1.00  # $1 per trade
slippage_bps = 5  # 5 basis points per side
spread_bps = 3  # average half-spread

total_cost_bps = slippage_bps + spread_bps  # per side
round_trip_cost_bps = total_cost_bps * 2  # 16 bps round trip
```

### From Backtest to Live

The progression from backtest to deployment:

1. **Backtest (in-sample)**: Develop and optimize on historical data
2. **Walk-forward validation**: Test robustness with rolling windows
3. **Out-of-sample test**: Final validation on held-out data
4. **Paper trading**: Live market data, simulated execution -- validates data pipeline and execution logic
5. **Pilot (small capital)**: Real money, small allocation -- validates fill quality and real-world costs
6. **Scale up**: Gradually increase allocation if pilot results confirm backtest expectations
7. **Monitor and review**: Ongoing comparison of live performance vs backtest expectations (see [[when-to-retire-a-strategy]])

### The Rigor Ladder

The `backtest_status` field used on every strategy page in this wiki encodes how far a strategy has climbed this ladder. Reading a strategy's status tells you how much to trust its numbers:

| `backtest_status` | What has been demonstrated | Trust level |
|---|---|---|
| `untested` | Idea only; numbers are priors, not evidence | None — treat figures as hypotheses |
| `naive-backtested` | In-sample fit, no cost model | Low — likely overfit |
| `walk-forward-validated` | Out-of-sample robustness shown | Moderate |
| `cost-corrected` | Realistic costs applied (per asset class above) | Moderate-high |
| `deflated-sharpe-significant` | Survives [[deflated-sharpe-ratio]] multiple-testing correction | High (statistical) |
| `paper-traded` → `pilot` → `live` | Real data / real money confirms the edge | Highest |

Most strategy pages in this wiki sit at `untested` deliberately — the honest label until a version-pinned, cost-corrected, out-of-sample run clears the strategy's stated null hypothesis. Do not confuse a well-argued economic rationale with a validated backtest.

## Regime Robustness in Backtests

A backtest that aggregates a full history into one Sharpe number hides the single most important question: **does the edge depend on a regime that may not recur?** Per the [[regime-matrix]], every strategy has regimes where it thrives and regimes where it dies; a backtest dominated by the favorable regime will look excellent and fail on deployment into a different one.

Practical regime-aware backtesting:

| Technique | What it reveals |
|---|---|
| **Sub-period decomposition** | Split returns by bull/bear/chop/high-vol; an edge concentrated in one regime is fragile |
| **Regime-conditional Sharpe** | Compute Sharpe within each [[market-regime]] separately, not just overall |
| **Crisis stress windows** | Re-run over 2008, 2020, 2018 [[volmageddon]], Aug-2024 spike — short-vol-like strategies that look great overall often collapse here |
| **Drawdown attribution** | Identify which regime contributes most of the lifetime drawdown (often a single transition) |
| **Funding/borrow regime split** (perps/shorts) | Re-run separately in positive- vs negative-carry regimes |

The deepest version of this critique is the [[long-vol-vs-short-vol]] insight: a [[short-volatility-strategies\|short-vol-like]] strategy backtested over a calm decade will show a 2+ Sharpe that tells you nothing about the next vol spike. Always know whether your backtested edge is implicitly long or short volatility, and stress it against the regime that punishes that posture. This is why a strong economic rationale and an explicit null hypothesis matter more than a high in-sample Sharpe.

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/ai-trading/backtesting"
WHERE type != "index"
SORT updated DESC
```

## Comparisons

- [[backtrader-vs-zipline-vs-quantconnect]] -- Comparing the three major Python backtesting frameworks
- [[python-vs-r-for-trading]] -- Choosing between Python and R for quantitative trading

## Getting the Data (CryptoDataAPI)

**Historical archive:**
- `GET /api/v1/backtesting/klines` — OHLCV candle archive
- `GET /api/v1/backtesting/funding` — funding-rate archive
- `GET /api/v1/backtesting/liquidations` — liquidation records archive
- `GET /api/v1/backtesting/daily-snapshots/{date}` — point-in-time daily snapshot
- `GET /api/v1/backtesting/archives` — Parquet dataset archive (since 2020)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/backtesting/symbols"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-backtesting]].

## Related

- [[backtesting-pitfalls]] -- Comprehensive guide to what can go wrong
- [[walk-forward-optimization]] -- Rolling validation methodology
- [[overfitting-in-trading]] -- The central danger of backtesting
- [[overfitting-detection]] -- Tools and techniques for detecting overfitting
- [[deflated-sharpe-ratio]] -- Adjusting Sharpe for multiple testing
- [[sharpe-ratio]] -- The most common risk-adjusted return metric
- [[ml-trading-pipeline]] -- End-to-end ML trading workflow
- [[ai-trading-overview]] -- Parent section: AI and trading technology
- [[regime-matrix]] -- Regime-aware view of where each strategy works
- [[market-regime]] -- The conceptual frame for regime-conditional backtesting
- [[long-vol-vs-short-vol]] -- Why you must know if your backtested edge is long or short vol
- [[when-to-retire-a-strategy]] -- Live monitoring and kill-criteria methodology
- [[crypto-perp-backtesting-pitfalls]] -- Funding, ADL, and perp-specific backtest traps
- [[ai-agent-strategies]] -- LLM-specific backtest contamination (look-ahead via training data)
