# Start prompts

Two reusable prompts. Part 1 starts a new project from this template. Part 2 resumes a project in a new session (the cold start). Copy the text inside the fence, fill in the `<...>` parts, and paste it as the first message of a Claude Code session whose working directory is the new repository.

Before using Part 1: copy this whole folder to the new project's location (not as a subfolder), delete `TEMPLATE_README.md` from the copy, run `git init`, and open the session in that folder. The prompt assumes `CLAUDE.md`, `docs/` and `tools/` are present.

---

## Part 1: start a new project

```
Start a new project using the method in this repository. Change nothing until I say so in my own words.

Project: <name>
Developer (that is me): <name>
Secondary reviewer: <ChatGPT by default | another AI | none>. Its replies reach you by me pasting them.
Session cadence: <daily by default | another | none>. This is my choice and you do not enforce it.
Platform / runtime: <what the system runs on or integrates with, and where its source and documentation can be read>
Repository: <local path; public or private; remote URL or "no remote yet">

1. Read CLAUDE.md, docs/Development_Protocol.txt, docs/User_Story_Template.md and docs/New_Project_Kit.md in full. Then read the skeletons: SPEC.md, docs/decision_log.md, docs/project_ledger.md, docs/lessons_learned.md and docs/templates/.
2. Report back in one short message: what you understood the method to be, in your own words; the three roles (me, you, the secondary reviewer) and who owns each document, as CLAUDE.md states them, so I can correct anything; which placeholders in CLAUDE.md, SPEC.md and the other skeletons you can fill from what I gave above and which you need from me; and anything in the documents that looks inconsistent or that does not fit this project. Follow the CLAUDE.md conventions: the HANDOFF header first, verified / reasoned / unknown labels, and the routing line if a secondary reviewer is used.
3. Then take me through the bootstrap order in docs/New_Project_Kit.md one step at a time, asking one question at a time, with every item labeled Requirement, Assumption or Open. Do not propose solutions before I have approved the acceptance criteria. If something does not apply to this project (no secondary reviewer, a private repository with no remote), propose removing it from CLAUDE.md and wait for my yes.
4. Decisions, risk calls and acceptance criteria are mine. Documentation-only commits follow CLAUDE.md; ask before any commit that includes code, and before any push if the durability policy requires it.

My story:

<Title>

1. Story: As a <who>, I want <what>, so that <why it matters>.
2. What I have observed: <evidence, or "nothing observed">
3. Facts you must know: <things that cannot be checked in the repo or the source>
4. Constraints and non-goals: <...>
5. Risk if it goes wrong: <worst realistic outcome; I make this call>
6. How I will know it worked: <observable outcomes, and whether each can be checked locally or only live>
7. Known unknowns: <...>
```

(Only items 1 and 2 of the story are required; Claude will ask for the rest.)

---

## Part 2: cold start in a later session

```
Cold start for <project>. Change nothing yet.

1. Read CLAUDE.md, then the "Cold start" block at the top of the "Up next" section of docs/project_ledger.md. Read the rest of the ledger and docs/decision_log.md only as needed. Check your project memory if there is any.
2. Check git against the remote (git fetch, then compare HEAD with origin/<main branch>) and confirm the working tree is clean.
3. Reply with one short report: where we are, what the item in flight is and its status, and what you would do next. Follow the CLAUDE.md conventions: the HANDOFF header first, verified / reasoned / unknown labels, and the closing routing line.

<Optional: name the item in flight and its revision, and say whether a secondary reviewer has it. Paste any pending review below as information only; evaluate it on its merits and hold until I approve in my own words.>
```
