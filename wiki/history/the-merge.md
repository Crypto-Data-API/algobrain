---
title: "The Merge (Ethereum)"
type: news
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [history, crypto, ethereum]
aliases: ["The Merge", "the-merge", "Ethereum Merge", "ETH Merge", "Ethereum PoS transition", "Paris upgrade"]
event_date: 2022-09-15
markets_affected: [crypto]
impact: high
verified: true
sources_count: 3
related: ["[[ethereum]]", "[[crypto-markets]]", "[[proof-of-stake]]", "[[proof-of-work]]", "[[bitcoin]]", "[[defi]]", "[[2022-09-ethereum-merge-fork-arbitrage]]", "[[staking]]", "[[ethereum-classic]]", "[[token-unlocks]]"]
---

**The Merge** was the September 15, 2022 upgrade that transitioned the [[ethereum|Ethereum]] blockchain from **proof-of-work (PoW)** mining to **proof-of-stake (PoS)** consensus. It was the most significant protocol change in Ethereum's history and one of the most anticipated events in [[crypto-markets|crypto]]: it cut Ethereum's energy consumption by roughly **99.95%**, ended ETH issuance to miners, and reshaped the asset's supply dynamics. The event was executed live, on a network securing tens of billions of dollars, without downtime.

## Background

When Ethereum launched in 2015 it used [[proof-of-work]], the same Nakamoto-style consensus as [[bitcoin|Bitcoin]], where miners expend electricity to produce blocks. From its earliest days the roadmap envisioned a move to [[proof-of-stake]], where validators post staked ETH as collateral instead of burning energy. The transition was repeatedly delayed across years of research and testing, becoming a long-running meme ("the Merge is six months away").

The mechanics were staged:

- **December 1, 2020** — the **Beacon Chain** launched as a separate PoS chain running in parallel, accumulating staked ETH (deposited at 32 ETH per validator) but not yet processing transactions. This was the "consensus layer" waiting to be bolted on.
- **2021-2022** — multiple testnet merges (Ropsten, Sepolia, Goerli) rehearsed the swap of the execution layer's consensus engine from PoW to the Beacon Chain.
- **September 6, 2022** — the **Bellatrix** consensus-layer upgrade activated, arming the trigger.
- **September 15, 2022** — the execution layer crossed a **terminal total difficulty (TTD)** threshold, at which point the **Paris** upgrade activated and the network produced its first PoS block. Mining stopped permanently.

## What Changed

| Dimension | Before (PoW) | After (PoS) |
|---|---|---|
| Consensus | Miners solving hashes | Validators staking 32 ETH |
| Energy use | ~70-110 TWh/yr (nation-scale) | ~0.01 TWh/yr (~99.95% reduction) |
| New ETH issuance | ~13,000 ETH/day to miners | ~1,600 ETH/day to validators |
| Security cost | Paid in electricity + hardware | Paid in slashable staked capital |
| 51% attack cost | Acquire hashpower | Acquire/stake majority of ETH (and risk slashing) |

The drop in issuance, combined with the [[ethereum|EIP-1559]] base-fee burn introduced in 2021, meant ETH could become **net deflationary** during periods of high network activity — the so-called "ultrasound money" narrative. In practice ETH's supply has oscillated around flat-to-slightly-deflationary depending on usage.

Critically, the Merge did **not** by itself reduce gas fees or increase throughput — those were left to later upgrades (Shanghai/Capella enabling withdrawals in April 2023, and the Dencun "blob" upgrade in March 2024 that cut layer-2 costs). A common pre-Merge misconception was that it would make transactions cheap; it did not.

## Market Reaction

The Merge was a textbook **"buy the rumour, sell the news"** event. ETH rallied roughly 100% from its June 2022 lows (~$880) into early September (~$1,800) on Merge anticipation, then **sold off after the upgrade completed**, drifting back toward $1,300 within weeks as the broader 2022 [[crypto-winter|crypto bear market]] and macro tightening reasserted control. Realized volatility around the event was high but the upgrade itself executed flawlessly, removing the technical tail risk that had been priced into options.

Several distinct trades clustered around the event:

- **PoW fork arbitrage.** Miners, made obsolete on the main chain, backed a contentious hard fork — **EthereumPoW (ETHW)** — that preserved proof-of-work. Holders of ETH at the fork block received ETHW airdrop tokens. This created a [[2022-09-ethereum-merge-fork-arbitrage|fork-arbitrage trade]]: capture the airdropped fork token while hedging ETH exposure. ETHW launched at a low single-digit-dollar value and bled out, as forks of this kind almost always do. [[ethereum-classic|Ethereum Classic (ETC)]] — the surviving 2016 PoW fork — also saw a temporary hashpower and price bump as displaced miners migrated to it.
- **Staking-yield repricing.** Post-Merge, staked ETH earned validator rewards (~4-5% then), making ETH a yield-bearing asset and seeding the **liquid-staking** sector ([[staking|Lido, Rocket Pool]]). However, staked ETH could not be withdrawn until the April 2023 Shanghai upgrade, so a discount on liquid-staking tokens (stETH) persisted and was itself a tradeable basis.
- **Implied-vol crush.** Options dealers saw event-vol collapse the moment the Merge completed without incident, a classic post-binary-event vega decay.

## Trading Lessons

1. **Anticipated catalysts are often priced in early.** The Merge's roadmap was public for years; the rally happened on the run-up, and the realized event was a sell. Trading a well-telegraphed upgrade by buying it on the day is usually late.
2. **Fork arbitrage is real but decays fast.** Airdropped fork tokens (ETHW) have a brief window of value before liquidity and miner support collapse. The edge is in the capture-and-hedge, not in holding the fork token. See [[2022-09-ethereum-merge-fork-arbitrage]].
3. **Read the actual spec, not the narrative.** The market widely (and wrongly) expected lower gas fees. Knowing that the Merge changed consensus, not capacity, was an information edge.
4. **Binary technical events crush vol.** Long-vol into a flawless upgrade is a losing trade once the binary resolves; the asymmetry favours selling event premium if you trust the execution.

## Aftermath

The Merge proved that a major live blockchain could swap its consensus mechanism without halting, validating the multi-year PoS research program. It set up subsequent upgrades — withdrawals (April 2023), proto-danksharding/blobs (March 2024) — and entrenched ETH's positioning as a programmable, yield-bearing, increasingly scarce asset. It also intensified the **regulatory question** of whether a staked, yield-bearing ETH is a security, a debate that featured in later US enforcement and the eventual approval of US spot ETH ETFs in July 2024.

## Related

- [[ethereum]] — the blockchain that underwent the transition
- [[proof-of-stake]] — the consensus model adopted
- [[proof-of-work]] — the consensus model retired on mainnet
- [[2022-09-ethereum-merge-fork-arbitrage]] — the ETHW fork-arbitrage trade
- [[staking]] — validator rewards and liquid staking that the Merge enabled
- [[ethereum-classic]] — the surviving earlier PoW fork
- [[crypto-markets]] — broader market context (2022 bear market)
- [[bitcoin]] — contrast: still proof-of-work

## Sources

- Ethereum Foundation, "The Merge" documentation and post-Merge upgrade notes (ethereum.org).
- On-chain data on ETH issuance and supply pre/post September 15, 2022.
- Contemporary market coverage of the Merge price action and the EthereumPoW (ETHW) hard fork, September 2022.
