---
title: "BitDCA"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, bitcoin, payments]
aliases: ["BDCA"]
entity_type: protocol
headquarters: "Decentralized (BitDCA / Littlebit project; Europe-focused)"
website: "https://www.bitdca.io/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[bitcoin]]", "[[dollar-cost-averaging]]"]
---

# BitDCA

**BitDCA** (ticker **BDCA**) is a **BNB Chain** payment-and-savings project whose mobile app, **Littlebit**, lets users automatically save in [[bitcoin|Bitcoin]] by setting aside a small percentage of each card payment — round-up / automatic [[dollar-cost-averaging|dollar-cost-averaging]] into BTC without opening new accounts or cards. BDCA is the project's utility token: holders earn a share of revenue generated from Littlebit transactions. The project is Europe-focused with stated plans for global expansion in 2026.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Ticker** | BDCA |
| **Price** | $0.6707 |
| **Market-cap rank** | #420 |
| **Market cap** | ~$55.3M |
| **Fully diluted valuation** | ~$95.7M |
| **24h volume** | ~$267K |
| **24h change** | +1.45% |
| **7d change** | -2.49% |
| **Circulating supply** | ~82.4M BDCA |
| **Total supply** | ~142.7M BDCA |
| **Max supply** | 150.0M BDCA |
| **All-time high** | $1.18 (2025-10-02), now -43.0% |
| **All-time low** | $0.3645 (2025-03-01), now +84.0% |

**Supply / valuation note:** Circulating supply (~82.4M) is about 55% of max supply (150M) and ~58% of total supply (~142.7M). Market cap (~$55.3M) sits well below FDV (~$95.7M), so roughly 68M BDCA (~45% of max) remains to be emitted/unlocked. This is a meaningful **dilution overhang** — future unlocks could pressure price as supply approaches the 150M cap.

---

## Technology & Mechanism

BitDCA is a **consumer fintech + token** model on BNB Chain:

- **Littlebit app.** Connects to a user's existing debit/credit card and automatically diverts a chosen percentage of each purchase into Bitcoin (automatic DCA / round-ups). No new bank account or card is required, lowering onboarding friction for retail savers.
- **Revenue share.** BDCA token holders earn a share of revenue from every Littlebit transaction — the token is positioned as a claim on app cashflow / usage, aligning holders with adoption.
- **Chain.** The BDCA token is issued on [[bnb|BNB Chain]] (BSC); contract `0x0c8382719ef242cae2247e4decb2891fbf699818`.
- **Security.** The project cites a CertiK audit and emphasizes security and transparency.

### Architecture: how the save-in-Bitcoin flow works

The product is, mechanically, an **automated [[dollar-cost-averaging|DCA]] / round-up engine** wrapped in a consumer app, with the token bolted on as a revenue-share instrument:

1. **Card linkage.** The Littlebit app connects to a user's *existing* debit/credit card — there is no new card or bank account, which is the central friction-reduction and the project's distribution edge.
2. **Round-up / percentage diversion.** On each qualifying purchase, the app sets aside a chosen small percentage (or rounds up), and that amount is periodically converted to [[bitcoin|BTC]]. This is recurring, behavior-driven accumulation — "[[dollar-cost-averaging|stacking sats]] from everyday spending" — rather than a lump-sum buy.
3. **Conversion & custody rails.** The diverted fiat is converted to BTC and held via the app's custody/conversion infrastructure; users depend on those rails for safekeeping and execution (a counterparty consideration — see Risks).
4. **Token revenue share.** Each Littlebit transaction generates revenue, and **BDCA holders earn a share of it**, making the token an explicit claim on app usage/cashflow rather than a gas or governance token.

The whole model is a **distribution bet**: the value of BDCA's revenue-share rests on Littlebit's transaction volume scaling (Europe-first, with stated 2026 global-expansion plans). The token does not power a chain or secure a network; it is a usage-linked incentive layer on top of a fintech product.

### Value accrual & governance

BDCA's value accrual is **revenue-share-based**, which is more direct than a soft loyalty token but entirely **adoption-contingent**: the share is only as valuable as the underlying Littlebit transaction stream. There is no gas-burn sink and the utility is framed around cashflow participation rather than governance. Because the share scales with app usage, the token is effectively a leveraged claim on whether the consumer app reaches and sustains scale — a high-variance, distribution-dependent payoff.

---

## Tokenomics & Supply

- **Max supply:** 150.0M BDCA (hard cap).
- **Circulating:** ~82.4M (~55% of cap); **total:** ~142.7M.
- The gap between circulating and total/max implies scheduled emissions or locked allocations still to enter the market — a dilution factor to watch (MC/FDV ~0.58).
- Token utility centers on **transaction revenue share** rather than gas or governance.

---

## How & Where It Trades

- **Exchanges:** No major centralized-exchange listing surfaced in the snapshot data; trading is primarily on BNB Chain DEX liquidity.
- **Liquidity profile:** Thin. 24h volume (~$267K) is very small relative to a ~$55M market cap, implying low float turnover and high slippage risk on size. Price is therefore sensitive to modest flows.
- **Derivatives:** None of note; treat as a spot-only, DEX-centric microcap.

