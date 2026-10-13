"""Builds designs/library.html, the Document Library, from designs/library.json.
To add a document: add it to library.json (and designs/README.md), run this, republish.
Run: python3 designs/library-build.py"""
import html, json, os, re
from pagekit import CSS, E

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib = json.load(open(os.path.join(ROOT, "designs", "library.json")))

STATUS = {"In use": "s-use", "Waiting for review": "s-review", "Draft": "s-review", "In progress": "s-review", "Reference": "s-ref"}
docs = {}
for a in lib["areas"]:
    for d in [a["parent"]] + a["children"]:
        if d["status"] not in STATUS:
            raise SystemExit(f"Unknown status for {d['name']}: {d['status']}")
        docs[d["id"]] = (d, a)

def card(d, cls):
    return (f'<a class="doc {cls}" href="{E(d["url"])}" target="_blank" rel="noopener" '
            f'data-search="{E((d["name"] + " " + d["what"] + " " + d["status"]).lower())}">'
            f'<span class="top"><span class="name">{E(d["name"])}</span><span class="status {STATUS[d["status"]]}">{E(d["status"])}</span></span>'
            f'<span class="what">{E(d["what"])}</span>'
            f'<span class="src">Working copy: {E(d["source"])}</span></a>')

start = "".join(
    f'<a class="start" href="{E(docs[i][0]["url"])}" target="_blank" rel="noopener"><span class="area">{E(docs[i][1]["name"])}</span>'
    f'<span class="name">{E(docs[i][0]["name"])}</span><span class="what">{E(docs[i][0]["what"])}</span></a>'
    for i in lib["start_here"])

areas = ""
for a in lib["areas"]:
    kids = "".join(f'<li>{card(c, "child")}</li>' for c in a["children"])
    areas += (f'<section class="area" id="{E(a["id"])}"><div class="ahead"><h2>{E(a["name"])}</h2><p>{E(a["why"])}</p></div>'
              f'<div class="tree">{card(a["parent"], "parent")}'
              + (f'<ul class="kids" aria-label="Under {E(a["parent"]["name"])}">{kids}</ul>' if kids else "")
              + '</div></section>')

blocks = "".join(
    f'<a class="block" href="{E(b["url"])}" target="_blank" rel="noopener" data-search="{E((b["name"] + " " + b["what"]).lower())}">'
    f'<span class="bcount">{E(b["count"])}</span><span class="name">{E(b["name"])}</span><span class="what">{E(b["what"])}</span>'
    f'<span class="status {STATUS[b["status"]]}">{E(b["status"])}</span></a>' for b in lib["building_blocks"])
nav = '<a href="#index">Index</a><a href="#blocks">By building block</a><a href="#docs">By document</a>' + "".join(f'<a href="#{E(a["id"])}">{E(a["name"])}<span class="count">{1 + len(a["children"])}</span></a>' for a in lib["areas"])
total = len(docs)

# The index: every page and its sections, read from each page's own source so it can't drift.
# A page's sections come from its own jump menu (first <nav> with # links), else its <h2 id> headings.
# Pages with no section links (the RM design canvas) are listed by name only.
PAGE_FILE = {"open-items": "open-items.html", "job-description": "job-description.html", "bank-business": "bank-business.html",
             "tech-stack": "tech-stack.html", "job-notes": "job-notes.html", "framework": "product-framework.html",
             "delivery-machine": "delivery-machine.html", "playbook": "playbook.html", "workflow": "role-workflow.html",
             "rm-design": None, "rm-plan": "rm-analytics-plan.html", "mckinsey-use-cases": "mckinsey-use-cases.html",
             "prompting": "prompting.html", "credit-market-scan": "credit-market-scan.html", "workflows": "workflows.html", "agents": "agents.html", "steps": "steps.html",
             "controls": "controls.html", "glossary": "glossary.html"}

def text(h):
    h = re.sub(r'<span class="g?count">.*?</span>', "", h)  # drop item counts like "19"
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).replace(" ,", ",").strip())

def sections(page_id):
    if page_id not in PAGE_FILE:
        raise SystemExit(f"library-build.py: add {page_id} to PAGE_FILE (its .html file, or None)")
    f = PAGE_FILE[page_id]
    if not f:
        return []
    src = open(os.path.join(ROOT, "designs", f)).read()
    for nav in re.findall(r"<nav[^>]*>(.*?)</nav>", src, re.S):
        links = re.findall(r'<a[^>]*href="#([^"]+)"[^>]*>(.*?)</a>', nav, re.S)
        if links:
            return [(i, text(t)) for i, t in links]
    return [(i, text(t)) for i, t in re.findall(r'<h2[^>]*\sid="([^"]+)"[^>]*>(.*?)</h2>', src, re.S)]

