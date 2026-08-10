"""Three-frequency parameter-free closure for conditioned drift-diffusion.

For a DC-normalized first-passage field F(z,omega), define

    r = d_z ln F,
    A = r' + r^2.

A local 1-D Markov drift-diffusion generator with real D(z),w(z) requires

    D A + w r = i omega

at every frequency. Therefore

    Y = i omega/r = D X + w,  X=A/r,

and any three frequencies satisfy

    det[[A_j, r_j, i omega_j]] = 0.

This regression constructs exact local roots for a uniform conditioned process
and compares them to a deliberately frequency-dependent diffusion law, which
violates the common-coefficient closure.
"""

from __future__ import annotations

import numpy as np


D0 = 0.08
W0 = 1.55
FREQUENCIES = np.array((0.7, 1.4, 2.8, 5.0))


def root(D: complex, w: complex, omega: float) -> complex:
    return (np.sqrt(w * w + 4j * D * omega) - w) / (2.0 * D)


def closure_determinant(r: np.ndarray, A: np.ndarray) -> complex:
    matrix = np.column_stack((A[:3], r[:3], 1j * FREQUENCIES[:3]))
    return complex(np.linalg.det(matrix))


def fit_real_D_w(r: np.ndarray, A: np.ndarray):
    # Stack real and imaginary equations for all frequencies.
    M = np.vstack(
        (
            np.column_stack((np.real(A), np.real(r))),
            np.column_stack((np.imag(A), np.imag(r))),
        )
    )
    b = np.concatenate((np.zeros_like(FREQUENCIES), FREQUENCIES))
    pars, _, _, _ = np.linalg.lstsq(M, b, rcond=None)
    residual = M @ pars - b
    return pars, float(np.linalg.norm(residual) / np.linalg.norm(b))


def main() -> None:
    # Exact local Markov model: uniform implies r'=0, hence A=r^2.
    r_good = np.asarray([root(D0, W0, omega) for omega in FREQUENCIES])
    A_good = r_good**2
    det_good = closure_determinant(r_good, A_good)
    pars_good, residual_good = fit_real_D_w(r_good, A_good)

    X = A_good / r_good
    Y = 1j * FREQUENCIES / r_good
    affine_error = np.max(np.abs(Y - (D0 * X + W0)))

    # Deliberate memory-like violation: each frequency sees a different real
    # effective diffusion coefficient. No single D,w can close all frequencies.
    D_bad = D0 * (1.0 + 0.09 * FREQUENCIES / FREQUENCIES[-1])
    r_bad = np.asarray(
        [root(Di, W0, omega) for Di, omega in zip(D_bad, FREQUENCIES)]
    )
    A_bad = r_bad**2
    det_bad = closure_determinant(r_bad, A_bad)
    _, residual_bad = fit_real_D_w(r_bad, A_bad)

    print("Three-frequency conditioned drift-diffusion closure")
    print(f"exact-model |3-frequency determinant| = {abs(det_good):.3e}")
    print(
        "exact-model recovered D,w = "
        f"{pars_good[0]:.12f}, {pars_good[1]:.12f}"
    )
    print(f"exact-model relative stacked residual = {residual_good:.3e}")
    print(f"exact-model affine-line max error = {affine_error:.3e}")
    print(f"frequency-dependent-D |determinant| = {abs(det_bad):.3e}")
    print(f"frequency-dependent-D relative stacked residual = {residual_bad:.3e}")

    assert abs(det_good) < 2.0e-14
    assert abs(pars_good[0] / D0 - 1.0) < 2.0e-14
    assert abs(pars_good[1] / W0 - 1.0) < 2.0e-14
    assert residual_good < 2.0e-14
    assert affine_error < 2.0e-14
    assert abs(det_bad) > 1.0e-5
    assert residual_bad > 1.0e-3

    print()
    print(
        "PASS: three RF frequencies satisfy an exact coefficient-free closure "
        "for one local Markov drift-diffusion process, while a modest explicit "
        "frequency dependence of the transport coefficient breaks the closure."
    )


if __name__ == "__main__":
    main()
