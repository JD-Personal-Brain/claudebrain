"""Builds two building-block pages, so any sub-step or control can be found on its own:
- designs/steps.html, the Steps Catalog: every playbook sub-step (from playbook/[1-6]-*.md),
  with its tasks and their kinds from the tables in product-framework.md.
- designs/controls.html, the Controls Catalog: every governance control (from playbook/controls.md).
Run: python3 designs/catalogs-build.py"""
import glob, os, re
from pagekit import CSS, E, inline, chipify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
read = lambda p: open(os.path.join(ROOT, p)).read()
STEPS = {"1": "Discover", "2": "Define", "3": "Build", "4": "Govern and test", "5": "Release and adopt", "6": "Measure and iterate"}
cap = lambda t: t[:1].upper() + t[1:] if t else t

HEAD = '''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">'''
STYLE = '''
[hidden]{display:none!important}
/* Layout: navy band with a search box and one filter; groups of cards; each card opens to its details. */
.filters{display:flex;flex-wrap:wrap;gap:14px;margin-top:20px}
.filters label{display:flex;flex-direction:column;gap:6px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy);flex:1 1 200px;max-width:320px}
.filters input,.filters select{font:inherit;font-size:15px;text-transform:none;letter-spacing:0;padding:9px 12px;border-radius:8px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:var(--onnavy)}
.filters option{color:#1B2433}
.filters input::placeholder{color:var(--onnavy-muted)}
.filters input:focus-visible,.filters select:focus-visible{outline:2px solid var(--label-on-navy);outline-offset:2px}
.ahead{border-top:4px solid var(--navy);padding-top:20px}
.ahead p{color:var(--muted);margin:6px 0 0}
.gcount{font-family:var(--mono);font-size:15px;color:var(--teal);vertical-align:middle}
.grp{gap:14px}
.clist{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;align-items:start}
.ccard{background:var(--card);border:1px solid var(--line);border-radius:8px;min-width:0}
.ccard[open]{border-color:var(--teal)}
.ccard summary{cursor:pointer;list-style:none;padding:14px 16px;display:grid;grid-template-columns:auto 1fr;gap:4px 10px;align-items:baseline}
.ccard summary::-webkit-details-marker{display:none}
.ccard summary:focus-visible{outline:2px solid var(--teal);outline-offset:2px}
.cid{font-family:var(--mono);font-size:12px;color:var(--teal);font-variant-numeric:tabular-nums}
.cname{font-family:var(--serif);font-weight:600;font-size:18px}
.cwhat{grid-column:1/-1;font-size:14px;color:var(--fg)}
.cmeta{grid-column:1/-1;font-family:var(--mono);font-size:11px;color:var(--muted)}
.ccard summary::after{content:"Show details";grid-column:1/-1;font-size:13px;color:var(--teal);font-weight:500}
.ccard[open] summary::after{content:"Hide details"}
.ccard .spec{margin:0;padding:12px 16px;display:flex;flex-direction:column;gap:6px;border-top:1px solid var(--line)}
.ccard .spec div{display:grid;grid-template-columns:130px minmax(0,1fr);gap:10px}
.ccard .spec dt{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:2px}
.ccard .spec dd{margin:0;font-size:14px}
.tasks{margin:0;padding:0 16px 12px;list-style:none;display:flex;flex-direction:column;gap:6px;font-size:14px}
.tasks li{margin:0}
.csrc{margin:0;padding:0 16px 14px;font-size:12px;color:var(--muted);max-width:none}
.empty{color:var(--muted)}
.howto{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px;color:var(--muted);align-items:center}
@media (max-width:760px){.clist{grid-template-columns:1fr}.ccard .spec div{grid-template-columns:1fr;gap:2px}}
'''
SCRIPT = '''<script>
(function(){
  var q=document.getElementById('q'), g=document.getElementById('grp'), none=document.getElementById('none');
  function run(){
    var t=q.value.trim().toLowerCase(), gv=g.value, shown=0;
    document.querySelectorAll('.grp').forEach(function(sec){
      var any=false;
      sec.querySelectorAll('.ccard').forEach(function(a){
        var hit=(!t||a.getAttribute('data-search').indexOf(t)>-1)&&(!gv||a.getAttribute('data-group')===gv);
        a.hidden=!hit; if(hit){any=true;shown++;}
      });
      sec.hidden=!any;
    });
    none.hidden=shown>0;
  }
  [q,g].forEach(function(el){el.addEventListener('input',run);el.addEventListener('change',run);});
})();
</script>
'''

