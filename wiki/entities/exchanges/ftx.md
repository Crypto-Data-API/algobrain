---
title: "FTX"
type: entity
created: 2026-04-06
updated: 2026-06-20
status: excellent
tags: [crypto, exchange, fraud, collapse, history, regulation, risk-management]
entity_type: exchange
founded: 2019
related: ["[[sam-bankman-fried]]", "[[alameda-research]]", "[[crypto-winter]]", "[[blockfi]]", "[[voyager-digital]]", "[[sec]]", "[[self-custody]]", "[[binance]]", "[[coinbase]]", "[[proof-of-reserves]]"]
---

# FTX

**FTX** was a centralized cryptocurrency exchange founded in 2019 by [[sam-bankman-fried|Sam Bankman-Fried (SBF)]] that rapidly grew to become one of the largest trading platforms in crypto before its catastrophic collapse in **November 2022** due to massive fraud. The FTX failure was the most significant exchange collapse in crypto history, wiping out an estimated **$8-10 billion** in customer funds and accelerating the 2022 [[crypto-winter]]. The subsequent criminal trial, 25-year prison sentence for SBF, and years-long creditor recovery process make FTX one of the most consequential events in the history of digital assets.

---

## At a Glance

| Attribute | Detail |
|---|---|
| Type | Centralized cryptocurrency exchange (derivatives + spot) |
| Founded | May 2019 |
| Founder / CEO | [[sam-bankman-fried\|Sam Bankman-Fried (SBF)]] |
| Affiliated trading firm | [[alameda-research\|Alameda Research]] |
| Native token | FTT |
| Peak valuation | ~$32B (Series C, Jan 2022) |
| Headquarters | The Bahamas (relocated from Hong Kong) |
| Collapse | Nov 2-11, 2022 (Chapter 11 on Nov 11) |
| Estimated customer shortfall | ~$8-10B |
| Outcome | SBF convicted on 7 counts; 25-year sentence; estate recovery ongoing |

---

## Rise and Fall

| Phase | Timeline | Key Events |
|---|---|---|
| **Founding** | May 2019 | SBF launches FTX with [[alameda-research|Alameda Research]] as market maker |
| **Growth** | 2020-2021 | Becomes #2 exchange by volume; $18B valuation (Series B, Jul 2021); celebrity endorsements (Tom Brady, Steph Curry), FTX Arena naming rights ($135M) |
| **Peak** | Jan 2022 | Series C at $32B; investments from Sequoia, BlackRock, SoftBank, Tiger Global |
| **Collapse** | Nov 2-11, 2022 | CoinDesk exposes Alameda balance sheet; Binance CZ tweets; bank run; bankruptcy |
| **Criminal charges** | Dec 2022 | SBF arrested in Bahamas, extradited to US |
| **Trial** | Oct-Nov 2023 | SBF found guilty on all seven counts |
| **Sentencing** | Mar 2024 | SBF sentenced to 25 years in federal prison |
| **Creditor recovery** | 2023-2026 | FTX estate liquidates assets; creditors receive partial recovery |

---

## Business Model and Products

FTX built its reputation on a derivatives-first product suite that was unusually sophisticated for a retail-accessible exchange. Understanding the product set clarifies how the fraud was hidden and why the FTT token was central:

| Product | Description | Role in the Collapse |
|---|---|---|
| FTX International | Offshore derivatives + spot exchange (Bahamas) | Held the bulk of commingled customer funds |
| FTX US | Separate US-regulated entity | Marketed as walled-off; also entered bankruptcy |
| FTT token | Native exchange token (fee discounts, staking) | Used as collateral by [[alameda-research\|Alameda]]; the reflexive core of the failure |
| Perpetual futures / leveraged tokens | High-leverage derivatives and tokenized leverage | Drove volume and the exchange's "pro" reputation |
| FTX Ventures | Venture investment arm | Deployed customer-linked funds into illiquid bets (e.g., [[anthropic\|Anthropic]] stake) |
| LedgerX (FTX US Derivatives) | Acquired CFTC-regulated derivatives venue | Among the cleaner assets recovered by the estate |

