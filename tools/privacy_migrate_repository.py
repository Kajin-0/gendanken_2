#!/usr/bin/env python3
"""One-time privacy migration: make pseudonymity the canonical repository default."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "01-vanishing-absorber"
OLD_SOURCE = "MANUSCRIPT_REV3_ANON_2026-08-11.tex"
NEW_SOURCE = "MANUSCRIPT_REV3_ANON_2026-08-11.tex"
OLD_NAME = "Anonymous"
OLD_SOURCE_SHA = "3ba57ed7c7bbe264038ffa4e6eabfc1ea90c1075d4989d4075d2589352cf6d8c"
NEW_SOURCE_SHA = "3ba57ed7c7bbe264038ffa4e6eabfc1ea90c1075d4989d4075d2589352cf6d8c"
OLD_GZIP_SHA = "e413c1be218f4f3d33611381b6407137169abafb6fc22a6087f33f77b3c2ae3e"
NEW_GZIP_SHA = "e413c1be218f4f3d33611381b6407137169abafb6fc22a6087f33f77b3c2ae3e"

PRIVACY_LOCK = """## CRITICAL: privacy / pseudonymity lock

**Pseudonymity is the default and identifying information is opt-in.** Never insert or restore a legal name, personal email, phone number, street address, precise personal location, employer/affiliation, signature, identifying account handle, or other identifying metadata into a manuscript, repository file, public artifact, PDF metadata, or release unless the user explicitly approves that specific disclosure.

Do not infer disclosure permission from account/profile information, prior files, git history, memory, authorship conventions, or the fact that identifying information appeared previously. Previous disclosure is not continuing consent.

For manuscripts and generated PDFs, the default author and PDF-author metadata are `Anonymous` unless the user explicitly chooses a pseudonym or author identity for that artifact. **A real identity must never become the canonical baseline by default.**

If identity disclosure is explicitly requested, follow `PRIVACY_PROTOCOL.md` and record only the minimum approved disclosure. Scientific preservation and identity disclosure are separate decisions.

"""

PRIVACY_DOC = """# Privacy and Pseudonymity Protocol

**Status:** MANDATORY  
**Default:** PSEUDONYMOUS / ANONYMOUS  

## Core rule

Identifying information is **opt-in, never inferred**.

No agent may insert, restore, propagate, canonicalize, or publish identifying information unless the user explicitly approves that specific disclosure. This applies even when the information is already available in account metadata, prior conversations, earlier drafts, git history, file metadata, or public sources.

Identifying information includes, at minimum: legal name, personal email, phone number, home/street address, precise personal location, employer or organizational affiliation when personally identifying, signatures, personal account handles, author metadata, and combinations of facts that materially identify the user.

## Manuscripts and artifacts

- Default author: `Anonymous`.
- Default PDF author metadata: `Anonymous`.
- A user-selected pseudonym may be used only after explicit approval of that pseudonym for the artifact.
- A legal/real identity may be used only after explicit approval for that artifact.
- Prior use of an identity is not continuing consent.
- Never make a real identity part of the canonical manuscript baseline merely because it appeared in an earlier draft.

## Repository behavior

Before adding identifying information to a tracked file or public artifact, require an explicit current user instruction. If approval is absent, omit the field or use `Anonymous`.

An identity-bearing manuscript change requires `IDENTITY_RELEASE.md` containing the exact user instruction authorizing the disclosure, the exact identifier approved, and the artifact/scope for which it is approved. Approval is scoped; it does not authorize reuse elsewhere.

## Priority rule

When scientific reproducibility and privacy conflict, preserve the scientific content while stripping or neutralizing identity metadata. Identity is not scientifically substantive content.

## Historical data

Do not rewrite scientific history merely to remove an identity from prose if doing so risks corrupting scientific provenance. However, remove identifying material from the live canonical tree when practical and do not propagate it into new artifacts. Git-history erasure is a separate destructive operation and must not be performed casually.
"""


def tracked_files() -> list[Path]:
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [ROOT / p.decode() for p in out.split(b"\0") if p]


def replace_text(path: Path) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return
    new = text.replace(OLD_NAME, "Anonymous")
    new = new.replace(OLD_SOURCE, NEW_SOURCE)
    new = new.replace(OLD_SOURCE_SHA, NEW_SOURCE_SHA)
    new = new.replace(OLD_GZIP_SHA, NEW_GZIP_SHA)
    new = new.replace("source_bytes: 43544", "source_bytes: 43544")
    new = new.replace('"source_bytes": 43544', '"source_bytes": 43544')
    new = new.replace("gzip bytes: 15358", "gzip bytes: 15358")
    if new != text:
        path.write_text(new, encoding="utf-8")


def main() -> int:
    # Replace identity-bearing canonical metadata across tracked text files.
    for path in tracked_files():
        replace_text(path)

    agents = ROOT / "AGENTS.md"
    text = agents.read_text(encoding="utf-8")
    if "## CRITICAL: privacy / pseudonymity lock" not in text:
        marker = "Read this file first.\n\n"
        if marker not in text:
            raise SystemExit("AGENTS.md insertion marker not found")
        text = text.replace(marker, marker + PRIVACY_LOCK, 1)
        agents.write_text(text, encoding="utf-8")

    privacy = ROOT / "PRIVACY_PROTOCOL.md"
    privacy.write_text(PRIVACY_DOC, encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    note = "**Privacy default:** pseudonymous/anonymous. Identifying information requires explicit user approval; see [`PRIVACY_PROTOCOL.md`](PRIVACY_PROTOCOL.md).\n\n"
    if note not in text:
        marker = "First-principles thought experiments in photodetector physics. Failed conjectures, counterexamples, corrections, and prior-art collisions are retained because they define the actual result.\n\n"
        text = text.replace(marker, marker + note, 1)
        readme.write_text(text, encoding="utf-8")

    # Update structured baseline fields exactly.
    manifest_path = EXP / "MANUSCRIPT_BASELINE.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["source_filename"] = NEW_SOURCE
    manifest["source_sha256"] = NEW_SOURCE_SHA
    manifest["source_bytes"] = 43544
    manifest["author"] = "Anonymous"
    manifest["privacy_default"] = "anonymous"
    manifest["identity_release_required"] = True
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Remove identity-bearing snapshot filenames from the live tree.
    history = EXP / "manuscript_history"
    for path in history.glob("MANUSCRIPT_REV3_ANON_2026-08-11.tex.gz.b64.part*"):
        path.unlink()

    # The one-time workflow removes itself before the migration commit.
    once = ROOT / ".github" / "workflows" / "privacy-migration-once.yml"
    if once.exists():
        once.unlink()

    # Current live tree must not contain the prior author identity or old identity-bearing filename.
    bad = []
    for path in tracked_files() + [privacy]:
        if not path.exists():
            continue
        try:
            t = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if OLD_NAME in t or OLD_SOURCE in t:
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        raise SystemExit("privacy migration incomplete: " + ", ".join(bad))

    print("privacy migration complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
