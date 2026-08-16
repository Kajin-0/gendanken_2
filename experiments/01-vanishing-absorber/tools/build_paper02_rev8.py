"""Build Paper 02 Rev. 8 deterministically from frozen Rev. 7.

Rev. 8 responds to the later adversarial review without editing Rev. 7:
- scope the theorem/counterexample to a single-mobile-carrier/unipolar observable;
- add the exact upstream affine-plus-exponential bridge;
- narrow 'remote' language to finite-support/mean-upstream coupling;
- make the exact planar continuum the primary full-contact result;
- distinguish root-space from full-channel multi-frequency rejection;
- add the checked two-carrier scope audit;
- remove internal review/run-history language from submission-facing text;
- state the amplitude-SNR dB convention explicitly.
"""
from pathlib import Path
import hashlib,re

ROOT=Path(__file__).resolve().parents[1]
MS=ROOT/'PAPER02_MANUSCRIPT_REV7_ANON_2026-08-16.tex'
SS=ROOT/'PAPER02_SUPPLEMENT_REV7_ANON_2026-08-16.tex'
MD=ROOT/'PAPER02_MANUSCRIPT_REV8_ANON_2026-08-16.tex'
SD=ROOT/'PAPER02_SUPPLEMENT_REV8_ANON_2026-08-16.tex'
MSHA='85e56d36d320e0012b28a6742f2b48d8c268af91'
SSHA='947641ca95bcda1319b6b5ef322404ee14fba027'

def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def frozen(p,s):
    b=p.read_bytes(); g=blob(b)
    if g!=s: raise RuntimeError(f'frozen blob changed: {p.name} {g} != {s}')
    return b.decode()
def once(t,a,b,label):
    if t.count(a)!=1: raise RuntimeError(f'{label}: count={t.count(a)}')
    return t.replace(a,b,1)
def replace_between(t,a,b,new,label):
    if t.count(a)!=1 or t.count(b)!=1: raise RuntimeError(f'{label}: bad boundaries')
    ia=t.index(a)+len(a); ib=t.index(b,ia)
    return t[:ia]+'\n'+new+'\n'+t[ib:]

