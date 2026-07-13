---
title: "Asset Allocation"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [portfolio-theory, risk-management]
aliases: ["Asset Allocation", "Strategic Asset Allocation", "Tactical Asset Allocation"]
domain: [portfolio-theory]
prerequisites: ["[[diversification]]"]
difficulty: beginner
related: ["[[diversification]]", "[[two-portfolio-strategy]]", "[[cash-as-asset]]", "[[portfolio-construction]]", "[[sector-rotation]]", "[[rebalancing]]", "[[risk-parity]]", "[[all-weather-portfolio]]", "[[modern-portfolio-theory]]"]
---

Asset allocation is the process of dividing a portfolio across different asset classes (equities, bonds, cash, commodities, real estate) to balance risk and return. It is the practical implementation of [[diversification]] at the highest level of a portfolio and the lever that [[modern-portfolio-theory|Modern Portfolio Theory]] identifies as the primary driver of the risk/return outcome. [[fred-mcnaught|Fred]] practises asset allocation through his [[two-portfolio-strategy]] (core + trading), maintaining [[cash-as-asset|cash as a distinct asset class]], and diversifying across sectors ([[gics-classification|GICS sectors]]) and geographies (domestic + international via SelfWealth).

## Why Asset Allocation Matters

Landmark research by Gary Brinson, L. Randolph Hood, and Gilbert Beebower (1986, updated 1991) found that asset allocation explains approximately 90% of the *variation* in portfolio returns over time, with individual security selection and [[market-timing]] contributing far less. This finding -- often summarized as "asset allocation is the most important investment decision" -- underscores that the choice between stocks, bonds, and cash matters more than which specific stocks or bonds to own. The implication is that investors should spend the majority of their planning effort on getting the asset mix right rather than obsessing over individual holdings.

> **Common misreading:** The Brinson result is about the variability of returns through time, not the *level* of return. It is often misquoted as "asset allocation determines 90% of your returns." The more defensible claim is that, for a diversified investor, the asset-class mix dominates the path of portfolio value far more than stock picking does.

## The Major Asset Classes

Each asset class earns a distinct risk premium and behaves differently across the economic cycle. The table below sketches typical roles (illustrative, long-run averages -- not a forecast).

| Asset class | Primary role | Typical real return | Volatility | Behaves best in |
|-------------|--------------|---------------------|------------|-----------------|
| Equities ([[sp500\|stocks]]) | Growth engine | High (~5-7% real) | High | Expansion / disinflation |
| Government [[bonds\|bonds]] | Deflation hedge, ballast | Low-moderate | Low-moderate | Recession / risk-off |
| Credit (corporate bonds) | Yield with some growth beta | Moderate | Moderate | Mid-cycle |
| [[cash-as-asset\|Cash]] / T-bills | Liquidity, dry powder, optionality | ~0% real | Near zero | Rate hikes / stress |
| [[commodities]] / [[gold]] | Inflation hedge | Variable | High | Inflation / supply shocks |
| Real estate (REITs) | Income + inflation pass-through | Moderate | Moderate-high | Reflation |

The reason mixing these works is [[correlation]]: when asset classes are imperfectly correlated, combining them lowers portfolio [[volatility]] for a given expected return -- the core mechanism behind the [[efficient-frontier]].

## Strategic vs. Tactical Allocation

**Strategic asset allocation (SAA)** sets long-term target weights based on an investor's risk tolerance, time horizon, and return objectives. The classic example is the **60/40 portfolio** (60% equities, 40% bonds), which has historically provided equity-like returns with lower [[volatility]] due to the typically negative correlation between stocks and bonds during risk-off periods. However, the 60/40 model struggled badly in 2022 when both stocks and bonds fell simultaneously as interest rates rose sharply -- a reminder that stock-bond correlation is regime-dependent, not a law of nature (see [[market-regime]]).

**Tactical asset allocation (TAA)** makes shorter-term adjustments around strategic weights based on market conditions, valuations, or macro signals -- for example, overweighting equities during early-cycle recoveries and shifting to bonds/cash during late-cycle peaks. TAA introduces [[market-timing]] risk and requires genuine skill to add value consistently net of trading costs and taxes.

| Dimension | Strategic (SAA) | Tactical (TAA) |
|-----------|-----------------|----------------|
| Horizon | Years to decades | Weeks to quarters |
| Driver | Goals, risk capacity | Valuation, macro, momentum |
| Turnover | Low (rebalance only) | Higher |
| Main risk | Drift, wrong long-run mix | Mis-timing, whipsaw, costs |
| Skill required | Low-moderate | High |

## Worked Example: Drift and Rebalancing

Suppose an investor sets a **60/40** target on a $100,000 portfolio: $60,000 equities, $40,000 bonds. Over a strong year equities rise 25% and bonds fall 5%:

