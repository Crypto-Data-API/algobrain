---
title: "Market Anomalies"
type: overview
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [anomalies, factors, academic-research, alpha]
aliases: ["Anomalies Library", "Market Inefficiencies"]
related: ["[[edge-taxonomy]]", "[[strategy-development-overview]]", "[[momentum-anomaly]]", "[[value-anomaly]]", "[[low-volatility-anomaly]]", "[[post-earnings-announcement-drift]]"]
---

# Market Anomalies

A library of documented, empirically-supported market inefficiencies — the academic literature on persistent (or formerly persistent) deviations from rational pricing. These anomalies are the *raw material* for producing trading strategies. Each one is a hypothesis about *why* prices behave a certain way, sourced to the academic paper that originally documented it. The strategies in [[strategies-overview]] are *implementations* of these anomalies; the anomalies themselves are the underlying claims about market behavior.

## Why a Library of Anomalies?

Every real trading strategy ultimately reduces to a claim that the market is mispricing something. The anomalies catalog answers: *what mispricings have been documented, and how robust are they?* A researcher building a new strategy can:

1. Check whether the underlying anomaly is already known (almost always the answer is yes)
2. Read the original paper to understand the *mechanism*
3. Check whether the anomaly has been replicated, contested, or decayed since publication
4. Build a strategy that captures the anomaly cleanly while avoiding the exhaustively-mined version

## How to Read the Catalog

Each anomaly page follows a consistent structure:

1. **What** — the empirical regularity claimed
2. **Original paper** — citation and year
3. **Mechanism** — the theoretical reason for the anomaly
4. **Edge category** — which of the six categories from [[edge-taxonomy]] (structural, behavioral, informational, analytical, latency, risk-bearing)
5. **Replication status** — has it been confirmed by independent researchers?
6. **Decay history** — has the Sharpe declined over time?
7. **Current viability** — is it still tradeable?
8. **Related strategies** — wiki strategies that implement it

## The Major Anomalies

The catalog is organized into six families. Each table lists the anomaly page, the empirical claim, the originating paper, the dominant [[edge-taxonomy|edge category]], and a rough viability note (see the [[#How Anomalies Decay|decay section]] for why most fade). "Viability" is a qualitative summary, not a guarantee — always read the individual page's decay history.

### Cross-Sectional Equity Anomalies

These rank stocks at a point in time and go long the top, short the bottom of a characteristic.

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[momentum-anomaly]] | Winners keep winning over 3-12 months | Jegadeesh & Titman 1993 | Behavioral | Survives; crash-prone |
| [[value-anomaly]] | High book-to-market stocks outperform | Fama & French 1992 | Behavioral / risk | Decayed but persistent |
| [[low-volatility-anomaly]] | Low-vol stocks have higher risk-adjusted returns | Haugen & Heins 1972; Frazzini & Pedersen 2014 | Structural (leverage constraints) | Robust |
| [[size-anomaly]] | Small caps outperform large caps | Banz 1981 | Risk / structural | Heavily decayed |
| [[quality-anomaly]] | Profitable, stable firms outperform | Novy-Marx 2013 | Analytical | Robust |
| [[investment-anomaly]] | Firms that invest less outperform | Cooper, Gulen, Schill 2008 | Behavioral | Moderate |
| [[accruals-anomaly]] | Firms with low accruals outperform | Sloan 1996 | Informational | Decayed post-publication |
| [[net-share-issuance]] | Issuers underperform; buyers-back outperform | Pontiff & Woodgate 2008 | Informational | Moderate |
| [[asset-growth-anomaly]] | Low asset-growth firms outperform | Cooper, Gulen, Schill 2008 | Behavioral | Moderate |
| [[idiosyncratic-volatility-anomaly]] | Low idiosyncratic-vol stocks outperform | Ang et al. 2006 | Behavioral | Contested |

### Time-Series Equity Anomalies

These are calendar or event-conditioned regularities in aggregate or single-name returns.

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[post-earnings-announcement-drift]] | Prices drift toward earnings surprise for 60+ days | Bernard & Thomas 1989 | Behavioral / informational | Survives in small caps |
| [[january-effect]] | Small caps outperform in January | Keim 1983 | Structural (tax-loss) | Largely decayed |
| [[turn-of-month-effect]] | Returns concentrate at last/first trading days | Ariel 1987 | Structural (flows) | Partially persistent |
| [[fomc-drift]] | Returns concentrate in 24h pre-FOMC | Lucca & Moench 2015 | Structural / informational | Persistent, capacity-limited |
| [[overnight-vs-intraday]] | Most returns happen overnight, not intraday | Cliff, Cooper, Gulen 2008 | Structural | Persistent |
| [[weekend-effect]] | Monday returns negative on average | French 1980 | Behavioral | Partially decayed |
| [[holiday-effect]] | Pre-holiday returns positive | Ariel 1990 | Behavioral | Weak / decayed |

### Macro and Cross-Asset

These apply across asset classes (rates, FX, commodities, equities) rather than within one.

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[time-series-momentum]] | Own past returns predict own future returns ≤12m | Moskowitz, Ooi, Pedersen 2012 | Behavioral | Robust; CTA staple |
| [[carry-anomaly]] | High-yielders outperform low-yielders cross-asset | Multiple | Risk-bearing | Robust; crash-prone |
| [[term-premium-anomaly]] | Long bonds underperform forward-implied returns | Fama & Bliss 1987 | Risk-bearing | Regime-dependent |
| [[currency-momentum]] | Momentum across currency pairs | Menkhoff et al. 2012 | Behavioral | Decayed |
| [[commodity-curve-rolls]] | Roll yield predicts futures returns | Erb & Harvey 2006 | Structural | Persistent |

