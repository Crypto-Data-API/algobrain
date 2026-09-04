---
title: "Token Emissions"
type: concept
created: 2026-07-19
updated: 2026-09-05
status: good
tags: [crypto, staking, yield-farming, governance]
aliases: ["Emissions Schedule", "Token Issuance", "Inflation Schedule", "Emission Rate"]
domain: [crypto, tokenomics]
prerequisites: ["[[tokenomics]]"]
difficulty: beginner
related: ["[[token-unlock-supply-event]]", "[[tokenomics]]", "[[staking]]", "[[cryptodataapi-supply]]", "[[token-unlocks]]", "[[liquidity-mining]]", "[[proof-of-work]]", "[[bitcoin-halving]]", "[[governance-token]]", "[[liquid-staking]]"]
---

# Token Emissions

**Token emissions** are the scheduled, continuous issuance of new tokens into circulation — staking rewards, liquidity-mining incentives, and proof-of-work mining rewards being the three most common sources. Unlike a one-off cliff unlock, emissions arrive as a steady drip (per block, per epoch, or per day), which makes them less dramatic than a single large unlock event but, over time, a more persistent source of sell pressure: every emitted token is a potential seller with no offsetting buy pressure unless something absorbs it. Emissions are a core input to [[tokenomics|tokenomics]] design and to the unlock/supply-event strategies that trade the resulting dilution.

## Emissions vs. Unlocks — Two Different Supply Events

