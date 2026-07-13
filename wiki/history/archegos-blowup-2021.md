---
title: "Archegos Blow-Up (March 2021)"
type: news
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [history, stocks, derivatives, leverage, risk-management]
aliases: ["Archegos Collapse", "Hwang Blow-Up", "Archegos 2021"]
event_date: 2021-03-26
markets_affected: [stocks, derivatives]
impact: high
verified: true
sources_count: 5
related: ["[[total-return-swap]]", "[[prime-broker]]", "[[ltcm-collapse-1998]]", "[[bill-hwang]]", "[[block-trade-flipping-arbitrage]]", "[[prime-broker-cascade-trading]]", "[[structural-forced-selling]]"]
---

The Archegos Capital Management blow-up in March 2021 was the largest single-fund prime-brokerage loss in modern finance: [[bill-hwang]]'s family office, running an undisclosed and extraordinarily leveraged concentrated book through [[total-return-swap|total-return swaps]] (TRS) with multiple prime brokers, faced a cascading margin call that triggered fire-sale liquidations. Bank losses exceeded roughly $10 billion in aggregate, with credit-suisse losing about $5.5 billion and nomura about $2.9 billion. The episode exposed catastrophic prime-broker risk-management failures, the opacity of synthetic-prime (TRS) books, and the regulatory gap for family offices. Hwang was convicted of fraud and market manipulation in July 2024.

## Background

**Bill Hwang** (Sung Kook Hwang) was a [[tiger-management]] "Tiger Cub" who ran Tiger Asia Management from 2001 until 2012, when the firm pled guilty to U.S. insider-trading charges and paid ~$44 million. Barred from managing outside capital, Hwang converted Tiger Asia into [[archegos|Archegos Capital Management]] in 2013 -- a family office deploying his personal wealth, which grew from roughly $200 million in 2013 to an estimated $35 billion of gross market exposure by March 2021 (reported leverage of approximately 5x-8x on roughly $10-15 billion of equity).

Because a family office manages only the principal's own capital, Archegos was exempt from U.S. Investment Advisers Act registration and reporting (the exemption solidified by Dodd-Frank's "family office rule" in 2011). It filed no 13F and published nothing about its book.

## Strategy and Mechanics

Archegos ran a long-biased, highly concentrated equity book in a small number of names -- notably [[viacomcbs]] (later Paramount Global), [[discovery-inc]], [[tencent-music]] ADRs, baidu, [[gsx-techedu]], [[iqiyi]], [[vipshop]], [[rlx-technology]], [[farfetch]], and shopify. Rather than hold shares directly, Archegos built most positions via **[[total-return-swap|total-return swaps]] (TRS)** and **[[contract-for-difference|contracts for difference]] (CFDs)** with prime-broker counterparties.

Under a TRS:

- The prime broker buys the underlying equity and holds it on balance sheet.
- Archegos pays financing (typically SOFR/LIBOR + spread) and a modest initial margin (often 10-20%).
- Archegos receives all price appreciation and dividends; pays any depreciation.
- The broker shows the hedged stock on its own books; Archegos's name appears nowhere in public filings.

This structure gave Hwang three decisive advantages:

1. **Invisibility**: TRS positions do not trigger 13D/13G disclosure, even when effective economic ownership crosses 5%. Archegos's share of ViacomCBS was reportedly close to 20% on a look-through basis.
2. **Leverage multiplication**: 15-20% initial margin equals 5-7x leverage on a single leg.
3. **Fragmentation of counterparty view**: because Hwang ran similar positions at credit-suisse, nomura, morgan-stanley, goldman-sachs, ubs, wells-fargo, [[mufg]], and others, no single bank could see the aggregate.

### Leverage mechanics worked example

The [[total-return-swap|TRS]] is the load-bearing instrument of the entire episode — without it, neither the leverage nor the invisibility was achievable. A simplified single-name leg illustrates how thin margin converts a modest move into a wipe-out:

