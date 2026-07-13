---
title: "LP Vault Comparison"
type: comparison
created: 2026-05-05
updated: 2026-06-21
status: excellent
tags: [crypto, defi, vaults, comparison, yield, hyperliquid, gmx, jupiter, ethena, aave, liquity]
aliases: ["DeFi Yield Vault Comparison", "HLP vs GLP vs JLP vs sUSDe"]
related: ["[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-vault-architecture]]", "[[ethena-usde]]", "[[ethena]]", "[[aave]]", "[[liquity]]", "[[gmx]]", "[[hlp-cascade-alongside-playbook]]", "[[hyperliquid]]", "[[hlp]]", "[[liquidity-provider]]", "[[liquidity-pool]]", "[[multi-venue-capital-management]]", "[[counterparty-risk]]", "[[smart-contract-risk]]"]
subjects: ["[[hyperliquid-hlp-basis-arbitrage|HLP]]", "[[gmx|GLP/GM]]", "[[jupiter-jlp|JLP]]", "[[ethena-usde|sUSDe]]", "[[aave|aUSDC]]", "[[liquity|Stability Pool]]"]
comparison_dimensions: [APR, risk profile, capacity, lockup, smart-contract age, drawdown history]
---

# LP Vault Comparison

A trader sitting on $50k-$5M of stablecoin capital looking for **passive on-chain yield** has roughly six serious choices, each representing a fundamentally different bet on what generates the yield. This page compares **[[hyperliquid-hlp-basis-arbitrage|HLP]]** ([[hyperliquid|Hyperliquid]]), **[[gmx|GLP/GM]]** ([[gmx|GMX]] V1/V2), **[[jupiter-jlp|JLP]]** ([[jupiter-perps|Jupiter Perps]] on [[solana|Solana]]), **[[ethena-usde|sUSDe]]** ([[ethena|Ethena]]), **[[aave|aUSDC]]** ([[aave|Aave]]), and the **[[liquity|Liquity Stability Pool]]** along the dimensions that actually matter: realistic APR, what risk you are paid to bear, capacity, lockup duration, smart-contract age, and historical drawdowns.

Each of these is a form of [[liquidity-pool|liquidity-provision (LP) vault]], but the analogy is loose — the risk you bear differs sharply by protocol. The thesis: the high-APR vaults (HLP, JLP, GLP) all pay you to be the **counterparty to leveraged perp speculators**. The stablecoin vaults (sUSDe, aUSDC) pay you for **funding harvest or lending demand**. Liquity SP pays you for **buying liquidated ETH at a discount**. Stacking these makes the "vault complex" diversified across uncorrelated yield drivers — but each has a non-trivial tail risk that only shows up in regime breaks.

> All APR and TVL figures below are **as of late 2025 / early 2026**. Always verify on the protocol's own dashboard (or [[defillama|DefiLlama]]) before sizing a position. Yields move fast and TVL caps change.

## The Six Vaults at a Glance

| Vault | What It Is | APR (2025-2026) | TVL | Lockup | Chain | Contract Age | Max Historical DD |
|-------|------------|-----------------|-----|--------|-------|--------------|-------------------|
| **[[hyperliquid-hlp-basis-arbitrage\|HLP]]** | Protocol market-maker + liquidator on [[hyperliquid\|Hyperliquid]] | ~15-30% (compressed from earlier 60%+) | $300M-$1B | 4 days | HyperEVM (custom L1) | Live since 2023 | ~25% on JELLYJELLY incident; -5% March 2024 cascade |
| **[[gmx\|GLP/GM]]** | Multi-asset LP backstop for [[gmx\|GMX]] perps | 10-20% (V2 GM markets) | $400-700M | None | [[arbitrum\|Arbitrum]], Avalanche | V1 Sep 2021, V2 Aug 2023 | -25% during late-2022 trending tape |
| **[[jupiter-jlp\|JLP]]** | LP backstop for Jupiter Perps on [[solana\|Solana]] | 25-50% | $1B+ | ~1 hour exit fee window (no hard lock) | [[solana\|Solana]] | Live since late 2023 | -8% on memecoin volatility 2024 |
| **[[ethena-usde\|sUSDe]]** | Funding-rate-harvesting synthetic dollar ([[ethena\|Ethena]]) | 8-20% (regime-dependent) | $5B+ | 7-day cooldown | [[ethereum\|Ethereum]] | Live since Feb 2024 | <1% (briefly during ENA depeg risk Q2 2024) |
| **[[aave\|aUSDC]]** | Money-market lending baseline | 4-8% (variable) | Multi-billion | None (instant) | Many EVM chains | V1 2020, V3 2022 | Negligible; bad-debt episodes <0.1% impact |
| **[[liquity\|Liquity SP]]** | LUSD staked to absorb [[ethereum\|ETH]]-only liquidations | 5-10% LUSD APR + 5-10% LQTY rewards | ~$200M | None | [[ethereum\|Ethereum]] L1 | Live since April 2021, immutable | ~5% during Mar 2023 ETH dip (depositor recovered + 6% via ETH gains) |

