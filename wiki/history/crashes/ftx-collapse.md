---
title: "FTX Collapse"
type: news
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [history, crashes, crypto, exchange]
event_date: 2022-11-11
markets_affected: [crypto]
impact: high
verified: true
sources_count: 0
related: ["[[binance]]", "[[solana]]", "[[alameda-research]]", "[[sam-bankman-fried]]", "[[ftt]]", "[[contagion]]", "[[bank-run]]", "[[counterparty-risk]]", "[[liquidity-risk]]"]
---

# FTX Collapse

The collapse of FTX in November 2022 was one of the most dramatic and consequential failures in the history of [[cryptocurrency]]. What had been the second-largest crypto exchange by volume, valued at $32 billion just months earlier, imploded in less than a week when it was revealed that billions of dollars in customer funds had been misappropriated. The event deepened the ongoing [[crypto-winter]], triggered widespread [[contagion]], and led to the criminal conviction of founder [[sam-bankman-fried]]. At its core it was not a market crash but a **fraud** — a customer [[bank-run]] that exposed the misuse of deposits — making it the crypto-era analogue of lehman-brothers crossed with a Madoff-style governance failure.

## Background: The Rise of FTX and SBF

Sam Bankman-Fried (commonly known as SBF) founded FTX in 2019 after previously founding [[alameda-research]], a quantitative [[crypto-trading]] firm, in 2017. FTX grew explosively by offering innovative products including [[futures]], [[options]], leveraged tokens, and prediction markets. The exchange was headquartered in the Bahamas and attracted high-profile investors including Sequoia Capital, SoftBank, and the Ontario Teachers' Pension Plan.

SBF cultivated an image as a wunderkind philanthropist committed to "effective altruism." He became a prominent political donor and a frequent presence in Washington, D.C., lobbying for crypto regulation that many critics later noted would have benefited FTX's competitive position. At its peak, FTX had naming rights to the Miami Heat's arena and was endorsed by celebrities including Tom Brady and Larry David.

Critically, FTX and [[alameda-research]] maintained an opaque and deeply intertwined relationship. Alameda served as a major [[market-maker]] on the FTX platform and, as would later be revealed, enjoyed special privileges including an effectively unlimited line of credit funded by FTX customer deposits.

## Timeline at a Glance

| Date | Event |
|---|---|
| 2017 | SBF founds [[alameda-research]] (quant trading firm) |
| 2019 | SBF founds FTX exchange; issues the [[ftt]] exchange token |
| Jan 2022 | FTX valued at $32B in a funding round — near its peak |
| **Nov 2, 2022** | CoinDesk reports [[alameda-research]]'s balance sheet is dominated by [[ftt]] — solvency hinges on a token FTX itself controls |
| **Nov 6, 2022** | [[binance|Binance]]'s CZ announces it will dump its ~$580M [[ftt]] holdings; panic begins |
| **Nov 7-8, 2022** | Customer [[bank-run]]: ~$6B in withdrawal requests in 72 hours; FTX halts withdrawals (Nov 8) |
| **Nov 8, 2022** | [[binance|Binance]] signs a non-binding letter of intent to acquire FTX |
| **Nov 9, 2022** | Binance walks away after due diligence; FTX is insolvent |
| **Nov 11, 2022** | FTX, FTX.US, [[alameda-research]] + ~130 entities file Chapter 11; SBF resigns; John J. Ray III appointed |
| **Dec 12, 2022** | SBF arrested in the Bahamas; later extradited to the US |
| Dec 2022 - early 2023 | Ellison, Wang, Singh plead guilty and cooperate |
| **Nov 2, 2023** | SBF **convicted on all 7 counts** of fraud and conspiracy after a five-week trial |
| **Mar 28, 2024** | SBF **sentenced to 25 years** in federal prison |

## The Unraveling: A Timeline (detail)

