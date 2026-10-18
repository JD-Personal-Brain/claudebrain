"""Builds RM Detail (memos/rm-ai-reference.md): every RM working
file stitched into one document, so someone can give an AI the whole RM picture in
one go (decided 2026-10-18). It is generated: edit the working files, never this
output. Run: python3 designs/rm-ai-build.py, then python3 designs/md-page-build.py."""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = "memos/rm-ai-reference.md"

# part title, working file, the one section to keep (None = the whole file)
PARTS = [
    ("Executive summary", "memos/rm-executive-summary.md", None),
    ("The product: The RM Assistant (short version for people)", "memos/rm-assistant.md", None),
    ("The RM Assistant in full detail", "memos/rm-assistant-detail.md", None),
    ("The plan (short version for people)", "memos/rm-plan.md", None),
    ("The full delivery plan, with every step, agent spec and workflow", "memos/rm-analytics-framework.md", None),
    ("Core use cases and outside research", "memos/use-case-library.md", "Relationship managers"),
    ("McKinsey's research in full", "memos/mckinsey-frontline-ai.md", None),
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
    dates = [re.search(r"_Last updated: ([^_]+)_", read(f)).group(1) for _, f, _ in PARTS]
    out = ["# RM Detail", "",
           "Everything about the relationship manager (RM) work at Associated Bank in one document, for an AI to read. "
           "Give this whole document to an AI model so it has the full context: the product, the plan, every step, "
           "the agent specs, the workflows and the McKinsey research (the earlier RM audit and market scan are kept as separate working files). People should read the three short pages above it in the RM section: "
           "the RM Executive Summary, RM Assistant and the RM Assistant Plan.", "",
           "> **How to read it (for the AI).** The parts below are the working files, copied in whole and in this order. "
           "Later parts give more detail on earlier ones. Lines marked ⚠️ are guesses or hypotheses to confirm at the bank; "
           "[X] marks a number not yet known: never invent a value for it. The product is a working hypothesis until Discover "
           "with the bank's RMs. Built automatically from the working files; never edit this file by hand.", ""]
    for i, (title, src, keep) in enumerate(PARTS, 1):
        out += [f"## Part {i}: {title}", "", f"Working file: `{src}`.", "", body(src, keep), ""]
    out.append(f"_Last updated: {max(dates)}_")
    open(os.path.join(ROOT, OUT), "w").write("\n".join(out) + "\n")

if __name__ == "__main__":
    build()
