---
title: "Delegated Proof of Stake"
type: concept
created: 2026-07-19
updated: 2026-09-06
status: good
tags: [crypto, governance, staking]
aliases: ["DPoS", "Delegated PoS", "Delegated Proof-of-Stake"]
domain: [market-microstructure]
prerequisites: ["[[consensus-mechanism]]", "[[proof-of-stake]]"]
difficulty: intermediate
related: ["[[consensus-mechanism]]", "[[proof-of-stake]]", "[[proof-of-work]]", "[[tron]]", "[[bnb-chain]]", "[[hive]]", "[[steem]]", "[[ark]]", "[[gxchain]]"]
---

# Delegated Proof of Stake

**Delegated Proof of Stake (DPoS)** is a consensus mechanism in which token holders vote to elect a small, fixed-size set of validators — variously called "witnesses," "block producers," or "Super Representatives" depending on the chain — who take turns producing blocks in rotation. It is a deliberate variant of [[proof-of-stake|Proof of Stake]] that trades decentralization for throughput and speed: instead of a large, pseudo-randomly sampled validator set (as in Ethereum-style PoS), DPoS concentrates block production in a small, known committee (typically **21 to 101 seats**) so blocks can be produced and finalized far faster and cheaper. [[tron|TRON]] and EOS are the canonical examples; the design lineage traces back to BitShares/Graphene, and this page covers the mechanism generally — see [[consensus-mechanism]] for how it fits alongside Proof of Work, plain Proof of Stake, and BFT-style consensus.

## How It Works

