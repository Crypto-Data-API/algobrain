---
title: "Short Interest Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, market-microstructure, stocks, quantitative]
aliases: ["Short Interest Anomaly", "High Short Interest Underperformance", "Short Ratio Anomaly"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[short-interest]]", "[[short-selling]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[short-interest]]", "[[idiosyncratic-volatility-anomaly]]", "[[lottery-stock-anomaly]]", "[[market-microstructure]]"]
---

# Short Interest Anomaly

Stocks with high short interest — particularly when short interest is growing — subsequently underperform the market by a wide margin. The anomaly represents informed selling: short-sellers are a self-selected, sophisticated group, and their collective willingness to pay borrowing costs to maintain short positions is one of the most informative public signals about which stocks are overvalued.

## What

Sort stocks monthly by short interest ratio (shares shorted / shares outstanding) or by days-to-cover (short interest / average daily volume). Long the lowest-short-interest decile, short the highest-short-interest decile. Boehme, Danielsen, Sorescu (2006) reported a ~1% monthly spread (~12% annualized) in the hedged portfolio, with most of the alpha coming from the short leg. Ranked over days-to-cover, the spread is even larger.

## Original Papers

- Asquith, Pathak, Ritter (2005) "Short Interest, Institutional Ownership, and Stock Returns" — *Journal of Financial Economics*
- Boehme, Danielsen, Sorescu (2006) "Short-Sale Constraints, Differences of Opinion, and Overvaluation" — *Journal of Financial and Quantitative Analysis*
- Cohen, Diether, Malloy (2007) "Supply and Demand Shifts in the Shorting Market" — *Journal of Finance*

## Mechanism

- **Informed short-sellers** — short-selling is expensive (borrow fees, margin requirements, unlimited downside risk), so only investors with strong convictions take meaningful short positions. Cohen-Diether-Malloy show that *shifts* in shorting demand are more informative than *levels*, supporting the informed-trader interpretation.
- **Limits to arbitrage / overpricing persistence** — the Miller (1977) model says that when optimists set the price and pessimists can't short (or face high borrow costs), stocks are systematically overpriced. High short interest indicates the borrow market is clearing at high cost, which indicates unusually elevated pessimist interest.
- **Feedback loop** — high short interest increases borrow cost, which deters arbitrage, which allows further overpricing.

## Edge Category

**Informational** (following sophisticated traders) + **structural** (limits to arbitrage amplify).

## Replication Status

Replicated across markets and time periods. Cohen-Diether-Malloy's shifts-in-demand refinement is particularly robust.

## Decay History

Moderate decay since publication as more funds incorporate short-interest data into their models. The raw signal has weakened, but the refined versions (days-to-cover, changes in short interest, cost-of-borrow) remain effective.

## Current Viability

Tradeable as:

- **A long-only screen** — avoid or underweight stocks with high or rising short interest
- **A factor overlay** — short interest is a common ingredient in composite quality/mispricing scores
- **A direct long-short strategy** — implementable but capacity-constrained by the high borrow costs it is based on

**Risk:** meme-stock short squeezes (e.g. GME 2021) are tail events in which high-short-interest stocks rally violently. The anomaly is not risk-free and concentrated positioning can blow up.

## Related Strategies

- [[idiosyncratic-volatility-anomaly]] — related limits-to-arbitrage mechanism
- [[lottery-stock-anomaly]] — overlapping clientele
- Short-book construction in factor hedge funds
- Cost-of-borrow-based alpha signals

## Sources

- Asquith, Pathak, Ritter (2005)
- Boehme, Danielsen, Sorescu (2006)
- Cohen, Diether, Malloy (2007) "Supply and Demand Shifts in the Shorting Market"
- Drechsler & Drechsler (2014) "The Shorting Premium"
- Miller (1977) "Risk, Uncertainty, and Divergence of Opinion"

## Related

- [[anomalies-overview]]
- [[idiosyncratic-volatility-anomaly]]
- [[lottery-stock-anomaly]]
- [[market-microstructure]]
