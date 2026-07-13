---
title: "Dragon Portfolio"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [portfolio-theory, crisis-alpha, trend-following, tail-risk]
aliases: ["Dragon Portfolio", "Artemis Dragon Portfolio"]
related: ["[[trend-plus-tail-hedge]]", "[[crisis-alpha]]", "[[all-weather-portfolio]]", "[[risk-parity]]", "[[trend-following-cta]]", "[[tail-risk-hedging]]", "[[gold]]", "[[commodities]]", "[[commodity-inflation-link]]", "[[antifragility]]", "[[portfolio-construction]]", "[[convexity]]"]
domain: [portfolio-theory]
prerequisites: ["[[portfolio-construction]]", "[[trend-plus-tail-hedge]]", "[[crisis-alpha]]"]
difficulty: advanced
---

The Dragon Portfolio is a macro-regime-resilient portfolio framework developed by Chris Cole of Artemis Capital Management in his 2020 research paper "The Allegory of the Hawk and Serpent." It is designed to perform across all four macro regimes — growth, recession, inflation, and deflation — rather than relying on the single regime (falling rates + rising growth) that has favored traditional portfolios since the 1980s.

## The Problem with Traditional Portfolios

The canonical 60/40 stock/bond portfolio — and even more sophisticated variants like [[risk-parity]] and [[all-weather-portfolio|All Weather]] — are heavily exposed to a single macro regime: falling interest rates paired with economic growth. The period from 1984 to 2020 was uniquely favorable for this regime. But examining 100 years of data (including the 1920s-1940s, the 1970s stagflation, and the Great Depression), 60/40 suffered devastating real drawdowns:

- **1929-1932**: Real equity losses of ~80%, bonds offered limited protection
- **1940s**: Negative real returns from financial repression (rates held below inflation)
- **1970s**: Both stocks and bonds lost real value during [[stagflation]]
- **2022**: Bonds fell 13% in the same year equities fell 25% — the "diversifier" failed

Cole's key insight: the last 40 years were a historically anomalous period for balanced portfolios. Investors who extrapolate that experience forward are making a regime-dependent bet, not a diversified allocation.

## The Five Components

The Dragon Portfolio allocates roughly equal risk across five asset classes, each designed to thrive in a different macro environment:

### 1. Equity-Linked Growth (~24%)

Long equities for growth and prosperity. This is the conventional portfolio engine — equities deliver the highest long-run real returns during periods of economic expansion and rising corporate profits. Implemented via broad equity index funds (S&P 500, global equity).

### 2. Fixed Income (~18%)

Bonds for deflation and recession protection. When economic growth collapses and central banks cut rates, high-quality bonds rally. This is the traditional "hedge" in 60/40 — but Cole recognizes it only works in deflationary/disinflationary recessions, not inflationary ones.

### 3. Gold (~19%)

Store of value for monetary debasement and inflation. [[gold]] protects against currency devaluation, loss of confidence in fiat money, and inflationary regimes. It performed strongly in the 1970s (+1,300%) and in 2020-2024 as central banks expanded balance sheets. See [[commodity-inflation-link]] for the broader relationship between commodities and inflation.

### 4. Commodity Trend Following (~18%)

[[trend-following-cta|CTAs and managed futures]] for inflation trends and [[crisis-alpha]]. This is the component most traditional portfolios lack entirely. Commodity trend following:

- Profits during inflationary spirals (long commodities, short bonds)
- Delivers crisis alpha during equity bear markets (short equities)
- Provides genuine diversification because it can go both long and short across all asset classes
- Earned +25-45% in 2022 when both stocks and bonds fell

### 5. Long Volatility / Tail Risk (~21%)

[[tail-risk-hedging|Options-based tail hedging]] for sudden crashes and volatility spikes. Deep OTM puts and [[vix|VIX]] calls that provide extreme [[convexity]] — near-zero value in calm markets, explosive payoffs in crises. This component protects against the fast crashes that trend following is too slow to catch.

## Why "Dragon"

Cole uses a mythological metaphor: the **hawk** represents equity and growth (soaring in good times), and the **serpent** represents bonds and deflation protection (coiled and defensive). Traditional portfolios combine only these two animals. The **dragon** combines both AND adds fire — commodity trend following, gold, and long volatility — creating a creature that thrives in chaos. The name captures the idea that the portfolio is not just resilient but potentially [[antifragility|antifragile]]: it can actually benefit from the disorder that destroys conventional allocations.

## Key Insight: Trend Following + Long Volatility

The most important finding in Cole's research is that over 100 years, the combination of commodity trend following plus long volatility is the only strategy pairing that consistently protected against both inflationary AND deflationary crises:

- **Inflationary crises** (1970s, 2022): Trend following profits by going long commodities and short bonds. Long volatility provides additional protection from volatility expansion.
- **Deflationary crises** (1930s, 2008): Trend following profits by going short equities and long bonds. Tail hedges explode in value during crash events.

