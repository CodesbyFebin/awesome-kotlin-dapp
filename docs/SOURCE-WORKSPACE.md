# Licensed source workspace

Clone all 24 pinned, license-verified sources:

```bash
git clone --recurse-submodules https://github.com/CodesbyFebin/awesome-kotlin-dapp.git
cd awesome-kotlin-dapp
git submodule status --recursive
```

For an existing checkout:

```bash
git pull --ff-only
git submodule sync
git submodule update --init --jobs 4
```

Each upstream repository is under upstream/<owner>/<repository> at its catalog commit. These are Git submodules: the parent repository stores commit pointers, not flattened copies. GitHub's default source ZIP does not include submodule content; use recursive cloning. Dependencies remain separate and do not form an integrated build automatically.

License files were read at the 24 exact commits. Apache-2.0, GPL-3.0, LGPL-3.0 and dual MIT/Apache-2.0 sources retain upstream ownership and notices. Magisk is an optional GPL platform reference, not an application dependency. Inspect nested dependency and asset terms before distribution. This is not a license compatibility audit.

The 24 remaining references are excluded from submodule imports. The catalog is retained for discovery; reference listing grants no reuse permission. Kr1ptal/ethers-kt metadata identifies Apache-2.0, but no root license file was located at its pinned commit, so it was excluded pending verification.

No builds or runtime wallet gates are closed by these source pointers. Submodule checkout must still execute on the user's networked machine.
