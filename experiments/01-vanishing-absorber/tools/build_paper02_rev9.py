from pathlib import Path
import hashlib

ROOT=Path('.')
MS=ROOT/'PAPER02_MANUSCRIPT_REV8_ANON_2026-08-16.tex'
SS=ROOT/'PAPER02_SUPPLEMENT_REV8_ANON_2026-08-16.tex'
BS=ROOT/'PAPER02_REFERENCES_REV7.bib'
MD=ROOT/'PAPER02_MANUSCRIPT_REV9_ANON_2026-08-16.tex'
SD=ROOT/'PAPER02_SUPPLEMENT_REV9_ANON_2026-08-16.tex'
BD=ROOT/'PAPER02_REFERENCES_REV9.bib'
MSHA='dc8c1df593379a898fa36280350d4462576a9041'
SSHA='6d7098f4c7eb37fb3d3c63ccdf6670047ebfc074'
BSHA='3aef882d23cf81973b4091b7d5964d90ec4e53e2'

def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def frozen(p,s):
    b=p.read_bytes(); g=blob(b)
    if g!=s: raise RuntimeError(f'frozen blob changed: {p.name} {g} != {s}')
    return b.decode()
def once(t,a,b,label):
    n=t.count(a)
    if n!=1: raise RuntimeError(f'{label}: count={n}')
    return t.replace(a,b,1)

m=frozen(MS,MSHA)
s=frozen(SS,SSHA)
bib=frozen(BS,BSHA)

# 1) Make the physical meaning of the unipolar restriction concrete without
# claiming that the planar surrogate is a UTC-PD device model.
old='The observable $H$ below is one mobile-carrier contribution. In an ordinary electron--hole pair both carrier trajectories can contribute to terminal current; that more general decomposition is not assumed here. The present equations apply directly to a unipolar observable and to regimes in which the complementary carrier contribution is independently isolated or negligible.'
new=old+r''' A concrete photodetector class in which strongly carrier-asymmetric transport is deliberately engineered is the uni-traveling-carrier photodiode (UTC-PD), introduced to exploit electron transport in the collection region \cite{ishibashi1997utc}. We cite UTC-PDs only as an existence example for a physically meaningful effectively one-traveling-carrier regime; the planar surrogate below is not a UTC-PD device model.'''
m=once(m,old,new,'unipolar physical context')

# 2) Explicitly link Eq. (10) to the H0 used in the finite-support theorem.
m=once(m,r'\section{Deterministic heterogeneity can appear diffusive}',r'\section{Deterministic heterogeneity can appear diffusive}\label{sec:heterogeneity}','heterogeneity label')
old=r'''Let a reference point-source response be
\begin{equation}
H_0(z)=A+B e^{rz},
\end{equation}
and suppose the true response differs only in a nuisance region $\Rregion$,'''
new=r'''Let a reference point-source response be
\begin{equation}
H_0(z)=A+B e^{rz}.
\end{equation}
For the downstream-heterogeneity construction of Sec.~\ref{sec:heterogeneity}, $H_0$ need not be the response of a globally uniform comparison device. At each frequency we may choose it as the analytic continuation of the \emph{actual} upstream solution in Eq.~\eqref{eq:upstreambridge}, namely $A=v_0/(i\omega L)$, $B=C(\omega)$, and $r=i\omega/v_0$. Then $H(z)=H_0(z)$ identically throughout the uniform upstream interval, and the discrepancy is supported only where the actual response departs from that continuation. With this choice, suppose the true response differs only in a nuisance region $\Rregion$,'''
m=once(m,old,new,'H0 linkage')