Equities protect only in growth. Bonds protect only in deflationary recession. Gold protects mainly in inflation. Only trend following + long volatility protect across the full spectrum. This is why [[trend-plus-tail-hedge]] is the critical "missing allocation" in most portfolios.

## Historical Performance

Cole's backtested research (1928-2020) shows the Dragon Portfolio would have generated approximately 9% annualized real returns over the full period, with significantly lower maximum drawdown than alternatives:

| Portfolio | Annualized Real Return | Max Drawdown | Worst Decade |
|-----------|----------------------|--------------|--------------|
| 60/40 | ~5.5% | ~-45% | 1970s (negative real) |
| Risk Parity | ~6.5% | ~-30% | 1970s |
| All Weather | ~6% | ~-25% | 1940s |
| Dragon Portfolio | ~9% | ~-15% | None catastrophic |

The Dragon Portfolio's edge is not higher returns per se — it is the avoidance of devastating drawdowns that take decades to recover from. By avoiding the -40% to -80% real drawdowns that afflicted every other approach in at least one regime, the Dragon compounds more effectively over long periods.

## Implementation

### For Institutional / Large Portfolios

- **Equity**: Broad global equity index (S&P 500, MSCI World)
- **Fixed income**: Long-duration US Treasuries ([[us-treasury-bonds]])
- **Gold**: Physical gold or GLD ETF, gold futures
- **Commodity trend following**: Allocation to CTA managers (Man AHL, Winton, etc.) or managed futures ETFs (DBMF, KMLM)
- **Long volatility**: Deep OTM SPX puts, VIX calls, or allocation to specialized tail-risk managers like [[universa-investments|Universa]]

### For Individual Investors

Implementation is harder at smaller scale because the long volatility component is expensive and complex. Practical approximations:

- Use managed futures ETFs (DBMF, KMLM) for the trend-following allocation
- Use a small allocation to TAIL (Cambria Tail Risk ETF) or similar for the long-vol component
- Gold via GLD or IAU
- Broad equity index via VOO or VTI
- Bond allocation via TLT (long-duration Treasuries)

The main challenge is that ETF proxies for trend following and long volatility are imperfect — they carry higher fees, tracking error, and may not capture the full convexity of direct futures/options implementation.

## Criticism

- **Backtesting limitations**: The 100-year backtest covers periods with very different market structures, instruments, and regulatory environments. Trend-following returns before the 1970s are partially reconstructed.
- **Long volatility cost**: The ~21% allocation to long volatility/tail risk creates a persistent drag of 2-4% annually during calm markets. Maintaining conviction through years of bleed is psychologically difficult.
- **Complexity**: Five components with periodic rebalancing is significantly more complex than a simple 60/40 or even [[risk-parity]] approach. Transaction costs and management fees can erode the theoretical edge.
- **Capacity constraints**: Both trend following and long volatility have capacity limits — if too many investors adopt the Dragon Portfolio, the strategies that power it may become crowded and less effective.
- **Regime-dependent assumptions**: The framework assumes macro regimes will continue to alternate. If the future is dominated by a single regime (e.g., permanent low rates and growth), the diversification across five components may be unnecessary overhead.

## Comparison with Related Frameworks

| Framework | Overlap with Dragon | Key Difference |
|-----------|-------------------|----------------|
| [[all-weather-portfolio]] | Both use risk-balanced allocation across macro regimes | All Weather lacks dedicated long-volatility and trend-following allocations |
| [[risk-parity]] | Both equalize risk contribution | Risk parity uses leverage on bonds; Dragon uses active strategies for crisis alpha |
| [[trend-plus-tail-hedge]] | Dragon includes both trend + tail | Dragon adds equities, bonds, and gold as standalone allocations |
| [[asymmetric-barbell]] | Both seek convex payoffs | Barbell is two extremes; Dragon is five balanced components |

## Related

- [[trend-plus-tail-hedge]] — the trend + tail component that is the Dragon's core innovation
- [[crisis-alpha]] — the return stream that Dragon aims to capture during crises
- [[all-weather-portfolio]] — Bridgewater's related but less complete framework
- [[risk-parity]] — risk-balanced allocation that Dragon builds upon
- [[trend-following-cta]] — the managed futures component
- [[tail-risk-hedging]] — the long-volatility component
- [[convexity]] — the payoff property that makes crisis-alpha components work
- [[gold]] — the monetary debasement hedge
- [[commodity-inflation-link]] — why commodities protect in inflationary regimes
- [[antifragility]] — the philosophical principle underlying the Dragon
- [[portfolio-construction]] — broader framework for building portfolios

## Sources

- Chris Cole, "The Allegory of the Hawk and Serpent" (Artemis Capital Management, 2020) — the original Dragon Portfolio research paper
- [[trend-plus-tail-hedge]] — detailed implementation of the crisis-alpha components
