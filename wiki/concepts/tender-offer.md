---
title: "Tender Offer"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [event-driven, market-microstructure, fundamental-analysis, stocks]
aliases: ["Tender Offer", "Tender Offers", "Self-Tender", "Issuer Tender Offer", "Cash Tender Offer", "Exchange Offer"]
domain: [market-microstructure, fundamental-analysis]
prerequisites: ["[[stocks]]", "[[share-buybacks]]"]
difficulty: intermediate
related: ["[[merger-arbitrage]]", "[[tender-offer-arbitrage]]", "[[mergers-and-acquisitions]]", "[[share-buybacks]]", "[[special-situations]]", "[[appraisal-rights-arbitrage]]", "[[delisting]]", "[[dutch-auction-tender-arbitrage]]"]
---

A **tender offer** is a public, structured offer to buy a large block of a company's shares directly from existing shareholders, usually at a **premium** to the prevailing market price and open for a fixed window (commonly 20+ business days in the US). It bypasses the open market: instead of accumulating stock tick by tick, the bidder invites every holder to "tender" their shares at a stated price. There are two main flavours — a **third-party tender offer**, where an outside acquirer bids to take control of the company, and an **issuer (self) tender offer**, where the company buys back its own shares (see [[share-buybacks]]).

## Why companies and acquirers do it

- **Acquire control quickly.** A third-party bidder can take a controlling stake faster than negotiating a full [[mergers-and-acquisitions|merger]], and can sometimes go directly to shareholders **over the board's objections** (a hostile bid). A friendly tender offer is often the first step of a two-step acquisition.
- **Buy back stock efficiently.** An issuer self-tender retires a large slug of shares at once, often via a **Dutch auction** (the company names a price range and buys at the lowest price that fills the desired volume — see [[dutch-auction-tender-arbitrage]]).
- **Signal confidence or return capital.** A self-tender at a premium signals management thinks the stock is cheap and concentrates ownership for remaining holders.

## What it means for you as a shareholder

You are not forced to do anything — you **choose** whether to tender. Key mechanics:

- **The premium.** The offer is typically above market (deal premiums of 20-40% are common in control bids), which is why the share price usually jumps toward — but stays slightly below — the offer price after announcement. That gap is the **deal spread** the market demands for the risk the offer fails (see [[merger-arbitrage]]).
- **Conditions.** Offers usually carry a **minimum tender condition** (e.g., the bidder only buys if enough shares are tendered to reach a threshold like a majority or 90%), plus financing and regulatory/antitrust conditions. If conditions aren't met, the bid can lapse and the price falls back.
- **Pro-ration.** If the bidder wants only a portion of shares and the offer is **oversubscribed**, tenders are accepted pro-rata. You might tender 1,000 shares but only have 600 bought, leaving 400 at the post-offer market price.
- **Squeeze-out / second-step merger.** If a control bidder crosses a high threshold (often 90% in many jurisdictions), it can force out the remaining holders in a **back-end merger** at the same price — so holding out rarely gets you more, and may leave you in an illiquid stub or trigger [[appraisal-rights-arbitrage|appraisal rights]].
- **Tax.** A **cash** tender is generally a taxable disposal (capital gain or loss); an **exchange offer** paid in the bidder's stock may be partly tax-deferred. Check your own jurisdiction.

## Hypothetical example

*Illustrative only.* Suppose ACME trades at $40 and BidCo announces a cash tender offer at **$52 per share** (a 30% premium), conditioned on at least 50% of shares being tendered. ACME jumps to ~$50.50 — close to but under $52, pricing in a small chance the deal breaks. You own 1,000 shares (cost basis $30). If you tender and the offer closes, you receive **$52,000** and realise a $22,000 capital gain. If you do nothing and BidCo reaches 90%, it can squeeze you out at $52 anyway via a back-end merger. If the financing condition fails and BidCo walks, ACME likely falls back toward $40 and you keep your shares.

## What to watch for

- **Premium vs. intrinsic value** — a premium to *market* is not the same as a premium to *fair value*; lowball self-tenders during a slump can be opportunistic.
- **Conditions and deal-break risk** — read the minimum-tender, financing, and regulatory conditions; the wider the spread, the more risk the market sees.
- **Withdrawal rights** — you can usually withdraw tendered shares while the offer is open if a higher competing bid emerges.
- **Pro-ration math** — in partial and Dutch-auction offers, model how much will actually be bought.
- **Cash vs. exchange** — cash is a taxable event now; stock defers tax but hands you exposure to the acquirer.
- **The stub** — after a successful control bid, any remaining listed shares can become illiquid and face [[delisting]].

## Related

- [[merger-arbitrage]] — trading the deal spread once an offer is live
- [[tender-offer-arbitrage]] — the dedicated arbitrage strategy page
- [[dutch-auction-tender-arbitrage]] — exploiting issuer Dutch-auction self-tenders
- [[mergers-and-acquisitions]] — the broader takeover picture from a shareholder's view
- [[share-buybacks]] — issuer self-tenders are one buyback mechanism
- [[special-situations]] — the event-driven bucket tender offers belong to
- [[appraisal-rights-arbitrage]] — recourse for squeezed-out minority holders
- [[delisting]] — the common endgame after a successful control bid

## Sources

- U.S. SEC, "Tender Offers" (Williams Act / Regulation 14D-14E) — disclosure rules, 20-business-day minimum, withdrawal and pro-ration rights.
- General corporate-finance knowledge on two-step acquisitions, minimum-tender conditions, and squeeze-out thresholds; no additional specific wiki source ingested yet.
