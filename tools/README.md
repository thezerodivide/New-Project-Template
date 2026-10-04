# Tools

Two standard-library Python scripts (tested on Python 3.14.7 only; the tar `data` filter is used where the Python version has it, which is untested on 3.12 and 3.13). Neither touches the network. Each prints `--help`.

## mutate.py: mutation checks (Protocol §7)

```
python tools/mutate.py --cmd "<test command>" --cwd <repo> [--expect <text>] <source file> <mutations file>
```

The mutations file defines `muts = [(name, old, new), ...]`. `old` must occur exactly once in the source; `@@` stands for a newline and becomes the file's own line ending (CRLF if the file has any, otherwise LF). The baseline must pass, each mutation is applied alone, and the source is restored byte for byte. The exit code is 0 only if every mutation was caught, every pattern matched exactly once, and the restore was identical.

A mutation counts as caught when the tests exit non-zero, and the last line of the test output is printed beside it so the reason can be read. A crash or a syntax error also exits non-zero, so use `--expect <text>` when you need "failed for the right reason" (Protocol §7): with it, a failure that does not contain the text is reported as a problem. A survivor is a missing test or an equivalent mutant (record the reason).

Compiled caches: a cache such as Python's `.pyc` is validated by the source's size and its modification time in whole seconds, so a same-size mutant written in the same second can run stale cached code. The script gives each mutant its own modification time (two seconds apart), restores the original time afterwards, and runs the test command with `PYTHONDONTWRITEBYTECODE=1` so it leaves no cached copies behind. Other languages with build or bytecode caches may need the same care.

Write mutations files in a scratch folder, not in the repository, unless the developer wants them kept. Build text containing backslashes with a Write or Edit tool, not a shell heredoc (CLAUDE.md, "Read back what you generate").

## refresh_review.py: the secondary reviewer's review folder (CLAUDE.md, "Pre-commit review handoff")

```
python tools/refresh_review.py --dev <checkout> --rev <review folder beside it> [--branch origin/main]
                               [--candidate <repo path> ...] [--keep <top-level name> ...]
```

Rebuilds the review folder from the pushed commit (byte-exact `git archive`), copies the named uncommitted files into `candidate/`, writes `MANIFEST.txt` (UTF-8) and verifies everything by reading it back. File names may contain spaces and non-ASCII characters. Run it from anywhere; it never writes inside `--dev`. After a push, run it with no `--candidate` to clear the candidates.

- It stops, before creating or deleting anything, if the review folder holds a top-level entry it does not recognise (the reviewer may have written there): inspect it, move it aside, run again.
- It **does** replace everything inside the top-level folders it manages (those listed in the previous manifest), so a reviewer's note saved inside such a folder is lost. Keep reviewer notes outside the managed folders.
- Refused with a message: a review folder inside the checkout or containing a `.git`, a missing candidate, and a commit that contains symbolic links or submodules (not supported).
