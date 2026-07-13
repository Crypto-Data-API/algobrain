---
title: "EigenLayer"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [crypto, defi, ethereum]
entity_type: protocol
aliases: ["Eigen Layer", "EIGEN", "EigenCloud"]
founded: 2023
headquarters: "Seattle, Washington, USA"
website: "https://www.eigenlayer.xyz"
related: ["[[ethereum]]", "[[staking]]", "[[defi]]", "[[restaking]]", "[[lido]]", "[[yield-farming]]"]
---

EigenLayer is an [[ethereum]] [[restaking]] protocol that allows users to re-stake their staked ETH -- or liquid staking tokens (LSTs) like [[lido|stETH]] -- to secure additional decentralized services in exchange for extra yield. Founded by Sreeram Kannan, a former University of Washington professor, EigenLayer introduces the concept of "pooled security" where Ethereum's existing validator set can opt in to secure new protocols without requiring each protocol to bootstrap its own trust network.

## How EigenLayer Works

EigenLayer operates through a system of **Actively Validated Services (AVSs)** -- protocols that need economic security but do not want to build their own validator set from scratch. Examples include oracle networks, data availability layers, bridges, and keeper networks. Restakers delegate their staked ETH (or LSTs) to operators who validate these AVSs, earning additional rewards on top of their base Ethereum staking yield.

The yield stack typically looks like:
1. **Base ETH staking yield:** ~3-5% APY from Ethereum proof-of-stake consensus
2. **LST yield:** stETH from [[lido]] captures this base yield in a liquid token
3. **EigenLayer restaking yield:** additional 2-10%+ from securing AVSs
4. **Points/token incentives:** during early phases, EigenLayer distributed points that converted to the EIGEN governance token

By mid-2024, EigenLayer had accumulated over $15 billion in total value locked (TVL), making it one of the largest DeFi protocols by deposits. The EIGEN token launched in 2024 with a governance and slashing function tied to AVS security.

## 2025-2026 Developments

EigenLayer is private (no equity ticker); traders gain exposure only through the **EIGEN** token, restaking yields, or the liquid restaking token (LRT) ecosystem built on top of it. Key themes through 2025-2026:

- **Slashing live** — The long-awaited slashing / "operator sets" functionality moved from testnet into production, completing the security model that lets AVSs actually penalize misbehaving operators. This is the feature that converts restaking from a points/yield game into genuine economic security.
- **EigenCloud / broader platform** — EigenLayer Labs repositioned the stack as a broader "verifiable cloud" platform (EigenCloud), extending beyond AVS security toward verifiable compute and data availability, backed by additional funding from a16z crypto.
- **Token unlocks and supply overhang** — Scheduled EIGEN unlocks to team, investors, and the ecosystem remain a recurring supply-side overhang that traders watch closely; the token has been volatile since its 2024 launch.
- **Competitive pressure** — Symbiotic, Karak, and Bitcoin-native [[restaking]] (Babylon) continued to compete for restaked collateral and AVS mandates, compressing the early TVL dominance.

> Figures and milestones reflect general knowledge as of mid-2026 and should be verified against on-chain data and official EigenLayer communications before trading.

## Trading Relevance

- **Yield amplification:** Restaking enables 10-50%+ effective ETH yields when layered with LST yields and AVS rewards, making it a core component of [[yield-farming]] strategies in the Ethereum ecosystem
- **Points farming meta:** EigenLayer's points system (pre-token) created an entire meta-game of depositing and farming points across "LRT" protocols (EtherFi, Renzo, Kelp, Puffer) that issue their own liquid restaking tokens
- **Risk of slashing cascades:** If an AVS operator behaves maliciously or fails validation, restaked ETH can be slashed -- and because the same ETH secures multiple AVSs, a single slashing event could cascade across the restaking ecosystem
- **Correlation risk:** Heavy restaking concentration means a significant portion of Ethereum's security is tied to EigenLayer's smart contracts, creating systemic risk if the protocol is exploited

## Risks

- **Smart contract risk:** EigenLayer adds an additional smart contract layer on top of already-complex LST protocols
- **Slashing cascades:** A single operator failure could trigger slashing across multiple AVSs simultaneously
- **Centralization:** Operator concentration risk -- a small number of operators may validate most AVSs
- **Regulatory uncertainty:** Restaking tokens and yields may attract securities classification scrutiny
- **Complexity:** Users often interact through 3-4 protocol layers (ETH -> stETH -> EigenLayer -> LRT), each adding risk

## EIGEN Token

The EIGEN token serves dual purposes in the EigenLayer ecosystem:

- **Governance:** Token holders vote on protocol parameters, AVS whitelisting, and slashing conditions
- **Intersubjective slashing:** EIGEN enables a novel slashing mechanism for faults that are observable but not provable on-chain (e.g., an oracle reporting a wrong price). In these cases, EIGEN holders can fork the token to slash misbehaving operators
- **Token distribution:** Initial distribution allocated tokens to early restakers (via points conversion), the team, investors, and a community treasury. The points-to-token conversion created significant speculative interest during the pre-launch period

## Key Competitors

- **Symbiotic:** Competing restaking protocol backed by Lido founders, launched 2024. Supports a wider range of collateral types beyond ETH/LSTs
- **Karak:** Multichain restaking protocol supporting assets beyond ETH, including LSTs on multiple chains
- **Babylon:** Bitcoin-native restaking protocol enabling BTC holders to secure proof-of-stake chains

## Related

- [[restaking]] -- the underlying concept EigenLayer pioneered
- [[ethereum]] -- the base layer whose security EigenLayer extends
- [[lido]] -- leading LST provider whose stETH is the primary EigenLayer deposit asset
- [[staking]] -- the foundational mechanism restaking builds upon
- [[yield-farming]] -- the broader DeFi strategy category
- [[defi]] -- the decentralized finance ecosystem
- [[smart-contract-risk]] -- the primary risk vector for restaking participants

## Sources

- General knowledge -- protocol mechanics and market data as of 2024
- EigenLayer / EigenCloud official site and docs — https://www.eigenlayer.xyz and https://docs.eigenlayer.xyz
- EigenLayer blog (slashing launch, EigenCloud announcements) — https://blog.eigencloud.xyz — Verified via Perplexity (sonar), 2026-06-10
- TVL and token data: DefiLlama (https://defillama.com/protocol/eigenlayer), CoinGecko EIGEN
