---
title: "Lottery Stock Anomaly"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [anomalies, lottery-effect, behavioral-finance]
aliases: ["Lottery Anomaly", "MAX Anomaly", "Lottery Preference"]
domain: [anomalies, behavioral-finance]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[low-volatility-anomaly]]", "[[low-vol-factor]]", "[[behavioral-finance]]", "[[edge-taxonomy]]", "[[options-trading-pitfalls]]"]
---

# Lottery Stock Anomaly

The empirical regularity that stocks with *lottery-like* payoff distributions — high probability of small loss, small probability of huge gain — systematically underperform on a risk-adjusted basis. Investors overpay for the lottery feature; the underperformance is the price they pay for the dream of a moonshot. Closely related to the [[low-volatility-anomaly|low-volatility anomaly]] but conceptually distinct: lottery stocks aren't just volatile, they're *positively skewed*.

## The Original Finding

**Source:** Bali, Cakici, Whitelaw (2011) "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns" — *Journal of Financial Economics*

The setup:
1. For each stock, compute the *maximum daily return* in the previous month (the "MAX" measure)
2. Sort stocks into deciles by MAX
3. The decile with the highest MAX (the most lottery-like stocks) is the "lottery" portfolio
4. Long the bottom decile, short the top decile

The result: the lottery portfolio underperformed the safe portfolio by approximately **1% per month**, with the result statistically significant and robust to controls for size, value, momentum, and standard volatility measures.

### The Anomaly at a Glance

| Dimension | Lottery Stocks (high MAX) | Non-Lottery Stocks (low MAX) |
|-----------|---------------------------|-------------------------------|
| Return distribution | Positively skewed (small loss, rare huge gain) | Roughly symmetric |
| Investor demand | Over-bought (people *want* the dream) | Fairly priced or unloved |
| Subsequent risk-adjusted return | Underperforms (~ -1%/month vs. low MAX) | Outperforms |
| Edge category ([[edge-taxonomy]]) | Behavioral | -- |
| Relationship to [[low-volatility-anomaly\|low-vol]] | High overlap; lottery is one driver | -- |
| How to trade it | Long-only: *avoid*. Long-short: short the top decile | -- |
| Main risk to the short | Short squeeze (a winner goes 3-10x) | -- |

## What It Says

Investors are not indifferent to the *shape* of return distributions. They prefer stocks with positive skew — small probability of a huge upside — even if the expected return is lower. This preference is rational given prospect theory (Kahneman & Tversky 1979), which predicts overweighting of low-probability gains.

The market does not fully arbitrage the preference because:
1. Many investors *want* the lottery feature for behavioral reasons
2. Shorting lottery stocks is dangerous — you can lose 200% if one of them goes 3x
3. Lottery stocks are often hard to short (low borrow availability)

## The Mechanism

The dominant theory is **prospect theory + lottery preferences**.

### Prospect Theory
Kahneman & Tversky's foundational result: people overweight low-probability outcomes, especially gains. A 1% chance of $1000 feels more attractive than its expected value of $10. This is rational under prospect theory's *probability weighting function* but irrational under expected utility.

Stocks with lottery-like payoffs (small but real chance of going 5x or 10x) are exactly what prospect theory predicts investors will overpay for.

### Skewness Preference
Beyond prospect theory, investors specifically prefer *positively skewed* return distributions. Three independent literatures support this:
- Survey evidence (people self-report preferring positive skew)
- Behavioral lab experiments
- Field evidence in lottery purchase patterns and the popularity of low-probability bets

### Coskewness Risk Premium
Some researchers argue lottery stocks have negative *coskewness* with the market — they pay off when the rest of your portfolio is doing well, so they're less valuable for risk management. The lottery underperformance is then a fair compensation for the negative coskewness.

In the [[edge-taxonomy]], lottery is **behavioral**.

## Replication Status

The lottery anomaly has been replicated:
- **Across countries** — Walkshäusl (2014) found the effect in Europe; subsequent papers confirmed in Asia and emerging markets
- **Across measures** — MAX, idiosyncratic skewness, expected idiosyncratic skewness all produce similar effects
- **Across decades** — pre and post the original 2011 publication

It is one of the more robust behavioral anomalies and has held up better than many post-publication.

