---
title: "BendDAO"
type: entity
entity_type: protocol
created: 2026-04-22
updated: 2026-06-10
status: good
founded: 2022
website: "https://www.benddao.xyz"
tags: [crypto, nft, defi, ethereum, leverage, liquidity, risk-management]
aliases: ["Bend DAO", "Bend Protocol", "bendapp"]
related: ["[[nftfi]]", "[[blend]]", "[[nft]]", "[[nft-trading]]", "[[ethereum]]", "[[bored-ape-yacht-club]]", "[[cryptopunks]]", "[[azuki]]"]
---

BendDAO is a peer-to-pool NFT lending protocol on Ethereum. Depositors supply ETH to a shared pool and earn yield; borrowers deposit blue-chip NFTs (BAYC, Mutant Apes, CryptoPunks, Azuki, Doodles, CloneX, and others) as collateral and draw ETH against an LTV based on a floor-price oracle. BendDAO's August 2022 liquidity crisis is the canonical cautionary case study in NFT lending systemic risk and is widely cited in any design discussion of NFT-backed debt.

## How it works

### Pool structure

- **Depositors (lenders)** supply ETH to the lending pool and receive interest-bearing bendETH. Rates float based on utilization, similar to Aave or Compound.
- **Borrowers** deposit a supported blue-chip NFT into BendDAO's contract and receive an ETH loan up to the collection's configured LTV (historically in the 30-40 percent range of the oracle floor price).
- NFT holders also receive "boundNFT" tokens, which represent their collateralized position and preserve certain utility rights (airdrops, governance snapshots) while the NFT is posted.

### Liquidation mechanism (pre-crisis design)

When a borrower's health factor fell below one (e.g., the floor price dropped, pushing LTV above the liquidation threshold), BendDAO triggered a 48-hour auction:

- Initial ask was set at the current floor price from the oracle.
- Bidders had 48 hours to bid; the highest bid wins.
- If no bid cleared the reserve, the auction failed and the collateral sat on the protocol's books as bad debt.

This design worked only if at least one bidder was always willing to pay at least the oracle floor for a seized NFT.

## August 2022 liquidity crisis

In August 2022, during a broad NFT drawdown, the BAYC floor fell from roughly 90 ETH toward the mid-50s within weeks. Multiple large BendDAO-collateralized BAYC loans became liquidatable. Because the auction floor was tied to the (still elevated) oracle price and the 48-hour duration was long relative to how fast the market was moving, almost no bids cleared. The consequences:

- **Bad debt accumulated** on the protocol as auctions repeatedly failed.
- **Depositors ran** — bendETH holders tried to withdraw ETH from the pool; utilization spiked toward 100 percent, pushing deposit rates up and making withdrawals practically unavailable.
- **Governance vote** — BendDAO's DAO passed an emergency proposal to drastically change liquidation parameters: the auction duration was cut from 48 hours to 4 hours, the auction starting price was lowered substantially below floor to actually attract bids, and the liquidation threshold was raised (reducing max LTV). The interest rate model was also rebalanced to break the withdrawal crunch.
- **Protocol survived** but several borrowers strategically defaulted, and BendDAO was left holding a portfolio of foreclosed BAYCs that it later auctioned off over an extended period.

The episode is a textbook example of:

- **Mispriced tail risk** — pool-based NFT lending implicitly assumes an always-liquid buyer at oracle prices. That assumption fails precisely when liquidity is most needed.
- **Oracle lag** — floor-price oracles updated slowly relative to the sell-side's willingness to transact.
- **Reflexivity** — liquidation supply hitting the floor while bidders wait for lower auction prices creates a downward spiral specific to lending protocols.
- **Pool vs. peer-to-peer risk transfer** — unlike [[nftfi]] (which isolates each loan between two parties) and [[blend]] (which uses refinance auctions and no oracle), BendDAO's pool structure socialized bad debt across all depositors.

## Fees and tokenomics

- Borrowers pay interest to the pool, rate-dependent on utilization.
- A portion of interest accrues to the treasury and to BEND stakers (BEND is BendDAO's governance token).
- veBEND is a vote-escrowed version of BEND used for protocol governance (including the emergency parameter changes during the 2022 crisis).

## What traders use it for

- **Instant liquidity against blue-chip NFTs** — faster than [[nftfi]] because there is no per-loan negotiation.
- **Yield on ETH** — lenders earn variable APY from NFT borrowers; higher than most ETH-denominated DeFi rates during bull phases but highly uneven.
- **Leveraged buying** (bendDAO's "down payment" feature, added post-crisis) — similar in spirit to [[blend]]'s BNPL, but sourced from the pool.

## Risks and limitations

- **Tail-event bad-debt risk** — the 2022 crisis demonstrated that pool-based NFT lending breaks down when no buyers exist at the oracle price.
- **Oracle dependence** — TWAPs or manipulation-resistant oracles are slow; fast feeds are manipulable. There is no perfect NFT oracle.
- **Limited supported collections** — only a small whitelist of blue-chips is collateral-eligible, so the protocol is concentrated in BAYC, Mutant Apes, CryptoPunks, and a handful of others.
- **Governance-driven parameter changes** — as in 2022, protocol parameters can be adjusted suddenly in response to stress, which lenders and borrowers must monitor.
- **Competition from perpetual peer-to-peer** — [[blend]] has taken significant share from BendDAO by eliminating oracles and expirations entirely; BendDAO's continued relevance depends on whether pooled liquidity beats peer-to-peer matching for most users.

## Status (2025-2026)

NFT-backed lending as a category contracted sharply through the 2023-2025 NFT bear market: blue-chip floor prices (BAYC, CryptoPunks, Azuki) fell far below their 2021-2022 peaks, collapsing the addressable collateral base and lender appetite. BendDAO remains live as one of the original pooled NFT-lending venues, but activity is a fraction of its 2022 peak, and [[blend]] (oracle-free, perpetual peer-to-peer, integrated with Blur) captured much of the surviving demand. The protocol's enduring relevance is primarily as the **canonical case study** in pooled-NFT-lending tail risk rather than as a high-volume venue. (Note: current TVL/activity figures were not verifiable as of 2026-06-10; treat the 2022 crisis facts as the load-bearing content here.)

## Related

- [[blend]] — peer-to-peer perpetual alternative; explicitly designed to avoid BendDAO's oracle/liquidation failure modes
- [[nftfi]] — older peer-to-peer fixed-term alternative
- [[bored-ape-yacht-club]], [[cryptopunks]], [[azuki]] — primary collateral collections
- [[nft-trading]], [[nft]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
