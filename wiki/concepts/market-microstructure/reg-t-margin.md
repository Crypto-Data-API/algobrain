---
title: "Reg-T Margin"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [margin, leverage, market-microstructure, risk-management, stocks, options]
domain: [risk-management, market-microstructure]
prerequisites: ["[[leverage]]", "[[margin]]"]
difficulty: intermediate
aliases: ["Reg T", "Regulation T", "Reg-T Margin", "Regulation T Margin", "Federal Reserve Regulation T", "12 CFR 220"]
related: ["[[portfolio-margin]]", "[[span-margin]]", "[[maintenance-margin]]", "[[initial-margin]]", "[[margin-call]]", "[[leverage]]", "[[short-selling]]", "[[options]]", "[[options-buying-power-reduction]]", "[[pattern-day-trader-rule]]", "[[finra]]", "[[tastytrade-platform]]"]
---

**Regulation T** ("**Reg-T**") is the US Federal Reserve rule -- codified at **12 CFR 220** -- that governs the extension of credit by broker-dealers to customers buying securities on margin. Its defining feature is the **50% initial margin requirement**: an investor can borrow at most half the purchase price of marginable equity securities, and must put up the other half in cash or eligible collateral. Reg-T is the legacy, strategy-based margin framework that applies to most US retail brokerage accounts; it is the more restrictive alternative to [[portfolio-margin|portfolio margin]] and a different framework entirely from the futures-world [[span-margin|SPAN]].

## Overview

Reg-T was introduced after the 1929 crash and the [[1929-crash|excessive leverage]] that amplified it -- before the rule, brokers routinely lent 80-90% against stock purchases, so a modest price drop wiped out the investor and cascaded into forced selling. By capping initial borrowing at 50%, Reg-T limits the leverage an ordinary investor can take to a maximum of **2:1** on a fully marginable long stock position.

Reg-T governs the **initial** extension of credit. Two related but distinct rules complete the picture:

- **Maintenance margin** is set by the self-regulatory organizations ([[finra|FINRA]] requires a minimum of **25%** equity in a long margin account; brokers commonly set higher "house" requirements of 30-40%). When account equity falls below the maintenance threshold, the broker issues a [[margin-call|margin call]]. See [[maintenance-margin]].
- **Pattern-day-trader (PDT) rules** require a [[pattern-day-trader-rule|pattern day trader]] to keep at least $25,000 of equity and grant up to 4:1 *intraday* buying power -- a separate FINRA overlay on top of Reg-T.

## The Core Rules

| Transaction | Reg-T requirement |
|---|---|
| Long marginable stock | **50% initial margin** (borrow up to 50%, i.e., max 2:1 leverage) |
| Short stock sale | **50% margin** on the value of the shorted stock (plus the short-sale proceeds held as collateral) |
| Long options | Paid in full -- options are **not marginable** under Reg-T; 100% of premium required |
| Short (naked) equity options | Strategy-based formula -- typically the greater of {20% of underlying minus out-of-the-money amount, plus premium} or {10% of strike plus premium} |
| Spreads / defined-risk option strategies | Margin equal to the **maximum loss** of the defined-risk structure |

The hallmark of Reg-T is that it is **strategy-based and formulaic**: each position (or recognized spread) is margined according to a fixed rule book, with little or no credit for portfolio-level offsets between uncorrelated positions. This is exactly the limitation that [[portfolio-margin]] and [[span-margin]] relax by computing risk at the portfolio level.

## Reg-T Buying Power and the Cash/Margin Distinction

In a Reg-T **margin** account, deposited cash is effectively doubled into **buying power** for marginable stock: $50,000 cash supports up to $100,000 of long stock. In a **cash** account, no credit is extended -- buying power equals settled cash, and Reg-T's "free-riding" and settlement rules (now under [[t-plus-one-settlement|T+1 settlement]]) restrict trading with unsettled proceeds.

For options sellers, the strategy-based formula determines the [[options-buying-power-reduction|buying power reduction]] -- the amount of account equity locked up to hold a short-option position -- which under Reg-T is typically far larger than the same position would consume under a risk-based portfolio-margin or SPAN system.

## Why It Matters to a Stock Investor

- **It sets the maximum leverage** an ordinary investor can take: 2:1 on stock at initiation. This is a deliberate guardrail against the kind of leverage that turned the 1929 decline into a wipeout.
- **It determines margin-call risk.** Buying at the 50% initial requirement leaves little cushion above the 25%+ maintenance floor; a moderate decline can trigger a [[margin-call|margin call]] forcing the investor to deposit cash or liquidate at the worst time.
- **It makes short option selling capital-intensive.** Because Reg-T gives no portfolio-level offsets, defined-risk and naked short option strategies tie up far more capital than under [[portfolio-margin]] -- a key reason active option sellers seek the $110,000+ portfolio-margin threshold or migrate to futures-options venues that use [[span-margin|SPAN]] (see [[tastytrade-platform]]).
- **It is the default.** Unless an investor qualifies for and elects portfolio margin, Reg-T is the framework their account runs under.

