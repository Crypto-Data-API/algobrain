---
title: "sudoswap"
type: entity
entity_type: protocol
founded: 2022
website: "https://sudoswap.xyz"
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, nft, defi, ethereum, market-microstructure, liquidity, algorithmic]
aliases: ["Sudoswap", "sudoAMM", "sudo"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-arbitrage]]", "[[ethereum]]", "[[opensea]]", "[[blur]]", "[[tensor]]", "[[seaport]]"]
---

sudoswap is an on-chain automated market maker (AMM) for NFTs on Ethereum, launched July 2022 by pseudonymous developer 0xmons. Unlike orderbook-based marketplaces such as [[opensea]] or [[blur]], sudoswap lets anyone create a bonding-curve liquidity pool ("sudo pool") that quotes a continuously updated bid and ask for a specific NFT collection. This made sudoswap the first widely used NFT-native DEX model and a conceptual template for later venues including Tensor's TAMM (see [[tensor]]).

> **2026 status update:** sudoswap is still operating but at a much reduced scale versus its 2022-2023 peak. As of early-2026 it carried only ~$1.16M total value locked (primarily on [[ethereum|Ethereum]]), and has expanded deployments to Base, Berachain, and Arbitrum. The SUDO governance token trades far below its February 2023 all-time high of ~$4.16 (circulating ~25M of a 60M max supply); a notable governance event was a DAO "rage quit" proposal that triggered sharp SUDO price moves. No protocol exploit or formal sunset has been reported (Verified via web search, 2026-06-11).

## How it works

A liquidity provider creates a **pair pool** that holds some combination of NFTs and ETH (or an ERC-20). The pool enforces a **bonding curve** defining how price moves after each trade:

- **Linear curve** — price moves up by a fixed `delta` ETH after each buy, and down by the same amount after each sell.
- **Exponential curve** — price moves by a multiplicative `delta` percent after each trade.
- **XYK (constant product)** — classic `x * y = k` curve, analogous to Uniswap v2, where pool reserves determine price.

Pools come in three types: **buy-only** (ETH in, quotes bids), **sell-only** (NFTs in, quotes asks), and **trade pools** (two-sided, quote both bid and ask with a configurable spread). Trade-pool LPs earn the spread, analogous to a traditional market maker.

All logic lives in immutable, open-source smart contracts. There are no off-chain orderbooks and no centralized matching engine; every trade is an on-chain swap against a specific pool.

## Fees and tokenomics

- **Protocol fee**: 0.5 percent on each trade, paid to the sudoswap treasury.
- **Trade-pool fee**: configurable by the LP, retained as spread.
- **Creator royalties**: optional on sudoswap, enforceable only via whitelist/blocklist systems (the same royalty-enforcement tension that defines the modern NFT market — see [[blur]], [[tensor]]).
- **SUDO token**: governance token introduced after launch; does not sit in the trade path.

## What traders use it for

- **Cheap floor-sweeping** — pool asks are often tighter than orderbook listings, especially for mid-tier collections where orderbook spreads are wide.
- **Liquidating bags** — sellers dumping 20-100 NFTs prefer AMM pools because one transaction hits a continuous curve instead of crossing dozens of discrete orderbook bids.
- **Market making** — sophisticated LPs deploy trade pools on popular collections and earn the configured spread plus price-drift profits.
- **Arbitrage against orderbooks** — bots constantly arbitrage between sudoswap pools and [[opensea]] / [[blur]] listings when bid/ask levels cross (see [[nft-arbitrage]]).
- **Fractional-style exposure** — rather than owning a specific NFT, a trader can hold an LP position that tracks the collection's average selling price.

## Risks and limitations

- **Inventory risk for LPs** — if the floor falls and sellers dump into a pool, the LP accumulates NFTs above the new market price. Conversely, if the floor rallies, NFTs are sold out of the pool too cheaply. Both are direct analogues of impermanent loss.
- **Thin-collection pricing is fragile** — bonding curves assume a statistically homogeneous collection. Trait-level rarity variance means pools can be adversely selected (sellers dump rare-trait NFTs in; buyers only sweep common-trait NFTs out).
- **Royalty optionality** — sudoswap not enforcing royalties by default drove early political controversy in the NFT space.
- **No ERC-721A / metadata checks at trade time** — LPs that deposit rare NFTs into a generic floor-price pool may sell them below trait value.
- **Smart contract risk** — immutable contracts also mean no kill switch if a vulnerability is found.

## Related

- [[tensor]] — Solana marketplace that integrated a sudoswap-style AMM (TAMM) alongside an orderbook
- [[blur]] — orderbook-based Ethereum counterpart
- [[seaport]] — the orderbook-style protocol from which sudoswap deliberately departs
- [[nft-arbitrage]]
- [[nft-trading]]

## Sources

- sudoswap official site and docs: [https://sudoswap.xyz/](https://sudoswap.xyz/), [https://docs.sudoswap.xyz/](https://docs.sudoswap.xyz/)
- DefiLlama — sudoswap (SUDO) protocol: [https://defillama.com/protocol/sudoswap](https://defillama.com/protocol/sudoswap)
- CoinGecko — sudoswap (SUDO) price/market data: [https://www.coingecko.com/en/coins/sudoswap](https://www.coingecko.com/en/coins/sudoswap)
- Verified via web search, 2026-06-11
