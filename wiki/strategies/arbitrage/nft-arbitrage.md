---
title: "NFT Arbitrage"
type: strategy
created: 2026-04-07
updated: 2026-10-17
status: review
tags: [arbitrage, nft, opensea, blur, marketplace, floor-price, traits, fractionalization, crypto]
aliases: ["NFT Arb", "NFT Marketplace Arbitrage", "NFT Floor Arbitrage"]
strategy_type: algorithmic
timeframe: scalp|day
markets: [crypto]
complexity: advanced
backtest_status: untested
related: ["[[nft-trading]]", "[[nft]]", "[[decentralized-exchanges]]", "[[cross-exchange-arbitrage]]", "[[wash-trading]]", "[[cryptodataapi]]"]

# Edge characterization
edge_source: [structural, informational]
edge_mechanism: "NFT marketplace fragmentation (no shared order book) creates persistent price dislocations; the counterparty is uninformed sellers who list below the clearing price on a low-traffic venue, and slow/manual buyers who do not monitor all venues simultaneously."

# Data and infrastructure requirements
data_required: [nft-floor-data, marketplace-listings, on-chain-gas, rarity-scores]
min_capital_usd: 2000
capacity_usd: 10000000
crowding_risk: high

# Performance expectations
expected_sharpe: 0.8
expected_max_drawdown: 0.50
breakeven_cost_bps: 500

# Kill criteria
kill_criteria: |
  - collection floor drops > 30% while holding inventory
  - NFT held > 7 days without a bid within 10% of ask (trait arb)
  - combined fees + royalties > 80% of gross spread on any cross-marketplace trade
gates:
  - id: liquid_collections
    role: universe
    rule: "Screen out thinly traded collections: only collections with enough volume for a realistic exit"
    runnable: partial
    endpoint: /api/v1/nfts/overview?days=7
    field: top_collections[].volume_usd_24h
    note: "From the page's agent workflow, which sets no volume floor. Treat reported volume as wash-trading suspect; daily per-collection history is on /nfts/collections/{slug} (series[].volume_usd)."
  - id: cross_marketplace_spread
    role: entry
    rule: "Buy when the cross-marketplace price gap exceeds marketplace fee + royalty + gas: more than 5% for low-floor and 3% for high-floor collections"
    runnable: false
    note: "Per-marketplace listings and floor prices are not served; /nfts/overview marketplaces[] carries volume and trade counts only. Needs OpenSea, Blur and Magic Eden APIs."
  - id: trait_underpriced
    role: entry
    rule: "Buy a rare-trait NFT listed within 10% of floor when comparable rare traits sold at 2-5x floor recently"
    runnable: false
    note: "Trait rarity, listings and per-token sales are not served."
  - id: wrapped_vault_gap
    role: entry
    rule: "Arbitrage a vault token when its redemption value differs from the floor price by more than gas plus the vault fee"
    runnable: false
    note: "Vault redemption values and floor prices are not served."
  - id: speculative_flow
    role: filter
    rule: "Cross the 5-15% round-trip fees only while speculative flow is active"
    runnable: partial
    endpoint: /api/v1/meme/regime/score
    field: composite_score
    note: "From the page's agent workflow: the meme-regime score is the nearest proxy for NFT risk appetite. The page gives no cut-off."
  - id: immediate_resale
    role: exit
    rule: "Cross-marketplace: list on the target marketplace immediately after purchase and accept the best offer above cost"
    runnable: true
    input: position
  - id: price_cut_48_72h
    role: exit
    rule: "If the NFT has not sold within 48-72 hours, cut the ask in steps"
    runnable: true
    input: position
  - id: floor_below_cost
    role: stop
    rule: "If the collection floor drops below the purchase price, cut the loss unless the trait premium still holds"
    runnable: false
    note: "Collection floor prices are not served, and the trait-premium call is a judgement."
---

# NFT Arbitrage

**NFT arbitrage** buys a non-fungible token, or a near-substitute floor item, where it is priced below what another venue, a vault, or an informed buyer will pay, and sells it there. The strategy has three variants: cross-marketplace spreads, trait mispricing, and NFT-vs-vault-token (NFTX/Sudoswap) gaps. All three are bounded by 5-15% round-trip costs and by inventory that may not sell. Since the 2021-22 peak, volume and the number of liquid collections have shrunk, and marketplaces have consolidated (X2Y2 closed in 2025). The opportunity set is now small and dominated by bots on the top collections.

## Edge source

**Structural** and **informational**. See [[edge-taxonomy]].

