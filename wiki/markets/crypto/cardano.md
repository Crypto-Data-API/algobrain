---
title: "Cardano"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, bitcoin, ethereum]
aliases: ["ADA"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://cardano.org/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[hyperliquid]]", "[[narrative-trading]]", "[[proof-of-stake]]", "[[staking]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[crypto-beta-rotation]]", "[[cash-and-carry]]"]
---

# Cardano

**Cardano** (ADA) is a blockchain platform built on academic research that enables smart contracts and decentralized applications while using significantly less energy than traditional cryptocurrencies like Bitcoin. 

What sets Cardano apart is its methodical, research-driven approach — every major feature is peer-reviewed by scientists and cryptographers before being added to the network. Since the January 2025 Plomin hard fork it runs fully on-chain governance. For traders, ADA is a benchmark "old L1" — a deep-liquidity, high-retail-ownership asset that trades on rotation flows and US ETF catalysts more than on ecosystem usage.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #18 |
| **Price** | $0.162881 |
| **Market Cap** | $6.06 billion |
| **24h Volume** | $242.03 million |
| **24h Change** | +1.76% |
| **7d Change** | -5.94% |
| **Circulating Supply** | 37,212,521,229 ADA |
| **Total Supply** | 45,000,000,000 ADA |
| **Max Supply** | 45,000,000,000 ADA (hard cap) |
| **Fully Diluted Valuation** | $7.33 billion (MC/FDV ≈ 0.83) |
| **All-Time High** | $3.09 (2021-09-02) — currently -94.7% |
| **All-Time Low** | $0.01925 (2020-03-13) — currently +746% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** [[crypto-market-sentiment|Fear & Greed]] = **22 (Extreme Fear)**; **Established Bear Market**. ADA has been one of the cycle's deepest large-cap underperformers — now **~95% below its Sept 2021 ATH** and down on the week (-5.9% 7d), having slipped from rank #14 to **#18**. This makes it a perennial candidate for "old L1 catch-up" rotation trades, but also a value trap until a genuine catalyst (the spot ETF) materializes.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ADA |
| **Market Cap Rank** | #18 |
| **Market Cap** | $6.06B (2026-06-20) |
| **Founder** | Charles Hoskinson (Input Output Global / IOG) |
| **Sector** | Layer 1 smart-contract platform (Ouroboros [[proof-of-stake]]), on-chain governance since Jan 2025 |
| **Supply** | 45B ADA hard cap; ~37.2B circulating (MC/FDV ≈ 0.83, remainder emitted via staking rewards) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Cardano Ecosystem, Proof of Stake (PoS), GMCI Layer 1 Index, GMCI 30 Index, GMCI Index, Made in USA, Coinbase 50 Index |
| **Website** | [https://cardano.org/](https://cardano.org/) |

---

## Overview

Cardano is a blockchain platform built on academic research that enables smart contracts and decentralized applications while using significantly less energy than traditional cryptocurrencies like Bitcoin. 

What sets Cardano apart is its methodical, research-driven approach — every major feature is peer-reviewed by scientists and cryptographers before being added to the network. This careful process aims to create a more secure and stable foundation compared to platforms that prioritize speed over thorough testing. The platform's native cryptocurrency, ADA, is used to send money, pay transaction fees, and participate in network governance.

Cardano uses a proof-of-stake system to process transactions, which works differently from Bitcoin's mining approach. Instead of competing to solve complex puzzles, users can "stake" their ADA — essentially locking it up temporarily — to become validators who verify transactions. The system selects validators based on how much ADA they've staked and for how long, then rewards them with additional ADA for their participation. This approach uses far less energy than traditional mining while keeping the network secure. The platform also features a two-layer design that separates basic payment transactions from smart contract operations, allowing each function to be optimized independently for better performance. 

ADA holders can earn staking rewards by locking up their tokens to help secure the network, vote on proposed changes to the platform, and use ADA for international money transfers with lower fees than traditional services.

Cardano was founded in 2017 by Charles Hoskinson, who previously helped create Ethereum. Hoskinson leads Input Output Global (IOG), the technology company that builds and maintains Cardano's core software. The ecosystem operates through three organizations: IOG handles technical development, the Cardano Foundation promotes adoption and standardization, and Emurgo helps businesses integrate blockchain t...

---

## Technology & Consensus

Cardano runs **Ouroboros**, a peer-reviewed [[proof-of-stake]] protocol — the first PoS protocol with formal security proofs. Time is divided into **epochs** and **slots**; slot leaders (selected proportional to stake) produce blocks. Validation is performed by ~**stake pools (SPOs)** that delegators back with their ADA.

Distinctive design choices:

- **eUTXO model:** Cardano extends Bitcoin's UTXO accounting (rather than Ethereum's account model) with an *extended* UTXO that supports smart contracts. This gives deterministic fee/validation (you know if a tx will succeed before submitting) but makes high-contention DeFi (shared-state AMMs) harder to engineer than on account-based chains.
- **Plutus / Aiken:** smart contracts are written in Plutus (Haskell-based) or the newer Aiken language, reflecting Cardano's functional-programming, formal-methods ethos.
- **Liquid (non-custodial) staking:** delegating ADA to a stake pool never locks or transfers the tokens — holders keep full custody and liquidity while earning rewards. This dampens forced sell pressure but also means staked ADA does not create a hard float lock-up.
- **Eras roadmap:** Byron → Shelley (decentralized staking) → Goguen (smart contracts) → Basho (scaling: Hydra L2, input endorsers) → Voltaire (on-chain governance, completed via the **Plomin** fork).

---

## Tokenomics & Supply Schedule

| Metric | Value |
|---|---|
| **Circulating Supply** | 37.21B ADA |
| **Total Supply** | 45.00B ADA |
| **Max Supply** | 45.00B ADA (hard cap) |
| **Fully Diluted Valuation** | $7.33B |
| **Market Cap / FDV** | ~0.83 |

- **Hard cap of 45B ADA** — unlike [[ethereum|ETH]]/[[solana|SOL]], ADA has a fixed maximum supply, with the un-circulating remainder released as **staking rewards** drawn from a decaying **reserve** plus transaction fees. This produces a predictable, disinflationary emission.
- **MC/FDV ≈ 0.83** — residual emission drag (the gap to fully-diluted) is modest; there are no large venture unlock cliffs, but staking rewards represent a steady, if slow, supply increase.
- **On-chain treasury** — a portion of rewards and fees funds a multi-billion-ADA treasury, now controlled by on-chain governance (dReps). Treasury disbursements are effective supply events traders watch.
- **High staking ratio** — historically ~60%+ of ADA is delegated via liquid (non-locking) staking, supporting price but muting staking-driven float squeezes.

---

## Ecosystem & Use Cases

Cardano's DeFi/app ecosystem is **smaller than its market cap and brand suggest** — a long-standing critique. Notable components:

- **DEXs / DeFi:** Minswap, SundaeSwap (AMMs); Liqwid (lending); Indigo (synthetics); Djed (algorithmic-ish stablecoin).
- **Scaling:** **Hydra** (state-channel L2 for high throughput) and **Leios** (input-endorser research for higher base-layer throughput).
- **Interop:** Bitcoin-DeFi interoperability and partner-chain initiatives are recurring IOG roadmap themes.
- **Governance:** binding on-chain constitutional governance (dReps vote on treasury and hard forks) — a genuine differentiator among major L1s.

ADA's practical trading thesis is therefore less "ecosystem usage" and more **brand + deep retail ownership + ETF optionality + governance treasury**.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.09 (2021-09-02) — currently -94.7% |
| **All-Time Low** | $0.01925 (2020-03-13) — currently +746% |
| **24h Change** | +1.76% |
| **7d Change** | -5.94% |

> *Price figures as of 2026-06-20 (CoinGecko).*

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ADA/USDT | N/A |
| Kraken | ADA/USD | N/A |
| Bitget | ADA/USDT | N/A |
| KuCoin | ADA/USDT | N/A |
| Crypto.com Exchange | ADA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | ADA-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://cardano.org/](https://cardano.org/) |
| **Twitter** | [@Cardano_CF](https://twitter.com/Cardano_CF) |
| **Reddit** | [https://www.reddit.com/r/cardano](https://www.reddit.com/r/cardano) |
| **Telegram** | [Cardano](https://t.me/Cardano) (15,628 members) |
| **GitHub** | [https://github.com/input-output-hk/cardano-sl](https://github.com/input-output-hk/cardano-sl) |
| **Whitepaper** | [https://docs.cardano.org/introduction](https://docs.cardano.org/introduction) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,757 |
| **GitHub Forks** | 643 |
| **Pull Requests Merged** | 1,706 |
| **Contributors** | 80 |

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **Rank** | #18 |
| **24h Volume** | $242.03M (2026-06-20) |
| **Liquidity** | Top-tier spot ([[binance]], [[coinbase]], Kraken, Bitget, KuCoin, Crypto.com) |
| **Volatility / beta** | Moderate-to-high beta; chronic underperformer in alt seasons |
| **Primary spot pairs** | ADA/USDT ([[binance]]), ADA/USD ([[coinbase]], Kraken) |
| **Primary perp** | ADA-PERP ([[hyperliquid]]) + all major CEX perp venues |
| **ETFs** | US futures ETFs live; **spot ETF (GADA, Grayscale)** is the standing catalyst |

ADA [[funding-rate|funding]] and [[open-interest]] tend to spike around ETF-headline events rather than ecosystem usage. The **GADA spot ETF** approval is the single biggest discrete catalyst; in the current Extreme-Fear regime, alt-ETF flows are typically muted. *(Flow magnitudes vary daily and are not quoted here to avoid stale figures.)*

---

## On-chain & Valuation Frameworks

| Metric | What it measures | Trading use |
|---|---|---|
| **Staking ratio** | % of ADA delegated to pools | Liquid-float & holder-conviction proxy |
| **dRep / treasury votes** | Governance disbursement decisions | Effective supply events |
| **DeFi TVL** | On-chain economic activity | Tests the "usage vs brand" thesis (historically weak) |
| **MC/FDV & emission** | Residual staking-reward dilution | Supply-pressure input |
| **ADA/BTC & ADA/ETH** | Relative strength vs majors | Rotation timing for the "old L1" basket |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events (2025–2026)

- **2025-01-29 — Plomin hard fork.** Completed the Chang/Voltaire governance sequence: full on-chain governance went live, with Delegate Representatives (dReps) voting on treasury spending and future hard forks on behalf of ADA holders. Cardano became one of the few major L1s with binding on-chain constitutional governance.
- **2025-02-10** — **Grayscale filed** to convert its Cardano Trust into a spot ADA ETF (ticker **GADA**, NYSE Arca); Grayscale also allocated 20% of one of its diversified crypto funds to ADA.
- **October 2025** — SEC action on GADA was **delayed** (deadline lapsed amid the US government shutdown); Cardano futures ETFs were already live, and Bloomberg analysts raised spot-approval odds under the SEC's new generic listing standards.
- **November 2025** — Cardano Foundation CEO Frederik Gregaard signaled US regulatory clarity on an ADA ETF was expected within ~30 days; spot ETF conversion remained in progress into 2026.
- **Price context:** ADA spent 2025–early 2026 as a relative underperformer (-55% y/y at the April 2026 snapshot, ~92% below the Sept 2021 ATH of $3.09), making it a frequent candidate for "old L1 catch-up" rotation trades.

---

## Trading Relevance

- **Where it trades:** top-tier spot liquidity (Binance, Coinbase, Kraken, Bitget, KuCoin, Crypto.com; ~$400M+ daily volume) and perps as **ADA-PERP** on [[hyperliquid]] and all major derivative venues. US futures ETFs exist; spot ETF (GADA) is the standing catalyst.
- **Narrative basket:** "old L1 / dino coin" rotation basket alongside XRP, LTC, DOT — these names move together when capital rotates out of [[bitcoin]]/[[ethereum]] dominance into legacy large caps. See [[narrative-trading]].
- **What drives it:** ETF headlines, governance/treasury votes (the on-chain treasury holds billions of ADA — disbursement decisions are supply events), IOG roadmap items (Hydra L2, Leios scaling research, Bitcoin-DeFi interop), and Charles Hoskinson headlines.
- **Structural notes:** ~60%+ of supply is staked via liquid (non-locking) delegation, dampening sell pressure but also muting staking-driven float squeezes; MC/FDV 0.82 means residual emission drag vs fully-diluted peers.

---

## Competitive Positioning

ADA competes with other smart-contract L1s but, in practice, trades as a member of the **"old L1 / dino coin" rotation basket** (with XRP, LTC, [[polkadot|DOT]]) rather than on head-to-head usage with [[ethereum|ETH]] or [[solana|SOL]].

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **Cardano (ADA)** | #18 | $6.1B | Ouroboros [[proof-of-stake\|PoS]] | Research-driven L1; ETF + governance optionality |
| [[bitcoin\|Bitcoin (BTC)]] | #1 | $1.27T | [[proof-of-work]] | Digital gold |
| [[ethereum\|Ethereum (ETH)]] | #2 | $208B | [[proof-of-stake]] | Dominant smart-contract ecosystem |
| [[solana\|Solana (SOL)]] | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | High-throughput L1 |
| [[polkadot\|Polkadot (DOT)]] | #51 | $1.63B | NPoS | Layer-0 interop; same rotation basket |

> Peer market data as of 2026-06-20 (CoinGecko). ADA's persistent underperformance vs ETH/SOL is the bear case; its deep retail base and ETF optionality is the bull case. See [[narrative-trading]].

---

## Regulatory

- **ETF status:** **Grayscale** filed to convert its Cardano Trust into a spot ETF (**GADA**, NYSE Arca); the SEC decision was delayed amid the 2025 US government shutdown, with approval odds rising under the SEC's new generic listing standards. Spot conversion remained in progress into 2026.
- **Securities question:** ADA was named in past SEC enforcement framing as an alleged security; ETF progress signals easing of that overhang under the newer regime.
- **Made-in-USA framing:** IOG's US base and Hoskinson's regulatory engagement are part of ADA's "compliant L1" positioning.

---

## Risks

- **Usage vs valuation gap** — DeFi TVL and on-chain activity remain modest relative to ADA's market cap and brand; a chronic value-trap risk.
- **Underperformance/rotation** — ADA has lagged ETH/SOL for multiple cycles; "catch-up" trades repeatedly fail to sustain.
- **ETF dependence** — much of the bull case hinges on the GADA spot-ETF catalyst landing.
- **Emission drag** — ongoing staking-reward issuance (MC/FDV ≈ 0.83) is a slow supply headwind.
- **Key-person/governance** — heavy association with Charles Hoskinson; on-chain governance is new and untested at scale.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. ADA is ~95% below its ATH and remains in a deep drawdown in the current Extreme-Fear / bear regime.

---

## Trading Profile

### Venues & liquidity

ADA is one of the deepest, most liquid two-venue alt perp markets. It trades on **both [[binance]]** (ADA/USDT spot plus a USD-margined ADA perpetual) **and [[hyperliquid]]** (ADA-PERP, listed with leverage up to ~40–50x), alongside every other major CEX derivatives venue. Spot depth is top-tier across Binance, Coinbase, Kraken, Bitget, KuCoin and Crypto.com, so slippage on standard clip sizes is low and the market absorbs size well.

- **Leverage:** ~40–50x on Hyperliquid ADA-PERP; USD-margined perp on Binance for CEX-side exposure.
- **Execution:** The dual-venue structure (a deep on-chain CLOB on Hyperliquid + the deepest CEX book on Binance) gives redundant liquidity — you can split fills, work larger orders, and route to whichever venue shows tighter spreads. It also enables the whole family of cross-venue and spot-vs-perp trades (funding capture, basis, HL-vs-CEX divergence) with genuine size.
- **Sizing:** Because both books are deep, ADA supports meaningfully larger positions than thin single-venue alts; funding and liquidation dynamics are visible on both venues, so risk can be sized against real depth rather than a single fragile book.

### Applicable strategies

- [[cash-and-carry]] — deep two-venue spot (Binance) + perp (HL/Binance) markets make long-spot / short-perp carry clean to construct and unwind on ADA.
- [[funding-rate-harvest]] — ADA funding spikes hard around ETF headlines and rotation flushes, offering recurring premium to farm while delta-hedged.
- [[hl-vs-cex-funding-divergence]] — ADA runs live perps on both Hyperliquid and Binance, so funding can dislocate between venues and be arbitraged.
- [[crypto-beta-rotation]] — ADA is the archetypal "old L1" rotation name; it moves as a high-beta basket member versus BTC/ETH dominance shifts.
- [[narrative-trading]] — ETF (GADA), governance/treasury votes and Hoskinson headlines drive discrete ADA moves more than ecosystem usage.
- [[liquidation-cascade-fade]] — as a heavily-levered, deep-liquidity perp, ADA sees flushes that overshoot and mean-revert, faded against visible book depth.

### Volatility & regime character

ADA is a **high-beta large-cap altcoin / "old L1" infra token** — not a memecoin and not a stablecoin. It carries a high positive beta to [[bitcoin|BTC]] and [[ethereum|ETH]]: it tends to underperform on the way up (a chronic alt-season laggard) yet still sells off hard in risk-off, giving it downside-skewed beta in bear regimes. Idiosyncratic moves cluster around discrete catalysts (ETF headlines, governance/treasury votes, roadmap items) rather than steady on-chain usage, so realized volatility is bursty — long quiet drifts punctuated by sharp headline-driven repricings. It trades in tandem with the DOT/XRP/LTC "dino coin" rotation cluster.

### Risk flags

- **Venue/narrative concentration:** Price action is dominated by a single discrete catalyst (the GADA spot-ETF decision) and Hoskinson/IOG headlines; catalyst dependence makes gaps and headline whipsaws common.
- **Perp funding dislocations:** Funding can spike and flip sharply around ETF news and rotation flushes, and can diverge between Hyperliquid and Binance — a risk to naive one-venue carry and a source of stop-outs.
- **Liquidation cascades:** High available leverage on a deep perp book means crowded positioning unwinds violently; cascades overshoot both directions.
- **Emission/supply drag:** Ongoing staking-reward issuance (MC/FDV ≈ 0.83) and on-chain treasury disbursements are slow but real supply-side headwinds.
- **Regulatory overhang:** ADA's past securities framing has eased under the newer regime but remains a tail risk tied to ETF and enforcement developments.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=ADA` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=ADA` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=ADA&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=ADA&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=ADA"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]] / [[solana]] — smart-contract L1 peers
- [[bitcoin]] — macro anchor
- [[polkadot]] — same "old L1" rotation basket
- [[proof-of-stake]] / [[staking]] — consensus and yield
- [[hyperliquid]] / [[funding-rate]] / [[open-interest]] — derivatives venue & toolkit
- [[narrative-trading]] — the rotation-basket framework

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- CoinDesk: "Cardano's Plomin Hard Fork Goes Live, Ushering in On-Chain Governance" (2025-01-29) — https://www.coindesk.com/tech/2025/01/29/cardano-s-plomin-hard-fork-goes-live-ushering-in-on-chain-governance
- Cardano.org: "Chang upgrade completed — Plomin hard fork achieved!" (2025-01-30) — https://cardano.org/news/2025-01-30-chang-upgrade-completed/
- SEC EDGAR: Grayscale Cardano Trust S-1 (GADA) — https://www.sec.gov/Archives/edgar/data/2083106/000208310625000004/gada-20250829.htm
- The Block: Grayscale Cardano Trust ETF (GADA) live status — https://www.theblock.co/other-etf-live-chart/370988/grayscale-cardano-trust-etf-gada
- CoinEdition: "Grayscale Cardano ETF (GADA) Approval Delayed by Shutdown" (Oct 2025) — https://coinedition.com/cardano-etf-delay-grayscale-fast-track-gada/
- Verified via Perplexity (sonar) + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 37.28B ADA |
| **Total Supply** | 45.00B ADA |
| **Max Supply** | 45.00B ADA |
| **Fully Diluted Valuation** | $7.30B |
| **Market Cap / FDV Ratio** | 0.83 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $298.58M |
| **Market Cap Rank** | #20 |
| **24h Range** | $0.1613 — $0.1683 |
| **CoinGecko Sentiment** | 81% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
