# Glossary: the words we use

One meaning for each word, used the same way in every plan, playbook page and
agent spec. The audit checks the core documents against it.

> **Two kinds of terms.** The first three sections are our own working words for
> how products are delivered: the bank won't supply these, so we define them.
> The last section lists the bank's business terms our plans depend on. Those
> are **not** defined here: each one is marked ⚠️ until the bank's own
> definition replaces it, because the bank's own names and definitions are the ones we plug into.

## How the work is organized

| Term | What it means |
|---|---|
| **Step** | One of the six parts every product goes through: Discover, Define, Build, Govern and test, Release and adopt, Measure and iterate. |
| **Sub-step** | A numbered piece of a step, from 1.0 to 6.6 (44 in all). Each has its own section in the playbook and its own card in the Steps Catalog. |
| **Gate** | The go/no-go decision at the end of each step. A named person decides, and the decision goes in the decision log. |
| **Governance thread** | The risk and control work that runs through every step, so that step 4 confirms what risk partners have already seen. |
| **Core use case** | One of the seven needs a plan's AI products answer (in the RM plan, each of The RM Assistant's capabilities answers one). The RM plan set them: McKinsey's five frontline use cases (prospecting and next best opportunities, lead nurturing, account intelligence and meeting prep, deal scoring and pricing, AI sales coaching) plus two of our own (admin off the RM's plate, keep clients). The credit work is proposed to reuse the same seven needs through each one's credit counterpart (the Use Case Library's portfolio manager section; used in the PM plan, reviewed 2026-10-19). Say **RM core use case** or **credit core use case** when it matters which. Each has a user problem and a return profile. |
| **Credit counterpart** | The credit-side version of an RM core use case, for portfolio managers and credit analysts; for example, credit memo and annual review drafts under account intelligence and meeting prep (see the Use Case Library's portfolio manager section). |
| **Use case (on its own)** | A whole area of work for one user group, such as the RM use case or the credit use case. Not one AI product (say AI product) and not one of the seven lines (say core use case). |
| **User workflow** | How a user group (RMs, portfolio managers) works today, and how that work changes with AI. Not the same as the plans' numbered workflows (B1 to B9 for RMs, B10 to B16 for PMs) on the Workflow Maps. |
| **AI product** | A specific capability we build and release, such as the pre-meeting client brief. Each sits under one core use case. |
| **RM Assistant** | The core RM product (a hypothesis since 2026-10-17): one personal AI assistant for each RM, with limits on its jobs, workflows, data and controls, and capabilities added feature wave by feature wave on a shared foundation (the RM Assistant page). The RM plan's "RM assistant" (wave 3) is now its **Client Q&A** capability. |
| **PM Assistant** | The core portfolio manager product (reviewed and agreed as our working hypothesis on 2026-10-19): one personal AI assistant for each PM, the credit counterpart of the RM Assistant, with the same kinds of limits and capabilities added feature wave by feature wave (The PM Assistant page). It gathers, drafts and flags; the PM writes the judgment and a named credit officer decides. |
| **Capability** | One specific job an assistant does, such as the RM Assistant's pre-meeting client brief or the PM Assistant's borrower file. Each capability is one AI product. |
| **Industry background draft** | The PM Assistant's first capability: the industry background section of a credit memo (the borrower's industry: its size and trend, main drivers and risks, outlook), drafted from approved and licensed sources only, every statement cited and dated, for the PM to edit and approve. It uses no borrower data and writes no judgment about the borrower. An outside firm the bank pays writes this section today (the credit lead, 2026-10-19; ⚠️ details to confirm). |
| **Borrower file** | The PM Assistant's wave 1 capability that gathers everything about one borrower (financials, loans, covenants, deposits, payments, the last review, the RM's notes) in one place, every figure with its source, and a list of what's missing or late. |
| **Early warning flags** | The PM Assistant's feature wave 2 capability: flags on a borrower, with the numbers behind each, for the PM to look at; never a watchlist or rating change. Named so it can't be mistaken for the bank's watchlist. |
| **Signals engine** | Simple, explainable rules that spot opportunities or risks, with AI explaining each one; shared by both assistants. |
| **Must-refuse case** | A test case the product must refuse, such as a request for a credit decision, a borrower risk rating or a price; required on the higher-risk path. |
| **Judgment sections** | The parts of a credit draft only the PM writes: the borrower risk rating and, in wave 1, the recommendation. |
| **Content owner** | The person who signs which documents a product may read, such as the credit file's owner; part of the data contract (sub-step 2.3). |
| **Wave** | Used two ways, so say which: a **feature wave** is a set of AI products released together, after a quick pass through Discover and Define; a **user wave** is the next group of users when a product scales (sub-step 5.7). |
| **Quick pass** | How each new feature wave goes through Discover and Define after the first pass: four sub-steps always done (2.3, 2.4, 2.5, 2.7), the rest reused unless something changed, and gates 1 and 2 decided together in writing (Product Framework). |
| **Material change** | A change to a live product that goes back through step 4: new data, a new action, users outside the full user group step 4 approved, a new AI model we choose, or a vendor model change the vendor announces as major (smaller vendor updates are re-tested in 6.3). User waves inside the approved group aren't material. The product manager proposes and the risk partner confirms; the bank's model risk policy has the final word ⚠️ (Product Framework). |
| **Higher-risk path** | The deeper step 4 review for a product whose output informs a credit decision, such as credit memo drafts: set at sub-step 2.4, under control K3. |
| **Pilot** | The first live use, by a small pilot group, alongside a comparison group. |
| **Comparison group** | Similar users who don't get the product yet, so its effect can be told apart from everything else that changed. |
| **Baseline** | A measure's value before the product, recorded with its date, source and exact definition (sub-step 1.7). |
| **Frozen version** | The exact version reviewers test and approve in step 4. Every fix creates a new frozen version, which is tested again. |
| **Product machine** | The whole system for running products: the six steps, the task tables (in `product-machine.md`, shown on the Product Machine page), the agents and the tracker. |
| **Playbook** | The Product Playbook, the field manual: how to do each sub-step the first time, and what to log so it can be automated later. |
| **First-time log** | The notes kept while doing a sub-step for the first time: start and finish, time spent, what was done, inputs, waits, what repeated, the wait index, and the cut-first and then-automate answers (the fields are in the Product Playbook). Later projects keep a light version (start, finish, hours, waits) so the machine's measures can be counted every time. |
| **Sub-step log** | The log kept for every sub-step on every project: the full first-time log on the first project, then a light version (start, finish, hours, waits). The machine's measures and the wait index come from it. |
| **Automation check** | Seven questions asked of every Me and Draft task at each gate, in order: **cut first** (should it exist, can we delete it, simplify it, make it faster?), **then automate** what's left (did it repeat, is it stable, is it safe alone?). Three yeses to the last three move it one kind toward Auto. Law and bank policy are never cut. |
| **Comes from** | Where a requirement (a control, sub-step or gate) comes from: **law or regulator**, **bank policy** or **our choice**. It says who to ask to change it: the partner who owns the law (compliance, privacy, model risk or vendor risk), the policy's owner or the product manager. |
| **Limiting factor** | The one thing holding a project back right now, with its owner (for example a data contract waiting for a signature). It opens the tracker and the weekly status note. |
| **Wait index** | For a sub-step: calendar days from start to finish, divided by hours of real work, from the sub-step log. A high number means waiting, not working. |
| **Machine measures** | How well the product machine itself works, per project: days from kickoff to pilot, days at each gate, releases per month in the pilot, and the wait index (Product Machine). |
| **Gate in writing** | A gate decided by the decider approving the gate pack in writing, used when every criterion is met; a meeting is held only when a criterion is contested or someone who decides asks for one. |
| **Use case kit** | The standard set of pieces every use case should have, in two layers: the **leader layer** I communicate from (for bank leaders) and the **working layer** I and the team work from. Set by Prompt 1 in the Prompt Library, run first on RMs, and agreed 2026-10-17: 4 leader pieces (the case, the plan on a page, the value, the ask) and 10 working pieces. Cut on 2026-10-18: people get three short pages (an executive summary, the product and the plan), and every working piece goes into one detail document for AI to read (RM Detail for RMs). |
| **Elon mode review** | A review of a plan or of the product machine through Elon Musk's lens (the Elon Mode page): the cut-first questions, the limiting factor and the machine's measures, plus the bank guardrails. |

