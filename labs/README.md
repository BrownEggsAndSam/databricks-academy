# Governance lab route

[Open the interactive labs](https://browneggsandsam.github.io/databricks-academy/governance-labs.html).

This is a public, generic learning track. Exact alignment to a private test plan is provisional. Use the evidence log locally to record neutral case references; keep internal exports, screenshots and actual evidence in approved systems.

## Prerequisites

Approved SQL warehouse with CAN USE; an approved writable Unity Catalog schema with USE CATALOG, USE SCHEMA and CREATE TABLE; normal access to owned lab objects. Use a unique prefix. New schema creation additionally requires CREATE SCHEMA and configured managed storage. The guide makes no network connection to Databricks or Collibra.

## The seven deliverables

### Day 1: Find and model your data

40–55 min. One synthetic table, with its structure explained.

1. **Find your starting point** — A successful query and at least one approved catalog.
2. **Reserve a clean lab space** — A writable schema with names saved in this guide.
3. **Create your synthetic fixture** — rows_created = 12.
4. **Separate an asset from its storage** — Four columns: loan_id, balance, state, status. DESCRIBE DETAIL reports Delta.

### Day 2: Make the asset discoverable

40–55 min. A small, reviewable metadata contract.

1. **Add a useful definition** — The table has GOV_A; balance has units and a rule.
2. **Export one table's inventory** — Exactly one matching raw-table row.
3. **Validate the column model** — Four ordered columns. Nullable metadata alone does not define your business rules.
4. **Map the technical fields to business terms** — Four proposed mappings; a technical column remains distinct from its business term.

### Day 3: Turn defects into a report

45–60 min. A reusable exception list and a quality score.

1. **Measure before changing data** — 12 total rows; 12 unique loans; 11 balances present; 1 missing.
2. **Make failures explainable** — exceptions = 4; the accepted view contains 8 rows.
3. **Build a score with a denominator** — 12 assessed; 8 accepted; 4 rejected; pass_pct = 66.7.
4. **Keep a small report** — A saved scorecard query and an export with four exceptions.

### Day 4: Trace impact and repair it

45–60 min. A before/after lineage and impact demonstration.

1. **Create a downstream table** — FL: 2 loans / 330000; NJ: 2 / 125000; VA: 4 / 1260000.
2. **Inspect the captured lineage** — A visible captured dependency, with table-level and column-level findings recorded separately.
3. **Predict, then introduce one defect** — The score drops to 58.3%; the stored summary still has the previous VA total of 1260000.
4. **Repair and prove recovery** — pass_pct = 66.7; accepted_balance = 1715000.

### Day 5: Test access with the right identity

40–60 min. An access matrix and a sharing test plan.

1. **Inspect what you can inspect** — Visible grants at each available level, plus any visibility limitation.
2. **Build a limited consumer view** — 4 rows, with loan_id and state only.
3. **Run an assisted allow/deny check** — Evidence for both the allowed path and the denied path under the intended identities.
4. **Choose the correct sharing test** — A scoped sharing plan; actual sharing remains blocked until both sides are exercised.

### Day 6: Reconcile Collibra metadata

45–65 min. A source-to-catalog comparison with clear gaps.

1. **Capture a source baseline** — One raw-table record and four column records, with names and comments.
2. **Validate the inbound asset mapping** — A recorded match/mismatch for each configured metadata field.
3. **Test a metadata change** — The source has GOV_B; a real integration test also finds GOV_B on the intended target asset.
4. **Check lineage independently** — Independent evidence for metadata sync and lineage sync.

### Day 7: Build your evidence pack

40–60 min. A short demo and an honest test summary.

1. **Trace your own lab changes** — At least one lab UPDATE in Delta history and a query-history observation.
2. **Inspect audit events if authorized** — Recent events for your identity, or a documented access/availability blocker.
3. **Separate practice from validation** — Each result says whether it was prepared, run locally, or run through the real integration.
4. **Demonstrate one useful pilot** — 66.7% pass rate; 3 summary rows; 8 accepted loans; 1715000 balance; 4 consumer-view rows.

## Evidence scope

- **Asset inventory & model** — Sandbox executed. Raw table and four columns match the agreed asset structure, types, definitions and parent relationships.
- **Profiling & exception reporting** — Sandbox executed. 12 assessed, 8 accepted, 4 explained exceptions, and 66.7% under the stated sample rules.
- **Local table & column lineage** — Sandbox executed. Actual captured upstream dependency and column finding retained; missing/masked edges are explained.
- **Least-privilege consumption** — Integration executed. Approved identities produce the expected allowed and denied results on source and consumer objects.
- **Cross-boundary sharing & lineage** — Integration executed. Approved provider and recipient demonstrate the requested data scope, access behavior and lineage; exact private case criteria apply.
- **Collibra metadata integration** — Integration executed. A real run maps the intended table/columns and required fields; GOV_A→GOV_B reaches the same target asset as configured.
- **Collibra technical lineage** — Integration executed. A real lineage run produces the expected source-to-target and column observations, with gaps recorded.
- **Centralized audit evidence** — Integration executed. The required event types, scope, retention and delivery are verified against the actual private case, with an audit-owner review.

## Assisted checks

- Access: use approved test identities and the actual expected allow/deny matrix. An owner session cannot prove consumer restrictions.
- Sharing: both provider and recipient must be exercised. A local projection is preparation only.
- Collibra: confirm metadata and technical-lineage capabilities separately; retain actual run references. A draft CSV is not a connector.
- Audit: validate event types, coverage, retention and delivery against the real case with the audit owner.

## Later tracks

Disaster recovery, networking, identity lifecycle, materialized-view sharing and unexplained internal integrations need separate requirements and specialist owners. They are not presumed irrelevant; they are outside this first-week practice track.

## Source and validation

Official sources are linked inside each exercise; checked 11 October 2026. The local verification script exercises UI logic with a mock DOM and verifies seed arithmetic. It is not a Databricks integration test or a visual browser test.

Run `python3 labs/build.py` and `node labs/verify.cjs`. Commit source plus `docs/governance-labs.html`.
