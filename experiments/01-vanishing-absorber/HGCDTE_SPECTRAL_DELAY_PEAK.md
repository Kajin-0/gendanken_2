# HgCdTe Spectral Delay Peak — A High-Optical-Depth Timing Fingerprint of a Monotonic Gap Gradient

**Date:** 2026-08-09  
**Status:** exact ballistic two-band/Kane high-optical-depth result for a linear graded absorber with parameterized photoelectron excess partition; candidate testable analytic prediction; priority unproven

## 1. Question

For a linearly decreasing HgCdTe band gap, the earliest optically allowed generation position moves upstream as photon energy rises—until the photon exceeds the entrance gap.

What does that imply for intrinsic carrier transit time at high optical depth, where absorption occurs close to the earliest allowed position?

The result is nonmonotonic.

---

## 2. Device profile

Let

```math
E_g(x)=E_{g,\rm in}-Gx,
\qquad 0\le x\le L,
```

with

```math
E_{g,\rm out}=E_{g,\rm in}-GL.
```

Assume quasi-neutral p-type majority-band pinning and ballistic motion in the two-band/Kane conduction branch.

Define

```math
E_0=E_{g,\rm out}
```

and the entrance-to-exit gap ratio

```math
\boxed{R=E_{g,\rm in}/E_0>1.}
```

For photon energy `E_gamma`, define

```math
\boxed{s=E_\gamma/E_0-1.}
```

---

## 3. Spectral region I — photon energy inside the graded gap range

For

```math
E_0<E_\gamma\le E_{g,\rm in},
```

or

```math
0<s\le R-1,
```

the earliest allowed generation point satisfies

```math
E_g(x_\gamma)=E_\gamma.
```

At that point the photon is exactly at the local interband edge, so the electron is born cold in the ideal model.

The high-optical-depth ballistic delay is

```math
\boxed{
T_<(E_\gamma)
=\frac{E_0}{Gv_K}
\theta_<(s),
}
```

with

```math
\boxed{
\theta_<(s)
=\frac{\sqrt s}{\sqrt{1+s}}
\left(1+\frac43s\right).
}
```

This increases monotonically with `s`.

Therefore, moving to shorter wavelength within the graded-gap interval moves generation farther upstream and increases the intrinsic transit delay.

---

## 4. Spectral region II — photon energy above the entrance gap

For

```math
E_\gamma>E_{g,\rm in},
```

or

```math
s>R-1,
```

the entire graded region is energetically eligible.

At high optical depth, absorption occurs near the physical entrance

```math
x=0.
```

The geometric path is now fixed at

```math
L=(E_{g,\rm in}-E_0)/G.
```

Further increases in photon energy no longer increase path length.

Instead they increase the electron's initial excess energy.

Let `xi_e` be the electron share of photon excess above the entrance gap:

```math
\varepsilon_{\rm gen}
=\xi_e(E_\gamma-E_{g,\rm in}).
```

Define dimensionless conserved electron energy

```math
\boxed{
e
=R+\xi_e(1+s-R),
}
```

initial excess

```math
\boxed{
z_s
=\xi_e(1+s-R),
}
```

and final excess

```math
\boxed{
z_0
=z_s+(R-1).
}
```

Using

```math
\phi(z,e)
=\sqrt{ez}+\frac{z^{3/2}}{3\sqrt e},
```

the high-optical-depth transit becomes

```math
\boxed{
T_>(E_\gamma)
=\frac{E_0}{Gv_K}
\left[
\phi(z_0,e)-\phi(z_s,e)
\right].
}
```

---

## 5. The delay is maximal at the entrance-gap photon energy

At the transition

```math
E_\gamma=E_{g,\rm in},
```

```math
s=R-1,
```

and the electron is generated cold at the physical entrance.

The two expressions join continuously:

```math
\boxed{
T_<(E_{g,\rm in})
=T_>(E_{g,\rm in}).
}
```

For photon energies above the entrance gap and `xi_e>0`, the geometric path remains fixed while the conserved electron energy increases.

For the Kane conduction branch, group velocity at fixed local gap increases with total electron energy. Therefore the transit time through that fixed profile decreases.

Hence

```math
\boxed{
T(E_\gamma)
\text{ has a maximum at }
E_\gamma=E_{g,\rm in}
}
```

within the stated high-optical-depth ballistic model.

In wavelength language, the delay maximum occurs at the **entrance cutoff wavelength**

```math
\boxed{
\lambda_{\rm peak}
\simeq
hc/E_{g,\rm in}.
}
```

