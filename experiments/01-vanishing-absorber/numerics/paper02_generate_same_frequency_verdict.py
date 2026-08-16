"""Generate a version-controlled scientific verdict from the same-frequency test."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def run(args):
    d = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = d["rows"]
    r100 = rows[0]
    first = bool(r100["positive_D_detectable_before_one_mode_rejection"])
    ratio = float(r100["hidden_risk_ratio_Sreject_over_SD"])

    if first:
        decision = "SAME-FREQUENCY HIDDEN-RISK ORDERING PASSED UNDER THE REFERENCE NOISE MODEL"
        consequence = (
            "At 100 MHz, statistically significant positive apparent diffusion is reached "
            "at a lower RMS-channel SNR than is required to reject the six-channel one-mode "
            "model.  There is therefore a finite SNR interval in which the wrong homogeneous "
            "material attribution is statistically significant while the same-frequency "
            "spectral model remains non-rejectable.  This is conditional on the stated "
            "independent equal-quadrature noise model and is not a universal ordering."
        )
    else:
        decision = "SAME-FREQUENCY HIDDEN-RISK ORDERING FAILED UNDER THE REFERENCE NOISE MODEL"
        consequence = (
            "At 100 MHz, the six-channel one-mode model is rejectable at an RMS-channel SNR "
            "no greater than that required to establish positive apparent diffusion.  The "
            "current example therefore does not support a claim that a statistically "
            "established positive diffusion coefficient is hidden from the same-frequency "
            "spectral model check.  The paper must retain the result as an effective-parameter "
            "bias / low-frequency dispersion alias and avoid claiming same-frequency statistical "
            "stealth for this case."
        )

    lines = [
        "# Paper 02 — Same-Frequency Statistical Verdict",
        "",
        "**Status:** **CHECKED UNDER EXPLICIT THEORETICAL NOISE MODEL**",
        "",
        f"## Verdict: **{decision}**",
        "",
        consequence,
        "",
        "## Reference noise/test model",
        "",
        "```text",
        "six complex spectral channels",
        "independent equal Gaussian real/imag quadrature noise",
        "S = RMS_m |J_m| / sigma_quadrature",
        "alpha = 0.0027",
        "power = 0.90",
        "one-mode residual dof = 6",
        "```",
        "",
        "## Numerical ordering",
        "",
        "| RF | D_eff [m^2/s] | SNR positive D [dB] | SNR one-mode rejection [dB] | D first? |",
        "|---:|---:|---:|---:|:---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['frequency_hz']/1e6:.0f} MHz | {r['D_eff_m2_per_s']:.6e} | "
            f"{r['snr_required_positive_D_db']:.3f} | "
            f"{r['snr_required_one_mode_rejection_db']:.3f} | "
            f"{'YES' if r['positive_D_detectable_before_one_mode_rejection'] else 'NO'} |"
        )
    lines += [
        "",
        "At 100 MHz:",
        "",
        "```text",
        f"SNR_D          = {r100['snr_required_positive_D']:.9g}",
        f"SNR_1mode      = {r100['snr_required_one_mode_rejection']:.9g}",
        f"SNR_1mode/SNR_D= {ratio:.9g}",
        "```",
        "",
        "## Interpretation rule",
        "",
        "The deterministic full-vector residual `||J-J_fit||/||J||` remains useful as an approximation metric but must not be substituted for this covariance-aware model-selection result.",
        "",
        "This verdict concerns only same-frequency channel-manifold rejection.  Multi-frequency homogeneous transport-law rejection is a separate test documented in `PAPER02_END_TO_END_REJECTION_SNR_RESULT_2026-08-15.md`.",
    ]
    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="results/paper02_same_frequency_hidden_risk_summary.json")
    p.add_argument("--output", default="../PAPER02_SAME_FREQUENCY_STATISTICAL_VERDICT_2026-08-15.md")
    return p


if __name__ == "__main__":
    run(parser().parse_args())
