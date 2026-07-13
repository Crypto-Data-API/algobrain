---
title: "BFUSD"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, margin, derivatives]
aliases: ["BFUSD", "Binance BFUSD"]
entity_type: protocol
founded: 2024
headquarters: "Binance (centralized product)"
website: "https://www.binance.com/en/bfusd"
related: ["[[crypto-markets]]", "[[binance]]", "[[ethena]]", "[[ethena-usde]]", "[[funding-rates]]", "[[stablecoins]]", "[[stablecoin-yields]]", "[[other-stablecoins]]"]
---

# BFUSD

**BFUSD** is [[binance|Binance]]'s reward-bearing **margin asset** for futures trading — explicitly *not* a stablecoin, per Binance's own clarification — that pays daily USD-stablecoin rewards on qualifying balances while simultaneously serving as collateral in futures accounts. For traders it matters twice over: as a capital-efficiency tool (earn yield on idle margin) and as a market signal — its supply (~$1.3B by April 2026) and APR track the same **delta-neutral basis/funding-rate trade** that powers [[ethena|Ethena's USDe]], making BFUSD growth a proxy for perp funding conditions.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BFUSD |
| **Market Cap Rank** | ~#58 — as of June 2026 (approximate; ~$1.3B outstanding) |
| **Type** | Yield-bearing margin asset (Binance-internal; not freely transferable on-chain) |
| **Yield source** | Ethereum staking + delta-neutral hedging between spot and futures (funding-rate capture) |
| **Rewards** | Daily, paid in USD stablecoin to the UM Futures Wallet; APR varies; launch marketing cited 19.55% APY, with periodic "+5% APR boost" promos |
| **Backstop** | Binance reserve fund to offset negative funding-rate periods |
| **Website** | [https://www.binance.com/en/bfusd](https://www.binance.com/en/bfusd) |

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | BFUSD |
| **Current Price** | $0.9989 |
| **Market Cap** | $1.319B |
| **Market Cap Rank** | #58 |
| **Fully Diluted Valuation** | $1.319B |
| **24h Volume** | $0.85M |
| **24h Change** | -0.02% |
| **7d Change** | -0.01% |
| **Circulating Supply** | 1.32B BFUSD |
| **Total Supply** | 1.32B BFUSD |
| **Max Supply** | Uncapped (mint/redeem against deposits) |
| **All-Time High** | $1.007 (2025-10-10), -0.80% from ATH |
| **All-Time Low** | $0.997035 (2026-01-24), +0.19% from ATL |

As a USD-redeemable margin asset, BFUSD trades in an extremely tight band around $1.00: its **all-time range is roughly $0.997–$1.007**, i.e. under ~1% peak-to-trough across its whole history. At $0.9989 on 2026-06-21 it sits marginally below par and essentially flat over 24h and 7d — behaviour consistent with a tightly-managed dollar peg rather than a directional token. Daily volume is thin (~$0.85M) because BFUSD is a closed-loop Binance product, not a freely-traded market. Macro backdrop (qualitative): the broad crypto tape is in an **Established Bear Market** with the Crypto Fear & Greed Index around **23 ("Extreme Fear")** as of 2026-06-21 — a regime that *compresses or inverts* the funding rates BFUSD's yield depends on (see de-peg risk below).

---

## Overview

BFUSD is a reward-bearing asset redeemable for USD stablecoin. It offers rewards on qualifying balances and can be used as margin in Futures Accounts, allowing users to earn rewards simultaneously. Users holding BFUSD receive a daily reward in USD stablecoin at the prevailing APR for their qualifying balance; Binance tracks holdings hourly and credits rewards daily into the Unified Margin (UM) Futures Wallet.

### How the yield is generated

Binance generates BFUSD returns from two strategies:

1. **Ethereum staking** yield.
2. **Delta-neutral hedging** — long spot vs. short perpetual futures, harvesting positive [[funding-rates|funding rates]] (the classic cash-and-carry basis trade, the same engine behind Ethena's USDe).

A dedicated **reserve fund** offsets negative funding-rate fees during adverse regimes and is replenished in favorable conditions.

### Launch controversy (2024–2025)

When Binance first announced BFUSD with a headline **19.55% APY** (late 2024), the product drew immediate comparisons to **Terra/Anchor's 20% yield** that preceded the 2022 UST collapse. Binance publicly clarified that BFUSD is *"not a stablecoin but a high-yield margin product"*, that it had not yet launched at announcement time, and later published the staking + delta-hedging mechanics. The episode is a useful reminder that yield-bearing dollar assets embed real trade risk (funding inversion, exchange/custody risk) — not riskless interest.

## Trading Relevance

- **Where it trades**: Binance only (BFUSD/USDT conversion within the platform). It is a closed-loop Binance product — there is no meaningful DEX or external CEX market, so it cannot be shorted or arbitraged externally.
- **Use case**: parking futures margin — earn the APR while the same balance collateralizes perp positions, improving capital efficiency for Binance perp traders.
- **As a signal**: BFUSD supply growth and APR changes are a readable proxy for **aggregate funding-rate conditions** on Binance. A falling APR or supply contraction implies compressed/negative funding — relevant to anyone running basis or funding-harvest strategies (see [[ethena]], [[funding-rates]]).
- **Risks**: centralized issuer risk (Binance solvency/custody), funding-regime inversion exhausting the reserve fund, and peg history — it traded as low as $0.9970 (Jan 2026) and as high as $1.01 (Oct 2025): a narrow but non-zero band.

---

## Peg, Backing & Yield Mechanism

BFUSD's "peg" is a **redeemability peg**, not a reserve-attestation peg: each BFUSD is intended to be convertible to ~$1 of USD stablecoin within Binance, and Binance manages the backing portfolio behind it.

- **Backing**: a **delta-neutral portfolio** — spot crypto (incl. staked ETH) held long, hedged 1:1 with short perpetual futures — plus a Binance-funded **reserve fund**. The dollar value is meant to be invariant to crypto price because the long and short legs offset.
- **Where the yield comes from**: (1) **Ethereum staking** rewards on the spot leg, and (2) **positive [[funding-rates|funding rates]]** paid by perp longs to the short hedge (the classic cash-and-carry basis trade — the same engine behind [[ethena-usde|Ethena's USDe]]).
- **The peg-defending buffer**: the reserve fund absorbs **negative funding** periods (when the short hedge *pays* instead of earns) and is replenished in favourable regimes.

### De-peg risk

| Risk vector | Mechanism | Evidence / mitigant |
|---|---|---|
| **Funding inversion** | Sustained negative funding turns the carry negative; the short hedge bleeds, draining the reserve fund. If the buffer is exhausted, backing erodes | Reserve fund is the first line of defence; **bear-market / extreme-fear regimes (as of 2026-06-21) are exactly when funding compresses or goes negative** |
| **Exchange/custody risk** | BFUSD is a closed-loop Binance liability; redemption depends entirely on Binance solvency and operations | No external custody attestation comparable to a regulated fiat stablecoin |
| **Hedge execution / basis blowout** | In extreme volatility the spot and perp legs can diverge (basis risk), and hedges may not fill cleanly | Same structural risk as any delta-neutral synthetic-dollar product |
| **Historical peg band** | Observed range $0.997–$1.007 across its history — narrow but **non-zero**; it did trade below par | See Market Data above |

Net: BFUSD is **not riskless interest**. It is a basis-trade-backed margin asset whose stability holds as long as funding stays net-positive on average and Binance remains solvent — the launch-era Terra/Anchor comparison (below) was overstated mechanically (BFUSD is collateralised, UST was not), but the *yield-source-dependence* lesson is real.

---

## Tokenomics

| Metric | Value (2026-06-21) |
|---|---|
| **Circulating Supply** | 1.32B BFUSD |
| **Total Supply** | 1.32B BFUSD |
| **Max Supply** | Uncapped (mint/redeem against deposits) |
| **Market Cap** | $1.319B (rank #58) |

---

## Exchange Listings

| Exchange | Pair | Notes |
|---|---|---|
| Binance | BFUSD/USDT | Only venue; ~$0.85M daily volume (2026-06-21). Closed-loop conversion within Binance — not externally arbitrageable |

---

## Related

- [[crypto-markets]]
- [[binance]]
- [[ethena]] / [[ethena-usde]] — same delta-neutral basis engine
- [[funding-rates]] — the yield source BFUSD depends on
- [[stablecoins]]
- [[stablecoin-yields]] — where this kind of yield comes from
- [[other-stablecoins]] — catalog and peg-mechanism taxonomy

---

## Sources

- Binance — What Is BFUSD and How to Use It as Margin in Futures: https://www.binance.com/en/support/faq/detail/d62d25f330b94f5ba613c53e3c1ee8d0
- The Block — "Binance clarifies 'rewards-bearing' BFUSD asset is not a stablecoin": https://www.theblock.co/post/327134/binance-clarifies-rewards-bearing-bfusd-asset-is-not-a-stablecoin-hasnt-launched
- Brave New Coin — "BFUSD: Not a Stablecoin, But a High-Yield Margin Product": https://bravenewcoin.com/insights/binance-bfusd-not-a-stablecoin-but-a-high-yield-margin-product
- Binance — APR boost announcements: https://www.binance.com/en/support/announcement/detail/9a41039716264e45a65317479ab00d21
- Web verification, 2026-06-10: yield mechanics (ETH staking + delta hedging), reserve fund, Terra/Anchor comparison controversy confirmed.
- (Source: [[coingecko-top-1000-2026-04-09]])
