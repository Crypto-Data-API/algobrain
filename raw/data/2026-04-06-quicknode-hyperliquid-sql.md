<!-- Source: QuickNode SQL Explorer API — Hyperliquid queries -->
<!-- Downloaded: 2026-04-06 via API calls -->
<!-- API Endpoint: POST https://api.quicknode.com/sql/rest/v1/query -->
<!-- Cluster: hyperliquid-core-mainnet -->

# QuickNode Hyperliquid SQL Explorer — Raw Data

## Queries Executed

1. Platform daily overview (30 days): hyperliquid_metrics_overview
2. Volume by coin (24h): hyperliquid_trades aggregated
3. Market contexts (funding, OI, prices): hyperliquid_perpetual_market_contexts
4. Whale trades >$100K (24h): hyperliquid_trades filtered
5. Hourly liquidation stats: hyperliquid_liquidations_hourly
6. Funding rate summary (24h): hyperliquid_funding_summary_hourly
7. Perpetual markets list: hyperliquid_perpetual_markets (229 markets)
8. Top traders by volume (24h): hyperliquid_trades aggregated by address

## Data Source

API documentation: https://www.quicknode.com/docs/sql-explorer/hyperliquid-queries

29 available tables:
- hyperliquid_trades, hyperliquid_dex_trades, hyperliquid_fills, hyperliquid_orders
- hyperliquid_funding, hyperliquid_blocks, hyperliquid_transactions
- hyperliquid_asset_transfers, hyperliquid_ledger_updates, hyperliquid_bridge
- hyperliquid_perpetual_markets, hyperliquid_spot_markets
- hyperliquid_perpetual_market_contexts, hyperliquid_oracle_prices
- hyperliquid_clearinghouse_states, hyperliquid_spot_clearinghouse_states
- hyperliquid_vault_equities, hyperliquid_sub_accounts, hyperliquid_agents
- hyperliquid_display_names, hyperliquid_delegator_rewards
- hyperliquid_builder_transactions, hyperliquid_builder_labels, hyperliquid_builder_fills
- hyperliquid_funding_summary_hourly, hyperliquid_liquidations_hourly
- hyperliquid_market_volume_hourly, hyperliquid_metrics_dex_overview
- hyperliquid_metrics_overview