def ientry(d):
    # One row per page. Pages with sections are a twisty: click the row to open its sections; click the name to open the page.
    secs = sections(d["id"])
    name = f'<a class="ipage" href="{E(d["url"])}" target="_blank" rel="noopener">{E(d["name"])}</a>'
    if not secs:
        return f'<div class="ientry plain" data-search="{E(d["name"].lower())}">{name}<span class="ic">{E(d.get("index_note", "Opens at the top"))}</span></div>'
    links = "".join(f'<li><a href="{E(d["url"])}#{E(i)}" target="_blank" rel="noopener" data-search="{E(t.lower())}">{E(t)}</a></li>' for i, t in secs)
    return (f'<details class="ientry" data-search="{E(d["name"].lower())}"><summary>{name}<span class="ic">{len(secs)} sections</span></summary>'
            f'<ul class="isecs">{links}</ul></details>')

igroups = [("Building blocks", lib["building_blocks"])] + [(a["name"], [a["parent"]] + a["children"]) for a in lib["areas"]]
index = "".join(f'<div class="igroup"><h3>{E(n)}</h3>{"".join(ientry(d) for d in ds)}</div>' for n, ds in igroups)
nsecs = sum(len(sections(d["id"])) for _, ds in igroups for d in ds)
npages = sum(len(ds) for _, ds in igroups)