- Equities: $60,000 -> $75,000
- Bonds: $40,000 -> $38,000
- Total: $113,000 -> the mix has **drifted to ~66/34**

The portfolio is now meaningfully riskier than intended. [[rebalancing|Rebalancing]] back to 60/40 means selling ~$7,200 of equities and buying bonds, mechanically "selling high and buying low." This is the disciplined counter-cyclical behaviour that asset allocation enforces -- and why drift control is as important as the original target.

## Alternative Approaches

**Risk parity** (popularized by Bridgewater's Ray Dalio; see [[risk-parity]] and the [[all-weather-portfolio]]) allocates based on risk contribution rather than capital, typically using [[leverage]] to bring lower-volatility assets (bonds) up to equity-like risk levels, so each asset class contributes equally to total portfolio risk. **Endowment model** (the "Yale model" developed by David Swensen) emphasizes heavy allocation to alternatives -- private equity, real estate, hedge funds -- and minimal fixed income, trading liquidity for return. **Lifecycle / target-date** approaches automatically shift from aggressive (equity-heavy) to conservative (bond-heavy) as the investor ages, following a "glide path." A common rule-of-thumb glide path is **equity % ≈ 110 − age**, though this is a crude heuristic, not a prescription.

| Approach | Allocation basis | Best suited to | Key trade-off |
|----------|------------------|----------------|---------------|
| 60/40 (strategic) | Capital weights | Most investors | Fails when stocks & bonds fall together |
| Risk parity | Equal risk contribution | Sophisticated, leverage-tolerant | Relies on leverage and stable correlations |
| Endowment / Yale | Heavy alternatives | Long-horizon institutions | Illiquidity, manager selection risk |
| Target-date glide path | Age / horizon | Hands-off retirement savers | One-size-fits-all, ignores valuation |

## How Traders and Investors Use It

- **Top-down framing:** decide the asset mix *first*, then populate each sleeve with specific holdings -- the opposite of starting from individual stock ideas.
- **Risk budgeting:** treat the allocation as a risk budget. A [[two-portfolio-strategy]] separates a stable core (income, index, infrastructure) from an active trading book that carries a deliberately small, capped share of risk.
- **Cash as a position:** holding [[cash-as-asset|cash]] is an active choice, not a failure to invest -- it provides optionality and dry powder for drawdowns.
- **Sector and geographic tilts:** within equities, allocation extends to [[sector-rotation|sectors]] ([[gics-classification|GICS]]) and regions, capturing diversification benefits beyond the stock/bond split.

## Common Pitfalls and Risks

- **Correlation breakdown:** diversification benefits shrink exactly when needed -- in crises, many "uncorrelated" assets fall together (correlations go to 1). 2022 is the canonical recent example.
- **Allocation drift:** without [[rebalancing]], winners grow until the portfolio is far riskier than the stated target.
- **Closet timing:** dressing up [[market-timing]] as "tactical" allocation. Most retail TAA underperforms a disciplined strategic mix after costs.
- **Home-country bias:** over-concentration in domestic equities reduces genuine diversification.
- **Ignoring taxes and costs:** rebalancing and tactical shifts trigger transaction costs and capital-gains events that can erode the theoretical benefit.
- **Reaching for yield:** swapping ballast bonds for high-yield credit raises hidden equity-like risk in the "defensive" sleeve.

## Related

- [[diversification]] -- the underlying principle that asset allocation implements
- [[portfolio-construction]] -- the broader process of building a portfolio
- [[rebalancing]] -- maintaining target allocations over time
- [[two-portfolio-strategy]] -- Fred's practical approach to allocation
- [[cash-as-asset]] -- treating cash as a deliberate allocation, not just a residual
- [[risk-parity]] -- allocating by risk contribution rather than capital
- [[all-weather-portfolio]] -- a risk-parity allocation designed for all regimes
- [[modern-portfolio-theory]] -- the theoretical framework asset allocation implements
- [[efficient-frontier]] -- the set of optimal risk/return mixes allocation targets
- [[correlation]] -- why combining asset classes lowers portfolio risk
- [[sector-rotation]] -- allocation within the equity sleeve across sectors
- [[market-timing]] -- the risk tactical allocation introduces

## Sources

- Brinson, Gary P., L. Randolph Hood, and Gilbert L. Beebower. "Determinants of Portfolio Performance." *Financial Analysts Journal* (1986; updated 1991).
- Markowitz, Harry. "Portfolio Selection." *Journal of Finance* (1952) -- the theoretical basis for diversifying across asset classes.
- Swensen, David. *Pioneering Portfolio Management* (2000) -- the endowment ("Yale") model.
- Dalio, Ray. *Principles* / Bridgewater research -- the risk-parity approach to allocation.
