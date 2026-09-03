---
title: "BNB Chain"
type: entity
created: 2026-09-03
updated: 2026-09-03
status: good
tags: [crypto, defi, bnb, smart-contracts, dex]
entity_type: protocol
founded: 2020
website: "https://www.bnbchain.org"
aliases: ["Binance Smart Chain", "BSC", "BNB Smart Chain"]
related: ["[[bnb]]", "[[binance]]", "[[ethereum]]", "[[layer-1]]", "[[pancakeswap-token]]", "[[venus]]", "[[defi]]", "[[asterdex]]"]
---

# BNB Chain

**BNB Chain** is an EVM-compatible [[layer-1|Layer 1]] blockchain launched by [[binance|Binance]] in 2020, originally named **Binance Smart Chain (BSC)** and renamed to BNB Chain in February 2022. It runs on **Proof of Staked Authority (PoSA)** consensus with a small, elected validator set, offering fast block times and low fees at the cost of decentralization relative to larger validator sets like [[ethereum]]'s. This page covers the chain/protocol layer; for the **BNB token** itself — market data, tokenomics, burn mechanism, and trading profile — see [[bnb]].

## Key Facts

| Metric | Value |
|---|---|
| Launched | September 2020, as Binance Smart Chain |
| Renamed | February 15, 2022 — Binance Smart Chain → BNB Chain |
| Consensus | Proof of Staked Authority (PoSA) |
| Active validators | ~21 in the original "Cabinet" design; expanded over time to improve decentralization |
| Execution environment | EVM-compatible (Ethereum Virtual Machine) |
| Block time | ~3 seconds under the original PoSA design (subsequent chain upgrades have targeted further reductions) |
| Native token | [[bnb|BNB]] — gas, staking, and fee-discount asset |
| Dominant DEX | [[pancakeswap-token|PancakeSwap]] |
| Website | https://www.bnbchain.org |

## History: From Binance Smart Chain to BNB Chain

Binance announced Binance Smart Chain in September 2020 as an EVM-compatible chain designed to run in parallel with the original Binance Chain (a separate, non-EVM chain built for fast token trading and later renamed BNB Beacon Chain). BSC's pitch was straightforward: an Ethereum-compatible smart-contract environment with far lower gas costs and faster confirmation than Ethereum mainnet, letting developers redeploy existing Solidity contracts with minimal changes.

On **February 15, 2022**, Binance rebranded Binance Chain and Binance Smart Chain together under the unified **BNB Chain** name — "BNB" standing for "Build and Build" — folding both chains and their ecosystem (later including the opBNB Layer-2 and BNB Greenfield decentralized storage network) under one umbrella brand tied to the BNB token rather than the Binance company name. The rebrand accompanied an increase in the active validator count from 21 toward a larger candidate set, aimed at addressing recurring centralization criticism.

## Consensus: Proof of Staked Authority (PoSA)

BNB Chain's PoSA design blends elements of Proof of Authority and Delegated Proof of Stake: a limited set of validators (~21 active seats in the original "Cabinet") produce blocks in rotation, elected daily based on the amount of [[bnb|BNB]] staked or delegated to them. This is a deliberate trade-off:

- **What it buys**: sub-3-second block times, low and predictable gas fees, and fast finality — well suited to the high-throughput DeFi and consumer activity BNB Chain was designed to host.
- **What it costs**: a validator set an order of magnitude smaller than [[ethereum]]'s or [[bitcoin]]'s, concentrating block-production power and drawing persistent centralization criticism. This is the standard trade-off documented in [[layer-1]]'s discussion of the blockchain trilemma (decentralization vs. security vs. scalability) — BNB Chain explicitly leans toward scalability.

## EVM Compatibility and Ecosystem