NFT markets have no unified order book — each marketplace (OpenSea, Blur, X2Y2, Magic Eden, Sudoswap) holds its own listings independently. No automatic arbitrage mechanism forces prices to converge; only human or automated searchers do. The structural source is marketplace fragmentation itself. The informational source is collection knowledge: recognising that a rare-trait NFT is mispriced requires domain expertise that most market participants lack.

## Why this edge exists

The counterparty is a seller who listed at below-clearing-price on a low-traffic marketplace, or a buyer who does not monitor all venues. Unlike fungible arb (CEX–CEX), no smart-contract mechanism auto-converges the prices. The edge decays as more bots scan all venues, but trait knowledge remains a slower-decaying informational edge. Wash trading artificially inflates reported volume, and the buyer of a wash-traded NFT at "floor" pays the real floor — below the manipulated nominal price.

## Null hypothesis

Under efficient markets, cross-marketplace price differences would reflect only gas and royalty costs. Any observed surplus above those costs would be transient noise, and no systematic edge would persist across collection cycles. If true, the distribution of cross-marketplace spreads would be centered on (fees + gas), with no fat tail of exploitable gaps.

## Overview

NFT arbitrage exploits price differences for the same non-fungible tokens across different marketplaces. Unlike fungible tokens (where 1 ETH = 1 ETH regardless of venue), each NFT is unique, creating a fragmented and inefficient market where the same collection -- or even the same individual token -- can be listed at significantly different prices on OpenSea, Blur, X2Y2, Magic Eden, and other platforms. The arbitrageur identifies these discrepancies, buys on the cheaper marketplace, and lists or sells on the more expensive one.

Beyond simple cross-marketplace arb, more sophisticated variants include trait-based arbitrage (buying NFTs with rare traits that are priced at or near the collection floor), wrapped/fractionalized NFT arbitrage (exploiting the gap between NFTX or Sudoswap vault token prices and whole NFT prices), and collection-level statistical arb (identifying collections that are underpriced relative to comparable projects). However, NFT arbitrage is significantly riskier than fungible token arbitrage due to illiquidity, high marketplace fees, wash trading that distorts reported prices, and the risk of rug pulls or abandoned projects.

## How It Works

**Cross-marketplace arbitrage:**
1. Monitor floor prices and listings across all major marketplaces in real time via aggregators (Gem, Blur) or custom bots.
2. When the same NFT or comparable floor NFT is listed cheaper on Marketplace A than the floor/best offer on Marketplace B, buy on A and sell on B.

**Trait-based arbitrage:**
1. Analyze rarity scores and trait distributions (using Rarity Sniper or custom scripts).
2. Identify NFTs with rare/desirable traits listed at or near the collection floor price.
3. Buy the underpriced rare NFT and relist at a premium. Requires deep knowledge of which traits the community values.

**Wrapped/fractionalized NFT arbitrage:**
1. Protocols like NFTX and Sudoswap create fungible ERC-20 tokens backed by NFT vaults (e.g., one PUNK token = one redeemable CryptoPunk).
2. If the PUNK token trades below CryptoPunk floor, buy tokens, redeem a Punk, sell at floor. If above floor, deposit a Punk into the vault and sell the tokens.

## Entry/Exit Rules

### Entry
1. **Cross-marketplace:** Buy when the price difference exceeds total fees (marketplace fee + royalty + gas). Thresholds: > 5% for low-floor, > 3% for high-floor collections.
2. **Trait-based:** Buy when a rare-trait NFT is listed within 10% of floor, while comparable rare traits have sold for 2-5x floor recently.
3. **Wrapped arb:** Execute when the redemption value of the vault token differs from the floor price by more than the gas cost + vault fee.
4. **Speed of execution:** Use bots or aggregators. Manual execution is too slow for cross-marketplace arb on popular collections.

### Exit
1. **Immediate resale:** For cross-marketplace arb, list the NFT on the target marketplace immediately after purchase. Accept best offer if one exists above your cost basis.
2. **Trait premium realization:** For trait-based arb, list at a premium and wait for a buyer. This may take days to weeks -- it is a slower arb.
3. **Price reduction:** If the NFT does not sell within 48-72 hours, incrementally reduce the price. Holding illiquid NFTs exposes you to collection-wide price declines.
4. **Stop loss:** If the collection floor drops below your purchase price, evaluate whether to hold (if the trait premium still exists) or cut losses immediately.

### Position sizing

