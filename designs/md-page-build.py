"""Builds branded pages from working-copy Markdown files that I read, so each
page always matches its file (rule R16). Run: python3 designs/md-page-build.py
To add a page: add a line to PAGES, run this, publish the new .html, and list
it in designs/README.md."""
import os, re
from pagekit import CSS, E, inline, render_blocks, series, SERIES_CSS

# Pages whose ### headings get ids, so other pages can link straight to them (RM Detail: the plan links into it).
ANCHORED = {"memos/rm-ai-reference.md"}

# Pages that are one of the four "How we deliver" pages get the reading-order strip.
SERIES_KEY = {"product-framework.md": "framework"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# source file, output page, page name, eyebrow label, one-line summary
PAGES = [
    ("product-framework.md", "product-framework.html", "Product Framework", "How we deliver",
     "The rules every product follows: who decides, how success is measured, how good is good enough, how we use AI, and how each step is written up."),
    ("tech-stack.md", "tech-stack.html", "Tech Stack Guide", "Associated Bank · technology guide",
     "Each technology in the job: what it is, how the bank likely uses it, and what I need to know."),
    ("job-description.md", "job-description.html", "Job Description", "Associated Bank · the role",
     "The Principal Applied AI Product Manager posting: what the role owns, what it requires, and the tools it names."),
    ("open-items.md", "open-items.html", "Open Items", "Where things stand",
     "Everything still open in one log: decisions and reviews waiting on me, work to do, questions for the bank, and what's parked."),
    ("memos/bank-business.md", "bank-business.html", "Bank Business Briefing", "Associated Bank · the business",
     "How the bank earns money, the corporate segment in depth, and where AI work lines up with each revenue line."),
    ("prompting.md", "prompting.html", "Prompting Guide", "Working with Claude",
     "How we write prompts: Anthropic's advice in plain English, a fill-in template, three worked examples and a checklist."),
    ("prompt-library.md", "prompt-library.html", "Prompt Library", "Working with Claude",
     "Our core prompts in one place, each with its version and what changed, so we can reuse them and improve them over time."),
    ("memos/use-case-library.md", "use-case-library.html", "Use Case Library", "Reference · use cases",
     "Where the value of AI is for each group of bankers we serve, and the outside research behind it: relationship managers (RMs) and portfolio managers (PMs).",
     {"Relationship managers": "Relationship managers", "Portfolio managers": "Portfolio managers"}),
    ("memos/rm-plan.md", "rm-analytics-plan.html", "RM Assistant Plan", "Relationship managers · the plan",
     "How The RM Assistant gets delivered: wave 1 in about six weeks, what sets the pace, who decides, how we prove the value, the risks and what to confirm.",
     {"The plan at a glance": "At a glance", "1. Wave 1 in about six weeks": "Wave 1", "2. What sets the pace": "Pace", "3. Who decides": "Who decides",
      "4. How we'll prove the value": "Value", "5. Top risks": "Risks", "6. What I'd confirm in the first weeks": "To confirm"}),
    ("memos/rm-ai-reference.md", "rm-ai-reference.html", "RM Detail", "Relationship managers · the detail, for AI to read",
     "Everything about the RM work in one document, built from the working files, to give an AI the full picture. People read the shorter RM pages.",
     {"Part 1: Executive summary": "1 Summary", "Part 2: The product: RM Assistant (short version for people)": "2 Product", "Part 3: The RM Assistant in full detail": "3 Product detail",
      "Part 4: The plan (short version for people)": "4 Plan", "Part 5: The full delivery plan, with every step, agent spec and workflow": "5 Full plan",
      "Part 6: Core use cases and outside research": "6 Use cases", "Part 7: McKinsey's research in full": "7 McKinsey"}),
    ("memos/rm-executive-summary.md", "rm-executive-summary.html", "RM Executive Summary", "Relationship managers · executive summary",
     "The RM work on one page, for the leaders of the RM business: the problem, the product, what RMs get first, the value, how fast, and what I need.",
     {"The product: The RM Assistant": "The product", "What RMs get first (wave 1)": "Wave 1", "What I need from you": "What I need"}),
    ("memos/rm-assistant.md", "rm-assistant.html", "RM Assistant", "Relationship managers · the product",
     "One AI assistant for each RM: its limits, its capabilities by moment in the RM's work and the core use case each answers, and what it's built on.",
     {"The product in one line": "The product", "1. Its limits": "Limits", "2. Capabilities, by moment in the RM's work": "Capabilities",
      "3. What it's built on": "Foundation"}),
    ("memos/credit-market-scan.md", "credit-market-scan.html", "Portfolio Manager Core Use Cases", "Portfolio managers · core use cases",
     "What banks are deploying in commercial credit, and the credit counterpart of each of the seven core use cases."),
    ("memos/elon-mode-research.md", "elon-mode.html", "Elon Mode", "Research · how Musk builds and improves systems",
     "The main ideas Elon Musk is known for in engineering, business and process improvement, how sure we are of each, where they went wrong, our read of his model, and the eight changes we made to our own system."),
    ("memos/audit-log.md", "audit-log.html", "Audit Log", "Reference · audit",
     "How we audit our work: the method, every check and when it runs, the record of every audit so far, and what to improve."),
    ("glossary.md", "glossary.html", "Glossary", "Reference · the words we use",
     "One meaning for each word in every plan, playbook page and agent spec, plus the bank's terms still to map."),
]

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40]

