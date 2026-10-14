"""Mechanical audit checks. Run from the repo root: python3 .claude/skills/audit/check.py
1. Framework task tables and playbook sub-steps match (every sub-step has rows, every
   review-table "Aim for" kind matches the framework, every sub-step has all 8 fields).
2. Designed-page sources in designs/ have no empty tables.
3. Every page built from a working copy is up to date.
2b. No built page shows a stray underscore left over from Markdown.
4. Every page in designs/README.md is in the Document Library (designs/library.json), and the other way round.
5. The Open Items log (open-items.md): no number used twice, counts match, pages and ideas still open are listed, not out of date.
6. NOW.md's "What's next" has no unexplained shorthand.
7. Alignment across documents (from L18): counts of agents, sub-steps, controls and workflow branches
   quoted anywhere match the sources; the framework's "What happens" lists have one item per playbook
   sub-step; the Six-Step Workflow memo and page carry the framework's gate wording.
8. The glossary: no word from its "Words we don't use" table appears in the core documents.
9. Retired wording: nothing from the glossary's "Old wording we've retired" table is left anywhere people read (idea 37).
Prints each problem and a total. 0 problems means the mechanical checks pass.
5b. Every V/D/W/P item number cited in the working files is a live open item in open-items.md
    (it can't tell whether a reference points to the RIGHT item: after a renumbering, re-read each one).
"""
import subprocess
import re,glob
fw=open('product-framework.md').read()
fwk={}
for m in re.finditer(r'^\| (\d\.\d) \| [^|]+ \| ([^|]+) \|',fw,re.M):
    fwk.setdefault(m.group(1),set()).add(m.group(2).strip().split()[0].lower())
probs=0
fields=["**Goal:**","**Why it matters:**","**Know first:**","**First time, step by step:**","**Output:**","**Done when:**","**Automation watch:**","**For RM analytics:**"]
for f in sorted(glob.glob('playbook/[1-6]-*.md')):
    s=open(f).read()
    subs=re.findall(r'^## (\d\.\d) ',s,re.M)
    for n in subs:
        if n not in fwk: print(f,n,"no framework row"); probs+=1
        body=s.split(f"## {n} ")[1].split("\n## ")[0]
        for fl in fields:
            if fl not in body: print(f,n,"missing field",fl); probs+=1
    rev=s[s.index("| Sub-step | Agent |"):]
    covered=set()
    for m in re.finditer(r'^\| ([\d., ]+) \| [^|]+ \| (\w+)[^|]* \| ([^|]+) \|',rev,re.M):
        aim=m.group(3).strip().split()[0].lower()
        for n in [x.strip() for x in m.group(1).split(",")]:
            covered.add(n)
            if aim not in fwk.get(n,set()): print(f,n,"aim",aim,"not in framework kinds",fwk.get(n)); probs+=1
    for n in subs:
        if n not in covered: print(f,n,"not in review table"); probs+=1
for n in fwk:
    if not any(re.search(rf'^## {re.escape(n)} ',open(f).read(),re.M) for f in glob.glob('playbook/[1-6]-*.md')): print("framework",n,"no playbook sub-step"); probs+=1
# 2. empty tables in designed pages
for f in glob.glob('designs/*.html'):
    for body in re.findall(r'<tbody>([\s\S]*?)</tbody>',open(f).read()):
        if not re.sub(r'<[^>]+>','',body).strip(): print(f,"has an empty table"); probs+=1
# 2b. stray Markdown marks left showing on a built page (from L7d)
for f in glob.glob('designs/*.html'):
    for m in re.findall(r'<(?:p|li|td|dd|dt|span|div|h\d)[^>]*>_[^<]{0,40}|[^<]{0,40}_</(?:p|li|td|dd|dt|span|div|h\d)>',open(f).read()):
        print(f,"shows a stray underscore:",m); probs+=1
