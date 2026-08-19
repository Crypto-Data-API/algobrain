---
title: "Cross-Chain Bridge"
type: concept
created: 2026-07-17
updated: 2026-08-19
status: draft
tags: [crypto, defi, market-microstructure, on-chain, security, exploits]
aliases: ["Blockchain Bridge", "Token Bridge", "Bridge Protocol"]
domain: [crypto, market-microstructure]
prerequisites: ["[[cross-chain]]", "[[smart-contracts]]", "[[layer-1]]"]
difficulty: intermediate
---

# Cross-Chain Bridge

A **cross-chain bridge** is the specific piece of infrastructure that physically moves an asset's economic representation from one blockchain to another — the mechanism-level layer beneath the general [[cross-chain]] concept and distinct from [[interoperability]], the broader messaging-standards philosophy many bridges are built on top of. Bridges are also, by a wide margin, the single most-exploited category of infrastructure in crypto: over **$2.5 billion** was stolen from bridge protocols between 2021 and 2024, because they concentrate large pools of locked value at the exact seam between two different consensus and security models. *(For the full protocol-by-protocol comparison table, decision tree, and extended hack timeline, see [[cross-chain-bridges]] — this page focuses on the three core mechanisms and the four hacks that most shaped how bridges are built today.)*

## How It Works

Bridges solve the same problem — asset A exists on Chain 1 and needs to be usable on Chain 2 — through three fundamentally different mechanisms:

1. **Lock-and-mint.** The user deposits tokens into a bridge contract on the source chain, which **locks** them. A validator set or oracle network observes the deposit and an equivalent amount of **wrapped tokens** is minted on the destination chain; reversing the process burns the wrapped tokens and unlocks the originals. This is the oldest and most common design, and its weakness is structural: the locked-token contract is a **honeypot** — a single point of failure holding the full backing value of every wrapped token in circulation. If it is drained, all wrapped tokens on the destination chain instantly become unbacked.
2. **Burn-and-mint (native issuance).** The source-chain tokens are permanently destroyed (burned), an attestation service confirms the burn, and the destination-chain contract mints a genuinely **native** unit — not a wrapped derivative. This only works when a single issuer controls the token's supply on every connected chain, which is why it's mainly used for stablecoins: Circle's CCTP burns and mints native USDC across chains with no locked-fund honeypot at all, since there is nothing sitting in a vault to steal.
3. **Liquidity-network (pool-based).** Independent liquidity providers deposit the native asset into a pool on each chain; a "bridge" transfer is really a swap that releases funds from the destination pool, which liquidity providers replenish later. Users receive native tokens, not wrapped ones, but the design needs deep two-sided liquidity and exposes LPs to pool-imbalance risk — Stargate and Hop are the largest examples.

Layered on top of any of these three, bridges also differ in **who is trusted to verify a transfer is legitimate**: an external validator or guardian multisig (fast but concentrates trust in N-of-M signers), an optimistic dispute window (a relayer's claim is accepted unless challenged with a fraud proof within hours), or a native light client / ZK proof of the source chain's own consensus (slower to build, mathematically the strongest guarantee).

## Concrete Examples

- **Ronin Bridge, March 23, 2022 (discovered March 29) — $625M.** Attackers compromised five of the nine validator keys securing the Axie Infinity gaming sidechain's bridge — four from developer Sky Mavis and one from the Axie DAO, via an emergency signing delegation to Sky Mavis that was granted during a period of high load and never revoked. The U.S. Treasury attributed the attack to North Korea's Lazarus Group. See [[ronin]].
- **Wormhole, February 2, 2022 — $325M.** A missing signature-verification check on the Solana side of the [[wormhole|Wormhole]] bridge let an attacker forge a valid attestation and mint **120,000 wrapped ETH** on Solana with no ETH ever deposited on the Ethereum side. Backer Jump Crypto replaced the stolen funds within days to preserve the wETH peg — an unusual private bailout that prevented a wider depeg cascade.
- **Nomad, August 1, 2022 — $190M.** A routine contract upgrade accidentally set a default "valid" state for message verification, so *any* message — not just legitimately signed ones — was accepted. Once the first attacker discovered this, hundreds of unrelated users copy-pasted the exploit transaction and substituted their own address, draining the bridge in what has been described as a "decentralized looting" rather than a single heist.
- **Multichain, July 2023 — $130M+.** Multichain's CEO was arrested by Chinese authorities, and it emerged the private keys controlling the bridge's multisig were effectively held by one individual. Funds were drained from multiple chains' contracts simultaneously; Multichain ceased operations permanently and never recovered or explained the full loss.
- **Structural response:** the scale of these losses drove the industry toward burn-and-mint designs with no honeypot ([[cctp]], live since 2023), intent-based bridging that keeps users out of bridge contracts entirely (Across, UniswapX), and — following the 2026 KelpDAO exploit — explicit market pricing of *verifier configuration quality* rather than just brand-name trust (see [[multi-dvn-bridge-config-arbitrage]]).

## Trading Relevance

- **[[multi-dvn-bridge-config-arbitrage]]:** the most direct application — a long/short pair trade that prices individual bridge applications by verifier-configuration quality (1-of-1 vs multi-verifier), built around the April 2026 KelpDAO exploit as its founding case study.
- **[[cross-chain-arbitrage]] and [[cross-l2-arbitrage]]:** the choice of bridge (CCTP vs Across vs Stargate vs a canonical 7-day L2 withdrawal) sets the minimum viable spread and the risk profile for any cross-chain arb — bridge fee plus latency is a direct input into the strategy's breakeven cost.
- **[[wrapped-asset-triangular-arbitrage]]:** the wrapped-vs-native pricing gap (USDC.e vs native USDC, wETH vs ETH) that persistent bridge risk and liquidity differences create is itself a small, structural arbitrage opportunity professional desks monitor continuously.
- **Exploit-reaction trades:** when a lock-and-mint bridge is hacked, every wrapped token on the destination chain instantly loses its backing — traders who recognize the depeg fastest can act before the broader market prices in the exploit, though the ethics of trading directly against affected users are contested (see the trading-lessons discussion on [[2020-2024-bridge-exploits]]).
- **[[interoperability-basket]]:** the Hyperliquid sector basket of bridge/interoperability tokens carries an explicit immediate-removal rule if any constituent bridge suffers a hack exceeding $50M — bridge security events are a first-order input into that basket's live composition.

## Related

- [[cross-chain]] — the general concept and taxonomy this page's mechanisms sit under
- [[cross-chain-bridges]] — the full protocol-comparison table, decision tree, and extended hack timeline
- [[interoperability]] — the broader messaging-standards layer bridges are often built on top of
- [[cctp]] — Circle's burn-and-mint design with no lock-and-mint honeypot
- [[2020-2024-bridge-exploits]] — the complete exploit timeline and trading-lessons writeup
- [[multi-dvn-bridge-config-arbitrage]] — trading strategy built directly on bridge verifier-config risk
- [[wormhole]] — the $325M Feb 2022 exploit's protocol
- [[ronin]] — the $625M Mar 2022 exploit's chain
- [[smart-contract-risk]] — the general risk category bridge exploits fall under

## Sources

- General crypto infrastructure knowledge; bridge exploit data from publicly reported incidents and post-mortems, consistent with the timeline documented on [[2020-2024-bridge-exploits]] and [[cross-chain-bridges]].
