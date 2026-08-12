#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def must_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing expected text in {label}: {old[:120]!r}")
    return text.replace(old, new)


def replace_between(text: str, start: str, end: str, new_block: str, label: str) -> str:
    i = text.find(start)
    j = text.find(end)
    if i < 0 or j < 0 or j <= i:
        raise SystemExit(f"cannot locate section markers in {label}: {start!r} -> {end!r}")
    return text[:i] + new_block.rstrip() + "\n\n" + text[j:]


# 1. Machine manifest.
p = EXP / "MANUSCRIPT_BASELINE.json"
data = json.loads(read(p))
data.update({
    "status": "canonical_rev7_literature_anchored_hgcdte_and_measurement_framing",
    "source_filename": "MANUSCRIPT_REV7_ANON_2026-08-11.tex",
    "source_sha256": "9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8",
    "source_bytes": 75182,
    "source_lines": 963,
    "compiled_pages": 24,
    "author": "Anonymous",
    "section_count": 12,
    "subsection_count": 18,
    "bibliography_item_count": 19,
    "equation_environment_count": 102,
    "privacy_default": "anonymous",
    "identity_release_required": True,
})
write(p, json.dumps(data, indent=2) + "\n")

# 2. Exact extractor.
p = ROOT / "tools" / "extract_manuscript_baseline.py"
t = read(p)
for old, new in [
    ("immutable anonymous Rev. 6 manuscript baseline", "immutable anonymous Rev. 7 manuscript baseline"),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part*", "MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part*"),
    ("2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4", "9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8"),
    ("aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e", "8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b"),
    ("EXPECTED_LINES = 924", "EXPECTED_LINES = 963"),
]:
    t = must_replace(t, old, new, str(p))
write(p, t)

# 3. Canonical baseline narrative.
p = EXP / "MANUSCRIPT_BASELINE.md"
t = read(p)
for old, new in [
    ("CANONICAL REV. 6 MANUSCRIPT BASELINE", "CANONICAL REV. 7 MANUSCRIPT BASELINE"),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex", "MANUSCRIPT_REV7_ANON_2026-08-11.tex"),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part", "MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part"),
    ("2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4", "9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8"),
    ("aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e", "8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b"),
    ("bytes: 67837", "bytes: 75182"),
    ("lines: 924", "lines: 963"),
    ("compiled pages: 22", "compiled pages: 24"),
    ("bibliography items: 13", "bibliography items: 19"),
    ("\\begin{equation} environments: 99", "\\begin{equation} environments: 102"),
    ("bytes: 23386", "bytes: 26026"),
    ("Rev. 6 was first validated against the established Rev. 5 baseline in PR #8. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 21 of 863 established Rev. 5 lines were changed or removed (~2.43%); no section, subsection, reference, or unrelated derivation was deleted.",
     "Rev. 7 was first validated against the established Rev. 6 baseline in PR #11. Only after the preservation and privacy gates passed were canonical pointers updated. The revision is surgical: 63 of 924 established Rev. 6 lines were changed or removed (~6.82%); no section, subsection, reference, or unrelated derivation was deleted."),
    ("Anonymous Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved", "Anonymous Rev. 6, Rev. 5, Rev. 4, and Rev. 3 snapshots remain preserved"),
    ("must not override Rev. 6", "must not override Rev. 7"),
]:
    t = must_replace(t, old, new, str(p))
