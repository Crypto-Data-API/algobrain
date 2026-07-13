---
title: "KOGE"
type: entity
created: 2026-04-09
updated: 2026-06-24
status: excellent
tags: [crypto, bnb]
aliases: ["KOGE", "BNB48 Club Token"]
entity_type: protocol
headquarters: "Decentralized (48 Club)"
website: "https://www.48.club"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]"]
---

# KOGE

**KOGE** (ticker **KOGE**, formerly **BNB48 Club Token**) is the native community/ecosystem token of the **48 Club**, a long-running validator and community organization on [[bnb|BNB Chain]] (BSC). It is a **BEP-20** asset (contract `0xe6df05ce8c8301223373cf5b969afcb1498c5528`) and a **Binance Alpha Spotlight** project. Rather than a single-purpose utility coin tied to one product, KOGE functions as a membership/community asset within the 48 Club orbit, with a deliberately **tiny fixed supply (~3.44M max)** that produces a high per-token price (low-$60s) on a relatively modest (~$214M) market cap. Its trading profile is defined by **extreme illiquidity** and dependence on BNB-ecosystem and Binance Alpha attention.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Ticker** | KOGE |
| **Price** | $63.42 |
| **Market-cap rank** | #170 |
| **Market cap** | ~$214.3M |
| **Fully diluted valuation** | ~$214.3M |
| **24h volume** | ~$62K |
| **24h change** | -1.61% |
| **7d change** | -1.89% |
| **Circulating supply** | ~3.38M KOGE |
| **Total supply** | ~3.38M KOGE |
| **Max supply** | ~3.44M KOGE |
| **All-time high** | $76.94 (2022-03-25), now -17.6% |
| **All-time low** | $1.19 (2021-02-01), now +5,225% |

**Supply / valuation note:** Circulating supply (~3.38M) essentially equals total supply and is ~98% of max supply (~3.44M), so **MC ≈ FDV** (ratio ~1.00) and there is **no meaningful dilution overhang** — almost the entire supply is already in circulation. The very small supply count (≈3.4M) explains the high per-token price.

---

## Architecture / How It Works

KOGE is best understood not as a product token but as the **community/ecosystem asset of the 48 Club**, so its design choices follow from that identity:

- **48 Club — validator and community.** 48 Club is a well-known [[bnb|BNB Chain]] validator and community organization. Validators on BNB Chain participate in block production and receive transaction-fee/gas rewards; the "club" wraps that infrastructure role in a community/membership identity. KOGE is the token associated with that group — a coordination and community asset rather than the gas token of an independent chain. (BNB itself is the chain's gas token; KOGE rides on top as a BEP-20.)
- **Chain & contract.** KOGE is issued on [[bnb|BNB Chain]] (BSC) as a standard **BEP-20** token, contract `0xe6df05ce8c8301223373cf5b969afcb1498c5528`. There is no separate "KOGE chain" — settlement, transfers and DEX liquidity all happen on BSC, and the token inherits BSC's low fees and fast blocks.
- **Tiny fixed supply → high unit price.** The defining structural feature is the **~3.44M max supply**. Because supply is measured in millions (not billions), a ~$214M market cap divides into a **low-$60s per-token price**. The high unit price is an artifact of the small float, not of an unusually large valuation. This is the inverse of typical memecoins, which use huge supplies to print sub-cent prices; KOGE deliberately does the opposite.
- **Binance Alpha Spotlight distribution.** KOGE has been featured in **[[binance|Binance]] Alpha**, the program that surfaces early-stage and BNB-ecosystem tokens to Binance users (often with points/airdrop campaigns, trading-volume incentives and visibility inside the Binance app/wallet). For a token with no major centralized-exchange spot pair, Alpha inclusion is the **primary distribution and attention channel** — it is what brings volume and price discovery to an otherwise on-chain-only asset.

> Because 48 Club is primarily a validator/community organization, the token's "mechanism" is social and infrastructural (community coordination + BNB validation + program inclusion) rather than a smart-contract product with a defined cash flow. Treat utility claims accordingly — see [[#Risks]].

---

## Tokenomics & Supply

- **Fixed, very small supply:** ~3.44M max, ~3.38M circulating (**≈98% already in circulation**).
- **No dilution overhang:** MC and FDV are effectively equal (ratio ~1.00). There is **no large unlock cliff or emission schedule** implied by the snapshot — unlike low-float L1/L2 tokens (e.g. [[adi-token|ADI]]) where most supply is locked and FDV dwarfs market cap, KOGE's quoted market cap already reflects nearly the full supply.
- **High unit price from float design:** The four-figure-style per-unit price seen across this cohort is a direct function of the deliberately tiny supply (≈3.4M units), **not** a signal of large fundamental value. Market cap (~$214M) is the meaningful aggregate, not the headline price.
- **Tight, concentrated holder base:** A small fixed supply held by a community/validator group tends to be **tightly held**, which suppresses freely-traded float still further and amplifies price sensitivity to any single large order.

---

## Value Accrual / Governance

KOGE's value proposition is **community- and validator-linked rather than product-linked**, and it is important to be candid about that:

- There is **no single headline product** (no flagship dApp, no fee-burn machine, no protocol revenue line) that mechanically accrues value to the token in the way a DEX or lending token might.
- Value accrual is **indirect and reflexive**: it derives from (1) the standing and activity of the 48 Club community and its BNB validator role, (2) inclusion in distribution/attention programs like **Binance Alpha Spotlight**, and (3) the scarcity narrative created by the tiny fixed float.
- **Governance** is community-driven within the 48 Club context rather than a formal on-chain DAO with treasury control over a product. Holders should not assume governance rights over cash flows that do not exist.
- Practically, this means KOGE behaves more like a **community/membership beta on BNB-ecosystem sentiment and Binance Alpha attention** than like an equity-style claim on a protocol's earnings.

---

## Comparison vs Other BNB-Ecosystem / Alpha Cohort Tokens

KOGE sits in the low-float, attention-driven corner of the [[bnb|BNB Chain]] ecosystem. It is most usefully contrasted with other BNB-ecosystem / Binance Alpha tokens and with high-unit-price low-supply assets:

| Token | Chain | Float / supply design | Primary price driver | Liquidity profile |
|---|---|---|---|---|
| **KOGE** (this page) | BNB Chain (BEP-20) | Tiny fixed (~3.44M), ~98% circulating, MC≈FDV | 48 Club community + Binance Alpha inclusion (no single product) | Very thin (~$62K/24h vs ~$214M MC); on-chain DEX + Alpha rails |
| [[siren-2|SIREN]] | BNB Chain (BEP-20, via Four.meme) | Large supply (~1B max), near-fully circulating | AI-agent / memecoin narrative + Binance Meme Liquidity / Alpha programs; product = Siren Terminal | Mid-cap at peak but reflexive — evaporates in drawdowns; spot via KuCoin / Binance Alpha |
| [[ultima\|ULTIMA]] | BNB Chain (BEP-20) | Tiny fixed (100k max) → four-figure unit price | High-yield / MLM-scrutiny ecosystem; new-money inflows | Concentrated, few venues; structural red flags |
| [[bnb\|BNB]] | BNB Chain (native gas) | Large, deflationary (quarterly burns) | Exchange utility + gas + fee burns; the ecosystem reserve asset | Deep, top-tier CEX + DEX liquidity |

**Reading the table:** KOGE shares SIREN's and ULTIMA's dependence on **program inclusion and ecosystem attention** (rather than a defensible product) but differs in supply design — KOGE's tiny fixed float resembles ULTIMA's "high unit price from small supply" model, while SIREN uses the opposite large-supply memecoin model. Against [[bnb|BNB]] itself, the contrast is stark: BNB has deep liquidity and a clear utility/burn value-accrual story, whereas KOGE's headline market cap rests on a sliver of active turnover.

---

## How & Where It Trades

- **Venues:** **No major centralized-exchange spot pair** surfaced in the snapshot; activity is concentrated on **BNB Chain DEX liquidity** and **[[binance|Binance]] Alpha** rails. Price discovery is therefore largely on-chain plus Alpha-program flow rather than order-book depth on a top-tier CEX.
- **Liquidity profile — extremely thin:** Reported **24h volume (~$62K) against a ~$214M market cap** is an exceptionally low turnover ratio (well under 0.1% of market cap traded per day). The quoted market cap rests on a very small float of *active* trading.
- **Headline MC may not be realizable in size:** Because so little trades each day, the ~$214M figure is a mark-to-last-print, **not** a number you could exit against. A position of any meaningful size would likely move the price sharply on the way out. Treat the headline market cap with caution.
- **Derivatives:** No major perpetual-futures or options market evident; effectively **spot/on-chain only**, which removes hedging avenues and concentrates risk in the illiquid spot venue.

---

## Narrative & Category

KOGE belongs to the **BNB Chain ecosystem / community-token** narrative, amplified by inclusion in **Binance Alpha Spotlight**. Its relevance is tied to the **48 Club** community and to broad [[bnb|BNB]]-ecosystem flows rather than a standalone product thesis. As with many low-float Alpha-listed tokens, attention and price are heavily driven by **program inclusion and community activity** — Alpha campaigns, points/airdrop mechanics, and BNB-ecosystem sentiment.

**Catalysts (attention-driven):**
- Continued or expanded **Binance Alpha Spotlight** inclusion, points campaigns, or volume incentives.
- Broad **BNB-ecosystem risk appetite** (BNB strength tends to lift its community-token satellites).
- 48 Club community / validator developments and visibility.
- Any move toward a major-CEX spot listing (would materially change the liquidity picture).

**Anti-catalysts:** loss of Alpha inclusion, fading BNB-ecosystem attention, or a broad risk-off leg in the [[crypto-markets|crypto market]].

---

## History / Timeline

Only events with verified dates from the market-data snapshot are listed; the rest of the timeline is intentionally left sparse rather than invented.

- **2021-02-01** — All-time low **$1.19** (now ~+5,225%). Reflects very early, illiquid pricing of a then-nascent BNB community token.
- **2022-03-25** — All-time high **$76.94** (now ~-17.6%), set during the broad 2021–2022 crypto cycle peak.
- **2026** — Featured as a **Binance Alpha Spotlight** project; trades in the low-$60s on extremely thin volume (snapshot 2026-06-21).

> No other dated milestones are independently verified here. The long gap between the 2022 ATH and the present, with price still within ~18% of that high, is notable for a token of this float and reflects the tightly held, low-turnover supply rather than deep liquid demand.

---

## Risks

- **Liquidity / float risk (high).** Extremely low volume (~$62K/24h) versus market cap (~$214M); the **headline valuation may not be realizable**, and exits in size could move price sharply against you. This is the single most important risk.
- **Headline-MC-not-realizable.** The market cap is a mark on a tiny active float, not a number you can sell into. Size positions to *daily volume*, not to market cap.
- **Low-float volatility & concentration.** A ~3.4M-unit supply held by a community/validator group makes price highly susceptible to a small number of concentrated holders and thin order books; a single large sell can gap the price.
- **Narrative / attention dependence.** Value is closely tied to [[bnb|BNB]]-ecosystem sentiment and **Binance Alpha** attention. Loss of program inclusion or a fade in ecosystem flow can remove the main demand driver.
- **Limited utility clarity.** As a community/ecosystem token (not a product token), fundamental value drivers are **less defined** — there is no protocol revenue, fee burn, or product cash flow to anchor valuation. See [[#Value Accrual / Governance]].
- **No derivatives / hedging.** Spot/on-chain only; no perps to hedge or to provide a deeper price-discovery venue.
- **Macro backdrop.** As of **2026-06-24** the crypto regime is an **Established Bear Market** (Fear & Greed **22 — Extreme Fear**; market-health 28/100, bearish; BTC ≈ $62,568, ~18% below its moving average). Low-liquidity community tokens are **highly exposed** to risk-off conditions, where thin books thin further and slippage rises.

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: 2026-06-24 — **Extreme Fear (22)**, Established Bear Market. This is a position-sizing-and-liquidity problem first, a thesis second.

- **Treat as illiquid by default.** With ~$62K/day turnover, even a modest position is large relative to the book. **Size to daily volume**, not to market cap, and assume meaningful slippage on entry *and* exit.
- **Plan the exit before the entry.** In a low-float, low-volume name, the exit is the hard part. Know in advance how many days of average volume it would take to unwind your size; if the answer is "many," the position is too big.
- **Use limit orders, never market orders.** Thin BNB Chain DEX depth means market orders can gap badly. Stage entries/exits in small clips.
- **Catalyst-gated, not buy-and-hold.** The realistic edge is around **Binance Alpha** campaigns / program inclusion and BNB-ecosystem attention spikes. Outside those windows, expect drift and dead volume.
- **In Extreme Fear, default to flat or tiny.** A bear regime is the worst environment for an illiquid attention token: demand evaporates first in exactly these names. If holding, keep size trivial and accept that you may not be able to exit cleanly.
- **Watch BNB.** [[bnb|BNB]] strength/weakness is the simplest read-through for community-token risk appetite; a weak BNB tape is a headwind for the whole cohort.

---

## Related

- [[bnb]]
- [[binance]]
- [[crypto-markets]]
- [[siren-2]]
- [[ultima]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Project: 48 Club (https://www.48.club).
- General market knowledge; no specific wiki source ingested yet.
