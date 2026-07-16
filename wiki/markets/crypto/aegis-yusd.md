---
title: "Aegis YUSD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, stablecoin]
aliases: ["YUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://app.aegis.im"
related: ["[[basis-trade]]", "[[bitcoin]]", "[[crypto-markets]]", "[[delta-neutral]]", "[[depeg]]", "[[ethena-usde]]", "[[ethereum]]", "[[funding-rate]]", "[[noon-usn]]", "[[stablecoin]]", "[[synthetic-dollar]]"]
---

# Aegis YUSD

**Aegis YUSD** (ticker **YUSD**; native chain [[ethereum|Ethereum]]) is a yield-bearing **[[synthetic-dollar]]** that aims to hold a 1:1 peg to the US dollar while paying yield to holders. Rather than relying on fiat bank reserves, Aegis backs YUSD with **[[bitcoin]]** held in off-exchange custody and runs a **[[delta-neutral]]** hedge using BTC-margined perpetual futures, so the portfolio's dollar value is stabilized regardless of BTC's spot price. The yield model is **funding-rate carry** (a [[basis-trade]]): the short perp leg collects funding in contango. It is the BTC-collateralized cousin of [[ethena-usde]] (which uses ETH/BTC) and a direct peer of [[noon-usn]].

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*
>
> *Disclaimer: figures below are a point-in-time snapshot and not investment advice. Verify live data and the protocol's own attestations before trading.*

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | YUSD |
| **Price (USD)** | $0.998308 (≈ peg, slightly below $1) |
| **Market Cap Rank** | #565 |
| **Market Cap** | $36,029,690 |
| **24h Change** | -0.02% |
| **7d Change** | -0.05% |
| **Currency tracked** | US dollar (USD) |

YUSD targets the US dollar, so ~$0.9983 is close to peg but slightly under — normal for a synthetic dollar whose backing and hedge can drift a few basis points from par. The small 24h/7d moves are consistent with a peg that holds within a tight band rather than a full [[depeg]].

## Architecture — How Aegis Works

Aegis is a **DeFi protocol** (no fiat issuer). The peg is maintained synthetically through a classic delta-neutral cash-and-carry structure:

1. **Collateral:** YUSD is backed by **Bitcoin** held in custodial / off-exchange-settlement vaults, with smart contracts coordinating the position. Using BTC (rather than ETH or stablecoins) as the spot leg is Aegis's main differentiator from ETH-centric synthetic dollars.
2. **Delta-neutral hedge:** Against the long BTC collateral, the protocol opens an equivalent **short** position in BTC-margined perpetual futures. The short offsets the spot exposure, so a fall in BTC is matched by a gain on the short (and vice versa). The net "delta" is ~zero, pinning the portfolio value near a stable USD figure. See [[delta-neutral]].
3. **Custody model:** Holding collateral off-exchange and trading via settlement rails (rather than parking BTC directly on a derivatives venue) is intended to limit exchange-insolvency loss — though hedge execution still depends on those venues.

### Mint / redeem & gating

YUSD is minted when collateral is deposited and the hedge is opened, and redeemed when the position is unwound — par is enforced by this mint/redeem arbitrage plus secondary trading, not by a fiat redemption desk. As with all carry stablecoins, **redemption can be gated or slowed in stress** (when unwinding the hedge is costly or venues are illiquid), so a $1 exit is not guaranteed on demand.

### Yield source & distribution

YUSD's yield does **not** come from a bank paying interest on cash. It is primarily **[[funding-rate]]** income: when perpetual-futures markets are in contango (longs paying shorts), the protocol's short positions **collect** funding payments — the main yield engine of the [[basis-trade]]. Additional yield may come from staking/collateral returns on the underlying BTC arrangement. Yield is typically distributed via a **staked variant** (the yield-accruing leg) so that base YUSD can stay closer to a pure $1 unit while stakers earn the carry.

This is the same family of yield as [[ethena-usde]] and other "carry" synthetic dollars. Holders should understand it is a **trade**, not a deposit.

## Tokenomics & Supply

- **YUSD** is mint-on-collateral / burn-on-redeem; supply scales with how much BTC collateral and hedge capacity the protocol runs. At the snapshot it backs a ~$36M market cap (rank #565) — small, so capacity and liquidity are limited.
- The economic split is **base YUSD (stable unit)** vs a **staked/yield variant (risk-return unit)** — holders self-select into yield by staking, mirroring the USDe/sUSDe and [[noon-usn|USN]] designs.

## Comparison vs Peer Stablecoins

| Feature | **Aegis (YUSD)** | [[ethena-usde\|Ethena USDe]] | [[noon-usn\|Noon USN]] | [[usdc\|Circle USDC]] |
|---|---|---|---|---|
| Peg target | US dollar | US dollar | US dollar | US dollar |
| Spot collateral | **Bitcoin** (off-exchange custody) | ETH/BTC + stables | Mixed collateral | Cash & T-bills |
| Mechanism | Delta-neutral BTC perp hedge | Delta-neutral hedge | Basis/funding strategy (may rotate) | Fiat reserve |
| Yield source | Funding-rate carry | Funding-rate carry | Funding/basis carry | None |
| Yield to | Staked YUSD | sUSDe | Staked USN | n/a |
| Size (snapshot) | ~$36M | Multi-billion | ~$33M | Tens of billions |
| Key risk | Negative funding, venue/custody | Negative funding, venue | Negative carry, venue | Issuer/bank |

## How & Where It Trades / Is Used

With ~$36M market cap and very low on-chain volume, YUSD is a **thinly-traded** synthetic dollar — secondary liquidity is shallow, so par exit relies mainly on protocol mint/redeem rather than deep order books. Its DeFi role is as a yield-bearing dollar building block: hold base YUSD as a dollar unit, or stake it for the carry. Composability (lending markets, LP pairs) is limited at this size relative to majors like USDe.

## Narrative / Category & Catalysts

YUSD sits in the **delta-neutral synthetic-dollar / "internet bond"** narrative pioneered by Ethena, with a **Bitcoin-collateral** twist that appeals to BTC-native holders who want dollar yield without selling their BTC thesis. Catalysts: sustained positive BTC perp funding (the lifeblood of the yield), growth of off-exchange settlement infrastructure that de-risks custody, BTC-collateral demand in a bottoming market, and DeFi integrations that deepen liquidity. The dominant headwind is **funding regime**: in the current **bottoming/accumulation / Extreme Fear** environment (Fear & Greed 21, as of 2026-06-22), perp funding can compress or flip negative, directly squeezing YUSD's yield engine.

## History / Timeline

- **2026-06-21** — Snapshot: YUSD ~$0.9983 (≈ peg, a few bps under $1), market cap ~$36.03M, rank #565; 24h −0.02%, 7d −0.05%. Peg holding within a tight band; **no depeg evident** in the recorded data.
- (No dated depeg or major incident appears in the data available to this wiki; the slight sub-$1 print is normal carry-stablecoin behaviour, not a peg break.)

## Risks — Yield-Bearing Synthetic Dollars Are NOT Risk-Free

- **Negative funding risk:** If perpetual funding flips negative for an extended period, the short side **pays** instead of receiving, eroding yield and potentially the backing.
- **Hedge / execution risk:** The delta-neutral hedge depends on liquid perp markets; gaps, liquidations, or auto-deleveraging on the venue can break the hedge during stress.
- **Exchange / custody / counterparty risk:** Collateral sits with custodians and hedges sit on derivatives venues — a custodian failure or exchange insolvency can cause loss and a [[depeg]].
- **Peg / liquidity risk:** With ~$36M market cap and very low on-chain volume, YUSD can trade off peg; redemptions in a crunch may not clear at $1.
- **Smart-contract & governance risk:** Bugs or admin-key compromise could threaten funds.
- **Not a bank deposit:** YUSD carries no deposit insurance; the "yield" is compensation for real market risk borne by the holder.

## Trading / Usage Playbook

- **Track BTC perp funding before chasing the yield.** Positive/contango funding feeds returns; flat or negative funding starves them. The yield is a live read on the basis, not a fixed rate.
- **Hold base YUSD for a dollar unit; stake only if you accept carry risk.** The staked variant is where the real market exposure lives.
- **Assume redemption can slow in stress** — at ~$36M with thin secondary liquidity, plan exits before a volatility event, not during one.
- **Watch venue and custody concentration** as the key tail risk; an exchange failure or custody breach is the classic way carry stablecoins [[depeg]].
- **Size as a risk asset, not cash equivalent.**

## See Also

- [[stablecoin]]
- [[synthetic-dollar]]
- [[delta-neutral]]
- [[funding-rate]]
- [[basis-trade]]
- [[ethena-usde]]
- [[noon-usn]] — direct basis-carry peer
- [[bitcoin]]
- [[crypto-markets]]
- [[ethereum]]
- [[depeg]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | YUSD |
| **Market Cap Rank** | #1117 |
| **Market Cap** | $10.86M |
| **Current Price** | $0.9985 |
| **Categories** | Decentralized Finance (DeFi), Yield-Bearing Stablecoin |
| **Website** | [https://yield.fi/](https://yield.fi/) |

---

## Overview

YieldFi is revolutionising decentralised finance with its comprehensive, cross-chain asset management platform. Delivering ~25% real yield on stablecoins like USDT and USDC, it offers a high-performance alternative to traditional investment options. With a proven track record of less than 1% drawdown over five years, YieldFi combines stability with high returns.

Key Features:
Exceptional Yields on Stablecoins - Earn High APY on USDT, USDC, and DAI  (Current APY ≈ 25%)

Your Personal Asset Manager: Diversify your capital with our systematic delta-neutral strategies across the centralized and decentralized finance platforms (CEXs and DEXs) universe to guarantee uncorrelated and consistent APY.

No Lock-In: Withdraw your assets anytime (or swap via DEXes) 
Minimal Risk Exposure: Rigorous backtesting of strategies by a team of quants and experts over the last 3 years, with a maximum drawdown &lt;1%, ensuring stable and reliable returns.

Incentivized Ecosystem: Earn daily rewards while participating in DeFi opportunities such as AMM, Lending &amp; Borrowing, CDPs, Perps, L2 Farming, Re-staking, and more

Cross-Chain Support: Works seamlessly across both EVM and non-EVM ecosystems.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.88M YUSD |
| **Total Supply** | 10.88M YUSD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $10.86M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.19 (2025-09-29) |
| **Current vs ATH** | -16.04% |
| **All-Time Low** | $0.9826 (2025-11-19) |
| **Current vs ATL** | +1.61% |
| **24h Change** | +0.00% |
| **7d Change** | +0.00% |
| **30d Change** | +0.00% |
| **1y Change** | -9.23% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x19ebd191f7a24ece672ba13a302212b5ef7f35cb` |
| Sonic | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |
| Base | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |
| Plume Network | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |
| Arbitrum One | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |
| Optimistic Ethereum | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |
| Katana | `0x4772d2e014f9fc3a820c444e3313968e9a5c8121` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://yield.fi/](https://yield.fi/) |
| **Whitepaper** | [https://docs.yield.fi/](https://docs.yield.fi/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $80.09 |
| **Market Cap Rank** | #1117 |
| **24h Range** | $0.9985 — $0.9985 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