newsec = r'''## Rev. 7 corrections now canonical

Rev. 7 preserves the central four-color theorem, branch-qualified inversion, finite-rank hierarchy, post-detection conditioning, singular weighting-field limit, and earlier nuisance analysis. It changes only points that survived independent checking of the post-Rev. 6 hostile review:

- the one- and two-exponential identities are explicitly placed in the classical **Prony / ESPRIT / matrix-pencil** lineage; neither the geometric identity nor the Hankel/Casoratian minor is claimed as new;
- the candidate contribution is narrowed to the detector-specific chain `calibrated spectral generation depth -> Shockley--Ramo terminal current -> spatial differencing -> classical finite-exponential model-order tests -> cross-RF physical root constraints`;
- the former arbitrary `xi=1` HgCdTe headline force is replaced by the 2025 electron-affinity relation `chi(x)=5.32+0.45x-E_g(x,300 K)` and therefore `E_drive^grad=|(dE_g/dx-0.45) dx/dz|`;
- the corresponding local electron-driving fraction `xi_e=1-0.45/(dE_g/dx)` is about **0.666--0.695** across the worked composition profile;
- the finite-width gradient-sensitive phase becomes approximately **-0.0220167, -0.1064448, -0.1942321 degree** at 100 MHz, 500 MHz, and 1 GHz;
- a deliberately steep spatially varying small-signal recombination stress anchored to a 5-us low-injection scale changes those closures by only about `4e-8` to `4e-7 degree` over 0.1--1 GHz in the stated model; this is a sensitivity result, not a universal Auger claim;
- the one-dimensional polynomial `E_w(z)` remains an exact surrogate theorem but is explicitly not a generic finite-pixel electrostatic solution; finite electrodes can have both axial and lateral weighting structure;
- the hierarchy is explicitly structural model-selection logic, not a globally calibrated sequential hypothesis test; quoted significance levels remain conditional on the rung being tested;
- a concrete common-reference/interleaved-wavelength coherent measurement architecture is stated, while experimental feasibility remains **OPEN**, not demonstrated;
- all HgCdTe conditioning, SNR, coordinate, phase, weighting-field, and baseline-covariance resource numbers are propagated to the literature-anchored transport scale.

Current key resource values include a conditioning optimum near **5.85 GHz**, 3-sigma current-step requirements of **90.9 / 82.9 / 77.1 / 71.4 dB** at 100 / 250 / 500 / 1000 MHz, nonaffine coordinate RMS near **4.5 nm**, and irregular channel-phase RMS of about **1.88e-4 / 9.15e-4 / 1.71e-3 degree** at 100 / 500 / 1000 MHz.

Detailed records:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```

The adversarial review itself is not authority. Its objections are retained as attack vectors; each is accepted, narrowed, or rejected only after independent mathematical, physical, numerical, or literature checking.'''
t = replace_between(t, "## Rev. 6 corrections now canonical", "## Priority and feasibility boundary", newsec, str(p))
write(p, t)

# 4. Current pointer.
p = EXP / "MANUSCRIPT_CURRENT.md"
t = read(p)
for old, new in [
    ("anonymous **22-page Rev. 6**", "anonymous **24-page Rev. 7**"),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex", "MANUSCRIPT_REV7_ANON_2026-08-11.tex"),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex.gz.b64.part", "MANUSCRIPT_REV7_ANON_2026-08-11.tex.gz.b64.part"),
    ("2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4", "9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8"),
    ("aa7ab9e3271599bf9cdaa5ef37618cb2b9757ee0e08c867303a83e06e61adb8e", "8056b7cf995e1d2985a6c5aaf6d6016c8d2714dcfe3e1e2d391fb0169716038b"),
    ("bytes = 67837", "bytes = 75182"),
    ("lines = 924", "lines = 963"),
    ("pages in matching compiled PDF = 22", "pages in matching compiled PDF = 24"),
    ("Rev. 5, Rev. 4, and Rev. 3 remain preserved", "Rev. 6, Rev. 5, Rev. 4, and Rev. 3 remain preserved"),
]:
    t = must_replace(t, old, new, str(p))