- **November 2, 2022**: CoinDesk published a bombshell article revealing that [[alameda-research]]'s balance sheet was heavily concentrated in [[ftt]] — the native token issued by FTX itself. Of Alameda's $14.6 billion in assets, a massive portion consisted of FTT and other illiquid, FTX-affiliated tokens. This meant Alameda's apparent solvency depended on the value of a token controlled by its sister company.
- **November 6, 2022**: Changpeng Zhao (CZ), CEO of rival exchange [[binance]], tweeted that Binance would liquidate its entire [[ftt]] holdings (worth approximately $580 million), citing "recent revelations." This triggered panic among FTX users — a public match dropped on a pile of dry kindling.
- **November 7-8, 2022**: A classic [[bank-run]] ensued. FTX faced approximately $6 billion in withdrawal requests in 72 hours. On November 8, FTX halted withdrawals.
- **November 8, 2022**: [[binance]] signed a non-binding letter of intent to acquire FTX, briefly calming markets. However, after reviewing FTX's books, Binance withdrew the offer within 24 hours, citing concerns about mishandled customer funds and pending regulatory investigations.
- **November 11, 2022**: FTX, FTX.US, [[alameda-research]], and approximately 130 affiliated entities filed for Chapter 11 bankruptcy. SBF resigned as CEO and was replaced by John J. Ray III, the restructuring specialist who had overseen Enron's bankruptcy. Ray would later testify that FTX represented the worst case of corporate failure he had ever seen.
- **December 12, 2022**: SBF was arrested in the Bahamas at the request of U.S. prosecutors and subsequently extradited to the United States.
- **November 2, 2023**: After a five-week trial, SBF was convicted on all seven counts of fraud and conspiracy.
- **March 28, 2024**: SBF was sentenced to 25 years in federal prison.

## The Fraud: What Actually Happened

Investigations revealed that FTX had secretly funneled approximately $8 billion in customer deposits to [[alameda-research]] to cover trading losses, venture investments, political donations, and personal expenditures. Alameda had a hidden "backdoor" in FTX's systems that allowed it to borrow customer funds without proper accounting or disclosure.

There were no functioning risk controls, no board of directors in any meaningful sense, and corporate funds were used to purchase personal real estate and make political contributions. Several key executives — including Caroline Ellison (CEO of Alameda), Gary Wang (co-founder and CTO of FTX), and Nishad Singh (head of engineering) — pleaded guilty and cooperated with prosecutors.

## Causes → Consequences

The collapse was the predictable end-state of a chain of structural flaws meeting a trigger:

| Root cause | Mechanism | Consequence |
|---|---|---|
| FTX/[[alameda-research]] conflict of interest | Sister trading firm with a backdoor line of credit | Customer deposits silently funded Alameda's losses (~$8B) |
| Collateral was [[ftt]] (a self-issued token) | "Asset" value controlled by the issuer; reflexive | One credibility shock made the balance sheet vaporize |
| No segregation of customer funds | Deposits commingled and lent out | A withdrawal wave instantly exposed the shortfall |
| No governance / risk controls / audit | No board, no CFO, no real books | Fraud went undetected until the run forced disclosure |
| Trigger: CZ's [[ftt]] dump tweet (Nov 6) | Public confidence shock | Customer [[bank-run]] → [[liquidity-risk|liquidity crisis]] → insolvency |
| High leverage and crypto interconnection | Lenders/funds exposed to FTX & FTT | [[contagion]]: BlockFi, Genesis, others failed in turn |

The deep point: FTX was *never* a [[liquidity-risk|liquidity]] problem that became a solvency problem — it was insolvent the whole time because the money was gone. The run merely revealed it. This distinguishes it from a classic illiquidity-driven [[bank-run]] and places it alongside fraud cases, not market accidents.

## Market Impact and Contagion

The collapse sent shockwaves through the entire [[crypto]] ecosystem:

- **[[bitcoin]]** fell from approximately $21,000 to roughly $15,500, hitting its cycle low.
- **[[solana]]** (SOL), closely associated with SBF and FTX/Alameda, crashed over 60% in the weeks following the collapse.
- **FTT** went from approximately $25 to under $1, a near-total loss.
- **[[contagion|Contagion]] spread rapidly**: [[blockfi]], which had significant exposure to FTX, filed for bankruptcy in late November. [[genesis]] Global Capital halted withdrawals and later filed for bankruptcy. [[voyager-digital]], already weakened by the [[terra-luna-collapse-2022]] collapse, saw its acquisition by FTX reversed. The 2022 sequence — [[terra-luna-collapse-2022]] (May) → Three Arrows Capital → Celsius/Voyager → FTX (November) — was a daisy chain of interlinked crypto credit, each failure feeding the next.
- Total [[crypto-market]] capitalization fell below $800 billion, down from nearly $3 trillion at the November 2021 peak.

## Regulatory Fallout

The FTX collapse accelerated regulatory scrutiny of the [[crypto]] industry worldwide. The SEC intensified enforcement actions against exchanges and token issuers. Multiple jurisdictions moved to implement stricter licensing requirements for crypto platforms. The concept of "proof of reserves" — where exchanges publicly verify they hold sufficient assets to cover customer deposits — gained traction, though critics noted that proof of reserves alone does not prove the absence of hidden liabilities.

## Lessons for Traders

The FTX collapse reinforced several critical principles for anyone trading in [[crypto]] or any market:

1. **[[counterparty-risk]] is paramount**: Even the largest, most reputable-seeming institutions can fail. This echoes lessons from lehman-brothers in the [[2008-global-financial-crisis]].
2. **"Not your keys, not your coins"**: Keeping assets in [[self-custody]] wallets eliminates exchange [[counterparty-risk]], a foundational principle of [[crypto]] that many had begun to ignore.
3. **Due diligence on exchanges**: Traders should evaluate an exchange's transparency, regulatory status, proof of reserves, and corporate governance before depositing funds.
4. **Beware of conflicts of interest**: The FTX/Alameda relationship was a massive red flag that many overlooked. When an exchange also runs a proprietary trading firm, the potential for abuse is significant.
5. **Celebrity endorsements mean nothing**: High-profile backers and flashy marketing are not substitutes for sound business practices and [[risk-management]].
6. **[[liquidity-risk]] in a crisis**: When panic sets in, the ability to withdraw funds matters more than any yield or feature an exchange offers. A [[bank-run]] on a leveraged, opaque custodian is a one-way door.
7. **Self-issued tokens are not collateral**: [[ftt]] backing Alameda's balance sheet was reflexive — its value depended on confidence in the very entity it was meant to support. Treat any "asset" the issuer controls as worth near-zero in a stress scenario.
8. **Audited, segregated, regulated > flashy**: The post-FTX flight to qualified custody, proof-of-reserves-plus-liabilities, and regulated venues reflects the real lesson — boring infrastructure beats charismatic founders.

## Related

- [[sam-bankman-fried]], [[alameda-research]], [[ftt]], [[binance]] — the principals and instruments
- [[bank-run]], [[liquidity-risk]], [[counterparty-risk]], [[contagion]] — the mechanisms
- [[terra-luna-collapse-2022]], [[blockfi]], [[genesis]], [[voyager-digital]] — the 2022 contagion chain
- lehman-brothers, [[2008-global-financial-crisis]] — the closest traditional-finance analogues
- [[self-custody]], [[crypto-winter]], [[solana]], [[bitcoin]]

## Sources

- General market knowledge; no specific wiki source ingested yet. Key dated facts (CoinDesk balance-sheet report Nov 2, 2022; Chapter 11 filing Nov 11, 2022; SBF conviction Nov 2, 2023; 25-year sentence Mar 28, 2024) are drawn from the widely documented public record. Customer-shortfall and contagion magnitudes are stated approximately and should be treated as estimates.
