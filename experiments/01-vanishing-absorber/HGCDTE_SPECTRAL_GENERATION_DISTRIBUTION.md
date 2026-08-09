# HgCdTe Spectral Generation Distribution — Quantum Efficiency, Transit Geometry, and Corrected Photoelectron Energy

**Date:** 2026-08-09  
**Status:** exact optical-depth generation statistics plus corrected conditional carrier-energy mapping; no novelty claim

## 1. Optical-depth generation distribution

For a fixed photon energy, let `x_gamma` be the earliest position where ordinary above-gap absorption is energetically allowed.

Define accumulated optical depth

```math
\boxed{
y(x)
=\int_{x_\gamma}^{x}
\alpha(E_\gamma,s)ds
}
```

and total eligible optical depth

```math
\boxed{\tau_\gamma=y(L).}
```

The single-pass absorption probability is

```math
\boxed{\eta_\gamma=1-e^{-\tau_\gamma}.}
```

Conditioned on absorption, the generation optical depth is exactly

```math
\boxed{
p(y|{\rm abs})
=\frac{e^{-y}}
{1-e^{-\tau_\gamma}},
\qquad 0\le y\le\tau_\gamma.
}
```

This distribution is independent of the detailed spatial form of `alpha(x)`.

---

## 2. Power-law near-edge mapping

For the analytic local model

```math
\alpha(E_\gamma,x)
=C[E_\gamma-E_g(x)]^\beta,
\qquad
\beta>-1,
```

inside a linear gap

```math
E_g(x)=E_{g,\rm in}-Gx,
```

define

```math
u=E_\gamma-E_g(x),
```

```math
\delta E=E_\gamma-E_{g,\rm out},
```

and

```math
n=\beta+1.
```

Then

```math
\boxed{
y(u)
=\frac{C}{Gn}u^n,
}
```

```math
\boxed{
\tau_\gamma
=\frac{C}{Gn}(\delta E)^n,
}
```

and therefore

```math
\boxed{
u(y)
=\delta E
\left(\frac{y}{\tau_\gamma}\right)^{1/n}.}
```

---

## 3. Remaining geometric transport after generation

The remaining downhill conduction-band drop is

```math
\boxed{
D(y)
=\delta E-u(y)
=\delta E
\left[
1-
\left(\frac{y}{\tau_\gamma}\right)^{1/n}
\right].
}
```

The remaining geometric distance is

```math
\boxed{d(y)=D(y)/G.}
```

This geometry is independent of how photon excess is partitioned between electron and hole.

Thus the robust generation-position conclusion remains:

```text
higher optical depth
-> absorption biased closer to the earliest allowed position
-> larger remaining transport distance for detected carriers.
```

---

## 4. Mean remaining distance / band-edge drop

The conditional mean local photon excess is

```math
\boxed{
\langle u\rangle
=
\frac{\delta E}{1-e^{-\tau_\gamma}}
\tau_\gamma^{-1/n}
\gamma\!\left(1+\frac1n,\tau_\gamma\right),
}
```

where lowercase `gamma` is the lower incomplete gamma function.

Hence

```math
\boxed{
\langle D\rangle
=
\delta E-
\langle u\rangle.
}
```

and

```math
\boxed{
\langle d\rangle
=\langle D\rangle/G.
}
```

### Optically thin limit

For `tau_gamma << 1`,

```math
\boxed{
\langle D\rangle
\to
\frac{\delta E}{\beta+2}.
}
```

For the illustrative `beta=1/2`,

```math
\boxed{
\langle D\rangle\to0.4\delta E.
}
```

### Optically thick limit

For `tau_gamma >> 1`,

```math
\boxed{\langle D\rangle\to\delta E.}
```

So high single-pass absorption pushes detected events toward longer remaining graded transport.

---

## 5. Critical correction — downstream-generated electrons are not cold

For an absorption event at local photon excess `u`, parameterize the electron share of that excess as

```math
\boxed{
\varepsilon_{\rm gen}(u)
=\xi_eu,
\qquad 0\le\xi_e\le1.
}
```

The symmetric two-band Kane optical transition gives

```math
\boxed{\xi_e=1/2,}
```

but real HgCdTe requires a multiband optical-transition calculation.

Therefore `D(y)` is the **remaining band-edge work**, not the total final hot-electron energy.

See `HGCDTE_PHOTOEXCITATION_ENERGY_PARTITION.md`.

---

## 6. Corrected mean-energy trajectory for each generation position

