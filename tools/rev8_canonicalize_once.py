#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/'experiments'/'01-vanishing-absorber'


def read(p): return Path(p).read_text(encoding='utf-8')
def write(p,s): Path(p).write_text(s,encoding='utf-8')
def must_replace(s,old,new,label,count=None):
    n=s.count(old)
    if n==0 or (count is not None and n!=count):
        raise SystemExit(f'{label}: expected {count if count is not None else ">=1"} occurrences of {old!r}, found {n}')
    return s.replace(old,new)
def replace_between(s,start,end,new,label):
    i=s.find(start); j=s.find(end)
    if i<0 or j<0 or j<=i:
        raise SystemExit(f'{label}: cannot find section {start!r} -> {end!r}')
    return s[:i]+new.rstrip()+'\n\n'+s[j:]

# Manifest
p=EXP/'MANUSCRIPT_BASELINE.json'
d=json.loads(read(p))
d.update({
 'status':'canonical_rev8_hankel_rank2_and_hgcdte_uncertainty',
 'source_filename':'MANUSCRIPT_REV8_ANON_2026-08-11.tex',
 'source_sha256':'28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9',
 'source_bytes':81816,'source_lines':1023,'compiled_pages':26,
 'section_count':12,'subsection_count':18,'bibliography_item_count':19,
 'equation_environment_count':107,'author':'Anonymous','privacy_default':'anonymous','identity_release_required':True,
})
write(p,json.dumps(d,indent=2)+'\n')

# Exact extractor
p=ROOT/'tools'/'extract_manuscript_baseline.py'; s=read(p)
for old,new in [
 ('immutable anonymous Rev. 7 manuscript baseline','immutable anonymous Rev. 8 manuscript baseline'),
 ('MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part*','MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part*'),
 ('9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8','28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9'),
 ('8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b','44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7'),
 ('EXPECTED_PARTS = 6','EXPECTED_PARTS = 7'),('EXPECTED_LINES = 963','EXPECTED_LINES = 1023')]:
    s=must_replace(s,old,new,str(p),1)
write(p,s)

# Baseline narrative
p=EXP/'MANUSCRIPT_BASELINE.md'; s=read(p)
for old,new in [
 ('CANONICAL REV. 7 MANUSCRIPT BASELINE','CANONICAL REV. 8 MANUSCRIPT BASELINE'),
 ('MANUSCRIPT_REV7_ANON_2026-08-11.tex','MANUSCRIPT_REV8_ANON_2026-08-11.tex'),
 ('Rev. 7 was first validated against the established Rev. 6 baseline in PR #11. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 63 of 924 established Rev. 6 lines were changed or removed (~6.82%); no section, subsection, reference, or unrelated derivation was deleted.',
  'Rev. 8 was first validated against the established Rev. 7 baseline in PR #13. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 26 of 826 established nonblank Rev. 7 lines were changed or removed (~3.15%); no section, subsection, reference, or unrelated derivation was deleted.'),
 ('The exact source is preserved as six deterministic base64 text parts containing a gzip-compressed snapshot:',
  'The exact source is preserved as seven deterministic base64 text parts containing a gzip-compressed snapshot:'),
 ('manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part06',
  'manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part06\nmanuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part07'),
 ('9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8','28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9'),
 ('bytes: 75182','bytes: 81816'),('lines: 963','lines: 1023'),('compiled pages: 24','compiled pages: 26'),
 ('\\begin{equation} environments: 102','\\begin{equation} environments: 107'),
 ('8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b','44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7'),
 ('bytes: 26026','bytes: 28082'),('parts: 6','parts: 7'),
 ('Anonymous Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved','Anonymous Rev. 7, Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved'),
 ('must not override Rev. 7','must not override Rev. 8')]:
    s=must_replace(s,old,new,str(p))
