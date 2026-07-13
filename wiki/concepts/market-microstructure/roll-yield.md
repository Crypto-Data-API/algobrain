---
title: "Roll Yield"
type: concept
created: 2026-04-14
updated: 2026-06-11
status: good
tags: [commodities, futures, market-microstructure]
aliases: ["Roll Return", "Rolling Yield"]
related: ["[[contango]]", "[[backwardation]]", "[[futures-overview]]", "[[convenience-yield]]", "[[cost-of-carry]]", "[[carry-anomaly]]"]
domain: market-microstructure
prerequisites: ["[[contango]]", "[[backwardation]]", "[[futures-overview]]"]
difficulty: intermediate
---

Roll yield is the return (positive or negative) generated when a futures position is "rolled" — that is, when an expiring near-month contract is closed and a new position is opened in a further-dated contract. It is one of the three components of total return in a futures-based investment, alongside spot price changes and collateral yield.

## How Roll Yield Works

Futures contracts expire on fixed dates, so any investor maintaining ongoing exposure must periodically sell the expiring contract and buy the next one. The roll yield arises from the price difference between the two contracts:

**Roll Yield ≈ (Near Price - Far Price) / Far Price**

- In [[backwardation]] (near price > far price), rolling generates **positive roll yield**. The investor sells the more expensive near contract and buys the cheaper far contract — effectively buying low and selling high with each roll.
- In [[contango]] (near price < far price), rolling generates **negative roll yield**. The investor sells the cheaper near contract and buys the more expensive far contract — a persistent headwind to returns.

The magnitude of roll yield depends on how steep the futures curve is and how frequently the position is rolled (Source: [[2026-04-14-commodities-research-framework]]).

## Impact on Commodity ETFs

Roll yield is the dominant driver of long-term return divergence between commodity futures-based products and spot prices. Commodity ETFs like USO (crude oil) and DBC (broad commodities) must continuously roll their futures holdings:

- **USO** historically suffered severe negative roll yield during prolonged [[contango]] periods in crude oil, causing the ETF to dramatically underperform the spot price of [[crude-oil]] over multi-year horizons.
- **DBC** diversifies across multiple commodities, partially mitigating roll yield drag by including commodities that may be in [[backwardation]].

Investors who look only at spot price charts can be misled about the actual returns available from futures-based commodity exposure (Source: [[2026-04-14-commodities-research-framework]]).

## Commodity Curve Roll Anomaly

Research by Erb and Harvey demonstrates that backwardated commodities have historically outperformed contangoed commodities — the so-called [[commodity-curve-rolls|commodity curve roll anomaly]]. A strategy that goes long backwardated commodity futures and short (or avoids) contangoed futures has generated positive excess returns over decades.

This anomaly is closely related to the [[carry-anomaly]], where the "carry" in commodity futures is essentially the roll yield. The economic logic is that [[backwardation]] often reflects a [[convenience-yield]] premium paid by consumers willing to pay up for immediate physical supply, and this premium accrues to futures investors on the other side (Source: [[2026-04-14-commodities-research-framework]]).

## Relationship to Carry and Storage

Roll yield is intimately connected to the [[cost-of-carry]] framework. In theory, the futures price should equal the spot price plus storage costs, financing costs, and insurance, minus the [[convenience-yield]]. When convenience yield dominates (typically during tight physical markets), the curve inverts into [[backwardation]] and roll yield turns positive. When [[storage-economics|storage costs]] dominate (abundant supply, cheap storage), [[contango]] prevails and roll yield turns negative.

[[trend-following-cta|Trend-following CTAs]] and other systematic commodity traders monitor roll yield as a signal — persistent positive roll yield can indicate structural tightness in a commodity market, while widening contango may signal oversupply.

## Related

- [[contango]]
- [[backwardation]]
- [[commodity-curve-rolls]]
- [[carry-anomaly]]
- [[convenience-yield]]
- [[storage-economics]]
- [[cost-of-carry]]
- [[trend-following-cta]]
- [[futures-overview]]

## Sources

- (Source: [[2026-04-14-commodities-research-framework]])
- Erb, Claude B., and Campbell R. Harvey. "The Strategic and Tactical Value of Commodity Futures." Financial Analysts Journal (2006).
- Gorton, Gary, and K. Geert Rouwenhorst. "Facts and Fantasies about Commodity Futures." Financial Analysts Journal (2006).