| Step | Cash equity (buy stock outright) | TRS leg at 15% initial margin |
|------|----------------------------------|--------------------------------|
| Notional exposure | $100m | $100m |
| Capital posted | $100m | $15m (initial margin) |
| Effective leverage | 1.0x | ~6.7x |
| Stock falls 15% (mark −$15m) | Equity now $85m (−15%) | Margin fully consumed; broker issues variation-margin call |
| Stock falls 30% (mark −$30m) | Equity $70m (−30%) | Posted margin (−$15m) gone **and** broker is $15m underwater if client cannot pay |

At ~6-7x effective leverage, a move equal to the initial margin (roughly the 15-20% Archegos posted) erases the position's entire collateral, and any further decline becomes the **prime broker's** loss once the client defaults. Because Archegos ran the *same* concentrated names this way across eight-plus banks simultaneously, a single basket-wide drawdown (the ViacomCBS-led decline) breached margin on every leg at once — the textbook mechanism behind a [[structural-forced-selling|forced-selling]] cascade and a direct demonstration of [[counterparty-risk|counterparty]] / [[counterparty-credit-risk|counterparty-credit risk]] in [[derivatives]]. The bank, not Hwang, was holding the residual tail. See also [[leverage]] and [[margin]].

## Trigger: ViacomCBS Secondary Offering

ViacomCBS (ticker VIAC/VIACA) had rallied roughly 300% from late 2020 into March 2021, partly on Hwang's buying pressure. On **Monday March 22, 2021**, ViacomCBS announced a $3 billion equity and convertible-preferred secondary offering, priced the next day at **$85 per share** -- well below where the stock had closed the previous week (~$100). The secondary triggered a sharp sell-off: VIAC fell roughly 9% on March 23 and continued lower through the week.

This mark-to-market decline, combined with similar moves in other Archegos concentrations (Discovery, Baidu, Tencent Music), generated **margin calls that Archegos could not meet** by Thursday March 25.

## The Cascade (March 25-29, 2021)

**Thursday March 25**: The primes convened a call to coordinate an orderly unwind. credit-suisse and nomura favored a staged liquidation; goldman-sachs and morgan-stanley refused to agree to a standstill.

**Friday March 26**: goldman-sachs and morgan-stanley launched large block sales *before* market open and through the day -- reportedly $10.5 billion from Goldman and similar size from Morgan Stanley. Stocks collapsed: ViacomCBS fell ~27% on the day; Discovery -27%; Baidu -14%; Tencent Music -34%. The block-trade tickets that hit the tape became visible to the market and compounded the selling.

**Sunday March 28 - Monday March 29**: credit-suisse and nomura, having moved slower, were left holding the worst of the exposure. Both disclosed preliminary loss estimates before the March 29 open.

### Condensed timeline

| Date (2021) | Event |
|-------------|-------|
| 2001-2012 | Hwang runs Tiger Asia; 2012 insider-trading plea (~$44m), barred from outside capital |
| 2013 | Tiger Asia converted to [[archegos|Archegos]] family office (~$200m principal) |
| Late 2020 | Heavy buying via [[total-return-swap|TRS]]/[[contract-for-difference|CFD]] inflates VIAC, DISCA, China ADRs; gross exposure builds toward ~$35bn |
| Mon Mar 22 | ViacomCBS announces $3bn secondary offering |
| Tue Mar 23 | Secondary priced at ~$85 (vs ~$100 prior week); VIAC −9% |
| Wed-Thu Mar 24-25 | Basket-wide mark-to-market decline breaches margin across multiple primes; Archegos cannot meet calls |
| Thu Mar 25 | Prime brokers convene; CS/Nomura want staged standstill, GS/MS refuse |
| Fri Mar 26 | GS and MS dump ~$20bn of underlying in block sales at 10-30% discounts; VIAC −27%, DISCA −27%, TME −34%, BIDU −14% |
| Mon Mar 29 | CS and Nomura disclose preliminary losses; Nomura −16% on the day |
| Apr 2022 | SEC civil + DOJ criminal charges against Hwang and Halligan |
| Jul 2024 | Hwang convicted on 10 of 11 counts; Halligan on 3 |
| Nov 2024 | Hwang sentenced to 18 years |