# 3) State the exact residual degrees-of-freedom convention and make the power
# comparison explicitly test-specific.
old='To illustrate the scale, we adopt an explicit theoretical noise model: six complex channels per RF frequency, independent equal Gaussian real and imaginary quadrature noise, equal RMS-channel SNR at each included RF, and no cross-frequency correlation. We define $S=\\sqrt{\\langle|J_m|^2\\rangle}/\\sigma_q$ and quote $S_{\\rm dB}=20\\log_{10}S$. In the root-space protocol the channel covariance is propagated through the kernel-aware one-mode root fit. At every cumulative RF bandwidth, the wrong homogeneous $D,w$ model is then re-fit jointly before its noncentral distance is evaluated.'
new=old+r''' For $n$ frequencies, root space contains $2n$ real root coordinates and fits two real global parameters $(D,w)$, so its residual degrees of freedom are $\nu_{\rm root}=2n-2$. The full-channel statistic contains $12n$ real quadratures and profiles two complex nuisance coefficients $(C_f,K_f)$ at each frequency in addition to the same two real global parameters, giving $\nu_{\rm full}=12n-(4n+2)=8n-2$. Under the deterministic alternative the corresponding quadratic form is treated as noncentral $\chi^2_{\nu}(\Lambda)$ with the same residual dimension; power is evaluated from $P[\chi^2_{\nu}(\Lambda)>\chi^2_{\nu,1-\alpha}]$.'''
m=once(m,old,new,'df convention')

old='Thus full channel is substantially stronger at intermediate bandwidth, whereas by 3 GHz the lower-dimensional root-space statistic is slightly stronger after its smaller residual degrees-of-freedom penalty. Neither test is claimed globally optimal outside the declared model and covariance.'
new='Thus full channel is substantially stronger at intermediate bandwidth, whereas by 3 GHz the lower-dimensional root-space statistic is slightly stronger for this particular alternative after its smaller residual degrees-of-freedom penalty. This is a test-specific power comparison: the 3-GHz reversal does not imply that root compression retains more raw information. Neither test is claimed globally optimal outside the declared model and covariance.'
m=once(m,old,new,'test-specific power')

# 4) Figure 5: switch the upper panel to a Rev9 plot containing both tests and
# update caption accordingly.
m=once(m,'numerics/paper02_figures/fig5_required_snr_vs_bandwidth.pdf','numerics/paper02_figures/fig5_required_snr_vs_bandwidth_rev9.pdf','fig5 path')
old='\\caption{Root-space discrimination of the deterministic nuisance from homogeneous diffusion. Increasing usable RF bandwidth substantially reduces the channel SNR required for a fixed rejection power because the first unmatched frequency terms grow beyond the low-frequency tangent regime.}'
new=r'''\caption{Multi-frequency discrimination of the deterministic nuisance from homogeneous diffusion. Top: required RMS-channel SNR for the root-space and direct full-channel tests under the stated $\alpha$ and power criterion. Full-channel retention of same-frequency normal residuals is advantageous at intermediate bandwidth; the small reversal at 3 GHz is test-specific and reflects the smaller root-space residual dimension rather than greater raw information after compression. Bottom: the homogeneous $D$ re-fitted in root space decreases as the usable bandwidth grows.}'''
m=once(m,old,new,'fig5 caption')

# Use a new bibliography rather than mutating the frozen Rev7 bibliography.
m=m.replace('\\bibliography{PAPER02_REFERENCES_REV7}','\\bibliography{PAPER02_REFERENCES_REV9}')

# Supplement title should exactly match the main title.
s=once(s,'\\title{Supplemental Material for: Apparent diffusion from deterministic velocity gradients in wavelength-resolved photodetectors}',
       '\\title{Supplemental Material for: Apparent diffusion from deterministic velocity gradients in wavelength-resolved unipolar photodetector transport}',
       'supplement title')