## Hypothetical Worked Example

*The following figures are illustrative, not advice.*

An investor deposits **$50,000** in a Reg-T margin account and buys stock at the maximum allowed leverage.

- Initial margin (50%) lets them buy **$100,000** of stock, borrowing $50,000 from the broker.
- Their starting equity is $50,000 (50% of the position) -- satisfying the Reg-T initial requirement.

Now suppose the stock falls 20%, to **$80,000**:

- The $50,000 loan is unchanged; equity = $80,000 - $50,000 = **$30,000**.
- Equity as a percentage of the position = $30,000 / $80,000 = **37.5%**.

If the broker's maintenance requirement is 30%, the investor is still above the line. But if the stock falls another 14% to roughly $69,000, equity falls to about $19,000 / $69,000 = ~27.5%, and at a 30% house requirement the broker issues a **margin call** demanding the investor add cash or sell shares. The 2:1 leverage that doubled the upside has also roughly doubled the speed at which a decline erodes the equity cushion -- the structural reason Reg-T exists.

## Reg-T vs Portfolio Margin vs SPAN

| Dimension | **Reg-T** | [[portfolio-margin\|Portfolio Margin (TIMS)]] | [[span-margin\|SPAN]] |
|---|---|---|---|
| Used for | Retail equity/options accounts | US equity-options accounts above ~$110K equity | Futures and futures-options accounts globally |
| Methodology | Strategy-based, fixed % per position | Risk-based; worst-case across a price/vol scenario grid | Risk-array across 16 price/vol scenarios |
| Portfolio offsets | Limited / none | Within product groups | Inter-commodity credits |
| Max stock leverage | 2:1 at initiation | Higher, risk-dependent | N/A (notional leverage much higher) |
| Account minimum | None | ~$110,000 equity (US) | Broker-set (often $25K+) |

Reg-T is the most conservative and the least capital-efficient of the three, which is its purpose: it protects unsophisticated investors and the broader system from the leverage spirals that risk-based systems permit in calm regimes and then violently reprice in stress.

## Limitations and Caveats

- **Capital-inefficient for hedged books.** Because it ignores portfolio-level risk offsets, a perfectly hedged position can still require full margin on each leg -- the central complaint that drove the creation of [[portfolio-margin]].
- **Initial vs maintenance confusion.** Reg-T sets only the *initial* 50% requirement; the ongoing risk of a margin call is governed by FINRA/house **maintenance** requirements, which are separate and often higher than the 25% federal floor.
- **House requirements override the minimums.** Brokers routinely impose stricter requirements on volatile, low-priced, or concentrated positions, so the effective Reg-T leverage is often below 2:1 in practice.
- **Not a measure of risk.** Like all margin frameworks, the dollar requirement reflects a rule, not the true tail risk of the position; a Reg-T-compliant account can still suffer catastrophic loss in a gap move.
- **Day-trading overlay.** Intraday, the [[pattern-day-trader-rule|PDT]] 4:1 buying power and $25,000 equity rule -- not the 50% Reg-T initial margin -- governs the constraints for frequent day traders.

## Related

- [[portfolio-margin]] -- the risk-based alternative for larger accounts
- [[span-margin]] -- the futures-world portfolio margining system
- [[maintenance-margin]] -- the ongoing equity floor that triggers margin calls
- [[initial-margin]] -- the broader concept Reg-T's 50% rule defines for equities
- [[margin-call]] -- the consequence of breaching maintenance margin
- [[leverage]] -- the broader concept Reg-T caps at 2:1
- [[short-selling]] -- also governed by Reg-T's 50% short-margin rule
- [[options-buying-power-reduction]] -- how Reg-T's strategy formulas lock up option-seller capital
- [[pattern-day-trader-rule]] -- the intraday buying-power overlay
- [[finra]] -- sets the maintenance-margin minimums
- [[tastytrade-platform]] -- a venue where Reg-T vs portfolio-margin economics drive behavior

## Sources

- US Federal Reserve, *Regulation T* (12 CFR Part 220), "Credit by Brokers and Dealers" -- the authoritative rule establishing the 50% initial margin requirement.
- FINRA Rule 4210 (Margin Requirements) -- sets the 25% minimum maintenance margin and related house-requirement framework.
- US Securities and Exchange Commission and FINRA investor education materials on margin accounts and margin calls.
