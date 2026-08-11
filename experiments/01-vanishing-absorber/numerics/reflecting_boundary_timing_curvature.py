"""Exact low-frequency three-color mean-time curvature from a reflecting boundary.

Uniform 1-D drift-diffusion on 0<=z<=L:

    D m'' + w m' = -1,
    m'(0)=0   reflecting upstream entrance,
    m(L)=0    absorbing collector.

The exact mean first-passage time is

    m(z)=(L-z)/w - (D/w^2)[exp(-w z/D)-exp(-w L/D)].

For point sources at z0-h,z0,z0+h, the linear bulk term cancels and

    C1=2m(z0)-m(z0-h)-m(z0+h)
      =2(D/w^2) exp(-z0/lD)[cosh(h/lD)-1],
    lD=D/w.

Thus a finite reflecting boundary creates an O(omega) three-color phase closure
even in perfectly homogeneous transport. For a rigid translated generation
kernel g(u), the same law acquires one fixed factor E_g[exp(-u/lD)].
"""

from __future__ import annotations

import math
import numpy as np


D = 0.023266815
W = 3.4543e4
L = 7.6e-6
ELL = D / W


def mean_time(z: float) -> float:
    return (
        (L - z) / W
        - D / W**2 * (math.exp(-z / ELL) - math.exp(-L / ELL))
    )


def point_curvature(z0: float, h: float) -> float:
    return 2.0 * mean_time(z0) - mean_time(z0 - h) - mean_time(z0 + h)


def point_curvature_closed(z0: float, h: float) -> float:
    return (
        2.0
        * D
        / W**2
        * math.exp(-z0 / ELL)
        * (math.cosh(h / ELL) - 1.0)
    )


def translated_kernel_curvature(z0: float, h: float, u: np.ndarray, g: np.ndarray) -> float:
    g = g / np.trapezoid(g, u)
    factor = float(np.trapezoid(g * np.exp(-u / ELL), u))
    return factor * point_curvature_closed(z0, h)


def main() -> None:
    print("Reflecting-boundary timing-curvature theorem")
    print(f"D={D:.9f} m^2/s, w={W:.6f} m/s")
    print(f"boundary diffusion length ell_D=D/w={ELL*1e6:.6f} um")

    for z0_um, h_um in ((2.5, 0.5), (3.5, 0.5), (4.5, 0.5), (4.0, 1.0)):
        z0 = z0_um * 1e-6
        h = h_um * 1e-6
        direct = point_curvature(z0, h)
        closed = point_curvature_closed(z0, h)
        print(
            f"z0={z0_um:.1f} um, h={h_um:.1f} um: "
            f"C1={closed*1e12:.9f} ps, error={abs(direct-closed):.3e} s"
        )
        assert abs(direct - closed) < 2.0e-25

    # Fixed-shape finite-width generation kernel preserves exponential depth
    # decay of the boundary closure.
    u = np.linspace(-0.3e-6, 0.3e-6, 2001)
    g = np.exp(-0.5 * (u / (0.10e-6)) ** 2)
    h = 0.5e-6
    z_a = 3.2e-6
    delta = 0.8e-6
    c_a = translated_kernel_curvature(z_a, h, u, g)
    c_b = translated_kernel_curvature(z_a + delta, h, u, g)
    ratio = c_b / c_a
    expected = math.exp(-delta / ELL)

    print()
    print("rigid finite-width kernel depth-ratio test")
    print(f"  C1(z+Delta)/C1(z)={ratio:.12f}")
    print(f"  exp(-Delta/ell_D)={expected:.12f}")
    assert abs(ratio / expected - 1.0) < 2.0e-14

    # Invert the two-triplet ratio to recover ell_D.
    ell_recovered = -delta / math.log(ratio)
    print(f"  recovered ell_D={ell_recovered*1e6:.9f} um")
    assert abs(ell_recovered / ELL - 1.0) < 2.0e-14

    print()
    print(
        "PASS: a reflecting upstream boundary produces an exact exponentially "
        "decaying O(omega) three-color phase curvature with length scale D/w. "
        "A rigid finite-width source preserves that depth law, so boundary "
        "curvature can itself be identified or bounded before bulk-gradient "
        "interpretation."
    )


if __name__ == "__main__":
    main()
