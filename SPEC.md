# <PROJECT NAME> — Design Spec

<Date> · <Developer>

*Skeleton. Written from the first approved story and its acceptance criteria (docs/User_Story_Template.md), never before. The spec says what the system must do; why each decision was made lives in docs/decision_log.md. Any in-place change after approval carries a dated marker such as `[CLARIFIED YYYY-MM-DD, DL-nnn: ...]` or `[CORRECTED YYYY-MM-DD: ...]`, so a correction stays visible as a correction (Protocol §2, §18). Delete this paragraph once the first section is real.*

## Overview

<What the system does and for whom, in a few sentences.>

**Goals**

- <...>

**Non-goals for v1**

- <...>

## Environment and confirmed facts

Facts established by source, documentation, live testing or logs. Mark each with where it was established. Anything not yet established is an open question (Protocol §4), not a fact.

| Item | Value |
| --- | --- |
| <e.g. runtime or platform version> | <value, and how it was confirmed> |

## Requirements

Behavior the developer has explicitly approved, each traceable to a decision log entry.

- <R1 — approved YYYY-MM-DD, DL-nnn>

## Architecture

<The designed shape: components, what each owns, how they communicate. Note which parts are runtime-bound and which are deterministic logic that can be tested without the runtime (Protocol §20).>

## Configuration

<Where configuration lives, which keys exist, their defaults, and what is validated.>

## Testing approach

<How requirements are tested locally, what can only be checked live, and how each test cites its source (Protocol §7).>

## Roadmap

Each phase gate is a specific, checkable condition, not a vague "when it feels ready".

| Phase | Scope | Gate |
| --- | --- | --- |
| 0 | <...> | <checkable condition> |

## Risks and spikes

Unknowns that need evidence before the design depends on them. Each spike: the question, the smallest test that answers it, and where the answer is recorded.

- <spike, status>
