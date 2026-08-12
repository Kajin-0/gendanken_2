# Manuscript Rev. 9 preservation report

## Canonical predecessor

```text
source: experiments/01-vanishing-absorber/MANUSCRIPT_REV8_ANON_2026-08-11.tex
SHA-256: 28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9
bytes: 81816
lines: 1023
compiled pages: 26
sections: 12
subsections: 18
bibliography items: 19
equation environments: 107
author/PDF metadata: Anonymous
```

## Rev. 9 candidate

```text
candidate source: experiments/01-vanishing-absorber/MANUSCRIPT_REV9_ANON_2026-08-11.tex
candidate SHA-256: df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4
candidate bytes: 92749
candidate lines: 1086
candidate compiled pages: 28
candidate sections: 12
candidate subsections: 19
candidate bibliography items: 21
candidate equation environments: 116
candidate author/PDF metadata: Anonymous
candidate PDF SHA-256: 7ed48fd44b948158fb08dcece8ea09b168eafbd48cf6c7d4c6643dea7546f386
candidate PDF bytes: 524876
```

## Structural preservation

```text
line count:                 1023 -> 1086
compiled pages:               26 -> 28
sections:                     12 -> 12
subsections:                  18 -> 19
bibliography items:           19 -> 21
equation environments:       107 -> 116
existing sections removed:     0
existing subsections removed:  0
references removed:            0
unrelated derivations removed: 0
```

Nonblank-line sequence comparison:

```text
Rev. 8 nonblank lines:                 883
exact prior nonblank lines retained:   849
prior nonblank lines replaced/deleted:  34
replacement/deletion fraction:        3.85%
```

This is well below the repository's 15% destructive-rewrite alarm. The candidate grows rather than shrinks.

## Additive material

New subsection:
```text
Known arbitrary generation kernels
```

New primary prior-art references:
```text
Goodman1961
Geist1980
```

## Scientific reasons for changed Rev. 8 lines

1. Add the confluent/repeated-root rank-two branch `(A+Bm)q^m` and classify rank two by the recurrence discriminant.
2. Qualify the determinant covariance near the rank-one nonregular boundary.
3. Separate common depth-scale calibration from nonaffine coordinate calibration and derive the exact scaling of `D,w,kappa`.
4. Add a kernel-aware homogeneous one-mode null for independently calibrated arbitrary generation kernels.
5. Treat the composition profile as a shared optical/transport nuisance in experimental inference.
6. Bound the quoted electron-affinity partition validation to the interval actually analyzed in its source.
7. Label the high-Peclet relation as asymptotic intuition at the worked local Peclet numbers.
8. Label the inherited hot-state stress as an independent deliberately strong benchmark.
9. Broaden the prior-art boundary to classical spectral-depth transport probing.
10. Add free DC physical-admissibility nulls.
11. Propagate these qualifications into the abstract, discussion, conclusion, hierarchy, and nuisance language.

No prior scientific result was removed merely because the hostile review criticized it.

## Regression

Local `rev9_review_regression.py`: PASS.

## Compilation and visual QA

- `pdflatex` completed twice without errors.
- No unresolved references or citations.
- No overfull boxes.
- PDF title is unchanged; PDF author is `Anonymous`.
- All 28 pages were rendered and visually inspected.
- No clipping, overlapping text, malformed equations, broken tables, or malformed glyphs were found.
- Underfull-box warnings in dense tabular material are visually benign.

## Privacy

The candidate retains:
```text
\author{Anonymous}
pdfauthor={Anonymous}
```

No identifying metadata has been introduced.

## Repository snapshot

The permanent repository snapshot was derived from the exact Rev. 9 source on the GitHub Actions Python 3.12 runner after the source SHA, byte count, line count, and anonymous metadata were verified.

```text
deterministic gzip SHA-256: 15b434edbd72a5217f6183e45a537350683755fd98ec7f39716a21e5f601cdb9
gzip bytes: 31390
base64 characters: 41856
snapshot parts: 7
part lengths: 6000 / 6000 / 6000 / 6000 / 6000 / 6000 / 5856
part01 SHA-256: 38bfafac58f83aa1a56817d1a10e40107b86bbeec01489dc11ff254c04a4a29f
part02 SHA-256: 40dd2c5e7ea8bab905a22632b93c0e763cd334a419a46d163fc06fb83651d8cd
part03 SHA-256: 627a39ba57ed7f4fc743cfb26bb35f550c0bc5455128396f8ab0facde638b63a
part04 SHA-256: e92a7aeda44b278d03938f4cf25911bdb566806ce4721e803bc39c016bc92f6c
part05 SHA-256: 978070ecd42af3ed7bfd8e1730640ba02e3da1d5fa3347aa3fbdbc1a3c3c5c2e
part06 SHA-256: 856c0d43913c177b7792dd7323d7beb480cb5f2cb44de4df78b87d78a95a854c
part07 SHA-256: afceaff9833ce594fe4b9762f6363558ee5b6b120c8fba5a5c422e75f70357f2
```

The decompressed source remains the primary invariant:
`df62813f764f051684ec52162095a5103296b71da1549b4c96829b0168fa1ce4`.
