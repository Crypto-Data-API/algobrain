---
title: "Fundamental Analysis"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [fundamental-analysis, valuation, event-driven]
aliases: ["Fundamentals-Based Trading"]
related: ["[[strategies-overview]]", "[[technical-analysis-overview]]", "[[quantitative-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[technical-vs-fundamental-analysis]]", "[[benjamin-graham]]"]
---

# Fundamental Analysis

Fundamental analysis is the family of strategies that determine what an asset is worth based on its underlying economic reality — earnings, revenue growth, cash flow, competitive position, and macroeconomic environment (Source: [[book-security-analysis]]). While technical analysis asks "what is the market doing?", fundamental analysis asks "what should the market be doing?" — and the gap between the two is where fundamentals-based traders find opportunity. The discipline was formalized by [[benjamin-graham]] and David Dodd in the 1930s and has been extended by practitioners ranging from [[philip-fisher]]'s qualitative "scuttlebutt" approach (Source: [[book-common-stocks-and-uncommon-profits]]) to [[william-o-neil]]'s growth-oriented CANSLIM system (Source: [[book-how-to-make-money-in-stocks]]).

## What Distinguishes This Family

- **Edge sources** (see [[edge-taxonomy]]): primarily *analytical* (better valuation work, deeper accounting analysis, superior macro framework) and *behavioral* (the market systematically overreacts to bad news and underreacts to fundamental improvement — the engine behind value, contrarian, and post-earnings-drift effects). Event-driven variants add *risk-bearing* edge: getting paid to hold deal-break or credit risk others must shed.
- **Typical timeframes**: the slowest category in the catalog — weeks to years. Even the "fast" variants (earnings, news, policy shocks) trade catalysts measured in days, not minutes. Fundamental theses need time for price to converge to value.
- **Capital and data requirements**: works at retail scale with free filings, earnings transcripts, and macro releases, but the institutional version layers on point-in-time fundamentals databases, expert networks, and alternative data. Position sizing must survive long convergence periods and mark-to-market pain; leverage is the classic killer of correct-but-early fundamental trades.
- **Who it suits**: patient traders comfortable with accounting and valuation, willing to do research that pays off over quarters rather than sessions, and able to hold against price action when the thesis is intact. It does not suit anyone who needs frequent feedback or cannot tolerate being early.

## Strategies in This Category

### Equity Styles

- [[value-investing-strategy]] — Buying assets below intrinsic value with a margin of safety, in the Graham tradition
- [[growth-investing-strategy]] — Paying up for businesses compounding revenue and earnings faster than the market expects
- [[contrarian-investing]] — Buying what the consensus has abandoned, on evidence of overreaction
- [[dividend-investing]] — Building income portfolios around sustainable, growing dividend payers
- [[dividend-capture]] — Short-hold trades around ex-dividend dates to collect the payout
- [[esg-investing]] — Screening and tilting portfolios on environmental, social, and governance factors
- [[long-short-equity]] — Pairing fundamentally cheap longs against expensive shorts to isolate stock-picking skill
- [[earnings-momentum]] — Trading the post-earnings-announcement drift: beats keep outperforming
- [[sector-rotation]] — Shifting capital between industries as the economic cycle progresses

### Event-Driven & Catalyst

- [[event-driven-trading]] — The umbrella approach: trading identifiable corporate and macro catalysts
- [[merger-arbitrage]] — Capturing the spread between a target's price and the announced deal price
- [[convertible-arbitrage]] — Long converts hedged with short stock, monetizing embedded optionality and credit
- [[news-trading]] — Positioning around scheduled and breaking news with a fundamental read on impact
- [[crypto-policy-shock-trading]] — Trading regulatory and policy surprises in crypto markets

### Macro, Commodity & Spread

- [[yield-curve-trading]] — Positioning on changes in the shape of the interest-rate curve
- [[crack-spread]] — Trading the refining margin between crude oil and its products
- [[crush-spread]] — Trading the processing margin between soybeans, meal, and oil
- [[spark-spread]] — Trading the margin between natural gas cost and electricity prices
- [[geographic-spread-trading]] — Exploiting regional price differentials in the same commodity
- [[seasonal-spread-trading]] — Calendar spreads driven by recurring supply/demand seasonality
- [[emissions-trading]] — Trading carbon allowance markets (EUA, CCA) on policy and compliance fundamentals
- [[weather-derivatives]] — Hedging and speculating on temperature and weather outcomes

## Start Here

- [[earnings-momentum]] — trading the post-earnings drift anomaly
- [[sector-rotation]] — cycling through sectors as the economy expands and contracts
- [[merger-arbitrage]] — profiting from announced M&A deals

## All Pages in This Folder

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/fundamental-analysis"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Comparisons

- [[technical-vs-fundamental-analysis]] — side-by-side comparison of fundamental and technical approaches

## Key Topics to Cover

- Financial statement analysis
- Valuation methods (DCF, P/E, P/B)
- Earnings reports and guidance
- Macro economic indicators
- Sector analysis
- On-chain fundamentals (crypto)

## Related

- [[strategies-overview]] — parent catalog of all strategy categories
- [[technical-analysis-overview]] — the price-action counterpart; many traders fuse the two ([[fundamental-technical-fusion]])
- [[quantitative-overview]] — systematic implementations of fundamental factors (value, quality)
- [[position-trading-overview]] — the timeframe category where most fundamental theses live
- [[edge-taxonomy]] — why analytical and behavioral edges persist in fundamentals
- [[regime-matrix]] — which fundamental styles work in which market regimes

## Sources

- [[book-security-analysis]] — Graham & Dodd's foundational text that formalized security analysis as a discipline
- [[book-the-intelligent-investor]] — Graham's accessible guide to fundamental investing principles and margin of safety
- [[book-common-stocks-and-uncommon-profits]] — Fisher's qualitative approach to evaluating growth companies
- [[book-one-up-on-wall-street]] — Lynch's practical guide to finding fundamentally strong stocks
- [[book-how-to-make-money-in-stocks]] — O'Neil's CANSLIM system combining fundamental and technical analysis
- [[book-a-random-walk-down-wall-street]] — Malkiel's critique of active fundamental analysis and case for efficient markets