The pattern: as you go up the APR curve you take on **newer chains, more concentrated counterparty exposure, and longer lockups**. The trade is real, not free.

## Comparison Dimensions Defined

Each dimension below is a distinct axis of the trade-off. A vault that wins on one almost always loses on another.

| Dimension | What It Measures | Why It Matters |
|---|---|---|
| **Realistic APR** | Net yield after the early-adopter spike compresses | Headline APR is a marketing number; the durable rate is lower |
| **Risk borne (what you're short)** | The specific tail you are paid to absorb | Two 15% vaults can be short completely different things |
| **Capacity** | $ you can deploy before market impact/APR-decay dominates | Determines whether the vault scales with your book |
| **Lockup** | How fast you can exit during stress | A high APR you can't escape in a crash is a trap |
| **Smart-contract age** | Battle-testing of the code | Older = fewer unknown-unknowns |
| **Drawdown history** | Worst realized loss and its cause | The empirical, not theoretical, tail |
| **Chain risk** | Outage / sequencer / validator exposure | Diversifying chains is the only mitigation |
| **Liquidity tier** | Instant vs cooldown vs hard lock | Governs use as reserve vs anchor capital |

## Risk/Return Profile Summary

A condensed view pairing each vault's expected return band with its dominant risk and the regime where it underperforms.

| Vault | Expected Return Band | Dominant Risk | Underperforms When | Liquidity Tier |
|---|---|---|---|---|
| **[[hlp\|HLP]]** | 12-30% (compressing) | Perp-trader edge + custom-L1 + thin-market manipulation | Coordinated thin-market squeeze; L1 fault | 4-day lock |
| **[[gmx\|GLP/GM]]** | 10-18% | Directional traders winning + oracle | Strong trending tape | Instant |
| **[[jupiter-jlp\|JLP]]** | 15-30% (uncertain) | [[solana\|Solana]] halt + newness | Memecoin liquidation cascade; chain halt | Soft (~1h fee window) |
| **[[ethena-usde\|sUSDe]]** | 8-20% (cyclical) | Funding inversion + CEX custodian | Extended negative-funding bear | 7-day cooldown |
| **[[aave\|aUSDC]]** | 4-8% | Bad debt + USDC depeg | Rare; near cash-equivalent | Instant |
| **[[liquity\|Liquity SP]]** | 6-12% | [[ethereum\|ETH]] flash-crash exhausting SP | (Net often *gains* in ETH crashes) | Instant |

**The single most important reframe:** sort vaults not by APR but by *what you are short*. HLP, GLP, and JLP are all short "perp speculators winning" — so they are **correlated** and stacking all three is not real diversification. True diversification means pairing a perp-LP vault with sUSDe (short funding inversion), aUSDC (short bad debt), and Liquity SP (short an ETH flash-crash) — uncorrelated tails.

## Risk Profile Breakdown by Vault

Most retail allocators ask "what's the APR?" The professional question is **"what am I actually short?"** Each vault is implicitly short a specific tail.

### HLP (Hyperliquid)

**You are short:** retail [[perpetual-futures|perp]] traders on Hyperliquid winning, **plus** custom-L1 smart contract risk on [[hyperliquid|HyperBVM/HyperEVM]], **plus** thin-market manipulation à la JELLYJELLY.

- HLP is the [[hyperliquid|Hyperliquid]] protocol's own market-maker and liquidator. When users open positions, HLP often takes the other side; HLP earns spread + liquidation fees (~1% bonus) + funding harvest, and loses on adverse selection.
- The **JELLYJELLY incident (March 2025)** — coordinated manipulation of a thin meme-perp market — caused HLP to take a paper loss of ~$13M before community/governance halted the manipulation. This is the canonical "HLP tail risk" episode. See [[hyperliquid-hlp-basis-arbitrage]].
- Custom L1 risk is **non-trivial**: Hyperliquid is its own chain with a small validator set. A consensus bug or validator collusion would directly affect HLP.
- Withdrawals subject to **4-day lockup**, meaning you can't exit instantly during a stress event.

### GLP / GM (GMX)

**You are short:** [[gmx|GMX]] traders winning on directional perps, **plus** [[arbitrum|Arbitrum]] sequencer risk, **plus** Chainlink oracle manipulation.

- GLP (V1) is a multi-asset basket: ETH, BTC, USDC, plus volatile alts. LPs are passive counterparty to every GMX perp trade. **GM markets (V2)** isolate the LP exposure into per-pair pools (e.g., ETH/USD, BTC/USD), reducing the cross-contamination that GLP V1 suffered.
- The **late-2022 trending tape** drew ~25% drawdown on GLP V1 because GMX traders were correctly long, and LPs (i.e., GLP holders) had to pay them out. This is the structural risk: in a strongly trending market, perp LPs lose to directional traders.
- Oracle risk: a large GMX exploit in September 2022 used AVAX/USD oracle manipulation; ~$565k extracted before pause. V2 shifted to Chainlink Low-Latency Oracles to mitigate this.
- **No lockup** — you can exit immediately, which is meaningful when the basket is moving against you.

### JLP (Jupiter Perps)

**You are short:** Jupiter Perps users winning, **plus** [[solana|Solana]] outage and chain-halt risk, **plus** newness (less battle-testing than GMX).

- JLP is the LP token for [[jupiter-perps|Jupiter Perps]] on Solana — structurally similar to GLP V1 but Solana-native and faster-moving.
- TVL grew to $1B+ very quickly during the 2024-2025 [[solana|Solana]] memecoin cycle, partly because Solana traders pay high funding rates that JLP captures.
- Solana has had **multiple chain halts** historically (most recent: Feb 2024, ~5 hours). During a halt, JLP can't rebalance and is exposed to gap risk.
- Effective lockup is short (~1 hour exit fee window on most stable conditions), but **dynamic exit fees** can make withdrawing during stress expensive.
- Less battle-tested than [[gmx|GMX]]; the 2024 tail-risk episodes (memecoin liquidation cascades) drew ~8% drawdowns.

### sUSDe (Ethena)

**You are short:** **funding-rate inversion** (perp funding going negative for an extended period), **plus** multi-CEX custodian risk, **plus** USDe depeg risk.

- [[ethena-usde|USDe]] is delta-hedged: long [[ethereum|ETH]]/[[bitcoin|BTC]] spot or staked-ETH, short the same notional in [[perpetual-futures|perpetuals]] across centralized exchanges (Binance, Bybit, OKX, Deribit). The yield comes from staked-ETH yield + perp funding (which is positive most of the time in crypto bull markets).
- **Funding inversion risk:** in deep [[bear-markets|bear markets]], funding can go negative for weeks. Ethena's reserve fund absorbs this, but if the fund is exhausted, USDe yield can collapse or the peg can wobble.
- **Custodian risk:** Ethena's collateral sits with off-exchange custodians (Copper, Ceffu) with delegation to CEXs. A CEX failure (e.g., FTX-style) would trigger losses despite the off-exchange structure.
- **7-day cooldown** to convert sUSDe back to USDe — meaningful in a fast-moving event.
- Historical drawdowns in sUSDe price have been **<1%**, but the regime-dependence means future drawdowns could be larger if funding regimes shift.

### Aave aUSDC

**You are short:** Aave bad-debt accumulation, **plus** [[stablecoin|stablecoin]] depeg of underlying USDC.

- [[aave|Aave]] is the **most battle-tested DeFi lending protocol**, live since 2020 (V1) with V3 since 2022. Multi-billion-dollar TVL, multiple audits, on-chain insurance via the [[aave|Safety Module]].
- Yield comes from borrowers paying interest. APR is typically **4-8%** on USDC depending on utilization.
- The only material tail risk is **bad debt from collateral liquidations**: if a major collateral asset (CRV, SUSHI, even WBTC) depegs or has insufficient liquidity, liquidations can fail, generating bad debt. The CRV liquidation episode of late 2022 illustrated this; outcome was ~$1.6M of bad debt out of multi-billion TVL.
- **Instant withdrawal** (subject to utilization). This is the single biggest non-yield benefit: aUSDC functions as cash-equivalent.

### Liquity Stability Pool

**You are short:** [[ethereum|ETH]]-collateralized [[liquity|Liquity]] borrowers being liquidated *and* generating losses for the SP, **plus** smart-contract risk on Liquity (which is **immutable** since deployment).

- [[liquity|Liquity]] is a CDP protocol on Ethereum: borrow LUSD against ETH collateral at minimum 110% collateralization. The Stability Pool absorbs liquidations; SP depositors burn LUSD and receive ETH at a discount (typically 10% bonus).
- Yields: ~5-10% from LQTY rewards (declining over time per emission schedule) + variable LUSD APR from liquidation flow + ETH gains during volatile downturns.
- **Very narrow exposure**: ETH-only, on immutable contracts, no governance, no admin keys. This is the "purest" DeFi vault.
- Historical experience: during the **March 2023 ETH dip**, SP depositors realized small LUSD losses but **net gained ~6%** because the liquidated ETH appreciated post-purchase.
- The "tail" is an **ETH flash-crash that exhausts the SP** before liquidations clear — this triggers Liquity's Recovery Mode and Redistribution, which is technically possible but hasn't happened.

## Capacity / Capital Efficiency

| Vault | Practical Capacity | Notes |
|-------|--------------------|-------|
| **HLP** | ~$1B | APR compresses linearly with TVL. Hyperliquid devs have signaled a soft cap around this level. |
| **GLP/GM** | ~$1B combined | V2 GM markets isolate per-pair so capacity scales with each market's volume. |
| **JLP** | ~$1.5B | Capacity limited by Solana perp volume. JLP minting is rate-capped to prevent imbalance. |
| **sUSDe** | $10B+ | Capacity is roughly *open interest available across all CEX perp venues to short* — currently $10B+ globally but cyclical. |
| **Aave aUSDC** | Effectively unlimited | Borrower demand is the constraint, not LP supply. Multiple chain deployments (Ethereum, Arbitrum, Optimism, Base, etc.). |
| **Liquity SP** | ~$200M | Hard-capped by total LUSD supply, which is bounded by ETH borrower demand. Smaller and won't grow much. |

**Implication for size:** if you have $50k-$500k, all six vaults are fungible from a capacity standpoint. If you have $5M+, you need to think about market-impact when entering/exiting HLP, GLP, JLP, and Liquity SP — but Aave and sUSDe remain near-frictionless.

## APR Durability — 3-Year Forward Expected APR

The **realized APR** over the past year is not the **expected APR** going forward. Each vault has different decay and durability profiles.

| Vault | 3-Year Forward Expected APR | Trend |
|-------|------------------------------|-------|
| **HLP** | 12-20% | Declining as TVL grows and Hyperliquid matures. Early 60%+ APRs are gone. Crowding risk is **high**. |
| **GLP/GM** | 10-18% | Stable. GMX has a mature LP base; APR moves with perp volume. |
| **JLP** | 15-30% (high uncertainty) | Currently elevated; expect compression as more competitors enter Solana perp space. **Decay risk: high.** |
| **sUSDe** | 8-15% averaged across cycles | **Cyclical**: 15-25% in bull markets (positive funding), 4-8% in bear markets (sometimes negative). |
| **aUSDC** | 4-7% | Stable, low. Set by general DeFi borrower demand; no decay catalyst. |
| **Liquity SP** | 6-12% | Stable but LQTY emissions decline; long-run yield converges to ~liquidation flow only (~5%). |

**The honest read:** any protocol-specific vault paying >20% sustained for 3+ years would be an anomaly. Most current high-yield vaults will compress to **10-15%** as capital flows in. Plan accordingly.

## Worked Allocation: Sample $250k Portfolio

Optimizing for diversified Sharpe and uncorrelated risk drivers. Not advice; illustrative.

| Vault | % | $ Amount | Why |
|-------|---|----------|-----|
| **HLP** | 25% | $62,500 | Highest expected Sharpe currently; primary "anchor" position. See [[hyperliquid-hlp-basis-arbitrage]] and [[hlp-cascade-alongside-playbook]]. |
| **GLP/GM** | 20% | $50,000 | Mature alternative to HLP; uncorrelated chain (Arbitrum) and uncorrelated trader pool. |
| **JLP** | 25% | $62,500 | Highest absolute APR but capped at 25% to control Solana-chain concentration. |
| **sUSDe** | 15% | $37,500 | Cyclical funding harvest; uncorrelated to perp-LP performance (it's *long* perps that pay funding, vault LPs are *short* trader edge). |
| **Aave aUSDC** | 10% | $25,000 | Battle-tested baseline + instant liquidity for opportunistic redeployment. |
| **Liquity SP** | 5% | $12,500 | Pure-DeFi, immutable contract, ETH liquidation tail exposure — small position because of TVL cap. |

Expected blended APR (mid-case): **~15-18%**. Worst-quartile outcome (everything-correlated drawdown): **-15 to -20%** for ~6 weeks. Best-quartile: **25%+** with a stable-coin-flat or slightly-up principal.

The point of the split is not just yield — it's that **no single tail event takes down more than 25% of the portfolio**.

## The Decision Matrix — When to Favor Each

| Trader Profile | Top 2 Vaults | Why |
|----------------|--------------|-----|
| **Yield-maximizer** (willing to accept tail risk for headline APR) | JLP + HLP | Highest current APRs; both are perp-LP plays. |
| **Risk-minimizer** (prioritize principal preservation) | aUSDC + sUSDe | Aave for absolute safety; sUSDe for incremental yield with manageable tail. |
| **Stability-seeker** (consistent returns over absolute) | GLP/GM + Liquity SP | Both are mature, well-understood, and have stable-ish APRs. |
| **Opportunistic** (rotates toward elevated yields) | aUSDC + (rotate into HLP/JLP/sUSDe as APRs spike) | Aave is the staging ground; redeploy when one vault's APR clearly exceeds others. |
| **Maximalist on a specific ecosystem** | HLP (Hyperliquid bull), JLP (Solana bull), Liquity SP (ETH-pure bull) | If you have a thesis on chain X, lean the LP allocation toward that chain. |

## Combined Risks — What the Whole Vault Complex Is Exposed To

Diversifying across these six vaults reduces **idiosyncratic** risk but does **not** eliminate **systemic** risk. The whole complex shares some exposures:

1. **Crypto solvency contagion.** If a major CEX (Binance, OKX) fails, sUSDe's collateral is at direct risk; HLP/GLP/JLP would face a panic outflow as users move to perceived safety. Aave would see emergency borrowing demand spike. Even Liquity (which has zero CEX dependency) would face ETH price shock.
2. **Regulatory action.** SEC or CFTC action on perp DEXs (especially [[gmx|GMX]] and [[hyperliquid|Hyperliquid]] post-2024-2025 IPO/listing buzz) could force protocol changes that hurt LP economics. [[ethena|Ethena]] is particularly exposed because of its CEX-funding dependency. See [[crypto-regulation]].
3. **Leverage flush.** A simultaneous market-wide deleveraging (March 2020, May 2022 LUNA, FTX November 2022, March 2024 Bitcoin pullback) hits **every** perp-LP vault at once. HLP, GLP, JLP all draw down together. sUSDe's funding goes deeply negative. Only Aave and Liquity SP are insulated — and Liquity SP's ETH gains during a flush often offset its LUSD losses.
4. **Stablecoin (USDC/USDT/DAI) depeg.** USDC's March 2023 depeg episode briefly de-pegged Aave aUSDC, GLP (which holds USDC), and any vault denominated in USDC. Diversifying *across* stables — by holding sUSDe and LUSD — partially mitigates this.
5. **Validator/sequencer outages.** [[solana|Solana]] halts (JLP), Arbitrum sequencer downtime (GLP), Hyperliquid validator issues (HLP) — none of these are zero-probability. Diversifying chains is the only mitigation.

## The Hidden Third Option: Protocol-Internal Vaults

Notable absence from the list: **protocol insurance funds** (Hyperliquid's Insurance Fund, GMX's escrow, Aave's Safety Module from a backstop perspective, Ethena's Reserve Fund). These vaults often run **higher Sharpe** than any depositor-facing vault — but **depositors can't access them**. They are funded from protocol revenue and capitalized by the protocol itself or via token-stakers.

Implication: the LP-vault opportunity set is the **second-best yield in DeFi**. The best yields go to the protocols themselves (and via [[hype|HYPE]] / [[gmx|GMX]] / [[ena|ENA]] token holders who get protocol revenue). Token-staking those governance tokens is the *related but distinct* exposure that complements LP vaults, but it adds beta to the underlying protocol's token price.

For someone thinking about a **complete DeFi yield stack**, the layers are:

1. Stable lending (Aave) — base layer
2. Stable funding harvest (sUSDe) — semi-stable
3. Perp-LP vaults (HLP, GLP, JLP) — risk-bearing layer
4. Liquidation flow vaults (Liquity SP) — narrow risk-bearing
5. Governance-token staking (HYPE, GMX, ENA, LQTY) — protocol equity layer

This page covers layers 1-4. Layer 5 is its own analysis (see [[defi-real-yield-tokens]]).

## Verdict

For a trader running an [[hlp-cascade-alongside-playbook|alongside-HLP playbook]], **HLP is the right anchor position** — its APR/Sharpe is currently the best-in-class among accessible vaults, and the [[hyperliquid|Hyperliquid]] ecosystem's growth provides a continuing catalyst. But concentration risk is real: the JELLYJELLY incident, the custom-L1 dependency, and the 4-day lockup mean that **allocations >40% of crypto-side capital should diversify into the other vaults**.

The minimum-viable diversified stack: **HLP + GLP + sUSDe + aUSDC**, weighted toward HLP. Add JLP if you have a Solana thesis. Add Liquity SP if you want ETH-pure liquidation exposure. The blended portfolio targets 12-18% APR with a worst-quartile drawdown bounded around -15 to -20%, which is dramatically better risk-adjusted than holding any single vault at full size.

Whatever the allocation, **(1) verify current APR/TVL on each protocol's own dashboard before sizing, (2) monitor crowding metrics monthly — APRs compress fast, and (3) hold a meaningful aUSDC reserve for opportunistic redeployment**, because the highest returns over a multi-year window come from rotating *into* vaults whose APR has temporarily spiked, not from buy-and-hold a single vault.

## Related

- [[hyperliquid-hlp-basis-arbitrage]] — full HLP playbook
- [[hyperliquid-vault-architecture]] — how HLP works under the hood
- [[hlp-cascade-alongside-playbook]] — using HLP as anchor in stress regimes
- [[ethena]] · [[ethena-usde]] — synthetic dollar mechanics
- [[gmx]] · [[jupiter-perps]] · [[aave]] · [[liquity]]
- [[funding-rate-arbitrage]] — adjacent strategy
- [[crypto-spot-perp-futures-triangle]] — multi-leg basis strategies
- [[defi-real-yield-tokens]] — protocol equity layer (governance-token staking)
- [[stablecoin-yield-comparison]] — broader stablecoin yield landscape
- [[counterparty-risk]] · [[smart-contract-risk]] · [[oracle-risk]]

## Sources

- [[hyperliquid-hlp-basis-arbitrage]] — primary HLP source page
- [[ethena-usde]] — Ethena USDe entity page
- DefiLlama vault tracker (live APR/TVL data; verify before sizing)
- GMX V2 documentation on GM markets and risk isolation
- Jupiter Perps documentation on JLP composition and dynamic exit fees
- Liquity protocol documentation on Stability Pool mechanics and ETH liquidation discount
- Aave V3 risk parameters and Safety Module documentation
- JELLYJELLY incident community post-mortems (March 2025)
- USDC depeg post-mortem (March 2023, Circle / Aave / Maker)
