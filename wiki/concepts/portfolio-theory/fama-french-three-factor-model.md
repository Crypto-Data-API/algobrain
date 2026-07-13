---
title: "Fama-French Three-Factor Model"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [portfolio-theory, quantitative, fundamental-analysis, valuation]
aliases: ["Fama-French", "Fama French Three Factor Model", "Three-Factor Model", "FF3", "SMB HML"]
related: ["[[capital-asset-pricing-model]]", "[[factor-investing]]", "[[value-factor]]", "[[size-factor]]", "[[momentum-factor]]", "[[low-vol-factor]]", "[[multi-factor-portfolio]]", "[[beta]]", "[[risk-free-rate]]", "[[sharpe-ratio]]"]
domain: [portfolio-theory, quantitative, anomalies]
prerequisites: ["[[capital-asset-pricing-model]]", "[[beta]]"]
difficulty: intermediate
---

The **Fama-French three-factor model** is an asset-pricing model that explains stock returns using three drivers instead of the single market factor in the [[capital-asset-pricing-model|CAPM]]: the **market** excess return, a **size** factor (small minus big, "SMB"), and a **value** factor (high minus low book-to-market, "HML"). Introduced by Eugene Fama and Kenneth French in their 1992-1993 papers, it showed that small-cap stocks and cheap ("value") stocks have historically earned higher average returns than the CAPM alone could explain, and it became the foundation of modern [[factor-investing]].

## Overview

The CAPM says a stock's expected return depends only on its sensitivity to the overall market ([[beta]]). Fama and French documented that two additional characteristics — a firm's **size** and its **book-to-market ratio** — explained a large part of the cross-section of returns that CAPM missed. Their model expresses a portfolio's excess return as a linear combination of three factor returns:

```
R_i − Rf = α + β_mkt·(R_mkt − Rf) + β_smb·SMB + β_hml·HML + ε
```

Where:
- **R_i − Rf** is the asset's return in excess of the [[risk-free-rate|risk-free rate]].
- **(R_mkt − Rf)** is the market risk premium (the CAPM factor).
- **SMB** ("Small Minus Big") is the average return of small-cap portfolios minus large-cap portfolios — the [[size-factor]].
- **HML** ("High Minus Low") is the average return of high book-to-market (value) portfolios minus low book-to-market (growth) portfolios — the [[value-factor]].
- **α** (alpha) is the return left unexplained by the three factors; a manager's skill (or luck) shows up here.

Fama and French built SMB and HML by sorting U.S. stocks into portfolios on size and book-to-market and taking long-short differences, a construction that became the template for nearly all later factors.

## Why It Matters

1. **It dethroned single-factor CAPM.** By the early 1990s the size effect (Banz, 1981) and the value effect (Basu, 1977) were well documented but had no unifying framework. The three-factor model gave the profession a richer, empirically grounded benchmark.
2. **It redefined "alpha."** A fund that beats the market may simply be loading on small-cap and value exposure — cheap, replicable risk premia — rather than generating genuine skill. Regressing a fund's returns on the three factors reveals how much of its performance is just factor tilt. This reframed the active-vs-passive debate.
3. **It launched factor investing and smart beta.** SMB and HML became investable products; the [[multi-factor-portfolio]] and the whole smart-beta ETF industry descend directly from this model.
4. **It is a research workhorse.** The three-factor regression is the standard tool for evaluating anomalies, fund performance, and trading strategies. Fama and French later extended it to a **five-factor model** (2015) adding profitability (RMW) and investment (CMA) factors, and a momentum factor (Carhart, 1997) is often appended to make a four-factor model.

## How It Is Used

- **Performance attribution:** regress a portfolio's monthly excess returns on the three factors; the betas show its style exposures and the intercept (alpha) shows skill net of those exposures.
- **Expected-return estimates:** combine a stock's factor loadings with expected factor premiums to estimate required return — an alternative to CAPM.
- **Strategy diagnosis:** if a "new" strategy's returns are fully explained by HML and SMB, it offers nothing beyond known factors. A statistically significant positive alpha *after* controlling for the factors is the bar a genuinely novel edge must clear.
- **Risk budgeting:** managers monitor SMB/HML loadings to avoid unintended concentration in small-cap or value risk.

Kenneth French maintains a widely-used public data library of the historical factor returns, which is why the three-factor model is the default benchmark in academic finance.

## Hypothetical Example

An analyst evaluates a small-cap value fund and runs a three-factor regression on its monthly excess returns, obtaining:

- Market beta = **1.05**
- SMB beta = **+0.60** (meaningful small-cap tilt)
- HML beta = **+0.45** (meaningful value tilt)
- Alpha = **+0.05% per month**, not statistically significant

Interpretation: the fund's outperformance versus a broad index is almost entirely *explained* by its loadings on the size and value factors — exposures an investor could obtain cheaply through a [[value-factor|value]] or small-cap index fund. The near-zero, insignificant alpha says the manager added little beyond those tilts, so paying an active fee for this fund is hard to justify. (Hypothetical numbers, for illustration only.)

## Criticisms and evolution

- **The factors are empirical, not theoretical.** Unlike CAPM, which derives from equilibrium theory, SMB and HML were found by data-mining the historical cross-section. Critics (notably in the "factor zoo" literature) argue that many published factors are the product of overfitting and fail to replicate out of sample.
- **The value premium has been weak since the mid-2000s.** HML delivered poor or negative returns for much of 2007–2020, a stretch long enough to raise the question of whether the value premium is compensation for risk, a behavioral mispricing that arbitrage has eroded, or partly a measurement artifact (book value poorly captures intangible-heavy modern firms). See [[value-factor]].
- **The size premium is fragile.** The standalone SMB premium is small, concentrated in the smallest and least-liquid stocks, sensitive to the January effect, and has largely disappeared in some post-1980 samples.
- **Model extensions.** Fama and French themselves added **profitability (RMW)** and **investment (CMA)** factors in their 2015 five-factor model, which makes HML partly redundant. A **momentum factor** (Carhart, 1997) is commonly appended because the three- and five-factor models notably fail to price momentum. Modern practice often uses these richer models — but they remain descriptive benchmarks, not laws.

## Related

- [[capital-asset-pricing-model]] — the single-factor model FF3 extends
- [[factor-investing]] — the discipline this model launched
- [[value-factor]] — the HML factor in detail
- [[size-factor]] — the SMB factor in detail
- [[momentum-factor]] — the fourth factor (Carhart) often appended
- [[low-vol-factor]], [[multi-factor-portfolio]] — modern factor stacks
- [[beta]] — the market factor loading
- [[risk-free-rate]] — excess returns are measured over Rf
- [[sharpe-ratio]] — risk-adjusted return the factors help decompose

## Sources

- Fama, E. F. and French, K. R. (1992). *"The Cross-Section of Expected Stock Returns."* *Journal of Finance* 47 (2): 427–465.
- Fama, E. F. and French, K. R. (1993). *"Common Risk Factors in the Returns on Stocks and Bonds."* *Journal of Financial Economics* 33 (1): 3–56.
- Fama, E. F. and French, K. R. (2015). *"A Five-Factor Asset Pricing Model."* *Journal of Financial Economics* 116 (1): 1–22.
- Carhart, M. M. (1997). *"On Persistence in Mutual Fund Performance."* *Journal of Finance* 52 (1): 57–82 (the momentum/four-factor extension).
- Kenneth R. French Data Library — public historical factor returns.
