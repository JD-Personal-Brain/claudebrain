"""Mechanical audit checks. Run from the repo root: python3 .claude/skills/audit/check.py
1. Framework task tables and playbook sub-steps match (every sub-step has rows, every
   review-table "Aim for" kind matches the framework, every sub-step has all 8 fields).
2. Designed-page sources in designs/ have no empty tables.
3. The delivery machine and playbook pages are up to date with their working copies.
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
# 3. pages built from working copies are up to date
for page,builder in [('designs/delivery-machine.html','designs/delivery-machine-build.py'),('designs/playbook.html','designs/playbook-build.py')]:
    before=open(page).read()
    subprocess.run(['python3',builder],check=True)
    if open(page).read()!=before: print(page,"was out of date: rebuilt it, republish it"); probs+=1
print("problems:",probs)
