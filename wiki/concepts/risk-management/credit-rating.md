---
title: "Credit Rating"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [risk-management, bonds, fundamental-analysis]
aliases: ["Credit Rating", "credit-rating", "Bond Rating", "Credit Ratings"]
related: ["[[credit-risk]]", "[[corporate-bonds]]", "[[bonds]]", "[[credit-default-swap]]", "[[basel-iii]]", "[[sovereign-debt]]", "[[credit-spread]]", "[[leverage]]"]
domain: [risk-management]
prerequisites: ["[[credit-risk]]", "[[bonds]]"]
difficulty: intermediate
---

A **credit rating** is a rating agency's forward-looking opinion of the creditworthiness of a borrower (an *issuer rating*) or of a specific debt security (an *issue rating*) — condensed into a letter grade such as `AAA`, `Baa2`, or `BB+`. The grade summarises the agency's assessment of how likely the obligor is to default and, in many cases, how much creditors would recover if it did. Ratings are one of the primary *inputs* to pricing [[credit-risk]]: a higher rating implies lower expected loss, a tighter [[credit-spread]], and a lower yield, while a lower rating implies the opposite.

## Overview

A credit rating maps the two building blocks of expected credit loss — probability of default and, to a lesser degree, recovery — onto an ordinal alphabetical scale that lets very different obligors (companies, sovereigns, banks, structured deals) be compared on one axis. It is deliberately an *opinion*, not a guarantee, a probability, or a buy/sell recommendation. Because the full mechanics of default probability, loss given default, and expected loss are covered under [[credit-risk]], this page focuses on the ratings themselves: the scales, who produces them, how they are formed, and how markets use and mis-use them.

Ratings serve two audiences at once. For **investors** they are a low-cost screen that compresses a mountain of issuer analysis into a single comparable grade. For **markets and regulators** they are a shared reference that plugs into index rules, mandate constraints, collateral eligibility, and bank capital calculations. That embeddedness is exactly why ratings carry weight far beyond their nominal status as "just an opinion."

## The Big Three agencies

Three firms — often called **the Big Three** — dominate global ratings and together account for the large majority of outstanding ratings:

