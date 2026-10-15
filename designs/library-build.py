"""Builds designs/library.html, the Document Library, from designs/library.json.
The page is one index in five numbered sections (the bank, how we deliver, relationship managers,
portfolio managers, reference), one row per page. A row shows the page's status;
its twisty opens a one-line description and the page's sections. Placeholder rows mark
pages still to build. A section marked "numbered" in library.json (how we deliver) shows
plain numbered rows instead, read in order: click the name to open the page.
To add a document: add it to library.json (and designs/README.md) and to PAGE_FILE below,
run this, republish.
Run: python3 designs/library-build.py"""
import html, json, os, re
from pagekit import CSS, E

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lib = json.load(open(os.path.join(ROOT, "designs", "library.json")))

STATUS = {"In use": "s-use", "Waiting for review": "s-review", "Draft": "s-review", "In progress": "s-review", "Reference": "s-ref",
          "To build": "s-todo", "Later": "s-todo"}
# Sections in page order, from library.json. An item is a page, or a placeholder ("todo") for one still to build.
groups = [(g["name"], g["why"], g["items"], g.get("numbered", False)) for g in lib["groups"]]
for _, _, ds, _ in groups:
    for d in ds:
        if d["status"] not in STATUS:
            raise SystemExit(f"Unknown status for {d['name']}: {d['status']}")

