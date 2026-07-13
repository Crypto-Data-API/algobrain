---
title: "Sharpe Ratio"
type: concept
created: 2026-04-07
updated: 2026-06-22
status: excellent
tags: [quantitative, risk-management, portfolio-theory]
aliases: ["Sharpe", "Risk-Adjusted Return", "Sharp Ratio", "sharp-ratio"]
domain: [risk-management, portfolio-theory]
prerequisites: ["[[standard-deviation]]", "[[expected-return]]"]
difficulty: intermediate
related: ["[[modern-portfolio-theory]]", "[[sortino-ratio]]", "[[risk-management]]", "[[alpha]]", "[[beta]]"]
---

The Sharpe Ratio is the most widely used metric for measuring [[risk-management|risk-adjusted]] return. Developed by Nobel laureate William Sharpe in 1966, it quantifies how much excess return an investor receives per unit of risk (volatility) taken.

## Formula

**Sharpe Ratio = (R_p - R_f) / sigma_p**

Where:
- **R_p** = Portfolio return
- **R_f** = Risk-free rate (typically the [[treasury-bonds|US Treasury]] yield)
- **sigma_p** = Standard deviation of portfolio returns

The numerator captures how much the portfolio outperforms the risk-free rate; the denominator penalizes for the volatility required to achieve that outperformance. Conceptually, the Sharpe Ratio is the slope of the line from the risk-free asset to the portfolio in [[mean-variance-optimization|mean-variance]] space — and the portfolio with the maximum Sharpe Ratio is precisely the tangency portfolio on the [[efficient-frontier|efficient frontier]] (see [[capital-market-line]]).

### Ex-ante vs ex-post

- **Ex-ante (expected)** Sharpe uses *expected* return and *forecast* volatility — used for portfolio optimization and capital allocation.
- **Ex-post (realized)** Sharpe uses *historical* mean excess return divided by *realized* [[standard-deviation]] — used for performance evaluation and [[backtesting]]. Most reported figures are ex-post.

## Annualization

Sharpe Ratios are nearly always quoted on an **annualized** basis so that strategies measured at different frequencies are comparable. To convert a per-period Sharpe to annual, multiply by the square root of the number of periods per year (the "square-root-of-time" rule, which assumes returns are independent and identically distributed):

**Sharpe_annual = Sharpe_period × √N**

| Sampling frequency | Periods/year (N) | Multiplier (√N) |
|---|---|---|
| Daily (trading days) | 252 | ~15.87 |
| Weekly | 52 | ~7.21 |
| Monthly | 12 | ~3.46 |
| Quarterly | 4 | 2.0 |

So a strategy with a daily Sharpe of 0.10 annualizes to roughly 0.10 × 15.87 ≈ **1.59**. The √N scaling breaks down when returns are autocorrelated (trend-following or illiquid assets inflate the annualized figure) or [[mean-reversion|mean-reverting]] (which deflates it). Returns must also be in *excess* of the risk-free rate at the same frequency.

## Worked Example

A long/short equity strategy returns **12%** over a year while the risk-free rate is **4%**, with realized annual volatility of **10%**:

> Sharpe = (0.12 − 0.04) / 0.10 = 0.08 / 0.10 = **0.80**

Now compare two managers, both earning 12% gross:

| Manager | Return R_p | Risk-free R_f | Volatility σ_p | Sharpe |
|---|---|---|---|---|
| A (steady) | 12% | 4% | 8% | (0.12−0.04)/0.08 = **1.00** |
| B (volatile) | 12% | 4% | 20% | (0.12−0.04)/0.20 = **0.40** |

Manager A earns the *same* return with far less risk and is the better risk-adjusted performer — exactly the comparison the Sharpe Ratio is built to surface. Raw return alone would rank them as equals.

## Interpretation

| Sharpe Ratio | Interpretation |
|---|---|
| < 0 | Strategy loses money relative to the risk-free rate |
| 0 - 1.0 | Suboptimal risk-adjusted returns |
| 1.0 - 2.0 | Good — acceptable for most institutional strategies |
| 2.0 - 3.0 | Excellent — typical of strong [[quantitative-strategies|quantitative strategies]] |
| > 3.0 | Exceptional — rare, may indicate overfitting or short track record |