newsec=r'''## Rev. 8 corrections now canonical

Rev. 8 preserves the central four-color theorem, branch-qualified inversion, classical finite-exponential lineage, singular weighting-field treatment, calibration framework, and the literature-anchored HgCdTe composition-band-edge stress. It repairs one genuine algebraic defect in the six-color rung and hardens the associated statistics and material-model boundaries.

The mandatory rank hierarchy is now:

```text
rank one rejected
-> rank-at-most-two Hankel-determinant null tested
-> two-mode recurrence parameters resolved
-> RF physical law tested
-> higher ordinary finite rank if rank two fails
```

The previous unconditional six-color minor closure is **SUPERSEDED** because

```math
W_1^2-W_0W_2=-d_2 det(H).
```

Thus `W1^2=W0W2` contains a spurious `d2=0` acceptance branch. The unconditional rank-at-most-two null is

```math
det [[d0,d1,d2],[d1,d2,d3],[d2,d3,d4]] = 0.
```

The adjacent-minor formula remains valid and useful for mode separation, conditioning, and recurrence recovery when nondegenerate; it is not the general model-order null. Rev. 8 also carries a covariance-aware complex determinant residual before root recovery.

Additional canonical hardening:

- the finite-kernel 1% weighting-field false phases are approximately `0.002947 / 0.012140 / 0.010007 degree` at 100 / 500 / 1000 MHz, with 10%-of-target allowable variations `0.757% / 0.881% / 1.961%`;
- the tiny graded-recombination subtraction is validated by a dedicated differential finite-difference versus adaptive-shooting comparison, conservatively agreeing within about `3e-9 degree` across tested numerical environments; the coarser `1e-5 degree` absolute solver comparison is not used to validate that subtraction;
- the 2025 electron-affinity relation anchors the **composition-induced conduction-band force term**, not the total self-consistent device drift; Poisson/electrostatic fields remain outside the worked one-dimensional stress;
- under the retained reduced `m* proportional to Eg` prescription, `|v_DOS|/v_field` ranges from about **8.8% to 18.3%**, so the DOS/effective-mass term is a substantive uncertainty rather than a negligible correction;
- scaling `v_DOS` by `alpha_DOS=0,0.5,1,1.5` moves the 100-MHz closure from about `-0.01861` to `-0.02349 degree`, exposing that uncertainty directly;
- in the nearly lossless two-carrier limit, total DC Shockley--Ramo response can become depth-degenerate, so species-specific tracking may require two or more nonzero RF frequencies;
- the exact closest 2024 graded-HgCdTe priority audit remains **OPEN / UNPROVEN**; metadata and adjacent papers do not substitute for the exact full-text comparison;
- the blind combined-physics detector challenge remains the next major device-physics validation, not a prerequisite for this localized algebraic repair.

Detailed records:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```

Adversarial reviews remain attack vectors rather than authority: accept, narrow, reject, or mark an objection out of scope only after independent checking.'''
s=replace_between(s,'## Rev. 7 corrections now canonical','## Priority and feasibility boundary',newsec,str(p))
write(p,s)

# Current pointer
p=EXP/'MANUSCRIPT_CURRENT.md'; s=read(p)
s=must_replace(s,'the anonymous **24-page Rev. 7**, validated against Rev. 5 before canonicalization','the anonymous **26-page Rev. 8**, validated against Rev. 7 before canonicalization',str(p),1)
s=must_replace(s,'historical Rev. 3/4/5 snapshots','historical Rev. 3/4/5/6/7 snapshots',str(p),1)
s=must_replace(s,'MANUSCRIPT_REV7_ANON_2026-08-11.tex','MANUSCRIPT_REV8_ANON_2026-08-11.tex',str(p))
s=must_replace(s,'and is preserved in six repository snapshot parts:','and is preserved in seven repository snapshot parts:',str(p),1)
s=must_replace(s,'manuscript_history/MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part06','manuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part06\nmanuscript_history/MANUSCRIPT_REV8_ANON_2026-08-11.tex.gz.b64.part07',str(p),1)
for old,new in [
 ('9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8','28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9'),
 ('8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b','44af67c407d07b6e7d60bbc6760f14cbe0f44cf763a74e972a9b3322a5d8d2f7'),
 ('bytes = 75182','bytes = 81816'),('lines = 963','lines = 1023'),('pages in matching compiled PDF = 24','pages in matching compiled PDF = 26')]:
    s=must_replace(s,old,new,str(p))