cursec = r'''## Rev. 7 status

Rev. 7 is a surgical response to the post-Rev. 6 hostile review. The report was treated as an attack list rather than authority: objections were independently checked and only scientifically useful corrections were adopted.

The core hierarchy is unchanged:

```text
rank detection
-> parameter resolution
-> physical root-law discrimination
```

Rev. 7 adds the following locks:

- classical Prony/ESPRIT/matrix-pencil algebra is cited explicitly and is **not** claimed as new;
- the proposed distinction is the calibrated spectral-depth + Shockley--Ramo + spatial-difference + classical finite-rank + cross-RF physical-constraint construction;
- the HgCdTe worked stress now uses the electron-affinity-anchored driving band edge `E_drive^grad=|(dE_g/dx-0.45) dx/dz|`, giving `xi_e~0.666--0.695`, instead of using `xi=1` as the headline baseline;
- the finite-width closure excess is about `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz;
- an intentionally steep 5-us-anchored spatial differential-recombination stress changes the closure by less than `4e-7 degree` over 0.1--1 GHz in this conditional model; do not generalize that result to high-injection, depleted, or arbitrary devices;
- the 1-D weighting-field theorem remains an effective axial observation-operator surrogate, not a generic finite-electrode electrostatic theorem;
- the hierarchy is structural model-selection logic; per-rung significance does not constitute a globally calibrated sequential test;
- a common-RF-reference, interleaved-wavelength, reference-photodiode/coherent-receiver architecture is specified as a plausible measurement path, but its residual calibration performance is not demonstrated.

Propagated design scales now include:

```text
conditioning optimum:             5.85 GHz
3-sigma current-step SNR:         90.9 / 82.9 / 77.1 / 71.4 dB at 100/250/500/1000 MHz
nonaffine coordinate RMS:         ~4.5 nm at 100--1000 MHz
irregular channel phase RMS:      1.88e-4 / 9.15e-4 / 1.71e-3 deg at 100/500/1000 MHz
1-D weighting change for <10%:    0.757% / 0.881% / 1.961%
same-optics baseline/excess:      17.3% / 17.9% / 19.8%
```

Detailed audit:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```

Rev. 6 and earlier revisions remain preserved historical provenance.'''
t = replace_between(t, "## Rev. 6 status", "## Priority and feasibility blockers", cursec, str(p))
old_order = "7. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. the exact extracted current source."
new_order = "7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;\n10. the exact extracted current source."
t = must_replace(t, old_order, new_order, str(p))
write(p, t)

# 5. Live state.
p = EXP / "CURRENT_STATE_LIVE.md"
t = read(p)
for old, new in [
    ("anonymous Rev. 6 manuscript + adversarial hardening", "anonymous Rev. 7 manuscript + adversarial hardening"),
    ("anonymous **22-page Rev. 6**", "anonymous **24-page Rev. 7**"),
    ("Rev. 6 was first judged against the established Rev. 5 preservation baseline. Only after the manuscript-preservation and privacy gates passed was it made canonical.", "Rev. 7 was first judged against the established Rev. 6 preservation baseline in PR #11. Only after the manuscript-preservation and privacy gates passed was it made canonical."),
    ("MANUSCRIPT_REV6_ANON_2026-08-11.tex", "MANUSCRIPT_REV7_ANON_2026-08-11.tex"),
    ("2f8f6c22b64d89f7237a3053663fc500f97574c75a0c60489bb7f19925f112b4", "9c7fa95eb714b32839760d47f7277aaad795589c44012e2324566b6e6cb9d2f8"),
    ("bytes = 67837", "bytes = 75182"),
    ("lines = 924", "lines = 963"),
    ("compiled pages = 22", "compiled pages = 24"),
    ("bibliography items = 13", "bibliography items = 19"),
    ("equation environments = 99", "equation environments = 102"),
    ("six Rev. 6 snapshot parts", "six Rev. 7 snapshot parts"),
    ("Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*`", "Rev. 6, Rev. 5, Rev. 4, Rev. 3, and `MANUSCRIPT_DRAFT.*`"),
]:
    t = must_replace(t, old, new, str(p))
