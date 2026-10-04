# User Story Template

How a new piece of work starts. The developer supplies a story; Claude drives the requirements *conversation* (questions, gaps, structure). The developer owns every decision, every risk judgment and every acceptance criterion. Source of truth stays the spec and the [decision log](decision_log.md) ([Development_Protocol.txt](Development_Protocol.txt) §1).

**Minimum viable story: sections 1 and 2.** Everything else can be left blank or marked "unknown"; Claude will ask. Nobody needs to write out all their reasoning: give conclusions and the facts that constrain them.

---

## The story (developer fills in)

**Title:** short name.

### 1. Story
As a *(who)*, I want *(what)*, so that *(why it matters)*.

### 2. What I have observed
Evidence, not theory: log excerpts, test output, a failure I saw, a run that worked. Say "nothing observed" if that's the truth; a story with no observation is allowed, but it is labeled speculative from the start.

### 3. Facts Claude must know
Things that cannot be checked in the repo, a dependency's source or the logs: domain rules, how the developer runs things, accounts, machines. Claude states any fact it is assuming instead of asking for the reasoning behind it.

### 4. Constraints and non-goals
What must stay true (existing DL entries, spec sections, rules in `CLAUDE.md`) and what this deliberately does not cover.

### 5. Risk if it goes wrong
The worst realistic outcome, and whether the developer judges it small. **The developer makes this call.** It weights how much automation versus caution is acceptable; Claude states the worst case and recommends, but never decides it.

### 6. How I'll know it worked
Observable outcomes, ideally one line each. For each, say whether it can be checked locally by a test or only live in the real runtime. Claude never calls something verified beyond its tier (Protocol §10).

### 7. Known unknowns
What the developer is unsure about.

---

## What Claude does next

1. **Restate** the story in Claude's own words, so misunderstandings surface first.
2. **Ask clarifying questions one at a time.** Facts before options; no list of questions; no request for a decision while the discussion is still open.
3. **Label every item** as **Requirement** (needs the developer's explicit yes), **Assumption** (needs a yes or a correction) or **Open** (unresolved). Nothing moves to Requirement by silence or by a bundled "agreed".
4. **Write acceptance criteria** with the developer, item by item.
5. **No solutions before the acceptance criteria are approved.** Then propose the smallest design that meets them, with a recommendation and its reasoning, and list what is deliberately deferred (Protocol §3; scope creep is called out by either side).
6. **Check the checkable first:** read the repo, `SPEC.md`, the ledger, the decision log, any dependency source kept in `references/` and the developer's related projects (the list in `CLAUDE.md`) before asking the developer.
7. **Record it** in the decision log (shape: [templates/decision_log_entry.md](templates/decision_log_entry.md)) and update the ledger. Docs-only commits need no permission and code commits do; a push follows the repository durability policy (see `CLAUDE.md`, "Commits and pushes").

## Decision log entry shape (new entries)

New entries use the shape in [templates/decision_log_entry.md](templates/decision_log_entry.md): the four labeled blocks of Protocol §2 (**Requirement**, **Design choices**, **Implementation choices**, **Open**), so a change to an implementation choice can never look like a change to the spec, plus the story, the developer's approving words quoted, the evidence (verified / reasoned / unknown), the review chain, **Depends on / Shares seams with**, the **not yet verified** list, and **Supersedes**. Do not keep a second copy of the shape here.