cursec=r'''## Rev. 8 status

Rev. 8 is a surgical correction of canonical Rev. 7. The hostile review was not followed mechanically: one theorem-level defect was accepted, several physical/numerical criticisms were narrowed and repaired, and suggestions that did not survive independent checking were not adopted as stated.

The critical model-order lock is:

```text
rank one rejected
-> rank-at-most-two determinant null tested
-> two-mode parameters resolved
-> physical root-law discrimination
```

For five first differences `d0...d4`, define the `3x3` Hankel matrix `H`. The unconditional six-color rank-at-most-two null is `det(H)=0`. The older scalar minor identity is no longer a general null because

```math
W1^2-W0W2 = -d2 det(H),
```

so it also vanishes spuriously when `d2=0`. Adjacent minors remain valid conditioning and parameter-recovery objects when nondegenerate.

Rev. 8 additionally locks in:

- a noise-aware covariance test for the complex Hankel determinant before rank-two root recovery;
- corrected finite-kernel weighting-field values: `0.002947 / 0.012140 / 0.010007 degree` false phase for 1% variation at 100 / 500 / 1000 MHz and allowable 10%-target variations `0.757% / 0.881% / 1.961%`;
- a dedicated differential recombination cross-check agreeing within about `3e-9 degree` across tested numerical environments;
- explicit separation of the electron-affinity-anchored composition-band-edge force from unknown self-consistent electrostatic drift;
- DOS/effective-mass sensitivity: `|v_DOS|/v_field ~= 8.8--18.3%` and a nontrivial `alpha_DOS` closure sweep;
- the nearly lossless two-carrier DC degeneracy, for which two or more nonzero RF frequencies may be required.

The worked finite-width HgCdTe closure remains approximately `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz. It remains a conditional composition-band-edge transport stress, not a calibrated device prediction.

Detailed audit:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```

Rev. 7 and earlier revisions remain preserved historical provenance.'''
s=replace_between(s,'## Rev. 7 status','## Priority and feasibility blockers',cursec,str(p))
old_order='7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;\n10. the exact extracted current source.'
new_order='7. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n10. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;\n11. the exact extracted current source.'
s=must_replace(s,old_order,new_order,str(p),1)
write(p,s)

