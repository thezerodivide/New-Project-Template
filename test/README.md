# Tests

The method's testing rules (Development Protocol §6, §7, §20). Fill in the language-specific parts at the start of the project and record them in `CLAUDE.md` ("Testing").

## Test-first workflow

Every code change that has a requirement follows this order. It is how the method applies Protocol §6 and §7 to code: the tests come before the implementation, and the review gates of §6 follow.

1. **Take the requirement.** An approved decision log entry, acceptance criterion or spec section. If there is none, stop: that is a missing decision, not a test to write.
2. **Write the tests from the requirement.** Each test cites its source (a decision log ID, a spec section or a real log line) in the test itself. The expected value comes from the requirement, never from running the implementation and pasting its output. Cover the failure and boundary cases the requirement implies, not only the happy path.
3. **Run them and watch each fail, for the right reason.** Failing because the function does not exist yet is not enough where a more specific failure is possible; check that each test fails on the behavior it protects. A test that passes before the implementation exists is testing nothing, or the wrong thing.
4. **Implement the smallest change that makes them pass.** No behavior beyond the requirement (Protocol §3).
5. **Run the whole check command**, not only the new tests, and read any failure before changing anything (Protocol §5: do not patch the last symptom).
6. **Mutation-check the logic-heavy parts** (`tools/mutate.py`): break each protected behavior on purpose and confirm a test fails because of it. Fix each survivor with a test, or record it as an equivalent mutant with the reason. Remove a check that the code makes redundant instead of keeping a test for it.
7. **Review as an outside developer**: compare the result with the spec, read the test evidence as though receiving the build, and inspect at least one representative log or output (Protocol §6 steps 2, 3 and 5, §8).
8. **Hand off with the evidence tier stated** (Protocol §10): local/simulated, static review or live. A passing local suite is never described as live validation.

Two cautions. A fake of a library or runtime must model the real contract, read from its documentation, because a fake written from memory by the author of the code can share the author's mistake (CLAUDE.md, "A reviewer's finding is a class, not an instance"). And a spike or live test that cannot run locally is still written from a stated question and a stated pass condition before it runs.

## Standing rules

1. **One check command runs everything** (syntax check, then each language's tests) and exits 0 only if all of it passes. Create it before the first code: `check.cmd`, `check.sh`, a Makefile target, whatever fits the platform. Run it before every commit.
2. **Every test cites its source** in the test itself: a decision log ID, a spec section or a real log line. Never take an expected value from running the implementation and pasting the output.
3. **Logic-heavy code gets a mutation check:** break the protected behavior on purpose and confirm the test fails because of it. `tools/mutate.py` automates this: one mutations file per source file, each mutation a unique `old` text and its `new` text; survivors are either fixed with a test or recorded as equivalent mutants with the reason.
4. **Separate deterministic logic from the runtime-bound adapter** wherever that gives real testability without distorting the design (§20). Test the logic with fakes; model a fake on the real library's documented contract, never from memory. The live run is the authority for the adapter.
5. **Say which tier the evidence is** (local/simulated, static review, live) whenever reporting a result (§10).

Suggested layout: `test/` for the tests and any shared fakes, `test/vendor/` for a vendored test framework left unmodified, and the check command at the top of `test/`.
