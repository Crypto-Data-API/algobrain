---
title: "Monero"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["XMR"]
entity_type: protocol
founded: 2014
headquarters: "Decentralized"
website: "https://www.getmonero.org/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[dash]]", "[[hyperliquid]]", "[[narrative-trading]]", "[[privacy-coins]]", "[[proof-of-work]]", "[[zcash]]"]
---

# Monero

**Monero** (XMR) is the flagship privacy coin: a [[proof-of-work]] Layer 1 launched in April 2014 whose ring signatures, stealth addresses, and RingCT make all transactions private by default. For traders it is the purest expression of the "[[privacy-coins|privacy]]/censorship-resistance" narrative basket — it led the privacy-coin rally of late 2025/early 2026, hitting an all-time high of ~$798 in January 2026 — while carrying structural liquidity risk from repeated exchange delistings.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #21 |
| **Market Cap** | $5.89B |
| **Current Price** | $314.01 |
| **24h Volume** | $145.09M |
| **24h Change** | -3.60% |
| **7d Change** | -8.00% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: the snapshot sits in **extreme fear** ([[fear-and-greed-index|Fear & Greed]] = 22) within an Established [[bear-market|Bear Market]]. XMR is **down** on both the day (-3.60%) and the week (-8.00%), underperforming the broad tape — a notable contrast with its privacy-peer [[zcash|Zcash]], which is green over the same window. At **$314.01**, XMR is ~60.6% below its January 2026 ATH of $797.73. Thin order books (a consequence of delistings) tend to amplify both legs of any move.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XMR |
| **Market Cap Rank** | #21 (2026-06-20) |
| **Market Cap** | $5.89B (2026-06-20) |
| **Price** | $314.01 (2026-06-20; vs ~$798 ATH 2026-01-14) |
| **Chain / Sector** | Own [[proof-of-work|PoW]] Layer 1; [[privacy-coins|privacy coin]] |
| **Consensus / Hashing** | Proof of Work, RandomX (CPU-friendly, ASIC-resistant) |
| **Supply Mechanics** | ~18.77M XMR circulating; no hard cap — perpetual "tail emission" of 0.6 XMR/block (~157K XMR/year, <1% inflation) |
| **Genesis Date** | 2014-04-18 |
| **Website** | [https://www.getmonero.org/](https://www.getmonero.org/) |

---

## Overview

Monero is the dominant privacy-by-default cryptocurrency. Unlike [[bitcoin]]'s transparent ledger, Monero hides sender, receiver, and amount on every transaction using ring signatures, stealth addresses, and Ring Confidential Transactions. Its RandomX hashing algorithm is deliberately CPU-friendly to resist ASIC and pool centralization. The supply schedule ended its main emission in 2022 and switched to a perpetual tail emission of 0.6 XMR per block, giving miners a permanent income floor and the asset a low, asymptotically declining inflation rate.

Because of its untraceability, Monero faces sustained regulatory pressure: it has been delisted from major exchanges in many jurisdictions (Binance delisted XMR in 2024; OKX, Kraken in the EEA, and others earlier), which fragments liquidity but also reinforces its core use case.

---

## Technology & Privacy

Monero achieves **mandatory, default privacy** — every transaction is shielded, with no opt-in/opt-out (the key contrast with [[zcash|Zcash]]'s optional shielding). Three primitives combine to hide the three pieces of transaction data:

| Primitive | Hides | How |
|---|---|---|
| **Ring signatures** | The *sender* | The real spend is mixed with decoy outputs (a "ring"); a verifier sees a valid signature from *one* of the ring members but cannot tell which |
| **Stealth addresses** | The *receiver* | Each payment is sent to a unique one-time address derived from the recipient's public keys; on-chain addresses never repeat and can't be linked to the recipient |
| **RingCT (Ring Confidential Transactions)** | The *amount* | Pedersen commitments + range proofs (Bulletproofs/Bulletproofs+) prove the amounts balance without revealing them |

| Component | Detail |
|---|---|
| **Consensus** | [[proof-of-work|Proof of Work]] |
| **Hash function** | **RandomX** — optimized for general-purpose CPUs and deliberately ASIC-hostile, to keep mining decentralized and pool-resistant |
| **Block time** | ~2 minutes; dynamic block size (no fixed cap) |
| **Privacy default** | Mandatory — there is no transparent ("t-address") mode; the entire chain is shielded |
| **Fungibility** | High — because history is hidden, coins are interchangeable; no "tainted UTXO" tracking is possible |

**Why RandomX matters for traders.** CPU-mineable PoW keeps mining broadly distributed but also makes **hashrate attacks cheaper to attempt** than on [[bitcoin]] — the Qubic episode (below) is the live example. Default privacy also means **no public rich list exists**, so whale/holder analytics are impossible by construction.

---

## Tokenomics & Supply

> *Supply snapshot from CoinGecko data, 2026-06-20.*

| Metric | Value |
|---|---|
| **Circulating Supply** | ~18,767,350 XMR |
| **Total Supply** | ~18,767,350 XMR |
| **Max Supply** | None (uncapped — perpetual tail emission) |
| **Market Cap / FDV Ratio** | ~1.00 |

- **Tail emission.** Monero's main emission curve ended in May 2022; since then the protocol pays a **perpetual tail emission of 0.6 XMR per block** (~157K XMR/year). This is a deliberate design choice: it gives miners a permanent block-reward income floor (so security does not depend solely on fees) at the cost of a small, asymptotically declining inflation rate (<1% and falling as the base grows). This contrasts sharply with [[zcash|Zcash]]'s [[bitcoin]]-style 21M hard cap and halving schedule.
- **No premine / no founder allocation.** Monero launched fair (no ICO, no VC allocation), so there is **no vesting overhang or foundation sell-pressure** — a structural positive often cited during rallies.
- **Fungibility as monetary property.** Because transaction history is hidden, all XMR are interchangeable; there is no way to blacklist "tainted" coins, which is core to its sound-money / censorship-resistance pitch.

---

## Ecosystem & Use Cases

- **Private payments** — the canonical use case: peer-to-peer payments where amounts and counterparties are confidential by default.
- **Censorship resistance / debanking hedge** — held as protection against financial surveillance, debanking, and transaction monitoring; demand spikes on surveillance-regulation headlines.
- **Darknet / OTC flows** — a non-trivial part of real usage (and a source of regulatory targeting); darknet/OTC demand data is a watched fundamental.
- **Merchant / donation rails** — privacy-preserving donations and merchant payments where transparency is undesirable.
- **Atomic swaps** — BTC↔XMR atomic swaps provide a (lower-liquidity) on/off ramp that bypasses delisting exchanges.

---

## Market Structure & Derivatives

Monero is the textbook case of a **liquidity-constrained, delisting-exposed** asset — this must be stated honestly:

- **Spot venues**: spot on [[kraken|Kraken]] (XMR/USD, with deposit restrictions tightened after Aug 2025), KuCoin, and smaller/offshore venues. **Delisted from [[binance|Binance]] (2024), OKX, and most regulated EEA venues** — fiat on/off ramps are structurally fragmented.
- **Perps / funding / OI**: perps on [[hyperliquid|Hyperliquid]] (XMR-PERP) and offshore CEXs. Because spot is thin and delistings concentrate flow, **perp funding and OI can swing violently**, and squeezes (both directions) are common. Daily volume ~$130M–$1B depending on regime.
- **No ETF pathway.** No US (or any major) spot ETF exists or is realistically filable for a default-privacy coin — this keeps XMR a **retail/OTC-flow asset**, removing the institutional-flow catalyst that [[near|NEAR]]/[[sui|Sui]]/[[hedera-hashgraph|Hedera]] enjoy and that even [[zcash|Zcash]] (optional privacy) has a marginally better claim to.
- **Slippage / execution**: thin order books mean material slippage on size; use limit orders, expect gaps around delisting/regulatory news.

---

## Trading Playbook

- **Sector lead**: XMR is the **anchor of the [[privacy-coins|privacy basket]]** ([[zcash|Zcash]] ZEC, [[dash|DASH]] followed XMR's January 2026 move with high beta). Watch XMR as the sector lead and trade laggards for catch-up; conversely, divergence (as on 2026-06-20, with ZEC green and XMR red) signals rotation *within* the basket.
- **Where it trades**: see Market Structure — thin, delisting-fragmented; treat liquidity as a first-class risk.
- **Catalysts**: privacy-regulation headlines (EU AMLR implementation, US surveillance proposals), exchange delisting/relisting announcements, hashrate-concentration scares (Qubic-style), darknet/OTC demand data.
- **Structural risks**: further delistings shrinking fiat ramps; 51%-attack repeats; a regulatory ban in a major jurisdiction. No ETF pathway means no institutional bid backstop.
- **Regime note (2026-06-20)**: XMR down ~8% on the week into extreme fear while ZEC rallies — a sign privacy-basket flows have rotated toward ZEC's zk-narrative; pairs traders watch the XMR/ZEC ratio.

---

## History

- **18 Apr 2014** — Launched as a fork of Bytecoin (originally "BitMonero"); fair launch, no premine.
- **2014–2018** — Iterative privacy hardening: RingCT (2017) hides amounts; mandatory min ring size raises baseline privacy.
- **2019** — Switch to **RandomX** PoW to resist ASICs and keep mining CPU-based and decentralized.
- **2021** — Bull-market run; sets prior cycle highs.
- **2022** — Main emission ends; **tail emission of 0.6 XMR/block** begins; Bulletproofs+ reduces fees/size.
- **2024** — **Binance delists XMR**; cumulative delisting pressure across regulated venues fragments liquidity.
- **12–18 Aug 2025** — **Qubic 51% episode** (see below): hashrate-concentration scare and Kraken deposit halt; XMR sells off then rebounds.
- **12–14 Jan 2026** — XMR breaks its 2021 ATH amid a privacy-coin sector rally, printing **$797.73 (2026-01-14)**; privacy sector ~$21B aggregate.
- **2026** — Retraces with the broad bear market; ~$314 at 2026-06-20 (-60.6% from ATH).

### Qubic 51% attack episode (August 2025)

- **2025-08-12** — The **Qubic mining pool** (led by IOTA co-founder Sergey Ivancheglo) claimed majority control of Monero's hashrate as a "useful proof-of-work demonstration," reorganizing 6 blocks and orphaning ~60 blocks. XMR dropped ~6% on the news and suffered a panic-driven sell-off of up to ~19% during the week.
- **2025-08-17/18** — **[[kraken|Kraken]] halted XMR deposits**, then re-enabled them with a punitive 720-confirmation requirement. Community miners redistributed hashrate; Qubic lost its majority and the network returned to pluralistic mining. XMR rebounded ~7% above $260.
- **Takeaway for traders**: Monero's CPU-mineable design makes hashrate attacks cheaper to attempt than on [[bitcoin]]; exchange-risk responses (deposit halts, confirmation hikes) can hit price faster than the attack itself.

### Privacy-coin rally (late 2025 – January 2026)

- XMR broke its 2021 ATH and ran to roughly **$657–$798 in January 2026** (CoinGecko ATH $797.73 on 2026-01-14), outperforming BTC, ETH and nearly all majors; the privacy sector reached ~$21B aggregate value.
- Drivers: US/EU surveillance and transaction-monitoring proposals, debanking/financial-censorship fears, growing awareness of [[bitcoin|Bitcoin]]'s permanent traceability, and a supply structure with minimal sell pressure (tail emission only, no foundation/VC overhang).
- Delisting-driven scarcity worked paradoxically in its favor: thin order books amplified the move both up and down. XMR retraced to ~$314 by mid-2026 (-60.6% from ATH).

---

## Competitive Positioning — Monero vs Zcash

| Dimension | **Monero (XMR)** | **[[zcash|Zcash]] (ZEC)** |
|---|---|---|
| Privacy model | **Mandatory / default** (every tx shielded) | **Optional** (transparent t-addr or shielded z-addr) |
| Cryptography | Ring signatures + stealth addresses + RingCT | **[[zero-knowledge-proofs|zk-SNARKs]]** (Halo/Orchard) |
| Supply | **Uncapped**, perpetual tail emission (0.6 XMR/block) | **21M hard cap**, [[bitcoin]]-style halvings |
| Consensus | [[proof-of-work|PoW]] (RandomX, CPU/ASIC-resistant) | [[proof-of-work|PoW]] (Equihash); PoS "Crosslink" planned |
| Fungibility | Very high (no traceable history) | Lower in practice (most tx historically transparent) |
| Launch | Fair launch, no premine | Founders' reward / dev funding model |
| Key tail risk | Hashrate-concentration (Qubic) + delistings | **AI-discovered crypto bugs** (June 2026 Orchard counterfeiting) |
| Anonymity-set issue | Decoy-based; ring size limits | Anonymity set = shielded pool usage |

**Bottom line**: Monero offers stronger *default* fungibility (everyone is private), while Zcash offers stronger *cryptographic* privacy when the shielded pool is used — but suffers from low shielded adoption and, in 2026, a high-profile zk-bug. They are the two poles of the [[privacy-coins]] sector and the primary pairs-trade within it. See also [[dash|DASH]] (optional CoinJoin-style privacy, higher beta laggard).

---

## Regulatory

- **Privacy-coin regulatory risk is the dominant overhang.** Default untraceability puts Monero squarely in the crosshairs of AML/CFT regimes:
  - **EU AMLR** — anti-money-laundering rules whose implementation timeline threatens privacy-coin support at regulated EU venues.
  - **US surveillance / transaction-monitoring proposals** — periodic catalysts in both directions (demand spikes vs. delisting fears).
- **Delisting cascade**: [[binance|Binance]] (2024), OKX, and most regulated EEA venues have removed XMR; each delisting fragments liquidity and is a discrete negative catalyst, though it paradoxically reinforces the censorship-resistance thesis.
- **No regulated product pathway**: a default-privacy coin is effectively un-ETF-able under current US frameworks, capping institutional adoption.
- **Jurisdictional ban risk**: an outright ban in a major jurisdiction is a live tail risk.

---

## Risks

- **Delisting / liquidity** — further removals shrink fiat ramps and thin order books; slippage and squeezes are structural.
- **51%-attack repeats** — CPU-mineable PoW makes hashrate attacks cheaper to attempt (Qubic, Aug 2025).
- **Regulatory ban** — a major-jurisdiction ban or AMLR-driven EU exclusion is a tail risk.
- **No institutional bid** — no ETF/regulated-product pathway; XMR is a retail/OTC asset.
- **Narrative dependence** — trades on privacy/surveillance headlines; can derate fast when the theme cools (as into mid-2026).
- **Macro/regime** — high-beta, thin-liquidity alt in an Established Bear Market; ~60% off ATH.

---

## Whale & Holder Information

> *Monero's privacy design makes on-chain holder distribution analysis impossible by construction — there is no public rich list.*

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Notes |
|---|---|---|
| Kraken | XMR/USD | Deposit restrictions tightened after Aug 2025 Qubic episode (720 confirmations) |
| KuCoin | XMR/USDT | |

> Delisted from [[binance|Binance]] (2024), OKX, and most regulated EEA venues — liquidity is structurally fragmented.

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | XMR-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.getmonero.org/](https://www.getmonero.org/) |
| **Twitter** | [@monero](https://twitter.com/monero) |
| **Reddit** | [https://www.reddit.com/r/monero](https://www.reddit.com/r/monero) |
| **GitHub** | [https://github.com/monero-project/monero](https://github.com/monero-project/monero) |
| **Whitepaper** | [https://www.getmonero.org/library/Zero-to-Monero-2-0-0.pdf](https://www.getmonero.org/library/Zero-to-Monero-2-0-0.pdf) |

---

## Developer Activity

> *Snapshot 2026-04-09.*

| Metric | Value |
|---|---|
| **GitHub Stars** | 8,309 |
| **GitHub Forks** | 3,594 |
| **Pull Requests Merged** | 4,875 |
| **Contributors** | 320 |

---

## Major News & Events

- 2025-08-12 — Qubic pool claims majority Monero hashrate; 6-block reorg, ~60 orphaned blocks
- 2025-08-17/18 — Kraken halts then restores XMR deposits with 720-confirmation requirement; miners reverse Qubic's majority; XMR rebounds above $260
- 2026-01-12/14 — XMR breaks 2021 ATH amid privacy-coin sector rally; prints ~$798 high; privacy sector ~$21B

---

## Related

- [[crypto-markets]]
- [[bitcoin]] — transparent-ledger counterpoint that drives privacy demand
- [[zcash]] — main privacy-coin peer (optional privacy vs Monero's default privacy)
- [[dash]] — optional-privacy laggard in the basket
- [[privacy-coins]] — sector page
- [[hyperliquid]] — main perp venue for XMR exposure
- [[narrative-trading]] — privacy basket
- [[proof-of-work]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko markets snapshot, 2026-06-20 (current Market Data block)
- CoinDesk — "Qubic Claims Majority Control of Monero Hashrate, Raising 51% Attack Fears" (2025-08-12): https://www.coindesk.com/business/2025/08/12/qubic-claims-majority-control-of-monero-hashrate-raising-51-attack-fears
- CryptoSlate — "Kraken suspends Monero deposits after 51% attack" (Aug 2025): https://cryptoslate.com/kraken-suspends-monero-deposits-after-51-attack/
- Coinspeaker — "Monero (XMR) Emerges Top Gainer as Miners Reverse Qubic's 51% Attack" (Aug 2025): https://www.coinspeaker.com/monero-xmr-emerges-top-gainer-as-miners-reverse-qubics-51-attack-and-kraken-restriction/
- CoinDesk — "Privacy tokens rally as XMR breaks all-time high" (2026-01-12): https://www.coindesk.com/markets/2026/01/12/privacy-tokens-rally-as-xmr-breaks-all-time-high
- DL News — "Privacy coins continue to rally — how long will the hype last?": https://www.dlnews.com/articles/markets/privacy-coins-are-surging-but-for-how-much-longer/
- Verified via Perplexity sonar + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.78M XMR |
| **Total Supply** | 18.78M XMR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $6.26B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $797.73 (2026-01-14) |
| **Current vs ATH** | -58.20% |
| **All-Time Low** | $0.2162 (2015-01-14) |
| **Current vs ATL** | +154139.87% |
| **24h Change** | +2.56% |
| **7d Change** | +3.55% |
| **30d Change** | -4.22% |
| **1y Change** | -0.37% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $98.80M |
| **Market Cap Rank** | #19 |
| **24h Range** | $324.74 — $333.98 |
| **CoinGecko Sentiment** | 84% positive |
| **Last Updated** | 2026-07-16 |

---

## See Also

- [[crypto-markets]]

---
