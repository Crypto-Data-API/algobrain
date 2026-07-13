---
title: Short Interest
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [short-selling, market-microstructure, sentiment-indicator, liquidity]
aliases: [SI, short interest ratio, days to cover, Short Interest]
domain: [market-microstructure]
prerequisites: ["[[short-selling]]", "[[float]]"]
difficulty: intermediate
related:
  - "[[short-squeeze]]"
  - "[[short-covering]]"
  - "[[short-position]]"
  - "[[float]]"
  - "[[short-interest-anomaly]]"
  - "[[regulation-sho]]"
---

# Short Interest

Short interest is the total number of shares of a stock that have been sold short and not yet covered. It is most useful when normalized — expressed as a percentage of the [[float]] (short interest % of float) or as "days to cover" (short interest divided by average daily volume) — and is widely watched as a [[sentiment]] and squeeze-risk indicator.

## Key Metrics

- **Short interest % of float** — the percentage of freely tradeable shares currently sold short. Above ~20% is considered high; above 30-40% flags meaningful [[short-squeeze]] risk. Values above 100% (as seen in GME in early 2021) indicate shares lent and re-shorted multiple times.
- **Days to cover (short interest ratio)** — `short interest ÷ average daily trading volume`. It estimates how many days of normal volume it would take all shorts to cover. Higher numbers mean covering demand is large relative to liquidity, amplifying squeeze potential.
- **Utilization rate** — the percentage of available lendable supply currently on loan. Above ~90% utilization, borrow costs and recall risk jump; this is a leading indicator that reported short interest understates.
- **Borrow fee** — the annualized cost to borrow the shares; a rising fee signals demand to short exceeding lendable supply.

## Where to Find It

US short interest is reported by FINRA/exchanges twice monthly (mid-month and end-of-month settlement dates), published with a delay of roughly 8-10 business days. Because the official figures are stale and biweekly, traders supplement them with real-time estimates from securities-lending data vendors such as Ortex and S3 Partners, which model utilization, borrow fees, and intraday short flow.

## Trading Relevance

High short interest is a double-edged indicator:

- **Bearish signal** — many sophisticated participants are positioned against the stock, often on fundamental or accounting concerns.
- **Squeeze fuel** — every shorted share is latent buy-to-cover demand. A rally can force [[short-covering]], which accelerates the move upward into a [[short-squeeze]].
- **Contrarian / capitulation signal** — extreme short interest can mark peak pessimism, setting up a reversal.

Academically, high short interest is one of the more robust cross-sectional return predictors: heavily shorted stocks tend to *underperform* on average, an effect documented as the [[short-interest-anomaly]]. The squeeze cases are the dramatic exceptions, not the base rate.

## Limitations

Short interest data is delayed and biweekly, so it lags real-time positioning. Synthetic shorts expressed through [[options]], swaps, or [[futures]] are not captured in reported share short interest. High short interest alone is not a buy signal — many heavily shorted stocks keep declining for good reason. Combine it with utilization, borrow-fee trend, and a catalyst before treating it as actionable.

## Sources

- FINRA, "Short Interest" reporting rules and Equity Short Interest data (official biweekly dataset)
- SEC, *Regulation SHO* — short-sale and reporting framework; Rule 13f-2 (2023) added monthly institutional short-position disclosure
- Asquith, Pathak & Ritter (2005), "Short Interest, Institutional Ownership, and Stock Returns," *Journal of Financial Economics*

## Related

- [[short-squeeze]] — what high short interest can fuel
- [[short-covering]] — the buy-to-cover demand short interest represents
- [[float]] — the denominator for short interest %
- [[short-interest-anomaly]] — the documented underperformance of heavily shorted stocks
- [[short-position]] — the underlying positions being aggregated
