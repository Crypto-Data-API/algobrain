---
title: Cloud Trading Infrastructure
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [infrastructure, cloud]
related: ["[[low-latency-trading]]", "[[co-location]]", "[[order-management-systems]]", "[[backtesting]]"]
---

# Cloud Trading Infrastructure

Cloud platforms (AWS, GCP, Azure) have made serious trading infrastructure accessible to individual traders and small funds. What once required a data center and a six-figure hardware budget can now run for a few hundred dollars a month.

## Cloud vs On-Premise

| Factor | Cloud | On-Premise |
|--------|-------|------------|
| Latency | 1-50ms to exchanges | Sub-microsecond (co-located) |
| Scalability | Spin up 100 GPUs in minutes | Buy and rack hardware |
| Maintenance | Provider handles hardware | You handle everything |
| Cost model | Pay-per-use, OpEx | Large upfront CapEx |
| Global deployment | Any region in minutes | Build/lease in each location |
| Data security | Shared infrastructure | Full physical control |

**Use cloud for**: Strategy research, [[backtesting]], paper trading, ML model training, swing/position trading execution, data pipelines, monitoring dashboards.

**Use on-premise for**: [[low-latency-trading]], [[co-location]] setups, regulatory requirements mandating data residency, strategies where cloud latency is the bottleneck.

## AWS Architecture for Trading

AWS is the most popular cloud for trading systems. A typical setup:

- **EC2**: Compute instances for running strategies. Use c-series (compute-optimized) for backtesting, p-series (GPU) for ML training
- **S3**: Object storage for historical market data, backtest results, model artifacts
- **Lambda**: Event-driven functions for alerts, webhook processing, scheduled data pulls
- **SageMaker**: Managed ML platform for training and deploying [[ml-models]]
- **RDS/DynamoDB**: Databases for trade logs, position tracking, signal storage
- **CloudWatch**: Monitoring, alerting, log aggregation

## Cost Estimates for Retail

| Setup Level | Monthly Cost | What You Get |
|------------|-------------|--------------|
| Basic | $50-100 | Small EC2 instance, S3 storage, basic data pipeline |
| Intermediate | $100-300 | Larger compute, GPU for ML training, multiple data feeds |
| Serious | $300-500 | Multi-instance setup, dedicated databases, monitoring |
| Small fund | $500-2000 | High-availability, redundancy, multiple strategies |

## Deployment Best Practices

**Docker containers**: Package your strategy and all dependencies into a container. Ensures identical behavior across development, testing, and production environments.

**Kubernetes**: Orchestrate multiple containers for complex multi-strategy setups. Auto-restart failed components. Scale compute up/down based on market hours.

**Infrastructure as Code**: Use Terraform or CloudFormation to define your entire infrastructure. Reproducible deployments, version-controlled configuration.

**Secrets management**: Never hardcode API keys. Use AWS Secrets Manager, environment variables, or HashiCorp Vault. A leaked exchange API key with withdrawal permissions is catastrophic.

## Region Selection

Place your cloud instances close to the exchanges or data sources you trade:

- **us-east-1 (Virginia)**: Closest to NYSE/NASDAQ data centers in New Jersey
- **us-east-2 (Ohio)**: Near CME in Chicago
- **eu-west-2 (London)**: For European exchanges
- **ap-northeast-1 (Tokyo)**: For Asian markets

## See Also

- [[low-latency-trading]] — when cloud isn't fast enough
- [[co-location]] — the on-premise extreme
- [[ai-trading-agents]] — agent systems that run on cloud infrastructure
