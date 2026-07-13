---
title: "NFT Lending"
type: concept
created: 2026-04-22
updated: 2026-04-22
status: good
tags: [crypto, nft, defi, risk-management, liquidity]
aliases: ["NFT-Backed Loans", "NFT Collateralized Lending", "NFT Perpetual Lending"]
related: ["[[nft]]", "[[nft-trading]]", "[[nft-floor-price]]", "[[nftfi]]", "[[blend]]", "[[benddao]]", "[[blur]]", "[[ethereum]]"]
domain: [risk-management, defi, liquidity]
prerequisites: ["[[nft]]", "[[nft-floor-price]]", "[[liquidity]]"]
difficulty: advanced
---

NFT lending protocols let holders use their NFTs as collateral to borrow fungible tokens (typically ETH, WETH, USDC, or DAI) without selling the NFT. The borrower retains upside exposure and sentimental ownership while unlocking stablecoin or ETH liquidity; the lender earns yield on idle capital in exchange for accepting the hard-to-liquidate collateral risk of a non-fungible asset. The category splits into three architectures — peer-to-peer, peer-to-pool, and perpetual — each with different liquidation mechanics, capital efficiency, and tail-risk profiles.

## Why It Exists

The core problem NFT lending solves: NFTs are large, indivisible, and illiquid. A holder of a single BAYC worth 30 ETH cannot access that capital for other trades without selling the NFT and potentially triggering a tax event, losing rarity-specific upside, losing airdrop and IP rights, and rebuying at a higher price later. Lending provides liquidity without the sale.

On the lender side, large ETH and stablecoin holders seek yield beyond DeFi base rates. NFT-collateralized loans at 10-30% APR are attractive when volatility premia are high and when lenders can selectively underwrite high-quality collections.

## Peer-to-Peer Lending

Peer-to-peer (P2P) protocols match individual lenders with individual borrowers for fixed-term loans on specific NFTs.

### Architecture
- The borrower deposits an NFT into an escrow contract and publishes a loan request (principal amount, duration, max APR).
- A lender accepts the request on-chain, transferring the principal to the borrower.
- The NFT is locked in escrow for the term (commonly 7, 14, 30, 90 days).
- At expiry, the borrower repays principal + interest. If they fail to repay, the NFT transfers to the lender.
- No forced liquidation during the loan — the lender cannot seize the NFT even if floor price collapses 50%.

### [[nftfi]]
NFTfi launched in 2020 and is the canonical P2P protocol. Key features:
- Borrower pays no platform fee; lender pays a small fee on interest earned.
- Loans are fully negotiated — lenders underwrite each NFT individually (specific token ID, not just the collection).
- Supported collateral includes BAYC, CryptoPunks, Art Blocks, Azuki, and many other established collections.
- Borrow on ETH, WETH, DAI, or USDC.

### Counterparty Risk Profile
- **Borrower-side**: No liquidation risk during the loan. The collateral cannot be seized mid-term even if floor crashes. The only risk is that the borrower fails to repay and loses the NFT at expiry.
- **Lender-side**: Carries the full duration risk. If the floor price drops below the loan amount during the term, the lender is underwater with no recourse. At expiry, either the borrower repays (lender collects interest) or the lender takes possession of a possibly-devalued NFT.
- **Lender must mark to fair value the NFT they might receive**, which is hard because floor prices are manipulable (see [[nft-floor-price]]) and particular token IDs trade at varying premia.

### Pricing
LTVs on NFTfi historically range 20-60% of floor. APRs range from 10% for blue chips (BAYC, CryptoPunks) up to 60-100% for riskier collections. Shorter durations command lower rates because the lender's floor-price risk is shorter.

## Peer-to-Pool Lending

Peer-to-pool (P2Pool) protocols replace individual lender underwriting with a capital pool that lends against any NFT in a supported collection, using the floor price as an oracle.

### Architecture
- Lenders deposit ETH or stablecoins into a pool.
- Borrowers deposit an NFT from a supported collection and can immediately borrow up to a fixed LTV (e.g., 40% of collection floor).
- Interest is variable, set by a utilization-based curve.
- If floor price drops below a liquidation threshold (e.g., health factor < 1), the NFT is put up for forced auction.
- Proceeds repay the pool; any surplus goes to the borrower.

### [[benddao]]
BendDAO pioneered the P2Pool model for NFTs in 2022. Key features:
- Supported collections limited to top-tier (BAYC, MAYC, CryptoPunks, Doodles, Azuki).
- LTV around 40% at loan origination.
- Liquidation threshold around 90% (if debt reaches 90% of floor, the loan enters 48-hour auction).
- Auction started at the current floor price as the opening bid.

### Auction Mechanics and the Key Vulnerability
The critical design choice: BendDAO auctions opened at the current floor. In a stable market, this works — bidders have incentive to compete below floor for a discount. In a falling market, it breaks catastrophically because no rational bidder will bid at the floor when they expect the floor to fall further during the 48-hour window. The auction simply gets zero bids.

### [[benddao]] August 2022 Crisis
In August 2022, the BAYC floor dropped from ~90 ETH to ~60 ETH over a few weeks. Several large BendDAO loans moved to auction simultaneously. The mechanics broke as designed:
- Auctions opened at the floor (60 ETH).
- No bidders entered because the expected floor in 48 hours was lower.
- Loans failed to liquidate and accumulated as protocol bad debt.
- The pool's available ETH was depleted as remaining depositors raced to withdraw.
- Withdrawal queues formed; the protocol was within hours of insolvency.

