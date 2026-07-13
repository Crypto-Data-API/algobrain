---
title: "Investment Banking"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [company, valuation, fundamental-analysis, market-microstructure]
aliases: ["Investment Banking", "investment-banking", "IB", "sell-side", "bulge bracket"]
domain: [market-microstructure, valuation]
prerequisites: ["[[valuation]]"]
difficulty: intermediate
related: ["[[goldman-sachs]]", "[[morgan-stanley]]", "[[ipo]]", "[[mergers-and-acquisitions]]", "[[valuation]]", "[[junior-analyst-stranding]]", "[[credit-cycle]]"]
---

Investment banking is the segment of the financial industry that helps corporations, governments, and institutions raise capital, execute mergers and acquisitions, and trade securities. Investment banks sit on the "sell side" — they originate, underwrite, and distribute securities and provide advisory services — in contrast to the "buy side" (asset managers, hedge funds, pension funds) that allocates capital. The largest are the "bulge bracket" firms such as [[goldman-sachs|Goldman Sachs]], [[morgan-stanley|Morgan Stanley]], and JPMorgan.

## Sell side vs. buy side

The single most important framing for a trader is which side of the table a firm sits on, because it determines incentives, information flow, and the nature of any [[conflict-of-interest|conflicts]].

| Dimension | Sell side (investment bank) | Buy side (asset manager / [[hedge-funds\|hedge fund]]) |
|---|---|---|
| Core function | Originate, underwrite, distribute, advise | Allocate capital, take positions |
| How it makes money | Fees, underwriting spreads, bid-ask | Returns on capital, management + performance fees |
| Relationship to issuer | Agent / advisor | Investor / counterparty |
| Research role | Publishes to win flow & banking deals | Consumes (and produces) to find alpha |
| Risk borne | Underwriting/placement risk, market-making inventory | Full market risk of positions |

## The tiering of banks

| Tier | Examples | Typical mandate |
|---|---|---|
| Bulge bracket | [[goldman-sachs\|Goldman Sachs]], [[morgan-stanley\|Morgan Stanley]], JPMorgan, BofA, Citi | Largest global deals, full product suite |
| Elite boutiques | Evercore, Lazard, Centerview, Moelis | Independent M&A advice, restructuring |
| Middle market | Jefferies, Houlihan Lokey, William Blair | Mid-cap deals, distressed/restructuring |
| Regional / specialist | Sector- or geography-focused houses | Niche coverage |

## Core Divisions

- **Investment Banking Division (IBD) / advisory** — capital raising and M&A advice. Subdivided into product groups (M&A, equity capital markets / [[ipo|ECM]], debt capital markets / DCM, leveraged finance, restructuring) and coverage groups organized by industry sector. Revenue is fee-based: underwriting spreads (typically ~1-7% of an IPO, smaller for large deals) and M&A advisory fees (often tiered, low single-digit percent of deal value).
- **Sales & Trading** — markets-facing. Makes markets, provides liquidity, and executes for institutional clients across equities, fixed income, currencies, and commodities (FICC). Earns bid-ask spread and flow commissions; proprietary risk-taking was curtailed for US banks by the post-2008 [[volcker-rule|Volcker Rule]].
- **Research** — publishes analysis and price targets that inform institutional clients. Separated from banking by a "Chinese wall" after the 2003 Global Research Settlement to curb conflicts of interest.
- **Asset / wealth management** — buy-side activities housed within the same parent (e.g. Goldman Sachs Asset Management).

## Key Activities and Mechanics

- **Underwriting** — the bank commits to buy a securities issue from the issuer and resell it to investors, bearing the placement risk in a firm-commitment deal. Book-building gauges demand and sets the price.
- **M&A advisory** — sell-side mandates (run an auction for a company) and buy-side mandates (advise an acquirer); includes valuation, deal structuring, and [[fairness-opinion|fairness opinions]].
- **Leveraged finance** — arranging high-yield bonds and leveraged loans, often to fund private-equity buyouts; tightly linked to the [[credit-cycle]].
- **Valuation toolkit** — comparable companies ("comps"), precedent transactions, discounted cash flow (DCF), and leveraged-buyout (LBO) models are the standard methods (see [[valuation]] and [[discounted-cash-flow]]).

### The underwriting fee structure

Capital-raising revenue scales inversely with deal size — small IPOs pay the headline ~7% "gross spread," while mega-deals and investment-grade bonds pay a fraction of that.

