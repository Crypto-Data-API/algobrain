---
title: "PAX Gold (PAXG)"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: review
tags: [crypto, gold, paxos, stablecoin, tokenized-asset, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives]
entity_type: protocol
aliases: ["PAXG", "Pax-Gold", "pax-gold"]
website: "https://paxos.com/paxgold"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cash-and-carry]]"]
headquarters: "Decentralized"
---

# PAX Gold (PAXG)

**PAX Gold (PAXG)** is a tokenized gold asset on the [[ethereum]] blockchain, where each PAXG token is backed 1:1 by one fine troy ounce of physical gold held in London Bullion Market Association (LBMA) vaults. Issued by **Paxos Trust Company** (a New York-regulated financial institution), PAXG bridges traditional commodity markets and [[crypto-markets|crypto]], allowing traders to hold and transfer gold exposure on-chain.

---

## Key Features

| Feature | Detail |
|---|---|
| **Backing** | 1 PAXG = 1 troy oz gold (physically allocated, audited monthly) |
| **Blockchain** | [[ethereum]] (ERC-20) |
| **Issuer** | Paxos Trust Company (NYDFS-regulated) |
| **Redemption** | Redeemable for physical gold or USD |
| **Divisibility** | Fractional ownership (can hold 0.001 PAXG) |
| **Market Cap** | Varies with gold price; typically $500M-$1B range |

---

## How It Works

Paxos purchases physical gold and stores it in LBMA-accredited vaults. For each ounce custodied, one PAXG token is minted on Ethereum. Token holders have legal ownership of the underlying gold. Monthly attestation reports verify 1:1 backing. Users can redeem PAXG for physical gold bars (minimum 430 oz) or sell on exchanges.

---

## Trading Relevance

- PAXG provides **gold exposure within crypto portfolios** -- useful for hedging during risk-off environments without leaving the on-chain ecosystem
- Trades on [[decentralized-exchanges|DEXs]] and centralized exchanges, enabling gold [[arbitrage]] against spot gold (XAU/USD)
- PAXG can serve as collateral in [[defi]] lending protocols, allowing traders to borrow against gold holdings
- Price tracks physical gold spot price closely, with minor premiums/discounts driven by on-chain demand
- PAXG-PERP on [[hyperliquid]] allows leveraged gold exposure via crypto infrastructure
- Useful as a safe-haven allocation during [[crypto-winter|crypto bear markets]] while remaining on-chain

---

## Trading Profile

### Venues & liquidity

PAXG is a genuine two-venue derivatives market. It trades **spot and a USD-margined perpetual on [[binance]]**, and as **PAXG-PERP on [[hyperliquid]]** with leverage up to roughly 40-50x. Binance provides deep spot/perp order books and the primary funding-rate reference, while Hyperliquid offers on-chain leverage and an independent funding curve. The dual-venue structure means execution can be split or routed to the tighter book, and cross-venue basis/funding differences are observable rather than theoretical. Because PAXG price simply tracks physical gold (XAU/USD), depth is respectable for its rank but thinner than major-cap crypto perps, so size positions with care and expect wider slippage on large clips, especially on Hyperliquid.

### Applicable strategies

- [[cash-and-carry]] -- long spot PAXG on Binance against a short perp captures any positive basis while the token remains 1:1 gold-backed, keeping the hedge nearly delta-neutral.
- [[basis-trading]] -- the Binance perp and Hyperliquid PAXG-PERP each carry their own basis to gold spot, giving clean converging legs to trade.
- [[hl-vs-cex-funding-divergence]] -- Hyperliquid and Binance funding on a low-crypto-beta gold token often diverge, letting you be long the cheaper-funding venue and short the richer one.
- [[funding-rate-harvest]] -- gold's muted directional drift makes a delta-hedged PAXG perp position suitable for collecting funding with limited trend risk.
- [[mean-reversion]] -- PAXG's on-chain premium/discount to physical gold tends to revert, so deviations from XAU/USD fair value are fadeable.
- [[pairs-trading]] -- PAXG versus XAU/USD (or versus another tokenized-gold proxy) is a tight, fundamentally anchored pair for relative-value trades.

### Volatility & regime character

PAXG is not a crypto-beta asset -- it is a **tokenized real-world commodity** whose price is pinned to physical gold. Realized volatility is far lower than typical altcoins and it carries **low, often near-zero or negative correlation to BTC/ETH beta**, frequently behaving as a safe-haven that firms during crypto risk-off. Its regime is driven by gold macro (real yields, USD, geopolitical risk) rather than the crypto narrative cycle, making it a diversifier and hedge within a crypto book.

