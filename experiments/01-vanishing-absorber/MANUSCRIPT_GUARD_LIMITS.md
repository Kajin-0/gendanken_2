# Manuscript Guard Enforcement Limits

The repository has three active layers against accidental manuscript loss:

1. mandatory agent/recovery rules in `AGENTS.md` and `MANUSCRIPT_PRESERVATION_PROTOCOL.md`;
2. a hash-verified immutable Rev. 3 source snapshot plus machine baseline;
3. GitHub Actions preservation checks for manuscript-related pull requests.

At the time this protection was installed, the connected repository-control capability did **not** expose a branch-protection/ruleset write operation. Therefore GitHub-side required-status-check enforcement could not be enabled programmatically from this session.

This does not weaken the source recovery anchor: the exact 16-page Rev. 3 source remains independently recoverable and verified. It means only that a human or tool with direct-write permission could technically bypass the PR rule. Such a direct manuscript write is explicitly prohibited by `AGENTS.md`.

If repository rulesets become available later, the preferred additional control is:

```text
protect main
require pull requests for manuscript changes
require the "Manuscript preservation / preservation" status check
block force pushes
```

Do not interpret the absence of GitHub branch protection as permission to bypass the preservation protocol.