## Bank Losses

| Bank | Disclosed Loss | Notes |
|------|----------------|-------|
| credit-suisse | ~$5.5 billion | Largest single loss; contributed to the bank's 2023 [[credit-suisse-collapse-2023|collapse and forced merger with UBS]] |
| nomura | ~$2.9 billion | Slow to exit; extensive internal review |
| morgan-stanley | ~$911 million | Sold aggressively into the unwind; loss relatively contained |
| ubs | ~$774 million | Disclosed in Q1 2021 results |
| [[mufg]] | ~$300 million | Smaller TRS book |
| [[mizuho]] | ~$90 million | |
| goldman-sachs | "immaterial" | First out the door; blocks executed near best levels |
| wells-fargo | "no loss" | Fully collateralized; unwound at no cost |

Aggregate industry loss: roughly **$10-12 billion**.

## Prime-Broker Risk-Management Failures

- **Initial margin too low**: Credit Suisse had reportedly extended TRS margin as low as 10% against a concentrated single-name book. Industry norms post-LTCM for similar concentrations are 25-50%.
- **No variation-margin discipline**: CS had tolerated past under-collateralization and had not enforced its own right to demand additional margin days or weeks earlier.
- **Single counterparty, multi-name concentration not priced**: Standard VaR models treated each position as if independent; Archegos's whole book was essentially one long-beta, long-China-ADR bet.
- **Siloed information**: CS's synthetic prime desk, cash-prime desk, and risk committee did not share a unified view of Archegos exposure until the week of the blow-up.
- **Competitive client retention**: CS reportedly did not want to lose fees to aggressive rivals (Goldman had onboarded Archegos in 2020 despite the Tiger Asia history) and so declined to push for higher margin.

Credit Suisse commissioned an external report by **Paul, Weiss** (published July 2021) that ran 165 pages and was brutal: it described "a fundamental failure of management and controls" inside the bank's investment-banking and risk-management functions.

## Regulatory and Legal Aftermath

- **SEC civil charges (April 2022)**: Hwang and CFO Patrick Halligan charged with racketeering, securities fraud, and market manipulation. DOJ filed parallel criminal charges.
- **Conviction (July 2024)**: A Manhattan federal jury convicted Hwang on 10 of 11 counts including securities fraud, wire fraud, and market manipulation; Halligan convicted on three counts.
- **Sentencing (November 2024)**: Hwang sentenced to **18 years** in federal prison -- one of the longest white-collar sentences in recent memory.
- **Rule 10B-1** (proposed SEC, 2022 -> final form stalled): would require disclosure of large security-based-swap positions, directly targeting the Archegos invisibility gap.
- **Basel / FSB**: Financial Stability Board issued 2021-2023 guidance urging banks to improve counterparty-credit-risk management for non-bank financial intermediaries (NBFIs).

## Connection to Credit Suisse's Demise

Archegos is widely cited as one of two catastrophic events ([[greensill-capital-collapse-2021|Greensill]] being the other, weeks earlier) that destroyed CS's remaining credibility with depositors, counterparties, and the Swiss regulator FINMA. CS's stock never recovered its March 2021 level. By March 2023, a run on deposits forced FINMA and the Swiss government to engineer an emergency acquisition by ubs (see [[credit-suisse-collapse-2023]]).

## How People Made Money

Public reporting focuses on the $10-12B aggregate bank loss, but several distinct pools of capital profited — directly or indirectly — from the cascade. The full taxonomy of winners:

### 1. Block-trade buyers ($1-3B+ pool)

The largest profit pool. Goldman Sachs and Morgan Stanley unloaded ~$20B of Archegos's underlying stock in coordinated block sales **Friday March 26, 2021**, priced at **10-30% discounts** to Thursday's close:

