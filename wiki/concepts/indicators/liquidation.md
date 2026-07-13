---
title: "Liquidation"
type: concept
created: 2026-04-06
updated: 2026-04-07
status: good
confidence: medium
tags: [derivatives, risk-management, liquidation, leverage]
aliases: ["Forced Liquidation", "Liq", "Getting Liquidated", "Getting Rekt", "Liquidation Risk"]
domain: [risk-management, derivatives]
prerequisites: ["[[leverage]]", "[[margin]]", "[[perpetual-futures]]"]
difficulty: intermediate
related: ["[[leverage]]", "[[margin]]", "[[risk-management]]", "[[perpetual-futures]]", "[[open-interest]]", "[[book-when-genius-failed]]", "[[book-the-black-swan]]"]
---

# Liquidation

**Liquidation** is the forced closure of a leveraged [[derivatives]] position when the trader's [[margin]] (collateral) falls below the required maintenance level. It is the exchange's mechanism for ensuring losses do not exceed posted collateral, protecting the platform and other traders from bad debt.

## How Liquidation Works

When a trader opens a leveraged position on [[perpetual-futures]], they post [[margin]] as collateral. As the market moves against their position, unrealized losses consume this margin. If losses erode equity below the **maintenance margin** threshold, the exchange's liquidation engine forcibly closes the position.

### Margin Types

**Initial margin** is the minimum collateral to *open* a position (e.g., $1,000 for a $10,000 position at 10x [[leverage]]). **Maintenance margin** is the minimum to *keep* it open, always lower than initial:

| Leverage | Initial Margin | Maintenance Margin |
|----------|---------------|-------------------|
| 5x | 20% | ~10% |
| 10x | 10% | ~5% |
| 20x | 5% | ~2.5% |
| 40x | 2.5% | ~1.25% |

## Calculating Liquidation Price

### Long Position Example

A trader opens a BTC long at $70,000 with 10x leverage ($7,000 margin, 0.5% maintenance rate):

```
Liq Price = $70,000 x (1 - 1/10 + 0.005) = $70,000 x 0.905 ≈ $63,350
```

A ~9.5% drop from entry liquidates this position.

### Short Position Example

A trader opens a BTC short at $70,000 with 20x leverage ($3,500 margin):

```
Liq Price = $70,000 x (1 + 1/20 - 0.005) = $70,000 x 1.045 ≈ $73,150
```

A ~4.5% rise liquidates this short. Higher [[leverage]] brings the liquidation price closer to entry.

## Partial vs. Full Liquidation

Many exchanges use **partial liquidation**: reducing position size incrementally (25-50% at a time) until margin requirements are met, minimizing market impact. **Full liquidation** closes the entire position at once -- more common on smaller exchanges. [[hyperliquid]] and [[binance]] use partial liquidation for larger positions.

## Cascading Liquidations

The most dangerous phenomenon in leveraged markets:

1. Price drops, triggering [[liquidation|liquidations]] of overleveraged longs
2. Liquidation orders are market sells, pushing price lower
3. Lower price triggers more liquidations of slightly less leveraged longs
4. Feedback loop continues until selling exhausts or buyers step in

This explains why leveraged markets experience sharper moves than [[spot-markets]]. Historical examples: **March 2020** (BTC dropped from $8,000 to $3,800 in hours), **May 2021** ($8 billion in liquidations as BTC fell from $43,000 to $30,000), and the **FTX collapse** (Nov 2022). The [[ltcm]] collapse of 1998 demonstrated the same cascade dynamic in traditional markets: as LTCM was forced to liquidate positions, their selling pushed prices further against them, triggering additional losses in a vicious feedback loop (Source: [[book-when-genius-failed]]).

## Live Liquidation Data

Recent activity on [[hyperliquid]]:

| Date | Total Liquidations | Notable |
|------|--------------------|---------|
| Apr 5, 2026 | 10,406 | Elevated but not extreme |
| Apr 2, 2026 | 32,964 | Highly volatile session |
| Peak hour (BTC) | 920 in one hour | Concentrated cascade event |

The 3x spike between Apr 5 and Apr 2 reveals a sharp, sudden move that caught leveraged traders off guard. Liquidation spikes coincide with [[volume]] surges and sharp [[open-interest]] drops.

## Insurance Funds and ADL

**Insurance funds** cover bad debt when positions cannot be closed at a price covering the [[margin]]. They are funded by residual margin from liquidations that close better than the bankruptcy price.

If the insurance fund is depleted, **socialized losses** distribute bad debt among profitable traders (rare on major exchanges). As a last resort, **auto-deleveraging (ADL)** forcibly reduces the most profitable, highest-leveraged positions on the opposite side to absorb the bankrupt position -- without consent.

## Practical Risk Mitigation

1. **Use appropriate [[leverage]]**: Experienced traders rarely exceed 5-10x
2. **Set [[stop-loss]] orders**: Exit *before* reaching the liquidation price
3. **Proper [[position-sizing]]**: Never risk more than 1-2% of total capital per trade
4. **Monitor [[margin]] ratio**: Keep well above maintenance level
5. **Watch [[open-interest]] and [[funding-rate]]**: Extreme readings warn of cascade potential
6. **Prefer isolated margin**: Caps maximum loss per position vs. cross margin (which risks entire account)

## Common Misconceptions

1. **"Liquidation is like a stop loss"** -- A [[stop-loss]] is voluntary at your chosen price; liquidation is forced when your margin is nearly gone. Very different timing and outcomes.
2. **"I can only lose my margin"** -- On isolated margin, yes. On **cross margin**, liquidation can drain your entire account balance.
3. **"Liquidation happens at exactly the liquidation price"** -- [[slippage]] in fast markets can cause worse execution. This is why insurance funds exist.
4. **"Only beginners get liquidated"** -- [[black-swan]] events can move markets faster than any risk model anticipates (Source: [[book-the-black-swan]]). Even experienced traders face liquidation in extreme conditions.
5. **"Adding more margin always helps"** -- It delays liquidation but increases total capital at risk. Sometimes accepting the loss is better. See [[risk-management]].

## Further Reading

- [[risk-management]] -- The discipline that prevents liquidation from ruining accounts
- [[leverage]] -- Understanding the amplifier that makes liquidation possible
- [[margin]] -- Collateral mechanics and isolated vs. cross margin
- [[perpetual-futures]] -- The primary instrument where liquidation occurs
- [[open-interest]] -- Tracking positioning to anticipate cascades
- [[position-sizing]] -- Determining appropriate trade sizes relative to capital

## Related

- [[derivatives-native-regime]] -- liquidation cascades as a tradeable regime state
- [[security-black-swan-regime]] -- shock-driven forced unwinds
- [[crypto-market-regime-taxonomy]] -- the 14-basket crypto regime framework

## Sources

- [[book-when-genius-failed]] -- Lowenstein documents how LTCM's forced liquidation created cascading losses that nearly collapsed the financial system
- [[book-the-black-swan]] -- Taleb argues that tail events move markets faster than risk models anticipate, making liquidation a constant threat in leveraged positions
