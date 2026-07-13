---
title: Market Impact
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - market-microstructure
  - slippage
  - liquidity
aliases:
  - market-impact
  - price-impact
  - Market Impact
domain: [market-microstructure]
prerequisites: ["[[liquidity]]", "[[order-book]]", "[[slippage]]"]
difficulty: intermediate
related: ["[[slippage]]", "[[liquidity]]", "[[order-book]]", "[[algorithmic-trading]]", "[[implementation-shortfall]]"]
---

# Market Impact

**Market impact** is the effect that a trade -- especially a large order -- has on the price of an asset. Large buy orders push prices up; large sell orders push them down.

Minimizing market impact is a key concern in [[algorithmic-trading]] and institutional execution. It is closely related to [[slippage]] and depends on [[liquidity]] and [[order-book]] depth.

## Temporary vs. Permanent Impact

- **Temporary impact** -- the short-lived price displacement caused by the mechanical pressure of executing an order. Once the order is complete and liquidity replenishes, the price partially reverts. This is sometimes called "market resilience."
- **Permanent impact** -- the lasting price change that occurs because the trade conveys information to the market. If a large fund is buying, other participants may infer that the fund has bullish conviction, and they adjust their prices accordingly. This informational component does not revert.

## The Square Root Law

Empirical research has established that market impact is approximately proportional to the square root of order size relative to average daily volume: Impact ~ sigma * sqrt(Q / V), where sigma is daily volatility, Q is order quantity, and V is average daily volume. This means doubling the order size does not double the impact -- it increases it by roughly 40%. This relationship, sometimes called the "square root law of market impact," has been validated across equities, futures, and FX.

## Minimizing Market Impact

Institutional traders use several execution strategies to reduce impact and the associated cost known as [[implementation-shortfall]]:

- **TWAP (Time-Weighted Average Price)** -- spreads the order evenly over a specified time window, reducing the concentration of demand at any one moment.
- **VWAP (Volume-Weighted Average Price)** -- distributes the order proportionally to historical volume patterns throughout the day, trading more during high-volume periods and less during quiet ones.
- **Dark pools** -- alternative trading venues where orders are not displayed on public [[order-book]]s, allowing large blocks to match without revealing intent to the market. See dark-pool-trading.
- **Iceberg orders** -- only a small portion of the total order is visible on the exchange, hiding the true size from other participants.

## Related

- [[slippage]]
- [[liquidity]]
- [[order-book]]
- [[algorithmic-trading]]
- [[implementation-shortfall]]

## Sources

- Robert Almgren and Neil Chriss, "Optimal execution of portfolio transactions," *Journal of Risk* 3, 2000 — the standard temporary/permanent impact framework
- J.-P. Bouchaud, J. Bonart, J. Donier, M. Gould, *Trades, Quotes and Prices: Financial Markets Under the Microscope* (Cambridge University Press, 2018) — the square-root law of market impact
- Xavier Gabaix et al., "A theory of power-law distributions in financial market fluctuations," *Nature* 423, 2003
- Larry Harris, *Trading and Exchanges: Market Microstructure for Practitioners* (Oxford University Press, 2003)
