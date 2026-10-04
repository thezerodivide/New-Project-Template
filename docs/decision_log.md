# <PROJECT NAME> Decision Log

Maintained per [Development_Protocol.txt](Development_Protocol.txt) Section 2. This log records *why* material decisions were made and how they evolved. It is distinct from [SPEC.md](../SPEC.md) (*what* the system must do) — do not merge the two, and do not reconstruct this log from memory; append to it as decisions are made. It is append-only: a correction is a dated addendum, never a rewrite.

Each entry is structured into four labeled blocks per §2: **Requirement** (behavior explicitly stated or approved), **Design choices** (the agreed shape of the solution), **Implementation choices** (details free to decide), and **Open** (unresolved questions). Approving a name or a number is not the same as approving a requirement. The blank shape is [templates/decision_log_entry.md](templates/decision_log_entry.md).

## Active overrides index

Entries below that supersede a specification item are indexed here so the supersession is visible without cross-referencing the whole log against the spec. Format: `**DL-nnn** SUPERSEDES SPEC.md <section or item>: <one line>`.

(none yet)

---

### DL-001 — <title: the first story, or a retrofit of an existing spec>

(For a later correction of this entry, do not edit it: append `**Addendum to DL-nnn, YYYY-MM-DD — <what changed and why>.**` at the end of the log.)

- **Status:** <Draft / Approved YYYY-MM-DD / Superseded by DL-nnn>. **Approved by the developer in their own words:** '<exact words>' (quote them; a reviewer's clearance is not the developer's approval). Verification tier: <none / local / code review / live>.
- **Story:** <the observed problem and what is actually known about it, before any solution is proposed>
- **Requirement:** <behavior explicitly stated or approved; each item the developer approved>
- **Design choices:** <the shape of the solution, agreed with the developer, with the reasoning>
- **Implementation choices:** <details free to decide; timing values are first guesses under Protocol §15 with evidence and a revisit trigger>
- **Open:** <unresolved items and what would resolve each>
- **Evidence:** <Verified (tested or read in source: say where) / Reasoned, not verified / Unknown>
- **Review chain:** <revisions presented, the secondary reviewer's findings, what was agreed or pushed back on>
- **Depends on / Shares seams with:** <other DL entries, hook points, data or ordering constraints, or none>
- **Not yet verified (do not describe as confirmed):** <list; update as items resolve>
- **Supersedes:** <earlier entry or spec item (also add it to the Active overrides index), or nothing>