---

## 6. Limiting behavior

### Long-wave endpoint

As

```math
E_\gamma\to E_0^+,
```

the earliest allowed generation point approaches the output and

```math
\boxed{T\to0.}
```

The optical absorption coefficient also approaches the edge and may become small, so this is not a statement of finite high QE exactly at cutoff.

### Very high photon energy

For `xi_e>0` and

```math
E_\gamma\gg E_{g,\rm in},
```

the electron velocity approaches the Kane velocity over most of the profile.

Therefore

```math
\boxed{
T\to L/v_K
=\frac{E_0}{Gv_K}(R-1).
}
```

The delay maximum at the entrance gap is larger than this asymptotic floor because the entrance-gap electron starts with zero group velocity and accelerates through the device.

---

## 7. Heavy-hole limit

The simplified HgCdTe Kane model contains a nearly flat heavy-hole band. For heavy-hole-to-electron photoexcitation, a useful baseline is

```math
\xi_e\approx1.
```

Then above the entrance gap

```math
\boxed{
e=1+s,}
```

```math
\boxed{
z_s=1+s-R,}
```

```math
\boxed{
z_0=s.}
```

Thus

```math
\boxed{
\theta_>(s;R,\xi_e=1)
=
\phi(s,1+s)
-
\phi(1+s-R,1+s).
}
```

This decreases from the entrance-gap peak toward `R-1`.

---

## 8. Example — factor-of-two gap span

Take

```math
R=2.
```

This corresponds approximately to an entrance cutoff one half of the output cutoff.

The dimensionless delay

```math
\theta=(Gv_K/E_0)T
```

for the heavy-hole baseline is

| `E_gamma/E0` | spectral location | `theta` |
|---:|---|---:|
| 1.05 | near output cutoff | 0.233 |
| 1.10 | inside gradient | 0.342 |
| 1.25 | inside gradient | 0.596 |
| 1.50 | inside gradient | 0.962 |
| 2.00 | **entrance gap** | **1.650** |
| 2.50 | above entrance gap | 1.131 |
| 3.00 | above entrance gap | 1.069 |
| 4.00 | above entrance gap | 1.030 |
| infinity | high-energy limit | 1.000 |

The predicted intrinsic timing fingerprint is therefore a pronounced peak at the wavelength corresponding to the high-gap entrance.

---

## 9. Why this may be experimentally useful

The peak location depends on

```math
E_{g,\rm in},
```

which is set by the composition profile.

The overall time scale depends on

```math
E_0/(Gv_K).
```

But the **shape** and peak wavelength are dimensionless consequences of the graded profile in the high-optical-depth ballistic model.

A tunable ultrafast source could therefore test

```text
long-wave side:
short delay near output cutoff
-> rising delay toward entrance-gap wavelength

short-wave side:
delay decreases again once the whole absorber is optically allowed.
```

A common wavelength-independent RC/readout pole would broaden all pulses but need not move the intrinsic peak in the same way.

---

## 10. Prior-art posture

Primary HgCdTe work already establishes

- graded-gap devices with faster carrier response;
- composition-dependent spectral response;
- tunable-pulse time-response measurements;
- heavy-hole-to-electron Kane interband transitions.

The focused search to date has not located an inspected primary HgCdTe paper explicitly predicting this **nonmonotonic wavelength-dependent intrinsic transit peak at the entrance-gap energy**.

Status:

**CANDIDATE DISTINCT / UNDEREXPLORED ANALYTIC PREDICTION — PRIORITY UNPROVEN.**

Negative search is not novelty evidence.

---

## 11. Caveats

The peak result assumes

- monotonic linear grading;
- high optical depth at the wavelength being considered;
- local direct absorption;
- ballistic two-band/Kane electron transport;
- pinned majority-hole band;
- `xi_e>0` above the entrance gap;
- no scattering, diffusion, recombination, avalanche, interface delay, or readout pole.

Finite optical depth broadens the generation-position distribution and smooths the peak.

Scattering can strongly alter the quantitative shape.

---

## 12. Next decisive test

The next research step should be empirical collision, not more symbolic optimization:

> search specifically for tunable-wavelength impulse-response data from a **compositionally graded HgCdTe detector** under fixed device bias and readout conditions.

If suitable raw/figure data exist, compare whether an intrinsic timing extremum occurs near the entrance-gap wavelength.

If not, this becomes a concrete proposed experiment and the next theoretical step should add one scattering/relaxation model to determine how robust the peak is beyond the ballistic limit.
