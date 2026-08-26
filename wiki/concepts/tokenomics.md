---
title: "Tokenomics"
type: concept
created: 2026-08-25
updated: 2026-08-25
status: draft
tags: [crypto, defi, governance, staking, yield-farming]
aliases: ["Token Economics", "Token Economic Design"]
domain: [crypto, tokenomics]
prerequisites: ["[[defi]]", "[[governance-token]]"]
difficulty: intermediate
related: ["[[emissions]]", "[[token-unlock-supply-event]]", "[[staking]]", "[[liquidity-mining]]", "[[governance-token]]"]
---

**Tokenomics** (token economics) is the design of a crypto asset's supply, distribution, and incentive structure — the rules that determine how many tokens exist, who receives them and when, what makes anyone want to hold them, and what behavior the token is meant to encourage or discourage. Good tokenomics aligns token holders, users, and the protocol's long-term health; weak tokenomics reliably shows up in price charts as relentless sell pressure, regardless of how good the underlying product is. This page is the umbrella concept for token supply, distribution, value accrual, and incentive design — see [[emissions]] for scheduled issuance specifically, [[token-unlock-supply-event]] for trading the resulting supply shocks, and [[staking]] for the mechanism that most commonly pays out newly issued tokens.

## Supply Design

- **Max supply.** Some tokens have a hard cap (Bitcoin's 21M, Ethereum Classic's ~210.7M — see [[ethereum-classic]]); others have no cap and issue indefinitely. A hard cap does not by itself make a token deflationary — what matters is the *rate* of issuance relative to demand growth.
- **Inflationary vs. deflationary.** An inflationary token continuously mints new supply (typically to pay staking or liquidity-mining rewards); a deflationary token removes supply over time through burns. Many tokens are both simultaneously — new emissions offset partly or fully by burns — making the net supply trajectory the number that actually matters, not the headline "max supply" figure.
- **Fixed vs. elastic supply.** Most tokens have a supply schedule fixed at launch (a known emissions curve). A smaller set use elastic or algorithmic supply that expands or contracts in response to market conditions — Olympus's treasury-backed OHM design and various now-defunct algorithmic stablecoins (including [[terra-luna|Terra's UST]]) are examples of elastic-supply experiments, several of which failed catastrophically when the mechanism's assumptions broke under stress.

## Distribution and Allocation

Where the initial and ongoing supply goes shapes both governance concentration and sell pressure:

- **Typical allocation splits** across major token generation events divide supply among the team, early investors/VCs, a treasury/foundation, and the community (airdrops, liquidity mining, public sale). Team and investor allocations commonly range from 15-30% combined, though this varies widely by protocol.
- **Vesting cliffs.** Team and investor tokens are almost never liquid at launch — they vest over months or years, often with an initial "cliff" (e.g., 12 months) before any tokens unlock, followed by linear or stepped release. Large cliff unlocks are a well-documented, tradeable source of sell pressure — see [[token-unlock-supply-event]] and [[token-unlock-arbitrage]] for how this is exploited systematically.
- **Concentration risk.** A token distribution concentrated in a small number of wallets (team, VCs, or a small early community) reproduces the same plutocracy and whale-capture risks discussed on the [[dao]] page, since token-weighted governance and token concentration are two views of the same underlying problem.

## Value Accrual Mechanisms

A token needs a reason for holders to want to hold it beyond pure speculation. Common mechanisms:

- **Fee capture.** Protocol revenue is distributed to token holders or stakers — MakerDAO's stability fees and DAI Savings Rate, or Curve's veCRV fee share, are examples (see [[makerdao]], [[curve-finance]]).
- **Buyback-and-burn.** Protocol revenue is used to buy the token on the open market and destroy it, permanently reducing supply. Uniswap's December 2025 "UNIfication" vote — which activated the protocol fee switch and immediately burned 100M UNI (~$600M) — is a recent, large-scale example of a governance token converting from pure voting rights into a cash-flow-linked, deflationary asset (see [[uniswap]]).
- **Staking yield.** Holders lock tokens to secure a network or backstop a protocol and earn a yield paid from emissions or fees — see [[staking]] for the general mechanism and [[liquid-staking]] for the tradeable-derivative version of it.
- **Governance rights** alone (no direct cash flow) is the weakest form of value accrual, and many governance tokens trade at what amounts to a persistent discount to their theoretical influence because voter participation is low — see [[governance-token]].

## Incentive Design: Sinks and Faucets

