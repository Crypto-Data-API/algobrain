---
title: "TerraClassicUSD"
type: entity
created: 2026-04-09
updated: 2026-04-14
status: good
tags: [crypto, stablecoin, defi, terra, algorithmic-stablecoin, collapse]
aliases: ["USTC", "UST", "TerraUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.terra-classic.io"
related: ["[[crypto-markets]]", "[[terra-luna-collapse]]", "[[terra-luna]]", "[[terra-luna-2]]", "[[2022-05-terra-luna-depeg-arb]]", "[[stablecoins]]", "[[stablecoin-depegs]]", "[[algorithmic-stablecoin]]"]
---

# TerraClassicUSD

**TerraClassicUSD** (USTC, originally UST / TerraUSD) was the largest [[algorithmic-stablecoin|algorithmic stablecoin]] in crypto history before its catastrophic depeg in May 2022. At its peak, UST had an $18.7 billion market cap and was backed entirely by a mint/burn arbitrage mechanism with [[terra-luna|LUNA]] — no fiat reserves, no over-collateralisation. When the mechanism failed, UST depegged from $1 to under $0.10 in less than a week, triggering the [[terra-luna-collapse]] and destroying ~$40 billion in combined value.

Since the collapse, USTC has been a freely traded token with no active peg mechanism. It trades at fractions of a cent, driven by speculation rather than any fundamental value.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USTC (originally UST) |
| **Market Cap Rank** | #714 |
| **Market Cap** | ~$25.5M |
| **Current Price** | ~$0.0046 |
| **ATH** | $1.09 (January 2021) |
| **Current vs ATH** | -99.58% |
| **Circulating Supply** | 5.58B USTC |
| **Category** | Former algorithmic stablecoin (no longer pegged) |

---

## How UST Worked (Before Collapse)

UST maintained its $1 peg through a **mint/burn arbitrage** with LUNA:

- **UST < $1**: Buy cheap UST → burn it → mint $1 of LUNA → sell LUNA for profit. UST supply contracts, price rises
- **UST > $1**: Burn LUNA → mint UST at $1 → sell UST above par. UST supply expands, price falls

This mechanism worked under normal conditions but was fatally vulnerable to reflexive feedback loops. When LUNA's price collapsed, burning UST yielded worthless LUNA, and the arbitrage that was supposed to stabilize the peg instead hyperinflated LUNA's supply. See [[2022-05-terra-luna-depeg-arb]] for the detailed mechanics.

**Anchor Protocol** subsidized ~19.5% APY on UST deposits, attracting $14B and creating massive concentrated demand. When large withdrawals began, the death spiral was unstoppable.

---

## The Depeg

| Date | UST Price | What Happened |
|------|-----------|---------------|
| May 7, 2022 | $0.985 | Large sells on Curve; first depeg |
| May 9 | $0.90 | LFG deploys BTC reserves to defend |
| May 10 | $0.68 | Reserves exhausted; arb hyperinflating LUNA |
| May 11 | $0.35 | Full bank run underway |
| May 12-13 | $0.10 | Peg irrecoverable; chain halted |

For the full timeline and contagion cascade, see [[terra-luna-collapse]].

---

## Post-Collapse Status

After the Terra 2.0 fork (May 28, 2022):
- UST was renamed **USTC** (TerraClassicUSD)
- The mint/burn stabilization mechanism was **permanently disabled**
- USTC trades purely on speculation — there is no peg maintenance and no collateral
- Community proposals to "re-peg" USTC have been discussed but none have produced a viable mechanism
- The SEC classified UST as a security in its case against Terraform Labs

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$2.1M |
| **Typical behavior** | Speculative micro-cap trading; occasional spikes on community re-peg proposals |
| **Exchange listings** | Binance (USTC/USDT), Bitget, KuCoin |
| **Perpetual futures** | Available on [[hyperliquid|Hyperliquid]] (USTC-PERP) |

USTC has no fundamental value driver. Any trading thesis is purely speculative or community-narrative driven.

---

## Major News & Events

| Date | Event |
|------|-------|
| Dec 2017 | Terra whitepaper published by Do Kwon and Daniel Shin |
| Mar 2021 | Anchor Protocol launches; UST growth accelerates |
| Apr 2022 | UST reaches $18.7B market cap; becomes 3rd largest stablecoin |
| May 7-13, 2022 | [[terra-luna-collapse]]: UST depegs and collapses to ~$0.10 |
| May 28, 2022 | Terra 2.0 fork; UST renamed USTC, stabilization mechanism disabled |
| Apr 2024 | SEC civil trial: jury finds UST was a security |
| Jun 2024 | Terraform Labs settles with SEC for $4.47 billion |

---

## See Also

- [[terra-luna-collapse]] — Full crash timeline and analysis
- [[2022-05-terra-luna-depeg-arb]] — The arbitrage death spiral mechanics
- [[terra-luna]] — Terra Luna Classic (LUNC), the companion token
- [[stablecoins]] — Stablecoin types and risk comparison
- [[stablecoin-depegs]] — History of de-peg events
- [[dai]] — Contrast: over-collateralised stablecoin that survived the crypto winter
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- SEC v. Terraform Labs (civil case), S.D.N.Y.