Because BNB Chain is EVM-compatible, contracts and tooling built for [[ethereum]] port to it with little modification, which was central to its rapid growth during the 2021 DeFi boom as a low-cost alternative when Ethereum gas fees spiked. The dominant application is **[[pancakeswap-token|PancakeSwap]]**, an automated market maker DEX and Uniswap-model fork that remains BNB Chain's largest source of on-chain volume and TVL; **[[venus|Venus]]** (money-market lending) is another long-running BNB Chain DeFi primitive. More recently, [[asterdex|AsterDEX]] — a multi-chain perpetual-futures DEX — routes the majority of its trading volume through a BNB Chain deployment alongside its Ethereum, Arbitrum, and Solana deployments, illustrating BNB Chain's continued role as a low-fee venue for high-frequency on-chain trading activity.

## Relationship to Binance

BNB Chain was launched by Binance and remains closely associated with the exchange's brand and user base, even after the 2022 rebrand away from the "Binance" name. This relationship is a double-edged structural fact documented on the token side ([[bnb]]): the chain benefits from Binance's distribution and liquidity, but it also inherits Binance's regulatory exposure — most notably the November 2023 US DOJ/SEC settlement against Binance, which the wiki's [[bnb]] page treats as a canonical example of Binance-side regulatory risk transmitting into the token. At the protocol level, this same association is why BNB Chain is sometimes treated as less "neutral" than a fully independent L1 — governance and validator incentives are widely understood to run through channels closely tied to Binance rather than a fully disintermediated foundation.

## Notable Incident: October 2022 Bridge Exploit

BNB Chain suffered a major cross-chain bridge exploit in **October 2022**, in which an attacker minted roughly **$570M** worth of BNB by exploiting a flaw in the BNB Beacon Chain-to-BNB Smart Chain cross-chain bridge (the same incident referenced on [[bnb]]'s Risks section). Validators temporarily halted the chain in response — itself only possible because of the small, coordinated validator set, illustrating the double edge of PoSA's centralization trade-off: it enabled a fast emergency response that would be far harder to coordinate on a larger, more decentralized validator set, but the same concentration is the recurring criticism of the design.

## Trading Relevance

- BNB Chain activity (DEX volume, TVL, new contract deployments) is a leading on-chain indicator tracked alongside [[bnb]] token performance
- PancakeSwap trading volume and TVL are the single largest on-chain proxy for BNB Chain's health as a DeFi venue
- The chain's low fees make it a preferred venue for high-frequency and market-making activity, including the majority of [[asterdex|AsterDEX]]'s multi-chain perpetual-futures volume
- Chain-level incidents (bridge exploits, validator-set changes, hard forks) are tradeable catalysts distinct from — but correlated with — [[bnb]] token price action
- See [[bnb]] for the token-level trading profile, funding-rate/derivatives coverage, and CryptoDataAPI data endpoints

## Related

- [[bnb]] — the native token: market data, tokenomics, burn mechanism, and derivatives/trading profile
- [[binance]] — the exchange that launched BNB Chain and remains closely associated with it
- [[layer-1]] — the general Layer 1 concept BNB Chain is an instance of (PoSA consensus, EVM execution, trilemma trade-offs)
- [[ethereum]] — the chain BNB Chain is EVM-compatible with and was positioned as a low-cost alternative to
- [[pancakeswap-token]] — the dominant DEX on BNB Chain
- [[venus]] — major BNB Chain lending protocol
- [[asterdex]] — perpetual-futures DEX routing the majority of its volume through a BNB Chain deployment
- [[defi]] — the broader DeFi category BNB Chain's ecosystem serves

## Sources

- [[bnb]] — existing wiki page (BNB Chain Ecosystem section, PoSA/validator facts, October 2022 bridge exploit, DOJ/SEC settlement)
- CoinDesk, "Binance Smart Chain Rebrands to BNB Chain," February 15, 2022
- BusinessToday / CryptoPolitan / Chain Bulletin, coverage of the February 2022 Binance Smart Chain → BNB Chain rebrand
- Verified via web search, 2026-09-03: BSC launch (September 2020), February 15, 2022 rebrand date, "Build and Build" naming, validator-count expansion