- No single NFT position above **5% of strategy capital**, and no single collection above **20%**.
- Total aged inventory (held more than 72h) capped at **30% of capital**. Above that, stop buying and clear existing inventory first.
- Size cross-marketplace buys to the *visible bid* on the exit venue, not to the floor. A floor without a bid is not an exit.

## Implementation pseudocode

```python
def scan_cross_marketplace(collection, venues, gas_eth):
    """Buy-now / sell-into-bid arbitrage. Only crosses when an executable bid exists."""
    best_ask = min(v.lowest_listing(collection) for v in venues)       # cheapest buyable item
    best_bid = max(v.best_collection_bid(collection) for v in venues)  # executable exit
    if best_bid.venue == best_ask.venue:
        return None
    cost = (best_ask.price * (1 + best_ask.venue.fee)
            + 2 * gas_eth)
    proceeds = best_bid.price * (1 - best_bid.venue.fee - collection.royalty_enforced(best_bid.venue))
    edge = proceeds - cost
    if edge / cost < MIN_NET_EDGE:            # e.g. 1.5% net after all costs
        return None
    if wash_trade_score(collection) > WASH_LIMIT or bid_depth(best_bid) < 1:
        return None
    return Trade(buy=best_ask, sell=best_bid, expected_net=edge)

def scan_vault_gap(collection, vault):
    """NFTX/Sudoswap-style: vault token vs whole-NFT floor."""
    redeem_value = vault.token_price() * vault.tokens_per_nft() - vault.redeem_fee()
    gap = collection.floor_bid() - redeem_value
    if gap > gas_cost() + vault.redeem_fee() + MIN_NET_EDGE * redeem_value:
        return "buy tokens -> redeem NFT -> sell into floor bid"
    if -gap > gas_cost() + vault.mint_fee() + MIN_NET_EDGE * redeem_value:
        return "buy floor NFT -> deposit -> sell tokens"
    return None

def manage_inventory(position, now):
    if now - position.bought_at > hours(72):
        position.reprice(step=-0.03)          # step down 3% per review
    if position.collection.floor_change_since(position.bought_at) < -0.30:
        position.market_exit()                # trade-level kill
```

## Example Trade

**Cross-marketplace arb:**
1. **Detect:** A Bored Ape Yacht Club (BAYC) NFT is listed on X2Y2 at 28.5 ETH. The floor on Blur is 31.0 ETH with active bids at 30.2 ETH.
2. **Buy on X2Y2** at 28.5 ETH. Gas cost: 0.02 ETH. X2Y2 fee: 0.5% = 0.14 ETH.
3. **Sell on Blur** by accepting the best bid at 30.2 ETH. Blur marketplace fee: 0.5% = 0.15 ETH. Creator royalty: 2.5% = 0.76 ETH.
4. **Gross revenue:** 30.2 ETH.
5. **Total costs:** 28.5 (purchase) + 0.02 (gas buy) + 0.14 (X2Y2 fee) + 0.02 (gas sell) + 0.15 (Blur fee) + 0.76 (royalty) = 29.59 ETH.
6. **Net profit:** 30.2 - 29.59 = **0.61 ETH** (~$2,074 at ETH = $3,400).
7. **Duration:** ~3 minutes from detection to completion.

*Review note (2026-10-17):* this example is historical. X2Y2 shut down its trading platform effective **April 30, 2025** ([[x2y2]]), so the X2Y2 leg can no longer be traded. It also charges Blur a 0.5% marketplace fee, while most of the wiki describes Blur as zero-fee. See Contradictions. Repricing the sell leg at 0% Blur fee raises net profit by ~0.15 ETH to ~0.76 ETH.

**Trait-based arb:**
1. A BAYC with the rare "Gold Fur" trait (only 46 exist) is listed at 32 ETH (near the 31 ETH collection floor).
2. Previous Gold Fur sales averaged 55-65 ETH in the past 60 days.
3. **Buy at 32 ETH.** List at 52 ETH (conservative estimate, below recent comparables).
4. **Sells after 5 days** at 48 ETH (buyer negotiated down).
5. **Net profit after fees:** 48 - 32 - fees (~2.5 ETH) = **~13.5 ETH**.

## Performance characteristics

