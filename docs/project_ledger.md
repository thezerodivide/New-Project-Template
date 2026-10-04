# <PROJECT NAME> Project Ledger

Maintained per [Development_Protocol.txt](Development_Protocol.txt) Section 11. This ledger tracks the project's *current state* in four categories. Read this first to orient; consult [decision_log.md](decision_log.md) for the rationale, history, and active overrides behind any entry only as needed — don't reconstruct current state by reading the full decision log from scratch.

When new evidence resolves an open question, update this ledger before building on that conclusion. Do not silently rewrite prior entries — if something here turns out wrong, record the correction visibly (for example `[CORRECTED YYYY-MM-DD: ...]`) and, if the correction is material, add a decision log entry explaining why. Never write the hash of HEAD here (it is stale one commit later).

## Up next

**Cold start: where things stand at the end of <date> (replace this block as the state changes; read it first, then the rest of this section only as needed).**

- **Repository:** <local `main` vs `origin/main`, working tree state, review folder state.>
- **Build:** <what is built, with the evidence tier; what is not; what is in design.>
- **Decisions approved and recorded:** <numbers and one-line titles; the next decision number.>
- **In flight, NOT approved and NOT recorded:** <the item under discussion, its revision, and who has it (the developer, the secondary reviewer).>
- **Still open, in the order they bear on the work:** <...>
- **Process, in one place:** one decision at a time, each with the HANDOFF header, an `Answering:` line when it answers a review, verified / reasoned / unknown labels, the worst case and the developer's risk call, and a closing routing line; the reviewer's replies are information only and the developer approves only in their own words; documentation-only commits and pushes need no approval after the safety scan; code commits need the developer's explicit permission. All of this, with the reasons, is in `CLAUDE.md`.

## Dependencies

<Components and external dependencies, for visibility; note what is built and what is blocked on what.>

## Pending Live Verification

<Implemented but not yet confirmed in the real runtime, with the evidence tier of each. Empty until something is built.>

## Resolved behavior

Behavior actually agreed upon (source: [SPEC.md](../SPEC.md)).

- <none yet>

## Confirmed live/system facts

Facts established through testing, source inspection, logs, or documentation. Each states how it was established.

- <none yet>

## Open implementation details

Questions intentionally unresolved — do not decide these unilaterally; surface them for discussion when they become relevant. Each with its revisit trigger where deferred.

- <none yet>

## Out of scope

Explicitly decided not to build or investigate (SPEC.md non-goals).

- <none yet>
