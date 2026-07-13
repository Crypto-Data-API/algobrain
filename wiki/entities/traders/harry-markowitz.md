---
title: "Harry Markowitz"
type: entity
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [person, portfolio-theory, risk-management, history, quantitative]
entity_type: person
aliases: ["Harry Markowitz", "Harry M. Markowitz", "Harry Max Markowitz"]
related: ["[[modern-portfolio-theory]]", "[[efficient-frontier]]", "[[diversification]]", "[[william-sharpe]]", "[[capm]]", "[[jack-treynor]]", "[[mean-variance-optimization]]", "[[correlation]]", "[[sharpe-ratio]]", "[[risk-management]]"]
---

# Harry Markowitz

Harry Max Markowitz (August 24, 1927 – June 22, 2023) was an American economist who founded **Modern Portfolio Theory (MPT)** with his 1952 paper *"Portfolio Selection,"* for which he shared the 1990 Nobel Memorial Prize in Economic Sciences. His core insight — that investors should evaluate assets by their contribution to portfolio-level risk and return, not in isolation — underpins virtually all institutional asset allocation, risk budgeting, and the [[mean-variance-optimization|mean-variance optimizers]] traders still use today.

## Key Facts

| Field | Detail |
|-------|--------|
| Full name | Harry Max Markowitz |
| Born | August 24, 1927, Chicago, Illinois, USA |
| Died | June 22, 2023, San Diego, California (aged 95) |
| Nationality | American |
| Education | University of Chicago (PhB, MA, PhD 1954) |
| PhD committee | Included Milton Friedman |
| Seminal work | *"[[modern-portfolio-theory\|Portfolio Selection]]"*, *Journal of Finance*, **March 1952** |
| Book | *Portfolio Selection: Efficient Diversification of Investments* (1959) |
| Nobel Prize | **1990**, shared with [[william-sharpe\|William Sharpe]] and Merton Miller |
| Other honors | von Neumann Theory Prize (1989) |
| Also created | **SIMSCRIPT** simulation language (with RAND, 1962); co-founded CACI |
| Field | [[portfolio-theory\|Portfolio theory]], [[risk-management]], financial economics |

## Who He Was and His Era

Markowitz was born in Chicago and studied economics at the **University of Chicago** (PhB, MA, PhD 1954), where his dissertation committee included **Milton Friedman** — who famously remarked, half-joking, that portfolio theory was "not economics." Markowitz's breakthrough came as a graduate student: reading John Burr Williams' theory that a stock's value is the present value of its future dividends, he noticed it implied an investor should simply put all their money in the single highest-expected-return security. That clearly contradicted real-world [[diversification]], and resolving the contradiction — by introducing **risk** (variance) as a second dimension to be optimized against return — produced MPT.

His 14-page article *"Portfolio Selection"* appeared in the *Journal of Finance* in **March 1952**, and he expanded it into the **1959** book *Portfolio Selection: Efficient Diversification of Investments*. He came of age intellectually alongside the founders of mathematical finance and operations research, bridging economics and computation throughout his career.

## What He Is Known For: Modern Portfolio Theory

Markowitz reframed investing as a constrained optimization problem in two variables: **expected return** and **risk, measured as variance (or its square root, standard deviation)**.

### The Core Mathematics

For a portfolio of assets with weights *wᵢ*:

- **Portfolio expected return** is the weighted average of the assets' expected returns:
  **E(Rₚ) = Σ wᵢ · E(Rᵢ)**
- **Portfolio variance** is **not** a simple weighted average — it depends on how assets *co-move*:
  **σ²ₚ = Σᵢ Σⱼ wᵢ wⱼ σᵢ σⱼ ρᵢⱼ**

  where **ρᵢⱼ** is the [[correlation]] between assets *i* and *j*. This term is the entire point: combining assets that are not perfectly correlated produces a portfolio whose risk is **less than the weighted average of the individual risks**. Diversification is, mathematically, "the only free lunch in investing."

### The Efficient Frontier