# 3. pages built from working copies are up to date
for page,builder in [('designs/delivery-machine.html','designs/delivery-machine-build.py'),('designs/playbook.html','designs/playbook-build.py'),('designs/product-framework.html','designs/md-page-build.py'),('designs/tech-stack.html','designs/md-page-build.py'),('designs/job-notes.html','designs/md-page-build.py'),('designs/job-description.html','designs/md-page-build.py'),('designs/prompting.html','designs/md-page-build.py'),('designs/bank-business.html','designs/md-page-build.py'),('designs/open-items.html','designs/md-page-build.py'),('designs/library.html','designs/library-build.py'),('designs/workflows.html','designs/workflows-build.py'),('designs/agents.html','designs/agents-build.py'),('designs/steps.html','designs/catalogs-build.py'),('designs/controls.html','designs/catalogs-build.py'),('designs/glossary.html','designs/md-page-build.py'),('designs/mckinsey-use-cases.html','designs/md-page-build.py'),('designs/credit-market-scan.html','designs/md-page-build.py')]:
    before=open(page).read()
    subprocess.run(['python3',builder],check=True)
    if open(page).read()!=before: print(page,"was out of date: rebuilt it, republish it"); probs+=1
# 4. every published page is in the Document Library
import json
lib=json.load(open('designs/library.json'))
lib_docs=[d for g in lib['groups'] for d in g['items'] if not d.get('todo')]  # every page in the library, placeholders left out
lib_urls={d['url'] for d in lib_docs}
readme_urls=set(re.findall(r'https://claude\.ai/artifact/\w+',open('designs/README.md').read()))
library_url='https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj'
for u in sorted(readme_urls-lib_urls-{library_url}): print("designs/library.json is missing",u); probs+=1
for u in sorted(lib_urls-readme_urls): print("designs/README.md is missing",u); probs+=1
# 5. the Open Items log is in step with the rest of the repo (open-items.md)
oi=open('open-items.md').read()
nums=re.findall(r'^\| ([A-Z]\d+) \|',oi,re.M)
for n in sorted({x for x in nums if nums.count(x)>1}): print("open-items.md uses the number",n,"twice"); probs+=1
# items are numbered in priority order (L22): within each kind (V, D, W, B, P) the numbers run 1, 2, 3... down the page, with no gaps
for k in 'VDWBP':
    seq=[int(x[1:]) for x in nums if x[0]==k]
    if seq!=list(range(1,len(seq)+1)): print("open-items.md: the",k,"items aren't numbered 1, 2, 3... in order down the page:",' '.join(k+str(n) for n in seq)); probs+=1
# numbers change with priorities, so every item number cited elsewhere must still be a live item (L22)
live=set(nums)
# it only checks that a cited number exists; after a renumbering, re-read each reference to confirm it names the right item
for f in ['NOW.md','ideas.md','product-framework.md','glossary.md','tech-stack.md','open-items.md']+sorted(glob.glob('memos/*.md'))+sorted(glob.glob('playbook/*.md'))+sorted(glob.glob('learning/*.md'))+sorted(glob.glob('.claude/skills/*/SKILL.md'))+sorted(glob.glob('designs/rm-analytics-canvas/*.dc.html')):
    t=open(f).read()
    if f=='open-items.md': t='\n'.join(re.sub(r'^\| [A-Z]\d+ \|','|',l) for l in t.split('\n'))
    for m in re.finditer(r'\b([VDWP]\d{1,2})\b(?! Labs)',t):
        if m.group(1) not in live: print(f,"cites",m.group(1),"but the Open Items log has no such open item: update the reference"); probs+=1
# the log is organized by stage (agreed 2026-10-10): each "At a glance" count must match the rows in its section
secs=re.split(r'^## ',oi,flags=re.M)
for m in re.finditer(r'^\| ((?:Stage \d\. )?[A-Z][^|]+?) \| (\d+) \| [^|]+ \|$',oi.split('## At a glance')[1].split('\n## ')[0] if '## At a glance' in oi else '',re.M):
    sec=[x for x in secs if x.startswith(m.group(1).strip()+'\n')]
    rows=len(re.findall(r'^\| [A-Z]\d+ \|',sec[0],re.M)) if sec else -1
    if rows!=int(m.group(2)): print("open-items.md 'At a glance' count for",m.group(1).strip(),"should be",rows if rows>=0 else '(no such section)'); probs+=1
