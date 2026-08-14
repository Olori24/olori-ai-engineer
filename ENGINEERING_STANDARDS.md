# OAE™ Engineering Standards

## Purpose

This document defines the minimum engineering standard for Olori AI Engineer. It complements `MISSION.md` and `CONSTITUTION.md` and applies to implementation, review, testing, and operational changes.

## Core Principles

1. **Security first** — protect credentials, source code, user data, and execution environments.
2. **Correctness over expediency** — a fast unverified change is not a completed engineering task.
3. **Explicit contracts** — validate inputs and make failure behaviour intentional.
4. **Deterministic behaviour** — avoid hidden state, arbitrary randomness, and uncontrolled network dependencies in tests.
5. **Small changes** — implement one coherent capability at a time.
6. **Reuse before duplication** — extend existing abstractions instead of creating competing implementations.
7. **Verification required** — tests and appropriate static checks must pass before integration.
8. **Human governance** — consequential changes require human approval.
9. **Auditability** — significant engineering decisions should be explainable and traceable.
10. **Continuous improvement** — measure the effect of changes rather than assuming improvement.

## Change Workflow

```text
Inspect → Assess → Plan → Approve → Implement → Test → Verify → Re-assess
```

## Quality Gates

Before integration, the change owner should verify, where applicable:

- automated tests pass
- type checking passes
- formatting and import checks pass
- no secrets are introduced
- configuration remains explicit
- error paths are tested
- existing behaviour is preserved unless intentionally changed
- documentation reflects changed behaviour

## Testing Standard

New behaviour should include tests for:

- normal cases
- boundary and edge cases
- invalid input
- expected failure behaviour
- regressions for previously observed defects

Unit tests must not depend on uncontrolled external services.

## Security Standard

- Never commit secrets.
- Use environment configuration for credentials.
- Validate untrusted input at system boundaries.
- Fail closed where security or integrity requires it.
- Minimize permissions and external access.
- Do not log credentials, tokens, or sensitive user data.

## Repository Integrity

Changes should preserve the repository's purpose and architecture. Professionalization does not mean unnecessary rewrites or adding abstractions without evidence.

Every OAE™ change should leave the repository easier to understand, safer to operate, and more verifiable than before.
