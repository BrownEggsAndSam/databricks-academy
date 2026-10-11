# Databricks Academy — one-week sandbox sprint

**[Open the hands-on guide](https://browneggsandsam.github.io/databricks-academy/)**

An action-first route for a data-governance practitioner learning Databricks. One project, seven days, four checkpoints per day. Keep the guide beside the company sandbox and work one step at a time.

| Day | Build or explore |
| --- | --- |
| 1 | Create 12 synthetic loans and find the table |
| 2 | Profile data and identify four defects |
| 3 | Build accepted, exception and scorecard views |
| 4 | Add descriptions, query inventory, inspect lineage, draft a Collibra mapping |
| 5 | Create a quality dashboard |
| 6 | Capture a snapshot and run it with a SQL job |
| 7 | Break one record, trace the results, refresh and repair |

Plan about 6–7 hours across the week. The outcome is practical fluency with a small workflow, not guaranteed expertise or certification readiness.

## Start in an empty sandbox

The guide supplies all sample data. You need an approved SQL warehouse, a Unity Catalog catalog, and permission to use a writable schema and create lab tables/views. Creating a new schema is optional if the vendor supplies one. The SQL job exercise requires a pro or serverless SQL warehouse and suitable job/run-as permissions.

Enter the catalog, schema and unique table prefix in **My sandbox**. Copy SQL from each step into Databricks. The guide never connects to your workspace or executes SQL itself. Instructions use AWS documentation; menu labels and available capabilities can differ.

**I'm stuck** provides a targeted hint and copyable access request. Mark unavailable steps blocked and continue; blocked work does not count as completed. Keep schedules off during the exercise.

## Progress and reference

Progress auto-saves in this browser. **Save & move** exports/imports the week's JSON backup. There is no login or automatic cross-device sync. Private browsing, cleared browser data or managed-device cleanup can remove progress.

The [older, extended academy](https://browneggsandsam.github.io/databricks-academy/deep-dive.html) remains optional reference. Its source and original progress key are preserved. The new checklist uses a separate storage key.

The site is public. Keep sensitive evidence in approved company systems. Downloads include per-step SQL, a draft Collibra mapping CSV and a three-minute team-demo card. Nothing is uploaded to Collibra.

## Maintain

No package installation is required.

```sh
python3 sprint/build.py
node sprint/verify.cjs
```

Edit `sprint/src/`, rebuild, and commit `docs/index.html` with the source. GitHub Pages serves `main:/docs`. The page is self-contained.

The previous course stays under `academy/`; `python3 academy/build.py` now rebuilds `docs/deep-dive.html`.

Validation covers routes, SQL names, checkpoints, blocked progress, import sanitization, storage failures and arithmetic from the actual synthetic SQL seed. The scripts were not executed in a live Databricks workspace; verify the indicated results there. Official links are inside the guide. Instructions checked 11 October 2026.
