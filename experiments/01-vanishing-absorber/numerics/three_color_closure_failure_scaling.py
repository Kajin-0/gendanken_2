"""Low-RF scaling of two distinct three-color closure failures.

Define the complex equal-spacing closure

    L = 2 ln H_2 - ln H_1 - ln H_3.

Case A: uniform transport, generation kernels centered at equal mean depths but
with smoothly changing shape. For centered Gaussian kernels,

    ln H_j = Gamma mu_j + Gamma^2 sigma_j^2/2.

The linear mean-depth term cancels, so optical shape evolution starts at
O(Gamma^2) ~ O(omega^2), primarily in the real/log-magnitude component.

Case B: point generation but spatially varying local conditioned drift. Then

    ln H(z)=int^z Gamma(u,omega) du,

and equal-spacing closure is

    L = -h^2 d_z Gamma + O(h^4).

At low RF Gamma~i omega/w, so transport inhomogeneity begins at O(omega),
primarily phase-like.

The script verifies both asymptotic scalings numerically.
"""

from __future__ import annotations

import numpy as np


H = 0.40
CENTERS = np.asarray((-H, 0.0, H))
D0 = 0.08
W0 = 1.70


def gamma_uniform(omega: float) -> complex:
    return (np.sqrt(W0 * W0 + 4j * D0 * omega) - W0) / (2.0 * D0)


def optical_closure(omega: float) -> complex:
    # Smooth variance curvature across equally spaced mean generation depths.
    sigma0_sq = 0.09
    variance_curvature = 0.25
    variances = sigma0_sq + variance_curvature * CENTERS**2
    Gamma = gamma_uniform(omega)

    # Exact centered-Gaussian moment transform.
    lnH = Gamma * CENTERS + 0.5 * Gamma**2 * variances
    return complex(2.0 * lnH[1] - lnH[0] - lnH[2])


def local_gamma(z: np.ndarray, omega: float) -> np.ndarray:
    # Deliberately smooth spatially varying conditioned drift.
    epsilon = 0.20
    w = W0 * (1.0 + epsilon * z)
    return (np.sqrt(w * w + 4j * D0 * omega) - w) / (2.0 * D0)


def propagation_log(z: float, omega: float) -> complex:
    grid = np.linspace(0.0, z, 5001)
    return complex(np.trapezoid(local_gamma(grid, omega), grid))


def transport_closure(omega: float) -> complex:
    lnH = np.asarray([propagation_log(z, omega) for z in CENTERS])
    return complex(2.0 * lnH[1] - lnH[0] - lnH[2])


def main() -> None:
    omegas = np.asarray((1.0e-3, 2.0e-3, 5.0e-3, 1.0e-2))

    opt_real_scaled = []
    opt_imag_scaled = []
    tr_imag_scaled = []
    tr_real_scaled = []

    print("Three-color closure failure scaling")
    for omega in omegas:
        Lopt = optical_closure(float(omega))
        Ltr = transport_closure(float(omega))

        opt_real_scaled.append(Lopt.real / omega**2)
        opt_imag_scaled.append(Lopt.imag / omega**3)
        tr_imag_scaled.append(Ltr.imag / omega)
        tr_real_scaled.append(Ltr.real / omega**2)

        print(
            f"omega={omega:.4g}: "
            f"L_opt={Lopt.real:.3e}+i{Lopt.imag:.3e}, "
            f"L_tr={Ltr.real:.3e}+i{Ltr.imag:.3e}"
        )

    opt_real_scaled = np.asarray(opt_real_scaled)
    opt_imag_scaled = np.asarray(opt_imag_scaled)
    tr_imag_scaled = np.asarray(tr_imag_scaled)
    tr_real_scaled = np.asarray(tr_real_scaled)

    # The scaled coefficients should approach constants across this low-RF set.
    assert np.ptp(opt_real_scaled) / abs(np.mean(opt_real_scaled)) < 1.0e-6
    assert np.ptp(opt_imag_scaled) / abs(np.mean(opt_imag_scaled)) < 1.0e-6
    assert np.ptp(tr_imag_scaled) / abs(np.mean(tr_imag_scaled)) < 1.0e-6
    assert np.ptp(tr_real_scaled) / abs(np.mean(tr_real_scaled)) < 1.0e-6

    print()
    print(
        "optical shape evolution: Re(L)/omega^2 -> "
        f"{np.mean(opt_real_scaled):.9f}; "
        "Im(L)/omega^3 -> "
        f"{np.mean(opt_imag_scaled):.9f}"
    )
    print(
        "transport inhomogeneity: Im(L)/omega -> "
        f"{np.mean(tr_imag_scaled):.9f}; "
        "Re(L)/omega^2 -> "
        f"{np.mean(tr_real_scaled):.9f}"
    )

    print()
    print(
        "PASS: after centering each generation kernel at its mean depth, smooth "
        "optical shape evolution first contaminates three-color closure at "
        "O(omega^2) in log magnitude, whereas spatial drift variation creates "
        "an O(omega) phase closure residual. RF scaling therefore separates the "
        "leading optical and transport failure channels in the stated limit."
    )


if __name__ == "__main__":
    main()
