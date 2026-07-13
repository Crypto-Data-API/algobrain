---
title: "XLF (Financial Select Sector SPDR)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, sp500, etf, options]
aliases: ["XLF ETF", "Financial Select Sector SPDR Fund", "Financials SPDR"]
related: ["[[spy]]", "[[xlk]]", "[[xle]]", "[[options-concentration-risk]]", "[[sector-rotation]]", "[[sp500]]"]
---

XLF is the Financial Select Sector SPDR Fund, issued by State Street Global Advisors. It tracks the S&P Financial Select Sector Index — the financials slice of the [[sp500|S&P 500]], including major banks, insurance companies, capital markets firms, and (since 2016) Berkshire Hathaway. XLF is the most liquid sector ETF for US financials and the standard vehicle for expressing views on banks, rates-sensitive financials, and the credit cycle.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | XLF |
| **Index tracked** | S&P Financial Select Sector Index |
| **Issuer** | State Street Global Advisors |
| **Structure** | Open-end ETF |
| **Inception** | December 16, 1998 |
| **Expense ratio** | 0.09% |
| **AUM** | approximately $45-55B (as of early 2026) |
| **Avg daily volume** | approx 30-50M shares/day |
| **Options liquidity** | Very deep — among the most heavily traded sector ETF options |
| **Dividend** | Quarterly, ~1.5% yield |

## Top Holdings

XLF is more diversified across its top names than [[xlk|XLK]], but still has meaningful concentration in the largest US banks and Berkshire:

| Holding | Approx Weight |
|---------|---------------|
| Berkshire Hathaway (BRK.B) | ~13-15% |
| JPMorgan Chase (JPM) | ~10-12% |
| Visa (V) | ~6-8% |
| Mastercard (MA) | ~6-7% |
| Bank of America (BAC) | ~4-5% |
| Wells Fargo (WFC) | ~3-4% |
| Goldman Sachs (GS), Morgan Stanley (MS), American Express (AXP), Citigroup (C), Charles Schwab (SCHW) | ~2-4% each |

XLF spans three distinct sub-sectors: traditional banks (JPM, BAC, WFC, C), capital markets / brokers (GS, MS, SCHW), and payments / insurance (V, MA, AXP, BRK.B, PGR). These groups have meaningfully different rate and credit-cycle sensitivities.

## Sub-Sector Composition

| Sub-sector | Approx Weight | Key Drivers |
|------------|---------------|-------------|
| Diversified banks | ~25-30% | Net interest margin, credit losses, deposit flows |
| Capital markets | ~12-15% | M&A activity, IPO volume, trading revenue |
| Insurance | ~15-18% | Underwriting cycle, catastrophe losses, investment income |
| Consumer finance / payments | ~18-22% | Card volumes, consumer credit, fees |
| Berkshire | ~13-15% | Standalone — operates as a conglomerate |

This breadth makes XLF a less pure "bank" play than the more concentrated KRE (regional banks) or KBE (broad banks). For a pure US bank exposure, KRE/KBE is the cleaner instrument; for "financials writ large," XLF dominates.

The sub-sector mix matters because the groups respond to *different* macro drivers, and that internal diversification is what mutes XLF relative to single-name banks. Payments names (Visa, Mastercard) are effectively consumer-spending toll-takers with little direct rate or credit-loss exposure; insurers earn on the underwriting cycle and investment income; capital-markets firms live on deal flow and trading volatility; and only the diversified banks carry the classic net-interest-margin and credit-loss profile. A "financials" view is therefore really a weighted blend of four distinct businesses.

## Sector Drivers & Macro Sensitivities

Financials are the S&P sector most directly geared to *interest rates, the yield curve, and the credit cycle*:

| Driver | Mechanism | Direction for XLF |
|--------|-----------|-------------------|
| Yield curve slope (10s2s) | Banks borrow short, lend long; a steeper curve widens net interest margin | Steepening → positive |
| Fed policy / short rates | Sets funding cost and deposit competition | Nuanced: rising rates help NIM but can crimp loan demand and bond books |
| Credit spreads ([[hyg\|HYG]] / [[lqd\|LQD]]) | Proxy for loan-loss and default risk | Widening spreads → negative |
| Loan growth / economic activity | Drives volume of lending and fee income | Pro-cyclical, positive |
| Capital-markets activity | M&A, IPO, trading revenue for GS/MS/SCHW | Positive in active markets |
| Consumer credit health | Card volumes and charge-offs for V/MA/AXP | Positive when consumer strong |
| Regulatory / stress-test regime | Capital requirements, buyback approvals | Looser → positive |
| Banking-system confidence | Deposit stability; runs are the acute tail | Stress → sharply negative |