def build_main():
    t=frozen(MS,MSHA)
    t=once(t,r'\title{Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors}',r'\title{Apparent diffusion from deterministic velocity gradients in wavelength-resolved unipolar photodetector transport}','title')
    abstract=r'''Wavelength-dependent photogeneration can encode internal transport in a detector response, but extracting a microscopic diffusion coefficient requires separating material transport from device-level heterogeneity sampled by finite generation profiles. We study this attribution problem for a single-mobile-carrier, or unipolar, planar Shockley--Ramo observable with zero microscopic diffusion and zero recombination. Finite generation-depth kernels that overlap a spatially nonuniform deterministic velocity region can yield a positive effective diffusion coefficient when the resulting terminal-current response is fit with a homogeneous drift--diffusion model. An exact full-contact planar continuum calculation gives $D_{\rm eff}=2.6182\times10^{-3}$, $2.5508\times10^{-3}$, and $2.3506\times10^{-3}\,\mathrm{m^2/s}$ at 100 MHz, 500 MHz, and 1 GHz, while upstream point-source controls remain at numerical-zero diffusion. Removing kernel support in the heterogeneous region collapses the effect even when every channel mean depth is restored. We derive the local low-frequency equivalence, an exact finite-support leakage relation, the upstream affine-plus-exponential bridge, and a profiled parameter-bias law separating tangent bias from normal model rejection. Independent velocity profiles give positive apparent diffusion for downstream acceleration, zero for uniform velocity, and negative values for deceleration. Root-space and direct full-channel multi-frequency tests quantify complementary falsification information: through 1 GHz the reference full-channel test lowers the required rejection SNR from 90.37 to 81.51 dB, whereas by 3 GHz the two protocols are comparable. Structured covariance and optical-kernel uncertainty stresses show that the numerical effective coefficient is conditional on the inverse metric and optical model. A separate pair-aware scope audit shows that the fitted single-carrier coefficient is not invariant when a second carrier contribution is admitted, so no generic two-carrier photodiode claim is made. The HgCdTe construction is retained only as a conditional optical/field/timing scale example, not as a self-consistent device simulation.'''
    t=replace_between(t,r'\begin{abstract}',r'\end{abstract}',abstract,'abstract')
    old='The forward systems used for the central counterexamples have'
    new='The central construction is explicitly a single-mobile-carrier, or unipolar, terminal-current contribution; it is not a complete electron--hole-pair model of a generic photodiode transient. The forward systems used for the central counterexamples have'
    t=once(t,old,new,'intro unipolar')
    t=t.replace('fitting the resulting terminal-current response with a homogeneous drift--diffusion model returns','fitting the resulting unipolar terminal-current response with a homogeneous drift--diffusion model returns',1)
    t=t.replace('Second, the coupling can be spatially remote: all nominal mean generation depths may lie outside the nonuniform region while finite kernel support inside that region drives the bias.','Second, mean generation depth is not a sufficient optical coordinate: all nominal means may lie upstream of the nonuniform region while finite kernel support inside that region drives the bias.',1)
    point='For deterministic downstream velocity $v(z)>0$, zero microscopic diffusion, zero recombination, and the planar weighting potential $\\phi_w=z/L$, the Shockley--Ramo path integral'
    scoped='The observable $H$ below is one mobile-carrier contribution. In an ordinary electron--hole pair both carrier trajectories can contribute to terminal current; that more general decomposition is not assumed here. The present equations apply directly to a unipolar observable and to regimes in which the complementary carrier contribution is independently isolated or negligible.\n\nFor deterministic downstream velocity $v(z)>0$, zero microscopic diffusion, zero recombination, and the planar weighting potential $\\phi_w=z/L$, the Shockley--Ramo path integral'
    t=once(t,point,scoped,'point scope')
    c='For constant velocity, the source-coordinate difference response is one exact spatial exponential. A velocity gradient changes the source-coordinate law even though every trajectory remains deterministic.'
    bridge=r'''For constant velocity, the source-coordinate difference response is one exact spatial exponential. More strongly, suppose the source lies in a uniform upstream interval $z<z_d$ with velocity $v_0$, while arbitrary deterministic heterogeneity is allowed downstream of $z_d$. Equation~\eqref{eq:ramoode} then gives
\begin{equation}
\boxed{H(z,\omega)=\frac{v_0}{i\omega L}+C(\omega)e^{i\omega z/v_0},\qquad z<z_d.}
\label{eq:upstreambridge}
\end{equation}
All downstream heterogeneity enters only through the matching constant $C(\omega)$. Thus point sources confined to the uniform upstream interval remain exactly affine plus one source-coordinate exponential even though those carriers later traverse the heterogeneous region. A velocity gradient changes the source-coordinate law only when the source samples the nonuniform interval or a finite generation kernel has support there.'''
    t=once(t,c,bridge,'upstream bridge')
    t=t.replace('Consequently, any recovered response with $a_1>0$ and $a_2>0$ admits','Consequently, for a locally physically admissible parameterization, a recovered response with $a_1>0$ and $a_2>0$ admits',1)
    t=t.replace(r'\section{Finite kernels couple remote device regions into the inverse}',r'\section{Finite kernels couple mean-upstream generation to device heterogeneity}')
    t=t.replace(r'\subsection{Exact remote-region leakage}',r'\subsection{Exact finite-support leakage}')
    t=t.replace('inside the remote nonuniform region','inside the nonuniform region').replace('all remote support','all support in the nonuniform region')
    t=t.replace('Remote generation support is the causal optical variable.','Generation support inside the nonuniform region is the causal optical variable.')
    t=t.replace('remote-support bound','finite-support bound')
    old=r'''The physical finite kernels centered at the original upstream means give
\begin{equation}
\Deff=2.6098\times10^{-3}\,\mathrm{m^2/s}.
\label{eq:hgcdteD}
\end{equation}
This is the value at the canonical manuscript baseline discretization.  Refining only the two-dimensional field mesh changes the $100\,\mathrm{MHz}$ result to $2.6535\times10^{-3}\,\mathrm{m^2/s}$, a $1.648\%$ shift, while preserving its positive sign and the causal controls.'''
    new=r'''The exact full-contact planar continuum calculation with the physical finite kernels gives at $100\,\mathrm{MHz}$
\begin{equation}
\Deff=2.6182\times10^{-3}\,\mathrm{m^2/s},
\label{eq:hgcdteD}
\end{equation}
and gives $2.5508\times10^{-3}$ and $2.3506\times10^{-3}\,\mathrm{m^2/s}$ at $500\,\mathrm{MHz}$ and $1\,\mathrm{GHz}$. These mesh-free values are the primary numerical results for the full-contact planar stress. The separate two-dimensional field/trajectory solver reproduces them within $0.320\%$, $0.087\%$, and $0.071\%$, respectively, and is retained as an independent numerical reproduction and extension path for nonplanar geometries.'''
    t=once(t,old,new,'exact primary')
    t=t.replace(r'\subsection{Covariance-aware multi-frequency rejection}',r'\subsection{Root-space and full-channel multi-frequency rejection}')
    old='To illustrate the scale, we adopt an explicit theoretical noise model: six complex channels per RF frequency, independent equal Gaussian real and imaginary quadrature noise, equal RMS-channel SNR at each included RF, and no cross-frequency correlation. The channel covariance is propagated through the kernel-aware one-mode root fit.'
    new='To illustrate the scale, we adopt an explicit theoretical noise model: six complex channels per RF frequency, independent equal Gaussian real and imaginary quadrature noise, equal RMS-channel SNR at each included RF, and no cross-frequency correlation. We define $S=\\sqrt{\\langle|J_m|^2\\rangle}/\\sigma_q$ and quote $S_{\\rm dB}=20\\log_{10}S$. In the root-space protocol the channel covariance is propagated through the kernel-aware one-mode root fit.'
    t=once(t,old,new,'snr convention')
    old='For false-rejection probability $\\alpha=0.0027$ and $90\\%$ power, the conditional planar-depletion nuisance requires approximately $90.4\\,\\mathrm{dB}$ RMS-channel SNR through $1\\,\\mathrm{GHz}$, $79.9\\,\\mathrm{dB}$ through $1.5\\,\\mathrm{GHz}$, $73.2\\,\\mathrm{dB}$ through $2\\,\\mathrm{GHz}$, and $64.2\\,\\mathrm{dB}$ through $3\\,\\mathrm{GHz}$. These are values under the stated theoretical covariance model, not universal instrument requirements.'
    new='For false-rejection probability $\\alpha=0.0027$ and $90\\%$ power, the exact-continuum root-space test requires $90.37\\,\\mathrm{dB}$ through $1\\,\\mathrm{GHz}$, $79.90\\,\\mathrm{dB}$ through $1.5\\,\\mathrm{GHz}$, $73.20\\,\\mathrm{dB}$ through $2\\,\\mathrm{GHz}$, and $64.21\\,\\mathrm{dB}$ through $3\\,\\mathrm{GHz}$. A direct full-channel test, which retains same-frequency normal residuals while profiling complex $C_f,K_f$ at each frequency, requires $81.51\\,\\mathrm{dB}$ through $1\\,\\mathrm{GHz}$, $72.28\\,\\mathrm{dB}$ through $2\\,\\mathrm{GHz}$, and $65.00\\,\\mathrm{dB}$ through $3\\,\\mathrm{GHz}$. Thus full channel is substantially stronger at intermediate bandwidth, whereas by 3 GHz the lower-dimensional root-space statistic is slightly stronger after its smaller residual degrees-of-freedom penalty. Neither test is claimed globally optimal outside the declared model and covariance.'
    t=once(t,old,new,'full channel')
    t=t.replace('Practical discrimination of the deterministic nuisance from homogeneous diffusion.','Root-space discrimination of the deterministic nuisance from homogeneous diffusion.',1)
    # Replace internal-history block in Discussion with submission-facing exact-primary + pair audit.
    a='The Supplemental Material accompanying this revision specifies'
    b='The framework has several limitations.'
    ia=t.index(a); ib=t.index(b,ia)
    clean=r'''The Supplemental Material specifies the theoretical optical-kernel construction, exact planar deterministic transport stress, independent two-dimensional numerical reproduction, pair-aware scope audit, and executable reproduction files.

For the full-width contact, the central calculation is evaluated directly in the exact planar continuum. It gives $D_{\rm eff}=2.6182\times10^{-3}$, $2.5508\times10^{-3}$, and $2.3506\times10^{-3}\,\mathrm{m^2/s}$ at $100\,\mathrm{MHz}$, $500\,\mathrm{MHz}$, and $1\,\mathrm{GHz}$. The upstream point-source sequence remains at numerical-zero scale, while the inside-region control remains positive. A separate two-dimensional field/trajectory calculation reproduces these values within $0.320\%$, $0.087\%$, and $0.071\%$ and is retained as an independent solver check rather than the definition of the planar result.

A pair-aware scope audit confirms why the unipolar restriction is necessary. The exact pair model satisfies $H_{\rm down}(z,0)+H_{\rm up}(z,0)=1$ to $1.1\times10^{-16}$ and its uniform two-mode null gives zero downstream diffusion to numerical precision. With a heterogeneous downstream carrier, however, a free two-root decomposition becomes underconstrained; even when the simple countercarrier propagation root is fixed to its known value, only one of 21 core speed/frequency cases retains positive downstream $D$. The fitted single-carrier coefficient is therefore not invariant under a generic two-carrier decomposition, and no such generalization is claimed.

'''
    t=t[:ia]+clean+t[ib:]
    t=t.replace('The framework has several limitations. The main counterexample','The framework has several limitations. Most importantly, the theorem concerns a single-mobile-carrier/unipolar terminal-current contribution; a generic two-carrier transient introduces a separate decomposition problem. The main counterexample',1)
    t=t.replace(r'\section{Discussion}',r'\section{Discussion}\label{sec:discussion}')
    t=t.replace('A positive diffusion coefficient obtained from wavelength-resolved photodetector transport data need not be a unique signature of microscopic diffusion.','For a single-mobile-carrier or unipolar wavelength-resolved terminal-current observable, a positive fitted diffusion coefficient need not be a unique signature of microscopic diffusion.',1)
    t=t.replace('A covariance-weighted manifold test shows that bandwidth can provide substantially more nuisance discrimination than extreme precision confined to the low-frequency tangent regime.','Root-space and full-channel tests show that bandwidth and retained channel-space residual directions provide complementary nuisance discrimination; neither compression is uniformly superior over the entire tested bandwidth.',1)
    return t