### Risk flags

- **Venue/liquidity concentration** -- meaningful perp liquidity sits on just two venues; depth is thinner than major-cap crypto, so large orders move price and Hyperliquid clips can slip.
- **Peg/backing dependence** -- value relies on Paxos's 1:1 physical gold custody and monthly attestations; any custody, audit, or issuer/regulatory event (NYDFS-regulated) could dislocate the on-chain price from gold.
- **Basis vs. underlying** -- the on-chain price can trade at a premium/discount to XAU/USD; hedges assuming perfect tracking bear residual basis risk.
- **Funding dislocations** -- low crypto beta plus modest depth can produce sharp, idiosyncratic funding swings across Binance and Hyperliquid that whipsaw carry positions.
- **Macro-driven gaps** -- price is exposed to gold macro shocks (real-rate and USD moves) that are unrelated to crypto flows.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=PAXG` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=PAXG` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=PAXG&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=PAXG&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=PAXG"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[ethereum]] -- The blockchain PAXG is issued on
- [[crypto-markets]] -- Broader crypto market context
- [[defi]] -- Protocols where PAXG can be used as collateral

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | PAXG |
| **Market Cap Rank** | #44 |
| **Market Cap** | $1.91B |
| **Current Price** | $4,176.78 |
| **Categories** | Tokenized Assets, Tokenized Gold, Ethereum Ecosystem, Real World Assets (RWA), Tokenized Commodities |
| **Website** | [https://www.paxos.com/paxgold/](https://www.paxos.com/paxgold/) |
> *Market data refreshed 2026-06-12 (CoinGecko top-1000 snapshot).*

---

## Overview

PAX Gold (PAXG) is an asset-backed token where one token should represent one fine troy ounce of a London Good Delivery gold bar, stored in professional vault facilities. Anyone who owns PAXG has ownership rights to that gold under the custody of Paxos Trust Company. Since PAXG represents physical gold, its value is tied directly to the real-time market value of that physical gold.

PAXG gives customers the benefits of actual physical ownership of specific gold bars with the speed and mobility of a digital asset. Customers are able to have fractional ownership of physical bars. On the Paxos platform, customers can convert their tokens to allocated gold, unallocated gold, or fiat currency (and vice versa) quickly and efficiently, reducing their exposure to settlement risk. PAXG is also available for trading on Paxos’ itBit exchange. PAXG will also be available on other crypto-asset exchanges, wallets, lending platforms and elsewhere within the crypto ecosystem. 

At any time, PAXG holders can lookup the serial number, value and physical characteristics of their vaulted gold just by entering their Ethereum wallet address on the PAXG lookup tool on Paxos.com/paxgold.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 514,129 PAXG |
| **Total Supply** | 514,129 PAXG |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $2.41B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5,619.09 (2026-01-29) |
| **Current vs ATH** | -16.43% |
| **All-Time Low** | $1,399.64 (2019-11-18) |
| **Current vs ATL** | +235.50% |
| **24h Change** | -2.03% |
| **7d Change** | -1.47% |
| **30d Change** | -8.73% |
| **1y Change** | +56.72% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x45804880de22913dafe09f4980848ece6ecbaf78` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | PAXG/USDT | N/A |
| Kraken | PAXG/USD | N/A |
| Bitget | PAXG/USDT | N/A |
| KuCoin | PAXG/USDT | N/A |
| Crypto.com Exchange | PAXG/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | PAXG-PERP | Perpetual |
| Uniswap V3 (Ethereum) | 0X45804880DE22913DAFE09F4980848ECE6ECBAF78/0X68749665FF8D2D112FA859AA293F07A622782F38 | Spot |
| Uniswap V2 (Ethereum) | 0X45804880DE22913DAFE09F4980848ECE6ECBAF78/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.paxos.com/paxgold/](https://www.paxos.com/paxgold/) |
| **Twitter** | [@paxosglobal](https://twitter.com/paxosglobal) |
| **GitHub** | [https://github.com/paxosglobal/paxos-gold-contract](https://github.com/paxosglobal/paxos-gold-contract) |
| **Whitepaper** | [https://www.paxos.com/pax-gold](https://www.paxos.com/pax-gold) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $319.48M |
| **Market Cap Rank** | #44 |
| **24h Range** | $4,689.31 — $4,811.69 |
| **CoinGecko Sentiment** | 75% positive |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
