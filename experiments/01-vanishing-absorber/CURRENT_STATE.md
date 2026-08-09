# Current State — Experiment 01: The Vanishing Absorber

**Date:** 2026-08-09  
**Status:** exploratory; active frontier is a wavelength-resolved intrinsic timing prediction for graded HgCdTe; no novelty claim

## 1. Current question

The original active-volume hypothesis was falsified. The project progressed through optical confinement, microscopic transitions, passive/active network resources, semiconductor extraction, tunneling, and HgCdTe band engineering.

The strongest current detector-specific question is now:

> **Does a monotonic compositionally graded HgCdTe absorber imprint a measurable wavelength dependence on intrinsic carrier transit time because photon wavelength determines where in the gap profile absorption can first occur?**

The present high-optical-depth ballistic model predicts a particularly sharp signature:

> **intrinsic transit delay rises from the long-wave endpoint to a maximum at the wavelength corresponding to the entrance band gap, then decreases again for higher photon energies.**

There is still **no manuscript**.

---

## 2. Read first

After root `AGENTS.md`:

1. `HGCDTE_SPECTRAL_DELAY_PEAK.md`
2. `HGCDTE_SPECTRAL_TRANSIT_STATISTICS.md`
3. `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`
4. `HGCDTE_HEAVY_HOLE_PHOTOEXCITATION_LIMIT.md`
5. `HGCDTE_SPECTRAL_GENERATION_DISTRIBUTION.md`
6. `HGCDTE_SPECTRAL_GENERATION_TRANSPORT.md`
7. `HGCDTE_SPECTRAL_TRANSIT_PRIOR_ART_AUDIT.md`
8. `HGCDTE_DIMENSIONLESS_DEVICE_PHASE_MAP.md`
9. `HGCDTE_GRADED_NONLOCAL_II_PHASE_BOUNDARY.md`
10. `HGCDTE_BOUNDARY_COOLING_TRANSIT_FLOOR.md`
11. `HGCDTE_TAT_TOLERANCE_FIELD_ALLOCATION.md`
12. `CLAIM_LEDGER.md`
13. `RESEARCH_LOG.md`

Older optical/control branches remain provenance but are no longer the active frontier.

---

## 3. Material architecture retained from the previous branch

For a quasi-neutral p-type graded absorber,

```math
p=N_v\exp[(E_v-E_F)/(k_BT)].
```

For nearly constant `N_A/N_v`,

```math
\boxed{E_v\approx\text{constant}.}
```

Therefore a decreasing gap

```math
E_g(x)=E_{g,\rm in}-Gx
```

naturally gives

```math
\boxed{E_c(x)\approx E_v+E_g(x),}
```

```math
\boxed{S_c=-dE_c/dx\approx G.}
```

This provides minority-electron drive without requiring the same common-mode electrostatic tilt that creates the ordinary direct-Zener geometry.

The graded-Kane WKB branch showed that, at fixed conduction slope, the ordinary direct-Zener action can increase strongly as the valence-band slope approaches zero.

This does **not** eliminate TAT, interface leakage, or hot-electron processes.

---

## 4. Nonlocal carrier heating remains a separate constraint

Use the mean-energy state

```math
\boxed{
\frac{d\varepsilon}{dx}
=S_c(x)-\frac{\varepsilon}{\ell_E(x)}.
}
```

For a linear graded absorber with constant `ell_E`, cold injection gives

```math
\boxed{
\varepsilon(x)=G\ell_E(1-e^{-x/\ell_E}).
}
```

With threshold surrogate

```math
E_{\rm th}=\chi E_g,
```

the full-span cold-injection phase boundary is

```math
\boxed{
\zeta_{\rm II}(r,\chi)
=
\frac{\chi}
{\chi+(1-e^{-r})/r},
}
```

where

```math
\zeta=\Delta E_g/E_{g,\rm in},
\qquad
r=L/\ell_E.
```

This remains useful for upstream injected carriers or photons energetic enough to be absorbed at the upstream edge.

It should **not** automatically be applied to every detected wavelength.

---

## 5. Spectral generation geometry

For a photon satisfying

```math
E_{g,\rm out}<E_\gamma<E_{g,\rm in},
```

ordinary above-gap absorption cannot begin until

```math
E_g(x_\gamma)=E_\gamma.
```

Thus

```math
\boxed{
x_\gamma
=\frac{E_{g,\rm in}-E_\gamma}{G},
}
```

and its maximum remaining transport distance is

```math
\boxed{
d_\gamma
=\frac{E_\gamma-E_{g,\rm out}}{G}.
}
```

Therefore

```text
longer wavelength
-> first allowed absorption farther downstream
-> shorter maximum remaining carrier path.
```

