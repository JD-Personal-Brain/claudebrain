# Open Items

The AI program delivers two personal AI assistants at the same time: one for each relationship manager (RM) and one for each portfolio manager (PM). Both run on one shared platform. This log lists what's still open on each of those three tracks, plus the decisions that cover the whole program.

> **How to read this.** Each track is numbered on its own (D for program decisions, PL for the shared platform, RM and PM for the two assistants, F for later): work first, then questions for the bank, each in priority order. When priorities change, the numbers change with them. **Owner** says who moves an item next, and ⚠️ marks an assumption to confirm with the bank. Finished items are closed and kept on record in the working copy. The full question lists live in each plan's "What I'd confirm in the first weeks" (RM Detail and PM Detail).

## Where the program stands

**The limiting factor right now** (our assumption, to confirm with the bank): how long the bank's review of AI takes, and what usually holds one up (PL7). Both assistants' timelines rest on it, so it is the first question in every conversation.

| Track | Where it is | Next milestone |
|---|---|---|
| **The shared platform** (what both assistants run on) | One delivery process (six steps with go/no-go gates), 25 controls and 43 agents specified. The shared foundation is designed: certified data, the bank's documents read with sources, a signals engine, and drafting with every number checked. Nothing is built on bank systems or run end to end yet | A dry run of the delivery process (PL1); confirm the bank's platforms, data owners and AI review |
| **The RM Assistant** | Working hypothesis. Three short pages and a clickable prototype with live agents, reviewed. Feature wave 1: the pre-meeting client brief, the meeting follow-up and the Monday list | Test it with the RM lead: how RMs work today, and which team pilots first |
| **The PM Assistant** | Working hypothesis. Three short pages and a clickable prototype, reviewed and in use. Feature wave 1: the industry background draft, the borrower file, then annual review and credit memo drafts (the higher-risk path) | Test it with the credit lead: today's industry background work, the review of AI that informs credit, and who the credit policy owner is |

## Decisions for the program

Decisions bank leaders make once, for both assistants.

| # | Decision | Owner | When |
|---|---|---|---|
| D1 | Which outcomes matter most right now (revenue, banker capacity, credit quality), how success will be judged in the first 6 months, and where Corporate & Commercial Banking's edges are (commercial real estate, the specialty industries) | Bank leaders, with the product manager | At the start of Discover (sub-step 1.1) |
| D2 | The order and overlap of the two assistants: both start together, or one leads by a few weeks; and where treasury and payments fits | Bank leaders, with the product manager | At the start of Discover (sub-step 1.1) |
| D3 | The pilot group. ⚠️ Our assumption: the franchise banking team (launched April 2026), where RMs and PMs work side by side, so one team can pilot both assistants | Bank leaders, with the product manager | By the end of Define (sub-step 2.8) |
| D4 | The team and budget for the pilot | Bank leaders | By the end of Define (sub-step 2.8) |

## The shared platform

Built once and used by both assistants: data, controls, the AI review and the delivery process.

**Work**

| # | Work | Owner | When |
|---|---|---|---|
| PL1 | Dry run of the delivery process: take one small made-up product through all six steps with the templates and two or three agents built as working prototypes, and log where it breaks. Include a deletion pass: mark every sub-step, agent and control "did it change a decision or catch a problem?" and delete what didn't, until about 1 in 10 has to come back; law and bank-policy items are never cut. Record each sub-step's wait index and the machine's measures as the first baseline. Merge overlapping agents during the deletion pass (the Agent Library lists them) | Product manager, with Claude | Now; needs only the first three PL2 templates |
| PL2 | Ready-to-fill templates, built as the dry run reaches them: first the brief, the data contract and the gate pack; then the value model, risk intake, decision log, evidence pack, monitoring plan (with the control watch list) and release-readiness checklist | Claude drafts, product manager reviews | The first three now; the rest during PL1 |
| PL3 | The tracker design and the approvals map. Tracker: the fields every task carries, written to work in any tool (PL10 is still open); each project's tracker opens with its limiting factor and owner, and records each sub-step's start and finish dates and hours, so the wait index and the machine's measures come straight from it. Approvals map: who signs what at each gate, typical turnaround ⚠️, and who to go to when a sign-off is stuck | Claude drafts, product manager reviews | During PL1 |
| PL4 | Close the three control gaps the Controls Catalog found in the playbook: K3's guardrails and named credit officer, K19's check against the approved-model list, K23's proof that only approved AI tools are used. Each needs a line in the right playbook step, or a decision that it isn't needed (the other nine gaps were closed on 2026-10-18 by the control watch list in the monitoring plan) | Claude drafts, product manager reviews | During PL1 |
| PL5 | Support model and incident runbook: who users call, how issues are logged and fixed, and the steps to pause or roll back a product | Claude drafts, product manager reviews | After PL1; before the first go-live |
| PL6 | Apply the delivery process to both plans, once the dry run has cut it down: mark every RM and PM task Auto, Draft, Me or Partner (the per-capability blocks are in RM3) | Product manager, with Claude | After PL1 |

