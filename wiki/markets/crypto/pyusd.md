---
title: "PayPal USD (PYUSD)"
type: entity
created: 2026-04-07
updated: 2026-07-16
status: excellent
tags: [crypto, ethereum, mainstream, solana, stablecoins]
aliases: ["PYUSD", "PayPal USD"]
entity_type: protocol
founded: 2023
headquarters: "San Jose, USA (PayPal)"
website: "https://www.paypal.com"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[regulation]]", "[[stablecoin-regulation]]", "[[stablecoins]]", "[[usdc]]"]
---

PayPal USD (ticker **PYUSD**) is a fiat-backed [[stablecoins|stablecoin]] issued by Paxos Trust Company on behalf of PayPal, trading natively on [[ethereum|Ethereum]] (ERC-20) with deployments on [[solana|Solana]], Arbitrum and Stellar. Launched in August 2023, it is the **first stablecoin issued by a major US financial institution**, representing a landmark moment in mainstream adoption of stablecoin technology. PayPal has over 400 million active users globally, giving PYUSD access to the largest existing distribution network of any stablecoin.

> **Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).**
>
> | Metric | Value |
> |---|---|
> | **Price** | $0.999877 |
> | **Market cap** | $2.77B (rank **#36**) |
> | **24h volume** | $61.94M |
> | **24h change** | +0.01% |
> | **7d change** | +0.02% |
> | **Circulating supply** | 2.77B PYUSD |
> | **Total supply** | 2.77B PYUSD |
> | **Max supply** | None (elastic; mint/redeem 1:1 by Paxos) |
> | **Fully diluted valuation** | $2.77B |
> | **All-time high** | $1.081 (2026-04-02) |
> | **All-time low** | $0.959426 (2024-12-05) |
>
> *Macro backdrop: Crypto Fear & Greed Index 23 ("Established Bear Market"). As a fully-reserved USD stablecoin, PYUSD's price is peg-anchored at $1.00 and largely insulated from crypto beta — the relevant variable is supply growth (a proxy for adoption) and peg integrity, not price. Supply contracted from ~$3.96B (April 2026) to ~$2.77B here, a meaningful drawdown in outstanding float worth watching. Figures are point-in-time.*

## Overview

PYUSD was launched on [[ethereum|Ethereum]] in August 2023 and expanded to [[solana|Solana]] in May 2024, later adding Arbitrum and Stellar. As of June 2026 its market capitalisation is approximately **$2.77 billion** (rank #36) -- still small compared to [[usdt|USDT]] ($110B+) and [[usdc|USDC]] ($30B+), but a major step up from its sub-$1B 2024 footprint, even after pulling back from the ~$3.96B peak earlier in 2026.

The stablecoin is issued by **Paxos Trust Company**, a New York-licensed trust company regulated by the New York Department of Financial Services (NYDFS). Paxos is one of the most heavily regulated stablecoin issuers in the world, also having previously issued BUSD for [[binance|Binance]] (ordered to wind down by NYDFS in February 2023) and Pax Dollar (USDP).

## Reserve Backing

PYUSD reserves are composed of:

- **US Treasury securities** (short-term)
- **Cash deposits** at regulated financial institutions
- **US Treasury reverse repurchase agreements**

Paxos publishes **monthly attestation reports** confirming 1:1 backing. The reserve composition is conservative and similar to [[usdc|USDC]], with no crypto assets, commercial paper, or corporate bonds.

## Peg Mechanism & Redemption

PYUSD is a **fiat-collateralised (custodial) stablecoin** — the peg is maintained by full 1:1 reserves and an authorised mint/redeem path, not by algorithmic supply rules or over-collateralisation like [[dai|DAI]]:

- **Mint:** Authorised participants (and PayPal/Venmo users via the app) deposit USD with Paxos, who mints an equal amount of PYUSD. Supply is *elastic* — it expands with deposits and contracts with redemptions, which is why outstanding supply is the cleanest proxy for adoption.
- **Redeem:** PYUSD is redeemed 1:1 for USD through Paxos / the PayPal app. This direct redemption is the core arbitrage that holds the peg: if PYUSD trades below $1, arbitrageurs buy it cheap and redeem at $1; if above, they mint and sell.
- **Reserve segregation:** Reserves are held in bankruptcy-remote accounts and US Treasuries under NYDFS oversight, reducing (though not eliminating) issuer-insolvency risk.

### De-Peg Risk

Despite its conservative design, PYUSD carries the standard custodial-stablecoin risks:

- **Reserve/banking risk:** A failure or freeze at a reserve-holding bank (the scenario that broke [[usdc|USDC]]'s peg to ~$0.88 during the March 2023 SVB crisis) could pressure the peg. PYUSD's snapshot ATL of **$0.959 (Dec 2024)** shows it is not immune to brief dislocations.
- **Liquidity-driven wobble:** Thin DeFi liquidity (see below) means large redemptions or sell-offs can move the secondary-market price more than for USDC/USDT before arbitrage closes the gap. The snapshot ATH of **$1.081 (Apr 2026)** reflects a transient upside dislocation, likely a liquidity squeeze.
- **Issuer/regulatory risk:** Like all custodial stablecoins, PYUSD can be **frozen or blacklisted** by Paxos/PayPal for legal/compliance reasons; a regulatory action against the issuer is an existential tail risk.
- **Redemption gating:** In a stress scenario, redemption throughput depends on Paxos and banking rails remaining open — a constraint that does not apply to fully on-chain stablecoins.

The base case, however, is a very tight peg: the snapshot 24h range is $0.9994-$1.00, and reserves are short-dated and liquid.

## Platform Integration

PYUSD is integrated into PayPal's existing product ecosystem:

- **PayPal app**: US users can buy, sell, hold, and send PYUSD within the PayPal app
- **Venmo**: PYUSD available on PayPal-owned Venmo for peer-to-peer payments
- **Checkout**: PayPal merchants can accept PYUSD as payment (converted to USD for settlement)
- **International transfers**: PYUSD can be sent between PayPal users with zero fees
- **On/off-ramp**: Seamless conversion between USD bank accounts and PYUSD

This integration means PYUSD does not require users to understand crypto wallets, private keys, or blockchain mechanics -- it behaves like a digital dollar within PayPal's walled garden, while also being usable on-chain for DeFi.

## Multi-Chain Deployment

| Blockchain | Launch Date | Notes |
|-----------|------------|-------|
| [[ethereum|Ethereum]] | August 2023 | Original deployment, ERC-20 token |
| Solana | May 2024 | Added for faster, cheaper transactions |

The Solana expansion was significant -- PayPal chose Solana over [[layer-2]] solutions like Arbitrum or Optimism, citing speed and cost advantages. PYUSD on Solana benefits from sub-second finality and fees below $0.01.

## DeFi Integration

Despite its centralised origin, PYUSD has been integrated into several [[defi|DeFi]] protocols:

- **Curve Finance**: PYUSD pools for stablecoin swaps
- **Uniswap**: Trading pairs on Ethereum and Solana
- **Aave**: Available as a supply/borrow asset on [[aave|Aave]]
- **Jupiter**: Major DEX aggregator on Solana

However, PYUSD's DeFi liquidity remains **significantly lower** than [[usdc|USDC]] or [[usdt|USDT]]. For most DeFi strategies, PYUSD would be swapped to USDC or USDT before being deployed in protocols with deeper liquidity.

## Market Structure & Derivatives

- **CEX spot:** Listed on Kraken, Bitget, KuCoin and Crypto.com, mostly as PYUSD/USD or PYUSD/USDT. Notably, PYUSD's largest distribution is *off-exchange* — inside the PayPal and Venmo apps — which is unusual for a top-40 asset.
- **DEX spot:** On-chain liquidity centres on Curve and Uniswap V3 (Ethereum) and Orca (Solana), but pools are shallow relative to USDC/USDT. The deepest on-chain venue is typically a Curve PYUSD/USDC pool used for stable-to-stable routing.
- **24h volume:** ~$61.9M in the snapshot. For a $2.77B stablecoin this is low turnover, consistent with PYUSD being held/transacted within PayPal rather than actively traded on crypto venues.
- **Derivatives:** Essentially none on PYUSD itself — a $1-pegged custodial stablecoin has no directional thesis to trade. PYUSD functions as a *settlement and quote* asset, not an underlying for perps or options.
- **Arbitrage rail:** The Paxos 1:1 mint/redeem path plus the PSM-style Curve pools are the mechanisms that keep secondary-market price aligned to $1.

## Valuation Framing (Qualitative)

PYUSD should trade at $1.00; it is not "valued" like a token. The analytically useful metrics are about *adoption and trust*, not price:

1. **Supply trajectory** — outstanding PYUSD is the single best proxy for adoption. The pullback from ~$3.96B (Apr 2026) to ~$2.77B (Jun 2026) is a yellow flag worth tracking against PayPal's stablecoin push.
2. **Distribution conversion** — what fraction of PayPal's 400M+ users actually hold/use PYUSD? Even single-digit penetration would rival USDC; near-zero conversion would make the distribution thesis moot.
3. **Reserve quality & yield retention** — reserves are short T-bills/cash (high quality), but holders earn no yield (PayPal/Paxos keep it). Yield-bearing competitors and [[stablecoin-yields]] products create a structural demand headwind.
4. **Regulatory tailwind** — under emerging US frameworks (GENIUS/CLARITY), a regulated, fully-reserved issuer like Paxos is among the best-positioned; favourable legislation is the main bull catalyst.

For directional exposure to PYUSD's success, the tradable instrument is **PayPal stock (NASDAQ: PYPL)**, not PYUSD itself.

## Regulatory Position

PYUSD benefits from one of the strongest regulatory positions in the stablecoin market:

- **Paxos Trust Company**: Regulated as a trust company by NYDFS -- subject to regular examinations, capital requirements, and consumer protection rules
- **PayPal**: Publicly traded (NASDAQ: PYPL), subject to SEC reporting, Sarbanes-Oxley compliance, and federal banking regulation
- **Compliance**: Full KYC/AML/CFT compliance within PayPal's existing regulatory framework

Under proposed US stablecoin legislation (GENIUS Act, CLARITY Act), PYUSD would likely be among the first to qualify for any new federal stablecoin licence. See [[stablecoin-regulation]].

## Strategic Significance

PYUSD's importance extends beyond its current market cap:

1. **Mainstream validation**: A Fortune 100 company issuing a stablecoin signals that stablecoins are entering mainstream financial infrastructure
2. **Distribution advantage**: PayPal's 400M+ user base provides unmatched distribution potential. If even 5% of PayPal users adopt PYUSD, it would rival [[usdc|USDC]]'s market cap
3. **TradFi convergence**: PYUSD represents the convergence of traditional finance and crypto -- PayPal, Visa, Mastercard, and Stripe are all building stablecoin capabilities
4. **Competitive pressure**: PYUSD's existence pressures banks, fintechs, and payment companies to develop their own stablecoin or digital dollar strategies
5. **Circle IPO implications**: PayPal competing in stablecoins adds competitive pressure on [[circle|Circle]] ahead of its planned IPO

## Stablecoin Peer Comparison

| Feature | PYUSD | [[usdc\|USDC]] | [[usdt\|USDT]] | [[dai\|DAI]] |
|---|---|---|---|---|
| Issuer | PayPal / Paxos (regulated) | Circle (regulated) | Tether (offshore) | MakerDAO/Sky (decentralised) |
| Backing | Cash + short T-bills | Cash + T-bills | Mixed reserves | Over-collateralised crypto + RWA + USDC |
| Market cap (snapshot) | ~$2.77B | ~$30-35B | ~$110B+ | ~$4.18B |
| Chains | Ethereum, Solana, Arbitrum, Stellar | 10+ | 10+ | Ethereum + L2s |
| DeFi liquidity | Low | Very deep | Deepest | Deep (decentralised) |
| Holder yield | No | No | No | Yes (DSR/sDAI) |
| Can be frozen | Yes | Yes | Yes | No (DAI itself) |
| Distribution edge | PayPal/Venmo 400M+ users | Coinbase, institutions | Emerging-market dominance | DeFi-native |

## Limitations

- **Geographic restriction**: Currently only available to US PayPal users (international expansion planned)
- **Low DeFi liquidity**: Much less liquid than USDC/USDT in DeFi protocols
- **Centralised**: Like USDC and USDT, PYUSD can be frozen by the issuer for compliance/legal reasons
- **Yield**: PYUSD holders do not earn yield on their holdings -- PayPal/Paxos retain the reserve yield. See [[stablecoin-yields]]
- **Limited chain availability**: Only on Ethereum and Solana (vs USDC on 10+ chains)

## For Traders

PYUSD matters primarily as a **signal and catalyst** rather than a trading tool:

- Monitor PYUSD market cap growth as an indicator of mainstream stablecoin adoption
- PYUSD's growth benefits the broader [[ethereum|Ethereum]] and Solana ecosystems
- PayPal stock (PYPL) offers indirect exposure to stablecoin adoption trends
- If PYUSD gains significant market share, it could reshape the USDC/USDT duopoly

For active trading and DeFi, [[usdc|USDC]] and [[usdt|USDT]] remain superior choices due to their deeper liquidity and wider protocol integration.

## Related

- [[stablecoins]] -- Stablecoin market overview
- [[usdc]] -- Primary regulated stablecoin competitor
- [[usdt]] -- Largest stablecoin
- [[ethereum]] -- Primary deployment chain
- [[defi]] -- DeFi integration
- [[regulation]] -- Regulatory landscape
- [[stablecoin-regulation]] -- Country-by-country stablecoin laws
- [[stablecoin-use-cases]] -- Real-world stablecoin adoption
- [[circle]] -- USDC issuer and competitor
- [[dai]] -- decentralised stablecoin alternative

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market-data snapshot, refreshed 2026-06-20
- Paxos / PayPal PYUSD documentation and monthly attestation reports (reserve composition, redemption)
- General crypto market knowledge for adoption history and regulatory context

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
