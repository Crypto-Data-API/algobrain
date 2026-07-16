---
title: "United Stables"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: review
tags: [crypto, stablecoins, defi]
aliases: ["U"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://u.tech/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-yield]]"]
---

# United Stables

**United Stables** (U) is a Stablecoins, USD Stablecoin, BNB Chain Ecosystem, Ethereum Ecosystem, Tron Ecosystem project. It ranks **#64** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | U |
| **Market Cap Rank** | #64 |
| **Market Cap** | $1.04B |
| **Current Price** | $0.9997 |
| **Categories** | Stablecoins, USD Stablecoin |
| **Website** | [https://u.tech/](https://u.tech/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.04B U |
| **Total Supply** | 1.04B U |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $1.04B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.01 (2026-02-05) |
| **Current vs ATH** | -0.78% |
| **All-Time Low** | $0.9682 (2025-12-21) |
| **Current vs ATL** | +3.28% |
| **24h Change** | +0.01% |
| **7d Change** | -0.06% |
| **30d Change** | -0.02% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0xce24439f2d9c6a2289f741120fe202248b666666` |
| Ethereum | `0xce24439f2d9c6a2289f741120fe202248b666666` |
| Tron | `TFNirp6PbqYE1ZTtWuCMUKJWLNZkoCoeFJ` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ETH/U | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://u.tech/](https://u.tech/) |
| **Twitter** | [@UTechStables](https://twitter.com/UTechStables) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $28.66M |
| **Market Cap Rank** | #64 |
| **24h Range** | $0.9978 — $1.00 |
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

United Stables (U) is a USD-pegged stablecoin traded on Binance. It is a PEG / cash-management instrument, NOT a directional asset — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. Because the primary listed pair is ETH/U on Binance rather than a deep U/USDT book, execution routes through the cross rather than a direct fiat-parity market, which widens effective spreads and makes size-in/size-out sensitive to the ETH leg. There is no meaningful case for directional leverage; leverage here is relevant only to carry and delta-neutral constructions where U is the cash/quote leg. Venue concentration on a single exchange means redemption and mint parity (issuer-side) — not on-exchange depth — is the real backstop for the peg, so sizing should assume thin secondary-market liquidity during stress and reserve headroom against having to exit a large position on-book.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — U has printed both above-peg ($1.01 ATH) and below-peg ($0.9682 ATL) excursions, so mean-reversion toward 1.00 after a depeg is the core edge for this instrument.
- [[stablecoin-pair-arbitrage]] — trade U against other USD stablecoins (e.g. USDT) when the ETH/U cross implies a deviation from parity versus a deeper stablecoin pair.
- [[stablecoin-yield]] — deploy idle U into lending/liquidity venues to earn on the cash-management leg while holding at par.
- [[mint-parity-arbitrage]] — when secondary-market U diverges from 1.00, arb against the issuer's mint/redeem parity to capture the spread back to peg.
- [[delta-neutral-yield-farming]] — use U as the stable quote/collateral leg in a hedged position to harvest yield without directional exposure.
- [[carry-trade]] — hold U as the funding/cash leg to capture rate differentials against higher-yielding assets.

### Volatility & regime character

Peg tightness is generally high: recent 24h range sat inside roughly $0.9978–$1.00 and 24h/7d/30d changes are within a few basis points of flat, consistent with a functioning USD peg. Historical excursions are modest but real — an ATL of $0.9682 (2025-12-21) marks the largest observed downside depeg, and an ATH of $1.01 (2026-02-05) marks a premium episode. Regime character is dominated by redemption mechanics and backing confidence rather than price momentum: in calm regimes U behaves as near-riskless cash, while stress regimes compress liquidity and open the depeg/arbitrage window. The backing model and redemption terms should be confirmed from primary issuer disclosures before sizing.

### Risk flags

- **Depeg risk** — U has traded below par (ATL $0.9682); a loss of parity is the primary trading risk and can gap on thin single-venue liquidity.
- **Reserve/backing transparency** — as a cash-management instrument, edge and safety depend on reserve composition and attestation quality; verify current backing disclosures rather than assuming full fiat reserves.
- **Redemption gating** — mint-parity and depeg-capture trades assume redemption is available at par; gating, delays, or eligibility limits can trap positions above or below peg.
- **Regulatory** — stablecoins face evolving oversight of issuance, reserves, and redemption; regulatory action can impair convertibility or venue availability.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=UUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=UUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=UUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=UUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
