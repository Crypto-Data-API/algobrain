---
title: "Momentum Investing"
type: strategy
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [quantitative, momentum, trend-following, stocks, backtesting]
aliases: ["Momentum Investing", "Momentum Strategy", "Cross-Sectional Momentum", "Momentum Stocks", "Stock Momentum", "Momentum Trading", "momo trading"]
related: ["[[trend-following]]", "[[momentum]]", "[[behavioral-finance]]", "[[factor-investing]]", "[[mean-reversion]]", "[[edge-taxonomy]]", "[[failure-modes]]"]
strategy_type: quantitative
timeframe: position
markets: [stocks, futures, crypto]
complexity: intermediate
backtest_status: cost-corrected
edge_source: [behavioral, risk-bearing]
edge_mechanism: "Investors underreact to news and sell winners too early (disposition effect), so prices drift toward fair value over months; momentum buyers harvest the drift while bearing crash risk at regime turns."
data_required: [ohlcv-daily, index-constituents, corporate-actions]
min_capital_usd: 25000
capacity_usd: 5000000000
crowding_risk: high
expected_sharpe: 0.5
expected_max_drawdown: 0.50
breakeven_cost_bps: 50
---

Momentum investing is a strategy that buys assets that have performed well over a recent period (typically 3-12 months) and sells or avoids assets that have performed poorly. It is one of the most thoroughly researched anomalies in finance, with academic evidence spanning over a century of data across dozens of markets worldwide. The strategy exploits the empirical tendency of asset returns to persist in the intermediate term -- past winners continue to outperform past losers for periods of several months before eventually reversing. It is the cross-sectional cousin of [[trend-following]] (time-series momentum) and a core member of the [[factor-investing|factor]] zoo alongside value and size.

## Quick Reference

