---
title: "Restaking"
type: concept
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, defi, staking, ethereum]
domain: [defi, staking]
prerequisites: ["[[staking]]", "[[ethereum]]", "[[defi]]"]
difficulty: advanced
aliases: ["ETH Restaking", "Liquid Restaking", "restaking", "re-staking", "LRT", "Liquid Restaking Token"]
related: ["[[eigenlayer]]", "[[staking]]", "[[ethereum]]", "[[lido]]", "[[yield-farming]]", "[[defi]]", "[[smart-contract-risk]]"]
---

Restaking is the practice of re-using already-staked assets -- primarily [[ethereum|ETH]] staked via liquid staking tokens (LSTs) like [[lido|stETH]] -- to provide economic security for additional protocols and services in exchange for extra yield. Pioneered by [[eigenlayer|EigenLayer]] in 2023, restaking allows the Ethereum validator set to extend its security guarantees to new networks and applications without requiring those applications to bootstrap their own trust from scratch.

## How Restaking Works

### The Core Mechanism

Traditional [[staking]] on Ethereum involves locking 32 ETH per validator to secure the Ethereum network, earning ~3-5% APY. Restaking adds an additional layer:

1. **Stake ETH:** Validator stakes ETH natively or through an LST (stETH, rETH, cbETH)
2. **Opt into restaking:** The staker deposits their LST into a restaking protocol (e.g., [[eigenlayer|EigenLayer]]) or enables native restaking by pointing their validator's withdrawal credentials to the restaking contract
3. **Secure additional services:** The restaked ETH now secures Actively Validated Services (AVSs) -- oracle networks, data availability layers, bridges, keeper networks, rollup sequencers, etc.
4. **Earn additional yield:** Restakers earn rewards from each AVS they help secure, stacking on top of base Ethereum staking yield

### The Yield Stack

| Layer | Source | Typical APY |
|-------|--------|-------------|
| Base ETH staking | Ethereum consensus rewards | 3-5% |
| LST yield | Liquid staking (stETH, rETH) | Included in above |
| Restaking rewards | AVS security fees | 2-10%+ |
| Points/incentives | Protocol bootstrapping | Variable |
| **Total** | **Stacked yield** | **5-15%+ on ETH** |

### Liquid Restaking Tokens (LRTs)

A second wave of protocols (EtherFi, Renzo, Kelp, Puffer) issue **liquid restaking tokens** -- tokens that represent restaked positions and can be used in further DeFi strategies. This creates an additional layer of composability (and risk):

ETH -> stETH (LST) -> eETH/ezETH/rsETH (LRT) -> use LRT as collateral in [[aave]] or LP in [[uniswap]]

## Trading Relevance

- **Yield amplification:** Restaking enables 10-50%+ effective ETH yields when points farming and LRT incentives are included, making it a core strategy in 2024-2026 [[yield-farming]]
- **Points farming meta:** EigenLayer's points system and derivative LRT protocols created an enormous meta of depositing assets and farming points in anticipation of token airdrops
- **LRT-fi strategies:** Using liquid restaking tokens as collateral for borrowing (leverage loops) or as LP assets creates complex yield strategies with high returns but compounded risk
- **Airdrop value extraction:** Restaking protocols distribute governance tokens to early depositors, creating speculative value beyond the stated yield

## Risks

### Slashing Cascades
The most significant novel risk of restaking. If a single operator misbehaves while validating multiple AVSs, the same underlying ETH can be slashed multiple times. Because many stakers delegate to the same popular operators, a single slashing event could cascade across the entire restaking ecosystem, potentially affecting billions in TVL.

### Smart Contract Complexity
Restaking involves 3-5 protocol layers (Ethereum -> LST protocol -> restaking protocol -> AVS -> optional LRT protocol). Each layer adds smart contract risk, and vulnerabilities at integration points between layers are especially dangerous.

### Centralization Risk
A small number of operators validate most AVSs, and a small number of LSTs (stETH dominates) constitute most restaked capital. This concentration creates systemic risk.

### Correlation Risk
If a significant portion of Ethereum's validator set is restaked through a single protocol, an exploit of that protocol could threaten Ethereum's base-layer security.

### Regulatory Uncertainty
Restaking tokens (LRTs) may be classified as securities. The multi-layered yield generation resembles structured financial products that attract regulatory scrutiny.

## Key Protocols

| Protocol | Role | Token |
|----------|------|-------|
| [[eigenlayer\|EigenLayer]] | Original restaking layer | EIGEN |
| Symbiotic | Competing restaking layer (Lido-backed) | -- |
| Karak | Multi-asset restaking | -- |
| EtherFi | Liquid restaking (issues eETH) | ETHFI |
| Renzo | Liquid restaking (issues ezETH) | REZ |
| Kelp | Liquid restaking (issues rsETH) | -- |
| Puffer | Liquid restaking (issues pufETH) | PUFFER |

## Related

- [[eigenlayer]] -- the protocol that pioneered restaking
- [[staking]] -- the foundational mechanism restaking builds upon
- [[ethereum]] -- the base layer whose security restaking extends
- [[lido]] -- the leading LST provider, primary source of restaked assets
- [[yield-farming]] -- the broader DeFi strategy category
- [[defi]] -- the decentralized finance ecosystem
- [[smart-contract-risk]] -- amplified by the multi-layered restaking architecture
- [[leverage]] -- restaking with LRT leverage loops introduces liquidation risk

## Sources

- EigenLayer — *EigenLayer Whitepaper: The Restaking Collective* (2023). https://docs.eigenlayer.xyz/ — original articulation of restaking and AVS security.
- Vitalik Buterin, "Don't overload Ethereum's consensus" (2023). https://vitalik.eth.limo/general/2023/05/21/dont_overload.html — the canonical critique of restaking's systemic risk to Ethereum base-layer security.
- DefiLlama — *Restaking and LRT TVL dashboards*. https://defillama.com/ — protocol landscape and TVL figures (EigenLayer, EtherFi, Renzo, Kelp, Puffer).
- Protocol documentation: EtherFi (eETH), Renzo (ezETH), Kelp (rsETH), Puffer (pufETH), Symbiotic, Karak — for per-protocol mechanics and token details.
- Mechanics, yield-stack, and risk framework reflect the ecosystem state through mid-2026.
