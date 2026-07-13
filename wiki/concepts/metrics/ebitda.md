---
title: "EBITDA"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, profitability, metrics, financial-statements, valuation]
aliases: ["EBITDA", "earnings before interest taxes depreciation amortization", "ebitda"]
domain: [fundamental-analysis]
prerequisites: ["[[financial-statement-analysis]]"]
difficulty: intermediate
related: ["[[ev-ebitda]]", "[[enterprise-value]]", "[[free-cash-flow]]", "[[operating-margin]]", "[[financial-statement-analysis]]", "[[valuation]]", "[[discounted-cash-flow]]", "[[buyouts]]"]
---

**EBITDA** (Earnings Before Interest, Taxes, Depreciation, and Amortization) is a non-GAAP profitability measure that strips out the effects of financing decisions, tax environments, and non-cash accounting charges. It is widely used as a proxy for a company's core operating cash-generating ability, particularly in M&A, leveraged buyouts, and cross-border comparisons.

## Formula

There are two standard derivations, both arriving at the same number. The **bottom-up** route starts from net income and adds back the four excluded items:

```
EBITDA = Net Income + Interest + Taxes + Depreciation + Amortization
```

The **top-down** route starts from operating income ([[operating-margin|EBIT]]) and adds back only the non-cash charges:

```
EBITDA = Operating Income (EBIT) + Depreciation + Amortization
```

The bridge between the two is worth memorising, because the letters in the acronym map directly onto the income statement, read upward from the bottom:

| Line item | Bottom-up build | What it strips out |
|---|---|---|
| Net income | start | — |
| + Taxes | → Pre-tax income | jurisdiction / tax regime |
| + Interest | → EBIT | financing / capital structure |
| + Depreciation | → EBITDA (partial) | non-cash wear on tangible assets |
| + Amortization | → **EBITDA** | non-cash write-down of intangibles / goodwill |

### Worked example

Suppose a firm reports the following for a fiscal year:

- Revenue: $1,000M
- COGS and operating expenses (cash): $760M
- Depreciation & amortization: $40M
- Interest expense: $30M
- Pre-tax income: $170M; taxes at ~24% = $40M; net income = $130M

Top-down: EBIT = Revenue − cash opex − D&A = $1,000M − $760M − $40M = $200M, so **EBITDA = $200M + $40M = $240M**.
Bottom-up: Net income $130M + interest $30M + taxes $40M + D&A $40M = **$240M**. The two routes reconcile.

The **EBITDA margin** here is $240M / $1,000M = **24%**. If the firm carried net debt of $480M, its **net-debt-to-EBITDA leverage** would be 480 / 240 = **2.0x** — comfortably investment-grade for most sectors. At an acquisition [[ev-ebitda|EV/EBITDA]] of 9x, the implied [[enterprise-value]] would be $240M × 9 = **$2,160M**.

## What EBITDA Is Meant to Represent

By removing interest (a financing choice), taxes (a jurisdictional artifact), and depreciation/amortization (non-cash allocations of past capex), EBITDA aims to isolate the economic output of the underlying business. This makes it attractive for comparing a highly leveraged firm against a debt-free peer, or a U.S. firm against a European one with different tax rates and depreciation schedules. It is the denominator of [[ev-ebitda|EV/EBITDA]] and the basis for most LBO debt-capacity calculations (typically expressed as "turns of EBITDA").

## EBITDA vs. Adjacent Metrics

EBITDA sits on a ladder of profitability measures, each removing or adding back a different layer. Knowing where it sits prevents the common error of treating it as if it were cash:

| Metric | Definition | Captures | Ignores |
|---|---|---|---|
| Gross profit | Revenue − COGS | Unit economics, [[gross-margin]] | Overhead, D&A, capex, tax, interest |
| EBITDA | EBIT + D&A | Core operating output, capital-structure-neutral | Capex, working capital, interest, tax |
| EBIT (operating income) | Revenue − opex − D&A | Operating profit after asset wear | Interest, tax |
| Net income | Bottom line | Everything GAAP recognises | Non-cash distortions; capital structure noise |
| [[free-cash-flow]] | Operating cash flow − capex | Actual cash to all providers | — (the "truth serum") |

The single most important relationship: **EBITDA − capex − Δworking capital − cash taxes − cash interest ≈ free cash flow to equity.** The gap between EBITDA and FCF is exactly the set of real cash costs EBITDA pretends away. For an asset-light software firm that gap is small; for an airline or telecom it is enormous.

## Typical Ranges and Use

**EBITDA margin** (EBITDA / Revenue) varies widely by sector. The table below gives rough order-of-magnitude bands (illustrative, not a substitute for live peer data):

| Sector | Typical EBITDA margin | Notes |
|---|---|---|
| Software / SaaS | 25-40%+ | Asset-light; EBITDA close to FCF once SBC is honestly counted |
| Utilities / telecom | 30-45% | High margin but huge capex — EBITDA flatters them most |
| Pharmaceuticals | 30-40% | High gross margin, heavy R&D |
| Mature industrials | 12-20% | Cyclical; watch through the cycle |
| Consumer staples | 15-25% | Stable, defensive |
| Grocery / supermarkets | 3-6% | Razor-thin margins, won on [[stock-turn|inventory velocity]] |
| Airlines | 10-20% (volatile) | EBITDA badly overstates economics vs. FCF |