- **Backtest status: untested.** No AlgoBrain backtest exists. The frontmatter's `expected_sharpe: 0.8` and `expected_max_drawdown: 0.50` are priors, not measurements.
- **Cost overlay.** Round-trip costs run 5-15% for marketplace-listed exits (fees + royalties + gas). Selling into a zero-fee venue's collection bid with minimal royalty brings this down to ~1-3%. The 2-3% net per-trade edge in the worked example therefore only exists on the low-cost path. Any trade that relies on relisting at a premium has to clear the high-cost path.
- **Return shape.** Many small cross-marketplace wins are punctuated by inventory losses when a collection reprices down while items are held. Trait arb has a much lower hit rate and a longer holding period, and its P&L is dominated by a few large wins.
- **Regime dependence.** Opportunity density tracks speculative NFT flow. When NFT volume is weak, spreads persist but there are no bids to sell into. The constraint becomes exit liquidity, not spread detection.

## Capacity limits

Cross-marketplace NFT arb is self-limiting: the universe of active, liquid collections with meaningful floor-price volume is small (typically 10–30 collections at any given time). Bot-driven arbs are already saturated for the top collections. Practical capacity for a human-and-bot operation is $1M–$10M deployed capital. Beyond that, holding large inventory concentrates illiquidity risk and the trader becomes the market.

## What kills this strategy

1. **Collection collapse** — NFT collections can lose 80–95% of floor value in weeks; held inventory becomes worthless.
2. **Marketplace consolidation** — if one marketplace (Blur) dominates flow, price gaps narrow across the board.
3. **Royalty enforcement changes** — platforms toggling royalty enforcement change the cost structure of round-trips overnight.
4. **Gas spikes** — Ethereum congestion during a mint or cascade can make small arbs unprofitable ($50+ gas on a $100 spread).
5. **Wash trading convergence** — if the apparent "floor" is a wash-traded ceiling, buying at that price leaves no real buyer above.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Collection floor drops > 30% while holding inventory
- NFT held > 7 days without a bid within 10% of ask (trait arb)
- Combined fees + royalties > 80% of gross spread on any cross-marketplace trade

The three rules above are *trade-level* stops. **Strategy-level retirement criteria** (added 2026-10-17, see [[when-to-retire-a-strategy]]):
- Rolling 90-day net P&L after all fees, royalties and gas < 0.
- Strategy drawdown > 25% of allocated capital, measured mark-to-floor-bid, not mark-to-floor-ask.
- Median net edge per completed cross-marketplace trade < 1% over the last 50 trades. Bots have closed the gap.
- More than 30% of capital sitting in inventory aged above 14 days for two consecutive monthly reviews. Exit liquidity is gone.
- Fewer than 5 collections clearing the liquidity screen (independent bid depth, wash-trading filter) for a full quarter.

## Risk Management

- **Illiquidity risk:** The greatest risk -- NFTs may not sell for days or weeks. Never arb more than you can afford to hold.
- **Fees eat profits:** Combined marketplace fees (0.5-2.5%) and royalties (0-10%) can consume the spread. Calculate net profit before executing.
- **[[wash-trading]] distorts prices:** Reported volumes are inflated. Verify real buyer diversity before relying on price data.
- **Rug pull and smart contract risk:** Smaller collections may be abandoned; marketplace contracts carry exploit risk.
- **Gas and royalty volatility:** Gas spikes make small arbs unprofitable; royalty enforcement policies differ across platforms.

## Advantages
- **Fragmented market creates persistent opportunities** -- unlike fungible token markets, NFT marketplaces do not share order books
- **Trait-based arb rewards knowledge over speed** -- deep collection expertise is a durable edge over bot-driven strategies
- **Low capital requirement** -- many collections have floor prices under 1 ETH; wrapped NFT arb via vault tokens is quasi-fungible and more calculable

## Disadvantages
- **Extreme illiquidity** -- NFTs are the least liquid asset class in crypto; exit is never guaranteed
- **High total fees** -- marketplace fees + royalties + gas can total 5-15% per round trip
- **Collection and [[wash-trading]] risk** -- collections can lose 90%+ of value, and wash trading distorts reported prices
- **Declining market** -- overall NFT volume has declined significantly from 2021-2022 peaks, reducing the opportunity set

## Real-World Examples
- **Blur vs. OpenSea price war (2023):** Blur launched with zero fees and optional royalties, creating price discrepancies with OpenSea (which enforced royalties). Arbers bought cheaper on Blur and sold on OpenSea.
- **NFTX vault arbitrage:** CryptoPunk vault tokens periodically traded at 3-5% discounts to the Punk floor price. Traders bought tokens, redeemed Punks, and sold at floor for profit.
- **Sudoswap AMM arb:** Sudoswap's bonding curve model creates predictable pricing. When marketplace floors diverge from pool prices, arb bots buy from the cheaper source.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/nfts/overview` — NFT market overview
- `GET /api/v1/nfts/collections` — collection list
- `GET /api/v1/nfts/volume` — volume data
- `GET /api/v1/nfts/correlations` — collection correlations

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/nfts/overview"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-nft]].