rev7state = r'''## 3. Rev. 7 adversarial corrections — canonical

### Review discipline

Adversarial reviews are **attack vectors, not authority**. For every criticism: independently verify the mathematical premise, physical regime, numerics, and scholarship; then accept, narrow, reject, or mark out-of-scope. Do not alter a correct result merely because a referee states an objection strongly, and do not defend the manuscript reflexively when an objection is valid.

### Classical exponential-sum lineage

The one- and two-mode spatial identities belong to classical finite-exponential algebra. Rev. 7 explicitly cites Prony (1795), ESPRIT (1989), and the matrix-pencil method (1990). The manuscript does not claim those algebraic identities as new.

The candidate distinction is narrower:

```text
calibrated spectral generation depth
-> Shockley-Ramo terminal-current observable
-> spatial differencing
-> classical finite-exponential model-order tests
-> branch-controlled / branch-free RF physical root constraints
```

Priority remains unproven.

### Literature-anchored HgCdTe force

The headline HgCdTe stress no longer uses the free `xi=1` normalization. A 2025 electron-affinity relation gives

```math
chi(x)=5.32+0.45x-E_g(x,300 K),
```

so the modeled electron-driving band-edge gradient is

```math
E_drive^grad(z)=|(dE_g/dx-0.45) dx/dz|.
```

For the worked `x=0.55 -> 0.32` profile,

```math
xi_e=1-0.45/(dE_g/dx) \simeq 0.666--0.695.
```

The resulting finite-width gradient-sensitive closure excess is approximately:

```text
100 MHz -> -0.0220167 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

The former constant-`xi` calculations remain sensitivity stresses, not the current headline material baseline.

### Spatial recombination stress

A nonlinear microscopic Auger law can be linearized around an operating point into a differential small-signal recombination rate. The relevant graded-material question is therefore whether that differential rate varies enough with depth to mimic the closure.

Rev. 7 tests an intentionally steep profile anchored at `5 us`:

```math
tau_gr(z)=5 us exp[(E_g(z)-E_g(x=0.325))/(k_B T)].
```

With a transit-weighted matched homogeneous baseline, its additional closure shift is only about `3.8e-8 / 1.8e-7 / 3.5e-7 degree` at 100 / 500 / 1000 MHz in the specified model. This is **CHECKED / CONDITIONAL**, not a universal statement about high-injection, depleted, or arbitrary HgCdTe devices.

### Observation operator and statistics

The one-dimensional polynomial `E_w(z)` theory remains an exact effective axial surrogate. It is not a generic finite-pixel electrostatic theorem; real finite electrodes can produce both axial and lateral weighting structure.

The hierarchy is structural model-selection logic. Per-rung covariance statistics remain conditional, and reusing the same noisy data for model-order selection and physical-root tests requires selection-aware error control in a full experiment.

### Measurement architecture and propagated resources

Rev. 7 specifies a plausible architecture using one common RF reference, interleaved wavelength acquisition, optical-power/reference-photodiode monitoring, one coherent DUT receiver chain, repeated reference wavelengths, and calibration of the non-common high-curvature spectral residual rather than absolute path delay. This is an architecture, **not demonstrated feasibility**.

Key propagated scales are:

```text
conditioning optimum                         5.85 GHz
K_D at 100 / 500 / 1000 MHz                33.95 / 7.57 / 4.75
weighting-mode rank-two SNR                 108.6 / 81.2 / 70.5 dB
five-color annihilation penalty             42.4 / 28.7 / 23.2 dB
3-sigma current-step SNR                    90.9 / 82.9 / 77.1 / 71.4 dB (100/250/500/1000 MHz)
nonaffine coordinate RMS                    4.54 / 4.55 / 4.51 nm
irregular channel phase RMS                 1.88e-4 / 9.15e-4 / 1.71e-3 deg
1-D weighting change for <10% target        0.757% / 0.881% / 1.961%
same-optics homogeneous phase / excess      17.3% / 17.9% / 19.8%
```

Detailed Rev. 7 records:

```text
REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md
MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md
numerics/rev7_review_regression.py
```'''
t = replace_between(t, "## 3. Rev. 6 adversarial corrections — canonical", "## 4. Earlier Rev. 4/5 corrections remain mandatory", rev7state, str(p))
t = must_replace(t, "116.2 / 88.4 / 76.7 dB optimistic equal-mode separation scale", "108.6 / 81.2 / 70.5 dB optimistic equal-mode separation scale", str(p))
t = must_replace(t, "46.3 / 32.3 / 26.4 dB five-color annihilation penalty", "42.4 / 28.7 / 23.2 dB five-color annihilation penalty", str(p))
hg = r'''## 5. Current HgCdTe conditional baseline

For the illustrative 7.6 um / 300 K graded-HgCdTe stress:

```text
mean generation depths = 2.5, 3.0, 3.5, 4.0 um
wavelengths ~ 2.134651, 2.215042, 2.301173, 2.393907 um
```

The current literature-anchored electron-driving force uses the 2025 electron-affinity relation and `xi_e~0.666--0.695`, not the historical `xi=1` headline normalization.

The finite-width gradient-sensitive four-color phase is approximately:

```text
100 MHz -> -0.0220167 deg
250 MHz -> -0.0546244 deg
500 MHz -> -0.1064448 deg
1 GHz   -> -0.1942321 deg
```

These remain conditional theory stresses, not calibrated predictions for a named detector.

The same-optics homogeneous subtraction remains part of the covariance budget; its nominal phase is about **17.3--19.8%** of the quoted excess over 100 MHz--1 GHz and its uncertainty must be modeled rather than assumed zero.

The derived nonaffine-coordinate requirement is about **4.5 nm RMS**. The independent irregular spectral-phase stress is about **1.88e-4 degree at 100 MHz** (about 5.2 fs differential timing) and rises to `1.71e-3 degree` at 1 GHz. These are design requirements, not demonstrated calibration performance.

The graded 5-us-anchored differential-recombination sensitivity changes the closure by less than `4e-7 degree` over the stated RF range in the specified model.'''
t = replace_between(t, "## 5. Current HgCdTe conditional baseline", "## 6. Separate realistic-geometry hardening result", hg, str(p))
t = must_replace(t, "100 MHz -> -0.008841 deg = 0.738 x current 1-D gradient target\n500 MHz -> -0.045827 deg = 0.780 x target\n1 GHz   -> -0.095513 deg = 0.865 x target", "100 MHz -> -0.008841 deg = 0.402 x current Rev. 7 1-D gradient target\n500 MHz -> -0.045827 deg = 0.431 x target\n1 GHz   -> -0.095513 deg = 0.492 x target", str(p))
old_order = "7. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as predecessor context;"
new_order = "7. `REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`;\n8. `REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md` as predecessor context;\n9. `REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md` and Rev. 4 record as earlier context;"
t = must_replace(t, old_order, new_order, str(p))
write(p, t)

