# Privacy and Pseudonymity Protocol

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