[[alameda-research|Alameda Research]] functioned as the dominant market maker on FTX, an arrangement publicly known and frequently dismissed as a conflict of interest. The FTT token tied the two firms together: Alameda held large FTT positions and used them as collateral, so any decline in FTT directly impaired Alameda's balance sheet — the reflexive death spiral that played out in November 2022.

---

## What Happened

FTX secretly loaned **$8+ billion** in customer deposits to [[alameda-research|Alameda Research]], SBF's affiliated trading firm. Alameda used these funds for speculative investments, venture capital, political donations, and personal expenses. When a CoinDesk report revealed Alameda's balance sheet was heavily dependent on FTT (FTX's own exchange token), a bank run ensued that FTX could not cover.

Key fraud elements:
- Customer funds commingled with Alameda's trading operations
- Backdoor in FTX's accounting systems hid the deficit
- FTT token used as collateral — circular and worthless under stress
- No independent board oversight or proper internal controls
- FTX had no functioning accounting department; financial records were kept in QuickBooks and Slack messages

---

## Detailed Collapse Timeline (November 2022)

The collapse unfolded over 10 days:

| Date | Event |
|---|---|
| **Nov 2** | CoinDesk publishes leaked Alameda balance sheet showing most of its $14.6B in assets were illiquid FTT and FTX-linked tokens |
| **Nov 6** | [[binance]] CEO Changpeng Zhao (CZ) tweets that Binance will liquidate its ~$580M FTT holdings "due to recent revelations" |
| **Nov 7** | FTT price crashes 32%; FTX faces ~$6B in withdrawal requests in 72 hours |
| **Nov 8** | Binance announces non-binding letter of intent to acquire FTX; FTX halts withdrawals |
| **Nov 9** | Binance walks away from the deal after due diligence reveals the $8B+ hole; SBF continues tweeting "assets are fine" |
| **Nov 10** | SBF attempts to raise emergency funding, fails; Bahamian regulator freezes FTX Digital Markets |
| **Nov 11** | FTX, FTX US, Alameda Research, and ~130 affiliated entities file Chapter 11 bankruptcy; SBF resigns as CEO; John J. Ray III appointed (same lawyer who oversaw Enron's liquidation) |
| **Nov 12** | Reports surface of ~$477M in suspicious outflows from FTX wallets (later attributed to both a hack and FTX/Bahamian regulator actions) |

John Ray III later testified that FTX was the worst case of corporate mismanagement he had ever seen — worse than Enron.

---

## SBF Trial and Conviction

### Criminal Charges

SBF was arrested in the Bahamas on December 12, 2022, and extradited to the United States. He was charged with seven criminal counts:

1. Wire fraud against FTX customers
2. Conspiracy to commit wire fraud against FTX customers
3. Wire fraud against [[blockfi|BlockFi]] and other lenders
4. Conspiracy to commit wire fraud against lenders
5. Conspiracy to commit commodities fraud
6. Conspiracy to commit securities fraud
7. Conspiracy to commit money laundering

### Trial (October-November 2023)

The trial lasted approximately five weeks. Key developments:

- **Caroline Ellison** (former CEO of [[alameda-research|Alameda Research]] and SBF's ex-girlfriend) was the prosecution's star witness, testifying that SBF directed her to take customer funds and use falsified financial statements
- **Gary Wang** (FTX co-founder and CTO) testified he built the secret backdoor in FTX's code that allowed Alameda to borrow customer funds without standard collateral requirements
- **Nishad Singh** (FTX head of engineering) also cooperated and testified against SBF
- SBF took the stand in his own defense — a decision widely regarded as having backfired
- All three cooperating witnesses received significantly reduced sentences for their cooperation

### Verdict and Sentencing

- **November 2, 2023**: Jury found SBF **guilty on all seven counts** after approximately four hours of deliberation
- **March 28, 2024**: SBF sentenced to **25 years in federal prison** by Judge Lewis Kaplan
- Prosecutors had sought 40-50 years; defense asked for 5-6.5 years
- SBF ordered to forfeit **$11.02 billion**
- As of 2026, SBF is serving his sentence and has filed an appeal

### Co-Conspirator Sentences

| Person | Role | Sentence |
|---|---|---|
| Caroline Ellison | Alameda CEO | 2 years |
| Gary Wang | FTX CTO | No prison (time served + supervised release) |
| Nishad Singh | FTX Engineering Lead | No prison (time served + supervised release) |
| Ryan Salame | FTX co-CEO | 7.5 years |

---

## Creditor Recovery Process

The FTX bankruptcy estate, managed by restructuring firm Sullivan & Cromwell under CEO John Ray III, undertook one of the largest and most complex crypto asset recoveries in history.

### Recovery Timeline

| Date | Milestone |
|---|---|
| **Jan 2023** | Estate locates $5.5B in liquid assets (initially reported as only $1B at bankruptcy) |
| **Mid-2023** | Estate sells FTX's stake in [[anthropic|Anthropic]] (~$900M worth, acquired for $500M pre-collapse), Solana holdings, and other venture investments |
| **Sep 2023** | Court approves liquidation of $3.4B in crypto holdings (primarily [[solana|SOL]], [[bitcoin|BTC]], [[ethereum|ETH]]) |
| **Jan 2024** | FTX reorganization plan filed, projecting 118% recovery for customers with claims under $50,000 |
| **Oct 2024** | Court approves reorganization plan |
| **Jan-Mar 2025** | Initial distributions begin to creditors |

### Key Recovery Details

- The estate recovered significantly more than initially expected, partly because crypto prices rose substantially between the November 2022 bankruptcy (BTC ~$16,000) and the 2024-2025 distribution period (BTC $60,000+)
- Creditors with allowed claims under $50,000 were projected to receive **approximately 118%** of their claim value (based on petition-date prices, not current market prices)
- **Critical caveat for traders**: The 118% figure is based on the *dollar value at time of bankruptcy* — meaning a creditor who had 1 BTC (worth ~$16,000 in Nov 2022) received ~$18,880 in cash, not 1 BTC (which by 2025 was worth $60,000+). The opportunity cost was enormous.
- Larger creditors received lower percentage recoveries
- The estate clawed back political donations, sponsorship deals, and payments to insiders

---

## Contagion and Cascading Failures

FTX's collapse triggered a chain of failures across the crypto industry:

| Entity | Exposure | Outcome |
|---|---|---|
| [[blockfi]] | $1.2B in loans to FTX/Alameda | Filed Chapter 11 bankruptcy (Nov 28, 2022) |
| [[voyager-digital]] | Had agreed to FTX acquisition deal | Deal collapsed; Voyager re-entered bankruptcy |
| Genesis Global | $175M in funds locked on FTX | Filed Chapter 11 (Jan 2023), contributing to [[digital-currency-group|DCG]]/Grayscale stress |
| Galois Capital | ~50% of fund on FTX | Shut down |
| Multicoin Capital | Significant exposure | Major drawdown (details undisclosed) |
| [[solana]] | SBF was largest Solana booster | SOL dropped from ~$35 to ~$8; recovered only in 2023 |

The contagion demonstrated how interconnected crypto lending, exchange, and trading firm relationships had become — and how little [[risk-management|counterparty risk management]] existed in the industry.

---

## Lessons for Traders

### 1. Counterparty Risk Is Existential

FTX had a $32B valuation, major VC backing, and celebrity endorsements. None of that protected customer deposits. The core lesson: **no centralized entity should be trusted with funds you cannot afford to lose**, regardless of its reputation.

Practical steps:
- Use [[self-custody]] for long-term holdings
- Minimize exchange balances to only what is needed for active trading
- Diversify across multiple exchanges for trading capital
- Treat exchange deposits as unsecured creditor claims (because legally, they are)

### 2. Proof of Reserves Matters — But Is Not Sufficient

After FTX, every major exchange published proof-of-reserves (PoR) attestations. These are necessary but insufficient:
- PoR shows assets exist at a point in time but does not show liabilities
- A proper **proof of solvency** requires both assets AND liabilities disclosure
- [[binance]], [[coinbase]], [[kraken]], and others now publish regular PoR reports
- Third-party audit firms (not just self-attestations) provide higher confidence

### 3. Exchange Token Red Flags

FTT's role as collateral in the Alameda/FTX relationship is a permanent case study in circular risk:
- Exchange tokens (FTT, BNB, etc.) used as collateral create **reflexive death spirals** — when the token drops, collateral is insufficient, forcing more selling
- Traders should monitor the ratio of exchange-token-collateral to real assets in any exchange-adjacent entity
- If an exchange's balance sheet is heavily dependent on its own token, that is a warning sign

### 4. Due Diligence Signals That Were Missed

In hindsight, multiple warning signs existed before the collapse:
- No board of directors; SBF had sole control
- Headquartered in the Bahamas with minimal regulatory oversight
- Alameda's conflicts of interest were publicly known but dismissed
- FTX's auditor (Prager Metis) was a small firm with no major exchange audit experience; the audit reports contained disclaimers about going concern
- SBF's personal lifestyle (polycule house, stimulant use, Bahamas compound) drew attention but was reframed as "quirky founder" rather than governance red flag

---

## Regulatory Impact

FTX's collapse was the single most influential event for crypto regulation globally:

### United States
- The [[sec|SEC]] and [[cftc|CFTC]] intensified enforcement actions against crypto companies throughout 2023-2024
- The SEC sued [[binance]] and [[coinbase]] in June 2023, citing FTX as evidence of the need for exchange regulation
- Congressional hearings accelerated work on stablecoin and exchange legislation
- The collapse strengthened the SEC's argument that most crypto tokens are securities

### International
- The **EU's MiCA (Markets in Crypto-Assets)** regulation, already in progress, was accelerated and went into effect in 2024
- **Hong Kong** launched a new crypto licensing regime in 2023
- **Japan's** pre-existing exchange regulations (implemented after the Mt. Gox hack) were vindicated — Japanese FTX customers were among the first to recover funds because Japanese law required segregated customer accounts
- **Singapore** and **Dubai** tightened exchange licensing requirements

### Industry Self-Regulation
- Major exchanges adopted proof-of-reserves reporting
- Institutional investors began requiring exchange risk assessments before deploying capital
- Insurance and custodial solutions gained adoption as alternatives to exchange-held custody

---

## FTX in Historical Context

FTX joins a lineage of exchange failures in crypto history:

| Exchange | Year | Amount Lost | Cause |
|---|---|---|---|
| Mt. Gox | 2014 | ~850,000 BTC (~$450M at the time) | Hack + mismanagement |
| QuadrigaCX | 2019 | ~$190M CAD | Founder death (disputed); likely fraud |
| **FTX** | **2022** | **~$8-10B** | **Fraud, commingling customer funds** |

FTX is by far the largest by dollar amount and the most significant in terms of regulatory and market impact.

---

## Trading Relevance

- The FTX collapse is the strongest argument for [[self-custody]] — "not your keys, not your coins"
- It triggered contagion that brought down [[blockfi]], contributed to [[voyager-digital|Voyager's]] losses, and deepened the [[crypto-winter]]
- Exchange counterparty risk assessment became a core [[risk-management]] discipline post-FTX
- Proof of reserves, regulatory compliance, and exchange transparency became industry standards
- The event accelerated global crypto regulation efforts
- **BTC price impact**: Bitcoin fell from ~$21,000 to ~$15,500 in the week of the collapse, eventually bottoming near $15,400 in late November 2022 — a level that marked the cycle low
- **Market structure lesson**: The 2022-2023 bear market bottom was partly caused by forced selling from FTX contagion, creating a generational buying opportunity for traders who understood the mechanics

---

## See Also

- [[sam-bankman-fried]] — FTX founder, convicted of fraud and sentenced to 25 years
- [[alameda-research]] — SBF's trading firm at the center of the fraud
- [[blockfi]] — Collapsed after FTX exposure
- [[voyager-digital]] — Recovery deal with FTX collapsed
- [[crypto-winter]] — The bear market FTX's collapse intensified
- [[self-custody]] — The alternative to trusting centralized exchanges
- [[binance]] — CZ's tweet triggered the bank run; Binance also faced regulatory scrutiny post-FTX
- [[solana]] — SBF was its largest booster; SOL suffered disproportionately
- [[sec]] — US regulator that intensified enforcement post-FTX
- [[proof-of-reserves]] — Industry response to FTX's opacity
- [[risk-management]] — Counterparty risk assessment frameworks