# Live state
p=EXP/'CURRENT_STATE_LIVE.md'; s=read(p)
s=must_replace(s,'**Status:** anonymous Rev. 7 manuscript + adversarial hardening.','**Status:** anonymous Rev. 8 manuscript + adversarial hardening.',str(p),1)
sec1=r'''## 1. Canonical manuscript

The current approved manuscript baseline is the anonymous **26-page Rev. 8**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 8 was first judged against the established Rev. 7 preservation baseline in PR #13. Only after the manuscript-preservation and privacy gates passed was it made canonical.

Exact source:

```text
MANUSCRIPT_REV8_ANON_2026-08-11.tex
SHA-256 = 28eb3de954d50046f177e06e4b54eb1812414c03a1d53a933904f99fb3c49ba9
bytes = 81816
lines = 1023
compiled pages = 26
sections = 12
subsections = 18
bibliography items = 19
equation environments = 107
author/PDF metadata = Anonymous
```

Hash-verified recovery uses seven Rev. 8 snapshot parts under `manuscript_history/` and `python tools/extract_manuscript_baseline.py`.

Rev. 7, Rev. 6, Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*` remain historical provenance only.'''
s=replace_between(s,'## 1. Canonical manuscript','## 2. Current paper hierarchy',sec1,str(p))
sec2=r'''## 2. Current paper hierarchy

```text
spectral wavelength
-> calibrated internal source coordinate
-> Shockley-Ramo-aware spatial first differences
-> four-color one-mode closure in multiplier q
-> branch-controlled continuous exponent gamma
-> if rank one fails: six-color Hankel rank-at-most-two determinant test
-> if rank two passes: recurrence-parameter resolution / conditioning
-> branch-free RF root invariants where available
-> branch/permutation-controlled physical root laws
-> higher ordinary finite rank if needed
-> mechanism assignment only after ordinary alternatives are excluded
```

The central one-mode terminal-current null remains

```math
(J_2-J_1)^2=(J_1-J_0)(J_3-J_2).
```

For the six-color rung, the unconditional rank-at-most-two null is the `3x3` Hankel determinant `det(H)=0`. The adjacent-minor witness

```math
W_m=d_md_{m+2}-d_{m+1}^2=ab(q_1q_2)^m(q_1-q_2)^2
```

remains useful only after the model-order test and appropriate nondegeneracy checks. The old scalar closure `W1^2=W0W2` is not a general model-order null because it equals `-d2 det(H)`.

The four-color multiplier null is branch-independent. Physical inversion is not: `q=e^{-gamma h}` admits spatial-log aliases and therefore requires independent branch control.'''
s=replace_between(s,'## 2. Current paper hierarchy','## 3. Rev. 7 adversarial corrections — canonical',sec2,str(p))
sec3=r'''## 3. Rev. 8 adversarial corrections — canonical

### Review discipline

Adversarial reviews are **attack vectors, not authority**. Independently verify the mathematical premise, physical regime, numerics, and scholarship before accepting, narrowing, rejecting, or marking an objection out of scope.

### Correct rank-two model-order null

The Rev. 7 six-color minor closure had a genuine blind component:

```math
W_1^2-W_0W_2=-d_2 det(H).
```

Therefore sequences with `d2=0` could satisfy the old scalar closure even at Hankel rank three. Rev. 8 replaces the unconditional model-order test by `det(H)=0` and adds the corresponding covariance-aware complex residual before parameter recovery.

Operational order:

```text
rank one rejected
-> rank at most two tested
-> rank-two parameters resolved
-> physical law tested
```

### Corrected weighting-field baseline

For the current finite-kernel transport model, a 1% linear weighting-field variation gives approximately:

```text
100 MHz -> 0.002947 deg
500 MHz -> 0.012140 deg
1 GHz   -> 0.010007 deg
```

The variations that place the false phase at 10% of the worked gradient target are approximately `0.757% / 0.881% / 1.961%`. The older prose values were stale; the referee's simple rescale of those stale values was not adopted.

### Differential recombination verification

The graded low-injection recombination correction remains about `3.8e-8 / 1.85e-7 / 3.45e-7 degree` at 100 / 500 / 1000 MHz. It is now checked by subtracting independently solved graded and matched-homogeneous cases in both finite-difference and adaptive-shooting implementations. The differential results agree within about `3e-9 degree` across tested environments. The coarser `1e-5 degree` absolute solver comparison is not claimed as validation of this tiny subtraction.

### HgCdTe force and DOS boundary

The electron-affinity relation anchors the composition-induced conduction-band force term only. It does not determine the self-consistent electrostatic field or total device drift. The worked calculation therefore remains a conditional composition-band-edge stress.

Under `m* proportional to Eg`, the DOS velocity is significant: `|v_DOS|/v_field ~= 8.8--18.3%`. The `alpha_DOS` sweep changes the 100-MHz closure from about `-0.01861 degree` at `alpha=0` to `-0.02349 degree` at `alpha=1.5`; the headline `alpha=1` result is `-0.02202 degree`.

### Two-carrier DC degeneracy

For nearly lossless electron-hole transport, integrated DC Shockley--Ramo path dependence can cancel, making the total DC sequence nearly depth-independent. Species-specific tracking can therefore require two or more nonzero RF frequencies even though the general recombining two-root theory remains valid.

Detailed Rev. 8 records:

```text
REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md
numerics/rev8_review_regression.py
```'''
s=replace_between(s,'## 3. Rev. 7 adversarial corrections — canonical','## 4. Earlier Rev. 4/5 corrections remain mandatory',sec3,str(p))
s=must_replace(s,'## 4. Earlier Rev. 4/5 corrections remain mandatory','## 4. Earlier Rev. 4/5/6/7 corrections remain mandatory',str(p),1)
s=must_replace(s,'Rev. 6 retains all prior hardening, especially:','Rev. 8 retains all prior hardening, especially:',str(p),1)
s=must_replace(s,'rank-at-most-two precision','rank-at-most-two precision plus the Rev. 8 Hankel-determinant model-order correction',str(p),1)
sec5=r'''## 5. Current HgCdTe conditional baseline

For the illustrative 7.6 um / 300 K graded-HgCdTe stress:

```text
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
```

The current literature-anchored composition-band-edge force uses the 2025 electron-affinity relation and `xi_e~0.666--0.695`; this anchors that band-edge term, not the total self-consistent drift.

The finite-width gradient-sensitive four-color phase remains approximately:

```text
100 MHz -> -0.0220167 deg
250 MHz -> -0.0546244 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

The DOS/effective-mass contribution is a material-model uncertainty: in the retained reduced prescription it is about 8.8--18.3% of the field-driven velocity, and removing it changes the worked closure by roughly 15%.

The same-optics homogeneous subtraction remains part of the covariance budget; its nominal phase is about 17.3--19.8% of the quoted excess over 100 MHz--1 GHz and its uncertainty must be modeled rather than assumed zero.

The nonaffine-coordinate requirement remains about 4.5 nm RMS. The independent irregular spectral-phase stress remains about `1.88e-4 degree` at 100 MHz and `1.71e-3 degree` at 1 GHz. These are design requirements, not demonstrated calibration performance.

The graded 5-us-anchored differential-recombination sensitivity changes the closure by less than `4e-7 degree`; the dedicated cross-solver subtraction agrees within about `3e-9 degree` across tested environments.'''
s=replace_between(s,'## 5. Current HgCdTe conditional baseline','## 6. Separate realistic-geometry hardening result',sec5,str(p))
s=must_replace(s,'current Rev. 7 1-D gradient target','current Rev. 8 1-D gradient target',str(p),1)
s=must_replace(s,'7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;',
 '7. `REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n10. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;',str(p),1)