Sustainable tokenomics requires balancing where tokens enter circulation ("faucets" — emissions, mining rewards, airdrops) against where they leave or get locked ("sinks" — burns, staking locks, vote-escrow locks, fee payments). A protocol with strong faucets and weak sinks prints tokens faster than anything absorbs them, and price bears the cost. [[liquidity-mining|Liquidity mining]] is the textbook faucet-heavy design: Compound's June 2020 launch of COMP rewards to lenders and borrowers ignited "DeFi Summer," pushing total value locked across DeFi from under $1B to over $10B within months — but much of that capital was **mercenary capital**, chasing the emission yield itself rather than the protocol's underlying utility, and it exited just as fast once emissions were cut or a higher-yielding farm appeared elsewhere. Protocol-owned liquidity (Olympus's "(3,3)" bonding model, see [[olympus]]) and vote-escrow locking (Curve's veCRV, see [[curve-finance]]) both emerged as direct responses to the mercenary-capital problem — attempting to convert rented liquidity into owned or committed liquidity. Not every alternative design has held up: Olympus's original high-APY OHM staking model saw its backing-per-token and price both collapse from 2021 peaks as the reflexive bonding mechanism ran in reverse during the 2022 bear market, a widely cited cautionary case for elastic-supply, yield-driven tokenomics.

## How Weak Tokenomics Fails

- **Hyperinflationary emissions crushing price.** When a token's staking or liquidity-mining APY is funded almost entirely by new issuance rather than real fee revenue, the yield is a wealth transfer from the token's future buyers to its current sellers — the APY is compensation for dilution, not free money. Once new buyers stop absorbing the emissions, price declines faster than the yield can compensate for.
- **No real sink.** A token with faucets (emissions) but no meaningful sink (nothing burns it, locks it, or requires holding it) has no structural floor under sell pressure; every emitted token is a candidate seller with no offsetting source of demand.
- **Governance capture via concentrated allocation.** When team and early-investor allocations dominate circulating (or votable) supply, "decentralized" governance can function as insider control well past the point where it appears in a public token distribution chart — see [[dao]] for the governance-side failure modes this produces (plutocracy, low-quorum exploitation) and [[governance-attacks]] for how attackers exploit concentrated or borrowable voting power directly.
- **Unlock overhangs.** Even well-designed tokenomics can produce a predictable price drag in the run-up to a large cliff unlock, as the market prices in the anticipated new supply before it actually arrives — the core mechanism behind [[token-unlock-supply-event]] and [[token-unlock-arbitrage]].

## Trading and Investing Relevance

- **Emissions schedules are public and modelable.** Because vesting and emission curves are typically defined in a smart contract or published token-generation-event terms, the resulting supply overhang is forecastable rather than surprising — see [[emissions]] and the CryptoDataAPI token-unlock data referenced on [[token-unlock-supply-event]].
- **Circulating-supply-to-FDV ratio is a standard screen.** A token with a small circulating supply relative to its fully diluted valuation has a large latent unlock overhang; comparing current market cap to FDV is a quick first check on future dilution risk.
- **Value-accrual mechanism determines what kind of asset you actually hold.** A pure governance token, a fee-capturing token, and a staking-yield token respond to very different catalysts (governance votes, protocol revenue, and net emissions respectively) even when they trade in the same sector.
- **Mercenary-capital dynamics are a leading indicator for TVL sustainability.** A sharp rise in TVL driven primarily by a new liquidity-mining program (rather than organic usage growth) tends to reverse once emissions taper — a pattern worth checking against emission-schedule data before treating a TVL spike as a durable signal.

## Related

- [[emissions]] — scheduled token issuance, the primary tokenomics "faucet"
- [[token-unlock-supply-event]] — trading strategy built on vesting-cliff unlock pressure
- [[token-unlock-arbitrage]] — related unlock-driven arbitrage strategy
- [[staking]] — the dominant mechanism for distributing new emissions and creating a supply sink
- [[liquid-staking]] — the tradeable-derivative form of staked tokenomics
- [[liquidity-mining]] — the canonical faucet-heavy incentive design and mercenary-capital case study
- [[governance-token]] — the instrument most tokenomics designs are built around
- [[dao]] — the governance structure that concentrated allocation can compromise
- [[governance-attacks]] — exploits enabled by concentrated or borrowable voting power
- [[uniswap]] — buyback-and-burn value accrual (UNIfication, 2025)
- [[curve-finance]] — vote-escrow (veCRV) sink design
- [[olympus]] — protocol-owned liquidity and an elastic-supply cautionary case
- [[dtao]] — a market-based alternative to emission-schedule design
- [[terra-luna]] — algorithmic elastic-supply failure case
- [[ethereum-classic]] — fixed hard-cap supply design example
