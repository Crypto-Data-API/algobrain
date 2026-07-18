---
title: "DAI Black Thursday March 12, 2020"
type: news
created: 2026-04-28
updated: 2026-06-12
status: good
tags: [crypto, stablecoins, depeg, history, dai, makerdao, defi, liquidation]
aliases: ["MakerDAO Black Thursday", "DAI March 2020", "DAI $1.10 Above Peg", "Zero-Bid Auction"]
event_date: 2020-03-12
markets_affected: [crypto]
impact: high
verified: true
sources_count: 7
related: ["[[stablecoin-pair-arbitrage]]", "[[stablecoin-depeg-profit-capture]]", "[[depeg-risk]]", "[[makerdao]]", "[[dai]]", "[[liquidation-cascade-arbitrage]]", "[[2023-03-usdc-svb-depeg]]", "[[stablecoin-depeg-history]]"]
---

# DAI Black Thursday — March 12, 2020

On **March 12, 2020 ("Black Thursday")**, ETH crashed ~50% in 24 hours as COVID-19 panic hit global markets. The MakerDAO collateral system, which backed DAI with ETH-denominated vaults, suffered a cascade failure: liquidation auctions broke because **gas prices spiked so high that keeper bots couldn't compete**, leaving ETH collateral being auctioned at **$0 bids** (zero-bid auctions). Roughly **$8.32M of ETH (~35,000 ETH) was won for zero DAI**, leaving MakerDAO with ~$4-5.5M of unbacked DAI (bad debt) that was later covered by minting and auctioning MKR. In the aftermath, DAI traded **above peg at $1.10+** for weeks as borrowers scrambled to repay debt with insufficient DAI supply.

**This is the canonical "above-peg" depeg case** — the rare opposite of the more common discount depegs. The trade was to **short DAI** (borrow + sell at premium; cover at peg).

## Timeline

| Date / Time (UTC) | Event |
|------------------|-------|
| Mar 11, 2020 | ETH at $200; CDP-1.0 (single-collateral DAI / SAI) and CDP-2.0 (multi-collateral) operational |
| **Mar 12, 11:00** | ETH starts crashing on COVID-19 panic; -25% in early hours |
| Mar 12, 12:00-15:00 | ETH drops below $130; cascading vault liquidations triggered |
| Mar 12, 15:00 | Ethereum gas prices spike to 200-1000+ gwei |
| Mar 12, 18:00 | **Zero-bid auctions begin**: keeper bots unable to participate due to gas costs; auction winners taking ETH for $0 DAI |
| Mar 12, 22:00 | ETH bottoms at ~$88 (-55% intraday) |
| Mar 12-13, 22:00-04:00 | ~$8.32M of ETH (~35,000 ETH) won via zero-bid auctions; ~$4-5.5M of resulting unbacked DAI (bad debt) |
| Mar 13, 06:00 | MakerDAO governance emergency response; system pause considered but not enacted |
| Mar 14-15 | DAI trades $1.05-1.10 (ABOVE peg) as vault holders need DAI to repay debt + close vaults |
| Mar 19, 2020 | MakerDAO governance approves **emergency surplus auction** (mint MKR, auction for DAI) |
| Mar 26, 2020 | First MKR-for-DAI auction completes; recapitalizes ~$5M |
| April 2020 | DAI gradually returns to peg as vault stress unwinds |

## The Mechanism Failure

**MakerDAO's auction design assumed gas-priced-in keeper competition.** Under normal conditions:
- A vault becomes under-collateralized
- Anyone can call liquidate(), triggering an English auction
- Keeper bots bid up to the fair value of the collateral
- Auction settles; collateral is sold; DAI debt is paid down

**Black Thursday broke this** because:
- Gas prices hit 200-1000+ gwei (vs typical 20-50 gwei)
- Submitting an auction bid cost $50-200 in gas
- Most keeper bots had insufficient gas budgets to participate
- A single bot operator submitted bids of effectively $0 DAI for the collateral across many auctions
- Without competing bids, the $0 bid won
- Result: ~$8.32M of ETH (~35,000 ETH) won for $0; this is what produced the protocol's bad debt

## DAI Trading Above Peg

The aftermath created an unusual depeg direction:

1. Vault holders facing under-collateralization needed to **repay DAI debt** to avoid liquidation
2. DAI supply had been **shrunk** by the failed auctions (some DAI debt was zeroed out from liquidations)
3. Emergency MKR auctions created additional DAI demand (MKR holders bidding USD-equivalent DAI for newly-minted MKR)
4. **Demand for DAI > supply → DAI traded above peg**

DAI peaked at approximately **$1.10** (10% above peg) on March 13-14, 2020, and remained $1.03-1.07 throughout March-April 2020.

## Trade: Short DAI Above Peg

