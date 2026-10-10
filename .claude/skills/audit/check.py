"""Mechanical audit checks. Run from the repo root: python3 .claude/skills/audit/check.py
1. Framework task tables and playbook sub-steps match (every sub-step has rows, every
   review-table "Aim for" kind matches the framework, every sub-step has all 8 fields).
2. Designed-page sources in designs/ have no empty tables.
3. Every page built from a working copy is up to date.
2b. No built page shows a stray underscore left over from Markdown.
4. Every page in designs/README.md is in the Document Library (designs/library.json), and the other way round.
5. The Open Items log (open-items.md): no number used twice, counts match, pages and ideas still open are listed, not out of date.
6. NOW.md's "What's next" has no unexplained shorthand.
Prints each problem and a total. 0 problems means the mechanical checks pass."""
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
for page,builder in [('designs/delivery-machine.html','designs/delivery-machine-build.py'),('designs/playbook.html','designs/playbook-build.py'),('designs/product-framework.html','designs/md-page-build.py'),('designs/tech-stack.html','designs/md-page-build.py'),('designs/job-notes.html','designs/md-page-build.py'),('designs/job-description.html','designs/md-page-build.py'),('designs/prompting.html','designs/md-page-build.py'),('designs/bank-business.html','designs/md-page-build.py'),('designs/open-items.html','designs/md-page-build.py'),('designs/library.html','designs/library-build.py'),('designs/workflows.html','designs/workflows-build.py'),('designs/agents.html','designs/agents-build.py'),('designs/steps.html','designs/catalogs-build.py'),('designs/controls.html','designs/catalogs-build.py')]:
    before=open(page).read()
    subprocess.run(['python3',builder],check=True)
    if open(page).read()!=before: print(page,"was out of date: rebuilt it, republish it"); probs+=1
# 4. every published page is in the Document Library
import json
lib=json.load(open('designs/library.json'))
lib_urls={d['url'] for a in lib['areas'] for d in [a['parent']]+a['children']}|{b['url'] for b in lib.get('building_blocks',[])}
readme_urls=set(re.findall(r'https://claude\.ai/artifact/\w+',open('designs/README.md').read()))
library_url='https://claude.ai/artifact/LTpbCT4kN4LcyEoYnh7vgj'
for u in sorted(readme_urls-lib_urls-{library_url}): print("designs/library.json is missing",u); probs+=1
for u in sorted(lib_urls-readme_urls): print("designs/README.md is missing",u); probs+=1
# 5. the Open Items log is in step with the rest of the repo (open-items.md)
oi=open('open-items.md').read()
nums=re.findall(r'^\| ([A-Z]\d+) \|',oi,re.M)
for n in sorted({x for x in nums if nums.count(x)>1}): print("open-items.md uses the number",n,"twice"); probs+=1
for label,pre in [('1. Decisions waiting on me','D'),('2. Reviews waiting on me','V'),('3. Work to do','W'),('4. To confirm at the bank','B'),('5. Parked on purpose','P')]:
    m=re.search(r'^\| '+re.escape(label)+r' \| (\d+) \|',oi,re.M)
    rows=len([x for x in nums if x[0]==pre])
    if not m or int(m.group(1))!=rows: print("open-items.md 'At a glance' count for",label,"should be",rows); probs+=1
oi_open=oi.split('## 2. Reviews')[-1].split('## 6. Closed')[0]  # a page must be named in an open item, not just anywhere
for a in lib['areas']:
    for d in [a['parent']]+a['children']:
        if d['status'] in ('Waiting for review','Draft','In progress') and d['name'] not in oi_open: print("open-items.md doesn't mention the page",d['name'],"(status:",d['status']+")"); probs+=1
for b in lib.get('building_blocks',[]):
    if b['status'] in ('Waiting for review','Draft','In progress') and b['name'] not in oi_open: print("open-items.md doesn't mention the page",b['name']); probs+=1
for m in re.finditer(r'^\| (\d+) \|.*\| ([^|]+) \|\s*$',open('ideas.md').read(),re.M):
    if re.match(r'(new|suggested|yes|not yet)\b',m.group(2).strip()) and not re.search(r'\bideas? [\d, and]*\b'+m.group(1)+r'\b',oi): print("open-items.md doesn't mention idea",m.group(1),"(status:",m.group(2).strip()[:20]+")"); probs+=1
def upd(f):
    m=re.search(r'_Last updated: (\d{4}-\d{2}-\d{2})',open(f).read()); return m.group(1) if m else ''
if upd('open-items.md')<upd('NOW.md'): print("open-items.md was last updated",upd('open-items.md'),"but NOW.md on",upd('NOW.md')+": review the open items"); probs+=1
# 6. shorthand in NOW.md's "What's next" (idea 32, from L10d): every item must explain itself.
# A code (a rule, test, lesson, idea or item number) is fine only inside brackets that also hold four or more other words.
now_parts=open('NOW.md').read().split("## What's next")
if len(now_parts)<2: print("NOW.md has no \"What's next\" heading to check"); probs+=1
else:
    CODE=r'\b(?:[RTLDWVBPCKMA]\d+[a-d]?|[Ii]deas? \d+)\b'
    for item in re.findall(r'^\d+\. .+$',now_parts[1].split("\n## ")[0],re.M):
        def keep(m):
            inner=re.sub(CODE,'',m.group(0)); return '' if len(re.findall(r"[A-Za-z']{2,}",inner))>=4 else m.group(0)
        bare=re.sub(r'\([^)]*\)',keep,re.sub(r'`[^`]*`','',item))
        codes=re.findall(CODE,bare)
        if codes: print("NOW.md What's next uses",", ".join(codes),"without explaining it:",item[:60]); probs+=1
        if len(item.split())<9: print("NOW.md What's next item is too short to explain itself:",item[:60]); probs+=1
print("problems:",probs)
