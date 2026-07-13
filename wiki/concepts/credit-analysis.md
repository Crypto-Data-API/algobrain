---
title: "Credit Analysis"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, bonds, risk-management, valuation]
aliases: ["Credit Analysis", "Credit Research", "Creditworthiness Assessment"]
related: ["[[fundamental-analysis]]", "[[bonds]]", "[[credit-spread]]", "[[credit-risk]]", "[[counterparty-risk]]", "[[credit-rating-agencies]]", "[[financial-statement-analysis]]", "[[default-risk]]", "[[interest-coverage-ratio]]", "[[credit-cycle]]", "[[recession]]"]
domain: [fundamental-analysis, risk-management]
prerequisites: ["[[fundamental-analysis]]", "[[bonds]]"]
difficulty: intermediate
---

**Credit analysis** is the assessment of a borrower's ability and willingness to meet its debt obligations — the discipline behind bond investing, lending, and [[counterparty-risk|counterparty]] evaluation. It estimates the probability of default and the likely recovery if default occurs, and translates that into a fair [[credit-spread]] or a lend/no-lend decision. Where equity analysis asks "how much can this company be worth?", credit analysis asks the narrower, asymmetric question "will I get paid back, and what do I lose if I don't?" — a payoff that caps upside at par-plus-coupon while exposing the full downside of default, which is why credit work is fundamentally about avoiding losers rather than picking winners.

## The Core Equation of Credit Risk

Almost all of credit analysis reduces to estimating the components of **expected loss**:

$$\text{Expected Loss} = PD \times LGD \times EAD$$

- **PD — probability of default**: the chance the borrower fails to pay over a horizon (1-year or cumulative to maturity).
- **LGD — loss given default**: the fraction *not* recovered, i.e. `1 − recovery rate`. Driven by seniority and collateral.
- **EAD — exposure at default**: the amount outstanding when default occurs (relevant for revolving/derivative exposures).

A bond's [[credit-spread]] over the risk-free curve must, in equilibrium, compensate for this expected loss plus a risk premium for the *uncertainty* around it. A rough first approximation often used as a sanity check is `spread ≈ PD × LGD`; a wider observed spread implies the market demands extra premium for liquidity and default-timing risk.

## How It Works

Credit analysts evaluate a borrower across several dimensions, classically framed as the **"Five Cs of Credit"**:

| C | Question it answers | What analysts look at |
|---|---|---|
| **Character** | Will they pay? | Management track record, payment history, governance, willingness to honour obligations |
| **Capacity** | Can they pay from cash flow? | Coverage ratios, free cash flow, earnings stability |
| **Capital** | Is there an equity cushion below me? | Leverage, equity value, skin in the game |
| **Collateral** | What backs the loan if they don't pay? | Pledged assets, security, lien priority |
| **Conditions** | Is the environment supportive? | Macro/[[credit-cycle|cycle]], industry, rate environment, use of proceeds |

For corporate issuers this is operationalized through [[financial-statement-analysis|financial-statement analysis]] focused on leverage and coverage:

| Dimension | Representative metric | What it gauges | Direction that helps credit |
|---|---|---|---|
| **Leverage** | Debt/EBITDA, Net Debt/EBITDA, Debt/Equity | Stock of obligation vs earnings power | Lower |
| **Coverage** | [[interest-coverage-ratio|EBIT / interest]], EBITDA/interest, fixed-charge coverage | Cushion between earnings and required payments | Higher |
| **Cash flow** | Free cash flow, FCF/Debt, cash-flow stability | Ability to service debt with *cash*, not accruals | Higher / steadier |
| **Liquidity** | Current ratio, cash on hand, maturity-wall coverage | Can near-term obligations be met and debt rolled? | Higher |
| **Structure** | Seniority, security, covenant package | Where you rank in bankruptcy → recovery | More senior / secured |

Debt is serviced with cash, not accounting earnings, so cash-flow quality (see [[accrual-accounting]] and [[free-cash-flow]]) is central — a borrower with high reported profit but weak cash conversion is a classic credit trap. Seniority and security drive recovery rates: secured and senior creditors rank above subordinated holders and equity in bankruptcy.

