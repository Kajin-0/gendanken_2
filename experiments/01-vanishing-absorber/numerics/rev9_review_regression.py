#!/usr/bin/env python3
"""Revision 9 adversarial-review regression checks."""
from __future__ import annotations
import cmath
import math
import numpy as np

def hankel_det(d):
    H=np.array([[d[0],d[1],d[2]],[d[1],d[2],d[3]],[d[2],d[3],d[4]]],dtype=complex)
    return np.linalg.det(H)

def minors(d):
    return [d[m]*d[m+2]-d[m+1]**2 for m in range(3)]

# 1. Confluent rank-two branch.
A=0.8-0.3j
B=0.21+0.17j
q=0.74+0.11j
d=np.array([(A+B*m)*q**m for m in range(5)],dtype=complex)
W=minors(d)
assert abs(hankel_det(d)) < 2e-14
for m,w in enumerate(W):
    want=-(B**2)*q**(2*m+2)
    assert abs(w-want) < 2e-14
P=W[1]/W[0]
S=(d[2]+P*d[0])/d[1]
disc=S*S-4*P
assert abs(P-q*q) < 2e-14
assert abs(S-2*q) < 2e-14
assert abs(disc) < 5e-14
assert abs(W[0]) > 1e-4

# Rank-one determinant gradient degeneracy.
a=0.7+0.2j
qr=0.83-0.04j
dr=np.array([a*qr**m for m in range(5)],dtype=complex)
g=np.array([
    dr[2]*dr[4]-dr[3]**2,
    2*(dr[2]*dr[3]-dr[1]*dr[4]),
    dr[0]*dr[4]+2*dr[1]*dr[3]-3*dr[2]**2,
    2*(dr[1]*dr[2]-dr[0]*dr[3]),
    dr[0]*dr[2]-dr[1]**2
])
assert np.max(np.abs(g)) < 2e-14

# 2. Common coordinate-scale transformation.
D=0.02327
w=2.22e4
kappa=2.0e5
omega=2*math.pi*5e8
gamma=(-w+cmath.sqrt(w*w+4*D*(kappa+1j*omega)))/(2*D)
for c in (0.98,1.02,1.13):
    gc=gamma/c
    Dc=c*c*D
    wc=c*w
    kc=kappa
    lhs=Dc*gc*gc+wc*gc
    assert abs(lhs-(kc+1j*omega)) < 5e-7*abs(kc+1j*omega)

# 3. Known-arbitrary-kernel one-mode null.
# Gaussian kernels with deliberately changing widths: not rigid translations.
mus=np.array([2.45,2.98,3.52,4.03])*1e-6
sig=np.array([0.31,0.36,0.42,0.49])*1e-6
r=(-1.7e5+2.4e4j)
M=np.exp(r*mus+0.5*(r*sig)**2)
A0=0.31-0.08j
B0=1.7+0.22j
J=A0+B0*M
R012=(J[1]-J[0])*(M[2]-M[0])-(J[2]-J[0])*(M[1]-M[0])
R013=(J[1]-J[0])*(M[3]-M[0])-(J[3]-J[0])*(M[1]-M[0])
assert abs(R012) < 2e-15
assert abs(R013) < 2e-15
# Simple geometric closure should not generally vanish for evolving kernels.
dJ=np.diff(J)
geom=dJ[1]**2-dJ[0]*dJ[2]
assert abs(geom) > 1e-5
# Perturb one channel and the kernel-aware fourth-channel residual must respond.
Jbad=J.copy(); Jbad[3]+=2e-3*(1+0.3j)
Rbad=(Jbad[1]-Jbad[0])*(M[3]-M[0])-(Jbad[3]-Jbad[0])*(M[1]-M[0])
assert abs(Rbad) > 1e-5

# 4. Peclet scales quoted in Rev. 9.
v=2.22e4
Dpe=0.02327
pe_h=v*0.5e-6/Dpe
pe_k=v*0.79e-6/Dpe
assert abs(pe_h-0.47658) < 5e-4
assert abs(pe_k-0.75299) < 7e-4

# 5. DC physical-admissibility null.
for D0,w0,k0,h in [(0.02,2e4,0.0,0.5e-6),(0.02,2e4,1e6,0.5e-6),(0.03,1e4,5e5,1e-6)]:
    g0=(math.sqrt(w0*w0+4*D0*k0)-w0)/(2*D0)
    q0=math.exp(-g0*h)
    assert g0 >= 0
    assert 0 < q0 <= 1.0

print("Revision 9 adversarial-review regression")
print(f"confluent: det(H)={hankel_det(d):.3e}, P-q^2={P-q*q:.3e}, S-2q={S-2*q:.3e}, discriminant={disc:.3e}")
print(f"rank-one determinant gradient max={np.max(np.abs(g)):.3e}")
print("common-scale law: D_cal=c^2 D, w_cal=c w, kappa_cal=kappa verified")
print(f"kernel-aware residuals: |R012|={abs(R012):.3e}, |R013|={abs(R013):.3e}, geometric failure={abs(geom):.3e}, perturbed |R013|={abs(Rbad):.3e}")
print(f"Peclet scales: Pe_h={pe_h:.4f}, Pe_kernel={pe_k:.4f}")
print("DC admissibility: q(0) in (0,1] verified")
print("PASS: Rev9 confluent rank, scale calibration, kernel-aware null, Peclet, and DC-admissibility checks verified.")
