---
title: "Net Current Asset Value (NCAV)"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [fundamental-analysis, valuation, value-investing, anomalies, education]
aliases: ["NCAV", "Net-Net", "Net Net", "Net-Net Working Capital", "NNWC", "Graham Net-Net"]
domain: [fundamental-analysis, valuation]
prerequisites: ["[[book-value]]", "[[value-investing]]"]
difficulty: intermediate
related: ["[[value-investing]]", "[[value-investing-strategy]]", "[[benjamin-graham]]", "[[book-value]]", "[[margin-of-safety]]", "[[fundamental-analysis]]", "[[anomalies-overview]]", "[[deep-value]]"]
---

**Net Current Asset Value (NCAV)** is a deep-value balance-sheet metric devised by [[benjamin-graham|Benjamin Graham]] that estimates a company's liquidation floor using only its current assets net of *all* liabilities. A stock trading below two-thirds of its NCAV per share — a "**net-net**" — is, in Graham's framework, priced below the conservative value of its liquid assets alone, giving the buyer assets like inventory, receivables, and cash essentially for free while ignoring the business, real estate, and goodwill entirely.

## Formula

The core NCAV calculation deliberately excludes long-term assets (property, intangibles, goodwill) because they are illiquid and uncertain in a wind-down:

```
NCAV = Current Assets − Total Liabilities
NCAV per share = (Current Assets − Total Liabilities) / Shares Outstanding
```

Note that **Total Liabilities** — not just current liabilities — is subtracted (including long-term debt and preferred stock). This is what makes NCAV more conservative than ordinary working capital.

### The net-net buy rule

Graham's classic screen: buy when

```
Price per share < (2/3) × NCAV per share
```

The one-third haircut is an explicit [[margin-of-safety]] against the fact that current assets rarely fetch full book value in a liquidation.

### Net-Net Working Capital (NNWC) — a stricter variant

A more conservative refinement haircuts the current assets by expected recovery rates:

```
NNWC = Cash + 0.75 × Receivables + 0.50 × Inventory − Total Liabilities
```

Cash is counted at 100%, receivables at ~75% (some won't be collected), and inventory at ~50% (fire-sale discount). NNWC is what serious deep-value practitioners use; raw NCAV overstates liquidation value.

## Why the anomaly exists

Net-net investing is one of the most-studied [[anomalies-overview|market anomalies]]. The mechanism is structural and behavioral:

- **Distress and small size.** Net-nets are almost always tiny, ugly, money-losing, or out-of-favor companies. Institutions cannot or will not own them (liquidity, mandate, headline risk), so they are systematically underpriced.
- **Aversion to "cigar butts."** Most investors refuse to buy businesses that look like they are dying, even when the balance sheet alone covers the price — a behavioral aversion that creates the discount.
- **Mean reversion / acquisition.** Many net-nets either recover, get acquired, or return cash. The basket wins on average even though individual names fail.

Studies (Oppenheimer 1986; later replications by Montier, Carlisle, and others) found net-net baskets returned roughly 25–35% annually over long stretches, far above the market — though with high single-name failure rates and concentration in micro-caps.

## Trading relevance

- **Screening, not single-stock conviction.** NCAV is a *basket* strategy. Buy 20–30 net-nets, hold ~1–2 years, rebalance. Individual net-nets go to zero; the diversified basket captures the premium.
- **Capacity is tiny.** The strategy lives in micro- and nano-cap stocks; it does not scale and is one of the few edges genuinely reserved for small accounts (see [[deep-value]]).
- **Filters matter.** Practitioners exclude Chinese reverse-mergers and fraud-prone names, require positive (or improving) NNWC, avoid heavy cash-burn, and prefer insider buying or low debt.
- **Regime sensitivity.** Net-nets appear in droves at market bottoms (2009, 2020 micro-cap lows) and nearly vanish in euphoric markets — their scarcity is itself a rough valuation thermometer.
- **Relationship to other metrics.** NCAV is the most conservative member of the value family; it sits below [[book-value]]-based screens, which sit below earnings-based screens like [[value-investing|P/E and P/B]].

## Limitations

- **Liquidation rarely happens.** The "floor" is theoretical; a value trap can erode current assets through ongoing losses before any recovery.
- **Stale balance sheets.** Reported current assets may be months old and already impaired.
- **Off-balance-sheet liabilities** (leases, pensions, litigation) can make true liabilities larger than reported.
- **Survivorship and cherry-picking** inflate some backtests; net failure rates are high.

## Related

- [[benjamin-graham]] — originator of NCAV and net-net investing
- [[value-investing]] — the parent discipline
- [[value-investing-strategy]] — implementation playbook
- [[book-value]] — the next-least-conservative balance-sheet metric
- [[margin-of-safety]] — the principle the two-thirds rule encodes
- [[deep-value]] — the small-cap edge family NCAV belongs to
- [[anomalies-overview]] — net-nets as a documented anomaly

## Sources

- Benjamin Graham & David Dodd, *Security Analysis* (1934) and Graham, *The Intelligent Investor*
- Henry Oppenheimer, "Ben Graham's Net Current Asset Values: A Performance Update," *Financial Analysts Journal* (1986)
- Tobias Carlisle, *Deep Value* (2014)
- James Montier, "Graham's Net-Nets: Outdated or Outstanding?" (SG Global Strategy, 2008)