# 6. README.
p = ROOT / "README.md"
t = read(p)
for old, new in [
    ("anonymous **22-page Rev. 6**", "anonymous **24-page Rev. 7**"),
    ("Rev. 6 was validated against Rev. 5 before canonicalization. It preserves the complete paper spine and established theorem chain while addressing the latest hostile-review points: post-detection rank-two conditioning, interpretation of the 1-D weighting-field stress, HgCdTe force-partition sensitivity, adjacent OED prior art, two-carrier identifiability, and sequential statistical testing.", "Rev. 7 was validated against Rev. 6 before canonicalization. It preserves the complete paper spine and established theorem chain while adding classical Prony/ESPRIT/matrix-pencil attribution, a literature-anchored HgCdTe electron-driving band edge, a graded differential-recombination stress, propagated resource numbers, and a concrete but still unvalidated measurement architecture."),
    ("6. [`REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md)\n7. [`REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md)\n8. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)", "6. [`REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md)\n7. [`REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md)\n8. [`REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`](experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md)\n9. [`PAPER_CLAIM_LEDGER.md`](experiments/01-vanishing-absorber/PAPER_CLAIM_LEDGER.md)"),
    ("116.2 / 88.4 / 76.7 dB at 100 / 500 / 1000 MHz", "108.6 / 81.2 / 70.5 dB at 100 / 500 / 1000 MHz"),
    ("46.3 / 32.3 / 26.4 dB", "42.4 / 28.7 / 23.2 dB"),
]:
    t = must_replace(t, old, new, str(p))
