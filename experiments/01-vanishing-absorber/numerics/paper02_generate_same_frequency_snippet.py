"""Generate a LaTeX snippet from the persisted same-frequency hidden-risk result.

The wording is selected from the actual statistical ordering rather than being
hard-coded into the manuscript before the test result is known.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def fmt_sci(x):
    if x == float("inf"):
        return r"\infty"
    return f"{x:.3g}"


def run(args):
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    rows = data["rows"]
    r100 = rows[0]
    d_first = bool(r100["positive_D_detectable_before_one_mode_rejection"])

    if d_first:
        ordering = (
            "Under this reference covariance, the positive apparent diffusion becomes "
            "statistically detectable before the same-frequency six-channel one-mode "
            "manifold becomes rejectable.  The nuisance is therefore hidden with respect "
            "to the same-frequency model check over a finite SNR interval; this statement "
            "is conditional on the stated noise model rather than a universal property."
        )
    else:
        ordering = (
            "Under this reference covariance, the six-channel one-mode manifold becomes "
            "rejectable no later than the positive apparent diffusion becomes statistically "
            "detectable.  The present example therefore does not support a claim that the "
            "same-frequency spectral model hides a statistically established diffusion "
            "coefficient.  The stronger identifiability issue remains the low-frequency "
            "dispersion alias and the need for nuisance-aware attribution."
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
        "We retain the independent equal real/imaginary quadrature-noise model used below and define $S=\sqrt{\langle |J_m|^2\rangle}/\sigma_{\rm q}$. "
        "For the one-mode test, the deterministic post-fit channel residual supplies the noncentral alternative. "
        "For positive-$D$ detectability, the full $12\times6$ channel Jacobian is propagated through the fitted complex root and then through $D(\gamma)$; an idealized one-sided Gaussian $D>0$ test is evaluated at the same $\alpha=0.0027$ and 90\% power."
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
            f"{row['snr_required_one_mode_rejection_db']:.2f}\\"
        )
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    lines.append("")
    lines.append(ordering)
    lines.append("")
    lines.append(
        "This comparison also clarifies the role of the deterministic full-vector residual quoted elsewhere in the paper: it is a descriptive approximation error, whereas Table~\ref{tab:samefreq} is the corresponding covariance-aware model-selection statement for the reference noise model."
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
