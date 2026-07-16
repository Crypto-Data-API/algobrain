---
title: "Bitcoin SV"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [bitcoin, crypto, history, regulation, hyperliquid, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["BSV", "Bitcoin Satoshi Vision"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://bitcoinsv.com/"
related: ["[[binance]]", "[[bitcoin-cash]]", "[[bitcoin]]", "[[crypto-markets]]", "[[hyperliquid]]", "[[kraken]]", "[[proof-of-work]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[pairs-trading]]", "[[event-driven-trading]]"]
---

# Bitcoin SV

**Bitcoin SV** (ticker **BSV**, "Satoshi Vision") is a [[proof-of-work|proof-of-work]] (SHA-256) Layer-1 blockchain that **hard-forked from [[bitcoin-cash|Bitcoin Cash]] (BCH) in November 2018**, BCH itself being a 2017 fork of [[bitcoin|Bitcoin]]. It claims to implement the "original" Bitcoin design with unbounded block sizes and restored Script opcodes. For traders, BSV is primarily a legacy-fork relative-value and event-driven asset: its price history is dominated by Craig Wright's legal saga (the 2024 COPA ruling that he is **not** Satoshi Nakamoto) and the fallout from its 2019 delisting by major exchanges, which spawned a $13 billion lawsuit finally killed by the UK Supreme Court in December 2025.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | BSV |
| **Chain** | Own Layer 1, SHA-256 [[proof-of-work|proof of work]] |
| **Current Price** | $11.70 |
| **Market Cap** | $234,583,605 |
| **Market Cap Rank** | #153 |
| **Fully Diluted Valuation** | $234,584,008 |
| **24h Volume** | $7,142,671 |
| **24h Range** | $11.46 — $11.73 |
| **24h Change** | +1.44% |
| **7d Change** | -0.51% |
| **Categories** | Bitcoin Fork, Proof of Work, Layer 1 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

BSV trades at **~$11.70, rank #153, ~$235M market cap** — more than **97% below its 2021 ATH** ($489.75) and only ~5% above a fresh all-time low ($11.09) set on **2026-06-11**. The decline through June 2026 fits the macro backdrop: crypto [[fear-and-greed-index|Fear & Greed]] reads **~23 (Extreme Fear)** within an **Established Bear Market**, and legacy-PoW forks with no revival catalyst are among the weakest cohorts.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BSV |
| **Fork lineage** | BTC → BCH (Aug 2017) → **BSV (Nov 2018 hash war)** |
| **Chain** | Own Layer 1, SHA-256 proof of work (shares mining algorithm with BTC/BCH) |
| **Sector** | Bitcoin fork / legacy PoW; pitches itself as enterprise data + micropayments chain |
| **Supply mechanics** | ~20M of 21M max supply circulating; MC/FDV ≈ 1.0 (fully diluted, no unlock overhang) |
| **Key infrastructure** | Teranode — scaling architecture targeting 1M+ TPS via multi-GB blocks |
| **Website** | [https://bitcoinsv.com/](https://bitcoinsv.com/) |

---

## Fork History & Proof of Work

BSV is the product of a two-step fork lineage off [[bitcoin|Bitcoin]], all sharing Bitcoin's SHA-256 [[proof-of-work|proof-of-work]] mining:

1. **August 2017 — BTC → [[bitcoin-cash|Bitcoin Cash]] (BCH).** A faction favouring larger blocks for cheap on-chain payments split from Bitcoin (which kept 1MB blocks and pursued off-chain scaling via the Lightning Network), raising the block size to 8MB.
2. **November 2018 — BCH → BSV ("hash war").** Within Bitcoin Cash, a further split pitted **Bitcoin ABC** (which became BCH) against **Bitcoin SV**, championed by Craig Wright (nChain) and Calvin Ayre. The two camps pointed mining hash power at each other's chains in a brief but costly "hash war"; BSV emerged as a separate chain pursuing **unbounded block sizes** and **re-enabled Script opcodes** disabled on BTC.

Because all three chains share SHA-256, the same ASIC fleets can mine BTC, BCH or BSV — BSV captures only a tiny fraction of total SHA-256 hash rate, which keeps its chain security low relative to BTC and makes hash-rate migration (and theoretical reorg risk) a structural concern. The **Teranode** node architecture, rolled out by the BSV Association, targets throughput in the millions of transactions per second with sub-$0.001 fees, betting on enterprise data and micropayment use-cases rather than store-of-value.

---

## Overview

Bitcoin SV emerged from the November 2018 "hash war" split of Bitcoin Cash, championed by Craig Wright (nChain) and Calvin Ayre. The project's stated goal is to fulfil the original vision of the Bitcoin protocol as described in Satoshi Nakamoto's white paper: it removed artificial block size limits and re-enabled Script commands disabled on BTC, allowing very large blocks, low-fee micropayments, tokens, and on-chain data applications. The **Teranode** node architecture, rolled out by the BSV Association, targets throughput in the millions of transactions per second with sub-$0.001 fees.

### Legal and market history (the dominant price driver)

- **April 2019** — [[binance|Binance]], [[kraken|Kraken]], ShapeShift and others **delisted BSV** after Craig Wright's legal threats against critics who disputed his Satoshi claim; BSV fell ~17% on the Binance announcement.
- **March 2024** — In *COPA v Wright* (UK High Court), Justice Mellor ruled Craig Wright is **not** Satoshi Nakamoto and did not author the Bitcoin white paper; the court later found he had forged documents on a massive scale, and in **December 2024** Wright received a 12-month suspended sentence for contempt of court.
- **2024-2025** — BSV investors pursued a **£9-13 billion "loss of chance" claim** against Binance, Kraken and others over the 2019 delistings, arguing BSV would have rivalled BTC absent the delisting. Lower courts struck out the speculative-gains theory.
- **December 15, 2025** — The **UK Supreme Court refused the appeal**, upholding lower-court decisions and effectively blocking claims that exchanges can be liable for speculative foregone gains after delisting a token — a precedent relevant to all exchange-delisting disputes. (Source: CoinDesk, Decrypt, Dec 2025.)
- Wright separately filed a ~$1.18B lawsuit against Bitcoin Core developers, claiming BSV is the "real" Bitcoin; courts have been uniformly hostile to his claims post-COPA.

As of June 2026 BSV trades **~$11.70, ~97% below its 2021 all-time high** (~$490), having just printed a fresh ATL ($11.09) on 2026-06-11, with no major revival catalyst; the narrative rests on Teranode enterprise adoption and a niche committed community. (Verified via Perplexity + web search, 2026-06-10; price refreshed 2026-06-21.)

---

## Tokenomics

| Metric | Value (2026-06-21 snapshot) |
|---|---|
| **Circulating Supply** | ~20.04M BSV |
| **Total Supply** | ~20.04M BSV |
| **Max Supply** | 21.0M BSV |
| **MC / FDV Ratio** | ~1.00 (no meaningful unlock overhang) |
| **Issuance** | PoW block rewards, Bitcoin-style halvings |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $489.75 (2021-04-16) |
| **All-Time Low** | $11.09 (2026-06-11) |
| **Snapshot (2026-06-21)** | $11.70, ~$235M mcap, rank #153 |
| **Current vs ATH** | -97.62% |
| **Current vs ATL** | +5.26% |
| **7d Change** | -0.51% |

The grind to a new ATL in June 2026 (below the prior $11.56 low) confirms BSV has no independent bid; it has tracked the broader legacy-PoW weakness in the Established Bear Market regime.

---

## Trading Relevance

- **Where it trades**: perps on [[hyperliquid|Hyperliquid]] (BSV-PERP); spot on Upbit (BSV/KRW — Korean flow is a large share of volume), Bitget, KuCoin. Still absent from Binance and Coinbase post-2019 delisting — a structural liquidity discount.
- **Narrative basket**: legacy PoW / Bitcoin-fork basket (BCH, BSV, and "old L1" rotations). BSV often catches delayed beta when BCH squeezes, making BCH/BSV a candidate relative-value pair.
- **Event-driven angle**: BSV's biggest historical moves are court-ruling driven (COPA 2024, Supreme Court Dec 2025, periodic "Satoshi reveal" headlines). The Korean-exchange concentration also makes it prone to kimchi-premium style dislocations and pump episodes.
- **Risks**: thin order books, headline risk from Wright litigation, possible further delistings, and near-zero organic developer mindshare relative to its market cap.

### Peer table — Bitcoin-fork / legacy-PoW basket

| Asset | Origin | Mining | June 2026 cap | Note |
|---|---|---|---|---|
| [[bitcoin\|BTC]] | Genesis (2009) | SHA-256 PoW | Mega-cap | The reference asset |
| [[bitcoin-cash\|BCH]] | BTC fork (Aug 2017) | SHA-256 PoW | Mid-cap | Bigger blocks; BSV's parent chain |
| **BSV** | BCH fork (Nov 2018) | SHA-256 PoW | ~$235M (#153) | Unbounded blocks; litigation-scarred |

BSV often catches **delayed beta when BCH squeezes**, making **BCH/BSV a candidate relative-value pair**; the shared SHA-256 algorithm also links all three via miner hash-rate rotation.

---

## Market Structure

- **Who can hold / trade it**: anyone via the surviving venues, but the venue set is degraded — **delisted from [[binance|Binance]], [[kraken|Kraken]] and ShapeShift since April 2019**, and still absent from Binance and Coinbase, which imposes a structural liquidity discount versus other ~$200M-cap coins.
- **Liquidity caveats**: thin order books; **Upbit (BSV/KRW) Korean flow is a large share of volume**, making BSV prone to kimchi-premium-style dislocations and isolated pump episodes; perps liquidity on [[hyperliquid|Hyperliquid]] is the main derivatives venue.

---

## Exchange Listings

| Venue | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BSV-PERP | Perpetual |
| Upbit | BSV/KRW | Spot |
| Bitget | BSV/USDT | Spot |
| KuCoin | BCHSV/USDT | Spot |

Delisted from [[binance|Binance]], [[kraken|Kraken]], ShapeShift (April 2019).

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://bitcoinsv.com/](https://bitcoinsv.com/) |
| **Twitter** | [@BSVBlockchain](https://twitter.com/BSVBlockchain) |
| **GitHub** | [https://github.com/bitcoin-sv/bitcoin-sv](https://github.com/bitcoin-sv/bitcoin-sv) |

---

## Related

- [[bitcoin]]
- [[bitcoin-cash]]
- [[proof-of-work]]
- [[binance]]
- [[kraken]]
- [[crypto-markets]]
- [[hyperliquid]]

---

## Sources

- Market data: cryptodataapi.com / CoinGecko top-1000 snapshot, 2026-06-21
- CoinGecko snapshot, 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- CoinDesk, "UK Supreme Court refuses BSV appeal, narrowing $13 billion lawsuit against crypto exchanges," 2025-12-15: https://www.coindesk.com/policy/2025/12/15/uk-supreme-court-refuses-bsv-appeal-narrowing-usd13b-lawsuit-against-crypto-exchanges
- Decrypt, "UK Supreme Court Shuts Down $13 Billion Bitcoin SV Case Appeal": https://decrypt.co/352442
- Decrypt, "Craig Wright Says Bitcoin Devs 'Misled the Public' in New $1 Billion Lawsuit": https://decrypt.co/287138/craig-wright-bitcoin-new-lawsuit
- CryptoSlate, "Binance delists Bitcoin SV following Craig Wright's legal threats" (April 2019): https://cryptoslate.com/binance-delists-bitcoin-sv-following-craig-wrights-legal-threats/
- COPA v Wright ruling, UK High Court, March 2024 (widely reported)
- Perplexity + web verification, 2026-06-10

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 605 |
| **GitHub Forks** | 299 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.92M |
| **Market Cap Rank** | #141 |
| **24h Range** | $13.09 — $13.78 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

BSV is a **PERP-FIRST asset**: it trades as a perpetual on [[hyperliquid|Hyperliquid]] (**BSV-PERP**, leverage up to **~40-50x**) but is **NOT listed on Binance** — spot access is limited and largely offshore (Upbit KRW, Bitget, KuCoin), so directional and derivatives flow concentrates on the HL perp rather than any deep spot book. Because there is no large-cap CEX spot venue anchoring price, the HL perp is effectively the reference market for two-sided liquidity, and its order book is **thin relative to major alts**. Practically this means: keep clip sizes small, use limit/passive execution to avoid walking the book, expect wider slippage on market orders, and treat the high available leverage as a liquidation-risk amplifier rather than a sizing invitation. Spot-scattered, offshore liquidity also makes any spot-perp arbitrage operationally harder to run cleanly.

### Applicable strategies

- [[pairs-trading]] — BSV is the natural mean-reverting leg against [[bitcoin-cash|BCH]] (its parent chain); it often catches delayed beta when BCH squeezes, so a BCH/BSV spread trade captures the lag.
- [[cross-sectional-relative-value]] — rank BSV within the legacy-PoW / Bitcoin-fork basket (BTC, BCH, BSV) and trade its rich/cheap divergence versus the cohort rather than outright.
- [[event-driven-trading]] — BSV's largest moves are court-ruling driven (COPA, Craig Wright litigation, delisting-lawsuit rulings); position around scheduled legal catalysts on the HL perp.
- [[liquidation-cascade-fade]] — a thin perp book plus high available leverage makes BSV prone to sharp forced-liquidation wicks that overshoot and snap back, offering fade entries into extremes.
- [[crowded-long-funding-fade]] — small-cap fork with periodic pump episodes; when funding spikes positive on a crowded HL long, fading the stretched positioning is a repeatable setup.
- [[range-mean-reversion]] — with no independent bid and no revival catalyst, BSV spends long stretches range-bound, favouring reversion off the range edges over trend-chasing.

### Volatility & regime character

BSV is a **low-mindshare, litigation-scarred legacy-PoW / Bitcoin-fork alt** — high-beta to BTC on downside moves but with little independent upside bid. It behaves as a **high-beta, low-liquidity small cap**: it broadly tracks BTC/ETH risk regimes (rallying and selling with the majors) yet shows idiosyncratic pump-and-fade behaviour driven by Korean-exchange flow and legal-headline reflexivity. Correlation to BTC is meaningful in risk-off but decays around Wright/BSV-specific news, when the asset trades on its own narrative.

### Risk flags

- **Venue concentration**: no Binance/Coinbase listing; derivatives flow is concentrated on the single HL perp, and spot is thin/offshore (Upbit KRW share is large) — dislocations and kimchi-premium-style gaps are common.
- **Narrative dependence**: price is dominated by Craig Wright litigation and delisting-lawsuit headlines; there is minimal organic developer/adoption catalyst, so headline risk dominates fundamentals.
- **Perp funding dislocations**: thin OI plus offshore spot make funding on BSV-PERP volatile and prone to sharp swings during pump/liquidation episodes.
- **Liquidity/execution risk**: shallow books amplify slippage and make high leverage a fast route to liquidation; further delistings remain a tail risk given its history.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=BSV` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BSV` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BSV&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BSV&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BSV"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]

---
