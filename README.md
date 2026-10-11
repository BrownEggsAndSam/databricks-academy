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

## Governance Labs — new hands-on track

**[Open Governance Labs](https://browneggsandsam.github.io/databricks-academy/governance-labs.html)**

Seven days, 28 short checkpoints, synthetic data, and a separate evidence log.

| Day | Deliverable |
| --- | --- |
| 1 | One registered asset and its structure |
| 2 | Table/column inventory and a four-field glossary mapping draft |
| 3 | Quality score and exception report |
| 4 | Captured lineage and a defect/repair demonstration |
| 5 | Access matrix and a sharing validation plan |
| 6 | Collibra metadata/lineage comparison, when configured |
| 7 | Evidence pack, audit findings and a proposed pilot |

The route is provisionally aligned to governance themes. Confirm exact test scope and acceptance criteria privately. The public repository contains no internal test exports or screenshots. Full cross-account sharing, identity, integration and audit validation requires the configured environments and responsible owners.

The evidence log records execution scope, observed result, a short evidence reference and a private case reference. A local simulation cannot be marked as a passed integration check. All recorded results remain self-reported. Progress and notes save in this browser under a separate key; export/import JSON to move devices. Keep actual evidence in approved systems.

Build and validate this track with:

```sh
python3 labs/build.py
node labs/verify.cjs
```

Edit `labs/src/`; commit the rebuilt `docs/governance-labs.html`. The dependency-free verifier covers 15 groups, including evidence scope gates, imports, exports and fixture arithmetic. SQL has not been run against a live Databricks workspace. Browser visual QA was unavailable during this update.

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
