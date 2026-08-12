# Current Manuscript Pointer

**Canonical manuscript status:** the current approved manuscript baseline is the anonymous **28-page Rev. 9**, validated against Rev. 8 before canonicalization.

**Canonical author metadata:** `Anonymous`.

Do **not** use `MANUSCRIPT_DRAFT.tex`, `MANUSCRIPT_DRAFT.md`, or historical Rev. 3/4/5/6/7/8 snapshots as the current source. Do not restore identifying author information from historical files, git history, account/profile information, public sources, or memory.

## Exact source

The canonical source is:

```text
MANUSCRIPT_REV9_ANON_2026-08-11.tex
```

and is preserved in seven repository snapshot parts:

```text
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part01
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part02
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part03
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part04
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part05
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part06
manuscript_history/MANUSCRIPT_REV9_ANON_2026-08-11.tex.gz.b64.part07
```

Recover the exact editable baseline only with:

```bash
python tools/extract_manuscript_baseline.py
```

The extractor refuses to write a working source unless the snapshot hash, source hash, line count, and anonymous author metadata match:

```text
source SHA-256 = df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
gzip SHA-256   = 15b434edbd72a5217f6183e45a537350683755fd98ec7f39716a21e5f601cdb9
bytes = 92749
lines = 1086
pages in matching compiled PDF = 28
author = Anonymous
PDF author metadata = Anonymous
```

The verified working copy is written to:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.tex
```

Never reconstruct it from handoff notes or overwrite it with an older source.

## Rev. 9 status

Rev. 9 is a surgical correction of canonical Rev. 8. The hostile review was treated as an attack list rather than authority; objections were integrated only after independent mathematical, numerical, physical, or literature checking.

The current rank-two hierarchy is:

```text
rank one rejected
-> rank-at-most-two determinant null tested
-> rank-two recurrence parameters resolved
-> distinct-root versus confluent/repeated-root branch classified
-> multiplicity-aware physical root law tested
```

For five first differences `d0...d4`, the unconditional six-color rank-at-most-two null remains `det(H)=0`. After rank two is resolved, define

```math
Delta_q=S^2-4P.
```

`Delta_q != 0` gives two distinct recurrence roots. `Delta_q = 0` with nonzero rank-two contrast gives the confluent sequence

```math
d_m=(A+Bm)q^m.
```

The ordinary distinct-root adjacent-minor identity is therefore not evaluated by naively setting `q1=q2` in the confluent case. Repeated roots can themselves be physical and require multiplicity-aware testing.

Rev. 9 additionally locks in:

- nonregular determinant statistics at the exact rank-one boundary, with null-constrained Monte Carlo / parametric-bootstrap calibration recommended when first-order linearization fails;
- common depth-scale sensitivity `D_cal=c^2D`, `w_cal=cw`, `kappa_cal=kappa`, separated from closure/nonaffine-coordinate calibration;
- a kernel-aware homogeneous one-mode null for independently calibrated arbitrary generation kernels, with the simple geometric four-color identity recovered for rigid translations;
- explicit recognition that raw simple-closure failure with evolving kernels rejects the combined transport+optical idealization unless the kernels are independently constrained;
- the composition profile `x(z)` as a shared optical/transport nuisance in experimental inference;
- the electron-affinity source's quoted 67.1% average partition / approximately ±1% two-thirds comparison bounded to its stated `0.15<x<0.45` interval rather than assumed to validate the worked front at `x=0.55`;
- local Peclet numbers near `0.48` per 0.5-um source step and `0.75` over the 0.79-um kernel width, so the high-Peclet formula is asymptotic intuition rather than the quantitative HgCdTe result;
- the inherited hot-to-cold calculation explicitly labeled as an independent deliberately strong two-state benchmark;
- older surface-photovoltage and photodiode spectral-response literature acknowledged as prior art for wavelength-dependent depth probing of carrier transport;
- free DC physical-admissibility checks `q(0) in (0,1]`, `D>0`, `kappa>=0`, plus the assumed drift-sign constraint.

The worked finite-width HgCdTe closure remains approximately `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz. It remains a conditional composition-band-edge transport stress, not a calibrated device prediction.

Detailed audit:

```text
REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV9_PRESERVATION_REPORT_2026-08-11.md
PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md
numerics/rev9_review_regression.py
```

Rev. 8 and earlier revisions remain preserved historical provenance.

## Priority and feasibility blockers

Priority remains **OPEN / UNPROVEN**. Spectral-depth carrier probing itself is established prior art. The exact closest 2024 graded-HgCdTe paper still requires a direct technical full-text comparison before submission-level priority/novelty language.

Experimental feasibility is also not demonstrated merely by deriving resource requirements. The few-nanometer nonaffine-coordinate and approximately `1e-4 degree` irregular-phase scales remain derived design requirements, the absolute common depth scale controls dimensional `D` and `w`, and kernel/composition/baseline-model covariance must eventually be demonstrated in a credible calibration architecture.

The strongest next device-physics validation remains a blind, self-consistent combined-physics synthetic detector challenge containing several ordinary departures simultaneously. Safe output `rank>2, mechanism unresolved` is an acceptable success mode.

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
7. `REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
8. `PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`;
9. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
10. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and earlier adversarial records as historical context;
11. the exact extracted current source.

**Preserve first; integrate second; rewrite only when explicitly requested by the user.**

**Pseudonymity first; identify only when explicitly approved by the user.**
