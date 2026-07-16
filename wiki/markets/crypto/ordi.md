---
title: "ORDI Token"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, nft]
aliases: ["ORDI", "ORDI token"]
entity_type: protocol
headquarters: "Decentralized"
related: ["[[bitcoin-ordinals]]", "[[bitcoin]]", "[[brc-20]]", "[[crypto-markets]]", "[[hyperliquid]]", "[[runes]]"]
---

# ORDI Token

**ORDI** (ticker **ORDI**) is the first [[brc-20|BRC-20]] fungible token, minted via the [[bitcoin-ordinals|Bitcoin Ordinals]] protocol on [[bitcoin|Bitcoin]] on March 8, 2023. Despite being fungible, ORDI is culturally tied to the Ordinals/inscriptions ecosystem — it is the flagship [[brc-20|BRC-20]] token and the most liquid proxy for speculation on Bitcoin inscription activity and the experimental "tokens on Bitcoin" thesis.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ORDI |
| **Market Cap Rank** | #355 |
| **Current Price** | $3.31 |
| **Market Cap** | $69.56M |
| **24h Volume** | $34.10M |
| **24h Change** | -5.68% |
| **7d Change** | -2.61% |
| **Market Cap / FDV** | ~1.00 |
| **All-Time High** | $95.52 (2024-03-05) — now ~-96.5% |
| **All-Time Low** | $2.12 (2026-03-29) — now ~+56.4% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

ORDI is down ~5.7% on the day and ~2.6% on the week, but its 24h volume (~$34.1M) is large relative to its ~$70M market cap — a very high turnover ratio (~49%) that flags speculative, perp-driven trading. This stands out against the broader risk-off backdrop, where the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** within an **Established Bear Market** as of 2026-06-21. ORDI sits ~96% below its March-2024 mania high but ~56% above the all-time low it set in March 2026.

---

## Technology / Protocol

ORDI exists on the [[bitcoin|Bitcoin]] base layer via two stacked experimental standards:

| Layer | What it does |
|---|---|
| **[[bitcoin-ordinals|Ordinals]]** | Assigns a serial number ("ordinal") to each satoshi and lets arbitrary data ("inscriptions") be attached to it — effectively NFTs on Bitcoin |
| **[[brc-20|BRC-20]]** | A token standard (proposed by pseudonymous "Domo") that uses Ordinals JSON inscriptions to deploy, mint, and transfer fungible tokens |

BRC-20 is **not a smart-contract standard** like Ethereum's ERC-20. There is no virtual machine; balances are tracked by off-chain indexers reading inscription data from the Bitcoin chain. ORDI was the first token deployed under this standard. Because mints and transfers are Bitcoin transactions, BRC-20 activity competes directly for Bitcoin block space and drives fee spikes during mania.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 21.0M ORDI |
| **Total Supply** | 21.0M ORDI |
| **Max Supply** | 21.0M ORDI (fully minted) |
| **Market Cap / FDV** | ~1.00 |

ORDI's supply is a deliberate homage to Bitcoin: **21 million tokens**, fully minted and distributed via the BRC-20 mint mechanism (anyone could inscribe a mint up to a per-transaction cap until the cap was reached). Because it is **fully circulating** with no team allocation or vesting unlocks (MC/FDV ≈ 1.00), ORDI has no dilution overhang — its float is fixed, which both removes unlock pressure and contributes to its high volatility.

---

## Market Structure & Derivatives

**Centralized spot venues:** Binance (ORDI/USDT — the deepest market and the key listing that catalyzed BRC-20 awareness), Bitget, KuCoin, and Crypto.com Exchange.