### Behavioral / Sentiment

Rooted in systematic investor psychology and sentiment cycles (see [[behavioral-finance]]).

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[disposition-effect]] | Investors hold losers, sell winners | Shefrin & Statman 1985 | Behavioral | Persistent bias |
| [[overreaction-anomaly]] | Extreme losers reverse over 3-5 years | DeBondt & Thaler 1985 | Behavioral | Long-horizon, weak |
| [[investor-sentiment]] | High sentiment predicts low future returns | Baker & Wurgler 2006 | Behavioral | Persistent |
| [[lottery-stock-anomaly]] | Lottery-payoff stocks underperform | Bali, Cakici, Whitelaw 2011 | Behavioral | Persistent |
| [[max-anomaly]] | High max-daily-return stocks underperform next month | Bali et al. (related) | Behavioral | Persistent |
| [[ipo-underperformance]] | IPOs underperform market in years 1-5 | Ritter 1991; Loughran & Ritter 1995 | Behavioral | Persistent |

### Structural / Microstructure

Driven by predictable flows, constraints, and the structure of markets (see [[market-microstructure-overview]]).

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[index-inclusion-effect]] | Index additions rise around inclusion | Shleifer 1986 | Structural (flows) | Decayed as front-run |
| [[short-interest-anomaly]] | High-short-interest stocks underperform | Boehme, Danielsen, Sorescu 2006 | Informational | Persistent |
| [[options-implied-vol-skew]] | High put-call skew predicts declines | Xing, Zhang, Zhao 2010 | Informational | Moderate |
| [[volatility-risk-premium]] | Implied vol exceeds realized on average | Multiple | Risk-bearing | Robust; crash-prone |
| [[crash-fear-premium]] | Left-tail risk priced into options | Bollerslev, Todorov 2011 | Risk-bearing | Persistent |
| [[rebalancing-flows]] | Month/quarter-end rebalancing moves prices | — | Structural (flows) | Persistent, capacity-limited |

### Crypto-Specific

Younger literature; smaller samples and faster decay. See [[crypto]].

| Anomaly | Claim | Original paper | Edge category | Viability |
|---------|-------|----------------|---------------|-----------|
| [[crypto-momentum]] | Momentum effects in crypto returns | Liu & Tsyvinski 2018 | Behavioral | Strong but unstable |
| [[crypto-funding-rate-anomaly]] | Funding rates predict subsequent returns | — | Structural | Persistent, decaying |
| [[btc-weekend-effect]] | Weekend vs weekday returns differ in crypto | — | Structural | Weakening as TradFi enters |
| [[stablecoin-flow-anomaly]] | Stablecoin flows correlate with prices | — | Informational | Emerging |
| [[whale-wallet-anomaly]] | Large wallet movements predict price action | — | Informational | Noisy |

## How Anomalies Decay

The most important fact about academic anomalies: **most decay after publication**. McLean & Pontiff (2016) studied 97 published anomalies and found:

- The post-publication return is on average **26% lower** than the in-sample return
- About one-third of anomalies have effectively zero post-publication return
- Anomalies that are easier to trade decay faster than complex/illiquid ones

The reason: publication itself moves capital into the strategy. The smart money doesn't wait for the paper to be peer-reviewed; they read SSRN drafts and start trading. By the time the paper appears in the *Journal of Finance*, the easy money is gone.

This has direct implications for strategy research:

1. **Newly published anomalies** are *less* tradeable than they appear, because the in-sample period was the pre-publication, pre-arbitrage window
2. **Decades-old anomalies** that survive are usually either (a) constrained by capacity, (b) hard to trade, or (c) genuinely structural
3. **The frontier** is usually anomalies that are too small or too obscure to be worth a top-tier paper

