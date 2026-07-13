---
title: "Shadow Banking"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [market-microstructure, risk-management, leverage]
aliases: ["Shadow Banking System", "Non-Bank Financial Intermediaries", "NBFI", "market-based finance"]
domain: [market-microstructure]
prerequisites: ["[[leverage]]", "[[liquidity]]"]
difficulty: advanced
related: ["[[leverage]]", "[[systemic-risk]]", "[[rehypothecation]]", "[[securities-lending]]", "[[counterparty-risk]]", "[[2008-global-financial-crisis]]"]
---

# Shadow Banking

**Shadow banking** (increasingly termed **non-bank financial intermediation, NBFI**, or **market-based finance**) refers to credit intermediation that occurs outside the traditional, regulated banking system. It encompasses the institutions and activities that perform bank-like functions — maturity transformation, liquidity transformation, leverage, and credit creation — without the deposit insurance, capital requirements, or central-bank backstop that govern chartered banks.

## What Counts as Shadow Banking

Entities and instruments commonly included:

- **Money market funds (MMFs)** — offer deposit-like redeemability but invest in short-term paper
- **Repo markets** — short-term collateralized borrowing that funds dealer balance sheets
- **Securities-lending programs** — see [[securities-lending]] and [[rehypothecation]]
- **Hedge funds and prime brokerage** — leveraged trading financed through dealers
- **Structured investment vehicles (SIVs) and conduits** — held mortgage and asset-backed paper off-balance-sheet
- **Asset-backed commercial paper (ABCP)** and **securitizations** (MBS, CDOs)
- **Finance companies and unregulated lenders** — including the offshore intermediaries that offer extreme [[leverage]] ratios prohibited under standard banking rules

The Financial Stability Board's "narrow measure" of NBFI activities that pose bank-like risks has been estimated in the tens of trillions of dollars globally.

## How It Works: Bank Functions Without a Bank

A bank takes short-term deposits and makes long-term loans (**maturity transformation**), turning illiquid assets into liquid claims (**liquidity transformation**), using [[leverage]]. Shadow banking replicates this chain across markets rather than inside one balance sheet:

> Saver → money market fund → repo / commercial paper → dealer → securitized assets

Each link is a separate, lightly-regulated entity, and the chain depends on continuous **rollover** of short-term funding. The fragility is structural: because shadow banks have no deposit insurance and no guaranteed access to the central-bank discount window, a loss of confidence triggers a **run** — wholesale lenders simply decline to roll over funding, forcing fire sales of the long-term assets.

## The 2008 Crisis

The [[2008-global-financial-crisis|2008 financial crisis]] was, at its core, a run on the shadow banking system. When subprime losses cast doubt on the value of mortgage-backed collateral:

- **Repo haircuts spiked**, withdrawing funding from dealers (Gorton and Metrick's "run on repo").
- **ABCP markets froze**, stranding SIVs.
- The **Reserve Primary Fund "broke the buck"** in September 2008, triggering a run on prime money market funds.

The interconnections with regulated banks proved far deeper than regulators understood — banks had provided liquidity backstops to off-balance-sheet vehicles, pulling the losses back onto their books.

## Trading Relevance

- **Systemic risk barometer:** Repo rates, MMF flows, and [[securities-lending]] utilization are real-time stress gauges. The September 2019 repo spike and March 2020 "dash for cash" both originated in shadow-banking plumbing and moved every asset class.
- **Funding-liquidity channel:** Leveraged traders depend on shadow-banking funding (repo, prime brokerage). A widening of haircuts or borrow costs forces deleveraging regardless of fundamentals — a key mechanism behind correlated drawdowns and [[counterparty-risk]].
- **Collateral chains:** [[rehypothecation]] and collateral reuse inside shadow banking amplify [[leverage]] system-wide; falling collateral velocity is an early deleveraging signal.
- **Regulatory arbitrage watch:** Activity migrates to wherever capital rules are loosest. After post-2008 bank regulation, leveraged lending, private credit, and crypto lending grew rapidly as the new shadow-banking frontier — and the 2022 crypto-lender collapses (Celsius, Voyager) were a textbook shadow-banking run.

## Related

- [[leverage]]
- [[systemic-risk]]
- [[rehypothecation]]
- [[securities-lending]]
- [[counterparty-risk]]
- [[2008-global-financial-crisis]]

## Sources

- Pozsar, Adrian, Ashcraft, and Boesky. "Shadow Banking." Federal Reserve Bank of New York Staff Report No. 458 (2010).
- Gorton, Gary, and Andrew Metrick. "Securitized Banking and the Run on Repo." Journal of Financial Economics (2012).
- Financial Stability Board, "Global Monitoring Report on Non-Bank Financial Intermediation" (annual).
- McCulley, Paul. PIMCO commentary coining the term "shadow banking system" (2007).
