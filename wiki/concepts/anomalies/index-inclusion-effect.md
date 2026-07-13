---
title: "Index Inclusion Effect"
type: concept
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [anomalies, index-inclusion, structural, market-microstructure]
aliases: ["Index Effect", "Index Reconstitution", "S&P 500 Inclusion"]
domain: [anomalies, market-microstructure]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[index-arbitrage]]", "[[etf-arbitrage]]", "[[edge-taxonomy]]"]
---

# Index Inclusion Effect

The empirical regularity that stocks added to major indices (S&P 500, Russell 1000, MSCI) experience a price increase around the announcement and effective date of inclusion, while stocks deleted experience a price decrease. The textbook example of a *structural* anomaly: the price moves are caused by mechanical buying from index funds that are *forced* to track the index, regardless of the stock's fundamentals. One of the cleanest empirical demonstrations of demand-curve slopes in equity markets, and the basis of index arbitrage strategies.

## The Original Finding

**Source:** Shleifer (1986) "Do Demand Curves for Stocks Slope Down?" — *Journal of Finance*

The setup:
1. Identify dates when stocks were added to or deleted from the S&P 500
2. Compute returns around the announcement date and the effective date (the day the index actually changes)
3. Compare to a matched control group

The result: added stocks experienced approximately **3% abnormal returns** between announcement and effective date, with most of the move happening immediately after announcement. Deleted stocks experienced symmetric negative returns.

This was the first clean empirical evidence that stock demand curves *slope downward* — that is, that buying pressure from non-fundamental sources can move prices. Standard finance theory before Shleifer assumed perfectly elastic demand (prices set by fundamentals only). The index inclusion effect proved otherwise.

## What It Says

When index funds buy a stock because it was added to their tracked index, the price goes up *not because the stock's fundamentals changed* but because the buying pressure is non-fundamental. A passive fund tracking the S&P 500 must buy the new addition; if all the fund is doing so simultaneously, they collectively move the price.

The size of the effect is roughly proportional to the size of the index funds' aggregate AUM relative to the market cap of the stock being added. Smaller stocks added to large-cap indices experience larger effects than larger stocks.

## The Mechanism

The mechanism is uncomplicated and mechanical:

1. Index providers (S&P, MSCI, Russell, FTSE) periodically rebalance their indices
2. Inclusion or deletion is announced 1-5 days before the effective date
3. Index fund managers must trade to match the new index composition by the effective date
4. The buying (or selling) pressure moves the price
5. The price reverts partially after the rebalancing flow ends

In the [[edge-taxonomy]], this is **structural** — a forced flow from non-discretionary participants (index funds tracking a benchmark).

## Replication Status

The index inclusion effect has been replicated:
- **S&P 500** — multiple papers from 1986 to present
- **Russell indices** — Russell 1000, Russell 2000 reconstitutions show large effects
- **MSCI indices** — international equivalent
- **FTSE indices** — UK and global equivalents
- **Bond indices** — Bloomberg Aggregate, Bloomberg Treasury show smaller but similar effects
- **Across decades** — robust from 1980s through 2010s, with declining magnitude

The effect is one of the most empirically demonstrated anomalies in finance.

## The Decay

The S&P 500 inclusion effect has decayed substantially since publication:

- 1980s-1990s: ~3-5% abnormal return around inclusion
- 2000s: ~1-2%
- 2010s onward: ~0.5-1%
- Some recent samples: indistinguishable from zero

The decay has multiple causes:

1. **Pre-positioning** — arbitrageurs now buy ahead of expected announcements, compressing the post-announcement move
2. **More transparency** — S&P 500 inclusion criteria are public, making predictions easier
3. **Smarter index funds** — modern index funds use trade impact-minimizing execution strategies (spread purchases over time, use closing auctions, etc.)
4. **Faster arbitrage capital** — the gap between announcement and effective date is now fully arbitraged

The effect persists more strongly in *less popular* indices (e.g., Russell 2000, MSCI emerging markets) where pre-positioning is less efficient. It also persists in *forced exits* from indices, which can produce sharp downward moves.

## Variations

### Predicted Inclusions
Build a model to predict which stocks will be added to an index *before* the announcement. The Sharpe of a "predicted inclusions" portfolio is much higher than the post-announcement strategy because you capture the pre-positioning move. This is the modern version of index arbitrage.

### Russell Reconstitution
Russell rebalances its indices once a year (June). The reconstitution is highly mechanical (rank by market cap, top 1000 = R1000, top 3000 = R3000, etc.). Predictable and historically very tradeable. The effect has shrunk but remains.

### Bond Index Inclusions
When a country is added to or removed from major bond indices (e.g., emerging markets indices), foreign capital flows in or out mechanically. The flows are larger than the stock equivalent because emerging market bonds are less liquid.

### China A-Share MSCI Inclusion
A famous recent example: MSCI's 2018 inclusion of China A-shares triggered ~$15B of mechanical buying. The effect was largely priced in before inclusion as market participants anticipated the flow.

### Spin-off Forced Selling
When a spinoff results in a stock that's too small or wrong-sector for the index, index funds must sell. The spinoff stock often experiences large negative returns purely from forced selling, which then mean-reverts.

## Current Viability

The basic announcement-effect strategy is mostly dead. Anyone running it today is competing against high-frequency arbitrageurs who pre-position immediately on the news.

What still works:
- **Predicting inclusions** — building models for which stocks will be added at the next rebalance, then buying ahead of the announcement
- **Less-watched indices** — Russell 2000, MSCI emerging markets, sector indices
- **Forced sells** — spinoffs, deletions, sub-index migrations
- **Bond index flows** — slower to arbitrage, larger relative impacts

The Sharpe of these residual strategies is modest (0.2-0.5) and capacity is limited (a single rebalance only happens a few times a year). But the underlying structural mechanism — mandatory flows from passive funds — hasn't disappeared and isn't going to.

## The Theoretical Importance

Beyond its tradeable implications, the index inclusion effect is *theoretically* important. It demonstrates:

1. **Demand curves for stocks slope down** — non-fundamental buying moves prices
2. **The market is not perfectly efficient** — passive flows have measurable price impact
3. **Capital structure (active vs. passive) matters** — the rise of passive investing has direct price-formation effects
4. **Forced flows are predictable** — and therefore tradeable

These observations have shaped how academic finance thinks about market efficiency and price formation. The pure-fundamentals view of price-setting was clearly wrong by 1986; subsequent decades have produced more evidence that flows matter.

## Strategies That Implement It

- [[index-arbitrage]] — direct implementation
- [[etf-arbitrage]] — related ETF creation/redemption flows
- [[expiration-and-rebalancing-flows]] — broader rebalancing flow strategy
- [[structural-forced-selling]] — exploits forced exits

## Sources

- Shleifer (1986) "Do Demand Curves for Stocks Slope Down?" — *Journal of Finance*
- Harris & Gurel (1986) — early replication
- Beneish & Whaley (1996) — S&P 500 game updates
- Chen, Noronha, Singal (2004) — long-term price effects
- Madhavan (2003) — Russell rebalance effects
- [[book-the-quants]] — broader context on structural anomalies

## Related

- [[anomalies-overview]]
- [[index-arbitrage]]
- [[etf-arbitrage]]
- [[expiration-and-rebalancing-flows]]
- [[structural-forced-selling]]
- [[edge-taxonomy]]
