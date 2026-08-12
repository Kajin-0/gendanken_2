#!/usr/bin/env python3
from pathlib import Path
p=Path('AGENTS.md')
s=p.read_text(encoding='utf-8')

def one(old,new):
    global s
    n=s.count(old)
    if n!=1: raise SystemExit(f'expected one occurrence, found {n}: {old[:80]!r}')
    s=s.replace(old,new)

def between(start,end,new):
    global s
    i=s.find(start); j=s.find(end,i+len(start))
    if i<0 or j<0: raise SystemExit(f'missing section boundary {start!r} -> {end!r}')
    s=s[:i]+new.rstrip()+'\n\n'+s[j:]

one('**Current mode:** **anonymous Rev. 8 working theory manuscript + adversarial revision; strongest result is a Shockley-Ramo-aware spectral-depth closure hierarchy for falsifying photocarrier transport models; HgCdTe is a conditional scaling/stress example; priority remains unproven**',
    '**Current mode:** **anonymous Rev. 9 working theory manuscript + adversarial revision; strongest result is a Shockley-Ramo-aware spectral-depth closure hierarchy with translated-kernel and calibrated arbitrary-kernel one-mode tests; HgCdTe is a conditional scaling/stress example; priority remains unproven**')
one('**Rev. 8 model-order lock:** the old six-color scalar closure `W1^2=W0W2` is superseded as an unconditional rank-two null because `W1^2-W0W2=-d2 det(H)`. Use the full `3x3` Hankel determinant `det(H)=0` to test rank at most two before recovering two roots.',
    '**Rev. 9 rank-two lock:** retain the Rev. 8 full `3x3` Hankel determinant `det(H)=0` as the unconditional rank-at-most-two null, then classify the resolved recurrence by `Delta_q=S^2-4P`. `Delta_q=0` with nonzero rank-two contrast is the confluent sequence `(A+Bm)q^m`, not two independent exponentials. Physical testing must be multiplicity-aware.')
one('**A working manuscript exists. The canonical manuscript is the anonymous 26-page Rev. 8, validated against the previous Rev. 7 baseline before canonicalization. It is not yet submission-ready; the exact closest-source priority audit and experimental-feasibility attack remain open.**',
    '**A working manuscript exists. The canonical manuscript is the anonymous 28-page Rev. 9, validated against the previous Rev. 8 baseline before canonicalization. It is not yet submission-ready; the exact closest-source priority audit, calibration feasibility, and combined-physics validation remain open.**')

new_read='''Before any manuscript edit, read these files in order:

1. root `PRIVACY_PROTOCOL.md`;
2. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`;
3. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`;
4. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
5. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`;
6. `experiments/01-vanishing-absorber/REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;
7. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`;
8. `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;
9. earlier adversarial records as historical context;
10. the exact verified manuscript source recovered with `python tools/extract_manuscript_baseline.py` when manuscript work is required.'''
between('Before any manuscript edit, read these files in order:','**Do not treat',new_read)
one('The immutable Rev. 8 source is stored inside the repository as hash-verified split snapshot parts under `experiments/01-vanishing-absorber/manuscript_history/`. The extractor verifies both the compressed snapshot and decompressed source before writing `MANUSCRIPT_CURRENT.tex`.',
    'The immutable Rev. 9 source is stored inside the repository as hash-verified split snapshot parts under `experiments/01-vanishing-absorber/manuscript_history/`. The extractor verifies both the compressed snapshot and decompressed source before writing `MANUSCRIPT_CURRENT.tex`.')
one('- `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`',
    '- `experiments/01-vanishing-absorber/REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n- `experiments/01-vanishing-absorber/MANUSCRIPT_REV9_PRESERVATION_REPORT_2026-08-11.md`\n- `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`\n- `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`')
one('**REV. 8 submission blockers:** the closest-looking 2024 graded-HgCdTe paper has verified bibliographic metadata but its exact full text has not yet been lawfully recovered and audited. That exact-source audit remains OPEN and blocks submission-level priority/novelty claims. Related-paper searches do not substitute for reading it.',
    '**REV. 9 submission blockers:** spectral-depth transport probing, wavelength-dependent RF sensing, and finite-exponential/Hankel identification are established prior-art lineages. The exact closest 2024 graded-HgCdTe paper still requires a direct technical full-text comparison. That exact-source audit remains OPEN and blocks submission-level priority/novelty claims; metadata and related-paper searches do not substitute for reading it.')

