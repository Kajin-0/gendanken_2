"""Exact real-coefficient closure hierarchy for local conditioned drift-diffusion.

At one depth z, a DC-normalized local 1-D Markov drift-diffusion field obeys

    D A_omega + w r_omega = i omega,

where

    r_omega = d_z ln F_omega,
    A_omega = r_omega' + r_omega^2 = F_omega''/F_omega,

and D(z), w(z) are REAL and frequency independent.

Writing real/imaginary parts gives a 2x2 real system at every frequency. If

    delta_omega = Re(A) Im(r) - Im(A) Re(r) != 0,

then that one frequency defines the apparent real coefficients

    D_app(omega) = -omega Re(r)/delta,
    w_app(omega) =  omega Re(A)/delta.

Therefore, for a set of frequencies with nonzero delta, existence of one local
real second-order Markov drift-diffusion generator is equivalent to BOTH
D_app and w_app being independent of frequency.

A previously used three-frequency complex determinant

    det[[A_j, r_j, i omega_j]] = 0

is necessary but NOT sufficient: it also accepts common complex coefficients.
This regression verifies the stronger iff closure and gives an explicit
counterexample to determinant sufficiency.
"""

from __future__ import annotations

import numpy as np


D0 = 0.08
W0 = 1.55
FREQUENCIES = np.asarray((0.7, 1.4, 2.8, 5.0), dtype=float)


def root(D: complex, w: complex, omega: float) -> complex:
    """Uniform spatial root continuously connected to zero as omega -> 0."""
    return (np.sqrt(w * w + 4j * D * omega) - w) / (2.0 * D)


def apparent_real_coefficients(r: complex, A: complex, omega: float):
    delta = A.real * r.imag - A.imag * r.real
    if abs(delta) < 1.0e-16:
        raise RuntimeError("single-frequency local inversion is singular")
    D_app = -omega * r.real / delta
    w_app = omega * A.real / delta
    return float(D_app), float(w_app), float(delta)


def complex_determinant(r: np.ndarray, A: np.ndarray) -> complex:
    matrix = np.column_stack((A[:3], r[:3], 1j * FREQUENCIES[:3]))
    return complex(np.linalg.det(matrix))


def pairwise_parameter_free_residuals(
    D_app: np.ndarray,
    w_app: np.ndarray,
):
    return (
        D_app[1:] - D_app[0],
        w_app[1:] - w_app[0],
    )


def main() -> None:
    # Exact physical model.
    r_good = np.asarray([root(D0, W0, om) for om in FREQUENCIES])
    A_good = r_good**2
    apparent_good = np.asarray(
        [
            apparent_real_coefficients(r, A, om)[:2]
            for r, A, om in zip(r_good, A_good, FREQUENCIES)
        ]
    )
    dD_good, dw_good = pairwise_parameter_free_residuals(
        apparent_good[:, 0], apparent_good[:, 1]
    )
    det_good = complex_determinant(r_good, A_good)

    # Counterexample: one pair of COMMON COMPLEX coefficients. The complex
    # determinant still vanishes, but no common REAL D,w exist.
    D_complex = D0 * (1.0 + 0.20j)
    w_complex = W0 * (1.0 - 0.10j)
    r_complex = np.asarray(
        [root(D_complex, w_complex, om) for om in FREQUENCIES]
    )
    A_complex = r_complex**2
    apparent_complex = np.asarray(
        [
            apparent_real_coefficients(r, A, om)[:2]
            for r, A, om in zip(r_complex, A_complex, FREQUENCIES)
        ]
    )
    det_complex = complex_determinant(r_complex, A_complex)

    # Explicit dispersive diffusion coefficient: determinant and the stronger
    # closure both fail.
    D_disp = D0 * (1.0 + 0.09 * FREQUENCIES / FREQUENCIES[-1])
    r_disp = np.asarray(
        [root(Di, W0, om) for Di, om in zip(D_disp, FREQUENCIES)]
    )
    A_disp = r_disp**2
    apparent_disp = np.asarray(
        [
            apparent_real_coefficients(r, A, om)[:2]
            for r, A, om in zip(r_disp, A_disp, FREQUENCIES)
        ]
    )

    print("Exact real-coefficient local Markov closure hierarchy")
    print(f"exact-model |complex 3-frequency det| = {abs(det_good):.3e}")
    print(
        "exact-model max |D_app-D0|, |w_app-W0| = "
        f"{np.max(np.abs(apparent_good[:,0]-D0)):.3e}, "
        f"{np.max(np.abs(apparent_good[:,1]-W0)):.3e}"
    )
    print(
        "exact-model max pairwise real-closure residual = "
        f"{max(np.max(np.abs(dD_good)), np.max(np.abs(dw_good))):.3e}"
    )
    print()

    print("complex-coefficient determinant counterexample")
    print(f"  |complex 3-frequency det| = {abs(det_complex):.3e}")
    print(
        "  apparent-real D range = "
        f"{np.ptp(apparent_complex[:,0]):.6f}"
    )
    print(
        "  apparent-real w range = "
        f"{np.ptp(apparent_complex[:,1]):.6f}"
    )
    print()

    print("frequency-dependent real diffusion counterexample")
    print(
        "  D_app = "
        + ", ".join(f"{x:.6f}" for x in apparent_disp[:,0])
    )
    print(
        "  w_app = "
        + ", ".join(f"{x:.6f}" for x in apparent_disp[:,1])
    )

    assert abs(det_good) < 2.0e-14
    assert np.max(np.abs(apparent_good[:, 0] - D0)) < 2.0e-12
    assert np.max(np.abs(apparent_good[:, 1] - W0)) < 2.0e-12

    # Determinant can be essentially zero while physical real closure fails.
    assert abs(det_complex) < 3.0e-14
    assert np.ptp(apparent_complex[:, 0]) > 0.25
    assert np.ptp(apparent_complex[:, 1]) > 0.02

    assert np.allclose(apparent_disp[:, 0], D_disp, rtol=0.0, atol=2.0e-12)
    assert np.max(np.abs(apparent_disp[:, 1] - W0)) < 2.0e-12

    print()
    print(
        "PASS: frequency-independence of the per-frequency REAL apparent "
        "coefficients is the exact iff closure (away from delta=0). The compact "
        "three-frequency complex determinant is only a necessary diagnostic."
    )


if __name__ == "__main__":
    main()
