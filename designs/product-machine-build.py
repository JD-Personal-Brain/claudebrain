import html
E=html.escape
import re, os
from pagekit import series, SERIES_CSS, STEPS_URL
# Reads the task tables straight from product-machine.md, and each step's question from the
# Product Workflow (memos/role-workflow.md), so the page can't drift from its working copies.
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FW=open(os.path.join(ROOT,"product-machine.md")).read()
RW=open(os.path.join(ROOT,"memos","role-workflow.md")).read()
def kind_of(k):
    k=k.lower()
    for name in ["partner","auto","draft","me"]:
        if k.startswith(name): return name
    raise ValueError("unknown kind: "+k)
def rows_after(header):
    block=FW[FW.index(header)+len(header):]
    out=[]
    for line in block.split("\n"):
        if line.startswith("| # ") or line.startswith("|---"): continue
        if not line.startswith("|"):
            if out: break
            continue
        c=[x.strip() for x in line.strip("|").split("|")]
        out.append((c[1],kind_of(c[2]),c[3],c[4],c[0],"⚠️" in c[2]))
    return out
questions={}
for m in re.finditer(r"^\| (\d)\. ([^|]+?) \| ([^|]+) \|",RW,re.M):
    questions[m.group(1)]=(m.group(2),m.group(3).strip())
steps=[(questions[n][0],questions[n][1],rows_after(f"**{n}. {questions[n][0]}**\n")) for n in "123456"]
running=rows_after("## Across every project (the running layer)")
# The prose sections below the tables are read from product-machine.md too (automation check,
# gates in writing, measuring the machine, many projects), so the page can't drift from the .md.
def section(head):
    b=FW[FW.index(head+"\n")+len(head)+1:]
    m=re.search(r"^## |^_Last updated",b,re.M)
    return b[:m.start()] if m else b
def inline(t):
    t=E(t)
    t=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",t)
    t=re.sub(r"`(.+?)`",r"\1",t)
    return t
def paras(block):
    return [" ".join(p.split("\n")).strip() for p in re.split(r"\n\s*\n",block.strip()) if p.strip()]
def numbered(block):
    out=[]
    for m in re.finditer(r"^\d+\. \*\*(.+?)\*\*\s*(.*)$",block,re.M):
        out.append(f'<li><b>{inline(m.group(1))}</b><span>{inline(m.group(2))}</span></li>' if m.group(2) else f'<li><b>{inline(m.group(1))}</b></li>')
    return "".join(out)
ck=section("## The automation check at every gate")
ck_intro,ck_rest=ck.split("**First, cut:**")
ck_cut,ck_rest=ck_rest.split("**Then, automate what's left:**")
ck_cut_items,*ck_cut_after=re.split(r"\n\s*\n",ck_cut.strip(),maxsplit=1)
_m=re.match(r"((?:^\d+\..*\n?)+)",ck_rest.strip(),re.M)
ck_auto_list=_m.group(1); ck_after=paras(ck_rest.strip()[len(ck_auto_list):])
check_html=(f'<p>{inline(" ".join(paras(ck_intro)))}</p><h3>First, cut</h3><ol>{numbered(ck_cut_items)}</ol>'
    +"".join(f'<p>{inline(x)}</p>' for x in paras(ck_cut_after[0] if ck_cut_after else ""))
    +f"<h3>Then, automate what's left</h3><ol start=\"5\">{numbered(ck_auto_list)}</ol>"
    +"".join(f'<p>{inline(x)}</p>' for x in ck_after))
gates_html="".join(f'<p>{inline(x)}</p>' for x in paras(section("## Gates in writing when they're clean")))
ms=section("## Measuring the machine")
ms_lines=ms.strip().split("\n")
ms_tab=[l for l in ms_lines if l.startswith("|")]
ms_text=[l for l in ms_lines if not l.startswith("|")]
ms_before=paras("\n".join(ms_text[:ms_lines.index(ms_tab[0])]))
ms_after=paras("\n".join(ms_lines[ms_lines.index(ms_tab[-1])+1:]))
ms_head=[x.strip() for x in ms_tab[0].strip("|").split("|")]
ms_rows=""
for l in ms_tab[2:]:
    c=[x.strip() for x in l.strip("|").split("|")]
    ms_rows+=f'<tr><td><b>{inline(c[0])}</b></td><td>{inline(c[1])}</td><td>{inline(c[2])}</td></tr>'
