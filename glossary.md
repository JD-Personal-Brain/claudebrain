# Glossary: the words we use

One meaning for each word, used the same way in every plan, playbook page and
agent spec. Claude loads this every session, and the audit checks the core
documents against it.

> **Two kinds of terms.** The first two sections are our own working words for
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
| **Core use case** | One of the seven lines a plan is organized on. The RM plan set them: McKinsey's five frontline use cases (prospecting and next best opportunities, lead nurturing, account intelligence and meeting prep, deal scoring and pricing, AI sales coaching) plus two of our own (admin off the RM's plate, keep clients). The credit work reuses the same seven lines through each one's credit counterpart. Say **RM core use case** or **credit core use case** when it matters which. Each has a user problem and a return profile. |
| **Credit counterpart** | The credit-side version of an RM core use case, for portfolio managers and credit analysts; for example, credit memo and annual review drafts under account intelligence and meeting prep (see the Credit Core Use Cases page). |
| **Use case (on its own)** | A whole area of work for one user group, such as the RM use case or the credit use case. Not one AI product (say AI product) and not one of the seven lines (say core use case). |
| **User workflow** | How a user group (RMs, the credit team) works today, and how that work changes with AI. Not the same as the RM plan's numbered workflows B1 to B9 on the Workflow Maps. |
| **AI product** | A specific capability we build and release, such as the pre-meeting brief. Each sits under one core use case. |
| **Wave** | Used two ways, so say which: a **feature wave** is a set of AI products released together, after a quick pass through Discover and Define; a **user wave** is the next group of users when a product scales (sub-step 5.7). |
| **Pilot** | The first live use, by a small pilot group, alongside a comparison group. |
| **Comparison group** | Similar users who don't get the product yet, so its effect can be told apart from everything else that changed. |
| **Baseline** | A measure's value before the product, recorded with its date, source and exact definition (sub-step 1.7). |
| **Frozen version** | The exact version reviewers test and approve in step 4. Every fix creates a new frozen version, which is tested again. |
| **Delivery machine** | The whole system for running products: the six steps, the task tables in the product framework, the agents and the tracker. |
| **Playbook** | The field manual: how to do each sub-step the first time, and what to log so it can be automated later. |
| **First-time log** | The notes kept while doing a sub-step for the first time: time spent, waits, inputs and what repeated. |
| **Automation check** | Three questions asked of every Me and Draft task at each gate: did it repeat, is it stable, is it safe alone? Three yeses move it one kind toward Auto. |

## People, agents and safeguards

| Term | What it means |
|---|---|
| **Sponsor** | The business leader who owns the outcome and the funding, and makes the call at each gate (together with risk at the step 4 gate). |
| **Product manager** | The person who owns scope, priorities and trade-offs, and owns the product until a long-term owner is named. |
| **Long-term owner** | The person who holds the product after launch, for example someone in a revenue line. Named in Define if known, confirmed before scaling (sub-steps 2.8 and 5.7). |
| **Risk partner** | The model risk contact who rates the product and works with the team from day one. **Risk partners** (plural) means everyone who signs off in step 4: model risk, compliance, privacy and security. |
| **Data owner** | The person who decides what data may be used, and signs the data contract. |
| **Champion** | A respected user who shows peers how they use the product. |
| **Kind** | Who does a task: **Auto** (runs on its own), **Draft** (AI drafts, a named person checks), **Me** (only a person) or **Partner** (a sign-off only a named partner can give). |
| **Agent** | An AI helper with one job, a short list of allowed actions and a named person in charge. |
| **General agent** | One of the 33 agents (M1 to M33) that run the delivery machine on every project, specified in the agent library: M1 to M19 handle the paperwork and routing, M20 to M33 do the team's analysis, testing and monitoring. |
| **Product agent** | An agent inside the product that users see, numbered per project (A1 to A6 in the RM plan). Specified in that project's memo, Appendix A. |
| **Agent spec** | An agent's written definition: its job, inputs, allowed and forbidden actions, outputs, when it stops, proof it worked and the person in charge. |
| **Ongoing mode** | An agent that keeps running after launch, not just once (for example M24 on every data refresh). |
| **Control** | A safeguard built into a product so the bank can trust it (K1 to K25 in the Controls Catalog). Each says where it is set, built, proved and watched. |
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
| **Value model** | The calculation of what a product earns against what it costs, with unknown numbers shown as [X]. Savings may be added with the credit use case. |

