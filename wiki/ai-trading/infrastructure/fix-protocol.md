---
title: FIX Protocol
type: concept
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [infrastructure, protocol]
related: ["[[order-management-systems]]", "[[low-latency-trading]]", "[[co-location]]"]
---

# FIX Protocol

The Financial Information eXchange (FIX) protocol is the industry-standard messaging format for electronic trading. Virtually every major exchange, broker, and institutional trading system speaks FIX. It is the TCP/IP of financial markets.

## Overview

FIX is a tag-value messaging protocol designed for order routing, execution reporting, and market data distribution. A typical FIX message looks like:

```
8=FIX.4.4|9=176|35=D|49=SENDER|56=TARGET|34=12|52=20260406-14:30:00|
11=ORDER123|21=1|55=AAPL|54=1|38=100|40=2|44=150.00|59=0|10=128|
```

Each field is a numbered tag with a value. Tag 35 defines the message type, and everything else provides the details.

## Key Message Types (Tag 35)

| Tag 35 Value | Message Type | Description |
|-------------|--------------|-------------|
| 0 | Heartbeat | Keep-alive between sessions |
| A | Logon | Initiate FIX session |
| D | New Order Single | Submit a new order |
| F | Order Cancel Request | Request to cancel an open order |
| G | Order Cancel/Replace | Modify an existing order |
| 8 | Execution Report | Fill, partial fill, reject, cancel confirmation |
| X | Market Data Incremental | Real-time market data updates |

## Protocol Layers

**Session layer**: Manages connection lifecycle — logon, logout, heartbeats, sequence number tracking, message recovery after disconnection. Ensures reliable, ordered message delivery.

**Application layer**: Carries the actual trading messages — orders, executions, market data. Built on top of the session layer's reliability guarantees.

## Versions

- **FIX 4.2**: Still widely used, especially in equities. Simple and well-understood.
- **FIX 4.4**: Added support for more complex order types and multi-leg instruments.
- **FIX 5.0 / FIXT 1.1**: Separated transport from application layer. Supports different transports including XML-based FIXML.

Most production systems still run FIX 4.2 or 4.4. Version 5.0 adoption has been slow.

## Libraries and Implementations

| Library | Language | Notes |
|---------|----------|-------|
| QuickFIX | C++, Python, Java, .NET | Most popular open-source FIX engine |
| QuickFIX/J | Java | Java-native implementation |
| FIX8 | C++ | High-performance alternative |
| fix-rs | Rust | Modern, memory-safe implementation |

## FIX in Practice

A typical institutional order flow through FIX:

1. Trader sends **New Order Single** (35=D) with symbol, side, quantity, price, order type
2. Exchange acknowledges with **Execution Report** (35=8, OrdStatus=0 "New")
3. When filled, exchange sends **Execution Report** (35=8, OrdStatus=2 "Filled")
4. [[order-management-systems]] log every message for audit and compliance

## Crypto Doesn't Use FIX

Cryptocurrency exchanges almost universally use **REST APIs** for order management and **WebSocket** connections for real-time market data. This is one reason traditional finance engineers find crypto infrastructure foreign — and vice versa.

## See Also

- [[order-management-systems]] — systems built on top of FIX
- [[low-latency-trading]] — optimizing FIX message processing
- [[co-location]] — where FIX sessions physically connect