**Live dashboards:** [NFT trends](https://cryptodataapi.com/nft-trends) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can use this data to scope the trade:

- **Universe** — `GET /api/v1/nfts/collections` + `GET /api/v1/nfts/volume` rank which collections still carry enough volume for a realistic exit; illiquidity is this strategy's main killer, so screen out anything thinly traded before hunting spreads.
- **Signal context** — `GET /api/v1/nfts/overview` and `GET /api/v1/nfts/correlations` frame market-wide direction and which collections move together (a correlated pair is a hedge candidate for floor-vs-vault trades). Per-listing marketplace spreads themselves come from marketplace APIs, not CryptoDataAPI.
- **Regime gate** — `GET /api/v1/meme/regime/score` (market-wide speculative-hype 0-100) is the closest proxy for NFT risk appetite; NFT spreads are only worth crossing 5-15% round-trip fees when speculative flow is active. `GET /api/v1/regimes/current` adds the cycle-level check.
- **Backtest** — no NFT archive exists in `/api/v1/backtesting/*`; to build history, poll `/api/v1/nfts/volume` and store it yourself, and use `GET /api/v1/backtesting/daily-snapshots` (full payload since 2026-03-02) for point-in-time market context around stored NFT observations.
- **Tips** — append `?format=markdown` for cleaner context; treat reported collection volume as wash-trading-suspect ([[wash-trading]]) and require independent bid depth before sizing.
- **History correction (2026-10-17)** — there is still no `/backtesting/*` NFT archive, but daily NFT history is available. `GET /api/v1/nfts/collections/{slug}?days=3650` returns a per-collection daily volume series, and `GET /api/v1/nfts/volume?by=collection&from=2024-01-01&to=2025-01-01` returns a dated window (Pro). Use them to rebuild the liquidity screen historically before polling. Neither gives listing-level spreads.

## Contradictions

> **Claim A** (Source: [[nft-trading]], and the worked example on this page, confidence: LOW): Blur charges a ~0.5% marketplace fee.
> **Claim B** (Source: [[blur]], [[gem-nft]], [[looksrare]], [[exchanges-overview]], [[vampire-attack-arbitrage]], confidence: MEDIUM): Blur launched with, and is described as having, zero marketplace fees. Only the creator royalty applies (a minimum royalty was enforced post-royalty-war).
> **Resolution**: Claim B is favoured by more pages. The 0.5% may be a misattributed royalty minimum. Pending a check of Blur's current fee schedule.

> **Claim A** (Source: [[2026-04-22-gap-finder-nft-trading]], confidence: LOW): X2Y2 trading platform shutdown "April 30 2026".
> **Claim B** (Source: [[x2y2]], confidence: MEDIUM): shutdown announced March 31, 2025, effective **April 30, 2025**.
> **Resolution**: Claim B is favoured because it carries the dated announcement (March 31, 2025) and the team's stated reason (a ~90% volume decline). The source summary's "2026" is probably a year typo. Either way, X2Y2 is not a live venue as of 2026-10-17.

## See Also
- [[nft-trading]] and [[nft]] -- foundational knowledge about NFT technology and trading
- [[cross-exchange-arbitrage]] -- the fungible token equivalent of marketplace arbitrage
- [[decentralized-exchanges]] -- the DEX infrastructure that powers NFT marketplaces
- [[wash-trading]] -- a major risk factor that distorts NFT price data

## Sources

- (Source: [[2026-04-22-gap-finder-nft-trading]]) — NFT marketplace landscape summary, including the X2Y2 closure (year disputed; see Contradictions).
- Marketplace and venue facts are cross-referenced from the [[x2y2]], [[blur]], [[nftx]], [[sudoswap]] and [[gem-nft]] entity pages.
- Fee, royalty and example-trade figures are illustrative and unverified against a dated fee schedule.

## Related

- [[nft-trading]] — directional NFT trading and its cost model
- [[vampire-attack-arbitrage]] — Blur's 2022-23 points campaign, the incentive war that reshaped NFT fees and royalties
- [[gaming-gamefi-basket]] / [[gamefi]] — the in-game NFT layer
- [[cryptodataapi-nft]] — NFT endpoints
- [[when-to-retire-a-strategy]] / [[failure-modes]] — retirement and failure framework