# Replace the terse pair audit with a self-contained model, branch convention,
# quantitative instability statement, and compact 21-case matrix.
start='\\section{Two-carrier scope audit}'
end='\\section{Covariance and optical-kernel uncertainty stresses}'
ia=s.index(start); ib=s.index(end,ia)
pair=r'''\section{Two-carrier scope audit}

With planar weighting potential $\phi_w=z/L$, the complementary carrier was added with output polarity for which both induced-current contributions add. The exact dc identity is
\begin{equation}
H_{\rm pair}(z,0)=\frac{L-z}{L}+\frac{z}{L}=1,
\end{equation}
and the sampled implementation error is $1.11\times10^{-16}$.

A uniform pair contains two source-coordinate exponentials. The finite-kernel inverse used for the pair audit is
\begin{equation}
J_m=C_0+C_d M_m(r_d)+C_u M_m(r_u),
\qquad
M_m(r)=\int_0^L g_m(z)e^{rz}\,dz,
\end{equation}
where the affine coefficient $C_0$ and both modal amplitudes $C_d,C_u$ are unconstrained complex coefficients profiled by linear least squares at each RF frequency. In the free two-root audit, $r_d$ is constrained to $\operatorname{Im}r_d>0$ and $r_u$ to $\operatorname{Im}r_u<0$, with both real parts bounded to $\pm20\,\mu\mathrm{m}^{-1}$ and multistart seeds around the physical pure-drift roots. The uniform null is recovered cleanly: over the 21 core cases the maximum $|D_{\rm down}|$ is $6.58\times10^{-9}\,\mathrm{m^2/s}$ and the maximum centered residual is $1.74\times10^{-13}$. The heterogeneous free-root decomposition is not parameter-stable despite small residuals: its fitted $D_{\rm down}$ spans $-7.68\times10^{7}$ to $+3.36\times10^{-1}\,\mathrm{m^2/s}$ across the same 21 cases while the maximum centered residual remains $1.10\times10^{-4}$. We therefore do not interpret the free two-root coefficients physically.

The stricter scope audit fixes the deliberately simple countercarrier root to its known uniform-velocity value
\begin{equation}
r_u=-i\omega/v_u,
\end{equation}
while still profiling its complex amplitude and fitting only the downstream root. The downstream fit uses $\operatorname{Im}r_d>0$, $\operatorname{Re}r_d\in[-20,20]~\mu\mathrm{m}^{-1}$, five multistart seeds spanning $0.8$--$1.2$ times the single-carrier imaginary-root seed, and selects the least-residual solution before mapping $-r_d$ through the same homogeneous dispersion relation used in the main text. The seven core ratios are $v_{\rm up}/v_{\rm down}=0.1,0.25,0.5,1,2,4,10$, each evaluated at 100 MHz, 500 MHz, and 1 GHz.

\begin{table}[h]
\caption{Known-countercarrier-root scope audit. Entries are fitted downstream $10^3D_{\rm down}$ in $\mathrm{m^2/s}$; the final column is the maximum centered relative residual across the three RF frequencies for that speed ratio. The only positive core case is marked by $^*$.}
\centering
\begin{tabular}{ccccc}
\toprule
$v_{\rm up}/v_{\rm down}$ & 100 MHz & 500 MHz & 1 GHz & $\max\epsilon_c$\\
\midrule
0.10 & -165.481 & -3.438 & $+1.494^*$ & $3.65\times10^{-4}$\\
0.25 & -320.962 & -11.337 & -0.583 & $1.27\times10^{-4}$\\
0.50 & -427.159 & -19.666 & -2.606 & $2.76\times10^{-4}$\\
1.00 & -464.715 & -28.619 & -4.798 & $4.76\times10^{-4}$\\
2.00 & -449.276 & -36.140 & -6.730 & $2.22\times10^{-4}$\\
4.00 & -422.569 & -41.223 & -8.119 & $1.73\times10^{-4}$\\
10.0 & -398.013 & -44.821 & -9.163 & $1.52\times10^{-4}$\\
\bottomrule
\end{tabular}
\end{table}

Thus only one of 21 core cases retains positive downstream $D$, specifically $v_{\rm up}/v_{\rm down}=0.1$ at 1 GHz with $D_{\rm down}=1.4936\times10^{-3}\,\mathrm{m^2/s}$. This negative result is the reason the main theorem is restricted to the unipolar observable rather than extended to a generic two-carrier photodiode transient.

'''
s=s[:ia]+pair+s[ib:]

