# Open items

Everything still open, organized as the path we agreed to operationalize the
framework: read the core, make it runnable, run it once, then get ready for Andy.
Claude updates it at every wrap-up: finished items move to "Closed" with the date.

> **How to read this.** Work top to bottom: "Now" first, then the stages (stage 2 runs alongside stage 1).
> Items are numbered in priority order within each kind: V1 is the first thing
> to read, W1 the first piece of work, D1 the first decision. When priorities
> change, the numbers change with them, so the top of each list is always
> what's next. Closed items (C) keep their number. Say "close V1" or "what's W6?". The letter says what kind of item it is: **D** a decision,
> **V** something to read, **W** work, **B** a question for the bank (not the RM plan's workflows B1 to B9), **P** parked, **C** closed.
> **Who** says who moves it next. ⚠️ marks a guess.

## The path (agreed 2026-10-10)

1. **Read and lock the core** (me): the three RM pages (V1); the Use Case Library is read and in use (C51).
2. **Make the machine runnable** (Claude): templates, tracker design, approvals map, control gaps.
3. **Dry run and fix** (both): one made-up product through all six steps; fix what breaks.
4. **Get ready for Andy** (Claude builds, I decide): the RM mock-up, the Andy edition and my questions for him.

**First, high priority:** on October 19, check that the bank news scout's first notice reached my personal email (W1, under "Now" below). **Then, stage 2 of the use case kit for RMs, in the agreed order (C44):** the RM user workflow (W2), then the per-AI-product work (W3). Stages 1 and 2 of the path (V1; W4 and W5) carry on alongside; none waits on another.

## At a glance

| Stage | Open | What it is |
|---|---|---|
| Now | 3 | What we're working on first |
| Stage 1. Read and lock the core | 2 | What I read, then the decision on the RM framework |
| Stage 2. Make the machine runnable | 4 | What Claude builds so a real run is possible |
| Stage 3. Dry run and fix | 3 | Running the machine once and fixing it |
| Stage 4. Get ready for Andy | 8 | What Andy sees, and what I ask him |
| Alongside the path | 10 | Useful any time; doesn't block a stage. Dated items first |
| Inside the bank | 21 | Questions only someone at the bank can answer |
| Parked on purpose | 5 | Not forgotten; waiting for a signal from me |

"Andy" here is my main contact at the bank. ⚠️ Claude assumes this is Andy Miner, the bank's senior director of AI for Corporate & Commercial Banking.

## Where we stand

**The goal right now:** build the machine for one product, end to end, and get
it running. Two or more products come after that. First checked on 2026-10-10 against
every working file and kept current at each wrap-up, last on 2026-10-18 (this section replaces the separate Gap Review page).

> **Later, not now: running many products at once.** We know we'll need it, but
> it isn't a priority until the machine runs one product well. It covers: one
> intake form for new product ideas, a scoring rule to rank them against each
> other, how many products I can run at once, my week and month across products,
> and when a live product is retired. Kept as parked item P4.

| Area | Rating | Where we are | Open items |
|---|---|---|---|
| The six-step process for one product | Strong on paper | Steps, gates, 44 sub-steps, first-time logs and the automation check at every gate. Not yet tried on real work | W8 |
| RM plan (the first worked example) | Strong draft, not reviewed | Since 2026-10-18 (C50) I read three short pages: the RM Executive Summary, RM Assistant and the RM Assistant Plan (`memos/rm-plan.md`). The full memo v10, with agent specs (A1 to A5) and workflows (B1 to B9), is read in RM Detail. Not yet read since the reorganization | V1 |
| Governance and controls | Partial | 25 controls named. 12 have a stage the playbook doesn't cover yet, such as who proves that only approved AI models are used | W7 |
| Automating the process | Partial | Every task is marked Auto, Draft or Me, and 39 agents are fully specified: 33 general agents that run the product machine, the RM product's own 5, and my research helper H1 (the bank news scout). None of the 33 general agents or the 5 product agents is built or tested; H1 is set up and running. How much can run alone depends on whether the bank lets automations message people ⚠️ | B22, W8 |
| Ready-to-fill templates | Missing | The brief, data contract, risk intake, gate pack, evidence pack and monitoring plan are described, but none exists as a template yet. The Draft agents need these to fill in | W4 |
| Tracker design | Missing | The reminders, status notes and progress view all read from one task list, but its fields aren't written down, and we don't know the bank's tool yet | W5, B23 |
| Approvals | Partial | Who decides is clear for every step. There's no map of who signs what, how long it takes, or who to go to when a sign-off is stuck | W6, B21 |
| Showing what an RM sees | Missing | The plan promises a working prototype in week 1, but there's nothing to show yet | W11 |
| A version written for Andy | Drafted | The RM Executive Summary (2026-10-18) is the RM Leader Brief (C43): one page, waiting for my read | V1 |
| Use case kit (RMs) | Partial | The kit is agreed (C40) and cut on 2026-10-18 to three short pages for people plus one detail document for AI (C50); all three RM pages exist. The RM work now centers on one product, The RM Assistant, a working hypothesis (C46) | W2, W3 |
| Knowing the RM's real day | Partial | The Bank Business Briefing is done and read. The user workflow maps will show how RMs and PMs work today (Job Notes dropped as not required, 2026-10-14) | W2 |
| After launch: support and incidents | Partial | Incident steps exist (who to call, how to pause). No support model or runbook yet. Needed before the first product goes live, not before Andy | W10 |

## Now

What we're working on first: a quick check on the bank news scout, then stage 2 of the use case kit for RMs in the agreed order (C44): the RM user workflow, then the per-AI-product work. Date to work toward: on Tuesday October 20, 2026 I talk with the credit lead and the RM lead, so I'm going down this log from the top before then (said 2026-10-14).

| # | Item | Who | Waits on |
|---|---|---|---|
| W1 | **High priority.** Check that the bank news scout's first weekly run (Monday October 19) reached my personal email, jeremydrane2021@gmail.com. The scout no longer uses Gmail or my work address: its summary arrives as the scheduled task's own notice (email and phone). If the notice goes somewhere else, tell Claude. Optionally, allow sec.gov, investor.associatedbank.com and associatedbank.com in the cloud environment's Network access settings, so the scout can open the bank's pages. **Also turn on automatic approval:** both scout tasks ("Bank news scout (weekly)" and "(after Q3 results)") are set to stop and wait whenever a step needs approval, and nobody is there to approve on a Monday morning, so the run could stall without sending anything. How (checked 2026-10-14, button names not confirmed): in the Claude desktop app, open the **Code** tab, click **Routines** in the left sidebar (or under **More**), click the task, click **Edit**, set the permission mode to automatic approval and save; then the other task. Claude can't turn this on itself. If the setting isn't there, skip it: Anthropic's help page says cloud tasks don't ask for approval, and a missing Monday notice would show a stalled run. | Me | Monday October 19, 2026 (first weekly run) |
| W2 | Map the RM user workflow (step 2 of the use case kit's agreed order, C44; first agreed 2026-10-14). How RMs work today can only come from the bank, so this is a draft of assumptions with questions to confirm, tested with the RM lead on October 20 and in Discover (said 2026-10-17): how RMs work today, where each AI product fits, and how the work changes. It starts from Map 2 on the Workflow Maps (an RM's week with AI, which shows only the with-AI side). Show a sample of the page layout first, then build it with the user-workflow routine (idea 41, built 2026-10-14) as a page; where it sits in the Document Library is decided when it's built, since the RM section now holds only three pages for people plus RM Detail (C50). The portfolio manager map follows once I say we're moving into PM | Claude and me | Nothing |
| W3 | **Stage 2 of the use case kit for RMs, step 4** (the agreed order, C44). Step 3, the RM Leader Brief (the Andy edition, C43), is built as the RM Executive Summary (2026-10-18, C50). Step 4: one block per AI product, exact measures and controls for each AI product, and the AI sales coaching product's agent spec and workflow, written in the full plan (`memos/rm-analytics-framework.md`), which feeds RM Detail | Claude, then me | W2 (the agreed order, C44); my read of V1 comes before anything is shared |

## Stage 1. Read and lock the core

**Who:** Me. You read the RM plan and the two core use case pages, then decide whether the RM framework is ready (D1). Nothing in stage 2 needs to wait for this, but the dry run and Andy do.

| # | Item | Who | Waits on |
|---|---|---|---|
| V1 | Read the three RM pages, now short and in reading order (reorganized 2026-10-18, C50): the RM Executive Summary, RM Assistant and the RM Assistant Plan. The full detail is in RM Detail, the fourth RM row, which is for AI to read, not me | Me | Nothing |
| D1 | Is the RM framework ready to copy to other use cases? My answer on 2026-10-09: not yet. The reading in stage 1 and the work in stages 2 and 3 come first | Me | Credit, the next use case, waits on this |

## Stage 2. Make the machine runnable

**Who:** Claude, then a quick review from me. Build what a real run needs and doesn't have yet: the templates every product fills in, the tracker design, who approves what, and the control gaps.

| # | Item | Who | Waits on |
|---|---|---|---|
| W4 | Ready-to-fill templates: brief, data contract, risk intake, gate pack, decision log, evidence pack, monitoring plan, release-readiness checklist | Claude drafts, I review | My yes |
| W5 | Tracker design: the fields every task carries, written to work in any tool (bank question B23 is still open). Each project's tracker opens with its limiting factor and owner, and records each sub-step's start and finish dates and hours, so the wait index and the machine's measures come straight from it (Elon mode, agreed 2026-10-15) | Claude drafts, I review | My yes |
| W6 | Approvals map for one product: who signs what at each gate, typical turnaround ⚠️, and who to go to when a sign-off is stuck | Claude drafts, I review | My yes |
| W7 | Close the gaps the Controls Catalog found in my playbook: 12 of the 25 controls have a stage marked "not covered in the playbook yet", such as who proves that only approved AI models are used. Each needs a line added to the right playbook step, or a decision that it isn't needed | Claude, with my yes for each playbook change | Nothing |

## Stage 3. Dry run and fix

**Who:** Claude and me. Take one small made-up product through all six steps with the templates and two or three agents built as Claude skills. Log where it breaks, fix the machine, then apply it to the RM plan.

| # | Item | Who | Waits on |
|---|---|---|---|
| W8 | Dry run of the machine: take one small made-up product through all six steps with the templates and two or three agents built as Claude skills, and log where it breaks. Include a **deletion pass** (Elon mode, agreed 2026-10-15): mark every sub-step, agent and control "did it change a decision or catch a problem?" and delete what didn't, until about 1 in 10 has to come back. Law and bank-policy items are never cut. Record each sub-step's wait index and the machine's measures as the first baseline | Claude and me | W4 and W5, and my read of the pages (V1) |
| W9 | Apply the product machine to the RM plan as the first worked example: mark every RM task Auto, Draft or Me (not the per-AI-product blocks, which are in W3) | Claude, with me | V1 and W8 |
| W10 | Support model and incident runbook for one product: who users call, how issues are logged and fixed, and the steps to pause or roll back the product | Claude drafts, I review | W8 (the dry run shows what support is needed) |

## Stage 4. Get ready for Andy

**Who:** Claude builds, I decide when to share. Turn the plan into something Andy can see and react to, plus the questions I'd ask him.

| # | Item | Who | Waits on |
|---|---|---|---|
| W11 | Build an RM mock-up: clickable screens of the Monday opportunity list and the pre-meeting client brief, on made-up sample data, so Andy can see what an RM gets (the kit's mock-up piece, C40; stays in stage 4, C44) | Claude, with my review | Stage 1 |
| B1 | Which revenue lever matters most to the business right now? (from: the full RM plan, section 9, in RM Detail) | Me, with Andy | Nothing |
| B2 | How will success be judged in the first 6 months? (from: the full RM plan, section 9, in RM Detail) | Me, with Andy | Nothing |
| B3 | What are Andy's first use cases, and how does RM analytics rank against credit (portfolio management) and treasury and payments? (from: Bank Business Briefing, section 9) | Me, with Andy | Nothing |
| B4 | ⚠️ Is the new franchise banking team (the bank's national team for franchise owners, launched in April 2026), where RMs and portfolio managers sit together, the intended first team? This is my guess from our conversation (from: Chat, 2026-10-09) | Me, with Andy | Nothing |
| B5 | Does "Corporate & Commercial Banking" include commercial real estate and the specialty industries, and where does the role sit? (from: Bank Business Briefing, section 9) | Me, with Andy | Nothing |
| B6 | What team and budget are available for the pilot? (from: the full RM plan, section 9, in RM Detail) | Me, with Andy | Nothing |
| B7 | Which RM teams would make a good pilot group? (from: the full RM plan, section 9, in RM Detail) | Me, with Andy | Nothing |

## Alongside the path

Useful any time; none of these blocks a stage. Dated ones first.

| # | Item | Who | Waits on |
|---|---|---|---|
| W12 | First weekly review: what's working, what's annoying, what to change. Also re-check Anthropic's prompting guide for changes | Me, with Claude | About 2026-10-21 (not yet, said 2026-10-14) |
| W13 | Re-run the Bank Business Briefing after the bank's Q3 2026 results on October 22, 2026, using the saved prompt (Prompt 3 in the Prompt Library). Read the full Q2 earnings call transcript at the same time; only a summary was available the first time. The bank news scout's scheduled run on October 23 does the re-run as a draft | Claude | October 22, 2026 |
| W14 | Two loose ends from the McKinsey article: confirm its publication date (the pasted page showed none), and decide whether role redesign (new RM roles as agents take on work, McKinsey's fifth principle) belongs in the playbook; it isn't covered yet | Claude, then me | Nothing |
| W15 | Loose ends in the Bank Business Briefing: check the exact wording of the bank's AI announcement before quoting it; replace the 2016 description of who the segment serves once the annual report for the 2025 financial year can be opened in full; and confirm two of my guesses, the RM headcount read from an unclear chart and that Omaha came with American National | Claude | Nothing |
| W16 | Run the tests of Claude's rules that need a real session. Each test is a short scenario in `learning/tests.md` that checks one rule still works. Not yet run in a live session: T7, T10, T13, T14 and T17, and the second parts of T2, T3, T9 and T16. Never run at all: T18 to T22, T24 to T27 (including T27's new second part, from 2026-10-14), T30 to T33, T36 to T38, T40, T41 and T44; finish T35 after the bank news scout's first scheduled run on October 19. Re-run T8 (does Claude label every suggestion Needed or Optional?), which failed on 2026-10-09 before its rule was tightened, and T5, whose first run wasn't a fair test | Claude, in a new session | Nothing |
| W17 | Check the product details marked "(verify)" in the Tech Stack Guide: product names, prices, vendor terms and any update to the regulators' model-risk guidance. Eleven lines carry the mark. New lead (2026-10-13, the credit scan now summarized in the Use Case Library): SR 26-2, issued 17 April 2026, reportedly replaces SR 11-7, which our files cite; sources disagree on whether it covers generative AI, so read the Fed's own text before changing anything | Claude | Nothing |
| W18 | Claude Mastery course: paste in the next page (Module 3: Projects, Connectors and Skills). Claude starts a course notes file when it arrives (idea 14, approved) | Me, then Claude | Nothing |
| W19 | Try the newer skills on real work: "prototype X", "write a prompt for X", "new use case: X" | Me | Nothing |
| W20 | Playbooks for my everyday tools (idea 3, approved): name two or three tasks I repeat in email, calendar or documents. Claude turns each into a step-by-step skill | Me, then Claude | Nothing |
| W21 | Give the portfolio manager section of the Document Library the same plain numbered rows as the other sections (the RM section got them on 2026-10-18, C50), and write the group names the glossary's way: spelled out with the short form the first time on a page ("relationship managers (RMs)", "portfolio managers (PMs)"), then RM and PM | Me, with Claude | Nothing |

## Inside the bank

The plans rest on these, but only someone at the bank can answer them. Ask once I start; many overlap.

| # | Item | Who | Waits on |
|---|---|---|---|
| B8 | How many RMs, treasury management officers and portfolio managers are there today, by market, including American National? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B9 | How are RMs measured, paid and rewarded, and how are referrals to treasury, capital markets and wealth credited? (from: the full RM plan, section 9, in RM Detail; Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B10 | The value model's inputs: win rate, first-year revenue per win by product, and client-facing hours per RM today (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B11 | The segment's fee income by line today, including what sits inside the $47.6 million the bank doesn't break down (public figures stop at the 2025 financial year) (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B12 | The segment's deposits, and the share of borrowing clients who keep their main accounts with the bank (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B13 | What share of commercial clients use treasury management? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B14 | Does Finance accept costs saved and loan losses avoided as returns, as well as new revenue? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B15 | Who owns the client data in Snowflake and Salesforce, and which data lives where? (from: the full RM plan, section 9, in RM Detail; playbook sub-step 2.3 (the data contract)) | The bank | Starting at the bank |
| B16 | How is each platform set up for RMs today: which features, licenses and connections? Which Salesforce products does the bank own? Every tool named in the product machine's task tables is a guess until this is known (from: the full RM plan, section 9, in RM Detail; Tech Stack Guide; Product Machine) | The bank | Starting at the bank |
| B17 | Why does the bank have both Snowflake and Fabric, and which holds what? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B18 | Which AI models are approved, and where do they run? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B19 | Has the American National systems conversion happened, and are the acquired clients in Salesforce and Snowflake? (from: Bank Business Briefing, section 9) | The bank | Starting at the bank |
| B20 | Who builds: my team, IT, or business staff using click-to-build tools such as Power Platform? (from: Tech Stack Guide) | The bank | Starting at the bank |
| B21 | What does the AI governance process look like, and how long does a review usually take? (from: the full RM plan, section 9, in RM Detail; Tech Stack Guide) | The bank | Starting at the bank |
| B22 | May automations message people or update trackers by themselves? This decides how much of the product machine can run on its own (from: Product Machine) | The bank | Starting at the bank |
| B23 | Which tracker tool does the bank use for projects? (from: Product Machine; agent library) | The bank | Starting at the bank |
| B24 | Twenty smaller permissions (twenty-one "To confirm" items, minus the tracker question in B23) the general agents depend on, such as whether meeting recaps are allowed, which test environments exist and how sign-offs must be recorded. Each is listed under "To confirm" in the agent library, and one overlaps B22 (from: `playbook/agents.md`) | The bank | Starting at the bank |
| B25 | Do RMs work mainly in Salesforce? This decides where the insights appear (from: the full RM plan, section 5, in RM Detail) | The bank | Starting at the bank |
| B26 | The numbers still shown as [X] in the RM plan, the Product Workflow, the Product Framework and the Product Machine, such as payback months, weekly-use targets and how many projects I run at once, and the plan's week estimates. Each gets set with the bank's real figures (from: RM plan; Product Workflow; Product Framework; Product Machine) | The bank | Starting at the bank |
| B27 | The 46 guesses about the bank marked ⚠️ across the six playbook steps. Each gets replaced with a fact as I learn it. Many overlap B15 to B23 (from: Product Playbook) | The bank | Starting at the bank |
| B28 | The 21 bank terms listed at the end of the Glossary (such as "AI-sourced opportunity", "qualified opportunity" and "win rate"). Each is marked ⚠️ until the bank's own definition is recorded there, with its source. Many overlap B9 and B10 (from: Glossary) | The bank | Starting at the bank |

## Parked on purpose

| # | Item | Who | Waits on |
|---|---|---|---|
| P1 | The credit (portfolio management) plan. Started at my request on 2026-10-13 with the Portfolio Manager Core Use Cases page (now the Use Case Library's PM section; the six parked credit processes plus two new ones, each lined up with a core use case); the portfolio manager user workflow map is part of W2. The order is agreed (C33): credit memo and annual review drafts first, early warning second, risk ratings out of the first feature waves. The plan itself still waits. Ready for then: franchise banking as a possible pilot, and whether to add "costs saved" and "loan losses avoided" to the value model | Me | Me saying the RM framework is ready (D1) |
| P2 | Sharing with Associated. We share the same pages, not a separate edition (idea 33: no, 2026-10-15). When I'm ready, Claude lists which pages to share one by one from each page's Share menu | Me | Me saying I'm ready to share |
| P3 | A treasury and payments use case. The bank named it as a starting point for AI, and nothing has been planned yet | Me | After credit, unless B3 changes the order |
| P4 | **Featured: running many products at once.** One intake form for new product ideas, a scoring rule to rank them against each other, how many products I can run at once, my week and month across products, and when a live product is retired | Me | The machine running one product well first |
| P5 | A question sheet for my talk with the RM and credit leads (idea 59), built from The RM Assistant's "What to confirm": not yet, we still have a lot of work to do first (said 2026-10-17) | Me | Me saying we're ready for it |

## Closed

| # | Item | Closed |
|---|---|---|
| C1 | Build the Bank Business Briefing and save its prompt (merged into main as pull request #54) | 2026-10-09 |
| C2 | Decide the order of use cases: RM first, credit second | 2026-10-09 |
| C3 | Bring in the unmerged work from my other session. Merged into this log's pull request, with both sides kept where they overlapped | 2026-10-09 |
| C4 | Four ideas: yes. The shorthand check (idea 32) and the Steps and Controls catalogs (idea 34) are built. Fewer pop-ups (idea 2) and everyday playbooks (idea 3) need facts from me first: pop-ups closed as C37; everyday playbooks are W20 | 2026-10-09 |
| C5 | Remove my safety rules (idea 16). The pop-up explanations and "Deny is safe" reminders are gone from the rule book, with the two pop-up rules and their tests | 2026-10-09 |
| C6 | Make the RM plan's 14 team agents general: yes. They are now M20 to M33 in the agent library, used by every project; the RM plan shows how it uses each one | 2026-10-10 |
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
| C28 | Section links work: a link from one page to a section of another opens at that section. I checked it on 2026-10-15: a sub-step link on the Product Workflow page opened its card in the Steps Catalog. So the Document Library's section links and the links between the Product Workflow, Steps Catalog, Workflow Maps and Product Playbook stay as they are | 2026-10-15 |
| C29 | Ideas 48, 49 and 50: yes, all built. The audit checker now fails on any link to a section of another of our pages that doesn't exist (298 links checked), each task row on the Product Machine page links to its sub-step card in the Steps Catalog, and every wrap-up now puts forward two open ideas from the list (wrap-up step 4) | 2026-10-15 |
| C30 | Add an AI product under core use case 5, AI sales coaching (personal guidance from call transcripts): yes | 2026-10-15 |
| C31 | Move prospecting (winning new clients) earlier than wave 3: yes | 2026-10-15 |
| C32 | Keep autonomous lead nurturing and pricing out of the RM plan for now, because they conflict with "nothing reaches a client without the RM" and the fair-lending control (K3): yes. Revisit later with evidence | 2026-10-15 |
| C33 | The credit order on the Portfolio Manager Core Use Cases page: yes. Credit memo and annual review drafts first, early warning second, risk ratings kept out of the first feature waves. The credit plan itself stays parked (P1) | 2026-10-15 |
| C34 | The eight Elon mode suggestions: yes to all, built 2026-10-15. The automation check now cuts first (should it exist, delete, simplify, faster) before it automates; every control says where it comes from (law or regulator, bank policy, our choice) and who to ask to change it, with a table for the sub-steps and gates in the playbook; the dry run (W8) includes a deletion pass; each project names its limiting factor (W5 and the running layer); the first-time log gives a wait index; the Product Machine measures the machine itself; gates are decided in writing when clean; and a new elon-mode skill reviews the work at every fifth wrap-up | 2026-10-15 |
| C35 | Requirement sources check (idea 52): yes, built. The audit checker now fails if a control has no "Comes from" line, or if a sub-step that sets, builds, proves or watches a law or bank-policy control is missing from the playbook's "Where the requirements come from" table; every sub-step that sets, builds, proves or watches such a control is now in the table | 2026-10-15 |
| C36 | The Audit Log (renamed from "How We Deliver Audit"): approved with all six improvements. Built: a GitHub check on every pull request, an Audit Log row after every audit, three audit sizes (quick, standard, deep), rule tests at every weekly review, lost lines counted per file. The pop-up fix was done the same day (C37) | 2026-10-15 |
| C37 | Fewer approval pop-ups (idea 2): the page rule is in `.claude/settings.json` (my commit, repaired by Claude the same day, pull request #96). Pages should no longer ask for approval from the next session | 2026-10-15 |
| C38 | The GitHub audit check is now required (idea 56). After the move to JD-Personal-Brain I ticked "Require status checks to pass before merging" with **audit** on main's rule; Claude's test (pull request #100, with a deliberate checker failure) showed GitHub reporting it as blocked, so a pull request with a red audit mark can't be merged, even from my phone | 2026-10-15 |
| C39 | The six gaps from the 2026-10-15 audit of How we deliver (idea 54): all six recommendations approved and written in. The Product Framework now says which gate is passed for a project, an AI product or a feature wave, the quick pass for each new feature wave, and when a change after launch goes back through step 4 (a material change); control K3 is now "AI drafts or flags; a named credit officer decides", with a higher-risk path set at 2.4; sub-steps 2.3, 3.2 and 3.3 cover products built on documents; and 1.3, 1.4 and 1.7 start from the user workflow map. The three Optional gaps (review depth by risk rating, four new controls, a fallback for each ⚠️ Auto task) stay on the Audit Log page | 2026-10-15 |
| C40 | The use case kit (Prompt 1 in the Prompt Library, stage 1 for RMs): agreed. Every use case has 4 leader pieces (the case, the plan on a page, the value, the ask) and 10 working pieces (user workflow, core use cases, AI products, value model, who decides, the six steps, measures and dashboard, risks and controls, agent specs and workflows, mock-up); the RM plan's sections 8 ("Built to reuse") and 10 ("How this plan covers the role") leave the kit. Decisions 2 to 5 on the review page follow (C41 onward) | 2026-10-17 |
| C41 | Where the two 2026-10-15 changes go in the RM plan (use case kit decision 2): prospect lookalikes move from wave 3 to wave 2 (about week 10), and the new AI sales coaching product takes their place in wave 3 (about week 15), because it needs call transcripts, recording consent (control K24) and more review: agreed | 2026-10-17 |
| C42 | One source for the RM plan (use case kit decision 3): agreed. The plan's working file (`memos/rm-analytics-framework.md`) becomes the one source, the long scrolling page is built from it by a script, and the RM Analytics Framework design page (the summary and six parts side by side) is retired and leaves the library. This replaces the 2026-10-09 agreement that edits go to the design page first; the work itself is done in stage 2 of the use case kit | 2026-10-17 |
| C43 | The RM Leader Brief (use case kit decision 4): agreed. One new page for Andy and bank leaders in four parts (the case, the plan on a page, the value, the ask), every line linking down to its detail; it replaces the one-page RM summary, is the Andy edition (W3), is built only after the Elon mode review of the RM plan, and follows Sample 1 on the review page | 2026-10-17 |
| C44 | The fix order for stage 2 of the use case kit (decision 5): agreed. 1. a current, single-source plan (the 2026-10-15 decisions and agreed waves, the plan in line with How we deliver, the scrolling page built from the working file); 2. the RM user workflow (W2), sample first; 3. the Elon mode review, then the RM Leader Brief (W3); 4. one block per AI product, exact measures and controls per AI product, the coaching product's agent and workflow. W9 and W11 stay in their stages | 2026-10-17 |
| C45 | A use case kit check (idea 58): yes, built. The audit checker now fails if a library section marked as following the use case kit is missing a kit piece (leader brief, user workflow, core use cases, plan, mock-up), as a page or a "to build" row. The RM section is marked and gained two "to build" rows (the RM Leader Brief and the RM mock-up); the portfolio manager section is marked when we move into PM. The reply-length warning (idea 57) stays not yet | 2026-10-17 |
| C46 | The RM Assistant (said 2026-10-17): yes, as our working hypothesis and the core RM product. Each RM gets one personal AI assistant, with limits (jobs, workflows, data, controls, feedback), capabilities for each moment of the RM's work drawn from McKinsey's use cases, our own needs and the RM's job, and a shared foundation that portfolio managers reuse. The RM Assistant page (https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2, working copy `memos/rm-assistant.md`) is in the library's RM section. The RM plan was rebuilt around it the same day (C47) | 2026-10-17 |
| C47 | The five Elon mode findings on the RM plan (said 2026-10-17): yes to all five, applied in memo v10. No week dates for waves 2 and 3 until gate 2; wave 1 is three capabilities (the pre-meeting client brief; the meeting follow-up, with call notes into Salesforce; the Monday opportunity list); the how-to helper (A6) removed and its number not reused; what the Product Framework says is linked, not repeated; freed-up time counted as hours, not revenue; the limiting factor named at the top. The page is renamed the RM Assistant Plan, and its wave 3 "RM assistant" is now Client Q&A (A5) | 2026-10-17 |
| C48 | A check that The RM Assistant page and the RM plan list the same capabilities in the same waves (idea 60): yes (said 2026-10-17), built as check 17 of the audit checker; it fails if either page lists a capability or wave the other doesn't | 2026-10-17 |
| C49 | An automatic length warning on Claude's replies (idea 57): yes (said 2026-10-17), built. A Stop hook (`.claude/hooks/reply-length.py`, switched on in `.claude/settings.json`) stops Claude once when a reply runs past 8 lines and asks for a short follow-up: the outcome, what it means and at most one step | 2026-10-17 |
| C50 | Reorganize the RM work (said 2026-10-18): yes. The RM section holds only three short pages for people, read in order: the RM Executive Summary (one page for the leaders of the RM business; it is the RM Leader Brief, C43), The RM Assistant (the product, cut short) and the RM Assistant Plan (cut from about 15 pages to a few). Everything in full goes into RM Detail (a fourth row in the RM section, for AI to read; first put in Reference as RM Product Information for AI), one document to give an AI, built from the working files. The core use case pages became one Use Case Library in Reference, with a section for RMs and one for PMs. The use case kit check now asks for those three pages (summary, product, plan) | 2026-10-18 |
| C51 | I read the Use Case Library: good to go, now marked In use | 2026-10-18 |

_Last updated: 2026-10-18_
