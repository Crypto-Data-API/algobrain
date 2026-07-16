---
title: "Sturdy (SN10)"
type: entity
created: 2026-04-19
updated: 2026-07-16
status: draft
tags: [bittensor, crypto, defi, yield]
aliases: ["SN10", "Sturdy Finance"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://sturdy.finance/"
related: ["[[bittensor-subnets]]", "[[bittensor]]", "[[crypto-markets]]", "[[defi-yield-farming]]", "[[dtao]]", "[[stablecoin-yield]]", "[[yield-aggregators]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Sturdy (SN10)

**Sturdy** (SN10) is a Bittensor subnet that pairs with Sturdy Finance's DeFi yield aggregator. Miners submit proposed capital allocations across lending markets (Aave, Compound, Morpho, Yearn-style vaults, etc.); validators score allocations on realized yield net of gas and risk. The best miner allocations are used to rebalance Sturdy Finance's on-chain vaults.

## How It Works

Sturdy Finance operates yield vaults on Ethereum (and rollups). SN10 effectively outsources the allocation-optimization problem to Bittensor miners. Each epoch:

1. Validators publish the current vault composition and available markets.
2. Miners submit proposed reallocations.
3. The selected allocation is executed on-chain.
4. Validators score miners retrospectively on the yield realized over the next epoch.

## Trading Relevance

**Directly useful for DeFi yield optimization.** Anyone running a stablecoin or ETH yield book can consume the SN10 signal (either by depositing into Sturdy vaults or by replicating the allocations off-chain). The subnet also has a clear off-chain revenue model: Sturdy Finance's vault management fees flow back to reinforce alpha-10 valuation.

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]] -- protocol context
- [[defi-yield-farming]], [[yield-aggregators]], [[stablecoin-yield]] -- strategy context
- [[sturdy-finance]] -- Sturdy's off-chain product

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SN10 |
| **Market Cap Rank** | #1439 |
| **Market Cap** | $6.14M |
| **Current Price** | $1.26 |
| **Categories** | Artificial Intelligence (AI), Bittensor Subnets |
| **Website** | [https://www.sturdysubnet.org/](https://www.sturdysubnet.org/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.86M SN10 |
| **Total Supply** | 4.86M SN10 |
| **Max Supply** | 21.00M SN10 |
| **Fully Diluted Valuation** | $6.14M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $9.28 (2025-06-10) |
| **Current vs ATH** | -86.35% |
| **All-Time Low** | $0.8666 (2026-02-11) |
| **Current vs ATL** | +46.23% |
| **24h Change** | +0.00% |
| **7d Change** | -2.81% |
| **30d Change** | -16.18% |
| **1y Change** | -75.97% |

---

## Platform & Chain Information

**Native Chain:** Bittensor

### Contract Addresses

| Chain | Address |
|---|---|
| Bittensor | `10` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.sturdysubnet.org/](https://www.sturdysubnet.org/) |
| **GitHub** | [https://github.com/Sturdy-Subnet/sturdy-subnet](https://github.com/Sturdy-Subnet/sturdy-subnet) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $144,271.00 |
| **Market Cap Rank** | #1439 |
| **24h Range** | $1.26 — $1.31 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