if '## At a glance' not in oi or '## Stage 1.' not in oi or '## Closed' not in oi: print("open-items.md is missing one of its section headings (At a glance, Stage 1, Closed)"); probs+=1
oi_live=oi.split('## Closed')[0]                                   # everything still open
oi_rev=oi_work=oi_live
where=lambda st: oi_live
for d in lib_docs:
    if d['status'] in ('Waiting for review','Draft','In progress') and d['name'] not in where(d['status']): print("open-items.md doesn't mention the page",d['name'],"(status:",d['status']+")"); probs+=1
for m in re.finditer(r'^\| (\d+) \|.*\| ([^|]+) \|\s*$',open('ideas.md').read(),re.M):
    if re.match(r'(new|suggested|yes|not yet)\b',m.group(2).strip()) and not re.search(r'\bideas? [\d, and]*\b'+m.group(1)+r'\b',oi_live): print("open-items.md doesn't mention idea",m.group(1),"(status:",m.group(2).strip()[:20]+")"); probs+=1
def upd(f):
    m=re.search(r'_Last updated: (\d{4}-\d{2}-\d{2})',open(f).read()); return m.group(1) if m else ''
if upd('open-items.md')<upd('NOW.md'): print("open-items.md was last updated",upd('open-items.md'),"but NOW.md on",upd('NOW.md')+": review the open items"); probs+=1
# 6. shorthand in NOW.md's "What's next" (idea 32, from L10d): every item must explain itself.
# A code (a rule, test, lesson, idea or item number) is fine only inside brackets that also hold four or more other words.
now_parts=open('NOW.md').read().split("## What's next")
if len(now_parts)<2: print("NOW.md has no \"What's next\" heading to check"); probs+=1
else:
    CODE=r'\b(?:[RTLDWVBPCKA]\d{1,2}[a-d]?|M\d{1,2}|[Ii]deas? \d+)\b'
    for item in re.findall(r'^\d+\. .+$',now_parts[1].split("\n## ")[0],re.M):
        def keep(m):
            inner=re.sub(CODE,'',m.group(0)); return '' if len(re.findall(r"[A-Za-z']{2,}",inner))>=4 else m.group(0)
        bare=re.sub(r'\([^)]*\)',keep,re.sub(r'`[^`]*`','',item))
        codes=re.findall(CODE,bare)
        if codes: print("NOW.md What's next uses",", ".join(codes),"without explaining it:",item[:60]); probs+=1
        if len(item.split())<9: print("NOW.md What's next item is too short to explain itself:",item[:60]); probs+=1
# 7. alignment across documents (from L18: the library said "19-agent library" while the Agent Library showed 39)
import json as _json, html as _html
n_sub={}
for f in sorted(glob.glob('playbook/[1-6]-*.md')):
    for n in re.findall(r'^## (\d)\.\d ',open(f).read(),re.M): n_sub[n]=n_sub.get(n,0)+1
SUB=sum(n_sub.values())
ctl=open('playbook/controls.md').read()
CTL=len(re.findall(r'^### K\d+\. ',ctl,re.M))
UNCOV=sum(1 for b in re.split(r'^### K\d+\. ',ctl,flags=re.M)[1:] if 'not covered' in b)
MS=[int(x) for x in re.findall(r'^### M(\d+)\. ',open('playbook/agents.md').read(),re.M)]
M=len(MS); MACH=sum(1 for x in MS if x<20)
H=len(re.findall(r'^### H\d+\. ',open('playbook/agents.md').read(),re.M))  # my research helpers
memo=open('memos/rm-analytics-framework.md').read()
appa=memo.split('## Appendix A')[1].split('## Appendix B')[0]
A=len(set(re.findall(r'\bA(\d+)\. ',appa)))
TEAM=M-MACH; PROD=A  # team agents (M20+) live in the agent library; Appendix A holds only the product's agents
B=len(re.findall(r'^\*\*B\d+\. ',memo.split('## Appendix B')[1],re.M))
lib=_json.load(open('designs/library.json'))
want={'agents':f'{M+A+H} agents','steps':f'{SUB} sub-steps','controls':f'{CTL} controls','workflows':f'2 maps · {SUB+B} branches'}
for b in lib_docs:
    if b['id'] in want and b['count']!=want[b['id']]: print('designs/library.json count for',b['name'],'is',repr(b['count']),'but the sources give',repr(want[b['id']])); probs+=1
