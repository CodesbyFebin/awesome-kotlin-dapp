# Philipp Lackner catalog checks

Session date (UTC): 2026-10-09.

Inspected GitHub repository metadata, default-branch commits and source trees for 12 selected learning references. The search inspected the first 100 repository results; this is not an exhaustive profile inventory. None of the selected source trees returned a LICENSE-named file, and GitHub license metadata was unidentified. Do not interpret that as permission to redistribute.

Executed locally:

- `python3 scripts/check-catalog.py`: exit 0; 37 records, JSON metadata and 10 local links.
- `python3 scripts/fetch-workspace.py --profile kotlin-learning --list`: exit 0; 12 pins.
- `python3 scripts/fetch-workspace.py --profile solana-android --list`: exit 0; nine pins, existing selection preserved.
- `python3 -m py_compile scripts/fetch-workspace.py`: exit 0.

Network source fetching, upstream builds, runtime tests and security qualification NOT_RUN.
