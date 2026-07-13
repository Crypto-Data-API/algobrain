---
title: "Espresso"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, layer-2]
aliases: ["ESP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.espresso.foundation/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-2]]", "[[modular-blockchains]]", "[[celestia]]", "[[sequencer]]", "[[arbitrum]]"]
---

# Espresso

**Espresso** (ticker **ESP**, deployed on [[ethereum|Ethereum]] and [[arbitrum|Arbitrum One]]) is a **shared sequencing / global confirmation layer** that provides [[layer-2|L2]] chains with fast, reliable transaction confirmations backed by BFT consensus. By sequencing transactions for multiple rollups, Espresso confirmations improve cross-chain composability — giving chains near-instant, credibly neutral information about what is happening not just on their own chain but across every chain plugged into the network. It can also serve as a decentralized [[sequencer]] and low-cost data-availability layer, placing it in the [[modular-blockchains|modular]] infrastructure stack.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ESP |
| **Current Price** | $0.061196 |
| **Market Cap** | $38.02M |
| **Market Cap Rank** | #548 |
| **Fully Diluted Valuation** | $220.68M |
| **24h Volume** | $2.74M |
| **24h Change** | -2.81% |
| **7d Change** | -18.02% |
| **Circulating Supply** | ~620.52M ESP |
| **Total Supply** | ~3.60B ESP |
| **Max Supply** | Uncapped (no fixed max) |
| **All-Time High** | $0.217368 (2026-02-24) |
| **All-Time Low** | $0.05223 (2026-02-15) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

ESP is a recent (2026) launch trading roughly 72% below its February 2026 all-time high of ~$0.22 and only ~17% above its all-time low of ~$0.052. The 7-day change of -18.02% is the weakest in this cohort, consistent with the extreme-fear backdrop (Crypto [[fear-and-greed-index|Fear & Greed Index]] of 23, "Established Bear Market"). The market-cap/FDV ratio of just ~0.17 is the dominant near-term risk: with ESP printing fresh weekly lows while sitting close to its ATL, the heavy locked supply is the structural feature anchoring price expectations.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~620.5M ESP |
| **Total Supply** | ~3.60B ESP |
| **Max Supply** | Uncapped (no fixed max) |
| **Market Cap / FDV** | 0.17 |

**Dilution overhang is severe.** Only ~620M of a ~3.6B total supply (~17%) circulates, leaving ~2.98B tokens (team, investors, ecosystem, foundation) to vest — and there is no fixed max supply, so issuance is not hard-capped. With market cap at ~$38M against an FDV of ~$221M, the locked supply is roughly 5.8× the current float. As a very recent launch, ESP faces a long, heavy unlock schedule that is the primary structural headwind to price.

---

## Peer Comparison

ESP sits in the shared-sequencing / modular-infrastructure niche, but its tradeable-token peers span the broader L2 / modular-DA stack. The table frames ESP against modular peers by size and float profile (data as of 2026-06-21).

| Token | Category | Mkt-cap rank | MC / FDV | Notes |
|---|---|---|---|---|
| **Espresso (ESP)** | Shared sequencing / DA | #548 | ~0.17 | Lowest float in cohort; uncapped supply |
| [[celestia\|Celestia (TIA)]] | Modular data availability | Large-cap | Higher | The reference DA layer; ESP overlaps where it offers DA |
| [[arbitrum\|Arbitrum (ARB)]] | Optimistic [[layer-2\|L2]] | Large-cap | Higher | A chain ESP can sequence/confirm; ARB runs its own sequencer today |

The comparison underlines ESP's two-sided position: too small and early to be a TIA-class infrastructure bet, yet dependent on chains like ARB choosing to outsource sequencing it does not yet control.

---

## How & Where It Trades

**Centralized exchanges (spot):** ESP has solid coverage for a new token — Binance (ESP/USDT), Kraken (ESP/USD), Upbit (ESP/KRW), KuCoin (ESP/USDT), and Crypto.com (ESP/USD). It launched via a Binance Wallet IDO and a Kaito Capital Launchpad campaign.

**Derivatives:** No major Hyperliquid perp is tracked for ESP in the current snapshot; perp coverage is limited relative to spot. Given the active downtrend and heavy unlock calendar, traders relying on hedging or leverage should confirm live CEX perp availability and funding before sizing.

**On-chain:** ESP is deployed on [[ethereum|Ethereum]] and [[arbitrum|Arbitrum One]] (note: different contract addresses on each chain).

---

## Market Structure & Derivatives

