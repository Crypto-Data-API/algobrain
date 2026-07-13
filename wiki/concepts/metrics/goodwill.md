---
title: "Goodwill"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [fundamental-analysis, valuation, education, stocks]
domain: [fundamental-analysis, valuation]
difficulty: beginner
aliases: ["Goodwill", "Acquired Goodwill", "Purchased Goodwill"]
prerequisites: ["[[balance-sheet]]"]
related: ["[[balance-sheet]]", "[[financial-statement-analysis]]", "[[tangible-book-value]]", "[[price-to-book-ratio]]", "[[intangible-assets]]", "[[asset-impairment]]", "[[return-on-assets]]", "[[return-on-equity]]", "[[enterprise-value]]", "[[net-income]]", "[[ifrs-vs-gaap]]"]
---

**Goodwill** is an intangible asset that appears on a company's [[balance-sheet]] only after it **acquires another business** for more than the fair value of that business's identifiable net assets. It captures the premium a buyer pays for things that cannot be individually itemised — brand reputation, customer relationships, assembled workforce, synergies, and market position. Goodwill is not the same as a company's own internally built brand value, which accounting rules generally do **not** let firms record on their own balance sheet.

## How goodwill arises

Goodwill is a residual computed in the acquisition (purchase) accounting of a [[balance-sheet|business combination]]:

```
Goodwill = Purchase Price
         − Fair Value of Identifiable Assets Acquired
         + Fair Value of Liabilities Assumed
```

Equivalently, goodwill is the purchase price minus the fair value of the acquired company's *net identifiable assets* (tangible assets plus separately identifiable intangibles such as patents and trademarks, less liabilities). Because it only exists as a by-product of an acquisition, a company that has never made an acquisition will report **zero goodwill**.

## Where it sits

Goodwill is a **non-current intangible asset** on the [[balance-sheet]]. It increases total assets and is balanced by the equity/cash/debt used to fund the deal. Because it is an accounting residual rather than a saleable asset, analysts often strip it out — see [[tangible-book-value]] (equity minus goodwill and other intangibles).

## Amortization vs. impairment

The accounting treatment changed materially over time and differs by regime:

- **No routine amortization** for public companies under current US GAAP and IFRS. Goodwill is **not** expensed gradually over a fixed life the way [[depreciation]] writes down PP&E.
- Instead, goodwill is tested for **[[asset-impairment|impairment]]** — at least annually, or whenever events suggest the acquired business is worth less than its carrying value. If impaired, the company books a one-time, **non-cash impairment charge** that reduces net income and writes the goodwill down.

An impairment is effectively the accountant's admission that the company **overpaid** for an acquisition. Large goodwill write-downs are common after the top of merger cycles.

## How it is used in analysis

- **Acquisition appetite and overpayment risk.** A balance sheet that is mostly goodwill signals a company built by acquisition (a "serial acquirer") rather than organic growth — and carries the risk of future write-downs if those deals underperform.
- **Return distortion.** Goodwill inflates total assets and equity, which *depresses* [[return-on-assets]] and [[return-on-equity]] — sometimes hiding a genuinely strong operating business behind an expensive acquisition. Some analysts compute returns on *tangible* capital to neutralise this.
- **Book-value quality.** A [[price-to-book-ratio]] looks cheaper than it is if much of that book value is goodwill. [[tangible-book-value]] removes it for a more conservative floor.
- **Impairment as a signal.** A write-down is backward-looking (the cash already left in the original deal) but flags poor capital allocation by management — relevant to [[financial-statement-analysis]].
- **Enterprise value is unaffected.** [[enterprise-value]] is built from market value and net debt, so it does not double-count goodwill; this is one reason EV-based multiples are preferred when comparing acquisitive firms.

## Negative goodwill (bargain purchase)

Occasionally a buyer pays *less* than the fair value of net identifiable assets — a **bargain purchase**. Under current standards the resulting "negative goodwill" is recognised as a one-time **gain** in the income statement after the acquirer re-checks its valuations, rather than being parked on the balance sheet.

## Limitations

- **Not a market value.** Goodwill is frozen at the deal date (historical cost less impairments); it does not rise when an acquisition turns out brilliantly.
- **Subjective impairment.** Impairment timing relies on management estimates of future cash flows, so write-downs can be delayed beyond when the economics have clearly deteriorated.
- **Non-cash, but not meaningless.** An impairment charge moves no cash in the period, but it reflects cash that *was* overspent in the original acquisition.
- **Regime differences.** Details of testing and recognition differ under [[ifrs-vs-gaap|IFRS vs. US GAAP]], reducing cross-border comparability.

## Worked example (hypothetical)

Suppose **Acme Co.** (hypothetical) acquires **Beta Inc.** (hypothetical) for **$500**. An independent valuation finds Beta's identifiable assets are worth **$400** and it carries **$120** of liabilities, so its fair value of net identifiable assets is **$280**.

```
Goodwill = $500 purchase price − $280 net identifiable assets = $220
```

Acme adds **$220** of goodwill to its [[balance-sheet]]. Two years later, Beta's business underperforms and Acme determines the unit is now worth only **$180** of the original premium. It books a **$40 non-cash impairment charge**, cutting that period's [[net-income]] by $40 and writing goodwill down from $220 to $180. No cash moves in the impairment year — the cash already left when Acme paid $500 up front.

## Related

- [[balance-sheet]] — where goodwill is reported as a non-current intangible
- [[tangible-book-value]] — equity with goodwill and intangibles removed
- [[price-to-book-ratio]] — distorted upward by large goodwill balances
- [[asset-impairment]] — the mechanism that writes goodwill down
- [[return-on-assets]] · [[return-on-equity]] — depressed by goodwill on the books
- [[enterprise-value]] — valuation lens unaffected by goodwill
- [[financial-statement-analysis]] — where acquisition quality is scrutinised

## Sources

- IFRS 3, *Business Combinations*; IAS 36, *Impairment of Assets*
- US GAAP ASC 805, *Business Combinations*; ASC 350, *Intangibles — Goodwill and Other*
- Stephen Penman, *Financial Statement Analysis and Security Valuation*
