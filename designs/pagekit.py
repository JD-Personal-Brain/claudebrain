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

def render_blocks(text, kinds=False, anchor=None):
    """Paragraphs, lists, tables and quotes. With anchor, ### and #### headings get an id
    (anchor + "-" + the heading as a slug), so other pages can link straight to them."""
    out, buf, mode = [], [], None
    def flush():
        nonlocal buf, mode
        if not buf: return
        if mode == "list": out.append(render_list(buf))
        elif mode == "table": out.append(render_table(buf, kinds))
        elif mode == "quote": out.append('<div class="note">' + inline(" ".join(l.lstrip("> ").strip() for l in buf)) + "</div>")
        else: out.append("<p>" + inline(" ".join(l.strip() for l in buf)) + "</p>")
        buf, mode = [], None
    fence, lang = None, ""
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            if fence is None:
                flush(); fence = []; lang = ln.strip()[3:].strip()
            else:
                out.append(render_gantt(fence) if lang == "gantt" else '<pre class="diagram">' + E("\n".join(fence)) + "</pre>"); fence = None
            continue
        if fence is not None:
            fence.append(ln); continue
        h = re.match(r"^(#{3,4}) (.+)$", ln)
        if h:
            hid = f' id="{anchor}-{re.sub(r"[^a-z0-9]+", "-", h.group(2).lower()).strip("-")[:40]}"' if anchor else ""
            flush(); out.append(f"<h{len(h.group(1))} class=\"md-h\"{hid}>{inline(h.group(2))}</h{len(h.group(1))}>"); continue
        if not ln.strip() or ln.strip() == "---":
            flush(); continue
        kind = "table" if ln.lstrip().startswith("|") else "quote" if ln.startswith(">") else "list" if re.match(r"^\s*(-|\d+\.)\s", ln) else ("list" if mode == "list" and ln.startswith("  ") else "para")
        if kind != mode and not (mode == "list" and kind == "para" and ln.startswith(" ")):
            flush(); mode = kind
        buf.append(ln)
    flush()
    return "".join(out)


GANTT_CSS = """.gantt{padding:12px 16px}.ginner{min-width:620px;display:flex;flex-direction:column;gap:6px}.grow{display:grid;grid-template-columns:230px 1fr;gap:12px;align-items:center;font-size:14px}.glab{line-height:1.3}.gtrack{position:relative;height:18px;background:repeating-linear-gradient(90deg,transparent 0,transparent calc(100%/13 - 1px),var(--line) calc(100%/13 - 1px),var(--line) calc(100%/13))}.gweeks{display:grid;grid-template-columns:repeat(13,1fr);background:none;height:auto;font-family:var(--mono);font-size:11px;color:var(--muted)}.gw{text-align:center}.ghead{border-bottom:1px solid var(--line);padding-bottom:4px}.gbar{position:absolute;top:3px;height:12px;border-radius:3px;display:inline-block}.g-build{background:var(--amber)}.g-live{background:var(--teal)}.g-ongoing{background:repeating-linear-gradient(45deg,var(--teal) 0 6px,var(--teal-bg) 6px 12px)}.gdia{position:absolute;top:2px;width:14px;height:14px;background:var(--me);transform:rotate(45deg);display:inline-block}.gmore{font-size:12px;white-space:nowrap}.gkey{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:13px;color:var(--muted);margin-top:6px}.gkey span{display:flex;align-items:center;gap:6px}.gkey i{position:static;width:22px;height:10px}.gkey i.gdia{width:10px;height:10px;transform:rotate(45deg)}"""