It is easy to conflate emissions with unlocks because both add circulating supply, but the wiki (and [[cryptodataapi|CryptoDataAPI]]'s own data model) treats them as distinct:

| | **Emissions** | **Cliff unlocks** |
|---|---|---|
| Shape | Continuous drip — per block/epoch/day | Discrete, dated events |
| Source | Staking rewards, mining rewards, liquidity-mining incentives | Vesting schedules for team, investor, and ecosystem allocations |
| Predictability | Governed by a protocol-level emission curve, known in advance | Governed by a token-generation-event vesting contract, known in advance |
| Typical size per event | Small, ongoing | Often large relative to daily volume, concentrated on one date |

[[cryptodataapi-supply|CryptoDataAPI's Supply category]] draws exactly this line in its data model: `GET /api/v1/supply/unlocks` is explicitly documented as **"a cliff calendar, not an emissions feed"** — continuous drip (mining inflation, linear vesting, runs of identical daily releases) is deliberately excluded from that endpoint, because mixing it in with real cliffs would bury the discrete catalysts that actually move price around a specific date. See [[token-unlocks]] for the narrative treatment of cliff-driven supply pressure specifically. This page covers the emissions side of that same distinction — the steady drip, not the calendar of cliffs.

## Emission Schedule Types

Protocols choose an emission schedule shape at design time, and the shape determines how the dilution pressure evolves over the asset's life:

- **Fixed and decaying (disinflationary).** Bitcoin's block-reward halving is the canonical example: a fixed subsidy per block that cuts in half on a fixed schedule (roughly every four years), producing an emission curve that asymptotically approaches a hard cap. See [[bitcoin-halving]]. Because the decay is scheduled and public, the market can (in principle) price in future emission cuts well ahead of time.
- **Fixed and non-decaying.** A constant number of tokens minted per block or epoch indefinitely — mechanically simple, but with no cap the token is permanently inflationary unless a burn mechanism offsets it (see [[tokenomics#Incentive Design: Sinks and Faucets|Sinks and Faucets]] on the [[tokenomics]] page).
- **Inflationary, target-rate.** Many proof-of-stake networks and DeFi protocols target a fixed *annual inflation rate* (e.g., "mint enough new tokens to pay X% APY to stakers") rather than a fixed token count — the actual token count minted then scales with total supply, so the dilution rate can stay roughly constant in percentage terms even as raw issuance grows.
- **Programmatic / incentive-driven.** [[liquidity-mining|Liquidity-mining]] emissions are typically set by governance as a reward budget for a specific pool or campaign, often front-loaded to bootstrap TVL and then tapered — Compound's June 2020 COMP distribution that ignited "DeFi Summer" is the archetype (see [[tokenomics]]).

## How Emissions Dilute Holders

Emissions dilute existing holders in a straightforward mechanical sense: if you hold a fixed number of tokens and total supply grows, your ownership share of the network or protocol shrinks, even if you never sell. The practical question for a holder or trader is not "are there emissions?" (almost every proof-of-stake and liquidity-mining protocol has them) but **"does the emission rate exceed the growth in real demand for the token?"** When emissions are used to pay a headline staking or farming APY that is funded almost entirely by new issuance rather than real protocol revenue, that yield is a wealth transfer from future buyers (who absorb the new supply) to current recipients (who are paid in newly minted tokens) — the APY compensates for dilution, it is not free money on top of it. This is the same dynamic [[tokenomics]] describes under "hyperinflationary emissions crushing price": once new buyers stop absorbing the emitted supply, price declines faster than the yield can compensate for.

Circulating-supply-to-fully-diluted-valuation (FDV) ratio is the standard quick screen for latent emission-driven dilution: a token with a small circulating supply relative to its FDV has a large share of its eventual supply still to be emitted (or unlocked), meaning today's price is being set by a small fraction of the tokens that will eventually exist.

## Emissions and Tokenomics Design: Cliffs vs. Linear Emission

[[tokenomics|Tokenomics design]] treats emissions as one of the primary "faucets" that must be balanced against sinks (burns, staking locks, fee payments) — see the [[tokenomics#Incentive Design: Sinks and Faucets|Sinks and Faucets section]] of that page for the general framework. Within that framework, the *shape* of how team and investor tokens enter supply is a deliberate design choice with different sell-pressure signatures:

- **Vesting cliffs** concentrate dilution into discrete, forecastable dates — a large tranche unlocks all at once, creating a visible overhang the market can price in ahead of time and that traders can position around directly (see [[token-unlock-supply-event]] and the broader [[token-unlocks]] narrative treatment).
- **Linear (continuous) emission** smooths the same total dilution across many small releases, avoiding a single sharp supply shock but producing the same "relentless sell pressure" pattern that weak tokenomics design tends to show up as — a persistent, low-grade headwind rather than a dated event.

Neither shape is inherently better: a cliff-heavy schedule is easier to trade around but can produce sharp, painful drawdowns on the unlock date; a linear-emission schedule is gentler day-to-day but harder to time and can quietly grind price down for years if demand growth never catches up to the emission rate. Well-designed tokenomics generally uses vesting cliffs (with an initial lockup) for team/investor allocations and continuous, tapering emission for ecosystem/incentive budgets — front-loading the discrete, disclosed events and smoothing the ongoing, demand-dependent ones.

## Trading and Investing Relevance

- **Emission schedules are public and modelable** — because they are typically defined in a smart contract or published token-generation-event terms, the resulting dilution is forecastable, not a surprise; the same cannot always be said for governance votes that later change the emission rate.
- **Net emissions, not headline max supply, is the number that matters** — many tokens run emissions (a faucet) and burns (a sink) simultaneously, so the *net* supply trajectory after burns is the figure worth modeling, not the advertised "max supply."
- **Staking/liquidity-mining APY should be decomposed** — separate the portion of a headline yield that comes from real fee revenue versus the portion that is simply newly emitted tokens; the latter is dilution wearing a yield costume.
- **Watch for emission-schedule changes via governance** — a protocol can vote to increase or decrease its own emission rate, which is itself a tradeable catalyst distinct from the originally scheduled curve.

## Related

- [[tokenomics]] — the umbrella concept for supply, distribution, and incentive design that emissions feed into
- [[token-unlock-supply-event]] — the strategy that trades discrete cliff-unlock supply pressure, the counterpart event type to continuous emissions
- [[token-unlocks]] — narrative/data treatment of unlock supply pressure, and the source of the emissions-vs-unlocks distinction this page follows
- [[staking]] — the dominant mechanism that pays out newly emitted tokens
- [[liquid-staking]] — the tradeable-derivative form of staked, emission-earning positions
- [[liquidity-mining]] — the canonical incentive-driven emissions program and its mercenary-capital risk
- [[proof-of-work]] — the mining-reward emission model underlying Bitcoin and similar chains
- [[bitcoin-halving]] — the scheduled decay event in Bitcoin's fixed emission curve
- [[governance-token]] — emissions frequently target governance-token distribution
- [[cryptodataapi-supply]] — the CryptoDataAPI data category that explicitly separates the cliff-unlock calendar from continuous emissions

## Sources

- [[cryptodataapi-supply]] — wiki source page documenting CryptoDataAPI's explicit emissions-vs-cliff-unlock data distinction (fetched from https://cryptodataapi.com/api/docs, 2026-09-02)
- [[tokenomics]] — wiki concept page for the sinks-and-faucets framework and the hyperinflationary-emissions failure mode this page builds on
- General knowledge of proof-of-work halving schedules, proof-of-stake inflation targeting, and liquidity-mining incentive design, cross-checked against the cited wiki pages