write(p,s)

# README
p=ROOT/'README.md'; s=read(p)
status=r'''## Manuscript status

The current approved baseline is the anonymous **26-page Rev. 8**:

```text
Spectral-depth closure tests for falsifying photocarrier transport from Shockley--Ramo current
```

Rev. 8 was validated against Rev. 7 before canonicalization. The central four-color theorem and branch-qualified inversion remain intact. The main new correction is a genuine six-color algebra fix: the unconditional rank-at-most-two model-order null is the full `3x3` Hankel determinant, because the older minor closure also vanished spuriously at `d2=0`.

Rev. 8 also adds the missing noisy rank-two determinant test, reconciles weighting-field numerics, validates the tiny recombination subtraction differentially, separates composition-band-edge force from total drift, quantifies DOS/effective-mass sensitivity, and states the nearly lossless two-carrier DC degeneracy.

The exact source is stored as a hash-verified anonymous seven-part snapshot. Older revisions remain provenance only.

Start here:

1. [`AGENTS.md`](AGENTS.md)
2. [`MANUSCRIPT_CURRENT.md`](experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md)
3. [`MANUSCRIPT_BASELINE.md`](experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md)
4. [`MANUSCRIPT_PRESERVATION_PROTOCOL.md`](experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md)
5. [`CURRENT_STATE_LIVE.md`](experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md)
6. [`REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
7. [`REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
8. [`REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md)
9. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)'''
s=replace_between(s,'## Manuscript status','## Manuscript safety rule',status,str(p))
s=must_replace(s,'-> six-color/higher finite-rank model-order tests if needed\n-> rank-two parameter-resolution check',
 '-> six-color Hankel rank-at-most-two determinant test if rank one fails\n-> rank-two parameter-resolution check if the determinant null passes\n-> higher finite-rank tests if rank two fails',str(p),1)
ranksec=r'''## Rev. 8 rank-two model-order boundary

The six-color rung now separates **existence of a second mode**, **rank-at-most-two model order**, and **parameter resolution**.

For five first differences, the unconditional rank-at-most-two null is

```math
det(H)=0,
```

for the `3x3` Hankel matrix of `d0...d4`. The older identity obeys

```math
W1^2-W0W2=-d2 det(H),
```

so it is not an unconditional model-order null. Adjacent minors remain useful after the determinant test for separation, conditioning, and recurrence recovery.

The live hierarchy is:

```text
rank one rejected
-> rank at most two tested
-> two-mode parameters resolved
-> physical root law tested
```

The Rev. 6 covariance result for recurrence parameters remains mandatory: statistically detecting a second mode does not guarantee accurate roots.'''
s=replace_between(s,'## Rev. 6 post-detection conditioning boundary','## Low-RF observation-mode boundary',ranksec,str(p))
hg=r'''## HgCdTe status

The graded-HgCdTe calculation remains a **conditional composition-band-edge transport stress**, not a calibrated detector prediction. The 2025 electron-affinity relation anchors the composition-induced electron band-edge force and gives `xi_e~0.666--0.695`; it does **not** anchor the omitted self-consistent electrostatic field or total carrier drift.

The finite-width phase remains about `-0.0220 / -0.1064 / -0.1942 degree` at 100 / 500 / 1000 MHz.

Rev. 8 exposes the retained DOS/effective-mass approximation as a significant uncertainty: `|v_DOS|/v_field` is about 8.8--18.3% across the layer, and an `alpha_DOS` sensitivity moves the worked closure appreciably. A deliberately steep 5-us-anchored differential-recombination stress remains negligible on the gradient-signal scale, with the tiny subtraction cross-checked independently to about `3e-9 degree` between implementations across tested environments.

The corrected 1% weighting-field false phases are `0.002947 / 0.012140 / 0.010007 degree` at 100 / 500 / 1000 MHz. The allowable variation for a 10%-of-target contamination is `0.757% / 0.881% / 1.961%`.

The same-optics homogeneous subtraction remains part of the covariance budget rather than assumed exact.'''
s=replace_between(s,'## HgCdTe status','## Prior-art boundary',hg,str(p))
write(p,s)

