---
title: "Depeg Risk"
type: concept
created: 2026-04-10
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management, stablecoins, liquidity]
aliases: ["depeg", "depeg risk", "depegging", "peg risk", "de-peg"]
domain: [risk-management, crypto]
difficulty: intermediate
prerequisites: ["[[stablecoins]]", "[[liquid-staking]]", "[[counterparty-risk]]"]
related: ["[[liquid-staking]]", "[[smart-contract-risk]]", "[[stablecoins]]", "[[terra-luna]]", "[[counterparty-risk]]", "[[oracle-manipulation]]", "[[liquidation-risk]]", "[[cross-chain-bridge-risk]]", "[[liquidity-risk]]", "[[stablecoin-attestations]]", "[[arbitrage]]"]
---

Depeg risk is the danger that a token engineered to track a fixed exchange rate with another asset — typically 1:1 with USD for stablecoins, or near-1:1 with ETH for [[liquid-staking|liquid staking tokens]] — loses that peg and trades meaningfully below par. Some depegs are temporary and recoverable, resolved within hours or days by arbitrageurs exercising the redemption mechanism; others are terminal, wiping out holders and triggering cascading liquidations across DeFi. Depeg risk is one of the three primary axes of DeFi risk alongside [[smart-contract-risk]] and [[counterparty-risk]].

## Overview and Mechanics

A "peg" is a market price an issuer or protocol promises to defend. The defense rests on an **arbitrage redemption loop**, not on a price oracle. Under normal conditions:

- If the token trades **below** par (e.g. USDC at $0.98), arbitrageurs buy it on the open market and redeem it with the issuer for $1.00 of the underlying reserve asset, pocketing the spread. This buying lifts the secondary price back toward par.
- If the token trades **above** par, arbitrageurs mint new tokens at $1.00 and sell them, increasing supply and pushing price down.

The peg holds **only as long as redemption is reliable, fast, and uncapped**. The structural fragility is that the loop has two failure points:

1. **Redemption is broken or gated.** If the issuer suspends redemptions, imposes a [[liquidity-risk|redemption gate]], or the underlying reserve is frozen/insolvent, the arbitrage cannot run. Price is then held only by market confidence, which evaporates under stress. The depth and duration of a depeg scale directly with how impaired the redemption path is.
2. **Reserves are insufficient or wrongly valued.** If the backing is fractional, illiquid, or held at a failing counterparty, the redemption claim itself is worth less than par — so arbitrage stops at the true reserve value, not at $1.00.

The size of a *recoverable* depeg is roughly bounded by the round-trip arbitrage friction:

```
max sustainable discount ≈ redemption fee + gas/transfer cost + redemption delay carry + perceived redemption-failure probability
```

When that last term — perceived probability of redemption failure — jumps from near-zero to material, the bound blows out and the discount can gap far below the mechanical floor. That is the moment a "tight" peg becomes a "broken" peg.

### Soft peg vs hard peg vs algorithmic

- **Fiat-collateralized (hard) stablecoins** (USDC, USDT) — backed by off-chain cash/T-bills. Depeg driver is reserve/counterparty doubt; recovery depends on the banking and attestation layer (see [[stablecoin-attestations]]).
- **Crypto-collateralized stablecoins** (DAI) — over-collateralized by on-chain assets. Depeg driver is collateral crash plus liquidation backlog; the over-collateralization buffer is the defense.
- **Algorithmic stablecoins** (the failed UST model) — "backed" by a sister token via a mint/burn loop with no exogenous reserve. The most fragile: the same mechanism that defends the peg accelerates the collapse once confidence breaks (the death spiral).
- **Liquid staking / restaking tokens** (stETH, rETH, rsETH) — track the redemption value of staked ETH. Depeg driver is redemption latency (withdrawal queues) and on-chain liquidity depth, not reserve doubt.

## Stablecoin Depegs

- **USDC / March 2023** — Silicon Valley Bank collapsed with ~$3.3B of Circle's reserves (~8% of USDC backing) trapped inside. Over a weekend USDC traded as low as **$0.87–$0.88 on 2023-03-11** on secondary venues before U.S. authorities announced SVB depositors would be made whole; the peg restored to ~$1.00 by **2023-03-13** (Source: [[2023-03-usdc-svb-depeg]]). This is the canonical *reserve-counterparty* depeg: redemption was technically fine, but the reserve value was in doubt.
- **UST / May 2022** — Terra's algorithmic stablecoin lost its peg and collapsed to near zero within days, erasing roughly **$40B** in combined UST + LUNA market value when the mint-burn arbitrage entered a death spiral: UST holders redeemed for newly minted LUNA, hyperinflating LUNA supply and crushing both assets simultaneously. See [[terra-luna]].
- **USDT** — Tether has periodically wobbled 1–2% during confidence crises (2017, 2018, 2022) but has always recovered as redemptions cleared.
- **DAI** — has briefly traded *above* peg during stress when traders bid it up as a decentralized safe haven relative to centralized alternatives (notably during the March 2023 USDC event, since DAI was partly USDC-collateralized — a depeg-contagion linkage).

## LST / LRT Depegs

