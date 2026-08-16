"""Build Paper-02 Rev. 5 from the frozen compiled Rev. 4 package.

Rev. 5 is intentionally narrow.  The Rev. 4 hostile review found one blocking
physics-semantics defect: the Poisson parameter Delta=0.05 V was described as a
literal extra terminal drop across the last 3 um, and Delta/Wd as an average
added field.  The actual solver keeps the terminal bias fixed and uses Delta as
a collector-side Poisson-curvature parameter.

This builder verifies the exact Rev. 4 Git blobs, changes only the affected
field-scale interpretation in the main manuscript and Supplemental Material,
and rejects the obsolete wording.  All theorem, finite-kernel, statistical,
convergence, bibliography, and figure content otherwise remains unchanged.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MAIN_SRC = ROOT / "PAPER02_MANUSCRIPT_REV4_ANON_2026-08-16.tex"
SUPP_SRC = ROOT / "PAPER02_SUPPLEMENT_REV4_ANON_2026-08-16.tex"
MAIN_DST = ROOT / "PAPER02_MANUSCRIPT_REV5_ANON_2026-08-16.tex"
SUPP_DST = ROOT / "PAPER02_SUPPLEMENT_REV5_ANON_2026-08-16.tex"

EXPECTED_MAIN_BLOB = "cbd5572a03cda72cd43688be949d6d9f087b0761"
EXPECTED_SUPP_BLOB = "0fa6c7b08cb06824cd5e41322af65e780fc03354"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def checked_source(path: Path, expected: str) -> str:
    data = path.read_bytes()
    observed = git_blob_sha(data)
    if observed != expected:
        raise RuntimeError(
            f"Frozen source changed for {path.name}: expected {expected}, observed {observed}"
        )
    return data.decode("utf-8")


def replace_once(text: str, old: str, new: str) -> str:
    n = text.count(old)
    if n != 1:
        raise RuntimeError(f"Expected one occurrence, found {n}: {old[:180]!r}")
    return text.replace(old, new, 1)


def guard_common(text: str, label: str) -> None:
    if text.count(r"\author{Anonymous}") != 1:
        raise RuntimeError(f"{label}: anonymity guard failed")

    forbidden_field_phrases = [
        "adds an electrostatic drop",
        "average added field of",
        "average added-field scale",
    ]
    for phrase in forbidden_field_phrases:
        if phrase.lower() in text.lower():
            raise RuntimeError(f"{label}: obsolete field wording remains: {phrase}")

    forbidden_priority = [
        r"\bfirst-ever\b",
        r"\bfor the first time\b",
        r"\bfundamental new mechanism\b",
        r"\buniversal false diffusion\b",
    ]
    for pat in forbidden_priority:
        if re.search(pat, text, flags=re.IGNORECASE):
            raise RuntimeError(f"{label}: forbidden priority wording found: {pat}")


def build_main() -> None:
    text = checked_source(MAIN_SRC, EXPECTED_MAIN_BLOB)

    old = (
        "The planar stress uses $L=7.6\\,\\mu\\mathrm{m}$ and an added electrostatic drop of "
        "$0.05\\,\\mathrm{V}$ across a $3.0\\,\\mu\\mathrm{m}$ collector-side region, "
        "corresponding to an average added field of $166.7\\,\\mathrm{V/cm}$."
    )
    new = (
        "The planar stress uses $L=7.6\\,\\mu\\mathrm{m}$, fixed terminal bias "
        "$V_{\\rm bias}=0.30\\,\\mathrm{V}$, and a collector-side Poisson-curvature region "
        "of width $W_d=3.0\\,\\mu\\mathrm{m}$ with parameter $\\Delta=0.05\\,\\mathrm{V}$, "
        "defined in the full-contact planar limit by $V''=2\\Delta/W_d^2$.  Thus "
        "$\\Delta/W_d=166.7\\,\\mathrm{V/cm}$ is a characteristic curvature-field scale, "
        "not an independently added terminal field.  With the endpoint potentials held fixed, "
        "the exact planar field magnitude spans approximately $328.9$--$662.3\\,\\mathrm{V/cm}$ "
        "across the curved region.  Its regional mean is $495.6\\,\\mathrm{V/cm}$, compared "
        "with $394.7\\,\\mathrm{V/cm}$ for the corresponding uniform-bias profile, so the "
        "mean field increment is $100.9\\,\\mathrm{V/cm}$."
    )
    text = replace_once(text, old, new)

    old_scale = (
        "These comparisons do not calibrate the conditional stress to either published detector. "
        "The optical kernels, exact field profiles, junction electrostatics, readout covariance, "
        "and excitation conditions differ. They establish only that the thickness and internal-field "
        "scales required by the theoretical counterexample are not obviously artificial for graded "
        "HgCdTe and that composition-driven fields are known to modify carrier transport on "
        "sub-nanosecond to GHz-adjacent timescales."
    )
    new_scale = (
        "These comparisons do not calibrate the conditional stress to either published detector. "
        "The optical kernels, exact field profiles, junction electrostatics, readout covariance, "
        "and excitation conditions differ.  The comparison is only one of scale: the exact mean "
        "field increment of $100.9\\,\\mathrm{V/cm}$ in the planar stress lies within the cited "
        "$100$--$200\\,\\mathrm{V/cm}$ composition-gradient range, while the modeled profile itself "
        "is not taken from the published device.  The literature therefore supports physical "
        "plausibility of the field scale, not validation of the predicted $D_{\\rm eff}$ for a real detector."
    )
    text = replace_once(text, old_scale, new_scale)

    # Positive guards for the repaired semantics.
    required = [
        r"V''=2\Delta/W_d^2",
        r"\Delta/W_d=166.7\,\mathrm{V/cm}",
        r"328.9$--$662.3\,\mathrm{V/cm}",
        r"100.9\,\mathrm{V/cm}",
        "not an independently added terminal field",
    ]
    for phrase in required:
        if phrase not in text:
            raise RuntimeError(f"Main manuscript repair missing: {phrase}")

    guard_common(text, "main")
    MAIN_DST.write_text(text, encoding="utf-8")


def build_supplement() -> None:
    text = checked_source(SUPP_SRC, EXPECTED_SUPP_BLOB)

    old = (
        "The central numerical counterexample is separate from the graded optical model above.  "
        "It solves a two-dimensional rectangular domain of lateral width $16\\,\\mu\\mathrm{m}$ "
        "and absorber thickness $L=7.6\\,\\mu\\mathrm{m}$.  The central case uses a full-width "
        "collecting contact, applied bias $V_{\\rm bias}=0.30\\,\\mathrm{V}$, and a collector-side "
        "nonuniform region of width $W_d=3.0\\,\\mu\\mathrm{m}$ with an added space-charge potential "
        "scale of $0.05\\,\\mathrm{V}$.  The corresponding average added-field scale is "
        "$166.7\\,\\mathrm{V/cm}$.  The physical electrostatic potential and the Shockley--Ramo "
        "weighting potential are solved independently."
    )
    new = r'''The central numerical counterexample is separate from the graded optical model above.  It solves a two-dimensional rectangular domain of lateral width $16\,\mu\mathrm{m}$ and absorber thickness $L=7.6\,\mu\mathrm{m}$.  The central case uses a full-width collecting contact and fixed endpoint potentials corresponding to $V_{\rm bias}=0.30\,\mathrm{V}$.  Over the collector-side region of width $W_d=3.0\,\mu\mathrm{m}$, the physical-potential solver imposes the Poisson curvature
\begin{equation}
\frac{d^2V}{dz^2}=\frac{2\Delta}{W_d^2},
\qquad \Delta=0.05\,\mathrm{V},
\end{equation}
while outside that region the planar continuum limit has $V''=0$.  The parameter $\Delta$ therefore controls curvature; it is not an independently added terminal voltage.  The characteristic curvature-field scale is $\Delta/W_d=166.7\,\mathrm{V/cm}$.

For the full-contact planar limit, let $a=L-W_d$.  The exact continuum solution consistent with $V(0)=0$ and $V(L)=V_{\rm bias}$ is
\begin{equation}
V(z)=
\begin{cases}
Az, & 0\le z<a,\\[3pt]
Az+\dfrac{\Delta}{W_d^2}(z-a)^2, & a\le z\le L,
\end{cases}
\qquad
A=\frac{V_{\rm bias}-\Delta}{L}.
\label{eq:planar-poisson}
\end{equation}
For the manuscript parameters, $A=0.0328947\,\mathrm{V/\mu m}$.  Accordingly, the electric-field magnitude across the curved region increases from $328.947$ to $662.281\,\mathrm{V/cm}$, with regional mean $495.614\,\mathrm{V/cm}$.  The corresponding uniform-bias field is $V_{\rm bias}/L=394.737\,\mathrm{V/cm}$, so the curved-region mean exceeds the uniform-bias value by $100.877\,\mathrm{V/cm}$.  The actual increase in potential drop across that $3.0\,\mu\mathrm{m}$ region relative to the uniform profile is $0.030263\,\mathrm{V}$, not $0.05\,\mathrm{V}$.  The physical electrostatic potential and the Shockley--Ramo weighting potential are solved independently.'''
    text = replace_once(text, old, new)

    required = [
        r"\frac{d^2V}{dz^2}=\frac{2\Delta}{W_d^2}",
        r"A=\frac{V_{\rm bias}-\Delta}{L}",
        r"328.947",
        r"662.281",
        r"495.614",
        r"394.737",
        r"100.877",
        r"0.030263",
        "not an independently added terminal voltage",
    ]
    for phrase in required:
        if phrase not in text:
            raise RuntimeError(f"Supplement repair missing: {phrase}")

    guard_common(text, "supplement")
    SUPP_DST.write_text(text, encoding="utf-8")


def main() -> None:
    build_main()
    build_supplement()
    print(MAIN_DST)
    print(SUPP_DST)


if __name__ == "__main__":
    main()