# Each count is read with up to one word in front of the noun ("25 governance controls"). A total is
# checked against its own number: "all 39 agents" must be every agent, "19 ... machine" agents the machine's.
for f in ['NOW.md','open-items.md','product-framework.md','playbook/README.md','designs/library.json','memos/role-workflow.md','tech-stack.md']:
    t=open(f).read()
    for m in re.finditer(r'\b(\d+)[ -](?:([A-Za-z]+) )?(agents?|sub-steps|controls)\b',t):
        num,mid,noun=int(m.group(1)),(m.group(2) or '').lower(),m.group(3)
        before=t[max(0,m.start()-6):m.start()].lower(); after=t[m.end():m.end()+40].lower()
        if noun.startswith('agent'):
            if before.endswith('all '): ok={M+A+H}
            elif 'machine' in mid+after: ok={M,MACH}
            elif 'project' in mid+after or 'rm' in mid or 'product' in mid: ok={A,PROD}
            else: ok={M,A,M+A,M+A+H,MACH,TEAM,PROD}
        elif noun=='sub-steps': ok={SUB}
        else: ok={CTL} | ({UNCOV} if after.startswith(' of the') or 'have a stage' in after or 'not covered' in after else set())
        if num not in ok: print(f,'says',repr(m.group(0)),'but the sources give',sorted(ok)); probs+=1
    if re.search(r'\b\d+-agent library',t): print(f,'says "N-agent library": say which agents (general, project or all)'); probs+=1
items={m.group(1):m.group(2).split(' · ') for m in re.finditer(r'^- \*\*(\d)\. [^:]+:\*\* (.+)$',fw,re.M)}
for n,c in n_sub.items():
    if len(items.get(n,[]))!=c: print('product-framework.md "What happens" step',n,'has',len(items.get(n,[])),'items but the playbook has',c,'sub-steps'); probs+=1
gates={m.group(1):m.group(2).strip() for m in re.finditer(r'^\| \*\*(\d)\. [^*]+\*\* \|[^|]+\|[^|]+\| ([^|]+) \|$',fw,re.M)}
if len(gates)!=6: print('product-framework.md: could not read the six gates, so the gate checks did not run'); probs+=1
rw=open('memos/role-workflow.md').read()
for m in re.finditer(r'^\| (\d)\. [^|]+\|[^|]+\|[^|]+\| ([^|]+) \|$',rw,re.M):
    if m.group(2).strip()!=gates.get(m.group(1)): print('memos/role-workflow.md gate',m.group(1),'differs from product-framework.md'); probs+=1
rh=_html.unescape(open('designs/role-workflow.html').read())
for n,g in gates.items():
    if f'<b>Gate {n}</b><span>{g[0].upper()+g[1:]}</span>' not in rh: print('designs/role-workflow.html gate',n,'differs from product-framework.md'); probs+=1
# 8. the glossary (glossary.md): no "Don't say" word (or its plural) in the core documents, and the library's term count is right
gl=open('glossary.md').read()
GT=len(re.findall(r'^\| \*\*[^*]+\*\* \|',gl,re.M))
gb=[d for g in lib['groups'] for d in g['items'] if d.get('id')=='glossary']
if not gb: print('designs/library.json has no Glossary entry'); probs+=1
for b in gb:
    if b['count']!=f'{GT} terms': print('designs/library.json count for Glossary is',repr(b['count']),'but glossary.md has',GT,'terms'); probs+=1
bad=[]
if "## Words we don't use" not in gl: print('glossary.md has no "Words we don\'t use" heading, so the word check did not run'); probs+=1
else:
    dont=gl.split("## Words we don't use")[1].split('\n## ')[0]
    for row in [l for l in dont.split('\n') if l.startswith('|') and not re.match(r'^\|\s*-',l) and "Don't say" not in l]:
        m=re.match(r'^\| ([^|*]+?) \| [^|]+ \| [^|]+ \|$',row)
        if m: bad.append(m.group(1).strip())
        else: print('glossary.md: could not read this "Words we don\'t use" row:',row[:60]); probs+=1
    if not bad: print('glossary.md: the "Words we don\'t use" table is empty'); probs+=1