## Lottery Stocks: Identification

What kind of stock has a lottery-like distribution? Characteristics:

- **Recent IPOs** — fresh names with high uncertainty and "story" appeal
- **Penny stocks** — small absolute price, percentage moves are large
- **Biotech** — binary FDA outcomes
- **Microcap miners** — exploration stories with binary outcomes
- **Crypto / token launches** — extreme positive skew
- **Meme stocks** — Reddit-driven momentum names
- **Small-cap tech with single-product risk**

A naive but effective lottery filter: stocks below $5, market cap below $500M, with at least one >20% daily return in the past 30 days. Or stocks where the highest daily return in the past month is more than 4x the average daily return.

## Connection to Other Anomalies

The lottery effect is one mechanism behind the broader [[low-volatility-anomaly|low-vol anomaly]] and the [[low-vol-factor|low-volatility factor]]:

- High-vol stocks tend to be lottery-like
- Investors overpay for them
- They underperform on a risk-adjusted basis
- The low-vol portfolio (which excludes them) outperforms

But the two are distinct: there are stocks with high volatility that are *not* lottery-like (e.g., evenly distributed but volatile names) and these don't show the lottery underperformance. Conversely, there are stocks with moderate volatility but heavy positive skew that *do* underperform.

The pure MAX effect is conceptually closer to skewness sorting than to volatility sorting, even though they're correlated empirically. Bali, Brown, Murray & Tang (2017) argued that the [[low-volatility-anomaly|low-vol]] / idiosyncratic-volatility puzzle is *substantially explained* by the lottery-demand (MAX) effect -- once you control for lottery demand, much of the idiosyncratic-volatility underperformance disappears. In that reading, lottery preference is the more fundamental behavioral driver, and the [[low-vol-factor]] partly inherits its premium.

| Anomaly | Sorting variable | Captures lottery? | Distinct from lottery? |
|---------|------------------|-------------------|------------------------|
| [[lottery-stock-anomaly\|Lottery / MAX]] | Max daily return / idio skew | Directly | -- |
| [[low-volatility-anomaly\|Idiosyncratic-vol]] | Total or residual volatility | Partly (vol & skew correlate) | Some high-vol names are symmetric |
| [[low-vol-factor\|Low-vol factor (BAB)]] | Beta / volatility | Partly | Leverage-constraint story is separate |
| Skewness factor | Realized / expected idio skew | Most precisely | -- |

## Variations

### Idiosyncratic Skewness
Sort by the *firm-specific* skewness of returns (residual after removing market beta). More precise than MAX but harder to estimate.

### Expected Idiosyncratic Skewness
Use a model to predict skewness from observable firm characteristics. Boyer, Mitton, Vorkink (2010) showed predicted skewness has stronger predictive power than realized skewness.

### Out-of-the-Money Call Demand
Stocks with high open interest in OTM calls relative to ATM calls signal lottery preference among options buyers. The underlying stocks subsequently underperform.

### Implied Volatility Skew
Stocks where the implied volatility curve is steeply *upward* sloping (right tail priced higher than left) often show subsequent underperformance.

### IPO Underperformance
Recent IPOs are heavily lottery-like. Loughran & Ritter (1995) documented that IPOs underperform the broader market in years 1-5, consistent with the lottery story.

### Meme Stock / Reddit Sentiment
A modern variant: stocks dominated by retail attention and Reddit hype (a proxy for lottery preference) systematically underperform fundamentals over multi-month horizons.

## Current Viability

The lottery anomaly is still tradeable. The Sharpe of a clean MAX-sort strategy in US equities is approximately 0.3-0.5, with stronger results in:
- Small caps
- International markets
- Periods of elevated retail participation (2020-2022 was a textbook example)

The effect has compressed somewhat with the rise of long-short factor ETFs that explicitly avoid lottery names, but it remains. Combining with momentum and quality screens improves the Sharpe further.

For long-only investors, the lesson is *avoid* the high-MAX names rather than try to short them. Equal-weighting the bottom 90% by MAX (excluding the top 10%) produces returns slightly higher than the broad market with materially lower volatility.

## Worked Example (Qualitative)

A factor investor runs a monthly MAX sort on the US equity universe.