The emergency response:
- Liquidation threshold lowered from 95% to 80% in stages, forcing earlier intervention.
- Auction floor price changed from "collection floor" to a 48-hour-Twap-based value.
- Interest rates raised to discourage further borrowing and encourage repayment.
- Emergency governance vote passed within days to inject capital and restructure parameters.

The case is the canonical lesson in oracle-and-liquidation design for illiquid collateral. Detailed in [[nft-floor-price]].

## Perpetual Lending

Perpetual NFT loans have no fixed expiry. Positions remain open indefinitely until the borrower repays or another lender refinances at a different rate.

### [[blend]] (Blur Lending)
Blur launched Blend in May 2023. The protocol was designed by Paradigm researchers (Dan Robinson, transmissions11, and others) and implemented by Blur Core Contributors (Source: Paradigm announcement, May 1, 2023). Key features:
- **No fixed term and no oracle dependency.** The loan runs as long as some lender is willing to hold the debt.
- **Off-chain offers**: Lenders post signed offers specifying loan amount, interest rate, and eligible collections. Borrowers browse and select compatible offers.
- **Refinance (Dutch) auctions**: When the current lender wants to exit, a Dutch auction opens in interest-rate space — starting at 0% and steadily rising until a new lender accepts the position at that rate. The new lender pays the full repayment amount to the old lender and takes over the loan.
- **Continuous interest**: Interest accumulates continuously; the repayment amount is calculated on the fly.
- **Liquidation**: If the refinance auction reaches the maximum rate (1000% APR in the original design) without finding a lender, the position liquidates and the current lender takes the collateral.

### Strategic Implications
- **Borrowers** get the UX of an indefinite loan: as long as some lender is willing to hold the debt, the position persists.
- **Lenders** have exit optionality: they can trigger an auction to hand off the loan rather than being stuck.
- **Leveraged NFT buying**: Blend was explicitly designed to enable 5-10x leverage on NFT purchases. A buyer can put down 10-20% of the NFT price, borrow the rest against the same NFT, and take possession. This pulled significant leveraged demand into Blur-listed collections and drove blue-chip floors upward in mid-2023.
- **Liquidation risk**: A borrower who can't match a rising rate loses the NFT via refinance-auction failure. In practice, during falling markets, rates spike and borrowers must either repay or surrender collateral.

## Key Risks Across All Architectures

- **Collateral illiquidity during crashes**: The floor that exists in calm markets disappears in crashes. Oracle price and true exit price decouple. Liquidation auctions receive zero bids.
- **Oracle manipulation**: Attackers can push a collection's floor price down via a handful of low-cost wash listings or large sweeps, triggering liquidations on real loans. P2Pool protocols that use the raw floor are most vulnerable; TWAP and multi-source oracles help but slow down legitimate price discovery.
- **Forced-sale cascades**: Simultaneous liquidations of multiple loans in the same collection push the floor lower, triggering further liquidations. Classic DeFi liquidation spiral, amplified by NFT illiquidity.
- **Trait valuation error**: Floor-based LTV ignores that an individual NFT might be far more or less valuable than the collection floor. Lenders accepting rare tokens at floor-based LTV may leave value on the table; lenders accepting floor-rank tokens at floor-based LTV may be over-collateralized on paper but under-collateralized in practice.
- **Counterparty risk in P2P**: Some P2P protocols require the lender to actively claim the NFT if the borrower defaults, with a time window. Missing the window can result in the loan rolling or worse.
- **Smart contract risk**: NFT lending protocols are complex and have been targets of exploits. Ensure protocol audits, treasury size, and bug bounty history are consistent with the position size.
- **Royalty interaction**: If the lender takes possession of the NFT and sells, they may owe royalties (depending on venue, see [[nft-royalty-enforcement]]) — relevant for lender economics on default.

## How Traders Use NFT Lending

- **Unlock liquidity without selling grails**: A holder of a rare BAYC with significant personal or IP value borrows against it to fund other trades, avoiding a tax-triggering sale and preserving optionality.
- **Leveraged long**: Borrow on an existing NFT, buy another NFT with the proceeds, potentially borrow again. [[blend]] makes this a first-class workflow. Each loop amplifies both upside and downside by the LTV ratio.
- **Carry trades**: Borrow at low rates against a blue chip, deploy the capital into higher-yielding DeFi strategies (stablecoin farming, perp funding). Viable when NFT borrow rates are below DeFi yields, but the mark-to-market risk on the NFT collateral can erase the spread.
- **Short the floor indirectly**: Lenders on P2Pool protocols are effectively short gamma on the floor — in a crash they end up owning the NFT at the liquidation price. Not a pure short, but a way to get paid to wait for a drawdown.
- **Liquidation sniping**: When a P2Pool protocol auctions liquidated NFTs, bidders can sometimes buy below true floor if auction mechanics are broken or auctions are undersubscribed. Risky — this is exactly the mechanism that failed at BendDAO in 2022.
- **Cash management without selling**: Tax-efficient liquidity access for creators, long-term holders, and institutional custodians who don't want a realized disposal.

## Related

- [[nft]]
- [[nft-trading]]
- [[nft-floor-price]]
- [[nft-aggregators]]
- [[nft-royalty-enforcement]]
- [[nftfi]]
- [[blend]]
- [[benddao]]
- [[blur]]
- [[opensea]]
- [[ethereum]]
- [[risk-management]]
- [[liquidity]]
- [[market-microstructure]]

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]])
- Paradigm, "Introducing Blend" (May 1, 2023): https://www.paradigm.xyz/2023/05/blend (Blend mechanics, Dutch auction, 1000% max rate)
