"""Generate a version-controlled scientific verdict from the same-frequency test."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def fmt_freq(row):
    mhz = row["frequency_hz"] / 1e6
    if abs(mhz - 1000.0) < 1e-9:
        return "1 GHz"
    if mhz >= 1000.0 and abs(mhz % 1000.0) < 1e-9:
        return f"{mhz / 1000.0:.0f} GHz"
    return f"{mhz:.0f} MHz"


def run(args):
    d = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = d["rows"]
    hidden_rows = [
        row for row in rows
        if bool(row["positive_D_detectable_before_one_mode_rejection"])
    ]
    announced_rows = [
        row for row in rows
        if not bool(row["positive_D_detectable_before_one_mode_rejection"])
    ]

    if hidden_rows and announced_rows:
        decision = "FREQUENCY-DEPENDENT SAME-FREQUENCY HIDDEN-RISK ORDERING"
        hidden_text = "; ".join(
            f"{fmt_freq(row)}: {row['snr_required_positive_D_db']:.3f}--"
            f"{row['snr_required_one_mode_rejection_db']:.3f} dB"
            for row in hidden_rows
        )
        announced_text = "; ".join(
            f"{fmt_freq(row)}: one-mode rejection {row['snr_required_one_mode_rejection_db']:.3f} dB, "
            f"positive-D detection {row['snr_required_positive_D_db']:.3f} dB"
            for row in announced_rows
        )
        consequence = (
            "The ordering is not uniform across RF.  At the tested low-frequency point(s), "
            f"the spectral-model check self-announces first ({announced_text}).  At the other "
            "tested point(s), positive apparent diffusion reaches the stated 90% detection "
            f"power before the one-mode manifold reaches 90% rejection power, leaving finite "
            f"RMS-channel-SNR hidden-risk windows ({hidden_text}).  The example therefore "
            "supports conditional same-frequency hidden risk at those RF points but not a "
            "universal stealth claim."
        )
    elif hidden_rows:
        decision = "SAME-FREQUENCY HIDDEN-RISK ORDERING PRESENT AT ALL TESTED RF POINTS"
        hidden_text = "; ".join(
            f"{fmt_freq(row)}: {row['snr_required_positive_D_db']:.3f}--"
            f"{row['snr_required_one_mode_rejection_db']:.3f} dB"
            for row in hidden_rows
        )
        consequence = (
            "At every tested RF point, statistically significant positive apparent diffusion "
            "reaches the stated 90% detection power at a lower RMS-channel SNR than is required "
            "for 90% rejection power against the six-channel one-mode model.  The finite "
            f"hidden-risk windows are {hidden_text}.  This conclusion remains conditional on "
            "the stated theoretical covariance model."
        )
    else:
        decision = "SAME-FREQUENCY HIDDEN-RISK ORDERING ABSENT AT ALL TESTED RF POINTS"
        consequence = (
            "At every tested RF point, the six-channel one-mode model reaches the stated 90% "
            "rejection power no later than positive apparent diffusion reaches 90% detection "
            "power.  This example therefore does not support same-frequency statistical hidden "
            "risk under the stated theoretical covariance model."
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
        "## Interpretation rule",
        "",
        "A hidden-risk window at one RF point means only that, under the stated covariance and power criterion, positive apparent diffusion reaches the chosen detection power before the same-frequency one-mode goodness-of-fit test reaches the chosen rejection power.  It is not a statement of universal model indistinguishability.",
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
