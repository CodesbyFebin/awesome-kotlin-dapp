# Agent quickstart

Clone this repository, then read AGENTS.md. Run `python3 scripts/check-catalog.py` and `python3 scripts/fetch-workspace.py --profile solana-android`.

The sources are material for an agent to inspect, not a pre-integrated Gradle project. The fetcher requires Python 3 and Git with network access. It refuses existing destinations rather than overwriting them. Its manifest records upstream commits; it does not check out secrets or run build scripts.

Choose a product goal and package ID. Paste docs/MASTER-BUILD-PROMPT.md into your coding agent with those values. The agent creates workspace/projects/<name>, selects compatible dependencies, implements the product and records actual gates. SDK installs, wallet approvals and release credentials stay with the owner.

Profiles: solana-android selects Android architecture, Kotlin concurrency/serialization, Solana SDK and wallet-testing sources, Ktor and reviewed skill references. full-reference fetches every catalog entry, including archived and privileged-platform references; it is research material only.

To update pins, verify upstream repository metadata and commit, then change the catalog in review. Never float every dependency to latest in one automated sweep.

For Philipp Lackner's Kotlin/Android tutorials, use `python3 scripts/fetch-workspace.py --profile kotlin-learning --list` to inspect the 12 selected pins, then omit `--list` to fetch. Verify upstream terms before reuse: license metadata is unresolved. Some default branches are course starters; inspect lesson branches explicitly. These sources do not implement Solana wallet integration.
