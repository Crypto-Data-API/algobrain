---
title: "Tokenization"
type: concept
created: 2026-08-25
updated: 2026-08-25
status: draft
tags: [crypto, defi, real-world-assets, smart-contracts]
aliases: ["Asset Tokenization", "On-Chain Tokenization", "Tokenized Asset"]
domain: [crypto, market-microstructure]
prerequisites: ["[[blockchain]]", "[[smart-contracts]]"]
difficulty: intermediate
related: ["[[real-world-assets]]", "[[liquid-staking]]", "[[stablecoins]]", "[[collateralization]]", "[[depeg-risk]]"]
---

**Tokenization** is the general process of minting a blockchain-native token that represents a claim on, or a unit of, value — whether that value originates natively on-chain (a staked position, a share of a liquidity pool) or off-chain (a government bond, a building, a fiat currency). It is the underlying pattern beneath nearly every structure in this wiki's crypto coverage: stablecoins, liquid-staking tokens, wrapped assets, NFTs, and real-world-asset (RWA) products are all specific applications of the same mechanism. This page covers tokenization as a mechanism one level up from any single application; for the deep, TradFi-specific treatment of tokenizing bonds, private credit, and real estate, see [[real-world-assets]].

## The General Mechanism

Every tokenized asset shares the same basic shape, regardless of what it represents:

1. **Underlying value** — the thing the token is a claim on. This can be self-contained on-chain state (an Ethereum validator's staked balance) or an off-chain asset that requires a trusted intermediary (a Treasury bill held by a custodian).
2. **Issuance** — a token is minted on a blockchain to represent a pro-rata or fixed claim on that underlying value, using a token standard: fungible tokens (the ERC-20 pattern) for interchangeable units, or non-fungible tokens ([[nft|ERC-721/ERC-1155]]) for unique claims.
3. **Custody model** — who (or what) actually holds the underlying value, and what stops the token from being minted without backing. This is the single most important variable in assessing a tokenized asset's risk, and it varies enormously by design (see below).
4. **Redemption mechanics** — the process by which a token can be converted back into the underlying value, which is what keeps the token's market price anchored to the value it represents.
5. **Legal or technical enforceability** — whether the token's holder actually has an enforceable claim on the underlying. For a pure on-chain claim (an LST redeemable via a smart contract), enforceability is code. For an off-chain asset, enforceability runs through courts, custodians, and securities law — a token is only as good as the legal structure standing behind it.

## Custody Models

Tokenization spans a spectrum of trust assumptions:

- **Fully on-chain / trustless** — the "underlying" *is* the smart contract state, so no off-chain custodian is needed. The clearest example is a liquid-staking token: [[liquid-staking|stETH or rETH]] represents a staked ETH position that is secured entirely by Ethereum's own consensus mechanism, not by a company holding assets in a vault.
- **Wrapped assets** — a custodian (often a multisig) locks a native asset one-to-one and mints a wrapped representation of it on a different chain or environment, so the asset can be used where it otherwise couldn't be (e.g., Bitcoin-backed value moving into Ethereum DeFi). This introduces a custodian trust assumption that a fully on-chain claim does not have; mispricing between a wrapped token and its underlying is a recurring, tradeable inefficiency — see [[wrapped-asset-triangular-arbitrage]].
- **Off-chain custody / SPV** — a regulated custodian or special-purpose vehicle holds a real-world asset, and the token is a claim on that vehicle rather than on the asset directly. This is the model used for tokenized Treasuries, private credit, and real estate; see [[real-world-assets]] for the compliance layer (KYC'd transfers, ERC-3643/ERC-1400 security-token standards) that this custody model typically requires.

## Native Crypto-Value vs. External-Asset Tokenization

Tokenization is often discussed only in the RWA sense — putting TradFi assets on-chain — but the mechanism is broader:

- **Tokenizing native crypto value.** [[liquid-staking|Liquid staking tokens]] tokenize a staked position; wrapped assets tokenize a coin's value on a foreign chain; liquidity-pool position tokens tokenize a share of an AMM pool. None of these require an off-chain custodian in the strict sense — they tokenize something that already exists natively on a blockchain.
- **Tokenizing external assets.** This is the RWA category proper — Treasuries, private credit, real estate, and other TradFi instruments represented as on-chain tokens via custodian/SPV structures. [[real-world-assets]] covers this application in depth, including market size (roughly $26-31B excluding stablecoins as of Q1-Q2 2026) and leading issuers like BlackRock's BUIDL and Ondo Finance.
- **Stablecoins** sit at the boundary: they are technically the largest tokenized-asset category (a tokenized claim on fiat currency) but are conventionally discussed separately from "RWA" because of their payment-token role rather than yield-bearing security role — see [[stablecoins]].

## Redemption Mechanics

How a token converts back into its underlying value determines how tightly its market price tracks fair value:

- **Burn-and-redeem** — the token is destroyed in exchange for the underlying, either instantly (for on-chain claims) or via a queue. Ethereum's staking-withdrawal queue is a well-known example where redemption can take days during periods of high exit demand, which is why liquid-staking tokens can trade at a discount to spot ETH during stress rather than redeeming immediately.
- **NAV-based pricing** — funds (most tokenized Treasury products) price the token against a published net asset value rather than a continuously updated exchange rate, so secondary-market price and NAV can diverge based on liquidity rather than solvency.
- **Rebasing vs. exchange-rate appreciation** — some tokenized claims (e.g., stETH) rebase the holder's balance to reflect accrued yield, while others (e.g., rETH) keep balance constant and let the token's exchange rate against the underlying rise — a distinction covered in [[liquid-staking]].

Whenever redemption is slow, gated, or discretionary, the token can trade away from its theoretical backing — this is the same underlying mechanism whether the asset in question is a stablecoin, an LST, or a tokenized RWA fund. See [[depeg-risk]] for the general treatment of what happens when that arbitrage loop breaks down, and [[terra-luna|Terra/UST]] for the canonical case of a tokenized-value peg failing catastrophically (May 2022).

## Trading and Investing Relevance

- **Redemption-friction arbitrage.** Any tokenized claim trading away from its redemption value creates an arbitrage opportunity bounded by how fast, cheap, and certain redemption actually is — the same structural trade recurs across wrapped assets, LSTs, and RWA fund tokens.
- **Custody risk is priced, not just theoretical.** A token's discount to its stated backing often reflects the market's assessment of custodian or smart-contract risk rather than pure liquidity — [[counterparty-risk]] and [[cross-chain-bridge-risk]] are the relevant risk categories to model when sizing a position in any tokenized asset.
- **Collateral use compounds the risk.** Tokenized assets are frequently used as [[collateralization|collateral]] in DeFi lending, meaning a redemption failure or depeg in the underlying tokenized asset can cascade into liquidations across unrelated positions — a dynamic documented after the 2022 Terra/UST and stETH stress events.
- **Legal enforceability varies by design, not by marketing.** Two tokens can look identical on-chain while having very different real-world claims behind them; understanding which custody model (fully on-chain, wrapped, or SPV) underlies a given token is a prerequisite to assessing tail risk, not an afterthought.

## Related

- [[real-world-assets]] — the TradFi-specific application of tokenization, in depth
- [[liquid-staking]] — tokenizing a native on-chain staked position
- [[stablecoins]] — the largest tokenized-asset category
- [[wrapped-asset-triangular-arbitrage]] — trading mispricing between a wrapped token and its underlying
- [[collateralization]] — how tokenized assets are used as DeFi collateral
- [[collateral]] — the broader collateral concept
- [[depeg-risk]] — what happens when a tokenized claim's redemption arbitrage breaks
- [[counterparty-risk]] — custodian and SPV risk in off-chain-backed tokens
- [[cross-chain-bridge-risk]] — risk specific to wrapped-asset custody models
- [[terra-luna]] — a canonical tokenized-value peg failure
- [[nft]] — non-fungible tokenization for unique claims
- [[smart-contracts]] — the infrastructure enforcing on-chain redemption