# Expand the statistical documentation in the Supplement as requested.
old='The root-space statistic compresses each six-complex-channel measurement to one fitted complex root. A direct full-channel check instead fits common homogeneous $D,w$ while profiling complex $C_f,K_f$ at every frequency. Under the same equal-quadrature convention, $S=\\sqrt{\\langle|J_m|^2\\rangle}/\\sigma_q$ and $S_{\\rm dB}=20\\log_{10}S$, with $\\alpha=0.0027$ and 90\\% power. Through 1 GHz the exact-continuum thresholds are 90.37 dB root-space and 81.51 dB full-channel; through 2 GHz they are 73.20 and 72.28 dB; through 3 GHz they are 64.21 and 65.00 dB. Same-frequency normal residuals therefore help substantially before the root-dispersion mismatch is large, while the full-channel statistic also pays a larger residual degrees-of-freedom penalty.'
new=r'''The root-space statistic compresses each six-complex-channel measurement to one fitted complex root. A direct full-channel check instead fits common homogeneous $D,w$ while profiling complex $C_f,K_f$ at every frequency. Under the same equal-quadrature convention, $S=\sqrt{\langle|J_m|^2\rangle}/\sigma_q$ and $S_{\rm dB}=20\log_{10}S$, with $\alpha=0.0027$ and 90\% power.

For $n$ RF frequencies the root-space data vector has $2n$ real coordinates and the homogeneous null fits the two real parameters $(D,w)$, hence $\nu_{\rm root}=2n-2$. The full-channel vector has $6n$ complex measurements, or $12n$ real quadratures. Profiling the complex coefficients $C_f,K_f$ removes $4n$ real nuisance coordinates, and fitting $(D,w)$ removes two more, hence $\nu_{\rm full}=8n-2$. In both protocols the null residual statistic is compared with $\chi^2_{\nu}$; under the fixed heterogeneous alternative it is represented by the corresponding noncentral $\chi^2_{\nu}(\Lambda)$ with the same residual dimension. Thus the quoted power comparison is specific to these two statistics and this alternative; it is not an information-ordering statement.

Through 1 GHz ($n=6$), $\nu_{\rm root}=10$ and $\nu_{\rm full}=46$, with exact-continuum thresholds 90.37 dB root-space and 81.51 dB full-channel. Through 2 GHz ($n=8$), the degrees of freedom are 14 and 62 and the thresholds are 73.20 and 72.28 dB. Through 3 GHz ($n=9$), they are 16 and 70 and the thresholds are 64.21 and 65.00 dB. Same-frequency normal residuals therefore help substantially before the root-dispersion mismatch is large; at 3 GHz the reduced residual dimension of the root-space test slightly offsets the information lost in compression for this particular alternative.'''
s=once(s,old,new,'supp df documentation')

s=s.replace('\\bibliography{PAPER02_REFERENCES_REV7}','\\bibliography{PAPER02_REFERENCES_REV9}')

entry=r'''

@inproceedings{ishibashi1997utc,
  author    = {Ishibashi, T. and Shimizu, N. and Kodama, S. and Ito, H. and Nagatsuma, T. and Furuta, T.},
  title     = {Uni-Traveling-Carrier Photodiodes},
  booktitle = {Ultrafast Electronics and Optoelectronics},
  editor    = {Nuss, M. and Bowers, J.},
  series    = {OSA Trends in Optics and Photonics Series},
  volume    = {13},
  publisher = {Optica Publishing Group},
  year      = {1997},
  note      = {Paper UC3},
  doi       = {10.1364/UEO.1997.UC3}
}
'''
if 'ishibashi1997utc' in bib: raise RuntimeError('UTC entry already exists')
bib=bib.rstrip()+entry

MD.write_text(m); SD.write_text(s); BD.write_text(bib)
print(MD, blob(MD.read_bytes()))
print(SD, blob(SD.read_bytes()))
print(BD, blob(BD.read_bytes()))
