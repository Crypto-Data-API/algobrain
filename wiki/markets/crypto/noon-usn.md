---
title: "Noon USN"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["USN"]
entity_type: protocol
headquarters: "Decentralized (Noon Capital)"
website: "https://www.noon.capital/"
related: ["[[aegis-yusd]]", "[[basis-trade]]", "[[crypto-markets]]", "[[delta-neutral]]", "[[depeg]]", "[[ethena-usde]]", "[[ethereum]]", "[[funding-rate]]", "[[stablecoin]]", "[[synthetic-dollar]]"]
---

# Noon USN

**Noon USN** (ticker **USN**; native chain [[ethereum|Ethereum]], with reach onto zkSync and Starknet) is a yield-bearing **[[synthetic-dollar|synthetic-dollar-style stablecoin]]** built by Noon Capital, designed to hold a 1:1 peg to the US dollar while paying competitive yield to holders. Like other carry-based stablecoins, its returns are generated from a **basis / funding-rate strategy** ([[basis-trade]]) rather than from a bank paying interest on fiat deposits, with yield typically accrued through a staked variant (sUSN-style) so base USN can stay near a clean $1. It is a direct peer of [[aegis-yusd]] and a relative of [[ethena-usde]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*
>
> *Disclaimer: figures below are a point-in-time snapshot and not investment advice. Verify live data and the protocol's own attestations before trading.*

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | USN |
| **Price (USD)** | $0.998631 (≈ peg, slightly below $1) |
| **Market Cap Rank** | #609 |
| **Market Cap** | $32,739,115 |
| **24h Change** | +0.02% |
| **7d Change** | -0.04% |
| **Currency tracked** | US dollar (USD) |

USN targets the US dollar, so ~$0.9986 is close to peg, sitting a few basis points under $1 — typical for a yield-bearing synthetic dollar. The negligible 24h/7d moves indicate the peg is holding within a tight band, not a [[depeg]].

## Architecture — How Noon Works

### Issuer & structure

USN is issued by **Noon Capital** and structured as a yield-bearing dollar token, typically paired with a **staked variant** that accrues the yield (similar in spirit to USDe/sUSDe and [[aegis-yusd]]'s staked YUSD). Base USN is the dollar unit; staking is what opts a holder into the carry and its risk. The protocol is deployed on [[ethereum]], with additional reach onto **zkSync and Starknet**.

### Collateral, hedge & delta-neutrality

Noon describes USN's returns as coming from a **"basis yield" strategy** — a [[basis-trade]] that combines long spot/collateral positions with offsetting short perpetual or futures positions to stay roughly **[[delta-neutral]]**, harvesting the **[[funding-rate]]** / basis spread between spot and derivatives. The long-spot leg supplies the collateral value; the short-derivatives leg cancels its price exposure, so the portfolio's USD value is stabilised while the spread is collected. Crucially, **the protocol may rotate among several such strategies** to keep returns consistent across market conditions — a more actively-managed, multi-strategy stance than a single fixed ETH/BTC carry.

### Mint / redeem & gating

USN is minted against deposited collateral when the hedge is established and redeemed when positions unwind; par is held by this mint/redeem arbitrage plus secondary trading rather than a fiat desk. As with every carry stablecoin, **redemption can be gated or slowed in stress**, when unwinding hedges is costly or venues are illiquid — so a $1 exit on demand is not guaranteed.

### Yield source & distribution

The yield is **market carry** — the basis/funding spread — **not** a guaranteed interest rate. When funding/basis is positive, holders (via the staked variant) earn; when it compresses or turns negative, yield falls and can be eroded. The multi-strategy rotation is intended to smooth this, but it does not remove the fundamental dependence on a positive carry regime.

## Tokenomics & Supply

- **USN** is mint-on-collateral / burn-on-redeem; supply scales with collateral and hedge capacity. At the snapshot it backs a ~$32.7M market cap (rank #609) — the smallest of this cohort, so capacity and liquidity are tight.
- Economic split: **base USN (stable unit)** vs **staked USN (yield-bearing claim)** — holders self-select into yield by staking, mirroring USDe/sUSDe and YUSD.

## Comparison vs Peer Stablecoins

| Feature | **Noon (USN)** | [[aegis-yusd\|Aegis YUSD]] | [[ethena-usde\|Ethena USDe]] | [[usdc\|Circle USDC]] |
|---|---|---|---|---|
| Peg target | US dollar | US dollar | US dollar | US dollar |
| Mechanism | **Multi-strategy** basis/funding carry | Delta-neutral BTC perp hedge | Delta-neutral ETH/BTC hedge | Fiat reserve |
| Spot collateral | Mixed / rotating | Bitcoin | ETH/BTC + stables | Cash & T-bills |
| Yield source | Funding/basis spread | Funding-rate carry | Funding-rate carry | None |
| Yield to | Staked USN | Staked YUSD | sUSDe | n/a |
| Chains | Ethereum, zkSync, Starknet | Ethereum | Ethereum + | Many |
| Size (snapshot) | ~$33M | ~$36M | Multi-billion | Tens of billions |
| Key risk | Negative carry, multi-venue | Negative funding, custody | Negative funding, venue | Issuer/bank |

## How & Where It Trades / Is Used

With ~$33M market cap and **very thin** on-chain volume, USN is a small, shallow-liquidity synthetic dollar — par exit depends mainly on protocol mint/redeem rather than deep order books, and modest flow can dislocate the price. Its multi-chain footprint (Ethereum, zkSync, Starknet) is aimed at composability across L2 DeFi, but at this size lending/LP depth is limited versus majors like USDe. Hold base USN as a dollar unit, or stake for the carry.

## Narrative / Category & Catalysts

USN sits in the **delta-neutral synthetic-dollar / "internet bond"** category, with a **multi-strategy carry** angle that pitches steadier yield by rotating across basis trades rather than relying on a single market. Catalysts: sustained positive funding/basis across the venues Noon trades, expansion of its L2 footprint and DeFi integrations, and demand for diversified-carry dollars. The dominant headwind is the **funding regime**: in the current **bottoming/accumulation / Extreme Fear** market (Fear & Greed 21, as of 2026-06-22), perp funding can compress or flip negative, directly squeezing the basis yield that USN depends on — the multi-strategy design mitigates but does not eliminate this.

## History / Timeline

- **2026-06-21** — Snapshot: USN ~$0.9986 (≈ peg, a few bps under $1), market cap ~$32.74M, rank #609; 24h +0.02%, 7d −0.04%. Peg holding within a tight band; **no depeg evident** in the recorded data.
- (No dated depeg or major incident appears in the data available to this wiki; the slight sub-$1 print is normal carry-stablecoin behaviour, not a peg break.)

## Risks — Yield-Bearing Synthetic Dollars Are NOT Risk-Free

- **Strategy / negative-carry risk:** If funding or the futures basis turns negative or compresses, the yield engine can stall or lose money.
- **Hedge & venue risk:** The delta-neutral structure depends on liquid derivatives markets; liquidations, ADL, or venue outages during stress can break the hedge.
- **Counterparty / custody risk:** Collateral and hedges held with exchanges or custodians carry insolvency and operational risk, which can trigger a [[depeg]].
- **Peg / liquidity risk:** With ~$33M market cap and **very thin** on-chain trading volume, USN can dislocate from $1 on modest flow; redemption in a crisis may not clear at par.
- **Smart-contract & admin risk:** Contract bugs or privileged-key compromise could threaten funds across its multi-chain deployment.
- **Not a deposit:** USN has no deposit insurance; its yield is compensation for taking on real, non-trivial market and counterparty risk.

## Trading / Usage Playbook

- **Watch the funding/basis regime first.** USN's yield is live carry — positive funding feeds it, negative funding starves it. The advertised rate is a snapshot, not a promise.
- **Hold base USN for a dollar unit; stake only if you accept multi-strategy carry risk.**
- **Account for multi-venue, multi-chain exposure.** Rotating across strategies and across Ethereum/zkSync/Starknet spreads risk but also multiplies the venues and bridges that can fail.
- **Assume redemption can slow in stress** — at ~$33M with thin secondary liquidity, exit before volatility events, not during them; a crisis redemption may not clear at $1 ([[depeg]] risk).
- **Size as a risk asset, not cash equivalent.**

## See Also

- [[stablecoin]]
- [[synthetic-dollar]]
- [[delta-neutral]]
- [[funding-rate]]
- [[basis-trade]]
- [[aegis-yusd]]
- [[ethena-usde]]
- [[crypto-markets]]
- [[ethereum]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