def page(title, label, lede, group_label, groups, sections, howto, footer, placeholder, out):
    opts = "".join(f'<option value="{E(g)}">{E(g)}</option>' for g in groups)
    html = f'''<title>{E(title)}</title>
{HEAD}
<style>{CSS}{STYLE}</style>
<div class="band"><div class="wrap">
<span class="label">{E(label)}</span>
<h1>{E(title)}</h1>
<p class="lede">{E(lede)}</p>
<div class="filters">
<label for="q">Search<input id="q" type="search" placeholder="{E(placeholder)}" autocomplete="off"></label>
<label for="grp">{E(group_label)}<select id="grp"><option value="">All</option>{opts}</select></label>
</div>
</div></div>
<main class="wrap">
{howto}
{sections}
<p class="empty" id="none" hidden>Nothing matches. Try another word or clear the filter.</p>
<footer>{footer}</footer>
</main>
{SCRIPT}'''
    open(os.path.join(ROOT, "designs", out), "w").write(html)

def fields_of(body):
    """Top-level '- **Name:** text' lines, with any indented lines under them joined on."""
    out, cur = {}, None
    for ln in body.split("\n"):
        m = re.match(r"^- \*\*([^*]+):\*\*\s*(.*)$", ln)
        if m:
            cur = m.group(1); out[cur] = m.group(2)
        elif cur and ln.startswith("  ") and ln.strip():
            out[cur] = (out[cur] + " " + re.sub(r"^\s*(-|\d+\.)\s*", "", ln)).strip()
        elif not ln.startswith("  "):
            cur = None
    return out

# ---------- Steps Catalog ----------
fw = read("product-framework.md")
tasks = {}
for m in re.finditer(r"^\| (\d\.\d) \| ([^|]+) \| ([^|]+) \| [^|]* \| ([^|]+) \|", fw, re.M):
    tasks.setdefault(m.group(1), []).append((m.group(2).strip(), m.group(3).strip(), m.group(4).strip()))

subs = []
for f in sorted(glob.glob(os.path.join(ROOT, "playbook", "[1-6]-*.md"))):
    s = open(f).read()
    for part in re.split(r"\n## ", s)[1:]:
        head, _, body = part.partition("\n")
        m = re.match(r"^(\d\.\d) (.+)$", head)
        if m:
            subs.append((m.group(1), m.group(2), fields_of(body.split("\n---")[0])))

def step_card(num, name, f):
    step = STEPS[num[0]]
    rows = "".join(f"<li>{chipify(k)} {inline(t)} <span class=\"cmeta\">→ {inline(to)}</span></li>" for t, k, to in tasks.get(num, []))
    spec = "".join(f"<div><dt>{E(k)}</dt><dd>{inline(cap(f[k]))}</dd></div>" for k in ["Why it matters", "Output", "Done when"] if f.get(k))
    return (f'<details class="ccard" data-group="{E(step)}" data-search="{E((num + " " + name + " " + " ".join(f.get(k, "") for k in ["Goal", "Why it matters", "Output", "Done when"]) + " " + " ".join(t for t, _, _ in tasks.get(num, []))).lower())}">'
            f'<summary><span class="cid">{num}</span><span class="cname">{inline(name)}</span>'
            f'<span class="cwhat">{inline(cap(f.get("Goal", "")))}</span><span class="cmeta">{E(step)} step · {len(tasks.get(num, []))} task{"" if len(tasks.get(num, [])) == 1 else "s"}</span></summary>'
            f'<dl class="spec">{spec}</dl><ul class="tasks" aria-label="Tasks in {num}">{rows}</ul>'
            f'<p class="csrc">How to do it the first time: Delivery Playbook, step {num[0]}, sub-step {num}</p></details>')

sections = ""
for n, step in STEPS.items():
    mine = [x for x in subs if x[0][0] == n]
    sections += (f'<section class="grp"><div class="ahead"><h2>{n}. {E(step)} <span class="gcount">{len(mine)}</span></h2></div>'
                 f'<div class="clist">{"".join(step_card(*x) for x in mine)}</div></section>')
