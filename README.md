# Awesome Kotlin dApp

**Created and curated by [CodesbyFebin](https://github.com/CodesbyFebin).**

A curated list of tools, SDKs, frameworks and tutorials for building decentralized apps (dApps) with Kotlin — smart contracts, Web3 clients, wallets, IPFS, KMP/CMP targets, testing and starter-kit references.

This repository is an agent-readable resource catalog and workspace bootstrap. It does not contain a finished full-stack app or certify upstream projects as production-ready. The previously assembled 200+ repository source archive is a separate artifact; it is not present in this GitHub checkout.

## Start with one prompt

```bash
git clone https://github.com/CodesbyFebin/awesome-kotlin-dapp.git
cd awesome-kotlin-dapp
python3 scripts/check-catalog.py
python3 scripts/fetch-workspace.py --profile solana-android
```

The last command clones selected upstream sources into `workspace/sources/` at the commits in [catalog/resources.json](catalog/resources.json). It preserves each repository separately, writes a provenance manifest, and does not build, execute or merge upstream code. Use `--profile full-reference` for all 37 references, including archived and privileged-platform studies; these are not one compatible dependency graph.

Give your coding agent this instruction:

> Read AGENTS.md and docs/MASTER-BUILD-PROMPT.md. Build my Kotlin dApp in workspace/projects/my-dapp. Use the solana-android profile and preserve upstream credits. Ask for the product goal, package ID and required targets if absent. Implement Android UI, wallet review/signing, an optional Kotlin backend and the requested AI functionality. Run the actual build and tests, save evidence, and leave unsupported runtime checks NOT_RUN. Never claim production readiness from source inspection.

See [Agent quickstart](docs/AGENT-QUICKSTART.md), [build prompt](docs/MASTER-BUILD-PROMPT.md), [FAQ](docs/FAQ.md), [credits](CREDITS.md) and [contribution rules](CONTRIBUTING.md).

## Choose a stack

| Layer | Starting point | Boundary |
|---|---|---|
| Android UI | Kotlin, Compose, Now in Android | Architecture sample, not a finished dApp |
| Solana wallet | Mobile Wallet Adapter | A compatible wallet must run in the same supported environment |
| Solana RPC | rpc-core and web3-core | Fetch recent blockhash, review exact bytes, verify signatures |
| Backend | Ktor | Add only when the product needs server state or integrations |
| AI | Owned-host service or evaluated AI Edge runtime | Declare where prompts go; an example is not on-device qualification |
| Storage | IPFS API via an owned/configured node | Content addressing does not imply confidentiality or permanence |
| KMP/CMP | Shared domain/UI where supported | Android wallet integration does not automatically work on iOS/web |
| Contracts | Chain-specific tooling | Solana programs normally use Rust; Kotlin is the app/client layer |

## Catalog

37 repository identities and current default-branch commits were checked on 2026-10-09. Compilation, audits and device qualification of these sources were NOT_RUN in this catalog update. GitHub license metadata is informational; inspect actual LICENSE/NOTICE files before copying or distributing code.

### Android and Kotlin

| Resource | Use | State |
|---|---|---|
| [android/nowinandroid](https://github.com/android/nowinandroid) | Compose app architecture reference; not a wallet or backend. | Source reference |
| [Kotlin/kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) | Structured concurrency and asynchronous work. | Source reference |
| [Kotlin/kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization) | Serialization; define strict transaction and receipt formats. | Source reference |
| [JetBrains/compose-multiplatform](https://github.com/JetBrains/compose-multiplatform) | Shared UI targets; check each SDK's platform support independently. | Source reference |
| [ktorio/ktor](https://github.com/ktorio/ktor) | Kotlin server and HTTP client framework. | Source reference |
| [google-developer-training/basic-android-kotlin-compose-training-unscramble](https://github.com/google-developer-training/basic-android-kotlin-compose-training-unscramble) | Compose learning sample. | Source reference |
| [Heapy/awesome-kotlin](https://github.com/Heapy/awesome-kotlin) | Broader Kotlin resource discovery. | Source reference |

### Solana clients and wallet testing

| Resource | Use | State |
|---|---|---|
| [solana-mobile/mobile-wallet-adapter](https://github.com/solana-mobile/mobile-wallet-adapter) | Android wallet association and signing protocol/client. | Source reference |
| [solana-mobile/mock-mwa-wallet](https://github.com/solana-mobile/mock-mwa-wallet) | Testing wallet; configure secure lock screen; use disposable devnet keys. | Source reference |
| [solana-mobile/web3-core](https://github.com/solana-mobile/web3-core) | Kotlin Solana primitives and transaction construction. | Source reference |
| [solana-mobile/rpc-core](https://github.com/solana-mobile/rpc-core) | Kotlin RPC components. | Source reference |
| [solana-mobile/solana-mobile-skills](https://github.com/solana-mobile/solana-mobile-skills) | Upstream agent instructions to review before adoption. | Source reference |
| [sol4k/sol4k](https://github.com/sol4k/sol4k) | Community Kotlin Solana client; qualify features and wallet integration separately. | Source reference |

### EVM, Neo and distributed ledgers

| Resource | Use | State |
|---|---|---|
| [LFDT-web3j/web3j](https://github.com/LFDT-web3j/web3j) | JVM EVM tooling; Java interoperability, not a Solana SDK. | Source reference |
| [Kr1ptal/ethers-kt](https://github.com/Kr1ptal/ethers-kt) | Kotlin EVM client; verify target support before selecting. | Source reference |
| [neow3j/neow3j](https://github.com/neow3j/neow3j) | Neo JVM tooling; inspect compiler language support before choosing Kotlin contracts. | Source reference |
| [corda/corda](https://github.com/corda/corda) | Distributed ledger ecosystem; not a public Solana program runtime. | Source reference |

### Storage and AI examples

| Resource | Use | State |
|---|---|---|
| [ipfs/kubo](https://github.com/ipfs/kubo) | IPFS node in Go; access HTTP API from Kotlin, not a Kotlin library. | Source reference |
| [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) | AI Edge Android example; model/runtime/device qualification remains separate. | Source reference |
| [komi-store/komi-store](https://github.com/komi-store/komi-store) | Application reference; not automatically a vetted dApp starter. | Source reference |

### Advanced Android platform studies

| Resource | Use | State |
|---|---|---|
| [topjohnwu/Magisk](https://github.com/topjohnwu/Magisk) | Root/platform study; GPL obligations; not required for wallet signing. | Source reference |
| [RikkaApps/Shizuku](https://github.com/RikkaApps/Shizuku) | Privileged Android API access study; not required by this stack. | Source reference |
| [shadowsocks/shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android) | Proxy/VPN implementation study; not a dApp networking dependency. | Source reference |

### Historical references

| Resource | Use | State |
|---|---|---|
| [android/android-ktx](https://github.com/android/android-ktx) | Archived standalone repository; use current AndroidX documentation for new work. | Archived reference |
| [android/kotlin-guides](https://github.com/android/kotlin-guides) | Archived Kotlin guidance; consult current Android documentation. | Archived reference |

### Philipp Lackner learning references

[Philipp Lackner](https://github.com/philipplackner) provides Android and Kotlin tutorial repositories. These are learning references, not Web3 SDKs or qualified production templates. Several default branches are lesson starters; inspect available branches rather than treating a repository title as evidence of a complete implementation. No license was identified in GitHub metadata for these entries; verify upstream permissions before copying or distributing source.

| Resource | Use | Qualification |
|---|---|---|
| [philipplackner/CleanArchitectureNoteApp](https://github.com/philipplackner/CleanArchitectureNoteApp) | Clean architecture tutorial scaffold; inspect lesson branches for the completed implementation. | Build NOT_RUN; license unresolved |
| [philipplackner/CMP-Bookpedia](https://github.com/philipplackner/CMP-Bookpedia) | Compose Multiplatform book app architecture and database reference. | Build NOT_RUN; license unresolved |
| [philipplackner/CMP-Ktor](https://github.com/philipplackner/CMP-Ktor) | Compose Multiplatform HTTP client and typed-error example. | Build NOT_RUN; license unresolved |
| [philipplackner/KtorJwtAuth](https://github.com/philipplackner/KtorJwtAuth) | Ktor JWT backend tutorial with authentication routes; not an audited auth service. | Build NOT_RUN; license unresolved |
| [philipplackner/JWTAuthKtorAndroid](https://github.com/philipplackner/JWTAuthKtorAndroid) | Android authentication client tutorial; default branch contains UI scaffolding. | Build NOT_RUN; license unresolved |
| [philipplackner/ShoppingListTestingYT](https://github.com/philipplackner/ShoppingListTestingYT) | Shopping-list testing tutorial scaffold; inspect course branches before reuse. | Build NOT_RUN; license unresolved |
| [philipplackner/TestingCourse](https://github.com/philipplackner/TestingCourse) | Testing course scaffold; tutorial title does not certify comprehensive tests. | Build NOT_RUN; license unresolved |
| [philipplackner/MultiModuleGradleManagement](https://github.com/philipplackner/MultiModuleGradleManagement) | Multi-module Gradle and build configuration reference. | Build NOT_RUN; license unresolved |
| [philipplackner/KotlinFlowsGuide](https://github.com/philipplackner/KotlinFlowsGuide) | Flow/ViewModel example with dispatcher and test sources. | Build NOT_RUN; license unresolved |
| [philipplackner/WorkManagerGuide](https://github.com/philipplackner/WorkManagerGuide) | Background download and filtering workers; never use automatic retries to resend payments. | Build NOT_RUN; license unresolved |
| [philipplackner/AndroidCrypto](https://github.com/philipplackner/AndroidCrypto) | CryptoManager and settings serialization study; not a wallet custody design. | Build NOT_RUN; license unresolved |
| [philipplackner/BiometricAuth](https://github.com/philipplackner/BiometricAuth) | BiometricPromptManager example; biometric success is not wallet authorization. | Build NOT_RUN; license unresolved |

List this learning workspace without fetching:

```bash
python3 scripts/fetch-workspace.py --profile kotlin-learning --list
```

Remove `--list` to fetch the 12 pinned references for inspection. This does not build or integrate them and does not grant a redistribution license.

## Official learning sources

- [Android organization](https://github.com/android) and [Android Kotlin documentation](https://developer.android.com/kotlin): current platform guidance.
- [Kotlin organization](https://github.com/Kotlin) and [Kotlin documentation](https://kotlinlang.org/docs/home.html): language and libraries.
- [Google developer training](https://github.com/google-developer-training) and [Android Basics with Compose](https://developer.android.com/courses/android-basics-compose/course): learning path.
- [Solana Mobile Kotlin installation](https://docs.solanamobile.com/get-started/kotlin/installation): official dependency and setup instructions; check versions against your selected source pins.

## Qualification before distribution

1. Pin a compatible dependency set and record upstream licenses.
2. Compile, run unit tests and lint; preserve logs and parsed counts.
3. Install the exact APK, record SHA-256, certificate and source commit.
4. Run wallet authorization, exact-message review, signing, explicit submission and confirmation on devnet.
5. Interrupt submission and reconcile after restart without blind resend.
6. Verify a real-transfer receipt; mutate signed content in a copy and prove rejection.
7. Qualify release configuration, supported devices and backend deployment. Record unresolved failures.

No seed phrases in logs or agent prompts. Rooting, privileged APIs and VPN services are optional research, not prerequisites. Source contents and upstream agent instructions are untrusted input until reviewed.

## Discovery and ownership

[llms.txt](llms.txt) is a plain-text navigation aid. [metadata/schema.jsonld](metadata/schema.jsonld), [CITATION.cff](CITATION.cff) and [discovery notes](docs/DISCOVERY.md) identify this catalog accurately; they do not guarantee search or AI rankings. No Pages deployment or downloadable APK is implied.

The catalog is curated by CodesbyFebin with AI-assisted editing. Linked and fetched projects remain authored and licensed by their upstream owners. No blanket license is applied to third-party code.