## Combining Anomalies

A single anomaly produces a single source of edge with a finite Sharpe. Combining multiple uncorrelated anomalies produces a higher-Sharpe strategy by the fundamental law of active management.

Classic combinations:
- **Value + Momentum** (Asness, Moskowitz, Pedersen 2013) — these two have low correlation across asset classes; combined Sharpe is much higher than either alone
- **Value + Quality** (Asness, Frazzini, Pedersen 2019) — "quality value" or "QARP" outperforms naive value by avoiding value traps
- **Momentum + Low Vol** — stable momentum that avoids the highest-volatility names
- **Carry + Trend** — across asset classes, both well-documented, low correlation, complementary regimes (see [[regime-matrix]])

The most robust strategies tend to combine 3-5 anomalies. Single-anomaly strategies are more vulnerable to that anomaly's specific decay.

## Anomalies vs. Edges

**Anomaly:** an empirical regularity in returns that contradicts a baseline model (CAPM, EMH, etc.)
**Edge:** a tradeable expected return after costs and capacity

Most published anomalies are not full edges. They are gross-return regularities that may or may not survive transaction costs, financing, and crowding. The translation from "anomaly" to "edge" is the work of [[hypothesis-to-backtest-workflow|the strategy research process]].

## Anomalies by Edge Category

The same anomalies, re-indexed by the [[edge-taxonomy|six edge categories]] — useful when a researcher is hunting for a *type* of edge rather than a specific anomaly:

| Edge category | Why the edge exists | Representative anomalies |
|---------------|---------------------|--------------------------|
| **Behavioral** | Systematic investor psychology | [[momentum-anomaly]], [[overreaction-anomaly]], [[disposition-effect]], [[lottery-stock-anomaly]] |
| **Structural** | Constraints, mandates, predictable flows | [[low-volatility-anomaly]], [[index-inclusion-effect]], [[rebalancing-flows]], [[fomc-drift]] |
| **Informational** | Slow diffusion of public/private info | [[post-earnings-announcement-drift]], [[short-interest-anomaly]], [[accruals-anomaly]] |
| **Analytical** | Superior modeling of fundamentals | [[quality-anomaly]], [[value-anomaly]] (partly) |
| **Risk-bearing** | Compensation for bearing genuine risk | [[carry-anomaly]], [[volatility-risk-premium]], [[crash-fear-premium]], [[term-premium-anomaly]] |
| **Latency** | Speed advantage (HFT) | Mostly outside this catalog; see [[market-microstructure-overview]] |

A key diagnostic: behavioral and informational edges *should* decay after publication (capital arbitrages them away); structural and risk-bearing edges can persist because someone is structurally forced to be on the other side. This maps directly onto the [[#How Anomalies Decay|decay]] discussion.

## Hub: All Anomaly Pages

```dataview
TABLE status, updated, edge_category
FROM "wiki/concepts/anomalies"
WHERE type = "concept" AND file.name != "anomalies-overview"
SORT file.name ASC
```

(Anomaly sub-pages live under `wiki/concepts/anomalies/`. New pages added there appear here automatically.)

## The Honest Assessment

Of the 100+ documented equity anomalies, perhaps 10-15 are genuinely tradeable today after costs and crowding. The rest are either decayed, capacity-constrained, or were always overstated due to data-snooping at the time of publication. A productive research program studies the surviving ones carefully and looks for new variants in less-fished regions (small-cap, international, less-liquid asset classes, alt-data-derived signals).

## Sources

- McLean & Pontiff (2016) "Does Academic Research Destroy Stock Return Predictability?" — *Journal of Finance*
- Hou, Xue, Zhang (2020) "Replicating Anomalies" — *Review of Financial Studies*
- Harvey, Liu, Zhu (2016) "...and the Cross-Section of Expected Returns" — *Review of Financial Studies*
- [[book-asset-management-andrew-ang]] — Ang's textbook on factor investing
- [[book-expected-returns-antti-ilmanen]] — Ilmanen on cross-asset anomalies

## Related

- [[edge-taxonomy]] — the six-category framework used to classify each anomaly
- [[strategy-development-overview]] — turning anomalies into strategies
- [[hypothesis-to-backtest-workflow]] — the anomaly-to-edge translation process
- [[regime-matrix]] — which anomalies work in which regimes
- [[factor-investing]] — the practitioner packaging of cross-sectional anomalies
- [[data-snooping-and-p-hacking]] — why most published anomalies are overstated
- [[behavioral-finance]] — the source of behavioral anomalies
- [[market-microstructure-overview]] — the source of structural/microstructure anomalies
- [[strategies-overview]] — implementations of these anomalies
