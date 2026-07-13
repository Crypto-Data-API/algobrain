---
title: "Tangible Book Value"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, metrics]
aliases: ["TBV", "tangible book value", "tangible-book-value", "Tangible Book Value", "tangible common equity", "TCE", "price-to-tangible-book-value", "P/TBV", "P/TBV ratio", "tangible book value per share"]
domain: [fundamental-analysis]
prerequisites: ["[[book-value]]", "[[balance-sheet]]"]
difficulty: intermediate
related: ["[[book-value]]", "[[price-to-book-ratio]]", "[[balance-sheet]]", "[[return-on-equity]]", "[[net-current-asset-value]]", "[[fundamental-analysis]]", "[[intangible-assets]]", "[[goodwill]]"]
---

**Tangible book value (TBV)** is a company's [[book-value|book value]] after stripping out **intangible assets** — goodwill, patents, brands, capitalized software, and similar non-physical items. It is the accounting estimate of what shareholders would be left with if the firm were wound down and only its hard, sellable assets counted. The per-share version is **tangible book value per share (TBVPS)**, and the valuation multiple built on it — **price-to-tangible-book-value (P/TBV)** — is the dominant yardstick for banks and other balance-sheet-driven businesses.

## Formula

$$\text{Tangible Book Value} = \text{Total Equity} - \text{Intangible Assets} - \text{Goodwill}$$

$$\text{TBV per Share} = \frac{\text{Tangible Book Value}}{\text{Shares Outstanding}}$$

$$\text{P/TBV} = \frac{\text{Share Price}}{\text{Tangible Book Value per Share}}$$

Some practitioners also subtract preferred equity to isolate **tangible common equity (TCE)**, the capital that genuinely backs the common shareholder. All inputs come from the [[balance-sheet|balance sheet]] and the share count.

## Why Strip Out Intangibles?

[[book-value|Book value]] (total equity) includes **goodwill** — the premium a company paid above fair value when it made acquisitions. Goodwill is not a saleable asset; it cannot be pledged, liquidated, or used to absorb losses, and it is the first thing written off when an acquisition disappoints (a goodwill impairment). Tangible book value removes this soft, judgment-laden layer to give a more conservative, downside-oriented floor on value. For a serial acquirer that has paid up for deals, the gap between book value and tangible book value can be enormous, and a P/B below 1 can coexist with a P/TBV well above 1.

## Worked Example

A bank reports:

- Total shareholders' equity: $12.0 billion
- Goodwill and other intangibles: $2.0 billion
- Shares outstanding: 500 million
- Share price: $24.00

$$\text{TBV} = 12.0 - 2.0 = \$10.0\text{ billion}$$
$$\text{TBVPS} = \frac{10.0\text{bn}}{500\text{m}} = \$20.00$$
$$\text{P/TBV} = \frac{24.00}{20.00} = 1.2\times$$

The market is paying 1.2 times the bank's tangible net worth. Whether that is cheap or rich depends on how much return the bank earns on that capital (see below).

## P/TBV and the Bank Valuation Framework

Banks and insurers are valued primarily on **P/TBV cross-referenced against return on tangible common equity (ROTCE)**, not on revenue multiples or EV/EBITDA. The logic is a direct relationship:

- A bank that earns a **high, durable ROTCE** (say 15%+) deserves to trade at a **premium** to tangible book (P/TBV well above 1).
- A bank earning a **return below its cost of equity** should trade **at or below 1x** tangible book — the market is signalling that each retained dollar is worth less than a dollar.
- A persistent **sub-1x P/TBV** is the classic bank turnaround setup: the thesis is that ROTCE recovers toward peers and the multiple re-rates up toward (and past) 1x.

Buying back stock **below** tangible book value is accretive to TBV per share (it retires shares for less than their tangible worth), while buying back **above** TBV dilutes it — a reason capital-return-focused investors track the buyback price against TBVPS.

## Typical Ranges

P/TBV is most meaningful for financials and asset-heavy firms:

- **High-quality banks (strong, stable ROTCE)**: 1.5–2.5x+
- **Average banks**: ~1.0–1.5x
- **Troubled / low-return banks**: below 1.0x
- **Asset-light, intangible-rich firms** (software, brands): P/TBV is often very high or even negative and is **not a useful metric** — for these, tangible book value can be near zero because almost all the value is intangible.

## Interpretation Notes

- **Negative tangible book value** is common and not automatically alarming for intangible-heavy businesses (a software firm or a brand-led consumer company funded by buybacks); for a bank it would be a serious solvency warning.
- TBV is a **liquidation-style floor**, useful in deep-value and distressed analysis, but it ignores the going-concern earning power that drives most of a healthy company's worth.
- For asset-light businesses, value lives in intangibles, people, and network effects that TBV deliberately excludes — so a low P/TBV there is a feature of the business model, not a bargain.

## Tangible Book Value vs. Related Measures

- **[[book-value|Book value]] / P/B** — includes goodwill and intangibles; TBV is the stricter, more conservative version.
- **[[net-current-asset-value|Net current asset value]] (NCAV)** — Graham's even harsher "net-net" measure that counts only current assets minus *all* liabilities.
- **[[intrinsic-value|Intrinsic value]]** — a forward, cash-flow-based estimate; TBV is a backward-looking balance-sheet figure.

## Limitations

1. **Useless for asset-light businesses** — where value is overwhelmingly intangible, TBV understates worth severely.
2. **Book values are historical cost** — assets carried at depreciated cost (or, for banks, loans at amortized cost) may not reflect current market value, in either direction.
3. **Hidden asset quality** — a bank's tangible book is only as good as its loan book; understated loan-loss reserves can make TBV look healthier than it is.
4. **Ignores earning power** — a high-ROTCE franchise is worth far more than its tangible book; a low-return one, far less. P/TBV must always be paired with ROTCE/ROE to be meaningful.

## Trading Relevance

P/TBV is the workhorse multiple for trading and investing in **banks, insurers, and other balance-sheet-driven financials**, where headline operating/net margins and EV/EBITDA are accounting artifacts. The core trade is the **P/TBV-versus-ROTCE re-rating**: identify a financial trading below the multiple its return-on-tangible-equity justifies and bet on convergence, often catalysed by improving credit conditions, rising net interest margins, or buybacks executed below TBV that mechanically grow TBV per share. In deep-value and distressed equity, tangible book provides a downside anchor for margin-of-safety estimates. Conversely, applying P/TBV to asset-light, intangible-heavy companies is a common analytical error that makes durable franchises look perpetually "expensive."

## Related

- [[book-value]]
- [[price-to-book-ratio]]
- [[balance-sheet]]
- [[return-on-equity]]
- [[net-current-asset-value]]
- [[fundamental-analysis]]
- [[intangible-assets]] — the items stripped out to get to tangible book value
- [[goodwill]] — the acquisition premium removed first

## Sources

- Graham, Benjamin & Dodd, David. *Security Analysis* — book value, tangible assets, and margin of safety.
- CFA Institute, *Equity Valuation* curriculum — book-value multiples and their use in financials.
- Damodaran, Aswath. "Valuing Financial Service Firms," NYU Stern (pages.stern.nyu.edu/~adamodar) — P/B, P/TBV, and ROE-based valuation of banks.
