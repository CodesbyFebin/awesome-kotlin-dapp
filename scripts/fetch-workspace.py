#!/usr/bin/env python3
"""Fetch selected pinned sources without executing upstream code."""
import argparse, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = {
    "android/nowinandroid", "Kotlin/kotlinx.coroutines",
    "Kotlin/kotlinx.serialization", "ktorio/ktor",
    "solana-mobile/mobile-wallet-adapter", "solana-mobile/mock-mwa-wallet",
    "solana-mobile/web3-core", "solana-mobile/rpc-core",
    "solana-mobile/solana-mobile-skills",
}
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=["solana-android", "kotlin-learning", "full-reference"], default="solana-android")
    parser.add_argument("--list", action="store_true", help="Show selections without cloning")
    args = parser.parse_args()
    rows = json.loads((ROOT / "catalog/resources.json").read_text())["resources"]
    rows = [r for r in rows if args.profile == "full-reference"\
            or (args.profile == "solana-android" and r["repository"] in CORE)\
            or (args.profile == "kotlin-learning" and r["repository"].startswith("philipplackner/"))]
    base = ROOT / "workspace/sources"
    targets = []
    for row in rows:
        name, sha = row["repository"], row["commit"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", name) or not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise SystemExit("Invalid repository identity or commit")
        target = base / name
        if args.list:
            print(name, sha)
        else:
            if target.exists():
                raise SystemExit(f"Destination exists; inspect before retry: {target}")
            targets.append((row, target))
    if args.list:
        return
    manifest = ROOT / "workspace/source-manifest.json"
    if manifest.exists():
        raise SystemExit("Manifest exists; preserve the previous workspace before fetching another profile")
    # All destinations checked before the first network operation.
    results = []
    for row, target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "-c", "core.hooksPath=/dev/null", "clone", "--no-checkout",
                        "--filter=blob:none", "--", row["url"] + ".git", str(target)], check=True)
        subprocess.run(["git", "-C", str(target), "-c", "core.hooksPath=/dev/null",
                        "-c", "submodule.recurse=false", "checkout", "--detach", row["commit"]], check=True)
        head = subprocess.check_output(["git", "-C", str(target), "rev-parse", "HEAD"], text=True).strip()
        if head != row["commit"]:
            raise SystemExit(f"Commit mismatch: {row['repository']}")
        results.append({"repository": row["repository"], "commit": head, "path": str(target.relative_to(ROOT))})
        manifest.parent.mkdir(parents=True, exist_ok=True)
        manifest.write_text(json.dumps({"profile": args.profile, "complete": False, "sources": results}, indent=2) + "\n")
    manifest.write_text(json.dumps({"profile": args.profile, "complete": True, "sources": results}, indent=2) + "\n")
    print(f"Fetched {len(results)} sources. No builds or upstream scripts executed.")
if __name__ == "__main__":
    main()
