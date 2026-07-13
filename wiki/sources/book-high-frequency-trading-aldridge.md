---
title: "High-Frequency Trading: A Practical Guide — Irene Aldridge (2013)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, hft, market-microstructure, low-latency, algorithmic]
aliases: ["High-Frequency Trading Aldridge"]
related: ["[[low-latency-trading]]", "[[co-location]]", "[[market-making-strategy]]", "[[order-flow-scalping]]", "[[flash-boys]]", "[[high-frequency-trading-aldridge]]"]
source_type: book
source_author: "Irene Aldridge"
source_date: 2013
confidence: high
claims_count: 10
---

Irene Aldridge's *High-Frequency Trading: A Practical Guide* (2nd edition) covers the operational reality of HFT — infrastructure, strategy taxonomy, risk management, and regulation. It classifies HFT strategies into four categories and provides practical guidance on latency measurement, hardware acceleration, and the competitive dynamics of high-frequency markets.

## Key Claims

1. [HIGH] HFT strategies fall into four categories: [[market-making-strategy|market making]], statistical [[arbitrage]], directional ([[momentum]]), and structural (latency arbitrage) — each with distinct economic logic, data requirements, and risk profiles.

2. [HIGH] Latency measurement must include all components: network transmission, kernel processing, application logic, and exchange matching engine response — optimizing only one component while ignoring others yields suboptimal results.

3. [HIGH] FPGA (Field-Programmable Gate Arrays) provide hardware-level speed advantages over software-based trading systems by eliminating operating system overhead and executing strategy logic directly in hardware.

4. [HIGH] Tick data analysis reveals microstructure patterns (order book dynamics, trade clustering, quote behavior) that are invisible at lower frequencies such as minute or hourly bars.

5. [HIGH] HFT [[market-making-strategy|market making]] provides liquidity and narrows spreads under normal market conditions — but may withdraw liquidity during stress events, making the liquidity provision conditional.

6. [HIGH] The arms race in latency has shifted from milliseconds (2005) to microseconds (2010) to nanoseconds (2015+), with each incremental reduction requiring exponentially greater infrastructure investment.

7. [HIGH] Regulatory changes (Reg NMS in the US, MiFID II in Europe) fundamentally reshaped the competitive landscape for HFT firms — Reg NMS fragmented markets, creating cross-venue arbitrage opportunities.

8. [HIGH] Risk management for HFT requires real-time position monitoring and automatic circuit breakers — manual risk management is too slow for strategies that execute thousands of trades per second.

9. [HIGH] Profitable HFT strategies have extremely high win rates (>50%) with small average profit per trade — the edge is statistical across thousands of trades, not dependent on any single trade outcome.

10. [HIGH] [[co-location]], cross-connects, and proximity hosting are foundational infrastructure requirements for competitive HFT — without physical proximity to exchange matching engines, latency disadvantages are insurmountable.

## Concepts Referenced

- [[low-latency-trading]]
- [[co-location]]
- [[market-making-strategy]]
- [[order-flow-scalping]]
- [[fix-protocol]]
- [[arbitrage]]
- [[momentum]]
- [[risk-management]]
- [[flash-boys]]
- [[fpga]]

## Pages Backed

- [[low-latency-trading]] — full latency stack breakdown, arms race dynamics, FPGA hardware acceleration
- [[co-location]] — physical infrastructure requirements for competitive HFT
- [[market-making-strategy]] — HFT market making strategy type, conditional liquidity provision
- [[order-flow-scalping]] — tick data analysis and microstructure pattern recognition
- [[high-frequency-trading-aldridge]] — primary source for education/book page
