---
title: "Ethereum ETFs"
type: market
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [crypto, ethereum, etf, institutional, sec, regulation]
aliases: ["ETH ETF", "Ethereum Spot ETF", "Spot ETH ETF"]
related: ["[[ethereum]]", "[[bitcoin-etfs]]", "[[2024-07-23-ethereum-spot-etf-launch]]", "[[2024-01-10-bitcoin-spot-etf-approval]]", "[[sec]]", "[[etf]]"]
---

# Ethereum ETFs

Ethereum ETFs are exchange-traded funds that provide regulated exposure to [[ethereum]] (ETH) without requiring investors to hold the underlying asset directly. Spot ETH ETFs began trading in the United States on July 23, 2024, following a two-step SEC approval process. They represent the second major crypto spot ETF category after [[bitcoin-etfs|Bitcoin ETFs]], though they have attracted significantly lower flows and face structural disadvantages — most notably the exclusion (initially) of [[staking]] yield.

> **This is a reference hub, not a single tradeable asset.** It maps the spot ETH ETF landscape — issuers, fees, structure, the staking angle, and flow dynamics — and links out to the underlying asset ([[ethereum]]) and the precedent product family ([[bitcoin-etfs]]). For a single-product price, consult the issuer's fact sheet; this page does not quote a live NAV.

### Macro backdrop (qualitative, as of 2026-06-21)

The broad crypto tape sits in an **Established Bear Market** with the Crypto Fear & Greed Index around **23 ("Extreme Fear")**. In risk-off regimes, ETF flow data tends to whipsaw: redemptions accelerate on drawdowns, and the ETH/BTC flow split (see [[bitcoin-etfs]]) becomes a sharper read on institutional risk appetite than absolute dollar inflows. No live ETH price or NAV is quoted here by design — this is a structural reference page.

## Products

| Issuer | Ticker | Exchange | Fee | Notes |
|--------|--------|----------|-----|-------|
| BlackRock | ETHA | Nasdaq | 0.25% | iShares Ethereum Trust; largest by AUM |
| Fidelity | FETH | Cboe BZX | 0.25% | Fidelity Ethereum Fund |
| Bitwise | ETHW | NYSE Arca | 0.20% | Low-cost option |
| Grayscale | ETHE | NYSE Arca | 2.50% | Converted from closed-end trust; highest fee |
| Grayscale | ETH | NYSE Arca | 0.15% | Grayscale Ethereum Mini Trust; low-cost alternative |
| 21Shares | CETH | Cboe BZX | 0.21% | Core Ethereum ETF |
| VanEck | ETHV | Cboe BZX | 0.20% | |
| Invesco Galaxy | QETH | Cboe BZX | 0.25% | |
| Franklin Templeton | EZET | Cboe BZX | 0.19% | Lowest standard fee |

The US spot ETH ETF complex is the same issuer cohort that dominates [[bitcoin-etfs|spot BTC ETFs]] — BlackRock, Fidelity, Bitwise, Grayscale, VanEck, Invesco/Galaxy, Franklin Templeton, 21Shares — recycling the wrapper, custody (largely Coinbase Custody), and authorized-participant plumbing built for BTC. As with BTC, the market structure is **fee-tiered**: a high-fee legacy converted trust (Grayscale ETHE at 2.50%) bleeding AUM into a cluster of sub-0.25% challengers, with BlackRock's ETHA the consolidating leader. Most issuers also waived fees for an introductory window or up to an AUM cap to win seed assets.

| Structural feature | Status (2024 launch → 2026) |
|---|---|
| Creation/redemption | Cash-only at launch; in-kind sought by issuers and broadly enabled as the regulatory stance softened |
| Custody | Predominantly Coinbase Custody; same model as BTC ETFs |
| Staking | **Excluded at launch**; staking-enabled ETH ETFs became the central 2025–2026 product battleground (see below) |
| Options | Listed on several products, enabling covered-call / collar overlays |
| Underlying | Spot ETH (not futures); CME ETH futures ETFs predate the spot products |

## Approval Timeline

| Date | Event |
|------|-------|
| Jan 10, 2024 | Spot [[bitcoin-etfs|BTC ETFs]] approved, establishing the regulatory precedent |
| May 23, 2024 | **SEC surprise-approves** Ethereum 19b-4 filings; prediction markets had placed probability below 25% |
| Jul 22, 2024 | S-1 registrations declared effective |
| Jul 23, 2024 | Spot ETH ETFs begin trading (see [[2024-07-23-ethereum-spot-etf-launch]]) |
| Q3 2024 | Net flows turn mixed as Grayscale ETHE outflows dominate |
| Q4 2024 | Flows stabilize; ETH benefits from broader crypto rally |
| 2025 | Flows gradually improve but remain a fraction of BTC ETF volumes |

## Flow Dynamics

ETH ETF flows have consistently underperformed BTC ETFs on every metric:

- **Total net inflows**: Roughly 10-15% of BTC ETF cumulative inflows in the first year
- **Grayscale ETHE outflows**: Mirrored the GBTC pattern exactly — legacy holders rotated to lower-fee alternatives, creating sustained selling pressure
- **BlackRock ETHA**: Dominant product by AUM, capturing the majority of new inflows
- **Fee compression**: Sub-0.25% products attracted most incremental capital

### Why Flows Lag BTC ETFs