**Questions for the bank**

| # | Question | Owner | When |
|---|---|---|---|
| PL7 | What does the AI governance process look like, how long does a review usually take, what usually holds one up, and how is AI that informs credit reviewed? Which model risk guidance does the bank follow today: SR 11-7, or SR 26-2, reportedly issued in April 2026 ⚠️? | The bank | First conversation |
| PL8 | Which AI models are approved, and where do they run? How is each platform set up (features, licenses and connections; which Salesforce products; the loan system and spreading tool)? Every tool named in the Product Machine is a guess until this is known | The bank | Define |
| PL9 | Who owns client and borrower data, and what lives where (Snowflake, Fabric, Salesforce, the loan system)? Why both Snowflake and Fabric? Are American National's clients and borrowers on the bank's systems yet? | The bank | Define |
| PL10 | Who builds (our team, IT, or business staff with click-to-build tools such as Power Platform)? May automations message people or update trackers by themselves? Which tracker tool is used? And the smaller permissions the general agents depend on, listed under "To confirm" in the agent library | The bank | Define |
| PL11 | Does Finance count costs saved and loan losses avoided as returns, as well as new revenue, and how are banker hours valued? | The bank | Define |

## The RM Assistant

**Work**

| # | Work | Owner | When |
|---|---|---|---|
| RM1 | Test the RM pages and the RM Assistant Prototype with the RM lead (October 20, 2026), and improve each page from what the bank says. Every fact about how the bank's RMs work stays an assumption until then | Product manager, with Claude | October 20, 2026 |
| RM2 | Map how RMs work today, where each capability fits and how the work changes, as a draft of assumptions for the RM lead to correct (building on Map 2 on the Workflow Maps) | Product manager, with Claude | Now |
| RM3 | The RM plan's remaining detail: one block per AI product with exact measures and controls, and the AI sales coaching agent spec and workflow (RM Detail: "How each capability is built", and the full plan's Appendices A and B) | Claude drafts, product manager reviews | Now |

**Questions for the bank**

| # | Question | Owner | When |
|---|---|---|---|
| RM4 | May client meetings be recorded? The meeting follow-up rests on it | The bank | First conversation |
| RM5 | How many RMs and treasury management officers are there, by market? How are RMs measured, paid and rewarded, and how are referrals to treasury, capital markets and wealth credited? | The bank | Discover |
| RM6 | The value model's inputs: win rate, first-year revenue per win by product, client-facing hours per RM, the segment's fee income by line (including the $47.6 million not broken down publicly), deposits, the share of borrowing clients who keep their main accounts with the bank, and treasury management use | The bank | Discover |
| RM7 | Do RMs work mainly in Salesforce? This decides where the assistant appears | The bank | Define |

## The PM Assistant

**Work**

| # | Work | Owner | When |
|---|---|---|---|
| PM1 | Test the PM section with the credit lead (October 20, 2026) and improve each page from what the bank says: the PM Executive Summary, The PM Assistant, the PM Assistant Plan, the PM Assistant Prototype and PM Detail. Every fact about how the bank's PMs work stays an assumption until then | Product manager, with Claude | October 20, 2026 |
| PM2 | Map how PMs work today, where each capability fits and how the work changes, as a draft of assumptions for the credit lead to correct (building on Map 3 on the Workflow Maps) | Product manager, with Claude | After PM1 |