This is the robust geometric core of the current branch.

---

## 6. Exact generation-position distribution in optical-depth coordinates

Let

```math
y(x)=\int_{x_\gamma}^{x}\alpha(E_\gamma,s)ds
```

and total eligible optical depth

```math
\tau_\gamma=y(L).
```

Conditioned on absorption,

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}
{1-e^{-\tau_\gamma}},
\qquad 0<y<\tau_\gamma.
}
```

For the analytic local edge model

```math
\alpha=C(E_\gamma-E_g)^\beta,
```

with `n=beta+1`,

```math
\boxed{
u(y)
=\delta E
\left(\frac{y}{\tau_\gamma}\right)^{1/n},
}
```

where

```math
u=E_\gamma-E_g(x),
```

```math
\delta E=E_\gamma-E_{g,\rm out}.
```

The remaining band-edge drop is

```math
\boxed{
D(y)=\delta E-u(y).
}
```

This optical statistic is independent of the later transport model.

---

## 7. Critical correction — photoelectrons generated downstream are not cold

If the photon is absorbed where

```math
u=E_\gamma-E_g(x)>0,
```

the electron begins with nonzero excess energy.

Parameterize

```math
\boxed{
\varepsilon_{\rm gen}=\xi_eu.
}
```

The symmetric two-band optical transition gives

```math
\xi_e=1/2.
```

However, HgCdTe's experimentally validated simplified Kane model contains a nearly flat heavy-hole band and observed heavy-hole-to-electron interband transitions.

In that flat-heavy-hole limit,

```math
\boxed{\xi_e\approx1.}
```

Thus a real HgCdTe baseline is likely much closer to `1` than to the symmetric `1/2` result for heavy-hole-dominated absorption, though a full multiband calculation is still required.

Do not use the old cold-downstream-photoelectron assumption.

---

## 8. Corrected exit mean energy

For constant gradient `G` and energy-relaxation length `ell_E`, define

```math
K=G\ell_E.
```

For local photon excess `u`, the remaining gap drop is

```math
D=\delta E-u.
```

The corrected exit mean excess energy is

```math
\boxed{
\varepsilon_{\rm out}(u)
=
K+
(\xi_eu-K)
\exp\!\left[-\frac{\delta E-u}{K}\right].
}
```

Its derivative is

```math
\boxed{
\frac{d\varepsilon_{\rm out}}{du}
=
\exp[-(\delta E-u)/K]
\left[(\xi_e-1)+\frac{\xi_eu}{K}\right].
}
```

Any interior extremum is a minimum. Therefore

```math
\boxed{
\varepsilon_{\max}
=
\max\left[
K(1-e^{-\delta E/K}),
\xi_e\delta E
\right].
}
```

For the flat-heavy-hole limit,

```math
\boxed{
\xi_e=1
\quad\Rightarrow\quad
\varepsilon_{\max}=\delta E
}
```

independent of energy-relaxation length.

Interpretation:

```text
upstream absorption
-> more band-edge acceleration
-> more distance to cool

near-output absorption
-> less band-edge acceleration
-> larger initial photon-excess energy
-> almost no distance to cool.
```

---

## 9. Corrected ballistic transit kernel

Let

```math
q=u/\delta E,
```

```math
s=\delta E/E_{g,\rm out}.
```

Define

```math
e=1+s[1-(1-\xi_e)q],
```

```math
z_s^*=\xi_esq,
```

```math
z_0^*=s[1-(1-\xi_e)q].
```

With

```math
\phi(z,e)=\sqrt{ez}+\frac{z^{3/2}}{3\sqrt e},
```

the exact two-band/Kane ballistic timing kernel is

```math
\boxed{
\theta(q;s,\xi_e)
\equiv
\frac{Gv_K}{E_{g,\rm out}}T_{\rm bal}
=
\phi(z_0^*,e)-\phi(z_s^*,e).
}
```

The exact optical-depth generation distribution can be integrated against this kernel to obtain mean delay and generation-position timing spread.

---

## 10. Strongest current prediction — high-optical-depth spectral delay peak

Let

```math
R=E_{g,\rm in}/E_{g,\rm out}>1.
```

### Photon energy inside the graded gap range

For

```math
0<s\le R-1,
```

high optical depth places absorption near the first allowed point, where the electron is born at the local edge.

Then

```math
\boxed{
\theta_<(s)
=\frac{\sqrt s}{\sqrt{1+s}}
\left(1+\frac43s\right).
}
```

This increases with photon energy because the first allowed generation position moves upstream.

### Photon energy above the entrance gap

For

```math
s>R-1,
```

the whole graded absorber is optically allowed, so high-optical-depth absorption is pinned near the physical entrance.

The path length no longer grows. Higher photon energy only increases initial electron kinetic energy.

For `xi_e>0`, the transit time therefore decreases with further photon energy.

Hence

```math
\boxed{
T(E_\gamma)
\text{ is maximal at }
E_\gamma=E_{g,\rm in}
}
```

inside the current high-optical-depth ballistic model.

In wavelength language,

```math
\boxed{
\lambda_{\rm peak}
\simeq hc/E_{g,\rm in}.
}
```

This is the strongest current candidate experimental signature.

---

## 11. Limiting behavior of the spectral timing curve

At the long-wave output cutoff,

```math
\boxed{T\to0}
```

in the ideal transport model because the eligible generation region collapses toward the collection side.

Exactly at cutoff the absorption coefficient also tends toward the edge, so high optical depth is not guaranteed.

At very high photon energy, for `xi_e>0`,

```math
\boxed{T\to L/v_K.}
```

Therefore the ideal high-QE timing shape is

```text
long-wave endpoint
T -> 0

