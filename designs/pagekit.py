"""Shared page kit: turns the house-style Markdown used in this repo into
branded HTML. Used by playbook-build.py and md-page-build.py."""
import html, re
E = html.escape

def inline(t):
    t = E(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
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
    KIND_COLS = ('First time', 'Aim for', 'Kind')
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines if not re.match(r"^\|[-|\s]+\|$", l.strip())]
    head, body = rows[0], rows[1:]
    th = "".join(f"<th>{inline(h)}</th>" for h in head)
    tb = ""
    for r in body:
        cells = []
        for i, c in enumerate(r):
            cells.append(f"<td>{chipify(c) if kinds and head[i] in KIND_COLS else inline(c)}</td>")
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
    fence = None
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            if fence is None:
                flush(); fence = []
            else:
                out.append('<pre class="diagram">' + E("\n".join(fence)) + "</pre>"); fence = None
            continue
        if fence is not None:
            fence.append(ln); continue
        h = re.match(r"^(#{3,4}) (.+)$", ln)
        if h:
            flush(); out.append(f"<h{len(h.group(1))} class=\"md-h\">{inline(h.group(2))}</h{len(h.group(1))}>"); continue
        if not ln.strip() or ln.strip() == "---":
            flush(); continue
        kind = "table" if ln.lstrip().startswith("|") else "quote" if ln.startswith(">") else "list" if re.match(r"^\s*(-|\d+\.)\s", ln) else ("list" if mode == "list" and ln.startswith("  ") else "para")
        if kind != mode and not (mode == "list" and kind == "para" and ln.startswith(" ")):
            flush(); mode = kind
        buf.append(ln)
    flush()
    return "".join(out)


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
.agents{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.agent{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:18px 20px;display:flex;flex-direction:column;gap:10px;min-width:0;scroll-margin-top:16px}
.agent header{display:flex;flex-wrap:wrap;gap:6px 12px;align-items:baseline}
.agent .used{font-family:var(--mono);font-size:12px;color:var(--muted);margin-left:auto}
.agent .job{margin:0;font-size:16px}
.kindrow{font-size:14px;color:var(--muted)}
.spec{margin:0;display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line);padding-top:10px}
.spec div{display:grid;grid-template-columns:140px minmax(0,1fr);gap:10px}
.spec dt{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:3px}
.spec dd{margin:0;font-size:14px}
pre.diagram{font-family:var(--mono);font-size:13px;line-height:1.5;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px 18px;overflow-x:auto;margin:0}
.md-h{margin:8px 0 2px}
footer{color:var(--muted);font-size:14px;border-top:1px solid var(--line);padding-top:16px}
@media (max-width:760px){.subgrid,.use,.meta,.agents{grid-template-columns:1fr}.spec div{grid-template-columns:1fr;gap:2px}.col.steps{border-left:0;border-top:1px solid var(--line)}}
"""


# ---------- The four "How we deliver" pages, in reading order ----------
# Each of the four pages shows this strip in its header, so they read as one set.
SERIES = [
    ("workflow", "Product Workflow", "The steps and their gates", "https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv"),
    ("framework", "Product Framework", "The rules every product follows", "https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ"),
    ("machine", "Product Machine", "Every task, marked by who does it", "https://claude.ai/artifact/S8Wbygy24cjguTMxZsN2QF"),
    ("playbook", "Product Playbook", "How to do each sub-step", "https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4"),
]
SERIES_CSS = """
.series{margin-top:22px;display:flex;flex-direction:column;gap:8px}
.series .stitle{font-family:var(--mono,monospace);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.series ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.series li a,.series li span.here{display:flex;flex-direction:column;gap:2px;height:100%;box-sizing:border-box;padding:10px 12px;border-radius:6px;border:1px solid rgba(255,255,255,.28);color:#fff;text-decoration:none;font-size:14px;line-height:1.3}
.series li a:hover{background:rgba(255,255,255,.1)}
.series li span.here{background:#fff;color:#14213D;border-color:#fff}
.series b{font-weight:600}
.series small{font-size:12.5px;opacity:.8}
.series .sn{font-family:var(--mono,monospace);font-size:12px;opacity:.75}
@media (max-width:720px){.series ol{grid-template-columns:repeat(2,minmax(0,1fr))}}
"""

def series(current):
    """The 'How we deliver' strip: four numbered tiles, the current page highlighted."""
    items = []
    for i, (key, name, what, url) in enumerate(SERIES, 1):
        inner = f'<span class="sn">{i} of 4</span><b>{E(name)}</b><small>{E(what)}</small>'
        if key == current:
            items.append(f'<li><span class="here" aria-current="page">{inner}</span></li>')
        else:
            items.append(f'<li><a href="{url}" target="_blank" rel="noopener">{inner}</a></li>')
    return f'<nav class="series" aria-label="How we deliver, in reading order"><span class="stitle">How we deliver · read in this order</span><ol>{"".join(items)}</ol></nav>'

# The three pages that show the six steps, each with one job; they link to each other.
WORKFLOW_URL = "https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv"   # Product Workflow: the steps and their gates
STEPS_URL = "https://claude.ai/artifact/8UncWMYUq7hsJUhn5NSYEB"      # Steps Catalog: look up any sub-step
MAPS_URL = "https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX"       # Workflow Maps: the processes as clickable maps
PLAYBOOK_URL = "https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4"   # Product Playbook: how to do each sub-step

def six_steps():
    """The six steps from the Product Workflow's working copy (memos/role-workflow.md), its one home:
    {"1": {"name", "question", "governance", "gate"}, ...}. Builders read them here so no page keeps its own copy."""
    import os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    text = open(os.path.join(root, "memos", "role-workflow.md")).read()
    out = {}
    for m in re.finditer(r"^\| (\d)\. ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", text, re.M):
        out[m.group(1)] = {"name": m.group(2).strip(), "question": m.group(3).strip(),
                           "governance": m.group(4).strip(), "gate": m.group(5).strip()}
    if sorted(out) != list("123456"):
        raise SystemExit("Could not read the six steps from memos/role-workflow.md")
    return out
