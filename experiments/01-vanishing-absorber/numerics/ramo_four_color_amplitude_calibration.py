"""Low-RF spectral amplitude-calibration rejection of the four-color closure.

At DC / sufficiently low RF for a one-carrier planar detector without loss,
raw current is affine in internal source coordinate:

    J_m = A + B m

for equally spaced channels m=0..3.  Suppose imperfect per-channel generated-
carrier / external-gain calibration leaves a small multiplicative error

    Jtilde_m = (1+eps_m) J_m.

For

    C4=2 log Delta J1 - log Delta J0 - log Delta J2,

the first variation is

    delta C4 = - Delta^3(eps_m J_m) / B.

Therefore constant or linear eps_m gives exactly zero first-order closure error.
A quadratic eps_m=c2 m^2 gives delta C4=-6 c2.

For smooth coordinate z with spacing h and local affine J(z),

    delta C4 ~= -h^2 [3 eps'' + (J/G) eps''']

where G=dJ/dz, evaluated locally.  The script verifies the finite-difference
identity and the expected small-error scaling against the exact logarithmic
closure.
"""

from __future__ import annotations

import numpy as np


A = 5.1
B = -0.5
M = np.arange(4, dtype=float)
J = A + B * M


def closure(values: np.ndarray) -> complex:
    d = np.diff(values.astype(complex))
    return complex(2.0 * np.log(d[1]) - np.log(d[0]) - np.log(d[2]))


def third_difference(values: np.ndarray) -> float:
    return float(values[3] - 3.0 * values[2] + 3.0 * values[1] - values[0])


def first_order(eps: np.ndarray) -> float:
    return -third_difference(eps * J) / B


def main() -> None:
    print("Four-color multiplicative amplitude-calibration rejection")
    C0 = closure(J)
    assert abs(C0) < 2.0e-14

    shapes = {
        "constant": 2.0e-4 + 0.0 * M,
        "linear": 1.0e-4 + 3.0e-5 * M,
        "quadratic": 2.0e-5 * M**2,
        "cubic": 3.0e-6 * M**3,
    }

    scale = 1.0e-3
    for name, shape in shapes.items():
        eps = scale * shape
        exact = closure((1.0 + eps) * J) - C0
        linear = first_order(eps)
        print(
            f"{name:9s}: exact={exact.real:+.6e}{exact.imag:+.2e}j, "
            f"first-order={linear:+.6e}"
        )

        if name in ("constant", "linear"):
            assert abs(linear) < 1.0e-15
            assert abs(exact) < 2.0e-12
        else:
            assert abs((exact.real - linear) / linear) < 2.0e-5

    # Quadratic eps=c2 m^2 gives exact first-order coefficient -6 c2.
    c2 = 1.7e-6
    eps_q = c2 * M**2
    assert abs(first_order(eps_q) + 6.0 * c2) < 1.0e-14

    # Smooth-coordinate formula test on exact polynomials.
    h = 0.4
    z0 = 1.2
    z = z0 + h * M
    Jz0 = 4.7
    G = -0.8
    Jz = Jz0 + G * (z - z0)
    e0, e1, e2, e3 = 0.01, -0.02, 0.004, 0.0015
    epsz = e0 + e1 * z + 0.5 * e2 * z**2 + e3 * z**3 / 6.0
    Bz = G * h
    discrete = -third_difference(epsz * Jz) / Bz
    # For cubic eps and affine J, fourth-degree eps*J has an O(h^3) correction;
    # compare only asymptotically by reducing h.
    hs = np.asarray((0.1, 0.05, 0.025, 0.0125))
    errors = []
    for hh in hs:
        zz = z0 + hh * M
        JJ = Jz0 + G * (zz - z0)
        ee = e0 + e1 * zz + 0.5 * e2 * zz**2 + e3 * zz**3 / 6.0
        disc = -third_difference(ee * JJ) / (G * hh)
        center = z0 + 1.5 * hh
        eps2 = e2 + e3 * center
        eps3 = e3
        Jcenter = Jz0 + G * (center - z0)
        smooth = -hh**2 * (3.0 * eps2 + (Jcenter / G) * eps3)
        errors.append(abs(disc - smooth))
    assert errors[-1] < errors[0] / 50.0

    print()
    print(
        "PASS: in the affine-current low-RF limit, four-color closure rejects "
        "common and linearly varying multiplicative spectral calibration error "
        "to first order.  The leading smooth contamination is calibration "
        "curvature, not absolute gain error."
    )


if __name__ == "__main__":
    main()