| Stock | Thu 25 close | Block-trade level | Discount |
|-------|--------------|--------------------|----------|
| ViacomCBS (VIAC) | ~$66 | ~$48 | -27% |
| Discovery (DISCA) | ~$57 | ~$42 | -27% |
| Baidu (BIDU) | ~$252 | ~$216 | -14% |
| Tencent Music (TME) | ~$24 | ~$16 | -34% |
| GSX Techedu | ~$93 | ~$32 | -65% (continuing) |

Buyers — Citadel, Millennium, Point72, BlackRock event-driven funds, Renaissance, and opportunistic mutual funds — absorbed the supply. Holders into the 30-90 day partial recovery captured 20-50% gross. The disciplined version: buy the discount, hedge index/sector beta, hold to convergence. Adapted into a repeatable strategy: see [[block-trade-flipping-arbitrage]].

### 2. First-mover prime brokers (~$5B avoided losses)

By moving Friday morning, goldman-sachs and morgan-stanley turned what would have been multi-billion-dollar losses into "immaterial" / $911M results — by selling at -10-20% rather than at -40-60% the following Monday. The prisoner's-dilemma payoff differential between first-mover and last-mover banks was approximately **$5B**. Wells Fargo had margined Archegos appropriately and unwound at $0 cost. Generalized as: see [[prime-broker-cascade-trading]].

### 3. Muddy Waters / Carson Block on GSX Techedu (~$200M+ on this name alone)

Muddy Waters Research had published a fraud thesis on GSX Techedu (later Gaotu Techedu) in **May 2020**, alleging up to 70% of revenue was fabricated. GSX was a major Archegos position; the unwind crashed it from ~$130 (late February) to ~$16 by early April — a **88% drop in five weeks**. Muddy Waters' largest 2021 winner, validated by the forced-seller cascade. See 2020-05-muddy-waters-gsx-short.

### 4. Single-name volatility longs

VIAC 1-month implied vol went from ~40% to **200%+** in a week. Long straddles and risk-reversals on Hwang's concentrated basket printed. Optiver, Citadel Securities, and SIG were major market-maker winners; directional vol funds (Capstone, Universa) profited on the long-gamma side.

### 5. Short Credit Suisse (largest single trade-thesis pool)

Archegos was the proximate trigger of CS's 2-year decline. Shorting CS equity from CHF 12 (Mar 22, 2021) into the **March 2023 forced UBS merger at CHF 0.76** delivered ~94% returns. CS AT1 bondholders were wiped to zero in the merger — CDS holders made bank. The "this bank cannot risk-manage" thesis paid in three legs:

- 2021: -25% in the months following Archegos.
- 2022: Greensill aftermath, deposit outflows.
- 2023: Bank-run collapse → forced merger; AT1 wipeout. See [[credit-suisse-collapse-2023]].

### 6. Short Nomura

Nomura -16% on March 29, 2021. Multi-month decline followed. Smaller in absolute terms than the CS short but cleaner.

### 7. The "Tiger Cub overhang" trade

Hwang was a [[tiger-management|Tiger Cub]] (alumnus of Julian Robertson's Tiger Management). Sophisticated PMs read Archegos as evidence that other Tiger Cub funds — Coatue, Lone Pine, Tiger Global, Maverick, Viking — ran similarly concentrated tech books. Shorting their crowded long-tech names through 2021-2022 (especially Tiger Global's late-stage tech book) became a separate multi-billion-dollar trade as the 2022 tech drawdown hit Tiger Cub portfolios harder than the broader market.

### 8. Insider leak from the March 25 prime-broker call

The Thursday meeting where CS/Nomura wanted standstill and GS/MS refused leaked into Asia trading hours. Hedge funds that pre-positioned shorts in VIAC/BIDU/DISCA Thursday afternoon ahead of Friday's blocks made outsized returns. This was not formally illegal — banks were unwinding a defaulted client — but the asymmetric information access is itself a recurring edge: see [[prime-broker-cascade-trading]].

### 9. Compliance/consulting boom

