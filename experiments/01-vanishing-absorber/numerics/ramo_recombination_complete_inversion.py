"""Observable-corrected complete inversion of uniform DD + recombination.

For homogeneous one-dimensional drift-diffusion with diffusion D>0, downstream
drift w>0, and independent Markov killing/recombination rate kappa>=0,

    D gamma(s)^2 + w gamma(s) = kappa + s.

In the uniform planar Shockley-Ramo geometry, raw current remains

    J(d,s)=C(s)[1-exp(-gamma(s)d)],

so four equally spaced source coordinates recover gamma(s) from first
differences at DC and RF.

Let g0=gamma(0) and g=gamma(i omega).  Subtract the two dispersion relations:

    D (g^2-g0^2) + w (g-g0) = i omega.

With A=g^2-g0^2, B=g-g0, and real D,w,

    delta = Re(A) Im(B) - Im(A) Re(B)
    D = -omega Re(B)/delta
    w =  omega Re(A)/delta
    kappa = D g0^2 + w g0.

Thus DC spatial propagation + one RF frequency identifies D,w,kappa exactly
in noiseless nonsingular data; a second RF frequency adds no parameter and is
a pure falsification point.
"""

from __future__ import annotations

import numpy as np


D_TRUE = 0.12
W_TRUE = 1.70
KAPPA_TRUE = 0.45
OMEGAS = (0.8, 2.3, 5.1)
DELTA_Z = 0.27
Z0 = 0.40
DEPTHS = Z0 + DELTA_Z * np.arange(4)


def gamma(s: complex) -> complex:
    return (
        np.sqrt(W_TRUE * W_TRUE + 4.0 * D_TRUE * (KAPPA_TRUE + s))
        - W_TRUE
    ) / (2.0 * D_TRUE)


def raw_current(depths: np.ndarray, s: complex) -> np.ndarray:
    g = gamma(s)
    # Any nonzero depth-independent complex prefactor is allowed.
    prefactor = (1.2 - 0.3j) * (1.0 + 0.07 * s)
    offset = 0.11 + 0.04j
    return prefactor * (1.0 - np.exp(-g * depths)) + offset


def recover_gamma(currents: np.ndarray) -> complex:
    d = np.diff(currents)
    q = d[1] / d[0]
    return -np.log(q) / DELTA_Z


def invert(g0: complex, gw: complex, omega: float):
    A = gw * gw - g0 * g0
    B = gw - g0
    delta = A.real * B.imag - A.imag * B.real
    D = -omega * B.real / delta
    w = omega * A.real / delta
    kappa = D * g0 * g0 + w * g0
    return D, w, kappa, delta


def main() -> None:
    g0 = recover_gamma(raw_current(DEPTHS, 0.0))
    print("DC + one-RF raw-Ramo drift-diffusion-recombination inversion")
    print(f"recovered gamma0 = {g0.real:.12f}{g0.imag:+.3e}j")

    max_D_rel = 0.0
    max_w_rel = 0.0
    max_k_rel = 0.0

    for omega in OMEGAS:
        gw = recover_gamma(raw_current(DEPTHS, 1j * omega))
        D, w, kappa, delta = invert(g0, gw, omega)
        max_D_rel = max(max_D_rel, abs(D / D_TRUE - 1.0))
        max_w_rel = max(max_w_rel, abs(w / W_TRUE - 1.0))
        max_k_rel = max(max_k_rel, abs(kappa.real / KAPPA_TRUE - 1.0))

        print(
            f"omega={omega:.2f}: D={D:.12f}, w={w:.12f}, "
            f"kappa={kappa.real:.12f}{kappa.imag:+.3e}j, delta={delta:.6e}"
        )

        assert abs(kappa.imag) < 2.0e-12
        assert abs(delta) > 1.0e-5

    assert max_D_rel < 2.0e-11
    assert max_w_rel < 2.0e-11
    assert max_k_rel < 2.0e-11

    print()
    print(
        "PASS: four-color raw-current spatial exponents at DC plus one RF "
        "frequency exactly identify uniform D, drift, and Markov recombination. "
        "Every additional RF frequency is overdetermined and therefore a pure "
        "model-closure test."
    )


if __name__ == "__main__":
    main()
