"""Builds designs/workflows.html, the Workflow Maps: each main process as a
left-to-right spine of stages, with its sub-processes branching underneath.
Click a branch to see its details. Reads memos/role-workflow.md (each step's
question, gate and governance thread, via pagekit.six_steps()), playbook/*.md,
product-machine.md and the RM memo's Appendix B, so the maps never drift from the documents.
Run: python3 designs/workflows-build.py"""
import os, re
from pagekit import CSS, E, inline, chipify, six_steps, WORKFLOW_URL, STEPS_URL, PLAYBOOK_URL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda p: open(os.path.join(ROOT, p)).read()
RM_PLAN_URL = "https://claude.ai/artifact/PhUyGc16TmNNXBsn6Yo25n"  # RM Detail, which holds the full plan and its Appendix B
SIX = six_steps()  # each step's question, governance thread and gate come from the Product Workflow, their one home

# ---------- Map 1: delivering a product (six steps -> 44 sub-steps) ----------
fw = read("product-machine.md")
kinds = {}
for m in re.finditer(r"^\| (\d\.\d) \| ([^|]+) \| ([^|]+) \|", fw, re.M):
    kinds.setdefault(m.group(1), []).append((m.group(2).strip(), m.group(3).strip()))

def field(body, name):
    m = re.search(r"^- \*\*" + re.escape(name) + r":\*\*\s*(.*)$", body, re.M)
    return m.group(1) if m else ""

stages1 = []
for fn in sorted(f for f in os.listdir(os.path.join(ROOT, "playbook")) if re.match(r"\d-.*\.md$", f)):
    s = read(os.path.join("playbook", fn))
    n = fn[0]
    name = SIX[n]["name"]
    q, gate, gov = SIX[n]["question"], SIX[n]["gate"], SIX[n]["governance"]
    review = s[s.index("| Sub-step | Agent |"):]
    branches = []
    for part in re.split(r"\n## ", s)[1:]:
        head, _, body = part.partition("\n")
        m = re.match(r"^(\d\.\d) (.+)$", head)
        if not m:
            continue
        num, title = m.groups()
        agents, assets = set(), []
        for row in review.split("\n"):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) >= 5 and num in [x.strip() for x in cells[0].split(",")]:
                # only agents the row actually uses: the "Already specified?" cell names them ("Yes, M1",
                # "Yes, M24 ..."); a mention like "None (feeds M30)" in the Agent cell is not a use
                if cells[4].lower().startswith("asset"):
                    assets.append(cells[1])
                if cells[4].lower().startswith("yes"):
                    agents |= set(re.findall(r"\b(?:A\d|M\d{1,2})\b", cells[1] + " " + cells[4]))
        agents = sorted(agents, key=lambda a: (a[0], int(a[1:])))
        branches.append({
            "id": f"d{num.replace('.', '-')}", "num": num, "title": title,
            "goal": field(body, "Goal"), "done": field(body, "Done when"),
            "tasks": kinds.get(num, []), "agents": agents, "assets": assets,
            "link": f"{PLAYBOOK_URL}#s{num.replace('.', '-')}",
            "catalog": f"{STEPS_URL}#s{num.replace('.', '-')}",
        })
    stages1.append({"n": n, "name": name, "q": q, "gate": gate, "gov": gov, "branches": branches})

# ---------- Map 2: an RM's week (The RM Assistant's workflows) ----------
memo = read("memos/rm-analytics-framework.md")
appb = memo.split("## Appendix B: Workflows")[1]
flows = {}
for block in re.split(r"\n\*\*(?=B\d+\. )", appb)[1:]:
    head, _, body = block.partition("\n")
    m = re.match(r"(B\d+)\. (.+?)\*\*\s*(?:\((.+?)\))?", head)
    bid, title, wave = m.group(1), m.group(2).strip(), (m.group(3) or "").strip()
    steps_txt = field(body, "Steps")
    steps = [st.strip() for st in re.split(r"\s*\d+\.\s+", steps_txt) if st.strip()]
    flows[bid] = {"id": bid.lower(), "num": bid, "title": title, "wave": wave,
                  "trigger": field(body, "Trigger"), "steps": steps,
                  "logged": field(body, "Logged"), "measures": field(body, "Measures"),
                  "check": field(body, "Check"),
                  "agents": sorted(set(re.findall(r"\b(?:A\d|M\d{1,2})\b", body)), key=lambda a: int(a[1:])),
                  "link": f"{RM_PLAN_URL}#part-5-the-full-delivery-plan-with-every"}