page = f'''<title>Document Library</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
[hidden]{{display:none!important}}
/* Layout: navy band with area pills and a filter; a "start here" row; then one section per area, each a parent card with its children hanging off a tree line. */
.count{{font-family:var(--mono);font-size:12px;color:var(--label-on-navy);margin-left:8px}}
.filter{{margin-top:20px;max-width:420px}}
.filter label{{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy);margin-bottom:6px}}
.filter input{{width:100%;font:inherit;font-size:16px;padding:10px 14px;border-radius:8px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:var(--onnavy)}}
.filter input::placeholder{{color:var(--onnavy-muted)}}
.filter input:focus-visible{{outline:2px solid var(--label-on-navy);outline-offset:2px}}
.starts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}
.start{{background:var(--navy);color:var(--onnavy);border-radius:8px;padding:18px 20px;text-decoration:none;display:flex;flex-direction:column;gap:6px;min-height:100%}}
.start:hover{{filter:brightness(1.15)}}
.start .area{{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy)}}
.start .name{{font-family:var(--serif);font-size:20px;font-weight:600}}
.start .what{{font-size:14px;color:var(--onnavy-muted)}}
.area{{gap:14px}}
.bintro{{color:var(--muted);margin:4px 0 4px}}
.blocks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.block{{background:var(--teal-bg);border:1px solid var(--line);border-radius:8px;padding:20px 22px;text-decoration:none;color:var(--fg);display:flex;flex-direction:column;gap:6px;align-items:flex-start}}
.block:hover{{border-color:var(--teal)}}
.block .bcount{{font-family:var(--mono);font-size:12px;color:var(--teal)}}
.block .name{{font-family:var(--serif);font-size:24px;font-weight:600}}
.block .what{{font-size:15px;color:var(--fg)}}
.ahead{{border-top:4px solid var(--navy);padding-top:20px}}
.ahead p{{color:var(--muted);margin:6px 0 0}}
.tree{{display:flex;flex-direction:column;gap:0}}
.doc{{display:flex;flex-direction:column;gap:6px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px 20px;text-decoration:none;color:var(--fg);min-width:0}}
.doc:hover{{border-color:var(--teal)}}
.doc .top{{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:baseline;justify-content:space-between}}
.doc .name{{font-family:var(--serif);font-weight:600;font-size:19px;color:var(--fg)}}
.doc.parent .name{{font-size:23px}}
.doc .what{{font-size:15px;color:var(--muted)}}
.doc .src{{font-family:var(--mono);font-size:11px;color:var(--muted)}}
.status{{font-family:var(--mono);font-size:11px;letter-spacing:.04em;padding:3px 9px;border-radius:999px;white-space:nowrap}}
.s-use{{background:var(--teal-bg);color:var(--teal)}}
.s-review{{background:var(--amber-bg);color:var(--amber)}}
.s-ref{{background:var(--partner-bg);color:var(--partner)}}
.kids{{list-style:none;margin:0 0 0 26px;padding:0;border-left:2px solid var(--line);display:flex;flex-direction:column;gap:10px;padding-top:10px}}
.kids li{{position:relative;padding-left:22px;margin:0}}
.kids li::before{{content:"";position:absolute;left:0;top:28px;width:16px;border-top:2px solid var(--line)}}
.legend{{display:flex;flex-wrap:wrap;gap:10px 18px;font-size:14px;color:var(--muted);align-items:center}}
.empty{{color:var(--muted)}}
/* Index: area groups flow in columns; each page name in bold, its sections as links on a thin rule. */
.index{{columns:2 380px;column-gap:24px}}
.igroup{{break-inside:avoid-column;margin:0 0 18px}}
.igroup h3{{font-family:var(--mono);font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin:0 0 6px}}
.ientry{{background:var(--card);border:1px solid var(--line);border-radius:8px;margin:0 0 6px;break-inside:avoid}}
.ientry>summary,.ientry.plain{{display:flex;align-items:baseline;gap:12px;padding:10px 16px}}
.ientry>summary{{cursor:pointer;list-style:none}}
.ientry>summary::-webkit-details-marker{{display:none}}
.ientry>summary::before{{content:"\\25B8";color:var(--teal);width:12px;flex:none}}
.ientry[open]>summary::before{{content:"\\25BE"}}
.ientry>summary:focus-visible{{outline:2px solid var(--teal);outline-offset:2px;border-radius:8px}}
.ientry[open]{{border-color:var(--teal)}}
.ipage{{font-family:var(--serif);font-weight:600;font-size:17px;color:var(--fg);text-decoration:none;margin-right:auto}}
.ipage:hover{{text-decoration:underline;color:var(--teal)}}
.ic{{font-family:var(--mono);font-size:12px;color:var(--muted);white-space:nowrap}}
.ientry.plain{{flex-wrap:wrap;row-gap:2px}}
.isecs{{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:0 16px 12px}}
.isecs li{{margin:0}}
.isecs a{{display:block;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;color:var(--fg);text-decoration:none}}
.isecs a:hover{{border-color:var(--teal);color:var(--teal)}}
@media (max-width:760px){{.starts,.blocks{{grid-template-columns:1fr}}.kids{{margin-left:10px}}.kids li{{padding-left:14px}}.kids li::before{{width:10px}}}}
</style>
<div class="band"><div class="wrap">
<span class="label">Everything in my Claude brain</span>
<h1>Document Library</h1>
<p class="lede">Everything in one place: an index of every page and its sections, then two ways in: by building block (workflows and agents) or by document, with each document under the one it belongs to. Click any card to open it.</p>
<nav class="stepnav" aria-label="Areas">{nav}</nav>
<div class="filter"><label for="q">Find a document</label><input id="q" type="search" placeholder="Type a word, like plan, agent or prompt" autocomplete="off"></div>
</div></div>
<main class="wrap">
<section id="index"><span class="label">Index</span><h2 style="margin-top:4px">Every page and its sections</h2><p class="bintro">{npages} pages, {nsecs} sections. Click the arrow (&#9656;) to see a page&#x27;s sections, then click one to jump to it. Click a page name to open the page.</p><div class="index">{index}</div></section>
<section id="blocks"><span class="label">Browse by building block</span><p class="bintro">The things people look for, pulled out of the documents into their own pages.</p><div class="blocks">{blocks}</div></section>
<section id="docs"><span class="label">By document</span><h2 style="margin-top:4px">Start here</h2><div class="starts">{start}</div></section>
<div class="legend"><span>Status:</span><span class="status s-use">In use</span><span class="status s-review">Waiting for review</span><span class="status s-review">Draft</span><span class="status s-review">In progress</span><span class="status s-ref">Reference</span></div>
{areas}
<p class="empty" id="none" hidden>No documents match that word.</p>
<footer>Built from <code>designs/library.json</code>. Say <strong>/documents</strong> to Claude to refresh it. Every page is private until you share it from its Share menu.</footer>
</main>
<script>
(function(){{
  var q=document.getElementById('q'), none=document.getElementById('none');
  q.addEventListener('input',function(){{
    var t=q.value.trim().toLowerCase(), shown=0;
    document.querySelectorAll('.block').forEach(function(b){{var hit=!t||b.getAttribute('data-search').indexOf(t)>-1;b.hidden=!hit;if(hit)shown++;}});
    document.querySelectorAll('.area').forEach(function(sec){{
      var any=false;
      sec.querySelectorAll('.doc').forEach(function(d){{
        var hit=!t||d.getAttribute('data-search').indexOf(t)>-1;
        var box=d.parentElement.tagName==='LI'?d.parentElement:d;
        box.hidden=!hit; if(hit){{any=true;shown++;}}
      }});
      sec.hidden=!any;
    }});
    document.querySelectorAll('.ientry').forEach(function(e){{
      // A page shows if its name or any section matches; while searching, a twisty opens when one of its sections matches.
      var pageHit=!t||e.getAttribute('data-search').indexOf(t)>-1, secHit=false;
      e.querySelectorAll('.isecs a').forEach(function(a){{var hit=!!t&&a.getAttribute('data-search').indexOf(t)>-1;a.parentElement.hidden=!(pageHit||hit);if(hit)secHit=true;}});
      e.hidden=!(pageHit||secHit); if(!e.hidden)shown++;
      if(e.tagName==='DETAILS')e.open=secHit;
    }});
    document.querySelectorAll('.igroup').forEach(function(g){{g.hidden=!g.querySelector('.ientry:not([hidden])');}});
    none.hidden=shown>0;
  }});
}})();
</script>
'''
open(os.path.join(ROOT, "designs", "library.html"), "w").write(page)
