import html
E=html.escape
steps=[
("Discover","Which problem is worth solving first?",[
("Agree the outcome and measure with the sponsor","me","Meeting","Sponsor"),
("First look at the size of the opportunity","draft","Snowflake, Power BI","Me, then sponsor"),
("Schedule interviews and shadowing","auto","Outlook, Power Automate","Users"),
("Interview and shadow users","me","Teams, in person","—"),
("Pull themes from interview notes","draft","M365 Copilot","Me"),
("Record today's baseline numbers (once the measure is set)","auto","Power BI","Sponsor"),
("Gate decision","me","Meeting","Sponsor")]),
("Define","What do we build first, and how will we know it worked?",[
("One-sentence problem and measurable outcome","me","—","Sponsor"),
("Choose the platform and delivery path (with platform teams)","me","—","Platform teams"),
("Data contract: fields, freshness, checks","draft","Snowflake","Data owner approves"),
("Risk intake form, filled in from the brief","draft","Bank's intake process","Model risk rates it"),
("User stories and acceptance criteria","draft","Backlog tool","Me"),
("Backlog priorities and trade-offs","me","Backlog tool","Decision log"),
("Measures, quality bar and value model","draft","Power BI","Me, then sponsor"),
("Gate decision","me","Meeting","Sponsor, risk")]),
("Build","What's the smallest version users will use and trust?",[
("Configure the AI capability (with platform teams)","me","Copilot Studio, Agentforce, Bedrock, Power Automate","—"),
("Build the test set: real examples, known good answers","draft","Spreadsheet or eval tool","Me and pilot users check"),
("Run the test set on every new version","auto","Bedrock evaluation or similar","Me, only when something fails"),
("Gate decision","me","—","Sponsor")]),
("Govern and test","Is it safe, fair and controlled?",[
("Red-team the product (try to break it)","auto","Red-team agent","Risk reviews every failure"),
("Put together the evidence pack","draft","Templates and test results","Me, then risk"),
("Send sign-off requests and chase them","auto","Power Automate approvals","Risk, compliance, privacy, security"),
("The sign-offs themselves","partner","—","Recorded in the tracker"),
("Unblock a stuck sign-off","me","Meeting","—")]),
("Release and adopt","Will users use it every week?",[
("Release readiness checklist","draft","Template","Me"),
("Train users on their own work; recruit champions","me","Teams, in person","Pilot users"),
("Weekly usage report","auto","Power BI","Sponsor, user leaders"),
("Sort feedback into bugs, quality issues and ideas","auto","Feedback triage agent","Backlog; I check a weekly sample"),
("Decide to scale to the next wave","me","Meeting","Sponsor")]),
("Measure and iterate","Is it delivering, and what comes next?",[
("Live dashboard against baseline and comparison group","auto","Power BI","Sponsor"),
("Re-test after every change; alert when quality slips","auto","Eval tool and alerts","Me"),
("Monthly keep / change / stop pack","draft","Power BI and template","Me"),
("Keep / change / stop decision and next wave","me","Meeting","Sponsor")]),
]
running=[
("One tracker for all projects: task, owner, date, status","auto","A shared tracker (tool to confirm)","Set up once by me, then updates itself"),
("Remind owners before a due date; tell me when something is late","auto","Power Automate","Owners, then me"),
("Weekly status note for each project","draft","M365 Copilot, from the tracker","Me, then stakeholders"),
("Decision log and risk / issue list, from meeting notes","draft","M365 Copilot","Me"),
("One view of all projects: step, late items, measures","auto","Power BI","Sponsors and leaders"),
]
LBL={"auto":"Auto","draft":"Draft","me":"Me","partner":"Partner"}
def chip(k): return f'<span class="chip k-{k}">{LBL[k]}</span>'
def table(rows,head="Task"):
    r="".join(f'<tr><td>{E(t)}</td><td>{chip(k)}</td><td>{E(tool)}</td><td>{E(to)}</td></tr>' for t,k,tool,to in rows)
    return f'<div class="tw"><table><thead><tr><th>{head}</th><th>Kind</th><th>Tool <span class="g">(guess)</span></th><th>Goes to</th></tr></thead><tbody>{r}</tbody></table></div>'
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
page=f'''<title>The Delivery Machine</title>
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
.kinds{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}
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
td:first-child{{width:42%}}
td:nth-child(3),td:nth-child(4){{color:var(--muted)}}
.steps{{display:flex;flex-direction:column;gap:20px}}
.check{{background:var(--navy);color:var(--onnavy);border-radius:8px;padding:28px;display:flex;flex-direction:column;gap:18px}}
.check h2{{color:var(--onnavy)}}
.check ol{{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}}
.check li{{border:1px solid rgba(255,255,255,.22);border-radius:6px;padding:16px;display:flex;flex-direction:column;gap:6px}}
.check li b{{font-family:var(--serif);font-size:19px;font-weight:600}}
.check li span,.check p{{color:var(--onnavy-muted)}}
.check .label{{color:#8FD3CA}}
.rules{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.rule{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:20px;display:flex;flex-direction:column;gap:8px}}
.rule h3{{font-size:18px}}
.rule p{{color:var(--muted);font-size:15px}}
footer{{color:var(--muted);font-size:14px;border-top:1px solid var(--line);padding-top:16px}}
@media (max-width:560px){{.rules{{grid-template-columns:1fr}}.mixrow{{grid-template-columns:1fr;gap:6px}}.check{{padding:20px}}}}
</style>
<div class="band"><div class="wrap">
<p class="label">Operating model · AI product delivery</p>
<h1>The Delivery Machine</h1>
<p class="lede">How one product manager runs many AI projects at once: routine work runs on its own and pushes tasks to people on time, so the PM's hours go to decisions and people.</p>
</div></div>
<main class="wrap">
<section style="padding-top:32px">
<p class="label">The idea</p>
<h2>Every task is one of three kinds</h2>
<p>Each project moves through the same six steps. Every task in every step is marked by who does it. Each project leaves the machine more automated than it found it.</p>
<div class="kinds">
<div class="kind">{chip("auto")}<h3>Runs on its own</h3><p>A workflow or agent does it and tells the right person. No one has to remember it.</p></div>
<div class="kind">{chip("draft")}<h3>AI drafts, a person checks</h3><p>AI does the first version, and a named person approves it.</p></div>
<div class="kind">{chip("me")}<h3>Only a person</h3><p>Decisions, agreement between people, relationships and trade-offs. This is where the PM's hours go.</p></div>
</div>
</section>
<section>
<p class="label">Where the PM's time goes</p>
<h2>Early steps need people; later steps run themselves</h2>
<p>Number of tasks of each kind, by step. Discover and Define are where judgment matters most, so they carry the most person-only work.</p>
<div class="mix">{bars}
<div class="legend">{chip("me")} Only a person {chip("draft")} AI drafts {chip("auto")} Runs on its own {chip("partner")} Partner sign-off</div></div>
</section>
<section>
<p class="label">The six steps</p>
<h2>Each step's tasks, by kind</h2>
<p>These tables are the starting point. Tools are first guesses until we confirm the bank's setup.</p>
<div class="note"><strong>To confirm first:</strong> whether bank policy lets automations message people or update trackers on their own. That decides how much can be marked Auto.</div>
<div class="steps">{stepsec}</div>
</section>
<section class="check">
<p class="label">At every gate</p>
<h2>The automation check</h2>
<p>Before each go/no-go, ask three questions of every task done by a person or drafted by AI:</p>
<ol>
<li><b>Did it repeat?</b><span>Will it come up again, in this project or the next one?</span></li>
<li><b>Is it stable?</b><span>Did we do it the same way at least twice?</span></li>
<li><b>Is it safe alone?</b><span>It makes no decision, nothing reaches a client, and bank rules allow it.</span></li>
</ol>
<p>Three yeses: move the task one kind toward Auto before the next project. If an automated task goes wrong, a person takes it back until it's fixed.</p>
</section>
<section>
<p class="label">Across every project</p>
<h2>The running layer</h2>
<p>One set of automations keeps all projects on schedule, so nothing depends on the PM remembering to chase.</p>
<div class="step">{table(running)}</div>
</section>
<section>
<p class="label">Many projects at once</p>
<h2>Four rules for running them side by side</h2>
<div class="rules">
<div class="rule"><h3>One machine for every project</h3><p>The same steps, tables and tracker, so any project can be compared with any other.</p></div>
<div class="rule"><h3>Limit the person-heavy steps</h3><p>At most [X] projects in Discover or Define at once. Steps 3 to 6 are mostly automated, so more projects can sit there.</p></div>
<div class="rule"><h3>Stagger the gates</h3><p>No two gate meetings in the same week.</p></div>
<div class="rule"><h3>Plan the PM's week</h3><p>[X] hours on decisions and gates, [X] on users, [X] on partners and sign-offs, [X] checking drafts. If person-only work runs over, the automation check comes first.</p></div>
</div>
</section>
<footer>Draft, 2026-10-09. Tool choices are guesses until confirmed against the bank's setup. [X] marks numbers still to be set. The RM analytics plan is the first project to run through this machine.</footer>
</main>
'''
open('/home/user/claudebrain/designs/delivery-machine.html','w').write(page)