newhg = r'''## HgCdTe status

The manuscript's graded-HgCdTe calculation remains a **conditional sensitivity/stress construction**, not a calibrated detector prediction. Rev. 7 replaces the historical free `xi=1` headline force with the 2025 electron-affinity relation,

```math
E_{drive}^{grad}(z)=|(dE_g/dx-0.45)(dx/dz)|,
```

which gives a local electron-driving fraction `xi_e~0.666--0.695` over the worked profile. The finite-width gradient-sensitive phase is about `-0.0220 / -0.1064 / -0.1942 degree` at 100 / 500 / 1000 MHz.

A deliberately steep spatial differential-recombination stress anchored to a 5-us low-injection scale shifts those closures by less than `4e-7 degree` over 0.1--1 GHz in the specified model. That is a conditional sensitivity result, not a general claim that Auger or recombination is negligible in all HgCdTe devices.

The same-optics homogeneous subtraction remains part of the covariance budget; its uncertainty is a required modeling resource rather than assumed zero.'''
t = replace_between(t, "## HgCdTe status", "## Prior-art boundary", newhg, str(p))
prior = r'''## Prior-art boundary

Rev. 7 explicitly places the finite-exponential algebra in the classical Prony / ESPRIT / matrix-pencil lineage. It also retains adjacent primary OED work on commercial Ge PN photodiodes (2021) and bias-tunable Ge PIN photodiodes (2024). Those works use wavelength-dependent RF phase/amplitude as sensing observables.

This manuscript's candidate distinction remains narrower: calibrated spectral channels are treated as an internal spatial sequence, mapped through Shockley--Ramo terminal current, and subjected to classical color-count model-order tests plus cross-RF physical root constraints.

This is a boundary statement, **not** evidence of novelty. The exact closest 2024 graded-HgCdTe paper still requires a full-text audit before any submission-level priority claim.'''
t = replace_between(t, "## Prior-art boundary", "## Separate geometry hardening result", prior, str(p))
t = must_replace(t, "Experimental/calibration feasibility and the exact closest-source priority audit remain separate open fronts.", "Experimental/calibration feasibility, the exact closest-source priority audit, and the blind combined-physics challenge remain separate open fronts. Adversarial referee reports are inputs to test, not instructions to follow automatically.", str(p))
write(p, t)

# 7. AGENTS — surgical update and explicit review-discipline lock.
p = ROOT / "AGENTS.md"
t = read(p)
for old, new in [
    ("**anonymous Rev. 6 working theory manuscript + adversarial revision;", "**anonymous Rev. 7 working theory manuscript + adversarial revision;"),
    ("canonical manuscript is the anonymous 22-page Rev. 6, validated against the previous Rev. 5 baseline before canonicalization", "canonical manuscript is the anonymous 24-page Rev. 7, validated against the previous Rev. 6 baseline before canonicalization"),
    ("The immutable Rev. 6 source is stored inside the repository", "The immutable Rev. 7 source is stored inside the repository"),
    ("**REV. 6 submission blockers:**", "**REV. 7 submission blockers:**"),
]:
    t = must_replace(t, old, new, str(p))