## People, agents and safeguards

| Term | What it means |
|---|---|
| **Sponsor** | The business leader who owns the outcome and the funding, and makes the call at each gate (together with risk at the step 4 gate). |
| **Product manager** | The person who owns scope, priorities and trade-offs, and owns the product until a long-term owner is named. Always spelled out: "PM" means portfolio manager. |
| **RMs and PMs** | The two user groups the work serves, always written this way: **RM, RMs** for relationship managers and **PM, PMs** for portfolio managers. Spell each out with its short form the first time on a page. An apostrophe shows ownership only ("the RM's own work"). (Decided 2026-10-14.) |
| **Long-term owner** | The person who holds the product after launch, for example someone in a revenue line. Named in Define if known, confirmed before scaling (sub-steps 2.8 and 5.7). |
| **Risk partner** | The model risk person who rates the product and works with the team from day one. **Risk partners** (plural) means everyone who signs off in step 4: model risk, compliance, privacy and security. |
| **Data owner** | The person who decides what data may be used, and signs the data contract. |
| **Champion** | A respected user who shows peers how they use the product. |
| **Kind** | Who does a task: **Auto** (runs on its own), **Draft** (AI drafts, a named person checks), **Me** (only a person) or **Partner** (a decision only a named partner can make, such as a sign-off). |
| **Agent** | An AI helper with one job, a short list of allowed actions and a named person in charge. |
| **Research helper** | An agent that keeps my own reference pages current, such as H1, the bank news scout. Numbered H1 and on, listed in the Agent Library, and not part of the product machine. |
| **General agent** | One of the 33 agents (M1 to M33) that run the product machine on every project, specified in the agent library: M1 to M19 handle the paperwork and routing, M20 to M33 do the team's analysis, testing and monitoring. |
| **Product agent** | An agent inside the product that users see, numbered per project, each number used once across projects (A1, A2, A3 and A5 in the RM plan; A4 was merged into workflow B1 on 2026-10-18 and A6 removed on 2026-10-17; A7 to A11 in the PM plan, from 2026-10-19). Workflows are numbered the same way: B1 to B9 in the RM plan, B10 to B16 in the PM plan. Specified in that project's memo, Appendix A. |
| **Agent spec** | An agent's written definition: its job, inputs, allowed and forbidden actions, outputs, when it stops, proof it worked and the person in charge. |
| **Ongoing mode** | An agent first used once in a sub-step that then keeps running until the product is retired (for example M24 on every data refresh). Agents built to run on a schedule from the start aren't counted as ongoing mode. |
| **Control** | A safeguard built into a product so the bank can trust it (K1 to K25 in the Controls Catalog). Each says where it is set, built, proved and watched, and where it comes from (law or regulator, bank policy or our choice). |
| **Sign-off** | A named partner's formal approval in step 4. Never automated. |
| **Quality bar** | The thresholds a product must meet: accuracy, sources shown, relevance, usefulness and permissions (zero tolerance). Set in Define. |
| **Test set** | Real examples with known good answers, run against every version. |
| **Red-teaming** | Trying on purpose to make the product fail: reveal other users' data, give a credit decision or go off-topic. |
| **Made-up answer** | An answer the AI states confidently that isn't supported by its sources ("hallucination"). |
| **Drift** | Quality slipping over time as data, models or instructions change. |
| **Brief** | The one-page product brief from Define: problem, outcome, users, platform, first-release scope, what's out of scope and the long-term owner. |
| **Backlog** | The ranked list of work still to build, with must-have controls at the top. |
| **User story** | A short "As a [user], I need [what], so that [why]" statement of something to build, with **acceptance criteria** that say how to tell it's done. |
| **Release 1** | The smallest useful first version and the pilot group who get it (sub-step 2.8). |
| **Assistive first** | The AI drafts or suggests and a named person decides. Autonomy grows only with evidence. |
| **Guardrail** | A filter that blocks off-topic answers, harmful content or sensitive data. |
| **Override** | A user changing or rejecting what the AI produced. Tracked as a risk and quality signal. |
| **Monitoring plan** | What is watched after launch, how often, the alert thresholds, who acts, and how to pause the product (sub-step 4.8). |
| **Leading and lagging measures** | Leading measures show up within weeks (use, insights acted on, pipeline created); lagging ones take months (closed revenue). |
| **Data contract** | The signed list of exact fields a product may use, how fresh they must be and the checks they must pass. |
| **The five kinds of measures** | Usage, quality, business impact, adoption, and risk and controls. Set in Define, tracked in Measure. |
| **Value model** | The calculation of what a product earns against what it costs, with unknown numbers shown as [X]. The PM plan's model also counts costs saved and tracks loan losses avoided, not counted until Finance and credit risk agree a method (agreed 2026-10-19). |