howto = ('<div class="howto"><span>Each task is marked with who does it once the machine is running:</span>'
         '<span><span class="chip k-auto">Auto</span>runs on its own</span><span><span class="chip k-draft">Draft</span>AI drafts, a person checks</span>'
         '<span><span class="chip k-me">Me</span>only a person</span><span><span class="chip k-partner">Partner</span>a partner\'s sign-off</span></div>')
page("Steps Catalog", "Building block · steps",
     f"All {len(subs)} sub-steps of the six-step delivery process in one place. Open any card to see why it matters, what it produces and its tasks.",
     "Step", list(STEPS.values()), sections, howto,
     "Built from the Delivery Playbook and the task tables in the Product Framework, so it always matches them. Tools and task kinds are guesses until confirmed at the bank.",
     "Like sign-off or pilot", "steps.html")

# ---------- Controls Catalog ----------
controls = []
for block in re.split(r"\n### ", read("playbook/controls.md"))[1:]:
    head, _, body = block.partition("\n")
    m = re.match(r"(K\d+)\. (.+)", head)
    controls.append((m.group(1), m.group(2), fields_of(body)))
NEED = ["Group", "What it is", "Why it matters", "Set in", "Built in", "Proved in", "Watched in", "Tool (guess)", "Proof"]
for cid, name, f in controls:
    missing = [k for k in NEED if not f.get(k)]
    if missing:
        raise SystemExit(f"{cid} is missing fields: {missing}")
real = {x[0] for x in subs}
for cid, name, f in controls:
    for k in ["Set in", "Built in", "Proved in", "Watched in"]:
        for n in re.findall(r"\b\d\.\d\b", f[k]):
            if n not in real:
                raise SystemExit(f"{cid} '{k}' names sub-step {n}, which isn't in the playbook")
groups = []
for _, _, f in controls:
    if f["Group"] not in groups:
        groups.append(f["Group"])

def stages(text):
    # every sub-step number the field names (not just the first), and say so when part is missing
    nums = list(dict.fromkeys(re.findall(r"\b\d\.\d\b", text)))
    if not nums:
        return "not covered yet"
    return ", ".join(nums) + (" (partly not covered)" if "not covered" in text else "")

def control_card(cid, name, f):
    spec = "".join(f"<div><dt>{E(k)}</dt><dd>{inline(cap(f[k]))}</dd></div>" for k in NEED[2:])
    return (f'<details class="ccard" data-group="{E(f["Group"])}" data-search="{E((cid + " " + name + " " + " ".join(f[k] for k in ["Group", "What it is", "Why it matters", "Tool (guess)", "Proof"])).lower())}">'
            f'<summary><span class="cid">{cid}</span><span class="cname">{inline(name)}</span>'
            f'<span class="cwhat">{inline(cap(f["What it is"]))}</span><span class="cmeta">Set: {E(stages(f["Set in"]))} · Proved: {E(stages(f["Proved in"]))}</span></summary>'
            f'<dl class="spec">{spec}</dl><p class="csrc">Numbers such as 2.4 are playbook sub-steps: look them up in the Steps Catalog.</p></details>')

sections = ""
for g in groups:
    mine = [c for c in controls if c[2]["Group"] == g]
    sections += (f'<section class="grp"><div class="ahead"><h2>{E(g)} <span class="gcount">{len(mine)}</span></h2></div>'
                 f'<div class="clist">{"".join(control_card(*c) for c in mine)}</div></section>')
howto = ('<div class="note"><span class="warn">⚠️</span> Gathered from my own framework and playbook, not from Associated Bank. '
         "The bank's own control list comes from its risk partner early in the Define step, and it replaces this one where they differ. "
         "Numbers such as 2.4 are sub-steps of my six-step process: look them up in the Steps Catalog.</div>")
page("Controls Catalog", "Building block · controls",
     f"All {len(controls)} governance controls in one place: the safeguards built into every AI product, with where each is set, built, proved and watched.",
     "Kind of control", groups, sections, howto,
     "Built from my controls list (kept with the playbook). \"Tool\" lines are guesses until confirmed at the bank.",
     "Like approval or data", "controls.html")
print(len(subs), "sub-steps;", len(controls), "controls")
