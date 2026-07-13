---
title: "Cash Equivalents"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [liquidity, risk-management, portfolio-theory, bonds, treasuries]
aliases: ["Cash Equivalents", "Cash Equivalent", "Cash & Equivalents"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[liquidity]]"]
difficulty: beginner
related: ["[[liquidity]]", "[[treasuries]]", "[[money-market-fund]]", "[[risk-free-rate]]", "[[asset-allocation]]", "[[stablecoins]]", "[[duration]]", "[[fed-policy]]"]
---

**Cash equivalents** are short-term, highly liquid investments that can be converted to a known amount of cash with negligible risk of price change. Under accounting standards (US GAAP ASC 305, IFRS IAS 7) the conventional threshold is an original maturity of **three months or less**, low credit risk, and no material exposure to interest-rate movements. In trading and portfolio management, "cash and cash equivalents" is the dry-powder bucket that earns the [[risk-free-rate]] while preserving optionality to deploy capital.

## What counts as a cash equivalent

| Instrument | Typical maturity | Notes |
|---|---|---|
| **Treasury bills (T-bills)** | 4–52 weeks | Backed by the US government; the canonical risk-free instrument |
| **Money market fund shares** | n/a (NAV ~$1.00) | Hold T-bills, repo, commercial paper; see [[money-market-fund]] |
| **Commercial paper** | ≤270 days | Short-term unsecured corporate debt; small credit/liquidity risk |
| **Certificates of deposit (CDs)** | ≤3 months | Bank-issued; insured up to limits |
| **Repurchase agreements (repo)** | overnight–weeks | Collateralized short-term lending |
| **Bankers' acceptances** | ≤180 days | Trade-finance instruments |

Longer-dated [[treasuries|Treasuries]], corporate bonds, and equities are **not** cash equivalents because their prices move materially with interest rates and credit spreads — they carry [[duration]] risk.

### The liquidity ladder

Cash equivalents sit on a spectrum from "is cash" to "almost cash" to "investment with cash-like features." Traders think of it as a ladder, trading off yield against immediacy and safety:

| Rung | Instrument | Settlement / access | Yield vs cash | Main risk |
|---|---|---|---|---|
| 1 (most cash-like) | Bank deposit / sweep | Instant | ~0 to policy rate | Bank credit (above insurance limits) |
| 2 | Government [[money-market-fund]] | Same-day / T+1 | ≈ policy rate | Negligible; tiny [[liquidity-risk|liquidity]] in extreme stress |
| 3 | 4-week **[[treasuries|T-bills]]** | Liquid secondary market | ≈ [[risk-free-rate]] | Tiny [[duration]] |
| 4 | Overnight [[repo]] | Overnight | ≈ SOFR | Collateral / counterparty |
| 5 | Prime MMF / [[commercial-paper]] | T+1 | + small spread | Credit, [[liquidity-risk]] in stress |
| 6 | Bankers' acceptances, ≤3-month CDs | At maturity | + small spread | Credit, early-withdrawal penalty |

The closer to rung 1, the more it behaves like literal cash; the further down, the more yield you earn for accepting a sliver of credit or liquidity risk.

## Why the three-month rule matters

The maturity limit is a proxy for **interest-rate insensitivity**. A 90-day instrument has very low [[duration]], so even a sharp move in policy rates changes its price only marginally; it rolls to par quickly. This is what lets accountants and portfolio managers treat it as "almost cash." Anything with meaningful duration can lose principal value — a 10-year Treasury fell roughly 17% in 2022 as the [[fed-policy|Fed]] hiked, disqualifying it as a cash substitute.

## Trading relevance

- **Dry powder and opportunity cost.** Cash equivalents are where capital waits between trades. In a high-rate environment (e.g., T-bills yielding 4–5%) holding cash equivalents has a real positive carry, lowering the opportunity cost of staying flat. In a zero-rate environment the carry is ~0 and the cost of waiting is purely the foregone risky return.
- **Collateral and margin.** T-bills and money-market balances are accepted as margin collateral by prime brokers and clearinghouses, often earning interest while posted — efficient capital use versus idle cash.
- **The cash-and-carry leg.** Many [[arbitrage]] trades (e.g., the futures basis trade) hold T-bills as the financing/collateral leg, capturing the risk-free rate plus the basis spread.
- **Defensive allocation.** Raising the cash-equivalent weight is the simplest way to cut portfolio [[volatility]] and [[drawdown]]; it is a position, not the absence of one, and its value is the embedded option to buy risk assets cheaper later.
- **Crypto analogue.** In crypto, [[stablecoins]] and tokenized T-bill funds (e.g., money-market tokens) serve the cash-equivalent role on-chain, though they add issuer/custody and smart-contract risk absent from a government T-bill.