- **Moody's** (Moody's Investors Service)
- **S&P** (S&P Global Ratings, formerly Standard & Poor's)
- **Fitch** (Fitch Ratings)

Each publishes its own scale, but the scales map onto one another closely. The most economically important feature they share is the split between **investment grade** and **speculative grade** ("high yield" or "junk").

## The rating scales

Long-term scales, from highest quality (lowest default risk) to default:

| Category | Moody's | S&P / Fitch | Meaning |
|---|---|---|---|
| **Investment grade** | Aaa | AAA | Highest quality, minimal default risk |
| | Aa1 / Aa2 / Aa3 | AA+ / AA / AA− | Very high quality |
| | A1 / A2 / A3 | A+ / A / A− | Upper-medium quality |
| | Baa1 / Baa2 / **Baa3** | BBB+ / BBB / **BBB−** | Lower-medium; **lowest investment grade** |
| **Speculative / high yield** | **Ba1** / Ba2 / Ba3 | **BB+** / BB / BB− | **Highest speculative grade**; substantial risk |
| | B1 / B2 / B3 | B+ / B / B− | Highly speculative |
| | Caa1 / Caa2 / Caa3 | CCC+ / CCC / CCC− | Poor standing; high default risk |
| | Ca | CC / C | Highly vulnerable / near default |
| | C | D (S&P uses SD/D; Fitch RD/D) | In default |

Notes on notation:

- **Modifiers.** Moody's appends the numerals `1`, `2`, `3` (best to worst within a category); S&P and Fitch append `+`, plain, `−`. So `A1 ≈ A+`, `Baa3 ≈ BBB−`, and so on.
- **Short-term scales** are separate: Moody's `P-1 / P-2 / P-3` (Prime) plus `Not Prime`; S&P `A-1 / A-2 / A-3`; Fitch `F1 / F2 / F3`. These rate near-term obligations such as commercial paper.
- **The investment-grade / high-yield boundary** falls between **Baa3 / BBB−** (the lowest IG rung) and **Ba1 / BB+** (the highest HY rung). Everything at `BBB−` / `Baa3` and above is investment grade; everything at `BB+` / `Ba1` and below is speculative grade.

### Why the IG/HY boundary matters

The line between investment grade and high yield is the single most consequential threshold in the whole scale, because it is written into rules rather than merely into opinions:

- **Mandate-driven forced selling.** Many pension funds, insurers, and IG bond funds are *contractually barred* from holding sub-investment-grade paper. When a bond crosses the line, these holders may be compelled to sell regardless of price.
- **"Fallen angels."** An issuer downgraded *from* investment grade *into* high yield is called a **fallen angel**. Because IG-constrained holders are dumping supply just as the (smaller) high-yield buyer base absorbs it, fallen angels can suffer outsized, technically-driven price drops that exceed what the fundamental change in default risk alone would justify. The mirror case — an issuer upgraded from HY into IG — is a **rising star**.
- **Index migration.** Bond indices are split by the same boundary, so a crossing forces mechanical rebalancing by every fund that tracks an IG or HY index.

## Issuer vs issue ratings, outlooks, and rating actions

- **Issuer (or "corporate family") rating** grades the obligor's overall capacity to meet its financial commitments — a rating of *the borrower*.
- **Issue rating** grades a *specific instrument*, reflecting its seniority, collateral, and structural position. A single company can therefore carry several different issue ratings at once.
- **Notching** is the practice of rating individual issues above or below the issuer rating to reflect their place in the capital structure: senior secured debt is *notched up* (better recovery), while subordinated, junior, or structurally subordinated debt is *notched down* (worse recovery). Notching is fundamentally a recovery/loss-given-default adjustment layered on top of the issuer's default risk.
- **Outlook** signals the likely direction of the rating over the medium term: `Positive`, `Negative`, `Stable`, or `Developing`.
- **Watch / CreditWatch / Rating Watch** flags a likely *near-term* action, usually pending a specific event (a merger, a large debt issue, a covenant breach).
- **Rating actions** are the discrete changes: an **upgrade** (rating raised), a **downgrade** (rating lowered), an **affirmation** (rating unchanged after review), or a **withdrawal**. A downgrade even *without* default is itself a source of loss — this is *migration / downgrade risk*, discussed under [[credit-risk]].

## How ratings are formed

Agency methodologies vary in detail but generally blend two broad pillars, scored qualitatively and quantitatively and combined into an indicative grade that a rating committee then finalises:

- **Business risk** — the durability and predictability of the obligor's cash flows: industry cyclicality and structure, competitive position, scale, diversification, regulatory environment, and management/governance quality.
- **Financial risk** — the balance sheet and its capacity to service debt, captured through **[[leverage]]** and **coverage ratios**. Typical inputs include debt/EBITDA, debt/capital, funds-from-operations to debt, free-cash-flow to debt, and interest coverage (see interest-coverage), alongside liquidity and refinancing profile. For financially distressed corporates, balance-sheet screens such as the altman-z-score point in the same direction the ratings do.

Additional structural considerations:

- **Sovereign ceilings.** A country's own [[sovereign-debt|sovereign]] rating has historically acted as a *ceiling* on the ratings of most issuers domiciled there, reflecting transfer-and-convertibility risk (the government could restrict access to foreign currency). Modern methodologies allow some strong exporters or structurally insulated issuers to "pierce" the ceiling, but the sovereign remains an anchor.
- **Through-the-cycle philosophy.** Agencies deliberately aim to rate through the economic cycle rather than chase every short-term market swing, which makes ratings *stable* but also *lagging* — a trade-off examined below.

### NRSRO regulation

In the United States, agencies whose ratings can be used for regulatory purposes must be registered with the SEC as a **Nationally Recognized Statistical Rating Organization (NRSRO)**. The designation dates to the 1970s; after the 2008 crisis the **Dodd-Frank Act** tightened NRSRO oversight, disclosure, and conflict-of-interest rules. In the European Union, credit rating agencies are registered and supervised by **ESMA** under the CRA Regulation. This regulatory plumbing is precisely what lets ratings be wired into capital rules and mandates.

## Uses and limitations

### Uses

- **Index eligibility** — bond indices are partitioned by rating, so ratings determine which securities enter an IG or HY benchmark and therefore what index-tracking funds must hold.
- **Regulatory capital** — under the Basel framework's standardised approach, banks' credit risk-weighted assets depend on external ratings; higher-rated exposures carry lower risk weights. See [[basel-iii]].
- **Mandates and covenants** — investment guidelines set minimum ratings; loan and bond documents embed **rating triggers** (e.g., a coupon step-up on downgrade, collateral-posting requirements, or a "change-of-control plus downgrade" put) that convert a rating action into a contractual cash-flow event.
- **Collateral and eligibility** — central banks and clearinghouses apply rating-based haircuts and eligibility screens to accepted collateral.

### Limitations and criticisms

- **Issuer-pays conflict of interest.** Under the dominant business model, the *issuer being rated pays the agency* for the rating. This creates an incentive to be accommodating and enables **ratings shopping**, where issuers solicit indicative grades and hire whichever agency offers the highest.
- **The 2008 structured-finance failures.** In the run-up to the 2007–2009 crisis, agencies assigned top ratings — often `AAA`/`Aaa` — to senior tranches of subprime residential mortgage-backed securities (RMBS) and collateralised debt obligations (CDOs) that subsequently suffered mass downgrades and losses. Flawed correlation assumptions, model limitations, and the issuer-pays conflict were all implicated, and the episode is the canonical case against treating ratings as ground truth. It directly motivated the post-crisis reforms noted above.
- **Ratings lag the market.** Because ratings are through-the-cycle and change discretely, market-based signals move first: [[credit-spread|credit spreads]] and [[credit-default-swap|CDS]] premiums re-price continuously and typically widen well before a formal downgrade (and tighten before an upgrade). Traders therefore watch spreads and CDS as a faster, higher-frequency read on credit than the letter grade.
- **Not a probability or a price.** A rating is an ordinal opinion, not a calibrated default probability and not a valuation; two `BBB` names can have quite different spreads.

## Relationship to spreads and default rates

Ratings and market pricing are tightly linked but not identical. As a rule, a **higher rating maps to a tighter [[credit-spread]] and a lower yield**, because investors demand less compensation for a lower assessed chance of loss; a lower rating maps to a wider spread and higher yield. The relationship is monotonic but noisy — spreads also embed liquidity, supply/demand technicals, and risk appetite that ratings do not, which is why same-rated bonds trade at a range of spreads and why spreads move continuously while ratings sit still.

> **Disambiguation.** In this wiki, `[[credit-spread]]` resolves to an **options income strategy** of the same name. Here "credit spread" means the **bond's yield premium over a comparable risk-free benchmark** — the market price of [[credit-risk]]. The two share only the word "spread"; see [[credit-risk]] for the bond-spread concept in full.

Ratings are validated against outcomes through the agencies' published **annual default and transition studies**, which tabulate the historical default rate of each rating cohort. The central empirical finding is an **ordinal, monotonic rating-to-default mapping**: default frequencies rise steadily as ratings fall. Historically, top investment-grade cohorts (`AAA`/`Aaa`, `AA`/`Aa`) have defaulted only very rarely over one-year horizons, `BBB`/`Baa` cohorts default modestly more often, and the lowest speculative cohorts (`CCC`/`Caa` and below) default at dramatically higher rates — the more so in recessions, when defaults cluster. These studies also report **transition (migration) matrices** — the probability that a bond starting the year at one rating ends it at another (or in default) — which feed portfolio credit models and the migration-risk framework in [[credit-risk]]. Actual realised default rates vary year to year and by cohort, so the mapping should be read as a robust *ordering*, not a fixed set of numbers.

## Related

- [[credit-risk]] — the parent concept; ratings are an input to pricing PD, LGD, and expected loss
- [[credit-spread]] — the bond yield premium a rating helps determine (note the same-name options-strategy disambiguation above)
- [[credit-default-swap]] — a faster, market-based read on default risk that tends to move ahead of ratings
- [[corporate-bonds]], [[bonds]] — the instruments most commonly rated
- [[sovereign-debt]] — sovereign ratings and the sovereign-ceiling effect
- [[basel-iii]] — how external ratings enter bank regulatory capital
- [[leverage]], interest-coverage — the financial-risk ratios that drive ratings

## Sources

- General, widely-taught fixed-income and credit knowledge (e.g. Fabozzi, *Bond Markets, Analysis, and Strategies*; Hull, *Risk Management and Financial Institutions*).
- Rating-scale definitions, the investment-grade / high-yield boundary, notching, outlooks, and the through-the-cycle philosophy follow the published rating methodologies and rating-definition documents of **Moody's**, **S&P Global Ratings**, and **Fitch Ratings**.
- The rating-to-default-rate relationship and transition matrices follow the agencies' published annual default and rating-transition studies (Moody's and S&P). No specific default percentages are asserted here — only the established ordinal relationship.
- Regulatory use of ratings (NRSRO/SEC, Dodd-Frank, ESMA CRA Regulation) and the bank-capital treatment follow US securities law and the Basel Committee on Banking Supervision framework (BIS). The 2008 structured-finance mis-rating episode is documented in official post-crisis reviews (e.g. the US Financial Crisis Inquiry Commission report).
