"""Generate a LaTeX snippet from the persisted same-frequency hidden-risk result.

The wording is selected from the actual row-by-row statistical ordering rather
than inferred from a single RF point.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def fmt_sci(x):
    if x == float("inf"):
        return r"\infty"
    return f"{x:.3g}"


def fmt_freq(row):
    mhz = row["frequency_hz"] / 1e6
    if abs(mhz - 1000.0) < 1e-9:
        return "1 GHz"
    if mhz >= 1000.0 and abs(mhz % 1000.0) < 1e-9:
        return f"{mhz / 1000.0:.0f} GHz"
    return f"{mhz:.0f} MHz"


def run(args):
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = data["rows"]
    hidden_rows = [
        row for row in rows
        if bool(row["positive_D_detectable_before_one_mode_rejection"])
    ]
    announced_rows = [
        row for row in rows
        if not bool(row["positive_D_detectable_before_one_mode_rejection"])
    ]

    if hidden_rows and announced_rows:
        announced = "; ".join(
            f"{fmt_freq(row)}: $S_{{1\\mathrm{{m}}}}={row['snr_required_one_mode_rejection_db']:.2f}$ dB "
            f"before $S_D={row['snr_required_positive_D_db']:.2f}$ dB"
            for row in announced_rows
        )
        hidden = "; ".join(
            f"{fmt_freq(row)}: ${row['snr_required_positive_D_db']:.2f}$--"
            f"${row['snr_required_one_mode_rejection_db']:.2f}$ dB"
            for row in hidden_rows
        )
        ordering = (
            "Under this reference covariance, the ordering is frequency dependent.  "
            f"At the tested point(s) {announced}, so the spectral-model check self-announces "
            "before positive apparent diffusion reaches the stated 90\\% detection power.  "
            f"At the remaining tested point(s), positive apparent diffusion reaches 90\\% "
            f"power first, leaving finite RMS-channel-SNR windows ({hidden}) in which "
            "$D>0$ has reached the stated detection power while rejection of the same-frequency "
            "one-mode manifold has not.  The example therefore supports conditional "
            "same-frequency hidden-risk windows at those RF points, not a universal stealth claim."
        )
    elif hidden_rows:
        hidden = "; ".join(
            f"{fmt_freq(row)}: ${row['snr_required_positive_D_db']:.2f}$--"
            f"${row['snr_required_one_mode_rejection_db']:.2f}$ dB"
            for row in hidden_rows
        )
        ordering = (
            "Under this reference covariance, positive apparent diffusion reaches the stated "
            "90\\% detection power before the same-frequency six-channel one-mode manifold "
            f"reaches 90\\% rejection power at every tested RF point.  The corresponding "
            f"RMS-channel-SNR windows are {hidden}.  This is conditional on the stated noise "
            "model and does not establish universal statistical stealth."
        )
    else:
        ordering = (
            "Under this reference covariance, the six-channel one-mode manifold reaches the "
            "stated 90\\% rejection power no later than positive apparent diffusion reaches "
            "90\\% detection power at every tested RF point.  The present example therefore "
            "does not support same-frequency statistical hidden risk under this noise model."
        )

    lines = []
    lines.append(r"\subsection{Same-frequency model rejection versus positive-$D$ detection}")
    lines.append("")
    lines.append(
        "A small deterministic fit residual relative to the full channel vector is not by itself a statistical model-acceptance statement. "
        "We therefore place the same-frequency one-mode goodness-of-fit test and the positive-$D$ test on the same explicit theoretical noise scale. "
        "At one RF frequency the six complex channels provide 12 real observations, while the complex $(C,K,r)$ one-mode model has six real fitted parameters, leaving six local residual degrees of freedom."
    )
    lines.append("")
    lines.append(
        r"We retain the independent equal real/imaginary quadrature-noise model used below and define $S=\sqrt{\langle |J_m|^2\rangle}/\sigma_{\rm q}$. "
        r"For the one-mode test, the deterministic post-fit channel residual supplies the noncentral alternative. "
        r"For positive-$D$ detectability, the full $12\times6$ channel Jacobian is propagated through the fitted complex root and then through $D(\gamma)$; an idealized one-sided Gaussian $D>0$ test is evaluated at the same $\alpha=0.0027$ and 90\% power."
    )
    lines.append("")
    lines.append(r"\begin{table}[t]")
    lines.append(r"\caption{Same-frequency statistical ordering under the reference independent-quadrature noise model. $S_D$ is the RMS-channel SNR required for 90\% power to establish positive apparent diffusion; $S_{1\mathrm{m}}$ is the SNR required for 90\% power to reject the six-channel one-mode manifold, both at $\alpha=0.0027$.}")
    lines.append(r"\label{tab:samefreq}")
    lines.append(r"\centering")
    lines.append(r"\begin{tabular}{rrrr}")
    lines.append(r"\toprule")
    lines.append(r"RF & $D_{\rm eff}$ (m$^2$/s) & $S_D$ (dB) & $S_{1\mathrm{m}}$ (dB)\\")
    lines.append(r"\midrule")
    for row in rows:
        lines.append(
            f"{row['frequency_hz']/1e6:.0f} MHz & "
            f"{row['D_eff_m2_per_s']:.3e} & "
            f"{row['snr_required_positive_D_db']:.2f} & "
            f"{row['snr_required_one_mode_rejection_db']:.2f}\\\\"
        )
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")
    lines.append(ordering)
    lines.append("")
    lines.append(
        r"This comparison also clarifies the role of the deterministic full-vector residual quoted elsewhere in the paper: it is a descriptive approximation error, whereas Table~\ref{tab:samefreq} is the corresponding covariance-aware model-selection statement for the reference noise model."
    )

    Path(args.output).write_text("\n".join(lines) + "\n", encoding="utf-8")


def parser():
    p = argparse.ArgumentParser()
    p.add_argument(
        "--input",
        default="results/paper02_same_frequency_hidden_risk_summary.json",
    )
    p.add_argument(
        "--output",
        default="../PAPER02_SAME_FREQUENCY_STATISTICAL_SNIPPET.tex",
    )
    return p


if __name__ == "__main__":
    run(parser().parse_args())
