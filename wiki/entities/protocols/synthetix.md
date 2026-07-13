---
title: "Synthetix"
type: entity
created: 2026-04-15
updated: 2026-06-10
status: good
tags: [crypto, defi, derivatives, ethereum]
entity_type: protocol
founded: 2018
website: "https://synthetix.io"
aliases: ["Synthetix", "SNX", "Havven", "sUSD"]
related: ["[[defi]]", "[[ethereum]]", "[[uniswap]]", "[[curve-finance]]", "[[hyperliquid]]", "[[dydx]]", "[[stablecoins]]", "[[perpetual-futures]]", "[[decentralized-exchanges]]"]
---

**Synthetix** is one of the oldest [[defi]] derivatives protocols on [[ethereum]], built around the SNX staking token and the crypto-collateralized stablecoin **sUSD**. Founded by Kain Warwick and launched in 2018 as **Havven** before rebranding, it pioneered the pooled-debt synthetic asset model and is now repositioning itself as an Ethereum-mainnet perpetual futures DEX and stablecoin issuer. For traders it matters as a perps venue, as the issuer of a stablecoin that suffered a major 2025 depeg, and as a case study in protocol-design risk.

## Overview

Synthetix originally let SNX stakers mint synthetic assets ("synths" — sUSD, sETH, sBTC and others) against pooled collateral, with all stakers sharing a collective debt pool. This model powered the first generation of on-chain synthetic exposure and fed liquidity to front-ends such as Kwenta. Over 2023-2024 the protocol fragmented across L2s (Optimism, Base) with Perps v2/v3, before reversing course in 2025-2026 to consolidate on Ethereum mainnet.

### Key events 2025-2026

- **Early 2025 — SIP-420 and the "420 pool"**: SIP-420 moved staking into a shared, delegated debt pool and cut the required collateralization ratio from 750% to 200%, improving capital efficiency but removing the individual incentive for stakers to buy back sUSD below $1 (Cointelegraph).
- **Early 2025 — Kwenta and TLX acquisitions**: Synthetix acquired Kwenta, the leading front-end for Synthetix perps, and leveraged-token protocol TLX, bringing trader UX in-house (Synthetix blog).
- **April 2025 — sUSD depeg**: sUSD fell roughly 31-34% below peg, trading as low as ~$0.66-0.68 on 18 April 2025 — one of the worst depegs of a major crypto-collateralized stablecoin since the 2022-2023 cycle (Cointelegraph, AInvest).
- **May 2025 — Derive acquisition proposed and withdrawn**: Synthetix proposed re-acquiring options protocol Derive (formerly Lyra) in a ~$27M token swap (27 DRV : 1 SNX, ~29.3M new SNX). After community pushback on valuation and terms, SIP-415 and the matching Derive proposal were mutually withdrawn (The Block, Synthetix blog).
- **December 2025 — Perps on Ethereum mainnet**: Synthetix launched perpetual futures on Ethereum mainnet in a capped launch with trading incentives, explicitly abandoning the multi-chain L2 strategy in favor of mainnet neutrality and composability (Synthetix blog, Cryptonomist).
- **2026 — "comeback year" roadmap**: the 2026 roadmap describes a ground-up rebuild positioning Synthetix as both a perp DEX and a stablecoin issuer. As of Q2 2026, multi-collateral margin is live with ETH (cbBTC planned), and full SNX buyback activation is gated on restoring the sUSD peg, which the team targets via 420-pool issuance/redemption mechanics and expects to stabilize around end-Q2 2026 (Synthetix 2026 roadmap, CoinMarketCap update 8 June 2026).

## Trading relevance

- **Perps venue**: Synthetix perps on mainnet compete with [[hyperliquid]], [[dydx]] and GMX; funding rates and open interest there are part of the on-chain derivatives picture.
- **sUSD depeg as event risk template**: the April 2025 depeg showed how a protocol-design change (SIP-420) can break a stablecoin's peg mechanism without any exploit — a structural risk checklist item for any stablecoin position. sUSD traded below peg for an extended period through 2025-2026.
- **SNX as a turnaround/event trade**: SNX traded around ~$0.50 in early 2026 (down from ~$1.88 in early 2025; verify current price on CoinGecko). Catalysts are explicit and dated: peg restoration, buyback activation, perps volume growth — making SNX a catalyst-driven trade rather than a passive hold.
- **Reflexivity warning**: SNX-collateralized sUSD embeds circular risk — falling SNX pressures the debt pool that backs sUSD, which pressures confidence in SNX.

## Key metrics (June 2026 — verify before use)

| Metric | Value | Source |
|---|---|---|
| SNX price | ~$0.50 (early 2026 reading; verify) | CoinGecko |
| sUSD peg | Below $1 through 2025; recovery targeted end-Q2 2026 | Synthetix blog |
| sUSD depeg low | ~$0.66-0.68 (18 April 2025) | Cointelegraph |
| Collateralization ratio | 200% (post SIP-420; was 750%) | Cointelegraph |

## Related

- [[defi]]
- [[ethereum]]
- [[stablecoins]]
- [[perpetual-futures]]
- [[decentralized-exchanges]]
- [[hyperliquid]]
- [[dydx]]
- [[uniswap]]
- [[curve-finance]]

## Sources

- Synthetix 2026 Roadmap — https://blog.synthetix.io/2026-roadmap/
- Synthetix sUSD Peg Update — https://blog.synthetix.io/synthetix-susd-peg-update/
- Synthetix Acquires Kwenta — https://blog.synthetix.io/synthetix-acquires-ecosystem-leading-perps-platform-kwenta/
- Withdrawal of the Derive Acquisition Proposal — https://blog.synthetix.io/the-withdrawal-of-the-derive-acquisition-proposal/
- Introducing Synthetix Perps on Ethereum Mainnet — https://blog.synthetix.io/synthetix-perps-on-ethereum-mainnet/
- Cointelegraph, "What happened to sUSD? How a crypto-collateralized stablecoin depegged" — https://cointelegraph.com/explained/what-happened-to-susd-how-a-crypto-collateralized-stablecoin-depegged
- The Block, "Synthetix proposes $27 million token swap to acquire options protocol Derive" — https://www.theblock.co/post/354222/synthetix-acquire-derive-lyra
- Cryptonomist, "Synthetix perps return to Ethereum with a capped launch" (12 Dec 2025) — https://en.cryptonomist.ch/2025/12/12/synthetix-perps-ethereum-launch/
- Verified via Perplexity (sonar) and web search, 2026-06-10.