## Worked Example: The Carry of Sitting in Cash

Two investors each hold $100,000 of dry powder for a year while waiting for an entry, in two different rate regimes:

| Scenario | T-bill yield | Inflation | Nominal end value | Real return | Take-away |
|---|---|---|---|---|---|
| **High-rate (2023-24-style)** | 5.0% | 3.0% | $105,000 | +1.9% | Cash *pays you to wait*; low [[opportunity-cost]] of staying flat |
| **Zero-rate (2020-21-style)** | 0.1% | 6.0% | $100,100 | -5.6% | Real value erodes ~5-6%; waiting is expensive |

Same instrument, opposite economics. This is why the attractiveness of holding [[cash-as-asset|cash as an asset]] is *regime-dependent*: in high-rate environments cash equivalents have genuine positive carry; in financially-repressed zero-rate environments they bleed real value. The relevant number is always the **real** yield (nominal minus inflation), not the headline rate. (Figures illustrative.)

## How Traders Use Cash Equivalents

- **The waiting room for capital.** Between trades, capital parks in T-bills or a [[money-market-fund]] so it earns the [[risk-free-rate]] instead of zero, while staying instantly deployable — the practical implementation of [[cash-as-asset]].
- **Margin efficiency.** Posting T-bills (rather than idle cash) as collateral lets the same dollar both back a position *and* earn interest.
- **The financing leg of basis trades.** Cash-and-carry [[arbitrage]] holds T-bills as the collateral/financing leg, capturing risk-free yield plus the basis.
- **Sequencing the ladder.** Active managers ladder maturities (some overnight, some 4-week, some 3-month) so cash matures on a schedule that matches expected liquidity needs — avoiding having to sell longer paper at a loss.
- **Liquidity buffer for [[liquidity-risk|funding shocks]].** A cash-equivalent reserve is the first line of defense against margin calls, so core positions need not be fire-sold in a [[drawdown]].

## Risks that erode the "equivalent" label

Cash equivalents are low-risk, not no-risk:

- **Credit risk** in non-government paper ([[commercial-paper]] froze in 2008; the Reserve Primary Fund "broke the buck" — its NAV fell below $1.00 — after Lehman exposure, triggering an MMF run).
- **[[liquidity-risk|Liquidity risk]]** in stress — even short paper can gap if a market seizes; prime money-market funds faced redemption pressure in March 2020 until backstopped by the Fed.
- **Inflation risk** — nominal principal is safe but real purchasing power erodes if yields lag inflation (see the worked example above).
- **Reinvestment risk** — falling rates mean each roll earns less.
- **Issuer/custody and smart-contract risk** for the crypto analogues ([[stablecoins]], tokenized funds), absent from a government T-bill — a de-peg or freeze can break the "equivalent" label entirely.

The 2008 and March-2020 episodes show the boundary: a government T-bill or government MMF held up; *prime* paper (commercial paper, CDs) is where the credit and liquidity cracks appear under stress.

## Related

- [[liquidity]], [[liquidity-risk]]
- [[treasuries]], [[repo]], [[commercial-paper]]
- [[money-market-fund]]
- [[risk-free-rate]]
- [[cash-as-asset]], [[opportunity-cost]], [[asset-allocation]]
- [[duration]]
- [[stablecoins]]
- [[fed-policy]]

## Sources

- IAS 7 *Statement of Cash Flows* (IFRS) — definition of cash equivalents (≤3 months, low risk).
- FASB ASC 305 *Cash and Cash Equivalents* (US GAAP).
- US Treasury — Treasury bills overview.
- SEC — Money Market Fund reform releases (Rule 2a-7).
- General market knowledge; the carry/ladder tables and worked example are illustrative.
