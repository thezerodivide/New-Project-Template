"""Generic mutation runner (Development Protocol section 7): break the protected behavior on purpose and confirm the tests
fail because of it.

Usage:
    python tools/mutate.py --cmd "<test command>" [--cwd <dir>] [--timeout <seconds>] [--expect <text>]
                           <source file> <mutations file>

  --cmd      the command that runs the relevant tests; exit code 0 means they pass (run through the shell).
  --cwd      the directory to run it in (default: the current directory).
  --expect   optional. Require this text in the test output for a mutation to count as caught, so a crash or a syntax
             error cannot pass for "the right test failed". Without it, any non-zero exit counts as caught, and the
             last line of the output is printed beside each caught mutation so the reason can be read.
  source     the file to mutate (path relative to --cwd, or absolute).
  mutations  a Python file that defines  muts = [(name, old, new), ...]  where `old` is text that occurs exactly once in
             the source and `new` replaces it. '@@' stands for a newline in both strings; it becomes the source file's
             own line ending (CRLF if the file contains any, otherwise LF).

The baseline must pass first. Each mutation is applied alone and the source is restored byte for byte at the end, even on
an error or an interrupt. To keep compiled caches honest (a cache such as Python's .pyc is validated by the source's size
and its modification time in whole seconds, so a same-size mutant written in the same second can run stale cached code),
each mutant is given its own modification time two seconds apart, the original time is put back after the restore, and
the test command runs with PYTHONDONTWRITEBYTECODE=1 so this script leaves no cached copies behind. Other languages with
build or bytecode caches may need the same care. A mutation is CAUGHT when the tests exit non-zero (or time out, or, with --expect, fail with
the expected text) and SURVIVED when they still pass. A survivor is either a missing test (add one) or an equivalent
mutant (record why, in the decision log or the commit). The exit code is 0 only if every mutation was caught, every
pattern matched exactly once, and the source was restored byte for byte.
"""
import argparse
import os
import runpy
import subprocess
import sys


def ascii_safe(text):
    return text.encode('ascii', 'backslashreplace').decode('ascii')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cmd', required=True)
    ap.add_argument('--cwd', default=os.getcwd())
    ap.add_argument('--timeout', type=float, default=120)
    ap.add_argument('--expect', default=None)
    ap.add_argument('source')
    ap.add_argument('mutations')
    args = ap.parse_args()

    cwd = os.path.abspath(args.cwd)
    source = args.source if os.path.isabs(args.source) else os.path.join(cwd, args.source)
    if not os.path.isfile(source):
        sys.exit('source file not found: ' + source)
    muts = runpy.run_path(args.mutations).get('muts')
    if not muts:
        sys.exit('the mutations file defines no muts (an empty list would pass vacuously)')

    original = open(source, 'rb').read()
    stat = os.stat(source)
    newline = '\r\n' if b'\r\n' in original else '\n'

    def run():
        """Return (exit code or 'timeout', combined output text)."""
        try:
            r = subprocess.run(args.cmd, shell=True, cwd=cwd, capture_output=True, timeout=args.timeout,
                               env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
        except subprocess.TimeoutExpired:
            return 'timeout', ''
        return r.returncode, (r.stdout + b'\n' + r.stderr).decode('utf-8', 'replace')

    def last_line(output):
        lines = [l.strip() for l in output.splitlines() if l.strip()]
        return ascii_safe(lines[-1][:120]) if lines else '(no output)'

    baseline, _ = run()
    print('baseline: %s' % ('pass' if baseline == 0 else 'FAIL (%s); fix the tests before mutating' % baseline))
    if baseline != 0:
        sys.exit(2)

    problems = []
    try:
        text = original.decode('utf-8')
        for index, (name, old, new) in enumerate(muts):
            old, new = old.replace('@@', newline), new.replace('@@', newline)
            count = text.count(old)
            if count != 1:
                print('PATTERN MATCHES %d TIMES (need exactly 1): %s' % (count, name))
                problems.append(name + ' [pattern]')
                continue
            open(source, 'wb').write(text.replace(old, new).encode('utf-8'))
            os.utime(source, ns=(stat.st_atime_ns, stat.st_mtime_ns + (index + 1) * 2_000_000_000))
            code, output = run()
            if code == 0:
                print('SURVIVED %s' % name)
                problems.append(name)
            elif args.expect is not None and code != 'timeout' and args.expect not in output:
                print('FAILED, BUT NOT WITH THE EXPECTED TEXT %r: %s | last line: %s' % (args.expect, name,
                                                                                         last_line(output)))
                problems.append(name + ' [unexpected failure]')
            else:
                print('caught   %s | exit %s | last line: %s' % (name, code, last_line(output)))
    finally:
        open(source, 'wb').write(original)
        os.utime(source, ns=(stat.st_atime_ns, stat.st_mtime_ns))
    restored = open(source, 'rb').read() == original
    print('restored identical:', restored)
    if not restored:
        problems.append('[source not restored]')
    print('%d mutations; problems: %s' % (len(muts), problems if problems else 'none'))
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
