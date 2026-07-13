---
title: "Cash Conversion Cycle"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [fundamental-analysis, valuation, indicators, liquidity]
domain: [fundamental-analysis]
difficulty: intermediate
aliases: ["CCC", "Cash Cycle", "Net Operating Cycle"]
prerequisites: ["[[balance-sheet]]"]
related: ["[[balance-sheet]]", "[[accrual-accounting]]", "[[current-ratio]]", "[[free-cash-flow]]", "[[gross-profit]]", "[[stock-turn]]", "[[gmroi]]", "[[alfred-fundamental-analysis]]"]
---

The **Cash Conversion Cycle (CCC)** measures how many days it takes a company to convert its investment in inventory and other operating resources into cash collected from customers. It chains three operating timings: how long inventory sits before being sold, how long it takes to collect payment after the sale, and how long the company is able to delay paying its own suppliers. A shorter CCC means cash is tied up for less time — a powerful, self-funding source of working capital.

## Formula

$$\text{CCC} = \text{DIO} + \text{DSO} - \text{DPO}$$

Where each component (all in days) is:

- **DIO** — Days Inventory Outstanding = (Average Inventory / COGS) × 365
- **DSO** — Days Sales Outstanding = (Average Accounts Receivable / Revenue) × 365
- **DPO** — Days Payable Outstanding = (Average Accounts Payable / COGS) × 365

Intuitively: *days my cash is locked in stock + days waiting to be paid − days I can defer paying suppliers.* All inputs come from the [[balance-sheet]] (averaged across the period) and the income statement.

The first two legs (DIO + DSO) form the **operating cycle** — total time from buying inventory to collecting cash. Subtracting DPO (supplier financing) gives the **cash** conversion cycle: the portion of the operating cycle the company must fund itself.

### Worked example

A specialty retailer reports for the year:

- Revenue = $1,000m
- COGS = $600m
- Average inventory = $120m
- Average accounts receivable = $50m
- Average accounts payable = $90m

| Component | Calculation | Result |
|---|---|---|
| **DIO** | (120 / 600) × 365 | **73.0 days** |
| **DSO** | (50 / 1,000) × 365 | **18.3 days** |
| **DPO** | (90 / 600) × 365 | **54.8 days** |
| Operating cycle | DIO + DSO | 91.3 days |
| **CCC** | 73.0 + 18.3 − 54.8 | **≈ 36.5 days** |

So this firm has roughly $1,000m × (36.5 / 365) ≈ **$100m of cash tied up** in the operating cycle at any moment — capital that grows in lock-step with sales. If the company negotiates supplier terms from 55 to 75 days (DPO → 75) and trims inventory so DIO falls to 60, the CCC drops to 60 + 18.3 − 75 ≈ **3.3 days**, freeing roughly $90m of cash *without raising a dollar of external financing*. That released working capital is the prize the CCC quantifies.

## Interpretation