# The RM's week as the main process. This grouping is my framing of the
# memo's workflows; confirm it with RMs in Discover.
RM_STAGES = [
    ("1", "Find the opportunity or risk", "Which clients should I call, and why?", ["B1", "B5", "B6", "B8"]),
    ("2", "Prepare (or any time)", "What do I need to know before I talk to them? Client Q&A (B7) works at any stage.", ["B2", "B7"]),
    ("3", "Meet and follow up", "What did we agree, and what happens next?", ["B3"]),
    ("4", "Log it", "Is the client record up to date?", ["B4"]),
]
flat = [b for *_, bs in RM_STAGES for b in bs] + ["B9"]
if len(flat) != len(set(flat)):
    raise SystemExit("A workflow is placed twice on the RM map")
used = set(flat)
missing = set(flows) - used
if missing:
    raise SystemExit(f"Workflows not placed on the RM map: {sorted(missing)}")

# ---------- rendering ----------
def chips(ts):
    seen, out = [], []
    for _, k in ts:
        base = k.split()[0]
        if base not in seen:
            seen.append(base); out.append(chipify(base))
    return "".join(out)

def delivery_detail(b):
    tasks = "".join(f"<li>{chipify(k)} {inline(t)}</li>" for t, k in b["tasks"])
    auto = any(kind.split()[0] in ("Auto", "Draft") for _, kind in b["tasks"])
    # Map 1 is for every product, so an RM plan product agent (A1, A2, A3, A5) says where it comes from
    ag = ", ".join([a + " (a product agent in the RM plan)" if a.startswith("A") else a for a in b["agents"]] + [f"{a.replace(' (template)', '')} (a reusable template)" for a in b["assets"]])
    if not ag:
        ag = "No named agent yet" if auto else "None: this stays with a person"
    return (f'<h4><span class="num">{b["num"]}</span> {inline(b["title"])}</h4>'
            f'<dl class="facts"><div><dt>Goal</dt><dd>{inline(b["goal"][:1].upper() + b["goal"][1:])}</dd></div>'
            f'<div><dt>Done when</dt><dd>{inline(b["done"][:1].upper() + b["done"][1:])}</dd></div>'
            f'<div><dt>Agents that help</dt><dd>{E(ag)}</dd></div></dl>'
            f'<h5>Tasks and who does them</h5><ul class="tasks">{tasks}</ul>'
            f'<p class="links"><a class="more" href="{E(b["link"])}" target="_blank" rel="noopener">Open the full sub-step in the playbook</a>'
            f'<a class="more" href="{E(b["catalog"])}" target="_blank" rel="noopener">Find it in the Steps Catalog</a></p>')

def rm_detail(f):
    steps = ""
    for st in f["steps"]:
        dec = st.startswith("**Decision point:**")
        txt = st.replace("**Decision point:**", "").strip()
        txt = txt[:1].upper() + txt[1:]
        steps += f'<li class="{"decide" if dec else ""}">{"<span class=dlabel>Decision point</span> " if dec else ""}{inline(txt)}</li>'
    extra = f'<div><dt>Check</dt><dd>{inline(f["check"])}</dd></div>' if f["check"] else ""
    ag = ", ".join(f["agents"]) if f["agents"] else "None"
    return (f'<h4><span class="num">{f["num"]}</span> {inline(f["title"])}</h4>'
            f'<dl class="facts"><div><dt>Starts when</dt><dd>{inline(f["trigger"][:1].upper() + f["trigger"][1:])}</dd></div>'
            f'<div><dt>Agents</dt><dd>{E(ag)}</dd></div>{extra}</dl>'
            f'<h5>Step by step</h5><ol class="flow">{steps}</ol>'
            f'<dl class="facts"><div><dt>Logged</dt><dd>{inline(f["logged"][:1].upper() + f["logged"][1:])}</dd></div>'
            f'<div><dt>Measured by</dt><dd>{inline(f["measures"][:1].upper() + f["measures"][1:])}</dd></div></dl>'
            f'<a class="more" href="{E(f["link"])}" target="_blank" rel="noopener">Open the workflows in RM Detail</a>')

