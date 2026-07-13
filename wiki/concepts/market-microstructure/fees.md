---
title: "Trading Fees"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [market-microstructure, execution, crypto, defi]
aliases: ["Trading Fees", "Exchange Fees"]
domain: [market-microstructure]
prerequisites: ["[[order-types]]"]
difficulty: beginner
related: ["[[transaction-costs]]", "[[binance]]", "[[market-making-strategy]]", "[[slippage]]", "[[execution-costs]]"]
---

Trading fees are the costs charged by exchanges, brokers, and networks for executing transactions. While individually small, fees compound over time and can be the difference between a profitable and unprofitable strategy, particularly for high-frequency approaches.

## Fee Structures

### Maker-Taker Model
The dominant model across both traditional and [[crypto-overview|crypto]] markets:

- **Maker fee**: Charged when an order adds liquidity to the [[order-book|order book]] (limit orders that do not immediately execute). Typically lower to incentivize liquidity provision.
- **Taker fee**: Charged when an order removes liquidity from the order book (market orders or limit orders that immediately execute). Typically higher.

| Venue Type | Maker Fee | Taker Fee |
|---|---|---|
| Crypto CEX (top tier) | 0.00% - 0.02% | 0.04% - 0.10% |
| Crypto CEX (retail) | 0.10% | 0.10% |
| US Equities (retail) | $0 (PFOF model) | $0 (PFOF model) |
| US Equities (institutional) | -$0.002/share (rebate) | $0.003/share |
| Futures (CME) | ~$1.25/contract | ~$1.25/contract |

### Volume-Based Tiers
Most exchanges reduce fees as trading volume increases. [[binance|Binance]] offers nine VIP tiers, with the highest tier (>25,000 BTC monthly volume) paying 0.01% maker / 0.03% taker. This creates a structural advantage for larger traders and [[market-making-strategy|market makers]].

### Crypto-Specific Fees

**Gas fees**: On [[ethereum|Ethereum]] and other blockchains, every transaction requires a gas fee paid to network validators. Ethereum gas fees can range from under $1 to over $100 during periods of high congestion, making small [[defi|DeFi]] trades economically unviable.

**[[layer-2|Layer 2]] fees**: L2 solutions like [[arbitrum|Arbitrum]] and [[polygon|Polygon]] reduce gas costs by 10-100x compared to Ethereum mainnet.

**DEX fees**: Decentralized exchanges like [[uniswap|Uniswap]] charge a swap fee (typically 0.3% for standard pools, 0.05% for stablecoin pairs) that goes to [[liquidity-providers|liquidity providers]].

**Withdrawal fees**: Fixed fees charged by centralized exchanges to withdraw crypto to an external wallet. These vary by asset and network.

## Impact on Strategy Profitability

Fees are a critical variable in [[backtesting]] and strategy design:

- A strategy trading 10 times per day with 0.1% round-trip fees loses **36.5%** annually to fees alone
- [[scalping]] strategies require extremely tight fees (0.01-0.02%) to be viable
- [[trend-following]] strategies with lower turnover are less fee-sensitive
- [[funding-rate-arbitrage|Funding rate arbitrage]] must account for fees when calculating expected carry

### The Fee Equation
**Net P&L = Gross P&L - (Entry Fee + Exit Fee + Spread Cost + [[slippage|Slippage]])**

Total [[transaction-costs|transaction costs]] (fees + spread + slippage) are often called "execution costs" and represent the strategy's hurdle rate.

## Fee Optimization

1. **Use limit orders**: Pay maker fees instead of taker fees
2. **Trade on high-volume venues**: Tighter spreads offset slightly higher fees
3. **Hold exchange tokens**: [[binance|BNB]], [[okx|OKB]] provide fee discounts (typically 25%)
4. **Achieve volume tiers**: Consolidate trading on fewer exchanges to reach higher tiers
5. **Batch transactions**: In DeFi, combine multiple operations to reduce gas overhead
6. **Time transactions**: Execute during low-congestion periods for lower gas fees

## Related

- [[transaction-costs]] -- Broader concept including fees, spread, and slippage
- [[slippage]] -- Price impact beyond quoted fees
- [[market-making-strategy]] -- Strategies that earn maker rebates
- [[binance]] -- Largest crypto exchange with tiered fee structure

## Sources

- Fee structures are well-documented across exchange documentation and [[market-microstructure]] literature
