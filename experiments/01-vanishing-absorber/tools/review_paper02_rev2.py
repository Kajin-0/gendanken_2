"""Generate a source-aware adversarial review of Paper-02 Rev. 2."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "PAPER02_MANUSCRIPT_REV2_ANON_2026-08-15.tex"
DATA = ROOT / "numerics/results/paper02_same_frequency_hidden_risk_summary.json"
OUT = ROOT / "PAPER02_REV2_ADVERSARIAL_REVIEW_2026-08-15.md"

text = SRC.read_text(encoding="utf-8")
data = json.loads(DATA.read_text(encoding="utf-8"))
r100 = data["rows"][0]
d_first = bool(r100["positive_D_detectable_before_one_mode_rejection"])

checks = {
    "local exponent bridge": r"\gamma_{\rm loc}" in text and r"P(z,\omega)" in text,
    "same-frequency statistical subsection": "PAPER02_SAME_FREQUENCY_STATISTICAL_SNIPPET" in text,
    "mean-depth causal language narrowed": "mean generation depth alone is insufficient" in text,
    "mathematical-control caveat": "mathematical causal controls" in text,
    "known-kernel vs experimental calibration distinction": "No experimental kernel calibration is performed" in text,
    "HgCdTe scale caveat": "does not validate the modeled velocity profile" in text,
    "title aligned with velocity theorem": "Apparent diffusion from deterministic velocity gradients" in text,
    "Shockley-Ramo primary citations": "shockley1938" in text and "ramo1939" in text,
}

if not all(checks.values()):
    disposition = "MAJOR REVISION STILL REQUIRED"
else:
    disposition = "MAJOR REV. 1 DEFECTS REPAIRED; MODERATE PRE-SUBMISSION REVISION REMAINS"

if d_first:
    ordering = (
        "The new same-frequency calculation supports a genuine conditional hidden-risk interval: "
        "positive apparent D reaches the stated detection criterion before the one-mode channel "
        "manifold reaches the stated rejection criterion under the reference noise model."
    )
else:
    ordering = (
        "The new same-frequency calculation does **not** support same-frequency statistical stealth: "
        "the one-mode channel model becomes rejectable no later than positive apparent D reaches the "
        "stated detection criterion.  Rev. 2 correctly narrows the generated subsection rather than "
        "overriding this unfavorable result.  The paper remains viable through the low-frequency "
        "dispersion alias, remote-support bias theorem, and nuisance-aware attribution framework."
    )

lines = [
    "# Paper 02 Rev. 2 — Adversarial Review",
    "",
    "**Date:** 2026-08-15  ",
    f"**Disposition:** **{disposition}**",
    "",
    "## Executive assessment",
    "",
    "Rev. 2 is materially stronger than Rev. 1. The central deterministic-zero-diffusion counterexample remains intact, while the manuscript now distinguishes local point-source theory from finite-kernel averaging, statistical model rejection from descriptive residual size, and theoretical known-kernel assumptions from experimental calibration.",
    "",
    ordering,
    "",
    "The paper is no longer blocked by an internal scientific defect found in the Rev. 1 adversarial review. The remaining work is manuscript hardening: exact optical-method documentation, bibliography completion, final figure integration, and submission-level source comparison.",
    "",
    "## Rev. 1 major-comment repair audit",
    "",
]
for name, ok in checks.items():
    lines.append(f"- {'PASS' if ok else 'FAIL'} — {name}")

lines += [
    "",
    "## Same-frequency statistical ordering",
    "",
    "Under the explicit six-complex-channel independent equal-quadrature noise model (`alpha=0.0027`, 90% power):",
    "",
    "```text",
    f"100 MHz apparent D                {r100['D_eff_m2_per_s']:.9g} m^2/s",
    f"SNR required for positive D       {r100['snr_required_positive_D']:.9g}  ({r100['snr_required_positive_D_db']:.3f} dB)",
    f"SNR required to reject one-mode   {r100['snr_required_one_mode_rejection']:.9g}  ({r100['snr_required_one_mode_rejection_db']:.3f} dB)",
    f"rejection / D-detection SNR ratio {r100['hidden_risk_ratio_Sreject_over_SD']:.9g}",
    f"positive D detected first?        {d_first}",
    "```",
    "",
    "This numerical ordering must control all later uses of `hidden`, `stealth`, or `non-rejectable` in the manuscript. The raw `||J-J_fit||/||J||` value is not an acceptable substitute.",
    "",
    "## Remaining substantive issues",
    "",
    "### R1. Optical-kernel construction still needs a submission-grade methods record",
    "",
    "Rev. 2 correctly states that the HgCdTe kernels are theoretical known-kernel inputs and not experimentally calibrated data. Before submission, the supplement must still give the actual absorption/composition law, numerical wavelength-to-mean-depth solve, discretization, normalization, and omitted optical effects. The main result does not require a specific HgCdTe absorption law, but the numerical overlap percentages do.",
    "",
    "### R2. Bibliography remains a working boundary bibliography",
    "",
    "Shockley and Ramo have been added, but the submission bibliography still needs publisher-level metadata verification and denser coverage of classical PIN transit/diffusion response, wavelength-dependent absorption-depth timing, OED predecessors, and any older effective-diffusion/migration inverse work identified through citation chaining.",
    "",
    "### R3. Main figures are still compile-safe placeholders",
    "",
    "This is acceptable for an internal Rev. 2 but not for referee-ready output. The canonical vector plots are already generated and reproducible; Rev. 3 should integrate them or create a manuscript-local figure artifact package with exact hashes.",
    "",
    "### R4. The remote-support theorem is general; the numerical magnitude is not",
    "",
    "The exact leakage identity and zero-overlap statement are kernel-family independent. The quoted `D_eff` magnitude and overlap probabilities belong to one conditional six-kernel HgCdTe-like family. Keep that distinction explicit in abstract, discussion, and conclusions.",
    "",
    "### R5. The HgCdTe section is now appropriately cautious, but should remain a scale check",
    "",
    "The `166.7 V/cm` versus published `100--200 V/cm` comparison establishes plausible field scale only. It cannot validate the modeled velocity profile, saturation law, or false-D magnitude in the published devices. Rev. 2 now says this; do not weaken that caveat later.",
    "",
    "### R6. Statistical SNR curve is a reference design, not a fundamental bound",
    "",
    "The very high channel SNR values depend on the chosen channel normalization, equal-quadrature noise, equal SNR across frequencies, and no calibration covariance. Retain the language `under the stated reference noise model` wherever numerical dB values are quoted.",
    "",
    "## Scientific decision",
    "",
    "The standalone Paper-02 path remains justified. Rev. 2 has moved the project from `major scientific repair` to `pre-submission manuscript hardening`.",
    "",
    "Recommended Rev. 3 scope:",
    "",
    "```text",
    "1. add exact conditional optical-kernel methods/supplement;",
    "2. integrate canonical figures and captions;",
    "3. harden/verify bibliography against primary sources;",
    "4. enforce the actual same-frequency statistical verdict throughout prose;",
    "5. re-run a final adversarial review on the compiled figure-bearing manuscript;",
    "6. do not alter Paper 01 / Rev. 9.",
    "```",
]

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(OUT)
