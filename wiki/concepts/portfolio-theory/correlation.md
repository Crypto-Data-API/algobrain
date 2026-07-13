---
title: "Correlation"
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [correlation, portfolio-theory, risk-management]
aliases: ["Correlation Coefficient", "Pearson Correlation"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[volatility]]", "[[diversification]]"]
difficulty: intermediate
related:
  - "[[diversification]]"
  - "[[position-sizing]]"
  - "[[volatility]]"
  - "[[modern-portfolio-theory]]"
  - "[[portfolio-construction]]"
  - "[[risk-parity]]"
  - "[[correlation-matrix]]"
  - "[[strategy-correlation-matrix]]"
  - "[[implied-correlation]]"
  - "[[covariance]]"
  - "[[derisking]]"
  - "[[efficient-frontier]]"
---

# Correlation

**Correlation** is a statistical measure (ranging from -1 to +1) that describes the degree to which two assets move in relation to each other. It is fundamental to [[diversification]], [[portfolio-construction]], and [[risk-management]] -- understanding correlation determines whether adding a new position actually reduces portfolio risk or merely concentrates it.

## Correlation Coefficient

The Pearson correlation coefficient (r) measures the linear relationship between two variables:

```
r = Cov(X, Y) / (StdDev(X) x StdDev(Y))
```

Where Cov(X,Y) is the [[covariance]] of returns, and StdDev is the standard deviation ([[volatility]]) of each asset.

### Interpreting the Scale

- **+1.0**: Perfect positive correlation. Assets move in lockstep in the same direction. Holding both provides zero diversification benefit.
- **+0.5 to +0.9**: Strong positive correlation. Common among assets in the same sector, market, or risk factor.
- **0.0**: No linear relationship. Movements are independent of each other. True zero correlation is rare in financial markets.
- **-0.5 to -0.9**: Strong negative correlation. Assets tend to move in opposite directions.
- **-1.0**: Perfect negative correlation. A perfect hedge -- when one goes up, the other goes down by a proportional amount.

### Example Calculations

If Stock A returns {+2%, -1%, +3%, -2%, +1%} and Stock B returns {+1.5%, -0.5%, +2%, -1%, +0.5%}, the correlation is approximately +0.99 (nearly perfectly correlated -- they move in the same direction by similar proportions).

## Why Correlation Drives Portfolio Risk

Correlation enters portfolio risk through the two-asset variance formula. For weights w₁, w₂, volatilities σ₁, σ₂, and correlation ρ:

```
σ_portfolio² = w₁²σ₁² + w₂²σ₂² + 2·w₁·w₂·σ₁·σ₂·ρ
```

The entire diversification benefit lives in that last term: the lower ρ is, the smaller (or negative) the cross term, and the lower portfolio risk becomes for the *same* expected return. This is the mathematical core of [[modern-portfolio-theory]] and [[diversification]].

### Worked example (qualitative)

Take two assets each with 20% annual [[volatility]], combined 50/50:

| Correlation (ρ) | Approx. portfolio volatility | Diversification benefit |
|-----------------|------------------------------|--------------------------|
| +1.0 | 20% | None — risk is the weighted average |
| +0.5 | ~17.3% | Modest reduction |
| 0.0 | ~14.1% | Substantial — risk falls ~30% below the average |
| -0.5 | ~10.0% | Strong — half the volatility |
| -1.0 | 0% | Perfect hedge — risk fully cancels |

The lesson: combining two equally risky assets only reduces risk when they are *not* perfectly correlated, and the benefit grows as ρ falls. This is precisely why [[diversification]] is "the only free lunch in investing" — and why [[correlation-breakdown]] (ρ spiking toward +1 in a crisis) is so dangerous: it removes the benefit exactly when it is needed most.

## Correlation vs Covariance

| Measure | Range | Depends on Scale? | Use Case |
|---------|-------|-------------------|----------|
| Covariance | -infinity to +infinity | Yes (units = return x return) | Mathematical input for [[modern-portfolio-theory]] |
| Correlation | -1 to +1 | No (dimensionless) | Intuitive comparison across any pair of assets |

Correlation is the standardized version of covariance. Covariance tells you the direction and magnitude of the relationship; correlation strips out magnitude to give a pure directional measure.

## Rolling Correlation

Static correlation (calculated over an entire history) can be misleading because the relationship between assets changes over time. Rolling correlation calculates the coefficient over a moving window:

- **Common windows**: 30-day, 60-day, 90-day, 252-day (1 year)
- **Shorter windows**: More responsive to recent changes, but noisier
- **Longer windows**: More stable, but slower to detect regime shifts

### Why Rolling Correlation Matters

- Two assets that were uncorrelated for years may suddenly become highly correlated
- Correlation tends to increase during market stress (see below)
- Trading strategies should monitor rolling correlation and adjust position sizes when the relationship changes
- [[risk-parity]] and [[portfolio-rebalancing]] strategies need current correlation estimates, not historical averages

## Correlation Breakdown in Crises