def render_gantt(lines):
    """A ```gantt block: one row per line, "Label | start week | end week | kind" (kind: build, live, gate,
    ongoing), and optionally "| link" to the detail behind the row. A gate is a diamond at its start week. The first line "weeks N" sets the axis length."""
    n = 13; rows = []
    for ln in lines:
        ln = ln.strip()
        if not ln: continue
        if ln.startswith("weeks "): n = int(ln.split()[1]); continue
        f = [x.strip() for x in ln.split("|")]
        rows.append((f[0], float(f[1]), float(f[2]), f[3], f[4] if len(f) > 4 else ""))
    head = "".join(f'<span class="gw">{w}</span>' for w in range(1, n + 1))
    body = ""
    for lab, a, b, k, url in rows:
        left = a / n * 100
        if k == "gate":
            bar = f'<span class="gdia" style="left:calc({left:.2f}% - 7px)"></span>'
        else:
            bar = f'<span class="gbar g-{k}" style="left:{left:.2f}%;width:{(b - a) / n * 100:.2f}%"></span>'
        more = f' <a class="gmore" href="{E(url)}" target="_blank" rel="noopener" title="Open the detail">detail&nbsp;↗</a>' if url else ""
        body += f'<div class="grow"><span class="glab">{inline(lab)}{more}</span><span class="gtrack">{bar}</span></div>'
    key = ('<div class="gkey"><span><i class="gbar g-build"></i>Build and test</span><span><i class="gbar g-live"></i>Live with pilot users</span>'
           '<span><i class="gbar g-ongoing"></i>Ongoing</span><span><i class="gdia"></i>Gate (go/no-go)</span></div>')
    return (f'<style>{GANTT_CSS}</style><div class="tw gantt"><div class="ginner"><div class="grow ghead"><span class="glab">Week</span><span class="gtrack gweeks">{head}</span></div>'
            f'{body}</div></div>{key}')

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
# The three pages that show the six steps, each with one job; they link to each other.
WORKFLOW_URL = "https://claude.ai/artifact/8Nm5fkdicn2Gu5VmNVTvYv"   # Product Workflow: the steps and their gates
STEPS_URL = "https://claude.ai/artifact/8UncWMYUq7hsJUhn5NSYEB"      # Steps Catalog: look up any sub-step
MAPS_URL = "https://claude.ai/artifact/CPLGBN1h9wdr3yP673PqyX"       # Workflow Maps: the processes as clickable maps
PLAYBOOK_URL = "https://claude.ai/artifact/YPEZ2F4Zp4bYUDmeQPzef4"   # Product Playbook: how to do each sub-step

