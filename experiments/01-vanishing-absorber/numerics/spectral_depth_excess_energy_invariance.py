"""Spectral-depth / initial-excess-energy invariance theorem regression.

Ideal theorem
-------------
Let a monotonic graded absorber have affine gap

    Eg(z)=Eg0-G z,  G>0,

and local absorption depend only on photon excess energy

    u=Eph-Eg(z),  alpha=alpha(u), alpha(u<=0)=0.

For a photon energy Eph whose threshold lies away from boundaries, changing Eph
translates z_t but the generation distribution expressed in u is exactly

    p_u(u)=alpha(u)/G * exp[-(1/G) int_0^u alpha(v)dv],

up to a common absorption-conditioning normalization if the downstream domain is
finite.  On a sufficiently deep/full-absorption domain p_u is photon-energy
independent exactly.

Real HgCdTe stress
------------------
The script also evaluates the current 300-K, 7.6-um linear x=0.55->0.32
Hansen/Moazzami quartet selected by mean generation depths 2.5,3.0,3.5,4.0 um.
It reports the generation-weighted distribution of total photon excess energy
Eph-Eg(z).  The near-invariance is numerical/conditional, not an exact HgCdTe
law and not a statement about electron/hole partition after photoexcitation.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq


# ---------------------------------------------------------------------------
# Ideal affine-gap theorem check
# ---------------------------------------------------------------------------
EG0 = 1.20
G = 0.080  # eV per arbitrary length
Z = np.linspace(0.0, 20.0, 200001)
A0 = 22.0
POWER = 0.72
PHOTON_ENERGIES = (0.88, 0.94, 1.00)


def alpha_ideal(u: np.ndarray) -> np.ndarray:
    out = np.zeros_like(u)
    mask = u > 0.0
    out[mask] = A0 * u[mask] ** POWER
    return out


def ideal_generation(Eph: float):
    gap = EG0 - G * Z
    u = Eph - gap
    alpha = alpha_ideal(u)
    tau = np.concatenate(([0.0], cumulative_trapezoid(alpha, Z)))
    density = alpha * np.exp(-tau)
    density /= np.trapezoid(density, Z)
    mean_z = float(np.trapezoid(Z * density, Z))
    mean_u = float(np.trapezoid(u * density, Z))
    var_u = float(np.trapezoid((u - mean_u) ** 2 * density, Z))
    return mean_z, mean_u, var_u, u, density


# ---------------------------------------------------------------------------
# Real HgCdTe conditional stress
# ---------------------------------------------------------------------------
HC_EV_UM = 1.2398419843320026
T_K = 300.0
L_UM = 7.6
X_FRONT = 0.55
X_BACK = 0.32
Z_HG = np.linspace(0.0, L_UM, 20001)
X_HG = X_FRONT + (X_BACK - X_FRONT) * Z_HG / L_UM
TARGET_MEANS = (2.5, 3.0, 3.5, 4.0)


def eg_hansen(x, T=T_K):
    return (
        -0.302 + 1.93 * x + 5.35e-4 * T * (1.0 - 2.0 * x)
        - 0.81 * x**2 + 0.832 * x**3
    )


def k_moazzami(x, T=T_K):
    return (
        -20060.0 + 115750.0 * x + 32.43 * T - 64170.0 * x**2
        + 0.43231 * T**2 - 101.92 * x * T
    )


def n_moazzami(x, T=T_K):
    return 0.74487 - 0.44513 * x + (0.000799 - 0.000757 * x) * T


def hg_generation(wavelength_um: float):
    Eph = HC_EV_UM / wavelength_um
    gap = eg_hansen(X_HG)
    frac = (Eph - gap) / Eph
    alpha = np.zeros_like(frac)
    mask = frac > 0.0
    alpha[mask] = (
        k_moazzami(X_HG[mask])
        * frac[mask] ** n_moazzami(X_HG[mask])
    )
    alpha = np.maximum(alpha, 0.0)
    tau = np.concatenate(
        ([0.0], cumulative_trapezoid(alpha, Z_HG * 1.0e-4))
    )
    density = alpha * 1.0e-4 * np.exp(-tau)
    pabs = float(1.0 - np.exp(-tau[-1]))
    density /= np.trapezoid(density, Z_HG)
    mean_z = float(np.trapezoid(Z_HG * density, Z_HG))

    excess = Eph - gap
    mean_u = float(np.trapezoid(excess * density, Z_HG))
    centered = excess - mean_u
    var_u = float(np.trapezoid(centered**2 * density, Z_HG))
    third = float(np.trapezoid(centered**3 * density, Z_HG))
    skew = third / var_u ** 1.5
    return pabs, mean_z, mean_u, var_u, skew, density


def wavelength_for_mean(target: float) -> float:
    return float(
        brentq(
            lambda wavelength: hg_generation(wavelength)[1] - target,
            1.95,
            3.20,
        )
    )


def main() -> None:
    print("Ideal affine-gap excess-energy translation theorem")
    ideal = [ideal_generation(E) for E in PHOTON_ENERGIES]
    mean_us = np.asarray([x[1] for x in ideal])
    var_us = np.asarray([x[2] for x in ideal])
    mean_zs = np.asarray([x[0] for x in ideal])

    for E, result in zip(PHOTON_ENERGIES, ideal):
        print(
            f"Eph={E:.3f} eV: mean z={result[0]:.9f}, "
            f"mean excess={result[1]:.12f} eV, "
            f"std excess={np.sqrt(result[2]):.12f} eV"
        )

    # Threshold-depth shift is Delta Eph/G; the generation u moments are common.
    expected_dz = np.diff(PHOTON_ENERGIES) / G
    observed_dz = np.diff(mean_zs)
    assert np.max(np.abs(observed_dz - expected_dz)) < 2.0e-8
    assert np.ptp(mean_us) < 2.0e-10
    assert np.ptp(var_us) < 2.0e-11

    print()
    print("Real HgCdTe quartet")
    wavelengths = [wavelength_for_mean(target) for target in TARGET_MEANS]
    rows = [hg_generation(wavelength) for wavelength in wavelengths]

    hg_mean_u = []
    hg_std_u = []
    hg_skew = []
    for target, wavelength, row in zip(TARGET_MEANS, wavelengths, rows):
        pabs, mean_z, mean_u, var_u, skew, _ = row
        hg_mean_u.append(mean_u)
        hg_std_u.append(np.sqrt(var_u))
        hg_skew.append(skew)
        print(
            f"mean z={target:.1f} um, lambda={wavelength:.9f} um, "
            f"Pabs={pabs:.9f}, mean excess={1e3*mean_u:.6f} meV, "
            f"std excess={1e3*np.sqrt(var_u):.6f} meV, skew={skew:.6f}"
        )

    hg_mean_u = np.asarray(hg_mean_u)
    hg_std_u = np.asarray(hg_std_u)
    hg_skew = np.asarray(hg_skew)

    mean_rel_span = np.ptp(hg_mean_u) / np.mean(hg_mean_u)
    std_rel_span = np.ptp(hg_std_u) / np.mean(hg_std_u)
    print()
    print(f"HgCdTe mean-excess relative span = {100*mean_rel_span:.4f}%")
    print(f"HgCdTe std-excess relative span = {100*std_rel_span:.4f}%")

    assert min(row[0] for row in rows) > 0.9993
    assert mean_rel_span < 0.003
    assert std_rel_span < 0.02
    assert 0.89 < np.min(hg_skew) < np.max(hg_skew) < 0.97

    print()
    print(
        "PASS: in the ideal affine-gap/excess-energy absorption model, changing "
        "photon energy translates generation depth while preserving the full "
        "initial total excess-energy distribution.  The real Hansen/Moazzami "
        "HgCdTe quartet is close: mean excess energy varies by <0.3% and its "
        "standard deviation by <2% across the four channels."
    )


if __name__ == "__main__":
    main()
