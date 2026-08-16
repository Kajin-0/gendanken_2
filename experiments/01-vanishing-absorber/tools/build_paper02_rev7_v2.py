"""Robust deterministic builder for Paper-02 Rev. 7.

This is additive provenance after the first Rev-7 builder failed on a brittle
whole-paragraph anchor.  It reads the exact frozen compile-valid Rev. 6 blobs,
uses section-boundary insertion rather than long prose matching, switches both
documents to the Rev. 7 bibliography, and adds the checked covariance/kernel-
uncertainty results plus the Ashry--Fares prior-art boundary.
"""
from __future__ import annotations
import hashlib,re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MS=ROOT/'PAPER02_MANUSCRIPT_REV6_ANON_2026-08-16.tex'
SS=ROOT/'PAPER02_SUPPLEMENT_REV6_ANON_2026-08-16.tex'
MD=ROOT/'PAPER02_MANUSCRIPT_REV7_ANON_2026-08-16.tex'
SD=ROOT/'PAPER02_SUPPLEMENT_REV7_ANON_2026-08-16.tex'
MSHA='594a38fce4e93cc96df2d45b43c03eb71551ee74'
SSHA='97ecf3e2b9d8ffd69c227a7c1946d4e7eb544d13'

def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def frozen(p,s):
    b=p.read_bytes(); g=blob(b)
    if g!=s: raise RuntimeError(f'frozen blob changed {p.name}: {g} != {s}')
    return b.decode()
def insert_before(t,anchor,block,label):
    if t.count(anchor)!=1: raise RuntimeError(f'{label}: anchor count {t.count(anchor)} for {anchor}')
    return t.replace(anchor,block+'\n'+anchor,1)
def replace_once(t,a,b,label):
    if t.count(a)!=1: raise RuntimeError(f'{label}: replace count {t.count(a)} for {a[:100]}')
    return t.replace(a,b,1)
def guards(t,label):
    if t.count(r'\author{Anonymous}')!=1: raise RuntimeError(f'{label}: anonymity')
    for p in (r'first-ever',r'for the first time',r'fundamental new mechanism',r'universal false diffusion',r'first demonstration'):
        if re.search(p,t,re.I): raise RuntimeError(f'{label}: forbidden priority {p}')