For constant downstream gradient `G` and energy-relaxation length `ell_E`, define

```math
D(u)=\delta E-u.
```

Then

```math
\boxed{
\varepsilon_{\rm out}(u)
=
\xi_eu
\exp\!\left[-\frac{D(u)}{G\ell_E}\right]
+
G\ell_E
\left\{
1-
\exp\!\left[-\frac{D(u)}{G\ell_E}\right]
\right\}.
}
```

The generation-position distribution therefore induces an energy distribution through

```math
u(y)=\delta E(y/\tau_\gamma)^{1/n}.
```

The mean exit energy among absorbed photons is

```math
\boxed{
\langle\varepsilon_{\rm out}\rangle
=
\frac1{1-e^{-\tau_\gamma}}
\int_0^{\tau_\gamma}
 e^{-y}
\varepsilon_{\rm out}[u(y)]dy.
}
```

No closed form is required for the current argument.

---

## 7. Ballistic limit

For `ell_E -> infinity`,

```math
\boxed{
\varepsilon_{\rm out}^{\rm bal}(u)
=\delta E-(1-\xi_e)u.
}
```

Hence

```math
\boxed{
\langle\varepsilon_{\rm out}^{\rm bal}\rangle
=\delta E-(1-\xi_e)\langle u\rangle.
}
```

This exposes a major distinction:

```text
generation farther downstream
-> always reduces remaining transit distance

but

generation farther downstream
-> reduces final ballistic electron energy only by factor (1-xi_e) of the local photon excess.
```

For `xi_e -> 1`, final ballistic electron energy is nearly independent of generation position.

---

## 8. Corrected threshold-accessible fraction

Use the deterministic output threshold surrogate

```math
E_{\rm th,out}=\chi E_{g,\rm out}.
```

For finite relaxation, the critical generation excess `u_c` is defined implicitly by

```math
\boxed{
\varepsilon_{\rm out}(u_c)
=\chi E_{g,\rm out}.
}
```

Because the energy formula now contains both initial photoexcitation energy and downstream band-edge work, the previous cold-injection closed form for the threshold-accessible generation fraction is **superseded**.

When a unique physical `u_c` exists in `[0,delta E]`, convert it to optical depth

```math
\boxed{
y_c
=\tau_\gamma
\left(\frac{u_c}{\delta E}\right)^n.}
```

The relevant generation fraction is then obtained from the exact truncated-exponential CDF, with the inequality direction determined by the monotonicity of `epsilon_out(u)` for the chosen `xi_e` and relaxation parameters.

Do not reuse the old cold-generation fraction formula.

---

## 9. Ballistic all-position safety condition survives

For `0 <= xi_e <= 1`,

```math
\varepsilon_{\rm out}^{\rm bal}(u)
\le\delta E.
```

Therefore the earliest allowed generation position remains the worst ballistic case, and the sufficient condition

```math
\boxed{
\delta E<\chi E_{g,\rm out}
}
```

still guarantees that every generation position is below the deterministic mean threshold in the ballistic model.

This corresponds approximately to

```math
\boxed{
\lambda_\gamma>
\lambda_{c,\rm out}/(1+\chi).
}
```

---

## 10. Quantum-efficiency / transport interpretation

Increasing `tau_gamma` raises single-pass absorption and biases absorbed photons toward small `y`, hence toward the earliest eligible region.

Robustly,

```text
higher optical depth
-> higher QE
-> larger mean remaining transport distance.
```

For hot-electron energy, the effect depends additionally on

```text
xi_e
+
ell_E
+
local gap profile.
```

Therefore a generic statement that high QE necessarily creates proportionally hotter electrons is too strong.

---

## 11. Claim boundary

### Exact

- conditional optical-depth generation distribution;
- `y <-> u` mapping for the stated local absorption law;
- remaining geometric distance distribution.

### Corrected / conditional

Hot-electron energy must include photoexcitation excess through `xi_e`.

### Superseded

The earlier cold-injection closed form for the fraction of downstream-generated absorbed photons whose mean trajectory reaches threshold.

### Open

- calibrated HgCdTe `xi_e(E_gamma,x)`;
- calibrated `alpha(E_gamma,x)`;
- stochastic II probability;
- real transport-time distribution;
- optical coherence/interference;
- novelty.

---

## 12. Next step

Propagate the exact generation distribution through the corrected ballistic/nonlocal transport formulas and obtain wavelength-resolved mean delay and generation-position timing spread as a function of `xi_e`.
