---
title: "Huma Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, payment-solutions, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, altcoins]
aliases: ["HUMA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://huma.finance/"
related: ["[[crypto-markets]]", "[[defi]]", "[[real-world-assets]]", "[[solana]]", "[[stablecoins]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[cash-and-carry]]"]
---

# Huma Finance

**Huma Finance** (HUMA) is the protocol token of what it bills as the first "PayFi" network — a [[defi|DeFi]] system that finances global payments by giving payment institutions instant, 24/7 access to on-chain stablecoin liquidity. The protocol is built primarily on [[solana|Solana]] (with a [[binance|BNB Chain]] deployment) and underwrites real-world payment receivables such as cross-border settlements, card pre-funding, and trade finance.

Huma's core idea is "PayFi": rather than collateralizing loans with crypto, lenders supply [[stablecoins]] into pools that advance funds against short-duration, real-world payment receivables, earning yield as those receivables settle. It sits at the intersection of [[defi|DeFi]] and [[real-world-assets|real-world assets (RWA)]].

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | HUMA |
| **Chain** | [[solana]] (also [[binance|BNB Chain]]) |
| **Current Price** | $0.02419808 |
| **Market Cap** | $41.94M |
| **Market Cap Rank** | #510 |
| **24h Volume** | $9.59M |
| **24h Change** | +2.43% |
| **7d Change** | +3.40% |
| **Fully Diluted Valuation** | $241.98M |
| **All-Time High** | $0.115647 (2025-05-26) |
| **All-Time Low** | $0.01107715 (2026-02-26) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Trading backdrop: the broad crypto market sits in **extreme fear** ([[crypto-fear-and-greed-index|Crypto Fear & Greed Index]] ≈ 23) within an **established bear market** regime as of 2026-06-21. HUMA's mild positive 24h/7d move (+2.4% / +3.4%) is set against that risk-off tape. The token trades ~79% below its May 2025 ATH ($0.1156) but ~2.2x above its February 2026 ATL ($0.0111). Note the large gap between market cap ($41.9M) and FDV ($242M) — see Tokenomics for the dilution overhang this implies.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 1,733,333,333 HUMA |
| **Total Supply** | 10,000,000,000 HUMA |
| **Max Supply** | 10,000,000,000 HUMA |
| **Fully Diluted Valuation** | $241.98M |
| **Market Cap / FDV** | ~0.17 |

The low market-cap-to-FDV ratio (~0.17) means roughly 83% of the maximum supply is not yet circulating. This is a meaningful future-emission / dilution overhang typical of recently launched tokens, and a key consideration for holders during the current bear regime: even flat demand implies downward price pressure as locked supply vests. The ~5.8x gap between FDV ($242M) and market cap ($41.9M) is the single most important number for valuing HUMA — at full dilution the token would need ~6x the current network usage to justify today's price.

### Categories

Decentralized Finance (DeFi), BNB Chain Ecosystem, Payment Solutions, Binance Alpha Spotlight.

### Contract Addresses

| Chain | Address |
|---|---|
| [[solana|Solana]] | `HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw` |
| [[binance|BNB Chain]] | `0x92516e0ddf1ddbf7fab1b79cac26689fdc5ba8e6` |

---

## How & Where It Trades

### Spot venues (CEX)

| Exchange | Pair |
|---|---|
| [[binance|Binance]] | HUMA/USDT |
| Upbit | HUMA/BTC |
| Bitget | HUMA/USDT |
| KuCoin | HUMA/USDT |

HUMA spot liquidity is concentrated on major centralized venues. With ~$9.8M of 24h volume against a ~$41.8M market cap, daily turnover is roughly 23% of cap — reasonably liquid for a small-cap token.

### Protocol mechanics (PayFi receivables)

The protocol itself is not a trading venue in the order-book sense; its on-chain "market" is the financing of payment **receivables**:

1. **Liquidity providers** deposit [[stablecoins]] (e.g. USDC) into Huma pools.
2. The protocol advances those funds to vetted payment institutions / borrowers against short-duration receivables (the right to a near-term payment that is already in transit).
3. As receivables settle, principal returns to the pool and LPs earn yield plus, in some programs, HUMA incentives ("Feathers"/points).

Because the advances are backed by real-world payment flows rather than volatile crypto collateral, returns are framed as receivable-financing yield rather than crypto-native lending rates. The HUMA token is used for governance and protocol incentives.

---

## Use Case, Narrative & Category

Huma popularized the **"PayFi"** narrative — using on-chain [[stablecoins]] to pre-fund and accelerate real-world payments (cross-border remittances, card settlement, trade finance, DePIN financing). It is categorized as a [[defi|DeFi]] / [[real-world-assets|RWA]] payments protocol and benefits from the broader institutional-stablecoin and tokenized-credit narratives. Its inclusion in Binance Alpha Spotlight gave it retail distribution.

PayFi sits in the wider **RWA-credit** family: rather than tokenizing a static asset (bonds, real estate), it tokenizes a *cash-flow* — short-duration payment receivables that self-liquidate as the underlying payment settles. The duration is days to weeks, not years, which (in theory) limits credit and rate risk versus longer RWA-lending books.

---

## Peer Comparison — RWA Credit / Stablecoin Yield Protocols

| Protocol | Token | Collateral / yield source | Duration profile |
|---|---|---|---|
| **Huma Finance** | HUMA | Real-world payment receivables (PayFi) | Very short (days–weeks) |
| [[spark-2\|Spark]] | SPK | [[sky\|Sky]]/MakerDAO reserves → DeFi/CeFi/RWA allocation | Mixed; backed by stablecoin reserves |
| Centrifuge | CFG | Tokenized invoices, structured credit | Medium-term private credit |
| Goldfinch | GFI | Off-chain private credit (emerging markets) | Longer-duration uncollateralized loans |
| Maple Finance | SYRUP | Institutional under-collateralized lending | Medium-term |

Huma's distinguishing feature is the **payment-receivable** angle: very short duration, self-liquidating advances tied to payment rails, rather than multi-month private-credit loans. This narrows duration risk but concentrates exposure on payment-counterparty settlement reliability.

---

## Valuation Framing (qualitative)

- **FDV is the binding constraint:** market cap ~$41.9M but FDV ~$242M (MC/FDV ~0.17). The ~83% locked supply is the dominant valuation factor — HUMA is "cheap" on cap but expensive on FDV, and unlocks are a persistent headwind in a bear tape.
- **Cash-flow-backed, not speculative collateral:** unlike crypto-collateralized DeFi, PayFi yield is sourced from real payment flows, which (if receivables perform) gives a more defensible, less reflexive revenue base — but introduces off-chain credit/settlement risk.
- **Narrative optionality:** rides the institutional-stablecoin and [[real-world-assets|RWA]]/tokenized-credit themes; a re-rate depends on demonstrable receivable volume and credit performance, not just narrative.
- **Versus Spark:** both are stablecoin-yield plays with heavy locked supply, but Huma's value is in *originating* real-world receivables while [[spark-2|Spark]] *allocates* an existing reserve — different points on the RWA-credit value chain.

---

## Notable History

- Token reached an all-time high of **$0.1156** on 2025-05-26; the current price is ~79% below that ATH.
- All-time low of **$0.0111** was printed on 2026-02-26, during the same broad bear market that persists in mid-2026.
- Development is associated with the **00labs** GitHub organization.

> *Notable protocol events and verified news will be added through the wiki's source-ingestion workflow as relevant articles are processed.*

---

## Risks

- **Dilution / emissions:** ~83% of max supply is not yet circulating (MC/FDV ~0.17); future unlocks can pressure price.
- **Real-world credit risk:** PayFi yield depends on payment counterparties actually settling their receivables; defaults, fraud, or settlement delays can impair LP capital — a risk that crypto-native lending does not carry in the same form.
- **Regulatory risk:** financing real-world payments and using [[stablecoins]] for settlement intersects with money-transmission and securities regulation across jurisdictions.
- **Smart-contract risk:** funds are custodied in [[smart-contracts]] on [[solana]] / [[binance|BNB Chain]]; exploits or [[oracle-manipulation|oracle]] issues are possible.
- **Market regime:** with the [[crypto-fear-and-greed-index|Fear & Greed Index]] at ≈23 (extreme fear) in an established bear market, small-cap [[defi|DeFi]] tokens like HUMA are vulnerable to sharp liquidity-driven drawdowns.

---

## Related

- [[crypto-markets]]
- [[solana]]
- [[defi]]
- [[stablecoins]]
- [[real-world-assets]]
- [[spark-2]]
- [[smart-contracts]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko top-1000 markets data (`raw/data/crypto-loop/coingecko-markets.json`).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HUMA |
| **Market Cap Rank** | #534 |
| **Market Cap** | $37.99M |
| **Current Price** | $0.0219 |
| **Categories** | Decentralized Finance (DeFi), Payment Solutions, Binance Alpha Spotlight |
| **Website** | [https://huma.finance/](https://huma.finance/) |

---

## Overview

Huma Finance is the first PayFi network, powering the financing of global payments with instant access to liquidity - anywhere, anytime. 

Huma Finance enables global payment institutions to settle their payments 24/7 using stablecoins and liquidity on-chain. It powers settlements for a range of PayFi use cases such as cross-border payments, credit cards, trade finance, and enables novel solutions like DePiN financing.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.73B HUMA |
| **Total Supply** | 10.00B HUMA |
| **Max Supply** | 10.00B HUMA |
| **Fully Diluted Valuation** | $219.18M |
| **Market Cap / FDV Ratio** | 0.17 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1156 (2025-05-26) |
| **Current vs ATH** | -80.97% |
| **All-Time Low** | $0.0111 (2026-02-26) |
| **Current vs ATL** | +98.65% |
| **24h Change** | -0.29% |
| **7d Change** | -1.11% |
| **30d Change** | -11.20% |
| **1y Change** | -40.59% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `HUMA1821qVDKta3u2ovmfDQeW2fSQouSKE8fkF44wvGw` |
| Binance Smart Chain | `0x92516e0ddf1ddbf7fab1b79cac26689fdc5ba8e6` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HUMA/USDT | N/A |
| Upbit | HUMA/BTC | N/A |
| Bitget | HUMA/USDT | N/A |
| KuCoin | HUMA/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://huma.finance/](https://huma.finance/) |
| **Twitter** | [@humafinance](https://twitter.com/humafinance) |
| **Discord** | [https://discord.com/invite/aCDxmJqvE2](https://discord.com/invite/aCDxmJqvE2) |
| **GitHub** | [https://github.com/00labs](https://github.com/00labs) |
| **Whitepaper** | [https://docs.huma.finance/](https://docs.huma.finance/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7.58M |
| **Market Cap Rank** | #534 |
| **24h Range** | $0.0216 — $0.0223 |
| **CoinGecko Sentiment** | 0% positive |
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

HUMA is tradable on [[binance|Binance]] — spot (HUMA/USDT) plus a USD-margined [[perpetual-futures|perpetual]], which brings [[funding-rate|funding]], [[open-interest|open interest]], and [[liquidations|liquidation]] data into play. It is **not** listed on [[hyperliquid|Hyperliquid]], so Binance is effectively the primary leveraged venue for HUMA. This concentrates derivatives price discovery and funding on a single exchange: order-book depth and perp liquidity are thinner than for large caps, so leveraged sizing should stay modest, and stops/limit orders are preferable to market fills to avoid slippage. With spot liquidity spread across Binance, Upbit, Bitget, and KuCoin but the perp anchored on Binance, execution for basis/funding trades routes through the Binance spot+perp pair.

### Applicable strategies

- [[funding-rate-harvest]] — HUMA's Binance perp funding can run persistently one-sided on a small-cap RWA token; harvesting the funding while delta-hedged monetizes that skew.
- [[crowded-long-funding-fade]] — narrative-driven pops (PayFi/RWA, Binance Alpha) can crowd longs and push funding sharply positive, setting up a funding-financed fade.
- [[cash-and-carry]] — long Binance spot HUMA/USDT versus short the USD-M perp captures the basis when the perp trades rich to spot.
- [[liquidation-cascade-fade]] — thin single-venue perp depth means forced liquidations overshoot; fading the cascade after exhaustion targets the mean-revert bounce.
- [[oi-confirmed-trend]] — pairing Binance open-interest expansion with price direction filters out low-conviction, liquidation-driven moves on this low-float token.
- [[token-unlock-supply-event]] — with ~83% of max supply still locked (MC/FDV ~0.17), scheduled unlocks are recurring supply events tradable around the vesting calendar.

### Volatility & regime character

HUMA is a small-cap ([[altcoins|altcoin]], rank ~533) [[defi|DeFi]]/[[real-world-assets|RWA]] infrastructure token with high-beta behavior: it amplifies moves in [[bitcoin|BTC]]/[[ethereum|ETH]] on the downside and is reflexive to the PayFi/RWA-credit narrative. The very low float (MC/FDV ~0.17) makes price sensitive to marginal flow and to unlock-driven supply, so realized volatility is elevated relative to large caps. Correlation to majors is strong in risk-off phases (as in the current bear/extreme-fear tape) and looser during narrative-specific catalysts.

### Risk flags

- **Venue concentration:** Binance is the sole meaningful leveraged venue — no [[hyperliquid|Hyperliquid]] listing — so funding, OI, and liquidation dynamics are single-exchange dependent, raising basis and execution risk if Binance conditions shift.
- **Unlocks / emissions:** ~83% of max supply not yet circulating; vesting is a persistent dilution overhang and a recurring supply catalyst.
- **Narrative dependence:** valuation rides the PayFi/RWA-credit and institutional-stablecoin themes; re-rates and de-rates track narrative and demonstrable receivable volume more than fundamentals.
- **Liquidity / small-cap risk:** thin perp depth means slippage and gap risk on size; liquidation cascades can overshoot violently.
- **Regulatory:** financing real-world payments with [[stablecoins]] intersects with money-transmission and securities regimes across jurisdictions.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=HUMAUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=HUMAUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=HUMA` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=HUMA` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=HUMAUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=HUMAUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=HUMA"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[solana]]

---
