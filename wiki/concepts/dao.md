---
title: "DAO (Decentralized Autonomous Organization)"
type: concept
created: 2026-08-25
updated: 2026-08-25
status: draft
tags: [crypto, defi, governance, smart-contracts, history]
aliases: ["DAO", "Decentralized Autonomous Organization", "DAOs", "Decentralized Autonomous Organizations"]
domain: [crypto, governance]
prerequisites: ["[[smart-contracts]]", "[[defi]]"]
difficulty: intermediate
related: ["[[governance-token]]", "[[governance-attacks]]", "[[makerdao]]", "[[2016-06-the-dao-hack]]", "[[ethereum-classic]]"]
---

A **DAO (Decentralized Autonomous Organization)** is an organization whose rules, treasury, and decision-making are encoded in smart contracts and executed according to the outcome of member votes, rather than controlled by a traditional corporate hierarchy. Members typically coordinate through a [[governance-token|governance token]] that confers voting rights, and the DAO's treasury — often worth hundreds of millions of dollars — is spent only when a proposal clears a defined voting and execution process. This page covers the DAO as an *organizational structure*: how proposals move from idea to execution, how votes are counted, how treasuries are secured, and where the model has failed. For the token instrument itself (UNI, AAVE, COMP) see [[governance-token]].

## Overview

DAOs sit on a spectrum from fully on-chain to hybrid. At one end, a proposal's full lifecycle — submission, voting, and fund transfer — happens through smart contracts (the model pioneered by Compound's Governor Alpha/Bravo framework, forked by dozens of protocols). At the other end, a DAO uses gasless off-chain signaling (Snapshot, where votes are signed messages rather than on-chain transactions) and then has a human-controlled [[safe|Safe]] multisig execute whatever the vote decided. Most real-world DAOs — including [[makerdao|MakerDAO]] and [[uniswap|Uniswap]] — use some hybrid of the two, because fully trustless on-chain execution of arbitrary treasury transfers is itself an attack surface (see Failure Modes below).

## Proposal Lifecycle

1. **Temperature check / forum discussion** — a proposal is drafted and discussed informally (Discourse, Commonwealth, Discord) to gauge sentiment before it costs anything to submit.
2. **Formal proposal submission** — the proposer must hold or be delegated a minimum token threshold to submit an on-chain (or Snapshot) proposal.
3. **Voting period** — typically 3-7 days. A **quorum** requirement (commonly 4-10% of circulating supply, per [[governance-token]]) must be met for the vote to count, and a proposal usually needs a simple majority or supermajority to pass.
4. **Timelock** — winning proposals are queued with a mandatory delay (48 hours to 7 days) before execution, giving the community a window to notice and react to a malicious or buggy proposal before funds move.
5. **Execution** — the proposal's payload runs automatically (on-chain) or is executed manually by multisig signers (hybrid model).

## Voting Mechanisms

