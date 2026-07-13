---
title: "Repurchase Agreements (Repo)"
type: concept
created: 2026-07-02
updated: 2026-07-02
status: good
tags: [market-microstructure, bonds, liquidity, risk-management, treasuries]
aliases: ["Repo", "repo", "Repurchase Agreement", "Repurchase Agreements", "Reverse Repo", "RRP"]
related: ["[[sofr]]", "[[fed-funds-rate]]", "[[treasuries]]", "[[collateral]]", "[[liquidity]]", "[[quantitative-easing]]", "[[forced-liquidation]]", "[[counterparty-risk]]"]
domain: [market-microstructure]
difficulty: intermediate
---

A **repurchase agreement (repo)** is a collateralised short-term loan dressed as a pair of securities trades: one party sells a security — most often a U.S. Treasury — and simultaneously agrees to buy it back at a set date for a slightly higher price. Economically it is a **secured loan**: the seller borrows cash, pledges the security as [[collateral]], and the difference between the sale price and the repurchase price is the interest, expressed as an annualised **repo rate**. Repo is the core plumbing of short-term dollar funding, and overnight Treasury repo transactions are the raw material from which [[sofr|SOFR]] is calculated.

## Overview

In a repo, the cash borrower is said to "do a repo" (they repo out securities to raise cash), while the cash lender is doing the mirror-image transaction, a **reverse repo** (they take in securities and lend cash). The two names describe the same trade seen from opposite sides: a repo to the collateral-provider is a reverse repo to the cash-provider. Because legal title to the collateral passes to the lender for the life of the trade, the lender is protected if the borrower defaults — it already holds the security and can sell it — which is why repo funding is cheap relative to unsecured borrowing.

The economics are simple to state:

- **Day 0** — Borrower sells $100 of Treasuries to Lender for, say, $99.90 in cash (a small **haircut** below market value).
- **Day 1 (overnight repo)** — Borrower repurchases the same $100 of Treasuries for $99.90 plus one day's interest at the repo rate.

The repo rate is quoted as an annualised percentage; the dollar interest is the repurchase price minus the sale price. Because the loan is fully collateralised and typically very short-dated, repo rates sit close to other secured overnight benchmarks and normally trade near the Fed's [[fed-funds-rate|policy]] corridor.

## Mechanics

**Collateral and haircuts.** The lender advances slightly less cash than the market value of the collateral; the shortfall is the **haircut** (or initial margin). A 2% haircut means $100 of collateral raises $98 of cash. Haircuts protect the lender against a fall in collateral value between the last margin call and a liquidation. They are small for high-quality collateral like on-the-run Treasuries and larger for riskier or less liquid securities (agency MBS, corporate bonds, equities). Trades are typically **marked to market** daily, with variation margin exchanged to keep the loan collateralised.

**Tenor: overnight vs term.** Most repo is **overnight** — borrowed today, repaid tomorrow, and often rolled day after day. **Term repo** fixes the loan for a stated period (a week, a month, or longer), locking in the rate and the funding for that horizon. Open repo has no fixed maturity and rolls until either side cancels.

**Market structure.** Repo trades in several venues that differ in how collateral is managed and who bears operational and settlement risk:

- **Bilateral repo** — negotiated directly between two counterparties, who handle their own collateral and settlement. Common for specific-collateral trades where the lender wants a particular security (see *specials* below).
- **Tri-party repo** — a third-party custodian bank (in the U.S., historically the clearing banks) sits between the two counterparties, holding the collateral, valuing it, applying haircuts, and managing substitutions. This dominates the financing of general collateral by money-market funds and other cash lenders because it outsources the operational burden.
- **Cleared repo (FICC / GCF)** — the Fixed Income Clearing Corporation (FICC) acts as central counterparty. **General Collateral Financing (GCF) repo** is a blind-brokered, FICC-cleared market that lets dealers trade general Treasury collateral anonymously and net their positions. FICC-sponsored repo has grown as a way to bring money funds and other cash lenders into centrally cleared trades.

**General collateral vs specials.** When the lender is indifferent to which specific security it receives (any Treasury of a given class will do), the trade is **general collateral (GC)** and prices off a broad GC rate. When a particular security is in high demand — for example, a bond needed to cover a short position — it trades **special**, meaning its repo rate falls (the holder can borrow cash cheaply because everyone wants that exact collateral). The spread between GC and a special rate reflects how scarce that specific bond is.

**Who uses repo.** The market links cash-rich lenders with collateral-rich borrowers:

- **Primary dealers and banks** finance their inventory of Treasuries and other bonds by repo-ing them out overnight, funding long positions cheaply rather than tying up their own capital.
- **Money-market funds** and other cash investors are the dominant cash lenders (reverse-repo side), earning a secured return on short-term cash.
- **Hedge funds** use repo to lever positions — most notably to finance long Treasury holdings in the cash-futures **basis trade** — obtaining leverage far larger than the cash they post, subject to the haircut.
- **The Federal Reserve** operates on both sides through its facilities (see below).

## Why It Matters

Repo is the wholesale funding market that keeps the financial system liquid day to day. Trillions of dollars of secured borrowing roll through it every night, letting dealers make markets, letting leveraged investors hold positions, and letting cash pools earn a safe return. When repo works, it is invisible; when it seizes, funding for the whole system tightens at once.

