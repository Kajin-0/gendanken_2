# Paper 02 — Rev. 8 adversarial-response ledger

**Date:** 2026-08-16  
**Status:** **CLOSED / REV. 8 PROMOTED / SCIENTIFIC SUBMISSION GATE RESTORED**

## Trigger

A later independent adversarial review of compiled Rev. 7 identified a major carrier-species scope issue plus several methodological/presentation issues. Rev. 7 remains immutable provenance. Rev. 8 was created only after the claim-affecting checks below were executed.

## Disposition

### R8-1 — Carrier-species closure — CLOSED

The exact planar pair model satisfies the dc full-collection identity to `1.11e-16`, and the uniform two-carrier null recovers numerical-zero diffusion. The heterogeneous pair stress shows that the positive single-carrier apparent-diffusion result is not generically invariant after admitting a second carrier contribution. In the cleaner known-countercarrier-root stress, only `1/21` core speed/frequency cases retains positive downstream inferred diffusion.

**Manuscript action:** Rev. 8 explicitly restricts the theorem/counterexample to a single-mobile-carrier / unipolar Shockley–Ramo observable. No generic two-carrier photodiode claim is made.

### R8-2 — Mean-upstream versus `remote` wording — CLOSED

The baseline demonstrates finite-support coupling while all channel means lie upstream, but does not justify a broad generic `remote` label.

**Manuscript action:** stronger `remote` language was removed. The result is stated as finite kernel support inside the nonuniform region despite mean generation depths lying upstream.

### R8-3 — Exact upstream one-mode bridge — CLOSED

For a uniform upstream interval with velocity `v0`, Rev. 8 now gives the exact affine-plus-exponential source-coordinate solution

```text
H(z,omega) = v0/(i omega L) + C(omega) exp(i omega z/v0)
```

with all downstream heterogeneity entering only through the matching constant. This explains why upstream point-source sequences can remain one-mode even though trajectories later cross the heterogeneous region.

### R8-4 — Exact planar continuum as primary calculation — CLOSED

The mesh-free exact planar continuum is now the primary full-contact calculation. The independent two-dimensional field/trajectory solver is retained as a numerical reproduction/generalization check.

Primary exact values:

```text
D_eff(100 MHz) = 2.618164535e-3 m^2/s
D_eff(500 MHz) = 2.550830551e-3 m^2/s
D_eff(1 GHz)   = 2.350617904e-3 m^2/s
```

### R8-5 — Root-space versus full-channel rejection — CLOSED

A direct full-channel homogeneous-manifold test was implemented in addition to the root-space test. Under the declared equal-quadrature covariance, `alpha=0.0027`, 90% power, and amplitude/RMS-channel convention `S_dB=20 log10 S`:

```text
through 1 GHz: root-space 90.37 dB; full-channel 81.51 dB
through 2 GHz: root-space 73.20 dB; full-channel 72.28 dB
through 3 GHz: root-space 64.21 dB; full-channel 65.00 dB
```

The tests are presented as complementary; neither is claimed globally optimal.

### R8-6 — Manuscript/reproducibility polish — CLOSED

- SNR dB convention made explicit.
- Internal `hostile review`, failed-run, validation-helper, and raw workflow-ID prose removed from submission-facing PDFs.
- Anonymity preserved.
- Source/reproduction statement retained without fabricating an archival DOI.

### R8-7 — HgCdTe self-consistency/significance — CLOSED AS A SCOPE LIMITATION

No poorly constrained self-consistent HgCdTe device simulation was manufactured. The HgCdTe construction remains explicitly a conditional optical/field/timing scale example, not a calibrated detector model. This is a significance/scope limitation rather than a correctness defect in the theorem.

## Final gate

```text
GitHub Actions run: 31983951996
job:               95255579031
artifact:          paper02-manuscript-rev8-package
artifact id:       9273251646
artifact SHA-256:  653c996b3166211cb465efceee5ba64944b7e92eab14c0ae38046e7fc89f2b60
main PDF SHA-256:  97a0916bcc83f94221f78e3315cf21e9b3c593a2a40601470cbf0dcdc685df75
supp PDF SHA-256:  a7dadfe7289a715f53c09456a315e81d83393a4dd3fc90aee9b683d0d1e717db
```

All claim-affecting science was recomputed on the final branch head; scope guards, canonical figure regeneration, LaTeX/reference resolution, source persistence, artifact upload, and rendered page-by-page inspection passed.

Canonical status is recorded in `PAPER02_MANUSCRIPT_CURRENT.md` and `PAPER02_CURRENT_STATE_REV8_2026-08-16.md`.