| Product | Typical fee / spread | Notes |
|---|---|---|
| Small-cap IPO | ~5–7% gross spread | The classic "7% solution" for sub-$1bn US IPOs |
| Large-cap IPO / follow-on | ~1–4% | Spreads compress with size and demand |
| [[high-yield-bonds\|High-yield]] bond | ~1.5–3% | Higher than IG due to placement risk |
| Investment-grade bond | ~0.3–0.9% | Commoditized, very thin spreads |
| M&A advisory | Tiered, low single-digit % of deal value | Often a Lehman-formula-style sliding scale + success fee |

### Worked example: an IPO underwriting

Suppose a company sells **10 million shares at $20.00** in its [[ipo|IPO]] with a **7% gross spread**.

- Gross proceeds = 10M × $20 = **$200M**.
- Underwriting fee (the spread) = 7% × $200M = **$14M**, split among the syndicate.
- Net proceeds to the company ≈ **$186M** (before other expenses).
- The lead underwriter typically also holds a **[[greenshoe|greenshoe (over-allotment) option]]** of up to 15% (1.5M extra shares) used to stabilize the price post-listing.

If the stock "pops" to $26 on day one (a 30% first-day return), that ~$60M of value accrued to allocated investors rather than the issuer — the long-running **IPO underpricing** debate, and a structural microstructure feature traders watch.

## Trading Relevance

Investment-bank activity is a real-time read on the market cycle. IPO and M&A volumes are pro-cyclical and tend to peak near market tops — a surge in deal activity, especially low-quality IPOs, has historically been a late-cycle signal. Bank earnings (advisory backlogs, trading revenue, FICC vs equities mix) are widely traded macro tells: strong trading revenue often coincides with volatility spikes, while collapsing advisory fees flag a frozen capital-markets window. Underwriting also creates exploitable microstructure: IPO lockup expirations, index-inclusion flows from newly public names, and the post-IPO "stabilization" period (the greenshoe option) all produce predictable supply/demand events. Research price-target revisions move single names, and the entire sector's headcount is now a watched datapoint for AI-driven labor disruption (see [[junior-analyst-stranding]]).

### Tradable events the sell side creates

| Event | Mechanism | How traders position |
|---|---|---|
| [[ipo|IPO]] first-day pop | Underpricing + scarce allocation | Allocation arbitrage; fade extreme pops |
| Lockup expiration | Insider/early-investor shares become sellable (~90–180 days) | Anticipate supply overhang, often short into it |
| [[greenshoe|Greenshoe]] / stabilization | Syndicate buys to support price post-listing | Watch for a price "floor" then its removal |
| [[index-inclusion|Index inclusion]] | Passive funds must buy at rebalance | Front-run the rebalance flow |
| M&A announcement | Target re-prices toward offer; spread opens | [[merger-arbitrage|Merger arbitrage]] (long target, short acquirer) |
| Secondary / block sale | Bank places a large line at a discount | Buy the discount, manage overhang |
| Research initiation / PT revision | New coverage moves single names | Trade the revision and its drift |

### Conflicts of interest to keep in mind

The sell-side fee model creates structural [[conflict-of-interest|conflicts]] that a trader should price in: research has historically skewed bullish on banking clients (the reason for the 2003 Global Research Settlement and the "Chinese wall"), [[fairness-opinion|fairness opinions]] are paid for by the very deal they bless, and a bank underwriting an IPO is incentivized to place the deal more than to price it precisely for the issuer. Read sell-side targets as one input, not gospel.

## Related

- [[goldman-sachs]], [[morgan-stanley]] — bulge-bracket examples
- [[ipo]] — primary equity issuance
- [[mergers-and-acquisitions]] — advisory product
- [[valuation]], [[discounted-cash-flow]] — analytical core
- [[credit-cycle]] — drives leveraged finance volume
- [[junior-analyst-stranding]] — AI exposure of the analyst class
- [[greenshoe]] — over-allotment / stabilization mechanism
- [[merger-arbitrage]] — buy-side trade off M&A announcements
- [[index-inclusion]] — passive flow event from newly public names
- [[hedge-funds]] — the buy-side counterpart
- [[volcker-rule]] — post-2008 limit on prop trading
- [[conflict-of-interest]] — structural sell-side incentives

## Sources

- Rosenbaum & Pearl, *Investment Banking: Valuation, LBOs, M&A* (Wiley) — standard practitioner reference
- SIFMA capital markets statistics — underwriting and trading volumes
- US Global Research Analyst Settlement (2003); Volcker Rule (Dodd-Frank, 2010) — structural constraints on the industry