| CCC | Meaning |
|-----|---------|
| Negative | Excellent — the company collects from customers *before* it pays suppliers, so suppliers finance growth (Amazon, supermarkets, Dell's classic build-to-order model) |
| Low (0–30 days) | Efficient working-capital management |
| 30–60 days | Typical for many industries |
| 90+ days | Capital-intensive — significant cash locked in operations; growth consumes cash |

A **negative CCC is a structural moat**: it lets a company grow without external financing, because each new sale is funded by supplier credit. A **rising CCC** over time is a warning — inventory building up unsold, customers paying slower, or suppliers tightening terms.

### Typical CCC by business model

CCC is only meaningful *relative to peers and the company's own history* — business models sit at very different points on the spectrum:

| Business model | Typical CCC | Why |
|---|---|---|
| Supermarket / discount grocer | Negative | Cash sales (low DSO), fast inventory turn, long supplier terms |
| Build-to-order tech (classic Dell), large-cap retailer with scale | Negative to ~0 | Customers/suppliers finance the cycle; huge payable leverage |
| Apparel / specialty retail | ~30–90 days | Seasonal inventory, markdown risk lengthens DIO |
| Industrial / capital goods | ~60–120+ days | Long production cycles, B2B receivables (high DSO) |
| Pharma / biotech with long shelf inventory | High | Regulatory + long-dated inventory locks up cash |

A grocer's negative CCC and an industrial's 100-day CCC are *both* normal; the signal is the *trend* and the *gap to direct competitors*, not the absolute level across sectors.

## Trading Relevance

- **Cash-flow forecasting.** CCC translates directly into how much cash growth will consume. A retailer with a 70-day CCC needs ~70 days of sales in working capital to fund expansion; a negative-CCC business is effectively paid to grow.
- **Quality and trend signal.** A *deteriorating* CCC frequently precedes earnings or cash-flow disappointments — receivables ballooning faster than sales is a classic channel-stuffing tell, linking CCC to [[accrual-accounting|accrual]] earnings-quality screens.
- **Competitive read.** Comparing CCC across peers reveals operational efficiency and supplier bargaining power that margins alone hide. "Companies survive on cash flow" — the CCC quantifies exactly how efficiently the [[balance-sheet]] generates that cash (Source: [[fred-sam-session-2024-01-02]]).
- **Component diagnosis.** Decompose the move: a rising CCC driven by DSO (collection problems) is more alarming than one driven by deliberate inventory pre-build ahead of a launch. The inventory leg connects to [[stock-turn]] and, for retail, [[gmroi]].

## How analysts and traders use the CCC

- **Decompose before you judge.** Always split a CCC change into its DIO / DSO / DPO drivers. The *same* +10-day move means very different things:
  - **DIO ↑** — inventory piling up unsold (demand softening, obsolescence/markdown risk ahead) — bearish, unless it's a deliberate pre-launch build.
  - **DSO ↑** — customers paying slower, or revenue pulled forward on loose credit (a classic [[accrual-accounting|channel-stuffing]] / earnings-quality red flag).
  - **DPO ↑** — usually *good* (more supplier financing), but an abrupt jump can signal a cash crunch where the firm is *stretching* payables to survive.
- **Lead indicator for FCF.** A widening CCC consumes cash that hits [[free-cash-flow|free cash flow]] *before* it shows up in accrual earnings — a reason CCC trends often front-run cash-flow misses and dividend/buyback risk.
- **Screen the trend, not the snapshot.** Plot CCC over 8–12 quarters against direct peers. Steady or falling CCC alongside growth = self-funding compounder; rising CCC alongside "growth" = growth that is quietly burning cash.
- **Cross-check liquidity.** Read CCC alongside the [[current-ratio]] and [[working-capital]] balance — CCC adds the *dynamic timing* that the static liquidity ratios miss.

## Common pitfalls

- **Using period-end instead of average balances** — seasonal businesses (a retailer at fiscal year-end after Christmas clearance) can show a wildly unrepresentative inventory figure; use *average* balances.
- **Cross-sector comparison** — a negative grocer CCC vs. a 100-day industrial CCC is meaningless as a head-to-head; only peers and own-history comparisons inform.
- **Treating negative CCC as risk-free** — supplier-financed growth is a moat *until* suppliers tighten terms or demand falls; the financing can reverse quickly in a downturn.
- **Confusing "good" DPO with health** — stretching payables raises DPO and *lowers* CCC, but extreme DPO can mask a company unable to pay on time.
- **Inconsistent denominators** — DSO is conventionally computed on revenue while DIO and DPO use COGS; mixing them up distorts the result.

## Related

- [[balance-sheet]] — source of inventory, receivables, payables inputs
- [[accrual-accounting]] — CCC measures the cash timing of operating accruals
- [[current-ratio]] — static liquidity; CCC adds the dynamic timing view
- [[free-cash-flow]] — working-capital changes feed directly into FCF
- [[stock-turn]] — inventory-turnover component (inverse of DIO)
- [[inventory-turnover]] — the velocity behind the DIO leg
- [[working-capital]] — what the CCC ties up and releases
- [[gmroi]] — retail-specific working-capital efficiency variant
- [[gross-profit]] — revenue and COGS feed the CCC components
- [[retail-metrics]] — sector KPIs that sit alongside the inventory leg
- [[alfred-fundamental-analysis]] — cash-flow assessment

## Sources

- CFA Institute, *Financial Statement Analysis* curriculum — working-capital and operating-cycle metrics
- Aswath Damodaran, *Investment Valuation* — working capital and reinvestment in cash-flow forecasting
- [[fred-sam-session-2024-01-02]] — "Companies survive on cash flow"
