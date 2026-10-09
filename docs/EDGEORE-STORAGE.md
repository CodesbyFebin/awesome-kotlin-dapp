# EdgeORE storage integration assessment

Status: design/reference only. No EdgeORE app files changed. Android NDK builds, JNI, remote uploads and storage payments NOT_RUN.

## Inspected source identity

- EdgeORE main: 2442ba1972def86a342e0e61a8fc456e769c6a98.
- Sia-Android develop: 797422781cf3b4d523db8b8f4af6f88e1b6b919c.
- self_encryption master: eb95108a6eb8f1012ff2499c1cbb830aed8392a8; Cargo package version 0.36.1.

## Findings

Sia-Android is a client for Sia node wallet/renter functions. It is not an existing EdgeORE backend. Its LICENSE.md explicitly reserves modification and redistribution rights to the author. Keep it as a credited reference only; obtaining author permission is required before adapting its code. Its inspected Android build targets SDK 28 and uses old Kotlin Android extensions and dependencies, so it is not a drop-in modern Compose component.

self_encryption is dual MIT/Apache-2.0. The current Rust library exposes content encryption, chunk/data-map structures and streaming APIs. Storage transport is outside its scope: no Sia contracts, Solana payment flow, provider availability or upload service is supplied by this crate. A cdylib crate type does not imply a ready JNI API.

Its README is stale relative to the pinned implementation: it describes older hashing/cipher choices and a larger minimum input size, while current source uses BLAKE3, a chacha20poly1305 dependency, a minimum input of three bytes, and different public/private decrypt entry points. Inspect cipher/stream modules and compile against actual exported APIs; do not copy README samples as verified code.

## Recommended architecture

Keep Kotlin/Compose for UI, Storage Access Framework file selection, bounded file I/O, persistent job state and progress. Keep the existing EOV2 Android Keystore AES-GCM vault intact. Add remote backup behind an explicit feature flag and a provider interface; keep encryption separate from provider transport and payments.

An optional Rust bridge should accept bounded streams or file descriptors and return encrypted chunks plus a versioned data map. It needs explicit ownership/freeing rules, bounded serialized metadata, cancellation, checked lengths and no panics crossing JNI. Do not pass entire large files as repeated Kotlin/Rust byte-array copies.

For private backup, prefer randomized authenticated encryption before any deduplicating content pipeline. Convergent encryption creates content-dependent identifiers and warrants analysis of equality leakage and guessed-content attacks; obfuscation is not a blanket security guarantee. A random outer envelope sacrifices plaintext-based deduplication intentionally. Protect the data map as secret recovery material, encrypted locally under Keystore, with a separately designed user-controlled export/recovery option. Never upload an unprotected map alongside chunks.

Upload only ciphertext through an authenticated backend. Verify stored chunk hashes, lengths and successful retrieval before marking a backup complete. Persist manifests and upload jobs atomically, bound retries and retain unresolved outcomes. Remote deletion should report provider acknowledgement separately from physical-erasure claims.

Sia has its own contracts, wallet and payment model. Solana MWA approval does not authorize Siacoin spending. Decide separately whether the owner-operated server funds Sia storage or the user controls a Sia wallet; do not silently introduce custodial funds or automatic contract renewal. Solana receipts may attest app records, not prove provider durability.

## Qualification order

1. Review selected release/commit and licenses; freeze compatible versions and a dependency lock.
2. Run Rust round-trip, small-input, corrupted/truncated/swapped chunk, invalid map, quota, cancellation and large-file memory tests.
3. Build an explicit JNI wrapper for arm64-v8a and x86_64 using pinned Rust, cargo-ndk and NDK. Add other ABIs only when supported and tested.
4. Test JNI error containment, native-library loading, lifecycle interruption, disk-full handling and Keystore behavior on Android.
5. Exercise a provider upload/download with owned-host authentication, interruptions and durable restart recovery. Verify restored bytes against the original.
6. Qualify provider contract/payment review, revocation, backup recovery, key loss, and receipt boundaries. Never mark these gates passed from source inspection.

Until these gates execute, UI should say remote encrypted storage is planned/unavailable. Do not replace the working local vault, publish an extremely-secure claim, or promise that an NDK compile alone produces decentralized storage.
