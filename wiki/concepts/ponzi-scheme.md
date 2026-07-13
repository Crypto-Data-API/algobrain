---
title: "Ponzi Scheme"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [history, regulation, behavioral-finance, crypto, defi, education]
aliases: ["Ponzi", "Ponzi Fraud", "Ponzinomics", "Pyramid Scheme"]
domain: [behavioral-finance, risk-management]
prerequisites: ["[[behavioral-finance]]", "[[counterparty-risk]]"]
difficulty: beginner
related: ["[[counterparty-risk]]", "[[behavioral-finance]]", "[[ftx-collapse]]", "[[due-diligence]]", "[[defi]]", "[[stablecoins]]", "[[regulation]]", "[[2021-ohm-ponzi-arbitrage]]"]
---

A **Ponzi scheme** is a fraud that pays apparent returns to existing investors using capital contributed by new investors, rather than from any genuine profit-generating activity. Named after Charles Ponzi (1920 Boston postal-coupon fraud), it survives only while new money inflows exceed redemptions; the moment inflows slow, the scheme collapses and late investors lose nearly everything. Recognizing the structural signature of a Ponzi — returns paid from inflows, not profits — is a core risk-management skill, especially in crypto where "Ponzinomics" is endemic.

## Mechanics

The defining feature is the **source of returns**:

1. An operator promises high, suspiciously consistent returns.
2. Early investors are paid those returns — but the money comes from later investors' deposits, not real earnings.
3. Visible "profits" and word-of-mouth attract exponentially more capital.
4. Redemptions are honored as long as inflows > outflows, sustaining the illusion.
5. When inflows slow (market stress, loss of confidence, a redemption wave), the scheme cannot meet withdrawals and collapses. Only the operator and earliest exiters profit.

### Ponzi vs pyramid scheme

- **Ponzi** — investors deal with a central operator who claims to invest their money; victims are usually passive.
- **Pyramid** — participants are recruited to recruit others, earning from downline recruitment rather than a product. Both are inflow-dependent and mathematically doomed, but the pyramid makes recruitment explicit.

## Warning signs (the red-flag checklist)

- **Consistent high returns regardless of market** — real strategies have drawdowns; flat 1–2%/month forever is the classic Madoff signature.
- **Opaque or "proprietary" strategy** that can't be explained or verified.
- **Difficulty withdrawing**, or pressure to reinvest rather than redeem.
- **Unregistered/unlicensed operator**, no independent auditor, self-custody of client assets.
- **Returns paid in new tokens or "points"** rather than the asset deposited.
- **Referral incentives** that reward bringing in new money.

## Famous cases

- **Charles Ponzi (1920)** — postal reply coupon arbitrage claim; the namesake.
- **Bernie Madoff (collapsed 2008)** — the largest Ponzi in history (~$65bn in claimed value), exposed when the financial crisis triggered redemptions he couldn't meet. Harry Markopolos had warned the SEC for years.
- **Crypto-era cases** — BitConnect (2018), and numerous "high-yield" DeFi and staking schemes. The [[ftx-collapse|FTX collapse]] (2022), while legally fraud/commingling rather than a pure Ponzi, shared the inflow-dependence: customer funds were used to plug Alameda's losses, sustainable only while deposits exceeded withdrawals.

## "Ponzinomics" in crypto

Crypto has produced a spectrum between outright Ponzi fraud and **reflexive token designs** whose yield is structurally funded by new buyers rather than external cash flow:

- **Unsustainable yield protocols.** Some DeFi projects offered four- or five-digit APYs paid in their own inflationary token — sustainable only while the token price held, which required continuous new buying. The [[2021-ohm-ponzi-arbitrage|OlympusDAO (OHM) episode]] is a documented case where extreme staking yields were criticized as Ponzi-like and the token's price collapsed when inflows reversed (Source: [[2021-ohm-ponzi-arbitrage]]).
- **Algorithmic-stablecoin death spirals.** The Terra/UST collapse (May 2022) paid ~20% yield via Anchor; the peg depended on confidence and inflows, and unwound catastrophically — a reflexive failure mode adjacent to Ponzi dynamics.
- **The grey zone.** Not every high-yield crypto product is fraud, but any yield that ultimately depends on the next buyer rather than on fees, lending spreads, or real cash flow carries Ponzi-shaped tail risk.

## Trading relevance

- **It is a risk filter, not a strategy.** The actionable takeaway is detection and avoidance — protect capital from blowups masquerading as alpha.
- **The "ride it and exit early" temptation.** Some traders knowingly farm Ponzi-like yields planning to exit before collapse. This is a negative-sum game of musical chairs with severe timing risk and, often, legal/reputational exposure; the late majority always loses.
- **Counterparty discipline.** Ponzi risk is a form of [[counterparty-risk]]: assume opaque, self-custodial, "guaranteed-return" venues can be inflow-dependent. Minimize balances, demand audits/proof-of-reserves, prefer self-custody.
- **Behavioral drivers.** Ponzis exploit greed, social proof, and the authority/affinity heuristics catalogued in [[behavioral-finance]] — which is why sophisticated, well-connected investors are frequently the victims.

## Related

- [[counterparty-risk]] — the framework Ponzi risk sits within
- [[behavioral-finance]] — the cognitive biases Ponzis exploit
- [[ftx-collapse]] — inflow-dependent fraud case study
- [[due-diligence]] — the process that catches red flags
- [[defi]] / [[stablecoins]] — where Ponzinomics is most prevalent
- [[2021-ohm-ponzi-arbitrage]] — documented "Ponzi-like" token-yield episode
- [[regulation]] — the legal regime that prosecutes these frauds

## Sources

- U.S. Securities and Exchange Commission, *Ponzi Schemes* investor education and Madoff enforcement record
- Harry Markopolos, *No One Would Listen: A True Financial Thriller* (2010)
- Mitchell Zuckoff, *Ponzi's Scheme: The True Story of a Financial Legend* (2005)
- Public reporting and post-mortems on BitConnect, Terra/UST (2022), and FTX (2022)
