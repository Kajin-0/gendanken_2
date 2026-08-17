"""Submission-facing cleanup for the unpromoted Paper 02 Rev. 8 supplement.

This is intentionally narrow: it removes internal CI/run-history prose that is
preserved in repository provenance but should not appear in the submitted
Supplemental Material. It does not alter equations, numerical results, figures,
claims, references, or the main manuscript.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "PAPER02_SUPPLEMENT_REV8_ANON_2026-08-16.tex"

text = P.read_text()

old_history = (
    "The checked workflows are: covariance run 31953328287; kernel-misspecification run 31953612225; exact-affine "
    "run 31953979410; frequency-aware local nuisance projection run 31954048251; and signed-mode threshold run "
    "31954087223. The frequency-aware ``v2'' nuisance projection supersedes only the higher-frequency diffusion-derivative "
    "fields of its first version, which had inherited a 100-MHz-fixed angular frequency from a validation helper; the first "
    "version's 100-MHz row and channel-space tangent/normal projection were unaffected.\n\n"
)
if text.count(old_history) != 1:
    raise RuntimeError(f"internal-history paragraph count={text.count(old_history)}")
text = text.replace(old_history, "", 1)

old_primary = (
    "The full-contact central case admits an exact calculation that eliminates the two-dimensional electrostatic mesh. "
    "Historically it was introduced after the original mesh-refinement study; in this revision it is the primary full-contact "
    "planar result because it removes discretization of electrostatics and trajectories."
)
new_primary = (
    "The full-contact central case admits an exact calculation that eliminates the two-dimensional electrostatic mesh. "
    "It is the primary full-contact planar result because it removes discretization of electrostatics and trajectories."
)
if text.count(old_primary) != 1:
    raise RuntimeError(f"primary-result history sentence count={text.count(old_primary)}")
text = text.replace(old_primary, new_primary, 1)

for forbidden in (
    "31953328287", "31953612225", "31953979410", "31954048251", "31954087223",
    "validation helper", "Historically it was introduced",
):
    if forbidden in text:
        raise RuntimeError(f"submission-facing internal history remains: {forbidden}")

P.write_text(text)
print(f"cleaned {P.name}")