| Dimension | Summary |
|---|---|
| **Core idea** | Buy recent winners, sell/avoid recent losers; returns persist over 3-12 months |
| **Canonical signal** | Cumulative return over months t-12 to t-2 (12-month lookback, skip last month) |
| **Edge source** | [[edge-taxonomy\|Behavioral (primary) + risk-bearing (secondary)]] — underreaction, disposition effect, crash-risk compensation |
| **Who's on the other side** | Investors who sell winners early and hold losers ([[behavioral-finance\|disposition effect]]); benchmark-constrained institutions |
| **Variants** | [[#Cross-Sectional Momentum\|Cross-sectional]], [[#Time-Series Momentum Trend Following\|time-series]] ([[trend-following]]), [[#Dual Momentum\|dual]] |
| **Turnover** | 100-300%/year — the binding cost and capacity constraint |
| **Crash risk** | Severe negative skew; academic WML lost ~91% (1932) and ~73% (2009) per Daniel-Moskowitz 2016 |
| **Crash control** | Vol-scaling (Barroso-Santa-Clara 2015) + bear-market de-risk (Daniel-Moskowitz 2016) |
| **Capacity** | ~$5B for equal-weighted US equity momentum (Korajczyk-Sadka 2004); higher for patient large-cap |
| **Crowding** | High — harvested simultaneously by factor funds, quant multistrats, and momentum ETFs |

## Overview

The momentum effect was formally documented by Narasimhan Jegadeesh and Sheridan Titman in their landmark 1993 paper "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency." They showed that a strategy of buying the top decile of stocks ranked by past 3-to-12-month returns and shorting the bottom decile generated average annual returns of approximately 12% per year from 1965 to 1989, after adjusting for market risk. Subsequent research has confirmed the effect across international equity markets, bonds, commodities, currencies, and even [[crypto-markets|cryptocurrencies]].

The persistence of momentum is remarkable. Geczy and Samonov (2016) documented the momentum premium in U.S. equities back to 1801, calling it "the world's longest backtest." Asness, Moskowitz, and Pedersen (2013) demonstrated momentum across eight diverse asset classes and multiple countries. It is widely regarded as one of the most robust return factors alongside value and size.

Despite its strong average returns, momentum is not a free lunch. The strategy is subject to severe and sudden drawdowns known as "momentum crashes," which tend to occur during sharp market reversals. Understanding and managing these crashes is critical to successful implementation.

## Edge source

Per the [[edge-taxonomy]], momentum draws primarily on the **behavioral** category, with a secondary **risk-bearing** component:

- **Behavioral** — the premium arises from systematic, persistent cognitive errors: underreaction to news, anchoring, and the disposition effect (detailed below). These biases are documented in investor-level trading data, not just inferred from prices, and they regenerate with each cohort of investors — which is the best explanation for why three decades of publication (post-Jegadeesh-Titman 1993) have weakened but not eliminated the effect.
- **Risk-bearing** — part of the premium is compensation for bearing crash risk. The long-short momentum portfolio has strongly negative skew and suffers its worst losses (-91% in 1932, -73% in 2009 for the academic WML portfolio per Daniel and Moskowitz 2016) at exactly the moments diversification fails. Investors who cannot tolerate that payoff profile cede the premium to those who can.

It is **not** an informational or latency edge: the signal is public, computable from past prices alone, and slow-moving. Whatever edge remains after crowding is earned by *holding the position through what others cannot hold*.

## Why this edge exists

**Who is on the other side:** investors who sell winners too early and cling to losers — predominantly retail investors exhibiting the disposition effect, but also institutions constrained by benchmarks, rebalancing rules, and career risk that force them to trim outperformers and average down into laggards.

The leading mechanisms from [[behavioral-finance]]:

- **Underreaction**: Investors are slow to incorporate new information into prices. Good news leads to gradual price appreciation as the market slowly adjusts, creating momentum in the interim. Earnings post-announcement drift is the cleanest documented instance.
- **Disposition effect**: Investors tend to sell winners too early and hold losers too long, dampening the speed at which prices reach fair value. Odean (1998) documented this directly in retail brokerage records.
- **Anchoring / confirmation bias**: Investors anchor on past prices and seek information confirming existing views, causing trends to persist beyond what the initial news warranted.
- **Herding**: Once a trend is established, other investors pile in, reinforcing the trend — which also seeds the eventual overreaction and long-term reversal.

**Why they keep losing:** these are not one-off mistakes but stable features of human decision-making under uncertainty, refreshed by every new market participant. Institutional constraints (quarterly benchmarking, "take profits" mandates, aversion to buying at 52-week highs) institutionalize the same behavior. Risk-based explanations (momentum as compensation for crash risk) have also been proposed and likely account for part of the premium, but the behavioral explanation remains more widely accepted.

## Null hypothesis

Under the null — prices follow a random walk and past returns carry no information about future returns:

- The expected return of winners-minus-losers (WML) is zero before costs and **negative after costs**, since the strategy's 100-300% annual turnover incurs pure transaction-cost drag with no offsetting signal.
- Decile spreads in any backtest would be statistical noise: roughly symmetric around zero across subperiods, markets, and asset classes, with no stable sign.
- The actual evidence rejects this null unusually strongly: a positive WML premium with t-statistics above 4 in the original U.S. sample, replicated out-of-sample *backward* (1801-1965, Geczy-Samonov), *forward* (post-1993 publication), and *sideways* (40+ countries, 8 asset classes, Asness-Moskowitz-Pedersen 2013). Data-mining alone cannot produce that pattern.
- The honest residual of the null: the premium has **shrunk post-publication** (U.S. long-short momentum has had long flat stretches since the 2000s), so the no-edge world and the crowded-edge world are getting harder to distinguish in recent samples. Position sizing should assume the forward premium is well below the historical 12%/year headline.

## Types of Momentum

### Cross-Sectional Momentum
The classic Jegadeesh-Titman approach: rank all assets in a universe by their past returns, go long the top quintile or decile, and short the bottom quintile or decile. This is a relative strategy -- it bets on which assets will outperform others, not on the market's overall direction.

### Time-Series Momentum (Trend Following)
Rather than comparing assets against each other, time-series momentum looks at each asset individually: go long if its own past return is positive, short if negative. Moskowitz, Ooi, and Pedersen (2012) showed that time-series momentum has been profitable across 58 liquid futures markets in a sample running from 1965 to 2009. This is closely related to [[trend-following]] strategies used by CTAs (commodity trading advisors) and managed futures funds.

### Dual Momentum
Popularized by Gary Antonacci, dual momentum combines both types: first, use time-series momentum to determine if stocks have positive absolute momentum (outperforming cash), then use cross-sectional momentum to choose between domestic and international equities. This approach seeks to capture upside momentum while avoiding bear markets.

## The Lookback Period

The choice of lookback period is critical. Research consistently shows:

- **1 month lookback**: Exhibits short-term reversal, not momentum. Stocks that rose sharply in the last month tend to mean-revert over the next month.
- **2-12 month lookback**: The sweet spot for momentum. The strongest effect appears at the 6-12 month horizon.
- **12 month with 1 month skip**: The most common academic specification. Using months 2-12 (skipping the most recent month) avoids the short-term reversal effect and has historically produced the strongest risk-adjusted returns.
- **Beyond 12-18 months**: Returns reverse. Long-term winners tend to underperform over the next 3-5 years, a phenomenon known as long-term reversal (related to [[mean-reversion]] and the value factor).

## Rules

**Universe and signal**
- Universe: liquid stocks only — e.g., S&P 500 or Russell 1000 constituents, or all stocks above $1B market cap and $10M median daily dollar volume. (Academic decile results include illiquid small caps that inflate the paper premium.)
- Signal: cumulative total return over months **t-12 to t-2** (12-month lookback, skipping the most recent month to avoid short-term reversal).

**Entry**
- At month-end, rank the universe by the signal. Buy the top decile (or top quintile for a more diversified, lower-turnover book) equal-weighted or volatility-weighted.
- Long-short variant: additionally short the bottom decile, sized to dollar or beta neutrality. Long-only investors simply hold the winner portfolio and avoid losers.

**Exit / rebalance**
- Rebalance monthly: sell holdings that fall out of the top decile/quintile, buy new entrants. A hold-band (e.g., sell only when a name drops below the top 20%) cuts turnover roughly in half for minimal signal loss.
- No discretionary exits — the rank IS the exit signal.

**Position sizing and risk management**
- Equal weight within the portfolio, capped at 5% per name; 30-100 names for adequate diversification.
- **Crash control (Daniel-Moskowitz / Barroso-Santa-Clara):** scale gross exposure by target volatility / realized strategy volatility (e.g., 12% target / trailing 6-month realized), and cut the short leg (or de-lever to 50%) when the trailing 24-month market return is negative AND market volatility is in its top quintile — the documented precondition for momentum crashes.

## Implementation pseudocode

```python
# Cross-sectional equity momentum, monthly rebalance, risk-managed
LOOKBACK, SKIP = 12, 1            # months: rank on t-12 .. t-2
TOP_PCT = 0.10                    # top decile
VOL_TARGET = 0.12                 # annualized target vol

def month_end_rebalance(universe, prices, market):
    # 1. Signal: 12-1 month return, liquid names only
    liquid = [s for s in universe
              if s.mcap > 1e9 and s.median_dollar_vol > 10e6]
    for s in liquid:
        s.signal = prices[s][-SKIP*21] / prices[s][-(LOOKBACK)*21] - 1

    # 2. Select winners (and losers for L/S variant)
    ranked  = sorted(liquid, key=lambda s: s.signal, reverse=True)
    longs   = ranked[: int(len(ranked) * TOP_PCT)]
    shorts  = ranked[-int(len(ranked) * TOP_PCT):]   # optional

    # 3. Crash guard: bear market + high vol => de-risk
    bear     = market.return_24m < 0
    high_vol = market.vol_percentile_63d > 0.80
    scale    = min(1.0, VOL_TARGET / strategy_realized_vol_6m())
    if bear and high_vol:
        scale *= 0.5
        shorts = []                # drop the short leg into the rebound risk

    # 4. Build equal-weight targets, 5% cap, trade the diff
    target = {s: min(scale / len(longs), 0.05) for s in longs}
    target.update({s: -min(scale / len(shorts), 0.05) for s in shorts})
    execute_to_target(target)      # monthly; use hold-band to cut turnover
```

The pseudocode mirrors the stated rules: 12-1 signal, decile selection, monthly rebalance, vol scaling, and the bear-plus-high-vol de-risking overlay that addresses momentum crashes.

## Indicators / data used

- **Total-return price history** (dividend-adjusted OHLCV, daily or monthly) — the only signal input; the strategy uses no fundamentals.
- **Point-in-time index constituents / delisting data** — essential for backtests; ignoring delistings materially inflates the short leg's paper returns (survivorship bias).
- **Corporate-actions data** (splits, dividends, spin-offs) for clean return computation.
- **Market-level inputs for the crash guard**: trailing 24-month index return and trailing realized volatility (63-day), per Daniel-Moskowitz; or strategy-level realized vol for Barroso-Santa-Clara scaling.
- **Liquidity fields** (market cap, median dollar volume) for universe filters.
- No indicators in the chartist sense are required, though practitioners sometimes proxy the signal with 52-week-high proximity or 12-month rate-of-change ([[indicators]]).

## Example trade

In January 2024, a momentum investor screens the S&P 500, ranking all 500 stocks by their total return from January 2023 to November 2023 (12 months minus 1 month skip). The top 50 stocks (decile 1) have average trailing returns of +45%; the bottom 50 average -15%. The investor buys an equal-weighted portfolio of the top 50 (2% per name on a $500k book, ~$10k per position) and rebalances monthly, replacing the handful of names that drop out of the decile each month.

Over the next 6 months, the momentum portfolio outperforms the equal-weighted S&P 500 by approximately 3-5% -- consistent with the historical premium, and in this particular period flattered by the persistence of the AI-hardware winners that dominated the 2023 ranking. Costs: roughly 20% of the book turns over across the 6 months; at ~10 bps round-trip all-in for S&P 500 names, the cost drag is ~2 bps on the book -- negligible at this size. The same trade at $5B would be a different conversation (see Capacity limits). In any given 6-month window, results vary widely; single-period outcomes say almost nothing about the strategy.

## Performance characteristics

All figures net-of-cost oriented, for the liquid large/mid-cap implementation — not the naive academic backtest:

- **Gross academic premium:** ~1% per month for the WML decile portfolio in the classic U.S. samples (Jegadeesh-Titman 1993; Ken French data library). This number is *not achievable*: it includes microcaps, ignores shorting costs, and predates crowding.
- **Net long-only tilt (realistic):** ~2-4%/year over the cap-weighted benchmark for a top-quintile large-cap portfolio, with tracking error of 4-8%. Live evidence: momentum index funds and the MSCI USA Momentum index have delivered positive but cyclical excess returns since the 1990s, with multi-year flat-to-negative stretches.
- **Net long-short:** Sharpe roughly **0.4-0.6 after costs** in liquid universes (frontmatter `expected_sharpe: 0.5`), down from ~0.8 gross in pre-2000 samples. Frazzini, Israel and Moskowitz (2015), using live AQR trading data, show realistic costs are far below earlier academic estimates and the strategy survives at multi-billion scale — but with a thinner margin.
- **Cost arithmetic:** turnover of 100-300%/year (long-short, both legs) against the net premium implies the strategy breaks even at roughly **50 bps round-trip** per trade (frontmatter `breakeven_cost_bps: 50`); large-cap implementation costs of 5-20 bps leave a positive but not luxurious margin. Small-cap implementations have a stronger signal and worse costs — roughly a wash.
- **Drawdown profile:** strongly negatively skewed. The academic WML portfolio lost ~91% in two months in 1932 and ~73% in three months in 2009 (Daniel-Moskowitz 2016). A risk-managed, vol-scaled long-short version historically cuts worst drawdowns to roughly 20-30%; long-only tilts draw down with the market plus tracking error. Frontmatter `expected_max_drawdown: 0.50` reflects the unmanaged long-short case.
- **Correlation properties:** roughly -0.3 to -0.5 correlation with the value factor — the basis of the value-momentum combination (Asness et al 2013).

## Capacity limits

Momentum is capacity-constrained by turnover, not by signal breadth:

- Korajczyk and Sadka (2004) estimated the equal-weighted U.S. equity momentum strategy's abnormal returns are eliminated at roughly **$5B** of strategy AUM, with liquidity-weighted versions surviving somewhat larger. Frazzini-Israel-Moskowitz (2015), using actual execution data, argue capacity is several times higher for patient, large-cap implementations. Frontmatter `capacity_usd: 5000000000` takes the conservative end.
- The constraint binds because the strategy demands liquidity at the same time as every other momentum follower: month-end rebalances into recent winners concentrate impact. Spreading execution over days and using hold-bands materially extends capacity.
- The **short leg saturates first** — bottom-decile names are smaller, harder to borrow, and more expensive to trade; institutional-scale programs typically run long-only or 130/30 partly for this reason.
- Crowding is the larger systemic issue (frontmatter `crowding_risk: high`): momentum is now harvested by factor funds, quant multistrats, and momentum ETFs simultaneously, and crowded unwinds (e.g., the August 2007 "quant quake") are themselves a capacity cost.

## Momentum Crashes

Momentum's Achilles heel is its vulnerability to sudden, severe drawdowns during market regime changes. The three most notable momentum crashes in U.S. equities:

1. **1932 (Great Depression rebound)**: As the market rebounded sharply from Depression lows, momentum's short portfolio (beaten-down stocks) surged while its long portfolio (prior winners) lagged. Daniel and Moskowitz (2016) report the academic WML portfolio lost approximately **91% in roughly two months** (July-August 1932).
2. **2009 (post-GFC rebound)**: After the 2008-2009 financial crisis, the most battered stocks (financials, cyclicals) rallied violently off the March 2009 low, while defensive stocks that had held up during the crash underperformed. The WML portfolio lost approximately **73% over about three months** (March-May 2009).
3. **2020 (vaccine rotation)**: A similar dynamic occurred in November 2020 when the Pfizer vaccine announcement (9 Nov 2020) triggered a massive single-day rotation out of work-from-home/growth momentum names into beaten-down value stocks — one of the worst single days on record for the momentum factor.

These crashes share a common pattern: they occur when the market abruptly reverses direction after a sustained decline, and the most extreme losers from the prior period violently outperform. The short side of momentum (high-beta-in-rebound, beaten-down stocks) snaps back with leveraged force -- in a rebound, the loser portfolio behaves like a call option on the market.

Daniel and Moskowitz (2016) showed that momentum crashes are partially predictable -- they tend to follow periods of high market volatility and occur when the market reverses from a sharp decline. This insight has led to risk-managed momentum strategies (volatility scaling per Barroso and Santa-Clara 2015; conditional de-risking per Daniel-Moskowitz) that substantially reduce crash exposure, and it is built into the Rules above.

## What kills this strategy

The most likely [[failure-modes]]:

1. **Momentum crashes** — the documented catastrophic mode (1932, 2009, Nov 2020). An unmanaged long-short book can lose half or more of its capital in weeks at the turn of a bear market. Mitigated, not eliminated, by vol scaling and the bear-market guard.
2. **Crowding and factor unwinds** — the premium is public, widely harvested, and periodically subject to correlated deleveraging (August 2007 quant quake). Each unwind is a drawdown; chronic crowding compresses the forward premium toward zero.
3. **Cost creep relative to a shrinking premium** — at 100-300% turnover, a premium that halves while costs stay fixed can flip net expectancy negative without any visible "event."
4. **Whipsaw / trendless regimes** — extended choppy markets (e.g., much of 2000-2010 for U.S. long-short momentum) generate turnover and losses with no trend to harvest.
5. **Behavioral abandonment** — buying all-time highs after a multi-year flat stretch is psychologically hard; investors quit at the bottom of the factor's own cycle, realizing the drawdown and missing the recovery.
6. **Implementation decay** — survivorship-biased backtests, ignored borrow costs on the short leg, and month-end execution into crowded prints make live results structurally worse than research.

## Kill criteria

For a live momentum allocation (numbers assume the risk-managed long-short variant; scale for long-only tilts):

- **Drawdown stop:** strategy drawdown exceeds **35%** despite the vol-scaling overlay → halt and re-evaluate; the crash controls have failed their design spec.
- **Premium-death test:** rolling **5-year** net Sharpe < 0 **while** the academic factor (e.g., Ken French UMD, gross) remains positive over the same window → implementation is broken (costs, execution, universe); fix or retire.
- **Factor-death test:** rolling **10-year** gross UMD factor return ≤ 0 across U.S. + international composites → the anomaly itself may be arbitraged away; retire rather than tinker (see [[when-to-retire-a-strategy]]).
- **Cost breach:** measured round-trip implementation cost exceeds **50 bps** (the breakeven in Performance characteristics) for 2 consecutive quarters → reduce turnover (hold-bands, quintiles not deciles) or retire.
- **Crowding red flag:** a one-month factor loss worse than **-15%** coinciding with broad quant-fund losses (unwind signature) → cut gross exposure 50% until factor vol normalizes below its 1-year median.

## Implementation and Monitoring Checklist

A consolidated process for deploying and running a momentum book:

**Before deployment**
1. **Clean the data.** Use point-in-time constituents and delisting returns — survivorship bias is the single most common way momentum backtests overstate the edge (see [[backtesting]]).
2. **Filter the universe for liquidity.** Drop names below the market-cap and dollar-volume floors; the academic decile premium leans on illiquid microcaps you cannot trade at scale.
3. **Cost-correct the backtest.** Apply realistic round-trip costs against 100-300% turnover. If the net premium does not clear the ~50 bps breakeven with margin to spare, do not deploy.
4. **Haircut the forward premium.** Assume it is well below the 12%/year historical headline — crowding has compressed it. Size for the crowded-edge world, not the 1990s world.
5. **Wire in the crash controls.** Vol-scaling to a target and the bear-market + high-vol de-risk rule are not optional; they are what make the drawdown survivable.

**Ongoing monitoring**
6. **Turnover and realised cost** — measure actual round-trip cost quarterly against the 50 bps breakeven.
7. **Rolling net Sharpe vs the gross academic factor (Ken French UMD)** — divergence flags an implementation problem (the premium-death test).
8. **Crash-precondition watch** — trailing 24-month market return and realised-vol percentile; tighten exposure as the documented crash setup appears.
9. **Crowding watch** — large single-month factor losses coinciding with broad quant-fund losses are the unwind signature.
10. **Behavioral discipline** — the hardest part is *not abandoning the strategy* during its normal multi-year flat stretches; pre-commit to the kill criteria so exits are mechanical, not emotional.

## Advantages

- **Strong academic evidence**: One of the most robust and well-documented anomalies in finance — two centuries of U.S. data, 40+ countries, out-of-sample persistence post-publication
- **Works across asset classes**: Demonstrated in equities, bonds, commodities, currencies, and crypto
- **Complementary to value**: Momentum and value are negatively correlated, making them powerful portfolio diversifiers when combined
- **Systematic and rules-based**: Can be fully automated with no subjective judgment, and is cheap to research (prices only, no fundamental data)
- **Crash risk is partially manageable**: the preconditions of momentum crashes are documented and the risk-managed variants have published, replicable fixes

## Disadvantages

- **Momentum crashes**: Severe, sudden drawdowns during market reversals — up to -91% (1932) and -73% (2009) for the unmanaged academic long-short portfolio
- **High turnover**: 100-300% annually generates significant transaction costs and tax inefficiency
- **Crowding risk**: Widespread adoption has plausibly eroded the premium; long flat stretches since the 2000s in U.S. long-short momentum
- **Difficult to short**: The short side contributes significantly to paper returns but is hard and expensive to implement live
- **Behavioral challenge**: Buying stocks at all-time highs feels psychologically uncomfortable, leading many investors to abandon the strategy at the wrong time
- **Premium is cyclical**: multi-year periods of underperformance are normal and indistinguishable in real time from permanent decay

## Sources

- Jegadeesh, N. and Titman, S. "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency." *Journal of Finance* (1993).
- Moskowitz, T., Ooi, Y.H., and Pedersen, L.H. "Time Series Momentum." *Journal of Financial Economics* (2012).
- Daniel, K. and Moskowitz, T. "Momentum Crashes." *Journal of Financial Economics* (2016).
- Barroso, P. and Santa-Clara, P. "Momentum Has Its Moments." *Journal of Financial Economics* (2015).
- Asness, C., Moskowitz, T., and Pedersen, L.H. "Value and Momentum Everywhere." *Journal of Finance* (2013).
- Geczy, C. and Samonov, M. "Two Centuries of Price-Return Momentum." *Financial Analysts Journal* (2016).
- Korajczyk, R. and Sadka, R. "Are Momentum Profits Robust to Trading Costs?" *Journal of Finance* (2004).
- Frazzini, A., Israel, R., and Moskowitz, T. "Trading Costs of Asset Pricing Anomalies" (AQR working paper, 2015).
- Antonacci, G. *Dual Momentum Investing* (2014).
- Odean, T. "Are Investors Reluctant to Realize Their Losses?" *Journal of Finance* (1998).

## Related

- [[trend-following]] -- time-series momentum applied primarily to futures
- [[momentum]] -- the broader concept of price persistence
- [[behavioral-finance]] -- the theoretical foundation for why momentum exists
- [[mean-reversion]] -- the opposite effect at longer horizons
- [[factor-investing]] -- momentum as a systematic risk factor
- [[risk-management]] -- managing the crash risk inherent in momentum strategies
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] -- methodology pages
- [[backtesting]] -- survivorship and delisting pitfalls specific to momentum research
- [[position-sizing]] -- sizing for the negatively-skewed crash profile
- [[risk-of-ruin]] -- why crash-control sizing is a survivability question
- [[kill-criteria]] -- the pre-committed exit thresholds
- [[kelly-criterion]] -- fractional sizing given the fat left tail
- [[tax-implications-trading]] -- the turnover-driven tax drag on a high-turnover book
