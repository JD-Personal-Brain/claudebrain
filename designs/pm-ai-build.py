"""Builds PM Detail (memos/pm-ai-reference.md): every portfolio manager (PM) working
file stitched into one document, so someone can give an AI the whole PM picture in
one go (copied from rm-ai-build.py on 2026-10-19). It is generated: edit the working files, never this
output. Run: python3 designs/pm-ai-build.py, then python3 designs/md-page-build.py."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = "memos/pm-ai-reference.md"

# part title, working file, the one section to keep (None = the whole file)
PARTS = [
    ("Executive summary", "memos/pm-executive-summary.md", None),
    ("The product: The PM Assistant (short version for people)", "memos/pm-assistant.md", None),
    ("The PM Assistant in full detail", "memos/pm-assistant-detail.md", None),
    ("The plan (short version for people)", "memos/pm-plan.md", None),
    ("The full delivery plan, with every step, agent spec and workflow", "memos/pm-assistant-framework.md", None),
    ("Core use cases and outside research", "memos/use-case-library.md", "Portfolio managers"),
    ("What banks are deploying in commercial credit, in full", "memos/credit-market-scan.md", None),
    ("The prototype: what it shows and how it's built", "prototypes/pm-assistant/README.md", None),
]

def read(p):
    return open(os.path.join(ROOT, p)).read()

def body(src, keep):
    s = read(src)
    s = re.sub(r"\n_Last updated: [^_]+_\s*$", "", s.strip())
    s = s.split("\n", 1)[1].strip()  # drop the file's own title
    if keep:
        s = s.split(f"## {keep}\n", 1)[1]
        s = re.split(r"\n## ", s, maxsplit=1)[0]
    return re.sub(r"^(#{2,3}) ", lambda m: "#" + m.group(1) + " ", s, flags=re.M)  # one level down

def build():
    parts = [p for p in PARTS if os.path.exists(os.path.join(ROOT, p[1]))]  # the prototype README joins once it exists
    dates = [re.search(r"_Last updated: ([^_]+)_", read(f)).group(1) for _, f, _ in parts]
    out = ["# PM Detail", "",
           "Everything about the portfolio manager (PM) work at Associated Bank in one document, for an AI to read. "
           "Give this whole document to an AI model so it has the full context: the product, the plan, every step, "
           "the agent specs, the workflows and the credit market research. People should read the three short pages for people above it in the PM section "
           "(the PM Executive Summary, The PM Assistant and the PM Assistant Plan), and can try the PM Assistant Prototype, the fourth row.", "",
           "> **How to read it (for the AI).** The parts below are the working files, copied in whole and in this order. "
           "Later parts give more detail on earlier ones. Lines marked ⚠️ are guesses or hypotheses to confirm at the bank; "
           "[X] marks a number not yet known: never invent a value for it. The product is a working hypothesis until Discover "
           "with the bank's PMs. Built automatically from the working files; never edit this file by hand.", ""]
    for i, (title, src, keep) in enumerate(parts, 1):
        out += [f"## Part {i}: {title}", "", f"Working file: `{src}`.", "", body(src, keep), ""]
    out.append(f"_Last updated: {max(dates)}_")
    open(os.path.join(ROOT, OUT), "w").write("\n".join(out) + "\n")

if __name__ == "__main__":
    build()
