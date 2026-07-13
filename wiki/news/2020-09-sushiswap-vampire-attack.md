---
title: "SushiSwap's Vampire Attack on Uniswap (Sep 2020)"
type: news
created: 2026-04-24
updated: 2026-06-12
status: good
tags: [news, crypto, defi, history, fork, governance, liquidity-mining]
event_date: 2020-09-09
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 5
related:
  - "[[sushiswap]]"
  - "[[uniswap]]"
  - "[[vampire-attack-arbitrage]]"
  - "[[airdrop-farming]]"
  - "[[sam-bankman-fried]]"
---

# SushiSwap's Vampire Attack on Uniswap (Sep 2020)

In late August and early September 2020, an anonymous developer using the pseudonym **"Chef Nomi"** launched [[sushiswap|SushiSwap]] — a near-direct fork of [[uniswap|Uniswap]] v2 — and bootstrapped it by paying SUSHI governance tokens to anyone who staked their Uniswap LP tokens on SushiSwap's farming contracts. Within two weeks, more than **$1B of liquidity** had migrated (or been positioned to migrate), Uniswap's TVL dropped from a peak near **~$1.8B to roughly $400-700M**, and the term "vampire attack" entered the DeFi vocabulary as the canonical name for this attack vector. The episode also kicked off **"DeFi Summer 2.0"** — the cascade of food-themed yield farms (YAM, CREAM, PICKLE, KIMCHI) that defined late 2020 in crypto.

## Timeline

| Date | Event |
|------|-------|
| 2020-08-26 | Chef Nomi deploys SushiSwap contracts; SUSHI emissions begin to Uniswap LP stakers (Pool 0 was UNI-V2 LP tokens) |
| 2020-08-28 - 09-04 | SUSHI rewards inflate emissions to ~1,000 SUSHI/block; TVL on SushiSwap-staked Uniswap LP positions exceeds $1B |
| 2020-09-05 | **Chef Nomi sells the developer fund** (~$14M of SUSHI) on the open market, drawing accusations of an exit scam ("rug pull") |
| 2020-09-06 | After community backlash, Chef Nomi pledges to return the funds and publicly apologises |
| 2020-09-06 | Chef Nomi transfers admin keys to **[[sam-bankman-fried|Sam Bankman-Fried]]** (then known primarily as the founder of [[ftx|FTX]] and Alameda Research), who takes emergency multisig control to manage "The Migration" |
| 2020-09-09 | **"The Migration"** executes: Uniswap LP tokens staked on SushiSwap are unwound, the underlying liquidity pulled from Uniswap, and re-deposited as native SushiSwap LP positions. Uniswap TVL drops sharply |
| 2020-09-10 | Chef Nomi returns the $14M of dev-fund proceeds to the SushiSwap treasury |
| 2020-09-17 | **Uniswap responds with the UNI airdrop** — 400 UNI per address that had ever interacted with Uniswap (~$1,200 at launch, peaked at ~$18,000 per address in 2021) |

## The Mechanism in Detail

The attack used Uniswap's own permissionless architecture against it:

1. **Stage 1 — Farming on the host.** SushiSwap's `MasterChef` contract accepted Uniswap v2 LP tokens (e.g., USDT-ETH, DAI-ETH) and emitted SUSHI rewards to depositors. The depositor still earned Uniswap trading fees *and* received SUSHI on top — a yield boost at zero apparent cost, because Uniswap had no native token and no way to retaliate in-kind.

2. **Stage 2 — The Migration.** SushiSwap's contract included a one-way migration function that, once triggered, would call `removeLiquidity` on Uniswap (returning the underlying tokens) and `addLiquidity` to SushiSwap's own pools. The economic effect was to drain Uniswap of the migrated capital and reconstitute it as SushiSwap liquidity.

3. **Stage 3 — Self-sustaining.** Once SushiSwap had deep liquidity, traders routed through it for better prices, generating fees that incentivised LPs to stay even after the initial SUSHI emissions tapered.

## Impact on Uniswap

- TVL fell from a peak near ~$1.8B to roughly ~$400-700M in the day surrounding "The Migration" (Sep 9, 2020) per [[defillama|DefiLlama]] historical data.
- Daily trading volume on Uniswap fell sharply for the following week.
- Uniswap's response — the UNI airdrop on **September 17, 2020** — was directly catalysed by the vampire attack. UNI's launch instantly created a $1B+ market cap and re-anchored liquidity to Uniswap; within weeks, Uniswap's TVL had recovered above SushiSwap's.

## Impact on the Broader Market

