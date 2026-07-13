---
title: "Black Thursday Crypto Crash (March 12, 2020)"
type: news
created: 2026-04-26
updated: 2026-06-12
status: good
tags: [crypto, history, bitcoin, defi, liquidity]
aliases: ["Black Thursday Crypto", "March 12 Crypto Crash", "MakerDAO $0 CDP Bug"]
event_date: 2020-03-12
markets_affected: [crypto, defi]
impact: high
verified: true
sources_count: 5
related: ["[[liquidation-cascade-arbitrage]]", "[[crypto-spot-perp-futures-triangle]]", "[[flash-loan-arbitrage]]", "[[funding-rate-arbitrage]]", "[[2020-03-dai-black-thursday]]", "[[covid-crash]]"]
---

# Black Thursday Crypto Crash (March 12, 2020)

On **March 12-13, 2020**, Bitcoin fell from $7,900 to **$3,915 (intraday low)** — a **51% crash in 24 hours** — as global COVID panic triggered margin liquidations across centralized and decentralized venues. Three structural failures compounded:

1. **BitMEX overload** — the dominant perp exchange went offline for 25 minutes during peak liquidation pressure, preventing close-out flows.
2. **MakerDAO $0 CDP auction bug** — Ethereum gas spiked from ~5 gwei to 200+ gwei; MakerDAO's liquidation auctions failed to receive bids; one keeper bot won **8.32 million DAI of ETH collateral for $0**.
3. **Massive cross-venue dislocations** — BTC simultaneously traded $3,800 (BitMEX) and $4,400 (Coinbase) for several minutes; perp funding rates spiked to -0.75%/8h (-820% APR).

The day generated extraordinary triangular-arb opportunities for traders with capital, infrastructure, and nerve — but most of the obvious trades were impossible to execute due to API failures and gas-price spikes.

## The Crash

| Time (UTC, Mar 12) | BTC (BitMEX) | BTC (Coinbase) | Comment |
|--------------------|--------------|----------------|---------|
| 00:00 | $7,900 | $7,920 | Steady |
| 12:00 | $7,300 | $7,350 | Initial COVID concerns |
| 18:00 | $6,800 | $6,950 | Building selling pressure |
| 22:00 | $5,700 | $6,200 | First cascade; perp funding -0.30%/8h |
| 23:30 | $4,800 | $5,400 | BitMEX overloaded |
| 02:30 (Mar 13) | $3,915 | $4,400 | Bottom; BitMEX briefly offline |
| 04:00 (Mar 13) | $4,950 | $5,000 | Convergence post-bounce |

**BitMEX downtime** was suspicious: many believed the exchange's "DDoS" was strategic to prevent further liquidations from cascading their insurance fund. Internal forensic analysis later showed actual DDoS-like traffic patterns, but the timing was extraordinarily convenient for BitMEX.

## The MakerDAO $0 Bug (and the $8.3M Free ETH)

> The MakerDAO/DAI side of Black Thursday — the zero-bid auctions, the resulting **above-peg** DAI dislocation, the short-DAI trade, and the protocol fixes (PSM, Liquidations 2.0) — is documented in depth in the companion case study [[2020-03-dai-black-thursday]]. This page covers the broader cross-venue market crash.

MakerDAO's collateralized debt positions (CDPs) auto-liquidated when ETH collateral fell below the maintenance ratio. Liquidation auctions ran for 10 minutes; **the highest bidder won at the implied price**.

On Black Thursday:
- Ethereum gas prices spiked from ~5 gwei to **200-1000 gwei**.
- Most arbitrage bots failed to submit bids because their gas configurations were too low.
- One bot operator (later identified as a sophisticated arb desk, name not publicly confirmed) had pre-set extremely high gas configurations — could submit bids even at 1000+ gwei.
- That bot won multiple liquidation auctions at **$0 bids** — taking ETH collateral worth ~$8.32M for essentially zero DAI.

**Total MakerDAO insurance-fund loss:** $5.4M emergency MKR auction needed to recapitalize.

The bug was technically not a bug — the auction mechanism worked as designed; only one keeper had bids in. MakerDAO governance subsequently:
- Slashed the bug-keeper's gains via complex multi-round MKR dilution (reduced winning by ~30%, but most of the gain stayed with the keeper).
- Implemented Liquidations 2.0 (Apr 2021) with continuous Dutch auctions instead of fixed-window batches.

## Triangular Aspects

Five distinct triangular arbitrage opportunities emerged:

**Triangle 1: BTC Coinbase vs BitMEX vs OKEx** — Up to $600 spread between Coinbase ($4,400) and BitMEX ($3,800) for 30+ minutes. Anyone with USDT/USD on multiple venues could buy on BitMEX, sell on Coinbase, capture 15%+ in minutes. Most were blocked by:
- BitMEX downtime.
- Coinbase API rate limits during overload.
- Exchange withdrawal delays.

**Triangle 2: BTC perp funding vs basis vs spot** — BitMEX perp funding hit **-0.375%/8h** (-410% APR), implying massive structural short positioning. Long BitMEX perp + short OKEx futures + long Coinbase spot was a 3-leg trade printing 20-50% APR for 3-7 days afterward.