1. **Token holders vote** — anyone holding the chain's native token can vote for candidate validators, typically weighted by the amount of stake behind each vote. Holders who do not want to run a validator themselves can **delegate** their voting weight to a chosen block producer, who shares a portion of block rewards back with delegators — the origin of the "delegated" in DPoS.
2. **A fixed committee is elected** — the top N vote-getters (21 for EOS's original design, 27 for TRON's Super Representatives, 51 for ARK's delegates) become the active validator set for a given period, re-elected on a rolling or periodic basis.
3. **Validators take turns producing blocks** — rather than competing (as in Proof of Work) or being randomly sampled per-slot (as in large-validator-set PoS), the elected committee produces blocks in a **round-robin schedule**, which is what makes DPoS block times fast and predictable (commonly 1-3 seconds).
4. **Underperforming or misbehaving validators can be voted out** — because the committee is small and re-elected regularly, token holders can in principle replace a validator that goes offline or acts maliciously simply by redirecting votes, without needing a formal slashing mechanism (though some DPoS chains layer slashing-like penalties on top).

## Tradeoffs vs. Plain Proof of Stake

DPoS is best understood as a throughput-first point on the same design spectrum as [[proof-of-stake|Proof of Stake]]:

- **What it buys** — sub-3-second block times, high transaction throughput, and low, predictable fees, because a small, known committee does not need the more elaborate randomized-sampling and attestation-aggregation machinery that a large PoS validator set (Ethereum has hundreds of thousands of validators) requires to reach consensus efficiently.
- **What it costs** — a validator set one to several orders of magnitude smaller than a large PoS chain's, concentrating block-production power in relatively few hands. This raises collusion and censorship risk (a cartel of top validators could in principle coordinate to exclude transactions or extract value) and makes the network's neutrality more dependent on the good behavior of a small group than a chain with thousands of independent validators.
- **Voter participation in practice** — DPoS's legitimacy depends on token holders actually voting thoughtfully for validators. In practice, voter turnout on several DPoS chains has been low and concentrated among large holders and exchanges, and EOS in particular drew sustained criticism for **vote-buying dynamics** — accusations that top block-producer candidates paid voters (via reward kickbacks or direct incentives) to secure and retain their seats, effectively turning validator elections into a bidding contest rather than a merit-based selection. This is the standard critique leveled at DPoS governance and a large part of why the design is viewed as more collusion-prone than either Proof of Work or a large-validator-set Proof of Stake chain.

## Canonical Examples

- **[[tron|TRON]]** — 27 elected **Super Representatives (SRs)** produce blocks on a roughly 3-second cadence; TRX holders stake to obtain "TRON Power" and vote. TRON is the highest-profile living DPoS chain by market cap, and its high throughput and low fees are the main reason it became the dominant settlement rail for USDT.
- **EOS** — one of the original and most-cited DPoS designs, launched in 2018 with **21 elected block producers**; also a frequent subject of the vote-buying and cartel-behavior criticism described above.
- **[[hive|Hive]]** and **[[steem|Steem]]** — a DPoS fork pair (Hive forked from Steem in 2020) in which token holders elect "witnesses" to produce blocks; optimized for high-frequency, feeless social-media and posting transactions rather than DeFi settlement. See both pages for how their post-fork governance legitimacy diverged despite near-identical DPoS mechanics.
- **ARK** — runs DPoS with **51 elected delegates** producing blocks in a fixed rotation, an explicit design choice for fast, deterministic block production.
- **GXChain** — combines DPoS (a small set of elected "trustnodes" producing blocks, in the BitShares/Graphene lineage shared with EOS) with a project-specific Proof of Credit Share layer for its data-economy use case.

## A Hybrid Case: BNB Chain's Proof of Staked Authority

**[[bnb-chain|BNB Chain]]** is sometimes loosely described as a DPoS chain, but its actual consensus — **Proof of Staked Authority (PoSA)** — is a deliberate **hybrid** of Proof-of-Authority and Delegated Proof of Stake, not plain DPoS. Like DPoS, PoSA elects a small validator set (~21 seats in the original "Cabinet") based on staked/delegated BNB, and that set rotates block production on a fast, predictable schedule. The "Authority" component layers identified, pre-vetted validator status on top of the stake-weighted election that a purely open DPoS chain like EOS or TRON relies on — meaning BNB Chain's validator legitimacy rests partly on staked-token voting (the DPoS element) and partly on validator identity/authority (the PoA element), rather than on stake-weighted voting alone. This distinction matters for risk assessment: describing BNB Chain flatly as "a DPoS chain" understates the authority/identity layer its own design documentation emphasizes. See [[bnb-chain]] for the full detail, including the October 2022 bridge exploit where the small, coordinated PoSA validator set was able to halt the chain quickly — the same centralization that draws structural criticism also enabled a fast emergency response, illustrating the double edge of any small-committee consensus design, DPoS or PoSA alike.

## Trading Relevance

- **Settlement-finality due diligence** — a chain's validator-set size and concentration directly affects its censorship resistance and collusion risk; this is a relevant factor before sizing any position that depends on fast, final settlement (bridging, large withdrawals, exchange deposit crediting) on a DPoS or PoSA chain versus a larger-validator-set alternative.
- **Throughput as a feature, not just a technical detail** — DPoS's fast, cheap blocks are precisely why TRON became the dominant USDT settlement rail and why Hive/Steem-style chains can support high-frequency, low-value social transactions that would be uneconomical on a slower or more expensive chain.
- **Governance/vote-buying headline risk** — a DPoS chain's validator elections are a recurring, chain-specific governance narrative (EOS's cartel accusations, the Steem/Hive fork's contested witness legitimacy) that can matter for a token's credibility and community trust independent of its price action.
- **Don't conflate PoSA with plain DPoS** — as the BNB Chain case shows, some chains marketed loosely as "DPoS-like" run a hybrid design with materially different trust assumptions; check the specific consensus mechanism before assuming EOS/TRON-style dynamics apply.

## Related

- [[consensus-mechanism]] — the general framework DPoS sits inside, alongside PoW, PoS, and BFT designs
- [[proof-of-stake]] — the parent design DPoS specializes for throughput
- [[proof-of-work]] — the original consensus family DPoS chains explicitly avoid
- [[tron]] — 27 Super Representatives; the highest-profile living DPoS chain
- [[bnb-chain]] — Proof of Staked Authority, a DPoS/Proof-of-Authority hybrid, not plain DPoS
- [[hive]], [[steem]] — witness-based DPoS fork pair
- [[ark]] — 51-delegate DPoS design
- [[gxchain]] — DPoS combined with a project-specific credit-share layer

## Sources

- [[consensus-mechanism]] — wiki concept page cross-checked for the DPoS definition, EOS/TRON examples, and the "early BNB Chain used a related design" framing this page expands on
- [[tron]] — wiki entity page verifying TRON's 27 Super Representatives and DPoS consensus detail
- [[bnb-chain]] — wiki entity page verifying BNB Chain's Proof of Staked Authority design as an explicit PoA/DPoS hybrid (not plain DPoS), cross-checked to keep the two pages consistent rather than contradictory
- [[hive]], [[steem]], [[ark]], [[gxchain]] — wiki entity pages verifying each chain's DPoS witness/delegate mechanics
- General knowledge of DPoS design and the EOS vote-buying/cartel criticism, cross-checked against the cited wiki pages; no specific external source document has been ingested for this page
