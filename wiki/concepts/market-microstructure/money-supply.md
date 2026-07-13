---
title: "Money Supply"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [fundamental-analysis, macro, economics, monetary-policy]
aliases: ["money supply", "M1", "M2", "money stock", "money creation"]
domain: [fundamental-analysis]
difficulty: intermediate
related: ["[[macroeconomics]]", "[[monetary-policy]]", "[[inflation]]", "[[quantitative-easing]]", "[[central-bank]]", "[[federal-reserve]]", "[[credit-cycle]]"]
---

The money supply is the total amount of money in circulation in an economy. Changes in money supply growth are a leading indicator of [[inflation]] and [[deflation]], and understanding money creation is essential for interpreting [[central-bank]] policy. For traders, money supply data provides a framework for anticipating shifts in [[liquidity]] conditions that drive asset prices across every market.

## Money Supply Measures

Economists and central banks define the money supply in progressively broader aggregates:

- **M0 (Monetary Base)** — Currency in circulation (physical cash) plus bank reserves held at the [[federal-reserve|Federal Reserve]]. This is the narrowest measure and the one most directly controlled by the central bank. Also called "high-powered money" because it forms the base on which commercial banks create broader money.

- **M1** — M0 plus checking accounts (demand deposits) and other highly liquid deposits. M1 represents money that is immediately available for spending. In 2020, the Fed redefined M1 to include savings deposits, which caused a one-time jump in the reported figure.

- **M2** — M1 plus savings deposits, money market accounts, and small time deposits (CDs under $100,000). M2 is the most-watched monetary aggregate because it captures the money available for both transactions and near-term spending. FRED series: M2SL.

- **M3 (discontinued in the US since 2006)** — M2 plus large time deposits, institutional money market funds, and other large liquid assets. The Fed stopped publishing M3 in 2006, arguing it provided no additional information for policy decisions. Some economists disagree and track private reconstructions.

## The Equation of Exchange

The foundational identity of monetary economics:

**MV = PQ** (also written MV = PY)

Where:
- **M** = money supply
- **V** = velocity of money (how many times each unit of money changes hands per period)
- **P** = price level
- **Q** (or Y) = real output (real GDP)

This is an identity — it is true by definition. The monetarist insight, associated primarily with Milton Friedman, is that in the long run, if velocity (V) and real output (Q) are roughly stable, then money supply growth directly drives [[inflation]]. Friedman's famous dictum: "Inflation is always and everywhere a monetary phenomenon."

In practice, V is not stable (see below), which is why the relationship between money supply and inflation is reliable over decades but unreliable over quarters. This distinction matters enormously for trading — money supply is a strategic indicator, not a tactical one.

## Velocity of Money

Velocity measures how many times a unit of money changes hands per period. It is calculated as nominal GDP divided by money supply (V = PQ / M).

Key facts about velocity:

- **Secular decline** — M2 velocity has been declining for decades, driven by financial asset accumulation, rising inequality (wealthy households have lower marginal propensity to spend), and the increasing use of money as a store of value rather than a medium of exchange.

- **COVID collapse** — After the pandemic, M2 velocity fell sharply as the Fed expanded M2 by roughly 40% but much of the new money sat in savings accounts and was not immediately spent. FRED series: M2V.

- **Why it matters for traders** — When velocity is low and declining, even large increases in money supply may not produce immediate inflation. This explains why the massive QE programs of 2008-2014 did not produce the consumer price inflation many predicted — the money went into financial assets rather than goods and services. When velocity eventually picks up (as it did in 2021-2022), the inflationary effects of prior money creation can materialize with a lag.

## How Money Is Created

Money enters the economy through two distinct channels, and understanding both is critical:

### 1. Central Bank Money Creation

The [[federal-reserve]] creates reserves by purchasing assets (typically Treasury bonds and mortgage-backed securities). This is [[quantitative-easing]] (QE). When the Fed buys a bond from a bank, it credits the bank's reserve account — new money that did not previously exist. Conversely, quantitative tightening (QT) destroys reserves by letting bonds mature without reinvestment.