def build(src, out, name, label, lede, short=None):
    s = open(os.path.join(ROOT, src)).read()
    title = re.match(r"^# (.+)$", s, re.M).group(1)
    updated = re.search(r"_Last updated: ([^_]+)_", s)
    s = re.sub(r"\n_Last updated: [^_]+_\s*$", "", s.strip())
    body = s.split("\n", 1)[1]
    parts = re.split(r"\n## ", "\n" + body)
    intro, sections = parts[0], parts[1:]
    key = SERIES_KEY.get(src)
    if key:  # the strip in the header replaces the working copy's "Page N of the four" list
        lines, keep, skipping = intro.split("\n"), [], False
        for ln in lines:
            if re.match(r"Page \d of the four", ln): skipping = True; continue
            if skipping and (re.match(r"\d\. ", ln) or not ln.strip() and not keep[-1:] == [""]):
                continue
            skipping = False; keep.append(ln)
        intro = "\n".join(keep).strip()
    nav, secs = [], []
    for sec in sections:
        head, _, text = sec.partition("\n")
        sid = slug(head)
        nav.append(f'<a href="#{sid}">{inline((short or {}).get(head, head))}</a>')
        secs.append(f'<section id="{sid}"><div class="stephead"><h2>{inline(head)}</h2></div>'
                    f'<div class="mdbody">{render_blocks(text, kinds=True, anchor=sid if src in ANCHORED else None)}</div></section>')
    page = f'''<title>{E(name)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
.mdbody{{display:flex;flex-direction:column;gap:12px}}
.mdbody>ul,.mdbody>ol{{max-width:78ch}}
.mdbody li{{margin:4px 0}}
.intro-block{{display:flex;flex-direction:column;gap:12px}}{SERIES_CSS if key else ""}
</style>
<div class="band"><div class="wrap">
<span class="label">{E(label)}</span>
<h1>{inline(title)}</h1>
<p class="lede">{E(lede)}</p>
<nav class="stepnav" aria-label="Sections">{"".join(nav)}</nav>{series(key) if key else ""}
</div></div>
<main class="wrap">
<div class="intro-block">{render_blocks(intro, kinds=True)}</div>
{"".join(secs)}
<footer>Built from the working copy <code>{E(src)}</code>{f" · last updated {E(updated.group(1))}" if updated else ""}. Lines marked ⚠️ are guesses to confirm; [X] marks numbers still to be set.</footer>
</main>
'''
    open(os.path.join(ROOT, "designs", out), "w").write(page)

for p in PAGES:
    build(*p)
