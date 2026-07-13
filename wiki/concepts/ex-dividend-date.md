---
title: "Ex-Dividend Date"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [valuation, income, stocks, market-microstructure]
aliases: ["Ex-Dividend Date", "Ex Dividend Date", "Ex-Date", "Ex-Dividend", "Ex Dividend", "Ex-Div"]
related: ["[[dividend]]", "[[dividend-yield]]", "[[dividend-capture]]", "[[dividend-arbitrage]]", "[[assignment-risk]]", "[[covered-call]]"]
domain: [market-microstructure, fundamental-analysis]
prerequisites: ["[[dividend]]", "[[stocks]]"]
difficulty: beginner
---

The **ex-dividend date** (or "ex-date") is the first trading day on which a stock trades *without* the right to its next declared [[dividend]]. To receive the dividend, an investor must own the shares before the ex-dividend date; buyers on or after the ex-date are not entitled to that distribution, which instead goes to the seller. On the morning of the ex-date the share price is expected to open lower by approximately the dividend amount, all else equal, because the company's value has fallen by the cash it is about to pay out.

## The four dividend dates

A dividend payment involves four ordered dates:

1. **Declaration date** — the board announces the dividend amount and the record/payment dates.
2. **Ex-dividend date** — the cutoff. Shares trade ex-dividend from this day; the buyer no longer captures the dividend.
3. **Record date** — the date on which the company checks its books to determine registered holders.
4. **Payment date** — the date the cash is actually paid.

Under the U.S. **T+1 settlement** regime (effective May 2024; previously T+2), the ex-dividend date typically falls on the **same business day as the record date**. Because settlement is now one day, an investor who buys on the record date settles too late to be on the books, so the ex-date and record date coincide. Under the old T+2 regime the ex-date was one business day before the record date. (In Australia the [[asx-200|ASX]] uses T+2 settlement, so the ex-date sits before the record date.)

### Timeline at a glance

A representative US (T+1) schedule for a $1.00 quarterly dividend:

| Date | Event | What it means for you |
|---|---|---|
| Mon (e.g. Apr 6) | **Declaration date** | Board declares $1.00, sets record + payment dates |
| Wed (Apr 22) | **Ex-dividend date** | First day trading *without* the dividend; buy *before* today to get paid. Price opens ~$1.00 lower |
| Wed (Apr 22) | **Record date** | Company checks the books (same day as ex-date under T+1) |
| Wed (May 6) | **Payment date** | Cash hits accounts |

The single decision rule: **own the shares at the close of the day *before* the ex-date** to receive the dividend. Buy *on* the ex-date and the dividend goes to the seller.

## The price adjustment

On the ex-date the exchange mechanically reduces the prior close by the dividend when calculating the opening reference price. A stock closing at $100.00 the day before a $1.00 ex-date opens with a $99.00 reference. This is not a loss — a holder gives up $1.00 of share price but receives $1.00 in cash. In practice the *observed* open is noisy: real-world drops tend to be slightly **less** than the full dividend, historically explained by the differential taxation of dividends versus capital gains and by short-term demand from income-seeking buyers. This empirical gap is the basis of the [[dividend-capture]] strategy.

### Worked example — dividend capture

A trader tries to "capture" a $1.00 dividend on a $100 stock ([[dividend-yield|yield]] 1% per quarter):

| Step | Cash flow / price | Note |
|---|---|---|
| Buy 1,000 shares @ $100.00 (cum-dividend) | −$100,000 | Owns shares before the ex-date |
| Ex-date open ~$99.20 (drop slightly < $1.00) | — | Empirical drop here ~$0.80, not the full $1.00 |
| Receive dividend | +$1,000 | $1.00 × 1,000 shares |
| Sell 1,000 shares @ $99.20 | +$99,200 | Realises an $0.80/share *capital loss* |
| **Gross result** | **+$200** | Dividend $1,000 − capital loss $800 |
| Less round-trip [[spread\|bid-ask spread]] (~$0.05/sh) | −$100 | Crossing the spread twice |
| Less commissions / slippage | −$X | Often eats most of the rest |
| **Tax: dividend taxed as ordinary income** | −$Y | Capture trade fails the [[qualified-dividends\|60-day holding rule]] |