def spine_map(mid, stages, branch_html, detail_html, tag):
    cols = ""
    templates = ""
    for i, st in enumerate(stages):
        br = ""
        for b in st["branches"]:
            br += (f'<li><button type="button" class="branch" id="{b["id"]}" data-map="{mid}" data-id="{b["id"]}" aria-controls="{mid}-panel">'
                   f'{branch_html(b)}</button></li>')
            templates += f'<template id="t-{b["id"]}">{detail_html(b)}</template>'
        arrow = '<span class="arrow" aria-hidden="true"><svg viewBox="0 0 24 12" width="24" height="12"><line x1="0" y1="6" x2="18" y2="6" stroke="currentColor" stroke-width="2"/><polygon points="17,1 24,6 17,11" fill="currentColor"/></svg></span>' if i < len(stages) - 1 else ""
        gate = f'<div class="gatebar"><span class="diamond" aria-hidden="true"></span>Gate: {inline(st["gate"])}</div>' if st.get("gate") else ""
        if st.get("gov"):
            gate += f'<div class="govbar"><b>Governance</b> {inline(st["gov"])}</div>'
        cols += (f'<li class="stage"><div class="stagebox"><span class="snum">{tag} {st["n"]}</span>'
                 f'<span class="sname">{inline(st["name"])}</span><span class="sq">{inline(st["q"][:1].upper() + st["q"][1:])}</span>{arrow}</div>'
                 f'<ul class="branches" aria-label="Sub-processes of {E(st["name"])}">{br}</ul>{gate}</li>')
    first = stages[0]["branches"][0]
    return (f'<ol class="spine" style="--cols:{len(stages)}">{cols}</ol>'
            f'<div class="panel" id="{mid}-panel" aria-live="polite">{detail_html(first)}</div>{templates}')

d_branch = lambda b: f'<span class="bnum">{b["num"]}</span><span class="btitle">{inline(b["title"])}</span><span class="bkinds">{chips(b["tasks"])}</span>'
r_branch = lambda f: f'<span class="bnum">{f["num"]}</span><span class="btitle">{inline(f["title"])}</span><span class="bkinds">{"<span class=wave>" + E(f["wave"].split(";")[0]) + "</span>" if f["wave"] else ""}</span>'

map1 = spine_map("deliver", stages1, d_branch, delivery_detail, "Step")
rm_stages = [{"n": n, "name": nm, "q": q, "gate": "", "branches": [flows[b] for b in bs]} for n, nm, q, bs in RM_STAGES]
map2 = spine_map("rm", rm_stages, r_branch, rm_detail, "Stage")
b9 = flows["B9"]
loop = (f'<div class="loop"><span class="label">Behind the scenes, every release</span>'
        f'<button type="button" class="branch wide" data-map="rm" data-id="{b9["id"]}" aria-controls="rm-panel">{r_branch(b9)}</button>'
        f'<p>Runs under every workflow above: no change reaches RMs until it passes the test set.</p></div>'
        f'<template id="t-{b9["id"]}">{rm_detail(b9)}</template>')
n_sub = sum(len(s["branches"]) for s in stages1)

