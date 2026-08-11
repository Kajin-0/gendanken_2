#!/usr/bin/env python3
"""Fail on accidental destructive rewrites of the photodetector manuscript.

This is intentionally conservative. It is a guardrail against incidental manuscript
replacement while integrating new science, not a prohibition on deliberate editorial
work explicitly requested by the user.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

SECTION_RE = re.compile(r"\\section\{([^}]*)\}")
SUBSECTION_RE = re.compile(r"\\subsection\{([^}]*)\}")
TITLE_RE = re.compile(r"\\title\{([^}]*)\}")
AUTHOR_RE = re.compile(r"\\author\{([^}]*)\}")
BIBITEM_RE = re.compile(r"\\bibitem(?:\[[^]]*\])?\{[^}]+\}")
EQUATION_RE = re.compile(r"\\begin\{equation\}")


@dataclass
class Metrics:
    path: str
    sha256: str
    bytes: int
    lines: int
    title: str | None
    author: str | None
    sections: list[str]
    subsections: list[str]
    bibliography_items: int
    equation_environments: int


def read_metrics(path: Path) -> tuple[str, Metrics]:
    text = path.read_text(encoding="utf-8")
    raw = text.encode("utf-8")
    title = TITLE_RE.search(text)
    author = AUTHOR_RE.search(text)
    return text, Metrics(
        path=str(path),
        sha256=hashlib.sha256(raw).hexdigest(),
        bytes=len(raw),
        lines=len(text.splitlines()),
        title=title.group(1).strip() if title else None,
        author=author.group(1).strip() if author else None,
        sections=SECTION_RE.findall(text),
        subsections=SUBSECTION_RE.findall(text),
        bibliography_items=len(BIBITEM_RE.findall(text)),
        equation_environments=len(EQUATION_RE.findall(text)),
    )


def destructive_override(path: Path | None) -> tuple[bool, str]:
    if not path or not path.exists():
        return False, ""
    text = path.read_text(encoding="utf-8")
    flag = re.search(
        r"^USER_EXPLICITLY_REQUESTED_LARGE_REWRITE:\s*true\s*$",
        text,
        re.M | re.I,
    )
    quote = re.search(r"^USER_REQUEST_QUOTE:\s*(.+?)\s*$", text, re.M)
    placeholder = "<verbatim user instruction authorizing compression/restructuring>"
    if flag and quote and quote.group(1).strip() and quote.group(1).strip() != placeholder:
        return True, quote.group(1).strip()
    return False, ""


def replacement_fraction(base_text: str, candidate_text: str) -> float:
    base = [line.rstrip() for line in base_text.splitlines() if line.strip()]
    candidate = [line.rstrip() for line in candidate_text.splitlines() if line.strip()]
    matcher = difflib.SequenceMatcher(a=base, b=candidate, autojunk=False)
    touched = 0
    for tag, i1, i2, _j1, _j2 in matcher.get_opcodes():
        if tag in {"delete", "replace"}:
            touched += i2 - i1
    return touched / max(1, len(base))


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def compare_to_manifest(candidate: Metrics, manifest: dict, allow: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    thresholds = manifest.get("alarm_thresholds", {})
    min_line_ratio = float(thresholds.get("minimum_line_ratio", 0.92))
    min_equation_ratio = float(thresholds.get("minimum_equation_ratio", 0.95))

    if candidate.title != manifest.get("title"):
        errors.append(f"title changed: {candidate.title!r} != {manifest.get('title')!r}")
    if candidate.author != manifest.get("author"):
        errors.append(f"author changed: {candidate.author!r} != {manifest.get('author')!r}")

    missing_sections = [
        section for section in manifest.get("required_sections", [])
        if section not in candidate.sections
    ]
    missing_subsections = [
        section for section in manifest.get("required_subsections", [])
        if section not in candidate.subsections
    ]
    if missing_sections:
        errors.append("missing baseline sections: " + "; ".join(missing_sections))
    if missing_subsections:
        errors.append("missing baseline subsections: " + "; ".join(missing_subsections))

    base_lines = int(manifest.get("source_lines", 0))
    if base_lines and candidate.lines / base_lines < min_line_ratio:
        errors.append(
            f"line count fell from baseline {base_lines} to {candidate.lines} "
            f"({candidate.lines/base_lines:.3f} < {min_line_ratio:.3f})"
        )

    base_bibliography = int(manifest.get("bibliography_item_count", 0))
    if candidate.bibliography_items < base_bibliography:
        errors.append(
            f"bibliography items fell from {base_bibliography} "
            f"to {candidate.bibliography_items}"
        )

    base_equations = int(manifest.get("equation_environment_count", 0))
    if base_equations and candidate.equation_environments / base_equations < min_equation_ratio:
        errors.append(
            f"equation environments fell from {base_equations} "
            f"to {candidate.equation_environments}"
        )

    if allow:
        warnings.extend("OVERRIDDEN: " + error for error in errors)
        errors.clear()
    return errors, warnings


def compare_files(
    base_text: str,
    base: Metrics,
    candidate_text: str,
    candidate: Metrics,
    manifest: dict,
    allow: bool,
) -> tuple[list[str], list[str], float]:
    errors, warnings = compare_to_manifest(candidate, manifest, allow=False)
    thresholds = manifest.get("alarm_thresholds", {})
    max_replace = float(thresholds.get("maximum_prior_line_replacement_fraction", 0.15))
    fraction = replacement_fraction(base_text, candidate_text)

    missing_sections = [section for section in base.sections if section not in candidate.sections]
    missing_subsections = [
        section for section in base.subsections if section not in candidate.subsections
    ]
    if missing_sections:
        errors.append("removed current-source sections: " + "; ".join(missing_sections))
    if missing_subsections:
        errors.append(
            "removed current-source subsections: " + "; ".join(missing_subsections)
        )
    if candidate.bibliography_items < base.bibliography_items:
        errors.append(
            f"bibliography items fell from current source {base.bibliography_items} "
            f"to {candidate.bibliography_items}"
        )
    if base.equation_environments and (
        candidate.equation_environments / base.equation_environments
        < float(thresholds.get("minimum_equation_ratio", 0.95))
    ):
        errors.append(
            f"equation environments fell from current source {base.equation_environments} "
            f"to {candidate.equation_environments}"
        )
    if base.lines and (
        candidate.lines / base.lines
        < float(thresholds.get("minimum_line_ratio", 0.92))
    ):
        errors.append(f"line count fell from current source {base.lines} to {candidate.lines}")
    if fraction > max_replace:
        errors.append(
            f"{fraction:.1%} of prior nonblank lines were deleted/replaced; "
            f"alarm threshold is {max_replace:.1%}"
        )
    if candidate.title != base.title:
        errors.append(f"title changed from current source: {base.title!r} -> {candidate.title!r}")
    if candidate.author != base.author:
        errors.append(f"author changed from current source: {base.author!r} -> {candidate.author!r}")

    errors = list(dict.fromkeys(errors))
    if allow:
        warnings.extend(
            "OVERRIDDEN BY EXPLICIT USER REWRITE REQUEST: " + error for error in errors
        )
        errors.clear()
    return errors, warnings, fraction


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--base", type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--justification", type=Path)
    parser.add_argument("--json-report", type=Path)
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    candidate_text, candidate = read_metrics(args.candidate)
    allow, quote = destructive_override(args.justification)

    if args.base:
        base_text, base = read_metrics(args.base)
        errors, warnings, fraction = compare_files(
            base_text,
            base,
            candidate_text,
            candidate,
            manifest,
            allow,
        )
    else:
        base = None
        errors, warnings = compare_to_manifest(candidate, manifest, allow)
        fraction = None

    report = {
        "candidate": asdict(candidate),
        "base": asdict(base) if base else None,
        "prior_line_replacement_fraction": fraction,
        "explicit_rewrite_override": allow,
        "user_request_quote": quote if allow else None,
        "errors": errors,
        "warnings": warnings,
        "result": "PASS" if not errors else "FAIL",
    }
    print(json.dumps(report, indent=2))
    if args.json_report:
        args.json_report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
