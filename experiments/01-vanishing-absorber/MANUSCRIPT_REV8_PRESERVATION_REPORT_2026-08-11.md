# Rev. 8 manuscript preservation report

## Scope

Rev. 8 is a surgical correction of canonical anonymous Rev. 7 in response to the next adversarial review. The revision is not a compression or structural rewrite. It preserves all unrelated derivations, sections, subsections, references, numerical resources, limitations, and historical corrections.

## Exact base

```text
base source: experiments/01-vanishing-absorber/MANUSCRIPT_REV7_ANON_2026-08-11.tex
base SHA-256: 9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8
base bytes: 75182
base lines: 963
base compiled pages: 24
base sections: 12
base subsections: 18
base bibliography items: 19
base equation environments: 102
base author/PDF metadata: Anonymous
```

## Rev. 8 candidate

```text
candidate source: experiments/01-vanishing-absorber/MANUSCRIPT_REV8_ANON_2026-08-11.tex
candidate SHA-256: 3f5307064b233f3976e037c541809557ee07fd712b1b5491734d9a3469035b97
candidate bytes: 81816
candidate lines: 1023
candidate compiled pages: 26
candidate sections: 12
candidate subsections: 18
candidate bibliography items: 19
candidate equation environments: 107
candidate author/PDF metadata: Anonymous
candidate PDF SHA-256: 54e43bbd18cd841bd2138ef98b1568cb16df39589c85e85e4b66a015552fd544
candidate PDF bytes: 508279
```

## Structural preservation

```text
line count:                  963 -> 1023
compiled pages:               24 -> 26
sections:                     12 -> 12
subsections:                  18 -> 18
bibliography items:           19 -> 19
equation environments:       102 -> 107
existing sections removed:     0
existing subsections removed:  0
references removed:            0
unrelated derivations removed: 0
```

Using a nonblank-line sequence comparison with the canonical Rev. 7 source:

```text
Rev. 7 nonblank lines:                826
exact prior nonblank lines retained:  800
prior nonblank lines replaced/deleted: 26
replacement/deletion fraction:       3.15%
```

This remains well below the repository's 15% destructive-rewrite alarm and the candidate grows rather than shrinks.

## Scientific reasons for the changed Rev. 7 lines

1. Replace the defective unconditional minor closure `W1^2=W0W2` with the full `3x3` Hankel determinant `det(H)=0`; retain adjacent minors for conditioning and recurrence recovery.
2. Add the missing noise-aware rank-at-most-two determinant test between rejection of rank one and two-root parameter recovery.
3. Correct stale weighting-field false-phase prose using one consistent finite-kernel Rev. 8 transport calculation.
4. Separate generic `1e-5 deg` absolute numerical cross-verification from a dedicated differential recombination subtraction cross-check.
5. State explicitly that the electron-affinity relation anchors the composition-induced band-edge force, not the total self-consistent device drift.
6. Quantify the non-negligible density-of-states/effective-mass sensitivity.
7. Add the nearly lossless two-carrier DC observability degeneracy.
8. Propagate the corrected rank hierarchy into the abstract, discussion, conclusion, and mechanism examples.
9. Change revision labels from Rev. 7 to Rev. 8 where appropriate.

No previous scientific result was removed merely because the new review criticized it. Suggestions that did not survive independent checking were not adopted as stated.

## Deterministic recovery snapshot

The exact Rev. 8 source is compressed with deterministic gzip (`mtime=0`), base64 encoded, and split into seven repository-safe parts:

```text
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part01
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part02
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part03
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part04
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part05
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part06
MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part07
```

Snapshot invariants:

```text
gzip SHA-256: b9c87ffa2dce8870a5716b106280a62f177425c562c44af59f452c8d425d0c67
gzip bytes: 28085
base64 characters: 37448
parts: 7
part lengths: 6000 / 6000 / 6000 / 6000 / 6000 / 6000 / 1448 characters
```

Reconstruction must yield source SHA-256 `3f5307064b233f3976e037c541809557ee07fd712b1b5491734d9a3469035b97`, 81816 bytes, and 1023 lines.

## Compilation and visual QA

- `pdflatex` completed twice without errors.
- No unresolved references or citations.
- No overfull boxes.
- PDF metadata title is unchanged and author is `Anonymous`.
- All 26 pages were rendered to images and visually inspected.
- No clipping, overlapping text, broken equations, broken tables, or malformed glyphs were found.
- The few underfull-box warnings are benign line-spacing warnings in dense tabular/paragraph material; no visible defect was found.

## Privacy

The title is unchanged. Author metadata remains `Anonymous` in both source and PDF. No identity release is present or required.

## Regression

`numerics/rev8_review_regression.py` verifies:

- the exact Rev. 7 spurious minor-closure counterexample;
- the factorization `W1^2-W0W2=-d2 det(H)` on generic complex sequences;
- unchanged Rev. 7/8 finite-width HgCdTe target values;
- corrected 1% weighting-field false phases and 10% nuisance allocations;
- DOS/field velocity ratio and the `alpha_DOS` closure sensitivity table;
- the dedicated finite-difference versus adaptive-shooting differential recombination comparison.

## Disposition

**PRESERVATION: PASS locally.** Rev. 8 should remain a candidate until the repository's permanent Rev. 7 preservation and privacy workflows pass on a dedicated PR. Canonical pointers must not be changed in the scientific candidate PR.
