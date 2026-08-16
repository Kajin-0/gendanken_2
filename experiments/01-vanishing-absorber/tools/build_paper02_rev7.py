"""Build Paper-02 Rev. 7 from frozen compile-valid Rev. 6 sources.

Rev. 7 is a bounded scientific revision.  It preserves deterministic velocity
heterogeneity as the central counterexample and adds the checked measurement-
covariance / optical-kernel-model uncertainty results developed after Rev. 6.

No theorem, exact-continuum result, optical-kernel definition, canonical figure
data, or exact-known-kernel same-frequency statistical result is removed.
Generalized least-squares / nuisance-projection identities are explicitly framed
as standard local inverse geometry rather than mathematical novelty.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN_SRC = ROOT / "PAPER02_MANUSCRIPT_REV6_ANON_2026-08-16.tex"
SUPP_SRC = ROOT / "PAPER02_SUPPLEMENT_REV6_ANON_2026-08-16.tex"
MAIN_DST = ROOT / "PAPER02_MANUSCRIPT_REV7_ANON_2026-08-16.tex"
SUPP_DST = ROOT / "PAPER02_SUPPLEMENT_REV7_ANON_2026-08-16.tex"

EXPECTED_MAIN_BLOB = "594a38fce4e93cc96df2d45b43c03eb71551ee74"
EXPECTED_SUPP_BLOB = "97ecf3e2b9d8ffd69c227a7c1946d4e7eb544d13"


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
        raise RuntimeError(f"Expected exactly one occurrence, found {n}: {old[:180]!r}")
    return text.replace(old, new, 1)


def common_guard(text: str, label: str) -> None:
    if text.count(r"\author{Anonymous}") != 1:
        raise RuntimeError(f"{label}: anonymity guard failed")
    for pat in (
        r"\bfirst-ever\b",
        r"\bfor the first time\b",
        r"\bfundamental new mechanism\b",
        r"\buniversal false diffusion\b",
        r"\bfirst demonstration\b",
    ):
        if re.search(pat, text, re.I):
            raise RuntimeError(f"{label}: forbidden priority phrase: {pat}")


def build_main() -> None:
    text = frozen(MAIN_SRC, EXPECTED_MAIN_BLOB)

    old_abstract = "A covariance-aware multi-frequency test shows that practical rejection of the wrong homogeneous model is controlled by bandwidth and inverse conditioning rather than structural overdetermination alone. A conditional HgCdTe stress is compared only against independently reported graded-HgCdTe field and timing scales; it is not calibrated to those devices. The result provides an attribution framework for distinguishing microscopic diffusion from finite-kernel coupling to deterministic device heterogeneity in wavelength-resolved transport measurements."
    new_abstract = "A covariance-aware multi-frequency test shows that practical rejection of the wrong homogeneous model is controlled by bandwidth and inverse conditioning rather than structural overdetermination alone. A separate nuisance stress shows that the tested same-frequency ordering survives broad covariance changes, whereas non-affine optical-kernel misspecification can itself generate positive apparent diffusion in a uniform zero-diffusion null; an exact affine depth-scale error does not. Thus the absolute effective coefficient is meaningful only conditional on the optical model and weighting metric. A conditional HgCdTe stress is compared only against independently reported graded-HgCdTe field and timing scales; it is not calibrated to those devices. The result provides an attribution framework for distinguishing microscopic diffusion from finite-kernel coupling to deterministic device heterogeneity in wavelength-resolved transport measurements."
    text = once(text, old_abstract, new_abstract)

    old_results = "We establish four results. First, deterministic downstream acceleration generates the same low-frequency real spatial exponent that a homogeneous inverse associates with positive diffusion. Second, the coupling can be spatially remote: all nominal mean generation depths may lie outside the nonuniform region while finite kernel support inside that region drives the bias. Removing that support collapses the apparent diffusion even if every channel mean is restored exactly. Third, the parameter bias and the same-frequency model residual are different projections of the channel discrepancy; a nuisance can therefore move the recovered root while producing little model-rejection signal. Fourth, additional RF frequencies reject the wrong model only when the covariance-weighted departure from the homogeneous dispersion manifold becomes statistically resolvable. This separates structural overdetermination from practical falsification."
    new_results = "We establish five results. First, deterministic downstream acceleration generates the same low-frequency real spatial exponent that a homogeneous inverse associates with positive diffusion. Second, the coupling can be spatially remote: all nominal mean generation depths may lie outside the nonuniform region while finite kernel support inside that region drives the bias. Removing that support collapses the apparent diffusion even if every channel mean is restored exactly. Third, the parameter bias and the same-frequency model residual are different projections of the channel discrepancy; a nuisance can therefore move the recovered root while producing little model-rejection signal. Fourth, additional RF frequencies reject the wrong model only when the covariance-weighted departure from the homogeneous dispersion manifold becomes statistically resolvable. Fifth, relaxing the exact-kernel assumption reveals a second identifiability boundary: covariance changes the metric defining the pseudo-true effective parameter, and fixed non-affine kernel error can itself project onto the transport-root tangent. This separates structural overdetermination from practical falsification and from optical-model attribution."
    text = once(text, old_results, new_results)

    old_boundary = "The analysis is intentionally framed as a systematic-error and identifiability theory, not as a claim that wavelength-dependent RF photodiode response, field-dependent carrier transport, or effective-parameter bias are individually new phenomena. The contribution is the detector-specific combination of finite generation kernels supplied exactly to the inverse, deterministic velocity heterogeneity, Shockley--Ramo terminal-current inversion, a true-zero-diffusion control, causal support ablations, and quantitative attribution and rejection criteria."
    new_boundary = "The analysis is intentionally framed as a systematic-error and identifiability theory, not as a claim that wavelength-dependent RF photodiode response, field-dependent carrier transport, effective-parameter bias, generalized least squares, nuisance projection, or Schur-complement information are individually new. The central contribution remains the detector-specific combination of finite generation kernels supplied exactly to the inverse, deterministic velocity heterogeneity, Shockley--Ramo terminal-current inversion, a true-zero-diffusion control, causal support ablations, and quantitative attribution and rejection criteria. We then relax the exact-kernel/noise-metric assumptions only to determine how strongly that attribution depends on optical-model and covariance knowledge."
    text = once(text, old_boundary, new_boundary)

    insert_anchor = r"\section{HgCdTe scale example and implications}"
    new_section = r'''
\section{Measurement covariance and optical-model uncertainty}
\label{sec:modeluncertainty}

The central counterexample deliberately supplies the same theoretical kernels to the forward average and inverse so that deterministic velocity heterogeneity can be isolated.  We now relax the measurement metric and optical-model assumptions separately.  The projection identities in this section are standard local generalized-least-squares and nuisance-parameter geometry; they are used here as attribution tools rather than claimed as new mathematics.

\subsection{Covariance changes both significance and the pseudo-true parameter}

For a real-stacked data vector with a small deterministic discrepancy $\bm e$, fitted-model Jacobian $G$, and measurement precision $W=\Sigma^{-1}$, the local generalized-least-squares shift is
\begin{equation}
\boxed{
\delta\bm\theta=(G^T W G)^{-1}G^T W\bm e,
}
\label{eq:generalbias}
\end{equation}
with weighted tangent projector
\begin{equation}
P_W=G(G^T W G)^{-1}G^T W
\end{equation}
and post-fit discrepancy $(I-P_W)\bm e$.  Thus the covariance changes both the parameter-bias direction and the normal distance used for rejection.  More strongly, under model misspecification the pseudo-true parameter
\begin{equation}
\bm\theta_*(W)=\arg\min_{\bm\theta}\|\bm y-\bm f(\bm\theta)\|_W^2
\end{equation}
can itself depend on the metric $W$.

We re-fit the exact-known-kernel heterogeneous response under twelve normalized covariance shapes, including channel equicorrelation and AR(1) correlations through $\rho=0.8$, low-rank common, slope, and curvature directions, and real--imaginary quadrature correlation.  The frequency-dependent ordering is unchanged throughout the tested family: at $100\,\mathrm{MHz}$ one-mode rejection precedes positive-$D$ detection in all 12 cases, whereas at $500\,\mathrm{MHz}$ and $1\,\mathrm{GHz}$ positive $D$ is detectable first in all 12.  The quantitative thresholds move substantially.  At $100\,\mathrm{MHz}$ the required positive-$D$ SNR spans $104.9$--$121.8\,\mathrm{dB}$ and the one-mode rejection threshold spans $95.3$--$102.3\,\mathrm{dB}$; the corresponding spans are $63.1$--$79.7$ versus $81.2$--$88.2\,\mathrm{dB}$ at $500\,\mathrm{MHz}$ and $45.4$--$61.1$ versus $74.8$--$82.3\,\mathrm{dB}$ at $1\,\mathrm{GHz}$.

The fitted effective coefficient is less invariant than this ordering.  At $100\,\mathrm{MHz}$ the same deterministic response yields $D_{\rm eff}$ from $1.66\times10^{-3}$ to $2.61\times10^{-3}\,\mathrm{m^2/s}$ across the tested weighting metrics.  Consequently, once the inverse family is misspecified, the numerical effective parameter is properly a property of the forward response, inverse family, and weighting metric rather than a metric-independent material observable.  A separate cross-frequency stress preserving every single-frequency marginal root covariance but adding AR(1) or equicorrelated RF errors changes the $3\,\mathrm{GHz}$ rejection requirement by at most about $1.1\,\mathrm{dB}$ in the tested family; the strong benefit of extending usable RF bandwidth therefore survives these particular correlations.

\subsection{Fixed optical-kernel error is a distinct nuisance}

Let the nominal kernels depend on optical nuisance coordinates $\bm\alpha$.  A fixed small error $\delta\bm\alpha$ produces channel discrepancy
\begin{equation}
\delta\bm J=B\,\delta\bm\alpha,
\qquad
B_{mj}=\int_0^L
\frac{\partial g_m(z;\bm\alpha)}{\partial\alpha_j}
H(z)\,dz.
\label{eq:kerneljacobian}
\end{equation}
Equation~\eqref{eq:generalbias} then applies with $\bm e=B\delta\bm\alpha$.  A zero-mean random kernel uncertainty may instead contribute $BC_\alpha B^T$ to an effective covariance at linear order, but a fixed or biased calibration error retains its deterministic tangent component.  In particular, if a kernel-nuisance direction lies in the profiled transport-root tangent, same-frequency SNR alone cannot separate the two locally.

Two controls distinguish benign coordinate error from dangerous non-affine error.  First, in the exact uniform-drift, zero-diffusion problem, a global affine depth map $z_{\rm true}=a+bz$ gives $\gamma_{\rm eff}=b\gamma$, $D_{\rm eff}=D/b^2$, and $w_{\rm eff}=w/b$.  An exact continuum calculation verifies that a $1\%$ depth-scale compression, which moves the six kernel means by as much as $18\,\mathrm{nm}$, leaves $|D_{\rm eff}|<4.7\times10^{-14}\,\mathrm{m^2/s}$ through $1\,\mathrm{GHz}$.  A pure affine depth-scale error therefore cannot create positive diffusion from exact $D=0$.

Second, non-affine channel-dependent kernel errors can.  As a controlled sensitivity coordinate, perturb the six optical wavelengths by
\begin{equation}
\delta\lambda_m=A(-1,-0.6,-0.2,0.2,0.6,1)_m.
\end{equation}
In the same exact uniform-velocity, $D_{\rm micro}=0$ null, while the inverse continues to use the nominal kernels, $A=0.02997\,\mathrm{nm}$ produces
\begin{equation}
D_{\rm eff}(100\,\mathrm{MHz})=2.6182\times10^{-3}\,\mathrm{m^2/s},
\end{equation}
matching the central heterogeneous exact-continuum value.  The resulting maximum change of a kernel mean is only $0.206\,\mathrm{nm}$, the one-mode relative residual is $3.1\times10^{-8}$, and under the reference covariance positive $D$ reaches the stated detection power at $115.2\,\mathrm{dB}$ while same-frequency one-mode rejection requires $156.8\,\mathrm{dB}$.  A separately signed curvature-shaped wavelength nuisance can reproduce the same target at amplitude $-0.00294\,\mathrm{nm}$ with a maximum mean-depth change of $0.020\,\mathrm{nm}$.

These sub-nanometer wavelength amplitudes are \emph{not} instrument calibration specifications or empirical error bars.  They parameterize particular theoretical perturbations of the wavelength-to-generation-kernel map, so their role is to expose conditioning and tangent alignment.  The experimentally relevant requirement is instead to constrain the kernel-nuisance subspace that overlaps the transport tangent.  The exact-known-kernel assumption is therefore load-bearing for interpreting the magnitude of $D_{\rm eff}$ as a material parameter, even though the deterministic velocity-heterogeneity counterexample itself remains independently established under that assumption.

'''
    if text.count(insert_anchor) != 1:
        raise RuntimeError("main: HgCdTe insertion anchor missing or duplicated")
    text = text.replace(insert_anchor, new_section + insert_anchor, 1)

    old_discussion = "Three aspects make the attribution problem particularly severe. First, supplying the exact theoretical optical kernels removes optical-model uncertainty from the controlled inverse but cannot make the underlying point-source transport homogeneous. Exact knowledge of $g_m(z)$ therefore does not by itself eliminate Eq.~\\eqref{eq:leakage}. Second, same-frequency model residual and parameter bias probe different directions in channel space. A nuisance nearly tangent to the kernel-aware model can strongly move the root while producing a very small fit residual. Third, the low-frequency homogeneous diffusion family itself has enough freedom to reproduce the first two frequency coefficients of a different analytic response. Practical rejection therefore begins with higher-order frequency structure and can require substantially more bandwidth than an identification calculation alone would suggest."
    new_discussion = "Four aspects make the attribution problem particularly severe. First, supplying the exact theoretical optical kernels isolates velocity heterogeneity but cannot make the underlying point-source transport homogeneous; exact knowledge of $g_m(z)$ therefore does not eliminate Eq.~\\eqref{eq:leakage}. Second, once those kernels are uncertain, fixed optical-model error can itself have a transport-tangent component, so exact kernel knowledge is a load-bearing condition for interpreting the fitted magnitude. Third, same-frequency model residual and parameter bias probe different directions in channel space, and their geometry depends on the measurement metric. A nuisance nearly tangent to the kernel-aware model can strongly move the root while producing a very small fit residual. Fourth, the low-frequency homogeneous diffusion family itself has enough freedom to reproduce the first two frequency coefficients of a different analytic response. Practical rejection therefore begins with higher-order frequency structure and can require substantially more bandwidth than an identification calculation alone would suggest."
    text = once(text, old_discussion, new_discussion)

    old_supp_sentence = "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the predeclared inferential convergence gate, the post-hoc exact-planar continuum cross-check, and executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the apparent $D_{\\rm eff}$ counterexample."
    new_supp_sentence = "The Supplemental Material accompanying this revision specifies the theoretical optical-kernel construction, six channel wavelengths and moments, the separate planar-depletion deterministic transport stress, the predeclared inferential convergence gate, the post-hoc exact-planar continuum cross-check, and the covariance/kernel-uncertainty stresses with executable workflow provenance.  The optical-kernel and transport-stress models are documented separately because the former supplies theoretical generation profiles whereas the latter generates the central apparent $D_{\\rm eff}$ counterexample."
    text = once(text, old_supp_sentence, new_supp_sentence)

    old_limit = "The framework has several limitations. The main numerical stress treats deterministic one-carrier transport and omits microscopic diffusion specifically so that the source of $\\Deff$ is unambiguous.  The optical kernels are likewise treated as known exactly; uncertainty in absorption, composition, interference, wavelength calibration, or the inferred kernel shapes would generate additional channel-space tangent and normal errors and must be propagated in an experiment. A real detector can contain both true diffusion and deterministic heterogeneity, in which case the inverse bias adds to rather than replaces the material contribution. The first-order bound assumes a locally regular, uniquely identified one-mode solution and does not yet propagate uncertainty in the supplied optical kernels or electrostatic model itself. The statistical example uses an intentionally simple independent equal-quadrature noise model. Frequency-dependent electronic noise, parasitics, correlated calibration errors, and optimized measurement-time allocation will change the quantitative SNR requirement."
    new_limit = "The framework has several limitations. The main numerical stress treats deterministic one-carrier transport and omits microscopic diffusion specifically so that the source of $\\Deff$ is unambiguous.  The optical-model extension tests controlled nuisance directions rather than a validated experimental error distribution; its wavelength amplitudes therefore quantify conditioning of this surrogate and must not be read as instrument specifications. A real detector can contain true diffusion, deterministic heterogeneity, and optical-model error simultaneously, in which case the biases need not add linearly outside the local regime. The first-order projection formulas assume a locally regular, uniquely identified one-mode solution. The covariance study spans deliberately broad structured families but is not a proof for arbitrary covariance, and it omits frequency-dependent parasitics, full electrostatic-model uncertainty, and optimized measurement-time allocation."
    text = once(text, old_limit, new_limit)

    old_extensions = "These limitations suggest direct extensions. A nuisance-aware joint model could include parameterized electrostatic profiles and compare their Fisher directions with those of microscopic diffusion. Wavelengths could be selected not only for depth separation but also to minimize restricted overlap with poorly characterized device regions or to maximize the normal distance between competing transport models. Multi-frequency experimental design could likewise allocate information where the heterogeneous and homogeneous dispersion manifolds diverge most strongly rather than uniformly increasing precision at all frequencies."
    new_extensions = "These limitations suggest direct extensions. A nuisance-aware joint model could include parameterized electrostatic and optical-kernel coordinates and compare their conditioned information with that of microscopic diffusion. Wavelengths could be selected not only for depth separation but also to reduce overlap between kernel-calibration and transport-root tangents or to maximize the normal distance between competing transport models. Multi-frequency experimental design could likewise allocate information where the heterogeneous, optical-nuisance, and homogeneous-diffusion manifolds diverge most strongly rather than uniformly increasing precision at all frequencies."
    text = once(text, old_extensions, new_extensions)

    old_conclusion_tail = "Additional RF frequencies provide a falsification route, but structural overdetermination is not equivalent to statistical power. A covariance-weighted manifold test shows that bandwidth can provide substantially more nuisance discrimination than extreme precision confined to the low-frequency tangent regime. Together, the support bound, parameter-bias law, and multi-frequency rejection criterion provide a framework for separating microscopic material diffusion from deterministic device heterogeneity in wavelength-resolved photodetector transport measurements."
    new_conclusion_tail = "Additional RF frequencies provide a falsification route, but structural overdetermination is not equivalent to statistical power. A covariance-weighted manifold test shows that bandwidth can provide substantially more nuisance discrimination than extreme precision confined to the low-frequency tangent regime. The optical-model stress adds a stricter attribution condition: a fitted diffusion magnitude is material-like only to the extent that kernel-nuisance directions overlapping the transport tangent are independently constrained. Together, the support bound, parameter-bias law, nuisance-conditioned projection geometry, and multi-frequency rejection criterion provide a framework for separating microscopic material diffusion from deterministic device heterogeneity and optical-model error in wavelength-resolved photodetector transport measurements."
    text = once(text, old_conclusion_tail, new_conclusion_tail)

    required = (
        r"\section{Measurement covariance and optical-model uncertainty}",
        r"\delta\bm\theta=(G^T W G)^{-1}G^T W\bm e",
        "one-mode rejection precedes positive-$D$ detection in all 12 cases",
        r"1.66\times10^{-3}",
        r"|D_{\rm eff}|<4.7\times10^{-14}",
        r"A=0.02997\,\mathrm{nm}",
        r"A=0.00294\,\mathrm{nm}",
        "not instrument calibration specifications or empirical error bars",
        "generalized least squares, nuisance projection, or Schur-complement information",
    )
    for phrase in required:
        if phrase not in text:
            raise RuntimeError(f"main missing required Rev7 phrase: {phrase}")
    for forbidden in (
        "does not yet propagate uncertainty in the supplied optical kernels",
        "The optical kernels are likewise treated as known exactly; uncertainty in absorption",
    ):
        if forbidden in text:
            raise RuntimeError(f"main retained superseded limitation phrase: {forbidden}")
    common_guard(text, "main")
    MAIN_DST.write_text(text, encoding="utf-8")


def build_supp() -> None:
    text = frozen(SUPP_SRC, EXPECTED_SUPP_BLOB)

    anchor = r"\section{Reproduction record}"
    new_section = r'''
\section{Covariance and optical-kernel uncertainty stresses}

The central velocity-heterogeneity result uses the theoretical kernels in Table~I exactly in both forward and inverse calculations.  The additional calculations in this section deliberately relax either the measurement covariance or the optical-kernel model, but not both simultaneously.  Their purpose is to test attribution robustness, not to supply experimental calibration tolerances.

\subsection{Structured covariance stress}

For one RF frequency the six complex channels are represented by a 12-component real vector.  Covariance shapes are normalized to unit mean quadrature variance so the RMS-channel SNR remains comparable.  The one-mode parameters $(\Re C,\Im C,\Re K,\Im K,\Re r,\Im r)$ are re-fit by generalized least squares for every covariance; the IID root is not held fixed.  The tested shapes comprise IID noise, channel equicorrelation and AR(1) correlations with $\rho=0.25,0.50,0.80$, rank-one common, spectral-slope, and spectral-curvature covariance directions with a 10:1 pre-normalization eigenvalue ratio, and real--imaginary quadrature correlations $q=\pm0.5$.

\begin{table}[h]
\caption{Same-frequency SNR ranges over the 12 tested covariance shapes for the exact-known-kernel heterogeneous response.  Ranges are in dB.}
\centering
\begin{tabular}{cccc}
\toprule
RF & positive-$D$ detection & one-mode rejection & ordering in all cases\\
\midrule
100 MHz & 104.9--121.8 & 95.3--102.3 & rejection first\\
500 MHz & 63.1--79.7 & 81.2--88.2 & positive $D$ first\\
1 GHz   & 45.4--61.1 & 74.8--82.3 & positive $D$ first\\
\bottomrule
\end{tabular}
\end{table}

Although the ordering is unchanged in this family, the 100-MHz pseudo-true $D_{\rm eff}$ spans $1.660\times10^{-3}$--$2.610\times10^{-3}\,\mathrm{m^2/s}$ because the closest point on the misspecified homogeneous manifold depends on the weighting metric.  A separate cumulative-RF stress preserves each marginal root covariance while imposing AR(1) or equicorrelated cross-frequency errors through $\rho=0.8$.  The required SNR through $3\,\mathrm{GHz}$ spans $59.9$--$65.3\,\mathrm{dB}$ around the IID value $64.2\,\mathrm{dB}$, so the bandwidth benefit survives these tested correlations.

\subsection{Exact affine depth-coordinate control}

The uniform deterministic reference has $D_{\rm micro}=0$ and velocity $v=2.92697\times10^4\,\mathrm{m/s}$.  To test a pure coordinate-scale error without finite-grid kernel warping, the nominal kernel coordinate $u$ is retained and the analytic point response is evaluated at
\begin{equation}
z_{\rm true}=z_c+b(u-z_c).
\end{equation}
For a uniform exponential spatial law this gives $\gamma_{\rm eff}=b\gamma$, $D_{\rm eff}=D/b^2$, and $w_{\rm eff}=w/b$.  Direct integrations for $b=0.990$, 0.995, and 1.000 at 100 MHz, 500 MHz, and 1 GHz give
\begin{equation}
\max |D_{\rm eff}|=4.67\times10^{-14}\,\mathrm{m^2/s},
\end{equation}
maximum relative drift error $1.49\times10^{-14}$, and maximum one-mode relative residual $7.73\times10^{-16}$.  At $b=0.990$ the nominal kernel means move by as much as $18\,\mathrm{nm}$.  This control therefore distinguishes a global affine depth-scale error from the non-affine errors below.

\subsection{Signed non-affine kernel perturbations}

The true uniform-drift channels are regenerated with perturbed theoretical optical kernels while the inverse continues to use the nominal kernels.  Three signed wavelength-registration modes are examined locally: common, channel-linear, and channel-curvature patterns.  At $100\,\mathrm{MHz}$ all three possess a sign for which the infinitesimal apparent diffusion is positive and reaches the stated positive-$D$ detection power before same-frequency one-mode rejection.  For the channel-linear mode
\begin{equation}
\delta\lambda_m=A(-1,-0.6,-0.2,0.2,0.6,1)_m,
\end{equation}
the local derivative at zero error is
\begin{equation}
\frac{dD_{\rm eff}}{dA}=8.513\times10^{-2}\,
\frac{\mathrm{m^2/s}}{\mathrm{nm}},
\end{equation}
and the asymptotic ratio of rejection SNR to positive-$D$ detection SNR is 72.7.  For the signed curvature mode the corresponding derivative magnitude is $8.899\times10^{-1}\,\mathrm{m^2/(s\,nm)}$ and the asymptotic SNR ratio is 14.0.  These first-order predictions agree with an independent nonlinear inverse at the $10^{-3}\,\mathrm{nm}$ finite-difference scale.

Using the exact heterogeneous 100-MHz value $D_{\rm target}=2.618164535\times10^{-3}\,\mathrm{m^2/s}$ only as a comparison scale, the exact uniform $D=0$ null reaches the same apparent value for the channel-linear mode at $A=+0.0299713\,\mathrm{nm}$.  The maximum shift of a kernel mean is then $0.205754\,\mathrm{nm}$, the one-mode relative residual is $3.09\times10^{-8}$, and the reference-covariance thresholds are $115.22\,\mathrm{dB}$ for positive-$D$ detection and $156.81\,\mathrm{dB}$ for one-mode rejection.  A curvature-shaped nuisance reaches the same target for signed amplitude $A=-0.00294205\,\mathrm{nm}$, maximum mean-depth shift $0.020041\,\mathrm{nm}$, and thresholds $115.23$ and $138.14\,\mathrm{dB}$, respectively.

The amplitudes above are coordinates in a controlled perturbation of the theoretical wavelength-to-kernel map.  They are not wavelength-meter specifications, measured calibration errors, or error bars for a real detector.  Their role is to demonstrate that non-affine optical-model directions can be nearly tangent to the transport inverse even when a much larger affine depth displacement leaves $D=0$ exactly.

\subsection{Model-uncertainty workflow provenance}

The checked calculations are version controlled by
\begin{itemize}
\item \texttt{numerics/paper02\_covariance\_geometry\_stress.py}, workflow run 31953328287;
\item \texttt{numerics/paper02\_kernel\_misspecification\_stress.py}, successful artifact-producing workflow run 31953612225;
\item \texttt{numerics/paper02\_exact\_affine\_depth\_control.py}, workflow run 31953979410;
\item \texttt{numerics/paper02\_kernel\_nuisance\_tangent\_projection\_v2.py}, workflow run 31954048251;
\item \texttt{numerics/paper02\_signed\_kernel\_mode\_thresholds.py}, workflow run 31954087223.
\end{itemize}
The frequency-aware ``v2'' nuisance projection supersedes only the 500-MHz and 1-GHz diffusion-derivative fields in its first version, which had inherited a 100-MHz-fixed angular frequency from an earlier validation helper.  The first version's 100-MHz row and its channel-space tangent/normal projections were unaffected.  Repository provenance retains both calculations.

'''
    if text.count(anchor) != 1:
        raise RuntimeError("supplement: reproduction anchor missing or duplicated")
    text = text.replace(anchor, new_section + anchor, 1)

    old_scope = "The manuscript uses two distinct numerical constructions that must not be conflated.  First, a one-dimensional monotonic graded-HgCdTe optical model is used only to generate six finite, wavelength-dependent theoretical generation kernels $g_m(z)$.  Those same generated kernel shapes are supplied exactly to the forward averaging and to the kernel-aware inverse.  They are not measured or experimentally calibrated kernels from a specific detector.  Second, the central apparent-diffusion counterexample is generated by a separate deterministic planar-depletion transport stress with microscopic diffusion fixed to zero.  The graded optical-kernel model therefore determines how the point-source response is sampled; it is not the electrostatic transport model that generates the counterexample."
    new_scope = "The manuscript uses two distinct numerical constructions that must not be conflated.  First, a one-dimensional monotonic graded-HgCdTe optical model is used only to generate six finite, wavelength-dependent theoretical generation kernels $g_m(z)$.  Those same generated kernel shapes are supplied exactly to the forward averaging and to the kernel-aware inverse for the central velocity-heterogeneity counterexample; they are not measured or experimentally calibrated kernels from a specific detector.  Second, the central apparent-diffusion counterexample is generated by a separate deterministic planar-depletion transport stress with microscopic diffusion fixed to zero.  The graded optical-kernel model therefore determines how the point-source response is sampled; it is not the electrostatic transport model that generates the counterexample.  A later, separately labeled uncertainty stress then perturbs the true kernels while leaving the inverse kernels nominal in order to test how load-bearing the exact-kernel assumption is."
    text = once(text, old_scope, new_scope)

    required = (
        r"\section{Covariance and optical-kernel uncertainty stresses}",
        r"\max |D_{\rm eff}|=4.67\times10^{-14}",
        r"A=+0.0299713\,\mathrm{nm}",
        r"A=-0.00294205\,\mathrm{nm}",
        "workflow run 31953328287",
        "workflow run 31954087223",
        "not wavelength-meter specifications",
        "frequency-aware ``v2'' nuisance projection",
    )
    for phrase in required:
        if phrase not in text:
            raise RuntimeError(f"supplement missing required Rev7 phrase: {phrase}")
    common_guard(text, "supplement")
    SUPP_DST.write_text(text, encoding="utf-8")


def main() -> None:
    build_main()
    build_supp()
    print(f"wrote {MAIN_DST.name}")
    print(f"wrote {SUPP_DST.name}")


if __name__ == "__main__":
    main()