# AGENTS: narrow but strong recovery locks
p=ROOT/'AGENTS.md'; s=read(p)
for old,new in [
 ('**Current mode:** **anonymous Rev. 7 working theory manuscript + adversarial revision;','**Current mode:** **anonymous Rev. 8 working theory manuscript + adversarial revision;'),
 ('canonical manuscript is the anonymous 24-page Rev. 7, validated against the previous Rev. 6 baseline','canonical manuscript is the anonymous 26-page Rev. 8, validated against the previous Rev. 7 baseline'),
 ('The immutable Rev. 7 source','The immutable Rev. 8 source'),
 ('**REV. 7 submission blockers:**','**REV. 8 submission blockers:**'),
 ('## 6. Rev. 4/5/6 mathematical boundary conditions — never regress','## 6. Rev. 4/5/6/7/8 mathematical boundary conditions — never regress')]:
    s=must_replace(s,old,new,str(p))
# current source list additions
s=must_replace(s,'- `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`',
 '- `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n- `experiments/01-vanishing-absorber/MANUSCRIPT_REV8_PRESERVATION_REPORT_2026-08-11.md`\n- `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`',str(p),1)
# pre-edit order
s=must_replace(s,'6. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n7. `experiments/01-vanishing-absorber/REV4_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n8. the exact verified manuscript source recovered with `python tools/extract_manuscript_baseline.py` when manuscript work is required.',
 '6. `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n7. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n8. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n9. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 as earlier context;\n10. the exact verified manuscript source recovered with `python tools/extract_manuscript_baseline.py` when manuscript work is required.',str(p),1)
# canonical reading order insert Rev8 before Rev7
s=must_replace(s,'6. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n7. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`',
 '6. `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n7. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n8. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`',str(p),1)
g3=r'''### Gedanken III — six colors and higher order

If the one-mode closure fails, use six source coordinates and test the **rank-at-most-two model itself** before interpreting two roots.

For

```math
d_m=a q_1^m+b q_2^m,
```

the adjacent minors still satisfy

```math
W_m=d_md_{m+2}-d_{m+1}^2
=ab(q_1q_2)^m(q_1-q_2)^2.
```

But **REV. 8 correction:** the unconditional six-color model-order null is the full `3x3` Hankel determinant

```math
det(H)=0,
```

not `W1^2=W0W2`, because

```math
W1^2-W0W2=-d2 det(H).
```

The old scalar closure therefore has a spurious `d2=0` branch. Never resurrect it as an unconditional rank-two test.

Mandatory operational order:

```text
rank one rejected
-> rank at most two tested with det(H)
-> two-mode recurrence parameters resolved
-> physical root law tested
-> higher ordinary finite rank if rank two fails
```

Adjacent minors remain useful for mode separation, conditioning, and recurrence recovery when nondegenerate. A covariance-aware determinant test is required in noise before two-root interpretation. Failure of rank two does **not** imply exotic transport; continue through higher ordinary finite-rank mechanisms first.'''
s=replace_between(s,'### Gedanken III — six colors and higher order','---\n\n## 5. Observable discipline — mandatory',g3,str(p))
# Add current explicit lock after review-discipline concept near top
anchor='The repository follows the physics rather than a predetermined paper. Failed conjectures, observable corrections, numerical corrections, counterexamples, and prior-art collisions are part of the result.\n'
insert=anchor+'\n**Rev. 8 model-order lock:** the old six-color scalar closure `W1^2=W0W2` is superseded as an unconditional rank-two null because `W1^2-W0W2=-d2 det(H)`. Use the full `3x3` Hankel determinant `det(H)=0` to test rank at most two before recovering two roots.\n'
s=must_replace(s,anchor,insert,str(p),1)
write(p,s)

print('Rev8 canonical recovery/state files updated.')