- The vampire attack template was copied immediately. **YAM Finance**, **CREAM**, **PICKLE Finance**, **KIMCHI**, **HOTDOG**, and dozens of other "food coin" farms launched in September-October 2020, each forking an existing protocol or pool and emitting a new governance token.
- The phrase **"DeFi Summer"** was coined retroactively for this period (June-October 2020); SushiSwap is generally considered the inflection point that turned a quiet research-focused DeFi sector into a mainstream speculation vehicle.
- The episode hardened the principle that **open-source DeFi protocols cannot rely on a moat** — anyone can fork the code and bootstrap liquidity with token incentives. Subsequent protocols (Curve, Balancer, Aave) launched with native tokens *from inception* partly to pre-empt this attack vector.

## Sam Bankman-Fried's Role

Chef Nomi's transfer of admin keys to [[sam-bankman-fried|SBF]] was, at the time, framed as a credible-stewardship move — SBF was respected in DeFi for arbitrage operations and had not yet developed his later notoriety. SBF executed The Migration, then transferred the keys to a 9-of-13 community multisig in late September 2020. This episode is sometimes cited as the start of SBF's public profile in DeFi governance — three years before the **2022-11 [[ftx|FTX]] collapse**.

## The Arb Trade

For arbers who were paying attention, the SushiSwap launch was a textbook [[vampire-attack-arbitrage|vampire attack arbitrage]] setup:

- Stake Uniswap LP tokens on SushiSwap from day one (Aug 26-28).
- Harvest SUSHI emissions and dump them on Uniswap's own SUSHI-ETH pool (which existed because SUSHI was an ERC-20 and trades anywhere).
- Migrate to SushiSwap proper after Sep 9 to capture native LP fees.
- Exit before SUSHI emissions tapered in October.

Realised APRs during the boost period were reportedly **>1,000% annualised**. The trade decayed rapidly: by mid-October 2020, SUSHI had fallen ~75% from its September peak, and the easy carry was gone.

## Aftermath and Legacy

- SushiSwap survived its turbulent launch and remained a top-10 DEX through 2024-2025, though it never recaptured Uniswap's dominance.
- Chef Nomi's true identity remains publicly unconfirmed.
- "Vampire attack" became standard DeFi terminology. Subsequent vampire attacks include:
  - **[[blur|Blur]] vs [[opensea|OpenSea]]** (NFT trading, BLUR airdrop February 2023)
  - **[[hyperliquid|Hyperliquid]] vs [[gmx|GMX]]** (perpetuals, HYPE airdrop late 2024)
  - **[[dydx-chain|dYdX v4]] vs [[ftx|FTX]]** (perp DEX migration after FTX collapse, 2022-2023)
  - **Friend.tech / various social-fi forks**
- The UNI airdrop on Sep 17, 2020 became the template for retroactive airdrops as a defensive token launch — copied by Optimism, Arbitrum, Blur, and dozens of other protocols.

## Trading Lessons

- **Open-source code is not a moat.** Any protocol that monetises only the contract logic can be forked overnight.
- **Token incentives can buy market position cheaply** — but the token must be sold *to someone* eventually, and the price reflects that.
- **Defensive token launches work.** UNI's Sep 17 airdrop neutralised SushiSwap within weeks. The lesson for incumbents: launch your token *before* the vampire arrives.
- **Migrations are reflexive.** As liquidity moves, prices on the destination improve, drawing more flow. As liquidity drains from the source, slippage worsens, accelerating the exodus.
- **Anonymous founder risk is real.** Chef Nomi's brief rug pull (and later return of funds) was a cleaner outcome than most; many subsequent vampire forks ended in actual exit scams.

See [[vampire-attack-arbitrage]] for the systematic strategy and [[airdrop-farming]] for the parallel discipline that emerged from the same era.

## Sources

- Chef Nomi / SushiSwap launch and migration announcements (Medium, Aug-Sep 2020).
- CoinDesk: "SushiSwap's Chef Nomi Returns $14M of Dev Funds After Community Backlash" (September 2020).
- The Block / Cointelegraph coverage of "The Migration" and SBF's emergency multisig role (September 9-10, 2020).
- Uniswap blog: "UNI token announcement" / retroactive airdrop (September 16-17, 2020).
- [[defillama|DefiLlama]] historical TVL data for Uniswap and SushiSwap.

## Related

- [[sushiswap]]
- [[uniswap]]
- [[vampire-attack-arbitrage]]
- [[airdrop-farming]]
- [[liquidity-mining]]
- [[sam-bankman-fried]]
- [[ftx]]
- [[defi-summer]]
- [[2022-05-terra-luna-depeg-arb]]
- [[2023-03-usdc-svb-depeg]]
