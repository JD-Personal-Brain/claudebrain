"""Nothing-lost check (idea 46, rule R29). Run from the repo root:
    python3 .claude/skills/audit/lost-lines.py [base]      (base defaults to origin/main)
Lists every sentence that was in a working file at <base> and is now gone from the whole repo:
not in that file, and not moved to any other working file or designed page. Each one printed
must be either put back, or named in the audit report as "cut on purpose" with the reason.
Sentences that were only reworded show up too; say so in the report.
Ends with a count per file (to group the lines by reason in the Audit Log entry) and "lost: N". 0 means nothing disappeared."""
import subprocess, re, sys, glob, html

base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
WORK = ["*.md", "memos/*.md", "playbook/*.md", "learning/*.md", ".claude/skills/*/SKILL.md", "designs/library.json"]
SKIP = {"learning/lessons.md", "ideas.md"}  # history files: lines there are kept on purpose

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True).stdout

def sentences(text):
    text = re.sub(r"<[^>]+>", "\n", text)            # each tag ends a piece, like a line break
    text = html.unescape(text)
    out = []
    for piece in re.split(r"\n|\|", text):          # one line or one table cell at a time
        piece = re.sub(r"[*`_>#]", " ", piece)       # Markdown marks
        piece = re.sub(r"\s+", " ", piece)
        for s in re.split(r"(?<=[.!?:;])\s+", piece):
            s = s.strip(" -·")
            if len(s.split()) >= 6:                  # short fragments are too noisy to track
                out.append(s)
    return out

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

# everything a reader or Claude can see today, flattened into one searchable text
now_files = set(git("ls-files").split())         # every file in the repo, nested folders included
now_files = {f for f in now_files if f.endswith((".md", ".json", ".html")) and not f.startswith("designs/rm-analytics-canvas/support")}
corpus = " ".join(norm(" ".join(sentences(open(f, errors="ignore").read()))) for f in now_files)

changed = [f for f in git("diff", "--name-only", base, "--", *WORK).split() if f not in SKIP]
# working files renamed since base (old path -> new path), checked under their old name
renamed = [l.split("\t")[1] for l in git("diff", "--name-status", "-M", base).splitlines()
           if l.startswith("R") and l.split("\t")[1].endswith((".md", ".json")) and l.split("\t")[1] not in SKIP]
lost = 0
printed = []
for f in sorted(set(changed + renamed)):
    old = git("show", f"{base}:{f}")
    if not old:
        continue
    for s in sentences(old):
        if norm(s) and norm(s) not in corpus:
            print(f"{f}: {s[:160]}")
            printed.append(f"{f}: {s[:160]}")
            lost += 1
# a count per file, so the audit entry can group them by reason (Audit Log improvement 6)
from collections import Counter
per = Counter(l.split(":")[0] for l in printed)
for f, n in sorted(per.items(), key=lambda x: -x[1]):
    print(f"  {n:4d}  {f}")
print("lost:", lost)
