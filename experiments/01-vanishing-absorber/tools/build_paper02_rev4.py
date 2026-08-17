"""Create Paper-02 Rev. 4 and Supplemental Material from frozen Rev. 3.

Rev. 4 is a bounded manuscript-hardening revision.  It does not alter the
central theorem stack or canonical figure datasets.  It:

1. requires the independently refined inferential convergence gate to have
   passed before any output is produced;
2. removes ambiguous empirical-calibration wording for the theoretical optical
   kernels while preserving legitimate references to wavelength/instrument
   calibration;
3. adds the checked numerical-convergence result to the manuscript;
4. creates actual Supplemental Material that separates the theoretical HgCdTe
   optical-kernel construction from the distinct planar-depletion deterministic
   transport stress; and
5. expands the bibliography with the load-bearing Hansen band-gap and Moazzami
   absorption-model sources.

The frozen Rev. 3 source is verified by Git blob SHA before transformation.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NUM = ROOT / "numerics"
SRC = ROOT / "PAPER02_MANUSCRIPT_REV3_ANON_2026-08-15.tex"
DST = ROOT / "PAPER02_MANUSCRIPT_REV4_ANON_2026-08-16.tex"
SUPP = ROOT / "PAPER02_SUPPLEMENT_REV4_ANON_2026-08-16.tex"
BIB_SRC = ROOT / "PAPER02_REFERENCES_REV2.bib"
BIB_DST = ROOT / "PAPER02_REFERENCES_REV4.bib"
CONV = NUM / "results" / "paper02_inference_convergence_summary.json"

EXPECTED_REV3_BLOB = "cf9d82b70e858027c038656ffa71f7fed9a2889d"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"Expected exactly one occurrence, found {n}: {old[:140]!r}")
    return text.replace(old, new, 1)


def load_checked_convergence():
    if not CONV.exists():
        raise RuntimeError(f"Missing persisted convergence result: {CONV}")
    payload = json.loads(CONV.read_text(encoding="utf-8"))
    if not payload.get("convergence", {}).get("overall_pass", False):
        raise RuntimeError("Paper-02 inferential convergence gate has not passed")
    return payload


def build_bibliography():
    text = BIB_SRC.read_text(encoding="utf-8")
    additions = r'''

% Load-bearing empirical relations used by the conditional theoretical
% HgCdTe optical-kernel construction in Rev. 4 / Supplemental Material.
@article{hansen1982gap,
  author  = {Hansen, G. L. and Schmit, J. L. and Casselman, T. N.},
  title   = {Energy gap versus alloy composition and temperature in {Hg1-xCdxTe}},
  journal = {Journal of Applied Physics},
  volume  = {53},
  number  = {10},
  pages   = {7099--7101},
  year    = {1982},
  doi     = {10.1063/1.330018}
}

@article{moazzami2005absorption,
  author  = {Moazzami, K. and Phillips, J. and Lee, D. and Krishnamurthy, S. and Benoit, G. and Fink, Y. and Tiwald, T.},
  title   = {Detailed study of above bandgap optical absorption in {HgCdTe}},
  journal = {Journal of Electronic Materials},
  volume  = {34},
  number  = {6},
  pages   = {773--778},
  year    = {2005},
  doi     = {10.1007/s11664-005-0019-3}
}
'''
    if "hansen1982gap" in text or "moazzami2005absorption" in text:
        raise RuntimeError("Rev. 2 bibliography unexpectedly already contains Rev. 4 additions")
    BIB_DST.write_text(text.rstrip() + additions + "\n", encoding="utf-8")


def build_main(conv):
    data = SRC.read_bytes()
    observed = git_blob_sha(data)
    if observed != EXPECTED_REV3_BLOB:
        raise RuntimeError(
            f"Frozen Rev. 3 blob changed: expected {EXPECTED_REV3_BLOB}, observed {observed}"
        )
    text = data.decode("utf-8")

    text = replace_once(text, r"\date{August 15, 2026}", r"\date{August 16, 2026}")

    replacements = [
        (
            "when finite calibrated generation kernels overlap a downstream region of nonuniform deterministic velocity",
            "when finite generation kernels treated as known by the inverse overlap a downstream region of nonuniform deterministic velocity",
        ),
        (
            "the detector-specific combination of finite calibrated generation kernels, deterministic velocity heterogeneity",
            "the detector-specific combination of finite generation kernels supplied exactly to the inverse, deterministic velocity heterogeneity",
        ),
        (
            "The calibrated one-mode inverse is written in the numerically stable form",
            "The kernel-aware one-mode inverse is written in the numerically stable form",
        ),
        (
            "This form retains the independently specified channel shapes rather than replacing them with delta functions or assuming rigid translations.  Throughout the mathematical analysis, ``known'' or ``calibrated'' kernel means that $g_m(z)$ is supplied to the inverse as an independently characterized forward-model input.  No experimental kernel calibration is performed in this work.",
            "This form retains the independently specified channel shapes rather than replacing them with delta functions or assuming rigid translations.  Throughout this work, a kernel treated as ``known'' means that the same theoretically specified $g_m(z)$ is supplied to the forward average and to the inverse.  No experimental kernel calibration is performed here, and optical-model uncertainty is deliberately excluded from the central counterexample.",
        ),
        (
            "For the conditional HgCdTe numerical example we use six normalized finite kernels generated by the repository's monotonic graded-HgCdTe optical model.",
            "For the conditional HgCdTe numerical example we use six normalized finite kernels generated by a monotonic graded-HgCdTe optical model using the Hansen band-gap relation and the Moazzami above-bandgap absorption parameterization \\cite{hansen1982gap,moazzami2005absorption}.",
        ),
        (
            "but the calibrated kernels retain finite probability inside it.",
            "but the theoretical kernels retain finite probability inside it.",
        ),
        (
            "Then the calibrated channel is exactly",
            "Then the kernel-averaged channel is exactly",
        ),
        (
            "At a fixed RF frequency, collect the calibrated channels into",
            "At a fixed RF frequency, collect the specified finite-kernel channels into",
        ),
        (
            "tangent to the calibrated one-mode manifold",
            "tangent to the kernel-aware one-mode manifold",
        ),
        (
            "while keeping the six calibrated optical kernels fixed.",
            "while keeping the six theoretical optical kernels fixed.",
        ),
        (
            "outside the local calibrated one-mode tangent in this test",
            "outside the local kernel-aware one-mode tangent in this test",
        ),
        (
            "follows the nonlinear calibrated-kernel inverse for both independent velocity families.",
            "follows the nonlinear kernel-aware inverse for both independent velocity families.",
        ),
        (
            "propagated through the calibrated one-mode root fit.",
            "propagated through the kernel-aware one-mode root fit.",
        ),
        (
            "the full calibrated generation kernels should be evaluated against known device-level nuisance regions.",
            "the full supplied generation kernels should be evaluated against known device-level nuisance regions.",
        ),
        (
            "First, calibrated optical kernels solve an optical forward-model problem but cannot make the underlying point-source transport homogeneous. Exact knowledge of $g_m(z)$ therefore does not by itself eliminate Eq.~\\eqref{eq:leakage}.",
            "First, supplying the exact theoretical optical kernels removes optical-model uncertainty from the controlled inverse but cannot make the underlying point-source transport homogeneous. Exact knowledge of $g_m(z)$ therefore does not by itself eliminate Eq.~\\eqref{eq:leakage}.",
        ),
        (
            "A nuisance nearly tangent to the calibrated model can strongly move the root",
            "A nuisance nearly tangent to the kernel-aware model can strongly move the root",
        ),
        (
            "The exact conditional optical-model implementation, selected channel wavelengths, kernel normalization checks, and numerical kernel moments are frozen in a machine-extracted methods record generated from the same executable module used by the calculations.  A submission version should reproduce those details in Supplemental Material rather than relying on undocumented code.",
            "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the independently refined inferential convergence gate, and executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the apparent $D_{\\rm eff}$ counterexample.",
        ),
        (
            "does not yet propagate uncertainty in the calibrated optical kernels or electrostatic model itself.",
            "does not yet propagate uncertainty in the supplied optical kernels or electrostatic model itself.",
        ),
        (
            "survives exact calibrated-kernel fitting",
            "survives exact finite-kernel fitting",
        ),
        (
            "projection onto the calibrated model tangent",
            "projection onto the kernel-aware model tangent",
        ),
        (
            r"\bibliography{PAPER02_REFERENCES_REV2}",
            r"\bibliography{PAPER02_REFERENCES_REV4}",
        ),
    ]
    for old, new in replacements:
        text = replace_once(text, old, new)

    # Add a numerical-convergence disclosure immediately after the new
    # Supplemental-Material paragraph and before limitations.
    marker = (
        "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the independently refined inferential convergence gate, and executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the apparent $D_{\\rm eff}$ counterexample."
    )
    mesh_rows = conv["convergence"]["axes"]["field_mesh"]
    by_metric = {row["metric"]: row for row in mesh_rows}
    d100 = 100.0 * by_metric["D_100"]["baseline_to_fine_change"]
    d500 = 100.0 * by_metric["D_500"]["baseline_to_fine_change"]
    d1000 = 100.0 * by_metric["D_1000"]["baseline_to_fine_change"]
    fine100 = by_metric["D_100"]["fine"]

    conv_par = (
        "\n\nThe nonlinear inference was also subjected to an independent numerical-convergence gate rather than relying only on the earlier raw closure-phase check.  Around the manuscript baseline, the two-dimensional electrostatic/weighting mesh, source-kernel quadrature, and trajectory step were refined one at a time.  The field mesh was the limiting coordinate: baseline-to-fine changes in $D_{\\rm eff}$ were "
        f"${d100:.3f}\\%$, ${d500:.3f}\\%$, and ${d1000:.3f}\\%$ at $100\\,\\mathrm{{MHz}}$, $500\\,\\mathrm{{MHz}}$, and $1\\,\\mathrm{{GHz}}$, respectively, all below the predeclared $2\\%$ gate.  The fine-mesh $100\\,\\mathrm{{MHz}}$ value was ${fine100:.4e}\\,\\mathrm{{m^2/s}}$.  Source-quadrature and trajectory-step refinements changed the three probe-frequency diffusion estimates only at approximately $3.3$--$3.8\\times10^{{-5}}$ and $5.0$--$8.2\\times10^{{-6}}$ relative, respectively.  The upstream point-source null remained at numerical-zero scale ($10^{{-12}}$--$10^{{-11}}\\,\\mathrm{{m^2/s}}$), whereas the inside-region point-source control remained near $4.87\\times10^{{-3}}\\,\\mathrm{{m^2/s}}$.  All predeclared convergence and Shockley--Ramo integrity checks passed.  These tests establish numerical stability of the stated deterministic surrogate and inverse, not experimental calibration or uniqueness of the mechanism in a real device."
    )
    text = replace_once(text, marker, marker + conv_par)

    # Make the baseline/fine-mesh distinction explicit at the central numerical
    # value without changing the canonical figure dataset.
    baseline_sentence = (
        "The physical finite kernels centered at the original upstream means give\n"
        "\\begin{equation}\n"
        "\\Deff=2.6098\\times10^{-3}\\,\\mathrm{m^2/s}.\n"
        "\\label{eq:hgcdteD}\n"
        "\\end{equation}"
    )
    refined_sentence = baseline_sentence + (
        "\nThis is the value at the canonical manuscript baseline discretization.  Refining only the two-dimensional field mesh changes the $100\\,\\mathrm{MHz}$ result to $2.6535\\times10^{-3}\\,\\mathrm{m^2/s}$, a $1.648\\%$ shift, while preserving its positive sign and the causal controls."
    )
    text = replace_once(text, baseline_sentence, refined_sentence)

    # Rev. 4 should contain no ambiguous use of "calibrated" for the optical
    # kernels/model.  Legitimate wavelength/calibration-error discussion remains.
    forbidden_phrases = [
        "calibrated generation kernel",
        "calibrated optical kernel",
        "calibrated-kernel",
        "calibrated one-mode",
        "calibrated model tangent",
        "calibrated channel",
    ]
    lowered = text.lower()
    for phrase in forbidden_phrases:
        if phrase.lower() in lowered:
            raise RuntimeError(f"Ambiguous kernel-calibration phrase remains: {phrase}")

    if text.count(r"\author{Anonymous}") != 1:
        raise RuntimeError("Anonymous author guard failed")

    # Guard the repository's no-superlative claim posture.
    for pat in (r"\bfirst-ever\b", r"\bfor the first time\b", r"\buniversal false diffusion\b", r"\bfundamental new mechanism\b"):
        if re.search(pat, text, flags=re.IGNORECASE):
            raise RuntimeError(f"Forbidden priority wording found: {pat}")

    DST.write_text(text, encoding="utf-8")


def build_supplement(conv):
    mesh_rows = {r["metric"]: r for r in conv["convergence"]["axes"]["field_mesh"]}
    quad_rows = {r["metric"]: r for r in conv["convergence"]["axes"]["source_quadrature"]}
    step_rows = {r["metric"]: r for r in conv["convergence"]["axes"]["trajectory_step"]}

    def pct(row):
        return 100.0 * row["baseline_to_fine_change"]

    supp = rf'''\documentclass[aps,pra,onecolumn,superscriptaddress,nofootinbib]{{revtex4-2}}
\usepackage{{amsmath,amssymb,bm}}
\usepackage{{booktabs}}
\usepackage{{siunitx}}
\usepackage{{hyperref}}
\hypersetup{{colorlinks=true,citecolor=blue,urlcolor=blue,linkcolor=blue}}
\sisetup{{detect-all}}

\begin{{document}}

\title{{Supplemental Material for: Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors}}
\author{{Anonymous}}
\date{{August 16, 2026}}
\maketitle

\section{{Scope and separation of the two conditional models}}

The manuscript uses two distinct numerical constructions that must not be conflated.  First, a one-dimensional monotonic graded-HgCdTe optical model is used only to generate six finite, wavelength-dependent theoretical generation kernels $g_m(z)$.  Those same generated kernel shapes are supplied exactly to the forward averaging and to the kernel-aware inverse.  They are not measured or experimentally calibrated kernels from a specific detector.  Second, the central apparent-diffusion counterexample is generated by a separate deterministic planar-depletion transport stress with microscopic diffusion fixed to zero.  The graded optical-kernel model therefore determines how the point-source response is sampled; it is not the electrostatic transport model that generates the counterexample.

All numerical quantities below are conditional theoretical-model outputs.  They do not constitute a calibrated simulation of a published detector.

\section{{Conditional HgCdTe optical-kernel construction}}

The optical coordinate is $0\le z\le L$ with $L=7.6\,\mu\mathrm{{m}}$.  At $T=300\,\mathrm{{K}}$ the Cd mole fraction is taken to vary monotonically from $x=0.55$ at $z=0$ to $x=0.32$ at $z=L$.  The band gap is evaluated with the Hansen--Schmit--Casselman empirical relation \cite{{hansen1982gap}},
\begin{{equation}}
E_g(x,T)=-0.302+1.93x-0.81x^2+0.832x^3+5.35\times10^{{-4}}T(1-2x),
\end{{equation}}
with energy in electronvolts.

The above-bandgap absorption coefficient uses the Moazzami \emph{{et al.}} parameterization \cite{{moazzami2005absorption}},
\begin{{align}}
\alpha(E,x,T) &= K(x,T)\left(\frac{{E-E_g}}{{E}}\right)^{{n(x,T)}},\qquad E>E_g,\\
K(x,T) &= -20060+115750x+32.43T-64170x^2+0.43231T^2-101.92xT,\\
n(x,T) &= 0.74487-0.44513x+(0.000799-0.000757x)T,
\end{{align}}
and $\alpha=0$ for $E\le E_g$.  Here $\alpha$ is used in $\mathrm{{cm^{-1}}}$ in the optical-depth integral.  For a selected wavelength the unnormalized absorbed-generation density is
\begin{{equation}}
\tilde g(z)=\alpha(z)\exp\left[-\int_0^z\alpha(u)\,du\right],
\end{{equation}}
and the manuscript kernel is $g(z)=\tilde g(z)/\int_0^L\tilde g(u)du$.  Each wavelength is found numerically so that the normalized mean $\int zg(z)dz$ equals its target depth.

\begin{{table}}[h]
\caption{{Theoretical generation channels supplied exactly to the forward average and inverse.  $P_{{\rm abs}}$ is the modeled absorbed probability through the $7.6\,\mu\mathrm{{m}}$ layer.}}
\centering
\begin{{tabular}}{{ccccc}}
\toprule
Target mean ($\mu$m) & $\lambda$ ($\mu$m) & $P_{{\rm abs}}$ & Reintegrated mean ($\mu$m) & $\sigma_z$ ($\mu$m)\\
\midrule
2.000 & 2.059342009 & 0.999996080 & 2.000000000 & 0.783254\\
2.500 & 2.134650687 & 0.999984721 & 2.500000000 & 0.787048\\
3.000 & 2.215042347 & 0.999943407 & 3.000000000 & 0.789835\\
3.500 & 2.301173443 & 0.999801116 & 3.500000000 & 0.790930\\
4.000 & 2.393906801 & 0.999337640 & 4.000000000 & 0.788849\\
4.500 & 2.494502544 & 0.997909184 & 4.500000000 & 0.780666\\
\bottomrule
\end{{tabular}}
\end{{table}}

The optical model uses a dense one-dimensional grid of 12001 points.  The kernel construction contains no experimental optical-model uncertainty in the present stress; such uncertainty would be an additional nuisance in an experiment.

\section{{Deterministic planar-depletion transport stress}}

The central numerical counterexample is separate from the graded optical model above.  It solves a two-dimensional rectangular domain of lateral width $16\,\mu\mathrm{{m}}$ and absorber thickness $L=7.6\,\mu\mathrm{{m}}$.  The central case uses a full-width collecting contact, applied bias $V_{{\rm bias}}=0.30\,\mathrm{{V}}$, and a collector-side nonuniform region of width $W_d=3.0\,\mu\mathrm{{m}}$ with an added space-charge potential scale of $0.05\,\mathrm{{V}}$.  The corresponding average added-field scale is $166.7\,\mathrm{{V/cm}}$.  The physical electrostatic potential and the Shockley--Ramo weighting potential are solved independently.

Carrier transport is deterministic: $D_{{\rm micro}}=0$ and recombination is omitted.  The local drift speed is
\begin{{equation}}
v(E)=\frac{{\mu E}}{{\sqrt{{1+(\mu E/v_{{\rm sat}})^2}}}},
\end{{equation}}
with $\mu=0.90\,\mathrm{{m^2/(V\,s)}}$ and $v_{{\rm sat}}=6.0\times10^4\,\mathrm{{m/s}}$.  Along each deterministic trajectory the complex terminal-current transfer is accumulated as
\begin{{equation}}
H(\omega)=\int e^{{-i\omega t}}\,d\phi_w,
\end{{equation}}
including the final electrode contribution.  At dc this gives the exact Shockley--Ramo identity $H(0)=1-\phi_w(\mathbf r_0)$ for collected trajectories.

The manuscript baseline uses a $121\times91$ physical/weighting-potential mesh, $13$-point lateral Gaussian quadrature, $41$ source-depth nodes, and trajectory step $0.020\,\mu\mathrm{{m}}$.  The finite channel is then
\begin{{equation}}
J_m(\omega)=\int g_m(z)H(z,\omega)\,dz
\end{{equation}}
with the theoretical kernels above.  The homogeneous inverse fits the finite-kernel one-mode exponent and interprets it through $D\gamma^2+w\gamma=-i\omega$.

\section{{Independent inferential convergence gate}}

The convergence decision was declared before the successful run.  Mesh, source quadrature, and trajectory step were refined independently around the baseline.  The three levels were
\begin{{align*}}
\text{{field mesh:}}\quad &(81,61)\rightarrow(121,91)\rightarrow(161,121),\\
\text{{source quadrature:}}\quad &(9,31)\rightarrow(13,41)\rightarrow(17,61),\\
\text{{trajectory step:}}\quad &0.035\rightarrow0.020\rightarrow0.0125\ \mu\mathrm{{m}}.
\end{{align*}}
Seven unique configurations were required because all axes share the same baseline.

The predeclared baseline-to-fine tolerances were $2\%$ relative for probe-frequency $D_{{\rm eff}}$, $0.5\%$ for $w_{{\rm eff}}$, $2\%$ and $0.5\%$ for the low-band joint $D,w$ fit, $0.002$ absolute for the 1-GHz homogeneous-law residual, $2\times10^{{-5}}$ absolute for the maximum one-mode kernel-fit residual through 1 GHz, $1\%$ of the fine finite-kernel 100-MHz diffusion scale for the upstream point-control change, $2\%$ relative for the inside-region point-control diffusion, $10^{{-10}}$ for the dc Ramo error, and a minimum collection fraction of 0.999.  Positive-$D$ sign stability was also required for the finite-kernel 100/500/1000-MHz inversions and the inside-region point-source control.

\begin{{table}}[h]
\caption{{Field-mesh convergence of the same-frequency finite-kernel inverse.  The field mesh is the limiting numerical coordinate.}}
\centering
\begin{{tabular}}{{ccccc}}
\toprule
Frequency & Coarse $D_{{\rm eff}}$ & Baseline $D_{{\rm eff}}$ & Fine $D_{{\rm eff}}$ & Baseline$\to$fine\\
 & \multicolumn{{3}}{{c}}{{($\mathrm{{m^2/s}}$)}} & (\%)\\
\midrule
100 MHz & {mesh_rows['D_100']['coarse']:.9f} & {mesh_rows['D_100']['baseline']:.9f} & {mesh_rows['D_100']['fine']:.9f} & {pct(mesh_rows['D_100']):.3f}\\
500 MHz & {mesh_rows['D_500']['coarse']:.9f} & {mesh_rows['D_500']['baseline']:.9f} & {mesh_rows['D_500']['fine']:.9f} & {pct(mesh_rows['D_500']):.3f}\\
1 GHz   & {mesh_rows['D_1000']['coarse']:.9f} & {mesh_rows['D_1000']['baseline']:.9f} & {mesh_rows['D_1000']['fine']:.9f} & {pct(mesh_rows['D_1000']):.3f}\\
\bottomrule
\end{{tabular}}
\end{{table}}

The corresponding baseline-to-fine drift-speed changes are {pct(mesh_rows['w_100']):.3f}\%, {pct(mesh_rows['w_500']):.3f}\%, and {pct(mesh_rows['w_1000']):.3f}\%.  The low-band joint $D$ and $w$ changes are {pct(mesh_rows['D_low']):.3f}\% and {pct(mesh_rows['w_low']):.3f}\%.  The 1-GHz law residual changes by {mesh_rows['law_residual_1ghz']['baseline_to_fine_change']:.3e} absolute and the maximum one-mode finite-kernel fit residual through 1 GHz changes by {mesh_rows['max_kernel_fit_1ghz']['baseline_to_fine_change']:.3e} absolute.

Source/kernel quadrature is substantially more converged: the baseline-to-fine relative changes in $D_{{\rm eff}}$ are {quad_rows['D_100']['baseline_to_fine_change']:.3e}, {quad_rows['D_500']['baseline_to_fine_change']:.3e}, and {quad_rows['D_1000']['baseline_to_fine_change']:.3e} at 100, 500, and 1000 MHz.  Trajectory-step changes are {step_rows['D_100']['baseline_to_fine_change']:.3e}, {step_rows['D_500']['baseline_to_fine_change']:.3e}, and {step_rows['D_1000']['baseline_to_fine_change']:.3e}.

The causal point controls remain separated.  The upstream point-source sequence gives $D_{{\rm eff}}={mesh_rows['D_out']['baseline']:.3e}\,\mathrm{{m^2/s}}$ at baseline and ${mesh_rows['D_out']['fine']:.3e}\,\mathrm{{m^2/s}}$ on the fine field mesh, both numerical-zero scale compared with the finite-kernel result.  The point-source sequence entirely inside the nonuniform region gives ${mesh_rows['D_in']['baseline']:.6e}\,\mathrm{{m^2/s}}$ at baseline and ${mesh_rows['D_in']['fine']:.6e}\,\mathrm{{m^2/s}}$ on the fine mesh.  All seven numerical configurations satisfy the collection and dc Shockley--Ramo integrity checks, and every predeclared convergence gate passes.

A convergence PASS establishes numerical stability of this deterministic surrogate and inverse under the declared refinements.  It does not establish experimental feasibility, device calibration, or uniqueness of the physical interpretation.

\section{{Reproduction record}}

The principal executable files for this supplement are:
\begin{{itemize}}
\item \texttt{{numerics/hgcdte\_ramo\_four\_color\_gradient\_prediction.py}} --- theoretical HgCdTe optical-kernel generator;
\item \texttt{{numerics/realistic\_geometry\_closure\_stress.py}} --- two-dimensional physical and weighting potentials plus deterministic Shockley--Ramo trajectories;
\item \texttt{{numerics/paper02\_kernel\_aware\_depletion\_frequency\_law.py}} --- finite-kernel homogeneous transport inverse;
\item \texttt{{numerics/paper02\_point\_vs\_kernel\_causal\_test.py}} --- upstream and inside-region point-source controls;
\item \texttt{{numerics/paper02\_inference\_convergence\_gate.py}} and \texttt{{paper02\_inference\_convergence\_runner.py}} --- independent numerical-refinement gate.
\end{{itemize}}

The corrected checked convergence execution is GitHub Actions run \texttt{{31948607702}}, job \texttt{{95168474631}}, artifact \texttt{{paper02-inference-convergence}} (artifact id \texttt{{9264012168}}).  The downloaded artifact SHA-256 recorded at validation was \texttt{{ac9c9ade5e658fedd6ff846ee869dcc25d5bb0e4d85dd26a9657e6cf3dfaf275}}.  The immediately preceding execution completed all seven numerical solves but failed in the reporting layer because the low-band metric label was mis-dispatched as a frequency label; it produced no convergence verdict.  That failed route is retained as provenance.

\bibliographystyle{{apsrev4-2}}
\bibliography{{PAPER02_REFERENCES_REV4}}

\end{{document}}
'''
    if r"\author{Anonymous}" not in supp:
        raise RuntimeError("Supplement anonymity guard failed")
    SUPP.write_text(supp, encoding="utf-8")


def main():
    conv = load_checked_convergence()
    build_bibliography()
    build_main(conv)
    build_supplement(conv)
    print(DST)
    print(SUPP)
    print(BIB_DST)


if __name__ == "__main__":
    main()