Plotting every possible portfolio in risk–return space produces a cloud whose upper-left boundary is the **[[efficient-frontier|efficient frontier]]** — the set of portfolios offering the **maximum expected return for each level of variance** (equivalently, minimum variance for each level of return). Rational, risk-averse investors should hold only frontier portfolios; everything below the frontier is dominated. This turned [[diversification]] from a folk rule ("don't put all your eggs in one basket") into a precise mathematical optimization.

## Career Beyond the 1952 Paper

- **RAND Corporation** — at RAND in the 1950s he worked on optimization and simulation, co-developing the **SIMSCRIPT** programming language (1962) and later co-founding **CACI**. He also influenced and mentored [[william-sharpe|William Sharpe]], whose [[capm|Capital Asset Pricing Model]] built directly on MPT and introduced beta and the [[sharpe-ratio|Sharpe ratio]].
- **Nobel Prize 1990** — shared with William Sharpe and Merton Miller "for pioneering work in the theory of financial economics." He also received the **von Neumann Theory Prize (1989)** from the operations-research community.
- **Later career** — professor at Baruch College and, from 1994, at UC San Diego's Rady School of Management; he consulted and published into his 90s, including the multi-volume *Risk-Return Analysis* series (2014–2020).
- He died in San Diego on **June 22, 2023**, aged 95.

## Why Markowitz Matters to Traders

- **[[mean-variance-optimization|Mean-variance optimization]]** remains the default framework for portfolio construction; every risk-parity, minimum-variance, and max-Sharpe allocation traces to his 1952 formulation.
- **Covariance is the point** — his demonstration that portfolio risk depends on [[correlation]] between assets, not just individual volatilities, is the basis of pairs construction, hedging, and cross-asset risk models.
- **Known limitations are tradable knowledge** — MPT's sensitivity to estimation error in expected returns ("error maximization") spawned successors traders use daily: the **Black-Litterman model** (see [[fischer-black]]), **shrinkage estimators** (Ledoit-Wolf), and robust/Bayesian optimization. Practitioners also note MPT assumes returns are normally distributed and that variance captures "risk" symmetrically — assumptions that fail in fat-tailed markets, motivating downside-risk and semivariance variants.
- Markowitz himself admitted he split his own retirement money 50/50 between stocks and bonds to minimize *regret* rather than running his own optimizer — an early, candid acknowledgment of the [[behavioral-finance]] limits to optimization.

## Influence and Legacy

Markowitz is universally regarded as the **father of [[modern-portfolio-theory]]** and one of the founders of quantitative finance. His framework launched the chain of theory that defines institutional investing: MPT → [[capm|CAPM]] (Sharpe, [[jack-treynor|Treynor]]) → the [[efficient-market-hypothesis|Efficient Market Hypothesis]] (Fama) → multi-factor models. The vocabulary of modern [[risk-management]] — efficient frontier, optimal portfolio, covariance matrix, diversification benefit — is essentially his. More than seventy years after a 14-page paper, mean-variance optimization is still the first tool taught in every portfolio-construction course and embedded in essentially every institutional allocation system.

## Related

- [[modern-portfolio-theory]] — the theory he founded
- [[efficient-frontier]] — his central construct
- [[mean-variance-optimization]] — the optimization method
- [[diversification]] — turned from folk rule into mathematics
- [[correlation]] — the term that makes diversification work
- [[william-sharpe]] / [[capm]] — the successor theory he influenced
- [[jack-treynor]] — co-developer of CAPM-era ideas
- [[sharpe-ratio]] — the risk-adjusted return measure built on his framework
- [[fischer-black]] — Black-Litterman, a key MPT refinement
- [[risk-management]] — the discipline he reshaped

## Sources

- Markowitz, H. (1952). "Portfolio Selection." *Journal of Finance*, 7(1), 77–91.
- Markowitz, H. (1959). *Portfolio Selection: Efficient Diversification of Investments*. Wiley.
- Nobel Prize biography: https://www.nobelprize.org/prizes/economic-sciences/1990/markowitz/biographical/
- Obituaries, June 2023 (NYT, Reuters) confirming death June 22, 2023, San Diego, age 95.
- Verified via Perplexity (sonar) and web search, 2026-06-10.
