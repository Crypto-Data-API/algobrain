---
title: "Forex Markets"
type: index
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [forex, markets, index]
---

# Forex Markets

The hub for foreign exchange — currency pairs, central-bank policy, market structure, and global macro dynamics. Forex (FX) is the largest financial market in the world, with roughly **$9.6 trillion in daily OTC turnover** as of the April 2025 BIS [[bank-for-international-settlements|Triennial Central Bank Survey]] (up ~28% from $7.5 trillion in 2022). It runs **24 hours a day, five days a week** across the Tokyo, London, and New York sessions, with peak liquidity during the London–New York overlap.

Forex is driven by macroeconomic fundamentals: interest-rate differentials, inflation and employment data, trade balances, and central-bank forward guidance. Major pairs dominate volume while exotics offer wider spreads and higher [[volatility]]. [[carry-trade|Carry]], momentum, and mean-reversion all have long track records in currencies. Unlike equities, FX is a decentralised **over-the-counter** market with no single exchange — a tiered network of interbank dealers, prime brokers, ECNs, and retail brokers.

## How a Quote Works

Every FX price is a **pair**: a *base* currency priced in terms of a *quote* currency. In EUR/USD = 1.0850, one euro (base) costs 1.0850 US dollars (quote). Buying the pair means buying the base and selling the quote.

| Term | Definition | Example |
|------|------------|---------|
| **Pip** | The standard smallest price increment — the 4th decimal for most pairs, the 2nd decimal for JPY pairs | EUR/USD 1.0850 → 1.0851 = 1 pip; USD/JPY 150.20 → 150.21 = 1 pip |
| **Pipette** | A fractional pip (5th decimal) quoted by many brokers | 1.08505 |
| **Spread** | Ask minus bid, the dealer's cost of execution, measured in pips | 1.0850 / 1.0851 = 1-pip spread |
| **Lot** | Standardised trade size | Standard = 100,000 units; mini = 10,000; micro = 1,000 |
| **Pip value** | Cash value of one pip for a given lot size | ~$10 per pip on a standard EUR/USD lot |

## Pair Categories

| Category | What it is | Examples | Characteristics |
|----------|------------|----------|-----------------|
| **Majors** | Most-traded pairs, all vs the [[us-dollar]] | [[eurusd\|EUR/USD]], [[usdjpy\|USD/JPY]], GBP/USD, USD/CHF, AUD/USD, USD/CAD | Deepest liquidity, tightest spreads |
| **Crosses (minors)** | Pairs without USD | EUR/GBP, EUR/JPY, GBP/JPY, AUD/JPY | Wider spreads; derived from two USD legs |
| **Exotics** | Major vs an emerging-market currency | USD/TRY, USD/ZAR, USD/MXN, USD/INR | Wide spreads, high volatility, political/headline risk |

## Leverage, Margin, and Risk

FX is traded on [[margin]] with substantial [[leverage]] — institutional players access very high effective leverage, while retail leverage is capped by regulators (e.g., 30:1 on majors in the EU/UK/Australia, 50:1 in the US). Leverage magnifies both gains and losses: a 1% adverse move on a 50:1 position wipes out half the posted margin. This is the single biggest reason inexperienced retail FX traders lose money, and disciplined [[position-sizing]] and [[stop-loss]] use are essential.

### Worked example (illustrative)

A trader buys **1 standard lot** of EUR/USD (100,000 units) at 1.0850, expecting the euro to strengthen.

- **Pip value**: 100,000 × 0.0001 = $10 per pip.
- If EUR/USD rises to 1.0900 (+50 pips), profit = 50 × $10 = **+$500**.
- If it falls to 1.0820 (−30 pips), loss = 30 × $10 = **−$300**.
- At 30:1 leverage the required margin is ~$108,500 / 30 ≈ **$3,617**, so the $300 loss is ~8% of margin from a move of under 0.3% in the underlying — illustrating the amplification leverage provides.

## Trading Sessions

| Session | Approx. hours (UTC) | Notes |
|---------|---------------------|-------|
| Sydney | 21:00–06:00 | Opens the trading week |
| Tokyo (Asia) | 00:00–09:00 | JPY, AUD, NZD activity; BoJ-sensitive |
| London (Europe) | 07:00–16:00 | Largest single centre by volume |
| New York (US) | 12:00–21:00 | USD data, Fed; **London–NY overlap (12:00–16:00) is peak liquidity** |

## Currencies & Pairs

- [[eurusd]] — The most liquid pair globally; the EUR/USD benchmark
- [[usdjpy]] — Rate-differential and carry barometer; sensitive to BoJ policy
- [[us-dollar]] — The world reserve currency; the other side of most pairs
- [[australian-dollar]] — Commodity-linked, risk-on "high-beta" currency
- [[currency-pairs]] — How pairs are constructed and quoted

## Macro Drivers

- [[carry-trade]] — Borrow low-yield, hold high-yield; the canonical FX strategy
- [[covered-interest-rate-parity]] — The no-arbitrage condition linking spot, forward, and rates
- [[cross-currency-basis-swap]] — CIP deviation; a funding-stress signal
- [[interest-rate-differential]] — The core driver of forward pricing and carry
- [[bank-of-japan]] — Yield-curve control and the global yen carry trade
- [[federal-reserve]] — US monetary policy; the dominant driver of dollar pairs

## Market Infrastructure

- [[last-look]] — Dealer execution protocol that allows trade rejection; a hidden execution cost
- [[lmax-exchange]] — Regulated, firm, no-last-look exchange venue
- [[settlement-risk]] — Herstatt/principal risk in cross-border FX settlement

## Brokers, Platforms & Data

- [[dukascopy]] — Free tick-level historical FX data for backtesting

## Hedging & Related Concepts

- [[currency-hedging]] — Managing FX exposure in international portfolios
- [[forward-contract]] — The core institutional FX hedging tool
- [[hedge-ratio]] — Sizing an FX or cross-asset hedge

## Common Pitfalls

- **Over-leverage** — the dominant cause of retail blow-ups (see worked example).
- **Trading the spread away** — wide-spread crosses/exotics and frequent scalping erode edge through transaction costs.
- **Ignoring rollover/swap** — holding positions overnight earns or pays the [[interest-rate-differential]]; a negative carry quietly bleeds a long-held position.
- **Event gaps** — central-bank decisions and surprise interventions (e.g., BoJ) can gap the market through stops.
- **Weekend / liquidity-hole risk** — thin liquidity at session boundaries and over weekends widens spreads and increases gap risk.

## Comparisons

- [[crypto-vs-forex]] — Crypto vs foreign-exchange markets compared

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/markets/forex"
WHERE type != "index"
SORT updated DESC
```

## Sources

- General market knowledge; BIS Triennial Central Bank Survey (April 2025) cited inline for turnover figures. Pip/lot/leverage/session conventions are standard FX-market knowledge. No additional wiki source ingested yet.
