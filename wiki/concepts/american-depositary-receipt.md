---
title: "American Depositary Receipt (ADR)"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [stocks, market-microstructure, regulation, forex]
aliases: ["ADR", "ADRs", "American Depositary Receipt", "American Depositary Receipts", "American Depository Receipt", "ADS", "American Depositary Share"]
related: ["[[stocks]]", "[[over-the-counter-markets]]", "[[nyse]]", "[[nasdaq]]", "[[dividend]]", "[[adr-arbitrage]]", "[[delisting]]", "[[emerging-markets]]"]
domain: [stocks, market-microstructure]
difficulty: beginner
---

An **American Depositary Receipt (ADR)** is a negotiable certificate issued by a US depositary bank that represents ownership of shares in a **foreign company**, allowing those shares to trade on US markets in US dollars. ADRs answer the common ALFRED question *"is this a foreign stock, and how am I actually holding it?"* — when you buy, say, a Chinese or European company on a US exchange, you are usually buying an ADR, not the foreign-listed share itself. The depositary bank holds the underlying foreign shares abroad and issues US-traded receipts against them, handling currency conversion, dividends, and corporate actions on the investor's behalf.

## How an ADR works

1. A US **depositary bank** (e.g., a large custodian bank) buys or holds a block of a foreign company's ordinary shares in the home market.
2. It issues **ADRs** against those shares, each ADR representing a defined number of underlying shares — the **ADR ratio** (e.g., 1 ADR = 2 ordinary shares, or 1 ADR = 0.5 share).
3. The ADRs trade in **US dollars** on a US venue ([[nyse|NYSE]], [[nasdaq|Nasdaq]], or the [[over-the-counter-markets|OTC market]]), settling like any US stock.
4. [[dividend|Dividends]] paid by the foreign company are converted to USD and passed through (net of fees and any foreign withholding tax).

The term **American Depositary Share (ADS)** refers to the underlying share-equivalent; "ADR" technically refers to the certificate, but in practice the terms are used interchangeably.

### ADR vs GDR vs ordinary shares

An ADR is the US-specific form of the broader **depositary receipt** family. A **Global Depositary Receipt (GDR)** works identically but is issued for trading outside the US — typically on the London or Luxembourg exchanges — and is often used to reach European and Asian institutional investors in a single instrument. Both differ from buying the company's **ordinary shares** directly on its home exchange, which requires a broker with access to that market, settlement in the local currency, and local custody. ADRs and GDRs package all of that into a single domestically-settled security; the trade-off is depositary fees and reliance on the sponsor to keep the program running.

## Types and levels

ADRs are categorized as **sponsored** (set up by the foreign company itself, with a single depositary) or **unsponsored** (set up by a bank without the company's involvement; multiple competing receipts can exist). Sponsored ADRs are further graded by level:

| Level | Where it trades | Disclosure / SEC registration | Can it raise capital? |
|---|---|---|---|
| **Level I** | [[over-the-counter-markets|OTC]] only | Minimal; no full SEC reporting | No |
| **Level II** | Listed on [[nyse|NYSE]]/[[nasdaq|Nasdaq]] | Full SEC reporting (Form 20-F) | No |
| **Level III** | Listed on NYSE/Nasdaq | Full SEC reporting + registered offering | Yes — can issue new shares to US investors |

Higher levels mean more disclosure, more liquidity, and a US exchange listing; Level I ADRs are the lightest-touch route and trade [[over-the-counter-markets|over the counter]].

## Why ADRs exist

- **For US investors** — buy foreign companies in USD, in US market hours, through an ordinary brokerage account, with dividends handled domestically — no foreign brokerage, currency account, or local custody needed.
- **For foreign companies** — access deep US capital pools and broaden their shareholder base without a full primary listing in their home structure.
- **Index and access** — many [[emerging-markets|emerging-market]] and European large caps are most easily held by US investors via ADRs.

## What to watch for

- **Currency exposure remains.** Trading in USD does not remove [[forex|FX]] risk. The ADR's value still tracks the foreign share priced in the home currency, so if that currency weakens against the dollar, the ADR falls even if the local share is flat. ADR return ≈ local-share return + currency move.
- **The ADR ratio matters.** Always check how many underlying shares one ADR represents; per-ADR figures (price, dividend, earnings) must be scaled by the ratio to compare with the home-market line.
- **Depositary fees.** Banks charge periodic custody/"pass-through" fees (often a few cents per ADR per year), sometimes netted from dividends — a small but real drag.
- **Dividend withholding.** Foreign governments may withhold tax on dividends before they reach the US holder; recovery depends on tax treaties.
- **Liquidity and the home market.** Level I OTC ADRs can be thin; the "true" price discovery often happens in the home market while it is open, leaving the ADR to gap at the US open.
- **Termination / [[delisting]] risk.** A sponsor can terminate an ADR program, or geopolitical/regulatory action (e.g., audit-compliance disputes) can force [[delisting]], leaving holders to convert into the foreign ordinary shares or be cashed out.

When the ADR and the underlying foreign share drift apart in price after adjusting for the ratio and currency, the gap is closed by traders running [[adr-arbitrage]].

## Hypothetical example

Suppose a fictional Japanese robotics maker, **Sakura Robotics**, has ordinary shares trading in Tokyo at **¥3,000**. A US bank sponsors a Level II ADR with a ratio of **1 ADR = 5 ordinary shares**, so each ADR represents ¥15,000 of stock. At an exchange rate of ¥150 per USD, the ADR should trade near **$100** on the [[nasdaq|Nasdaq]]. If the yen weakens to ¥165 per USD while the Tokyo share price is unchanged, the ADR's fair value falls to about **$90.91** purely from the currency move — illustrating that a US-dollar quote does not insulate the holder from FX risk. If the ADR briefly traded at $95 while the underlying implied $90.91, an [[adr-arbitrage|arbitrageur]] could short the rich ADR and buy the Tokyo shares to capture the gap. (Sakura Robotics is illustrative, not a real company.)

## Related

- [[stocks]] — ADRs are a wrapper around foreign equity
- [[over-the-counter-markets]] — where Level I ADRs trade
- [[nyse]] / [[nasdaq]] — where Level II/III ADRs list
- [[dividend]] — foreign dividends are passed through in USD
- [[adr-arbitrage]] — trading ADR-vs-ordinary price gaps
- [[emerging-markets]] — many EM names are accessed via ADRs
- [[delisting]] — ADR programs can be terminated or forced off-exchange
- [[global-depositary-receipt]] — the non-US sibling of the ADR
- [[forex]] — the currency risk that a USD quote does not remove

## Sources

- US Securities and Exchange Commission, investor bulletin on American Depositary Receipts.
- JPMorgan / BNY Mellon / Citi depositary-receipt program documentation (sponsored vs. unsponsored, Levels I-III, ADR ratios and fees).
- General market knowledge; no specific wiki source ingested yet.
