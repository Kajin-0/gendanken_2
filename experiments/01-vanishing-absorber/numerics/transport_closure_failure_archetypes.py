"""Archetypal violations of the real multi-frequency drift-diffusion closure.

This is a theory regression, not a calibrated HgCdTe model.

Baseline uniform conditioned local Markov transport:

    D r^2 + w r = s,       s=i omega.

Three deliberately simple departures are compared by asking what ordinary
second-order drift-diffusion would infer at each frequency:

1. reversible immobilizing trap state
       Psi(s)=s [1 + k_t/(k_d+s)]
   with D r^2+w r=Psi;

2. finite flux-relaxation / telegraph archetype
       Psi(s)=s(1+tau_J s);

3. leading spatially nonlocal Kramers-Moyal correction
       C r^3+D r^2+w r=s.

For each case calculate the REAL apparent D_app(omega),w_app(omega) that would
be inferred if the data were forced into the ordinary local Markov closure.
Frequency dispersion is the falsification signal.
"""

from __future__ import annotations

import numpy as np


D0 = 0.08
W0 = 1.55
FREQUENCIES = np.asarray((0.10, 0.20, 0.50, 1.0, 2.0, 5.0), dtype=float)

K_TRAP = 0.80
K_DETRAP = 1.00
TAU_FLUX = 0.015
C_SPATIAL = 0.020


def quadratic_root(rhs: complex) -> complex:
    return (np.sqrt(W0 * W0 + 4.0 * D0 * rhs) - W0) / (2.0 * D0)


def spatial_cubic_root(s: complex) -> complex:
    roots = np.roots((C_SPATIAL, D0, W0, -s))
    reference = quadratic_root(s)
    return complex(roots[np.argmin(np.abs(roots - reference))])


def apparent(r: complex, omega: float):
    A = r * r
    delta = A.real * r.imag - A.imag * r.real
    return np.asarray(
        (
            -omega * r.real / delta,
            omega * A.real / delta,
        )
    )


def model_roots(name: str) -> np.ndarray:
    roots = []
    for omega in FREQUENCIES:
        s = 1j * omega
        if name == "markov":
            r = quadratic_root(s)
        elif name == "trap":
            psi = s * (1.0 + K_TRAP / (K_DETRAP + s))
            r = quadratic_root(psi)
        elif name == "flux":
            psi = s * (1.0 + TAU_FLUX * s)
            r = quadratic_root(psi)
        elif name == "spatial":
            r = spatial_cubic_root(s)
        else:
            raise ValueError(name)
        roots.append(r)
    return np.asarray(roots)


def apparent_table(name: str) -> np.ndarray:
    roots = model_roots(name)
    return np.asarray([apparent(r, om) for r, om in zip(roots, FREQUENCIES)])


def main() -> None:
    tables = {name: apparent_table(name) for name in ("markov", "trap", "flux", "spatial")}

    print("Multi-frequency closure-failure archetypes")
    print(f"baseline D={D0:.6f}, w={W0:.6f}")
    print()

    for name, table in tables.items():
        print(name)
        print(
            "  D_app = "
            + ", ".join(f"{x:.6f}" for x in table[:, 0])
        )
        print(
            "  w_app = "
            + ", ".join(f"{x:.6f}" for x in table[:, 1])
        )
        print(
            "  ranges = "
            f"Delta D {np.ptp(table[:,0]):.6f}, "
            f"Delta w {np.ptp(table[:,1]):.6f}"
        )
        print()

    markov = tables["markov"]
    trap = tables["trap"]
    flux = tables["flux"]
    spatial = tables["spatial"]

    # Exact baseline closure.
    assert np.max(np.abs(markov[:, 0] - D0)) < 1.0e-11
    assert np.max(np.abs(markov[:, 1] - W0)) < 1.0e-11

    # Reversible trapping produces strong turnover/dispersion on the chosen
    # dimensionless frequency range.
    assert np.ptp(trap[:, 0]) > 0.20
    assert np.ptp(trap[:, 1]) > 0.45

    # Finite flux relaxation is subtler here but still violates closure.
    assert np.ptp(flux[:, 0]) > 1.0e-3
    assert np.ptp(flux[:, 1]) > 1.0e-2

    # Leading spatial nonlocality leaves the low-frequency limit nearly intact
    # and grows strongly with frequency.
    assert abs(spatial[0, 0] - D0) < 1.0e-4
    assert abs(spatial[0, 1] - W0) < 2.0e-4
    assert spatial[-1, 0] - D0 > 0.03
    assert W0 - spatial[-1, 1] > 0.20

    # Low-frequency analytic limits.
    c1_trap = 1.0 + K_TRAP / K_DETRAP
    c2_trap = -K_TRAP / K_DETRAP**2
    D_trap_0 = D0 / c1_trap - c2_trap * W0**2 / c1_trap**3
    w_trap_0 = W0 / c1_trap

    D_flux_0 = D0 - TAU_FLUX * W0**2
    w_flux_0 = W0

    print("analytic omega->0 apparent coefficients")
    print(f"  trap: D_app -> {D_trap_0:.6f}, w_app -> {w_trap_0:.6f}")
    print(f"  flux: D_app -> {D_flux_0:.6f}, w_app -> {w_flux_0:.6f}")
    print(f"  spatial: D_app -> {D0:.6f}, w_app -> {W0:.6f}")

    # 0.1 is already close to the analytic low-frequency limits.
    assert abs(trap[0, 0] - D_trap_0) < 1.0e-3
    assert abs(trap[0, 1] - w_trap_0) < 1.0e-4
    assert abs(flux[0, 0] - D_flux_0) < 2.0e-5
    assert abs(flux[0, 1] - w_flux_0) < 2.0e-5

    print()
    print(
        "PASS: a single low-frequency measurement can absorb several memory "
        "mechanisms into renormalized apparent transport coefficients. Their "
        "frequency dispersion, not one-frequency fit quality, is the robust "
        "local-Markov falsification signal."
    )


if __name__ == "__main__":
    main()