One of the most important facts in portfolio management: **correlations tend to spike toward +1 during market crises**. This phenomenon is sometimes called "correlation breakdown" (though the correlation is actually increasing, not breaking).

### Why This Happens

1. **Forced selling**: When institutions face margin calls or redemptions, they sell everything -- [[deleveraging]] is indiscriminate
2. **Risk-off behavior**: Investors flee all risky assets simultaneously, moving to cash and government bonds
3. **[[liquidity-risk|Liquidity]] withdrawal**: Market makers widen spreads and reduce risk, amplifying price moves across all assets
4. **Contagion**: Losses in one asset class force selling in others to meet margin requirements

### Historical Examples

- **2008 Financial Crisis**: Stocks, corporate bonds, commodities, and even some "hedges" fell simultaneously. Only US Treasuries and gold provided protection.
- **March 2020 (COVID crash)**: Nearly all assets sold off together in the initial liquidity panic, including gold (briefly). Treasuries eventually rallied.
- **Crypto crashes**: During major crypto drawdowns, [[bitcoin]], [[ethereum]], and altcoins all correlate at 0.9+ -- "diversifying" across crypto assets provides almost no risk reduction.

### Implications for Risk Management

- Do not assume your portfolio's "normal" correlation will hold during a crisis
- Stress-test portfolios using crisis-period correlations, not average correlations
- True diversifiers during crises are limited: government bonds, gold, [[vix]] derivatives, and cash
- [[derisking]] protocols should trigger when cross-asset correlation spikes

## Using Correlation for Portfolio Construction

### Efficient Frontier

[[modern-portfolio-theory]] uses correlation (via the covariance matrix) to construct the [[efficient-frontier]] -- the set of portfolios offering maximum return for each level of risk:

- Lower correlations between holdings push the efficient frontier further northwest (higher return per unit of risk)
- The optimal portfolio is not the one with the highest returns, but the one with the best risk-adjusted returns given the correlation structure

### Practical Portfolio Rules

- **Target average pairwise correlation below 0.4**: A portfolio where all holdings are correlated above 0.7 is effectively a concentrated bet
- **Include assets with negative correlation**: Even a small allocation to a negatively correlated asset (e.g., long volatility) can significantly reduce portfolio drawdowns
- **Monitor correlation stability**: Assets with unstable correlations are less reliable diversifiers
- **Correlation is not static**: Rebalance and reassess quarterly or when market regimes shift

### Position Sizing Adjustment

[[position-sizing]] should account for correlation between positions:

- If two positions are highly correlated (r > 0.7), treat them as partially the same position and reduce sizes accordingly
- The effective number of independent bets = N / (1 + (N-1) x avg_correlation), where N is the number of positions
- A portfolio of 10 positions with average correlation of 0.6 has roughly 2.5 effective independent positions

## Cross-Asset Correlations

The following are *indicative, regime-dependent* ranges — not fixed constants. Every one of them rises toward +1 in a [[correlation-breakdown|liquidity crisis]]. Use them as priors, not promises.

| Pair | Typical range (normal regime) | Behaviour in stress | Notes |
|------|-------------------------------|---------------------|-------|
| Stocks–Bonds | -0.5 to +0.5 (regime-dependent) | Can flip positive (2022) | Sign depends on inflation vs growth driver |
| Stocks–Gold | -0.2 to +0.2 | Gold often holds / rallies | Defensive diversifier, not reliable hedge |
| Stocks–Oil | -0.2 to +0.4 | Both fall in demand shocks | Cyclical, inflation-linked |
| BTC–ETH | +0.8 to +0.95 | ~+0.95 | Near-redundant; little diversification |
| BTC–NASDAQ | +0.3 to +0.6 | Rises | Grew with institutional adoption post-2020 |
| BTC–Gold | 0.0 to +0.3 | Inconsistent | Weak support for "digital gold" |
| USD ([[dxy]])–Risk assets | Negative | More negative | Flight-to-USD in risk-off |

### Stocks and Bonds

Historically the most important correlation for portfolio construction:

- **Pre-2000**: Stocks and bonds were often positively correlated (both driven by inflation)
- **2000-2021**: Negative correlation (flight-to-quality during stock selloffs boosted bonds)
- **2022-2024**: Positive correlation returned as inflation forced rates higher, hurting both stocks and bonds simultaneously
- The stock-bond correlation is not stable and depends on the macroeconomic regime (inflation vs growth-driven)

### Stocks and Commodities

- Generally low or negative correlation with stocks over long periods
- Oil and gold provide different diversification benefits: oil is cyclical, gold is defensive
- [[commodity-inflation-link|Commodities as inflation hedge]]: tend to rally when inflation surprises to the upside

### Crypto Correlations

Crypto assets have a distinct correlation structure:

- **BTC-ETH**: Typically 0.8-0.95 -- very high, limited diversification benefit
- **BTC-altcoins**: 0.5-0.9 depending on the altcoin and market conditions; rises sharply in crashes
- **BTC-stocks (NASDAQ)**: Correlation has increased since 2020 as institutional adoption grew; typically 0.3-0.6
- **BTC-gold**: Low and inconsistent (0.0-0.3); the "digital gold" narrative has weak correlation support
- **During crypto crashes**: All crypto correlations spike to 0.9+; the only hedge is not being in crypto