## Pages and records

| Term | What it means |
|---|---|
| **Designed page** | A branded page a person reads. Everything a person reads is one. |
| **Working copy** | The Markdown file behind a designed page. Claude edits it; people read the page. |
| **Reference page** | A page built to look things up: the Agent Library, Workflow Maps, Steps Catalog, Controls Catalog and this glossary (the Document Library's Reference section also lists the Tech Stack Guide, a guide I read). Claude keeps them aligned; they're never on the review list. |
| **Gate pack** | Everything the decider needs at a gate, put together in one document. |
| **Evidence pack** | Everything reviewers sign in step 4: the outputs of 4.1 to 4.6 (risk rating, data and privacy review, test and red-team results, fairness, controls and vendor reviews). |
| **Decision log** | The record of each decision: what was decided, the options, who decided and why. |
| **Tracker** | The one task list for a project: each task with its owner, date and status. |
| **Open item** | Anything unfinished, kept in the Open Items log with a number that never changes. |

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

## Old wording we've retired

When we rename something or change a count, the old wording goes here. The
audit checker fails on any of it left in a core document, a memo, NOW.md, the
working copy of a designed page, the Document Library, the scrolling RM plan or
the design canvas, so a rename can't stop halfway. A line
that also says the new wording (a note about the change) is allowed.

| Retired wording | Use instead | Retired on |
|---|---|---|
| five core use cases | seven core use cases | 2026-10-10 |
| stop each use case | stop each AI product | 2026-10-10 |
| stop each feature | stop each AI product | 2026-10-10 |
| wave 1 use cases | wave 1 AI products | 2026-10-10 |
| Each use case, step by step | Each AI product, step by step | 2026-10-10 |
| machine agent | general agent | 2026-10-10 |
| Six-step workflow visual | Six-Step Product Workflow | 2026-10-10 |
| Agent idea: | Agent: (with the agent's M number) | 2026-10-10 |
| (spec M | (agent library) | 2026-10-10 |
| 19-agent library | the agent library (33 general agents) | 2026-10-10 |
| McKinsey Use Cases | RM Core Use Cases (the page name) | 2026-10-14 |
| Credit Market Scan | Credit Core Use Cases (the page name) | 2026-10-14 |

## Bank terms to map

Our plans depend on these, but the definitions belong to the bank. Each stays
⚠️ until the bank's own definition is recorded here, with its source.

| Term | How our plans use it today | Bank definition |
|---|---|---|
| Relationship manager (RM) | The banker who owns business client relationships and brings in new deals | ⚠️ to map |
| Portfolio manager | The credit partner paired with an RM | ⚠️ to map |
| Treasury management officer | The specialist an RM refers clients to for payments and cash management | ⚠️ to map |
| Client, relationship | A business client and everything the bank does with it | ⚠️ to map |
| Segment and market | How clients and bankers are grouped (for example, by size or region) | ⚠️ to map |
| AI-sourced opportunity | An opportunity in the CRM that started from an AI insight, tagged so results can be counted | ⚠️ to map |
| Win rate | The share of opportunities that close as won | ⚠️ to map |
| First-year revenue per win | The revenue a won deal brings in its first year | ⚠️ to map |
| Active user (weekly) | A user who used the product in a given week | ⚠️ to map |
| Client-facing time | Time a banker spends with clients rather than on admin or internal work | ⚠️ to map |
| Product gap | A product a client would likely need but doesn't have with the bank | ⚠️ to map |
| Referral | One banker passing a client need to another team | ⚠️ to map |
| Certified data | Data the bank has approved as trusted for use | ⚠️ to map |
| Risk rating | The level the bank's model risk process assigns to an AI use | ⚠️ to map |
| Model inventory | The bank's register of models and AI uses | ⚠️ to map |
| Qualified opportunity | An opportunity good enough to count in the value model ("qualified opportunities surfaced per RM") | ⚠️ to map |
| Pipeline, closed won | Open opportunities, and opportunities that closed as won | ⚠️ to map |
| RMs in scope, book size | How many RMs a product covers, and how many clients each RM covers | ⚠️ to map |
| Hours saved | Time a product frees up each week, and how it's measured (Finance agrees the method) | ⚠️ to map |
| Client attrition, at-risk client | A client who leaves or reduces business, and early signs that one might | ⚠️ to map |

_Last updated: 2026-10-14_
