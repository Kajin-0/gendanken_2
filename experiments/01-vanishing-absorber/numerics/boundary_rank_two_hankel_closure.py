"""Finite reflecting boundary as an exact rank-two spatial propagation effect.

Uniform drift-diffusion RF equation

    D u'' + w u' - s u = 0

has roots r_+,r_-. In an interior/semi-infinite downstream problem only one
physical spatial propagation mode is retained. A finite reflecting upstream
boundary u'(0)=0 generally forces both roots:

    u(z)=A exp(r_+ z)+B exp(r_- z).

Therefore responses sampled at equally spaced source coordinates form a rank-2
sequence. The three-color/rank-1 determinant generally fails, while the
five-color 3x3 Hankel determinant vanishes exactly.

A rigid translated finite-width source preserves the two spatial roots and hence
the same rank bound.
"""

from __future__ import annotations

import numpy as np


D = 0.23
W = 1.4
OMEGA = 2.3
S = 1j * OMEGA
L = 8.0
Z0 = 0.8
DZ = 0.9


def roots():
    disc = np.sqrt(W * W + 4.0 * D * S)
    r_plus = (-W + disc) / (2.0 * D)
    r_minus = (-W - disc) / (2.0 * D)
    return r_plus, r_minus


def coefficients():
    rp, rm = roots()
    # Reflecting entrance: A rp + B rm = 0 -> B=-A rp/rm.
    ratio = -rp / rm
    A = 1.0 / (np.exp(rp * L) + ratio * np.exp(rm * L))
    B = ratio * A
    return A, B


def point_response(z: float) -> complex:
    rp, rm = roots()
    A, B = coefficients()
    return complex(A * np.exp(rp * z) + B * np.exp(rm * z))


def rigid_kernel_response(zc: float) -> complex:
    # A deliberately asymmetric finite-width discrete source shape in local
    # coordinate u. Translating it only multiplies each spatial root by one
    # fixed transform factor, preserving the two-mode representation.
    u = np.asarray((-0.35, -0.08, 0.17, 0.42))
    p = np.asarray((0.15, 0.35, 0.30, 0.20))
    p /= np.sum(p)
    return complex(np.sum(p * np.asarray([point_response(zc + du) for du in u])))


def hankel(y: np.ndarray, size: int) -> np.ndarray:
    return np.asarray([[y[i + j] for j in range(size)] for i in range(size)])


def main() -> None:
    z = Z0 + DZ * np.arange(5)
    yp = np.asarray([point_response(value) for value in z])
    yk = np.asarray([rigid_kernel_response(value) for value in z])

    for name, y in (("point", yp), ("rigid finite-width", yk)):
        det2 = np.linalg.det(hankel(y, 2))
        det3 = np.linalg.det(hankel(y, 3))
        scale2 = np.linalg.norm(hankel(y, 2)) ** 2
        scale3 = np.linalg.norm(hankel(y, 3)) ** 3

        rel2 = abs(det2) / scale2
        rel3 = abs(det3) / scale3

        print(name)
        print(f"  relative 2x2/rank-1 determinant = {rel2:.9e}")
        print(f"  relative 3x3/rank-2 determinant = {rel3:.9e}")

        assert rel2 > 1.0e-7
        assert rel3 < 2.0e-14

    rp, rm = roots()
    print()
    print(f"r_plus={rp.real:.9f}+i{rp.imag:.9f}")
    print(f"r_minus={rm.real:.9f}+i{rm.imag:.9f}")
    print()
    print(
        "PASS: one reflecting boundary promotes scalar homogeneous second-order "
        "transport from a one-mode interior spatial response to an exact two-mode "
        "response. Three-color closure can fail while five-color rank-two Hankel "
        "closure remains exact, even for a rigid finite-width source."
    )


if __name__ == "__main__":
    main()