### Currency Correlations

- [[dxy|USD strength]] is generally negatively correlated with risk assets
- AUD/USD and NZD/USD are positively correlated with global risk appetite
- JPY tends to strengthen during risk-off events (carry trade unwinds)

## Correlation in Strategy Development

### Pairs Trading

[[pairs-trading]] directly exploits correlation:

- Identify two assets with historically high correlation (r > 0.8)
- When the spread between them widens beyond normal, go long the underperformer and short the outperformer
- Profit as the spread reverts to its historical mean
- Risk: correlation can break permanently (structural change)

### Strategy Portfolio Correlation

When running multiple strategies, the [[strategy-correlation-matrix]] determines overall portfolio risk:

- Strategies with low correlation to each other provide genuine diversification
- A momentum strategy and a mean-reversion strategy are often negatively correlated (good)
- Two momentum strategies on correlated assets are highly correlated (bad -- effectively the same bet)
- Allocate more capital to strategies that have low correlation with the rest of the portfolio

### Correlation as an Indicator

- [[implied-correlation]]: Derived from index option prices; measures the market's expectation of future correlation
- Rising implied correlation signals increasing systematic risk (less benefit from diversification)
- The CBOE Implied Correlation Index can serve as a market stress indicator

## Measurement Choices That Change the Answer

Correlation is not a single number — the value you get depends on choices that are easy to make carelessly:

| Choice | Effect on the estimate |
|--------|------------------------|
| **Return frequency** (daily vs weekly vs monthly) | Daily returns can understate correlation when assets trade in different time zones (non-synchronous pricing); lower frequencies often read higher |
| **Lookback window** | Short windows are noisy; long windows blur regime changes (see [[#Rolling Correlation]]) |
| **Pearson vs Spearman** | Pearson captures linear co-movement; Spearman (rank) captures monotonic relationships and is more robust to outliers |
| **Levels vs returns** | Correlating price *levels* produces spurious correlation; always use returns |
| **Conditioning on regime** | Up-market and down-market correlations differ (Ang & Chen, 2002 — see [[#Sources]]) |

Pearson correlation also only measures *linear* association. Two assets can have ρ ≈ 0 yet be strongly dependent in the tails — the case that matters most for risk. This is why [[tail-risk]] analysis often turns to copulas and tail-dependence measures rather than a single Pearson coefficient.

## Common Mistakes

1. **Assuming correlation is constant**: It changes with market regime, volatility level, and time frame
2. **Confusing correlation with causation**: Two correlated assets may both be driven by a third factor
3. **Ignoring non-linear relationships**: Pearson correlation only captures linear relationships; assets may be uncorrelated in normal markets but highly correlated in tails (see [[tail-risk]])
4. **Over-relying on historical correlation**: The past 5 years may not predict the next 5 years, especially across regime changes
5. **Diversifying within correlated assets**: 20 different altcoins is not diversification if they all correlate at 0.9

## Sources

- Markowitz, H. (1952). "Portfolio Selection." *Journal of Finance*, 7(1), 77-91 — the foundational paper establishing covariance/correlation as the core input to portfolio optimization.
- Longin, F. & Solnik, B. (2001). "Extreme Correlation of International Equity Markets." *Journal of Finance*, 56(2), 649-676 — documents that correlations rise in market downturns (tail dependence).
- CBOE. "Cboe S&P 500 Implied Correlation Indices" methodology — basis for [[implied-correlation]] as a systematic-risk gauge.
- Ang, A. & Chen, J. (2002). "Asymmetric Correlations of Equity Portfolios." *Journal of Financial Economics*, 63(3), 443-494 — correlation asymmetry between up and down markets.

## Related

- [[diversification]] -- Relies on low correlation between holdings
- [[modern-portfolio-theory]] -- Uses correlation to optimize portfolios
- [[efficient-frontier]] -- Optimal risk-return tradeoffs given correlation structure
- [[position-sizing]] -- Should account for inter-asset correlation
- [[volatility]] -- Correlated assets amplify portfolio volatility
- [[risk-parity]] -- Equalizes risk contribution using correlation and volatility
- [[correlation-matrix]] -- Visualizing pairwise correlations
- [[strategy-correlation-matrix]] -- Correlation between trading strategies
- [[implied-correlation]] -- Market-implied future correlation
- [[derisking]] -- Triggered by correlation spikes
- [[portfolio-construction]] -- Building portfolios with optimal correlation structure
- [[covariance]] -- The unstandardized version of correlation
- [[correlation-breakdown]] -- When correlations spike toward +1 in crises
- [[tail-risk]] -- Where linear correlation breaks down and dependence concentrates
- [[pairs-trading]] -- A strategy that directly exploits high correlation
- [[diversification]] -- The free lunch that low correlation provides