ESP's float is small and its venue mix is spot-dominated. Daily turnover of ~$2.7M against a ~$38M cap is a ~7% velocity — modest, and thinner than the high-turnover AI/DePIN names in adjacent cohorts. The lack of a tracked, liquid [[hyperliquid|Hyperliquid]] perp means there is no convenient on-chain venue to express a short or to read funding/open-interest as a sentiment gauge; hedging the heavy unlock calendar requires confirming live CEX perp availability first. In an [[established-bear-market|established bear market]] a thin, spot-only book amplifies downside: there is no perp liquidity to absorb forced selling around unlock dates, and slippage on size is a real concern.

---

## Technology

Espresso's design centers on **decoupling sequencing from execution** and offering it as a shared service:

- **Global confirmation layer** — a BFT consensus network that orders and confirms transactions for many rollups at once, giving fast (sub-second) economic confirmations.
- **Shared sequencing** — multiple L2s opt into Espresso for ordering, enabling atomic cross-rollup composability and reducing reliance on each chain's single centralized sequencer.
- **Sequencer-equivocation and reorg protection** — Espresso confirmations prevent a sequencer from giving conflicting commitments and reduce finality risk for solvers in intent-based systems.
- **Optional DA** — chains can also use Espresso as a low-cost data-availability layer, overlapping with [[celestia|Celestia]]/EigenDA in the [[modular-blockchains|modular]] stack.

The thesis is that as rollups proliferate, fragmented sequencing harms composability, and a neutral shared sequencer becomes valuable connective tissue.

---

## Use Case, Narrative & Category

ESP is a **shared-sequencing / Rollups-as-a-Service infrastructure** narrative play: the bet that a neutral, decentralized sequencing and confirmation layer becomes essential connective tissue for a multi-rollup world. CoinGecko categories include Infrastructure, Rollups-as-a-Service (RaaS), Ethereum Ecosystem, and Arbitrum Ecosystem. The bull case is widespread rollup adoption of shared sequencing for cross-chain composability; the bear case is that major L2s keep their own sequencers and shared sequencing stays a thin niche.

---

## Valuation Framing

*Qualitative — not a price target.* ESP's ~$38M market cap prices it as a speculative, pre-revenue infrastructure bet rather than a cash-flowing protocol. The key valuation tension is the gap between market cap and the ~$221M FDV: today's holder is paying for a small float of a token whose supply will multiply roughly 5.8× as locks release into an uncapped schedule. For the FDV to be justified, Espresso would need a material number of rollups to route ordering/DA through it and to capture fees from that flow — neither of which is demonstrated yet. Against modular peers, ESP is a fraction of [[celestia|Celestia]]'s size, which is appropriate given Celestia has live DA adoption while shared sequencing remains largely a thesis. The honest framing: ESP is an early-stage option on the multi-rollup composability thesis, with the unlock calendar acting as a persistent drag until real adoption metrics appear.

---

## Notable History

- **Token launched 2026** (ATH and ATL both in February 2026), via a Binance Wallet IDO and a Kaito Capital Launchpad campaign — a very recent listing.
- Built by Espresso Systems, a long-standing research team in the shared-sequencing / decentralized-sequencer space.
- Spent its first months in a downtrend, with a -18% week into 2026-06-21 amid the broader bear market — the weakest performer in this cohort.

---

## Risks

- **Severe unlock/dilution overhang** — only ~17% of supply circulates; ~83% (≈2.98B ESP) remains to vest, with no fixed max supply.
- **Adoption risk** — shared sequencing is technically compelling but major L2s have been slow to give up their own sequencers; demand is unproven.
- **Competition** — competes with other shared-sequencing/sequencer efforts (Astria, Radius, Rome) and overlaps with DA providers (Celestia, EigenDA) where it offers DA.
- **Very early stage** — recent launch, short price history, no established floor (trading ~17% above ATL).
- **Active downtrend** — weakest 7-day performance (-18%) in this cohort.
- **Thin, spot-only liquidity** — no tracked liquid perp; forced selling around unlocks has little market depth to absorb it.
- **Macro/regime** — extreme-fear sentiment ([[fear-and-greed-index|F&G]] 23) and an established bear market amplify drawdowns in newly launched infrastructure tokens.

---

## Related

- [[sequencer]] — the core primitive Espresso decentralizes and shares
- [[layer-2]] — the rollups Espresso sequences and confirms
- [[modular-blockchains]] — the architecture thesis
- [[celestia]] — peer/competitor where Espresso offers DA
- [[arbitrum]] — a chain ESP is deployed on and can sequence
- [[ethereum]] — primary settlement layer
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`)
- General market knowledge; no specific wiki source ingested yet.