photon energy rises through graded gap range
T rises

E_gamma = Eg,in
T maximum

photon energy rises above entrance gap
T decreases

very high photon energy
T -> L/vK.
```

---

## 12. Prior-art collision status

Primary literature already establishes separately

- compositionally graded HgCdTe detectors;
- grading-induced carrier drift and faster response;
- graded HgCdTe spectral response/QE;
- tunable-pulse HgCdTe timing measurements;
- heavy-hole-to-electron Kane transitions.

The focused search has **not** found an inspected primary source explicitly deriving or measuring

```text
lambda
-> generation-position distribution
-> corrected graded transit distribution
```

or the more specific

```text
intrinsic timing maximum at the entrance-gap wavelength.
```

**Status:** candidate underexplored / potentially distinct analytic prediction; priority unproven.

The closest graded high-speed experiments found use fixed short-wave excitation rather than sweeping through the graded IR absorption range.

Do not claim novelty from the negative search.

---

## 13. Timing-spread correction

At finite optical depth, increasing absorption probability generally moves the mean generation position upstream and increases mean remaining transport distance.

But generation-position timing spread is **not generally monotonic** with optical depth. Numerical quadrature shows it can rise slightly from very thin to moderate optical depth before decreasing toward zero in the optically thick limit.

Do not claim a universal `higher QE -> lower jitter` law.

---

## 14. Collection-boundary result retained

A wider-gap boundary remains useful for separating leakage protection from graded acceleration.

Barrier-free extraction requires

```math
qV_b\ge\alpha\Delta E_g^{(b)}.
```

Local TAT/BTBT voltage capacity requires

```math
V_b\le\int F_{\rm allow}(x)dx.
```

At minimum compensation the total conduction edge is flat, so the boundary can serve as a relaxation region rather than adding further downhill carrier work.

This remains a complementary architectural result rather than the present timing prediction.

---

## 15. Numerical regressions

Current relevant regressions include

```text
numerics/hgcdte_spectral_delay_peak.py
numerics/hgcdte_spectral_transit_statistics.py
numerics/hgcdte_dimensionless_device_phase_map.py
numerics/hgcdte_ii_safe_transit_ceiling.py
numerics/hgcdte_graded_nonlocal_ii_phase_boundary.py
numerics/hgcdte_graded_kane_wkb.py
```

They protect

- the nonzero-initial-energy transit integral;
- the entrance-gap timing maximum;
- the high-energy `L/v_K` asymptote;
- the endpoint maximum of finite-relaxation exit energy;
- the earlier graded-II phase boundaries.

No CI is justified yet.

---

## 16. Main missing inputs

For quantitative HgCdTe prediction, need

```text
multiband optical transition / xi_e(E_gamma,x)
+
calibrated alpha(E_gamma,x,T)
+
ell_E(E,x,T)
+
stochastic Gamma_II(E,x)
+
real Eg(x), Ec(x), Ev(x) under doping and bias
+
readout / RC transfer function for comparison to experiment.
```

Do not invent coefficients from narrative literature statements.

---

## 17. Next decisive work

Do **not** open a manuscript yet.

The next step should test robustness of the timing peak rather than extend the abstract theory.

Priority order:

1. add one finite energy-relaxation/scattering model to determine whether the entrance-gap timing maximum survives beyond the ballistic limit;
2. search/reanalyze any tunable-wavelength graded-HgCdTe impulse-response data under fixed bias/readout;
3. if no data exist, formulate the tunable-pulse spectral timing sweep as the proposed decisive experiment.

If the timing peak survives scattering and remains absent from prior literature, reassess publication significance at that point.
