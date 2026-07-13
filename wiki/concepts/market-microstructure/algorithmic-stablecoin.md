---
title: "Algorithmic Stablecoins"
type: concept
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [crypto, defi, stablecoins, algorithmic-stablecoin]
aliases: ["algorithmic stablecoin", "algo stablecoin", "unbacked stablecoin"]
domain: [crypto, market-microstructure]
difficulty: intermediate
prerequisites: ["[[stablecoins]]", "[[defi]]"]
related: ["[[stablecoins]]", "[[terra-luna]]", "[[terrausd]]", "[[depeg-risk]]", "[[makerdao]]", "[[defi]]"]
---

An algorithmic stablecoin maintains its peg to a target price (usually $1 USD) using automated mechanisms — token minting/burning, arbitrage incentives, or rebasing — rather than holding dollar reserves in a bank account. Unlike fiat-backed stablecoins (USDC, USDT) that are redeemable 1:1 for dollars, or crypto-collateralized stablecoins ([[makerdao|DAI]]) that are overcollateralized with crypto assets, algorithmic stablecoins rely on market incentives and game theory to maintain their peg. This design is capital-efficient but fundamentally fragile under stress, as demonstrated by the [[terra-luna|Terra/LUNA collapse]] ($40B destroyed, May 2022).

## How Algorithmic Stablecoins Work

### Seigniorage / Mint-Burn Model (Terra/UST)

The most common design uses a two-token system:
- **Stablecoin** (e.g., UST): the dollar-pegged token
- **Governance/seigniorage token** (e.g., LUNA): absorbs volatility

**Peg maintenance mechanism:**
- If UST > $1: anyone can mint 1 UST by burning $1 worth of LUNA → supply increases → price drops to $1
- If UST < $1: anyone can burn 1 UST to receive $1 worth of LUNA → supply decreases → price rises to $1

The arbitrage is supposed to be self-correcting. But it assumes:
1. Arbitrageurs are always willing to participate (they aren't during panics)
2. The seigniorage token (LUNA) maintains value (it doesn't if confidence collapses)
3. The mechanism can absorb any amount of selling pressure (it can't — there's a reflexive death spiral)

### Rebase Model (Ampleforth)

The token's *supply* adjusts rather than the price:
- If price > $1: all wallet balances increase proportionally (inflationary rebase)
- If price < $1: all wallet balances decrease proportionally (deflationary rebase)

The market cap (price × supply) floats freely, but individual tokens are supposed to trend toward $1.

### Fractional-Algorithmic (Frax)

A hybrid: partially backed by collateral (USDC) and partially stabilized algorithmically. The collateral ratio adjusts based on demand — higher ratio during stress, lower during stability. Frax has since moved to fully-collateralized (100% collateral ratio) after the Terra collapse.

## The Death Spiral Problem

The fundamental vulnerability of algorithmic stablecoins is the **death spiral** — a reflexive feedback loop where loss of confidence becomes self-fulfilling:

```
Stablecoin depegs ($1 → $0.98)
  → Arbitrageurs burn stablecoin, mint governance token
    → Governance token supply inflates, price drops
      → Confidence in the system falls further
        → More stablecoin selling ($0.98 → $0.90)
          → More governance token minting → price crashes further
            → Governance token approaches zero → no incentive to arbitrage
              → Stablecoin goes to zero
```

This dynamic played out in real-time with [[terra-luna|Terra/LUNA]]:
- UST depegged from $1.00 on May 9, 2022
- LUNA supply hyperinflated from 340M tokens to 6.5 trillion as arbitrageurs burned UST
- LUNA price crashed from $80 to $0.0001
- UST stabilized at $0.02 — a 98% loss
- $40B in combined value destroyed in days

## Track Record

| Project | Type | Peak Market Cap | Outcome |
|---------|------|----------------|---------|
| [[terrausd|UST (Terra)]] | Mint-burn seigniorage | $18.7B | **Collapsed** — death spiral, May 2022 |
| Iron Finance (TITAN) | Partially algo | $2B TVL | **Collapsed** — death spiral, June 2021 |
| Basis Cash | Seigniorage bonds | ~$200M | **Failed** — never maintained peg |
| Empty Set Dollar | Rebase + bonds | ~$100M | **Failed** — peg abandoned |
| Ampleforth (AMPL) | Rebase | ~$700M peak | **Survives** but doesn't maintain $1; volatile market cap |
| Frax (FRAX) | Fractional-algo → fully collateralized | ~$1.5B | **Pivoted** to full collateralization after UST collapse |
| Ethena (USDe) | Delta-neutral hedge (crypto collateral + short perps) | ~$5B | Active as of 2025; novel design, not purely algorithmic |

No purely algorithmic stablecoin has maintained a reliable peg at scale over an extended period. Every major attempt has either collapsed, abandoned the algorithmic model, or operates at small scale with volatile peg adherence.

## Why They Keep Being Attempted

Despite the track record, algorithmic stablecoins are attempted repeatedly because:
1. **Capital efficiency**: No need to hold $1 of collateral per $1 of stablecoin — "creating money from nothing" is attractive
2. **Decentralization**: No reliance on traditional banking (unlike USDC, which depends on Circle/bank reserves)
3. **Seigniorage profits**: The governance token captures the value of stablecoin demand growth — extremely profitable if it works
4. **Academic appeal**: The mechanism is elegant in theory — arbitrage should maintain the peg

## Trading Lessons

1. **Reflexive mechanisms fail under reflexive conditions.** The arbitrage that maintains the peg requires confidence in the arbitrage itself. When confidence breaks, the mechanism accelerates the collapse instead of preventing it.
2. **"Algorithmic stablecoin" is a red flag for traders.** No purely algorithmic stablecoin has survived a serious stress test at scale. Treat them as high-risk, not as cash equivalents.
3. **Depegs create trading opportunities.** The UST depeg created profitable short opportunities on LUNA and arb opportunities on UST. See [[2022-05-terra-luna-depeg-arb]].
4. **Collateralization ratio is the key metric.** The further below 100% a stablecoin's effective collateralization, the higher the death-spiral risk.

## Related

- [[stablecoins]] — all stablecoin types compared
- [[terra-luna]] — the largest algorithmic stablecoin failure
- [[terrausd]] — UST specifically
- [[depeg-risk]] — the risk of stablecoin peg loss
- [[makerdao]] — crypto-collateralized stablecoin (overcollateralized, not algorithmic)
- [[2022-05-terra-luna-depeg-arb]] — trading the UST depeg

## Sources

_Content based on public documentation from Terra, Frax, Ampleforth, and Ethena; academic analysis of seigniorage mechanisms; and post-mortem analysis of UST collapse. No raw sources ingested._