# The index: every page and its sections, read from each page's own source so it can't drift.
# A page's sections come from its own jump menu (first <nav> with # links), else its <h2 id> headings.
# Pages with no section links (the RM design canvas) are listed by name only.
PAGE_FILE = {"open-items": "open-items.html", "job-description": "job-description.html", "bank-business": "bank-business.html",
             "tech-stack": "tech-stack.html", "framework": "product-framework.html",
             "product-machine": "product-machine.html", "playbook": "playbook.html", "workflow": "role-workflow.html",
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

def chip(d):
    return f'<span class="status {STATUS[d["status"]]}">{E(d["status"])}</span>'

def entry(d, num=None):
    if num:
        # Numbered rows: reading order, name and status only; the name opens the page.
        return (f'<div class="ientry plain numbered" data-search="{E((d["name"] + " " + d["what"]).lower())}"><span class="inum">{num}</span>'
                f'<a class="ipage" href="{E(d["url"])}" target="_blank" rel="noopener">{E(d["name"])}</a>{chip(d)}</div>')
    if d.get("todo"):
        return f'<div class="ientry plain todo" data-search="{E((d["name"] + " " + d["what"]).lower())}"><span class="ipage">{E(d["name"])}</span>{chip(d)}<p class="idesc">{E(d["what"])}</p></div>'
    # Pages with sections are a twisty: click the row to open it; click the name to open the page.
    secs = sections(d["id"])
    search = E((d["name"] + " " + d["what"]).lower())
    name = f'<a class="ipage" href="{E(d["url"])}" target="_blank" rel="noopener">{E(d["name"])}</a>'
    if not secs:
        note = (" " + d["index_note"]) if d.get("index_note") else ""
        return f'<div class="ientry plain" data-search="{search}">{name}{chip(d)}<p class="idesc">{E(d["what"] + note)}</p></div>'
    links = "".join(f'<li><a href="{E(d["url"])}#{E(i)}" target="_blank" rel="noopener" data-search="{E(t.lower())}">{E(t)}</a></li>' for i, t in secs)
    return (f'<details class="ientry" data-search="{search}"><summary>{name}{chip(d)}<span class="ic" title="Sections">{len(secs)}</span></summary>'
            f'<p class="idesc">{E(d["what"])}</p><ul class="isecs">{links}</ul></details>')

index = "".join(f'<div class="igroup" id="g{i}"><h3><span class="gnum">{i+1}</span>{E(n)}</h3><p class="gwhy">{E(why)}</p>{"".join(entry(d, k + 1 if numbered else None) for k, d in enumerate(ds))}</div>' for i, (n, why, ds, numbered) in enumerate(groups))
nav = "".join(f'<a href="#g{i}"><span class="num">{i+1}</span>{E(n)}</a>' for i, (n, _, _, _) in enumerate(groups))

page = f'''<title>Document Library</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>{CSS}
[hidden]{{display:none!important}}
/* Layout: navy band with numbered section pills and a filter; then one column of numbered sections, one row per page. */
.count{{font-family:var(--mono);font-size:12px;color:var(--label-on-navy);margin-left:8px}}
.filter{{margin-top:20px;max-width:420px}}
.filter label{{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--label-on-navy);margin-bottom:6px}}
.filter input{{width:100%;font:inherit;font-size:16px;padding:10px 14px;border-radius:8px;border:1px solid rgba(255,255,255,.3);background:rgba(255,255,255,.08);color:var(--onnavy)}}
.filter input::placeholder{{color:var(--onnavy-muted)}}
.filter input:focus-visible{{outline:2px solid var(--label-on-navy);outline-offset:2px}}
.status{{font-family:var(--mono);font-size:11px;letter-spacing:.04em;padding:3px 9px;border-radius:999px;white-space:nowrap;flex:none}}
.s-use{{background:var(--teal-bg);color:var(--teal)}}
.s-review{{background:var(--amber-bg);color:var(--amber)}}
.s-ref{{background:var(--partner-bg);color:var(--partner)}}
.index{{max-width:760px}}
.igroup{{margin:0 0 28px;scroll-margin-top:16px}}
.igroup h3{{font-family:var(--serif);font-size:22px;font-weight:600;margin:0;display:flex;gap:12px;align-items:baseline}}
.gnum{{font-family:var(--mono);font-size:14px;color:var(--teal)}}
.gwhy{{color:var(--muted);font-size:15px;margin:2px 0 10px}}
.s-todo{{background:transparent;border:1px dashed var(--line);color:var(--muted)}}
.ientry.todo{{background:transparent;border-style:dashed}}
.ientry.todo .ipage{{color:var(--muted)}}
.ientry{{background:var(--card);border:1px solid var(--line);border-radius:8px;margin:0 0 6px}}
.ientry>summary,.ientry.plain{{display:flex;align-items:baseline;gap:12px;padding:10px 16px}}
.ientry>summary{{cursor:pointer;list-style:none}}
.ientry>summary::-webkit-details-marker{{display:none}}
.ientry>summary::before{{content:"\\25B8";color:var(--teal);width:12px;flex:none}}
.ientry[open]>summary::before{{content:"\\25BE"}}
.ientry>summary:focus-visible{{outline:2px solid var(--teal);outline-offset:2px;border-radius:8px}}
.ientry[open]{{border-color:var(--teal)}}
.ientry.plain{{flex-wrap:wrap;row-gap:2px}}
.ipage{{font-family:var(--serif);font-weight:600;font-size:17px;color:var(--fg);text-decoration:none;margin-right:auto}}
.ipage:hover{{text-decoration:underline;color:var(--teal)}}
.ic{{font-family:var(--mono);font-size:12px;color:var(--muted);white-space:nowrap}}
.idesc{{margin:0;padding:0 16px 10px 40px;font-size:14px;color:var(--muted);max-width:none}}
.ientry.plain .idesc{{padding:0;flex-basis:100%}}
.inum{{font-family:var(--mono);font-size:14px;color:var(--teal);width:12px;flex:none}}
.isecs{{list-style:none;display:flex;flex-wrap:wrap;gap:6px;margin:0;padding:0 16px 12px}}
.isecs li{{margin:0}}
.isecs a{{display:block;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;color:var(--fg);text-decoration:none}}
.isecs a:hover{{border-color:var(--teal);color:var(--teal)}}
.empty{{color:var(--muted)}}
</style>
<div class="band"><div class="wrap">
<span class="label">The program</span>
<h1>Document Library</h1>
<p class="lede">The AI program for Associated Bank&#x27;s relationship managers and credit team: the bank, each group&#x27;s work and core use cases, how we deliver, and reference.</p>
<nav class="stepnav" aria-label="Sections">{nav}</nav>
<div class="filter"><label for="q">Find a document</label><input id="q" type="search" placeholder="Type a word, like plan, agent or prompt" autocomplete="off"></div>
</div></div>
<main class="wrap">
<section id="index"><div class="index">{index}</div></section>
<p class="empty" id="none" hidden>No documents match that word.</p>
<footer>Built from <code>designs/library.json</code>. Say <strong>/documents</strong> to Claude to refresh it. Every page is private until you share it from its Share menu.</footer>
</main>
<script>
(function(){{
  var q=document.getElementById('q'), none=document.getElementById('none');
  q.addEventListener('input',function(){{
    var t=q.value.trim().toLowerCase(), shown=0;
    document.querySelectorAll('.ientry').forEach(function(e){{
      // A page shows if its name, description or any section matches; while searching, a twisty opens when one of its sections matches.
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
