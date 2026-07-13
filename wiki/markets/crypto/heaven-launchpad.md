---
title: "Heaven Launchpad"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, solana, memecoin, launchpad, sniping]
aliases: ["Heaven", "Heaven Launchpad", "LIGHT/DARK"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://heaven.xyz"
related: ["[[pump-fun]]", "[[solana]]", "[[memecoin-sniping]]", "[[bonding-curve-analysis]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Heaven Launchpad

**Heaven** is a [[solana]] memecoin launchpad that briefly surged to the **#2 position** on Solana after launching its native LIGHT token (which posted 800%+ gains in its initial run). Its defining feature is a **dual-token model (LIGHT / DARK)** combined with a **100% revenue burn**, presenting a sharply different tokenomics design from [[pump-fun|Pump.fun]] (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

---

## Overview

Heaven entered the Solana launchpad market by leading with an aggressive, deflationary tokenomics narrative rather than purely on UX. The platform's pitch is that **all platform revenue is burned**, with the LIGHT/DARK dual-token structure encoding the protocol's economic flows.

The launch narrative drove a brief but pronounced surge: LIGHT reportedly returned 800%+ in its initial price action, and Heaven temporarily became the second-most-active Solana memecoin launchpad. As of this writing, it is one of several platforms competing for share that Pump.fun previously dominated alone (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]).

---

## How it works

Heaven follows the standard one-click launch shape used across Solana launchpads — bonding-curve issuance followed by DEX migration — with its differentiation concentrated in tokenomics rather than launch mechanics.

- Solana-native deployment, single-transaction launches
- [[bonding-curve-analysis|Bonding-curve]] price discovery on the platform
- Migration to a Solana AMM after the curve fills (presumed [[raydium]] / [[pumpswap]]-class venue)
- Native protocol tokens **LIGHT** and **DARK** capture and burn platform revenue

> **Data gap:** the specific roles of LIGHT vs. DARK (e.g., revenue claim, governance, fee discount, supply cap) are not detailed in our source set. The 100% burn directionality is confirmed; the routing is not.

---

## Tokenomics / fee model

Confirmed from sourced reporting (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]]):

- **100% revenue burn** — all (or substantially all) platform fee revenue is destroyed rather than being retained as treasury or distributed to a single token
- **Dual-token structure**: LIGHT and DARK
- LIGHT was the visible launch token and posted 800%+ early gains
- DARK exists as the counterpart in the dual-token model

> **Data gap:** exact fee rates, burn routing, the LIGHT/DARK supply schedules, and any locked/vesting structure are not in our source set. Treat all numerical claims about Heaven's tokenomics beyond "100% burn" and "LIGHT 800%+ early gain" as unverified.

---

## Comparison to Pump.fun

| Dimension | Heaven | [[pump-fun|Pump.fun]] |
|---|---|---|
| Chain | Solana | Solana, Base, Blast |
| Launch model | Bonding curve, fair-launch (assumed) | Bonding curve, fair-launch |
| Native token(s) | LIGHT + DARK (dual) | PUMP (single) |
| Revenue treatment | 100% burn (per reporting) | Treasury + revenue-share program |
| Differentiation lever | Tokenomics (deflationary) | UX, network effects, multi-chain |
| 2026 trajectory | Brief #2 surge after launch | Incumbent, defending share |

The comparison highlights the **two main strategic levers** competitors pull against Pump.fun: ecosystem alignment (LetsBonk → BONK) and tokenomics radicalism (Heaven → 100% burn).

---

## Trader strategies

- **Launchpad-launch token sniping** — when a launchpad releases its *own* native token (as Heaven did with LIGHT), the early window has historically been one of the highest-EV setups in this category (LIGHT 800%+ initial run is the canonical recent example). Treat such windows as their own distinct setup, not as standard memecoin launches.
- **Tokenomics-driven flow** — 100% burn narratives can attract sustained buy-side flow if revenue is real; pair Heaven price action with on-chain revenue/burn tracking to avoid trading the marketing rather than the cashflow.
- **Standard memecoin sniping** — see [[memecoin-sniping]] and [[bonding-curve-analysis]]; mechanics carry over from Pump.fun for tokens launched on Heaven's curve.
- **Migration sniping** — see [[token-migration-sniping]]; identify the curve-completion threshold and trade the DEX migration.
- **Hype-cycle fade** — launchpads showing brief #2/#3 surges have historically reverted as attention rotates to the next platform; consider mean-reversion or short-vol setups around peak hype.
- **Tooling** — check [[axiom-pro]], [[bonkbot]], and [[trojan-bot]] for Heaven support before scaling size.

See [[low-cap-crypto-trading-map]] for the broader framework these strategies sit in.

---

## Risks

- **Hype-cycle reversion** — brief surges to #2 frequently fade; launchpad attention is highly mobile (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]])
- **Tokenomics opacity** — dual-token models are easy to misread; LIGHT/DARK roles, supply, and burn routing should be verified before sizing
- **Smart-contract risk** — newer codebase, less battle-testing than Pump.fun
- **Reflexive risk** — if revenue (and therefore burn) drops, the deflationary narrative reverses quickly
- **Concentration risk** — early-launch native tokens often have concentrated holders; exit liquidity can degrade fast

---

## Sources

- (Source: [[2026-04-22-gap-finder-pump.fun-competitors-letsbonk-believe-mo]])

---

## Related

- [[pump-fun]]
- [[pumpswap]]
- [[raydium]]
- [[solana]]
- [[letsbonk]]
- [[sunpump]]
- [[believe]]
- [[moonshot]]
- [[memecoin-sniping]]
- [[token-migration-sniping]]
- [[bonding-curve-analysis]]
- [[low-cap-crypto-trading-map]]
- [[axiom-pro]]
- [[bonkbot]]
- [[trojan-bot]]
