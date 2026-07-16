---
title: "First Digital USD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, stablecoins, defi]
aliases: ["FDUSD", "First Digital Dollar"]
entity_type: protocol
founded: 2023
headquarters: "Hong Kong (issuer: First Digital Trust / FD121 Limited)"
website: "https://firstdigitallabs.com/"
related: ["[[binance]]", "[[crypto-markets]]", "[[ethereum]]", "[[stablecoin-depegs]]", "[[stablecoins]]", "[[tron]]", "[[usdc]]", "[[stablecoin-depeg-profit-capture]]", "[[stablecoin-pair-arbitrage]]", "[[mint-parity-arbitrage]]"]
---

# First Digital USD

**First Digital USD** (FDUSD) is a fiat-backed USD [[stablecoin]] launched in June 2023 by Hong Kong's First Digital group (issuer FD121 Limited, reserves custodied by First Digital Trust), deployed natively on [[ethereum|Ethereum]] and BNB Chain, which rose to a >$2B supply almost entirely on the back of [[binance|Binance]] zero-fee trading promotions. It is now best known to traders as the subject of one of the defining [[stablecoin-depegs|stablecoin depeg]] events of 2025: Justin Sun's April 2025 insolvency allegations against First Digital Trust knocked FDUSD to ~$0.87 intraday, and although the peg recovered within days, supply collapsed roughly 80% — from ~$2B to ~$350M by mid-2026.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $0.9984 (essentially on peg) |
| **Market cap** | $351.96M |
| **Market-cap rank** | #127 |
| **24h volume** | $37.84M (~11% of float turning over daily — Binance pair flow) |
| **Circulating supply** | 352.52M FDUSD |
| **Total supply** | 352.52M FDUSD |
| **Max supply** | None (mint/burn vs. fiat) |
| **24h change** | +0.04% |
| **7d change** | +0.06% |
| **All-time high** | $1.15 (2025-02-03, illiquid wick) — currently −13.3% |
| **All-time low** | $0.9404 (2024-12-05) — currently +6.2% |