UNCERTAINTY=r'''
\section{Measurement covariance and optical-model uncertainty}
\label{sec:modeluncertainty}

The central counterexample deliberately supplies the same theoretical kernels to the forward average and inverse so that deterministic velocity heterogeneity can be isolated. Here we relax the measurement metric and optical-model assumptions separately. The projection identities below are standard generalized-least-squares and nuisance-parameter geometry and are used as attribution tools rather than claimed as new mathematics. Spectral photodiode inverses are already known to depend sensitively on optical-model inputs: Ashry and Fares extracted diffusion length from wavelength-dependent photodiode response and reported strong sensitivity to absorption-coefficient errors \cite{ashry2003diffusion}. The narrower issue here is whether an optical-model error can align with the same-frequency transport-root tangent of a Shockley--Ramo RF inverse.

For a real-stacked data vector with small deterministic discrepancy $\bm e$, fitted-model Jacobian $G$, and precision $W=\Sigma^{-1}$, the local generalized-least-squares displacement is
\begin{equation}
\boxed{\delta\bm\theta=(G^T W G)^{-1}G^T W\bm e},
\label{eq:generalbias}
\end{equation}
with weighted tangent projector $P_W=G(G^T W G)^{-1}G^T W$ and post-fit discrepancy $(I-P_W)\bm e$. Thus covariance changes both the parameter-bias direction and the normal distance used for rejection. Under model misspecification the pseudo-true parameter $\bm\theta_*(W)=\arg\min_{\bm\theta}\|\bm y-\bm f(\bm\theta)\|_W^2$ can itself depend on the metric.

We re-fit the exact-known-kernel heterogeneous response under twelve normalized covariance shapes: IID; channel equicorrelation and AR(1) through $\rho=0.8$; low-rank common, spectral-slope, and spectral-curvature directions; and real--imaginary quadrature correlation. The frequency-dependent ordering is unchanged throughout this tested family. At $100\,\mathrm{MHz}$ one-mode rejection precedes positive-$D$ detection in all 12 cases, whereas at $500\,\mathrm{MHz}$ and $1\,\mathrm{GHz}$ positive $D$ is detectable first in all 12. The required positive-$D$ versus rejection SNR spans are $104.9$--$121.8$ versus $95.3$--$102.3\,\mathrm{dB}$ at 100 MHz, $63.1$--$79.7$ versus $81.2$--$88.2\,\mathrm{dB}$ at 500 MHz, and $45.4$--$61.1$ versus $74.8$--$82.3\,\mathrm{dB}$ at 1 GHz. The fitted $D_{\rm eff}$ at 100 MHz spans $1.66\times10^{-3}$--$2.61\times10^{-3}\,\mathrm{m^2/s}$ across the same weighting metrics. A separate cross-frequency stress changes the 3-GHz rejection requirement by at most about $1.1\,\mathrm{dB}$ over the tested correlation family; the bandwidth advantage therefore survives these particular correlations.

Fixed optical-kernel error is a distinct nuisance. If the nominal kernels depend on optical coordinates $\bm\alpha$, then a small fixed error gives $\delta\bm J=B\delta\bm\alpha$, with
\begin{equation}
B_{mj}=\int_0^L\frac{\partial g_m(z;\bm\alpha)}{\partial\alpha_j}H(z)\,dz.
\end{equation}
Equation~\eqref{eq:generalbias} then separates its tangent bias from its normal rejection signal. A zero-mean random kernel uncertainty may contribute $BC_\alpha B^T$ to an effective covariance at linear order, but a fixed or biased calibration error retains its deterministic tangent component.

An exact affine-depth control distinguishes a benign coordinate rescaling from non-affine kernel error. In the uniform deterministic $D_{\rm micro}=0$ problem, $z_{\rm true}=a+bz$ gives $\gamma_{\rm eff}=b\gamma$, $D_{\rm eff}=D/b^2$, and $w_{\rm eff}=w/b$. An exact continuum calculation with a 1\% depth-scale compression moves kernel means by as much as $18\,\mathrm{nm}$ yet leaves $|D_{\rm eff}|<4.7\times10^{-14}\,\mathrm{m^2/s}$ through 1 GHz.

Non-affine channel-dependent kernel error can behave differently. As a controlled sensitivity coordinate, take $\delta\lambda_m=A(-1,-0.6,-0.2,0.2,0.6,1)_m$. In the exact uniform-velocity $D_{\rm micro}=0$ null, while the inverse still uses the nominal kernels, $A=0.02997\,\mathrm{nm}$ produces $D_{\rm eff}(100\,\mathrm{MHz})=2.6182\times10^{-3}\,\mathrm{m^2/s}$, matching the central heterogeneous exact-continuum value. The maximum kernel-mean shift is $0.206\,\mathrm{nm}$, the one-mode relative residual is $3.1\times10^{-8}$, and positive $D$ reaches the stated detection power at $115.2\,\mathrm{dB}$ while same-frequency rejection requires $156.8\,\mathrm{dB}$. A signed curvature-shaped nuisance reproduces the same target at $A=-0.00294\,\mathrm{nm}$ with a maximum mean-depth shift of $0.020\,\mathrm{nm}$ and thresholds $115.2$ and $138.1\,\mathrm{dB}$.

These sub-nanometer amplitudes are not instrument calibration specifications or empirical error bars. They are coordinates in particular theoretical perturbations of the wavelength-to-generation-kernel map and expose conditioning and tangent alignment. The exact-known-kernel assumption is therefore load-bearing for interpreting the numerical magnitude of $D_{\rm eff}$ as a material parameter, although the deterministic velocity-heterogeneity counterexample remains independently established under that assumption.
'''

