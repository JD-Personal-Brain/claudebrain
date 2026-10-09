"""Builds designs/playbook.html from the playbook/*.md files, so the designed page
never drifts from the working copy. Run from anywhere: python3 designs/playbook-build.py"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PB = os.path.join(ROOT, "playbook")
E = html.escape

def inline(t):
    t = E(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = t.replace("⚠️", '<span class="warn" title="Guess about the bank: to confirm">⚠️</span>')
    return t

KINDS = {"auto": "Auto", "draft": "Draft", "me": "Me", "partner": "Partner"}
def chipify(cell):
    m = re.match(r"^(Auto|Draft|Me|Partner)\b(.*)$", cell.strip())
    if not m:
        return inline(cell)
    k = m.group(1).lower()
    return f'<span class="chip k-{k}">{m.group(1)}</span>{inline(m.group(2))}'

def render_list(lines):
    """Render indented markdown list lines (bullets or numbers) into nested HTML lists."""
    out, stack = [], []
    for ln in lines:
        m = re.match(r"^(\s*)(-|\d+\.)\s+(.*)$", ln)
        if not m:  # continuation of previous item
            out.append(" " + inline(ln.strip()))
            continue
        depth = len(m.group(1)) // 2
        tag = "ol" if m.group(2)[0].isdigit() else "ul"
        while len(stack) > depth + 1 or (len(stack) == depth + 1 and stack[-1] != tag):
            out.append(f"</li></{stack.pop()}>")
        if len(stack) == depth + 1:
            out.append("</li>")
        while len(stack) < depth + 1:
            out.append(f"<{tag}>")
            stack.append(tag)
        out.append("<li>" + inline(m.group(3)))
    while stack:
        out.append(f"</li></{stack.pop()}>")
    return "".join(out)

def render_table(lines, kinds=False):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines if not re.match(r"^\|[-|\s]+\|$", l.strip())]
    head, body = rows[0], rows[1:]
    th = "".join(f"<th>{inline(h)}</th>" for h in head)
    tb = ""
    for r in body:
        cells = []
        for i, c in enumerate(r):
            cells.append(f"<td>{chipify(c) if kinds and head[i] in ('First time', 'Aim for') else inline(c)}</td>")
        tb += "<tr>" + "".join(cells) + "</tr>"
    return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'

def render_blocks(text, kinds=False):
    """Paragraphs, lists, tables and quotes."""
    out, buf, mode = [], [], None
    def flush():
        nonlocal buf, mode
        if not buf: return
        if mode == "list": out.append(render_list(buf))
        elif mode == "table": out.append(render_table(buf, kinds))
        elif mode == "quote": out.append('<div class="note">' + inline(" ".join(l.lstrip("> ").strip() for l in buf)) + "</div>")
        else: out.append("<p>" + inline(" ".join(l.strip() for l in buf)) + "</p>")
        buf, mode = [], None
    for ln in text.split("\n"):
        if not ln.strip() or ln.strip() == "---":
            flush(); continue
        kind = "table" if ln.lstrip().startswith("|") else "quote" if ln.startswith(">") else "list" if re.match(r"^\s*(-|\d+\.)\s", ln) else ("list" if mode == "list" and ln.startswith("  ") else "para")
        if kind != mode and not (mode == "list" and kind == "para" and ln.startswith(" ")):
            flush(); mode = kind
        buf.append(ln)
    flush()
    return "".join(out)

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

readme = open(os.path.join(PB, "README.md")).read()
how = readme.split("## How every sub-step is written")[1].split("\n## ")[0]
log = readme.split("## The first-time log (fill in for every sub-step)")[1].split("\n## ")[0]
rules = readme.split("## Rules that apply to every step")[1].split("_Last updated")[0]
steps = [step(f) for f in sorted(os.listdir(PB)) if re.match(r"\d-.*\.md$", f)]
nav = '<a href="#use">How to use it</a>' + "".join(f'<a href="#step{n}"><span class="num">{n}</span>{inline(t)}</a>' for n, t, _ in steps)

CSS = """
/* Layout: navy header band, a pill nav of the six steps, then one reading column; each sub-step is a card with a two-column body. */
:root{--bg:#F4F6F8;--card:#FFFFFF;--line:#D9DEE5;--fg:#1B2433;--muted:#4D5868;--navy:#14213D;--onnavy:#FFFFFF;--onnavy-muted:#C9D3E3;--teal:#0F5F59;--teal-bg:#E1F0EE;--amber-bg:#FDF3E1;--amber:#8A4B00;--me:#14213D;--me-fg:#FFFFFF;--partner-bg:#E6E9EE;--partner:#3B4656;--label-on-navy:#8FD3CA;
--serif:"IBM Plex Serif",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0E1420;--card:#161E2C;--line:#2A3446;--fg:#E6EAF0;--muted:#A3AEBF;--navy:#0A1830;--onnavy:#FFFFFF;--onnavy-muted:#B4C1D6;--teal:#5FC4B8;--teal-bg:#123A37;--amber-bg:#3A2A10;--amber:#F2C27A;--me:#C9D6F0;--me-fg:#0E1420;--partner-bg:#2A3446;--partner:#C6CFDC;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0E1420;--card:#161E2C;--line:#2A3446;--fg:#E6EAF0;--muted:#A3AEBF;--navy:#0A1830;--onnavy:#FFFFFF;--onnavy-muted:#B4C1D6;--teal:#5FC4B8;--teal-bg:#123A37;--amber-bg:#3A2A10;--amber:#F2C27A;--me:#C9D6F0;--me-fg:#0E1420;--partner-bg:#2A3446;--partner:#C6CFDC;color-scheme:dark}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:16px;line-height:1.55}
a{color:var(--teal)}
a:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
code{font-family:var(--mono);font-size:.88em;background:var(--teal-bg);color:var(--teal);padding:1px 5px;border-radius:4px}
.band{background:var(--navy);color:var(--onnavy);padding-block:48px 36px;padding-inline:20px}
.wrap{max-width:1080px;margin:0 auto}
.label{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--teal)}
.band .label{color:var(--label-on-navy)}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(32px,5vw,46px);line-height:1.15;margin:10px 0 12px;text-wrap:balance}
.lede{font-size:18px;color:var(--onnavy-muted);max-width:66ch;margin:0}
.stepnav{display:flex;flex-wrap:wrap;gap:8px;margin-top:24px}
.stepnav a{color:var(--onnavy);text-decoration:none;border:1px solid rgba(255,255,255,.28);border-radius:999px;padding:7px 14px;font-size:14px;display:flex;gap:8px;align-items:center}
.stepnav a:hover{background:rgba(255,255,255,.08)}
.stepnav .num{color:var(--label-on-navy)}
main.wrap{padding-block:32px 64px;padding-inline:20px;display:flex;flex-direction:column;gap:56px}
h2{font-family:var(--serif);font-weight:600;font-size:34px;line-height:1.2;margin:6px 0 0;text-wrap:balance}
h3{font-family:var(--serif);font-weight:600;font-size:22px;margin:0}
h4{font-family:var(--serif);font-weight:600;font-size:20px;margin:0;text-wrap:balance}
h5{font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
p{margin:0 0 8px;max-width:72ch}
ul,ol{margin:0;padding-left:22px}
li{margin:3px 0}
.num{font-family:var(--mono);font-size:13px;color:var(--teal);font-variant-numeric:tabular-nums}
section{display:flex;flex-direction:column;gap:18px}
.use{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;min-width:0}
.stephead{border-top:4px solid var(--navy);padding-top:22px}
.meta{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:16px 0 0}
.meta div{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;min-width:0}
.meta dt{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:4px}
.meta dd{margin:0;font-size:15px}
.intro p{color:var(--muted)}
.note{background:var(--amber-bg);border-radius:8px;padding:14px 18px;font-size:15px;max-width:none}
.warn{font-size:.9em}
.toc{display:flex;flex-wrap:wrap;gap:8px}
.toc a{display:flex;gap:8px;align-items:baseline;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 12px;font-size:14px;color:var(--fg);text-decoration:none}
.toc a:hover{border-color:var(--teal)}
.sub{background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden;scroll-margin-top:16px}
.sub>header{display:flex;gap:14px;align-items:baseline;padding:16px 20px;border-bottom:1px solid var(--line)}
.sub>header .num{font-size:15px}
.subgrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:0}
.col{padding:16px 20px;display:flex;flex-direction:column;gap:12px;min-width:0}
.col.steps{border-left:1px solid var(--line)}
.col.steps ol{display:flex;flex-direction:column;gap:6px}
.fld p,.fld li{font-size:15px}
.auto{background:var(--teal-bg);padding:14px 20px;font-size:15px}
.auto h5{color:var(--teal)}
.rm{padding:12px 20px;font-size:14px;color:var(--muted);border-top:1px solid var(--line);display:flex;gap:10px;flex-wrap:wrap;align-items:baseline}
.rm p{margin:0}
.rmlabel{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--amber);background:var(--amber-bg);padding:2px 8px;border-radius:4px;white-space:nowrap}
.gate{background:var(--navy);color:var(--onnavy);border-radius:8px;padding:22px 24px;display:flex;flex-direction:column;gap:8px}
.gate .label{color:var(--label-on-navy)}
.gate h3{color:var(--onnavy)}
.gate li{color:var(--onnavy-muted)}
.gate strong{color:var(--onnavy)}
.review{display:flex;flex-direction:column;gap:10px}
.review>p{color:var(--muted);font-size:15px}
.tw{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:8px}
table{width:100%;border-collapse:collapse;font-size:15px;min-width:600px}
th{text-align:left;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:10px 16px;border-bottom:1px solid var(--line)}
td{padding:10px 16px;border-bottom:1px solid var(--line);vertical-align:top}
tr:last-child td{border-bottom:0}
.chip{display:inline-block;font-family:var(--mono);font-size:12px;padding:2px 9px;border-radius:999px;white-space:nowrap;font-weight:500;margin-right:4px}
.k-auto{background:var(--teal-bg);color:var(--teal)}
.k-draft{background:var(--amber-bg);color:var(--amber)}
.k-me{background:var(--me);color:var(--me-fg)}
.k-partner{background:var(--partner-bg);color:var(--partner)}
footer{color:var(--muted);font-size:14px;border-top:1px solid var(--line);padding-top:16px}
@media (max-width:760px){.subgrid,.use,.meta{grid-template-columns:1fr}.col.steps{border-left:0;border-top:1px solid var(--line)}}
"""

page = f'''<title>Delivery Playbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}</style>
<div class="band"><div class="wrap">
<span class="label">Field manual · AI product delivery</span>
<h1>Delivery Playbook</h1>
<p class="lede">How to run each of the six steps the first time, sub-step by sub-step, and what to watch so the second time can be automated. It sits under the delivery machine: that page says what happens; this one says how.</p>
<nav class="stepnav" aria-label="Steps">{nav}</nav>
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
<footer>Draft, 2026-10-09. Built from the working copy in <code>playbook/</code>; lines marked ⚠️ are guesses about the bank, and [X] marks numbers still to be set. Kinds: <span class="chip k-auto">Auto</span> runs on its own · <span class="chip k-draft">Draft</span> AI drafts, a person checks · <span class="chip k-me">Me</span> only a person · <span class="chip k-partner">Partner</span> a named partner's sign-off.</footer>
</main>
'''
open(os.path.join(ROOT, "designs", "playbook.html"), "w").write(page)
