"""Build Paper-02 Rev. 6 from frozen Rev. 5 sources.

Bounded hostile-review revision only.  Rev. 6 adds the checked POST-HOC exact
planar continuum cross-check, narrows acceleration-sign language, removes an
unneeded HgCdTe thickness attribution, and labels the surrogate mobility and
saturation speed as illustrative rather than calibrated.  The theorem, optical
kernels, figure datasets, same-frequency statistics, and multi-frequency noise
model are unchanged.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN_SRC = ROOT / "PAPER02_MANUSCRIPT_REV5_ANON_2026-08-16.tex"
SUPP_SRC = ROOT / "PAPER02_SUPPLEMENT_REV5_ANON_2026-08-16.tex"
MAIN_DST = ROOT / "PAPER02_MANUSCRIPT_REV6_ANON_2026-08-16.tex"
SUPP_DST = ROOT / "PAPER02_SUPPLEMENT_REV6_ANON_2026-08-16.tex"
CROSS = ROOT / "numerics/results/paper02_exact_planar_continuum_crosscheck_summary.json"

EXPECTED_MAIN_BLOB = "d61023ee44b7a8b365cf15f6dce579dff4f8a045"
EXPECTED_SUPP_BLOB = "5b6499c24be70164ea25791e19d143f61197195b"


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def frozen(path: Path, expected: str) -> str:
    data = path.read_bytes()
    got = blob_sha(data)
    if got != expected:
        raise RuntimeError(f"Frozen source changed: {path.name}: {got} != {expected}")
    return data.decode("utf-8")


def once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"Expected one occurrence, found {n}: {old[:160]!r}")
    return text.replace(old, new, 1)


def common_guard(text: str, label: str) -> None:
    if text.count(r"\author{Anonymous}") != 1:
        raise RuntimeError(f"{label}: anonymity guard failed")
    for pat in (
        r"\bfirst-ever\b",
        r"\bfor the first time\b",
        r"\bfundamental new mechanism\b",
        r"\buniversal false diffusion\b",
    ):
        if re.search(pat, text, re.I):
            raise RuntimeError(f"{label}: forbidden priority phrase: {pat}")


def crosscheck() -> dict:
    x = json.loads(CROSS.read_text(encoding="utf-8"))
    assert x["comparison"]["overall_pass_against_existing_tolerances"] is True
    assert "POST-HOC" in x["status"]
    return x


def build_main() -> None:
    text = frozen(MAIN_SRC, EXPECTED_MAIN_BLOB)

    text = once(
        text,
        "Independent linear and exponential velocity profiles give positive apparent diffusion for downstream acceleration, zero diffusion for uniform velocity, and negative apparent diffusion for deceleration. A covariance-aware multi-frequency test shows that practical rejection of the wrong homogeneous model is controlled by bandwidth and inverse conditioning rather than structural overdetermination alone.",
        "Independent linear and exponential velocity profiles give positive apparent diffusion for downstream acceleration, zero diffusion for uniform velocity, and negative apparent diffusion for deceleration. A post-hoc exact full-contact planar continuum calculation removes the electrostatic mesh and trajectory stepping from the central stress and reproduces the numerical-baseline $D_{\\rm eff}$ within $0.32\\%$ at $100\\,\\mathrm{MHz}$ and below $0.1\\%$ at $500\\,\\mathrm{MHz}$ and $1\\,\\mathrm{GHz}$. A covariance-aware multi-frequency test shows that practical rejection of the wrong homogeneous model is controlled by bandwidth and inverse conditioning rather than structural overdetermination alone.",
    )

    text = once(
        text,
        "A conditional HgCdTe stress uses thickness and internal-field scales independently reported for graded HgCdTe devices.",
        "A conditional HgCdTe stress is compared only against independently reported graded-HgCdTe field and timing scales; it is not calibrated to those devices.",
    )

    text = once(
        text,
        "The preceding results do not depend on HgCdTe specifically.  This section checks only whether the geometric and effective-field scales used by the conditional stress have independent precedent in HgCdTe; it does not validate the modeled velocity profile or the predicted $D_{\\rm eff}$ for any published detector.  We use the existing theoretical HgCdTe kernel construction as a scale example because independently published graded HgCdTe devices provide relevant thickness, field, and timing benchmarks.",
        "The preceding results do not depend on HgCdTe specifically.  This section checks only whether the effective-field and timing scales used by the conditional stress have independent precedent in HgCdTe; it does not validate the modeled velocity profile or the predicted $D_{\\rm eff}$ for any published detector.  We use the existing theoretical HgCdTe kernel construction as a scale example because independently published graded HgCdTe studies provide relevant field and timing benchmarks.",
    )

    text = once(
        text,
        "A published compositionally graded HgCdTe sample has a reported processed thickness near $7.6\\,\\mu\\mathrm{m}$ and calculated composition-gradient built-in fields of approximately $100$--$200\\,\\mathrm{V/cm}$ in the linear graded region, with stronger local surface fields when a nonlinear composition region is retained \\cite{xu2023graded}.",
        "A published compositionally graded HgCdTe study reports calculated composition-gradient built-in fields of approximately $100$--$200\\,\\mathrm{V/cm}$ in the linear graded region, with stronger local surface fields when a nonlinear composition region is retained \\cite{xu2023graded}.",
    )

    text = once(
        text,
        "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the independently refined inferential convergence gate, and executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the apparent $D_{\\rm eff}$ counterexample.",
        "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the predeclared inferential convergence gate, the post-hoc exact-planar continuum cross-check, and executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the apparent $D_{\\rm eff}$ counterexample.",
    )

    old_conv = "The nonlinear inference was also subjected to an independent numerical-convergence gate rather than relying only on the earlier raw closure-phase check.  Around the manuscript baseline, the two-dimensional electrostatic/weighting mesh, source-kernel quadrature, and trajectory step were refined one at a time.  The field mesh was the limiting coordinate: baseline-to-fine changes in $D_{\\rm eff}$ were $1.648\\%$, $1.641\\%$, and $1.633\\%$ at $100\\,\\mathrm{MHz}$, $500\\,\\mathrm{MHz}$, and $1\\,\\mathrm{GHz}$, respectively, all below the predeclared $2\\%$ gate.  The fine-mesh $100\\,\\mathrm{MHz}$ value was $2.6535e-03\\,\\mathrm{m^2/s}$.  Source-quadrature and trajectory-step refinements changed the three probe-frequency diffusion estimates only at approximately $3.3$--$3.8\\times10^{-5}$ and $5.0$--$8.2\\times10^{-6}$ relative, respectively.  The upstream point-source null remained at numerical-zero scale ($10^{-12}$--$10^{-11}\\,\\mathrm{m^2/s}$), whereas the inside-region point-source control remained near $4.87\\times10^{-3}\\,\\mathrm{m^2/s}$.  All predeclared convergence and Shockley--Ramo integrity checks passed.  These tests establish numerical stability of the stated deterministic surrogate and inverse, not experimental calibration or uniqueness of the mechanism in a real device."
    new_conv = "The nonlinear inference was first subjected to an independent predeclared numerical-convergence gate rather than relying only on the earlier raw closure-phase check.  Around the manuscript baseline, the two-dimensional electrostatic/weighting mesh, source-kernel quadrature, and trajectory step were refined one at a time.  The field mesh was the limiting coordinate: baseline-to-fine changes in $D_{\\rm eff}$ were $1.648\\%$, $1.641\\%$, and $1.633\\%$ at $100\\,\\mathrm{MHz}$, $500\\,\\mathrm{MHz}$, and $1\\,\\mathrm{GHz}$, respectively, all below the predeclared $2\\%$ stability gate.  Source-quadrature and trajectory-step changes were much smaller, and the upstream/inside-region causal split survived every refinement.  This refinement sequence is a stability test and should not itself be interpreted as a monotone extrapolation to the continuum.\n\nBecause the central case has a full-width contact, a later hostile review identified a stronger mesh-free check: the planar electrostatic potential has the exact piecewise solution given in the Supplemental Material and $\\phi_w=z/L$.  A deliberately labeled post-hoc continuum calculation therefore evaluates the same deterministic Shockley--Ramo transfer and kernel-aware inverse without the two-dimensional field mesh or trajectory stepping.  It gives $D_{\\rm eff}=2.6182\\times10^{-3}$, $2.5508\\times10^{-3}$, and $2.3506\\times10^{-3}\\,\\mathrm{m^2/s}$ at $100\\,\\mathrm{MHz}$, $500\\,\\mathrm{MHz}$, and $1\\,\\mathrm{GHz}$.  The corresponding numerical-baseline values differ by only $0.320\\%$, $0.087\\%$, and $0.071\\%$; the inferred drift scales differ by about $0.03\\%$.  The exact upstream point-source sequence remains at numerical-zero scale ($4.5\\times10^{-11}\\,\\mathrm{m^2/s}$), while the exact inside-region control is $4.8706\\times10^{-3}\\,\\mathrm{m^2/s}$.  This post-hoc cross-check strengthens numerical attribution inside the stated deterministic surrogate; it does not convert the synthetic model into an experimentally calibrated device or establish uniqueness in a real detector."
    text = once(text, old_conv, new_conv)

    text = once(
        text,
        "A positive diffusion coefficient obtained from wavelength-resolved photodetector transport data need not be a unique signature of microscopic diffusion. In deterministic zero-diffusion models, finite generation kernels that overlap a region of spatially varying carrier velocity can produce a terminal-current response that a homogeneous drift--diffusion inverse interprets as $\\Deff>0$. The effect is sign controlled by deterministic acceleration, survives exact finite-kernel fitting, and can remain close to the homogeneous low-RF dispersion law over a finite bandwidth.",
        "A positive diffusion coefficient obtained from wavelength-resolved photodetector transport data need not be a unique signature of microscopic diffusion. In deterministic zero-diffusion models, finite generation kernels that overlap a region of spatially varying carrier velocity can produce a terminal-current response that a homogeneous drift--diffusion inverse interprets as $\\Deff>0$.  At the point-source level, monotonic downstream acceleration gives a positive quadratic apparent-diffusion coefficient; in the tested linear and exponential finite-kernel families the fitted sign follows the velocity-gradient direction.  The positive accelerating cases survive exact finite-kernel fitting and can remain close to the homogeneous low-RF dispersion law over a finite bandwidth.",
    )

    required = (
        "post-hoc exact full-contact planar continuum calculation",
        r"2.6182\times10^{-3}",
        r"0.320\%",
        "This refinement sequence is a stability test",
        "compared only against independently reported graded-HgCdTe field and timing scales",
        "monotonic downstream acceleration gives a positive quadratic apparent-diffusion coefficient",
    )
    for phrase in required:
        if phrase not in text:
            raise RuntimeError(f"main missing required Rev6 phrase: {phrase}")
    for forbidden in (
        "reported processed thickness near",
        "uses thickness and internal-field scales independently reported",
        "The effect is sign controlled by deterministic acceleration",
    ):
        if forbidden in text:
            raise RuntimeError(f"main retained forbidden Rev5 phrase: {forbidden}")
    common_guard(text, "main")
    MAIN_DST.write_text(text, encoding="utf-8")


def build_supp() -> None:
    text = frozen(SUPP_SRC, EXPECTED_SUPP_BLOB)

    text = once(
        text,
        "with $\\mu=0.90\\,\\mathrm{m^2/(V\\,s)}$ and $v_{\\rm sat}=6.0\\times10^4\\,\\mathrm{m/s}$.  Along each deterministic trajectory",
        "with $\\mu=0.90\\,\\mathrm{m^2/(V\\,s)}$ and $v_{\\rm sat}=6.0\\times10^4\\,\\mathrm{m/s}$.  These two transport values define the illustrative surrogate coordinate; they are not fitted to, or claimed as a calibration of, either cited graded-HgCdTe device.  Along each deterministic trajectory",
    )

    anchor = "A convergence PASS establishes numerical stability of this deterministic surrogate and inverse under the declared refinements.  It does not establish experimental feasibility, device calibration, or uniqueness of the physical interpretation.\n\n\\section{Reproduction record}"
    added = r'''A convergence PASS establishes numerical stability of this deterministic surrogate and inverse under the declared refinements.  It does not establish experimental feasibility, device calibration, or uniqueness of the physical interpretation.

\section{Post-hoc exact planar continuum cross-check}

The full-contact central case admits an additional check that eliminates the two-dimensional electrostatic mesh.  This check was designed \emph{after} the mesh-refinement result was known and is therefore explicitly post-hoc rather than a predeclared convergence gate.  In the full-contact planar limit, Eq.~\eqref{eq:planar-poisson} gives the physical potential exactly and the weighting potential is
\begin{equation}
\phi_w(z)=\frac{z}{L}.
\end{equation}
Using the same saturated-drift law, define
\begin{equation}
T(z)=\int_0^z\frac{du}{v(u)}.
\end{equation}
The exact planar point-source terminal transfer is
\begin{equation}
H(z,\omega)=\frac{e^{i\omega T(z)}}{L}\int_z^L e^{-i\omega T(x)}\,dx,
\end{equation}
which obeys $H(z,0)=1-z/L$.  The same six theoretical optical kernels and the same kernel-aware homogeneous inverse are then used.

\begin{table}[h]
\caption{Fresh numerical baseline compared with the post-hoc exact-planar continuum calculation.}
\centering
\begin{tabular}{cccc}
\toprule
RF & Numerical $D_{\rm eff}$ & Exact $D_{\rm eff}$ & Relative difference\\
 & \multicolumn{2}{c}{($\mathrm{m^2/s}$)} & (\%)\\
\midrule
100 MHz & 0.002609795 & 0.002618165 & 0.320\\
500 MHz & 0.002548603 & 0.002550831 & 0.087\\
1 GHz   & 0.002348945 & 0.002350618 & 0.071\\
\bottomrule
\end{tabular}
\end{table}

The exact-continuum low-band joint fit gives $D_{\rm eff}=2.610344\times10^{-3}\,\mathrm{m^2/s}$ and $w_{\rm eff}=2.569862\times10^4\,\mathrm{m/s}$.  The 100-MHz-anchored homogeneous-law residual at 1 GHz is $8.9163\times10^{-3}$, differing from the numerical baseline by only $3.11\times10^{-5}$ absolute.  The maximum one-mode finite-kernel fit residual through 1 GHz differs by $3.00\times10^{-7}$ absolute.

The causal split is also retained without the field mesh.  The exact upstream point-source sequence gives $D_{\rm eff}=4.49\times10^{-11}\,\mathrm{m^2/s}$, whereas the exact sequence inside the nonuniform region gives $D_{\rm eff}=4.870586\times10^{-3}\,\mathrm{m^2/s}$.  The continuum comparison satisfies every previously declared numerical-convergence tolerance scale, but the agreement remains explicitly post-hoc because this check was designed after inspection of the mesh-refinement result.

\section{Reproduction record}'''
    text = once(text, anchor, added)

    text = once(
        text,
        "\\item \\texttt{numerics/paper02\\_inference\\_convergence\\_gate.py} and \\texttt{paper02\\_inference\\_convergence\\_runner.py} --- independent numerical-refinement gate.\n\\end{itemize}",
        "\\item \\texttt{numerics/paper02\\_inference\\_convergence\\_gate.py} and \\texttt{paper02\\_inference\\_convergence\\_runner.py} --- independent predeclared numerical-refinement gate;\n\\item \\texttt{numerics/paper02\\_exact\\_planar\\_continuum\\_crosscheck.py} --- post-hoc mesh-free full-contact continuum cross-check.\n\\end{itemize}",
    )

    old_record = "The corrected checked convergence execution is GitHub Actions run \\texttt{31948607702}, job \\texttt{95168474631}, artifact \\texttt{paper02-inference-convergence} (artifact id \\texttt{9264012168}).  The downloaded artifact SHA-256 recorded at validation was \\texttt{ac9c9ade5e658fedd6ff846ee869dcc25d5bb0e4d85dd26a9657e6cf3dfaf275}.  The immediately preceding execution completed all seven numerical solves but failed in the reporting layer because the low-band metric label was mis-dispatched as a frequency label; it produced no convergence verdict.  That failed route is retained as provenance."
    new_record = old_record + "\n\nThe post-hoc exact-planar continuum execution is GitHub Actions run \\texttt{31951040229}, job \\texttt{95174419655}, artifact \\texttt{paper02-exact-planar-continuum-crosscheck} (artifact id \\texttt{9264645817}); the uploaded artifact ZIP SHA-256 is \\texttt{1bccc68a1496c3db4fb30cc7fcd4dd6e649eb0f2206c5e6379cce51a675ab3d7}.  Its repository record explicitly retains the POST-HOC label."
    text = once(text, old_record, new_record)

    for phrase in (
        r"\section{Post-hoc exact planar continuum cross-check}",
        r"\phi_w(z)=\frac{z}{L}",
        "0.002618165",
        r"4.870586\times10^{-3}",
        "not fitted to, or claimed as a calibration of",
        "31951040229",
        "9264645817",
    ):
        if phrase not in text:
            raise RuntimeError(f"supplement missing required Rev6 phrase: {phrase}")
    common_guard(text, "supplement")
    SUPP_DST.write_text(text, encoding="utf-8")


def main() -> None:
    crosscheck()
    build_main()
    build_supp()
    print(MAIN_DST)
    print(SUPP_DST)


if __name__ == "__main__":
    main()