## Pages and records

| Term | What it means |
|---|---|
| **Designed page** | A branded page a person reads. Everything a person reads is one. |
| **Working copy** | The Markdown file behind a designed page. people read the page. |
| **Reference page** | A page built to look things up: the Agent Library, Workflow Maps, Steps Catalog, Controls Catalog and this glossary (since 2026-10-18 they are the only pages in the Document Library's Reference section; the pages I read or act on sit elsewhere: the Job Description and Tech Stack Guide in "The bank and the role", the Use Case Library in Research, and Open Items, the Audit Log, the Prompting Guide and the Prompt Library in "My workspace"). RM Detail, in the RM section, and PM Detail, in the PM section, are built automatically for an AI to read, not for people. Claude keeps them aligned; they're never on the review list. |
| **Gate pack** | Everything the decider needs at a gate, put together in one document. |
| **Evidence pack** | Everything reviewers sign in step 4: the outputs of 4.1 to 4.6 (risk rating, data and privacy review, test and red-team results, fairness, controls and vendor reviews) and the draft monitoring plan (4.8). |
| **Decision log** | The record of each decision: what was decided, the options, who decided and why. For gates it also records the date the gate pack was ready and the decision date. |
| **Risk and issue list** | The one list of a project's dependencies, risks and issues, each with an owner and a date, reviewed weekly. Its top item is the limiting factor. |
| **Project file** | The project's working document (`memos/<project>.md`), created at kickoff (1.0): the plan, the who-decides list and the approved AI tools. People read the short pages built from it; the full file goes into the project's detail document for AI. |
| **Automation review** | The table at the end of each playbook step that lists each sub-step's agent (or None) with its first-time kind and the kind to aim for; at the gate, the automation check runs through it. |
| **Tracker** | The one task list for a project (its section of the one shared tracker): each task with its owner, date and status. |
| **Open item** | Anything unfinished, kept in the Open Items log and numbered in priority order within its kind (W1 is the first piece of work). Numbers change when priorities change; closed items (C) keep theirs. |

## Words we don't use

The audit flags these in the core documents. Use the word on the right.

| Don't say | Say instead | Why |
|---|---|---|
| product owner | product manager, or long-term owner | Two different roles; "product owner" blurs them. |
| control group | comparison group | One name for one idea. |
| phase | step | Our process has steps, each ending in a gate. |
| stage gate | gate | One name for one idea. |
| signoff | sign-off | One spelling. |
| cohort | pilot group, or comparison group | Say which group. |
| risk contact | risk partner | One name for one role. |

## Old wording we've retired

An editing aid: when we rename something or change a count, the old wording goes here, so no page keeps an outdated name. The
audit checker fails on any of it left in a core document, a memo, NOW.md, the
working copy of a designed page, the Document Library or the RM Assistant Plan page, so a rename can't stop halfway. A line
that also says the new wording (a note about the change) is allowed.

| Retired wording | Use instead | Retired on |
|---|---|---|
| five core use cases | seven core use cases | 2026-10-10 |
| stop each use case | stop each AI product | 2026-10-10 |
| stop each feature | stop each AI product | 2026-10-10 |
| wave 1 use cases | wave 1 AI products | 2026-10-10 |
| Each use case, step by step | Each AI product, step by step | 2026-10-10 |
| machine agent | general agent | 2026-10-10 |
| Six-step workflow visual | Product Workflow | 2026-10-10 |
| Six-Step Product Workflow | Product Workflow (the page name) | 2026-10-14 |
| Delivery Machine | Product Machine (the page name; "product machine" for the whole system) | 2026-10-14 |
| Delivery Playbook | Product Playbook (the page name) | 2026-10-14 |
| Agent idea: | Agent: (with the agent's M number) | 2026-10-10 |
| (spec M | (agent library) | 2026-10-10 |
| 19-agent library | the agent library (33 general agents) | 2026-10-10 |
| McKinsey Use Cases | Use Case Library (the page name since 2026-10-18) | 2026-10-14 |
| Credit Market Scan | the Use Case Library's portfolio manager section (since 2026-10-18) | 2026-10-14 |
| Credit Core Use Cases | the Use Case Library's portfolio manager section (since 2026-10-18) | 2026-10-14 |
| Credit user workflow | Portfolio manager user workflow (the page name) | 2026-10-14 |
| Product manager (PM | product manager (spelled out; PM means portfolio manager) | 2026-10-14 |
| one PM runs | one product manager runs | 2026-10-14 |
| PM and sponsor | product manager and sponsor | 2026-10-14 |
| PM sets priorities | product manager sets priorities | 2026-10-14 |
| PM and platform team | product manager and platform team | 2026-10-14 |
| the PM's hours | the product manager's hours | 2026-10-14 |
| Scale in waves | Scale in user waves (sub-step 5.7; say which kind of wave) | 2026-10-15 |
| written gate | gate in writing | 2026-10-15 |
| risk/issue list | risk and issue list | 2026-10-15 |
| How We Deliver Audit | Audit Log (the page name) | 2026-10-15 |
| Elon Mode Research | Elon Mode (the page name; it sits in the library's Research section) | 2026-10-15 |
| RM Analytics Plan | RM Assistant Plan (the page name) | 2026-10-17 |
| RM Product Information for AI | RM Detail (the page name; it sits in the RM section) | 2026-10-18 |
| three-question check | the automation check (seven questions: cut first, then automate) | 2026-10-15 |

## Bank terms to map

Our plans depend on these, but the definitions belong to the bank. Each stays
⚠️ until the bank's own definition is recorded here, with its source.

| Term | How our plans use it today | Bank definition |
|---|---|---|
| Relationship manager (RM) | The banker who owns business client relationships and brings in new deals | ⚠️ to map |
| Portfolio manager (PM) | The credit partner paired with an RM. Associated's own job postings use this title (AVP to SVP) for the role that underwrites, monitors credit and partners closely with RMs (seen on job boards, 2026-10-14) | ⚠️ to map |
| Credit officer | The person with credit authority who makes a credit decision that an AI draft or flag informs (control K3); it may be the portfolio manager or a credit approver | ⚠️ to map |
| Treasury management officer | The specialist an RM refers clients to for payments and cash management | ⚠️ to map |
| Client, relationship | A business client and everything the bank does with it | ⚠️ to map |
| Segment and market | How clients and bankers are grouped (for example, by size or region) | ⚠️ to map |
| AI-sourced opportunity | An opportunity in the CRM that started from an AI insight, tagged so results can be counted | ⚠️ to map |
| Complete credit request | The date a credit request has everything needed for a decision, the start of the PM plan's turnaround measure | ⚠️ to map |
| Win rate | The share of opportunities that close as won | ⚠️ to map |
| First-year revenue per win | The revenue a won deal brings in its first year | ⚠️ to map |
| Active user (weekly) | A user who used the product in a given week | ⚠️ to map |
| Client-facing time | Time a banker spends with clients rather than on admin or internal work | ⚠️ to map |
| Product gap | A product a client would likely need but doesn't have with the bank | ⚠️ to map |
| Referral | One banker passing a client need to another team | ⚠️ to map |
| Certified data | Data the bank has approved as trusted for use | ⚠️ to map |
| Risk rating (of an AI use) | The level the bank's model risk process assigns to an AI use | ⚠️ to map |
| Model inventory | The bank's register of models and AI uses | ⚠️ to map |
| Qualified opportunity | An opportunity good enough to count in the value model ("qualified opportunities surfaced per RM") | ⚠️ to map |
| Pipeline, closed won | Open opportunities, and opportunities that closed as won | ⚠️ to map |
| RMs in scope, book size | How many RMs a product covers, and how many clients each RM covers | ⚠️ to map |
| Hours saved | Time a product frees up each week, and how it's measured (Finance agrees the method) | ⚠️ to map |
| Client attrition, at-risk client | A client who leaves or reduces business, and early signs that one might | ⚠️ to map |
| Borrower risk rating | The bank's credit grade of a borrower; not the model risk rating of an AI use | ⚠️ to map |
| Annual review | The yearly credit review of a borrower | ⚠️ to map |
| Credit memo | The written case for a credit decision | ⚠️ to map |
| Credit file | Everything the bank keeps on a borrower's credit | ⚠️ to map |
| Spread, spreading tool | A borrower's financial statements put into the bank's standard layout, and the tool that does it | ⚠️ to map |
| Covenant, compliance certificate | A condition a borrower agrees to in its loan, and the borrower's signed statement that it meets them | ⚠️ to map |
| Watchlist | The bank's own list of borrowers under closer watch; our early warning flags are separate | ⚠️ to map |
| Credit policy, credit appetite | The bank's credit rules, and the kinds and amount of credit risk it is willing to take | ⚠️ to map |
| Approval-authority list | Who may approve which credit decisions, and up to what size | ⚠️ to map |
| Credit administration | The team that books, documents and services loans | ⚠️ to map |
| Credit risk, credit risk review | The team that owns credit risk, and its independent review of loans | ⚠️ to map |
| Credit analyst | The person who spreads statements and drafts credit analysis for a portfolio manager | ⚠️ to map |
| Renewal, line change | Extending a loan or line when it matures, and changing its size or terms | ⚠️ to map |
| Loan system | The bank's system of record for loans | ⚠️ to map |

_Last updated: 2026-10-19_