**Questions for the bank**

| # | Question | Owner | When |
|---|---|---|---|
| PM3 | The industry background section today: which outside firm writes it, its cost, how many a year, how long each takes, the contract's notice period, which sources the firm uses, and does the bank already license industry data? ⚠️ | The bank | First conversation |
| PM4 | Who is the credit policy owner, who is the credit officer for each kind of decision, and who keeps the approval-authority list? | The bank | Discover |
| PM5 | How many PMs and credit analysts are there, how many borrowers each, and how many annual reviews and memos a year? How long does a review take, and which part takes longest? | The bank | Discover |
| PM6 | Is there a standard template for annual reviews and credit memos, and how is credit quality watched today (a watchlist, a portfolio review), and by whom? | The bank | Define |
| PM7 | How are PMs measured? | The bank | Define |

## Later

| # | Item | Owner | When |
|---|---|---|---|
| F1 | A third assistant, for treasury and payments. The bank named it as a starting point for AI; nothing is planned yet | Product manager | Once the first two run, unless D2 changes the order |
| F2 | Running several AI products at once: one intake form for new product ideas, a scoring rule to rank them, how many run at once, my week and month across products, and when a live product is retired | Product manager | Once one product runs end to end |

## My workspace

Upkeep of the reference pages and of how I work with Claude. Not shown on the page; none of it blocks the program.