SERIES = [
    ("workflow", "Product Workflow", "The steps and their gates", WORKFLOW_URL),
    ("framework", "Product Framework", "The rules every product follows", "https://claude.ai/artifact/HJnqf9A7R2jQ5iEZCYpMaZ"),
    ("machine", "Product Machine", "Every task, marked by who does it", "https://claude.ai/artifact/S8Wbygy24cjguTMxZsN2QF"),
    ("playbook", "Product Playbook", "How to do each sub-step", PLAYBOOK_URL),
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


# ---------- Cross-links (added 2026-10-18, from the deep audit and Elon mode review) ----------
# Every built page links its references automatically, so no link has to be added by hand:
# control numbers (K1 to K25) to their card in the Controls Catalog, agent numbers (M1 to M33,
# A1 to A11 as they exist, H1) to their card in the Agent Library, workflow numbers (B1 to B16) to their card
# on the Workflow Maps, sub-step numbers (1.0 to 6.6, when written "sub-step 2.4", "(2.4", "at 2.4" or
# "in 2.4") to their card in the Steps Catalog, and page names to their page. The links
# come from the page list in designs/README.md, so a page's address lives in one place. Text inside
# links, code, headings, card summaries and table headers is left alone.
import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
def _page_urls():
    urls = {}
    for m in re.finditer(r"\| *([^|]+?) *\| *(https://claude\.ai/artifact/\w+) *\| *`([^`]+)`", open(_os.path.join(_ROOT, "designs", "README.md")).read()):
        urls[m.group(3)] = m.group(2)  # the full source path, so two prototypes both named prototype-v1.html stay apart
        urls.setdefault(_os.path.basename(m.group(3)), m.group(2))
    return urls
PAGE_NAMES = [  # name as people write it -> the page's built file
    ("Controls Catalog", "controls.html"), ("Agent Library", "agents.html"), ("Steps Catalog", "steps.html"),
    ("Workflow Maps", "workflows.html"), ("Use Case Library", "use-case-library.html"), ("RM Detail", "rm-ai-reference.html"),
    ("RM Assistant Plan", "rm-analytics-plan.html"), ("RM Assistant Prototype", "prototypes/rm-assistant/prototype-v5.html"), ("RM Executive Summary", "rm-executive-summary.html"),
    ("PM Detail", "pm-ai-reference.html"), ("PM Assistant Plan", "pm-assistant-plan.html"), ("PM Assistant Prototype", "prototypes/pm-assistant/prototype-v5.html"),
    ("PM Executive Summary", "pm-executive-summary.html"),
    ("Product Workflow", "role-workflow.html"), ("Product Framework", "product-framework.html"), ("Product Machine", "product-machine.html"),
    ("Product Playbook", "playbook.html"), ("Elon Mode", "elon-mode.html"), ("Glossary", "glossary.html"), ("Bank Business Briefing", "bank-business.html"),
    ("Tech Stack Guide", "tech-stack.html"), ("Prompt Library", "prompt-library.html"), ("Prompting Guide", "prompting.html"),
    ("Open Items", "open-items.html"), ("The RM Assistant", "rm-assistant.html"), ("The PM Assistant", "pm-assistant.html"),
    ("Audit Log", "audit-log.html"), ("Document Library", "library.html"), ("Job Description", "job-description.html")]
# The sub-steps that exist (1.0 to 6.6), read from the playbook so the list can't drift from it.
SUBSTEPS = set(re.findall(r"^## (\d\.\d) ", "".join(open(f).read() for f in sorted(__import__("glob").glob(_os.path.join(_ROOT, "playbook", "[1-6]-*.md")))), re.M))
_SUB_NO_LINK = {"steps.html", "playbook.html"}  # these pages hold the sub-steps themselves
_SKIP = {"a", "code", "pre", "script", "style", "title", "summary", "th", "h1", "nav", "button", "label", "select", "option"}
def link_refs(page, here):
    """here: this page's built file name (links to itself become in-page jumps)."""
    urls = _page_urls()
    def target(fname, anchor=""):
        if fname == here: return "#" + anchor if anchor else None
        u = urls.get(fname)
        return (u + ("#" + anchor if anchor else "")) if u else None
    names = sorted(PAGE_NAMES, key=lambda x: -len(x[0]))
    name_re = re.compile(r"\b(" + "|".join(re.escape(n) for n, _ in names) + r")\b")
    # A full stop after a code still links it ("control K3."), but "K3.5"-style tokens don't.
    code_re = re.compile(r"(?<![\w.$-])(K(?:2[0-5]|1\d|[1-9])|M(?:3[0-3]|[12]\d|[1-9])|A(?:1[01]|[1235789])|B(?:1[0-6]|[1-9])|H1)(?![\w%-]|\.\d)")
    # Sub-steps: only after "sub-step(s) ", "(", "at " or "in ", plus any that follow in a list ("2.3, 2.4 and 2.7",
    # "4.2 to 4.7"), and never before a digit, "%", or a unit ("1.5 million", "2.5 hours"), so other decimals stay plain.
    _ss = r"[1-6]\.\d(?![\d%]|\.\d|\s*(?:million|billion|bn|m\b|k\b|x\b|times|hours?|days?|weeks?|months?|years?|percent|points?)|\s*(?:to|or|and|[–-])\s*\d+(?![.\d]))"
    sub_re = re.compile(r"((?:\bsub-steps?\s+|\(|\bat\s+|\bin\s+))(" + _ss + r"(?:(?:,\s*|,?\s+and\s+|,?\s+or\s+|\s+to\s+|\s*[–-]\s*)" + _ss + r")*)")
    def repl_text(t):
        def code(m):
            c = m.group(1); href = target({"K": "controls.html", "B": "workflows.html"}.get(c[0], "agents.html"), c.lower())
            return f'<a class="xref" href="{href}"{"" if href.startswith("#") else " target=\"_blank\" rel=\"noopener\""}>{c}</a>' if href else c
        def sub(m):
            def one(n):
                href = target("steps.html", "s" + n.group(0).replace(".", "-")) if n.group(0) in SUBSTEPS else None
                return f'<a class="xref" href="{href}" target="_blank" rel="noopener">{n.group(0)}</a>' if href and not href.startswith("#") else n.group(0)
            return m.group(1) + re.sub(r"[1-6]\.\d", one, m.group(2))
        def name(m):
            f = dict(names)[m.group(1)]; href = target(f)
            return f'<a class="xref" href="{href}" target="_blank" rel="noopener">{m.group(1)}</a>' if href and not href.startswith("#") else m.group(1)
        parts = re.split(r"(<a\b[^>]*>.*?</a>)", name_re.sub(name, t))   # names first, then codes outside the new links
        t = "".join(p if p.startswith("<a") else code_re.sub(code, p) for p in parts)
        if here in _SUB_NO_LINK: return t
        parts = re.split(r"(<a\b[^>]*>.*?</a>)", t)
        return "".join(p if p.startswith("<a") else sub_re.sub(sub, p) for p in parts)
    out, depth = [], 0
    for tok in re.split(r"(<[^>]+>)", page):
        if tok.startswith("<"):
            m = re.match(r"<(/?)([a-zA-Z0-9]+)", tok)
            if m and m.group(2).lower() in _SKIP:
                depth += -1 if m.group(1) else (0 if tok.endswith("/>") else 1)
                depth = max(depth, 0)
            out.append(tok)
        else:
            out.append(tok if depth or not tok.strip() else repl_text(tok))
    return "".join(out)
XREF_CSS = ".xref{color:inherit;text-decoration:underline;text-decoration-color:var(--teal);text-underline-offset:2px}.xref:hover{color:var(--teal)}"
CSS += XREF_CSS
CSS += "code{overflow-wrap:anywhere}"
CSS += "p,li,dd{overflow-wrap:break-word}"
