---
title: "BSquared Network"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, layer-2]
aliases: ["B2", "B2 Network", "B² Network"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.bsquared.network/"
related: ["[[bitcoin]]", "[[bnb]]", "[[crypto-markets]]", "[[layer-2]]"]
---

# BSquared Network

**BSquared Network** (B², ticker **B2**) is a Bitcoin-centric [[layer-2]] network aiming to extend [[bitcoin]] with smart-contract execution, a rollup-style settlement layer, and a data-availability (DA) layer — the broad design space marketed as "BTCFi" (Bitcoin DeFi). The native **B2** token is used for gas, ecosystem incentives, and governance across the network. It is backed by investors including Animoca Brands and OKX Ventures, and ranks **#782** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

At the latest snapshot B2 traded near **$0.52793** (market cap **$21,861,165**, rank **#782**), down **2.65% over 24h** but up a notable **22.98% over 7d** — a strong weekly rally that stands out against an "Extreme Fear" market backdrop (Fear & Greed Index at 22, [[bitcoin]] around $64,180). Like most low-cap alts, B2 remains far below its all-time high and is sensitive to broad-market risk sentiment.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | B2 |
| **Market Cap Rank** | #782 |
| **Market Cap** | $21,861,165 |
| **Current Price** | $0.52793 |
| **24h Change** | -2.65% |
| **7d Change** | +22.98% |
| **Categories** | Smart Contract Platform, Bitcoin Layer 2, Zero Knowledge (ZK), Animoca Brands Portfolio, Data Availability, Rollup, OKX Ventures Portfolio, Binance Wallet IDO |
| **Website** | [https://www.bsquared.network/](https://www.bsquared.network/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Architecture & Mechanism

B² Network positions itself as a [[bitcoin]] [[layer-2]] that adds a programmable, EVM-compatible execution environment on top of Bitcoin's base layer. The stated design combines three components:

- **Execution / rollup layer** — an EVM-compatible environment where smart contracts run and transactions are batched, allowing developers to deploy DeFi, NFT, and gaming applications that ultimately reference Bitcoin for settlement.
- **Data availability (DA) layer** — off-chain data storage with commitments anchored back to Bitcoin, intended to let anyone reconstruct and verify L2 state.
- **Zero-knowledge (ZK) and fraud-proof tooling** — used to attest to the validity of batched transactions before they are committed.

The token **B2** functions as gas/utility for the network, an incentive asset for ecosystem participants (liquidity, staking programs, points campaigns), and a governance asset.

### How the rollup/settlement/DA model actually works

Putting the three components together, the intended flow is:

1. **Execution** happens on B²'s EVM-compatible rollup, where users transact cheaply and quickly.
2. **Transactions are batched** and a commitment (and, per the design, ZK validity proofs) is produced for the batch.
3. **Data availability** is handled off-chain with commitments anchored back to [[bitcoin]] — the project's pitch is that publishing commitments to Bitcoin lets anyone challenge or reconstruct L2 state.
4. **Settlement / verification** references Bitcoin: B² has publicly described a scheme to inscribe rollup commitments to Bitcoin and use a challenge/fraud-proof window so that, in theory, an honest party can dispute an invalid state transition.

This is more ambitious than a plain sidechain, but it sits on top of a hard constraint described below.

### BTC layer-2 trust-model caveat (read this before trusting "Bitcoin security")

The label "Bitcoin layer-2" should be read critically. [[bitcoin]]'s base protocol does not natively support the kind of validity-proof verification or fraud-proof enforcement that Ethereum-style rollups rely on — Bitcoin Script cannot execute a ZK verifier or arbitrate a rollup dispute on-chain. So most projects marketed as "BTC L2s" are in practice **sidechains, federated bridges, or rollups whose security ultimately depends on a multisig/committee rather than on Bitcoin consensus**. Even when commitments are *inscribed* to Bitcoin (so the data is timestamped and censorship-resistant), Bitcoin itself cannot *enforce* the rollup's rules; enforcement still relies on an off-Bitcoin operator/committee and the bridge that custodies BTC.

In these designs, **custody of bridged BTC and the honesty of the operator set — not Bitcoin's proof-of-work — are the real trust assumptions.** Users should verify, for any given BTCFi network, exactly how bridged BTC is custodied (multisig? MPC? threshold signatures? who holds keys?), how withdrawals are enforced if operators misbehave, and whether state can be reconstructed from Bitcoin alone. Treat marketing claims of "inheriting Bitcoin security" as unverified unless the specific bridge and proof mechanism are documented and audited. For B² specifically, the security of the BTC bridge and the liveness of its operator/prover set are the dominant failure modes — far more than anything in the EVM execution layer.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 41.55M B2 |
| **Total Supply** | 210.00M B2 |
| **Max Supply** | 210.00M B2 |
| **Fully Diluted Valuation** | $134.36M |
| **Market Cap / FDV Ratio** | 0.20 |

### Value accrual & governance

B2 is intended to capture value through three channels: **gas** (transactions on the rollup are paid in B2 or settle to B2-denominated fees), **incentives** (staking, liquidity-mining, and points campaigns that bootstrap TVL), and **governance** (steering ecosystem grants and protocol parameters). With MC/FDV ≈ 0.20, ~80% of the 210M max supply is not yet circulating, so a large share of any "staking yield" is emission-funded dilution rather than fee revenue. As with all BTCFi rollups, the durable question is whether real BTC inflows and application fees grow faster than the unlock schedule — incentive-driven TVL tends to leave when emissions taper.

---

## Comparison vs competitor chains

B²'s peer set is the crowded **Bitcoin L2 / BTCFi** category. The honest framing: all of these face the same base-layer constraint (Bitcoin can't natively verify rollups), so they differ mainly in their bridge/trust model and ecosystem traction.

| Network | Model | Trust assumption | Differentiator vs B² |
|---|---|---|---|
| **B² Network (B2)** | ZK-flavored rollup + DA, EVM execution | Bridge custody + operator/prover set; commitments inscribed to BTC | ZK + fraud-proof tooling pitch; Animoca/OKX Ventures backing |
| **[[bitlayer]]** (BTR) | BitVM-based rollup | BitVM bridge / committee | BitVM paradigm for trust-minimized verification |
| **Merlin Chain** | ZK-rollup sidechain | Federated bridge / committee | Large early TVL via incentives; Bitcoin inscriptions focus |
| **[[stacks]]** (STX) | Bitcoin L2 (sBTC, PoX) | Stacks consensus + sBTC signer set | Own L1 token + smart contracts; longest-running BTC smart-contract layer |
| **[[base]]** (Ethereum L2) | Optimistic rollup | Inherits [[ethereum]] security | *Not* a BTC L2 — shown as the contrast: a "real" rollup whose L1 can enforce disputes |

The contrast with [[base]] is the point: an Ethereum rollup can have its disputes adjudicated by the L1 itself, whereas every BTC L2 (B² included) must lean on an off-Bitcoin operator/bridge. B²'s competitive task is to differentiate within BTCFi on security model and ecosystem, not to claim Ethereum-grade trust-minimization.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.11 (2025-10-26) |
| **Current vs ATH** | approx. -75% |
| **All-Time Low** | $0.3177 (2025-06-14) |
| **Current Price** | $0.52793 |
| **24h Change** | -2.65% |
| **7d Change** | +22.98% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x783c3f003f172c6ac5ac700218a357d2d66ee2a2` |

---

## How & where it trades

- **Spot venues (CEX):** Kraken (B2/EUR), Bitget (B2/USDT), and KuCoin (B2/USDT) are the listed centralized pairs. B² ran a **Binance Wallet IDO**, routing some early distribution and attention through Binance's wallet surface.
- **Derivatives / perps:** No major perpetual-futures market is tracked for B2 in the current snapshot; treat it as effectively spot-only and verify live perp availability before any leveraged or hedged position.
- **Liquidity & float:** at roughly **$22M market cap** with only ~20% of supply circulating, B2 is a low-float small-cap. Spreads are wide, depth is thin, and the +22.98% 7d rally into an Extreme-Fear tape illustrates how easily a low-float token can be marked up — and how violently it can reverse. Scheduled unlocks against the 210M max supply are the structural counterweight to any rally.

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | B2/EUR | N/A |
| Bitget | B2/USDT | N/A |
| KuCoin | B2/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.bsquared.network/](https://www.bsquared.network/) |
| **Twitter** | [@BsquaredNetwork](https://twitter.com/BsquaredNetwork) |
| **Discord** | [https://discord.com/invite/bsquarednetwork](https://discord.com/invite/bsquarednetwork) |
| **GitHub** | [https://github.com/b2network/](https://github.com/b2network/) |
| **Whitepaper** | [https://docs.bsquared.network/](https://docs.bsquared.network/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.52793 |
| **Market Cap** | $21,861,165 |
| **Market Cap Rank** | #782 |
| **24h Change** | -2.65% |
| **7d Change** | +22.98% (strong weekly rally) |
| **Last Updated** | 2026-06-21 |

---

## Risks

- **Trust-model / bridge risk** — as above, the security of any "BTC L2" depends heavily on how bridged BTC is custodied and how withdrawals are enforced. A compromised bridge or operator set is the dominant failure mode for this category.
- **Low liquidity / low market cap** — at roughly $22M market cap and rank #782, B2 is a small-cap asset prone to sharp drawdowns, wide spreads, and slippage on larger orders.
- **Token unlock / dilution** — circulating supply is a fraction of max supply (210M), so future emissions and unlocks can pressure price.
- **Ecosystem execution risk** — the BTCFi narrative is crowded and competitive; sustained value depends on real application usage and TVL, which can be transient and incentive-driven.
- **Sentiment beta** — the +22.98% 7d move shows the token can rally hard, but the same volatility cuts both ways during an "Extreme Fear" market.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Narrative, category & catalysts

B² is a **BTCFi / Bitcoin-L2** narrative play with **Animoca Brands** and **OKX Ventures** in the cap table — VC backing that gives it visibility above many anonymous BTC-L2 forks. The category thesis is that the trillions of dollars of dormant [[bitcoin]] capital represent the largest untapped DeFi collateral base, and whichever L2 wins safe, usable BTC yield captures enormous value. The bear case is that BTCFi has repeatedly attracted mercenary, incentive-driven TVL that evaporates, and that the bridge trust models keep the "safe" promise unproven.

Plausible **catalysts** (positive): a credibly trust-minimized bridge upgrade (e.g. BitVM-style verification), sustained non-incentivized TVL, major CEX spot listings, renewed BTCFi narrative rotation. **Negative catalysts:** a bridge/operator exploit (category-defining tail risk), token unlocks into thin liquidity, BTCFi narrative fatigue.

## History / timeline

- **2025-06-14** — All-time low near **$0.3177**.
- **2025-10-26** — All-time high near **$2.11**.
- **2026-06-21** — Trading at **$0.52793** (rank #782), ~75% below ATH, after a **+22.98% 7d** rally against an Extreme-Fear backdrop.

*(Dates/prices from the market-data snapshot; no mainnet/launch date is asserted here as it is not independently verified in this wiki.)*

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context as of 2026-06-23: market-wide **Extreme Fear** (F&G 21), transitional **bottoming/accumulation** long-horizon regime, BTC ~16% below its 200-day MA.

- **Read the rally with skepticism.** B2's +22.98% week is a low-float pop, not a fundamental re-rating. In Extreme Fear, such moves often round-trip; chasing strength here has poor risk/reward.
- **If positioning:** size small, prefer limit entries on weakness rather than buying the spike, and treat unlock dates as scheduled risk events. The dominant tail risk (bridge/operator failure) is binary and macro-independent — do not over-size on a name where a single exploit can impair the token.
- **Invalidation:** a broad regime flip out of Extreme Fear plus a project catalyst (bridge security upgrade, major listing, durable TVL). Absent both, default to patience.
- **Always** verify the **B2 ticker and BSC contract** before trading.

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[bitcoin]]
- [[layer-2]]
- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | B2/USD | N/A |
| Bitget | B2/USDT | N/A |
| KuCoin | B2/USDT | N/A |

---
