---
title: "Credit Rating Agencies"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [regulation, history]
aliases: ["CRAs", "Moody's", "S&P Ratings", "Fitch", "Credit Rating Agency"]
domain: [market-microstructure]
prerequisites: ["[[bond-market]]"]
difficulty: beginner
related: ["[[subprime-mortgage]]", "[[2008-global-financial-crisis]]", "[[bond-market]]", "[[corporate-bonds]]", "[[credit-default-swaps]]", "[[credit-cycle]]", "[[moral-hazard]]", "[[dodd-frank-act]]"]
---

# Credit Rating Agencies

Credit rating agencies (CRAs) are firms that assess the creditworthiness of debt issuers and their securities, assigning letter grades (AAA, AA, BBB, etc.) that indicate the likelihood of default. The three dominant agencies -- Moody's, Standard & Poor's (S&P), and Fitch -- collectively control approximately 95% of the global ratings market.

## How Ratings Work

- **Investment grade**: AAA through BBB- (S&P/Fitch) or Aaa through Baa3 (Moody's). Eligible for most institutional investors.
- **High yield ("junk")**: BB+ and below. Higher default risk, higher yields. Many institutional mandates prohibit holding junk-rated debt.
- **Downgrade triggers**: A downgrade from investment grade to junk can force institutional selling, creating cascading price declines.

## The 2008 Failure

Credit rating agencies played a central role in the [[2008-global-financial-crisis]]. They assigned AAA ratings to [[subprime-mortgage]]-backed CDOs that were fundamentally high-risk, enabling these toxic securities to be sold to pension funds, insurance companies, and banks worldwide. The agencies operated under a **conflict of interest**: they were paid by the issuers whose securities they rated (the "issuer-pays" model), creating incentive to assign favorable ratings.

## Post-Crisis Reforms

The [[dodd-frank-act]] increased regulatory oversight of CRAs, required greater transparency in methodologies, and attempted to reduce overreliance on ratings in financial regulation. However, the fundamental structure of the ratings industry -- including the issuer-pays model -- remains largely intact.

## Why It Matters for Traders

Credit ratings directly affect [[bond-market]] prices, corporate borrowing costs, and institutional portfolio allocations. Rating changes can move markets sharply, and understanding the limitations and conflicts inherent in the ratings process helps traders avoid blind reliance on agency assessments. A key trading dynamic is the **"fallen angel"** — a bond downgraded from investment grade (BBB-) to high yield (BB+) forces mandate-constrained holders (pension funds, insurers, index funds) to sell regardless of price, creating mechanical, non-fundamental selling pressure. Traders anticipate these downgrade cliffs by watching [[credit-default-swaps|CDS]] spreads, which typically move ahead of agency action. Sovereign downgrades (e.g., the 2011 S&P downgrade of US Treasuries) can move global rates and risk assets.

## Related

- [[subprime-mortgage]] — toxic securities rated AAA before 2008
- [[2008-global-financial-crisis]] — the agencies' central role and conflict of interest
- [[credit-default-swaps]] — market-implied default risk, often a leading indicator vs. ratings
- [[credit-cycle]] — ratings and spreads as cycle-position signals
- [[bond-market]] — where ratings determine pricing and eligibility
- [[corporate-bonds]] — investment-grade vs. high-yield classification
- [[moral-hazard]] — the issuer-pays incentive distortion
- [[dodd-frank-act]] — post-crisis reform of CRA oversight

## Sources

- U.S. Securities and Exchange Commission, "Annual Report on Nationally Recognized Statistical Rating Organizations" (NRSRO market-share data).
- Financial Crisis Inquiry Commission (2011). *Final Report* (chapter on rating agencies and the issuer-pays conflict).
- White, L. (2010). "Markets: The Credit Rating Agencies." *Journal of Economic Perspectives.*
