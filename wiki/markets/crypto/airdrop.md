---
title: "Airdrop"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["Airdrop", "Airdrops", "Token Airdrop"]
related: ["[[liquidity-mining]]", "[[defi]]", "[[ethereum]]", "[[on-chain-analysis]]", "[[yield-farming]]"]
domain: [crypto, defi]
difficulty: beginner
---

An airdrop is the distribution of free [[crypto|crypto]] tokens to a set of wallet addresses, usually as a marketing tactic, a community-bootstrapping mechanism, or -- most consequentially -- a **retroactive reward** to early users of a protocol. Rather than selling tokens in an ICO, many projects now allocate a portion of their supply to be claimed by addresses that previously used the product, decentralizing ownership and rewarding adopters who took early risk. Airdrops have become one of the most lucrative and gamed activities in crypto: well-targeted recipients of the largest airdrops have received five- and six-figure windfalls, spawning an entire industry of "airdrop farming."

## Overview

The canonical event was **Uniswap's UNI airdrop in September 2020**, which granted 400 UNI to every address that had ever interacted with the protocol before a cutoff date. At launch UNI traded around $3-7, making the airdrop worth roughly $1,200-2,800 per wallet -- and far more at UNI's later highs. It established the template: reward genuine past users retroactively, with no claim required at the time of use, to decentralize governance and reward loyalty.

Subsequent landmark airdrops cemented the model and raised the stakes:

| Token | Project | Year | Notable detail |
|-------|---------|------|----------------|
| **UNI** | Uniswap | 2020 | 400 UNI to all prior users; defined the category |
| **dYdX** | dYdX | 2021 | Tiered by past trading volume |
| **ENS** | Ethereum Name Service | 2021 | Rewarded domain registrants; weighted by tenure |
| **ARB** | Arbitrum | 2023 | Large L2 airdrop; sybil-filtered eligibility |
| **OP** | Optimism | 2022+ | Multiple rounds; rewarded users *and* governance voters |
| **JTO / JUP / others** | Solana ecosystem | 2023-2024 | Revived airdrop mania on Solana |

## How Airdrops Work

- **Snapshot** -- the project picks a historical block height and records the state (balances, interactions) of qualifying wallets at that moment, so eligibility cannot be gamed after the fact.
- **Eligibility criteria** -- typically past usage (swaps, deposits, bridging, governance votes), often *tiered* by volume, frequency, or tenure to reward deeper engagement.
- **Sybil filtering** -- analysis to detect and exclude addresses controlled by a single actor pretending to be many users (see below).
- **Claim** -- eligible users claim via a contract within a window; unclaimed tokens are often returned to the treasury.

### Airdrop types

| Type | Trigger | Example pattern |
|---|---|---|
| **Retroactive** | Past usage before an undisclosed snapshot | Uniswap UNI (2020) — reward genuine prior users |
| **Tiered / weighted** | Usage scaled by volume, tenure, or frequency | dYdX, ENS — bigger users get more |
| **Points-program** | Accumulated "points" convert to tokens later | Modern emission-deferred farming campaigns |
| **Holder / staker** | Holding or staking another asset at snapshot | "Stake X, receive Y" distributions |
| **Lockdrop** | Locking capital for a period earns allocation | Time-weighted commitment rewards |

### Worked example (qualitative)

A user bridges $2,000 to a new pre-token rollup, makes a dozen swaps, supplies liquidity for a month, and votes in a governance test. At the undisclosed snapshot the protocol records this activity. When the token launches, a **tiered** formula maps the user's volume and tenure into an allocation — say 1,500 tokens. If the token opens around $1.50, that is a ~$2,250 claim. But the *realizable* value depends on selling into day-one liquidity before the farmer dump (below) compresses the price, and on the income-tax liability crystallized at claim — so the headline number rarely equals the cash kept.

## Airdrop Farming and Sybil Attacks

Because airdrops reward past usage, users now **speculatively farm** protocols that have not yet issued a token, hoping a future airdrop will reward their activity. This is the dominant motive behind much of the volume on new chains and protocols, and it has industrialized:

- **Airdrop farming** -- deliberately using pre-token protocols (bridging, swapping, providing liquidity, voting) to qualify for an expected future distribution. "Points programs" formalize this by promising a future token weighted by accumulated points.
- **Sybil attacks** -- a single farmer splits capital across hundreds or thousands of wallets to multiply their claim, since flat per-wallet airdrops reward address count, not capital. Industrial sybil operations script wallet creation and activity at scale.
- **Sybil defense** -- projects respond with on-chain clustering ([[on-chain-analysis]]), funding-graph analysis, behavioral heuristics, and proof-of-personhood, then exclude or down-weight detected sybils. Arbitrum and others publicly removed large numbers of flagged addresses before distribution.

This is an arms race: tighter criteria push farmers toward more "organic-looking" behavior, raising the cost of meaningful on-chain activity for everyone.

## Market and Tax Dynamics

- **Sell pressure ("the dump")** -- a large fraction of airdrop recipients sell immediately, since the tokens were free and many recipients are mercenary farmers with no conviction. This produces a characteristic price pattern: a high opening valuation followed by sustained selling as claimants and farmers exit. Listing an airdropped token therefore often means stepping in front of a wall of cost-basis-zero supply.
- **Float and unlock overhang** -- airdrops are usually only one slice of supply; team, investor, and ecosystem allocations unlock later, adding further dilution that traders must price in.
- **Taxation** -- in many jurisdictions (e.g. the US per IRS guidance), airdropped tokens are treated as **ordinary income at fair market value when received/claimed**, with a later capital gain or loss on disposal. This creates the trap of owing tax on a token's claim-day value even if it subsequently crashes before the recipient sells.
- **Reflexive hype** -- the *expectation* of an airdrop can itself inflate a protocol's metrics (TVL, transaction count), which farmers then unwind once the token lands.

### Tax treatment (general, not advice)

Rules vary by jurisdiction; the table sketches a common US-style pattern and is **not tax advice** — consult a professional.

| Event | Typical treatment | The trap |
|---|---|---|
| **Receipt / claim** | Ordinary income at fair market value when dominion received | Tax due on claim-day value even if you never sell |
| **Later sale** | Capital gain/loss vs. claim-day cost basis | Token can crash below the taxed value, leaving tax owed on phantom gains |
| **Record-keeping** | Need timestamp, FMV, and tx hash at claim | Sparse data on new tokens makes valuation hard |

The combination of "income on claim" plus "crash before sale" is the canonical airdrop tax pitfall: a recipient can owe more tax than the tokens are ultimately worth.

## Trading and Market Relevance

- Airdrops are a recurring **catalyst** event; traders monitor eligibility snapshots, claim windows, and exchange listings for volatility opportunities.
- Farmed activity distorts on-chain metrics, so analysts discount TVL and usage on pre-token protocols for likely airdrop-driven inflation.
- The day-one selloff pattern makes freshly airdropped tokens a common short / fade candidate, balanced against squeeze risk from low initial float.

## Related

- [[liquidity-mining]] -- a related, ongoing form of incentive distribution; airdrops are its retroactive cousin
- [[yield-farming]] -- airdrop farming is an extension of yield-chasing behavior
- [[on-chain-analysis]] -- the toolkit used for sybil detection and eligibility
- [[defi]] -- the ecosystem where airdrops are most prevalent
- [[ethereum]] -- the chain of most landmark airdrops

## Sources

- General market knowledge; no specific wiki source ingested yet.
