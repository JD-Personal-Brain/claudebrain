"""The mechanical part of a wrap-up (Elon mode findings 11 and 12, 2026-10-18), so Claude keeps only
the judgment: lessons, ideas, questions and the plain-words message.
Run from the repo root: python3 .claude/skills/wrap-up/run.py [base]   (base defaults to origin/main)
It:
  1. rebuilds every designed page from its working file (designs/*-build.py);
  2. runs the audit checker, the render check and the nothing-lost list;
  3. runs the RM prototype's tests if anything under prototypes/rm-assistant/ changed;
  4. lists every designed page that changed since base, with the link to republish it to
     (one place to see what's out of date, instead of remembering by hand);
  5. prints a draft Audit Log row, sized "quick", for Claude to finish (findings and lost lines by reason).
It changes no working file except the built pages, and publishes nothing: publishing stays a step Claude takes."""
import datetime, glob, os, re, subprocess, sys

base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
os.chdir(ROOT)

def run(cmd, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)
    return r.returncode, (r.stdout + r.stderr).strip()

def last(text, n=1):
    return "\n".join(text.splitlines()[-n:])

print("1. Rebuilding every page")
failed = [b for b in sorted(glob.glob("designs/*-build.py")) if run(["python3", b])[0] != 0]
print("   " + ("all builders ran" if not failed else "FAILED: " + ", ".join(failed)))

print("2. Audit scripts")
_, chk = run(["python3", ".claude/skills/audit/check.py"])
_, rnd = run(["node", "designs/render-check.js"])
_, lost = run(["python3", ".claude/skills/audit/lost-lines.py", base])
checker, render = last(chk), last(rnd)
lost_n = (re.search(r"lost: (\d+)", lost) or re.search(r"(\d+)", "0")).group(1)
print(f"   checker: {checker}\n   render check: {render}\n   nothing-lost: {lost_n} lines (run lost-lines.py to read them)")
if not checker.endswith(": 0"):
    print("\n".join("     " + l for l in chk.splitlines() if not l.startswith(("problems", "38 {", "44 sub"))))

_, changed = run(["git", "diff", "--name-only", base, "--", "."])
_, untracked = run(["git", "ls-files", "--others", "--exclude-standard"])
files = sorted(set(changed.split() + untracked.split()))

proto = "not changed"
if any(f.startswith("prototypes/rm-assistant/") for f in files):
    code, out = run(["node", "tests/run-tests.js"], cwd="prototypes/rm-assistant")
    proto = last(out)
print(f"3. RM prototype tests: {proto}")

print("4. Pages to republish (changed since " + base + ")")
links = {}
for line in open("designs/README.md", encoding="utf-8"):
    m = re.search(r"(https://claude\.ai/artifact/\w+).*?`([^`]+\.html)`", line)
    if m: links[os.path.basename(m.group(2))] = m.group(1)
pages = [f for f in files if f.endswith(".html") and (f.startswith("designs/") or f.startswith("prototypes/"))]
for f in pages:
    print(f"   {f}  ->  {links.get(os.path.basename(f), 'not in designs/README.md: check the latest prototype version link')}")
if not pages: print("   none")

print("5. Draft Audit Log row (finish the findings and lost-lines reasons)")
today = datetime.date.today().isoformat()
what = ", ".join(sorted({f.split('/')[0] if '/' in f else f for f in files})) or "nothing"
print(f"| {today} | Wrap-up: [what changed, in plain words] ({what}) | Quick: checker, render check, nothing-lost"
      f"{', the prototype tests' if proto != 'not changed' else ''} | [N] findings; lost lines: {lost_n}, [reworded / moved / cut on purpose] | Waiting for my yes to merge |")