Promontory Financial Group, Oliver Wyman, and Big-4 prime-brokerage risk-consulting practices saw 2022-2024 revenue spike. Not a trade, but a $300M+ industry windfall.

## Lessons

1. **Family-office exemption is a structural risk gap**: an unregulated pool managing $35B of gross exposure is not materially different from a hedge fund and should not be treated as such by counterparties.
2. **TRS/CFD structures obscure real ownership**: synthetic prime is opaque by design. Banks must model aggregate client concentration regardless of legal form.
3. **Coordinated unwinds require pre-commitment**: the prisoner's-dilemma structure on March 25 guaranteed that early movers won and late movers lost. Post-Archegos, ISDA has floated standardized multi-dealer unwind protocols.
4. **Margin is the only real defense**: no VaR model would have caught this; only robust initial-margin discipline sized to concentrated-book tail risk would have contained it.
5. **Historical red flags matter**: Hwang's 2012 [[tiger-asia]] plea was public. Goldman's 2020 decision to onboard him despite the history was a documented internal debate that risk overrode for revenue.

### Risk taxonomy of the blow-up

| Risk type | How it manifested in Archegos | Generalized lesson |
|-----------|-------------------------------|--------------------|
| [[counterparty-risk\|Counterparty / counterparty-credit risk]] | Primes carried the residual loss once the leveraged client defaulted | Margin sized to a concentrated book's tail, not normal-times VaR, is the only real backstop |
| [[concentration-risk\|Concentration risk]] | ~10 names, one long-beta / long-China-ADR factor bet across the whole book | A single-factor book is one position, not many; correlation collapses diversification in stress |
| Disclosure / transparency gap | TRS hid >5% economic ownership from 13D/13G; no 13F as a family office | Synthetic exposure must be aggregated by economic substance, not legal form (driver of proposed Rule 10B-1) |
| [[leverage\|Leverage]] / margin risk | ~6-7x via 15-20% initial margin; no enforced variation-margin discipline | A loss equal to initial margin wipes the position and pushes the rest onto the broker |
| Coordination / game-theory risk | March 25 prisoner's dilemma; first movers (GS/MS) won, slow movers (CS/Nomura) lost ~$5bn extra | Multi-dealer unwinds need pre-committed protocols, not ad-hoc Thursday-night calls |
| Regulatory-arbitrage risk | Family-office exemption left a $35bn pool effectively unsupervised | Economic size, not entity label, should drive prudential treatment of NBFIs |

## Related

- [[bill-hwang]] -- principal
- [[archegos]] -- family office
- [[total-return-swap]] -- the instrument
- [[prime-broker]] -- counterparty structure
- [[contract-for-difference]] -- sister instrument
- credit-suisse / [[credit-suisse-collapse-2023]] -- downstream consequence
- [[ltcm-collapse-1998]] -- prior prime-broker cascade
- [[concentration-risk]] -- general failure mode
- [[counterparty-credit-risk]] -- core lesson

## Sources

- **Paul, Weiss, Rifkind, Wharton & Garrison**, "Report on Archegos Capital Management" (Credit Suisse Special Committee of the Board of Directors, July 29, 2021) — 165-page external review of CS's risk-management failures.
- **SEC v. Sung Kook (Bill) Hwang et al.**, civil complaint, S.D.N.Y., April 27, 2022 — securities fraud and market manipulation charges.
- **U.S. v. Hwang and Halligan**, DOJ indictment (April 2022) and Manhattan federal jury trial record (verdict July 2024; Hwang sentenced to 18 years, November 2024).
- **Financial Stability Board**, guidance on counterparty credit risk management of non-bank financial intermediaries (2021-2023).
- Contemporaneous reporting: *Wall Street Journal*, *Financial Times*, and Bloomberg coverage of the March 26-29, 2021 block-sale cascade and disclosed bank losses.

_Source-summary pages for these documents are queued in [[raw-source-index]]; the figures above are drawn from the public filings and reports named here._