# Add Rev7 records near current-state list.
old = "- `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n- `experiments/01-vanishing-absorber/MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md`"
new = "- `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n- `experiments/01-vanishing-absorber/MANUSCRIPT_REV7_PRESERVATION_REPORT_2026-08-11.md`\n- `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n- `experiments/01-vanishing-absorber/MANUSCRIPT_REV6_PRESERVATION_REPORT_2026-08-11.md`"
t = must_replace(t, old, new, str(p))
# Add Rev7 at first canonical reading order occurrence without requiring renumber cleanup elsewhere.
old = "6. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n6. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`"
new = "6. `experiments/01-vanishing-absorber/REV7_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n7. `experiments/01-vanishing-absorber/REV6_ADVERSARIAL_CORRECTIONS_2026-08-11.md`\n8. `experiments/01-vanishing-absorber/REV5_ADVERSARIAL_CORRECTIONS_2026-08-11.md`"
t = must_replace(t, old, new, str(p))
lock = r'''## 6A. Rev. 7 scientific locks — never regress

### Adversarial-review discipline

A hostile referee report is **evidence and an attack vector, not authority or a task list**. Independently determine whether each objection is mathematically correct, physically relevant in the stated regime, numerically supported, and within scope. Then explicitly classify it as accepted, narrowed, rejected, useful stress test, or out-of-scope. Do not overcorrect a valid but limited criticism, and do not defend an invalid manuscript claim merely because it is already in the paper.

### Classical finite-exponential attribution

The geometric one-mode identity and two-mode Hankel/Casoratian identities belong to the classical Prony/ESPRIT/matrix-pencil family. Never imply that those algebraic identities themselves are novel. The candidate distinction is the detector-specific construction that creates and physically constrains the spatial sequence.

### HgCdTe force baseline

The current headline worked stress uses the 2025 electron-affinity relation

```math
chi(x)=5.32+0.45x-E_g(x,300 K)
```

and therefore

```math
E_{drive}^{grad}=|(dE_g/dx-0.45)dx/dz|,
```

with `xi_e~0.666--0.695` for the worked `x=0.55 -> 0.32` profile. The historical `xi=1` calculation is a sensitivity case, not the canonical Rev. 7 HgCdTe baseline.

Canonical finite-width gradient-sensitive phase stresses are approximately `-0.0220167 / -0.1064448 / -0.1942321 degree` at 100 / 500 / 1000 MHz.

### Recombination interpretation

Do not repeat the false statement that nonlinear Auger recombination is intrinsically incompatible with a first-order small-signal `kappa`. A nonlinear recombination law can be linearized around an operating point; the graded-material issue is the resulting spatially varying differential rate.

The Rev. 7 deliberately steep 5-us-anchored recombination profile changes the closure by less than `4e-7 degree` over 0.1--1 GHz in the specified conditional stress. This does **not** establish negligible recombination for high injection, depletion, every composition profile, or every detector architecture.

### Current experimental/resource scales

Use the Rev. 7 propagated scales, not Rev. 5/6 values: conditioning optimum about `5.85 GHz`; optimistic weighting-mode rank-two separation about `108.6 / 81.2 / 70.5 dB`; five-color penalty about `42.4 / 28.7 / 23.2 dB`; 3-sigma current-step SNR `90.9 / 82.9 / 77.1 / 71.4 dB` at 100/250/500/1000 MHz; nonaffine coordinate RMS about `4.5 nm`; irregular phase RMS `1.88e-4 / 9.15e-4 / 1.71e-3 degree` at 100/500/1000 MHz.

The proposed common-reference/interleaved-wavelength coherent architecture is **not demonstrated feasibility**. Residual spectral-phase/depth and baseline-covariance performance remain open experimental requirements.

---'''
marker = "## 7. Major invalidations — never silently resurrect"
if marker not in t:
    raise SystemExit("AGENTS Rev7 insertion marker missing")
t = t.replace(marker, lock + "\n\n" + marker, 1)
write(p, t)

print("Rev7 canonical recovery/state files updated.")