SUPPUNC=r'''
\section{Covariance and optical-kernel uncertainty stresses}

The central velocity-heterogeneity result uses the theoretical kernels exactly in forward and inverse calculations. The stresses here relax either measurement covariance or the optical-kernel model, but not both simultaneously; their amplitudes are theoretical nuisance coordinates rather than experimental calibration tolerances.

For the covariance test, each six-complex-channel one-mode model is re-fit by generalized least squares under twelve normalized covariance shapes. At 100 MHz the positive-$D$ threshold spans 104.9--121.8 dB while one-mode rejection spans 95.3--102.3 dB, with rejection first in all cases. At 500 MHz the corresponding spans are 63.1--79.7 and 81.2--88.2 dB, and at 1 GHz 45.4--61.1 and 74.8--82.3 dB, with positive $D$ first in all cases. The 100-MHz pseudo-true $D_{\rm eff}$ spans $1.660\times10^{-3}$--$2.610\times10^{-3}\,\mathrm{m^2/s}$, demonstrating metric dependence of the effective coefficient under misspecification.

For the affine-depth control, the nominal kernel coordinate $u$ is retained and the analytic uniform-drift response is evaluated at $z_{\rm true}=z_c+b(u-z_c)$. For $b=0.990$, 0.995, and 1.000 at 100 MHz, 500 MHz, and 1 GHz, the maximum absolute inferred diffusion is $4.67\times10^{-14}\,\mathrm{m^2/s}$, maximum relative drift error is $1.49\times10^{-14}$, and maximum one-mode relative residual is $7.73\times10^{-16}$. The $b=0.990$ case moves kernel means by as much as 18 nm without creating diffusion.

For signed non-affine perturbations, the exact uniform deterministic null is regenerated with perturbed true kernels while the inverse remains nominal. The channel-linear mode $\delta\lambda_m=A(-1,-0.6,-0.2,0.2,0.6,1)_m$ has local $dD_{\rm eff}/dA=8.513\times10^{-2}\,\mathrm{m^2/(s\,nm)}$ at 100 MHz and an asymptotic rejection-SNR to positive-$D$-SNR ratio of 72.7. It matches the exact heterogeneous target $D_{\rm eff}=2.618164535\times10^{-3}\,\mathrm{m^2/s}$ at $A=+0.0299713\,\mathrm{nm}$, where the maximum kernel-mean shift is $0.205754\,\mathrm{nm}$, the one-mode residual is $3.09\times10^{-8}$, and the thresholds are 115.22 and 156.81 dB. A curvature-shaped signed nuisance reaches the same target at $A=-0.00294205\,\mathrm{nm}$, maximum mean shift $0.020041\,\mathrm{nm}$, and thresholds 115.23 and 138.14 dB.

The amplitudes above are not wavelength-meter specifications, measured calibration errors, or error bars for a real detector. They expose conditioning of the theoretical wavelength-to-kernel map. The local signed tangent calculation, exact affine null, and finite nonlinear inversions are independently executable.

The checked workflows are: covariance run 31953328287; kernel-misspecification run 31953612225; exact-affine run 31953979410; frequency-aware local nuisance projection run 31954048251; and signed-mode threshold run 31954087223. The frequency-aware ``v2'' nuisance projection supersedes only the higher-frequency diffusion-derivative fields of its first version, which had inherited a 100-MHz-fixed angular frequency from a validation helper; the first version's 100-MHz row and channel-space tangent/normal projection were unaffected.
'''