- **Token-weighted voting** — one token, one vote. The default and most common model; it is also inherently plutocratic, since voting power tracks capital rather than participation or expertise.
- **Delegation** — token holders assign their voting power to a delegate without transferring custody of the tokens, letting passive holders participate via trusted representatives. Compound popularized this model in 2020, and it is now standard across most major DAOs.
- **Vote-escrow (ve-) models** — tokens are locked for a fixed period (up to several years) in exchange for boosted voting weight and yield. [[curve-finance|Curve's]] veCRV is the canonical example, spawning an entire secondary market for vote-buying ("bribes") via Convex and Votium — see [[governance-token]] for the mechanics.
- **Quadratic voting** — the cost of casting additional votes on the same proposal rises with the square of vote count, intended to blunt whale dominance by making concentrated influence expensive. It remains largely experimental (e.g., as an optional strategy on Snapshot) rather than used for treasury-critical votes at major DAOs; a related but distinct mechanism, quadratic *funding*, has seen real production use in Gitcoin's grants-matching rounds.
- **Market-based emission allocation** — a newer alternative to voting altogether: [[dtao|Bittensor's dTAO upgrade]] (February 2025) replaced validator-voted emissions with a bonding-curve market that allocates emissions based on capital flows rather than ballots, illustrating that "governance" need not mean voting at all.

## Treasury Management and Execution

Because a DAO's treasury is a large, identifiable pool of assets, how it is secured matters as much as how spending decisions are made. Two patterns dominate:

- **Multisig custody** — a small set of trusted signers (often elected or founding-team members) hold keys to a smart-contract wallet like [[safe|Safe]] (formerly Gnosis Safe), and execute whatever a governance vote approved. This is faster and cheaper to build than fully on-chain execution but reintroduces a trust assumption in the signer set. [[gnosis|GnosisDAO]] — the protocol behind Safe itself — is a well-known example of a DAO whose own treasury and NAV-redemption mechanics are closely watched by traders.
- **Fully on-chain execution** — the timelock contract itself holds and disburses funds once a vote passes, with no human signer able to override or delay it. This removes signer-collusion risk but makes any bug in the governance contract itself a direct path to the treasury (see Failure Modes).

Many DAO treasuries are also concentrated in the protocol's own governance token rather than diversified into stablecoins or [[real-world-assets|RWAs]] — a structural weakness discussed further in [[tokenomics]].

## Legal Wrappers

By default, an unincorporated DAO risks being treated under U.S. law as a general partnership, exposing every voting token holder to personal liability for the DAO's actions. Wyoming addressed this in July 2021 by passing the first U.S. law explicitly recognizing the "DAO LLC" as a legal entity, letting a DAO register as a limited-liability company administered by its smart contract; the Marshall Islands passed similar DAO-recognition legislation in 2022. The liability question is not hypothetical: in September 2022 the CFTC sued Ooki DAO (a rebrand of bZx) for offering illegal leveraged trading and unregistered swaps, and in June 2023 a federal court entered a default judgment — including a $643,542 penalty and a shutdown order — after finding Ooki DAO could be treated as an unincorporated association whose token-holder voters bore responsibility for its conduct. The case is now a standard reference point for why protocols increasingly seek a formal legal wrapper before decentralizing governance.

## Notable Examples

- **[[makerdao|MakerDAO]] (founded 2014, DAI live December 2017)** — one of the longest-running DAOs, governing a protocol with roughly $8-10B in total value locked. MKR holders vote on collateral types, stability fees, and treasury allocation into [[real-world-assets|real-world assets]]; the DAO rebranded to Sky Protocol in September 2024, with MKR migrating to SKY.
- **[[uniswap|Uniswap]]** — UNI holders govern the largest decentralized exchange. In a landmark December 2025 vote ("UNIfication"), governance passed with 99.9% in favor to finally activate the protocol fee switch and route fees to UNI burns, alongside an immediate 100M UNI burn (~$600M) — converting a purely governance-rights token into a cash-flow-linked asset.
- **The DAO (2016)** — not to be confused with the general concept this page describes, "The DAO" was a specific 2016 crowdfunded investment vehicle on Ethereum that raised roughly $150M (about 15% of all ETH in circulation at the time). On June 17, 2016 an attacker exploited a reentrancy bug to drain 3.6 million ETH (~$60M at the time), crashing ETH's price ~35% in a day. The Ethereum community's response — a hard fork on July 20, 2016 at block 1,920,000 that returned the stolen funds — split the chain permanently into Ethereum (ETH, the forked chain) and [[ethereum-classic|Ethereum Classic]] (ETC, the chain that refused to roll back state on "code is law" grounds). See [[2016-06-the-dao-hack]] and [[2016-07-ethereum-dao-fork-arbitrage]] for the full history and the fork-arbitrage trade it created.

## Failure Modes

- **Voter apathy** — typical participation in DAO governance votes is only 5-15% of circulating supply, per [[governance-token]], meaning most "decentralized" decisions are actually made by a small, engaged minority.
- **Plutocracy and whale capture** — because voting power tracks token holdings, large holders (early investors, VCs, exchanges) can dominate outcomes; a sufficiently patient buyer can accumulate a controlling position on the open market and push through self-serving proposals — a hostile-takeover pattern documented in [[governance-attacks]].
- **Flash-loan and capital-based governance attacks** — an attacker who can temporarily borrow enough governance tokens to pass and immediately execute a malicious proposal can drain a treasury in a single transaction. [[2022-04-beanstalk-governance-attack|Beanstalk]] lost $182M this way in April 2022 (the largest governance attack on record); Build Finance DAO lost $470K in a similar slow-accumulation takeover in May 2022; Tornado Cash's governance was hijacked via fraudulent votes in February 2023. See [[governance-attacks]] for the full taxonomy and defenses (snapshot-based voting, time locks, quorum minimums).
- **Treasury mismanagement** — treasuries concentrated in a DAO's own native token are procyclical: the treasury's purchasing power collapses in exactly the bear-market conditions when the protocol most needs runway to fund development or incentives.

## Trading and Investing Relevance

- **Governance outcomes are tradeable events.** When a DAO vote determines the resolution of a hack or a fee-switch activation, the market-implied probability of that outcome can itself be traded — see [[governance-restitution-arbitrage]] for the pattern established after Euler Finance's 2023 hack and subsequent governance vote on the recovery deal.
- **Treasury composition informs NAV-style valuation.** Some governance tokens (GNO being a clear example) trade at a discount or premium to the protocol's disclosed treasury value, creating a tradeable structural setup distinct from pure narrative speculation.
- **Timelock windows are known-duration event risk.** Because execution is delayed by a fixed, public timelock after a vote passes, the period between "vote result known" and "funds actually move" is a predictable event window rather than a surprise.
- **Delegate concentration is a centralization signal.** A DAO where voting power is delegated to a handful of addresses is more exposed to the plutocracy and takeover risks above, regardless of its formal decentralization claims.

## Related

- [[governance-token]] — the token instrument that grants DAO voting rights
- [[governance-attacks]] — taxonomy of exploits against DAO governance
- [[2022-04-beanstalk-governance-attack]] — the largest flash-loan governance attack on record
- [[2016-06-the-dao-hack]] — the original 2016 DAO hack
- [[2016-07-ethereum-dao-fork-arbitrage]] — the ETH/ETC fork the hack triggered
- [[ethereum-classic]] — the chain that resulted from the fork
- [[hard-fork]] — the mechanism used to reverse the hack
- [[makerdao]] — one of the longest-running DAOs
- [[uniswap]] — UNI governance and the 2025 fee-switch vote
- [[safe]] — the multisig wallet standard used by most DAO treasuries
- [[gnosis]] — Safe's parent DAO and a treasury-NAV trading case study
- [[curve-finance]] — vote-escrow (veCRV) governance model
- [[dtao]] — a market-based alternative to voted governance
- [[tokenomics]] — treasury and incentive design as part of overall token economics
- [[real-world-assets]] — where DAO treasuries increasingly deploy capital
- [[smart-contracts]] — the infrastructure that makes DAO governance enforceable