- **stETH / June 2022** — dropped to roughly **0.93 ETH** on secondary markets during the Three Arrows Capital and Celsius collapse. The depeg was a *liquidity-discount* event, not a solvency event: beacon-chain withdrawals were not yet enabled, so stETH could not be redeemed 1:1 for ETH — it could only be sold into on-chain AMM liquidity, and forced sellers (Celsius, 3AC) overwhelmed that liquidity. Once the Shapella upgrade enabled withdrawals in **April 2023**, the redemption arbitrage was restored and the peg tightened to near-zero discount.
- **cbETH, rETH** — historically trade tight to implied redemption value, with occasional small discounts during broad crypto drawdowns. Because their value *accrues* (1 LST > 1 ETH over time from staking rewards), the relevant peg is the on-chain exchange rate, not 1:1.
- **LRTs (rsETH, weETH, etc.)** — restaking tokens add an extra layer: their value depends on the underlying LST *and* the restaking/AVS layer *and* (when bridged) the [[cross-chain-bridge-risk|bridge]]. A bridge or smart-contract failure on the LRT can produce a depeg with no move in ETH at all.

## Causes of Depeg

- **Liquidity crisis** — forced sellers exhaust thin order books / AMM depth faster than arbitrage capital arrives.
- **Reserve doubts** — holders lose faith in the backing assets or the issuer's solvency (USDC/SVB).
- **Redemption failure** — the 1:1 redemption mechanism is disabled, delayed, gated, or capped.
- **Smart-contract exploit** — minting bug or reserve drain breaks the supply/backing relationship.
- **Algorithmic feedback failure** — reflexive mint/burn loops (UST) turn the peg defense into the collapse accelerant.
- **Contagion** — one asset's depeg propagates through collateral linkages (DAI ← USDC) and shared liquidity pools.

## How Pegs Recover

Recovery requires the arbitrage loop to function. The fastest recoveries (USDC 72 hours, stETH after Shapella) follow restoration of credible, uncapped redemption. The slowest or non-recoveries (UST) occur when the redemption mechanism is itself the source of dilution, or when reserves are genuinely impaired. A practical leading indicator: watch whether the issuer **keeps redemptions open and honors them at par**. The moment redemption is paused or rate-limited, treat the peg as broken regardless of the current spot quote.

## Trading Relevance and Risk Management

Depeg risk is asymmetric and convex: holders earn a small carry (or zero) for sitting in a pegged asset and face a fat left tail. Practical management:

- **Monitor peg health continuously** for any pegged asset held at scale — secondary-market price, redemption status, reserve attestations ([[stablecoin-attestations]]), and on-chain liquidity depth.
- **Set hard exit thresholds.** A common rule: auto-exit (or hedge) if a stablecoin trades below $0.99 for more than a defined window, before the discount gaps. Pre-commit it; depeg panics are exactly when discretion fails.
- **Avoid leverage on pegged assets.** A minor depeg cascades violently through [[liquidation-risk|leveraged borrow positions]] — lending markets often price collateral off the *peg*, so a depeg can trigger liquidations even though the [[oracle-manipulation|oracle]] still reads $1.00, or vice-versa.
- **Prefer assets with live, uncapped redemption** over those relying purely on secondary-market arbitrage.
- **Treat redemption latency as a position cost.** For LSTs/LRTs, the withdrawal queue length is your effective exit time under stress; size accordingly.
- **Model depeg as a Bernoulli tail in backtests**, not as continuous noise: a small annualized probability of a 5–30% (recoverable) or 80–100% (terminal) loss-given-depeg, correlated with broad crypto stress regimes — depegs cluster with drawdowns, the worst possible time. The same modeling discipline applies as for [[cross-chain-bridge-risk|bridge failure]].
- **Diversify across multiple stablecoins / LSTs** rather than concentrating, but note the contagion linkage: assets sharing collateral or liquidity pools are not independent (DAI ← USDC).

## Related

- [[stablecoins]] — the asset class most exposed to depeg risk
- [[stablecoin-attestations]] — reserve transparency that bounds reserve-doubt depegs
- [[liquid-staking]] — LST/LRT depegs are a liquidity-and-latency phenomenon
- [[terra-luna]] — the canonical algorithmic-stablecoin death spiral
- [[smart-contract-risk]] — exploit-driven depeg cause
- [[counterparty-risk]] — reserve-custody risk behind fiat-backed depegs
- [[cross-chain-bridge-risk]] — bridged/wrapped tokens carry a separate depeg vector
- [[liquidation-risk]] — depegs cascade through leveraged positions
- [[oracle-manipulation]] — lending-market depegs interact with price feeds
- [[liquidity-risk]] — thin liquidity widens and deepens depegs

## Sources

- (Source: [[2023-03-usdc-svb-depeg]]) — USDC/SVB depeg low ($0.87–$0.88, 2023-03-11) and recovery (2023-03-13).
- Circle, "USDC and the SVB situation" / public reserve disclosures (March 2023).
- Terra/LUNA collapse post-mortems — see [[terra-luna]] for the death-spiral mechanics and ~$40B loss figure.
- Lido / Ethereum Shapella upgrade documentation — stETH redemption enablement (April 2023).
</content>
</invoke>