page = f'''<title>Workflow Maps</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
[hidden]{{display:none!important}}
/* Layout: each map is a spine of stage boxes left to right (arrows between), branches hanging below each stage, and one detail panel under the map. */
.mapwrap{{display:flex;flex-direction:column;gap:16px}}
.spine{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(var(--cols),minmax(0,1fr));gap:14px}}
.stage{{display:flex;flex-direction:column;gap:10px;min-width:0}}
.stagebox{{position:relative;background:var(--navy);color:var(--onnavy);border-radius:8px;padding:14px 14px 16px;display:flex;flex-direction:column;gap:4px;min-height:132px}}
.snum{{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy)}}
.sname{{font-family:var(--serif);font-weight:600;font-size:18px;line-height:1.2}}
.sq{{font-size:13px;color:var(--onnavy-muted);line-height:1.4}}
.arrow{{position:absolute;right:-20px;top:50%;transform:translateY(-50%);color:var(--teal);z-index:1}}
.branches{{list-style:none;margin:0;padding:0 0 0 12px;border-left:2px solid var(--line);margin-left:16px;display:flex;flex-direction:column;gap:8px}}
.branches li{{position:relative}}
.branches li::before{{content:"";position:absolute;left:-12px;top:20px;width:10px;border-top:2px solid var(--line)}}
.branch{{all:unset;box-sizing:border-box;width:100%;cursor:pointer;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:8px 10px;display:flex;flex-direction:column;gap:4px;font-size:13px;line-height:1.35;color:var(--fg)}}
.branch:hover{{border-color:var(--teal)}}
.branch:focus-visible{{outline:2px solid var(--teal);outline-offset:2px}}
.branch[aria-pressed="true"]{{border-color:var(--teal);box-shadow:inset 0 0 0 1px var(--teal);background:var(--teal-bg)}}
.bnum{{font-family:var(--mono);font-size:11px;color:var(--teal)}}
.btitle{{font-weight:500}}
.bkinds{{display:flex;flex-wrap:wrap;gap:3px}}
.bkinds .chip{{font-size:10px;padding:1px 6px;margin:0}}
.wave{{font-family:var(--mono);font-size:10px;color:var(--muted)}}
.gatebar{{margin-left:16px;font-size:12px;color:var(--fg);display:flex;gap:8px;align-items:flex-start;line-height:1.4}}
.diamond{{flex:none;width:10px;height:10px;background:var(--amber);transform:rotate(45deg);margin-top:3px}}
.panel{{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);border-radius:8px;padding:20px 24px;display:flex;flex-direction:column;gap:12px}}
.panel h4{{font-size:22px}}
.panel h5{{margin:4px 0 0}}
.facts{{margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}}
.facts dt{{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:2px}}
.facts dd{{margin:0;font-size:15px}}
.tasks{{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px;font-size:15px}}
.flow{{margin:0;padding-left:22px;display:flex;flex-direction:column;gap:6px;font-size:15px}}
.flow li.decide{{background:var(--amber-bg);border-radius:6px;padding:6px 10px;margin-left:-10px}}
.dlabel{{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--amber);margin-right:6px}}
.more{{align-self:flex-start;font-weight:500}}
.links{{display:flex;flex-wrap:wrap;gap:6px 20px;margin:0;max-width:none}}
.govbar{{margin-left:16px;font-size:12px;line-height:1.4;background:var(--amber-bg);border-radius:6px;padding:6px 8px}}
.govkey{{display:inline-block;background:var(--amber-bg);border-radius:6px;padding:2px 8px;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);border:1px dashed var(--amber)}}
.govbar b{{font-family:var(--mono);font-weight:500;font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--amber);display:block}}
.loop{{background:var(--card);border:1px dashed var(--line);border-radius:8px;padding:14px 16px;display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center}}
.loop p{{margin:0;font-size:14px;color:var(--muted);flex:1 1 260px}}
.branch.wide{{width:auto;flex:0 1 280px}}
.howto{{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:14px;color:var(--muted);align-items:center}}
.note{{max-width:none}}
@media (max-width:860px){{.spine{{grid-template-columns:1fr}}.arrow{{right:auto;left:24px;top:auto;bottom:-16px;transform:rotate(90deg)}}.stagebox{{min-height:0}}}}
</style>
<div class="band"><div class="wrap">
<span class="label">Workflow maps</span>
<h1>Workflow Maps</h1>
<p class="lede">Each main process runs left to right. The sub-processes hang underneath the stage where they happen. Click any box to see its details, then open the full document if you need more.</p>
<nav class="stepnav" aria-label="Maps"><a href="#deliver">How we deliver a product</a><a href="#rm">How an RM uses the product</a></nav>
<nav class="stepnav" aria-label="Related pages"><a href="{WORKFLOW_URL}" target="_blank" rel="noopener">Product Workflow: the steps and their gates ↗</a><a href="{STEPS_URL}" target="_blank" rel="noopener">Steps Catalog: look up any sub-step ↗</a></nav>
</div></div>
<main class="wrap">
<div class="howto"><span>Reading the maps:</span><span>Big navy box = a step (Map 1) or a stage of the RM's week (Map 2)</span><span>Small box = a sub-process</span><span><span class="chip k-auto">Auto</span><span class="chip k-draft">Draft</span><span class="chip k-me">Me</span><span class="chip k-partner">Partner</span> = who does its tasks</span><span>◆ = a go/no-go gate</span><span><span class="govkey">Governance</span> = the risk work in that step</span></div>
<section id="deliver" class="mapwrap">
<div class="stephead"><span class="label">Map 1 · every product</span><h2>How we deliver a product</h2>
<p class="intro" style="margin-top:6px;color:var(--muted)">The six steps of the Product Workflow, each ending in a gate, with its {n_sub} sub-steps underneath and the governance thread (the risk work) under each gate. After the first pass, steps 3 to 6 repeat in short cycles.</p></div>
{map1}
</section>
<section id="rm" class="mapwrap">
<div class="stephead"><span class="label">Map 2 · The RM Assistant</span><h2>How an RM uses the product</h2>
<p class="intro" style="margin-top:6px;color:var(--muted)">An RM's week, with each of the product's workflows placed where it helps. Every RM-facing workflow (B1 to B8) has a point where the RM decides, and nothing reaches a client without the RM. B9 is the release routine behind them.</p></div>
<div class="note">⚠️ Grouping the workflows into these four stages is my framing of the plan. Confirm it with RMs in Discover.</div>
{map2}
{loop}
</section>
<footer>Built from <code>memos/role-workflow.md</code> (each step's question, gate and governance thread), <code>playbook/</code>, <code>product-machine.md</code> and the RM memo's Appendix B by <code>designs/workflows-build.py</code>. Tasks marked ⚠️ depend on the bank allowing automations.</footer>
</main>
<script>
(function(){{
  function show(btn){{
    var map=btn.getAttribute('data-map'), panel=document.getElementById(map+'-panel'), t=document.getElementById('t-'+btn.getAttribute('data-id'));
    if(!panel||!t) return;
    panel.innerHTML=t.innerHTML;
    document.querySelectorAll('.branch[data-map="'+map+'"]').forEach(function(b){{b.setAttribute('aria-pressed', b===btn?'true':'false');}});
    var r=panel.getBoundingClientRect();
    if(r.top>window.innerHeight||r.bottom<0) panel.scrollIntoView({{behavior:'smooth',block:'nearest'}});
  }}
  document.querySelectorAll('.branch').forEach(function(b){{
    b.setAttribute('aria-pressed','false');
    b.addEventListener('click',function(){{show(b);}});
  }});
  ['deliver','rm'].forEach(function(m){{var f=document.querySelector('.branch[data-map="'+m+'"]'); if(f) f.setAttribute('aria-pressed','true');}});
  // a link from another page that names a sub-step (#d3-1) shows that sub-step's details
  function openHash(){{var h=location.hash&&document.getElementById(decodeURIComponent(location.hash.slice(1))); if(h&&h.classList.contains('branch')) show(h);}}
  openHash(); window.addEventListener('hashchange',openHash);
}})();
</script>
'''
open(os.path.join(ROOT, "designs", "workflows.html"), "w").write(page)
