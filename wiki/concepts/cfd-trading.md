---
title: "CFD Trading"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [derivatives, leverage, margin, regulation]
aliases: ["CFD Trading", "CFD", "Contract for Difference", "Contracts for Difference", "CFDs"]
domain: [derivatives]
prerequisites: ["[[leverage]]", "[[derivatives]]"]
difficulty: beginner
related: ["[[perpetual-futures]]", "[[leverage]]", "[[regulation]]", "[[margin]]", "[[funding-rate]]", "[[asic]]"]
---

# CFD Trading

A **Contract for Difference (CFD)** is a derivative instrument that allows traders to speculate on the price movement of an underlying asset without owning it. The trader and broker agree to exchange the difference in the asset's price between the opening and closing of the contract. CFDs are available on stocks, indices, commodities, forex, and crypto, and are the primary instrument used by retail traders outside the United States (where CFDs are banned for retail).

## How CFDs Work

1. **Open a position**: go long (buy) if you expect the price to rise, or short (sell) if you expect it to fall
2. **Margin**: you post a fraction of the total position value (e.g., 5-20% depending on the asset and jurisdiction)
3. **Mark-to-market**: profits and losses are calculated in real time against your margin
4. **Close the position**: settle the difference between open and close price
5. **Overnight financing**: holding CFDs overnight incurs a financing charge (long positions pay; short positions may receive)

No physical delivery or ownership of the underlying asset occurs.

## Key Characteristics

| Dimension | CFD Trading |
|-----------|-------------|
| **Leverage** | Typically 5:1 to 30:1 for retail (jurisdiction-dependent) |
| **Short selling** | Yes, as easy as going long |
| **Asset classes** | Stocks, indices, commodities, forex, crypto, bonds |
| **Ownership** | No — you never own the underlying |
| **Dividends** | Adjustment credits (long) or debits (short) applied |
| **Expiry** | None (open-ended, similar to [[perpetual-futures]]) |
| **Overnight cost** | Yes — financing charge applied daily |
| **US availability** | Banned for retail traders (Dodd-Frank Act) |

## CFDs vs Perpetual Futures

CFDs and [[perpetual-futures]] are functionally similar — both are open-ended leveraged derivatives that track an underlying asset. Key differences:

| Dimension | CFDs | [[perpetual-futures|Perpetual Futures]] |
|-----------|------|------|
| **Counterparty** | The broker (OTC) | The exchange / other traders |
| **Custody** | Custodial (broker holds funds) | Self-custody (on DEXs) |
| **Regulation** | Heavily regulated (FCA, ESMA, ASIC) | Mostly unregulated (crypto DEXs) |
| **Funding mechanism** | Overnight financing rate | 8-hour [[funding-rate]] |
| **Price discovery** | Broker sets the price (market maker) | Exchange order book |
| **Conflict of interest** | Yes (broker profits from your losses) | No (exchange is neutral) |

## Regulation

CFD regulation varies dramatically by jurisdiction:

- **United States**: CFDs are **illegal** for retail traders under the Dodd-Frank Act
- **EU (ESMA)**: Leverage capped at 30:1 (forex), 20:1 (indices), 5:1 (individual stocks); negative balance protection required
- **UK (FCA)**: Similar to ESMA rules post-Brexit; crypto CFDs banned for retail
- **Australia ([[asic|ASIC]])**: Leverage caps similar to ESMA; stricter since 2021 reforms
- **Singapore (MAS)**: CFDs allowed with leverage limits

## Major CFD Brokers

- Plus500, eToro, Saxo Bank, Interactive Brokers (non-US)

## Risks

- **Counterparty risk**: the broker is your counterparty — if they fail, you may lose funds
- **Leverage amplifies losses**: a 5% move on 20:1 leverage is a 100% loss of margin
- **Overnight costs**: compound over time, making long-term CFD holding expensive
- **Conflict of interest**: many CFD brokers operate a market-maker model where they profit when you lose
- **Regulatory arbitrage**: some offshore brokers offer CFDs with minimal protections

## Related

- [[perpetual-futures]] — crypto-native equivalent
- [[leverage]] — understanding leveraged trading
- [[margin]] — margin and maintenance mechanics
- [[regulation]] — regulatory landscape

## Sources

- ESMA — Product intervention measures on contracts for differences (2018) — EU retail leverage caps and negative-balance protection.
- FCA (UK) — PS19/18 Restrictions on the sale of CFDs to retail clients.
- ASIC (Australia) — Product Intervention Order: CFDs (2021) — leverage limits and conduct rules.
- CFTC / SEC — Dodd-Frank Act framework underpinning the US retail CFD prohibition.