The defining macro fact: XLF is a **levered bet on the credit cycle and the shape of the yield curve**. It leads the broad market into recoveries (credit reflation) and lags badly into credit deterioration. Its dominant tail risk — a deposit run or banking-confidence shock (2008, March 2023 SVB) — is largely orthogonal to the recession/demand risk that drives [[xle|XLE]] or the rates/AI risk that drives [[xlk|XLK]].

## Seasonality

Financials seasonality is dominated by the **earnings calendar** rather than the weather or commodity cycle:

- **Quarterly earnings clustering** — the big banks (JPM, BAC, WFC, C, GS, MS) report in a tight window at the start of each earnings season (mid-Jan, mid-Apr, mid-Jul, mid-Oct), making XLF implied vol rise into those windows and collapse after. This is the single most important calendar effect for XLF options.
- **"Sell in May" cyclicality** — as a high-beta cyclical, XLF participates in the broad-market tendency for weaker summer (May-Oct) returns and stronger Nov-Apr performance, though the effect is modest and macro-dominated.
- **Year-end positioning** — bank buyback windows and CCAR/stress-test results can drive episodic year-end strength when capital-return capacity is confirmed.
- **FOMC clustering** — XLF reacts more sharply to FOMC days than most sectors; its calendar is effectively the Fed's calendar.

Treat XLF seasonality as overwhelmingly *event-driven* (earnings + Fed) rather than calendar-driven. See [[seasonality]] and [[earnings-calendar]].

## How XLF Trades vs the Broad Index

- **High correlation to [[spy|SPY]]** (~0.85) with beta typically 0.9-1.1 — XLF is a large, cyclical chunk of the index, so it tracks it closely in calm regimes but amplifies moves in stress.
- **Rate-and-curve sensitivity.** XLF moves more sharply than SPY on FOMC days and on big moves in the 2s10s curve; long XLF / short [[tlt|TLT]] is a clean curve-steepener expression.
- **Credit-cycle leadership.** XLF tends to top out before the broad market when credit conditions deteriorate, and to lead off the bottom when spreads compress — useful as a forward-looking cycle tell.
- **Idiosyncratic tail behavior.** The banking-stress regime (March 2023) shows XLF can decouple downward from SPY even when the broad market is calm, because deposit-run fear is sector-specific. The diversification across mega-banks and non-bank financials, however, mutes the move relative to regional-bank instruments like KRE.

## Options on XLF

XLF hosts one of the most active sector ETF options markets:

- **Weekly expirations**
- **Strike granularity** — $0.50 near ATM (XLF trades around $40-50)
- **American-style**, physical settlement
- **IV regime** — typically 18-25% annualized; spikes to 35%+ during banking stress (March 2023 SVB / regional bank crisis)
- **Skew** — pronounced put skew, especially during credit-cycle concerns

XLF options are popular for hedging concentrated bank exposure and for expressing views on Fed policy, yield curve shape, and credit conditions.

## Sector-Specific Vol Regimes

XLF realized vol regimes are distinct from broad-market vol:

- **Calm regime** (post-stress, expanding economy): 14-18% realized vol, in line with SPY
- **Rate-sensitive regime** (Fed cycle changes): 20-25% realized vol; XLF moves more sharply than SPY on FOMC days
- **Banking-stress regime** (2008, March 2023 SVB): 40%+ realized vol; XLF can drop 15-20% in a week while SPY moves much less

The March 2023 SVB / Signature / First Republic episode is the recent canonical case: XLF fell ~12% in two weeks while SPY barely moved net. Single-name regional banks (KRE) crashed 30%+, but XLF's diversification across mega-banks and non-bank financials muted the move.

## Concentration Risk Angle

[[options-concentration-risk]] uses banks as one of the canonical sector-concentration examples: a book of short premium on JPM, BAC, WFC, GS, MS, C looks like six positions but acts as one XLF position in stress. Pairwise correlation among the major banks runs 0.7-0.85 in normal regimes and approaches 0.9+ in banking stress.

XLF serves multiple roles in the concentration framework:

- **Diagnostic** — beta-weight any bank book to XLF; if XLF-equivalent exposure dominates, the book is a sector trade
- **Hedge** — long XLF puts to cap sector-wide downside on a concentrated bank book
- **Diversifier** — for a tech-heavy short premium book ([[xlk]]-like), adding XLF short premium provides exposure to a sector with different vol regime drivers (rates and credit cycle vs AI capex)
- **Pair trade** — long XLF / short XLK is the canonical value-vs-growth or financials-vs-tech rotation trade

## Trading Uses

