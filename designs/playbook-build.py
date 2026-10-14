"""Builds designs/playbook.html from the playbook/*.md files, so the designed page
never drifts from the working copy. Run from anywhere: python3 designs/playbook-build.py"""
import html, os, re
from pagekit import E, inline, chipify, render_list, render_table, render_blocks

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PB = os.path.join(ROOT, "playbook")

FIELDS = ["Goal", "Why it matters", "Know first", "First time, step by step", "Output", "Done when", "Automation watch", "For RM analytics"]
def parse_fields(body):
    fields, cur = {}, None
    for ln in body.split("\n"):
        m = re.match(r"^- \*\*([^*]+):\*\*\s*(.*)$", ln)
        if m and m.group(1) in FIELDS:
            cur = m.group(1); fields[cur] = {"text": m.group(2), "sub": []}
        elif cur and ln.startswith("  "):
            fields[cur]["sub"].append(ln[2:])
    return fields

def field_html(f):
    raw = f["text"][:1].upper() + f["text"][1:] if f["text"] else ""
    t = inline(raw) if raw else ""
    return (f"<p>{t}</p>" if t else "") + (render_list(f["sub"]) if f["sub"] else "")

def substep(num, title, body):
    f = parse_fields(body)
    missing = [k for k in FIELDS if k not in f]
    if missing:
        raise SystemExit(f"{num} is missing fields: {missing}")
    left = "".join(f'<div class="fld"><h5>{k}</h5>{field_html(f[k])}</div>' for k in ["Goal", "Why it matters", "Know first", "Output", "Done when"])
    return f'''<article class="sub" id="s{num.replace('.', '-')}">
<header><span class="num">{num}</span><h4>{inline(title)}</h4></header>
<div class="subgrid"><div class="col">{left}</div>
<div class="col steps"><h5>First time, step by step</h5>{field_html(f["First time, step by step"])}</div></div>
<div class="auto"><h5>Automation watch</h5>{field_html(f["Automation watch"])}</div>
<div class="rm"><span class="rmlabel">For RM analytics</span> {field_html(f["For RM analytics"])}</div>
</article>'''

def step(fn):
    s = open(os.path.join(PB, fn)).read()
    n = fn[0]
    title = re.match(r"# Step \d: (.+?), the first time", s).group(1)
    q = re.search(r"\*\*The question:\*\* (.+)", s).group(1)
    g = re.search(r"\*\*The gate:\*\* (.+)", s).group(1)
    gov = re.search(r"\*\*Governance thread:\*\* (.+)", s).group(1)
    parts = re.split(r"\n## ", s)
    intro = parts[0].split(gov, 1)[1]
    html_parts = [f'''<section class="step" id="step{n}">
<div class="stephead"><span class="label">Step {n} of 6</span><h2>{inline(title)}</h2>
<dl class="meta"><div><dt>The question</dt><dd>{inline(q)}</dd></div><div><dt>The gate</dt><dd>{inline(g)}</dd></div><div><dt>Governance thread</dt><dd>{inline(gov)}</dd></div></dl></div>
<div class="intro">{render_blocks(intro)}</div>''']
    subs = []
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        m = re.match(r"^(\d\.\d) (.+)$", head)
        if m:
            subs.append((m.group(1), m.group(2)))
            html_parts.append(substep(m.group(1), m.group(2), body))
        elif head.startswith("The ") and "gate" in head:
            html_parts.append(f'<div class="gate"><span class="label">Go / no-go</span><h3>{inline(head)}</h3>{render_blocks(body)}</div>')
        elif "automation review" in head:
            body = re.sub(r"\n_Last updated.*", "", body)
            html_parts.append(f'<div class="review"><h3>{inline(head)}</h3>{render_blocks(body, kinds=True)}</div>')
    html_parts.append("</section>")
    toc = "".join(f'<a href="#s{a.replace(".", "-")}"><span class="num">{a}</span>{inline(b)}</a>' for a, b in subs)
    html_parts.insert(1, f'<nav class="toc" aria-label="Sub-steps in {E(title)}">{toc}</nav>')
    return n, title, "".join(html_parts)


AGENT_LIBRARY_URL = "https://claude.ai/artifact/Cn9nANQoqp2BP7yrmy61zn"

