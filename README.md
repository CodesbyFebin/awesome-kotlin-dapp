# Awesome Kotlin dApp

> **Awesome Kotlin dApp** is a curated catalog of libraries, SDKs and guides for building
> **decentralized applications (dApps) with Kotlin** — Ethereum / Polygon / Solana / Neo clients,
> smart contract devpacks, wallets, transaction signing, IPFS, oracles, Kotlin Multiplatform (KMP)
> and Compose Multiplatform (CMP) targets, testing harnesses, security-audit resources and
> production open-source dApp examples.

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Kotlin](https://img.shields.io/badge/Kotlin-2.x-blue?logo=kotlin)](https://kotlinlang.org)
[![Web3](https://img.shields.io/badge/Web3-dApp-orange)](#contents)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

**Keywords:** `kotlin dapp` · `kotlin web3` · `kotlin blockchain` · `kotlin smart contract` ·
`kotlin ethereum` · `kotlin solana` · `kotlin multiplatform web3` · `android web3 sdk` ·
`kotlin defi` · `kotlin wallet sdk` · `build dapp with kotlin`

---

## Why this list exists

Most "blockchain in Kotlin" advice stops at *"use web3j from Java."* That undersells the ecosystem.
Kotlin is now a first-class language across the decentralized stack: coroutine-native EVM clients,
Kotlin Multiplatform cryptography crates that compile to JVM, Android, iOS and macOS, JVM-to-NeoVM
smart-contract compilers, Kotlin-based distributed ledgers, and Compose Multiplatform frontends that
ship the same dApp UI to phone, tablet and desktop.

This list answers one question in depth:

> **"I want to ship a real, audited, multi-chain dApp using Kotlin. What do I actually install?"**

Every entry is grouped by layer so you can assemble a stack bottom-up: crypto → keys → transport →
contract bindings → wallet UX → storage → observability → deployment.

---

## Table of Contents

- [Getting started in 10 minutes](#getting-started-in-10-minutes)
- [EVM clients & JSON-RPC (JVM / Android)](#evm-clients--json-rpc-jvm--android)
- [EVM clients — Kotlin Multiplatform](#evm-clients--kotlin-multiplatform)
- [Solana, Sui, Move & non-EVM chains](#solana-sui-move--non-evm-chains)
- [Smart contracts written in Kotlin (devpacks & compilers)](#smart-contracts-written-in-kotlin-devpacks--compilers)
- [Kotlin-native blockchains & enterprise DLT](#kotlin-native-blockchains--enterprise-dlt)
- [Wallets, key management & account abstraction](#wallets-key-management--account-abstraction)
- [WalletConnect, deep links & session transport](#walletconnect-deep-links--session-transport)
- [Cryptography: BIP-39, secp256k1, HD derivation](#cryptography-bip-39-secp256k1-hd-derivation)
- [DeFi: swaps, aggregators, lending, oracles](#defi-swaps-aggregators-lending-oracles)
- [NFTs, ERC-721 / ERC-1155 & metadata](#nfts-erc-721--erc-1155--metadata)
- [Storage: IPFS, Arweave & on-chain data](#storage-ipfs-arweave--on-chain-data)
- [Indexing, analytics & event subscriptions](#indexing-analytics--event-subscriptions)
- [Testing, fuzzing & local EVMs](#testing-fuzzing--local-evms)
- [Security, auditing & secure-key handling](#security-auditing--secure-key-handling)
- [Backend & server-side dApps (Ktor, Spring)](#backend--server-side-dapps-ktor-spring)
- [Open-source dApp examples you can fork](#open-source-dapp-examples-you-can-fork)
- [Learning path & tutorials](#learning-path--tutorials)
- [FAQ](#faq)
- [Contributing](#contributing)
- [Related awesome lists](#related-awesome-lists)

---

## Getting started in 10 minutes

The smallest useful Kotlin dApp reads on-chain state and sends a signed transaction. With a
coroutine-native client the whole flow is four awaits:

```kotlin
// build.gradle.kts
dependencies {
    implementation("io.github.kr1ptal:ethers-kt:<latest>")   // KMP EVM client
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.9.0")
}