core=['product-framework.md','open-items.md','tech-stack.md','memos/rm-analytics-framework.md','memos/rm-analytics-summary.md','memos/role-workflow.md']+sorted(glob.glob('playbook/*.md'))
for f in core:
    for i,line in enumerate(open(f).read().split('\n'),1):
        for w in bad:
            if re.search(r'\b'+re.escape(w)+r'(s|es)?\b',line,re.I): print(f+':'+str(i),'uses',repr(w),'(see the glossary\'s "Words we don\'t use")'); probs+=1
# 9. retired wording (idea 37): nothing from the glossary's "Old wording we've retired" table is left behind.
# Each file is read as plain text (tags removed, entities decoded, spaces collapsed), so a phrase split by a tag,
# a line break or a non-breaking space is still found. A match is allowed only when the new wording sits within
# 150 characters of it (a note about the change), so one long line can't hide a leftover.
import html as _html
def _plain(t,is_html):
    if is_html: t=re.sub(r'<[^>]+>',' ',t)
    return re.sub(r'\s+',' ',_html.unescape(t).replace('\xa0',' '))
if "## Old wording we've retired" not in gl: print('glossary.md has no "Old wording we\'ve retired" heading, so the retired-wording check did not run'); probs+=1
else:
    ret=[]
    for row in gl.split("## Old wording we've retired")[1].split('\n## ')[0].split('\n'):
        if not row.startswith('|') or re.match(r'^\|\s*-',row) or row.startswith('| Retired wording'): continue
        m=re.match(r'^\| ([^|]+?) \| ([^|]+?) \| \d{4}-\d\d-\d\d \|\s*$',row)
        if m: ret.append((m.group(1).strip(),m.group(2).strip()))
        else: print('glossary.md: could not read this "Old wording we\'ve retired" row:',row[:60]); probs+=1
    if not ret: print('glossary.md: the "Old wording we\'ve retired" table is empty'); probs+=1
    where=sorted(set(core+glob.glob('memos/*.md')+['NOW.md','glossary.md','prompting.md','job-notes.md','job-description.md','designs/library.json','designs/README.md','designs/role-workflow.html','designs/rm-analytics-plan.html']+glob.glob('designs/*-build.py')+glob.glob('designs/rm-analytics-canvas/*.dc.html')))
    for f in where:
        txt=open(f).read()
        if f=='glossary.md': txt=txt.split("## Old wording we've retired")[0]
        plain=_plain(txt,f.endswith('.html') or f.endswith('.py'))
        low=plain.lower()
        for old,new in ret:
            nw=new.split(' (')[0].lower() if not new.startswith('(') else new.lower()
            for m in re.finditer(r'(?<!\w)'+re.escape(old.lower())+r'(?!\w)',low):
                if nw in low[max(0,m.start()-150):m.start()]+low[m.end():m.end()+150]: continue  # the new wording must sit outside the match itself
                print(f,'still says',repr(old),'(retired; use',repr(new)+'), near:',repr(plain[max(0,m.start()-40):m.end()+40])); probs+=1
# 10. the two user groups are always written RM, RMs, PM, PMs (said 2026-10-14): no "Rms", "rms" and so on (an apostrophe for ownership, "the RM's", is fine, and so are all-capital labels such as "FOR RMS")
for f in sorted(set(core+glob.glob('memos/*.md')+['NOW.md','glossary.md','open-items.md','designs/library.json','designs/rm-analytics-plan.html']+glob.glob('designs/*-build.py')+glob.glob('designs/rm-analytics-canvas/*.dc.html'))):
    for m in re.finditer(r"(?<![\w/.#-])(Rms|rms|Pms|pms|R\.M\.s?|P\.M\.s?)(?![\w])",open(f).read()):
        print(f,'writes',repr(m.group(1)),'- write RMs or PMs'); probs+=1
print("problems:",probs)