**Step 1 -- Measure.** At month-end, for every stock compute the single largest daily return over the trailing ~21 trading days (the MAX measure). A microcap that printed a +38% day on a press release scores very high; a steady large-cap utility scores low.

**Step 2 -- Rank and bucket.** Sort all names into deciles by MAX. Decile 10 (highest MAX) is the lottery basket: it is dominated by recent IPOs, biotech ahead of readouts, [[meme stock|meme]]-adjacent small caps, and crypto-linked microcaps. Decile 1 is dull, low-skew names.

**Step 3 -- Form the view.** Prospect-theory demand should have pushed decile-10 prices *above* fair value, so their forward returns should lag. The investor expects decile 1 to beat decile 10 on a risk-adjusted basis over the next month.

**Step 4 -- Implement.** A long-short fund shorts decile 10 and goes long decile 1 (or buys a [[low-vol-factor]] proxy). A long-only investor simply *excludes* decile 10 from the buy list -- the safer and far more common implementation, since shorting lottery names is dangerous.

**Step 5 -- Manage the tail.** One decile-10 name doubles on a buyout rumor, generating a large mark-to-market loss on that short leg. Because the position was equal-weighted and small per name, the diversified basket still captures the average underperformance -- the edge is statistical across many names, not a bet on any single one.

**Step 6 -- What would invalidate it.** A regime of heavy retail speculation (e.g., 2020-2021) can extend lottery overvaluation for months before it reverts, producing painful interim drawdowns on the short leg. The edge is real but slow; it requires breadth and patience.

## Pitfalls in Trading the Lottery Anomaly

- **Shorting the basket naively.** A short lottery position has *unbounded* loss -- one name going 5x can wipe out a year of the strategy's edge. The anomaly is best harvested long-only (avoidance) or in a tightly risk-managed, broadly diversified short book. See [[options-trading-pitfalls]] for the parallel "buying OTM lottery tickets" mistake in options.
- **Borrow scarcity.** Lottery stocks are often hard to borrow, expensive to short, or subject to recall at the worst moment (a squeeze) -- exactly when the position is losing.
- **Crowding and decay.** The proliferation of factor ETFs that screen out lottery names has compressed the premium. Treat published Sharpe figures as upper bounds, not entitlements.
- **Confusing lottery with momentum.** Some high-MAX names are also strong momentum names. Sorting on MAX alone can inadvertently short winners; combine with momentum and quality screens to avoid fighting a durable trend.
- **Regime sensitivity.** During speculative manias the anomaly *reverses* short-term -- lottery names keep ripping. Position sizing must survive these stretches.
- **Liquidity and costs.** Decile-10 names are small, illiquid, and gap-prone. Realistic transaction costs and slippage can consume much of the paper edge; the net premium is meaningfully smaller than the gross.

## Strategies That Implement It

- [[low-volatility-anomaly]] — captures part of the lottery effect via volatility filtering
- [[multi-factor-portfolio|multi-factor portfolio]] — lottery as a quality screen

## Sources

- Bali, Cakici, Whitelaw (2011) "Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns" — *Journal of Financial Economics*
- Bali, Brown, Murray & Tang (2017) "A Lottery-Demand-Based Explanation of the Beta Anomaly" — *Journal of Financial and Quantitative Analysis* (lottery demand explains much of the low-beta / low-vol effect)
- Boyer, Mitton, Vorkink (2010) "Expected Idiosyncratic Skewness" — *Review of Financial Studies*
- Kumar (2009) "Who Gambles in the Stock Market?" — *Journal of Finance* (investor-level evidence of lottery preference)
- Kahneman & Tversky (1979) "Prospect Theory" — *Econometrica*
- Loughran & Ritter (1995) "The New Issues Puzzle" — *Journal of Finance*
- Walkshäusl (2014) — replication of the MAX effect in European equities
- [[book-thinking-fast-and-slow]] — Kahneman on prospect theory

## Related

- [[anomalies-overview]]
- [[low-volatility-anomaly]]
- [[low-vol-factor]]
- [[behavioral-finance]]
- [[prospect-theory]]
- [[edge-taxonomy]]
- [[options-trading-pitfalls]] — the options analogue: buying OTM "lottery tickets"
- [[skewness]]
