"""Pure frequency-domain cumulant nulls for uniform drift-diffusion first passage.

Let l(omega)=ln H(omega)=m(omega)+i phi(omega), where H is the
DC-normalized successful transit-time characteristic function. Around omega=0,

    phi'(0)    = -kappa1
    m''(0)     = -kappa2
    phi'''(0)  =  kappa3
    m''''(0)   =  kappa4.

For uniform 1-D drift-diffusion first passage (inverse Gaussian),

    kappa3*kappa1/kappa2^2 = 3
    kappa4*kappa2/kappa3^2 = 5/3.

Therefore directly in RF derivatives,

    -phi'(0)*phi'''(0) / m''(0)^2 = 3
    -m''(0)*m''''(0) / phi'''(0)^2 = 5/3.

The script checks these identities analytically across several D,w,d values and
also verifies the Péclet extraction from low-frequency derivatives.
"""

from __future__ import annotations

import math


def cumulants(D: float, w: float, d: float):
    k1 = d / w
    k2 = 2.0 * D * d / w**3
    k3 = 12.0 * D**2 * d / w**5
    k4 = 120.0 * D**3 * d / w**7
    return k1, k2, k3, k4


def main() -> None:
    cases = (
        (0.20, 1.0e5, 2.0e-6),
        (0.0233, 3.4e4, 4.0e-6),
        (0.80, 2.2e5, 0.8e-6),
    )

    print("RF-derivative drift-diffusion nulls")
    for D, w, d in cases:
        k1, k2, k3, k4 = cumulants(D, w, d)

        phi1 = -k1
        m2 = -k2
        phi3 = k3
        m4 = k4

        null1 = -phi1 * phi3 / m2**2
        null2 = -m2 * m4 / phi3**2

        cv2 = -m2 / phi1**2
        pe_from_rf = 2.0 / cv2
        pe_true = w * d / D

        print(f"D={D:.6g}, w={w:.6g}, d={d:.6g}")
        print(f"  -phi1*phi3/m2^2 = {null1:.12f}")
        print(f"  -m2*m4/phi3^2   = {null2:.12f}")
        print(f"  Pe from RF derivatives = {pe_from_rf:.12f}; true Pe={pe_true:.12f}")

        assert abs(null1 - 3.0) < 2.0e-14
        assert abs(null2 - 5.0 / 3.0) < 2.0e-14
        assert abs(pe_from_rf / pe_true - 1.0) < 2.0e-14

    print()
    print(
        "PASS: the inverse-Gaussian cumulant hierarchy becomes a purely "
        "frequency-domain set of parameter-free derivative identities. A low-RF "
        "complex-response sweep can test these nulls without time-resolved "
        "single-carrier arrival measurements."
    )


if __name__ == "__main__":
    main()
