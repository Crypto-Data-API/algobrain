---
title: "Velvet"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, bnb, crypto, defi]
aliases: ["VELVET", "Velvet Capital"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.velvet.capital/"
related: ["[[base]]", "[[bnb]]", "[[crypto-markets]]", "[[decentralized-finance]]"]
---

# Velvet (Velvet Capital)

**Velvet** (ticker **VELVET**) is the token of **Velvet Capital**, a DeFi asset-management / on-chain portfolio protocol with an "AI + DeFi" ([[defai|DeFAI]]) positioning. It is multi-chain — deployed on both [[bnb|BNB Chain]] and [[base|Base]] — and is associated with the YZi Labs (formerly Binance Labs) portfolio. CoinGecko tags include AI, DeFi, DeFAI, BNB Chain Ecosystem, Base Ecosystem/Native, and Binance Wallet IDO.

---

## Market Data

| Field | Value |
|---|---|
| **Market Cap Rank** | #179 |
| **Price** | $0.4746 |
| **Market Cap** | $200.13M |
| **24h Volume** | $13.01M |
| **24h Change** | +5.07% |
| **7d Change** | +9.35% |
| **Circulating Supply** | 420.80M VELVET |
| **Total / Max Supply** | 1.00B VELVET |
| **Fully Diluted Valuation** | $475.59M |
| **All-Time High** | $1.83 (2026-06-12) — currently ~74% below ATH |
| **All-Time Low** | $0.0413 (2025-07-10) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Dilution flag:** ~42% of the 1B max supply is circulating (420.8M). FDV ($475.6M) is roughly **2.4x** the circulating market cap ($200.1M), so a sizeable unlock overhang remains. Future emissions are a structural headwind unless demand grows alongside supply. See [[token-unlocks]].

---

## Architecture / How it works

Velvet Capital is a **DeFi asset-management protocol** — effectively on-chain infrastructure for building and running tokenized portfolios:

- **Tokenized portfolios / index-like products** — the core offering is tooling to **create, manage, and invest in** baskets of on-chain assets. A manager bundles assets and a strategy into a tokenized portfolio; other users allocate capital to it by holding the portfolio token, similar to an on-chain index or managed fund.
- **Manager + allocator model** — strategy creators (managers) define and rebalance portfolios; passive allocators get exposure without managing positions themselves. This two-sided design is the protocol's network effect.
- **DeFAI layer** — an increasing emphasis on **AI-assisted portfolio construction and automation**: using AI to help design, rebalance, or optimize portfolios, which is what places VELVET in the [[defai|DeFAI]] cohort rather than being a plain index protocol.
- **Multi-chain deployment** — running on both [[bnb|BNB Chain]] and [[base|Base]] widens the addressable asset universe and user base.

The **YZi Labs / Binance Labs association** gives Velvet more institutional pedigree than typical small-cap alts, and a **Binance Wallet IDO** tag points to a structured launch. Specific product metrics (**TVL, fees, AUM**) are not verified within this wiki — confirm current product scope against the project [docs](https://docs.velvet.capital/). Contracts: BNB (`0x8b194370825e37b33373e74a41009161808c1488`) and Base (`0xbf927b841994731c573bdf09ceb0c6b0aa887cdd`).

---

## Tokenomics & supply

- **Max supply:** 1.00B VELVET (fixed; total = max).
- **Circulating supply:** 420.80M (~42% of max).
- **MC / FDV ratio:** ~0.42 — meaningful unlocks still to come.

The ~58% of supply not yet circulating is the key tokenomics risk: scheduled unlocks (team, investors, ecosystem) can add sell pressure. The **fixed 1B cap** is a positive versus the uncapped peers in this batch ([[reallink|REAL]], [[ai-powered-finance|AIPF]]) — there is no open-ended inflation, only a finite vesting glide path. Review the vesting schedule before sizing a position. See [[token-unlocks]].

## Value accrual / governance

As an asset-management protocol, the natural value-accrual path is **management/performance fees on AUM**, optionally routed to the token via fee-share, staking, or buy-back/burn, plus governance over protocol parameters. **Honest flag:** the wiki does **not** verify a live fee-share, burn, or staking-yield mechanism, nor current AUM/fee figures — so value accrual is **plausible but unconfirmed**. That said, Velvet's model is one of the few in this batch where a *clear* revenue source (fees on managed assets) exists in principle; the open question is how much of it reaches the token. Confirm against the docs before assuming cash-flow backing.

## Comparison vs competitors

VELVET competes in **on-chain asset management / DeFAI portfolio tooling**.

| Dimension | **Velvet (VELVET)** | **[[index-coop|Index Coop (INDEX)]]** | **dHEDGE / Toros** | **[[ai-powered-finance|AIPF]]** |
|---|---|---|---|---|
| Category | DeFAI asset management | On-chain index products | On-chain managed vaults | AI-assisted DeFi automation |
| AI angle | DeFAI portfolio automation | Minimal | Minimal | "AI-assisted" contracts |
| Chains | [[bnb|BNB]] + [[base|Base]] | Ethereum / L2s | Optimism / Polygon / Base | [[polygon|Polygon]] |
| Supply | 1B fixed cap | Fixed | Varies | Uncapped |
| Backing | YZi Labs (ex-Binance Labs) | Community/DAO | Independent | None notable |
| CEX presence | Kraken / Bitget / KuCoin | Limited | Limited | None in snapshot |
| Revenue model | Fees on AUM (clear in principle) | Streaming fees on index supply | Vault performance fees | Unclear |

Takeaway: Velvet pairs a **conventional, well-understood revenue model** (fees on managed assets) with a **DeFAI narrative wrapper, institutional backing, and a real CEX footprint including Kraken** — a higher-quality profile than the thin/uncapped peers in this batch, though the unlock overhang and unverified token value-accrual remain the caveats.

---

## How & where it trades

- **Native chains:** BNB Smart Chain (`0x8b194370825e37b33373e74a41009161808c1488`) and Base (`0xbf927b841994731c573bdf09ceb0c6b0aa887cdd`).
- **Centralized venues:** historically listed on **Kraken (VELVET/USD)**, **Bitget (VELVET/USDT)**, and **KuCoin (VELVET/USDT)** — a Kraken listing is a notable liquidity/credibility positive versus pure DEX-only peers.
- **Liquidity:** ~$13.0M of 24h volume on a $200M cap (turnover ~6.5%/day) is healthy for the size. No verified perpetual-futures market is recorded here.
- **Unlock overhang:** ~58% of supply still to vest is the structural feature to watch; size against FDV (~$476M), not just the headline cap.

---

## Narrative / category & catalysts

Velvet sits squarely in the **DeFAI (AI + DeFi)** and **on-chain asset-management** narratives, with a Base-ecosystem and YZi Labs angle. It outperformed over the trailing week (+9.4%) and rallied 24h (+5.1%) against the soft tape — high-beta behaviour. Despite the bounce it remains ~74% below its mid-June 2026 ATH. See [[decentralized-finance]] and [[ai-trading]].

**Catalysts (potential, unverified):** disclosed AUM/TVL and fee growth; activation/confirmation of a token fee-share or buy-back; further CEX listings or a perp market; broad DeFAI-meta strength. Negative catalysts: large scheduled unlocks, DeFAI rotation, or evidence the token does not capture protocol fees.

## History / timeline

- **2025-07-10** — All-time low of $0.0413.
- **2026-06-12** — All-time high of $1.83.
- **2026-06-21** — Snapshot: ~$0.4746 (~-74% from ATH), ~$200.13M cap, #179 rank, ~$13.01M/day volume, +9.35% on the week.

*(Only dated events present in the market-data snapshot are listed; no TGE/launch date is asserted because none is verified in the wiki. The mid-June 2026 ATH followed by a sharp pullback shows a recent, volatile re-rating.)*

---

## Risks

- **Unlock overhang:** ~58% of supply not yet circulating; FDV ~2.4x market cap ([[token-unlocks]]).
- **Severe drawdown:** ~74% below its recent ATH; high [[volatility]].
- **Value-accrual unverified:** a clear fee source exists in principle, but token capture (fee-share/burn) and current AUM/fees are not confirmed in the wiki.
- **Narrative crowding:** "DeFAI" is a competitive, sentiment-driven category.
- **Execution / smart-contract risk:** asset-management protocols add strategy and contract risk on top of token risk ([[smart-contract-risk]]).
- **Bear-market beta:** the tape on 2026-06-23 is Extreme Fear ([[fear-and-greed-index|Fear & Greed]] 21, market-health 29/100, BEARISH) in a long-horizon **Bottoming / Accumulation** regime — outsized rallies can reverse quickly in risk-off conditions.

## Trading playbook

- **Bias:** the highest-quality name in this batch (fixed cap, YZi Labs backing, Kraken listing, real revenue model), but still a high-beta DeFAI token. Suitable as a small core-satellite if a fee/value-accrual loop is confirmed.
- **Entry:** in a bottoming, Extreme-Fear tape, the +9% weekly outperformance shows leadership behaviour — prefer adding on pullbacks toward support rather than chasing the bounce; a fee-activation or AUM-disclosure catalyst would strengthen conviction.
- **Risk control:** value on FDV; pre-define a stop given the ~74% drawdown history and the vesting overhang. No perp to hedge. Track the unlock calendar — scheduled vesting is the most likely sharp-drawdown trigger.
- **Watch:** AUM/fee disclosures and any token fee-share announcement as the value-accrual confirmation.

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[base]]
- [[decentralized-finance]]
- [[defai]]
- [[ai-trading]]
- [[token-unlocks]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- Macro framing as of 2026-06-23 (cryptodataapi.com / CoinGecko): Fear & Greed 21 (Extreme Fear), Bottoming / Accumulation regime.
- Project site/docs: https://www.velvet.capital/ , https://docs.velvet.capital/ — self-reported; not independently verified.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | VELVET |
| **Market Cap Rank** | #156 |
| **Market Cap** | $216.25M |
| **Current Price** | $0.5149 |
| **Categories** | Artificial Intelligence (AI), Decentralized Finance (DeFi), AI Applications, DeFAI, Binance Wallet IDO, Base Native |
| **Website** | [https://www.velvet.capital/](https://www.velvet.capital/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 421.07M VELVET |
| **Total Supply** | 1.00B VELVET |
| **Max Supply** | 1.00B VELVET |
| **Fully Diluted Valuation** | $513.57M |
| **Market Cap / FDV Ratio** | 0.42 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.07 (2026-06-29) |
| **Current vs ATH** | -75.43% |
| **All-Time Low** | $0.0413 (2025-07-10) |
| **Current vs ATL** | +1132.01% |
| **24h Change** | -0.48% |
| **7d Change** | +21.47% |
| **30d Change** | +13.25% |
| **1y Change** | +709.21% |

---

## Platform & Chain Information

**Native Chain:** Binance Smart Chain

### Contract Addresses

| Chain | Address |
|---|---|
| Binance Smart Chain | `0x8b194370825e37b33373e74a41009161808c1488` |
| Base | `0xbf927b841994731c573bdf09ceb0c6b0aa887cdd` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | VELVET/USD | N/A |
| Bitget | VELVET/USDT | N/A |
| KuCoin | VELVET/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.velvet.capital/](https://www.velvet.capital/) |
| **Twitter** | [@velvet_capital](https://twitter.com/velvet_capital) |
| **Telegram** | [velvetcapital](https://t.me/velvetcapital) (7,923 members) |
| **Whitepaper** | [https://docs.velvet.capital/](https://docs.velvet.capital/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $8.65M |
| **Market Cap Rank** | #156 |
| **24h Range** | $0.4916 — $0.5313 |
| **CoinGecko Sentiment** | 62% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