1. **Second-mover disadvantage**: BTC ETFs were a paradigm-shifting first; ETH ETFs were an incremental follow-on
2. **No staking yield**: ETH ETFs cannot stake their holdings, meaning holders forgo ~3-5% annual staking rewards. This makes the ETF structurally less attractive than holding ETH directly (or via a staking service)
3. **Weaker institutional narrative**: "Digital gold" (BTC) is a simpler pitch to traditional allocators than "programmable money / world computer" (ETH)
4. **Existing on-chain yield**: Sophisticated investors can earn yield on ETH through staking, [[defi]], and [[restaking]] — the ETF provides none of this
5. **Higher correlation to risk assets**: ETH correlates more closely with tech stocks, making it less useful as a portfolio diversifier compared to BTC

## Staking Exclusion and the Staking-ETF Angle

The most significant structural feature of ETH ETFs is their relationship to [[staking]] yield — the single largest differentiator from [[bitcoin-etfs|BTC ETFs]] (BTC has no native yield to forgo).

**The launch-era drag (2024).** The SEC's initial approval explicitly excluded staking from ETH ETF operations, creating a persistent opportunity cost:

- ETH stakers earn ~3-5% APR in network rewards (variable with network conditions; see [[ethereum]])
- ETH ETF holders earned 0% — and paid a management fee on top
- Net annual cost of holding ETH via a non-staking ETF vs. direct staking is roughly **3.5-5.5%/year**
- This makes a non-staking ETH ETF structurally inferior to holding ETH directly (or via a liquid-staking token such as stETH) for any holder indifferent to custody convenience

**The staking-ETF battleground (2025–2026).** Allowing ETF holdings to be staked transforms the value proposition — it converts the wrapper from a yield-sacrificing convenience into a yield-bearing instrument competitive with direct staking, net of fees. The mechanics issuers must solve:

| Challenge | Why it matters |
|---|---|
| **Liquidity / unbonding** | Staked ETH faces an exit/unbonding queue. An ETF must meet daily redemptions while holdings are locked, so issuers stake only a partial sleeve and hold a liquid buffer |
| **Slashing risk** | Validator misbehavior can be penalized; an ETF must use insured or institutional staking infrastructure |
| **Reward tax/treatment** | Staking rewards may be income; pass-through vs. accrual affects NAV and investor taxation |
| **Securities framing** | A yield-bearing ETF invites the same "is this a security?" debate seen with [[stablecoin-yields|yield-bearing stablecoins]] |

If/when staking is broadly permitted across the complex, it is the clearest single catalyst for ETH ETF flows — closing the yield gap that drove sophisticated capital to direct staking and [[restaking]]. Watch for SEC rule proposals, exemptive relief, and commissioner statements as the leading indicators.

## Trading Implications

- **Relative value signal**: ETH ETF net flows vs BTC ETF net flows provide a real-time gauge of institutional preference between the two assets. Sustained divergence signals shifting allocation trends
- **Grayscale rotation**: The ETHE → low-fee ETF rotation is a predictable headwind. Once ETHE AUM stabilizes, net ETH ETF flows should improve (as happened with GBTC)
- **"Buy the rumor, sell the news"**: The May 2024 surprise approval was the better entry than the July 2024 launch. This pattern should inform expectations for future altcoin ETF products
- **ETH/BTC ratio**: ETH ETF flow data is now a key input for ETH/BTC relative value trades. Accelerating ETH ETF inflows → bullish for ETH/BTC
- **Staking catalyst**: Any SEC signal toward allowing staking in ETH ETFs is likely a significant bullish catalyst — watch for rule proposals and commissioner statements
- **Prediction market lesson**: The sub-25% probability assigned to approval just days before the May 2024 surprise showed how wrong consensus can be. Regulatory events carry more optionality than markets price

## Comparison: ETH ETFs vs BTC ETFs

| Dimension | ETH ETFs | BTC ETFs |
|---|---|---|
| **Launch date** | July 2024 | January 2024 |
| **Cumulative inflows (first year)** | ~$5-8B | ~$50-60B |
| **Largest product** | BlackRock ETHA | BlackRock IBIT |
| **Grayscale outflow problem** | Yes (ETHE, 2.50% fee) | Yes (GBTC, 1.50% fee) |
| **Yield opportunity cost** | High (3-5% staking yield forfeited) | Low (BTC has no native yield) |
| **Institutional narrative** | Complex ("world computer") | Simple ("digital gold") |
| **Regulatory precedent** | Followed BTC ETF | First crypto spot ETF |
| **Impact on asset price** | Modest structural bid | Massive structural bid |

## Future Outlook

Key developments to watch:
- **Staking approval**: Would transform the ETH ETF value proposition overnight
- **Options on ETH ETFs**: Options listing would enable covered call strategies and increase institutional adoption
- **In-kind creation/redemption**: Currently cash-only; in-kind would reduce tracking error and costs
- **Fee war resolution**: Fees are already low; further compression unlikely to move the needle
- **Altcoin ETF cascade**: XRP, SOL, and other altcoin ETF approvals could normalize the ETF wrapper for all crypto, indirectly benefiting ETH ETF adoption

## See Also

- [[ethereum]] — The underlying asset
- [[bitcoin-etfs]] — The precedent-setting BTC ETF products
- [[2024-07-23-ethereum-spot-etf-launch]] — The news event coverage
- [[2024-01-10-bitcoin-spot-etf-approval]] — The BTC ETF approval that set the precedent
- [[sec]] — The regulator
- [[etf]] — ETF structure and mechanics
- [[staking]] — The yield source excluded from ETH ETFs

## Sources

- SEC filings and approval orders (19b-4 and S-1 registrations)
- ETF issuer fact sheets and fee schedules
- Flow data from Bloomberg ETF analytics
- (Source: [[2024-07-23-ethereum-spot-etf-launch]])
