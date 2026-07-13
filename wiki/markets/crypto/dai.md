---
title: "DAI"
type: entity
created: 2026-04-07
updated: 2026-06-20
status: excellent
tags: [crypto, decentralized, defi, ethereum, stablecoin]
aliases: ["DAI", "MakerDAO DAI"]
entity_type: protocol
founded: 2017
headquarters: "Decentralised (MakerDAO)"
website: "https://makerdao.com"
related: ["[[makerdao]]", "[[aave]]", "[[automated-market-maker]]", "[[crypto-markets]]", "[[defi-lending]]", "[[defi]]", "[[ethereum]]", "[[stablecoin-depegs]]", "[[stablecoin-yields]]", "[[stablecoins]]", "[[uniswap]]", "[[usdc]]"]
---

DAI (ticker **DAI**) is the largest [[defi|decentralised]] [[stablecoins|stablecoin]], issued by the [[makerdao|MakerDAO]] / [[sky|Sky]] protocol on [[ethereum|Ethereum]]. Unlike centralised stablecoins such as [[usdc|USDC]] and [[usdt|USDT]], DAI is created through over-collateralised lending -- users deposit crypto assets into smart contract "Vaults" and mint DAI against their collateral. No single entity can freeze, blacklist, or censor DAI transactions, making it the standard censorship-resistant stablecoin for [[defi|DeFi]].

