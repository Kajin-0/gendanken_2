# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **22-page Rev. 6**, validated against Rev. 5 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or historical Rev. 3/4/5 snapshots as the current source. Do not restore identifying author information from historical files, git history, account/profile information, public sources, or memory.

## Exact source

The canonical source is:

```text
MANUSCRIPT_REV6_ANON_2026-08-11.tex
```

and is preserved in six repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part06
```

Recover the exact editable baseline only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor refuses to write a working source unless the snapshot hash, source hash, line count, and anonymous author metadata match:

```text
source SHA-256 = 2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4
gzip SHA-256   = aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e
bytes = 67837
lines = 924
pages in matching compiled PDF = 22
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

Never reconstruct it from handoff notes or overwrite it with an older source.

## Rev. 6 status

Rev. 6 is a surgical response to the Rev. 5 hostile review. It does **not** reopen or compress the established four-color theorem, branch-qualified DC/RF inversion, hot-state treatment, singular weighting-field theorem, source-coordinate analysis, or nuisance framework.

The new boundaries that must be preserved are:

```text
rank-two detection
-> rank-two parameter resolution
-> physical root-law discrimination
```

A nominally significant second Hankel mode does not imply well-conditioned recovered roots. For the product

```math
P=q_1q_2=W_1/W_0,
```

Rev. 6 carries the first-order covariance including the shared-minor covariance. In the deliberately optimistic independent equal-significance limit,

```math
sigma_P/|P| ~ sqrt(2)/Z,
```

so `Z=3` corresponds to about **47.1%** relative product uncertainty; roughly `Z=14.1` is needed for 10% product precision in that simplified limit.

Rev. 6 also makes explicit that:

- the one-dimensional nonuniform weighting field is an **effective observation-operator surrogate**, not a generic self-consistent finite-pixel geometry;
- the HgCdTe stress uses a force-partition sensitivity coordinate `xi`, with all previously reported finite-width benchmark/resource values corresponding to the **conditional `xi=1` baseline**;
- adjacent 2021 Ge-PN and 2024 Ge-PIN OED literature is part of the prior-art boundary, but those works use wavelength-dependent detector response as a sensing observable rather than imposing the manuscript's calibrated spatial-sequence/model-order/cross-RF null hierarchy;
- two-carrier labels are meaningful only after both modes are statistically resolved and continuously tracked;
- covariance chi-square tests are per-rung/conditional; sequential model-order selection and subsequent root-law tests require hierarchical error control in an experiment;
- the next decisive device-physics validation is one self-consistent **combined-physics synthetic detector challenge analyzed blindly through the hierarchy**.

Detailed audit:

```text
REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md
numerics/rev6_review_regression.py
```

Rev. 5, Rev. 4, and Rev. 3 remain preserved historical provenance.

## Priority and feasibility blockers

Priority remains **OPEN / UNPROVEN**. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before submission-level priority/novelty language.

Experimental feasibility is also not demonstrated merely by deriving resource requirements. The few-nanometer nonaffine-coordinate and approximately `1e-4 degree` irregular-phase scales remain derived design requirements, and the baseline-model covariance requirement must eventually be demonstrated in a credible calibration architecture.

## Privacy rule

Pseudonymity is the default. Any author name, pseudonym, affiliation, email, location, signature, or other identifying metadata requires explicit approval for that specific artifact. Prior appearance is not continuing consent.

See root `PRIVACY_PROTOCOL.md`.

## Separate geometry result

The realistic finite-electrode/depletion calculation remains separately auditable in:

```text
REALISTIC_GEOMETRY_CLOSURE_STRESS.md
PAPER_CLAIM_LEDGER_REV3_GEOMETRY_ADDENDUM_2026-08-11.md
MANUSCRIPT_REV3_GEOMETRY_INTEGRATION_PLAN_2026-08-11.md
```

It continues to qualify mechanism assignment but is not a calibrated device prediction and does not authorize compression of manuscript content.

## Mandatory rule

Before any manuscript edit, read:

1. root `PRIVACY_PROTOCOL.md`;
2. root `AGENTS.md`;
3. `MANUSCRIPT_BASELINE.md`;
4. `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. this file;
6. `CURRENT_STATE_LIVE.md`;
7. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
