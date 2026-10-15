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
stepsec=""
for i,(name,q,rows) in enumerate(steps,1):
    stepsec+=f'<article class="step"><header><span class="num big">{i}</span><div><h3>{E(name)}</h3><p class="q">{E(q)}</p></div></header>{table(rows)}</article>'
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
<h2 id="mix">Early steps need people; later steps run themselves</h2>
<p>Number of tasks of each kind once the machine is running, by step, gate decisions included. Discover and Define carry the most person-only work, because that is where judgment matters most.</p>
<div class="mix">{bars}
<div class="legend">{chip("me")} Only a person {chip("draft")} AI drafts {chip("auto")} Runs on its own {chip("partner")} Partner sign-off</div></div>
</section>
<section>
<p class="label">The six steps</p>
<h2 id="tasks">Each step's tasks, by kind</h2>
<p>One row per task, numbered to match the sub-steps in the Product Playbook. Kind is the target once the machine is running; the first time through, many tasks are done by hand so they can be logged before they are automated. Tools are first guesses until we confirm the bank's setup.</p>
<div class="note"><strong>To confirm first:</strong> whether bank policy lets automations message people or update trackers on their own. Tasks marked ⚠️ depend on it.</div>
<div class="steps">{stepsec}</div>
</section>
<section class="check">
<p class="label">At every gate</p>
<h2 id="check">The automation check: cut first, then automate</h2>
<p>Before each go/no-go, take every task done by a person or drafted by AI through seven questions, in this order. Automating a task that shouldn't exist only locks in the waste (the order comes from Elon Musk's "algorithm"; see the Elon Mode Research page).</p>
<h3>First, cut</h3>
<ol>
<li><b>Should it exist?</b><span>Who required it, and where does it come from: law or regulator, bank policy, or our choice (each control's card in the Controls Catalog; the Product Playbook's table for sub-steps and gates)? Law and bank policy stay. Our choices can be challenged.</span></li>
<li><b>Can we delete it?</b><span>Record what it did and who agreed in the decision log. If nothing ever has to come back, we aren't cutting enough (about 1 in 10 should; ⚠️ sources give 10% or 20%).</span></li>
<li><b>Can we simplify it?</b><span>Fewer steps, fewer hand-offs, fewer people to wait on.</span></li>
<li><b>Can we make it faster?</b><span>Shorten the longest wait first. The wait index shows where.</span></li>
</ol>
<h3>Then, automate what's left</h3>
<ol start="5">
<li><b>Did it repeat?</b><span>Will it come up again, in this project or the next one?</span></li>
<li><b>Is it stable?</b><span>Did we do it the same way at least twice?</span></li>
<li><b>Is it safe alone?</b><span>It makes no decision, nothing reaches a client, and bank rules allow it.</span></li>
</ol>
<p>Three yeses: move the task one kind toward Auto before the next project. If an automated task goes wrong, a person takes it back until it's fixed.</p>
</section>
<section>
<p class="label">At every gate</p>
<h2 id="gates">Gates in writing when they're clean</h2>
<p>When every gate criterion is met, the decider approves the gate pack in writing, and the approval goes in the decision log. A gate meeting happens only when a criterion is contested or someone who decides asks for one. Partner sign-offs in step 4 don't change: each named partner still signs, and at the step 4 gate the decider approves the signed evidence pack (⚠️ the bank's approval policy may require a committee meeting). ⚠️ Whether the bank's culture accepts gates in writing is a guess; confirm it at the first project.</p>
</section>
<section>
<p class="label">The machine is a product too</p>
<h2 id="measures">Measuring the machine</h2>
<p>Recorded for every project in sub-step 6.6 and shown in the one view of all projects. Targets are [X] until the first project sets a baseline; after that, each project should beat the last.</p>
<div class="step"><div class="tw"><table><thead><tr><th>Measure</th><th>What it is</th><th>Where it comes from</th></tr></thead><tbody>
<tr><td><b>Days from kickoff to pilot</b></td><td>Calendar days from sub-step 1.0 to the pilot launch (5.2)</td><td>The tracker</td></tr>
<tr><td><b>Days at each gate</b></td><td>Calendar days from the gate pack being ready to the decision</td><td>The decision log</td></tr>
<tr><td><b>Releases per month in the pilot</b></td><td>How many improved versions reach pilot users each month (how fast we iterate)</td><td>Release notes (5.6)</td></tr>
<tr><td><b>Wait index</b></td><td>For each sub-step: calendar days from start to finish, divided by hours of real work. A high number means waiting, not working; fix the highest first</td><td>The first-time logs (6.6, agent M19)</td></tr>
</tbody></table></div></div>
</section>
<section>
<p class="label">Across every project</p>
<h2 id="running">The running layer</h2>
<p>One set of automations keeps all projects on schedule, so nothing depends on the product manager remembering to chase.</p>
<div class="step">{table(running)}</div>
</section>
<section>
<p class="label">Many projects at once</p>
<h2 id="rules">Four rules for running them side by side</h2>
<div class="rules">
<div class="rule"><h3>One machine for every project</h3><p>The same steps, tables and tracker, so any project can be compared with any other.</p></div>
<div class="rule"><h3>Limit the person-heavy steps</h3><p>At most [X] projects in Discover or Define at once. Steps 3 to 6 are mostly automated, so more projects can sit there.</p></div>
<div class="rule"><h3>Stagger the gates</h3><p>No two gate meetings (the contested ones) in the same week.</p></div>
<div class="rule"><h3>Plan the product manager's week</h3><p>[X] hours on decisions and gates, [X] on users, [X] on partners and sign-offs, [X] checking drafts. If person-only work runs over, the automation check comes first.</p></div>
</div>
</section>
<footer>In use: reviewed 2026-10-14; cut-first check, gates in writing and the machine's measures added 2026-10-15. Tool choices are guesses until confirmed against the bank's setup. [X] marks numbers still to be set. The RM analytics plan is the first project to run through this machine.</footer>
</main>
'''
open(os.path.join(ROOT,'designs','product-machine.html'),'w').write(page)
