---
title: "Liquidity Providers"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, liquidity, market-microstructure]
aliases: ["Liquidity Providers", "Liquidity Provider", "LP", "LPs"]
related: ["[[liquidity-pools]]", "[[impermanent-loss]]", "[[automated-market-maker]]", "[[yield-farming]]", "[[uniswap]]"]
domain: [defi, market-microstructure]
difficulty: intermediate
---

A liquidity provider (LP) is a participant who deposits assets into an [[automated-market-maker|automated market maker (AMM)]] [[liquidity-pools|liquidity pool]] so that others can trade against those reserves. In exchange for supplying capital and bearing risk, LPs earn a share of the trading fees the pool generates. LPs are the decentralized-finance analogue of traditional [[market-making|market makers]], but instead of quoting bids and asks on an order book, they passively post capital to a pricing curve and let an algorithm do the quoting. Anyone with the relevant tokens can become an LP -- it is a permissionless role -- which is what allows [[decentralized-exchanges|DEXs]] like [[uniswap|Uniswap]], Curve, and Balancer to bootstrap liquidity without professional intermediaries.

## Overview

When a user becomes an LP, they typically deposit an equal value of two tokens (e.g. ETH and USDC) into a pool. In return they receive **LP tokens** (or, on Uniswap v3, an NFT position) representing their proportional claim on the reserves plus accrued fees. As traders swap against the pool, each swap pays a fee -- commonly 0.05%, 0.30%, or 1.00% on Uniswap depending on the tier -- which is added to the reserves and accrues pro-rata to LPs. Withdrawing ("burning" the LP token) returns the LP's current share of both tokens, which will have rebalanced according to the [[automated-market-maker#constant-product|constant-product]] (x·y=k) or other pricing formula.

The economic proposition for an LP is a wager: **fee income versus [[impermanent-loss|impermanent loss]] plus risk.** If the fees earned over the holding period exceed the divergence loss caused by price movement, the LP profits relative to simply holding the two tokens.

### Worked example (qualitative)

An LP deposits $5,000 of ETH and $5,000 of USDC into a constant-product pool ($10,000 total). Two scenarios:

- **ETH +50%, low fees.** The [[automated-market-maker|x·y=k]] curve forces the pool to sell ETH into the rally, so the LP ends with *less* ETH than if they had simply held — a divergence (impermanent) loss of roughly 2% of position value versus holding. If swap fees over the period earned only ~1%, the LP **underperforms holding** by ~1%.
- **ETH +50%, high volume.** Same price move, but a busy high-fee pool earns ~4% in fees over the period. Now fees (4%) exceed the ~2% impermanent loss, and the LP **beats holding** net.

The example shows the LP's core trade-off in one line: *fees must out-earn divergence loss.* Volatile pairs widen the IL term; high volume and wider fee tiers widen the fee term. Note that impermanent loss only becomes *permanent* if the LP withdraws while prices remain diverged.

## How LPs Earn

| Revenue source | Description |
|----------------|-------------|
| **Swap fees** | The core income; a cut of every trade, proportional to the LP's pool share |
| **[[liquidity-mining]] rewards** | Bonus governance/incentive tokens emitted by the protocol to attract liquidity (see [[yield-farming]]) |
| **Trading-fee tiers** | Higher-fee pools (e.g. 1%) compensate for more volatile/illiquid pairs |

Fee yield is highly variable. A deep, high-volume stablecoin pool (e.g. USDC/USDT on Curve) may earn a low but steady single-digit APY with minimal impermanent loss. A volatile, low-cap pair may advertise a high APY that is wiped out the moment prices diverge.

## Passive vs. Professional LPs

The introduction of **concentrated liquidity** (Uniswap v3, May 2021) split the LP population into two very different cohorts.

| Dimension | Passive LP | Professional / active LP |
|-----------|-----------|--------------------------|
| Strategy | Deposit and hold; wide or full-range | Tight ranges concentrated near spot price |
| Capital efficiency | Low | High -- earns far more fee per dollar deployed |
| Management | "Set and forget" | Constant rebalancing as price moves out of range |
| Impermanent loss | Moderate but diffuse | Severe if price exits the range; position goes 100% into one token |
| Who | Retail, treasuries, long-term holders | Quant firms, market-making desks, automated vaults |
| Tooling | None needed | Bots, hedging (perps/options), [[automated-market-maker|JIT]] liquidity, MEV awareness |

Concentrated liquidity rewards LPs who correctly predict where price will trade and actively manage their range -- effectively turning passive yield into an active market-making strategy. Studies of Uniswap v3 have repeatedly found that a large share of passive LPs underperform simply holding the assets once impermanent loss is accounted for, while a small cohort of sophisticated LPs and **JIT (just-in-time) liquidity** providers capture a disproportionate share of fees.

## Trading and Market Relevance

- LPs are the supply side of on-chain liquidity; the depth they provide directly determines [[slippage]] and execution quality for [[on-chain-trading|on-chain traders]].
- Professional LPing is a genuine [[market-making|market-making]] strategy with a real (if competitive) edge -- but it requires active hedging of [[impermanent-loss|inventory risk]], typically via perpetual futures or options on a CEX.
- The "LP as a yield product" narrative is frequently mis-sold: advertised APYs usually quote gross fee/reward yield and ignore impermanent loss, gas, and token-emission decay.

## Risks

- **[[impermanent-loss|Impermanent loss]]** -- the defining risk; divergence in the token-pair price ratio causes the LP to underperform holding. For volatile pairs it can dwarf fee income.
- **[[smart-contract-risk|Smart-contract risk]]** -- a bug or exploit in the pool or router can drain deposited funds.
- **Rug pulls / malicious tokens** -- providing liquidity for a scam token can leave the LP holding a worthless asset after the creator removes value.
- **Emission decay** -- [[liquidity-mining]] rewards that prop up a pool's APY decline over time; mercenary capital then leaves, thinning liquidity.
- **Out-of-range inactivity (v3)** -- concentrated positions stop earning fees and become fully exposed to the weaker asset when price exits the chosen band.

## Related

- [[liquidity-pools]] -- the structures LPs deposit into
- [[impermanent-loss]] -- the central risk LPs face
- [[automated-market-maker]] -- the mechanism LPs supply
- [[yield-farming]] -- maximizing LP returns with incentive rewards
- [[liquidity-mining]] -- protocols paying LPs in governance tokens
- [[market-making]] -- the traditional-finance analogue
- [[uniswap]] -- the leading venue for liquidity provision

## Sources

- General market knowledge; no specific wiki source ingested yet.
