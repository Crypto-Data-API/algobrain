---
title: "Litecoin"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, altcoins]
aliases: ["LTC"]
entity_type: protocol
founded: 2011
headquarters: "Decentralized (Litecoin Foundation, Singapore)"
website: "https://litecoin.org"
related: ["[[crypto-markets]]", "[[bitcoin]]", "[[bitcoin-cash]]", "[[dogecoin]]", "[[monero]]", "[[proof-of-work]]", "[[hyperliquid]]", "[[etf]]", "[[narrative-trading]]"]
---

# Litecoin

**Litecoin** (LTC) is one of the oldest cryptocurrencies — a 2011 [[bitcoin]] code fork by ex-Google engineer Charlie Lee with 2.5-minute blocks, the Scrypt PoW algorithm, and an 84M hard cap ("digital silver" to Bitcoin's gold). Its trading significance was renewed in October 2025 when the **Canary Litecoin ETF (Nasdaq: LTCC)** became one of the first US spot altcoin ETFs, giving LTC a regulated-flow channel few [[proof-of-work]] assets have; the next halving lands in **August 2027**.

---

## Market Data

| Metric | Value |
|---|---|
| **Price (USD)** | $44.05 |
| **Market Cap** | $3.41B |
| **Market Cap Rank** | #30 |
| **24h Volume** | $186.3M |
| **24h Change** | +1.34% |
| **7d Change** | +1.29% |
| **Circulating Supply** | 77.30M LTC (~92% of 84M cap mined) |
| **Total Supply** | 77.30M LTC |
| **Max Supply** | 84.00M LTC (hard cap) |
| **All-Time High** | $410.26 (2021-05-10) — now **-89.26%** |
| **All-Time Low** | $1.15 (2015-01-14) — now **+3,730%** |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** Crypto Fear & Greed Index = **22 (extreme fear)**; the tape is in an **Established Bear Market**. LTC's near-flat week (+1.29%) is mild relative strength against a fearful backdrop, but the asset remains a high-beta [[bitcoin]] follower — see [[narrative-trading]].

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LTC |
| **Market Cap Rank** | #30 (~$3.41B, 2026-06-20); was ~#26 at the April 2026 snapshot |
| **Price** | $44.05 (2026-06-20); ATH $410.26 (May 2021) → -89.26% |
| **Chain / Sector** | Own [[proof-of-work|PoW]] Layer 1; payments / "digital silver" / ETF-wrapped majors |
| **Consensus / Hashing** | Proof of Work, Scrypt; 2.5-minute blocks; merge-mined with Dogecoin |
| **Supply Mechanics** | 84M hard cap, ~77M mined (~92%); halving every ~4 years — next ~August 2027 |
| **Privacy** | Optional MimbleWimble Extension Blocks (MWEB) since 2022 |
| **Genesis Date** | 2011-10-08 |
| **ETF** | Canary Litecoin ETF (Nasdaq: LTCC), launched 2025-10-28 |
| **Website** | [https://litecoin.org](https://litecoin.org) |

---

## Overview

Litecoin is a decentralized, peer-to-peer digital currency designed to enable instant, near-zero cost payments to individuals and merchants worldwide. As an open-source global payment network that functions independently of central banks or intermediaries, its main value proposition lies in providing a scarce digital asset with a fixed maximum supply of 84 million tokens.

The network operates using a Proof of Work mechanism where computers solve complex puzzles to confirm transactions and secure the blockchain. It is distinguished by a block generation time of 2.5 minutes, which allows for faster transaction confirmations and a higher total throughput than earlier protocols. Key technical features include the Scrypt hashing algorithm, which promotes wider network participation, and MimbleWimble Extension Blocks, which improve user privacy by allowing transaction details to be hidden.

The LTC token is used for settling global payments, executing microtransactions through smaller units called litoshis, and diversifying digital portfolios with a highly liquid asset. New tokens are issued to miners as rewards for verifying blocks, though these rewards undergo a halving event approximately every four years to strictly control inflation. This process ensures the ledger maintains immutability, meaning records cannot be changed once they are saved to the global network.

Created by former Google engineer Charlie Lee, the project is supported by the Litecoin Foundation, a non-profit organization dedicated to ecosystem adoption. Unlike many venture-backed projects, it is maintained by a decentralized community of independent developers and a global network of miners. The project has seen recent institutional adoption, with entities like Lite Strategy and Luxxfolio Holdings adding significant amounts of LTC to their corporate treasuries as of late 2025.

---

## Technology & Consensus

Litecoin is a near-direct [[bitcoin]] code fork, but with deliberate parameter changes that define its niche as "digital silver" to Bitcoin's gold.

| Property | Litecoin | [[bitcoin|Bitcoin]] |
|---|---|---|
| **Consensus** | [[proof-of-work\|Proof of Work]] | [[proof-of-work\|Proof of Work]] |
| **Hash algorithm** | **Scrypt** (memory-hard) | SHA-256 |
| **Block time** | 2.5 minutes | ~10 minutes |
| **Supply cap** | 84,000,000 | 21,000,000 |
| **Privacy** | Optional MWEB (since 2022) | None native |

- **Scrypt vs SHA-256.** Litecoin chose the memory-hard **Scrypt** hashing algorithm partly to resist the early ASIC centralization seen on [[bitcoin]]'s SHA-256 chain. Scrypt ASICs eventually arrived anyway, but the algorithm choice permanently separated LTC's mining ecosystem from BTC's.
- **Merge mining with [[dogecoin]].** Since 2014, Litecoin and [[dogecoin]] are **merge-mined** — miners secure both Scrypt chains simultaneously with the same work. This binds LTC and DOGE hashrate together and is a core part of DOGE's security budget; it also means Scrypt hashrate is a shared variable for the two assets.
- **2.5-minute blocks** give ~4× faster confirmations than [[bitcoin]], the original "faster, cheaper payments" pitch.
- **MimbleWimble Extension Blocks (MWEB)** — activated 2022 — add *optional* confidential transactions. Privacy is opt-in (unlike [[monero]]'s mandatory privacy), which keeps the regulatory surface smaller but still drew exchange scrutiny (see Risks).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 77.30M LTC |
| **Total Supply** | 77.30M LTC |
| **Max Supply** | 84.00M LTC (hard cap) |
| **% of cap mined** | ~92% |
| **Current block reward** | 6.25 LTC |
| **Next halving** | ~August 2027 → 3.125 LTC |
| **Halving interval** | ~4 years (840,000 blocks) |
| **Inflation** | Disinflationary; trends to zero at cap |

- **Fixed 84M cap** = exactly 4× [[bitcoin]]'s 21M, reinforcing the **"digital silver"** framing — a more abundant but still strictly scarce store-of-value sibling.
- ~92% of supply is already mined, so new issuance is a small and shrinking share of float; supply shocks come from halvings, not unlocks (MC/FDV ≈ 1.00, no overhang).
- Halving history: **2015** (50 → 25), **2019** (25 → 12.5), **2023** (12.5 → 6.25); next ~**August 2027** (6.25 → 3.125).

---

## Ecosystem & Use Cases

- **Payments & merchant rails.** LTC's fast, low-fee blocks made it an early favorite for crypto payments and point-of-sale processors; it remains one of the most widely accepted altcoins at payment gateways.
- **Microtransactions.** Sub-unit **litoshis** (1 LTC = 100,000,000 litoshis) enable tiny-value transfers; low fees suit micropayment use cases.
- **Corporate treasuries (late 2025).** **Lite Strategy** and **Luxxfolio Holdings** accumulated LTC as treasury assets — a small-scale echo of the MicroStrategy/Bitcoin playbook and the first visible "treasury demand" channel for LTC.
- **Regulated wrapper.** The **Canary Litecoin ETF (LTCC)** routes US advisor/retail flow into LTC without self-custody (see Market Structure).

---

## 2025–2026 Developments

- **2025-10-28 — Canary Litecoin ETF (LTCC) launches on Nasdaq**: Canary Capital's spot Litecoin ETF began trading after SEC clearance, among the first US spot altcoin ETFs (alongside HBAR and others in the October 2025 wave enabled by generic listing standards). Grayscale and CoinShares also pursued Litecoin products. LTCC filed its first Form 10-K for FY2025, confirming an operational fund. AUM remains modest relative to BTC/ETH funds — flows, not approval, are now the variable to watch.
- **Corporate treasuries (late 2025)** — Lite Strategy and Luxxfolio Holdings accumulated LTC as treasury assets, a small-scale echo of the MicroStrategy playbook.
- **Halving countdown** — block reward drops from 6.25 to 3.125 LTC around **August 2027**; historically LTC has rallied into halvings (2015, 2019, 2023) with "buy the rumor, sell the event" behavior.
- Price has lagged the majors: ~$54 at the April 2026 snapshot, -87% from the 2021 ATH, despite the ETF — evidence that regulated access alone has not generated sustained bid.

---

## Trading Relevance

- **ETF flow trade**: LTCC (plus any Grayscale/CoinShares conversions) creates a daily printed flow signal for LTC, the same structure traders use on BTC/ETH ETFs. Sustained inflows would be the first structural demand change in years; continued negligible flows confirm the bear case.
- **Halving cycle**: the August 2027 halving is the next scheduled catalyst; the historical pattern is a run-up starting ~6–9 months prior. Combine with miner-capitulation metrics (hashrate, hashprice) for entries.
- **Where it trades**: deep spot on every major CEX (Binance, Kraken, Bitget, KuCoin, Crypto.com); **LTC-PERP on [[hyperliquid]]**; CME does not list LTC futures, so perp funding is the main derivatives signal. Member of GMCI 30 and Coinbase 50 indices.
- **Basket behavior**: trades in the "legacy PoW majors" basket with BCH and DOGE (Doge is merge-mined with LTC — Scrypt hashrate links the two). High correlation to [[bitcoin]] with beta >1 in drawdowns; historically used as a liquid laggard rotation target late in alt cycles.
- **MWEB caveat**: optional privacy has occasionally drawn regulatory scrutiny (Korean exchanges delisted LTC over MWEB in 2022) — a tail risk shared with [[monero]] but much smaller since privacy is opt-in.

---

## Tokenomics (snapshot)

> *Historical CoinGecko snapshot, 2026-04-09. Current figures live in [[litecoin#Market Data|Market Data]] and [[litecoin#Tokenomics & Supply|Tokenomics & Supply]].*

| Metric | Value |
|---|---|
| **Circulating Supply** | 77.04M LTC |
| **Total Supply** | 77.04M LTC |
| **Max Supply** | 84.00M LTC |
| **Fully Diluted Valuation** | $4.15B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

> *Current point figures (2026-06-20). ATH/ATL levels are durable; short-horizon changes are current.*

| Metric | Value |
|---|---|
| **All-Time High** | $410.26 (2021-05-10) |
| **Current vs ATH** | -89.26% |
| **All-Time Low** | $1.15 (2015-01-14) |
| **Current vs ATL** | +3,730% |
| **24h Change** | +1.34% |
| **7d Change** | +1.29% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | LTC/USDT | N/A |
| Kraken | LTC/USD | N/A |
| Bitget | LTC/USDT | N/A |
| KuCoin | LTC/USDT | N/A |
| Crypto.com Exchange | LTC/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | LTC-PERP | Perpetual |

### Exchange-Traded Products

| Product | Venue | Ticker | Launched |
|---|---|---|---|
| Canary Litecoin ETF | Nasdaq | LTCC | 2025-10-28 |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://litecoin.org](http://litecoin.org) |
| **Twitter** | [@LTCFoundation](https://twitter.com/LTCFoundation) |
| **Reddit** | [https://www.reddit.com/r/litecoin/](https://www.reddit.com/r/litecoin/) |
| **GitHub** | [https://github.com/litecoin-project/litecoin](https://github.com/litecoin-project/litecoin) |
| **Whitepaper** | [https://crypto-risk-metrics.com/wp-content/uploads/2025-04-22-White-paper-Litecoin-FFG-D74JZ1VRD.pdf](https://crypto-risk-metrics.com/wp-content/uploads/2025-04-22-White-paper-Litecoin-FFG-D74JZ1VRD.pdf) |

---

## Developer Activity

> *Snapshot 2026-04-09. Note the very low commit rate — Litecoin is in maintenance mode, tracking upstream Bitcoin Core changes.*

| Metric | Value |
|---|---|
| **GitHub Stars** | 4,266 |
| **GitHub Forks** | 3,059 |
| **Commits (4 weeks)** | 1 |
| **Pull Requests Merged** | 119 |
| **Contributors** | 48 |

---

## Trading Characteristics

> *Current, 2026-06-20.*

| Characteristic | Detail |
|---|---|
| **Price** | $44.05 |
| **24h Volume** | $186.3M |
| **Market Cap Rank** | #30 |
| **24h Change** | +1.34% |
| **7d Change** | +1.29% |
| **Last Updated** | 2026-06-20 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. Disclosed corporate holders: Lite Strategy, Luxxfolio Holdings (late 2025); Canary LTCC trust holdings are the largest transparent regulated pool.*

---

## Major News & Events

- 2022 — MWEB activates (optional privacy); some Korean exchanges delist LTC in response
- 2023-08 — Third halving (12.5 → 6.25 LTC)
- 2025-10-28 — Canary Litecoin ETF (LTCC) launches on Nasdaq — first US spot Litecoin ETF
- 2025 (late) — Lite Strategy / Luxxfolio corporate treasury accumulation
- 2027-08 (expected) — Fourth halving (6.25 → 3.125 LTC)

---

## Market Structure & Derivatives

| Venue type | Detail |
|---|---|
| **Spot (CEX)** | Deep books on Binance, Kraken, Bitget, KuCoin, Crypto.com; one of the most liquid legacy altcoins |
| **Perps** | **LTC-PERP** on [[hyperliquid]] and every major perp venue; funding/OI are the primary derivatives read |
| **Listed futures** | **No CME LTC futures** — unlike BTC/ETH, so perp funding (not CME basis) is the main institutional-derivatives signal |
| **ETP** | **Canary Litecoin ETF (LTCC)**, Nasdaq, launched 2025-10-28 — first US spot Litecoin ETF |
| **Indices** | GMCI 30, Coinbase 50 |

- The **Canary Litecoin ETF (LTCC)** is the structural novelty: it gives LTC a *daily printed regulated-flow* channel that most [[proof-of-work]] assets lack. Treat published creation/redemption flow the same way traders read BTC/ETH ETF flow — sustained inflows would be the first new structural demand in years; persistent negligible flow confirms the bear case. (No AUM/flow figures asserted here without a primary source.)
- Because float is mature (~92% mined, MC/FDV ≈ 1.00), price is driven by flow and BTC beta, not unlock schedules.

---

## Trading Playbook

- **ETF-flow trade.** Watch LTCC (and any Grayscale/CoinShares conversions) net flow as a structural-demand signal; pair with hashrate/hashprice for miner-capitulation confirmation.
- **Halving-cycle run-up.** The **August 2027** halving is the next scheduled catalyst; LTC has historically rallied ~6–9 months ahead of halvings (2015, 2019, 2023) with "buy the rumor, sell the event" behavior.
- **Legacy-PoW-majors basket.** LTC rotates with [[bitcoin-cash]] and [[dogecoin]] as the "cheap/old PoW" basket; DOGE is merge-mined with LTC, so Scrypt hashrate links the two. See [[narrative-trading]].
- **High-beta BTC follower.** LTC tracks [[bitcoin]] with **beta > 1 in drawdowns** — it falls harder in risk-off and is used as a liquid **laggard-rotation target** late in alt cycles.
- **Regime note (2026-06-20):** with Fear & Greed = 22 and an Established Bear Market, the laggard-rotation and run-up trades are early/contrarian, not confirmed-trend setups.

---

## Competitive Positioning

LTC and [[bitcoin-cash]] are the two canonical **[[bitcoin]] forks / "cheap BTC" proxies**, but they diverge on algorithm, lineage, and niche:

| Dimension | Litecoin (LTC) | [[bitcoin-cash\|Bitcoin Cash (BCH)]] | [[bitcoin\|Bitcoin (BTC)]] |
|---|---|---|---|
| **Relationship to BTC** | 2011 code fork (separate chain from genesis) | 2017 *chain* hard fork (shared BTC history pre-fork) | Original |
| **Hash algorithm** | Scrypt | SHA-256 | SHA-256 |
| **Block time** | 2.5 min | ~10 min | ~10 min |
| **Supply cap** | 84M | 21M | 21M |
| **Halving family** | Own schedule (next ~Aug 2027) | Same family as BTC (last Apr 2024) | Apr 2024 |
| **US spot ETF** | Yes — LTCC (Nasdaq) | No (Grayscale trust only) | Yes |
| **Niche** | "Digital silver", payments, merge-mined w/ DOGE | "Big-block" payments, CashTokens scripting | "Digital gold", reserve asset |

- **vs [[bitcoin]]:** LTC is positioned as **"digital silver"** — same store-of-value logic, 4× the cap, faster/cheaper blocks, but far smaller security budget and brand.
- **vs [[bitcoin-cash]]:** both are "cheap BTC" rotation candidates, but BCH shares BTC's SHA-256 mining and pre-2017 history, while LTC is an older, algorithmically distinct chain with the unique ETF + merge-mining angles.

---

## Risks

- **Maintenance-mode development.** Core dev activity is very low (≈1 commit in a 4-week window at the April 2026 snapshot); LTC largely tracks upstream Bitcoin Core changes rather than innovating.
- **ETF hasn't moved price.** LTC was ~-87% from ATH even *after* the LTCC launch — regulated access alone has not generated a sustained bid. The bear case is "access without demand."
- **MWEB regulatory tail risk.** Optional privacy has drawn scrutiny — Korean exchanges delisted LTC over MWEB in 2022. A shared (but smaller) risk with [[monero]] since privacy is opt-in.
- **Security-budget dependence.** LTC's hashrate is intertwined with [[dogecoin]] via merge mining; a collapse in Scrypt mining economics would weaken both chains.
- **High-beta drawdowns.** In risk-off tape (current Fear & Greed = 22, Established Bear Market), LTC tends to underperform [[bitcoin]] to the downside.

---

## Related

- [[crypto-markets]]
- [[bitcoin]] — parent codebase and dominant price driver ("digital silver" vs gold)
- [[bitcoin-cash]] — fellow "cheap BTC" fork / legacy-PoW basket peer
- [[dogecoin]] — merge-mined Scrypt partner; shared hashrate
- [[monero]] — full-privacy counterpart to LTC's optional MWEB
- [[proof-of-work]] — consensus mechanism (Scrypt variant)
- [[etf]] — LTCC as the altcoin-ETF template
- [[hyperliquid]] — LTC perp venue
- [[narrative-trading]] — legacy-PoW / ETF-rotation baskets

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Canary Capital — "Canary Capital Launches Canary Litecoin ETF (LTCC)" (2025-10-28): https://www.canary.capital/thought-leadership/canary-capital-launches-canary-litecoin-etf-ltcc
- Nasdaq — launch press release (2025-10-28): https://www.nasdaq.com/press-release/canary-capital-launches-canary-litecoin-etf-ltcc-2025-10-28
- SEC EDGAR — Canary Litecoin ETF Form 10-K FY2025 and S-1/A filings: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002039461
- ETFGI — "Canary Capital Launches Canary Litecoin ETF (LTCC)": https://etfgi.com/news/stories/2025/10/canary-capital-launches-canary-litecoin-etf-ltcc
- Verified via Perplexity sonar + web search, 2026-06-10