**The basis for SOFR.** [[sofr|SOFR]] is computed by the Federal Reserve Bank of New York as a volume-weighted median of rates on overnight **Treasury repo** transactions — tri-party, cleared bilateral, and GCF repo. Repo is therefore not just adjacent to SOFR; it is the underlying market SOFR measures, which is why understanding repo is a prerequisite for understanding the dollar's principal risk-free benchmark.

**Fed tools and the policy corridor.** The Fed uses repo to steer overnight rates within its target range:

- The **Overnight Reverse Repo Facility (ON RRP)** lets eligible counterparties (notably money-market funds) lend cash to the Fed overnight against Treasury collateral at an administered rate. It acts as a **floor** under money-market rates — no one lends below the rate they can earn risk-free at the Fed — and absorbs excess cash from the system.
- The **Standing Repo Facility (SRF)**, established in 2021, works in the opposite direction: it lets primary dealers and eligible banks borrow cash from the Fed against Treasuries at an administered rate, acting as a **ceiling** that caps how far repo rates can spike when collateral is plentiful but cash is scarce.

Together these facilities frame a corridor. Repo rates normally trade between the ON RRP floor and the SRF ceiling, alongside the [[fed-funds-rate]] and the interest the Fed pays on reserve balances, so movements in repo are read as signals about the balance of cash and collateral in the system.

## Stress Episodes

Repo has been at the centre of every major dollar-funding scare, precisely because it is where leverage and liquidity meet.

**The 2008 "run on repo."** In the financial crisis, repo was a primary transmission channel of distress. As doubts grew about the value of mortgage-related collateral, lenders raised haircuts and pulled back from lending against it. Firms that funded illiquid assets with overnight repo found they could not roll their funding — a **run on repo** rather than a run by retail depositors. This dynamic was central to the failures of **Bear Stearns** and **Lehman Brothers**, both of which relied heavily on short-term secured funding that evaporated as counterparties lost confidence.

**September 2019 repo spike.** Overnight repo rates jumped sharply above the Fed's target range over a few days when the supply of cash reserves fell short of the collateral needing financing — a collision of corporate tax payments and heavy Treasury settlement that drained reserves at the wrong moment. The episode showed that even a market as deep as Treasury repo can dislocate on **reserve scarcity**, and it directly motivated the Fed to resume large repo operations and, later, to stand up the permanent SRF.

**March 2020 dash-for-cash.** In the early pandemic panic, investors sold even safe assets to raise cash, and Treasury-market functioning deteriorated. Funding markets came under acute strain as everyone tried to raise liquidity at once, prompting massive Fed intervention — repo operations plus [[quantitative-easing|large-scale asset purchases]] — to restore orderly markets.

The common thread: repo transmits stress fast because it is short-dated and collateralised. When collateral values wobble or cash grows scarce, haircuts rise and lenders retreat, and borrowers who depend on rolling overnight funding are forced to sell.

## Risks

- **Counterparty and collateral risk.** Although repo is secured, the lender still faces [[counterparty-risk]]: if the borrower defaults, the lender must sell the collateral, and its protection is only as good as that collateral's value and liquidity. A default combined with a fall in collateral prices can leave the lender short — the exact scenario haircuts are meant to cover but do not always fully cover.
- **Haircut procyclicality.** Haircuts tend to be low in calm markets and rise abruptly in stress. Rising haircuts force borrowers to post more collateral or shrink positions at the worst time, amplifying deleveraging — a feedback loop between falling prices and tightening funding.
- **Fire-sale and deleveraging dynamics.** When funding is withdrawn, leveraged holders must sell collateral to repay loans, pushing prices down, which raises haircuts and margin calls further and triggers more selling. This [[forced-liquidation|fire-sale]] spiral is how a localised funding shock can cascade into a broad sell-off.
- **The basis-trade leverage angle.** Hedge funds finance long cash-Treasury positions in repo against offsetting short Treasury-futures positions — the **cash-futures basis trade**. Because the position is funded with repo at a small haircut, effective leverage is very high. A spike in repo rates, a jump in haircuts, or a margin call on the futures leg can force rapid unwinds, selling Treasuries into a falling market and feeding back into repo and Treasury-market stress. Regulators have repeatedly flagged the scale of this leveraged repo-funded basis position as a systemic vulnerability.

## Related

- [[sofr]] — computed directly from overnight Treasury repo transactions; repo is the market SOFR measures
- [[fed-funds-rate]] — the unsecured overnight benchmark that repo rates trade alongside within the policy corridor
- [[treasuries]] — the dominant repo collateral
- [[collateral]] — repo is a collateralised loan; haircuts and margining govern lender protection
- [[liquidity]] — repo is the core short-term funding and liquidity market
- [[quantitative-easing]] — Fed reserve creation and balance-sheet policy move repo conditions and rates
- [[forced-liquidation]] — haircut spirals and margin calls in repo drive fire-sale deleveraging
- [[counterparty-risk]] — the residual risk a repo lender bears despite holding collateral

## Sources

- Federal Reserve Bank of New York — repo and reverse-repo operations, the Overnight Reverse Repo Facility, the Standing Repo Facility, and SOFR methodology (general, publicly documented material; no specific figures reproduced here).
- Bank for International Settlements (BIS) — analyses of repo-market structure, the September 2019 repo dislocation, and funding-market plumbing.
- General, widely-taught fixed-income and money-market knowledge on repo mechanics, haircuts, tri-party and cleared repo, the 2008 "run on repo," the March 2020 dash-for-cash, and the Treasury cash-futures basis trade.
