"""Builds designs/agents.html, the Agent Library: every agent in one place,
filterable, each opening to its full spec. Reads playbook/agents.md (M1-M19,
the agents that run the delivery machine) and the RM memo's Appendix A
(A1-A20). Run: python3 designs/agents-build.py"""
import os, re
from pagekit import CSS, E, inline, chipify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda p: open(os.path.join(ROOT, p)).read()
STEPS = {"1": "Discover", "2": "Define", "3": "Build", "4": "Govern and test", "5": "Release and adopt", "6": "Measure and iterate"}
SHORT = {"Discover": "Discover", "Define": "Define", "Build": "Build", "Govern": "Govern and test", "Release": "Release and adopt", "Measure": "Measure and iterate"}
cap = lambda t: t[:1].upper() + t[1:] if t else t
agents = []

# M1-M19: the delivery machine
for block in re.split(r"\n### ", read("playbook/agents.md"))[1:]:
    head, _, body = block.partition("\n")
    m = re.match(r"(M\d+)\. (.+)", head)
    if not m:
        continue
    f = dict(re.findall(r"^- \*\*([^*]+):\*\*\s*(.*)$", body.split("\n---")[0], re.M))
    steps = sorted({STEPS[n[0]] for n in re.findall(r"\d\.\d", f["Used in"])}, key=list(STEPS.values()).index)
    kind_aim = f["Kind"].split("→")[-1].strip().split()[0]
    agents.append({"id": m.group(1), "name": m.group(2), "group": "machine", "steps": steps, "aim": kind_aim,
                   "job": f["Job"], "meta": f"Used in {f['Used in']} · {f['Kind']}",
                   "fields": [(k, f[k]) for k in ["Starts when", "Inputs", "Allowed actions", "Not allowed", "Outputs", "Stops when", "Proof it worked", "Person in charge", "Runs on (guess)", "To confirm"]],
                   "source": "Delivery Playbook · agent library"})

memo = read("memos/rm-analytics-framework.md")
appa = memo.split("## Appendix A: Agent specs")[1].split("## Appendix B")[0]
# A1-A6: the product RMs use
for block in re.split(r"\n\*\*(?=A\d+\. )", appa.split("### Agents the team uses")[0])[1:]:
    head, _, body = block.partition("\n")
    m = re.match(r"(A\d+)\. (.+?)\*\*\s*·\s*(.+)", head)
    f = dict(re.findall(r"^- \*\*([^*]+):\*\*\s*(.*)$", body, re.M))
    agents.append({"id": m.group(1), "name": m.group(2), "group": "product", "steps": ["Used by RMs"], "aim": "",
                   "job": f["Job"], "meta": cap(m.group(3).strip()),
                   "fields": [(k, f[k]) for k in ["Inputs", "Allowed actions", "Not allowed", "Outputs", "Stops when", "Proof it worked", "Person in charge"] if k in f],
                   "source": "RM Analytics plan · Appendix A"})
# A7-A20: the RM project team
for row in appa.split("### Agents the team uses")[1].split("\n"):
    m = re.match(r"^\| \*\*(A\d+)\. ([^*]+)\*\* \|(.*)\|\s*$", row)
    if not m:
        continue
    c = [x.strip() for x in m.group(3).split("|")]
    step, job, inputs, allowed, outputs, stops, proof, owner = c
    agents.append({"id": m.group(1), "name": m.group(2), "group": "team", "steps": [SHORT[step]], "aim": "",
                   "job": job, "meta": f"{SHORT[step]} step",
                   "fields": [("Inputs", inputs), ("Allowed actions", allowed), ("Outputs", outputs), ("Stops when", stops), ("Proof it worked", proof), ("Person in charge", owner)],
                   "source": "RM Analytics plan · Appendix A"})

GROUPS = [("machine", "Run the delivery machine", "Help the team run any project through the six steps. Reused on every project."),
          ("team", "Help the RM project team", "The RM project's own helpers, one for each job the team does."),
          ("product", "The product RMs use", "The agents inside RM Analytics. Nothing reaches a client without the RM. Insights and alerts are shown to the RM and their manager; anything saved as the RM's own work, like a call note or an opportunity, needs the RM's approval.")]
counts = {g: sum(a["group"] == g for a in agents) for g, *_ in GROUPS}

def card(a):
    spec = "".join(f"<div><dt>{E(k)}</dt><dd>{inline(cap(v))}</dd></div>" for k, v in a["fields"])
    aim = chipify(a["aim"]) if a["aim"] else ""
    return (f'<details class="agcard" data-group="{a["group"]}" data-steps="{E("|".join(a["steps"]))}" '
            f'data-search="{E((a["id"] + " " + a["name"] + " " + a["job"]).lower())}">'
            f'<summary><span class="aid">{a["id"]}</span><span class="aname">{E(a["name"])}</span>{aim}'
            f'<span class="ajob">{inline(cap(a["job"]))}</span><span class="ameta">{inline(a["meta"])}</span></summary>'
            f'<dl class="spec">{spec}</dl><p class="asrc">Full spec: {E(a["source"])}</p></details>')

sections = ""
for g, name, why in GROUPS:
    cards = "".join(card(a) for a in agents if a["group"] == g)
    sections += f'<section class="grp" data-group="{g}"><div class="ahead"><h2>{E(name)} <span class="gcount">{counts[g]}</span></h2><p>{E(why)}</p></div><div class="aglist">{cards}</div></section>'