Central bank money creation directly affects M0 (the monetary base) but only indirectly affects broader money supply measures.

### 2. Commercial Bank Money Creation

This is where most money actually comes from. When a commercial bank makes a loan, it does not lend out existing deposits — it creates a new deposit in the borrower's account. This is the fractional reserve system in action. A single dollar of reserves can support multiple dollars of deposits, with the exact ratio determined by reserve requirements and bank capital constraints.

The implication is profound: **the money supply is primarily determined by the willingness of banks to lend and borrowers to borrow**, not by the central bank alone. This is why the [[credit-cycle]] and money supply are so closely linked — when banks tighten lending standards, money creation slows regardless of what the Fed does with reserves.

## Fed Balance Sheet as a Trading Signal

The Fed's balance sheet is the most direct measure of central bank [[liquidity]] injection or withdrawal:

- **QE expands the balance sheet** — More reserves enter the system, pushing investors into riskier assets (the "portfolio rebalancing channel"). Asset prices rise.
- **QT shrinks the balance sheet** — Reserves drain from the system, tightening financial conditions. This creates a headwind for risk assets.

Key milestones:
- Pre-2008: ~$900 billion
- Post-2008 QE: ~$4.5 trillion
- Post-COVID QE peak (2022): ~$9 trillion
- After QT (2026): ~$6.7 trillion

Track via FRED series WALCL (Total Assets of the Federal Reserve). Changes in the balance sheet, particularly the pace of change, have been correlated with [[sp500|S&P 500]] performance since 2009.

## Money Supply and Markets

M2 growth has historically been one of the most reliable leading indicators for both equity markets and inflation:

- **M2 growth leads equity returns by 6-12 months** — When M2 is accelerating, liquidity conditions are improving and risk assets tend to follow. When M2 is decelerating or contracting, it signals tightening conditions ahead.

- **M2 growth leads consumer inflation by 12-18 months** — The lag exists because money must circulate through the economy before affecting consumer prices. This lag was visible in 2020-2022: M2 surged in mid-2020, and CPI inflation did not peak until mid-2022.

- **The 2022-2023 M2 contraction** — For the first time since the Great Depression, US M2 actually declined year-over-year in 2022-2023. This was a significant bearish signal and preceded the tightening of financial conditions, regional bank stress, and the slowdown in economic growth.

- **Global M2** — In an interconnected financial system, US M2 alone is insufficient. Traders increasingly track global M2 (US + Eurozone + Japan + China) as a proxy for worldwide [[liquidity]]. Global M2 expansion has been strongly correlated with [[bitcoin|Bitcoin]] and other risk asset performance.

## Where to Track Money Supply Data

| Series | Description | Source |
|--------|-------------|--------|
| M2SL | US M2 Money Stock | FRED |
| M2V | Velocity of M2 | FRED |
| WALCL | Fed Total Assets (balance sheet) | FRED |
| RRPONTSYD | Reverse Repo (liquidity drain) | FRED |
| WTREGEN | Treasury General Account (liquidity impact) | FRED |

## Related

- [[macroeconomics]] — Money supply is a core macro variable
- [[monetary-policy]] — Central bank tools for influencing money supply
- [[inflation]] — The primary long-term consequence of money supply growth
- [[deflation]] — What happens when money supply contracts
- [[quantitative-easing]] — The mechanism by which central banks expand the monetary base
- [[credit-cycle]] — Bank lending is the primary channel of money creation
- [[federal-reserve]] — The institution that controls the monetary base
- [[central-bank]] — Central banks globally manage their respective money supplies

## Sources

- Milton Friedman & Anna Schwartz, *A Monetary History of the United States, 1867-1960* — foundational monetarist work.
- Federal Reserve, *Money Stock Measures (H.6)* release — official M1/M2 definitions and the 2020 M1 redefinition.
- Federal Reserve Bank of St. Louis, FRED database — series M2SL, M2V, WALCL, RRPONTSYD, WTREGEN.
- Bank of England, "Money creation in the modern economy" (Quarterly Bulletin, 2014) — commercial-bank money creation via lending.
