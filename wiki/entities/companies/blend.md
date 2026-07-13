---
title: "Blend"
type: entity
entity_type: protocol
created: 2026-04-22
updated: 2026-06-19
status: excellent
tags: [crypto, nft, defi, ethereum, leverage, derivatives, liquidity]
aliases: ["Blur Lending", "Blend Protocol", "Blur Blend"]
related: ["[[blur]]", "[[nftfi]]", "[[benddao]]", "[[nft]]", "[[nft-trading]]", "[[ethereum]]", "[[bored-ape-yacht-club]]", "[[cryptopunks]]", "[[azuki]]"]
---

> **Disambiguation.** This page is **Blend (Blur Lending)** — the peer-to-peer perpetual NFT lending *protocol* on [[ethereum|Ethereum]]. It is NOT "Blend Labs, Inc." (NASDAQ: BLND), the mortgage/banking software company. If you are looking for the public fintech equity, that company does not yet have a page in this wiki — see the note in [[#Related]].

Blend (Blur Lending) is a peer-to-peer perpetual NFT lending protocol launched in May 2023 by Blur core contributors and published by Paradigm (authored by Dan Robinson, transmissions11, Galaga, Toad, and Pacman). It enables NFT-collateralized borrowing with no fixed expiry and no on-chain price oracle, as well as leveraged NFT purchases with a buy-now-pay-later (BNPL) flow. Within months of launch, Blend became a dominant NFT lending venue on Ethereum by volume, reshaping the competitive landscape that previously belonged to [[nftfi]] and [[benddao]].

## How it works

Blend's design centers on three ideas: no expirations, no oracles, and auction-driven refinancing.

### Perpetual loans

A borrower and a lender match off-chain on terms (principal, APR, collateral NFT). Once matched, the loan has **no maturity date**. Interest accrues continuously. Either side can exit via the refinance-auction mechanism described below.

### Refinance auctions

Because loans are perpetual, either party triggers price discovery by calling for a refinance auction:

- If the **lender** wants out (e.g., they want their capital back), they start a Dutch auction in **interest-rate space**. The auction rate starts at 0% and climbs; new lenders can step in at any rate they are willing to offer, taking over the loan at that rate. If the auction reaches a maximum rate threshold without a replacement lender accepting, the borrower is given a short window to repay; failing that, the original lender seizes the NFT (liquidation).
- If the **borrower** wants to exit, they can simply repay the principal plus accrued interest at any time, with no penalty.
- If the **borrower** wants to lower their rate, they can also kick off an auction seeking better terms from new lenders.

This auction is the mechanism that replaces both fixed expiries and oracles: price discovery is triggered by one side's action rather than by a scheduled event or external price feed.

### BNPL (buy-now-pay-later) purchasing

Blend also powers leveraged NFT buying inside [[blur]]: a user selects "Buy Now Pay Later," puts up a fraction of the NFT's price as down payment, and Blend matches them with a lender who funds the balance. The NFT goes to the buyer, who now holds a perpetual Blend loan against it. This created the most common entry point for retail leveraged NFT exposure on Ethereum.

## Fees and structure

- **Protocol fee**: zero at launch. Blend was explicitly designed fee-free to grow share; [[blur]] retained the option to activate fees later via governance.
- **No oracle**: pricing is implicit in the auction mechanism; Blend does not rely on floor-price oracles that could be manipulated.
- **BLUR token**: [[blur]]'s governance token is used for fee-switch / governance decisions over Blend; it does not sit in the trade path.

## Design comparison / competitive positioning

Blend is one of two dominant NFT-lending design archetypes. The competitive axis is **fixed-term, oracle-light P2P (NFTfi) versus pooled, oracle-based lending (BendDAO) versus Blend's perpetual, oracle-free, auction-refinanced model**.

| Protocol | Model | Pricing / liquidation | Notes |
|---|---|---|---|
| **Blend (Blur Lending)** | Peer-to-peer, perpetual loans | No oracle; Dutch auctions in rate-space trigger refinance/liquidation | Buy-now-pay-later flow inside [[blur]]; fee-free at launch |
| [[nftfi]] | Peer-to-peer, fixed-term loans | Negotiated terms; fixed expiry; no oracle | Older, more conservative P2P design |
| [[benddao]] | Peer-to-pool lending | Oracle-based floor price; auction liquidation on health-factor breach | Pooled liquidity; contrasted with Blend as the other dominant archetype |
| Arcade / Gondi | Peer-to-peer term lending | Negotiated; supports higher-value / 1-of-1 NFTs | Niche, higher-value collateral focus |

Blend's edge was distribution: it launched directly inside the [[blur]] marketplace front-end with BLUR incentives, instantly routing the marketplace's trading volume into leverage. Its weakness is exactly that coupling — liquidity rises and falls with [[blur]] usage and incentive programs.

## What traders use it for

- **Leveraged entry into blue chips** — BNPL buyers taking 2-5x-style exposure to BAYC, CryptoPunks, Azuki, Pudgy Penguins, Milady, etc.
- **Cash-out loans** — NFT holders mint perpetual ETH loans against their collateral without selling.
- **Capital-efficient market making** — NFT whales lend against floors they would be comfortable seizing, collecting yield and occasionally acquiring NFTs at attractive basis.
- **Carry trades** — borrow ETH against a stable-floor collection, deploy the ETH elsewhere (DeFi, further NFT positions), target a spread over the loan APR.

## Trader's playbook

- **As a borrower:** monitor for lender-initiated refinance auctions — "perpetual" does not mean "uncallable." Keep ETH ready to repay within the short repay-or-liquidate window during sharp floor drawdowns.
- **As a lender:** the yield is compensation for being short an option on the floor — you can be forced to seize an NFT at a now-underwater basis. Lend only against floors you would genuinely be content to own.
- **As a floor trader:** Blend's mechanics are a *reflexivity signal*. Heavy BNPL borrowing on the way up adds synthetic demand; clusters of refinance auctions on the way down telegraph forced selling. Watching outstanding Blend loan volume and auction activity per collection can front-run liquidation cascades.
- **Venue/incentive watch:** because Blend liquidity tracks [[blur]] incentives, changes to BLUR reward programs are a leading indicator for outstanding loan volume and, by extension, leverage in the NFT market.

## Risks and limitations

- **Cascading refinance auctions in drawdowns** — when the floor falls sharply, lenders simultaneously trigger auctions, and if no counterparty bids, borrowers face 24-hour repay-or-liquidate windows. Multiple waves of Blend borrower liquidations have occurred during sharp BAYC and Azuki drawdowns, accelerating the sell pressure on the underlying collection.
- **Reflexive price spirals** — aggressive BNPL borrowing pumps floors on the way up (synthetic demand) and crushes them on the way down (forced sales and seized collateral dumped back on the market). Blend is widely credited with both extending the mid-2023 NFT rally and sharpening its subsequent drawdown.
- **Perpetual structure mis-sold** — retail borrowers often treat "perpetual" as "cannot be called," but lenders can trigger refinance auctions at will, forcing the borrower to repay or take worse terms.
- **No oracle also means no safety net** — there is no automatic margin call based on floor price. Instead, auctions must be triggered manually, which can be late in a fast-moving drawdown.
- **Venue concentration** — Blend liquidity is tightly coupled to [[blur]] front-end usage and BLUR incentive programs. Changes in incentives have historically produced large swings in outstanding loan volume.
- **Smart-contract & illiquidity risk** — as with any DeFi protocol, contract risk applies; and NFT collateral can become effectively illiquid in a fast drawdown, leaving lenders holding hard-to-sell assets.

## Related

- [[blur]] — the marketplace that operates Blend
- [[nftfi]] — older fixed-term peer-to-peer NFT lender
- [[benddao]] — peer-to-pool NFT lender; often contrasted with Blend as the two dominant NFT-lending design archetypes
- [[nft-trading]], [[nft]]
- [[ethereum]]
- [[bored-ape-yacht-club]], [[cryptopunks]], [[azuki]]
- **Note:** the public mortgage/banking software company "Blend Labs, Inc." (NASDAQ: BLND) — peers ncino and rocket-companies — is a distinct entity and is not covered by this protocol page.

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