step_opts = "".join(f'<option value="{E(s)}">{E(s)}</option>' for s in list(STEPS.values()) + ["Used by RMs"])
page = f'''<title>Agent Library</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
[hidden]{{display:none!important}}
/* Layout: navy band with filters; three groups of agent cards; each card opens to its full spec. */
.filters{{display:flex;flex-wrap:wrap;gap:14px;margin-top:20px}}
.filters label{{display:flex;flex-direction:column;gap:6px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy);flex:1 1 200px;max-width:320px}}
.filters input,.filters select{{font:inherit;font-size:15px;text-transform:none;letter-spacing:0;padding:9px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:var(--onnavy)}}
.filters option{{color:#1B2433}}
.filters input::placeholder{{color:var(--onnavy-muted)}}
.ahead{{border-top:4px solid var(--navy);padding-top:20px}}
.ahead p{{color:var(--muted);margin:6px 0 0}}
.gcount{{font-family:var(--mono);font-size:15px;color:var(--teal);vertical-align:middle}}
.grp{{gap:14px}}
.aglist{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;align-items:start}}
.agcard{{background:var(--card);border:1px solid var(--line);border-radius:8px;min-width:0}}
.agcard[open]{{border-color:var(--teal)}}
.agcard summary{{cursor:pointer;list-style:none;padding:14px 16px;display:grid;grid-template-columns:auto 1fr auto;gap:4px 10px;align-items:baseline}}
.agcard summary::-webkit-details-marker{{display:none}}
.agcard summary:focus-visible{{outline:2px solid var(--teal);outline-offset:2px}}
.aid{{font-family:var(--mono);font-size:12px;color:var(--teal)}}
.aname{{font-family:var(--serif);font-weight:600;font-size:18px}}
.ajob{{grid-column:1/-1;font-size:14px;color:var(--fg)}}
.ameta{{grid-column:1/-1;font-family:var(--mono);font-size:11px;color:var(--muted)}}
.agcard summary::after{{content:"Show spec";grid-column:1/-1;font-size:13px;color:var(--teal);font-weight:500}}
.agcard[open] summary::after{{content:"Hide spec"}}
.agcard .spec{{margin:0;padding:0 16px 12px;display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line);padding-top:12px}}
.agcard .spec div{{display:grid;grid-template-columns:130px minmax(0,1fr);gap:10px}}
.agcard .spec dt{{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:2px}}
.agcard .spec dd{{margin:0;font-size:14px}}
.asrc{{margin:0;padding:0 16px 14px;font-size:12px;color:var(--muted)}}
.empty{{color:var(--muted)}}
@media (max-width:760px){{.aglist{{grid-template-columns:1fr}}.agcard .spec div{{grid-template-columns:1fr;gap:2px}}}}
</style>
<div class="band"><div class="wrap">
<span class="label">Building block · agents</span>
<h1>Agent Library</h1>
<p class="lede">All {len(agents)} agents in one place. Each one has a single job, a short list of things it may do, and a named person in charge. Open any card to see its full spec.</p>
<div class="filters">
<label for="q">Search<input id="q" type="search" placeholder="Like scheduler, Salesforce or sign-off" autocomplete="off"></label>
<label for="grp">Who it serves<select id="grp"><option value="">All agents</option>{"".join(f'<option value="{g}">{E(n)}</option>' for g, n, _ in GROUPS)}</select></label>
<label for="step">Step<select id="step"><option value="">Any step</option>{step_opts}</select></label>
</div>
</div></div>
<main class="wrap">
<div class="howto" style="display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px;color:var(--muted);align-items:center"><span>The chip shows what each machine agent aims to become:</span><span class="chip k-auto">Auto</span> runs on its own <span class="chip k-draft">Draft</span> drafts for a person to check</div>
{sections}
<p class="empty" id="none" hidden>No agents match. Try another word or clear the filters.</p>
<footer>Built from <code>playbook/agents.md</code> and the RM memo's Appendix A by <code>designs/agents-build.py</code>. "Runs on" tools are guesses until confirmed at the bank.</footer>
</main>
<script>
(function(){{
  var q=document.getElementById('q'), g=document.getElementById('grp'), st=document.getElementById('step'), none=document.getElementById('none');
  function run(){{
    var t=q.value.trim().toLowerCase(), gv=g.value, sv=st.value, shown=0;
    document.querySelectorAll('.grp').forEach(function(sec){{
      var any=false;
      sec.querySelectorAll('.agcard').forEach(function(a){{
        var hit=(!t||a.getAttribute('data-search').indexOf(t)>-1)&&(!gv||a.getAttribute('data-group')===gv)&&(!sv||a.getAttribute('data-steps').split('|').indexOf(sv)>-1);
        a.hidden=!hit; if(hit){{any=true;shown++;}}
      }});
      sec.hidden=!any;
    }});
    none.hidden=shown>0;
  }}
  [q,g,st].forEach(function(el){{el.addEventListener('input',run);el.addEventListener('change',run);}});
}})();
</script>
'''
open(os.path.join(ROOT, "designs", "agents.html"), "w").write(page)
print(len(agents), counts)
