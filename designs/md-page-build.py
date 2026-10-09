"""Builds branded pages from working-copy Markdown files that I read, so each
page always matches its file (rule R16). Run: python3 designs/md-page-build.py
To add a page: add a line to PAGES, run this, publish the new .html, and list
it in designs/README.md."""
import os, re
from pagekit import CSS, E, inline, render_blocks

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# source file, output page, page name, eyebrow label, one-line summary
PAGES = [
    ("product-framework.md", "product-framework.html", "Product Framework", "How I organize product work",
     "The six steps every product goes through, the delivery machine that runs them, and the rules that keep it governed."),
    ("tech-stack.md", "tech-stack.html", "Tech Stack Guide", "Associated Bank · technology guide",
     "Each technology in the job: what it is, how the bank likely uses it, and what I need to know."),
    ("job-notes.md", "job-notes.html", "Job Notes", "Associated Bank · thinking through the job",
     "My answers so far, part by part, so any session can pick up where I stopped."),
    ("job-description.md", "job-description.html", "Job Description", "Associated Bank · the role",
     "The Principal Applied AI Product Manager posting: what the role owns, what it requires, and the tools it names."),
    ("prompting.md", "prompting.html", "Prompting Guide", "Working with Claude",
     "How we write prompts: Anthropic's advice in plain English, a fill-in template, worked examples and a checklist."),
]

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40]

def build(src, out, name, label, lede):
    s = open(os.path.join(ROOT, src)).read()
    title = re.match(r"^# (.+)$", s, re.M).group(1)
    updated = re.search(r"_Last updated: ([^_]+)_", s)
    s = re.sub(r"\n_Last updated: [^_]+_\s*$", "", s.strip())
    body = s.split("\n", 1)[1]
    parts = re.split(r"\n## ", "\n" + body)
    intro, sections = parts[0], parts[1:]
    nav, secs = [], []
    for sec in sections:
        head, _, text = sec.partition("\n")
        sid = slug(head)
        nav.append(f'<a href="#{sid}">{inline(head)}</a>')
        secs.append(f'<section id="{sid}"><div class="stephead"><h2>{inline(head)}</h2></div>'
                    f'<div class="mdbody">{render_blocks(text, kinds=True)}</div></section>')
    page = f'''<title>{E(name)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
.mdbody{{display:flex;flex-direction:column;gap:12px}}
.mdbody>ul,.mdbody>ol{{max-width:78ch}}
.mdbody li{{margin:4px 0}}
.intro-block{{display:flex;flex-direction:column;gap:12px}}
</style>
<div class="band"><div class="wrap">
<span class="label">{E(label)}</span>
<h1>{inline(title)}</h1>
<p class="lede">{E(lede)}</p>
<nav class="stepnav" aria-label="Sections">{"".join(nav)}</nav>
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