**Triangle 3: ETH/BTC ratio dislocation** — ETH fell harder than BTC (-50% intraday vs BTC -42%). ETH/BTC ratio dropped from 0.0260 to 0.0218 (-16%). Triangulation between ETH/USD, BTC/USD, ETH/BTC across exchanges offered 200-500 bp spreads.

**Triangle 4: MakerDAO collateral discount + flash loan** — A flash-loan arb could borrow stablecoins, bid on MakerDAO auctions at the discount, sell ETH at market, repay loan, pocket the spread. Required (a) sufficient gas configuration, (b) flash loan integration with Maker, (c) milliseconds of timing.

**Triangle 5: USDT premium dynamics** — USDT traded at 5-10% premium during the panic (flight-to-stable), creating BTC/USDT vs BTC/USD vs USDT/USD triangulation across Bitfinex, Kraken, Binance.

## Winners

**The MakerDAO $0 keeper** — One operator made an estimated $8.32M in 24 hours from the auction bug. Identity never publicly confirmed; rumor suggested Cumberland-DRW or a small specialist arb desk.

**Alameda Research** — Sam Bankman-Fried's team had pre-positioned BTC OTM puts and was reportedly net long-vol on March 12. Estimated $50-100M profit.

**Cross-exchange arbitrageurs with multi-venue infrastructure** — Cumberland-DRW, Genesis Trading, B2C2, Jump Crypto reportedly extracted $20-50M each from the inter-venue spreads.

**Volatility funds** — Crypto vol indices (DVOL on Deribit) spiked from 50% to 200%+. Long-vol traders printed.

**Coinbase prime customers** — Coinbase remained operational; institutional buyers absorbed BTC at $4,000-5,000 levels and held; many doubled by year-end.

**Microstrategy founder Michael Saylor** — Began publicly buying BTC for MicroStrategy treasury ~6 months later (August 2020), citing the post-Black-Thursday recovery as proof of resilience.

## Losers

**BitMEX retail traders** — Catastrophic liquidations. Many users were force-liquidated at $3,800-4,000 BTC even though spot was $4,400+ on Coinbase. Class-action discussions (no major suits eventually).

**MakerDAO insurance fund** — $5.4M recapitalization required via MKR dilution.

**MakerDAO MKR holders** — Diluted via emergency mint; MKR price fell 50%+ over the following month.

**Highly leveraged DeFi positions on Compound/dYdX** — Many liquidated; some at unfavorable prices due to oracle delays.

**USDT-denominated stablecoin yield farms** — Yields collapsed; some early DeFi protocols saw mass withdrawals.

## Aftermath

- **March 13-31, 2020:** BTC recovered to $6,000+; gradual recovery to $9,000 by end of April.
- **April 2020:** MakerDAO Liquidations 2.0 designed; deployed April 2021.
- **June 2020:** Compound's COMP token launch kicked off DeFi Summer.
- **August 2020:** MicroStrategy first BTC purchase; institutional adoption thesis confirmed.
- **October 2020:** PayPal added BTC support; institutional-driven rally accelerated.
- **December 2020:** BTC re-tested $20,000 ATH from 2017.
- **Late 2020-2021:** Massive bull run; BTC peaked $69,000 November 2021.

## Lessons for Crypto Traders

1. **Exchange downtime is a structural arb risk.** BitMEX going offline at the worst possible moment cost users billions and benefited the exchange's insurance fund.
2. **Gas pricing is the difference between profit and loss in DeFi crisis events.** The MakerDAO $8M bug was won by one bot with unusually high gas configuration.
3. **Flash loans turn capital constraints into infrastructure problems.** With sufficient flash loan integration, the MakerDAO arb required zero capital.
4. **Cross-venue spreads of 10-20% appear in crisis windows but vanish in minutes.** Pre-positioned multi-venue infrastructure is the gating moat.
5. **Funding rate extremes (-820% APR) create durable basis-trade alpha.** Even after the immediate crisis, the funding-rate dislocation persisted for days, generating risk-managed arb returns.
6. **Stablecoin premium dynamics under stress** are predictable: USDT/USDC/DAI traded at 1-10% premium during the panic; the basket converged within a week.

## Sources

- BitMEX, *Post-mortem of March 12-13 Outage* (March 2020).
- MakerDAO Foundation, *Black Thursday Response* whitepaper (April 2020).
- Cyrus Younessi (MakerDAO contributor), *The MKR Auction Mechanism* analysis (March 2020).
- Glassnode On-Chain Analysis, March 2020 series.
- Frank Chaparro / The Block, contemporaneous coverage March 12-15, 2020.

## Related

[[liquidation-cascade-arbitrage]] · [[crypto-spot-perp-futures-triangle]] · [[flash-loan-arbitrage]] · [[funding-rate-arbitrage]] · [[2020-03-dai-black-thursday]] · [[covid-crash]] · [[2017-12-cme-bitcoin-futures-launch]] · [[2022-05-terra-luna-depeg-arb]] · [[2022-06-steth-depeg]] · [[2020-03-ackman-pandemic-cds-trade]]