def build_supp():
    t=frozen(SS,SSHA)
    t=once(t,'The manuscript uses two distinct numerical constructions that must not be conflated.','The central transport observable is explicitly one mobile-carrier/unipolar Shockley--Ramo contribution, not the complete electron--hole transient of a generic photodiode. A pair-aware scope audit below motivates this restriction.\n\nThe manuscript uses two distinct numerical constructions that must not be conflated.','supp scope')
    t=t.replace(r'\section{Post-hoc exact planar continuum cross-check}',r'\section{Exact planar continuum primary calculation}')
    t=t.replace('The full-contact central case admits an additional check that eliminates the two-dimensional electrostatic mesh.  This check was designed \\emph{after} the mesh-refinement result was known and is therefore explicitly post-hoc rather than a predeclared convergence gate.','The full-contact central case admits an exact calculation that eliminates the two-dimensional electrostatic mesh. Historically it was introduced after the original mesh-refinement study; in this revision it is the primary full-contact planar result because it removes discretization of electrostatics and trajectories.')
    t=t.replace('Fresh numerical baseline compared with the post-hoc exact-planar continuum calculation.','Independent two-dimensional numerical reproduction compared with the exact-planar continuum primary calculation.')
    t=t.replace('The continuum comparison satisfies every previously declared numerical-convergence tolerance scale, but the agreement remains explicitly post-hoc because this check was designed after inspection of the mesh-refinement result.','The independent numerical calculation agrees with the exact continuum on the previously declared tolerance scale. Its convergence history remains useful as a solver validation, but the exact continuum values define the central planar result.')
    pair=r'''\section{Two-carrier scope audit}

With planar weighting potential $\phi_w=z/L$, the complementary carrier was added with output polarity for which both induced-current contributions add. The exact dc identity is
\begin{equation}
H_{\rm pair}(z,0)=\frac{L-z}{L}+\frac{z}{L}=1,
\end{equation}
and the sampled implementation error is $1.11\times10^{-16}$.

A uniform pair contains two source-coordinate exponentials, so the first audit used a two-mode finite-kernel inverse. Over the core countercarrier-speed sweep its uniform null returns maximum $|D_{\rm down}|=6.58\times10^{-9}\,\mathrm{m^2/s}$ and maximum centered residual $1.74\times10^{-13}$. With a heterogeneous downstream response, however, the two freely fitted roots are not stably decomposed. A stricter follow-up fixed the simple countercarrier propagation root to its known uniform-velocity value while profiling its complex amplitude and fitting only the downstream root. Of 21 core cases spanning $v_{\rm up}/v_{\rm down}=0.1$--$10$ at 100 MHz, 500 MHz, and 1 GHz, only one retained positive downstream $D$. We therefore restrict the main result to the unipolar observable rather than tuning a two-carrier model to preserve the sign.'''
    t=t.replace(r'\section{Covariance and optical-kernel uncertainty stresses}',pair+'\n\n'+r'\section{Covariance and optical-kernel uncertainty stresses}',1)
    full=r'''\section{Full-channel multi-frequency rejection comparison}

The root-space statistic compresses each six-complex-channel measurement to one fitted complex root. A direct full-channel check instead fits common homogeneous $D,w$ while profiling complex $C_f,K_f$ at every frequency. Under the same equal-quadrature convention, $S=\sqrt{\langle|J_m|^2\rangle}/\sigma_q$ and $S_{\rm dB}=20\log_{10}S$, with $\alpha=0.0027$ and 90\% power. Through 1 GHz the exact-continuum thresholds are 90.37 dB root-space and 81.51 dB full-channel; through 2 GHz they are 73.20 and 72.28 dB; through 3 GHz they are 64.21 and 65.00 dB. Same-frequency normal residuals therefore help substantially before the root-dispersion mismatch is large, while the full-channel statistic also pays a larger residual degrees-of-freedom penalty.'''
    a=r'\section{Reproduction record}'; ia=t.index(a); ib=t.index(r'\bibliographystyle',ia)
    repro=r'''\section{Reproduction record}

The anonymous source package accompanying this revision includes executable scripts and machine-readable outputs for the exact planar continuum, independent two-dimensional reproduction, kernel-aware inverse, two-carrier scope audit, covariance/kernel-uncertainty stresses, and root-space/full-channel rejection comparison. Internal workflow identifiers and failed-development history are retained in the research repository rather than the submission-facing supplement. A persistent public archival identifier should be added to the final publication record when available.

'''
    t=t[:ia]+full+'\n\n'+repro+t[ib:]
    return t

def guards(t,label):
    if t.count(r'\author{Anonymous}')!=1: raise RuntimeError(label+' anonymity')
    bad=('hostile review','failed in the reporting layer','first-ever','for the first time','universal false diffusion','fundamental new mechanism')
    for q in bad:
        if q.lower() in t.lower(): raise RuntimeError(label+' forbidden '+q)

m=build_main(); s=build_supp(); guards(m,'main'); guards(s,'supp')
for q in ('single-mobile-carrier','eq:upstreambridge','81.51','90.37','2.6182'):
    if q not in m: raise RuntimeError('main missing '+q)
for q in ('Two-carrier scope audit','81.51','Internal workflow identifiers'):
    if q not in s: raise RuntimeError('supp missing '+q)
MD.write_text(m); SD.write_text(s)
print('wrote',MD.name,SD.name)