def main_build():
    t=frozen(MS,MSHA)
    # Short, stable insertions only.
    abst='\\end{abstract}'
    sentence=('The exact-kernel counterexample is supplemented by covariance and optical-model uncertainty stresses: the tested frequency ordering survives broad covariance changes, whereas fixed non-affine kernel misspecification can itself generate positive apparent diffusion in a uniform zero-diffusion null; an exact affine depth-scale error does not. Consequently, the numerical effective coefficient is conditional on the optical model and weighting metric.\n')
    t=insert_before(t,abst,sentence,'main abstract')
    intro_anchor='\\section{Measurement model and attribution problem}'
    intro=('Spectral-response transport extraction is itself established prior art, and optical-model error can bias such inferred diffusion quantities. In particular, Ashry and Fares reported strong sensitivity of photodiode diffusion-length extraction to absorption-coefficient errors \\cite{ashry2003diffusion}. We therefore do not claim that optical-model sensitivity, generalized least squares, nuisance projection, or Schur-complement information is new. The detector-specific question developed below is the joint Shockley--Ramo spectral-depth attribution geometry under an explicit zero-microscopic-diffusion control.\n\n')
    t=insert_before(t,intro_anchor,intro,'main intro')
    t=insert_before(t,'\\section{HgCdTe scale example and implications}',UNCERTAINTY,'main uncertainty')
    # Supersede the stale limitations paragraph using uniquely bounded markers.
    a='The framework has several limitations.'
    b='These limitations suggest direct extensions.'
    ia=t.find(a); ib=t.find(b)
    if ia<0 or ib<0 or ib<=ia: raise RuntimeError('main limitations bounds not found')
    newlim=("The framework has several limitations. The main counterexample deliberately omits microscopic diffusion so its deterministic source is unambiguous, while the optical-model extension tests controlled nuisance directions rather than a validated experimental error distribution. Its sub-nanometer wavelength amplitudes therefore quantify conditioning of this surrogate and must not be read as instrument specifications. A real detector can contain true diffusion, deterministic heterogeneity, optical-model error, parasitics, and correlated calibration errors simultaneously. The local projection formulas assume a regular identified one-mode solution, and the covariance study spans broad structured families rather than arbitrary covariance. Full electrostatic-model uncertainty and optimized measurement-time allocation remain outside the present scope.\n\n")
    t=t[:ia]+newlim+t[ib:]
    concl_anchor='Additional RF frequencies provide a falsification route, but structural overdetermination is not equivalent to statistical power.'
    add=("The optical-model stress adds a stricter attribution condition. A fitted diffusion magnitude can be interpreted as material-like only to the extent that kernel-nuisance directions overlapping the transport-root tangent are independently constrained. This does not replace the deterministic velocity-gradient counterexample; it bounds what its fitted effective coefficient can mean when the optical model is uncertain.\n\n")
    t=insert_before(t,concl_anchor,add,'main conclusion')
    t=replace_once(t,'\\bibliography{PAPER02_REFERENCES_REV4}','\\bibliography{PAPER02_REFERENCES_REV7}','main bibliography')
    for s in (r'\section{Measurement covariance and optical-model uncertainty}',r'\cite{ashry2003diffusion}',r'A=0.02997\,\mathrm{nm}',r'A=-0.00294\,\mathrm{nm}','not instrument calibration specifications or empirical error bars','PAPER02_REFERENCES_REV7'):
        if s not in t: raise RuntimeError('main required missing '+s)
    if 'does not yet propagate uncertainty in the supplied optical kernels' in t: raise RuntimeError('stale limitation retained')
    guards(t,'main'); MD.write_text(t)

    s=frozen(SS,SSHA)
    scope_anchor='\\section{Conditional HgCdTe optical-kernel construction}'
    scope=("The exact-kernel condition above isolates the central velocity-heterogeneity mechanism. A separately labeled uncertainty stress later in this supplement perturbs the true kernels while keeping the inverse kernels nominal; those results test how load-bearing the exact-kernel assumption is and do not constitute experimental calibration.\n\n")
    s=insert_before(s,scope_anchor,scope,'supp scope')
    s=insert_before(s,'\\section{Reproduction record}',SUPPUNC,'supp uncertainty')
    s=replace_once(s,'\\bibliography{PAPER02_REFERENCES_REV4}','\\bibliography{PAPER02_REFERENCES_REV7}','supp bibliography')
    for q in (r'\section{Covariance and optical-kernel uncertainty stresses}',r'A=+0.0299713\,\mathrm{nm}',r'A=-0.00294205\,\mathrm{nm}','not wavelength-meter specifications','frequency-aware ``v2','PAPER02_REFERENCES_REV7'):
        if q not in s: raise RuntimeError('supp required missing '+q)
    guards(s,'supp'); SD.write_text(s)
    print('wrote',MD.name); print('wrote',SD.name)

if __name__=='__main__': main_build()