---

## Comparison vs. Bitcoin-savings / round-up peers

| Product | Token? | Mechanism | Custody/asset | Distinguishing edge |
|---|---|---|---|---|
| **BitDCA / Littlebit** | **BDCA** (revenue share) | Auto-DCA / round-ups on existing card | App-custodied BTC | Token revenue-share; Europe-first card integration |
| **Relai** | No token | Recurring/one-off BTC buys (app) | Self-custody / app | BTC-only, EU-regulated, no token complexity |
| **Strike** | No token | Buy/DCA BTC + payments (Lightning) | App/Lightning | Lightning payments + DCA, large reach |
| **Cash App (Bitcoin)** | No token | Recurring BTC purchases / round-ups | App-custodied | Massive distribution via existing fintech base |

The comparison isolates BitDCA's two-sided proposition: most "auto-stack-BTC" competitors are **tokenless apps** that compete purely on UX, regulation, and reach, whereas BitDCA layers a **revenue-share token** on top. That token is upside if Littlebit scales, but it also adds the speculative/dilution dynamics those tokenless rivals avoid — so BDCA must out-execute on *distribution* to justify the extra moving part.

---

## Narrative & Category

BDCA sits in the **Bitcoin-savings / payments / consumer-fintech** narrative — "stack sats automatically from everyday spending." It belongs with the broader crop of apps that gamify or automate Bitcoin accumulation for non-technical users, with the token layered on as a revenue-share incentive. The edge is distribution (Europe-first card integration); the question is whether app adoption scales enough to back the token's valuation.

### Catalysts

Positive catalysts are adoption- and reach-driven: execution on the **2026 global-expansion** plan, growth in Littlebit's user base and transaction volume (which directly feeds the revenue share), new licensing/geographies, payment-rail or card integrations, and any credible centralized-exchange listing that would relieve the thin-liquidity problem. The negative path is the mirror image — adoption stalling, EU consumer-finance/crypto regulatory friction on card-linked auto-investing, or the substantial emission overhang weighing on price as supply approaches the 150M cap.

## History / timeline

- **2025-03-01** — All-time low of **$0.3645** recorded.
- **2025-10-02** — All-time high of **$1.18** recorded.
- **2026 (stated)** — Project plans global expansion beyond its Europe-first base.
- **2026-04-09** — CoinGecko top-1000 snapshot ingested for this page.
- **2026-06-21** — Market snapshot: **$0.6707**, ~$55.3M cap, rank #420; +1.45% / 24h, -2.49% / 7d (now -43% from ATH).

---

## Risks

- **Dilution.** ~45% of max supply not yet circulating; emissions can pressure price.
- **Adoption risk.** Token value rests on Littlebit app usage and transaction volume actually materializing and scaling globally.
- **Liquidity risk.** Very thin volume; no major CEX listing means difficult exits in size.
- **Regulatory risk.** Card-linked auto-investing into crypto touches EU consumer-finance and crypto regulation; expansion plans depend on licensing.
- **Custody / counterparty risk.** Users rely on the app's BTC custody and conversion rails.
- **Macro backdrop.** As of 2026-06-21 crypto Fear & Greed reads 23 ("Established Bear Market"); small-cap consumer tokens are especially exposed to risk-off conditions, and BDCA is already -43% from its ATH.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context: as of 2026-06-23 the market reads **Extreme Fear (F&G 21)** with a long-horizon **bottoming/accumulation** regime ([[bitcoin|BTC]] ~$64,568) — consistent with, and slightly worse than, the bearish backdrop noted on the page's 2026-06-21 snapshot. For a thin, adoption-dependent consumer-fintech microcap like BDCA:

- **Two layered bets.** Holding BDCA is a bet on **[[bitcoin|BTC]] direction** *and* on **Littlebit adoption** — the revenue share only matters if app usage scales. In Extreme-Fear risk-off, the second bet is the fragile one; a low token price alone is not a thesis.
- **Liquidity is the binding constraint.** No major CEX listing plus ~$267K daily volume means exits in size are slippage-heavy; size positions assuming you may not get the screen price. See [[liquidity]] and [[risk-management]].
- **Dilution headwind.** ~45% of max supply is still to be emitted; an accumulation case must price in unlock pressure as supply approaches 150M.
- **Distinguish bounce from turn.** A bottoming-regime sentiment rally can lift the whole small-cap cohort; a *durable* re-rate for BDCA needs evidence of Littlebit transaction growth — data the market doesn't yet have. Avoid leverage given the thin, derivatives-light market.

---

## Related

- [[bitcoin]]
- [[dollar-cost-averaging]]
- [[bnb]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Issuer documentation: BitDCA / Littlebit (https://www.bitdca.io/, https://gitbook.bitdca.com/).
- General market knowledge; no specific wiki source ingested yet.
