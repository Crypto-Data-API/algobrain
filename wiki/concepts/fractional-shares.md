---
title: "Fractional Shares"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [stocks, market-microstructure, education]
aliases: ["Fractional Share", "Fractional Investing", "Dollar-Based Investing", "fractional shares"]
domain: [market-microstructure]
prerequisites: ["[[stocks]]", "[[liquidity]]"]
difficulty: beginner
related: ["[[stocks]]", "[[dollar-cost-averaging]]", "[[dividends]]", "[[market-orders-vs-limit-orders]]", "[[robinhood-vs-interactive-brokers]]", "[[etf]]", "[[stock-split]]", "[[liquidity]]"]
---

# Fractional Shares

A **fractional share** is a portion of a single share of stock or an [[etf|ETF]] — less than one whole unit. Instead of buying shares by quantity ("buy 1 share"), brokers that support fractional investing let you buy by **dollar amount** ("invest $25"), and the order is filled as whatever fraction of a share that dollar amount buys. Fractional trading became a mainstream U.S. retail feature around 2019–2020 and is now offered by most major brokers. It exists to solve a simple problem: when a single share costs hundreds or thousands of dollars, a small investor would otherwise be priced out or unable to diversify.

## How It Works

- **Dollar-based orders.** You specify a dollar amount; the broker computes the fraction. Putting $50 into a stock trading at $400 buys **0.125 shares**.
- **The broker holds the inventory.** Exchanges trade in whole shares, so the broker typically buys whole shares for its own book and allocates fractions to customer accounts internally. Your fraction is a beneficial interest the broker tracks; it is not a separate exchange-listed instrument.
- **Pro-rated economics.** Your fraction earns the same *percentage* return as a whole share. [[dividends]] are paid in proportion — owning 0.125 shares pays 12.5% of the per-share dividend (often rounded to the nearest cent).
- **Reinvestment fit.** Fractional support is what makes automatic [[dividends|dividend reinvestment (DRIP)]] and recurring [[dollar-cost-averaging|dollar-cost-averaging]] work cleanly, because dividends and fixed contributions rarely equal a whole-share price.

## Broker Adoption

Fractional investing went mainstream through a wave of broker launches:

- **Robinhood** rolled out fractional shares in late **2019**, popularizing dollar-based orders for a young retail base.
- **Charles Schwab** launched **"Stock Slices"** in June **2020**, initially limited to S&P 500 companies with a **$5** minimum per slice.
- **Fidelity** introduced **"Stocks by the Slice"** (as little as **$1**) in early **2020**.
- **Interactive Brokers**, **SoFi**, **Webull**, and others followed. The trigger was the **October 2019 shift to zero commissions** across major US brokers: once per-trade fees vanished, filling and tracking tiny fractional orders became economical.

## Why It Matters to a Retail Stock Investor

- **Access to expensive stocks.** A single share of a high-priced company can cost hundreds or thousands of dollars; fractional shares let you own a slice with as little as $1–$5.
- **Precise [[diversification]] on a small budget.** With $100 you can spread across ten names by buying $10 fractions of each, rather than being forced into one cheap stock.
- **Clean automation.** Recurring fixed-dollar investing and dividend reinvestment don't leave awkward cash remainders — the whole contribution gets invested.
- **Lower behavioral friction.** Investing "$50 a paycheck" is easier to stick to than computing share counts, which supports disciplined [[dollar-cost-averaging]].

## How to Use It

1. **Switch your order entry to dollars** where the broker offers it, and confirm the fraction it implies.
2. **Use it for accumulation, not active trading.** Fractional shares shine for steady buying and DRIP; they are less suited to fast in-and-out trading because of the order-type limits below.
3. **Pair with recurring buys** to automate [[dollar-cost-averaging]] and dividend reinvestment.

## Limitations and Caveats

- **Order types are restricted.** Fractional orders are commonly **market orders only**, filled at the next available price; many brokers do not allow limit, stop, or extended-hours fractional orders. (See [[market-orders-vs-limit-orders]] for why this matters.)
- **Not transferable in kind.** If you move brokers, fractional positions usually **cannot be transferred** — the broker liquidates them for cash (a potential taxable event), and only whole shares transfer via ACATS.
- **No voting on the fraction.** Fractional holders generally cannot vote the fractional portion in shareholder matters; voting and proxy rights typically attach to whole shares.
- **Broker-dependent and less liquid to exit.** Because the fraction is an internal book entry, your ability to sell depends on the broker's program; it is not independently listed.
- **Rounding.** Dividends and share quantities are rounded (often to the cent or to a set number of decimal places), so tiny amounts can round to zero.
- **Availability varies.** Not every security is eligible for fractional trading at every broker.
- **Cost basis and tax lots.** Each fractional purchase still creates a tax lot; the broker tracks **cost basis pro-rata** on the fraction. A cash-out at a transfer (rather than an in-kind move) can **realize a capital gain or loss**, and frequent tiny reinvestments can generate many small lots that complicate tax reporting and wash-sale tracking.

## Fractional Shares vs Stock Splits

Both make a high-priced stock more accessible, but differently. A [[stock-split]] divides each existing share into more shares for *all* holders, lowering the per-share price mechanically without changing total value. Fractional shares leave the share price untouched and instead let an individual buyer own a *part* of one share. After fractional investing became widespread, the affordability motive for stock splits weakened — though companies still split for other reasons (liquidity, optics, options-market mechanics).

## Hypothetical Example

A new investor has **$120** and wants exposure to three fictional companies whose shares trade at **$400 (Acme), $300 (Globex), and $50 (Initech)**.

- Without fractional shares: $120 buys **0 shares of Acme, 0 of Globex, and 2 of Initech** — no diversification, forced into the cheapest name.
- With fractional shares: she invests **$40 each** → **0.10 Acme + 0.133 Globex + 0.80 Initech**, holding all three in proportion to her plan.
- A quarter later Acme pays a **$2.00 per-share** dividend; her 0.10 share earns **$0.20**, automatically reinvested into another fractional sliver.

All figures are illustrative, not real quotes. The point: fractional shares converted a budget too small for even one share of the priciest name into a diversified, automatable position.

## Related

- [[stocks]] — the underlying instrument being subdivided
- [[dollar-cost-averaging]] — the strategy fractional shares enable cleanly
- [[dividends]] — paid pro-rata on fractional holdings; powers DRIP
- [[market-orders-vs-limit-orders]] — why fractional orders are usually market orders
- [[robinhood-vs-interactive-brokers]] — brokers differ in fractional support and rules
- [[etf]] — fractional buying applies to ETFs too
- [[stock-split]] — the older mechanism for making shares affordable

## Sources

- U.S. Securities and Exchange Commission, investor education on fractional shares and dollar-based investing (investor.gov)
- FINRA, investor guidance on fractional shares and brokerage account transfers (ACATS) (finra.org)
- Broker disclosures on fractional-share programs (e.g. Fidelity, Schwab, Robinhood help-center documentation)