The output is a credit assessment, often expressed on the scale used by the [[credit-rating-agencies|rating agencies]] (Moody's, S&P, Fitch). The further down the scale, the higher the modeled default probability and the wider the [[credit-spread|credit spread]] demanded.

### Rating Scale and Default/Recovery Tendencies

The single most important threshold is **investment grade vs. high yield**, because many institutional mandates can only hold investment-grade paper — a downgrade across that line forces selling and widens spreads.

| Tier | S&P / Fitch | Moody's | Character | Relative default tendency |
|---|---|---|---|---|
| Investment grade | AAA … BBB− | Aaa … Baa3 | "Prime" to "lower-medium grade" | Low; rises gradually down the scale |
| High yield ("junk") | BB+ … B− | Ba1 … B3 | "Speculative" | Materially higher, cycle-sensitive |
| Distressed / default | CCC … D | Caa … C | Substantial risk to default | Very high; CCC defaults cluster in recessions |

Recovery rates are *illustrative ranks*, not fixed numbers — senior secured debt historically recovers far more than subordinated or unsecured debt, and recoveries fall in recessions when many issuers default at once (correlation between PD and LGD). A **"fallen angel"** is an issuer downgraded from investment grade to high yield; a **"rising star"** is the reverse — both are fertile ground for relative-value trades because the forced-flow dynamics around the IG/HY boundary can dislocate prices from fundamentals.

## Quantitative and Market-Based Approaches

Beyond ratio analysis, credit risk is also estimated with:

- **Structural (Merton) models** — treat a firm's equity as a call option on its assets; default occurs when asset value falls below the debt level at maturity. Inputs are asset value, asset volatility, and the debt level. Moody's KMV "distance-to-default" is the best-known commercial implementation.
- **Reduced-form / market-implied models** — back out default probability from observed [[credit-spread|credit spreads]] and credit default swap (CDS) prices. Using the approximation `spread ≈ PD × LGD`, a market-implied PD can be solved as `PD ≈ spread / LGD`.
- **Statistical scores** — e.g., the **Altman Z-score**, which combines five balance-sheet/market ratios into a single bankruptcy-risk indicator (a higher Z is safer; low scores flag distress).

## Worked Example — Reading the Spread

Suppose a high-yield bond trades at a [[credit-spread]] of **400 bps (4%)** over the equivalent-maturity Treasury, and a recovery assumption of **40%** is standard for senior unsecured debt (so LGD = 60%). Using the reduced-form approximation:

$$PD \approx \frac{\text{spread}}{\text{LGD}} = \frac{0.04}{0.60} \approx 6.7\%\ \text{annual implied default probability}$$

Your job as a credit analyst is to form an *independent* estimate of PD and LGD from the fundamentals (leverage trend, coverage, liquidity runway, covenant protection, collateral). If your bottom-up work says the true PD is closer to 3%, the bond is **cheap** — the market is over-pricing default — and it is a relative-value *buy* (a "money-good" credit yielding more than it should). If your work says PD is really 12% and the company faces a near-term maturity wall it cannot refinance, the bond is **rich** and you avoid or short it (e.g. via CDS). This gap between fundamental PD and market-implied PD is the core of fundamental credit trading. *(Numbers illustrative.)*

## Trading Relevance

Credit analysis drives several trading and risk activities:

- **Bond and credit selection** — buying issuers whose actual creditworthiness is better than their spread implies (relative-value credit), and avoiding "fallen angels" before downgrades widen spreads.
- **Credit spreads as a macro signal** — widening high-yield spreads are a classic risk-off / [[recession]] warning; the spread between junk and Treasuries is a real-time market verdict on systemic credit stress, and credit often leads equities at turning points (see [[credit-cycle]]).
- **[[counterparty-risk|Counterparty risk]] management** — assessing the solvency of brokers, exchanges, and trading counterparties (acutely relevant in crypto after multiple exchange/lender failures).
- **Capital structure / event-driven trades** — distressed-debt, capital-structure arbitrage, and merger-arb strategies hinge on recovery estimates and covenant analysis (which tranche of the stack is "money-good"?).
- **Hedging and basis trades** — comparing a bond's cash spread against its CDS to trade the **CDS-bond basis** when the two diverge.

### Common Pitfalls

- **Over-reliance on agency ratings** — ratings are lagging, conflicted (issuer-paid), notch-coarse, and were badly wrong on structured credit in 2008. Watch market-implied spreads, which move faster than ratings.
- **Earnings ≠ cash** — a borrower can show healthy accrual profit while burning cash; always validate coverage with [[free-cash-flow]] and watch the [[accrual-accounting|accruals]] gap.
- **The maturity wall / refinancing risk** — a solvent issuer can still default if it cannot *roll* maturing debt when markets close; map the maturity schedule against expected market access.
- **Covenant erosion** — "cov-lite" loans and aggressive EBITDA add-backs flatter leverage and reduce creditor protection; read the documents, not just the ratios.
- **PD-LGD correlation** — defaults and low recoveries cluster in the same bad states (recessions), so models that assume independence understate tail loss.
- **Survivorship in spreads** — a tight average spread can mask a fat tail of issuers about to deteriorate; concentration and dispersion matter as much as the mean.

## Sources

- Fabozzi, Frank J. *Bond Markets, Analysis, and Strategies.* — credit analysis and ratings.
- Altman, Edward I. (1968), "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy," *Journal of Finance* (the Z-score).
- Merton, Robert C. (1974), "On the Pricing of Corporate Debt: The Risk Structure of Interest Rates," *Journal of Finance*.
- CFA Institute curriculum — Fixed Income: Fundamentals of Credit Analysis.

## Related

- [[bonds]] — the primary instruments credit analysis prices
- [[credit-spread]] — the market price of credit risk
- [[credit-risk]] — the risk class credit analysis measures
- [[default-risk]] — the probability-of-default leg of expected loss
- [[credit-rating-agencies]] — institutional credit assessment
- [[credit-cycle]] — the macro backdrop that swings default and recovery rates
- [[counterparty-risk]] — applying credit analysis to trading counterparties
- [[financial-statement-analysis]] — the toolkit for corporate credit
- [[interest-coverage-ratio]] — a key coverage metric
- [[free-cash-flow]] / [[accrual-accounting]] — the cash backing behind coverage
- [[fundamental-analysis]] — the broader analytical discipline
