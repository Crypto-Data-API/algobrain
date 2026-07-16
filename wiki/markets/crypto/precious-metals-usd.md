---
title: "Precious Metals USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, real-world-assets, stablecoins]
aliases: ["PMUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://raac.io/"
related: ["[[commodities]]", "[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[gold]]", "[[real-world-assets]]", "[[stablecoin]]", "[[stablecoins]]"]
---

# Precious Metals USD

**Precious Metals USD** (ticker **PMUSD**) is a dollar-denominated [[real-world-assets|RWA]] token issued by **Real Asset Acquisition Corp (RAAC)** on [[ethereum|Ethereum]], nominally targeting US$1 and backed by tokenized precious-metals / real-world-asset collateral. The real-world asset it nominally represents is a book of precious-metals and real-asset exposure that RAAC deploys into DeFi to unlock liquidity and on-chain yield. **Important: as of this snapshot PMUSD is significantly de-pegged**, trading well below $1 — see the market-data block and Risks below. This page documents it as a *broken* stablecoin, not a stable $1 unit.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | PMUSD |
| **Market Cap Rank** | #344 |
| **Current Price** | $0.7681 |
| **Market Cap** | $72.2M |
| **24h Volume** | $31.5K |
| **24h Change** | -1.72% |
| **Circulating / Total Supply** | 94.0M / 94.0M PMUSD |
| **All-Time High** | $1.037 |
| **All-Time Low** | $0.1162 |
| **Categories** | Stablecoins, RWA, Ethereum Ecosystem |
| **Website** | [https://raac.io/](https://raac.io/) |

**De-peg, documented honestly:** PMUSD traded at **$0.7681** at the snapshot — roughly **23% below its $1 target**, and down a further -1.72% on the day. Far more striking, its **all-time low is $0.1162**, meaning PMUSD has at some point lost nearly 90% of its peg value (against an ATH of $1.037). This is a **severely and chronically de-pegged** token, not a stable $1 unit; the partial recovery to ~$0.77 still leaves it deeply broken. Treat any "stablecoin" labeling with extreme caution. (Note: market cap here is reported against circulating supply at a price below par, so the figures should be read as approximate.)

---

## Architecture — How It Works (and Why It Broke)

### Reserve / collateral model
PMUSD is marketed as backed by **tokenized real-world assets, including precious metals**, deployed by RAAC into DeFi. Unlike a cash-and-Treasuries stablecoin (which can typically defend a peg cheaply), a metals/real-asset backed token depends on the **custody, valuation, and on-demand liquidity** of physical or tokenized commodity collateral — far harder to redeem instantly at par. **The market price ($0.77, ATL $0.12) implies the market does not currently value PMUSD at its nominal backing**, the signature of impaired or illiquid collateral, redemption friction, or lost confidence in the issuer's reserves.

### NAV / peg mechanism (impaired)
The token *nominally* targets 1 PMUSD ≈ US$1. In practice the peg is unenforced: the persistent deep discount means whatever NAV/redemption mechanism may exist is either gated, unavailable to ordinary holders, or not trusted by the market. A working RWA stablecoin keeps price ≈ NAV via reliable redemption; PMUSD's chart shows that link is broken.

### Yield mechanism
RAAC markets on-chain yield from deploying RWA collateral into DeFi. Given the de-peg, **any advertised yield must be weighed against severe principal risk** and is kept strictly qualitative here — a high headline yield on a sub-par, illiquid token is not a free lunch but compensation for (realized) impairment risk.

### Mint / redeem & gating
If a 1:1 redemption-at-NAV mechanism exists, the persistent ~23% discount (and historical ~89% discount) suggests it is either gated, unavailable to ordinary holders, or not trusted — the usual signature of a broken RWA stablecoin. On-chain price is dominated by a single shallow Uniswap V3 pool rather than an issuer redemption window.

### Issuer / regulatory wrapper
Issued by **Real Asset Acquisition Corp (RAAC)**; the GitHub org is listed as "Regnum Aurum Acquisition Corp." Commodity-backed tokens face commodities- and securities-law scrutiny, and a self-described "stablecoin" trading 23% off peg invites additional regulatory attention.

---

## Comparison vs Peers

| Product | Backing | Peg status | Liquidity | Notes |
|---|---|---|---|---|
| **PMUSD** (RAAC) | Precious-metals / RWA collateral | **Broken** (~$0.77; ATL $0.12) | Very thin (~$31.5K/24h) | Chronically de-pegged "stablecoin" |
| **PAXG** (Paxos) | Allocated physical gold | Tracks gold price (not $1) | Deep | Per-token = 1 fine troy oz gold |
| **XAUT** (Tether Gold) | Allocated physical gold | Tracks gold price (not $1) | Deep | Gold-backed, redeemable |
| **USDC** (Circle) | Cash + short Treasuries | On-peg $1 | Deep | Benchmark fiat stablecoin |

The instructive contrast: established gold tokens (**PAXG**, **XAUT**) do *not* try to hold $1 — they openly track the gold price and offer credible redemption, so they trade near fair value. PMUSD attempts a **$1 peg on metals/real-asset collateral but fails to defend it**, which is the worst of both worlds: neither a clean commodity tracker nor a working dollar stablecoin.

---

## How / Where It Trades

- **Primary venue:** on-chain on [[ethereum|Ethereum]] (`0xc0c17dd08263c16f6b64e772fb9b723bf1344ddf`), notably a Uniswap V3 PMUSD/[[usdc|USDC]] pool.
- **Liquidity caveat:** extremely thin — only ~$31.5K of 24h volume against a nominal ~$72M cap. A token this illiquid and this far off peg is very hard to exit near par; the on-chain price is dominated by a shallow Uniswap pool, so prints are unreliable and slippage on any meaningful size is severe.
- **No CEX presence** in CoinGecko data; the single DEX pool is effectively the entire market.

---

## Narrative / Category & Catalysts

PMUSD sits at the intersection of **RWA tokenization** and **commodity-backed stablecoins** — a narrative with genuine demand, but PMUSD is a cautionary case rather than a leader. Relevant factors:
- **Restoration catalysts (speculative):** credible reserve attestations, a working redemption window, or fresh collateral injection could in principle narrow the discount — but none is documented here.
- **Continued impairment:** absent those, the discount can persist or widen, especially under stress.
- **Macro backdrop:** as of 2026-06-22 the [[crypto-fear-and-greed-index|Fear & Greed Index]] reads **21 (Extreme Fear)** in an established bear market — the regime in which fragile, thinly-backed RWA tokens are *least* able to defend their peg.

---

## History / Timeline

| Date | Event |
|---|---|
| (undated) | All-time-high price of $1.037 — the token's only sustained period near/above peg |
| (undated) | All-time-low price of $0.1162 — a ~89% collapse from the $1 target |
| 2026-04-09 | Captured in CoinGecko top-1000 snapshot ([[coingecko-top-1000-2026-04-09]]) |
| 2026-06-21 | Market snapshot: $0.7681 (~23% below peg), 24h -1.72%, market cap ~$72.2M |

*(Exact dates for the ATH/ATL prints are not in the ingested data and are therefore left undated rather than fabricated.)*

---

## Risks

- **De-peg risk (realized, severe):** PMUSD is **already de-pegged** (~$0.77, ATL $0.1162). This is the headline risk and it has materialized — holders have suffered large mark-to-market losses versus the $1 target.
- **NAV-gap / collateral risk:** the deep, persistent discount points to impaired or illiquid precious-metals/RWA backing, or an inability to redeem at NAV. The market is pricing material doubt about reserve quality or accessibility.
- **Redemption-gating risk:** any par-redemption mechanism appears gated, unavailable, or untrusted — ordinary holders cannot reliably exit at $1.
- **Issuer / custodian counterparty risk:** heavy dependence on RAAC to hold, value, and honor the real-asset collateral; a metals-backed token is only as sound as the custody and audit behind it.
- **Liquidity risk:** essentially no depth (~$31.5K/24h in one Uniswap pool); exiting is punishing and prints are unreliable.
- **Regulatory risk:** commodity-backed / metals tokens face commodities and securities scrutiny, and a broken "stablecoin" invites added regulatory attention.
- **Macro backdrop:** the Extreme-Fear / bear regime (see above) is precisely when thinly-backed RWA tokens are least able to defend a peg.

---

## Trading / Usage Playbook

- **Do not treat as a stablecoin.** PMUSD is a broken peg; it is not a safe $1 unit of account and should not be used as settlement collateral.
- **Discount ≠ guaranteed value.** A price of $0.77 vs a $1 "target" is not a 30% upside trade — it reflects realized impairment; the gap can persist or widen.
- **Liquidity trap.** With ~$31.5K/24h in a single pool, any non-trivial position is effectively illiquid; assume severe slippage to exit.
- **Demand verifiable reserves before any exposure.** Without independent, current attestation of metals/RWA backing and a working redemption window, treat principal as at risk.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 94.0M PMUSD |
| **Total Supply** | 94.0M PMUSD |
| **Max Supply** | Unlimited |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.037 |
| **All-Time Low** | $0.1162 — ~89% de-peg |
| **Current Price** | $0.7681 (~23% below $1 target) |
| **24h Change** | -1.72% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc0c17dd08263c16f6b64e772fb9b723bf1344ddf` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XC0C17DD08263C16F6B64E772FB9B723BF1344DDF/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://raac.io/](https://raac.io/) |
| **Twitter** | [@Raacfi](https://twitter.com/Raacfi) |
| **Discord** | [https://discord.com/invite/raac](https://discord.com/invite/raac) |
| **GitHub** | [https://github.com/RegnumAurumAcquisitionCorp](https://github.com/RegnumAurumAcquisitionCorp) |
| **Whitepaper** | [https://docs.raac.io/](https://docs.raac.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $31.5K |
| **Market Cap Rank** | #344 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[stablecoin]] / [[stablecoins]]
- [[real-world-assets]]
- [[gold]] / [[commodities]]
- [[depeg]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PMUSD |
| **Market Cap Rank** | #347 |
| **Market Cap** | $69.05M |
| **Current Price** | $0.7346 |
| **Categories** | Stablecoins, Real World Assets (RWA) |
| **Website** | [https://raac.io/](https://raac.io/) |

---

## Overview

Real Asset Acquisition Corp (RAAC) is a decentralized finance (DeFi) protocol powered by real-world assets (RWAs). 

The ecosystem empowers token holders through a set of custom-built products to tokenize real-world assets; deploying traditional finance assets into DeFi, with a goal to unlock liquidity and on-chain yield opportunities. This model allows RAAC to expand DeFi liquidity collateralized by RWAs.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