**On-chain:** Native ORDI trades within the Ordinals/BRC-20 ecosystem (marketplaces such as Unisat and OKX's Ordinals market). A wrapped representation also exists on [[solana|Solana]] for DEX trading.

**Derivatives:** ORDI has a perpetual market on [[hyperliquid|Hyperliquid]] (ORDI-PERP) plus deep CEX perps. Given the elevated ~49% volume-to-cap ratio, much of ORDI's flow is leverage-driven; funding swings hard with sentiment and OI can spike fast on Bitcoin-ecosystem catalysts, making it prone to violent squeezes in both directions.

---

## Use Case / Narrative / Category

ORDI belongs to the **Bitcoin Ordinals / BRC-20** category. It has no smart-contract utility in the Ethereum sense; its "use case" is as the original and most recognizable experiment in issuing fungible tokens directly on Bitcoin via inscriptions. It functions primarily as a meme/speculative bellwether: when interest in Bitcoin Ordinals, inscriptions, and Bitcoin-native assets rises, ORDI is the first name traders reach for. Its fortunes are closely correlated with broader Bitcoin-ecosystem narrative cycles.

| Peer / standard | Category | Notes |
|---|---|---|
| **ORDI** | BRC-20 (flagship) | First and most liquid BRC-20 |
| SATS | BRC-20 | High-supply Ordinals meme |
| [[runes|Runes]] | Bitcoin fungible-token protocol | Post-2024-halving competitor to BRC-20 |
| Bitcoin Ordinals NFTs | Inscriptions | The non-fungible side of the same ecosystem |

---

## Valuation Framing

Like other inscription-era assets, ORDI has no cash flow and is best framed reflexively: its value tracks the **Bitcoin-native speculation cycle** (Ordinals, BRC-20, [[runes|Runes]]) rather than any fundamental. With supply fully circulating, market cap equals FDV — no dilution discount applies. The key relative gauge is ORDI's mindshare versus competing Bitcoin token standards: the rise of Runes after the 2024 halving fragmented inscription flow, structurally diluting attention even though ORDI's own token supply is fixed.

---

## Notable History

- **2023-03-08** — ORDI minted, the first BRC-20 token, shortly after Domo proposed the experimental standard.
- **November 2023** — A **Binance listing** brought mainstream attention and a major rally, helping define the BRC-20 narrative.
- **2024-03-05** — All-time high near **$95.52** during peak Ordinals/inscriptions mania.
- **2024-2026** — Drew down ~96% as the inscriptions narrative cooled and Runes/competing standards fragmented attention.
- **2026-03-29** — All-time low of $2.12; has since recovered ~56%.

---

## Risks

- **Narrative fragility** — value rests almost entirely on Ordinals/BRC-20 hype, with no cash-flow or utility backstop.
- **Standard competition** — [[runes|Runes]] and other Bitcoin-native token standards compete for the same speculative flow.
- **Extreme volatility / leverage** — high perp turnover (~49% of cap traded daily) means brutal squeezes in both directions.
- **Bitcoin-block-space dependency** — BRC-20 activity competes for block space and rises/falls with fee markets.
- **Bear-market beta** — a small-cap (#355) speculative token in an extreme-fear environment (Fear & Greed = 23).

---

## Related

- [[crypto-markets]]
- [[bitcoin]]
- [[bitcoin-ordinals]]
- [[brc-20]]
- [[runes]]
- [[hyperliquid]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ORDI |
| **Market Cap Rank** | #300 |
| **Market Cap** | $78.56M |
| **Current Price** | $3.74 |
| **Categories** | Meme, BRC-20, Inscriptions |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 21.00M ORDI |
| **Total Supply** | 21.00M ORDI |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $78.56M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $95.52 (2024-03-05) |
| **Current vs ATH** | -96.08% |
| **All-Time Low** | $2.12 (2026-03-29) |
| **Current vs ATL** | +76.63% |
| **24h Change** | +9.23% |
| **7d Change** | +6.24% |
| **30d Change** | +4.33% |
| **1y Change** | -61.13% |

---

## Platform & Chain Information

**Native Chain:** Ordinals

### Contract Addresses

| Chain | Address |
|---|---|
| Ordinals | `b61b0172d95e266c18aea0c624db987e971a5d6d4ebc2aaed85da4642d635735i0` |
| Solana | `u9nmK5sQovm6ACVCQbbq8xUMpFqdPSYxdxVwXUX4sjY` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ORDI/USDT | N/A |
| Bitget | ORDI/USDT | N/A |
| KuCoin | ORDI/USDT | N/A |
| Crypto.com Exchange | ORDI/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | U9NMK5SQOVM6ACVCQBBQ8XUMPFQDPSYXDXVWXUX4SJY/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $28.29M |
| **Market Cap Rank** | #300 |
| **24h Range** | $3.41 — $3.75 |
| **CoinGecko Sentiment** | 75% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
