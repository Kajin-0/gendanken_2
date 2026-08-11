# Manuscript Build Fixes — 2026-08-11

**Status:** build QA for `MANUSCRIPT_DRAFT.tex`; no scientific claim change

The user-facing PDF compiled on 2026-08-11 required two source-level build corrections that should be synchronized into the canonical LaTeX manuscript on the next direct source edit.

## 1. Double-subscript macro

`MANUSCRIPT_DRAFT.tex` defines

```tex
\newcommand{\Cfour}{\mathcal{C}_4}
```

so expressions such as

```tex
\Cfour_{\mathrm{opt}}
```

and

```tex
\Cfour_{\mathrm{coord}}
```

produce a LaTeX `Double subscript` error.

Use either

```tex
\mathcal{C}_{4,\mathrm{opt}}
```

and

```tex
\mathcal{C}_{4,\mathrm{coord}}
```

or redefine the macro so that it does not contain a fixed subscript.

The compiled user-facing paper uses the explicit `\mathcal{C}_{4,...}` form.

## 2. Bibliography portability in the current runtime

The container has `pdflatex` / `latexmk` but no `bibtex` executable. The repository's separate

```text
MANUSCRIPT_REFERENCES.bib
```

is still the preferred machine-readable bibliography. For the downloadable PDF produced on 2026-08-11, the same verified references were embedded in a `thebibliography` environment so the paper could compile with repeated `pdflatex` passes alone.

This is an environment portability issue, not a bibliography-content change.

## 3. Cosmetic QA applied to the downloadable build

The user-facing compiled source also uses

```tex
\usepackage[hidelinks]{hyperref}
```

and fixed table placement for the two compact HgCdTe tables to avoid link boxes and awkward sentence/float splitting.

The final PDF was rendered page-by-page after compilation and checked for clipping, overlaps, broken references, and table layout.

## 4. Repository next action

On the next edit of `MANUSCRIPT_DRAFT.tex`:

1. apply the double-subscript correction;
2. preserve `MANUSCRIPT_REFERENCES.bib` as the canonical bibliography;
3. retain the cosmetic PDF QA improvements where compatible with the eventual journal class;
4. compile before committing the replacement source.
