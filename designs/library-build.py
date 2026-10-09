"""Builds designs/library.html, the Document Library, from designs/library.json.
To add a document: add it to library.json (and designs/README.md), run this, republish.
Run: python3 designs/library-build.py"""
import json, os
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

nav = "".join(f'<a href="#{E(a["id"])}">{E(a["name"])}<span class="count">{1 + len(a["children"])}</span></a>' for a in lib["areas"])
total = len(docs)

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
@media (max-width:760px){{.starts{{grid-template-columns:1fr}}.kids{{margin-left:10px}}.kids li{{padding-left:14px}}.kids li::before{{width:10px}}}}
</style>
<div class="band"><div class="wrap">
<span class="label">Everything in my Claude brain</span>
<h1>Document Library</h1>
<p class="lede">All {total} documents in one place, grouped by what they're for. Each document sits under the one it belongs to. Click any card to open it.</p>
<nav class="stepnav" aria-label="Areas">{nav}</nav>
<div class="filter"><label for="q">Find a document</label><input id="q" type="search" placeholder="Type a word, like plan, agent or prompt" autocomplete="off"></div>
</div></div>
<main class="wrap">
<section><span class="label">Start here</span><div class="starts">{start}</div></section>
<div class="legend"><span>Status:</span><span class="status s-use">In use</span><span class="status s-review">Waiting for review</span><span class="status s-review">Draft</span><span class="status s-ref">Reference</span></div>
{areas}
<p class="empty" id="none" hidden>No documents match that word.</p>
<footer>Built from <code>designs/library.json</code>. Say <strong>/documents</strong> to Claude to refresh it. Every page is private until you share it from its Share menu.</footer>
</main>
<script>
(function(){{
  var q=document.getElementById('q'), none=document.getElementById('none');
  q.addEventListener('input',function(){{
    var t=q.value.trim().toLowerCase(), shown=0;
    document.querySelectorAll('.area').forEach(function(sec){{
      var any=false;
      sec.querySelectorAll('.doc').forEach(function(d){{
        var hit=!t||d.getAttribute('data-search').indexOf(t)>-1;
        var box=d.parentElement.tagName==='LI'?d.parentElement:d;
        box.hidden=!hit; if(hit){{any=true;shown++;}}
      }});
      sec.hidden=!any;
    }});
    none.hidden=shown>0;
  }});
}})();
</script>
'''
open(os.path.join(ROOT, "designs", "library.html"), "w").write(page)
