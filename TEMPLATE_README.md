# New Project Template (TEMPLATE_README.md)

Everything a new project needs to follow the development method worked out in MQClaudeTestBridge (and PTAutoRoute before it): a spec, an append-only decision log, a current-state ledger, a development protocol, a working agreement for the AI, a story template for starting work, a lessons log, and the two helper scripts the method relies on. Created 2026-10-04 from a review of every document in MQClaudeTestBridge. [docs/New_Project_Kit.md](docs/New_Project_Kit.md) explains the method and which documents are copied versus created per project.

## How to use it

1. Copy this folder's contents to the new project's location (not as a subfolder), delete `TEMPLATE_README.md` from the copy (it describes the template, not the project; write a real `README.md` later if you want one), and run `git init`. Do not edit the template folder itself; it is the master copy.
2. Open a Claude Code session in the new folder and paste **Part 1 of [START_PROMPT.md](START_PROMPT.md)**, filled in. Claude reads the documents, reports what it understands, and walks you through the bootstrap one question at a time.
3. Later sessions start with **Part 2** of the same file.

## What is here

| Path | What it is | Copied or created |
| --- | --- | --- |
| `START_PROMPT.md` | The reusable start prompt and the cold-start prompt. | Used, not committed unless you want it. |
| `CLAUDE.md` | The working agreement loaded every session. Portable rules; `<PLACEHOLDER>` text for the project. | Copied, then filled in. |
| `docs/Development_Protocol.txt` | The 22-section process contract, with the origin project's runtime-specific wording made generic. | Copied. |
| `docs/User_Story_Template.md` | How new work starts. | Copied. |
| `docs/New_Project_Kit.md` | The method's document checklist and bootstrap order. | Copied. |
| `docs/templates/` | Blank shapes: decision log entry, lesson entry, plain-text review handoff. | Copied. |
| `SPEC.md` | Skeleton of the specification. | Created per project. |
| `docs/decision_log.md` | Skeleton with the header, the overrides index and DL-001's shape. | Created per project. |
| `docs/project_ledger.md` | Skeleton with the four categories and a cold-start block. | Created per project. |
| `docs/lessons_learned.md` | Header and rules, no entries. | Created per project. |
| `tools/mutate.py`, `tools/refresh_review.py`, `tools/README.md` | The mutation runner and the review-folder refresher, generic and standard-library only. | Copied. |
| `test/README.md` | The testing rules to adapt to the language and platform. | Copied, then filled in. |
| `.gitignore` | A generic starting point. | Copied, then extended. |

## Not in this folder, on purpose

- This project's history, facts and decisions. A new project inherits none of them.
- A test harness or check command, which depends on the language; `test/README.md` says what it must do.
- Claude's per-user memory notes. The rules that matter are in `CLAUDE.md`, so nothing depends on memory.

## Changes from the origin documents

- `docs/Development_Protocol.txt`: the origin project's MacroQuest-specific wording was replaced with generic wording in §4 (one sentence), §8 (the file schema, now decided once per project and recorded in `CLAUDE.md`), §10 (one bullet), §14 (all examples) and §15 (one example). Every rule is unchanged.
- `docs/Development_Protocol.txt` §6: one added paragraph stating that code is test-first (the origin Protocol lists "implement the behavior" first and does not say tests come before it; the practice was recorded only in the origin project's decision log). The origin's own Protocol was not changed.
- `test/README.md` and `CLAUDE.md`: the test-first workflow (eight steps) written down; in the origin it lives only in its decision log's build-order entry.
- `docs/User_Story_Template.md`: four origin-specific phrases made generic.
- `CLAUDE.md`: new sections state, instead of leaving them implied, the roles and document ownership (developer, Claude as implementer and document maintainer, the secondary reviewer, ChatGPT by default), the spike procedure and the live-test handoff; the session cadence is the developer's choice (daily by default). The origin's one-line "Implement → ..." step was corrected in both repositories to say tests come first. The origin project's dated stories ("what prompted it") were removed, the rules kept; the second-reviewer sections are marked deletable; the push policy is parameterized.
- `tools/refresh_review.py`: rewritten to be generic, and safer than the original (it stops on an unrecognised entry instead of deleting it). `tools/mutate.py` is a new language-neutral version of the origin's runner.

The scripts were tested on scratch repositories (refresh with and without candidates, file names with spaces and non-ASCII characters, a stray entry, unsafe paths, symbolic links and submodules; mutation on LF and CRLF files with a caught, a surviving and an unmatched mutation, and with `--expect`; 32 checks in all, including a stale-bytecode-cache scenario run with the cache enabled and a drive-letter-case guard check; kept outside the template). Nothing else in this folder has been exercised.
