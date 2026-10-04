# New Project Kit: the documents this method needs

The method is a set of documents that carry the rules and the state, so that a cold-start Claude session and a secondary reviewer can rebuild context from the repository alone, with nothing resting on anyone's memory. This file says which documents a project needs, which of them are copied and which are created, how to fill in `CLAUDE.md`, and the order to bootstrap in. It is a guide, not part of the Protocol; it changes no rule. Origin: the method was developed in MQClaudeTestBridge, building on PTAutoRoute.

## The method in one paragraph

The spec says what the system must do. The decision log says why each material decision was made, append-only, in a fixed shape (Requirement / Design choices / Implementation choices / Open, plus evidence, review chain and a not-yet-verified list). The ledger says what is true now, in four categories, updated in place. The Development Protocol and `CLAUDE.md` say how decisions are made and recorded. The developer facilitates and makes every decision and risk call; Claude is the implementer and the document maintainer, drives the requirements conversation and surfaces what is verified, reasoned or unknown; an optional secondary reviewer (ChatGPT by default) reviews and recommends but never decides. Work goes one change at a time, test-first, with tests that cite their source and are proven able to fail, and nothing is called ready beyond its evidence tier.

## Documents that come with the template (the method itself)

These carry the rules, not the state. They are already in the template folder and already generic; copy them as they are, and fill in only what is named.

| Document | Job | What to fill in | Update rule |
| --- | --- | --- | --- |
| `docs/Development_Protocol.txt` | The process contract (22 sections). | Nothing. §8's file schema is decided once per project and recorded in `CLAUDE.md`. | Changed only by the developer, at a retrospective. |
| `CLAUDE.md` | The working agreement loaded every session. | The `<PLACEHOLDER>` text; see the table below. | In step with the code and the ledger (Protocol §18). |
| `docs/User_Story_Template.md` | How new work starts: story, observation, facts, constraints, risk, success criteria; Claude's one-question-at-a-time conversation and the Requirement / Assumption / Open labels. | Nothing. | Rarely. |
| `docs/templates/` | Blank shapes: decision log entry, lesson entry, plain-text review handoff. | Nothing. | When the shapes change. |
| `docs/New_Project_Kit.md` (this file) | The checklist. | Nothing. | When any document of the method changes shape. |
| `tools/` | `mutate.py` and `refresh_review.py`, with their README. | Nothing. | When a script changes. |
| `test/README.md` | The test-first workflow and the testing rules. | The language-specific parts (the check command, the layout). | When the testing method changes. |
| `START_PROMPT.md`, `TEMPLATE_README.md` | The start and cold-start prompts, and the template's own explanation. | Nothing; delete `TEMPLATE_README.md` from the new project. | Not applicable to the new project. |

## Documents each project creates for itself (the project's own state)

A new project does not inherit these from another project. Each starts as the skeleton in the template, and the project's first story fills it. Another project's versions would import that project's history and facts.

| Document | Job | What it starts as | Update rule |
| --- | --- | --- | --- |
| `SPEC.md` | What the system must do; authoritative. Confirmed facts, requirements, non-goals, a roadmap with checkable phase gates, risks and spikes. | A skeleton with placeholders; written from the first approved story and its acceptance criteria, never before. | In place, never silently, with dated `[CLARIFIED]` or `[CORRECTED]` markers; re-read end to end before release or handoff (§18). |
| `docs/decision_log.md` | Why each material decision was made. | A header, an empty "Active overrides index" so a supersession is visible where the log is read, and a DL-001 in the shape of `docs/templates/decision_log_entry.md` (a retrofit entry if a spec existed first). | Append-only; a correction is a dated addendum. |
| `docs/project_ledger.md` | Current state. | Four categories (Resolved behavior, Confirmed live/system facts, Open implementation details, Out of scope), an "Up next" section that opens with a cold-start block, Dependencies, and Pending Live Verification. | In place, with the correction visible; updated in the same step as any commit, push, review refresh or finished step. Never write the hash of HEAD in it. |
| `docs/lessons_learned.md` | Running log of lessons for a release retrospective. | A header explaining that it is not the Protocol, the Area / Suggested / Triage fields, and no entries. Triage stays blank until the retrospective. | Append-only; annotate, never delete. |

## Things that live beside the documents

- **A test harness and one check command** (for example a `check.cmd` or `check.sh`: syntax check, then the tests of each language; exit 0 only if all pass), a rule that every test cites its source, and a mutation runner for logic-heavy code (Protocol §7). `tools/mutate.py` works for any language through a test command.
- **A review folder for the secondary reviewer**, if one is used: a plain folder beside the checkout with no `.git`, a `MANIFEST.txt` (commit, hashes, which files are candidates), a `candidate/` subfolder for uncommitted files, and the refresh script (`tools/refresh_review.py`). The exact-artifact handoff in `CLAUDE.md` depends on it.
- **Claude's per-project memory notes**, if any: they are per user and per machine, so nothing may depend on them. Every rule that matters is in `CLAUDE.md`; put a new one there.
- **`.gitignore`** for machine-specific config, generated folders and caches, and a tracked `config.example.toml` (or equivalent) for the machine-specific file.

## Filling in `CLAUDE.md`

| `CLAUDE.md` section | What to do |
| --- | --- |
| Authoritative documents | Check the list matches the repository; keep the one-line job of each document. |
| What this is | Write it: one paragraph and how to run the project. |
| Development Protocol: core rules | Keep. |
| Roles and ownership | Keep; correct the cadence or reviewer if the developer says otherwise. |
| Working agreement | Keep. |
| The secondary reviewer, the reply format, the alert rule, the routing line | Keep if a secondary reviewer is used (ChatGPT unless the developer says otherwise); delete these sections and the review-folder process if not. |
| Handoff header on every reply | Keep. |
| Safety-sensitive code | Keep. |
| Spikes, Live-test handoff | Keep. |
| Pre-commit review handoff | Keep if a review folder is used; replace `<PROJECT>-Review` with the folder's name. |
| Approvals on pasted text, Working agreements | Keep. |
| Commits and pushes, durability policy | Keep. Delete the policy only if the repository has no remote. Replace `<USER>` and the branch name; adapt the scan's path pattern if the platform is not Windows. |
| Related projects | Start the list for the new platform, or leave "none yet". |
| Tooling notes, Architecture, Testing | Fill in as the project learns them. |

## Bootstrap order for a new project

1. Copy the template folder's contents to the new project's location (not as a subfolder), delete `TEMPLATE_README.md`, and run `git init`.
2. Fill in `CLAUDE.md` as in the table above, with the developer.
3. Run the first story through `docs/User_Story_Template.md`: the developer's story, Claude's restatement, one question at a time, labelled items, acceptance criteria approved before any solution. Record it in the decision log as DL-001 and write `SPEC.md` from what was approved.
4. Add the test harness and the single check command before the first code; write each test from a requirement with its source cited, before the implementation (`test/README.md`).
5. If using a secondary reviewer, create the review folder and manifest before the first review.
6. End each working session on the cadence the developer chose, with the ledger's cold-start block current (Protocol §22).