| # | Item | Who | Waits on |
|---|---|---|---|
| W1 | First weekly review: what's working, what's annoying, what to change. Also re-check Anthropic's prompting guide for changes | Me, with Claude | About 2026-10-21 (not yet, said 2026-10-14) |
| W2 | Re-run the Bank Business Briefing after the bank's Q3 2026 results on October 22, 2026, using the saved prompt (Prompt 3 in the Prompt Library). Read the full Q2 earnings call transcript at the same time; only a summary was available the first time. The bank news scout's scheduled run on October 23 does the re-run as a draft. At the same time, close the loose ends in the Bank Business Briefing: check the exact wording of the bank's AI announcement before quoting it; replace the 2016 description of who the segment serves once the annual report for the 2025 financial year can be opened in full; and confirm two of my guesses, the RM headcount read from an unclear chart and that Omaha came with American National; and two from the McKinsey article: confirm its publication date (the pasted page showed none), and decide whether role redesign (new RM roles as agents take on work, McKinsey's fifth principle) belongs in the playbook; it isn't covered yet | Claude | October 22, 2026 |
| W3 | Run the tests of Claude's rules that need a real session. Each test is a short scenario in `learning/tests.md` that checks one rule still works. Not yet run in a live session: T7, T10, T13, T14 and T17, and the second parts of T2, T3, T9 and T16. Never run at all: T18 to T22, T24 to T27 (including T27's new second part, from 2026-10-14), T30 to T33, T36 to T38, T40, T41 and T44; finish T35 after the bank news scout's first scheduled run on October 19. Re-run T8 (does Claude label every suggestion Needed or Optional?), which failed on 2026-10-09 before its rule was tightened, and T5, whose first run wasn't a fair test | Claude, in a new session | Nothing |
| W4 | Check the product details marked "(verify)" in the Tech Stack Guide: product names, prices, vendor terms and any update to the regulators' model-risk guidance. Eleven lines carry the mark. New lead (2026-10-13, the credit scan now summarized in the Use Case Library): SR 26-2, issued 17 April 2026, reportedly replaces SR 11-7, which our files cite; sources disagree on whether it covers generative AI, so read the Fed's own text before changing anything | Claude | Nothing |
| W5 | Claude Mastery course: paste in the next page (Module 3: Projects, Connectors and Skills). Claude starts a course notes file when it arrives (idea 14, approved) | Me, then Claude | Nothing |
| W6 | Playbooks for my everyday tools (idea 3, approved): name two or three tasks I repeat in email, calendar or documents. Claude turns each into a step-by-step skill | Me, then Claude | Nothing |
| W7 | Process fixes from the Elon mode reviews of 2026-10-18 not built yet (the wrap-up script, a lighter wrap-up, a shorter NOW.md and audit sizing are done): one list of pages (the library file only); counts inserted from one source; turn repeated reviewer findings into checks (links that don't resolve, a footer date older than the file, and every agent, control or workflow number linking to its card: idea 62, suggested 2026-10-19; and a check that no workspace or closed item shows on the Open Items page, or is cited by a page the bank reads: idea 63, suggested 2026-10-19). The user-workflow routine (idea 41) gets its first use on RM2 and PM2; a rename command; build the Product Workflow page from its working file; count what each checker check catches and drop the silent ones; run or retire the 30 rule tests never run (one test per rule); one home for repeated rules ("in writing; a meeting only if contested" is in about 35 lines across 11 files). Needs my yes: the GitHub check also runs the render check and the prototype tests | Claude | Nothing (the GitHub check: my yes) |

## Closed

| # | Item | Closed |
|---|---|---|
| C1 | Build the Bank Business Briefing and save its prompt (merged into main as pull request #54) | 2026-10-09 |
| C2 | Decide the order of use cases: RM first, credit second | 2026-10-09 |
| C3 | Bring in the unmerged work from my other session. Merged into this log's pull request, with both sides kept where they overlapped | 2026-10-09 |
| C4 | Four ideas: yes. The shorthand check (idea 32) and the Steps and Controls catalogs (idea 34) are built. Fewer pop-ups (idea 2) and everyday playbooks (idea 3) need facts from me first: pop-ups closed as C37; everyday playbooks are W19 | 2026-10-09 |
| C5 | Remove my safety rules (idea 16). The pop-up explanations and "Deny is safe" reminders are gone from the rule book, with the two pop-up rules and their tests | 2026-10-09 |
| C6 | Make the RM plan's 14 team agents general: yes. They are now M20 to M33 in the agent library, used by every project; the RM plan shows how it uses each one | 2026-10-10 |
| C7 | Three new controls: yes. K23 (approved AI tools for the team's own work), K24 (consent before recording) and K25 (agents stop rather than guess) are in the Controls Catalog, set and built in the playbook (proving K23 and watching all three are still gaps, in the control-gaps item); the playbook's control check (4.5) now also confirms the build, test and live path and IT's approval of every connection | 2026-10-10 |
| C8 | The line saying credit comes next moved to the leader edition item, later decided: no separate edition (C66) | 2026-10-10 |
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
| C26 | Thinking through the job, Part 1 (the Job Notes page): not required, so it's off the Document Library and no longer an open item. The working file was deleted on 2026-10-19 (C67) | 2026-10-14 |
| C27 | Idea 46: yes. Every audit now runs a "nothing lost" check (`lost-lines.py`) that lists each sentence that disappeared from the working files, and each one must be put back or explained | 2026-10-14 |
| C28 | Section links work: a link from one page to a section of another opens at that section. I checked it on 2026-10-15: a sub-step link on the Product Workflow page opened its card in the Steps Catalog. So the Document Library's section links and the links between the Product Workflow, Steps Catalog, Workflow Maps and Product Playbook stay as they are | 2026-10-15 |
| C29 | Ideas 48, 49 and 50: yes, all built. The audit checker now fails on any link to a section of another of our pages that doesn't exist (298 links checked), each task row on the Product Machine page links to its sub-step card in the Steps Catalog, and every wrap-up now puts forward two open ideas from the list (wrap-up step 4) | 2026-10-15 |
| C30 | Add an AI product under core use case 5, AI sales coaching (personal guidance from call transcripts): yes | 2026-10-15 |
| C31 | Move prospecting (winning new clients) earlier than wave 3: yes | 2026-10-15 |
| C32 | Keep autonomous lead nurturing and pricing out of the RM plan for now, because they conflict with "nothing reaches a client without the RM" and the fair-lending control (K3): yes. Revisit later with evidence | 2026-10-15 |
| C33 | The credit order on the Portfolio Manager Core Use Cases page: yes. Credit memo and annual review drafts first, early warning second, risk ratings kept out of the first feature waves. The credit plan itself stays parked (until 2026-10-19, C62) | 2026-10-15 |
| C34 | The eight Elon mode suggestions: yes to all, built 2026-10-15. The automation check now cuts first (should it exist, delete, simplify, faster) before it automates; every control says where it comes from (law or regulator, bank policy, our choice) and who to ask to change it, with a table for the sub-steps and gates in the playbook; the dry run (W8) includes a deletion pass; each project names its limiting factor (W5 and the running layer); the first-time log gives a wait index; the Product Machine measures the machine itself; gates are decided in writing when clean; and a new elon-mode skill reviews the work at every fifth wrap-up | 2026-10-15 |
| C35 | Requirement sources check (idea 52): yes, built. The audit checker now fails if a control has no "Comes from" line, or if a sub-step that sets, builds, proves or watches a law or bank-policy control is missing from the playbook's "Where the requirements come from" table; every sub-step that sets, builds, proves or watches such a control is now in the table | 2026-10-15 |
| C36 | The Audit Log (renamed from "How We Deliver Audit"): approved with all six improvements. Built: a GitHub check on every pull request, an Audit Log row after every audit, three audit sizes (quick, standard, deep), rule tests at every weekly review, lost lines counted per file. The pop-up fix was done the same day (C37) | 2026-10-15 |
| C37 | Fewer approval pop-ups (idea 2): the page rule is in `.claude/settings.json` (my commit, repaired by Claude the same day, pull request #96). Pages should no longer ask for approval from the next session | 2026-10-15 |
| C38 | The GitHub audit check is now required (idea 56). After the move to this repository I ticked "Require status checks to pass before merging" with **audit** on main's rule; Claude's test (pull request #100, with a deliberate checker failure) showed GitHub reporting it as blocked, so a pull request with a red audit mark can't be merged, even from my phone | 2026-10-15 |
| C39 | The six gaps from the 2026-10-15 audit of How we deliver (idea 54): all six recommendations approved and written in. The Product Framework now says which gate is passed for a project, an AI product or a feature wave, the quick pass for each new feature wave, and when a change after launch goes back through step 4 (a material change); control K3 is now "AI drafts or flags; a named credit officer decides", with a higher-risk path set at 2.4; sub-steps 2.3, 3.2 and 3.3 cover products built on documents; and 1.3, 1.4 and 1.7 start from the user workflow map. The three Optional gaps (review depth by risk rating, four new controls, a fallback for each ⚠️ Auto task) stay on the Audit Log page | 2026-10-15 |
| C40 | The use case kit (Prompt 1 in the Prompt Library, stage 1 for RMs): agreed. Every use case has 4 leader pieces (the case, the plan on a page, the value, the ask) and 10 working pieces (user workflow, core use cases, AI products, value model, who decides, the six steps, measures and dashboard, risks and controls, agent specs and workflows, mock-up); the RM plan's sections 8 ("Built to reuse") and 10 ("How this plan covers the role") leave the kit. Decisions 2 to 5 on the review page follow (C41 onward) | 2026-10-17 |
| C41 | Where the two 2026-10-15 changes go in the RM plan (use case kit decision 2): prospect lookalikes move from wave 3 to wave 2 (about week 10), and the new AI sales coaching product takes their place in wave 3 (about week 15), because it needs call transcripts, recording consent (control K24) and more review: agreed | 2026-10-17 |
| C42 | One source for the RM plan (use case kit decision 3): agreed. The plan's working file (`memos/rm-analytics-framework.md`) becomes the one source, the long scrolling page is built from it by a script, and the RM Analytics Framework design page (the summary and six parts side by side) is retired and leaves the library. This replaces the 2026-10-09 agreement that edits go to the design page first; the work itself is done in stage 2 of the use case kit | 2026-10-17 |
| C43 | The RM Leader Brief (use case kit decision 4): agreed. One new page for bank leaders in four parts (the case, the plan on a page, the value, the ask), every line linking down to its detail; it replaces the one-page RM summary, is the leader edition, is built only after the Elon mode review of the RM plan, and follows Sample 1 on the review page | 2026-10-17 |
| C44 | The fix order for stage 2 of the use case kit (decision 5): agreed. 1. a current, single-source plan (the 2026-10-15 decisions and agreed waves, the plan in line with How we deliver, the scrolling page built from the working file); 2. the RM user workflow (W2), sample first; 3. the Elon mode review, then the RM Leader Brief (C43); 4. one block per AI product, exact measures and controls per AI product, the coaching product's agent and workflow. W9 and the RM mock-up (since closed as C60) stay in their stages | 2026-10-17 |
| C45 | A use case kit check (idea 58): yes, built. The audit checker now fails if a library section marked as following the use case kit is missing a kit piece (leader brief, user workflow, core use cases, plan, mock-up), as a page or a "to build" row. The RM section is marked and gained two "to build" rows (the RM Leader Brief and the RM mock-up); the portfolio manager section is marked when we move into PM. The reply-length warning (idea 57) stays not yet | 2026-10-17 |
| C46 | The RM Assistant (said 2026-10-17): yes, as our working hypothesis and the core RM product. Each RM gets one personal AI assistant, with limits (jobs, workflows, data, controls, feedback), capabilities for each moment of the RM's work drawn from McKinsey's use cases, our own needs and the RM's job, and a shared foundation that portfolio managers reuse. The RM Assistant page (https://claude.ai/artifact/RBaZS636CtycDwZyDrgum2, working copy `memos/rm-assistant.md`) is in the library's RM section. The RM plan was rebuilt around it the same day (C47) | 2026-10-17 |
| C47 | The five Elon mode findings on the RM plan (said 2026-10-17): yes to all five, applied in memo v10. No week dates for waves 2 and 3 until gate 2; wave 1 is three capabilities (the pre-meeting client brief; the meeting follow-up, with call notes into Salesforce; the Monday opportunity list); the how-to helper (A6) removed and its number not reused; what the Product Framework says is linked, not repeated; freed-up time counted as hours, not revenue; the limiting factor named at the top. The page is renamed the RM Assistant Plan, and its wave 3 "RM assistant" is now Client Q&A (A5) | 2026-10-17 |
| C48 | A check that The RM Assistant page and the RM plan list the same capabilities in the same waves (idea 60): yes (said 2026-10-17), built as check 17 of the audit checker; it fails if either page lists a capability or wave the other doesn't | 2026-10-17 |
| C49 | An automatic length warning on Claude's replies (idea 57): yes (said 2026-10-17), built. A Stop hook (`.claude/hooks/reply-length.py`, switched on in `.claude/settings.json`) stops Claude once when a reply runs past 8 lines and asks for a short follow-up: the outcome, what it means and at most one step | 2026-10-17 |
| C50 | Reorganize the RM work (said 2026-10-18): yes. The RM section holds only three short pages for people, read in order: the RM Executive Summary (one page for the leaders of the RM business; it is the RM Leader Brief, C43), The RM Assistant (the product, cut short) and the RM Assistant Plan (cut from about 15 pages to a few). Everything in full goes into RM Detail (a fourth row in the RM section, for AI to read; first put in Reference as RM Product Information for AI), one document to give an AI, built from the working files. The core use case pages became one Use Case Library in Reference, with a section for RMs and one for PMs. The use case kit check now asks for those three pages (summary, product, plan) | 2026-10-18 |
| C51 | I read the Use Case Library: good to go, now marked In use | 2026-10-18 |
| C52 | The deep audit and Elon mode review of the RM work (said 2026-10-18: go with the recommendations): about 35 fixes made (bank facts marked as assumptions, plainer words, wording aligned with the How we deliver pages); gate 1 aligned with the Product Workflow (target, measure and today's baseline agreed at gate 1); the full plan cut from about 10,500 to about 5,100 words (one step table, no duplicate summary, capabilities or team-agent table); agent A4 merged into workflow B1; wave 1's Monday list suggests only deposit and treasury gaps (credit products wait for the PM work). What the prototype shows is next | 2026-10-18 |
| C53 | The RM section's order (said 2026-10-18): the RM Assistant Prototype is row 4 and RM Detail row 5, after the three short pages for people (C50) | 2026-10-18 |
| C54 | Regroup the Document Library by use, for a human reader (said 2026-10-18): seven sections. "The bank and the role" adds the Job Description and Tech Stack Guide; Reference holds only the five lookup pages, in process order (Glossary, Steps Catalog, Workflow Maps, Agent Library, Controls Catalog); Research adds the Use Case Library; a new "My workspace" section, for me only, holds Open Items, the Audit Log, the Prompting Guide and the Prompt Library | 2026-10-18 |
| C55 | RM gate 1 timing (said 2026-10-18: overlap, as recommended): the overlapping first pass is written into the Product Framework, so gate 1 can pass on a first sizing and a provisional baseline, with the rest of Discover and the final baseline finished by gate 2 | 2026-10-18 |
| C56 | The checker rule for one user group per people page (idea 61, an open decision until now): yes on 2026-10-18 and built the same day as checker check 18 | 2026-10-18 |
| C57 | The question sheet for my talk with the RM and credit leads (idea 59, parked until now): no (said 2026-10-18) | 2026-10-18 |
| C58 | My workspace in the Document Library isn't private any more (said 2026-10-18: I don't mind people seeing my work): the "for me only" wording is gone from the library, and Open Items can be shared like any other page | 2026-10-18 |
| C59 | Read the three short RM pages: reviewed and good (said 2026-10-19); the RM pages are now In use in the Document Library | 2026-10-19 |
| C60 | The RM mock-up: the RM Assistant Prototype, version 4, reviewed and good (said 2026-10-19) | 2026-10-19 |
| C61 | Is the RM framework ready to copy to other use cases? Yes (said 2026-10-19: the RM section is complete); the portfolio manager work starts (W1) | 2026-10-19 |
| C62 | The parked credit (portfolio management) plan: started on 2026-10-19 with Prompt 5. Its first cut includes the two open questions it kept: franchise banking as a possible pilot stays a question for the bank (B4), and the PM value model now counts costs saved and tracks loan losses avoided (not counted until Finance and credit risk agree a method) | 2026-10-19 |
| C63 | The portfolio manager section of the Document Library gets the same plain numbered rows as the RM section, with the group names written the glossary's way | 2026-10-19 |
| C64 | The industry background section of credit memos, written today by an outside firm the bank pays (the credit lead, 2026-10-19): made the PM Assistant's first capability, the industry background draft (agent A11, workflow B16), live at about week 6 | 2026-10-19 |
| C65 | The bank news scout's first weekly run: it ran and succeeded on Monday October 19, 2026; its notice goes to my personal email by the scheduled task itself | 2026-10-19 |
| C66 | Sharing with Associated: yes. The Document Library and the GitHub repository are shared with Andy (said 2026-10-19). Every page is shared as it is, with no separate edition (idea 33: no, 2026-10-15); sharing the library doesn't share the pages it links to, so each page is shared from its own Share menu | 2026-10-19 |
| C67 | Ready to share the repo (said 2026-10-19): the two unused interview-prep files (job notes and job prompts) deleted, a README added at the top of the repo, and the pay range taken off the Job Description page; the repo is shared as it is, history included | 2026-10-19 |
| C68 | Try the newer skills on real work: "prototype X", "write a prompt for X", "new use case: X": done in practice (the prototype skill built both assistants' prototypes, and Prompt 5 built the PM section); closed in the Elon mode review of the Open Items log (said 2026-10-19: apply all five) | 2026-10-19 |
| C69 | The PM section: reviewed and in use (said 2026-10-19): the PM Executive Summary, The PM Assistant, the PM Assistant Plan and the PM Assistant Prototype are In use in the Document Library; PM Detail stays a reference page for AI | 2026-10-19 |


_Last updated: 2026-10-19_
