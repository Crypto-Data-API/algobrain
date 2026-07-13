---
title: "Trading and Exchanges — Larry Harris (2003)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, market-microstructure, order-types, liquidity]
aliases: ["Trading and Exchanges"]
related: ["[[order-flow-scalping]]", "[[market-making-strategy]]", "[[slippage]]", "[[bid-ask-spread]]", "[[trading-and-exchanges]]"]
source_type: book
source_author: "Larry Harris"
source_date: 2003
confidence: high
claims_count: 10
---

Larry Harris's *Trading and Exchanges* is the definitive academic textbook on market microstructure — the study of how markets actually work at the mechanical level. It covers order types, market maker behavior, transaction costs, price discovery, regulation, and the economic incentives that drive market participants. Despite being published in 2003, its framework for understanding market structure, adverse selection, and transaction costs remains foundational and applicable across asset classes including modern electronic markets.

## Key Claims

1. [HIGH] [[market-making-strategy|Market makers]] profit from uninformed traders and lose to informed ones — understanding whether you are the informed or uninformed party in a trade is critical to profitability.

2. [HIGH] Limit orders provide [[liquidity]] and earn the [[bid-ask-spread]] but face [[adverse-selection]]; market orders consume liquidity and pay the spread — the choice between them reflects a speed-vs-cost tradeoff.

3. [HIGH] The [[bid-ask-spread]] compensates market makers for three costs: order processing costs, inventory carrying costs, and [[adverse-selection]] costs (losses to informed traders).

4. [HIGH] [[transaction-costs]] are iceberg-like: commissions are the visible tip but are dwarfed by spread costs, [[market-impact]], and opportunity costs (the cost of not trading when you should have).

5. [HIGH] [[market-impact]] is a function of order size, urgency, and information content — large orders from informed traders move prices more than small orders from noise traders.

6. [HIGH] Market quality has multiple dimensions: [[liquidity]], [[price-discovery]], [[volatility]], and [[transaction-costs]] — these dimensions frequently trade off against each other (e.g., transparency improves price discovery but may reduce liquidity).

7. [HIGH] Regulation (tick sizes, order handling rules, transparency requirements) shapes [[market-microstructure]] and determines which participants can profitably operate — market structure is not natural but designed.

8. [HIGH] Informed order flow is detectable through trade size patterns, timing relative to information events, and venue selection — this detection drives adverse selection and market maker behavior.

9. [HIGH] Optimal execution balances speed against [[market-impact]] — executing too quickly moves the market against you, while executing too slowly exposes you to adverse price movement.

10. [HIGH] Implementation shortfall (the gap between the decision price and the actual execution price) is where alpha leaks — measuring and minimizing this gap is essential for strategy profitability.

## Concepts Referenced

- [[market-microstructure]]
- [[market-making-strategy]]
- [[bid-ask-spread]]
- [[adverse-selection]]
- [[liquidity]]
- [[market-impact]]
- [[transaction-costs]]
- [[slippage]]
- [[price-discovery]]
- [[order-flow-scalping]]
- [[execution-algorithms]]

## Pages Backed

- [[order-flow-scalping]] — informed vs uninformed flow, adverse selection framework
- [[market-making-strategy]] — market maker economics, spread decomposition
- [[slippage]] — implementation shortfall, market impact functions
- [[bid-ask-spread]] — three-component cost decomposition
- [[trading-and-exchanges]] — primary source for entity/concept page
