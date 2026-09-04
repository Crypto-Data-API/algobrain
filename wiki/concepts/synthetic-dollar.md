---
title: "Synthetic Dollar"
type: concept
created: 2026-07-19
updated: 2026-09-05
status: good
tags: [crypto, defi, stablecoins, derivatives, yield]
aliases: ["Synthetic Stablecoin", "Delta-Neutral Dollar", "Delta-Neutral Stablecoin"]
domain: [defi, stablecoins]
prerequisites: ["[[stablecoins]]", "[[carry-trade]]", "[[funding-rate]]"]
difficulty: advanced
related: ["[[ethena-usde]]", "[[ethena]]", "[[stablecoins]]", "[[funding-rate-arbitrage]]", "[[carry-trade]]", "[[dai]]", "[[makerdao]]", "[[usdc]]", "[[usdt]]", "[[stablecoin-depeg-profit-capture]]", "[[synthetic-stablecoin-depeg-arbitrage]]", "[[basis-carry-regime]]", "[[depeg-risk]]", "[[funding-rates]]"]
---

# Synthetic Dollar

A **synthetic dollar** is a stablecoin that maintains its $1 peg through derivatives and collateral mechanics — specifically a **delta-neutral hedge** — rather than through fiat reserves held at a bank or overcollateralized crypto locked in a vault. [[ethena-usde|Ethena's USDe]] is the flagship (and, as of writing, only large-scale) example: it holds staked crypto collateral and simultaneously shorts an equal notional in perpetual futures, so that price moves in the collateral are offset by the short. Because the position pays out staking yield plus perpetual funding, a synthetic dollar is best understood as a **tokenized carry trade** wrapped in a stable-value wrapper — its yield is real but cyclical, and its risks (funding flipping negative, custody/venue failure) are structurally different from either a fiat-backed or a crypto-overcollateralized stablecoin's failure modes.

## The Mechanism: Delta-Neutral Basis Trade

The mechanism has three moving parts:

1. **Long the collateral.** The issuer holds staked ETH, BTC, SOL, or liquid staking derivatives (stETH and similar) as collateral, deposited by a whitelisted market maker in exchange for newly minted synthetic-dollar tokens at a 1:1 rate against the collateral's dollar value.
2. **Short an equal notional in perpetuals.** The issuer simultaneously opens a short perpetual futures position of the same notional value on centralized exchanges and/or on-chain perp venues (Ethena hedges across CEXs and [[hyperliquid|Hyperliquid]]), holding the collateral itself with off-exchange custodians rather than on the exchange where the short is booked.
3. **Delta cancels out.** Because the long spot/staked position and the short perp position move in opposite directions by construction, the combined position's value is insulated from the collateral's price movement — this is what "delta-neutral" means. The dollar value of the position stays roughly constant regardless of whether the underlying collateral asset rallies or crashes.

**Revenue = staking yield + perp funding.** The collateral itself earns staking yield (if it's staked ETH or a similar yield-bearing asset). The short perp leg earns (or pays) funding — and because crypto perpetual futures are structurally long-biased most of the time, funding is positive more often than not, meaning the short side gets paid to hold the hedge. Both revenue streams flow to holders of the yield-bearing wrapper token (sUSDe, in Ethena's case) who stake the base synthetic dollar. This is precisely the [[carry-trade|carry trade]] crypto traders run manually — long spot, short perp, collect the funding spread — tokenized into a stable-value instrument anyone can hold. See [[basis-carry-regime]] for the regime-level framing of when this trade is healthy versus crowded.

## Key Risks

The synthetic-dollar model trades fiat-custody risk and crypto-collateral-liquidation risk for a different risk set entirely:

- **Funding-rate flips.** When [[funding-rate|funding]] turns negative for a sustained period — which happens in risk-off, bearish, or heavily-shorted market conditions — the issuer's short perp leg *pays* funding instead of earning it. Revenue turns negative, and the protocol must draw down a reserve fund (or cut the yield paid to holders) to keep operating the hedge. Prolonged negative funding is the single most important stress scenario for any synthetic dollar, and it is structurally impossible for a fiat-backed or crypto-overcollateralized design to face this specific risk, since neither depends on perpetual-futures funding at all.
- **Venue and custody risk.** The short leg lives on centralized exchanges (and/or on-chain perp venues), meaning the issuer bears counterparty and custody exposure to those venues independent of the collateral's own solvency — an exchange insolvency, withdrawal freeze, or hack can impair the hedge even if the underlying collateral asset is fine.
- **De-peg scenarios distinct from fiat-backed de-pegs.** A fiat-backed stablecoin depegs from a reserve or redemption failure (e.g., USDC's brief 2023 wobble when Circle's reserves were partly held at the failing Silicon Valley Bank); a crypto-overcollateralized stablecoin depegs from a collateral-value crash outrunning liquidations. A synthetic dollar depegs from a **funding/basis stress event**: negative funding eroding the reserve buffer, a redemption queue backing up under whitelisted-flow constraints, or a sudden liquidity crunch on the hedging venue during a broad deleveraging event. USDe's brief dips to $0.9295 (October 2024) and a repeat wobble in October 2025 during a market-wide deleveraging cascade are both instances of this synthetic-specific stress, not a reserve failure in the fiat-backed sense. [[synthetic-stablecoin-depeg-arbitrage]] and [[stablecoin-depeg-profit-capture]] cover the trades built around this distinction, and [[depeg-risk]] covers the general concept.
- **Reserve-fund transparency.** Solvency depends on the reserve fund's size relative to circulating supply and on the actual custody arrangements for the collateral — opacity here is the core credit risk, structurally similar to the disclosure concerns around fiat reserve composition, but applied to a hedge book instead of a bank balance.

## How Synthetic Dollars Differ from Other Stablecoin Designs

[[stablecoins|The wiki's stablecoin peg-mechanism comparison]] treats synthetic/delta-neutral as one of four structurally distinct families, alongside fiat-backed, crypto-overcollateralized, and (now largely discredited) algorithmic seigniorage designs:

| Design | Peg mechanism | Capital efficiency | Primary failure mode | Examples |
|---|---|---|---|---|
| **Fiat-backed** | 1:1 redeemable for off-chain reserves | High (1:1) | Reserve/bank failure or freeze | [[usdc]], [[usdt]] |
| **Crypto-overcollateralized** | Over-collateralized crypto vault, arbitraged via mint/redeem + liquidations | Low (130-170%+) | Collateral crash + liquidation cascade outrunning the buffer | [[dai]] |
| **Synthetic / delta-neutral** | Long staked collateral hedged with an equal-notional short perp | Medium (close to 1:1 in substance) | Negative funding regimes; exchange/custody counterparty risk | [[ethena-usde\|USDe]] |
| **Algorithmic (seigniorage)** | Mint/burn a sister token to expand/contract supply, no hard collateral floor | Very high | Reflexive death spiral | UST/LUNA (failed) |

The practical distinctions that matter most for a trader:

- **Versus fiat-backed (USDC/USDT):** a synthetic dollar is not redeemable against a bank account — it is redeemable against a hedge book. It typically offers native, on-chain yield without relying on a regulated issuer passing through T-bill interest (which regulators including the US GENIUS Act have restricted for regulated fiat-backed issuers), but that yield is variable and can go to zero or negative in the underlying economics even if the peg itself holds.
- **Versus crypto-overcollateralized (DAI):** a synthetic dollar is markedly more capital-efficient — it does not need to lock 130-170% of collateral value to mint 100% of face value, because the short perp (not excess collateral) absorbs price risk. The tradeoff is that DAI's liquidation-based risk is transparent and on-chain, while a synthetic dollar's hedge book, custody arrangements, and reserve-fund coverage are comparatively opaque and depend on trusting the issuer's execution and disclosure.
- **The supply signal is inverted relative to a normal token.** A synthetic dollar's circulating supply is a real-time gauge of how crowded the underlying long-perp carry trade is: supply growth means the trade is profitable and attracting capital (compressing the funding rate other participants can earn); supply contraction means funding has turned muted or negative and the trade is unwinding — exactly what happened to USDe's supply through 2026 (falling from a ~$14B late-2025 peak toward ~$4.5B by mid-2026 as funding compressed). This makes synthetic-dollar supply a genuinely useful cross-market signal for perp funding conditions generally, not just for the issuer's own solvency.

## Getting the Data (CryptoDataAPI)

[[cryptodataapi|CryptoDataAPI]] does not track a synthetic dollar's own supply or reserve-fund data directly, but it verifiably covers the two live inputs that determine whether a synthetic dollar's yield is healthy or stressed: the stablecoin-market backdrop and the funding-rate leg of the hedge.

**Live data:**
- `GET /api/v1/sentiment/stablecoins` — current aggregate stablecoin market cap with 14d/90d flow deltas; a synthetic dollar's own mint/redeem flow is a subset of this broader stablecoin-supply signal (see [[cryptodataapi-sentiment]])
- `GET /api/v1/derivatives/funding-rates?coin=BTC` (or `ETH`) — cross-exchange (Binance + Hyperliquid) current funding rate, the direct proxy for whether a synthetic dollar's short-perp leg is currently earning or paying (see [[cryptodataapi-derivatives]])

**Historical data:**
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — up to 365 days of daily stablecoin market-cap history, for tracking supply-contraction cycles
- `GET /api/v1/backtesting/funding` — deeper funding-rate archive back to 2020, for backtesting how sustained negative-funding periods have historically played out

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-sentiment]], [[cryptodataapi-derivatives]].

## Related

- [[ethena-usde]] — the flagship synthetic dollar; full market data, tokenomics, and 2025-2026 supply-contraction history
- [[ethena]] — the issuing protocol and its governance token (ENA)
- [[stablecoins]] — the peg-mechanism comparison table this page's design family sits within
- [[carry-trade]] — the underlying basis/funding trade a synthetic dollar tokenizes
- [[funding-rate-arbitrage]] — the manual version of the trade a synthetic dollar automates and wraps
- [[basis-carry-regime]] — regime-level framing for when the carry trade underlying a synthetic dollar is healthy versus crowded/fragile
- [[dai]], [[makerdao]] — the crypto-overcollateralized alternative design
- [[usdc]], [[usdt]] — the fiat-backed alternative design
- [[stablecoin-depeg-profit-capture]], [[synthetic-stablecoin-depeg-arbitrage]] — strategies trading synthetic-dollar-specific depeg stress
- [[depeg-risk]] — general concept of a stablecoin trading away from its peg

## Sources

- [[ethena-usde]] — wiki entity page with verified mechanism detail, supply trajectory, and depeg history for the flagship synthetic dollar
- [[stablecoins]] — wiki concept page for the four-family peg-mechanism comparison this page builds on
- [[cryptodataapi-sentiment]], [[cryptodataapi-derivatives]] — wiki source pages verifying the cited CryptoDataAPI endpoints (fetched from https://cryptodataapi.com/api/docs)
- General knowledge of delta-neutral basis-trade mechanics, cross-checked against the cited wiki pages
