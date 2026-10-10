# Storage resource selection

Checked on 2026-10-10. All builds, uploads, provider payments and Android runtime integrations remain NOT_RUN.

## Start with the product's storage requirements

Android file selection and sharing are distinct from remote persistence. Use current Android SAF/MediaStore/FileProvider guidance for local file access. The archived android/storage-samples and google/modernstorage repositories are historical examples; pinning them does not make them current production dependencies.

For EdgeORE's owned-node IPFS approach: encrypt on the client, upload ciphertext through an authenticated backend, keep the IPFS administrative API private, explicitly pin content and verify retrieval plus restored plaintext before marking backup complete. CID, encryption, pinning and provider availability are separate evidence dimensions. These newly listed repos do not automatically implement that design.

## Provider distinctions

- Autonomi: the supplied maidsafe/autonomi repository is archived. Its README points to the WithAutonomi organization for current development. Do not treat its network/payment commands as current verified integration instructions. Root redistribution terms were not resolved in this inspection, so it remains a link.
- Filester: Android temporary cloud file-sharing reference. GPL-3.0 source is included separately; privacy claims are upstream descriptions, not audit findings. Adapt UI only under applicable license obligations and verify actual server/encryption behavior.
- ShadowDriveMobile: a Kotlin Android Shadow Drive example according to its repository metadata. No root license identified; reference only. A provider-specific storage account is not equivalent to an IPFS CID or generic vault.
- filestorage.js: a JavaScript SKALE client. It requires SKALE-specific endpoint/chain integration; it is not a Kotlin artifact and Solana MWA does not authorize its EVM operations. Source remains an LGPL-3.0 reference, not bundled into the Android app.
- hox: React/Solidity/Web3 hackathon prototype, not a Kotlin production backend. Unresolved license, reference only.
- cloud-file-storage: Kotlin project with Docker infrastructure. Minimal README does not establish authentication, quota enforcement, encryption or recovery guarantees. Unresolved license, reference only.
- LatihanKotlin: beginner Kotlin exercises. The README's cloud-storage title refers to practice material; do not advertise it as a functional cloud-storage provider. Unresolved license, reference only.

## Adoption gates

Review licenses, source age, supported targets and exact dependencies. Keep transport adapters behind a small interface for put/get/status/delete; avoid exposing provider-specific custody and contract operations as generic storage buttons. Persist jobs and acknowledgements, bound input/memory/network use, authenticate endpoints and test interrupted upload recovery, corruption, unavailable provider, quota exhaustion and key loss.

No automated storage payments or arbitrary provider SDKs are added by this catalog update. Existing EdgeORE local-vault and wallet code is unchanged.