- **Financials sector view** — long or short XLF to express bank/financial direction
- **Yield curve trade** — XLF tends to benefit from a steep yield curve (banks borrow short, lend long); long XLF / short [[tlt|TLT]] expresses curve steepening
- **Credit cycle proxy** — XLF underperforms during credit deterioration; useful as a cycle indicator
- **Sector rotation** — XLF is the primary "value" expression in growth-vs-value rotation trades vs XLK
- **Hedge for bank-heavy portfolios** — wealth managers with large bank exposure use XLF puts as cheaper sector-level protection
- **Dispersion trade** — short XLF vol / long single-name bank vol around earnings season

## Peer & Related ETF Comparison

XLF is the broad, cap-weighted "financials writ large" vehicle. The peer set lets you isolate purer slices of the sector:

| ETF | Focus | How it differs from XLF |
|-----|-------|-------------------------|
| **XLF** | Cap-weighted S&P 500 financials | Includes Berkshire + payments + insurance; not a pure bank play |
| **KBE** (SPDR Bank) | Equal-weighted US banks | Removes mega-cap dominance; cleaner bank beta, higher vol |
| **KRE** (SPDR Regional Bank) | Equal-weighted regional banks | The high-beta deposit-run / NIM play; crashed 30%+ in March 2023 |
| **VFH** (Vanguard Financials) | Broad US financials, MCap-weighted | Similar to XLF, wider basket, lower fee |
| **IYF** (iShares US Financials) | US financials incl. real estate historically | Broader definition, less liquid options |
| **KIE** (SPDR Insurance) | Insurance only | Underwriting-cycle play; low rate/credit beta |
| **IAI** (Broker-Dealers) | Capital markets / exchanges | Deal-flow and trading-volume play |
| **EUFN** (Europe Financials) | European banks | Different rate regime; for relative-value vs US |

The key axis is **diversified (XLF) vs pure bank (KBE/KRE)**. If the thesis is specifically "regional-bank stress" or "net-interest-margin," KRE/KBE express it far more directly and with much higher beta; XLF's payments/insurance/Berkshire ballast will dilute the trade. For "financials as a cyclical sector" and for the deepest options liquidity, XLF is the default.

## Risks

- **Banking-confidence / deposit-run tail.** The acute downside (2008, March 2023 SVB) is a sudden loss of confidence in deposit safety that no amount of diversification fully hedges; it can take XLF down double digits in days.
- **Credit-cycle gearing.** XLF is a levered bet on loan losses and spreads; a sharp credit deterioration hits banks, consumer-finance, and insurers' investment books simultaneously.
- **Rate-regime ambiguity.** Rising rates are not unambiguously good — they lift NIM but can crush bank bond portfolios (the SVB mechanism), slow loan demand, and raise funding costs as depositors chase yield.
- **Single-name dependency.** Berkshire (~14%) and JPMorgan (~10-12%) together are ~25% of the fund; an idiosyncratic event at either moves XLF disproportionately.
- **Regulatory shock.** Capital-requirement changes, failed stress tests, or buyback restrictions can re-rate the whole sector.
- **Correlation spikes in stress.** Pairwise bank correlation runs ~0.7-0.85 normally but approaches 0.9+ in banking stress — diversification across banks largely evaporates exactly when it's needed. See [[options-concentration-risk]].

## Key Relationships

- **XLF vs SPY**: ~0.85 correlated; beta typically 0.9-1.1 (lower in calm regimes, higher in stress)
- **XLF vs XLK**: ~0.55-0.65 correlated; the canonical value/growth pair
- **XLF vs yield curve (10s2s)**: positive correlation; steepener helps banks
- **XLF vs credit spreads (HYG, LQD)**: positive correlation with HYG; XLF and high-yield credit move together on cycle changes
- **XLF vs BRK.B**: meaningful single-stock dependency given Berkshire's ~14% weight

## Sources

- State Street SPDR official fund documentation
- S&P Dow Jones Indices methodology
- CBOE options market data
- Federal Reserve banking sector data

## Related

- [[spy]] — broad benchmark
- [[xlk]] — tech SPDR; canonical pair-trade counterpart
- [[xle]] — energy SPDR
- [[sector-rotation]] — XLF as a sector-rotation building block
- [[seasonality]] — XLF's earnings- and Fed-driven calendar
- [[earnings-calendar]] — bank earnings cluster that drives XLF IV
- [[options-concentration-risk]] — XLF as the proxy for hidden bank concentration
- [[sp500]] — underlying parent index
- [[tlt]] — long-end Treasuries; inverse to XLF on curve steepening trades
- [[hyg]] — high-yield credit; co-moves with XLF on the cycle
- [[lqd]] — investment-grade credit proxy