*Macro backdrop: [[crypto-fear-and-greed-index|Fear & Greed]] 23 ("Established Bear Market"). For a $1-pegged stablecoin this is irrelevant to NAV — FDUSD trades flat regardless of risk sentiment — but the bear tape, thinner Binance promo activity, and migration to [[usdc|USDC]]/USDT all weigh on FDUSD float.*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FDUSD |
| **Type** | Fiat-backed USD stablecoin (1:1, cash and cash equivalents, bankruptcy-remote trust structure) |
| **Issuer** | FD121 Limited / First Digital Trust (Hong Kong, registered trust company; First Digital founded 2019) |
| **Backing** | Cash and cash equivalents (incl. short-term [[treasury-bills|US T-bills]]), held in bankruptcy-remote segregated trust accounts; redeemable 1:1 for USD |
| **Supply** | ~352M FDUSD (2026-06-20) — down from ~$2.04B in February 2025, an ~83% contraction post-depeg |
| **Rank** | #127 by market cap (2026-06-20); formerly a top-4 stablecoin at peak |
| **Chains** | [[ethereum|Ethereum]] (native), BNB Chain, Solana, Sui, TON, Arbitrum |
| **Primary venue** | [[binance|Binance]] (BTC/FDUSD and other zero-fee pairs) |
| **Website** | [https://firstdigitallabs.com/](https://firstdigitallabs.com/) |

---

## Overview

First Digital USD (FDUSD) aims to combine the stability of cash reserves with blockchain settlement efficiency. Key design claims from the issuer:

- **Redeemable 1:1**: backed by high-quality reserves — cash and cash equivalents, including short-term [[treasury-bills|US Treasury bills]] — with holders able to redeem FDUSD for US dollars at par.
- **Bankruptcy remote**: reserves held in segregated accounts at a registered trust company (First Digital Trust), separated from the issuer's operational accounts.
- **Multichain**: deployed on [[ethereum|Ethereum]], BNB Chain, Solana, Sui, TON and Arbitrum.
- **Low fees / Binance-native flow**: most utility has come from [[binance|Binance]]'s zero-fee spot promotions, which made FDUSD pairs (notably BTC/FDUSD) among the highest-volume spot pairs in crypto during 2024-2025.

Established in 2019, First Digital is a Hong Kong-based trust and custody group bridging traditional and digital finance. Its February 2025 attestation reported about **$2.051B in reserves backing ~$2.042B FDUSD** outstanding. (Source: First Digital reserve report via Blockworks, 2025-02.)

### Reserves, attestation & peg mechanics

FDUSD is a pure fiat-collateralized stablecoin — there is no algorithmic or crypto-collateral component. Reserves are intended to be 100% cash and cash equivalents (US T-bills, overnight repo, bank deposits) custodied at First Digital Trust, with periodic third-party attestations published by the issuer. The peg is enforced by **arbitrage against par redemption**: authorized participants mint FDUSD by depositing USD and burn it to redeem USD, so any persistent discount/premium is a redemption-cost arbitrage. The April 2025 event (below) is the canonical case where that mechanism was tested by a *credibility* shock rather than a reserve-quality shock — redemptions cleared at par throughout, which is why the price snapped back even as float permanently shrank.

---

## The April 2025 Depeg (key event)

- **2025-04-02**: TRON founder Justin Sun publicly alleged that **First Digital Trust was insolvent**, amid a dispute over ~$456M of TUSD reserves that First Digital had administered. FDUSD depegged, trading as low as **~$0.87-0.91** intraday. (Sources: Blockworks; BeInCrypto; CryptoSlate, April 2025.)
- First Digital stated the dispute concerned **TUSD, not FDUSD**, called Sun's claims a "smear campaign," affirmed FDUSD remained fully backed and redeemable, and **processed ~$26M of redemptions** through the episode while announcing legal action for defamation. (Sources: Cointelegraph via TradingView; CryptoSlate.)
- The peg recovered to ~$1.00 within days, but trust damage was lasting: **supply fell from ~$2B to roughly $350M over the following year** (2026-06-20: ~352.5M float, rank #127), as Binance broadened zero-fee promotions to other stablecoins and market share shifted to [[usdc|USDC]] and USDT.
- The episode is catalogued in [[stablecoin-depegs]] as a template for "issuer-credibility" depegs (vs. reserve-asset depegs like USDC/SVB March 2023): price recovered fast, but float never did.

---

## Tokenomics

See the **Market Data** block above for the single authoritative price/supply/volume snapshot (2026-06-20). Structural notes:

- **Supply mechanics**: no max supply; FDUSD is minted against USD deposits and burned on redemption, so float is a direct read on net Binance promotional demand ([[stablecoin-supply]]).
- **Peg performance**: ATH $1.15 (2025-02-03, illiquid wick), ATL $0.9404 (2024-12-05); the April 2025 depeg traded as low as ~$0.87 on some venues before recovering.
- **Volume/float ratio**: ~11% of the ~$352M float turns over per day, far higher than a typical stablecoin of this size — a residue of FDUSD's role as Binance execution plumbing.

### Peer comparison — major fiat-backed USD stablecoins

| Stablecoin | Issuer | Mcap (2026-06-20) | Yield to holder | Key differentiator |
|---|---|---|---|---|
| USDT (Tether) | Tether | ~$170B (largest) | None | Deepest liquidity, offshore |
| [[usdc|USDC]] | [[circle|Circle]] | tens of $B | None | Most regulated US-facing |
| [[global-dollar|USDG]] | [[paxos|Paxos]] | $2.81B (#33) | Shared with distributors | Yield-sharing network model |
| **FDUSD** | First Digital (FD121) | **$351.96M (#127)** | None | Binance zero-fee pair plumbing |

> Unlike yield-bearing tokenized-Treasury products ([[ousg|OUSG]], [[ondo-us-dollar-yield|USDY]], [[hashnote-usyc|USYC]]), FDUSD passes **no yield** to holders — it is a pure payment/settlement stablecoin. See [[stablecoins]] for the full taxonomy.

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc5f0f7b66764f6ec8c8dff7ba683102295e16409` |
| Sui | `0xf16e6b723f242ec745dfd7634ad072c42d5c1d9ac9d62a39c381303eaa57693a::fdusd::FDUSD` |
| The Open Network | `EQD0Evpk4timFOHmy4Sv3l_KEUXlM-dN1_KhroTCfB2wkO89` |
| Solana | `9zNQRsGLjNKwCUU5Gq5LR8beUCPzQMVMqKAi3SSZh54u` |
| Binance Smart Chain | `0xc5f0f7b66764f6ec8c8dff7ba683102295e16409` |
| Arbitrum One | `0x93c9932e4afa59201f0b5e63f7d816516f1669fe` |

---

## Exchange Listings

| Exchange | Pair | Notes |
|---|---|---|
| [[binance|Binance]] | BTC/FDUSD (+ other FDUSD quote pairs) | Historically zero-fee promo pairs; the core of FDUSD demand |
| Orca (Solana) | FDUSD/USDC | Spot DEX |

---

## Trading Relevance

- **Depeg playbook reference**: April 2025 FDUSD is the canonical recent example of an allegation-driven depeg — buyable at $0.87-0.93 *if* you could verify reserves were genuinely unaffected (they were; redemptions cleared at par). Compare USDC/SVB 2023. See [[stablecoin-depegs]].
- **Binance flow signal**: FDUSD supply is effectively a gauge of Binance promotional flow ([[stablecoin-supply]]). The 80% supply contraction post-depeg shows how quickly promo-driven stablecoin float migrates; FDUSD pairs can carry small persistent basis vs USDT pairs that arb bots harvest.
- **Counterparty awareness**: any strategy holding FDUSD inventory (e.g., for zero-fee spot execution on Binance) carries issuer/trust jurisdictional risk (Hong Kong trust regime, ongoing Sun-First Digital litigation). Position accordingly — it is execution plumbing, not a treasury asset.
- **Regulatory backdrop**: Hong Kong's stablecoin licensing regime (Stablecoins Ordinance, effective August 2025) is the key structural watch item for the issuer's status.

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://firstdigitallabs.com/](https://firstdigitallabs.com/) |
| **Twitter** | [@FDLabsHQ](https://twitter.com/FDLabsHQ) |
| **Whitepaper** | [https://firstdigitallabs.com/workspace/uploads/FDUSD-Whitepaper-25216064ca0cc8.pdf](https://firstdigitallabs.com/workspace/uploads/FDUSD-Whitepaper-25216064ca0cc8.pdf) |

---

## Related

- [[stablecoins]]
- [[stablecoin-depegs]]
- [[stablecoin-supply]]
- [[binance]]
- [[usdc]]
- [[tron]] (Justin Sun)
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (supply/market data baseline)
- Blockworks — "FDUSD depegs after Justin Sun insolvency claims" (2025-04) — https://blockworks.com/news/fdusd-depeg-sun-justin-insolvency-stablecoin
- BeInCrypto — "Justin Sun stablecoin FDUSD Binance depeg" (2025-04) — https://beincrypto.com/justin-sun-stablecoin-fdusd-binance-depeg/
- Cointelegraph (via TradingView) — "First Digital redeems $26M after FDUSD depeg, dismisses Sun insolvency claims" — https://www.tradingview.com/news/cointelegraph:2fda99a48094b:0-first-digital-redeems-26m-after-fdusd-depeg-dismisses-sun-insolvency-claims/
- CryptoSlate — "FDUSD issuer refutes Justin Sun's insolvency allegations, calls it a smear campaign" — https://cryptoslate.com/fdusd-issuer-refutes-justin-suns-insolvency-allegations-calls-it-a-smear-campaign/
- First Digital whitepaper — https://firstdigitallabs.com/
- Perplexity sonar verification (FDUSD depeg timeline, Feb 2025 reserve figures), 2026-06-10.

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.15 (2025-02-03) |
| **Current vs ATH** | -13.40% |
| **All-Time Low** | $0.9404 (2024-12-05) |
| **Current vs ATL** | +6.02% |
| **24h Change** | -0.02% |
| **7d Change** | -0.00% |
| **30d Change** | -0.13% |
| **1y Change** | -0.10% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $87.19M |
| **Market Cap Rank** | #122 |
| **24h Range** | $0.9956 — $0.9983 |
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

FDUSD is a USD-pegged stablecoin traded almost exclusively on [[binance|Binance]]. It is a PEG / cash-management instrument, NOT a directional asset — the profile is about peg stability, backing/reserves, depeg risk, and yield/arbitrage, not momentum. Liquidity is heavily concentrated in Binance FDUSD-quote pairs (notably BTC/FDUSD), a legacy of zero-fee spot promotions, with only thin secondary DEX depth (e.g. Orca FDUSD/USDC on Solana). Because depth is single-venue, execution and sizing hinge on Binance order-book conditions: away from Binance, spreads widen sharply and large redemptions must route through the issuer's mint/burn at par. Leverage is inappropriate for a par-pegged instrument — the only meaningful moves are small basis deviations and depeg events, so sizing is governed by redemption-cost basis and counterparty exposure rather than volatility targeting.

### Applicable strategies

- [[stablecoin-depeg-profit-capture]] — FDUSD's April 2025 allegation-driven drop to ~$0.87 is the canonical buy-the-depeg setup where reserves cleared at par and the peg snapped back within days.
- [[stablecoin-pair-arbitrage]] — FDUSD carries a small persistent basis versus USDT/USDC on Binance pairs that arb flow harvests, especially across BTC/FDUSD versus BTC/USDT.
- [[mint-parity-arbitrage]] — authorized-participant mint (deposit USD) and burn (redeem USD) enforce par, so secondary-market discount/premium is a redemption-cost arbitrage against the issuer.
- [[synthetic-stablecoin-depeg-arbitrage]] — a credibility shock like the Sun insolvency claim lets traders express depeg-vs-par views synthetically while redemptions remain clearing at par.
- [[stablecoin-yield]] — FDUSD passes no native yield, so any carry must be sourced externally via lending/LP venues, making yield capture strategy-dependent rather than embedded.

### Volatility & regime character

Qualitatively, FDUSD trades flat at ~$1.00 in normal regimes with very tight peg deviation, insensitive to broad crypto risk sentiment. Its defining historical stress is the April 2025 depeg to ~$0.87 intraday, driven by issuer-credibility allegations (a TUSD-reserve dispute) rather than a reserve-asset failure — the reason price recovered quickly while float did not. The backing model is pure fiat-collateralized (100% cash and cash equivalents including short-term T-bills, in a bankruptcy-remote trust), with no algorithmic or crypto-collateral component. Redemption mechanics are 1:1 mint/burn against USD for authorized participants, which is what caps sustained premium/discount to redemption cost.

### Risk flags

- **Depeg risk** — thin single-venue liquidity means a credibility or reserve shock can produce sharp intraday deviations (as in April 2025) before par arbitrage restores the peg.
- **Reserve/backing transparency** — reliance on periodic third-party attestations of First Digital Trust reserves; attestation timing and disclosure quality are ongoing watch items.
- **Redemption gating** — par redemption is available only to authorized participants and depends on issuer operational continuity; retail exit runs through Binance market depth.
- **Regulatory** — Hong Kong trust-jurisdiction exposure and the Stablecoins Ordinance (effective August 2025) regime, plus ongoing Sun-First Digital litigation, are structural watch items.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for peg monitoring (auth via `X-API-Key`). Watch for depeg events.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=FDUSDUSDT` — current price (peg deviation vs 1.00)
- `GET /api/v1/market-data/ticker/24hr?symbol=FDUSDUSDT` — 24h range (intraday peg stress)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=FDUSDUSDT&interval=1h&limit=1000` — peg history / past depegs
- `GET /api/v1/backtesting/klines` — deep archive for depeg backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/ticker/price?symbol=FDUSDUSDT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