new_order='''## 3. Canonical reading order

1. `PRIVACY_PROTOCOL.md`
2. `experiments/01-vanishing-absorber/MANUSCRIPT_CURRENT.md`
3. `experiments/01-vanishing-absorber/MANUSCRIPT_BASELINE.md`
4. `experiments/01-vanishing-absorber/MANUSCRIPT_PRESERVATION_PROTOCOL.md`
5. `experiments/01-vanishing-absorber/CURRENT_STATE_LIVE.md`
6. `experiments/01-vanishing-absorber/REV9_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
7. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER_REV9_ADVERSARIAL_ADDENDUM_2026-08-11.md`
8. `experiments/01-vanishing-absorber/REV8_ADVERSARIAL_CORRECTIONS_2026-08-11.md`
9. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and earlier adversarial records as historical context
10. `experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md`
11. `experiments/01-vanishing-absorber/REALISTIC_GEOMETRY_CLOSURE_STRESS.md` when relevant
12. `experiments/01-vanishing-absorber/MANUSCRIPT_BLUEPRINT_ADVERSARIAL.md`
13. `experiments/01-vanishing-absorber/SUPPLEMENTARY_MATERIAL.md`
14. supporting theorem/result files only as needed.

When manuscript work is requested, recover the exact verified `MANUSCRIPT_CURRENT.tex` before editing it. Older drafts and snapshots remain provenance only.'''
between('## 3. Canonical reading order','---\n\n## 4. Current paper spine',new_order)

one('Three source coordinates identify one spatial multiplier `q`. The fourth is a parameter-free null measurement.',
'''Three source coordinates identify one spatial multiplier `q`. The fourth is a parameter-free null measurement **for the rigid translated-kernel construction**.

**REV. 9 optical-kernel qualification:** if the channel generation kernels are independently calibrated but not rigid translations, define `M_m(r)=int g_m(z) exp(rz) dz`; the homogeneous one-mode model becomes `J_m=A+B M_m(r)`. Four channels still overdetermine the common root `r`, but the null is then a kernel-aware nonlinear consistency test rather than the simple geometric identity.''')

new_g3='''### Gedanken III — six colors and higher order

If the one-mode test fails, use six source coordinates and test the **rank-at-most-two model itself** before interpreting roots.

The unconditional model-order null remains the Rev. 8 `3x3` Hankel determinant

```math
det(H)=0.
```

The old scalar closure must not be resurrected because

```math
W_1^2-W_0W_2=-d_2 det(H).
```

After rank two is accepted and recurrence parameters `S,P` are resolved, Rev. 9 requires the discriminant

```math
Delta_q=S^2-4P.
```

Classification:

```text
Delta_q != 0
-> distinct-root rank two

Delta_q = 0 with nonzero rank-two contrast
-> confluent/repeated-root rank two
-> d_m=(A+Bm)q^m
```

For distinct roots the adjacent-minor identity remains useful for separation, conditioning, and recurrence recovery. Do not obtain the confluent case by setting `q1=q2` in the distinct-root amplitude formula; the multiplicity-aware basis is different. A repeated root can itself be physical for a second-order model.

Mandatory operational order:

```text
rank one rejected
-> rank at most two tested with det(H)
-> recurrence parameters resolved
-> distinct/confluent branch classified
-> multiplicity-aware physical root law tested
-> higher ordinary finite rank if rank two fails
```

Near exact rank one the determinant statistic is nonregular because all `2x2` cofactors vanish. Use null-constrained Monte Carlo / parametric bootstrap when first-order covariance linearization is inadequate. Failure of rank two does **not** imply exotic transport; continue through higher ordinary finite-rank mechanisms first.'''
between('### Gedanken III — six colors and higher order','---\n\n## 5. Observable discipline — mandatory',new_g3)
one('## 6. Rev. 4/5/6/7/8 mathematical boundary conditions — never regress','## 6. Rev. 4/5/6/7/8/9 mathematical boundary conditions — never regress')
anchor='## 6. Rev. 4/5/6/7/8/9 mathematical boundary conditions — never regress\n'
insert='''\n### Rev. 9 calibration and experimental-null boundary\n\nA common spatial scale error cancels from model-order closure but biases dimensional transport coefficients: `D_cal=c^2D`, `w_cal=cw`, `kappa_cal=kappa`. Keep this absolute/common-scale budget separate from nonaffine coordinate errors.\n\nFor evolving wavelength-dependent kernels, an uncorrected geometric four-color failure rejects the combined homogeneous-transport + optical-kernel idealization. To isolate transport experimentally, use independently constrained kernels or the Rev. 9 kernel-aware null. In graded HgCdTe, the same `x(z)` controls both optical depth mapping and the modeled composition-band-edge force, so it is a shared nuisance unless independently measured.\n'''
if anchor not in s: raise SystemExit('missing section 6 anchor')
s=s.replace(anchor,anchor+insert,1)

p.write_text(s,encoding='utf-8')
print('PASS: AGENTS Rev9 canonical state patch applied')
