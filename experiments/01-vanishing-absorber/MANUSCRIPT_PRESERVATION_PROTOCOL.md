# Manuscript Preservation Protocol

**Purpose:** prevent accidental loss of accumulated scientific work when a new agent integrates a new theorem, simulation, reviewer response, or correction.

This protocol is mandatory for any file matching `MANUSCRIPT*.tex` or any file designated as the current manuscript.

## 1. Source-of-truth rule

Before editing the manuscript, read in this order:

1. root `AGENTS.md`;
2. `MANUSCRIPT_BASELINE.md`;
3. the exact current manuscript source or its verified repository snapshot;
4. `PAPER_CLAIM_LEDGER.md` plus any newer claim-ledger addenda;
5. the result/addendum being integrated.

**A handoff summary is navigation, not source material.**

Do not reconstruct the paper from summaries, theorem notes, old drafts, PDFs, or memory when the exact current source exists or can be recovered.

If the exact current source is unavailable or its hash cannot be verified, stop manuscript editing. New work may be recorded only in a separate addendum/result file until the source is recovered.

## 2. Preserve first; integrate second

The default manuscript operation is a surgical edit of the exact previous source.

When integrating a new scientific result:

- preserve every unrelated derivation, quantitative stress, calibration result, table, reference, limitation, and counterexample;
- change only claims or passages logically affected by the new result;
- add a new section/subsection when that is clearer than rewriting existing material;
- do not opportunistically compress, reorganize, restyle, or rewrite unrelated portions of the paper;
- do not change author/title metadata unless the user explicitly asks.

A new result that weakens a claim is allowed to weaken that claim. It does **not** grant permission to shorten the rest of the paper.

## 3. Large-rewrite rule

Assume a destructive rewrite has occurred until proven otherwise if any of the following happens relative to the current canonical source:

```text
line count falls by > 8%
> 15% of prior nonblank source lines are deleted/replaced
an existing section disappears
an existing subsection disappears
bibliography-item count decreases
equation-environment count falls by > 5%
author or title changes unexpectedly
```

These thresholds are alarms, not scientific laws. Exceeding one requires an **explicit current user request** for compression, restructuring, or a large rewrite.

An agent may not infer that permission from phrases such as `revise`, `integrate`, `harden`, `improve`, `update`, `review`, or `make submission-ready`.

## 4. Required preservation report

Every manuscript-changing PR must report at minimum:

```text
base source path/hash
candidate source path/hash
base -> candidate line count
base -> candidate page count if compiled
sections removed
subsections removed
bibliography items removed
equation environments removed
approximate prior-line replacement/deletion fraction
new sections/subsections
scientific reason for every removed item
```

The expected normal integration pattern is:

```text
existing sections removed: 0
existing references removed: 0
unrelated derivations removed: 0
```

## 5. Explicit-rewrite exception

A deliberate compression/reorganization is allowed only when the user explicitly asks for it in the current task.

If automated preservation checks would otherwise fail, create a temporary justification file named:

```text
experiments/01-vanishing-absorber/MANUSCRIPT_DESTRUCTIVE_EDIT_JUSTIFICATION.md
```

It must contain both:

```text
USER_EXPLICITLY_REQUESTED_LARGE_REWRITE: true
USER_REQUEST_QUOTE: <verbatim user instruction authorizing compression/restructuring>
```

The justification must explain every removed section/subsection and should be deleted after the reviewed rewrite lands.

Do not fabricate or paraphrase the quote.

## 6. Branch/PR rule

Do not make manuscript changes directly on `main`.

Use a dedicated branch and PR. Numerical/result files may be developed first; manuscript integration should be a separate, reviewable commit or PR stage whenever practical.

Before merge:

1. run `tools/check_manuscript_preservation.py` against the exact previous source;
2. compile the manuscript;
3. visually inspect the PDF pages;
4. verify references/equations/tables and author metadata;
5. inspect the complete diff for unrelated deletions.

## 7. Canonicalization after an approved revision

After a manuscript revision is accepted:

- preserve an immutable snapshot under `manuscript_history/`;
- update `MANUSCRIPT_BASELINE.md` with the new source hash and structural counts;
- update the current-source pointer in `AGENTS.md`;
- update the claim ledger and current-state file only for scientific conclusions that actually changed.

Never leave a newer user-facing manuscript outside the repository without recording its exact filename/hash and preservation status.

## 8. Current recovery incident

This protocol was added after a 2026-08-11 audit found that a new-agent reconstruction shortened the true 16-page Rev. 3 source from 696 LaTeX lines to 436 lines while unintentionally removing established conditioning, two-carrier, hot-carrier, weighting-field, calibration, spacing, recombination, cross-check, and measurement-resource material.

That reconstruction was closed unmerged. The incident is provenance for why these safeguards exist.