> **Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).**
>
> | Metric | Value |
> |---|---|
> | **Price** | $0.999654 |
> | **Market cap** | $4.18B (rank **#25**) |
> | **24h volume** | $82.37M |
> | **24h change** | -0.02% |
> | **7d change** | -0.02% |
> | **Circulating supply** | 4.18B DAI |
> | **Total supply** | 4.18B DAI |
> | **Max supply** | None (elastic; minted/burned against collateral) |
> | **Fully diluted valuation** | $4.18B |
> | **All-time high** | $1.22 (2020-03-13) |
> | **All-time low** | $0.88196 (2023-03-11) |
>
> *Macro backdrop: Crypto Fear & Greed Index 23 ("Established Bear Market"). As a USD-pegged stablecoin, DAI's price is peg-anchored near $1.00 and is largely insulated from directional crypto beta; the relevant risk is de-peg, not drawdown. Supply is elastic — it expands and contracts with vault demand and the [[sky|Sky]] PSM, so market cap reflects collateralised borrowing demand more than speculation.*
>
> Figures are point-in-time and will drift; treat as historical. A prior version of this page carried a snapshot for an unrelated PulseChain token also ticking "DAI" — those figures have been removed in favour of the canonical [[makerdao|MakerDAO]] DAI above.

## Overview

DAI launched in December 2017 as "Single-Collateral DAI" (SCD), backed only by ETH. In November 2019, MakerDAO upgraded to "Multi-Collateral DAI" (MCD), enabling multiple collateral types including WBTC, USDC, real-world assets, and various [[ethereum|Ethereum]] tokens.

As of June 2026, DAI has a market capitalisation of approximately **$4.18 billion** (rank #25 overall), keeping it among the largest stablecoins behind [[usdt|USDT]] and [[usdc|USDC]], and the largest decentralised stablecoin by a wide margin. Note that DAI's supply is *elastic* — there is no fixed maximum; tokens are minted when users borrow against collateral and burned when debt is repaid, so its "market cap" is really a measure of outstanding collateralised debt plus PSM-swapped stablecoins, not market sentiment.

## How DAI Works

### Vault Mechanism

1. A user deposits collateral (e.g., ETH, WBTC, USDC) into a Maker Vault smart contract
2. The user mints DAI against this collateral, up to the maximum allowed by the collateral ratio
3. Most vault types require a **minimum 150% collateralisation ratio** -- to mint $1,000 of DAI, the user must lock at least $1,500 in collateral
4. If the collateral value falls below the liquidation threshold, the vault is automatically liquidated -- collateral is sold to repay the DAI debt plus a liquidation penalty
5. To recover their collateral, the user repays the DAI debt plus a **stability fee** (variable interest rate set by governance)

### Peg Stability

DAI maintains its $1 peg through economic incentives:

- **If DAI > $1**: Users are incentivised to open vaults and mint new DAI (selling it at above-par value), increasing supply and pushing the price down
- **If DAI < $1**: Users are incentivised to buy cheap DAI and repay their vault debts (effectively buying back $1 of debt for less than $1), reducing supply and pushing the price up
- **DAI Savings Rate (DSR)**: A variable interest rate earned by DAI holders who deposit into the DSR contract. Used as a monetary policy tool -- higher DSR incentivises DAI holding, increasing demand

## Governance

MakerDAO is governed by holders of the MKR token, who vote on critical parameters:

- **Stability fees**: Interest rates charged to vault creators (revenue for the protocol)
- **Collateral types**: Which assets can be used as vault collateral
- **Debt ceilings**: Maximum DAI that can be minted against each collateral type
- **Liquidation ratios**: Minimum collateralisation required before liquidation
- **DAI Savings Rate**: Yield paid to DAI depositors
- **Risk parameters**: Oracle configuration, auction parameters, emergency shutdown

MKR also acts as the "lender of last resort" -- if the system becomes undercollateralised (e.g., during a rapid price crash where liquidations fail to recover enough), new MKR tokens are minted and sold to cover the deficit, diluting existing MKR holders.

## Sky Protocol Rebrand (2024)

In September 2024, MakerDAO announced a rebrand to **"Sky" protocol**:

- DAI is being migrated to **"USDS" (Sky Dollar)**
- MKR is being migrated to **"SKY"** governance token
- The upgrade introduces "SubDAOs" (now "Stars") -- specialised DAOs managing different aspects of the protocol

The rebrand has been **controversial** within the community. Many users and protocols continue to refer to "DAI" and "MakerDAO," and it remains unclear whether the rebrand will achieve broad adoption. Both DAI and USDS coexist during the migration period.

## Collateral Composition

As of late 2024, DAI/USDS collateral includes:

| Collateral Type | Approximate Share | Notes |
|----------------|------------------|-------|
| Real-World Assets (RWA) | ~40% | US Treasuries, institutional loans via partners like BlockTower, Monetalis |
| USDC and stablecoins | ~25% | PSM (Peg Stability Module) -- direct 1:1 swap between USDC and DAI |
| ETH and staked ETH | ~20% | Traditional crypto collateral |
| WBTC and other crypto | ~10% | Multi-collateral vault types |
| Other | ~5% | Various smaller vault types |

### The Centralisation Paradox

A significant portion of DAI's backing comes from [[usdc|USDC]] (through the Peg Stability Module) and US Treasuries (through RWA vaults). This means that DAI -- the premier "decentralised" stablecoin -- is **partially dependent on centralised assets** and counterparties:

- If Circle froze USDC held in the PSM, a substantial portion of DAI's backing would be at risk
- If US Treasury markets experienced severe disruption, RWA-backed DAI could be affected

This tension between decentralisation ideals and practical stability is an ongoing debate within the Maker community. Purists argue for reducing USDC exposure; pragmatists note that RWAs provide the most stable and profitable backing.

## Revenue Model and DAI Savings Rate

MakerDAO earns revenue from:

1. **Stability fees**: Interest charged to vault creators (e.g., 5-8% on ETH vaults during high-rate periods)
2. **RWA yield**: US Treasury and institutional loan yields (~4-5%) on real-world asset collateral
3. **Liquidation penalties**: Fees charged during vault liquidations (typically 13%)

A portion of this revenue is distributed to DAI holders through the **DAI Savings Rate (DSR)**. During 2023-2024, the DSR ranged from 5-8%, funded primarily by RWA yields. Users who deposit DAI into the DSR contract receive **sDAI** (savings DAI), a yield-bearing stablecoin that automatically appreciates against DAI. See [[stablecoin-yields]].

This makes DAI/sDAI one of the few stablecoins where holders can earn yield directly from the protocol, unlike [[usdc|USDC]] and [[usdt|USDT]] where the issuer retains all reserve yield.

## De-Peg History

DAI has experienced several notable de-pegs:

- **March 2020 ("Black Thursday")**: ETH crashed 43% in a single day. Liquidation auctions malfunctioned, allowing some bidders to buy collateral for $0. The system became undercollateralised, requiring emergency MKR dilution. DAI traded above $1.05 for weeks as demand for DAI (to repay vaults) exceeded supply.
- **March 2023**: DAI de-pegged to ~$0.89 following the [[usdc|USDC]]/SVB crisis, because a significant portion of DAI collateral was USDC. When USDC recovered, DAI recovered. See [[stablecoin-depegs]].

## Use in DeFi

DAI is deeply integrated into [[defi|DeFi]]:

- **Lending**: Widely available on [[aave|Aave]], Compound, Spark Protocol (Maker's own lending protocol)
- **AMM pools**: Core pair on [[uniswap|Uniswap]] and Curve Finance. DAI/USDC/USDT (3pool) is a benchmark DeFi pool
- **Censorship-resistant settlement**: DAI is the preferred stablecoin when censorship resistance matters -- no entity can freeze or seize DAI
- **Composability**: sDAI (yield-bearing version) is increasingly used as collateral in other DeFi protocols
- **Cross-chain**: Available on multiple [[layer-2]] networks and alternative L1 chains

## Market Structure & Derivatives

DAI's market structure differs fundamentally from a speculative token — it is a unit of account rather than a trade:

- **Spot venues:** DAI trades on virtually every major CEX (Binance, Coinbase, Kraken, OKX) and is a base/quote pair in countless DeFi pools. Its deepest liquidity is on-chain in the Curve **3pool** (DAI/USDC/USDT) and Uniswap stable pools, where it is a benchmark constituent.
- **24h volume:** ~$82.4M in the snapshot. For a $4.18B stablecoin this turnover is modest, reflecting DAI's role as a held/settled asset (and increasingly held as yield-bearing **sDAI**) rather than an actively traded one.
- **Redemption / mint path:** The most important "venue" is the protocol itself. Anyone can mint DAI by locking collateral or burning it by repaying debt; the **Peg Stability Module (PSM)** offers near-instant 1:1 swaps between DAI and [[usdc|USDC]], which is the dominant arbitrage rail keeping the peg tight.
- **Derivatives:** There is essentially no perp/futures market on DAI itself (a stablecoin pegged to $1 has no directional thesis to speculate on). DAI instead serves as *collateral and settlement* for derivatives elsewhere — margin on DEX perps, quote currency for options, and the borrow asset in money markets.
- **Peg tightness:** 24h range hugs $1.00; the snapshot shows ATH $1.22 (Black Thursday demand spike, 2020) and ATL $0.882 (the March 2023 USDC/SVB contagion). Both extremes were event-driven and resolved within weeks.

## Valuation Framing (Qualitative)

DAI is not "valued" the way a token is — it should trade at $1.00 and any deviation is the signal. The relevant analytical questions are:

1. **Peg integrity** — how tight is the band around $1, and what is the depth of the PSM/arbitrage that defends it? A persistent premium signals minting frictions; a persistent discount signals collateral or confidence stress.
2. **Backing quality** — what fraction of collateral is liquid and safe (T-bills, USDC) vs volatile/illiquid (long-tail crypto, RWA loans)? Higher safe-asset backing means a more robust peg but more centralisation exposure.
3. **Yield competitiveness** — the [[stablecoin-yields|DSR/sDAI]] rate vs T-bill yields and competitor stablecoin yields drives demand for *holding* DAI, which expands supply.
4. **Surplus buffer** — MakerDAO/Sky's accumulated surplus (protocol equity) is the first loss-absorbing layer before MKR/SKY dilution; a thick buffer means the system can absorb bad debt without diluting governance holders.

For the governance token's valuation (MKR/SKY), see [[makerdao]] and [[sky]] — that is where protocol revenue, the surplus buffer, and the lender-of-last-resort dilution mechanics actually accrue value.

## DAI vs Other Stablecoins

| Feature | DAI | [[usdc|USDC]] | [[usdt|USDT]] | [[pyusd\|PYUSD]] |
|---------|-----|------|------|------|
| Issuer model | Decentralised (MakerDAO/Sky governance) | Circle (regulated) | Tether (offshore) | PayPal / Paxos (regulated) |
| Can be frozen/blacklisted | No (DAI itself) | Yes | Yes | Yes |
| KYC required | No | No (hold), yes (redeem) | No (hold), yes (redeem) | Yes (PayPal account) |
| Yield for holders | Yes (DSR/sDAI) | No | No | No |
| Backing | Over-collateralised crypto + RWA + USDC | Cash + T-bills | Mixed reserves | Cash + T-bills |
| Backing transparency | Fully on-chain | Monthly attestation | Quarterly attestation | Monthly attestation |
| Capital efficiency | Low (over-collateralised) | High (1:1) | High (1:1) | High (1:1) |
| Market cap (snapshot) | ~$4.18B | ~$30-35B | ~$110B+ | ~$2.77B |

## Related

- [[stablecoins]] -- Stablecoin market overview
- [[defi]] -- Decentralised finance ecosystem
- [[ethereum]] -- DAI's primary blockchain
- [[usdc]] -- Centralised competitor (also significant DAI collateral)
- [[usdt]] -- Largest stablecoin
- [[aave]] -- Major lending market for DAI
- [[defi-lending]] -- Lending protocols using DAI
- [[automated-market-maker]] -- AMM pools containing DAI
- [[impermanent-loss]] -- Relevant for DAI liquidity provision
- [[stablecoin-yields]] -- sDAI and yield-bearing stablecoins
- [[stablecoin-depegs]] -- DAI de-peg history
- [[makerdao]] -- issuing protocol and MKR governance
- [[sky]] -- Sky rebrand, USDS and SKY tokens
- [[pyusd]] -- regulated TradFi stablecoin competitor

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — market-data snapshot reconciled to the canonical MakerDAO DAI (rank #25), refreshed 2026-06-20
- MakerDAO / Sky documentation (vault mechanics, PSM, DSR/sDAI, governance)
- General crypto market knowledge for protocol history and de-peg events

## Platform & Chain Information

**Native Chain:** [[ethereum|Ethereum]] (deployed cross-chain to multiple [[layer-2]] networks and alternative L1s).

### Canonical Contract Address

| Chain | Address |
|---|---|
| Ethereum | `0x6b175474e89094c44da98b954eedeac495271d0f` |

> *Note: a separate, unrelated token also using the "DAI" ticker exists on PulseChain; it is not the MakerDAO/Sky DAI documented here.*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

- **December 2017** — Single-Collateral DAI (SCD) launches, backed only by ETH.
- **November 2019** — Multi-Collateral DAI (MCD) launch enables WBTC, USDC, RWA and other collateral types.
- **March 2020 ("Black Thursday")** — liquidation-auction failure; emergency MKR dilution; DAI traded above $1.05 (snapshot ATH $1.22).
- **March 2023** — DAI de-pegged to ~$0.882 during the USDC/SVB crisis (snapshot ATL), recovering with USDC.
- **September 2024** — MakerDAO announces the [[sky|Sky]] rebrand: DAI ↔ USDS and MKR ↔ SKY migration.
- **June 2026** — DAI holds its peg at ~$1.00 with a ~$4.18B market cap (rank #25) amid an "Established Bear Market" (Fear & Greed 23).

---

## See Also

- [[crypto-markets]]
- [[stablecoins]]
- [[makerdao]]

---
