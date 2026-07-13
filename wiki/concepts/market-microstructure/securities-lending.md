---
title: "Securities Lending"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [market-microstructure, short-selling, trading-mechanics, leverage]
aliases: ["stock lending", "stock loan", "borrow rate", "securities finance"]
domain: [market-microstructure]
prerequisites: ["[[short-selling]]", "[[margin]]"]
difficulty: intermediate
related: ["[[short-selling]]", "[[rehypothecation]]", "[[short-interest]]", "[[float]]", "[[gamestop-short-squeeze]]", "[[shadow-banking]]", "[[sec]]"]
---

# Securities Lending

Securities lending is the temporary transfer of securities from a lender (typically a long-term institutional holder or custodian) to a borrower (typically a broker-dealer or hedge fund), most often to facilitate [[short-selling]]. The borrower posts collateral and pays a fee (the **borrow rate**) for the duration of the loan; the lender earns incremental yield on otherwise idle holdings while retaining the economic exposure of the position.

## How It Works

1. A trader wants to short a stock they do not own.
2. Their broker **locates** available shares from a lender — often a pension fund, mutual fund, index fund, or ETF provider holding large long positions.
3. The borrower posts collateral (typically **102–105%** of the securities' market value, marked to market daily) and pays a borrow rate, which ranges from under 1% annually for "general collateral" (easy-to-borrow) names to **50%+** for "special" hard-to-borrow ("HTB") names.
4. The borrowed shares are sold in the open market. When the short seller closes the position, they buy shares back and return them to the lender.

The lender continues to receive substitute payments in lieu of dividends and any distributions, and can recall the loan at any time. The economics are driven by supply and demand for the specific security: scarce borrow + heavy short demand drives the rate up.

## The Securities-Lending Chain

Securities lending sits at the heart of [[shadow-banking]] collateral flows. Lenders typically reinvest the cash collateral they receive, and the borrowed securities are frequently re-lent via [[rehypothecation]] — the same shares may be borrowed and re-lent through several intermediaries. This collateral reuse is how aggregate [[short-interest]] can exceed 100% of a stock's [[float]], as occurred with GameStop before the [[gamestop-short-squeeze]].

## Key Terms

- **Borrow Rate (fee):** The annualized cost to borrow shares. Spikes when a stock is in high short demand; a leading indicator of squeeze risk.
- **Locate:** Confirmation that shares are available to borrow before executing a short sale, required by [[sec]] Regulation SHO.
- **Recall:** A lender can recall lent shares at any time, forcing the borrower to return them or source replacements — a recall during a squeeze can force buy-ins.
- **General Collateral (GC) vs. Special:** GC trades near the benchmark rate; "specials" trade at elevated, sometimes punitive, rates.
- **Rebate Rate:** For cash-collateralized loans, the interest the lender pays back to the borrower on the cash; a deeply negative rebate signals an expensive borrow.
- **Fail-to-Deliver (FTD):** When shares are not delivered by settlement, creating settlement stress and "phantom" exposure.

## Trading Relevance

Securities-lending mechanics are critical for short sellers and anyone trading heavily shorted stocks:

- **Cost of carry on shorts:** The borrow rate is the recurring cost of a short position; a 50% borrow can wipe out a profitable short thesis if the move is slow.
- **Squeeze early-warning:** Rising borrow rates and a falling utilization-adjusted supply of lendable shares signal mounting pressure. Data vendors (S3 Partners, Ortex, IHS Markit) sell exactly this borrow/utilization data.
- **Buy-side income:** For long-only funds and ETF providers, lending out holdings is a meaningful incremental return stream — but it introduces [[counterparty-risk]] and collateral-reinvestment risk (a key channel in the 2008 crisis via AIG's lending program).
- **Squeeze fragility:** The [[gamestop-short-squeeze]] showed how [[rehypothecation]] and excessive [[short-interest]] create fragility; understanding lending mechanics is essential for assessing squeeze risk on either side.

## Related

- [[short-selling]]
- [[rehypothecation]]
- [[short-interest]]
- [[float]]
- [[gamestop-short-squeeze]]
- [[shadow-banking]]
- [[sec]]

## Sources

- US SEC, Regulation SHO (locate and close-out requirements for short sales).
- International Securities Lending Association (ISLA), securities-lending market reports.
- Faulkner, Mark C. "An Introduction to Securities Lending" (5th ed.), Securities Lending and Repo Committee.
- Duffie, Garleanu, and Pedersen, "Securities Lending, Shorting, and Pricing," Journal of Financial Economics (2002).
