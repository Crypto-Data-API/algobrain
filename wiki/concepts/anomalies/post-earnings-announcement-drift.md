---
title: "Post-Earnings Announcement Drift"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [anomalies, earnings, behavioral-finance, post-earnings-drift]
aliases: ["PEAD", "Earnings Drift", "Bernard-Thomas Drift"]
domain: [anomalies, behavioral-finance]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[earnings-momentum]]", "[[earnings]]", "[[earnings-revision]]", "[[edge-taxonomy]]"]
---

# Post-Earnings Announcement Drift

The empirical regularity that stocks which beat earnings expectations continue to outperform for 60+ days after the announcement, while stocks that miss continue to underperform. The longest-documented behavioral anomaly in finance and one of the few that has *partially* survived decades of arbitrage. The most studied evidence of slow information diffusion and underreaction in equity markets.

## The Original Finding

**Source:** Bernard & Thomas (1989, 1990) "Post-Earnings Announcement Drift: Delayed Price Response or Risk Premium?" and follow-up papers — *Journal of Accounting Research*

The setup:
1. For each quarterly earnings announcement, compute the *earnings surprise* (actual EPS minus expected EPS, scaled by some volatility measure)
2. Sort stocks into deciles based on the surprise
3. Form portfolios long the top decile (positive surprises) and short the bottom decile (negative surprises)
4. Hold for 60-90 days

The result: this portfolio earned approximately **2-4% over the 60-day holding period**, with the effect concentrated in the immediate weeks but persisting for months. The strategy was profitable in nearly every sub-period from 1974-1986.

The original Bernard-Thomas measure used "Standardized Unexpected Earnings" (SUE) — the surprise divided by the standard deviation of historical surprises.

## What It Says

When companies report earnings that beat (or miss) expectations, the immediate price reaction *underreacts*. The full repricing happens gradually over the following weeks and months. An investor who buys winners and shorts losers immediately after the announcement captures the residual drift.

This is a *direct contradiction* of the semi-strong efficient market hypothesis. EMH says that publicly announced earnings should be fully reflected in price within minutes. Bernard-Thomas showed they're not — they take *weeks*.

## The Mechanism

Several behavioral theories:

### 1. Anchoring on Past Earnings
Investors anchor on the trajectory of historical earnings and treat surprises as transient noise. They under-update their expectations even when the surprise is large and persistent. Subsequent earnings reports continue to surprise in the same direction, and the price gradually catches up.

### 2. Limited Attention
Many investors don't pay attention to earnings reports immediately. Information diffuses to them over days to weeks via news coverage, analyst reports, and portfolio rebalancing. The slower diffusion produces the gradual repricing.

Hong, Lim, Stein (2000) showed that PEAD is *stronger* in stocks with low analyst coverage, consistent with the limited-attention story. Less-watched stocks have slower information diffusion.

### 3. Risk Compensation (Disputed)
Some authors argued the drift was compensation for risk. Bernard and Thomas explicitly rejected this in their original paper, showing that the post-announcement returns were too large and too systematic to be a risk premium.

### 4. Conservatism Bias
Investors update their beliefs too slowly relative to Bayesian rationality. Earnings surprises trigger small belief updates that should be larger; the gap is closed gradually as more information arrives.

In the [[edge-taxonomy]], PEAD is a clear **behavioral edge**. The losers are investors who underreact to public earnings announcements.

## Replication Status

PEAD has been replicated:
- **Over multiple decades** — the original 1989 paper used 1974-1986 data, and the effect persisted in 1986-2000 and beyond
- **Internationally** — Hew et al. (2017) found PEAD in European, Japanese, and other international markets
- **Across firm sizes** — strongest in small caps but present in all sizes
- **Across measures of surprise** — SUE, analyst-estimate-based surprises, revenue surprises

It is one of the most robust anomalies in the literature.

## Decay History

PEAD has decayed somewhat but not as dramatically as some other published anomalies:
- 1974-1986 (original sample): ~3-4% per 60 days
- 1990s: ~2-3% per 60 days
- 2000s: ~1.5-2% per 60 days
- 2010s onward: closer to 1% per 60 days, with significant noise

The decay is consistent with arbitrage capital flowing into the strategy. The effect persists because (a) the underlying behavioral cause hasn't gone away — investors still anchor — and (b) the strategy is *capacity constrained* (you have to trade thousands of small to mid-cap names quickly around earnings dates).

## Where the Effect Is Strongest

PEAD is not uniform across firms. It's concentrated in:

1. **Small caps** — less analyst coverage, slower information diffusion
2. **Stocks with low institutional ownership** — fewer arbitrageurs
3. **Less-followed industries** — fewer specialist analysts
4. **Surprises in the same direction as recent surprises** — momentum compounds with PEAD
5. **Surprises accompanied by analyst revisions** — when sell-side analysts also start updating, the drift is stronger

A targeted PEAD strategy focuses on these high-effect subsets rather than blanketing the whole universe.

## Variations

### Earnings Revision Drift
Instead of the surprise on announcement day, use the *trajectory of analyst earnings revisions*. Stocks with rising estimates outperform; stocks with falling estimates underperform. Partially overlaps with PEAD but has its own dynamics. See [[earnings-revision]].

### Revenue Drift
Revenue surprises drift similarly to EPS surprises and are less subject to GAAP accounting tricks. Some research suggests revenue PEAD is more robust.

### Sales Growth Drift
Acceleration in sales growth predicts subsequent returns over multi-quarter periods. A slower-moving variant.

### Conference-Call Sentiment
Use NLP on earnings conference calls to extract management sentiment. Combines with PEAD by adding qualitative information not in the headline numbers.

### Analyst-Whisper Drift
Use the gap between official consensus and "whisper" estimates as a refinement of the surprise measure.

## Current Viability

PEAD is one of the *most* viable behavioral anomalies as of 2024-2026. The Sharpe of a simple PEAD strategy in US equities is around 0.4-0.6 after costs, with the right targeting (small caps, low analyst coverage, persistent surprises) potentially higher.

The strategy is capacity-constrained — you can't run it at $10B because you can't trade enough small caps fast enough — but at $10M-$500M it remains robustly profitable.

The right implementation:
1. Use a clean earnings surprise definition (SUE or analyst-based)
2. Filter to liquid-enough names that you can actually trade
3. Enter immediately after the announcement (delay reduces the edge linearly)
4. Hold for 30-60 days
5. Combine with related signals (revisions, conference call sentiment) for stronger conviction

## Strategies That Implement It

- [[earnings-momentum]] — direct PEAD implementation
- [[earnings-revision]] — closely related drift on revisions
- [[news-trading]] — broader event-driven framework
- [[event-driven-trading]]

## Sources

- Bernard & Thomas (1989) "Post-Earnings-Announcement Drift" — *Journal of Accounting Research*
- Bernard & Thomas (1990) "Evidence That Stock Prices Do Not Fully Reflect the Implications of Current Earnings for Future Earnings" — *Journal of Accounting and Economics*
- Hong, Lim, Stein (2000) "Bad News Travels Slowly" — *Journal of Finance*
- Hong & Stein (1999) "A Unified Theory of Underreaction, Momentum Trading, and Overreaction" — *Journal of Finance*
- [[book-quantitative-equity-portfolio-management]]

## Related

- [[anomalies-overview]]
- [[earnings-momentum]]
- [[earnings]]
- [[earnings-revision]]
- [[edge-taxonomy]]
- [[momentum-anomaly]]