The headline math looks like a free $200, but the *observed* sub-full-dividend drop is exactly the variable that makes or breaks it: if the stock had instead opened at $99.00 (full drop), the gross capture would be **zero** before costs. Net of the spread, commissions, slippage, and the loss of [[qualified-dividends|qualified-dividend]] tax treatment, the expected edge is thin and frequently *negative* — which is why dividend capture is more cautionary tale than reliable strategy. See [[dividend-capture]] and [[dividend-arbitrage]].

## Trading relevance

- **Dividend capture / arbitrage.** Traders attempt to buy just before the ex-date, collect the dividend, and sell on or after the ex-date, hoping the price recovers more than the after-tax dividend is worth. Net of taxes, the bid-ask [[spread]], and the holding-period rules for [[qualified-dividends|qualified-dividend]] treatment, the edge is thin and frequently negative — see [[dividend-capture]] and [[dividend-arbitrage]].
- **Options early assignment.** The ex-date is the single most important date for short-call risk. A short in-the-money [[call-option]] whose extrinsic value is less than the upcoming dividend is a prime candidate for **early [[assignment-risk|assignment]]** the day before the ex-date, as the long-call holder exercises to capture the dividend. This is the central hazard for [[covered-call]] writers and short-call spreads. See [[assignment-risk]] and [[cum-ex-dividend-stripping]].
- **Options pricing.** Expected dividends are embedded in forward prices and therefore in put-call parity: higher expected dividends raise put prices and lower call prices for [[equity-options]]. Index [[spx-options|SPX]] and single-name chains price the dividend stream into the forward.
- **Index and ETF mechanics.** Total-return indices reinvest dividends on the ex-date; price-return indices do not, which is why a price index gaps down on heavy ex-date days. [[etf|ETF]] distributions follow the same four-date structure.
- **Dividend reinvestment.** Long-term holders on a [[drp|dividend reinvestment plan (DRP)]] don't see the ex-date drop as a loss at all — the cash is automatically used to buy more shares, compounding the position. The ex-date drop and the new shares net out, and the [[dividend-yield|yield]] is harvested as growth rather than income.

### How traders use the ex-date

| Participant | What they do around the ex-date |
|---|---|
| **Long-term / income investor** | Largely ignores it; collects the dividend or reinvests via [[drp\|DRP]]. The ex-date drop is offset by the cash |
| **Dividend-capture trader** | Buys cum-dividend, sells ex; chases the sub-full-dividend drop — see the worked example above |
| **[[covered-call\|Covered-call]] / short-call writer** | Monitors the ex-date as the prime early-[[assignment-risk\|assignment]] window; may roll or close ITM short calls beforehand |
| **Options market-maker** | Prices the expected dividend into the forward, [[put-call-parity\|put-call parity]], and early-exercise models |
| **Index / ETF arbitrageur** | Tracks heavy ex-date days that gap a price index and the reinvestment mechanics of total-return products |

## Common pitfalls

- Believing the ex-date drop is "free money" — the price adjustment offsets the cash.
- Forgetting the [[qualified-dividends|holding-period rule]]: in the U.S. a dividend is only "qualified" (taxed at the lower long-term rate) if the share is held more than 60 days in the 121-day window around the ex-date; dividend-capture trades usually fail this test and are taxed as ordinary income.
- Ignoring that special/large dividends can trigger options **contract adjustments** rather than the standard price gap.

## Related

- [[dividend]]
- [[dividend-yield]]
- [[dividend-capture]]
- [[dividend-arbitrage]]
- [[cum-ex-dividend-stripping]]
- [[assignment-risk]]
- [[covered-call]]
- [[equity-options]]
- [[dividend-yield]]
- [[drp]]
- [[qualified-dividends]]
- [[put-call-parity]]

## Sources

- U.S. SEC Investor Bulletin, "Ex-Dividend Dates: When Are You Entitled to Stock and Cash Dividends," sec.gov
- FINRA, "Understanding the Ex-Dividend Date," finra.org
- DTCC / SEC, T+1 settlement transition (effective 28 May 2024) — alignment of ex-date and record date
- ASX, "Dividends and the ex-dividend date," asx.com.au (T+2 settlement)
- Elton & Gruber, "Marginal Stockholder Tax Rates and the Clientele Effect," *Review of Economics and Statistics* (1970) — empirical ex-date price drop less than the dividend
