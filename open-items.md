# Open items

Everything still open, organized as the path we agreed to operationalize the
framework: read the core, make it runnable, run it once, then get ready for Andy.
Claude updates it at every wrap-up: finished items move to "Closed" with the date.

> **How to read this.** Work top to bottom: "Now" first, then the stages (stage 2 runs alongside stage 1).
> Items are numbered in priority order within each kind: V1 is the first thing
> to read, W1 the first piece of work, D1 the first decision. When priorities
> change, the numbers change with them, so the top of each list is always
> what's next. Closed items (C) keep their number. Say "close V1" or "what's W5?". The letter says what kind of item it is: **D** a decision,
> **V** something to read, **W** work, **B** a question for the bank (not the RM plan's workflows B1 to B9), **P** parked, **C** closed.
> **Who** says who moves it next. ⚠️ marks a guess.

## The path (agreed 2026-10-10)

1. **Read and lock the core** (me): the RM plan and the playbook.
2. **Make the machine runnable** (Claude): templates, task list design, approvals map, control gaps.
3. **Dry run and fix** (both): one made-up product through all six steps; fix what breaks.
4. **Get ready for Andy** (Claude builds, I decide): the RM mock-up, the Andy edition and my questions for him.

**First, high priority:** on October 19, check that the bank news scout's first notice reached my personal email (W1, under "Now" below). **Next up (agreed 2026-10-14):** map the RM and portfolio manager user workflows (W2). Stage 1 (V1, the RM plan) and stage 2 (W3 and W4) carry on alongside; none waits on another.

## At a glance

| Stage | Open | What it is |
|---|---|---|
| Now | 2 | What we're working on first |
| Stage 1. Read and lock the core | 8 | What I read, then the decision on the RM framework |
| Stage 2. Make the machine runnable | 4 | What Claude builds so a real run is possible |
| Stage 3. Dry run and fix | 3 | Running the machine once and fixing it |
| Stage 4. Get ready for Andy | 9 | What Andy sees, and what I ask him |
| Alongside the path | 11 | Useful any time; doesn't block a stage. Dated items first |
| Inside the bank | 21 | Questions only someone at the bank can answer |
| Parked on purpose | 4 | Not forgotten; waiting for a signal from me |

"Andy" here is my main contact at the bank. ⚠️ Claude assumes this is Andy Miner, the bank's senior director of AI for Corporate & Commercial Banking.

## Where we stand

**The goal right now:** build the machine for one product, end to end, and get
it running. Two or more products come after that. Checked on 2026-10-10 against
every working file (this section replaces the separate Gap Review page).

> **Later, not now: running many products at once.** We know we'll need it, but
> it isn't a priority until the machine runs one product well. It covers: one
> intake form for new product ideas, a scoring rule to rank them against each
> other, how many products I can run at once, my week and month across products,
> and when a live product is retired. Kept as parked item P4.

| Area | Rating | Where we are | Open items |
|---|---|---|---|
| The six-step process for one product | Strong on paper | Steps, gates, 44 sub-steps, first-time logs and the automation check at every gate. Not yet tried on real work | W7 |
| RM plan (the first worked example) | Strong draft, not reviewed | Memo v8, with agent specs and workflows. I've read only the summary's opening and plan table. Now organized on seven core use cases | V1, D1 to D3 |
| Governance and controls | Partial | 25 controls named. 13 have a stage the playbook doesn't cover yet, such as who proves that only approved AI models are used | W6 |
| Automating the process | Partial | Every task is marked Auto, Draft or Me, and 40 agents are fully specified: 33 general agents that run the product machine, the RM product's own 6, and my research helper H1 (the bank news scout). None of the 39 delivery agents is built or tested; H1 is set up and running. How much can run alone depends on whether the bank lets automations message people ⚠️ | B22, W7 |
| Ready-to-fill templates | Missing | The brief, data contract, risk intake, gate pack, evidence pack and monitoring plan are described, but none exists as a template yet. The Draft agents need these to fill in | W3 |
| Task list design | Missing | The reminders, status notes and progress view all read from one task list, but its fields aren't written down, and we don't know the bank's tool yet | W4, B23 |
| Approvals | Partial | Who decides is clear for every step. There's no map of who signs what, how long it takes, or who to go to when a sign-off is stuck | W5, B21 |
| Showing what an RM sees | Missing | The plan promises a working prototype in week 1, but there's nothing to show yet | W10 |
| A version written for Andy | Missing | The plan is written as my working plan, with internal labels, and doesn't say credit comes next | W11 |
| Knowing the RM's real day | Partial | The Bank Business Briefing is done and read. The user workflow maps will show how RMs and PMs work today (Job Notes dropped as not required, 2026-10-14) | W2 |
| After launch: support and incidents | Partial | Incident steps exist (who to call, how to pause). No support model or runbook yet. Needed before the first product goes live, not before Andy | W9 |

## Now

What we're working on first: a quick check on the bank news scout, then the user workflow maps, which feed both the RM and the credit work. Date to work toward: on Tuesday October 20, 2026 I talk with the credit lead and the RM lead, so I'm going down this log from the top before then (said 2026-10-14).

| # | Item | Who | Waits on |
|---|---|---|---|
| W1 | **High priority.** Check that the bank news scout's first weekly run (Monday October 19) reached my personal email, jeremydrane2021@gmail.com. The scout no longer uses Gmail or my work address: its summary arrives as the scheduled task's own notice (email and phone). If the notice goes somewhere else, tell Claude. Optionally, allow sec.gov, investor.associatedbank.com and associatedbank.com in the cloud environment's Network access settings, so the scout can open the bank's pages. **Also turn on automatic approval:** both scout tasks ("Bank news scout (weekly)" and "(after Q3 results)") are set to stop and wait whenever a step needs approval, and nobody is there to approve on a Monday morning, so the run could stall without sending anything. How (checked 2026-10-14, button names not confirmed): in the Claude desktop app, open the **Code** tab, click **Routines** in the left sidebar (or under **More**), click the task, click **Edit**, set the permission mode to automatic approval and save; then the other task. Claude can't turn this on itself. If the setting isn't there, skip it: Anthropic's help page says cloud tasks don't ask for approval, and a missing Monday notice would show a stalled run. | Me | Monday October 19, 2026 (first weekly run) |
| W2 | Map the RM and portfolio manager user workflows (agreed 2026-10-14, the next job; the RM map starts from Map 2 on the Workflow Maps, an RM's week with AI, which shows only the with-AI side): how each group works today, where each AI product fits, and how the work changes. **Start with the RM user workflow** (you asked for it on 2026-10-14; the next session begins here), then credit. Each gets a page in the Document Library, where a placeholder row waits. Show a sample of the page layout before building it. Use the new user-workflow routine (idea 41, built 2026-10-14) | Claude and me | Nothing |

## Stage 1. Read and lock the core

**Who:** Me. You read the plan and the manual the whole framework rests on, then decide whether the RM framework is ready (D5). Nothing in stage 2 needs to wait for this, but the dry run and Andy do.

| # | Item | Who | Waits on |
|---|---|---|---|
| V1 | Read the RM Analytics Plan (the long scrolling page): everything after the summary's opening and plan table: from "What lets us move this fast" on, then Parts 1 to 6. The RM Analytics Framework design page holds the same words | Me | Nothing |
| V2 | Read the RM Core Use Cases page: McKinsey's five frontline AI use cases and their returns, how the RM plan covers them, and the questions it raises | Me | Nothing |
| V3 | Read the Portfolio Manager Core Use Cases page: what banks are deploying in commercial credit, and the credit counterpart proposed for each of the seven core use cases | Me | Nothing |
| D1 | Add an AI product under core use case 5, AI sales coaching (personal guidance from call transcripts)? Low risk, and McKinsey reports new bankers ramping up 20% faster | Me | V2 |
| D2 | Move prospecting (winning new clients) earlier than wave 3? McKinsey reports its biggest revenue numbers there; outside prospect data may set the pace | Me | V2 |
| D3 | Keep autonomous lead nurturing and pricing out for now, because they conflict with "nothing reaches a client without the RM" and the fair-lending control? Claude recommends yes, revisit later with evidence | Me | V2 |
| D4 | Agree the credit order the Portfolio Manager Core Use Cases page proposes: credit memo and annual review drafts first, early warning second, risk ratings kept out of the first waves? | Me | V3 |
| D5 | Is the RM framework ready to copy to other use cases? My answer on 2026-10-09: not yet. The reading in stage 1 and the work in stages 2 and 3 come first | Me | Credit, the next use case, waits on this |

## Stage 2. Make the machine runnable

**Who:** Claude, then a quick review from me. Build what a real run needs and doesn't have yet: the templates every product fills in, the task list design, who approves what, and the control gaps.

| # | Item | Who | Waits on |
|---|---|---|---|
| W3 | Ready-to-fill templates: brief, data contract, risk intake, gate pack, decision log, evidence pack, monitoring plan, release-readiness checklist | Claude drafts, I review | My yes |
| W4 | Tracker design: the fields every task carries, written to work in any tool (bank question B23 is still open) | Claude drafts, I review | My yes |
| W5 | Approvals map for one product: who signs what at each gate, typical turnaround ⚠️, and who to go to when a sign-off is stuck | Claude drafts, I review | My yes |
| W6 | Close the gaps the Controls Catalog found in my playbook: 13 of the 25 controls have a stage marked "not covered in the playbook yet", such as who proves that only approved AI models are used. Each needs a line added to the right playbook step, or a decision that it isn't needed | Claude, with my yes for each playbook change | Nothing |

## Stage 3. Dry run and fix

**Who:** Claude and me. Take one small made-up product through all six steps with the templates and two or three agents built as Claude skills. Log where it breaks, fix the machine, then apply it to the RM plan.

| # | Item | Who | Waits on |
|---|---|---|---|
| W7 | Dry run of the machine: take one small made-up product through all six steps with the templates and two or three agents built as Claude skills, and log where it breaks | Claude and me | W3 and W4, and my read of the pages (V1) |
| W8 | Apply the product machine to the RM plan as the first worked example: mark every RM task Auto, Draft or Me | Claude, with me | V1 and W7 |
| W9 | Support model and incident runbook for one product: who users call, how issues are logged and fixed, and the steps to pause or roll back the product | Claude drafts, I review | W7 (the dry run shows what support is needed) |

## Stage 4. Get ready for Andy

**Who:** Claude builds, I decide when to share. Turn the plan into something Andy can see and react to, plus the questions I'd ask him.

| # | Item | Who | Waits on |
|---|---|---|---|
| W10 | Build an RM mock-up: clickable screens of the Monday opportunity list and the pre-meeting client brief, on made-up sample data, so Andy can see what an RM gets | Claude, with my review | Stage 1 |
| W11 | Build an "Andy edition" of the RM plan: two to three pages in his terms, no internal labels, with one line that credit comes next | Claude, then me | V1 and my yes |
| B1 | Which revenue lever matters most to the business right now? (from: RM plan, section 11) | Me, with Andy | Nothing |
| B2 | How will success be judged in the first 6 months? (from: RM plan, section 11) | Me, with Andy | Nothing |
| B3 | What are Andy's first use cases, and how does RM analytics rank against credit (portfolio management) and treasury and payments? (from: Bank Business Briefing, section 9) | Me, with Andy | Nothing |
| B4 | ⚠️ Is the new franchise banking team (the bank's national team for franchise owners, launched in April 2026), where RMs and portfolio managers sit together, the intended first team? This is my guess from our conversation (from: Chat, 2026-10-09) | Me, with Andy | Nothing |
| B5 | Does "Corporate & Commercial Banking" include commercial real estate and the specialty industries, and where does the role sit? (from: Bank Business Briefing, section 9) | Me, with Andy | Nothing |
| B6 | What team and budget are available for the pilot? (from: RM plan, section 11) | Me, with Andy | Nothing |
| B7 | Which RM teams would make a good pilot group? (from: RM plan, section 11) | Me, with Andy | Nothing |

## Alongside the path

Useful any time; none of these blocks a stage. Dated ones first.

| # | Item | Who | Waits on |
|---|---|---|---|
| W12 | First weekly review: what's working, what's annoying, what to change. Also re-check Anthropic's prompting guide for changes | Me, with Claude | About 2026-10-21 (not yet, said 2026-10-14) |
| W13 | Re-run the Bank Business Briefing after the bank's Q3 2026 results on October 22, 2026, using the saved prompt (Example 5 in the Prompting Guide). Read the full Q2 earnings call transcript at the same time; only a summary was available the first time. The bank news scout's scheduled run on October 23 does the re-run as a draft | Claude | October 22, 2026 |
| W14 | Check that a section link in the Document Library opens the page at that section. If it only opens the top, drop the section links or say so on the page | Me, then Claude | Nothing |
| W15 | Two loose ends from the McKinsey article: confirm its publication date (the pasted page showed none), and decide whether role redesign (new RM roles as agents take on work, McKinsey's fifth principle) belongs in the playbook; it isn't covered yet | Claude, then me | Nothing |
| W16 | Loose ends in the Bank Business Briefing: check the exact wording of the bank's AI announcement before quoting it; replace the 2016 description of who the segment serves once the annual report for the 2025 financial year can be opened in full; and confirm two of my guesses, the RM headcount read from an unclear chart and that Omaha came with American National | Claude | Nothing |
| W17 | Run the tests of Claude's rules that need a real session. Each test is a short scenario in `learning/tests.md` that checks one rule still works. Not yet run in a live session: T7, T10, T13, T14 and T17, and the second parts of T2, T3, T9 and T16. Never run at all: T18 to T22, T24 to T27 (including T27's new second part, from 2026-10-14) and T30 to T33. Re-run T8 (does Claude label every suggestion Needed or Optional?), which failed on 2026-10-09 before its rule was tightened, and T5, whose first run wasn't a fair test | Claude, in a new session | Nothing |
| W18 | Check the product details marked "(verify)" in the Tech Stack Guide: product names, prices, vendor terms and any update to the regulators' model-risk guidance. Eleven lines carry the mark. New lead (2026-10-13, Portfolio Manager Core Use Cases page): SR 26-2, issued 17 April 2026, reportedly replaces SR 11-7, which our files cite; sources disagree on whether it covers generative AI, so read the Fed's own text before changing anything | Claude | Nothing |
| W19 | Claude Mastery course: paste in the next page (Module 3: Projects, Connectors and Skills). Claude starts a course notes file when it arrives (idea 14, approved) | Me, then Claude | Nothing |
| W20 | Try the newer skills on real work: "prototype X", "write a prompt for X", "new use case: X" | Me | Nothing |
| W21 | Fewer approval pop-ups (idea 2, approved): tell Claude which pop-ups I still see and in which app, so it can pre-approve the safe, read-only ones. Claude won't change my permission settings on a guess | Me, then Claude | Nothing |
| W22 | Playbooks for my everyday tools (idea 3, approved): name two or three tasks I repeat in email, calendar or documents. Claude turns each into a step-by-step skill | Me, then Claude | Nothing |

## Inside the bank

The plans rest on these, but only someone at the bank can answer them. Ask once I start; many overlap.

| # | Item | Who | Waits on |
|---|---|---|---|
| B8 | How many RMs, treasury management officers and portfolio managers are there today, by market, including American National? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B9 | How are RMs measured, paid and rewarded, and how are referrals to treasury, capital markets and wealth credited? (from: RM plan, section 11; Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B10 | The value model's inputs: win rate, first-year revenue per win by product, and client-facing hours per RM today (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B11 | The segment's fee income by line today, including what sits inside the $47.6 million the bank doesn't break down (public figures stop at the 2025 financial year) (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B12 | The segment's deposits, and the share of borrowing clients who keep their main accounts with the bank (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B13 | What share of commercial clients use treasury management? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B14 | Does Finance accept costs saved and loan losses avoided as returns, as well as new revenue? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B15 | Who owns the client data in Snowflake and Salesforce, and which data lives where? (from: RM plan, section 11; playbook sub-step 2.3 (the data contract)) | The bank | Starting at the bank |
| B16 | How is each platform set up for RMs today: which features, licenses and connections? Which Salesforce products does the bank own? Every tool named in the product machine's task tables is a guess until this is known (from: RM plan, section 11; Tech Stack Guide; Product Machine) | The bank | Starting at the bank |
| B17 | Why does the bank have both Snowflake and Fabric, and which holds what? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B18 | Which AI models are approved, and where do they run? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B19 | Has the American National systems conversion happened, and are the acquired clients in Salesforce and Snowflake? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B20 | Who builds: my team, IT, or business staff using click-to-build tools such as Power Platform? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B21 | What does the AI governance process look like, and how long does a review usually take? (from: RM plan, section 11; Tech Stack Guide) | The bank | Starting at the bank |
| B22 | May automations message people or update trackers by themselves? This decides how much of the product machine can run on its own (from: Product Machine) | The bank | Starting at the bank |
| B23 | Which tracker tool does the bank use for projects? (from: Product Machine; agent library) | The bank | Starting at the bank |
| B24 | Twenty smaller permissions (twenty-one "To confirm" items, minus the tracker question in B23) the delivery agents depend on, such as whether meeting recaps are allowed, which test environments exist and how sign-offs must be recorded. Each is listed under "To confirm" in the agent library, and one overlaps B22 (from: `playbook/agents.md`) | The bank | Starting at the bank |
| B25 | Do RMs work mainly in Salesforce? This decides where the insights appear (from: RM plan, section 5) | The bank | Starting at the bank |
| B26 | The numbers still shown as [X] in the RM plan, the Product Workflow, the Product Framework and the Product Machine, such as payback months, weekly-use targets and how many projects I run at once, and the plan's week estimates. Each gets set with the bank's real figures (from: RM plan; Product Workflow; Product Framework; Product Machine) | The bank | Starting at the bank |
| B27 | The 46 guesses about the bank marked ⚠️ across the six playbook steps. Each gets replaced with a fact as I learn it. Many overlap B15 to B23 (from: Product Playbook) | The bank | Starting at the bank |
| B28 | The 20 bank terms listed at the end of the Glossary (such as "AI-sourced opportunity", "qualified opportunity" and "win rate"). Each is marked ⚠️ until the bank's own definition is recorded there, with its source. Many overlap B9 and B10 (from: Glossary) | The bank | Starting at the bank |

## Parked on purpose

| # | Item | Who | Waits on |
|---|---|---|---|
| P1 | The credit (portfolio management) plan. Started at my request on 2026-10-13 with the Portfolio Manager Core Use Cases page (the six parked credit processes plus two new ones, each lined up with a core use case); the portfolio manager user workflow map is part of W2. The plan itself still waits. Ready for then: franchise banking as a possible pilot, and whether to add "costs saved" and "loan losses avoided" to the value model | Me | Me saying the RM framework is ready (D5) |
| P2 | Sharing with Associated. When I'm ready, Claude builds an "Associated edition" of the Document Library (idea 33): only the pages meant for them, with no internal labels | Me | Me saying I'm ready to share |
| P3 | A treasury and payments use case. The bank named it as a starting point for AI, and nothing has been planned yet | Me | After credit, unless B3 changes the order |
| P4 | **Featured: running many products at once.** One intake form for new product ideas, a scoring rule to rank them against each other, how many products I can run at once, my week and month across products, and when a live product is retired | Me | The machine running one product well first |

## Closed

| # | Item | Closed |
|---|---|---|
| C1 | Build the Bank Business Briefing and save its prompt (merged into main as pull request #54) | 2026-10-09 |
| C2 | Decide the order of use cases: RM first, credit second | 2026-10-09 |
| C3 | Bring in the unmerged work from my other session. Merged into this log's pull request, with both sides kept where they overlapped | 2026-10-09 |
| C4 | Four ideas: yes. The shorthand check (idea 32) and the Steps and Controls catalogs (idea 34) are built. Fewer pop-ups (idea 2) and everyday playbooks (idea 3) need facts from me first: see the pop-ups and everyday-playbooks items | 2026-10-09 |
| C5 | Remove my safety rules (idea 16). The pop-up explanations and "Deny is safe" reminders are gone from the rule book, with the two pop-up rules and their tests | 2026-10-09 |
| C6 | Make the RM plan's 14 helper agents general: yes. They are now M20 to M33 in the agent library, used by every project; the RM plan shows how it uses each one | 2026-10-10 |
| C7 | Three new controls: yes. K23 (approved AI tools for the team's own work), K24 (consent before recording) and K25 (agents stop rather than guess) are in the Controls Catalog, set and built in the playbook (proving K23 and watching all three are still gaps, in the control-gaps item); the playbook's control check (4.5) now also confirms the build, test and live path and IT's approval of every connection | 2026-10-10 |
| C8 | The line saying credit comes next is now part of the Andy edition item | 2026-10-10 |
| C9 | Keeping the reference pages in line is now built into every audit (the alignment sweep and its automatic checks), and the Glossary was added as a fifth reference page | 2026-10-10 |
| C10 | Ideas 35 and 36: yes. The design canvas's runtime is kept in the repo so the render check always runs, and a check before every merge blocks it if the audit checker or render check finds a problem | 2026-10-10 |
| C11 | The McKinsey numbers in the RM plan are confirmed against the article's text (3–15% higher revenue per RM, 20–40% lower cost to serve, and RMs spending about 25–30% of their time with clients). The last one is now credited to McKinsey directly | 2026-10-10 |
| C12 | Organize the RM plan on seven core use cases: yes. Done: McKinsey's five frontline use cases plus two of our own (admin off the RM's plate, keep clients), with our AI products underneath each and a return profile for each (McKinsey benchmarks next to our own [X] targets) | 2026-10-10 |
| C13 | Idea 37 (check for old wording after a rename): yes. The audit checker now fails on any old wording left after a rename, from a new "Old wording we've retired" table in the glossary | 2026-10-10 |
| C14 | Call notes into Salesforce moved from wave 2 into wave 1, live with the insights about weeks 4–6, because McKinsey's banker survey ranks admin a top-two problem at every stage of the sales funnel | 2026-10-10 |
| C15 | Ideas 38 and 39: yes. Before editing a designed page, Claude now checks that the live page isn't newer than the repo copy (a step in the designed-doc skill), and every outside chart I share is saved with its numbers and source in the matching memo (rule R24) | 2026-10-10 |
| C16 | The old `prompt-email-example` branch is deleted. Everything on it was already in main | 2026-10-13 |
| C17 | Organize the Document Library around the two groups we serve: yes. It's one index in six sections (the bank, relationship managers, credit, how we deliver, reference, my workspace), with the two core use case pages renamed to match | 2026-10-14 |
| C18 | Number open items by priority: yes. Each kind runs 1, 2, 3 in priority order, numbers change when priorities change, and closed items keep theirs | 2026-10-14 |
| C19 | I read the Bank Business Briefing. It's fine as is, no changes | 2026-10-14 |
| C20 | Idea 43 (quieter startup warning): yes. The startup check now fetches more history before comparing an old branch and stays quiet when its changes are already in main; the two empty old branches that kept being flagged are gone from GitHub | 2026-10-14 |
| C21 | I read the Product Framework, Product Workflow, Product Machine and Product Playbook. All four are good to go and now marked In use | 2026-10-14 |
| C22 | Rename the credit pages to match the library's "Portfolio managers" section (idea 44): yes. They're now the Portfolio Manager Core Use Cases page, the portfolio manager user workflow and the portfolio manager plan | 2026-10-14 |
| C23 | Lock the Bank Business Briefing: audited; it now names both user groups, RMs and PMs, with a "which bankers" column, a section on PMs and a section on how the page stays current. The bank news scout is agent H1 in the Agent Library. "PM" now means portfolio manager everywhere, and "product manager" is spelled out | 2026-10-14 |
| C24 | Ideas 40 and 45: yes. The page check now clicks every jump link on every page and fails if one lands in the wrong place, and Claude checks the bank news scout's last run at the start of each session | 2026-10-14 |
| C25 | Reorganize the "How we deliver" pages so each has one job, read in order: Product Workflow (the steps), Product Framework (the rules), Product Machine (who does each task), Product Playbook (how to do each sub-step, with a short agent list linking to the Agent Library). Merged into main as pull request #80 | 2026-10-14 |
| C26 | Thinking through the job, Part 1 (the Job Notes page): not required, so it's off the Document Library and no longer an open item. The working file `job-notes.md` stays for reference | 2026-10-14 |
| C27 | Idea 46: yes. Every audit now runs a "nothing lost" check (`lost-lines.py`) that lists each sentence that disappeared from the working files, and each one must be put back or explained | 2026-10-14 |

_Last updated: 2026-10-14_
