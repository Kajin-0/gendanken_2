"""Exact recombination identifiability theorem for uniform drift-diffusion.

For constant drift v, diffusion D, and recombination rate kappa, the localized
first-passage transform has spatial exponent

    gamma(s) = [sqrt(v^2 + 4D(kappa+s)) - v]/(2D).

If RF transfer is conditioned on DC-collected carriers, its spatial exponent is

    Gamma(omega) = gamma(i omega) - gamma(0).

Defining

    Vstar = sqrt(v^2 + 4D kappa),

one gets exactly

    Gamma = [sqrt(Vstar^2 + 4 i D omega) - Vstar]/(2D).

Thus normalized RF identifies D and Vstar, but cannot separate v and kappa.
If the DC collection spatial slope gamma0 is also measured, then

    v = Vstar - 2D gamma0
    kappa = Vstar*gamma0 - D*gamma0^2.
"""

from __future__ import annotations

import numpy as np


def gamma_full(v: float, D: float, kappa: float, s: complex) -> complex:
    return (np.sqrt(v * v + 4.0 * D * (kappa + s)) - v) / (2.0 * D)


def invert_no_recomb_form(Gamma: complex, omega: float) -> tuple[float, float]:
    a = float(np.real(Gamma))
    b = float(np.imag(Gamma))
    modulus2 = a * a + b * b
    D = omega * a / (b * modulus2)
    Vstar = omega * (b * b - a * a) / (b * modulus2)
    return D, Vstar


def main() -> None:
    cases = (
        (1.40, 0.080, 0.60, 3.0),
        (2.20, 0.150, 0.25, 1.7),
        (0.95, 0.035, 1.10, 5.5),
    )

    max_collapse_error = 0.0
    max_v_error = 0.0
    max_kappa_error = 0.0

    for v, D, kappa, omega in cases:
        gamma0 = gamma_full(v, D, kappa, 0.0)
        gammaw = gamma_full(v, D, kappa, 1j * omega)
        Gamma = gammaw - gamma0

        Vstar = np.sqrt(v * v + 4.0 * D * kappa)
        Gamma_collapsed = (
            np.sqrt(Vstar * Vstar + 4j * D * omega) - Vstar
        ) / (2.0 * D)
        max_collapse_error = max(
            max_collapse_error,
            abs(Gamma - Gamma_collapsed),
        )

        D_rec, Vstar_rec = invert_no_recomb_form(Gamma, omega)
        v_rec = Vstar_rec - 2.0 * D_rec * float(np.real(gamma0))
        kappa_rec = (
            Vstar_rec * float(np.real(gamma0))
            - D_rec * float(np.real(gamma0)) ** 2
        )

        max_v_error = max(max_v_error, abs(v_rec / v - 1.0))
        max_kappa_error = max(
            max_kappa_error, abs(kappa_rec / kappa - 1.0)
        )

    # Explicit non-identifiability pair: same D and Vstar, different v,kappa.
    D = 0.10
    Vstar = 1.80
    omega = 2.5
    v1 = 1.70
    k1 = (Vstar * Vstar - v1 * v1) / (4.0 * D)
    v2 = 1.45
    k2 = (Vstar * Vstar - v2 * v2) / (4.0 * D)

    G1 = gamma_full(v1, D, k1, 1j * omega) - gamma_full(v1, D, k1, 0.0)
    G2 = gamma_full(v2, D, k2, 1j * omega) - gamma_full(v2, D, k2, 0.0)

    print("Uniform drift-diffusion recombination identifiability")
    print(f"max exact Vstar-collapse error = {max_collapse_error:.3e}")
    print(f"max recovered-v relative error = {max_v_error:.3e}")
    print(f"max recovered-kappa relative error = {max_kappa_error:.3e}")
    print(
        "explicit indistinguishable normalized-RF pair: "
        f"(v1,k1)=({v1:.3f},{k1:.3f}), "
        f"(v2,k2)=({v2:.3f},{k2:.3f}), "
        f"|Gamma1-Gamma2|={abs(G1-G2):.3e}"
    )

    assert max_collapse_error < 3.0e-15
    assert max_v_error < 5.0e-14
    assert max_kappa_error < 5.0e-13
    assert abs(G1 - G2) < 3.0e-15

    print()
    print(
        "PASS: DC-normalized RF transport structurally identifies only D and "
        "Vstar=sqrt(v^2+4D kappa). Drift and recombination are exactly "
        "confounded until the DC collection spatial slope is supplied; then "
        "v,D,kappa are recovered algebraically."
    )


if __name__ == "__main__":
    main()
