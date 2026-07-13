---
title: "T+1 Settlement"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [market-microstructure, stocks, liquidity, regulation]
aliases: ["T+1 Settlement", "T+1", "T plus 1", "T+2 Settlement", "T+2", "Settlement Cycle", "Settlement Date", "Trade Date", "Settlement Period"]
domain: [market-microstructure]
prerequisites: ["[[settlement-risk]]", "[[counterparty-risk]]"]
difficulty: beginner
related: ["[[settlement-risk]]", "[[counterparty-risk]]", "[[ex-dividend-date]]", "[[securities-lending]]", "[[short-selling]]", "[[pattern-day-trader-rule]]", "[[market-hours]]", "[[asx]]"]
---

**Settlement** is the moment a trade is finalised: the buyer's cash is exchanged for the seller's securities and ownership is officially transferred on the books of the clearing system. The settlement cycle is written as **T+n**, where **T** is the **trade date** (the day the order executes) and **n** is the number of business days until the transfer completes. Since **28 May 2024** the standard cycle for US stocks, ETFs, corporate bonds, and most other securities is **T+1** — one business day after the trade. The previous standard was **T+2**.

## Trade date vs settlement date

When you buy a stock, two distinct dates are created:

- **Trade date (T)** — the day your order matches a counterparty and the price, quantity, and obligation are locked in. Your broker shows the position immediately, and you bear the price risk from this moment.
- **Settlement date (T+1)** — the next business day, when the cash actually leaves your account and the shares are legally delivered through the clearing and depository system (in the US, the DTCC's NSCC and DTC subsidiaries).

The gap exists because the plumbing — netting thousands of offsetting trades, moving cash between banks, and updating ownership records — takes time. **Business days only count**: a trade on Friday settles Monday (T+1), and weekends and market holidays are skipped. See [[market-hours]].

## The T+1 timeline

| Day | Event |
|---|---|
| **Monday (T)** | You buy 100 shares. Position appears in your account; you owe the cash |
| **Tuesday (T+1)** | Cash debited, shares delivered, trade legally settled |

If Monday were the day before a holiday, settlement would roll to the next business day.

## How the cycle has shortened over time

The settlement cycle has been compressed repeatedly as technology replaced paper certificates and manual processing:

| Era | Cycle | Note |
|---|---|---|
| Pre-1995 (US) | **T+5** | Paper certificates physically delivered |
| 1995–2017 | **T+3** | First major compression |
| Sept 2017 – May 2024 | **T+2** | SEC amendment to Rule 15c6-1 |
| **28 May 2024 onward** | **T+1** | Current US/Canada/Mexico standard |

The SEC adopted the move to T+1 in February 2024 (amending Rule 15c6-1); Canada and Mexico transitioned on the same week. The European Union, the United Kingdom, and Switzerland have announced a coordinated move to T+1 targeted for **October 2027**.

## Why a shorter cycle matters

- **Less [[counterparty-risk|counterparty risk]] and [[settlement-risk|settlement risk]].** The shorter the window between trade and settlement, the less time for either side (or the clearing house) to default while the trade is "in flight." This was a central lesson of the March 2020 volatility and the January 2021 meme-stock episode, where clearing-house margin spiked because of the two-day exposure.
- **Lower clearing margin.** Brokers post collateral to the clearing house against unsettled trades; halving the window roughly halves the time that capital is tied up.
- **Faster access to cash and securities.** Sale proceeds are available a day sooner.
- **Tighter operational tolerances.** Trade allocation, confirmation, and FX funding must now happen on trade date ("T+0 affirmation"), which is hardest for overseas investors who must source US dollars across time zones in a single day.

## Settled cash, free-riding, and cash accounts

In a **cash account** (not a margin account), you must pay for a purchase with **settled funds**. Two rules flow from the settlement cycle:

- **Good-faith violation / free-riding** — buying a stock and selling it before the original purchase has settled, then withdrawing the proceeds, can trigger a violation and a 90-day restriction. T+1 shortens but does not eliminate this constraint.
- **Day-trading and margin** are governed separately by the [[pattern-day-trader-rule|pattern day trader rule]], which depends on account equity rather than the settlement cycle.

## Settlement and related mechanics

- **[[ex-dividend-date|Ex-dividend dates]].** Under T+1 the ex-dividend date now typically falls on the **same business day as the record date** (under T+2 the ex-date was one day earlier). To receive a dividend you must own the shares before the ex-date, because a purchase on the record date would settle too late to put you on the company's books. See [[ex-dividend-date]].
- **[[short-selling|Short selling]] and [[securities-lending|securities lending]].** A short seller must deliver borrowed shares by the settlement date; failure to deliver creates a "fail," and persistent fails feed the SEC's Reg SHO threshold lists. A compressed cycle gives stock-loan desks less time to locate and recall shares.
- **Failed trades.** If the seller cannot deliver by T+1, the trade "fails to settle" and buy-in procedures may follow.

## Other markets

- **Australia ([[asx|ASX]])** settles equities on **T+2**, so an ASX ex-dividend date sits one business day *before* the record date — the mirror of the US T+1 alignment.
- **India** moved its main equity segment to **T+1** by January 2023 (ahead of the US) and has piloted an **optional T+0 (same-day)** settlement track.
- **FX spot** conventionally settles **T+2**, which creates a funding mismatch for foreign investors buying US stocks that now settle in one day.

## Practical takeaways for dashboard users

- A position you buy today is **yours immediately for price purposes**, but the cash and legal transfer complete the **next business day**.
- **Sale proceeds settle T+1** — plan around that if you need the cash or want to redeploy it into a different security from a cash account.
- The **ex-dividend date** logic changed with T+1: own the shares **before** the ex-date (now usually equal to the record date) to be paid.
- **Holidays and weekends extend settlement** because only business days count.

## Related

- [[settlement-risk]] — the core risk the cycle is designed to limit
- [[counterparty-risk]] — exposure while a trade is unsettled
- [[ex-dividend-date]] — alignment of ex-date and record date under T+1
- [[securities-lending]] — short sellers must deliver by settlement
- [[short-selling]] — fails-to-deliver and Reg SHO
- [[pattern-day-trader-rule]] — the separate constraint on day trading
- [[market-hours]] — business-day counting and holidays
- [[asx]] — the T+2 contrast in Australia

## Sources

- U.S. SEC, "SEC Finalizes Rules to Reduce Risks in Clearance and Settlement" / final rule amending Rule 15c6-1 to shorten the standard settlement cycle to T+1 (adopted February 2024, effective 28 May 2024), sec.gov.
- DTCC, T+1 settlement transition resources and industry implementation playbook, dtcc.com.
- SEC Investor.gov, "Trade Execution: Settlement Dates" investor education.
- ASX, settlement and clearing (CHESS, T+2) documentation, asx.com.au.
- European securities regulators (ESMA) and UK/EU announcements of a coordinated T+1 move targeted for October 2027.