**The arb that worked**:

1. **Borrow DAI** — sources:
   - Compound (DAI lending market; APR spiked to 8%+ during stress but available)
   - Aave (V1 at the time)
   - Other DAI-margin lending venues
2. **Sell borrowed DAI** at $1.05-1.10 on Coinbase Pro / Curve / Uniswap
3. **Wait for peg restoration**
4. **Buy back DAI** at $1.00-1.02 once supply normalized
5. **Repay borrowed DAI**; capture the spread

**P&L worked example**:
- Borrow 1,000,000 DAI at 8% APR (~$110/day in interest)
- Sell at $1.07 = $1,070,000 USD proceeds
- Wait 3 weeks for peg restoration
- Cover at $1.02 = $1,020,000 cost
- Borrow interest: ~$2,300 over 3 weeks
- **Net P&L: $1,070,000 - $1,020,000 - $2,300 = $47,700 on borrowed-position**
- Equity required: ~$200K-300K margin on Compound/Aave for the borrow; effective return on equity ~16-24%

## Alternative Trade: Long ETH at Bottom + Short DAI

Combined trade: long ETH at the bottom (post-crash) + short DAI (above peg) was a popular convergence trade. Both legs benefited from the recovery.

## Who Made Money

- **Specialist DeFi-native desks** (KFB, Three Arrows Capital prior to its 2022 collapse, Polychain) shorted DAI systematically
- **MakerDAO MKR holders who participated in the recapitalization auction** got MKR cheap (it had crashed) and benefited from later MKR appreciation
- **The zero-bid bot operator** captured ~$8.32M of ETH (~35,000 ETH) at $0 cost — a controversial but mechanically-permissioned outcome

## Who Lost Money

- **Vault owners** whose collateral was zero-bid-auctioned (~$8.32M of ETH taken for $0; Maker governance ultimately voted not to compensate them)
- **MKR holders pre-recapitalization** (MKR diluted by ~5% via the recap auction)
- **Long-DAI panic positions** (anyone buying DAI at $1.10 expecting further premium got mean-reversion'd)

## MakerDAO Response — Long-Term Fixes

The Black Thursday experience drove three major MakerDAO architecture changes:

1. **Peg Stability Module (PSM)** — December 2020. Introduced direct USDC↔DAI swap at 1:1 (subject to fee + capacity). This eliminated the above-peg scenario for future events because DAI buyers can mint via PSM at $1.00.

2. **Auction parameter overhaul** — auction durations extended; minimum bid increments enforced; gas-conscious design.

3. **Multi-collateral DAI (MCD) maturation** — broader collateral mix reduced ETH-concentration risk.

These fixes have largely worked: DAI has not had a comparable above-peg episode since.

## Lessons for Modern Stable Depeg Trading

This case study informs three principles for [[stablecoin-depeg-profit-capture]]:

1. **Above-peg depegs are rare but tradable.** Most participants only think about discount depegs; above-peg events (like DAI Mar 2020 or BUSD-related anomalies) are sometimes the larger opportunity.

2. **Mechanism failures can be more profitable than mechanism stress.** The DAI premium emerged because the *system* broke in an unusual way (auction design + gas spikes), not because the peg mechanism stressed normally. These are higher-Sharpe trades but require deep understanding of the protocol's design.

3. **Gas-coupled liquidation systems are fragile.** Modern protocols (Aave V3 with isolated tier system; Curve LLAMMA soft-liquidation) have moved away from gas-priced-in keeper competition. But forks of Compound v2 / pre-PSM MakerDAO architectures still have this exposure.

4. **PSM-style direct redemption is now the standard fix.** Any stable that has a PSM (DAI, GHO, FRAX) can mean-revert quickly to peg in either direction. Stables WITHOUT a PSM (most synthetic/algorithmic stables) are vulnerable to both above-peg and below-peg dislocations.

## Sources

- MakerDAO post-mortem (March 2020): `forum.makerdao.com`
- DAIstats.com historical data
- Etherscan transaction analysis of zero-bid auctions
- Coin Metrics Black Thursday analysis (March 2020)
- The Block / CoinDesk coverage (March 12-19, 2020)
- Vitalik Buterin commentary on liquidation design
- MakerDAO governance proposal records (March-April 2020)

## Related

- [[stablecoin-pair-arbitrage]] — strategy hub
- [[stablecoin-depeg-profit-capture]] — above-peg case is referenced in Method 6
- [[liquidation-cascade-arbitrage]] — adjacent strategy on Aave/Compound liquidations
- [[depeg-risk]] — risk framework
- [[makerdao]] · [[dai]] — entity pages
- [[2023-03-usdc-svb-depeg]] — modern parallel (mechanism stress, but discount-depeg direction)
- [[stablecoin-depeg-history]] — master timeline
