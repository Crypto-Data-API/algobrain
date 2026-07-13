---
title: Maintenance Margin
type: concept
created: 2026-06-24
updated: 2026-06-24
status: good
tags: [market-microstructure, margin, leverage, derivatives, risk-management]
aliases: [maintenance-margin, maintenance-margin-requirement, MMR, margin-ratio]
domain: [market-microstructure, risk-management]
prerequisites: ["[[leverage]]", "[[mark-price]]", "[[liquidation]]"]
difficulty: intermediate
related:
  - "[[mark-price]]"
  - "[[liquidation]]"
  - "[[liquidation-cascade]]"
  - "[[cross-margin-vs-isolated-margin]]"
  - "[[crypto-perpetual-futures]]"
  - "[[leverage]]"
  - "[[perpetual-futures]]"
---

# Maintenance Margin

Maintenance margin is the minimum amount of equity a trader must keep against a leveraged position to keep it open. When account equity (valued at the [[mark-price]]) falls to the maintenance-margin level, the position is force-closed by [[liquidation]]. It is distinct from, and lower than, the initial margin required to open the position.

## Initial vs Maintenance Margin

- **Initial margin** — the collateral required to *open* a position. It is set by the chosen [[leverage]]: at 10x leverage the initial margin is roughly 1/10 of the position's notional value.
- **Maintenance margin** — the lower equity threshold that must be maintained to *keep* the position open. The buffer between initial and maintenance margin is the room a position has to move against the trader before liquidation.

Maintenance-margin requirements are commonly expressed as a small percentage of notional and vary by venue and by position size — illustratively in the low single-digit percent range, but this varies by venue and tier.

## Margin Ratio and the Liquidation Trigger

Venues track a **margin ratio**, conceptually:

```
margin_ratio = maintenance_margin_requirement / account_equity
```

where `account_equity` is marked at the [[mark-price]]. As the position moves against the trader, equity falls and the ratio rises toward 100%. When it reaches the venue's threshold, the liquidation engine takes over, closing the position (and, in cross mode, potentially others). Because equity is marked at the mark price rather than the last trade, a brief wick generally will not trigger liquidation on its own.

## Tiered Margin for Large Positions

To control the risk that one giant position cannot be unwound without large market impact, venues use **tiered (risk-limit) margin**: larger notional positions face higher maintenance-margin percentages and lower maximum leverage. As a position grows past each tier boundary, its required maintenance margin steps up, so the same dollar of equity supports less notional. This protects the venue's insurance fund and other users from outsized [[liquidation]] impact.

## Worked Illustrative Example

A trader opens a long worth 1,000 of notional at 10x leverage, posting 100 of initial margin. Suppose the venue's maintenance-margin requirement for that size is 5 of equity. The position can absorb losses until equity declines from 100 toward 5; at that point the margin ratio hits the threshold and the position is liquidated at the [[mark-price]]. The roughly 95 of cushion above maintenance is the trader's runway. (All figures are illustrative; requirements and tiers vary by venue.)

## How Traders Use It / Why It Matters

- **Position sizing** — knowing the maintenance requirement lets traders compute their true liquidation price and size positions to survive expected volatility.
- **Leverage selection** — higher leverage shrinks the gap between entry and liquidation, so the maintenance buffer is central to survival.
- **Account mode interaction** — whether one position's shortfall can pull down others depends on [[cross-margin-vs-isolated-margin]].

## Risks and Pitfalls

- **Tier creep** — scaling a position into a higher risk tier silently raises the maintenance requirement and can move your liquidation price closer than expected.
- **Mark vs last price confusion** — liquidation is on [[mark-price]], so a "safe-looking" last trade does not mean you are safe.
- **Fees and funding erode equity** — accrued [[funding-rate]] payments and fees reduce equity and can push a position into liquidation even without an adverse price move.
- **Cascade exposure** — many positions liquidating near the same level can amplify moves; see [[liquidation-cascade]].

## Related

- [[mark-price]]
- [[liquidation]]
- [[liquidation-cascade]]
- [[cross-margin-vs-isolated-margin]]
- [[crypto-perpetual-futures]]
- [[leverage]]
- [[funding-rate]]
- [[perpetual-futures]]

## Sources

General market knowledge; no specific wiki source ingested yet.