Tracking margin over time and against peers is far more informative than the absolute dollar figure. A margin that is expanding faster than revenue signals operating leverage; a contracting margin during revenue growth signals "growth at any cost" (see [[revenue-growth]]).

## Limitations

Warren Buffett famously dismissed EBITDA with: *"Does management think the tooth fairy pays for capex?"* The critique is sharp — EBITDA ignores the real cash cost of maintaining the asset base, ignores working capital swings, and treats debt service as irrelevant when it isn't. For capital-intensive businesses (airlines, steel, telecom), EBITDA systematically overstates economic profit relative to [[free-cash-flow]].

**Adjusted EBITDA** games are endemic: companies add back stock-based compensation, restructuring charges, "one-time" legal fees that recur yearly, and founder salaries to inflate the headline number. When reviewing a deal deck, always reconcile adjusted EBITDA to GAAP net income line by line. WeWork's 2019 "Community Adjusted EBITDA" — which added back marketing, administrative, and even some rent costs — became the textbook example of the metric's abuse.

### Common pitfalls and red flags

- **Stock-based compensation (SBC) add-backs.** SBC is a real cost — it dilutes shareholders even though no cash leaves the building. Adding it back to "adjusted EBITDA" is the single most common and most misleading adjustment, especially in tech.
- **"Recurring one-offs."** Restructuring charges, impairments, or legal settlements that reappear every single year are operating costs, not one-time items. Add-backs that recur are a deception.
- **Capex blindness.** EBITDA treats a $1B factory and a software license as equally free. For capital-intensive firms, always pair EBITDA with capex and [[free-cash-flow]].
- **Working-capital swings.** A company can grow EBITDA while bleeding cash into inventory and receivables. EBITDA captures none of this.
- **Lease accounting (IFRS 16 / ASC 842).** Capitalising operating leases mechanically inflates EBITDA (rent moves from opex into D&A and interest). Comparisons across accounting regimes can be apples-to-oranges.
- **Growing add-backs as a short signal.** Sophisticated traders treat a widening gap between GAAP EBITDA and "adjusted EBITDA" as a governance red flag and a candidate for the short side.

## Trading Relevance

EBITDA is the backbone of the [[ev-ebitda|EV/EBITDA]] multiple, the dominant valuation yardstick in M&A, private equity, and cross-border equity research because it is neutral to capital structure and tax jurisdiction. For event-driven and merger-arbitrage traders, the **"turns of EBITDA"** a target can support (net debt ÷ EBITDA, and the multiple at which deals print) sets the floor and ceiling for takeover speculation. In credit and distressed trading, the **net-debt-to-EBITDA leverage ratio** is the single most-watched covenant metric — a breach can force refinancing, equity dilution, or default, and EBITDA covenant definitions are heavily negotiated. Because adjusted EBITDA is so easily manipulated, sophisticated traders treat large or growing add-backs as a short/avoid signal and reconcile to [[free-cash-flow]].

### How analysts and traders use EBITDA in practice

- **Valuation multiples.** Build [[ev-ebitda|EV/EBITDA]] across a peer set, identify the cheap and expensive names, and ask *why* the gap exists. This is the core of relative [[valuation]] and quantitative value screens.
- **LBO debt sizing.** Private-equity buyers size acquisition debt as a multiple of EBITDA ("6 turns of leverage"). The target's stable EBITDA is the collateral that services that debt; see [[buyouts]].
- **Credit covenants.** Leveraged-loan and high-yield-bond covenants are written in EBITDA terms (max net-debt/EBITDA, min EBITDA/interest coverage). Traders model covenant headroom to anticipate forced refinancing or default.
- **DCF cross-check.** A [[discounted-cash-flow]] values the business off unlevered FCF, but practitioners sanity-check the implied exit multiple against current [[ev-ebitda|EV/EBITDA]] comps.
- **Quality filter.** Pair EBITDA with capex and [[free-cash-flow]] conversion (FCF ÷ EBITDA). High, stable conversion = genuine cash machine; low conversion = EBITDA is fiction.

## Related

- [[ev-ebitda]] — the primary valuation multiple built on EBITDA
- [[enterprise-value]] — the numerator EBITDA is divided into
- [[free-cash-flow]] — the metric Buffett prefers instead; the "truth serum"
- [[discounted-cash-flow]] — intrinsic valuation that EBITDA multiples cross-check
- [[buyouts]] — LBO debt is sized in turns of EBITDA
- [[operating-margin]] — EBIT, one rung up the profitability ladder
- [[gross-margin]] — unit economics, one rung down
- [[valuation]], [[financial-statement-analysis]]

## Sources

- Berkshire Hathaway shareholder letters (Warren Buffett & Charlie Munger) — critique of EBITDA and capex ("the tooth fairy")
- SEC Regulation G — non-GAAP measure reconciliation rules covering adjusted EBITDA disclosure
- Damodaran, A., *Investment Valuation* — EBITDA, EV/EBITDA, and their use and abuse in valuation
- WeWork (The We Company) Form S-1, 2019 — "Community Adjusted EBITDA" as a case study in metric abuse