def agent_library():
    """A short summary of the general agents. Their full specs live on the Agent Library page."""
    s = open(os.path.join(PB, "agents.md")).read()
    agents = []
    for block in re.split(r"\n### ", s)[1:]:
        head, _, body = block.partition("\n")
        m = re.match(r"(M\d+)\. (.+)", head)
        if not m:
            continue
        used = re.search(r"^- \*\*Used in:\*\*\s*(.*)$", body, re.M).group(1)
        agents.append((int(m.group(1)[1:]), m.group(1), m.group(2), used))
    groups = [("Run the machine", "M1 to M19 handle the paperwork and routing that move a project through the six steps: kickoff, notes, gate packs, sign-offs and releases.", [a for a in agents if a[0] <= 19]),
              ("Do the team's analysis, testing and monitoring", "M20 to M33 size opportunities, draft requirements, check data, test, red-team, watch fairness and quality, and measure impact.", [a for a in agents if a[0] >= 20])]
    cols = "".join(f'<div class="agroup"><h3>{E(t)}</h3><p>{E(why)}</p><ul class="alist">'
                   + "".join(f'<li><span class="aid">{aid}</span><span class="aname">{inline(name)}</span><span class="aused">{inline(used)}</span></li>' for _, aid, name, used in items)
                   + "</ul></div>" for t, why, items in groups)
    return f'''<section id="agents"><div class="stephead"><span class="label">Agents</span><h2>The agents that run the machine</h2></div>
<p>{len(agents)} general agents do the routine work in the steps above, on every project. Each one has one job, a short list of allowed actions and a named person in charge. This is the short list, with the sub-steps where each is used; the full spec of every agent (what starts it, what it may and may not do, when it stops and who checks it) is on the Agent Library page.</p>
<div class="agroups">{cols}</div>
<p><a class="golib" href="{AGENT_LIBRARY_URL}" target="_blank" rel="noopener">Open the Agent Library for every agent's full spec →</a></p></section>'''

readme = open(os.path.join(PB, "README.md")).read()
how = readme.split("## How every sub-step is written")[1].split("\n## ")[0]
log = readme.split("## The first-time log (fill in for every sub-step)")[1].split("\n## ")[0]
rules = readme.split("## Rules that apply to every step")[1].split("_Last updated")[0]
steps = [step(f) for f in sorted(os.listdir(PB)) if re.match(r"\d-.*\.md$", f)]
nav = '<a href="#use">How to use it</a>' + "".join(f'<a href="#step{n}"><span class="num">{n}</span>{inline(t)}</a>' for n, t, _ in steps) + '<a href="#agents">Agents</a>'

from pagekit import CSS, series, SERIES_CSS


page = f'''<title>Product Playbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}{SERIES_CSS}
.agroups{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.agroup{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:10px}}
.agroup h3{{font-size:18px;margin:0}}
.agroup p{{color:var(--muted);font-size:15px;margin:0}}
.alist{{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}}
.alist li{{display:grid;grid-template-columns:44px 1fr auto;gap:8px;align-items:baseline;padding:6px 0;border-top:1px solid var(--line);font-size:15px}}
.alist .aid{{font-family:var(--mono);font-size:13px;color:var(--muted)}}
.alist .aused{{font-family:var(--mono);font-size:12.5px;color:var(--muted);text-align:right}}
.golib{{display:inline-block;padding:10px 16px;border-radius:6px;background:var(--navy);color:var(--onnavy);text-decoration:none;font-weight:600}}
@media (max-width:720px){{.agroups{{grid-template-columns:1fr}}}}
</style>
<div class="band"><div class="wrap">
<span class="label">How we deliver</span>
<h1>Product Playbook</h1>
<p class="lede">How to run each of the six steps the first time, sub-step by sub-step, and what to watch so the second time can be automated. The Product Workflow says what happens, the Product Machine says who does each task; this page says how. A short list of the agents closes the page; their full specs are on the Agent Library.</p>
<nav class="stepnav" aria-label="Steps">{nav}</nav>
{series("playbook")}
</div></div>
<main class="wrap">
<section id="use">
<span class="label">How to use it</span>
<h2>Work through each sub-step, and log it as you go</h2>
<p>Open the step you're in and work through its sub-steps in order. Each one has the same parts, so any step reads like any other. Fill in the first-time log as you go: you can't automate work you never wrote down.</p>
<div class="use">
<div class="panel"><h5>Every sub-step has</h5>{render_blocks(how)}</div>
<div class="panel"><h5>Rules for every step</h5>{render_blocks(rules)}</div>
</div>
<div><h3 style="margin-bottom:10px">The first-time log</h3>{render_blocks(log)}</div>
</section>
{"".join(h for _, _, h in steps)}
{agent_library()}
<footer>In use: all six steps reviewed 2026-10-14. Built from the working copy in <code>playbook/</code>; lines marked ⚠️ are guesses about the bank, and [X] marks numbers still to be set. Kinds: <span class="chip k-auto">Auto</span> runs on its own · <span class="chip k-draft">Draft</span> AI drafts, a person checks · <span class="chip k-me">Me</span> only a person · <span class="chip k-partner">Partner</span> a named partner's sign-off.</footer>
</main>
'''
open(os.path.join(ROOT, "designs", "playbook.html"), "w").write(page)