measures_html=("".join(f'<p>{inline(x)}</p>' for x in ms_before)
    +f'<div class="step"><div class="tw"><table><thead><tr>{"".join(f"<th>{E(h)}</th>" for h in ms_head)}</tr></thead><tbody>{ms_rows}</tbody></table></div></div>'
    +"".join(f'<p>{inline(x)}</p>' for x in ms_after))
rules=re.findall(r"^- \*\*(.+?)\*\*\s*(.*)$",section("## Many projects at once"),re.M)
rules_html="".join(f'<div class="rule"><h3>{inline(t.rstrip(".:"))}</h3><p>{inline(b)}</p></div>' for t,b in rules)
NUMW={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight"}
LBL={"auto":"Auto","draft":"Draft","me":"Me","partner":"Partner"}
def chip(k): return f'<span class="chip k-{k}">{LBL[k]}</span>'
def cell_num(num):
    # a sub-step number links to its card in the Steps Catalog (idea 49); "Gate" and "All" stay plain
    if re.fullmatch(r"\d\.\d",num):
        return f'<a href="{STEPS_URL}#s{num.replace(".","-")}" target="_blank" rel="noopener" title="Open sub-step {num} in the Steps Catalog">{E(num)}</a>'
    return E(num)
def table(rows,head="Task"):
    r="".join(f'<tr><td class="n">{cell_num(num)}</td><td>{E(t)}</td><td>{chip(k)}{" ⚠️" if w else ""}</td><td>{E(tool)}</td><td>{E(to)}</td></tr>' for t,k,tool,to,num,w in rows)
    return f'<div class="tw"><table><thead><tr><th>#</th><th>{head}</th><th>Kind</th><th>Tool <span class="g">(guess)</span></th><th>Goes to</th></tr></thead><tbody>{r}</tbody></table></div>'
# mix bars
bars=""
for i,(name,q,rows) in enumerate(steps,1):
    n=len(rows); segs=""
    for k in ["me","draft","auto","partner"]:
        c=sum(1 for r in rows if r[1]==k)
        if c: segs+=f'<span class="seg k-{k}" style="flex:{c}" title="{LBL[k]}: {c}">{c}</span>'
    bars+=f'<div class="mixrow"><div class="mixname"><span class="num">{i}</span>{E(name)}</div><div class="mixbar" role="img" aria-label="{E(name)}: '+", ".join(f"{sum(1 for r in rows if r[1]==k)} {LBL[k]}" for k in ["me","draft","auto","partner"] if any(r[1]==k for r in rows))+f'">{segs}</div></div>'
me_counts=[(sum(1 for r in rows if r[1]=="me"),name) for name,q,rows in steps]
top=max(c for c,_ in me_counts)
top_names=[n for c,n in me_counts if c==top]
mix_text=(" and ".join(top_names)+(" carry" if len(top_names)>1 else " carries")+f" the most person-only work ({top} tasks"+(" each" if len(top_names)>1 else "")+"); the other steps lean more on AI drafts and automation.")
def note_after(header):
    # any short paragraph under a step's table (for example the step 4 gate note) shows under that table on the page
    b=FW[FW.index(header)+len(header):]
    lines=b.split("\n"); i=0
    while i<len(lines) and lines[i].startswith("|"): i+=1
    rest="\n".join(lines[i:]).strip()
    m=re.search(r"^\*\*\d\. |^## ",rest,re.M)
    return paras(rest[:m.start()] if m else rest)
stepsec=""
for i,(name,q,rows) in enumerate(steps,1):
    notes="".join(f'<p class="q" style="padding:14px 20px;border-top:1px solid var(--line);max-width:none">{inline(x)}</p>' for x in note_after(f"**{i}. {name}**\n"))
    stepsec+=f'<article class="step"><header><span class="num big">{i}</span><div><h3>{E(name)}</h3><p class="q">{E(q)}</p></div></header>{table(rows)}{notes}</article>'
page=f'''<title>Product Machine</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>
/* Layout: navy header band, then a single reading column of sections; each step is a card with a task table. */
:root{{--bg:#F4F6F8;--card:#FFFFFF;--line:#D9DEE5;--fg:#1B2433;--muted:#4D5868;--navy:#14213D;--onnavy:#FFFFFF;--onnavy-muted:#C9D3E3;--teal:#0F5F59;--teal-bg:#E1F0EE;--amber-bg:#FDF3E1;--amber:#8A4B00;--me:#14213D;--me-fg:#FFFFFF;--partner-bg:#E6E9EE;--partner:#3B4656;
--serif:"IBM Plex Serif",Georgia,"Times New Roman",serif;--sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0E1420;--card:#161E2C;--line:#2A3446;--fg:#E6EAF0;--muted:#A3AEBF;--navy:#0A1830;--onnavy:#FFFFFF;--onnavy-muted:#B4C1D6;--teal:#5FC4B8;--teal-bg:#123A37;--amber-bg:#3A2A10;--amber:#F2C27A;--me:#C9D6F0;--me-fg:#0E1420;--partner-bg:#2A3446;--partner:#C6CFDC;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0E1420;--card:#161E2C;--line:#2A3446;--fg:#E6EAF0;--muted:#A3AEBF;--navy:#0A1830;--onnavy:#FFFFFF;--onnavy-muted:#B4C1D6;--teal:#5FC4B8;--teal-bg:#123A37;--amber-bg:#3A2A10;--amber:#F2C27A;--me:#C9D6F0;--me-fg:#0E1420;--partner-bg:#2A3446;--partner:#C6CFDC;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:16px;line-height:1.55}}
.band{{background:var(--navy);color:var(--onnavy);padding-block:48px 40px;padding-inline:20px}}
.wrap{{max-width:960px;margin:0 auto}}
main.wrap{{padding-block:8px 64px;padding-inline:20px;display:flex;flex-direction:column;gap:48px}}
.label{{font-family:var(--mono);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin:0 0 8px}}
.band .label{{color:#8FD3CA}}
h1{{font-family:var(--serif);font-weight:600;font-size:clamp(32px,5vw,46px);line-height:1.15;margin:0 0 12px;text-wrap:balance}}
.lede{{font-size:18px;color:var(--onnavy-muted);max-width:62ch;margin:0}}
h2{{font-family:var(--serif);font-weight:600;font-size:28px;line-height:1.2;margin:0 0 12px;text-wrap:balance}}
h3{{font-family:var(--serif);font-weight:600;font-size:21px;margin:0}}
p{{margin:0;max-width:68ch}}
section{{display:flex;flex-direction:column;gap:16px}}
.kinds{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.kind{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:10px;min-width:0}}
.kind p{{color:var(--muted);font-size:15px}}
.chip{{display:inline-block;font-family:var(--mono);font-size:12px;letter-spacing:.04em;padding:3px 9px;border-radius:999px;white-space:nowrap;font-weight:500}}
.k-auto{{background:var(--teal-bg);color:var(--teal)}}
.k-draft{{background:var(--amber-bg);color:var(--amber)}}
.k-me{{background:var(--me);color:var(--me-fg)}}
.k-partner{{background:var(--partner-bg);color:var(--partner)}}
.kind .chip{{align-self:flex-start;font-size:13px}}
.mix{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:12px}}
.mixrow{{display:grid;grid-template-columns:190px 1fr;gap:16px;align-items:center}}
.mixname{{font-weight:500;display:flex;gap:10px;align-items:center}}
.num{{font-family:var(--mono);font-size:12px;color:var(--teal);min-width:1.2em}}
.mixbar{{display:flex;gap:3px;height:28px}}
.seg{{display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:12px;border-radius:4px;font-variant-numeric:tabular-nums}}
.legend{{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:14px;color:var(--muted);align-items:center}}
.note{{background:var(--amber-bg);color:var(--fg);border-radius:8px;padding:16px 20px}}
.note strong{{color:var(--amber)}}
.step{{background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden}}
.step header{{display:flex;gap:16px;align-items:center;padding:18px 20px;border-bottom:1px solid var(--line)}}
.num.big{{font-size:15px;width:34px;height:34px;border-radius:50%;border:1.5px solid var(--teal);display:flex;align-items:center;justify-content:center;flex:none}}
.q{{color:var(--muted);font-size:15px}}
.tw{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:15px;min-width:620px}}
th{{text-align:left;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:10px 20px;border-bottom:1px solid var(--line)}}
th .g{{text-transform:none;letter-spacing:0}}
td{{padding:11px 20px;border-bottom:1px solid var(--line);vertical-align:top}}
tr:last-child td{{border-bottom:0}}
td.n{{font-family:var(--mono);font-size:12px;color:var(--teal);white-space:nowrap;width:1%}}td:nth-child(2){{width:40%}}
td:nth-child(3),td:nth-child(4){{color:var(--muted)}}
.steps{{display:flex;flex-direction:column;gap:20px}}
.check{{background:var(--navy);color:var(--onnavy);border-radius:8px;padding:28px;display:flex;flex-direction:column;gap:18px}}
.check h2{{color:var(--onnavy)}}
.check ol{{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}
.check li{{border:1px solid rgba(255,255,255,.22);border-radius:6px;padding:16px;display:flex;flex-direction:column;gap:6px}}
.check li b{{font-family:var(--serif);font-size:19px;font-weight:600}}
.check li span,.check p{{color:var(--onnavy-muted)}}
.check .label{{color:#8FD3CA}}
.check h3{{font-family:var(--mono);font-size:12px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:#8FD3CA;margin:4px 0 -6px}}
.rules{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.rule{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:8px}}
.rule h3{{font-size:18px}}
.rule p{{color:var(--muted);font-size:15px}}
footer{{color:var(--muted);font-size:14px;border-top:1px solid var(--line);padding-top:16px}}
{SERIES_CSS}
@media (max-width:560px){{.kinds{{grid-template-columns:1fr}}.rules{{grid-template-columns:1fr}}.mixrow{{grid-template-columns:1fr;gap:6px}}.check{{padding:20px}}}}
</style>
<div class="band"><div class="wrap">
<p class="label">How we deliver</p>
<h1>Product Machine</h1>
<p class="lede">How one product manager runs many AI projects at once: routine work runs on its own and pushes tasks to people on time, so the product manager's hours go to decisions and people.</p>
{series("machine")}
</div></div>
<main class="wrap">
<section style="padding-top:32px">
<p class="label">The idea</p>
<h2 id="kinds">Three kinds of work, plus partner sign-offs</h2>
<p>Each project moves through the same six steps. Every task in every step is marked by who does it. Each project leaves the machine more automated than it found it.</p>
<div class="kinds">
<div class="kind">{chip("auto")}<h3>Runs on its own</h3><p>A workflow or agent does it and tells the right person. No one has to remember it.</p></div>
<div class="kind">{chip("draft")}<h3>AI drafts, a person checks</h3><p>AI does the first version, and a named person approves it.</p></div>
<div class="kind">{chip("me")}<h3>Only a person</h3><p>Decisions, agreement between people, relationships and trade-offs. This is where the product manager's hours go.</p></div>
<div class="kind">{chip("partner")}<h3>Partner sign-off</h3><p>A decision only a named partner can make, such as risk or compliance. Never automated.</p></div>
</div>
</section>
<section>
<p class="label">Where the product manager's time goes</p>
<h2 id="mix">Where person-only work sits</h2>
<p>Number of tasks of each kind once the machine is running, by step, gate decisions included. {E(mix_text)}</p>
<div class="mix">{bars}
<div class="legend">{chip("me")} Only a person {chip("draft")} AI drafts {chip("auto")} Runs on its own {chip("partner")} Partner sign-off</div></div>
</section>
<section>
<p class="label">The six steps</p>
<h2 id="tasks">Each step's tasks, by kind</h2>
<p>One row per task, numbered to match the sub-steps in the Product Playbook. Kind is the target once the machine is running; the first time through, many tasks are done by hand so they can be logged before they are automated. Tools are first guesses until we confirm the bank's setup.</p>
<div class="note"><strong>To confirm first:</strong> whether bank policy lets automations send requests, reminders, reports or alerts to people outside the project team, or change a live system, on their own. Tasks marked ⚠️ depend on it.</div>
<div class="steps">{stepsec}</div>
</section>
<section class="check">
<p class="label">At every gate</p>
<h2 id="check">The automation check: cut first, then automate</h2>
{check_html}
</section>
<section>
<p class="label">At every gate</p>
<h2 id="gates">Gates in writing when they're clean</h2>
{gates_html}
</section>
<section>
<p class="label">The machine is a product too</p>
<h2 id="measures">Measuring the machine</h2>
{measures_html}
</section>
<section>
<p class="label">Across every project</p>
<h2 id="running">The running layer</h2>
<p>One set of automations keeps all projects on schedule, so nothing depends on the product manager remembering to chase.</p>
<div class="step">{table(running)}</div>
</section>
<section>
<p class="label">Many projects at once</p>
<h2 id="rules">{NUMW.get(len(rules),str(len(rules)))} rules for running them side by side</h2>
<div class="rules">
{rules_html}
</div>
</section>
<footer>In use: reviewed 2026-10-14; cut-first check, gates in writing and the machine's measures added 2026-10-15. Tool choices are guesses until confirmed against the bank's setup. [X] marks numbers still to be set. The RM analytics plan is the first project to run through this machine.</footer>
</main>
'''
open(os.path.join(ROOT,'designs','product-machine.html'),'w').write(page)