Most [[hedge-funds|hedge funds]] target a Sharpe Ratio above 1.0. [[renaissance-technologies|Renaissance Technologies']] Medallion Fund reportedly achieved Sharpe Ratios above 6.0, though such figures are extraordinary and not replicable by most managers.

## Usage in Practice

- **Comparing strategies across asset classes**: A Sharpe of 1.5 in [[bonds-overview|bonds]] is directly comparable to a Sharpe of 1.5 in [[crypto-overview|crypto]], even though absolute returns and volatility differ dramatically.
- **Portfolio optimization**: [[modern-portfolio-theory|Modern Portfolio Theory]] uses the Sharpe Ratio to identify the tangent portfolio on the [[efficient-frontier|efficient frontier]] -- the portfolio with the highest Sharpe Ratio.
- **Backtesting evaluation**: When [[backtesting]] a strategy, the Sharpe Ratio is typically the primary metric reported alongside total return and [[maximum-drawdown|maximum drawdown]].
- **Capital allocation / risk budgeting**: Allocators size positions and sleeves roughly in proportion to expected Sharpe, since a higher-Sharpe sleeve contributes more return per unit of risk to the book. This underpins [[risk-parity]] and Kelly-style sizing.
- **Manager due diligence**: Institutional allocators screen out managers below a Sharpe threshold (often ~1.0 net of fees) and treat suspiciously high Sharpes as a red flag for hidden [[tail-risk]] or short, lucky track records.

## How Allocators and Traders Use It

- **Quant funds** treat ex-ante Sharpe as the objective to maximize in [[portfolio-construction]] — the [[fundamental-law-of-active-management|Fundamental Law of Active Management]] frames the achievable [[information-ratio]] (a benchmark-relative cousin of Sharpe) as IC × √Breadth.
- **Combining strategies**: Two uncorrelated strategies each with Sharpe 1.0 combine to a portfolio Sharpe of ~1.41 (√2). Low [[correlation]] is the lever that lets [[diversification]] raise the *aggregate* Sharpe above any single component — the mathematical case for running many independent bets.
- **Position sizing**: A higher-Sharpe edge justifies a larger fraction of the [[kelly-criterion|Kelly]] bet; allocators rarely bet full Kelly, using a fraction to control drawdown.

## Limitations

1. **Assumes normal distribution**: Real market returns exhibit [[fat-tails|fat tails]] and [[skewness]], meaning the standard deviation underestimates true risk.
2. **Penalizes upside volatility equally**: A strategy that occasionally produces large gains is penalized the same as one with large losses. The [[sortino-ratio|Sortino Ratio]] addresses this by using only downside deviation.
3. **Time-period sensitive**: Annualized Sharpe Ratios can vary significantly depending on the measurement period. A strategy may have a Sharpe of 2.0 over one year and 0.8 over five years.
4. **Risk-free rate dependency**: The choice of risk-free rate affects the calculation, especially in different currency regimes.
5. **Can be gamed**: Strategies that sell [[options-overview|options]] (collecting small premiums with occasional large losses) can produce artificially high Sharpe Ratios until a [[tail-risk|tail event]] occurs. Smoothing/illiquidity (private credit, real estate) understates measured volatility and inflates Sharpe — see [[liquidity]].
6. **Backtest overfitting**: A reported Sharpe from a search over many strategies is biased upward. The **Deflated Sharpe Ratio** (Bailey & López de Prado) adjusts the threshold for the number of trials tested — a key tool in [[overfitting-detection]].

## Variants and Related Ratios

| Ratio | Numerator | Denominator (risk measure) | Best used for |
|---|---|---|---|
| **Sharpe** | Excess return over R_f | Total [[standard-deviation]] | General risk-adjusted return |
| **[[sortino-ratio\|Sortino]]** | Excess return over R_f (or MAR) | Downside deviation only | Asymmetric / skewed return profiles |
| **[[information-ratio\|Information Ratio]]** | Return over a *benchmark* | Tracking error (active risk) | Active managers vs an index |
| **Calmar / MAR** | Annualized return | [[maximum-drawdown\|Max drawdown]] | Trend-followers, CTAs, drawdown sensitivity |
| **Treynor** | Excess return over R_f | [[beta]] (systematic risk) | Well-diversified portfolios |
| **Deflated Sharpe** | Observed Sharpe | Adjusted for # of trials | [[overfitting-detection\|Overfitting]] correction |

The key contrasts: the **[[sortino-ratio|Sortino Ratio]]** fixes the Sharpe's symmetric-volatility flaw by penalizing only downside deviation; the **[[information-ratio|Information Ratio]]** replaces the risk-free rate with a *benchmark* and uses tracking error, making it the standard yardstick for [[active-management|active]] managers measured against an index like the [[sp500|S&P 500]]. The **Calmar Ratio** swaps volatility for [[maximum-drawdown|max drawdown]], which many CTAs and [[trend-following|trend-followers]] prefer because drawdown is what actually triggers redemptions.

## Sources

- (Source: [[book-quantitative-trading-ernest-chan]]) -- Chan emphasizes Sharpe Ratio as the primary metric for evaluating quantitative strategies, noting that institutional capital typically requires Sharpe > 2.0
- (Source: [[book-inside-the-black-box]]) -- Narang discusses how quant funds use Sharpe Ratios in strategy selection and risk allocation
